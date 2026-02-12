#
# com/icl/wicl/parser.py
#
# WICL generator parser internal realization
#

from ....iml.imldef import *
from .codegen import *

import time
import os

class ICLParser(IIMLParser):
    class ICLContext(IIMLContext):
        external_function_count: int
        last_defined_interface: str
        in_gencommentlw_block: bool
        declaring_structure: str
        declaring_class: bool
        enum_entry_count: int
        declaring_enum: str
        function_count: int
        commentext: str
        silent: bool
        docs: str
        base: str
        py: bool
        
        def on_initialize(self):
            self.in_gencommentlw_block = False
            self.external_function_count = 0
            self.last_defined_interface = ''
            self.declaring_structure = ''
            self.declaring_class = False
            self.enum_entry_count = 0
            self.declaring_enum = ''
            self.function_count = 0
            self.commentext = ''
            self.silent = False
            self.py = False
            self.docs = ''
            self.base = ''
            
    context_type = ICLContext
    context: ICLContext
        
    TYPE_MAP = {
        'INT': 'int', 'DWORD': 'int', 'WORD': 'int',
        'SHORT': 'int', 'USHORT': 'int', 'UINT': 'int',
        'INT_PTR': 'int', 'UINT_PTR': 'int', 'LONG_PTR': 'int',
        'ULONG_PTR': 'int', 'HRESULT': 'int', 'ULONG': 'int',
        'LONG': 'int', 'void': '', 'BOOL': 'bool', 'VOID': ''
    }
    POINTER_MAP = {
        'IUnknown': 'LPUNKNOWN', 'IEnumString': 'LPENUMSTRING',
        'IStream': 'LPSTREAM', 'IMalloc': 'LPMALLOC', 
        'IMallocSpy': 'LPMALLOCSPY', 'CLSID': 'LPCLSID',
        'IID': 'LPIID', 'GUID': 'LPGUID', 'VOID': 'PVOID',
        'void': 'PVOID'
    }
    
    SUGAR = {'{'}
    VERSION = '100'
    
    file: TextIOWrapper
    code: Code
        
    def parse_arguments(self, decorator_args: List[str],
                        decorator_named_args: List[str], 
                        args: List[Tuple[str, str]],
                        disp: int, has_refs: Ref[bool], 
                        refs: List[Tuple[int, str]]):
        for i in range((self.context.tokens_length - disp) // 2):
            i *= 2
            arg_name = self.context.tokens[disp+i]
            arg_type = self.context.tokens[disp+i+1]
            params = arg_type.split('.')
            type_name = params.pop()
            orig_type_name = type_name
            params = [param.lower() for param in params]
            ptr_count = params.count('p')
            forward_decl = 'fd' in params
            is_ref = 'r' in params
            if is_ref:
                if arg_name.startswith('r'):
                    arg_name = arg_name[1:]
                refs.append((i//2, arg_name))
                ptr_count += 1
            if is_ref and not has_refs.value:
                decorator_named_args.append(('intermediate_method', 'True'))
                has_refs.value = True
                
            if ptr_count != 0:
                if ptr_count > 2:
                    self.syntax_error('3+ pointers at the same time not supported.')
            
                ptr_type = 'IPointer' if ptr_count == 1 else 'IDoublePtr'
                ptr_type += '['
                if forward_decl:
                    ptr_type += f"'{type_name}'"
                else:
                    ptr_type += type_name
                ptr_type += ']'
                
                if not forward_decl:
                    if orig_type_name == 'PVOID':
                        decorator_args.append('PVOID')
                    else:
                        if ptr_count == 2:
                            if type_name in self.POINTER_MAP:
                                type_name = f'PTR({self.POINTER_MAP[type_name]})'
                            else: type_name = f'DOUBLE_PTR({type_name})'
                        else:
                            type_name = self.POINTER_MAP.get(
                                type_name, f'PTR({type_name})')
                    decorator_args.append(type_name)
                else:
                    decorator_args.append('PVOID')
                type_name = ptr_type
            else:
                if forward_decl:
                    type_name = f"'{type_name}'"
                decorator_args.append(type_name)
                type_name = self.TYPE_MAP.get(type_name, type_name)
            if is_ref:
                type_name = orig_type_name
            
            args.append((arg_name, type_name))
        
    def new_function(self, has_refs: Ref[bool], function_name: str,
                     result_type: str, args: List[str], decorator_name: str,
                     decorator_args: List[str], decorator_named_args: List[str],
                     refs: List[str], is_foreign: bool = False):
        if self.context.silent: return
        
        self.code.append_decorator(decorator_name, decorator_args, decorator_named_args)
        if len(self.context.docs) != 0:
            self.code.append_function(function_name, result_type, args, [], kwargs=has_refs, has_body=True)
            
            indents = self.indented
            self.context.docs = self.context.docs.replace('\n', indents)
            self.code.append(f'{indents}"""')
            self.code.append(self.context.docs, not_breakline=True)
            self.code.append(f'{indents}"""')
        elif has_refs:
            self.code.append_function(function_name, result_type, args, [], kwargs=has_refs, has_body=True)
            
            delegate_args = []
            for i, name_type in enumerate(args):
                if not is_foreign:
                    if i == 0: continue
                arg, _ = name_type
                for j, ref in refs:
                    if i == j:
                        arg = ref + '.ref()'
                delegate_args.append(arg)
                
            if is_foreign:
                self.code.append_external_delegate(delegate_args)
            else:
                self.code.append_virtdelegate(delegate_args)
        else:
            self.code.append_function(function_name, result_type, args, [])
            
    @property
    def indents(self) -> str:
        return self.code.make_indents()
    
    @property
    def indented(self) -> str:
        return self.code.make_indents()+self.code.INDENT
    
    def on_initialize(self):
        self.code = Code(os.path.splitext(self.file.name)[0] + '.py')
        
    def on_parse_ended(self):
        if self.context.in_gencommentlw_block:
            self.code.append_comment('}')
        self.code.file.close()
        
    def on_line(self, line: str, lineno: int) -> str:
        if lineno == 0:
            if not line.startswith('.icl'):
                self.syntax_error('ICL Header is corrupted. ', 1)
            return None

        line = line.strip()
            
        return line
    
    def on_tokens_defined(self):
        if self.context.tokens_length == 0:
            if self.context.py:
                self.code.append_newline()
    
    def on_instruction(self, instruction: str) -> bool:
        if self.context.py:
            if instruction == '}':
                self.context.py = False
            elif instruction != '{':
                self.code.append(self.context.last_line)
                self.code.indent()
            return True

        if self.context.last_line.startswith('~'):
            self.code.append(self.context.last_line[1:])
            return True
        
        if instruction == '.ver':
            if self.context.tokens[1] != self.VERSION:
                self.syntax_error(f'ICL Version is not {self.VERSION}. Update the ICL File.', 
                                  len(instruction) + 2)
        elif instruction == 'I':
            self.define_interface()
        elif instruction == '}':
            if not self.generic_end():
                self.interface_end()
        elif instruction == 'ie':
            self.interface_end()
        elif instruction in self.SUGAR: pass
        elif instruction in ('.inc', '.incl'):
            self.include()
        elif instruction == 'iid':
            if not self.context.silent:
                self.iid()
        elif instruction == 'cf':
            if not self.context.silent:
                self.com_function()
        elif instruction == 'vf':
            if not self.context.silent:
                self.virtual_function()
        elif instruction == 'pi':
            self.pointer_interface()
        elif instruction == 'pie':
            self.pointer_explicit()
        elif instruction == 'sd':
            self.structure_define()
        elif instruction == 'sf':
            if not self.context.silent:
                self.structure_field()
        elif instruction == 'ed':
            self.enum_define()
        elif instruction == 'ee':
            if not self.context.silent:
                self.enum_entry()
        elif instruction == 'silent':
            self.context.silent = True
        elif instruction == 'py':
            self.context.py = True
        elif instruction == 'al':
            self.alias()
        elif instruction == '.gencomment':
            if not self.context.silent:
                self.gencomment()
        elif instruction == '.gencommentlw':
            if not self.context.silent:
                self.gencommentlw()
        elif instruction in ('.commentext', '.commext'):
            self.context.commentext += self.context.last_line[len(instruction):].lstrip()+'\n'
        elif instruction == 'ff':
            if not self.context.silent:
                self.foreign_function()
        elif instruction in ('oleff', 'oleautff', 'oleaccff') :
            if not self.context.silent:
                self.foreign_function_lib(instruction)
        elif instruction == 'doc':
            self.context.docs += self.context.last_line[3:].lstrip()+'\n'
        elif instruction == 'eq':
            if not self.context.silent:
                self.equal()
        elif instruction == 'dg':
            if not self.context.silent:
                self.define_guid()
        elif instruction == 'dii':
            if not self.context.silent:
                self.define_guid('IID')
        elif instruction == 'dcl':
            if not self.context.silent:
                self.define_guid('CLSID')
        elif instruction == 'IU':
            self.define_interface_unknown()
        elif instruction == 'C':
            if not self.context.silent:
                self.define_coclass()
        elif instruction == 'clsid':
            if not self.context.silent:
                self.clsid()
        else:
            return False
        return True
    
    def define_interface(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of interface, '
                            'missing interface name.', 3)
        interface_name = self.context.tokens[1]
        self.context.base = ''
        if self.context.tokens_length > 2:
            token = self.context.tokens[2]
            if token != 'ex':
                self.syntax_error(f'Unknown token "{token}".', len(interface_name)+4)
            
            if self.context.tokens_length == 2:
                self.syntax_error('Incorrect declaration of interface base,'
                                'missing base interface name.', len(interface_name)+6)
            
            self.context.base = self.context.tokens[3]
        
        if not self.context.silent:
            self.code.append_class(interface_name, self.context.base)
            self.code.indent()
            if self.context.base != '':
                self.code.append_field('virtual_table',
                                    value=f"COMVirtualTable.from_ancestor({self.context.base})")
            else:
                self.code.append_field('virtual_table', value=f"COMVirtualTable('{interface_name}')")
        
        self.context.last_defined_interface = interface_name
        
    def generic_end(self) -> bool:
        if self.context.silent:
            self.context.silent = False
            return True
        elif self.context.declaring_enum:
            self.code.append(f'{self.context.declaring_enum} = INT')
            self.code.append_newline()
            self.context.declaring_enum = ''
            self.context.enum_entry_count = 0
            return True
        elif self.context.declaring_structure:
            self.context.declaring_structure = ''
            self.code.unindent()
            self.code.append_newline()
            return True
        elif self.context.declaring_class:
            self.context.declaring_class = False
            self.code.unindent()
            self.code.append_newline()
            return True
        return False
        
    def interface_end(self):
        if self.context.base == '':
            self.code.append_field('_fields_', value='virtual_table.build()')
        else:
            self.code.append(f'{self.indents}virtual_table.build()\n')
        self.code.unindent()
        self.context.function_count = 0
        
    def include(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect usage of ".inc(l)" instruction,'
                                'missing ICL file name.')
            
        include_filepath = self.context.tokens[1]
            
        self.file = open(include_filepath, 'r', encoding='utf-8')
        os.chdir(os.path.join(os.curdir, os.path.dirname(include_filepath)))
        cached_code = self.code.file
        cached_cwd = os.getcwd()
        cached_file = self.file
        
        self.code.file = open(os.devnull, 'w')
        self.parse()
        
        os.chdir(cached_cwd)
        self.code.file.close()
        self.file.close()
        
        self.code.file = cached_code
        self.file = cached_file
        
    def iid(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect usage of "iid" instruction,'
                            'missing IID.', len(self.context.last_line)+1)
        
        iid = self.context.tokens[1]
        self.code.append_field('_iid_', value='IID("{'+iid+'}")')
            
    def com_function(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of COM function,'
                            'missing function name', len(self.context.last_line)+1)
        self.context.function_count += 1
        if self.context.function_count == 1 and not self.context.silent:
            self.code.append_newline()
        
        com_name = self.context.tokens[1]
        decorator_args = []
        decorator_named_args = []
        has_refs: Ref[bool] = Ref(bool)
        args = [('self', '')]
        refs = []
        if self.context.tokens_length > 2:
            if (self.context.tokens_length % 2) != 0:
                self.syntax_error('Incorrect declaration of COM function, '
                                'missing one of argument components '
                                '(tokens count is not even)', len(com_name)+5)
            
            self.parse_arguments(decorator_args, decorator_named_args, args, 2, has_refs, refs)
        
        self.new_function(has_refs, com_name, 'int', args, 
                          'virtual_table.com_function', 
                          decorator_args, decorator_named_args,
                          refs)
        if len(self.context.docs) != 0: self.context.docs = ''
        
    def virtual_function(self):
        if self.context.tokens_length < 3:
            self.syntax_error('Incorrect declaration of virtual function, '
                            'missing result type, function name and arguments', len(self.context.last_line)+1)
        
        self.context.function_count += 1
        if self.context.function_count == 1 and not self.context.silent:
            self.code.append_newline()
        function_name = self.context.tokens[1]
        result_type = self.context.tokens[2]
        decorator_args = [result_type]
        decorator_named_args = []
        has_refs: Ref[bool] = Ref(bool)
        if result_type == 'BOOL':
            result_type = 'bool'
            decorator_named_args.append(('result_function', 'bool'))
        result_type = self.TYPE_MAP.get(result_type, result_type)
        args = [('self', '')]
        refs = []
        if self.context.tokens_length > 3:
            if ((self.context.tokens_length-3) % 2) != 0 or self.context.tokens_length == 4:
                self.syntax_error('Incorrect declaration of virtual function,'
                                'missing one of argument components '
                                '(tokens count is not even or == 4)', 
                                len(function_name)+len(result_type)+5)
            
            
            self.parse_arguments(decorator_args, decorator_named_args, args, 3, has_refs, refs)
        
        self.new_function(has_refs, function_name, result_type, args, 
                          'virtual_table.function', decorator_args, 
                          decorator_named_args, refs)
        if len(self.context.docs) != 0: self.context.docs = ''
        
    def pointer_interface(self):
        pointer_types = self.context.tokens[1:]
        if len(pointer_types) == 0:
            self.syntax_error('Incorrect usage of instruction "pi", '
                            'missing pointer type names.', 2)
        type_name = self.POINTER_MAP.get(self.context.last_defined_interface,
                                            f'{self.context.last_defined_interface}.PTR()')
        pointer_types.append(type_name)
        if not self.context.silent:
            self.code.append(' = '.join(pointer_types))
            self.code.append_newline()
        self.POINTER_MAP[self.context.tokens[1]] = pointer_types[0]
        
    def pointer_explicit(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect usage of instruction "pie", '
                            'missing type name and type names.', 3)
        type_name = self.context.tokens[1]
        pointer_types = self.context.tokens[2:]
        if len(pointer_types) == 0:
            self.syntax_error('Incorrect usage of instruction "pie", '
                            'missing pointer type names.', len(type_name)+3)
        type_name = self.POINTER_MAP.get(type_name,
                                            f'{type_name}.PTR()')
        
        pointer_types.append(type_name)
        if not self.context.silent:
            self.code.append(' = '.join(pointer_types))
            self.code.append_newline()
        self.POINTER_MAP[self.context.tokens[1]] = pointer_types[0]
        
    def structure_define(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of structure placeholder, '
                            'missing structure name.', 3)
        
        structure_name = self.context.tokens[1]
        self.context.declaring_structure = structure_name
        if not self.context.silent:
            self.code.append_decorator('CStructure.make', [], [])
            self.code.append_class(structure_name, 'CStructure')
            self.code.indent()
            
    def structure_field(self):
        if self.context.tokens_length < 3:
            self.syntax_error('Incorrect declaration of structure field, '
                              'missing field type and field name.', 3)
        
        field_type = self.context.tokens[1]
        *parameters, field_type = field_type.split('.')
        parameters = [param.lower() for param in parameters]
        
        ptr_count = parameters.count('p')
        if ptr_count == 2:
            field_type = 'IDoublePtr[' + field_type +  ']'
        else:
            field_type = 'IPointer[' * ptr_count + field_type + ']' * ptr_count
        
        field = self.context.tokens[2]
        self.code.append(f'{self.indents}{field}: {field_type}')
            
    def enum_define(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of enum, '
                            'missing enum name.', 3)
        
        enum_name = self.context.tokens[1]
        self.TYPE_MAP[enum_name] = 'int'
        self.context.declaring_enum = enum_name
        self.context.enum_entry_count = 0
        
    def enum_entry(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of enum entry,'
                              'missing enum entry name.')
        
        enum_entry_count = self.context.enum_entry_count
        entry_name = self.context.tokens[1]
        
        if self.context.tokens_length > 2:
            enum_entry_count = self.context.tokens[2]
            if enum_entry_count.startswith('0x'):
                self.context.enum_entry_count = int(enum_entry_count, 16)
            else:
                self.context.enum_entry_count = int(enum_entry_count)
        
        self.code.append(f'{entry_name} = {enum_entry_count}')
        self.context.enum_entry_count += 1
        
    def alias(self):
        if self.context.tokens_length < 3:
            self.syntax_error('Incorrect usage of "al" instruction, '
                                'missing alias and names.', len(self.context.last_line))
        
        alias = self.context.tokens[1]
        names = self.context.tokens[2:]
        for name in names:
            self.TYPE_MAP[name] = alias
            
    def gencomment(self):
        self.code.append_comment()
        self.code.append_comment(f'{self.code.file.name}')
        self.code.append_comment()
        self.code.append_comment('File created by WICL generator version 1.00')
        self.code.append_comment(f'Creation timestamp: {time.ctime()}')
        self.code.append_comment(f'Generated from ICL: {self.file.name}')
        if self.context.commentext:
            self.code.append_comment()
            self.code.append_comment('Additional info:')
            self.code.append_comment(self.context.commentext, not_breakline=True)
            self.context.commentext = ''
        self.code.append_comment()
            
    def gencommentlw(self):
        self.code.append_comment('This code created by WICL generator version 1.00')
        self.code.append_comment(f'Creation timestamp: {time.ctime()}')
        self.code.append_comment(f'Generated from ICL: {self.file.name}')
        if self.context.commentext:
            self.code.append_comment()
            self.code.append_comment('Additional info:')
            self.code.append_comment(self.context.commentext, not_breakline=True)
            self.context.commentext = ''
        self.code.append_comment('{')
        self.context.in_gencommentlw_block = True
        
    def foreign_function(self):
        if self.context.tokens_length < 3:
            self.syntax_error('Incorrect declaration of foreign function, '
                            'missing result type, function name and arguments',
                            len(self.context.last_line))
        
        function_name = self.context.tokens[1]
        lib_name, function_name = function_name.split('.')
        result_type = self.context.tokens[2]
        decorator_args = [result_type]
        decorator_named_args = []
        has_refs: Ref[bool] = Ref(bool)
        if result_type == 'BOOL':
            result_type = 'bool'
            decorator_named_args.append(('result_function', 'bool'))
        result_type = self.TYPE_MAP.get(result_type, result_type)
        args = []
        refs = []
        if self.context.tokens_length > 3:
            if ((self.context.tokens_length-3) % 2) != 0 or self.context.tokens_length == 4:
                self.syntax_error('Incorrect declaration of foreign function,'
                                'missing one of argument components '
                                '(tokens count is not even or == 4)',
                                len(function_name)+len(result_type)+5)
            
            
            self.parse_arguments(decorator_args, decorator_named_args, args, 3, has_refs, refs)
            
        self.context.external_function_count += 1
        if self.context.external_function_count == 1:
            self.code.append_newline()
        
        self.new_function(has_refs, function_name, result_type, args,
                            f'{lib_name}.foreign', decorator_args, 
                            decorator_named_args, refs, True)
        if len(self.context.docs) != 0: self.context.docs = ''
        
    def foreign_function_lib(self, instruction: str):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of foreign function,'
                            'missing function name', len(self.context.last_line))
        self.context.function_count += 1
        if self.context.function_count == 1 and not self.context.silent:
            self.code.append_newline()
        
        function_name = self.context.tokens[1]
        lib_name = instruction[:-2]
        if lib_name == 'ole' or lib_name == 'oleaut':
            lib_name += '32'
        decorator_args = ['HRESULT']
        decorator_named_args = []
        has_refs: Ref[bool] = Ref(bool)
        args = []
        refs = []
        if self.context.tokens_length > 2:
            if (self.context.tokens_length % 2) != 0:
                self.syntax_error('Incorrect declaration of foreign function,'
                                'missing one of argument components '
                                '(tokens count is not even)',
                                len(function_name)+len(instruction))
            
            self.parse_arguments(decorator_args, decorator_named_args, args, 2, has_refs, refs)
        
        self.context.external_function_count += 1
        if self.context.external_function_count == 1:
            self.code.append_newline()
        
        self.new_function(has_refs, function_name, 'int', args,
                            f'{lib_name}.foreign', decorator_args, 
                            decorator_named_args, refs, True)
        if len(self.context.docs) != 0: self.context.docs = ''
        
    def equal(self):
        if self.context.tokens_length < 3:
            self.syntax_error('Incorrect declaration of equal statement, '
                              'missing name and value.', len(self.context.last_line))
        
        self.code.append(f'{self.context.tokens[1]} = {self.context.tokens[2]}')
        
    def define_guid(self, class_name: str = None):
        if class_name is None:
            if self.context.tokens_length < 13:
                self.syntax_error('Incorrect declaration of define GUID, '
                                  'missing class, name and value.', len(self.context.last_line))
            class_name = self.context.tokens[1]
            name = self.context.tokens[2]
            data1, data2, data3, *d = self.context.tokens[3:]  
        else:
            if self.context.tokens_length < 12:
                self.syntax_error('Incorrect declaration of define GUID, '
                                  'missing name and value.', len(self.context.last_line))
            name = self.context.tokens[1]
            data1, data2, data3, *d = self.context.tokens[2:]
        
        data1 = data1[2:].zfill(8)
        data2 = data2[2:].zfill(4)
        data3 = data3[2:].zfill(4)
        d = [data[2:].zfill(2) for data in d]
        
        guid = f'{{{data1}-{data2}-{data3}-{d[0]+d[1]}-{d[2]+d[3]+d[4]+d[5]+d[6]+d[7]}}}'
        self.code.append(f"{name} = {class_name}('{guid}')")
        
    def define_interface_unknown(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of interface, '
                            'missing interface name.', 3)
        interface_name = self.context.tokens[1]
        self.context.base = 'IUnknown'
        
        if not self.context.silent:
            self.code.append_class(interface_name, self.context.base)
            self.code.indent()
            if self.context.base != '':
                self.code.append_field('virtual_table',
                                    value=f"COMVirtualTable.from_ancestor({self.context.base})")
            else:
                self.code.append_field('virtual_table', value=f"COMVirtualTable('{interface_name}')")
        
        self.context.last_defined_interface = interface_name
        
    def define_coclass(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect declaration of coclass, '
                            'missing class name.', 3)
        class_name = self.context.tokens[1]
        
        self.code.append_class(class_name, 'COMClass')
        self.code.indent()
        
        self.context.declaring_class = True
        
    def clsid(self):
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect usage of "clsid" instruction,'
                            'missing CLSID.', len(self.context.last_line)+1)
        
        clsid = self.context.tokens[1]
        self.code.append_field('_clsid_', value='CLSID("{'+clsid+'}")')