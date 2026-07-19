from .imagelist import *
from .window import *

class Toolbar(Control):
    """
    Win32 Toolbar common control.
    """
    
    def __init__(self, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self.class_name = "ToolbarWindow32"
    
    def create(self):
        super().create(0, 0, window_name=NULL)
        self.send(TB_BUTTONSTRUCTSIZE, sizeof(TBBUTTON))
        
    @property
    def image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(TB_GETIMAGELIST))
    
    @image_list.setter
    def image_list(self, image_list: ImageList):
        self.send(TB_SETIMAGELIST, 0, image_list)
        
    def add(self, image_index: int, identifier: int | HMENU, 
            style: int = BTNS_BUTTON, state: int = TBSTATE_ENABLED):
        btn = TBBUTTON(iBitmap=image_index, idCommand=identifier,
                       fsStyle=style, fsState=state)
        self.send(TB_ADDBUTTONS, 1, btn.ref())
        
    def enable(self, identifier: int, enable: bool = True):
        self.send(TB_ENABLEBUTTON, identifier, enable)
        
    def disable(self, identifier: int):
        self.send(TB_ENABLEBUTTON, identifier, FALSE)
        
    def information(self, identifier: int, mask: int | None = None) -> TBBUTTONINFOW:
        if mask is None:
            mask = (TBIF_COMMAND | TBIF_IMAGE | TBIF_LPARAM | TBIF_SIZE | TBIF_STYLE)
        tbi = TBBUTTONINFOW()
        tbi.cbSize = tbi.size()
        tbi.mask = mask
        self.send(TB_GETBUTTONINFOW, identifier, tbi.ref())
        return tbi
        
    def set(self, identifier: int, information: TBBUTTONINFOW, mask: int | None = None):
        if mask is None:
            mask = (TBIF_COMMAND | TBIF_IMAGE | TBIF_LPARAM | TBIF_SIZE | TBIF_STYLE)
        information.cbSize = information.size()
        information.mask = mask
        self.send(TB_SETBUTTONINFOW, identifier, information.ref())