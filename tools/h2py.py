import clang.cindex as CC
import typing as t

import io
import os

class HeaderParser:
    class StructureHolder:
        fields: dict[str, t.Any]
    
    c_type_to_ctypes_map = {
        'int': 'c_int',
        'unsigned int': 'c_uint',
        'short': 'c_short',
        'unsigned short': 'c_ushort',
        'long': 'c_long',
        'unsigned long': 'c_ulong',
        'long long': 'c_longlong',
        'unsigned long long': 'c_ulonglong',
        'float': 'c_float',
        'double': 'c_double',
        'char': 'c_char',
        'wchar_t': 'c_wchar',
        'bool': 'c_bool',
        'void': 'None',
        'size_t': 'c_size_t',
        'ssize_t': 'c_ssize_t',
        'int8_t': 'c_int8',
        'uint8_t': 'c_uint8',
        'int16_t': 'c_int16',
        'uint16_t': 'c_uint16',
        'int32_t': 'c_int32',
        'uint32_t': 'c_uint32',
        'int64_t': 'c_int64',
        'uint64_t': 'c_uint64',
    }
    
    c_type_to_py_types = {
        'int': 'int',
        'unsigned int': 'int',
        'short': 'int',
        'unsigned short': 'int',
        'long': 'int',
        'unsigned long': 'int',
        'long long': 'int',
        'unsigned long long': 'int',
        'float': 'float',
        'double': 'float',
        'char': 'int',
        'wchar_t': 'str',
        'bool': 'bool',
        'void': 'None',
        'OLECHAR *': 'LPWSTR',
        'WCHAR *': 'LPWSTR',
        'wchar_t *': 'LPWSTR',
        'char *': 'LPSTR',
        'CHAR *': 'LPSTR',
        'LPCSTR': 'LPSTR',
        'LPCWSTR': 'LPWSTR',
        'LPSTR': 'LPSTR',
        'LPWSTR': 'LPWSTR',
    }
    
    string_types = {
        'LPWSTR', 'LPCWSTR', 'OLECHAR *', 'WCHAR *', 'wchar_t *',
        'LPSTR', 'LPCSTR', 'char *', 'CHAR *'
    }
    
    typedefs: dict[str, str] = {}
    
    py_code: io.TextIOWrapper
    header_path: str
    library: str
    
    def recursive_get_typedef(self, typedef: str) -> str:
        if typedef in self.typedefs:
            base_type = self.typedefs[typedef]
            if base_type == typedef:
                return typedef
            return self.recursive_get_typedef(base_type)
        return typedef
    
    def _clean_type(self, c_type: str) -> tuple[str, str]:
        c_type = c_type.strip()
        
        while c_type.startswith('const '):
            c_type = c_type[6:].strip()
        
        pointer_level = 0
        while c_type.endswith('*'):
            c_type = c_type[:-1].rstrip()
            pointer_level += 1
        while c_type.endswith('&'):
            c_type = c_type[:-1].rstrip()
            pointer_level += 1
        
        return c_type, '*' * pointer_level
    
    def c_type_to_ctypes(self, c_type: str) -> str:
        base_type, pointer_level = self._clean_type(c_type)
        
        base_type = self.recursive_get_typedef(base_type)
        
        if base_type in self.c_type_to_ctypes_map:
            ctypes_type = self.c_type_to_ctypes_map[base_type]
        else:
            ctypes_type = base_type
        
        if pointer_level == '*':
            if base_type in self.string_types or 'char' in base_type.lower():
                if 'wchar' in base_type.lower() or 'WCHAR' in base_type or 'OLECHAR' in base_type:
                    return 'LPWSTR'
                else:
                    return 'LPSTR'
            else:
                return f'POINTER({ctypes_type})'
        elif pointer_level == '**':
            return f'POINTER(POINTER({ctypes_type}))'
        elif len(pointer_level) > 2:
            return 'c_void_p'
        
        return ctypes_type
    
    def c_type_to_py(self, c_type: str) -> str:
        base_type, pointer_level = self._clean_type(c_type)
        
        base_type = self.recursive_get_typedef(base_type)
        
        full_type = base_type + pointer_level if pointer_level else base_type
        if full_type in self.c_type_to_py_types:
            return self.c_type_to_py_types[full_type]
        
        if base_type in self.c_type_to_py_types:
            py_type = self.c_type_to_py_types[base_type]
        else:
            py_type = base_type
        
        if pointer_level == '*':
            if 'char' in base_type.lower():
                if 'wchar' in base_type.lower() or 'WCHAR' in base_type or 'OLECHAR' in base_type:
                    return 'LPWSTR'
                else:
                    return 'LPSTR'
            return f'IPointer[{py_type}]'
        elif pointer_level == '**':
            return f'IDoublePtr[{py_type}]'
        elif len(pointer_level) > 2:
            raise RuntimeError()
        
        return py_type
    
    def __init__(self, header_path: str):
        py_name = os.path.splitext(os.path.basename(header_path))[0] + '.py'
        self.py_code = open(py_name, 'w', encoding='utf-8')
        self.header_path = header_path
        self.library = ''
        
    def __del__(self):
        self.close()
        
    def close(self):
        if not self.py_code.closed:
            self.py_code.close()
            
    cursor: CC.Cursor
    
    def header_parse(self):
        index: CC.Index = CC.Index.create()
        tu: CC.TranslationUnit = index.parse(self.header_path, ['-x', 'c++', '--std=c++11'])
        
        for diag in tu.diagnostics:
            print(f'[Diag] #{diag.severity} {diag.location}: {diag.spelling}')
        
        self.cursor = tu.cursor
            
    def ast_parse(self):
        for cursor in self.cursor.walk_preorder():
            kind: CC.CursorKind = cursor.kind
            location: CC.SourceLocation = cursor.location
            
            if kind.is_declaration():
                if location.file.name == self.header_path:
                    if kind.name == 'FUNCTION_DECL':
                        foreign_string: str
                        
                        if self.library == '':
                            foreign_string = '@foreign('
                        else:
                            foreign_string = f'@{self.library}.foreign('
                        
                        arguments = cursor.get_arguments()
                        argument: CC.Cursor
                        
                        result_type: CC.Type = cursor.result_type
                        foreign_arguments = [self.c_type_to_ctypes(result_type.spelling)]
                        foreign_py_result = self.c_type_to_py(result_type.spelling)
                        foreign_py = []
                        
                        for argument in arguments:
                            argument_type: CC.Type = argument.type
                            foreign_arguments.append(self.c_type_to_ctypes(argument_type.spelling))
                            foreign_py.append(f'{argument.spelling}: {self.c_type_to_py(argument_type.spelling)}')
                            
                        foreign_string += ', '.join(foreign_arguments) + ')\n'
                        foreign_string += f'def {cursor.spelling}('
                        foreign_string += ', '.join(foreign_py) + f') -> {foreign_py_result}: ...\n\n'
                        
                        self.py_code.write(foreign_string)
                else:
                    if kind.name == 'TYPEDEF_DECL':
                        typedef_type: CC.Type = cursor.underlying_typedef_type
                        self.typedefs[cursor.spelling] = typedef_type.spelling
                    elif kind.name == 'STRUCT_DECL':
                        spelling: str = cursor.spelling
                        self.typedefs[spelling] = spelling.split()[-1]