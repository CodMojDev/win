
"""
/*****************************************************************************\
*                                                                             *
* commctrl.h - - Interface for the Windows Common Controls                    *
*                                                                             *
* Version 1.2                                                                 *
*                                                                             *
* Copyright (c) Microsoft Corporation. All rights reserved.                   *
*                                                                             *
\*****************************************************************************/
"""

from . import cpreproc

from .defbase import *

from .sdkddkver import *

from .minwindef import *

from .guiddef import LPIID, REFIID, IID

from .winuser import *

from .winnt import TEXT, SYSTEMTIME

if cpreproc.pragma_once("_INC_COMMCTRL"):
    comctl32 = W_WinDLL("comctl32.dll")

    #
    # Users of this header may define any number of these constants to avoid
    # the definitions of each functional group.
    #
    #    NOTOOLBAR    Customizable bitmap-button toolbar control.
    #    NOUPDOWN     Up and Down arrow increment/decrement control.
    #    NOSTATUSBAR  Status bar control.
    #    NOMENUHELP   APIs to help manage menus, especially with a status bar.
    #    NOTRACKBAR   Customizable column-width tracking control.
    #    NODRAGLIST   APIs to make a listbox source and sink drag&drop actions.
    #    NOPROGRESS   Progress gas gauge.
    #    NOHOTKEY     HotKey control
    #    NOHEADER     Header bar control.
    #    NOIMAGEAPIS  ImageList apis.
    #    NOLISTVIEW   ListView control.
    #    NOTREEVIEW   TreeView control.
    #    NOTABCONTROL Tab control.
    #    NOANIMATE    Animate control.
    #    NOBUTTON     Button control.
    #    NOSTATIC     Static control.
    #    NOEDIT       Edit control.
    #    NOLISTBOX    Listbox control.
    #    NOCOMBOBOX   Combobox control.
    #    NOSCROLLBAR  Scrollbar control.
    #    NOTASKDIALOG Task Dialog.
    #
    #=============================================================================

    from .prsht import *

    @comctl32.foreign(VOID)
    def InitCommonControls(): ...

    class tagINITCOMMONCONTROLSEX(CStructure):
        _fields_ = [
            ("dwSize", DWORD), # size of this structure
            ("dwICC", DWORD), # flags indicating which classes to be initialized
        ]
        
        dwSize: int
        dwICC: int
        
    INITCOMMONCONTROLSEX = tagINITCOMMONCONTROLSEX
    LPINITCOMMONCONTROLSEX = POINTER(INITCOMMONCONTROLSEX)

    ICC_LISTVIEW_CLASSES = 0x00000001 # listview, header
    ICC_TREEVIEW_CLASSES = 0x00000002 # treeview, tooltips
    ICC_BAR_CLASSES = 0x00000004 # toolbar, statusbar, trackbar, tooltips
    ICC_TAB_CLASSES = 0x00000008 # tab, tooltips
    ICC_UPDOWN_CLASS = 0x00000010 # updown
    ICC_PROGRESS_CLASS = 0x00000020 # progress
    ICC_HOTKEY_CLASS = 0x00000040 # hotkey
    ICC_ANIMATE_CLASS = 0x00000080 # animate
    ICC_WIN95_CLASSES = 0x000000FF
    ICC_DATE_CLASSES = 0x00000100 # month picker, date picker, time picker, updown
    ICC_USEREX_CLASSES = 0x00000200 # comboex
    ICC_COOL_CLASSES = 0x00000400 # rebar (coolbar) control
    ICC_INTERNET_CLASSES = 0x00000800
    ICC_PAGESCROLLER_CLASS = 0x00001000 # page scroller
    ICC_NATIVEFNTCTL_CLASS = 0x00002000 # native font control
    ICC_STANDARD_CLASSES = 0x00004000
    ICC_LINK_CLASS = 0x00008000
    @comctl32.foreign(BOOL, LPINITCOMMONCONTROLSEX)
    def InitCommonControlsEx(picce: IPointer[INITCOMMONCONTROLSEX]) -> int: ...
    ODT_HEADER = 100
    ODT_TAB = 101
    ODT_LISTVIEW = 102
    #====== Ranges for control message IDs =======================================
    LVM_FIRST = 0x1000 # ListView messages
    TV_FIRST = 0x1100 # TreeView messages
    HDM_FIRST = 0x1200 # Header messages
    TCM_FIRST = 0x1300 # Tab control messages
    PGM_FIRST = 0x1400 # Pager control messages
    ECM_FIRST = 0x1500 # Edit control messages
    BCM_FIRST = 0x1600 # Button control messages
    CBM_FIRST = 0x1700 # Combobox control messages
    CCM_FIRST = 0x2000 # Common control shared messages
    CCM_LAST = (CCM_FIRST + 0x200)
    CCM_SETBKCOLOR = (CCM_FIRST + 1) # lParam is bkColor

    class tagCOLORSCHEME(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("clrBtnHighlight", COLORREF), # highlight color
            ("clrBtnShadow", COLORREF) # shadow color
        ]
        
        dwSize: int
        clrBtnHighlight: int
        clrBtnShadow: int
        
    COLORSCHEME = tagCOLORSCHEME
    LPCOLORSCHEME = POINTER(COLORSCHEME)

    CCM_SETCOLORSCHEME = (CCM_FIRST + 2) # lParam is color scheme
    CCM_GETCOLORSCHEME = (CCM_FIRST + 3) # fills in COLORSCHEME pointed to by lParam
    CCM_GETDROPTARGET = (CCM_FIRST + 4)
    CCM_SETUNICODEFORMAT = (CCM_FIRST + 5)
    CCM_GETUNICODEFORMAT = (CCM_FIRST + 6)
    COMCTL32_VERSION = 6
    COMCTL32_VERSION = 5
    CCM_SETVERSION = (CCM_FIRST + 0x7)
    CCM_GETVERSION = (CCM_FIRST + 0x8)
    CCM_SETNOTIFYWINDOW = (CCM_FIRST + 0x9) # wParam == hwndParent.
    CCM_SETWINDOWTHEME = (CCM_FIRST + 0xb)
    CCM_DPISCALE = (CCM_FIRST + 0xc) # wParam == Awareness
    # for tooltips
    INFOTIPSIZE = 1024
    #====== WM_NOTIFY Macros =====================================================
    def HANDLE_WM_NOTIFY(hwnd, wParam, lParam, fn):
        return fn(hwnd, wParam, cast(lParam, LPNMHDR))
    
    def FORWARD_WM_NOTIFY(hwnd, idFrom, pnmhdr, fn):
        return fn(hwnd, WM_NOTIFY, WPARAM(idFrom).value, cast(pnmhdr, LPARAM))
    
    #====== Generic WM_NOTIFY notification codes =================================
    NM_FIRST = (0 - 0) # generic to all controls
    NM_LAST = (0 - 99)
    NM_OUTOFMEMORY = (NM_FIRST-1)
    NM_CLICK = (NM_FIRST-2) # uses NMCLICK struct
    NM_DBLCLK = (NM_FIRST-3)
    NM_RETURN = (NM_FIRST-4)
    NM_RCLICK = (NM_FIRST-5) # uses NMCLICK struct
    NM_RDBLCLK = (NM_FIRST-6)
    NM_SETFOCUS = (NM_FIRST-7)
    NM_KILLFOCUS = (NM_FIRST-8)
    NM_CUSTOMDRAW = (NM_FIRST-12)
    NM_HOVER = (NM_FIRST-13)
    NM_NCHITTEST = (NM_FIRST-14) # uses NMMOUSE struct
    NM_KEYDOWN = (NM_FIRST-15) # uses NMKEY struct
    NM_RELEASEDCAPTURE = (NM_FIRST-16)
    NM_SETCURSOR = (NM_FIRST-17) # uses NMMOUSE struct
    NM_CHAR = (NM_FIRST-18) # uses NMCHAR struct
    NM_TOOLTIPSCREATED = (NM_FIRST-19) # notify of when the tooltips window is create
    NM_LDOWN = (NM_FIRST-20)
    NM_RDOWN = (NM_FIRST-21)
    NM_THEMECHANGED = (NM_FIRST-22)
    NM_FONTCHANGED = (NM_FIRST-23)
    NM_CUSTOMTEXT = (NM_FIRST-24) # uses NMCUSTOMTEXT struct
    NM_TVSTATEIMAGECHANGING = (NM_FIRST-24) # uses NMTVSTATEIMAGECHANGING struct, defined after HTREEITEM

    def CCSIZEOF_STRUCT(structname, member):
        return getattr(structname, member).offset + getattr(structname, member).size

    #====== Generic WM_NOTIFY notification structures ============================
    class tagNMTOOLTIPSCREATED(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("hwndToolTips", HWND)
        ]
        hdr: NMHDR
        hwndToolTips: int
        
        hdr: NMHDR
        
    NMTOOLTIPSCREATED = tagNMTOOLTIPSCREATED
    LPNMTOOLTIPSCREATED = POINTER(NMTOOLTIPSCREATED)

    class tagNMMOUSE(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("dwItemSpec", DWORD_PTR),
            ("dwItemData", DWORD_PTR),
            ("pt", POINT),
            ("dwHitInfo", LPARAM) # any specifics about where on the item or control the mouse is
        ]
        hdr: NMHDR
        dwItemSpec: int
        dwItemData: int
        pt: POINT
        dwHitInfo: int
    NMMOUSE = tagNMMOUSE
    LPNMMOUSE = POINTER(NMMOUSE)

    NMCLICK = NMMOUSE
    LPNMCLICK = LPNMMOUSE

    # Generic structure to request an object of a specific type.

    class tagNMOBJECTNOTIFY(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("iItem", INT),
            ("piid", LPIID),
            ("pObject", PVOID),
            ("hResult", HRESULT),
            ("dwFlags", DWORD) # control specific flags (hints as to where in iItem it hit)
        ]
        hdr: NMHDR
        iItem: int
        piid: IPointer[IID]
        pObject: int
        hResult: int
        dwFlags: int
    NMOBJECTNOTIFY = tagNMOBJECTNOTIFY
    LPNMOBJECTNOTIFY = POINTER(NMOBJECTNOTIFY)

    # Generic structure for a key

    class tagNMKEY(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("nVKey", UINT),
            ("uFlags", UINT)
        ]
        hdr: NMHDR
        nVKey: int
        uFlags: int
    NMKEY = tagNMKEY
    LPNMKEY = POINTER(NMKEY)

    # Generic structure for a character

    class tagNMCHAR(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("ch", UINT),
            ("dwItemPrev", DWORD), # Item previously selected
            ("dwItemNext", DWORD) # Item to be selected
        ]
        hdr: NMHDR
        ch: int
        dwItemPrev: int
        dwItemNext: int
    NMCHAR = tagNMCHAR
    LPNMCHAR = POINTER(NMCHAR)

    class tagNMCUSTOMTEXT(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("hDC", HDC),
            ("lpString", LPCWSTR),
            ("nCount", INT),
            ("lpRect", LPRECT),
            ("uFormat", UINT),
            ("fLink", BOOL)
        ]
        hdr: NMHDR
        hDC: int
        lpString: LPCWSTR
        nCount: int
        lpRect: LPRECT
        uFormat: int
        fLink: int
    NMCUSTOMTEXT = tagNMCUSTOMTEXT
    LPNMCUSTOMTEXT = POINTER(NMCUSTOMTEXT)

    #====== WM_NOTIFY codes (NMHDR.code values) ==================================
    NM_FIRST = (0- 0) # generic to all controls
    NM_LAST = (0- 99)
    LVN_FIRST = (0-100) # listview
    LVN_LAST = (0-199)
    # Property sheet reserved      (0-200) -  (0-299) - see prsht.h
    HDN_FIRST = (0-300) # header
    HDN_LAST = (0-399)
    TVN_FIRST = (0-400) # treeview
    TVN_LAST = (0-499)
    TTN_FIRST = (0-520) # tooltips
    TTN_LAST = (0-549)
    TCN_FIRST = (0-550) # tab control
    TCN_LAST = (0-580)
    # Shell reserved               (0-580) -  (0-589)
    CDN_FIRST = (0-601) # common dialog (new)
    CDN_LAST = (0-699)
    TBN_FIRST = (0-700) # toolbar
    TBN_LAST = (0-720)
    UDN_FIRST = (0-721) # updown
    UDN_LAST = (0-729)
    DTN_FIRST = (0-740) # datetimepick
    DTN_LAST = (0-745) # DTN_FIRST - 5
    MCN_FIRST = (0-746) # monthcal
    MCN_LAST = (0-752) # MCN_FIRST - 6
    DTN_FIRST2 = (0-753) # datetimepick2
    DTN_LAST2 = (0-799)
    CBEN_FIRST = (0-800) # combo box ex
    CBEN_LAST = (0-830)
    RBN_FIRST = (0-831) # rebar
    RBN_LAST = (0-859)
    IPN_FIRST = (0-860) # internet address
    IPN_LAST = (0-879) # internet address
    SBN_FIRST = (0-880) # status bar
    SBN_LAST = (0-899)
    PGN_FIRST = (0-900) # Pager Control
    PGN_LAST = (0-950)
    WMN_FIRST = (0-1000)
    WMN_LAST = (0-1200)
    BCN_FIRST = (0-1250)
    BCN_LAST = (0-1350)
    TRBN_FIRST = (0-1501) # trackbar
    TRBN_LAST = (0-1519)
    EN_FIRST = (0-1520) # edit control
    EN_LAST = (0-1540)
    MSGF_COMMCTRL_BEGINDRAG = 0x4200
    MSGF_COMMCTRL_SIZEHEADER = 0x4201
    MSGF_COMMCTRL_DRAGSELECT = 0x4202
    MSGF_COMMCTRL_TOOLBARCUST = 0x4203
    #==================== CUSTOM DRAW ==========================================
    # custom draw return flags
    # values under 0x00010000 are reserved for global custom draw values.
    # above that are for specific controls
    CDRF_DODEFAULT = 0x00000000
    CDRF_NEWFONT = 0x00000002
    CDRF_SKIPDEFAULT = 0x00000004
    CDRF_DOERASE = 0x00000008 # draw the background
    CDRF_SKIPPOSTPAINT = 0x00000100 # don't draw the focus rect
    CDRF_NOTIFYPOSTPAINT = 0x00000010
    CDRF_NOTIFYITEMDRAW = 0x00000020
    CDRF_NOTIFYSUBITEMDRAW = 0x00000020 # flags are the same, we can distinguish by context
    CDRF_NOTIFYPOSTERASE = 0x00000040
    # drawstage flags
    # values under 0x00010000 are reserved for global custom draw values.
    # above that are for specific controls
    CDDS_PREPAINT = 0x00000001
    CDDS_POSTPAINT = 0x00000002
    CDDS_PREERASE = 0x00000003
    CDDS_POSTERASE = 0x00000004
    # the 0x000010000 bit means it's individual item specific
    CDDS_ITEM = 0x00010000
    CDDS_ITEMPREPAINT = (CDDS_ITEM | CDDS_PREPAINT)
    CDDS_ITEMPOSTPAINT = (CDDS_ITEM | CDDS_POSTPAINT)
    CDDS_ITEMPREERASE = (CDDS_ITEM | CDDS_PREERASE)
    CDDS_ITEMPOSTERASE = (CDDS_ITEM | CDDS_POSTERASE)
    CDDS_SUBITEM = 0x00020000
    # itemState flags
    CDIS_SELECTED = 0x0001
    CDIS_GRAYED = 0x0002
    CDIS_DISABLED = 0x0004
    CDIS_CHECKED = 0x0008
    CDIS_FOCUS = 0x0010
    CDIS_DEFAULT = 0x0020
    CDIS_HOT = 0x0040
    CDIS_MARKED = 0x0080
    CDIS_INDETERMINATE = 0x0100
    CDIS_SHOWKEYBOARDCUES = 0x0200
    CDIS_NEARHOT = 0x0400
    CDIS_OTHERSIDEHOT = 0x0800
    CDIS_DROPHILITED = 0x1000

    class tagNMCUSTOMDRAWINFO(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("dwDrawStage", DWORD),
            ("hdc", HDC),
            ("rc", RECT),
            ("dwItemSpec", DWORD_PTR), # this is control specific, but it's how to specify an item.  valid only with CDDS_ITEM bit set
            ("uItemState", UINT),
            ("lItemlParam", LPARAM)
        ]
        hdr: NMHDR
        dwDrawStage: int
        hdc: int
        rc: RECT
        dwItemSpec: int
        uItemState: int
        lItemlParam: int
    NMCUSTOMDRAW = tagNMCUSTOMDRAWINFO
    LPNMCUSTOMDRAW = POINTER(NMCUSTOMDRAW)

    class tagNMTTCUSTOMDRAW(CStructure):
        _fields_ = [
            ("nmcd", NMCUSTOMDRAW),
            ("uDrawFlags", UINT)
        ]
        nmcd: NMCUSTOMDRAW
        uDrawFlags: int
    NMTTCUSTOMDRAW = tagNMTTCUSTOMDRAW
    LPNMTTCUSTOMDRAW = POINTER(NMTTCUSTOMDRAW)

    class tagNMCUSTOMSPLITRECTINFO(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("rcClient", RECT),
            ("rcButton", RECT),
            ("rcSplit", RECT)
        ]
        hdr: NMHDR
        rcClient: RECT
        rcButton: RECT
        rcSplit: RECT
    NMCUSTOMSPLITRECTINFO = tagNMCUSTOMSPLITRECTINFO
    LPNMCUSTOMSPLITRECTINFO = POINTER(NMCUSTOMSPLITRECTINFO)

    NM_GETCUSTOMSPLITRECT = (BCN_FIRST + 0x0003)

    #====== IMAGE APIS ===========================================================

    if cpreproc.ifndef("NOIMAGEAPIS"):

        CLR_NONE = 0xFFFFFFFF
        CLR_DEFAULT = 0xFF000000

        HIMAGELIST = HANDLE

        class _IMAGELISTDRAWPARAMS(CStructure):
            _fields_ = [
                ("cbSize", DWORD),
                ("himl", HIMAGELIST),
                ("i", INT),
                ("hdcDst", HDC),
                ("x", INT),
                ("y", INT),
                ("cx", INT),
                ("cy", INT),
                ("xBitmap", INT), # x offest from the upperleft of bitmap
                ("yBitmap", INT), # y offset from the upperleft of bitmap
                ("rgbBk", COLORREF),
                ("rgbFg", COLORREF),
                ("fStyle", UINT),
                ("dwRop", DWORD),
                ("fState", DWORD),
                ("Frame", DWORD),
                ("crEffect", COLORREF)
            ]
            cbSize: int
            himl: int
            i: int
            hdcDst: int
            x: int
            y: int
            cx: int
            cy: int
            xBitmap: int
            yBitmap: int
            rgbBk: int
            rgbFg: int
            fStyle: int
            dwRop: int
            fState: int
            Frame: int
            crEffect: int
        IMAGELISTDRAWPARAMS = _IMAGELISTDRAWPARAMS
        LPIMAGELISTDRAWPARAMS = POINTER(IMAGELISTDRAWPARAMS)

        IMAGELISTDRAWPARAMS_V3_SIZE = CCSIZEOF_STRUCT(IMAGELISTDRAWPARAMS, "dwRop")

        ILC_MASK = 0x00000001
        ILC_COLOR = 0x00000000
        ILC_COLORDDB = 0x000000FE
        ILC_COLOR4 = 0x00000004
        ILC_COLOR8 = 0x00000008
        ILC_COLOR16 = 0x00000010
        ILC_COLOR24 = 0x00000018
        ILC_COLOR32 = 0x00000020
        ILC_PALETTE = 0x00000800 # (not implemented)
        ILC_MIRROR = 0x00002000 # Mirror the icons contained, if the process is mirrored
        ILC_PERITEMMIRROR = 0x00008000 # Causes the mirroring code to mirror each item when inserting a set of images, verses the whole strip
        ILC_ORIGINALSIZE = 0x00010000 # Imagelist should accept smaller than set images and apply OriginalSize based on image added
        ILC_HIGHQUALITYSCALE = 0x00020000 # Imagelist should enable use of the high quality scaler.
        
        ImageList_Create = declare(comctl32.ImageList_Create, HIMAGELIST, INT, INT, UINT, INT, INT)
        ImageList_Destroy = declare(comctl32.ImageList_Destroy, BOOL, HIMAGELIST)
        ImageList_GetImageCount = declare(comctl32.ImageList_GetImageCount, INT, HIMAGELIST)
        ImageList_SetImageCount = declare(comctl32.ImageList_SetImageCount, BOOL, HIMAGELIST, UINT)
        ImageList_Add = declare(comctl32.ImageList_Add, INT, HIMAGELIST, HBITMAP, HBITMAP)
        ImageList_ReplaceIcon = declare(comctl32.ImageList_ReplaceIcon, INT, HIMAGELIST, INT, HICON)
        ImageList_SetBkColor = declare(comctl32.ImageList_SetBkColor, COLORREF, HIMAGELIST, COLORREF)
        ImageList_GetBkColor = declare(comctl32.ImageList_GetBkColor, COLORREF, HIMAGELIST)
        ImageList_SetOverlayImage = declare(comctl32.ImageList_SetOverlayImage, BOOL, HIMAGELIST, INT, INT)

        def ImageList_AddIcon(himl, hicon):
            return ImageList_ReplaceIcon(himl, -1, hicon)
        
        ILD_NORMAL = 0x00000000
        ILD_TRANSPARENT = 0x00000001
        ILD_MASK = 0x00000010
        ILD_IMAGE = 0x00000020
        ILD_ROP = 0x00000040
        ILD_BLEND25 = 0x00000002
        ILD_BLEND50 = 0x00000004
        ILD_OVERLAYMASK = 0x00000F00
        INDEXTOOVERLAYMASK = lambda i: ((i) << 8)
        ILD_PRESERVEALPHA = 0x00001000 # This preserves the alpha channel in dest
        ILD_SCALE = 0x00002000 # Causes the image to be scaled to cx, cy instead of clipped
        ILD_DPISCALE = 0x00004000
        ILD_ASYNC = 0x00008000
        ILD_SELECTED = ILD_BLEND50
        ILD_FOCUS = ILD_BLEND25
        ILD_BLEND = ILD_BLEND50
        CLR_HILIGHT = CLR_DEFAULT
        ILS_NORMAL = 0x00000000
        ILS_GLOW = 0x00000001
        ILS_SHADOW = 0x00000002
        ILS_SATURATE = 0x00000004
        ILS_ALPHA = 0x00000008
        ILGT_NORMAL = 0x00000000
        ILGT_ASYNC = 0x00000001

        HBITMAP_CALLBACK = HBITMAP(-1) # only for SparseImageList

        ImageList_Draw = declare(comctl32.ImageList_Draw, BOOL, HIMAGELIST, INT, HDC, INT, INT, UINT)
        ImageList_Replace = declare(comctl32.ImageList_Replace, BOOL, HIMAGELIST, INT, HBITMAP, HBITMAP)
        ImageList_AddMasked = declare(comctl32.ImageList_AddMasked, INT, HIMAGELIST, HBITMAP, COLORREF)
        ImageList_DrawEx = declare(comctl32.ImageList_DrawEx, BOOL, HIMAGELIST, INT, HDC, INT, INT, INT, INT, COLORREF, COLORREF, UINT)
        ImageList_DrawIndirect = declare(comctl32.ImageList_DrawIndirect, BOOL, LPIMAGELISTDRAWPARAMS)
        ImageList_Remove = declare(comctl32.ImageList_Remove, BOOL, HIMAGELIST, INT)
        ImageList_GetIcon = declare(comctl32.ImageList_GetIcon, HICON, HIMAGELIST, INT, UINT)
        ImageList_LoadImageA = declare(comctl32.ImageList_LoadImageA, HIMAGELIST, HINSTANCE, LPCSTR, INT, INT, COLORREF, UINT, UINT)
        ImageList_LoadImageW = declare(comctl32.ImageList_LoadImageW, HIMAGELIST, HINSTANCE, LPCWSTR, INT, INT, COLORREF, UINT, UINT)
        ImageList_LoadImage = unicode(ImageList_LoadImageW, ImageList_LoadImageA)

        ILCF_MOVE = 0x00000000
        ILCF_SWAP = 0x00000001

        ImageList_Copy = declare(comctl32.ImageList_Copy, BOOL, HIMAGELIST, INT, HIMAGELIST, INT, UINT)
        ImageList_BeginDrag = declare(comctl32.ImageList_BeginDrag, BOOL, HIMAGELIST, INT, INT, INT)
        ImageList_EndDrag = declare(comctl32.ImageList_EndDrag, VOID, VOID)
        ImageList_DragEnter = declare(comctl32.ImageList_DragEnter, BOOL, HWND, INT, INT)
        ImageList_DragLeave = declare(comctl32.ImageList_DragLeave, BOOL, HWND)
        ImageList_DragMove = declare(comctl32.ImageList_DragMove, BOOL, INT, INT)
        ImageList_SetDragCursorImage = declare(comctl32.ImageList_SetDragCursorImage, BOOL, HIMAGELIST, INT, INT, INT)
        ImageList_DragShowNolock = declare(comctl32.ImageList_DragShowNolock, BOOL, BOOL)
        ImageList_GetDragImage = declare(comctl32.ImageList_GetDragImage, HIMAGELIST, PPOINT, PPOINT)

        def ImageList_RemoveAll(himl):
            return ImageList_Remove(himl, -1)
        
        def ImageList_ExtractIcon(hi, himl, i):
            return ImageList_GetIcon(himl, i, 0)
        
        def ImageList_LoadBitmap(hi, lpbmp, cx, cGrow, crMask):
            return ImageList_LoadImage(hi, lpbmp, cx, cGrow, crMask, IMAGE_BITMAP, 0)

        PIstream = PVOID

        ImageList_Read = declare(comctl32.ImageList_Read, HIMAGELIST, PIstream)
        ImageList_Write = declare(comctl32.ImageList_Write, BOOL, HIMAGELIST, PIstream)
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            ILP_NORMAL = 0 # Writes or reads the stream using new sematics for this version of comctl32
            ILP_DOWNLEVEL = 1 # Write or reads the stream using downlevel sematics.
            ImageList_ReadEx = declare(comctl32.ImageList_ReadEx, HRESULT, DWORD, PIstream, REFIID, PPVOID)
            ImageList_WriteEx = declare(comctl32.ImageList_WriteEx, HRESULT, HIMAGELIST, DWORD, PIstream)   

        class _IMAGEINFO(CStructure):
            _fields_ = [
                ("hbmImage", HBITMAP),
                ("hbmMask", HBITMAP),
                ("Unused1", INT),
                ("Unused2", INT),
                ("rcImage", RECT)
            ]
            hbmImage: int
            hbmMask: int
            Unused1: int
            Unused2: int
            rcImage: RECT
        IMAGEINFO = _IMAGEINFO
        LPIMAGEINFO = POINTER(IMAGEINFO)

        ImageList_GetIconSize = declare(comctl32.ImageList_GetIconSize, BOOL, HIMAGELIST, PINT, PINT)
        ImageList_SetIconSize = declare(comctl32.ImageList_SetIconSize, BOOL, HIMAGELIST, INT, INT)
        ImageList_GetImageInfo = declare(comctl32.ImageList_GetImageInfo, BOOL, HIMAGELIST, INT, LPIMAGEINFO)
        ImageList_Merge = declare(comctl32.ImageList_Merge, HIMAGELIST, HIMAGELIST, INT, HIMAGELIST, INT, INT, INT)
        ImageList_Duplicate = declare(comctl32.ImageList_Duplicate, HIMAGELIST, HIMAGELIST)

        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            HIMAGELIST_QueryInterface = declare(comctl32.HIMAGELIST_QueryInterface, HRESULT, HIMAGELIST, REFIID, PVOID)
    #====== HEADER CONTROL =======================================================
    if cpreproc.ifndef("NOHEADER"):
        if cpreproc.ifdef("_WIN32"):
            WC_HEADERA = "SysHeader32"
            WC_HEADERW = u"SysHeader32"
            WC_HEADER = unicode(WC_HEADERW, WC_HEADERA)
        else:
            WC_HEADER = "SysHeader"
    # begin_r_commctrl
    HDS_HORZ = 0x0000
    HDS_BUTTONS = 0x0002
    HDS_HOTTRACK = 0x0004
    HDS_HIDDEN = 0x0008
    HDS_DRAGDROP = 0x0040
    HDS_FULLDRAG = 0x0080
    HDS_FILTERBAR = 0x0100
    HDS_FLAT = 0x0200
    HDS_CHECKBOXES = 0x0400
    HDS_NOSIZING = 0x0800
    HDS_OVERFLOW = 0x1000
    # end_r_commctrl
    HDFT_ISSTRING = 0x0000 # HD_ITEM.pvFilter points to a HD_TEXTFILTER
    HDFT_ISNUMBER = 0x0001 # HD_ITEM.pvFilter points to a INT
    HDFT_ISDATE = 0x0002 # HD_ITEM.pvFilter points to a DWORD (
    HDFT_HASNOVALUE = 0x8000 # clear the filter,
    class _HD_TEXTFILTERA(CStructure):
        _fields_ = [
            ("pszText", LPSTR), # [in] pointer to the buffer containing the filter (ANSI)
            ("cchTextMax", INT) # [in] max size of buffer/edit control buffer
        ]
        pszText: LPSTR
        cchTextMax: int
    HD_TEXTFILTERA = _HD_TEXTFILTERA
    LPHD_TEXTFILTERA = POINTER(HD_TEXTFILTERA)

    class _HD_TEXTFILTERW(CStructure):
        _fields_ = [
            ("pszText", LPWSTR), # [in] pointer to the buffer containing the filter (Unicode)
            ("cchTextMax", INT) # [in] max size of buffer/edit control buffer
        ]
        pszText: LPWSTR
        cchTextMax: int
    HD_TEXTFILTERW = _HD_TEXTFILTERW
    LPHD_TEXTFILTERW = POINTER(HD_TEXTFILTERW)

    class _HD_ITEMA(CStructure):
        _fields_ = [
            ("mask", UINT),
            ("cx", INT),
            ("pszText", LPSTR),
            ("hbm", HBITMAP),
            ("cchTextMax", INT),
            ("fmt", INT),
            ("lParam", LPARAM),
            ("iImage", INT), # index of bitmap in ImageList
            ("iOrder", INT), # where to draw this item
            ("type", UINT), # [in] filter type (defined what pvFilter is a pointer to)
            ("pvFilter", PVOID), # [in] filter data see above
            ("state", UINT)
        ]
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            _fields_.append(("state", UINT))
        mask: int
        cx: int
        pszText: LPSTR
        hbm: int
        cchTextMax: int
        fmt: int
        lParam: int
        iImage: int
        iOrder: int
        type: int
        pvFilter: int
        state: int
    HDITEMA = _HD_ITEMA
    LPHDITEMA = POINTER(HDITEMA)

    class _HD_ITEMW(CStructure):
        _fields_ = [
            ("mask", UINT),
            ("cx", INT),
            ("pszText", LPWSTR),
            ("hbm", HBITMAP),
            ("cchTextMax", INT),
            ("fmt", INT),
            ("lParam", LPARAM),
            ("iImage", INT), # index of bitmap in ImageList
            ("iOrder", INT), # where to draw this item
            ("type", UINT), # [in] filter type (defined what pvFilter is a pointer to)
            ("pvFilter", PVOID) # [in] filter data see above
        ]
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            _fields_.append(("state", UINT))
        mask: int
        cx: int
        pszText: LPWSTR
        hbm: int
        cchTextMax: int
        fmt: int
        lParam: int
        iImage: int
        iOrder: int
        type: int
        pvFilter: int
        state: int
    HDITEMW = _HD_ITEMW
    LPHDITEMW = POINTER(HDITEMW)

    HDITEM = unicode(HDITEMW, HDITEMA)

    HD_ITEMA = HDITEMA
    HD_ITEMW = HDITEMW
    HD_ITEM = HDITEM

    HDITEMA_V1_SIZE = CCSIZEOF_STRUCT(HDITEMA, "lParam")
    HDITEMW_V1_SIZE = CCSIZEOF_STRUCT(HDITEMW, "lParam")

    HD_TEXTFILTER = unicode(HD_TEXTFILTERW, HD_TEXTFILTERW)
    LPHD_TEXTFILTER = unicode(LPHD_TEXTFILTERW, LPHD_TEXTFILTERA)

    HDI_WIDTH = 0x0001
    HDI_HEIGHT = HDI_WIDTH
    HDI_TEXT = 0x0002
    HDI_FORMAT = 0x0004
    HDI_LPARAM = 0x0008
    HDI_BITMAP = 0x0010
    HDI_IMAGE = 0x0020
    HDI_DI_SETITEM = 0x0040
    HDI_ORDER = 0x0080
    HDI_FILTER = 0x0100
    HDI_STATE = 0x0200
    # HDF_ flags are shared with the listview control (LVCFMT_ flags)
    HDF_LEFT = 0x0000 # Same as LVCFMT_LEFT
    HDF_RIGHT = 0x0001 # Same as LVCFMT_RIGHT
    HDF_CENTER = 0x0002 # Same as LVCFMT_CENTER
    HDF_JUSTIFYMASK = 0x0003 # Same as LVCFMT_JUSTIFYMASK
    HDF_RTLREADING = 0x0004 # Same as LVCFMT_LEFT
    HDF_BITMAP = 0x2000
    HDF_STRING = 0x4000
    HDF_OWNERDRAW = 0x8000 # Same as LVCFMT_COL_HAS_IMAGES
    HDF_IMAGE = 0x0800 # Same as LVCFMT_IMAGE
    HDF_BITMAP_ON_RIGHT = 0x1000 # Same as LVCFMT_BITMAP_ON_RIGHT
    HDF_SORTUP = 0x0400
    HDF_SORTDOWN = 0x0200
    HDF_CHECKBOX = 0x0040
    HDF_CHECKED = 0x0080
    HDF_FIXEDWIDTH = 0x0100 # Can't resize the column; same as LVCFMT_FIXED_WIDTH
    HDF_SPLITBUTTON = 0x1000000 # Column is a split button; same as LVCFMT_SPLITBUTTON
    HDIS_FOCUSED = 0x00000001
    HDM_GETITEMCOUNT = (HDM_FIRST + 0)

    def Header_GetItemCount(hwndHD):
        return SendMessage(hwndHD, HDM_GETITEMCOUNT, 0, 0)
    
    HDM_INSERTITEMA = (HDM_FIRST + 1)
    HDM_INSERTITEMW = (HDM_FIRST + 10)
    HDM_INSERTITEM = unicode(HDM_INSERTITEMW, HDM_INSERTITEMA)

    def Header_InsertItem(hwndHD, i, phdi):
        return SendMessage(hwndHD, HDM_INSERTITEM, i, cast(phdi, PVOID).value)
    
    HDM_DELETEITEM = (HDM_FIRST + 2)

    def Header_DeleteItem(hwndHD, i):
        return SendMessage(hwndHD, HDM_DELETEITEM, i, 0)
    
    HDM_GETITEMA = (HDM_FIRST + 3)
    HDM_GETITEMW = (HDM_FIRST + 11)
    HDM_GETITEM = unicode(HDM_GETITEMW, HDM_GETITEMA)

    def Header_GetItem(hwndHD, i, phdi):
        return SendMessage(hwndHD, HDM_GETITEM, i, cast(phdi, PVOID).value)
    
    HDM_SETITEMA = (HDM_FIRST + 4)
    HDM_SETITEMW = (HDM_FIRST + 12)
    HDM_SETITEM = unicode(HDM_SETITEMW, HDM_SETITEMA)

    def Header_SetItem(hwndHD, i, phdi):
        return SendMessage(hwndHD, HDM_SETITEM, i, cast(phdi, PVOID).value)
    
    class _HD_LAYOUT(CStructure):
        _fields_ = [
            ("prc", PRECT),
            ("pwpos", PWINDOWPOS)
        ]
        prc: PRECT
        pwpos: IPointer[WINDOWPOS]
    HDLAYOUT = _HD_LAYOUT
    LPHDLAYOUT = POINTER(HDLAYOUT)

    HD_LAYOUT = HDLAYOUT

    HDM_LAYOUT = (HDM_FIRST + 5)

    def Header_Layout(hwndHD, playout):
        return SendMessage(hwndHD, HDM_LAYOUT, 0, cast(playout, PVOID).value)

    HHT_NOWHERE = 0x0001
    HHT_ONHEADER = 0x0002
    HHT_ONDIVIDER = 0x0004
    HHT_ONDIVOPEN = 0x0008
    HHT_ONFILTER = 0x0010
    HHT_ONFILTERBUTTON = 0x0020
    HHT_ABOVE = 0x0100
    HHT_BELOW = 0x0200
    HHT_TORIGHT = 0x0400
    HHT_TOLEFT = 0x0800
    HHT_ONITEMSTATEICON = 0x1000
    HHT_ONDROPDOWN = 0x2000
    HHT_ONOVERFLOW = 0x4000

    class _HD_HITTESTINFO(CStructure):
        _fields_ = [
            ("pt", POINT),
            ("flags", UINT),
            ("iItem", INT)
        ]
        pt: POINT
        flags: int
        iItem: int
    HDHITTESTINFO = _HD_HITTESTINFO
    LPHDHITTESTINFO = POINTER(HDHITTESTINFO)
    
    HD_HITTESTINFO = HDHITTESTINFO

    HDSIL_NORMAL = 0
    HDSIL_STATE = 1

    HDM_HITTEST = (HDM_FIRST + 6)

    HDM_GETITEMRECT = (HDM_FIRST + 7)

    def Header_GetItemRect(hwnd, iItem, lprc):
        return SendMessage(hwnd, HDM_GETITEMRECT, iItem, cast(lprc, PVOID).value)
    
    HDM_SETIMAGELIST = (HDM_FIRST + 8)

    def Header_SetImageList(hwnd, himl):
        return SendMessage(hwnd, HDM_SETIMAGELIST, HDSIL_NORMAL, cast(himl, PVOID).value)
    
    def Header_SetStateImageList(hwnd, himl):
        return SendMessage(hwnd, HDM_SETIMAGELIST, HDSIL_STATE, cast(himl, PVOID).value)

    HDM_GETIMAGELIST = (HDM_FIRST + 9)

    def Header_GetImageList(hwnd):
        return SendMessage(hwnd, HDM_GETIMAGELIST, HDSIL_NORMAL, 0)
    
    def Header_GetStateImageList(hwnd):
        return SendMessage(hwnd, HDM_GETIMAGELIST, HDSIL_STATE, 0)

    HDM_ORDERTOINDEX = (HDM_FIRST + 15)

    def Header_OrderToIndex(hwnd, i):
        return SendMessage(hwnd, HDM_ORDERTOINDEX, i, 0)

    HDM_CREATEDRAGIMAGE = (HDM_FIRST + 16)  # wparam = which item (by index)

    def Header_CreateDragImage(hwnd, i):
        return SendMessage(hwnd, HDM_CREATEDRAGIMAGE, i, 0)

    HDM_GETORDERARRAY = (HDM_FIRST + 17)

    def Header_GetOrderArray(hwnd, iCount, lpi):
        return SendMessage(hwnd, HDM_GETORDERARRAY, iCount, cast(lpi, PVOID).value)

    HDM_SETORDERARRAY = (HDM_FIRST + 18)

    def Header_SetOrderArray(hwnd, iCount, lpi):
        return SendMessage(hwnd, HDM_SETORDERARRAY, iCount, cast(lpi, PVOID).value)
    
    # lparam = int array of size HDM_GETITEMCOUNT
    # the array specifies the order that all items should be displayed.
    # e.g.  { 2, 0, 1}
    # says the index 2 item should be shown in the 0ths position
    #      index 0 should be shown in the 1st position
    #      index 1 should be shown in the 2nd position


    HDM_SETHOTDIVIDER = (HDM_FIRST + 19)

    def Header_SetHotDivider(hwnd, fPos, dw):
        return SendMessage(hwnd, HDM_SETHOTDIVIDER, fPos, dw)
    
    # convenience message for external dragdrop
    # wParam = BOOL  specifying whether the lParam is a dwPos of the cursor
    #              position or the index of which divider to hotlight
    # lParam = depends on wParam  (-1 and wParm = FALSE turns off hotlight)

    HDM_SETBITMAPMARGIN = (HDM_FIRST + 20)

    def Header_SetBitmapMargin(hwnd, iWidth):
        return SendMessage(hwnd, HDM_SETBITMAPMARGIN, iWidth, 0)

    HDM_GETBITMAPMARGIN = (HDM_FIRST + 21)

    def Header_GetBitmapMargin(hwnd):
        return SendMessage(hwnd, HDM_GETBITMAPMARGIN, 0, 0)

    HDM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT

    def Header_SetUnicodeFormat(hwnd, fUnicode):
        return SendMessage(hwnd, HDM_SETUNICODEFORMAT, fUnicode, 0)

    HDM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT

    def Header_GetUnicodeFormat(hwnd):
        return SendMessage(hwnd, HDM_GETUNICODEFORMAT, 0, 0)
    
    HDM_SETFILTERCHANGETIMEOUT = (HDM_FIRST+22)

    def Header_SetFilterChangeTimeout(hwnd, i):
        return SendMessage(hwnd, HDM_SETFILTERCHANGETIMEOUT, 0, i)

    HDM_EDITFILTER = (HDM_FIRST+23)

    def Header_EditFilter(hwnd, i, fDiscardChanges):
        return SendMessage(hwnd, HDM_EDITFILTER, i, MAKELPARAM(fDiscardChanges, 0))

    # Clear filter takes -1 as a column value to indicate that all
    # the filter should be cleared.  When this happens you will
    # only receive a single filter changed notification.

    HDM_CLEARFILTER = (HDM_FIRST+24)

    def Header_ClearFilter(hwnd, i):
        return SendMessage(hwnd, HDM_CLEARFILTER, i, 0)
    
    def Header_ClearAllFilters(hwnd):
        return SendMessage(hwnd, HDM_CLEARFILTER, -1, 0)
    
    HDM_GETITEMDROPDOWNRECT = (HDM_FIRST+25)  # rect of item's drop down button

    def Header_GetItemDropDownRect(hwnd, iItem, lprc):
        return SendMessage(hwnd, HDM_GETITEMDROPDOWNRECT, iItem, cast(lprc, PVOID).value)

    HDM_GETOVERFLOWRECT = (HDM_FIRST+26)  # rect of overflow button

    def Header_GetOverflowRect(hwnd, lprc):
        return SendMessage(hwnd, HDM_GETOVERFLOWRECT, 0, cast(lprc, PVOID).value)

    HDM_GETFOCUSEDITEM = (HDM_FIRST+27)

    def Header_GetFocusedItem(hwnd):
        return SendMessage(hwnd, HDM_GETFOCUSEDITEM, 0, 0)

    HDM_SETFOCUSEDITEM = (HDM_FIRST+28)

    def Header_SetFocusedItem(hwnd, iItem):
        return SendMessage(hwnd, HDM_SETFOCUSEDITEM, 0, iItem)
    
    HDN_ITEMCHANGINGA = (HDN_FIRST-0)
    HDN_ITEMCHANGINGW = (HDN_FIRST-20)
    HDN_ITEMCHANGEDA = (HDN_FIRST-1)
    HDN_ITEMCHANGEDW = (HDN_FIRST-21)
    HDN_ITEMCLICKA = (HDN_FIRST-2)
    HDN_ITEMCLICKW = (HDN_FIRST-22)
    HDN_ITEMDBLCLICKA = (HDN_FIRST-3)
    HDN_ITEMDBLCLICKW = (HDN_FIRST-23)
    HDN_DIVIDERDBLCLICKA = (HDN_FIRST-5)
    HDN_DIVIDERDBLCLICKW = (HDN_FIRST-25)
    HDN_BEGINTRACKA = (HDN_FIRST-6)
    HDN_BEGINTRACKW = (HDN_FIRST-26)
    HDN_ENDTRACKA = (HDN_FIRST-7)
    HDN_ENDTRACKW = (HDN_FIRST-27)
    HDN_TRACKA = (HDN_FIRST-8)
    HDN_TRACKW = (HDN_FIRST-28)
    HDN_GETDISPINFOA = (HDN_FIRST-9)
    HDN_GETDISPINFOW = (HDN_FIRST-29)
    HDN_BEGINDRAG = (HDN_FIRST-10)
    HDN_ENDDRAG = (HDN_FIRST-11)
    HDN_FILTERCHANGE = (HDN_FIRST-12)
    HDN_FILTERBTNCLICK = (HDN_FIRST-13)
    HDN_BEGINFILTEREDIT = (HDN_FIRST-14)
    HDN_ENDFILTEREDIT = (HDN_FIRST-15)
    HDN_ITEMSTATEICONCLICK = (HDN_FIRST-16)
    HDN_ITEMKEYDOWN = (HDN_FIRST-17)
    HDN_DROPDOWN = (HDN_FIRST-18)
    HDN_OVERFLOWCLICK = (HDN_FIRST-19)
    HDN_ITEMCHANGING = unicode(HDN_ITEMCHANGINGW, HDN_ITEMCHANGINGA)
    HDN_ITEMCHANGED = unicode(HDN_ITEMCHANGEDW, HDN_ITEMCHANGEDA)
    HDN_ITEMCLICK = unicode(HDN_ITEMCLICKW, HDN_ITEMCLICKA)
    HDN_ITEMDBLCLICK = unicode(HDN_ITEMDBLCLICKW, HDN_ITEMDBLCLICKA)
    HDN_DIVIDERDBLCLICK = unicode(HDN_DIVIDERDBLCLICKW, HDN_DIVIDERDBLCLICKA)
    HDN_BEGINTRACK = unicode(HDN_BEGINTRACKW, HDN_BEGINTRACKA)
    HDN_ENDTRACK = unicode(HDN_ENDTRACKW, HDN_ENDTRACKA)
    HDN_TRACK = unicode(HDN_TRACKW, HDN_TRACKA)
    HDN_GETDISPINFO = unicode(HDN_GETDISPINFOW, HDN_GETDISPINFOA)
    class tagNMHEADERA(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("iItem", INT),
            ("iButton", INT),
            ("pItem", LPHDITEMA)
        ]
        hdr: int
        iItem: int
        iButton: int
        pItem: IPointer[HDITEMA]
    NMHEADERA = tagNMHEADERA
    LPNMHEADERA = POINTER(NMHEADERA)

    class tagNMHEADERW(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("iItem", INT),
            ("iButton", INT),
            ("pItem", LPHDITEMW)
        ]
        hdr: int
        iItem: int
        iButton: int
        pItem: IPointer[HDITEMW]
    NMHEADERW = tagNMHEADERW
    LPNMHEADERW = POINTER(NMHEADERW)

    NMHEADER = unicode(NMHEADERW, NMHEADERA)
    LPNMHEADER = unicode(LPNMHEADERW, LPNMHEADERA)

    HD_NOTIFYA = NMHEADERA
    HD_NOTIFYW = NMHEADERW
    HD_NOTIFY = NMHEADER

    #====== TOOLBAR CONTROL ======================================================
    if cpreproc.ifndef("NOTOOLBAR"):
        if cpreproc.ifdef("_WIN32"):
            TOOLBARCLASSNAMEW = u"ToolbarWindow32"
            TOOLBARCLASSNAMEA = "ToolbarWindow32"
            TOOLBARCLASSNAME = unicode(TOOLBARCLASSNAMEW, TOOLBARCLASSNAMEA)
        else:
            TOOLBARCLASSNAME = "ToolbarWindow"
        if cpreproc.ifdef("_WIN64"):
            _padding = 6 # padding for alignment
        else:
            _padding = 2 # padding for alignment
        class _TBBUTTON(CStructure):
            _fields_ = [
                ("iBitmap", INT),
                ("idCommand", INT),
                ("fsState", BYTE),
                ("fsStyle", BYTE),
                ("bReserved", BYTE * _padding),
                ("dwData", DWORD_PTR),
                ("iString", INT_PTR)
            ]
            iBitmap: int
            idCommand: int
            fsState: int
            fsStyle: int
            bReserved: IArray[int]
            dwData: int
            iString: int
        TBBUTTON = _TBBUTTON
        PTBBUTTON = POINTER(TBBUTTON)
        LPTBBUTTON = PTBBUTTON
        LPCTBBUTTON = PTBBUTTON


        class _COLORMAP(CStructure):
            _fields_ = [
                ("from_", COLORREF),
                ("to", COLORREF)
            ]
            from_: int
            to: int
        COLORMAP = _COLORMAP
        LPCOLORMAP = POINTER(COLORMAP)

        CreateToolbarEx = declare(comctl32.CreateToolbarEx, HWND, HWND, DWORD, UINT, INT, HINSTANCE, UINT_PTR, LPCTBBUTTON, INT, INT, INT, INT, INT, UINT)
        CreateMappedBitmap = declare(comctl32.CreateMappedBitmap, HBITMAP, HINSTANCE, INT_PTR, UINT, LPCOLORMAP, INT)

        CMB_MASKED = 0x02
        TBSTATE_CHECKED = 0x01
        TBSTATE_PRESSED = 0x02
        TBSTATE_ENABLED = 0x04
        TBSTATE_HIDDEN = 0x08
        TBSTATE_INDETERMINATE = 0x10
        TBSTATE_WRAP = 0x20
        TBSTATE_ELLIPSES = 0x40
        TBSTATE_MARKED = 0x80
        # begin_r_commctrl
        TBSTYLE_BUTTON = 0x0000 # obsolete; use BTNS_BUTTON instead
        TBSTYLE_SEP = 0x0001 # obsolete; use BTNS_SEP instead
        TBSTYLE_CHECK = 0x0002 # obsolete; use BTNS_CHECK instead
        TBSTYLE_GROUP = 0x0004 # obsolete; use BTNS_GROUP instead
        TBSTYLE_CHECKGROUP = (TBSTYLE_GROUP | TBSTYLE_CHECK) # obsolete; use BTNS_CHECKGROUP instead
        TBSTYLE_DROPDOWN = 0x0008 # obsolete; use BTNS_DROPDOWN instead
        TBSTYLE_AUTOSIZE = 0x0010 # obsolete; use BTNS_AUTOSIZE instead
        TBSTYLE_NOPREFIX = 0x0020 # obsolete; use BTNS_NOPREFIX instead
        TBSTYLE_TOOLTIPS = 0x0100
        TBSTYLE_WRAPABLE = 0x0200
        TBSTYLE_ALTDRAG = 0x0400
        TBSTYLE_FLAT = 0x0800
        TBSTYLE_LIST = 0x1000
        TBSTYLE_CUSTOMERASE = 0x2000
        TBSTYLE_REGISTERDROP = 0x4000
        TBSTYLE_TRANSPARENT = 0x8000
        # end_r_commctrl
        TBSTYLE_EX_DRAWDDARROWS = 0x00000001
        # begin_r_commctrl
        BTNS_BUTTON = TBSTYLE_BUTTON # 0x0000
        BTNS_SEP = TBSTYLE_SEP # 0x0001
        BTNS_CHECK = TBSTYLE_CHECK # 0x0002
        BTNS_GROUP = TBSTYLE_GROUP # 0x0004
        BTNS_CHECKGROUP = TBSTYLE_CHECKGROUP # (TBSTYLE_GROUP | TBSTYLE_CHECK)
        BTNS_DROPDOWN = TBSTYLE_DROPDOWN # 0x0008
        BTNS_AUTOSIZE = TBSTYLE_AUTOSIZE # 0x0010; automatically calculate the cx of the button
        BTNS_NOPREFIX = TBSTYLE_NOPREFIX # 0x0020; this button should not have accel prefix
        BTNS_SHOWTEXT = 0x0040 # ignored unless TBSTYLE_EX_MIXEDBUTTONS is set
        BTNS_WHOLEDROPDOWN = 0x0080 # draw drop-down arrow, but without split arrow section
        # end_r_commctrl
        TBSTYLE_EX_MIXEDBUTTONS = 0x00000008
        TBSTYLE_EX_HIDECLIPPEDBUTTONS = 0x00000010 # don't show partially obscured buttons
        TBSTYLE_EX_MULTICOLUMN = 0x00000002 # conflicts w/ TBSTYLE_WRAPABLE
        TBSTYLE_EX_VERTICAL = 0x00000004
        TBSTYLE_EX_DOUBLEBUFFER = 0x00000080 # Double Buffer the toolbar

        # Custom Draw Structure
        class _NMTBCUSTOMDRAW(CStructure):
            _fields_ = [
                ("nmcd", NMCUSTOMDRAW),
                ("hbrMonoDither", HBRUSH),
                ("hbrLines", HBRUSH), # For drawing lines on buttons
                ("hpenLines", HPEN), # For drawing lines on buttons
                ("clrText", COLORREF), # Color of text
                ("clrMark", COLORREF), # Color of text bk when marked. (only if TBSTATE_MARKED)
                ("clrTextHighlight", COLORREF), # Color of text when highlighted
                ("clrBtnFace", COLORREF), # Background of the button
                ("clrBtnHighlight", COLORREF), # 3D highlight
                ("clrHighlightHotTrack", COLORREF), # In conjunction with fHighlightHotTrack
                                                    # will cause button to highlight like a menu
                ("rcText", RECT), # Rect for text
                ("nStringBkMode", INT),
                ("nHLStringBkMode", INT)
            ]
            if cpreproc.get_version() >= WIN32_WINNT_WINXP:
                _fields_.append(("iListGap", INT))
            nmcd: NMCUSTOMDRAW
            hbrMonoDither: int
            hbrLines: int
            hpenLines: int
            clrText: int
            clrMark: int
            clrTextHighlight: int
            clrBtnFace: int
            clrBtmHighlight: int
            clrHighlightHotTrack: int
            rcText: int
            nStringBkMode: int
            nHLStringBkMode: int
            iListGap: int
        NMTBCUSTOMDRAW = _NMTBCUSTOMDRAW
        LPNMTBCUSTOMDRAW = POINTER(NMTBCUSTOMDRAW)
        
        # Toolbar custom draw return flags
        TBCDRF_NOEDGES = 0x00010000 # Don't draw button edges
        TBCDRF_HILITEHOTTRACK = 0x00020000 # Use color of the button bk when hottracked
        TBCDRF_NOOFFSET = 0x00040000 # Don't offset button if pressed
        TBCDRF_NOMARK = 0x00080000 # Don't draw default highlight of image/text for TBSTATE_MARKED
        TBCDRF_NOETCHEDEFFECT = 0x00100000 # Don't draw etched effect for disabled items
        TBCDRF_BLENDICON = 0x00200000 # Use ILD_BLEND50 on the icon image
        TBCDRF_NOBACKGROUND = 0x00400000 # Use ILD_BLEND50 on the icon image
        TBCDRF_USECDCOLORS = 0x00800000 # Use CustomDrawColors to RenderText regardless of VisualStyle
        TB_ENABLEBUTTON = (WM_USER + 1)
        TB_CHECKBUTTON = (WM_USER + 2)
        TB_PRESSBUTTON = (WM_USER + 3)
        TB_HIDEBUTTON = (WM_USER + 4)
        TB_INDETERMINATE = (WM_USER + 5)
        TB_MARKBUTTON = (WM_USER + 6)
        TB_ISBUTTONENABLED = (WM_USER + 9)
        TB_ISBUTTONCHECKED = (WM_USER + 10)
        TB_ISBUTTONPRESSED = (WM_USER + 11)
        TB_ISBUTTONHIDDEN = (WM_USER + 12)
        TB_ISBUTTONINDETERMINATE = (WM_USER + 13)
        TB_ISBUTTONHIGHLIGHTED = (WM_USER + 14)
        TB_SETSTATE = (WM_USER + 17)
        TB_GETSTATE = (WM_USER + 18)
        TB_ADDBITMAP = (WM_USER + 19)

        class tagTBADDBITMAP(CStructure):
            _fields_ = [
                ("hInst", HINSTANCE),
                ("nID", UINT_PTR)
            ]
            hInst: int
            nID: int
        TBADDBITMAP = tagTBADDBITMAP
        LPTBADDBITMAP = POINTER(TBADDBITMAP)

        HINST_COMMCTRL = HINSTANCE(-1)
        IDB_STD_SMALL_COLOR = 0
        IDB_STD_LARGE_COLOR = 1
        IDB_VIEW_SMALL_COLOR = 4
        IDB_VIEW_LARGE_COLOR = 5
        IDB_HIST_SMALL_COLOR = 8
        IDB_HIST_LARGE_COLOR = 9
        IDB_HIST_NORMAL = 12
        IDB_HIST_HOT = 13
        IDB_HIST_DISABLED = 14
        IDB_HIST_PRESSED = 15
        # icon indexes for standard bitmap
        STD_CUT = 0
        STD_COPY = 1
        STD_PASTE = 2
        STD_UNDO = 3
        STD_REDOW = 4
        STD_DELETE = 5
        STD_FILENEW = 6
        STD_FILEOPEN = 7
        STD_FILESAVE = 8
        STD_PRINTPRE = 9
        STD_PROPERTIES = 10
        STD_HELP = 11
        STD_FIND = 12
        STD_REPLACE = 13
        STD_PRINT = 14
        # icon indexes for standard view bitmap
        VIEW_LARGEICONS = 0
        VIEW_SMALLICONS = 1
        VIEW_LIST = 2
        VIEW_DETAILS = 3
        VIEW_SORTNAME = 4
        VIEW_SORTSIZE = 5
        VIEW_SORTDATE = 6
        VIEW_SORTTYPE = 7
        VIEW_PARENTFOLDER = 8
        VIEW_NETCONNECT = 9
        VIEW_NETDISCONNECT = 10
        VIEW_NEWFOLDER = 11
        VIEW_VIEWMENU = 12
        HIST_BACK = 0
        HIST_FORWARD = 1
        HIST_FAVORITES = 2
        HIST_ADDTOFAVORITES = 3
        HIST_VIEWTREE = 4
        TB_ADDBUTTONSA = (WM_USER + 20)
        TB_INSERTBUTTONA = (WM_USER + 21)
        TB_DELETEBUTTON = (WM_USER + 22)
        TB_GETBUTTON = (WM_USER + 23)
        TB_BUTTONCOUNT = (WM_USER + 24)
        TB_COMMANDTOINDEX = (WM_USER + 25)

        class tagTBSAVEPARAMSA(CStructure):
            _fields_ = [
                ("hkr", HKEY),
                ("pszSubKey", LPCSTR),
                ("pszValueName", LPCSTR)
            ]
            hkr: int
            pszSubKey: LPCSTR
            pszValueName: LPCSTR
        TBSAVEPARAMSA = tagTBSAVEPARAMSA
        LPTBSAVEPARAMSA = POINTER(TBSAVEPARAMSA)
        
        class tagTBSAVEPARAMSW(CStructure):
            _fields_ = [
                ("hkr", HKEY),
                ("pszSubKey", LPCWSTR),
                ("pszValueName", LPCWSTR)
            ]
            hkr: int
            pszSubKey: LPCWSTR
            pszValueName: LPCWSTR
        TBSAVEPARAMSW = tagTBSAVEPARAMSW
        LPTBSAVEPARAMSW = POINTER(TBSAVEPARAMSW)

        TBSAVEPARAMS = unicode(TBSAVEPARAMSW, TBSAVEPARAMSA)
        LPTBSAVEPARAMS = unicode(LPTBSAVEPARAMSW, LPTBSAVEPARAMSA)

        TB_SAVERESTOREA = (WM_USER + 26)
        TB_SAVERESTOREW = (WM_USER + 76)
        TB_CUSTOMIZE = (WM_USER + 27)
        TB_ADDSTRINGA = (WM_USER + 28)
        TB_ADDSTRINGW = (WM_USER + 77)
        TB_GETITEMRECT = (WM_USER + 29)
        TB_BUTTONSTRUCTSIZE = (WM_USER + 30)
        TB_SETBUTTONSIZE = (WM_USER + 31)
        TB_SETBITMAPSIZE = (WM_USER + 32)
        TB_AUTOSIZE = (WM_USER + 33)
        TB_GETTOOLTIPS = (WM_USER + 35)
        TB_SETTOOLTIPS = (WM_USER + 36)
        TB_SETPARENT = (WM_USER + 37)
        TB_SETROWS = (WM_USER + 39)
        TB_GETROWS = (WM_USER + 40)
        TB_SETCMDID = (WM_USER + 42)
        TB_CHANGEBITMAP = (WM_USER + 43)
        TB_GETBITMAP = (WM_USER + 44)
        TB_GETBUTTONTEXTA = (WM_USER + 45)
        TB_GETBUTTONTEXTW = (WM_USER + 75)
        TB_REPLACEBITMAP = (WM_USER + 46)
        TB_SETINDENT = (WM_USER + 47)
        TB_SETIMAGELIST = (WM_USER + 48)
        TB_GETIMAGELIST = (WM_USER + 49)
        TB_LOADIMAGES = (WM_USER + 50)
        TB_GETRECT = (WM_USER + 51) # wParam is the Cmd instead of index
        TB_SETHOTIMAGELIST = (WM_USER + 52)
        TB_GETHOTIMAGELIST = (WM_USER + 53)
        TB_SETDISABLEDIMAGELIST = (WM_USER + 54)
        TB_GETDISABLEDIMAGELIST = (WM_USER + 55)
        TB_SETSTYLE = (WM_USER + 56)
        TB_GETSTYLE = (WM_USER + 57)
        TB_GETBUTTONSIZE = (WM_USER + 58)
        TB_SETBUTTONWIDTH = (WM_USER + 59)
        TB_SETMAXTEXTROWS = (WM_USER + 60)
        TB_GETTEXTROWS = (WM_USER + 61)
        TB_GETBUTTONTEXT = unicode(TB_GETBUTTONTEXTW, TB_GETBUTTONTEXTA)
        TB_SAVERESTORE = unicode(TB_SAVERESTOREW, TB_SAVERESTOREA)
        TB_ADDSTRING = unicode(TB_ADDSTRINGW, TB_ADDSTRINGA)
        TB_GETOBJECT = (WM_USER + 62) # wParam == IID, lParam void **ppv
        TB_GETHOTITEM = (WM_USER + 71)
        TB_SETHOTITEM = (WM_USER + 72) # wParam == iHotItem
        TB_SETANCHORHIGHLIGHT = (WM_USER + 73) # wParam == TRUE/FALSE
        TB_GETANCHORHIGHLIGHT = (WM_USER + 74)
        TB_MAPACCELERATORA = (WM_USER + 78) # wParam == ch, lParam int * pidBtn

        class TBINSERTMARK(CStructure):
            _fields_ = [
                ("iButton", INT),
                ("dwFlags", DWORD)
            ]
            iButton: int
            dwFlags: int
        LPTBINSERTMARK = POINTER(TBINSERTMARK)

        TBIMHT_AFTER = 0x00000001 # TRUE = insert After iButton, otherwise before
        TBIMHT_BACKGROUND = 0x00000002 # TRUE iff missed buttons completely
        TB_GETINSERTMARK = (WM_USER + 79) # lParam == LPTBINSERTMARK
        TB_SETINSERTMARK = (WM_USER + 80) # lParam == LPTBINSERTMARK
        TB_INSERTMARKHITTEST = (WM_USER + 81) # wParam == LPPOINT lParam == LPTBINSERTMARK
        TB_MOVEBUTTON = (WM_USER + 82)
        TB_GETMAXSIZE = (WM_USER + 83) # lParam == LPSIZE
        TB_SETEXTENDEDSTYLE = (WM_USER + 84) # For TBSTYLE_EX_*
        TB_GETEXTENDEDSTYLE = (WM_USER + 85) # For TBSTYLE_EX_*
        TB_GETPADDING = (WM_USER + 86)
        TB_SETPADDING = (WM_USER + 87)
        TB_SETINSERTMARKCOLOR = (WM_USER + 88)
        TB_GETINSERTMARKCOLOR = (WM_USER + 89)
        TB_SETCOLORSCHEME = CCM_SETCOLORSCHEME # lParam is color scheme
        TB_GETCOLORSCHEME = CCM_GETCOLORSCHEME # fills in COLORSCHEME pointed to by lParam
        TB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        TB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        TB_MAPACCELERATORW = (WM_USER + 90) # wParam == ch, lParam int * pidBtn
        TB_MAPACCELERATOR = unicode(TB_MAPACCELERATORW, TB_MAPACCELERATORA)

        class TBREPLACEBITMAP(CStructure):
            _fields_ = [
                ("hInstOld", HINSTANCE),
                ("nIDOld", UINT_PTR),
                ("hInstNew", HINSTANCE),
                ("nIDNew", UINT_PTR),
                ("nButtons", INT)
            ]
            hInstOld: int
            nIDOld: int
            hInstNew: int
            nIDNew: int
            nButtons: int
        LPTBREPLACEBITMAP = POINTER(TBREPLACEBITMAP)

        TBBF_LARGE = 0x0001
        TB_GETBITMAPFLAGS = (WM_USER + 41)
        TBIF_IMAGE = 0x00000001
        TBIF_TEXT = 0x00000002
        TBIF_STATE = 0x00000004
        TBIF_STYLE = 0x00000008
        TBIF_LPARAM = 0x00000010
        TBIF_COMMAND = 0x00000020
        TBIF_SIZE = 0x00000040
        TBIF_BYINDEX = 0x80000000 # this specifies that the wparam in Get/SetButtonInfo is an index, not id

        class TBBUTTONINFOA(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("dwMask", DWORD),
                ("idCommand", INT),
                ("iImage", INT),
                ("fsState", BYTE),
                ("fsStyle", BYTE),
                ("cx", WORD),
                ("lParam", DWORD_PTR),
                ("pszText", LPSTR),
                ("cchText", INT)
            ]
            cbSize: int
            dwMask: int
            idCommand: int
            iImage: int
            fsState: int
            fsStyle: int
            cx: int
            lParam: int
            pszText: LPSTR
            cchText: int
        LPTBBUTTONINFOA = POINTER(TBBUTTONINFOA)

        class TBBUTTONINFOW(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("dwMask", DWORD),
                ("idCommand", INT),
                ("iImage", INT),
                ("fsState", BYTE),
                ("fsStyle", BYTE),
                ("cx", WORD),
                ("lParam", DWORD_PTR),
                ("pszText", LPWSTR),
                ("cchText", INT)
            ]
            cbSize: int
            dwMask: int
            idCommand: int
            iImage: int
            fsState: int
            fsStyle: int
            cx: int
            lParam: int
            pszText: LPWSTR
            cchText: int
        LPTBBUTTONINFOW = POINTER(TBBUTTONINFOW)

        TBBUTTONINFOW = unicode(TBBUTTONINFOW, TBBUTTONINFOA)
        LPTBBUTTONINFO = unicode(LPTBBUTTONINFOW, LPTBBUTTONINFOA)

        # BUTTONINFO APIs do NOT support the string pool.
        TB_GETBUTTONINFOW = (WM_USER + 63)
        TB_SETBUTTONINFOW = (WM_USER + 64)
        TB_GETBUTTONINFOA = (WM_USER + 65)
        TB_SETBUTTONINFOA = (WM_USER + 66)
        TB_GETBUTTONINFO = unicode(TB_GETBUTTONINFOW, TB_GETBUTTONINFOA)
        TB_SETBUTTONINFO = unicode(TB_SETBUTTONINFOW, TB_SETBUTTONINFOA)
        TB_INSERTBUTTONW = (WM_USER + 67)
        TB_ADDBUTTONSW = (WM_USER + 68)
        TB_HITTEST = (WM_USER + 69)
        # New post Win95/NT4 for InsertButton and AddButton.  if iString member
        # is a pointer to a string, it will be handled as a string like listview
        # (although LPSTR_TEXTCALLBACK is not supported).
        TB_INSERTBUTTON = unicode(TB_INSERTBUTTONW, TB_INSERTBUTTONA)
        TB_ADDBUTTONS = unicode(TB_ADDBUTTONSW, TB_ADDBUTTONSA)
        TB_SETDRAWTEXTFLAGS = (WM_USER + 70) # wParam == mask lParam == bit values
        TB_GETSTRINGW = (WM_USER + 91)
        TB_GETSTRINGA = (WM_USER + 92)
        TB_GETSTRING = unicode(TB_GETSTRINGW, TB_GETSTRINGA)
        TB_SETBOUNDINGSIZE = (WM_USER + 93)
        TB_SETHOTITEM2 = (WM_USER + 94) # wParam == iHotItem,  lParam = dwFlags
        TB_HASACCELERATOR = (WM_USER + 95) # wParam == char, lParam = &iCount
        TB_SETLISTGAP = (WM_USER + 96)
        TB_GETIMAGELISTCOUNT = (WM_USER + 98)
        TB_GETIDEALSIZE = (WM_USER + 99) # wParam == fHeight, lParam = psize
        # before using WM_USER + 103, recycle old space above (WM_USER + 97)
        TBMF_PAD = 0x00000001
        TBMF_BARPAD = 0x00000002
        TBMF_BUTTONSPACING = 0x00000004

        class TBMETRICS(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("dwMask", DWORD),
                ("cxPad", INT), # PAD
                ("cyPad", INT), 
                ("cxBarPad", INT), # BARPAD
                ("cyBarPad", INT),
                ("cxButtonSpacing", INT), # BUTTONSPACING
                ("cyButtonSpacing", INT)
            ]
            cbSize: int
            dwMask: int
            cxPad: int
            cyPad: int
            cxBarPad: int
            cyBarPad: int
            cxButtonSpacing: int
            cyButtonSpacing: int
        LPTBMETRICS = POINTER(TBMETRICS)

        TB_GETMETRICS = (WM_USER + 101)
        TB_SETMETRICS = (WM_USER + 102)
        TB_GETITEMDROPDOWNRECT = (WM_USER + 103) # Rect of item's drop down button
        TB_SETPRESSEDIMAGELIST = (WM_USER + 104)
        TB_GETPRESSEDIMAGELIST = (WM_USER + 105)
        TB_SETWINDOWTHEME = CCM_SETWINDOWTHEME
        TBN_GETBUTTONINFOA = (TBN_FIRST-0)
        TBN_BEGINDRAG = (TBN_FIRST-1)
        TBN_ENDDRAG = (TBN_FIRST-2)
        TBN_BEGINADJUST = (TBN_FIRST-3)
        TBN_ENDADJUST = (TBN_FIRST-4)
        TBN_RESET = (TBN_FIRST-5)
        TBN_QUERYINSERT = (TBN_FIRST-6)
        TBN_QUERYDELETE = (TBN_FIRST-7)
        TBN_TOOLBARCHANGE = (TBN_FIRST-8)
        TBN_CUSTHELP = (TBN_FIRST-9)
        TBN_DROPDOWN = (TBN_FIRST - 10)
        TBN_GETOBJECT = (TBN_FIRST - 12)
        # Structure for TBN_HOTITEMCHANGE notification
        class tagNMTBHOTITEM(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("idOld", INT),
                ("idNew", INT),
                ("dwFlags", DWORD) # HICF_*
            ]
            hdr: NMHDR
            idOld: int
            idNew: int
            dwFlags: int
        NMTBHOTITEM = tagNMTBHOTITEM
        LPNMTBHOTITEM = POINTER(NMTBHOTITEM)

        # Hot item change flags
        HICF_OTHER = 0x00000000
        HICF_MOUSE = 0x00000001 # Triggered by mouse
        HICF_ARROWKEYS = 0x00000002 # Triggered by arrow keys
        HICF_ACCELERATOR = 0x00000004 # Triggered by accelerator
        HICF_DUPACCEL = 0x00000008 # This accelerator is not unique
        HICF_ENTERING = 0x00000010 # idOld is invalid
        HICF_LEAVING = 0x00000020 # idNew is invalid
        HICF_RESELECT = 0x00000040 # hot item reselected
        HICF_LMOUSE = 0x00000080 # left mouse button selected
        HICF_TOGGLEDROPDOWN = 0x00000100 # Toggle button's dropdown state
        TBN_HOTITEMCHANGE = (TBN_FIRST - 13)
        TBN_DRAGOUT = (TBN_FIRST - 14) # this is sent when the user clicks down on a button then drags off the button
        TBN_DELETINGBUTTON = (TBN_FIRST - 15) # uses TBNOTIFY
        TBN_GETDISPINFOA = (TBN_FIRST - 16) # This is sent when the  toolbar needs  some display information
        TBN_GETDISPINFOW = (TBN_FIRST - 17) # This is sent when the  toolbar needs  some display information
        TBN_GETINFOTIPA = (TBN_FIRST - 18)
        TBN_GETINFOTIPW = (TBN_FIRST - 19)
        TBN_GETBUTTONINFOW = (TBN_FIRST - 20)
        TBN_RESTORE = (TBN_FIRST - 21)
        TBN_SAVE = (TBN_FIRST - 22)
        TBN_INITCUSTOMIZE = (TBN_FIRST - 23)
        TBNRF_HIDEHELP = 0x00000001
        TBNRF_ENDCUSTOMIZE = 0x00000002
        TBN_WRAPHOTITEM = (TBN_FIRST - 24)
        TBN_DUPACCELERATOR = (TBN_FIRST - 25)
        TBN_WRAPACCELERATOR = (TBN_FIRST - 26)
        TBN_DRAGOVER = (TBN_FIRST - 27)
        TBN_MAPACCELERATOR = (TBN_FIRST - 28)

        class tagNMTBSAVE(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("pData", PDWORD),
                ("pCurrent", PDWORD),
                ("cbData", UINT),
                ("iItem", INT),
                ("cButtons", INT),
                ("tbButton", TBBUTTON)
            ]
            hdr: NMHDR
            pData: PDWORD
            pCurrent: PDWORD
            cbData: int
            iItem: int
            cButtons: int
            tbButton: TBBUTTON
        NMTBSAVE = tagNMTBSAVE
        LPNMTBSAVE = POINTER(NMTBSAVE)

        class tagNMTBRESTORE(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("pData", PDWORD),
                ("pCurrent", PDWORD),
                ("cbData", UINT),
                ("iItem", INT),
                ("cButtons", INT),
                ("cbBytesPerRecord", INT),
                ("tbButton", TBBUTTON)
            ]
            hdr: NMHDR
            pData: PDWORD
            pCurrent: PDWORD
            cbData: int
            iItem: int
            cButtons: int
            cbBytesPerRecord: int
            tbButton: TBBUTTON
        NMTBRESTORE = tagNMTBRESTORE
        LPNMTBRESTORE = POINTER(NMTBRESTORE)

        class tagNMTBGETINFOTIPA(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("pszText", LPSTR),
                ("cchTextMax", INT),
                ("iItem", INT),
                ("lParam", LPARAM)
            ]
            hdr: NMHDR
            pszText: LPSTR
            cchTextMax: int
            iItem: int
            lParam: int
        NMTBGETINFOTIPA = tagNMTBGETINFOTIPA
        LPNMTBGETINFOTIPA = POINTER(NMTBGETINFOTIPA)

        class tagNMTBGETINFOTIPW(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("pszText", LPWSTR),
                ("cchTextMax", INT),
                ("iItem", INT),
                ("lParam", LPARAM)
            ]
            hdr: NMHDR
            pszText: LPWSTR
            cchTextMax: int
            iItem: int
            lParam: int
        NMTBGETINFOTIPW = tagNMTBGETINFOTIPW
        LPNMTBGETINFOTIPW = POINTER(NMTBGETINFOTIPW)

        TBN_GETINFOTIP = unicode(TBN_GETINFOTIPW, TBN_GETINFOTIPA)
        NMTBGETINFOTIP = unicode(NMTBGETINFOTIPW, NMTBGETINFOTIPA)
        LPNMTBGETINFOTIP = unicode(LPNMTBGETINFOTIPW, LPNMTBGETINFOTIPA)

        TBNF_IMAGE  = 0x00000001
        TBNF_TEXT = 0x00000002
        TBNF_DI_SETITEM = 0x10000000

        class NMTBDISPINFOA(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("dwMask", DWORD), # [in] Specifies the values requested .[out] Client ask the data to be set for future use
                ("idCommand", INT), # [in] id of button we're requesting info for
                ("lParam", DWORD_PTR), # [in] lParam of button
                ("iImage", INT), # [out] image index
                ("pszText", LPSTR), # [out] new text for item
                ("cchText", INT) # [in] size of buffer pointed to by pszText
            ]
            hdr: NMHDR
            dwMask: int
            idCommand: int
            lParam: int
            iImage: int
            pszText: LPSTR
            cchText: int
        LPNMTBDISPINFOA = POINTER(NMTBDISPINFOA)

        class NMTBDISPINFOW(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("dwMask", DWORD), # [in] Specifies the values requested .[out] Client ask the data to be set for future use
                ("idCommand", INT), # [in] id of button we're requesting info for
                ("lParam", DWORD_PTR), # [in] lParam of button
                ("iImage", INT), # [out] image index
                ("pszText", LPWSTR), # [out] new text for item
                ("cchText", INT) # [in] size of buffer pointed to by pszText
            ]
            hdr: NMHDR
            dwMask: int
            idCommand: int
            lParam: int
            iImage: int
            pszText: LPWSTR
            cchText: int
        LPNMTBDISPINFOW = POINTER(NMTBDISPINFOW)

        TBN_GETDISPINFO = unicode(TBN_GETDISPINFOW, TBN_GETDISPINFOA)
        NMTBDISPINFO = unicode(NMTBDISPINFOW, NMTBDISPINFOA)
        LPNMTBDISPINFO = unicode(LPNMTBDISPINFOW, LPNMTBDISPINFOA)

        # Return codes for TBN_DROPDOWN
        TBDDRET_DEFAULT = 0
        TBDDRET_NODEFAULT = 1
        TBDDRET_TREATPRESSED = 2 # Treat as a standard press button
        TBN_GETBUTTONINFO = unicode(TBN_GETBUTTONINFOW, TBN_GETBUTTONINFOA)

        class tagNMTOOLBARA(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("iItem", INT),
                ("tbButton", TBBUTTON),
                ("cchText", INT),
                ("pszText", LPSTR),
                ("rcButton", RECT)
            ]
            hdr: NMHDR
            iItem: int
            tbButton: TBBUTTON
            cchText: int
            pszText: LPSTR
            rcButton: RECT
        NMTOOLBARA = tagNMTOOLBARA
        LPNMTOOLBARA = POINTER(NMTOOLBARA)

        class tagNMTOOLBARW(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("iItem", INT),
                ("tbButton", TBBUTTON),
                ("cchText", INT),
                ("pszText", LPWSTR),
                ("rcButton", RECT)
            ]
            hdr: NMHDR
            iItem: int
            tbButton: TBBUTTON
            cchText: int
            pszText: LPWSTR
            rcButton: RECT
        NMTOOLBARW = tagNMTOOLBARW
        LPNMTOOLBARW = POINTER(NMTOOLBARW)

        NMTOOLBAR = unicode(NMTOOLBARW, NMTOOLBARA)
        LPNMTOOLBAR = unicode(LPNMTOOLBARW, LPNMTOOLBARA)

        TBNOTIFYA = NMTOOLBARA
        TBNOTIFYW = NMTOOLBARW
        LPTBNOTIFYA = LPNMTOOLBARA
        LPTBNOTIFYW = LPNMTOOLBARW
        TBNOTIFY = NMTOOLBAR
        LPTBNOTIFY = LPNMTOOLBAR
    #====== REBAR CONTROL ========================================================
    if cpreproc.ifndef("NOREBAR"):
        if cpreproc.ifdef("_WIN32"):
            REBARCLASSNAMEW = u"ReBarWindow32"
            REBARCLASSNAMEA = "ReBarWindow32"
            REBARCLASSNAME = unicode(REBARCLASSNAMEW, REBARCLASSNAMEA)
        else:
            REBARCLASSNAME = "ReBarWindow"
        RBIM_IMAGELIST = 0x00000001
        # begin_r_commctrl
        RBS_TOOLTIPS = 0x00000100
        RBS_VARHEIGHT = 0x00000200
        RBS_BANDBORDERS = 0x00000400
        RBS_FIXEDORDER = 0x00000800
        RBS_REGISTERDROP = 0x00001000
        RBS_AUTOSIZE = 0x00002000
        RBS_VERTICALGRIPPER = 0x00004000 # this always has the vertical gripper (default for horizontal mode)
        RBS_DBLCLKTOGGLE = 0x00008000
        # end_r_commctrl
        class tagREBARINFO(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("fMask", UINT),
                ("himl", HANDLE)
            ]
            cbSize: int
            fMask: int
            himl: int
        REBARINFO = tagREBARINFO
        LPREBARINFO = POINTER(REBARINFO)

        RBBS_BREAK = 0x00000001 # break to new line
        RBBS_FIXEDSIZE = 0x00000002 # band can't be sized
        RBBS_CHILDEDGE = 0x00000004 # edge around top & bottom of child window
        RBBS_HIDDEN = 0x00000008 # don't show
        RBBS_NOVERT = 0x00000010 # don't show when vertical
        RBBS_FIXEDBMP = 0x00000020 # bitmap doesn't move during band resize
        RBBS_VARIABLEHEIGHT = 0x00000040 # allow autosizing of this child vertically
        RBBS_GRIPPERALWAYS = 0x00000080 # always show the gripper
        RBBS_NOGRIPPER = 0x00000100 # never show the gripper
        RBBS_USECHEVRON = 0x00000200 # display drop-down button for this band if it's sized smaller than ideal width
        RBBS_HIDETITLE = 0x00000400 # keep band title hidden
        RBBS_TOPALIGN = 0x00000800 # keep band in top row
        RBBIM_STYLE = 0x00000001
        RBBIM_COLORS = 0x00000002
        RBBIM_TEXT = 0x00000004
        RBBIM_IMAGE = 0x00000008
        RBBIM_CHILD = 0x00000010
        RBBIM_CHILDSIZE = 0x00000020
        RBBIM_SIZE = 0x00000040
        RBBIM_BACKGROUND = 0x00000080
        RBBIM_ID = 0x00000100
        RBBIM_IDEALSIZE = 0x00000200
        RBBIM_LPARAM = 0x00000400
        RBBIM_HEADERSIZE = 0x00000800 # control the size of the header
        RBBIM_CHEVRONLOCATION = 0x00001000
        RBBIM_CHEVRONSTATE = 0x00002000

        class tagREBARBANDINFOA(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("fMask", UINT),
                ("fStyle", UINT), 
                ("clrFore", COLORREF),
                ("clrBack", COLORREF),
                ("lpText", LPSTR),
                ("cch", UINT),
                ("iImage", INT),
                ("hwndChild", HWND),
                ("cxMinChild", UINT),
                ("cyMinChild", UINT),
                ("cx", UINT),
                ("hbmBack", HBITMAP),
                ("wID", UINT),
                ("cyChild", UINT),
                ("cyMaxChild", UINT),
                ("cyIntegral", UINT),
                ("cxIdeal", UINT), 
                ("lParam", LPARAM),
                ("cxHeader", UINT)
            ]
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                _fields_.extend([
                    ("rcChevronLocation", RECT), # the rect is in client co-ord wrt hwndChild
                    ("uChevronState", UINT) # STATE_SYSTEM_*
                ])
            cbSize: int
            fMask: int
            fStyle: int
            clrFore: int
            clrBack: int
            lpText: LPSTR
            cch: int
            iImage: int
            hwndChild: int
            cxMinChild: int
            cyMinChild: int
            cx: int
            hbmBack: int
            wID: int
            cyChild: int
            cyMaxChild: int
            cyIntegral: int
            cxIdeal: int
            lParam: int
            cxHeader: int
            rcChevronLocation: RECT
            uChevronState: int
        REBARBANDINFOA = tagREBARBANDINFOA
        LPREBARBANDINFOA = POINTER(REBARBANDINFOA)

        class tagREBARBANDINFOW(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("fMask", UINT),
                ("fStyle", UINT), 
                ("clrFore", COLORREF),
                ("clrBack", COLORREF),
                ("lpText", LPWSTR),
                ("cch", UINT),
                ("iImage", INT),
                ("hwndChild", HWND),
                ("cxMinChild", UINT),
                ("cyMinChild", UINT),
                ("cx", UINT),
                ("hbmBack", HBITMAP),
                ("wID", UINT),
                ("cyChild", UINT),
                ("cyMaxChild", UINT),
                ("cyIntegral", UINT),
                ("cxIdeal", UINT), 
                ("lParam", LPARAM),
                ("cxHeader", UINT),
                ("rcChevronLocation", RECT), # the rect is in client co-ord wrt hwndChild
                ("uChevronState", UINT), # STATE_SYSTEM_*
            ]
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                _fields_.extend([
                    ("rcChevronLocation", RECT), # the rect is in client co-ord wrt hwndChild
                    ("uChevronState", UINT) # STATE_SYSTEM_*
                ])
            cbSize: int
            fMask: int
            fStyle: int
            clrFore: int
            clrBack: int
            lpText: LPWSTR
            cch: int
            iImage: int
            hwndChild: int
            cxMinChild: int
            cyMinChild: int
            cx: int
            hbmBack: int
            wID: int
            cyChild: int
            cyMaxChild: int
            cyIntegral: int
            cxIdeal: int
            lParam: int
            cxHeader: int
            rcChevronLocation: RECT
            uChevronState: int
        REBARBANDINFOW = tagREBARBANDINFOW
        LPREBARBANDINFOW = POINTER(REBARBANDINFOW)

        REBARBANDINFOA_V3_SIZE = CCSIZEOF_STRUCT(REBARBANDINFOA, "wID")
        REBARBANDINFOW_V3_SIZE = CCSIZEOF_STRUCT(REBARBANDINFOW, "wID")

        REBARBANDINFOA_V6_SIZE = CCSIZEOF_STRUCT(REBARBANDINFOA, "cxHeader")
        REBARBANDINFOW_V6_SIZE = CCSIZEOF_STRUCT(REBARBANDINFOW, "cxHeader")

        REBARBANDINFO = unicode(REBARBANDINFOW, REBARBANDINFOA)
        LPREBARBANDINFO = unicode(LPREBARBANDINFOW, LPREBARBANDINFOA)
        LPCREBARBANDINFO = LPREBARBANDINFO
        REBARBANDINFO_V3_SIZE = unicode(REBARBANDINFOW_V3_SIZE, REBARBANDINFOA_V3_SIZE)
        REBARBANDINFO_V6_SIZE = unicode(REBARBANDINFOW_V6_SIZE, REBARBANDINFOA_V6_SIZE)

        RB_INSERTBANDA = (WM_USER + 1)
        RB_DELETEBAND = (WM_USER + 2)
        RB_GETBARINFO = (WM_USER + 3)
        RB_SETBARINFO = (WM_USER + 4)
        RB_SETBANDINFOA = (WM_USER + 6)
        RB_SETPARENT = (WM_USER + 7)
        RB_HITTEST = (WM_USER + 8)
        RB_GETRECT = (WM_USER + 9)
        RB_INSERTBANDW = (WM_USER + 10)
        RB_SETBANDINFOW = (WM_USER + 11)
        RB_GETBANDCOUNT = (WM_USER + 12)
        RB_GETROWCOUNT = (WM_USER + 13)
        RB_GETROWHEIGHT = (WM_USER + 14)
        RB_IDTOINDEX = (WM_USER + 16) # wParam == id
        RB_GETTOOLTIPS = (WM_USER + 17)
        RB_SETTOOLTIPS = (WM_USER + 18)
        RB_SETBKCOLOR = (WM_USER + 19) # sets the default BK color
        RB_GETBKCOLOR = (WM_USER + 20) # defaults to CLR_NONE
        RB_SETTEXTCOLOR = (WM_USER + 21)
        RB_GETTEXTCOLOR = (WM_USER + 22) # defaults to 0x00000000
        RBSTR_CHANGERECT = 0x0001 # flags for RB_SIZETORECT
        RB_SIZETORECT = (WM_USER + 23) # resize the rebar/break bands and such to this rect (lparam)
        RB_SETCOLORSCHEME = CCM_SETCOLORSCHEME # lParam is color scheme
        RB_GETCOLORSCHEME = CCM_GETCOLORSCHEME # fills in COLORSCHEME pointed to by lParam
        RB_INSERTBAND = unicode(RB_INSERTBANDW, RB_INSERTBANDA)
        RB_SETBANDINFO = unicode(RB_SETBANDINFOW, RB_SETBANDINFOA)
        # for manual drag control
        # lparam == cursor pos
        # -1 means do it yourself.
        # -2 means use what you had saved before
        RB_BEGINDRAG = (WM_USER + 24)
        RB_ENDDRAG = (WM_USER + 25)
        RB_DRAGMOVE = (WM_USER + 26)
        RB_GETBARHEIGHT = (WM_USER + 27)
        RB_GETBANDINFOW = (WM_USER + 28)
        RB_GETBANDINFOA = (WM_USER + 29)
        RB_GETBANDINFO = unicode(RB_GETBANDINFOW, RB_GETBANDINFOA)
        RB_MINIMIZEBAND = (WM_USER + 30)
        RB_MAXIMIZEBAND = (WM_USER + 31)
        RB_GETDROPTARGET = (CCM_GETDROPTARGET)
        RB_GETBANDBORDERS = (WM_USER + 34) # returns in lparam = lprc the amount of edges added to band wparam
        RB_SHOWBAND = (WM_USER + 35) # show/hide band
        RB_SETPALETTE = (WM_USER + 37)
        RB_GETPALETTE = (WM_USER + 38)
        RB_MOVEBAND = (WM_USER + 39)
        RB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        RB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        RB_GETBANDMARGINS = (WM_USER + 40)
        RB_SETWINDOWTHEME = CCM_SETWINDOWTHEME
        RB_SETEXTENDEDSTYLE = (WM_USER + 41)
        RB_GETEXTENDEDSTYLE = (WM_USER + 42)
        RB_PUSHCHEVRON = (WM_USER + 43)
        RB_SETBANDWIDTH = (WM_USER + 44) # set width for docked band
        RBN_HEIGHTCHANGE = (RBN_FIRST - 0)
        RBN_GETOBJECT = (RBN_FIRST - 1)
        RBN_LAYOUTCHANGED = (RBN_FIRST - 2)
        RBN_AUTOSIZE = (RBN_FIRST - 3)
        RBN_BEGINDRAG = (RBN_FIRST - 4)
        RBN_ENDDRAG = (RBN_FIRST - 5)
        RBN_DELETINGBAND = (RBN_FIRST - 6) # Uses NMREBAR
        RBN_DELETEDBAND = (RBN_FIRST - 7) # Uses NMREBAR
        RBN_CHILDSIZE = (RBN_FIRST - 8)
        RBN_CHEVRONPUSHED = (RBN_FIRST - 10)
        RBN_SPLITTERDRAG = (RBN_FIRST - 11)
        RBN_MINMAX = (RBN_FIRST - 21)
        RBN_AUTOBREAK = (RBN_FIRST - 22)

        class tagNMREBARCHILDSIZE(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("uBand", UINT),
                ("wID", UINT),
                ("rcChild", RECT),
                ("rcBand", RECT)
            ]
            hdr: NMHDR
            uBand: int
            wID: int
            rcChild: RECT
            rcBand: RECT
        NMREBARCHILDSIZE = tagNMREBARCHILDSIZE
        LPNMREBARCHILDSIZE = POINTER(NMREBARCHILDSIZE)

        class tagNMREBAR(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("dwMask", DWORD),
                ("uBand", UINT),
                ("fStyle", UINT),
                ("wID", UINT), # RBNM_*
                ("lParam", LPARAM)
            ]
            hdr: NMHDR
            dwMask: int
            uBand: int
            fStyle: int
            wID: int
            lParam: int
        NMREBAR = tagNMREBAR
        LPNMREBAR = POINTER(NMREBAR)

        # Mask flags for NMREBAR
        RBNM_ID = 0x00000001
        RBNM_STYLE = 0x00000002
        RBNM_LPARAM = 0x00000004


        class tagNMRBAUTOSIZE(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("fChanged", BOOL),
                ("rcTarget", RECT),
                ("rcActual", RECT)
            ]
            hdr: NMHDR
            fChanged: int
            rcTarget: RECT
            rcActual: RECT
        NMRBAUTOSIZE = tagNMRBAUTOSIZE
        LPNMRBAUTOSIZE = POINTER(NMRBAUTOSIZE)

        class tagNMREBARCHEVRON(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("uBand", UINT),
                ("wID", UINT),
                ("lParam", LPARAM),
                ("rc", RECT),
                ("lParamNM", LPARAM)
            ]
            hdr: NMHDR
            uBand: int
            wID: int
            lParam: int
            rc: RECT
            lParamNM: int
        NMREBARCHEVRON = tagNMREBARCHEVRON
        LPNMREBARCHEVRON = POINTER(NMREBARCHEVRON)

        class tagNMREBARSPLITTER(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("rcSizing", RECT)
            ]
            hdr: NMHDR
            rcSizing: RECT
        NMREBARSPLITTER = tagNMREBARSPLITTER
        LPNMREBARSPLITTER = POINTER(NMREBARSPLITTER)

        RBAB_AUTOSIZE = 0x0001 # These are not flags and are all mutually exclusive
        RBAB_ADDBAND = 0x0002

        class tagNMREBARAUTOBREAK(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("uBand", UINT),
                ("wID", UINT),
                ("lParam", LPARAM),
                ("uMsg", UINT),
                ("fStyleCurrent", UINT),
                ("fAutoBreak", BOOL)
            ]
            hdr: int
            uBand: int
            wID: int
            lParam: int
            uMsg: int
            fStyleCurrent: int
            fAutoBreak: int
        NMREBARAUTOBREAK = tagNMREBARAUTOBREAK
        LPNMREBARAUTOBREAK = POINTER(NMREBARAUTOBREAK)

        RBHT_NOWHERE = 0x0001
        RBHT_CAPTION = 0x0002
        RBHT_CLIENT = 0x0003
        RBHT_GRABBER = 0x0004
        RBHT_CHEVRON = 0x0008
        RBHT_SPLITTER = 0x0010

        class _RB_HITTESTINFO(CStructure):
            _fields_ = [
                ("pt", POINT),
                ("flags", UINT),
                ("iBand", INT)
            ]
            pt: POINT
            flags: int
            iBand: int
        RBHITTESTINFO = _RB_HITTESTINFO
        LPRBHITTESTINFO = POINTER(RBHITTESTINFO)
    #====== TOOLTIPS CONTROL =====================================================
    if cpreproc.ifndef("NOTOOLTIPS"):
        if cpreproc.ifdef("_WIN32"):
            TOOLTIPS_CLASSW = u"tooltips_class32"
            TOOLTIPS_CLASSA = "tooltips_class32"
            TOOLTIPS_CLASS = unicode(TOOLTIPS_CLASSW, TOOLTIPS_CLASSA)
        else:
            TOOLTIPS_CLASS = "tooltips_class"

        class tagTOOLINFOA(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("uFlags", UINT),
                ("hwnd", HWND),
                ("uId", UINT_PTR),
                ("rect", RECT),
                ("hinst", HINSTANCE),
                ("lpszText", LPSTR),
                ("lParam", LPARAM)
            ]
            if cpreproc.get_version() >= WIN32_WINNT_WINXP:
                _fields_.append(("lpReserved", PVOID))
            cbSize: int
            uFlags: int
            hwnd: int
            uId: int
            rect: RECT
            hinst: int
            lpszText: LPSTR
            lParam: int
            lpReserved: int
        TTTOOLINFOA = tagTOOLINFOA
        PTOOLINFOA = POINTER(TTTOOLINFOA)
        LPTTTOOLINFOA = PTOOLINFOA

        class tagTOOLINFOW(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("uFlags", UINT),
                ("hwnd", HWND),
                ("uId", UINT_PTR),
                ("rect", RECT),
                ("hinst", HINSTANCE),
                ("lpszText", LPWSTR),
                ("lParam", LPARAM)
            ]
            if (cpreproc.get_version() >= WIN32_WINNT_WINXP):
                _fields_.append(("lpReserved", PVOID))
            cbSize: int
            uFlags: int
            hwnd: int
            uId: int
            rect: RECT
            hinst: int
            lpszText: LPWSTR
            lParam: int
            lpReserved: int
        
        TTTOOLINFOW = tagTOOLINFOW
        PTOOLINFOW = POINTER(TTTOOLINFOW)
        LPTTTOOLINFOW = PTOOLINFOW

        TTTOOLINFO = unicode(TTTOOLINFOW, TTTOOLINFOA)
        PTOOLINFOW = unicode(PTOOLINFOW, PTOOLINFOA)
        LPTTTOOLINFO = PTOOLINFOW

        LPTOOLINFOA = LPTTTOOLINFOA
        LPTOOLINFOW = LPTTTOOLINFOW
        TOOLINFOA = TTTOOLINFOA
        TOOLINFOW = TTTOOLINFOW
        LPTOOLINFO = LPTTTOOLINFO
        TOOLINFO = TTTOOLINFO
        TTTOOLINFOA_V1_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, "lpszText")
        TTTOOLINFOW_V1_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, "lpszText")
        TTTOOLINFOA_V2_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, "lParam")
        TTTOOLINFOW_V2_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, "lParam")
        TTTOOLINFOA_V3_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOA, "lpReserved")
        TTTOOLINFOW_V3_SIZE = CCSIZEOF_STRUCT(TTTOOLINFOW, "lpReserved")

        # begin_r_commctrl
        TTS_ALWAYSTIP = 0x01
        TTS_NOPREFIX = 0x02
        TTS_NOANIMATE = 0x10
        TTS_NOFADE = 0x20
        TTS_BALLOON = 0x40
        TTS_CLOSE = 0x80
        TTS_USEVISUALSTYLE = 0x100 # Use themed hyperlinks
        # end_r_commctrl
        TTF_IDISHWND = 0x0001
        # Use this to center around trackpoint in trackmode
        # -OR- to center around tool in normal mode.
        # Use TTF_ABSOLUTE to place the tip exactly at the track coords when
        # in tracking mode.  TTF_ABSOLUTE can be used in conjunction with TTF_CENTERTIP
        # to center the tip absolutely about the track point.
        TTF_CENTERTIP = 0x0002
        TTF_RTLREADING = 0x0004
        TTF_SUBCLASS = 0x0010
        TTF_TRACK = 0x0020
        TTF_ABSOLUTE = 0x0080
        TTF_TRANSPARENT = 0x0100
        TTF_PARSELINKS = 0x1000
        TTF_DI_SETITEM = 0x8000 # valid only on the TTN_NEEDTEXT callback
        TTDT_AUTOMATIC = 0
        TTDT_RESHOW = 1
        TTDT_AUTOPOP = 2
        TTDT_INITIAL = 3
        # ToolTip Icons (Set with TTM_SETTITLE)
        TTI_NONE = 0
        TTI_INFO = 1
        TTI_WARNING = 2
        TTI_ERROR = 3
        TTI_INFO_LARGE = 4
        TTI_WARNING_LARGE = 5
        TTI_ERROR_LARGE = 6
        # Tool Tip Messages
        TTM_ACTIVATE = (WM_USER + 1)
        TTM_SETDELAYTIME = (WM_USER + 3)
        TTM_ADDTOOLA = (WM_USER + 4)
        TTM_ADDTOOLW = (WM_USER + 50)
        TTM_DELTOOLA = (WM_USER + 5)
        TTM_DELTOOLW = (WM_USER + 51)
        TTM_NEWTOOLRECTA = (WM_USER + 6)
        TTM_NEWTOOLRECTW = (WM_USER + 52)
        TTM_RELAYEVENT = (WM_USER + 7) # Win7: wParam = GetMessageExtraInfo() when relaying WM_MOUSEMOVE
        TTM_GETTOOLINFOA = (WM_USER + 8)
        TTM_GETTOOLINFOW = (WM_USER + 53)
        TTM_SETTOOLINFOA = (WM_USER + 9)
        TTM_SETTOOLINFOW = (WM_USER + 54)
        TTM_HITTESTA = (WM_USER +10)
        TTM_HITTESTW = (WM_USER +55)
        TTM_GETTEXTA = (WM_USER +11)
        TTM_GETTEXTW = (WM_USER +56)
        TTM_UPDATETIPTEXTA = (WM_USER +12)
        TTM_UPDATETIPTEXTW = (WM_USER +57)
        TTM_GETTOOLCOUNT = (WM_USER +13)
        TTM_ENUMTOOLSA = (WM_USER +14)
        TTM_ENUMTOOLSW = (WM_USER +58)
        TTM_GETCURRENTTOOLA = (WM_USER + 15)
        TTM_GETCURRENTTOOLW = (WM_USER + 59)
        TTM_WINDOWFROMPOINT = (WM_USER + 16)
        TTM_TRACKACTIVATE = (WM_USER + 17) # wParam = TRUE/FALSE start end  lparam = LPTOOLINFO
        TTM_TRACKPOSITION = (WM_USER + 18) # lParam = dwPos
        TTM_SETTIPBKCOLOR = (WM_USER + 19)
        TTM_SETTIPTEXTCOLOR = (WM_USER + 20)
        TTM_GETDELAYTIME = (WM_USER + 21)
        TTM_GETTIPBKCOLOR = (WM_USER + 22)
        TTM_GETTIPTEXTCOLOR = (WM_USER + 23)
        TTM_SETMAXTIPWIDTH = (WM_USER + 24)
        TTM_GETMAXTIPWIDTH = (WM_USER + 25)
        TTM_SETMARGIN = (WM_USER + 26) # lParam = lprc
        TTM_GETMARGIN = (WM_USER + 27) # lParam = lprc
        TTM_POP = (WM_USER + 28)
        TTM_UPDATE = (WM_USER + 29)
        TTM_GETBUBBLESIZE = (WM_USER + 30)
        TTM_ADJUSTRECT = (WM_USER + 31)
        TTM_SETTITLEA = (WM_USER + 32) # wParam = TTI_*, lParam = char* szTitle
        TTM_SETTITLEW = (WM_USER + 33) # wParam = TTI_*, lParam = wchar* szTitle
        TTM_POPUP = (WM_USER + 34)
        TTM_GETTITLE = (WM_USER + 35) # wParam = 0, lParam = TTGETTITLE*

        class _TTGETTITLE(CStructure):
            _fields_ = [
                ("dwSize", DWORD),
                ("uTitleBitmap", UINT),
                ("cch", UINT),
                ("pszTitle", PWCHAR)
            ]
            dwSize: int
            uTitleBitmap: int
            cch: int
            pszTitle: LPWSTR
        TTGETTITLE = _TTGETTITLE
        PTTGETTITLE = POINTER(TTGETTITLE)

        TTM_ADDTOOL = unicode(TTM_ADDTOOLW, TTM_ADDTOOLA)
        TTM_DELTOOL = unicode(TTM_DELTOOLW, TTM_DELTOOLA)
        TTM_NEWTOOLRECT = unicode(TTM_NEWTOOLRECTW, TTM_NEWTOOLRECTA)
        TTM_GETTOOLINFO = unicode(TTM_GETTOOLINFOW, TTM_GETTOOLINFOA)
        TTM_SETTOOLINFO = unicode(TTM_SETTOOLINFOW, TTM_SETTOOLINFOA)
        TTM_HITTEST = unicode(TTM_HITTESTW, TTM_HITTESTA)
        TTM_GETTEXT = unicode(TTM_GETTEXTW, TTM_GETTEXTA)
        TTM_UPDATETIPTEXT = unicode(TTM_UPDATETIPTEXTW, TTM_UPDATETIPTEXTA)
        TTM_ENUMTOOLS = unicode(TTM_ENUMTOOLSW, TTM_ENUMTOOLSA)
        TTM_GETCURRENTTOOL = unicode(TTM_GETCURRENTTOOLW, TTM_GETCURRENTTOOLA)
        TTM_SETTITLE = unicode(TTM_SETTITLEW, TTM_SETTITLEA)

        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            TTM_SETWINDOWTHEME = CCM_SETWINDOWTHEME

        class _TT_HITTESTINFOA(CStructure):
            _fields_ = [
                ("hwnd", HWND),
                ("pt", POINT),
                ("ti", TTTOOLINFOA)
            ]
            hwnd: int
            pt: POINT
            ti: TTTOOLINFOA
        TTHITTESTINFOA = _TT_HITTESTINFOA
        LPTTHITTESTINFOA = POINTER(TTHITTESTINFOA)

        class _TT_HITTESTINFOW(CStructure):
            _fields_ = [
                ("hwnd", HWND),
                ("pt", POINT),
                ("ti", TTTOOLINFOW)
            ]
            hwnd: int
            pt: POINT
            ti: TTTOOLINFOW
        TTHITTESTINFOW = _TT_HITTESTINFOW
        LPTTHITTESTINFOW = POINTER(TTHITTESTINFOW)

        TTHITTESTINFO = unicode(TTHITTESTINFOW, TTHITTESTINFOA)
        LPTTHITTESTINFO = unicode(LPTTHITTESTINFOW, LPTTHITTESTINFOA)
        
        LPHITTESTINFOW = LPTTHITTESTINFOW
        LPHITTESTINFOA = LPTTHITTESTINFOA
        LPHITTESTINFO = LPTTHITTESTINFO  

        TTN_GETDISPINFOA = (TTN_FIRST - 0)
        TTN_GETDISPINFOW = (TTN_FIRST - 10)
        TTN_SHOW = (TTN_FIRST - 1)
        TTN_POP = (TTN_FIRST - 2)
        TTN_LINKCLICK = (TTN_FIRST - 3)
        TTN_GETDISPINFO = unicode(TTN_GETDISPINFOW, TTN_GETDISPINFOA)
        TTN_NEEDTEXT = TTN_GETDISPINFO
        TTN_NEEDTEXTA = TTN_GETDISPINFOA
        TTN_NEEDTEXTW = TTN_GETDISPINFOW

        class tagNMTTDISPINFOA(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("lpszText", LPSTR),
                ("szText", CHAR * 80),
                ("hinst", HINSTANCE),
                ("uFlags", UINT),
                ("lParam", LPARAM)
            ]
            hdr: NMHDR
            lpszText: LPSTR
            szText: IWideCharArray
            hinst: int
            uFlags: int
            lParam: int
        NMTTDISPINFOA = tagNMTTDISPINFOA
        LPNMTTDISPINFOA = POINTER(NMTTDISPINFOA)

        class tagNMTTDISPINFOW(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("lpszText", LPWSTR),
                ("szText", WCHAR * 80),
                ("hinst", HINSTANCE),
                ("uFlags", UINT),
                ("lParam", LPARAM)
            ]
            hdr: NMHDR
            lpszText: LPWSTR
            szText: IWideCharArray
            hinst: int
            uFlags: int
            lParam: int
        NMTTDISPINFOW = tagNMTTDISPINFOW
        LPNMTTDISPINFOW = POINTER(NMTTDISPINFOW)

        NMTTDISPINFO = unicode(NMTTDISPINFOW, NMTTDISPINFOA)
        LPNMTTDISPINFO = unicode(LPNMTTDISPINFOW, LPNMTTDISPINFOA)

        TOOLTIPTEXTW = NMTTDISPINFOW
        TOOLTIPTEXTA = NMTTDISPINFOA
        LPTOOLTIPTEXTA = LPNMTTDISPINFOA
        LPTOOLTIPTEXTW = LPNMTTDISPINFOW
        TOOLTIPTEXT = NMTTDISPINFO
        LPTOOLTIPTEXT = LPNMTTDISPINFO

        NMTTDISPINFOA_V1_SIZE = CCSIZEOF_STRUCT(NMTTDISPINFOA, "uFlags")
        NMTTDISPINFOW_V1_SIZE = CCSIZEOF_STRUCT(NMTTDISPINFOW, "uFlags")

        NMTTDISPINFO_V1_SIZE = unicode(NMTTDISPINFOW_V1_SIZE, NMTTDISPINFOA_V1_SIZE)
    #====== STATUS BAR CONTROL ===================================================
    if cpreproc.ifndef("NOSTATUSBAR"):
        # begin_r_commctrl
        SBARS_SIZEGRIP = 0x0100
        SBARS_TOOLTIPS = 0x0800
        # this is a status bar flag, preference to SBARS_TOOLTIPS
        SBT_TOOLTIPS = 0x0800
        # end_r_commctrl

        DrawStatusTextA = declare(comctl32.DrawStatusTextA, VOID, HDC, LPRECT, LPCSTR, UINT)
        DrawStatusTextW = declare(comctl32.DrawStatusTextW, VOID, HDC, LPRECT, LPCWSTR, UINT)
        CreateStatusWindowA = declare(comctl32.CreateStatusWindowA, HWND, LONG, LPCSTR, HWND, UINT)
        CreateStatusWindowW = declare(comctl32.CreateStatusWindowW, HWND, LONG, LPCWSTR, HWND, UINT)

        CreateStatusWindow = unicode(CreateStatusWindowW, CreateStatusWindowA)
        DrawStatusText = unicode(DrawStatusTextW, DrawStatusTextA)
        if cpreproc.ifdef("_WIN32"):
            STATUSCLASSNAMEW = u"msctls_statusbar32"
            STATUSCLASSNAMEA = "msctls_statusbar32"
            STATUSCLASSNAME = unicode(STATUSCLASSNAMEW, STATUSCLASSNAMEA)
        else:
            STATUSCLASSNAME = "msctls_statusbar"
        SB_SETTEXTA = (WM_USER+1)
        SB_SETTEXTW = (WM_USER+11)
        SB_GETTEXTA = (WM_USER+2)
        SB_GETTEXTW = (WM_USER+13)
        SB_GETTEXTLENGTHA = (WM_USER+3)
        SB_GETTEXTLENGTHW = (WM_USER+12)
        SB_GETTEXT = unicode(SB_GETTEXTW, SB_GETTEXTA)
        SB_SETTEXT = unicode(SB_SETTEXTW, SB_SETTEXTA)
        SB_GETTEXTLENGTH = unicode(SB_GETTEXTLENGTHW, SB_GETTEXTLENGTHA)
        SB_SETPARTS = (WM_USER+4)
        SB_GETPARTS = (WM_USER+6)
        SB_GETBORDERS = (WM_USER+7)
        SB_SETMINHEIGHT = (WM_USER+8)
        SB_SIMPLE = (WM_USER+9)
        SB_GETRECT = (WM_USER+10)
        SB_ISSIMPLE = (WM_USER+14)
        SB_SETICON = (WM_USER+15)
        SB_SETTIPTEXTA = (WM_USER+16)
        SB_SETTIPTEXTW = (WM_USER+17)
        SB_GETTIPTEXTA = (WM_USER+18)
        SB_GETTIPTEXTW = (WM_USER+19)
        SB_SETTIPTEXT = unicode(SB_SETTIPTEXTW, SB_SETTIPTEXTA)
        SB_GETTIPTEXT = unicode(SB_GETTIPTEXTW, SB_GETTIPTEXTA)
        SB_GETICON = (WM_USER+20)
        SB_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        SB_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        SBT_OWNERDRAW = 0x1000
        SBT_NOBORDERS = 0x0100
        SBT_POPOUT = 0x0200
        SBT_RTLREADING = 0x0400
        SBT_NOTABPARSING = 0x0800
        SB_SETBKCOLOR = CCM_SETBKCOLOR # lParam = bkColor
        # status bar notifications
        SBN_SIMPLEMODECHANGE = (SBN_FIRST - 0)
        # refers to the data saved for simple mode
        SB_SIMPLEID = 0x00ff
        # NOSTATUSBAR
    #====== MENU HELP ============================================================
    if cpreproc.ifndef("NOMENUHELP"):
        MenuHelp = declare(comctl32.MenuHelp, VOID, UINT, WPARAM, LPARAM, HMENU, HINSTANCE, HWND, PUINT)
        ShowHideMenuCtl = declare(comctl32.ShowHideMenuCtl, BOOL, HWND, UINT_PTR, LPINT)
        GetEffectiveClientRect = declare(comctl32.GetEffectiveClientRect, VOID, HWND, LPRECT, PINT)
        MINSYSCOMMAND = SC_SIZE
    #====== TRACKBAR CONTROL =====================================================
    if cpreproc.ifndef("NOTRACKBAR"):
        if cpreproc.ifdef("_WIN32"):
            TRACKBAR_CLASSA = "msctls_trackbar32"
            TRACKBAR_CLASSW = u"msctls_trackbar32"
            TRACKBAR_CLASS = unicode(TRACKBAR_CLASSW, TRACKBAR_CLASSA)
        else:
            TRACKBAR_CLASS = "msctls_trackbar"
        # begin_r_commctrl
        TBS_AUTOTICKS = 0x0001
        TBS_VERT = 0x0002
        TBS_HORZ = 0x0000
        TBS_TOP = 0x0004
        TBS_BOTTOM = 0x0000
        TBS_LEFT = 0x0004
        TBS_RIGHT = 0x0000
        TBS_BOTH = 0x0008
        TBS_NOTICKS = 0x0010
        TBS_ENABLESELRANGE = 0x0020
        TBS_FIXEDLENGTH = 0x0040
        TBS_NOTHUMB = 0x0080
        TBS_TOOLTIPS = 0x0100
        TBS_REVERSED = 0x0200 # Accessibility hint: the smaller number (usually the min value) means "high" and the larger number (usually the max value) means "low"
        TBS_DOWNISLEFT = 0x0400 # Down=Left and Up=Right (default is Down=Right and Up=Left)
        TBS_NOTIFYBEFOREMOVE = 0x0800 # Trackbar should notify parent before repositioning the slider due to user action (enables snapping)
        TBS_TRANSPARENTBKGND = 0x1000 # Background is painted by the parent via WM_PRINTCLIENT
        # end_r_commctrl
        TBM_GETPOS = (WM_USER)
        TBM_GETRANGEMIN = (WM_USER+1)
        TBM_GETRANGEMAX = (WM_USER+2)
        TBM_GETTIC = (WM_USER+3)
        TBM_SETTIC = (WM_USER+4)
        TBM_SETPOS = (WM_USER+5)
        TBM_SETRANGE = (WM_USER+6)
        TBM_SETRANGEMIN = (WM_USER+7)
        TBM_SETRANGEMAX = (WM_USER+8)
        TBM_CLEARTICS = (WM_USER+9)
        TBM_SETSEL = (WM_USER+10)
        TBM_SETSELSTART = (WM_USER+11)
        TBM_SETSELEND = (WM_USER+12)
        TBM_GETPTICS = (WM_USER+14)
        TBM_GETTICPOS = (WM_USER+15)
        TBM_GETNUMTICS = (WM_USER+16)
        TBM_GETSELSTART = (WM_USER+17)
        TBM_GETSELEND = (WM_USER+18)
        TBM_CLEARSEL = (WM_USER+19)
        TBM_SETTICFREQ = (WM_USER+20)
        TBM_SETPAGESIZE = (WM_USER+21)
        TBM_GETPAGESIZE = (WM_USER+22)
        TBM_SETLINESIZE = (WM_USER+23)
        TBM_GETLINESIZE = (WM_USER+24)
        TBM_GETTHUMBRECT = (WM_USER+25)
        TBM_GETCHANNELRECT = (WM_USER+26)
        TBM_SETTHUMBLENGTH = (WM_USER+27)
        TBM_GETTHUMBLENGTH = (WM_USER+28)
        TBM_SETTOOLTIPS = (WM_USER+29)
        TBM_GETTOOLTIPS = (WM_USER+30)
        TBM_SETTIPSIDE = (WM_USER+31)
        # TrackBar Tip Side flags
        TBTS_TOP = 0
        TBTS_LEFT = 1
        TBTS_BOTTOM = 2
        TBTS_RIGHT = 3
        TBM_SETBUDDY = (WM_USER+32) # wparam = BOOL fLeft; (or right)
        TBM_GETBUDDY = (WM_USER+33) # wparam = BOOL fLeft; (or right)
        TBM_SETPOSNOTIFY = (WM_USER+34)
        TBM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        TBM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        TB_LINEUP = 0
        TB_LINEDOWN = 1
        TB_PAGEUP = 2
        TB_PAGEDOWN = 3
        TB_THUMBPOSITION = 4
        TB_THUMBTRACK = 5
        TB_TOP = 6
        TB_BOTTOM = 7
        TB_ENDTRACK = 8
        # custom draw item specs
        TBCD_TICS = 0x0001
        TBCD_THUMB = 0x0002
        TBCD_CHANNEL = 0x0003
        TRBN_THUMBPOSCHANGING = (TRBN_FIRST-1)
        # Structure for Trackbar's TRBN_THUMBPOSCHANGING notification
        class NMTRBTHUMBPOSCHANGING(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("dwPos", DWORD),
                ("nReason", INT)
            ]
            hdr: NMHDR
            dwPos: int
            nReason: int

        # trackbar

        #====== DRAG LIST CONTROL ====================================================

    if cpreproc.ifndef("NODRAGLIST"):
        class DRAGLISTINFO(CStructure):
            _fields_ = [
                ("uNotification", UINT),
                ("hWnd", HWND),
                ("ptCursor", POINT)
            ]
            uNotification: int
            hWnd: int
            ptCursor: POINT
        LPDRAGLISTINFO = POINTER(DRAGLISTINFO)

        DL_BEGINDRAG = (WM_USER+133)
        DL_DRAGGING = (WM_USER+134)
        DL_DROPPED = (WM_USER+135)
        DL_CANCELDRAG = (WM_USER+136)
        DL_CURSORSET = 0
        DL_STOPCURSOR = 1
        DL_COPYCURSOR = 2
        DL_MOVECURSOR = 3
        DRAGLISTMSGSTRING = TEXT("commctrl_DragListMsg")
        MakeDragList = declare(comctl32.MakeDragList, BOOL, HWND)
        DrawInsert = declare(comctl32.DrawInsert, VOID, HWND, HWND, INT)
        LBItemFromPt = declare(comctl32.LBItemFromPt, INT, HWND, POINT, BOOL)
    #====== UPDOWN CONTROL =======================================================
    if cpreproc.ifndef("NOUPDOWN"):
        if cpreproc.ifdef("_WIN32"):
            UPDOWN_CLASSA = "msctls_updown32"
            UPDOWN_CLASSW = u"msctls_updown32"
            UPDOWN_CLASS = unicode(UPDOWN_CLASSW, UPDOWN_CLASSA)
        else:
            UPDOWN_CLASS = "msctls_updown"
        class UDACCEL(CStructure):
            _fields_ = [
                ("nSec", UINT),
                ("nInc", UINT)
            ]
            nSec: int
            nInc: int
        LPUDACCEL = POINTER(UDACCEL)
        UD_MAXVAL = 0x7fff
        UD_MINVAL = (-UD_MAXVAL)
        # begin_r_commctrl
        UDS_WRAP = 0x0001
        UDS_SETBUDDYINT = 0x0002
        UDS_ALIGNRIGHT = 0x0004
        UDS_ALIGNLEFT = 0x0008
        UDS_AUTOBUDDY = 0x0010
        UDS_ARROWKEYS = 0x0020
        UDS_HORZ = 0x0040
        UDS_NOTHOUSANDS = 0x0080
        UDS_HOTTRACK = 0x0100
        # end_r_commctrl
        UDM_SETRANGE = (WM_USER+101)
        UDM_GETRANGE = (WM_USER+102)
        UDM_SETPOS = (WM_USER+103)
        UDM_GETPOS = (WM_USER+104)
        UDM_SETBUDDY = (WM_USER+105)
        UDM_GETBUDDY = (WM_USER+106)
        UDM_SETACCEL = (WM_USER+107)
        UDM_GETACCEL = (WM_USER+108)
        UDM_SETBASE = (WM_USER+109)
        UDM_GETBASE = (WM_USER+110)
        UDM_SETRANGE32 = (WM_USER+111)
        UDM_GETRANGE32 = (WM_USER+112) # wParam & lParam are LPINT
        UDM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        UDM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        UDM_SETPOS32 = (WM_USER+113)
        UDM_GETPOS32 = (WM_USER+114)
        CreateUpDownControl = declare(comctl32.CreateUpDownControl, HWND, DWORD, INT, INT, INT, INT, HWND, INT, HINSTANCE, HWND, INT, INT, INT)

        class NMUPDOWN(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("iPos", INT),
                ("iDelta", INT)
            ]
            hdr: NMHDR
            iPos: int
            iDelta: int
        LPNMUPDOWN = POINTER(NMUPDOWN)
        
        NM_UPDOWN = NMUPDOWN
        LPNM_UPDOWN = LPNMUPDOWN

        UDN_DELTAPOS = (UDN_FIRST - 1)
    # NOUPDOWN
    #====== PROGRESS CONTROL =====================================================
    if cpreproc.ifndef("NOPROGRESS"):
        PROGRESS_CLASSA = b"msctls_progress32"
        PROGRESS_CLASSW = u"msctls_progress32"
        PROGRESS_CLASS = PROGRESS_CLASSW
        # begin_r_commctrl
        PBS_SMOOTH = 0x01
        PBS_VERTICAL = 0x04
        # end_r_commctrl
        PBM_SETRANGE = (WM_USER+1)
        PBM_SETPOS = (WM_USER+2)
        PBM_DELTAPOS = (WM_USER+3)
        PBM_SETSTEP = (WM_USER+4)
        PBM_STEPIT = (WM_USER+5)
        PBM_SETRANGE32 = (WM_USER+6) # lParam = high, wParam = low

        class PBRANGE(CStructure):
            _fields_ = [
                ("iLow", INT),
                ("iHigh", INT)
            ]
            iLow: int
            iHigh: int
        PPBRANGE = POINTER(PBRANGE)

        PBM_GETRANGE = (WM_USER+7) # wParam = return (TRUE ? low : high). lParam = PPBRANGE or NULL
        PBM_GETPOS = (WM_USER+8)
        PBM_SETBARCOLOR = (WM_USER+9) # lParam = bar color
        PBM_SETBKCOLOR = CCM_SETBKCOLOR # lParam = bkColor
        # begin_r_commctrl
        PBS_MARQUEE = 0x08
        # end_r_commctrl
        PBM_SETMARQUEE = (WM_USER+10)
        # begin_r_commctrl
        PBS_SMOOTHREVERSE = 0x10
        # end_r_commctrl
        PBM_GETSTEP = (WM_USER+13)
        PBM_GETBKCOLOR = (WM_USER+14)
        PBM_GETBARCOLOR = (WM_USER+15)
        PBM_SETSTATE = (WM_USER+16) # wParam = PBST_[State] (NORMAL, ERROR, PAUSED)
        PBM_GETSTATE = (WM_USER+17)
        PBST_NORMAL = 0x0001
        PBST_ERROR = 0x0002
        PBST_PAUSED = 0x0003
    # NOPROGRESS
    #====== HOTKEY CONTROL =======================================================
    if cpreproc.ifndef("NOHOTKEY"):
        HOTKEYF_SHIFT = 0x01
        HOTKEYF_CONTROL = 0x02
        HOTKEYF_ALT = 0x04
        HOTKEYF_EXT = 0x08
        HKCOMB_NONE = 0x0001
        HKCOMB_S = 0x0002
        HKCOMB_C = 0x0004
        HKCOMB_A = 0x0008
        HKCOMB_SC = 0x0010
        HKCOMB_SA = 0x0020
        HKCOMB_CA = 0x0040
        HKCOMB_SCA = 0x0080
        HKM_SETHOTKEY = (WM_USER+1)
        HKM_GETHOTKEY = (WM_USER+2)
        HKM_SETRULES = (WM_USER+3)
        if cpreproc.ifdef("_WIN32"):
            HOTKEY_CLASSA = "msctls_hotkey32"
            HOTKEY_CLASSW = u"msctls_hotkey32"
            HOTKEY_CLASS = unicode(HOTKEY_CLASSW, HOTKEY_CLASSA)
        else:
            HOTKEY_CLASS = "msctls_hotkey"
    # NOHOTKEY
    # begin_r_commctrl
    #====== COMMON CONTROL STYLES ================================================
    CCS_TOP = 0x00000001
    CCS_NOMOVEY = 0x00000002
    CCS_BOTTOM = 0x00000003
    CCS_NORESIZE = 0x00000004
    CCS_NOPARENTALIGN = 0x00000008
    CCS_ADJUSTABLE = 0x00000020
    CCS_NODIVIDER = 0x00000040
    CCS_VERT = 0x00000080
    CCS_LEFT = (CCS_VERT | CCS_TOP)
    CCS_RIGHT = (CCS_VERT | CCS_BOTTOM)
    CCS_NOMOVEX = (CCS_VERT | CCS_NOMOVEY)
    # end_r_commctrl
    #====== SysLink control =========================================
    if cpreproc.ifndef("NOSYSLINK"):
        INVALID_LINK_INDEX = (-1)
        MAX_LINKID_TEXT = 48
        L_MAX_URL_LENGTH = (2048 + 32 + len(": #"))
        WC_LINK = u"SysLink"
        # begin_r_commctrl
        LWS_TRANSPARENT = 0x0001
        LWS_IGNORERETURN = 0x0002
        LWS_NOPREFIX = 0x0004
        LWS_USEVISUALSTYLE = 0x0008
        LWS_USECUSTOMTEXT = 0x0010
        LWS_RIGHT = 0x0020
        # end_r_commctrl
        LIF_ITEMINDEX = 0x00000001
        LIF_STATE = 0x00000002
        LIF_ITEMID = 0x00000004
        LIF_URL = 0x00000008
        LIS_FOCUSED = 0x00000001
        LIS_ENABLED = 0x00000002
        LIS_VISITED = 0x00000004
        LIS_HOTTRACK = 0x00000008
        LIS_DEFAULTCOLORS = 0x00000010 # Don't use any custom text colors

        class LITEM(CStructure):
            _fields_ = [
                ("mask", UINT),
                ("iLink", INT),
                ("state", UINT),
                ("stateMask", UINT),
                ("szID", WCHAR * MAX_LINKID_TEXT),
                ("szUrl", WCHAR * L_MAX_URL_LENGTH)
            ]
            mask: int
            iLink: int
            state: int
            stateMask: int
            szID: IWideCharArray
            szUrl: IWideCharArray
            
        PLITEM = POINTER(LITEM)

        class LHITTESTINFO(CStructure):
            _fields_ = [
                ("pt", POINT),
                ("item", LITEM)
            ]
            pt: POINT
            item: LITEM
        PLHITTESTINFO = POINTER(LHITTESTINFO)

        class NMLINK(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("item", LITEM)
            ]
            hdr: NMHDR
            item: LITEM
            
        PNMLINK = POINTER(NMLINK)

        #  SysLink notifications
        #  NM_CLICK   # wParam: control ID, lParam: PNMLINK, ret: ignored.
        #  LinkWindow messages
        LM_HITTEST = (WM_USER+0x300) # wParam: n/a, lparam: PLHITTESTINFO, ret: BOOL
        LM_GETIDEALHEIGHT = (WM_USER+0x301) # wParam: cxMaxWidth, lparam: n/a, ret: cy
        LM_SETITEM = (WM_USER+0x302) # wParam: n/a, lparam: LITEM*, ret: BOOL
        LM_GETITEM = (WM_USER+0x303) # wParam: n/a, lparam: LITEM*, ret: BOOL
        LM_GETIDEALSIZE = (LM_GETIDEALHEIGHT) # wParam: cxMaxWidth, lparam: SIZE*, ret: cy
    #====== End SysLink control =========================================
    #====== LISTVIEW CONTROL =====================================================
    if cpreproc.ifndef("NOLISTVIEW"):
        WC_LISTVIEWA = "SysListView32"
        WC_LISTVIEWW = u"SysListView32"
        WC_LISTVIEW = WC_LISTVIEWW
        # begin_r_commctrl
        LVS_ICON = 0x0000
        LVS_REPORT = 0x0001
        LVS_SMALLICON = 0x0002
        LVS_LIST = 0x0003
        LVS_TYPEMASK = 0x0003
        LVS_SINGLESEL = 0x0004
        LVS_SHOWSELALWAYS = 0x0008
        LVS_SORTASCENDING = 0x0010
        LVS_SORTDESCENDING = 0x0020
        LVS_SHAREIMAGELISTS = 0x0040
        LVS_NOLABELWRAP = 0x0080
        LVS_AUTOARRANGE = 0x0100
        LVS_EDITLABELS = 0x0200
        LVS_OWNERDATA = 0x1000
        LVS_NOSCROLL = 0x2000
        LVS_TYPESTYLEMASK = 0xfc00
        LVS_ALIGNTOP = 0x0000
        LVS_ALIGNLEFT = 0x0800
        LVS_ALIGNMASK = 0x0c00
        LVS_OWNERDRAWFIXED = 0x0400
        LVS_NOCOLUMNHEADER = 0x4000
        LVS_NOSORTHEADER = 0x8000
        # end_r_commctrl
        LVM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT

        def ListView_SetUnicodeFormat(hwnd, fUnicode):
            return SendMessage(hwnd, LVM_SETUNICODEFORMAT, fUnicode, 0)

        LVM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT

        def ListView_GetUnicodeFormat(hwnd):
            return SendMessage(hwnd, LVM_GETUNICODEFORMAT, 0, 0)

        LVM_GETBKCOLOR = (LVM_FIRST + 0)

        def ListView_GetBkColor(hwnd):
            return SendMessage(hwnd, LVM_GETBKCOLOR, 0, 0)

        LVM_SETBKCOLOR = (LVM_FIRST + 1)

        def ListView_SetBkColor(hwnd, clrBk):
            return SendMessage(hwnd, LVM_SETBKCOLOR, 0, clrBk)

        LVM_GETIMAGELIST = (LVM_FIRST + 2)

        def ListView_GetImageList(hwnd, iImageList):
            return SendMessage(hwnd, LVM_GETIMAGELIST, iImageList, 0)

        LVSIL_NORMAL = 0
        LVSIL_SMALL = 1
        LVSIL_STATE  =  2
        LVSIL_GROUPHEADER = 3

        LVM_SETIMAGELIST = (LVM_FIRST + 3)

        def ListView_SetImageList(hwnd, himl, iImageList):
            return SendMessage(hwnd, LVM_SETIMAGELIST, iImageList, cast(himl, PVOID).value)

        LVM_GETITEMCOUNT = (LVM_FIRST + 4)

        def ListView_GetItemCount(hwnd):
            return SendMessage(hwnd, LVM_GETITEMCOUNT, 0, 0)
        
        LVIF_TEXT = 0x00000001
        LVIF_IMAGE = 0x00000002
        LVIF_PARAM = 0x00000004
        LVIF_STATE = 0x00000008
        LVIF_INDENT = 0x00000010
        LVIF_NORECOMPUTE = 0x00000800
        LVIF_GROUPID = 0x00000100
        LVIF_COLUMNS = 0x00000200
        LVIF_COLFMT = 0x00010000 # The piColFmt member is valid in addition to puColumns
        LVIS_FOCUSED = 0x0001
        LVIS_SELECTED = 0x0002
        LVIS_CUT = 0x0004
        LVIS_DROPHILITED = 0x0008
        LVIS_GLOW = 0x0010
        LVIS_ACTIVATING = 0x0020
        LVIS_OVERLAYMASK = 0x0F00
        LVIS_STATEIMAGEMASK = 0xF000
        INDEXTOSTATEIMAGEMASK = lambda i: ((i) << 12)
        I_INDENTCALLBACK = (-1)

        LVITEMA__fields_ = [
            ("mask", UINT),
            ("iItem", INT),
            ("iSubItem", INT),
            ("state", UINT),
            ("stateMask", UINT),
            ("pszText", LPSTR),
            ("cchTextMax", INT),
            ("iImage", INT),
            ("lParam", LPARAM),
            ("iIndent", INT)
        ]
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            LVITEMA__fields_.append(("iGroupId", INT))
            LVITEMA__fields_.append(("cColumns", UINT)) # tile view columns
            LVITEMA__fields_.append(("puColumns", PUINT))
        if cpreproc.get_version() >= WIN32_WINNT_VISTA: # Will be unused downlevel, but sizeof(LVITEMA) must be equal to sizeof(LVITEMW)
            LVITEMA__fields_.append(("piColFmt", PINT))
            LVITEMA__fields_.append(("iGroup", INT)) # readonly. only valid for owner data.
        class LVITEMA(CStructure):
            _fields_ = LVITEMA__fields_
            mask: int
            iItem: int
            iSubItem: int
            state: int
            stateMask: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int
            lParam: int
            iIndent: int
            iGroupId: int
            cColumns: int
            puColumns: PUINT
            piColFmt: PINT
            iGroup: int
            
        LPLVITEMA = POINTER(LVITEMA)

        LVITEMW__fields_ = [
            ("mask", UINT),
            ("iItem", INT),
            ("iSubItem", INT),
            ("state", UINT),
            ("stateMask", UINT),
            ("pszText", LPWSTR),
            ("cchTextMax", INT),
            ("iImage", INT),
            ("lParam", LPARAM),
            ("iIndent", INT)
        ]
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            LVITEMW__fields_.append(("iGroupId", INT))
            LVITEMW__fields_.append(("cColumns", UINT)) # tile view columns
            LVITEMW__fields_.append(("puColumns", PUINT))
        if cpreproc.get_version() >= WIN32_WINNT_VISTA: # Will be unused downlevel, but sizeof(LVITEMA) must be equal to sizeof(LVITEMW)
            LVITEMW__fields_.append(("piColFmt", PINT))
            LVITEMW__fields_.append(("iGroup", INT)) # readonly. only valid for owner data.
        class LVITEMW(CStructure):
            _fields_ = LVITEMW__fields_
            mask: int
            iItem: int
            iSubItem: int
            state: int
            stateMask: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            lParam: int
            iIndent: int
            iGroupId: int
            cColumns: int
            puColumns: PUINT
            piColFmt: PINT
            iGroup: int
        LPLVITEMW = POINTER(LVITEMW)
        LVITEM = unicode(LVITEMW, LVITEMA)

        LV_ITEMA = LVITEMA
        LV_ITEMW = LVITEMW
        I_GROUPIDCALLBACK = (-1)
        I_GROUPIDNONE = (-2)
        LV_ITEM = LVITEM
        LVITEMA_V1_SIZE = CCSIZEOF_STRUCT(LVITEMA, "lParam")
        LVITEMW_V1_SIZE = CCSIZEOF_STRUCT(LVITEMW, "lParam")
        LVITEMA_V5_SIZE = CCSIZEOF_STRUCT(LVITEMA, "puColumns")
        LVITEMW_V5_SIZE = CCSIZEOF_STRUCT(LVITEMW, "puColumns")
        LVITEM_V1_SIZE = unicode(LVITEMW_V1_SIZE, LVITEMA_V1_SIZE)
        LVITEM_V5_SIZE = unicode(LVITEMW_V5_SIZE, LVITEMA_V5_SIZE)
        LPSTR_TEXTCALLBACKW = cast(-1, LPWSTR)
        LPSTR_TEXTCALLBACKA = cast(-1, LPSTR)
        LPSTR_TEXTCALLBACK = unicode(LPSTR_TEXTCALLBACKW, LPSTR_TEXTCALLBACKA)
        I_IMAGECALLBACK = (-1)
        I_IMAGENONE = (-2)
        # For tileview
        I_COLUMNSCALLBACK = UINT(-1)
        LVM_GETITEMA = (LVM_FIRST + 5)
        LVM_GETITEMW = (LVM_FIRST + 75)
        LVM_GETITEM = unicode(LVM_GETITEMW, LVM_GETITEMA)

        def ListView_GetItem(hwnd, pitem):
            return SendMessage(hwnd, LVM_GETITEM, 0, cast(pitem, PVOID).value)


        LVM_SETITEMA = (LVM_FIRST + 6)
        LVM_SETITEMW = (LVM_FIRST + 76)
        LVM_SETITEM = unicode(LVM_SETITEMW, LVM_SETITEMA)

        def ListView_SetItem(hwnd, pitem):
            return SendMessage(hwnd, LVM_SETITEM, 0, cast(pitem, PVOID).value)

        LVM_INSERTITEMA = (LVM_FIRST + 7)
        LVM_INSERTITEMW = (LVM_FIRST + 77)
        LVM_INSERTITEM = unicode(LVM_INSERTITEMW, LVM_INSERTITEMA)

        def ListView_InsertItem(hwnd, pitem):
            return SendMessage(hwnd, LVM_INSERTITEM, 0, cast(pitem, PVOID).value)

        LVM_DELETEITEM = (LVM_FIRST + 8)

        def ListView_DeleteItem(hwnd, i):
            return SendMessage(hwnd, LVM_DELETEITEM, i, 0)

        LVM_DELETEALLITEMS = (LVM_FIRST + 9)

        def ListView_DeleteAllItems(hwnd):
            return SendMessage(hwnd, LVM_DELETEALLITEMS, 0, 0)

        LVM_GETCALLBACKMASK = (LVM_FIRST + 10)

        def ListView_GetCallbackMask(hwnd):
            return SendMessage(hwnd, LVM_GETCALLBACKMASK, 0, 0)

        LVM_SETCALLBACKMASK = (LVM_FIRST + 11)

        def ListView_SetCallbackMask(hwnd, mask):
            return SendMessage(hwnd, LVM_SETCALLBACKMASK, mask, 0)
        
        LVNI_ALL = 0x0000
        LVNI_FOCUSED = 0x0001
        LVNI_SELECTED = 0x0002
        LVNI_CUT = 0x0004
        LVNI_DROPHILITED = 0x0008
        LVNI_STATEMASK = (LVNI_FOCUSED | LVNI_SELECTED | LVNI_CUT | LVNI_DROPHILITED)
        LVNI_VISIBLEORDER = 0x0010
        LVNI_PREVIOUS = 0x0020
        LVNI_VISIBLEONLY = 0x0040
        LVNI_SAMEGROUPONLY = 0x0080
        LVNI_ABOVE = 0x0100
        LVNI_BELOW = 0x0200
        LVNI_TOLEFT = 0x0400
        LVNI_TORIGHT = 0x0800
        LVNI_DIRECTIONMASK = (LVNI_ABOVE | LVNI_BELOW | LVNI_TOLEFT | LVNI_TORIGHT)
        LVM_GETNEXTITEM = (LVM_FIRST + 12)

        def ListView_GetNextItem(hwnd, i, flags):
            return SendMessage(hwnd, LVM_GETNEXTITEM, i, MAKELPARAM(flags, 0))
        
        LVFI_PARAM = 0x0001
        LVFI_STRING = 0x0002
        LVFI_SUBSTRING = 0x0004 # Same as LVFI_PARTIAL
        LVFI_PARTIAL = 0x0008
        LVFI_WRAP = 0x0020
        LVFI_NEARESTXY = 0x0040

        class LVFINDINFOA(CStructure):
            _fields_ = [
                ("flags", UINT),
                ("psz", LPCSTR),
                ("lParam", LPARAM),
                ("pt", POINT),
                ("vkDirection", UINT)
            ]
            flags: int
            psz: LPCSTR
            lParam: int
            pt: POINT
            vkDirection: int
            
        LPFINDINFOA = POINTER(LVFINDINFOA)

        class LVFINDINFOW(CStructure):
            _fields_ = [
                ("flags", UINT),
                ("psz", LPCWSTR),
                ("lParam", LPARAM),
                ("pt", POINT),
                ("vkDirection", UINT)
            ]
            flags: int
            psz: LPCWSTR
            lParam: int
            pt: POINT
            vkDirection: int
            
        LPFINDINFOW = POINTER(LVFINDINFOW)

        LVFINDINFO = unicode(LVFINDINFOW, LVFINDINFOA)
        LPFINDINFO = unicode(LPFINDINFOW, LPFINDINFOA)

        LV_FINDINFOA = LVFINDINFOA
        LV_FINDINFOW = LVFINDINFOW
        LV_FINDINFO = LVFINDINFO

        LVM_FINDITEMA  = (LVM_FIRST + 13)
        LVM_FINDITEMW = (LVM_FIRST + 83)
        LVM_FINDITEM = unicode(LVM_FINDITEMW, LVM_FINDITEMA)

        def ListView_FindItem(hwnd, iStart, plvfi):
            return SendMessage(hwnd, LVM_FINDITEM, iStart, cast(plvfi, PVOID).value)

        LVIR_BOUNDS = 0
        LVIR_ICON = 1
        LVIR_LABEL = 2
        LVIR_SELECTBOUNDS = 3

        LVM_GETITEMRECT = (LVM_FIRST + 14)

        def ListView_GetItemRect(hwnd, i, prc, code):
            if prc:
                if hasattr(prc, '_obj'):
                    prc._obj.left = code
                else:
                    prc.contents.left = code
                lParam = cast(prc, PVOID).value
            else:
                lParam = 0
            return SendMessage(hwnd, LVM_GETITEMRECT, i, lParam)

        LVM_SETITEMPOSITION = (LVM_FIRST + 15)

        def ListView_SetItemPosition(hwndLV, i, x, y):
            return SendMessage(hwndLV, LVM_SETITEMPOSITION, i, MAKELPARAM(x, y))

        LVM_GETITEMPOSITION = (LVM_FIRST + 16)

        def ListView_GetItemPosition(hwndLV, i, ppt):
            return SendMessage(hwndLV, LVM_GETITEMPOSITION, i, cast(ppt, PVOID).value)

        LVM_GETSTRINGWIDTHA = (LVM_FIRST + 17)
        LVM_GETSTRINGWIDTHW = (LVM_FIRST + 87)
        LVM_GETSTRINGWIDTH = unicode(LVM_GETSTRINGWIDTHW, LVM_GETSTRINGWIDTHA)

        def ListView_GetStringWidth(hwndLV, psz):
            return SendMessage(hwndLV, LVM_GETSTRINGWIDTH, 0, cast(psz, PVOID).value)

        LVHT_NOWHERE = 0x00000001
        LVHT_ONITEMICON = 0x00000002
        LVHT_ONITEMLABEL = 0x00000004
        LVHT_ONITEMSTATEICON = 0x00000008
        LVHT_ONITEM = (LVHT_ONITEMICON | LVHT_ONITEMLABEL | LVHT_ONITEMSTATEICON)

        LVHT_ABOVE = 0x00000008
        LVHT_BELOW = 0x00000010
        LVHT_TORIGHT = 0x00000020
        LVHT_TOLEFT = 0x00000040


        LVHT_EX_GROUP_HEADER = 0x10000000
        LVHT_EX_GROUP_FOOTER = 0x20000000
        LVHT_EX_GROUP_COLLAPSE = 0x40000000
        LVHT_EX_GROUP_BACKGROUND = 0x80000000
        LVHT_EX_GROUP_STATEICON = 0x01000000
        LVHT_EX_GROUP_SUBSETLINK = 0x02000000
        LVHT_EX_GROUP = (LVHT_EX_GROUP_BACKGROUND | LVHT_EX_GROUP_COLLAPSE | LVHT_EX_GROUP_FOOTER | LVHT_EX_GROUP_HEADER | LVHT_EX_GROUP_STATEICON | LVHT_EX_GROUP_SUBSETLINK)
        LVHT_EX_ONCONTENTS = 0x04000000 # On item AND not on the background
        LVHT_EX_FOOTER = 0x08000000

        _LVHITTESTINFO_fields_ = [
                ("pt", POINT),
                ("flags", UINT),
                ("iItem", INT),
                ("iSubItem", INT) # this is was NOT in win95.  valid only for LVM_SUBITEMHITTEST
            ]
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            _LVHITTESTINFO_fields_.append(
                ("iGroup", INT) # readonly. index of group. only valid for owner data.
                                # supports single item in multiple groups.
            )
        
        class LVHITTESTINFO(CStructure):
            pt: POINT
            flags: int
            iItem: int
            iSubItem: int
            iGroup: int
            _fields_ = _LVHITTESTINFO_fields_
        LPLVHITTESTINFO = POINTER(LVHITTESTINFO)
        
        LV_HITTESTINFO = LVHITTESTINFO

        LVHITTESTINFO_V1_SIZE = CCSIZEOF_STRUCT(LVHITTESTINFO, "iItem")

        LVM_HITTEST = (LVM_FIRST + 18)

        def ListView_HitTest(hwndLV, pinfo):
            return SendMessage(hwndLV, LVM_HITTEST, 0, cast(pinfo, PVOID).value)
         
        def ListView_HitTestEx(hwndLV, pinfo):
            return SendMessage(hwndLV, LVM_HITTEST, -1, cast(pinfo, PVOID).value)

        LVM_ENSUREVISIBLE = (LVM_FIRST + 19)

        def ListView_EnsureVisible(hwndLV, i, fPartialOK):
            return SendMessage(hwndLV, LVM_ENSUREVISIBLE, i, MAKELPARAM(fPartialOK, 0))

        LVM_SCROLL = (LVM_FIRST + 20)

        def ListView_Scroll(hwndLV, dx, dy):
            return SendMessage(hwndLV, LVM_SCROLL, dx, dy)

        LVM_REDRAWITEMS = (LVM_FIRST + 21)

        def ListView_RedrawItems(hwndLV, iFirst, iLast):
            return SendMessage(hwndLV, LVM_REDRAWITEMS, iFirst, iLast)

        LVA_DEFAULT = 0x0000
        LVA_ALIGNLEFT = 0x0001
        LVA_ALIGNTOP = 0x0002
        LVA_SNAPTOGRID = 0x0005


        LVM_ARRANGE = (LVM_FIRST + 22)

        def ListView_Arrange(hwndLV, code):
            return SendMessage(hwndLV, LVM_ARRANGE, UINT(code).value, 0)

        LVM_EDITLABELA = (LVM_FIRST + 23)
        LVM_EDITLABELW = (LVM_FIRST + 118)
        LVM_EDITLABEL = unicode(LVM_EDITLABELW, LVM_EDITLABELA)

        def ListView_EditLabel(hwndLV, i):
            return SendMessage(hwndLV, LVM_EDITLABEL, i, 0)

        LVM_GETEDITCONTROL = (LVM_FIRST + 24)

        def ListView_GetEditControl(hwndLV):
            return SendMessage(hwndLV, LVM_GETEDITCONTROL, 0, 0)

        _LVCOLUMNA_fields_ = [
                ("mask", UINT),
                ("fmt", INT),
                ("cx", INT),
                ("pszText", LPSTR),
                ("cchTextMax", INT),
                ("iSubItem", INT),
                ("iImage", INT),
                ("iOrder", INT)
            ]

        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            _LVCOLUMNA_fields_.append(("cxMin", INT))      # min snap point
            _LVCOLUMNA_fields_.append(("cxDefault", INT))  # default snap point
            _LVCOLUMNA_fields_.append(("cxIdeal", INT))    # read only. ideal may not eqaul current width if auto sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
        
        class LVCOLUMNA(CStructure):
            _fields_ = _LVCOLUMNA_fields_
            mask: int
            fmt: int
            cx: int
            pszText: LPSTR
            cchTextMax: int
            iSubItem: int
            iImage: int
            iOrder: int
            cxMin: int
            cxDefault: int
            cxIdeal: int
        LPLVCOLUMNA = POINTER(LVCOLUMNA)

        _LVCOLUMNW_fields_ = [
                ("mask", UINT),
                ("fmt", INT),
                ("cx", INT),
                ("pszText", LPWSTR),
                ("cchTextMax", INT),
                ("iSubItem", INT),
                ("iImage", INT),
                ("iOrder", INT)
            ]

        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            _LVCOLUMNW_fields_.append(("cxMin", INT))      # min snap point
            _LVCOLUMNW_fields_.append(("cxDefault", INT))  # default snap point
            _LVCOLUMNW_fields_.append(("cxIdeal", INT))    # read only. ideal may not eqaul current width if auto sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
        
        class LVCOLUMNW(CStructure):
            _fields_ = _LVCOLUMNW_fields_
            mask: int
            fmt: int
            cx: int
            pszText: LPWSTR
            cchTextMax: int
            iSubItem: int
            iImage: int
            iOrder: int
            cxMin: int
            cxDefault: int
            cxIdeal: int
            
        LPLVCOLUMNW = POINTER(LVCOLUMNW)
        LVCOLUMN = unicode(LVCOLUMNW, LVCOLUMNA)
        LPLVCOLUMN = unicode(LPLVCOLUMNW, LPLVCOLUMNA)
        
        LV_COLUMNA = LVCOLUMNA
        LV_COLUMNW = LVCOLUMNW

        LV_COLUMN = LVCOLUMN

        LVCOLUMNA_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNA, "iSubItem")
        LVCOLUMNW_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNW, "iSubItem")
        
        LVCF_FMT = 0x0001
        LVCF_WIDTH = 0x0002
        LVCF_TEXT = 0x0004
        LVCF_SUBITEM = 0x0008
        LVCF_IMAGE = 0x0010
        LVCF_ORDER = 0x0020
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            LVCF_MINWIDTH = 0x0040
            LVCF_DEFAULTWIDTH = 0x0080
            LVCF_IDEALWIDTH = 0x0100
        # LVCFMT_ flags up to FFFF are shared with the header control(HDF_ flags).
        # Flags above FFFF are listview-specific.
        LVCFMT_LEFT = 0x0000 # Same as HDF_LEFT
        LVCFMT_RIGHT = 0x0001 # Same as HDF_RIGHT
        LVCFMT_CENTER = 0x0002 # Same as HDF_CENTER
        LVCFMT_JUSTIFYMASK = 0x0003 # Same as HDF_JUSTIFYMASK
        LVCFMT_IMAGE = 0x0800 # Same as HDF_IMAGE
        LVCFMT_BITMAP_ON_RIGHT = 0x1000 # Same as HDF_BITMAP_ON_RIGHT
        LVCFMT_COL_HAS_IMAGES = 0x8000 # Same as HDF_OWNERDRAW
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            LVCFMT_FIXED_WIDTH = 0x00100 # Can't resize the column; same as HDF_FIXEDWIDTH
            LVCFMT_NO_DPI_SCALE = 0x40000 # If not set, CCM_DPISCALE will govern scaling up fixed width
            LVCFMT_FIXED_RATIO = 0x80000 # Width will augment with the row height
            # The following flags
            LVCFMT_LINE_BREAK = 0x100000 # Move to the top of the next list of columns
            LVCFMT_FILL = 0x200000 # Fill the remainder of the tile area. Might have a title.
            LVCFMT_WRAP = 0x400000 # This sub-item can be wrapped.
            LVCFMT_NO_TITLE = 0x800000 # This sub-item doesn't have an title.
            LVCFMT_TILE_PLACEMENTMASK = (LVCFMT_LINE_BREAK | LVCFMT_FILL)
            LVCFMT_SPLITBUTTON = 0x1000000 # Column is a split button; same as HDF_SPLITBUTTON
        LVM_GETCOLUMNA = (LVM_FIRST + 25)
        LVM_GETCOLUMNW = (LVM_FIRST + 95)
        LVM_GETCOLUMN = unicode(LVM_GETCOLUMNW, LVM_GETCOLUMNA)
        
        def ListView_GetColumn(hwnd, iCol, pcol):
            return SendMessage(hwnd, LVM_GETCOLUMN, iCol, PtrUtil.get_address(pcol))
        
        LVM_SETCOLUMNA          = (LVM_FIRST + 26)
        LVM_SETCOLUMNW          = (LVM_FIRST + 96)
        LVM_SETCOLUMN = unicode(LVM_SETCOLUMNW, LVM_SETCOLUMNA)
        
        def ListBiew_SetColumn(hwnd, iCol, pcol):
            return SendMessage(hwnd, LVM_SETCOLUMN, iCol, PtrUtil.get_address(pcol))
        
        LVM_INSERTCOLUMNA       = (LVM_FIRST + 27)
        LVM_INSERTCOLUMNW       = (LVM_FIRST + 97)
        LVM_INSERTCOLUMN = unicode(LVM_INSERTCOLUMNW, LVM_INSERTCOLUMNA)
        
        def ListView_InsertColumn(hwnd, iCol, pcol):
            return SendMessage(hwnd, LVM_INSERTCOLUMN, iCol, PtrUtil.get_address(pcol))
        
        LVM_DELETECOLUMN = (LVM_FIRST + 28)
        
        def ListView_DeleteColumn(hwnd, iCol):
            return SendMessage(hwnd, LVM_DELETECOLUMN, iCol, 0)
        
        LVM_GETCOLUMNWIDTH = (LVM_FIRST + 29)
        
        def ListView_GetColumnWidth(hwnd, iCol):
            return SendMessage(hwnd, LVM_GETCOLUMNWIDTH, iCol, 0)
        
        LVSCW_AUTOSIZE = -1
        LVSCW_USEHEADER = -2
        LVM_SETCOLUMNWIDTH = (LVM_FIRST + 30)
        
        def ListView_SetColumnWidth(hwnd, iCol, cx):
            return SendMessage(hwnd, LVM_SETCOLUMNWIDTH, iCol, cx)
        
        LVM_GETHEADER = (LVM_FIRST + 31)
        
        def ListView_GetHeader(hwnd):
            return SendMessage(hwnd, LVM_GETHEADER, 0, 0)
        
        LVM_CREATEDRAGIMAGE = (LVM_FIRST + 33)
        
        def ListView_CreateDragImage(hwnd, i, lpptUpLeft):
            return SendMessage(hwnd, LVM_CREATEDRAGIMAGE, i, PtrUtil.get_address(lpptUpLeft))
        
        LVM_GETVIEWRECT = (LVM_FIRST + 34)
        
        def ListView_GetViewRect(hwnd, prc):
            return SendMessage(hwnd, LVM_GETVIEWRECT, 0, PtrUtil.get_address(prc))
        
        LVM_GETTEXTCOLOR = (LVM_FIRST + 35)
        
        def ListView_GetTextColor(hwnd):
            return SendMessage(hwnd, LVM_GETTEXTCOLOR, 0, 0)
        
        LVM_SETTEXTCOLOR = (LVM_FIRST + 36)
        
        def ListView_SetTextColor(hwnd, clrText):
            return SendMessage(hwnd, LVM_SETTEXTCOLOR, 0, clrText)
        
        LVM_GETTEXTBKCOLOR = (LVM_FIRST + 37)
        
        def ListView_GetTextBkColor(hwnd):
            return SendMessage(hwnd, LVM_GETTEXTBKCOLOR, 0, 0)
        
        LVM_SETTEXTBKCOLOR = (LVM_FIRST + 38)
        
        def ListView_SetTextBkColor(hwnd, clrTextBk):
            return SendMessage(hwnd, LVM_SETTEXTBKCOLOR, 0, clrTextBk)
        
        # FORCED DEVELOPMENT, NO MACROS
        
        LVM_GETTOPINDEX = (LVM_FIRST + 39)
        LVM_GETCOUNTPERPAGE = (LVM_FIRST + 40)
        LVM_GETORIGIN = (LVM_FIRST + 41)
        LVM_UPDATE = (LVM_FIRST + 42)
        LVM_SETITEMSTATE = (LVM_FIRST + 43)
        LVM_GETITEMSTATE = (LVM_FIRST + 44)
        LVM_GETITEMTEXTA = (LVM_FIRST + 45)
        LVM_GETITEMTEXTW = (LVM_FIRST + 115)
        LVM_GETITEMTEXT = unicode(LVM_GETITEMTEXTW, LVM_GETITEMTEXTA)
        LVM_SETITEMTEXTA = (LVM_FIRST + 46)
        LVM_SETITEMTEXTW = (LVM_FIRST + 116)
        LVM_SETITEMTEXT = unicode(LVM_SETITEMTEXTW, LVM_SETITEMTEXTA)
        
        # these flags only apply to LVS_OWNERDATA listviews in report or list mode
        LVSICF_NOINVALIDATEALL = 0x00000001
        LVSICF_NOSCROLL = 0x00000002
        LVM_SETITEMCOUNT = (LVM_FIRST + 47)
        PFNLVCOMPARE = CALLBACK(INT, LPARAM, LPARAM, LPARAM)
        LVM_SORTITEMS = (LVM_FIRST + 48)
        LVM_SETITEMPOSITION32 = (LVM_FIRST + 49)
        LVM_GETSELECTEDCOUNT = (LVM_FIRST + 50)
        LVM_GETITEMSPACING = (LVM_FIRST + 51)
        LVM_GETISEARCHSTRINGA = (LVM_FIRST + 52)
        LVM_GETISEARCHSTRINGW = (LVM_FIRST + 117)
        LVM_GETISEARCHSTRING = unicode(LVM_GETISEARCHSTRINGW, LVM_GETISEARCHSTRINGA)
        LVM_SETICONSPACING = (LVM_FIRST + 53)
        LVM_SETEXTENDEDLISTVIEWSTYLE = (LVM_FIRST + 54) # optional wParam == mask
        LVM_GETEXTENDEDLISTVIEWSTYLE = (LVM_FIRST + 55)
        LVS_EX_GRIDLINES = 0x00000001
        LVS_EX_SUBITEMIMAGES = 0x00000002
        LVS_EX_CHECKBOXES = 0x00000004
        LVS_EX_TRACKSELECT = 0x00000008
        LVS_EX_HEADERDRAGDROP = 0x00000010
        LVS_EX_FULLROWSELECT = 0x00000020 # applies to report mode only
        LVS_EX_ONECLICKACTIVATE = 0x00000040
        LVS_EX_TWOCLICKACTIVATE = 0x00000080
        LVS_EX_FLATSB = 0x00000100
        LVS_EX_REGIONAL = 0x00000200
        LVS_EX_INFOTIP = 0x00000400 # listview does InfoTips for you
        LVS_EX_UNDERLINEHOT = 0x00000800
        LVS_EX_UNDERLINECOLD = 0x00001000
        LVS_EX_MULTIWORKAREAS = 0x00002000
        LVS_EX_LABELTIP = 0x00004000 # listview unfolds partly hidden labels if it does not have infotip text
        LVS_EX_BORDERSELECT = 0x00008000 # border selection style instead of highlight
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            LVS_EX_DOUBLEBUFFER = 0x00010000
            LVS_EX_HIDELABELS = 0x00020000
            LVS_EX_SINGLEROW = 0x00040000
            LVS_EX_SNAPTOGRID = 0x00080000 # Icons automatically snap to grid.
            LVS_EX_SIMPLESELECT = 0x00100000 # Also changes overlay rendering to top right for icon mode.
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            LVS_EX_JUSTIFYCOLUMNS = 0x00200000 # Icons are lined up in columns that use up the whole view area.
            LVS_EX_TRANSPARENTBKGND = 0x00400000 # Background is painted by the parent via WM_PRINTCLIENT
            LVS_EX_TRANSPARENTSHADOWTEXT = 0x00800000 # Enable shadow text on transparent backgrounds only(useful with bitmaps)
            LVS_EX_AUTOAUTOARRANGE = 0x01000000 # Icons automatically arrange if no icon positions have been set
            LVS_EX_HEADERINALLVIEWS = 0x02000000 # Display column header in all view modes
            LVS_EX_AUTOCHECKSELECT = 0x08000000
            LVS_EX_AUTOSIZECOLUMNS = 0x10000000
            LVS_EX_COLUMNSNAPPOINTS = 0x40000000
            LVS_EX_COLUMNOVERFLOW = 0x80000000
        LVM_GETSUBITEMRECT = (LVM_FIRST + 56)
        LVM_SUBITEMHITTEST = (LVM_FIRST + 57)
        LVM_SETCOLUMNORDERARRAY = (LVM_FIRST + 58)
        LVM_GETCOLUMNORDERARRAY = (LVM_FIRST + 59)
        LVM_SETHOTITEM = (LVM_FIRST + 60)
        LVM_GETHOTITEM = (LVM_FIRST + 61)
        LVM_SETHOTCURSOR = (LVM_FIRST + 62)
        LVM_GETHOTCURSOR = (LVM_FIRST + 63)
        LVM_APPROXIMATEVIEWRECT = (LVM_FIRST + 64)
        LV_MAX_WORKAREAD = 16
        LVM_SETWORKAREAS = (LVM_FIRST + 65)
        LVM_GETWORKAREAS = (LVM_FIRST + 70)
        LVM_GETNUMBEROFWORKAREAD = (LVM_FIRST + 73)
        LVM_GETSELECTIONMARK = (LVM_FIRST + 66)
        LVM_SETSELECTIONMARK = (LVM_FIRST + 67)
        LVM_SETHOVERTIME = (LVM_FIRST + 71)
        LVM_GETHOVERTIME = (LVM_FIRST + 72)
        LVM_SETTOOLTIPS = (LVM_FIRST + 74)
        LVM_GETTOOLTIPS = (LVM_FIRST + 78)
        LVM_SORTITEMSEX = (LVM_FIRST + 81)
        
        class LVBKIMAGEA(CStructure):
            _fields_ = [
                ('ulFlags', ULONG),
                ('hbm', HBITMAP),
                ('pszImage', LPSTR),
                ('cchImageMax', UINT),
                ('xOffsetPercent', INT),
                ('yOffsetPercent', INT)
            ]
            
            ulFlags: int
            hbm: int
            pszImage: LPSTR
            cchImageMax: int
            xOffsetPercent: int
            yOffsetPercent: int

        LPLVBKIMAGEA = LVBKIMAGEA.PTR()
        
        class LVBKIMAGEW(CStructure):
            _fields_ = [
                ('ulFlags', ULONG),
                ('hbm', HBITMAP),
                ('pszImage', LPWSTR),
                ('cchImageMax', UINT),
                ('xOffsetPercent', INT),
                ('yOffsetPercent', INT)
            ]
            
            ulFlags: int
            hbm: int
            pszImage: LPWSTR
            cchImageMax: int
            xOffsetPercent: int
            yOffsetPercent: int
        
        LPLVBKIMAGEW = LVBKIMAGEW.PTR()
        
        LVBKIF_SOURCE_NONE = 0x00000000
        LVBKIF_SOURCE_HBITMAP = 0x00000001
        LVBKIF_SOURCE_URL = 0x00000002
        LVBKIF_SOURCE_MASK = 0x00000003
        LVBKIF_STYLE_NORMAL = 0x00000000
        LVBKIF_STYLE_TILE = 0x00000010
        LVBKIF_STYLE_MASK = 0x00000010
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            LVBKIF_FLAG_TILEOFFSET = 0x00000100
            LVBKIF_TYPE_WATERMARK = 0x10000000
            LVBKIF_FLAG_ALPHABLEND = 0x20000000
        LVM_SETBKIMAGEA = (LVM_FIRST + 68)
        LVM_SETBKIMAGEW = (LVM_FIRST + 138)
        LVM_GETBKIMAGEA = (LVM_FIRST + 69)
        LVM_GETBKIMAGEW = (LVM_FIRST + 139)
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            LVM_SETSELECTEDCOLUMN = (LVM_FIRST + 140)
            LV_VIEW_ICON = 0x0000
            LV_VIEW_DETAILS = 0x0001
            LV_VIEW_SMALLICON = 0x0002
            LV_VIEW_LIST = 0x0003
            LV_VIEW_TILE = 0x0004
            LV_VIEW_MAX = 0x0004
            LVM_SETVIEW = (LVM_FIRST + 142)
            LVM_GETVIEW = (LVM_FIRST + 143)
            LVGF_NONE = 0x00000000
            LVGF_HEADER = 0x00000001
            LVGF_FOOTER = 0x00000002
            LVGF_STATE = 0x00000004
            LVGF_ALIGN = 0x00000008
            LVGF_GROUPID = 0x00000010
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                LVGF_SUBTITLE = 0x00000100 # pszSubtitle is valid
                LVGF_TASK = 0x00000200 # pszTask is valid
                LVGF_DESCRIPTIONTOP = 0x00000400 # pszDescriptionTop is valid
                LVGF_DESCRIPTIONBOTTOM = 0x00000800 # pszDescriptionBottom is valid
                LVGF_TITLEIMAGE = 0x00001000 # iTitleImage is valid
                LVGF_EXTENDEDIMAGE = 0x00002000 # iExtendedImage is valid
                LVGF_ITEMS = 0x00004000 # iFirstItem and cItems are valid
                LVGF_SUBSET = 0x00008000 # pszSubsetTitle is valid
                LVGF_SUBSETITEMS = 0x00010000 # readonly, cItems holds count of items in visible subset, iFirstItem is valid
            LVGS_NORMAL = 0x00000000
            LVGS_COLLAPSED = 0x00000001
            LVGS_HIDDEN = 0x00000002
            LVGS_NOHEADER = 0x00000004
            LVGS_COLLAPSIBLE = 0x00000008
            LVGS_FOCUSED = 0x00000010
            LVGS_SELECTED = 0x00000020
            LVGS_SUBSETED = 0x00000040
            LVGS_SUBSETLINKFOCUSED = 0x00000080
            LVGA_HEADER_LEFT = 0x00000001
            LVGA_HEADER_CENTER = 0x00000002
            LVGA_HEADER_RIGHT = 0x00000004 # Don't forget to validate exclusivity
            LVGA_FOOTER_LEFT = 0x00000008
            LVGA_FOOTER_CENTER = 0x00000010
            LVGA_FOOTER_RIGHT = 0x00000020 # Don't forget to validate exclusivity
            
            class LVGROUP(CStructure):
                fields = [
                    ('cbSize', UINT),
                    ('mask', UINT),
                    ('pszHeader', LPWSTR),
                    ('cchHeader', INT),
                    ('pszFooter', LPWSTR),
                    ('cchFooter', INT),
                    ('iGroupId', INT),
                    ('stateMask', UINT),
                    ('state', UINT),
                    ('uAlign', UINT)
                ]
                if cpreproc.getdef('_WINVER') >= WIN32_WINNT_VISTA:
                    fields.extend([
                        ('pszSubtitle', LPWSTR),
                        ('cchSubtitle', UINT),
                        ('pszTask', LPWSTR),
                        ('cchTask', UINT),
                        ('pszDescriptionTop', LPWSTR),
                        ('cchDescriptionTop', UINT),
                        ('pszDescriptionBottom', LPWSTR),
                        ('cchDescriptionBottom', UINT),
                        ('iTitleImage', INT),
                        ('iExtendedImage', INT),
                        ('iFirstItem', INT),
                        ('cItems', UINT),
                        ('pszSubsetTitle', LPWSTR),
                        ('cchSubsetTitle', UINT)
                    ])
                
                cbSize: int
                mask: int
                pszHeader: LPWSTR
                cchHeader: int
                
                pszFooter: LPWSTR
                cchFooter: int
                
                iGroupId: int
                
                stateMask: int
                state: int
                uAlign: int
                
                iExtendedImage: int # Read only
                cItems: int # Read only
                pszSubsetTitle: LPWSTR # NULL if group is not subset
                cchSubsetTitle: int
            
            declare_fields(LVGROUP)
            
            LVGROUP_V5_SIZE = CCSIZEOF_STRUCT(LVGROUP, 'uAlign')
            PLVGROUP = LVGROUP.PTR()
            LVM_INSERTGROUP = (LVM_FIRST + 145)
            LVM_SETGROUPINFO = (LVM_FIRST + 147)
            LVM_GETGROUPINFO = (LVM_FIRST + 149)
            LVM_REMOVEGROUP = (LVM_FIRST + 150)
            LVM_MOVEGROUP = (LVM_FIRST + 151)
            LVM_GETGROUPCOUNT = (LVM_FIRST + 152)
            LVM_GETGROUPINFOBYINDEX = (LVM_FIRST + 153)
            LVM_MOVEITEMTOGROUP = (LVM_FIRST + 154)
            LVGGR_GROUP = 0 # Entire expanded group
            LVGGR_HEADER = 1 # Header only(collapsed group)
            LVGGR_LABEL = 2 # Label only
            LVGGR_SUBSETLINK = 3 # subset link only
            LVM_GETGROUPRECT = (LVM_FIRST + 98)
            LVGMF_NONE = 0x00000000
            LVGMF_BORDERSIZE = 0x00000001
            LVGMF_BORDERCOLOR = 0x00000002
            LVGMF_TEXTCOLOR = 0x00000004

            class LVGROUPMETRICS(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('mask', UINT),
                    ('Left', UINT),
                    ('Top', UINT),
                    ('Right', UINT),
                    ('Bottom', UINT),
                    ('crLeft', COLORREF),
                    ('crTop', COLORREF),
                    ('crRight', COLORREF),
                    ('crBottom', COLORREF),
                    ('crHeader', COLORREF),
                    ('crFooter', COLORREF)
                ]
                cbSize: int
                mask: int
                Left: int
                Top: int
                Right: int
                Bottom: int
                crLeft: int
                crTop: int
                crRight: int
                crBottom: int
                crHeader: int
                crFooter: int
            PLVGROUPMETRICS = LVGROUPMETRICS.PTR()

            LVM_SETGROUPMETRICS = (LVM_FIRST + 155)
            LVM_GETGROUPMETRICS = (LVM_FIRST + 156)
            LVM_ENABLEGROUPVIEW = (LVM_FIRST + 157)
            # typedef int(CALLBACK *PFNLVGROUPCOMPARE)(int, int, void *);
            PFNLVGROUPCOMPARE = CALLBACK(INT, INT, INT, PVOID)
            LVM_SORTGROUPS = (LVM_FIRST + 158)

            class LVINSERTGROUPSORTED(CStructure):
                _fields_ = [
                    ('pfnGroupCompare', PFNLVGROUPCOMPARE),
                    ('pvData', PVOID),
                    ('lvGroup', LVGROUP)
                ]
                pfnGroupCompare: FARPROC
                pvData: int
                lvGroup: LVGROUP
            PLVINSERTGROUPSORTED = LVINSERTGROUPSORTED.PTR()

            LVM_INSERTGROUPSORTED = (LVM_FIRST + 159)
            LVM_REMOVEALLGROUPS = (LVM_FIRST + 160)
            LVM_HASGROUP = (LVM_FIRST + 161)
            LVM_GETGROUPSTATE = (LVM_FIRST + 92)
            LVM_GETFOCUSEDGROUP = (LVM_FIRST + 93)
            LVTVIF_AUTOSIZE = 0x00000000
            LVTVIF_FIXEDWIDTH = 0x00000001
            LVTVIF_FIXEDHEIGHT = 0x00000002
            LVTVIF_FIXEDSIZE = 0x00000003
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                LVTVIF_EXTENDED = 0x00000004
            LVTVIM_TILESIZE = 0x00000001
            LVTVIM_COLUMNS = 0x00000002
            LVTVIM_LABELMARGIN = 0x00000004

            class LVTILEVIEWINFO(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('dwMask', DWORD),
                    ('dwFlags', DWORD),
                    ('sizeTile', SIZE),
                    ('cLines', INT),
                    ('rcLabelMargin', RECT)
                ]
                cbSize: int
                dwMask: int
                dwFlags: int
                sizeTile: SIZE
                cLines: int
                rcLabelMargin: RECT
            PLVTILEVIEWINFO = LVTILEVIEWINFO.PTR()

            class LVTILEINFO(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('iItem', INT),
                    ('cColumns', UINT),
                    ('puColumns', PUINT)
                ]
                if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                    _fields_.append(('piColFmt', PINT))
                cbSize: int
                iItem: int
                cColumns: int
                puColumns: PUINT
                piColFmt: PINT
            PLVTILEINFO = LVTILEINFO.PTR()

            LVTILEINFO_V5_SIZE = CCSIZEOF_STRUCT(LVTILEINFO, 'puColumns')
            LVM_SETTILEVIEWINFO = (LVM_FIRST + 162)
            LVM_GETTILEVIEWINFO = (LVM_FIRST + 163)
            LVM_SETTILEINFO = (LVM_FIRST + 164)
            LVM_GETTILEINFO = (LVM_FIRST + 165)

            class LVINSERTMARK(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('dwFlags', DWORD),
                    ('iItem', INT),
                    ('dwReserved', DWORD)
                ]
                cbSize: int
                dwFlags: int
                iItem: int
                dwReserved: int
            LPLVINSERTMARK = LVINSERTMARK.PTR()

            LVIM_AFTER = 0x00000001 # TRUE = insert After iItem, otherwise before
            LVM_SETINSERTMARK = (LVM_FIRST + 166)
            LVM_GETINSERTMARK = (LVM_FIRST + 167)
            LVM_INSERTMARKHITTEST = (LVM_FIRST + 168)
            LVM_GETINSERTMARKRECT = (LVM_FIRST + 169)
            LVM_SETINSERTMARKCOLOR = (LVM_FIRST + 170)
            LVM_GETINSERTMARKCOLOR = (LVM_FIRST + 171)

            class LVSETINFOTIP(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('dwFlags', DWORD),
                    ('pszText', LPWSTR),
                    ('iItem', INT),
                    ('iSubItem', INT)
                ]
                cbSize: int
                dwFlags: int
                pszText: LPWSTR
                iItem: int
                iSubItem: int
            PLVSETINFOTIP = LVSETINFOTIP.PTR()

            LVM_SETINFOTIP = (LVM_FIRST + 173)
            LVM_GETSELECTEDCOLUMN = (LVM_FIRST + 174)
            LVM_ISGROUPVIEWENABLED = (LVM_FIRST + 175)
            LVM_GETOUTLINECOLOR = (LVM_FIRST + 176)
            LVM_SETOUTLINECOLOR = (LVM_FIRST + 177)
            LVM_CANCELEDITLABEL = (LVM_FIRST + 179)
            # These next to methods make it easy to identify an item that can be repositioned
            # within listview. For example: Many developers use the lParam to store an identifier that is
            # unique. Unfortunatly, in order to find this item, they have to iterate through all of the items
            # in the listview. Listview will maintain a unique identifier.  The upper bound is the size of a DWORD.
            LVM_MAPINDEXTOID = (LVM_FIRST + 180)
            LVM_MAPIDTOINDEX = (LVM_FIRST + 181)
            LVM_ISITEMVISIBLE = (LVM_FIRST + 182)
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                LVM_GETEMPTYTEXT = (LVM_FIRST + 204)
                LVM_GETFOOTERRECT = (LVM_FIRST + 205)
                # footer flags
                LVFF_ITEMCOUNT = 0x00000001

                class LVFOOTERINFO(CStructure):
                    _fields_ = [
                        ('mask', UINT),
                        ('pszText', LPWSTR),
                        ('cchTextMax', INT),
                        ('cItems', UINT)
                    ]
                    mask: int
                    pszText: LPWSTR
                    cchTextMax: int
                    cItems: int
                LPLVFOOTERINFO = LVFOOTERINFO.PTR()

                LVM_GETFOOTERINFO = (LVM_FIRST + 206)
                LVM_GETFOOTERITEMRECT = (LVM_FIRST + 207)
                # footer item flags
                LVFIF_TEXT = 0x00000001
                LVFIF_STATE = 0x00000002
                # footer item state
                LVFIS_FOCUSED = 0x0001

                class LVFOOTERITEM(CStructure):
                    _fields_ = [
                        ('mask', UINT),
                        ('iItem', INT),
                        ('pszText', LPWSTR),
                        ('cchTextMax', INT),
                        ('state', UINT),
                        ('stateMask', UINT)
                    ]
                    mask: int
                    iItem: int
                    pszText: LPWSTR
                    cchTextMax: int
                    state: int
                    stateMask: int
                LPLVFOOTERITEM = LVFOOTERITEM.PTR()

                LVM_GETFOOTERITEM = (LVM_FIRST + 208)
                # supports a single item in multiple groups.

                class LVITEMINDEX(CStructure):
                    _fields_ = [
                        ('iItem', INT),
                        ('iGroup', INT)
                    ]
                    iItem: int
                    iGroup: int
                PLVITEMINDEX = LVITEMINDEX.PTR()

                LVM_GETITEMINDEXRECT = (LVM_FIRST + 209)
                LVM_SETITEMINDEXSTATE = (LVM_FIRST + 210)
                LVM_GETNEXTITEMINDEX = (LVM_FIRST + 211)
            LVBKIMAGE = unicode(LVBKIMAGEW, LVBKIMAGEA)
            LPLVBKIMAGE = unicode(LPLVBKIMAGEW, LPLVBKIMAGEA)
            LVM_SETBKIMAGE = unicode(LVM_SETBKIMAGEW, LVM_SETBKIMAGEA)
            LVM_GETBKIMAGE = unicode(LVM_GETBKIMAGEW, LVM_GETBKIMAGEA)

            class NMLISTVIEW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT),
                    ('uChanged', UINT),
                    ('ptAction', POINT),
                    ('lParam', LPARAM)
                ]
                hdr: NMHDR
                iItem: int
                iSubItem: int
                uNewState: int
                uNewState: int
                uOldState: int
                uChanged: int
                ptAction: POINT
                lParam: int
            LPNMLISTVIEW = NMLISTVIEW.PTR()
            LPNM_LISTVIEW = LPNMLISTVIEW
            NM_LISTVIEW = NMLISTVIEW

            # NMITEMACTIVATE is used instead of NMLISTVIEW in IE >= 0x400
            # therefore all the fields are the same except for extra uKeyFlags
            # they are used to store key flags at the time of the single click with
            # delayed activation - because by the time the timer goes off a user may
            # not hold the keys(shift, ctrl) any more

            class NMITEMACTIVATE(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT),
                    ('uChanged', UINT),
                    ('ptAction', POINT),
                    ('lParam', LPARAM),
                    ('uKeyFlags', UINT)
                ]
                hdr: NMHDR
                iItem: int
                iSubItem: int
                uNewState: int
                uOldState: int
                uChanged: int
                ptAction: POINT
                lParam: int
                uKeyFlags: int
            LPNMITEMACTIVATE = NMITEMACTIVATE.PTR()
            
            # key flags stored in uKeyFlags
            LVKF_ALT = 0x0001
            LVKF_CONTROL = 0x0002
            LVKF_SHIFT = 0x0004

            class NMLVCUSTOMDRAW(CStructure):
                _fields_ = [
                    ('nmcd', NMCUSTOMDRAW),
                    ('clrText', COLORREF),
                    ('clrTextBk', COLORREF),
                    ('iSubItem', INT)
                ]
                if cpreproc.get_version() >= WIN32_WINNT_WINXP:
                    _fields_.extend([
                        ('dwItemType', DWORD),
                        ('clrFace', COLORREF),
                        ('iIconEffect', INT),
                        ('iIconPhase', INT),
                        ('iPartId', INT),
                        ('iStateId', INT),
                        ('rcText', RECT),
                        ('uAlign', UINT)
                    ])
                nmcd: NMCUSTOMDRAW
                clrText: int
                clrTextBk: int
                iSubItem: int
                dwItemType: int
                clrFace: int
                iIconEffect: int
                iIconPhase: int
                iPartId: int
                iStateId: int
                rcText: RECT
                uAlign: int
            LPNMLVCUSTOMDRAW = NMLVCUSTOMDRAW.PTR()
            NMLVCUSTOMDRAW_V3_SIZE = CCSIZEOF_STRUCT(NMLVCUSTOMDRAW, 'clrTextBk')

            # dwItemType
            LVCDI_ITEM = 0x00000000
            LVCDI_GROUP = 0x00000001
            LVCDI_ITEMSLIST = 0x00000002
            # ListView custom draw return values
            LVCDRF_NOSELECT = 0x00010000
            LVCDRF_NOGROUPFRAME = 0x00020000

            class NMLVCACHEHINT(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iFrom', INT),
                    ('iTo', INT)
                ]
                hdr: NMHDR
                iFrom: int
                iTo: int
            LPNMLVCACHEHINT = NMLVCACHEHINT.PTR()

            LPNM_CACHEHINT = LPNMLVCACHEHINT
            PNM_CACHEHINT = LPNMLVCACHEHINT
            NM_CACHEHINT = NMLVCACHEHINT

            class NMLVFINDITEMA(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iStart', INT),
                    ('lvfi', LVFINDINFOA)
                ]
                hdr: NMHDR
                iStart: int
                lvfi: LVFINDINFOA
            LPNMLVFINDITEMA = NMLVFINDITEMA.PTR()

            class NMLVFINDITEMW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iStart', INT),
                    ('lvfi', LVFINDINFOW)
                ]
                hdr: NMHDR
                iStart: int
                lvfi: LVFINDINFOW
            LPNMLVFINDITEMW = NMLVFINDITEMW.PTR()

            PNM_FINDITEMA = LPNMLVFINDITEMA
            LPNM_FINDITEMA = LPNMLVFINDITEMA
            NM_FINDITEMA = NMLVFINDITEMA
            PNM_FINDITEMW = LPNMLVFINDITEMW
            LPNM_FINDITEMW = LPNMLVFINDITEMW
            NM_FINDITEMW = NMLVFINDITEMW
            PNM_FINDITEM = unicode(PNM_FINDITEMW, PNM_FINDITEMA)
            LPNM_FINDITEM = unicode(LPNM_FINDITEMW, LPNM_FINDITEMA)
            NM_FINDITEM = unicode(NM_FINDITEMW, NM_FINDITEMA)
            NMLVFINDITEM = unicode(NMLVFINDITEMW, NMLVFINDITEMA)
            LPNMLVFINDITEM = unicode(LPNMLVFINDITEMW, LPNMLVFINDITEMA)

            class NMLVODSTATECHANGE(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('iFrom', INT),
                    ('iTo', INT),
                    ('uNewState', UINT),
                    ('uOldState', UINT)
                ]
                hdr: NMHDR
                iFrom: int
                iTo: int
                uNewState: int
                uOldState: int
            LPNMLVODSTATECHANGE = NMLVODSTATECHANGE.PTR()

            PNM_ODSTATECHANGE = LPNMLVODSTATECHANGE
            LPNM_ODSTATECHANGE = LPNMLVODSTATECHANGE
            NM_ODSTATECHANGE = NMLVODSTATECHANGE
            LVN_ITEMCHANGING = (LVN_FIRST-0)
            LVN_ITEMCHANGED = (LVN_FIRST-1)
            LVN_INSERTITEM = (LVN_FIRST-2)
            LVN_DELETEITEM = (LVN_FIRST-3)
            LVN_DELETEALLITEMS = (LVN_FIRST-4)
            LVN_BEGINLABELEDITA = (LVN_FIRST-5)
            LVN_BEGINLABELEDITW = (LVN_FIRST-75)
            LVN_ENDLABELEDITA = (LVN_FIRST-6)
            LVN_ENDLABELEDITW = (LVN_FIRST-76)
            LVN_COLUMNCLICK = (LVN_FIRST-8)
            LVN_BEGINDRAG = (LVN_FIRST-9)
            LVN_BEGINRDRAG = (LVN_FIRST-11)
            LVN_ODCACHEHINT = (LVN_FIRST-13)
            LVN_ODFINDITEMA = (LVN_FIRST-52)
            LVN_ODFINDITEMW = (LVN_FIRST-79)
            LVN_ITEMACTIVATE = (LVN_FIRST-14)
            LVN_ODSTATECHANGED = (LVN_FIRST-15)
            LVN_ODFINDITEM = unicode(LVN_ODFINDITEMW, LVN_ODFINDITEMA)
            LVN_HOTTRACK = (LVN_FIRST-21)
            LVN_GETDISPINFOA = (LVN_FIRST-50)
            LVN_GETDISPINFOW = (LVN_FIRST-77)
            LVN_SETDISPINFOA = (LVN_FIRST-51)
            LVN_SETDISPINFOW = (LVN_FIRST-78)
            LVN_BEGINLABELEDIT = unicode(LVN_BEGINLABELEDITW, LVN_BEGINLABELEDITA)
            LVN_ENDLABELEDIT = unicode(LVN_ENDLABELEDITW, LVN_ENDLABELEDITA)
            LVN_GETDISPINFO = unicode(LVN_GETDISPINFOW, LVN_GETDISPINFOA)
            LVN_SETDISPINFO = unicode(LVN_SETDISPINFOW, LVN_SETDISPINFOA)
            LVIF_DI_SETITEM = 0x1000

            class NMLVDISPINFOA(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('item', LVITEMA)
                ]
                hdr: NMHDR
                item: LVITEMA
            LPNMLVDISPINFOA = NMLVDISPINFOA.PTR()

            class NMLVDISPINFOW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('item', LVITEMW)
                ]
                hdr: NMHDR
                item: LVITEMW
            LPNMLVDISPINFOW = NMLVDISPINFOW.PTR()

            NMLVDISPINFO = unicode(NMLVDISPINFOW, NMLVDISPINFOA)
            LV_DISPINFOA = NMLVDISPINFOA
            LV_DISPINFOW = NMLVDISPINFOW
            LV_DISPINFO = NMLVDISPINFO
            LVN_KEYDOWN = (LVN_FIRST-55)

            class NMLVKEYDOWN(CStructure):
                _pack_ = 1
                _fields_ = [
                    ('hdr', NMHDR),
                    ('wVKey', WORD),
                    ('flags', UINT)
                ]
                hdr: NMHDR
                wVKey: int
                flags: int
            LPNMLVKEYDOWN = NMLVKEYDOWN.PTR()
            LV_KEYDOWN = NMLVKEYDOWN

            LVN_MARQUEEBEGIN = (LVN_FIRST-56)
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:

                class NMLVLINK(CStructure):
                    _fields_ = [
                        ('hdr', NMHDR),
                        ('link', LITEM),
                        ('iItem', INT),
                        ('iSubItem', INT)
                    ]
                    hdr: NMHDR
                    link: LITEM
                    iItem: int
                    iSubItem: int
                PNMLVLINK = NMLVLINK.PTR()


            class NMLVGETINFOTIPA(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlags', DWORD),
                    ('pszText', LPSTR),
                    ('cchTextMax', INT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('lParam', LPARAM)
                ]
                hdr: NMHDR
                dwFlags: int
                pszText: LPSTR
                cchTextMax: int
                iItem: int
                iSubItem: int
                lParam: int
            LPNMLVGETINFOTIPA = NMLVGETINFOTIPA.PTR()


            class NMLVGETINFOTIPW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlags', DWORD),
                    ('pszText', LPWSTR),
                    ('cchTextMax', INT),
                    ('iItem', INT),
                    ('iSubItem', INT),
                    ('lParam', LPARAM)
                ]
                hdr: NMHDR
                dwFlags: int
                pszText: LPWSTR
                cchTextMax: int
                iItem: int
                iSubItem: int
                lParam: int
            LPNMLVGETINFOTIPW = NMLVGETINFOTIPW.PTR()

            # NMLVGETINFOTIPA.dwFlag values
            LVGIT_UNFOLDED = 0x0001
            LVN_GETINFOTIPA = (LVN_FIRST-57)
            LVN_GETINFOTIPW = (LVN_FIRST-58)
            LVN_GETINFOTIP = unicode(LVN_GETINFOTIPW, LVN_GETINFOTIPA)
            NMLVGETINFOTIP = unicode(NMLVGETINFOTIPW, NMLVGETINFOTIPA)
            LPNMLVGETINFOTIP = unicode(LPNMLVGETINFOTIPW, LPNMLVGETINFOTIPA)
            #
            #  LVN_INCREMENTALSEARCH gives the app the opportunity to customize
            #  incremental search.  For example, if the items are numeric,
            #  the app can do numerical search instead of string search.
            #
            #  ListView notifies the app with NMLVFINDITEM.
            #  The app sets pnmfi->lvfi.lParam to the result of the incremental search,
            #  or to LVNSCH_DEFAULT if ListView should do the default search,
            #  or to LVNSCH_ERROR to fail the search and just beep,
            #  or to LVNSCH_IGNORE to stop all ListView processing.
            #
            #  The return value is not used.
            LVNSCH_DEFAULT = -1
            LVNSCH_ERROR = -2
            LVNSCH_IGNORE = -3
            LVN_INCREMENTALSEARCHA = (LVN_FIRST-62)
            LVN_INCREMENTALSEARCHW = (LVN_FIRST-63)
            LVN_INCREMENTALSEARCH = unicode(LVN_INCREMENTALSEARCHW, LVN_INCREMENTALSEARCHA)
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                LVN_COLUMNDROPDOWN = (LVN_FIRST-64)
                LVN_COLUMNOVERFLOWCLICK = (LVN_FIRST-66)
            #(WIN32_WINNT_VERSION >= WIN32_WINNT_VISTA)
            if cpreproc.get_version() >= WIN32_WINNT_WINXP:
                class NMLVSCROLL(CStructure):
                    _fields_ = [
                        ('hdr', NMHDR),
                        ('dx', INT),
                        ('dy', INT)
                    ]
                    hdr: NMHDR
                    dx: int
                    dy: int
                LPNMLVSCROLL = NMLVSCROLL.PTR()

                LVN_BEGINSCROLL = (LVN_FIRST-80)
                LVN_ENDSCROLL = (LVN_FIRST-81)
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                LVN_LINKCLICK = (LVN_FIRST-84)
                EMF_CENTERED = 0x00000001 # render markup centered in the listview area

                class NMLVEMPTYMARKUP(CStructure):
                    _fields_ = [
                        ('hdr', NMHDR),
                        ('dwFlags', DWORD),
                        ('szMarkup', WCHAR * L_MAX_URL_LENGTH)
                    ]
                    hdr: NMHDR
                    dwFlags: int
                    szMarkup: IWideCharArray

                LVN_GETEMPTYMARKUP = (LVN_FIRST-87)
    
    #====== TREEVIEW CONTROL =====================================================
    if cpreproc.ifndef("NOTREEVIEW"):
        WC_TREEVIEWA = b"SysTreeView32"
        WC_TREEVIEWW = u"SysTreeView32"
        WC_TREEVIEW = WC_TREEVIEWW
        # begin_r_commctrl
        TVS_HASBUTTONS = 0x0001
        TVS_HASLINES = 0x0002
        TVS_LINESATROOT = 0x0004
        TVS_EDITLABELS = 0x0008
        TVS_DISABLEDRAGDROP = 0x0010
        TVS_SHOWSELALWAYS = 0x0020
        TVS_RTLREADING = 0x0040
        TVS_NOTOOLTIPS = 0x0080
        TVS_CHECKBOXES = 0x0100
        TVS_TRACKSELECT = 0x0200
        TVS_SINGLEEXPAND = 0x0400
        TVS_INFOTIP = 0x0800
        TVS_FULLROWSELECT = 0x1000
        TVS_NOSCROLL = 0x2000
        TVS_NONEVENHEIGHT = 0x4000
        TVS_NOHSCROLL = 0x8000 # TVS_NOSCROLL overrides this
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            TVS_EX_NOSINGLECOLLAPSE = 0x0001
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            TVS_EX_MULTISELECT = 0x0002
            TVS_EX_DOUBLEBUFFER = 0x0004
            TVS_EX_NOINDENTSTATE = 0x0008
            TVS_EX_RICHTOOLTIP = 0x0010
            TVS_EX_AUTOHSCROLL = 0x0020
            TVS_EX_FADEINOUTEXPANDOS = 0x0040
            TVS_EX_PARTIALCHECKBOXES = 0x0080
            TVS_EX_EXCLUSIONCHECKBOXES = 0x0100
            TVS_EX_DIMMEDCHECKBOXES = 0x0200
            TVS_EX_DRAWIMAGEASYNC = 0x0400
        # end_r_commctrl
        HTREEITEM = HANDLE

        TVIF_TEXT = 0x0001
        TVIF_IMAGE = 0x0002
        TVIF_PARAM = 0x0004
        TVIF_STATE = 0x0008
        TVIF_HANDLE = 0x0010
        TVIF_SELECTEDIMAGE = 0x0020
        TVIF_CHILDREN = 0x0040
        TVIF_INTEGRAL = 0x0080
        if WIN32_IE >= WIN32_IE_IE60:
            TVIF_STATEEX = 0x0100
            TVIF_EXPANDEDIMAGE = 0x0200
        TVIS_SELECTED = 0x0002
        TVIS_CUT = 0x0004
        TVIS_DROPHILITED = 0x0008
        TVIS_BOLD = 0x0010
        TVIS_EXPANDED = 0x0020
        TVIS_EXPANDEDONCE = 0x0040
        TVIS_EXPANDPARTIAL = 0x0080
        TVIS_OVERLAYMASK = 0x0F00
        TVIS_STATEIMAGEMASK = 0xF000
        TVIS_USERMASK = 0xF000
        if WIN32_IE >= WIN32_IE_IE60:
            TVIS_EX_FLAT = 0x0001
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                TVIS_EX_DISABLED = 0x0002
            TVIS_EX_ALL = 0x0002
            # Structure for TreeView's NM_TVSTATEIMAGECHANGING notification

            class NMTVSTATEIMAGECHANGING(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('hti', HTREEITEM),
                    ('iOldStateImageIndex', INT),
                    ('iNewStateImageIndex', INT)
                ]
                hdr: NMHDR
                hti: int
                iOldStateImageIndex: int
                iNewStateImageIndex: int
            LPNMTVSTATEIMAGECHANGING = NMTVSTATEIMAGECHANGING.PTR()

        I_CHILDRENCALLBACK = (-1)
        I_CHILDRENAUTO = (-2)

        class TVITEMA(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('hItem', HTREEITEM),
                ('state', UINT),
                ('stateMask', UINT),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('cChildren', INT),
                ('lParam', LPARAM)
            ]
            mask: int
            hItem: int
            state: int
            stateMask: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            cChildren: int
            lParam: int

        LPTVITEMA = TVITEMA.PTR()

        class TVITEMW(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('hItem', HTREEITEM),
                ('state', UINT),
                ('stateMask', UINT),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('cChildren', INT),
                ('lParam', LPARAM)
            ]
            mask: int
            hItem: int
            state: int
            stateMask: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            cChildren: int
            lParam: int
            
        LPTVITEMW = TVITEMW.PTR()

        class TVITEMEXA(CStructure):
            fields = [
                ('mask', UINT),
                ('hItem', HTREEITEM),
                ('state', UINT),
                ('stateMask', UINT),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('cChildren', INT),
                ('lParam', LPARAM),
                ('iIntegral', INT)
            ]
            if WIN32_IE >= WIN32_IE_IE60:
                fields.extend([
                    ('uStateEx', UINT),
                    ('hwnd', HWND),
                    ('iExpandedImage', INT)
                ])
            if cpreproc.get_version() >= WIN32_WINNT_WIN7:
                fields.append(('iReserved', INT))
            mask: int
            hItem: int
            state: int
            stateMask: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            cChildren: int
            lParam: int
            iIntegral: int
            uStateEx: int
            hwnd: int
            iExpandedImage: int
            iReserved: int
        declare_fields(TVITEMEXA)
        LPTVITEMEXA = TVITEMEXA.PTR()

        class TVITEMEXW(CStructure):
            fields = [
                ('mask', UINT),
                ('hItem', HTREEITEM),
                ('state', UINT),
                ('stateMask', UINT),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('cChildren', INT),
                ('lParam', LPARAM),
                ('iIntegral', INT)
            ]
            if WIN32_IE >= WIN32_IE_IE60:
                fields.extend([
                    ('uStateEx', UINT),
                    ('hwnd', HWND),
                    ('iExpandedImage', INT)
                ])
            if cpreproc.get_version() >= WIN32_WINNT_WIN7:
                fields.append(('iReserved', INT))
            mask: int
            hItem: int
            state: int
            stateMask: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            cChildren: int
            lParam: int
            iIntegral: int
            uStateEx: int
            hwnd: int
            iExpandedImage: int
            iReserved: int
        declare_fields(TVITEMEXW)
        LPTVITEMEXW = TVITEMEXW.PTR()

        # UNICODE
        TVITEM = unicode(TVITEMW, TVITEMA)
        LPTVITEM = unicode(LPTVITEMW, LPTVITEMA)
        
        LPTV_ITEMW = LPTVITEMW
        LPTV_ITEMA = LPTVITEMA
        TV_ITEMW = TVITEMW
        TV_ITEMA = TVITEMA
        LPTV_ITEM = LPTVITEM
        TV_ITEM = TVITEM
        
        LPTVITEMW = TVITEMW.PTR()
        LPTV_ITEMW = LPTVITEMW
        LPTV_ITEMA = LPTVITEMA
        TV_ITEMW = TVITEMW
        TV_ITEMA = TVITEMA
        LPTV_ITEM = LPTVITEM
        TV_ITEM = TVITEM
        TVI_ROOT = HTREEITEM(ULONG_PTR(-0x10000).value).value
        TVI_FIRST = HTREEITEM(ULONG_PTR(-0x0FFFF).value).value
        TVI_LAST = HTREEITEM(ULONG_PTR(-0x0FFFE).value).value
        TVI_SORT = HTREEITEM(ULONG_PTR(-0x0FFFD).value).value

        class TVINSERTSTRUCTA(CStructure):
            class _U(CUnion):
                _fields_ = [
                    ('itemex', TVITEMEXA),
                    ('item', TVITEMA)
                ]
            _fields_ = [
                ('hParent', HTREEITEM),
                ('hInsertAfter', HTREEITEM),
                ('_u', _U)
            ]
            _anonymous_ = ['_u']
            itemex: TVITEMEXA
            item: TVITEMA
            hParent: int
            hInsertAfter: int
        
        LPTVINSERTSTRUCTA = TVINSERTSTRUCTA.PTR()

        class TVINSERTSTRUCTW(CStructure):
            class _U(CUnion):
                _fields_ = [
                    ('itemex', TVITEMEXW),
                    ('item', TVITEMW)
                ]
            _fields_ = [
                ('hParent', HTREEITEM),
                ('hInsertAfter', HTREEITEM),
                ('_u', _U)
            ]
            _anonymous_ = ['_u']
            itemex: TVITEMEXW
            item: TVITEMW
            hParent: int
            hInsertAfter: int
        
        LPTVINSERTSTRUCTW = TVINSERTSTRUCTW.PTR()
        TVINSERTSTRUCT = unicode(TVINSERTSTRUCTW, TVINSERTSTRUCTA)
        LPTVINSERTSTRUCT = unicode(LPTVINSERTSTRUCTW, LPTVINSERTSTRUCTA)

        LPTV_INSERTSTRUCTA = LPTVINSERTSTRUCTA
        LPTV_INSERTSTRUCTW = LPTVINSERTSTRUCTW
        TV_INSERTSTRUCTA = TVINSERTSTRUCTA
        TV_INSERTSTRUCTW = TVINSERTSTRUCTW
        TV_INSERTSTRUCT = TVINSERTSTRUCT
        LPTV_INSERTSTRUCT = LPTVINSERTSTRUCT
        TVINSERTSTRUCTA_V1_SIZE = CCSIZEOF_STRUCT(TVINSERTSTRUCTA, 'item')
        TVINSERTSTRUCTW_V1_SIZE = CCSIZEOF_STRUCT(TVINSERTSTRUCTW, 'item')

        TVM_INSERTITEMA = (TV_FIRST + 0)
        TVM_INSERTITEMW = (TV_FIRST + 50)
        TVM_INSERTITEM = unicode(TVM_INSERTITEMW, TVM_INSERTITEMA)
        TVM_DELETEITEM = (TV_FIRST + 1)
        TVM_EXPAND = (TV_FIRST + 2)
        TVE_COLLAPSE = 0x0001
        TVE_EXPAND = 0x0002
        TVE_TOGGLE = 0x0003
        TVE_EXPANDPARTIAL = 0x4000
        TVE_COLLAPSERESET = 0x8000
        TVM_GETITEMRECT = (TV_FIRST + 4)
        TVM_GETCOUNT = (TV_FIRST + 5)
        TVM_GETINDENT = (TV_FIRST + 6)
        TVM_SETINDENT = (TV_FIRST + 7)
        TVM_GETIMAGELIST = (TV_FIRST + 8)
        TVSIL_NORMAL = 0
        TVSIL_STATE = 2
        TVM_SETIMAGELIST = (TV_FIRST + 9)
        TVM_GETNEXTITEM = (TV_FIRST + 10)
        TVGN_ROOT = 0x0000
        TVGN_NEXT = 0x0001
        TVGN_PREVIOUS = 0x0002
        TVGN_PARENT = 0x0003
        TVGN_CHILD = 0x0004
        TVGN_FIRSTVISIBLE = 0x0005
        TVGN_NEXTVISIBLE = 0x0006
        TVGN_PREVIOUSVISIBLE = 0x0007
        TVGN_DROPHILITE = 0x0008
        TVGN_CARET = 0x0009
        TVGN_LASTVISIBLE = 0x000A
        if WIN32_IE >= WIN32_IE_IE60:
            TVGN_NEXTSELECTED = 0x000B
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            TVSI_NOSINGLEEXPAND = 0x8000 # Should not conflict with TVGN flags.
        TVM_SELECTITEM = (TV_FIRST + 11)
        TVM_GETITEMA = (TV_FIRST + 12)
        TVM_GETITEMW = (TV_FIRST + 62)
        TVM_GETITEM = unicode(TVM_GETITEMW, TVM_GETITEMA)
        TVM_SETITEMA = (TV_FIRST + 13)
        TVM_SETITEMW = (TV_FIRST + 63)
        TVM_SETITEM = unicode(TVM_SETITEMW, TVM_SETITEMA)
        TVM_EDITLABELA = (TV_FIRST + 14)
        TVM_EDITLABELW = (TV_FIRST + 65)
        TVM_EDITLABEL = unicode(TVM_EDITLABELW, TVM_EDITLABELA)
        TVM_GETEDITCONTROL = (TV_FIRST + 15)
        TVM_GETVISIBLECOUNT = (TV_FIRST + 16)
        TVM_HITTEST = (TV_FIRST + 17)

        class TVHITTESTINFO(CStructure):
            _fields_ = [
                ('pt', POINT),
                ('flags', UINT),
                ('hItem', HTREEITEM)
            ]
            pt: POINT
            flags: int
            hItem: int
        
        LPTVHITTESTINFO = TVHITTESTINFO.PTR()
        LPTV_HITTESTINFO = LPTVHITTESTINFO
        TV_HITTESTINFO = TVHITTESTINFO

        TVHT_NOWHERE = 0x0001
        TVHT_ONITEMICON = 0x0002
        TVHT_ONITEMLABEL = 0x0004
        TVHT_ONITEMSTATEICON = 0x0040
        TVHT_ONITEM = (TVHT_ONITEMICON | TVHT_ONITEMLABEL | TVHT_ONITEMSTATEICON)
        TVHT_ONITEMINDENT = 0x0008
        TVHT_ONITEMBUTTON = 0x0010
        TVHT_ONITEMRIGHT = 0x0020
        TVHT_ABOVE = 0x0100
        TVHT_BELOW = 0x0200
        TVHT_TORIGHT = 0x0400
        TVHT_TOLEFT = 0x0800
        TVM_CREATEDRAGIMAGE = (TV_FIRST + 18)
        TVM_SORTCHILDREN = (TV_FIRST + 19)
        TVM_ENSUREVISIBLE = (TV_FIRST + 20)
        TVM_SORTCHILDRENCB = (TV_FIRST + 21)
        TVM_ENDEDITLABELNOW = (TV_FIRST + 22)
        TVM_GETISEARCHSTRINGA = (TV_FIRST + 23)
        TVM_GETISEARCHSTRINGW = (TV_FIRST + 64)
        TVM_GETISEARCHSTRING = unicode(TVM_GETISEARCHSTRINGW, TVM_GETISEARCHSTRINGA)
        TVM_SETTOOLTIPS = (TV_FIRST + 24)
        TVM_GETTOOLTIPS = (TV_FIRST + 25)
        TVM_SETINSERTMARK = (TV_FIRST + 26)
        TVM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        TVM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        TVM_SETITEMHEIGHT = (TV_FIRST + 27)
        TVM_GETITEMHEIGHT = (TV_FIRST + 28)
        TVM_SETBKCOLOR = (TV_FIRST + 29)
        TVM_SETTEXTCOLOR = (TV_FIRST + 30)
        TVM_GETBKCOLOR = (TV_FIRST + 31)
        TVM_GETTEXTCOLOR = (TV_FIRST + 32)
        TVM_SETSCROLLTIME = (TV_FIRST + 33)
        TVM_GETSCROLLTIME = (TV_FIRST + 34)
        TVM_SETINSERTMARKCOLOR = (TV_FIRST + 37)
        TVM_GETINSERTMARKCOLOR = (TV_FIRST + 38)
        TVM_SETBORDER = (TV_FIRST + 35)
        TVSBF_XBORDER = 0x00000001
        TVSBF_YBORDER = 0x00000002
        # tvm_?etitemstate only uses mask, state and stateMask.
        # so unicode or ansi is irrelevant.
        TVM_GETITEMSTATE = (TV_FIRST + 39)
        TVM_SETLINECOLOR = (TV_FIRST + 40)
        TVM_GETLINECOLOR = (TV_FIRST + 41)
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            TVM_MAPACCIDTOHTREEITEM = (TV_FIRST + 42)
            TVM_MAPHTREEITEMTOACCID = (TV_FIRST + 43)
            TVM_SETEXTENDEDSTYLE = (TV_FIRST + 44)
            TVM_GETEXTENDEDSTYLE = (TV_FIRST + 45)
            TVM_SETAUTOSCROLLINFO = (TV_FIRST + 59)
        TVM_SETHOT = (TV_FIRST + 58)
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            TVM_GETSELECTEDCOUNT = (TV_FIRST + 70)
            TVM_SHOWINFOTIP = (TV_FIRST + 71)

            if True:
                TVGIPR_BUTTON  = 0x0001
            TVITEMPART = INT

            class TVGETITEMPARTRECTINFO(CStructure):
                _fields_ = [
                    ('hti', HTREEITEM),
                    ('prc', PRECT),
                    ('partID', TVITEMPART)
                ]
                hti: int
                prc: PRECT
                partID: TVITEMPART

            TVM_GETITEMPARTRECT = (TV_FIRST + 72)
        # typedef int(CALLBACK *)(LPARAM lParam1, LPARAM lParam2, LPARAM lParamSort)
        PFNTVCOMPARE = CALLBACK(INT, LPARAM, LPARAM, LPARAM)

        class TVSORTCB(CStructure):
            _fields_ = [
                ('hParent', HTREEITEM),
                ('lpfnCompare', PFNTVCOMPARE),
                ('lParam', LPARAM)
            ]
            hParent: int
            lpfnCompare: FARPROC
            lParam: int
            
        LPTVSORTCB = TVSORTCB.PTR()
        LPTV_SORTCB = LPTVSORTCB
        TV_SORTCB = TVSORTCB

        class NMTREEVIEWA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('action', UINT),
                ('itemOld', TVITEMA),
                ('itemNew', TVITEMA),
                ('ptDrag', POINT)
            ]
            hdr: NMHDR
            action: int
            itemOld: TVITEMA
            itemNew: TVITEMA
            ptDrag: POINT
        LPNMTREEVIEWA = NMTREEVIEWA.PTR()

        class NMTREEVIEWW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('action', UINT),
                ('itemOld', TVITEMW),
                ('itemNew', TVITEMW),
                ('ptDrag', POINT)
            ]
            hdr: NMHDR
            action: int
            itemOld: TVITEMW
            itemNew: TVITEMW
            ptDrag: POINT
        LPNMTREEVIEWW = NMTREEVIEWW.PTR()

        NMTREEVIEW = unicode(NMTREEVIEWW, NMTREEVIEWA)
        LPNMTREEVIEW = unicode(LPNMTREEVIEWW, LPNMTREEVIEWA)

        LPNM_TREEVIEWA = LPNMTREEVIEWA
        LPNM_TREEVIEWW = LPNMTREEVIEWW
        NM_TREEVIEWW = NMTREEVIEWW
        NM_TREEVIEWA = NMTREEVIEWA
        LPNM_TREEVIEW = LPNMTREEVIEW
        NM_TREEVIEW = NMTREEVIEW
        TVN_SELCHANGINGA = (TVN_FIRST-1)
        TVN_SELCHANGINGW = (TVN_FIRST-50)
        TVN_SELCHANGEDA = (TVN_FIRST-2)
        TVN_SELCHANGEDW = (TVN_FIRST-51)
        TVC_UNKNOWN = 0x0000
        TVC_BYMOUSE = 0x0001
        TVC_BYKEYBOARD = 0x0002
        TVN_GETDISPINFOA = (TVN_FIRST-3)
        TVN_GETDISPINFOW = (TVN_FIRST-52)
        TVN_SETDISPINFOA = (TVN_FIRST-4)
        TVN_SETDISPINFOW = (TVN_FIRST-53)
        TVIF_DI_SETITEM = 0x1000

        class NMTVDISPINFOA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('item', TVITEMA)
            ]
            hdr: NMHDR
            item: TVITEMA
            
        LPNMTVDISPINFOA = NMTVDISPINFOA.PTR()

        class NMTVDISPINFOW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('item', TVITEMW)
            ]
            hdr: NMHDR
            item: TVITEMW
            
        LPNMTVDISPINFOW = NMTVDISPINFOW.PTR()

        NMTVDISPINFO = unicode(NMTVDISPINFOW, NMTVDISPINFOA)
        LPNMTVDISPINFO = unicode(LPNMTVDISPINFOW, LPNMTVDISPINFOA)
        TV_DISPINFOA = NMTVDISPINFOA
        TV_DISPINFOW = NMTVDISPINFOW
        TV_DISPINFO = NMTVDISPINFO
        if WIN32_IE >= WIN32_IE_IE60:
            class NMTVDISPINFOEXA(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('item', TVITEMEXA)
                ]
                hdr: NMHDR
                item: TVITEMEXA
            LPNMTVDISPINFOEXA = NMTVDISPINFOEXA.PTR()
            
            class NMTVDISPINFOEXW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('item', TVITEMEXW)
                ]
                hdr: NMHDR
                item: TVITEMEXW
            LPNMTVDISPINFOEXW = NMTVDISPINFOEXW.PTR()

        NMTVDISPINFOEX = unicode(NMTVDISPINFOEXW, NMTVDISPINFOEXA)
        LPNMTVDISPINFOEX = unicode(LPNMTVDISPINFOEXW, LPNMTVDISPINFOEXA)
        TV_DISPINFOEXA = NMTVDISPINFOEXA
        TV_DISPINFOEXW = NMTVDISPINFOEXW
        TV_DISPINFOEX = NMTVDISPINFOEX
        TVN_ITEMEXPANDINGA = (TVN_FIRST-5)
        TVN_ITEMEXPANDINGW = (TVN_FIRST-54)
        TVN_ITEMEXPANDEDA = (TVN_FIRST-6)
        TVN_ITEMEXPANDEDW = (TVN_FIRST-55)
        TVN_BEGINDRAGA = (TVN_FIRST-7)
        TVN_BEGINDRAGW = (TVN_FIRST-56)
        TVN_BEGINRDRAGA = (TVN_FIRST-8)
        TVN_BEGINRDRAGW = (TVN_FIRST-57)
        TVN_DELETEITEMA = (TVN_FIRST-9)
        TVN_DELETEITEMW = (TVN_FIRST-58)
        TVN_BEGINLABELEDITA = (TVN_FIRST-10)
        TVN_BEGINLABELEDITW = (TVN_FIRST-59)
        TVN_ENDLABELEDITA = (TVN_FIRST-11)
        TVN_ENDLABELEDITW = (TVN_FIRST-60)
        TVN_KEYDOWN = (TVN_FIRST-12)
        TVN_GETINFOTIPA = (TVN_FIRST-13)
        TVN_GETINFOTIPW = (TVN_FIRST-14)
        TVN_SINGLEEXPAND = (TVN_FIRST-15)
        TVNRET_DEFAULT = 0
        TVNRET_SKIPOLD = 1
        TVNRET_SKIPNEW = 2
        if WIN32_IE >= WIN32_IE_IE60:
            TVN_ITEMCHANGINGA = (TVN_FIRST-16)
            TVN_ITEMCHANGINGW = (TVN_FIRST-17)
            TVN_ITEMCHANGEDA = (TVN_FIRST-18)
            TVN_ITEMCHANGEDW = (TVN_FIRST-19)
            TVN_ASYNCDRAW = (TVN_FIRST-20)
        
        class NMTVKEYDOWN(CStructure):
            _pack_ = 1
            _fields_ = [
                ('hdr', NMHDR),
                ('wVKey', WORD),
                ('flags', UINT)
            ]
            hdr: NMHDR
            wVKey: int
            flags: int
        LPNMTVKEYDOWN = NMTVKEYDOWN.PTR()
        TV_KEYDOWN = NMTVKEYDOWN

        # pack-end
        TVN_SELCHANGING = unicode(TVN_SELCHANGINGW, TVN_SELCHANGINGA)
        TVN_SELCHANGED = unicode(TVN_SELCHANGEDW, TVN_SELCHANGEDA)
        TVN_GETDISPINFO = unicode(TVN_GETDISPINFOW, TVN_GETDISPINFOA)
        TVN_SETDISPINFO = unicode(TVN_SETDISPINFOW, TVN_SETDISPINFOA)
        TVN_ITEMEXPANDING = unicode(TVN_ITEMEXPANDINGW, TVN_ITEMEXPANDINGA)
        TVN_ITEMEXPANDED = unicode(TVN_ITEMEXPANDEDW, TVN_ITEMEXPANDEDA)
        TVN_BEGINDRAG = unicode(TVN_BEGINDRAGW, TVN_BEGINDRAGA)
        TVN_BEGINRDRAG = unicode(TVN_BEGINRDRAGW, TVN_BEGINRDRAGA)
        TVN_DELETEITEM = unicode(TVN_DELETEITEMW, TVN_DELETEITEMA)
        TVN_BEGINLABELEDIT = unicode(TVN_BEGINLABELEDITW, TVN_BEGINLABELEDITA)
        TVN_ENDLABELEDIT = unicode(TVN_ENDLABELEDITW, TVN_ENDLABELEDITA)

        class NMTVCUSTOMDRAW(CStructure):
            _fields_ = [
                ('nmcd', NMCUSTOMDRAW),
                ('clrText', COLORREF),
                ('clrTextBk', COLORREF),
                ('iLevel', INT)
            ]
            nmcd: NMCUSTOMDRAW
            clrText: int
            clrTextBk: int
            iLevel: int
        
        NMTVCUSTOMDRAW_V3_SIZE = CCSIZEOF_STRUCT(NMTVCUSTOMDRAW, 'clrTextBk')
        LPNMTVCUSTOMDRAW = NMTVCUSTOMDRAW.PTR()

        # for tooltips

        class NMTVGETINFOTIPA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('hItem', HTREEITEM),
                ('lParam', LPARAM)
            ]
            hdr: NMHDR
            pszText: LPSTR
            cchTextMax: int
            hItem: int
            lParam: int
            
        LPNMTVGETINFOTIPA = NMTVGETINFOTIPA.PTR()

        class NMTVGETINFOTIPW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('hItem', HTREEITEM),
                ('lParam', LPARAM)
            ]
            hdr: NMHDR
            pszText: LPWSTR
            cchTextMax: int
            hItem: int
            lParam: int
            
        LPNMTVGETINFOTIPW = NMTVGETINFOTIPW.PTR()

        TVN_GETINFOTIP = unicode(TVN_GETINFOTIPW, TVN_GETINFOTIPA)
        NMTVGETINFOTIP = unicode(NMTVGETINFOTIPW, NMTVGETINFOTIPA)
        LPNMTVGETINFOTIP = unicode(LPNMTVGETINFOTIPW, LPNMTVGETINFOTIPA)
        # treeview's customdraw return meaning don't draw images.  valid on CDRF_NOTIFYITEMPREPAINT
        TVCDRF_NOIMAGES = 0x00010000
        if WIN32_IE > WIN32_IE_IE60:
            class NMTVITEMCHANGE(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('uChanged', UINT),
                    ('hItem', HTREEITEM),
                    ('uStateNew', UINT),
                    ('uStateOld', UINT),
                    ('lParam', LPARAM)
                ]
                hdr: NMHDR
                uChanged: int
                hItem: int
                uStateNew: int
                uStateOld: int
                lParam: int
                
            class NMTVASYNCDRAW(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('pimldp', IMAGELISTDRAWPARAMS.PTR()),
                    ('hr', HRESULT),
                    ('hItem', HTREEITEM),
                    ('lParam', LPARAM),
                    ('dwRetFlags', DWORD),
                    ('iRetImageIndex', INT)
                ]
                hdr: NMHDR
                pimldp: IPointer[IMAGELISTDRAWPARAMS]
                hr: int
                hItem: int
                lParam: int
                dwRetFlags: int
                iRetImageIndex: int

        TVN_ITEMCHANGING = unicode(TVN_ITEMCHANGINGW, TVN_ITEMCHANGINGA)
        TVN_ITEMCHANGED = unicode(TVN_ITEMCHANGEDW, TVN_ITEMCHANGEDA)
        # _WIN32_IE >= 0x0600
    # NOTREEVIEW
    ##########  ComboBoxEx ################
    if cpreproc.ifndef('NOUSEREXCONTROLS'):
        WC_COMBOBOXEXW = u"ComboBoxEx32"
        WC_COMBOBOXEXA = b"ComboBoxEx32"
        WC_COMBOBOXEX = WC_COMBOBOXEXW
        CBEIF_TEXT = 0x00000001
        CBEIF_IMAGE = 0x00000002
        CBEIF_SELECTEDIMAGE = 0x00000004
        CBEIF_OVERLAY = 0x00000008
        CBEIF_INDENT = 0x00000010
        CBEIF_LPARAM = 0x00000020
        CBEIF_DI_SETITEM = 0x10000000

        class COMBOBOXEXITEMA(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('iItem', INT_PTR),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('iOverlay', INT),
                ('iIndent', INT),
                ('lParam', LPARAM)
            ]
            mask: int
            iItem: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            iOverlay: int
            iIndent: int
            lParam: int
        
        PCCOMBOBOXEXITEMA = PCOMBOBOXEXITEMA = COMBOBOXEXITEMA.PTR()

        class COMBOBOXEXITEMW(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('iItem', INT_PTR),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('iImage', INT),
                ('iSelectedImage', INT),
                ('iOverlay', INT),
                ('iIndent', INT),
                ('lParam', LPARAM)
            ]
            mask: int
            iItem: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            iSelectedImage: int
            iOverlay: int
            iIndent: int
            lParam: int
            
        PCCOMBOBOXEXITEMW = PCOMBOBOXEXITEMW = COMBOBOXEXITEMW.PTR()

        COMBOBOXEXITEM = unicode(COMBOBOXEXITEMW, COMBOBOXEXITEMA)
        PCOMBOBOXEXITEM = unicode(PCOMBOBOXEXITEMW, PCOMBOBOXEXITEMA)
        PCCOMBOBOXEXITEM = unicode(PCCOMBOBOXEXITEMW, PCCOMBOBOXEXITEMA)
        CBEM_INSERTITEMA = (WM_USER + 1)
        CBEM_SETIMAGELIST = (WM_USER + 2)
        CBEM_GETIMAGELIST = (WM_USER + 3)
        CBEM_GETITEMA = (WM_USER + 4)
        CBEM_SETITEMA = (WM_USER + 5)
        CBEM_DELETEITEM = CB_DELETESTRING
        CBEM_GETCOMBOCONTROL = (WM_USER + 6)
        CBEM_GETEDITCONTROL = (WM_USER + 7)
        CBEM_SETEXSTYLE = (WM_USER + 8) # use  SETEXTENDEDSTYLE instead
        CBEM_SETEXTENDEDSTYLE = (WM_USER + 14) # lparam == new style, wParam(optional) == mask
        CBEM_GETEXSTYLE = (WM_USER + 9) # use GETEXTENDEDSTYLE instead
        CBEM_GETEXTENDEDSTYLE = (WM_USER + 9)
        CBEM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        CBEM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        CBEM_HASEDITCHANGED = (WM_USER + 10)
        CBEM_INSERTITEMW = (WM_USER + 11)
        CBEM_SETITEMW = (WM_USER + 12)
        CBEM_GETITEMW = (WM_USER + 13)
        CBEM_INSERTITEM = unicode(CBEM_INSERTITEMW, CBEM_INSERTITEMA)
        CBEM_SETITEM = unicode(CBEM_SETITEMW, CBEM_SETITEMA)
        CBEM_GETITEM = unicode(CBEM_GETITEMW, CBEM_GETITEMA)
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            CBEM_SETWINDOWTHEME = CCM_SETWINDOWTHEME
        CBES_EX_NOEDITIMAGE = 0x00000001
        CBES_EX_NOEDITIMAGEINDENT = 0x00000002
        CBES_EX_PATHWORDBREAKPROC = 0x00000004
        CBES_EX_NOSIZELIMIT = 0x00000008
        CBES_EX_CASESENSITIVE = 0x00000010
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            CBES_EX_TEXTENDELLIPSIS = 0x00000020

        class NMCOMBOBOXEXA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('ceItem', COMBOBOXEXITEMA)
            ]
            hdr: NMHDR
            ceItem: COMBOBOXEXITEMA
            
        PNMCOMBOBOXEXA = NMCOMBOBOXEXA.PTR()

        class NMCOMBOBOXEXW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('ceItem', COMBOBOXEXITEMW)
            ]
            hdr: NMHDR
            ceItem: COMBOBOXEXITEMW
            
        PNMCOMBOBOXEXW = NMCOMBOBOXEXW.PTR()

        NMCOMBOBOXEX = unicode(NMCOMBOBOXEXW, NMCOMBOBOXEXA)
        PNMCOMBOBOXEX = unicode(PNMCOMBOBOXEXW, PNMCOMBOBOXEXA)
        CBEN_GETDISPINFOA = (CBEN_FIRST - 0)
        CBEN_INSERTITEM = (CBEN_FIRST - 1)
        CBEN_DELETEITEM = (CBEN_FIRST - 2)
        CBEN_BEGINEDIT = (CBEN_FIRST - 4)
        CBEN_ENDEDITA = (CBEN_FIRST - 5)
        CBEN_ENDEDITW = (CBEN_FIRST - 6)
        CBEN_GETDISPINFOW = (CBEN_FIRST - 7)
        CBEN_GETDISPINFO = unicode(CBEN_GETDISPINFOW, CBEN_GETDISPINFOA)
        CBEN_DRAGBEGINA = (CBEN_FIRST - 8)
        CBEN_DRAGBEGINW = (CBEN_FIRST - 9)
        CBEN_DRAGBEGIN = unicode(CBEN_DRAGBEGINW, CBEN_DRAGBEGINA)
        # lParam specifies why the endedit is happening
        CBEN_ENDEDIT = unicode(CBEN_ENDEDITW, CBEN_ENDEDITA)
        CBENF_KILLFOCUS = 1
        CBENF_RETURN = 2
        CBENF_ESCAPE = 3
        CBENF_DROPDOWN = 4
        CBEMAXSTRLEN = 260
        # CBEN_DRAGBEGIN sends this information ...

        class NMCBEDRAGBEGINW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('iItemid', INT),
                ('szText', WCHAR * CBEMAXSTRLEN)
            ]
            hdr: NMHDR
            iItemid: int
            szText: IWideCharArray
            
        LPNMCBEDRAGBEGINW = PNMCBEDRAGBEGINW = NMCBEDRAGBEGINW.PTR()

        class NMCBEDRAGBEGINA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('iItemid', INT),
                ('szText', CHAR * CBEMAXSTRLEN)
            ]
            hdr: NMHDR
            iItemid: int
            szText: ICharArray
            
        LPNMCBEDRAGBEGINA = PNMCBEDRAGBEGINA = NMCBEDRAGBEGINA.PTR()

        NMCBEDRAGBEGIN = unicode(NMCBEDRAGBEGINW, NMCBEDRAGBEGINA)
        LPNMCBEDRAGBEGIN = unicode(LPNMCBEDRAGBEGINW, LPNMCBEDRAGBEGINA)
        PNMCBEDRAGBEGIN = unicode(PNMCBEDRAGBEGINW, PNMCBEDRAGBEGINA)
        # CBEN_ENDEDIT sends this information...
        # fChanged if the user actually did anything
        # iNewSelection gives what would be the new selection unless the notify is failed
        #                      iNewSelection may be CB_ERR if there's no match

        class NMCBEENDEDITW(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('fChanged', BOOL),
                ('iNewSelection', INT),
                ('szText', WCHAR * CBEMAXSTRLEN),
                ('iWhy', INT)
            ]
            hdr: NMHDR
            fChanged: int
            iNewSelection: int
            szText: IWideCharArray
            iWhy: int
        
        LPNMCBEENDEDITW = PNMCBEENDEDITW = NMCBEENDEDITW.PTR()

        class NMCBEENDEDITA(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('fChanged', BOOL),
                ('iNewSelection', INT),
                ('szText', CHAR * CBEMAXSTRLEN),
                ('iWhy', INT)
            ]
            hdr: NMHDR
            fChanged: int
            iNewSelection: int
            szText: ICharArray
            iWhy: int
        
        LPNMCBEENDEDITA = PNMCBEENDEDITA = NMCBEENDEDITA.PTR()

        NMCBEENDEDIT = unicode(NMCBEENDEDITW, NMCBEENDEDITA)
        LPNMCBEENDEDIT = unicode(LPNMCBEENDEDITW, LPNMCBEENDEDITA)
        PNMCBEENDEDIT = unicode(PNMCBEENDEDITW, PNMCBEENDEDITA)
    # NOUSEREXCONTROLS
    #====== TAB CONTROL ==========================================================
    if cpreproc.ifndef("NOTABCONTROL"):
        WC_TABCONTROLA = b"SysTabControl32"
        WC_TABCONTROLW = u"SysTabControl32"
        WC_TABCONTROL = "SysTabControl"
        # begin_r_commctrl
        TCS_SCROLLOPPOSITE = 0x0001 # assumes multiline tab
        TCS_BOTTOM = 0x0002
        TCS_RIGHT = 0x0002
        TCS_MULTISELECT = 0x0004 # allow multi-select in button mode
        TCS_FLATBUTTONS = 0x0008
        TCS_FORCEICONLEFT = 0x0010
        TCS_FORCELABELLEFT = 0x0020
        TCS_HOTTRACK = 0x0040
        TCS_VERTICAL = 0x0080
        TCS_TABS = 0x0000
        TCS_BUTTONS = 0x0100
        TCS_SINGLELINE = 0x0000
        TCS_MULTILINE = 0x0200
        TCS_RIGHTJUSTIFY = 0x0000
        TCS_FIXEDWIDTH = 0x0400
        TCS_RAGGEDRIGHT = 0x0800
        TCS_FOCUSONBUTTONDOWN = 0x1000
        TCS_OWNERDRAWFIXED = 0x2000
        TCS_TOOLTIPS = 0x4000
        TCS_FOCUSNEVER = 0x8000
        # end_r_commctrl
        # EX styles for use with TCM_SETEXTENDEDSTYLE
        TCS_EX_FLATSEPARATORS = 0x00000001
        TCS_EX_REGISTERDROP = 0x00000002
        TCM_GETIMAGELIST = (TCM_FIRST + 2)
        TCM_SETIMAGELIST = (TCM_FIRST + 3)
        TCM_GETITEMCOUNT = (TCM_FIRST + 4)
        TCIF_TEXT = 0x0001
        TCIF_IMAGE = 0x0002
        TCIF_RTLREADING = 0x0004
        TCIF_PARAM = 0x0008
        TCIF_STATE = 0x0010
        TCIS_BUTTONPRESSED = 0x0001
        TCIS_HIGHLIGHTED = 0x0002

        class TCITEMHEADERA(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('lpReserved1', UINT),
                ('lpReserved2', UINT),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('iImage', INT)
            ]
            
            mask: int
            lpReserved1: int
            lpReserved2: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int
            
        LPTCITEMHEADERA = TCITEMHEADERA.PTR()

        class TCITEMHEADERW(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('lpReserved1', UINT),
                ('lpReserved2', UINT),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('iImage', INT)
            ]
            
            mask: int
            lpReserved1: int
            lpReserved2: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            
        LPTCITEMHEADERW = TCITEMHEADERW.PTR()

        TCITEMHEADER = unicode(TCITEMHEADERW, TCITEMHEADERA)
        LPTCITEMHEADER = unicode(LPTCITEMHEADERW, LPTCITEMHEADERA)
        TC_ITEMHEADERA = TCITEMHEADERA
        TC_ITEMHEADERW = TCITEMHEADERW
        TC_ITEMHEADER = TCITEMHEADER

        class TCITEMA(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('dwState', DWORD),
                ('dwStateMask', DWORD),
                ('pszText', LPSTR),
                ('cchTextMax', INT),
                ('iImage', INT)
            ]
            
            mask: int
            dwState: int
            dwStateMask: int
            pszText: LPSTR
            cchTextMax: int
            iImage: int

        LPTCITEMA = TCITEMA.PTR()

        class TCITEMW(CStructure):
            _fields_ = [
                ('mask', UINT),
                ('dwState', DWORD),
                ('dwStateMask', DWORD),
                ('pszText', LPWSTR),
                ('cchTextMax', INT),
                ('iImage', INT)
            ]
            
            mask: int
            dwState: int
            dwStateMask: int
            pszText: LPWSTR
            cchTextMax: int
            iImage: int
            
        LPTCITEMW = TCITEMW.PTR()

        TCITEM = unicode(TCITEMW, TCITEMA)
        LPTCITEM = unicode(LPTCITEMW, LPTCITEMA)
        TCM_GETITEMA = (TCM_FIRST + 5)
        TCM_GETITEMW = (TCM_FIRST + 60)
        TCM_GETITEM = unicode(TCM_GETITEMW, TCM_GETITEMA)

        TC_ITEMA = TCITEMA
        TC_ITEMW = TCITEMW
        TC_ITEM = TCITEM
        TCM_SETITEMA = (TCM_FIRST + 6)
        TCM_SETITEMW = (TCM_FIRST + 61)
        TCM_SETITEM = unicode(TCM_SETITEMW, TCM_SETITEMA)
        TCM_INSERTITEMA = (TCM_FIRST + 7)
        TCM_INSERTITEMW = (TCM_FIRST + 62)
        TCM_INSERTITEM = unicode(TCM_INSERTITEMW, TCM_INSERTITEMA)
        TCM_DELETEITEM = (TCM_FIRST + 8)
        TCM_DELETEALLITEMS = (TCM_FIRST + 9)
        TCM_GETITEMRECT = (TCM_FIRST + 10)
        TCM_GETCURSEL = (TCM_FIRST + 11)
        TCM_SETCURSEL = (TCM_FIRST + 12)
        TCHT_NOWHERE = 0x0001
        TCHT_ONITEMICON = 0x0002
        TCHT_ONITEMLABEL = 0x0004
        TCHT_ONITEM = (TCHT_ONITEMICON | TCHT_ONITEMLABEL)

        class TCHITTESTINFO(CStructure):
            _fields_ = [
                ('pt', POINT),
                ('flags', UINT)
            ]
            
            pt: POINT
            flags: int
        
        LPTC_HITTESTINFO = LPTCHITTESTINFO = TCHITTESTINFO.PTR()
        TC_HITTESTINFO = TCHITTESTINFO

        TCM_HITTEST = (TCM_FIRST + 13)
        TCM_SETITEMEXTRA = (TCM_FIRST + 14)
        TCM_ADJUSTRECT = (TCM_FIRST + 40)
        TCM_SETITEMSIZE = (TCM_FIRST + 41)
        TCM_REMOVEIMAGE = (TCM_FIRST + 42)
        TCM_SETPADDING = (TCM_FIRST + 43)
        TCM_GETROWCOUNT = (TCM_FIRST + 44)
        TCM_GETTOOLTIPS = (TCM_FIRST + 45)
        TCM_SETTOOLTIPS = (TCM_FIRST + 46)
        TCM_GETCURFOCUS = (TCM_FIRST + 47)
        TCM_SETCURFOCUS = (TCM_FIRST + 48)
        TCM_SETMINTABWIDTH = (TCM_FIRST + 49)
        TCM_DESELECTALL = (TCM_FIRST + 50)
        TCM_HIGHLIGHTITEM = (TCM_FIRST + 51)
        TCM_SETEXTENDEDSTYLE = (TCM_FIRST + 52) # optional wParam == mask
        TCM_GETEXTENDEDSTYLE = (TCM_FIRST + 53)
        TCM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        TCM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        TCN_KEYDOWN = (TCN_FIRST - 0)

        class NMTCKEYDOWN(CStructure):
            _pack_ = 1
            _fields_ = [
                ('hdr', NMHDR),
                ('wVKey', WORD),
                ('flags', UINT)
            ]
            
            hdr: NMHDR
            wVKey: int
            flags: int
        TC_KEYDOWN = NMTCKEYDOWN

        TCN_SELCHANGE = (TCN_FIRST - 1)
        TCN_SELCHANGING = (TCN_FIRST - 2)
        TCN_GETOBJECT = (TCN_FIRST - 3)
        TCN_FOCUSCHANGE = (TCN_FIRST - 4)
    # NOTABCONTROL
    if cpreproc.ifndef("NOANIMATE"):
        ANIMATE_CLASSW = u"SysAnimate32"
        ANIMATE_CLASSA = b"SysAnimate32"
        ANIMATE_CLASS = "SysAnimate32"
        # begin_r_commctrl
        ACS_CENTER = 0x0001
        ACS_TRANSPARENT = 0x0002
        ACS_AUTOPLAY = 0x0004
        ACS_TIMER = 0x0008 # don't use threads... use timers
        # end_r_commctrl
        ACM_OPENA = (WM_USER+100)
        ACM_OPENW = (WM_USER+103)
        ACM_OPEN = unicode(ACM_OPENW, ACM_OPENA)
        ACM_PLAY = (WM_USER+101)
        ACM_STOP = (WM_USER+102)
        ACM_ISPLAYING = (WM_USER+104)
        ACN_START = 1
        ACN_STOP = 2
    # NOANIMATE
    #====== MONTHCAL CONTROL ======================================================
    if cpreproc.ifndef("NOMONTHCAL"):
        MONTHCAL_CLASSW = u"SysMonthCal32"
        MONTHCAL_CLASSA = b"SysMonthCal32"
        MONTHCAL_CLASS = MONTHCAL_CLASSW
        # bit-packed array of "bold" info for a month
        # if a bit is on, that day is drawn bold
        MONTHDAYSTATE = DWORD
        LPMONTHDAYSTATE = PDWORD
        MCM_FIRST = 0x1000
        # BOOL MonthCal_GetCurSel(HWND hmc, LPSYSTEMTIME pst)
        #   returns FALSE if MCS_MULTISELECT
        #   returns TRUE and sets *pst to the currently selected date otherwise
        MCM_GETCURSEL = (MCM_FIRST + 1)
        # BOOL MonthCal_SetCurSel(HWND hmc, LPSYSTEMTIME pst)
        #   returns FALSE if MCS_MULTISELECT
        #   returns TURE and sets the currently selected date to *pst otherwise
        MCM_SETCURSEL = (MCM_FIRST + 2)
        # DWORD MonthCal_GetMaxSelCount(HWND hmc)
        #   returns the maximum number of selectable days allowed
        MCM_GETMAXSELCOUNT = (MCM_FIRST + 3)
        # BOOL MonthCal_SetMaxSelCount(HWND hmc, UINT n)
        #   sets the max number days that can be selected iff MCS_MULTISELECT
        MCM_SETMAXSELCOUNT = (MCM_FIRST + 4)
        # BOOL MonthCal_GetSelRange(HWND hmc, LPSYSTEMTIME rgst)
        #   sets rgst[0] to the first day of the selection range
        #   sets rgst[1] to the last day of the selection range
        MCM_GETSELRANGE = (MCM_FIRST + 5)
        # BOOL MonthCal_SetSelRange(HWND hmc, LPSYSTEMTIME rgst)
        #   selects the range of days from rgst[0] to rgst[1]
        MCM_SETSELRANGE = (MCM_FIRST + 6)
        # DWORD MonthCal_GetMonthRange(HWND hmc, DWORD gmr, LPSYSTEMTIME rgst)
        #   if rgst specified, sets rgst[0] to the starting date and
        #      and rgst[1] to the ending date of the the selectable(non-grayed)
        #      days if GMR_VISIBLE or all the displayed days(including grayed)
        #      if GMR_DAYSTATE.
        #   returns the number of months spanned by the above range.
        MCM_GETMONTHRANGE = (MCM_FIRST + 7)
        # BOOL MonthCal_SetDayState(HWND hmc, int cbds, DAYSTATE *rgds)
        #   cbds is the count of DAYSTATE items in rgds and it must be equal
        #   to the value returned from MonthCal_GetMonthRange(hmc, GMR_DAYSTATE, NULL)
        #   This sets the DAYSTATE bits for each month(grayed and non-grayed
        #   days) displayed in the calendar. The first bit in a month's DAYSTATE
        #   corresponts to bolding day 1, the second bit affects day 2, etc.
        MCM_SETDAYSTATE = (MCM_FIRST + 8)
        # BOOL MonthCal_GetMinReqRect(HWND hmc, LPRECT prc)
        #   sets *prc the minimal size needed to display one month
        #   To display two months, undo the AdjustWindowRect calculation already done to
        #   this rect, double the width, and redo the AdjustWindowRect calculation --
        #   the monthcal control will display two calendars in this window(if you also
        #   double the vertical size, you will get 4 calendars)
        #   NOTE: if you want to gurantee that the "Today" string is not clipped,
        #   get the MCM_GETMAXTODAYWIDTH and use the max of that width and this width
        MCM_GETMINREQRECT = (MCM_FIRST + 9)
        # set colors to draw control with -- see MCSC_ bits below
        MCM_SETCOLOR = (MCM_FIRST + 10)
        MCM_GETCOLOR = (MCM_FIRST + 11)
        MCSC_BACKGROUND = 0 # the background color(between months)
        MCSC_TEXT = 1 # the dates
        MCSC_TITLEBK = 2 # background of the title
        MCSC_TITLETEXT = 3
        MCSC_MONTHBK = 4 # background within the month cal
        MCSC_TRAILINGTEXT = 5 # the text color of header & trailing days
        # set what day is "today"   send NULL to revert back to real date
        MCM_SETTODAY = (MCM_FIRST + 12)
        # get what day is "today"
        # returns BOOL for success/failure
        MCM_GETTODAY = (MCM_FIRST + 13)
        # determine what pinfo->pt is over
        MCM_HITTEST = (MCM_FIRST + 14)

        class MCHITTESTINFO(CStructure):
            fields = [
                ('cbSize', UINT),
                ('pt', POINT),
                ('uHit', UINT),
                ('st', SYSTEMTIME)
            ]
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                fields.extend([
                    ('rc', RECT),
                    ('iOffset', INT),
                    ('iRow', INT),
                    ('iCol', INT)
                ])
            cbSize: int
            pt: POINT
            uHit: int
            st: SYSTEMTIME
            rc: RECT
            iOffset: int
            iRow: int
            iCol: int
        
        declare_fields(MCHITTESTINFO)
        
        PMCHITTESTINFO = MCHITTESTINFO.PTR()
        MCHITTESTINFO_V1_SIZE = CCSIZEOF_STRUCT(MCHITTESTINFO, 'st')
        
        MCHT_TITLE = 0x00010000
        MCHT_CALENDAR = 0x00020000
        MCHT_TODAYLINK = 0x00030000
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            MCHT_CALENDARCONTROL = 0x00100000
        MCHT_NEXT = 0x01000000 # these indicate that hitting
        MCHT_PREV = 0x02000000 # here will go to the next/prev month
        MCHT_NOWHERE = 0x00000000
        MCHT_TITLEBK = (MCHT_TITLE)
        MCHT_TITLEMONTH = (MCHT_TITLE | 0x0001)
        MCHT_TITLEYEAR = (MCHT_TITLE | 0x0002)
        MCHT_TITLEBTNNEXT = (MCHT_TITLE | MCHT_NEXT | 0x0003)
        MCHT_TITLEBTNPREV = (MCHT_TITLE | MCHT_PREV | 0x0003)
        MCHT_CALENDARBK = (MCHT_CALENDAR)
        MCHT_CALENDARDATE = (MCHT_CALENDAR | 0x0001)
        MCHT_CALENDARDATENEXT = (MCHT_CALENDARDATE | MCHT_NEXT)
        MCHT_CALENDARDATEPREV = (MCHT_CALENDARDATE | MCHT_PREV)
        MCHT_CALENDARDAY = (MCHT_CALENDAR | 0x0002)
        MCHT_CALENDARWEEKNUM = (MCHT_CALENDAR | 0x0003)
        MCHT_CALENDARDATEMIN = (MCHT_CALENDAR | 0x0004)
        MCHT_CALENDARDATEMAX = (MCHT_CALENDAR | 0x0005)
        # set first day of week to iDay:
        # 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
        # -1 for means use locale info
        MCM_SETFIRSTDAYOFWEEK = (MCM_FIRST + 15)
        # DWORD result...  low word has the day.  high word is bool if this is app set
        # or not(FALSE == using locale info)
        MCM_GETFIRSTDAYOFWEEK = (MCM_FIRST + 16)
        # DWORD MonthCal_GetRange(HWND hmc, LPSYSTEMTIME rgst)
        #   modifies rgst[0] to be the minimum ALLOWABLE systemtime(or 0 if no minimum)
        #   modifies rgst[1] to be the maximum ALLOWABLE systemtime(or 0 if no maximum)
        #   returns GDTR_MIN|GDTR_MAX if there is a minimum|maximum limit
        MCM_GETRANGE = (MCM_FIRST + 17)
        # BOOL MonthCal_SetRange(HWND hmc, DWORD gdtr, LPSYSTEMTIME rgst)
        #   if GDTR_MIN, sets the minimum ALLOWABLE systemtime to rgst[0], otherwise removes minimum
        #   if GDTR_MAX, sets the maximum ALLOWABLE systemtime to rgst[1], otherwise removes maximum
        #   returns TRUE on success, FALSE on error(such as invalid parameters)
        MCM_SETRANGE = (MCM_FIRST + 18)
        # int MonthCal_GetMonthDelta(HWND hmc)
        #   returns the number of months one click on a next/prev button moves by
        MCM_GETMONTHDELTA = (MCM_FIRST + 19)
        # int MonthCal_SetMonthDelta(HWND hmc, int n)
        #   sets the month delta to n. n==0 reverts to moving by a page of months
        #   returns the previous value of n.
        MCM_SETMONTHDELTA = (MCM_FIRST + 20)
        # DWORD MonthCal_GetMaxTodayWidth(HWND hmc, LPSIZE psz)
        #   sets *psz to the maximum width/height of the "Today" string displayed
        #   at the bottom of the calendar(as long as MCS_NOTODAY is not specified)
        MCM_GETMAXTODAYWIDTH = (MCM_FIRST + 21)
        MCM_SETUNICODEFORMAT = CCM_SETUNICODEFORMAT
        MCM_GETUNICODEFORMAT = CCM_GETUNICODEFORMAT
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            # View
            MCMV_MONTH = 0
            MCMV_YEAR = 1
            MCMV_DECADE = 2
            MCMV_CENTURY = 3
            MCMV_MAX = MCMV_CENTURY
            MCM_GETCURRENTVIEW = (MCM_FIRST + 22)
            MCM_GETCALENDARCOUNT = (MCM_FIRST + 23)
            # Part
            MCGIP_CALENDARCONTROL = 0
            MCGIP_NEXT = 1
            MCGIP_PREV = 2
            MCGIP_FOOTER = 3
            MCGIP_CALENDAR = 4
            MCGIP_CALENDARHEADER = 5
            MCGIP_CALENDARBODY = 6
            MCGIP_CALENDARROW = 7
            MCGIP_CALENDARCELL = 8
            MCGIF_DATE = 0x00000001
            MCGIF_RECT = 0x00000002
            MCGIF_NAME = 0x00000004
            # Note: iRow of -1 refers to the row header and iCol of -1 refers to the col header.

            class MCGRIDINFO(CStructure):
                _fields_ = [
                    ('cbSize', UINT),
                    ('dwPart', DWORD),
                    ('dwFlags', DWORD),
                    ('iCalendar', INT),
                    ('iRow', INT),
                    ('iCol', INT),
                    ('bSelected', BOOL),
                    ('stStart', SYSTEMTIME),
                    ('stEnd', SYSTEMTIME),
                    ('rc', RECT),
                    ('pszName', LPWSTR),
                    ('cchName', SIZE_T)
                ]
                cbSize: int
                dwPart: int
                dwFlags: int
                iCalendar: int
                iRow: int
                iCol: int
                bSelected: int
                stStart: SYSTEMTIME
                stEnd: SYSTEMTIME
                rc: RECT
                pszName: LPWSTR
                cchName: int
            PMCGRIDINFO = PTR(MCGRIDINFO)

            MCM_GETCALENDARGRIDINFO = (MCM_FIRST + 24)
            MCM_GETCALID = (MCM_FIRST + 27)
            MCM_SETCALID = (MCM_FIRST + 28)
            # Returns the min rect that will fit the max number of calendars for the passed in rect.
            MCM_SIZERECTTOMIN = (MCM_FIRST + 29)
            MCM_SETCALENDARBORDER = (MCM_FIRST + 30)
            MCM_GETCALENDARBORDER = (MCM_FIRST + 31)
            MCM_SETCURRENTVIEW = (MCM_FIRST + 32)
        # MCN_SELCHANGE is sent whenever the currently displayed date changes
        # via month change, year change, keyboard navigation, prev/next button
        #

        class NMSELCHANGE(CStructure):
            _fields_ = [
                ('nmhdr', NMHDR),
                ('stSelStart', SYSTEMTIME),
                ('stSelEnd', SYSTEMTIME)
            ]
            nmhdr: NMHDR
            stSelStart: SYSTEMTIME
            stSelEnd: SYSTEMTIME
        LPNMSELCHANGE = NMSELCHANGE.PTR()

        MCN_SELCHANGE = (MCN_FIRST - 3) # -749
        # MCN_GETDAYSTATE is sent for MCS_DAYSTATE controls whenever new daystate
        # information is needed(month or year scroll) to draw bolding information.
        # The app must fill in cDayState months worth of information starting from
        # stStart date. The app may fill in the array at prgDayState or change
        # prgDayState to point to a different array out of which the information
        # will be copied.(similar to tooltips)
        #

        class NMDAYSTATE(CStructure):
            _fields_ = [
                ('nmhdr', NMHDR),
                ('stStart', SYSTEMTIME),
                ('cDayState', INT),
                ('prgDayState', LPMONTHDAYSTATE)
            ]
            nmhdr: NMHDR
            stStart: SYSTEMTIME
            cDayState: int
            prgDayState: LPMONTHDAYSTATE
        LPNMDAYSTATE = NMDAYSTATE.PTR()

        MCN_GETDAYSTATE = (MCN_FIRST - 1) # -747
        # MCN_SELECT is sent whenever a selection has occured(via mouse or keyboard)
        #
        # typedef NMSELCHANGE NMSELECT, *LPNMSELECT;
        MCN_SELECT = (MCN_FIRST) # -746

        class NMVIEWCHANGE(CStructure):
            _fields_ = [
                ('nmhdr', NMHDR),
                ('dwOldView', DWORD),
                ('dwNewView', DWORD)
            ]
            nmhdr: NMHDR
            dwOldView: int
            dwNewView: int
        LPNMVIEWCHANGE = NMVIEWCHANGE.PTR()

        MCN_VIEWCHANGE = (MCN_FIRST - 4) # -750
        # begin_r_commctrl
        MCS_DAYSTATE = 0x0001
        MCS_MULTISELECT = 0x0002
        MCS_WEEKNUMBERS = 0x0004
        MCS_NOTODAYCIRCLE = 0x0008
        MCS_NOTODAY = 0x0010
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            MCS_NOTRAILINGDATES = 0x0040
            MCS_SHORTDAYSOFWEEK = 0x0080
            MCS_NOSELCHANGEONNAV = 0x0100
        # end_r_commctrl
        GMR_VISIBLE = 0 # visible portion of display
        GMR_DAYSTATE = 1 # above plus the grayed out parts of
        # partially displayed months
    # NOMONTHCAL
    #====== DATETIMEPICK CONTROL ==================================================
    if cpreproc.ifndef("NODATETIMEPICK"):
        DATETIMEPICK_CLASSW = u"SysDateTimePick32"
        DATETIMEPICK_CLASSA = b"SysDateTimePick32"
        DATETIMEPICK_CLASS = DATETIMEPICK_CLASSW
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            """

            typedef struct tagDATETIMEPICKERINFO
            {
            DWORD cbSize;

            RECT rcCheck;
            DWORD stateCheck;

            RECT rcButton;
            DWORD stateButton;

            HWND hwndEdit;
            HWND hwndUD;
            HWND hwndDropDown;
            } DATETIMEPICKERINFO, *LPDATETIMEPICKERINFO;

            """

        #(_WINVER >= WIN32_WINNT_VISTA)
        DTM_FIRST = 0x1000
        # DWORD DateTimePick_GetSystemtime(HWND hdp, LPSYSTEMTIME pst)
        #   returns GDT_NONE if "none" is selected(DTS_SHOWNONE only)
        #   returns GDT_VALID and modifies *pst to be the currently selected value
        DTM_GETSYSTEMTIME = (DTM_FIRST + 1)
        # BOOL DateTime_SetSystemtime(HWND hdp, DWORD gd, LPSYSTEMTIME pst)
        #   if gd==GDT_NONE, sets datetimepick to None(DTS_SHOWNONE only)
        #   if gd==GDT_VALID, sets datetimepick to *pst
        #   returns TRUE on success, FALSE on error(such as bad params)
        DTM_SETSYSTEMTIME = (DTM_FIRST + 2)
        # DWORD DateTime_GetRange(HWND hdp, LPSYSTEMTIME rgst)
        #   modifies rgst[0] to be the minimum ALLOWABLE systemtime(or 0 if no minimum)
        #   modifies rgst[1] to be the maximum ALLOWABLE systemtime(or 0 if no maximum)
        #   returns GDTR_MIN|GDTR_MAX if there is a minimum|maximum limit
        DTM_GETRANGE = (DTM_FIRST + 3)
        # BOOL DateTime_SetRange(HWND hdp, DWORD gdtr, LPSYSTEMTIME rgst)
        #   if GDTR_MIN, sets the minimum ALLOWABLE systemtime to rgst[0], otherwise removes minimum
        #   if GDTR_MAX, sets the maximum ALLOWABLE systemtime to rgst[1], otherwise removes maximum
        #   returns TRUE on success, FALSE on error(such as invalid parameters)
        DTM_SETRANGE = (DTM_FIRST + 4)
        # BOOL DateTime_SetFormat(HWND hdp, LPCTSTR sz)
        #   sets the display formatting string to sz(see GetDateFormat and GetTimeFormat for valid formatting chars)
        #   NOTE: 'X' is a valid formatting character which indicates that the application
        #   will determine how to display information. Such apps must support DTN_WMKEYDOWN,
        #   DTN_FORMAT, and DTN_FORMATQUERY.
        DTM_SETFORMATA = (DTM_FIRST + 5)
        DTM_SETFORMATW = (DTM_FIRST + 50)
        DTM_SETFORMAT = unicode(DTM_SETFORMATW, DTM_SETFORMATA)
        DTM_SETMCCOLOR = (DTM_FIRST + 6)
        DTM_GETMCCOLOR = (DTM_FIRST + 7)
    # HWND DateTime_GetMonthCal(HWND hdp)
    #   returns the HWND of the MonthCal popup window. Only valid
    # between DTN_DROPDOWN and DTN_CLOSEUP notifications.
    DTM_GETMONTHCAL = (DTM_FIRST + 8)
    DTM_SETMCFONT = (DTM_FIRST + 9)
    DTM_GETMCFONT = (DTM_FIRST + 10)
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        DTM_SETMCSTYLE = (DTM_FIRST + 11)
        DTM_GETMCSTYLE = (DTM_FIRST + 12)
        DTM_CLOSEMONTHCAL = (DTM_FIRST + 13)
        # DateTime_GetDateTimePickerInfo(HWND hdp, DATETIMEPICKERINFO* pdtpi)
        # Retrieves information about the selected date time picker.
        DTM_GETDATETIMEPICKERINFO = (DTM_FIRST + 14)
        DTM_GETIDEALSIZE = (DTM_FIRST + 15)
    #(_WINVER >= WIN32_WINNT_VISTA)
    # begin_r_commctrl
    DTS_UPDOWN = 0x0001 # use UPDOWN instead of MONTHCAL
    DTS_SHOWNONE = 0x0002 # allow a NONE selection
    DTS_SHORTDATEFORMAT = 0x0000 # use the short date format(app must forward WM_WININICHANGE messages)
    DTS_LONGDATEFORMAT = 0x0004 # use the long date format(app must forward WM_WININICHANGE messages)
    DTS_SHORTDATECENTURYFORMAT = 0x000C # short date format with century(app must forward WM_WININICHANGE messages)
    DTS_TIMEFORMAT = 0x0009 # use the time format(app must forward WM_WININICHANGE messages)
    DTS_APPCANPARSE = 0x0010 # allow user entered strings(app MUST respond to DTN_USERSTRING)
    DTS_RIGHTALIGN = 0x0020 # right-align popup instead of left-align it
    # end_r_commctrl
    DTN_DATETIMECHANGE = (DTN_FIRST2 - 6) # the systemtime has changed, -759

    class NMDATETIMECHANGE(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('dwFlags', DWORD),
            ('st', SYSTEMTIME)
        ]
        nmhdr: NMHDR
        dwFlags: int
        st: SYSTEMTIME
    LPNMDATETIMECHANGE = PTR(NMDATETIMECHANGE)

    DTN_USERSTRINGA = (DTN_FIRST2 - 5) # the user has entered a string, -758
    DTN_USERSTRINGW = (DTN_FIRST - 5) # -745

    class NMDATETIMESTRINGA(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszUserString', LPCSTR),
            ('st', SYSTEMTIME),
            ('dwFlags', DWORD)
        ]
        nmhdr: NMHDR
        pszUserString: LPCSTR
        st: SYSTEMTIME
        dwFlags: int
    LPNMDATETIMESTRINGA = PTR(NMDATETIMESTRINGA)

    class NMDATETIMESTRINGW(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszUserString', LPCWSTR),
            ('st', SYSTEMTIME),
            ('dwFlags', DWORD)
        ]
        nmhdr: NMHDR
        pszUserString: LPCWSTR
        st: SYSTEMTIME
        dwFlags: int
    LPNMDATETIMESTRINGW = PTR(NMDATETIMESTRINGW)

    DTN_USERSTRING = unicode(DTN_USERSTRINGW, DTN_USERSTRINGA)
    NMDATETIMESTRING = unicode(NMDATETIMESTRINGW, NMDATETIMESTRINGA)
    LPNMDATETIMESTRING = unicode(LPNMDATETIMESTRINGW, LPNMDATETIMESTRINGA)
    DTN_WMKEYDOWNA = (DTN_FIRST2 - 4) # modify keydown on app format field(X), , -757
    DTN_WMKEYDOWNW = (DTN_FIRST - 4) # -744

    class NMDATETIMEWMKEYDOWNA(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('nVirtKey', INT),
            ('pszFormat', LPCSTR),
            ('st', SYSTEMTIME)
        ]
        nmhdr: NMHDR
        nVirtKey: int
        pszFormat: LPCSTR
        st: SYSTEMTIME
    LPNMDATETIMEWMKEYDOWNA = PTR(NMDATETIMEWMKEYDOWNA)

    class NMDATETIMEWMKEYDOWNW(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('nVirtKey', INT),
            ('pszFormat', LPCWSTR),
            ('st', SYSTEMTIME)
        ]
        nmhdr: NMHDR
        nVirtKey: int
        pszFormat: LPCSTR
        st: SYSTEMTIME
    LPNMDATETIMEWMKEYDOWNW = PTR(NMDATETIMEWMKEYDOWNW)

    DTN_WMKEYDOWN = unicode(DTN_WMKEYDOWNW, DTN_WMKEYDOWNA)
    NMDATETIMEWMKEYDOWN = unicode(NMDATETIMEWMKEYDOWNW, NMDATETIMEWMKEYDOWNA)
    LPNMDATETIMEWMKEYDOWN = unicode(LPNMDATETIMEWMKEYDOWNW, LPNMDATETIMEWMKEYDOWNA)
    DTN_FORMATA = (DTN_FIRST2 - 3) # query display for app format field(X), -756
    DTN_FORMATW = (DTN_FIRST - 3) # -743

    class NMDATETIMEFORMATA(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszFormat', LPCSTR),
            ('st', SYSTEMTIME),
            ('pszDisplay', LPCSTR),
            ('szDisplay', CHAR * 64)
        ]
        nmhdr: NMHDR
        pszFormat: LPCSTR
        st: SYSTEMTIME
        pszDisplay: LPCSTR
        szDisplay: ICharArray
    LPNMDATETIMEFORMATA = PTR(NMDATETIMEFORMATA)

    class NMDATETIMEFORMATW(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszFormat', LPCWSTR),
            ('st', SYSTEMTIME),
            ('pszDisplay', LPCWSTR),
            ('szDisplay', WCHAR * 64)
        ]
        nmhdr: NMHDR
        pszFormat: LPCSTR
        st: SYSTEMTIME
        pszDisplay: LPCSTR
        szDisplay: IWideCharArray
    LPNMDATETIMEFORMATW = PTR(NMDATETIMEFORMATW)

    DTN_FORMAT = unicode(DTN_FORMATW, DTN_FORMATA)
    NMDATETIMEFORMAT = unicode(NMDATETIMEFORMATW, NMDATETIMEFORMATA)
    LPNMDATETIMEFORMAT = unicode(LPNMDATETIMEFORMATW, LPNMDATETIMEFORMATA)
    DTN_FORMATQUERYA = (DTN_FIRST2 - 2) # query formatting info for app format field(X), -755
    DTN_FORMATQUERYW = (DTN_FIRST - 2) # -742

    class NMDATETIMEFORMATQUERYA(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszFormat', LPCSTR),
            ('szMax', SIZE)
        ]
        nmhdr: NMHDR
        pszFormat: LPCSTR
        szMax: SIZE
    LPNMDATETIMEFORMATQUERYA = PTR(NMDATETIMEFORMATQUERYA)

    class NMDATETIMEFORMATQUERYW(CStructure):
        _fields_ = [
            ('nmhdr', NMHDR),
            ('pszFormat', LPCWSTR),
            ('szMax', SIZE)
        ]
        nmhdr: NMHDR
        pszFormat: LPCWSTR
        szMax: SIZE
    LPNMDATETIMEFORMATQUERYW = PTR(NMDATETIMEFORMATQUERYW)

    DTN_FORMATQUERY = unicode(DTN_FORMATQUERYW, DTN_FORMATQUERYA)
    NMDATETIMEFORMATQUERY = unicode(NMDATETIMEFORMATQUERYW, NMDATETIMEFORMATQUERYA)
    LPNMDATETIMEFORMATQUERY = unicode(LPNMDATETIMEFORMATQUERYW, LPNMDATETIMEFORMATQUERYA)
    DTN_DROPDOWN = (DTN_FIRST2 - 1) # MonthCal has dropped down, -754
    DTN_CLOSEUP = (DTN_FIRST2) # MonthCal is popping up, -753
    GDTR_MIN = 0x0001
    GDTR_MAX = 0x0002
    GDT_ERROR = -1
    GDT_VALID = 0
    GDT_NONE = 1
    # _WIN32
    # NODATETIMEPICK
    if cpreproc.ifndef("NOIPADDRESS"):
        #######################/
        #    IP Address edit control
        # Messages sent to IPAddress controls
        IPM_CLEARADDRESS = (WM_USER+100)
        IPM_SETADDRESS = (WM_USER+101) # lparam = TCP/IP address
        IPM_GETADDRESS = (WM_USER+102) # lresult = # of non black fields.  lparam = LPDWORD for TCP/IP address
        IPM_SETRANGE = (WM_USER+103)
        IPM_SETFOCUS = (WM_USER+104)
        IPM_ISBLANK = (WM_USER+105) # no parameters
        WC_IPADDRESSW = u"SysIPAddress32"
        WC_IPADDRESSA = b"SysIPAddress32"
        WC_IPADDRESS = WC_IPADDRESSW
        IPN_FIELDCHANGED = (IPN_FIRST - 0)

        class NMIPADDRESS(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('iField', INT),
                ('iValue', INT)
            ]
            hdr: NMHDR
            iField: int
            iValue: int
        LPNMIPADDRESS = PTR(NMIPADDRESS)

        # The following is a useful macro for passing the range values in the
        # IPM_SETRANGE message.
        MAKEIPRANGE = lambda low, high: (LPARAM(WORD((BYTE(high).value<<8) + BYTE(low).value)).value).value
        # And this is a useful macro for making the IP Address to be passed
        # as a LPARAM.
        MAKEIPADDRESS = lambda b1,b2,b3,b4: (LPARAM(((DWORD(b1).value<<24)+(DWORD(b2).value<<16)+(DWORD(b3).value<<8)+(DWORD(b4).value)))).value
        # Get individual number
        FIRST_IPADDRESS = lambda x: (((x) >> 24) & 0xff)
        SECOND_IPADDRESS = lambda x: (((x) >> 16) & 0xff)
        THIRD_IPADDRESS = lambda x: (((x) >> 8) & 0xff)
        FOURTH_IPADDRESS = lambda x: ((x) & 0xff)
    # NOIPADDRESS
    #---------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------
    #  ====================== Pager Control =============================
    #---------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------
    if cpreproc.ifndef("NOPAGESCROLLER"):
        # Pager Class Name
        WC_PAGESCROLLERW = u"SysPager"
        WC_PAGESCROLLERA = b"SysPager"
        WC_PAGESCROLLER = WC_PAGESCROLLERW
        #---------------------------------------------------------------------------------------
        # Pager Control Styles
        #---------------------------------------------------------------------------------------
        # begin_r_commctrl
        PGS_VERT = 0x00000000
        PGS_HORZ = 0x00000001
        PGS_AUTOSCROLL = 0x00000002
        PGS_DRAGNDROP = 0x00000004
        # end_r_commctrl
        #---------------------------------------------------------------------------------------
        # Pager Button State
        #---------------------------------------------------------------------------------------
        #The scroll can be in one of the following control State
        PGF_INVISIBLE = 0 # Scroll button is not visible
        PGF_NORMAL = 1 # Scroll button is in normal state
        PGF_GRAYED = 2 # Scroll button is in grayed state
        PGF_DEPRESSED = 4 # Scroll button is in depressed state
        PGF_HOT = 8 # Scroll button is in hot state
        # The following identifiers specifies the button control
        PGB_TOPORLEFT = 0
        PGB_BOTTOMORRIGHT = 1
        #---------------------------------------------------------------------------------------
        # Pager Control  Messages
        #---------------------------------------------------------------------------------------
        PGM_SETCHILD = (PGM_FIRST + 1) # lParam == hwnd
        PGM_RECALCSIZE = (PGM_FIRST + 2)
        PGM_FORWARDMOUSE = (PGM_FIRST + 3)
        PGM_SETBKCOLOR = (PGM_FIRST + 4)
        PGM_GETBKCOLOR = (PGM_FIRST + 5)
        PGM_SETBORDER = (PGM_FIRST + 6)
        PGM_GETBORDER = (PGM_FIRST + 7)
        PGM_SETPOS = (PGM_FIRST + 8)
        PGM_GETPOS = (PGM_FIRST + 9)
        PGM_SETBUTTONSIZE = (PGM_FIRST + 10)
        PGM_GETBUTTONSIZE = (PGM_FIRST + 11)
        PGM_GETBUTTONSTATE = (PGM_FIRST + 12)
        PGM_GETDROPTARGET = CCM_GETDROPTARGET
        PGM_SETSCROLLINFO = (PGM_FIRST + 13)
        #---------------------------------------------------------------------------------------
        #Pager Control Notification Messages
        #---------------------------------------------------------------------------------------
        # PGN_SCROLL Notification Message
        PGN_SCROLL = (PGN_FIRST-1)
        PGF_SCROLLUP = 1
        PGF_SCROLLDOWN = 2
        PGF_SCROLLLEFT = 4
        PGF_SCROLLRIGHT = 8
        #Keys down
        PGK_SHIFT = 1
        PGK_CONTROL = 2
        PGK_MENU = 4
        # This structure is sent along with PGN_SCROLL notifications

        class NMPGSCROLL(CStructure):
            _pack_ = 1
            _fields_ = [
                ('hdr', NMHDR),
                ('fwKeys', WORD),
                ('rcParent', RECT),
                ('iDir', INT),
                ('iXpos', INT),
                ('iYpos', INT),
                ('iScroll', INT)
            ]
            hdr: NMHDR
            fwKeys: int
            rcParent: RECT
            iDir: int
            iXpos: int
            iYpos: int
            iScroll: int
        LPNMPGSCROLL = PTR(NMPGSCROLL)

        # PGN_CALCSIZE Notification Message
        PGN_CALCSIZE = (PGN_FIRST-2)
        PGF_CALCWIDTH = 1
        PGF_CALCHEIGHT = 2

        class NMPGCALCSIZE(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('dwFlag', DWORD),
                ('iWidth', INT),
                ('iHeight', INT)
            ]
            hdr: NMHDR
            dwFlag: int
            iWidth: int
            iHeight: int
        LPNMPGCALCSIZE = PTR(NMPGCALCSIZE)

        # PGN_HOTITEMCHANGE Notification Message
        PGN_HOTITEMCHANGE = (PGN_FIRST-3)

        # The PGN_HOTITEMCHANGE notification uses these notification
        # flags defined in TOOLBAR:

        HICF_ENTERING = 0x00000010 # idOld is invalid
        HICF_LEAVING = 0x00000020 # idNew is invalid

        # Structure for PGN_HOTITEMCHANGE notification
        #

        class NMPGHOTITEM(CStructure):
            _fields_ = [
                ('hdr', NMHDR),
                ('idOld', INT),
                ('idNew', INT),
                ('dwFlags', DWORD)
            ]
            hdr: NMHDR
            idOld: int
            idNew: int
            dwFlags: int
        LPNMPGHOTITEM = PTR(NMPGHOTITEM)

    # NOPAGESCROLLER
    ##======================  End Pager Control ==========================================
    #
    # === Native Font Control ===
    #
    if cpreproc.ifndef("NONATIVEFONTCTL"):
        # NativeFont Class Name
        WC_NATIVEFONTCTLW = u"NativeFontCtl"
        WC_NATIVEFONTCTLA = b"NativeFontCtl"
        WC_NATIVEFONTCTL = unicode(WC_NATIVEFONTCTLW, WC_NATIVEFONTCTLA)
        # begin_r_commctrl
        # style definition
        NFS_EDIT = 0x0001
        NFS_STATIC = 0x0002
        NFS_LISTCOMBO = 0x0004
        NFS_BUTTON = 0x0008
        NFS_ALL = 0x0010
        NFS_USEFONTASSOC = 0x0020
        # end_r_commctrl
    # NONATIVEFONTCTL
    # === End Native Font Control ===
    # ====================== Button Control =============================
    if cpreproc.ifndef("NOBUTTON"):
        # Button Class Name
        WC_BUTTONA = b"Button"
        WC_BUTTONW = u"Button"
        WC_BUTTON = WC_BUTTONW
        if cpreproc.get_version() >= WIN32_WINNT_WINXP:
            BUTTON_IMAGELIST_ALIGN_LEFT = 0
            BUTTON_IMAGELIST_ALIGN_RIGHT = 1
            BUTTON_IMAGELIST_ALIGN_TOP = 2
            BUTTON_IMAGELIST_ALIGN_BOTTOM = 3
            BUTTON_IMAGELIST_ALIGN_CENTER = 4 # Doesn't draw text

            class BUTTON_IMAGELIST(CStructure):
                _fields_ = [
                    ('himl', HIMAGELIST),
                    ('margin', RECT),
                    ('uAlign', UINT)
                ]
                himl: int
                margin: RECT
                uAlign: int
            PBUTTON_IMAGELIST = PTR(BUTTON_IMAGELIST)

            BCM_GETIDEALSIZE = (BCM_FIRST + 0x0001)
            BCM_SETIMAGELIST = (BCM_FIRST + 0x0002)
            BCM_GETIMAGELIST = (BCM_FIRST + 0x0003)
            BCM_SETTEXTMARGIN = (BCM_FIRST + 0x0004)
            BCM_GETTEXTMARGIN = (BCM_FIRST + 0x0005)

            class NMBCHOTITEM(CStructure):
                _fields_ = [
                    ('hdr', NMHDR),
                    ('dwFlags', DWORD)
                ]
                hdr: NMHDR
                dwFlags: int
            LPNMBCHOTITEM = PTR(NMBCHOTITEM)

            BCN_HOTITEMCHANGE = (BCN_FIRST + 0x0001)
            BST_HOT = 0x0200
        # (_WINVER >= WIN32_WINNT_WINXP)
        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            # BUTTON STATE FLAGS
            BST_DROPDOWNPUSHED = 0x0400
            # begin_r_commctrl
            # BUTTON STYLES
            BS_SPLITBUTTON = 0x0000000C
            BS_DEFSPLITBUTTON = 0x0000000D
            BS_COMMANDLINK = 0x0000000E
            BS_DEFCOMMANDLINK = 0x0000000F
            # SPLIT BUTTON INFO mask flags
            BCSIF_GLYPH = 0x0001
            BCSIF_IMAGE = 0x0002
            BCSIF_STYLE = 0x0004
            BCSIF_SIZE = 0x0008
            # SPLIT BUTTON STYLE flags
            BCSS_NOSPLIT = 0x0001
            BCSS_STRETCH = 0x0002
            BCSS_ALIGNLEFT = 0x0004
            BCSS_IMAGE = 0x0008
            # end_r_commctrl
            # BUTTON STRUCTURES

            class BUTTON_SPLITINFO(CStructure):
                _fields_ = [
                    ('mask', UINT),
                    ('himlGlyph', HIMAGELIST),
                    ('uSplitStyle', UINT),
                    ('size', SIZE)
                ]
                mask: int
                himlGlyph: int
                uSplitStyle: int
                size: SIZE
            PBUTTON_SPLITINFO = BUTTON_SPLITINFO.PTR()

            # BUTTON MESSAGES
            BCM_SETDROPDOWNSTATE = (BCM_FIRST + 0x0006)
            BCM_SETSPLITINFO = (BCM_FIRST + 0x0007)
            BCM_GETSPLITINFO = (BCM_FIRST + 0x0008)
            BCM_SETNOTE = (BCM_FIRST + 0x0009)
            BCM_GETNOTE = (BCM_FIRST + 0x000A)
            BCM_GETNOTELENGTH = (BCM_FIRST + 0x000B)
            # Macro to use on a button or command link to display an elevated icon
            BCM_SETSHIELD = (BCM_FIRST + 0x000C)
            # Value to pass to BCM_SETIMAGELIST to indicate that no glyph should be
            # displayed
            BCCL_NOGLYPH = HIMAGELIST(-1).value
            # NOTIFICATION MESSAGES

            class NMBCDROPDOWN(CStructure):
                _fields_ =  [
                    ('hdr', NMHDR),
                    ('rcButton', RECT)
                ]
                hdr: NMHDR
                rcButton: RECT
            LPNMBCDROPDOWN = PTR(NMBCDROPDOWN)

            BCN_DROPDOWN = (BCN_FIRST + 0x0002)
        # (_WINVER >= WIN32_WINNT_VISTA)
        # NOBUTTON
        # =====================  End Button Control =========================
        # ====================== Static Control =============================
        if cpreproc.ifndef("NOSTATIC"):
            # Static Class Name
            WC_STATICA = b"Static"
            WC_STATICW = u"Static"
            WC_STATIC = WC_STATICW
        # NOSTATIC
        # =====================  End Static Control =========================
        # ====================== Edit Control =============================
        if cpreproc.ifndef("NOEDIT"):
            # Edit Class Name
            WC_EDITA = b"Edit"
            WC_EDITW = u"Edit"
            WC_EDIT = WC_EDITW
            if cpreproc.get_version() >= WIN32_WINNT_WIN10:
                # Edit Control Extended Styles to use with EM_SETEXTENDEDSTYLE/EM_GETEXTENDEDSTYLE
                ES_EX_ALLOWEOL_CR = 0x0001
                ES_EX_ALLOWEOL_LF = 0x0002
                ES_EX_ALLOWEOL_ALL = (ES_EX_ALLOWEOL_CR | ES_EX_ALLOWEOL_LF)
                ES_EX_CONVERT_EOL_ON_PASTE = 0x0004
                ES_EX_ZOOMABLE = 0x0010
            if cpreproc.get_version() >= WIN32_WINNT_WINXP:
                EM_SETCUEBANNER = (ECM_FIRST + 1) # Set the cue banner with the lParm = LPCWSTR
                EM_GETCUEBANNER = (ECM_FIRST + 2) # Set the cue banner with the lParm = LPCWSTR

                class EDITBALLOONTIP(CStructure):
                    _fields_ = [
                        ('cbStruct', DWORD),
                        ('pszTitle', LPCWSTR),
                        ('pszText', LPCWSTR),
                        ('ttiIcon', INT)
                    ]
                    cbStruct: int
                    pszTitle: LPCWSTR
                    pszText: LPCWSTR
                    ttiIcon: int
                PEDITBALLOONTIP = PTR(EDITBALLOONTIP)

                EM_SHOWBALLOONTIP = (ECM_FIRST + 3) # Show a balloon tip associated to the edit control
                EM_HIDEBALLOONTIP = (ECM_FIRST + 4) # Hide any balloon tip associated with the edit control
            if cpreproc.get_version() >= WIN32_WINNT_VISTA:
                EM_SETHILITE = (ECM_FIRST + 5)
                EM_GETHILITE = (ECM_FIRST + 6)
            EM_NOSETFOCUS = (ECM_FIRST + 7)
            EM_TAKEFOCUS = (ECM_FIRST + 8)
            if cpreproc.get_version() >= WIN32_WINNT_WIN10:
                # EM_SETENDOFLINE/EM_GETENDOFLINE options

                if True:
                    EC_ENDOFLINE_DETECTFROMCONTENT = 0
                    EC_ENDOFLINE_CRLF              = 1
                    EC_ENDOFLINE_CR                = 2
                    EC_ENDOFLINE_LF                = 3
                EC_ENDOFLINE = INT

                EM_SETEXTENDEDSTYLE = (ECM_FIRST + 10)
                EM_GETEXTENDEDSTYLE = (ECM_FIRST + 11)
                EM_SETENDOFLINE = (ECM_FIRST + 12)
                EM_GETENDOFLINE = (ECM_FIRST + 13)
                EM_ENABLESEARCHWEB = (ECM_FIRST + 14)
                EM_SEARCHWEB = (ECM_FIRST + 15)
                # Form codes are internal-only so keep the api internal
                EM_SETCARETINDEX = (ECM_FIRST + 17)
                EM_GETCARETINDEX = (ECM_FIRST + 18)
                # We want to reuse the same messages as richedit.h
                # which is why these are outside of the ECM_FIRST-ECM_LAST range.
                EM_GETZOOM = (WM_USER + 224)
                EM_SETZOOM = (WM_USER + 225)
                EM_FILELINEFROMCHAR = (ECM_FIRST + 19)
                EM_FILELINEINDEX = (ECM_FIRST + 20)
                EM_FILELINELENGTH = (ECM_FIRST + 21)
                EM_GETFILELINE = (ECM_FIRST + 22)
                EM_GETFILELINECOUNT = (ECM_FIRST + 23)
                EN_SEARCHWEB = (EN_FIRST - 0)

                if True:
                    EC_SEARCHWEB_ENTRYPOINT_EXTERNAL    = 0
                    EC_SEARCHWEB_ENTRYPOINT_CONTEXTMENU = 1
                EC_SEARCHWEB_ENTRYPOINT = INT

                class NMSEARCHWEB(CStructure):
                    _fields_ = [
                        ('hdr', NMHDR),
                        ('entrypoint', EC_SEARCHWEB_ENTRYPOINT),
                        ('hasQueryText', BOOL),
                        ('invokeSucceeded', BOOL)
                    ]
                    hdr: NMHDR
                    entrypoint: int
                    hasQueryText: int
                    invokeSucceeded: int
        # NOEDIT
        # =====================  End Edit Control =========================
    # ====================== Listbox Control =============================
    if cpreproc.ifndef('NOLISTBOX'):
        # Listbox Class Name
        WC_LISTBOXA             = b"ListBox"
        WC_LISTBOXW             = u"ListBox"
        WC_LISTBOX              = WC_LISTBOXW
    # NOLISTBOX
    # =====================  End Listbox Control =========================
    # ====================== Combobox Control =============================
    if cpreproc.ifndef('NOCOMBOBOX'):
        # Combobox Class Name
        WC_COMBOBOXA            = b"ComboBox"
        WC_COMBOBOXW            = u"ComboBox"
        WC_COMBOBOX             = WC_COMBOBOXW
    # NOCOMBOBOX
    if cpreproc.get_version() >= WIN32_WINNT_WINXP:
        # custom combobox control messages
        CB_SETMINVISIBLE        = (CBM_FIRST + 1)
        CB_GETMINVISIBLE        = (CBM_FIRST + 2)
        CB_SETCUEBANNER         = (CBM_FIRST + 3)
        CB_GETCUEBANNER         = (CBM_FIRST + 4)
    # =====================  End Combobox Control =========================
    # ====================== Scrollbar Control ============================
    if cpreproc.ifndef('NOSCROLLBAR'):
        # Scrollbar Class Name
        WC_SCROLLBARA            = b"ScrollBar"
        WC_SCROLLBARW            = u"ScrollBar"
        WC_SCROLLBAR             = WC_SCROLLBARW
    # NOSCROLLBAR
    # ===================== End Scrollbar Control =========================
    # ===================== Task Dialog =========================
    if cpreproc.ifndef('NOTASKDIALOG'):
        # Task Dialog is only available starting Windows Vista
        if (cpreproc.get_version() >= WIN32_WINNT_VISTA):
            #ifdef _WIN32
            #include <pshpack1.h>
            #endif

            # typedef HRESULT (CALLBACK *PFTASKDIALOGCALLBACK)(_In_ HWND hwnd, _In_ UINT msg, _In_ WPARAM wParam, _In_ LPARAM lParam, _In_ LONG_PTR lpRefData);
            PFTASKDIALOGCALLBACK = CALLBACK(HRESULT, HWND, UINT, WPARAM, LPARAM, LONG_PTR)

            if True:
                TDF_ENABLE_HYPERLINKS               = 0x0001
                TDF_USE_HICON_MAIN                  = 0x0002
                TDF_USE_HICON_FOOTER                = 0x0004
                TDF_ALLOW_DIALOG_CANCELLATION       = 0x0008
                TDF_USE_COMMAND_LINKS               = 0x0010
                TDF_USE_COMMAND_LINKS_NO_ICON       = 0x0020
                TDF_EXPAND_FOOTER_AREA              = 0x0040
                TDF_EXPANDED_BY_DEFAULT             = 0x0080
                TDF_VERIFICATION_FLAG_CHECKED       = 0x0100
                TDF_SHOW_PROGRESS_BAR               = 0x0200
                TDF_SHOW_MARQUEE_PROGRESS_BAR       = 0x0400
                TDF_CALLBACK_TIMER                  = 0x0800
                TDF_POSITION_RELATIVE_TO_WINDOW     = 0x1000
                TDF_RTL_LAYOUT                      = 0x2000
                TDF_NO_DEFAULT_RADIO_BUTTON         = 0x4000
                TDF_CAN_BE_MINIMIZED                = 0x8000
                if cpreproc.get_version() >= WIN32_WINNT_WIN8:
                    TDF_NO_SET_FOREGROUND               = 0x00010000 # Don't call SetForegroundWindow() when activating the dialog
                # (_WINVER >= WIN32_WINNT_WIN8)
                TDF_SIZE_TO_CONTENT                 = 0x01000000  # used by ShellMessageBox to emulate MessageBox sizing behavior
            TASKDIALOG_FLAGS = INT # Note: _TASKDIALOG_FLAGS is an int

            if True:
                TDM_NAVIGATE_PAGE                   = WM_USER+101
                TDM_CLICK_BUTTON                    = WM_USER+102 # wParam = Button ID
                TDM_SET_MARQUEE_PROGRESS_BAR        = WM_USER+103 # wParam = 0 (nonMarque) wParam != 0 (Marquee)
                TDM_SET_PROGRESS_BAR_STATE          = WM_USER+104 # wParam = new progress state
                TDM_SET_PROGRESS_BAR_RANGE          = WM_USER+105 # lParam = MAKELPARAM(nMinRange, nMaxRange)
                TDM_SET_PROGRESS_BAR_POS            = WM_USER+106 # wParam = new position
                TDM_SET_PROGRESS_BAR_MARQUEE        = WM_USER+107 # wParam = 0 (stop marquee), wParam != 0 (start marquee), lparam = speed (milliseconds between repaints)
                TDM_SET_ELEMENT_TEXT                = WM_USER+108 # wParam = element (TASKDIALOG_ELEMENTS), lParam = new element text (LPCWSTR)
                TDM_CLICK_RADIO_BUTTON              = WM_USER+110 # wParam = Radio Button ID
                TDM_ENABLE_BUTTON                   = WM_USER+111 # lParam = 0 (disable), lParam != 0 (enable), wParam = Button ID
                TDM_ENABLE_RADIO_BUTTON             = WM_USER+112 # lParam = 0 (disable), lParam != 0 (enable), wParam = Radio Button ID
                TDM_CLICK_VERIFICATION              = WM_USER+113 # wParam = 0 (unchecked), 1 (checked), lParam = 1 (set key focus)
                TDM_UPDATE_ELEMENT_TEXT             = WM_USER+114 # wParam = element (TASKDIALOG_ELEMENTS), lParam = new element text (LPCWSTR)
                TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE = WM_USER+115 # wParam = Button ID, lParam = 0 (elevation not required), lParam != 0 (elevation required)
                TDM_UPDATE_ICON                     = WM_USER+116  # wParam = icon element (TASKDIALOG_ICON_ELEMENTS), lParam = new icon (hIcon if TDF_USE_HICON_* was set, PCWSTR otherwise)
            TASKDIALOG_MESSAGES = INT

            if True:
                TDN_CREATED                         = 0
                TDN_NAVIGATED                       = 1
                TDN_BUTTON_CLICKED                  = 2            # wParam = Button ID
                TDN_HYPERLINK_CLICKED               = 3            # lParam = (LPCWSTR)pszHREF
                TDN_TIMER                           = 4            # wParam = Milliseconds since dialog created or timer reset
                TDN_DESTROYED                       = 5
                TDN_RADIO_BUTTON_CLICKED            = 6            # wParam = Radio Button ID
                TDN_DIALOG_CONSTRUCTED              = 7
                TDN_VERIFICATION_CLICKED            = 8             # wParam = 1 if checkbox checked, 0 if not, lParam is unused and always 0
                TDN_HELP                            = 9
                TDN_EXPANDO_BUTTON_CLICKED          = 10            # wParam = 0 (dialog is now collapsed), wParam != 0 (dialog is now expanded)
            TASKDIALOG_NOTIFICATIONS = INT

            class TASKDIALOG_BUTTON(CStructure):
                _fields_ = [
                    ('nButtonID', INT),
                    ('pszButtonText', LPCWSTR)
                ]
                nButtonID: int
                pszButtonText: LPCWSTR

            if True:
                TDE_CONTENT = 0
                TDE_EXPANDED_INFORMATION = 1
                TDE_FOOTER = 2
                TDE_MAIN_INSTRUCTION = 3
            TASKDIALOG_ELEMENTS = INT

            if True:
                TDIE_ICON_MAIN = 0
                TDIE_ICON_FOOTER = 1
            TASKDIALOG_ICON_ELEMENTS = INT

            TD_WARNING_ICON         = MAKEINTRESOURCEW(-1)
            TD_ERROR_ICON           = MAKEINTRESOURCEW(-2)
            TD_INFORMATION_ICON     = MAKEINTRESOURCEW(-3)
            TD_SHIELD_ICON          = MAKEINTRESOURCEW(-4)

        # (_WINVER >= WIN32_WINNT_VISTA)

        if cpreproc.get_version() >= WIN32_WINNT_VISTA:
            if True:
                TDCBF_OK_BUTTON            = 0x0001 # selected control return value IDOK
                TDCBF_YES_BUTTON           = 0x0002 # selected control return value IDYES
                TDCBF_NO_BUTTON            = 0x0004 # selected control return value IDNO
                TDCBF_CANCEL_BUTTON        = 0x0008 # selected control return value IDCANCEL
                TDCBF_RETRY_BUTTON         = 0x0010 # selected control return value IDRETRY
                TDCBF_CLOSE_BUTTON         = 0x0020  # selected control return value IDCLOSE
                
            TASKDIALOG_COMMON_BUTTON_FLAGS = INT # Note: _TASKDIALOG_COMMON_BUTTON_FLAGS is an int

            class TASKDIALOGCONFIG(CStructure):
                class _U1(CUnion):
                    _fields_ = [
                        ('hMainIcon', HICON),
                        ('pszMainIcon', LPCWSTR)
                    ]
                class _U2(CUnion):
                    _fields_ = [
                        ('hFooterIcon', HICON),
                        ('pszFooterIcon', LPCWSTR)
                    ]
                _fields_ = [
                    ('cbSize', UINT),
                    ('hwndParent', HWND),                                   # incorrectly named, this is the owner window, not a parent.
                    ('hInstance', HINSTANCE),                               # used for MAKEINTRESOURCE() strings
                    ('dwFlags', TASKDIALOG_FLAGS),                          # TASKDIALOG_FLAGS (TDF_XXX) flags
                    ('dwCommonButtons', TASKDIALOG_COMMON_BUTTON_FLAGS),    # TASKDIALOG_COMMON_BUTTON (TDCBF_XXX) flags
                    ('pszWindowTitle', LPCWSTR),                             # string or MAKEINTRESOURCE()
                    ('_u1', _U1),
                    ('pszMainInstruction', LPCWSTR),
                    ('pszContent', LPCWSTR),
                    ('cButtons', UINT),
                    ('pButtons', PTR(TASKDIALOG_BUTTON)),
                    ('nDefaultButton', INT),
                    ('cRadioButtons', UINT),
                    ('pRadioButtons', PTR(TASKDIALOG_BUTTON)),
                    ('nDefaultRadioButton', INT),
                    ('pszVerificationText', LPCWSTR),
                    ('pszExpandedInformation', LPCWSTR),
                    ('pszExpandedControlText', LPCWSTR),
                    ('pszCollapsedControlText', LPCWSTR),
                    ('_u2', _U2),
                    ('pszFooter', LPCWSTR),
                    ('pfCallback', PFTASKDIALOGCALLBACK),
                    ('lpCallbackData', LONG_PTR),
                    ('cxWidth', UINT)                                       # width of the Task Dialog's client area in DLU's. If 0, Task Dialog will calculate the ideal width.
                ]
                _anonymous_ = ['_u1', '_u2']
                cbSize: int
                hwndParent: int
                hInstance: int
                dwFlags: int
                dwCommonButtons: int
                pszWindowTitle: LPCWSTR
                hMainIcon: int
                pszMainIcon: LPCWSTR
                pszMainInstruction: LPCWSTR
                pszContent: LPCWSTR
                cButtons: int
                pButtons: IPointer[TASKDIALOG_BUTTON]
                nDefaultButton: int
                cRadioButtons: int
                pRadioButtons: IPointer[TASKDIALOG_BUTTON]
                nDefaultRadioButton: int
                pszVerificationText: LPCWSTR
                pszExpandedInformation: LPCWSTR
                pszExpandedControlText: LPCWSTR
                pszCollapsedControlText: LPCWSTR
                hFooterIcon: int
                pszFooterIcon: LPCWSTR
                pszFooter: LPCWSTR
                pfCallback: FARPROC
                lpCallbackData: int
                cxWidth: int

            @comctl32.foreign(HRESULT, PTR(TASKDIALOGCONFIG), PINT, PINT, PBOOL)
            def TaskDialogIndirect(self, pTaskConfig: IPointer[TASKDIALOGCONFIG], pnButton: PINT, pnRadioButton: PINT, pfVerificationFlagChecked: PBOOL) -> int: ...
            
            @comctl32.foreign(HRESULT, HWND, HINSTANCE, LPCWSTR, LPCWSTR, LPCWSTR, TASKDIALOG_COMMON_BUTTON_FLAGS, LPCWSTR, PINT)
            def TaskDialog(self, hwndOwner: int, hInstance: int, pszWindowTitle: LPCWSTR, pszMainInstruction: LPCWSTR, pszContent: LPCWSTR, dwCommonButtons: int, pszIcon: LPCWSTR, pnButton: PINT) -> int: ...

        # (_WINVER >= WIN32_WINNT_VISTA)
    # NOTASKDIALOG
    # ==================== End TaskDialog =======================
    #
    # === MUI APIs ===
    #
    if cpreproc.ifndef('NOMUI'):
        @comctl32.foreign(VOID, LANGID)
        def InitMUILanguage(uiLang: int): ...
        
        @comctl32.foreign(LANGID)
        def GetMUILanguage() -> int: ...
    # NOMUI
    # ====== Flat Scrollbar APIs=========================================
    if cpreproc.ifndef('NOFLATSBAPIS'):
        WSB_PROP_CYVSCROLL  = 0x00000001
        WSB_PROP_CXHSCROLL  = 0x00000002
        WSB_PROP_CYHSCROLL  = 0x00000004
        WSB_PROP_CXVSCROLL  = 0x00000008
        WSB_PROP_CXHTHUMB   = 0x00000010
        WSB_PROP_CYVTHUMB   = 0x00000020
        WSB_PROP_VBKGCOLOR  = 0x00000040
        WSB_PROP_HBKGCOLOR  = 0x00000080
        WSB_PROP_VSTYLE     = 0x00000100
        WSB_PROP_HSTYLE     = 0x00000200
        WSB_PROP_WINSTYLE   = 0x00000400
        WSB_PROP_PALETTE    = 0x00000800
        WSB_PROP_MASK       = 0x00000FFF

        FSB_FLAT_MODE       = 2
        FSB_ENCARTA_MODE    = 1
        FSB_REGULAR_MODE    = 0
        
        @comctl32.foreign(BOOL, HWND, INT, UINT)
        def FlatSB_EnableScrollBar(hWndParent: int, code: int, esbFlags: int) -> int: ...
        
        @comctl32.foreign(BOOL, HWND, INT, BOOL)
        def FlatSB_ShowScrollBar(hWndParent: int, code: int, fShow: int) -> int: ...
        
        @comctl32.foreign(BOOL, HWND, INT, LPINT, LPINT)
        def FlatSB_GetScrollRange(hWndParent: int, code: int, piMin: LPINT, piMax: LPINT) -> int: ...
        
        @comctl32.foreign(BOOL, HWND, INT, LPSCROLLINFO)
        def FlatSB_GetScrollInfo(hWndParent: int, code: int, pScrollInfo: IPointer[SCROLLINFO]) -> int: ...
        
        @comctl32.foreign(INT, HWND, INT)
        def FlatSB_GetScrollPos(hWndParent: int, code: int) -> int: ...
        
        @comctl32.foreign(BOOL, HWND, INT, LPINT)
        def FlatSB_GetScrollProp(hWndParent: int, propIndex: int, piData: LPINT) -> int: ...
        
        if cpreproc.ifdef('_WIN64'):
            @comctl32.foreign(BOOL, HWND, INT, PINT_PTR)
            def FlatSB_GetScrollPropPtr(hWndParent: int, propIndex: int, piData: PINT_PTR) -> int: ...
        else:
            FlatSB_GetScrollPropPtr = FlatSB_GetScrollProp
            
        @comctl32.foreign(INT, HWND, INT, INT, BOOL)
        def FlatSB_SetScrollPos(hWndParent: int, code: int, pos: int, fRedraw: int) -> int: ...
        
        @comctl32.foreign(INT, HWND, INT, LPSCROLLINFO, BOOL)
        def FlatSB_SetScrollInfo(hWndParent: int, code: int, psi: IPointer[SCROLLINFO], fRedraw: int) -> int: ...
        
        @comctl32.foreign(INT, HWND, INT, INT, INT, BOOL)
        def FlatSB_SetScrollRange(hWndParent: int, code: int, min: int, max: int, fRedraw: int) -> int: ...
        
        @comctl32.foreign(BOOL, HWND, UINT, INT_PTR, BOOL)
        def FlatSB_SetScrollProp(hWndParent: int, index: int, newValue: int, fRedraw: int) -> int: ...
        
        FlatSB_SetScrollPropPtr = FlatSB_SetScrollProp
        
        @comctl32.foreign(BOOL, HWND)
        def InitializeFlatSB(hWndParent: int) -> int: ...
        
        @comctl32.foreign(HRESULT, HWND)
        def UninitializeFlatSB(hWndParent: int) -> int: ...
    # NOFLATSBAPIS