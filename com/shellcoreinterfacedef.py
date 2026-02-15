#
# shellcoreinterfacedef.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sat Feb 14 16:12:42 2026
# Generated from ICL: shellcoreinterfacedef.icl
#

from .ctlinterfacedef import *
from .objectarray import *
from ..shtypes import *
from ..shellapi import *

CMF_NORMAL = 0x00000000
CMF_DEFAULTONLY = 0x00000001
CMF_VERBSONLY = 0x00000002
CMF_EXPLORE = 0x00000004
CMF_NOVERBS = 0x00000008
CMF_CANRENAME = 0x00000010
CMF_NODEFAULT = 0x00000020

from ..sdkddkver import *
_version = cpreproc.get_version()

if _version < WIN32_WINNT_VISTA:
    CMF_INCLUDESTATIC = 0x00000040

if _version >= WIN32_WINNT_VISTA:
    CMF_ITEMMENU = 0x00000080

CMF_EXTENDEDVERBS = 0x00000100

if _version >= WIN32_WINNT_VISTA:
    CMF_DISABLEDVERBS = 0x00000200

CMF_ASYNCVERBSTATE = 0x00000400
CMF_OPTIMIZEFORINVOKE = 0x00000800
CMF_SYNCCASCADEMENU = 0x00001000
CMF_DONOTPICKDEFAULT = 0x00002000
CMF_RESERVED = 0xffff0000

GCS_VERBA = 0x00000000
GCS_HELPTEXTA = 0x00000001
GCS_VALIDATEA = 0x00000002
GCS_VERBW = 0x00000004
GCS_HELPTEXTW = 0x00000005
GCS_VALIDATEW = 0x00000006
GCS_VERBICONW = 0x00000014
GCS_UNICODE = 0x00000004

if cpreproc.ifdef("UNICODE"):
    GCS_VERB = GCS_VERBW
    GCS_HELPTEXT = GCS_HELPTEXTW
    GCS_VALIDATE = GCS_VALIDATEW
else:
    GCS_VERB = GCS_VERBA
    GCS_HELPTEXT = GCS_HELPTEXTA
    GCS_VALIDATE = GCS_VALIDATEA

CMDSTR_NEWFOLDERA = b"NewFolder"
CMDSTR_VIEWLISTA = b"ViewList"
CMDSTR_VIEWDETAILSA = b"ViewDetails"
CMDSTR_NEWFOLDERW = "NewFolder"
CMDSTR_VIEWLISTW = "ViewList"
CMDSTR_VIEWDETAILSW = "ViewDetails"

if cpreproc.ifdef("UNICODE"):
    CMDSTR_NEWFOLDER = CMDSTR_NEWFOLDERW
    CMDSTR_VIEWLIST = CMDSTR_VIEWLISTW
    CMDSTR_VIEWDETAILS = CMDSTR_VIEWDETAILSW
else:
    CMDSTR_NEWFOLDER = CMDSTR_NEWFOLDERA
    CMDSTR_VIEWLIST = CMDSTR_VIEWLISTA
    CMDSTR_VIEWDETAILS = CMDSTR_VIEWDETAILSA

CMIC_MASK_HOTKEY = SEE_MASK_HOTKEY
CMIC_MASK_ICON = SEE_MASK_ICON
CMIC_MASK_FLAG_NO_UI = SEE_MASK_FLAG_NO_UI
CMIC_MASK_UNICODE = SEE_MASK_UNICODE
CMIC_MASK_NO_CONSOLE = SEE_MASK_NO_CONSOLE
CMIC_MASK_ASYNCOK = SEE_MASK_ASYNCOK
if _version >= WIN32_WINNT_VISTA:
    CMIC_MASK_NOASYNC = SEE_MASK_NOASYNC

CMIC_MASK_SHIFT_DOWN = 0x10000000
CMIC_MASK_CONTROL_DOWN = 0x40000000
CMIC_MASK_FLAG_LOG_USAGE = SEE_MASK_FLAG_LOG_USAGE
CMIC_MASK_NOZONECHECKS = SEE_MASK_NOZONECHECKS
CMIC_MASK_PTINVOKE = 0x20000000

@CStructure.make
class CMINVOKECOMMANDINFO(CStructure):
    cbSize: IDword
    fMask: IDword
    hwnd: IHandle
    lpVerb: LPCSTR
    lpParameters: LPCSTR
    lpDirectory: LPCSTR
    nShow: IInt
    dwHotKey: IDword
    hIcon: IHandle

LPCMINVOKECOMMANDINFO = PCCMINVOKECOMMANDINFO = CMINVOKECOMMANDINFO.PTR()

@CStructure.make
class CMINVOKECOMMANDINFOEX(CStructure):
    cbSize: IDword
    fMask: IDword
    hwnd: IHandle
    lpVerb: LPCSTR
    lpParameters: LPCSTR
    lpDirectory: LPCSTR
    nShow: IInt
    dwHotKey: IDword
    hIcon: IHandle
    lpTitle: LPCSTR
    lpVerbW: LPCWSTR
    lpParametersW: LPCWSTR
    lpDirectoryW: LPCWSTR
    lpTitleW: LPCWSTR
    ptInvoke: POINT

LPCMINVOKECOMMANDINFOEX = PCCMINVOKECOMMANDINFO = CMINVOKECOMMANDINFOEX.PTR()

@CStructure.make
class CMINVOKECOMMANDINFOEX_REMOTE(CStructure):
    cbSize: IDword
    fMask: IDword
    hwnd: IHandle
    lpVerbString: LPCSTR
    lpParameters: LPCSTR
    lpDirectory: LPCSTR
    nShow: IInt
    dwHotKey: IDword
    lpTitle: LPCSTR
    lpVerbWString: LPCWSTR
    lpParametersW: LPCWSTR
    lpDirectoryW: LPCWSTR
    lpTitleW: LPCWSTR
    ptInvoke: POINT
    lpVerbInt: IUInt
    lpVerbWInt: IUInt

class IContextMenu(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214e4-0000-0000-c000-000000000046}")

    @virtual_table.com_function(HMENU, UINT, UINT, UINT, UINT)
    def QueryContextMenu(self, hmenu: HMENU, indexMenu: int, idCmdFirst: int, idCmdLast: int, uFlags: int) -> int: ...

    @virtual_table.com_function(LPCMINVOKECOMMANDINFO)
    def InvokeCommand(self, pici: IPointer[CMINVOKECOMMANDINFO]) -> int: ...

    @virtual_table.com_function(UINT_PTR, UINT, PUINT, LPSTR, UINT)
    def GetCommandString(self, idCmd: int, uType: int, pReserved: PUINT, pszName: LPSTR, cchMax: int) -> int: ...

    virtual_table.build()

LPCONTEXTMENU = IContextMenu.PTR()

class IContextMenu2(IContextMenu):
    virtual_table = COMVirtualTable.from_ancestor(IContextMenu)
    _iid_ = IID("{000214f4-0000-0000-c000-000000000046}")

    @virtual_table.com_function(UINT, WPARAM, LPARAM)
    def HandleMenuMsg(self, uMsg: int, wParam: int, lParam: int) -> int: ...

    virtual_table.build()

LPCONTEXTMENU2 = IContextMenu2.PTR()

class IContextMenu3(IContextMenu2):
    virtual_table = COMVirtualTable.from_ancestor(IContextMenu2)
    _iid_ = IID("{BCFCE0A0-EC17-11d0-8D10-00A0C90F2719}")

    @virtual_table.com_function(UINT, WPARAM, LPARAM, PTR(LRESULT))
    def HandleMenuMsg2(self, uMsg: int, wParam: int, lParam: int, plResult: IPointer[LRESULT]) -> int: ...

    virtual_table.build()

LPCONTEXTMENU3 = IContextMenu3.PTR()

class IStaticVerbProvider(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{4B770DA6-D111-4015-96FD-8C1C56F06C55}")

    @virtual_table.com_function(LPCWSTR, PBOOL)
    def IsVerbSupported(self, verbName: LPCWSTR, result: PBOOL) -> int: ...

    virtual_table.build()

class IExecuteCommand(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7F9185B0-CB92-43c5-80A9-92277A4F7B54}")

    @virtual_table.com_function(DWORD)
    def SetKeyState(self, grfKeyState: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetParameters(self, pszParameters: LPCWSTR) -> int: ...

    @virtual_table.com_function(POINT)
    def SetPosition(self, pt: POINT) -> int: ...

    @virtual_table.com_function(INT)
    def SetShowWindow(self, nShow: int) -> int: ...

    @virtual_table.com_function(BOOL)
    def SetNoShowUI(self, fNoShowUI: bool) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetDirectory(self, pszDirectory: LPCWSTR) -> int: ...

    @virtual_table.com_function
    def Execute(self) -> int: ...

    virtual_table.build()

class IPersistFolder(IPersist):
    virtual_table = COMVirtualTable.from_ancestor(IPersist)
    _iid_ = IID("{000214ea-0000-0000-c000-000000000046}")

    @virtual_table.com_function(PIDLIST_ABSOLUTE)
    def Initialize(self, pidl: IPointer[ITEMIDLIST_ABSOLUTE]) -> int: ...

    virtual_table.build()

LPPERSISTFOLDER = IPersistFolder.PTR()

IRTIR_TASK_NOT_RUNNING = 0
IRTIR_TASK_RUNNING = 1
IRTIR_TASK_SUSPENDED = 2
IRTIR_TASK_PENDING = 3
IRTIR_TASK_FINISHED = 4
class IRunnableTask(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{85788d00-6807-11d0-b810-00c04fd706ec}")

    @virtual_table.com_function
    def Run(self) -> int: ...

    @virtual_table.com_function(BOOL)
    def Kill(self, bWait: bool) -> int: ...

    @virtual_table.com_function
    def Suspend(self) -> int: ...

    @virtual_table.com_function
    def Resume(self) -> int: ...

    @virtual_table.function(ULONG)
    def IsRunning(self) -> int: ...

    virtual_table.build()

TOID_NULL = GUID_NULL
ITSAT_DEFAULT_LPARAM = DWORD_PTR(-1).value
ITSAT_DEFAULT_PRIORITY = 0x10000000
ITSAT_MAX_PRIORITY = 0x7fffffff
ITSAT_MIN_PRIORITY = 0x00000000
ITSSFLAG_COMPLETE_ON_DESTROY = 0x0000
ITSSFLAG_KILL_ON_DESTROY = 0x0001
ITSSFLAG_FLAGS_MASK = 0x0003
ITSS_THREAD_DESTROY_DEFAULT_TIMEOUT = (10*1000)
INFINITE = 0xFFFFFFFF
ITSS_THREAD_TERMINATE_TIMEOUT = (INFINITE)
ITSS_THREAD_TIMEOUT_NO_CHANGE = (INFINITE-1)

class IShellTaskScheduler(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{6CCB7BE0-6807-11d0-B810-00C04FD706EC}")

    @virtual_table.com_function(PTR(IRunnableTask), REFTASKOWNERID, DWORD_PTR, DWORD)
    def AddTask(self, prt: IPointer[IRunnableTask], rtoid: IPointer[TASKOWNERID], lParam: int, dwPriority: int) -> int: ...

    @virtual_table.com_function(REFTASKOWNERID, DWORD_PTR, BOOL)
    def RemoveTasks(self, rtoid: IPointer[TASKOWNERID], lParam: int, bWaitIfRunning: bool) -> int: ...

    @virtual_table.com_function(REFTASKOWNERID)
    def CountTasks(self, rtoid: IPointer[TASKOWNERID]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD)
    def Status(self, dwReleaseStatus: int, dwThreadTimeout: int) -> int: ...

    virtual_table.build()

class IPersistFolder2(IPersistFolder):
    virtual_table = COMVirtualTable.from_ancestor(IPersistFolder)
    _iid_ = IID("{1AC3D9F0-175C-11d1-95BE-00609797EA4F}")

    @virtual_table.com_function(PTR(PIDLIST_ABSOLUTE))
    def GetCurFolder(self, ppidl: IDoublePtr[ITEMIDLIST_ABSOLUTE]) -> int: ...

    virtual_table.build()

@CStructure.make
class PERSIST_FOLDER_TARGET_INFO(CStructure):
    pidlTargetFolder: IPointer[ITEMIDLIST_ABSOLUTE]
    szTargetParsingName: IWideCharArrayFixedSize[260]
    szNetworkProvider: IWideCharArrayFixedSize[260]
    dwAttributes: IDword
    csidl: IInt

class IPersistFolder3(IPersistFolder2):
    virtual_table = COMVirtualTable.from_ancestor(IPersistFolder2)
    _iid_ = IID("{CEF04FDF-FE72-11d2-87A5-00C04F6837CF}")

    @virtual_table.com_function(LPBINDCTX, PIDLIST_ABSOLUTE, PTR(PERSIST_FOLDER_TARGET_INFO))
    def InitializeEx(self, pbc: IPointer[IBindCtx], pidlRoot: IPointer[ITEMIDLIST_ABSOLUTE], ppfti: IPointer[PERSIST_FOLDER_TARGET_INFO]) -> int: ...

    @virtual_table.com_function(PTR(PERSIST_FOLDER_TARGET_INFO))
    def GetFolderTargetInfo(self, ppfti: IPointer[PERSIST_FOLDER_TARGET_INFO]) -> int: ...

    virtual_table.build()

class IPersistIDList(IPersist):
    virtual_table = COMVirtualTable.from_ancestor(IPersist)
    _iid_ = IID("{1079acfc-29bd-11d3-8e0d-00c04f6837d5}")

    @virtual_table.com_function(PIDLIST_ABSOLUTE)
    def SetIDList(self, pidl: IPointer[ITEMIDLIST_ABSOLUTE]) -> int: ...

    @virtual_table.com_function(PTR(PIDLIST_ABSOLUTE))
    def GetIDList(self, ppidl: IDoublePtr[ITEMIDLIST_ABSOLUTE]) -> int: ...

    virtual_table.build()

class IEnumIDList(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214F2-0000-0000-C000-000000000046}")

    @virtual_table.com_function(ULONG, PTR(PITEMID_CHILD), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[ITEMID_CHILD], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumIDList']) -> int: ...

    virtual_table.build()

LPENUMIDLIST = IEnumIDList.PTR()

class IEnumFullIDList(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{d0191542-7954-4908-bc06-b2360bbe45ba}")

    @virtual_table.com_function(ULONG, PTR(PIDLIST_ABSOLUTE), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[ITEMIDLIST_ABSOLUTE], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumFullIDList']) -> int: ...

    virtual_table.build()

SHGDN_NORMAL = 0
SHGDN_INFOLDER = 0x1
SHGDN_FOREDITING = 0x1000
SHGDN_FORADDRESSBAR = 0x4000
SHGDN_FORPARSING = 0x8000
SHGDNF = INT

SHCONTF_CHECKING_FOR_CHILDREN = 0x10
SHCONTF_FOLDERS = 0x20
SHCONTF_NONFOLDERS = 0x40
SHCONTF_INCLUDEHIDDEN = 0x80
SHCONTF_INIT_ON_FIRST_NEXT = 0x100
SHCONTF_NETPRINTERSRCH = 0x200
SHCONTF_SHAREABLE = 0x400
SHCONTF_STORAGE = 0x800
SHCONTF_NAVIGATION_ENUM = 0x1000
SHCONTF_FASTITEMS = 0x2000
SHCONTF_FLATLIST = 0x4000
SHCONTF_ENABLE_ASYNC = 0x8000
SHCONTF_INCLUDESUPERHIDDEN = 0x10000
SHCONTF = INT

SHCIDS_ALLFIELDS = 0x80000000
SHCIDS_CANONICALONLY = 0x10000000
SHCIDS_BITMASK = 0xFFFF0000
SHCIDS_COLUMNMASK = 0x0000FFFF
SFGAO_CANCOPY = DROPEFFECT_COPY
SFGAO_CANMOVE = DROPEFFECT_MOVE
SFGAO_CANLINK = DROPEFFECT_LINK
SFGAO_STORAGE = 0x00000008
SFGAO_CANRENAME = 0x00000010
SFGAO_CANDELETE = 0x00000020
SFGAO_HASPROPSHEET = 0x00000040
SFGAO_DROPTARGET = 0x00000100
SFGAO_CAPABILITYMASK = 0x00000177
SFGAO_PLACEHOLDER = 0x00000800
SFGAO_SYSTEM = 0x00001000
SFGAO_ENCRYPTED = 0x00002000
SFGAO_ISSLOW = 0x00004000
SFGAO_GHOSTED = 0x00008000
SFGAO_LINK = 0x00010000
SFGAO_SHARE = 0x00020000
SFGAO_READONLY = 0x00040000
SFGAO_HIDDEN = 0x00080000
SFGAO_DISPLAYATTRMASK = 0x000FC000
SFGAO_FILESYSANCESTOR = 0x10000000
SFGAO_FOLDER = 0x20000000
SFGAO_FILESYSTEM = 0x40000000
SFGAO_HASSUBFOLDER = 0x80000000
SFGAO_CONTENTSMASK = 0x80000000
SFGAO_VALIDATE = 0x01000000
SFGAO_REMOVABLE = 0x02000000
SFGAO_COMPRESSED = 0x04000000
SFGAO_BROWSABLE = 0x08000000
SFGAO_NONENUMERATED = 0x00100000
SFGAO_NEWCONTENT = 0x00200000
SFGAO_CANMONIKER = 0x00400000
SFGAO_HASSTORAGE = 0x00400000
SFGAO_STREAM = 0x00400000
SFGAO_STORAGEANCESTOR = 0x00800000
SFGAO_STORAGECAPMASK = 0x70C50008
SFGAO_PKEYSFGAOMASK = 0x81044000
SFGAOF = ULONG

STS_NONE = 0
STS_NEEDSUPLOAD = 0x1
STS_NEEDSDOWNLOAD = 0x2
STS_TRANSFERRING = 0x4
STS_PAUSED = 0x8
STS_HASERROR = 0x10
STS_FETCHING_METADATA = 0x20
STS_USER_REQUESTED_REFRESH = 0x40
STS_HASWARNING = 0x80
STS_EXCLUDED = 0x100
STS_INCOMPLETE = 0x200
STS_PLACEHOLDER_IFEMPTY = 0x400
SYNC_TRANSFER_STATUS = INT

SPFF_NONE = 0
SPFF_DOWNLOAD_BY_DEFAULT = 1
SPFF_CREATED_ON_THIS_DEVICE = 2
STORAGE_PROVIDER_FILE_FLAGS = INT

PS_NONE = 0
PS_MARKED_FOR_OFFLINE_AVAILABILITY = 0x1
PS_FULL_PRIMARY_STREAM_AVAILABLE = 0x2
PS_CREATE_FILE_ACCESSIBLE = 0x4
PS_CLOUDFILE_PLACEHOLDER = 0x8
PS_DEFAULT = ((PS_MARKED_FOR_OFFLINE_AVAILABILITY|PS_FULL_PRIMARY_STREAM_AVAILABLE)|PS_CREATE_FILE_ACCESSIBLE)
PS_ALL = (((PS_MARKED_FOR_OFFLINE_AVAILABILITY|PS_FULL_PRIMARY_STREAM_AVAILABLE)|PS_CREATE_FILE_ACCESSIBLE)|PS_CLOUDFILE_PLACEHOLDER)
PLACEHOLDER_STATES = INT

MUS_COMPLETE = 0
MUS_USERINPUTNEEDED = 1
MUS_FAILED = 2
MERGE_UPDATE_STATUS = INT

class IFileSyncMergeHandler(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{d97b5aac-c792-433c-975d-35c4eadc7a9d}")

    @virtual_table.com_function(LPCWSTR, LPCWSTR, PTR(MERGE_UPDATE_STATUS))
    def Merge(self, localFilePath: LPCWSTR, serverFilePath: LPCWSTR, updateStatus: IPointer[MERGE_UPDATE_STATUS]) -> int: ...

    @virtual_table.com_function(LPCWSTR, HMONITOR)
    def ShowResolveConflictUIAsync(self, localFilePath: LPCWSTR, monitorToDisplayOn: HMONITOR) -> int: ...

    virtual_table.build()

STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE = "Force Folder Shortcut Resolve"
STR_AVOID_DRIVE_RESTRICTION_POLICY = "Avoid Drive Restriction Policy"
STR_AVOID_DRIVE_RESTRICTION_POLICY = "Avoid Drive Restriction Policy"
STR_SKIP_BINDING_CLSID = "Skip Binding CLSID"
STR_PARSE_PREFER_FOLDER_BROWSING = "Parse Prefer Folder Browsing"
STR_DONT_PARSE_RELATIVE = "Don't Parse Relative"
STR_PARSE_TRANSLATE_ALIASES = "Parse Translate Aliases"
STR_PARSE_SKIP_NET_CACHE = "Skip Net Resource Cache"
STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS = "Parse Shell Protocol To File Objects"

if WIN32_IE >= WIN32_IE_IE70:
    STR_TRACK_CLSID = "Track the CLSID"
    STR_INTERNAL_NAVIGATE = "Internal Navigation"
    STR_PARSE_PROPERTYSTORE = "DelegateNamedProperties"
    STR_NO_VALIDATE_FILENAME_CHARS = "NoValidateFilenameChars"
    STR_BIND_DELEGATE_CREATE_OBJECT = "Delegate Object Creation"
    STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS = "Allow binding to Internet shell folder handlers and negate STR_PARSE_PREFER_WEB_BROWSING"
    STR_PARSE_PREFER_WEB_BROWSING = "Do not bind to Internet shell folder handlers"
    STR_PARSE_SHOW_NET_DIAGNOSTICS_UI = "Show network diagnostics UI"
    STR_PARSE_DONT_REQUIRE_VALIDATED_URLS = "Do not require validated URLs"
    STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE = "Validate UR"

if _version >= WIN32_WINNT_WIN8:
    BIND_INTERRUPTABLE = 0xFFFFFFFF

if _version >= WIN32_WINNT_WIN7:
    STR_BIND_FOLDERS_READ_ONLY = "Folders As Read Only"
    STR_BIND_FOLDER_ENUM_MODE = "Folder Enum Mode"

    FEM_VIEWRESULT = 0
    FEM_NAVIGATION = 1
    FOLDER_ENUM_MODE = INT

    class IObjectWithFolderEnumMode(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{6a9d9026-0e6e-464c-b000-42ecc07de673}")

        @virtual_table.com_function(FOLDER_ENUM_MODE)
        def SetMode(self, feMode: int) -> int: ...

        @virtual_table.com_function(PTR(FOLDER_ENUM_MODE))
        def GetMode(self, pfeMode: IPointer[FOLDER_ENUM_MODE]) -> int: ...

        virtual_table.build()

    STR_PARSE_WITH_EXPLICIT_PROGID = "ExplicitProgid"
    STR_PARSE_WITH_EXPLICIT_ASSOCAPP = "ExplicitAssociationApp"
    STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL = "ExplicitAssociationSuccessfu"
    STR_PARSE_AND_CREATE_ITEM = "ParseAndCreateItem"
    STR_PROPERTYBAG_PARAM = "SHBindCtxPropertyBag"
    STR_ENUM_ITEMS_FLAGS = "SHCONTF"
    STR_STORAGEITEM_CREATION_FLAGS = "SHGETSTORAGEITEM"

    class IParseAndCreateItem(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{67efed0e-e827-4408-b493-78f3982b685c}")

        @virtual_table.com_function(PVOID)
        def SetItem(self, psi: IPointer['IShellItem']) -> int: ...

        @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
        def GetItem(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid, ppv)

        virtual_table.build()

    STR_ITEM_CACHE_CONTEXT = "ItemCacheContext"

class IShellFolder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214E6-0000-0000-C000-000000000046}")

    @virtual_table.com_function(HWND, LPBINDCTX, LPWSTR, PULONG, DOUBLE_PTR(ITEMIDLIST_RELATIVE), PULONG)
    def ParseDisplayName(self, hwnd: HWND, pbc: IPointer[IBindCtx], pszDisplayName: LPWSTR, pchEaten: PULONG, ppidl: IDoublePtr[ITEMIDLIST_RELATIVE], pdwAttributes: PULONG) -> int: ...

    @virtual_table.com_function(HWND, SHCONTF, DOUBLE_PTR(IEnumIDList))
    def EnumObjects(self, hwnd: HWND, grfFlags: int, ppenumIDList: IDoublePtr[IEnumIDList]) -> int: ...

    @virtual_table.com_function(PTR(ITEMIDLIST_RELATIVE), LPBINDCTX, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToObject(self, pidl: IPointer[ITEMIDLIST_RELATIVE], pbc: IPointer[IBindCtx], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pidl, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PTR(ITEMIDLIST_RELATIVE), LPBINDCTX, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToStorage(self, pidl: IPointer[ITEMIDLIST_RELATIVE], pbc: IPointer[IBindCtx], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pidl, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPARAM, PTR(ITEMIDLIST_RELATIVE), PTR(ITEMIDLIST_RELATIVE))
    def CompareIDs(self, lParam: int, pidl1: IPointer[ITEMIDLIST_RELATIVE], pidl2: IPointer[ITEMIDLIST_RELATIVE]) -> int: ...

    @virtual_table.com_function(HWND, LPIID, PVOID, PVOID, intermediate_method = True)
    def CreateViewObject(self, hwndOwner: HWND, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(UINT, PTR(PITEMID_CHILD), PTR(SFGAOF))
    def GetAttributesOf(self, cidl: int, apidl: IDoublePtr[ITEMID_CHILD], rgfInOut: IPointer[SFGAOF]) -> int: ...

    @virtual_table.com_function(HWND, UINT, PTR(PITEMID_CHILD), LPIID, PUINT, PVOID, PVOID, intermediate_method = True)
    def GetUIObjectOf(self, hwndOwner: HWND, cidl: int, apidl: IDoublePtr[ITEMID_CHILD], iid: IID, rgfReserved: PUINT, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(hwndOwner, cidl, iid.ref() if iid else NULL, iid, rgfReserved, ppv)

    @virtual_table.com_function(PITEMID_CHILD, SHGDNF, LPSTRRET)
    def GetDisplayNameOf(self, pidl: IPointer[ITEMID_CHILD], uFlags: int, pName: IPointer[STRRET]) -> int: ...

    @virtual_table.com_function(HWND, PITEMID_CHILD, LPCWSTR, SHGDNF, PTR(PITEMID_CHILD))
    def SetNameOf(self, hwnd: HWND, pidl: IPointer[ITEMID_CHILD], pszName: LPCWSTR, uFlags: int, ppidlOut: IDoublePtr[ITEMID_CHILD]) -> int: ...

    virtual_table.build()

LPSHELLFOLDER = IShellFolder.PTR()

@CStructure.make
class EXTRASEARCH(CStructure):
    guidSearch: GUID
    wszFriendlyName: IWideCharArrayFixedSize[80]
    wszUrl: IWideCharArrayFixedSize[2084]

LPEXTRASEARCH = EXTRASEARCH.PTR()

class IEnumExtraSearch(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{0E700BE1-9DB6-11d1-A1CE-00C04FD75D13}")

    @virtual_table.com_function(ULONG, LPEXTRASEARCH, PULONG)
    def Next(self, celt: int, rgelt: IPointer[EXTRASEARCH], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumExtraSearch']) -> int: ...

    virtual_table.build()

LPENUMEXTRASEARCH = IEnumExtraSearch.PTR()

class IShellFolder2(IShellFolder):
    virtual_table = COMVirtualTable.from_ancestor(IShellFolder)
    _iid_ = IID("{93F2F68C-1D1B-11d3-A30E-00C04F79ABD1}")

    @virtual_table.com_function(LPGUID)
    def GetDefaultSearchGUID(self, pguid: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(PTR(LPENUMEXTRASEARCH))
    def EnumSearches(self, ppenum: IDoublePtr[IEnumExtraSearch]) -> int: ...

    @virtual_table.com_function(DWORD, PULONG, PULONG)
    def GetDefaultColumn(self, dwRes: int, pSort: PULONG, pDisplay: PULONG) -> int: ...

    @virtual_table.com_function(UINT, PTR(SHCOLSTATEF))
    def GetDefaultColumnState(self, iColumn: int, pcsFlags: IPointer[SHCOLSTATEF]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, LPCSHCOLUMNID, LPVARIANT)
    def GetDetailsEx(self, pidl: IPointer[ITEMID_CHILD], pscid: IPointer[SHCOLUMNID], pv: IPointer[VARIANT]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, UINT, LPSHELLDETAILS)
    def GetDetailsOf(self, pidl: IPointer[ITEMID_CHILD], iColumn: int, psd: IPointer[SHELLDETAILS]) -> int: ...

    @virtual_table.com_function(UINT, LPCSHCOLUMNID)
    def MapColumnToSCID(self, iColumn: int, pscid: IPointer[SHCOLUMNID]) -> int: ...

    virtual_table.build()

