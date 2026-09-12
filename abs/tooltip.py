from .window import *

class Tooltip(Window):
    def __init__(self):
        super().__init__()
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add(WS_POPUP)
        self.class_name = TOOLTIPS_CLASSW
        
    def create(self, parent: int | HANDLE = NULL):
        super().create(parent)
        self.set_position(insert_after=HWND_TOPMOST, flags=SWP_NOACTIVATE)
    TTM_ACTIVATE
    def activate(self, activate: bool = True):
        self.send(TTM_ACTIVATE, activate)
        
    def deactivate(self):
        self.send(TTM_ACTIVATE, False)
        
    def add(self, value: int | HANDLE, text: str,
            parent: int | HANDLE | None = None, 
            rect: RECT | None = None,
            flags: int=0, parameter: int = 0):
        ti = TTTOOLINFOW()
        ti.cbSize = ti.size()
        if parent is None:
            parent = self.parent
        if rect is not None:
            ti.rect = rect
        ti.hwnd = parent
        ti.uId = PtrUtil.get_address(value)
        ti.lParam = PtrUtil.get_address(parameter)
        ti.uFlags = flags
        self.send(TTM_ADDTOOL, 0, ti.ref())