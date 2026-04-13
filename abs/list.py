from .window import *

class List(Control):
    def __init__(self, parent: int | HWND = NULL, identifier: int | HWND = NULL):
        super().__init__(parent, identifier)
        
        self.class_name = WC_LISTVIEWW
        