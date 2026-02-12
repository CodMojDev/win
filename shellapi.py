"""
/*****************************************************************************\
*                                                                             *
* shellapi.h -  SHELL.DLL functions, types, and definitions                   *
*                                                                             *
* Copyright (c) Microsoft Corporation. All rights reserved.                   *
*                                                                             *
\*****************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

from comtypes import IID, GUID

from .winnt import (PZZSTR, PZZWSTR, PCZZSTR, 
                    PCZZWSTR, PCSTR, PCWSTR, 
                    PWSTR, DWORDLONG)

from .winuser import WM_USER, SendMessage

from .sdkddkver import *

from .winbase import LPSECURITY_ATTRIBUTES

from .processthreadsapi import LPSTARTUPINFOW, LPPROCESS_INFORMATION

if cpreproc.pragma_once("_INC_SHELLAPI"):
    shell32 = W_WinDLL("shell32.dll")
    
    CommandLineToArgvW = declare(shell32.CommandLineToArgvW, LPWSTR, LPCWSTR, PINT)

    HDROP = HANDLE

    DragQueryFileA = declare(shell32.DragQueryFileA, UINT, HDROP, UINT, LPSTR, UINT)
    DragQueryFileW = declare(shell32.DragQueryFileW, UINT, HDROP, UINT, LPWSTR)
    DragQueryFile = unicode(DragQueryFileW, DragQueryFileA)
    
    DragQueryPoint = declare(shell32.DragQueryPoint, BOOL, HDROP, PPOINT)
    DragFinish = declare(shell32.DragFinish, VOID, HDROP)
    DragAcceptFiles = declare(shell32.DragAcceptFiles, VOID, HWND, BOOL)
    ShellExecuteA = declare(shell32.ShellExecuteA, HINSTANCE, HWND, LPCSTR, LPCSTR, LPCSTR, LPCSTR, INT)
    ShellExecuteW = declare(shell32.ShellExecuteW, HINSTANCE, HWND, LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, INT)
    ShellExecute = unicode(ShellExecuteW, ShellExecuteA)
    
    FindExecutableA = declare(shell32.FindExecutableA, HINSTANCE, LPCSTR, LPCSTR, LPSTR)
    FindExecutableW = declare(shell32.FindExecutableW, HINSTANCE, LPCWSTR, LPCWSTR, LPWSTR)
    FindExecutable = unicode(FindExecutableW, FindExecutableA)
    
    ShellAboutA = declare(shell32.ShellAboutA, INT, HWND, LPCSTR, LPCSTR, HICON)
    ShellAboutW = declare(shell32.ShellAboutW, INT, HWND, LPCWSTR, LPCWSTR, HICON)
    ShellAbout = unicode(ShellAboutW, ShellAboutA)
    
    DuplicateIcon = declare(shell32.DuplicateIcon, HICON, HINSTANCE, HICON)
    ExtractAssociatedIconA = declare(shell32.ExtractAssociatedIconA, HICON, HINSTANCE, LPSTR, PWORD)
    ExtractAssociatedIconW = declare(shell32.ExtractAssociatedIconW, HICON, HINSTANCE, LPWSTR, PWORD)
    ExtractAssociatedIcon = unicode(ExtractAssociatedIconW, ExtractAssociatedIconA)
    
    ExtractAssociatedIconExA = declare(shell32.ExtractAssociatedIconExA, HICON, HINSTANCE, LPSTR, PWORD, PWORD)
    ExtractAssociatedIconExW = declare(shell32.ExtractAssociatedIconExW, HICON, HINSTANCE, LPWSTR, PWORD, PWORD)
    ExtractAssociatedIconEx = unicode(ExtractAssociatedIconExW, ExtractAssociatedIconExA)
    
    ExtractIconA = declare(shell32.ExtractIconA, HICON, HINSTANCE, LPCSTR, UINT)
    ExtractIconW = declare(shell32.ExtractIconW, HICON, HINSTANCE, LPCWSTR, UINT)
    ExtractIcon = unicode(ExtractIconW, ExtractIconA)

    class _DRAGINFOA(CStructure):
        _fields_ = [
            ("uSize", UINT), # init with sizeof(DRAGINFO) */
            ("pt", POINT),
            ("fNC", BOOL),
            ("lpFileList", PZZSTR),
            ("grfKeyState", DWORD)
        ]
    DRAGINFOA = _DRAGINFOA
    LPDRAGINFOA = POINTER(DRAGINFOA)

    class _DRAGINFOW(CStructure):
        _fields_ = [
            ("uSize", UINT), # init with sizeof(DRAGINFO) */
            ("pt", POINT),
            ("fNC", BOOL),
            ("lpFileList", PZZWSTR),
            ("grfKeyState", DWORD)
        ]
    DRAGINFOW = _DRAGINFOW
    LPDRAGINFOW = POINTER(DRAGINFOW)

    ##
    ## AppBar stuff
    ##
    ABM_NEW = 0x00000000
    ABM_REMOVE = 0x00000001
    ABM_QUERYPOS = 0x00000002
    ABM_SETPOS = 0x00000003
    ABM_GETSTATE = 0x00000004
    ABM_GETTASKBARPOS = 0x00000005
    ABM_ACTIVATE = 0x00000006 # lParam == TRUE/FALSE means activate/deactivate
    ABM_GETAUTOHIDEBAR = 0x00000007
    ABM_SETAUTOHIDEBAR = 0x00000008 # this can fail at any time.  MUST check the result
    # lParam = TRUE/FALSE  Set/Unset
    # uEdge = what edge
    ABM_WINDOWPOSCHANGED = 0x0000009
    ABM_SETSTATE = 0x0000000a
    ABM_GETAUTOHIDEBAREX = 0x0000000b # multimon aware autohide bars
    ABM_SETAUTOHIDEBAREX = 0x0000000c
    # these are put in the wparam of callback messages
    ABN_STATECHANGE = 0x0000000
    ABN_POSCHANGED = 0x0000001
    ABN_FULLSCREENAPP = 0x0000002
    ABN_WINDOWARRANGE = 0x0000003 # lParam == TRUE means hide
    # flags for get state
    ABS_AUTOHIDE = 0x0000001
    ABS_ALWAYSONTOP = 0x0000002
    ABE_LEFT = 0
    ABE_TOP = 1
    ABE_RIGHT = 2
    ABE_BOTTOM = 3

    class _AppBarData(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("hWnd", HWND),
            ("uCallbackMessage", UINT),
            ("uEdge", UINT),
            ("rc", RECT),
            ("lParam", LPARAM) # message specific
        ]
    APPBARDATA = _AppBarData
    PAPPBARDATA = POINTER(APPBARDATA)

    SHAppBarMessage = declare(shell32.SHAppBarMessage, UINT_PTR, DWORD, PAPPBARDATA)
    ##
    ##  EndAppBar
    ##
    DoEnvironmentSubstA = declare(shell32.DoEnvironmentSubstA, DWORD, LPSTR, UINT)
    DoEnvironmentSubstW = declare(shell32.DoEnvironmentSubstW, DWORD, LPWSTR, UINT)
    DoEnvironmentSubst = unicode(DoEnvironmentSubstW, DoEnvironmentSubstA)
    # !UNICODE
    EIRESID = lambda x: (-1 * x)
    ExtractIconExA = declare(shell32.ExtractIconExA, UINT, LPCSTR, INT, POINTER(HICON), POINTER(HICON), UINT)
    ExtractIconExW = declare(shell32.ExtractIconExW, UINT, LPCWSTR, INT, POINTER(HICON), POINTER(HICON), UINT)
    ExtractIconEx = unicode(ExtractIconExW, ExtractIconExA)
    # !UNICODE
    # Shell File Operations
    FO_MOVE = 0x0001
    FO_COPY = 0x0002
    FO_DELETE = 0x0003
    FO_RENAME = 0x0004
    # SHFILEOPSTRUCT.fFlags and IFileOperation::SetOperationFlags() flag values
    FOF_MULTIDESTFILES = 0x0001
    FOF_CONFIRMMOUSE = 0x0002
    FOF_SILENT = 0x0004 # don't display progress UI (confirm prompts may be displayed still)
    FOF_RENAMEONCOLLISION = 0x0008 # automatically rename the source files to avoid the collisions
    FOF_NOCONFIRMATION = 0x0010 # don't display confirmation UI, assume "yes" for cases that can be bypassed, "no" for those that can not
    FOF_WANTMAPPINGHANDLE = 0x0020 # Fill in SHFILEOPSTRUCT.hNameMappings
    # Must be freed using SHFreeNameMappings
    FOF_ALLOWUNDO = 0x0040 # enable undo including Recycle behavior for IFileOperation::Delete()
    FOF_FILESONLY = 0x0080 # only operate on the files (non folders), both files and folders are assumed without this
    FOF_SIMPLEPROGRESS = 0x0100 # means don't show names of files
    FOF_NOCONFIRMMKDIR = 0x0200 # don't dispplay confirmatino UI before making any needed directories, assume "Yes" in these cases
    FOF_NOERRORUI = 0x0400 # don't put up error UI, other UI may be displayed, progress, confirmations
    FOF_NOCOPYSECURITYATTRIBS = 0x0800 # dont copy file security attributes (ACLs)
    FOF_NORECURSION = 0x1000 # don't recurse into directories for operations that would recurse
    FOF_NO_CONNECTED_ELEMENTS = 0x2000 # don't operate on connected elements ("xxx_files" folders that go with .htm files)
    FOF_WANTNUKEWARNING = 0x4000 # during delete operation, warn if object is being permanently destroyed instead of recycling (partially overrides FOF_NOCONFIRMATION)
    FOF_NORECURSEREPARSE = 0x8000 # deprecated; the operations engine always does the right thing on FolderLink objects (symlinks, reparse points, folder shortcuts)
    FOF_NO_UI = (FOF_SILENT | FOF_NOCONFIRMATION | FOF_NOERRORUI | FOF_NOCONFIRMMKDIR) # don't display any UI at all

    FILEOP_FLAGS = DWORD

    PO_DELETE = 0x0013 # printer is being deleted
    PO_RENAME = 0x0014 # printer is being renamed
    PO_PORTCHANGE = 0x0020 # port this printer connected to is being changed
    # if this id is set, the strings received by
    # the copyhook are a doubly-null terminated
    # list of strings.  The first is the printer
    # name and the second is the printer port.
    PO_REN_PORT = 0x0034 # PO_RENAME and PO_PORTCHANGE at same time.
    # no POF_ flags currently defined

    PRINTEROP_FLAGS = WORD

    # implicit parameters are:
    #      if pFrom or pTo are unqualified names the current directories are
    #      taken from the global current drive/directory settings managed
    #      by Get/SetCurrentDrive/Directory
    #
    #      the global confirmation settings
    class _SHFILEOPSTRUCTA(CStructure):
        _fields_ = [
            ("hwnd", HWND),
            ("wFunc", UINT),
            ("pFrom", PCZZSTR),
            ("pTo", PCZZSTR),
            ("fFlags", FILEOP_FLAGS),
            ("fAnyOperationsAborted", BOOL),
            ("hNameMappings", LPVOID),
            ("lpszProgressTitle", PCSTR) # only used if FOF_SIMPLEPROGRESS
        ]
    SHFILEOPSTRUCTA = _SHFILEOPSTRUCTA
    LPSHFILEOPSTRUCTA = POINTER(SHFILEOPSTRUCTA)

    class _SHFILEOPSTRUCTW(CStructure):
        _fields_ = [
            ("hwnd", HWND),
            ("wFunc", UINT),
            ("pFrom", PCZZWSTR),
            ("pTo", PCZZWSTR),
            ("fFlags", FILEOP_FLAGS),
            ("fAnyOperationsAborted", BOOL),
            ("hNameMappings", LPVOID),
            ("lpszProgressTitle", PCWSTR) # only used if FOF_SIMPLEPROGRESS
        ]
    SHFILEOPSTRUCTW = _SHFILEOPSTRUCTW
    LPSHFILEOPSTRUCTW = POINTER(SHFILEOPSTRUCTW)

    SHFILEOPSTRUCT = unicode(SHFILEOPSTRUCTW, SHFILEOPSTRUCTA)
    LPSHFILEOPSTRUCT = unicode(LPSHFILEOPSTRUCTW, LPSHFILEOPSTRUCTA)

    SHFileOperationA = declare(shell32.SHFileOperationA, INT, LPSHFILEOPSTRUCTA)
    SHFileOperationW = declare(shell32.SHFileOperationW, INT, LPSHFILEOPSTRUCTW)
    SHFileOperation = unicode(SHFileOperationW, SHFileOperationA)
    
    SHFreeNameMappings = declare(shell32.SHFreeNameMappings, VOID, HANDLE)

    class _SHNAMEMAPPINGA(CStructure):
        _fields_ = [
            ("pszOldPath", LPSTR),
            ("pszNewPath", LPSTR),
            ("cchOldPath", INT),
            ("cchNewPath", INT)
        ]
    SHNAMEMAPPINGA = _SHNAMEMAPPINGA
    LPSHNAMEMAPPINGA = POINTER(SHNAMEMAPPINGA)

    class _SHNAMEMAPPINGW(CStructure):
        _fields_ = [
            ("pszOldPath", LPWSTR),
            ("pszNewPath", LPWSTR),
            ("cchOldPath", INT),
            ("cchNewPath", INT)
        ]
    SHNAMEMAPPINGW = _SHNAMEMAPPINGW
    LPSHNAMEMAPPINGW = POINTER(SHNAMEMAPPINGW)

    SHNAMEMAPPING = unicode(SHNAMEMAPPINGW, SHNAMEMAPPINGA)
    LPSHNAMEMAPPING = unicode(LPSHNAMEMAPPINGW, LPSHNAMEMAPPINGA)

    ##
    ## End Shell File Operations
    ##
    ##
    ##  Begin ShellExecuteEx and family
    ##
    # ShellExecute() and ShellExecuteEx() error codes
    # regular WinExec() codes
    SE_ERR_FNF = 2 # file not found
    SE_ERR_PNF = 3 # path not found
    SE_ERR_ACCESSDENIED = 5 # access denied
    SE_ERR_OOM = 8 # out of memory
    SE_ERR_DLLNOTFOUND = 32
    # WINVER >= 0x0400
    # error values for ShellExecute() beyond the regular WinExec() codes
    SE_ERR_SHARE = 26
    SE_ERR_ASSOCINCOMPLETE = 27
    SE_ERR_DDETIMEOUT = 28
    SE_ERR_DDEFAIL = 29
    SE_ERR_DDEBUSY = 30
    SE_ERR_NOASSOC = 31
    # Note CLASSKEY overrides CLASSNAME
    SEE_MASK_DEFAULT = 0x00000000
    SEE_MASK_CLASSNAME = 0x00000001 # SHELLEXECUTEINFO.lpClass is valid
    SEE_MASK_CLASSKEY = 0x00000003 # SHELLEXECUTEINFO.hkeyClass is valid
    # Note SEE_MASK_INVOKEIDLIST(0xC) implies SEE_MASK_IDLIST(0x04)
    SEE_MASK_IDLIST = 0x00000004 # SHELLEXECUTEINFO.lpIDList is valid
    SEE_MASK_INVOKEIDLIST = 0x0000000c # enable IContextMenu based verbs
    SEE_MASK_ICON = 0x00000010 # not used
    SEE_MASK_HOTKEY = 0x00000020 # SHELLEXECUTEINFO.dwHotKey is valid
    SEE_MASK_NOCLOSEPROCESS = 0x00000040 # SHELLEXECUTEINFO.hProcess
    SEE_MASK_CONNECTNETDRV = 0x00000080 # enables re-connecting disconnected network drives
    SEE_MASK_NOASYNC = 0x00000100 # block on the call until the invoke has completed, use for callers that exit after calling ShellExecuteEx()
    SEE_MASK_FLAG_DDEWAIT = SEE_MASK_NOASYNC # Use SEE_MASK_NOASYNC instead of SEE_MASK_FLAG_DDEWAIT as it more accuratly describes the behavior
    SEE_MASK_DOENVSUBST = 0x00000200 # indicates that SHELLEXECUTEINFO.lpFile contains env vars that should be expanded
    SEE_MASK_FLAG_NO_UI = 0x00000400 # disable UI including error messages
    SEE_MASK_UNICODE = 0x00004000
    SEE_MASK_NO_CONSOLE = 0x00008000
    SEE_MASK_ASYNCOK = 0x00100000
    SEE_MASK_HMONITOR = 0x00200000 # SHELLEXECUTEINFO.hMonitor
    SEE_MASK_NOZONECHECKS = 0x00800000
    SEE_MASK_NOQUERYCLASSSTORE = 0x01000000
    SEE_MASK_WAITFORINPUTIDLE = 0x02000000
    SEE_MASK_FLAG_LOG_USAGE = 0x04000000
    # When SEE_MASK_FLAG_HINST_IS_SITE is specified SHELLEXECUTEINFO.hInstApp is used as an
    # _In_ parameter and specifies a IUnknown* to be used as a site pointer. The site pointer
    # is used to provide services to shell execute, the handler binding process and the verb handlers
    # once they are invoked.
    SEE_MASK_FLAG_HINST_IS_SITE = 0x08000000

    class _U_HIHM(Union):
        _fields_ = [
            ("hIcon", HANDLE), # not used
            ("hMonitor", HANDLE) # in, valid when SEE_MASK_HMONITOR specified
        ]

    class _SHELLEXECUTEINFOA(CStructure):
        _fields_ = [
            ("cbSize", DWORD), # in, required, sizeof of this structure
            ("fMask", ULONG), # in, SEE_MASK_XXX values
            ("hwnd", HWND), # in, optional
            ("lpVerb", LPCSTR), # in, optional when unspecified the default verb is choosen
            ("lpFile", LPCSTR), # in, either this value or lpIDList must be specified
            ("lpParameters", LPCSTR), # in, optional
            ("lpDirectory", LPCSTR), # in, optional
            ("nShow", INT), # in, required
            ("hInstApp", HINSTANCE), # out when SEE_MASK_NOCLOSEPROCESS is specified
            ("lpIDList", PVOID), # in, valid when SEE_MASK_IDLIST is specified, PCIDLIST_ABSOLUTE, for use with SEE_MASK_IDLIST & SEE_MASK_INVOKEIDLIST
            ("lpClass", LPCSTR), # in, valid when SEE_MASK_CLASSNAME is specified
            ("hkeyClass", HKEY), # in, valid when SEE_MASK_CLASSKEY is specified
            ("dwHotKey", DWORD), # in, valid when SEE_MASK_HOTKEY is specified
            ("u", _U_HIHM), 
            ("hProcess", HANDLE) # out, valid when SEE_MASK_NOCLOSEPROCESS specified
        ]
    SHELLEXECUTEINFOA = _SHELLEXECUTEINFOA
    LPSHELLEXECUTEINFOA = POINTER(SHELLEXECUTEINFOA)


    class _SHELLEXECUTEINFOW(CStructure):
        _fields_ = [
            ("cbSize", DWORD), # in, required, sizeof of this structure
            ("fMask", ULONG), # in, SEE_MASK_XXX values
            ("hwnd", HWND), # in, optional
            ("lpVerb", LPCSTR), # in, optional when unspecified the default verb is choosen
            ("lpFile", LPCSTR), # in, either this value or lpIDList must be specified
            ("lpParameters", LPCSTR), # in, optional
            ("lpDirectory", LPCSTR), # in, optional
            ("nShow", INT), # in, required
            ("hInstApp", HINSTANCE), # out when SEE_MASK_NOCLOSEPROCESS is specified
            ("lpIDList", PVOID), # in, valid when SEE_MASK_IDLIST is specified, PCIDLIST_ABSOLUTE, for use with SEE_MASK_IDLIST & SEE_MASK_INVOKEIDLIST
            ("lpClass", LPCSTR), # in, valid when SEE_MASK_CLASSNAME is specified
            ("hkeyClass", HKEY), # in, valid when SEE_MASK_CLASSKEY is specified
            ("dwHotKey", DWORD), # in, valid when SEE_MASK_HOTKEY is specified
            ("u", _U_HIHM), 
            ("hProcess", HANDLE) # out, valid when SEE_MASK_NOCLOSEPROCESS specified
        ]
    SHELLEXECUTEINFOW = _SHELLEXECUTEINFOW
    LPSHELLEXECUTEINFOW = POINTER(SHELLEXECUTEINFOW)

    SHELLEXECUTEINFO = unicode(SHELLEXECUTEINFOW, SHELLEXECUTEINFOA)
    LPSHELLEXECUTEINFO = unicode(LPSHELLEXECUTEINFOW, LPSHELLEXECUTEINFOA)

    ShellExecuteExA = declare(shell32.ShellExecuteExA, BOOL, LPSHELLEXECUTEINFOA)
    ShellExecuteExW = declare(shell32.ShellExecuteExW, BOOL, LPSHELLEXECUTEINFOW)
    ShellExecuteEx = unicode(ShellExecuteExW, ShellExecuteExA)
    
    # deprecated, no longer implemented
    class _SHCREATEPROCESSINFOW(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("fMask", ULONG),
            ("hwnd", HWND),
            ("pszFile", LPCWSTR),
            ("pszParameters", LPCWSTR),
            ("pszCurrentDirectory", LPCWSTR),
            ("hUserToken", HANDLE),
            ("lpProcessAttributes", LPSECURITY_ATTRIBUTES),
            ("lpThreadAttributes", LPSECURITY_ATTRIBUTES),
            ("bInheritHandles", BOOL),
            ("dwCreationFlags", DWORD),
            ("lpStartupInfo", LPSTARTUPINFOW),
            ("lpProcessInformation", LPPROCESS_INFORMATION)
        ]
    SHCREATEPROCESSINFOW = _SHCREATEPROCESSINFOW
    PSHCREATEPROCESSINFOW = POINTER(SHCREATEPROCESSINFOW)

    SHCreateProcessAsUserW = declare(shell32.SHCreateProcessAsUserW, BOOL, PSHCREATEPROCESSINFOW)

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        SHEvaluateSystemCommandTemplate = declare(shell32.SHEvaluateSystemCommandTemplate, VOID, PCWSTR, POINTER(PWSTR), POINTER(PWSTR), POINTER(PWSTR))

    #
    #  SHEvaluateSystemCommandTemplate()
    #      *   enforces stricter validation before calling CreateProcess().  may also be
    #              used before calling ShellExecute().
    #      *   should be used when caller wants the deterministic behavior from a command template
    #              regardless of execution context.  it ignores the current process state,
    #              such as the %PATH%, GetCurrentDirectory(), and parent process directory.
    #      *   should be used when the command is hardcoded.
    #      *   is used by ShellExecute() when handling file associations from HKCR.
    #      *   reduces CreateProcess() commandline exploits
    #      *   is not designed for processing user input, and may generate unexpected failures.
    #
    #  INPUT:
    #      pszCmdTemplate =    command line, this may or may not include parameters.
    #                          if the parameters are substitution parameters then this API
    #                          should be called before parameters have been replaced.
    #                          (check the examples below to see sample supported inputs.)
    #
    #  OUTPUT on return: S_OK
    #      ppszApplication =   verified path to the Application.  this should be passed as the lpApplication
    #                          parameter to CreateProcess() or the lpFile parameter to ShellExecute().
    #                          (allocated using CoTaskMemAlloc(), free with CoTaskMemFree())
    #
    #      ppszCommandLine =   OPTIONAL - use if planning to call CreateProcess().
    #                          resulting command line template.  parameters should be replaced based on this template,
    #                          and then passed as the lpCommandLine parameter to CreateProcess().
    #                          it is guaranteed to be of a form that PathGetArgs() will always succeed correctly.
    #                          (allocated using CoTaskMemAlloc(), free with CoTaskMemFree())
    #
    #      ppszParameters  =   OPTIONAL - use if planning to call ShellExecute().
    #                          resulting parameter list template.  parameters should be replaced based on this template,
    #                          and then passed as the lpParameters parameter to ShellExecute().
    #                          NOTE: identical to PathGetArgs(*ppszCommandLine).
    #                          (allocated using CoTaskMemAlloc(), free with CoTaskMemFree())
    #
    #  OUTPUT on return: FAILED()
    #      all outputs will be NULL'ed on failure
    #
    #  NOTES:  the parsing logic to determine a valid Application path is non-trivial, although
    #              the extension is not required and if missing will be completed
    #              in the following standard order:  { .PIF, .COM, .EXE, .BAT, .CMD }
    #
    #      Relative Paths are System Paths - if the first token has no path qualifiers
    #              then the token is first checked to see if a key of the same name has
    #              been installed under HKLM\Software\Microsoft\Windows\CurrentVersion\App Paths.
    #              if the key or default value does not exist, it is assumed to be a child
    #              of the system directories.  the following directories will be searched
    #              in order for the relative token: { CSIDL_SYSTEM, CSIDL_WINDOWS }
    #
    #      Prefer Quoted Paths - if the first token in pszCmdTemplate is quoted and appears
    #              to be an absolute path then the token is the only possible result.
    #
    #      Limit Forms of Unquoted Paths - if the first token is unquoted and appears
    #              to be an absolute path, then it is subject to more stringent limitations.
    #              if the token is a substring of CSIDL_PROGRAM_FILES or does not
    #              exist on the file system, then SHEvaluateSystemCommandTemplate() will
    #              attempt to complete using a token delimited by the first space of the
    #              last valid path segment (usually the file name).  if this token also doesnt exist,
    #              then the next space will be used, etc.
    #
    #  USAGE:      used before calling into CreateProcess() or ShellExecute(), callers
    #              would typically look like the following:

    """
    #if 0
    HRESULT MyCreateProcessPriv(_In_ PCWSTR pszCmd)
    {
    PWSTR pszApp;
    PWSTR pszCmdLine;
    HRESULT hr = SHEvaluateSystemCommandTemplate(pszCmd, &pszApp, &pszCmdLine);
    if (SUCCEEDED(hr))
    {

    PROCESS_INFORMATION pi;
    STARTUPINFO si = {0};
    si.cb = sizeof(startup);
    si.wShowWindow = SW_SHOWNORMAL;

    if (CreateProcess(pszApp, pszCmdLine, NULL, NULL, FALSE,
    CREATE_DEFAULT_ERROR_MODE, NULL, NULL, &si, &pi))
    {

    ASSERT(hr == S_OK);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    }
    else
    {
    hr = HRESULT_FROM_WIN32(GetLastError());
    }

    CoTaskMemFree(pszApp);
    CoTaskMemFree(pszCmdLine);
    }
    return hr;
    }

    HRESULT MyShellExec(_In_ PCWSTR pszCmd)
    {
    PWSTR pszApp;
    PWSTR pszCmdLine;
    HRESULT hr = SHEvaluateSystemCommandTemplate(pszCmd, &pszApp, &pszCmdLine);
    if (SUCCEEDED(hr))
    {

    SHELLEXECUTEINFOW sei = {
    sizeof(sei),
    0,
    NULL,
    NULL,
    pszApp,
    PathGetArgs(pszCmdLine),
    NULL,
    SW_SHOWNORMAL,
    0,
    NULL,
    NULL,
    NULL,
    0,
    NULL,
    NULL
    };

    if (ShellExecuteEx(&sei))
    {

    ASSERT(hr == S_OK);
    }
    else
    {
    hr = HRESULT_FROM_WIN32(GetLastError());
    }

    CoTaskMemFree(pszApp);
    CoTaskMemFree(pszCmdLine);
    }
    return hr;
    }
    #  0 # SAMPLE CODE

    """

    #  EXAMPLE:   Each example will show an input parameter and the results returned by
    #              SHEvaluateSystemCommandTemplate().  Also included is the alternate result
    #              of what CreateProcess() would have created if pszCmdTemplate were
    #              passed directly as lpCommandLine and lpApplication were NULL.
    #              (results marked with an asterisk (*) indicate differences.)
    #
    #          Assume for the examples that the following paths and values exist:
    #
    #      SHGetFolderPath() values:
    #          CSIDL_SYSTEM            =   C:\windows\system32
    #          CSIDL_WINDOWS           =   C:\windows
    #          CSIDL_PROGRAM_FILES     =   C:\Program Files
    #
    #      Environment settings
    #          GetModuleFileName(NULL) =   C:\Program Files\Example\sample.exe
    #          GetCurrentDirectory()   =   \\server\share\foo
    #          HKLM\...\App Paths\pbrush.exe = C:\windows\system32\mspaint.exe
    #          HKLM\...\App Paths\mycl.exe = C:\Program Files\Compilers\mycl.exe
    #          PATH                    =   c:\windows\system32;C:\windows;c:\;C:\Program Files\Compilers\
    #
    #      Valid Application paths:
    #          C:\Program Files\Internet Explorer\iexplore.exe
    #          C:\windows\system32\rundll32.exe
    #          C:\windows\system32\notepad.exe
    #          C:\windows\notepad.exe
    #          C:\Program Files\Example\sample.exe
    #          C:\Program Files\Compilers\cl.exe
    #          C:\Other Programs\prog.exe
    #
    #      Suspicious (possibly hostile) Application paths:
    #          C:\Program.exe
    #          C:\Program Files\Internet.exe
    #          C:\Program Files\Example\regedit.bat
    #          C:\mycl.exe
    #          \\server\share\foo\rundll32.exe
    #          \\server\share\foo\myapp.exe
    #
    #
    #  Relative Path Example #1
    #      pszCmdTemplate      =   notepad.exe %1
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\windows\system32\notepad.exe
    #              pszCommandLine  =   "notepad.exe" %1
    #          CreateProcess() would return TRUE
    #              new process =   C:\windows\system32\notepad.exe
    #
    #  Relative Path Example #2
    #      pszCmdTemplate      =   rundll32.exe shell32.dll,RunDll
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\windows\system32\rundll32.exe
    #              pszCommandLine  =   "rundll32.exe" shell32.dll,RunDll
    #          * CreateProcess() would return TRUE
    #              new process =   \\server\share\foo\rundll32.exe
    #
    #  Relative Path Example #3
    #      pszCmdTemplate      =   regedit %1
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\windows\system32\regedit.exe
    #              pszCommandLine  =   "regedit.exe" %1
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program Files\Example\regedit.bat
    #
    #  Relative Path Example #4
    #      pszCmdTemplate      =   pbrush "%1"
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\windows\system32\mspaint.exe
    #              pszCommandLine  =   "mspaint.exe" "%1"
    #          * CreateProcess() would return FALSE
    #
    #  Relative Path Example #5
    #      pszCmdTemplate      =   mycl "%1" "%2"
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Compilers\mycl.exe
    #              pszCommandLine  =   "mycl.exe" "%1" "%2"
    #          * CreateProcess() would return TRUE
    #              new process =   C:\mycl.exe
    #
    #  Relative Path Example #6
    #      pszCmdTemplate      =   myapp.exe
    #          SHEvaluateSystemCommandTemplate() returns: CO_E_APPNOTFOUND
    #          * CreateProcess() would return TRUE
    #              new process =   \\server\share\foo\myapp.exe
    #
    #  Quoted Path Example #1
    #      pszCmdTemplate      =   "C:\Program Files\Internet Explorer\iexplore.exe" -nohome
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet Explorer\iexplore.exe
    #              pszCommandLine  =   "C:\Program Files\Internet Explorer\iexplore.exe" -nohome
    #          CreateProcess() would return TRUE
    #              new process =   C:\Program Files\Internet Explorer\iexplore.exe
    #
    #  Quoted Path Example #2
    #      pszCmdTemplate      =   "C:\Program Files\Internet" -url
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet.exe
    #              pszCommandLine  =   "C:\Program Files\Internet.exe" -url
    #          CreateProcess() would return TRUE
    #              new process =   C:\Program Files\internet.exe
    #
    #  Quoted Path Example #3
    #      pszCmdTemplate      =   "C:\Program" -url
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program.exe
    #              pszCommandLine  =   "C:\Program.exe" -url
    #          CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #1
    #      pszCmdTemplate      =   C:\Program Files\Internet Explorer\iexplore.exe -nohome
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet Explorer\iexplore.exe
    #              pszCommandLine  =   "C:\Program Files\Internet Explorer\iexplore.exe" -nohome
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #2
    #      pszCmdTemplate      =   C:\Program Files\Internet Explorer\iexplore.exe -url fool.htm
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet Explorer\iexplore.exe
    #              pszCommandLine  =   "C:\Program Files\Internet Explorer\iexplore.exe" -url fool.htm
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #3
    #      pszCmdTemplate      =   C:\Program Files\Internet Explorer\iexplore.exe -url C:\fool.htm
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet Explorer\iexplore.exe
    #              pszCommandLine  =   "C:\Program Files\Internet Explorer\iexplore.exe" -url C:\fool.htm
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #4
    #      pszCmdTemplate      =   C:\Program Files\Internet -url
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Program Files\Internet.exe
    #              pszCommandLine  =   "C:\Program Files\Internet.exe" -url
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #5
    #      pszCmdTemplate      =   C:\Other Programs\prog.exe -go %1 \fool %2
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Other Programs\prog.exe
    #              pszCommandLine  =   "C:\Other Programs\prog.exe" %1 \fool %2
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Other Programs\prog.exe
    #
    #  Unquoted Example #6
    #      pszCmdTemplate      =   C:\Other Programs\prog.exe -go "\fool" "%1"
    #          SHEvaluateSystemCommandTemplate() returns: S_OK
    #              pszApplication  =   C:\Other Programs\prog.exe
    #              pszCommandLine  =   "C:\Other Programs\prog.exe" -go "\fool" "%1"
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Other Programs\prog.exe
    #
    #  Unquoted Example #7
    #      pszCmdTemplate      =   C:\Program Files\Internet Explorer\iexplore.exe -url \fool.htm
    #          SHEvaluateSystemCommandTemplate() returns: CO_E_APPNOTFOUND
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #8
    #      pszCmdTemplate      =   C:\Program -url
    #          SHEvaluateSystemCommandTemplate() returns: CO_E_APPNOTFOUND
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #9
    #      pszCmdTemplate      =   C:\Other Programs\prog.exe -go \fool us
    #          SHEvaluateSystemCommandTemplate() returns: CO_E_APPNOTFOUND
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Other Programs\prog.exe
    #
    #  Unquoted Example #10
    #      pszCmdTemplate      =   C:\Other Programs\prog.exe -go \fool %1
    #          SHEvaluateSystemCommandTemplate() returns: CO_E_APPNOTFOUND
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Other Programs\prog.exe
    #
    #  Unquoted Example #11
    #      pszCmdTemplate      =   C:\Program "%1"
    #          SHEvaluateSystemCommandTemplate() returns: E_ACCESSDENIED
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  Unquoted Example #12
    #      pszCmdTemplate      =   C:\Program
    #          SHEvaluateSystemCommandTemplate() returns: E_ACCESSDENIED
    #          * CreateProcess() would return TRUE
    #              new process =   C:\Program.exe
    #
    #  used for implementing IShellFolder::GetUIObject(IID_IQueryAssociations)
    #  designed for namespace extensions with registered extensible types
    #  SHCreateDefaultContextMenu() and others use IQueryAssociations to build up data sets

    ASSOCCLASS = INT
    if True:
                                         #  which other members are used
        ASSOCCLASS_SHELL_KEY = 0,        #  hkeyClass
        ASSOCCLASS_PROGID_KEY = 1        #  hkeyClass
        ASSOCCLASS_PROGID_STR = 2        #  pszClass (HKCR\pszClass)
        ASSOCCLASS_CLSID_KEY = 3         #  hkeyClass
        ASSOCCLASS_CLSID_STR = 4         #  pszClass (HKCR\CLSID\pszClass)
        ASSOCCLASS_APP_KEY = 5           #  hkeyClass
        ASSOCCLASS_APP_STR = 6           #  pszClass (HKCR\Applications\PathFindFileName(pszClass))
        ASSOCCLASS_SYSTEM_STR = 7        #  pszClass
        ASSOCCLASS_FOLDER = 8            #  none
        ASSOCCLASS_STAR = 9              #  none
        ASSOCCLASS_FIXED_PROGID_STR = 10 #  pszClass (HKCR\pszClass), do not apply mapping of pszClass based on user defaults
        ASSOCCLASS_PROTOCOL_STR = 11     #  pszClass is a protocol, apply mapping of pszClass based on user defaults

    class ASSOCIATIONELEMENT(CStructure):
        _fields_ = [
            ("ac", ASSOCCLASS), # required
            ("hkClass", HKEY), # may be NULL
            ("pszClass", PCWSTR) # may be NULL
        ]

    # the object returned from this API implements IQueryAssociations

    AssocCreateForClasses = declare(shell32.AssocCreateForClasses, VOID, POINTER(ASSOCIATIONELEMENT), ULONG, POINTER(IID), PPVOID)

    """
    #if 0
    HRESULT CCustomFolder::_AssocCreate(_In_ PCUITEMID_CHILD pidl, _In_ REFIID riid, _Outptr_ void **ppv)
    {
    *ppv = nullptr;
    ASSOCIATIONELEMENT rgAssoc[] =
    {
    { ASSOCCLASS_PROGID_STR, nullptr, CCustomFolder::_MapChildToType(pidl)},
    { ASSOCCLASS_FOLDER, nullptr, nullptr},
    };
    if (CCustomFolder::_IsFolder(pidl))
    {
    return AssocCreateForClasses(rgAssoc, ARRAYSIZE(rgAssoc), riid, ppv);
    }
    else
    {

    return AssocCreateForClasses(rgAssoc, ARRAYSIZE(rgAssoc)-1, riid, ppv);
    }
    }

    HRESULT CCustomFolder::GetUIObjectOf(...)
    {

    if (riid == IID_IQueryAssociations)
    {
    hr = _AssocCreate(apidl[0], riid, ppv);
    }

    }
    # SAMPLE CODE

    """

    ##
    ##  End ShellExecuteEx and family
    ##
    #
    # RecycleBin
    #
    # struct for query recycle bin info
    class _SHQUERYRBINFO(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("i64Size", DWORDLONG),
            ("i64NumItems", DWORDLONG)
        ]
    SHQUERYRBINFO = _SHQUERYRBINFO
    LPSHQUERYRBINFO = POINTER(SHQUERYRBINFO)

    # flags for SHEmptyRecycleBin
    #
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI = 0x00000002
    SHERB_NOSOUND = 0x00000004

    SHQueryRecycleBinA = declare(shell32.SHQueryRecycleBinA, VOID, LPCSTR, LPSHQUERYRBINFO)
    SHQueryRecycleBinW = declare(shell32.SHQueryRecycleBinW, VOID, LPCWSTR, LPSHQUERYRBINFO)
    SHQueryRecycleBin = unicode(SHQueryRecycleBinW, SHQueryRecycleBinA)
    
    SHEmptyRecycleBinA = declare(shell32.SHEmptyRecycleBinA, VOID, HWND, LPCSTR, DWORD)
    SHEmptyRecycleBinW = declare(shell32.SHEmptyRecycleBinW, VOID, HWND, LPCWSTR, DWORD)
    SHEmptyRecycleBin = unicode(SHEmptyRecycleBinW, SHEmptyRecycleBinA)

    ##
    ## end of RecycleBin

    ##
    ## Taskbar notification definitions
    ##

    QUERY_USER_NOTIFICATION_STATE = INT
    if True:
        QUNS_NOT_PRESENT               = 1    # The user is not present.  Heuristic check for modes like: screen saver, locked machine, non-active FUS session
        QUNS_BUSY                      = 2    # The user is busy.  Heuristic check for modes like: full-screen app
        QUNS_RUNNING_D3D_FULL_SCREEN   = 3    # full-screen (exlusive-mode) D3D app
        QUNS_PRESENTATION_MODE         = 4    # Windows presentation mode (laptop feature) is turned on
        QUNS_ACCEPTS_NOTIFICATIONS     = 5    # notifications can be freely sent
        QUNS_QUIET_TIME                = 6    # We are in OOBE quiet period
        QUNS_APP                       = 7    # App-mode application

    SHQueryUserNotificationState = declare(shell32.SHQueryUserNotificationState, VOID, POINTER(QUERY_USER_NOTIFICATION_STATE))

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN7:
        # This api retrieves an IPropertyStore that stores the window's properties.
        SHGetPropertyStoreForWindow = declare(shell32.SHGetPropertyStoreForWindow, VOID, HWND, POINTER(IID), PPVOID)

    class NOTIFYICONDATAA(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("hWnd", HWND),
            ("uID", UINT),
            ("uFlags", UINT),
            ("uCallbackMessage", UINT),
            ("hIcon", HICON),
        ]

        if cpreproc.getdef("_WINVER") < WIN32_WINNT_WIN2K:
            _fields_.append(("szTip", CHAR * 64))
        else:
            _fields_.append(("szTip", CHAR * 128))
            _fields_.append(("dwState", DWORD))
            _fields_.append(("dwStateMask", DWORD))
            _fields_.append(("szInfo", CHAR * 256))

            if cpreproc.ifndef("_SHELL_EXPORTS_INTERNALAPI_H_"):
                class _U_UTUV(Union):
                    _fields_ = [
                        ("uTimeout", UINT),
                        ("uVersion", UINT),
                    ]
                _fields_.append(("u", _U_UTUV))

            _fields_.append(("szInfoTitle", CHAR * 64))
            _fields_.append(("dwInfoFlags", DWORD))

            if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
                _fields_.append(("guidItem", GUID))
            if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
                _fields_.append(("hBalloonIcon", HICON))

    PNOTIFYICONDATAA = POINTER(NOTIFYICONDATAA)

    class NOTIFYICONDATAW(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("hWnd", HWND),
            ("uID", UINT),
            ("uFlags", UINT),
            ("uCallbackMessage", UINT),
            ("hIcon", HICON),
        ]

        if cpreproc.getdef("_WINVER") < WIN32_WINNT_WIN2K:
            _fields_.append(("szTip", WCHAR * 64))
        else:
            _fields_.append(("szTip", WCHAR * 128))
            _fields_.append(("dwState", DWORD))
            _fields_.append(("dwStateMask", DWORD))
            _fields_.append(("szInfo", WCHAR * 256))

            if cpreproc.ifndef("_SHELL_EXPORTS_INTERNALAPI_H_"):
                class _U_UTUV(Union):
                    _fields_ = [
                        ("uTimeout", UINT),
                        ("uVersion", UINT),
                    ]
                _fields_.append(("u", _U_UTUV))

            _fields_.append(("szInfoTitle", WCHAR * 64))
            _fields_.append(("dwInfoFlags", DWORD))

            if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
                _fields_.append(("guidItem", GUID))
            if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
                _fields_.append(("hBalloonIcon", HICON))

    PNOTIFYICONDATAW = POINTER(NOTIFYICONDATAW)
    NOTIFYICONDATA = unicode(NOTIFYICONDATAW, NOTIFYICONDATAA)
    PNOTIFYICONDATA = unicode(PNOTIFYICONDATAW, PNOTIFYICONDATAA)

    NOTIFYICONDATAA_V1_SIZE = NOTIFYICONDATAA.szTip.offset
    NOTIFYICONDATAW_V1_SIZE = NOTIFYICONDATAW.szTip.offset

    NOTIFYICONDATAA_V2_SIZE = NOTIFYICONDATAA.guidItem.offset
    NOTIFYICONDATAW_V2_SIZE = NOTIFYICONDATAW.guidItem.offset

    NOTIFYICONDATAA_V3_SIZE = NOTIFYICONDATAA.hBalloonIcon.offset
    NOTIFYICONDATAW_V3_SIZE = NOTIFYICONDATAW.hBalloonIcon.offset

    NOTIFYICONDATA_V1_SIZE = unicode(NOTIFYICONDATAW_V1_SIZE, NOTIFYICONDATAA_V1_SIZE)
    NOTIFYICONDATA_V2_SIZE = unicode(NOTIFYICONDATAW_V2_SIZE, NOTIFYICONDATAA_V2_SIZE)
    NOTIFYICONDATA_V3_SIZE = unicode(NOTIFYICONDATAW_V3_SIZE, NOTIFYICONDATAA_V3_SIZE)

    NIN_SELECT = (WM_USER + 0)
    NINF_KEY = 0x1
    NIN_KEYSELECT = (NIN_SELECT | NINF_KEY)
    NIN_BALLOONSHOW = (WM_USER + 2)
    NIN_BALLOONHIDE = (WM_USER + 3)
    NIN_BALLOONTIMEOUT = (WM_USER + 4)
    NIN_BALLOONUSERCLICK = (WM_USER + 5)
    NIN_POPUPOPEN = (WM_USER + 6)
    NIN_POPUPCLOSE = (WM_USER + 7)
    NIM_ADD = 0x00000000
    NIM_MODIFY = 0x00000001
    NIM_DELETE = 0x00000002
    NIM_SETFOCUS = 0x00000003
    NIM_SETVERSION = 0x00000004
    # set NOTIFYICONDATA.uVersion with 0, 3 or 4
    # please read the documentation on the behavior difference that the different versions imply
    NOTIFYICON_VERSION = 3
    NOTIFYICON_VERSION_4 = 4
    NIF_MESSAGE = 0x00000001
    NIF_ICON = 0x00000002
    NIF_TIP = 0x00000004
    NIF_STATE = 0x00000008
    NIF_INFO = 0x00000010
    NIF_GUID = 0x00000020
    NIF_REALTIME = 0x00000040
    NIF_SHOWTIP = 0x00000080
    NIS_HIDDEN = 0x00000001
    NIS_SHAREDICON = 0x00000002
    # says this is the source of a shared icon
    # Notify Icon Infotip flags
    NIIF_NONE = 0x00000000
    # icon flags are mutually exclusive
    # and take only the lowest 2 bits
    NIIF_INFO = 0x00000001
    NIIF_WARNING = 0x00000002
    NIIF_ERROR = 0x00000003
    NIIF_USER = 0x00000004
    NIIF_ICON_MASK = 0x0000000F
    NIIF_NOSOUND = 0x00000010
    NIIF_LARGE_ICON = 0x00000020
    NIIF_RESPECT_QUIET_TIME = 0x00000080

    class _NOTIFYICONIDENTIFIER(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("hWnd", HWND),
            ("uID", UINT),
            ("guidItem", GUID)
        ]
    NOTIFYICONIDENTIFIER = _NOTIFYICONIDENTIFIER
    PNOTIFYICONIDENTIFIER = POINTER(NOTIFYICONIDENTIFIER)

    Shell_NotifyIconA = declare(shell32.Shell_NotifyIconA, VOID, DWORD, PNOTIFYICONDATAA)
    Shell_NotifyIconW = declare(shell32.Shell_NotifyIconW, VOID, DWORD, PNOTIFYICONDATAW)
    Shell_NotifyIcon = unicode(Shell_NotifyIconW, Shell_NotifyIconA)

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN7:
        Shell_NotifyIconGetRect = declare(shell32.Shell_NotifyIconGetRect, VOID, PNOTIFYICONIDENTIFIER, PRECT)

    ##
    ## End Taskbar Notification Icons
    ##
    if cpreproc.pragma_once("SHFILEINFO_DEFINED"):
        ##
        ## Begin SHGetFileInfo
        ##

        """

        * for a file given a pathname.
        *
        *   PARAMETERS
        *
        *     pszPath              file name to get info about
        *     dwFileAttributes     file attribs, only used with SHGFI_USEFILEATTRIBUTES
        *     psfi                 place to return file info
        *     cbFileInfo           size of structure
        *     uFlags               flags
        *
        *   RETURN
        *     TRUE if things worked

        """
        
        class _SHFILEINFOA(CStructure):
            _fields_ = [
                ("hIcon", HICON), #
                ("iIcon", INT), #
                ("dwAttributes", DWORD), #
                ("szDisplayName", CHAR * MAX_PATH), #
                ("szTypeName", CHAR * 80) #
            ]
        SHFILEINFOA = _SHFILEINFOA
        class _SHFILEINFOW(CStructure):
            _fields_ = [
                ("hIcon", HICON), #
                ("iIcon", INT), #
                ("dwAttributes", DWORD), #
                ("szDisplayName", WCHAR * MAX_PATH), #
                ("szTypeName", WCHAR * 80) #
            ]
        SHFILEINFOW = _SHFILEINFOW

        SHFILEINFO = unicode(SHFILEINFOW, SHFILEINFOA)

    # NOTE: This is also in shlwapi.h.  Please keep in synch.
    # !SHFILEINFO_DEFINED
    SHGFI_ICON = 0x000000100 # get icon
    SHGFI_DISPLAYNAME = 0x000000200 # get display name
    SHGFI_TYPENAME = 0x000000400 # get type name
    SHGFI_ATTRIBUTES = 0x000000800 # get attributes
    SHGFI_ICONLOCATION = 0x000001000 # get icon location
    SHGFI_EXETYPE = 0x000002000 # return exe type
    SHGFI_SYSICONINDEX = 0x000004000 # get system icon index
    SHGFI_LINKOVERLAY = 0x000008000 # put a link overlay on icon
    SHGFI_SELECTED = 0x000010000 # show icon in selected state
    SHGFI_ATTR_SPECIFIED = 0x000020000 # get only specified attributes
    SHGFI_LARGEICON = 0x000000000 # get large icon
    SHGFI_SMALLICON = 0x000000001 # get small icon
    SHGFI_OPENICON = 0x000000002 # get open icon
    SHGFI_SHELLICONSIZE = 0x000000004 # get shell size icon
    SHGFI_PIDL = 0x000000008 # pszPath is a pidl
    SHGFI_USEFILEATTRIBUTES = 0x000000010 # use passed dwFileAttribute
    SHGFI_ADDOVERLAYS = 0x000000020 # apply the appropriate overlays
    SHGFI_OVERLAYINDEX = 0x000000040 # Get the index of the overlay
    # in the upper 8 bits of the iIcon

    SHGetFileInfoA = declare(shell32.SHGetFileInfoA, DWORD_PTR, LPCSTR, DWORD, POINTER(SHFILEINFOA), UINT, UINT)
    SHGetFileInfoW = declare(shell32.SHGetFileInfoW, DWORD_PTR, LPCSTR, DWORD, POINTER(SHFILEINFOW), UINT, UINT)
    SHGetFileInfo = unicode(SHGetFileInfoW, SHGetFileInfoA)

    class _SHSTOCKICONINFO(CStructure):
        _fields_ = [
            ("cbSize", DWORD),
            ("hIcon", HICON),
            ("iSysImageIndex", INT),
            ("iIcon", INT),
            ("szPath", WCHAR * MAX_PATH)
        ]
    SHSTOCKICONINFO = _SHSTOCKICONINFO

    SHGSI_ICONLOCATION = 0 # you always get the icon location
    SHGSI_ICON = SHGFI_ICON
    SHGSI_SYSICONINDEX = SHGFI_SYSICONINDEX
    SHGSI_LINKOVERLAY = SHGFI_LINKOVERLAY
    SHGSI_SELECTED = SHGFI_SELECTED
    SHGSI_LARGEICON = SHGFI_LARGEICON
    SHGSI_SMALLICON = SHGFI_SMALLICON
    SHGSI_SHELLICONSIZE = SHGFI_SHELLICONSIZE

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        #  Shell icons
        SHSTOCKICONID = INT
        if True:
            SIID_DOCNOASSOC = 0          #  document (blank page), no associated program
            SIID_DOCASSOC = 1            #  document with an associated program
            SIID_APPLICATION = 2         #  generic application with no custom icon
            SIID_FOLDER = 3              #  folder (closed)
            SIID_FOLDEROPEN = 4          #  folder (open)
            SIID_DRIVE525 = 5            #  5.25" floppy disk drive
            SIID_DRIVE35 = 6             #  3.5" floppy disk drive
            SIID_DRIVEREMOVE = 7         #  removable drive
            SIID_DRIVEFIXED = 8          #  fixed (hard disk) drive
            SIID_DRIVENET = 9            #  network drive
            SIID_DRIVENETDISABLED = 10   #  disconnected network drive
            SIID_DRIVECD = 11            #  CD drive
            SIID_DRIVERAM = 12           #  RAM disk drive
            SIID_WORLD = 13              #  entire network
            SIID_SERVER = 15             #  a computer on the network
            SIID_PRINTER = 16            #  printer
            SIID_MYNETWORK = 17          #  My network places
            SIID_FIND = 22               #  Find
            SIID_HELP = 23               #  Help
            SIID_SHARE = 28              #  overlay for shared items
            SIID_LINK = 29               #  overlay for shortcuts to items
            SIID_SLOWFILE = 30           #  overlay for slow items
            SIID_RECYCLER = 31           #  empty recycle bin
            SIID_RECYCLERFULL = 32       #  full recycle bin
            SIID_MEDIACDAUDIO = 40       #  Audio CD Media
            SIID_LOCK = 47               #  Security lock
            SIID_AUTOLIST = 49           #  AutoList
            SIID_PRINTERNET = 50         #  Network printer
            SIID_SERVERSHARE = 51        #  Server share
            SIID_PRINTERFAX = 52         #  Fax printer
            SIID_PRINTERFAXNET = 53      #  Networked Fax Printer
            SIID_PRINTERFILE = 54        #  Print to File
            SIID_STACK = 55              #  Stack
            SIID_MEDIASVCD = 56          #  SVCD Media
            SIID_STUFFEDFOLDER = 57      #  Folder containing other items
            SIID_DRIVEUNKNOWN = 58       #  Unknown drive
            SIID_DRIVEDVD = 59           #  DVD Drive
            SIID_MEDIADVD = 60           #  DVD Media
            SIID_MEDIADVDRAM = 61        #  DVD-RAM Media
            SIID_MEDIADVDRW = 62         #  DVD-RW Media
            SIID_MEDIADVDR = 63          #  DVD-R Media
            SIID_MEDIADVDROM = 64        #  DVD-ROM Media
            SIID_MEDIACDAUDIOPLUS = 65   #  CD+ (Enhanced CD) Media
            SIID_MEDIACDRW = 66          #  CD-RW Media
            SIID_MEDIACDR = 67           #  CD-R Media
            SIID_MEDIACDBURN = 68        #  Burning CD
            SIID_MEDIABLANKCD = 69       #  Blank CD Media
            SIID_MEDIACDROM = 70         #  CD-ROM Media
            SIID_AUDIOFILES = 71         #  Audio files
            SIID_IMAGEFILES = 72         #  Image files
            SIID_VIDEOFILES = 73         #  Video files
            SIID_MIXEDFILES = 74         #  Mixed files
            SIID_FOLDERBACK = 75         #  Folder back
            SIID_FOLDERFRONT = 76        #  Folder front
            SIID_SHIELD = 77             #  Security shield. Use for UAC prompts only.
            SIID_WARNING = 78            #  Warning
            SIID_INFO = 79               #  Informational
            SIID_ERROR = 80              #  Error
            SIID_KEY = 81                #  Key / Secure
            SIID_SOFTWARE = 82           #  Software
            SIID_RENAME = 83             #  Rename
            SIID_DELETE = 84             #  Delete
            SIID_MEDIAAUDIODVD = 85      #  Audio DVD Media
            SIID_MEDIAMOVIEDVD = 86      #  Movie DVD Media
            SIID_MEDIAENHANCEDCD = 87    #  Enhanced CD Media
            SIID_MEDIAENHANCEDDVD = 88   #  Enhanced DVD Media
            SIID_MEDIAHDDVD = 89         #  HD-DVD Media
            SIID_MEDIABLURAY = 90        #  BluRay Media
            SIID_MEDIAVCD = 91           #  VCD Media
            SIID_MEDIADVDPLUSR = 92      #  DVD+R Media
            SIID_MEDIADVDPLUSRW = 93     #  DVD+RW Media
            SIID_DESKTOPPC = 94          #  desktop computer
            SIID_MOBILEPC = 95           #  mobile computer (laptop/notebook)
            SIID_USERS = 96              #  users
            SIID_MEDIASMARTMEDIA = 97    #  Smart Media
            SIID_MEDIACOMPACTFLASH = 98  #  Compact Flash
            SIID_DEVICECELLPHONE = 99    #  Cell phone
            SIID_DEVICECAMERA = 100      #  Camera
            SIID_DEVICEVIDEOCAMERA = 101 #  Video camera
            SIID_DEVICEAUDIOPLAYER = 102 #  Audio player
            SIID_NETWORKCONNECT = 103    #  Connect to network
            SIID_INTERNET = 104          #  Internet
            SIID_ZIPFILE = 105           #  ZIP file
            SIID_SETTINGS = 106          #  Settings
            # 107-131 are internal Vista RTM icons
            # 132-159 for SP1 icons
            SIID_DRIVEHDDVD = 132        #  HDDVD Drive (all types)
            SIID_DRIVEBD = 133           #  BluRay Drive (all types)
            SIID_MEDIAHDDVDROM = 134     #  HDDVD-ROM Media
            SIID_MEDIAHDDVDR = 135       #  HDDVD-R Media
            SIID_MEDIAHDDVDRAM = 136     #  HDDVD-RAM Media
            SIID_MEDIABDROM = 137        #  BluRay ROM Media
            SIID_MEDIABDR = 138          #  BluRay R Media
            SIID_MEDIABDRE = 139         #  BluRay RE Media (Rewriable and RAM)
            SIID_CLUSTEREDDRIVE = 140    #  Clustered disk
            # 160+ are for Windows 7 icons
            SIID_MAX_ICONS = 181

        SIID_INVALID = SHSTOCKICONID(-1)

        SHGetStockIconInfo = declare(shell32.SHGetStockIconInfo, VOID, SHSTOCKICONID, UINT, POINTER(SHSTOCKICONINFO))

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN2K:
        SHGetDiskFreeSpaceExA = declare(shell32.SHGetDiskFreeSpaceExA, BOOL, LPCSTR, PULARGE_INTEGER, PULARGE_INTEGER, PULARGE_INTEGER)
        SHGetDiskFreeSpaceExW = declare(shell32.SHGetDiskFreeSpaceExW, BOOL, LPCWSTR, PULARGE_INTEGER, PULARGE_INTEGER, PULARGE_INTEGER)
        SHGetDiskFreeSpaceEx = unicode(SHGetDiskFreeSpaceExW, SHGetDiskFreeSpaceExA)
        SHGetDiskFreeSpace = SHGetDiskFreeSpaceEx

        SHGetNewLinkInfoA = declare(shell32.SHGetNewLinkInfoA, LPCSTR, LPCSTR, LPSTR, PBOOL, UINT)
        SHGetNewLinkInfoW = declare(shell32.SHGetNewLinkInfoW, LPCWSTR, LPCWSTR, LPWSTR, PBOOL, UINT)
        SHGetNewLinkInfo = unicode(SHGetNewLinkInfoW, SHGetNewLinkInfoA)

        SHGNLI_PIDL = 0x000000001 # pszLinkTo is a pidl
        SHGNLI_PREFIXNAME = 0x000000002 # Make name "Shortcut to xxx"
        SHGNLI_NOUNIQUE = 0x000000004 # don't do the unique name generation
        SHGNLI_NOLNK = 0x000000008 # don't add ".lnk" extension
        SHGNLI_NOLOCNAME = 0x000000010 # use non localized (parsing) name from the target
        SHGNLI_USEURLEXT = 0x000000020 # use ".url" extension instead of ".lnk"
        # (NTDDI_VERSION >= NTDDI_WIN2K)
        PRINTACTION_OPEN = 0 # pszBuf1:<PrinterName>
        PRINTACTION_PROPERTIES = 1 # pszBuf1:<PrinterName>, pszBuf2:optional <PageName>
        PRINTACTION_NETINSTALL = 2 # pszBuf1:<NetPrinterName>
        PRINTACTION_NETINSTALLLINK = 3 # pszBuf1:<NetPrinterName>, pszBuf2:<path to store link>
        PRINTACTION_TESTPAGE = 4 # pszBuf1:<PrinterName>
        PRINTACTION_OPENNETPRN = 5 # pszBuf1:<NetPrinterName>
        PRINTACTION_DOCUMENTDEFAULTS = 6 # pszBuf1:<PrinterName>
        PRINTACTION_SERVERPROPERTIES = 7 # pszBuf1:<Server> or <NetPrinterName>
        # deprecated, instead invoke verbs on printers/netprinters using IContextMenu or ShellExecute()
        SHInvokePrinterCommandA = declare(shell32.SHInvokePrinterCommandA, BOOL, HWND, UINT, LPCSTR, LPCSTR, BOOL)
        SHInvokePrinterCommandW = declare(shell32.SHInvokePrinterCommandW, BOOL, HWND, UINT, LPCWSTR, LPCWSTR, BOOL)
        SHInvokePrinterCommand = unicode(SHInvokePrinterCommandW, SHInvokePrinterCommandA)
    # (NTDDI_VERSION >= NTDDI_WIN2K)
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        class _OPEN_PRINTER_PROPS_INFOA(CStructure):
            _fields_ = [
                ("dwSize", DWORD),
                ("pszSheetName", LPSTR),
                ("uSheetIndex", UINT),
                ("dwFlags", DWORD),
                ("bModal", BOOL)
            ]
        OPEN_PRINTER_PROPS_INFOA = _OPEN_PRINTER_PROPS_INFOA
        POPEN_PRINTER_PROPS_INFOA = POINTER(OPEN_PRINTER_PROPS_INFOA)

        class _OPEN_PRINTER_PROPS_INFOW(CStructure):
            _fields_ = [
                ("dwSize", DWORD),
                ("pszSheetName", LPSTR),
                ("uSheetIndex", UINT),
                ("dwFlags", DWORD),
                ("bModal", BOOL)
            ]
        OPEN_PRINTER_PROPS_INFOW = _OPEN_PRINTER_PROPS_INFOW
        POPEN_PRINTER_PROPS_INFOW = POINTER(OPEN_PRINTER_PROPS_INFOW)

        OPEN_PRINTER_PROPS_INFO = unicode(OPEN_PRINTER_PROPS_INFOW, OPEN_PRINTER_PROPS_INFOA)
        POPEN_PRINTER_PROPS_INFO = unicode(POPEN_PRINTER_PROPS_INFOW, POPEN_PRINTER_PROPS_INFOA)

        PRINT_PROP_FORCE_NAME = 0x01

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN2K:

            #
            # The SHLoadNonloadedIconOverlayIdentifiers API causes the shell's
            # icon overlay manager to load any registered icon overlay
            # identifers that are not currently loaded.  This is useful if an
            # overlay identifier did not load at shell startup but is needed
            # and can be loaded at a later time.  Identifiers already loaded
            # are not affected.  Overlay identifiers implement the
            # IShellIconOverlayIdentifier interface.
            #
            # Returns:
            #      S_OK
            #
            SHLoadNonloadedIconOverlayIdentifiers = declare(shell32.SHLoadNonloadedIconOverlayIdentifiers, VOID, VOID)

            #
            # The SHIsFileAvailableOffline API determines whether a file
            # or folder is available for offline use.
            #
            # Parameters:
            #     pwszPath             file name to get info about
            #     pdwStatus            (optional) OFFLINE_STATUS_* flags returned here
            #
            # Returns:
            #     S_OK                 File/directory is available offline, unless
            #                            OFFLINE_STATUS_INCOMPLETE is returned.
            #     E_INVALIDARG         Path is invalid, or not a net path
            #     E_FAIL               File/directory is not available offline
            #
            # Notes:
            #     OFFLINE_STATUS_INCOMPLETE is never returned for directories.
            #     Both OFFLINE_STATUS_LOCAL and OFFLINE_STATUS_REMOTE may be returned,
            #     indicating "open in both places." This is common when the server is online.
            #
            SHIsFileAvailableOffline = declare(shell32.SHIsFileAvailableOffline, VOID, PCWSTR, PDWORD)

            #define OFFLINE_STATUS_LOCAL        0x0001  # If open, it's open locally
            #define OFFLINE_STATUS_REMOTE       0x0002  # If open, it's open remotely
            #define OFFLINE_STATUS_INCOMPLETE   0x0004  # The local copy is currently imcomplete.
                                                        # The file will not be available offline
                                                        # until it has been synchronized.

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
            #  sets the specified path to use the string resource
            #  as the UI instead of the file system name
            SHSetLocalizedName = declare(shell32.SHSetLocalizedName, VOID, PCWSTR, PCWSTR, INT)
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            #  sets the specified path to use the string resource
            #  as the UI instead of the file system name
            SHRemoveLocalizedName = declare(shell32.SHRemoveLocalizedName, VOID, PCWSTR)
            #  gets the string resource for the specified path
            SHGetLocalizedName = declare(shell32.SHGetLocalizedName, VOID, PCWSTR, PWSTR, UINT, PINT)


        #====== ShellMessageBox ================================================

        # If lpcTitle is NULL, the title is taken from hWnd
        # If lpcText is NULL, this is assumed to be an Out Of Memory message
        # If the selector of lpcTitle or lpcText is NULL, the offset should be a
        #     string resource ID
        # The variable arguments must all be 32-bit values (even if fewer bits
        #     are actually used)
        # lpcText (or whatever string resource it causes to be loaded) should
        #     be a formatting string similar to wsprintf except that only the
        #     following formats are available:
        #         %%              formats to a single '%'
        #         %nn%s           the nn-th arg is a string which is inserted
        #         %nn%ld          the nn-th arg is a DWORD, and formatted decimal
        #         %nn%lx          the nn-th arg is a DWORD, and formatted hex
        #     note that lengths are allowed on the %s, %ld, and %lx, just
        #                         like wsprintf
        #

        ShellMessageBoxA = declare(shell32.ShellMessageBoxA, INT, HINSTANCE, HWND, LPCSTR, LPCSTR, UINT)
        ShellMessageBoxW = declare(shell32.ShellMessageBoxW, INT, HINSTANCE, HWND, LPCWSTR, LPCWSTR, UINT)
        ShellMessageBox = unicode(ShellMessageBoxW, ShellMessageBoxA)

        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN2K:
            IsLFNDriveA = declare(shell32.IsLFNDriveA, BOOL, LPCSTR)
            IsLFNDriveW = declare(shell32.IsLFNDriveW, BOOL, LPCWSTR)
            IsLFNDrive = unicode(IsLFNDriveW, IsLFNDriveA)


        if WIN32_IE >= WIN32_IE_IE60:
            #SHEnumerateUnreadMailAccountsA = declare(shell32.SHEnumerateUnreadMailAccountsA, VOID, HKEY, DWORD, LPSTR, INT)
            SHEnumerateUnreadMailAccountsW = declare(shell32.SHEnumerateUnreadMailAccountsW, VOID, HKEY, DWORD, LPWSTR, INT)
            SHEnumerateUnreadMailAccounts = SHEnumerateUnreadMailAccountsW

            #SHGetUnreadMailCountA = declare(shell32.SHGetUnreadMailCountA, VOID, HKEY, LPCSTR, PDWORD, PFILETIME, LPSTR, INT)
            SHGetUnreadMailCountW = declare(shell32.SHGetUnreadMailCountW, VOID, HKEY, LPCWSTR, PDWORD, PFILETIME, LPWSTR, INT)
            SHGetUnreadMailCount = SHGetUnreadMailCountW
            
            #SHSetUnreadMailCountA = declare(shell32.SHSetUnreadMailCountA, VOID, LPCSTR, DWORD, LPCSTR)
            SHSetUnreadMailCountW = declare(shell32.SHSetUnreadMailCountW, VOID, LPCWSTR, DWORD, LPCWSTR)
            SHSetUnreadMailCount = SHSetUnreadMailCountW

        if WIN32_IE >= WIN32_IE_IE60SP1:
            SHTestTokenMembership = declare(shell32.SHTestTokenMembership, BOOL, HANDLE, ULONG)

        if WIN32_IE >= WIN32_IE_IE60:
            if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
                SHGetImageList = declare(shell32.SHGetImageList, VOID, INT, POINTER(IID), PPVOID)

                SHIL_LARGE = 0 # normally 32x32
                SHIL_SMALL = 1 # normally 16x16
                SHIL_EXTRALARGE = 2
                SHIL_SYSSMALL = 3 # like SHIL_SMALL, but tracks system small icon metric correctly
                if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
                    SHIL_JUMBO = 4 # normally 256x256
                    SHIL_LAST = SHIL_JUMBO
            PFNCANSHAREFOLDERW = CALLBACK(HRESULT, PCWSTR)
            PFNSHOWSHAREFOLDERUIW = CALLBACK(HRESULT, HWND, PCWSTR)
        if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
            # API for new Network Address Control

            # Instantiation
            WC_NETADDRESS = u"msctls_netaddress"
            InitNetworkAddressControl = declare(shell32.InitNetworkAddressControl, BOOL, VOID)

            # Address Control Messages

            # NCM_GETADDRESS returns the type of address that is present in the
            # control (based on TBD Net Address flags).  If the input string has
            # not been validated using this message will force the validation of
            # the input string.  The WPARAM is a BOOL to determine to show the
            # balloon tip.  The LPARAM is a pointer to the structure to fill in
            # with the address type and address string.
            NCM_GETADDRESS = (WM_USER+1)

            def NetAddr_GetAddress(hwnd,pv):
                return SendMessage(hwnd, NCM_GETADDRESS, 0, cast(pv, PVOID).value)
            
            if cpreproc.ifdef("__IPHLPAPI_H__"):
                from .iphlpapi import PNET_ADDRESS_INFO_
                class tagNC_ADDRESS(CStructure):
                    _fields_ = [
                        ("pAddrInfo", PNET_ADDRESS_INFO_), # defined in iphlpapi.h
                        ("PortNumber", USHORT),
                        ("PrefixLength", BYTE)
                    ]
                NC_ADDRESS = tagNC_ADDRESS
                PNC_ADDRESS = POINTER(NC_ADDRESS)

                # NCM_SETALLOWTYPE sets the type of addresses that the control will allow.
                # The address flags are defined in iphlpapi.h
                NCM_SETALLOWTYPE = (WM_USER+2)

                def NetAddr_SetAllowType(hwnd,addrMask):
                    return SendMessage(hwnd, NCM_SETALLOWTYPE, addrMask, 0)
                
                # NCM_GETALLOWTYPE returns the currently allowed type mask.
                NCM_GETALLOWTYPE = (WM_USER+3)

                def NetAddr_GetAllowType(hwnd):
                    return SendMessage(hwnd, NCM_GETALLOWTYPE, 0, 0)

                # NCM_DISPLAYERRORTIP displays the error balloon tip with the correct
                # error string (based on the last failure from the NCM_GETADDRESS call
                NCM_DISPLAYERRORTIP = (WM_USER+4)

                def NetAddr_DisplayErrorTip(hwnd):
                    return SendMessage(hwnd, NCM_DISPLAYERRORTIP, 0, 0)

            # Returns the type of media (CD, DVD, Blank, etc) that is in the drive.
            # dwMediaContent is set to a combination of ARCONTENT flags.
            SHGetDriveMedia = declare(shell32.SHGetDriveMedia, VOID, PCWSTR, PDWORD)