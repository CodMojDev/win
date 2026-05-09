from win.commdlg import *
from .window import *

class ColorDialog:
    def __init__(self, owner: int | HANDLE = NULL, 
                 full_open: bool = False, show_help: bool = False, 
                 rgb: Optional[int] = None, template: Optional[int | PVOID] = None):
        self.choose_color = CHOOSECOLORW()
        self.choose_color.Flags |= CC_ANYCOLOR | CC_ENABLEHOOK
        self.choose_color.lStructSize = self.choose_color.size()
        self.choose_color.hwndOwner = owner
        self.pfnHookProc = LPCCHOOKPROC(self.hook_proc)
        self.choose_color.lpfnHook = self.pfnHookProc
        self.cust_colors = (COLORREF * 16)()
        self.choose_color.lpCustColors = self.cust_colors
        
        if rgb is not None:
            self.choose_color.Flags |= CC_RGBINIT
            self.choose_color.rgbResult = rgb
        
        if full_open:
            self.choose_color.Flags |= CC_FULLOPEN
        
        if show_help:
            self.choose_color.Flags |= CC_SHOWHELP
            
        if template is not None:
            self.choose_color.Flags |= CC_ENABLETEMPLATEHANDLE
            self.choose_color.hInstance = PtrUtil.get_address(template)
    
    @property
    def color(self) -> Color.RGB:
        return Color.RGB(self.choose_color.rgbResult)
    
    def create(self) -> bool:
        return bool(ChooseColorW(self.choose_color.ref()))
    
    def on_message(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        return FALSE
    
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        return self.on_message(hWnd, uMsg, wParam, lParam)