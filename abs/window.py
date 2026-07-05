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

# COM HRESULTs
from win.com.comdefbase import HRESULT, COMError, FAILED

# random module for class name generation
import random

# WinAbs initialization procedure
def _abs_init():
    # initialize the INITCOMMONCONTROLSEX structure
    icex = INITCOMMONCONTROLSEX()
    icex.dwSize = sizeof(icex)
    icex.dwICC = ICC_WIN95_CLASSES

    # initialize the common controls (comctl32)
    if not InitCommonControlsEx(icex.ref()):
        raise WinException()

dwmapi = get_win_library('dwmapi.dll')

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

@user32.foreign(BOOL, HWND, LPWINDOWCOMPOSITIONATTRIBDATA)
def SetWindowCompositionAttribute(hwnd: int, pwcad: IPointer[WINDOWCOMPOSITIONATTRIBDATA]) -> int: pass

@dwmapi.foreign(HRESULT, HWND, DWORD, LPCVOID, DWORD)
def DwmSetWindowAttribute(hwnd: int, dwAttribute: int, pvAtribute: int, cbAttribute: int): pass

DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_USE_HOSTBACKDROPBRUSH = 17
DWMWA_SYSTEMBACKDROP_TYPE = 38
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

ACCENT_DISABLED = 0
ACCENT_ENABLE_GRADIENT = 1
ACCENT_ENABLE_TRANSPARENTGRADIENT = 2
ACCENT_ENABLE_BLURBEHIND = 3
ACCENT_ENABLE_SLOWMOVE = 4
ACCENT_STATE = INT

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

@kernel32.foreign(UINT, ATOM, LPWSTR, INT)
def GlobalGetAtomNameW(nAtom: int, lpBuffer: WT_LPWSTR, nSize: int) -> int: ...

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

class Menu(Handle):
    """
    Main window menu.
    """
    
    def close(self):
        DestroyMenu(self)
        self._closed = True
    
    def __init__(self, **kwargs):
        if 'headless' not in kwargs:
            super().__init__(CreateMenu())
            if not self.value:
                raise WinException()
        else:
            super().__init__()
    
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

class PopupMenu(Menu):
    """
    Popup menu class.
    """
    
    def __init__(self):
        super().__init__()
        self.value = CreatePopupMenu()
        if not self.value:
            raise WinException()
        
    def track(self, x: int, y: int, hWnd: int | HANDLE, flags: int=0):
        """
        Track the popup menu in given coordinates of window.
        """
        
        if not TrackPopupMenu(self, flags, x, y, 0, hWnd, NULL):
            raise WinException()

class Window(HWND, Abs.Object):
    """
    Class, wrapping functionality of Win32 Window.
    """
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
    
    _foreign_cache: dict[int, 'Window'] = {}
    
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
            window = cls(hwnd, headless=True)
            Window._foreign_cache[hwnd] = window
        return window
    
    styles: Styles
    
    def __init__(self, *args, **kwargs):
        HWND.__init__(self, *args)
        self.styles = self.Styles(self)
        
        # headless construct = construct `Window` object from HWND
        if 'headless' not in kwargs:
            Abs.Object.__init__(self)
            # fields for class registering
            self.class_name = None
            self.class_style = 0
            self.hbrBackground = (COLOR_WINDOW + 1)
            self.cursor = None
            self.icon = None
            
            # styles for window creation
            self._style = WS_OVERLAPPEDWINDOW
            self._extended_style = 0
            
            # timer callback cache
            self._timers = {}
            
            # events collection
            self.on_create = MultiEvent()
            self.on_left_button_down = MultiEvent()
            self.on_left_button_up = MultiEvent()
            self.on_left_button_double_click = MultiEvent()
            self.on_right_button_down = MultiEvent()
            self.on_right_button_up = MultiEvent()
            self.on_right_button_double_click = MultiEvent()
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
            self.after_message = MultiEvent()
            self.on_notify = MultiEvent()
            self.on_message = MultiEvent()
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
            
            # bind the standard handler for destroy: application cycle notifier
            self.on_nc_destroy += self.Window_on_nc_destroy
            
            # bind the standard handler for creation: application cycle notifier
            self.on_create += self.Window_on_create
    
    _timers: dict[int, FARPROC]
    class_name: str | None
    
    cursor: int | HANDLE | None
    icon: int | HANDLE | None
    
    def Window_on_nc_destroy(self):
        # notify the application cycle what one of application-hosted windows is destroyed
        app = Application()
        app.windows -= 1
        app.notify()
        
    def Window_on_create(self):
        app = Application()
        app.windows += 1 # add the application cycle windows count
        return True
    
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
    
    def enable(self):
        """
        Enable the window.
        """
        
        EnableWindow(self, True)
        
    def disable(self):
        """
        Disable the window.
        """
        
        EnableWindow(self, False)
    
    def register(self):
        """
        Register the window class.
        """
        
        wc = WNDCLASSW()
        
        # standard icon/cursor loading
        if self.icon is None:
            self.icon = Icon.load(IDI_APPLICATION)
        if self.cursor is None:
            self.cursor = Cursor.load(IDC_ARROW)
        
        # visual setting
        wc.hbrBackground = self.hbrBackground
        wc.hIcon = self.icon
        wc.hCursor = self.cursor
        wc.style = self.class_style
        
        # the base handle of executable module (commonly python.exe)
        wc.hInstance = GetModuleHandleW(NULL)
        
        # construct the random class name
        class_name = f'Win-Abs/Class-N{str(random.randint(0, 10000000)).zfill(8)}'
        wc.lpszClassName = class_name
        
        # install the class window procedure
        self.pfnWndProc = wc.lpfnWndProc = WNDPROC(self.window_proc)
        atomResult = RegisterClass(wc.ref())
        
        # check the registration result
        if not atomResult:
            raise WinException()
        
        self.class_name = class_name
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL,
               identifier: int | HMENU = NULL):
        """
        Create the window.
        """
        
        if self.class_name is None:
            self.register()
        self.value = CreateWindowExW(self._extended_style, self.class_name, window_name, self._style, 
                                     x, y, width, height, parent, identifier, GetModuleHandle(NULL), NULL)
        if not self.value:
            raise WinException()
        
        Window._foreign_cache[self.value] = self
    
    def on_paint(self, dc: PaintDC):
        pass
    
    def on_size(self, flags: int, width: int, height: int):
        pass
    
    def on_erase_background(self, dc: DC) -> bool:
        return False
    
    def on_focus_changed(self, previous: 'Window'):
        pass
    
    def on_focus_lost(self, focused: 'Window'):
        pass
    
    def on_set_cursor(self, hwnd: int, ht: int, message: int) -> bool:
        return None
    
    def on_nc_paint(self, dc: DC, region: Region):
        return self # sentinel value
    
    def on_nc_hittest(self, x: int, y: int) -> int:
        return None
    
    def on_nc_calcsize(self, rect: RECT, rectangles: list=None, position: WINDOWPOS=None) -> int:
        return self # sentinel value
    
    # ** Main window procedure ** #
    def window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        if msg == WM_CREATE: # window created
            self.value = hwnd
            if not all(self.on_create.execute()): # check the all window.on_create returned True
                return -1
            return 0
        elif msg == WM_PAINT: # window paint request
            with PaintDC(self) as dc: # begin the paint and return dc into handler
                self.on_paint(dc) # execute handler
            return 0
        elif msg == WM_LBUTTONDOWN: # left mouse button down
            self.on_left_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_LBUTTONUP: # left mouse button up
            self.on_left_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_LBUTTONDBLCLK: # left mouse button double-clicked
            self.on_left_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_RBUTTONDOWN: # right mouse button down
            self.on_right_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_RBUTTONUP: # right mouse button up
            self.on_right_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_RBUTTONDBLCLK: # right mouse button double-clicked
            self.on_right_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_CLOSE: # window closed
            if all(self.on_close.execute()):
                self.destroy()
            return 0
        elif msg == WM_DESTROY: # window destroyed
            self.on_destroy.execute()
            return 0
        elif msg == WM_COMMAND: # command send from child to window
            self.on_command.execute(LOWORD(wParam), HIWORD(wParam), lParam)
            return 0
        elif msg == WM_SIZE: # window sized
            self.on_size(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_KEYDOWN: # key down
            wVK = LOWORD(wParam) # virtual key code
            fKeyFlags = HIWORD(lParam) # key flags
            wScanCode = LOBYTE(fKeyFlags) # scan code
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED: # if extended scan code
                wScanCode = MAKEWORD(wScanCode, 0xE0) # when manually extend
            self.on_key_down.execute(wVK, fKeyFlags, wScanCode) # execute handler
            return 0
        elif msg == WM_KEYUP: # key up
            wVK = LOWORD(wParam) # virtual key code
            fKeyFlags = HIWORD(lParam) # key flags
            wScanCode = LOBYTE(fKeyFlags) # scan code
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED: # if extended scan code
                wScanCode = MAKEWORD(wScanCode, 0xE0) # when manually extend
            self.on_key_up.execute(wVK, fKeyFlags, wScanCode) # execute handler
            return 0
        elif msg == WM_MOVE: # window moved
            self.on_move.execute(LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_SHOWWINDOW: # window showed
            self.on_show.execute(wParam == TRUE, lParam)
            return 0
        elif msg == WM_STYLECHANGED: # window styles changed
            self.on_style_changed.execute(i_cast(lParam, LPSTYLESTRUCT).contents, wParam == GWL_EXSTYLE)
            return 0
        elif msg == WM_THEMECHANGED: # window theme changed
            self.on_theme_changed.execute()
            return 0
        elif msg == WM_USERCHANGED: # user changed in system
            self.on_user_changed.execute()
            return 0
        elif msg == WM_ENABLE: # window enabled
            self.on_enable.execute(wParam == TRUE)
            return 0
        elif msg == WM_ERASEBKGND: # erase background request
            dc = DC.foreign_owner(wParam) # pack the hDC into DC wrapper
            if self.on_erase_background(dc): # the background was erased
                return TRUE
            return FALSE # the background wasn't erased
        elif msg == WM_SETFONT: # set window font request
            self.on_set_font.execute(Font.foreign_owner(wParam), LOWORD(lParam) == TRUE)
            return 0
        elif msg == WM_MOUSEWHEEL:
            self.on_mouse_wheel.execute(SHORT(HIWORD(wParam)).value, LOWORD(wParam), LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_TIMER: # timer message
            self.on_timer.execute(wParam, i_cast(lParam, TIMERPROC))
            return 0
        elif msg == WM_NOTIFY: # notify message from child control
            nmhdr = i_cast(lParam, LPNMHDR).contents
            self.on_notify.execute(nmhdr)
            return 0
        elif msg == WM_MOUSEMOVE: # mouse moved
            self.on_mouse_move.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_DRAWITEM: # draw the item (by style *_OWNERDRAW)
            if not self.on_draw_item.empty(): # if has draw item handlers
                self.on_draw_item.execute(wParam, i_cast_value(lParam, DRAWITEMSTRUCT))
                return TRUE # WM_DRAWITEM handled
            return FALSE # not handled
        elif msg == WM_SETFOCUS: # the window got focus
            self.on_focus_changed(Window.foreign(wParam)) # pack the previous focus window into Window and execute event
            return 0
        elif msg == WM_KILLFOCUS: # the window lost focus
            self.on_focus_lost(Window.foreign(wParam)) # pack the new focus window into Window and execute event
            return 0
        elif msg == WM_PALETTECHANGED: # window palette changed
            self.on_palette_changed.execute(Palette.foreign_owner(wParam))
            return 0
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
        elif msg == WM_CHAR:
            self.on_char.execute(chr(wParam))
            return FALSE
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
                with DC.get(self) as dc:
                    result = self.on_nc_paint(dc, None)
            else:
                with DC.get(self, region, DCX_WINDOW | DCX_INTERSECTRGN | DCX_CACHE) as dc: # call GetDCEx
                    result = self.on_nc_paint(dc, region) # call handler
            # if sentinel value matches, we are falling back to default procedure
            if result is not self:
                return 0 # otherwise we are handled the message
        elif msg == WM_NCHITTEST: # non-client area hit test message
            result = self.on_nc_hittest(LOWORD(wParam), HIWORD(wParam)) # call message handler
            if result is not None: return result # if message is handled, when return hit test result
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
        else:
            # unknown window message received
            result = self.on_unknown_message.execute(hwnd, msg, wParam, lParam) # trying to call all unknown message handlers
            for value in result: # iterate through returned values tuple
                if value is not None: # if value != None, when handler is handled our message
                    return value # return handler value as procedure LRESULT
        
        return self.default_window_proc(hwnd, msg, wParam, lParam) # otherwise let procedure fallback into defined fallback procedure (commonly DefWindowProc)
    
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
    
    def timer(self, function: Callable, elapse: int, event_id: int = 0) -> int:
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
        
    def hide(self):
        """
        Hide the window.
        """
        
        ShowWindowAsync(self, SW_HIDE)
    
    def show(self, nCmdShow: int = SW_SHOW):
        """
        Show the window.
        """
        
        ShowWindowAsync(self, nCmdShow)
        
    def set_font(self, font: int | HANDLE, redraw: bool = True):
        """
        Set the window font.
        """
        
        self.post(WM_SETFONT, font, redraw)
        
    @property
    def font(self) -> Font:
        return Font.foreign_owner(self.send(WM_GETFONT))
    
    @font.setter
    def font(self, font: int | HANDLE):
        self.set_font(font)
    
    def is_child(self, hWnd: int | HANDLE) -> bool:
        """
        Check another window is a child of window.
        """
        
        return bool(IsChild(self, hWnd))
    
    def is_child_of(self, hWnd: int | HANDLE) -> bool:
        """
        Check is window child of another window.
        """
        
        return bool(IsChild(hWnd, self))
    
    def send(self, message: int, wParam: int = 0, lParam: int = 0) -> int:
        """
        Send the message to window.
        """
        
        if isinstance(wParam, str):
            wParam = create_unicode_buffer(wParam)
        
        if isinstance(lParam, str):
            lParam = create_unicode_buffer(lParam)
        
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
            
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
            
        return SendMessage(self, message, wParam, lParam)
    
    def post(self, message: int, wParam: int = 0, lParam: int = 0):
        """
        Post the message to window (asynchronous send).
        """
        
        if isinstance(wParam, str):
            wParam = create_unicode_buffer(wParam)
        
        if isinstance(lParam, str):
            lParam = create_unicode_buffer(lParam)
        
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
            
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
            
        PostMessage(self, message, wParam, lParam)
 
    def map(self, window: int | HWND, points: Iterable[GraphicUtils.Point]) -> tuple[POINT, ...]:
        """
        Map the given points of window to an another window.
        """
        
        pointsToMap = [GraphicUtils.point(point) for point in points]
        length = len(points)
        pPoints = (POINT * length)(*pointsToMap)
        MapWindowPoints(self, window, pPoints, length)
        return tuple(pPoints)
    
    @property
    def menu(self) -> 'Menu':
        hMenu = GetMenu(self)
        if not hMenu: raise WinException()
        return Menu.foreign_owner(hMenu)
    
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
        
        hwnd = GetForegroundWindow()
        return Window.foreign(hwnd)
    
    @classmethod
    def desktop(self) -> 'Window':
        """
        Get the desktop window.
        """
        
        hwnd = GetDesktopWindow()
        return Window.foreign(hwnd)
    
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
        return IsWindow(self)
    
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
            if GetLastError() != 0: raise WinException()
        return result
    
    def set_long(self, index: int, value: int):
        """
        Set window long value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        if not SetWindowLongW(self, index, value):
            if GetLastError() != 0: raise WinException()
    
    def get_long_ptr(self, index: int) -> int:
        """
        Get window long pointer value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        result = GetWindowLongPtrW(self, index)
        if not result: 
            if GetLastError() != 0: raise WinException()
        return result
    
    def set_long_ptr(self, index: int, value: int):
        """
        Set window long pointer value.
        """
        index = PtrUtil.get_address(index)
        SetLastError(0)
        if not SetWindowLongPtrW(self, index, value):
            if GetLastError() != 0: raise WinException()
            
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
        self.parent.tile_windows(how, [self], rect)
        
    def get_prop(self, prop: str | int) -> int:
        """
        Get the property value in window property list.
        """
        if isinstance(prop, str):
            prop = create_unicode_buffer(prop)
        prop = i_cast(PtrUtil.get_address(prop), LPCWSTR)
        return GetPropW(self, prop)
        
    def set_prop(self, prop: str | int, data: int):
        """
        Set the property value in window property list.
        """
        if isinstance(prop, str):
            prop = create_unicode_buffer(prop)
        prop = i_cast(PtrUtil.get_address(prop), LPCWSTR)
        data = PtrUtil.get_address(data)
        if not SetPropW(self, prop, data):
            raise WinException()
        
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
        def callback_thunk(hwndUnused: int, lpwszProp: LPCWSTR, hData: int, lParam: int) -> bool:
            pvProp = PtrUtil.get_address(lpwszProp)
            if pvProp < 65536:
                buffer = create_unicode_buffer(256)
                GlobalGetAtomNameW(pvProp, buffer, 256)
                prop = buffer.value
            else:
                prop = lpwszProp.value
            return callback(prop, hData, lParam)
        
        pfnEnumProc = PROPENUMPROCEXW(callback_thunk)
        iResult = EnumPropsExW(self, pfnEnumProc, PtrUtil.get_address(parameter))
        
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
        def callback_thunk(hwnd: int, lParam: int) -> bool:
            return callback(Window.foreign(hwnd), lParam)
        
        pfnEnumProc = WNDENUMPROC(callback_thunk)
        SetLastError(0)
        iResult = EnumWindows(pfnEnumProc, parameter)
        dwError = GetLastError()
        
        if not iResult and dwError != 0: 
            raise WinException(dwError)
        
        return iResult != 0
    
    def top(self) -> 'Window':
        """
        Get top window.
        """
        return Window.foreign(GetTopWindow(self))
    
class Application:
    """
    Main application class. 
    """
    
    INSTANCE: 'Application' = None
    
    modeless_dialogs: list[int | HWND]
    windows: int
    
    def __new__(cls):
        if Application.INSTANCE is None:
            return super().__new__(cls)
            
        return Application.INSTANCE
    
    def __init__(self):
        if Application.INSTANCE is None:
            # application events
            self.after_message = MultiEvent()
            self.on_destroy = MultiEvent()
            self.on_message = MultiEvent()
            
            # application instance data
            self.modeless_dialogs = []
            self.running = False
            self.windows = 0
            
            # set application singleton
            Application.INSTANCE = self
            
    def notify(self):
        """
        Notify the application about windows count changed.
        """
        
        if not self.windows:
            self.running = False
    
    def launch(self):
        """
        Launch the application event cycle.
        """
        
        # set the MSG structure and running state
        self.running = True
        msg = MSG()
        pMsg = byref(msg)
        
        while self.running:
            try:
                if PeekMessage(pMsg, NULL, 0, 0, PM_REMOVE): # asynchronous PeekMessage
                    dispatch = True
                    # check if window belongs to one of modeless dialogs
                    for modeless_dialog in self.modeless_dialogs:
                        if IsDialogMessage(modeless_dialog, pMsg):
                            dispatch = False # if true, don't dispatch the message into main cycle
                            break
                    if dispatch: # if we can dispatch message, do it
                        TranslateMessage(pMsg)
                        self.on_message.execute(msg) # execute the application.on_message handler before dispatching
                        DispatchMessageW(pMsg)
                
                self.after_message.execute() # execute the application.after_message handler for after-message handling
                MsgWaitForMultipleObjects(0, NULL, FALSE, 10, QS_ALLEVENTS) # block the event cycle for 10 ms while waiting new messages into queue
            except KeyboardInterrupt:
                break
        
        self.on_destroy.execute() # execute the application.on_destroy because application event loop was destroyed
    
    def hook(self, hwnd: int | HANDLE, procedure: Callable[[MSG], None], message: int=None):
        if isinstance(hwnd, HANDLE): hwnd = hwnd.value
        
        if message is not None:
            def on_message_handler(msg: MSG):
                if msg.message == message and msg.hWnd == hwnd:
                    procedure(msg)
        else:
            def on_message_handler(msg: MSG):
                if msg.hWnd == hwnd:
                    procedure(msg)
                    
        self.on_message += on_message_handler
    
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

class Control(Window):
    """
    Class, representing the control (window, hosted and owned by another window).
    """
    
    _id_last: ClassVar[int] = 0x7ff
    
    def __init__(self, parent: int | HWND, identifier: int | HMENU):
        super().__init__()
        self._style = WS_CHILD | WS_VISIBLE
        self._identifier = identifier
        self._parent = parent
     
    _identifier: int | HMENU
    _parent: int | HWND
    
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
        Application().after_message += self.GL_after_message
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
        Application().after_message -= self.GL_after_message
    
    def GL_after_message(self):
        # standard after-message handler, execute OpenGL tick event and swap the buffers
        self.gl_tick.execute()
        SwapBuffers(self.dc)
        
    def GL_close(self):
        # OpenGL window closed, if enabled after-message render when unbind it from application
        if self.enable_after_message_render:
            Application().after_message -= self.GL_after_message
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
        
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT, 
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT, 
               window_name: str = 'Window', parent = NULL):
        # block the window.gl_ready event for silenting the execution (event is called by us in this function)
        self.gl_ready.block()
        super().create(width, height, x, y, window_name, parent)
        self.gl_ready.unblock() # unblock the window.gl_ready event so we can execute it
        
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
        
        # set the OpenGL context and exchange current state owning to handle wrapper
        self.gl_context = GLContext.current_external(self.dc, hGLCtx).owned_current(True)
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
        
_abs_init()