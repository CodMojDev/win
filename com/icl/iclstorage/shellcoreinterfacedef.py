#
# F:\Python\Lib\site-packages\win\com\icl\iclstorage\shellcoreinterfacedef.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Thu Jul 16 11:11:19 2026
# Generated from ICL: F:\Python\Lib\site-packages\win\com\icl\iclstorage\shellcoreinterfacedef.icl
#

from .ctlinterfacedef import *
from .objectarray import *
from ..shtypes import *
from ..shellapi import *
from ..commctrl import *

CMF_NORMAL = 0x00000000
CMF_DEFAULTONLY = 0x00000001
CMF_VERBSONLY = 0x00000002
CMF_EXPLORE = 0x00000004
CMF_NOVERBS = 0x00000008
CMF_CANRENAME = 0x00000010
CMF_NODEFAULT = 0x00000020

from win.sdkddkver import *
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

LPCMINVOKECOMMANDINFO = PCCMINVOKECOMMANDINFO = LPCMINVOKECOMMANDINFO

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

LPCMINVOKECOMMANDINFOEX = PCCMINVOKECOMMANDINFO = LPCMINVOKECOMMANDINFOEX

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
    def QueryContextMenu(self, hmenu: int, indexMenu: int, idCmdFirst: int, idCmdLast: int, uFlags: int) -> int: ...

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

    @virtual_table.com_function()
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

    @virtual_table.com_function()
    def Run(self) -> int: ...

    @virtual_table.com_function(BOOL)
    def Kill(self, bWait: bool) -> int: ...

    @virtual_table.com_function()
    def Suspend(self) -> int: ...

    @virtual_table.com_function()
    def Resume(self) -> int: ...

    @virtual_table.function(ULONG)
    def IsRunning(): ...

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

    @virtual_table.com_function()
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

    @virtual_table.com_function()
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
    def ParseDisplayName(self, hwnd: int, pbc: IPointer[IBindCtx], pszDisplayName: LPWSTR, pchEaten: PULONG, ppidl: IDoublePtr[ITEMIDLIST_RELATIVE], pdwAttributes: PULONG) -> int: ...

    @virtual_table.com_function(HWND, SHCONTF, DOUBLE_PTR(IEnumIDList))
    def EnumObjects(self, hwnd: int, grfFlags: int, ppenumIDList: IDoublePtr[IEnumIDList]) -> int: ...

    @virtual_table.com_function(PTR(ITEMIDLIST_RELATIVE), LPBINDCTX, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToObject(self, pidl: IPointer[ITEMIDLIST_RELATIVE], pbc: IPointer[IBindCtx], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pidl, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PTR(ITEMIDLIST_RELATIVE), LPBINDCTX, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToStorage(self, pidl: IPointer[ITEMIDLIST_RELATIVE], pbc: IPointer[IBindCtx], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pidl, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPARAM, PTR(ITEMIDLIST_RELATIVE), PTR(ITEMIDLIST_RELATIVE))
    def CompareIDs(self, lParam: int, pidl1: IPointer[ITEMIDLIST_RELATIVE], pidl2: IPointer[ITEMIDLIST_RELATIVE]) -> int: ...

    @virtual_table.com_function(HWND, LPIID, PVOID, PVOID, intermediate_method = True)
    def CreateViewObject(self, hwndOwner: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(UINT, PTR(PITEMID_CHILD), PTR(SFGAOF))
    def GetAttributesOf(self, cidl: int, apidl: IDoublePtr[ITEMID_CHILD], rgfInOut: IPointer[SFGAOF]) -> int: ...

    @virtual_table.com_function(HWND, UINT, PTR(PITEMID_CHILD), LPIID, PUINT, PVOID, PVOID, intermediate_method = True)
    def GetUIObjectOf(self, hwndOwner: int, cidl: int, apidl: IDoublePtr[ITEMID_CHILD], iid: IID, rgfReserved: PUINT, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(hwndOwner, cidl, iid.ref() if iid else NULL, iid, rgfReserved, ppv)

    @virtual_table.com_function(PITEMID_CHILD, SHGDNF, LPSTRRET)
    def GetDisplayNameOf(self, pidl: IPointer[ITEMID_CHILD], uFlags: int, pName: IPointer[STRRET]) -> int: ...

    @virtual_table.com_function(HWND, PITEMID_CHILD, LPCWSTR, SHGDNF, PTR(PITEMID_CHILD))
    def SetNameOf(self, hwnd: int, pidl: IPointer[ITEMID_CHILD], pszName: LPCWSTR, uFlags: int, ppidlOut: IDoublePtr[ITEMID_CHILD]) -> int: ...

    virtual_table.build()

LPSHELLFOLDER = IShellFolder.PTR()

@CStructure.make
class EXTRASEARCH(CStructure):
    guidSearch: GUID
    wszFriendlyName: IWideCharArrayFixedSize[80]
    wszUrl: IWideCharArrayFixedSize[2084]

LPEXTRASEARCH = LPEXTRASEARCH

class IEnumExtraSearch(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{0E700BE1-9DB6-11d1-A1CE-00C04FD75D13}")

    @virtual_table.com_function(ULONG, LPEXTRASEARCH, PULONG)
    def Next(self, celt: int, rgelt: IPointer[EXTRASEARCH], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumExtraSearch']) -> int: ...

    virtual_table.build()

LPENUMEXTRASEARCH = LPENUMEXTRASEARCH

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

FWF_NONE = 0x00000000
FWF_AUTOARRANGE = 0x00000001
FWF_ABBREVIATEDNAMES = 0x00000002
FWF_SNAPTOGRID = 0x00000004
FWF_OWNERDATA = 0x00000008
FWF_BESTFITWINDOW = 0x00000010
FWF_DESKTOP = 0x00000020
FWF_SINGLESEL = 0x00000040
FWF_NOSUBFOLDERS = 0x00000080
FWF_TRANSPARENT = 0x00000100
FWF_NOCLIENTEDGE = 0x00000200
FWF_NOSCROLL = 0x00000400
FWF_ALIGNLEFT = 0x00000800
FWF_NOICONS = 0x00001000
FWF_SHOWSELALWAYS = 0x00002000
FWF_NOVISIBLE = 0x00004000
FWF_SINGLECLICKACTIVATE = 0x00008000
FWF_NOWEBVIEW = 0x00010000
FWF_HIDEFILENAMES = 0x00020000
FWF_CHECKSELECT = 0x00040000
FWF_NOENUMREFRESH = 0x00080000
FWF_NOGROUPING = 0x00100000
FWF_FULLROWSELECT = 0x00200000
FWF_NOFILTERS = 0x00400000
FWF_NOCOLUMNHEADER = 0x00800000
FWF_NOHEADERINALLVIEWS = 0x01000000
FWF_EXTENDEDTILES = 0x02000000
FWF_TRICHECKSELECT = 0x04000000
FWF_AUTOCHECKSELECT = 0x08000000
FWF_NOBROWSERVIEWSTATE = 0x10000000
FWF_SUBSETGROUPS = 0x20000000
FWF_USESEARCHFOLDER = 0x40000000
FWF_ALLOWRTLREADING = 0x80000000
FOLDERFLAGS = INT

FVM_AUTO = -1
FVM_FIRST = 1
FVM_ICON = 1
FVM_SMALLICON = 2
FVM_LIST = 3
FVM_DETAILS = 4
FVM_THUMBNAIL = 5
FVM_TILE = 6
FVM_THUMBSTRIP = 7
FVM_CONTENT = 8
FVM_LAST = 8
FOLDERVIEWMODE = INT

FLVM_UNSPECIFIED = -1
FLVM_FIRST = 1
FLVM_DETAILS = 1
FLVM_TILES = 2
FLVM_ICONS = 3
FLVM_LIST = 4
FLVM_CONTENT = 5
FLVM_LAST = 5
FOLDERLOGICALVIEWMODE = INT

@CStructure.make
class FOLDERSETTINGS(CStructure):
    ViewMode: IInteger[FOLDERVIEWMODE]
    fFlags: IInteger[FOLDERLOGICALVIEWMODE]

LPFOLDERSETTINGS = LPCFOLDERSETTINGS = PFOLDERSETTINGS = LPFOLDERSETTINGS

SVSI_DESELECT = 0x00000000
SVSI_SELECT = 0x00000001
SVSI_EDIT = 0x00000003
SVSI_DESELECTOTHERS = 0x00000004
SVSI_ENSUREVISIBLE = 0x00000008
SVSI_FOCUSED = 0x00000010
SVSI_TRANSLATEPT = 0x00000020
SVSI_SELECTIONMARK = 0x00000040
SVSI_POSITIONITEM = 0x00000080
SVSI_CHECK = 0x00000100
SVSI_CHECK2 = 0x00000200
SVSI_KEYBOARDSELECT = 0x00000401
SVSI_NOTAKEFOCUS = 0x40000000
SVSIF = INT

SVSI_NOSTATECHANGE = 0x80000000

SVGIO_BACKGROUND = 0x00000000
SVGIO_SELECTION = 0x00000001
SVGIO_ALLVIEW = 0x00000002
SVGIO_CHECKED = 0x00000003
SVGIO_TYPE_MASK = 0x0000000F
SVGIO_FLAG_VIEWORDER = 0x80000000
SVGIO = INT

SVUIA_DEACTIVATE = 0
SVUIA_ACTIVATE_NOFOCUS = 1
SVUIA_ACTIVATE_FOCUS = 2
SVUIA_INPLACEACTIVATE = 3
SVUIA_STATUS = INT

class IShellView(IOleWindow):
    virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
    _iid_ = IID("{000214E3-0000-0000-C000-000000000046}")

    @virtual_table.com_function(PMSG)
    def TranslateAccelerator(self, pmsg: IPointer[MSG]) -> int: ...

    @virtual_table.com_function(BOOL)
    def EnableModeless(self, fEnable: bool) -> int: ...

    @virtual_table.com_function(SVUIA_STATUS)
    def UIActivate(self, uState: int) -> int: ...

    @virtual_table.com_function()
    def Refresh(self) -> int: ...

    @virtual_table.com_function(PVOID, LPFOLDERSETTINGS, PVOID, PRECT, PTR(HWND))
    def CreateViewWindow(self, psvPrevious: IPointer['IShellView'], pfs: IPointer[FOLDERSETTINGS], psb: IPointer['IShellBrowser'], prc: IPointer[RECT], phWnd: IPointer[HWND]) -> int: ...

    @virtual_table.com_function()
    def DestroyViewWindow(self) -> int: ...

    @virtual_table.com_function(LPFOLDERSETTINGS)
    def GetCurrentInfo(self, pfs: IPointer[FOLDERSETTINGS]) -> int: ...

    @virtual_table.com_function(DWORD, LPFNSVADDPROPSHEETPAGE, LPARAM)
    def AddPropertySheetPages(self, dwReserved: int, pfn: FARPROC, lparam: int) -> int: ...

    @virtual_table.com_function()
    def SaveViewState(self) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, SVSIF)
    def SelectItem(self, pidlItem: IPointer[ITEMID_CHILD], uFlags: int) -> int: ...

    @virtual_table.com_function(SVGIO, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetItemObject(self, uItem: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    virtual_table.build()

LPSHELLVIEW = IShellView.PTR()

SV2GV_CURRENTVIEW = UINT(-1).value
SV2GV_DEFAULTVIEW = UINT(-2).value

SHELLVIEWID = GUID

@CStructure.make
class SV2CVW2_PARAMS(CStructure):
    cbSize: IDword
    psvPrev: IPointer[IShellView]
    pfs: IPointer[FOLDERSETTINGS]
    psbOwner: IPointer['IShellBrowser']
    prcView: IPointer[RECT]
    pvid: IPointer[SHELLVIEWID]
    hwndView: IHandle

LPSV2CVW2_PARAMS = LPSV2CVW2_PARAMS

class IShellView2(IShellView):
    virtual_table = COMVirtualTable.from_ancestor(IShellView)
    _iid_ = IID("{88E39E80-3578-11CF-AE69-08002B2E1262}")

    @virtual_table.com_function(PTR(SHELLVIEWID), ULONG)
    def GetView(self, pvid: IPointer[SHELLVIEWID], uView: int) -> int: ...

    @virtual_table.com_function(LPSV2CVW2_PARAMS)
    def CreateViewWindow2(self, lpParams: IPointer[SV2CVW2_PARAMS]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD)
    def HandleRename(self, pidlNew: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, SVSIF, PTR(POINT))
    def SelectAndPositionItem(self, pidlItem: IPointer[ITEMID_CHILD], uFlags: int, ppt: IPointer[POINT]) -> int: ...

    virtual_table.build()

LPSHELLVIEW2 = IShellView2.PTR()

class IFolderView(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{cde725b0-ccc9-4519-917e-325d72fab4ce}")

    @virtual_table.com_function(PTR(FOLDERVIEWMODE))
    def GetCurrentViewMode(self, pViewMode: IPointer[FOLDERVIEWMODE]) -> int: ...

    @virtual_table.com_function(FOLDERVIEWMODE)
    def SetCurrentViewMode(self, ViewMode: int) -> int: ...

    @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
    def GetFolder(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid, ppv)

    @virtual_table.com_function(INT, PITEMID_CHILD)
    def Item(self, iItemIndex: int, ppidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(SVGIO, PTR(INT))
    def ItemCount(self, uFlags: int, pcItems: IPointer[INT]) -> int: ...

    @virtual_table.com_function(SVGIO, LPIID, PVOID, PVOID, intermediate_method = True)
    def Items(self, uFlags: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PTR(INT))
    def GetSelectionMarkedItem(self, piItem: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PTR(INT))
    def GetFocusedItem(self, piItem: IPointer[INT]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, PTR(POINT))
    def GetItemPosition(self, pidl: IPointer[ITEMID_CHILD], ppt: IPointer[POINT]) -> int: ...

    @virtual_table.com_function(PTR(POINT))
    def GetSpacing(self, ppt: IPointer[POINT]) -> int: ...

    @virtual_table.com_function(PTR(POINT))
    def GetDefaultSpacing(self, ppt: IPointer[POINT]) -> int: ...

    @virtual_table.com_function()
    def GetAutoArrange(self) -> int: ...

    @virtual_table.com_function(INT, SVSIF)
    def SelectItem(self, iItem: int, dwFlags: int) -> int: ...

    @virtual_table.com_function(UINT, PTR(PITEMID_CHILD), PTR(POINT), SVSIF)
    def SelectAndPositionItems(self, cidl: int, apidl: IDoublePtr[ITEMID_CHILD], apt: IPointer[POINT], dwFlags: int) -> int: ...

    virtual_table.build()

SID_SFolderView = IFolderView._iid_

if _version >= WIN32_WINNT_VISTA:
    SORT_DESCENDING = -1
    SORT_ASCENDING = 1
    SORTDIRECTION = INT

    @CStructure.make
    class SORTCOLUMN(CStructure):
        propkey: PROPERTYKEY
        direction: IInteger[SORTDIRECTION]

    FVST_EMPTYTEXT = 0
    FVTEXTTYPE = INT

    DEPRECATED_HRESULT = HRESULT

    class IFolderView2(IFolderView):
        virtual_table = COMVirtualTable.from_ancestor(IFolderView)
        _iid_ = IID("{1af3a467-214f-4298-908e-06b03e0b39f9}")

        @virtual_table.com_function(LPPROPERTYKEY, BOOL, intermediate_method = True)
        def SetGroupBy(self, key: PROPERTYKEY, fAscending: bool, **kwargs) -> int:
            return self.virt_delegate(key, fAscending)

        @virtual_table.com_function(LPPROPERTYKEY, PTR(BOOL))
        def GetGroupBy(self, pkey: IPointer[PROPERTYKEY], pfAscending: IPointer[BOOL]) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD, LPPROPERTYKEY, LPPROPVARIANT, intermediate_method = True)
        def SetViewProperty(self, pidl: IPointer[ITEMID_CHILD], propkey: PROPERTYKEY, propvar: IPointer[PROPVARIANT], **kwargs) -> int:
            return self.virt_delegate(propkey.ref() if propkey else NULL, propkey, propvar)

        @virtual_table.com_function(PITEMID_CHILD, LPPROPERTYKEY, LPPROPVARIANT, intermediate_method = True)
        def GetViewProperty(self, pidl: IPointer[ITEMID_CHILD], propkey: PROPERTYKEY, ppropvar: IPointer[PROPVARIANT], **kwargs) -> int:
            return self.virt_delegate(propkey.ref() if propkey else NULL, propkey, ppropvar)

        @virtual_table.com_function(PITEMID_CHILD, LPCWSTR)
        def SetTileViewProperties(self, pidl: IPointer[ITEMID_CHILD], pszPropList: LPCWSTR) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD, LPCWSTR)
        def SetExtendedTileViewProperties(self, pidl: IPointer[ITEMID_CHILD], pszPropList: LPCWSTR) -> int: ...

        @virtual_table.com_function(FVTEXTTYPE, LPCWSTR)
        def SetText(self, iType: int, pwszText: LPCWSTR) -> int: ...

        @virtual_table.com_function(DWORD, DWORD)
        def SetCurrentFolderFlags(self, dwMask: int, dwFlags: int) -> int: ...

        @virtual_table.com_function(PTR(FOLDERFLAGS))
        def GetCurrentFolderFlags(self, pdwFlags: IPointer[FOLDERFLAGS]) -> int: ...

        @virtual_table.com_function(PTR(INT))
        def GetSortColumnCount(self, pcColumns: IPointer[INT]) -> int: ...

        @virtual_table.com_function(PTR(SORTCOLUMN), INT)
        def GetSortColumns(self, rgSortColumns: IPointer[SORTCOLUMN], cColumns: int) -> int: ...

        @virtual_table.com_function(INT, LPIID, PVOID, PVOID, intermediate_method = True)
        def GetItem(self, iItem: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

        @virtual_table.com_function(INT, BOOL, PTR(INT))
        def GetVisibleItem(self, iStart: int, fPrevious: bool, piItem: IPointer[INT]) -> int: ...

        @virtual_table.com_function(INT, PTR(INT))
        def GetSelectedItem(self, iStart: int, piItem: IPointer[INT]) -> int: ...

        @virtual_table.com_function(BOOL, PVOID)
        def GetSelection(self, fNoneImpliesFolder: bool, ppsia: IDoublePtr['IShellItemArray']) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD, PTR(SVSIF))
        def GetSelectionState(self, pidl: IPointer[ITEMID_CHILD], pdwFlags: IPointer[SVSIF]) -> int: ...

        @virtual_table.com_function(LPCSTR)
        def InvokeVerbOnSelection(self, pszVerb: LPCSTR) -> int: ...

        @virtual_table.com_function(FOLDERVIEWMODE, INT)
        def SetViewModeAndIconSize(self, uViewMode: int, iImageSize: int) -> int: ...

        @virtual_table.com_function(PTR(FOLDERVIEWMODE), PTR(INT))
        def GetViewModeAndIconSize(self, puViewMode: IPointer[FOLDERVIEWMODE], piImageSize: IPointer[INT]) -> int: ...

        @virtual_table.com_function(UINT)
        def SetGroupSubsetCount(self, cVisibleRows: int) -> int: ...

        @virtual_table.com_function(PTR(UINT))
        def GetGroupSubsetCount(self, pcVisibleRows: IPointer[UINT]) -> int: ...

        @virtual_table.com_function(BOOL)
        def SetRedraw(self, fRedrawOn: bool) -> int: ...

        @virtual_table.com_function()
        def IsMoveInSameFolder(self) -> int: ...

        @virtual_table.com_function()
        def DoRename(self) -> int: ...

        virtual_table.build()

    class IFolderViewSettings(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{ae8c987d-8797-4ed3-be72-2a47dd938db0}")

        @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
        def GetColumnPropertyList(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid, ppv)

        @virtual_table.com_function(LPPROPERTYKEY, PTR(BOOL))
        def GetGroupByProperty(self, pkey: IPointer[PROPERTYKEY], pfGroupAscending: IPointer[BOOL]) -> int: ...

        @virtual_table.com_function(PTR(FOLDERLOGICALVIEWMODE))
        def GetViewMode(self, plvm: IPointer[FOLDERLOGICALVIEWMODE]) -> int: ...

        @virtual_table.com_function(PTR(UINT))
        def GetIconSize(self, puIconSize: IPointer[UINT]) -> int: ...

        @virtual_table.com_function(PTR(FOLDERFLAGS), PTR(FOLDERFLAGS))
        def GetFolderFlags(self, pfolderMask: IPointer[FOLDERFLAGS], pfolderFlags: IPointer[FOLDERFLAGS]) -> int: ...

        @virtual_table.com_function(PTR(SORTCOLUMN), UINT, PTR(UINT))
        def GetSortColumns(self, rgSortColumns: IPointer[SORTCOLUMN], cColumnsIn: int, pcColumnsOut: IPointer[UINT]) -> int: ...

        @virtual_table.com_function(PTR(UINT))
        def GetGroupSubsetCount(self, pcVisibleRows: IPointer[UINT]) -> int: ...

        virtual_table.build()

    class IInitializeNetworkFolder(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{6e0f9881-42a8-4f2a-97f8-8af4e026d92d}")

        @virtual_table.com_function(PITEMID_CHILD, PITEMID_CHILD, UINT, LPCWSTR, LPCWSTR)
        def Initialize(self, pidl: IPointer[ITEMID_CHILD], pidlTarget: IPointer[ITEMID_CHILD], uDisplayType: int, pszResName: LPCWSTR, pszProvider: LPCWSTR) -> int: ...

        virtual_table.build()

    class INetworkFolderInternal(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{CEB38218-C971-47BB-A703-F0BC99CCDB81}")

        @virtual_table.com_function(PTR(UINT))
        def GetResourceDisplayType(self, displayType: IPointer[UINT]) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD)
        def GetIDList(self, idList: IPointer[ITEMID_CHILD]) -> int: ...

        @virtual_table.com_function(UINT, PTR(PITEMID_CHILD), UINT, LPWSTR)
        def GetProvider(self, itemIdCount: int, itemIds: IDoublePtr[ITEMID_CHILD], providerMaxLength: int, provider: LPWSTR) -> int: ...

        virtual_table.build()


if WIN32_IE >= WIN32_IE_IE70:
    class IPreviewHandlerVisuals(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{196bf9a5-b346-4ef0-aa1e-5dcdb76768b1}")

        @virtual_table.com_function(COLORREF)
        def SetBackgroundColor(self, color: int) -> int: ...

        @virtual_table.com_function(LPLOGFONTW)
        def SetFont(self, plf: IPointer[LOGFONTW]) -> int: ...

        @virtual_table.com_function(COLORREF)
        def SetColor(self, color: int) -> int: ...

        virtual_table.build()


CDBOSC_SETFOCUS = 0x00000000
CDBOSC_KILLFOCUS = 0x00000001
CDBOSC_SELCHANGE = 0x00000002
CDBOSC_RENAME = 0x00000003
CDBOSC_STATECHANGE = 0x00000004

class ICommDlgBrowser(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214F1-0000-0000-C000-000000000046}")

    @virtual_table.com_function(PTR(IShellView))
    def OnDefaultCommand(self, ppshv: IPointer[IShellView]) -> int: ...

    @virtual_table.com_function(PTR(IShellView), ULONG)
    def OnStateChange(self, ppshv: IPointer[IShellView], uChange: int) -> int: ...

    @virtual_table.com_function(PTR(IShellView), PITEMID_CHILD)
    def IncludeObject(self, ppshv: IPointer[IShellView], pidl: IPointer[ITEMID_CHILD]) -> int: ...

    virtual_table.build()

LPCOMMDLGBROWSER = ICommDlgBrowser.PTR()

SID_SExplorerBrowserFrame = ICommDlgBrowser._iid_
if _version >= WIN32_WINNT_WIN2K:
    CDB2N_CONTEXTMENU_DONE = 0x00000001
    CDB2N_CONTEXTMENU_START = 0x00000002

    CDB2GVF_SHOWALLFILES = 0x00000001
if _version >= WIN32_WINNT_VISTA:
        CDB2GVF_ISFILESAVE = 0x00000002
        CDB2GVF_ALLOWPREVIEWPANE = 0x00000004
        CDB2GVF_NOSELECTVERB = 0x00000008
        CDB2GVF_NOINCLUDEITEM = 0x00000010
        CDB2GVF_ISFOLDERPICKER = 0x00000020
        CDB2GVF_ADDSHIELD = 0x00000040


    class ICommDlgBrowser2(ICommDlgBrowser):
        virtual_table = COMVirtualTable.from_ancestor(ICommDlgBrowser)
        _iid_ = IID("{0339516-2894-11d2-9039-00C04F8EEB3E}")

        @virtual_table.com_function(PTR(IShellView), DWORD)
        def Notify(self, ppshv: IPointer[IShellView], dwNotifyType: int) -> int: ...

        @virtual_table.com_function(PTR(IShellView), LPWSTR, INT)
        def GetDefaultMenuText(self, ppshv: IPointer[IShellView], pszText: LPWSTR, cchMax: int) -> int: ...

        @virtual_table.com_function(PTR(DWORD))
        def GetViewFlags(self, pdwFlags: IPointer[DWORD]) -> int: ...

        virtual_table.build()

LPCOMMDLGBROWSER2 = ICommDlgBrowser2.PTR()


if WIN32_IE >= WIN32_IE_IE70:
    CM_MASK_WIDTH = 0x00000001
    CM_MASK_DEFAULTWIDTH = 0x00000002
    CM_MASK_IDEALWIDTH = 0x00000004
    CM_MASK_NAME = 0x00000008
    CM_MASK_STATE = 0x00000010
    CM_MASK = INT

    CM_STATE_NONE = 0x00000000
    CM_STATE_VISIBLE = 0x00000001
    CM_STATE_FIXEDWIDTH = 0x00000002
    CM_STATE_NOSORTBYFOLDERNESS = 0x00000004
    CM_STATE_ALWAYSVISIBLE = 0x00000008
    CM_STATE = INT

    CM_ENUM_ALL = 0x00000001
    CM_ENUM_VISIBLE = 0x00000002
    CM_ENUM_FLAGS = INT

    CM_WIDTH_USEDEFAULT = -1
    CM_WIDTH_AUTOSIZE = -2
    CM_SET_WIDTH_VALUE = INT

    MAX_COLUMN_NAME_LEN = 80

    @CStructure.make
    class CM_COLUMNINFO(CStructure):
        cbSize: IDword
        dwMask: IDword
        dwState: IDword
        uWidth: IUint
        uDefaultWidth: IUint
        uIdealWidth: IUint
        wszName: IWideCharArrayFixedSize[80]

    class IColumnManager(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{d8ec27bb-3f3b-4042-b10a-4acfd924d453}")

        @virtual_table.com_function(LPPROPERTYKEY, PTR(CM_COLUMNINFO), intermediate_method = True)
        def SetColumnInfo(self, propkey: PROPERTYKEY, pcmci: IPointer[CM_COLUMNINFO], **kwargs) -> int:
            return self.virt_delegate(propkey, pcmci)

        @virtual_table.com_function(LPPROPERTYKEY, PTR(CM_COLUMNINFO), intermediate_method = True)
        def GetColumnInfo(self, propkey: PROPERTYKEY, pcmci: IPointer[CM_COLUMNINFO], **kwargs) -> int:
            return self.virt_delegate(propkey, pcmci)

        @virtual_table.com_function(CM_ENUM_FLAGS, PTR(UINT))
        def GetColumnCount(self, dwFlags: int, puCount: IPointer[UINT]) -> int: ...

        @virtual_table.com_function(CM_ENUM_FLAGS, LPPROPERTYKEY, UINT)
        def GetColumns(self, dwFlags: int, rgkeyOrder: IPointer[PROPERTYKEY], cColumns: int) -> int: ...

        @virtual_table.com_function(LPPROPERTYKEY, UINT)
        def SetColumns(self, rgkeyOrder: IPointer[PROPERTYKEY], cVisible: int) -> int: ...

        virtual_table.build()


class IFolderFilterSite(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{C0A651F5-B48B-11d2-B5ED-006097C686F6}")

    @virtual_table.com_function(LPUNKNOWN)
    def SetFilter(self, punk: IPointer[IUnknown]) -> int: ...

    virtual_table.build()

class IFolderFilter(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{9CC22886-DC8E-11d2-B1D0-00C04F8EEB3E}")

    @virtual_table.com_function(PTR(IShellFolder), PITEMID_CHILD, PITEMID_CHILD)
    def ShouldShow(self, psf: IPointer[IShellFolder], pidlFolder: IPointer[ITEMID_CHILD], pidlItem: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PTR(IShellFolder), PITEMID_CHILD, PTR(HWND))
    def GetEnumFlags(self, psf: IPointer[IShellFolder], pidlFolder: IPointer[ITEMID_CHILD], phwnd: IPointer[HWND]) -> int: ...

    virtual_table.build()

class IInputObjectSite(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{F1DB8392-7331-11D0-8C99-00A0C92DBFE8}")

    @virtual_table.com_function(LPUNKNOWN, BOOL)
    def OnFocusChangeIS(self, punkObj: IPointer[IUnknown], fSetFocus: bool) -> int: ...

    virtual_table.build()

class IInputObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{68284fAA-6A48-11D0-8c78-00C04fd918b4}")

    @virtual_table.com_function(BOOL, PMSG)
    def UIActivateIO(self, fActivate: bool, pMsg: IPointer[MSG]) -> int: ...

    @virtual_table.com_function()
    def HasFocusIO(self) -> int: ...

    @virtual_table.com_function(PMSG)
    def TranslateAcceleratorIO(self, pMsg: IPointer[MSG]) -> int: ...

    virtual_table.build()

class IInputObject2(IInputObject):
    virtual_table = COMVirtualTable.from_ancestor(IInputObject)
    _iid_ = IID("{6915C085-510B-44cd-94AF-28DFA56CF92B}")

    @virtual_table.com_function(PMSG)
    def TranslateAcceleratorGlobal(self, pMsg: IPointer[MSG]) -> int: ...

    virtual_table.build()

class IShellIcon(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214E5-0000-0000-C000-000000000046}")

    @virtual_table.com_function(PITEMID_CHILD, UINT, PTR(INT))
    def GetIconOf(self, pidl: IPointer[ITEMID_CHILD], flags: int, pIconIndex: IPointer[INT]) -> int: ...

    virtual_table.build()

SBSP_DEFBROWSER = 0x0000
SBSP_SAMEBROWSER = 0x0001
SBSP_NEWBROWSER = 0x0002
SBSP_DEFMODE = 0x0000
SBSP_OPENMODE = 0x0010
SBSP_EXPLOREMODE = 0x0020
SBSP_HELPMODE = 0x0040
SBSP_NOTRANSFERHIST = 0x0080
SBSP_ABSOLUTE = 0x0000
SBSP_RELATIVE = 0x1000
SBSP_PARENT = 0x2000
SBSP_NAVIGATEBACK = 0x4000
SBSP_NAVIGATEFORWARD = 0x8000
SBSP_ALLOW_AUTONAVIGATE = 0x00010000
if _version >= WIN32_WINNT_VISTA:
    SBSP_KEEPSAMETEMPLATE = 0x00020000
    SBSP_KEEPWORDWHEELTEXT = 0x00040000
    SBSP_ACTIVATE_NOFOCUS = 0x00080000
    SBSP_CREATENOHISTORY = 0x00100000
    SBSP_PLAYNOSOUND = 0x00200000

if WIN32_IE >= WIN32_IE_IE60SP2:
    SBSP_CALLERUNTRUSTED = 0x00800000
    SBSP_TRUSTFIRSTDOWNLOAD = 0x01000000
    SBSP_UNTRUSTEDFORDOWNLOAD = 0x02000000

SBSP_NOAUTOSELECT = 0x04000000
SBSP_WRITENOHISTORY = 0x08000000
if WIN32_IE >= WIN32_IE_IE60SP2:
    SBSP_TRUSTEDFORACTIVEX = 0x10000000

if WIN32_IE >= WIN32_IE_IE70:
    SBSP_FEEDNAVIGATION = 0x20000000

SBSP_REDIRECT = 0x40000000
SBSP_INITIATEDBYHLINKFRAME = 0x80000000

FCW_STATUS = 0x0001
FCW_TOOLBAR = 0x0002
FCW_TREE = 0x0003
FCW_INTERNETBAR = 0x0006
FCW_PROGRESS = 0x0008

FCT_MERGE = 0x0001
FCT_CONFIGABLE = 0x0002
FCT_ADDTOEND = 0x0004

LPTBBUTTONSB = LPTBBUTTON

class IShellBrowser(IOleWindow):
    virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
    _iid_ = IID("{000214E2-0000-0000-C000-000000000046}")

    @virtual_table.com_function(HMENU, LPOLEMENUGROUPWIDTHS)
    def InsertMenusSB(self, hmenuShared: int, lpMenuWidths: IPointer[OLEMENUGROUPWIDTHS]) -> int: ...

    @virtual_table.com_function(HMENU, HOLEMENU, HWND)
    def SetMenuSB(self, hmenuShared: int, holemenuRes: int, hwndActiveObject: int) -> int: ...

    @virtual_table.com_function(HMENU)
    def RemoveMenusSB(self, hmenuShared: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetStatusTextSB(self, pszStatusText: LPCWSTR) -> int: ...

    @virtual_table.com_function(BOOL)
    def EnableModelessSB(self, fEnable: bool) -> int: ...

    @virtual_table.com_function(PMSG, WORD)
    def TranslateAcceleratorSB(self, pmsg: IPointer[MSG], wID: int) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD, UINT)
    def BrowseObject(self, pidl: IPointer[ITEMID_CHILD], wFlags: int) -> int: ...

    @virtual_table.com_function(DWORD, PTR(LPSTREAM))
    def GetViewStateStream(self, grfMode: int, ppStrm: IDoublePtr[IStream]) -> int: ...

    @virtual_table.com_function(UINT, PTR(HWND))
    def GetControlWindow(self, id: int, phwnd: IPointer[HWND]) -> int: ...

    @virtual_table.com_function(UINT, UINT, WPARAM, LPARAM, PTR(LRESULT))
    def SendControlMsg(self, id: int, uMsg: int, wParam: int, lParam: int, pret: IPointer[LRESULT]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IShellView))
    def QueryActiveShellView(self, ppshv: IDoublePtr[IShellView]) -> int: ...

    @virtual_table.com_function(LPTBBUTTON, UINT, UINT)
    def SetToolbarItems(self, lpButtons: IPointer[TBBUTTON], nButtons: int, uFlags: int) -> int: ...

    virtual_table.build()

LPSHELLBROWSER = IShellBrowser.PTR()

class IProfferService(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{cb728b20-f786-11ce-92ad-00aa00a74cd0}")

    @virtual_table.com_function(LPGUID, LPSERVICEPROVIDER, PTR(DWORD), intermediate_method = True)
    def ProfferService(self, guidService: GUID, psp: IPointer[IServiceProvider], pdwCookie: IPointer[DWORD], **kwargs) -> int:
        return self.virt_delegate(guidService, psp, pdwCookie)

    @virtual_table.com_function(DWORD)
    def RevokeService(self, dwCookie: int) -> int: ...

    virtual_table.build()

SID_SProfferService = IProfferService._iid_

STR_DONT_RESOLVE_LINK = "Don't Resolve Link"
STR_GET_ASYNC_HANDLER = "GetAsyncHandler"

SIGDN_NORMALDISPLAY = 0x00000000
SIGDN_PARENTRELATIVEPARSING = 0x80018001
SIGDN_DESKTOPABSOLUTEPARSING = 0x80028000
SIGDN_PARENTRELATIVEEDITING = 0x80031001
SIGDN_DESKTOPABSOLUTEEDITING = 0x8004c000
SIGDN_FILESYSPATH = 0x80058000
SIGDN_URL = 0x80068000
SIGDN_PARENTRELATIVEFORADDRESSBAR = 0x8007c001
SIGDN_PARENTRELATIVE = 0x80080001
SIGDN_PARENTRELATIVEFORUI = 0x80094001
SIGDN = INT

SICHINT_DISPLAY = 0x00000000
SICHINT_ALLFIELDS = 0x80000000
SICHINT_CANONICAL = 0x10000000
SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL = 0x20000000
SICHINTF = INT

class IShellItem(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{43826d1e-e718-42ee-bc55-a1e261c37bfe}")

    @virtual_table.com_function(LPBINDCTX, LPGUID, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToHandler(self, pbc: IPointer[IBindCtx], bhid: GUID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(bhid.ref() if bhid else NULL, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PVOID)
    def GetParent(self, ppsi: IDoublePtr['IShellItem']) -> int: ...

    @virtual_table.com_function(SIGDN, PTR(LPWSTR))
    def GetDisplayName(self, sigdnName: int, ppszName: IPointer[LPWSTR]) -> int: ...

    @virtual_table.com_function(SFGAOF, PTR(SFGAOF))
    def GetAttributes(self, sfgaoMask: SFGAOF, psfgaoAttribs: IPointer[SFGAOF]) -> int: ...

    @virtual_table.com_function(PVOID, SICHINTF, PTR(INT))
    def Compare(self, psi: IPointer['IShellItem'], hint: int, piOrder: IPointer[INT]) -> int: ...

    virtual_table.build()


@shell32.foreign(PITEMID_CHILD)
def SHSimpleIDListFromPath() -> IPointer[ITEMID_CHILD]: ...

if WIN32_IE >= WIN32_IE_IE70:
    @shell32.foreign(HRESULT, PITEMID_CHILD, LPIID, intermediate_method = True)
    def SHCreateItemFromIDList(pidl: IPointer[ITEMID_CHILD], iid: IID, **kwargs) -> int:
        return delegate(pidl, iid)

    @shell32.foreign(HRESULT, PCWSTR, LPBINDCTX, LPIID, intermediate_method = True)
    def SHCreateItemFromParsingName(pszPath: PCWSTR, pbc: IPointer[IBindCtx], iid: IID, **kwargs) -> int:
        return delegate(pszPath, pbc, iid)

    @shell32.foreign(HRESULT, PITEMID_CHILD, PTR(IShellFolder), PITEMID_CHILD, LPIID, intermediate_method = True)
    def SHCreateItemWithParent(pidlParent: IPointer[ITEMID_CHILD], psfParent: IPointer[IShellFolder], pidl: IPointer[ITEMID_CHILD], iid: IID, **kwargs) -> int:
        return delegate(pidlParent, psfParent, pidl, iid)

    @shell32.foreign(HRESULT, PTR(IShellItem), PCWSTR, LPBINDCTX, LPIID, intermediate_method = True)
    def SHCreateItemFromRelativeName(psiParent: IPointer[IShellItem], pszName: PCWSTR, pbz: IPointer[IBindCtx], iid: IID, **kwargs) -> int:
        return delegate(psiParent, pszName, pbz, iid)


if _version >= WIN32_WINNT_VISTA:
    @shell32.foreign(HRESULT, LPGUID, DWORD, PCWSTR, LPIID, intermediate_method = True)
    def SHCreateItemInKnownFolder(kfid: GUID, dwKFFlags: int, pszItem: PCWSTR, iid: IID, **kwargs) -> int:
        return delegate(kfid, kfid.ref() if kfid else NULL, pszItem, iid)

    @shell32.foreign(HRESULT, LPUNKNOWN)
    def SHGetIDListFromObject(punk: IPointer[IUnknown]) -> int: ...

    @shell32.foreign(HRESULT, LPUNKNOWN, LPIID, intermediate_method = True)
    def SHGetItemFromObject(punk: IPointer[IUnknown], iid: IID, **kwargs) -> int:
        return delegate(punk, iid)

    @shell32.foreign(HRESULT, PITEMID_CHILD, GETPROPERTYSTOREFLAGS, LPIID, intermediate_method = True)
    def SHGetPropertyStoreFromIDList(pidl: IPointer[ITEMID_CHILD], flags: GETPROPERTYSTOREFLAGS, iid: IID, **kwargs) -> int:
        return delegate(pidl, flags, iid)

    @shell32.foreign(HRESULT, PCWSTR, LPBINDCTX, GETPROPERTYSTOREFLAGS, LPIID, intermediate_method = True)
    def SHGetPropertyStoreFromParsingName(pszPath: PCWSTR, pbc: IPointer[IBindCtx], flags: GETPROPERTYSTOREFLAGS, iid: IID, **kwargs) -> int:
        return delegate(pszPath, pbc, flags, iid)

    @shell32.foreign(HRESULT, PITEMID_CHILD, SIGDN)
    def SHGetNameFromIDList(pidl: IPointer[ITEMID_CHILD], sigdnName: int) -> int: ...



if _version >= WIN32_WINNT_WIN7:
    DOGIF_DEFAULT = 0x0000
    DOGIF_TRAVERSE_LINK = 0x0001
    DOGIF_NO_HDROP = 0x0002
    DOGIF_NO_URL = 0x0004
    DOGIF_ONLY_IF_ONE = 0x000
    DATAOBJ_GET_ITEM_FLAGS = INT

    @shell32.foreign(HRESULT, LPDATAOBJECT, DATAOBJ_GET_ITEM_FLAGS, LPIID, intermediate_method = True)
    def SHGetItemFromDataObject(pdtObj: IPointer[IDataObject], dwFlags: int, iid: IID, **kwargs) -> int:
        return delegate(pdtObj, dwFlags, iid)



STR_GPS_HANDLERPROPERTIESONLY = "GPS_HANDLERPROPERTIESONLY"
STR_GPS_FASTPROPERTIESONLY = "GPS_FASTPROPERTIESONLY"
STR_GPS_OPENSLOWITEM = "GPS_OPENSLOWITEM"
STR_GPS_DELAYCREATION = "GPS_DELAYCREATION"
STR_GPS_BESTEFFORT = "GPS_BESTEFFORT"
STR_GPS_NO_OPLOCK = "GPS_NO_OPLOCK"

class IShellItem2(IShellItem):
    virtual_table = COMVirtualTable.from_ancestor(IShellItem)
    _iid_ = IID("{7e9fb0d3-919f-4307-ab2e-9b1860310c93}")

    @virtual_table.com_function(GETPROPERTYSTOREFLAGS, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyStore(self, flags: GETPROPERTYSTOREFLAGS, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(GETPROPERTYSTOREFLAGS, LPUNKNOWN, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyStoreWithCreateObject(self, flags: GETPROPERTYSTOREFLAGS, punkCreateObject: IPointer[IUnknown], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(flags, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPPROPERTYKEY, UINT, GETPROPERTYSTOREFLAGS, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyStoreForKeys(self, rgKeys: IPointer[PROPERTYKEY], cKeys: int, flags: GETPROPERTYSTOREFLAGS, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(rgKeys, cKeys, iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPPROPERTYKEY, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyDescriptionList(self, keyType: PROPERTYKEY, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPBINDCTX)
    def Update(self, pbc: IPointer[IBindCtx]) -> int: ...

    @virtual_table.com_function(LPPROPERTYKEY, LPPROPVARIANT, intermediate_method = True)
    def GetProperty(self, key: PROPERTYKEY, ppropvar: IPointer[PROPVARIANT], **kwargs) -> int:
        return self.virt_delegate(key, ppropvar)

    @virtual_table.com_function(LPPROPERTYKEY, LPCLSID, intermediate_method = True)
    def GetCLSID(self, key: PROPERTYKEY, pclsid: IPointer[CLSID], **kwargs) -> int:
        return self.virt_delegate(key, pclsid)

    @virtual_table.com_function(LPPROPERTYKEY, LPFILETIME, intermediate_method = True)
    def GetFileTime(self, key: PROPERTYKEY, pft: IPointer[FILETIME], **kwargs) -> int:
        return self.virt_delegate(key, pft)

    @virtual_table.com_function(LPPROPERTYKEY, PTR(INT), intermediate_method = True)
    def GetInt32(self, key: PROPERTYKEY, pi: IPointer[INT], **kwargs) -> int:
        return self.virt_delegate(key, pi)

    @virtual_table.com_function(LPPROPERTYKEY, PTR(LPWSTR), intermediate_method = True)
    def GetString(self, key: PROPERTYKEY, ppsz: IPointer[LPWSTR], **kwargs) -> int:
        return self.virt_delegate(key, ppsz)

    @virtual_table.com_function(LPPROPERTYKEY, PTR(ULONG), intermediate_method = True)
    def GetUInt32(self, key: PROPERTYKEY, pui: IPointer[ULONG], **kwargs) -> int:
        return self.virt_delegate(key, pui)

    @virtual_table.com_function(LPPROPERTYKEY, PTR(ULONGLONG), intermediate_method = True)
    def GetUInt64(self, key: PROPERTYKEY, pull: IPointer[ULONGLONG], **kwargs) -> int:
        return self.virt_delegate(key, pull)

    @virtual_table.com_function(LPPROPERTYKEY, PTR(BOOL), intermediate_method = True)
    def GetBool(self, key: PROPERTYKEY, pf: IPointer[BOOL], **kwargs) -> int:
        return self.virt_delegate(key, pf)

    virtual_table.build()

SIIGBF_RESIZETOFIT = 0x00000000
SIIGBF_BIGGERSIZEOK = 0x00000001
SIIGBF_MEMORYONLY = 0x00000002
SIIGBF_ICONONLY = 0x00000004
SIIGBF_THUMBNAILONLY = 0x00000008
SIIGBF_INCACHEONLY = 0x00000010
SIIGBF_CROPTOSQUARE = 0x00000020
SIIGBF_WIDETHUMBNAILS = 0x00000040
SIIGBF_ICONBACKGROUND = 0x00000080
SIIGBF_SCALEUP = 0x00000100
SIIGBF = INT

class IShellItemImageFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{bcc18b79-ba16-442f-80c4-8a59c30c463b}")

    @virtual_table.com_function(SIZE, SIIGBF, PTR(HBITMAP))
    def GetImage(self, size: SIZE, flags: int, phbm: IPointer[HBITMAP]) -> int: ...

    virtual_table.build()

class IEnumShellItems(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{70629033-e363-4a28-a567-0db78006e6d7}")

    @virtual_table.com_function(ULONG, DOUBLE_PTR(IShellItem), PTR(ULONG))
    def Next(self, celt: int, rgelt: IDoublePtr[IShellItem], pceltFetched: IPointer[ULONG]) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumShellItems']) -> int: ...

    virtual_table.build()

STGTRANSCONFIRMATION = GUID
LPSTGTRANSCONFIRMATION = LPGUID

STGOP_MOVE = 1
STGOP_COPY = 2
STGOP_SYNC = 3
STGOP_REMOVE = 5
STGOP_RENAME = 6
STGOP_APPLYPROPERTIES = 8
STGOP_NEW = 10
STGOP = INT

TSF_NORMAL = 0x00000000
TSF_FAIL_EXIST = 0x00000000
TSF_RENAME_EXIST = 0x00000001
TSF_OVERWRITE_EXIST = 0x00000002
TSF_ALLOW_DECRYPTION = 0x00000004
TSF_NO_SECURITY = 0x00000008
TSF_COPY_CREATION_TIME = 0x00000010
TSF_COPY_WRITE_TIME = 0x00000020
TSF_USE_FULL_ACCESS = 0x00000040
TSF_DELETE_RECYCLE_IF_POSSIBLE = 0x00000080
TSF_COPY_HARD_LINK = 0x00000100
TSF_COPY_LOCALIZED_NAME = 0x00000200
TSF_MOVE_AS_COPY_DELETE = 0x00000400
TSF_SUSPEND_SHELLEVENTS = 0x00000800
TRANSFER_SOURCE_FLAGS = INT

if WIN32_IE >= WIN32_IE_IE70:
    TS_NONE = 0
    TS_PERFORMING = 1
    TS_PREPARING = 2
    TS_INDETERMINATE = 4
    TRANSFER_ADVISE_STATUS = INT

    class ITransferAdviseSink(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{d594d0d8-8da7-457b-b3b4-ce5dbaac0b88}")

        @virtual_table.com_function(ULONGLONG, ULONGLONG, INT, INT, INT, INT)
        def UpdateProgress(self, ullSizeCurrent: ULONGLONG, ullSizeTotal: ULONGLONG, nFilesCurrent: int, nFilesTotal: int, nFoldersCurrent: int, nFoldersTotal: int) -> int: ...

        @virtual_table.com_function(TRANSFER_ADVISE_STATUS)
        def UpdateTransferState(self, ts: int) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), LPCWSTR)
        def ConfirmOverwrite(self, psiSource: IPointer[IShellItem], psiDestParent: IPointer[IShellItem], pszName: LPCWSTR) -> int: ...

        @virtual_table.com_function(PTR(IShellItem))
        def ConfirmEncryptionLoss(self, psiSource: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), LPCWSTR, HRESULT, LPWSTR, ULONG)
        def FileFailure(self, psi: IPointer[IShellItem], pszItem: LPCWSTR, hrError: int, pszRename: LPWSTR, cchRename: int) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), LPCWSTR, HRESULT)
        def SubStreamFailure(self, psi: IPointer[IShellItem], pszStreamName: LPCWSTR, hrError: int) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), LPPROPERTYKEY, HRESULT)
        def PropertyFailure(self, psi: IPointer[IShellItem], pkey: IPointer[PROPERTYKEY], hrError: int) -> int: ...

        virtual_table.build()


if _version >= WIN32_WINNT_VISTA:
    class ITransferSource(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{00adb003-bde9-45c6-8e29-d09f9353e108}")

        @virtual_table.com_function(PTR(ITransferAdviseSink), PTR(DWORD))
        def Advise(self, psink: IPointer[ITransferAdviseSink], pdwCookie: IPointer[DWORD]) -> int: ...

        @virtual_table.com_function(DWORD)
        def Unadvise(self, dwCookie: int) -> int: ...

        @virtual_table.com_function(PTR(IPropertyChangeArray))
        def SetProperties(self, pproparray: IPointer[IPropertyChangeArray]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), TRANSFER_SOURCE_FLAGS, LPIID, PVOID, PVOID, intermediate_method = True)
        def OpenItem(self, psi: IPointer[IShellItem], flags: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(psi, iid.ref() if iid else NULL, iid, ppv)

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), LPCWSTR, TRANSFER_SOURCE_FLAGS, DOUBLE_PTR(IShellItem))
        def MoveItem(self, psi: IPointer[IShellItem], psiParentDst: IPointer[IShellItem], pszNameDst: LPCWSTR, flags: int, ppsiNew: IDoublePtr[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), TRANSFER_SOURCE_FLAGS, DOUBLE_PTR(IShellItem))
        def RecycleItem(self, psiSource: IPointer[IShellItem], psiParentDest: IPointer[IShellItem], flags: int, ppsiNewDst: IDoublePtr[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), LPCWSTR, TRANSFER_SOURCE_FLAGS, DOUBLE_PTR(IShellItem))
        def RemoveItem(self, psiSource: IPointer[IShellItem], pszNewName: LPCWSTR, flags: int, ppsiNewDest: IDoublePtr[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), LPCWSTR, TRANSFER_SOURCE_FLAGS, DOUBLE_PTR(IShellItem))
        def LinkItem(self, psiSource: IPointer[IShellItem], psiParentDest: IPointer[IShellItem], pszNewName: LPCWSTR, flags: int, ppsiNewDst: IDoublePtr[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), DOUBLE_PTR(IShellItem))
        def ApplyPropertiesToItem(self, psiSource: IPointer[IShellItem], ppsiNew: IDoublePtr[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), PTR(LPWSTR))
        def GetDefaultDestinationName(self, psiSource: IPointer[IShellItem], psiParentDest: IPointer[IShellItem], ppszDestinationName: IPointer[LPWSTR]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem))
        def EnterFolder(self, psiChildFolderDest: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem))
        def LeaveFolder(self, psiChildFolderDest: IPointer[IShellItem]) -> int: ...

        virtual_table.build()


@CStructure.make
class SHELL_ITEM_RESOURCE(CStructure):
    guidType: GUID
    szName: IWideCharArrayFixedSize[260]

class IEnumResources(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{2dd81fe3-a83c-4da9-a330-47249d345ba1}")

    @virtual_table.com_function(ULONG, PTR(SHELL_ITEM_RESOURCE), PTR(ULONG))
    def Next(self, celt: int, psir: IPointer[SHELL_ITEM_RESOURCE], pceltFetched: IPointer[ULONG]) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenumr: IDoublePtr['IEnumResources']) -> int: ...

    virtual_table.build()

class IShellItemResources(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{ff5693be-2ce0-4d48-b5c5-40817d1acdb9}")

    @virtual_table.com_function(PTR(DWORD))
    def GetAttributes(self, pdwAttributes: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(PTR(ULONGLONG))
    def GetSize(self, pullSize: IPointer[ULONGLONG]) -> int: ...

    @virtual_table.com_function(LPFILETIME, LPFILETIME, LPFILETIME)
    def GetTimes(self, pftCreation: IPointer[FILETIME], pftWrite: IPointer[FILETIME], pftAccess: IPointer[FILETIME]) -> int: ...

    @virtual_table.com_function(LPFILETIME, LPFILETIME, LPFILETIME)
    def SetTimes(self, pftCreation: IPointer[FILETIME], pftWrite: IPointer[FILETIME], pftAccess: IPointer[FILETIME]) -> int: ...

    @virtual_table.com_function(PTR(SHELL_ITEM_RESOURCE), PTR(LPWSTR))
    def GetResourceDescription(self, pcsir: IPointer[SHELL_ITEM_RESOURCE], ppszDescription: IPointer[LPWSTR]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IEnumResources))
    def EnumResource(self, ppenumr: IDoublePtr[IEnumResources]) -> int: ...

    @virtual_table.com_function(PTR(SHELL_ITEM_RESOURCE))
    def SupportsResource(self, pcsir: IPointer[SHELL_ITEM_RESOURCE]) -> int: ...

    @virtual_table.com_function(PTR(SHELL_ITEM_RESOURCE), LPIID, PVOID, PVOID, intermediate_method = True)
    def OpenResource(self, pcsir: IPointer[SHELL_ITEM_RESOURCE], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PTR(SHELL_ITEM_RESOURCE), LPIID, PVOID, PVOID, intermediate_method = True)
    def CreateResource(self, pcsir: IPointer[SHELL_ITEM_RESOURCE], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function()
    def MarkForDelete(self) -> int: ...

    virtual_table.build()

class ITransferDestination(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{48addd32-3ca5-4124-abe3-b5a72531b207}")

    @virtual_table.com_function(PTR(ITransferAdviseSink), PTR(DWORD))
    def Advise(self, psink: IPointer[ITransferAdviseSink], pdwCookie: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(DWORD)
    def Unadvise(self, dwCookie: int) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD, ULONGLONG, TRANSFER_SOURCE_FLAGS, LPIID, PVOID, PVOID, LPIID, PVOID, PVOID, intermediate_method = True)
    def CreateItem(self, pszName: LPCWSTR, dwAttributes: int, ullSize: ULONGLONG, flags: int, iidItem: IID, ppvItem: IPointer[PVOID], iidResources: IID, ppvResources: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pszName, dwAttributes, ullSize, iidItem.ref() if iidItem else NULL, iidItem, iidResources.ref() if iidResources else NULL, iidResources, ppvResources)

    virtual_table.build()

if WIN32_IE >= WIN32_IE_IE70:
    class IFileOperationProgressSink(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{04b0f1a7-9490-44bc-96e1-4296a31252e2}")

        @virtual_table.com_function()
        def StartOperations(self) -> int: ...

        @virtual_table.com_function(HRESULT)
        def FinishOperations(self, hrResult: int) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), LPCWSTR)
        def PreRenameItem(self, dwFlags: int, psiItem: IPointer[IShellItem], pszNewName: LPCWSTR) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), LPCWSTR, HRESULT, PTR(IShellItem))
        def PostRenameItem(self, dwFlags: int, psiItem: IPointer[IShellItem], pszNewName: LPCWSTR, hrRename: int, psiNewlyCreated: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), PTR(IShellItem), LPCWSTR)
        def PreMoveItem(self, dwFlags: int, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), PTR(IShellItem), LPCWSTR, HRESULT, PTR(IShellItem))
        def PostMoveItem(self, dwFlags: int, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR, hrMove: int, psiNewlyCreated: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), PTR(IShellItem), LPCWSTR)
        def PreCopyItem(self, dwFlags: int, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), PTR(IShellItem), LPCWSTR, HRESULT, PTR(IShellItem))
        def PostCopyItem(self, dwFlags: int, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR, hrCopy: int, psiNewlyCreated: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem))
        def PreDeleteItem(self, dwFlags: int, psiItem: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), HRESULT, PTR(IShellItem))
        def PostDeleteItem(self, dwFlags: int, psiItem: IPointer[IShellItem], hrDelete: int, psiNewlyCreated: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), LPCWSTR)
        def PreNewItem(self, dwFlags: int, psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR) -> int: ...

        @virtual_table.com_function(DWORD, PTR(IShellItem), LPCWSTR, DWORD, HRESULT, PTR(IShellItem))
        def PostNewItem(self, dwFlags: int, psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR, dwFileAttributes: int, hrNew: int, psiNewItem: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(UINT, UINT)
        def UpdateProgress(self, iWorkTotal: int, iWorkSoFar: int) -> int: ...

        @virtual_table.com_function()
        def ResetTimer(self) -> int: ...

        @virtual_table.com_function()
        def PauseTimer(self) -> int: ...

        @virtual_table.com_function()
        def ResumeTimer(self) -> int: ...

        virtual_table.build()


SIATTRIBFLAGS_AND = 1
SIATTRIBFLAGS_OR = 2
SIATTRIBFLAGS_APPCOMPAT = 3
SIATTRIBFLAGS_MASK = 3
SIATTRIBFLAGS_ALLITEMS = 0x4000
SIATTRIBFLAGS = INT

class IShellItemArray(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{b63ea76d-1f85-456f-a19c-48159efa858b}")

    @virtual_table.com_function(LPBINDCTX, LPGUID, LPIID, PVOID, PVOID, intermediate_method = True)
    def BindToHandler(self, pbc: IPointer[IBindCtx], bhid: GUID, iid: IID, ppvOut: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(bhid.ref() if bhid else NULL, iid.ref() if iid else NULL, iid, ppvOut)

    @virtual_table.com_function(GETPROPERTYSTOREFLAGS, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyStore(self, flags: GETPROPERTYSTOREFLAGS, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(LPPROPERTYKEY, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetPropertyDescriptionList(self, keyType: PROPERTYKEY, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(SIATTRIBFLAGS, SFGAOF, PTR(SFGAOF))
    def GetAttributes(self, AttribFlags: int, sfgaoMask: SFGAOF, psfgaoAttribs: IPointer[SFGAOF]) -> int: ...

    @virtual_table.com_function(PTR(DWORD))
    def GetCount(self, pdwNumItems: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(DWORD, DOUBLE_PTR(IShellItem))
    def GetItemAt(self, dwIndex: int, ppsi: IDoublePtr[IShellItem]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IEnumShellItems))
    def EnumItems(self, ppenumShellItems: IDoublePtr[IEnumShellItems]) -> int: ...

    virtual_table.build()

if WIN32_IE >= WIN32_IE_IE70:
    @shell32.foreign(HRESULT, PITEMID_CHILD, PTR(IShellFolder), UINT, PTR(PITEMID_CHILD))
    def SHCreateShellItemArray(pidlParent: IPointer[ITEMID_CHILD], psf: IPointer[IShellFolder], cidl: int, ppidl: IDoublePtr[ITEMID_CHILD]) -> int: ...

    @shell32.foreign(HRESULT, LPDATAOBJECT, LPIID, intermediate_method = True)
    def SHCreateShellItemArrayFromDataObject(pdo: IPointer[IDataObject], iid: IID, **kwargs) -> int:
        return delegate(pdo, iid)

    @shell32.foreign(HRESULT, UINT, PTR(PITEMID_CHILD))
    def SHCreateShellItemArrayFromIDLists(cidl: int, rgpidl: IDoublePtr[ITEMID_CHILD]) -> int: ...

    @shell32.foreign(HRESULT, PTR(IShellItem), LPIID, intermediate_method = True)
    def SHCreateShellItemArrayFromShellItem(psi: IPointer[IShellItem], iid: IID, **kwargs) -> int:
        return delegate(psi, iid)


class IInitializeWithItem(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7f73be3f-fb79-493c-a6c7-7ee14e245841}")

    @virtual_table.com_function(PTR(IShellItem), DWORD)
    def Initialize(self, psi: IPointer[IShellItem], grfMode: int) -> int: ...

    virtual_table.build()

class IObjectWithSelection(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1c9cd5bb-98e9-4491-a60f-31aacc72b83c}")

    @virtual_table.com_function(PTR(IShellItemArray))
    def SetSelection(self, psia: IPointer[IShellItemArray]) -> int: ...

    @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
    def GetSelection(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid, ppv)

    virtual_table.build()

class IObjectWithBackReferences(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{321a6a6a-d61f-4bf3-97ae-14be2986bb36}")

    @virtual_table.com_function()
    def RemoveBackReferences(self) -> int: ...

    virtual_table.build()

PUIF_DEFAULT = 0
PUIF_RIGHTALIGN = 1
PUIF_NOLABELININFOTIP = 2
PROPERTYUI_FLAGS = INT

PUIFFDF_DEFAULT = 0
PUIFFDF_RIGHTTOLEFT = 1
PUIFFDF_SHORTFORMAT = 2
PUIFFDF_NOTIME = 4
PUIFFDF_FRIENDLYDATE = 8
PROPERTYUI_FORMAT_FLAGS = INT

class IPropertyUI(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{757a7d9f-919a-4118-99d7-dbb208c8cc66}")

    @virtual_table.com_function(LPCWSTR, PTR(FMTID), PTR(PROPID), PTR(ULONG))
    def ParsePropertyName(self, pszName: LPCWSTR, pfmtid: IPointer[FMTID], ppid: IPointer[PROPID], pchEaten: IPointer[ULONG]) -> int: ...

    @virtual_table.com_function(PTR(FMTID), PROPID, LPWSTR, DWORD, intermediate_method = True)
    def GetCannonicalName(self, fmtid: FMTID, pid: PROPID, pwszText: LPWSTR, cchText: int, **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, pwszText, cchText)

    @virtual_table.com_function(PTR(FMTID), PROPID, PROPERTYUI_NAME_FLAGS, LPWSTR, DWORD, intermediate_method = True)
    def GetDisplayName(self, fmtid: FMTID, pid: PROPID, flags: PROPERTYUI_NAME_FLAGS, pwszText: LPWSTR, cchText: int, **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, flags, pwszText, cchText)

    @virtual_table.com_function(PTR(FMTID), PROPID, LPWSTR, DWORD, intermediate_method = True)
    def GetPropertyDescription(self, fmtid: FMTID, pid: PROPID, pwszText: LPWSTR, cchText: int, **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, pwszText, cchText)

    @virtual_table.com_function(PTR(FMTID), PROPID, PTR(ULONG), intermediate_method = True)
    def GetDefaultWidth(self, fmtid: FMTID, pid: PROPID, pcxChars: IPointer[ULONG], **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, pcxChars)

    @virtual_table.com_function(PTR(FMTID), PROPID, PTR(PROPERTYUI_FLAGS), intermediate_method = True)
    def GetFlags(self, fmtid: FMTID, pid: PROPID, pflags: IPointer[PROPERTYUI_FLAGS], **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, pflags)

    @virtual_table.com_function(PTR(FMTID), PROPID, LPPROPVARIANT, PROPERTYUI_FORMAT_FLAGS, LPWSTR, DWORD, intermediate_method = True)
    def FormatForDisplay(self, fmtid: FMTID, pid: PROPID, ppropvar: IPointer[PROPVARIANT], puiff: int, pwszText: LPWSTR, cchText: int, **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, ppropvar, puiff, pwszText, cchText)

    @virtual_table.com_function(PTR(FMTID), PROPID, LPWSTR, DWORD, PTR(UINT), intermediate_method = True)
    def GetHelpInfo(self, fmtid: FMTID, pid: PROPID, pwszHelpFile: LPWSTR, cch: int, puHelpID: IPointer[UINT], **kwargs) -> int:
        return self.virt_delegate(fmtid, pid, pwszHelpFile, cch, puHelpID)

    virtual_table.build()

class ICategoryProvider(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{9af64809-5864-4c26-a720-c1f78c086ee3}")

    @virtual_table.com_function(LPCSHCOLUMNID)
    def CanCategorizeOnSCID(self, pscid: IPointer[SHCOLUMNID]) -> int: ...

    @virtual_table.com_function(LPGUID, LPCSHCOLUMNID)
    def GetDefaultCategory(self, pguid: IPointer[GUID], pscid: IPointer[SHCOLUMNID]) -> int: ...

    @virtual_table.com_function(LPCSHCOLUMNID, LPGUID)
    def GetCategoryForSCID(self, pscid: IPointer[SHCOLUMNID], pguid: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IEnumGUID))
    def EnumCategories(self, penum: IDoublePtr[IEnumGUID]) -> int: ...

    @virtual_table.com_function(LPGUID, LPWSTR, UINT)
    def GetCategoryName(self, pguid: IPointer[GUID], pszName: LPWSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPGUID, LPIID, PVOID, PVOID, intermediate_method = True)
    def CreateCategory(self, pguid: IPointer[GUID], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    virtual_table.build()

CATINFO_NORMAL = 0x00000000
CATINFO_COLLAPSED = 0x00000001
CATINFO_HIDDEN = 0x00000002
CATINFO_EXPANDED = 0x00000004
CATINFO_NOHEADER = 0x00000008
CATINFO_NOTCOLLAPSIBLE = 0x00000010
CATINFO_NOHEADERCOUNT = 0x00000020
CATINFO_SUBSETTED = 0x00000040
CATINFO_SEPARATE_IMAGES = 0x00000080
CATINFO_SHOWEMPTY = 0x00000100
CATEGORYINFO_FLAGS = INT

CATSORT_DEFAULT = 0
CATSORT_NAME = 1
CATSORT_FLAGS = INT

@CStructure.make
class CATEGORY_INFO(CStructure):
    cif: IInteger[CATEGORYINFO_FLAGS]
    wszName: IWideCharArrayFixedSize[260]

class ICategorizer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{a3b14589-9174-49a8-89a3-06a1ae2b9ba7}")

    @virtual_table.com_function(LPWSTR, UINT)
    def GetDescription(self, pszDesc: LPWSTR, cch: int) -> int: ...

    @virtual_table.com_function(UINT, PITEMID_CHILD, PTR(DWORD))
    def GetCategory(self, cidl: int, apidl: IPointer[ITEMID_CHILD], rgCategoryIds: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(DWORD, PTR(CATEGORY_INFO))
    def GetCategoryInfo(self, dwCategoryId: int, pci: IPointer[CATEGORY_INFO]) -> int: ...

    @virtual_table.com_function(CATSORT_FLAGS, DWORD, DWORD)
    def CompareCategory(self, csfFlags: int, dwCategoryId1: int, dwCategoryId2: int) -> int: ...

    virtual_table.build()

if _version >= WIN32_WINNT_WIN2K:
    @CStructure.make
    class SHDRAGIMAGE(CStructure):
        sizeDragImage: SIZE
        ptOffset: POINT
        hbmpDragImage: IHandle
        crColorKey: IInteger[COLORREF]

LPSHDRAGIMAGE = LPSHDRAGIMAGE

    DI_GETDRAGIMAGE = TEXT("ShellGetDragImage")

    class IDropTargetHelper(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{4657278B-411B-11D2-839A-00C04FD918D0}")

        @virtual_table.com_function(HWND, LPDATAOBJECT, PTR(POINT), DWORD)
        def DragEnter(self, hwndTarget: int, pDataObject: IPointer[IDataObject], ppt: IPointer[POINT], dwEffect: int) -> int: ...

        @virtual_table.com_function()
        def DragLeave(self) -> int: ...

        @virtual_table.com_function(PTR(POINT), DWORD)
        def DragOver(self, ppt: IPointer[POINT], dwEffect: int) -> int: ...

        @virtual_table.com_function(LPDATAOBJECT, PTR(POINT), DWORD)
        def Drop(self, pDataObject: IPointer[IDataObject], ppt: IPointer[POINT], dwEffect: int) -> int: ...

        @virtual_table.com_function(BOOL)
        def Show(self, fShow: bool) -> int: ...

        virtual_table.build()

    class IDragSourceHelper(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{DE5BF786-477A-11D2-839D-00C04FD918D0}")

        @virtual_table.com_function(LPSHDRAGIMAGE, LPDATAOBJECT)
        def InitializeFromBitmap(self, pshdi: IPointer[SHDRAGIMAGE], pDataObject: IPointer[IDataObject]) -> int: ...

        @virtual_table.com_function(HWND, PTR(POINT), LPDATAOBJECT)
        def InitializeFromWindow(self, hwnd: int, ppt: IPointer[POINT], pDataObject: IPointer[IDataObject]) -> int: ...

        virtual_table.build()


SLR_NONE = 0x0
SLR_NO_UI = 0x0001
SLR_ANY_MATCH = 0x0002
SLR_UPDATE = 0x0004
SLR_NOUPDATE = 0x0008
SLR_NOSEARCH = 0x0010
SLR_NOTRACK = 0x0020
SLR_NOLINKINFO = 0x0040
SLR_INVOKE_MSI = 0x0080
SLR_NO_UI_WITH_MSG_PUMP = 0x0101
SLR_OFFER_DELETE_WITHOUT_FILE = 0x0200
SLR_KNOWNFOLDER = 0x0400
SLR_MACHINE_IN_LOCAL_TARGET = 0x0800
SLR_UPDATE_MACHINE_AND_SID = 0x1000
SLR_NO_OBJECT_ID = 0x2000
SLR_FLAGS = INT

SLGP_SHORTPATH = 0x0001
SLGP_UNCPRIORITY = 0x0002
SLGP_RAWPATH = 0x0004
SLGP_RELATIVEPRIORITY = 0x0008
SLGP_FLAGS = INT

class IShellLinkA(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214EE-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPSTR, INT, PTR(WIN32_FIND_DATAA), DWORD)
    def GetPath(self, pszFile: LPSTR, cch: int, pfd: IPointer[WIN32_FIND_DATAA], fFlags: int) -> int: ...

    @virtual_table.com_function(PTR(PITEMID_CHILD))
    def GetIDList(self, ppidl: IDoublePtr[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD)
    def SetIDList(self, pidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(LPSTR, INT)
    def GetDescription(self, pszName: LPSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCSTR)
    def SetDescription(self, pszName: LPCSTR) -> int: ...

    @virtual_table.com_function(LPSTR, INT)
    def GetWorkingDirectory(self, pszDir: LPSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCSTR)
    def SetWorkingDirectory(self, pszDir: LPCSTR) -> int: ...

    @virtual_table.com_function(LPSTR, INT)
    def GetArguments(self, pszArgs: LPSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCSTR)
    def SetArguments(self, pszArgs: LPCSTR) -> int: ...

    @virtual_table.com_function(PTR(WORD))
    def GetHotkey(self, pwHotkey: IPointer[WORD]) -> int: ...

    @virtual_table.com_function(WORD)
    def SetHotkey(self, wHotkey: int) -> int: ...

    @virtual_table.com_function(PTR(INT))
    def GetShowCmd(self, piShowCmd: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT)
    def SetShowCmd(self, iShowCmd: int) -> int: ...

    @virtual_table.com_function(LPSTR, INT, PTR(INT))
    def GetIconLocation(self, pszIconPath: LPSTR, cch: int, piIcon: IPointer[INT]) -> int: ...

    @virtual_table.com_function(LPCSTR, INT)
    def SetIconLocation(self, pszIconPath: LPCSTR, iIcon: int) -> int: ...

    @virtual_table.com_function(LPCSTR, DWORD)
    def SetRelativePath(self, pszPathRel: LPCSTR, dwReserved: int) -> int: ...

    @virtual_table.com_function(HWND, DWORD)
    def Resolve(self, hwnd: int, fFlags: int) -> int: ...

    @virtual_table.com_function(LPCSTR)
    def SetPath(self, pszFile: LPCSTR) -> int: ...

    virtual_table.build()

class IShellLinkW(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214F9-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPWSTR, INT, PTR(WIN32_FIND_DATAA), DWORD)
    def GetPath(self, pszFile: LPWSTR, cch: int, pfd: IPointer[WIN32_FIND_DATAA], fFlags: int) -> int: ...

    @virtual_table.com_function(PTR(PITEMID_CHILD))
    def GetIDList(self, ppidl: IDoublePtr[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PITEMID_CHILD)
    def SetIDList(self, pidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(LPWSTR, INT)
    def GetDescription(self, pszName: LPWSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetDescription(self, pszName: LPCWSTR) -> int: ...

    @virtual_table.com_function(LPWSTR, INT)
    def GetWorkingDirectory(self, pszDir: LPWSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetWorkingDirectory(self, pszDir: LPCWSTR) -> int: ...

    @virtual_table.com_function(LPWSTR, INT)
    def GetArguments(self, pszArgs: LPWSTR, cch: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetArguments(self, pszArgs: LPCWSTR) -> int: ...

    @virtual_table.com_function(PTR(WORD))
    def GetHotkey(self, pwHotkey: IPointer[WORD]) -> int: ...

    @virtual_table.com_function(WORD)
    def SetHotkey(self, wHotkey: int) -> int: ...

    @virtual_table.com_function(PTR(INT))
    def GetShowCmd(self, piShowCmd: IPointer[INT]) -> int: ...

    @virtual_table.com_function(INT)
    def SetShowCmd(self, iShowCmd: int) -> int: ...

    @virtual_table.com_function(LPWSTR, INT, PTR(INT))
    def GetIconLocation(self, pszIconPath: LPWSTR, cch: int, piIcon: IPointer[INT]) -> int: ...

    @virtual_table.com_function(LPCWSTR, INT)
    def SetIconLocation(self, pszIconPath: LPCWSTR, iIcon: int) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD)
    def SetRelativePath(self, pszPathRel: LPCWSTR, dwReserved: int) -> int: ...

    @virtual_table.com_function(HWND, DWORD)
    def Resolve(self, hwnd: int, fFlags: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def SetPath(self, pszFile: LPCWSTR) -> int: ...

    virtual_table.build()

if cpreproc.ifdef("UNICODE"):
    IShellLink = IShellLinkW
else:
    IShellLink = IShellLinkA


class IShellLinkDataList(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{45e2b4ae-b1c3-11d0-b92f-00a0c90312e1}")

    @virtual_table.com_function(PVOID)
    def AddDataBlock(self, pDataBlock: PVOID) -> int: ...

    @virtual_table.com_function(DWORD, PVOID, PVOID)
    def CopyDataBlock(self, dwSig: int, ppDataBlock: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(DWORD)
    def RemoveDataBlock(self, dwSig: int) -> int: ...

    @virtual_table.com_function(PTR(DWORD))
    def GetFlags(self, pdwFlags: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetFlags(self, dwFlags: int) -> int: ...

    virtual_table.build()

if _version >= WIN32_WINNT_WIN2K:
    class IResolveShellLink(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{5cd52983-9449-11d2-963a-00c04f79adf0}")

        @virtual_table.com_function(LPUNKNOWN, HWND, DWORD)
        def ResolveShellLink(self, punkLink: IPointer[IUnknown], hwnd: int, fFlags: int) -> int: ...

        virtual_table.build()


SPINITF_NORMAL = 0
SPINITF_MODAL = 1
SPINITF_NOMINIMIZE = 8
SPINITF = INT

class IActionProgressDialog(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{49ff1172-eadc-446d-9285-156453a6431c}")

    @virtual_table.com_function(SPINITF, LPCWSTR, LPCWSTR)
    def Initialize(self, flags: int, pszTitle: LPCWSTR, pszCancel: LPCWSTR) -> int: ...

    @virtual_table.com_function()
    def Stop(self) -> int: ...

    virtual_table.build()

ARCONTENT_AUTORUNINF = 0x00000002
ARCONTENT_AUDIOCD = 0x00000004
ARCONTENT_DVDMOVIE = 0x00000008
ARCONTENT_BLANKCD = 0x00000010
ARCONTENT_BLANKDVD = 0x00000020
ARCONTENT_UNKNOWNCONTENT = 0x00000040
ARCONTENT_AUTOPLAYPIX = 0x00000080
ARCONTENT_AUTOPLAYMUSIC = 0x00000100
ARCONTENT_AUTOPLAYVIDEO = 0x00000200
if _version >= WIN32_WINNT_VISTA:
    ARCONTENT_VCD = 0x00000400
    ARCONTENT_SVCD = 0x00000800
    ARCONTENT_DVDAUDIO = 0x00001000
    ARCONTENT_BLANKBD = 0x00002000
    ARCONTENT_BLURAY = 0x00004000
    ARCONTENT_CAMERASTORAGE = 0x00008000
    ARCONTENT_CUSTOMEVENT = 0x00010000
    ARCONTENT_NONE = 0x00000000
    ARCONTENT_MASK = 0x0001FFFE
    ARCONTENT_PHASE_UNKNOWN = 0x00000000
    ARCONTENT_PHASE_PRESNIFF = 0x10000000
    ARCONTENT_PHASE_SNIFFING = 0x20000000
    ARCONTENT_PHASE_FINAL = 0x40000000
    ARCONTENT_PHASE_MASK = 0x70000000


SPBEGINF_NORMAL = 0
SPBEGINF_AUTOTIME = 2
SPBEGINF_NOPROGRESSBAR = 16
SPBEGINF_MARQUEEPROGRESS = 32
SPBEGINF_NOCANCELBUTTON = 64
SPBEGINF = INT

SPACTION_NONE = 0
SPACTION_MOVING = 1
SPACTION_COPYING = 2
SPACTION_RECYCLING = 3
SPACTION_APPLYINGATTRIBS = 4
SPACTION_DOWNLOADING = 5
SPACTION_SEARCHING_INTERNET = 6
SPACTION_CALCULATING = 7
SPACTION_UPLOADING = 8
SPACTION_SEARCHING_FILES = 9
SPACTION_DELETING = 10
SPACTION_RENAMING = 11
SPACTION_FORMATTING = 12
SPACTION_COPY_MOVING = 13
SPACTION = INT

SPTEXT_ACTIONDESCRIPTION = 1
SPTEXT_ACTIONDETAIL = 2
SPTEXT = INT

class IActionProgress(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{49ff1173-eadc-446d-9285-156453a6431c}")

    @virtual_table.com_function(SPACTION, SPBEGINF)
    def Begin(self, action: int, flags: int) -> int: ...

    @virtual_table.com_function(ULONGLONG, ULONGLONG)
    def UpdateProgress(self, ulCompleted: ULONGLONG, ulTotal: ULONGLONG) -> int: ...

    @virtual_table.com_function(SPTEXT, LPCWSTR, BOOL)
    def UpdateText(self, spText: int, pszText: LPCWSTR, fMayCompact: bool) -> int: ...

    @virtual_table.com_function(PTR(BOOL))
    def QueryCancel(self, pfCancelled: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function()
    def ResetCancel(self) -> int: ...

    @virtual_table.com_function()
    def End(self) -> int: ...

    virtual_table.build()

class IShellExtInit(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214E8-0000-0000-C000-000000000046}")

    @virtual_table.com_function(PITEMID_CHILD, LPDATAOBJECT, HKEY)
    def Initialize(self, pidlFolder: IPointer[ITEMID_CHILD], pdtObj: IPointer[IDataObject], hkeyProgID: int) -> int: ...

    virtual_table.build()

LPSHELLEXTINIT = IShellExtInit.PTR()

EXPPS_FILETYPES = 1
EXPPS = INT

class IShellPropSheetExt(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214E9-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPFNSVADDPROPSHEETPAGE, LPARAM)
    def AddPages(self, pfnAddPage: FARPROC, lParam: int) -> int: ...

    @virtual_table.com_function(EXPPS, LPFNSVADDPROPSHEETPAGE, LPARAM)
    def ReplacePage(self, uPageID: int, pfnReplaceWith: FARPROC, lParam: int) -> int: ...

    virtual_table.build()

LPSHELLPROPSHEETEXT = IShellPropSheetExt.PTR()

class IRemoteComputer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{000214FE-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPCWSTR, BOOL)
    def Initialize(self, pszMachine: LPCWSTR, bEnumerating: bool) -> int: ...

    virtual_table.build()

class IQueryContinue(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7307055c-b24a-486b-9f25-163e597a28a9}")

    @virtual_table.com_function()
    def QueryContinue(self) -> int: ...

    virtual_table.build()

class IObjectWithCancelEvent(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{F279B885-0AE9-4b85-AC06-DDECF9408941}")

    @virtual_table.com_function(PTR(HANDLE))
    def GetCancelEvent(self, phEvent: IPointer[HANDLE]) -> int: ...

    virtual_table.build()

class IUserNotification(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{ba9711ba-5893-4787-a7e1-41277151550b}")

    @virtual_table.com_function(LPCWSTR, LPCWSTR, DWORD)
    def SetBalloonInfo(self, pszTitle: LPCWSTR, pszText: LPCWSTR, dwInfoFlags: int) -> int: ...

    @virtual_table.com_function(DWORD, DWORD, UINT)
    def SetBalloonRetry(self, dwShowTime: int, dwInterval: int, cRetryCount: int) -> int: ...

    @virtual_table.com_function(HICON, LPCWSTR)
    def SetIconInfo(self, hIcon: int, pszToolTip: LPCWSTR) -> int: ...

    @virtual_table.com_function(PTR(IQueryContinue), DWORD)
    def Show(self, pqc: IPointer[IQueryContinue], dwContinuePollInterval: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def PlaySound(self, pszSoundName: LPCWSTR) -> int: ...

    virtual_table.build()

class IItemNameLimits(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1df0d7f1-b267-4d28-8b10-12e23202a5c4}")

    @virtual_table.com_function(PTR(LPWSTR), PTR(LPWSTR))
    def GetValidCharacters(self, ppwszValidChars: IPointer[LPWSTR], ppwszInvalidChars: IPointer[LPWSTR]) -> int: ...

    @virtual_table.com_function(LPCWSTR, PTR(INT))
    def GetMaxLength(self, pszName: LPCWSTR, piMaxNameLen: IPointer[INT]) -> int: ...

    virtual_table.build()

if _version >= WIN32_WINNT_VISTA:
    class ISearchFolderItemFactory(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{a0ffbc28-5482-4366-be27-3e81e78e06c2}")

        @virtual_table.com_function(LPCWSTR)
        def SetDisplayName(self, pszDisplayName: LPCWSTR) -> int: ...

        @virtual_table.com_function(GUID)
        def SetFolderTypeID(self, ftid: GUID) -> int: ...

        @virtual_table.com_function(FOLDERLOGICALVIEWMODE)
        def SetFolderLogicalViewMode(self, flvm: int) -> int: ...

        @virtual_table.com_function(INT)
        def SetIconSize(self, iIconSize: int) -> int: ...

        @virtual_table.com_function(UINT, LPPROPERTYKEY)
        def SetVisibleColumns(self, cVisibleColumns: int, rgKey: IPointer[PROPERTYKEY]) -> int: ...

        @virtual_table.com_function(UINT, PTR(SORTCOLUMN))
        def SetSortColumns(self, cSortColumns: int, rgSortColumns: IPointer[SORTCOLUMN]) -> int: ...

        @virtual_table.com_function(LPPROPERTYKEY, intermediate_method = True)
        def SetGroupColumn(self, keyGroup: PROPERTYKEY, **kwargs) -> int:
            return self.virt_delegate(keyGroup)

        @virtual_table.com_function(UINT, LPPROPERTYKEY)
        def SetStacks(self, cStacksKeys: int, rgStackKeys: IPointer[PROPERTYKEY]) -> int: ...

        @virtual_table.com_function(PTR(IShellItemArray))
        def SetScope(self, psiaScope: IPointer[IShellItemArray]) -> int: ...

        @virtual_table.com_function(PTR(ICondition))
        def SetCondition(self, pCondition: IPointer[ICondition]) -> int: ...

        @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
        def GetShellItem(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid, ppv)

        @virtual_table.com_function(PTR(PITEMID_CHILD))
        def GetIDList(self, ppidl: IDoublePtr[ITEMID_CHILD]) -> int: ...

        virtual_table.build()


IEI_PRIORITY_MAX = ITSAT_MAX_PRIORITY
IEI_PRIORITY_MIN = ITSAT_MIN_PRIORITY
IEIT_PRIORITY_NORMAL = ITSAT_DEFAULT_PRIORITY

IEIFLAG_ASYNC = 0x0001
IEIFLAG_CACHE = 0x0002
IEIFLAG_ASPECT = 0x0004
IEIFLAG_OFFLINE = 0x0008
IEIFLAG_GLEAM = 0x0010
IEIFLAG_SCREEN = 0x0020
IEIFLAG_ORIGSIZE = 0x0040
IEIFLAG_NOSTAMP = 0x0080
IEIFLAG_NOBORDER = 0x0100
IEIFLAG_QUALITY = 0x0200
IEIFLAG_REFRESH = 0x0400

class IExtractImage(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{BB2E617C-0920-11d1-9A0B-00C04FC2D6C1}")

    @virtual_table.com_function(LPWSTR, DWORD, PTR(DWORD), PTR(SIZE), DWORD, PTR(DWORD))
    def GetLocation(self, pszPathBuffer: LPWSTR, cch: int, pdwPriority: IPointer[DWORD], prgSize: IPointer[SIZE], dwRecClrDepth: int, pdwFlags: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(PTR(HBITMAP))
    def Extract(self, phBmpThumbnail: IPointer[HBITMAP]) -> int: ...

    virtual_table.build()

LPEXTRACTIMAGE = IExtractImage.PTR()

class IExtractImage2(IExtractImage):
    virtual_table = COMVirtualTable.from_ancestor(IExtractImage)
    _iid_ = IID("{953BB1EE-93B4-11d1-98A3-00C04FB687DA}")

    @virtual_table.com_function(LPFILETIME)
    def GetDateStamp(self, pDateStamp: IPointer[FILETIME]) -> int: ...

    virtual_table.build()

class IThumbnailHandlerFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{e35b4b2e-00da-4bc1-9f13-38bc11f5d417}")

    @virtual_table.com_function(PITEMID_CHILD, LPBINDCTX, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetThumbnailHandler(self, pidlChild: IPointer[ITEMID_CHILD], pbc: IPointer[IBindCtx], iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pidlChild, iid.ref() if iid else NULL, iid, ppv)

    virtual_table.build()

class IParentAndItem(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{b3a4b685-b685-4805-99d9-5dead2873236}")

    @virtual_table.com_function(PITEMID_CHILD, PTR(IShellFolder), PITEMID_CHILD)
    def SetParentAndItem(self, pidlParent: IPointer[ITEMID_CHILD], psf: IPointer[IShellFolder], pidlChild: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PTR(PITEMID_CHILD), DOUBLE_PTR(IShellFolder), PTR(PITEMID_CHILD))
    def GetParentAndItem(self, ppidlParent: IDoublePtr[ITEMID_CHILD], ppsf: IDoublePtr[IShellFolder], ppidlChild: IDoublePtr[ITEMID_CHILD]) -> int: ...

    virtual_table.build()

class IDockingWindow(IOleWindow):
    virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
    _iid_ = IID("{012dd920-7b26-11d0-8ca9-00a0c92dbfe8}")

    @virtual_table.com_function(BOOL)
    def ShowDW(self, fShow: bool) -> int: ...

    @virtual_table.com_function(DWORD)
    def CloseDW(self, dwReserved: int) -> int: ...

    @virtual_table.com_function(PRECT, LPUNKNOWN, BOOL)
    def ResizeBorderDW(self, prcBorder: IPointer[RECT], punkToolbarSite: IPointer[IUnknown], fReserved: bool) -> int: ...

    virtual_table.build()

DBIM_MINSIZE = 0x0001
DBIM_MAXSIZE = 0x0002
DBIM_INTEGRAL = 0x0004
DBIM_ACTUAL = 0x0008
DBIM_TITLE = 0x0010
DBIM_MODEFLAGS = 0x0020
DBIM_BKCOLOR = 0x0040

@CStructure.make
class DESKBANDINFO(CStructure):
    dwMask: IDword
    ptMinSize: POINTL
    ptMaxSize: POINTL
    ptIntegral: POINTL
    ptActual: POINTL
    wszTitle: IWideCharArrayFixedSize[256]
    dwModeFlags: IDword
    crBkgnd: IInteger[COLORREF]

DBIMF_NORMAL = 0x0000
DBIMF_FIXED = 0x0001
DBIMF_FIXEDBMP = 0x0004
DBIMF_VARIABLEHEIGHT = 0x0008
DBIMF_UNDELETEABLE = 0x0010
DBIMF_DEBOSSED = 0x0020
DBIMF_BKCOLOR = 0x0040
DBIMF_USECHEVRON = 0x0080
DBIMF_BREAK = 0x0100
DBIMF_ADDTOFRONT = 0x0200
DBIMF_TOPALIGN = 0x0400
if _version >= WIN32_WINNT_VISTA:
    DBIMF_NOGRIPPER = 0x0800
    DBIMF_ALWAYSGRIPPER = 0x1000
    DBIMF_NOMARGINS = 0x2000


DBIF_VIEWMODE_NORMAL = 0x0000
DBIF_VIEWMODE_VERTICAL = 0x0001
DBIF_VIEWMODE_FLOATING = 0x0002
DBIF_VIEWMODE_TRANSPARENT = 0x0004

DBID_BANDINFOCHANGED = 0
DBID_SHOWONLY = 1
DBID_MAXIMIZEBAND = 2
DBID_PUSHCHEVRON = 3
DBID_DELAYINIT = 4
DBID_FINISHINIT = 5
DBID_SETWINDOWTHEME = 6
DBID_PERMITAUTOHIDE = 7
DESKBANDCID = INT

DBPC_SELECTFIRST = DWORD(-1).value
DBPC_SELECTLAST = DWORD(-2).value

class IDeskBand(IDockingWindow):
    virtual_table = COMVirtualTable.from_ancestor(IDockingWindow)
    _iid_ = IID("{EB0FE172-1A3A-11D0-89B3-00A0C90A90AC}")

    @virtual_table.com_function(DWORD, DWORD, PTR(DESKBANDINFO))
    def GetBandInfo(self, dwBandID: int, dwViewMode: int, pdbi: IPointer[DESKBANDINFO]) -> int: ...

    virtual_table.build()

CGID_IDeskBand = IDeskBand._iid_

if _version >= WIN32_WINNT_VISTA:
    class IDeskBandInfo(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{77E425FC-CBF9-4307-BA6A-BB5727745661}")

        @virtual_table.com_function(DWORD, DWORD, PTR(INT))
        def GetDefaultBandWidth(self, dwBandID: int, dwViewMode: int, pnWidth: IPointer[INT]) -> int: ...

        virtual_table.build()


class ITaskbarList(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{56FDF342-FD6D-11d0-958A-006097C9A090}")

    @virtual_table.com_function()
    def HrInit(self) -> int: ...

    @virtual_table.com_function(HWND)
    def AddTab(self, hwnd: int) -> int: ...

    @virtual_table.com_function(HWND)
    def DeleteTab(self, hwnd: int) -> int: ...

    @virtual_table.com_function(HWND)
    def ActivateTab(self, hwnd: int) -> int: ...

    @virtual_table.com_function(HWND)
    def SetActiveAlt(self, hwnd: int) -> int: ...

    virtual_table.build()

class ITaskbarList2(ITaskbarList):
    virtual_table = COMVirtualTable.from_ancestor(ITaskbarList)
    _iid_ = IID("{602D4995-B13A-429b-A66E-1935E44F4317}")

    @virtual_table.com_function(HWND, BOOL)
    def MarkFullscreenWindow(self, hwnd: int, fFullscreen: bool) -> int: ...

    virtual_table.build()

THBF_ENABLED = 0x00000000
THBF_DISABLED = 0x00000001
THBF_DISMISSONCLICK = 0x00000002
THBF_NOBACKGROUND = 0x00000004
THBF_HIDDEN = 0x00000008
THBF_NONINTERACTIVE = 0x00000010
THUMBBUTTONFLAGS = INT

THB_BITMAP = 0x00000001
THB_ICON = 0x00000002
THB_TOOLTIP = 0x00000004
THB_FLAGS = 0x00000008
THUMBBUTTONMASK = INT

@CStructure.make
class THUMBBUTTON(CStructure):
    dwMask: IInteger[THUMBBUTTONMASK]
    iId: IUint
    iBitmap: IUint
    hIcon: IInteger[HICON]
    szTip: IWideCharArrayFixedSize[260]
    dwFlags: IInteger[THUMBBUTTONFLAGS]

LPTHUMBBUTTON = LPTHUMBBUTTON

THBN_CLICKED = 0x1800

TBPF_NOPROGRESS = 0x00000000
TBPF_INDETERMINATE = 0x00000001
TBPF_NORMAL = 0x00000002
TBPF_ERROR = 0x00000004
TBPF_PAUSED = 0x00000008
TBPFLAG = INT

class ITaskbarList3(ITaskbarList2):
    virtual_table = COMVirtualTable.from_ancestor(ITaskbarList2)
    _iid_ = IID("{ea1afb91-9e28-4b86-90e9-9e9f8a5eefaf}")

    @virtual_table.com_function(HWND, ULONGLONG, ULONGLONG)
    def SetProgressValue(self, hwnd: int, ullCompleted: ULONGLONG, ullTotal: ULONGLONG) -> int: ...

    @virtual_table.com_function(HWND, TBPFLAG)
    def SetProgressState(self, hwnd: int, tbpFlags: int) -> int: ...

    @virtual_table.com_function(HWND, HWND)
    def RegisterTab(self, hwndTab: int, hwndMDI: int) -> int: ...

    @virtual_table.com_function(HWND)
    def UnregisterTab(self, hwndTab: int) -> int: ...

    @virtual_table.com_function(HWND, HWND)
    def SetTabOrder(self, hwndTab: int, hwndInsertBefore: int) -> int: ...

    @virtual_table.com_function(HWND, HWND, DWORD)
    def SetTabActive(self, hwndTab: int, hwndMDI: int, dwReserved: int) -> int: ...

    @virtual_table.com_function(HWND, UINT, LPTHUMBBUTTON)
    def ThumbBarAddButtons(self, hwnd: int, cButtons: int, pButton: IPointer[THUMBBUTTON]) -> int: ...

    @virtual_table.com_function(HWND, UINT, LPTHUMBBUTTON)
    def ThumbBarUpdateButtons(self, hwnd: int, cButtons: int, pButton: IPointer[THUMBBUTTON]) -> int: ...

    @virtual_table.com_function(HWND, HIMAGELIST)
    def ThumbBarSetImageList(self, hwnd: int, himl: int) -> int: ...

    @virtual_table.com_function(HWND, HICON, LPCWSTR)
    def SetOverlayIcon(self, hwnd: int, hIcon: int, pszDescription: LPCWSTR) -> int: ...

    @virtual_table.com_function(HWND, LPCWSTR)
    def SetThumbnailTooltip(self, hwnd: int, pszTip: LPCWSTR) -> int: ...

    @virtual_table.com_function(HWND, PRECT)
    def SetThumbnailClip(self, hwnd: int, prcClip: IPointer[RECT]) -> int: ...

    virtual_table.build()

STPF_NONE = 0x00000000
STPF_USEAPPTHUMBNAILALWAYS = 0x00000001
STPF_USEAPPTHUMBNAILWHENACTIVE = 0x00000002
STPF_USEAPPPEEKALWAYS = 0x00000004
STPF_USEAPPPEEKWHENACTIVE = 0x00000008
STPFLAG = INT

class ITaskbarList4(ITaskbarList3):
    virtual_table = COMVirtualTable.from_ancestor(ITaskbarList3)
    _iid_ = IID("{c43dc798-95d1-4bea-9030-bb99e2983a1a}")

    @virtual_table.com_function(HWND, STPFLAG)
    def SetTabProperties(self, hwndTab: int, stpFlags: int) -> int: ...

    virtual_table.build()

if WIN32_IE >= WIN32_IE_IE70:
    class IExplorerBrowserEvents(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{361bbdc7-e6ee-4e13-be58-58e2240c810f}")

        @virtual_table.com_function(PITEMID_CHILD)
        def OnNavigationPending(self, pidlFolder: IPointer[ITEMID_CHILD]) -> int: ...

        @virtual_table.com_function(PTR(IShellView))
        def OnViewCreated(self, psv: IPointer[IShellView]) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD)
        def OnNavigationComplete(self, pidlFolder: IPointer[ITEMID_CHILD]) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD)
        def OnNavigationFailed(self, pidlFolder: IPointer[ITEMID_CHILD]) -> int: ...

        virtual_table.build()

    EBO_NONE = 0x00000000
    EBO_NAVIGATEONCE = 0x00000001
    EBO_SHOWFRAMES = 0x00000002
    EBO_ALWAYSNAVIGATE = 0x00000004
    EBO_NOTRAVELLOG = 0x00000008
    EBO_NOWRAPPERWINDOW = 0x00000010
    EBO_HTMLSHAREPOINTVIEW = 0x00000020
    EBO_NOBORDER = 0x00000040
    EBO_NOPERSISTVIEWSTATE = 0x00000080
    EXPLORER_BROWSER_OPTIONS = INT

    EBF_NONE = 0x0000000
    EBF_SELECTFROMDATAOBJECT = 0x0000100
    EBF_NODROPTARGET = 0x0000200
    EXPLORER_BROWSER_FILL_FLAGS = INT

    class IExplorerBrowser(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{dfd3b6b5-c10c-4be9-85f6-a66969f402f6}")

        @virtual_table.com_function(HWND, PRECT, LPFOLDERSETTINGS)
        def Initialize(self, hwndParent: int, prc: IPointer[RECT], pfs: IPointer[FOLDERSETTINGS]) -> int: ...

        @virtual_table.com_function()
        def DestroyViewWindow(self) -> int: ...

        @virtual_table.com_function(PTR(HDWP), RECT)
        def SetRect(self, phdwp: IPointer[HDWP], rcBrowser: RECT) -> int: ...

        @virtual_table.com_function(LPCWSTR)
        def SetPropertyBag(self, pszPropertyBag: LPCWSTR) -> int: ...

        @virtual_table.com_function(LPCWSTR)
        def SetEmptyText(self, pszEmptyText: LPCWSTR) -> int: ...

        @virtual_table.com_function(LPFOLDERSETTINGS)
        def SetFolderSettings(self, pfs: IPointer[FOLDERSETTINGS]) -> int: ...

        @virtual_table.com_function(PTR(IExplorerBrowserEvents), PTR(DWORD))
        def Advise(self, psbe: IPointer[IExplorerBrowserEvents], pdwCookie: IPointer[DWORD]) -> int: ...

        @virtual_table.com_function(DWORD)
        def Unadvise(self, dwCookie: int) -> int: ...

        @virtual_table.com_function(EXPLORER_BROWSER_OPTIONS)
        def SetOptions(self, dwFlags: int) -> int: ...

        @virtual_table.com_function(PTR(EXPLORER_BROWSER_OPTIONS))
        def GetOptions(self, pdwFlag: IPointer[EXPLORER_BROWSER_OPTIONS]) -> int: ...

        @virtual_table.com_function(PITEMID_CHILD, UINT)
        def BrowseToIDList(self, pidl: IPointer[ITEMID_CHILD], uFlags: int) -> int: ...

        @virtual_table.com_function(LPUNKNOWN, UINT)
        def BrowseToObject(self, punk: IPointer[IUnknown], uFlags: int) -> int: ...

        @virtual_table.com_function(LPUNKNOWN, EXPLORER_BROWSER_FILL_FLAGS)
        def FillFromObject(self, punk: IPointer[IUnknown], dwFlags: int) -> int: ...

        @virtual_table.com_function()
        def RemoveAll(self) -> int: ...

        @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
        def GetCurrentView(self, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid, ppv)

        virtual_table.build()

    class IEnumObjects(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{2c1c7e2e-2d0e-4059-831e-1e6f82335c2e}")

        @virtual_table.com_function(ULONG, LPIID, PVOID, PVOID, PTR(ULONG), intermediate_method = True)
        def Next(self, celt: int, iid: IID, rgelt: IPointer[PVOID], pceltFetched: IPointer[ULONG], **kwargs) -> int:
            return self.virt_delegate(iid.ref() if iid else NULL, iid, rgelt, pceltFetched)

        @virtual_table.com_function(ULONG)
        def Skip(self, celt: int) -> int: ...

        @virtual_table.com_function()
        def Reset(self) -> int: ...

        @virtual_table.com_function(PVOID)
        def Clone(self, ppenum: IDoublePtr['IEnumObjects']) -> int: ...

        virtual_table.build()

    OPPROGDLG_DEFAULT = 0x00000000
    OPPROGDLG_ENABLEPAUSE = 0x00000080
    OPPROGDLG_ALLOWUNDO = 0x00000100
    OPPROGDLG_DONTDISPLAYSOURCEPATH = 0x00000200
    OPPROGDLG_DONTDISPLAYDESTPATH = 0x00000400
    OPPROGDLG_NOMULTIDAYESTIMATES = 0x00000800
    OPPROGDLG_DONTDISPLAYLOCATIONS = 0x00001000
    OPPROGDLGF = INT

    PDM_DEFAULT = 0x00000000
    PDM_RUN = 0x00000001
    PDM_PREFLIGHT = 0x00000002
    PDM_UNDOING = 0x00000004
    PDM_ERRORSBLOCKING = 0x00000008
    PDM_INDETERMINATE = 0x00000010
    PDMODE = INT

    PDOPS_RUNNING = 1
    PDOPS_PAUSED = 2
    PDOPS_CANCELLED = 3
    PDOPS_STOPPED = 4
    PDOPS_ERRORS = 5
    PDOPSTATUS = INT

    class IOperationsProgressDialog(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{0C9FB851-E5C9-43EB-A370-F0677B13874C}")

        @virtual_table.com_function(HWND, OPPROGDLGF)
        def StartProgressDialog(self, hwndOwner: int, flags: int) -> int: ...

        @virtual_table.com_function()
        def StopProgressDialog(self) -> int: ...

        @virtual_table.com_function(SPACTION)
        def SetOperation(self, action: int) -> int: ...

        @virtual_table.com_function(PDMODE)
        def SetMode(self, mode: int) -> int: ...

        @virtual_table.com_function(ULONGLONG, ULONGLONG, ULONGLONG, ULONGLONG, ULONGLONG, ULONGLONG)
        def UpdateProgress(self, ullPointsCurrent: ULONGLONG, ullPointsTotal: ULONGLONG, ullSizeCurrent: ULONGLONG, ullSizeTotal: ULONGLONG, ullItemsCurrent: ULONGLONG, ullItemsTotal: ULONGLONG) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), PTR(IShellItem))
        def UpdateLocations(self, psiSource: IPointer[IShellItem], psiTarget: IPointer[IShellItem], psiItem: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function()
        def ResetTimer(self) -> int: ...

        @virtual_table.com_function()
        def PauseTimer(self) -> int: ...

        @virtual_table.com_function()
        def ResumeTimer(self) -> int: ...

        @virtual_table.com_function(PTR(ULONGLONG), PTR(ULONGLONG))
        def GetMilliseconds(self, pullElapsed: IPointer[ULONGLONG], pullRemaining: IPointer[ULONGLONG]) -> int: ...

        @virtual_table.com_function(PTR(PDOPSTATUS))
        def GetOperationStatus(self, popstatus: IPointer[PDOPSTATUS]) -> int: ...

        virtual_table.build()

    class IIOCancelInformation(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{f5b0bf81-8cb5-4b1b-9449-1a159e0c733c}")

        @virtual_table.com_function(DWORD, UINT)
        def SetCancelInformation(self, dwThreadID: int, uMsgCancel: int) -> int: ...

        @virtual_table.com_function(PTR(DWORD), PTR(UINT))
        def GetCancelInformation(self, pdwThreadID: IPointer[DWORD], puMsgCancel: IPointer[UINT]) -> int: ...

        virtual_table.build()

    FOFX_NOSKIPJUNCTIONS = 0x00010000
    FOFX_PREFERHARDLINK = 0x00020000
    FOFX_SHOWELEVATIONPROMPT = 0x00040000
    FOFX_RECYCLEONDELETE = 0x00080000
    FOFX_EARLYFAILURE = 0x00100000
    FOFX_PRESERVEFILEEXTENSIONS = 0x00200000
    FOFX_KEEPNEWERFILE = 0x00400000
    FOFX_NOCOPYHOOKS = 0x00800000
    FOFX_NOMINIMIZEBOX = 0x01000000
    FOFX_MOVEACLSACROSSVOLUMES = 0x02000000
    FOFX_DONTDISPLAYSOURCEPATH = 0x04000000
    FOFX_DONTDISPLAYDESTPATH = 0x08000000
    FOFX_REQUIREELEVATION = 0x10000000
    FOFX_ADDUNDORECORD = 0x20000000
    FOFX_COPYASDOWNLOAD = 0x40000000
    FOFX_DONTDISPLAYLOCATIONS = 0x80000000

    class IFileOperation(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{947aab5f-0a5c-4c13-b4d6-4bf7836fc9f8}")

        @virtual_table.com_function(PTR(IFileOperationProgressSink), PTR(DWORD))
        def Advise(self, pfops: IPointer[IFileOperationProgressSink], pdwCookie: IPointer[DWORD]) -> int: ...

        @virtual_table.com_function(DWORD)
        def Unadvise(self, dwCookie: int) -> int: ...

        @virtual_table.com_function(DWORD)
        def SetOperationFlags(self, dwOperationFlags: int) -> int: ...

        @virtual_table.com_function(LPCWSTR)
        def SetProgressMessage(self, pszMessage: LPCWSTR) -> int: ...

        @virtual_table.com_function(PTR(IOperationsProgressDialog))
        def SetProgressDialog(self, popd: IPointer[IOperationsProgressDialog]) -> int: ...

        @virtual_table.com_function(PTR(IPropertyChangeArray))
        def SetProperties(self, pproparray: IPointer[IPropertyChangeArray]) -> int: ...

        @virtual_table.com_function(HWND)
        def SetOwnerWindow(self, hwndOwner: int) -> int: ...

        @virtual_table.com_function(PTR(IShellItem))
        def ApplyPropertiesToItem(self, psiItem: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(LPUNKNOWN)
        def ApplyPropertiesToItems(self, punkItems: IPointer[IUnknown]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), LPCWSTR, PTR(IFileOperationProgressSink))
        def RenameItem(self, psiItem: IPointer[IShellItem], pszNewName: LPCWSTR, pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function(LPUNKNOWN, LPCWSTR)
        def RenameItems(self, pUnkItems: IPointer[IUnknown], pszNewName: LPCWSTR) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), LPCWSTR, PTR(IFileOperationProgressSink))
        def MoveItem(self, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszNewName: LPCWSTR, pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function(LPUNKNOWN, PTR(IShellItem))
        def MoveItems(self, punkItems: IPointer[IUnknown], psiDestinationFolder: IPointer[IShellItem]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IShellItem), LPCWSTR, PTR(IFileOperationProgressSink))
        def CopyItem(self, psiItem: IPointer[IShellItem], psiDestinationFolder: IPointer[IShellItem], pszCopyName: LPCWSTR, pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function(LPUNKNOWN, PTR(IFileOperationProgressSink))
        def CopyItems(self, punkItems: IPointer[IUnknown], pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), PTR(IFileOperationProgressSink))
        def DeleteItem(self, psiItem: IPointer[IShellItem], pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function(LPUNKNOWN)
        def DeleteItems(self, punkItems: IPointer[IUnknown]) -> int: ...

        @virtual_table.com_function(PTR(IShellItem), DWORD, LPCWSTR, LPCWSTR, PTR(IFileOperationProgressSink))
        def NewItem(self, psiDestinationFolder: IPointer[IShellItem], dwFileAttributes: int, pszName: LPCWSTR, pszTemplateName: LPCWSTR, pfopsItem: IPointer[IFileOperationProgressSink]) -> int: ...

        @virtual_table.com_function()
        def PerformOperations(self) -> int: ...

        @virtual_table.com_function(PTR(BOOL))
        def GetAnyOperationsAborted(self, pfAnyOperationsAborted: IPointer[BOOL]) -> int: ...

        virtual_table.build()

    class IObjectProvider(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{a6087428-3be3-4d73-b308-7c04a540bf1af5b0bf81-8cb5-4b1b-9449-1a159e0c733c}")

        @virtual_table.com_function(LPGUID, LPIID, PVOID, PVOID, intermediate_method = True)
        def QueryObject(self, guidObject: GUID, iid: IID, ppvOut: IPointer[PVOID], **kwargs) -> int:
            return self.virt_delegate(iid.ref() if iid else NULL, iid, ppvOut)

        virtual_table.build()


if _version >= WIN32_WINNT_WIN10:
    FOF2_NONE = 0x00000000
    FOF2_MERGEFOLDERSONCOLLISION = 0x00000001
    FILE_OPERATION_FLAGS2 = INT

    class IFileOperation2(IFileOperation):
        virtual_table = COMVirtualTable.from_ancestor(IFileOperation)
        _iid_ = IID("{cd8f23c1-8f61-4916-909d-55bdd0918753}")

        @virtual_table.com_function(FILE_OPERATION_FLAGS2)
        def SetOperationFlags2(self, operationFlags2: int) -> int: ...

        virtual_table.build()


class INamespaceWalkCB(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{d92995f8-cf5e-4a76-bf59-ead39ea2b97e}")

    @virtual_table.com_function(PTR(IShellFolder), PITEMID_CHILD)
    def FoundItem(self, psf: IPointer[IShellFolder], pidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PTR(IShellFolder), PITEMID_CHILD)
    def EnterFolder(self, psf: IPointer[IShellFolder], pidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PTR(IShellFolder), PITEMID_CHILD)
    def LeaveFolder(self, psf: IPointer[IShellFolder], pidl: IPointer[ITEMID_CHILD]) -> int: ...

    @virtual_table.com_function(PTR(LPWSTR), PTR(LPWSTR))
    def InitializeProgressDialog(self, ppszTitle: IPointer[LPWSTR], ppszCancel: IPointer[LPWSTR]) -> int: ...

    virtual_table.build()

if WIN32_IE >= WIN32_IE_IE70:
    class INamespaceWalkCB2(INamespaceWalkCB):
        virtual_table = COMVirtualTable.from_ancestor(INamespaceWalkCB)
        _iid_ = IID("{7ac7492b-c38e-438a-87db-68737844ff70}")

        @virtual_table.com_function(HRESULT)
        def WalkComplete(self, hr: int) -> int: ...

        virtual_table.build()


NSWF_DEFAULT = 0x00000000
NSWF_NONE_IMPLIES_ALL = 0x00000001
NSWF_ONE_IMPLIES_ALL = 0x00000002
NSWF_DONT_TRAVERSE_LINKS = 0x00000004
NSWF_DONT_ACCUMULATE_RESULT = 0x00000008
NSWF_TRAVERSE_STREAM_JUNCTIONS = 0x00000010
NSWF_FILESYSTEM_ONLY = 0x00000020
NSWF_SHOW_PROGRESS = 0x00000040
NSWF_FLAG_VIEWORDER = 0x00000080
NSWF_IGNORE_AUTOPLAY_HIDA = 0x00000100
NSWF_ASYNC = 0x00000200
NSWF_DONT_RESOLVE_LINKS = 0x00000400
NSWF_ACCUMULATE_FOLDERS = 0x00000800
NSWF_DONT_SORT = 0x00001000
NSWF_USE_TRANSFER_MEDIUM = 0x00002000
NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS = 0x00004000
NSWF_ANY_IMPLIES_ALL = 0x00008000
NAMESPACEWALKFLAG = INT

class INamespaceWalk(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{57ced8a7-3f4a-432c-9350-30f24483f74f}")

    @virtual_table.com_function(LPUNKNOWN, DWORD, INT, PTR(INamespaceWalkCB))
    def Walk(self, punkToWalk: IPointer[IUnknown], dwFlags: int, cDepth: int, pnswcb: IPointer[INamespaceWalkCB]) -> int: ...

    @virtual_table.com_function(PTR(UINT), PTR(PTR(PITEMID_CHILD)))
    def GetIDArrayResult(self, pcItems: IPointer[UINT], prgpidl: IPointer[IPointer[IPointer[ITEMID_CHILD]]]) -> int: ...

    virtual_table.build()

def FreeIDListArray(ppidls: IDoublePtr[ITEMIDLIST], cItems: int):
	for i in range(cItems):
		CoTaskMemFree(ppidls[i])
	CoTaskMemFree(ppidls)

FreeIDListArrayFull = FreeIDListArrayChild = FreeIDListArray

@CStructure.make
class BANDSITEINFO(CStructure):
    dwMask: IDword
    dwState: IDword
    dwStyle: IDword

BSID_BANDADDED = 0
BSID_BANDREMOVED = 1
BANDSITECID = INT

BSIM_STATE = 0x00000001
BSIM_STYLE = 0x00000002

BSSF_VISIBLE = 0x00000001
BSSF_NOTITLE = 0x00000002
BSSF_UNDELETEABLE = 0x00001000

BSIS_AUTOGRIPPER = 0x00000000
BSIS_NOGRIPPER = 0x00000001
BSIS_ALWAYSGRIPPER = 0x00000002
BSIS_LEFTALIGN = 0x00000004
BSIS_SINGLECLICK = 0x00000008
BSIS_NOCONTEXTMENU = 0x00000010
BSIS_NODROPTARGET = 0x00000020
BSIS_NOCAPTION = 0x00000040
BSIS_PREFERNOLINEBREAK = 0x00000080
BSIS_LOCKED = 0x00000100
if WIN32_IE >= WIN32_IE_IE70:
    BSIS_PRESERVEORDERDURINGLAYOUT = 0x00000200
    BSIS_FIXEDORDER = 0x00000400


class IBandSite(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{4CF504B0-DE96-11D0-8B3F-00A0C911E8E5}")

    @virtual_table.com_function(LPUNKNOWN)
    def AddBand(self, punk: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(UINT, PTR(DWORD))
    def EnumBands(self, uBand: int, pdwBandID: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(DWORD, DOUBLE_PTR(IDeskBand), PTR(DWORD), LPWSTR, INT)
    def QueryBand(self, dwBandID: int, ppstb: IDoublePtr[IDeskBand], pdwState: IPointer[DWORD], pszName: LPWSTR, cchName: int) -> int: ...

    @virtual_table.com_function(DWORD, DWORD, DWORD)
    def SetBandState(self, dwBandID: int, dwMask: int, dwState: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def RemoveBand(self, dwBandID: int) -> int: ...

    @virtual_table.com_function(DWORD, LPIID, PVOID, PVOID, intermediate_method = True)
    def GetBandObject(self, dwBandID: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref() if iid else NULL, iid, ppv)

    @virtual_table.com_function(PTR(BANDSITEINFO))
    def SetBandSiteInfo(self, pbsinfo: IPointer[BANDSITEINFO]) -> int: ...

    @virtual_table.com_function(PTR(BANDSITEINFO))
    def GetBandSiteInfo(self, pbsinfo: IPointer[BANDSITEINFO]) -> int: ...

    virtual_table.build()

SID_SBandSite = IBandSite._iid_
CGID_BandSite = IBandSite._iid_
class IModalWindow(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{b4db1657-70d7-485e-8e3e-6fcb5a5c1802}")

    @virtual_table.com_function(HWND)
    def Show(self, hwndOwner: int) -> int: ...

    virtual_table.build()

class IContextMenuSite(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{0811AEBE-0B87-4C54-9E72-548CF649016B}")

    @virtual_table.com_function(LPUNKNOWN, UINT, POINT)
    def DoContextMenuPopup(self, punkContextMenu: IPointer[IUnknown], fFlags: int, pt: POINT) -> int: ...

    virtual_table.build()

MBHANDCID_PIDLSELECT = 0
MENUBANDHANDLERCID = INT

class IMenuBand(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{568804CD-CBD7-11d0-9816-00C04FD91972}")

    @virtual_table.com_function(PMSG)
    def IsMenuMessage(self, pmsg: IPointer[MSG]) -> int: ...

    @virtual_table.com_function(PMSG, PTR(LRESULT))
    def TranslateMenuMessage(self, pmsg: IPointer[MSG], plRet: IPointer[LRESULT]) -> int: ...

    virtual_table.build()

class IRegTreeItem(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{A9521922-0812-4d44-9EC3-7FD38C726F3D}")

    @virtual_table.com_function(PTR(BOOL))
    def GetCheckState(self, pbCheck: IPointer[BOOL]) -> int: ...

    @virtual_table.com_function(BOOL)
    def SetCheckState(self, bCheck: bool) -> int: ...

    virtual_table.build()

class IDeskBar(IOleWindow):
    virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
    _iid_ = IID("{EB0FE173-1A3A-11D0-89B3-00A0C90A90AC}")

    @virtual_table.com_function(LPUNKNOWN)
    def SetClient(self, punkClient: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def GetClient(self, ppunkClient: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PRECT)
    def OnPosRecChangeDB(self, prc: IPointer[RECT]) -> int: ...

    virtual_table.build()

MPOS_EXECUTE = 0
MPOS_FULLCANCEL = 1
MPOS_CANCELLEVEL = 2
MPOS_SELECTLEFT = 3
MPOS_SELECTRIGHT = 4
MPOS_CHILDTRACKING = 5
MENUPOPUPSELECT = INT

MPPF_SETFOCUS = 0x00000001
MPPF_INITIALSELECT = 0x00000002
MPPF_NOANIMATE = 0x00000004
MPPF_KEYBOARD = 0x00000010
MPPF_REPOSITION = 0x00000020
MPPF_FORCEZORDER = 0x00000040
MPPF_FINALSELECT = 0x00000080
MPPF_TOP = 0x20000000
MPPF_LEFT = 0x40000000
MPPF_RIGHT = 0x60000000
MPPF_BOTTOM = 0x80000000
MPPF_POS_MASK = 0xE0000000
MPPF_ALIGN_LEFT = 0x02000000
MPPF_ALIGN_RIGHT = 0x04000000
MP_POPUPFLAGS = INT

class IMenuPopup(IDeskBar):
    virtual_table = COMVirtualTable.from_ancestor(IDeskBar)
    _iid_ = IID("{D1E7AFEB-6A2E-11d0-8C78-00C04FD918B4}")

    @virtual_table.com_function(PTR(POINTL), PTR(RECTL), MP_POPUPFLAGS)
    def Popup(self, ppt: IPointer[POINTL], prcExclude: IPointer[RECTL], dwFlags: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def OnSelect(self, dwSelectType: int) -> int: ...

    @virtual_table.com_function(PVOID, BOOL)
    def SetSubMenu(self, pmp: IPointer['IMenuPopup'], fSet: bool) -> int: ...

    virtual_table.build()

FUT_PLAYING = 0
FUT_EDITING = 1
FUT_GENERIC = 2
FILE_USAGE_TYPE = INT

OF_CAP_CANSWITCHTO = 0x0001
OF_CAP_CANCLOSE = 0x0002

class IFileIsInUse(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{64a1cbf0-3a1a-4461-9158-376969693950}")

    @virtual_table.com_function(PTR(LPWSTR))
    def GetAppName(self, ppszName: IPointer[LPWSTR]) -> int: ...

    @virtual_table.com_function(PTR(FILE_USAGE_TYPE))
    def GetUsage(self, pfut: IPointer[FILE_USAGE_TYPE]) -> int: ...

    @virtual_table.com_function(PTR(DWORD))
    def GetCapabilities(self, pdwCapFlags: IPointer[DWORD]) -> int: ...

    @virtual_table.com_function(PTR(HWND))
    def GetSwitchToHWND(self, phwnd: IPointer[HWND]) -> int: ...

    @virtual_table.com_function()
    def CloseFile(self) -> int: ...

    virtual_table.build()

