from .window import *

EM_SETCUEBANNER   = ECM_FIRST + 1
EM_GETCUEBANNER   = ECM_FIRST + 2
EM_REDO = WM_USER + 84

class Edit(Control):
    def __init__(self, width: int, height: int, parent: int | HWND, 
                 identifier: int | HMENU, text: str = '', readonly: bool = False):
        super().__init__(parent, identifier)
        self.class_name = 'EDIT'
        if readonly:
            self._style |= ES_READONLY
        self._text = text
        self._width = width
        self._height = height
            
    @property
    def selection(self) -> tuple[int, int]:
        selStart = DWORD()
        selEnd = DWORD()
        SendMessage(self, EM_GETSEL, PtrUtil.get_address(byref(selStart)), 
                    PtrUtil.get_address(byref(selEnd)))
        return (selStart.value, selEnd.value)
    
    @selection.setter
    def selection(self, selection: tuple[int, int]):
        SendMessage(self, EM_SETSEL, selection[0], selection[1])
        
    def undo(self):
        SendMessage(self, EM_UNDO, 0, 0)
        
    def redo(self):
        SendMessage(self, EM_REDO, 0, 0)
        
    @property
    def readonly(self) -> bool:
        return self.style & ES_READONLY
    
    @readonly.setter
    def readonly(self, readonly: bool):
        SendMessage(self, EM_SETREADONLY, readonly, 0)
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, self._text, relative)
        
    @property
    def cue_banner(self) -> str:
        buf = create_unicode_buffer(256)
        SendMessage(self, EM_GETCUEBANNER, PtrUtil.get_address(buf), 256)
        return buf.value
    
    @cue_banner.setter
    def cue_banner(self, cue_banner: str):
        buf = create_unicode_buffer(cue_banner)
        SendMessage(self, EM_SETCUEBANNER, FALSE, PtrUtil.get_address(buf))
        
    def get_line(self, index: int) -> str:
        buf = create_unicode_buffer(512)
        i_cast(buf, PWORD)[0] = 512
        SendMessage(self, EM_GETLINE, index, PtrUtil.get_address(buf))
        return buf.value
    
    @property
    def current_line(self) -> int:
        return SendMessage(self, EM_LINEFROMCHAR, -1, 0)