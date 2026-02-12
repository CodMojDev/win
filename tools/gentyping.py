from ..minwindef import *
from typing import List

TYPE_MAP = {
    c_int: 'int', c_uint: 'int', c_short: 'int',
    c_ushort: 'int', c_float: 'float', c_double: 'float',
    c_longdouble: 'float', c_long: 'int', c_ulong: 'int',
    c_byte: 'int', c_ubyte: 'int', c_longlong: 'int',
    c_ulonglong: 'int', c_char: 'int', c_char_p: 'bytes',
    c_wchar_p: 'str', c_wchar: 'int'
}

def GenerateTyping(structure: Type[CStructure]) -> str:
    fields: List[str] = []
    for field in structure._fields_:
        typ, field_name = field[1], field[0]
        if PtrUtil.is_pointer(typ) and not typ in TYPE_MAP:
            ptr_type = PtrUtil.get_type(typ)
            if PtrUtil.is_pointer(ptr_type):
                ptr_type = PtrUtil.get_type(ptr_type)
                typ = f'IDoublePtr[{ptr_type.__name__}]'
            else:
                typ = f'IPointer[{ptr_type.__name__}]'
        else:
            typ = TYPE_MAP.get(typ, typ)
        fields.append(f'{field_name}: {typ}')
    fields = sorted(fields, key=lambda member: len(member), reverse=True)
    return '\n'.join(fields)