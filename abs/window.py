from win.defbase_errordef import *
from win.libloaderapi import *
from win.commctrl import *
from .core.handle import *
from .core.event import *
from .core.absutils import *

import random

class Menu(Handle):
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
        if isinstance(lp, str):
            lp = create_unicode_buffer(lp)
        if not AppendMenuW(self, flags, PtrUtil.get_address(item), i_cast(lp, LPCWSTR)):
            raise WinException()

    def modify(self, position: int, item: int, lp, flags: int):
        if isinstance(lp, str):
            lp = create_unicode_buffer(lp)
        if not ModifyMenuW(self, position, flags, PtrUtil.get_address(item), i_cast(lp, LPWSTR)):
            raise WinException()

class PopupMenu(Menu):
    def __init__(self):
        super().__init__()
        self.value = CreatePopupMenu()
        if not self.value:
            raise WinException()
        
    def track(self, x: int, y: int, hWnd: int | HANDLE, flags: int=0):
        if not TrackPopupMenu(self, flags, x, y, 0, hWnd, NULL):
            raise WinException()

class Window(HWND):
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, window: int | HANDLE):
        if isinstance(window, int):
            return window == self.value
        return window.value == self.value
    
    @classmethod
    def foreign(cls, hwnd: int) -> 'Window':
        if PtrUtil.get_address(hwnd) == 0: return None
        if not IsWindow(hwnd):
            raise WinException()
        return cls(hwnd, headless=True)
    
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
            self.on_left_button_down = Event()
            self.on_left_button_up = Event()
            self.on_left_button_double_click = Event()
            self.on_right_button_down = Event()
            self.on_right_button_up = Event()
            self.on_right_button_double_click = Event()
            self.on_close = Event()
            self.on_destroy = Event()
            self.on_key_down = Event()
            self.on_key_up = Event()
            self.on_move = Event()
            self.on_show = Event()
            self.on_style_changed = Event()
            self.on_theme_changed = Event()
            self.on_user_changed = Event()
            self.on_unknown_message = Event()
            self.on_enable = Event()
            self.on_set_font = Event()
            self.on_mouse_wheel = Event()
            self.on_timer = Event()
            self.after_message = Event()
            self.on_notify = Event()
            self.on_message = Event()
            self.on_mouse_move = Event()
            self.on_draw_item = Event()
            self.on_palette_changed = Event()
            self.on_destroy += self.Window_on_destroy
    
    _timers: dict[int, FARPROC]
    class_name: str | None
    
    cursor: int | HANDLE | None
    icon: int | HANDLE | None
    
    def Window_on_destroy(self):
        app = Application()
        app.windows -= 1
        app.notify()
    
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
    
    def remove(self, *styles: int):
        for style in styles:
            self.style &= ~style
    
    def remove_extended(self, *extended_styles: int):
        for extended_style in extended_styles:
            self.extended_style &= ~extended_style
    
    def enable(self):
        EnableWindow(self, True)
        
    def disable(self):
        EnableWindow(self, False)
    
    def register(self):
        wc = WNDCLASSW()
        
        wc.hbrBackground = self.hbrBackground
        if self.icon is None:
            self.icon = Icon.load(IDI_APPLICATION)
        if self.cursor is None:
            self.cursor = Cursor.load(IDC_ARROW)
        wc.hIcon = self.icon
        wc.hCursor = self.cursor
        wc.hInstance = GetModuleHandleW(NULL)
        wc.style = self.class_style
        
        class_name = f'Win-Abs/Class-N{str(random.randint(0, 10000000)).zfill(8)}'
        
        wc.lpszClassName = class_name
        self.pfnWndProc = wc.lpfnWndProc = WNDPROC(self.window_proc)
        atomResult = RegisterClass(wc.ref())
        
        if not atomResult:
            raise WinException()
        
        self.class_name = class_name
    
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
    
    def on_paint(self, dc: PaintDC):
        pass
    
    def on_command(self, identifier: int, notify_code: int, hwnd: int):
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
    
    def window_proc(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        if msg == WM_CREATE:
            self.running = True
            self.value = hwnd
            Application().windows += 1
            if not all(self.on_create.execute()):
                return -1
            return 0
        elif msg == WM_PAINT:
            with PaintDC(self) as dc:
                self.on_paint(dc)
            return 0
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
            if all(self.on_close.execute()):
                self.destroy()
        elif msg == WM_DESTROY:
            self.on_destroy.execute()
            self.running = False
        elif msg == WM_COMMAND:
            self.on_command(LOWORD(wParam), HIWORD(wParam), lParam)
            return 0
        elif msg == WM_SIZE:
            self.on_size(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
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
            self.on_show.execute(wParam == TRUE)
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
            if self.on_erase_background(dc):
                return TRUE
            return FALSE
        elif msg == WM_SETFONT:
            self.on_set_font.execute(Font.foreign_owner(wParam), LOWORD(lParam) == TRUE)
            return 0
        elif msg == WM_TIMER:
            self.on_timer.execute(wParam, i_cast(lParam, TIMERPROC))
            return 0
        elif msg == WM_NOTIFY:
            nmhdr = i_cast(lParam, LPNMHDR).contents
            self.on_notify.execute(nmhdr)
            return 0
        elif msg == WM_MOUSEMOVE:
            self.on_mouse_move.execute(wParam, LOWORD(lParam), HIWORD(lParam))
            return 0
        elif msg == WM_DRAWITEM:
            if not self.on_draw_item.empty():
                self.on_draw_item.execute(wParam, i_cast_value(lParam, DRAWITEMSTRUCT))
                return TRUE
        elif msg == WM_SETFOCUS:
            self.on_focus_changed(Window.foreign(wParam))
            return 0
        elif msg == WM_KILLFOCUS:
            self.on_focus_lost(Window.foreign(wParam))
            return 0
        elif msg == WM_PALETTECHANGED:
            self.on_palette_changed.execute(Palette.foreign_owner(wParam))
        elif msg == WM_SETCURSOR:
            result = self.on_set_cursor(Window.foreign(wParam), LOWORD(lParam), HIWORD(lParam))
            if result is not None:
                return result
        else:
            result = self.on_unknown_message.execute(hwnd, msg, wParam, lParam)
            for value in result:
                if value is not None:
                    return value
                
        return self.wnd_proc_fallback(hwnd, msg, wParam, lParam)
    
    def wnd_proc_fallback(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return DefWindowProcW(hwnd, msg, wParam, lParam)
    
    def focus(self):
        SetFocus(self)
    
    @property
    def focused(self) -> bool:
        return GetFocus() == self.value
    
    def capture(self):
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
        if event_id in self._timers:
            del self._timers[event_id]
        
    def close(self):
        self.post(WM_CLOSE)
        
    def destroy(self):
        if not DestroyWindow(self):
            raise WinException()
        
    def hide(self):
        self.post(SW_HIDE)
    
    def show(self, nCmdShow: int = SW_SHOW):
        ShowWindow(self, nCmdShow)
        
    def set_font(self, font: int | HANDLE, redraw: bool = True):
        self.post(WM_SETFONT, font, redraw)
        
    @property
    def font(self) -> Font:
        return Font.foreign_owner(self.send(WM_GETFONT))
    
    @font.setter
    def font(self, font: int | HANDLE):
        self.set_font(font)
    
    def is_child(self, hWnd: int | HANDLE) -> bool:
        return bool(IsChild(self, hWnd))
    
    def is_child_of(self, hWnd: int | HANDLE) -> bool:
        return bool(IsChild(hWnd, self))
    
    def send(self, message: int, wParam: int = 0, lParam: int = 0) -> int:
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
        if isinstance(wParam, str):
            wParam = create_unicode_buffer(wParam)
        
        if isinstance(lParam, str):
            lParam = create_unicode_buffer(lParam)
        
        if wParam != 0: 
            wParam = PtrUtil.get_address(wParam)
            
        if lParam != 0:
            lParam = PtrUtil.get_address(lParam)
            
        PostMessage(self, message, wParam, lParam)
"""  """    
    def map(self, window: int | HWND, points: Iterable[GraphicUtils.Point]) -> tuple[POINT, ...]:
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
        hwnd = GetForegroundWindow()
        return Window.foreign(hwnd)
    
    @classmethod
    def desktop(self) -> 'Window':
        hwnd = GetDesktopWindow()
        return Window.foreign(hwnd)
    
    def set_foreground(self):
        if not SetForegroundWindow(self):
            raise WinException()
        
    def to_client(self, screen: POINT):
        if not ScreenToClient(self, byref(screen)):
            raise WinException()
        
    def to_screen(self, client: POINT):
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
        
    def invalidate(self, rect: RECT = None, erase: bool = True):
        InvalidateRect(self, byref(rect) if rect is not None else rect, erase)
    
    def update(self):
        if not UpdateWindow(self):
            raise WinException()

class Application:
    INSTANCE: 'Application' = None
    
    modeless_dialogs: list[int | HWND]
    windows: int
    
    def __new__(cls):
        if Application.INSTANCE is None:
            return super().__new__(cls)
            
        return Application.INSTANCE
    
    def __init__(self):
        if Application.INSTANCE is None:
            self.after_message = Event()
            self.modeless_dialogs = []
            self.on_message = Event()
            self.running = False
            self.windows = 0
            Application.INSTANCE = self
            
    def notify(self):
        if not self.windows:
            self.running = False
    
    def launch(self):
        self.running = True
        msg = MSG()
        pMsg = byref(msg)
        
        while self.running:
            if PeekMessage(pMsg, NULL, 0, 0, PM_REMOVE):
                dispatch = True
                for modeless_dialog in self.modeless_dialogs:
                    if IsDialogMessage(modeless_dialog, pMsg):
                        dispatch = False
                        break
                if dispatch:
                    TranslateMessage(pMsg)
                    self.on_message.execute(msg)
                    DispatchMessageW(pMsg)
            
            self.after_message.execute()
            MsgWaitForMultipleObjects(0, NULL, FALSE, 10, QS_ALLEVENTS)

class IdentifiersT:
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
            self.style |= WS_VISIBLE
        else:
            self.style &= ~WS_VISIBLE
    
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
        self.gl_tick = Event()
        self.enable_after_message_render = True
        Application().after_message += self.GL_after_message
        self.on_close += self.GL_close
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
        self.gl_ready = Event()
        self.manual_initialize = False
    
    def disable_after_message_render(self):
        self.enable_after_message_render = False
        Application().after_message -= self.GL_after_message
    
    def GL_after_message(self):
        self.gl_tick.execute()
        SwapBuffers(self.dc)
        
    def GL_close(self):
        if self.enable_after_message_render:
            Application().after_message -= self.GL_after_message
    
    def initialize_gl(self):
        self.dc = DC.get(self)
        pPfd = self.pfd.ref()
        iPixelFormat = ChoosePixelFormat(self.dc, pPfd)
        SetPixelFormat(self.dc, iPixelFormat, pPfd)
        self.gl_context = GLContext.current(self.dc)
        self.gl_ready.execute()
    
    def create(self, width: int = CW_USEDEFAULT, height: int = CW_USEDEFAULT, 
               x: int = CW_USEDEFAULT, y: int = CW_USEDEFAULT, 
               window_name: str = 'Window', parent = NULL):
        super().create(width, height, x, y, window_name, parent, NULL)
        if not self.manual_initialize:
            self.initialize_gl()

PFNWGLCREATECONTEXTATTRIBSARB = APIENTRY(HGLRC, HDC, HGLRC, PINT)
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
        self.gl_ready.block()
        super().create(width, height, x, y, window_name, parent)
        self.gl_ready.unblock()
        wglCreateContextAttribsARB = wglGetProcAddress(b'wglCreateContextAttribsARB')
        self.wglCreateContextAttribsARB = i_cast(wglCreateContextAttribsARB, PFNWGLCREATECONTEXTATTRIBSARB)
        attribs = [entry for pair in self.attributes.items() for entry in pair]
        attribList = (INT * (len(attribs) + 1))(*attribs, 0)
        hGLCtx = self.wglCreateContextAttribsARB(
            self.dc, NULL, attribList)
        if not hGLCtx:
            raise WinException()
        self.gl_context = GLContext.current_external(self.dc, hGLCtx).owned_current(True)
        self.gl_ready.execute()
        
    def version(self, major: int | str, minor: int = None):
        if minor is None:
            if isinstance(major, str):
                components = major.split('.')[0:2]
                major, minor = components
                major, minor = int(major), int(minor)
            else:
                minor = 0
                
        major = int(major)
        minor = int(minor)
        self.attributes[WGL_CONTEXT_MAJOR_VERSION_ARB] = major
        self.attributes[WGL_CONTEXT_MINOR_VERSION_ARB] = minor