from win.minwindef import *

class StructureInspector:
    def __init__(self, struct: CStructure):
        self.struct = struct
    
    def print(self):
        for o, f, s in self.get():
            print(f'{format_hex(o, 2)} {f} +{s}')
        
    def get(self) -> list[tuple[int, str, int]]:
        last = 0
        r = []
        for f in self.struct._fields_:
            f, *_ = f
            o = self.struct.offset(f)
            s = self.struct.field_size(f)
            if o != last:
                r.append((last, 'Gap', o - last))
            r.append((o, f, s))
            last = o + s
        return r

# migrated from defbase_helper.py
def has_contents(attr) -> bool:
    try:
        return hasattr(attr, 'contents')
    except ValueError:
        return True

def make_fields(structure):
    fields = []
    for mro in type(structure).__mro__:
        if hasattr(mro, '_fields_'):
            fields = mro._fields_ + fields
    return fields

def format_structure(formatname, structure):
    if has_contents(structure):
        if not structure:
            print(f"{formatname} => NULL")
            return
        structure = structure.contents
        delimiter = '->'
    else:
        delimiter = '.'
    
    if isinstance(structure, Structure):
        for i, t, *_ in make_fields(structure):
            formatted = formatname + delimiter + i
            attr = getattr(structure, i)
            if has_contents(attr):
                format_structure(formatted, attr)
            elif isinstance(attr, Structure):
                format_structure(formatted, attr)
            else:
                if issubclass(t, c_void_p):
                    if not attr:
                        print(f"{formatted} => NULL")
                    else:
                        print(f"{formatted} => {format_hex(attr, sizeof(c_void_p))}")
                else:
                    print(f"{formatted} => {attr}")
    else:
        return structure