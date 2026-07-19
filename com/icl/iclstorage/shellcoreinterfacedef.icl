.icl
.ver 100

//
// Interface Contract Language description of ShObjIdl_core
//

.gencomment

//
// shellcoreinterfacedef.icl
//
// ICL of ShObjIdl_core.h
//

imports
{
	// local imports
	import .ctlinterfacedef
	import .objectarray
	
	// win imports
	import ..shtypes
	import ..shellapi
	import ..commctrl
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
	pie PROPVARIANT LPPROPVARIANT PPROPVARIANT
	pie PROPERTYKEY LPPROPERTYKEY PPROPERTYKEY
	pie OLEMENUGROUPWIDTHS LPOLEMENUGROUPWIDTHS
	pie IServiceProvider LPSERVICEPROVIDER
	pie IStream LPSTREAM
	pie IDataObject LPDATAOBJECT
	pie FILETIME LPFILETIME
	pie LOGFONTW LPLOGFONTW
	pie MSG PMSG
	pie RECT PRECT
	pie TBBUTTON LPTBBUTTON
}

// [Generator-Only] Alias to generator type map
al int UINT_PTR LPARAM WPARAM DWORD_PTR SHCOLSTATEF COLORREF HMENU HWND HOLEMENU HKEY HANDLE HICON HACCEL HIMAGELIST

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

ed FOLDERFLAGS
{
    // XP flags
    ee FWF_NONE 0x00000000
    ee FWF_AUTOARRANGE 0x00000001
    ee FWF_ABBREVIATEDNAMES 0x00000002     // not supported
    ee FWF_SNAPTOGRID 0x00000004
    ee FWF_OWNERDATA 0x00000008     // not supported
    ee FWF_BESTFITWINDOW 0x00000010
    ee FWF_DESKTOP 0x00000020     // implies NOCLIENTEDGE/NOSCROLL
    ee FWF_SINGLESEL 0x00000040
    ee FWF_NOSUBFOLDERS 0x00000080
    ee FWF_TRANSPARENT 0x00000100
    ee FWF_NOCLIENTEDGE 0x00000200     // not supported this is always assumed to be true
    ee FWF_NOSCROLL 0x00000400
    ee FWF_ALIGNLEFT 0x00000800
    ee FWF_NOICONS 0x00001000
    ee FWF_SHOWSELALWAYS 0x00002000
    ee FWF_NOVISIBLE 0x00004000
    ee FWF_SINGLECLICKACTIVATE 0x00008000     // not supported
    ee FWF_NOWEBVIEW 0x00010000     // not supported
    ee FWF_HIDEFILENAMES 0x00020000
    ee FWF_CHECKSELECT 0x00040000     // check boxes with 2 modes { unchecked SVSI_CHECK }

    // Vista Flags
    ee FWF_NOENUMREFRESH 0x00080000
    ee FWF_NOGROUPING 0x00100000
    ee FWF_FULLROWSELECT 0x00200000
    ee FWF_NOFILTERS 0x00400000
    ee FWF_NOCOLUMNHEADER 0x00800000     // don't show column header
    ee FWF_NOHEADERINALLVIEWS 0x01000000     // don't show column header if not in details mode
    ee FWF_EXTENDEDTILES 0x02000000
    ee FWF_TRICHECKSELECT 0x04000000     // checks boxes have 3 modes { unchecked, SVSI_CHECK SVSI_CHECK2 }
    ee FWF_AUTOCHECKSELECT 0x08000000     // check boxes to change item selection state
    ee FWF_NOBROWSERVIEWSTATE 0x10000000
    ee FWF_SUBSETGROUPS 0x20000000
    ee FWF_USESEARCHFOLDER 0x40000000     // Use the search folder for stacking and searching
    ee FWF_ALLOWRTLREADING 0x80000000     // Do not use WS_EX_RTLREADING when WS_EX_LAYOUTRTL is set (thereby keeping RTL reading)
}

ed FOLDERVIEWMODE
{
    ee FVM_AUTO -1
    ee FVM_FIRST 1
    ee FVM_ICON 1
    ee FVM_SMALLICON 2
    ee FVM_LIST 3
    ee FVM_DETAILS 4
    ee FVM_THUMBNAIL 5
    ee FVM_TILE 6
    ee FVM_THUMBSTRIP 7
    ee FVM_CONTENT 8
    ee FVM_LAST 8
}

ed FOLDERLOGICALVIEWMODE
{
    ee FLVM_UNSPECIFIED -1
    ee FLVM_FIRST 1
    ee FLVM_DETAILS 1
    ee FLVM_TILES 2
    ee FLVM_ICONS 3
    ee FLVM_LIST 4
    ee FLVM_CONTENT 5
    ee FLVM_LAST 5
}

sd FOLDERSETTINGS
{
	sf IInteger[FOLDERVIEWMODE] ViewMode // View Mode
	sf IInteger[FOLDERLOGICALVIEWMODE] fFlags // View options
}

pie FOLDERSETTINGS LPFOLDERSETTINGS LPCFOLDERSETTINGS PFOLDERSETTINGS

ed SVSIF
{
    ee SVSI_DESELECT 0x00000000
    ee SVSI_SELECT 0x00000001
    ee SVSI_EDIT 0x00000003  // includes SVSI_SELECT
    ee SVSI_DESELECTOTHERS 0x00000004
    ee SVSI_ENSUREVISIBLE 0x00000008
    ee SVSI_FOCUSED 0x00000010
    ee SVSI_TRANSLATEPT 0x00000020
    ee SVSI_SELECTIONMARK 0x00000040
    ee SVSI_POSITIONITEM 0x00000080
    ee SVSI_CHECK 0x00000100
    ee SVSI_CHECK2 0x00000200
    ee SVSI_KEYBOARDSELECT 0x00000401  // includes SVSI_SELECT
    ee SVSI_NOTAKEFOCUS 0x40000000
}

eq SVSI_NOSTATECHANGE 0x80000000 // work around the use of the high bit that results in 4245: signed/unsigned mismatch")
~

ed SVGIO
{
    ee SVGIO_BACKGROUND 0x00000000     // riid =IID_IDispatch -> view automation object, implements supports connection point container for DIID_DShellFolderViewEvents
                                       // riid =IID_IContextMenu -> backgroud context menu object
                                       // riid =IID_IPersistHistory -> persist history object for the view
    ee SVGIO_SELECTION 0x00000001      // the selected items in the view
    ee SVGIO_ALLVIEW 0x00000002        // all of the items in the view
    ee SVGIO_CHECKED 0x00000003        // if the view is in check select mode the checked items
    ee SVGIO_TYPE_MASK 0x0000000F      // mask for above values
    ee SVGIO_FLAG_VIEWORDER 0x80000000 // request items in view order
}

ed SVUIA_STATUS
{
    ee SVUIA_DEACTIVATE 0
    ee SVUIA_ACTIVATE_NOFOCUS 1
    ee SVUIA_ACTIVATE_FOCUS 2
    ee SVUIA_INPLACEACTIVATE 3          // new flag for IShellView2
}

// [Generator-Only]
al FARPROC LPFNSVADDPROPSHEETPAGE

I IShellView ex IOleWindow
{
	iid 000214E3-0000-0000-C000-000000000046
	cf TranslateAccelerator pmsg P.MSG
	cf EnableModeless fEnable BOOL
	cf UIActivate uState SVUIA_STATUS
	cf Refresh
	cf CreateViewWindow psvPrevious FD.P.IShellView pfs P.FOLDERSETTINGS psb FD.P.IShellBrowser prc P.RECT phWnd P.HWND
	cf DestroyViewWindow
	cf GetCurrentInfo pfs P.FOLDERSETTINGS
	cf AddPropertySheetPages dwReserved DWORD pfn LPFNSVADDPROPSHEETPAGE lparam LPARAM
	cf SaveViewState
	cf SelectItem pidlItem P.ITEMID_CHILD uFlags SVSIF
	cf GetItemObject uItem SVGIO riid R.IID ppv P.PVOID
}

pi LPSHELLVIEW

eq SV2GV_CURRENTVIEW UINT(-1).value
eq SV2GV_DEFAULTVIEW UINT(-2).value
~

eq SHELLVIEWID GUID
~

sd SV2CVW2_PARAMS
{
	sf IDword cbSize
	sf IPointer[IShellView] psvPrev
	sf IPointer[FOLDERSETTINGS] pfs
	sf IPointer['IShellBrowser'] psbOwner
	sf IPointer[RECT] prcView
	sf IPointer[SHELLVIEWID] pvid
	sf IHandle hwndView
}

pie SV2CVW2_PARAMS LPSV2CVW2_PARAMS

I IShellView2 ex IShellView
{
	iid 88E39E80-3578-11CF-AE69-08002B2E1262
	cf GetView pvid P.SHELLVIEWID uView ULONG
	cf CreateViewWindow2 lpParams P.SV2CVW2_PARAMS
	cf HandleRename pidlNew P.ITEMID_CHILD
	cf SelectAndPositionItem pidlItem P.ITEMID_CHILD uFlags SVSIF ppt P.POINT
}

pi LPSHELLVIEW2

IU IFolderView
{
	iid cde725b0-ccc9-4519-917e-325d72fab4ce
	cf GetCurrentViewMode pViewMode P.FOLDERVIEWMODE
	cf SetCurrentViewMode ViewMode FOLDERVIEWMODE
	cf GetFolder riid R.IID ppv P.PVOID
	cf Item iItemIndex INT ppidl P.ITEMID_CHILD
	cf ItemCount uFlags SVGIO pcItems P.INT
	cf Items uFlags SVGIO riid R.IID ppv P.PVOID
	cf GetSelectionMarkedItem piItem P.INT
	cf GetFocusedItem piItem P.INT
	cf GetItemPosition pidl P.ITEMID_CHILD ppt P.POINT
	cf GetSpacing ppt P.POINT
	cf GetDefaultSpacing ppt P.POINT
	cf GetAutoArrange
	cf SelectItem iItem INT dwFlags SVSIF
	cf SelectAndPositionItems cidl UINT apidl P.P.ITEMID_CHILD apt P.POINT dwFlags SVSIF
}

eq SID_SFolderView IFolderView._iid_
~

ifver @VISTA
{
	ed SORTDIRECTION
	{
		ee SORT_DESCENDING -1
		ee SORT_ASCENDING 1
	}
	
	sd SORTCOLUMN
	{
		sf PROPERTYKEY propkey
		sf IInteger[SORTDIRECTION] direction
	}
	
	ed FVTEXTTYPE
	{
		ee FVST_EMPTYTEXT 0
	}
	
	eq DEPRECATED_HRESULT HRESULT
~
	
	I IFolderView2 ex IFolderView
	{
		iid 1af3a467-214f-4298-908e-06b03e0b39f9
		cf SetGroupBy key R.PROPERTYKEY fAscending BOOL
		cf GetGroupBy pkey P.PROPERTYKEY pfAscending P.BOOL
		cf SetViewProperty pidl P.ITEMID_CHILD propkey R.PROPERTYKEY propvar P.PROPVARIANT
		cf GetViewProperty pidl P.ITEMID_CHILD propkey R.PROPERTYKEY ppropvar P.PROPVARIANT
		cf SetTileViewProperties pidl P.ITEMID_CHILD pszPropList LPCWSTR
		cf SetExtendedTileViewProperties pidl P.ITEMID_CHILD pszPropList LPCWSTR
		cf SetText iType FVTEXTTYPE pwszText LPCWSTR
		cf SetCurrentFolderFlags dwMask DWORD dwFlags DWORD
		cf GetCurrentFolderFlags pdwFlags P.FOLDERFLAGS
		cf GetSortColumnCount pcColumns P.INT
		cf GetSortColumns rgSortColumns P.SORTCOLUMN cColumns INT
		cf GetItem iItem INT riid R.IID ppv P.PVOID
		cf GetVisibleItem iStart INT fPrevious BOOL piItem P.INT
		cf GetSelectedItem iStart INT piItem P.INT
		cf GetSelection fNoneImpliesFolder BOOL ppsia FD.P.P.IShellItemArray
		cf GetSelectionState pidl P.ITEMID_CHILD pdwFlags P.SVSIF
		cf InvokeVerbOnSelection pszVerb LPCSTR
		cf SetViewModeAndIconSize uViewMode FOLDERVIEWMODE iImageSize INT
		cf GetViewModeAndIconSize puViewMode P.FOLDERVIEWMODE piImageSize P.INT
		cf SetGroupSubsetCount cVisibleRows UINT
		cf GetGroupSubsetCount pcVisibleRows P.UINT
		cf SetRedraw fRedrawOn BOOL
		cf IsMoveInSameFolder
		cf DoRename
	}
	
	IU IFolderViewSettings
	{
		iid ae8c987d-8797-4ed3-be72-2a47dd938db0
		cf GetColumnPropertyList riid R.IID ppv P.PVOID
		cf GetGroupByProperty pkey P.PROPERTYKEY pfGroupAscending P.BOOL
		cf GetViewMode plvm P.FOLDERLOGICALVIEWMODE
		cf GetIconSize puIconSize P.UINT
		cf GetFolderFlags pfolderMask P.FOLDERFLAGS pfolderFlags P.FOLDERFLAGS
		cf GetSortColumns rgSortColumns P.SORTCOLUMN cColumnsIn UINT pcColumnsOut P.UINT
		cf GetGroupSubsetCount pcVisibleRows P.UINT
	}
	
	IU IInitializeNetworkFolder
	{
		iid 6e0f9881-42a8-4f2a-97f8-8af4e026d92d
		cf Initialize pidl P.ITEMID_CHILD pidlTarget P.ITEMID_CHILD uDisplayType UINT pszResName LPCWSTR pszProvider LPCWSTR
	}
	
	IU INetworkFolderInternal
	{
		iid CEB38218-C971-47BB-A703-F0BC99CCDB81
		cf GetResourceDisplayType displayType P.UINT
		cf GetIDList idList P.ITEMID_CHILD
		cf GetProvider itemIdCount UINT itemIds P.P.ITEMID_CHILD providerMaxLength UINT provider LPWSTR
	}
}

ifver_ie @IE70
{
	IU IPreviewHandlerVisuals
	{
		iid 196bf9a5-b346-4ef0-aa1e-5dcdb76768b1
		cf SetBackgroundColor color COLORREF
		cf SetFont plf P.LOGFONTW
		cf SetColor color COLORREF
	}
}

eq CDBOSC_SETFOCUS 0x00000000
eq CDBOSC_KILLFOCUS 0x00000001
eq CDBOSC_SELCHANGE 0x00000002
eq CDBOSC_RENAME 0x00000003
eq CDBOSC_STATECHANGE 0x00000004
~

IU ICommDlgBrowser
{
	iid 000214F1-0000-0000-C000-000000000046
	cf OnDefaultCommand ppshv P.IShellView
	cf OnStateChange ppshv P.IShellView uChange ULONG
	cf IncludeObject ppshv P.IShellView pidl P.ITEMID_CHILD
}

pi LPCOMMDLGBROWSER

eq SID_SExplorerBrowserFrame ICommDlgBrowser._iid_

ifver @WIN2K
{
	eq CDB2N_CONTEXTMENU_DONE 0x00000001
	eq CDB2N_CONTEXTMENU_START 0x00000002
~
	eq CDB2GVF_SHOWALLFILES 0x00000001
	ifver @VISTA
	{
		eq CDB2GVF_ISFILESAVE 0x00000002 // is file save, else file open
		eq CDB2GVF_ALLOWPREVIEWPANE 0x00000004
		eq CDB2GVF_NOSELECTVERB 0x00000008
		eq CDB2GVF_NOINCLUDEITEM 0x00000010
		eq CDB2GVF_ISFOLDERPICKER 0x00000020
		eq CDB2GVF_ADDSHIELD 0x00000040   // when CDB2GVF_NOSELECTVERB is not specified this flag controls the display of a LUA shield on the Select menu item
	}
~
	
	I ICommDlgBrowser2 ex ICommDlgBrowser
	{
		iid 0339516-2894-11d2-9039-00C04F8EEB3E
		cf Notify ppshv P.IShellView dwNotifyType DWORD
		cf GetDefaultMenuText ppshv P.IShellView pszText LPWSTR cchMax INT
		cf GetViewFlags pdwFlags P.DWORD
	}
	
	pi LPCOMMDLGBROWSER2
}

ifver_ie @IE70
{
	ed CM_MASK
	{
		ee CM_MASK_WIDTH 0x00000001
		ee CM_MASK_DEFAULTWIDTH 0x00000002
		ee CM_MASK_IDEALWIDTH 0x00000004
		ee CM_MASK_NAME 0x00000008
		ee CM_MASK_STATE 0x00000010
	}
	
	ed CM_STATE
	{
	    ee CM_STATE_NONE 0x00000000
		ee CM_STATE_VISIBLE 0x00000001  // The column is visible
		ee CM_STATE_FIXEDWIDTH 0x00000002  // Can't resize the column
		ee CM_STATE_NOSORTBYFOLDERNESS 0x00000004  // Do not sort folders seperately
		ee CM_STATE_ALWAYSVISIBLE 0x00000008  // readonly. column cannot be hidden
	}
	
	ed CM_ENUM_FLAGS
	{
	    ee CM_ENUM_ALL 0x00000001
		ee CM_ENUM_VISIBLE 0x00000002
	}
	
	ed CM_SET_WIDTH_VALUE
	{
		ee CM_WIDTH_USEDEFAULT -1
		ee CM_WIDTH_AUTOSIZE -2
	}
	
	eq MAX_COLUMN_NAME_LEN 80
~
	
	sd CM_COLUMNINFO
	{
		sf IDword cbSize
		sf IDword dwMask
		sf IDword dwState
		sf IUint uWidth
		sf IUint uDefaultWidth
		sf IUint uIdealWidth
		sf IWideCharArrayFixedSize[80] wszName
	}
	
	IU IColumnManager
	{
		iid d8ec27bb-3f3b-4042-b10a-4acfd924d453
		cf SetColumnInfo propkey R.PROPERTYKEY pcmci P.CM_COLUMNINFO
		cf GetColumnInfo propkey R.PROPERTYKEY pcmci P.CM_COLUMNINFO
		cf GetColumnCount dwFlags CM_ENUM_FLAGS puCount P.UINT
		cf GetColumns dwFlags CM_ENUM_FLAGS rgkeyOrder P.PROPERTYKEY cColumns UINT
		cf SetColumns rgkeyOrder P.PROPERTYKEY cVisible UINT
	}
}

IU IFolderFilterSite
{
	iid C0A651F5-B48B-11d2-B5ED-006097C686F6
	cf SetFilter punk P.IUnknown
}

IU IFolderFilter
{
	iid 9CC22886-DC8E-11d2-B1D0-00C04F8EEB3E
	cf ShouldShow psf P.IShellFolder pidlFolder P.ITEMID_CHILD pidlItem P.ITEMID_CHILD
	cf GetEnumFlags psf P.IShellFolder pidlFolder P.ITEMID_CHILD phwnd P.HWND
}

IU IInputObjectSite
{
	iid F1DB8392-7331-11D0-8C99-00A0C92DBFE8
	cf OnFocusChangeIS punkObj P.IUnknown fSetFocus BOOL
}

IU IInputObject
{
	iid 68284fAA-6A48-11D0-8c78-00C04fd918b4
	cf UIActivateIO fActivate BOOL pMsg P.MSG
	cf HasFocusIO
	cf TranslateAcceleratorIO pMsg P.MSG
}

I IInputObject2 ex IInputObject
{
	iid 6915C085-510B-44cd-94AF-28DFA56CF92B
	cf TranslateAcceleratorGlobal pMsg P.MSG
}

IU IShellIcon
{
	iid 000214E5-0000-0000-C000-000000000046
	cf GetIconOf pidl P.ITEMID_CHILD flags UINT pIconIndex P.INT
}

//
// flag values to be combined for the Flags parameter of IShellBrowser::BrowseObject() method
//
eq SBSP_DEFBROWSER 0x0000
eq SBSP_SAMEBROWSER 0x0001
eq SBSP_NEWBROWSER 0x0002

eq SBSP_DEFMODE 0x0000
eq SBSP_OPENMODE 0x0010
eq SBSP_EXPLOREMODE 0x0020
eq SBSP_HELPMODE 0x0040
eq SBSP_NOTRANSFERHIST 0x0080

eq SBSP_ABSOLUTE 0x0000
eq SBSP_RELATIVE 0x1000
eq SBSP_PARENT 0x2000
eq SBSP_NAVIGATEBACK 0x4000
eq SBSP_NAVIGATEFORWARD 0x8000

eq SBSP_ALLOW_AUTONAVIGATE 0x00010000

ifver @VISTA
{
	eq SBSP_KEEPSAMETEMPLATE 0x00020000
	eq SBSP_KEEPWORDWHEELTEXT 0x00040000
	eq SBSP_ACTIVATE_NOFOCUS 0x00080000
	eq SBSP_CREATENOHISTORY 0x00100000
	eq SBSP_PLAYNOSOUND 0x00200000
}

ifver_ie @IE60SP2
{
	eq SBSP_CALLERUNTRUSTED 0x00800000
	eq SBSP_TRUSTFIRSTDOWNLOAD 0x01000000
	eq SBSP_UNTRUSTEDFORDOWNLOAD 0x02000000
}
eq SBSP_NOAUTOSELECT 0x04000000
eq SBSP_WRITENOHISTORY 0x08000000
ifver_ie @IE60SP2
{
	eq SBSP_TRUSTEDFORACTIVEX 0x10000000
}
ifver_ie @IE70
{
	eq SBSP_FEEDNAVIGATION 0x20000000
}

eq SBSP_REDIRECT 0x40000000
eq SBSP_INITIATEDBYHLINKFRAME 0x80000000
~

//
// Values for id parameter of ISB::GetWindow/SendControlMsg members.
//
// WARNING:
//  Any shell extensions which sends messages to those control windows
// might not work in the future version of windows. If you really need
// to send messages to them, (1) don't assume that those control window
// always exist (i.e. GetControlWindow may fail) and (2) verify the window
// class of the window before sending any messages.
//

eq FCW_STATUS 0x0001
eq FCW_TOOLBAR 0x0002
eq FCW_TREE 0x0003
eq FCW_INTERNETBAR 0x0006
eq FCW_PROGRESS 0x0008
~

//
// Values for uFlags paremeter of ISB::SetToolbarItems member.
//
eq FCT_MERGE 0x0001
eq FCT_CONFIGABLE 0x0002
eq FCT_ADDTOEND 0x0004
~

eq LPTBBUTTONSB LPTBBUTTON
~

I IShellBrowser ex IOleWindow
{
	iid 000214E2-0000-0000-C000-000000000046
	cf InsertMenusSB hmenuShared HMENU lpMenuWidths P.OLEMENUGROUPWIDTHS
	cf SetMenuSB hmenuShared HMENU holemenuRes HOLEMENU hwndActiveObject HWND
	cf RemoveMenusSB hmenuShared HMENU
	cf SetStatusTextSB pszStatusText LPCWSTR
	cf EnableModelessSB fEnable BOOL
	cf TranslateAcceleratorSB pmsg P.MSG wID WORD
	cf BrowseObject pidl P.ITEMID_CHILD wFlags UINT
	cf GetViewStateStream grfMode DWORD ppStrm P.P.IStream
	cf GetControlWindow id UINT phwnd P.HWND
	cf SendControlMsg id UINT uMsg UINT wParam WPARAM lParam LPARAM pret P.LRESULT
	cf QueryActiveShellView ppshv P.P.IShellView
	cf SetToolbarItems lpButtons P.TBBUTTON nButtons UINT uFlags UINT
}

pi LPSHELLBROWSER

IU IProfferService
{
	iid cb728b20-f786-11ce-92ad-00aa00a74cd0
	cf ProfferService guidService R.GUID psp P.IServiceProvider pdwCookie P.DWORD
	cf RevokeService dwCookie DWORD
}

eq SID_SProfferService IProfferService._iid_
~

// Tells an IShellItem not to resolve the link target obtained
// when using the BHID_LinkTargetItem GUID in BindToHandler.
eq STR_DONT_RESOLVE_LINK "Don't Resolve Link"

// The handler is being retrieved on the UI thread.  Avoid any expensive work that touches the disk, network, etc.
eq STR_GET_ASYNC_HANDLER "GetAsyncHandler"
~

// New for XP, but used by downlevel code
//#if (NTDDI_VERSION >NTDDI_WINXP)

//  BindHandler GUIDs for IShellItem::BindToHandler (defined in shlguid.h)")
//  BHID_SFObject            restricts usage to IShellFolder::BindToObject()")
//  BHID_SFUIObject          restricts usage to IShellFolder::GetUIObjectOf()")
//  BHID_SFViewObject        restricts usage to IShellFolder::CreateViewObject()")
//  BHID_LinkTargetItem      CLSID_ShellItem initialized with the target this item (SFGAO_LINK only)")
//  BHID_Storage             attempts to get the stg/stm riid from BTO, but defaults to shell implementations on failure")

ed SIGDN
{
	ee SIGDN_NORMALDISPLAY 0x00000000       // SHGDN_NORMAL
	ee SIGDN_PARENTRELATIVEPARSING 0x80018001 // SHGDN_INFOLDER | SHGDN_FORPARSING
	ee SIGDN_DESKTOPABSOLUTEPARSING 0x80028000 // SHGDN_FORPARSING
	ee SIGDN_PARENTRELATIVEEDITING 0x80031001 // SHGDN_INFOLDER | SHGDN_FOREDITING
	ee SIGDN_DESKTOPABSOLUTEEDITING 0x8004c000 // SHGDN_FORPARSING | SHGDN_FORADDRESSBAR
	ee SIGDN_FILESYSPATH 0x80058000 // SHGDN_FORPARSING
	ee SIGDN_URL 0x80068000 // SHGDN_FORPARSING
	ee SIGDN_PARENTRELATIVEFORADDRESSBAR 0x8007c001 // SHGDN_INFOLDER | SHGDN_FORPARSING | SHGDN_FORADDRESSBAR
	ee SIGDN_PARENTRELATIVE 0x80080001 // SHGDN_INFOLDER
	ee SIGDN_PARENTRELATIVEFORUI 0x80094001 // SHGDN_INFOLDER | SHGDN_FORADDRESSBAR
}

//  SICHINT_DISPLAY         iOrder based on display in a folder view
//  SICHINT_ALLFIELDS       exact instance compare
//  SICHINT_CANONICAL       iOrder based on canonical name (better performance)

ed SICHINTF
{
	ee SICHINT_DISPLAY 0x00000000
	ee SICHINT_ALLFIELDS 0x80000000
	ee SICHINT_CANONICAL 0x10000000
	ee SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL 0x20000000
}

IU IShellItem
{
	iid 43826d1e-e718-42ee-bc55-a1e261c37bfe
	cf BindToHandler pbc P.IBindCtx bhid R.GUID riid R.IID ppv P.PVOID
	cf GetParent ppsi FD.P.P.IShellItem
	cf GetDisplayName sigdnName SIGDN ppszName P.LPWSTR
	cf GetAttributes sfgaoMask SFGAOF psfgaoAttribs P.SFGAOF
	cf Compare psi FD.P.IShellItem hint SICHINTF piOrder P.INT
}

ff shell32.SHSimpleIDListFromPath P.ITEMID_CHILD pszPath PCWSTR

ifver_ie @IE70
{
	// CLSID_ShellItem create and init helper APIs. produce IShellItem derived interfaces from these different expressions of an item
	ff shell32.SHCreateItemFromIDList HRESULT pidl P.ITEMID_CHILD riid R.IID ppv P.PVOID
	ff shell32.SHCreateItemFromParsingName HRESULT pszPath PCWSTR pbc P.IBindCtx riid R.IID ppv P.PVOID
	ff shell32.SHCreateItemWithParent HRESULT pidlParent P.ITEMID_CHILD psfParent P.IShellFolder pidl P.ITEMID_CHILD riid R.IID ppvItem P.PVOID
	ff shell32.SHCreateItemFromRelativeName HRESULT psiParent P.IShellItem pszName PCWSTR pbz P.IBindCtx riid R.IID ppv P.PVOID
}

ifver @VISTA
{
	ff shell32.SHCreateItemInKnownFolder HRESULT kfid R.GUID dwKFFlags DWORD pszItem PCWSTR riid R.IID ppv P.PVOID
	// get the IDList expression from an object, works with objects that support IPersistIDlist or IPersistIDlist like CLSID_ShellItem and most shell folders
	ff shell32.SHGetIDListFromObject HRESULT punk P.IUnknown ppidl P.P.ITEMID_CHILD
	// similar to SHGetIDListFromObject but returns an IShellItem-based object (preferred for performance if the IDList is already bound to a folder)
	ff shell32.SHGetItemFromObject HRESULT punk P.IUnknown riid R.IID ppv P.PVOID

	// these APIs return object that support IPropertyStore or related interfaces
	ff shell32.SHGetPropertyStoreFromIDList HRESULT pidl P.ITEMID_CHILD flags GETPROPERTYSTOREFLAGS riid R.IID ppv P.PVOID
	ff shell32.SHGetPropertyStoreFromParsingName HRESULT pszPath PCWSTR pbc P.IBindCtx flags GETPROPERTYSTOREFLAGS riid R.IID ppv P.PVOID
	ff shell32.SHGetNameFromIDList HRESULT pidl P.ITEMID_CHILD sigdnName SIGDN ppszName P.PWSTR
~
}
	
ifver @WIN7
{
	ed DATAOBJ_GET_ITEM_FLAGS
	{
		ee DOGIF_DEFAULT 0x0000
		ee DOGIF_TRAVERSE_LINK 0x0001    // if the item is a link get the target
		ee DOGIF_NO_HDROP 0x0002    // don't fallback and use CF_HDROP clipboard format
		ee DOGIF_NO_URL 0x0004    // don't fallback and use URL clipboard format
		ee DOGIF_ONLY_IF_ONE 0x000    // only return the item if there is one item in the array
	}
	
	ff shell32.SHGetItemFromDataObject HRESULT pdtObj P.IDataObject dwFlags DATAOBJ_GET_ITEM_FLAGS riid R.IID ppv P.PVOID
~
}

//
// When requesting a property store through IShellFolder, you can specify the equivalent of
// GPS_DEFAULT by passing in a null IBindCtx parameter.
//
// You can specify the equivalent of GPS_READWRITE by passing a mode of STGM_READWRITE | STGM_EXCLUSIVE
// in the bind context
//
// Here are the string versions of GPS_ flags, passed to IShellFolder::BindToObject() via IBindCtx::RegisterObjectParam()
// These flags are valid when requesting an IPropertySetStorage or IPropertyStore handler
//
// The meaning of these flags are described above.
//
// There is no STR_ equivalent for GPS_TEMPORARY because temporary property stores
// are provided by IShellItem2 only -- not by the underlying IShellFolder.
//
eq STR_GPS_HANDLERPROPERTIESONLY "GPS_HANDLERPROPERTIESONLY"
eq STR_GPS_FASTPROPERTIESONLY "GPS_FASTPROPERTIESONLY"
eq STR_GPS_OPENSLOWITEM "GPS_OPENSLOWITEM"
eq STR_GPS_DELAYCREATION "GPS_DELAYCREATION"
eq STR_GPS_BESTEFFORT "GPS_BESTEFFORT"
eq STR_GPS_NO_OPLOCK "GPS_NO_OPLOCK"
~

I IShellItem2 ex IShellItem
{
	iid 7e9fb0d3-919f-4307-ab2e-9b1860310c93
	cf GetPropertyStore flags GETPROPERTYSTOREFLAGS riid R.IID ppv P.PVOID
	cf GetPropertyStoreWithCreateObject flags GETPROPERTYSTOREFLAGS punkCreateObject P.IUnknown riid R.IID ppv P.PVOID
	cf GetPropertyStoreForKeys rgKeys P.PROPERTYKEY cKeys UINT flags GETPROPERTYSTOREFLAGS riid R.IID ppv P.PVOID
	cf GetPropertyDescriptionList keyType R.PROPERTYKEY riid R.IID ppv P.PVOID
	cf Update pbc P.IBindCtx
	cf GetProperty key R.PROPERTYKEY ppropvar P.PROPVARIANT
	cf GetCLSID key R.PROPERTYKEY pclsid P.CLSID
	cf GetFileTime key R.PROPERTYKEY pft P.FILETIME
	cf GetInt32 key R.PROPERTYKEY pi P.INT
	cf GetString key R.PROPERTYKEY ppsz P.LPWSTR
	cf GetUInt32 key R.PROPERTYKEY pui P.ULONG
	cf GetUInt64 key R.PROPERTYKEY pull P.ULONGLONG
	cf GetBool key R.PROPERTYKEY pf P.BOOL
}

ed SIIGBF
{
	ee SIIGBF_RESIZETOFIT 0x00000000   // If necessary, shrink the bitmap (preserving aspect ratio) so width and height fit the given size.
    ee SIIGBF_BIGGERSIZEOK 0x00000001   // A larger bitmap than requested may be returned, the caller will manage scaling down (inverse of SIIGBF_RESIZETOFIT).
    ee SIIGBF_MEMORYONLY 0x00000002   // Return the item only if it is already in memory. Do not access the disk even if the item is cached.
    ee SIIGBF_ICONONLY 0x00000004   // Return only the icon, never the thumbnail.
    ee SIIGBF_THUMBNAILONLY 0x00000008   // Return only the thumbnail, never the icon.
    ee SIIGBF_INCACHEONLY 0x00000010   // Allows access to the disk, but only to retrieve a cached item.
    ee SIIGBF_CROPTOSQUARE 0x00000020   // Windows 8 and later. If necessary, crop the bitmap to a square.
    ee SIIGBF_WIDETHUMBNAILS 0x00000040   // Windows 8 and later. Stretch and crop the bitmap to a .7 aspect ratio.
    ee SIIGBF_ICONBACKGROUND 0x00000080   // Windows 8 and later. If returning an icon, paint a background using the associated app's registered background color.
    ee SIIGBF_SCALEUP 0x00000100   // Windows 8 and later. If necessary, stretch the bitmap so width and height fit the given size.
}

IU IShellItemImageFactory
{
	iid bcc18b79-ba16-442f-80c4-8a59c30c463b
	cf GetImage size SIZE flags SIIGBF phbm P.HBITMAP
}

IU IEnumShellItems
{
	iid 70629033-e363-4a28-a567-0db78006e6d7
	cf Next celt ULONG rgelt P.P.IShellItem pceltFetched P.ULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppenum FD.P.P.IEnumShellItems
}

eq STGTRANSCONFIRMATION GUID
eq LPSTGTRANSCONFIRMATION LPGUID
~

ed STGOP
{
	ee STGOP_MOVE 1
	ee STGOP_COPY 2
	ee STGOP_SYNC 3
	ee STGOP_REMOVE 5
	ee STGOP_RENAME 6
	ee STGOP_APPLYPROPERTIES 8
	ee STGOP_NEW 10
}

ed TRANSFER_SOURCE_FLAGS
{
    ee TSF_NORMAL                      0x00000000
    ee TSF_FAIL_EXIST                  0x00000000   // Fail if destination already exists
    ee TSF_RENAME_EXIST                0x00000001   // Rename with auto-name generation if destination already exists
    ee TSF_OVERWRITE_EXIST             0x00000002   // Overwrite/Merge with destination
    ee TSF_ALLOW_DECRYPTION            0x00000004   // Allow creation of decrypted destination
    ee TSF_NO_SECURITY                 0x00000008   // Without DACL/SACL/Owner
    ee TSF_COPY_CREATION_TIME          0x00000010   // Copy the creation time as part of the copy (useful for move as copy/delete)
    ee TSF_COPY_WRITE_TIME             0x00000020   // Copy the last write time as part of the copy
    ee TSF_USE_FULL_ACCESS             0x00000040   // Open a file with write, read, or delete as share mode
    ee TSF_DELETE_RECYCLE_IF_POSSIBLE  0x00000080   // Recycle if possible
    ee TSF_COPY_HARD_LINK              0x00000100   // Hard link desired (not required)
    ee TSF_COPY_LOCALIZED_NAME         0x00000200   // Copy localized name
    ee TSF_MOVE_AS_COPY_DELETE         0x00000400   // We are doing a move operation, but we are doing it as a copy/delete
    ee TSF_SUSPEND_SHELLEVENTS         0x00000800   // suspend shell events
}

ifver_ie @IE70
{
	ed TRANSFER_ADVISE_STATUS
	{
		ee TS_NONE 0
		ee TS_PERFORMING 1
		ee TS_PREPARING 2
		ee TS_INDETERMINATE 4
	}
	
	IU ITransferAdviseSink
	{
		iid d594d0d8-8da7-457b-b3b4-ce5dbaac0b88
		cf UpdateProgress ullSizeCurrent ULONGLONG ullSizeTotal ULONGLONG nFilesCurrent INT nFilesTotal INT nFoldersCurrent INT nFoldersTotal INT
		cf UpdateTransferState ts TRANSFER_ADVISE_STATUS
		cf ConfirmOverwrite psiSource P.IShellItem psiDestParent P.IShellItem pszName LPCWSTR
		cf ConfirmEncryptionLoss psiSource P.IShellItem
		cf FileFailure psi P.IShellItem pszItem LPCWSTR hrError HRESULT pszRename LPWSTR cchRename ULONG
		cf SubStreamFailure psi P.IShellItem pszStreamName LPCWSTR hrError HRESULT
		cf PropertyFailure psi P.IShellItem pkey P.PROPERTYKEY hrError HRESULT
	}
}

ifver @VISTA
{
	IU ITransferSource
	{
		iid 00adb003-bde9-45c6-8e29-d09f9353e108
		cf Advise psink P.ITransferAdviseSink pdwCookie P.DWORD
		cf Unadvise dwCookie DWORD
		cf SetProperties pproparray P.IPropertyChangeArray
		cf OpenItem psi P.IShellItem flags TRANSFER_SOURCE_FLAGS riid R.IID ppv P.PVOID
		cf MoveItem psi P.IShellItem psiParentDst P.IShellItem pszNameDst LPCWSTR flags TRANSFER_SOURCE_FLAGS ppsiNew P.P.IShellItem
		cf RecycleItem psiSource P.IShellItem psiParentDest P.IShellItem flags TRANSFER_SOURCE_FLAGS ppsiNewDst P.P.IShellItem
		cf RemoveItem psiSource P.IShellItem pszNewName LPCWSTR flags TRANSFER_SOURCE_FLAGS ppsiNewDest P.P.IShellItem
		cf LinkItem psiSource P.IShellItem psiParentDest P.IShellItem pszNewName LPCWSTR flags TRANSFER_SOURCE_FLAGS ppsiNewDst P.P.IShellItem
		cf ApplyPropertiesToItem psiSource P.IShellItem ppsiNew P.P.IShellItem
		cf GetDefaultDestinationName psiSource P.IShellItem psiParentDest P.IShellItem ppszDestinationName P.LPWSTR
		cf EnterFolder psiChildFolderDest P.IShellItem
		cf LeaveFolder psiChildFolderDest P.IShellItem
	}
}

sd SHELL_ITEM_RESOURCE
{
	sf GUID guidType
	sf IWideCharArrayFixedSize[260] szName
}

IU IEnumResources
{
	iid 2dd81fe3-a83c-4da9-a330-47249d345ba1
	cf Next celt ULONG psir P.SHELL_ITEM_RESOURCE pceltFetched P.ULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppenumr FD.P.P.IEnumResources
}

IU IShellItemResources
{
	iid ff5693be-2ce0-4d48-b5c5-40817d1acdb9
	cf GetAttributes pdwAttributes P.DWORD
	cf GetSize pullSize P.ULONGLONG
	cf GetTimes pftCreation P.FILETIME pftWrite P.FILETIME pftAccess P.FILETIME
	cf SetTimes pftCreation P.FILETIME pftWrite P.FILETIME pftAccess P.FILETIME
	cf GetResourceDescription pcsir P.SHELL_ITEM_RESOURCE ppszDescription P.LPWSTR
	cf EnumResource ppenumr P.P.IEnumResources
	cf SupportsResource pcsir P.SHELL_ITEM_RESOURCE
	cf OpenResource pcsir P.SHELL_ITEM_RESOURCE riid R.IID ppv P.PVOID
	cf CreateResource pcsir P.SHELL_ITEM_RESOURCE riid R.IID ppv P.PVOID
	cf MarkForDelete
}

IU ITransferDestination
{
	iid 48addd32-3ca5-4124-abe3-b5a72531b207
	cf Advise psink P.ITransferAdviseSink pdwCookie P.DWORD
	cf Unadvise dwCookie DWORD
	cf CreateItem pszName LPCWSTR dwAttributes DWORD ullSize ULONGLONG flags TRANSFER_SOURCE_FLAGS riidItem R.IID ppvItem P.PVOID riidResources R.IID ppvResources P.PVOID
}

ifver_ie @IE70
{
	IU IFileOperationProgressSink
	{
		iid 04b0f1a7-9490-44bc-96e1-4296a31252e2
		cf StartOperations
		cf FinishOperations hrResult HRESULT
		cf PreRenameItem dwFlags DWORD psiItem P.IShellItem pszNewName LPCWSTR
		cf PostRenameItem dwFlags DWORD psiItem P.IShellItem pszNewName LPCWSTR hrRename HRESULT psiNewlyCreated P.IShellItem
		cf PreMoveItem dwFlags DWORD psiItem P.IShellItem psiDestinationFolder P.IShellItem pszNewName LPCWSTR
		cf PostMoveItem dwFlags DWORD psiItem P.IShellItem psiDestinationFolder P.IShellItem pszNewName LPCWSTR hrMove HRESULT psiNewlyCreated P.IShellItem
		cf PreCopyItem dwFlags DWORD psiItem P.IShellItem psiDestinationFolder P.IShellItem pszNewName LPCWSTR
		cf PostCopyItem dwFlags DWORD psiItem P.IShellItem psiDestinationFolder P.IShellItem pszNewName LPCWSTR hrCopy HRESULT psiNewlyCreated P.IShellItem
		cf PreDeleteItem dwFlags DWORD psiItem P.IShellItem
		cf PostDeleteItem dwFlags DWORD psiItem P.IShellItem hrDelete HRESULT psiNewlyCreated P.IShellItem
		cf PreNewItem dwFlags DWORD psiDestinationFolder P.IShellItem pszNewName LPCWSTR
		cf PostNewItem dwFlags DWORD psiDestinationFolder P.IShellItem pszNewName LPCWSTR dwFileAttributes DWORD hrNew HRESULT psiNewItem P.IShellItem
		cf UpdateProgress iWorkTotal UINT iWorkSoFar UINT
		cf ResetTimer
		cf PauseTimer
		cf ResumeTimer
	}
}

ed SIATTRIBFLAGS
{
	ee SIATTRIBFLAGS_AND 1
	ee SIATTRIBFLAGS_OR 2
	ee SIATTRIBFLAGS_APPCOMPAT 3
	ee SIATTRIBFLAGS_MASK 3
	ee SIATTRIBFLAGS_ALLITEMS 0x4000
}

IU IShellItemArray
{
	iid b63ea76d-1f85-456f-a19c-48159efa858b
	cf BindToHandler pbc P.IBindCtx bhid R.GUID riid R.IID ppvOut P.PVOID
	cf GetPropertyStore flags GETPROPERTYSTOREFLAGS riid R.IID ppv P.PVOID
	cf GetPropertyDescriptionList keyType R.PROPERTYKEY riid R.IID ppv P.PVOID
	cf GetAttributes AttribFlags SIATTRIBFLAGS sfgaoMask SFGAOF psfgaoAttribs P.SFGAOF
	cf GetCount pdwNumItems P.DWORD
	cf GetItemAt dwIndex DWORD ppsi P.P.IShellItem
	cf EnumItems ppenumShellItems P.P.IEnumShellItems
}

ifver_ie @IE70
{
	ff shell32.SHCreateShellItemArray HRESULT pidlParent P.ITEMID_CHILD psf P.IShellFolder cidl UINT ppidl P.P.ITEMID_CHILD ppsiItemArray P.P.IShellItemArray
	ff shell32.SHCreateShellItemArrayFromDataObject HRESULT pdo P.IDataObject riid R.IID ppv P.PVOID
	ff shell32.SHCreateShellItemArrayFromIDLists HRESULT cidl UINT rgpidl P.P.ITEMID_CHILD ppsiItemArray P.P.IShellItemArray
	ff shell32.SHCreateShellItemArrayFromShellItem HRESULT psi P.IShellItem riid R.IID ppv P.PVOID
}

IU IInitializeWithItem
{
	iid 7f73be3f-fb79-493c-a6c7-7ee14e245841
	cf Initialize psi P.IShellItem grfMode DWORD
}

IU IObjectWithSelection
{
	iid 1c9cd5bb-98e9-4491-a60f-31aacc72b83c
	cf SetSelection psia P.IShellItemArray
	cf GetSelection riid R.IID ppv P.PVOID
}

IU IObjectWithBackReferences
{
	iid 321a6a6a-d61f-4bf3-97ae-14be2986bb36
	cf RemoveBackReferences
}

ed PROPERTYUI_FLAGS
{
	ee PUIF_DEFAULT 0
	ee PUIF_RIGHTALIGN 1
	ee PUIF_NOLABELININFOTIP 2
}

ed PROPERTYUI_FORMAT_FLAGS
{
	ee PUIFFDF_DEFAULT 0
	ee PUIFFDF_RIGHTTOLEFT 1
	ee PUIFFDF_SHORTFORMAT 2
	ee PUIFFDF_NOTIME 4
	ee PUIFFDF_FRIENDLYDATE 8
}

IU IPropertyUI
{
	iid 757a7d9f-919a-4118-99d7-dbb208c8cc66
	cf ParsePropertyName pszName LPCWSTR pfmtid P.FMTID ppid P.PROPID pchEaten P.ULONG
	cf GetCannonicalName fmtid R.FMTID pid PROPID pwszText LPWSTR cchText DWORD
	cf GetDisplayName fmtid R.FMTID pid PROPID flags PROPERTYUI_NAME_FLAGS pwszText LPWSTR cchText DWORD
	cf GetPropertyDescription fmtid R.FMTID pid PROPID pwszText LPWSTR cchText DWORD
	cf GetDefaultWidth fmtid R.FMTID pid PROPID pcxChars P.ULONG
	cf GetFlags fmtid R.FMTID pid PROPID pflags P.PROPERTYUI_FLAGS
	cf FormatForDisplay fmtid R.FMTID pid PROPID ppropvar P.PROPVARIANT puiff PROPERTYUI_FORMAT_FLAGS pwszText LPWSTR cchText DWORD
	cf GetHelpInfo fmtid R.FMTID pid PROPID pwszHelpFile LPWSTR cch DWORD puHelpID P.UINT
}

IU ICategoryProvider
{
	iid 9af64809-5864-4c26-a720-c1f78c086ee3
	cf CanCategorizeOnSCID pscid P.SHCOLUMNID
	cf GetDefaultCategory pguid P.GUID pscid P.SHCOLUMNID
	cf GetCategoryForSCID pscid P.SHCOLUMNID pguid P.GUID
	cf EnumCategories penum P.P.IEnumGUID
	cf GetCategoryName pguid P.GUID pszName LPWSTR cch UINT
	cf CreateCategory pguid P.GUID riid R.IID ppv P.PVOID
}

ed CATEGORYINFO_FLAGS
{
	ee CATINFO_NORMAL 0x00000000   // Apply default properties to this category
    ee CATINFO_COLLAPSED 0x00000001   // This category should appear collapsed. useful for the "None" category.
    ee CATINFO_HIDDEN 0x00000002   // This category should follow the "Hidden" files setting for being displayed
    ee CATINFO_EXPANDED 0x00000004   // This category should appear expanded.
    ee CATINFO_NOHEADER 0x00000008   // This category has no header.
    ee CATINFO_NOTCOLLAPSIBLE 0x00000010   // This category can not be collapsed.
    ee CATINFO_NOHEADERCOUNT 0x00000020   // The count of items in the category should not be displayed in the header
    // Win7 Flags
    ee CATINFO_SUBSETTED 0x00000040   // The category should appear subsetted.
    // Threshold Flags
    ee CATINFO_SEPARATE_IMAGES 0x00000080   // The category should use its own image list.
    ee CATINFO_SHOWEMPTY 0x00000100   // Show the category even when empty.
}

ed CATSORT_FLAGS
{
	ee CATSORT_DEFAULT 0
	ee CATSORT_NAME 1
}

sd CATEGORY_INFO
{
	sf IInteger[CATEGORYINFO_FLAGS] cif
	sf IWideCharArrayFixedSize[260] wszName
}

IU ICategorizer
{
	iid a3b14589-9174-49a8-89a3-06a1ae2b9ba7
	cf GetDescription pszDesc LPWSTR cch UINT
	cf GetCategory cidl UINT apidl P.ITEMID_CHILD rgCategoryIds P.DWORD
	cf GetCategoryInfo dwCategoryId DWORD pci P.CATEGORY_INFO
	cf CompareCategory csfFlags CATSORT_FLAGS dwCategoryId1 DWORD dwCategoryId2 DWORD
}

ifver @WIN2K
{
	sd SHDRAGIMAGE
	{
		sf SIZE sizeDragImage
		sf POINT ptOffset
		sf IHandle hbmpDragImage
		sf IInteger[COLORREF] crColorKey
	}

	pie SHDRAGIMAGE LPSHDRAGIMAGE

	eq DI_GETDRAGIMAGE TEXT("ShellGetDragImage")
~

	IU IDropTargetHelper
	{
		iid 4657278B-411B-11D2-839A-00C04FD918D0
		cf DragEnter hwndTarget HWND pDataObject P.IDataObject ppt P.POINT dwEffect DWORD
		cf DragLeave
		cf DragOver ppt P.POINT dwEffect DWORD
		cf Drop pDataObject P.IDataObject ppt P.POINT dwEffect DWORD
		cf Show fShow BOOL
	}

	IU IDragSourceHelper
	{
		iid DE5BF786-477A-11D2-839D-00C04FD918D0
		cf InitializeFromBitmap pshdi P.SHDRAGIMAGE pDataObject P.IDataObject
		cf InitializeFromWindow hwnd HWND ppt P.POINT pDataObject P.IDataObject
	}
}

ed SLR_FLAGS
{
    ee SLR_NONE 0x0
    ee SLR_NO_UI 0x0001   // don't display any UI during the resolve operation, call blocks until done
    ee SLR_ANY_MATCH 0x0002   // no longer used
    ee SLR_UPDATE 0x0004   // save the link back to it's file if the track made it dirty
    ee SLR_NOUPDATE 0x0008   // don't update the link file (if there is one) if the resolve made it dirty
    ee SLR_NOSEARCH 0x0010   // don't execute the search heuristics
    ee SLR_NOTRACK 0x0020   // don't use the link tracking service (trkwks) to find the target
    ee SLR_NOLINKINFO 0x0040   // don't use the network and volume serial number information
    ee SLR_INVOKE_MSI 0x0080   // for MSI links call MSI to install the application
    ee SLR_NO_UI_WITH_MSG_PUMP 0x0101   // don't display UI but enter a nested message loop and wait for the resolve to finish
    ee SLR_OFFER_DELETE_WITHOUT_FILE 0x0200   // offer the option to delete when unable to resolve, even if the shortcut is not stored in a file
    ee SLR_KNOWNFOLDER 0x0400   // update known folder information if path changes due to folder redirection
    ee SLR_MACHINE_IN_LOCAL_TARGET 0x0800   // resolve machine name in UNC targets pointing to local machine (used with SLDF_KEEP_LOCAL_IDLIST_FOR_UNC_TARGET)
    ee SLR_UPDATE_MACHINE_AND_SID 0x1000   // update machine GUID and user SID if necessary
    ee SLR_NO_OBJECT_ID 0x2000   // don't use the Volume Id and Object Id to locate the file.
}

ed SLGP_FLAGS
{
    ee SLGP_SHORTPATH 0x0001
    ee SLGP_UNCPRIORITY 0x0002
    ee SLGP_RAWPATH 0x0004
    ee SLGP_RELATIVEPRIORITY 0x0008
}

IU IShellLinkA
{
	iid 000214EE-0000-0000-C000-000000000046
	cf GetPath pszFile LPSTR cch INT pfd P.WIN32_FIND_DATAA fFlags DWORD
	cf GetIDList ppidl P.P.ITEMID_CHILD
	cf SetIDList pidl P.ITEMID_CHILD
	cf GetDescription pszName LPSTR cch INT
	cf SetDescription pszName LPCSTR
	cf GetWorkingDirectory pszDir LPSTR cch INT
	cf SetWorkingDirectory pszDir LPCSTR
	cf GetArguments pszArgs LPSTR cch INT
	cf SetArguments pszArgs LPCSTR
	cf GetHotkey pwHotkey P.WORD
	cf SetHotkey wHotkey WORD
	cf GetShowCmd piShowCmd P.INT
	cf SetShowCmd iShowCmd INT
	cf GetIconLocation pszIconPath LPSTR cch INT piIcon P.INT
	cf SetIconLocation pszIconPath LPCSTR iIcon INT
	cf SetRelativePath pszPathRel LPCSTR dwReserved DWORD
	cf Resolve hwnd HWND fFlags DWORD
	cf SetPath pszFile LPCSTR
}

IU IShellLinkW
{
	iid 000214F9-0000-0000-C000-000000000046
	cf GetPath pszFile LPWSTR cch INT pfd P.WIN32_FIND_DATAA fFlags DWORD
	cf GetIDList ppidl P.P.ITEMID_CHILD
	cf SetIDList pidl P.ITEMID_CHILD
	cf GetDescription pszName LPWSTR cch INT
	cf SetDescription pszName LPCWSTR
	cf GetWorkingDirectory pszDir LPWSTR cch INT
	cf SetWorkingDirectory pszDir LPCWSTR
	cf GetArguments pszArgs LPWSTR cch INT
	cf SetArguments pszArgs LPCWSTR
	cf GetHotkey pwHotkey P.WORD
	cf SetHotkey wHotkey WORD
	cf GetShowCmd piShowCmd P.INT
	cf SetShowCmd iShowCmd INT
	cf GetIconLocation pszIconPath LPWSTR cch INT piIcon P.INT
	cf SetIconLocation pszIconPath LPCWSTR iIcon INT
	cf SetRelativePath pszPathRel LPCWSTR dwReserved DWORD
	cf Resolve hwnd HWND fFlags DWORD
	cf SetPath pszFile LPCWSTR
}

unicode
{
	eq IShellLink IShellLinkW
elsedef
	eq IShellLink IShellLinkA
}
~

IU IShellLinkDataList
{
	iid 45e2b4ae-b1c3-11d0-b92f-00a0c90312e1
	cf AddDataBlock pDataBlock PVOID
	cf CopyDataBlock dwSig DWORD ppDataBlock P.PVOID
	cf RemoveDataBlock dwSig DWORD
	cf GetFlags pdwFlags P.DWORD
	cf SetFlags dwFlags DWORD
}

ifver @WIN2K
{
	IU IResolveShellLink
	{
		iid 5cd52983-9449-11d2-963a-00c04f79adf0
		cf ResolveShellLink punkLink P.IUnknown hwnd HWND fFlags DWORD
	}
}

ed SPINITF
{
	ee SPINITF_NORMAL 0
	ee SPINITF_MODAL 1
	ee SPINITF_NOMINIMIZE 8
}

IU IActionProgressDialog
{
	iid 49ff1172-eadc-446d-9285-156453a6431c
	cf Initialize flags SPINITF pszTitle LPCWSTR pszCancel LPCWSTR
	cf Stop
}

// Do not use 0x1, it was used to indicate cancellation in legacy autoplay.
eq ARCONTENT_AUTORUNINF 0x00000002   // That's the one we have today, and always had
eq ARCONTENT_AUDIOCD 0x00000004   // Audio CD (not MP3 and the like, the stuff you buy at the store)
eq ARCONTENT_DVDMOVIE 0x00000008   // DVD Movie (not MPEGs, the stuff you buy at the store)
eq ARCONTENT_BLANKCD 0x00000010   // Blank CD-R/CD-RW)
eq ARCONTENT_BLANKDVD 0x00000020   // Blank DVD-R/DVD-RW
eq ARCONTENT_UNKNOWNCONTENT 0x00000040   // Whatever files.  Mean that it's formatted.
eq ARCONTENT_AUTOPLAYPIX 0x00000080   // Any files classified by shell as image. (jpg, bmp, etc.)
eq ARCONTENT_AUTOPLAYMUSIC 0x00000100   // Any files classified by shell as music. (wma, mp3, etc.)
eq ARCONTENT_AUTOPLAYVIDEO 0x00000200   // Any files classified by shell as video. (mpg, avi, etc.)

ifver @VISTA
{
	eq ARCONTENT_VCD 0x00000400   // VCD format
	eq ARCONTENT_SVCD 0x00000800   // Super-VCD format
	eq ARCONTENT_DVDAUDIO 0x00001000   // DVD-Audio
	eq ARCONTENT_BLANKBD 0x00002000   // Blank BD-R/BD-RW
	eq ARCONTENT_BLURAY 0x00004000   // Blu-ray Disc
	eq ARCONTENT_CAMERASTORAGE 0x00008000   // Camera Storage
	eq ARCONTENT_CUSTOMEVENT 0x00010000   // Custom Event
	eq ARCONTENT_NONE 0x00000000 // Empty (but formatted)
	eq ARCONTENT_MASK 0x0001FFFE // Bits that denote valid content types

	eq ARCONTENT_PHASE_UNKNOWN 0x00000000   // We can be in any phase.  This is XP behavior.
	eq ARCONTENT_PHASE_PRESNIFF 0x10000000   // These are contents we know w/o scanning the media for complete data (e.g. Audio track, DVD Movie).
	eq ARCONTENT_PHASE_SNIFFING 0x20000000   // We are in the middle of searching the media.  There could be more contents to be found than currently reported.
	eq ARCONTENT_PHASE_FINAL 0x40000000   // We have finished searching; contents we report are final.
	eq ARCONTENT_PHASE_MASK 0x70000000   // Bits that denote what phase we are in the Autoplay process.
}
~

ed SPBEGINF
{
	ee SPBEGINF_NORMAL 0
	ee SPBEGINF_AUTOTIME 2
	ee SPBEGINF_NOPROGRESSBAR 16
	ee SPBEGINF_MARQUEEPROGRESS 32
	ee SPBEGINF_NOCANCELBUTTON 64
}

ed SPACTION
{
	ee SPACTION_NONE 0
	ee SPACTION_MOVING
	ee SPACTION_COPYING
	ee SPACTION_RECYCLING
	ee SPACTION_APPLYINGATTRIBS
	ee SPACTION_DOWNLOADING
	ee SPACTION_SEARCHING_INTERNET
	ee SPACTION_CALCULATING
	ee SPACTION_UPLOADING
	ee SPACTION_SEARCHING_FILES
	ee SPACTION_DELETING                            // Vista or higher
	ee SPACTION_RENAMING                            // Vista or higher
	ee SPACTION_FORMATTING                          // Vista or higher
	ee SPACTION_COPY_MOVING                         // Move as copy-delete, Windows 7 or higher
}

ed SPTEXT
{
	ee SPTEXT_ACTIONDESCRIPTION 1
	ee SPTEXT_ACTIONDETAIL
}

IU IActionProgress
{
	iid 49ff1173-eadc-446d-9285-156453a6431c
	cf Begin action SPACTION flags SPBEGINF
	cf UpdateProgress ulCompleted ULONGLONG ulTotal ULONGLONG
	cf UpdateText spText SPTEXT pszText LPCWSTR fMayCompact BOOL
	cf QueryCancel pfCancelled P.BOOL
	cf ResetCancel
	cf End
}

IU IShellExtInit
{
	iid 000214E8-0000-0000-C000-000000000046
	cf Initialize pidlFolder P.ITEMID_CHILD pdtObj P.IDataObject hkeyProgID HKEY
}

pi LPSHELLEXTINIT

ed EXPPS
{
	ee EXPPS_FILETYPES 1
}

IU IShellPropSheetExt
{
	iid 000214E9-0000-0000-C000-000000000046
	cf AddPages pfnAddPage LPFNSVADDPROPSHEETPAGE lParam LPARAM
	cf ReplacePage uPageID EXPPS pfnReplaceWith LPFNSVADDPROPSHEETPAGE lParam LPARAM
}

pi LPSHELLPROPSHEETEXT

IU IRemoteComputer
{
	iid 000214FE-0000-0000-C000-000000000046
	cf Initialize pszMachine LPCWSTR bEnumerating BOOL
}

IU IQueryContinue
{
	iid 7307055c-b24a-486b-9f25-163e597a28a9
	cf QueryContinue
}

IU IObjectWithCancelEvent
{
	iid F279B885-0AE9-4b85-AC06-DDECF9408941
	cf GetCancelEvent phEvent P.HANDLE
}

IU IUserNotification
{
	iid ba9711ba-5893-4787-a7e1-41277151550b
	cf SetBalloonInfo pszTitle LPCWSTR pszText LPCWSTR dwInfoFlags DWORD
	cf SetBalloonRetry dwShowTime DWORD dwInterval DWORD cRetryCount UINT
	cf SetIconInfo hIcon HICON pszToolTip LPCWSTR
	cf Show pqc P.IQueryContinue dwContinuePollInterval DWORD
	cf PlaySound pszSoundName LPCWSTR
}

IU IItemNameLimits
{
	iid 1df0d7f1-b267-4d28-8b10-12e23202a5c4
	cf GetValidCharacters ppwszValidChars P.LPWSTR ppwszInvalidChars P.LPWSTR
	cf GetMaxLength pszName LPCWSTR piMaxNameLen P.INT
}

ifver @VISTA
{
	IU ISearchFolderItemFactory
	{
		iid a0ffbc28-5482-4366-be27-3e81e78e06c2
		cf SetDisplayName pszDisplayName LPCWSTR
		cf SetFolderTypeID ftid GUID
		cf SetFolderLogicalViewMode flvm FOLDERLOGICALVIEWMODE
		cf SetIconSize iIconSize INT
		cf SetVisibleColumns cVisibleColumns UINT rgKey P.PROPERTYKEY
		cf SetSortColumns cSortColumns UINT rgSortColumns P.SORTCOLUMN
		cf SetGroupColumn keyGroup R.PROPERTYKEY
		cf SetStacks cStacksKeys UINT rgStackKeys P.PROPERTYKEY
		cf SetScope psiaScope P.IShellItemArray
		cf SetCondition pCondition P.ICondition
		cf GetShellItem riid R.IID ppv P.PVOID
		cf GetIDList ppidl P.P.ITEMID_CHILD
	}
}

eq IEI_PRIORITY_MAX ITSAT_MAX_PRIORITY
eq IEI_PRIORITY_MIN ITSAT_MIN_PRIORITY
eq IEIT_PRIORITY_NORMAL ITSAT_DEFAULT_PRIORITY
~

eq IEIFLAG_ASYNC 0x0001      // (deprecated) ask the extractor if it supports ASYNC extract (free threaded)
eq IEIFLAG_CACHE 0x0002      // returned from the extractor if it does NOT cache the thumbnail
eq IEIFLAG_ASPECT 0x0004      // passed to the extractor to beg it to render to the aspect ratio of the supplied rect
eq IEIFLAG_OFFLINE 0x0008      // if the extractor shouldn't hit the net to get any content neede for the rendering
eq IEIFLAG_GLEAM 0x0010      // does the image have a gleam ? this will be returned if it does
eq IEIFLAG_SCREEN 0x0020      // render as if for the screen  (this is exlusive with IEIFLAG_ASPECT )
eq IEIFLAG_ORIGSIZE 0x0040      // render to the approx size passed, but crop if neccessary
eq IEIFLAG_NOSTAMP 0x0080      // returned from the extractor if it does NOT want an icon stamp on the thumbnail
eq IEIFLAG_NOBORDER    0x0100      // returned from the extractor if it does NOT want an a border around the thumbnail
eq IEIFLAG_QUALITY 0x0200      // passed to the Extract method to indicate that a slower, higher quality image is desired, re-compute the thumbnail
eq IEIFLAG_REFRESH 0x0400      // returned from the extractor if it would like to have Refresh Thumbnail available
~

IU IExtractImage
{
	iid BB2E617C-0920-11d1-9A0B-00C04FC2D6C1
	cf GetLocation pszPathBuffer LPWSTR cch DWORD pdwPriority P.DWORD prgSize P.SIZE dwRecClrDepth DWORD pdwFlags P.DWORD
	cf Extract phBmpThumbnail P.HBITMAP
}

pi LPEXTRACTIMAGE

I IExtractImage2 ex IExtractImage
{
	iid 953BB1EE-93B4-11d1-98A3-00C04FB687DA
	cf GetDateStamp pDateStamp P.FILETIME
}

IU IThumbnailHandlerFactory
{
	iid e35b4b2e-00da-4bc1-9f13-38bc11f5d417
	cf GetThumbnailHandler pidlChild P.ITEMID_CHILD pbc P.IBindCtx riid R.IID ppv P.PVOID
}

IU IParentAndItem
{
	iid b3a4b685-b685-4805-99d9-5dead2873236
	cf SetParentAndItem pidlParent P.ITEMID_CHILD psf P.IShellFolder pidlChild P.ITEMID_CHILD
	cf GetParentAndItem ppidlParent P.P.ITEMID_CHILD ppsf P.P.IShellFolder ppidlChild P.P.ITEMID_CHILD
}

I IDockingWindow ex IOleWindow
{
	iid 012dd920-7b26-11d0-8ca9-00a0c92dbfe8
	cf ShowDW fShow BOOL
	cf CloseDW dwReserved DWORD
	cf ResizeBorderDW prcBorder P.RECT punkToolbarSite P.IUnknown fReserved BOOL
}

eq DBIM_MINSIZE 0x0001
eq DBIM_MAXSIZE 0x0002
eq DBIM_INTEGRAL 0x0004
eq DBIM_ACTUAL 0x0008
eq DBIM_TITLE 0x0010
eq DBIM_MODEFLAGS 0x0020
eq DBIM_BKCOLOR 0x0040
~

sd DESKBANDINFO
{
	sf IDword dwMask
	sf POINTL ptMinSize
	sf POINTL ptMaxSize
	sf POINTL ptIntegral
	sf POINTL ptActual
	sf IWideCharArrayFixedSize[256] wszTitle
	sf IDword dwModeFlags
	sf IInteger[COLORREF] crBkgnd
}

// DESKBANDINFO dwModeFlags values
eq DBIMF_NORMAL 0x0000
eq DBIMF_FIXED 0x0001
eq DBIMF_FIXEDBMP 0x0004   // a fixed background bitmap (if supported)
eq DBIMF_VARIABLEHEIGHT 0x0008
eq DBIMF_UNDELETEABLE 0x0010
eq DBIMF_DEBOSSED 0x0020
eq DBIMF_BKCOLOR 0x0040
eq DBIMF_USECHEVRON 0x0080
eq DBIMF_BREAK 0x0100
eq DBIMF_ADDTOFRONT 0x0200
eq DBIMF_TOPALIGN 0x0400

ifver @VISTA
{
	eq DBIMF_NOGRIPPER 0x0800
	eq DBIMF_ALWAYSGRIPPER 0x1000
	eq DBIMF_NOMARGINS 0x2000
}
~

// GetBandInfo view mode values
eq DBIF_VIEWMODE_NORMAL 0x0000
eq DBIF_VIEWMODE_VERTICAL 0x0001
eq DBIF_VIEWMODE_FLOATING 0x0002
eq DBIF_VIEWMODE_TRANSPARENT 0x0004
~

ed DESKBANDCID
{
    ee DBID_BANDINFOCHANGED 0
    ee DBID_SHOWONLY 1
    ee DBID_MAXIMIZEBAND 2      // Maximize the specified band (VT_UI4 =dwID)
    ee DBID_PUSHCHEVRON 3
    ee DBID_DELAYINIT 4      // Note: _bandsite_ calls _band_ with this code
    ee DBID_FINISHINIT 5      // Note: _bandsite_ calls _band_ with this code
    ee DBID_SETWINDOWTHEME 6      // Note: _bandsite_ calls _band_ with this code
    ee DBID_PERMITAUTOHIDE 7
}

eq DBPC_SELECTFIRST DWORD(-1).value
eq DBPC_SELECTLAST DWORD(-2).value
~

I IDeskBand ex IDockingWindow
{
	iid EB0FE172-1A3A-11D0-89B3-00A0C90A90AC
	cf GetBandInfo dwBandID DWORD dwViewMode DWORD pdbi P.DESKBANDINFO
}

eq CGID_IDeskBand IDeskBand._iid_
~

ifver @VISTA
{
	IU IDeskBandInfo
	{
		iid 77E425FC-CBF9-4307-BA6A-BB5727745661
		cf GetDefaultBandWidth dwBandID DWORD dwViewMode DWORD pnWidth P.INT
	}
}

IU ITaskbarList
{
	iid 56FDF342-FD6D-11d0-958A-006097C9A090
	cf HrInit
	cf AddTab hwnd HWND
	cf DeleteTab hwnd HWND
	cf ActivateTab hwnd HWND
	cf SetActiveAlt hwnd HWND
}

I ITaskbarList2 ex ITaskbarList
{
	iid 602D4995-B13A-429b-A66E-1935E44F4317
	cf MarkFullscreenWindow hwnd HWND fFullscreen BOOL
}

ed THUMBBUTTONFLAGS
{
    ee THBF_ENABLED 0x00000000
    ee THBF_DISABLED 0x00000001
    ee THBF_DISMISSONCLICK 0x00000002
    ee THBF_NOBACKGROUND 0x00000004
    ee THBF_HIDDEN 0x00000008
    ee THBF_NONINTERACTIVE 0x00000010
}

ed THUMBBUTTONMASK
{
    ee THB_BITMAP 0x00000001
    ee THB_ICON 0x00000002
    ee THB_TOOLTIP 0x00000004
    ee THB_FLAGS 0x00000008
}

sd THUMBBUTTON
{
	sf IInteger[THUMBBUTTONMASK] dwMask
	sf IUint iId
	sf IUint iBitmap
	sf IInteger[HICON] hIcon
	sf IWideCharArrayFixedSize[260] szTip
	sf IInteger[THUMBBUTTONFLAGS] dwFlags
}

pie THUMBBUTTON LPTHUMBBUTTON

eq THBN_CLICKED 0x1800
~

ed TBPFLAG
{
	ee TBPF_NOPROGRESS 0x00000000
	ee TBPF_INDETERMINATE 0x00000001
	ee TBPF_NORMAL 0x00000002
	ee TBPF_ERROR 0x00000004
	ee TBPF_PAUSED 0x00000008
}

I ITaskbarList3 ex ITaskbarList2
{
	iid ea1afb91-9e28-4b86-90e9-9e9f8a5eefaf
	cf SetProgressValue hwnd HWND ullCompleted ULONGLONG ullTotal ULONGLONG
	cf SetProgressState hwnd HWND tbpFlags TBPFLAG
	cf RegisterTab hwndTab HWND hwndMDI HWND
	cf UnregisterTab hwndTab HWND
	cf SetTabOrder hwndTab HWND hwndInsertBefore HWND
	cf SetTabActive hwndTab HWND hwndMDI HWND dwReserved DWORD
	cf ThumbBarAddButtons hwnd HWND cButtons UINT pButton P.THUMBBUTTON
	cf ThumbBarUpdateButtons hwnd HWND cButtons UINT pButton P.THUMBBUTTON
	cf ThumbBarSetImageList hwnd HWND himl HIMAGELIST
	cf SetOverlayIcon hwnd HWND hIcon HICON pszDescription LPCWSTR
	cf SetThumbnailTooltip hwnd HWND pszTip LPCWSTR
	cf SetThumbnailClip hwnd HWND prcClip P.RECT
}

ed STPFLAG
{
	ee STPF_NONE 0x00000000
	ee STPF_USEAPPTHUMBNAILALWAYS 0x00000001
	ee STPF_USEAPPTHUMBNAILWHENACTIVE 0x00000002
	ee STPF_USEAPPPEEKALWAYS 0x00000004
	ee STPF_USEAPPPEEKWHENACTIVE 0x00000008
}

I ITaskbarList4 ex ITaskbarList3
{
	iid c43dc798-95d1-4bea-9030-bb99e2983a1a
	cf SetTabProperties hwndTab HWND stpFlags STPFLAG
}

ifver_ie @IE70
{
	IU IExplorerBrowserEvents
	{
		iid 361bbdc7-e6ee-4e13-be58-58e2240c810f
		cf OnNavigationPending pidlFolder P.ITEMID_CHILD
		cf OnViewCreated psv P.IShellView
		cf OnNavigationComplete pidlFolder P.ITEMID_CHILD
		cf OnNavigationFailed pidlFolder P.ITEMID_CHILD
	}
	
	ed EXPLORER_BROWSER_OPTIONS
	{
	    ee EBO_NONE 0x00000000     // No options
		ee EBO_NAVIGATEONCE 0x00000001     // Don't navigate after initial navigation
		ee EBO_SHOWFRAMES 0x00000002     // Show with frame module manager on - otherwise, single view object
		ee EBO_ALWAYSNAVIGATE 0x00000004     // Always navigate, even if you are attempting to navigate to the current folder
		ee EBO_NOTRAVELLOG 0x00000008     // Do not update travel log
		ee EBO_NOWRAPPERWINDOW 0x00000010     // For legacy clients that need the browser parented directly on themselves
		ee EBO_HTMLSHAREPOINTVIEW 0x00000020     // Show WebView for sharepoint sites
		ee EBO_NOBORDER 0x00000040     // Do not draw a border around ExplorerBrowser's HWND - Windows 8 and above
		ee EBO_NOPERSISTVIEWSTATE 0x00000080     // Do not persist the view state
	}
	
	ed EXPLORER_BROWSER_FILL_FLAGS
	{
	    ee EBF_NONE  0x0000000   // No flags
		// Causes FillFromObject to populate the ResultsFolder with the
		// contents of the parent folders of the items in the DataObject
		// and then check-selects only the items that are in the DataObject
		ee EBF_SELECTFROMDATAOBJECT 0x0000100
		// don't regsiter a drop target for the view, this enables apps to register their own drop target
		// that they can use to receive the drops
		ee EBF_NODROPTARGET 0x0000200
	}
	
	IU IExplorerBrowser
	{
		iid dfd3b6b5-c10c-4be9-85f6-a66969f402f6
		cf Initialize hwndParent HWND prc P.RECT pfs P.FOLDERSETTINGS
		cf DestroyViewWindow
		cf SetRect phdwp P.HDWP rcBrowser RECT
		cf SetPropertyBag pszPropertyBag LPCWSTR
		cf SetEmptyText pszEmptyText LPCWSTR
		cf SetFolderSettings pfs P.FOLDERSETTINGS
		cf Advise psbe P.IExplorerBrowserEvents pdwCookie P.DWORD
		cf Unadvise dwCookie DWORD
		cf SetOptions dwFlags EXPLORER_BROWSER_OPTIONS
		cf GetOptions pdwFlag P.EXPLORER_BROWSER_OPTIONS
		cf BrowseToIDList pidl P.ITEMID_CHILD uFlags UINT
		cf BrowseToObject punk P.IUnknown uFlags UINT
		cf FillFromObject punk P.IUnknown dwFlags EXPLORER_BROWSER_FILL_FLAGS
		cf RemoveAll
		cf GetCurrentView riid R.IID ppv P.PVOID
	}
	
	IU IEnumObjects
	{
		iid 2c1c7e2e-2d0e-4059-831e-1e6f82335c2e
		cf Next celt ULONG riid R.IID rgelt P.PVOID pceltFetched P.ULONG
		cf Skip celt ULONG
		cf Reset
		cf Clone ppenum FD.P.P.IEnumObjects
	}
	
	ed OPPROGDLGF
	{
	    // The flag space includes OPPROGDLG_ and PROGDLG_ values
		// please guarantee they don't conflict. See shlobj.w for PROGDLG_*
		ee OPPROGDLG_DEFAULT 0x00000000
		ee OPPROGDLG_ENABLEPAUSE 0x00000080   // Add a pause button (operation can be paused)
		ee OPPROGDLG_ALLOWUNDO 0x00000100   // The operation can be undone in the dialog.  (The Stop button becomes Undo)
		ee OPPROGDLG_DONTDISPLAYSOURCEPATH 0x00000200   // Don't display the path of source file in progress dialog
		ee OPPROGDLG_DONTDISPLAYDESTPATH 0x00000400   // Don't display the path of destination file in progress dialog
		ee OPPROGDLG_NOMULTIDAYESTIMATES 0x00000800   // deprecated - progress dialog no longer displays > 1 day estimates
		ee OPPROGDLG_DONTDISPLAYLOCATIONS 0x00001000   // Don't display the location line in the progress dialog
	}
	
	ed PDMODE
	{
	    ee PDM_DEFAULT 0x00000000
        ee PDM_RUN 0x00000001       // Operation is running
        ee PDM_PREFLIGHT 0x00000002       // Pre-flight mode, calculating operation time, etc
        ee PDM_UNDOING 0x00000004       // Operation is rolling back, undo has been selected
        ee PDM_ERRORSBLOCKING 0x00000008       // Only errors remain, error dialogs are blocking progress from completing
        ee PDM_INDETERMINATE 0x00000010       // The length of the operation is indeterminate, don't show a timer, progressbar is in marquee mode
	}
	
	ed PDOPSTATUS
	{
	    ee PDOPS_RUNNING 1       // Operation is running, no user intervention
        ee PDOPS_PAUSED 2       // Operation has been paused by the user
        ee PDOPS_CANCELLED 3       // Operation has been cancelled by the user - now go undo
        ee PDOPS_STOPPED 4       // Operation has been stopped by the user - terminate completely
        ee PDOPS_ERRORS 5       // Operation has gone as far as it can without throwing error dialogs
	}
	
	IU IOperationsProgressDialog
	{
		iid 0C9FB851-E5C9-43EB-A370-F0677B13874C
		cf StartProgressDialog hwndOwner HWND flags OPPROGDLGF
		cf StopProgressDialog
		cf SetOperation action SPACTION
		cf SetMode mode PDMODE
		cf UpdateProgress ullPointsCurrent ULONGLONG ullPointsTotal ULONGLONG ullSizeCurrent ULONGLONG ullSizeTotal ULONGLONG ullItemsCurrent ULONGLONG ullItemsTotal ULONGLONG
		cf UpdateLocations psiSource P.IShellItem psiTarget P.IShellItem psiItem P.IShellItem
		cf ResetTimer
		cf PauseTimer
		cf ResumeTimer
		cf GetMilliseconds pullElapsed P.ULONGLONG pullRemaining P.ULONGLONG
		cf GetOperationStatus popstatus P.PDOPSTATUS
	}
	
	IU IIOCancelInformation
	{
		iid f5b0bf81-8cb5-4b1b-9449-1a159e0c733c
		cf SetCancelInformation dwThreadID DWORD uMsgCancel UINT
		cf GetCancelInformation pdwThreadID P.DWORD puMsgCancel P.UINT
	}
	
	eq FOFX_NOSKIPJUNCTIONS         0x00010000  // Don't avoid binding to junctions (like Task folder, Recycle-Bin)
	eq FOFX_PREFERHARDLINK          0x00020000  // Create hard link if possible
	eq FOFX_SHOWELEVATIONPROMPT     0x00040000  // Show elevation prompts when error UI is disabled (use with FOF_NOERRORUI)
	eq FOFX_RECYCLEONDELETE         0x00080000  // Recycle when deleting, rather than permanently deleting
	eq FOFX_EARLYFAILURE            0x00100000  // Fail operation as soon as a single error occurs rather than trying to process other items (applies only when using FOF_NOERRORUI)
	eq FOFX_PRESERVEFILEEXTENSIONS  0x00200000  // Rename collisions preserve file extns (use with FOF_RENAMEONCOLLISION)
	eq FOFX_KEEPNEWERFILE           0x00400000  // Keep newer file on naming conflicts
	eq FOFX_NOCOPYHOOKS             0x00800000  // Don't use copy hooks
	eq FOFX_NOMINIMIZEBOX           0x01000000  // Don't allow minimizing the progress dialog
	eq FOFX_MOVEACLSACROSSVOLUMES   0x02000000  // Copy security information when performing a cross-volume move operation
	eq FOFX_DONTDISPLAYSOURCEPATH   0x04000000  // Don't display the path of source file in progress dialog
	eq FOFX_DONTDISPLAYDESTPATH     0x08000000  // Don't display the path of destination file in progress dialog
	eq FOFX_REQUIREELEVATION        0x10000000  // User expects the elevation; don't show a dialog to confirm
	eq FOFX_ADDUNDORECORD           0x20000000  // This is a user-invoked operation, and should be placed on the undo stack.  This flag is preferred to FOF_ALLOWUNDO
	eq FOFX_COPYASDOWNLOAD          0x40000000  // Show Downloading instead of Copying
	eq FOFX_DONTDISPLAYLOCATIONS    0x80000000  // Hides the locations line in the progress dialog
~
	
	IU IFileOperation
	{
		iid 947aab5f-0a5c-4c13-b4d6-4bf7836fc9f8
		cf Advise pfops P.IFileOperationProgressSink pdwCookie P.DWORD
		cf Unadvise dwCookie DWORD
		cf SetOperationFlags dwOperationFlags DWORD
		cf SetProgressMessage pszMessage LPCWSTR
		cf SetProgressDialog popd P.IOperationsProgressDialog
		cf SetProperties pproparray P.IPropertyChangeArray
		cf SetOwnerWindow hwndOwner HWND
		cf ApplyPropertiesToItem psiItem P.IShellItem
		cf ApplyPropertiesToItems punkItems P.IUnknown
		cf RenameItem psiItem P.IShellItem pszNewName LPCWSTR pfopsItem P.IFileOperationProgressSink
		cf RenameItems pUnkItems P.IUnknown pszNewName LPCWSTR
		cf MoveItem psiItem P.IShellItem psiDestinationFolder P.IShellItem pszNewName LPCWSTR pfopsItem P.IFileOperationProgressSink
		cf MoveItems punkItems P.IUnknown psiDestinationFolder P.IShellItem
		cf CopyItem psiItem P.IShellItem psiDestinationFolder P.IShellItem pszCopyName LPCWSTR pfopsItem P.IFileOperationProgressSink
		cf CopyItems punkItems P.IUnknown pfopsItem P.IFileOperationProgressSink
		cf DeleteItem psiItem P.IShellItem pfopsItem P.IFileOperationProgressSink
		cf DeleteItems punkItems P.IUnknown
		cf NewItem psiDestinationFolder P.IShellItem dwFileAttributes DWORD pszName LPCWSTR pszTemplateName LPCWSTR pfopsItem P.IFileOperationProgressSink
		cf PerformOperations
		cf GetAnyOperationsAborted pfAnyOperationsAborted P.BOOL
	}
	
	IU IObjectProvider
	{
		iid a6087428-3be3-4d73-b308-7c04a540bf1af5b0bf81-8cb5-4b1b-9449-1a159e0c733c
		cf QueryObject guidObject R.GUID riid R.IID ppvOut P.PVOID
	}
}

ifver @WIN10
{
	ed FILE_OPERATION_FLAGS2
	{
	    ee FOF2_NONE 0x00000000
		ee FOF2_MERGEFOLDERSONCOLLISION 0x00000001
	}
	
	I IFileOperation2 ex IFileOperation
	{
		iid cd8f23c1-8f61-4916-909d-55bdd0918753
		cf SetOperationFlags2 operationFlags2 FILE_OPERATION_FLAGS2
	}
}

IU INamespaceWalkCB
{
	iid d92995f8-cf5e-4a76-bf59-ead39ea2b97e
	cf FoundItem psf P.IShellFolder pidl P.ITEMID_CHILD
	cf EnterFolder psf P.IShellFolder pidl P.ITEMID_CHILD
	cf LeaveFolder psf P.IShellFolder pidl P.ITEMID_CHILD
	cf InitializeProgressDialog ppszTitle P.LPWSTR ppszCancel P.LPWSTR
}

ifver_ie @IE70
{
	I INamespaceWalkCB2 ex INamespaceWalkCB
	{
		iid 7ac7492b-c38e-438a-87db-68737844ff70
		cf WalkComplete hr HRESULT
	}
}

ed NAMESPACEWALKFLAG
{
	ee NSWF_DEFAULT                        0x00000000
	ee NSWF_NONE_IMPLIES_ALL               0x00000001
	ee NSWF_ONE_IMPLIES_ALL                0x00000002
	ee NSWF_DONT_TRAVERSE_LINKS            0x00000004   // don't traverse the targets of link items (items with SFGAO_LINK)
	ee NSWF_DONT_ACCUMULATE_RESULT         0x00000008   // don't store the results of the walk, GetIDArrayResult() will fail if called

	// for items with both SFGAO_FOLDER and SFGAO_STREAM discovered via the walk
	// (as opposed to those passed as the input) for example .zip, .search-ms and .library-ms files
	// traverse through them and find the items they reference. this will result in
	// EnterFolder()/LeaveFolder() callbacks instead of FoundItem()
	ee NSWF_TRAVERSE_STREAM_JUNCTIONS      0x00000010

	ee NSWF_FILESYSTEM_ONLY                0x00000020   // only return file system items (SFGAO_FILESYSTEM)
	ee NSWF_SHOW_PROGRESS                  0x00000040   // display the progress dialog while walking
	ee NSWF_FLAG_VIEWORDER                 0x00000080   // order the items based on the view order that might be different from the default sort
	ee NSWF_IGNORE_AUTOPLAY_HIDA           0x00000100
	ee NSWF_ASYNC                          0x00000200   // run the walk on a background thread
	ee NSWF_DONT_RESOLVE_LINKS             0x00000400   // avoid the expense of resolving links, means link targets might not be up to date
	ee NSWF_ACCUMULATE_FOLDERS 0x00000800
	ee NSWF_DONT_SORT                      0x00001000   // Don't maintain sort order of items
	ee NSWF_USE_TRANSFER_MEDIUM            0x00002000   // Use SHCONTF_STORAGE in enumerations

	// for items with both SFGAO_FOLDER and SFGAO_STREAM passed to the walk
	// (as opposed to those discovered by walking), for example .zip, .search-ms and .library-ms files
	// do not traverse them, instead treat them as items. this will result in
	// FoundItem() callbacks instead of EnterFolder()/LeaveFolder()
	ee NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS 0x00004000
	ee NSWF_ANY_IMPLIES_ALL                0x00008000   // For selections > 0
}

IU INamespaceWalk
{
	iid 57ced8a7-3f4a-432c-9350-30f24483f74f
	cf Walk punkToWalk P.IUnknown dwFlags DWORD cDepth INT pnswcb P.INamespaceWalkCB
	cf GetIDArrayResult pcItems P.UINT prgpidl P.P.P.ITEMID_CHILD
}

~def FreeIDListArray(ppidls: IDoublePtr[ITEMIDLIST], cItems: int):
~	for i in range(cItems):
~		CoTaskMemFree(ppidls[i])
~	CoTaskMemFree(ppidls)
~
~FreeIDListArrayFull = FreeIDListArrayChild = FreeIDListArray
~

sd BANDSITEINFO
{
	sf IDword dwMask
	sf IDword dwState
	sf IDword dwStyle
}

ed BANDSITECID
{
	ee BSID_BANDADDED
	ee BSID_BANDREMOVED
}

// Field mask
eq BSIM_STATE          0x00000001
eq BSIM_STYLE          0x00000002
~

// State flags
eq BSSF_VISIBLE        0x00000001
eq BSSF_NOTITLE        0x00000002
eq BSSF_UNDELETEABLE   0x00001000
~

// Style flags
eq BSIS_AUTOGRIPPER               0x00000000
eq BSIS_NOGRIPPER                 0x00000001
eq BSIS_ALWAYSGRIPPER             0x00000002
eq BSIS_LEFTALIGN                 0x00000004
eq BSIS_SINGLECLICK               0x00000008
eq BSIS_NOCONTEXTMENU             0x00000010
eq BSIS_NODROPTARGET              0x00000020
eq BSIS_NOCAPTION                 0x00000040
eq BSIS_PREFERNOLINEBREAK         0x00000080
eq BSIS_LOCKED                    0x00000100
ifver_ie @IE70
{
	eq BSIS_PRESERVEORDERDURINGLAYOUT 0x00000200
	eq BSIS_FIXEDORDER                0x00000400
}
~

IU IBandSite
{
	iid 4CF504B0-DE96-11D0-8B3F-00A0C911E8E5
	cf AddBand punk P.IUnknown
	cf EnumBands uBand UINT pdwBandID P.DWORD
	cf QueryBand dwBandID DWORD ppstb P.P.IDeskBand pdwState P.DWORD pszName LPWSTR cchName INT
	cf SetBandState dwBandID DWORD dwMask DWORD dwState DWORD
	cf RemoveBand dwBandID DWORD
	cf GetBandObject dwBandID DWORD riid R.IID ppv P.PVOID
	cf SetBandSiteInfo pbsinfo P.BANDSITEINFO
	cf GetBandSiteInfo pbsinfo P.BANDSITEINFO
}

eq SID_SBandSite IBandSite._iid_
eq CGID_BandSite IBandSite._iid_

IU IModalWindow
{
	iid b4db1657-70d7-485e-8e3e-6fcb5a5c1802
	cf Show hwndOwner HWND
}

IU IContextMenuSite
{
	iid 0811AEBE-0B87-4C54-9E72-548CF649016B
	cf DoContextMenuPopup punkContextMenu P.IUnknown fFlags UINT pt POINT
}

ed MENUBANDHANDLERCID
{
	ee MBHANDCID_PIDLSELECT 0
}

IU IMenuBand
{
	iid 568804CD-CBD7-11d0-9816-00C04FD91972
	cf IsMenuMessage pmsg P.MSG
	cf TranslateMenuMessage pmsg P.MSG plRet P.LRESULT
}

IU IRegTreeItem
{
	iid A9521922-0812-4d44-9EC3-7FD38C726F3D
	cf GetCheckState pbCheck P.BOOL
	cf SetCheckState bCheck BOOL
}

I IDeskBar ex IOleWindow
{
	iid EB0FE173-1A3A-11D0-89B3-00A0C90A90AC
	cf SetClient punkClient P.IUnknown
	cf GetClient ppunkClient P.P.IUnknown
	cf OnPosRecChangeDB prc P.RECT
}

ed MENUPOPUPSELECT
{
	ee MPOS_EXECUTE 0           // Execute the selected menu item
	ee MPOS_FULLCANCEL            // Cancel the entire menu
	ee MPOS_CANCELLEVEL           // Cancel the current cascaded menu
	ee MPOS_SELECTLEFT            // select one to the left of the cur selection
	ee MPOS_SELECTRIGHT           // select one to the right of the cur selection
	ee MPOS_CHILDTRACKING          // the child got a tracking select (mouse moved over)
}

ed MP_POPUPFLAGS
{
	ee MPPF_SETFOCUS 0x00000001    // Menu can take the focus
	ee MPPF_INITIALSELECT 0x00000002    // Select the first item
	ee MPPF_NOANIMATE 0x00000004    // Do not animate this show
	ee MPPF_KEYBOARD 0x00000010    // The menu is activated by keyboard
	ee MPPF_REPOSITION 0x00000020    // Resposition the displayed bar.
	ee MPPF_FORCEZORDER 0x00000040    // internal: Tells menubar to ignore Submenu positions
	ee MPPF_FINALSELECT 0x00000080    // Select the last item
	ee MPPF_TOP 0x20000000    // Popup menu up from point
	ee MPPF_LEFT 0x40000000    // Popup menu left from point
	ee MPPF_RIGHT 0x60000000    // Popup menu right from point
	ee MPPF_BOTTOM 0x80000000 // Popup menu below point
	ee MPPF_POS_MASK 0xE0000000 // Menu Position Mask
	ee MPPF_ALIGN_LEFT 0x02000000    // Default alignment
	ee MPPF_ALIGN_RIGHT 0x04000000     // Popup menu aligned to right of exclude rect
}

I IMenuPopup ex IDeskBar
{
	iid D1E7AFEB-6A2E-11d0-8C78-00C04FD918B4
	cf Popup ppt P.POINTL prcExclude P.RECTL dwFlags MP_POPUPFLAGS
	cf OnSelect dwSelectType DWORD
	cf SetSubMenu pmp FD.P.IMenuPopup fSet BOOL
}

ed FILE_USAGE_TYPE
{
	ee FUT_PLAYING 0
	ee FUT_EDITING
	ee FUT_GENERIC
}

eq OF_CAP_CANSWITCHTO 0x0001
eq OF_CAP_CANCLOSE 0x0002
~

IU IFileIsInUse
{
	iid 64a1cbf0-3a1a-4461-9158-376969693950
	cf GetAppName ppszName P.LPWSTR
	cf GetUsage pfut P.FILE_USAGE_TYPE
	cf GetCapabilities pdwCapFlags P.DWORD
	cf GetSwitchToHWND phwnd P.HWND
	cf CloseFile
}



// to be continued
// uncompleted