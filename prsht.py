"""
 /*****************************************************************************\\
 *                                                                             *
 * prsht.h - - Interface for the Windows Property Sheet Pages                  *
 *                                                                             *
 * Version 1.0                                                                 *
 *                                                                             *
 * Copyright (c) Microsoft Corporation. All rights reserved.                   *
 *                                                                             *
\\*****************************************************************************/
"""

from .minwindef import *

from .sdkddkver import *
from .winnt import (CALLBACK, PVOID)
from .winuser import (LPCDLGTEMPLATE, DLGPROC, 
                      SendMessage, PostMessage,
                      NMHDR, WM_USER, 
                      LPCDLGTEMPLATEA, 
                      LPCDLGTEMPLATEW,
                      DLGTEMPLATE)
from typing import Union as TUnion

from .defbase import *

from . import cpreproc

if cpreproc.pragma_once("_PRSHT_H_"):
    comctl32 = W_WinDLL("comctl32.dll")
    
    MAXPROPPAGES = 100

    HPROPSHEETPAGE = HANDLE
    PPROPSHEETPAGEA = PVOID
    PPROPSHEETPAGEW = PVOID

    LPFNPSPCALLBACKA = CALLBACK(UINT, HWND, UINT, PPROPSHEETPAGEA)
    LPFNPSPCALLBACKW = CALLBACK(UINT, HWND, UINT, PPROPSHEETPAGEW)
    LPFNPSPCALLBACK = unicode(LPFNPSPCALLBACKW, LPFNPSPCALLBACKA)

    PSP_DEFAULT = 0x00000000
    PSP_DLGINDIRECT = 0x00000001
    PSP_USEHICON = 0x00000002
    PSP_USEICONID = 0x00000004
    PSP_USETITLE = 0x00000008
    PSP_RTLREADING = 0x00000010
    PSP_HASHELP = 0x00000020
    PSP_USEREFPARENT = 0x00000040
    PSP_USECALLBACK = 0x00000080
    PSP_PREMATURE = 0x00000400
    #----- New flags for wizard97 --------------
    PSP_HIDEHEADER = 0x00000800
    PSP_USEHEADERTITLE = 0x00001000
    PSP_USEHEADERSUBTITLE = 0x00002000
    #-------------------------------------------
    PSP_USEFUSIONCONTEXT = 0x00004000
    PSPCB_ADDREF = 0
    PSPCB_RELEASE = 1
    PSPCB_CREATE = 2

    if cpreproc.ifdef("_WIN32"):
        PROPSHEETPAGE_RESOURCE = LPCDLGTEMPLATE
    else:
        PROPSHEETPAGE_RESOURCE = LPCVOID

    class _U_PTPRA(Union):
        _fields_ = [
            ("pszTemplate", LPCSTR),
            ("pResource", PROPSHEETPAGE_RESOURCE)
        ]
        
        pResource: TUnion[LPCVOID, IPointer[DLGTEMPLATE]]
        pszTemplate: bytes
    
    class _U_HIPIA(Union):
        _fields_ = [
            ("hIcon", HICON),
            ("pszIcon", LPCSTR)
        ]

    class _PROPSHEETPAGEA_V1(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRA),
            ("u2", _U_HIPIA),
            ("pszTitle", LPCSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKA),
            ("pcRefParent", PUINT)
        ]
    PROPSHEETPAGEA_V1 = _PROPSHEETPAGEA_V1
    LPPROPSHEETPAGEA_V1 = POINTER(PROPSHEETPAGEA_V1)
    LPCPROPSHEETPAGEA_V1 = LPPROPSHEETPAGEA_V1

    class _U_PTPRW(Union):
        _fields_ = [
            ("pszTemplate", LPCWSTR),
            ("pResource", PROPSHEETPAGE_RESOURCE)
        ]
    
    class _U_HIPIW(Union):
        _fields_ = [
            ("hIcon", HICON),
            ("pszIcon", LPCWSTR)
        ]

    class _PROPSHEETPAGEW_V1(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRW),
            ("u2", _U_HIPIW),
            ("pszTitle", LPCWSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKW),
            ("pcRefParent", PUINT)
        ]
    PROPSHEETPAGEW_V1 = _PROPSHEETPAGEW_V1
    LPPROPSHEETPAGEW_V1 = POINTER(PROPSHEETPAGEW_V1)
    LPCPROPSHEETPAGEW_V1 = LPPROPSHEETPAGEW_V1

    class _PROPSHEETPAGEA_V2(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRA),
            ("u2", _U_HIPIA),
            ("pszTitle", LPCSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKA),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCSTR),
            ("pszHeaderSubTitle", LPCSTR)
        ]
    PROPSHEETPAGEA_V2 = _PROPSHEETPAGEA_V2
    LPPROPSHEETPAGEA_V2 = POINTER(PROPSHEETPAGEA_V2)
    LPCPROPSHEETPAGEA_V2 = LPPROPSHEETPAGEA_V2

    class _PROPSHEETPAGEW_V2(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRW),
            ("u2", _U_HIPIW),
            ("pszTitle", LPCWSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKW),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCWSTR),
            ("pszHeaderSubTitle", LPCWSTR)
        ]
    PROPSHEETPAGEW_V2 = _PROPSHEETPAGEW_V2
    LPPROPSHEETPAGEW_V2 = POINTER(PROPSHEETPAGEW_V2)
    LPCPROPSHEETPAGEW_V2 = LPPROPSHEETPAGEW_V2

    class _PROPSHEETPAGEA_V3(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRA),
            ("u2", _U_HIPIA),
            ("pszTitle", LPCSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKA),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCSTR),
            ("pszHeaderSubTitle", LPCSTR),
            ("hActCtx", HANDLE)
        ]
    PROPSHEETPAGEA_V3 = _PROPSHEETPAGEA_V3
    LPPROPSHEETPAGEA_V3 = POINTER(PROPSHEETPAGEA_V3)
    LPCPROPSHEETPAGEA_V3 = LPPROPSHEETPAGEA_V3

    class _PROPSHEETPAGEW_V3(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRW),
            ("u2", _U_HIPIW),
            ("pszTitle", LPCWSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKW),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCWSTR),
            ("pszHeaderSubTitle", LPCWSTR),
            ("hActCtx", HANDLE)
        ]
    PROPSHEETPAGEW_V3 = _PROPSHEETPAGEW_V3
    LPPROPSHEETPAGEW_V3 = POINTER(PROPSHEETPAGEW_V3)
    LPCPROPSHEETPAGEW_V3 = LPPROPSHEETPAGEW_V3

    class _U_HHPHA(Union):
        _fields_ = [
            ("hbmHeader", HBITMAP),
            ("pszbmHeader", LPCSTR)
        ]

    class _PROPSHEETPAGEA_V4(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRA),
            ("u2", _U_HIPIA),
            ("pszTitle", LPCSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKA),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCSTR),
            ("pszHeaderSubTitle", LPCSTR),
            ("hActCtx", HANDLE),
            ("u3", _U_HHPHA)
        ]
    PROPSHEETPAGEA_V4 = _PROPSHEETPAGEA_V4
    LPPROPSHEETPAGEA_V4 = POINTER(PROPSHEETPAGEA_V4)
    LPCPROPSHEETPAGEA_V4 = LPPROPSHEETPAGEA_V4

    class _U_HHPHW(Union):
        _fields_ = [
            ("hbmHeader", HBITMAP),
            ("pszbmHeader", LPCWSTR)
        ]

    class _PROPSHEETPAGEW_V4(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),
            ("u", _U_PTPRW),
            ("u2", _U_HIPIW),
            ("pszTitle", LPCWSTR),
            ("pfnDlgProc", DLGPROC),
            ("lParam", LPARAM),
            ("pfnCallback", LPFNPSPCALLBACKW),
            ("pcRefParent", PUINT),
            ("pszHeaderTitle", LPCWSTR),
            ("pszHeaderSubTitle", LPCWSTR),
            ("hActCtx", HANDLE),
            ("u3", _U_HHPHW)
        ]
    PROPSHEETPAGEW_V4 = _PROPSHEETPAGEW_V4
    LPPROPSHEETPAGEW_V4 = POINTER(PROPSHEETPAGEW_V4)
    LPCPROPSHEETPAGEW_V4 = LPPROPSHEETPAGEW_V4

    PROPSHEETPAGEA_V1_SIZE = sizeof(PROPSHEETPAGEA_V1)
    PROPSHEETPAGEW_V1_SIZE = sizeof(PROPSHEETPAGEW_V1)

    PROPSHEETPAGEA_V2_SIZE = sizeof(PROPSHEETPAGEA_V2)
    PROPSHEETPAGEW_V2_SIZE = sizeof(PROPSHEETPAGEW_V2)

    PROPSHEETPAGEA_V3_SIZE = sizeof(PROPSHEETPAGEA_V3)
    PROPSHEETPAGEW_V3_SIZE = sizeof(PROPSHEETPAGEW_V3)

    PROPSHEETPAGEA_V4_SIZE = sizeof(PROPSHEETPAGEA_V4)
    PROPSHEETPAGEW_V4_SIZE = sizeof(PROPSHEETPAGEW_V4)
    
    _winver_ = cpreproc.getdef("_WINVER")

    if _winver_ >= WIN32_WINNT_VISTA:
        PROPSHEETPAGEA_LATEST = PROPSHEETPAGEA_V4
        PROPSHEETPAGEW_LATEST = PROPSHEETPAGEW_V4
        LPPROPSHEETPAGEA_LATEST = LPCPROPSHEETPAGEA_V4
        LPPROPSHEETPAGEW_LATEST = LPCPROPSHEETPAGEW_V4
        LPCPROPSHEETPAGEA_LATEST = LPCPROPSHEETPAGEA_V4
        LPCPROPSHEETPAGEW_LATEST = LPCPROPSHEETPAGEW_V4
    else:
        PROPSHEETPAGEA_LATEST = PROPSHEETPAGEA_V3
        PROPSHEETPAGEW_LATEST = PROPSHEETPAGEW_V3
        LPPROPSHEETPAGEA_LATEST = LPCPROPSHEETPAGEA_V3
        LPPROPSHEETPAGEW_LATEST = LPCPROPSHEETPAGEW_V3
        LPCPROPSHEETPAGEA_LATEST = LPCPROPSHEETPAGEA_V3
        LPCPROPSHEETPAGEW_LATEST = LPCPROPSHEETPAGEW_V3
        
    if _winver_ >= WIN32_WINNT_VISTA:
        PROPSHEETPAGEA = PROPSHEETPAGEA_V4
        PROPSHEETPAGEW = PROPSHEETPAGEW_V4
        LPPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V4
        LPPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V4
        LPCPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V4
        LPCPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V4
    elif _winver_ >= WIN32_WINNT_WINXP:
        PROPSHEETPAGEA = PROPSHEETPAGEA_V3
        PROPSHEETPAGEW = PROPSHEETPAGEW_V3
        LPPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V3
        LPPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V3
        LPCPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V3
        LPCPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V3
    else:
        PROPSHEETPAGEA = PROPSHEETPAGEA_V2
        PROPSHEETPAGEW = PROPSHEETPAGEW_V2
        LPPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V2
        LPPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V2
        LPCPROPSHEETPAGEA = LPCPROPSHEETPAGEA_V2
        LPCPROPSHEETPAGEW = LPCPROPSHEETPAGEW_V2

    PROPSHEETPAGE_V1 = unicode(PROPSHEETPAGEW_V1, PROPSHEETPAGEA_V1)
    PROPSHEETPAGE_V2 = unicode(PROPSHEETPAGEW_V2, PROPSHEETPAGEA_V2)
    PROPSHEETPAGE_V3 = unicode(PROPSHEETPAGEW_V3, PROPSHEETPAGEA_V3)
    PROPSHEETPAGE_V4 = unicode(PROPSHEETPAGEW_V4, PROPSHEETPAGEA_V4)
    LPPROPSHEETPAGE_V1 = unicode(LPCPROPSHEETPAGEW_V1, LPCPROPSHEETPAGEA_V1)
    LPPROPSHEETPAGE_V2 = unicode(LPCPROPSHEETPAGEW_V2, LPCPROPSHEETPAGEA_V2)
    LPPROPSHEETPAGE_V3 = unicode(LPCPROPSHEETPAGEW_V3, LPCPROPSHEETPAGEA_V3)
    LPPROPSHEETPAGE_V4 = unicode(LPCPROPSHEETPAGEW_V4, LPCPROPSHEETPAGEA_V4)
    LPCPROPSHEETPAGE_V1 = unicode(LPCPROPSHEETPAGEW_V1, LPCPROPSHEETPAGEA_V1)
    LPCPROPSHEETPAGE_V2 = unicode(LPCPROPSHEETPAGEW_V2, LPCPROPSHEETPAGEA_V2)
    LPCPROPSHEETPAGE_V3 = unicode(LPCPROPSHEETPAGEW_V3, LPCPROPSHEETPAGEA_V3)
    LPCPROPSHEETPAGE_V4 = unicode(LPCPROPSHEETPAGEW_V4, LPCPROPSHEETPAGEA_V4)

    PROPSHEETPAGE_LATEST = unicode(PROPSHEETPAGEW_LATEST, PROPSHEETPAGEA_LATEST)
    LPPROPSHEETPAGE_LATEST = unicode(LPCPROPSHEETPAGEW_LATEST, LPCPROPSHEETPAGEA_LATEST)
    LPCPROPSHEETPAGE_LATEST = unicode(LPCPROPSHEETPAGEW_LATEST, LPCPROPSHEETPAGEA_LATEST)

    #----- PropSheet Header related ---------
    PSH_DEFAULT = 0x00000000
    PSH_PROPTITLE = 0x00000001
    PSH_USEHICON = 0x00000002
    PSH_USEICONID = 0x00000004
    PSH_PROPSHEETPAGE = 0x00000008
    PSH_WIZARDHASFINISH = 0x00000010
    PSH_WIZARD = 0x00000020
    PSH_USEPSTARTPAGE = 0x00000040
    PSH_NOAPPLYNOW = 0x00000080
    PSH_USECALLBACK = 0x00000100
    PSH_HASHELP = 0x00000200
    PSH_MODELESS = 0x00000400
    PSH_RTLREADING = 0x00000800
    PSH_WIZARDCONTEXTHELP = 0x00001000
    #----- New flags for wizard97 -----------
    PSH_WIZARD97 = 0x00002000
    PSH_WIZARD97 = 0x01000000
    PSH_WATERMARK = 0x00008000
    PSH_USEHBMWATERMARK = 0x00010000 # user pass in a hbmWatermark instead of pszbmWatermark
    PSH_USEHPLWATERMARK = 0x00020000 #
    PSH_STRETCHWATERMARK = 0x00040000 # stretchwatermark also applies for the header
    PSH_HEADER = 0x00080000
    PSH_USEHBMHEADER = 0x00100000
    PSH_USEPAGELANG = 0x00200000 # use frame dialog template matched to page
    #----------------------------------------
    #----- New flags for wizard-lite --------
    PSH_WIZARD_LITE = 0x00400000
    PSH_NOCONTEXTHELP = 0x02000000
    #----------------------------------------
    PSH_AEROWIZARD = 0x00004000
    PSH_RESIZABLE = 0x04000000
    PSH_HEADERBITMAP = 0x08000000
    PSH_NOMARGIN = 0x10000000

    PFNPROPSHEETCALLBACK = CALLBACK(INT, HWND, UINT, LPARAM)

    class _U_PP(Union):
        _fields_ = [
            ("ppsp", LPCPROPSHEETPAGEA),
            ("phpage", POINTER(HPROPSHEETPAGE))
        ]

    class _U_NSPPSPA(Union):
        _fields_ = [
            ("nStartPage", UINT),
            ("pStartPage", LPCSTR)
        ]

    class _PROPSHEETHEADERA_V1(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hwndParent", HWND),
            ("hInstance", HINSTANCE),
            ("u", _U_HIPIA),
            ("pszCaption", LPCSTR),
            ("nPages", UINT),
            ("u2", _U_NSPPSPA),
            ("u3", _U_PP),
            ("pfnCallback", PFNPROPSHEETCALLBACK)
        ] 
    PROPSHEETHEADERA_V1 = _PROPSHEETHEADERA_V1
    LPPROPSHEETHEADERA_V1 = POINTER(PROPSHEETHEADERA_V1)
    LPCPROPSHEETHEADERA_V1 = LPPROPSHEETHEADERA_V1

    class _U_NSPPSPW(Union):
        _fields_ = [
            ("nStartPage", UINT),
            ("pStartPage", LPCWSTR)
        ]

    class _PROPSHEETHEADERW_V1(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hwndParent", HWND),
            ("hInstance", HINSTANCE),
            ("u", _U_HIPIW),
            ("pszCaption", LPCWSTR),
            ("nPages", UINT),
            ("u2", _U_NSPPSPW),
            ("u3", _U_PP),
            ("pfnCallback", PFNPROPSHEETCALLBACK)
        ] 
    PROPSHEETHEADERW_V1 = _PROPSHEETHEADERW_V1 
    LPPROPSHEETHEADERW_V1 = POINTER(PROPSHEETHEADERW_V1)
    LPCPROPSHEETHEADERW_V1 = LPPROPSHEETHEADERW_V1

    class _U_HWPWA(Union):
        _fields_ = [
            ("hbmWatermark", HBITMAP),
            ("pszbmWatermark", LPCSTR)
        ]

    class _PROPSHEETHEADERA_V2(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hwndParent", HWND),
            ("hInstance", HINSTANCE),
            ("u", _U_HIPIA),
            ("pszCaption", LPCSTR),
            ("nPages", UINT),
            ("u2", _U_NSPPSPA),
            ("u3", _U_PP),
            ("pfnCallback", PFNPROPSHEETCALLBACK),
            ("u4", _U_HWPWA),
            ("hplWatermark", HPALETTE),
            ("u5", _U_HHPHA)
        ] 
    PROPSHEETHEADERA_V2 = _PROPSHEETHEADERA_V2
    LPPROPSHEETHEADERA_V2 = POINTER(PROPSHEETHEADERA_V2)
    LPCPROPSHEETHEADERA_V2 = LPPROPSHEETHEADERA_V2

    class _U_HWPWW(Union):
        _fields_ = [
            ("hbmWatermark", HBITMAP),
            ("pszbmWatermark", LPCWSTR)
        ]

    class _PROPSHEETHEADERW_V2(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("hwndParent", HWND),
            ("hInstance", HINSTANCE),
            ("u", _U_HIPIW),
            ("pszCaption", LPCWSTR),
            ("nPages", UINT),
            ("u2", _U_NSPPSPW),
            ("u3", _U_PP),
            ("pfnCallback", PFNPROPSHEETCALLBACK),
            ("u4", _U_HWPWW),
            ("hplWatermark", HPALETTE),
            ("u5", _U_HHPHW)
        ] 
    PROPSHEETHEADERW_V2 = _PROPSHEETHEADERW_V2
    LPPROPSHEETHEADERW_V2 = POINTER(PROPSHEETHEADERW_V2)
    LPCPROPSHEETHEADERW_V2 = LPPROPSHEETHEADERW_V2

    PROPSHEETHEADERA_V1_SIZE = sizeof(PROPSHEETHEADERA_V1)
    PROPSHEETHEADERW_V1_SIZE = sizeof(PROPSHEETHEADERW_V1)

    PROPSHEETHEADERA_V2_SIZE = sizeof(PROPSHEETHEADERA_V2)
    PROPSHEETHEADERW_V2_SIZE = sizeof(PROPSHEETHEADERW_V2)

    PROPSHEETHEADER_V1 = unicode(PROPSHEETHEADERW_V1, PROPSHEETHEADERA_V1)
    PROPSHEETHEADER_V1 = unicode(PROPSHEETHEADERW_V1, PROPSHEETHEADERA_V1)
    LPPROPSHEETHEADER_V1 = unicode(LPPROPSHEETHEADERW_V1, LPPROPSHEETHEADERA_V1)
    LPPROPSHEETHEADER_V1 = unicode(LPPROPSHEETHEADERW_V1, LPPROPSHEETHEADERA_V1)
    LPCPROPSHEETHEADER_V1 = unicode(LPCPROPSHEETHEADERW_V1, LPCPROPSHEETHEADERA_V1)
    LPCPROPSHEETHEADER_V1 = unicode(LPCPROPSHEETHEADERW_V1, LPCPROPSHEETHEADERA_V1)

    PROPSHEETHEADER_V2 = unicode(PROPSHEETHEADERW_V2, PROPSHEETHEADERA_V2)
    PROPSHEETHEADER_V2 = unicode(PROPSHEETHEADERW_V2, PROPSHEETHEADERA_V2)
    LPPROPSHEETHEADER_V2 = unicode(LPPROPSHEETHEADERW_V2, LPPROPSHEETHEADERA_V2)
    LPPROPSHEETHEADER_V2 = unicode(LPPROPSHEETHEADERW_V2, LPPROPSHEETHEADERA_V2)
    LPCPROPSHEETHEADER_V2 = unicode(LPCPROPSHEETHEADERW_V2, LPCPROPSHEETHEADERA_V2)
    LPCPROPSHEETHEADER_V2 = unicode(LPCPROPSHEETHEADERW_V2, LPCPROPSHEETHEADERA_V2)

    PROPSHEETHEADERA = PROPSHEETHEADERA_V2
    LPPROPSHEETHEADERA = LPPROPSHEETHEADERA_V2
    LPCPROPSHEETHEADERA = LPCPROPSHEETHEADERA_V2

    PROPSHEETHEADERW = PROPSHEETHEADERW_V2
    LPPROPSHEETHEADERW = LPPROPSHEETHEADERW_V2
    LPCPROPSHEETHEADERW = LPCPROPSHEETHEADERW_V2

    PROPSHEETHEADER_V1_SIZE = unicode(PROPSHEETHEADERW_V1_SIZE, PROPSHEETHEADERA_V1_SIZE)
    PROPSHEETHEADER_V2_SIZE = unicode(PROPSHEETHEADERW_V2_SIZE, PROPSHEETHEADERA_V2_SIZE)

    PSCB_INITIALIZED = 1
    PSCB_PRECREATE = 2

    # PSCB_BUTTONPRESSED will be sent when the user clicks a button in the
    # property dialog (OK, Cancel, Apply, or Close).  The message will be sent
    # to PROPSHEETHEADER's pfnCallback if the PSH_USECALLBACK flag was specified.
    # The LPARAM will be equal to one of the following based on the button pressed:
    # This message is only supported on comctl32 v6.
    # PSBTN_FINISH (Close), PSBTN_OK, PSBTN_APPLYNOW, or PSBTN_CANCEL

    PSCB_BUTTONPRESSED = 3

    CreatePropertySheetPageA = declare(comctl32.CreatePropertySheetPageA, HPROPSHEETPAGE, LPCPROPSHEETPAGEA)
    CreatePropertySheetPageW = declare(comctl32.CreatePropertySheetPageW, HPROPSHEETPAGE, LPCPROPSHEETPAGEW)
    DestroyPropertySheetPage = declare(comctl32.DestroyPropertySheetPage, BOOL, HPROPSHEETPAGE)
    PropertySheetA = declare(comctl32.PropertySheetA, INT_PTR, LPCPROPSHEETHEADERA)
    PropertySheetW = declare(comctl32.PropertySheetW, INT_PTR, LPCPROPSHEETHEADERW)
    CreatePropertySheetPage = unicode(CreatePropertySheetPageW, CreatePropertySheetPageA)
    PropertySheet = unicode(PropertySheetW, PropertySheetA)

    LPFNADDPROPSHEETPAGE = CALLBACK(BOOL, HPROPSHEETPAGE, LPARAM)
    LPFNADDPROPSHEETPAGES = CALLBACK(BOOL, LPVOID, LPFNADDPROPSHEETPAGE, LPARAM)

    class _PSHNOTIFY(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("lParam", LPARAM)
        ]
    PSHNOTIFY = _PSHNOTIFY
    LPPSHNOTIFY = POINTER(PSHNOTIFY)

    PSN_FIRST = (0-200)
    PSN_LAST = (0-299)
    PSN_SETACTIVE = (PSN_FIRST-0)
    PSN_KILLACTIVE = (PSN_FIRST-1)
    PSN_VALIDATE = (PSN_FIRST-1)
    PSN_APPLY = (PSN_FIRST-2)
    PSN_RESET = (PSN_FIRST-3)
    PSN_CANCEL = (PSN_FIRST-3)
    PSN_HELP = (PSN_FIRST-5)
    PSN_WIZBACK = (PSN_FIRST-6)
    PSN_WIZNEXT = (PSN_FIRST-7)
    PSN_WIZFINISH = (PSN_FIRST-8)
    PSN_QUERYCANCEL = (PSN_FIRST-9)
    PSN_GETOBJECT = (PSN_FIRST-10)
    PSN_TRANSLATEACCELERATOR = (PSN_FIRST-12)
    PSN_QUERYINITIALFOCUS = (PSN_FIRST-13)
    PSNRET_NOERROR = 0
    PSNRET_INVALID = 1
    PSNRET_INVALID_NOCHANGEPAGE = 2
    PSNRET_MESSAGEHANDLED = 3
    PSM_SETCURSEL = (WM_USER + 101)

    def PropSheet_SetCurSel(hDlg, hpage, index):
        SendMessage(hDlg, PSM_SETCURSEL, index, hpage)

    PSM_REMOVEPAGE = (WM_USER + 102)

    def PropSheet_RemovePage(hDlg, hpage, index):
        SendMessage(hDlg, PSM_REMOVEPAGE, index, hpage)

    PSM_ADDPAGE = (WM_USER + 103)

    def PropSheet_AddPage(hDlg, hpage):
        SendMessage(hDlg, PSM_ADDPAGE, 0, hpage)

    PSM_CHANGED = (WM_USER + 104)

    def PropSheet_Changed(hDlg, hwnd):
        SendMessage(hDlg, PSM_CHANGED, hwnd, 0)

    PSM_RESTARTWINDOWS = (WM_USER + 105)

    def PropSheet_RestartWindows(hDlg):
        SendMessage(hDlg, PSM_RESTARTWINDOWS, 0, 0)

    PSM_REBOOTSYSTEM = (WM_USER + 106)

    def PropSheet_RebootSystem(hDlg):
        SendMessage(hDlg, PSM_REBOOTSYSTEM, 0, 0)

    PSM_CANCELTOCLOSE = (WM_USER + 107)

    def PropSheet_CancelToClose(hDlg):
        PostMessage(hDlg, PSM_CANCELTOCLOSE, 0, 0)

    PSM_QUERYSIBLINGS = (WM_USER + 108)

    def PropSheet_QuerySiblings(hDlg, wParam, lParam):
        SendMessage(hDlg, PSM_QUERYSIBLINGS, wParam, lParam)
        
    PSM_UNCHANGED = (WM_USER + 109)

    def PropSheet_UnChanged(hDlg, hwnd):
        SendMessage(hDlg, PSM_UNCHANGED, hwnd, 0)
        
    PSM_APPLY = (WM_USER + 110)

    def PropSheet_Apply(hDlg):
        SendMessage(hDlg, PSM_APPLY, 0, 0)
        
    PSM_SETTITLEA = (WM_USER + 111)
    PSM_SETTITLEW = (WM_USER + 120)
    PSM_SETTITLE = unicode(PSM_SETTITLEW, PSM_SETTITLEA)

    def PropSheet_SetTitle(hDlg, wStyle, lpszText):
        SendMessage(hDlg, PSM_SETTITLE, wStyle, cast(lpszText, PVOID).value)

    PSM_SETWIZBUTTONS = (WM_USER + 112)

    def PropSheet_SetWizButtons(hDlg, dwFlags):
        PostMessage(hDlg, PSM_SETWIZBUTTONS, 0, dwFlags)
        
    PSWIZB_BACK = 0x00000001
    PSWIZB_NEXT = 0x00000002
    PSWIZB_FINISH = 0x00000004
    PSWIZB_DISABLEDFINISH = 0x00000008
    PSWIZBF_ELEVATIONREQUIRED = 0x00000001
    # Only for PSH_AEROWIZARD - used in PSM_SHOWWIZBUTTONS
    PSWIZB_CANCEL = 0x00000010
    PSM_PRESSBUTTON = (WM_USER + 113)

    def PropSheet_PressButton(hDlg, iButton):
        PostMessage(hDlg, PSM_PRESSBUTTON, iButton, 0)
        
    PSBTN_BACK = 0
    PSBTN_NEXT = 1
    PSBTN_FINISH = 2
    PSBTN_OK = 3
    PSBTN_APPLYNOW = 4
    PSBTN_CANCEL = 5
    PSBTN_HELP = 6
    PSBTN_MAX = 6
    PSM_SETCURSELID = (WM_USER + 114)

    def PropSheet_SetCurSelByID(hDlg, id):
        SendMessage(hDlg, PSM_SETCURSELID, 0, id)
        
    PSM_SETFINISHTEXTA = (WM_USER + 115)
    PSM_SETFINISHTEXTW = (WM_USER + 121)
    PSM_SETFINISHTEXT = unicode(PSM_SETFINISHTEXTW, PSM_SETFINISHTEXTA)

    def PropSheet_SetFinishText(hDlg, lpszText):
        SendMessage(hDlg, PSM_SETFINISHTEXT, 0, cast(lpszText, PVOID).value)
        
    PSM_GETTABCONTROL = (WM_USER + 116)

    def PropSheet_GetTabControl(hDlg):
        SendMessage(hDlg, PSM_GETTABCONTROL, 0, 0)
        
    PSM_ISDIALOGMESSAGE = (WM_USER + 117)

    def PropSheet_IsDialogMessage(hDlg, pMsg):
        SendMessage(hDlg, PSM_ISDIALOGMESSAGE, 0, pMsg)
        
    PSM_GETCURRENTPAGEHWND = (WM_USER + 118)

    def PropSheet_GetCurrentPageHwnd(hDlg):
        SendMessage(hDlg, PSM_GETCURRENTPAGEHWND, 0, 0)
        
    PSM_INSERTPAGE = (WM_USER + 119)

    def PropSheet_InsertPage(hDlg, hpage, index):
        SendMessage(hDlg, PSM_INSERTPAGE, index, hpage)
        
    # Only for PSH_AEROWIZARD - used in PSM_SETHEADERTITLE
    PSWIZF_SETCOLOR = ((UINT)(-1))
    PSM_SETHEADERTITLEA = (WM_USER + 125)
    PSM_SETHEADERTITLEW = (WM_USER + 126)
    PSM_SETHEADERTITLE = unicode(PSM_SETHEADERTITLEW, PSM_SETHEADERTITLEA)

    def PropSheet_SetHeaderTitle(hDlg, index, lpszText):
        SendMessage(hDlg, PSM_SETHEADERTITLE, index, cast(lpszText, PVOID).value)
        
    PSM_SETHEADERSUBTITLEA = (WM_USER + 127)
    PSM_SETHEADERSUBTITLEW = (WM_USER + 128)
    PSM_SETHEADERSUBTITLE = unicode(PSM_SETHEADERSUBTITLEW, PSM_SETHEADERSUBTITLEA)

    def PropSheet_SetHeaderSubTitle(hDlg, index, lpszText):
        SendMessage(hDlg, PSM_SETHEADERSUBTITLE, index, cast(lpszText, PVOID).value)
        
    PSM_HWNDTOINDEX = (WM_USER + 129)

    def PropSheet_HwndToIndex(hDlg, hwnd):
        SendMessage(hDlg, PSM_HWNDTOINDEX, hwnd, 0)
        
    PSM_INDEXTOHWND = (WM_USER + 130)

    def PropSheet_IndexToHwnd(hDlg, i):
        SendMessage(hDlg, PSM_INDEXTOHWND, i, 0)
        
    PSM_PAGETOINDEX = (WM_USER + 131)

    def PropSheet_PageToIndex(hDlg, hpage):
        SendMessage(hDlg, PSM_PAGETOINDEX, 0, hpage)
        
    PSM_INDEXTOPAGE = (WM_USER + 132)

    def PropSheet_IndexToPage(hDlg, i):
        SendMessage(hDlg, PSM_INDEXTOPAGE, i, 0)
        
    PSM_IDTOINDEX = (WM_USER + 133)

    def PropSheet_IdToIndex(hDlg, id):
        SendMessage(hDlg, PSM_IDTOINDEX, 0, id)
        
    PSM_INDEXTOID = (WM_USER + 134)

    def PropSheet_IndexToId(hDlg, i):
        SendMessage(hDlg, PSM_INDEXTOID, i, 0)
        
    PSM_GETRESULT = (WM_USER + 135)

    def PropSheet_GetResult(hDlg):
        SendMessage(hDlg, PSM_GETRESULT, 0, 0)
        
    PSM_RECALCPAGESIZES = (WM_USER + 136)

    def PropSheet_RecalcPageSizes(hDlg):
        SendMessage(hDlg, PSM_RECALCPAGESIZES, 0, 0)
        
    # Only UNICODE
    # These messages are only for Aero Wizard style wizards. The Wizard author
    # needs to specify the PSH_AEROWIZARD flag in the dwFlags member of the PROPSHEETHEADER
    # structure to get this behavior.
    PSM_SETNEXTTEXTW = (WM_USER + 137)
    PSM_SETNEXTTEXT = PSM_SETNEXTTEXTW

    def PropSheet_SetNextText(hDlg, lpszText):
        SendMessage(hDlg, PSM_SETNEXTTEXT, 0, cast(lpszText, PVOID).value)
        
    PSWIZB_SHOW = 0
    PSWIZB_RESTORE = 1
    PSM_SHOWWIZBUTTONS = (WM_USER + 138)

    def PropSheet_ShowWizButtons(hDlg, dwFlag, dwButton):
        PostMessage(hDlg, PSM_SHOWWIZBUTTONS, dwFlag, dwButton)
        
    PSM_ENABLEWIZBUTTONS = (WM_USER + 139)

    def PropSheet_EnableWizButtons(hDlg, dwState, dwMask):
        PostMessage(hDlg, PSM_ENABLEWIZBUTTONS, dwState, dwMask)
        
    PSM_SETBUTTONTEXTW = (WM_USER + 140)
    PSM_SETBUTTONTEXT = PSM_SETBUTTONTEXTW

    def PropSheet_SetButtonText(hDlg, dwButton, lpszText):
        SendMessage(hDlg, PSM_SETBUTTONTEXT, dwButton, cast(lpszText, PVOID).value)
        
    ID_PSRESTARTWINDOWS = 0x2
    ID_PSREBOOTSYSTEM = (ID_PSRESTARTWINDOWS | 0x1)
    WIZ_CXDLG = 276
    WIZ_CYDLG = 140
    WIZ_CXBMP = 80
    WIZ_BODYX = 92
    WIZ_BODYCX = 184
    PROP_SM_CXDLG = 212
    PROP_SM_CYDLG = 188
    PROP_MED_CXDLG = 227
    PROP_MED_CYDLG = 215
    PROP_LG_CXDLG = 252
    PROP_LG_CYDLG = 218