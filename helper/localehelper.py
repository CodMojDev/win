import locale

loc: str = locale._getdefaultlocale()[0]

def GetLocale() -> str:
    return loc

def UpdateLoc() -> None:
    global loc
    loc = locale._getdefaultlocale()[0]

def IsLocaleEqual(e_loc: str) -> bool:
    return e_loc == loc
    
def IsLocalesEqual(e_locs: list[str]) -> bool:
    return loc in e_locs