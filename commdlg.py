"""
*************************************************************************
*                                                                       *
*   commdlg.h -- This module defines the 32-Bit Common Dialog APIs      *
*                                                                       *
*   Copyright (c) Microsoft Corporation. All rights reserved.           *
*                                                                       *
*************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .wingdi import LPDEVMODE, DEVMODEW, DM_COPIES, DM_COLLATE, LPLOGFONTA, LPLOGFONTW

from .com.unknwn import *

from .winuser import SendMessage

if cpreproc.pragma_once("_INC_COMMDLG"):
    comdlg32 = W_WinDLL("comdlg32.dll")

    #
    #  IPrintDialogCallback interface id used by PrintDlgEx.
    #
    #  {5852A2C3-6530-11D1-B6A3-0000F8757BF9}
    #
    IID_IPrintDialogCallback = IID("{5852A2C3-6530-11D1-B6A3-0000F8757BF9}")

    #
    #  IPrintDialogServices interface id used by PrintDlgEx.
    #
    #  {509AAEDA-5639-11D1-B6A1-0000F8757BF9}
    #
    IID_IPrintDialogServices = IID("{509AAEDA-5639-11D1-B6A1-0000F8757BF9}")

    from .prsht import *

    LPOFNHOOKPROC = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)

    def CDSIZEOF_STRUCT(structname, member):
        return getattr(structname, member).offset + getattr(structname, member).size
    
    class tagOFN_NT4A(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hInstance", HINSTANCE),
            ("lpstrFilter", LPCSTR),
            ("lpstrCustomFilter", LPSTR),
            ("nMaxCustFilter", DWORD),
            ("nFilterIndex", DWORD),
            ("lpstrFile", LPSTR),
            ("nMaxFile", DWORD),
            ("lpstrFileTitle", LPSTR),
            ("nMaxFileTitle", DWORD),
            ("lpstrInitialDir", LPCSTR),
            ("lpstrTitle", LPCSTR),
            ("Flags", DWORD),
            ("nFileOffset", WORD),
            ("nFileExtension", WORD),
            ("lpstrDefExt", LPCSTR),
            ("lCustData", LPARAM),
            ("lpfnHook", LPOFNHOOKPROC),
            ("lpTemplateName", LPCSTR)
        ]
    OPENFILENAME_NT4A = tagOFN_NT4A
    LPOPENFILENAME_NT4A = POINTER(OPENFILENAME_NT4A)

    class tagOFN_NT4W(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hInstance", HINSTANCE),
            ("lpstrFilter", LPCWSTR),
            ("lpstrCustomFilter", LPWSTR),
            ("nMaxCustFilter", DWORD),
            ("nFilterIndex", DWORD),
            ("lpstrFile", LPWSTR),
            ("nMaxFile", DWORD),
            ("lpstrFileTitle", LPWSTR),
            ("nMaxFileTitle", DWORD),
            ("lpstrInitialDir", LPCWSTR),
            ("lpstrTitle", LPCWSTR),
            ("Flags", DWORD),
            ("nFileOffset", WORD),
            ("nFileExtension", WORD),
            ("lpstrDefExt", LPCWSTR),
            ("lCustData", LPARAM),
            ("lpfnHook", LPOFNHOOKPROC),
            ("lpTemplateName", LPCWSTR)
        ]
    OPENFILENAME_NT4W = tagOFN_NT4W
    LPOPENFILENAME_NT4W = POINTER(OPENFILENAME_NT4W)

    OPENFILENAME_NT4 = unicode(OPENFILENAME_NT4W, OPENFILENAME_NT4A)
    LPOPENFILENAME_NT4 = unicode(LPOPENFILENAME_NT4W, LPOPENFILENAME_NT4A)

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN2K:
        class tagOFNA(CStructure):
            _fields_ = [
                ("lStructSize", DWORD),
                ("hwndOwner", HWND),
                ("hInstance", HINSTANCE),
                ("lpstrFilter", LPCSTR),
                ("lpstrCustomFilter", LPSTR),
                ("nMaxCustFilter", DWORD),
                ("nFilterIndex", DWORD),
                ("lpstrFile", LPSTR),
                ("nMaxFile", DWORD),
                ("lpstrFileTitle", LPSTR),
                ("nMaxFileTitle", DWORD),
                ("lpstrInitialDir", LPCSTR),
                ("lpstrTitle", LPCSTR),
                ("Flags", DWORD),
                ("nFileOffset", WORD),
                ("nFileExtension", WORD),
                ("lpstrDefExt", LPCSTR),
                ("lCustData", LPARAM),
                ("lpfnHook", LPOFNHOOKPROC),
                ("lpTemplateName", LPCSTR),
                ("pvReserved", PVOID),
                ("dwReserved", DWORD),
                ("FlagsEx", DWORD)
            ]
        OPENFILENAMEA = tagOFNA
        LPOPENFILENAMEA = POINTER(OPENFILENAMEA)

        class tagOFNW(CStructure):
            _fields_ = [
                ("lStructSize", DWORD),
                ("hwndOwner", HWND),
                ("hInstance", HINSTANCE),
                ("lpstrFilter", LPCWSTR),
                ("lpstrCustomFilter", LPWSTR),
                ("nMaxCustFilter", DWORD),
                ("nFilterIndex", DWORD),
                ("lpstrFile", LPWSTR),
                ("nMaxFile", DWORD),
                ("lpstrFileTitle", LPWSTR),
                ("nMaxFileTitle", DWORD),
                ("lpstrInitialDir", LPCWSTR),
                ("lpstrTitle", LPCWSTR),
                ("Flags", DWORD),
                ("nFileOffset", WORD),
                ("nFileExtension", WORD),
                ("lpstrDefExt", LPCWSTR),
                ("lCustData", LPARAM),
                ("lpfnHook", LPOFNHOOKPROC),
                ("lpTemplateName", LPCWSTR),
                ("pvReserved", PVOID),
                ("dwReserved", DWORD),
                ("FlagsEx", DWORD)
            ]
        OPENFILENAMEW = tagOFNW
        LPOPENFILENAMEW = POINTER(OPENFILENAMEW)
        OPENFILENAME_SIZE_VERSION_400A = CDSIZEOF_STRUCT(OPENFILENAMEA, "lpTemplateName")
        OPENFILENAME_SIZE_VERSION_400W = CDSIZEOF_STRUCT(OPENFILENAMEW, "lpTemplateName")
    else:
        tagOFNA = OPENFILENAME_NT4A
        tagOFNW = OPENFILENAME_NT4W
        OPENFILENAMEA = OPENFILENAME_NT4A
        OPENFILENAMEW = OPENFILENAME_NT4W
        LPOPENFILENAMEW = LPOPENFILENAME_NT4W
        LPOPENFILENAMEA = LPOPENFILENAME_NT4A
    OPENFILENAME = unicode(OPENFILENAMEW, OPENFILENAMEA)
    LPOPENFILENAME = unicode(LPOPENFILENAMEW, LPOPENFILENAMEA)

    GetOpenFileNameA = declare(comdlg32.GetOpenFileNameA, BOOL, LPOPENFILENAMEA)
    GetOpenFileNameW = declare(comdlg32.GetOpenFileNameW, BOOL, LPOPENFILENAMEW)
    GetOpenFileName = unicode(GetOpenFileNameW, GetOpenFileNameA)
    
    GetSaveFileNameA = declare(comdlg32.GetSaveFileNameA, BOOL, LPOPENFILENAMEA)
    GetSaveFileNameW = declare(comdlg32.GetSaveFileNameW, BOOL, LPOPENFILENAMEW)
    GetSaveFileName = unicode(GetSaveFileNameW, GetSaveFileNameA)
    
    GetFileTitleA = declare(comdlg32.GetFileTitleA, SHORT, LPCSTR, LPSTR, WORD)
    GetFileTitleW = declare(comdlg32.GetFileTitleW, SHORT, LPCWSTR, LPWSTR, WORD)
    GetFileTitle = unicode(GetFileTitleW, GetFileTitleA)

    OFN_READONLY = 0x00000001
    OFN_OVERWRITEPROMPT = 0x00000002
    OFN_HIDEREADONLY = 0x00000004
    OFN_NOCHANGEDIR = 0x00000008
    OFN_SHOWHELP = 0x00000010
    OFN_ENABLEHOOK = 0x00000020
    OFN_ENABLETEMPLATE = 0x00000040
    OFN_ENABLETEMPLATEHANDLE = 0x00000080
    OFN_NOVALIDATE = 0x00000100
    OFN_ALLOWMULTISELECT = 0x00000200
    OFN_EXTENSIONDIFFERENT = 0x00000400
    OFN_PATHMUSTEXIST = 0x00000800
    OFN_FILEMUSTEXIST = 0x00001000
    OFN_CREATEPROMPT = 0x00002000
    OFN_SHAREAWARE = 0x00004000
    OFN_NOREADONLYRETURN = 0x00008000
    OFN_NOTESTFILECREATE = 0x00010000
    OFN_NONETWORKBUTTON = 0x00020000
    OFN_NOLONGNAMES = 0x00040000 # force no long names for 4.x modules
    OFN_EXPLORER = 0x00080000 # new look commdlg
    OFN_NODEREFERENCELINKS = 0x00100000
    OFN_LONGNAMES = 0x00200000 # force long names for 3.x modules
    # OFN_ENABLEINCLUDENOTIFY and OFN_ENABLESIZING require
    # Windows 2000 or higher to have any effect.
    OFN_ENABLEINCLUDENOTIFY = 0x00400000 # send include message to callback
    OFN_ENABLESIZING = 0x00800000
    OFN_DONTADDTORECENT = 0x02000000
    OFN_FORCESHOWHIDDEN = 0x10000000 # Show All files including System and hidden files
    #FlagsEx Values
    OFN_EX_NOPLACESBAR = 0x00000001
    # Return values for the registered message sent to the hook function
    # when a sharing violation occurs.  OFN_SHAREFALLTHROUGH allows the
    # filename to be accepted, OFN_SHARENOWARN rejects the name but puts
    # up no warning (returned when the app has already put up a warning
    # message), and OFN_SHAREWARN puts up the default warning message
    # for sharing violations.
    #
    # Note:  Undefined return values map to OFN_SHAREWARN, but are
    #        reserved for future use.
    OFN_SHAREFALLTHROUGH = 2
    OFN_SHARENOWARN = 1
    OFN_SHAREWARN = 0
    
    LPCCHOOKPROC = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)

    # Structure used for all file based OpenFileName notifications
    class _OFNOTIFYA(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("lpOFN", LPOPENFILENAMEA),
            ("pszFile", LPSTR) # May be NULL     
        ]
    OFNOTIFYA = _OFNOTIFYA
    LPOFNOTIFYA = POINTER(OFNOTIFYA)

    # Structure used for all file based OpenFileName notifications
    class _OFNOTIFYW(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("lpOFN", LPOPENFILENAMEA),
            ("pszFile", LPSTR) # May be NULL     
        ]
    OFNOTIFYW = _OFNOTIFYW
    LPOFNOTIFYW = POINTER(OFNOTIFYW)

    OFNOTIFY = unicode(OFNOTIFYW, OFNOTIFYA)
    LPOFNOTIFY = unicode(LPOFNOTIFYW, LPOFNOTIFYA)

    # Structure used for all object based OpenFileName notifications
    class _OFNOTIFYEXA(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("lpOFN", LPOPENFILENAMEA),
            ("psf", LPVOID),
            ("pidl", LPVOID) # May be NULL
        ]
    OFNOTIFYEXA = _OFNOTIFYEXA
    LPOFNOTIFYEXA = POINTER(OFNOTIFYEXA)

    # Structure used for all object based OpenFileName notifications
    class _OFNOTIFYEXW(CStructure):
        _fields_ = [
            ("hdr", NMHDR),
            ("lpOFN", LPOPENFILENAMEW),
            ("psf", LPVOID),
            ("pidl", LPVOID) # May be NULL
        ]
    OFNOTIFYEXW = _OFNOTIFYEXW
    LPOFNOTIFYEXW = POINTER(OFNOTIFYEXW)

    OFNOTIFYEX = unicode(OFNOTIFYEXW, OFNOTIFYEXA)
    LPOFNOTIFYEX = unicode(LPOFNOTIFYEXW, LPOFNOTIFYEXA)

    CDN_FIRST = (0-601)
    CDN_LAST = (0-699)
    # Notifications from Open or Save dialog
    CDN_INITDONE = (CDN_FIRST - 0x0000)
    CDN_SELCHANGE = (CDN_FIRST - 0x0001)
    CDN_FOLDERCHANGE = (CDN_FIRST - 0x0002)
    CDN_SHAREVIOLATION = (CDN_FIRST - 0x0003)
    CDN_HELP = (CDN_FIRST - 0x0004)
    CDN_FILEOK = (CDN_FIRST - 0x0005)
    CDN_TYPECHANGE = (CDN_FIRST - 0x0006)
    CDN_INCLUDEITEM = (CDN_FIRST - 0x0007)
    CDM_FIRST = (WM_USER + 100)
    CDM_LAST = (WM_USER + 200)
    # Messages to query information from the Open or Save dialogs
    # lParam = pointer to text buffer that gets filled in
    # wParam = max number of characters of the text buffer (including NULL)
    # return = < 0 if error; number of characters needed (including NULL)
    CDM_GETSPEC = (CDM_FIRST + 0x0000)

    def CommDlg_OpenSave_GetSpecA(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETSPEC, _cbmax, cast(cast(_psz, LPSTR), PVOID).value)
    
    def CommDlg_OpenSave_GetSpecW(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETSPEC, _cbmax, cast(cast(_psz, LPWSTR), PVOID).value)
    
    CommDlg_OpenSave_GetSpec = unicode(CommDlg_OpenSave_GetSpecW, CommDlg_OpenSave_GetSpecA)

    # lParam = pointer to text buffer that gets filled in
    # wParam = max number of characters of the text buffer (including NULL)
    # return = < 0 if error; number of characters needed (including NULL)
    CDM_GETFILEPATH = (CDM_FIRST + 0x0001)

    def CommDlg_OpenSave_GetFilePathA(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETFILEPATH, _cbmax, cast(cast(_psz, LPSTR), PVOID).value)
    
    def CommDlg_OpenSave_GetFilePathW(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETFILEPATH, _cbmax, cast(cast(_psz, LPWSTR), PVOID).value)
    
    CommDlg_OpenSave_GetFilePath = unicode(CommDlg_OpenSave_GetFilePathW, CommDlg_OpenSave_GetFilePathA)

    # lParam = pointer to text buffer that gets filled in
    # wParam = max number of characters of the text buffer (including NULL)
    # return = < 0 if error; number of characters needed (including NULL)
    CDM_GETFOLDERPATH = (CDM_FIRST + 0x0002)

    def CommDlg_OpenSave_GetFolderPathA(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETFOLDERPATH, _cbmax, cast(cast(_psz, LPSTR), PVOID).value)
    
    def CommDlg_OpenSave_GetFolderPathW(_hdlg, _psz, _cbmax):
        return SendMessage(_hdlg, CDM_GETFOLDERPATH, _cbmax, cast(cast(_psz, LPWSTR), PVOID).value)
    
    CommDlg_OpenSave_GetFolderPath = unicode(CommDlg_OpenSave_GetFolderPathW, CommDlg_OpenSave_GetFolderPathA)

    # lParam = pointer to ITEMIDLIST buffer that gets filled in
    # wParam = size of the ITEMIDLIST buffer
    # return = < 0 if error; length of buffer needed
    CDM_GETFOLDERIDLIST = (CDM_FIRST + 0x0003)

    def CommDlg_OpenSave_GetFolderIDList(_hdlg, _pidl, _cbmax):
        return SendMessage(_hdlg, CDM_GETFOLDERIDLIST , _cbmax, cast(cast(_pidl, LPVOID), PVOID).value)

    # lParam = pointer to a string
    # wParam = ID of control to change
    # return = not used
    CDM_SETCONTROLTEXT = (CDM_FIRST + 0x0004)

    def CommDlg_OpenSave_SetControlText(_hdlg, _id, _text):
        return SendMessage(_hdlg, CDM_SETCONTROLTEXT, _id, cast(cast(_text, LPSTR), PVOID).value)

    # lParam = not used
    # wParam = ID of control to change
    # return = not used
    CDM_HIDECONTROL = (CDM_FIRST + 0x0005)

    def CommDlg_OpenSave_HideControl(_hdlg, _id):
        return SendMessage(_hdlg, CDM_HIDECONTROL, _id, 0)

    # lParam = pointer to default extension (no dot)
    # wParam = not used
    # return = not used
    CDM_SETDEFEXT = (CDM_FIRST + 0x0006)

    def CommDlg_OpenSave_SetDefExt(_hdlg, _psztext):
        return SendMessage(_hdlg, CDM_SETDEFEXT, 0, cast(cast(_psztext, LPSTR), PVOID).value)
    
    class tagCHOOSECOLORA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hInstance", HWND),
            ("rgbResult", COLORREF),
            ("lpCustColors", LPCOLORREF),
            ("Flags", DWORD),
            ("lCustData", LPARAM),
            ("lpfnHook", LPCCHOOKPROC),
            ("lpTemplateName", LPCSTR)
        ]
    CHOOSECOLORA = tagCHOOSECOLORA
    LPCHOOSECOLORA = POINTER(CHOOSECOLORA)

    class tagCHOOSECOLORW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hInstance", HWND),
            ("rgbResult", COLORREF),
            ("lpCustColors", LPCOLORREF),
            ("Flags", DWORD),
            ("lCustData", LPARAM),
            ("lpfnHook", LPCCHOOKPROC),
            ("lpTemplateName", LPCWSTR)
        ]
    CHOOSECOLORW = tagCHOOSECOLORW
    LPCHOOSECOLORW = POINTER(CHOOSECOLORW)

    CHOOSECOLOR = unicode(CHOOSECOLORW, CHOOSECOLORA)
    LPCHOOSECOLOR = unicode(LPCHOOSECOLORW, LPCHOOSECOLORA)

    ChooseColorA = declare(comdlg32.ChooseColorA, BOOL, LPCHOOSECOLORA)
    ChooseColorW = declare(comdlg32.ChooseColorW, BOOL, LPCHOOSECOLORW)
    ChooseColor = unicode(ChooseColorW, ChooseColorA)

    CC_RGBINIT = 0x00000001
    CC_FULLOPEN = 0x00000002
    CC_PREVENTFULLOPEN = 0x00000004
    CC_SHOWHELP = 0x00000008
    CC_ENABLEHOOK = 0x00000010
    CC_ENABLETEMPLATE = 0x00000020
    CC_ENABLETEMPLATEHANDLE = 0x00000040
    CC_SOLIDCOLOR = 0x00000080
    CC_ANYCOLOR = 0x00000100

    LPFRHOOKPROC = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)

    class tagFINDREPLACEA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD), # size of this struct 0x20
            ("hwndOwner", HWND), # handle to owner's window
            ("hInstance", HINSTANCE), # instance handle of.EXE that
                                      #   contains cust. dlg. template
            ("Flags", DWORD), # one or more of the FR_??
            ("lpstrFindWhat", LPSTR), # ptr. to search string
            ("lpstrReplaceWith", LPSTR), # ptr. to replace string
            ("wFindWhatLen", WORD), # size of find buffer
            ("wReplaceWithLen", WORD), # size of replace buffer
            ("lCustData", LPARAM), # data passed to hook fn.
            ("lpfnHook", LPFRHOOKPROC), # ptr. to hook fn. or NULL
            ("lpTemplateName", LPCSTR) # custom template name
        ]
    FINDREPLACEA = tagFINDREPLACEA
    LPFINDREPLACEA = POINTER(FINDREPLACEA)

    class tagFINDREPLACEW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD), # size of this struct 0x20
            ("hwndOwner", HWND), # handle to owner's window
            ("hInstance", HINSTANCE), # instance handle of.EXE that
                                      #   contains cust. dlg. template
            ("Flags", DWORD), # one or more of the FR_??
            ("lpstrFindWhat", LPWSTR), # ptr. to search string
            ("lpstrReplaceWith", LPWSTR), # ptr. to replace string
            ("wFindWhatLen", WORD), # size of find buffer
            ("wReplaceWithLen", WORD), # size of replace buffer
            ("lCustData", LPARAM), # data passed to hook fn.
            ("lpfnHook", LPFRHOOKPROC), # ptr. to hook fn. or NULL
            ("lpTemplateName", LPCSTR) # custom template name
        ]
    FINDREPLACEW = tagFINDREPLACEW
    LPFINDREPLACEW = POINTER(FINDREPLACEW)

    FINDREPLACE = unicode(FINDREPLACEW, FINDREPLACEA)
    LPFINDREPLACE = unicode(LPFINDREPLACEW, LPFINDREPLACEA)
    
    FR_DOWN = 0x00000001
    FR_WHOLEWORD = 0x00000002
    FR_MATCHCASE = 0x00000004
    FR_FINDNEXT = 0x00000008
    FR_REPLACE = 0x00000010
    FR_REPLACEALL = 0x00000020
    FR_DIALOGTERM = 0x00000040
    FR_SHOWHELP = 0x00000080
    FR_ENABLEHOOK = 0x00000100
    FR_ENABLETEMPLATE = 0x00000200
    FR_NOUPDOWN = 0x00000400
    FR_NOMATCHCASE = 0x00000800
    FR_NOWHOLEWORD = 0x00001000
    FR_ENABLETEMPLATEHANDLE = 0x00002000
    FR_HIDEUPDOWN = 0x00004000
    FR_HIDEMATCHCASE = 0x00008000
    FR_HIDEWHOLEWORD = 0x00010000
    FR_RAW = 0x00020000
    FR_SHOWWRAPAROUND = 0x00040000
    FR_NOWRAPAROUND = 0x00080000
    FR_WRAPAROUND = 0x00100000
    FR_MATCHDIAC = 0x20000000
    FR_MATCHKASHIDA = 0x40000000
    FR_MATCHALEFHAMZA = 0x80000000
    
    FindTextA = declare(comdlg32.FindTextA, HWND, LPFINDREPLACEA)
    FindTextW = declare(comdlg32.FindTextW, HWND, LPFINDREPLACEW)
    FindText = unicode(FindTextW, FindTextA)
    
    ReplaceTextA = declare(comdlg32.ReplaceTextA, HWND, LPFINDREPLACEA)
    ReplaceTextW = declare(comdlg32.ReplaceTextW, HWND, LPFINDREPLACEW)
    
    if cpreproc.ifndef("_MAC"):
        ReplaceText = unicode(ReplaceTextW, ReplaceTextA)
    else:
        AfxReplaceTextA = declare(comdlg32.AfxReplaceTextA, HWND, LPFINDREPLACEA)
        AfxReplaceTextW = declare(comdlg32.AfxReplaceTextW, HWND, LPFINDREPLACEW)
        AfxReplaceText = unicode(AfxReplaceTextW, AfxReplaceTextA)
        
    FRM_FIRST = (WM_USER + 100)
    FRM_LAST = (WM_USER + 200)
    
    # Messages to notify the Find or Replace dialogs of the result of a find or replace operation
    # for accessibility purposes
    # lParam = pointer to the FINDREPLACE structure that was sent to the client to begin the operation
    # wParam = FR_* flags indicating which operations were completed
    # return = not used
    FRM_SETOPERATIONRESULT = (FRM_FIRST + 0x0000)
    def CommDlg_FindReplace_SendResult(_hdlg, _flags, _fr):
        SendMessage(_hdlg, FRM_SETOPERATIONRESULT, _flags, cast(_fr, PVOID).value)

    # lParam = pointer to a string to be used to communicate the result of an operation to a user
    # wParam = not used
    # return = not used
    FRM_SETOPERATIONRESULTTEXT = (FRM_FIRST + 0x0001)
    def CommDlg_FindReplace_SendCustomResult(_hdlg, _psz):
        SendMessage(_hdlg, FRM_SETOPERATIONRESULTTEXT, 0, cast(_psz, PVOID).value)
        
    LPCFHOOKPROC = CALLBACK(INT_PTR, HWND, UINT, WPARAM, LPARAM)

    class tagCHOOSEFONTA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),                # caller's window handle
            ("hDC", HDC),                       # printer DC/IC or NULL
            ("lpLogFont", LPLOGFONTA),          # ptr. to a LOGFONT struct
            ("iPointSize", INT),                # 10 * size in points of selected font
            ("Flags", DWORD),                   # enum. type flags
            ("rgbColors", COLORREF),            # returned text color
            ("lCustData", LPARAM),              # data passed to hook fn.
            ("lpfnHook", LPCFHOOKPROC),         # ptr. to hook function
            ("lpTemplateName", LPCSTR),         # custom template name
            ("hInstance", HINSTANCE),           # instance handle of.EXE that
                                                #   contains cust. dlg. template
            ("lpszStyle", LPSTR),               # return the style field here
                                                # must be LF_FACESIZE or bigger
            ("nFontType", WORD),                # same value reported to the EnumFonts
                                                #   call back with the extra FONTTYPE_
                                                #   bits added
            ("___MISSING_ALIGNMENT__", WORD),
            ("nSizeMin", INT),                  # minimum pt size allowed &
            ("nSizeMax", INT),                  # max pt size allowed if
                                                #   CF_LIMITSIZE is used
        ]
    CHOOSEFONTA = tagCHOOSEFONTA
    
    class tagCHOOSEFONTW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),                # caller's window handle
            ("hDC", HDC),                       # printer DC/IC or NULL
            ("lpLogFont", LPLOGFONTW),          # ptr. to a LOGFONT struct
            ("iPointSize", INT),                # 10 * size in points of selected font
            ("Flags", DWORD),                   # enum. type flags
            ("rgbColors", COLORREF),            # returned text color
            ("lCustData", LPARAM),              # data passed to hook fn.
            ("lpfnHook", LPCFHOOKPROC),         # ptr. to hook function
            ("lpTemplateName", LPCWSTR),        # custom template name
            ("hInstance", HINSTANCE),           # instance handle of.EXE that
                                                #   contains cust. dlg. template
            ("lpszStyle", LPWSTR),              # return the style field here
                                                # must be LF_FACESIZE or bigger
            ("nFontType", WORD),                # same value reported to the EnumFonts
                                                #   call back with the extra FONTTYPE_
                                                #   bits added
            ("___MISSING_ALIGNMENT__", WORD),
            ("nSizeMin", INT),                  # minimum pt size allowed &
            ("nSizeMax", INT),                  # max pt size allowed if
                                                #   CF_LIMITSIZE is used
        ]
    CHOOSEFONTW = tagCHOOSEFONTW
    
    CHOOSEFONT = unicode(CHOOSEFONTW, CHOOSEFONTA)
    LPCHOOSEFONTA = PCCHOOSEFONTA = POINTER(CHOOSEFONTA)
    LPCHOOSEFONTW = PCCHOOSEFONTW = POINTER(CHOOSEFONTW)
    LPCHOOSEFONT = PCCHOOSEFONT = unicode(LPCHOOSEFONTW, LPCHOOSEFONTA)
    
    ChooseFontA = declare(comdlg32.ChooseFontA, BOOL, LPCHOOSEFONTA)
    ChooseFontW = declare(comdlg32.ChooseFontW, BOOL, LPCHOOSEFONTW)
    ChooseFont = unicode(ChooseFontW, ChooseFontA)
    
    CF_SCREENFONTS = 0x00000001
    CF_PRINTERFONTS = 0x00000002
    CF_BOTH = (CF_SCREENFONTS | CF_PRINTERFONTS)
    CF_SHOWHELP = 0x00000004
    CF_ENABLEHOOK = 0x00000008
    CF_ENABLETEMPLATE = 0x00000010
    CF_ENABLETEMPLATEHANDLE = 0x00000020
    CF_INITTOLOGFONTSTRUCT = 0x00000040
    CF_USESTYLE = 0x00000080
    CF_EFFECTS = 0x00000100
    CF_APPLY = 0x00000200
    CF_ANSIONLY = 0x00000400
    CF_SCRIPTSONLY = CF_ANSIONLY
    CF_NOVECTORFONTS = 0x00000800
    CF_NOOEMFONTS = CF_NOVECTORFONTS
    CF_NOSIMULATIONS = 0x00001000
    CF_LIMITSIZE = 0x00002000
    CF_FIXEDPITCHONLY = 0x00004000
    CF_WYSIWYG = 0x00008000 # must also have CF_SCREENFONTS & CF_PRINTERFONTS
    CF_FORCEFONTEXIST = 0x00010000
    CF_SCALABLEONLY = 0x00020000
    CF_TTONLY = 0x00040000
    CF_NOFACESEL = 0x00080000
    CF_NOSTYLESEL = 0x00100000
    CF_NOSIZESEL = 0x00200000
    CF_SELECTSCRIPT = 0x00400000
    CF_NOSCRIPTSEL = 0x00800000
    CF_NOVERTFONTS = 0x01000000
    CF_INACTIVEFONTS = 0x02000000
    # these are extra nFontType bits that are added to what is returned to the
    # EnumFonts callback routine
    SIMULATED_FONTTYPE = 0x8000
    PRINTER_FONTTYPE = 0x4000
    SCREEN_FONTTYPE = 0x2000
    BOLD_FONTTYPE = 0x0100
    ITALIC_FONTTYPE = 0x0200
    REGULAR_FONTTYPE = 0x0400
    # EnumFonts callback routine only uses these bits, so we can use the rest
    # #define RASTER_FONTTYPE     0x001
    # #define DEVICE_FONTTYPE     0x002
    # #define TRUETYPE_FONTTYPE   0x004
    PS_OPENTYPE_FONTTYPE = 0x10000
    TT_OPENTYPE_FONTTYPE = 0x20000
    TYPE1_FONTTYPE = 0x40000
    SYMBOL_FONTTYPE = 0x80000
    WM_CHOOSEFONT_GETLOGFONT = (WM_USER + 1)
    WM_CHOOSEFONT_SETLOGFONT = (WM_USER + 101)
    WM_CHOOSEFONT_SETFLAGS = (WM_USER + 102)
    # strings used to obtain unique window message for communication
    # between dialog and caller
    LBSELCHSTRINGA = b"commdlg_LBSelChangedNotify"
    SHAREVISTRINGA = b"commdlg_ShareViolation"
    FILEOKSTRINGA = b"commdlg_FileNameOK"
    COLOROKSTRINGA = b"commdlg_ColorOK"
    SETRGBSTRINGA = b"commdlg_SetRGBColor"
    HELPMSGSTRINGA = b"commdlg_help"
    FINDMSGSTRINGA = b"commdlg_FindReplace"
    LBSELCHSTRINGW = u"commdlg_LBSelChangedNotify"
    SHAREVISTRINGW = u"commdlg_ShareViolation"
    FILEOKSTRINGW = u"commdlg_FileNameOK"
    COLOROKSTRINGW = u"commdlg_ColorOK"
    SETRGBSTRINGW = u"commdlg_SetRGBColor"
    HELPMSGSTRINGW = u"commdlg_help"
    FINDMSGSTRINGW = u"commdlg_FindReplace"
    LBSELCHSTRING = unicode(LBSELCHSTRINGW, LBSELCHSTRINGA)
    SHAREVISTRING = unicode(SHAREVISTRINGW, SHAREVISTRINGA)
    FILEOKSTRING = unicode(FILEOKSTRINGW, FILEOKSTRINGA)
    COLOROKSTRING = unicode(COLOROKSTRINGW, COLOROKSTRINGA)
    SETRGBSTRING = unicode(SETRGBSTRINGW, SETRGBSTRINGA)
    HELPMSGSTRING = unicode(HELPMSGSTRINGW, HELPMSGSTRINGA)
    FINDMSGSTRING = unicode(FINDMSGSTRINGW, FINDMSGSTRINGA)
    # HIWORD values for lParam of commdlg_LBSelChangeNotify message
    CD_LBSELNOITEMS = -1
    CD_LBSELCHANGE = 0
    CD_LBSELSUB = 1
    CD_LBSELADD = 2
    
    LPPRINTHOOKPROC = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)
    LPSETUPHOOKPROC = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)

    class tagPDA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hDevMode", HGLOBAL),
            ("hDevNames", HGLOBAL),
            ("hDC", HDC),
            ("Flags", DWORD),
            ("nFromPage", WORD),
            ("nToPage", WORD),
            ("nMinPage", WORD),
            ("nMaxPage", WORD),
            ("nCopies", WORD),
            ("hInstance", HINSTANCE),
            ("lCustData", LPARAM),
            ("lpfnPrintHook", LPPRINTHOOKPROC),
            ("lpfnSetupHook", LPSETUPHOOKPROC),
            ("lpPrintTemplateName", LPCSTR),
            ("lpSetupTemplateName", LPCSTR),
            ("hPrintTemplate", HGLOBAL),
            ("hSetupTemplate", HGLOBAL)
        ]
    PRINTDLGA = tagPDA
    LPPRINTDLGA = POINTER(PRINTDLGA)
    
    class tagPDW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hDevMode", HGLOBAL),
            ("hDevNames", HGLOBAL),
            ("hDC", HDC),
            ("Flags", DWORD),
            ("nFromPage", WORD),
            ("nToPage", WORD),
            ("nMinPage", WORD),
            ("nMaxPage", WORD),
            ("nCopies", WORD),
            ("hInstance", HINSTANCE),
            ("lCustData", LPARAM),
            ("lpfnPrintHook", LPPRINTHOOKPROC),
            ("lpfnSetupHook", LPSETUPHOOKPROC),
            ("lpPrintTemplateName", LPCWSTR),
            ("lpSetupTemplateName", LPCWSTR),
            ("hPrintTemplate", HGLOBAL),
            ("hSetupTemplate", HGLOBAL)
        ]
    PRINTDLGW = tagPDW
    LPPRINTDLGW = POINTER(PRINTDLGW)
    
    PRINTDLG = unicode(PRINTDLGW, PRINTDLGA)
    LPPRINTDLG = unicode(LPPRINTDLGW, LPPRINTDLGA)

    PrintDlgA = declare(comdlg32.PrintDlgA, BOOL, LPPRINTDLGA)
    PrintDlgW = declare(comdlg32.PrintDlgW, BOOL, LPPRINTDLGW)
    PrintDlg = unicode(PrintDlgW, PrintDlgA)

    #-------------------------------------------------------------------------
    #
    #  IPrintDialogCallback Interface
    #
    #  IPrintDialogCallback::InitDone()
    #    This function is called by PrintDlgEx when the system has finished
    #    initializing the main page of the print dialog.  This function
    #    should return S_OK if it has processed the action or S_FALSE to let
    #    PrintDlgEx perform the default action.
    #
    #  IPrintDialogCallback::SelectionChange()
    #    This function is called by PrintDlgEx when a selection change occurs
    #    in the list view that displays the currently installed printers.
    #    This function should return S_OK if it has processed the action or
    #    S_FALSE to let PrintDlgEx perform the default action.
    #
    #  IPrintDialogCallback::HandleMessage(hDlg, uMsg, wParam, lParam, pResult)
    #    This function is called by PrintDlgEx when a message is sent to the
    #    child window of the main page of the print dialog.  This function
    #    should return S_OK if it has processed the action or S_FALSE to let
    #    PrintDlgEx perform the default action.
    #
    #  IObjectWithSite::SetSite(punkSite)
    #    IPrintDialogCallback usually paired with IObjectWithSite.
    #    Provides the IUnknown pointer of the site to QI for the
    #    IPrintDialogServices interface.
    #
    #-------------------------------------------------------------------------
    class IPrintDialogCallback(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID_IPrintDialogCallback
        
        @virtual_table.com_function()
        def InitDone(self) -> int: ...
        
        @virtual_table.com_function()
        def SelectionChange(self) -> int: ...
        
        @virtual_table.com_function(HWND, UINT, WPARAM, LPARAM, LRESULT)
        def HandleMessage(self, hDlg: WT_HANDLE, uMsg: int, wParam: int, lParam: int, pResult: int) -> int: ...
        
        virtual_table.build()

    #-------------------------------------------------------------------------
    #
    #  IPrintDialogServices Interface
    #
    #  IPrintDialogServices::GetCurrentDevMode(pDevMode, pcbSize)
    #    Returns the DEVMODE structure for the currently selected printer.
    #
    #  IPrintDialogServices::GetCurrentPrinterName(pPrinterName, pcchSize)
    #    Returns the printer name for the currently selected printer.
    #
    #  IPrintDialogServices::GetCurrentPortName(pPortName, pcchSize)
    #    Returns the port name for the currently selected printer.
    #
    #-------------------------------------------------------------------------
    
    class IPrintDialogServices(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID_IPrintDialogServices
        
        @virtual_table.com_function(LPDEVMODE, PUINT)
        def GetCurrentDevMode(self, pDevMode: IPointer[DEVMODEW], pcbSize: PUINT) -> int: ...
        
        @virtual_table.com_function(LPWSTR, PUINT)
        def GetCurrentPrinterName(self, pPrinterName: WT_LPWSTR, pcchSize: PUINT) -> int: ...
        
        @virtual_table.com_function(LPWSTR, PUINT)
        def GetCurrentPortName(self, pPortName: WT_LPWSTR, pcchSize: PUINT) -> int: ...
        
        virtual_table.build()

    #
    #  Page Range structure for PrintDlgEx.
    #
    class tagPRINTPAGERANGE(CStructure):
        _fields_ = [
            ("nFromPage", DWORD),
            ("nToPage", DWORD)
        ]
    PRINTPAGERANGE = tagPRINTPAGERANGE
    LPPRINTPAGERANGE = POINTER(PRINTPAGERANGE)
    PCPRINTPAGERANGE = LPPRINTPAGERANGE

    #
    #  PrintDlgEx structure.
    #
    class tagPDEXA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD), # size of structure in bytes
            ("hwndOwner", HWND), # caller's window handle
            ("hDevMode", HGLOBAL), # handle to DevMode
            ("hDevNames", HGLOBAL), # handle to DevNames
            ("hDC", HDC), # printer DC/IC or NULL
            ("Flags", DWORD), # PD_ flags
            ("Flags2", DWORD), # reserved
            ("ExclusionFlags", DWORD), # items to exclude from driver pages
            ("nPageRanges", DWORD), # number of page ranges
            ("nMaxPageRanges", DWORD), # max number of page ranges
            ("lpPageRanges", LPPRINTPAGERANGE), # array of page ranges
            ("nMinPage", DWORD), # min page number
            ("nMaxPage", DWORD), # max page number
            ("nCopies", DWORD), # number of copies
            ("hInstance", HINSTANCE), # instance handle
            ("lpPrintTemplateName", LPCSTR), # template name for app specific area
            ("lpCallback", POINTER(IUnknown)), # app callback interface
            ("nPropertyPages", DWORD), # number of app property pages in lphPropertyPages
            ("lphPropertyPages", HPROPSHEETPAGE), # array of app property page handles
            ("nStartPage", DWORD), # start page id
            ("dwResultAction", DWORD) # result action if S_OK is returned
        ]
    PRINTDLGEXA = tagPDEXA
    LPPRINTDLGEXA = POINTER(PRINTDLGEXA)

    #
    #  PrintDlgEx structure.
    #
    class tagPDEXW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD), # size of structure in bytes
            ("hwndOwner", HWND), # caller's window handle
            ("hDevMode", HGLOBAL), # handle to DevMode
            ("hDevNames", HGLOBAL), # handle to DevNames
            ("hDC", HDC), # printer DC/IC or NULL
            ("Flags", DWORD), # PD_ flags
            ("Flags2", DWORD), # reserved
            ("ExclusionFlags", DWORD), # items to exclude from driver pages
            ("nPageRanges", DWORD), # number of page ranges
            ("nMaxPageRanges", DWORD), # max number of page ranges
            ("lpPageRanges", LPPRINTPAGERANGE), # array of page ranges
            ("nMinPage", DWORD), # min page number
            ("nMaxPage", DWORD), # max page number
            ("nCopies", DWORD), # number of copies
            ("hInstance", HINSTANCE), # instance handle
            ("lpPrintTemplateName", LPCWSTR), # template name for app specific area
            ("lpCallback", POINTER(IUnknown)), # app callback interface
            ("nPropertyPages", DWORD), # number of app property pages in lphPropertyPages
            ("lphPropertyPages", HPROPSHEETPAGE), # array of app property page handles
            ("nStartPage", DWORD), # start page id
            ("dwResultAction", DWORD) # result action if S_OK is returned
        ]
    PRINTDLGEXW = tagPDEXW
    LPPRINTDLGEXW = POINTER(PRINTDLGEXW)

    PRINTDLGEX = unicode(PRINTDLGEXW, PRINTDLGEXA)
    LPPRINTDLGEX = unicode(LPPRINTDLGEXW, LPPRINTDLGEXA)

    PrintDlgExA = declare(comdlg32.PrintDlgExA, HRESULT, LPPRINTDLGEXA)
    PrintDlgExW = declare(comdlg32.PrintDlgExW, HRESULT, LPPRINTDLGEXW)
    PrintDlgEx = unicode(PrintDlgExW, PrintDlgExA)

    #
    #  Flags for PrintDlg and PrintDlgEx.
    #
    PD_ALLPAGES = 0x00000000
    PD_SELECTION = 0x00000001
    PD_PAGENUMS = 0x00000002
    PD_NOSELECTION = 0x00000004
    PD_NOPAGENUMS = 0x00000008
    PD_COLLATE = 0x00000010
    PD_PRINTTOFILE = 0x00000020
    PD_PRINTSETUP = 0x00000040
    PD_NOWARNING = 0x00000080
    PD_RETURNDC = 0x00000100
    PD_RETURNIC = 0x00000200
    PD_RETURNDEFAULT = 0x00000400
    PD_SHOWHELP = 0x00000800
    PD_ENABLEPRINTHOOK = 0x00001000
    PD_ENABLESETUPHOOK = 0x00002000
    PD_ENABLEPRINTTEMPLATE = 0x00004000
    PD_ENABLESETUPTEMPLATE = 0x00008000
    PD_ENABLEPRINTTEMPLATEHANDLE = 0x00010000
    PD_ENABLESETUPTEMPLATEHANDLE = 0x00020000
    PD_USEDEVMODECOPIES = 0x00040000
    PD_USEDEVMODECOPIESANDCOLLATE = 0x00040000
    PD_DISABLEPRINTTOFILE = 0x00080000
    PD_HIDEPRINTTOFILE = 0x00100000
    PD_NONETWORKBUTTON = 0x00200000
    PD_CURRENTPAGE = 0x00400000
    PD_NOCURRENTPAGE = 0x00800000
    PD_EXCLUSIONFLAGS = 0x01000000
    PD_USELARGETEMPLATE = 0x10000000
    #
    #  Exclusion flags for PrintDlgEx.
    #
    PD_EXCL_COPIESANDCOLLATE = (DM_COPIES | DM_COLLATE)
    #
    #  Define the start page for the print dialog when using PrintDlgEx.
    #
    START_PAGE_GENERAL = 0xffffffff
    #
    #  Result action ids for PrintDlgEx.
    #
    PD_RESULT_CANCEL = 0
    PD_RESULT_PRINT = 1
    PD_RESULT_APPLY = 2
    #
    #  Device Names structure for PrintDlg and PrintDlgEx.
    #
    class tagDEVNAMES(CStructure):
        _fields_ = [
            ("wDriverOffset", WORD),
            ("wDeviceOffset", WORD),
            ("wOutputOffset", WORD),
            ("wDefault", WORD)
        ]
    DEVNAMES = tagDEVNAMES
    LPDEVNAMES = POINTER(DEVNAMES)
    PCDEVNAMES = LPDEVNAMES

    DN_DEFAULTPRN = 0x0001

    CommDlgExtendedError = declare(comdlg32.CommDlgExtendedError, DWORD, VOID)

    WM_PSD_PAGESETUPDLG = (WM_USER  )
    WM_PSD_FULLPAGERECT = (WM_USER+1)
    WM_PSD_MINMARGINRECT = (WM_USER+2)
    WM_PSD_MARGINRECT = (WM_USER+3)
    WM_PSD_GREEKTEXTRECT = (WM_USER+4)
    WM_PSD_ENVSTAMPRECT = (WM_USER+5)
    WM_PSD_YAFULLPAGERECT = (WM_USER+6)

    LPPAGEPAINTHOOK = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)
    LPPAGESETUPHOOK = CALLBACK(UINT_PTR, HWND, UINT, WPARAM, LPARAM)

    class tagPSDA(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hDevMode", HGLOBAL),
            ("hDevNames", HGLOBAL),
            ("Flags", DWORD),
            ("ptPaperSize", POINT),
            ("rtMinMargin", RECT),
            ("rtMargin", RECT),
            ("hInstance", HINSTANCE),
            ("lCustData", LPARAM),
            ("lpfnPageSetupHook", LPPAGESETUPHOOK),
            ("lpfnPagePaintHook", LPPAGEPAINTHOOK),
            ("lpPageSetupTemplateName", LPCSTR),
            ("hPageSetupTemplate", HGLOBAL)
        ]
    PAGESETUPDLGA = tagPSDA
    LPPAGESETUPDLGA = POINTER(PAGESETUPDLGA)

    class tagPSDW(CStructure):
        _fields_ = [
            ("lStructSize", DWORD),
            ("hwndOwner", HWND),
            ("hDevMode", HGLOBAL),
            ("hDevNames", HGLOBAL),
            ("Flags", DWORD),
            ("ptPaperSize", POINT),
            ("rtMinMargin", RECT),
            ("rtMargin", RECT),
            ("hInstance", HINSTANCE),
            ("lCustData", LPARAM),
            ("lpfnPageSetupHook", LPPAGESETUPHOOK),
            ("lpfnPagePaintHook", LPPAGEPAINTHOOK),
            ("lpPageSetupTemplateName", LPCWSTR),
            ("hPageSetupTemplate", HGLOBAL)
        ]
    PAGESETUPDLGW = tagPSDW
    LPPAGESETUPDLGW = POINTER(PAGESETUPDLGW)

    PAGESETUPDLG = unicode(PAGESETUPDLGW, PAGESETUPDLGA)
    LPPAGESETUPDLG = unicode(LPPAGESETUPDLGW, LPPAGESETUPDLGA)

    PageSetupDlgA = declare(comdlg32.PageSetupDlgA, BOOL, LPPAGESETUPDLGA)
    PageSetupDlgW = declare(comdlg32.PageSetupDlgW, BOOL, LPPAGESETUPDLGW)
    PageSetupDlg = unicode(PageSetupDlgW, PageSetupDlgA)

    PSD_DEFAULTMINMARGINS = 0x00000000 # default (printer's)
    PSD_INWININIINTLMEASURE = 0x00000000 # 1st of 4 possible
    PSD_MINMARGINS = 0x00000001 # use caller's
    PSD_MARGINS = 0x00000002 # use caller's
    PSD_INTHOUSANDTHSOFINCHES = 0x00000004 # 2nd of 4 possible
    PSD_INHUNDREDTHSOFMILLIMETERS = 0x00000008 # 3rd of 4 possible
    PSD_DISABLEMARGINS = 0x00000010
    PSD_DISABLEPRINTER = 0x00000020
    PSD_NOWARNING = 0x00000080 # must be same as PD_*
    PSD_DISABLEORIENTATION = 0x00000100
    PSD_RETURNDEFAULT = 0x00000400 # must be same as PD_*
    PSD_DISABLEPAPER = 0x00000200
    PSD_SHOWHELP = 0x00000800 # must be same as PD_*
    PSD_ENABLEPAGESETUPHOOK = 0x00002000 # must be same as PD_*
    PSD_ENABLEPAGESETUPTEMPLATE = 0x00008000 # must be same as PD_*
    PSD_ENABLEPAGESETUPTEMPLATEHANDLE = 0x00020000 # must be same as PD_*
    PSD_ENABLEPAGEPAINTHOOK = 0x00040000
    PSD_DISABLEPAGEPAINTING = 0x00080000
    PSD_NONETWORKBUTTON = 0x00200000 # must be same as PD_*