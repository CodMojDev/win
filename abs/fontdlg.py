from .window import *
from win.commdlg import *

class FontDialog(Window):
    """
    Font dialog class.
    """
    
    choose_font: CHOOSEFONTW  
    lpfnHook: FARPROC
    lpTemplateName: IWideCharArray | None
    lpszStyle: IWideCharArray | None
    on_message: SingleEvent
    
    def __init__(self, owner: int | HANDLE = NULL, lf: LOGFONTW | int | HANDLE | EXTLOGFONTW | GDIObjectHandle | None = None,
                 dc: int | HANDLE = NULL, template: str | None = None, 
                 handle: WT_ADDRLIKE = NULL, color: Color.IColor | int = 0,
                 style: str | None = None, size: GraphicUtils.Size | None = None,
                 extra_flags: int = 0):
        super().__init__()
    
        # setup the CHOOSEFONTW structure
        self.choose_font = CHOOSEFONTW()
        self.choose_font.lStructSize = CHOOSEFONT.size()
        self.choose_font.lpfnHook = self.lpfnHook = LPCFHOOKPROC(self.hook_proc)
        self.choose_font.hwndOwner = owner
        # hook is always enabled
        extra_flags |= CF_ENABLEHOOK
        
        # if LOGFONTW structure given, then add it and adjust flags
        if lf is not None:
            if isinstance(lf, EXTLOGFONTW):
                lf = lf.elfLogFont
            elif not isinstance(lf, LOGFONTW):
                if isinstance(lf, GDIObjectHandle):
                    hfont = lf
                else:
                    hfont = GDIObjectHandle.foreign_owner(lf)
                ty = hfont.type
                if ty == OBJ_FONT:
                    lf = hfont.object
                elif ty == 0:
                    raise ValueError(f'Invalid GDI Handle {hfont.value}.')
                else:
                    raise ValueError(f'Invalid GDI Handle type {ty}.')
                    
            extra_flags |= CF_INITTOLOGFONTSTRUCT
        else: # otherwise create automatically
            lf = LOGFONTW()
        self.choose_font.lpLogFont = lf.ptr()
        
        # if template name present, then set it into struct
        if template is not None:
            self.lpTemplateName = create_unicode_buffer(template)
            self.choose_font.lpTemplateName = i_cast(self.lpTemplateName, LPCWSTR)
            self.choose_font.hInstance = handle
            extra_flags |= CF_ENABLETEMPLATE
        else:
            self.lpTemplateName = None
            if handle is not None:
                self.choose_font.hInstance = handle
                extra_flags |= CF_ENABLETEMPLATEHANDLE
        # if style is used, when set it and adjust flags
        if extra_flags & CF_USESTYLE:
            self.lpszStyle = create_unicode_buffer(256)
            if style is not None:
                self.lpszStyle.value = style
            self.choose_font.lpszStyle = i_cast(self.lpszStyle, LPWSTR)
        
        # if size is given, when set it and adjust CF_LIMITSIZE
        if size is not None:
            extra_flags |= CF_LIMITSIZE
            self.choose_font.nSizeMin, self.choose_font.nSizeMax = size
        
        # set the CHOOSEFONTW rgbColors field
        self.choose_font.rgbColors = int(color)
        
        # set the CHOOSEFONTW flags
        self.choose_font.Flags = extra_flags
        
        # create the common dialog events
        self.on_message = SingleEvent()
    
    def create(self) -> bool:
        """
        Create the Font dialog.
        """
        result = ChooseFontW(self.choose_font.ref()) != FALSE
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
    
    @property
    def point_size(self) -> int:
        return self.choose_font.iPointSize
    
    @property
    def font_type(self) -> int:
        return self.choose_font.nFontType
    
    @property
    def font(self) -> LOGFONTW:
        return self.choose_font.lpLogFont.contents
    
    @property
    def color(self) -> Color.BGR:
        return Color.BGR(self.choose_font.rgbColors)