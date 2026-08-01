from .window import *

class Static(Control):
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = 'STATIC'
        
    def create(self, x: int = 0, y: int = 0, window_name: str='', relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, window_name, relative=relative)
        
    @property
    def icon(self) -> Icon:
        return Icon.foreign_owner(self.send(STM_GETICON))
    
    @icon.setter
    def icon(self, icon: int | HANDLE):
        self.send(STM_SETICON, icon)
        
    @property
    def bitmap(self) -> Bitmap:
        return Bitmap.foreign_owner(self.send(STM_GETIMAGE, IMAGE_BITMAP))
    
    @bitmap.setter
    def bitmap(self, bitmap: int | HANDLE):
        self.send(STM_SETIMAGE, IMAGE_BITMAP, bitmap)
        
    @property
    def cursor(self) -> Cursor:
        return Cursor.foreign_owner(self.send(STM_GETIMAGE, IMAGE_CURSOR))
    
    @cursor.setter
    def cursor(self, cursor: int | HANDLE):
        self.send(STM_SETIMAGE, IMAGE_CURSOR, cursor)
        
    @property
    def text(self) -> str:
        i = self.send(WM_GETTEXTLENGTH)
        p = create_unicode_buffer(i)
        self.send(WM_GETTEXT, i, p)
        return p.value
    
    @text.setter
    def text(self, text: str):
        self.send(WM_SETTEXT, 0, text)