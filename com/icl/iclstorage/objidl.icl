.icl
.ver 100
.inc ptrs.icl

////////////////////////////////////
// ICL (Interface Contract Language)
// ObjIdl.icl - Partial Declaration
// Declaring tail of ObjIdl.idl
////////////////////////////////////

// forward pointer declarations for readability
pie FORMATETC LPFORMATETC
pie STGMEDIUM LPSTGMEDIUM
pie IAdviseSink LPADVISESINK
pie IEnumSTATDATA LPENUMSTATDATA
pie IEnumFORMATETC LPENUMFORMATETC
pie ILockBytes LPLOCKBYTES
pie IBindCtx LPBINDCTX
pie IStorage LPSTORAGE

// forward declaring of aliases, internally in generator
al int INT64 UINT64 HRESULT

I IMessageFilter ex IUnknown
{
	iid 00000016-0000-0000-C000-000000000046
	vf HandleInComingCall DWORD dwCallType DWORD htaskCaller HTASK dwTickCount DWORD lpInterfaceInfo P.INTERFACEINFO
	vf RetryRejectedCall DWORD htaskCallee HTASK dwTickCount DWORD dwRejectType DWORD
	vf MessagePending DWORD htaskCallee HTASK dwTickCount DWORD dwPendingType DWORD
}

pi LPMESSAGEFILTER

I IClassActivator ex IUnknown
{
	iid 00000140-0000-0000-C000-000000000046
	cf GetClassObject rclsid R.CLSID dwClassContext DWORD locale LCID riid R.IID ppv P.PVOID
}

I IFillLockBytes ex IUnknown
{
	iid 99caf010-415e-11cf-8814-00aa00b569f5
	cf FillAppend pv LPCVOID cb ULONG pcbWritten PULONG
	cf FillAt ulOffset ULARGE_INTEGER pv LPCVOID cb ULONG pcbWritten PULONG
	cf SetFillSize ulSize ULARGE_INTEGER
	cf Terminate bCanceled BOOL
}

I IProgressNotify ex IUnknown
{
	iid a9d758a0-4617-11cf-95fc-00aa00680db4
	cf OnProgress dwProgressCurrent DWORD dwProgressMaximum DWORD fAccurate BOOL fOwner BOOL
}

// StorageLayout placeholder
sd StorageLayout

I ILayoutStorage ex IUnknown
{
	iid 0e6d4d90-6738-11cf-9608-00aa00680db4
	cf LayoutScript pStorageLayout P.StorageLayout nEntries DWORD glfInterleavedFlag DWORD
	cf BeginMonitor
	cf EndMonitor
	cf ReLayoutDocfile pwcsNewDfName LPOLESTR
	cf ReLayoutDocfileOnILockBytes pILockBytes P.ILockBytes
}

I IBlockingLock ex IUnknown
{
	iid 30f3d47a-6447-11d1-8e3c-00c04fb9386d
	cf Lock dwTimeout DWORD
	cf Unlock
}

I ITimeAndNoticeControl ex IUnknown
{
	iid bc0bf6ae-8878-11d1-83e9-00c04fc2c6d4
	cf SuppressChanges res1 DWORD res2 DWORD
}

I IOplockStorage ex IUnknown
{
	iid 8d19c834-8879-11d1-83e9-00c04fc2c6d4
	cf CreateStorageEx pwcsName LPCWSTR grfMode DWORD stgfmt DWORD grfAttrs DWORD riid R.IID ppstgOpen P.PVOID
	cf OpenStorageEx pwcsName LPCWSTR grfMode DWORD stgfmt DWORD grfAttrs DWORD riid R.IID ppstgOpen P.PVOID
}

I IDirectWriterLock ex IUnknown
{
	iid 0e6d4d92-6738-11cf-9608-00aa00680db4
	cf WaitForWriteAccess dwTimeout DWORD
	cf ReleaseWriteAccess
	cf HaveWriteAccess
}

I IUrlMon ex IUnknown
{
	iid 00000026-0000-0000-C000-000000000046
	cf AsyncGetClassBits rclsid R.CLSID pszType LPCWSTR pszExt LPCWSTR dwFileVersionMS DWORD dwFileVersionLS DWORD pszCodeBase LPCWSTR pbc P.IBindCtx dwClassContext DWORD riid R.IID flags DWORD
}

I IForegroundTransfer ex IUnknown
{
	iid 00000145-0000-0000-C000-000000000046
	cf AllowForegroundTransfer lpvReserved PVOID
}

I IThumbnailExtractor ex IUnknown
{
	iid 969dc708-5c76-11d1-8d86-0000f804b057
	cf ExtractThumbnail pStg P.IStorage ulLength ULONG ulHeight ULONG pulOutputLength PULONG pulOutputHeight PULONG phOutputBitmap P.HBITMAP
	cf OnFileUpdated pStg P.IStorage
}

I IDummyHICONIncluder ex IUnknown
{
	iid 947990de-cc28-11d2-a0f7-00805f858fb1
	cf Dummy h1 HICON h2 HDC
}

// Placeholder for enums
ed ApplicationType
ed ShutdownType

I IProcessLock ex IUnknown
{
	iid 000001d5-0000-0000-C000-000000000046
	vf AddRefOnProcess ULONG
	vf ReleaseRefOnProcess ULONG
}

I ISurrogateService ex IUnknown
{
	iid 000001d4-0000-0000-C000-000000000046
	cf Init rguidProcessID R.GUID pProcessLock P.IProcessLock pfApplicationAware PBOOL
	cf ApplicationLaunch rguidApplID R.GUID appType ApplicationType
	cf ApplicationFree rguidApplID R.GUID
	cf CatalogRefresh ulReserved ULONG
	cf ProcessShutdown ulReserved ULONG
}

I IInitializeSpy ex IUnknown
{
	iid 00000034-0000-0000-C000-000000000046
	cf PreInitialize dwCoInit DWORD dwCurThreadAptRefs DWORD
	cf PostInitialize hrCoInit HRESULT dwCoInit DWORD dwNewThreadAptRefs DWORD
	cf PreUninitialize dwCurThreadAptRefs DWORD
	cf PostUninitialize dwNewThreadAptRefs DWORD
}

pi LPINITIALIZESPY

I IApartmentShutdown ex IUnknown
{
	iid A2F05A09-27A2-42B5-BC0E-AC163EF49D9B
	cf OnUninitialize ui64ApartmentIdentifier UINT64
}

