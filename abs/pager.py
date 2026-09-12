from .window import *
from win.com.oleidl import IDropTarget

class Pager(Control):
    """
    The Win32 Pager control.
    """
    
    _width: int
    _height: int
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        
        self.class_name = WC_PAGESCROLLERW
        self._width = width
        self._height = height
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        return super().create(self._width, self._height, x, y, NULL, relative)
    
    @property
    def bk_color(self) -> Color.BGR:
        return Color.BGR(self.send(PGM_GETBKCOLOR))
    
    @bk_color.setter
    def bk_color(self, bk_color: int | Color.IColor):
        self.send(PGM_SETBKCOLOR, 0, int(bk_color))
        
    @property
    def border(self) -> int:
        return self.send(PGM_GETBORDER)
    
    @border.setter
    def border(self, border: int):
        self.send(PGM_SETBORDER, 0, border)
        
    def recalculate(self):
        """
        Recalculate the size of an autonomous window.
        """
        self.send(PGM_RECALCSIZE)
        
    @property
    def drop_target(self) -> IDropTarget:
        pTarget = IDropTarget.NULL()
        self.send(PGM_GETDROPTARGET, 0, byref(pTarget))
        return pTarget.contents
    
    @property
    def button_size(self) -> int:
        return self.send(PGM_GETBUTTONSIZE)
    
    @button_size.setter
    def button_size(self, button_size: int):
        self.send(PGM_SETBUTTONSIZE, 0, button_size)
    
    @property
    def button_state(self) -> int:
        return self.send(PGM_GETBUTTONSTATE)
    
    def set(self, child: int | HANDLE):
        """
        Set the child window of a pager control.
        """
        self.send(PGM_SETCHILD, 0, child)
        
    def forward_mouse(self, value: bool = True):
        """
        Enable or disable the mouse forwarding for pager.
        """
        self.send(PGM_FORWARDMOUSE, value)