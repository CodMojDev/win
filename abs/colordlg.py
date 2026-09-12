from win.commdlg import *
from .window import *

class ColorDialog(Window):
    """
    Color dialog class.
    """
    
    on_message: SingleEvent
    choose_color: CHOOSECOLORW
    pfnHookProc: FARPROC
    cust_colors: IArray[int]
    
    def __init__(self, owner: int | HANDLE = NULL, 
                 full_open: bool = False, show_help: bool = False, 
                 color: Optional[int | Color.IColor] = None, template: Optional[int | PVOID] = None):
        super().__init__()
        
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
    
        self.on_message = SingleEvent()
    
    @property
    def color(self) -> Color.BGR:
        return Color.BGR(self.choose_color.rgbResult)
    
    def create(self) -> bool:
        """
        Create "Choose color" dialog.
        """
        result = ChooseColorW(self.choose_color.ref()) != FALSE
        if not result:
            code = CommDlgExtendedError()
            if code != 0:
                raise CommonDialogError(code)
        return result
    
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        if uMsg == WM_INITDIALOG:
            self.value = hWnd
        if self.on_message.empty(): return FALSE
        return self.on_message.execute(hWnd, uMsg, wParam, lParam)