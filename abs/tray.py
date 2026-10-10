from .window import *
from win.shellapi import *

class TrayBalloonIcon:
    NONE = NIIF_NONE
    INFO = NIIF_INFO
    WARNING = NIIF_WARNING
    ERROR = NIIF_ERROR

class TrayIcon(Window):
    WM_TRAYICON = WM_USER + 1414
    notify_icon: NOTIFYICONDATAW
    on_balloon_show: MultiEvent
    on_balloon_hide: MultiEvent
    on_balloon_timeout: MultiEvent
    on_balloon_click: MultiEvent
    
    def __init__(self):
        super().__init__()
        self.style = 0
        self.on_destroy += self.TrayIcon_on_destroy
    
    def headless_init(self):
        self.notify_icon = NOTIFYICONDATAW()
        self.notify_icon.cbSize = sizeof(NOTIFYICONDATAW)
        self.on_balloon_show = MultiEvent()
        self.on_balloon_hide = MultiEvent()
        self.on_balloon_timeout = MultiEvent()
        self.on_balloon_click = MultiEvent()
    
    @property
    def icon(self) -> Icon | None:
        return Icon.foreign_owner(self.notify_icon.hIcon)
    
    @icon.setter
    def icon(self, icon: int | HANDLE):
        self.notify_icon.hIcon = icon
        self.notify_icon.uFlags |= NIF_ICON
        if self.value: self.update()
    
    def create(self):
        super().create(0, 0, 0, 0, NULL)
        self.notify_icon.hWnd = self.value
        self.notify_icon.uFlags |= NIF_MESSAGE
        self.notify_icon.uCallbackMessage = TrayIcon.WM_TRAYICON
        if not Shell_NotifyIconW(NIM_ADD, self.notify_icon.ref()):
            raise WinException()
        self.notify_icon.uFlags = 0
    
    @property
    def balloon_icon(self) -> Icon | None:
        return Icon.foreign_owner(self.notify_icon.hBalloonIcon)
    
    @balloon_icon.setter
    def balloon_icon(self, balloon_icon: int | HANDLE):
        self.notify_icon.hBalloonIcon = balloon_icon
        self.notify_icon.uFlags |= NIF_INFO
        extra = NIIF_USER
        if isinstance(balloon_icon, int):
            if balloon_icon >= TrayBalloonIcon.NONE and balloon_icon <= TrayBalloonIcon.ERROR:
                extra = balloon_icon
        self.notify_icon.dwInfoFlags |= extra
        
    def delete(self):
        if not Shell_NotifyIconW(NIM_DELETE, self.notify_icon.ref()):
            raise WinException()
        self.notify_icon.hWnd = 0
        
    def TrayIcon_on_destroy(self):
        if self.notify_icon.hWnd:
            Shell_NotifyIconW(NIM_DELETE, self.notify_icon.ref())
        
    def update(self):
        Shell_NotifyIconW(NIM_MODIFY, self.notify_icon.ref())
        self.notify_icon.uFlags = 0
        
    @property
    def tip(self) -> str:
        return self.notify_icon.szTip.value
    
    @tip.setter
    def tip(self, tip: str):
        self.notify_icon.szTip.value = tip
        self.notify_icon.uFlags |= NIF_TIP
        self.update()
    
    def balloon(self, sound: bool = True, large_icon: bool = False, realtime: bool = False):
        if not sound:
            self.notify_icon.dwInfoFlags |= NIIF_NOSOUND
        if large_icon:
            self.notify_icon.dwInfoFlags |= NIIF_LARGE_ICON
        if realtime:
            self.notify_icon.uFlags |= NIF_REALTIME
        self.update()
        self.notify_icon.dwInfoFlags = 0
        
    @property
    def info_title(self) -> str:
        return self.notify_icon.szInfoTitle.value
    
    @info_title.setter
    def info_title(self, info_title: str):
        self.notify_icon.szInfoTitle.value = info_title
        self.notify_icon.uFlags |= NIF_INFO
        
    @property
    def info(self) -> str:
        return self.notify_icon.szInfoTitle.value
    
    @info.setter
    def info(self, info: str):
        self.notify_icon.szInfo.value = info
        self.notify_icon.uFlags |= NIF_INFO
    
    def TrayIcon_on_unknown_message(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if msg == TrayIcon.WM_TRAYICON:
            if lParam == WM_CONTEXTMENU:
                wParamData = self.value
                x, y = Cursor.position
                lParamData = MAKELPARAM(x, y)
            elif lParam >= WM_MOUSEFIRST and lParam <= WM_MOUSELAST:
                wParamData = 0
                if (GetKeyState(VK_CONTROL)  & KF_UP): wParamData |= MK_CONTROL
                if (GetKeyState(VK_SHIFT)    & KF_UP): wParamData |= MK_SHIFT
                if (GetKeyState(VK_LBUTTON)  & KF_UP): wParamData |= MK_LBUTTON
                if (GetKeyState(VK_RBUTTON)  & KF_UP): wParamData |= MK_RBUTTON
                if (GetKeyState(VK_MBUTTON)  & KF_UP): wParamData |= MK_MBUTTON
                if (GetKeyState(VK_XBUTTON1) & KF_UP): wParamData |= MK_XBUTTON1
                if (GetKeyState(VK_XBUTTON2) & KF_UP): wParamData |= MK_XBUTTON2
                x, y = Cursor.position
                lParamData = MAKELPARAM(x, y)
            else:
                wParamData = 0
                lParamData = 0
            self.window_proc(hwnd, lParam, wParamData, lParamData)
            return 0
        elif msg == NIN_BALLOONSHOW:
            self.on_balloon_show.execute()
            return 0
        elif msg == NIN_BALLOONHIDE:
            self.on_balloon_hide.execute()
            return 0
        elif msg == NIN_BALLOONTIMEOUT:
            self.on_balloon_timeout.execute()
            return 0
        elif msg == NIN_BALLOONUSERCLICK:
            self.on_balloon_click.execute()
            return 0
        return None
    
    def hide(self):
        self.notify_icon.dwStateMask |= NIS_HIDDEN
        self.notify_icon.dwState |= NIS_HIDDEN
        self.notify_icon.uFlags |= NIF_STATE
        if self.value: self.update()
        self.notify_icon.dwStateMask = 0
    
    def show(self):
        self.notify_icon.dwStateMask |= NIS_HIDDEN
        self.notify_icon.dwState &= ~NIS_HIDDEN
        self.notify_icon.uFlags |= NIF_STATE
        if self.value: self.update()
        self.notify_icon.dwStateMask = 0