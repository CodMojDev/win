from .window import *

class StatusBar(Control):
    """
    Win32 Status bar common control.
    """
    class Item:
        sb: 'StatusBar'
        index: int
        
        def __init__(self, sb: 'StatusBar', index: int):
            self.index = index
            self.sb = sb
        
        @property
        def text(self) -> str:
            lRet = self.sb.send(SB_GETTEXTLENGTHW, self.index)
            nSymbols = LOWORD(lRet)
            buf = create_unicode_buffer(nSymbols)
            self.sb.send(SB_GETTEXTW, self.index, buf)
            return buf.value
        
        @property
        def rect(self) -> Rect:
            rc = Rect()
            if not self.sb.send(SB_GETRECT, self.index, rc.ref()):
                raise WinException()
            return rc
    
    def __init__(self, text: str, parent: int | HWND, 
                 identifier: int | HMENU, draw_mode: int = 0):
        super().__init__(parent, identifier)
        self._draw_mode = draw_mode
        self._text = text
        
    def create(self):
        """
        Create status bar control.
        """
        
        self.value = CreateStatusWindowW(self._style, self._text, self._parent, self._identifier)
        if not self.value:
            raise WinException()
        
    def __setitem__(self, index: int, value: str):
        buf = create_unicode_buffer(value)
        self.buf = buf
        self.send(SB_SETTEXTW, MAKEWORD(index, self._draw_mode), buf)
        
    def __getitem__(self, index: int) -> Item:
        return self.Item(self, index)
    
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