from .window import *

class StatusBar(Control):
    def __init__(self, text: str, parent: int | HWND, 
                 identifier: int | HMENU, draw_mode: int = 0):
        super().__init__(parent, identifier)
        self._draw_mode = draw_mode
        self._text = text
        
    def create(self):
        self.value = CreateStatusWindowW(self._style, self._text, self._parent, self._identifier)
        if not self.value:
            raise WinException()
        
    def __setitem__(self, index: int, value: str):
        buf = create_unicode_buffer(value)
        self.send(SB_SETTEXTW, MAKEWORD(index, self._draw_mode), buf)
        
    def __getitem__(self, index: int) -> str:
        lRet = self.send(SB_GETTEXTLENGTHW, index)
        nSymbols = LOWORD(lRet)
        buf = create_unicode_buffer(nSymbols)
        self.send(SB_GETTEXTW, index, buf)
        return buf.value
    
    @property
    def parts(self) -> tuple[int, ...]:
        nParts = self.send(SB_GETPARTS, lParam=NULL)
        buf = (INT * nParts)()
        self.send(SB_GETPARTS, nParts, buf)
        return tuple(buf)
        
    @parts.setter
    def parts(self, parts: Iterable[int]):
        length = len(parts)
        iParts = []
        for part in parts:
            iParts.append(int(part))
        pParts = (INT * length)(*iParts)
        self.send(SB_SETPARTS, length, pParts)