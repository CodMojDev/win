from win.defbase_errordef import *
from win.libloaderapi import *
from win.commctrl import *
from .core.handle import *
from .core.event import *

class Window(HWND):
    _class_count: int = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        
        if 'headless' not in kwargs:
            self._extended_style = 0
            self.class_name = None
            self._style = WS_OVERLAPPEDWINDOW
            self._timers = {}
            self.hbrBackground = (COLOR_WINDOW + 1)
            self.cursor = None
            self.icon = None
            self.class_style = 0
            self.running = False
            
            self.on_create = Event()
            self.on_paint = Event()
            self.on_left_button_down = Event()
            self.on_left_button_up = Event()
            self.on_left_button_double_click = Event()
            self.on_right_button_down = Event()
            self.on_right_button_up = Event()
            self.on_right_button_double_click = Event()
            self.on_close = Event()
            self.on_destroy = Event()
            self.on_command = Event()
            self.on_size = Event()
            self.on_key_down = Event()
            self.on_key_up = Event()
            self.on_move = Event()
            self.on_show = Event()
            self.on_style_changed = Event()
            self.on_theme_changed = Event()
            self.on_user_changed = Event()
            self.on_unknown_message = Event()
            self.on_enable = Event()
            self.on_erase_background = Event()
            self.on_set_font = Event()
            self.on_mouse_wheel = Event()
            self.on_timer = Event()
            self.after_message = Event()
    
    _timers: dict[int, FARPROC]
    class_name: str | None
    
    cursor: int | HANDLE | None
    icon: int | HANDLE | None
    
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
            return self._style
        return GetWindowLongW(self, GWL_EXSTYLE)
    
    @style.setter
    def extended_style(self, extended_style: int):
        self._extended_style = extended_style
        if self.value:
            SetWindowLongW(self, GWL_EXSTYLE, extended_style)
    
    def register(self):
        wc = WNDCLASSW()
        
        wc.hbrBackground = self.hbrBackground
        if self.icon is None:
            self.icon = LoadIconW(NULL, i_cast(IDI_APPLICATION, LPWSTR))
        if self.cursor is None:
            self.cursor = LoadCursorW(NULL, i_cast(IDC_ARROW, LPWSTR))
        wc.hIcon = self.icon
        wc.hCursor = self.cursor
        wc.hInstance = GetModuleHandleW(NULL)
        wc.style = self.class_style
        
        class_name = f'Win-Abs/Class-N{str(Window._class_count).zfill(4)}'
        
        wc.lpszClassName = class_name
        self.pfsnWndProc = wc.lpfnWndProc = WNDPROC(self.window_proc)
        atomResult = RegisterClass(wc.ref())
        
        if not atomResult:
            raise WinException()
        
        self.class_name = class_name
        Window._class_count += 1
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT,
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT,
               window_name: str = 'Window', parent: int | HWND = NULL,
               identifier: int | HMENU = NULL):
        if self.class_name is None:
            self.register()
        self.value = CreateWindowExW(self._extended_style, self.class_name, window_name, self._style, 
                                     x, y, width, height, parent, identifier, GetModuleHandle(NULL), NULL)
        if not self.value:
            raise WinException()
    
    def window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        if msg == WM_CREATE:
            self.running = True
            self.value = hwnd
            self.on_create.execute()
        elif msg == WM_PAINT:
            with PaintDC(self) as dc:
                self.on_paint.execute(dc)
        elif msg == WM_LBUTTONDOWN:
            self.on_left_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_LBUTTONUP:
            self.on_left_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_LBUTTONDBLCLK:
            self.on_left_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_RBUTTONDOWN:
            self.on_right_button_down.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_RBUTTONUP:
            self.on_right_button_up.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_RBUTTONDBLCLK:
            self.on_right_button_double_click.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_CLOSE:
            if all(self.on_close.execute(hwnd)):
                SendMessage(hwnd, WM_DESTROY, 0, 0)
        elif msg == WM_DESTROY:
            self.on_destroy.execute(hwnd)
            self.running = False
            PostQuitMessage(0)
        elif msg == WM_COMMAND:
            self.on_command.execute(LOWORD(wParam), HIWORD(wParam), lParam)
        elif msg == WM_SIZE:
            self.on_size.execute(wParam, LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_KEYDOWN:
            wVK = LOWORD(wParam)
            fKeyFlags = HIWORD(lParam)
            wScanCode = LOBYTE(fKeyFlags)
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED:
                wScanCode = MAKEWORD(wScanCode, 0xE0)
            self.on_key_down.execute(wVK, fKeyFlags, wScanCode)
        elif msg == WM_KEYUP:
            wVK = LOWORD(wParam)
            fKeyFlags = HIWORD(lParam)
            wScanCode = LOBYTE(fKeyFlags)
            if (fKeyFlags & KF_EXTENDED) == KF_EXTENDED:
                wScanCode = MAKEWORD(wScanCode, 0xE0)
            self.on_key_up.execute(wVK, fKeyFlags, wScanCode)
        elif msg == WM_MOVE:
            self.on_move.execute(LOWORD(lParam), HIWORD(lParam))
        elif msg == WM_SHOWWINDOW:
            self.on_show.execute(wParam == TRUE, lParam)
        elif msg == WM_STYLECHANGED:
            self.on_style_changed.execute(i_cast(lParam, LPSTYLESTRUCT).contents, wParam == GWL_EXSTYLE)
        elif msg == WM_THEMECHANGED:
            self.on_theme_changed.execute()
        elif msg == WM_USERCHANGED:
            self.on_user_changed.execute()
        elif msg == WM_ENABLE:
            self.on_enable.execute(wParam == TRUE)
        elif msg == WM_ERASEBKGND:
            dc = DC.foreign_owner(wParam)
            if not all(self.on_erase_background.execute(dc)):
                return FALSE
        elif msg == WM_SETFONT:
            self.on_set_font.execute(wParam, LOWORD(lParam) == TRUE)
        elif msg == WM_TIMER:
            if not all(self.on_timer.execute(wParam, i_cast(lParam, TIMERPROC))):
                return FALSE
        else:
            result = self.on_unknown_message.execute(msg, wParam, lParam)
            for value in result:
                if value != -1:
                    return value
                
        return DefWindowProcW(hwnd, msg, wParam, lParam)
    
    def timer(self, function: Callable, elapse: int, event_id: int = 0) -> int:
        @TIMERPROC
        def timerProc(hWndUnused: int, wmTimerUnused: int, idEvent: int, dwTime: int):
            function(idEvent, dwTime)
        event_id = SetTimer(self, event_id, elapse, timerProc)
        self._timers[event_id] = timerProc
        return event_id
    
    def delay(self, function: Callable, elapse: int, event_id: int = 0) -> int:
        @TIMERPROC
        def timerProc(hWndUnused: int, wmTimerUnused: int, idEvent: int, dwTimeUnused: int):
            function()
            self.kill_timer(idEvent)
        event_id = SetTimer(self, event_id, elapse, timerProc)
        self._timers[event_id] = timerProc
        return event_id
    
    def kill_timer(self, event_id: int):
        if not KillTimer(self, event_id):
            raise WinException()
        
    def close(self):
        SendMessage(self, WM_CLOSE, 0, 0)
        
    def destroy(self):
        SendMessage(self, WM_DESTROY, 0, 0)
        
    def hide(self):
        self.show(SW_HIDE)
    
    def show(self, nCmdShow: int = SW_SHOW):
        ShowWindow(self, nCmdShow)
        
    def set_font(self, font: int | HANDLE, redraw: bool = True):
        self.send(WM_SETFONT, font, redraw)
        
    def send(self, message: int, wParam: int = 0, lParam: int = 0) -> int:
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
            
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
            
        return SendMessage(self, message, wParam, lParam)
        
    @property
    def parent(self) -> 'Window':
        return Window(GetParent(self), headless=True)
    
    @parent.setter
    def parent(self, parent: int | HWND):
        SetParent(self, parent)
        
    @property
    def rect(self) -> RECT:
        rc = RECT()
        if not GetWindowRect(self, byref(rc)):
            raise WinException()
        return rc
    
    def set_position(self, x: int = None, y: int = None, 
                     width: int = None, height: int = None, 
                     flags: int = 0, insert_after: int | HWND = None):
        if insert_after is None:
            flags |= SWP_NOZORDER
        notx, noty = x is None, y is None
        if notx or noty:
            if notx and noty:
                flags |= SWP_NOMOVE
                x = y = 0
            else:
                rect = self.rect
                if notx: x = rect.left
                if noty: y = rect.top
        notw, noth = width is None, height is None
        if notw or noth:
            if notw and noth:
                flags |= SWP_NOSIZE
                width = height = 0
            else:
                rect = self.rect
                if notw: width = rect.right - rect.left
                if noth: height = rect.bottom - rect.top
        SetWindowPos(self, insert_after, x, y, width, height, flags)
        
    def set_foreground(self):
        SetForegroundWindow(self)
        
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
        return self.rect.left
    
    @x.setter
    def x(self, x: int):
        self.set_position(x=x)
        
    @property
    def y(self) -> int:
        return self.rect.top
    
    @y.setter
    def y(self, y: int):
        self.set_position(y=y)
        
    def invalidate(self, rect: RECT = None, erase: bool = True):
        InvalidateRect(self, byref(rect) if rect is not None else rect, erase)
    
    def launch(self):
        if not UpdateWindow(self):
            raise WinException()
        
        msg = MSG()
        pMsg = byref(msg)
        
        while self.running:
            if PeekMessage(pMsg, NULL, 0, 0, PM_REMOVE):
                TranslateMessage(pMsg)
                DispatchMessageW(pMsg)
                
            self.after_message.execute()

class ControlsT:
    _controls: dict[str, int]
    
    def __init__(self):
        self._controls = {}
    
    def __getitem__(self, control: str) -> int:
        control_id = self._controls.get(control, None)
        if control_id is None:
            control_id = Control.id()
            self._controls[control] = control_id
        return control_id
    
Controls = ControlsT()

class Control(Window):
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
        Control._id_last += 1
        return Control._id_last
    
    @property
    def visible(self):
        return self.style & WS_VISIBLE
    
    @visible.setter
    def visible(self, visible: bool):
        if visible:
            self.style &= ~WS_VISIBLE
        else:
            self.style |= WS_VISIBLE
    
    def create(self, width: int, height: int, x: int = 0, y: int = 0, window_name: str='Control', relative: int | HWND = NULL):
        if relative is not NULL:
            rc = RECT()
            
            if not GetWindowRect(relative, byref(rc)):
                raise WinException()
            
            rcParent = RECT()
            
            if not GetWindowRect(self._parent, byref(rcParent)):
                raise WinException()
            
            x, y = rc.left + x - rcParent.left, rc.top + y - rcParent.top
            
        super().create(width, height, x, y, window_name, self._parent, self._identifier)
        
icex = INITCOMMONCONTROLSEX()
icex.dwSize = sizeof(icex)
icex.dwICC = ICC_WIN95_CLASSES

if not InitCommonControlsEx(icex.ref()):
    raise WinException()

class GLWindow(Window):
    """
    GL (1.1) Window.
    """
    
    pfd: PIXELFORMATDESCRIPTOR
    gl_context: GLContext
    
    def __init__(self):
        super().__init__()
        self.class_style = CS_OWNDC
        self.after_message += EventCallback(self.GL_after_message, Priority.Max)
        self._style |= WS_CLIPCHILDREN | WS_CLIPSIBLINGS
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
    
    def GL_after_message(self):
        SwapBuffers(self.dc)
        
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT, 
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT, 
               window_name: str = 'Window', parent = NULL):
        super().create(width, height, x, y, window_name, parent, NULL)
        self.dc = DC.get(self)
        pPfd = self.pfd.ref()
        iPixelFormat = ChoosePixelFormat(self.dc, pPfd)
        SetPixelFormat(self.dc, iPixelFormat, pPfd)
        self.gl_context = GLContext.current(self.dc)