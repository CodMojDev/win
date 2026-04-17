from .imagelist import *
from .window import *

class Toolbar(Control):
    def __init__(self, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self.class_name = TOOLBARCLASSNAMEW
    
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