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