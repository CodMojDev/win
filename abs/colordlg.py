from win.commdlg import *
from .window import *

class ColorDialog:
    """
    Color dialog class.
    """
    
    def __init__(self, owner: int | HANDLE = NULL, 
                 full_open: bool = False, show_help: bool = False, 
                 color: Optional[int | Color.IColor] = None, template: Optional[int | PVOID] = None):
        # setup CHOOSECOLORW structure
        self.choose_color = CHOOSECOLORW()
        self.choose_color.Flags |= CC_ANYCOLOR | CC_ENABLEHOOK
        self.choose_color.lStructSize = self.choose_color.size()
        
        # setup dialog owner
        self.choose_color.hwndOwner = owner
        
        # setup dialog message hook procedure
        self.pfnHookProc = LPCCHOOKPROC(self.hook_proc)
        self.choose_color.lpfnHook = self.pfnHookProc
        
        # allocate custom colors array (16 COLORREFs)
        self.cust_colors = (COLORREF * 16)()
        self.choose_color.lpCustColors = self.cust_colors
        
        # if initial color is set, when adjust flags and set the initial color
        if color is not None:
            self.choose_color.Flags |= CC_RGBINIT
            self.choose_color.rgbResult = int(color)
        
        # support for full opening color dialog
        if full_open:
            self.choose_color.Flags |= CC_FULLOPEN
        
        # support for help
        if show_help:
            self.choose_color.Flags |= CC_SHOWHELP
            
        # support for custom dialog template
        if template is not None:
            self.choose_color.Flags |= CC_ENABLETEMPLATEHANDLE
            self.choose_color.hInstance = PtrUtil.get_address(template)
    
    @property
    def color(self) -> Color.BGR:
        return Color.BGR(self.choose_color.rgbResult)
    
    def create(self) -> bool:
        """
        Create "Choose color" dialog.
        """
        
        return bool(ChooseColorW(self.choose_color.ref()))
    
    def on_message(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        """"
        This handler is called on dialog message.
        """
        
        return FALSE
    
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        return self.on_message(hWnd, uMsg, wParam, lParam)