from .window import *

EM_SETCUEBANNER   = ECM_FIRST + 1
EM_GETCUEBANNER   = ECM_FIRST + 2
EM_REDO = WM_USER + 84

class Edit(Control):
    """
    Win32 Edit common control.
    """
    
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
        self.send(EM_GETSEL, byref(selStart), byref(selEnd))
        return (selStart.value, selEnd.value)
    
    @selection.setter
    def selection(self, selection: tuple[int, int]):
        self.post(EM_SETSEL, selection[0], selection[1])
        
    def undo(self):
        """
        Undo the changes to edit control.
        """
        
        self.post(EM_UNDO)
        
    def redo(self):
        """
        Redo the changes to edit control.
        """
        
        self.post(EM_REDO)
        
    @property
    def readonly(self) -> bool:
        return self.style & ES_READONLY
    
    @readonly.setter
    def readonly(self, readonly: bool):
        self.send(EM_SETREADONLY, readonly)
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        """
        Create the edit control.
        """
        super().create(self._width, self._height, x, y, self._text, relative)
        
    @property
    def cue_banner(self) -> str:
        buf = create_unicode_buffer(256)
        self.send(EM_GETCUEBANNER, buf, 256)
        return buf.value
    
    @cue_banner.setter
    def cue_banner(self, cue_banner: str):
        buf = create_unicode_buffer(cue_banner)
        self.post(EM_SETCUEBANNER, FALSE, buf)
        
    def get_line(self, index: int) -> str:
        """
        Get the edit control line.
        """
        buf = create_unicode_buffer(512)
        i_cast(buf, PWORD)[0] = 512
        self.send(EM_GETLINE, index, buf)
        return buf.value
    
    @property
    def current_line(self) -> int:
        return self.send(EM_LINEFROMCHAR, -1)
    
    @property
    def line_count(self) -> int:
        return self.send(EM_GETLINECOUNT)