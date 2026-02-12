from .minwindef import *

from .defbase import *

from . import cpreproc

from .winbase import MAKEINTATOM

from .windef import HWINEVENTHOOK

from . import wingdi as _

from .winnt import (
    LONG_PTR, ULONG_PTR, INT_PTR, 
    UINT_PTR, ACCESS_MASK, LPSECURITY_ATTRIBUTES,
    PVOID, PSECURITY_DESCRIPTOR, PSECURITY_INFORMATION,
    POINTS, GUID, UCHAR, 
    PDWORD_PTR, LUID, LPCGUID,
    UINT32, UINT64, INT32,
    PUINT32, UINT16, DWORD_PTR,
    HandleToULong, NULL,
    CALLBACK, WINAPI,
    MAKELONG, MAXUINT_PTR, VOID, 
    LOWORD, HIWORD, TRUE
)

if cpreproc.pragma_once("_WINUSER_"):
    if cpreproc.ifndef("NOUSER"):

        user32 = W_WinDLL("user32.dll")

        LRESULT = LONG_PTR

        HDWP = HANDLE
        HCURSOR = HANDLE
        MENUTEMPLATEA = None
        MENUTEMPLATEW = None

        MENUTEMPLATE = unicode(MENUTEMPLATEW, MENUTEMPLATEA)
            
        LPMENUTEMPLATEA = LPVOID
        LPMENUTEMPLATEW = LPVOID

        LPMENUTEMPLATE = unicode(LPMENUTEMPLATEW, LPMENUTEMPLATEA)
            
        WNDPROC = CALLBACK(LRESULT, HWND, UINT, WPARAM, LPARAM)
        DLGPROC = CALLBACK(INT_PTR, HWND, UINT, WPARAM, LPARAM)
        TIMERPROC = CALLBACK(VOID, HWND, UINT, UINT_PTR, DWORD)

        GRAYSTRINGPROC = CALLBACK(BOOL, HDC, LPARAM, INT)
        WNDENUMPROC = CALLBACK(BOOL, HWND, LPARAM)
        HOOKPROC = CALLBACK(LRESULT, INT, WPARAM, LPARAM)
        SENDASYNCPROC = CALLBACK(VOID, HWND, UINT, ULONG_PTR, LRESULT)

        PROPENUMPROCA = CALLBACK(BOOL, HWND, LPCSTR, HANDLE)
        PROPENUMPROCW = CALLBACK(BOOL, HWND, LPCWSTR, HANDLE)

        PROPENUMPROCEXA = CALLBACK(BOOL, HWND, LPSTR, HANDLE, ULONG_PTR)
        PROPENUMPROCEXW = CALLBACK(BOOL, HWND, LPWSTR, HANDLE, ULONG_PTR)

        EDITWORDBREAKPROCA = CALLBACK(INT, LPSTR, INT, INT, INT)
        EDITWORDBREAKPROCW = CALLBACK(INT, LPSTR, INT, INT, INT)

        DRAWSTATEPROC = CALLBACK(BOOL, HDC, LPARAM, WPARAM, INT, INT)

        PROPENUMPROC = unicode(PROPENUMPROCW, PROPENUMPROCA)
        PROPENUMPROCEX = unicode(PROPENUMPROCEXW, PROPENUMPROCEXA)
        EDITWORDBREAKPROC = unicode(EDITWORDBREAKPROCW, EDITWORDBREAKPROCA)
            
        NAMEENUMPROCA = CALLBACK(BOOL, LPSTR, LPARAM)
        NAMEENUMPROCW = CALLBACK(BOOL, LPWSTR, LPARAM)

        WINSTAENUMPROCA = NAMEENUMPROCA
        DESKTOPENUMPROCA = NAMEENUMPROCA
        WINSTAENUMPROCW = NAMEENUMPROCW
        DESKTOPENUMPROCW = NAMEENUMPROCW

        WINSTAENUMPROC = unicode(WINSTAENUMPROCW, WINSTAENUMPROCA)
        DESKTOPENUMPROC = unicode(DESKTOPENUMPROCW, DESKTOPENUMPROCA)

        class tagCREATESTRUCTA(CStructure):
            _fields_ = [
                ("lpCreateParams", LPVOID),
                ("hInstance", HINSTANCE),
                ("hMenu", HMENU),
                ("hwndParent", HWND),
                ("cy", INT),
                ("cx", INT),
                ("y", INT),
                ("x", INT),
                ("style", LONG),
                ("lpszName", LPCSTR),
                ("lpszClass", LPCSTR),
                ("dwExStyle", DWORD)
            ]
            
            lpCreateParams: LPVOID
            hInstance: int
            hMenu: int
            hwndParent: int
            cy: int
            cx: int
            y: int
            x: int
            style: int
            lpszName: bytes
            lpszClass: bytes
            dwExStyle: int
            
        CREATESTRUCTA = tagCREATESTRUCTA
        LPCREATESTRUCTA = POINTER(CREATESTRUCTA)

        class tagCREATESTRUCTW(CStructure):
            _fields_ = [
                ("lpCreateParams", LPVOID),
                ("hInstance", HINSTANCE),
                ("hMenu", HMENU),
                ("hwndParent", HWND),
                ("cy", INT),
                ("cx", INT),
                ("y", INT),
                ("x", INT),
                ("style", LONG),
                ("lpszName", LPCWSTR),
                ("lpszClass", LPCWSTR),
                ("dwExStyle", DWORD)
            ]
            
            lpCreateParams: LPVOID
            hInstance: int
            hMenu: int
            hwndParent: int
            cy: int
            cx: int
            y: int
            x: int
            style: int
            lpszName: str
            lpszClass: str
            dwExStyle: int
            
        CREATESTRUCTW = tagCREATESTRUCTW
        LPCREATESTRUCTW = POINTER(CREATESTRUCTW)

        CREATESTRUCT = unicode(CREATESTRUCTW, CREATESTRUCTA)
            
        IS_INTRESOURCE = lambda _r: ((ULONG_PTR(_r).value >> 16) == 0)
        MAKEINTRESOURCEA = lambda i: cast(ULONG_PTR(WORD(i).value).value, PVOID)
        MAKEINTRESOURCEW = lambda i: cast(ULONG_PTR(WORD(i).value).value, PVOID)

        MAKEINTRESOURCE = unicode(MAKEINTRESOURCEW, MAKEINTRESOURCEA)

        if cpreproc.ifndef("NORESOURCE"):

            """
            * Predefined Resource Types
            """

            RT_CURSOR = MAKEINTRESOURCE(1)
            RT_BITMAP = MAKEINTRESOURCE(2)
            RT_ICON = MAKEINTRESOURCE(3)
            RT_MENU = MAKEINTRESOURCE(4)
            RT_DIALOG = MAKEINTRESOURCE(5)
            RT_STRING = MAKEINTRESOURCE(6)
            RT_FONTDIR = MAKEINTRESOURCE(7)
            RT_FONT = MAKEINTRESOURCE(8)
            RT_ACCELERATOR = MAKEINTRESOURCE(9)
            RT_RCDATA = MAKEINTRESOURCE(10)
            RT_MESSAGETABLE = MAKEINTRESOURCE(11)
            DIFFERENCE = 11
            RT_GROUP_CURSOR = MAKEINTRESOURCE(ULONG_PTR(RT_CURSOR.value).value + DIFFERENCE)
            RT_GROUP_ICON = MAKEINTRESOURCE(ULONG_PTR(RT_ICON.value).value + DIFFERENCE)
            RT_VERSION = MAKEINTRESOURCE(16)
            RT_DLGINCLUDE = MAKEINTRESOURCE(17)
            RT_PLUGPLAY = MAKEINTRESOURCE(19)
            RT_VXD = MAKEINTRESOURCE(20)
            RT_ANICURSOR = MAKEINTRESOURCE(21)
            RT_ANIICON = MAKEINTRESOURCE(22)
        # WINVER >= 0x0400
        RT_HTML = MAKEINTRESOURCE(23)
        if cpreproc.ifdef("RC_INVOKED"):
            RT_MANIFEST = 24
            CREATEPROCESS_MANIFEST_RESOURCE_ID = 1
            ISOLATIONAWARE_MANIFEST_RESOURCE_ID = 2
            ISOLATIONAWARE_NOSTATICIMPORT_MANIFEST_RESOURCE_ID = 3
            ISOLATIONPOLICY_MANIFEST_RESOURCE_ID = 4
            ISOLATIONPOLICY_BROWSER_MANIFEST_RESOURCE_ID = 5
            MINIMUM_RESERVED_MANIFEST_RESOURCE_ID = 1 # inclusive
            MAXIMUM_RESERVED_MANIFEST_RESOURCE_ID = 16 # inclusive
        else: # RC_INVOKED
            RT_MANIFEST = MAKEINTRESOURCE(24)
            CREATEPROCESS_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(1)
            ISOLATIONAWARE_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(2)
            ISOLATIONAWARE_NOSTATICIMPORT_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(3)
            ISOLATIONPOLICY_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(4)
            ISOLATIONPOLICY_BROWSER_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(5)
            MINIMUM_RESERVED_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(1) #inclusive
            MAXIMUM_RESERVED_MANIFEST_RESOURCE_ID = MAKEINTRESOURCE(16) #inclusive
        # RC_INVOKED
        # !NORESOURCE
            
        SETWALLPAPER_DEFAULT = LPWSTR(-1)
        if cpreproc.ifndef("NOSCROLL"):

            """
            * Scroll Bar Constants
            """

            SB_HORZ = 0
            SB_VERT = 1
            SB_CTL = 2
            SB_BOTH = 3

            """
            * Scroll Bar Commands
            """

            SB_LINEUP = 0
            SB_LINELEFT = 0
            SB_LINEDOWN = 1
            SB_LINERIGHT = 1
            SB_PAGEUP = 2
            SB_PAGELEFT = 2
            SB_PAGEDOWN = 3
            SB_PAGERIGHT = 3
            SB_THUMBPOSITION = 4
            SB_THUMBTRACK = 5
            SB_TOP = 6
            SB_LEFT = 6
            SB_BOTTOM = 7
            SB_RIGHT = 7
            SB_ENDSCROLL = 8
        if cpreproc.ifndef("NOSHOWWINDOW"):

            """
            * ShowWindow() Commands
            """

            SW_HIDE = 0
            SW_SHOWNORMAL = 1
            SW_NORMAL = 1
            SW_SHOWMINIMIZED = 2
            SW_SHOWMAXIMIZED = 3
            SW_MAXIMIZE = 3
            SW_SHOWNOACTIVATE = 4
            SW_SHOW = 5
            SW_MINIMIZE = 6
            SW_SHOWMINNOACTIVE = 7
            SW_SHOWNA = 8
            SW_RESTORE = 9
            SW_SHOWDEFAULT = 10
            SW_FORCEMINIMIZE = 11
            SW_MAX = 11

            """
            * Old ShowWindow() Commands
            """

            HIDE_WINDOW = 0
            SHOW_OPENWINDOW = 1
            SHOW_ICONWINDOW = 2
            SHOW_FULLSCREEN = 3
            SHOW_OPENNOACTIVATE = 4

            """
            * Identifiers for the WM_SHOWWINDOW message
            """

            SW_PARENTCLOSING = 1
            SW_OTHERZOOM = 2
            SW_PARENTOPENING = 3
            SW_OTHERUNZOOM = 4

        """
        * AnimateWindow() Commands
        """

        AW_HOR_POSITIVE = 0x00000001
        AW_HOR_NEGATIVE = 0x00000002
        AW_VER_POSITIVE = 0x00000004
        AW_VER_NEGATIVE = 0x00000008
        AW_CENTER = 0x00000010
        AW_HIDE = 0x00010000
        AW_ACTIVATE = 0x00020000
        AW_SLIDE = 0x00040000
        AW_BLEND = 0x00080000

        """
        * WM_KEYUP/DOWN/CHAR HIWORD(lParam) flags
        """

        KF_EXTENDED = 0x0100
        KF_DLGMODE = 0x0800
        KF_MENUMODE = 0x1000
        KF_ALTDOWN = 0x2000
        KF_REPEAT = 0x4000
        KF_UP = 0x8000
        if cpreproc.ifndef("NOVIRTUALKEYCODES"):

            """
            * Virtual Keys, Standard Set
            """

            VK_LBUTTON = 0x01
            VK_RBUTTON = 0x02
            VK_CANCEL = 0x03
            VK_MBUTTON = 0x04
            VK_XBUTTON1 = 0x05
            VK_XBUTTON2 = 0x06

        """
        * 0x07 : reserved
        """

        VK_BACK = 0x08
        VK_TAB = 0x09

        """
        * 0x0A - 0x0B : reserved
        """

        VK_CLEAR = 0x0C
        VK_RETURN = 0x0D

        """
        * 0x0E - 0x0F : unassigned
        """

        VK_SHIFT = 0x10
        VK_CONTROL = 0x11
        VK_MENU = 0x12
        VK_PAUSE = 0x13
        VK_CAPITAL = 0x14
        VK_KANA = 0x15
        VK_HANGEUL = 0x15
        VK_HANGUL = 0x15
        VK_IME_ON = 0x16
        VK_JUNJA = 0x17
        VK_FINAL = 0x18
        VK_HANJA = 0x19
        VK_KANJI = 0x19
        VK_IME_OFF = 0x1A
        VK_ESCAPE = 0x1B
        VK_CONVERT = 0x1C
        VK_NONCONVERT = 0x1D
        VK_ACCEPT = 0x1E
        VK_MODECHANGE = 0x1F
        VK_SPACE = 0x20
        VK_PRIOR = 0x21
        VK_NEXT = 0x22
        VK_END = 0x23
        VK_HOME = 0x24
        VK_LEFT = 0x25
        VK_UP = 0x26
        VK_RIGHT = 0x27
        VK_DOWN = 0x28
        VK_SELECT = 0x29
        VK_PRINT = 0x2A
        VK_EXECUTE = 0x2B
        VK_SNAPSHOT = 0x2C
        VK_INSERT = 0x2D
        VK_DELETE = 0x2E
        VK_HELP = 0x2F

        """
        * VK_0 - VK_9 are the same as ASCII '0' - '9' (0x30 - 0x39)
        * 0x3A - 0x40 : unassigned
        * VK_A - VK_Z are the same as ASCII 'A' - 'Z' (0x41 - 0x5A)
        """

        VK_LWIN = 0x5B
        VK_RWIN = 0x5C
        VK_APPS = 0x5D

        """
        * 0x5E : reserved
        """

        VK_SLEEP = 0x5F
        VK_NUMPAD0 = 0x60
        VK_NUMPAD1 = 0x61
        VK_NUMPAD2 = 0x62
        VK_NUMPAD3 = 0x63
        VK_NUMPAD4 = 0x64
        VK_NUMPAD5 = 0x65
        VK_NUMPAD6 = 0x66
        VK_NUMPAD7 = 0x67
        VK_NUMPAD8 = 0x68
        VK_NUMPAD9 = 0x69
        VK_MULTIPLY = 0x6A
        VK_ADD = 0x6B
        VK_SEPARATOR = 0x6C
        VK_SUBTRACT = 0x6D
        VK_DECIMAL = 0x6E
        VK_DIVIDE = 0x6F
        VK_F1 = 0x70
        VK_F2 = 0x71
        VK_F3 = 0x72
        VK_F4 = 0x73
        VK_F5 = 0x74
        VK_F6 = 0x75
        VK_F7 = 0x76
        VK_F8 = 0x77
        VK_F9 = 0x78
        VK_F10 = 0x79
        VK_F11 = 0x7A
        VK_F12 = 0x7B
        VK_F13 = 0x7C
        VK_F14 = 0x7D
        VK_F15 = 0x7E
        VK_F16 = 0x7F
        VK_F17 = 0x80
        VK_F18 = 0x81
        VK_F19 = 0x82
        VK_F20 = 0x83
        VK_F21 = 0x84
        VK_F22 = 0x85
        VK_F23 = 0x86
        VK_F24 = 0x87

        """
        * 0x88 - 0x8F : UI navigation
        """

        VK_NAVIGATION_VIEW = 0x88 # reserved
        VK_NAVIGATION_MENU = 0x89 # reserved
        VK_NAVIGATION_UP = 0x8A # reserved
        VK_NAVIGATION_DOWN = 0x8B # reserved
        VK_NAVIGATION_LEFT = 0x8C # reserved
        VK_NAVIGATION_RIGHT = 0x8D # reserved
        VK_NAVIGATION_ACCEPT = 0x8E # reserved
        VK_NAVIGATION_CANCEL = 0x8F # reserved
        VK_NUMLOCK = 0x90
        VK_SCROLL = 0x91

        """
        * NEC PC-9800 kbd definitions
        """

        VK_OEM_NEC_EQUAL = 0x92 # '=' key on numpad

        """
        * Fujitsu/OASYS kbd definitions
        """

        VK_OEM_FJ_JISHO = 0x92 # 'Dictionary' key
        VK_OEM_FJ_MASSHOU = 0x93 # 'Unregister word' key
        VK_OEM_FJ_TOUROKU = 0x94 # 'Register word' key
        VK_OEM_FJ_LOYA = 0x95 # 'Left OYAYUBI' key
        VK_OEM_FJ_ROYA = 0x96 # 'Right OYAYUBI' key

        """
        * 0x97 - 0x9F : unassigned
        """


        """
        * VK_L* & VK_R* - left and right Alt, Ctrl and Shift virtual keys.
        * Used only as parameters to GetAsyncKeyState() and GetKeyState().
        * No other API or message will distinguish left and right keys in this way.
        """

        VK_LSHIFT = 0xA0
        VK_RSHIFT = 0xA1
        VK_LCONTROL = 0xA2
        VK_RCONTROL = 0xA3
        VK_LMENU = 0xA4
        VK_RMENU = 0xA5
        VK_BROWSER_BACK = 0xA6
        VK_BROWSER_FORWARD = 0xA7
        VK_BROWSER_REFRESH = 0xA8
        VK_BROWSER_STOP = 0xA9
        VK_BROWSER_SEARCH = 0xAA
        VK_BROWSER_FAVORITES = 0xAB
        VK_BROWSER_HOME = 0xAC
        VK_VOLUME_MUTE = 0xAD
        VK_VOLUME_DOWN = 0xAE
        VK_VOLUME_UP = 0xAF
        VK_MEDIA_NEXT_TRACK = 0xB0
        VK_MEDIA_PREV_TRACK = 0xB1
        VK_MEDIA_STOP = 0xB2
        VK_MEDIA_PLAY_PAUSE = 0xB3
        VK_LAUNCH_MAIL = 0xB4
        VK_LAUNCH_MEDIA_SELECT = 0xB5
        VK_LAUNCH_APP1 = 0xB6
        VK_LAUNCH_APP2 = 0xB7

        """
        * 0xB8 - 0xB9 : reserved
        """

        VK_OEM_1 = 0xBA # ';:' for US
        VK_OEM_PLUS = 0xBB # '+' any country
        VK_OEM_COMMA = 0xBC # ',' any country
        VK_OEM_MINUS = 0xBD # '-' any country
        VK_OEM_PERIOD = 0xBE # '.' any country
        VK_OEM_2 = 0xBF # '/?' for US
        VK_OEM_3 = 0xC0 # '`~' for US

        """
        * 0xC1 - 0xC2 : reserved
        """


        """
        * 0xC3 - 0xDA : Gamepad input
        """

        VK_GAMEPAD_A = 0xC3 # reserved
        VK_GAMEPAD_B = 0xC4 # reserved
        VK_GAMEPAD_X = 0xC5 # reserved
        VK_GAMEPAD_Y = 0xC6 # reserved
        VK_GAMEPAD_RIGHT_SHOULDER = 0xC7 # reserved
        VK_GAMEPAD_LEFT_SHOULDER = 0xC8 # reserved
        VK_GAMEPAD_LEFT_TRIGGER = 0xC9 # reserved
        VK_GAMEPAD_RIGHT_TRIGGER = 0xCA # reserved
        VK_GAMEPAD_DPAD_UP = 0xCB # reserved
        VK_GAMEPAD_DPAD_DOWN = 0xCC # reserved
        VK_GAMEPAD_DPAD_LEFT = 0xCD # reserved
        VK_GAMEPAD_DPAD_RIGHT = 0xCE # reserved
        VK_GAMEPAD_MENU = 0xCF # reserved
        VK_GAMEPAD_VIEW = 0xD0 # reserved
        VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON = 0xD1 # reserved
        VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 0xD2 # reserved
        VK_GAMEPAD_LEFT_THUMBSTICK_UP = 0xD3 # reserved
        VK_GAMEPAD_LEFT_THUMBSTICK_DOWN = 0xD4 # reserved
        VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT = 0xD5 # reserved
        VK_GAMEPAD_LEFT_THUMBSTICK_LEFT = 0xD6 # reserved
        VK_GAMEPAD_RIGHT_THUMBSTICK_UP = 0xD7 # reserved
        VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN = 0xD8 # reserved
        VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT = 0xD9 # reserved
        VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT = 0xDA # reserved
        VK_OEM_4 = 0xDB #  '[{' for US
        VK_OEM_5 = 0xDC #  '\|' for US
        VK_OEM_6 = 0xDD #  ']}' for US
        VK_OEM_7 = 0xDE #  ''"' for US
        VK_OEM_8 = 0xDF

        """
        * 0xE0 : reserved
        """


        """
        * Various extended or enhanced keyboards
        """

        VK_OEM_AX = 0xE1 #  'AX' key on Japanese AX kbd
        VK_OEM_102 = 0xE2 #  "<>" or "\|" on RT 102-key kbd.
        VK_ICO_HELP = 0xE3 #  Help key on ICO
        VK_ICO_00 = 0xE4 #  00 key on ICO
        VK_PROCESSKEY = 0xE5
        VK_ICO_CLEAR = 0xE6
        VK_PACKET = 0xE7

        """
        * 0xE8 : unassigned
        """


        """
        * Nokia/Ericsson definitions
        """

        VK_OEM_RESET = 0xE9
        VK_OEM_JUMP = 0xEA
        VK_OEM_PA1 = 0xEB
        VK_OEM_PA2 = 0xEC
        VK_OEM_PA3 = 0xED
        VK_OEM_WSCTRL = 0xEE
        VK_OEM_CUSEL = 0xEF
        VK_OEM_ATTN = 0xF0
        VK_OEM_FINISH = 0xF1
        VK_OEM_COPY = 0xF2
        VK_OEM_AUTO = 0xF3
        VK_OEM_ENLW = 0xF4
        VK_OEM_BACKTAB = 0xF5
        VK_ATTN = 0xF6
        VK_CRSEL = 0xF7
        VK_EXSEL = 0xF8
        VK_EREOF = 0xF9
        VK_PLAY = 0xFA
        VK_ZOOM = 0xFB
        VK_NONAME = 0xFC
        VK_PA1 = 0xFD
        VK_OEM_CLEAR = 0xFE

        """
        * 0xFF : reserved
        """

        if cpreproc.ifndef("NOWH"):

            """
            * SetWindowsHook() codes
            """

            WH_MIN = (-1)
            WH_MSGFILTER = (-1)
            WH_JOURNALRECORD = 0
            WH_JOURNALPLAYBACK = 1
            WH_KEYBOARD = 2
            WH_GETMESSAGE = 3
            WH_CALLWNDPROC = 4
            WH_CBT = 5
            WH_SYSMSGFILTER = 6
            WH_MOUSE = 7
            WH_HARDWARE = 8
            WH_DEBUG = 9
            WH_SHELL = 10
            WH_FOREGROUNDIDLE = 11
            WH_CALLWNDPROCRET = 12
            WH_KEYBOARD_LL = 13
            WH_MOUSE_LL = 14
            WH_MAX = 14
            WH_MINHOOK = WH_MIN
            WH_MAXHOOK = WH_MAX

            """
            * Hook Codes
            """

            HC_ACTION = 0
            HC_GETNEXT = 1
            HC_SKIP = 2
            HC_NOREMOVE = 3
            HC_NOREM = HC_NOREMOVE
            HC_SYSMODALON = 4
            HC_SYSMODALOFF = 5

            """
            * CBT Hook Codes
            """

            HCBT_MOVESIZE = 0
            HCBT_MINMAX = 1
            HCBT_QS = 2
            HCBT_CREATEWND = 3
            HCBT_DESTROYWND = 4
            HCBT_ACTIVATE = 5
            HCBT_CLICKSKIPPED = 6
            HCBT_KEYSKIPPED = 7
            HCBT_SYSCOMMAND = 8
            HCBT_SETFOCUS = 9

            # REGION *** Desktop Family ***

            """
            * HCBT_CREATEWND parameters pointed to by lParam
            """
            class tagCBT_CREATEWNDA(CStructure):
                _fields_ = [
                    ("lpcs", POINTER(tagCREATESTRUCTA)),
                    ("hwndInsertAfter", HWND)
                ]
                
                lpcs: IPointer[tagCREATESTRUCTA]
                hwndInsertAfter: int
                
            CBT_CREATEWNDA = tagCBT_CREATEWNDA
            LPCBT_CREATEWNDA = POINTER(CBT_CREATEWNDA)
            
            """
            * HCBT_CREATEWND parameters pointed to by lParam
            """
            class tagCBT_CREATEWNDW(CStructure):
                _fields_ = [
                    ("lpcs", POINTER(tagCREATESTRUCTW)),
                    ("hwndInsertAfter", HWND)
                ]
                
                lpcs: IPointer[tagCREATESTRUCTW]
                hwndInsertAfter: int
            CBT_CREATEWNDW = tagCBT_CREATEWNDW
            LPCBT_CREATEWNDW = POINTER(CBT_CREATEWNDW)
            
            CBT_CREATEWND = unicode(CBT_CREATEWNDW, CBT_CREATEWNDA)
            LPCBT_CREATEWND = unicode(LPCBT_CREATEWNDW, LPCBT_CREATEWNDA)

            """
            * HCBT_ACTIVATE structure pointed to by lParam
            """
            class tagCBTACTIVATESTRUCT(CStructure):
                _fields_ = [
                    ("fMouse", BOOL),
                    ("hWndActive", HWND)
                ]
                
                fMouse: bool
                hWndActive: int
                
            CBTACTIVATESTRUCT = tagCBTACTIVATESTRUCT
            LPCBTACTIVATESTRUCT = POINTER(CBTACTIVATESTRUCT)
            
            # REGION ***

            # REGION *** Desktop Family ***

            """
            * WTSSESSION_NOTIFICATION struct pointed by lParam, for WM_WTSSESSION_CHANGE
            """
            class tagWTSSESSION_NOTIFICATION(CStructure):
                _fields_ = [
                    ("cbSize", DWORD),
                    ("dwSessionId", DWORD)
                ]
                
                cbSize: int
                dwSessionId: int
                
            WTSSESSION_NOTIFICATION = tagWTSSESSION_NOTIFICATION
            PWTSSESSION_NOTIFICATION = POINTER(WTSSESSION_NOTIFICATION)
            
            # REGION ***
            
            """
            * codes passed in WPARAM for WM_WTSSESSION_CHANGE
            """

            WTS_CONSOLE_CONNECT = 0x1
            WTS_CONSOLE_DISCONNECT = 0x2
            WTS_REMOTE_CONNECT = 0x3
            WTS_REMOTE_DISCONNECT = 0x4
            WTS_SESSION_LOGON = 0x5
            WTS_SESSION_LOGOFF = 0x6
            WTS_SESSION_LOCK = 0x7
            WTS_SESSION_UNLOCK = 0x8
            WTS_SESSION_REMOTE_CONTROL = 0x9
            WTS_SESSION_CREATE = 0xa
            WTS_SESSION_TERMINATE = 0xb

            """
            * WH_MSGFILTER Filter Proc Codes
            """

            MSGF_DIALOGBOX = 0
            MSGF_MESSAGEBOX = 1
            MSGF_MENU = 2
            MSGF_SCROLLBAR = 5
            MSGF_NEXTWINDOW = 6
            MSGF_MAX = 8 # unused
            MSGF_USER = 4096

            """
            * Shell support
            """

            HSHELL_WINDOWCREATED = 1
            HSHELL_WINDOWDESTROYED = 2
            HSHELL_ACTIVATESHELLWINDOW = 3
            HSHELL_WINDOWACTIVATED = 4
            HSHELL_GETMINRECT = 5
            HSHELL_REDRAW = 6
            HSHELL_TASKMAN = 7
            HSHELL_LANGUAGE = 8
            HSHELL_SYSMENU = 9
            HSHELL_ENDTASK = 10
            HSHELL_ACCESSIBILITYSTATE = 11
            HSHELL_APPCOMMAND = 12
            HSHELL_WINDOWREPLACED = 13
            HSHELL_WINDOWREPLACING = 14
            HSHELL_MONITORCHANGED = 16
            HSHELL_HIGHBIT = 0x8000
            HSHELL_FLASH = (HSHELL_REDRAW|HSHELL_HIGHBIT)
            HSHELL_RUDEAPPACTIVATED = (HSHELL_WINDOWACTIVATED|HSHELL_HIGHBIT)
            APPCOMMAND_BROWSER_BACKWARD = 1
            APPCOMMAND_BROWSER_FORWARD = 2
            APPCOMMAND_BROWSER_REFRESH = 3
            APPCOMMAND_BROWSER_STOP = 4
            APPCOMMAND_BROWSER_SEARCH = 5
            APPCOMMAND_BROWSER_FAVORITES = 6
            APPCOMMAND_BROWSER_HOME = 7
            APPCOMMAND_VOLUME_MUTE = 8
            APPCOMMAND_VOLUME_DOWN = 9
            APPCOMMAND_VOLUME_UP = 10
            APPCOMMAND_MEDIA_NEXTTRACK = 11
            APPCOMMAND_MEDIA_PREVIOUSTRACK = 12
            APPCOMMAND_MEDIA_STOP = 13
            APPCOMMAND_MEDIA_PLAY_PAUSE = 14
            APPCOMMAND_LAUNCH_MAIL = 15
            APPCOMMAND_LAUNCH_MEDIA_SELECT = 16
            APPCOMMAND_LAUNCH_APP1 = 17
            APPCOMMAND_LAUNCH_APP2 = 18
            APPCOMMAND_BASS_DOWN = 19
            APPCOMMAND_BASS_BOOST = 20
            APPCOMMAND_BASS_UP = 21
            APPCOMMAND_TREBLE_DOWN = 22
            APPCOMMAND_TREBLE_UP = 23
            APPCOMMAND_MICROPHONE_VOLUME_MUTE = 24
            APPCOMMAND_MICROPHONE_VOLUME_DOWN = 25
            APPCOMMAND_MICROPHONE_VOLUME_UP = 26
            APPCOMMAND_HELP = 27
            APPCOMMAND_FIND = 28
            APPCOMMAND_NEW = 29
            APPCOMMAND_OPEN = 30
            APPCOMMAND_CLOSE = 31
            APPCOMMAND_SAVE = 32
            APPCOMMAND_PRINT = 33
            APPCOMMAND_UNDO = 34
            APPCOMMAND_REDO = 35
            APPCOMMAND_COPY = 36
            APPCOMMAND_CUT = 37
            APPCOMMAND_PASTE = 38
            APPCOMMAND_REPLY_TO_MAIL = 39
            APPCOMMAND_FORWARD_MAIL = 40
            APPCOMMAND_SEND_MAIL = 41
            APPCOMMAND_SPELL_CHECK = 42
            APPCOMMAND_DICTATE_OR_COMMAND_CONTROL_TOGGLE = 43
            APPCOMMAND_MIC_ON_OFF_TOGGLE = 44
            APPCOMMAND_CORRECTION_LIST = 45
            APPCOMMAND_MEDIA_PLAY = 46
            APPCOMMAND_MEDIA_PAUSE = 47
            APPCOMMAND_MEDIA_RECORD = 48
            APPCOMMAND_MEDIA_FAST_FORWARD = 49
            APPCOMMAND_MEDIA_REWIND = 50
            APPCOMMAND_MEDIA_CHANNEL_UP = 51
            APPCOMMAND_MEDIA_CHANNEL_DOWN = 52
            APPCOMMAND_DELETE = 53
            APPCOMMAND_DWM_FLIP3D = 54
            FAPPCOMMAND_MOUSE = 0x8000
            FAPPCOMMAND_KEY = 0
            FAPPCOMMAND_OEM = 0x1000
            FAPPCOMMAND_MASK = 0xF000
            GET_APPCOMMAND_LPARAM = lambda lParam: (SHORT(HIWORD(lParam) & ~FAPPCOMMAND_MASK)).value
            GET_DEVICE_LPARAM = lambda lParam: (WORD(HIWORD(lParam) & FAPPCOMMAND_MASK)).value
            GET_MOUSEORKEY_LPARAM = GET_DEVICE_LPARAM
            GET_FLAGS_LPARAM = lambda lParam: (LOWORD(lParam))
            GET_KEYSTATE_LPARAM = lambda lParam: GET_FLAGS_LPARAM(lParam)

            # REGION *** Desktop Family ***
            
            class SHELLHOOKINFO(CStructure):
                _fields_ = [
                    ('hwnd', HWND),
                    ('rc', RECT)
                ]
                
                hwnd: int
                rc: RECT
            
            SHELLHOOKINFO = SHELLHOOKINFO
            PSHELLHOOKINFO = POINTER(SHELLHOOKINFO)
            LPSHELLHOOKINFO = POINTER(SHELLHOOKINFO)

            """
            * Message Structure used in Journaling
            """
            class tagEVENTMSG(CStructure):
                _fields_ = [
                    ('message', UINT),
                    ('paramL', UINT),
                    ('paramH', UINT),
                    ('time', DWORD),
                    ('hwnd', HWND)
                ]
                
                message: int
                paramL: int
                paramH: int
                time: int
                hwnd: int
                
            EVENTMSG = tagEVENTMSG
            PEVENTMSG = POINTER(EVENTMSG)

            PEVENTMSGMSG = POINTER(tagEVENTMSG)
            LPEVENTMSG = POINTER(tagEVENTMSG)
            LPEVENTMSGMSG = POINTER(tagEVENTMSG)
            NPEVENTMSGMSG = POINTER(tagEVENTMSG)
            NPEVENTMSGMSGMSG = POINTER(tagEVENTMSG)

            """
            * Message structure used by WH_CALLWNDPROC
            """
            class tagCWPSTRUCT(CStructure):
                _fields_ = [
                    ('lParam', LPARAM),
                    ('wParam', WPARAM),
                    ('message', UINT),
                    ('hwnd', HWND)
                ]
                
                lParam: int
                wParam: int
                message: int
                hwnd: int

            CWPSTRUCT = tagCWPSTRUCT
            PCWPSTRUCT = POINTER(CWPSTRUCT)

            LPCWPSTRUCT = POINTER(tagCWPSTRUCT)
            
            """
            * Message structure used by WH_CALLWNDPROCRET
            """
            class tagCWPRETSTRUCT(CStructure):
                _fields_ = [
                    ("lResult", LRESULT),
                    ("lParam", LPARAM),
                    ("wParam", WPARAM),
                    ("message", UINT),
                    ("hwnd", HWND)
                ]
                
                lResult: int
                lParam: int
                wParam: int
                message: int
                hwnd: int
                
            CWPRETSTRUCT = tagCWPRETSTRUCT
            PCWPRETSTRUCT = POINTER(CWPRETSTRUCT)
            NPCWPRETSTRUCT = PCWPRETSTRUCT
            LPCWPRETSTRUCT = PCWPRETSTRUCT
            
            # REGION ***
            
            LLKHF_EXTENDED = (KF_EXTENDED >> 8) # 0x00000001
            LLKHF_INJECTED = 0x00000010
            LLKHF_ALTDOWN = (KF_ALTDOWN >> 8) # 0x00000020
            LLKHF_UP = (KF_UP >> 8) # 0x00000080
            LLKHF_LOWER_IL_INJECTED = 0x00000002
            LLMHF_INJECTED = 0x00000001
            LLMHF_LOWER_IL_INJECTED = 0x00000002

            # REGION *** Desktop Family ***
            
            """
            * Structure used by WH_KEYBOARD_LL
            """
            class tagKBDLLHOOKSTRUCT(CStructure):
                _fields_ = [
                    ("vkCode", DWORD),
                    ("scanCode", DWORD),
                    ("flags", DWORD),
                    ("time", DWORD),
                    ("dwExtraInfo", ULONG_PTR)
                ]
                
                vkCode: int
                scanCode: int
                flags: int
                time: int
                dwExtraInfo: int
                
            KBDLLHOOKSTRUCT = tagKBDLLHOOKSTRUCT
            LPKBDLLHOOKSTRUCT = POINTER(KBDLLHOOKSTRUCT)
            PKBDLLHOOKSTRUCT = LPKBDLLHOOKSTRUCT

            """
            * Structure used by WH_MOUSE_LL
            """
            class tagMSLLHOOKSTRUCT(CStructure):
                _fields_ = [
                    ("pt", POINT),
                    ("mouseData", DWORD),
                    ("flags", DWORD),
                    ("time", DWORD),
                    ("dwExtraInfo", ULONG_PTR)
                ]
                
                pt: POINT
                mouseData: int
                flags: int
                time: int
                dwExtraInfo: int
                
            MSLLHOOKSTRUCT = tagMSLLHOOKSTRUCT
            LPMSLLHOOKSTRUCT = POINTER(MSLLHOOKSTRUCT)
            PMSLLHOOKSTRUCT = LPMSLLHOOKSTRUCT

            # REGION ***

            # REGION *** Desktop Family ***

            """
            * Structure used by WH_DEBUG
            """
            class tagDEBUGHOOKINFO(CStructure):
                _fields_ = [
                    ("idThread", DWORD),
                    ("idThreadInstaller", DWORD),
                    ("lParam", LPARAM),
                    ("wParam", WPARAM),
                    ("code", INT)
                ]
                
                idThread: int
                idThreadInstaller: int
                lParam: int
                wParam: int
                code: int
                
            DEBUGHOOKINFO = tagDEBUGHOOKINFO
            PDEBUGHOOKINFO = POINTER(DEBUGHOOKINFO)
            NPDEBUGHOOKINFO = PDEBUGHOOKINFO
            LPDEBUGHOOKINFO = PDEBUGHOOKINFO

            """
            * Structure used by WH_MOUSE
            """
            class tagMOUSEHOOKSTRUCT(CStructure):
                _fields_ = [
                    ("pt", POINT),
                    ("hwnd", HWND),
                    ("wHitTestCode", UINT),
                    ("dwExtraInfo", ULONG_PTR)
                ]
                
                pt: POINT
                hwnd: int
                wHitTestCode: int
                dwExtraInfo: int
                
            MOUSEHOOKSTRUCT = tagMOUSEHOOKSTRUCT
            LPMOUSEHOOKSTRUCT = POINTER(MOUSEHOOKSTRUCT)
            PMOUSEHOOKSTRUCT = LPMOUSEHOOKSTRUCT

            class tagMOUSEHOOKSTRUCTEX(CStructure):
                _fields_ = [
                    ("s", MOUSEHOOKSTRUCT),
                    ("mouseData", DWORD)
                ]
                
                s: MOUSEHOOKSTRUCT
                mouseData: int
                
            MOUSEHOOKSTRUCTEX = tagMOUSEHOOKSTRUCTEX
            LPMOUSEHOOKSTRUCTEX = POINTER(MOUSEHOOKSTRUCTEX)
            PMOUSEHOOKSTRUCTEX = LPMOUSEHOOKSTRUCTEX
            
            """
            * Structure used by WH_HARDWARE
            """
            class tagHARDWAREHOOKSTRUCT(CStructure):
                _fields_ = [
                    ("hwnd", HWND),
                    ("message", UINT),
                    ("wParam", WPARAM),
                    ("lParam", LPARAM)
                ]
                
                hwnd: int
                message: int
                wParam: int
                lParam: int
                
            HARDWAREHOOKSTRUCT = tagHARDWAREHOOKSTRUCT
            LPHARDWAREHOOKSTRUCT = POINTER(HARDWAREHOOKSTRUCT)
            PHARDWAREHOOKSTRUCT = LPHARDWAREHOOKSTRUCT
        
        # REGION ***
        
        """
        * Keyboard Layout API
        """

        HKL_PREV = 0
        HKL_NEXT = 1
        KLF_ACTIVATE = 0x00000001
        KLF_SUBSTITUTE_OK = 0x00000002
        KLF_REORDER = 0x00000008
        KLF_REPLACELANG = 0x00000010
        KLF_NOTELLSHELL = 0x00000080
        KLF_SETFORPROCESS = 0x00000100
        KLF_SHIFTLOCK = 0x00010000
        KLF_RESET = 0x40000000

        """
        * Bits in wParam of WM_INPUTLANGCHANGEREQUEST message
        """

        INPUTLANGCHANGE_SYSCHARSET = 0x0001
        INPUTLANGCHANGE_FORWARD = 0x0002
        INPUTLANGCHANGE_BACKWARD = 0x0004

        """
        * Size of KeyboardLayoutName (number of characters), including nul terminator
        """

        KL_NAMELENGTH = 9

        # REGION *** Desktop Family ***

        LoadKeyboardLayoutA = declare(user32.LoadKeyboardLayoutA, HKL, LPCSTR, UINT)
        LoadKeyboardLayoutW = declare(user32.LoadKeyboardLayoutW, HKL, LPCWSTR, UINT)

        LoadKeyboardLayout = unicode(LoadKeyboardLayoutW, LoadKeyboardLayoutA)

        ActivateKeyboardLayout = declare(user32.ActivateKeyboardLayout, HKL, HKL, UINT)

        ToUnicodeEx = declare(user32.ToUnicodeEx, INT, UINT, UINT, PBYTE, LPWSTR, INT, UINT, HKL)

        UnloadKeyboardLayout = declare(user32.UnloadKeyboardLayout, BOOL, HKL)

        GetKeyboardLayoutNameA = declare(user32.GetKeyboardLayoutNameA, BOOL, LPSTR)
        GetKeyboardLayoutNameW = declare(user32.GetKeyboardLayoutNameW, BOOL, LPWSTR)
        GetKeyboardLayoutName = unicode(GetKeyboardLayoutNameW, GetKeyboardLayoutNameA)

        GetKeyboardLayoutList = declare(user32.GetKeyboardLayoutList, INT, INT, POINTER(HKL))

        GetKeyboardLayout = declare(user32.GetKeyboardLayout, HKL, DWORD)

        # REGION ***

        # REGION *** Desktop Family ***

        class tagMOUSEMOVEPOINT(CStructure):
            _fields_ = [
                ("x", INT),
                ("y", INT),
                ("time", DWORD),
                ("dwExtraInfo", ULONG_PTR)
            ]
            
            x: int
            y: int
            time: int
            dwExtraInfo: int
            
        MOUSEMOVEPOINT = tagMOUSEMOVEPOINT
        PMOUSEMOVEPOINT = POINTER(MOUSEMOVEPOINT)
        LPMOUSEMOVEPOINT = PMOUSEMOVEPOINT

        # REGION ***

        """
        * Values for resolution parameter of GetMouseMovePointsEx
        """
        GMMP_USE_DISPLAY_POINTS = 1
        GMMP_USE_HIGH_RESOLUTION_POINTS = 2

        # REGION *** Desktop Family ***

        GetMouseMovePointsEx = declare(user32.GetMouseMovePointsEx, INT, UINT, LPMOUSEMOVEPOINT, INT, DWORD)

        # REGION ***

        if cpreproc.ifndef("NODESKTOP"):
                    
            """
            * Desktop-specific access flags
            """

            DESKTOP_READOBJECTS = 0x0001
            DESKTOP_CREATEWINDOW = 0x0002
            DESKTOP_CREATEMENU = 0x0004
            DESKTOP_HOOKCONTROL = 0x0008
            DESKTOP_JOURNALRECORD = 0x0010
            DESKTOP_JOURNALPLAYBACK = 0x0020
            DESKTOP_ENUMERATE = 0x0040
            DESKTOP_WRITEOBJECTS = 0x0080
            DESKTOP_SWITCHDESKTOP = 0x0100

            """
            * Desktop-specific control flags
            """

            DF_ALLOWOTHERACCOUNTHOOK = 0x0001

            if cpreproc.ifdef("_WINGDI_"):
                if cpreproc.ifndef("NOGDI"):
                    # REGION *** Desktop Family ***

                    from .wingdi import PDEVMODEA, PDEVMODEW, PBLENDFUNCTION

                    CreateDesktopA = declare(user32.CreateDesktopA, HDESK, LPCSTR, LPCSTR, PDEVMODEA, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES)
                    CreateDesktopW = declare(user32.CreateDesktopW, HDESK, LPCSTR, LPCWSTR, PDEVMODEW, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES)
                    CreateDesktop = unicode(CreateDesktopW, CreateDesktopA)

                    CreateDesktopExA = declare(user32.CreateDesktopExA, HDESK, LPCSTR, LPCSTR, PDEVMODEA, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES, ULONG, PVOID)
                    CreateDesktopExW = declare(user32.CreateDesktopExW, HDESK, LPCWSTR, LPCWSTR, PDEVMODEW, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES, ULONG, PVOID)
                    CreateDesktopEx = unicode(CreateDesktopExW, CreateDesktopExA)

                    # REGION ***

            # REGION *** Desktop Family ***

            OpenDesktopA = declare(user32.OpenDesktopA, HDESK, LPCSTR, DWORD, BOOL, ACCESS_MASK)
            OpenDesktopW = declare(user32.OpenDesktopW, HDESK, LPCWSTR, DWORD, BOOL, ACCESS_MASK)
            OpenDesktop = unicode(OpenDesktopW, OpenDesktopA)

            OpenInputDesktop = declare(user32.OpenInputDesktop, HDESK, DWORD, BOOL, ACCESS_MASK)

            EnumDesktopsA = declare(user32.EnumDesktopsA, BOOL, HWINSTA, DESKTOPENUMPROCA, LPARAM)
            EnumDesktopsW = declare(user32.EnumDesktopsW, BOOL, HWINSTA, DESKTOPENUMPROCW, LPARAM)
            EnumDesktops = unicode(EnumDesktopsW, EnumDesktopsA)

            EnumDesktopWindows = declare(user32.EnumDesktopWindows, BOOL, HDESK, WNDENUMPROC, LPARAM)

            SwitchDesktop = declare(user32.SwitchDesktop, BOOL, HDESK)

            SetThreadDesktop = declare(user32.SetThreadDesktop, BOOL, HDESK)

            CloseDesktop = declare(user32.CloseDesktop, BOOL, HDESK)

            GetThreadDesktop = declare(user32.GetThreadDesktop, HDESK, DWORD)

            # REGION ***
        if cpreproc.ifndef("NOWINDOWSTATION"):

            """
            * Windowstation-specific access flags
            """

            WINSTA_ENUMDESKTOPS = 0x0001
            WINSTA_READATTRIBUTES = 0x0002
            WINSTA_ACCESSCLIPBOARD = 0x0004
            WINSTA_CREATEDESKTOP = 0x0008
            WINSTA_WRITEATTRIBUTES = 0x0010
            WINSTA_ACCESSGLOBALATOMS = 0x0020
            WINSTA_EXITWINDOWS = 0x0040
            WINSTA_ENUMERATE = 0x0100
            WINSTA_READSCREEN = 0x0200
            WINSTA_ALL_ACCESS = (WINSTA_ENUMDESKTOPS | WINSTA_READATTRIBUTES | WINSTA_ACCESSCLIPBOARD | 
                                WINSTA_CREATEDESKTOP | WINSTA_WRITEATTRIBUTES | WINSTA_ACCESSGLOBALATOMS | 
                                WINSTA_EXITWINDOWS | WINSTA_ENUMERATE | WINSTA_READSCREEN)

            """
            * Windowstation creation flags.
            """

            CWF_CREATE_ONLY = 0x00000001

            """
            * Windowstation-specific attribute flags
            """

            WSF_VISIBLE = 0x0001

            # REGION *** Desktop Family ***

            CreateWindowStationA = declare(user32.CreateWindowStationA, HWINSTA, LPCSTR, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES)
            CreateWindowStationW = declare(user32.CreateWindowStationW, HWINSTA, LPCWSTR, DWORD, ACCESS_MASK, LPSECURITY_ATTRIBUTES)
            CreateWindowStation = unicode(CreateWindowStationW, CreateWindowStationA)

            OpenWindowStationA = declare(user32.OpenWindowStationA, HWINSTA, LPCSTR, BOOL, ACCESS_MASK)
            OpenWindowStationW = declare(user32.OpenWindowStationW, HWINSTA, LPCWSTR, BOOL, ACCESS_MASK)
            OpenWindowStation = unicode(OpenWindowStationW, OpenWindowStationA)

            EnumWindowStationsA = declare(user32.EnumWindowStationsA, BOOL, WINSTAENUMPROCA, LPARAM)
            EnumWindowStationsW = declare(user32.EnumWindowStationsW, BOOL, WINSTAENUMPROCW, LPARAM)
            EnumWindowStations = unicode(EnumWindowStationsW, EnumWindowStationsA)

            CloseWindowStation = declare(user32.CloseWindowStation, BOOL, HWINSTA)

            SetProcessWindowStation = declare(user32.CloseWindowStation, BOOL, HWINSTA)

            GetProcessWindowStation = declare(user32.GetProcessWindowStation, HWINSTA, VOID)

        # REGION ***

        if cpreproc.ifndef("NOSECURITY"):
            # REGION *** Desktop Family ***

            SetUserObjectSecurity = declare(user32.SetUserObjectSecurity, BOOL, HANDLE, PSECURITY_INFORMATION, PSECURITY_DESCRIPTOR)

            GetUserObjectSecurity = declare(user32.SetUserObjectSecurity, BOOL, HANDLE, PSECURITY_INFORMATION, PSECURITY_DESCRIPTOR, DWORD, LPDWORD)

            # REGION ***

            UOI_FLAGS = 1
            UOI_NAME = 2
            UOI_TYPE = 3
            UOI_USER_SID = 4
            UOI_HEAPSIZE = 5
            UOI_IO = 6
            UOI_TIMERPROC_EXCEPTION_SUPPRESSION = 7

            # REGION *** Desktop Family ***

            class tagUSEROBJECTFLAGS(CStructure):
                _fields_ = [
                    ("fInherit", BOOL),
                    ("fReserved", BOOL),
                    ("dwFlags", DWORD)
                ]
            USEROBJECTFLAGS = tagUSEROBJECTFLAGS
            PUSEROBJECTFLAGS = POINTER(USEROBJECTFLAGS)

            GetUserObjectInformationA = declare(user32.GetUserObjectInformationA, BOOL, HANDLE, INT, PVOID, DWORD, LPDWORD)
            GetUserObjectInformationW = declare(user32.GetUserObjectInformationW, BOOL, HANDLE, INT, PVOID, DWORD, LPDWORD)
            GetUserObjectInformation = unicode(GetUserObjectInformationW, GetUserObjectInformationA)

            SetUserObjectInformationA = declare(user32.SetUserObjectInformationA, BOOL, HANDLE, INT, PVOID, DWORD)
            SetUserObjectInformationW = declare(user32.SetUserObjectInformationW, BOOL, HANDLE, INT, PVOID, DWORD)
            SetUserObjectInformation = unicode(SetUserObjectInformationW, SetUserObjectInformationA)

        # REGION ***

        # REGION *** Desktop or Games Family ***

        class tagWNDCLASSEXA(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                # Win 3.x
                ("style", UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", INT),
                ("cbWndExtra", INT),
                ("hInstance", HINSTANCE),
                ("hIcon", HICON),
                ("hCursor", HCURSOR),
                ("hbrBackground", HBRUSH),
                ("lpszMenuName", LPCSTR),
                ("lpszClassName", LPCSTR),
                # Win 4.0
                ("hIconSm", HICON)
            ]
        WNDCLASSEXA = tagWNDCLASSEXA
        NPWNDCLASSEXA = POINTER(WNDCLASSEXA)
        LPWNDCLASSEXA = NPWNDCLASSEXA
        PWNDCLASSEXA = LPWNDCLASSEXA

        class tagWNDCLASSEXW(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                # Win 3.x
                ("style", UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", INT),
                ("cbWndExtra", INT),
                ("hInstance", HINSTANCE),
                ("hIcon", HICON),
                ("hCursor", HCURSOR),
                ("hbrBackground", HBRUSH),
                ("lpszMenuName", LPCWSTR),
                ("lpszClassName", LPCWSTR),
                # Win 4.0
                ("hIconSm", HICON)
            ]
        WNDCLASSEXW = tagWNDCLASSEXW
        NPWNDCLASSEXW = POINTER(WNDCLASSEXW)
        LPWNDCLASSEXW = NPWNDCLASSEXW
        PWNDCLASSEXW = LPWNDCLASSEXW

        WNDCLASSEX = unicode(WNDCLASSEXW, WNDCLASSEXA)
        PWNDCLASSEX = unicode(PWNDCLASSEXW, PWNDCLASSEXA)
        NPWNDCLASSEX = unicode(NPWNDCLASSEXW, NPWNDCLASSEXA)
        LPWNDCLASSEX = unicode(LPWNDCLASSEXW, LPWNDCLASSEXA)

        class tagWNDCLASSA(CStructure):
            _fields_ = [
                ("style", UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", INT),
                ("cbWndExtra", INT),
                ("hInstance", HINSTANCE),
                ("hIcon", HICON),
                ("hCursor", HCURSOR),
                ("hbrBackground", HBRUSH),
                ("lpszMenuName", LPCSTR),
                ("lpszClassName", LPCSTR)
            ]
            
            lpszClassName: LPCSTR
            lpszMenuName: LPCSTR
            lpfnWndProc: PVOID
            hbrBackground: int
            cbClsExtra: int
            cbWndExtra: int
            hInstance: int
            hCursor: int
            hIcon: int
            style: int
            
        WNDCLASSA = tagWNDCLASSA
        NPWNDCLASSA = POINTER(WNDCLASSA)
        LPWNDCLASSA = NPWNDCLASSA
        PWNDCLASSA = LPWNDCLASSA

        class tagWNDCLASSW(CStructure):
            _fields_ = [
                ("style", UINT),
                ("lpfnWndProc", WNDPROC),
                ("cbClsExtra", INT),
                ("cbWndExtra", INT),
                ("hInstance", HINSTANCE),
                ("hIcon", HICON),
                ("hCursor", HCURSOR),
                ("hbrBackground", HBRUSH),
                ("lpszMenuName", LPCWSTR),
                ("lpszClassName", LPCWSTR)
            ]
            
            lpszClassName: LPCWSTR
            lpszMenuName: LPCWSTR
            lpfnWndProc: PVOID
            hbrBackground: int
            cbClsExtra: int
            cbWndExtra: int
            hInstance: int
            hCursor: int
            hIcon: int
            style: int
            
        WNDCLASSW = tagWNDCLASSW
        NPWNDCLASSW = POINTER(WNDCLASSW)
        LPWNDCLASSW = NPWNDCLASSW
        PWNDCLASSW = LPWNDCLASSW

        WNDCLASS = unicode(WNDCLASSW, WNDCLASSA)
        PWNDCLASS = unicode(PWNDCLASSW, PWNDCLASSA)
        NPWNDCLASS = unicode(NPWNDCLASSW, NPWNDCLASSA)
        LPWNDCLASS = unicode(LPWNDCLASSW, LPWNDCLASSA)

        # REGION ***

        # REGION *** Desktop Family ***

        IsHungAppWindow = declare(user32.IsHungAppWindow, BOOL, HWND)

        DisableProcessWindowsGhosting = declare(user32.DisableProcessWindowsGhosting, VOID, VOID)

        # REGION ***

        def POINTSTOPOINT(pt, pts):
            pt.x = LONG(pts.x)
            pt.y = LONG(pts.x)

        POINTTOPOINTS = lambda pt: POINTS(SHORT(pt.x), SHORT(pt.y))
        MAKEWPARAM = lambda l, h: WPARAM(DWORD(MAKELONG(l, h)).value)
        MAKELPARAM = lambda l, h: LPARAM(DWORD(MAKELONG(l, h)).value)
        MAKELRESULT = lambda l, h: LRESULT(DWORD(MAKELONG(l, h)))

        if cpreproc.ifndef("NOWINOFFSETS"):

            """
            * Window field offsets for GetWindowLong()
            """

            GWL_WNDPROC = (-4)
            GWL_HINSTANCE = (-6)
            GWL_HWNDPARENT = (-8)
            GWL_STYLE = (-16)
            GWL_EXSTYLE = (-20)
            GWL_USERDATA = (-21)
            GWL_ID = (-12)
            GWLP_WNDPROC = (-4)
            GWLP_HINSTANCE = (-6)
            GWLP_HWNDPARENT = (-8)
            GWLP_USERDATA = (-21)
            GWLP_ID = (-12)

            """
            * Class field offsets for GetClassLong()
            """

            GCL_MENUNAME = (-8)
            GCL_HBRBACKGROUND = (-10)
            GCL_HCURSOR = (-12)
            GCL_HICON = (-14)
            GCL_HMODULE = (-16)
            GCL_CBWNDEXTRA = (-18)
            GCL_CBCLSEXTRA = (-20)
            GCL_WNDPROC = (-24)
            GCL_STYLE = (-26)
            GCW_ATOM = (-32)
            GCL_HICONSM = (-34)
        # !NOWINOFFSETS
        if cpreproc.ifndef("NOWINMESSAGES"):

            """
            * Window Messages
            """

            WM_NULL = 0x0000
            WM_CREATE = 0x0001
            WM_DESTROY = 0x0002
            WM_MOVE = 0x0003
            WM_SIZE = 0x0005
            WM_ACTIVATE = 0x0006

            """
            * WM_ACTIVATE state values
            """

            WA_INACTIVE = 0
            WA_ACTIVE = 1
            WA_CLICKACTIVE = 2
            WM_SETFOCUS = 0x0007
            WM_KILLFOCUS = 0x0008
            WM_ENABLE = 0x000A
            WM_SETREDRAW = 0x000B
            WM_SETTEXT = 0x000C
            WM_GETTEXT = 0x000D
            WM_GETTEXTLENGTH = 0x000E
            WM_PAINT = 0x000F
            WM_CLOSE = 0x0010
            WM_QUERYENDSESSION = 0x0011
            WM_QUERYOPEN = 0x0013
            WM_ENDSESSION = 0x0016
            WM_QUIT = 0x0012
            WM_ERASEBKGND = 0x0014
            WM_SYSCOLORCHANGE = 0x0015
            WM_SHOWWINDOW = 0x0018
            WM_WININICHANGE = 0x001A
            WM_SETTINGCHANGE = WM_WININICHANGE
            WM_DEVMODECHANGE = 0x001B
            WM_ACTIVATEAPP = 0x001C
            WM_FONTCHANGE = 0x001D
            WM_TIMECHANGE = 0x001E
            WM_CANCELMODE = 0x001F
            WM_SETCURSOR = 0x0020
            WM_MOUSEACTIVATE = 0x0021
            WM_CHILDACTIVATE = 0x0022
            WM_QUEUESYNC = 0x0023
            WM_GETMINMAXINFO = 0x0024

            # REGION *** Desktop Family ***

            """
            * Struct pointed to by WM_GETMINMAXINFO lParam
            """
            class tagMINMAXINFO(CStructure):
                _fields_ = [
                    ("ptReserved", POINT),
                    ("ptMaxSize", POINT),
                    ("ptMaxPosition", POINT),
                    ("ptMinTrackSize", POINT),
                    ("ptMaxTrackSize", POINT)
                ]
            MINMAXINFO = tagMINMAXINFO
            PMINMAXINFO = POINTER(MINMAXINFO)
            LPMINMAXINFO = PMINMAXINFO

            # REGION ***

            WM_PAINTICON = 0x0026
            WM_ICONERASEBKGND = 0x0027
            WM_NEXTDLGCTL = 0x0028
            WM_SPOOLERSTATUS = 0x002A
            WM_DRAWITEM = 0x002B
            WM_MEASUREITEM = 0x002C
            WM_DELETEITEM = 0x002D
            WM_VKEYTOITEM = 0x002E
            WM_CHARTOITEM = 0x002F
            WM_SETFONT = 0x0030
            WM_GETFONT = 0x0031
            WM_SETHOTKEY = 0x0032
            WM_GETHOTKEY = 0x0033
            WM_QUERYDRAGICON = 0x0037
            WM_COMPAREITEM = 0x0039
            WM_GETOBJECT = 0x003D
            # WINVER >= 0x0500
            WM_COMPACTING = 0x0041
            WM_COMMNOTIFY = 0x0044 # no longer suported
            WM_WINDOWPOSCHANGING = 0x0046
            WM_WINDOWPOSCHANGED = 0x0047
            WM_POWER = 0x0048

            """
            * wParam for WM_POWER window message and DRV_POWER driver notification
            """

            PWR_OK = 1
            PWR_FAIL = (-1)
            PWR_SUSPENDREQUEST = 1
            PWR_SUSPENDRESUME = 2
            PWR_CRITICALRESUME = 3
            WM_COPYDATA = 0x004A
            WM_CANCELJOURNAL = 0x004B

            # REGION *** Desktop Family ***

            """
            * lParam of WM_COPYDATA message points to...
            """
            class tagCOPYDATASTRUCT(CStructure):
                _fields_ = [
                    ("dwData", ULONG_PTR),
                    ("cbData", DWORD),
                    ("lpData", PVOID)
                ]
            COPYDATASTRUCT = tagCOPYDATASTRUCT
            PCOPYDATASTRUCT = POINTER(COPYDATASTRUCT)

            class tagMDINEXTMENU(CStructure):
                _fields_ = [
                    ("hmenuIn", HMENU),
                    ("hmenuNext", HMENU),
                    ("hwndNext", HWND)
                ]
            MDINEXTMENU = tagMDINEXTMENU
            PMDINEXTMENU = POINTER(MDINEXTMENU)
            LPMDINEXTMENU = PMDINEXTMENU

            # REGION ***

            WM_NOTIFY = 0x004E
            WM_INPUTLANGCHANGEREQUEST = 0x0050
            WM_INPUTLANGCHANGE = 0x0051
            WM_TCARD = 0x0052
            WM_HELP = 0x0053
            WM_USERCHANGED = 0x0054
            WM_NOTIFYFORMAT = 0x0055
            NFR_ANSI = 1
            NFR_UNICODE = 2
            NF_QUERY = 3
            NF_REQUERY = 4
            WM_CONTEXTMENU = 0x007B
            WM_STYLECHANGING = 0x007C
            WM_STYLECHANGED = 0x007D
            WM_DISPLAYCHANGE = 0x007E
            WM_GETICON = 0x007F
            WM_SETICON = 0x0080
            WM_NCCREATE = 0x0081
            WM_NCDESTROY = 0x0082
            WM_NCCALCSIZE = 0x0083
            WM_NCHITTEST = 0x0084
            WM_NCPAINT = 0x0085
            WM_NCACTIVATE = 0x0086
            WM_GETDLGCODE = 0x0087
            WM_SYNCPAINT = 0x0088
            WM_NCMOUSEMOVE = 0x00A0
            WM_NCLBUTTONDOWN = 0x00A1
            WM_NCLBUTTONUP = 0x00A2
            WM_NCLBUTTONDBLCLK = 0x00A3
            WM_NCRBUTTONDOWN = 0x00A4
            WM_NCRBUTTONUP = 0x00A5
            WM_NCRBUTTONDBLCLK = 0x00A6
            WM_NCMBUTTONDOWN = 0x00A7
            WM_NCMBUTTONUP = 0x00A8
            WM_NCMBUTTONDBLCLK = 0x00A9
            WM_NCXBUTTONDOWN = 0x00AB
            WM_NCXBUTTONUP = 0x00AC
            WM_NCXBUTTONDBLCLK = 0x00AD
            WM_INPUT_DEVICE_CHANGE = 0x00FE
            WM_INPUT = 0x00FF
            WM_KEYFIRST = 0x0100
            WM_KEYDOWN = 0x0100
            WM_KEYUP = 0x0101
            WM_CHAR = 0x0102
            WM_DEADCHAR = 0x0103
            WM_SYSKEYDOWN = 0x0104
            WM_SYSKEYUP = 0x0105
            WM_SYSCHAR = 0x0106
            WM_SYSDEADCHAR = 0x0107
            WM_UNICHAR = 0x0109
            WM_KEYLAST = 0x0109
            UNICODE_NOCHAR = 0xFFFF
            WM_KEYLAST = 0x0108
            WM_IME_STARTCOMPOSITION = 0x010D
            WM_IME_ENDCOMPOSITION = 0x010E
            WM_IME_COMPOSITION = 0x010F
            WM_IME_KEYLAST = 0x010F
            WM_INITDIALOG = 0x0110
            WM_COMMAND = 0x0111
            WM_SYSCOMMAND = 0x0112
            WM_TIMER = 0x0113
            WM_HSCROLL = 0x0114
            WM_VSCROLL = 0x0115
            WM_INITMENU = 0x0116
            WM_INITMENUPOPUP = 0x0117
            WM_GESTURE = 0x0119
            WM_GESTURENOTIFY = 0x011A
            WM_MENUSELECT = 0x011F
            WM_MENUCHAR = 0x0120
            WM_ENTERIDLE = 0x0121
            WM_MENURBUTTONUP = 0x0122
            WM_MENUDRAG = 0x0123
            WM_MENUGETOBJECT = 0x0124
            WM_UNINITMENUPOPUP = 0x0125
            WM_MENUCOMMAND = 0x0126
            WM_CHANGEUISTATE = 0x0127
            WM_UPDATEUISTATE = 0x0128
            WM_QUERYUISTATE = 0x0129

            """
            * LOWORD(wParam) values in WM_*UISTATE*
            """

            UIS_SET = 1
            UIS_CLEAR = 2
            UIS_INITIALIZE = 3

            """
            * HIWORD(wParam) values in WM_*UISTATE*
            """

            UISF_HIDEFOCUS = 0x1
            UISF_HIDEACCEL = 0x2
            UISF_ACTIVE = 0x4
            # WINVER >= 0x0500
            WM_CTLCOLORMSGBOX = 0x0132
            WM_CTLCOLOREDIT = 0x0133
            WM_CTLCOLORLISTBOX = 0x0134
            WM_CTLCOLORBTN = 0x0135
            WM_CTLCOLORDLG = 0x0136
            WM_CTLCOLORSCROLLBAR = 0x0137
            WM_CTLCOLORSTATIC = 0x0138
            MN_GETHMENU = 0x01E1
            WM_MOUSEFIRST = 0x0200
            WM_MOUSEMOVE = 0x0200
            WM_LBUTTONDOWN = 0x0201
            WM_LBUTTONUP = 0x0202
            WM_LBUTTONDBLCLK = 0x0203
            WM_RBUTTONDOWN = 0x0204
            WM_RBUTTONUP = 0x0205
            WM_RBUTTONDBLCLK = 0x0206
            WM_MBUTTONDOWN = 0x0207
            WM_MBUTTONUP = 0x0208
            WM_MBUTTONDBLCLK = 0x0209
            WM_MOUSEWHEEL = 0x020A
            WM_XBUTTONDOWN = 0x020B
            WM_XBUTTONUP = 0x020C
            WM_XBUTTONDBLCLK = 0x020D
            WM_MOUSEHWHEEL = 0x020E
            WM_MOUSELAST = 0x020E
            WM_MOUSELAST = 0x020D
            WM_MOUSELAST = 0x020A
            WM_MOUSELAST = 0x0209
            WHEEL_DELTA = 120
            GET_WHEEL_DELTA_WPARAM = lambda wParam: SHORT(HIWORD(wParam)).value
            WHEEL_PAGESCROLL = (MAXUINT_PTR)
            GET_KEYSTATE_WPARAM = lambda wParam: LOWORD(wParam)
            GET_NCHITTEST_WPARAM = lambda wParam: SHORT(LOWORD(wParam)).value
            GET_XBUTTON_WPARAM = lambda wParam: HIWORD(wParam)
            XBUTTON1 = 0x0001
            XBUTTON2 = 0x0002
            WM_PARENTNOTIFY = 0x0210
            WM_ENTERMENULOOP = 0x0211
            WM_EXITMENULOOP = 0x0212
            WM_NEXTMENU = 0x0213
            WM_SIZING = 0x0214
            WM_CAPTURECHANGED = 0x0215
            WM_MOVING = 0x0216
            WM_POWERBROADCAST = 0x0218
            PBT_APMQUERYSUSPEND = 0x0000
            PBT_APMQUERYSTANDBY = 0x0001
            PBT_APMQUERYSUSPENDFAILED = 0x0002
            PBT_APMQUERYSTANDBYFAILED = 0x0003
            PBT_APMSUSPEND = 0x0004
            PBT_APMSTANDBY = 0x0005
            PBT_APMRESUMECRITICAL = 0x0006
            PBT_APMRESUMESUSPEND = 0x0007
            PBT_APMRESUMESTANDBY = 0x0008
            PBTF_APMRESUMEFROMFAILURE = 0x00000001
            PBT_APMBATTERYLOW = 0x0009
            PBT_APMPOWERSTATUSCHANGE = 0x000A
            PBT_APMOEMEVENT = 0x000B
            PBT_APMRESUMEAUTOMATIC = 0x0012
            if cpreproc.pragma_once("PBT_POWERSETTINGCHANGE"):
                PBT_POWERSETTINGCHANGE = 0x8013

                # REGION *** Desktop Family ***

                class POWERBROADCAST_SETTING(CStructure):
                    _fields_ = [
                        ("PowerSetting", GUID),
                        ("DataLength", DWORD),
                        ("Data", UCHAR * 1)
                    ]
                PPOWERBROADCAST_SETTING = POINTER(POWERBROADCAST_SETTING)

                # REGION ***
            WM_DEVICECHANGE = 0x0219
            WM_MDICREATE = 0x0220
            WM_MDIDESTROY = 0x0221
            WM_MDIACTIVATE = 0x0222
            WM_MDIRESTORE = 0x0223
            WM_MDINEXT = 0x0224
            WM_MDIMAXIMIZE = 0x0225
            WM_MDITILE = 0x0226
            WM_MDICASCADE = 0x0227
            WM_MDIICONARRANGE = 0x0228
            WM_MDIGETACTIVE = 0x0229
            WM_MDISETMENU = 0x0230
            WM_ENTERSIZEMOVE = 0x0231
            WM_EXITSIZEMOVE = 0x0232
            WM_DROPFILES = 0x0233
            WM_MDIREFRESHMENU = 0x0234
            WM_POINTERDEVICECHANGE = 0x238
            WM_POINTERDEVICEINRANGE = 0x239
            WM_POINTERDEVICEOUTOFRANGE = 0x23A
            WM_TOUCH = 0x0240
            WM_NCPOINTERUPDATE = 0x0241
            WM_NCPOINTERDOWN = 0x0242
            WM_NCPOINTERUP = 0x0243
            WM_POINTERUPDATE = 0x0245
            WM_POINTERDOWN = 0x0246
            WM_POINTERUP = 0x0247
            WM_POINTERENTER = 0x0249
            WM_POINTERLEAVE = 0x024A
            WM_POINTERACTIVATE = 0x024B
            WM_POINTERCAPTURECHANGED = 0x024C
            WM_TOUCHHITTESTING = 0x024D
            WM_POINTERWHEEL = 0x024E
            WM_POINTERHWHEEL = 0x024F
            DM_POINTERHITTEST = 0x0250
            WM_POINTERROUTEDTO = 0x0251
            WM_POINTERROUTEDAWAY = 0x0252
            WM_POINTERROUTEDRELEASED = 0x0253
            WM_IME_SETCONTEXT = 0x0281
            WM_IME_NOTIFY = 0x0282
            WM_IME_CONTROL = 0x0283
            WM_IME_COMPOSITIONFULL = 0x0284
            WM_IME_SELECT = 0x0285
            WM_IME_CHAR = 0x0286
            WM_IME_REQUEST = 0x0288
            WM_IME_KEYDOWN = 0x0290
            WM_IME_KEYUP = 0x0291
            WM_MOUSEHOVER = 0x02A1
            WM_MOUSELEAVE = 0x02A3
            WM_NCMOUSEHOVER = 0x02A0
            WM_NCMOUSELEAVE = 0x02A2
            WM_WTSSESSION_CHANGE = 0x02B1
            WM_TABLET_FIRST = 0x02c0
            WM_TABLET_LAST = 0x02df
            WM_DPICHANGED = 0x02E0
            WM_DPICHANGED_BEFOREPARENT = 0x02E2
            WM_DPICHANGED_AFTERPARENT = 0x02E3
            WM_GETDPISCALEDSIZE = 0x02E4
            WM_CUT = 0x0300
            WM_COPY = 0x0301
            WM_PASTE = 0x0302
            WM_CLEAR = 0x0303
            WM_UNDO = 0x0304
            WM_RENDERFORMAT = 0x0305
            WM_RENDERALLFORMATS = 0x0306
            WM_DESTROYCLIPBOARD = 0x0307
            WM_DRAWCLIPBOARD = 0x0308
            WM_PAINTCLIPBOARD = 0x0309
            WM_VSCROLLCLIPBOARD = 0x030A
            WM_SIZECLIPBOARD = 0x030B
            WM_ASKCBFORMATNAME = 0x030C
            WM_CHANGECBCHAIN = 0x030D
            WM_HSCROLLCLIPBOARD = 0x030E
            WM_QUERYNEWPALETTE = 0x030F
            WM_PALETTEISCHANGING = 0x0310
            WM_PALETTECHANGED = 0x0311
            WM_HOTKEY = 0x0312
            WM_PRINT = 0x0317
            WM_PRINTCLIENT = 0x0318
            WM_APPCOMMAND = 0x0319
            WM_THEMECHANGED = 0x031A
            WM_CLIPBOARDUPDATE = 0x031D
            WM_DWMCOMPOSITIONCHANGED = 0x031E
            WM_DWMNCRENDERINGCHANGED = 0x031F
            WM_DWMCOLORIZATIONCOLORCHANGED = 0x0320
            WM_DWMWINDOWMAXIMIZEDCHANGE = 0x0321
            WM_DWMSENDICONICTHUMBNAIL = 0x0323
            WM_DWMSENDICONICLIVEPREVIEWBITMAP = 0x0326
            WM_GETTITLEBARINFOEX = 0x033F
            WM_HANDHELDFIRST = 0x0358
            WM_HANDHELDLAST = 0x035F
            WM_AFXFIRST = 0x0360
            WM_AFXLAST = 0x037F
            WM_PENWINFIRST = 0x0380
            WM_PENWINLAST = 0x038F
            WM_APP = 0x8000

            """
            * NOTE: All Message Numbers below 0x0400 are RESERVED.
            *
            * Private Window Messages Start Here:
            """

            WM_USER = 0x0400
            WMSZ_LEFT = 1
            WMSZ_RIGHT = 2
            WMSZ_TOP = 3
            WMSZ_TOPLEFT = 4
            WMSZ_TOPRIGHT = 5
            WMSZ_BOTTOM = 6
            WMSZ_BOTTOMLEFT = 7
            WMSZ_BOTTOMRIGHT = 8
            if cpreproc.ifndef("NONCMESSAGES"):

                    """
                    * WM_NCHITTEST and MOUSEHOOKSTRUCT Mouse Position Codes
                    """

                    HTERROR = (-2)
                    HTTRANSPARENT = (-1)
                    HTNOWHERE = 0
                    HTCLIENT = 1
                    HTCAPTION = 2
                    HTSYSMENU = 3
                    HTGROWBOX = 4
                    HTSIZE = HTGROWBOX
                    HTMENU = 5
                    HTHSCROLL = 6
                    HTVSCROLL = 7
                    HTMINBUTTON = 8
                    HTMAXBUTTON = 9
                    HTLEFT = 10
                    HTRIGHT = 11
                    HTTOP = 12
                    HTTOPLEFT = 13
                    HTTOPRIGHT = 14
                    HTBOTTOM = 15
                    HTBOTTOMLEFT = 16
                    HTBOTTOMRIGHT = 17
                    HTBORDER = 18
                    HTREDUCE = HTMINBUTTON
                    HTZOOM = HTMAXBUTTON
                    HTSIZEFIRST = HTLEFT
                    HTSIZELAST = HTBOTTOMRIGHT
                    HTOBJECT = 19
                    HTCLOSE = 20
                    HTHELP = 21

                    """
                    * SendMessageTimeout values
                    """

                    SMTO_NORMAL = 0x0000
                    SMTO_BLOCK = 0x0001
                    SMTO_ABORTIFHUNG = 0x0002
                    SMTO_NOTIMEOUTIFNOTHUNG = 0x0008
                    SMTO_ERRORONEXIT = 0x0020
            # !NONCMESSAGES

            """
            * WM_MOUSEACTIVATE Return Codes
            """

            MA_ACTIVATE = 1
            MA_ACTIVATEANDEAT = 2
            MA_NOACTIVATE = 3
            MA_NOACTIVATEANDEAT = 4

            """
            * WM_SETICON / WM_GETICON Type Codes
            """

            ICON_SMALL = 0
            ICON_BIG = 1
            ICON_SMALL2 = 2

            # REGION *** Desktop Family ***

            RegisterWindowMessageA = declare(user32.RegisterWindowMessageA, UINT, LPCSTR)
            RegisterWindowMessageW = declare(user32.RegisterWindowMessageW, UINT, LPCWSTR)
            RegisterWindowMessage = unicode(RegisterWindowMessageW, RegisterWindowMessageA)

            # REGION ***

            """
            * WM_SIZE message wParam values
            """

            SIZE_RESTORED = 0
            SIZE_MINIMIZED = 1
            SIZE_MAXIMIZED = 2
            SIZE_MAXSHOW = 3
            SIZE_MAXHIDE = 4

            """
            * Obsolete constant names
            """

            SIZENORMAL = SIZE_RESTORED
            SIZEICONIC = SIZE_MINIMIZED
            SIZEFULLSCREEN = SIZE_MAXIMIZED
            SIZEZOOMSHOW = SIZE_MAXSHOW
            SIZEZOOMHIDE = SIZE_MAXHIDE

            # REGION *** Desktop Family ***

            """
            * WM_WINDOWPOSCHANGING/CHANGED struct pointed to by lParam
            """
            class tagWINDOWPOS(CStructure):
                _fields_ = [
                    ("hwnd", HWND),
                    ("hwndInsertAfter", HWND),
                    ("x", INT),
                    ("y", INT),
                    ("cx", INT),
                    ("cy", INT),
                    ("flags", UINT)
                ]
            WINDOWPOS = tagWINDOWPOS
            LPWINDOWPOS = POINTER(WINDOWPOS)
            PWINDOWPOS = LPWINDOWPOS

            """"
            * WM_NCCALCSIZE parameter structure
            """
            class tagNCCALCSIZE_PARAMS(CStructure):
                _fields_ = [
                    ("rgrc", RECT * 3),
                    ("lppos", PWINDOWPOS)
                ]
            NCCALCSIZE_PARAMS = tagNCCALCSIZE_PARAMS
            LPNCCALCSIZE_PARAMS = POINTER(NCCALCSIZE_PARAMS)

            # REGION ***

            """
            * WM_NCCALCSIZE "window valid rect" return values
            """

            WVR_ALIGNTOP = 0x0010
            WVR_ALIGNLEFT = 0x0020
            WVR_ALIGNBOTTOM = 0x0040
            WVR_ALIGNRIGHT = 0x0080
            WVR_HREDRAW = 0x0100
            WVR_VREDRAW = 0x0200
            WVR_REDRAW = (WVR_HREDRAW | WVR_VREDRAW)
            WVR_VALIDRECTS = 0x0400
            if cpreproc.ifndef("NOKEYSTATES"):

                """
                * Key State Masks for Mouse Messages
                """

                MK_LBUTTON = 0x0001
                MK_RBUTTON = 0x0002
                MK_SHIFT = 0x0004
                MK_CONTROL = 0x0008
                MK_MBUTTON = 0x0010
                MK_XBUTTON1 = 0x0020
                MK_XBUTTON2 = 0x0040
            # !NOKEYSTATES
            if cpreproc.ifndef("NOTRACKMOUSEEVENT"):
                TME_HOVER = 0x00000001
                TME_LEAVE = 0x00000002
                TME_NONCLIENT = 0x00000010
                TME_QUERY = 0x40000000
                TME_CANCEL = 0x80000000
                HOVER_DEFAULT = 0xFFFFFFFF

                # REGION *** Desktop Family ***

                class tagTRACKMOUSEEVENT(CStructure):
                    _fields_ = [
                        ("cbSize", DWORD),
                        ("dwFlags", DWORD),
                        ("hwndTrack", HWND),
                        ("dwHoverTime", DWORD)
                    ]
                TRACKMOUSEEVENT = tagTRACKMOUSEEVENT
                LPTRACKMOUSEEVENT = POINTER(TRACKMOUSEEVENT)

                TrackMouseEvent = declare(user32.TrackMouseEvent, BOOL, LPTRACKMOUSEEVENT)

                # REGION ***
            # !NOTRACKMOUSEEVENT
        # !NOWINMESSAGES
        if cpreproc.ifndef("NOWINSTYLES"):

            """
            * Window Styles
            """

            WS_OVERLAPPED = 0x00000000
            WS_POPUP = 0x80000000
            WS_CHILD = 0x40000000
            WS_MINIMIZE = 0x20000000
            WS_VISIBLE = 0x10000000
            WS_DISABLED = 0x08000000
            WS_CLIPSIBLINGS = 0x04000000
            WS_CLIPCHILDREN = 0x02000000
            WS_MAXIMIZE = 0x01000000
            WS_CAPTION = 0x00C00000 # WS_BORDER | WS_DLGFRAME
            WS_BORDER = 0x00800000
            WS_DLGFRAME = 0x00400000
            WS_VSCROLL = 0x00200000
            WS_HSCROLL = 0x00100000
            WS_SYSMENU = 0x00080000
            WS_THICKFRAME = 0x00040000
            WS_GROUP = 0x00020000
            WS_TABSTOP = 0x00010000
            WS_MINIMIZEBOX = 0x00020000
            WS_MAXIMIZEBOX = 0x00010000
            WS_TILED = WS_OVERLAPPED
            WS_ICONIC = WS_MINIMIZE
            WS_SIZEBOX = WS_THICKFRAME
            WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED  | 
                                    WS_CAPTION     | 
                                    WS_SYSMENU     | 
                                    WS_THICKFRAME  | 
                                    WS_MINIMIZEBOX | 
                                    WS_MAXIMIZEBOX)
            WS_TILEDWINDOW = WS_OVERLAPPEDWINDOW

            """
            * Common Window Styles
            """

            WS_POPUPWINDOW = (WS_POPUP  | 
                                WS_BORDER | 
                                WS_SYSMENU)
            WS_CHILDWINDOW = (WS_CHILD)

            """
            * Extended Window Styles
            """

            WS_EX_DLGMODALFRAME = 0x00000001
            WS_EX_NOPARENTNOTIFY = 0x00000004
            WS_EX_TOPMOST = 0x00000008
            WS_EX_ACCEPTFILES = 0x00000010
            WS_EX_TRANSPARENT = 0x00000020
            WS_EX_MDICHILD = 0x00000040
            WS_EX_TOOLWINDOW = 0x00000080
            WS_EX_WINDOWEDGE = 0x00000100
            WS_EX_CLIENTEDGE = 0x00000200
            WS_EX_CONTEXTHELP = 0x00000400
            WS_EX_RIGHT = 0x00001000
            WS_EX_LEFT = 0x00000000
            WS_EX_RTLREADING = 0x00002000
            WS_EX_LTRREADING = 0x00000000
            WS_EX_LEFTSCROLLBAR = 0x00004000
            WS_EX_RIGHTSCROLLBAR = 0x00000000
            WS_EX_CONTROLPARENT = 0x00010000
            WS_EX_STATICEDGE = 0x00020000
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_OVERLAPPEDWINDOW = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
            WS_EX_PALETTEWINDOW = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)
            WS_EX_LAYERED = 0x00080000
            WS_EX_NOINHERITLAYOUT = 0x00100000 # Disable inheritence of mirroring by children
            WS_EX_NOREDIRECTIONBITMAP = 0x00200000
            WS_EX_LAYOUTRTL = 0x00400000 # Right to left mirroring
            WS_EX_COMPOSITED = 0x02000000
            WS_EX_NOACTIVATE = 0x08000000

            """
            * Class styles
            """

            CS_VREDRAW = 0x0001
            CS_HREDRAW = 0x0002
            CS_DBLCLKS = 0x0008
            CS_OWNDC = 0x0020
            CS_CLASSDC = 0x0040
            CS_PARENTDC = 0x0080
            CS_NOCLOSE = 0x0200
            CS_SAVEBITS = 0x0800
            CS_BYTEALIGNCLIENT = 0x1000
            CS_BYTEALIGNWINDOW = 0x2000
            CS_GLOBALCLASS = 0x4000
            CS_IME = 0x00010000
            CS_DROPSHADOW = 0x00020000
        # !NOWINSTYLES
        PRF_CHECKVISIBLE = 0x00000001
        PRF_NONCLIENT = 0x00000002
        PRF_CLIENT = 0x00000004
        PRF_ERASEBKGND = 0x00000008
        PRF_CHILDREN = 0x00000010
        PRF_OWNED = 0x00000020
        BDR_RAISEDOUTER = 0x0001
        BDR_SUNKENOUTER = 0x0002
        BDR_RAISEDINNER = 0x0004
        BDR_SUNKENINNER = 0x0008
        BDR_OUTER = (BDR_RAISEDOUTER | BDR_SUNKENOUTER)
        BDR_INNER = (BDR_RAISEDINNER | BDR_SUNKENINNER)
        BDR_RAISED = (BDR_RAISEDOUTER | BDR_RAISEDINNER)
        BDR_SUNKEN = (BDR_SUNKENOUTER | BDR_SUNKENINNER)
        EDGE_RAISED = (BDR_RAISEDOUTER | BDR_RAISEDINNER)
        EDGE_SUNKEN = (BDR_SUNKENOUTER | BDR_SUNKENINNER)
        EDGE_ETCHED = (BDR_SUNKENOUTER | BDR_RAISEDINNER)
        EDGE_BUMP = (BDR_RAISEDOUTER | BDR_SUNKENINNER)
        BF_LEFT = 0x0001
        BF_TOP = 0x0002
        BF_RIGHT = 0x0004
        BF_BOTTOM = 0x0008
        BF_TOPLEFT = (BF_TOP | BF_LEFT)
        BF_TOPRIGHT = (BF_TOP | BF_RIGHT)
        BF_BOTTOMLEFT = (BF_BOTTOM | BF_LEFT)
        BF_BOTTOMRIGHT = (BF_BOTTOM | BF_RIGHT)
        BF_RECT = (BF_LEFT | BF_TOP | BF_RIGHT | BF_BOTTOM)
        BF_DIAGONAL = 0x0010
        BF_DIAGONAL_ENDTOPRIGHT = (BF_DIAGONAL | BF_TOP | BF_RIGHT)
        BF_DIAGONAL_ENDTOPLEFT = (BF_DIAGONAL | BF_TOP | BF_LEFT)
        BF_DIAGONAL_ENDBOTTOMLEFT = (BF_DIAGONAL | BF_BOTTOM | BF_LEFT)
        BF_DIAGONAL_ENDBOTTOMRIGHT = (BF_DIAGONAL | BF_BOTTOM | BF_RIGHT)
        BF_MIDDLE = 0x0800 # Fill in the middle
        BF_SOFT = 0x1000 # For softer buttons
        BF_ADJUST = 0x2000 # Calculate the space left over
        BF_FLAT = 0x4000 # For flat rather than 3D borders
        BF_MONO = 0x8000 # For monochrome borders

        # REGION *** Desktop Family ***

        DrawEdge = declare(user32.DrawEdge, BOOL, HDC, LPRECT, UINT, UINT)

        # REGION ***

        DFC_CAPTION = 1
        DFC_MENU = 2
        DFC_SCROLL = 3
        DFC_BUTTON = 4
        DFC_POPUPMENU = 5
        DFCS_CAPTIONCLOSE = 0x0000
        DFCS_CAPTIONMIN = 0x0001
        DFCS_CAPTIONMAX = 0x0002
        DFCS_CAPTIONRESTORE = 0x0003
        DFCS_CAPTIONHELP = 0x0004
        DFCS_MENUARROW = 0x0000
        DFCS_MENUCHECK = 0x0001
        DFCS_MENUBULLET = 0x0002
        DFCS_MENUARROWRIGHT = 0x0004
        DFCS_SCROLLUP = 0x0000
        DFCS_SCROLLDOWN = 0x0001
        DFCS_SCROLLLEFT = 0x0002
        DFCS_SCROLLRIGHT = 0x0003
        DFCS_SCROLLCOMBOBOX = 0x0005
        DFCS_SCROLLSIZEGRIP = 0x0008
        DFCS_SCROLLSIZEGRIPRIGHT = 0x0010
        DFCS_BUTTONCHECK = 0x0000
        DFCS_BUTTONRADIOIMAGE = 0x0001
        DFCS_BUTTONRADIOMASK = 0x0002
        DFCS_BUTTONRADIO = 0x0004
        DFCS_BUTTON3STATE = 0x0008
        DFCS_BUTTONPUSH = 0x0010
        DFCS_INACTIVE = 0x0100
        DFCS_PUSHED = 0x0200
        DFCS_CHECKED = 0x0400
        DFCS_TRANSPARENT = 0x0800
        DFCS_HOT = 0x1000
        DFCS_ADJUSTRECT = 0x2000
        DFCS_FLAT = 0x4000
        DFCS_MONO = 0x8000

        # REGION *** Desktop Family ***

        DrawFrameControl = declare(user32.DrawFrameControl, BOOL, HDC, LPRECT, UINT, UINT)

        # REGION ***

        DC_ACTIVE = 0x0001
        DC_SMALLCAP = 0x0002
        DC_ICON = 0x0004
        DC_TEXT = 0x0008
        DC_INBUTTON = 0x0010
        DC_GRADIENT = 0x0020
        DC_BUTTONS = 0x1000

        # REGION *** Desktop Family ***

        DrawCaption = declare(user32.DrawCaption, BOOL, HWND, HDC, LPRECT, UINT)

        # REGION ***

        IDANI_OPEN = 1
        INANI_CAPTION = 3

        # REGION *** Desktop Family ***

        DrawAnimatedRects = declare(user32.DrawAnimatedRects, BOOL, HWND, INT, LPRECT, LPRECT)

        # REGION ***

        if cpreproc.ifndef("NOCLIPBOARD"):

            """
            * Predefined Clipboard Formats
            """

            CF_TEXT = 1
            CF_BITMAP = 2
            CF_METAFILEPICT = 3
            CF_SYLK = 4
            CF_DIF = 5
            CF_TIFF = 6
            CF_OEMTEXT = 7
            CF_DIB = 8
            CF_PALETTE = 9
            CF_PENDATA = 10
            CF_RIFF = 11
            CF_WAVE = 12
            CF_UNICODETEXT = 13
            CF_ENHMETAFILE = 14
            CF_HDROP = 15
            CF_LOCALE = 16
            CF_DIBV5 = 17
            CF_MAX = 18
            CF_MAX = 17
            CF_MAX = 15
            CF_OWNERDISPLAY = 0x0080
            CF_DSPTEXT = 0x0081
            CF_DSPBITMAP = 0x0082
            CF_DSPMETAFILEPICT = 0x0083
            CF_DSPENHMETAFILE = 0x008E

            """
            * "Private" formats don't get GlobalFree()'d
            """

            CF_PRIVATEFIRST = 0x0200
            CF_PRIVATELAST = 0x02FF

            """
            * "GDIOBJ" formats do get DeleteObject()'d
            """

            CF_GDIOBJFIRST = 0x0300
            CF_GDIOBJLAST = 0x03FF
        # !NOCLIPBOARD

        """
        * Defines for the fVirt field of the Accelerator table structure.
        """

        FVIRTKEY = TRUE # Assumed to be == TRUE
        FNOINVERT = 0x02
        FSHIFT = 0x04
        FCONTROL = 0x08
        FALT = 0x10

        # REGION *** Desktop Family ***

        class tagACCEL(CStructure):
            _fields_ = [
                ("fVirt", BYTE),
                ("key", WORD),
                ("cmd", WORD)
            ]
        ACCEL = tagACCEL
        LPACCEL = POINTER(ACCEL)

        class tagPAINTSTRUCT(CStructure):
            _fields_ = [
                ("hdc", HDC),
                ("fErase", BOOL),
                ("rcPaint", RECT),
                ("fRestore", BOOL),
                ("fIncUpdate", BOOL),
                ("rgbReserved", BYTE * 32)
            ]
        PAINTSTRUCT = tagPAINTSTRUCT
        PPAINTSTRUCT = POINTER(PAINTSTRUCT)
        NPPAINTSTRUCT = PPAINTSTRUCT
        LPPAINTSTRUCT = PPAINTSTRUCT

        # REGION ***

        # REGION *** Desktop Family ***

        class tagWINDOWPLACEMENT(CStructure):
            _fields_ = [
                ("length", UINT),
                ("flags", UINT),
                ("showCmd", UINT),
                ("ptMinPosition", POINT),
                ("ptMaxPosition", POINT),
                ("rcNormalPosition", RECT)
            ]
        WINDOWPLACEMENT = tagWINDOWPLACEMENT
        PWINDOWPLACEMENT = POINTER(WINDOWPLACEMENT)
        LPWINDOWPLACEMENT = PWINDOWPLACEMENT

        WPF_SETMINPOSITION = 0x0001
        WPF_RESTORETOMAXIMIZED = 0x0002
        WPF_ASYNCWINDOWPLACEMENT = 0x0004
        # _WIN32_WINNT >= 0x0500

        # REGION ***

        # REGION *** Application Family or OneCore Family ***

        class tagNMHDR(CStructure):
            _fields_ = [
                ("hwndFrom", HWND),
                ("idFrom", UINT_PTR),
                ("code", UINT) # NM_CODE
            ]
        NMHDR = tagNMHDR

        # REGION ***

        # REGION *** Desktop Family ***

        LPNMHDR = POINTER(NMHDR)

        class tagSTYLESTRUCT(CStructure):
            _fields_ = [
                ("styleOld", DWORD),
                ("styleNew", DWORD)
            ]
        STYLESTRUCT = tagSTYLESTRUCT
        LPSTYLESTRUCT = POINTER(STYLESTRUCT)

        # REGION ***

        """
        * Owner draw control types
        """

        ODT_MENU = 1
        ODT_LISTBOX = 2
        ODT_COMBOBOX = 3
        ODT_BUTTON = 4
        ODT_STATIC = 5

        """
        * Owner draw actions
        """

        ODA_DRAWENTIRE = 0x0001
        ODA_SELECT = 0x0002
        ODA_FOCUS = 0x0004

        """
        * Owner draw state
        """

        ODS_SELECTED = 0x0001
        ODS_GRAYED = 0x0002
        ODS_DISABLED = 0x0004
        ODS_CHECKED = 0x0008
        ODS_FOCUS = 0x0010
        ODS_DEFAULT = 0x0020
        ODS_COMBOBOXEDIT = 0x1000
        ODS_HOTLIGHT = 0x0040
        ODS_INACTIVE = 0x0080
        ODS_NOACCEL = 0x0100
        ODS_NOFOCUSRECT = 0x0200

        # REGION *** Desktop Family ***

        """
        * MEASUREITEMSTRUCT for ownerdraw
        """
        class tagMEASUREITEMSTRUCT(CStructure):
            _fields_ = [
                ("CtlType", UINT),
                ("CtlID", UINT),
                ("itemID", UINT),
                ("itemWidth", UINT),
                ("itemHeight", UINT),
                ("itemData", ULONG_PTR)
            ]
        MEASUREITEMSTRUCT = tagMEASUREITEMSTRUCT
        PMEASUREITEMSTRUCT = POINTER(MEASUREITEMSTRUCT)
        LPMEASUREITEMSTRUCT = PMEASUREITEMSTRUCT

        """
        * DRAWITEMSTRUCT for ownerdraw
        """
        class tagDRAWITEMSTRUCT(CStructure):
            _fields_ = [
                ("CtlType", UINT),
                ("CtlID", UINT),
                ("itemID", UINT),
                ("itemAction", UINT),
                ("itemState", UINT),
                ("hwndItem", HWND),
                ("hDC", HDC),
                ("rcItem", RECT),
                ("itemData", ULONG_PTR)
            ]
        DRAWITEMSTRUCT = tagDRAWITEMSTRUCT
        PDRAWITEMSTRUCT = POINTER(DRAWITEMSTRUCT)
        LPDRAWITEMSTRUCT = PDRAWITEMSTRUCT

        """
        * DELETEITEMSTRUCT for ownerdraw
        """
        class tagDELETEITEMSTRUCT(CStructure):
            _fields_ = [
                ("CtlType", UINT),
                ("CtlID", UINT),
                ("itemID", UINT),
                ("hwndItem", HWND),
                ("itemData", ULONG_PTR)
            ]
        DELETEITEMSTRUCT = tagDELETEITEMSTRUCT
        PDELETEITEMSTRUCT = POINTER(DELETEITEMSTRUCT)
        LPDELETEITEMSTRUCT = PDELETEITEMSTRUCT

        """
        * COMPAREITEMSTUCT for ownerdraw sorting
        """
        class tagCOMPAREITEMSTRUCT(CStructure):
            _fields_ = [
                ("CtlType", UINT),
                ("CtlID", UINT),
                ("hwndItem", HWND),
                ("itemID1", UINT),
                ("itemData1", ULONG_PTR),
                ("itemID2", UINT),
                ("itemData2", ULONG_PTR),
                ("dwLocaleId", DWORD)
            ]
        COMPAREITEMSTRUCT = tagCOMPAREITEMSTRUCT
        PCOMPAREITEMSTRUCT = POINTER(COMPAREITEMSTRUCT)
        LPCOMPAREITEMSTRUCT = PCOMPAREITEMSTRUCT

        # REGION ***

        if cpreproc.ifndef("NOMSG"):

            # REGION *** Desktop Family or Games Family ***

            """
            * Message Function Templates
            """

            GetMessageA = declare(user32.GetMessageA, BOOL, LPMSG, HWND, UINT, UINT)
            GetMessageW = declare(user32.GetMessageW, BOOL, LPMSG, HWND, UINT, UINT)
            GetMessage = unicode(GetMessageW, GetMessageA)

            TranslateMessage = declare(user32.TranslateMessage, BOOL, LPMSG)

            DispatchMessageA = declare(user32.DispatchMessageA, LRESULT, LPMSG)
            DispatchMessageW = declare(user32.DispatchMessageW, LRESULT, LPMSG)
            DispatchMessage = unicode(DispatchMessageW, DispatchMessageA)

            # REGION ***

            # REGION *** Desktop Family ***

            SetMessageQueue = declare(user32.SetMessageQueue, BOOL, INT)

            # REGION ***

            # REGION *** Desktop Family or Games Family ***

            PeekMessageA = declare(user32.PeekMessageA, BOOL, LPMSG, HWND, UINT, UINT, UINT)
            PeekMessageW = declare(user32.PeekMessageW, BOOL, LPMSG, HWND, UINT, UINT, UINT)
            PeekMessage = unicode(PeekMessageW, PeekMessageA)

            # REGION ***

            """
            * Queue status flags for GetQueueStatus() and MsgWaitForMultipleObjects()
            """

            QS_KEY = 0x0001
            QS_MOUSEMOVE = 0x0002
            QS_MOUSEBUTTON = 0x0004
            QS_POSTMESSAGE = 0x0008
            QS_TIMER = 0x0010
            QS_PAINT = 0x0020
            QS_SENDMESSAGE = 0x0040
            QS_HOTKEY = 0x0080
            QS_ALLPOSTMESSAGE = 0x0100
            QS_RAWINPUT = 0x0400
            QS_TOUCH = 0x0800
            QS_POINTER = 0x1000
            QS_MOUSE = (QS_MOUSEMOVE | 
                        QS_MOUSEBUTTON)
            QS_INPUT = (QS_MOUSE    | 
                        QS_KEY      |
                        QS_RAWINPUT |
                        QS_TOUCH    | 
                        QS_POINTER)
            QS_INPUT = (QS_MOUSE | 
                        QS_KEY   |
                        QS_RAWINPUT)
            QS_INPUT = (QS_MOUSE | 
                        QS_KEY)
            QS_ALLEVENTS = (QS_INPUT       |
                            QS_POSTMESSAGE |
                            QS_TIMER       | 
                            QS_PAINT       | 
                            QS_HOTKEY)
            QS_ALLINPUT = (QS_INPUT       | 
                        QS_POSTMESSAGE | 
                        QS_TIMER       | 
                        QS_PAINT       | 
                        QS_HOTKEY      | 
                        QS_SENDMESSAGE)

            """
            * PeekMessage() Options
            """

            PM_NOREMOVE = 0x0000
            PM_REMOVE = 0x0001
            PM_NOYIELD = 0x0002
            PM_QS_INPUT = (QS_INPUT << 16)
            PM_QS_POSTMESSAGE = ((QS_POSTMESSAGE | QS_HOTKEY | QS_TIMER) << 16)
            PM_QS_PAINT = (QS_PAINT << 16)
            PM_QS_SENDMESSAGE = (QS_SENDMESSAGE << 16)
        # !NOMSG

        # REGION *** Desktop Family ***

        RegisterHotKey = declare(user32.RegisterHotKey, BOOL, HWND, INT, UINT, UINT)

        UnregisterHotKey = declare(user32.UnregisterHotKey, BOOL, HWND, INT)

        # REGION ***

        MOD_ALT = 0x0001
        MOD_CONTROL = 0x0002
        MOD_SHIFT = 0x0004
        MOD_WIN = 0x0008
        MOD_NOREPEAT = 0x4000
        IDHOT_SNAPWINDOW = (-1) # SHIFT-PRINTSCRN
        IDHOT_SNAPDESKTOP = (-2) # PRINTSCRN
        if cpreproc.ifdef("WIN_INTERNAL"):
            if cpreproc.ifndef("LSTRING"):
                cpreproc.define("NOLSTRING")
            # LSTRING
            if cpreproc.ifndef("LFILEIO"):
                cpreproc.define("NOLFILEIO")
            # LFILEIO
        # WIN_INTERNAL
        ENDSESSION_CLOSEAPP = 0x00000001
        ENDSESSION_CRITICAL = 0x40000000
        ENDSESSION_LOGOFF = 0x80000000
        EWX_LOGOFF = 0x00000000
        EWX_SHUTDOWN = 0x00000001
        EWX_REBOOT = 0x00000002
        EWX_FORCE = 0x00000004
        EWX_POWEROFF = 0x00000008
        EWX_FORCEIFHUNG = 0x00000010
        EWX_QUICKRESOLVE = 0x00000020
        EWX_RESTARTAPPS = 0x00000040
        EWX_HYBRID_SHUTDOWN = 0x00400000
        EWX_BOOTOPTIONS = 0x01000000
        EWX_ARSO = 0x04000000

        # REGION *** Desktop Family ***

        ExitWindowsEx = declare(user32.ExitWindowsEx, BOOL, UINT, DWORD)
        ExitWindows = lambda dwReserved=0, code=0: ExitWindowsEx(EWX_LOGOFF, MAXUINT_PTR)

        SwapMouseButton = declare(user32.SwapMouseButton, BOOL, BOOL)

        GetMessagePos = declare(user32.GetMessagePos, DWORD, VOID)
        
        GetMessageTime = declare(user32.GetMessageTime, LONG, VOID)

        GetMessageExtraInfo = declare(user32.GetMessageExtraInfo, LPARAM, VOID)

        GetUnpredictedMessagePos = declare(user32.GetUnpredictedMessagePos, DWORD, VOID)

        IsWow64Message = declare(user32.IsWow64Message, BOOL, VOID)

        SetMessageExtraInfo = declare(user32.SetMessageExtraInfo, LPARAM, LPARAM)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        SendMessageA = declare(user32.SendMessageA, LRESULT, HWND, UINT, WPARAM, LPARAM)
        SendMessageW = declare(user32.SendMessageW, LRESULT, HWND, UINT, WPARAM, LPARAM)
        SendMessage = unicode(SendMessageW, SendMessageA)

        # REGION ***

        # REGION *** Desktop Family ***

        SendMessageTimeoutA = declare(user32.SendMessageTimeoutA, LRESULT, HWND, UINT, WPARAM, LPARAM, UINT, UINT, PDWORD_PTR)
        SendMessageTimeoutW = declare(user32.SendMessageTimeoutW, LRESULT, HWND, UINT, WPARAM, LPARAM, UINT, UINT, PDWORD_PTR)
        SendMessageTimeout = unicode(SendMessageTimeoutW, SendMessageTimeoutA)

        SendNotifyMessageA = declare(user32.SendNotifyMessageA, BOOL, HWND, UINT, WPARAM, LPARAM)
        SendNotifyMessageW = declare(user32.SendNotifyMessageW, BOOL, HWND, UINT, WPARAM, LPARAM)
        SendNotifyMessage = unicode(SendNotifyMessageW, SendNotifyMessageA)

        SendMessageCallbackA = declare(user32.SendMessageCallbackA, BOOL, HWND, UINT, WPARAM, LPARAM, SENDASYNCPROC, ULONG_PTR)
        SendMessageCallbackW = declare(user32.SendMessageCallbackW, BOOL, HWND, UINT, WPARAM, LPARAM, SENDASYNCPROC, ULONG_PTR)
        SendMessageCallback = unicode(SendMessageCallbackW, SendMessageCallbackA)

        class BSMINFO(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("hdesk", HDESK),
                ("hwnd", HWND),
                ("luid", LUID)
            ]
        PBSMINFO = POINTER(BSMINFO)

        BroadcastSystemMessageExA = declare(user32.BroadcastSystemMessageExA, LONG, DWORD, LPDWORD, UINT, WPARAM, LPARAM, PBSMINFO)
        BroadcastSystemMessageExW = declare(user32.BroadcastSystemMessageExW, LONG, DWORD, LPDWORD, UINT, WPARAM, LPARAM, PBSMINFO)
        BroadcastSystemMessageEx = unicode(BroadcastSystemMessageExW, BroadcastSystemMessageExA)

        # REGION ***

        # REGION *** Desktop Family ***

        BroadcastSystemMessageA = declare(user32.BroadcastSystemMessageA, LONG, DWORD, LPDWORD, UINT, WPARAM, LPARAM)
        BroadcastSystemMessageW = declare(user32.BroadcastSystemMessageW, LONG, DWORD, LPDWORD, UINT, WPARAM, LPARAM)
        BroadcastSystemMessage = unicode(BroadcastSystemMessageW, BroadcastSystemMessageA)

        # REGION ***

        BSM_ALLCOMPONENTS = 0x00000000
        BSM_VXDS = 0x00000001
        BSM_NETDRIVER = 0x00000002
        BSM_INSTALLABLEDRIVERS = 0x00000004
        BSM_APPLICATIONS = 0x00000008
        BSM_ALLDESKTOPS = 0x00000010
        BSF_QUERY = 0x00000001
        BSF_IGNORECURRENTTASK = 0x00000002
        BSF_FLUSHDISK = 0x00000004
        BSF_NOHANG = 0x00000008
        BSF_POSTMESSAGE = 0x00000010
        BSF_FORCEIFHUNG = 0x00000020
        BSF_NOTIMEOUTIFNOTHUNG = 0x00000040
        BSF_ALLOWSFW = 0x00000080
        BSF_SENDNOTIFYMESSAGE = 0x00000100
        BSF_RETURNHDESK = 0x00000200
        BSF_LUID = 0x00000400
        BROADCAST_QUERY_DENY = 0x424D5144 # Return this value to deny a query.
        # WINVER >= 0x0400

        # REGION *** Desktop Family ***

        HDEVNOTIFY = HANDLE
        PHDEVNOTIFY = PHANDLE

        DEVICE_NOTIFY_WINDOW_HANDLE = 0x00000000
        DEVICE_NOTIFY_SERVICE_HANDLE = 0x00000001
        DEVICE_NOTIFY_ALL_INTERFACE_CLASSES = 0x00000004
        # _WIN32_WINNT >= 0x0501

        RegisterDeviceNotificationA = declare(user32.RegisterDeviceNotificationA, HDEVNOTIFY, HANDLE, LPVOID, DWORD)
        RegisterDeviceNotificationW = declare(user32.RegisterDeviceNotificationW, HDEVNOTIFY, HANDLE, LPVOID, DWORD)
        RegisterDeviceNotification = unicode(RegisterDeviceNotificationW, RegisterDeviceNotificationA)

        UnregisterDeviceNotification = declare(user32.UnregisterDeviceNotification, BOOL, HDEVNOTIFY)

        if cpreproc.pragma_once("_HPOWERNOTIFY_DEF_"):
            HPOWERNOTIFY = HANDLE
            PHPOWERNOTIFY = PHANDLE
        
        RegisterPowerSettingNotification = declare(user32.RegisterPowerSettingNotification, HPOWERNOTIFY, HANDLE, LPCGUID, DWORD)

        UnregisterPowerSettingNotification = declare(user32.UnregisterPowerSettingNotification, BOOL, HPOWERNOTIFY)

        RegisterSuspendResumeNotification = declare(user32.RegisterSuspendResumeNotification, HPOWERNOTIFY, HANDLE, DWORD)

        UnregisterSuspendResumeNotification = declare(user32.UnregisterSuspendResumeNotification, BOOL, HPOWERNOTIFY)

        # REGION ***

        # REGION *** Desktop Family ***

        PostMessageA = declare(user32.PostMessageA, BOOL, HWND, UINT, WPARAM, LPARAM)
        PostMessageW = declare(user32.PostMessageW, BOOL, HWND, UINT, WPARAM, LPARAM)
        PostMessage = unicode(PostMessageW, PostMessageA)

        PostThreadMessageA = declare(user32.PostThreadMessageA, BOOL, DWORD, UINT, WPARAM, LPARAM)
        PostThreadMessageW = declare(user32.PostThreadMessageW, BOOL, DWORD, UINT, WPARAM, LPARAM)
        PostThreadMessage = unicode(PostThreadMessageW, PostThreadMessageA)

        # REGION ***

        PostAppMessageA = lambda idThread, wMsg, wParam, lParam: PostThreadMessageA(DWORD(idThread), wMsg, wParam, lParam)
        PostAppMessageW = lambda idThread, wMsg, wParam, lParam: PostThreadMessageW(DWORD(idThread), wMsg, wParam, lParam)
        PostAppMessage = unicode(PostAppMessageW, PostAppMessageA)

        """
        * Special HWND value for use with PostMessage() and SendMessage()
        """

        HWND_BROADCAST = HWND(0xFFFF)
        HWND_MESSAGE = HWND(-3)

        # REGION *** Desktop Family ***

        AttachThreadInput = declare(user32.AttachThreadInput, BOOL, DWORD, DWORD, BOOL)

        ReplyMessage = declare(user32.ReplyMessage, BOOL, LRESULT)

        WaitMessage = declare(user32.WaitMessage, BOOL, VOID)

        WaitForInputIdle = declare(user32.WaitForInputIdle, DWORD, HANDLE, DWORD)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        DefWindowProcA = declare(user32.DefWindowProcA, LRESULT, HWND, UINT, WPARAM, LPARAM)
        DefWindowProcW = declare(user32.DefWindowProcW, LRESULT, HWND, UINT, WPARAM, LPARAM)
        DefWindowProc = unicode(DefWindowProcW, DefWindowProcA)

        PostQuitMessage = declare(user32.PostQuitMessage, VOID, INT)

        CallWindowProcA = declare(user32.CallWindowProcA, LRESULT, WNDPROC, HWND, UINT, WPARAM, LPARAM)
        CallWindowProcW = declare(user32.CallWindowProcW, LRESULT, WNDPROC, HWND, UINT, WPARAM, LPARAM)
        CallWindowProc = unicode(CallWindowProcW, CallWindowProcA)

        # REGION ***

        # REGION *** Desktop Family ***

        InSendMessage = declare(user32.InSendMessage, BOOL, VOID)

        # REGION ***

        # REGION *** Desktop Family ***

        InSendMessageEx = declare(user32.InSendMessageEx, DWORD, LPVOID)

        # REGION ***

        """
        * InSendMessageEx return value
        """

        ISMEX_NOSEND = 0x00000000
        ISMEX_SEND = 0x00000001
        ISMEX_NOTIFY = 0x00000002
        ISMEX_CALLBACK = 0x00000004
        ISMEX_REPLIED = 0x00000008
        # WINVER >= 0x0500

        # REGION *** Desktop Family ***

        GetDoubleClickTime = declare(user32.GetDoubleClickTime, UINT, VOID)

        SetDoubleClickTime = declare(user32.SetDoubleClickTime, BOOL, UINT)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        RegisterClassA = declare(user32.RegisterClassA, ATOM, LPWNDCLASSA)
        RegisterClassW = declare(user32.RegisterClassW, ATOM, LPWNDCLASSW)
        RegisterClass = unicode(RegisterClassW, RegisterClassA)

        UnregisterClassA = declare(user32.UnregisterClassA, BOOL, LPCSTR, HINSTANCE)
        UnregisterClassW = declare(user32.UnregisterClassW, BOOL, LPCWSTR, HINSTANCE)
        UnregisterClass = unicode(UnregisterClassW, UnregisterClassA)

        # REGION ***

        # REGION *** Desktop Family ***

        GetClassInfoA = declare(user32.GetClassInfoA, BOOL, HINSTANCE, LPCSTR, LPWNDCLASSA)
        GetClassInfoW = declare(user32.GetClassInfoW, BOOL, HINSTANCE, LPCWSTR, LPWNDCLASSW)
        GetClassInfo = unicode(GetClassInfoW, GetClassInfoA)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        RegisterClassExA = declare(user32.RegisterClassExA, ATOM, LPWNDCLASSEXA)
        RegisterClassExW = declare(user32.RegisterClassExW, ATOM, LPWNDCLASSEXW)
        RegisterClassEx = unicode(RegisterClassExW, RegisterClassExA)

        # REGION ***
        
        # REGION *** Desktop Family ***

        GetClassInfoExA = declare(user32.GetClassInfoExA, BOOL, HINSTANCE, LPCSTR, LPWNDCLASSEXA)
        GetClassInfoExW = declare(user32.GetClassInfoExW, BOOL, HINSTANCE, LPCWSTR, LPWNDCLASSEXW)
        GetClassInfoEx = unicode(GetClassInfoExW, GetClassInfoExA)

        # REGION ***

        CW_USEDEFAULT = INT(0x80000000)

        """
        * Special value for CreateWindow, et al.
        """
        HWND_DESKTOP = HWND(0)

        # REGION *** Desktop Family or Games Family ***

        PREGISTERCLASSNAMEW = WINAPI(BOOLEAN, LPCWSTR)

        CreateWindowExA = declare(user32.CreateWindowExA, HWND, DWORD, LPCSTR, LPCSTR, DWORD, INT, INT, INT, INT, HWND, HMENU, HINSTANCE, LPVOID)
        CreateWindowExW = declare(user32.CreateWindowExW, HWND, DWORD, LPCWSTR, LPCWSTR, DWORD, INT, INT, INT, INT, HWND, HMENU, HINSTANCE, LPVOID)
        CreateWindowEx = unicode(CreateWindowExW, CreateWindowExA)

        # REGION ***

        CreateWindowA = lambda lpClassName, lpWindowName, dwStyle, x, y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam: CreateWindowExA(0, lpClassName, lpWindowName, dwStyle, x, y,
                                nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)
        CreateWindowW = lambda lpClassName, lpWindowName, dwStyle, x, y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam: CreateWindowExW(0, lpClassName, lpWindowName, dwStyle, x, y,
                                nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam)
        
        CreateWindow = unicode(CreateWindowW, CreateWindowA)

        # REGION *** Desktop Family ***

        IsWindow = declare(user32.IsWindow, BOOL, HWND)

        IsMenu = declare(user32.IsMenu, BOOL, HMENU)

        IsChild = declare(user32.IsChild, BOOL, HWND, HWND)

        # REGION ***

        # REGION *** Desktop or Games Family ***

        DestroyWindow = declare(user32.DestroyWindow, BOOL, HWND)

        ShowWindow = declare(user32.ShowWindow, BOOL, HWND, INT)

        # REGION ***

        # REGION *** Desktop Family ***

        AnimateWindow = declare(user32.AnimateWindow, BOOL, HWND, DWORD, DWORD)

        # REGION ***

        if cpreproc.ifdef("_WINGDI_"):
            if cpreproc.ifndef("NOGDI"):

                # REGION *** Desktop Family ***

                UpdateLayeredWindow = declare(user32.UpdateLayeredWindow, HWND, HDC, PPOINT, PSIZE, HDC, PPOINT, COLORREF, PBLENDFUNCTION, DWORD)

                """
                * Layered Window Update information
                """
                class tagUPDATELAYEREDWINDOWINFO(CStructure):
                    _fields_ = [
                        ("cbSize", DWORD),
                        ("hdcDst", HDC),
                        ("pptDst", PPOINT),
                        ("psize", PSIZE),
                        ("hdcSrc", HDC),
                        ("pptSrc", PPOINT),
                        ("crKey", COLORREF),
                        ("pblend", PBLENDFUNCTION),
                        ("dwFlags", DWORD),
                        ("prcDirty", PRECT)
                    ]
                UPDATELAYEREDWINDOWINFO = tagUPDATELAYEREDWINDOWINFO
                PUPDATELAYEREDWINDOWINFO = POINTER(UPDATELAYEREDWINDOWINFO)

                UpdateLayeredWindowIndirect = declare(user32.UpdateLayeredWindowIndirect, BOOL, HWND, PUPDATELAYEREDWINDOWINFO)

                # REGION ***
            # !NOGDI
        # _WINGDI_

        # REGION *** Desktop Family ***
        
        GetLayeredWindowAttributes = declare(user32.GetLayeredWindowAttributes, BOOL, HWND, POINTER(COLORREF), PBYTE, PDWORD)

        PW_CLIENTONLY = 0x00000001
        PW_RENDERFULLCONTENT = 0x00000002

        PrintWindow = declare(user32.PrintWindow, BOOL, HWND, HDC, UINT)

        # REGION ***

        # REGION *** Desktop Family ***

        SetLayeredWindowAttributes = declare(user32.SetLayeredWindowAttributes, BOOL, HWND, COLORREF, BYTE, DWORD)

        # REGION ***

        LWA_COLORKEY = 0x00000001
        LWA_ALPHA = 0x00000002
        ULW_COLORKEY = 0x00000001
        ULW_ALPHA = 0x00000002
        ULW_OPAQUE = 0x00000004
        ULW_EX_NORESIZE = 0x00000008
        # _WIN32_WINNT >= 0x0500

        # REGION *** Desktop Family ***

        ShowWindowAsync = declare(user32.ShowWindowAsync, BOOL, HWND, INT)

        FlashWindow = declare(user32.FlashWindow, BOOL, HWND, BOOL)

        class FLASHWINFO(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("hwnd", HWND),
                ("dwFlags", DWORD),
                ("uCount", UINT),
                ("dwTimeout", DWORD)
            ]
        PFLASHWINFO = POINTER(FLASHWINFO)

        FlashWindowEx = declare(user32.FlashWindowEx, BOOL, PFLASHWINFO)

        ShowOwnedPopups = declare(user32.ShowOwnedPopups, BOOL, HWND, BOOL)

        OpenIcon = declare(user32.OpenIcon, BOOL, HWND)

        CloseWindow = declare(user32.CloseWindow, BOOL, HWND)

        # REGION ***

        # REGION *** Desktop Family ***

        MoveWindow = declare(user32.MoveWindow, BOOL, HWND, INT, INT, INT, INT, BOOL)

        SetWindowPos = declare(user32.SetWindowPos, BOOL, HWND, HWND, INT, INT, INT, INT, UINT)

        # REGION ***

        # REGION *** Desktop Family ***

        GetWindowPlacement = declare(user32.GetWindowPlacement, BOOL, HWND, PWINDOWPLACEMENT)

        SetWindowPlacement = declare(user32.SetWindowPlacement, BOOL, HWND, PWINDOWPLACEMENT)

        WDA_NONE = 0x00000000
        WDA_MONITOR = 0x00000001
        WDA_EXCLUDEFROMCAPTURE = 0x00000011

        GetWindowDisplayAffinity = declare(user32.GetWindowDisplayAffinity, BOOL, HWND, PDWORD)

        SetWindowDisplayAffinity = declare(user32.SetWindowDisplayAffinity, BOOL, HWND, DWORD)

        # REGION ***

        if cpreproc.ifndef("NODEFERWINDOWPOS"):
            # REGION *** Desktop Family ***

            BeginDeferWindowPos = declare(user32.BeginDeferWindowPos, HDWP, INT)

            DeferWindowPos = declare(user32.DeferWindowPos, HDWP, HDWP, HWND, HWND, INT, INT, INT, INT, UINT)

            EndDeferWindowPos = declare(user32.EndDeferWindowPos, BOOL, HDWP)

            # REGION ***
        # !NODEFERWINDOWPOS

        # REGION *** Desktop Family ***

        IsWindowVisible = declare(user32.IsWindowVisible, BOOL, HWND)

        # REGION ***

        # REGION *** Desktop Family ***

        IsIconic = declare(user32.IsIconic, BOOL, HWND)

        AnyPopup = declare(user32.AnyPopup, BOOL, VOID)

        BringWindowToTop = declare(user32.BringWindowToTop, BOOL, HWND)

        IsZoomed = declare(user32.IsZoomed, BOOL, HWND)

        # REGION ***

        """
        * SetWindowPos Flags
        """

        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        SWP_NOZORDER = 0x0004
        SWP_NOREDRAW = 0x0008
        SWP_NOACTIVATE = 0x0010
        SWP_FRAMECHANGED = 0x0020 # The frame changed: send WM_NCCALCSIZE
        SWP_SHOWWINDOW = 0x0040
        SWP_HIDEWINDOW = 0x0080
        SWP_NOCOPYBITS = 0x0100
        SWP_NOOWNERZORDER = 0x0200 # Don't do owner Z ordering
        SWP_NOSENDCHANGING = 0x0400 # Don't send WM_WINDOWPOSCHANGING
        SWP_DRAWFRAME = SWP_FRAMECHANGED
        SWP_NOREPOSITION = SWP_NOOWNERZORDER
        SWP_DEFERERASE = 0x2000
        SWP_ASYNCWINDOWPOS = 0x4000
        HWND_TOP = HWND(0)
        HWND_BOTTOM = HWND(1)
        HWND_TOPMOST = HWND(-1)
        HWND_NOTOPMOST = HWND(-2)
        if cpreproc.ifndef("NOCTLMGR"):
            # REGION *** Application Family or OneCore Family ***

            """
            * original NT 32 bit dialog template:
            """
            class DLGTEMPLATE(CStructure):
                _pack_ = 2
                _fields_ = [
                    ("style", DWORD),
                    ("dwExtendedStyle", DWORD),
                    ("cdit", WORD),
                    ("x", SHORT),
                    ("y", SHORT),
                    ("cx", SHORT),
                    ("cy", SHORT)
                ]

            # REGION ***

            # REGION *** Desktop Family ***

            LPDLGTEMPLATEA = POINTER(DLGTEMPLATE)
            LPDLGTEMPLATEW = POINTER(DLGTEMPLATE)
            LPDLGTEMPLATE = unicode(LPDLGTEMPLATEW, LPDLGTEMPLATEA)

            # REGION ***

            # REGION *** Application Family or OneCore Family ***

            LPCDLGTEMPLATEA = POINTER(DLGTEMPLATE)
            LPCDLGTEMPLATEW = POINTER(DLGTEMPLATE)
            LPCDLGTEMPLATE = unicode(LPCDLGTEMPLATEW, LPCDLGTEMPLATEA)

            # REGION ***

            # REGION *** Desktop Family ***

            """
            * 32 bit Dialog item template.
            """
            class DLGITEMTEMPLATE(CStructure):
                _pack_ = 2
                _fields_ = [
                    ("style", DWORD),
                    ("dwExtendedStyle", DWORD),
                    ("x", SHORT),
                    ("y", SHORT),
                    ("cx", SHORT),
                    ("cy", SHORT),
                    ("id", DWORD)
                ]
            PDLGITEMTEMPLATEA = POINTER(DLGITEMTEMPLATE)
            PDLGITEMTEMPLATEW = POINTER(DLGITEMTEMPLATE)
            PDLGITEMTEMPLATE = unicode(PDLGITEMTEMPLATEW, PDLGITEMTEMPLATEA)

            LPDLGITEMTEMPLATEA = POINTER(DLGITEMTEMPLATE)
            LPDLGITEMTEMPLATEW = POINTER(DLGITEMTEMPLATE)
            LPDLGITEMTEMPLATE = unicode(LPDLGITEMTEMPLATEW, LPDLGITEMTEMPLATEA)

            # REGION ***

            # REGION *** Desktop Family ***

            CreateDialogParamA = declare(user32.CreateDialogParamA, HWND, HINSTANCE, LPCSTR, HWND, DLGPROC, LPARAM)
            CreateDialogParamW = declare(user32.CreateDialogParamW, HWND, HINSTANCE, LPCWSTR, HWND, DLGPROC, LPARAM)
            CreateDialogParam = unicode(CreateDialogParamW, CreateDialogParamA)

            CreateDialogIndirectParamA = declare(user32.CreateDialogIndirectParamA, HWND, HINSTANCE, LPCDLGTEMPLATEA, HWND, DLGPROC, LPARAM)
            CreateDialogIndirectParamW = declare(user32.CreateDialogIndirectParamW, HWND, HINSTANCE, LPCDLGTEMPLATEW, HWND, DLGPROC, LPARAM)
            CreateDialogIndirectParam = unicode(CreateDialogIndirectParamW, CreateDialogIndirectParamA)

            CreateDialogA = lambda hInstance, lpName, hWndParent, lpDialogFunc: CreateDialogParamA(hInstance, lpName, 
                                                                                                hWndParent, lpDialogFunc, 0)
            CreateDialogW = lambda hInstance, lpName, hWndParent, lpDialogFunc: CreateDialogParamW(hInstance, lpName, 
                                                                                                hWndParent, lpDialogFunc, 0)
            CreateDialog = unicode(CreateDialogW, CreateDialogA)

            CreateDialogIndirectA = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: CreateDialogIndirectParamA(hInstance, lpTemplate, hWndParent, lpDialogFunc, 0)
            CreateDialogIndirectW = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: CreateDialogIndirectParamW(hInstance, lpTemplate, hWndParent, lpDialogFunc, 0)
            CreateDialogIndirect = unicode(CreateDialogIndirectW, CreateDialogIndirectA)

            DialogBoxParamA = declare(user32.DialogBoxParamA, INT_PTR, HINSTANCE, LPCSTR, HWND, DLGPROC, LPARAM)
            DialogBoxParamW = declare(user32.DialogBoxParamW, INT_PTR, HINSTANCE, LPCWSTR, HWND, DLGPROC, LPARAM)
            DialogBoxParam = unicode(DialogBoxParamW, DialogBoxParamA)

            DialogBoxIndirectParamA = declare(user32.DialogBoxIndirectParamA, INT_PTR, HINSTANCE, LPCDLGTEMPLATEA, HWND, DLGPROC, LPARAM)
            DialogBoxIndirectParamW = declare(user32.DialogBoxIndirectParamW, INT_PTR, HINSTANCE, LPCDLGTEMPLATEW, HWND, DLGPROC, LPARAM)
            DialogBoxIndirectParam = unicode(DialogBoxIndirectParamW, DialogBoxIndirectParamA)

            DialogBoxA = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: DialogBoxParamA(hInstance, lpTemplate, 
                                                                                                hWndParent, lpDialogFunc, 0)
            DialogBoxW = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: DialogBoxParamW(hInstance, lpTemplate, 
                                                                                                hWndParent, lpDialogFunc, 0)
            DialogBox = unicode(DialogBoxW, DialogBoxA)

            DialogBoxIndirectA = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: DialogBoxIndirectParamA(hInstance, lpTemplate, 
                                                                                                                hWndParent, lpDialogFunc, 0)
            DialogBoxIndirectW = lambda hInstance, lpTemplate, hWndParent, lpDialogFunc: DialogBoxIndirectParamW(hInstance, lpTemplate, 
                                                                                                                hWndParent, lpDialogFunc, 0)
            DialogBoxIndirect = unicode(DialogBoxIndirectW, DialogBoxIndirectA)

            EndDialog = declare(user32.EndDialog, BOOL, HWND, INT_PTR)

            GetDlgItem = declare(user32.GetDlgItem, HWND, HWND, INT)

            SetDlgItemInt = declare(user32.SetDlgItemInt, BOOL, HWND, INT, UINT, BOOL)

            GetDlgItemInt = declare(user32.GetDlgItemInt, BOOL, HWND, INT, PBOOL, BOOL)

            SetDlgItemTextA = declare(user32.SetDlgItemTextA, BOOL, HWND, INT, LPCSTR)
            SetDlgItemTextW = declare(user32.SetDlgItemTextW, BOOL, HWND, INT, LPCWSTR)
            SetDlgItemText = unicode(SetDlgItemTextW, SetDlgItemTextA)

            GetDlgItemTextA = declare(user32.GetDlgItemTextA, UINT, HWND, INT, LPSTR, INT)
            GetDlgItemTextW = declare(user32.GetDlgItemTextW, UINT, HWND, INT, LPWSTR, INT)
            GetDlgItemText = unicode(GetDlgItemTextW, GetDlgItemTextA)

            CheckDlgButton = declare(user32.CheckDlgButton, BOOL, HWND, INT, UINT)

            CheckRadioButton = declare(user32.CheckDlgButton, BOOL, HWND, INT, INT, INT)

            IsDlgButtonChecked = declare(user32.CheckDlgButton, UINT, HWND, INT)

            SendDlgItemMessageA = declare(user32.SendDlgItemMessageA, LRESULT, HWND, INT, UINT, WPARAM, LPARAM)
            SendDlgItemMessageW = declare(user32.SendDlgItemMessageW, LRESULT, HWND, INT, UINT, WPARAM, LPARAM)
            SendDlgItemMessage = unicode(SendDlgItemMessageW, SendDlgItemMessageA)

            GetNextDlgGroupItem = declare(user32.GetNextDlgGroupItem, HWND, HWND, HWND, BOOL)

            GetNextDlgTabItem = declare(user32.GetNextDlgTabItem, HWND, HWND, HWND, BOOL)

            GetDlgCtrlID = declare(user32.GetDlgCtrlID, INT, HWND)

            GetDialogBaseUnits = declare(user32.GetDialogBaseUnits, LONG, VOID)

            DefDlgProcA = declare(user32.DefDlgProcA, LRESULT, HWND, UINT, WPARAM, LPARAM)
            DefDlgProcW = declare(user32.DefDlgProcW, LRESULT, HWND, UINT, WPARAM, LPARAM)
            DefDlgProc = unicode(DefDlgProcW, DefDlgProcA)

            DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS = INT
            if True:
                DCDC_DEFAULT                  = 0x0000
                DCDC_DISABLE_FONT_UPDATE      = 0x0001
                DCDC_DISABLE_RELAYOUT         = 0x0002

            SetDialogControlDpiChangeBehavior = declare(user32.SetDialogControlDpiChangeBehavior, BOOL,
                                                        HWND, DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS,
                                                        DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS)
            
            GetDialogControlDpiChangeBehavior = declare(user32.GetDialogControlDpiChangeBehavior,
                                                        DIALOG_CONTROL_DPI_CHANGE_BEHAVIORS, HWND)
            
            DIALOG_DPI_CHANGE_BEHAVIORS = INT
            if True:
                DDC_DEFAULT                     = 0x0000
                DDC_DISABLE_ALL                 = 0x0001
                DDC_DISABLE_RESIZE              = 0x0002
                DDC_DISABLE_CONTROL_RELAYOUT    = 0x0004

            SetDialogDpiChangeBehavior = declare(user32.SetDialogDpiChangeBehavior, BOOL,
                                                        HWND, DIALOG_DPI_CHANGE_BEHAVIORS,
                                                        DIALOG_DPI_CHANGE_BEHAVIORS)
            
            GetDialogDpiChangeBehavior = declare(user32.GetDialogDpiChangeBehavior,
                                                        DIALOG_DPI_CHANGE_BEHAVIORS, HWND)

            # REGION ***
        # !NOCTLMGR

        # REGION *** Desktop Family ***

        if cpreproc.ifndef("NOMSG"):
            CallMsgFilterA = declare(user32.CallMsgFilterA, BOOL, LPMSG, INT)
            CallMsgFilterW = declare(user32.CallMsgFilterW, BOOL, LPMSG, INT)
            CallMsgFilter = unicode(CallMsgFilterW, CallMsgFilterA)
        # !NOMSG

        if cpreproc.ifndef("NOCLIPBOARD"):

            """
            * Clipboard Manager Functions
            """

            OpenClipboard = declare(user32.OpenClipboard, BOOL, HWND)

            CloseClipboard = declare(user32.CloseClipboard, BOOL, VOID)

            GetClipboardSequenceNumber = declare(user32.GetClipboardSequenceNumber, DWORD, VOID)

            GetClipboardOwner = declare(user32.GetClipboardOwner, HWND, VOID)

            SetClipboardViewer = declare(user32.SetClipboardViewer, HWND, HWND)

            GetClipboardViewer = declare(user32.GetClipboardViewer, HWND, VOID)

            ChangeClipboardChain = declare(user32.ChangeClipboardChain, BOOL, HWND, HWND)

            SetClipboardData = declare(user32.SetClipboardData, HANDLE, UINT, HANDLE)

            GetClipboardData = declare(user32.GetClipboardData, HANDLE, UINT)

            RegisterClipboardFormatA = declare(user32.RegisterClipboardFormatA, UINT, LPCSTR)
            RegisterClipboardFormatW = declare(user32.RegisterClipboardFormatW, UINT, LPCWSTR)
            RegisterClipboardFormat = unicode(RegisterClipboardFormatW, RegisterClipboardFormatA)

            CountClipboardFormats = declare(user32.CountClipboardFormats, INT, VOID)

            EnumClipboardFormats = declare(user32.EnumClipboardFormats, UINT, UINT)

            GetClipboardFormatNameA = declare(user32.GetClipboardFormatNameA, INT, UINT, LPSTR, INT)
            GetClipboardFormatNameW = declare(user32.GetClipboardFormatNameW, INT, UINT, LPWSTR, INT)
            GetClipboardFormatName = unicode(GetClipboardFormatNameW, GetClipboardFormatNameA)

            EmptyClipboard = declare(user32.EmptyClipboard, BOOL, VOID)

            IsClipboardFormatAvailable = declare(user32.IsClipboardFormatAvailable, BOOL, UINT)

            GetPriorityClipboardFormat = declare(user32.GetPriorityClipboardFormat, INT, UINT, INT)

            GetOpenClipboardWindow = declare(user32.GetOpenClipboardWindow, HWND, VOID)

            AddClipboardFormatListener = declare(user32.AddClipboardFormatListener, BOOL, HWND)

            RemoveClipboardFormatListener = declare(user32.RemoveClipboardFormatListener, BOOL, HWND)

            GetUpdatedClipboardFormats = declare(user32.GetUpdatedClipboardFormats, BOOL, PUINT, UINT, PUINT)
            """
            * Character Translation Routines
            """

            CharToOemA = declare(user32.CharToOemA, BOOL, LPCSTR, LPSTR)
            CharToOemW = declare(user32.CharToOemW, BOOL, LPCWSTR, LPSTR)
            CharToOem = unicode(CharToOemW, CharToOemA)

            OemToCharA = declare(user32.OemToCharA, BOOL, LPCSTR, LPSTR)
            OemToCharW = declare(user32.OemToCharW, BOOL, LPCSTR, LPWSTR)
            OemToChar = unicode(OemToCharW, OemToCharA)
            
            CharToOemBuffA = declare(user32.CharToOemBuffA, BOOL, LPCSTR, LPSTR, DWORD)
            CharToOemBuffW = declare(user32.CharToOemBuffW, BOOL, LPCWSTR, LPSTR, DWORD)
            CharToOemBuff = unicode(CharToOemBuffW, CharToOemBuffA)
            
            OemToCharBuffA = declare(user32.OemToCharBuffA, BOOL, LPCSTR, LPSTR, DWORD)
            OemToCharBuffW = declare(user32.OemToCharBuffW, BOOL, LPCSTR, LPWSTR, DWORD)
            OemToCharBuff = unicode(OemToCharBuffW, OemToCharBuffA)

            # REGION ***

            # REGION *** Desktop Family or OneCore Family ***
        # !NOCLIPBOARD

        CharUpperA = declare(user32.CharUpperA, LPSTR, LPSTR)
        CharUpperW = declare(user32.CharUpperW, LPWSTR, LPWSTR)
        CharUpper = unicode(CharUpperW, CharUpperA)

        CharUpperBuffA = declare(user32.CharUpperBuffA, DWORD, LPSTR, DWORD)
        CharUpperBuffW = declare(user32.CharUpperBuffW, DWORD, LPWSTR, DWORD)
        CharUpperBuff = unicode(CharUpperBuffW, CharUpperBuffA)

        CharLowerA = declare(user32.CharLowerA, LPSTR, LPSTR)
        CharLowerW = declare(user32.CharLowerW, LPWSTR, LPWSTR)
        CharLower = unicode(CharLowerW, CharLowerA)
        
        CharLowerBuffA = declare(user32.CharLowerBuffA, DWORD, LPSTR, DWORD)
        CharLowerBuffW = declare(user32.CharLowerBuffW, DWORD, LPWSTR, DWORD)
        CharLowerBuff = unicode(CharLowerBuffW, CharLowerBuffA)
        
        CharNextA = declare(user32.CharNextA, LPSTR, LPCSTR)
        CharNextW = declare(user32.CharNextW, LPWSTR, LPCWSTR)
        CharNext = unicode(CharNextW, CharNextA)
        
        CharPrevA = declare(user32.CharPrevA, LPSTR, LPCSTR, LPCSTR)
        CharPrevW = declare(user32.CharPrevW, LPWSTR, LPCWSTR, LPCWSTR)
        CharPrev = unicode(CharPrevW, CharPrevA)
        
        CharNextExA = declare(user32.CharNextExA, LPSTR, WORD, LPCSTR, DWORD)
        CharPrevExA = declare(user32.CharPrevExA, LPSTR, WORD, LPCSTR, LPCSTR, DWORD)

        # REGION ***

        """
        * Compatibility defines for character translation routines
        """

        AnsiToOem = CharToOemA
        OemToAnsi = OemToCharA
        AnsiToOemBuff = CharToOemBuffA
        OemToAnsiBuff = OemToCharBuffA
        AnsiUpper = CharUpperA
        AnsiUpperBuff = CharUpperBuffA
        AnsiLower = CharLowerA
        AnsiLowerBuff = CharLowerBuffA
        AnsiNext = CharNextA
        AnsiPrev = CharPrevA

        # REGION *** Desktop or OneCore Family ***

        if cpreproc.ifndef(" NOLANGUAGE"):

            """
            * Language dependent Routines
            """

            IsCharAlphaA = declare(user32.IsCharAlphaA, BOOL, CHAR)
            IsCharAlphaW = declare(user32.IsCharAlphaW, BOOL, WCHAR)
            IsCharAlpha = unicode(IsCharAlphaW, IsCharAlphaA)

            IsCharAlphaNumericA = declare(user32.IsCharAlphaNumericA, BOOL, CHAR)
            IsCharAlphaNumericW = declare(user32.IsCharAlphaNumericW, BOOL, WCHAR)
            IsCharAlphaNumeric = unicode(IsCharAlphaNumericW, IsCharAlphaNumericA)

            IsCharUpperA = declare(user32.IsCharUpperA, BOOL, CHAR)
            IsCharUpperW = declare(user32.IsCharUpperW, BOOL, WCHAR)
            IsCharUpper = unicode(IsCharUpperW, IsCharUpperA)

            IsCharLowerA = declare(user32.IsCharLowerA, BOOL, CHAR)
            IsCharLowerW = declare(user32.IsCharLowerW, BOOL, WCHAR)
            IsCharLower = unicode(IsCharLowerW, IsCharLowerA)

        # !NOLANGUAGE

        # REGION ***

        # REGION *** Desktop Family ***

        SetFocus = declare(user32.SetFocus, HWND, HWND)
        GetActiveWindow = declare(user32.GetActiveWindow, HWND, VOID)
        GetFocus = declare(user32.GetFocus, HWND, VOID)
        GetKBCodePage = declare(user32.GetKBCodePage, UINT, VOID)
        GetKeyState = declare(user32.GetKeyState, SHORT, INT)
        GetAsyncKeyState = declare(user32.GetAsyncKeyState, SHORT, INT)
        GetKeyboardState = declare(user32.GetKeyboardState, BOOL, PBYTE)
        SetKeyboardState = declare(user32.SetKeyboardState, BOOL, LPBYTE)

        # REGION ***

        # REGION ***  Desktop or PC Family ***

        GetKeyNameTextA = declare(user32.GetKeyNameTextA, INT, LONG, LPSTR, INT)
        GetKeyNameTextW = declare(user32.GetKeyNameTextW, INT, LONG, LPWSTR, INT)
        GetKeyNameText = unicode(GetKeyNameTextW, GetKeyNameTextA)

        # REGION ***

        # REGION *** Desktop Family ***

        GetKeyboardType = declare(user32.GetKeyboardType, INT, INT)
        ToAscii = declare(user32.ToAscii, INT, UINT, UINT, PBYTE, LPWORD, UINT)
        ToAsciiEx = declare(user32.ToAsciiEx, INT, UINT, UINT, PBYTE, LPWORD, UINT, HKL)
        ToUnicode = declare(user32.ToUnicode, INT, UINT, UINT, PBYTE, LPWSTR, INT, UINT)
        OemKeyScan = declare(user32.OemKeyScan, DWORD, WORD)
        VkKeyScanA = declare(user32.VkKeyScanA, SHORT, CHAR)
        VkKeyScanW = declare(user32.VkKeyScanW, SHORT, WCHAR)
        VkKeyScan = unicode(VkKeyScanW, VkKeyScanA)
        VkKeyScanExA = declare(user32.VkKeyScanExA, SHORT, CHAR, HKL)
        VkKeyScanExW = declare(user32.VkKeyScanExW, SHORT, WCHAR, HKL)
        VkKeyScanEx = unicode(VkKeyScanExW, VkKeyScanExA)
        # WINVER >= 0x0400
        KEYEVENTF_EXTENDEDKEY = 0x0001
        KEYEVENTF_KEYUP = 0x0002
        KEYEVENTF_UNICODE = 0x0004
        KEYEVENTF_SCANCODE = 0x0008
        keybd_event = declare(user32.keybd_event, VOID, BYTE, BYTE, DWORD, ULONG_PTR)

        # REGION ***
        MOUSEEVENTF_MOVE = 0x0001 # mouse move
        MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
        MOUSEEVENTF_LEFTUP = 0x0004 # left button up
        MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down
        MOUSEEVENTF_RIGHTUP = 0x0010 # right button up
        MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
        MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up
        MOUSEEVENTF_XDOWN = 0x0080 # x button down
        MOUSEEVENTF_XUP = 0x0100 # x button down
        MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled
        MOUSEEVENTF_HWHEEL = 0x01000 # hwheel button rolled
        MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000 # do not coalesce mouse moves
        MOUSEEVENTF_VIRTUALDESK = 0x4000 # map to entire virtual desktop
        MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move

        # REGION *** Desktop Family ***

        mouse_event = declare(user32.mouse_event, VOID, DWORD, DWORD, DWORD, DWORD, ULONG_PTR)

        class tagMOUSEINPUT(CStructure):
            _fields_ = [
                ("dx", LONG),
                ("dy", LONG),
                ("mouseData", DWORD),
                ("dwFlags", DWORD),
                ("time", DWORD),
                ("dwExtraInfo", ULONG_PTR)
            ]
        MOUSEINPUT = tagMOUSEINPUT
        PMOUSEINPUT = POINTER(MOUSEINPUT)
        LPMOUSEINPUT = PMOUSEINPUT

        class tagKEYBDINPUT(CStructure):
            _fields_ = [
                ("wVk", WORD),
                ("wScan", WORD),
                ("dwFlags", DWORD),
                ("time", DWORD),

                # 
                # * When dwFlags has KEYEVENTF_SYSTEMINJECTION specified this field may carry
                # * KEY_UNICODE_SEQUENCE_ITEM or KEY_UNICODE_SEQUENCE_END which are used by InputService
                # * to distinguish injected unicode sequences. Those flags are stored in low word.
                # * When dwFlags has KEYEVENTF_ATTRIBUTED_INPUT specified this field carries in its high word
                # * ID of attributes associated with injected input. This ID is assigned by InputService and
                # * recognized only by it.
                # * For all other usage scenarios please refer to official documentation.

                ("dwExtraInfo", ULONG_PTR)
            ]
        KEYBDINPUT = tagKEYBDINPUT
        PKEYBDINPUT = POINTER(KEYBDINPUT)

        # REGION *** Desktop Family ***

        class tagHARDWAREINPUT(CStructure):
            _fields_ = [
                ("uMsg", DWORD),
                ("wParamL", WORD),
                ("wParamH", WORD)
            ]
        HARDWAREINPUT = tagHARDWAREINPUT
        PHARDWAREINPUT = POINTER(HARDWAREINPUT)
        LPHARDWAREINPUT = PHARDWAREINPUT

        INPUT_MOUSE = 0
        INPUT_KEYBOARD = 1
        INPUT_HARDWARE = 2

        class _U_MKH(Union):
            _fields_ = [
                ("mi", MOUSEINPUT),
                ("ki", KEYBDINPUT),
                ("hi", HARDWAREINPUT)
            ]

        class tagINPUT(CStructure):
            _fields_ = [
                ("type", DWORD),
                ("u", _U_MKH)
            ]
        INPUT = tagINPUT
        PINPUT = POINTER(INPUT)
        LPINPUT = PINPUT

        SendInput = declare(user32.SendInput, UINT, UINT, LPINPUT, INT)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        # (_WIN32_WINNT > 0x0400)

        # REGION *** Desktop Family ***


        """
        * Touch Input defines and functions
        """


        """
        * Touch input handle
        """
        HTOUCHINPUT = HANDLE

        class tagTOUCHINPUT(CStructure):
            _fields_ = [
                ("x", LONG),
                ("y", LONG),
                ("hSource", HANDLE),
                ("dwID", DWORD),
                ("dwFlags", DWORD),
                ("dwMask", DWORD),
                ("dwTime", DWORD),
                ("dwExtraInfo", ULONG_PTR),
                ("cxContact", DWORD),
                ("cyContact", DWORD)
            ]
        TOUCHINPUT = tagTOUCHINPUT
        PTOUCHINPUT = POINTER(TOUCHINPUT)
        PCTOUCHINPUT = PTOUCHINPUT

        # REGION ***

        """
        * Conversion of touch input coordinates to pixels
        """

        TOUCH_COORD_TO_PIXEL = lambda l: ((l) // 100)

        """
        * Touch input flag values (TOUCHINPUT.dwFlags)
        """

        TOUCHEVENTF_MOVE = 0x0001
        TOUCHEVENTF_DOWN = 0x0002
        TOUCHEVENTF_UP = 0x0004
        TOUCHEVENTF_INRANGE = 0x0008
        TOUCHEVENTF_PRIMARY = 0x0010
        TOUCHEVENTF_NOCOALESCE = 0x0020
        TOUCHEVENTF_PEN = 0x0040
        TOUCHEVENTF_PALM = 0x0080

        """
        * Touch input mask values (TOUCHINPUT.dwMask)
        """

        TOUCHINPUTMASKF_TIMEFROMSYSTEM = 0x0001 # the dwTime field contains a system generated value
        TOUCHINPUTMASKF_EXTRAINFO = 0x0002 # the dwExtraInfo field is valid
        TOUCHINPUTMASKF_CONTACTAREA = 0x0004 # the cxContact and cyContact fields are valid

        # REGION *** Desktop Family ***

        GetTouchInputInfo = declare(user32.GetTouchInputInfo, BOOL, HTOUCHINPUT, UINT, PTOUCHINPUT, INT)
        CloseTouchInputHandle = declare(user32.CloseTouchInputHandle, BOOL, HTOUCHINPUT)

        # REGION ***

        """
        * RegisterTouchWindow flag values
        """

        TWF_FINETOUCH = (0x00000001)
        TWF_WANTPALM = (0x00000002)

        # REGION *** Desktop Family ***

        RegisterTouchWindow = declare(user32.RegisterTouchWindow, BOOL, HWND, ULONG)
        UnregisterTouchWindow = declare(user32.UnregisterTouchWindow, BOOL, HWND)
        IsTouchWindow = declare(user32.IsTouchWindow, BOOL, HWND, PULONG)

        # REGION ***

        # REGION *** Desktop Family ***

        cpreproc.define("POINTER_STRUCTURES")

        tagPOINTER_INPUT_TYPE = INT
        if True:
            PT_POINTER  = 1   # Generic pointer
            PT_TOUCH    = 2   # Touch
            PT_PEN      = 3   # Pen
            PT_MOUSE    = 4   # Mouse
            PT_TOUCHPAD = 5   # Touchpad

        POINTER_INPUT_TYPE = DWORD
        POINTER_FLAGS = UINT32

        # REGION ***
        POINTER_FLAG_NONE = 0x00000000 # Default
        POINTER_FLAG_NEW = 0x00000001 # New pointer
        POINTER_FLAG_INRANGE = 0x00000002 # Pointer has not departed
        POINTER_FLAG_INCONTACT = 0x00000004 # Pointer is in contact
        POINTER_FLAG_FIRSTBUTTON = 0x00000010 # Primary action
        POINTER_FLAG_SECONDBUTTON = 0x00000020 # Secondary action
        POINTER_FLAG_THIRDBUTTON = 0x00000040 # Third button
        POINTER_FLAG_FOURTHBUTTON = 0x00000080 # Fourth button
        POINTER_FLAG_FIFTHBUTTON = 0x00000100 # Fifth button
        POINTER_FLAG_PRIMARY = 0x00002000 # Pointer is primary
        POINTER_FLAG_CONFIDENCE = 0x00004000 # Pointer is considered unlikely to be accidental
        POINTER_FLAG_CANCELED = 0x00008000 # Pointer is departing in an abnormal manner
        POINTER_FLAG_DOWN = 0x00010000 # Pointer transitioned to down state (made contact)
        POINTER_FLAG_UPDATE = 0x00020000 # Pointer update
        POINTER_FLAG_UP = 0x00040000 # Pointer transitioned from down state (broke contact)
        POINTER_FLAG_WHEEL = 0x00080000 # Vertical wheel
        POINTER_FLAG_HWHEEL = 0x00100000 # Horizontal wheel
        POINTER_FLAG_CAPTURECHANGED = 0x00200000 # Lost capture
        POINTER_FLAG_HASTRANSFORM = 0x00400000 # Input has a transform associated with it

        """
        * Pointer info key states defintions.
        """

        POINTER_MOD_SHIFT = (0x0004) # Shift key is held down.
        POINTER_MOD_CTRL = (0x0008) # Ctrl key is held down.

        # REGION *** Desktop Family ***

        tagPOINTER_BUTTON_CHANGE_TYPE = INT
        if True:
            POINTER_CHANGE_NONE = 0
            POINTER_CHANGE_FIRSTBUTTON_DOWN = 1
            POINTER_CHANGE_FIRSTBUTTON_UP = 2
            POINTER_CHANGE_SECONDBUTTON_DOWN = 3
            POINTER_CHANGE_SECONDBUTTON_UP = 4
            POINTER_CHANGE_THIRDBUTTON_DOWN = 5
            POINTER_CHANGE_THIRDBUTTON_UP = 6
            POINTER_CHANGE_FOURTHBUTTON_DOWN = 7
            POINTER_CHANGE_FOURTHBUTTON_UP = 8
            POINTER_CHANGE_FIFTHBUTTON_DOWN = 9
            POINTER_CHANGE_FIFTHBUTTON_UP = 10
        POINTER_BUTTON_CHANGE_TYPE = tagPOINTER_BUTTON_CHANGE_TYPE

        class tagPOINTER_INFO(CStructure):
            _fields_ = [
                ("pointerType", POINTER_INPUT_TYPE),
                ("pointerId", UINT32),
                ("frameId", UINT32),
                ("pointerFlags", POINTER_FLAGS),
                ("sourceDevice", HANDLE),
                ("hwndTarget", HWND),
                ("ptPixelLocation", POINT),
                ("ptHimetricLocation", POINT),
                ("ptPixelLocationRaw", POINT),
                ("ptHimetricLocationRaw", POINT),
                ("dwTime", DWORD),
                ("historyCount", UINT32),
                ("inputData", INT32),
                ("dwKeyStates", DWORD),
                ("PerformanceCount", UINT64),
                ("ButtonChangeType", POINTER_BUTTON_CHANGE_TYPE)
            ]
        POINTER_INFO = tagPOINTER_INFO

        TOUCH_FLAGS = UINT32
        TOUCH_MASK = UINT32

        TOUCH_FLAG_NONE = 0x00000000 # Default

        TOUCH_MASK_NONE = 0x00000000 # Default - none of the optional fields are valid
        TOUCH_MASK_CONTACTAREA = 0x00000001 # The rcContact field is valid
        TOUCH_MASK_ORIENTATION = 0x00000002 # The orientation field is valid
        TOUCH_MASK_PRESSURE = 0x00000004 # The pressure field is valid

        class tagPOINTER_TOUCH_INFO(CStructure):
            _fields_ = [
                ("pointerInfo", POINTER_INFO),
                ("touchFlags", TOUCH_FLAGS),
                ("touchMask", TOUCH_MASK),
                ("rcContact", RECT),
                ("rcContactRaw", RECT),
                ("orientation", UINT32),
                ("pressure", UINT32)
            ]
        POINTER_TOUCH_INFO = tagPOINTER_TOUCH_INFO

        PEN_FLAGS = UINT32
        PEN_MASK = UINT32

        PEN_FLAG_NONE = 0x00000000 # Default
        PEN_FLAG_BARREL = 0x00000001 # The barrel button is pressed
        PEN_FLAG_INVERTED = 0x00000002 # The pen is inverted
        PEN_FLAG_ERASER = 0x00000004 # The eraser button is pressed
        PEN_MASK_NONE = 0x00000000 # Default - none of the optional fields are valid
        PEN_MASK_PRESSURE = 0x00000001 # The pressure field is valid
        PEN_MASK_ROTATION = 0x00000002 # The rotation field is valid
        PEN_MASK_TILT_X = 0x00000004 # The tiltX field is valid
        PEN_MASK_TILT_Y = 0x00000008 # The tiltY field is valid

        class tagPOINTER_PEN_INFO(CStructure):
            _fields_ = [
                ("pointerInfo", POINTER_INFO),
                ("penFlags", PEN_FLAGS),
                ("penMask", PEN_MASK),
                ("pressure", UINT32),
                ("rotation", UINT32),
                ("tiltX", INT32),
                ("tiltY", INT32)
            ]
        POINTER_PEN_INFO = tagPOINTER_PEN_INFO
        
        # REGION ***

        """
        * Flags that appear in pointer input message parameters
        """

        POINTER_MESSAGE_FLAG_NEW = 0x00000001 # New pointer
        POINTER_MESSAGE_FLAG_INRANGE = 0x00000002 # Pointer has not departed
        POINTER_MESSAGE_FLAG_INCONTACT = 0x00000004 # Pointer is in contact
        POINTER_MESSAGE_FLAG_FIRSTBUTTON = 0x00000010 # Primary action
        POINTER_MESSAGE_FLAG_SECONDBUTTON = 0x00000020 # Secondary action
        POINTER_MESSAGE_FLAG_THIRDBUTTON = 0x00000040 # Third button
        POINTER_MESSAGE_FLAG_FOURTHBUTTON = 0x00000080 # Fourth button
        POINTER_MESSAGE_FLAG_FIFTHBUTTON = 0x00000100 # Fifth button
        POINTER_MESSAGE_FLAG_PRIMARY = 0x00002000 # Pointer is primary
        POINTER_MESSAGE_FLAG_CONFIDENCE = 0x00004000 # Pointer is considered unlikely to be accidental
        POINTER_MESSAGE_FLAG_CANCELED = 0x00008000 # Pointer is departing in an abnormal manner

        """
        * Macros to retrieve information from pointer input message parameters
        """

        GET_POINTERID_WPARAM = lambda wParam: (LOWORD(wParam))
        IS_POINTER_FLAG_SET_WPARAM = lambda wParam, flag: (DWORD(HIWORD(wParam) & (flag)).value == (flag))
        IS_POINTER_NEW_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_NEW)
        IS_POINTER_INRANGE_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_INRANGE)
        IS_POINTER_INCONTACT_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_INCONTACT)
        IS_POINTER_FIRSTBUTTON_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_FIRSTBUTTON)
        IS_POINTER_SECONDBUTTON_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_SECONDBUTTON)
        IS_POINTER_THIRDBUTTON_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_THIRDBUTTON)
        IS_POINTER_FOURTHBUTTON_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_FOURTHBUTTON)
        IS_POINTER_FIFTHBUTTON_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_FIFTHBUTTON)
        IS_POINTER_PRIMARY_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_PRIMARY)
        HAS_POINTER_CONFIDENCE_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_CONFIDENCE)
        IS_POINTER_CANCELED_WPARAM = lambda wParam: IS_POINTER_FLAG_SET_WPARAM(wParam, POINTER_MESSAGE_FLAG_CANCELED)

        """
        * WM_POINTERACTIVATE return codes
        """

        PA_ACTIVATE = MA_ACTIVATE
        PA_NOACTIVATE = MA_NOACTIVATE
        MAX_TOUCH_COUNT = 256
        TOUCH_FEEDBACK_DEFAULT = 0x1
        TOUCH_FEEDBACK_INDIRECT = 0x2
        TOUCH_FEEDBACK_NONE = 0x3

        class POINTER_FEEDBACK_MODE(CStructure):
            POINTER_FEEDBACK_DEFAULT = 1   # The injected pointer input feedback may get suppressed by the end-user settings in the Pen and Touch control panel.
            POINTER_FEEDBACK_INDIRECT = 2  # The injected pointer input feedback overrides the end-user settings in the Pen and Touch control panel.
            POINTER_FEEDBACK_NONE = 3      # No touch visualizations.

        # REGION *** Desktop Family ***

        InitializeTouchInjection = declare(user32.InitializeTouchInjection, BOOL, UINT32, DWORD)
        InjectTouchInput = declare(user32.InjectTouchInput, BOOL, POINTER(POINTER_TOUCH_INFO))

        class tagUSAGE_PROPERTIES(CStructure):
            _fields_ = [
                ("level", USHORT),
                ("page", USHORT),
                ("usage", USHORT),
                ("logicalMinimum", INT32),
                ("logicalMaximum", INT32),
                ("uint", USHORT),
                ("exponent", USHORT),
                ("count", BYTE),
                ("physicalMinimum", INT32),
                ("physicalMaximum", INT32)
            ]
        USAGE_PROPERTIES = tagUSAGE_PROPERTIES
        PUSAGE_PROPERTIES = POINTER(USAGE_PROPERTIES)

        class _U_TP(CStructure):
            _fields_ = [
                ("touchInfo", POINTER_TOUCH_INFO),
                ("penInfo", POINTER_PEN_INFO)
            ]

        class tagPOINTER_TYPE_INFO(CStructure):
            _fields_ = [
                ("type", POINTER_INPUT_TYPE),
                ("u", _U_TP)
            ]
        POINTER_TYPE_INFO = tagPOINTER_TYPE_INFO
        PPOINTER_TYPE_INFO = POINTER(POINTER_TYPE_INFO)

        class tagINPUT_INJECTION_VALUE(CStructure):
            _fields_ = [
                ("page", USHORT),
                ("usage", USHORT),
                ("value", INT32),
                ("index", USHORT)
            ]
        INPUT_INJECTION_VALUE = tagINPUT_INJECTION_VALUE
        PINPUT_INJECTION_VALUE = POINTER(INPUT_INJECTION_VALUE)

        # REGION ***

        # REGION *** Desktop Family ***

        GetPointerType = declare(user32.GetPointerType, BOOL, UINT32, POINTER(POINTER_INPUT_TYPE))

        GetPointerCursorId = declare(user32.GetPointerCursorId, BOOL, UINT32, PUINT32)
        
        GetPointerInfo = declare(user32.GetPointerInfo, BOOL, UINT32, POINTER(POINTER_INFO))

        GetPointerInfoHistory = declare(user32.GetPointerInfoHistory, BOOL, UINT32, PUINT32, POINTER(POINTER_INFO))

        GetPointerFrameInfo = declare(user32.GetPointerFrameInfo, BOOL, UINT32, PUINT32, POINTER(POINTER_INFO))

        GetPointerFrameInfoHistory = declare(user32.GetPointerFrameInfoHistory, BOOL, UINT32, PUINT32, PUINT32, POINTER(POINTER_INFO))

        GetPointerTouchInfo = declare(user32.GetPointerTouchInfo, BOOL, UINT32, POINTER(POINTER_TOUCH_INFO))

        GetPointerTouchInfoHistory = declare(user32.GetPointerTouchInfoHistory, BOOL, UINT32, PUINT32, POINTER(POINTER_TOUCH_INFO))

        GetPointerFrameTouchInfo = declare(user32.GetPointerFrameTouchInfo, BOOL, UINT32, PUINT32, POINTER(POINTER_TOUCH_INFO))

        GetPointerFrameTouchInfoHistory = declare(user32.GetPointerFrameTouchInfoHistory, BOOL, UINT32, PUINT32, PUINT32, POINTER(POINTER_TOUCH_INFO))

        GetPointerPenInfo = declare(user32.GetPointerPenInfo, BOOL, UINT32, POINTER(POINTER_PEN_INFO))

        GetPointerPenInfoHistory = declare(user32.GetPointerPenInfoHistory, BOOL, UINT32, PUINT32, POINTER(POINTER_PEN_INFO))

        GetPointerFramePenInfo = declare(user32.GetPointerFramePenInfo, BOOL, UINT32, PUINT32, POINTER(POINTER_PEN_INFO))

        GetPointerFramePenInfoHistory = declare(user32.GetPointerFramePenInfoHistory, BOOL, UINT32, PUINT32, PUINT32, POINTER(POINTER_PEN_INFO))

        SkipPointerFrameMessages = declare(user32.SkipPointerFrameMessages, BOOL, UINT32)

        RegisterPointerInputTarget = declare(user32.RegisterPointerInputTarget, BOOL, HWND, POINTER_INPUT_TYPE)

        UnregisterPointerInputTarget = declare(user32.UnregisterPointerInputTarget, BOOL, HWND, POINTER_INPUT_TYPE)

        RegisterPointerInputTargetEx = declare(user32.RegisterPointerInputTargetEx, BOOL, HWND, POINTER_INPUT_TYPE, BOOL)

        UnregisterPointerInputTargetEx = declare(user32.UnregisterPointerInputTargetEx, BOOL, HWND, POINTER_INPUT_TYPE)

        HSYNTHETICPOINTERDEVICE = HANDLE

        CreateSyntheticPointerDevice = declare(user32.CreateSyntheticPointerDevice, HSYNTHETICPOINTERDEVICE, POINTER_INPUT_TYPE, ULONG, POINTER_FEEDBACK_MODE)

        InjectSyntheticPointerInput = declare(user32.InjectSyntheticPointerInput, BOOL, HSYNTHETICPOINTERDEVICE, PPOINTER_TYPE_INFO, UINT32)

        DestroySyntheticPointerDevice = declare(user32.DestroySyntheticPointerDevice, VOID, HSYNTHETICPOINTERDEVICE)

        # NTDDI_VERSION >= NTDDI_WIN10_RS5
        EnableMouseInPointer = declare(user32.EnableMouseInPointer, BOOL, BOOL)

        IsMouseInPointerEnabled = declare(user32.IsMouseInPointerEnabled, BOOL, VOID)

        #EnableMouseInPointerForThread = declare(user32.EnableMouseInPointerForThread, BOOL, VOID)

        TOUCH_HIT_TESTING_DEFAULT = 0x0
        TOUCH_HIT_TESTING_CLIENT = 0x1
        TOUCH_HIT_TESTING_NONE = 0x2

        RegisterTouchHitTestingWindow = declare(user32.RegisterTouchHitTestingWindow, BOOL, HWND, ULONG)

        class tagTOUCH_HIT_TESTING_PROXIMITY_EVALUATION(CStructure):
            _fields_ = [
                ("score", UINT16),
                ("adjustedPoint", POINT)
            ]
        TOUCH_HIT_TESTING_PROXIMITY_EVALUATION = tagTOUCH_HIT_TESTING_PROXIMITY_EVALUATION
        PTOUCH_HIT_TESTING_PROXIMITY_EVALUATION = POINTER(TOUCH_HIT_TESTING_PROXIMITY_EVALUATION)

        """
        * WM_TOUCHHITTESTING structure
        """

        class tagTOUCH_HIT_TESTING_INPUT(CStructure):
            _fields_ = [
                ("pointerId", UINT32),
                ("point", POINT),
                ("boundingBox", RECT),
                ("nonOccludedBoundingBox", RECT),
                ("orientation", UINT32)
            ]
        TOUCH_HIT_TESTING_INPUT = tagTOUCH_HIT_TESTING_INPUT
        PTOUCH_HIT_TESTING_INPUT = POINTER(TOUCH_HIT_TESTING_INPUT)


        TOUCH_HIT_TESTING_PROXIMITY_CLOSEST = 0x0
        TOUCH_HIT_TESTING_PROXIMITY_FARTHEST = 0xFFF

        EvaluateProximityToRect = declare(user32.EvaluateProximityToRect, BOOL, PRECT, PTOUCH_HIT_TESTING_INPUT, PTOUCH_HIT_TESTING_PROXIMITY_EVALUATION)
        EvaluateProximityToPolygon = declare(user32.EvaluateProximityToPolygon, BOOL, UINT32, PPOINT, PTOUCH_HIT_TESTING_INPUT, PTOUCH_HIT_TESTING_PROXIMITY_EVALUATION)
        PackTouchHitTestingProximityEvaluation = declare(user32.PackTouchHitTestingProximityEvaluation, LRESULT, PTOUCH_HIT_TESTING_INPUT, PTOUCH_HIT_TESTING_PROXIMITY_EVALUATION)

        tagFEEDBACK_TYPE = INT
        if True:
            FEEDBACK_TOUCH_CONTACTVISUALIZATION = 1
            FEEDBACK_PEN_BARRELVISUALIZATION    = 2
            FEEDBACK_PEN_TAP                    = 3
            FEEDBACK_PEN_DOUBLETAP              = 4
            FEEDBACK_PEN_PRESSANDHOLD           = 5
            FEEDBACK_PEN_RIGHTTAP               = 6
            FEEDBACK_TOUCH_TAP                  = 7
            FEEDBACK_TOUCH_DOUBLETAP            = 8
            FEEDBACK_TOUCH_PRESSANDHOLD         = 9
            FEEDBACK_TOUCH_RIGHTTAP             = 10
            FEEDBACK_GESTURE_PRESSANDTAP        = 11
            FEEDBACK_MAX                        = 0xFFFFFFFF
        FEEDBACK_TYPE = tagFEEDBACK_TYPE

        GWFS_INCLUDE_ANCESTORS = 0x00000001

        GetWindowFeedbackSetting = declare(user32.GetWindowFeedbackSetting, BOOL, HWND, FEEDBACK_TYPE, DWORD, PUINT32, PVOID)
        SetWindowFeedbackSetting = declare(user32.SetWindowFeedbackSetting, BOOL, HWND, FEEDBACK_TYPE, DWORD, UINT32, PVOID)

        # REGION ***

        # REGION *** Desktop Family ***

        class _S_TRNSFM(CStructure):
            _fields_ = [
                ("_11", FLOAT), ("_12", FLOAT), ("_13", FLOAT), ("_14", FLOAT),
                ("_21", FLOAT), ("_22", FLOAT), ("_23", FLOAT), ("_24", FLOAT),
                ("_31", FLOAT), ("_32", FLOAT), ("_33", FLOAT), ("_34", FLOAT),
                ("_41", FLOAT), ("_42", FLOAT), ("_43", FLOAT), ("_44", FLOAT)
            ]
        
        class _U_TRNSFM(CStructure):
            _fields_ = [
                ("s", _S_TRNSFM),
                ("m", FLOAT * 4 * 4)
            ]

        class tagINPUT_TRANSFORM(CStructure):
            _fields_ = [
                ("u", _U_TRNSFM)
            ]
        INPUT_TRANSFORM = tagINPUT_TRANSFORM
        GetPointerInputTransform = declare(user32.GetPointerInputTransform, BOOL, UINT32, UINT32, POINTER(INPUT_TRANSFORM))

        # REGION ***

        # REGION *** Desktop Family ***

        class tagLASTINPUTINFO(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("dwTime", DWORD)
            ]
        LASTINPUTINFO = tagLASTINPUTINFO
        PLASTINPUTINFO = POINTER(LASTINPUTINFO)

        GetLastInputInfo = declare(user32.GetLastInputInfo, BOOL, PLASTINPUTINFO)
        # _WIN32_WINNT >= 0x0500
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP)

        # REGION ***

        # REGION *** Desktop or PC Family ***

        MapVirtualKeyA = declare(user32.MapVirtualKeyA, UINT, UINT, UINT)
        MapVirtualKeyW = declare(user32.MapVirtualKeyW, UINT, UINT, UINT)
        MapVirtualKey = unicode(MapVirtualKeyW, MapVirtualKeyA)
        MapVirtualKeyExA = declare(user32.MapVirtualKeyExA, UINT, UINT, UINT, HKL)
        MapVirtualKeyExW = declare(user32.MapVirtualKeyExW, UINT, UINT, UINT, HKL)
        MapVirtualKeyEx = unicode(MapVirtualKeyExW, MapVirtualKeyExA)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_PC_APP)

        # REGION ***

        # REGION *** Desktop Family ***

        MAPVK_VK_TO_VSC = (0)
        MAPVK_VSC_TO_VK = (1)
        MAPVK_VK_TO_CHAR = (2)
        MAPVK_VSC_TO_VK_EX = (3)
        MAPVK_VK_TO_VSC_EX = (4)
        GetInputState = declare(user32.GetInputState, BOOL, VOID)
        GetQueueStatus = declare(user32.GetQueueStatus, DWORD, UINT)
        GetCapture = declare(user32.GetCapture, HWND, VOID)
        SetCapture = declare(user32.SetCapture, HWND, HWND)
        ReleaseCapture = declare(user32.ReleaseCapture, BOOL, VOID)
        MsgWaitForMultipleObjects = declare(user32.MsgWaitForMultipleObjects, DWORD, DWORD, PHANDLE, BOOL, DWORD, DWORD)
        MsgWaitForMultipleObjectsEx = declare(user32.MsgWaitForMultipleObjectsEx, DWORD, DWORD, PHANDLE, DWORD, DWORD, DWORD)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        MWMO_WAITALL = 0x0001
        MWMO_ALERTABLE = 0x0002
        MWMO_INPUTAVAILABLE = 0x0004

        # REGION *** Desktop Family or Games Family ***

        USER_TIMER_MAXIMUM = 0x7FFFFFFF
        USER_TIMER_MINIMUM = 0x0000000A

        """
        * Windows Functions
        """

        SetTimer = declare(user32.SetTimer, UINT_PTR, HWND, UINT_PTR, UINT, TIMERPROC)
        TIMERV_DEFAULT_COALESCING = (0)
        TIMERV_NO_COALESCING = (0xFFFFFFFF)
        TIMERV_COALESCING_MIN = (1)
        TIMERV_COALESCING_MAX = (0x7FFFFFF5)

        # REGION ***

        # REGION *** Desktop Family ***

        SetCoalescableTimer = declare(user32.SetCoalescableTimer, UINT_PTR, HWND, UINT_PTR, UINT, TIMERPROC, ULONG)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        KillTimer = declare(user32.KillTimer, BOOL, HWND, UINT_PTR)

        # REGION ***

        # REGION *** Desktop Family ***

        IsWindowUnicode = declare(user32.IsWindowUnicode, BOOL, HWND)
        EnableWindow = declare(user32.EnableWindow, BOOL, HWND, BOOL)
        IsWindowEnabled = declare(user32.IsWindowEnabled, BOOL, HWND)
        LoadAcceleratorsA = declare(user32.LoadAcceleratorsA, HACCEL, HINSTANCE, LPCSTR)
        LoadAcceleratorsW = declare(user32.LoadAcceleratorsW, HACCEL, HINSTANCE, LPCWSTR)
        LoadAccelerators = unicode(LoadAcceleratorsW, LoadAcceleratorsA)
        CreateAcceleratorTableA = declare(user32.CreateAcceleratorTableA, HACCEL, LPACCEL, INT)
        CreateAcceleratorTableW = declare(user32.CreateAcceleratorTableW, HACCEL, LPACCEL, INT)
        CreateAcceleratorTable = unicode(CreateAcceleratorTableW, CreateAcceleratorTableA)

        DestroyAcceleratorTable = declare(user32.DestroyAcceleratorTable, BOOL, HACCEL)
        CopyAcceleratorTableA = declare(user32.CopyAcceleratorTableA, INT, HACCEL, LPACCEL, INT)
        CopyAcceleratorTableW = declare(user32.CopyAcceleratorTableW, INT, HACCEL, LPACCEL, INT)
        CopyAcceleratorTable = unicode(CopyAcceleratorTableW, CopyAcceleratorTableA)

        if cpreproc.ifndef("NOMSG"):
            TranslateAcceleratorA = declare(user32.TranslateAcceleratorA, INT, HWND, HACCEL, LPMSG)
            TranslateAcceleratorW = declare(user32.TranslateAcceleratorW, INT, HWND, HACCEL, LPMSG)
            TranslateAccelerator = unicode(TranslateAcceleratorW, TranslateAcceleratorA)

        # !NOMSG
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        if cpreproc.ifndef("NOSYSMETRICS"):

            """
            * GetSystemMetrics() codes
            """

            SM_CXSCREEN = 0
            SM_CYSCREEN = 1
            SM_CXVSCROLL = 2
            SM_CYHSCROLL = 3
            SM_CYCAPTION = 4
            SM_CXBORDER = 5
            SM_CYBORDER = 6
            SM_CXDLGFRAME = 7
            SM_CYDLGFRAME = 8
            SM_CYVTHUMB = 9
            SM_CXHTHUMB = 10
            SM_CXICON = 11
            SM_CYICON = 12
            SM_CXCURSOR = 13
            SM_CYCURSOR = 14
            SM_CYMENU = 15
            SM_CXFULLSCREEN = 16
            SM_CYFULLSCREEN = 17
            SM_CYKANJIWINDOW = 18
            SM_MOUSEPRESENT = 19
            SM_CYVSCROLL = 20
            SM_CXHSCROLL = 21
            SM_DEBUG = 22
            SM_SWAPBUTTON = 23
            SM_RESERVED1 = 24
            SM_RESERVED2 = 25
            SM_RESERVED3 = 26
            SM_RESERVED4 = 27
            SM_CXMIN = 28
            SM_CYMIN = 29
            SM_CXSIZE = 30
            SM_CYSIZE = 31
            SM_CXFRAME = 32
            SM_CYFRAME = 33
            SM_CXMINTRACK = 34
            SM_CYMINTRACK = 35
            SM_CXDOUBLECLK = 36
            SM_CYDOUBLECLK = 37
            SM_CXICONSPACING = 38
            SM_CYICONSPACING = 39
            SM_MENUDROPALIGNMENT = 40
            SM_PENWINDOWS = 41
            SM_DBCSENABLED = 42
            SM_CMOUSEBUTTONS = 43
            SM_CXFIXEDFRAME = SM_CXDLGFRAME # ;win40 name change
            SM_CYFIXEDFRAME = SM_CYDLGFRAME # ;win40 name change
            SM_CXSIZEFRAME = SM_CXFRAME # ;win40 name change
            SM_CYSIZEFRAME = SM_CYFRAME # ;win40 name change
            SM_SECURE = 44
            SM_CXEDGE = 45
            SM_CYEDGE = 46
            SM_CXMINSPACING = 47
            SM_CYMINSPACING = 48
            SM_CXSMICON = 49
            SM_CYSMICON = 50
            SM_CYSMCAPTION = 51
            SM_CXSMSIZE = 52
            SM_CYSMSIZE = 53
            SM_CXMENUSIZE = 54
            SM_CYMENUSIZE = 55
            SM_ARRANGE = 56
            SM_CXMINIMIZED = 57
            SM_CYMINIMIZED = 58
            SM_CXMAXTRACK = 59
            SM_CYMAXTRACK = 60
            SM_CXMAXIMIZED = 61
            SM_CYMAXIMIZED = 62
            SM_NETWORK = 63
            SM_CLEANBOOT = 67
            SM_CXDRAG = 68
            SM_CYDRAG = 69
            SM_SHOWSOUNDS = 70
            SM_CXMENUCHECK = 71 # Use instead of GetMenuCheckMarkDimensions()!
            SM_CYMENUCHECK = 72
            SM_SLOWMACHINE = 73
            SM_MIDEASTENABLED = 74
            SM_MOUSEWHEELPRESENT = 75
            SM_XVIRTUALSCREEN = 76
            SM_YVIRTUALSCREEN = 77
            SM_CXVIRTUALSCREEN = 78
            SM_CYVIRTUALSCREEN = 79
            SM_CMONITORS = 80
            SM_SAMEDISPLAYFORMAT = 81
            SM_IMMENABLED = 82
            SM_CXFOCUSBORDER = 83
            SM_CYFOCUSBORDER = 84
            SM_TABLETPC = 86
            SM_MEDIACENTER = 87
            SM_STARTER = 88
            SM_SERVERR2 = 89
            SM_MOUSEHORIZONTALWHEELPRESENT = 91
            SM_CXPADDEDBORDER = 92
            SM_DIGITIZER = 94
            SM_MAXIMUMTOUCHES = 95
            SM_CMETRICS = 76
            SM_CMETRICS = 83
            SM_CMETRICS = 91
            SM_CMETRICS = 93
            SM_CMETRICS = 97
            SM_REMOTESESSION = 0x1000
            SM_SHUTTINGDOWN = 0x2000
            SM_REMOTECONTROL = 0x2001
            SM_CARETBLINKINGENABLED = 0x2002
            SM_CONVERTIBLESLATEMODE = 0x2003
            SM_SYSTEMDOCKED = 0x2004

            # REGION *** Desktop Family ***

            GetSystemMetrics = declare(user32.GetSystemMetrics, INT, INT)
            GetSystemMetricsForDpi = declare(user32.GetSystemMetricsForDpi, INT, INT, UINT)

                # REGION ***
        # !NOSYSMETRICS

        # REGION *** Desktop Family ***

        if cpreproc.ifndef("NOMENUS"):
            LoadMenuA = declare(user32.LoadMenuA, HMENU, HINSTANCE, LPCSTR)
            LoadMenuW = declare(user32.LoadMenuW, HMENU, HINSTANCE, LPCWSTR)
            LoadMenu = unicode(LoadMenuW, LoadMenuA)
            LoadMenuIndirectA = declare(user32.LoadMenuIndirectA, HMENU, POINTER(MENUTEMPLATEA))
            LoadMenuIndirectW = declare(user32.LoadMenuIndirectW, HMENU, POINTER(MENUTEMPLATEW))
            LoadMenuIndirect = unicode(LoadMenuIndirectW, LoadMenuIndirectA)

            GetMenu = declare(user32.GetMenu, HMENU, HWND)
            SetMenu = declare(user32.SetMenu, BOOL, HWND, HMENU)
            ChangeMenuA = declare(user32.ChangeMenuA, BOOL, HMENU, UINT, LPCSTR, UINT, UINT)
            ChangeMenuW = declare(user32.ChangeMenuW, BOOL, HMENU, UINT, LPCWSTR, UINT, UINT)
            ChangeMenu = unicode(ChangeMenuW, ChangeMenuA)

            HiliteMenuItem = declare(user32.HiliteMenuItem, BOOL, HWND, HMENU, UINT, UINT)
            GetMenuStringA = declare(user32.GetMenuStringA, INT, HMENU, UINT, LPSTR, INT, UINT)
            GetMenuStringW = declare(user32.GetMenuStringW, INT, HMENU, UINT, LPWSTR, INT, UINT)
            GetMenuString = unicode(GetMenuStringW, GetMenuStringA)

            GetMenuState = declare(user32.GetMenuState, UINT, HMENU, UINT, UINT)
            DrawMenuBar = declare(user32.DrawMenuBar, BOOL, HWND)
            PMB_ACTIVE = 0x00000001
            GetSystemMenu = declare(user32.GetSystemMenu, HMENU, HWND, BOOL)
            CreateMenu = declare(user32.CreateMenu, HMENU, VOID)
            CreatePopupMenu = declare(user32.CreatePopupMenu, HMENU, VOID)
            DestroyMenu = declare(user32.DestroyMenu, BOOL, HMENU)
            CheckMenuItem = declare(user32.CheckMenuItem, DWORD, HMENU, UINT, UINT)
            EnableMenuItem = declare(user32.EnableMenuItem, BOOL, HMENU, UINT, UINT)
            GetSubMenu = declare(user32.GetSubMenu, HMENU, HMENU, INT)
            GetMenuItemID = declare(user32.GetMenuItemID, UINT, HMENU, INT)
            GetMenuItemCount = declare(user32.GetMenuItemCount, INT, HMENU)
            InsertMenuA = declare(user32.InsertMenuA, BOOL, HMENU, UINT, UINT, UINT_PTR, LPCSTR)
            InsertMenuW = declare(user32.InsertMenuW, BOOL, HMENU, UINT, UINT, UINT_PTR, LPCWSTR)
            InsertMenu = unicode(InsertMenuW, InsertMenuA)

            AppendMenuA = declare(user32.AppendMenuA, BOOL, HMENU, UINT, UINT_PTR, LPCSTR)
            AppendMenuW = declare(user32.AppendMenuW, BOOL, HMENU, UINT, UINT_PTR, LPCWSTR)
            AppendMenu = unicode(AppendMenuW, AppendMenuA)

            ModifyMenuA = declare(user32.ModifyMenuA, BOOL, HMENU, UINT, UINT, UINT_PTR, LPCSTR)
            ModifyMenuW = declare(user32.ModifyMenuW, BOOL, HMENU, UINT, UINT, UINT_PTR, LPCWSTR)
            ModifyMenu = unicode(ModifyMenuW, ModifyMenuA)

            DeleteMenu = declare(user32.DeleteMenu, BOOL, HMENU, UINT, UINT)
            SetMenuItemBitmaps = declare(user32.SetMenuItemBitmaps, BOOL, HMENU, UINT, UINT, HBITMAP, HBITMAP)
            GetMenuCheckMarkDimensions = declare(user32.GetMenuCheckMarkDimensions, LONG, VOID)
            TrackPopupMenu = declare(user32.TrackPopupMenu, BOOL, HMENU, UINT, INT, INT, INT, HWND, PRECT)
            MNC_IGNORE = 0
            MNC_CLOSE = 1
            MNC_EXECUTE = 2
            MNC_SELECT = 3

            class tagTPMPARAMS(CStructure):
                _fields_ = [
                    ("cbSize", UINT), # Size of structure
                    ("rcExclude", RECT) # Screen coordinates of rectangle to exclude when positioning
                ]
            TPMPARAMS = tagTPMPARAMS
            LPTPMPARAMS = POINTER(TPMPARAMS)

            TrackPopupMenuEx = declare(user32.TrackPopupMenuEx, BOOL, HMENU, UINT, INT, INT, HWND, LPTPMPARAMS)
            CalculatePopupWindowPosition = declare(user32.CalculatePopupWindowPosition, BOOL, PPOINT, PSIZE, UINT, PRECT, PRECT)
            MNS_NOCHECK = 0x80000000
            MNS_MODELESS = 0x40000000
            MNS_DRAGDROP = 0x20000000
            MNS_AUTODISMISS = 0x10000000
            MNS_NOTIFYBYPOS = 0x08000000
            MNS_CHECKORBMP = 0x04000000
            MIM_MAXHEIGHT = 0x00000001
            MIM_BACKGROUND = 0x00000002
            MIM_HELPID = 0x00000004
            MIM_MENUDATA = 0x00000008
            MIM_STYLE = 0x00000010
            MIM_APPLYTOSUBMENUS = 0x80000000

            class tagMENUINFO(CStructure):
                _fields_ = [
                    ("cbSize", DWORD),
                    ("fMask", DWORD),
                    ("dwStyle", DWORD),
                    ("cyMax", UINT),
                    ("hbrBack", HBRUSH),
                    ("dwContextHelpID", DWORD),
                    ("dwMenuData", ULONG_PTR)
                ]
            MENUINFO = tagMENUINFO
            LPMENUINFO = POINTER(MENUINFO)
            LPCMENUINFO = LPMENUINFO

            GetMenuInfo = declare(user32.GetMenuInfo, BOOL, HMENU, LPMENUINFO)
            SetMenuInfo = declare(user32.SetMenuInfo, BOOL, HMENU, LPCMENUINFO)
            EndMenu = declare(user32.EndMenu, BOOL, VOID)

            """
            * WM_MENUDRAG return values.
            """

            MND_CONTINUE = 0
            MND_ENDMENU = 1

            class tagMENUGETOBJECTINFO(CStructure):
                _fields_ = [
                    ("dwFlags", DWORD),
                    ("uPos", UINT),
                    ("hmenu", HMENU),
                    ("riid", PVOID),
                    ("pvObj", PVOID)
                ]
            MENUGETOBJECTINFO = tagMENUGETOBJECTINFO
            PMENUGETOBJECTINFO = POINTER(MENUGETOBJECTINFO)

            """
            * MENUGETOBJECTINFO dwFlags values
            """

            MNGOF_TOPGAP = 0x00000001
            MNGOF_BOTTOMGAP = 0x00000002

            """
            * WM_MENUGETOBJECT return values
            """

            MNGO_NOINTERFACE = 0x00000000
            MNGO_NOERROR = 0x00000001
            # WINVER >= 0x0500
            MIIM_STATE = 0x00000001
            MIIM_ID = 0x00000002
            MIIM_SUBMENU = 0x00000004
            MIIM_CHECKMARKS = 0x00000008
            MIIM_TYPE = 0x00000010
            MIIM_DATA = 0x00000020
            MIIM_STRING = 0x00000040
            MIIM_BITMAP = 0x00000080
            MIIM_FTYPE = 0x00000100
            HBMMENU_CALLBACK = HBITMAP(-1)
            HBMMENU_SYSTEM = HBITMAP(1)
            HBMMENU_MBAR_RESTORE = HBITMAP(2)
            HBMMENU_MBAR_MINIMIZE = HBITMAP(3)
            HBMMENU_MBAR_CLOSE = HBITMAP(5)
            HBMMENU_MBAR_CLOSE_D = HBITMAP(6)
            HBMMENU_MBAR_MINIMIZE_D = HBITMAP(7)
            HBMMENU_POPUP_CLOSE = HBITMAP(8)
            HBMMENU_POPUP_RESTORE = HBITMAP(9)
            HBMMENU_POPUP_MAXIMIZE = HBITMAP(10)
            HBMMENU_POPUP_MINIMIZE = HBITMAP(11)

            class tagMENUITEMINFOA(CStructure):
                _fields_ = [
                    ("cbSize", UINT),
                    ("fMask", UINT),
                    ("fType", UINT), # used if MIIM_TYPE (4.0) or MIIM_FTYPE (>4.0)
                    ("fState", UINT), # used if MIIM_STATE
                    ("wID", UINT), # used if MIIM_ID
                    ("hSubMenu", HMENU), # used if MIIM_SUBMENU
                    ("hbmpChecked", HBITMAP), # used if MIIM_CHECKMARKS
                    ("hbmpUnchecked", HBITMAP), # used if MIIM_CHECKMARKS
                    ("dwItemData", ULONG_PTR), # used if MIIM_DATA
                    ("dwTypeData", LPSTR), # used if MIIM_TYPE (4.0) or MIIM_STRING (>4.0)
                    ("cch", UINT), # used if MIIM_TYPE (4.0) or MIIM_STRING (>4.0)
                    ("hbmpItem", HBITMAP), # used if MIIM_BITMAP
                ]
            MENUITEMINFOA = tagMENUITEMINFOA
            LPMENUITEMINFOA = POINTER(MENUITEMINFOA)

            class tagMENUITEMINFOW(CStructure):
                _fields_ = [
                    ("cbSize", UINT),
                    ("fMask", UINT),
                    ("fType", UINT), # used if MIIM_TYPE (4.0) or MIIM_FTYPE (>4.0)
                    ("fState", UINT), # used if MIIM_STATE
                    ("wID", UINT), # used if MIIM_ID
                    ("hSubMenu", HMENU), # used if MIIM_SUBMENU
                    ("hbmpChecked", HBITMAP), # used if MIIM_CHECKMARKS
                    ("hbmpUnchecked", HBITMAP), # used if MIIM_CHECKMARKS
                    ("dwItemData", ULONG_PTR), # used if MIIM_DATA
                    ("dwTypeData", LPWSTR), # used if MIIM_TYPE (4.0) or MIIM_STRING (>4.0)
                    ("cch", UINT), # used if MIIM_TYPE (4.0) or MIIM_STRING (>4.0)
                    ("hbmpItem", HBITMAP), # used if MIIM_BITMAP
                ]
            MENUITEMINFOW = tagMENUITEMINFOW
            LPMENUITEMINFOW = POINTER(MENUITEMINFOW)

            MENUITEMINFO = unicode(MENUITEMINFOW, MENUITEMINFOA)
            LPMENUITEMINFO = unicode(LPMENUITEMINFOW, LPMENUITEMINFOA)

            LPCMENUITEMINFOA = LPMENUITEMINFOA
            LPCMENUITEMINFOW = LPMENUITEMINFOW

            LPCMENUITEMINFO = unicode(LPCMENUITEMINFOW, LPCMENUITEMINFOA)
            InsertMenuItemA = declare(user32.InsertMenuItemA, BOOL, HMENU, UINT, BOOL, LPCMENUITEMINFOA)
            InsertMenuItemW = declare(user32.InsertMenuItemW, BOOL, HMENU, UINT, BOOL, LPCMENUITEMINFOW)
            InsertMenuItem = unicode(InsertMenuItemW, InsertMenuItemA)
            # !UNICODE
            GetMenuItemInfoA = declare(user32.GetMenuItemInfoA, BOOL, HMENU, UINT, BOOL, LPMENUITEMINFOA)
            GetMenuItemInfoW = declare(user32.GetMenuItemInfoW, BOOL, HMENU, UINT, BOOL, LPMENUITEMINFOW)
            GetMenuItemInfo = unicode(GetMenuItemInfoW, GetMenuItemInfoA)
            # !UNICODE
            SetMenuItemInfoA = declare(user32.SetMenuItemInfoA, BOOL, HMENU, UINT, BOOL, LPCMENUITEMINFOA)
            SetMenuItemInfoW = declare(user32.SetMenuItemInfoW, BOOL, HMENU, UINT, BOOL, LPCMENUITEMINFOW)
            SetMenuItemInfo = unicode(SetMenuItemInfoW, SetMenuItemInfoA)
            # !UNICODE
            GMDI_USEDISABLED = 0x0001
            GMDI_GOINTOPOPUPS = 0x0002
            GetMenuDefaultItem = declare(user32.GetMenuDefaultItem, UINT, HMENU, UINT, UINT)
            SetMenuDefaultItem = declare(user32.SetMenuDefaultItem, BOOL, HMENU, UINT, UINT)
            GetMenuItemRect = declare(user32.GetMenuItemRect, BOOL, HWND, HMENU, UINT, LPRECT)
            MenuItemFromPoint = declare(user32.MenuItemFromPoint, INT, HWND, HMENU, POINT)
            # WINVER >= 0x0400

            """
            * Flags for TrackPopupMenu
            """

            TPM_LEFTBUTTON = 0x0000
            TPM_RIGHTBUTTON = 0x0002
            TPM_LEFTALIGN = 0x0000
            TPM_CENTERALIGN = 0x0004
            TPM_RIGHTALIGN = 0x0008
            TPM_TOPALIGN = 0x0000
            TPM_VCENTERALIGN = 0x0010
            TPM_BOTTOMALIGN = 0x0020
            TPM_HORIZONTAL = 0x0000 # Horz alignment matters more
            TPM_VERTICAL = 0x0040 # Vert alignment matters more
            TPM_NONOTIFY = 0x0080 # Don't send any notification msgs
            TPM_RETURNCMD = 0x0100
            TPM_RECURSE = 0x0001
            TPM_HORPOSANIMATION = 0x0400
            TPM_HORNEGANIMATION = 0x0800
            TPM_VERPOSANIMATION = 0x1000
            TPM_VERNEGANIMATION = 0x2000
            TPM_NOANIMATION = 0x4000
            TPM_LAYOUTRTL = 0x8000
            TPM_WORKAREA = 0x10000
        # !NOMENUS
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop Family ***

        #
        # Drag-and-drop support
        # Obsolete - use OLE instead
        #
        class tagDROPSTRUCT(CStructure):
            _fields_ = [
                ("hwndSource", HWND),
                ("hwndSink", HWND),
                ("wFmt", DWORD),
                ("dwData", ULONG_PTR),
                ("ptDrop", POINT),
                ("dwControlData", DWORD)
            ]
        DROPSTRUCT = tagDROPSTRUCT
        PDROPSTRUCT = POINTER(DROPSTRUCT)
        LPDROPSTRUCT = PDROPSTRUCT

        # REGION ***
        DOF_EXECUTABLE = 0x8001 # wFmt flags
        DOF_DOCUMENT = 0x8002
        DOF_DIRECTORY = 0x8003
        DOF_MULTIPLE = 0x8004
        DOF_PROGMAN = 0x0001
        DOF_SHELLDATA = 0x0002
        DO_DROPFILE = 0x454C4946
        DO_PRINTFILE = 0x544E5250

        # REGION *** Desktop Family ***

        DragObject = declare(user32.DragObject, DWORD, HWND, HWND, UINT, ULONG_PTR, HCURSOR)
        DragDetect = declare(user32.DragDetect, BOOL, HWND, POINT)

        # REGION ***
        # WINVER >= 0x0400

        # REGION *** Desktop Family ***

        DrawIcon = declare(user32.DrawIcon, BOOL, HDC, INT, INT, HICON)

        # REGION ***
        if cpreproc.ifndef("NODRAWTEXT"):

            """
            * DrawText() Format Flags
            """

            DT_TOP = 0x00000000
            DT_LEFT = 0x00000000
            DT_CENTER = 0x00000001
            DT_RIGHT = 0x00000002
            DT_VCENTER = 0x00000004
            DT_BOTTOM = 0x00000008
            DT_WORDBREAK = 0x00000010
            DT_SINGLELINE = 0x00000020
            DT_EXPANDTABS = 0x00000040
            DT_TABSTOP = 0x00000080
            DT_NOCLIP = 0x00000100
            DT_EXTERNALLEADING = 0x00000200
            DT_CALCRECT = 0x00000400
            DT_NOPREFIX = 0x00000800
            DT_INTERNAL = 0x00001000
            DT_EDITCONTROL = 0x00002000
            DT_PATH_ELLIPSIS = 0x00004000
            DT_END_ELLIPSIS = 0x00008000
            DT_MODIFYSTRING = 0x00010000
            DT_RTLREADING = 0x00020000
            DT_WORD_ELLIPSIS = 0x00040000
            DT_NOFULLWIDTHCHARBREAK = 0x00080000
            DT_HIDEPREFIX = 0x00100000
            DT_PREFIXONLY = 0x00200000

            # REGION *** Desktop Family ***

            class tagDRAWTEXTPARAMS(CStructure):
                _fields_ = [
                    ("cbSize", UINT),
                    ("iTabLength", INT),
                    ("iLeftMargin", INT),
                    ("iRightMargin", INT),
                    ("uiLengthDrawn", UINT)
                ]
            DRAWTEXTPARAMS = tagDRAWTEXTPARAMS
            LPDRAWTEXTPARAMS = POINTER(DRAWTEXTPARAMS)

            DrawTextA = declare(user32.DrawTextA, INT, HDC, LPCSTR, INT, LPRECT, UINT)
            DrawTextW = declare(user32.DrawTextW, INT, HDC, LPCWSTR, INT, LPRECT, UINT)
            DrawText = unicode(DrawTextW, DrawTextA)

            DrawTextExA = declare(user32.DrawTextExA, INT, HDC, LPSTR, INT, LPRECT, UINT, LPDRAWTEXTPARAMS)
            DrawTextExW = declare(user32.DrawTextExW, INT, HDC, LPWSTR, INT, LPRECT, UINT, LPDRAWTEXTPARAMS)
            DrawTextEx = unicode(DrawTextExW, DrawTextExA)

        # !NODRAWTEXT

        # REGION *** Desktop Family ***

        GrayStringA = declare(user32.GrayStringA, BOOL, HDC, HBRUSH, GRAYSTRINGPROC, LPARAM, INT, INT, INT, INT, INT)
        GrayStringW = declare(user32.GrayStringW, BOOL, HDC, HBRUSH, GRAYSTRINGPROC, LPARAM, INT, INT, INT, INT, INT)
        GrayString = unicode(GrayStringW, GrayStringA)

        # REGION ***
        DST_COMPLEX = 0x0000
        DST_TEXT = 0x0001
        DST_PREFIXTEXT = 0x0002
        DST_ICON = 0x0003
        DST_BITMAP = 0x0004
        DSS_NORMAL = 0x0000
        DSS_UNION = 0x0010 # Gray string appearance
        DSS_DISABLED = 0x0020
        DSS_MONO = 0x0080
        DSS_HIDEPREFIX = 0x0200
        DSS_PREFIXONLY = 0x0400
        DSS_RIGHT = 0x8000

        # REGION *** Desktop Family ***

        DrawStateA = declare(user32.DrawStateA, BOOL, HDC, HBRUSH, DRAWSTATEPROC, LPARAM, WPARAM, INT, INT, INT, INT, UINT)
        DrawStateW = declare(user32.DrawStateW, BOOL, HDC, HBRUSH, DRAWSTATEPROC, LPARAM, WPARAM, INT, INT, INT, INT, UINT)
        DrawState = unicode(DrawStateW, DrawStateA)

        # REGION ***

        # REGION *** Desktop Family ***

        TabbedTextOutA = declare(user32.TabbedTextOutA, LONG, HDC, INT, INT, LPCSTR, INT, INT, PINT, INT)
        TabbedTextOutW = declare(user32.TabbedTextOutW, LONG, HDC, INT, INT, LPCWSTR, INT, INT, PINT, INT)
        TabbedTextOut = unicode(TabbedTextOutW, TabbedTextOutA)
        GetTabbedTextExtentA = declare(user32.GetTabbedTextExtentA, DWORD, HDC, LPCSTR, INT, INT, PINT)
        GetTabbedTextExtentW = declare(user32.GetTabbedTextExtentW, DWORD, HDC, LPCWSTR, INT, INT, PINT)
        GetTabbedTextExtent = unicode(GetTabbedTextExtentW, GetTabbedTextExtentA)
        # !UNICODE
        UpdateWindow = declare(user32.UpdateWindow, BOOL, HWND)
        SetActiveWindow = declare(user32.SetActiveWindow, HWND, HWND)
        GetForegroundWindow = declare(user32.GetForegroundWindow, HWND, VOID)
        PaintDesktop = declare(user32.PaintDesktop, BOOL, HDC)
        SwitchToThisWindow = declare(user32.SwitchToThisWindow, VOID, HWND, BOOL)
        SetForegroundWindow = declare(user32.SetForegroundWindow, BOOL, HWND)
        AllowSetForegroundWindow = declare(user32.AllowSetForegroundWindow, BOOL, DWORD)
        ASFW_ANY = DWORD(-1)
        LockSetForegroundWindow = declare(user32.LockSetForegroundWindow, BOOL, UINT)
        LSFW_LOCK = 1
        LSFW_UNLOCK = 2
        WindowFromDC = declare(user32.WindowFromDC, HWND, HDC)
        GetDC = declare(user32.GetDC, HDC, HWND)
        GetDCEx = declare(user32.GetDCEx, HDC, HWND, HRGN, DWORD)

        # REGION ***

        """
        * GetDCEx() flags
        """

        DCX_WINDOW = 0x00000001
        DCX_CACHE = 0x00000002
        DCX_NORESETATTRS = 0x00000004
        DCX_CLIPCHILDREN = 0x00000008
        DCX_CLIPSIBLINGS = 0x00000010
        DCX_PARENTCLIP = 0x00000020
        DCX_EXCLUDERGN = 0x00000040
        DCX_INTERSECTRGN = 0x00000080
        DCX_EXCLUDEUPDATE = 0x00000100
        DCX_INTERSECTUPDATE = 0x00000200
        DCX_LOCKWINDOWUPDATE = 0x00000400
        DCX_VALIDATE = 0x00200000

        # REGION *** Desktop Family ***

        GetWindowDC = declare(user32.GetWindowDC, HDC, HWND)
        ReleaseDC = declare(user32.ReleaseDC, INT, HWND, HDC)
        BeginPaint = declare(user32.BeginPaint, HDC, HWND, LPPAINTSTRUCT)
        EndPaint = declare(user32.EndPaint, BOOL, HWND, PPAINTSTRUCT)
        GetUpdateRect = declare(user32.GetUpdateRect, BOOL, HWND, LPRECT, BOOL)
        GetUpdateRgn = declare(user32.GetUpdateRgn, INT, HWND, HRGN, BOOL)
        SetWindowRgn = declare(user32.SetWindowRgn, INT, HWND, HRGN, BOOL)

        # REGION ***

        # REGION *** Desktop Family ***

        GetWindowRgn = declare(user32.GetWindowRgn, INT, HWND, HRGN)
        GetWindowRgnBox = declare(user32.GetWindowRgnBox, INT, HWND, LPRECT)
        ExcludeUpdateRgn = declare(user32.ExcludeUpdateRgn, INT, HDC, HWND)
        InvalidateRect = declare(user32.InvalidateRect, BOOL, HWND, PRECT, BOOL)
        ValidateRect = declare(user32.ValidateRect, BOOL, HWND, PRECT)
        InvalidateRgn = declare(user32.InvalidateRgn, BOOL, HWND, HRGN, BOOL)
        ValidateRgn = declare(user32.ValidateRgn, BOOL, HWND, HRGN)
        RedrawWindow = declare(user32.RedrawWindow, BOOL, HWND, PRECT, HRGN, UINT)

        # REGION ***

        """
        * RedrawWindow() flags
        """

        RDW_INVALIDATE = 0x0001
        RDW_INTERNALPAINT = 0x0002
        RDW_ERASE = 0x0004
        RDW_VALIDATE = 0x0008
        RDW_NOINTERNALPAINT = 0x0010
        RDW_NOERASE = 0x0020
        RDW_NOCHILDREN = 0x0040
        RDW_ALLCHILDREN = 0x0080
        RDW_UPDATENOW = 0x0100
        RDW_ERASENOW = 0x0200
        RDW_FRAME = 0x0400
        RDW_NOFRAME = 0x0800

        # REGION *** Desktop Family ***


        """
        """

        LockWindowUpdate = declare(user32.LockWindowUpdate, BOOL, HWND)
        ScrollWindow = declare(user32.ScrollWindow, BOOL, HWND, INT, INT, PRECT, PRECT)
        ScrollDC = declare(user32.ScrollDC, BOOL, HDC, INT, INT, PRECT, PRECT, HRGN, LPRECT)
        ScrollWindowEx = declare(user32.ScrollWindowEx, INT, HWND, INT, INT, PRECT, PRECT, HRGN, LPRECT, UINT)

        # REGION ***
        SW_SCROLLCHILDREN = 0x0001 # Scroll children within *lprcScroll.
        SW_INVALIDATE = 0x0002 # Invalidate after scrolling
        SW_ERASE = 0x0004 # If SW_INVALIDATE, don't send WM_ERASEBACKGROUND
        SW_SMOOTHSCROLL = 0x0010 # Use smooth scrolling

        # REGION *** Desktop Family ***

        if cpreproc.ifndef("NOSCROLL"):
            SetScrollPos = declare(user32.SetScrollPos, INT, HWND, INT, INT, BOOL)
            GetScrollPos = declare(user32.GetScrollPos, INT, HWND, INT)
            SetScrollRange = declare(user32.SetScrollRange, BOOL, HWND, INT, INT, INT, BOOL)
            GetScrollRange = declare(user32.GetScrollRange, BOOL, HWND, INT, LPINT, LPINT)
            ShowScrollBar = declare(user32.ShowScrollBar, BOOL, HWND, INT, BOOL)
            EnableScrollBar = declare(user32.EnableScrollBar, BOOL, HWND, UINT, UINT)

            """
            * EnableScrollBar() flags
            """

            ESB_ENABLE_BOTH = 0x0000
            ESB_DISABLE_BOTH = 0x0003
            ESB_DISABLE_LEFT = 0x0001
            ESB_DISABLE_RIGHT = 0x0002
            ESB_DISABLE_UP = 0x0001
            ESB_DISABLE_DOWN = 0x0002
            ESB_DISABLE_LTUP = ESB_DISABLE_LEFT
            ESB_DISABLE_RTDN = ESB_DISABLE_RIGHT
        SetPropA = declare(user32.SetPropA, BOOL, HWND, LPCSTR, HANDLE)
        SetPropW = declare(user32.SetPropW, BOOL, HWND, LPCWSTR, HANDLE)
        SetProp = unicode(SetPropW, SetPropA)
        # !UNICODE
        GetPropA = declare(user32.GetPropA, HANDLE, HWND, LPCSTR)
        GetPropW = declare(user32.GetPropW, HANDLE, HWND, LPCWSTR)
        GetProp = unicode(GetPropW, GetPropA)
        # !UNICODE
        RemovePropA = declare(user32.RemovePropA, HANDLE, HWND, LPCSTR)
        RemovePropW = declare(user32.RemovePropW, HANDLE, HWND, LPCWSTR)
        RemoveProp = unicode(RemovePropW, RemovePropA)
        # !UNICODE
        EnumPropsExA = declare(user32.EnumPropsExA, INT, HWND, PROPENUMPROCEXA, LPARAM)
        EnumPropsExW = declare(user32.EnumPropsExW, INT, HWND, PROPENUMPROCEXW, LPARAM)
        EnumPropsEx = unicode(EnumPropsExW, EnumPropsExA)
        # !UNICODE
        EnumPropsA = declare(user32.EnumPropsA, INT, HWND, PROPENUMPROCA)
        EnumPropsW = declare(user32.EnumPropsW, INT, HWND, PROPENUMPROCW)
        EnumProps = unicode(EnumPropsW, EnumPropsA)
        # !UNICODE
        SetWindowTextA = declare(user32.SetWindowTextA, BOOL, HWND, LPCSTR)
        SetWindowTextW = declare(user32.SetWindowTextW, BOOL, HWND, LPCWSTR)
        SetWindowText = unicode(SetWindowTextW, SetWindowTextA)
        # !UNICODE
        GetWindowTextA = declare(user32.GetWindowTextA, INT, HWND, LPSTR, INT)
        GetWindowTextW = declare(user32.GetWindowTextW, INT, HWND, LPWSTR, INT)
        GetWindowText = unicode(GetWindowTextW, GetWindowTextA)
        # !UNICODE
        GetWindowTextLengthA = declare(user32.GetWindowTextLengthA, INT, HWND)
        GetWindowTextLengthW = declare(user32.GetWindowTextLengthW, INT, HWND)
        GetWindowTextLength = unicode(GetWindowTextLengthW, GetWindowTextLengthA)
        # !UNICODE
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        GetClientRect = declare(user32.GetClientRect, BOOL, HWND, LPRECT)

        # REGION ***

        # REGION *** Desktop Family ***

        GetWindowRect = declare(user32.GetWindowRect, BOOL, HWND, LPRECT)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        AdjustWindowRect = declare(user32.AdjustWindowRect, BOOL, LPRECT, DWORD, BOOL)
        AdjustWindowRectEx = declare(user32.AdjustWindowRectEx, BOOL, LPRECT, DWORD, BOOL, DWORD)

        # REGION ***

        # REGION *** Desktop Family ***

        AdjustWindowRectExForDpi = declare(user32.AdjustWindowRectExForDpi, BOOL, LPRECT, DWORD, BOOL, DWORD, UINT)

        # REGION ***
        HELPINFO_WINDOW = 0x0001
        HELPINFO_MENUITEM = 0x0002

        # REGION *** Desktop Family ***

        class tagHELPINFO(CStructure): # Structure pointed to by lParam of WM_HELP
            _fields_ = [
                ("cbSize", UINT), # Size in bytes of this struct
                ("iContextType", INT), # Either HELPINFO_WINDOW or HELPINFO_MENUITEM 
                ("iCtrlId", INT), # Control Id or a Menu item Id. 
                ("hItemHandle", HANDLE), # hWnd of control or hMenu.     
                ("dwContextId", DWORD_PTR), # Context Id associated with this item 
                ("MousePos", POINT) # Mouse Position in screen co-ordinates 
            ]
        HELPINFO = tagHELPINFO
        LPHELPINFO = POINTER(HELPINFO)

        SetWindowContextHelpId = declare(user32.SetWindowContextHelpId, BOOL, HWND, DWORD)
        GetWindowContextHelpId = declare(user32.GetWindowContextHelpId, DWORD, HWND)
        SetMenuContextHelpId = declare(user32.SetMenuContextHelpId, BOOL, HMENU, DWORD)
        GetMenuContextHelpId = declare(user32.GetMenuContextHelpId, DWORD, HMENU)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        # WINVER >= 0x0400
        if cpreproc.ifndef("NOMB"):

            """
            * MessageBox() Flags
            """

            MB_OK = 0x00000000
            MB_OKCANCEL = 0x00000001
            MB_ABORTRETRYIGNORE = 0x00000002
            MB_YESNOCANCEL = 0x00000003
            MB_YESNO = 0x00000004
            MB_RETRYCANCEL = 0x00000005
            MB_CANCELTRYCONTINUE = 0x00000006
            MB_ICONHAND = 0x00000010
            MB_ICONQUESTION = 0x00000020
            MB_ICONEXCLAMATION = 0x00000030
            MB_ICONASTERISK = 0x00000040
            MB_USERICON = 0x00000080
            MB_ICONWARNING = MB_ICONEXCLAMATION
            MB_ICONERROR = MB_ICONHAND
            MB_ICONINFORMATION = MB_ICONASTERISK
            MB_ICONSTOP = MB_ICONHAND
            MB_DEFBUTTON1 = 0x00000000
            MB_DEFBUTTON2 = 0x00000100
            MB_DEFBUTTON3 = 0x00000200
            MB_DEFBUTTON4 = 0x00000300
            MB_APPLMODAL = 0x00000000
            MB_SYSTEMMODAL = 0x00001000
            MB_TASKMODAL = 0x00002000
            MB_HELP = 0x00004000 # Help Button
            MB_NOFOCUS = 0x00008000
            MB_SETFOREGROUND = 0x00010000
            MB_DEFAULT_DESKTOP_ONLY = 0x00020000
            MB_TOPMOST = 0x00040000
            MB_RIGHT = 0x00080000
            MB_RTLREADING = 0x00100000
            if cpreproc.ifdef("_WIN32_WINNT"):
                MB_SERVICE_NOTIFICATION = 0x00200000
                MB_SERVICE_NOTIFICATION = 0x00040000
                MB_SERVICE_NOTIFICATION_NT3X = 0x00040000
            MB_TYPEMASK = 0x0000000F
            MB_ICONMASK = 0x000000F0
            MB_DEFMASK = 0x00000F00
            MB_MODEMASK = 0x00003000
            MB_MISCMASK = 0x0000C000

            # REGION *** Desktop Family ***

        MessageBoxA = declare(user32.MessageBoxA, INT, HWND, LPCSTR, LPCSTR, UINT)
        MessageBoxW = declare(user32.MessageBoxW, INT, HWND, LPCWSTR, LPCWSTR, UINT)
        MessageBox = unicode(MessageBoxW, MessageBoxA)

        MessageBoxExA = declare(user32.MessageBoxExA, INT, HWND, LPCSTR, LPCSTR, UINT, WORD)
        MessageBoxExW = declare(user32.MessageBoxExW, INT, HWND, LPCWSTR, LPCWSTR, UINT, WORD)
        MessageBoxEx = unicode(MessageBoxExW, MessageBoxExA)
        # !UNICODE

        MSGBOXCALLBACK = CALLBACK(VOID, LPHELPINFO)

        class tagMSGBOXPARAMSA(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("hwndOwner", HWND),
                ("hInstance", HINSTANCE),
                ("lpszText", LPCSTR),
                ("lpszCaption", LPCSTR),
                ("dwStyle", DWORD),
                ("lpszIcon", LPCSTR),
                ("dwContextHelpId", DWORD_PTR),
                ("lpfnMsgBoxCallback", MSGBOXCALLBACK),
                ("dwLanguageId", DWORD)
            ]
        MSGBOXPARAMSA = tagMSGBOXPARAMSA
        PMSGBOXPARAMSA = POINTER(MSGBOXPARAMSA)
        LPMSGBOXPARAMSA = PMSGBOXPARAMSA

        class tagMSGBOXPARAMSW(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("hwndOwner", HWND),
                ("hInstance", HINSTANCE),
                ("lpszText", LPCWSTR),
                ("lpszCaption", LPCWSTR),
                ("dwStyle", DWORD),
                ("lpszIcon", LPCWSTR),
                ("dwContextHelpId", DWORD_PTR),
                ("lpfnMsgBoxCallback", MSGBOXCALLBACK),
                ("dwLanguageId", DWORD)
            ]
        MSGBOXPARAMSW = tagMSGBOXPARAMSW
        PMSGBOXPARAMSW = POINTER(MSGBOXPARAMSW)
        LPMSGBOXPARAMSW = PMSGBOXPARAMSW

        MSGBOXPARAMS = unicode(MSGBOXPARAMSW, MSGBOXPARAMSA)
        PMSGBOXPARAMS = unicode(PMSGBOXPARAMSW, PMSGBOXPARAMSA)
        LPMSGBOXPARAMS = unicode(LPMSGBOXPARAMSW, LPMSGBOXPARAMSA)

        MessageBoxIndirectA = declare(user32.MessageBoxIndirectA, INT, PMSGBOXPARAMSA)
        MessageBoxIndirectW = declare(user32.MessageBoxIndirectW, INT, PMSGBOXPARAMSW)
        MessageBoxIndirect = unicode(MessageBoxIndirectW, MessageBoxIndirectA)
        # !UNICODE
        # WINVER >= 0x0400
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop Family ***

        MessageBeep = declare(user32.MessageBeep, BOOL, UINT)

        # REGION ***
        # !NOMB

        # REGION *** Desktop Family ***


        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        ShowCursor = declare(user32.ShowCursor, INT, BOOL)

        # REGION ***

        # REGION *** Desktop Family ***

        SetCursorPos = declare(user32.SetCursorPos, BOOL, INT, INT)
        
        SetPhysicalCursorPos = declare(user32.SetPhysicalCursorPos, BOOL, INT, INT)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        SetCursor = declare(user32.SetCursor, HCURSOR, HCURSOR)

        GetCursorPos = declare(user32.GetCursorPos, BOOL, LPPOINT)

        # REGION ***

        # REGION *** Desktop Family ***

        GetPhysicalCursorPos = declare(user32.GetPhysicalCursorPos, BOOL, LPPOINT)

        GetClipCursor = declare(user32.GetClipCursor, BOOL, LPRECT)

        GetCursor = declare(user32.GetCursor, HCURSOR, VOID)

        CreateCaret = declare(user32.CreateCaret, BOOL, HWND, HBITMAP, INT, INT)

        GetCaretBlinkTime = declare(user32.GetCaretBlinkTime, UINT, VOID)

        SetCaretBlinkTime = declare(user32.SetCaretBlinkTime, BOOL, UINT)

        DestroyCaret = declare(user32.DestroyCaret, BOOL, VOID)

        HideCaret = declare(user32.HideCaret, BOOL, HWND)

        ShowCaret = declare(user32.ShowCaret, BOOL, HWND)

        SetCaretPos = declare(user32.SetCaretPos, BOOL, INT, INT)
        
        GetCaretPos = declare(user32.GetCaretPos, BOOL, LPPOINT)

        ClientToScreen = declare(user32.ClientToScreen, BOOL, HWND, LPPOINT)

        ScreenToClient = declare(user32.ScreenToClient, BOOL, HWND, LPPOINT)

        LogicalToPhysicalPoint = declare(user32.LogicalToPhysicalPoint, BOOL, HWND, LPPOINT)

        PhysicalToLogicalPoint = declare(user32.PhysicalToLogicalPoint, BOOL, HWND, LPPOINT)

        LogicalToPhysicalPointForPerMonitorDPI = declare(user32.LogicalToPhysicalPointForPerMonitorDPI, BOOL, HWND, LPPOINT)

        PhysicalToLogicalPointForPerMonitorDPI = declare(user32.PhysicalToLogicalPointForPerMonitorDPI, BOOL, HWND, LPPOINT)

        MapWindowPoints = declare(user32.MapWindowPoints, INT, HWND, HWND, LPPOINT, UINT)

        WindowFromPoint = declare(user32.WindowFromPoint, HWND, POINT)

        WindowFromPhysicalPoint = declare(user32.WindowFromPhysicalPoint, HWND, POINT)

        ChildWindowFromPoint = declare(user32.ChildWindowFromPoint, HWND, HWND, POINT)

        # REGION ***

        # REGION *** Desktop or PC Family ***

        ClipCursor = declare(user32.ClipCursor, BOOL, PRECT)

        # REGION ***
        CWP_ALL = 0x0000
        CWP_SKIPINVISIBLE = 0x0001
        CWP_SKIPDISABLED = 0x0002
        CWP_SKIPTRANSPARENT = 0x0004

        # REGION *** Desktop Family ***

        ChildWindowFromPointEx = declare(user32.ChildWindowFromPointEx, HWND, HWND, POINT, UINT)

        # REGION ***
        if cpreproc.ifndef("NOCOLOR"):

            """
            * Color Types
            """

            CTLCOLOR_MSGBOX = 0
            CTLCOLOR_EDIT = 1
            CTLCOLOR_LISTBOX = 2
            CTLCOLOR_BTN = 3
            CTLCOLOR_DLG = 4
            CTLCOLOR_SCROLLBAR = 5
            CTLCOLOR_STATIC = 6
            CTLCOLOR_MAX = 7
            COLOR_SCROLLBAR = 0
            COLOR_BACKGROUND = 1
            COLOR_ACTIVECAPTION = 2
            COLOR_INACTIVECAPTION = 3
            COLOR_MENU = 4
            COLOR_WINDOW = 5
            COLOR_WINDOWFRAME = 6
            COLOR_MENUTEXT = 7
            COLOR_WINDOWTEXT = 8
            COLOR_CAPTIONTEXT = 9
            COLOR_ACTIVEBORDER = 10
            COLOR_INACTIVEBORDER = 11
            COLOR_APPWORKSPACE = 12
            COLOR_HIGHLIGHT = 13
            COLOR_HIGHLIGHTTEXT = 14
            COLOR_BTNFACE = 15
            COLOR_BTNSHADOW = 16
            COLOR_GRAYTEXT = 17
            COLOR_BTNTEXT = 18
            COLOR_INACTIVECAPTIONTEXT = 19
            COLOR_BTNHIGHLIGHT = 20
            COLOR_3DDKSHADOW = 21
            COLOR_3DLIGHT = 22
            COLOR_INFOTEXT = 23
            COLOR_INFOBK = 24
            COLOR_HOTLIGHT = 26
            COLOR_GRADIENTACTIVECAPTION = 27
            COLOR_GRADIENTINACTIVECAPTION = 28
            COLOR_MENUHILIGHT = 29
            COLOR_MENUBAR = 30
            COLOR_DESKTOP = COLOR_BACKGROUND
            COLOR_3DFACE = COLOR_BTNFACE
            COLOR_3DSHADOW = COLOR_BTNSHADOW
            COLOR_3DHIGHLIGHT = COLOR_BTNHIGHLIGHT
            COLOR_3DHILIGHT = COLOR_BTNHIGHLIGHT
            COLOR_BTNHILIGHT = COLOR_BTNHIGHLIGHT

            # REGION *** Desktop Family ***

            GetSysColor = declare(user32.GetSysColor, DWORD, INT)
            GetSysColorBrush = declare(user32.GetSysColorBrush, HBRUSH, INT)
            SetSysColors = declare(user32.SetSysColors, BOOL, INT, PINT, POINTER(COLORREF))

            # REGION ***
        # !NOCOLOR

        # REGION *** Desktop Family ***

        DrawFocusRect = declare(user32.DrawFocusRect, BOOL, HDC, PRECT)
        FillRect = declare(user32.FillRect, INT, HDC, PRECT, HBRUSH)
        FrameRect = declare(user32.FrameRect, INT, HDC, PRECT, HBRUSH)
        InvertRect = declare(user32.InvertRect, BOOL, HDC, PRECT)
        SetRect = declare(user32.SetRect, BOOL, LPRECT, INT, INT, INT, INT)
        SetRectEmpty = declare(user32.SetRectEmpty, BOOL, LPRECT)
        CopyRect = declare(user32.CopyRect, BOOL, LPRECT, PRECT)
        InflateRect = declare(user32.InflateRect, BOOL, LPRECT, INT, INT)
        IntersectRect = declare(user32.IntersectRect, BOOL, LPRECT, PRECT, PRECT)
        UnionRect = declare(user32.UnionRect, BOOL, LPRECT, PRECT, PRECT)
        SubtractRect = declare(user32.SubtractRect, BOOL, LPRECT, PRECT, PRECT)
        OffsetRect = declare(user32.OffsetRect, BOOL, LPRECT, INT, INT)
        IsRectEmpty = declare(user32.IsRectEmpty, BOOL, PRECT)
        EqualRect = declare(user32.EqualRect, BOOL, PRECT, PRECT)
        PtInRect = declare(user32.PtInRect, BOOL, PRECT, POINT)
        if cpreproc.ifndef("NOWINOFFSETS"):
            GetWindowWord = declare(user32.GetWindowWord, WORD, HWND, INT)
            SetWindowWord = declare(user32.SetWindowWord, WORD, HWND, INT, WORD)

            # REGION ***

        # REGION *** Desktop Family or Games Family ***

        if cpreproc.ifndef("NOWINOFFSETS"):
            GetWindowLongA = declare(user32.GetWindowLongA, LONG, HWND, INT)
            GetWindowLongW = declare(user32.GetWindowLongW, LONG, HWND, INT)
            GetWindowLong = unicode(GetWindowLongW, GetWindowLongA)
            SetWindowLongA = declare(user32.SetWindowLongA, LONG, HWND, INT, LONG)
            SetWindowLongW = declare(user32.SetWindowLongW, LONG, HWND, INT, LONG)
            SetWindowLong = unicode(SetWindowLongW, SetWindowLongA)
            
            GetWindowLongPtrA = declare(user32.GetWindowLongPtrA, LONG_PTR, HWND, INT)
            GetWindowLongPtrW = declare(user32.GetWindowLongPtrW, LONG_PTR, HWND, INT)
            GetWindowLongPtr = unicode(GetWindowLongPtrW, GetWindowLongPtrA)

            SetWindowLongPtrA = declare(user32.SetWindowLongPtrA, LONG_PTR, HWND, INT, LONG_PTR)
            SetWindowLongPtrW = declare(user32.SetWindowLongPtrW, LONG_PTR, HWND, INT, LONG_PTR)
            SetWindowLongPtr = unicode(SetWindowLongPtrW, SetWindowLongPtrA)
        # !NOWINOFFSETS

        # REGION ***

        # REGION *** Desktop Family ***

        if cpreproc.ifndef("NOWINOFFSETS"):
            GetClassWord = declare(user32.GetClassWord, WORD, HWND, INT)
            SetClassWord = declare(user32.SetClassWord, WORD, HWND, INT, WORD)
            GetClassLongA = declare(user32.GetClassLongA, DWORD, HWND, INT)
            GetClassLongW = declare(user32.GetClassLongW, DWORD, HWND, INT)
            GetClassLong = unicode(GetClassLongW, GetClassLongA)
            SetClassLongA = declare(user32.SetClassLongA, DWORD, HWND, INT, LONG)
            SetClassLongW = declare(user32.SetClassLongW, DWORD, HWND, INT, LONG)
            SetClassLong = unicode(SetClassLongW, SetClassLongA)
            
            GetClassLongPtrA = declare(user32.GetClassLongPtrA, ULONG_PTR, HWND, INT)
            GetClassLongPtrW = declare(user32.GetClassLongPtrW, ULONG_PTR, HWND, INT)
            GetClassLongPtr = unicode(GetClassLongPtrW, GetClassLongPtrA)
            
            SetClassLongPtrA = declare(user32.SetClassLongPtrA, ULONG_PTR, HWND, INT, LONG_PTR)
            SetClassLongPtrW = declare(user32.SetClassLongPtrW, ULONG_PTR, HWND, INT, LONG_PTR)
            SetClassLongPtr = unicode(SetClassLongPtrW, SetClassLongPtrA)
        # !NOWINOFFSETS
        GetProcessDefaultLayout = declare(user32.GetProcessDefaultLayout, BOOL, PDWORD)
        SetProcessDefaultLayout = declare(user32.SetProcessDefaultLayout, BOOL, DWORD)
        GetDesktopWindow = declare(user32.GetDesktopWindow, HWND, VOID)
        GetParent = declare(user32.GetParent, HWND, HWND)
        SetParent = declare(user32.SetParent, HWND, HWND, HWND)
        EnumChildWindows = declare(user32.EnumChildWindows, BOOL, HWND, WNDENUMPROC, LPARAM)
        FindWindowA = declare(user32.FindWindowA, HWND, LPCSTR, LPCSTR)
        FindWindowW = declare(user32.FindWindowW, HWND, LPCWSTR, LPCWSTR)
        FindWindow = unicode(FindWindowW, FindWindowA)
        # !UNICODE
        FindWindowExA = declare(user32.FindWindowExA, HWND, HWND, HWND, LPCSTR, LPCSTR)
        FindWindowExW = declare(user32.FindWindowExW, HWND, HWND, HWND, LPCWSTR, LPCWSTR)
        FindWindowEx = unicode(FindWindowExW, FindWindowExA)
        GetShellWindow = declare(user32.GetShellWindow, HWND, VOID)
        # WINVER >= 0x0400
        RegisterShellHookWindow = declare(user32.RegisterShellHookWindow, BOOL, HWND)
        DeregisterShellHookWindow = declare(user32.DeregisterShellHookWindow, BOOL, HWND)
        EnumWindows = declare(user32.EnumWindows, BOOL, WNDENUMPROC, LPARAM)
        EnumThreadWindows = declare(user32.EnumThreadWindows, BOOL, DWORD, WNDENUMPROC, LPARAM)
        EnumTaskWindows = lambda hTask, lpfn, lParam: EnumThreadWindows(HandleToULong(hTask), lpfn, lParam)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop Family or Games Family ***

        GetClassNameA = declare(user32.GetClassNameA, INT, HWND, LPSTR, INT, )
        GetClassNameW = declare(user32.GetClassNameW, INT, HWND, LPWSTR, INT, )
        GetClassName = unicode(GetClassNameW, GetClassNameA)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_GAMES)

        # REGION ***

        # REGION *** Desktop Family ***

        GetTopWindow = declare(user32.GetTopWindow, HWND, HWND)
        GetNextWindow = lambda hWnd, wCmd: GetWindow(hWnd, wCmd)
        GetSysModalWindow = lambda: NULL
        SetSysModalWindow = lambda hWnd: NULL
        GetWindowThreadProcessId = declare(user32.GetWindowThreadProcessId, DWORD, HWND, LPDWORD)
        IsGUIThread = declare(user32.IsGUIThread, BOOL, BOOL)
        GetWindowTask = lambda hWnd: HANDLE(DWORD_PTR(GetWindowThreadProcessId(hWnd, NULL).value).value)
        GetLastActivePopup = declare(user32.GetLastActivePopup, HWND, HWND)

        """
        * GetWindow() Constants
        """

        GW_HWNDFIRST = 0
        GW_HWNDLAST = 1
        GW_HWNDNEXT = 2
        GW_HWNDPREV = 3
        GW_OWNER = 4
        GW_CHILD = 5
        GW_MAX = 5
        GW_ENABLEDPOPUP = 6
        GW_MAX = 6
        GetWindow = declare(user32.GetWindow, HWND, HWND, UINT)
        if cpreproc.ifndef("NOWH"):
            SetWindowsHookA = declare(user32.SetWindowsHookA, HHOOK, INT, HOOKPROC)
            SetWindowsHookW = declare(user32.SetWindowsHookW, HHOOK, INT, HOOKPROC)
            SetWindowsHook = unicode(SetWindowsHookW, SetWindowsHookA)
            UnhookWindowsHook = declare(user32.UnhookWindowsHook, BOOL, INT, HOOKPROC)
            SetWindowsHookExA = declare(user32.SetWindowsHookExA, HHOOK, INT, HOOKPROC, HINSTANCE, DWORD)
            SetWindowsHookExW = declare(user32.SetWindowsHookExW, HHOOK, INT, HOOKPROC, HINSTANCE, DWORD)
            SetWindowsHookEx = unicode(SetWindowsHookExW, SetWindowsHookExA)
            # !UNICODE
            UnhookWindowsHookEx = declare(user32.UnhookWindowsHookEx, BOOL, HHOOK)
            CallNextHookEx = declare(user32.CallNextHookEx, LRESULT, HHOOK, INT, WPARAM, LPARAM)

            """
            * Macros for source-level compatibility with old functions.
            """

            DefHookProc = lambda nCode, wParam, lParam, phhk: CallNextHookEx(phhk._obj if hasattr(phhk, '_obj') else phhk.contents, nCode, wParam, lParam)
        # !NOWH
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        if cpreproc.ifndef("NOMENUS"):

            """
            * Menu flags for Add/Check/EnableMenuItem()
            """

            MF_INSERT = 0x00000000
            MF_CHANGE = 0x00000080
            MF_APPEND = 0x00000100
            MF_DELETE = 0x00000200
            MF_REMOVE = 0x00001000
            MF_BYCOMMAND = 0x00000000
            MF_BYPOSITION = 0x00000400
            MF_SEPARATOR = 0x00000800
            MF_ENABLED = 0x00000000
            MF_GRAYED = 0x00000001
            MF_DISABLED = 0x00000002
            MF_UNCHECKED = 0x00000000
            MF_CHECKED = 0x00000008
            MF_USECHECKBITMAPS = 0x00000200
            MF_STRING = 0x00000000
            MF_BITMAP = 0x00000004
            MF_OWNERDRAW = 0x00000100
            MF_POPUP = 0x00000010
            MF_MENUBARBREAK = 0x00000020
            MF_MENUBREAK = 0x00000040
            MF_UNHILITE = 0x00000000
            MF_HILITE = 0x00000080
            MF_DEFAULT = 0x00001000
            MF_SYSMENU = 0x00002000
            MF_HELP = 0x00004000
            MF_RIGHTJUSTIFY = 0x00004000
            MF_MOUSESELECT = 0x00008000
            MF_END = 0x00000080 # Obsolete -- only used by old RES files
            MFT_STRING = MF_STRING
            MFT_BITMAP = MF_BITMAP
            MFT_MENUBARBREAK = MF_MENUBARBREAK
            MFT_MENUBREAK = MF_MENUBREAK
            MFT_OWNERDRAW = MF_OWNERDRAW
            MFT_RADIOCHECK = 0x00000200
            MFT_SEPARATOR = MF_SEPARATOR
            MFT_RIGHTORDER = 0x00002000
            MFT_RIGHTJUSTIFY = MF_RIGHTJUSTIFY
            MFS_GRAYED = 0x00000003
            MFS_DISABLED = MFS_GRAYED
            MFS_CHECKED = MF_CHECKED
            MFS_HILITE = MF_HILITE
            MFS_ENABLED = MF_ENABLED
            MFS_UNCHECKED = MF_UNCHECKED
            MFS_UNHILITE = MF_UNHILITE
            MFS_DEFAULT = MF_DEFAULT

            # REGION *** Desktop Family ***

            CheckMenuRadioItem = declare(user32.CheckMenuRadioItem, BOOL, HMENU, UINT, UINT, UINT, UINT)

            """
            * Menu item resource format
            """
            class MENUITEMTEMPLATEHEADER(CStructure):
                _fields_ = [
                    ("versionNumber", WORD),
                    ("offset", WORD)
                ]
            PMENUITEMTEMPLATEHEADER = POINTER(MENUITEMTEMPLATEHEADER)
            
            class MENUITEMTEMPLATE(CStructure): # version 0
                _fields_ = [
                    ("mtOption", WORD),
                    ("mtID", WORD),
                    ("mtString", WCHAR * 1)
                ]
            PMENUITEMTEMPLATE = POINTER(MENUITEMTEMPLATE)

            MF_END = 0x00000080

            # REGION ***
        # !NOMENUS
        if cpreproc.ifndef("NOSYSCOMMANDS"):

            """
            * System Menu Command Values
            """

            SC_SIZE = 0xF000
            SC_MOVE = 0xF010
            SC_MINIMIZE = 0xF020
            SC_MAXIMIZE = 0xF030
            SC_NEXTWINDOW = 0xF040
            SC_PREVWINDOW = 0xF050
            SC_CLOSE = 0xF060
            SC_VSCROLL = 0xF070
            SC_HSCROLL = 0xF080
            SC_MOUSEMENU = 0xF090
            SC_KEYMENU = 0xF100
            SC_ARRANGE = 0xF110
            SC_RESTORE = 0xF120
            SC_TASKLIST = 0xF130
            SC_SCREENSAVE = 0xF140
            SC_HOTKEY = 0xF150
            SC_DEFAULT = 0xF160
            SC_MONITORPOWER = 0xF170
            SC_CONTEXTHELP = 0xF180
            SC_SEPARATOR = 0xF00F
            SCF_ISSECURE = 0x00000001
            GET_SC_WPARAM = lambda wParam: (INT(wParam).value & 0xFFF0)

            """
            * Obsolete names
            """

            SC_ICON = SC_MINIMIZE
            SC_ZOOM = SC_MAXIMIZE
        # !NOSYSCOMMANDS

        """
        * Resource Loading Routines
        """

        # REGION *** Desktop Family ***

        LoadBitmapA = declare(user32.LoadBitmapA, HBITMAP, HINSTANCE, LPCSTR)
        LoadBitmapW = declare(user32.LoadBitmapW, HBITMAP, HINSTANCE, LPCWSTR)
        LoadBitmap = unicode(LoadBitmapW, LoadBitmapA)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop or Games Family ***

        LoadCursorA = declare(user32.LoadCursorA, HCURSOR, HINSTANCE, LPCSTR)
        LoadCursorW = declare(user32.LoadCursorW, HCURSOR, HINSTANCE, LPCWSTR)
        LoadCursor = unicode(LoadCursorW, LoadCursorA)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_GAMES)

        # REGION ***

        # REGION *** Desktop Family ***

        LoadCursorFromFileA = declare(user32.LoadCursorFromFileA, HCURSOR, LPCSTR)
        LoadCursorFromFileW = declare(user32.LoadCursorFromFileW, HCURSOR, LPCWSTR)
        LoadCursorFromFile = unicode(LoadCursorFromFileW, LoadCursorFromFileA)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        CopyIcon = declare(user32.CopyIcon, HICON, HICON)

        # REGION ***

        # REGION *** Desktop or Games Family ***

        CreateCursor = declare(user32.CreateCursor, HCURSOR, HINSTANCE, INT, INT, INT, INT, PVOID, PVOID)
        DestroyCursor = declare(user32.DestroyCursor, BOOL, HCURSOR)

        # REGION ***

        # REGION *** Desktop Family ***

        CopyCursor = lambda pcur: HCURSOR(CopyIcon(HICON(pcur)))
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***

        """
        * Standard Cursor IDs
        """

        IDC_ARROW = MAKEINTRESOURCE(32512)
        IDC_IBEAM = MAKEINTRESOURCE(32513)
        IDC_WAIT = MAKEINTRESOURCE(32514)
        IDC_CROSS = MAKEINTRESOURCE(32515)
        IDC_UPARROW = MAKEINTRESOURCE(32516)
        IDC_SIZE = MAKEINTRESOURCE(32640) # OBSOLETE: use IDC_SIZEALL
        IDC_ICON = MAKEINTRESOURCE(32641) # OBSOLETE: use IDC_ARROW
        IDC_SIZENWSE = MAKEINTRESOURCE(32642)
        IDC_SIZENESW = MAKEINTRESOURCE(32643)
        IDC_SIZEWE = MAKEINTRESOURCE(32644)
        IDC_SIZENS = MAKEINTRESOURCE(32645)
        IDC_SIZEALL = MAKEINTRESOURCE(32646)
        IDC_NO = MAKEINTRESOURCE(32648) #not in win3.1
        IDC_HAND = MAKEINTRESOURCE(32649)
        IDC_APPSTARTING = MAKEINTRESOURCE(32650) #not in win3.1
        IDC_HELP = MAKEINTRESOURCE(32651)
        IDC_PIN = MAKEINTRESOURCE(32671)
        IDC_PERSON = MAKEINTRESOURCE(32672)

        # REGION *** Desktop Family ***

        SetSystemCursor = declare(user32.SetSystemCursor, BOOL, HCURSOR, DWORD)

        class _ICONINFO(CStructure):
            _fields_ = [
                ("fIcon", BOOL),
                ("xHotspot", DWORD),
                ("yHotspot", DWORD),
                ("hbmMask", HBITMAP),
                ("hbmColor", HBITMAP)
            ]
        ICONINFO = _ICONINFO
        PICONINFO = POINTER(ICONINFO)

        LoadIconA = declare(user32.LoadIconA, HICON, HINSTANCE, LPCSTR)
        LoadIconW = declare(user32.LoadIconW, HICON, HINSTANCE, LPCWSTR)
        LoadIcon = unicode(LoadIconW, LoadIconA)
        
        PrivateExtractIconsA = declare(user32.PrivateExtractIconsA, UINT, LPCSTR, INT, INT, INT, POINTER(HICON), PUINT, UINT, UINT)
        PrivateExtractIconsW = declare(user32.PrivateExtractIconsW, UINT, LPCWSTR, INT, INT, INT, POINTER(HICON), PUINT, UINT, UINT)
        PrivateExtractIcons = unicode(PrivateExtractIconsW, PrivateExtractIconsA)
        
        CreateIcon = declare(user32.CreateIcon, HICON, HINSTANCE, INT, INT, BYTE, BYTE, PBYTE, PBYTE)
        DestroyIcon = declare(user32.DestroyIcon, BOOL, HICON)
        LookupIconIdFromDirectory = declare(user32.LookupIconIdFromDirectory, INT, PBYTE, BOOL)
        LookupIconIdFromDirectoryEx = declare(user32.LookupIconIdFromDirectoryEx, INT, PBYTE, BOOL, INT, INT, UINT)
        CreateIconFromResource = declare(user32.CreateIconFromResource, HICON, PBYTE, DWORD, BOOL, DWORD)
        CreateIconFromResourceEx = declare(user32.CreateIconFromResourceEx, HICON, PBYTE, DWORD, BOOL, DWORD, INT, INT, UINT)

        # Icon/Cursor header
        class tagCURSORSHAPE(CStructure):
            _fields_ = [
                ("xHotSpot", INT),
                ("yHotSpot", INT),
                ("cx", INT),
                ("cy", INT),
                ("cbWidth", INT),
                ("Planes", BYTE),
                ("BitsPixel", BYTE)
            ]
        CURSORSHAPE = tagCURSORSHAPE
        LPCURSORSHAPE = POINTER(CURSORSHAPE)

        # REGION ***

        IMAGE_BITMAP = 0
        IMAGE_ICON = 1
        IMAGE_CURSOR = 2
        IMAGE_ENHMETAFILE = 3
        LR_DEFAULTCOLOR = 0x00000000
        LR_MONOCHROME = 0x00000001
        LR_COLOR = 0x00000002
        LR_COPYRETURNORG = 0x00000004
        LR_COPYDELETEORG = 0x00000008
        LR_LOADFROMFILE = 0x00000010
        LR_LOADTRANSPARENT = 0x00000020
        LR_DEFAULTSIZE = 0x00000040
        LR_VGACOLOR = 0x00000080
        LR_LOADMAP3DCOLORS = 0x00001000
        LR_CREATEDIBSECTION = 0x00002000
        LR_COPYFROMRESOURCE = 0x00004000
        LR_SHARED = 0x00008000

        # REGION *** Desktop Family ***

        LoadImageA = declare(user32.LoadImageA, HANDLE, HINSTANCE, LPCSTR, UINT, INT, INT, UINT)
        LoadImageW = declare(user32.LoadImageW, HANDLE, HINSTANCE, LPCWSTR, UINT, INT, INT, UINT)
        LoadImage = unicode(LoadImageW, LoadImageA)
        CopyImage = declare(user32.CopyImage, HANDLE, HANDLE, UINT, INT, INT, UINT)
        DI_MASK = 0x0001
        DI_IMAGE = 0x0002
        DI_NORMAL = 0x0003
        DI_COMPAT = 0x0004
        DI_DEFAULTSIZE = 0x0008
        DI_NOMIRROR = 0x0010

        # REGION ***

        # REGION *** Desktop Family ***

        CreateIconIndirect = declare(user32.CreateIconIndirect, HICON, PICONINFO)
        GetIconInfo = declare(user32.GetIconInfo, BOOL, HICON, PICONINFO)

        class _ICONINFOEXA(CStructure):
            _fields_ = [
                ("cbSize", DWORD),
                ("fIcon", BOOL),
                ("xHotspot", DWORD),
                ("yHotspot", DWORD),
                ("hbmMask", HBITMAP),
                ("hbmColor", HBITMAP),
                ("wResID", WORD),
                ("szModName", CHAR * MAX_PATH),
                ("szResName", CHAR * MAX_PATH)
            ]
        ICONINFOEXA = _ICONINFOEXA
        PICONINFOEXA = POINTER(ICONINFOEXA)

        class _ICONINFOEXW(CStructure):
            _fields_ = [
                ("cbSize", DWORD),
                ("fIcon", BOOL),
                ("xHotspot", DWORD),
                ("yHotspot", DWORD),
                ("hbmMask", HBITMAP),
                ("hbmColor", HBITMAP),
                ("wResID", WORD),
                ("szModName", WCHAR * MAX_PATH),
                ("szResName", WCHAR * MAX_PATH)
            ]
        ICONINFOEXW = _ICONINFOEXW
        PICONINFOEXW = POINTER(ICONINFOEXW)

        ICONINFOEX = unicode(ICONINFOEXW, ICONINFOEXA)
        PICONINFOEX = unicode(PICONINFOEXW, PICONINFOEXA)

        GetIconInfoExA = declare(user32.GetIconInfoExA, BOOL, HICON, PICONINFOEXA)
        GetIconInfoExW = declare(user32.GetIconInfoExW, BOOL, HICON, PICONINFOEXW)
        GetIconInfoEx = unicode(GetIconInfoExW, GetIconInfoExA)
        RES_ICON = 1
        RES_CURSOR = 2

        # REGION ***
        if cpreproc.ifdef("OEMRESOURCE"):

            """
            * OEM Resource Ordinal Numbers
            """

            OBM_CLOSE = 32754
            OBM_UPARROW = 32753
            OBM_DNARROW = 32752
            OBM_RGARROW = 32751
            OBM_LFARROW = 32750
            OBM_REDUCE = 32749
            OBM_ZOOM = 32748
            OBM_RESTORE = 32747
            OBM_REDUCED = 32746
            OBM_ZOOMD = 32745
            OBM_RESTORED = 32744
            OBM_UPARROWD = 32743
            OBM_DNARROWD = 32742
            OBM_RGARROWD = 32741
            OBM_LFARROWD = 32740
            OBM_MNARROW = 32739
            OBM_COMBO = 32738
            OBM_UPARROWI = 32737
            OBM_DNARROWI = 32736
            OBM_RGARROWI = 32735
            OBM_LFARROWI = 32734
            OBM_OLD_CLOSE = 32767
            OBM_SIZE = 32766
            OBM_OLD_UPARROW = 32765
            OBM_OLD_DNARROW = 32764
            OBM_OLD_RGARROW = 32763
            OBM_OLD_LFARROW = 32762
            OBM_BTSIZE = 32761
            OBM_CHECK = 32760
            OBM_CHECKBOXES = 32759
            OBM_BTNCORNERS = 32758
            OBM_OLD_REDUCE = 32757
            OBM_OLD_ZOOM = 32756
            OBM_OLD_RESTORE = 32755
            OCR_NORMAL = 32512
            OCR_IBEAM = 32513
            OCR_WAIT = 32514
            OCR_CROSS = 32515
            OCR_UP = 32516
            OCR_SIZE = 32640 # OBSOLETE: use OCR_SIZEALL
            OCR_ICON = 32641 # OBSOLETE: use OCR_NORMAL
            OCR_SIZENWSE = 32642
            OCR_SIZENESW = 32643
            OCR_SIZEWE = 32644
            OCR_SIZENS = 32645
            OCR_SIZEALL = 32646
            OCR_ICOCUR = 32647 # OBSOLETE: use OIC_WINLOGO
            OCR_NO = 32648
            OCR_HAND = 32649
            OCR_APPSTARTING = 32650
            OIC_SAMPLE = 32512
            OIC_HAND = 32513
            OIC_QUES = 32514
            OIC_BANG = 32515
            OIC_NOTE = 32516
            OIC_WINLOGO = 32517
            OIC_WARNING = OIC_BANG
            OIC_ERROR = OIC_HAND
            OIC_INFORMATION = OIC_NOTE
            OIC_SHIELD = 32518
        # OEMRESOURCE
        ORD_LANGDRIVER = 1 # The ordinal number for the entry point of
                            # language drivers
                            #

        if cpreproc.ifndef("NOICONS"):

            """
            * Standard Icon IDs
            """

            if cpreproc.ifdef("RC_INVOKED"):
                IDI_APPLICATION = 32512
                IDI_HAND = 32513
                IDI_QUESTION = 32514
                IDI_EXCLAMATION = 32515
                IDI_ASTERISK = 32516
                IDI_WINLOGO = 32517
                IDI_SHIELD = 32518
            else:
                IDI_APPLICATION = MAKEINTRESOURCE(32512)
                IDI_HAND = MAKEINTRESOURCE(32513)
                IDI_QUESTION = MAKEINTRESOURCE(32514)
                IDI_EXCLAMATION = MAKEINTRESOURCE(32515)
                IDI_ASTERISK = MAKEINTRESOURCE(32516)
                IDI_WINLOGO = MAKEINTRESOURCE(32517)
                IDI_SHIELD = MAKEINTRESOURCE(32518)
            # RC_INVOKED
            IDI_WARNING = IDI_EXCLAMATION
            IDI_ERROR = IDI_HAND
            IDI_INFORMATION = IDI_ASTERISK
        # !NOICONS
        if cpreproc.ifdef("NOAPISET"):

            # REGION *** Desktop Family ***

            LoadStringA = declare(user32.LoadStringA, INT, HINSTANCE, UINT, LPSTR, INT)
            LoadStringW = declare(user32.LoadStringW, INT, HINSTANCE, UINT, LPWSTR, INT)
            LoadString = unicode(LoadStringW, LoadStringA)
            # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            # REGION ***
        # NOAPISET

        """
        * Dialog Box Command IDs
        """

        IDOK = 1
        IDCANCEL = 2
        IDABORT = 3
        IDRETRY = 4
        IDIGNORE = 5
        IDYES = 6
        IDNO = 7
        IDCLOSE = 8
        IDHELP = 9
        IDTRYAGAIN = 10
        IDCONTINUE = 11
        if "IDTIMEOUT" not in globals():
                IDTIMEOUT = 32000
        # WINVER >= 0x0501
        if cpreproc.ifndef("NOCTLMGR"):

            """
            * Control Manager Structures and Definitions
            """

            if cpreproc.ifndef("NOWINSTYLES"):

                """
                * Edit Control Styles
                """

                ES_LEFT = 0x0000
                ES_CENTER = 0x0001
                ES_RIGHT = 0x0002
                ES_MULTILINE = 0x0004
                ES_UPPERCASE = 0x0008
                ES_LOWERCASE = 0x0010
                ES_PASSWORD = 0x0020
                ES_AUTOVSCROLL = 0x0040
                ES_AUTOHSCROLL = 0x0080
                ES_NOHIDESEL = 0x0100
                ES_OEMCONVERT = 0x0400
                ES_READONLY = 0x0800
                ES_WANTRETURN = 0x1000
                ES_NUMBER = 0x2000
            # !NOWINSTYLES

            """
            * Edit Control Notification Codes
            """

            EN_SETFOCUS = 0x0100
            EN_KILLFOCUS = 0x0200
            EN_CHANGE = 0x0300
            EN_UPDATE = 0x0400
            EN_ERRSPACE = 0x0500
            EN_MAXTEXT = 0x0501
            EN_HSCROLL = 0x0601
            EN_VSCROLL = 0x0602
            EN_ALIGN_LTR_EC = 0x0700
            EN_ALIGN_RTL_EC = 0x0701
            EN_BEFORE_PASTE = 0x0800
            EN_AFTER_PASTE = 0x0801
            EC_LEFTMARGIN = 0x0001
            EC_RIGHTMARGIN = 0x0002
            EC_USEFONTINFO = 0xffff
            EMSIS_COMPOSITIONSTRING = 0x0001
            EIMES_GETCOMPSTRATONCE = 0x0001
            EIMES_CANCELCOMPSTRINFOCUS = 0x0002
            EIMES_COMPLETECOMPSTRKILLFOCUS = 0x0004
            if cpreproc.ifndef("NOWINMESSAGES"):

                """
                * Edit Control Messages
                """

                EM_GETSEL = 0x00B0
                EM_SETSEL = 0x00B1
                EM_GETRECT = 0x00B2
                EM_SETRECT = 0x00B3
                EM_SETRECTNP = 0x00B4
                EM_SCROLL = 0x00B5
                EM_LINESCROLL = 0x00B6
                EM_SCROLLCARET = 0x00B7
                EM_GETMODIFY = 0x00B8
                EM_SETMODIFY = 0x00B9
                EM_GETLINECOUNT = 0x00BA
                EM_LINEINDEX = 0x00BB
                EM_SETHANDLE = 0x00BC
                EM_GETHANDLE = 0x00BD
                EM_GETTHUMB = 0x00BE
                EM_LINELENGTH = 0x00C1
                EM_REPLACESEL = 0x00C2
                EM_GETLINE = 0x00C4
                EM_LIMITTEXT = 0x00C5
                EM_CANUNDO = 0x00C6
                EM_UNDO = 0x00C7
                EM_FMTLINES = 0x00C8
                EM_LINEFROMCHAR = 0x00C9
                EM_SETTABSTOPS = 0x00CB
                EM_SETPASSWORDCHAR = 0x00CC
                EM_EMPTYUNDOBUFFER = 0x00CD
                EM_GETFIRSTVISIBLELINE = 0x00CE
                EM_SETREADONLY = 0x00CF
                EM_SETWORDBREAKPROC = 0x00D0
                EM_GETWORDBREAKPROC = 0x00D1
                EM_GETPASSWORDCHAR = 0x00D2
                EM_SETMARGINS = 0x00D3
                EM_GETMARGINS = 0x00D4
                EM_SETLIMITTEXT = EM_LIMITTEXT # ;win40 Name change
                EM_GETLIMITTEXT = 0x00D5
                EM_POSFROMCHAR = 0x00D6
                EM_CHARFROMPOS = 0x00D7
                EM_SETIMESTATUS = 0x00D8
                EM_GETIMESTATUS = 0x00D9
                EM_ENABLEFEATURE = 0x00DA
            # !NOWINMESSAGES

            """
            * EM_ENABLEFEATURE options
            """
            EDIT_CONTROL_FEATURE = INT
            if True:
                EDIT_CONTROL_FEATURE_ENTERPRISE_DATA_PROTECTION_PASTE_SUPPORT  = 0
                EDIT_CONTROL_FEATURE_PASTE_NOTIFICATIONS                       = 1

            """
            * EDITWORDBREAKPROC code values
            """

            WB_LEFT = 0
            WB_RIGHT = 1
            WB_ISDELIMITER = 2

            """
            * Button Control Styles
            """

            BS_PUSHBUTTON = 0x00000000
            BS_DEFPUSHBUTTON = 0x00000001
            BS_CHECKBOX = 0x00000002
            BS_AUTOCHECKBOX = 0x00000003
            BS_RADIOBUTTON = 0x00000004
            BS_3STATE = 0x00000005
            BS_AUTO3STATE = 0x00000006
            BS_GROUPBOX = 0x00000007
            BS_USERBUTTON = 0x00000008
            BS_AUTORADIOBUTTON = 0x00000009
            BS_PUSHBOX = 0x0000000A
            BS_OWNERDRAW = 0x0000000B
            BS_TYPEMASK = 0x0000000F
            BS_LEFTTEXT = 0x00000020
            BS_TEXT = 0x00000000
            BS_ICON = 0x00000040
            BS_BITMAP = 0x00000080
            BS_LEFT = 0x00000100
            BS_RIGHT = 0x00000200
            BS_CENTER = 0x00000300
            BS_TOP = 0x00000400
            BS_BOTTOM = 0x00000800
            BS_VCENTER = 0x00000C00
            BS_PUSHLIKE = 0x00001000
            BS_MULTILINE = 0x00002000
            BS_NOTIFY = 0x00004000
            BS_FLAT = 0x00008000
            BS_RIGHTBUTTON = BS_LEFTTEXT

            """
            * User Button Notification Codes
            """

            BN_CLICKED = 0
            BN_PAINT = 1
            BN_HILITE = 2
            BN_UNHILITE = 3
            BN_DISABLE = 4
            BN_DOUBLECLICKED = 5
            BN_PUSHED = BN_HILITE
            BN_UNPUSHED = BN_UNHILITE
            BN_DBLCLK = BN_DOUBLECLICKED
            BN_SETFOCUS = 6
            BN_KILLFOCUS = 7

            """
            * Button Control Messages
            """

            BM_GETCHECK = 0x00F0
            BM_SETCHECK = 0x00F1
            BM_GETSTATE = 0x00F2
            BM_SETSTATE = 0x00F3
            BM_SETSTYLE = 0x00F4
            BM_CLICK = 0x00F5
            BM_GETIMAGE = 0x00F6
            BM_SETIMAGE = 0x00F7
            BM_SETDONTCLICK = 0x00F8
            BST_UNCHECKED = 0x0000
            BST_CHECKED = 0x0001
            BST_INDETERMINATE = 0x0002
            BST_PUSHED = 0x0004
            BST_FOCUS = 0x0008

            """
            * Static Control Constants
            """

            SS_LEFT = 0x00000000
            SS_CENTER = 0x00000001
            SS_RIGHT = 0x00000002
            SS_ICON = 0x00000003
            SS_BLACKRECT = 0x00000004
            SS_GRAYRECT = 0x00000005
            SS_WHITERECT = 0x00000006
            SS_BLACKFRAME = 0x00000007
            SS_GRAYFRAME = 0x00000008
            SS_WHITEFRAME = 0x00000009
            SS_USERITEM = 0x0000000A
            SS_SIMPLE = 0x0000000B
            SS_LEFTNOWORDWRAP = 0x0000000C
            SS_OWNERDRAW = 0x0000000D
            SS_BITMAP = 0x0000000E
            SS_ENHMETAFILE = 0x0000000F
            SS_ETCHEDHORZ = 0x00000010
            SS_ETCHEDVERT = 0x00000011
            SS_ETCHEDFRAME = 0x00000012
            SS_TYPEMASK = 0x0000001F
            SS_REALSIZECONTROL = 0x00000040
            SS_NOPREFIX = 0x00000080 # Don't do "&" character translation
            SS_NOTIFY = 0x00000100
            SS_CENTERIMAGE = 0x00000200
            SS_RIGHTJUST = 0x00000400
            SS_REALSIZEIMAGE = 0x00000800
            SS_SUNKEN = 0x00001000
            SS_EDITCONTROL = 0x00002000
            SS_ENDELLIPSIS = 0x00004000
            SS_PATHELLIPSIS = 0x00008000
            SS_WORDELLIPSIS = 0x0000C000
            SS_ELLIPSISMASK = 0x0000C000
            if cpreproc.ifndef("NOWINMESSAGES"):

                """
                * Static Control Mesages
                """

                STM_SETICON = 0x0170
                STM_GETICON = 0x0171
                STM_SETIMAGE = 0x0172
                STM_GETIMAGE = 0x0173
                STN_CLICKED = 0
                STN_DBLCLK = 1
                STN_ENABLE = 2
                STN_DISABLE = 3
                STM_MSGMAX = 0x0174
            # !NOWINMESSAGES

            """
            * Dialog window class
            """

            WC_DIALOG = (MAKEINTATOM(0x8002))

            """
            * Get/SetWindowWord/Long offsets for use with WC_DIALOG windows
            """

            DWL_MSGRESULT = 0
            DWL_DLGPROC = 4
            DWL_USER = 8
            DWLP_MSGRESULT = 0
            DWLP_DLGPROC = DWLP_MSGRESULT + sizeof(LRESULT)
            DWLP_USER = DWLP_DLGPROC + sizeof(DLGPROC)

            # REGION *** Desktop Family ***


            """
            * Dialog Manager Routines
            """

            if cpreproc.ifndef("NOMSG"):
                IsDialogMessageA = declare(user32.IsDialogMessageA, BOOL, HWND, LPMSG)
                IsDialogMessageW = declare(user32.IsDialogMessageW, BOOL, HWND, LPMSG)
                IsDialogMessage = unicode(IsDialogMessageW, IsDialogMessageA)
            # !NOMSG
            MapDialogRect = declare(user32.MapDialogRect, BOOL, HWND, LPRECT)
            DlgDirListA = declare(user32.DlgDirListA, INT, HWND, LPSTR, INT, INT, UINT)
            DlgDirListW = declare(user32.DlgDirListW, INT, HWND, LPWSTR, INT, INT, UINT)
            DlgDirList = unicode(DlgDirListW, DlgDirListA)
            # !UNICODE
            # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            # REGION ***

            """
            * DlgDirList, DlgDirListComboBox flags values
            """

            DDL_READWRITE = 0x0000
            DDL_READONLY = 0x0001
            DDL_HIDDEN = 0x0002
            DDL_SYSTEM = 0x0004
            DDL_DIRECTORY = 0x0010
            DDL_ARCHIVE = 0x0020
            DDL_POSTMSGS = 0x2000
            DDL_DRIVES = 0x4000
            DDL_EXCLUSIVE = 0x8000

            # REGION *** Desktop Family ***

            DlgDirSelectExA = declare(user32.DlgDirSelectExA, BOOL, HWND, LPSTR, INT, INT)
            DlgDirSelectExW = declare(user32.DlgDirSelectExW, BOOL, HWND, LPWSTR, INT, INT)
            DlgDirSelectEx = unicode(DlgDirSelectExW, DlgDirSelectExA)
            DlgDirListComboBoxA = declare(user32.DlgDirListComboBoxA, INT, HWND, LPSTR, INT, INT, UINT)
            DlgDirListComboBoxW = declare(user32.DlgDirListComboBoxW, INT, HWND, LPWSTR, INT, INT, UINT)
            DlgDirListComboBox = unicode(DlgDirListComboBoxW, DlgDirListComboBoxA)
            # !UNICODE
            DlgDirSelectComboBoxExA = declare(user32.DlgDirSelectComboBoxExA, BOOL, HWND, LPSTR, INT, INT)
            DlgDirSelectComboBoxExW = declare(user32.DlgDirSelectComboBoxExW, BOOL, HWND, LPWSTR, INT, INT)
            DlgDirSelectComboBoxEx = unicode(DlgDirSelectComboBoxExW, DlgDirSelectComboBoxExA)
            # !UNICODE
            # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

            # REGION ***

            """
            * Dialog Styles
            """

            DS_ABSALIGN = 0x01
            DS_SYSMODAL = 0x02
            DS_LOCALEDIT = 0x20 # Edit items get Local storage.
            DS_SETFONT = 0x40 # User specified font for Dlg controls
            DS_MODALFRAME = 0x80 # Can be combined with WS_CAPTION
            DS_NOIDLEMSG = 0x100 # WM_ENTERIDLE message will not be sent
            DS_SETFOREGROUND = 0x200 # not in win3.1
            DS_3DLOOK = 0x0004
            DS_FIXEDSYS = 0x0008
            DS_NOFAILCREATE = 0x0010
            DS_CONTROL = 0x0400
            DS_CENTER = 0x0800
            DS_CENTERMOUSE = 0x1000
            DS_CONTEXTHELP = 0x2000
            DS_SHELLFONT = (DS_SETFONT | DS_FIXEDSYS)
            DS_USEPIXELS = 0x8000
            DM_GETDEFID = (WM_USER+0)
            DM_SETDEFID = (WM_USER+1)
            DM_REPOSITION = (WM_USER+2)

            """
            * Returned in HIWORD() of DM_GETDEFID result if msg is supported
            """

            DC_HASDEFID = 0x534B

            """
            * Dialog Codes
            """

            DLGC_WANTARROWS = 0x0001 # Control wants arrow keys
            DLGC_WANTTAB = 0x0002 # Control wants tab keys
            DLGC_WANTALLKEYS = 0x0004 # Control wants all keys
            DLGC_WANTMESSAGE = 0x0004 # Pass message to control
            DLGC_HASSETSEL = 0x0008 # Understands EM_SETSEL message
            DLGC_DEFPUSHBUTTON = 0x0010 # Default pushbutton
            DLGC_UNDEFPUSHBUTTON = 0x0020 # Non-default pushbutton
            DLGC_RADIOBUTTON = 0x0040 # Radio button
            DLGC_WANTCHARS = 0x0080 # Want WM_CHAR messages
            DLGC_STATIC = 0x0100 # Static item: don't include
            DLGC_BUTTON = 0x2000 # Button item: can be checked
            LB_CTLCODE = 0

            """
            * Listbox Return Values
            """

            LB_OKAY = 0
            LB_ERR = (-1)
            LB_ERRSPACE = (-2)

            """
            **  The idStaticPath parameter to DlgDirList can have the following values
            **  ORed if the list box should show other details of the files along with
            **  the name of the files;
            """


            """
            * Listbox Notification Codes
            """

            LBN_ERRSPACE = (-2)
            LBN_SELCHANGE = 1
            LBN_DBLCLK = 2
            LBN_SELCANCEL = 3
            LBN_SETFOCUS = 4
            LBN_KILLFOCUS = 5
            if cpreproc.ifndef("NOWINMESSAGES"):

                """
                * Listbox messages
                """

                LB_ADDSTRING = 0x0180
                LB_INSERTSTRING = 0x0181
                LB_DELETESTRING = 0x0182
                LB_SELITEMRANGEEX = 0x0183
                LB_RESETCONTENT = 0x0184
                LB_SETSEL = 0x0185
                LB_SETCURSEL = 0x0186
                LB_GETSEL = 0x0187
                LB_GETCURSEL = 0x0188
                LB_GETTEXT = 0x0189
                LB_GETTEXTLEN = 0x018A
                LB_GETCOUNT = 0x018B
                LB_SELECTSTRING = 0x018C
                LB_DIR = 0x018D
                LB_GETTOPINDEX = 0x018E
                LB_FINDSTRING = 0x018F
                LB_GETSELCOUNT = 0x0190
                LB_GETSELITEMS = 0x0191
                LB_SETTABSTOPS = 0x0192
                LB_GETHORIZONTALEXTENT = 0x0193
                LB_SETHORIZONTALEXTENT = 0x0194
                LB_SETCOLUMNWIDTH = 0x0195
                LB_ADDFILE = 0x0196
                LB_SETTOPINDEX = 0x0197
                LB_GETITEMRECT = 0x0198
                LB_GETITEMDATA = 0x0199
                LB_SETITEMDATA = 0x019A
                LB_SELITEMRANGE = 0x019B
                LB_SETANCHORINDEX = 0x019C
                LB_GETANCHORINDEX = 0x019D
                LB_SETCARETINDEX = 0x019E
                LB_GETCARETINDEX = 0x019F
                LB_SETITEMHEIGHT = 0x01A0
                LB_GETITEMHEIGHT = 0x01A1
                LB_FINDSTRINGEXACT = 0x01A2
                LB_SETLOCALE = 0x01A5
                LB_GETLOCALE = 0x01A6
                LB_SETCOUNT = 0x01A7
                LB_INITSTORAGE = 0x01A8
                LB_ITEMFROMPOINT = 0x01A9
                LB_MULTIPLEADDSTRING = 0x01B1
                LB_GETLISTBOXINFO = 0x01B2
                LB_MSGMAX = 0x01B3
                LB_MSGMAX = 0x01B1
                LB_MSGMAX = 0x01B0
                LB_MSGMAX = 0x01A8
            # !NOWINMESSAGES
            if cpreproc.ifndef("NOWINSTYLES"):

                """
                * Listbox Styles
                """

                LBS_NOTIFY = 0x0001
                LBS_SORT = 0x0002
                LBS_NOREDRAW = 0x0004
                LBS_MULTIPLESEL = 0x0008
                LBS_OWNERDRAWFIXED = 0x0010
                LBS_OWNERDRAWVARIABLE = 0x0020
                LBS_HASSTRINGS = 0x0040
                LBS_USETABSTOPS = 0x0080
                LBS_NOINTEGRALHEIGHT = 0x0100
                LBS_MULTICOLUMN = 0x0200
                LBS_WANTKEYBOARDINPUT = 0x0400
                LBS_EXTENDEDSEL = 0x0800
                LBS_DISABLENOSCROLL = 0x1000
                LBS_NODATA = 0x2000
                LBS_NOSEL = 0x4000
                LBS_COMBOBOX = 0x8000
                LBS_STANDARD = (LBS_NOTIFY | LBS_SORT | WS_VSCROLL | WS_BORDER)
            # !NOWINSTYLES

            """
            * Combo Box return Values
            """

            CB_OKAY = 0
            CB_ERR = (-1)
            CB_ERRSPACE = (-2)

            """
            * Combo Box Notification Codes
            """

            CBN_ERRSPACE = (-1)
            CBN_SELCHANGE = 1
            CBN_DBLCLK = 2
            CBN_SETFOCUS = 3
            CBN_KILLFOCUS = 4
            CBN_EDITCHANGE = 5
            CBN_EDITUPDATE = 6
            CBN_DROPDOWN = 7
            CBN_CLOSEUP = 8
            CBN_SELENDOK = 9
            CBN_SELENDCANCEL = 10
            if cpreproc.ifndef("NOWINSTYLES"):

                """
                * Combo Box styles
                """

                CBS_SIMPLE = 0x0001
                CBS_DROPDOWN = 0x0002
                CBS_DROPDOWNLIST = 0x0003
                CBS_OWNERDRAWFIXED = 0x0010
                CBS_OWNERDRAWVARIABLE = 0x0020
                CBS_AUTOHSCROLL = 0x0040
                CBS_OEMCONVERT = 0x0080
                CBS_SORT = 0x0100
                CBS_HASSTRINGS = 0x0200
                CBS_NOINTEGRALHEIGHT = 0x0400
                CBS_DISABLENOSCROLL = 0x0800
                CBS_UPPERCASE = 0x2000
                CBS_LOWERCASE = 0x4000
            # !NOWINSTYLES

            """
            * Combo Box messages
            """

            if cpreproc.ifndef("NOWINMESSAGES"):
                CB_GETEDITSEL = 0x0140
                CB_LIMITTEXT = 0x0141
                CB_SETEDITSEL = 0x0142
                CB_ADDSTRING = 0x0143
                CB_DELETESTRING = 0x0144
                CB_DIR = 0x0145
                CB_GETCOUNT = 0x0146
                CB_GETCURSEL = 0x0147
                CB_GETLBTEXT = 0x0148
                CB_GETLBTEXTLEN = 0x0149
                CB_INSERTSTRING = 0x014A
                CB_RESETCONTENT = 0x014B
                CB_FINDSTRING = 0x014C
                CB_SELECTSTRING = 0x014D
                CB_SETCURSEL = 0x014E
                CB_SHOWDROPDOWN = 0x014F
                CB_GETITEMDATA = 0x0150
                CB_SETITEMDATA = 0x0151
                CB_GETDROPPEDCONTROLRECT = 0x0152
                CB_SETITEMHEIGHT = 0x0153
                CB_GETITEMHEIGHT = 0x0154
                CB_SETEXTENDEDUI = 0x0155
                CB_GETEXTENDEDUI = 0x0156
                CB_GETDROPPEDSTATE = 0x0157
                CB_FINDSTRINGEXACT = 0x0158
                CB_SETLOCALE = 0x0159
                CB_GETLOCALE = 0x015A
                CB_GETTOPINDEX = 0x015b
                CB_SETTOPINDEX = 0x015c
                CB_GETHORIZONTALEXTENT = 0x015d
                CB_SETHORIZONTALEXTENT = 0x015e
                CB_GETDROPPEDWIDTH = 0x015f
                CB_SETDROPPEDWIDTH = 0x0160
                CB_INITSTORAGE = 0x0161
                CB_MULTIPLEADDSTRING = 0x0163
                CB_GETCOMBOBOXINFO = 0x0164
                CB_MSGMAX = 0x0165
                CB_MSGMAX = 0x0163
                CB_MSGMAX = 0x0162
                CB_MSGMAX = 0x015B
            # !NOWINMESSAGES
            if cpreproc.ifndef("NOWINSTYLES"):

                """
                * Scroll Bar Styles
                """

                SBS_HORZ = 0x0000
                SBS_VERT = 0x0001
                SBS_TOPALIGN = 0x0002
                SBS_LEFTALIGN = 0x0002
                SBS_BOTTOMALIGN = 0x0004
                SBS_RIGHTALIGN = 0x0004
                SBS_SIZEBOXTOPLEFTALIGN = 0x0002
                SBS_SIZEBOXBOTTOMRIGHTALIGN = 0x0004
                SBS_SIZEBOX = 0x0008
                SBS_SIZEGRIP = 0x0010
            # !NOWINSTYLES

            """
            * Scroll bar messages
            """

            if cpreproc.ifndef("NOWINMESSAGES"):
                SBM_SETPOS = 0x00E0 #not in win3.1
                SBM_GETPOS = 0x00E1 #not in win3.1
                SBM_SETRANGE = 0x00E2 #not in win3.1
                SBM_SETRANGEREDRAW = 0x00E6 #not in win3.1
                SBM_GETRANGE = 0x00E3 #not in win3.1
                SBM_ENABLE_ARROWS = 0x00E4 #not in win3.1
                SBM_SETSCROLLINFO = 0x00E9
                SBM_GETSCROLLINFO = 0x00EA
                SBM_GETSCROLLBARINFO = 0x00EB
                SIF_RANGE = 0x0001
                SIF_PAGE = 0x0002
                SIF_POS = 0x0004
                SIF_DISABLENOSCROLL = 0x0008
                SIF_TRACKPOS = 0x0010
                SIF_ALL = (SIF_RANGE | SIF_PAGE | SIF_POS | SIF_TRACKPOS)

                # REGION *** Desktop Family ***

                class tagSCROLLINFO(CStructure):
                    _fields_ = [
                        ("cbSize", UINT),
                        ("fMask", UINT),
                        ("nMin", INT),
                        ("nMax", INT),
                        ("nPage", UINT),
                        ("nPos", INT),
                        ("nTrackPos", INT)
                    ]
                SCROLLINFO = tagSCROLLINFO
                LPSCROLLINFO = POINTER(SCROLLINFO)
                LPCSCROLLINFO = LPSCROLLINFO

                SetScrollInfo = declare(user32.SetScrollInfo, INT, HWND, INT, LPCSCROLLINFO, BOOL)
                GetScrollInfo = declare(user32.GetScrollInfo, BOOL, HWND, INT, LPSCROLLINFO)
                # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

                # REGION ***
            # !NOWINMESSAGES
        # !NOCTLMGR
        if cpreproc.ifndef("NOMDI"):

            """
            * MDI client style bits
            """

            MDIS_ALLCHILDSTYLES = 0x0001

            """
            * wParam Flags for WM_MDITILE and WM_MDICASCADE messages.
            """

            MDITILE_VERTICAL = 0x0000 #not in win3.1
            MDITILE_HORIZONTAL = 0x0001 #not in win3.1
            MDITILE_SKIPDISABLED = 0x0002 #not in win3.1
            MDITILE_ZORDER = 0x0004

            # REGION *** Desktop Family ***

            class tagMDICREATESTRUCTA(CStructure):
                _fields_ = [
                    ("szClass", LPCSTR),
                    ("szTitle", LPCSTR),
                    ("hOwner", HANDLE),
                    ("x", INT),
                    ("y", INT),
                    ("cx", INT),
                    ("cy", INT),
                    ("style", DWORD),
                    ("lParam", LPARAM) # app-defined stuff
                ]
            MDICREATESTRUCTA = tagMDICREATESTRUCTA
            LPMDICREATESTRUCTA = POINTER(MDICREATESTRUCTA)

            class tagMDICREATESTRUCTW(CStructure):
                _fields_ = [
                    ("szClass", LPCWSTR),
                    ("szTitle", LPCWSTR),
                    ("hOwner", HANDLE),
                    ("x", INT),
                    ("y", INT),
                    ("cx", INT),
                    ("cy", INT),
                    ("style", DWORD),
                    ("lParam", LPARAM) # app-defined stuff
                ]
            MDICREATESTRUCTW = tagMDICREATESTRUCTW
            LPMDICREATESTRUCTW = POINTER(MDICREATESTRUCTW)

            MDICREATESTRUCT = unicode(MDICREATESTRUCTW, MDICREATESTRUCTA)
            LPMDICREATESTRUCT = unicode(LPMDICREATESTRUCTW, LPMDICREATESTRUCTA)

            class tagCLIENTCREATESTRUCT(CStructure):
                _fields_ = [
                    ("hWindowMenu", HANDLE),
                    ("idFirstChild", UINT)
                ]
            CLIENTCREATESTRUCT = tagCLIENTCREATESTRUCT
            LPCLIENTCREATESTRUCT = POINTER(CLIENTCREATESTRUCT)

            DefFrameProcA = declare(user32.DefFrameProcA, LRESULT, HWND, HWND, UINT, WPARAM, LPARAM)
            DefFrameProcW = declare(user32.DefFrameProcW, LRESULT, HWND, HWND, UINT, WPARAM, LPARAM)
            DefFrameProc = unicode(DefFrameProcW, DefFrameProcA)

            DefMDIChildProcA = declare(user32.DefMDIChildProcA, LRESULT, HWND, UINT, WPARAM, LPARAM)
            DefMDIChildProcW = declare(user32.DefMDIChildProcW, LRESULT, HWND, UINT, WPARAM, LPARAM)
            DefMDIChildProc = unicode(DefMDIChildProcW, DefMDIChildProcA)
            
            if cpreproc.ifndef("NOMSG"):
                TranslateMDISysAccel = declare(user32.TranslateMDISysAccel, BOOL, HWND, LPMSG)
            # !NOMSG
            ArrangeIconicWindows = declare(user32.ArrangeIconicWindows, UINT, HWND)

            CreateMDIWindowA = declare(user32.CreateMDIWindowA, HWND, LPCSTR, LPCSTR, DWORD, INT, INT, INT, INT, HWND, HINSTANCE, LPARAM)
            CreateMDIWindowW = declare(user32.CreateMDIWindowW, HWND, LPCWSTR, LPCWSTR, DWORD, INT, INT, INT, INT, HWND, HINSTANCE, LPARAM)
            CreateMDIWindow = unicode(CreateMDIWindowW, CreateMDIWindowA)
            
            TileWindows = declare(user32.TileWindows, WORD, HWND, UINT, PRECT, UINT, POINTER(HWND))

            # REGION ***
        # !NOMDI
    # !NOUSER

    ### Help support ############################
    if cpreproc.ifndef("NOHELP"):
        # REGION *** Desktop Family ***

        HELPPOLY = DWORD
        class MULTIKEYHELPA(CStructure):
            _fields_ = [
                ("mkSize", DWORD),
                ("mkKeylist", CHAR),
                ("szKeyphrase", CHAR * 1)
            ]
        PMULTIKEYHELPA = POINTER(MULTIKEYHELPA)
        LPMULTIKEYHELPA = PMULTIKEYHELPA

        class MULTIKEYHELPW(CStructure):
            _fields_ = [
                ("mkSize", DWORD),
                ("mkKeylist", WCHAR),
                ("szKeyphrase", WCHAR * 1)
            ]
        PMULTIKEYHELPW = POINTER(MULTIKEYHELPW)
        LPMULTIKEYHELPW = PMULTIKEYHELPW
        MULTIKEYHELP = unicode(MULTIKEYHELPW, MULTIKEYHELPA)
        PMULTIKEYHELP = unicode(PMULTIKEYHELPW, PMULTIKEYHELPA)
        LPMULTIKEYHELP = PMULTIKEYHELP

        class HELPWININFOA(CStructure):
            _fields_ = [
                ("wStructSize", INT),
                ("x", INT),
                ("y", INT),
                ("dx", INT),
                ("dy", INT),
                ("wMax", INT),
                ("rgchMember", CHAR * 2)
            ]
        PHELPWININFOA = POINTER(HELPWININFOA)
        LPHELPWININFOA = PHELPWININFOA

        class HELPWININFOW(CStructure):
            _fields_ = [
                ("wStructSize", INT),
                ("x", INT),
                ("y", INT),
                ("dx", INT),
                ("dy", INT),
                ("wMax", INT),
                ("rgchMember", WCHAR * 2)
            ]
        PHELPWININFOW = POINTER(HELPWININFOW)
        LPHELPWININFOW = PHELPWININFOW
        HELPWININFO = unicode(HELPWININFOW, HELPWININFOA)
        PHELPWININFO = unicode(PHELPWININFOW, PHELPWININFOA)
        LPHELPWININFO = PHELPWININFO

        """
        * Commands to pass to WinHelp()
        """
        HELP_CONTEXT = 0x0001        # Display topic in ulTopic
        HELP_QUIT = 0x0002           # Terminate help
        HELP_INDEX = 0x0003          # Display index
        HELP_CONTENTS = 0x0003
        HELP_HELPONHELP = 0x0004     # Display help on using help
        HELP_SETINDEX = 0x0005       # Set current Index for multi index help
        HELP_SETCONTENTS = 0x0005
        HELP_CONTEXTPOPUP = 0x0008
        HELP_FORCEFILE = 0x0009
        HELP_KEY = 0x0101            # Display topic for keyword in offabData
        HELP_COMMAND = 0x0102
        HELP_PARTIALKEY = 0x0105
        HELP_MULTIKEY = 0x0201
        HELP_SETWINPOS = 0x0203
        HELP_CONTEXTMENU = 0x000a
        HELP_FINDER = 0x000b
        HELP_WM_HELP = 0x000c
        HELP_SETPOPUP_POS = 0x000d

        HELP_TCARD = 0x8000
        HELP_TCARD_DATA = 0x0010
        HELP_TCARD_OTHER_CALLER = 0x0011

        # These are in winhelp.h in Win95.
        IDH_NO_HELP = 28440
        IDH_MISSING_CONTEXT = 28441 # Control doesn't have matching help context
        IDH_GENERIC_HELP_BUTTON = 28442 # Property sheet help button
        IDH_OK = 28443
        IDH_CANCEL = 28444
        IDH_HELP = 28445

        WinHelpA = declare(user32.WinHelpA, BOOL, HWND, LPCSTR, UINT, ULONG_PTR)
        WinHelpW = declare(user32.WinHelpW, BOOL, HWND, LPCWSTR, UINT, ULONG_PTR)
        WinHelp = unicode(WinHelpW, WinHelpA)
        # REGION ***
    #!NOHELP

    GR_GDIOBJECTS = 0       # Count of GDI objects
    GR_USEROBJECTS = 1       # Count of USER objects
    GR_GDIOBJECTS_PEAK = 2       # Peak count of GDI objects
    GR_USEROBJECTS_PEAK = 4       # Peak count of USER objects
    GR_GLOBAL = HANDLE(-2)

    # REGION *** Desktop Family ***

    GetGuiResources = declare(user32.GetGuiResources, DWORD, HANDLE, DWORD)

    # REGION ***

    # REGION *** Desktop Family ***

    if cpreproc.ifndef("NOSYSPARAMSINFO"):

        """
        * Parameter for SystemParametersInfo.
        """

        SPI_GETBEEP = 0x0001
        SPI_SETBEEP = 0x0002
        SPI_GETMOUSE = 0x0003
        SPI_SETMOUSE = 0x0004
        SPI_GETBORDER = 0x0005
        SPI_SETBORDER = 0x0006
        SPI_GETKEYBOARDSPEED = 0x000A
        SPI_SETKEYBOARDSPEED = 0x000B
        SPI_LANGDRIVER = 0x000C
        SPI_ICONHORIZONTALSPACING = 0x000D
        SPI_GETSCREENSAVETIMEOUT = 0x000E
        SPI_SETSCREENSAVETIMEOUT = 0x000F
        SPI_GETSCREENSAVEACTIVE = 0x0010
        SPI_SETSCREENSAVEACTIVE = 0x0011
        SPI_GETGRIDGRANULARITY = 0x0012
        SPI_SETGRIDGRANULARITY = 0x0013
        SPI_SETDESKWALLPAPER = 0x0014
        SPI_SETDESKPATTERN = 0x0015
        SPI_GETKEYBOARDDELAY = 0x0016
        SPI_SETKEYBOARDDELAY = 0x0017
        SPI_ICONVERTICALSPACING = 0x0018
        SPI_GETICONTITLEWRAP = 0x0019
        SPI_SETICONTITLEWRAP = 0x001A
        SPI_GETMENUDROPALIGNMENT = 0x001B
        SPI_SETMENUDROPALIGNMENT = 0x001C
        SPI_SETDOUBLECLKWIDTH = 0x001D
        SPI_SETDOUBLECLKHEIGHT = 0x001E
        SPI_GETICONTITLELOGFONT = 0x001F
        SPI_SETDOUBLECLICKTIME = 0x0020
        SPI_SETMOUSEBUTTONSWAP = 0x0021
        SPI_SETICONTITLELOGFONT = 0x0022
        SPI_GETFASTTASKSWITCH = 0x0023
        SPI_SETFASTTASKSWITCH = 0x0024
        SPI_SETDRAGFULLWINDOWS = 0x0025
        SPI_GETDRAGFULLWINDOWS = 0x0026
        SPI_GETNONCLIENTMETRICS = 0x0029
        SPI_SETNONCLIENTMETRICS = 0x002A
        SPI_GETMINIMIZEDMETRICS = 0x002B
        SPI_SETMINIMIZEDMETRICS = 0x002C
        SPI_GETICONMETRICS = 0x002D
        SPI_SETICONMETRICS = 0x002E
        SPI_SETWORKAREA = 0x002F
        SPI_GETWORKAREA = 0x0030
        SPI_SETPENWINDOWS = 0x0031
        SPI_GETHIGHCONTRAST = 0x0042
        SPI_SETHIGHCONTRAST = 0x0043
        SPI_GETKEYBOARDPREF = 0x0044
        SPI_SETKEYBOARDPREF = 0x0045
        SPI_GETSCREENREADER = 0x0046
        SPI_SETSCREENREADER = 0x0047
        SPI_GETANIMATION = 0x0048
        SPI_SETANIMATION = 0x0049
        SPI_GETFONTSMOOTHING = 0x004A
        SPI_SETFONTSMOOTHING = 0x004B
        SPI_SETDRAGWIDTH = 0x004C
        SPI_SETDRAGHEIGHT = 0x004D
        SPI_SETHANDHELD = 0x004E
        SPI_GETLOWPOWERTIMEOUT = 0x004F
        SPI_GETPOWEROFFTIMEOUT = 0x0050
        SPI_SETLOWPOWERTIMEOUT = 0x0051
        SPI_SETPOWEROFFTIMEOUT = 0x0052
        SPI_GETLOWPOWERACTIVE = 0x0053
        SPI_GETPOWEROFFACTIVE = 0x0054
        SPI_SETLOWPOWERACTIVE = 0x0055
        SPI_SETPOWEROFFACTIVE = 0x0056
        SPI_SETCURSORS = 0x0057
        SPI_SETICONS = 0x0058
        SPI_GETDEFAULTINPUTLANG = 0x0059
        SPI_SETDEFAULTINPUTLANG = 0x005A
        SPI_SETLANGTOGGLE = 0x005B
        SPI_GETWINDOWSEXTENSION = 0x005C
        SPI_SETMOUSETRAILS = 0x005D
        SPI_GETMOUSETRAILS = 0x005E
        SPI_SETSCREENSAVERRUNNING = 0x0061
        SPI_SCREENSAVERRUNNING = SPI_SETSCREENSAVERRUNNING
        SPI_GETFILTERKEYS = 0x0032
        SPI_SETFILTERKEYS = 0x0033
        SPI_GETTOGGLEKEYS = 0x0034
        SPI_SETTOGGLEKEYS = 0x0035
        SPI_GETMOUSEKEYS = 0x0036
        SPI_SETMOUSEKEYS = 0x0037
        SPI_GETSHOWSOUNDS = 0x0038
        SPI_SETSHOWSOUNDS = 0x0039
        SPI_GETSTICKYKEYS = 0x003A
        SPI_SETSTICKYKEYS = 0x003B
        SPI_GETACCESSTIMEOUT = 0x003C
        SPI_SETACCESSTIMEOUT = 0x003D
        SPI_GETSERIALKEYS = 0x003E
        SPI_SETSERIALKEYS = 0x003F
        SPI_GETSOUNDSENTRY = 0x0040
        SPI_SETSOUNDSENTRY = 0x0041
        SPI_GETSNAPTODEFBUTTON = 0x005F
        SPI_SETSNAPTODEFBUTTON = 0x0060
        SPI_GETMOUSEHOVERWIDTH = 0x0062
        SPI_SETMOUSEHOVERWIDTH = 0x0063
        SPI_GETMOUSEHOVERHEIGHT = 0x0064
        SPI_SETMOUSEHOVERHEIGHT = 0x0065
        SPI_GETMOUSEHOVERTIME = 0x0066
        SPI_SETMOUSEHOVERTIME = 0x0067
        SPI_GETWHEELSCROLLLINES = 0x0068
        SPI_SETWHEELSCROLLLINES = 0x0069
        SPI_GETMENUSHOWDELAY = 0x006A
        SPI_SETMENUSHOWDELAY = 0x006B
        SPI_GETWHEELSCROLLCHARS = 0x006C
        SPI_SETWHEELSCROLLCHARS = 0x006D
        SPI_GETSHOWIMEUI = 0x006E
        SPI_SETSHOWIMEUI = 0x006F
        SPI_GETMOUSESPEED = 0x0070
        SPI_SETMOUSESPEED = 0x0071
        SPI_GETSCREENSAVERRUNNING = 0x0072
        SPI_GETDESKWALLPAPER = 0x0073
        SPI_GETAUDIODESCRIPTION = 0x0074
        SPI_SETAUDIODESCRIPTION = 0x0075
        SPI_GETSCREENSAVESECURE = 0x0076
        SPI_SETSCREENSAVESECURE = 0x0077
        SPI_GETHUNGAPPTIMEOUT = 0x0078
        SPI_SETHUNGAPPTIMEOUT = 0x0079
        SPI_GETWAITTOKILLTIMEOUT = 0x007A
        SPI_SETWAITTOKILLTIMEOUT = 0x007B
        SPI_GETWAITTOKILLSERVICETIMEOUT = 0x007C
        SPI_SETWAITTOKILLSERVICETIMEOUT = 0x007D
        SPI_GETMOUSEDOCKTHRESHOLD = 0x007E
        SPI_SETMOUSEDOCKTHRESHOLD = 0x007F
        SPI_GETPENDOCKTHRESHOLD = 0x0080
        SPI_SETPENDOCKTHRESHOLD = 0x0081
        SPI_GETWINARRANGING = 0x0082
        SPI_SETWINARRANGING = 0x0083
        SPI_GETMOUSEDRAGOUTTHRESHOLD = 0x0084
        SPI_SETMOUSEDRAGOUTTHRESHOLD = 0x0085
        SPI_GETPENDRAGOUTTHRESHOLD = 0x0086
        SPI_SETPENDRAGOUTTHRESHOLD = 0x0087
        SPI_GETMOUSESIDEMOVETHRESHOLD = 0x0088
        SPI_SETMOUSESIDEMOVETHRESHOLD = 0x0089
        SPI_GETPENSIDEMOVETHRESHOLD = 0x008A
        SPI_SETPENSIDEMOVETHRESHOLD = 0x008B
        SPI_GETDRAGFROMMAXIMIZE = 0x008C
        SPI_SETDRAGFROMMAXIMIZE = 0x008D
        SPI_GETSNAPSIZING = 0x008E
        SPI_SETSNAPSIZING = 0x008F
        SPI_GETDOCKMOVING = 0x0090
        SPI_SETDOCKMOVING = 0x0091
        MAX_TOUCH_PREDICTION_FILTER_TAPS = 3

        # REGION *** Desktop Family ***

        class TouchPredictionParameters(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("dwLatency", UINT),       # Latency in millisecs
                ("dwSampleTime", UINT),    # Sample time in millisecs (used to deduce velocity)
                ("bUseHWTimeStamp", UINT), # Use H/W TimeStamps
            ]
        TOUCHPREDICTIONPARAMETERS = TouchPredictionParameters
        PTOUCHPREDICTIONPARAMETERS = POINTER(TOUCHPREDICTIONPARAMETERS)

        TOUCHPREDICTIONPARAMETERS_DEFAULT_LATENCY = 8
        TOUCHPREDICTIONPARAMETERS_DEFAULT_SAMPLETIME = 8
        TOUCHPREDICTIONPARAMETERS_DEFAULT_USE_HW_TIMESTAMP = 1
        TOUCHPREDICTIONPARAMETERS_DEFAULT_RLS_DELTA = 0.001
        TOUCHPREDICTIONPARAMETERS_DEFAULT_RLS_LAMBDA_MIN = 0.9
        TOUCHPREDICTIONPARAMETERS_DEFAULT_RLS_LAMBDA_MAX = 0.999
        TOUCHPREDICTIONPARAMETERS_DEFAULT_RLS_LAMBDA_LEARNING_RATE = 0.001
        TOUCHPREDICTIONPARAMETERS_DEFAULT_RLS_EXPO_SMOOTH_ALPHA = 0.99
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        SPI_GETTOUCHPREDICTIONPARAMETERS = 0x009C
        SPI_SETTOUCHPREDICTIONPARAMETERS = 0x009D
        MAX_LOGICALDPIOVERRIDE = 2
        MIN_LOGICALDPIOVERRIDE = -2
        SPI_GETLOGICALDPIOVERRIDE = 0x009E
        SPI_SETLOGICALDPIOVERRIDE = 0x009F
        SPI_GETMENURECT = 0x00A2
        SPI_SETMENURECT = 0x00A3
        # WINVER >= 0x0602
        SPI_GETACTIVEWINDOWTRACKING = 0x1000
        SPI_SETACTIVEWINDOWTRACKING = 0x1001
        SPI_GETMENUANIMATION = 0x1002
        SPI_SETMENUANIMATION = 0x1003
        SPI_GETCOMBOBOXANIMATION = 0x1004
        SPI_SETCOMBOBOXANIMATION = 0x1005
        SPI_GETLISTBOXSMOOTHSCROLLING = 0x1006
        SPI_SETLISTBOXSMOOTHSCROLLING = 0x1007
        SPI_GETGRADIENTCAPTIONS = 0x1008
        SPI_SETGRADIENTCAPTIONS = 0x1009
        SPI_GETKEYBOARDCUES = 0x100A
        SPI_SETKEYBOARDCUES = 0x100B
        SPI_GETMENUUNDERLINES = SPI_GETKEYBOARDCUES
        SPI_SETMENUUNDERLINES = SPI_SETKEYBOARDCUES
        SPI_GETACTIVEWNDTRKZORDER = 0x100C
        SPI_SETACTIVEWNDTRKZORDER = 0x100D
        SPI_GETHOTTRACKING = 0x100E
        SPI_SETHOTTRACKING = 0x100F
        SPI_GETMENUFADE = 0x1012
        SPI_SETMENUFADE = 0x1013
        SPI_GETSELECTIONFADE = 0x1014
        SPI_SETSELECTIONFADE = 0x1015
        SPI_GETTOOLTIPANIMATION = 0x1016
        SPI_SETTOOLTIPANIMATION = 0x1017
        SPI_GETTOOLTIPFADE = 0x1018
        SPI_SETTOOLTIPFADE = 0x1019
        SPI_GETCURSORSHADOW = 0x101A
        SPI_SETCURSORSHADOW = 0x101B
        SPI_GETMOUSESONAR = 0x101C
        SPI_SETMOUSESONAR = 0x101D
        SPI_GETMOUSECLICKLOCK = 0x101E
        SPI_SETMOUSECLICKLOCK = 0x101F
        SPI_GETMOUSEVANISH = 0x1020
        SPI_SETMOUSEVANISH = 0x1021
        SPI_GETFLATMENU = 0x1022
        SPI_SETFLATMENU = 0x1023
        SPI_GETDROPSHADOW = 0x1024
        SPI_SETDROPSHADOW = 0x1025
        SPI_GETBLOCKSENDINPUTRESETS = 0x1026
        SPI_SETBLOCKSENDINPUTRESETS = 0x1027
        SPI_GETUIEFFECTS = 0x103E
        SPI_SETUIEFFECTS = 0x103F
        SPI_GETDISABLEOVERLAPPEDCONTENT = 0x1040
        SPI_SETDISABLEOVERLAPPEDCONTENT = 0x1041
        SPI_GETCLIENTAREAANIMATION = 0x1042
        SPI_SETCLIENTAREAANIMATION = 0x1043
        SPI_GETCLEARTYPE = 0x1048
        SPI_SETCLEARTYPE = 0x1049
        SPI_GETSPEECHRECOGNITION = 0x104A
        SPI_SETSPEECHRECOGNITION = 0x104B
        SPI_GETCARETBROWSING = 0x104C
        SPI_SETCARETBROWSING = 0x104D
        SPI_GETTHREADLOCALINPUTSETTINGS = 0x104E
        SPI_SETTHREADLOCALINPUTSETTINGS = 0x104F
        SPI_GETSYSTEMLANGUAGEBAR = 0x1050
        SPI_SETSYSTEMLANGUAGEBAR = 0x1051
        SPI_GETFOREGROUNDLOCKTIMEOUT = 0x2000
        SPI_SETFOREGROUNDLOCKTIMEOUT = 0x2001
        SPI_GETACTIVEWNDTRKTIMEOUT = 0x2002
        SPI_SETACTIVEWNDTRKTIMEOUT = 0x2003
        SPI_GETFOREGROUNDFLASHCOUNT = 0x2004
        SPI_SETFOREGROUNDFLASHCOUNT = 0x2005
        SPI_GETCARETWIDTH = 0x2006
        SPI_SETCARETWIDTH = 0x2007
        SPI_GETMOUSECLICKLOCKTIME = 0x2008
        SPI_SETMOUSECLICKLOCKTIME = 0x2009
        SPI_GETFONTSMOOTHINGTYPE = 0x200A
        SPI_SETFONTSMOOTHINGTYPE = 0x200B
        # constants for SPI_GETFONTSMOOTHINGTYPE and SPI_SETFONTSMOOTHINGTYPE:
        FE_FONTSMOOTHINGSTANDARD = 0x0001
        FE_FONTSMOOTHINGCLEARTYPE = 0x0002
        SPI_GETFONTSMOOTHINGCONTRAST = 0x200C
        SPI_SETFONTSMOOTHINGCONTRAST = 0x200D
        SPI_GETFOCUSBORDERWIDTH = 0x200E
        SPI_SETFOCUSBORDERWIDTH = 0x200F
        SPI_GETFOCUSBORDERHEIGHT = 0x2010
        SPI_SETFOCUSBORDERHEIGHT = 0x2011
        SPI_GETFONTSMOOTHINGORIENTATION = 0x2012
        SPI_SETFONTSMOOTHINGORIENTATION = 0x2013
        # constants for SPI_GETFONTSMOOTHINGORIENTATION and SPI_SETFONTSMOOTHINGORIENTATION:
        FE_FONTSMOOTHINGORIENTATIONBGR = 0x0000
        FE_FONTSMOOTHINGORIENTATIONRGB = 0x0001
        SPI_GETMINIMUMHITRADIUS = 0x2014
        SPI_SETMINIMUMHITRADIUS = 0x2015
        SPI_GETMESSAGEDURATION = 0x2016
        SPI_SETMESSAGEDURATION = 0x2017
        SPI_GETCONTACTVISUALIZATION = 0x2018
        SPI_SETCONTACTVISUALIZATION = 0x2019
        # constants for SPI_GETCONTACTVISUALIZATION and SPI_SETCONTACTVISUALIZATION
        CONTACTVISUALIZATION_OFF = 0x0000
        CONTACTVISUALIZATION_ON = 0x0001
        CONTACTVISUALIZATION_PRESENTATIONMODE = 0x0002
        SPI_GETGESTUREVISUALIZATION = 0x201A
        SPI_SETGESTUREVISUALIZATION = 0x201B
        # constants for SPI_GETGESTUREVISUALIZATION and SPI_SETGESTUREVISUALIZATION
        GESTUREVISUALIZATION_OFF = 0x0000
        GESTUREVISUALIZATION_ON = 0x001F
        GESTUREVISUALIZATION_TAP = 0x0001
        GESTUREVISUALIZATION_DOUBLETAP = 0x0002
        GESTUREVISUALIZATION_PRESSANDTAP = 0x0004
        GESTUREVISUALIZATION_PRESSANDHOLD = 0x0008
        GESTUREVISUALIZATION_RIGHTTAP = 0x0010
        SPI_GETMOUSEWHEELROUTING = 0x201C
        SPI_SETMOUSEWHEELROUTING = 0x201D
        MOUSEWHEEL_ROUTING_FOCUS = 0
        MOUSEWHEEL_ROUTING_HYBRID = 1
        MOUSEWHEEL_ROUTING_MOUSE_POS = 2
        SPI_GETPENVISUALIZATION = 0x201E
        SPI_SETPENVISUALIZATION = 0x201F
        # constants for SPI_{GET|SET}PENVISUALIZATION
        PENVISUALIZATION_ON = 0x0023
        PENVISUALIZATION_OFF = 0x0000
        PENVISUALIZATION_TAP = 0x0001
        PENVISUALIZATION_DOUBLETAP = 0x0002
        PENVISUALIZATION_CURSOR = 0x0020
        SPI_GETPENARBITRATIONTYPE = 0x2020
        SPI_SETPENARBITRATIONTYPE = 0x2021
        # constants for SPI_{GET|SET}PENARBITRATIONTYPE
        PENARBITRATIONTYPE_NONE = 0x0000
        PENARBITRATIONTYPE_WIN8 = 0x0001
        PENARBITRATIONTYPE_FIS = 0x0002
        PENARBITRATIONTYPE_SPT = 0x0003
        PENARBITRATIONTYPE_MAX = 0x0004
        SPI_GETCARETTIMEOUT = 0x2022
        SPI_SETCARETTIMEOUT = 0x2023
        SPI_GETHANDEDNESS = 0x2024
        SPI_SETHANDEDNESS = 0x2025

        HANDEDNESS = INT
        if True:
            HANDEDNESS_LEFT = 0
            HANDEDNESS_RIGHT = 1
        PHANDEDNESS = HANDEDNESS

        """
        * Flags
        """
        SPIF_UPDATEINIFILE = 0x0001
        SPIF_SENDWININICHANGE = 0x0002
        SPIF_SENDCHANGE = SPIF_SENDWININICHANGE


        METRICS_USEDEFAULT = -1

        if cpreproc.ifndef("_WINGDI_"):
            cpreproc.define("NOGDI")

            from .wingdi import LOGFONTA, LOGFONTW

            # REGION *** Desktop Family ***

            _NONCLIENTMETRICSA_fields_ = [
                    ("cbSize", UINT),
                    ("iBorderWidth", INT),
                    ("iScrollWidth", INT),
                    ("iScrollHeight", INT),
                    ("iCaptionWidth", INT),
                    ("iCaptionHeight", INT),
                    ("lfCaptionFont", LOGFONTA),
                    ("iSmCaptionWidth", INT),
                    ("iSmCaptionHeight", INT),
                    ("lfSmCaptionFont", LOGFONTA),
                    ("iMenuWidth", INT),
                    ("iMenuHeight", INT),
                    ("lfMenuFont", LOGFONTA),
                    ("lfStatusFont", LOGFONTA),
                    ("lfMessageFont", LOGFONTA)
                ]
            if cpreproc.getdef("_WINVER") > 0x0600:
                _NONCLIENTMETRICSA_fields_.append(("iPaddedBorderWidth", INT))

            class NONCLIENTMETRICSA(CStructure):
                _fields_ = _NONCLIENTMETRICSA_fields_
            PNONCLIENTMETRICSA = POINTER(NONCLIENTMETRICSA)
            LPNONCLIENTMETRICSA = PNONCLIENTMETRICSA

            _NONCLIENTMETRICSW_fields_ = [
                    ("cbSize", UINT),
                    ("iBorderWidth", INT),
                    ("iScrollWidth", INT),
                    ("iScrollHeight", INT),
                    ("iCaptionWidth", INT),
                    ("iCaptionHeight", INT),
                    ("lfCaptionFont", LOGFONTW),
                    ("iSmCaptionWidth", INT),
                    ("iSmCaptionHeight", INT),
                    ("lfSmCaptionFont", LOGFONTW),
                    ("iMenuWidth", INT),
                    ("iMenuHeight", INT),
                    ("lfMenuFont", LOGFONTW),
                    ("lfStatusFont", LOGFONTW),
                    ("lfMessageFont", LOGFONTW)
                ]
            if cpreproc.getdef("_WINVER") > 0x0600:
                _NONCLIENTMETRICSW_fields_.append(("iPaddedBorderWidth", INT))

            class NONCLIENTMETRICSW(CStructure):
                _fields_ = _NONCLIENTMETRICSW_fields_
            PNONCLIENTMETRICSW = POINTER(NONCLIENTMETRICSW)
            LPNONCLIENTMETRICSW = PNONCLIENTMETRICSW
            NONCLIENTMETRICS = unicode(NONCLIENTMETRICSW, NONCLIENTMETRICSA)
            PNONCLIENTMETRICS = unicode(PNONCLIENTMETRICSW, PNONCLIENTMETRICSA)
            LPNONCLIENTMETRICS = PNONCLIENTMETRICS

            # REGION ***
        # NOGDI
    # _WINGDI_
    ARW_BOTTOMLEFT = 0x0000
    ARW_BOTTOMRIGHT = 0x0001
    ARW_TOPLEFT = 0x0002
    ARW_TOPRIGHT = 0x0003
    ARW_STARTMASK = 0x0003
    ARW_STARTRIGHT = 0x0001
    ARW_STARTTOP = 0x0002
    ARW_LEFT = 0x0000
    ARW_RIGHT = 0x0000
    ARW_UP = 0x0004
    ARW_DOWN = 0x0004
    ARW_HIDE = 0x0008

    # REGION *** Desktop Family ***

    class MINIMIZEDMETRICS(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("iWidth", INT),
            ("iHorzGap", INT),
            ("iVertGap", INT),
            ("iArrange", INT)
        ]
    PMINIMIZEDMETRICS = POINTER(MINIMIZEDMETRICS)
    LPMINIMIZEDMETRICS = PMINIMIZEDMETRICS

    if cpreproc.ifdef("_WINGDI_"):
        if cpreproc.ifndef("NOGDI"):

            from .wingdi import LOGFONTA, LOGFONTW

            class ICONMETRICSA(CStructure):
                _fields_ = [
                    ("cbSize", UINT),
                    ("iHorzSpacing", INT),
                    ("iVertSpacing", INT),
                    ("iTitleWrap", INT),
                    ("lfFont", LOGFONTA)
                ]
            PICONMETRICSA = POINTER(ICONMETRICSA)
            LPICONMETRICSA = PICONMETRICSA

            class ICONMETRICSW(CStructure):
                _fields_ = [
                    ("cbSize", UINT),
                    ("iHorzSpacing", INT),
                    ("iVertSpacing", INT),
                    ("iTitleWrap", INT),
                    ("lfFont", LOGFONTW)
                ]
            PICONMETRICSW = POINTER(ICONMETRICSW)
            LPICONMETRICSW = PICONMETRICSW
            ICONMETRICS = unicode(ICONMETRICSW, ICONMETRICSA)
            PICONMETRICS = unicode(PICONMETRICSW, PICONMETRICSA)
            LPICONMETRICS = PICONMETRICS
        # NOGDI
    # _WINGDI_

    class ANIMATIONINFO(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("iMinAnimate", INT)
        ]
    LPANIMATIONINFO = POINTER(ANIMATIONINFO)

    class SERIALKEYSA(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("dwFlags", DWORD),
            ("lpszActivePort", LPSTR),
            ("lpszPort", LPSTR),
            ("iBaudRate", UINT),
            ("iPortState", UINT),
            ("iActive", UINT)
        ]
    LPSERIALKEYSA = POINTER(SERIALKEYSA)

    class SERIALKEYSW(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("dwFlags", DWORD),
            ("lpszActivePort", LPWSTR),
            ("lpszPort", LPWSTR),
            ("iBaudRate", UINT),
            ("iPortState", UINT),
            ("iActive", UINT)
        ]
    LPSERIALKEYSW = POINTER(SERIALKEYSW)
    SERIALKEYS = unicode(SERIALKEYSW, SERIALKEYSA)
    LPSERIALKEYS = unicode(LPSERIALKEYSW, LPSERIALKEYSA)

    # flags for SERIALKEYS dwFlags field
    SERKF_SERIALKEYSON = 0x00000001
    SERKF_AVAILABLE = 0x00000002
    SERKF_INDICATOR = 0x00000004


    class HIGHCONTRASTA(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("dwFlags", DWORD),
            ("lpszDefaultScheme", LPSTR)
        ]
    LPHIGHCONTRASTA = POINTER(HIGHCONTRASTA)

    class HIGHCONTRASTW(CStructure):
        _fields_ = [
            ("cbSize", UINT),
            ("dwFlags", DWORD),
            ("lpszDefaultScheme", LPWSTR)
        ]
    LPHIGHCONTRASTW = POINTER(HIGHCONTRASTW)
    HIGHCONTRAST = unicode(HIGHCONTRASTW, HIGHCONTRASTA)
    LPHIGHCONTRAST = unicode(LPHIGHCONTRASTW, LPHIGHCONTRASTA)

    # REGION ***
    
    # flags for HIGHCONTRAST dwFlags field
    HCF_HIGHCONTRASTON = 0x00000001
    HCF_AVAILABLE = 0x00000002
    HCF_HOTKEYACTIVE = 0x00000004
    HCF_CONFIRMHOTKEY = 0x00000008
    HCF_HOTKEYSOUND = 0x00000010
    HCF_INDICATOR = 0x00000020
    HCF_HOTKEYAVAILABLE = 0x00000040
    HCF_LOGONDESKTOP = 0x00000100
    HCF_DEFAULTDESKTOP = 0x00000200
    HCF_OPTION_NOTHEMECHANGE = 0x00001000
    # Flags for ChangeDisplaySettings
    CDS_UPDATEREGISTRY = 0x00000001
    CDS_TEST = 0x00000002
    CDS_FULLSCREEN = 0x00000004
    CDS_GLOBAL = 0x00000008
    CDS_SET_PRIMARY = 0x00000010
    CDS_VIDEOPARAMETERS = 0x00000020
    CDS_ENABLE_UNSAFE_MODES = 0x00000100
    CDS_DISABLE_UNSAFE_MODES = 0x00000200
    CDS_RESET = 0x40000000
    CDS_RESET_EX = 0x20000000
    CDS_NORESET = 0x10000000
    # Return values for ChangeDisplaySettings
    DISP_CHANGE_SUCCESSFUL = 0
    DISP_CHANGE_RESTART = 1
    DISP_CHANGE_FAILED = -1
    DISP_CHANGE_BADMODE = -2
    DISP_CHANGE_NOTUPDATED = -3
    DISP_CHANGE_BADFLAGS = -4
    DISP_CHANGE_BADPARAM = -5
    DISP_CHANGE_BADDUALVIEW = -6

    # REGION *** Desktop Family ***

    if cpreproc.ifdef("_WINGDI_"):
        if cpreproc.ifndef("NOGDI"):

            from .wingdi import (PDEVMODEA, PDEVMODEW, 
                                PDISPLAY_DEVICEA, PDISPLAY_DEVICEW,
                                DISPLAYCONFIG_MODE_INFO, DISPLAYCONFIG_PATH_INFO,
                                DISPLAYCONFIG_DEVICE_INFO_HEADER, DISPLAYCONFIG_TOPOLOGY_ID)

            ChangeDisplaySettingsA = declare(user32.ChangeDisplaySettingsA, LONG, PDEVMODEA, DWORD)
            ChangeDisplaySettingsW = declare(user32.ChangeDisplaySettingsW, LONG, PDEVMODEW, DWORD)
            ChangeDisplaySettings = unicode(ChangeDisplaySettingsW, ChangeDisplaySettingsA)
            ChangeDisplaySettingsExA = declare(user32.ChangeDisplaySettingsExA, LONG, LPCSTR, PDEVMODEA, HWND, DWORD, LPVOID)
            ChangeDisplaySettingsExW = declare(user32.ChangeDisplaySettingsExW, LONG, LPCWSTR, PDEVMODEW, HWND, DWORD, LPVOID)
            ChangeDisplaySettingsEx = unicode(ChangeDisplaySettingsExW, ChangeDisplaySettingsExA)
            ENUM_CURRENT_SETTINGS = DWORD(-1).value
            ENUM_REGISTRY_SETTINGS = DWORD(-2).value
            EnumDisplaySettingsA = declare(user32.EnumDisplaySettingsA, BOOL, LPCSTR, DWORD, PDEVMODEA)
            EnumDisplaySettingsW = declare(user32.EnumDisplaySettingsW, BOOL, LPCWSTR, DWORD, PDEVMODEW)
            EnumDisplaySettings = unicode(EnumDisplaySettingsW, EnumDisplaySettingsA)
            EnumDisplaySettingsExA = declare(user32.EnumDisplaySettingsExA, BOOL, LPCSTR, DWORD, PDEVMODEA, DWORD)
            EnumDisplaySettingsExW = declare(user32.EnumDisplaySettingsExW, BOOL, LPCWSTR, DWORD, PDEVMODEW, DWORD)
            EnumDisplaySettingsEx = unicode(EnumDisplaySettingsExW, EnumDisplaySettingsExA)
            # Flags for EnumDisplaySettingsEx
            EDS_RAWMODE = 0x00000002
            EDS_ROTATEDMODE = 0x00000004
            EnumDisplayDevicesA = declare(user32.EnumDisplayDevicesA, BOOL, LPCSTR, DWORD, PDISPLAY_DEVICEA, DWORD)
            EnumDisplayDevicesW = declare(user32.EnumDisplayDevicesW, BOOL, LPCWSTR, DWORD, PDISPLAY_DEVICEW, DWORD)
            EnumDisplayDevices = unicode(EnumDisplayDevicesW, EnumDisplayDevicesA)
            # !UNICODE
            # Flags for EnumDisplayDevices
            EDD_GET_DEVICE_INTERFACE_NAME = 0x00000001
            # WINVER >= 0x0500
            GetDisplayConfigBufferSizes = declare(user32.GetDisplayConfigBufferSizes, LONG, UINT32, PUINT32, PUINT32)
            SetDisplayConfig = declare(user32.SetDisplayConfig, LONG, UINT32, POINTER(DISPLAYCONFIG_PATH_INFO), UINT32, POINTER(DISPLAYCONFIG_MODE_INFO), UINT32)
            QueryDisplayConfig = declare(user32.QueryDisplayConfig, LONG, UINT32, PUINT32, POINTER(DISPLAYCONFIG_PATH_INFO), PUINT32, POINTER(DISPLAYCONFIG_MODE_INFO), POINTER(DISPLAYCONFIG_TOPOLOGY_ID))
            DisplayConfigGetDeviceInfo = declare(user32.DisplayConfigGetDeviceInfo, LONG, POINTER(DISPLAYCONFIG_DEVICE_INFO_HEADER))
            DisplayConfigSetDeviceInfo = declare(user32.DisplayConfigSetDeviceInfo, LONG, POINTER(DISPLAYCONFIG_DEVICE_INFO_HEADER))
        # NOGDI
    # _WINGDI_
    SystemParametersInfoA = declare(user32.SystemParametersInfoA, BOOL, UINT, UINT, PVOID, UINT)
    SystemParametersInfoW = declare(user32.SystemParametersInfoW, BOOL, UINT, UINT, PVOID, UINT)
    SystemParametersInfo = unicode(SystemParametersInfoW, SystemParametersInfoA)
    SystemParametersInfoForDpi = declare(user32.SystemParametersInfoForDpi, BOOL, UINT, UINT, PVOID, UINT, UINT)

    # REGION ***
# !NOSYSPARAMSINFO

# REGION *** Desktop Family ***


"""

* Accessibility support

"""

class FILTERKEYS(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD),
        ("iWaitMSec", DWORD),   # Acceptance Delay
        ("iDelayMSec", DWORD),  # Delay Until Repeat
        ("iRepeatMSec", DWORD), # Repeat Rate
        ("iBounceMSec", DWORD)  # Debounce Time
    ]
LPFILTERKEYS = POINTER(FILTERKEYS)

# REGION ***

"""

 * FILTERKEYS dwFlags field

"""

FKF_FILTERKEYSON = 0x00000001
FKF_AVAILABLE = 0x00000002
FKF_HOTKEYACTIVE = 0x00000004
FKF_CONFIRMHOTKEY = 0x00000008
FKF_HOTKEYSOUND = 0x00000010
FKF_INDICATOR = 0x00000020
FKF_CLICKON = 0x00000040

# REGION *** Desktop Family ***

class STICKYKEYS(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD)
    ]
LPSTICKYKEYS = POINTER(STICKYKEYS)

# REGION ***

"""

 * STICKYKEYS dwFlags field

"""

SKF_STICKYKEYSON = 0x00000001
SKF_AVAILABLE = 0x00000002
SKF_HOTKEYACTIVE = 0x00000004
SKF_CONFIRMHOTKEY = 0x00000008
SKF_HOTKEYSOUND = 0x00000010
SKF_INDICATOR = 0x00000020
SKF_AUDIBLEFEEDBACK = 0x00000040
SKF_TRISTATE = 0x00000080
SKF_TWOKEYSOFF = 0x00000100
SKF_LALTLATCHED = 0x10000000
SKF_LCTLLATCHED = 0x04000000
SKF_LSHIFTLATCHED = 0x01000000
SKF_RALTLATCHED = 0x20000000
SKF_RCTLLATCHED = 0x08000000
SKF_RSHIFTLATCHED = 0x02000000
SKF_LWINLATCHED = 0x40000000
SKF_RWINLATCHED = 0x80000000
SKF_LALTLOCKED = 0x00100000
SKF_LCTLLOCKED = 0x00040000
SKF_LSHIFTLOCKED = 0x00010000
SKF_RALTLOCKED = 0x00200000
SKF_RCTLLOCKED = 0x00080000
SKF_RSHIFTLOCKED = 0x00020000
SKF_LWINLOCKED = 0x00400000
SKF_RWINLOCKED = 0x00800000

# REGION *** Desktop Family ***

class MOUSEKEYS(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD),
        ("iMaxSpeed", DWORD),
        ("iTimeToMaxSpeed", DWORD),
        ("iCtrlSpeed", DWORD),
        ("dwReserved1", DWORD),
        ("dwReserved2", DWORD)
    ]
LPMOUSEKEYS = POINTER(MOUSEKEYS)

# REGION ***

"""

 * MOUSEKEYS dwFlags field

"""

MKF_MOUSEKEYSON = 0x00000001
MKF_AVAILABLE = 0x00000002
MKF_HOTKEYACTIVE = 0x00000004
MKF_CONFIRMHOTKEY = 0x00000008
MKF_HOTKEYSOUND = 0x00000010
MKF_INDICATOR = 0x00000020
MKF_MODIFIERS = 0x00000040
MKF_REPLACENUMBERS = 0x00000080
MKF_LEFTBUTTONSEL = 0x10000000
MKF_RIGHTBUTTONSEL = 0x20000000
MKF_LEFTBUTTONDOWN = 0x01000000
MKF_RIGHTBUTTONDOWN = 0x02000000
MKF_MOUSEMODE = 0x80000000

# REGION *** Desktop Family ***

class ACCESSTIMEOUT(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD),
        ("iTimeOutMSec", DWORD)
    ]
LPACCESSTIMEOUT = POINTER(ACCESSTIMEOUT)

# REGION ***

"""

 * ACCESSTIMEOUT dwFlags field

"""

ATF_TIMEOUTON = 0x00000001
ATF_ONOFFFEEDBACK = 0x00000002
# values for SOUNDSENTRY iFSGrafEffect field
SSGF_NONE = 0
SSGF_DISPLAY = 3
# values for SOUNDSENTRY iFSTextEffect field
SSTF_NONE = 0
SSTF_CHARS = 1
SSTF_BORDER = 2
SSTF_DISPLAY = 3
# values for SOUNDSENTRY iWindowsEffect field
SSWF_NONE = 0
SSWF_TITLE = 1
SSWF_WINDOW = 2
SSWF_DISPLAY = 3
SSWF_CUSTOM = 4

# REGION *** Desktop Family ***

class SOUNDSENTRYA(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD),
        ("iFSTextEffect", DWORD),
        ("iFSTextEffectMSec", DWORD),
        ("iFSTextEffectColorBits", DWORD),
        ("iFSGrafEffect", DWORD),
        ("iFSGrafEffectMSec", DWORD),
        ("iFSGrafEffectColor", DWORD),
        ("iWindowsEffect", DWORD),
        ("iWindowsEffectMSec", DWORD),
        ("lpszWindowsEffectDLL", LPSTR),
        ("iWindowsEffectOrdinal", DWORD)
    ]
LPSOUNDSENTRYA = POINTER(SOUNDSENTRYA)

class SOUNDSENTRYW(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD),
        ("iFSTextEffect", DWORD),
        ("iFSTextEffectMSec", DWORD),
        ("iFSTextEffectColorBits", DWORD),
        ("iFSGrafEffect", DWORD),
        ("iFSGrafEffectMSec", DWORD),
        ("iFSGrafEffectColor", DWORD),
        ("iWindowsEffect", DWORD),
        ("iWindowsEffectMSec", DWORD),
        ("lpszWindowsEffectDLL", LPWSTR),
        ("iWindowsEffectOrdinal", DWORD)
    ]
LPSOUNDSENTRYW = POINTER(SOUNDSENTRYW)
SOUNDSENTRY = unicode(SOUNDSENTRYW, SOUNDSENTRYA)
LPSOUNDSENTRY = unicode(LPSOUNDSENTRYW, LPSOUNDSENTRYA)

# REGION ***

"""

 * SOUNDSENTRY dwFlags field

"""

SSF_SOUNDSENTRYON = 0x00000001
SSF_AVAILABLE = 0x00000002
SSF_INDICATOR = 0x00000004

# REGION *** Desktop or PC Family ***

SoundSentry = declare(user32.SoundSentry, BOOL, VOID)

# REGION ***

class TOGGLEKEYS(CStructure):
    _fields_ = [
        ("cbSize", UINT),
        ("dwFlags", DWORD)
    ]
LPTOGGLEKEYS = POINTER(TOGGLEKEYS)

# REGION ***

"""

 * TOGGLEKEYS dwFlags field

"""

TKF_TOGGLEKEYSON = 0x00000001
TKF_AVAILABLE = 0x00000002
TKF_HOTKEYACTIVE = 0x00000004
TKF_CONFIRMHOTKEY = 0x00000008
TKF_HOTKEYSOUND = 0x00000010
TKF_INDICATOR = 0x00000020

# REGION *** Desktop Family ***

class AUDIODESCRIPTION(CStructure):
    _fields_ = [
        ("cbSize", UINT),  # sizeof(AudioDescriptionType)
        ("Enabled", BOOL), # On/Off
        ("Locale", LCID),  # locale ID for language
    ]
LPAUDIODESCRIPTION = POINTER(AUDIODESCRIPTION)

"""

 * Set debug level

"""

SetDebugErrorLevel = declare(user32.SetDebugErrorLevel, VOID, DWORD)
# WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

# REGION ***

"""

 * SetLastErrorEx() types.

"""

SLE_ERROR = 0x00000001
SLE_MINORERROR = 0x00000002
SLE_WARNING = 0x00000003

# REGION *** Desktop Family ***

SetLastErrorEx = declare(user32.SetLastErrorEx, VOID, DWORD, DWORD)
InternalGetWindowText = declare(user32.InternalGetWindowText, INT, HWND, LPWSTR, INT)
EndTask = declare(user32.EndTask, BOOL, HWND, BOOL, BOOL)
CancelShutdown = declare(user32.CancelShutdown, BOOL, VOID)

# REGION ***

"""

 * Multimonitor API.

"""

MONITOR_DEFAULTTONULL = 0x00000000
MONITOR_DEFAULTTOPRIMARY = 0x00000001
MONITOR_DEFAULTTONEAREST = 0x00000002

# REGION *** Desktop Family ***

MonitorFromPoint = declare(user32.MonitorFromPoint, HMONITOR, POINT, DWORD)
MonitorFromRect = declare(user32.MonitorFromRect, HMONITOR, LPRECT, DWORD)
MonitorFromWindow = declare(user32.MonitorFromWindow, HMONITOR, HWND, DWORD)

# REGION ***
MONITORINFOF_PRIMARY = 0x00000001
if cpreproc.ifndef("CCHDEVICENAME"):
    CCHDEVICENAME = 32

    # REGION *** Desktop Family ***
    
    class MONITORINFO(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("rcMonitor", RECT),
            ("rcWork", RECT),
            ("dwFlags", DWORD)
        ]
    LPMONITORINFO = POINTER(MONITORINFO)

    class MONITORINFOEXA(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("rcMonitor", RECT),
            ("rcWork", RECT),
            ("dwFlags", DWORD),
            ("szDevice", CHAR * CCHDEVICENAME)
        ]
    LPMONITORINFOEXA = POINTER(MONITORINFOEXA)

    class MONITORINFOEXW(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("rcMonitor", RECT),
            ("rcWork", RECT),
            ("dwFlags", DWORD),
            ("szDevice", WCHAR * CCHDEVICENAME)
        ]
    LPMONITORINFOEXW = POINTER(MONITORINFOEXW)

    GetMonitorInfoA = declare(user32.GetMonitorInfoA, BOOL, HMONITOR, LPMONITORINFO)
    GetMonitorInfoW = declare(user32.GetMonitorInfoW, BOOL, HMONITOR, LPMONITORINFO)
    GetMonitorInfo = unicode(GetMonitorInfoW, GetMonitorInfoA)
    # !UNICODE
    MONITORENUMPROC = CALLBACK(BOOL, HMONITOR, HDC, LPRECT, LPARAM)

    EnumDisplayMonitors = declare(user32.EnumDisplayMonitors, BOOL, HDC, LPRECT, MONITORENUMPROC, LPARAM)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

    # REGION ***
    if cpreproc.ifndef("NOWINABLE"):

        # REGION *** Desktop Family ***


        """

        * WinEvents - Active Accessibility hooks

        """

        NotifyWinEvent = declare(user32.NotifyWinEvent, VOID, DWORD, HWND, LONG, LONG)

        WINEVENTPROC = CALLBACK(VOID, HWINEVENTHOOK, DWORD, HWND, LONG, LONG, DWORD, DWORD)

        SetWinEventHook = declare(user32.SetWinEventHook, HWINEVENTHOOK, DWORD, DWORD, HMODULE, WINEVENTPROC, DWORD, DWORD, DWORD)
        IsWinEventHookInstalled = declare(user32.IsWinEventHookInstalled, BOOL, DWORD)

        # REGION ***

        """

        * dwFlags for SetWinEventHook

        """

        WINEVENT_OUTOFCONTEXT = 0x0000 # Events are ASYNC
        WINEVENT_SKIPOWNTHREAD = 0x0001 # Don't call back for events on installer's thread
        WINEVENT_SKIPOWNPROCESS = 0x0002 # Don't call back for events on installer's process
        WINEVENT_INCONTEXT = 0x0004 # Events are SYNC, this causes your dll to be injected into every process

        # REGION *** Desktop Family ***

        UnhookWinEvent = declare(user32.UnhookWinEvent, BOOL, HWINEVENTHOOK)

        # REGION ***

        """

        * idObject values for WinEventProc and NotifyWinEvent

        """


        """

        * hwnd + idObject can be used with OLEACC.DLL's OleGetObjectFromWindow()
        * to get an interface pointer to the container.  indexChild is the item
        * within the container in question.  Setup a VARIANT with vt VT_I4 and
        * lVal the indexChild and pass that in to all methods.  Then you
        * are raring to go.

        """


        """

        * Common object IDs (cookies, only for sending WM_GETOBJECT to get at the
        * thing in question).  Positive IDs are reserved for apps (app specific),
        * negative IDs are system things and are global, 0 means "just little old
        * me".

        """

        CHILDID_SELF = 0
        INDEXID_OBJECT = 0
        INDEXID_CONTAINER = 0

        """

        * Reserved IDs for system objects

        """

        OBJID_WINDOW = LONG(0x00000000).value
        OBJID_SYSMENU = LONG(0xFFFFFFFF).value
        OBJID_TITLEBAR = LONG(0xFFFFFFFE).value
        OBJID_MENU = LONG(0xFFFFFFFD).value
        OBJID_CLIENT = LONG(0xFFFFFFFC).value
        OBJID_VSCROLL = LONG(0xFFFFFFFB).value
        OBJID_HSCROLL = LONG(0xFFFFFFFA).value
        OBJID_SIZEGRIP = LONG(0xFFFFFFF9).value
        OBJID_CARET = LONG(0xFFFFFFF8).value
        OBJID_CURSOR = LONG(0xFFFFFFF7).value
        OBJID_ALERT = LONG(0xFFFFFFF6).value
        OBJID_SOUND = LONG(0xFFFFFFF5).value
        OBJID_QUERYCLASSNAMEIDX = LONG(0xFFFFFFF4).value
        OBJID_NATIVEOM = LONG(0xFFFFFFF0).value

        """

        * EVENT DEFINITION

        """

        EVENT_MIN = 0x00000001
        EVENT_MAX = 0x7FFFFFFF

        """

        *  EVENT_SYSTEM_SOUND
        *  Sent when a sound is played.  Currently nothing is generating this, we
        *  this event when a system sound (for menus, etc) is played.  Apps
        *  generate this, if accessible, when a private sound is played.  For
        *  example, if Mail plays a "New Mail" sound.
        *
        *  System Sounds:
        *  (Generated by PlaySoundEvent in USER itself)
        *      hwnd            is NULL
        *      idObject        is OBJID_SOUND
        *      idChild         is sound child ID if one
        *  App Sounds:
        *  (PlaySoundEvent won't generate notification; up to app)
        *      hwnd + idObject gets interface pointer to Sound object
        *      idChild identifies the sound in question
        *  are going to be cleaning up the SOUNDSENTRY feature in the control panel
        *  and will use this at that time.  Applications implementing WinEvents
        *  are perfectly welcome to use it.  Clients of IAccessible* will simply
        *  turn around and get back a non-visual object that describes the sound.

        """

        EVENT_SYSTEM_SOUND = 0x0001

        """

        * EVENT_SYSTEM_ALERT
        * System Alerts:
        * (Generated by MessageBox() calls for example)
        *      hwnd            is hwndMessageBox
        *      idObject        is OBJID_ALERT
        * App Alerts:
        * (Generated whenever)
        *      hwnd+idObject gets interface pointer to Alert

        """

        EVENT_SYSTEM_ALERT = 0x0002

        """

        * EVENT_SYSTEM_FOREGROUND
        * Sent when the foreground (active) window changes, even if it is changing
        * to another window in the same thread as the previous one.
        *      hwnd            is hwndNewForeground
        *      idObject        is OBJID_WINDOW
        *      idChild    is INDEXID_OBJECT

        """

        EVENT_SYSTEM_FOREGROUND = 0x0003

        """

        * Menu
        *      hwnd            is window (top level window or popup menu window)
        *      idObject        is ID of control (OBJID_MENU, OBJID_SYSMENU, OBJID_SELF for popup)
        *      idChild         is CHILDID_SELF
        *
        * EVENT_SYSTEM_MENUSTART
        * EVENT_SYSTEM_MENUEND
        * For MENUSTART, hwnd+idObject+idChild refers to the control with the menu bar,
        *  or the control bringing up the context menu.
        *
        * Sent when entering into and leaving from menu mode (system, app bar, and
        * track popups).

        """

        EVENT_SYSTEM_MENUSTART = 0x0004
        EVENT_SYSTEM_MENUEND = 0x0005

        """

        * EVENT_SYSTEM_MENUPOPUPSTART
        * EVENT_SYSTEM_MENUPOPUPEND
        * Sent when a menu popup comes up and just before it is taken down.  Note
        * that for a call to TrackPopupMenu(), a client will see EVENT_SYSTEM_MENUSTART
        * followed almost immediately by EVENT_SYSTEM_MENUPOPUPSTART for the popup
        * being shown.
        *
        * For MENUPOPUP, hwnd+idObject+idChild refers to the NEW popup coming up, not the
        * parent item which is hierarchical.  You can get the parent menu/popup by
        * asking for the accParent object.

        """

        EVENT_SYSTEM_MENUPOPUPSTART = 0x0006
        EVENT_SYSTEM_MENUPOPUPEND = 0x0007

        """

        * EVENT_SYSTEM_CAPTURESTART
        * EVENT_SYSTEM_CAPTUREEND
        * Sent when a window takes the capture and releases the capture.

        """

        EVENT_SYSTEM_CAPTURESTART = 0x0008
        EVENT_SYSTEM_CAPTUREEND = 0x0009

        """

        * Move Size
        * EVENT_SYSTEM_MOVESIZESTART
        * EVENT_SYSTEM_MOVESIZEEND
        * Sent when a window enters and leaves move-size dragging mode.

        """

        EVENT_SYSTEM_MOVESIZESTART = 0x000A
        EVENT_SYSTEM_MOVESIZEEND = 0x000B

        """

        * Context Help
        * EVENT_SYSTEM_CONTEXTHELPSTART
        * EVENT_SYSTEM_CONTEXTHELPEND
        * Sent when a window enters and leaves context sensitive help mode.

        """

        EVENT_SYSTEM_CONTEXTHELPSTART = 0x000C
        EVENT_SYSTEM_CONTEXTHELPEND = 0x000D

        """

        * Drag & Drop
        * EVENT_SYSTEM_DRAGDROPSTART
        * EVENT_SYSTEM_DRAGDROPEND
        * Send the START notification just before going into drag&drop loop.  Send
        * the END notification just after canceling out.
        * Note that it is up to apps and OLE to generate this, since the system
        * doesn't know.  Like EVENT_SYSTEM_SOUND, it will be a while before this
        * is prevalent.

        """

        EVENT_SYSTEM_DRAGDROPSTART = 0x000E
        EVENT_SYSTEM_DRAGDROPEND = 0x000F

        """

        * Dialog
        * Send the START notification right after the dialog is completely
        *  initialized and visible.  Send the END right before the dialog
        *  is hidden and goes away.
        * EVENT_SYSTEM_DIALOGSTART
        * EVENT_SYSTEM_DIALOGEND

        """

        EVENT_SYSTEM_DIALOGSTART = 0x0010
        EVENT_SYSTEM_DIALOGEND = 0x0011

        """

        * EVENT_SYSTEM_SCROLLING
        * EVENT_SYSTEM_SCROLLINGSTART
        * EVENT_SYSTEM_SCROLLINGEND
        * Sent when beginning and ending the tracking of a scrollbar in a window,
        * and also for scrollbar controls.

        """

        EVENT_SYSTEM_SCROLLINGSTART = 0x0012
        EVENT_SYSTEM_SCROLLINGEND = 0x0013

        """

        * Alt-Tab Window
        * Send the START notification right after the switch window is initialized
        * and visible.  Send the END right before it is hidden and goes away.
        * EVENT_SYSTEM_SWITCHSTART
        * EVENT_SYSTEM_SWITCHEND

        """

        EVENT_SYSTEM_SWITCHSTART = 0x0014
        EVENT_SYSTEM_SWITCHEND = 0x0015

        """

        * EVENT_SYSTEM_MINIMIZESTART
        * EVENT_SYSTEM_MINIMIZEEND
        * Sent when a window minimizes and just before it restores.

        """

        EVENT_SYSTEM_MINIMIZESTART = 0x0016
        EVENT_SYSTEM_MINIMIZEEND = 0x0017
        EVENT_SYSTEM_DESKTOPSWITCH = 0x0020
        # AppGrabbed: HWND = hwnd of app thumbnail, objectID = 0, childID = 0
        EVENT_SYSTEM_SWITCHER_APPGRABBED = 0x0024
        # OverTarget: HWND = hwnd of app thumbnail, objectID =
        #            1 for center
        #            2 for near snapped
        #            3 for far snapped
        #            4 for prune
        #            childID = 0
        EVENT_SYSTEM_SWITCHER_APPOVERTARGET = 0x0025
        # Dropped: HWND = hwnd of app thumbnail, objectID = <same as above>, childID = 0
        EVENT_SYSTEM_SWITCHER_APPDROPPED = 0x0026
        # Cancelled: HWND = hwnd of app thumbnail, objectID = 0, childID = 0
        EVENT_SYSTEM_SWITCHER_CANCELLED = 0x0027

        """

        * Sent when an IME's soft key is pressed and should be echoed,
        * but is not passed through the keyboard hook.
        * Must not be sent when a key is sent through the keyboard hook.
        *     HWND             is the hwnd of the UI containing the soft key
        *     idChild          is the Unicode value of the character entered
        *     idObject         is a bitfield
        *         0x00000001: set if a 32-bit Unicode surrogate pair is used

        """

        EVENT_SYSTEM_IME_KEY_NOTIFICATION = 0x0029
        EVENT_SYSTEM_END = 0x00FF
        EVENT_OEM_DEFINED_START = 0x0101
        EVENT_OEM_DEFINED_END = 0x01FF
        EVENT_UIA_EVENTID_START = 0x4E00
        EVENT_UIA_EVENTID_END = 0x4EFF
        EVENT_UIA_PROPID_START = 0x7500
        EVENT_UIA_PROPID_END = 0x75FF
        EVENT_CONSOLE_CARET = 0x4001
        EVENT_CONSOLE_UPDATE_REGION = 0x4002
        EVENT_CONSOLE_UPDATE_SIMPLE = 0x4003
        EVENT_CONSOLE_UPDATE_SCROLL = 0x4004
        EVENT_CONSOLE_LAYOUT = 0x4005
        EVENT_CONSOLE_START_APPLICATION = 0x4006
        EVENT_CONSOLE_END_APPLICATION = 0x4007

        """

        * Flags for EVENT_CONSOLE_START/END_APPLICATION.

        """

        CONSOLE_APPLICATION_16BIT = 0x0000
        CONSOLE_APPLICATION_16BIT = 0x0001

        """

        * Flags for EVENT_CONSOLE_CARET

        """

        CONSOLE_CARET_SELECTION = 0x0001
        CONSOLE_CARET_VISIBLE = 0x0002
        EVENT_CONSOLE_END = 0x40FF

        """

        * Object events
        *
        * The system AND apps generate these.  The system generates these for
        * real windows.  Apps generate these for objects within their window which
        * act like a separate control, e.g. an item in a list view.
        *
        * When the system generate them, dwParam2 is always WMOBJID_SELF.  When
        * apps generate them, apps put the has-meaning-to-the-app-only ID value
        * in dwParam2.
        * For all events, if you want detailed accessibility information, callers
        * should
        *      * Call AccessibleObjectFromWindow() with the hwnd, idObject parameters
        *          of the event, and IID_IAccessible as the REFIID, to get back an
        *          IAccessible* to talk to
        *      * Initialize and fill in a VARIANT as VT_I4 with lVal the idChild
        *          parameter of the event.
        *      * If idChild isn't zero, call get_accChild() in the container to see
        *          if the child is an object in its own right.  If so, you will get
        *          back an IDispatch* object for the child.  You should release the
        *          parent, and call QueryInterface() on the child object to get its
        *          IAccessible*.  Then you talk directly to the child.  Otherwise,
        *          if get_accChild() returns you nothing, you should continue to
        *          use the child VARIANT.  You will ask the container for the properties
        *          of the child identified by the VARIANT.  In other words, the
        *          child in this case is accessible but not a full-blown object.
        *          Like a button on a titlebar which is 'small' and has no children.

        """


        """

        * For all EVENT_OBJECT events,
        *      hwnd is the dude to Send the WM_GETOBJECT message to (unless NULL,
        *          see above for system things)
        *      idObject is the ID of the object that can resolve any queries a
        *          client might have.  It's a way to deal with windowless controls,
        *          controls that are just drawn on the screen in some larger parent
        *          window (like SDM), or standard frame elements of a window.
        *      idChild is the piece inside of the object that is affected.  This
        *          allows clients to access things that are too small to have full
        *          blown objects in their own right.  Like the thumb of a scrollbar.
        *          The hwnd/idObject pair gets you to the container, the dude you
        *          probably want to talk to most of the time anyway.  The idChild
        *          can then be passed into the acc properties to get the name/value
        *          of it as needed.
        *
        * Example #1:
        *      System propagating a listbox selection change
        *      EVENT_OBJECT_SELECTION
        *          hwnd == listbox hwnd
        *          idObject == OBJID_WINDOW
        *          idChild == new selected item, or CHILDID_SELF if
        *              nothing now selected within container.
        *      Word '97 propagating a listbox selection change
        *          hwnd == SDM window
        *          idObject == SDM ID to get at listbox 'control'
        *          idChild == new selected item, or CHILDID_SELF if
        *              nothing
        *
        * Example #2:
        *      System propagating a menu item selection on the menu bar
        *      EVENT_OBJECT_SELECTION
        *          hwnd == top level window
        *          idObject == OBJID_MENU
        *          idChild == ID of child menu bar item selected
        *
        * Example #3:
        *      System propagating a dropdown coming off of said menu bar item
        *      EVENT_OBJECT_CREATE
        *          hwnd == popup item
        *          idObject == OBJID_WINDOW
        *          idChild == CHILDID_SELF
        *
        * Example #4:
        *
        * For EVENT_OBJECT_REORDER, the object referred to by hwnd/idObject is the
        * PARENT container in which the zorder is occurring.  This is because if
        * one child is zordering, all of them are changing their relative zorder.

        """

        EVENT_OBJECT_CREATE = 0x8000 # hwnd + ID + idChild is created item
        EVENT_OBJECT_DESTROY = 0x8001 # hwnd + ID + idChild is destroyed item
        EVENT_OBJECT_SHOW = 0x8002 # hwnd + ID + idChild is shown item
        EVENT_OBJECT_HIDE = 0x8003 # hwnd + ID + idChild is hidden item
        EVENT_OBJECT_REORDER = 0x8004 # hwnd + ID + idChild is parent of zordering children

        """

        * NOTE:
        * Minimize the number of notifications!
        *
        * When you are hiding a parent object, obviously all child objects are no
        * longer visible on screen.  They still have the same "visible" status,
        * but are not truly visible.  Hence do not send HIDE notifications for the
        * children also.  One implies all.  The same goes for SHOW.

        """

        EVENT_OBJECT_FOCUS = 0x8005 # hwnd + ID + idChild is focused item
        EVENT_OBJECT_SELECTION = 0x8006 # hwnd + ID + idChild is selected item (if only one), or idChild is OBJID_WINDOW if complex
        EVENT_OBJECT_SELECTIONADD = 0x8007 # hwnd + ID + idChild is item added
        EVENT_OBJECT_SELECTIONREMOVE = 0x8008 # hwnd + ID + idChild is item removed
        EVENT_OBJECT_SELECTIONWITHIN = 0x8009 # hwnd + ID + idChild is parent of changed selected items

        """

        * NOTES:
        * There is only one "focused" child item in a parent.  This is the place
        * keystrokes are going at a given moment.  Hence only send a notification
        * about where the NEW focus is going.  A NEW item getting the focus already
        * implies that the OLD item is losing it.
        *
        * SELECTION however can be multiple.  Hence the different SELECTION
        * notifications.  Here's when to use each:
        *
        * (1) Send a SELECTION notification in the simple single selection
        *     case (like the focus) when the item with the selection is
        *     merely moving to a different item within a container.  hwnd + ID
        *     is the container control, idChildItem is the new child with the
        *     selection.
        *
        * (2) Send a SELECTIONADD notification when a new item has simply been added
        *     to the selection within a container.  This is appropriate when the
        *     number of newly selected items is very small.  hwnd + ID is the
        *     container control, idChildItem is the new child added to the selection.
        *
        * (3) Send a SELECTIONREMOVE notification when a new item has simply been
        *     removed from the selection within a container.  This is appropriate
        *     when the number of newly selected items is very small, just like
        *     SELECTIONADD.  hwnd + ID is the container control, idChildItem is the
        *     new child removed from the selection.
        *
        * (4) Send a SELECTIONWITHIN notification when the selected items within a
        *     control have changed substantially.  Rather than propagate a large
        *     number of changes to reflect removal for some items, addition of
        *     others, just tell somebody who cares that a lot happened.  It will
        *     be faster an easier for somebody watching to just turn around and
        *     query the container control what the new bunch of selected items
        *     are.

        """

        EVENT_OBJECT_STATECHANGE = 0x800A # hwnd + ID + idChild is item w/ state change

        """

        * Examples of when to send an EVENT_OBJECT_STATECHANGE include
        *      * It is being enabled/disabled (USER does for windows)
        *      * It is being pressed/released (USER does for buttons)
        *      * It is being checked/unchecked (USER does for radio/check buttons)

        """

        EVENT_OBJECT_LOCATIONCHANGE = 0x800B # hwnd + ID + idChild is moved/sized item

        """

        * Note:
        * A LOCATIONCHANGE is not sent for every child object when the parent
        * changes shape/moves.  Send one notification for the topmost object
        * that is changing.  For example, if the user resizes a top level window,
        * USER will generate a LOCATIONCHANGE for it, but not for the menu bar,
        * title bar, scrollbars, etc.  that are also changing shape/moving.
        *
        * In other words, it only generates LOCATIONCHANGE notifications for
        * real windows that are moving/sizing.  It will not generate a LOCATIONCHANGE
        * for every non-floating child window when the parent moves (the children are
        * logically moving also on screen, but not relative to the parent).
        *
        * Now, if the app itself resizes child windows as a result of being
        * sized, USER will generate LOCATIONCHANGEs for those dudes also because
        * it doesn't know better.
        *
        * Note also that USER will generate LOCATIONCHANGE notifications for two
        * non-window sys objects:
        *      (1) System caret
        *      (2) Cursor

        """ 

        EVENT_OBJECT_NAMECHANGE = 0x800C # hwnd + ID + idChild is item w/ name change
        EVENT_OBJECT_DESCRIPTIONCHANGE = 0x800D # hwnd + ID + idChild is item w/ desc change
        EVENT_OBJECT_VALUECHANGE = 0x800E # hwnd + ID + idChild is item w/ value change
        EVENT_OBJECT_PARENTCHANGE = 0x800F # hwnd + ID + idChild is item w/ new parent
        EVENT_OBJECT_HELPCHANGE = 0x8010 # hwnd + ID + idChild is item w/ help change
        EVENT_OBJECT_DEFACTIONCHANGE = 0x8011 # hwnd + ID + idChild is item w/ def action change
        EVENT_OBJECT_ACCELERATORCHANGE = 0x8012 # hwnd + ID + idChild is item w/ keybd accel change
        EVENT_OBJECT_INVOKED = 0x8013 # hwnd + ID + idChild is item invoked
        EVENT_OBJECT_TEXTSELECTIONCHANGED = 0x8014 # hwnd + ID + idChild is item w? test selection change

        """

        * EVENT_OBJECT_CONTENTSCROLLED
        * Sent when ending the scrolling of a window object.
        *
        * Unlike the similar event (EVENT_SYSTEM_SCROLLEND), this event will be
        * associated with the scrolling window itself. There is no difference
        * between horizontal or vertical scrolling.
        *
        * This event should be posted whenever scroll action is completed, including
        * when it is scrolled by scroll bars, mouse wheel, or keyboard navigations.
        *
        *   example:
        *          hwnd == window that is scrolling
        *          idObject == OBJID_CLIENT
        *          idChild == CHILDID_SELF

        """

        EVENT_OBJECT_CONTENTSCROLLED = 0x8015
        EVENT_SYSTEM_ARRANGMENTPREVIEW = 0x8016

        """

        * EVENT_OBJECT_CLOAKED / UNCLOAKED
        * Sent when a window is cloaked or uncloaked.
        * A cloaked window still exists, but is invisible to
        * the user.

        """

        EVENT_OBJECT_CLOAKED = 0x8017
        EVENT_OBJECT_UNCLOAKED = 0x8018

        """

        * EVENT_OBJECT_LIVEREGIONCHANGED
        * Sent when an object that is part of a live region
        * changes.  A live region is an area of an application
        * that changes frequently and/or asynchronously, so
        * that an assistive technology tool might want to pay
        * special attention to it.

        """

        EVENT_OBJECT_LIVEREGIONCHANGED = 0x8019

        """

        * EVENT_OBJECT_HOSTEDOBJECTSINVALIDATED
        * Sent when a window that is hosting other Accessible
        * objects changes the hosted objects.  A client may
        * wish to requery to see what the new hosted objects are,
        * especially if it has been monitoring events from this
        * window.  A hosted object is one with a different Accessibility
        * framework (MSAA or UI Automation) from its host.
        *
        * Changes in hosted objects with the *same* framework
        * as the parent should be handed with the usual structural
        * change events, such as EVENT_OBJECT_CREATED for MSAA.
        * see above.

        """

        EVENT_OBJECT_HOSTEDOBJECTSINVALIDATED = 0x8020

        """

        * Drag / Drop Events
        * These events are used in conjunction with the
        * UI Automation Drag/Drop patterns.
        *
        * For DRAGSTART, DRAGCANCEL, and DRAGCOMPLETE,
        * HWND+objectID+childID refers to the object being dragged.
        *
        * For DRAGENTER, DRAGLEAVE, and DRAGDROPPED,
        * HWND+objectID+childID refers to the target of the drop
        * that is being hovered over.

        """

        EVENT_OBJECT_DRAGSTART = 0x8021
        EVENT_OBJECT_DRAGCANCEL = 0x8022
        EVENT_OBJECT_DRAGCOMPLETE = 0x8023
        EVENT_OBJECT_DRAGENTER = 0x8024
        EVENT_OBJECT_DRAGLEAVE = 0x8025
        EVENT_OBJECT_DRAGDROPPED = 0x8026

        """

        * EVENT_OBJECT_IME_SHOW/HIDE
        * Sent by an IME window when it has become visible or invisible.

        """

        EVENT_OBJECT_IME_SHOW = 0x8027
        EVENT_OBJECT_IME_HIDE = 0x8028

        """

        * EVENT_OBJECT_IME_CHANGE
        * Sent by an IME window whenever it changes size or position.

        """

        EVENT_OBJECT_IME_CHANGE = 0x8029
        EVENT_OBJECT_TEXTEDIT_CONVERSIONTARGETCHANGED = 0x8030
        EVENT_OBJECT_END = 0x80FF
        EVENT_AIA_START = 0xA000
        EVENT_AIA_END = 0xAFFF

        """

        * Child IDs

        """


        """

        * System Sounds (idChild of system SOUND notification)

        """

        SOUND_SYSTEM_STARTUP = 1
        SOUND_SYSTEM_SHUTDOWN = 2
        SOUND_SYSTEM_BEEP = 3
        SOUND_SYSTEM_ERROR = 4
        SOUND_SYSTEM_QUESTION = 5
        SOUND_SYSTEM_WARNING = 6
        SOUND_SYSTEM_INFORMATION = 7
        SOUND_SYSTEM_MAXIMIZE = 8
        SOUND_SYSTEM_MINIMIZE = 9
        SOUND_SYSTEM_RESTOREUP = 10
        SOUND_SYSTEM_RESTOREDOWN = 11
        SOUND_SYSTEM_APPSTART = 12
        SOUND_SYSTEM_FAULT = 13
        SOUND_SYSTEM_APPEND = 14
        SOUND_SYSTEM_MENUCOMMAND = 15
        SOUND_SYSTEM_MENUPOPUP = 16
        CSOUND_SYSTEM = 16

        """

        * System Alerts (indexChild of system ALERT notification)

        """

        ALERT_SYSTEM_INFORMATIONAL = 1 # MB_INFORMATION
        ALERT_SYSTEM_WARNING = 2 # MB_WARNING
        ALERT_SYSTEM_ERROR = 3 # MB_ERROR
        ALERT_SYSTEM_QUERY = 4 # MB_QUESTION
        ALERT_SYSTEM_CRITICAL = 5 # HardSysErrBox
        CALERT_SYSTEM = 6

        # REGION *** Desktop Family ***

# NOT REALIZED
# TODO

# REGION ***