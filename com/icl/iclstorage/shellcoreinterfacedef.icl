.icl
.ver 100

.gencomment

//
// shellcoreinterfacedef.icl
//
// analogue of ShObjIdl_core.h
//

imports
{
	// local imports
	import .ctlinterfacedef
	import .objectarray
	
	// win imports
	import ..shtypes
	import ..shellapi
}

// [Generator-Only] Declarations to generator type/pointer map
silent
{
	pie ITEMIDLIST_ABSOLUTE PIDLIST_ABSOLUTE PCIDLIST_ABSOLUTE
	pie TASKOWNERID REFTASKOWNERID
	pie IBindCtx LPBINDCTX
	pie ITEMID_CHILD PITEMID_CHILD
	pie STRRET LPSTRRET
	pie SHCOLUMNID LPCSHCOLUMNID
	pie SHELLDETAILS LPSHELLDETAILS
	pie VARIANT LPVARIANT
}

// [Generator-Only] Alias to generator type map
al int UINT_PTR LPARAM WPARAM DWORD_PTR SHCOLSTATEF

// QueryContextMenu uFlags
eq CMF_NORMAL 0x00000000
eq CMF_DEFAULTONLY 0x00000001
eq CMF_VERBSONLY 0x00000002
eq CMF_EXPLORE 0x00000004
eq CMF_NOVERBS 0x00000008
eq CMF_CANRENAME 0x00000010
eq CMF_NODEFAULT 0x00000020

ifver_l @VISTA
{
	eq CMF_INCLUDESTATIC 0x00000040
}

ifver @VISTA
{
	eq CMF_ITEMMENU 0x00000080
}

eq CMF_EXTENDEDVERBS 0x00000100
~

ifver @VISTA
{
	eq CMF_DISABLEDVERBS 0x00000200
}

eq CMF_ASYNCVERBSTATE 0x00000400
eq CMF_OPTIMIZEFORINVOKE 0x00000800
eq CMF_SYNCCASCADEMENU 0x00001000
eq CMF_DONOTPICKDEFAULT 0x00002000
eq CMF_RESERVED 0xffff0000
~

// GetCommandString uFlags
eq GCS_VERBA 0x00000000     // canonical verb
eq GCS_HELPTEXTA 0x00000001     // help text (for status bar)
eq GCS_VALIDATEA 0x00000002     // validate command exists
eq GCS_VERBW 0x00000004     // canonical verb (unicode)
eq GCS_HELPTEXTW 0x00000005     // help text (unicode version)
eq GCS_VALIDATEW 0x00000006     // validate command exists (unicode)
eq GCS_VERBICONW 0x00000014     // icon string (unicode)
eq GCS_UNICODE 0x00000004     // for bit testing - Unicode string
~

unicode
{
	eq GCS_VERB GCS_VERBW
	eq GCS_HELPTEXT GCS_HELPTEXTW
	eq GCS_VALIDATE GCS_VALIDATEW
elsedef
	eq GCS_VERB GCS_VERBA
	eq GCS_HELPTEXT GCS_HELPTEXTA
	eq GCS_VALIDATE GCS_VALIDATEA
}

eq CMDSTR_NEWFOLDERA b"NewFolder"
eq CMDSTR_VIEWLISTA b"ViewList"
eq CMDSTR_VIEWDETAILSA b"ViewDetails"
eq CMDSTR_NEWFOLDERW "NewFolder"
eq CMDSTR_VIEWLISTW "ViewList"
eq CMDSTR_VIEWDETAILSW "ViewDetails"
~

unicode
{
	eq CMDSTR_NEWFOLDER CMDSTR_NEWFOLDERW
	eq CMDSTR_VIEWLIST CMDSTR_VIEWLISTW
	eq CMDSTR_VIEWDETAILS CMDSTR_VIEWDETAILSW
elsedef
	eq CMDSTR_NEWFOLDER CMDSTR_NEWFOLDERA
	eq CMDSTR_VIEWLIST CMDSTR_VIEWLISTA
	eq CMDSTR_VIEWDETAILS CMDSTR_VIEWDETAILSA
}

eq CMIC_MASK_HOTKEY SEE_MASK_HOTKEY
eq CMIC_MASK_ICON SEE_MASK_ICON
eq CMIC_MASK_FLAG_NO_UI SEE_MASK_FLAG_NO_UI
eq CMIC_MASK_UNICODE SEE_MASK_UNICODE
eq CMIC_MASK_NO_CONSOLE SEE_MASK_NO_CONSOLE

/*
ifver_l @VISTA
{
	eq CMIC_MASK_HASLINKNAME SEE_MASK_HASLINKNAME
	eq CMIC_MASK_HASTITLE SEE_MASK_HASTITLE
}

eq CMIC_MASK_FLAG_SEP_VDM SEE_MASK_FLAG_SEPVDM
*/

eq CMIC_MASK_ASYNCOK SEE_MASK_ASYNCOK

ifver @VISTA
{
	eq CMIC_MASK_NOASYNC SEE_MASK_NOASYNC
}

eq CMIC_MASK_SHIFT_DOWN 0x10000000
eq CMIC_MASK_CONTROL_DOWN 0x40000000
eq CMIC_MASK_FLAG_LOG_USAGE SEE_MASK_FLAG_LOG_USAGE
eq CMIC_MASK_NOZONECHECKS SEE_MASK_NOZONECHECKS
eq CMIC_MASK_PTINVOKE 0x20000000
~

sd CMINVOKECOMMANDINFO
{
	sf IDword cbSize
	sf IDword fMask
	sf IHandle hwnd
	sf LPCSTR lpVerb
	sf LPCSTR lpParameters
	sf LPCSTR lpDirectory
	sf IInt nShow
	sf IDword dwHotKey
	sf IHandle hIcon
}

pie CMINVOKECOMMANDINFO LPCMINVOKECOMMANDINFO PCCMINVOKECOMMANDINFO

sd CMINVOKECOMMANDINFOEX
{
	sf IDword cbSize
	sf IDword fMask
	sf IHandle hwnd
	sf LPCSTR lpVerb
	sf LPCSTR lpParameters
	sf LPCSTR lpDirectory
	sf IInt nShow
	sf IDword dwHotKey
	sf IHandle hIcon
	sf LPCSTR lpTitle
	sf LPCWSTR lpVerbW
	sf LPCWSTR lpParametersW
	sf LPCWSTR lpDirectoryW
	sf LPCWSTR lpTitleW
	sf POINT ptInvoke
}

pie CMINVOKECOMMANDINFOEX LPCMINVOKECOMMANDINFOEX PCCMINVOKECOMMANDINFO

sd CMINVOKECOMMANDINFOEX_REMOTE
{
	sf IDword cbSize
	sf IDword fMask
	sf IHandle hwnd
	sf LPCSTR lpVerbString
	sf LPCSTR lpParameters
	sf LPCSTR lpDirectory
	sf IInt nShow
	sf IDword dwHotKey
	sf LPCSTR lpTitle
	sf LPCWSTR lpVerbWString
	sf LPCWSTR lpParametersW
	sf LPCWSTR lpDirectoryW
	sf LPCWSTR lpTitleW
	sf POINT ptInvoke
	sf IUInt lpVerbInt
	sf IUInt lpVerbWInt
}

IU IContextMenu
{
	iid 000214e4-0000-0000-c000-000000000046
	cf QueryContextMenu hmenu HMENU indexMenu UINT idCmdFirst UINT idCmdLast UINT uFlags UINT
	cf InvokeCommand pici P.CMINVOKECOMMANDINFO
	cf GetCommandString idCmd UINT_PTR uType UINT pReserved PUINT pszName LPSTR cchMax UINT
}

pi LPCONTEXTMENU

I IContextMenu2 ex IContextMenu
{
	iid 000214f4-0000-0000-c000-000000000046
	cf HandleMenuMsg uMsg UINT wParam WPARAM lParam LPARAM
}

pi LPCONTEXTMENU2

I IContextMenu3 ex IContextMenu2
{
	iid BCFCE0A0-EC17-11d0-8D10-00A0C90F2719
	cf HandleMenuMsg2 uMsg UINT wParam WPARAM lParam LPARAM plResult P.LRESULT
}

pi LPCONTEXTMENU3

IU IStaticVerbProvider
{
	iid 4B770DA6-D111-4015-96FD-8C1C56F06C55
	cf IsVerbSupported verbName LPCWSTR result PBOOL
}

IU IExecuteCommand
{
	iid 7F9185B0-CB92-43c5-80A9-92277A4F7B54
	cf SetKeyState grfKeyState DWORD
	cf SetParameters pszParameters LPCWSTR
	cf SetPosition pt POINT
	cf SetShowWindow nShow INT
	cf SetNoShowUI fNoShowUI BOOL
	cf SetDirectory pszDirectory LPCWSTR
	cf Execute
}

I IPersistFolder ex IPersist
{
	iid 000214ea-0000-0000-c000-000000000046
	cf Initialize pidl P.ITEMIDLIST_ABSOLUTE
}

pi LPPERSISTFOLDER

eq IRTIR_TASK_NOT_RUNNING 0
eq IRTIR_TASK_RUNNING 1
eq IRTIR_TASK_SUSPENDED 2
eq IRTIR_TASK_PENDING 3
eq IRTIR_TASK_FINISHED 4

IU IRunnableTask
{
	iid 85788d00-6807-11d0-b810-00c04fd706ec
	cf Run
	cf Kill bWait BOOL
	cf Suspend
	cf Resume
	vf IsRunning ULONG
}

eq TOID_NULL GUID_NULL
eq ITSAT_DEFAULT_LPARAM DWORD_PTR(-1).value
eq ITSAT_DEFAULT_PRIORITY 0x10000000
eq ITSAT_MAX_PRIORITY 0x7fffffff
eq ITSAT_MIN_PRIORITY 0x00000000
eq ITSSFLAG_COMPLETE_ON_DESTROY 0x0000 // wait for the current task to complete before deleting the scheduler
eq ITSSFLAG_KILL_ON_DESTROY 0x0001 // kill the current task (if there is one) when the task scheduler is deleted
eq ITSSFLAG_FLAGS_MASK 0x0003
eq ITSS_THREAD_DESTROY_DEFAULT_TIMEOUT (10*1000)       // default milliseconds until a sleeping worker thread is released
eq INFINITE 0xFFFFFFFF
eq ITSS_THREAD_TERMINATE_TIMEOUT (INFINITE)      // set sleeping worker threads to never be released
eq ITSS_THREAD_TIMEOUT_NO_CHANGE (INFINITE-1)  // no change to the thread timeout
~

IU IShellTaskScheduler
{
	iid 6CCB7BE0-6807-11d0-B810-00C04FD706EC
	cf AddTask prt P.IRunnableTask rtoid P.TASKOWNERID lParam DWORD_PTR dwPriority DWORD
	cf RemoveTasks rtoid P.TASKOWNERID lParam DWORD_PTR bWaitIfRunning BOOL
	cf CountTasks rtoid P.TASKOWNERID
	cf Status dwReleaseStatus DWORD dwThreadTimeout DWORD
}

I IPersistFolder2 ex IPersistFolder
{
	iid 1AC3D9F0-175C-11d1-95BE-00609797EA4F
	cf GetCurFolder ppidl P.P.ITEMIDLIST_ABSOLUTE
}

sd PERSIST_FOLDER_TARGET_INFO
{
	sf IPointer[ITEMIDLIST_ABSOLUTE] pidlTargetFolder
	sf IWideCharArrayFixedSize[260] szTargetParsingName
	sf IWideCharArrayFixedSize[260] szNetworkProvider
	sf IDword dwAttributes
	sf IInt csidl
}

I IPersistFolder3 ex IPersistFolder2
{
	iid CEF04FDF-FE72-11d2-87A5-00C04F6837CF
	cf InitializeEx pbc P.IBindCtx pidlRoot P.ITEMIDLIST_ABSOLUTE ppfti P.PERSIST_FOLDER_TARGET_INFO
	cf GetFolderTargetInfo ppfti P.PERSIST_FOLDER_TARGET_INFO
}

I IPersistIDList ex IPersist
{
	iid 1079acfc-29bd-11d3-8e0d-00c04f6837d5
	cf SetIDList pidl P.ITEMIDLIST_ABSOLUTE
	cf GetIDList ppidl P.P.ITEMIDLIST_ABSOLUTE
}

IU IEnumIDList
{
	iid 000214F2-0000-0000-C000-000000000046
	cf Next celt ULONG rgelt P.P.ITEMID_CHILD pceltFetched PULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppenum FD.P.P.IEnumIDList
}

pi LPENUMIDLIST

IU IEnumFullIDList
{
	iid d0191542-7954-4908-bc06-b2360bbe45ba
	cf Next celt ULONG rgelt P.P.ITEMIDLIST_ABSOLUTE pceltFetched PULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppenum FD.P.P.IEnumFullIDList
}

ed SHGDNF
{
	ee SHGDN_NORMAL 0
    ee SHGDN_INFOLDER 0x1
    ee SHGDN_FOREDITING 0x1000
    ee SHGDN_FORADDRESSBAR 0x4000
    ee SHGDN_FORPARSING 0x8000
}

ed SHCONTF
{
	ee SHCONTF_CHECKING_FOR_CHILDREN 0x10
	ee SHCONTF_FOLDERS 0x20
	ee SHCONTF_NONFOLDERS 0x40
	ee SHCONTF_INCLUDEHIDDEN 0x80
	ee SHCONTF_INIT_ON_FIRST_NEXT 0x100
	ee SHCONTF_NETPRINTERSRCH 0x200
	ee SHCONTF_SHAREABLE 0x400
	ee SHCONTF_STORAGE 0x800
	ee SHCONTF_NAVIGATION_ENUM 0x1000
	ee SHCONTF_FASTITEMS 0x2000
	ee SHCONTF_FLATLIST 0x4000
	ee SHCONTF_ENABLE_ASYNC 0x8000
	ee SHCONTF_INCLUDESUPERHIDDEN 0x10000
}

eq SHCIDS_ALLFIELDS 0x80000000
eq SHCIDS_CANONICALONLY 0x10000000
eq SHCIDS_BITMASK 0xFFFF0000
eq SHCIDS_COLUMNMASK 0x0000FFFF
eq SFGAO_CANCOPY DROPEFFECT_COPY // Objects can be copied    (0x1)
eq SFGAO_CANMOVE DROPEFFECT_MOVE // Objects can be moved     (0x2)
eq SFGAO_CANLINK DROPEFFECT_LINK // Objects can be linked    (0x4)
eq SFGAO_STORAGE 0x00000008     // supports BindToObject(IID_IStorage)
eq SFGAO_CANRENAME 0x00000010     // Objects can be renamed
eq SFGAO_CANDELETE 0x00000020     // Objects can be deleted
eq SFGAO_HASPROPSHEET 0x00000040     // Objects have property sheets
eq SFGAO_DROPTARGET 0x00000100     // Objects are drop target
eq SFGAO_CAPABILITYMASK 0x00000177
eq SFGAO_PLACEHOLDER 0x00000800     // File or folder is not fully present and recalled on open or access
eq SFGAO_SYSTEM 0x00001000     // System object
eq SFGAO_ENCRYPTED 0x00002000     // Object is encrypted (use alt color)
eq SFGAO_ISSLOW 0x00004000     // 'Slow' object
eq SFGAO_GHOSTED 0x00008000     // Ghosted icon
eq SFGAO_LINK 0x00010000     // Shortcut (link)
eq SFGAO_SHARE 0x00020000     // Shared
eq SFGAO_READONLY 0x00040000     // Read-only
eq SFGAO_HIDDEN 0x00080000     // Hidden object
eq SFGAO_DISPLAYATTRMASK 0x000FC000
eq SFGAO_FILESYSANCESTOR 0x10000000     // May contain children with SFGAO_FILESYSTEM
eq SFGAO_FOLDER 0x20000000     // Support BindToObject(IID_IShellFolder)
eq SFGAO_FILESYSTEM 0x40000000     // Is a win32 file system object (file/folder/root)
eq SFGAO_HASSUBFOLDER 0x80000000     // May contain children with SFGAO_FOLDER (may be slow)
eq SFGAO_CONTENTSMASK 0x80000000
eq SFGAO_VALIDATE 0x01000000     // Invalidate cached information (may be slow)
eq SFGAO_REMOVABLE 0x02000000     // Is this removeable media?
eq SFGAO_COMPRESSED 0x04000000     // Object is compressed (use alt color)
eq SFGAO_BROWSABLE 0x08000000     // Supports IShellFolder, but only implements CreateViewObject() (non-folder view)
eq SFGAO_NONENUMERATED 0x00100000     // Is a non-enumerated object (should be hidden)
eq SFGAO_NEWCONTENT 0x00200000     // Should show bold in explorer tree
eq SFGAO_CANMONIKER 0x00400000     // Obsolete
eq SFGAO_HASSTORAGE 0x00400000     // Obsolete
eq SFGAO_STREAM 0x00400000     // Supports BindToObject(IID_IStream)
eq SFGAO_STORAGEANCESTOR 0x00800000     // May contain children with SFGAO_STORAGE or SFGAO_STREAM
eq SFGAO_STORAGECAPMASK 0x70C50008     // For determining storage capabilities, ie for open/save semantics
eq SFGAO_PKEYSFGAOMASK 0x81044000     // Attributes that are masked out for PKEY_SFGAOFlags because they are considered to cause slow calculations or lack context (SFGAO_VALIDATE | SFGAO_ISSLOW | SFGAO_HASSUBFOLDER and others)
eq SFGAOF ULONG
~

ed SYNC_TRANSFER_STATUS
{
	ee STS_NONE
	ee STS_NEEDSUPLOAD 0x1
	ee STS_NEEDSDOWNLOAD 0x2
	ee STS_TRANSFERRING 0x4
	ee STS_PAUSED 0x8
	ee STS_HASERROR 0x10
	ee STS_FETCHING_METADATA 0x20
	ee STS_USER_REQUESTED_REFRESH 0x40
	ee STS_HASWARNING 0x80
	ee STS_EXCLUDED 0x100
	ee STS_INCOMPLETE 0x200
	ee STS_PLACEHOLDER_IFEMPTY 0x400
}

ed STORAGE_PROVIDER_FILE_FLAGS
{
	ee SPFF_NONE
	ee SPFF_DOWNLOAD_BY_DEFAULT
	ee SPFF_CREATED_ON_THIS_DEVICE
}

ed PLACEHOLDER_STATES
{
	ee PS_NONE
	ee PS_MARKED_FOR_OFFLINE_AVAILABILITY 0x1
	ee PS_FULL_PRIMARY_STREAM_AVAILABLE 0x2
	ee PS_CREATE_FILE_ACCESSIBLE 0x4
	ee PS_CLOUDFILE_PLACEHOLDER 0x8
	eef PS_DEFAULT ((PS_MARKED_FOR_OFFLINE_AVAILABILITY|PS_FULL_PRIMARY_STREAM_AVAILABLE)|PS_CREATE_FILE_ACCESSIBLE)
	eef PS_ALL (((PS_MARKED_FOR_OFFLINE_AVAILABILITY|PS_FULL_PRIMARY_STREAM_AVAILABLE)|PS_CREATE_FILE_ACCESSIBLE)|PS_CLOUDFILE_PLACEHOLDER)
}

ed MERGE_UPDATE_STATUS
{
	ee MUS_COMPLETE
	ee MUS_USERINPUTNEEDED
	ee MUS_FAILED
}

IU IFileSyncMergeHandler
{
	iid d97b5aac-c792-433c-975d-35c4eadc7a9d
	cf Merge localFilePath LPCWSTR serverFilePath LPCWSTR updateStatus P.MERGE_UPDATE_STATUS
	cf ShowResolveConflictUIAsync localFilePath LPCWSTR monitorToDisplayOn HMONITOR
}

eq STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE "Force Folder Shortcut Resolve"
eq STR_AVOID_DRIVE_RESTRICTION_POLICY "Avoid Drive Restriction Policy"
eq STR_AVOID_DRIVE_RESTRICTION_POLICY "Avoid Drive Restriction Policy"
eq STR_SKIP_BINDING_CLSID "Skip Binding CLSID"
eq STR_PARSE_PREFER_FOLDER_BROWSING "Parse Prefer Folder Browsing"
eq STR_DONT_PARSE_RELATIVE "Don't Parse Relative"
eq STR_PARSE_TRANSLATE_ALIASES "Parse Translate Aliases"
eq STR_PARSE_SKIP_NET_CACHE "Skip Net Resource Cache"
eq STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS "Parse Shell Protocol To File Objects"
~

ifver_ie @IE70
{
	eq STR_TRACK_CLSID "Track the CLSID"
	eq STR_INTERNAL_NAVIGATE "Internal Navigation"
	eq STR_PARSE_PROPERTYSTORE "DelegateNamedProperties"
	eq STR_NO_VALIDATE_FILENAME_CHARS "NoValidateFilenameChars"
	eq STR_BIND_DELEGATE_CREATE_OBJECT "Delegate Object Creation"
	eq STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS "Allow binding to Internet shell folder handlers and negate STR_PARSE_PREFER_WEB_BROWSING"
	eq STR_PARSE_PREFER_WEB_BROWSING "Do not bind to Internet shell folder handlers"
	eq STR_PARSE_SHOW_NET_DIAGNOSTICS_UI "Show network diagnostics UI"
	eq STR_PARSE_DONT_REQUIRE_VALIDATED_URLS "Do not require validated URLs"
	eq STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE "Validate UR"
}

ifver @WIN8
{
	eq BIND_INTERRUPTABLE 0xFFFFFFFF
}

ifver @WIN7
{
	eq STR_BIND_FOLDERS_READ_ONLY "Folders As Read Only"
	eq STR_BIND_FOLDER_ENUM_MODE "Folder Enum Mode"
~

	ed FOLDER_ENUM_MODE
	{
		ee FEM_VIEWRESULT
		ee FEM_NAVIGATION
	}
	
	IU IObjectWithFolderEnumMode
	{
		iid 6a9d9026-0e6e-464c-b000-42ecc07de673
		cf SetMode feMode FOLDER_ENUM_MODE
		cf GetMode pfeMode P.FOLDER_ENUM_MODE
	}
	
	eq STR_PARSE_WITH_EXPLICIT_PROGID "ExplicitProgid"
	eq STR_PARSE_WITH_EXPLICIT_ASSOCAPP "ExplicitAssociationApp"
	eq STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL "ExplicitAssociationSuccessfu"
	eq STR_PARSE_AND_CREATE_ITEM "ParseAndCreateItem"
	eq STR_PROPERTYBAG_PARAM "SHBindCtxPropertyBag"
	eq STR_ENUM_ITEMS_FLAGS "SHCONTF"
	eq STR_STORAGEITEM_CREATION_FLAGS "SHGETSTORAGEITEM"
~
	
	IU IParseAndCreateItem
	{
		iid 67efed0e-e827-4408-b493-78f3982b685c
		cf SetItem psi FD.P.IShellItem
		cf GetItem riid R.IID ppv P.PVOID
	}
	
	eq STR_ITEM_CACHE_CONTEXT "ItemCacheContext"
}

IU IShellFolder
{
	iid 000214E6-0000-0000-C000-000000000046
	cf ParseDisplayName hwnd HWND pbc P.IBindCtx pszDisplayName LPWSTR pchEaten PULONG ppidl P.P.ITEMIDLIST_RELATIVE pdwAttributes PULONG
	cf EnumObjects hwnd HWND grfFlags SHCONTF ppenumIDList P.P.IEnumIDList
	cf BindToObject pidl P.ITEMIDLIST_RELATIVE pbc P.IBindCtx riid R.IID ppv P.PVOID
	cf BindToStorage pidl P.ITEMIDLIST_RELATIVE pbc P.IBindCtx riid R.IID ppv P.PVOID
	cf CompareIDs lParam LPARAM pidl1 P.ITEMIDLIST_RELATIVE pidl2 P.ITEMIDLIST_RELATIVE
	cf CreateViewObject hwndOwner HWND riid R.IID ppv P.PVOID
	cf GetAttributesOf cidl UINT apidl P.P.ITEMID_CHILD rgfInOut P.SFGAOF
	cf GetUIObjectOf hwndOwner HWND cidl UINT apidl P.P.ITEMID_CHILD riid R.IID rgfReserved PUINT ppv P.PVOID
	cf GetDisplayNameOf pidl P.ITEMID_CHILD uFlags SHGDNF pName P.STRRET
	cf SetNameOf hwnd HWND pidl P.ITEMID_CHILD pszName LPCWSTR uFlags SHGDNF ppidlOut P.P.ITEMID_CHILD
}

pi LPSHELLFOLDER

sd EXTRASEARCH
{
	sf GUID guidSearch
	sf IWideCharArrayFixedSize[80] wszFriendlyName
	sf IWideCharArrayFixedSize[2084] wszUrl
}

pie EXTRASEARCH LPEXTRASEARCH

IU IEnumExtraSearch
{
	iid 0E700BE1-9DB6-11d1-A1CE-00C04FD75D13
	cf Next celt ULONG rgelt P.EXTRASEARCH pceltFetched PULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppenum FD.P.P.IEnumExtraSearch
}

pie IEnumExtraSearch LPENUMEXTRASEARCH

I IShellFolder2 ex IShellFolder
{
	iid 93F2F68C-1D1B-11d3-A30E-00C04F79ABD1
	cf GetDefaultSearchGUID pguid P.GUID
	cf EnumSearches ppenum P.P.IEnumExtraSearch
	cf GetDefaultColumn dwRes DWORD pSort PULONG pDisplay PULONG
	cf GetDefaultColumnState iColumn UINT pcsFlags P.SHCOLSTATEF
	cf GetDetailsEx pidl P.ITEMID_CHILD pscid P.SHCOLUMNID pv P.VARIANT
	cf GetDetailsOf pidl P.ITEMID_CHILD iColumn UINT psd P.SHELLDETAILS
	cf MapColumnToSCID iColumn UINT pscid P.SHCOLUMNID
}

// to be continued
// uncompleted