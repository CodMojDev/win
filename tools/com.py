from ..com.interfacedef import *
from ..defbase_process import *

def VTable_View(itf: COMInterface, virtual_table: COMVirtualTable, process: CProcess = CProcess()) -> str:
    vtable = i_cast(getattr(itf, virtual_table.field_name), PTR(virtual_table.VType))
    result = ''
    for i, field in enumerate(vtable.contents._fields_):
        field_name = field[0]
        address = getattr(vtable.contents, field_name)
        address = process.format_address(address)
        offset = format_hex(vtable.contents.offset(field_name), sizeof(WORD))
        if i != 0:
            result += '\n'
        result += f'{offset} {field_name} = {address}'
    return result