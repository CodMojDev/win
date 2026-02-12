
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

from .guiddef import LPIID, REFIID

from .winuser import *

from .winnt import TEXT

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

    InitCommonControls = declare(comctl32.InitCommonControls, VOID, VOID)

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
    InitCommonControlsEx = declare(comctl32.InitCommonControlsEx, BOOL, LPINITCOMMONCONTROLSEX)
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
    NMOBJECTNOTIFY = tagNMOBJECTNOTIFY
    LPNMOBJECTNOTIFY = POINTER(NMOBJECTNOTIFY)

    # Generic structure for a key

    class tagNMKEY(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("nVKey", UINT),
            ("uFlags", UINT)
        ]
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
    if not "WMN_FIRST" in globals():
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
    NMCUSTOMDRAW = tagNMCUSTOMDRAWINFO
    LPNMCUSTOMDRAW = POINTER(NMCUSTOMDRAW)

    class tagNMTTCUSTOMDRAW(CStructure):
        _fields_ = [
            ("nmcd", NMCUSTOMDRAW),
            ("uDrawFlags", UINT)
        ]
    NMTTCUSTOMDRAW = tagNMTTCUSTOMDRAW
    LPNMTTCUSTOMDRAW = POINTER(NMTTCUSTOMDRAW)

    class tagNMCUSTOMSPLITRECTINFO(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("rcClient", RECT),
            ("rcButton", RECT),
            ("rcSplit", RECT)
        ]
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
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
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
        IMAGEINFO = _IMAGEINFO
        LPIMAGEINFO = POINTER(IMAGEINFO)

        ImageList_GetIconSize = declare(comctl32.ImageList_GetIconSize, BOOL, HIMAGELIST, PINT, PINT)
        ImageList_SetIconSize = declare(comctl32.ImageList_SetIconSize, BOOL, HIMAGELIST, INT, INT)
        ImageList_GetImageInfo = declare(comctl32.ImageList_GetImageInfo, BOOL, HIMAGELIST, INT, LPIMAGEINFO)
        ImageList_Merge = declare(comctl32.ImageList_Merge, HIMAGELIST, HIMAGELIST, INT, HIMAGELIST, INT, INT, INT)
        ImageList_Duplicate = declare(comctl32.ImageList_Duplicate, HIMAGELIST, HIMAGELIST)

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
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
    HD_TEXTFILTERA = _HD_TEXTFILTERA
    LPHD_TEXTFILTERA = POINTER(HD_TEXTFILTERA)

    class _HD_TEXTFILTERW(CStructure):
        _fields_ = [
            ("pszText", LPWSTR), # [in] pointer to the buffer containing the filter (Unicode)
            ("cchTextMax", INT) # [in] max size of buffer/edit control buffer
        ]
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
    if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        del _HD_ITEMA.state
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
            ("pvFilter", PVOID), # [in] filter data see above
            ("state", UINT)
        ]
    if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        del _HD_ITEMW.state
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

    def eader_GetImageList(hwnd):
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
    NMHEADERA = tagNMHEADERA
    LPNMHEADERA = POINTER(NMHEADERA)

    class tagNMHEADERW(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("iItem", INT),
            ("iButton", INT),
            ("pItem", LPHDITEMW)
        ]
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
        TBBUTTON = _TBBUTTON
        PTBBUTTON = POINTER(TBBUTTON)
        LPTBBUTTON = PTBBUTTON
        LPCTBBUTTON = PTBBUTTON


        class _COLORMAP(CStructure):
            _fields_ = [
                ("from", COLORREF),
                ("to", COLORREF)
            ]
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
                ("nHLStringBkMode", INT),
                ("iListGap", INT)
            ]
        if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            del _NMTBCUSTOMDRAW.iListGap
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
        TBSAVEPARAMSA = tagTBSAVEPARAMSA
        LPTBSAVEPARAMSA = POINTER(TBSAVEPARAMSA)
        
        class tagTBSAVEPARAMSW(CStructure):
            _fields_ = [
                ("hkr", HKEY),
                ("pszSubKey", LPCWSTR),
                ("pszValueName", LPCWSTR)
            ]
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
                ("cxHeader", UINT),
                ("rcChevronLocation", RECT), # the rect is in client co-ord wrt hwndChild
                ("uChevronState", UINT), # STATE_SYSTEM_*
            ]
        if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            del tagREBARBANDINFOA.rcChevronLocation
            del tagREBARBANDINFOA.uChevronState
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
        if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            del tagREBARBANDINFOW.rcChevronLocation
            del tagREBARBANDINFOW.uChevronState
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
        NMREBARCHEVRON = tagNMREBARCHEVRON
        LPNMREBARCHEVRON = POINTER(NMREBARCHEVRON)

        class tagNMREBARSPLITTER(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("rcSizing", RECT)
            ]
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
                ("lParam", LPARAM),
                ("lpReserved", PVOID)
            ]
        if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            del tagTOOLINFOA.lpReserved
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
                ("lParam", LPARAM),
                ("lpReserved", PVOID)
            ]
        if not cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            del tagTOOLINFOW.lpReserved
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

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            TTM_SETWINDOWTHEME = CCM_SETWINDOWTHEME

        class _TT_HITTESTINFOA(CStructure):
            _fields_ = [
                ("hwnd", HWND),
                ("pt", POINT),
                ("ti", TTTOOLINFOA)
            ]
        TTHITTESTINFOA = _TT_HITTESTINFOA
        LPTTHITTESTINFOA = POINTER(TTHITTESTINFOA)

        class _TT_HITTESTINFOW(CStructure):
            _fields_ = [
                ("hwnd", HWND),
                ("pt", POINT),
                ("ti", TTTOOLINFOW)
            ]
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

        # trackbar

        #====== DRAG LIST CONTROL ====================================================

    if cpreproc.ifndef("NODRAGLIST"):
        class DRAGLISTINFO(CStructure):
            _fields_ = [
                ("uNotification", UINT),
                ("hWnd", HWND),
                ("ptCursor", POINT)
            ]
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
        LPNMUPDOWN = POINTER(NMUPDOWN)
        
        NM_UPDOWN = NMUPDOWN
        LPNM_UPDOWN = LPNMUPDOWN

        UDN_DELTAPOS = (UDN_FIRST - 1)
    # NOUPDOWN
    #====== PROGRESS CONTROL =====================================================
    if cpreproc.ifndef("NOPROGRESS"):
        if cpreproc.ifdef("_WIN32"):
            PROGRESS_CLASSA = "msctls_progress32"
            PROGRESS_CLASSW = u"msctls_progress32"
            PROGRESS_CLASS = unicode(PROGRESS_CLASSW, PROGRESS_CLASSA)
        else:
            PROGRESS_CLASS = "msctls_progress"
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
        PLITEM = POINTER(LITEM)

        class LHITTESTINFO(CStructure):
            _fields_ = [
                ("pt", POINT),
                ("item", LITEM)
            ]
        PLHITTESTINFO = POINTER(LHITTESTINFO)

        class NMLINK(CStructure):
            _fields_ = [
                ("hdr", NMHDR),
                ("item", LITEM)
            ]
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
        if cpreproc.ifdef("_WIN32"):
            WC_LISTVIEWA = "SysListView32"
            WC_LISTVIEWW = u"SysListView32"
            WC_LISTVIEW = unicode(WC_LISTVIEWW, WC_LISTVIEWA)
        else:
            WC_LISTVIEW = "SysListView"
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
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            LVITEMA__fields_.append(("iGroupId", INT))
            LVITEMA__fields_.append(("cColumns", UINT)) # tile view columns
            LVITEMA__fields_.append(("puColumns", PUINT))
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA: # Will be unused downlevel, but sizeof(LVITEMA) must be equal to sizeof(LVITEMW)
            LVITEMA__fields_.append(("piColFmt", PINT))
            LVITEMA__fields_.append(("iGroup", INT)) # readonly. only valid for owner data.
        class LVITEMA(CStructure):
            _fields_ = LVITEMA__fields_
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
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            LVITEMW__fields_.append(("iGroupId", INT))
            LVITEMW__fields_.append(("cColumns", UINT)) # tile view columns
            LVITEMW__fields_.append(("puColumns", PUINT))
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA: # Will be unused downlevel, but sizeof(LVITEMA) must be equal to sizeof(LVITEMW)
            LVITEMW__fields_.append(("piColFmt", PINT))
            LVITEMW__fields_.append(("iGroup", INT)) # readonly. only valid for owner data.
        class LVITEMW(CStructure):
            _fields_ = LVITEMW__fields_
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
        LPFINDINFOA = POINTER(LVFINDINFOA)

        class LVFINDINFOW(CStructure):
            _fields_ = [
                ("flags", UINT),
                ("psz", LPCWSTR),
                ("lParam", LPARAM),
                ("pt", POINT),
                ("vkDirection", UINT)
            ]
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
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            _LVHITTESTINFO_fields_.append(
                ("iGroup", INT) # readonly. index of group. only valid for owner data.
                                # supports single item in multiple groups.
            )
        
        class LVHITTESTINFO(CStructure):
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

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            _LVCOLUMNA_fields_.append(("cxMin", INT))      # min snap point
            _LVCOLUMNA_fields_.append(("cxDefault", INT))  # default snap point
            _LVCOLUMNA_fields_.append(("cxIdeal", INT))    # read only. ideal may not eqaul current width if auto sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
        
        class LVCOLUMNA(CStructure):
            _fields_ = _LVCOLUMNA_fields_
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

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            _LVCOLUMNW_fields_.append(("cxMin", INT))      # min snap point
            _LVCOLUMNW_fields_.append(("cxDefault", INT))  # default snap point
            _LVCOLUMNW_fields_.append(("cxIdeal", INT))    # read only. ideal may not eqaul current width if auto sized (LVS_EX_AUTOSIZECOLUMNS) to a lesser width.
        
        class LVCOLUMNW(CStructure):
            _fields_ = _LVCOLUMNW_fields_
        LPLVCOLUMNW = POINTER(LVCOLUMNW)
        LVCOLUMN = unicode(LVCOLUMNW, LVCOLUMNA)
        LPLVCOLUMN = unicode(LPLVCOLUMNW, LPLVCOLUMNA)
        
        LV_COLUMNA = LVCOLUMNA
        LV_COLUMNW = LVCOLUMNW

        LV_COLUMN = LVCOLUMN

        LVCOLUMNA_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNA, "iSubItem")
        LVCOLUMNW_V1_SIZE = CCSIZEOF_STRUCT(LVCOLUMNW, "iSubItem")