from .window import *
from win.abs.core.iathook import *
import winreg

class DarkModeUtil:
    """
    Utilities for Dark Mode.
    """
    _USER_ENABLED: ClassVar[bool | None] = None
    ON_MANAGED_CHANGE: ClassVar[MultiEvent] = MultiEvent()
    
    @classmethod
    def enabled(cls) -> bool:
        """
        Check Dark Mode is enabled.
        """
        
        if cls._USER_ENABLED is not None:
            return cls._USER_ENABLED
        
        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, 
                'SOFTWARE\\Microsoft\\Windows\\'
                'CurrentVersion\\Themes\\Personalize') as key_Personalize:
                value_AppsUseLightTheme = winreg.QueryValueEx(key_Personalize, 'AppsUseLightTheme')[0]
            return value_AppsUseLightTheme == 0
        except:
            cls._USER_ENABLED = False
            return False
        
    @classmethod
    def enable(cls):
        """
        Enable Dark Mode.
        """
        cls._USER_ENABLED = True
        cls.ON_MANAGED_CHANGE.execute(True)
        
    @classmethod
    def disable(cls):
        """
        Disable Dark Mode.
        """
        cls._USER_ENABLED = False
        cls.ON_MANAGED_CHANGE.execute(False)
        
    @classmethod
    def reset(cls):
        """
        Reset Dark Mode user settings.
        """
        cls._USER_ENABLED = None
        cls.ON_MANAGED_CHANGE.execute(None)
        
    @classmethod
    def usersetted(cls) -> bool:
        """
        Check Dark Mode settings is user-setted.
        """
        return cls._USER_ENABLED is not None

@uxtheme.foreign(BOOL, BOOL, ordinal=135)
def AllowDarkModeForApp_Or_SetPreferredAppMode(n: int) -> int: ...

@uxtheme.foreign(VOID, ordinal=136)
def FlushMenuThemes(): ...

@uxtheme.foreign(VOID, ordinal=104)
def RefreshImmersiveColorPolicyState(): ...

@uxtheme.foreign(BOOL, HWND, BOOL, ordinal=133)
def AllowDarkModeForWindow(hWnd: int, allow: int) -> int: ...

IMMERSIVE_HC_CACHE_MODE = UINT
IHCM_USE_CACHED_VALUE = 0
IHCM_REFRESH = 1

@uxtheme.foreign(UINT, UINT, UINT, BOOL, IMMERSIVE_HC_CACHE_MODE, ordinal=95)
def GetImmersiveColorFromColorSetEx(dwImmersiveColorSet: int, dwImmersiveColorType: int, bIgnoreHighContrast: int, dwHighContrastCacheMode: int) -> int: ...

@uxtheme.foreign(INT, LPWSTR, ordinal=96)
def GetImmersiveColorTypeFromName(pName: WT_LPWSTR) -> int: ...

@uxtheme.foreign(INT, BOOL, BOOL, ordinal=98)
def GetImmersiveUserColorSetPreference(bForceCheckRegistry: int, bSkipCheckOnFail: int) -> int: ...

@uxtheme.foreign(PTR(LPWSTR), UINT, ordinal=100)
def GetImmersiveColorNamedTypeByIndex(dwImmersiveColorIndex: int) -> IPointer[LPWSTR]: ...

@uxtheme.foreign(UINT, ordinal=105)
def GetImmersiveDefaultColorSet() -> int: ...

class ImmersiveColors:
    _COLOR_SET: ClassVar[int] = GetImmersiveDefaultColorSet()
    _COLOR_CACHE: ClassVar[dict[str, int]] = {}

    @classmethod
    def update(cls):
        cls._COLOR_SET = GetImmersiveUserColorSetPreference(True, False)
        cls._COLOR_CACHE.clear()

    def __class_getitem__(cls, name: str) -> Color.ABGR:
        index = cls._COLOR_CACHE.get(name, None)
        if index is None:
            index = GetImmersiveColorTypeFromName('Immersive' + name)
            if index == -1:
                raise KeyError(f"'{name}'")
            cls._COLOR_CACHE[name] = index
        return Color.ABGR(GetImmersiveColorFromColorSetEx(cls._COLOR_SET, index, False, IHCM_USE_CACHED_VALUE))

@user32.foreign(VOID, LPCOLORREF, LPCOLORREF, INT)
def SetSysColorsTemp(pColors: IPointer[COLORREF], pReserved: IPointer[COLORREF], dwCount: int) -> int: ...

class DarkModeWindow(Window):
    _DARK_MODE_ENABLED: ClassVar[bool] = False
    _DARK_MODE_USERSETTED: ClassVar[bool] = False
    _DARK_MODE_CHANGED: ClassVar[MultiEvent] = MultiEvent()
    _internal_explorerscrollbar_name: ClassVar[LPWSTR | None] = None
    _internal_pfunction_OpenNcThemeData: ClassVar[FARPROC | None] = None
    
    _ctrl_colored_brush: Brush | None
    
    def __init__(self):
        super().__init__()
        self._ctrl_colored_brush = None
        # Dark Mode visibility presented in Windows 10
        # since 17666 build, if build number <17666 then
        # dark mode is forcely disabled and physically
        # can't draw dark theme by system API
        if cpreproc.get_build() >= 17666:
            # subscribe on Window events:
            # WM_CREATE, WM_SETTINGCHANGE, 
            # WM_DESTROY, WM_PARENTNOTIFY
            self.on_create += self._darkmode_window_created
            self.on_setting_change += self._darkmode_window_setting_changed
            self.on_destroy += self._darkmode_window_destroyed
            self.on_parent_notify += self._darkmode_window_parentnotify
            self._DARK_MODE_CHANGED += self._darkmode_window_mode_changed
    
    @classmethod
    def _init_darkmode_scrollbar_iathook(cls):
        cls._internal_explorerscrollbar_name = LPWSTR('Explorer::ScrollBar')
        @uxtheme.foreign(HTHEME, HWND, LPWSTR, ordinal=49)
        def OpenNcThemeData(hWnd: int, classList: WT_LPWSTR) -> int: ...
        FN_OpenNcThemeData = WINAPI(HTHEME, HWND, LPWSTR)
        def _OpenNcThemeData(hWnd: int, classList: LPWSTR) -> int:
            if cls._DARK_MODE_ENABLED:
                if classList.value == 'ScrollBar':
                    classList = cls._internal_explorerscrollbar_name
                    hWnd = None
            return OpenNcThemeData(hWnd, classList)
        cls._internal_pfunction_OpenNcThemeData = FN_OpenNcThemeData(_OpenNcThemeData)
        IATHook.replace(comctl32, 'uxtheme.dll', 49, cls._internal_pfunction_OpenNcThemeData, delay_load=True)
    
    @classmethod
    def _init_darkmode_window_internals(cls):
        cls._init_darkmode_scrollbar_iathook()
    
    @classmethod
    def _init_darkmode_window(cls):
        # Dark Mode visibility presented in Windows 10
        # since 17666 build, if build number <17666 then
        # dark mode is forcely disabled and physically
        # can't draw dark theme by system API
        if cpreproc.get_build() < 17666:
            cls._DARK_MODE_ENABLED = False
            cls._DARK_MODE_USERSETTED = True
        else:
            cls._DARK_MODE_ENABLED = DarkModeUtil.enabled()
            cls._DARK_MODE_USERSETTED = DarkModeUtil.usersetted()
            
            DarkModeUtil.ON_MANAGED_CHANGE += cls._darkmode_managed_change
            # 17666-18334 AllowDarkModeForApp and 18334+ SetPreferredAppMode
            # lays on the same uxtheme.dll ordinal (135) and
            # TRUE in AllowDarkModeForApp equals AllowDark in SetPreferredAppMode
            # as TRUE = 1 and AllowDark = 1 too
            AllowDarkModeForApp_Or_SetPreferredAppMode(1)
            # refresh immersive color policy state
            RefreshImmersiveColorPolicyState()
            # flush menu themes to draw menu
            # with themed dark colors
            FlushMenuThemes()
            # refresh ImmersiveColors cache
            ImmersiveColors.update()
            # init DarkModeWindow internals
            cls._init_darkmode_window_internals()
    
    def _darkmode_window_created(self) -> bool:
        if self._DARK_MODE_ENABLED:
            # set window theme to DarkMode_Explorer
            # for dark scrollbar
            self.set_window_theme('DarkMode_Explorer')
        # update dark-mode view
        self._update_darkmode_window()
        return True
    
    def _darkmode_window_destroyed(self):
        self._DARK_MODE_CHANGED -= self._darkmode_window_mode_changed
    
    def _update_darkmode_window(self):
        # reset control color brush
        self._ctrl_color_brush = None
        # apply DWMWA_USE_IMMERSIVE_DARK_MODE to window
        # for dark window caption or if disabled
        # remove its attribute from window
        # (Applied only if WS_CHILD style not presented)
        if not (self.style & WS_CHILD):
            self.set_dwm_attribute(DWMWA_USE_IMMERSIVE_DARK_MODE, self._DARK_MODE_ENABLED)
        # if window is visible then update its non-client frame
        if self.visible:
            foreground = Window.foreground()
            # window active -> from false to true
            if foreground == self:
                self.send(WM_NCACTIVATE, FALSE)
                self.send(WM_NCACTIVATE, TRUE)
            # window inactive -> from true to false
            else:
                self.send(WM_NCACTIVATE, TRUE)
                self.send(WM_NCACTIVATE, FALSE)
        # tell the window about the theme was changed
        self.send(WM_THEMECHANGED)
    
    def _darkmode_window_setting_changed(self, name: str, action: int):
        if name == 'ImmersiveColorSet' and not self._DARK_MODE_USERSETTED:
            # flush menu themes for dark themed colors
            FlushMenuThemes()
            # reload immersive color policy state
            RefreshImmersiveColorPolicyState()
            # update the dark mode window state
            self._darkmode_managed_change(DarkModeUtil.enabled())
            self._update_darkmode_window()
    
    def _darkmode_window_mode_changed(self):
        self._update_darkmode_window()
    
    @classmethod
    def _darkmode_managed_change(cls, value: bool | None):
        if value is None:
            cls._DARK_MODE_USERSETTED = False
            cls._DARK_MODE_ENABLED = DarkModeUtil.enabled()
        else:
            cls._DARK_MODE_USERSETTED = True
            cls._DARK_MODE_ENABLED = value
        cls._DARK_MODE_CHANGED.execute()
    
    def _darkmode_window_parentnotify(self, msg: int, args: list[Any]):
        if msg == WM_CREATE:
            if self._DARK_MODE_ENABLED:
                # the child control was created
                window: Window
                _, window = args
                # check window class is in common controls list
                class_name = window.class_name.lower()
                # allow dark mode for this window
                AllowDarkModeForWindow(window, True)
                # ComboBox and ComboBoxEx32 classes is themed
                # by DarkMode_CFD::Combobox class
                if class_name in ('combobox', 'comboboxex32'):
                    window.set_window_theme('CFD')
                # BUTTON class theme is defined in DarkMode_Explorer::Button
                if class_name == 'button':
                    window.set_window_theme('Explorer')
                # additionally handle and subclass the SysListView32
                # because it has SysHeader32 control in it plus
                # supports TextColor/BkColor and NM_CUSTOMDRAW
                elif class_name == 'syslistview32':
                    window.set_window_theme('ItemsView')
                    window.subclass(self._darkmode_listview_hook)
                    window.send(
                        LVM_SETEXTENDEDLISTVIEWSTYLE, 
                        LVS_EX_DOUBLEBUFFER, LVS_EX_DOUBLEBUFFER)
                    header = Window.foreign(window.send(LVM_GETHEADER))
                    if header is not None:
                        header.set_window_theme('ItemsView')
                        AllowDarkModeForWindow(header, True)
                        header.send(WM_THEMECHANGED)
                # SysTreeView32 needs subclassing coz it is
                # complex control and supports TextColor/BkColor
                # settings plus NM_CUSTOMDRAW
                elif class_name == 'systreeview32':
                    window.set_window_theme('Explorer')
                    window.send(
                        TVM_SETEXTENDEDSTYLE, 
                        TVS_EX_DOUBLEBUFFER, TVS_EX_DOUBLEBUFFER)
                    window.subclass(self._darkmode_treeview_hook)
                # msctls_statusbar32 needs to be hooked for custom paint
                elif class_name == 'msctls_statusbar32':
                    window.subclass(self._darkmode_statusbar_hook)
                # EDIT class theme is defined in DarkMode_CFD::Edit
                elif class_name == 'edit':
                    window.set_window_theme('CFD')
                # ToolbarWindow32 class theme is defined in Dark::Toolbar
                elif class_name == 'toolbarwindow32':
                    window.set_window_theme('Dark')
                window.send(WM_THEMECHANGED)
    
    def _claim_ctrl_colored_brush(self) -> Brush:
        if self._ctrl_colored_brush is None:
            self._ctrl_colored_brush = Brush.create(Color.BGR.string('#383838'))
        return self._ctrl_colored_brush
    
    def _on_control_color(self, window: Window, dc: DC) -> Brush:
        if not self._DARK_MODE_ENABLED:
            return None
        dc.text_color = Color.BGR.string('#ffffff')
        dc.bk_color = Color.BGR.string('#212121')
        return self._claim_ctrl_colored_brush()
    
    def on_control_color_edit(self, edit: Window, dc: DC) -> Brush:
        return self._on_control_color(edit, dc)
    
    def on_control_color_dialog(self, dialog: Window, dc: DC) -> Brush:
        return self._on_control_color(dialog, dc)
    
    def on_control_color_listbox(self, listbox: Window, dc: DC) -> Brush:
        return self._on_control_color(listbox, dc)
    
    def _darkmode_listview_hook(self, hwnd: int, msg: int, wParam: int, lParam: int):
        if not self._DARK_MODE_ENABLED:
            return None
        if msg == WM_NOTIFY:
            nm = i_cast_value(lParam, NMHDR)
            code = INT(nm.code).value
            
            if code == NM_CUSTOMDRAW:
                nmcd = i_cast_value(lParam, NMCUSTOMDRAW)
                stage = nmcd.dwDrawStage
                
                if stage == CDDS_PREPAINT:
                    return CDRF_NOTIFYITEMDRAW
                elif stage == CDDS_ITEMPREPAINT:
                    dc = DC.foreign_owner(nmcd.hdc)
                    dc.text_color = Color.BGR.string('#ffffff')
                    return CDRF_DODEFAULT
        elif msg == WM_THEMECHANGED:
            window = Window.foreign(hwnd)
            color = Color.BGR.string('#ffffff')
            window.send(LVM_SETTEXTCOLOR, 0, int(color))
            color = Color.BGR.string('#2b2b2b')
            window.send(LVM_SETTEXTBKCOLOR, 0, int(color))
            window.send(LVM_SETBKCOLOR, 0, int(color))
        return None
    
    def _darkmode_treeview_hook(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if not self._DARK_MODE_ENABLED:
            return None
        if msg == WM_NOTIFY:
            nm = i_cast_value(lParam, NMHDR)
            code = INT(nm.code).value
            
            if code == NM_CUSTOMDRAW:
                nmcd = i_cast_value(lParam, NMCUSTOMDRAW)
                stage = nmcd.dwDrawStage
                
                if stage == CDDS_PREPAINT:
                    return CDRF_NOTIFYITEMDRAW
                elif stage == CDDS_ITEMPREPAINT:
                    dc = DC.foreign_owner(nmcd.hdc)
                    dc.text_color = Color.BGR.string('#ffffff')
                    return CDRF_DODEFAULT
        elif msg == WM_THEMECHANGED:
            window = Window.foreign(hwnd)
            color = Color.BGR.string('#ffffff')
            window.send(TVM_SETTEXTCOLOR, 0, int(color))
            color = Color.BGR.string('#2b2b2b')
            window.send(TVM_SETBKCOLOR, 0, int(color))
        elif msg == WM_MOUSEMOVE:
            result = DefSubclassProc(hwnd, msg, wParam, lParam)
            window = Window.foreign(hwnd)
            tooltips = Window.foreign(window.send(TVM_GETTOOLTIPS))
            if tooltips:
                if 'WinAbs.ToolTips_ThemeApplied' not in tooltips.props:
                    tooltips.props['WinAbs.ToolTips_ThemeApplied'] = True
                    tooltips.set_window_theme('DarkMode_Explorer')
            return result
        return None
    
    def _darkmode_statusbar_hook(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if not self._DARK_MODE_ENABLED:
            return None
        if msg == WM_PAINT:
            window = Window.foreign(hwnd)
            with PaintDC(hwnd) as dc:
                client = window.client_rect
                top_border = Rect.create(client.left, client.top, client.width, 1)
                old_bkcolor = dc.set_bk_color(Color.BGR.string('#3a3a3a'))
                dc.text_out(0, 0, '', ETO_OPAQUE, top_border)
                client.top += 1
                dc.bk_color = Color.BGR.string('#202020')
                dc.text_out(0, 0, '', ETO_OPAQUE, client)
                dc.bk_color = Color.BGR.string('#3a3a3a')
                count = window.send(SB_GETPARTS, lParam=NULL)
                buf = (INT * count)()
                window.send(SB_GETPARTS, count, buf)
                parts = list(buf)
                with dc.set_bk_mode_ex(TRANSPARENT):
                    with dc.set_text_color_ex(Color.BGR.string('#f0f0f0')):
                        rect = Rect()
                        for i, part in enumerate(parts):
                            window.send(SB_GETRECT, i, rect.ref())
                            if part != -1:
                                border = Rect.create(rect.right + 1, rect.top, 1, rect.height - 1)
                                dc.text_out(0, 0, '', ETO_OPAQUE, border)
                            
                            result = window.send(SB_GETTEXTLENGTHW, i)
                            symbols = LOWORD(result)
                            buf = create_unicode_buffer(symbols)
                            window.send(SB_GETTEXTW, i, buf)
                            
                            logfont = VisualStyleElements.Status.Pane.NORMAL.get_system_font(TMT_STATUSFONT, hwnd)
                            with Font.indirect(logfont) as font, dc.select_ex(font):
                                rect.left += 2
                                dc.draw_text(buf.value, rect, DT_SINGLELINE | DT_LEFT | DT_VCENTER)
                dc.bk_color = Color.BGR.string('#5a5a5a')
                # 3 Vertical blocks
                rect = Rect.create(client.right - 2 - 3, client.bottom - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                rect = Rect.create(client.right - 2 - 3, client.bottom - 2 - 3 - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                rect = Rect.create(client.right - 2 - 3, client.bottom - 2 - 3 - 2 - 3 - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                # 2 Vertical blocks
                rect = Rect.create(client.right - 2 - 3 - 2 - 3, client.bottom - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                rect = Rect.create(client.right - 2 - 3 - 2 - 3, client.bottom - 2 - 3 - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                # 1 Vertical block
                rect = Rect.create(client.right - 2 - 3 - 2 - 3 - 2 - 3, client.bottom - 2 - 3, 3, 3)
                dc.text_out(0, 0, '', ETO_OPAQUE, rect)
                dc.bk_color = old_bkcolor
                
            return 0
        return None
    
    def _draw_darkmode_menu_bottomline(self, dc: DC | None = None):
        if not self.menu:
            return
        if dc is None:
            dc = DC.window(self)
        
        client = self.client_rect
        client = Rect.build(*self.map(None, client.split()))
        
        rect = self.rect
        client.offset_rect(-rect.left, -rect.top)
        
        client.bottom = client.top
        client.top -= 1
        
        with dc.set_bk_color_ex(Color.BGR.string('#2b2b2b')):
            dc.text_out(0, 0, '', ETO_OPAQUE, client)
            
    def on_uah_draw_menu(self, menu: UAHMENU) -> bool:
        if not self._DARK_MODE_ENABLED:
            self.send_message_indirect(WSMT_DEFAULT, self.last_message)
            return True
        
        dc = DC.foreign_owner(menu.hdc)
        self._draw_darkmode_menu_bottomline(dc)
        bar = self.get_menu_bar_info().rect
        rect = self.rect
        bar.offset_rect(-rect.left, -rect.top)
        with dc.set_bk_color_ex(Color.BGR.string('#2b2b2b')):
            dc.text_out(0, 0, '', ETO_OPAQUE, bar)
        return True
    
    def on_uah_draw_menu_item(self, item: UAHDRAWMENUITEM):
        if not self._DARK_MODE_ENABLED:
            self.send_message_indirect(WSMT_DEFAULT, self.last_message)
            return True
        
        menu = Menu.foreign_owner(item.um.hmenu)
        dc = DC.foreign_owner(item.um.hdc)
        
        self._draw_darkmode_menu_bottomline(dc)
        
        info = menu.item_info(item.umi.iPosition, MIIM_STRING)
        flags = DT_SINGLELINE | DT_CENTER | DT_VCENTER
        
        if item.dis.itemState & ODS_HOTLIGHT:
            background = Color.BGR.string('#414141')
        else:
            background = Color.BGR.string('#2b2b2b')
        
        if item.dis.itemState & ODS_NOACCEL:
            flags |= DT_HIDEPREFIX
        
        options = DTTOPTS()
        options.crText = int(Color.BGR.string('#ffffff'))
        options.dwFlags = DTT_TEXTCOLOR
        
        with dc.set_bk_color_ex(background):
            dc.text_out(0, 0, '', ETO_OPAQUE, item.dis.rcItem)
        vs = VisualStyleElements.Menu.BarItem.NORMAL
        vs.draw_text(dc, info.dwTypeData.value, flags, item.dis.rcItem, options, self)
        
        return True
    
    def on_nc_activate(self, active: bool, window: Window | None) -> bool:
        self.send_message_indirect(WSMT_DEFAULT, self.last_message)
        if self._DARK_MODE_ENABLED:
            self._draw_darkmode_menu_bottomline()
        return True
    
    def on_nc_paint(self, dc: DC, region: Region) -> bool:
        self.send_message_indirect(WSMT_DEFAULT, self.last_message)
        if self._DARK_MODE_ENABLED:
            self._draw_darkmode_menu_bottomline(dc)
        return True
    
DarkModeWindow._init_darkmode_window()