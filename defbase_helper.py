from .defbase import CStructure

def format_structure(formatname, structure):
    if isinstance(structure, CStructure):
        for i in dir(CStructure):
            if not i.startswith("_"):
                formatted = formatname + "." + i
                attr = getattr(structure, i)
                if isinstance(attr, CStructure):
                    format_structure(formatted, attr)
                else:
                    print(f"{formatted} => {attr}")
    else:
        return structure