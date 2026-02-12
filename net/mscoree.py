#
# mscoree.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sun Feb  8 15:04:19 2026
# Generated from ICL: mscoree.icl
#

from ..processthreadsapi import *
from ..minwinbase import *

from ..com.autointerfacedef import *
from ..com.bstr import *

from .gchost import *
from .ivalidator import *

mscoree = get_win_library('mscoree.dll')

CLR_MAJOR_VERSION = 4
CLR_MINOR_VERSION = 0
CLR_BUILD_VERSION = 30319
CLR_ASSEMBLY_MAJOR_VERSION = 4
CLR_ASSEMBLY_MINOR_VERSION = 0
CLR_ASSEMBLY_BUILD_VERSION = 0

LIBID_mscoree = CLSID('{5477469e-83b1-11d2-8b49-00a0c9b7c9c4}')
CLSID_CorRuntimeHost = CLSID('{cb2f6723-ab3a-11d2-9c40-00c04fa30a3e}')
CLSID_TypeNameFactory = CLSID('{B81FF171-20F3-11d2-8dcc-00a0c9b00525}')
CLSID_CLRRuntimeHost = CLSID('{90F1A06E-7712-4762-86B5-7A5EBA6BDB02}')
CLSID_ComCallUnmarshal = CLSID('{3F281000-E95A-11d2-886B-00C04F869F04}')
CLSID_ComCallUnmarshalV4 = CLSID('{45fb4600-e6e8-4928-b25e-50476ff79425}')
IID_IObjectHandle = IID('{c460e2b4-e199-412a-8456-84dc3e4838c3}')
IID_IManagedObject = IID('{c3fcc19e-a970-11d2-8b5a-00a0c9b7c9c4}')
IID_IApartmentCallback = IID('{178e5337-1528-4591-b1c9-1c6e484686d8}')
IID_ICatalogServices = IID('{04c6be1e-1db1-4058-ab7a-700cccfbf254}')
IID_ICorRuntimeHost = IID('{cb2f6722-ab3a-11d2-9c40-00c04fa30a3e}')
IID_ICorThreadpool = IID('{84680D3A-B2C1-46e8-ACC2-DBC0A359159A}')
IID_ICLRDebugManager = IID('{00dcaec6-2ac0-43a9-acf9-1e36c139b10d}')
IID_IHostMemoryNeededCallback = IID('{47EB8E57-0846-4546-AF76-6F42FCFC2649}')
IID_IHostMalloc = IID('{1831991C-CC53-4A31-B218-04E910446479}')
IID_IHostMemoryManager = IID('{7BC698D1-F9E3-4460-9CDE-D04248E9FA25}')
IID_ICLRTask = IID('{28E66A4A-9906-4225-B231-9187c3eb8611}')
IID_ICLRTask2 = IID('{28E66A4A-9906-4225-B231-9187c3eb8612}')
IID_IHostTask = IID('{C2275828-C4B1-4B55-82C9-92135F74DF1A}')
IID_ICLRTaskManager = IID('{4862efbe-3ae5-44f8-8FEB-346190eE8A34}')
IID_IHostTaskManager = IID('{997FF24C-43B7-4352-8667-0DC04FAFD354}')
IID_IHostThreadpoolManager = IID('{983D50E2-CB15-466B-80FC-845DC6E8C5FD}')
IID_ICLRIoCompletionManager = IID('{2D74CE86-B8D6-4C84-B3A7-9768933B3C12}')
IID_IHostIoCompletionManager = IID('{8BDE9D80-EC06-41D6-83E6-22580EFFCC20}')
IID_IHostSyncManager = IID('{234330c7-5f10-4f20-9615-5122dab7a0ac}')
IID_IHostCrst = IID('{6DF710A6-26A4-4a65-8cd5-7237b8bda8dc}')
IID_IHostAutoEvent = IID('{50B0CFCE-4063-4278-9673-e5cb4ed0bdb8}')
IID_IHostManualEvent = IID('{1BF4EC38-AFFE-4fb9-85a6-525268f15b54}')
IID_IHostSemaphore = IID('{855efd47-cc09-463a-a97d-16acab882661}')
IID_ICLRSyncManager = IID('{55FF199D-AD21-48f9-a16c-f24ebbb8727d}')
IID_ICLRAppDomainResourceMonitor = IID('{C62DE18C-2E23-4AEA-8423-B40C1FC59EAE}')
IID_ICLRPolicyManager = IID('{7D290010-D781-45da-A6F8-AA5D711A730E}')
IID_ICLRGCManager = IID('{54D9007E-A8E2-4885-B7BF-F998DEEE4F2A}')
IID_ICLRGCManager2 = IID('{0603B793-A97A-4712-9CB4-0CD1C74C0F7C}')
IID_ICLRErrorReportingManager = IID('{980d2f1a-bf79-4c08-812a-bb9778928f78}')
IID_IHostPolicyManager = IID('{7AE49844-B1E3-4683-BA7C-1E8212EA3B79}')
IID_IHostGCManager = IID('{5D4EC34E-F248-457B-B603-255FAABA0D21}')
IID_IActionOnCLREvent = IID('{607BE24B-D91B-4E28-A242-61871CE56E35}')
IID_ICLROnEventManager = IID('{1D0E0132-E64F-493D-9260-025C0E32C175}')
IID_ICLRRuntimeHost = IID('{90F1A06C-7712-4762-86B5-7A5EBA6BDB02}')
IID_ICLRHostProtectionManager = IID('{89f25f5c-ceef-43e1-9cfa-a68ce863aaac}')
IID_IHostAssemblyStore = IID('{7b102a88-3f7f-496d-8fa2-c35374e01af3}')
IID_IHostAssemblyManager = IID('{613dabd7-62b2-493e-9e65-c1e32a1e0c5e}')
IID_IHostSecurityManager = IID('{75ad2468-a349-4d02-a764-76a68aee0c4f}')
IID_IHostSecurityContext = IID('{7e573ce4-0343-4423-98d7-6318348a1d3c}')
IID_ICLRAssemblyIdentityManager = IID('{15f0a9da-3ff6-4393-9da9-fdfd284e6972}')
IID_ICLRDomainManager = IID('{270d00a2-8e15-4d0b-adeb-37bc3e47df77}')
IID_ITypeName = IID('{B81FF171-20F3-11d2-8dcc-00a0c9b00522}')
IID_ICLRAssemblyReferenceList = IID('{1b2c9750-2e66-4bda-8b44-0a642c5cd733}')
IID_ICLRReferenceAssemblyEnum = IID('{d509cb5d-cf32-4876-ae61-67770cf91973}')
IID_ICLRProbingAssemblyEnum = IID('{d0c5fb1f-416b-4f97-81f4-7ac7dc24dd5d}')
IID_ICLRHostBindingPolicyManager = IID('{4b3545e7-1856-48c9-a8ba-24b21a753c09}')
IID_ITypeNameBuilder = IID('{B81FF171-20F3-11d2-8dcc-00a0c9b00523}')
IID_ITypeNameFactory = IID('{B81FF171-20F3-11d2-8dcc-00a0c9b00521}')

@mscoree.foreign(HRESULT, LPWSTR, DWORD, PDWORD)
def GetCORSystemDirectory(pbuffer: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

@mscoree.foreign(HRESULT, LPWSTR, DWORD, PDWORD)
def GetCORVersion(pbBuffer: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

@mscoree.foreign(HRESULT, LPCWSTR, LPWSTR, DWORD, PDWORD)
def GetFileVersion(szFilename: LPCWSTR, szBuffer: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

@mscoree.foreign(HRESULT, LPWSTR, DWORD, PDWORD)
def GetCORRequiredVersion(pbuffer: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

@mscoree.foreign(HRESULT, LPCWSTR, LPCWSTR, LPCWSTR, DWORD, DWORD, LPWSTR, DWORD, PDWORD, LPWSTR, DWORD, DWORD)
def GetRequestedRuntimeInfo(pExe: LPCWSTR, pwszVersion: LPCWSTR, pConfigurationFile: LPCWSTR, startupFlags: int, runtimeInfoFlags: int, pDirectory: LPWSTR, dwDirectory: int, dwDirectoryLength: PDWORD, pVersion: LPWSTR, cchBuffer: int, dwlength: int) -> int: ...

@mscoree.foreign(HRESULT, LPWSTR, LPWSTR, DWORD, PDWORD)
def GetRequestedRuntimeVersion(pExe: LPWSTR, pVersion: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

@mscoree.foreign(HRESULT, LPCWSTR, LPCWSTR, LPCWSTR, PVOID, DWORD, LPCLSID, LPIID, PVOID, PVOID, intermediate_method = True)
def CorBindToRuntimeHost(pwszVersion: LPCWSTR, pwszBuildFlavor: LPCWSTR, pwszHostConfigFile: LPCWSTR, pReserved: PVOID, startupFlags: int, clsid: CLSID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(pwszVersion, pwszBuildFlavor, pwszHostConfigFile, pReserved, startupFlags, clsid.ref(), iid.ref(), ppv)

@mscoree.foreign(HRESULT, LPCWSTR, LPCWSTR, DWORD, LPCLSID, LPIID, PVOID, PVOID, intermediate_method = True)
def CorBindToRuntimeEx(pwszVersion: LPCWSTR, pwszBuildFlavor: LPCWSTR, startupFlags: int, clsid: CLSID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(pwszVersion, pwszBuildFlavor, startupFlags, clsid.ref(), iid.ref(), ppv)

@mscoree.foreign(HRESULT, LPSTREAM, DWORD, DWORD, LPCLSID, LPIID, PVOID, PVOID, intermediate_method = True)
def CorBindToRuntimeByCfg(pCfgStream: IPointer[IStream], reserved: int, startupFlags: int, clsid: CLSID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(pCfgStream, reserved, startupFlags, clsid.ref(), iid.ref(), ppv)

@mscoree.foreign(HRESULT, LPCWSTR, LPCWSTR, LPCLSID, LPIID, PVOID, PVOID, intermediate_method = True)
def CorBindToRuntime(pwszVersion: LPCWSTR, pwszBuildFlavor: LPCWSTR, clsid: CLSID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(pwszVersion, pwszBuildFlavor, clsid.ref(), iid.ref(), ppv)

@mscoree.foreign(HRESULT, LPCWSTR, LPCLSID, LPIID, PVOID, PVOID, intermediate_method = True)
def CorBindToCurrentRuntime(pwszFileName: LPCWSTR, clsid: CLSID, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(pwszFileName, clsid.ref(), iid.ref(), ppv)

@mscoree.foreign(HRESULT, LPCWSTR, LPIID, PVOID, PVOID, intermediate_method = True)
def ClrCreateManagedInstance(pTypeName: LPCWSTR, iid: IID, ppObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(pTypeName, iid.ref(), ppObject)

@mscoree.foreign(VOID)
def CorMarkThreadInThreadPool(): ...

@mscoree.foreign(HRESULT, HWND, HINSTANCE, LPCWSTR, INT)
def RunDll32ShimW(hwnd: HWND, hinst: HINSTANCE, lpszCmdLine: LPCWSTR, nCmdShow: int) -> int: ...

@mscoree.foreign(HRESULT, LPCWSTR, LPCWSTR, PVOID, PTR(HMODULE))
def LoadLibraryShim(szDllName: LPCWSTR, szVersion: LPCWSTR, pvReserved: PVOID, phModDll: IPointer[HMODULE]) -> int: ...

@mscoree.foreign(HRESULT, LPCWSTR, LPCSTR, PVOID, PVOID, LPCWSTR, PVOID)
def CallFunctionShim(szDllName: LPCWSTR, szFunctionName: LPCSTR, lpvArgument1: PVOID, lpvArgument2: PVOID, szVersion: LPCWSTR, pvReserved: PVOID) -> int: ...

@mscoree.foreign(HRESULT, LPSTR, PVOID, PVOID)
def GetRealProcAddress(pwszProcName: LPSTR, ppv: IPointer[PVOID]) -> int: ...

@mscoree.foreign(VOID, INT)
def CorExitProcess(exitCode: int): ...

@mscoree.foreign(HRESULT, UINT, LPWSTR, INT, INT)
def LoadStringRC(iResouceID: int, szBuffer: LPWSTR, iMax: int, bQuiet: int) -> int: ...

@mscoree.foreign(HRESULT, LCID, UINT, LPWSTR, INT, INT, PINT)
def LoadStringRCEx(lcid: int, iResouceID: int, szBuffer: LPWSTR, iMax: int, bQuiet: int, pcwchUsed: PINT) -> int: ...

FLockClrVersionCallback = WINAPI(HRESULT)

@mscoree.foreign(HRESULT, FLockClrVersionCallback, PVOID, PVOID)
def LockClrVersion(hostCallback: FARPROC, pBeginHostSetup: PVOID, pEndHostSetup: PVOID) -> int: ...

@mscoree.foreign(HRESULT, INT, LPCWSTR, PTR(LPUNKNOWN))
def CreateDebuggingInterfaceFromVersion(iDebuggerVersion: int, szDebuggeeVersion: LPCWSTR, ppCordb: IDoublePtr[IUnknown]) -> int: ...

@mscoree.foreign(HRESULT, HANDLE, LPWSTR, DWORD, PDWORD)
def GetVersionFromProcess(hProcess: HANDLE, pVersion: LPWSTR, cchBuffer: int, dwLength: PDWORD) -> int: ...

HOST_TYPE_DEFAULT = 0
HOST_TYPE_APPLAUNCH = 1
HOST_TYPE_CORFLAG = 2
HOST_TYPE = INT

@mscoree.foreign(HRESULT, HOST_TYPE, LPCWSTR, DWORD, PTR(LPCWSTR), DWORD, PTR(LPCWSTR), LPPROCESS_INFORMATION)
def CorLaunchApplication(dwClickOnceHost: int, pwzAppFullName: LPCWSTR, dwManifestPaths: int, ppwzManifestPaths: IPointer[LPCWSTR], dwActivationData: int, ppwzActivationData: IPointer[LPCWSTR], lpProcessInformation: IPointer[PROCESS_INFORMATION]) -> int: ...

FExecuteInAppDomainCallback = WINAPI(HRESULT, PVOID)

STARTUP_CONCURRENT_GC = 0x1
STARTUP_LOADER_OPTIMIZATION_MASK = ( 0x3 << 1 )
STARTUP_LOADER_OPTIMIZATION_SINGLE_DOMAIN = ( 0x1 << 1 )
STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN = ( 0x2 << 1 )
STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST = ( 0x3 << 1 )
STARTUP_LOADER_SAFEMODE = 0x10
STARTUP_LOADER_SETPREFERENCE = 0x100
STARTUP_SERVER_GC = 0x1000
STARTUP_HOARD_GC_VM = 0x2000
STARTUP_SINGLE_VERSION_HOSTING_INTERFACE = 0x4000
STARTUP_LEGACY_IMPERSONATION = 0x10000
STARTUP_DISABLE_COMMITTHREADSTACK = 0x20000
STARTUP_ALWAYSFLOW_IMPERSONATION = 0x40000
STARTUP_TRIM_GC_COMMIT = 0x80000
STARTUP_ETW = 0x100000
STARTUP_ARM = 0x400000
STARTUP_FLAGS = INT

CLSID_RESOLUTION_DEFAULT = 0
CLSID_RESOLUTION_REGISTERED = 1
CLSID_RESOLUTION_FLAGS = INT

RUNTIME_INFO_UPGRADE_VERSION = 1
RUNTIME_INFO_REQUEST_IA64 = 2
RUNTIME_INFO_REQUEST_AMD64 = 4
RUNTIME_INFO_REQUEST_X86 = 8
RUNTIME_INFO_DONT_RETURN_DIRECTORY = 16
RUNTIME_INFO_DONT_RETURN_VERSION = 32
RUNTIME_INFO_DONT_SHOW_ERROR_DIALOG = 64
RUNTIME_INFO_IGNORE_ERROR_MODE = 4096
RUNTIME_INFO_FLAGS = INT

APPDOMAIN_SECURITY_DEFAULT = 0
APPDOMAIN_SECURITY_SANDBOXED = 1
APPDOMAIN_SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE = 2
APPDOMAIN_FORCE_TRIVIAL_WAIT_OPERATIONS = 8
APPDOMAIN_SECURITY_FLAGS = INT

@mscoree.foreign(HRESULT, LPCLSID, LPWSTR, DWORD, PDWORD, CLSID_RESOLUTION_FLAGS, intermediate_method = True)
def GetRequestedRuntimeVersionForCLSID(clsid: CLSID, pVersion: LPWSTR, cchBuffer: int, dwLength: PDWORD, dwResolutionFlags: int, **kwargs) -> int:
    return delegate(clsid.ref(), pVersion, cchBuffer, dwLength, dwResolutionFlags)

class IObjectHandle(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{C460E2B4-E199-412a-8456-84DC3E4838C3}")

    @virtual_table.com_function(LPVARIANT)
    def Unwrap(self, ppv: IPointer[VARIANT]) -> int: ...

    virtual_table.build()

class IAppDomainBinding(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{5C2B07A7-1E98-11d3-872F-00C04F79ED0D}")

    @virtual_table.com_function(LPUNKNOWN)
    def OnAppDomain(self, pAppdomain: IPointer[IUnknown]) -> int: ...

    virtual_table.build()

class IGCThreadControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{F31D1788-C397-4725-87A5-6AF3472C2791}")

    @virtual_table.com_function
    def ThreadIsBlockingForSuspension(self) -> int: ...

    @virtual_table.com_function
    def SuspensionStarting(self) -> int: ...

    @virtual_table.com_function(DWORD)
    def SuspensionEnding(self, Generation: int) -> int: ...

    virtual_table.build()

class IGCHostControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{5513D564-8374-4cb9-AED9-0083F4160A1D}")

    @virtual_table.com_function(SIZE_T, PSIZE_T)
    def RequestVirtualMemLimit(self, sztMaxVirtualMemMB: int, psztNewMaxVirtualMemMB: IPointer[SIZE_T]) -> int: ...

    virtual_table.build()

PTLS_CALLBACK_FUNCTION = WINAPI(VOID, PVOID)

class ICorThreadpool(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{84680D3A-B2C1-46e8-ACC2-DBC0A359159A}")

    @virtual_table.com_function(PHANDLE, HANDLE, WAITORTIMERCALLBACK, PVOID, ULONG, BOOL, PBOOL)
    def CorRegisterWaitForSingleObject(self, phNewWaitObject: IPointer[HANDLE], hWaitObject: HANDLE, Callback: WAITORTIMERCALLBACK, Context: PVOID, timeout: int, executeOnlyOnce: bool, result: PBOOL) -> int: ...

    @virtual_table.com_function(HANDLE, HANDLE, PBOOL)
    def CorUnregisterWait(self, hWaitObject: HANDLE, CompletionEvent: HANDLE, result: PBOOL) -> int: ...

    @virtual_table.com_function(LPTHREAD_START_ROUTINE, PVOID, BOOL, PBOOL)
    def CorQueueUserWorkItem(self, Function: FARPROC, Context: PVOID, executeOnlyOnce: bool, result: PBOOL) -> int: ...

    @virtual_table.com_function(PHANDLE, WAITORTIMERCALLBACK, PVOID, DWORD, DWORD, PBOOL)
    def CorCreateTimer(self, phNewTimer: IPointer[HANDLE], Callback: WAITORTIMERCALLBACK, Parameter: PVOID, DueTime: int, Period: int, result: PBOOL) -> int: ...

    @virtual_table.com_function(HANDLE, ULONG, ULONG, PBOOL)
    def CorChangeTimer(self, Timer: HANDLE, DueTime: int, Period: int, result: PBOOL) -> int: ...

    @virtual_table.com_function(HANDLE, HANDLE, PBOOL)
    def CorDeleteTimer(self, Timer: HANDLE, CompletionEvent: HANDLE, result: PBOOL) -> int: ...

    @virtual_table.com_function(HANDLE, LPOVERLAPPED_COMPLETION_ROUTINE)
    def CorBindIoCompletionCallback(self, fileHandle: HANDLE, callback: FARPROC) -> int: ...

    @virtual_table.com_function(LPTHREAD_START_ROUTINE, PVOID, PBOOL)
    def CorCallOrQueueUserWorkItem(self, Function: FARPROC, Context: PVOID, result: PBOOL) -> int: ...

    @virtual_table.com_function(DWORD, DWORD)
    def CorSetMaxThreads(self, MaxWorkerThreads: int, MaxIOCompletionThreads: int) -> int: ...

    @virtual_table.com_function(PDWORD, PDWORD)
    def CorGetMaxThreads(self, MaxWorkerThreads: PDWORD, MaxIOCompletionThreads: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD, PDWORD)
    def CorGetAvailableThreads(self, AvailableWorkerThreads: PDWORD, AvailableIOCompletionThreads: PDWORD) -> int: ...

    virtual_table.build()

class IDebuggerThreadControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{23D86786-0BB5-4774-8FB5-E3522ADD6246}")

    @virtual_table.com_function
    def ThreadIsBlockingForDebugger(self) -> int: ...

    @virtual_table.com_function
    def ReleaseAllRuntimeThreads(self) -> int: ...

    @virtual_table.com_function(DWORD)
    def StartBlockingForDebugger(self, dwUnused: int) -> int: ...

    virtual_table.build()

class IDebuggerInfo(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{BF24142D-A47D-4d24-A66D-8C2141944E44}")

    @virtual_table.com_function(PBOOL)
    def IsDebuggerAttached(self, pbAttached: PBOOL) -> int: ...

    virtual_table.build()

class ICorConfiguration(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)

    @virtual_table.com_function(PTR(IGCThreadControl))
    def SetGCThreadControl(self, pGCThreadControl: IPointer[IGCThreadControl]) -> int: ...

    @virtual_table.com_function(PTR(IGCHostControl))
    def SetGCHostControl(self, pGCHostControl: IPointer[IGCHostControl]) -> int: ...

    @virtual_table.com_function(PTR(IDebuggerThreadControl))
    def SetDebuggerThreadControl(self, pDebuggerThreadControl: IPointer[IDebuggerThreadControl]) -> int: ...

    @virtual_table.com_function(DWORD)
    def AddDebuggerSpecialThread(self, dwSpecialThreadId: int) -> int: ...

    virtual_table.build()

HDOMAINENUM = PVOID

class ICorRuntimeHost(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{CB2F6722-AB3A-11d2-9C40-00C04FA30A3E}")

    @virtual_table.com_function
    def CreateLogicalThreadState(self) -> int: ...

    @virtual_table.com_function
    def DeleteLogicalThreadState(self) -> int: ...

    @virtual_table.com_function(PDWORD)
    def SwitchInLogicalThreadState(self, pFiberCookie: PDWORD) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(DWORD))
    def SwitchOutLogicalThreadState(self, pFiberCookie: IDoublePtr[DWORD]) -> int: ...

    @virtual_table.com_function(PDWORD)
    def LocksHeldByLogicalThread(self, pCount: PDWORD) -> int: ...

    @virtual_table.com_function(HANDLE, PTR(HMODULE))
    def MapFile(self, hFile: HANDLE, hMapAddress: IPointer[HMODULE]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ICorConfiguration))
    def GetConfiguration(self, pConfiguration: IDoublePtr[ICorConfiguration]) -> int: ...

    @virtual_table.com_function
    def Start(self) -> int: ...

    @virtual_table.com_function
    def Stop(self) -> int: ...

    @virtual_table.com_function(LPCWSTR, LPUNKNOWN, PTR(LPUNKNOWN))
    def CreateDomain(self, pwzFriendlyName: LPCWSTR, pIdentityArray: IPointer[IUnknown], pAppDomain: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def GetDefaultDomain(self, pAppDomain: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(HDOMAINENUM))
    def EnumDomains(self, hEnum: IPointer[HDOMAINENUM]) -> int: ...

    @virtual_table.com_function(HDOMAINENUM, PTR(LPUNKNOWN))
    def NextDomain(self, hEnum: HDOMAINENUM, pAppDomain: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(HDOMAINENUM)
    def CloseEnum(self, hEnum: HDOMAINENUM) -> int: ...

    @virtual_table.com_function(LPCWSTR, LPUNKNOWN, LPUNKNOWN, PTR(LPUNKNOWN))
    def CreateDomainEx(self, pwzFriendlyName: LPCWSTR, pSetup: IPointer[IUnknown], pEvidence: IPointer[IUnknown], pAppDomain: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def CreateDomainSetup(self, pAppDomainSetup: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def CreateEvidence(self, pEvidence: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def UnloadDomain(self, pAppDomain: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(PTR(LPUNKNOWN))
    def CurrentDomain(self, pAppDomain: IDoublePtr[IUnknown]) -> int: ...

    virtual_table.build()

eMemoryAvailableLow = 1
eMemoryAvailableNeutral = 2
eMemoryAvailableHigh = 3
EMemoryAvailable = INT

eTaskCritical = 0
eAppDomainCritical = 1
eProcessCritical = 2
EMemoryCriticalLevel = INT

WAIT_MSGPUMP = 1
WAIT_ALERTABLE = 2
WAIT_NOTINDEADLOCK = 4
WAIT_OPTION = INT

class ICLRMemoryNotificationCallback(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{47EB8E57-0846-4546-AF76-6F42FCFC2649}")

    @virtual_table.com_function(EMemoryAvailable)
    def OnMemoryNotification(self, eMemoryAvailable: int) -> int: ...

    virtual_table.build()

class IHostMalloc(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1831991C-CC53-4A31-B218-04E910446479}")

    @virtual_table.com_function(SIZE_T, EMemoryCriticalLevel, PVOID, PVOID)
    def Alloc(self, cbSize: int, eCriticalLevel: int, ppMem: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(SIZE_T, EMemoryCriticalLevel, LPSTR, INT, PVOID, PVOID)
    def DebugAlloc(self, cbSize: int, eCriticalLevel: int, pszFileName: LPSTR, iLineNo: int, ppMem: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(PVOID)
    def Free(self, pMem: PVOID) -> int: ...

    virtual_table.build()

MALLOC_THREADSAFE = 1
MALLOC_EXECUTABLE = 2
MALLOC_TYPE = INT

class IHostMemoryManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7BC698D1-F9E3-4460-9CDE-D04248E9FA25}")

    @virtual_table.com_function(DWORD, DOUBLE_PTR(IHostMalloc))
    def CreateMalloc(self, dwMallocType: int, ppMalloc: IDoublePtr[IHostMalloc]) -> int: ...

    @virtual_table.com_function(PVOID, SIZE_T, DWORD, DWORD, EMemoryCriticalLevel, PVOID, PVOID)
    def VirtualAlloc(self, pAddress: PVOID, dwSize: int, flAllocationType: int, flProtect: int, eCriticalLevel: int, ppMem: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(LPVOID, SIZE_T, DWORD)
    def VirtualFree(self, lpAddress: LPVOID, dwSize: int, dwFreeType: int) -> int: ...

    @virtual_table.com_function(PVOID, PVOID, SIZE_T, PSIZE_T)
    def VirtualQuery(self, lpAddress: PVOID, lpBuffer: PVOID, dwLength: int, pResult: IPointer[SIZE_T]) -> int: ...

    @virtual_table.com_function(PVOID, SIZE_T, DWORD, PDWORD)
    def VirtualProtect(self, lpAddress: PVOID, dwSize: int, flNewProtect: int, pflOldProtect: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD, PSIZE_T)
    def GetMemoryLoad(self, pMemoryLoad: PDWORD, pAvailableBytes: IPointer[SIZE_T]) -> int: ...

    @virtual_table.com_function(PTR(ICLRMemoryNotificationCallback))
    def RegisterMemoryNotificationCallback(self, pCallback: IPointer[ICLRMemoryNotificationCallback]) -> int: ...

    @virtual_table.com_function(LPVOID, SIZE_T)
    def NeedsVirtualAddressSpace(self, startAddress: LPVOID, size: int) -> int: ...

    @virtual_table.com_function(LPVOID, SIZE_T)
    def AcquiredVirtualAddressSpace(self, startAddress: LPVOID, size: int) -> int: ...

    @virtual_table.com_function(LPVOID)
    def ReleasedVirtualAddressSpace(self, startAddress: LPVOID) -> int: ...

    virtual_table.build()

TASKID = UINT64
CONNID = DWORD

class ICLRTask(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{28E66A4A-9906-4225-B231-9187C3EB8611}")

    @virtual_table.com_function(HANDLE)
    def SwitchIn(self, threadHandle: HANDLE) -> int: ...

    @virtual_table.com_function
    def SwitchOut(self) -> int: ...

    @virtual_table.com_function(PTR(COR_GC_THREAD_STATS))
    def GetMemStats(self, memUsage: IPointer[COR_GC_THREAD_STATS]) -> int: ...

    @virtual_table.com_function(BOOL)
    def Reset(self, fFull: bool) -> int: ...

    @virtual_table.com_function
    def ExitTask(self) -> int: ...

    @virtual_table.com_function
    def Abort(self) -> int: ...

    @virtual_table.com_function
    def RudeAbort(self) -> int: ...

    @virtual_table.com_function(PBOOL)
    def NeedsPriorityScheduling(self, pbNeedsPriorityScheduling: PBOOL) -> int: ...

    @virtual_table.com_function
    def YieldTask(self) -> int: ...

    @virtual_table.com_function(PSIZE_T)
    def LocksHeld(self, pLockCount: IPointer[SIZE_T]) -> int: ...

    @virtual_table.com_function(TASKID)
    def SetTaskIdentifier(self, asked: int) -> int: ...

    virtual_table.build()

class ICLRTask2(ICLRTask):
    virtual_table = COMVirtualTable.from_ancestor(ICLRTask)
    _iid_ = IID("{28E66A4A-9906-4225-B231-9187C3EB8612}")

    @virtual_table.com_function
    def BeginPreventAsyncAbort(self) -> int: ...

    @virtual_table.com_function
    def EndPreventAsyncAbort(self) -> int: ...

    virtual_table.build()

class IHostTask(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{C2275828-C4B1-4B55-82C9-92135F74DF1A}")

    @virtual_table.com_function
    def Start(self) -> int: ...

    @virtual_table.com_function
    def Alert(self) -> int: ...

    @virtual_table.com_function(DWORD, DWORD)
    def Join(self, dwMilliseconds: int, option: int) -> int: ...

    @virtual_table.com_function(INT)
    def SetPriority(self, newPriority: int) -> int: ...

    @virtual_table.com_function(PINT)
    def GetPriority(self, pPriority: PINT) -> int: ...

    @virtual_table.com_function(PTR(ICLRTask))
    def SetCLRTask(self, pCLRTask: IPointer[ICLRTask]) -> int: ...

    virtual_table.build()

TT_DEBUGGERHELPER = 0x1
TT_GC = 0x2
TT_FINALIZER = 0x4
TT_THREADPOOL_TIMER = 0x8
TT_THREADPOOL_GATE = 0x10
TT_THREADPOOL_WORKER = 0x20
TT_THREADPOOL_IOCOMPLETION = 0x40
TT_ADUNLOAD = 0x80
TT_USER = 0x100
TT_THREADPOOL_WAIT = 0x200
TT_UNKNOWN = 0x80000000
ETaskType = INT

class ICLRTaskManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{4862efbe-3ae5-44f8-8feb-346190ee8a34}")

    @virtual_table.com_function(DOUBLE_PTR(ICLRTask))
    def CreateTask(self, pTask: IDoublePtr[ICLRTask]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ICLRTask))
    def GetCurrentTask(self, pTask: IDoublePtr[ICLRTask]) -> int: ...

    @virtual_table.com_function(LCID)
    def SetUILocale(self, lcid: int) -> int: ...

    @virtual_table.com_function(LCID)
    def SetLocale(self, lcid: int) -> int: ...

    @virtual_table.com_function(PTR(ETaskType))
    def GetCurrentTaskType(self, pTaskType: IPointer[ETaskType]) -> int: ...

    virtual_table.build()

class IHostTaskManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{997FF24C-43B7-4352-8667-0DC04FAFD354}")

    @virtual_table.com_function(DOUBLE_PTR(IHostTask))
    def GetCurrentTask(self, pTask: IDoublePtr[IHostTask]) -> int: ...

    @virtual_table.com_function(DWORD, LPTHREAD_START_ROUTINE, PVOID, DOUBLE_PTR(IHostTask))
    def CreateTask(self, dwStackSize: int, pStartAddress: FARPROC, pParameter: PVOID, ppTask: IDoublePtr[IHostTask]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD)
    def Sleep(self, dwMilliseconds: int, option: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def SwitchToTask(self, option: int) -> int: ...

    @virtual_table.com_function(LCID)
    def SetUILocale(self, lcid: int) -> int: ...

    @virtual_table.com_function(LCID)
    def SetLocale(self, lcid: int) -> int: ...

    @virtual_table.com_function(SIZE_T, PBOOL)
    def CallNeedsHostHook(self, target: int, pbCallNeedsHostHook: PBOOL) -> int: ...

    @virtual_table.com_function(SIZE_T)
    def LeaveRuntime(self, target: int) -> int: ...

    @virtual_table.com_function
    def EnterRuntime(self) -> int: ...

    @virtual_table.com_function
    def ReverseLeaveRuntime(self) -> int: ...

    @virtual_table.com_function
    def ReverseEnterRuntime(self) -> int: ...

    @virtual_table.com_function
    def BeginDelayAbort(self) -> int: ...

    @virtual_table.com_function
    def EndDelayAbort(self) -> int: ...

    @virtual_table.com_function
    def BeginThreadAffinity(self) -> int: ...

    @virtual_table.com_function
    def EndThreadAffinity(self) -> int: ...

    @virtual_table.com_function(ULONG)
    def SetStackGuarantee(self, guarantee: int) -> int: ...

    @virtual_table.com_function(PULONG)
    def GetStackGuarantee(self, pGuarantee: PULONG) -> int: ...

    @virtual_table.com_function(PTR(ICLRTaskManager))
    def SetCLRTaskManager(self, ppManager: IPointer[ICLRTaskManager]) -> int: ...

    virtual_table.build()

class IHostThreadpoolManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{983D50E2-CB15-466B-80FC-845DC6E8C5FD}")

    @virtual_table.com_function(LPTHREAD_START_ROUTINE, PVOID, ULONG)
    def QueueUserWorkItem(self, Function: FARPROC, Context: PVOID, Flags: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetMaxThreads(self, dwMaxWorkerThreads: int) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetMaxThreads(self, pdwMaxWorkerThreads: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetAvailableThreads(self, pdwAvailableWorkerThreads: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetMinThreads(self, dwMinIOCompletionThreads: int) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetMinThreads(self, pdwMinIOCompletionThreads: PDWORD) -> int: ...

    virtual_table.build()

class ICLRIoCompletionManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{2d74ce86-b8d6-4c84-b3a7-9768933b3c12}")

    @virtual_table.com_function(DWORD, DWORD, PVOID)
    def OnComplete(self, dwErrorCode: int, NumberOfBytesTransferred: int, pvOverlapped: PVOID) -> int: ...

    virtual_table.build()

class IHostIoCompletionManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{8bde9d80-ec06-41d6-83e6-22580effcc20}")

    @virtual_table.com_function(PHANDLE)
    def CreateIoCompletionPort(self, phPort: IPointer[HANDLE]) -> int: ...

    @virtual_table.com_function(HANDLE)
    def CloseIoCompletionPort(self, hPort: HANDLE) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetMaxThreads(self, dwMaxIOCompletionThreads: int) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetMaxThread(self, pdwMaxIOCompletionThreads: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetAvailableThreads(self, pdwMaxIOCompletionThreads: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetHostOverlappedSize(self, pcbSize: PDWORD) -> int: ...

    @virtual_table.com_function(PTR(ICLRIoCompletionManager))
    def SetCLRIoCompletionManager(self, pManager: IPointer[ICLRIoCompletionManager]) -> int: ...

    @virtual_table.com_function(PVOID)
    def InitializeHostOverlapped(self, pvOverlapped: PVOID) -> int: ...

    @virtual_table.com_function(HANDLE, HANDLE)
    def Bind(self, hPort: HANDLE, hHandle: HANDLE) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetMinThreads(self, dwMinIOCompletionThreads: int) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetMinThreads(self, pdwMinIOCompletionThreads: PDWORD) -> int: ...

    virtual_table.build()

eSymbolReadingNever = 0
eSymbolReadingAlways = 1
eSymbolReadingFullTrustOnly = 2
ESymbolReadingPolicy = INT

class ICLRDebugManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00DCAEC6-2AC0-43a9-ACF9-1E36C139B10D}")

    @virtual_table.com_function(CONNID, LPWSTR)
    def BeginConnection(self, dwConnectionId: int, szConnectionName: LPWSTR) -> int: ...

    @virtual_table.com_function(CONNID, DWORD, DOUBLE_PTR(ICLRTask))
    def SetConnectionTasks(self, id: int, dwCount: int, ppCLRTask: IDoublePtr[ICLRTask]) -> int: ...

    @virtual_table.com_function(CONNID)
    def EndConnection(self, dwConnectionId: int) -> int: ...

    @virtual_table.com_function(PACL)
    def SetDacl(self, pacl: IPointer[ACL]) -> int: ...

    @virtual_table.com_function(PACL)
    def GetDacl(self, pacl: IPointer[ACL]) -> int: ...

    @virtual_table.com_function(PBOOL)
    def IsDebuggerAttached(self, pbAttached: PBOOL) -> int: ...

    @virtual_table.com_function(ESymbolReadingPolicy)
    def SetSymbolReadingPolicy(self, policy: int) -> int: ...

    virtual_table.build()

DUMP_FLAVOR_Mini = 0
DUMP_FLAVOR_CriticalCLRState = 1
DUMP_FLAVOR_NonHeapCLRState = 2
DUMP_FLAVOR_DEFAULT = DUMP_FLAVOR_Mini
ECustomDumpFlavor = INT

DUMP_ITEM_None = 0
ECustomDumpItemKind = INT

@CStructure.make
class CustomDumpItem(CStructure):
    itemKind: ECustomDumpItemKind

    @CUnion.make
    class U(CUnion):
        pReserved: IUIntPtr

    _u: IAnonymous[U]

BucketParamsCount = 10
BucketParamLength = 255
Parameter1 = 0
Parameter2 = 1
Parameter3 = 2
Parameter4 = 3
Parameter5 = 4
Parameter6 = 5
Parameter7 = 6
Parameter8 = 7
Parameter9 = 8
InvalidBucketParamIndex = 9
BucketParameterIndex = INT

@CStructure.make
class BucketParameters(CStructure):
    fInited: IBool
    pszEventTypeName: IArrayFixedSize[IWideChar,255]
    pszParams: IArrayFixedSize[IArrayFixedSize[IWideChar,10],255]

class ICLRErrorReportingManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{980D2F1A-BF79-4c08-812A-BB9778928F78}")

    @virtual_table.com_function(PTR(BucketParameters))
    def GetBucketParametersForCurrentException(self, pParams: IPointer[BucketParameters]) -> int: ...

    @virtual_table.com_function(ECustomDumpFlavor, DWORD, PTR(CustomDumpItem), DWORD)
    def BeginCustomDump(self, dwFlavor: int, dwNumItems: int, items: IPointer[CustomDumpItem], dwReserved: int) -> int: ...

    @virtual_table.com_function
    def EndCustomDump(self) -> int: ...

    virtual_table.build()

class IHostCrst(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{6DF710A6-26A4-4a65-8CD5-7237B8BDA8DC}")

    @virtual_table.com_function(DWORD)
    def Enter(self, option: int) -> int: ...

    @virtual_table.com_function
    def Leave(self) -> int: ...

    @virtual_table.com_function(DWORD, PBOOL)
    def TryEnter(self, option: int, pbSucceeded: PBOOL) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetSpinCount(self, dwSpinCount: int) -> int: ...

    virtual_table.build()

class IHostAutoEvent(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{50B0CFCE-4063-4278-9673-E5CB4ED0BDB8}")

    @virtual_table.com_function(DWORD, DWORD)
    def Wait(self, dwMilliseconds: int, option: int) -> int: ...

    @virtual_table.com_function
    def Set(self) -> int: ...

    virtual_table.build()

class IHostManualEvent(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1BF4EC38-AFFE-4fb9-85A6-525268F15B54}")

    @virtual_table.com_function(DWORD, DWORD)
    def Wait(self, dwMilliseconds: int, option: int) -> int: ...

    @virtual_table.com_function
    def Reset(self) -> int: ...

    @virtual_table.com_function
    def Set(self) -> int: ...

    virtual_table.build()

class IHostSemaphore(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{855efd47-cc09-463a-a97d-16acab882661}")

    @virtual_table.com_function(DWORD, DWORD)
    def Wait(self, dwMilliseconds: int, option: int) -> int: ...

    @virtual_table.com_function(LONG, PLONG)
    def ReleaseSemaphore(self, lReleaseCount: int, lpPreviousCount: PLONG) -> int: ...

    virtual_table.build()

class ICLRSyncManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{55FF199D-AD21-48f9-A16C-F24EBBB8727D}")

    @virtual_table.com_function(SIZE_T, DOUBLE_PTR(IHostTask))
    def GetMonitorOwner(self, Cookie: int, ppOwnerHostTask: IDoublePtr[IHostTask]) -> int: ...

    @virtual_table.com_function(SIZE_T, PSIZE_T)
    def CreateRWLockOwnerIterator(self, Cookie: int, pIterator: IPointer[SIZE_T]) -> int: ...

    @virtual_table.com_function(SIZE_T, DOUBLE_PTR(IHostTask))
    def GetRWLockOwnerNext(self, Iterator: int, ppOwnerHostTask: IDoublePtr[IHostTask]) -> int: ...

    @virtual_table.com_function(SIZE_T)
    def DeleteRWLockOwnerIterator(self, Iterator: int) -> int: ...

    virtual_table.build()

class IHostSyncManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{234330c7-5f10-4f20-9615-5122dab7a0ac}")

    @virtual_table.com_function(PTR(ICLRSyncManager))
    def SetCLRSyncManager(self, pManager: IPointer[ICLRSyncManager]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IHostCrst))
    def CreateCrst(self, ppCrst: IDoublePtr[IHostCrst]) -> int: ...

    @virtual_table.com_function(DWORD, DOUBLE_PTR(IHostCrst))
    def CreateCrstWithSpinCount(self, dwSpinCount: int, ppCrst: IDoublePtr[IHostCrst]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IHostAutoEvent))
    def CreateAutoEvent(self, ppEvent: IDoublePtr[IHostAutoEvent]) -> int: ...

    @virtual_table.com_function(BOOL, DOUBLE_PTR(IHostManualEvent))
    def CreateManualEvent(self, bInitialState: bool, ppEvent: IDoublePtr[IHostManualEvent]) -> int: ...

    @virtual_table.com_function(SIZE_T, DOUBLE_PTR(IHostAutoEvent))
    def CreateMonitorEvent(self, Cookie: int, ppEvent: IDoublePtr[IHostAutoEvent]) -> int: ...

    @virtual_table.com_function(SIZE_T, DOUBLE_PTR(IHostAutoEvent))
    def CreateRWLockWriterEvent(self, Cookie: int, ppEvent: IDoublePtr[IHostAutoEvent]) -> int: ...

    @virtual_table.com_function(BOOL, SIZE_T, DOUBLE_PTR(IHostManualEvent))
    def CreateRWLockReaderEvent(self, bInitialState: bool, Cookie: int, ppEvent: IDoublePtr[IHostManualEvent]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD, DOUBLE_PTR(IHostSemaphore))
    def CreateSemaphore(self, dwInitial: int, dwMax: int, ppSemaphore: IDoublePtr[IHostSemaphore]) -> int: ...

    virtual_table.build()

OPR_ThreadAbort = 0
OPR_ThreadRudeAbortInNonCriticalRegion = 1
OPR_ThreadRudeAbortInCriticalRegion = 2
OPR_AppDomainUnload = 3
OPR_AppDomainRudeUnload = 4
OPR_ProcessExit = 5
OPR_FinalizerRun = 6
MaxClrOperation = 7
EClrOperation = INT

FAIL_NonCriticalResource = 0
FAIL_CriticalResource = 1
FAIL_FatalRuntime = 2
FAIL_OrphanedLock = 3
FAIL_StackOverflow = 4
FAIL_AccessViolation = 5
FAIL_CodeContract = 6
MaxClrFailure = 7
EClrFailure = INT

eRuntimeDeterminedPolicy = 0
eHostDeterminedPolicy = 1
EClrUnhandledException = INT

eNoAction = 0
eThrowException = 1
eAbortThread = 2
eRudeAbortThread = 3
eUnloadAppDomain = 4
eRudeUnloadAppDomain = 5
eExitProcess = 6
eFastExitProcess = 7
eRudeExitProcess = 8
eDisableRuntime = 9
MaxPolicyAction = 10
EPolicyAction = INT

class ICLRPolicyManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7D290010-D781-45da-A6F8-AA5D711A730E}")

    @virtual_table.com_function(EClrOperation, EPolicyAction)
    def SetDefaultAction(self, operation: int, action: int) -> int: ...

    @virtual_table.com_function(EClrOperation, DWORD)
    def SetTimeout(self, operation: int, dwMilliseconds: int) -> int: ...

    @virtual_table.com_function(EClrOperation, EPolicyAction)
    def SetActionOnTimeout(self, operation: int, action: int) -> int: ...

    @virtual_table.com_function(EClrOperation, DWORD, EPolicyAction)
    def SetTimeoutAndAction(self, operation: int, dwMilliseconds: int, action: int) -> int: ...

    @virtual_table.com_function(EClrFailure, EPolicyAction)
    def SetActionOnFailure(self, failure: int, action: int) -> int: ...

    @virtual_table.com_function(EClrUnhandledException)
    def SetUnhandledExceptionPolicy(self, policy: int) -> int: ...

    virtual_table.build()

class IHostPolicyManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7AE49844-B1E3-4683-BA7C-1E8212EA3B79}")

    @virtual_table.com_function(EClrOperation, EPolicyAction)
    def OnDefaultAction(self, operation: int, action: int) -> int: ...

    @virtual_table.com_function(EClrOperation, EPolicyAction)
    def OnTimeout(self, operation: int, action: int) -> int: ...

    @virtual_table.com_function(EClrFailure, EPolicyAction)
    def OnFailure(self, failure: int, action: int) -> int: ...

    virtual_table.build()

Event_DomainUnload = 0
Event_ClrDisabled = 1
Event_MDAFired = 2
Event_StackOverflow = 3
MaxClrEvent = 4
EClrEvent = INT

@CStructure.make
class MDAInfo(CStructure):
    lpMDACaption: LPCWSTR
    lpMDAMessage: LPCWSTR
    lpStackTrace: LPCWSTR

SO_Managed = 0
SO_ClrEngine = 1
SO_Other = 2
StackOverflowType = INT

@CStructure.make
class StackOverflowInfo(CStructure):
    soType: IInteger[StackOverflowType]
    pExceptionInfo: IPointer[EXCEPTION_POINTERS]

class IActionOnCLREvent(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{607BE24B-D91B-4E28-A242-61871CE56E35}")

    @virtual_table.com_function(EClrEvent, PVOID)
    def OnEvent(self, event: int, data: PVOID) -> int: ...

    virtual_table.build()

class ICLROnEventManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1D0E0132-E64F-493D-9260-025C0E32C175}")

    @virtual_table.com_function(EClrEvent, PTR(IActionOnCLREvent))
    def RegisterActionOnEvent(self, event: int, pAction: IPointer[IActionOnCLREvent]) -> int: ...

    @virtual_table.com_function(EClrEvent, PTR(IActionOnCLREvent))
    def UnregisterActionOnEvent(self, event: int, pAction: IPointer[IActionOnCLREvent]) -> int: ...

    virtual_table.build()

class IHostGCManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{5D4EC34E-F248-457B-B603-255FAABA0D21}")

    @virtual_table.com_function
    def ThreadIsBlockingForSuspension(self) -> int: ...

    @virtual_table.com_function
    def SuspensionStarting(self) -> int: ...

    @virtual_table.com_function(DWORD)
    def SuspensionEnding(self, Generation: int) -> int: ...

    virtual_table.build()

class ICLRAssemblyReferenceList(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{1b2c9750-2e66-4bda-8b44-0a642c5cd733}")

    @virtual_table.com_function(LPCWSTR)
    def IsStringAssemblyReferenceInList(self, pwzAssemblyName: LPCWSTR) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def IsAssemblyReferenceInList(self, pName: IPointer[IUnknown]) -> int: ...

    virtual_table.build()

class ICLRReferenceAssemblyEnum(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{d509cb5d-cf32-4876-ae61-67770cf91973}")

    @virtual_table.com_function(DWORD, LPWSTR, PDWORD)
    def Get(self, dwIndex: int, pwzBuffer: LPWSTR, pcchBufferSize: PDWORD) -> int: ...

    virtual_table.build()

class ICLRProbingAssemblyEnum(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{d0c5fb1f-416b-4f97-81f4-7ac7dc24dd5d}")

    @virtual_table.com_function(DWORD, LPWSTR, PDWORD)
    def Get(self, dwIndex: int, pwzBuffer: LPWSTR, pcchBufferSize: PDWORD) -> int: ...

    virtual_table.build()

CLR_ASSEMBLY_IDENTITY_FLAGS_DEFAULT = 0
ECLRAssemblyIdentityFlags = INT

class ICLRAssemblyIdentityManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{15f0a9da-3ff6-4393-9da9-fdfd284e6972}")

    @virtual_table.com_function(PTR(LPCWSTR), DWORD, DOUBLE_PTR(ICLRAssemblyReferenceList))
    def GetCLRAssemblyReferenceList(self, ppwzAssemblyReferences: IPointer[LPCWSTR], dwNumOfReferences: int, ppReferenceList: IDoublePtr[ICLRAssemblyReferenceList]) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD, LPWSTR, PDWORD)
    def GetBindingIdentityFromFile(self, pwzFilePath: LPCWSTR, dwFlags: int, pwzBuffer: LPWSTR, pcchBufferSize: PDWORD) -> int: ...

    @virtual_table.com_function(LPSTREAM, DWORD, LPWSTR, PDWORD)
    def GetBindingIdentityFromStream(self, pStream: IPointer[IStream], dwFlags: int, pwzBuffer: LPWSTR, pcchBufferSize: PDWORD) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD, PTR(ICLRAssemblyReferenceList), DOUBLE_PTR(ICLRReferenceAssemblyEnum))
    def GetReferencedAssembliesFromFile(self, pwzFilePath: LPCWSTR, dwFlags: int, pExcludeAssembliesList: IPointer[ICLRAssemblyReferenceList], ppReferenceEnum: IDoublePtr[ICLRReferenceAssemblyEnum]) -> int: ...

    @virtual_table.com_function(LPSTREAM, DWORD, PTR(ICLRAssemblyReferenceList), DOUBLE_PTR(ICLRReferenceAssemblyEnum))
    def GetReferencedAssembliesFromStream(self, pStream: IPointer[IStream], dwFlags: int, pExcludeAssembliesList: IPointer[ICLRAssemblyReferenceList], ppReferenceEnum: IDoublePtr[ICLRReferenceAssemblyEnum]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD, LPCWSTR, DOUBLE_PTR(ICLRProbingAssemblyEnum))
    def GetProbingAssembliesFromReference(self, dwMachineType: int, dwFlags: int, pwzReferenceIdentity: LPCWSTR, ppProbingAssemblyEnum: IDoublePtr[ICLRProbingAssemblyEnum]) -> int: ...

    @virtual_table.com_function(LPCWSTR, PBOOL)
    def IsStronglyNamed(self, pwzAssemblyIdentity: LPCWSTR, pbIsStronglyNamed: PBOOL) -> int: ...

    virtual_table.build()

HOST_BINDING_POLICY_MODIFY_DEFAULT = 0
HOST_BINDING_POLICY_MODIFY_CHAIN = 1
HOST_BINDING_POLICY_MODIFY_REMOVE = 2
HOST_BINDING_POLICY_MODIFY_MAX = 3
EHostBindingPolicyModifyFlags = INT

class ICLRHostBindingPolicyManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{4b3545e7-1856-48c9-a8ba-24b21a753c09}")

    @virtual_table.com_function(LPCWSTR, LPCWSTR, PBYTE, DWORD, DWORD, PBYTE, PDWORD)
    def ModifyApplicationPolicy(self, pwzSourceAssemblyIdentity: LPCWSTR, pwzTargetAssemblyIdentity: LPCWSTR, pbApplicationPolicy: PBYTE, cbAppPolicySize: int, dwPolicyModifyFlags: int, pbNewApplicationPolicy: PBYTE, pcbNewAppPolicySize: PDWORD) -> int: ...

    @virtual_table.com_function(LPCWSTR, PBYTE, DWORD, LPWSTR, PDWORD, PDWORD)
    def EvaluatePolicy(self, pwzReferenceIdentity: LPCWSTR, pbApplicationPolicy: PBYTE, cbAppPolicySize: int, pwzPostPolicyReferenceIdentity: LPWSTR, pcchPostPolicyReferenceIdentity: PDWORD, pdwPoliciesApplied: PDWORD) -> int: ...

    virtual_table.build()

class ICLRGCManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{54D9007E-A8E2-4885-B7BF-F998DEEE4F2A}")

    @virtual_table.com_function(LONG)
    def Collect(self, Generation: int) -> int: ...

    @virtual_table.com_function(PTR(COR_GC_STATS))
    def GetStats(self, pStats: IPointer[COR_GC_STATS]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD)
    def SetGCStartupLimits(self, SegmentSize: int, MaxGen0Size: int) -> int: ...

    virtual_table.build()

class ICLRGCManager2(ICLRGCManager):
    virtual_table = COMVirtualTable.from_ancestor(ICLRGCManager)
    _iid_ = IID("{0603B793-A97A-4712-9CB4-0CD1C74C0F7C}")

    @virtual_table.com_function(SIZE_T, SIZE_T)
    def SetGCStartupLimitsEx(self, SegmentSize: int, MaxGen0Size: int) -> int: ...

    virtual_table.build()

ePolicyLevelNone = 0
ePolicyLevelRetargetable = 0x1
ePolicyUnifiedToCLR = 0x2
ePolicyLevelApp = 0x4
ePolicyLevelPublisher = 0x8
ePolicyLevelHost = 0x10
ePolicyLevelAdmin = 0x20
ePolicyPortability = 0x40
EBindPolicyLevels = INT

@CStructure.make
class AssemblyBindInfo(CStructure):
    dwAppDomainId: IDword
    lpReferencedIdentity: LPCWSTR
    lpPostPolicyIdentity: LPCWSTR
    ePolicyLevel: IDword

@CStructure.make
class ModuleBindInfo(CStructure):
    dwAppDomainId: IDword
    lpAssemblyIdentity: LPCWSTR
    lpModuleName: LPCWSTR

HOST_APPLICATION_BINDING_POLICY = 1
EHostApplicationPolicy = INT

class IHostAssemblyStore(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7b102a88-3f7f-496d-8fa2-c35374e01af3}")

    @virtual_table.com_function(PTR(AssemblyBindInfo), PUINT64, PUINT64, PTR(LPSTREAM), PTR(LPSTREAM))
    def ProvideAssembly(self, pBindInfo: IPointer[AssemblyBindInfo], pAssemblyId: IPointer[UINT64], pContext: IPointer[UINT64], ppStmAssemblyImage: IDoublePtr[IStream], ppStmPDB: IDoublePtr[IStream]) -> int: ...

    @virtual_table.com_function(PTR(ModuleBindInfo), PDWORD, PTR(LPSTREAM), PTR(LPSTREAM))
    def ProvideModule(self, pBindInfo: IPointer[ModuleBindInfo], pdwModuleId: PDWORD, ppStmModuleImage: IDoublePtr[IStream], ppStmPDB: IDoublePtr[IStream]) -> int: ...

    virtual_table.build()

class IHostAssemblyManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{613dabd7-62b2-493e-9e65-c1e32a1e0c5e}")

    @virtual_table.com_function(DOUBLE_PTR(ICLRAssemblyReferenceList))
    def GetNonHostStoreAssemblies(self, ppReferenceList: IDoublePtr[ICLRAssemblyReferenceList]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IHostAssemblyStore))
    def GetAssemblyStore(self, ppAssemblyStore: IDoublePtr[IHostAssemblyStore]) -> int: ...

    virtual_table.build()

@mscoree.foreign(HRESULT, LPIID, PTR(LPUNKNOWN), intermediate_method = True)
def GetCLRIdentityManager(iid: IID, ppManager: IDoublePtr[IUnknown], **kwargs) -> int:
    return delegate(iid.ref(), ppManager)

class IHostControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{02CA073C-7079-4860-880A-C2F7A449C991}")

    @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
    def GetHostManager(self, iid: IID, ppObject: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid, ppObject)

    @virtual_table.com_function(DWORD, LPUNKNOWN)
    def SetAppDomainManager(self, dwAppDomainId: int, pUnkAppDomainManager: IPointer[IUnknown]) -> int: ...

    virtual_table.build()

class ICLRControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{9065597E-D1A1-4fb2-B6BA-7E1FCE230F61}")

    @virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
    def GetCLRManager(self, iid: IID, ppObject: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid, ppObject)

    @virtual_table.com_function(LPCWSTR, LPCWSTR)
    def SetAppDomainManagerType(self, pwzAppDomainManagerAssembly: LPCWSTR, pwzAppDomainManagerType: LPCWSTR) -> int: ...

    virtual_table.build()

class ICLRRuntimeHost(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{90F1A06C-7712-4762-86B5-7A5EBA6BDB02}")

    @virtual_table.com_function
    def Start(self) -> int: ...

    @virtual_table.com_function
    def Stop(self) -> int: ...

    @virtual_table.com_function(PTR(IHostControl))
    def SetHostControl(self, pHostControl: IPointer[IHostControl]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ICLRControl))
    def GetCLRControl(self, pCLRControl: IDoublePtr[ICLRControl]) -> int: ...

    @virtual_table.com_function(DWORD, BOOL)
    def UnloadAppDomain(self, dwAppDomainId: int, fWaitUntilDone: bool) -> int: ...

    @virtual_table.com_function(DWORD, FExecuteInAppDomainCallback, PVOID)
    def ExecuteInAppDomain(self, dwAppDomainId: int, pCallback: FARPROC, cookie: PVOID) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetCurrentAppDomainId(self, pdwAppDomainId: PDWORD) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD, PTR(LPCWSTR), DWORD, PTR(LPCWSTR), PINT)
    def ExecuteApplication(self, pwzAppFullName: LPCWSTR, dwManifestPaths: int, ppwzManifestPaths: IPointer[LPCWSTR], dwActivationData: int, ppwzActivationData: IPointer[LPCWSTR], pReturnValue: PINT) -> int: ...

    @virtual_table.com_function(LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, PDWORD)
    def ExecuteInDefaultAppDomain(self, pwzAssemblyPath: LPCWSTR, pwzTypeName: LPCWSTR, pwzMethodName: LPCWSTR, pwzArgument: LPCWSTR, pReturnValue: PDWORD) -> int: ...

    virtual_table.build()

eNoChecks = 0
eSynchronization = 0x1
eSharedState = 0x2
eExternalProcessMgmt = 0x4
eSelfAffectingProcessMgmt = 0x8
eExternalThreading = 0x10
eSelfAffectingThreading = 0x20
eSecurityInfrastructure = 0x40
eUI = 0x80
eMayLeakOnAbort = 0x100
eAll = 0x1ff
EApiCategories = INT

class ICLRHostProtectionManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{89F25F5C-CEEF-43e1-9CFA-A68CE863AAAC}")

    @virtual_table.com_function(EApiCategories)
    def SetProtectedCategories(self, categories: int) -> int: ...

    @virtual_table.com_function
    def SetEagerSerializeGrantSets(self) -> int: ...

    virtual_table.build()

eInitializeNewDomainFlags_None = 0
eInitializeNewDomainFlags_NoSecurityChanges = 2
EInitializeNewDomainFlags = INT

class ICLRDomainManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{270D00A2-8E15-4d0b-ADEB-37BC3E47DF77}")

    @virtual_table.com_function(LPCWSTR, LPCWSTR, EInitializeNewDomainFlags)
    def SetAppDomainManagerType(self, wszAppDomainManagerAssembly: LPCWSTR, wszAppDomainManagerType: LPCWSTR, dwInitializeDomainFlags: int) -> int: ...

    @virtual_table.com_function(DWORD, PTR(LPCWSTR), PTR(LPCWSTR))
    def SetPropertiesForDefaultAppDomain(self, nProperties: int, pwszPropertyNames: IPointer[LPCWSTR], pwszPropertyValues: IPointer[LPCWSTR]) -> int: ...

    virtual_table.build()

class ITypeName(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{B81FF171-20F3-11d2-8DCC-00A0C9B00522}")

    @virtual_table.com_function(PDWORD)
    def GetNameCount(self, pCount: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD, LPBSTR, PDWORD)
    def GetNames(self, count: int, rgbszNames: IPointer[BSTR], pCount: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetTypeArgumentCount(self, pCount: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD, PVOID, PDWORD)
    def GetTypeArguments(self, count: int, rgpArguments: IDoublePtr['ITypeName'], pCount: PDWORD) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetModifierLength(self, pCount: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD, PDWORD, PDWORD)
    def GetModifiers(self, count: int, rgModifiers: PDWORD, pCount: PDWORD) -> int: ...

    @virtual_table.com_function(LPBSTR)
    def GetAssemblyName(self, rgbszAssemblyNames: IPointer[BSTR]) -> int: ...

    virtual_table.build()

class ITypeNameBuilder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{B81FF171-20F3-11d2-8DCC-00A0C9B00523}")

    @virtual_table.com_function
    def OpenGenericArguments(self) -> int: ...

    @virtual_table.com_function
    def CloseGenericArguments(self) -> int: ...

    @virtual_table.com_function
    def OpenGenericArgument(self) -> int: ...

    @virtual_table.com_function
    def CloseGenericArgument(self) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def AddName(self, szName: LPCWSTR) -> int: ...

    @virtual_table.com_function
    def AddPointer(self) -> int: ...

    @virtual_table.com_function
    def AddByRef(self) -> int: ...

    @virtual_table.com_function
    def AddSzArray(self) -> int: ...

    @virtual_table.com_function(DWORD)
    def AddArray(self, rank: int) -> int: ...

    @virtual_table.com_function(LPCWSTR)
    def AddAssemblySpec(self, szAssemblySpec: LPCWSTR) -> int: ...

    @virtual_table.com_function(LPBSTR)
    def ToString(self, pszStringRepresentation: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function
    def Clear(self) -> int: ...

    virtual_table.build()

class ITypeNameFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{B81FF171-20F3-11d2-8DCC-00A0C9B00521}")

    @virtual_table.com_function(LPCWSTR, PDWORD, DOUBLE_PTR(ITypeName))
    def ParseTypeName(self, szName: LPCWSTR, pError: PDWORD, ppTypeName: IDoublePtr[ITypeName]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(ITypeNameBuilder))
    def GetTypeNameBuilder(self, ppTypeBuilder: IDoublePtr[ITypeNameBuilder]) -> int: ...

    virtual_table.build()

class IApartmentCallback(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{178E5337-1528-4591-B1C9-1C6E484686D8}")

    @virtual_table.com_function(SIZE_T, SIZE_T)
    def DoCallback(self, pFunc: int, pData: int) -> int: ...

    virtual_table.build()

class IManagedObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{C3FCC19E-A970-11d2-8B5A-00A0C9B7C9C4}")

    @virtual_table.com_function(LPBSTR)
    def GetSerializedBuffer(self, pBSTR: IPointer[BSTR]) -> int: ...

    @virtual_table.com_function(LPBSTR, PINT, PINT)
    def GetObjectIdentity(self, pBSTRGUID: IPointer[BSTR], pAppDomainID: PINT, pCCW: PINT) -> int: ...

    virtual_table.build()

class ICatalogServices(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{04C6BE1E-1DB1-4058-AB7A-700CCCFBF254}")

    @virtual_table.com_function
    def Autodone(self) -> int: ...

    @virtual_table.com_function
    def NotAutodone(self) -> int: ...

    virtual_table.build()

class ComCallUnmarshal(COMClass):
    _clsid_ = CLSID("{3F281000-E95A-11d2-886B-00C04F869F04}")

class ComCallUnmarshalV4(COMClass):
    _clsid_ = CLSID("{45FB4600-E6E8-4928-B25E-50476FF79425}")

class CorRuntimeHost(COMClass):
    _clsid_ = CLSID("{CB2F6723-AB3A-11d2-9C40-00C04FA30A3E}")

class CLRRuntimeHost(COMClass):
    _clsid_ = CLSID("{90F1A06E-7712-4762-86B5-7A5EBA6BDB02}")

class TypeNameFactory(COMClass):
    _clsid_ = CLSID("{B81FF171-20F3-11d2-8DCC-00A0C9B00525}")

eCurrentContext = 0
eRestrictedContext = 1
EContextType = INT

class IHostSecurityContext(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{7E573CE4-0343-4423-98D7-6318348A1D3C}")

    @virtual_table.com_function(PVOID)
    def Capture(self, ppClonedContext: IDoublePtr['IHostSecurityContext']) -> int: ...

    virtual_table.build()

class IHostSecurityManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{75ad2468-a349-4d02-a764-76a68aee0c4f}")

    @virtual_table.com_function(HANDLE)
    def ImpersonateLoggedOnUser(self, hToken: HANDLE) -> int: ...

    @virtual_table.com_function
    def RevertToSelf(self) -> int: ...

    @virtual_table.com_function(DWORD, BOOL, PHANDLE)
    def OpenThreadToken(self, dwDesiredAccess: int, bOpenAsSelf: bool, phThreadToken: IPointer[HANDLE]) -> int: ...

    @virtual_table.com_function(HANDLE)
    def SetThreadToken(self, hToken: HANDLE) -> int: ...

    @virtual_table.com_function(EContextType, DOUBLE_PTR(IHostSecurityContext))
    def GetSecurityContext(self, eContextType: int, ppSecurityContext: IDoublePtr[IHostSecurityContext]) -> int: ...

    @virtual_table.com_function(EContextType, PTR(IHostSecurityContext))
    def SetSecurityContext(self, eContextType: int, pSecurityContext: IPointer[IHostSecurityContext]) -> int: ...

    virtual_table.build()

class ICLRAppDomainResourceMonitor(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{c62de18c-2e23-4aea-8423-b40c1fc59eae}")

    @virtual_table.com_function(DWORD, PULONGLONG)
    def GetCurrentAllocated(self, dwAppDomainId: int, pBytesAllocated: IPointer[ULONGLONG]) -> int: ...

    @virtual_table.com_function(DWORD, PULONGLONG, PULONGLONG)
    def GetCurrentSurvived(self, dwAppDomainId: int, pAppDomainBytesSurvived: IPointer[ULONGLONG], pTotalBytesSurvived: IPointer[ULONGLONG]) -> int: ...

    @virtual_table.com_function(DWORD, PULONGLONG)
    def GetCurrentCpuTime(self, dwAppDomainId: int, pMilliseconds: IPointer[ULONGLONG]) -> int: ...

    virtual_table.build()

