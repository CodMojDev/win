from .controllable import *
from win.winuser import *
from win.defbase_errordef import *
from win.com.comdefbase import *
from .handle import *

uxtheme = get_win_library('uxtheme.dll')

HTHEME = HANDLE

@uxtheme.foreign(HRESULT, HWND, HDC, PRECT)
def DrawThemeParentBackground(hwnd: int | HANDLE, hdc: int | HANDLE, prc: PRECT) -> int: ...

@uxtheme.foreign(HTHEME, HWND, LPCWSTR)
def OpenThemeData(hwnd: int | HANDLE, pszClassList: str | LPCWSTR) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME)
def CloseThemeData(hTheme: int | HANDLE): ...

@uxtheme.foreign(BOOL, HTHEME, INT, INT)
def IsThemeBackgroundPartiallyTransparent(hTheme: int | HANDLE, iPartId: int, iStateId: int) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME, HDC, INT, INT, LPCWSTR, INT, DWORD, DWORD, LPCRECT)
def DrawThemeText(
    hTheme: int | HANDLE, hdc: int | HANDLE, iPartId: int, iStateId: int,
    pszText: str | LPCWSTR, cchText: int, dwTextFlags: int,
    dwTextFlags2: int, pRect: IPointer[RECT]) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME, HDC, INT, INT, LPCRECT, LPCRECT)
def DrawThemeBackground(hTheme: int | HANDLE, hdc: int | HANDLE, iPartId: int, iStateId: int, 
                        pRect: IPointer[RECT], pClipRect: IPointer[RECT]) -> int: ...

DTT_CALLBACK_PROC = WINAPI(INT, HDC, LPWSTR, INT, PRECT, UINT, LPARAM)

DTT_TEXTCOLOR       = (1 << 0)      # crText has been specified
DTT_BORDERCOLOR     = (1 << 1)      # crBorder has been specified
DTT_SHADOWCOLOR     = (1 << 2)      # crShadow has been specified
DTT_SHADOWTYPE      = (1 << 3)      # iTextShadowType has been specified
DTT_SHADOWOFFSET    = (1 << 4)      # ptShadowOffset has been specified
DTT_BORDERSIZE      = (1 << 5)      # iBorderSize has been specified
DTT_FONTPROP        = (1 << 6)      # iFontPropId has been specified
DTT_COLORPROP       = (1 << 7)      # iColorPropId has been specified
DTT_STATEID         = (1 << 8)      # IStateId has been specified
DTT_CALCRECT        = (1 << 9)      # Use pRect as and in/out parameter
DTT_APPLYOVERLAY    = (1 << 10)     # fApplyOverlay has been specified
DTT_GLOWSIZE        = (1 << 11)     # iGlowSize has been specified
DTT_CALLBACK        = (1 << 12)     # pfnDrawTextCallback has been specified
DTT_COMPOSITED      = (1 << 13)     # Draws text with antialiased alpha (needs a DIB section)
DTT_VALIDBITS       = (DTT_TEXTCOLOR | DTT_BORDERCOLOR | DTT_SHADOWCOLOR | 
                       DTT_SHADOWTYPE | DTT_SHADOWOFFSET | DTT_BORDERSIZE |
                       DTT_FONTPROP | DTT_COLORPROP | DTT_STATEID | DTT_GLOWSIZE | 
                       DTT_CALCRECT | DTT_APPLYOVERLAY | DTT_COMPOSITED)

class DTTOPTS(CStructure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('crText', COLORREF),
        ('crBorder', COLORREF),
        ('crShadow', COLORREF),
        ('iTextShadowType', INT),
        ('ptShadowOffset', POINT),
        ('iBorderSize', INT),
        ('iFontPropId', INT),
        ('iColorPropId', INT),
        ('iStateId', INT),
        ('fApplyOverlay', BOOL),
        ('iGlowSize', INT),
        ('pfnDrawTextCallback', DTT_CALLBACK_PROC),
        ('lParam', LPARAM)
    ]
    dwSize: int
    dwFlags: int
    crText: int
    crBorder: int
    crShadow: int
    iTextShadowType: int
    ptShadowOffset: int
    iBorderSize: int
    iFontPropId: int
    iColorPropId: int
    iStateId: int
    fApplyOverlay: int
    iGlowSize: int
    pfnDrawTextCallback: FARPROC
    lParam: int

PDTTOPTS = PTR(DTTOPTS)

@uxtheme.foreign(HRESULT, HTHEME, HDC, INT, INT, LPCWSTR, INT, DWORD, LPRECT, PDTTOPTS)
def DrawThemeTextEx(hTheme: int, hdc: int, iPartId: int, iStateId: int, pszText: WT_LPWSTR, cchText: int, dwTextFlags: int, pRect: IPointer[RECT], pOptions: IPointer[DTTOPTS]) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME, HDC, INT, INT, INT, LPLOGFONTW)
def GetThemeFont(hTheme: int, hdc: int, iPartId: int, iStateId: int, iPropId: int, pFont: IPointer[LOGFONTW]) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME, INT, LPLOGFONTW)
def GetThemeSysFont(hTheme: int, iFontId: int, pFont: IPointer[LOGFONTW]) -> int: ...

TMT_RESERVEDLOW = 0
TMT_RESERVEDHIGH = 7999
TMT_DIBDATA = 2
TMT_GLYPHDIBDATA = 8
TMT_ENUM = 200
TMT_STRING = 201
TMT_INT = 202
TMT_BOOL = 203
TMT_COLOR = 204
TMT_MARGINS = 205
TMT_FILENAME = 206
TMT_SIZE = 207
TMT_POSITION = 208
TMT_RECT = 209
TMT_FONT = 210
TMT_INTLIST = 211
TMT_HBITMAP = 212
TMT_DISKSTREAM = 213
TMT_STREAM = 214
TMT_BITMAPREF = 215
TMT_FLOAT = 216
TMT_FLOATLIST = 217
TMT_COLORSCHEMES = 401
TMT_SIZES = 402
TMT_CHARSET = 403
TMT_NAME = 600
TMT_DISPLAYNAME = 601
TMT_TOOLTIP = 602
TMT_COMPANY = 603
TMT_AUTHOR = 604
TMT_COPYRIGHT = 605
TMT_URL = 606
TMT_VERSION = 607
TMT_DESCRIPTION = 608
TMT_FIRST_RCSTRING_NAME = TMT_DISPLAYNAME
TMT_LAST_RCSTRING_NAME = TMT_DESCRIPTION
TMT_CAPTIONFONT = 801
TMT_SMALLCAPTIONFONT = 802
TMT_MENUFONT = 803
TMT_STATUSFONT = 804
TMT_MSGBOXFONT = 805
TMT_ICONTITLEFONT = 806
TMT_HEADING1FONT = 807
TMT_HEADING2FONT = 808
TMT_BODYFONT = 809
TMT_FIRSTFONT = TMT_CAPTIONFONT
TMT_LASTFONT = TMT_BODYFONT
TMT_FLATMENUS = 1001
TMT_FIRSTBOOL = TMT_FLATMENUS
TMT_LASTBOOL = TMT_FLATMENUS
TMT_SIZINGBORDERWIDTH = 1201
TMT_SCROLLBARWIDTH = 1202
TMT_SCROLLBARHEIGHT = 1203
TMT_CAPTIONBARWIDTH = 1204
TMT_CAPTIONBARHEIGHT = 1205
TMT_SMCAPTIONBARWIDTH = 1206
TMT_SMCAPTIONBARHEIGHT = 1207
TMT_MENUBARWIDTH = 1208
TMT_MENUBARHEIGHT = 1209
TMT_PADDEDBORDERWIDTH = 1210
TMT_FIRSTSIZE = TMT_SIZINGBORDERWIDTH
TMT_LASTSIZE = TMT_PADDEDBORDERWIDTH
TMT_MINCOLORDEPTH = 1301
TMT_FIRSTINT = TMT_MINCOLORDEPTH
TMT_LASTINT = TMT_MINCOLORDEPTH
TMT_CSSNAME = 1401
TMT_XMLNAME = 1402
TMT_LASTUPDATED = 1403
TMT_ALIAS = 1404
TMT_FIRSTSTRING = TMT_CSSNAME
TMT_LASTSTRING = TMT_ALIAS
TMT_SCROLLBAR = 1601
TMT_BACKGROUND = 1602
TMT_ACTIVECAPTION = 1603
TMT_INACTIVECAPTION = 1604
TMT_MENU = 1605
TMT_WINDOW = 1606
TMT_WINDOWFRAME = 1607
TMT_MENUTEXT = 1608
TMT_WINDOWTEXT = 1609
TMT_CAPTIONTEXT = 1610
TMT_ACTIVEBORDER = 1611
TMT_INACTIVEBORDER = 1612
TMT_APPWORKSPACE = 1613
TMT_HIGHLIGHT = 1614
TMT_HIGHLIGHTTEXT = 1615
TMT_BTNFACE = 1616
TMT_BTNSHADOW = 1617
TMT_GRAYTEXT = 1618
TMT_BTNTEXT = 1619
TMT_INACTIVECAPTIONTEXT = 1620
TMT_BTNHIGHLIGHT = 1621
TMT_DKSHADOW3D = 1622
TMT_LIGHT3D = 1623
TMT_INFOTEXT = 1624
TMT_INFOBK = 1625
TMT_BUTTONALTERNATEFACE = 1626
TMT_HOTTRACKING = 1627
TMT_GRADIENTACTIVECAPTION = 1628
TMT_GRADIENTINACTIVECAPTION = 1629
TMT_MENUHILIGHT = 1630
TMT_MENUBAR = 1631
TMT_FIRSTCOLOR = TMT_SCROLLBAR
TMT_LASTCOLOR = TMT_MENUBAR
TMT_FROMHUE1 = 1801
TMT_FROMHUE2 = 1802
TMT_FROMHUE3 = 1803
TMT_FROMHUE4 = 1804
TMT_FROMHUE5 = 1805
TMT_TOHUE1 = 1806
TMT_TOHUE2 = 1807
TMT_TOHUE3 = 1808
TMT_TOHUE4 = 1809
TMT_TOHUE5 = 1810
TMT_FROMCOLOR1 = 2001
TMT_FROMCOLOR2 = 2002
TMT_FROMCOLOR3 = 2003
TMT_FROMCOLOR4 = 2004
TMT_FROMCOLOR5 = 2005
TMT_TOCOLOR1 = 2006
TMT_TOCOLOR2 = 2007
TMT_TOCOLOR3 = 2008
TMT_TOCOLOR4 = 2009
TMT_TOCOLOR5 = 2010
TMT_TRANSPARENT = 2201
TMT_AUTOSIZE = 2202
TMT_BORDERONLY = 2203
TMT_COMPOSITED = 2204
TMT_BGFILL = 2205
TMT_GLYPHTRANSPARENT = 2206
TMT_GLYPHONLY = 2207
TMT_ALWAYSSHOWSIZINGBAR = 2208
TMT_MIRRORIMAGE = 2209
TMT_UNIFORMSIZING = 2210
TMT_INTEGRALSIZING = 2211
TMT_SOURCEGROW = 2212
TMT_SOURCESHRINK = 2213
TMT_DRAWBORDERS = 2214
TMT_NOETCHEDEFFECT = 2215
TMT_TEXTAPPLYOVERLAY = 2216
TMT_TEXTGLOW = 2217
TMT_TEXTITALIC = 2218
TMT_COMPOSITEDOPAQUE = 2219
TMT_LOCALIZEDMIRRORIMAGE = 2220
TMT_IMAGECOUNT = 2401
TMT_ALPHALEVEL = 2402
TMT_BORDERSIZE = 2403
TMT_ROUNDCORNERWIDTH = 2404
TMT_ROUNDCORNERHEIGHT = 2405
TMT_GRADIENTRATIO1 = 2406
TMT_GRADIENTRATIO2 = 2407
TMT_GRADIENTRATIO3 = 2408
TMT_GRADIENTRATIO4 = 2409
TMT_GRADIENTRATIO5 = 2410
TMT_PROGRESSCHUNKSIZE = 2411
TMT_PROGRESSSPACESIZE = 2412
TMT_SATURATION = 2413
TMT_TEXTBORDERSIZE = 2414
TMT_ALPHATHRESHOLD = 2415
TMT_WIDTH = 2416
TMT_HEIGHT = 2417
TMT_GLYPHINDEX = 2418
TMT_TRUESIZESTRETCHMARK = 2419
TMT_MINDPI1 = 2420
TMT_MINDPI2 = 2421
TMT_MINDPI3 = 2422
TMT_MINDPI4 = 2423
TMT_MINDPI5 = 2424
TMT_TEXTGLOWSIZE = 2425
TMT_FRAMESPERSECOND = 2426
TMT_PIXELSPERFRAME = 2427
TMT_ANIMATIONDELAY = 2428
TMT_GLOWINTENSITY = 2429
TMT_OPACITY = 2430
TMT_COLORIZATIONCOLOR = 2431
TMT_COLORIZATIONOPACITY = 2432
TMT_MINDPI6 = 2433
TMT_MINDPI7 = 2434
TMT_GLYPHFONT = 2601
TMT_IMAGEFILE = 3001
TMT_IMAGEFILE1 = 3002
TMT_IMAGEFILE2 = 3003
TMT_IMAGEFILE3 = 3004
TMT_IMAGEFILE4 = 3005
TMT_IMAGEFILE5 = 3006
TMT_GLYPHIMAGEFILE = 3008
TMT_IMAGEFILE6 = 3009
TMT_IMAGEFILE7 = 3010
TMT_TEXT = 3201
TMT_CLASSICVALUE = 3202
TMT_OFFSET = 3401
TMT_TEXTSHADOWOFFSET = 3402
TMT_MINSIZE = 3403
TMT_MINSIZE1 = 3404
TMT_MINSIZE2 = 3405
TMT_MINSIZE3 = 3406
TMT_MINSIZE4 = 3407
TMT_MINSIZE5 = 3408
TMT_NORMALSIZE = 3409
TMT_MINSIZE6 = 3410
TMT_MINSIZE7 = 3411
TMT_SIZINGMARGINS = 3601
TMT_CONTENTMARGINS = 3602
TMT_CAPTIONMARGINS = 3603
TMT_BORDERCOLOR = 3801
TMT_FILLCOLOR = 3802
TMT_TEXTCOLOR = 3803
TMT_EDGELIGHTCOLOR = 3804
TMT_EDGEHIGHLIGHTCOLOR = 3805
TMT_EDGESHADOWCOLOR = 3806
TMT_EDGEDKSHADOWCOLOR = 3807
TMT_EDGEFILLCOLOR = 3808
TMT_TRANSPARENTCOLOR = 3809
TMT_GRADIENTCOLOR1 = 3810
TMT_GRADIENTCOLOR2 = 3811
TMT_GRADIENTCOLOR3 = 3812
TMT_GRADIENTCOLOR4 = 3813
TMT_GRADIENTCOLOR5 = 3814
TMT_SHADOWCOLOR = 3815
TMT_GLOWCOLOR = 3816
TMT_TEXTBORDERCOLOR = 3817
TMT_TEXTSHADOWCOLOR = 3818
TMT_GLYPHTEXTCOLOR = 3819
TMT_GLYPHTRANSPARENTCOLOR = 3820
TMT_FILLCOLORHINT = 3821
TMT_BORDERCOLORHINT = 3822
TMT_ACCENTCOLORHINT = 3823
TMT_TEXTCOLORHINT = 3824
TMT_HEADING1TEXTCOLOR = 3825
TMT_HEADING2TEXTCOLOR = 3826
TMT_BODYTEXTCOLOR = 3827
TMT_BGTYPE = 4001
TMT_BORDERTYPE = 4002
TMT_FILLTYPE = 4003
TMT_SIZINGTYPE = 4004
TMT_HALIGN = 4005
TMT_CONTENTALIGNMENT = 4006
TMT_VALIGN = 4007
TMT_OFFSETTYPE = 4008
TMT_ICONEFFECT = 4009
TMT_TEXTSHADOWTYPE = 4010
TMT_IMAGELAYOUT = 4011
TMT_GLYPHTYPE = 4012
TMT_IMAGESELECTTYPE = 4013
TMT_GLYPHFONTSIZINGTYPE = 4014
TMT_TRUESIZESCALINGTYPE = 4015
TMT_USERPICTURE = 5001
TMT_DEFAULTPANESIZE = 5002
TMT_BLENDCOLOR = 5003
TMT_CUSTOMSPLITRECT = 5004
TMT_ANIMATIONBUTTONRECT = 5005
TMT_ANIMATIONDURATION = 5006
TMT_TRANSITIONDURATIONS = 6000
TMT_SCALEDBACKGROUND = 7001
TMT_ATLASIMAGE = 8000
TMT_ATLASINPUTIMAGE = 8001
TMT_ATLASRECT = 8002

PO_STATE = 0
PO_PART = 1
PO_CLASS = 2
PO_GLOBAL = 3
PO_NOTFOUND = 4
PROPERTYORIGIN = UINT

@uxtheme.foreign(BOOL, HTHEME, INT, INT)
def IsThemePartDefined(hTheme: int, iPartId: int, iStateId: int) -> int: ...

@uxtheme.foreign(BOOL, HTHEME, INT, INT)
def IsThemeBackgroundPartiallyTransparent(hTheme: int, iPartId: int, iStateId: int) -> int: ...

@uxtheme.foreign(HRESULT, HTHEME, INT, INT, INT, LPCOLORREF)
def GetThemeColor(hTheme: int, iPartId: int, iStateId: int, iPropId: int, pColor: IPointer[COLORREF]) -> int: ...

class Theme(Handle):
    """
    Class, representing Windows theme.
    """
    
    @classmethod
    def create(cls, hwnd: int | HANDLE, class_list: str) -> 'Theme':
        theme = cls(OpenThemeData(hwnd, class_list))
        if not theme.value: raise WinException()
        return theme
    
    def close(self):
        hr = CloseThemeData(self)
        if FAILED(hr): raise COMError(hr)
        self._closed = True
        
    def draw_background(self, dc: int | HANDLE, part_id: int, state_id: int, rect: RECT, clip: RECT=NULL):
        """
        Draw the border and fill defined by the visual style for the specified control part.
        """
        hr = DrawThemeBackground(self, dc, part_id, state_id, rect.ref(), clip.ref() if clip is not NULL else NULL)
        if FAILED(hr): raise COMError(hr)
        
    def draw_text(self, dc: int | HANDLE, part_id: int, state_id: int, text: str, flags: int, rect: RECT, options: DTTOPTS | None = None):
        """
        Draws text using the color and font defined by the visual style.
        """
        if options is None:
            options = DTTOPTS()
        options.dwSize = options.size()
        hr = DrawThemeTextEx(self, dc, part_id, state_id, text, len(text), flags, rect.ref(), options.ref())
        if FAILED(hr): raise COMError(hr)
        
    def get_font(self, dc: int | HANDLE, part_id: int, state_id: int) -> LOGFONTW:
        """
        Get the themed font from theme file.
        """
        lf = LOGFONTW()
        hr = GetThemeFont(self, dc, part_id, state_id, TMT_FONT, lf.ref())
        if FAILED(hr): raise COMError(hr)
        return lf
    
    def get_system_font(self, font_id: int) -> LOGFONTW:
        """
        Get the system font from theme file.
        """
        lf = LOGFONTW()
        hr = GetThemeSysFont(self, font_id, lf.ref())
        if FAILED(hr): raise COMError(hr)
        return lf
    
    def partially_transparent(self, part_id: int, state_id: int) -> bool:
        """
        Check the visual style background is partially transparent.
        """
        return IsThemeBackgroundPartiallyTransparent(self, part_id, state_id) != FALSE

    def part_defined(self, part_id: int, state_id: int) -> bool:
        """
        Check the given visual style part is defined in theme.
        """
        return IsThemePartDefined(self, part_id, state_id) != FALSE

    def get_color(self, part_id: int, state_id: int, prop_id: int) -> Color.BGR:
        """
        Get the visual style part color which defined in theme.
        """
        color = COLORREF()
        hr = GetThemeColor(self, part_id, state_id, prop_id, byref(color))
        if FAILED(hr): raise COMError(hr)
        return Color.BGR(color.value)

class VisualStyleElement:
    THEME_HANDLES: ClassVar[dict[str, Theme]] = {}
    
    @staticmethod
    def refresh(self):
        self.THEME_HANDLES.clear()
    
    class_name: str
    part_id: int
    state_id: int
    
    def __init__(self, class_name: str, part_id: int, state_id: int = 0):
        self.class_name = class_name
        self.part_id = part_id
        self.state_id = state_id
        
    def get(self, hwnd: int | HANDLE | None = None) -> Theme:
        """
        Get the Theme handle from Visual Style element.
        """
        if hwnd is None:
            theme = self.THEME_HANDLES.get(self.class_name, None)
            if theme is None:
                theme = Theme.create(NULL, self.class_name)
                self.THEME_HANDLES[self.class_name] = theme
        else:
            theme = Theme.create(NULL, self.class_name)
        return theme
    
    def draw_background(self, dc: DC, rc: RECT, hwnd: int | HANDLE | None = None):
        """
        Draw the background of Visual Style element.
        """
        self.get(hwnd).draw_background(dc, self.part_id, self.state_id, rc, NULL)
        
    def draw_text(self, dc: int | HANDLE, text: str, flags: int, rect: RECT, options: DTTOPTS | None = None, hwnd: int | HANDLE | None = None):
        """
        Draws text of Visual Style element.
        """
        self.get(hwnd).draw_text(dc, self.part_id, self.state_id, text, flags, rect, options)
        
    def get_font(self, dc: int | HANDLE, hwnd: int | HANDLE | None = None) -> LOGFONTW:
        """
        Get the font of Visual Style element.
        """
        return self.get(hwnd).get_font(dc, self.part_id, self.state_id)
        
    def get_system_font(self, font_id: int, hwnd: int | HANDLE | None = None) -> LOGFONTW:
        """
        Get the system font of Visual Style element.
        """
        return self.get(hwnd).get_system_font(font_id)
 
    def partially_transparent(self, hwnd: int | HANDLE | None = None) -> bool:
        """
        Check the Visual Style Element background is partially transparent.
        """
        return self.get(hwnd).partially_transparent(self.part_id, self.state_id)
 
    def defined(self, hwnd: int | HANDLE | None = None) -> bool:
        """
        Check the Visual Style Element is defined.
        """
        return self.get(hwnd).part_defined(self.part_id, self.state_id)
    
    def color(self, property_id: int, hwnd: int | HANDLE | None = None) -> Color.BGR:
        """
        Get the color of the Visual Style Element.
        """
        return self.get(hwnd).get_color(self.part_id, self.state_id, property_id)
 
class VisualStyleElements:
    class Button:
        class PushButton:
            NORMAL = VisualStyleElement('BUTTON', 1, 1)
            HOT = VisualStyleElement('BUTTON', 1, 2)
            PRESSED = VisualStyleElement('BUTTON', 1, 3)
            DISABLED = VisualStyleElement('BUTTON', 1, 4)
            DEFAULT = VisualStyleElement('BUTTON', 1, 5)
            
        class RadioButton:
            UNCHECKED_NORMAL = VisualStyleElement('BUTTON', 2, 1)
            UNCHECKED_HOT = VisualStyleElement('BUTTON', 2, 2)
            UNCHECKED_PRESSED = VisualStyleElement('BUTTON', 2, 3)
            UNCHECKED_DISABLED = VisualStyleElement('BUTTON', 2, 4)
            CHECKED_NORMAL = VisualStyleElement('BUTTON', 2, 5)
            CHECKED_HOT = VisualStyleElement('BUTTON', 2, 6)
            CHECKED_PRESSED = VisualStyleElement('BUTTON', 2, 7)
            CHECKED_DISABLED = VisualStyleElement('BUTTON', 2, 8)
        
        class CheckBox:
            UNCHECKED_NORMAL = VisualStyleElement('BUTTON', 3, 1)
            UNCHECKED_HOT = VisualStyleElement('BUTTON', 3, 2)
            UNCHECKED_PRESSED = VisualStyleElement('BUTTON', 3, 3)
            UNCHECKED_DISABLED = VisualStyleElement('BUTTON', 3, 4)
            CHECKED_NORMAL = VisualStyleElement('BUTTON', 3, 5)
            CHECKED_HOT = VisualStyleElement('BUTTON', 3, 6)
            CHECKED_PRESSED = VisualStyleElement('BUTTON', 3, 7)
            CHECKED_DISABLED = VisualStyleElement('BUTTON', 3, 8)
            MIXED_NORMAL = VisualStyleElement('BUTTON', 3, 9)
            MIXED_HOT = VisualStyleElement('BUTTON', 3, 10)
            MIXED_PRESSED = VisualStyleElement('BUTTON', 3, 11)
            MIXED_DISABLED = VisualStyleElement('BUTTON', 3, 12)
        
        class GroupBox:
            NORMAL = VisualStyleElement('BUTTON', 4, 1)
            DISABLED = VisualStyleElement('BUTTON', 4, 2)
            
        class UserButton:
            NORMAL = VisualStyleElement('BUTTON', 5, 0)
            
    class ComboBox:
        class DropDownButton:
            NORMAL = VisualStyleElement('COMBOBOX', 1, 1)
            HOT = VisualStyleElement('COMBOBOX', 1, 2)
            PRESSED = VisualStyleElement('COMBOBOX', 1, 3)
            DISABLED = VisualStyleElement('COMBOBOX', 1, 4)
            
        class Border:
            NORMAL = VisualStyleElement('COMBOBOX', 4, 3)
            
        class ReadOnlyButton:
            NORMAL = VisualStyleElement('COMBOBOX', 5, 2)
            
        class DropDownButtonRight:
            NORMAL = VisualStyleElement('COMBOBOX', 6, 1)
            
        class DropDownButtonLeft:
            NORMAL = VisualStyleElement('COMBOBOX', 7, 2)
            
    class Page:
        class Up:
            NORMAL = VisualStyleElement('PAGE', 1, 1)
            HOT = VisualStyleElement('PAGE', 1, 2)
            PRESSED = VisualStyleElement('PAGE', 1, 3)
            DISABLED = VisualStyleElement('PAGE', 1, 4)
            
        class Down:
            NORMAL = VisualStyleElement('PAGE', 2, 1)
            HOT = VisualStyleElement('PAGE', 2, 2)
            PRESSED = VisualStyleElement('PAGE', 2, 3)
            DISABLED = VisualStyleElement('PAGE', 2, 4)
            
        class UpHorizontal:
            NORMAL = VisualStyleElement('PAGE', 3, 1)
            HOT = VisualStyleElement('PAGE', 3, 2)
            PRESSED = VisualStyleElement('PAGE', 3, 3)
            DISABLED = VisualStyleElement('PAGE', 3, 4)
            
        class DownHorizontal:
            NORMAL = VisualStyleElement('PAGE', 4, 1)
            HOT = VisualStyleElement('PAGE', 4, 2)
            PRESSED = VisualStyleElement('PAGE', 4, 3)
            DISABLED = VisualStyleElement('PAGE', 4, 4)

    class Spin:
        class Up:
            NORMAL = VisualStyleElement('SPIN', 1, 1)
            HOT = VisualStyleElement('SPIN', 1, 2)
            PRESSED = VisualStyleElement('SPIN', 1, 3)
            DISABLED = VisualStyleElement('SPIN', 1, 4)
            
        class Down:
            NORMAL = VisualStyleElement('SPIN', 2, 1)
            HOT = VisualStyleElement('SPIN', 2, 2)
            PRESSED = VisualStyleElement('SPIN', 2, 3)
            DISABLED = VisualStyleElement('SPIN', 2, 4)
            
        class UpHorizontal:
            NORMAL = VisualStyleElement('SPIN', 3, 1)
            HOT = VisualStyleElement('SPIN', 3, 2)
            PRESSED = VisualStyleElement('SPIN', 3, 3)
            DISABLED = VisualStyleElement('SPIN', 3, 4)
            
        class DownHorizontal:
            NORMAL = VisualStyleElement('SPIN', 4, 1)
            HOT = VisualStyleElement('SPIN', 4, 2)
            PRESSED = VisualStyleElement('SPIN', 4, 3)
            DISABLED = VisualStyleElement('SPIN', 4, 4)

    class ScrollBar:
        class ArrowButton:
            UP_NORMAL = VisualStyleElement('SCROLLBAR', 1, 1)
            UP_HOT = VisualStyleElement('SCROLLBAR', 1, 2)
            UP_PRESSED = VisualStyleElement('SCROLLBAR', 1, 3)
            UP_DISABLED = VisualStyleElement('SCROLLBAR', 1, 4)
            DOWN_NORMAL = VisualStyleElement('SCROLLBAR', 1, 5)
            DOWN_HOT = VisualStyleElement('SCROLLBAR', 1, 6)
            DOWN_PRESSED = VisualStyleElement('SCROLLBAR', 1, 7)
            DOWN_DISABLED = VisualStyleElement('SCROLLBAR', 1, 8)
            LEFT_NORMAL = VisualStyleElement('SCROLLBAR', 1, 9)
            LEFT_HOT = VisualStyleElement('SCROLLBAR', 1, 10)
            LEFT_PRESSED = VisualStyleElement('SCROLLBAR', 1, 11)
            LEFT_DISABLED = VisualStyleElement('SCROLLBAR', 1, 12)
            RIGHT_NORMAL = VisualStyleElement('SCROLLBAR', 1, 13)
            RIGHT_HOT = VisualStyleElement('SCROLLBAR', 1, 14)
            RIGHT_PRESSED = VisualStyleElement('SCROLLBAR', 1, 15)
            RIGHT_DISABLED = VisualStyleElement('SCROLLBAR', 1, 16)
            
        class ThumbButtonHorizontal:
            NORMAL = VisualStyleElement('SCROLLBAR', 2, 1)
            HOT = VisualStyleElement('SCROLLBAR', 2, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 2, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 2, 4)
            
        class ThumbButtonVertical:
            NORMAL = VisualStyleElement('SCROLLBAR', 3, 1)
            HOT = VisualStyleElement('SCROLLBAR', 3, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 3, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 3, 4)
            
        class RightTrackHorizontal:
            NORMAL = VisualStyleElement('SCROLLBAR', 4, 1)
            HOT = VisualStyleElement('SCROLLBAR', 4, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 4, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 4, 4)
            
        class LeftTrackHorizontal:
            NORMAL = VisualStyleElement('SCROLLBAR', 5, 1)
            HOT = VisualStyleElement('SCROLLBAR', 5, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 5, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 5, 4)
            
        class LowerTrackVertical:
            NORMAL = VisualStyleElement('SCROLLBAR', 6, 1)
            HOT = VisualStyleElement('SCROLLBAR', 6, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 6, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 6, 4)
            
        class UpperTrackVertical:
            NORMAL = VisualStyleElement('SCROLLBAR', 7, 1)
            HOT = VisualStyleElement('SCROLLBAR', 7, 2)
            PRESSED = VisualStyleElement('SCROLLBAR', 7, 3)
            DISABLED = VisualStyleElement('SCROLLBAR', 7, 4)
            
        class GripperHorizontal:
            NORMAL = VisualStyleElement('SCROLLBAR', 8, 0)
            
        class GripperVertical:
            NORMAL = VisualStyleElement('SCROLLBAR', 9, 0)
            
        class SizeBox:
            RIGHT_ALIGN = VisualStyleElement('SCROLLBAR', 10, 1)
            LEFT_ALIGN = VisualStyleElement('SCROLLBAR', 10, 2)

    class Tab:
        class TabItem:
            NORMAL = VisualStyleElement('TAB', 1, 1)
            HOT = VisualStyleElement('TAB', 1, 2)
            PRESSED = VisualStyleElement('TAB', 1, 3)
            DISABLED = VisualStyleElement('TAB', 1, 4)
            
        class TabItemLeftEdge:
            NORMAL = VisualStyleElement('TAB', 2, 1)
            HOT = VisualStyleElement('TAB', 2, 2)
            PRESSED = VisualStyleElement('TAB', 2, 3)
            DISABLED = VisualStyleElement('TAB', 2, 4)
            
        class TabItemRightEdge:
            NORMAL = VisualStyleElement('TAB', 3, 1)
            HOT = VisualStyleElement('TAB', 3, 2)
            PRESSED = VisualStyleElement('TAB', 3, 3)
            DISABLED = VisualStyleElement('TAB', 3, 4)
            
        class TabItemBothEdges:
            NORMAL = VisualStyleElement('TAB', 4, 0)
            
        class TopTabItem:
            NORMAL = VisualStyleElement('TAB', 5, 1)
            HOT = VisualStyleElement('TAB', 5, 2)
            PRESSED = VisualStyleElement('TAB', 5, 3)
            DISABLED = VisualStyleElement('TAB', 5, 4)
            
        class TopTabItemLeftEdge:
            NORMAL = VisualStyleElement('TAB', 6, 1)
            HOT = VisualStyleElement('TAB', 6, 2)
            PRESSED = VisualStyleElement('TAB', 6, 3)
            DISABLED = VisualStyleElement('TAB', 6, 4)
            
        class TopTabItemRightEdge:
            NORMAL = VisualStyleElement('TAB', 7, 1)
            HOT = VisualStyleElement('TAB', 7, 2)
            PRESSED = VisualStyleElement('TAB', 7, 3)
            DISABLED = VisualStyleElement('TAB', 7, 4)
            
        class TopTabItemBothEdges:
            NORMAL = VisualStyleElement('TAB', 8, 0)
            
        class Pane:
            NORMAL = VisualStyleElement('TAB', 9, 0)
            
        class Body:
            NORMAL = VisualStyleElement('TAB', 10, 0)

    class ExplorerBar:
        class HeaderBackground:
            NORMAL = VisualStyleElement('EXPLORERBAR', 1, 0)
            
        class HeaderClose:
            NORMAL = VisualStyleElement('EXPLORERBAR', 2, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 2, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 2, 3)
            
        class HeaderPin:
            NORMAL = VisualStyleElement('EXPLORERBAR', 3, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 3, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 3, 3)
            SELECTED_NORMAL = VisualStyleElement('EXPLORERBAR', 3, 4)
            SELECTED_HOT = VisualStyleElement('EXPLORERBAR', 3, 5)
            SELECTED_PRESSED = VisualStyleElement('EXPLORERBAR', 3, 6)
            
        class IEBarMenu:
            NORMAL = VisualStyleElement('EXPLORERBAR', 4, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 4, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 4, 3)
            
        class NormalGroupBackground:
            NORMAL = VisualStyleElement('EXPLORERBAR', 5, 0)
            
        class NormalGroupCollapse:
            NORMAL = VisualStyleElement('EXPLORERBAR', 6, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 6, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 6, 3)
            
        class NormalGroupExpand:
            NORMAL = VisualStyleElement('EXPLORERBAR', 7, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 7, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 7, 3)
            
        class NormalGroupHead:
            NORMAL = VisualStyleElement('EXPLORERBAR', 8, 0)
            
        class SpecialGroupBackground:
            NORMAL = VisualStyleElement('EXPLORERBAR', 9, 0)
            
        class SpecialGroupCollapse:
            NORMAL = VisualStyleElement('EXPLORERBAR', 10, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 10, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 10, 3)
            
        class SpecialGroupExpand:
            NORMAL = VisualStyleElement('EXPLORERBAR', 11, 1)
            HOT = VisualStyleElement('EXPLORERBAR', 11, 2)
            PRESSED = VisualStyleElement('EXPLORERBAR', 11, 3)
            
        class SpecialGroupHead:
            NORMAL = VisualStyleElement('EXPLORERBAR', 12, 0)

    class Header:
        class Item:
            NORMAL = VisualStyleElement('HEADER', 1, 1)
            HOT = VisualStyleElement('HEADER', 1, 2)
            PRESSED = VisualStyleElement('HEADER', 1, 3)
            
        class ItemLeft:
            NORMAL = VisualStyleElement('HEADER', 2, 1)
            HOT = VisualStyleElement('HEADER', 2, 2)
            PRESSED = VisualStyleElement('HEADER', 2, 3)
            
        class ItemRight:
            NORMAL = VisualStyleElement('HEADER', 3, 1)
            HOT = VisualStyleElement('HEADER', 3, 2)
            PRESSED = VisualStyleElement('HEADER', 3, 3)
            
        class SortArrow:
            SORTED_UP = VisualStyleElement('HEADER', 4, 1)
            SORTED_DOWN = VisualStyleElement('HEADER', 4, 2)

    class ListView:
        class Item:
            NORMAL = VisualStyleElement('LISTVIEW', 1, 1)
            HOT = VisualStyleElement('LISTVIEW', 1, 2)
            SELECTED = VisualStyleElement('LISTVIEW', 1, 3)
            DISABLED = VisualStyleElement('LISTVIEW', 1, 4)
            SELECTED_NOT_FOCUS = VisualStyleElement('LISTVIEW', 1, 5)
            
        class Group:
            NORMAL = VisualStyleElement('LISTVIEW', 2, 0)
            
        class Detail:
            NORMAL = VisualStyleElement('LISTVIEW', 3, 0)
            
        class SortedDetail:
            NORMAL = VisualStyleElement('LISTVIEW', 4, 0)
            
        class EmptyText:
            NORMAL = VisualStyleElement('LISTVIEW', 5, 0)

    class MenuBand:
        class NewApplicationButton:
            NORMAL = VisualStyleElement('MENUBAND', 1, 1)
            HOT = VisualStyleElement('MENUBAND', 1, 2)
            PRESSED = VisualStyleElement('MENUBAND', 1, 3)
            DISABLED = VisualStyleElement('MENUBAND', 1, 4)
            CHECKED = VisualStyleElement('MENUBAND', 1, 5)
            HOT_CHECKED = VisualStyleElement('MENUBAND', 1, 6)
            
        class Separator:
            NORMAL = VisualStyleElement('MENUBAND', 2, 0)

    class Menu:
        class Item:
            NORMAL = VisualStyleElement('MENU', 1, 1)
            SELECTED = VisualStyleElement('MENU', 1, 2)
            DEMOTED = VisualStyleElement('MENU', 1, 3)
            
        class DropDown:
            NORMAL = VisualStyleElement('MENU', 2, 0)
            
        class BarItem:
            NORMAL = VisualStyleElement('MENU', 3, 0)
            
        class BarDropDown:
            NORMAL = VisualStyleElement('MENU', 4, 0)
            
        class Chevron:
            NORMAL = VisualStyleElement('MENU', 5, 0)
            
        class Separator:
            NORMAL = VisualStyleElement('MENU', 6, 0)

    class ProgressBar:
        class Bar:
            NORMAL = VisualStyleElement('PROGRESS', 1, 0)
            
        class BarVertical:
            NORMAL = VisualStyleElement('PROGRESS', 2, 0)
            
        class Chunk:
            NORMAL = VisualStyleElement('PROGRESS', 3, 0)
            
        class ChunkVertical:
            NORMAL = VisualStyleElement('PROGRESS', 4, 0)

    class Rebar:
        class Gripper:
            NORMAL = VisualStyleElement('REBAR', 1, 0)
            
        class GripperVertical:
            NORMAL = VisualStyleElement('REBAR', 2, 0)
            
        class Band:
            NORMAL = VisualStyleElement('REBAR', 3, 0)
            
        class Chevron:
            NORMAL = VisualStyleElement('REBAR', 4, 1)
            HOT = VisualStyleElement('REBAR', 4, 2)
            PRESSED = VisualStyleElement('REBAR', 4, 3)
            
        class ChevronVertical:
            NORMAL = VisualStyleElement('REBAR', 5, 1)
            HOT = VisualStyleElement('REBAR', 5, 2)
            PRESSED = VisualStyleElement('REBAR', 5, 3)

    class StartPanel:
        class UserPane:
            NORMAL = VisualStyleElement('STARTPANEL', 1, 0)
            
        class MorePrograms:
            NORMAL = VisualStyleElement('STARTPANEL', 2, 0)
            
        class MoreProgramsArrow:
            NORMAL = VisualStyleElement('STARTPANEL', 3, 1)
            HOT = VisualStyleElement('STARTPANEL', 3, 2)
            PRESSED = VisualStyleElement('STARTPANEL', 3, 3)
            
        class ProgList:
            NORMAL = VisualStyleElement('STARTPANEL', 4, 0)
            
        class ProgListSeparator:
            NORMAL = VisualStyleElement('STARTPANEL', 5, 0)
            
        class PlaceList:
            NORMAL = VisualStyleElement('STARTPANEL', 6, 0)
            
        class PlaceListSeparator:
            NORMAL = VisualStyleElement('STARTPANEL', 7, 0)
            
        class LogOff:
            NORMAL = VisualStyleElement('STARTPANEL', 8, 0)
            
        class LogOffButtons:
            NORMAL = VisualStyleElement('STARTPANEL', 9, 1)
            HOT = VisualStyleElement('STARTPANEL', 9, 2)
            PRESSED = VisualStyleElement('STARTPANEL', 9, 3)
            
        class UserPicture:
            NORMAL = VisualStyleElement('STARTPANEL', 10, 0)
            
        class Preview:
            NORMAL = VisualStyleElement('STARTPANEL', 11, 0)

    class Status:
        class Bar:
            NORMAL = VisualStyleElement('STATUS', 0, 0)
            
        class Pane:
            NORMAL = VisualStyleElement('STATUS', 1, 0)
            
        class GripperPane:
            NORMAL = VisualStyleElement('STATUS', 2, 0)
            
        class Gripper:
            NORMAL = VisualStyleElement('STATUS', 3, 0)

    class TaskBand:
        class GroupCount:
            NORMAL = VisualStyleElement('TASKBAND', 1, 0)
            
        class FlashButton:
            NORMAL = VisualStyleElement('TASKBAND', 2, 0)
            
        class FlashButtonGroupMenu:
            NORMAL = VisualStyleElement('TASKBAND', 3, 0)

    class TaskbarClock:
        class Time:
            NORMAL = VisualStyleElement('CLOCK', 1, 1)

    class Taskbar:
        class BackgroundBottom:
            NORMAL = VisualStyleElement('TASKBAR', 1, 0)
            
        class BackgroundRight:
            NORMAL = VisualStyleElement('TASKBAR', 2, 0)
            
        class BackgroundTop:
            NORMAL = VisualStyleElement('TASKBAR', 3, 0)
            
        class BackgroundLeft:
            NORMAL = VisualStyleElement('TASKBAR', 4, 0)
            
        class SizingBarBottom:
            NORMAL = VisualStyleElement('TASKBAR', 5, 0)
            
        class SizingBarRight:
            NORMAL = VisualStyleElement('TASKBAR', 6, 0)
            
        class SizingBarTop:
            NORMAL = VisualStyleElement('TASKBAR', 7, 0)
            
        class SizingBarLeft:
            NORMAL = VisualStyleElement('TASKBAR', 8, 0)

    class ToolBar:
        class Button:
            NORMAL = VisualStyleElement('TOOLBAR', 1, 1)
            HOT = VisualStyleElement('TOOLBAR', 1, 2)
            PRESSED = VisualStyleElement('TOOLBAR', 1, 3)
            DISABLED = VisualStyleElement('TOOLBAR', 1, 4)
            CHECKED = VisualStyleElement('TOOLBAR', 1, 5)
            HOT_CHECKED = VisualStyleElement('TOOLBAR', 1, 6)
            
        class DropDownButton:
            NORMAL = VisualStyleElement('TOOLBAR', 2, 1)
            HOT = VisualStyleElement('TOOLBAR', 2, 2)
            PRESSED = VisualStyleElement('TOOLBAR', 2, 3)
            DISABLED = VisualStyleElement('TOOLBAR', 2, 4)
            CHECKED = VisualStyleElement('TOOLBAR', 2, 5)
            HOT_CHECKED = VisualStyleElement('TOOLBAR', 2, 6)
            
        class SplitButton:
            NORMAL = VisualStyleElement('TOOLBAR', 3, 1)
            HOT = VisualStyleElement('TOOLBAR', 3, 2)
            PRESSED = VisualStyleElement('TOOLBAR', 3, 3)
            DISABLED = VisualStyleElement('TOOLBAR', 3, 4)
            CHECKED = VisualStyleElement('TOOLBAR', 3, 5)
            HOT_CHECKED = VisualStyleElement('TOOLBAR', 3, 6)
            
        class SplitButtonDropDown:
            NORMAL = VisualStyleElement('TOOLBAR', 4, 1)
            HOT = VisualStyleElement('TOOLBAR', 4, 2)
            PRESSED = VisualStyleElement('TOOLBAR', 4, 3)
            DISABLED = VisualStyleElement('TOOLBAR', 4, 4)
            CHECKED = VisualStyleElement('TOOLBAR', 4, 5)
            HOT_CHECKED = VisualStyleElement('TOOLBAR', 4, 6)
            
        class SeparatorHorizontal:
            NORMAL = VisualStyleElement('TOOLBAR', 5, 0)
            
        class SeparatorVertical:
            NORMAL = VisualStyleElement('TOOLBAR', 6, 0)

    class ToolTip:
        class Standard:
            NORMAL = VisualStyleElement('TOOLTIP', 1, 1)
            LINK = VisualStyleElement('TOOLTIP', 1, 2)
            
        class StandardTitle:
            NORMAL = VisualStyleElement('TOOLTIP', 2, 0)
            
        class Balloon:
            NORMAL = VisualStyleElement('TOOLTIP', 3, 1)
            LINK = VisualStyleElement('TOOLTIP', 3, 2)
            
        class BalloonTitle:
            NORMAL = VisualStyleElement('TOOLTIP', 4, 0)
            
        class Close:
            NORMAL = VisualStyleElement('TOOLTIP', 5, 1)
            HOT = VisualStyleElement('TOOLTIP', 5, 2)
            PRESSED = VisualStyleElement('TOOLTIP', 5, 3)

    class TrackBar:
        class Track:
            NORMAL = VisualStyleElement('TRACKBAR', 1, 1)
            
        class TrackVertical:
            NORMAL = VisualStyleElement('TRACKBAR', 2, 1)
            
        class Thumb:
            NORMAL = VisualStyleElement('TRACKBAR', 3, 1)
            HOT = VisualStyleElement('TRACKBAR', 3, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 3, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 3, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 3, 5)
            
        class ThumbBottom:
            NORMAL = VisualStyleElement('TRACKBAR', 4, 1)
            HOT = VisualStyleElement('TRACKBAR', 4, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 4, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 4, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 4, 5)
            
        class ThumbTop:
            NORMAL = VisualStyleElement('TRACKBAR', 5, 1)
            HOT = VisualStyleElement('TRACKBAR', 5, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 5, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 5, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 5, 5)
            
        class ThumbVertical:
            NORMAL = VisualStyleElement('TRACKBAR', 6, 1)
            HOT = VisualStyleElement('TRACKBAR', 6, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 6, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 6, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 6, 5)
            
        class ThumbLeft:
            NORMAL = VisualStyleElement('TRACKBAR', 7, 1)
            HOT = VisualStyleElement('TRACKBAR', 7, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 7, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 7, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 7, 5)
            
        class ThumbRight:
            NORMAL = VisualStyleElement('TRACKBAR', 8, 1)
            HOT = VisualStyleElement('TRACKBAR', 8, 2)
            PRESSED = VisualStyleElement('TRACKBAR', 8, 3)
            FOCUSED = VisualStyleElement('TRACKBAR', 8, 4)
            DISABLED = VisualStyleElement('TRACKBAR', 8, 5)
            
        class Ticks:
            NORMAL = VisualStyleElement('TRACKBAR', 9, 1)
            
        class TicksVertical:
            NORMAL = VisualStyleElement('TRACKBAR', 10, 1)

    class TreeView:
        class Item:
            NORMAL = VisualStyleElement('TREEVIEW', 1, 1)
            HOT = VisualStyleElement('TREEVIEW', 1, 2)
            SELECTED = VisualStyleElement('TREEVIEW', 1, 3)
            DISABLED = VisualStyleElement('TREEVIEW', 1, 4)
            SELECTED_NOT_FOCUS = VisualStyleElement('TREEVIEW', 1, 5)
            
        class Glyph:
            CLOSED = VisualStyleElement('TREEVIEW', 2, 1)
            OPENED = VisualStyleElement('TREEVIEW', 2, 2)
            
        class Branch:
            NORMAL = VisualStyleElement('TREEVIEW', 3, 0)

    class ExplorerTreeView:
        class Glyph:
            CLOSED = VisualStyleElement('Explorer::TreeView', 2, 1)
            OPENED = VisualStyleElement('Explorer::TreeView', 2, 2)

    class TextBox:
        class TextEdit:
            NORMAL = VisualStyleElement('EDIT', 1, 1)
            HOT = VisualStyleElement('EDIT', 1, 2)
            SELECTED = VisualStyleElement('EDIT', 1, 3)
            DISABLED = VisualStyleElement('EDIT', 1, 4)
            FOCUSED = VisualStyleElement('EDIT', 1, 5)
            READ_ONLY = VisualStyleElement('EDIT', 1, 6)
            ASSIST = VisualStyleElement('EDIT', 1, 7)
            
        class Caret:
            NORMAL = VisualStyleElement('EDIT', 2, 0)

    class TrayNotify:
        class Background:
            NORMAL = VisualStyleElement('TRAYNOTIFY', 1, 0)
            
        class AnimateBackground:
            NORMAL = VisualStyleElement('TRAYNOTIFY', 2, 0)

    class Window:
        class Caption:
            ACTIVE = VisualStyleElement('WINDOW', 1, 1)
            INACTIVE = VisualStyleElement('WINDOW', 1, 2)
            DISABLED = VisualStyleElement('WINDOW', 1, 3)
            
        class SmallCaption:
            ACTIVE = VisualStyleElement('WINDOW', 2, 1)
            INACTIVE = VisualStyleElement('WINDOW', 2, 2)
            DISABLED = VisualStyleElement('WINDOW', 2, 3)
            
        class MinCaption:
            ACTIVE = VisualStyleElement('WINDOW', 3, 1)
            INACTIVE = VisualStyleElement('WINDOW', 3, 2)
            DISABLED = VisualStyleElement('WINDOW', 3, 3)
            
        class SmallMinCaption:
            ACTIVE = VisualStyleElement('WINDOW', 4, 1)
            INACTIVE = VisualStyleElement('WINDOW', 4, 2)
            DISABLED = VisualStyleElement('WINDOW', 4, 3)
            
        class MaxCaption:
            ACTIVE = VisualStyleElement('WINDOW', 5, 1)
            INACTIVE = VisualStyleElement('WINDOW', 5, 2)
            DISABLED = VisualStyleElement('WINDOW', 5, 3)
            
        class SmallMaxCaption:
            ACTIVE = VisualStyleElement('WINDOW', 6, 1)
            INACTIVE = VisualStyleElement('WINDOW', 6, 2)
            DISABLED = VisualStyleElement('WINDOW', 6, 3)
            
        class FrameLeft:
            ACTIVE = VisualStyleElement('WINDOW', 7, 1)
            INACTIVE = VisualStyleElement('WINDOW', 7, 2)
            
        class FrameRight:
            ACTIVE = VisualStyleElement('WINDOW', 8, 1)
            INACTIVE = VisualStyleElement('WINDOW', 8, 2)
            
        class FrameBottom:
            ACTIVE = VisualStyleElement('WINDOW', 9, 1)
            INACTIVE = VisualStyleElement('WINDOW', 9, 2)
            
        class SmallFrameLeft:
            ACTIVE = VisualStyleElement('WINDOW', 10, 1)
            INACTIVE = VisualStyleElement('WINDOW', 10, 2)
            
        class SmallFrameRight:
            ACTIVE = VisualStyleElement('WINDOW', 11, 1)
            INACTIVE = VisualStyleElement('WINDOW', 11, 2)
            
        class SmallFrameBottom:
            ACTIVE = VisualStyleElement('WINDOW', 12, 1)
            INACTIVE = VisualStyleElement('WINDOW', 12, 2)
            
        class SysButton:
            NORMAL = VisualStyleElement('WINDOW', 13, 1)
            HOT = VisualStyleElement('WINDOW', 13, 2)
            PRESSED = VisualStyleElement('WINDOW', 13, 3)
            DISABLED = VisualStyleElement('WINDOW', 13, 4)
            
        class MdiSysButton:
            NORMAL = VisualStyleElement('WINDOW', 14, 1)
            HOT = VisualStyleElement('WINDOW', 14, 2)
            PRESSED = VisualStyleElement('WINDOW', 14, 3)
            DISABLED = VisualStyleElement('WINDOW', 14, 4)
            
        class MinButton:
            NORMAL = VisualStyleElement('WINDOW', 15, 1)
            HOT = VisualStyleElement('WINDOW', 15, 2)
            PRESSED = VisualStyleElement('WINDOW', 15, 3)
            DISABLED = VisualStyleElement('WINDOW', 15, 4)
            
        class MdiMinButton:
            NORMAL = VisualStyleElement('WINDOW', 16, 1)
            HOT = VisualStyleElement('WINDOW', 16, 2)
            PRESSED = VisualStyleElement('WINDOW', 16, 3)
            DISABLED = VisualStyleElement('WINDOW', 16, 4)
            
        class MaxButton:
            NORMAL = VisualStyleElement('WINDOW', 17, 1)
            HOT = VisualStyleElement('WINDOW', 17, 2)
            PRESSED = VisualStyleElement('WINDOW', 17, 3)
            DISABLED = VisualStyleElement('WINDOW', 17, 4)
            
        class CloseButton:
            NORMAL = VisualStyleElement('WINDOW', 18, 1)
            HOT = VisualStyleElement('WINDOW', 18, 2)
            PRESSED = VisualStyleElement('WINDOW', 18, 3)
            DISABLED = VisualStyleElement('WINDOW', 18, 4)
            
        class SmallCloseButton:
            NORMAL = VisualStyleElement('WINDOW', 19, 1)
            HOT = VisualStyleElement('WINDOW', 19, 2)
            PRESSED = VisualStyleElement('WINDOW', 19, 3)
            DISABLED = VisualStyleElement('WINDOW', 19, 4)
            
        class MdiCloseButton:
            NORMAL = VisualStyleElement('WINDOW', 20, 1)
            HOT = VisualStyleElement('WINDOW', 20, 2)
            PRESSED = VisualStyleElement('WINDOW', 20, 3)
            DISABLED = VisualStyleElement('WINDOW', 20, 4)
            
        class RestoreButton:
            NORMAL = VisualStyleElement('WINDOW', 21, 1)
            HOT = VisualStyleElement('WINDOW', 21, 2)
            PRESSED = VisualStyleElement('WINDOW', 21, 3)
            DISABLED = VisualStyleElement('WINDOW', 21, 4)
            
        class MdiRestoreButton:
            NORMAL = VisualStyleElement('WINDOW', 22, 1)
            HOT = VisualStyleElement('WINDOW', 22, 2)
            PRESSED = VisualStyleElement('WINDOW', 22, 3)
            DISABLED = VisualStyleElement('WINDOW', 22, 4)
            
        class HelpButton:
            NORMAL = VisualStyleElement('WINDOW', 23, 1)
            HOT = VisualStyleElement('WINDOW', 23, 2)
            PRESSED = VisualStyleElement('WINDOW', 23, 3)
            DISABLED = VisualStyleElement('WINDOW', 23, 4)
            
        class MdiHelpButton:
            NORMAL = VisualStyleElement('WINDOW', 24, 1)
            HOT = VisualStyleElement('WINDOW', 24, 2)
            PRESSED = VisualStyleElement('WINDOW', 24, 3)
            DISABLED = VisualStyleElement('WINDOW', 24, 4)
            
        class HorizontalScroll:
            NORMAL = VisualStyleElement('WINDOW', 25, 1)
            HOT = VisualStyleElement('WINDOW', 25, 2)
            PRESSED = VisualStyleElement('WINDOW', 25, 3)
            DISABLED = VisualStyleElement('WINDOW', 25, 4)
            
        class HorizontalThumb:
            NORMAL = VisualStyleElement('WINDOW', 26, 1)
            HOT = VisualStyleElement('WINDOW', 26, 2)
            PRESSED = VisualStyleElement('WINDOW', 26, 3)
            DISABLED = VisualStyleElement('WINDOW', 26, 4)
            
        class VerticalScroll:
            NORMAL = VisualStyleElement('WINDOW', 27, 1)
            HOT = VisualStyleElement('WINDOW', 27, 2)
            PRESSED = VisualStyleElement('WINDOW', 27, 3)
            DISABLED = VisualStyleElement('WINDOW', 27, 4)
            
        class VerticalThumb:
            NORMAL = VisualStyleElement('WINDOW', 28, 1)
            HOT = VisualStyleElement('WINDOW', 28, 2)
            PRESSED = VisualStyleElement('WINDOW', 28, 3)
            DISABLED = VisualStyleElement('WINDOW', 28, 4)
            
        class Dialog:
            NORMAL = VisualStyleElement('WINDOW', 29, 0)
            
        class CaptionSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 30, 0)
            
        class SmallCaptionSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 31, 0)
            
        class FrameLeftSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 32, 0)
            
        class SmallFrameLeftSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 33, 0)
            
        class FrameRightSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 34, 0)
            
        class SmallFrameRightSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 35, 0)
            
        class FrameBottomSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 36, 0)
            
        class SmallFrameBottomSizingTemplate:
            NORMAL = VisualStyleElement('WINDOW', 37, 0)