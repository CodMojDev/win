# Win32 errors stringification and WinException
from win.defbase_errordef import *

# WinAPI header files
from win.errhandlingapi import *
from win.libloaderapi import *
from win.commctrl import *

# WinAbs core imports
from .core.handle import * # Handles, colors and utils core logic
from .core.event import * # Event class
from .core.absutils import * # Abs.* access
from .core.theme import * # Theme API

# COM HRESULTs
from win.com.comdefbase import HRESULT, COMError, FAILED

# COM Property stores
from win.com.propdef import (PROPVARIANT, PROPERTYKEY, 
                             IPropertyStore, LPPROPERTYSTORE,
                             LPPROPVARIANT, ole32)

# random module for class name generation
import random

# imports from typing module
from typing import Iterator

# import from DefbCI
from win import _defbase_ctypinit as _defb_ci

# # # # # # # # # # # # # # # # # # # #
# Win Abstractions Layer code Begins

# WinAbs initialization procedure
def init_common_controls(icc: int = ICC_WIN95_CLASSES):
    # initialize the INITCOMMONCONTROLSEX structure
    icex = INITCOMMONCONTROLSEX()
    icex.dwSize = sizeof(icex)
    icex.dwICC = icc

    # initialize the common controls (comctl32)
    if not InitCommonControlsEx(icex.ref()):
        raise WinException()

class Scrollbar:
    """
    The window scrollbar, vertical, horizontal or custom.
    """
    
    class Button:
        # parent scrollbar
        scrollbar: 'Scrollbar'
        
        # self button disable switch
        switch: int
        # self button state index
        state_index: int
        
        # antagonist button disable switch
        antagonist_switch: int
        # antagonist button state index
        antagonist_state_index: int
        
        def __init__(self, scrollbar: 'Scrollbar', switch: int, state_index: int, antagonist_switch: int, antagonist_state_index: int):
            self.scrollbar = scrollbar
            
            self.state_index = state_index
            self.switch = switch
            
            self.antagonist_switch = antagonist_switch
            self.antagonist_state_index = antagonist_state_index
        
        def enable(self):
            """
            Enable the scrollbar button.
            """
            sbi = self.scrollbar.info()
            antagonist_enabled = (sbi.rgstate[self.antagonist_state_index] & 1) == 0
            EnableScrollBar(self.scrollbar.window, self.scrollbar.type, ESB_ENABLE_BOTH)
            if not antagonist_enabled:
                EnableScrollBar(self.scrollbar.window, self.scrollbar.type, self.antagonist_switch)
        
        def disable(self):
            """
            Disable the scrollbar button.
            """
            EnableScrollBar(self.scrollbar.window, self.scrollbar.type, self.switch)
        
        @property
        def enabled(self) -> bool:
            return self.scrollbar.info().rgstate[self.state_index] & 1
        
    # scrollbar HWND and type (SB_VERT, SB_HORZ, SB_CTL)
    window: int | HWND
    type: int
    
    # scrollbar buttons
    left: Button
    right: Button
    up: Button
    down: Button
    
    def __init__(self, window: int | HWND, type: int):
        self.window = window
        self.type = type
        
        self.left = self.Button(self, ESB_DISABLE_LEFT, 5, ESB_DISABLE_RIGHT, 1)
        self.down = self.Button(self, ESB_DISABLE_DOWN, 5, ESB_DISABLE_UP, 1)
        self.right = self.Button(self, ESB_DISABLE_RIGHT, 1, ESB_DISABLE_LEFT, 5)
        self.up = self.Button(self, ESB_DISABLE_UP, 1, ESB_DISABLE_DOWN, 5)
        
    def info(self) -> SCROLLBARINFO:
        """
        Get the scrollbar information.
        """
        sbi = SCROLLBARINFO()
        sbi.cbSize = sbi.size()
        if self.type == SB_VERT:
            l = GetScrollBarInfo(self.window, OBJID_VSCROLL, sbi.ref())
        elif self.type == SB_HORZ:
            l = GetScrollBarInfo(self.window, OBJID_HSCROLL, sbi.ref())
        elif self.type == SB_CTL:
            l = SendMessageW(self.window, SBM_GETSCROLLBARINFO, 0, sbi.addressof())
        if not l:
            raise WinException()
        return sbi
    
    @property
    def range(self) -> tuple[int, int]:
        iMin, iMax = UINT(), UINT()
        if not GetScrollRange(self.window, self.type, byref(iMin), byref(iMax)):
            raise WinException()
        return iMin.value, iMax.value
    
    @range.setter
    def range(self, range: tuple[int, int]):
        if not SetScrollRange(self.window, self.type, range[0], range[1], TRUE):
            raise WinException()
        
    @property
    def position(self) -> int:
        SetLastError(0)
        i = GetScrollPos(self.window, self.type)
        code = GetLastError()
        if i == 0 and code != 0:
            raise WinException(code)
        return i
    
    @position.setter
    def position(self, position: int):
        SetLastError(0)
        if not SetScrollPos(self.window, self.type, position, TRUE):
            code = GetLastError()
            if code != 0: raise WinException(code)
    
    def get_scroll_info(self, mask: int) -> SCROLLINFO:
        """
        Get the scroll info of scrollbar.
        """
        si = SCROLLINFO()
        si.cbSize = si.size()
        si.fMask = mask
        if not GetScrollInfo(self.window, self.type, si.ref()):
            raise WinException()
        return si
    
    def set_scroll_info(self, mask: int, si: SCROLLINFO):
        """
        Set the scroll info of scrollbar.
        """
        si.cbSize = si.size()
        si.fMask = mask
        SetLastError(0)
        SetScrollInfo(self.window, self.type, si.ref(), TRUE)
        code = GetLastError()
        if code != 0:
            raise WinException(code)
    
    @property
    def track_position(self) -> int:
        return self.get_scroll_info(SIF_TRACKPOS).nTrackPos
    
    @track_position.setter
    def track_position(self, track_position: int):
        si = SCROLLINFO()
        si.nTrackPos = track_position
        self.set_scroll_info(SIF_TRACKPOS, si)
        
    @property
    def page(self) -> int:
        return self.get_scroll_info(SIF_PAGE).nPage
    
    @page.setter
    def page(self, page: int):
        si = SCROLLINFO()
        si.nPage = page
        self.set_scroll_info(SIF_PAGE, si)
        
    @property
    def minimal(self) -> int:
        return self.range[0]
    
    @minimal.setter
    def minimal(self, minimal: int):
        self.range = (minimal, self.maximal)
        
    @property
    def maximal(self) -> int:
        return self.range[1]
    
    @maximal.setter
    def maximal(self, maximal: int):
        self.range = (self.minimal, maximal)
        
    def enable_all(self):
        """
        Enable all the buttons.
        """
        EnableScrollBar(self.window, self.type, ESB_ENABLE_BOTH)

# menu APIs
class Menu(Handle):
    """
    Main window menu.
    """
    
    def close(self):
        DestroyMenu(self)
        self._closed = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._buffer = create_unicode_buffer(256)
    
    @classmethod
    def create(cls):
        menu = cls(CreateMenu())
        if not menu.value:
            raise WinException()
        return menu
    
    def append(self, item: int, lp, flags: int):
        """
        Append the item to menu.
        """
        if isinstance(lp, str):
            lp = create_unicode_buffer(lp)
        if not AppendMenuW(self, flags, PtrUtil.get_address(item), i_cast(lp, LPCWSTR)):
            raise WinException()

    def modify(self, position: int, item: int, lp, flags: int):
        """
        Modify the menu.
        """
        if isinstance(lp, str):
            lp = create_unicode_buffer(lp)
        if not ModifyMenuW(self, position, flags, PtrUtil.get_address(item), i_cast(lp, LPWSTR)):
            raise WinException()

    def get_state(self, identifier: int, flags: int = MF_BYCOMMAND) -> int:
        """
        Get state of the menu item.
        """
        state = GetMenuState(self, identifier, flags)
        if state == -1: raise WinException()
        return state
    
    def check(self, identifier: int, check: bool = False, flags: int = MF_BYCOMMAND) -> int:
        """
        Check or uncheck the menu item.
        """
        if check: extra = MF_CHECKED
        else: extra = MF_UNCHECKED
        result = CheckMenuItem(self, identifier, flags | extra)
        if result == MAXDWORD:
            raise WinException()
        return result
    
    def information(self, mask: int | None = None) -> MENUINFO:
        """
        Get the menu information.
        """
        mi = MENUINFO()
        mi.cbSize = mi.size()
        if mask is None:
            mask = (MIM_APPLYTOSUBMENUS | MIM_BACKGROUND | MIM_HELPID |
                    MIM_MAXHEIGHT | MIM_MENUDATA | MIM_MAXHEIGHT)
        mi.fMask = mask
        if not GetMenuInfo(self, mi.ref()):
            raise WinException()
        return mi

    def set_information(self, information: MENUINFO, mask: int | None = None):
        """
        Set the menu information.
        """
        information.cbSize = information.size()
        if mask is None:
            mask = (MIM_APPLYTOSUBMENUS | MIM_BACKGROUND | MIM_HELPID |
                    MIM_MAXHEIGHT | MIM_MENUDATA | MIM_MAXHEIGHT)
        information.fMask = mask
        if not SetMenuInfo(self, information.ref()):
            raise WinException()
    
    def item_info(self, index: int, mask: int | None = None, positioned: bool = True) -> MENUITEMINFOW:
        """
        Get the item menu information
        """
        mii = MENUITEMINFOW()
        mii.cbSize = mii.size()
        if mask is None:
            mask = (MIIM_BITMAP | MIIM_CHECKMARKS | MIIM_ID | MIIM_STATE |
                    MIIM_FTYPE | MIIM_STRING | MIIM_DATA | MIIM_STRING |
                    MIIM_TYPE | MIIM_SUBMENU)
        if mask & MIIM_STRING:
            mii.dwTypeData = i_cast(self._buffer, LPWSTR)
            mii.cch = 256
        mii.fMask = mask
        if not GetMenuItemInfoW(self, index, positioned, mii.ref()):
            raise WinException()
        return mii

class PopupMenu(Menu):
    """
    Popup menu class.
    """
    
    @classmethod
    def create(cls):
        menu = cls(CreatePopupMenu())
        if not menu.value:
            raise WinException()
        return menu
        
    def track(self, x: int, y: int, hWnd: int | HANDLE, flags: int=0, parameters: TPMPARAMS | None = None):
        """
        Track the popup menu in given coordinates of window.
        """
        if parameters is not None:
            parameters = parameters.ref()
        if not TrackPopupMenuEx(self, flags, x, y, hWnd, parameters):
            raise WinException()
        
    def information(self, mask: int | None = None) -> MENUITEMINFOW:
        """
        Get the popup menu information.
        """
        return self.item_info(self.value, mask, False)

class ContextMenu(PopupMenu):
    """
    Context menu extension for popup menu.
    """
    
    def track(self, x: int, y: int, hWnd: int | HANDLE, flags: int=0, parameters: TPMPARAMS | None = None, screen: bool = False):
        """
        Track the context menu in given coordinates of window.
        """
        if not screen:
            pt = Point(x, y)
            if not ClientToScreen(hWnd, pt.ref()):
                raise WinException()
            x, y = pt
        super().track(x, y, hWnd, flags, parameters)

# DWM & Compositor infrastructure
dwmapi = get_win_library('dwmapi.dll')

WM_DWMEXILEFRAME = 0x0322
WM_MAGNIFICATION_STARTED = 0x0324

WINDOWCOMPOSITIONATTRIB = INT

class WINDOWCOMPOSITIONATTRIBDATA(CStructure):
    _fields_ = [
        ('Attrib', WINDOWCOMPOSITIONATTRIB),
        ('pvData', PVOID),
        ('cbData', UINT)
    ]
    Attrib: int
    pvData: int
    cbData: int

LPWINDOWCOMPOSITIONATTRIBDATA = PTR(WINDOWCOMPOSITIONATTRIBDATA)

# the compositor attributes methods Infrastructure
@user32.foreign(BOOL, HWND, LPWINDOWCOMPOSITIONATTRIBDATA)
def SetWindowCompositionAttribute(hwnd: int, pwcad: IPointer[WINDOWCOMPOSITIONATTRIBDATA]) -> int: pass

@dwmapi.foreign(HRESULT, HWND, DWORD, LPCVOID, DWORD)
def DwmSetWindowAttribute(hwnd: int, dwAttribute: int, pvAtribute: int, cbAttribute: int): pass

# the DWM infrastructure
@dwmapi.foreign(BOOL, HWND, UINT, WPARAM, LPARAM, PTR(LRESULT))
def DwmDefWindowProc(hWnd: int, msg: int, wParam: int, lParam: int, plResult: IPointer[LRESULT]) -> int: ...

@dwmapi.foreign(HRESULT, HWND, PTR(MARGINS))
def DwmExtendFrameIntoClientArea(hWnd: int, pMarInset: IPointer[MARGINS]) -> int: ...

# DWM window attributes
DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_USE_HOSTBACKDROPBRUSH = 17
DWMWA_SYSTEMBACKDROP_TYPE = 38

# System Backdrop Type
DWMSBT_AUTO = 0
DWMSBT_NONE = 1
DWMSBT_MAINWINDOW = 2
DWMSBT_TRANSIENTWINDOW = 3
DWMSBT_TABBEDWINDOW = 4

# document "undocumented" composition attribs.
WCA_TRANSITIONS_FORCEDISABLED = 3
WCA_ALLOW_NCPAINT = 4
WCA_CAPTION_BUTTON_BOUNDS = 5
WCA_NONCLIENT_RTL_LAYOUT = 6
WCA_EXTENDED_FRAME_BOUNDS = 8
WCA_DISALLOW_PEEK = 16
WCA_CLOAK = 17
WCA_CLOAKED = 18
WCA_ACCENT_POLICY = 19
WCA_EXCLUDED_FROM_DDA = 24
WCA_USEDARKMODECOLORS = 26

# accent state enumeration
ACCENT_DISABLED = 0
ACCENT_ENABLE_GRADIENT = 1
ACCENT_ENABLE_TRANSPARENTGRADIENT = 2
ACCENT_ENABLE_BLURBEHIND = 3
ACCENT_ENABLE_SLOWMOVE = 4
ACCENT_STATE = INT

# ToUnicodeEx infrastructure
_to_unicode_keyboard_state = (BYTE * 256)()

def to_unicode(vk: int, scan_code: int) -> tuple[str, int]:
    """
    Convert virtual key code and scan code to characters and integer `ToUnicodeEx` result.
    """
    if not GetKeyboardState(_to_unicode_keyboard_state):
        raise WinException()
    buffer = (WCHAR * 10)()
    result = ToUnicodeEx(vk, scan_code, _to_unicode_keyboard_state, buffer, 10, 0, GetKeyboardLayout(0))
    return buffer.value, result

# DPI process awareness
@user32.foreign(BOOL)
def SetProcessDPIAware() -> int: ...

# document "undocumented" window band infrastructure
@user32.foreign(BOOL, HWND, PDWORD)
def GetWindowBand(hwnd: int, pdwBand: IPointer[DWORD]) -> int: ...

ZBID_DEFAULT = 0
ZBID_DESKTOP = 1
ZBID_UIACCESS = 2
ZBID_IMMERSIVE_IHM = 3
ZBID_IMMERSIVE_NOTIFICATION = 4
ZBID_IMMERSIVE_APPCHROME = 5
ZBID_IMMERSIVE_MOGO = 6
ZBID_IMMERSIVE_EDGY = 7
ZBID_IMMERSIVE_INACTIVEMOBODY = 8
ZBID_IMMERSIVE_INACTIVEDOCK = 9
ZBID_IMMERSIVE_ACTIVEMOBODY = 10
ZBID_IMMERSIVE_ACTIVEDOCK = 11
ZBID_IMMERSIVE_BACKGROUND = 12
ZBID_IMMERSIVE_SEARCH = 13
ZBID_GENUINE_WINDOWS = 14
ZBID_IMMERSIVE_RESTRICTED = 15
ZBID_SYSTEM_TOOLS = 16
ZBID_LOCK = 17
ZBID_ABOVELOCK_UX = 18

# document "undocumented" UAH (User Aero Hooks) infrastructure
WM_UAHDESTROYWINDOW = 0x0090
WM_UAHDRAWMENU = 0x0091
WM_UAHDRAWMENUITEM = 0x0092
WM_UAHINITMENU = 0x0093
WM_UAHMEASUREMENUITEM = 0x0094
WM_UAHNCPAINTMENUPOPUP = 0x0095

class UAHMENU(CStructure):
    _fields_ = [
        ('hmenu', HMENU),
        ('hdc', HDC),
        ('dwFlags', DWORD)
    ]
    hmenu: int
    hdc: int
    dwFlags: int
    
LPUAHMENU = PTR(UAHMENU)
    
class UAHMENUITEMMETRICS(CStructure):
    _fields_ = [
        ('rgsizeBar', SIZE * 2),
        ('rgsizePopup', SIZE * 4)
    ]
    rgsizeBar: IArray[SIZE]
    rgsizePopup: IArray[SIZE]
    
class UAHMENUPOPUPMETRICS(CStructure):
    _fields_ = [
        ('rgcx', DWORD * 4),
        ('fUpdateMaxWidths', DWORD, 2)
    ]
    rgcx: IArray[int]
    fUpdateMaxWidths: int
    
class UAHMENUITEM(CStructure):
    _fields_ = [
        ('iPosition', INT),
        ('umim', UAHMENUITEMMETRICS),
        ('umpm', UAHMENUPOPUPMETRICS)
    ]
    iPosition: int
    umim: UAHMENUITEMMETRICS
    umpm: UAHMENUPOPUPMETRICS

class UAHDRAWMENUITEM(CStructure):
    _fields_ = [
        ('dis', DRAWITEMSTRUCT),
        ('um', UAHMENU),
        ('umi', UAHMENUITEM)
    ]
    dis: DRAWITEMSTRUCT
    um: UAHMENU
    umi: UAHMENUITEM

LPUAHDRAWMENUITEM = PTR(UAHDRAWMENUITEM)

class UAHMEASUREMENUITEM(CStructure):
    _fields_ = [
        ('mis', MEASUREITEMSTRUCT),
        ('um', UAHMENU),
        ('umi', UAHMENUITEM)
    ]
    mis: MEASUREITEMSTRUCT
    um: UAHMENU
    umi: UAHMENUITEM
    
LPUAHMEASUREMENUITEM = PTR(UAHMEASUREMENUITEM)

# Prop API
@ole32.foreign(HRESULT, LPPROPVARIANT)
def PropVariantClear(pv: IPointer[PROPVARIANT]) -> int: ...

# Shell API
shell32 = get_win_library('shell32.dll')

@shell32.foreign(HRESULT, HWND, REFIID, LPPROPERTYSTORE, intermediate_method=True)
def SHGetPropertyStoreForWindow(hWnd: int, riid: IID, ppStore: IDoublePtr[IPropertyStore], **kwargs) -> int:
    return delegate(hWnd, riid.ref(), ppStore)

PKEY_AppUserModel_ID = PROPERTYKEY(GUID.string('{9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3}'), 5)

# UxTheme API
@uxtheme.foreign(HTHEME, HWND)
def GetWindowTheme(hWnd: int) -> int: ...

@uxtheme.foreign(HRESULT, HWND, LPCWSTR, LPCWSTR)
def SetWindowTheme(hWnd: int, pszSubAppName: WT_LPWSTR, pszSubIdList: WT_LPWSTR) -> int: ...

@uxtheme.foreign(BOOL, HWND)
def IsThemeDialogTextureEnabled(hWnd: int) -> int: ...

# Kernel32 ATOM API

@kernel32.foreign(UINT, ATOM, LPWSTR, INT)
def GlobalGetAtomNameW(nAtom: int | ATOM, lpBuffer: WT_LPWSTR, nSize: int) -> int: ...

@kernel32.foreign(UINT, ATOM, LPWSTR, INT)
def GetAtomNameW(nAtom: int | ATOM, lpBuffer: WT_LPWSTR, nSize: int) -> int: ...

@kernel32.foreign(ATOM, LPCWSTR)
def GlobalFindAtomW(lpString: WT_LPWSTR) -> int: ...

@kernel32.foreign(ATOM, LPCWSTR)
def FindAtomW(lpString: WT_LPWSTR) -> int: ...

@kernel32.foreign(ATOM, ATOM)
def GlobalDeleteAtom(nAtom: int | ATOM) -> int: ...

@kernel32.foreign(ATOM, ATOM)
def DeleteAtom(nAtom: int | ATOM) -> int: ...

@kernel32.foreign(ATOM, LPCWSTR)
def AddAtomW(lpString: WT_LPWSTR) -> int: ...

@kernel32.foreign(ATOM, LPCWSTR)
def GlobalAddAtomW(lpString: WT_LPWSTR) -> int: ...

class Atom(ControllableValue, ATOM):
    """
    Class representing ATOM value.
    """
    
    local: bool
    
    @property
    def name(self) -> str:
        buffer = create_unicode_buffer(256)
        if self.local:
            GetAtomNameW(self, buffer, 256)
        else:
            GlobalGetAtomNameW(self, buffer, 256)
        return buffer.value
    
    def initialize_from_foreign(self, local: bool = False):
        self.local = local
    
    @classmethod
    def create(cls, name: str, local: bool = False):
        if local:
            atom = cls(AddAtomW(name))
        else:
            atom = cls(GlobalAddAtomW(name))
        atom.local = local
        if not atom.value:
            raise WinException()
        return atom
    
    @classmethod
    def find(cls, name: str, local: bool = False):
        """
        Find the ATOM by name.
        """
        if local:
            atom = cls(FindAtomW(name))
        else:
            atom = cls(GlobalFindAtomW(name))
        if not atom.value:
            raise WinException()
        return atom 
    
    def close(self):
        SetLastError(0)
        if self.local:
            DeleteAtom(self)
        else:
            GlobalDeleteAtom(self)
        code = GetLastError()
        if code != 0:
            raise WinException(code)
        self._closed = True

SUBCLASSPROC = CALLBACK(LRESULT, HWND, UINT, WPARAM, LPARAM, UINT_PTR, DWORD_PTR)

@comctl32.foreign(BOOL, HWND, SUBCLASSPROC, UINT_PTR, DWORD_PTR)
def SetWindowSubclass(hWnd: int, pfnSubclass: FARPROC, uIdSubclass: int, dwRefData: int) -> int: ...

@comctl32.foreign(BOOL, HWND, SUBCLASSPROC, UINT_PTR)
def RemoveWindowSubclass(hWnd: int, pfnSubclass: FARPROC, uIdSubclass: int) -> int: ...

@comctl32.foreign(LRESULT, HWND, UINT, WPARAM, LPARAM)
def DefSubclassProc(hWnd: int, uMsg: int, wParam: int, lParam: int) -> int: ...

class ACCENTPOLICY(CStructure):
    _fields_ = [
        ('AccentState', ACCENT_STATE),
        ('AccentFlags', UINT),
        ('GradientColor', COLORREF),
        ('AnimationId', UINT)
    ]
    AccentState: int
    AccentFlags: int
    GradientColor: int
    AnimationId: int

GCLP_MENUNAME = (-8)
GCLP_HBRBACKGROUND = (-10)
GCLP_HCURSOR = (-12)
GCLP_HICON = (-14)
GCLP_HMODULE = (-16)
GCLP_CBWNDEXTRA = (-18)
GCLP_CBCLSEXTRA = (-20)
GCLP_WNDPROC = (-24)
GCLP_STYLE = (-26)
GCW_ATOM = (-32)
GCLP_HICONSM = (-34)

@user32.foreign(BOOL, HWND, LONG, LONG, PMENUBARINFO)
def GetMenuBarInfo(hwnd: int, idObject: int, idItem: int, pmbi: IPointer[MENUBARINFO]) -> int: ...

# Window send message type enumeration
WSMT_SEND = 0
WSMT_POST = 1
WSMT_DEFAULT = 2
WSMT_NOTIFY = 3
WSMT_WPARAMFORMAT = 4
WSMT_LPARAMFORMAT = 5
WSMT_DEFAULTSUBCLASS = 6

class Window(Abs.Object, HWND):
    """
    Class, wrapping functionality of Win32 Window.
    """
    try:
        WINABS_ICON = Icon.from_icon(os.path.normpath(os.path.join(os.path.dirname(__file__), 'data/win-abs.ico')))
    except Exception as e:
        WINABS_ICON = Icon.load(IDI_APPLICATION)
    
    class Styles:
        window: 'Window'
        
        def __init__(self, window: 'Window'):
            self.window = window
            
        def add(self, *styles: int):
            """
            Add specific style (or styles).
            """
            for style in styles:
                self.window.style |= style
            
        def remove(self, *styles: int):
            """
            Remove specific style (or styles).
            """
            for style in styles:
                self.window.style &= ~style
            
        def add_ex(self, *styles: int):
            """
            Add specific extended style (or styles).
            """
            for style in styles:
                self.window.extended_style |= style
            
        def remove_ex(self, *styles: int):
            """
            Remove specific extended style (or styles).
            """
            for style in styles:
                self.window.extended_style &= ~style
                
        def has(self, *styles: int) -> bool:
            """
            Check specific style (or styles) setted up.
            """
            style = 0
            for i in styles:
                style |= i
            return (self.window.style & style) != 0
                
        def has_ex(self, *styles: int) -> bool:
            """
            Check specific extended style (or styles) setted up.
            """
            style = 0
            for i in styles:
                style |= i
            return (self.window.extended_style & style) != 0
        
    class Props:
        window: 'Window'
        
        def __init__(self, window: 'Window'):
            self.window = window
            
        def __getitem__(self, prop: str | int | Atom) -> int:
            return self.window.get_prop(prop)
        
        def __setitem__(self, prop: str | int | Atom, value: WT_ADDRLIKE):
            self.window.set_prop(prop, value)
            
        def pop(self, prop: str | int | Atom) -> int:
            """
            Pop the property from property set of the window
            """
            return self.window.remove_prop(prop)
        
        def remove(self, prop: str | int | Atom):
            """
            Remove the property from property set of the window.
            """
            self.window.remove_prop(prop)
            
        def __iter__(self) -> Iterator[Atom | str]:
            props = []
            def enum(k: Atom | str, *_) -> bool:
                props.append(k)
                return True
            self.window.enum_props(enum)
            return iter(props)
        
        def keys(self) -> Iterator[Atom | str]:
            """
            Get keys of property set of the window.
            """
            return iter(self)
        
        def values(self) -> Iterator[int]:
            """
            Get values of property set of the window.
            """
            values = []
            def enum(_, v: int, l: int) -> bool:
                values.append(v)
                return True
            self.window.enum_props(enum)
            return iter(values)
        
        def items(self) -> Iterator[tuple[Atom | str, int]]:
            """
            Get items of property set of the window.
            """
            items = []
            def enum(k: Atom | str, v: int, _) -> bool:
                items.append((k, v))
                return True
            self.window.enum_props(enum)
            return iter(items)
        
        def update(self, value: Iterable[tuple[str | int | Atom, WT_ADDRLIKE]] | dict[str | int | Atom, WT_ADDRLIKE]):
            """
            Update the window property set with dictionary-like property update structure.
            """
            value = dict(value)
            for k, v in value.items():
                self.window.set_prop(k, v)
                
        def get(self, prop: str | int | Atom, default: WT = None) -> WT | int:
            """
            Get the window property value with default argument fallback.
            """
            try:
                return self.window.get_prop(prop)
            except WinException:
                return default
            
        def __contains__(self, prop: str | int | Atom) -> bool:
            try:
                self.window.get_prop(prop)
            except WinException:
                return False
            return True
        
        def __delitem__(self, prop: str | int | Atom):
            self.window.remove_prop(prop)
            
    class Children:
        window: 'Window'
        children: list['Window']
        
        def __init__(self, window: 'Window', children: list['Window']):
            self.window = window
            self.children = children
            
        def __iter__(self) -> Iterator['Window']:
            return iter(self.children)
        
        def append(self, window: 'Window'):
            """
            Add the new window to window children.
            """
            window.parent = self.window
            self.children.append(window)
        
        def add(self, window: 'Window'):
            """
            Add the new window to window children.
            """
            window.parent = self.window
            self.children.append(window)
            
        def __getitem__(self, index: int) -> 'Window':
            return self.children[index]
        
        def __contains__(self, window: 'Window') -> bool:
            return window in self.children
    
    _foreign_cache: dict[int, 'Window'] = {}
    styles: Styles
    props: Props
    vscroll: Scrollbar
    hscroll: Scrollbar
    on_create: MultiEvent
    
    on_left_button_down: MultiEvent
    on_left_button_up: MultiEvent
    on_left_button_double_click: MultiEvent
    on_right_button_down: MultiEvent
    on_right_button_up: MultiEvent
    on_right_button_double_click: MultiEvent
    on_x_button_down: MultiEvent
    on_x_button_up: MultiEvent
    on_x_button_double_click: MultiEvent
    on_middle_button_down: MultiEvent
    on_middle_button_up: MultiEvent
    on_middle_button_double_click: MultiEvent
    
    on_close: MultiEvent
    on_destroy: MultiEvent
    on_key_down: MultiEvent
    on_key_up: MultiEvent
    on_move: MultiEvent
    on_show: MultiEvent
    on_theme_changed: MultiEvent
    on_user_changed: MultiEvent
    on_unknown_message: MultiEvent
    on_enable: MultiEvent
    on_set_font: MultiEvent
    on_mouse_wheel: MultiEvent
    on_timer: MultiEvent
    on_notify: MultiEvent
    on_mouse_move: MultiEvent
    on_draw_item: MultiEvent
    on_palette_changed: MultiEvent
    on_measure_item: MultiEvent
    on_compare_item: MultiEvent
    on_char: MultiEvent
    on_command: MultiEvent
    on_hscroll: MultiEvent
    on_vscroll: MultiEvent
    on_nc_destroy: MultiEvent
    on_mouse_leave: MultiEvent
    on_power_broadcast: MultiEvent
    on_sizing: MultiEvent
    on_enter_menu_loop: MultiEvent
    on_exit_menu_loop: MultiEvent
    on_enter_idle: MultiEvent
    on_sys_command: MultiEvent
    on_activate: MultiEvent
    on_activate_app: MultiEvent
    on_child_activate: MultiEvent
    on_compacting: MultiEvent
    on_style_changed: MultiEvent
    on_style_changing: MultiEvent
    on_extended_style_changed: MultiEvent
    on_extended_style_changing: MultiEvent
    on_window_position_changed: MultiEvent
    on_window_position_changing: MultiEvent
    on_capture_changed: MultiEvent
    on_focus_changed: MultiEvent
    on_focus_lost: MultiEvent
    on_dwm_colorization_color: MultiEvent
    on_dwm_composition_changed: MultiEvent
    on_dwm_nc_rendering_changed: MultiEvent
    on_dwm_send_iconic_live_preview_bitmap: MultiEvent
    on_dwm_send_iconic_thumbnail: MultiEvent
    on_dwm_window_maximized_change: MultiEvent
    on_dwm_exile_frame: MultiEvent
    on_magnification_started: MultiEvent
    on_sys_color_change: MultiEvent
    on_time_changed: MultiEvent
    
    class_style: int
    last_message: MSG
    pending_messages: list[tuple[int, int, int, int]]
    
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, window: int | HANDLE):
        if isinstance(window, int):
            return window == self.value
        return window.value == self.value
    
    @classmethod
    def foreign(cls, hwnd: int) -> 'Window':
        """
        Create `Window` object from foreign HWND.
        """
        hwnd = PtrUtil.get_address(hwnd)
        if hwnd == 0: return None
        window = Window._foreign_cache.get(hwnd)
        if window is None:
            window = cls.__new__(cls)
            window.value = hwnd
            Window.__init__(window, headless=True)
            Window._foreign_cache[hwnd] = window
        return window
    
    def headless_init(self):
        pass
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._abs_managed = 'headless' not in kwargs
        self.styles = self.Styles(self)
        self.props = self.Props(self)
        self.vscroll = Scrollbar(self, SB_VERT)
        self.hscroll = Scrollbar(self, SB_HORZ)
        
        # subclass procedure
        self.pfnSubclassThunkProc = SUBCLASSPROC(self.window_subclass_thunk_proc)
        
        # events collection
        self.on_create = MultiEvent()
        self.on_left_button_down = MultiEvent()
        self.on_left_button_up = MultiEvent()
        self.on_left_button_double_click = MultiEvent()
        self.on_right_button_down = MultiEvent()
        self.on_right_button_up = MultiEvent()
        self.on_right_button_double_click = MultiEvent()
        self.on_x_button_down = MultiEvent()
        self.on_x_button_up = MultiEvent()
        self.on_x_button_double_click = MultiEvent()
        self.on_middle_button_down = MultiEvent()
        self.on_middle_button_up = MultiEvent()
        self.on_middle_button_double_click = MultiEvent()
        self.on_close = MultiEvent()
        self.on_destroy = MultiEvent()
        self.on_key_down = MultiEvent()
        self.on_key_up = MultiEvent()
        self.on_move = MultiEvent()
        self.on_show = MultiEvent()
        self.on_style_changed = MultiEvent()
        self.on_theme_changed = MultiEvent()
        self.on_user_changed = MultiEvent()
        self.on_unknown_message = MultiEvent()
        self.on_enable = MultiEvent()
        self.on_set_font = MultiEvent()
        self.on_mouse_wheel = MultiEvent()
        self.on_timer = MultiEvent()
        self.on_notify = MultiEvent()
        self.on_mouse_move = MultiEvent()
        self.on_draw_item = MultiEvent()
        self.on_palette_changed = MultiEvent()
        self.on_measure_item = MultiEvent()
        self.on_compare_item = MultiEvent()
        self.on_char = MultiEvent()
        self.on_command = MultiEvent()
        self.on_hscroll = MultiEvent()
        self.on_vscroll = MultiEvent()
        self.on_nc_destroy = MultiEvent()
        self.on_mouse_leave = MultiEvent()
        self.on_power_broadcast = MultiEvent()
        self.on_sizing = MultiEvent()
        self.on_enter_menu_loop = MultiEvent()
        self.on_exit_menu_loop = MultiEvent()
        self.on_enter_idle = MultiEvent()
        self.on_activate = MultiEvent()
        self.on_activate_app = MultiEvent()
        self.on_style_changed = MultiEvent()
        self.on_style_changing = MultiEvent()
        self.on_extended_style_changed = MultiEvent()
        self.on_extended_style_changing = MultiEvent()
        self.on_window_position_changed = MultiEvent()
        self.on_window_position_changing = MultiEvent()
        self.on_child_activate = MultiEvent()
        self.on_capture_changed = MultiEvent()
        self.on_focus_changed = MultiEvent()
        self.on_focus_lost = MultiEvent()
        self.on_dwm_colorization_color = MultiEvent()
        self.on_dwm_composition_changed = MultiEvent()
        self.on_dwm_nc_rendering_changed = MultiEvent()
        self.on_dwm_send_iconic_live_preview_bitmap = MultiEvent()
        self.on_dwm_send_iconic_thumbnail = MultiEvent()
        self.on_dwm_window_maximized_change = MultiEvent()
        self.on_dwm_exile_frame = MultiEvent()
        self.on_magnification_started = MultiEvent()
        self.on_sys_color_change = MultiEvent()
        self.on_time_changed = MultiEvent()
        
        self.headless_init()
        
        # bind the standard handler for destroy: application cycle notifier
        self.on_nc_destroy += EventCallback(self.Window_on_nc_destroy, Priority._PrivateMinPriority)
        
        # bind the standard handler for creation: application cycle notifier
        self.on_create += EventCallback(self.Window_on_create, Priority._PrivateMaxPriority)
        
        # headless construct = construct `Window` object from HWND
        if 'headless' not in kwargs:
            # fields for class registering
            self._class_name = None
            self.class_style = 0
            self._background_brush = (COLOR_WINDOW + 1)
            self._cursor = None
            self._icon = None
            self._small_icon = None
            self.last_message = MSG()
            self.pending_messages = []
            
            # styles for window creation
            self._style = WS_OVERLAPPEDWINDOW
            self._extended_style = 0
            
            # timer callback cache
            self._timers = {}
    
    _timers: dict[int, FARPROC]
    class_name: str | None
    
    def on_fully_created(self):
        pass
    
    def Window_on_nc_destroy(self):
        # notify the application cycle what one of application-hosted windows is destroyed
        app = WindowLoopUnit.current(running=False)
        app.windows -= 1
        app.notify()
        
    def Window_on_create(self):
        app = WindowLoopUnit.current(running=False)
        app.windows += 1 # add the application cycle windows count
        return True
    
    @property
    def class_name(self) -> str | None:
        if not self:
            return self._class_name
        class_name = create_unicode_buffer(256)
        if not GetClassNameW(self, class_name, 256):
            raise WinException()
        return class_name.value
    
    @class_name.setter
    def class_name(self, class_name: str | None):
        self._class_name = class_name
    
    @property
    def style(self) -> int:
        if not self.value:
            return self._style
        return GetWindowLongW(self, GWL_STYLE)
    
    @style.setter
    def style(self, style: int):
        self._style = style
        if self.value:
            SetWindowLongW(self, GWL_STYLE, style)
        
    @property
    def extended_style(self) -> int:
        if not self.value:
            return self._extended_style
        return GetWindowLongW(self, GWL_EXSTYLE)
    
    @extended_style.setter
    def extended_style(self, extended_style: int):
        self._extended_style = extended_style
        if self.value:
            SetWindowLongW(self, GWL_EXSTYLE, extended_style)
    
    @property
    def icon(self) -> Cursor | None:
        if self.value:
            return Icon.foreign_owner(GetClassLongPtrW(self, GCLP_HICON))
        return self._icon
    
    @icon.setter
    def icon(self, icon: int | HANDLE):
        if self.value:
            SetClassLongPtrW(self, GCLP_HICON, PtrUtil.get_address(icon))
        self._icon = icon
    
    @property
    def cursor(self) -> Cursor | None:
        if self.value:
            return Cursor.foreign_owner(GetClassLongPtrW(self, GCLP_HCURSOR))
        return self._cursor
    
    @cursor.setter
    def cursor(self, cursor: int | HANDLE):
        if self.value:
            SetClassLongPtrW(self, GCLP_HCURSOR, cursor)
        self._cursor = cursor
        
    @property
    def background_brush(self) -> Brush | None:
        if self.value:
            x = GetClassLongPtrW(self, GCLP_HBRBACKGROUND)
        else:
            x = self._background_brush
        if x <= 31:
            brush = Brush.stock(x)
        else:
            brush = Brush.foreign_owner(x)
        return brush
    
    @background_brush.setter
    def background_brush(self, background_brush: int | HANDLE | None = None):
        if background_brush is None:
            background_brush = 0
        else:
            if isinstance(background_brush, HANDLE):
                background_brush = background_brush.value
            if background_brush <= 31:
                background_brush += 1
        if self.value:
            SetClassLongPtrW(self, GCLP_HBRBACKGROUND, background_brush)
        else:
            self._background_brush = background_brush
            
    @property
    def small_icon(self) -> Icon | None:
        if self.value:
            return Icon.foreign_owner(GetClassLongPtrW(self, GCLP_HICONSM))
        return self._small_icon
    
    @small_icon.setter
    def small_icon(self, small_icon: int | HANDLE | None):
        if self.value:
            SetClassLongPtrW(self, GCLP_HICONSM, small_icon)
        else:
            self._small_icon = small_icon
    
    def get_class_word(self, index: int) -> int:
        """
        Get class word value at specified index.
        """
        return GetClassWord(self, index)
    
    def set_class_word(self, index: int, value: WT_ADDRLIKE) -> int:
        """
        Set class word value at specified index.
        """
        value = PtrUtil.get_address(value)
        result = SetClassWord(self, index, value)
        if not result:
            code = GetLastError()
            if code != 0: raise WinException(code)
        return result
    
    def get_class_long(self, index: int) -> int:
        """
        Get class long value at specified index.
        """
        return GetClassLongW(self, index)
    
    def set_class_long(self, index: int, value: WT_ADDRLIKE) -> int:
        """
        Set class long value at specified index.
        """
        value = PtrUtil.get_address(value)
        result = SetClassLongW(self, index, value)
        if not result:
            code = GetLastError()
            if code != 0: raise WinException(code)
        return result
    
    def get_class_long_ptr(self, index: int) -> int:
        """
        Get class long pointer value at specified index.
        """
        return GetClassLongPtrW(self, index)
    
    def set_class_long_ptr(self, index: int, value: WT_ADDRLIKE) -> int:
        """
        Set class long pointer value at specified index.
        """
        value = PtrUtil.get_address(value)
        result = SetClassLongPtrW(self, index, value)
        if not result:
            code = GetLastError()
            if code != 0: raise WinException(code)
        return result
    
    def enable(self, enable: bool = True):
        """
        Enable the window.
        """
        EnableWindow(self, enable)
        
    def disable(self):
        """
        Disable the window.
        """
        EnableWindow(self, False)
    
    def register(self) -> Atom | None:
        """
        Register the window class.
        """
        wcex = WNDCLASSEXW()
        wcex.cbSize = wcex.size()
        # standard icon/cursor loading
        if self._icon is None:
            self._icon = self.WINABS_ICON
        if self._cursor is None:
            self._cursor = Cursor.load(IDC_ARROW)
        # visual setting
        wcex.hbrBackground = self._background_brush
        wcex.hIcon = self._icon
        wcex.hCursor = self._cursor
        wcex.style = self.class_style
        wcex.hIconSm = self._small_icon
        
        # the base handle of executable module (commonly python.exe)
        wcex.hInstance = GetModuleHandleW(NULL)
        
        # install the class window procedure
        self.pfnWndProc = wcex.lpfnWndProc = WNDPROC(self.window_proc)
        # construct the unique class name
        class_name = f'Win-Abs/Class:{wcex.style}:{wcex.hIcon}:{wcex.hIconSm}:{wcex.hCursor}:{wcex.hbrBackground}:{PtrUtil.get_address(wcex.lpfnWndProc)}:{wcex.cbClsExtra}:{wcex.cbWndExtra}:{wcex.hInstance}'
        wcex.lpszClassName = class_name
        # check the registration result
        atom = RegisterClassEx(wcex.ref())
        if not atom:
            code = GetLastError()
            if code != ERROR_CLASS_ALREADY_EXISTS:
                raise WinException(code)
            atom = None
        else:
            atom = Atom.foreign_owner(atom, local=True)
        
        self._class_name = class_name
        return atom
    
    def unregister(self):
        """
        Unregister the window class.
        """
        if self._class_name is not None:
            if not UnregisterClassW(self._class_name, GetModuleHandleW(NULL)):
                raise WinException()
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL,
               identifier: int | HMENU = NULL, parameter: int | WT_ADDRLIKE = NULL):
        """
        Create the window.
        """
        if self._class_name is None:
            self.register()
        self.value = CreateWindowExW(self._extended_style, self._class_name, window_name, self._style, 
                                     x, y, width, height, parent, identifier, GetModuleHandleW(NULL), PtrUtil.get_address(parameter))
        if not self.value:
            error = GetLastError()
            if error != 0: raise WinException(error)
            else: return
        
        Window._foreign_cache[self.value] = self
        self.on_fully_created()
    
    def on_paint(self, dc: PaintDC) -> bool:
        return False
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        return False
    
    def on_erase_background(self, dc: DC) -> bool:
        return False
    
    def on_set_cursor(self, window: 'Window', ht: int, message: int) -> bool:
        return None
    
    def on_nc_paint(self, dc: DC, region: Region):
        return self # sentinel value
    
    def on_nc_hittest(self, x: int, y: int) -> int:
        return None
    
    def on_nc_calcsize(self, rect: RECT, rectangles: list=None, position: WINDOWPOS=None) -> int:
        return self # sentinel value
    
    def on_uah_destroy_window(self) -> bool:
        return False
    
    def on_uah_draw_menu(self, menu: UAHMENU) -> bool:
        return False
    
    def on_uah_draw_menu_item(self, item: UAHDRAWMENUITEM) -> bool:
        return False
    
    def on_uah_init_menu(self) -> bool:
        return False
    
    def on_uah_measure_menu_item(self, item: UAHMEASUREMENUITEM) -> bool:
        return False
    
    def on_uah_nc_paint_init_menu_popup(self) -> bool:
        return False
    
    def on_nc_activate(self, active: bool, window: TUnion['Window', None]) -> bool:
        return False
    
    def on_get_minmax_info(self, info: MINMAXINFO) -> bool:
        return False
    
    def on_sys_command(self, code: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_left_button_down(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_left_button_up(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_left_button_double_click(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_right_button_down(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_right_button_up(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_right_button_double_click(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_x_button_down(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_x_button_up(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_x_button_double_click(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_middle_button_down(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_middle_button_up(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_middle_button_double_click(self, ht: int, x: int, y: int) -> bool:
        return False
    
    def on_nc_mouse_leave(self) -> bool:
        return False
    
    def on_control_color_edit(self, edit: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_control_color_listbox(self, listbox: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_control_color_msgbox(self, msgbox: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_control_color_static(self, static: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_control_color_button(self, button: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_control_color_dialog(self, dialog: 'Window', dc: DC) -> int | HANDLE | None:
        return None
    
    def on_get_icon(self, icon_type: int, dpi: int) -> int | HANDLE:
        return self # sentinel value
    
    def on_set_icon(self, icon_type: int, icon: Icon | None) -> int | HANDLE:
        return self # sentinel value
    
    # ** Main window procedure ** #
    def window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        # setup last message structure for access
        self.last_message.hWnd = hwnd # handle to the window
        self.last_message.message = msg # message code
        self.last_message.wParam = wParam # wParam
        self.last_message.lParam = lParam # lParam
        if msg == WM_CREATE: # window created
            self.value = hwnd # setup the HWND value to newly created window handle
            if not all(self.on_create.execute()): # check the all window.on_create returned True
                return -1 # the one of WM_CREATE handlers returned False, when abort the window creation
            self.unpend_all_messages() # if success, then unpend all pending messages queue to window
            return 0 # the message is handled, so return 0
        elif msg == WM_PAINT: # window paint request
            with PaintDC(self) as dc: # begin the paint and return dc into handler
                if self.on_paint(dc): # execute handler
                    return 0 # the message is handled, so return 0
        elif msg == WM_LBUTTONDOWN: # left mouse button down
            self.on_left_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_LBUTTONUP: # left mouse button up
            self.on_left_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_LBUTTONDBLCLK: # left mouse button double-clicked
            self.on_left_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_RBUTTONDOWN: # right mouse button down
            self.on_right_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_RBUTTONUP: # right mouse button up
            self.on_right_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_RBUTTONDBLCLK: # right mouse button double-clicked
            self.on_right_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_MBUTTONDOWN: # middle mouse button down
            self.on_middle_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_MBUTTONUP: # middle mouse button up
            self.on_middle_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_MBUTTONDBLCLK: # middle mouse button double-clicked
            self.on_middle_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_XBUTTONDOWN: # X mouse button down
            self.on_x_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_XBUTTONUP: # X mouse button up
            self.on_x_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_XBUTTONDBLCLK: # X mouse button double-clicked
            self.on_x_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_CLOSE: # window closed
            if all(self.on_close.execute()):
                self.destroy()
            return 0 # the message is handled, so return 0
        elif msg == WM_DESTROY: # window destroyed
            self.on_destroy.execute()
            return 0 # the message is handled, so return 0
        elif msg == WM_COMMAND: # command send from child to window
            self.on_command.execute(LOWORD(wParam), HIWORD(wParam), lParam)
            return 0 # the message is handled, so return 0
        elif msg == WM_SIZE: # window sized
            if self.on_size(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # the message is handled, so return 0
        elif msg == WM_KEYDOWN: # key down
            wVK = LOWORD(wParam) # virtual key code
            fKeyFlags = HIWORD(lParam) # key flags
            wScanCode = LOBYTE(fKeyFlags) # scan code
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED: # if extended scan code
                wScanCode = MAKEWORD(wScanCode, 0xE0) # when manually extend
            self.on_key_down.execute(wVK, fKeyFlags, wScanCode) # execute handler
            return 0 # the message is handled, so return 0
        elif msg == WM_KEYUP: # key up
            wVK = LOWORD(wParam) # virtual key code
            fKeyFlags = HIWORD(lParam) # key flags
            wScanCode = LOBYTE(fKeyFlags) # scan code
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED: # if extended scan code
                wScanCode = MAKEWORD(wScanCode, 0xE0) # when manually extend
            self.on_key_up.execute(wVK, fKeyFlags, wScanCode) # execute handler
            return 0 # the message is handled, so return 0
        elif msg == WM_MOVE: # window moved
            self.on_move.execute(LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_SHOWWINDOW: # window showed
            self.on_show.execute(wParam == TRUE, lParam)
            return 0 # the message is handled, so return 0
        elif msg == WM_THEMECHANGED: # window theme changed
            self.on_theme_changed.execute()
            return 0 # the message is handled, so return 0
        elif msg == WM_USERCHANGED: # user changed in system
            self.on_user_changed.execute()
            return 0 # the message is handled, so return 0
        elif msg == WM_ENABLE: # window enabled
            self.on_enable.execute(wParam == TRUE)
            return 0 # the message is handled, so return 0
        elif msg == WM_ERASEBKGND: # erase background request
            dc = DC.foreign_owner(wParam) # pack the hDC into DC wrapper
            if self.on_erase_background(dc): # the background was erased
                return TRUE
            return self.default_window_proc(hwnd, msg, wParam, lParam) # the background wasn't erased
        elif msg == WM_SETFONT: # set window font request
            self.on_set_font.execute(Font.foreign_owner(wParam), LOWORD(lParam) == TRUE)
            return 0 # the message is handled, so return 0
        elif msg == WM_MOUSEWHEEL:
            self.on_mouse_wheel.execute(SHORT(HIWORD(wParam)).value, LOWORD(wParam), LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_TIMER: # timer message
            self.on_timer.execute(wParam, i_cast(lParam, TIMERPROC))
            return 0 # the message is handled, so return 0
        elif msg == WM_NOTIFY: # notify message from child control
            nmhdr = i_cast(lParam, LPNMHDR).contents
            self.on_notify.execute(nmhdr)
            return 0 # the message is handled, so return 0
        elif msg == WM_MOUSEMOVE: # mouse moved
            self.on_mouse_move.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_DRAWITEM: # draw the item (by style *_OWNERDRAW)
            if not self.on_draw_item.empty(): # if has draw item handlers
                self.on_draw_item.execute(wParam, i_cast_value(lParam, DRAWITEMSTRUCT))
                return TRUE # WM_DRAWITEM handled
            return FALSE # not handled
        elif msg == WM_SETFOCUS: # the window got focus
            self.on_focus_changed.execute(Window.foreign(wParam)) # pack the previous focus window into Window and execute event
            return 0 # the message is handled, so return 0
        elif msg == WM_KILLFOCUS: # the window lost focus
            self.on_focus_lost.execute(Window.foreign(wParam)) # pack the new focus window into Window and execute event
            return 0 # the message is handled, so return 0
        elif msg == WM_PALETTECHANGED: # window palette changed
            self.on_palette_changed.execute(Palette.foreign_owner(wParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_SETCURSOR: # set window cursor request
            result = self.on_set_cursor(Window.foreign(wParam), LOWORD(lParam), HIWORD(lParam))
            if result is not None: # return True/False
                return result
        elif msg == WM_MEASUREITEM: # measure the item
            if not self.on_measure_item.empty(): # if has measure item handlers
                self.on_measure_item.execute(wParam, i_cast_value(lParam, MEASUREITEMSTRUCT))
                return TRUE # WM_MEASUREITEM handled
            return FALSE # not handled
        elif msg == WM_COMPAREITEM:
            if not self.on_compare_item.empty(): # if has compare item handlers
                self.on_compare_item.execute(wParam, i_cast_value(lParam, COMPAREITEMSTRUCT))
                return TRUE # WM_COMPAREITEM handled
            return FALSE # not handled
        elif msg == WM_CHAR: # the character is pressed
            # convert character code to unicode and call handler
            self.on_char.execute(chr(wParam))
            return 0 # the message is handled, so return 0
        elif msg == WM_HSCROLL: # horizontal scroll message
            self.on_hscroll.execute(LOWORD(wParam), HIWORD(wParam), Window.foreign(lParam))
            return 0
        elif msg == WM_VSCROLL: # vertical scroll message
            self.on_vscroll.execute(LOWORD(wParam), HIWORD(wParam), Window.foreign(lParam))
            return 0
        elif msg == WM_NCDESTROY: # window was completely destroyed
            self.on_nc_destroy.execute() # execute handlers
            return 0
        elif msg == WM_NCPAINT: # non-client area paint
            region = Region.foreign_owner(wParam) # create Region from wParam
            if wParam == 1:
                with DC.window(self) as dc: # get the window DC
                    # call the handler
                    result = self.on_nc_paint(dc, None)
            else:
                # todo: GetDCEx with region is breaking non-client display
                with DC.window(self) as dc: # get the window DC
                    # call the handler
                    result = self.on_nc_paint(dc, region)
            # if sentinel value matches, we are falling back to default procedure
            if result is not self:
                return 0 # otherwise we are handled the message
        elif msg == WM_NCHITTEST: # non-client area hit test message
            result = self.on_nc_hittest(LOWORD(wParam), HIWORD(wParam)) # call message handler
            # if message is handled, when return hit test result
            if result is not None: return result
        elif msg == WM_NCCALCSIZE: # non-client area calculate size
            if wParam: # if need to indicate valid client area size
                # marshal WM_NCCALCSIZE lParam parameters pointer to structure
                parameters = i_cast_value(lParam, NCCALCSIZE_PARAMS)
                
                # setup rectangles list from NCCALCSIZE_PARAMS
                rectangle0 = i_cast_structure(parameters.rgrc[0], Rect)
                rectangle1 = i_cast_structure(parameters.rgrc[1], Rect)
                rectangle2 = i_cast_structure(parameters.rgrc[2], Rect)
                rectangles = [rectangle0, rectangle1, rectangle2]
                
                # call WM_NCCALCSIZE handler
                result = self.on_nc_calcsize(rectangle0, rectangles, parameters.lppos.contents)
            else: # don't need
                result = self.on_nc_calcsize(i_cast_value(lParam, Rect)) # call handler
            # if sentinel value matches, we are falling back to default procedure
            if result is not self: 
                return 0 # otherwise we are handled the message
        elif msg == WM_MOUSELEAVE: # mouse is leaved from window
            self.on_mouse_leave.execute() # call handler
            return 0 # message handled
        elif msg == WM_POWERBROADCAST: # power broadcast message received
            n = None # additional argument
            # if wParam == PBT_POWERSETTINGCHANGE,
            if wParam == PBT_POWERSETTINGCHANGE: # then lParam contains
                n = i_cast_value(lParam, POWERBROADCAST_SETTING) # PPOWERBROADCAST_SETTING
            self.on_power_broadcast.execute(wParam, n) # execute the handler
            return TRUE # message handled
        elif msg == WM_SIZING: # window is being sized
            # unpack edge and rectangle, call handler
            self.on_sizing.execute(wParam, i_cast_value(lParam, Rect))
            return TRUE # message handled
        elif msg == WM_ENTERIDLE: # window is entering idle state
            # unpack state and window and call handler
            self.on_enter_idle.execute(wParam, Window.foreign(lParam))
            return 0 # the message is handled, so return 0d
        elif msg == WM_SYSCOMMAND: # on system command received
            # unpack SC_* code and x,y coords and call handler, check boolean return
            if self.on_sys_command(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # the message is handled so return 0
            # otherwise, let it fallback
        elif msg == WM_ENTERMENULOOP: # window is entered menu loop
            self.on_enter_menu_loop.execute(wParam != 0) # unpack boolean from wParam and call handler
            return 0 # the message is handled, so return 0
        elif msg == WM_EXITMENULOOP: # window is exited menu loop
            self.on_exit_menu_loop.execute(wParam != 0) # unpack boolean from wParam and call handler
            return 0 # the message is handled, so return 0
        # undocumented UAH messages handling
        elif msg == WM_UAHDESTROYWINDOW:
            # UAH: window destroying notification
            if self.on_uah_destroy_window():
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_UAHDRAWMENU:
            # UAH: handle this to draw menu
            if self.on_uah_draw_menu(UAHMENU.from_address(lParam)):
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_UAHDRAWMENUITEM:
            # UAH: handle this to draw menu item
            if self.on_uah_draw_menu_item(UAHDRAWMENUITEM.from_address(lParam)):
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_UAHINITMENU:
            # UAH: called when menu is initialized
            if self.on_uah_init_menu():
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_UAHMEASUREMENUITEM:
            # UAH: handle this to measure menu item
            if self.on_uah_measure_menu_item(UAHMEASUREMENUITEM.from_address(lParam)):
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_UAHNCPAINTMENUPOPUP:
            # UAH: menu popup window NCPAINT
            if self.on_uah_nc_paint_init_menu_popup():
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_NCACTIVATE:
            # non-client area is being activated
            if self.on_nc_activate(wParam != FALSE, Window.foreign(lParam) if lParam != MAXULONG_PTR else None):
                return TRUE # if handled return TRUE, otherwise let it fallback
        elif msg == WM_ACTIVATEAPP:
            # the different application window is being activated
            self.on_activate_app.execute(wParam != FALSE, lParam)
            return 0 # the message is handled so return 0
        elif msg == WM_ACTIVATE:
            # the window is being activated or deactivated
            self.on_activate.execute(wParam, Window.foreign(lParam))
            return 0 # the message is handled so return 0
        elif msg == WM_CHILDACTIVATE:
            # sent to the child window when the window's title bar clicked or over activation operation performed
            self.on_child_activate.execute()
            return 0
        elif msg == WM_COMPACTING:
            # system memory is low and WM_COMPACTING is sent
            self.on_compacting.execute(round(wParam / 65535 * 100))
            return 0 # the message is handled so return 0
        elif msg == WM_GETMINMAXINFO:
            # the system is needed in min and max window sizes
            # cast lParam to MINMAXINFO and call handler
            if self.on_get_minmax_info(i_cast_value(lParam, MINMAXINFO)):
                return 0 # the message is handled so return 0
            # otherwise let it fallback
        elif msg == WM_STYLECHANGED:
            # the one of window's styles has been changed
            ss = i_cast_value(lParam, STYLESTRUCT) # cast the lParam to STYLESTRUCT
            if wParam == GWL_STYLE: # if change is a simple style,
                self.on_style_changed.execute(ss) # when call its handler
            elif wParam == GWL_EXSTYLE: # otherwise, if change is extended style
                self.on_extended_style_changed.execute(ss) # when call its handle
            return 0 # the message is handled so return 0
        elif msg == WM_STYLECHANGING:
            # the one of window's styles is being to be changed
            ss = i_cast_value(lParam, STYLESTRUCT) # cast the lParam to STYLESTRUCT
            if wParam == GWL_STYLE: # if change is a simple style,
                self.on_style_changing.execute(ss) # when call its handler
            elif wParam == GWL_EXSTYLE: # otherwise, if change is extended style
                self.on_extended_style_changing.execute(ss) # when call its handle
            return 0 # the message is handled so return 0
        elif msg == WM_WINDOWPOSCHANGED:
            # the window position is has been changed
            pos = i_cast_value(lParam, WINDOWPOS) # cast the lParam to WINDOWPOS
            self.on_window_position_changed.execute(pos) # call handler
        elif msg == WM_WINDOWPOSCHANGING:
            # the window position is being to be changed
            pos = i_cast_value(lParam, WINDOWPOS) # cast the lParam to WINDOWPOS
            self.on_window_position_changing.execute(pos) # call handler
        elif msg == WM_NCMOUSELEAVE: # the mouse leaving non-client area
            # call the handler and check result
            if not self.on_nc_mouse_leave():
                result = LRESULT()
                # get the result from DWM default window procedure
                if not is_null(DwmDefWindowProc):
                    if DwmDefWindowProc(hwnd, msg, wParam, lParam, byref(result)):
                        return result.value # if succeeded, then return LRESULT
                # otherwise let it fallback
            else: # otherwise the message is handled
                return 0
        elif msg == WM_NCLBUTTONDOWN: # the left mouse button was pressed over non-client area
            # call the handler and check the boolean result
            if self.on_nc_left_button_down(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCLBUTTONUP: # the left mouse button was released over non-client area
            # call the handler and check the boolean result
            if self.on_nc_left_button_up(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCLBUTTONDBLCLK: # the left mouse button was double-clicked over non-client area
            # call the handler and check the boolean result
            if self.on_nc_left_button_double_click(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCRBUTTONDOWN: # the right mouse button was pressed over non-client area
            # call the handler and check the boolean result
            if self.on_nc_right_button_down(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCRBUTTONUP: # the right mouse button was released over non-client area
            # call the handler and check the boolean result
            if self.on_nc_right_button_up(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCRBUTTONDBLCLK: # the right mouse button was double-clicked over non-client area
            # call the handler and check the boolean result
            if self.on_nc_right_button_double_click(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCXBUTTONDOWN: # the X mouse button was pressed over non-client area
            # call the handler and check the boolean result
            if self.on_nc_x_button_down(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCXBUTTONUP: # the X mouse button was released over non-client area
            # call the handler and check the boolean result
            if self.on_nc_x_button_up(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCXBUTTONDBLCLK: # the X mouse button was double-clicked over non-client area
            # call the handler and check the boolean result
            if self.on_nc_x_button_double_click(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCMBUTTONDOWN: # the middle mouse button was pressed over non-client area
            # call the handler and check the boolean result
            if self.on_nc_middle_button_down(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCMBUTTONUP: # the middle mouse button was released over non-client area
            # call the handler and check the boolean result
            if self.on_nc_middle_button_up(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_NCMBUTTONDBLCLK: # the middle mouse button was double-clicked over non-client area
            # call the handler and check the boolean result
            if self.on_nc_middle_button_double_click(wParam, LOWORD(lParam), HIWORD(lParam)):
                return 0 # if the message is handled then return 0
            # otherwise let it fallback
        elif msg == WM_CAPTURECHANGED: # the mouse capture has been changed
            # call the handler, lParam=window that is gaining mouse capture
            self.on_capture_changed.execute(Window.foreign(lParam))
            return 0 # the message is handled.
        elif msg == WM_DWMCOLORIZATIONCOLORCHANGED: # DWM colorization settings is changed
            # call the handler, wParam=colorARGB, lParam=isBlended
            self.on_dwm_colorization_color.execute(Color.ARGB(wParam), lParam != FALSE)
            return 0 # the message is handled
        elif msg == WM_DWMCOMPOSITIONCHANGED: # DWM composition is enabled/disabled (Vista or 7)
            # call the handler
            self.on_dwm_composition_changed.execute()
            return 0 # the message is handled
        elif msg == WM_DWMNCRENDERINGCHANGED: # DWM non-client rendering is enabled/disabled
            # call the handler, wParam=fEnabled
            self.on_dwm_nc_rendering_changed.execute(wParam != FALSE)
            return 0 # the message is handled
        elif msg == WM_DWMSENDICONICLIVEPREVIEWBITMAP: # window need to provide a iconic live preview bmp
            # call the handler
            self.on_dwm_send_iconic_live_preview_bitmap.execute()
            return 0 # the message is handled
        elif msg == WM_DWMSENDICONICTHUMBNAIL: # window need to provide a thumbnail bmp
            # call the handler, lParam HIWORD=width, lParam LOWORD=height
            self.on_dwm_send_iconic_thumbnail.execute(HIWORD(lParam), LOWORD(lParam))
            return 0 # the message is handled
        elif msg == WM_DWMWINDOWMAXIMIZEDCHANGE: # DWM-composed window is maximized or minimized
            # call the handler, wParam=fMinimized
            self.on_dwm_window_maximized_change.execute(wParam != FALSE)
            return 0 # the message is handled
        elif msg == WM_DWMEXILEFRAME: # UNDOCUMENTED(DWM): the DWM instructs window to exile frame from compositor
            # call the handler, wParam=fExile
            self.on_dwm_exile_frame.execute(wParam != FALSE)
            return 0 # the message is handled
        elif msg == WM_MAGNIFICATION_STARTED: # UNDOCUMENTED(Vista+): magnification process has been started
            # call the handler, wParam=fMagnification
            self.on_magnification_started.execute(wParam != FALSE)
            return 0 # the message is handled
        elif msg == WM_CTLCOLOREDIT: # the window can change edit control's colors
            # call the handler, wParam=hDC, lParam=hEdit
            brush = self.on_control_color_edit(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_CTLCOLORSTATIC: # the window can change static control's colors
            # call the handler, wParam=hDC, lParam=hStatic
            brush = self.on_control_color_static(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_CTLCOLORMSGBOX: # the window can change msgbox's colors
            # call the handler, wParam=hDC, lParam=hMsgBox
            brush = self.on_control_color_msgbox(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_CTLCOLORLISTBOX: # the window can change listbox control's colors
            # call the handler, wParam=hDC, lParam=hListBox
            brush = self.on_control_color_listbox(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_CTLCOLORBTN: # the window can change button's colors
            # call the handler, wParam=hDC, lParam=hButton
            brush = self.on_control_color_button(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_CTLCOLORDLG: # the window can change dialog's colors
            # call the handler, wParam=hDC, lParam=hDialog
            brush = self.on_control_color_dialog(Window.foreign(lParam), DC.foreign_owner(wParam))
            if brush: # if not None or not NULL brush returned, then return it
                return PtrUtil.get_address(brush)
            # otherwise let it fallback
        elif msg == WM_SYSCOLORCHANGE: # the system colors is changed
            # call the handler
            self.on_sys_color_change.execute()
            return 0 # message handled
        elif msg == WM_GETICON: # the window has to return the icon
            # call the handler, wParam=nIconType, lParam=nDPI
            result = self.on_get_icon(wParam, lParam)
            if result is not self: # if sentinel value is not returned:
                return result # then return it as icon handle
            # otherwise let it fallback into default proc
        elif msg == WM_SETICON: # the icon of a window is changed by external app
            # wParam=nIconType, lParam=hIcon or NULL
            if lParam == 0: # if setted to NULL, then
                icon = None # icon = None
            else: # otherwise it is handle
                icon = Icon.foreign_owner(lParam)
            # call the handler
            result = self.on_set_icon(wParam, icon)
            if result is self: pass # sentinel value, fallback to default handler
            else: # message is handled
                return result # return icon handle or NULL
            # let it fallback into default proc
        elif msg == WM_TIMECHANGE: # the system broadcasting time change to all windows
            # call the handler
            self.on_time_changed.execute()
            return 0 # message is handled
        else:
            # unknown window message received
            result = self.on_unknown_message.execute(hwnd, msg, wParam, lParam) # trying to call all unknown message handlers
            for value in result: # iterate through returned values tuple
                if value is not None: # if value != None, when handler is handled our message
                    return value # return handler value as procedure LRESULT
        
        return self.default_window_proc(hwnd, msg, wParam, lParam) # otherwise let procedure fallback into defined fallback procedure (commonly DefWindowProc)
    
    def window_subclass_thunk_proc(self, hwnd: int, msg: int, wParam: int, lParam: int, subclassId: int, dwUnused: int): 
        if msg == WM_NCDESTROY:
            RemoveWindowSubclass(hwnd, self.pfnSubclassThunkProc, subclassId)
        elif msg == WM_CREATE:
            self.value = hwnd
        result = self.window_subclass_proc(hwnd, msg, wParam, lParam)
        if result is None: return DefSubclassProc(hwnd, msg, wParam, lParam)
        return result
    
    def subclass(self):
        SetWindowSubclass(self, self.pfnSubclassThunkProc, SubclassIdentifiers[id(self)], 0)
    
    def unsubclass(self):
        RemoveWindowSubclass(self, self.pfnSubclassThunkProc, SubclassIdentifiers[id(self)])
        
    def window_subclass_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        return None
    
    def default_window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return DefWindowProcW(hwnd, msg, wParam, lParam) # standard window procedure fallback
    
    def focus(self):
        """
        Focus the current window.
        """
        SetFocus(self)
    
    @property
    def focused(self) -> bool:
        return GetFocus() == self.value
    
    @property
    def visible(self) -> bool:
        return IsWindowVisible(self) != FALSE
    
    def capture(self):
        """
        Set the current window as mouse capture.
        """
        SetCapture(self)
    
    @property
    def capturing(self) -> bool:
        return GetCapture() == self.value
    
    @capturing.setter
    def capturing(self, capturing: bool):
        if capturing:
            self.capture()
        else:
            ReleaseCapture()
    
    def timer(self, function: Callable[[int, int], None], elapse: int, event_id: int = 0) -> int:
        # timer procedure
        @TIMERPROC
        def timerProc(hWndUnused: int, wmTimerUnused: int, idEvent: int, dwTime: int):
            function(idEvent, dwTime) # call the function with useful arguments: event ID and time
        event_id = SetTimer(self, event_id, elapse, timerProc)
        # cache timer in callback cache for GC safety
        self._timers[event_id] = timerProc
        return event_id
    
    def delay(self, function: Callable, elapse: int, event_id: int = 0) -> int:
        # timer procedure
        @TIMERPROC
        def timerProc(hWndUnused: int, wmTimerUnused: int, idEvent: int, dwTimeUnused: int):
            function() # call the function without arguments (delayed function does not needs in event ID / time)
            self.kill_timer(idEvent) # kill the timer after calling callback, it is 1 times called timer.
        event_id = SetTimer(self, event_id, elapse, timerProc)
        # cache timer in callback cache for GC safety
        self._timers[event_id] = timerProc
        return event_id
    
    def kill_timer(self, event_id: int):
        """
        Kill the timer by given Event ID.
        """
        if not KillTimer(self, event_id):
            raise WinException()
        # if event held by window, remove callback cache for event
        if event_id in self._timers:
            del self._timers[event_id]
        
    def close(self):
        """
        Close the window.
        """
        self.post(WM_CLOSE)
        
    def destroy(self):
        """
        Destroy the window.
        """
        if not DestroyWindow(self):
            raise WinException()
        
    def hide(self, asynchronous: bool = True):
        """
        Hide the window.
        """
        if asynchronous:
            ShowWindowAsync(self, SW_HIDE)
        else:
            ShowWindow(self, SW_HIDE)
    
    def show(self, nCmdShow: int = SW_SHOW, asynchronous: bool = True):
        """
        Show the window.
        """
        if asynchronous:
            ShowWindowAsync(self, nCmdShow)
        else:
            ShowWindow(self, nCmdShow)
        
    def set_font(self, font: int | HANDLE, redraw: bool = True):
        """
        Set the window font.
        """
        self.post(WM_SETFONT, font, redraw)
        
    @property
    def font(self) -> Font | None:
        return Font.foreign_owner(self.send(WM_GETFONT))
    
    @font.setter
    def font(self, font: int | HANDLE):
        self.set_font(font)
    
    def is_child(self, hWnd: int | HANDLE) -> bool:
        """
        Check another window is a child of window.
        """
        return IsChild(self, hWnd) != 0
    
    def is_child_of(self, hWnd: int | HANDLE) -> bool:
        """
        Check is window child of another window.
        """
        return IsChild(hWnd, self) != 0
    
    def send_message(self, smt: int, message: int, wParam: WT_ADDRLIKE | str = 0, lParam: WT_ADDRLIKE | str = 0):
        """
        Overrideable send message with Send/Post negotiation and pending support.
        """
        if isinstance(wParam, str):
            wParam = create_unicode_buffer(wParam)
        if isinstance(lParam, str):
            lParam = create_unicode_buffer(lParam)
        
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
        
        if smt == WSMT_WPARAMFORMAT:
            return wParam
        elif smt == WSMT_LPARAMFORMAT:
            return lParam
            
        if not self.value and hasattr(self, 'pending_messages'):
            self.pending_messages.append((smt, message, wParam, lParam))
            return 0
        
        if smt == WSMT_POST:
            PostMessageW(self, message, wParam, lParam)
            return 0
        elif smt == WSMT_SEND:
            return SendMessageW(self, message, wParam, lParam)
        elif smt == WSMT_DEFAULT:
            return self.default_window_proc(self, message, wParam, lParam)
        elif smt == WSMT_NOTIFY:
            return SendNotifyMessageW(self, message, wParam, lParam)
        elif smt == WSMT_DEFAULTSUBCLASS:
            return DefSubclassProc(self, message, wParam, lParam)
        return 0
    
    def send(self, message: int, wParam: WT_ADDRLIKE | str = 0, lParam: WT_ADDRLIKE | str = 0) -> int:
        """
        Send the message to window.
        """
        return self.send_message(WSMT_SEND, message, wParam, lParam)
    
    def send_timeout(self, message: int, wParam: WT_ADDRLIKE | str = 0, lParam: WT_ADDRLIKE | str = 0, flags: int = SMTO_NORMAL, timeout: int = 0) -> int:
        """
        Send the message to window with timeout and flags.
        """
        wParam = self.send_message(WSMT_WPARAMFORMAT, 0, wParam, 0)
        lParam = self.send_message(WSMT_LPARAMFORMAT, 0, 0, lParam)
        lResult = DWORD_PTR()
        SetLastError(0)
        if not SendMessageTimeoutW(self, message, wParam, lParam, flags, timeout, byref(lResult)):
            code = GetLastError()
            if code != 0:
                raise WinException(code)
        return lResult.value
    
    def send_timeout_indirect(self, msg: MSG, flags: int = SMTO_NORMAL, timeout: int = 0) -> int:
        """
        Indirectly send the message to window with timeout and flags.
        """
        return self.send_timeout(msg.message, msg.wParam, msg.lParam, flags, timeout)
    
    def post(self, message: int, wParam: WT_ADDRLIKE | str = 0, lParam: WT_ADDRLIKE | str = 0):
        """
        Post the message to window (asynchronous send).
        """
        self.send_message(WSMT_POST, message, wParam, lParam)
 
    def map(self, window: int | HWND, points: Iterable[GraphicUtils.Point]) -> tuple[POINT, ...]:
        """
        Map the given points of window to an another window.
        """
        pointsToMap = [GraphicUtils.point(point) for point in points]
        length = len(points)
        pPoints = (Point * length)(*pointsToMap)
        MapWindowPoints(self, window, pPoints, length)
        return tuple(pPoints)
    
    def post_indirect(self, msg: MSG):
        """
        Indirectly post MSG structure to the window (asynchronous send).
        """
        return self.send_message(WSMT_POST, msg.message, msg.wParam, msg.lParam)
    
    def send_indirect(self, msg: MSG) -> int:
        """
        Indirectly send MSG structure to the window.
        """
        return self.send_message(WSMT_SEND, msg.message, msg.wParam, msg.lParam)
    
    def send_message_indirect(self, smt: int, msg: MSG) -> int:
        """
        Indirectly send message with send/post negotiation.
        """
        return self.send_message(smt, msg.message, msg.wParam, msg.lParam)
    
    def unpend_all_messages(self) -> tuple[int, int]:
        """
        Unpend all send all pended messages.
        """
        result = (self.send_message(smt, msg, wParam, lParam) for smt, msg, wParam, lParam in self.pending_messages)
        self.pending_messages.clear()
        return result
    
    def pend_message(self, smt: int, message: int, wParam: int = 0, lParam: int = 0):
        """
        Pend the message into pending queue.
        """
        self.pending_messages.append((smt, message, wParam, lParam))
    
    @property
    def menu(self) -> Menu | None:
        return Menu.foreign_owner(GetMenu(self))
    
    @menu.setter
    def menu(self, menu: int | HANDLE):
        if not SetMenu(self, menu):
            raise WinException()
    
    @property
    def name(self) -> str:
        nText = GetWindowTextLengthW(self) + 1
        buffer = create_unicode_buffer(nText)
        GetWindowTextW(self, buffer, nText)
        return buffer.value
    
    @name.setter
    def name(self, name: str):
        if not SetWindowTextW(self, name):
            raise WinException()
    
    @property
    def parent(self) -> 'Window':
        return Window.foreign(GetParent(self))
    
    @parent.setter
    def parent(self, parent: int | HWND):
        SetParent(self, parent)
        
    @property
    def rect(self) -> Rect:
        rc = Rect()
        if not GetWindowRect(self, byref(rc)):
            raise WinException()
        return rc
    
    def set_position(self, x: int = None, y: int = None, 
                     width: int = None, height: int = None, 
                     flags: int = 0, insert_after: int | HWND = None):
        """
        Set the window position.
        """
        if insert_after is None:
            flags |= SWP_NOZORDER
        notx, noty = x is None, y is None
        if notx or noty:
            if notx and noty:
                flags |= SWP_NOMOVE
                x = y = 0
            else:
                pos = self.position
                if notx: x = pos[0]
                if noty: y = pos[1]
        notw, noth = width is None, height is None
        if notw or noth:
            if notw and noth:
                flags |= SWP_NOSIZE
                width = height = 0
            else:
                rect = self.rect
                if notw: width = rect.right - rect.left
                if noth: height = rect.bottom - rect.top
        if not SetWindowPos(self, insert_after, x, y, width, height, flags):
            raise WinException()
    
    @classmethod
    def foreground(self) -> 'Window':
        """
        Get the foreground window.
        """
        return Window.foreign(GetForegroundWindow())
    
    @classmethod
    def desktop(self) -> 'Window':
        """
        Get the desktop window.
        """
        return Window.foreign(GetDesktopWindow())
    
    def set_foreground(self):
        """
        Set the current window as foreground.
        """
        if not SetForegroundWindow(self):
            raise WinException()
        
    def to_client(self, screen: POINT):
        """
        Convert screen point to client point.
        """
        if not ScreenToClient(self, byref(screen)):
            raise WinException()
        
    def to_screen(self, client: POINT):
        """
        Convert client point to screen point.
        """
        if not ClientToScreen(self, byref(client)):
            raise WinException()
        
    @property
    def client_rect(self) -> Rect:
        rc = Rect()
        if not GetClientRect(self, byref(rc)):
            raise WinException()
        return rc
    
    @client_rect.setter
    def client_rect(self, client_rect: RECT):
        self.set_position(
            x=client_rect.left, y=client_rect.top, 
            width=client_rect.right - client_rect.left,
            height=client_rect.bottom - client_rect.top)
        
    @property
    def valid(self):
        return IsWindow(self) != 0
    
    @property
    def width(self) -> int:
        rc = self.rect
        return rc.right - rc.left
    
    @width.setter
    def width(self, width: int):
        self.set_position(width=width)
    
    @property
    def height(self) -> int:
        rc = self.rect
        return rc.bottom - rc.top
    
    @height.setter
    def height(self, height: int):
        self.set_position(height=height)
        
    @property
    def size(self) -> tuple[int, int]:
        rc = self.rect
        return (rc.right - rc.left, rc.bottom - rc.top)
    
    @size.setter
    def size(self, size: tuple[int, int]):
        self.set_position(width=size[0], height=size[1])
        
    @property
    def x(self) -> int:
        return self.position[0]
    
    @x.setter
    def x(self, x: int):
        self.set_position(x=x)
        
    @property
    def y(self) -> int:
        return self.position[1]
    
    @y.setter
    def y(self, y: int):
        self.set_position(y=y)
    
    @property
    def position(self) -> tuple[int, int]:
        rc = self.rect
        pt = POINT(rc.left, rc.top)
        self.to_client(pt)
        return pt.x, pt.y
    
    @position.setter
    def position(self, position: GraphicUtils.Point):
        point = GraphicUtils.point(position)
        self.set_position(x=point.x, y=point.y)
        
    def invalidate(self, region: RECT | Region = None, erase: bool = True):
        """
        Invalidate the given rectangle/region (or NULL) of window.
        """
        if region is NULL:
            InvalidateRect(self, NULL, erase)
        elif isinstance(region, Region):
            InvalidateRgn(self, region, erase)
        else:
            InvalidateRect(self, region.ref(), erase)
    
    def update(self):
        """
        Update the window view.
        """
        if not UpdateWindow(self):
            raise WinException()
        
    def set_dwm_attribute(self, attribute: int, value: CData):
        """
        Set the DWM attribute of window.
        """
        hr = DwmSetWindowAttribute(self, attribute, addressof(value), sizeof(value))
        if FAILED(hr): raise COMError(hr)
        
    def set_composition_attribute(self, attribute: int, value: CData):
        """
        Set the composition attribute of window.
        """
        wcad = WINDOWCOMPOSITIONATTRIBDATA(attribute, addressof(value), sizeof(value))
        hr = SetWindowCompositionAttribute(self, wcad.ref())
        if FAILED(hr): raise COMError(hr)
    
    def get_long(self, index: int) -> int:
        """
        Get window long value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        result = GetWindowLongW(self, index)
        if not result: 
            code = GetLastError()
            if code != 0: raise WinException(code)
        return result
    
    def set_long(self, index: int, value: int):
        """
        Set window long value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        if not SetWindowLongW(self, index, value):
            code = GetLastError()
            if code != 0: raise WinException(code)
    
    def get_long_ptr(self, index: int) -> int:
        """
        Get window long pointer value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        result = GetWindowLongPtrW(self, index)
        if not result: 
            code = GetLastError()
            if code != 0: raise WinException(code)
        return result
    
    def set_long_ptr(self, index: int, value: int):
        """
        Set window long pointer value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        if not SetWindowLongPtrW(self, index, value):
            code = GetLastError()
            if code != 0: raise WinException(code)
        
    def redraw(self, flags: int, region: RECT | Region=NULL):
        """
        Redraw the window.
        """
        if region is NULL:
            result = RedrawWindow(self, NULL, NULL, flags)
        elif isinstance(region, Region): 
            result = RedrawWindow(self, NULL, region, flags)
        else: 
            result = RedrawWindow(self, region.ref(), NULL, flags)
        if not result: raise WinException()
        
    def validate(self, region: RECT | Region = None):
        """
        Validate the given rectangle/region (or NULL) of window.
        """
        if region is NULL:
            ValidateRect(self, NULL)
        elif isinstance(region, Region):
            ValidateRgn(self, region)
        else:
            ValidateRect(self, region.ref())
            
    @classmethod
    def from_dc(cls, dc: DC) -> 'Window':
        """
        Get the window from DC.
        """
        return cls.foreign(WindowFromDC(dc))
    
    def draw_caption(self, dc: DC, rect: RECT, flags: int):
        """
        Draw the caption of window.
        """
        if not DrawCaption(self, dc, rect.ref(), flags):
            raise WinException()
        
    @classmethod
    def from_point(cls, point: POINT, physical: bool = False) -> 'Window':
        """
        Get the window from point (DPI-adjusted or physical).
        """
        if not physical: return cls.foreign(WindowFromPoint(point))
        else: return cls.foreign(WindowFromPhysicalPoint(point))

    def set_layered_attributes(self, color: Color.IColorAlpha | int, alpha: bool, flags: int):
        """
        Set the opacity and transparency color key of a layered window.
        """
        if not SetLayeredWindowAttributes(self, int(color), alpha, flags):
            raise WinException()
    
    def update_layered(self, flags: int, color: Color.IColorAlpha | int, dest_dc: DC=NULL, 
                       dest_point: GraphicUtils.Point=NULL, size: GraphicUtils.Size=NULL, src_dc: DC=NULL, 
                       src_point: GraphicUtils.Point=NULL, blend: BLENDFUNCTION=NULL):
        """
        Update the position, size, shape, content, and translucency of a layered window.
        """
        if not UpdateLayeredWindow(self, dest_dc, GraphicUtils.point(dest_point).ref() if dest_point is not NULL else NULL,
                                   GraphicUtils.size(size).ref() if size is not NULL else NULL, src_dc,
                                   GraphicUtils.point(src_point).ref() if src_point is not NULL else NULL,
                                   color, blend.ref() if blend is not NULL else NULL, flags):
            raise WinException()
        
    def tile_windows(self, how: int, windows: Iterable['Window'], rect: RECT = NULL):
        """
        Tile specified child windows.
        """
        if rect is not NULL: rect = rect.ref()
        cKids = len(windows)
        lpKids = (HWND * cKids)(*windows)
        if not TileWindows(self, how, rect, cKids, lpKids) and cKids:
            raise WinException()
        
    def tile(self, how: int, rect: RECT = NULL):
        """
        Tile current window.
        """
        parent = self.parent
        if not parent:
            Window.tile_windows(None, how, [self], rect)
        else:
            parent.tile_windows(how, [self], rect)
        
    def get_prop(self, prop: str | int | Atom) -> int:
        """
        Get the property value in window property list.
        """
        if isinstance(prop, str):
            prop = create_unicode_buffer(prop)
        prop = i_cast(PtrUtil.get_address(prop), LPCWSTR)
        SetLastError(0)
        data = GetPropW(self, prop)
        if not data:
            code = GetLastError()
            if code != 0:
                raise WinException(code)
        return data
        
    def set_prop(self, prop: str | int | Atom, data: WT_ADDRLIKE):
        """
        Set the property value in window property list.
        """
        if isinstance(prop, str):
            prop = create_unicode_buffer(prop)
        prop = i_cast(prop, LPCWSTR)
        data = PtrUtil.get_address(data)
        if not SetPropW(self, prop, data):
            raise WinException()
    
    def remove_prop(self, prop: str | int) -> int:
        """
        Remove the property from window property list.
        """
        if isinstance(prop, str):
            prop = create_unicode_buffer(prop)
        prop = i_cast(prop, LPCWSTR)
        SetLastError(0)
        data = RemovePropW(self, prop)
        if not data:
            code = GetLastError()
            if code != 0:
                raise WinException(code)
        return data
        
    def draw_theme_parent_bk(self, dc: int | HANDLE, rect: RECT = NULL):
        """
        Draw the part of a parent control that is covered by a partially-transparent or alpha-blended child control.
        """
        if rect is not None: rect = rect.ref()
        hr = DrawThemeParentBackground(self, dc, rect)
        if FAILED(hr): raise COMError(hr)
        
    @property
    def band(self) -> int:
        band = DWORD()
        if not GetWindowBand(self, byref(band)):
            raise WinException()
        return band.value
    
    @classmethod
    def find(cls, name: str = NULL, class_name: str = NULL, 
             parent: int | HANDLE = NULL, after: int | HANDLE = NULL) -> 'Window':
        """
        Find window.
        """
        return Window.foreign(FindWindowExW(parent, after, class_name, name))

    def enum_props(self, callback: Callable[[str, int], bool], parameter: int=0) -> bool:
        """
        Enumerate properties of a window.
        """
        @PROPENUMPROCEXW
        def callback_thunk(hwndUnused: int, lpwszProp: LPCWSTR, hData: int, lParam: int) -> bool:
            pvProp = PtrUtil.get_address(lpwszProp)
            if pvProp <= MAXWORD:
                prop = Atom.foreign_owner(pvProp, pvProp < 0xC000).name
            else:
                prop = lpwszProp.value
            return callback(prop, hData, lParam)
        
        iResult = EnumPropsExW(self, callback_thunk, PtrUtil.get_address(parameter))
        
        return iResult != -1
    
    def get(self, command: int) -> 'Window':
        """
        Get window by command, which is related with instance window.
        """
        return Window.foreign(GetWindow(self, command))
    
    @classmethod
    def enum_windows(cls, callback: Callable[['Window', int], bool], parameter: int = 0) -> bool:
        """
        Enumerate all top-level windows.
        """
        @WNDENUMPROC
        def callback_thunk(hwnd: int, lParam: int) -> bool:
            return callback(Window.foreign(hwnd), lParam)
        
        SetLastError(0)
        iResult = EnumWindows(callback_thunk, parameter)
        dwError = GetLastError()
        
        if not iResult and dwError != 0: 
            raise WinException(dwError)
        
        return iResult != 0
    
    def top(self) -> 'Window':
        """
        Get top window.
        """
        return Window.foreign(GetTopWindow(self))
    
    def enum_child_windows(self, callback: Callable[['Window', int], bool], parameter: WT_ADDRLIKE = 0):
        """
        Enumerate child windows of window.
        """
        parameter = PtrUtil.get_address(parameter)
        @WNDENUMPROC
        def thunk(hwnd, lParam):
            return callback(Window.foreign(hwnd), lParam)
        EnumChildWindows(self, thunk, parameter)
    
    @property
    def children(self) -> Children:
        result = []
        def enum(window: 'Window', _) -> bool:
            parent = window.parent
            if parent is not None:
                parent = parent.value
            if parent == self.value:
                result.append(window)
            return True
        self.enum_child_windows(enum)
        return self.Children(self, result)
    
    @property
    def descendants(self) -> list['Window']:
        result = []
        def enum(window: 'Window', _) -> bool:
            result.append(window)
            return True
        self.enum_child_windows(enum)
        return result
    
    def item(self, identifier: int) -> 'Window':
        """
        Get item in window/dialog by identifier.
        """
        return Window.foreign(GetDlgItem(self, identifier))
    
    @property
    def identifier(self) -> int:
        return GetDlgCtrlID(self)
    
    def get_menu_bar_info(self, object_id: int = OBJID_MENU, identifier: int = 0) -> MENUBARINFO:
        """
        Get the menu bar info.
        """
        mbi = MENUBARINFO()
        mbi.cbSize = mbi.size()
        if not GetMenuBarInfo(self, object_id, identifier, mbi.ref()):
            raise WinException()
        return mbi
    
    @property
    def thread_id(self) -> int:
        thread_id = GetWindowThreadProcessId(self, NULL)
        if not thread_id: raise WinException()
        return thread_id
    
    @property
    def process_id(self) -> int:
        process_id = DWORD()
        _ = GetWindowThreadProcessId(self, byref(process_id))
        if not _: raise WinException()
        return process_id.value
    
    @property
    def zoomed(self) -> bool:
        return IsZoomed(self) != FALSE
    
    @property
    def maximized(self) -> bool:
        return IsZoomed(self) != FALSE
    
    @property
    def iconic(self) -> bool:
        return IsIconic(self) != FALSE
    
    @property
    def minimized(self) -> bool:
        return IsIconic(self) != FALSE
    
    @property
    def frozen(self) -> bool:
        return IsHungAppWindow(self) != FALSE
        
    @property
    def text(self) -> str:
        i = self.send(WM_GETTEXTLENGTH)
        p = create_unicode_buffer(i)
        self.send(WM_GETTEXT, i+1, p)
        return p.value
    
    @text.setter
    def text(self, text: str):
        self.send(WM_SETTEXT, 0, text)
        
    @classmethod
    def shell(cls) -> Self:
        """
        Get the Shell window.
        """
        return cls.foreign(GetShellWindow())
    
    @property
    def aumid(self) -> str | None:
        # get the Shell32 Property store for window
        pStore = IPropertyStore.NULL()
        hr = SHGetPropertyStoreForWindow(self, IPropertyStore.iid(), byref(pStore))
        if FAILED(hr): return None # no AUMID
        
        # initialize AUMID propvariant
        prop = PROPVARIANT()
        
        # get the AUMID value by its PKEY
        hr = pStore.contents.GetValue(PKEY_AppUserModel_ID, prop.ref())
        pStore.contents.Release() # release the property store
        if FAILED(hr): return None # no AUMID
        
        # if prop vartype is VT_LPWSTR and AUMID is set
        if prop.vt == VT_LPWSTR and prop.pwszVal:
            aumid = prop.pwszVal.value # return it
        else: # otherwise window don't have AUMID
            aumid = None
        # clear the propvariant
        PropVariantClear(prop.ref())
        return aumid # return the AUMID or None
    
    @aumid.setter
    def aumid(self, aumid: str):
        # get the Shell32 property store for window
        pStore = IPropertyStore.NULL()
        hr = SHGetPropertyStoreForWindow(self, IPropertyStore.iid(), byref(pStore))
        if FAILED(hr): raise COMError(hr)
        
        # allocate AUMID name buffer
        pAumid = create_unicode_buffer(aumid)
        # initialize propvariant with AUMID value
        prop = PROPVARIANT()
        prop.vt = VT_LPWSTR
        prop.pwszVal = i_cast(pAumid, LPWSTR)
        
        # try to set the AUMID of the window by its PKEY
        hr = pStore.contents.SetValue(PKEY_AppUserModel_ID, prop)
        if FAILED(hr): # if failed HR, then raise error
            pStore.contents.Release() # release the propstore
            raise COMError(hr)
        # commit the changes into property store
        hr = pStore.contents.Commit()
        pStore.contents.Release() # release the propstore
        if FAILED(hr): # if failed, then raise error
            raise COMError(hr)
        # otherwise we are successfully set the AUMID
    
    def get_window_theme(self) -> Theme | None:
        """
        Get the window theme (Theme handle).
        """
        return Theme.foreign_owner(GetWindowTheme(self))
    
    def set_window_theme(self, app_name: str | None = None, id_list: str | None = None):
        """
        Set the window theme by application name and ID list.
        """
        hr = SetWindowTheme(self, app_name, id_list)
        if FAILED(hr): raise COMError(hr)
    
class Mouse:
    @staticmethod
    def track(window: int | HANDLE, flags: int = TME_LEAVE, hover_time: int = 0):
        """
        Track the mouse events.
        """
        tme = TRACKMOUSEEVENT()
        tme.cbSize = tme.size()
        tme.dwFlags = flags
        tme.dwHoverTime = hover_time
        tme.hwndTrack = window
        if not TrackMouseEvent(tme.ref()):
            raise WinException()

class MDIMenu(Menu):
    """
    Menu instance for MDI frames.
    """
    
    window: Window
    
    def initialize_from_foreign(self, window: int | HANDLE):
        if not isinstance(window, Window):
            window = Window.foreign(window)
        self.window = window
    
    @classmethod
    def create(cls, window: int | HWND):
        menu = super().create()
        if not isinstance(window, Window):
            window = Window.foreign(window)
        menu.window = window
        return menu
    
    def refresh(self):
        """
        Refresh MDI Menu.
        """
        self.window.send(WM_MDIREFRESHMENU)
        if not DrawMenuBar(self.window):
            raise WinException()

class MDIWindow(Window):
    """
    Window instance for MDI Frames.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'headless' not in kwargs:
            self.client = MDIClientWindow()
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL,
               identifier: int | HMENU = NULL):
        super().create(width, height, x, y, window_name, parent, identifier)
    
    def default_window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return DefFrameProcW(hwnd, self.client, msg, wParam, lParam)

# MDI child ID base for CLIENTCREATESTRUCT
MDI_CHILDID_BASE = 0x8080

class MDIClientWindow(Window):
    """
    Window for MDI Client class.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'headless' not in kwargs:
            self.class_name = 'MDIClient'
            self.styles.add_ex(WS_EX_CLIENTEDGE)
            self.styles.remove(WS_OVERLAPPEDWINDOW)
            self.styles.add(WS_VISIBLE, WS_CHILD)
            self.on_mdi_activate = MultiEvent()
            self.on_mdi_destroy = MultiEvent()
            self.on_mdi_cascade = MultiEvent()
            self.on_mdi_tile = MultiEvent()
            self.on_mdi_create = MultiEvent()
            self.on_mdi_restore = MultiEvent()
            self.on_mdi_arrange = MultiEvent()
            self.on_mdi_maximize = MultiEvent()
            self.on_mdi_set_menu = MultiEvent()
            self.on_unknown_message += self.mdi_message_procedure
            
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL,
               menu: int | HMENU = NULL):
        ccs = CLIENTCREATESTRUCT()
        ccs.hWindowMenu = menu
        ccs.idFirstChild = MDI_CHILDID_BASE
        super().create(width, height, x, y, window_name, parent, parameter=ccs.ref())
        self.subclass()
        
    def cascade(self, behavior: int = 0):
        """
        Cascade all MDI children by specified behavior.
        """
        self.send(WM_MDICASCADE, behavior)
        
    def tile(self, tiling: int):
        """
        Tile all MDI children by specified tiling.
        """
        self.send(WM_MDITILE, tiling)
    
    def arrange(self):
        """
        Arrange all MDI children.
        """
        self.send(WM_MDIICONARRANGE)
    
    @property
    def active(self) -> 'MDIChildWindow':
        return MDIChildWindow.foreign(self.send(WM_MDIGETACTIVE))
    
    @property
    def menu(self) -> 'MDIMenu':
        hMenu = GetMenu(self)
        return MDIMenu.foreign_owner(hMenu, self)
    
    @menu.setter
    def menu(self, menu: int | HANDLE):
        self.send(WM_MDISETMENU, menu)
        if not DrawMenuBar(self):
            raise WinException()
        
    def set_window_menu(self, window_menu: int | HANDLE):
        """
        Set MDI frame window menu.
        """
        self.send(WM_MDISETMENU, 0, window_menu)
        if not DrawMenuBar(self):
            raise WinException()
        
    window_menu = property(fset=set_window_menu)
    
    def window_subclass_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if msg in (WM_MDIACTIVATE, WM_MDIDESTROY, WM_MDICASCADE, WM_MDITILE,
                   WM_MDICREATE, WM_MDIRESTORE, WM_MDIICONARRANGE, WM_MDIMAXIMIZE,
                   WM_MDISETMENU): return self.window_proc(hwnd, msg, wParam, lParam)
        return None
    
    def mdi_message_procedure(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if msg == WM_MDIACTIVATE:
            self.on_mdi_activate.execute(MDIChildWindow.foreign(wParam))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDIDESTROY:
            self.on_mdi_destroy.execute(MDIChildWindow.foreign(wParam))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDICASCADE:
            self.on_mdi_cascade.execute(wParam)
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDITILE:
            self.on_mdi_tile.execute(wParam)
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDICREATE:
            self.on_mdi_create.execute(i_cast_value(lParam, MDICREATESTRUCTW))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDIRESTORE:
            self.on_mdi_restore.execute(MDIChildWindow.foreign(wParam))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDIICONARRANGE:
            self.on_mdi_arrange.execute()
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDIMAXIMIZE:
            self.on_mdi_maximize.execute(MDIChildWindow.foreign(wParam))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        elif msg == WM_MDISETMENU:
            self.on_mdi_set_menu.execute(MDIMenu.foreign_owner(wParam, self), Menu.foreign_owner(lParam))
            return DefSubclassProc(hwnd, msg, wParam, lParam)
        return None

class MDIChildWindow(Window):
    """
    The MDI Child window.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        if 'headless' not in kwargs:
            self.extended_style |= WS_EX_MDICHILD
        
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL):
        if self.class_name is None:
            self.register()
        mdics = MDICREATESTRUCTW()
        mdics.hOwner = GetModuleHandleW(NULL)
        mdics.x = x
        mdics.y = y
        mdics.cx = width
        mdics.cy = height
        mdics.szClass = self.class_name
        mdics.szTitle = window_name
        self.value = SendMessageW(parent, WM_MDICREATE, 0, mdics.addressof())
        if not self.value:
            raise WinException()

    def close(self):
        self.parent.send(WM_MDIDESTROY, self.value)
        
    def destroy(self):
        self.close()
        
    def maximize(self):
        """
        Maximize the MDI child window.
        """
        self.parent.send(WM_MDIMAXIMIZE, self.value)
    
    def restore(self):
        """
        Restore the MDI child window.
        """
        self.parent.send(WM_MDIRESTORE, self)
        
    def default_window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return DefMDIChildProcW(hwnd, msg, wParam, lParam)

class AcceleratorTable(Handle):
    """
    The Win32 accelerator table.
    """
    
    entries: list[ACCEL]
    window: int | HANDLE
    
    @classmethod
    def create(cls, entries: list[ACCEL], window: int | HANDLE | None = None) -> 'AcceleratorTable':
        pEntries = (ACCEL * len(entries))(*entries)
        hAccel = CreateAcceleratorTableW(pEntries, len(entries))
        if not hAccel: raise WinException()
        table = AcceleratorTable(hAccel)
        table.window = window
        table.entries = entries
        return table
    
    def close(self):
        if not DestroyAcceleratorTable(self):
            raise WinException()
        self._closed = True

TLUX_PASS = 0
TLUX_STOP = 1
TLUX_RAISE = 2

class ThreadLoopUnit:
    """
    The thread loop unit class.
    """
    
    RUNNING_LOOPS: dict[int, Self] = {}
    ALL_LOOPS: dict[int, Self] = {}
    
    @classmethod
    def current(cls, running: bool = True) -> TUnion[Self, None]:
        loops = cls.RUNNING_LOOPS if running else cls.ALL_LOOPS
        return loops.get(GetCurrentThreadId(), None)
    
    @classmethod
    def identified(cls, thread_id: int, running: bool = True) -> TUnion[Self, None]:
        loops = cls.RUNNING_LOOPS if running else cls.ALL_LOOPS
        return loops.get(thread_id, None)
    
    after_message: MultiEvent
    on_destroy: MultiEvent
    on_message: MultiEvent
    
    block_timeout: int
    thread_id: int
    running: bool
    foreign: bool
    
    def __init__(self, thread_id: int | None = None):
        # thread loop events
        self.after_message = MultiEvent()
        self.on_destroy = MultiEvent()
        self.on_message = MultiEvent()
        
        # thread loop instance data
        self.running = False
        self.block_timeout = 10
        if thread_id is not None:
            self.thread_id = thread_id
            self.foreign = True
        else:
            self.thread_id = GetCurrentThreadId()
            self.foreign = False
        self.ALL_LOOPS[self.thread_id] = self
    
    def post(self, message: int, wParam: int, lParam: int):
        """
        Post the message into thread loop.
        """
        if isinstance(wParam, str):
            wParam = create_unicode_buffer(wParam)
        if isinstance(lParam, str):
            lParam = create_unicode_buffer(lParam)
        
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
            
        if not PostThreadMessageW(self.thread_id, message, wParam, lParam):
            raise WinException()
    
    def launch(self, window: int | HANDLE = NULL):
        """
        Launch the thread loop event cycle.
        """
        # check if window is foreign, when it is not allowed to "launch" its event loop
        if self.foreign:
            raise RuntimeError('Not allowed to run event cycle on foreign thread loop.')
        
        # set the MSG structure and running state
        self.running = True
        msg = MSG()
        pMsg = byref(msg)
        self.RUNNING_LOOPS[self.thread_id] = self
        
        while self.running:
            try:
                if PeekMessageW(pMsg, window, 0, 0, PM_REMOVE): # asynchronous PeekMessage
                    if msg.message == WM_QUIT:
                        self.running = False
                        break
                    
                    if self.on_dispatch_message(msg, pMsg): # if we can dispatch message, do it
                        TranslateMessage(pMsg)
                        self.on_message.execute(msg) # execute the application.on_message handler before dispatching
                        DispatchMessageW(pMsg)
                
                self.after_message.execute() # execute the application.after_message handler for after-message handling
                MsgWaitForMultipleObjects(0, NULL, FALSE, self.block_timeout, QS_ALLEVENTS) # block the event cycle for 10 ms while waiting new messages into queue
            except BaseException as exception:
                tlux = self.on_exception(exception)
                if tlux == TLUX_STOP:
                    self.running = False
                    break
                elif tlux == TLUX_RAISE:
                    raise exception from None
                elif tlux == TLUX_PASS:
                    continue
        
        del self.RUNNING_LOOPS[self.thread_id]
        self.on_destroy.execute() # execute the application.on_destroy because application event loop was destroyed

    def on_dispatch_message(self) -> bool:
        """
        The dispatch event callback.
        Return `False` if message should not be processed, otherwise `True`.
        """
        return True
    
    def on_exception(self, exception: BaseException) -> int:
        """
        The exception event callback.
        Return `TLUX_STOP` if loop must be stopped, `TLUX_PASS` if loop
        must be remain run state, otherwise return `TLUX_RAISE` for re-raise.
        """
        if isinstance(exception, KeyboardInterrupt):
            return TLUX_STOP
        return TLUX_RAISE

class WindowLoopUnit(ThreadLoopUnit):
    """
    The window loop unit class.
    """
    
    modeless_dialogs: list[int | HWND]
    accelerator_tables: list[AcceleratorTable]
    windows: int
    
    def __init__(self, thread_id: int | None = None):
        # call ThreadLoopUnit constructor
        super().__init__(thread_id)
        
        # window loop instance data
        self.modeless_dialogs = []
        self.accelerator_tables = []
        self.windows = 0
            
    def notify(self):
        """
        Notify the window loop about windows count changed.
        """
        if not self.windows:
            self.running = False
    
    def hook(self, hwnd: int | HWND, procedure: Callable[[MSG], None], message: int=None):
        """
        Hook the message (or all messages) from the providen window.
        """
        if isinstance(hwnd, HWND): hwnd = hwnd.value
        
        if message is not None:
            def on_message_handler(msg: MSG):
                if msg.message == message and msg.hWnd == hwnd:
                    procedure(msg)
        else:
            def on_message_handler(msg: MSG):
                if msg.hWnd == hwnd:
                    procedure(msg)
                    
        self.on_message += on_message_handler
        
    def on_dispatch_message(self, msg: MSG, pMsg: IPointer[MSG]) -> bool:
        dispatch = True
        # check if message processes through HACCELs list
        for accelerator_table in self.accelerator_tables:
            if accelerator_table.window is None:
                hwnd = msg.hWnd
            else:
                hwnd = accelerator_table.window
            if TranslateAcceleratorW(hwnd, accelerator_table, pMsg):
                dispatch = False
                break
        if dispatch:
            # check if message belongs to one of modeless dialogs
            for modeless_dialog in self.modeless_dialogs:
                if IsDialogMessage(modeless_dialog, pMsg):
                    dispatch = False # if true, don't dispatch the message into main cycle
                    break
        return dispatch

class Application(WindowLoopUnit):
    """
    Main application class. 
    """
    CURRENT: 'Application' = None
    
    def __new__(cls):
        if Application.CURRENT is None:
            return super().__new__(cls)
        return Application.CURRENT
    
    def __init__(self):
        if Application.CURRENT is None:
            # call super constructor
            super().__init__()
            # set application singleton
            Application.CURRENT = self
            # set process DPI-aware
            if not is_null(SetProcessDPIAware):
                SetProcessDPIAware()
    
class IdentifiersT:
    """
    Class specifically for generating new item identifiers by instance get-item access.
    
    E.g. Identifiers['Name'] => 0x800
    """
    
    _identifiers: dict[str, int]
    
    def __init__(self):
        self._identifiers = {}
    
    def __getitem__(self, identifier: str) -> int:
        identifier_id = self._identifiers.get(identifier, None)
        if identifier_id is None:
            identifier_id = Control.id()
            self._identifiers[identifier] = identifier_id
        return identifier_id
    
Controls = Identifiers = IdentifiersT()

class MessagesT:
    """
    Class specifically for generating new window messages by instance get-item access.
    
    E.g. Messages['Name'] => 0x4AB
    """
    
    _messages: dict[str, int]
    
    def __init__(self):
        self._messages = {}
    
    def __getitem__(self, message: str) -> int:
        message_id = self._messages.get(message, None)
        if message_id is None:
            buffer = create_string_buffer(message)
            message_id = RegisterWindowMessageW(buffer)
            if not message_id:
                raise WinException()
            self._messages[message] = message_id
        return message_id
    
Messages = MessagesT()

class AutoIncrementMap:
    """
    Class specifically for incrementally increasing from base by instance get-item access.
    
    E.g. AutoIncrementMap(0xFAFA)['Name'] => 0xFAFA
    """
    
    _map: dict[str, int]
    
    def __init__(self, start: int):
        self.start = start
        self._map = {}
    
    def __getitem__(self, name: str) -> int:
        value = self._map.get(name, None)
        if value is None:
            value = self.start
            self._map[name] = value
            self.start += 1
        return value
    
    def get(self) -> int:
        """
        Get the value and increase counter.
        """
        value = self.start
        self.start += 1
        return value
    
SubclassIdentifiers = AutoIncrementMap(0)

class ICacheAccessor(IInterface, Generic[WT]):
    @interface_abstract_method
    def cache(self, v: WT):
        pass

class AutoCacheMap(Generic[WT]):
    """
    Class for specifically key-value caching.
    """
    
    class Accessor(ICacheAccessor):
        _map: 'AutoCacheMap'
        _name: str
        def __init__(self, map: 'AutoCacheMap', name: str):
            self._map = map
            self._name = name
        def cache(self, v: Any):
            self._map[self._name] = v
    _map: dict[str, WT]
    
    def __init__(self):
        self._map = {}
        
    def __getitem__(self, k: str) -> WT | None:
        return self._map.get(k, None)
    
    def __setitem__(self, k: str, v: Any):
        self._map[k] = v
        
    def access(self, name: str) -> ICacheAccessor:
        return self.Accessor(self, name)

class Control(Window):
    """
    Class, representing the control (window, hosted and owned by another window).
    """
    
    _id_last: ClassVar[int] = 0x7ff
    
    def __init__(self, parent: int | HWND=None, identifier: int | HMENU=None, **kwargs):
        super().__init__()
        if 'headless' not in kwargs:
            self._style = WS_CHILD | WS_VISIBLE
            self._identifier = identifier
            self._parent = parent
            
            self.on_click = MultiEvent()
            self.on_right_click = MultiEvent()
            self.on_double_click = MultiEvent()
            self.on_right_double_click = MultiEvent()
            self.on_return = MultiEvent()
            self.on_nm_key_down = MultiEvent()
            self.on_capture_released = MultiEvent()
            self.on_nm_focus_changed = MultiEvent()
            self.on_nm_focus_lost = MultiEvent()
        
            # if parent is window and Abs-managed object, then subscribe on events
            if isinstance(parent, Window) and Abs.managed(parent):
                parent.on_command += self.parent_window_on_command
                parent.on_notify += self.parent_window_on_notify
     
    _identifier: int | HMENU
    _parent: int | HWND
    
    on_click: MultiEvent
    on_right_click: MultiEvent
    on_double_click: MultiEvent
    on_right_double_click: MultiEvent
    on_return: MultiEvent
    on_nm_key_down: MultiEvent
    on_capture_released: MultiEvent
    on_nm_focus_changed: MultiEvent
    on_nm_focus_lost: MultiEvent
    
    @staticmethod
    def id() -> int:
        """
        Generate the new control ID.
        """
        
        Control._id_last += 1
        return Control._id_last
    
    @property
    def visible(self):
        return self.style & WS_VISIBLE
    
    @visible.setter
    def visible(self, visible: bool):
        if visible:
            self.style |= WS_VISIBLE
        else:
            self.style &= ~WS_VISIBLE
    
    def create(self, width: int, height: int, x: int = 0, y: int = 0, window_name: str='Control', relative: int | HWND = NULL):
        """
        Create the control.
        """
        
        if relative is not NULL:
            rc = RECT()
            
            if not GetWindowRect(relative, byref(rc)):
                raise WinException()
            
            rcParent = RECT()
            
            if not GetWindowRect(self._parent, byref(rcParent)):
                raise WinException()
            
            x, y = rc.left + x - rcParent.left, rc.top + y - rcParent.top
            
        super().create(width, height, x, y, window_name, self._parent, self._identifier)

    def parent_window_on_command(self, identifier: int, notify_code: int, hwnd: int):
        pass
    
    def parent_window_on_notify(self, nm: NMHDR):
        if nm.hwndFrom == self.value:
            code = INT(nm.code).value
            if code == NM_CLICK:
                x, y = Cursor.position
                position = Point(x, y)
                self.to_client(position)
                
                self.on_click.execute(position.x, position.y)
            elif code == NM_RCLICK:
                x, y = Cursor.position
                position = Point(x, y)
                self.to_client(position)
                
                self.on_right_click.execute(position.x, position.y)
            elif code == NM_DBLCLK:
                x, y = Cursor.position
                position = Point(x, y)
                self.to_client(position)
                
                self.on_double_click.execute(position.x, position.y)
            elif code == NM_RDBLCLK:
                x, y = Cursor.position
                position = Point(x, y)
                self.to_client(position)
                
                self.on_right_double_click.execute(position.x, position.y)
            elif code == NM_RETURN:
                self.on_return.execute()
            elif code == NM_KEYDOWN:
                self.on_nm_key_down.execute(i_cast_structure(nm, NMKEY))
            elif code == NM_RELEASEDCAPTURE:
                self.on_capture_released.execute()
            elif code == NM_SETFOCUS:
                self.on_nm_focus_changed.execute()
            elif code == NM_KILLFOCUS:
                self.on_nm_focus_lost.execute()

    def notify_parent(self, nm: NMHDR) -> int:
        """
        Notify the parent of a control.
        """
        parent = self.parent
        if parent:
            parent.send(WM_NOTIFY, self.identifier, nm.addressof())

    def command_parent(self, code: int) -> int:
        """
        Send a command to the parent of a control.
        """
        parent = self.parent
        if parent:
            parent.send(WM_COMMAND, MAKEWPARAM(code, self.identifier), self.value)

class GLWindow(Window):
    """
    GL (1.1) Window.
    """
    
    pfd: PIXELFORMATDESCRIPTOR
    gl_context: GLContext
    
    def __init__(self):
        super().__init__()
        
        # styles
        self._style |= WS_CLIPCHILDREN | WS_CLIPSIBLINGS # for correct OpenGL visual state
        self.class_style = CS_OWNDC # for singleton DC for all window.
        
        # custom OpenGL window events
        self.gl_tick = MultiEvent()
        self.gl_ready = MultiEvent()
        
        # OpenGL window settings
        self.enable_after_message_render = True # by default, after-message rendering is ON
        self.manual_initialize = False # let you manually initialize the OpenGL context. by default it is OFF
        
        # OpenGL-specific window event subscribing
        ThreadLoopUnit.current(False).after_message += self.GL_after_message
        self.on_close += self.GL_close
        
        # setup the OpenGL pixel format
        self.pfd = PIXELFORMATDESCRIPTOR(
            sizeof(PIXELFORMATDESCRIPTOR),
            1,
            PFD_DRAW_TO_WINDOW |
            PFD_SUPPORT_OPENGL |
            PFD_DOUBLEBUFFER,
            PFD_TYPE_RGBA,
            32,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            24,
            8,
            0,
            PFD_MAIN_PLANE,
            0, 0, 0, 0
        )
    
    def disable_after_message_render(self):
        """
        Disable the after-message render, which is bound to application event cycle.
        """
        
        self.enable_after_message_render = False
        ThreadLoopUnit.current(False).after_message -= self.GL_after_message
    
    def GL_after_message(self):
        # standard after-message handler, execute OpenGL tick event and swap the buffers
        self.gl_tick.execute()
        SwapBuffers(self.dc)
        
    def GL_close(self):
        # OpenGL window closed, if enabled after-message render when unbind it from application
        if self.enable_after_message_render:
            ThreadLoopUnit.current(False).after_message -= self.GL_after_message
        return True
    
    def initialize_gl(self):
        """
        Initialize the OpenGL context on window.
        """
        
        # get the current DC for window
        self.dc = DC.get(self)
        
        # set the pixel format
        pPfd = self.pfd.ref()
        iPixelFormat = ChoosePixelFormat(self.dc, pPfd)
        SetPixelFormat(self.dc, iPixelFormat, pPfd)
        
        # create and set the OpenGL context
        self.gl_context = GLContext.current(self.dc)
        self.gl_ready.execute() # execute OpenGL ready event
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT, 
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT, 
               window_name: str = 'Window', parent = NULL):
        """
        Create the OpenGL window.
        """
        
        super().create(width, height, x, y, window_name, parent, NULL)
        if not self.manual_initialize:
            self.initialize_gl()

    def swap_buffers(self):
        """
        Swap the underlying and overlaying buffers.
        """
        if not SwapBuffers(self.dc): raise WinException()

# WGL context creation ARB extension function
PFNWGLCREATECONTEXTATTRIBSARB = APIENTRY(HGLRC, HDC, HGLRC, PINT)

#
# WGL context attributes
#

WGL_CONTEXT_MAJOR_VERSION_ARB = (0x2091)
WGL_CONTEXT_MINOR_VERSION_ARB = (0x2092)
WGL_CONTEXT_PROFILE_MASK_ARB = (0x9126)

WGL_CONTEXT_CORE_PROFILE_BIT_ARB = (0x00000001)
WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB = (0x00000002)

WGL_CONTEXT_FLAGS_ARB = (0x2094)

WGL_CONTEXT_DEBUG_BIT_ARB = (0x0001)
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB = (0x0002)

WGL_CONTEXT_LAYER_PLANE_ARB = (0x2093)

class ExtendedGLWindow(GLWindow):
    """
    Extended GL Window with modern OpenGL support.
    """
    
    wglCreateContextAttribsARB: Callable[[int, int, PINT], int]
    attributes: dict[int, int]
    
    def __init__(self):
        super().__init__()
        self.attributes = {}
        self.wglCreateContextAttribsARB = None
    
    def create_extended_context(self, attributes: dict[int, int]) -> GLContext:
        if not self.wglCreateContextAttribsARB:
            # setup the WGL create context ARB function for extended context functionality
            wglCreateContextAttribsARB = wglGetProcAddress(b'wglCreateContextAttribsARB')
            self.wglCreateContextAttribsARB = i_cast(wglCreateContextAttribsARB, PFNWGLCREATECONTEXTATTRIBSARB)
        
        # setup the OpenGL ARB attributes list
        attribs = [entry for pair in self.attributes.items() for entry in pair]
        attribList = (INT * (len(attribs) + 1))(*attribs, 0)
        
        # create modern OpenGL context
        hGLCtx = self.wglCreateContextAttribsARB(
            self.dc, NULL, attribList)
        if not hGLCtx:
            raise WinException()
        
        return GLContext.foreign_owner(hGLCtx).exchange_owner()
     
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT, 
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT, 
               window_name: str = 'Window', parent = NULL):
        # block the window.gl_ready event for silenting the execution (event is called by us in this function)
        self.gl_ready.block()
        super().create(width, height, x, y, window_name, parent)
        self.gl_ready.unblock() # unblock the window.gl_ready event so we can execute it
        
        # create the OpenGL extended context
        context = self.create_extended_context(self.attributes)
        context.set_current(self.dc)
        # set the OpenGL context and exchange current state owning to handle wrapper
        self.gl_context = context.owned_current(True)
        self.gl_ready.execute() # execute OpenGL ready event
        
    def version(self, major: int | str, minor: int = None):
        """
        Set the OpenGL version of window. 
        """
        
        # minor is provided as None, it is because string version was provided or minor 0 by default
        if minor is None:
            if isinstance(major, str):
                # split the string version into components
                components = major.split('.')[0:2] # truncate to 2 components
                # convert string components to major/minor pair
                major, minor = components
            else:
                # if no minor, it is 0 by default
                minor = 0
        
        # forcely convert major/minor to integers
        major = int(major)
        minor = int(minor)
        
        # set the WGL attributes of version
        self.attributes[WGL_CONTEXT_MAJOR_VERSION_ARB] = major
        self.attributes[WGL_CONTEXT_MINOR_VERSION_ARB] = minor
        
# Win Abstractions Layer code Ends
# # # # # # # # # # # # # # # # # # # #