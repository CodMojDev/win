from .window import *

class Combobox(Control):
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = WC_COMBOBOXW
        
    def create(self, x: int, y: int, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, '', relative)
        
    def reset(self):
        self.send(CB_RESETCONTENT)
        
    def count(self) -> int:
        return self.send(CB_GETCOUNT)
    
    def insert(self, index: int, variant: str):
        self.send(CB_INSERTSTRING, index, variant)
        
    def append(self, variant: str):
        self.send(CB_ADDSTRING, 0, variant)
        
    def limit(self, limit: int):
        self.send(CB_LIMITTEXT, limit)
        
    @property
    def current(self) -> int:
        return self.send(CB_GETCURSEL)
    
    @current.setter
    def current(self, current: int):
        self.send(CB_SETCURSEL, current)
        
    def text(self, index: int) -> str | None:
        """
        Get text of the item.
        """
        length = self.send(CB_GETLBTEXTLEN, index)
        if length == CB_ERR: return None
        text = create_unicode_buffer(length)
        if self.send(CB_GETLBTEXT, index, text) == CB_ERR:
            return None
        return text.value