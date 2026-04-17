from .window import *

class TabControl(Control):
    def __init__(self, width: int, height: int, parent: int | HANDLE, identifier: int | HANDLE):
        super().__init__(parent, identifier)
        
    def adjust_rect(self, pRect : IPointer[RECT], non_client: bool = False):
        SendMessage(self, TCM_)