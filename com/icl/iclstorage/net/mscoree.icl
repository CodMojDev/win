.icl
.ver 100
.gencomment

/********************************************
 *	MSCOREE.ICL Interface Contract Language
 *	Core definition of MSCorEE types.
 ********************************************/

.inc gchost.icl
.inc ivalidator.icl

silent
{
	pie PROCESS_INFORMATION LPPROCESS_INFORMATION
	pie IStream LPSTREAM
	pie VARIANT LPVARIANT
	pie SIZE_T PSIZE_T
	pie HANDLE PHANDLE
	pie ACL PACL
	pie UINT64 PUINT64
	pie BSTR LPBSTR
	pie ULONGLONG PULONGLONG
}

al int LCID UINT64
al FARPROC LPOVERLAPPED_COMPLETION_ROUTINE LPTHREAD_START_ROUTINE FLockClrVersionCallback FExecuteInAppDomainCallback

~
~from ..processthreadsapi import *
~from ..minwinbase import *
~
~from ..com.autointerfacedef import *
~from ..com.bstr import *
~
~from .gchost import *
~from .ivalidator import *
~
~mscoree = get_win_library('mscoree.dll')
~

eq CLR_MAJOR_VERSION 4
eq CLR_MINOR_VERSION 0
eq CLR_BUILD_VERSION 30319
eq CLR_ASSEMBLY_MAJOR_VERSION 4
eq CLR_ASSEMBLY_MINOR_VERSION 0
eq CLR_ASSEMBLY_BUILD_VERSION 0

~

dcl LIBID_mscoree 0x5477469e 0x83b1 0x11d2 0x8b 0x49 0x00 0xa0 0xc9 0xb7 0xc9 0xc4
dcl CLSID_CorRuntimeHost 0xcb2f6723 0xab3a 0x11d2 0x9c 0x40 0x00 0xc0 0x4f 0xa3 0x0a 0x3e
dcl CLSID_TypeNameFactory 0xB81FF171 0x20F3 0x11d2 0x8d 0xcc 0x00 0xa0 0xc9 0xb0 0x05 0x25
dcl CLSID_CLRRuntimeHost 0x90F1A06E 0x7712 0x4762 0x86 0xB5 0x7A 0x5E 0xBA 0x6B 0xDB 0x02
dcl CLSID_ComCallUnmarshal 0x3F281000 0xE95A 0x11d2 0x88 0x6B 0x00 0xC0 0x4F 0x86 0x9F 0x04
dcl CLSID_ComCallUnmarshalV4 0x45fb4600 0xe6e8 0x4928 0xb2 0x5e 0x50 0x47 0x6f 0xf7 0x94 0x25
dii IID_IObjectHandle 0xc460e2b4 0xe199 0x412a 0x84 0x56 0x84 0xdc 0x3e 0x48 0x38 0xc3
dii IID_IManagedObject 0xc3fcc19e 0xa970 0x11d2 0x8b 0x5a 0x00 0xa0 0xc9 0xb7 0xc9 0xc4
dii IID_IApartmentCallback 0x178e5337 0x1528 0x4591 0xb1 0xc9 0x1c 0x6e 0x48 0x46 0x86 0xd8
dii IID_ICatalogServices 0x04c6be1e 0x1db1 0x4058 0xab 0x7a 0x70 0x0c 0xcc 0xfb 0xf2 0x54
dii IID_ICorRuntimeHost 0xcb2f6722 0xab3a 0x11d2 0x9c 0x40 0x00 0xc0 0x4f 0xa3 0x0a 0x3e
dii IID_ICorThreadpool 0x84680D3A 0xB2C1 0x46e8 0xAC 0xC2 0xDB 0xC0 0xA3 0x59 0x15 0x9A
dii IID_ICLRDebugManager 0xdcaec6 0x2ac0 0x43a9 0xac 0xf9 0x1e 0x36 0xc1 0x39 0xb1 0xd
dii IID_IHostMemoryNeededCallback 0x47EB8E57 0x0846 0x4546 0xAF 0x76 0x6F 0x42 0xFC 0xFC 0x26 0x49
dii IID_IHostMalloc 0x1831991C 0xCC53 0x4A31 0xB2 0x18 0x04 0xE9 0x10 0x44 0x64 0x79
dii IID_IHostMemoryManager 0x7BC698D1 0xF9E3 0x4460 0x9C 0xDE 0xD0 0x42 0x48 0xE9 0xFA 0x25
dii IID_ICLRTask 0x28E66A4A 0x9906 0x4225 0xB2 0x31 0x91 0x87 0xc3 0xeb 0x86 0x11
dii IID_ICLRTask2 0x28E66A4A 0x9906 0x4225 0xB2 0x31 0x91 0x87 0xc3 0xeb 0x86 0x12
dii IID_IHostTask 0xC2275828 0xC4B1 0x4B55 0x82 0xC9 0x92 0x13 0x5F 0x74 0xDF 0x1A
dii IID_ICLRTaskManager 0x4862efbe 0x3ae5 0x44f8 0x8F 0xEB 0x34 0x61 0x90 0xeE 0x8A 0x34
dii IID_IHostTaskManager 0x997FF24C 0x43B7 0x4352 0x86 0x67 0x0D 0xC0 0x4F 0xAF 0xD3 0x54
dii IID_IHostThreadpoolManager 0x983D50E2 0xCB15 0x466B 0x80 0xFC 0x84 0x5D 0xC6 0xE8 0xC5 0xFD
dii IID_ICLRIoCompletionManager 0x2D74CE86 0xB8D6 0x4C84 0xB3 0xA7 0x97 0x68 0x93 0x3B 0x3C 0x12
dii IID_IHostIoCompletionManager 0x8BDE9D80 0xEC06 0x41D6 0x83 0xE6 0x22 0x58 0x0E 0xFF 0xCC 0x20
dii IID_IHostSyncManager 0x234330c7 0x5f10 0x4f20 0x96 0x15 0x51 0x22 0xda 0xb7 0xa0 0xac
dii IID_IHostCrst 0x6DF710A6 0x26A4 0x4a65 0x8c 0xd5 0x72 0x37 0xb8 0xbd 0xa8 0xdc
dii IID_IHostAutoEvent 0x50B0CFCE 0x4063 0x4278 0x96 0x73 0xe5 0xcb 0x4e 0xd0 0xbd 0xb8
dii IID_IHostManualEvent 0x1BF4EC38 0xAFFE 0x4fb9 0x85 0xa6 0x52 0x52 0x68 0xf1 0x5b 0x54
dii IID_IHostSemaphore 0x855efd47 0xcc09 0x463a 0xa9 0x7d 0x16 0xac 0xab 0x88 0x26 0x61
dii IID_ICLRSyncManager 0x55FF199D 0xAD21 0x48f9 0xa1 0x6c 0xf2 0x4e 0xbb 0xb8 0x72 0x7d
dii IID_ICLRAppDomainResourceMonitor 0XC62DE18C 0X2E23 0X4AEA 0X84 0X23 0XB4 0X0C 0X1F 0XC5 0X9E 0XAE
dii IID_ICLRPolicyManager 0x7D290010 0xD781 0x45da 0xA6 0xF8 0xAA 0x5D 0x71 0x1A 0x73 0x0E
dii IID_ICLRGCManager 0x54D9007E 0xA8E2 0x4885 0xB7 0xBF 0xF9 0x98 0xDE 0xEE 0x4F 0x2A
dii IID_ICLRGCManager2 0x0603B793 0xA97A 0x4712 0x9C 0xB4 0x0C 0xD1 0xC7 0x4C 0x0F 0x7C
dii IID_ICLRErrorReportingManager 0x980d2f1a 0xbf79 0x4c08 0x81 0x2a 0xbb 0x97 0x78 0x92 0x8f 0x78
dii IID_IHostPolicyManager 0x7AE49844 0xB1E3 0x4683 0xBA 0x7C 0x1E 0x82 0x12 0xEA 0x3B 0x79
dii IID_IHostGCManager 0x5D4EC34E 0xF248 0x457B 0xB6 0x03 0x25 0x5F 0xAA 0xBA 0x0D 0x21
dii IID_IActionOnCLREvent 0x607BE24B 0xD91B 0x4E28 0xA2 0x42 0x61 0x87 0x1C 0xE5 0x6E 0x35
dii IID_ICLROnEventManager 0x1D0E0132 0xE64F 0x493D 0x92 0x60 0x02 0x5C 0x0E 0x32 0xC1 0x75
dii IID_ICLRRuntimeHost 0x90F1A06C 0x7712 0x4762 0x86 0xB5 0x7A 0x5E 0xBA 0x6B 0xDB 0x02
dii IID_ICLRHostProtectionManager 0x89f25f5c 0xceef 0x43e1 0x9c 0xfa 0xa6 0x8c 0xe8 0x63 0xaa 0xac
dii IID_IHostAssemblyStore 0x7b102a88 0x3f7f 0x496d 0x8f 0xa2 0xc3 0x53 0x74 0xe0 0x1a 0xf3
dii IID_IHostAssemblyManager 0x613dabd7 0x62b2 0x493e 0x9e 0x65 0xc1 0xe3 0x2a 0x1e 0x0c 0x5e
dii IID_IHostSecurityManager 0x75ad2468 0xa349 0x4d02 0xa7 0x64 0x76 0xa6 0x8a 0xee 0x0c 0x4f
dii IID_IHostSecurityContext 0x7e573ce4 0x343 0x4423 0x98 0xd7 0x63 0x18 0x34 0x8a 0x1d 0x3c
dii IID_ICLRAssemblyIdentityManager 0x15f0a9da 0x3ff6 0x4393 0x9d 0xa9 0xfd 0xfd 0x28 0x4e 0x69 0x72
dii IID_ICLRDomainManager 0x270d00a2 0x8e15 0x4d0b 0xad 0xeb 0x37 0xbc 0x3e 0x47 0xdf 0x77
dii IID_ITypeName 0xB81FF171 0x20F3 0x11d2 0x8d 0xcc 0x00 0xa0 0xc9 0xb0 0x05 0x22
dii IID_ICLRAssemblyReferenceList 0x1b2c9750 0x2e66 0x4bda 0x8b 0x44 0x0a 0x64 0x2c 0x5c 0xd7 0x33
dii IID_ICLRReferenceAssemblyEnum 0xd509cb5d 0xcf32 0x4876 0xae 0x61 0x67 0x77 0x0c 0xf9 0x19 0x73
dii IID_ICLRProbingAssemblyEnum 0xd0c5fb1f 0x416b 0x4f97 0x81 0xf4 0x7a 0xc7 0xdc 0x24 0xdd 0x5d
dii IID_ICLRHostBindingPolicyManager 0x4b3545e7 0x1856 0x48c9 0xa8 0xba 0x24 0xb2 0x1a 0x75 0x3c 0x09
dii IID_ITypeNameBuilder 0xB81FF171 0x20F3 0x11d2 0x8d 0xcc 0x00 0xa0 0xc9 0xb0 0x05 0x23
dii IID_ITypeNameFactory 0xB81FF171 0x20F3 0x11d2 0x8d 0xcc 0x00 0xa0 0xc9 0xb0 0x05 0x21

ff mscoree.GetCORSystemDirectory HRESULT pbuffer LPWSTR cchBuffer DWORD dwLength PDWORD
ff mscoree.GetCORVersion HRESULT pbBuffer LPWSTR cchBuffer DWORD dwLength PDWORD
ff mscoree.GetFileVersion HRESULT szFilename LPCWSTR szBuffer LPWSTR cchBuffer DWORD dwLength PDWORD
ff mscoree.GetCORRequiredVersion HRESULT pbuffer LPWSTR cchBuffer DWORD dwLength PDWORD
ff mscoree.GetRequestedRuntimeInfo HRESULT pExe LPCWSTR pwszVersion LPCWSTR pConfigurationFile LPCWSTR startupFlags DWORD runtimeInfoFlags DWORD pDirectory LPWSTR dwDirectory DWORD dwDirectoryLength PDWORD pVersion LPWSTR cchBuffer DWORD dwlength DWORD
ff mscoree.GetRequestedRuntimeVersion HRESULT pExe LPWSTR pVersion LPWSTR cchBuffer DWORD dwLength PDWORD
ff mscoree.CorBindToRuntimeHost HRESULT pwszVersion LPCWSTR pwszBuildFlavor LPCWSTR pwszHostConfigFile LPCWSTR pReserved PVOID startupFlags DWORD rclsid R.CLSID riid R.IID ppv P.PVOID
ff mscoree.CorBindToRuntimeEx HRESULT pwszVersion LPCWSTR pwszBuildFlavor LPCWSTR startupFlags DWORD rclsid R.CLSID riid R.IID ppv P.PVOID
ff mscoree.CorBindToRuntimeByCfg HRESULT pCfgStream P.IStream reserved DWORD startupFlags DWORD rclsid R.CLSID riid R.IID ppv P.PVOID
ff mscoree.CorBindToRuntime HRESULT pwszVersion LPCWSTR pwszBuildFlavor LPCWSTR rclsid R.CLSID riid R.IID ppv P.PVOID
ff mscoree.CorBindToCurrentRuntime HRESULT pwszFileName LPCWSTR rclsid R.CLSID riid R.IID ppv P.PVOID
ff mscoree.ClrCreateManagedInstance HRESULT pTypeName LPCWSTR riid R.IID ppObject P.PVOID
ff mscoree.CorMarkThreadInThreadPool VOID 
ff mscoree.RunDll32ShimW HRESULT hwnd HWND hinst HINSTANCE lpszCmdLine LPCWSTR nCmdShow INT
ff mscoree.LoadLibraryShim HRESULT szDllName LPCWSTR szVersion LPCWSTR pvReserved PVOID phModDll P.HMODULE
ff mscoree.CallFunctionShim HRESULT szDllName LPCWSTR szFunctionName LPCSTR lpvArgument1 PVOID lpvArgument2 PVOID szVersion LPCWSTR pvReserved PVOID
ff mscoree.GetRealProcAddress HRESULT pwszProcName LPSTR ppv P.PVOID
ff mscoree.CorExitProcess VOID exitCode INT
ff mscoree.LoadStringRC HRESULT iResouceID UINT szBuffer LPWSTR iMax INT bQuiet INT
ff mscoree.LoadStringRCEx HRESULT lcid LCID iResouceID UINT szBuffer LPWSTR iMax INT bQuiet INT pcwchUsed PINT

~FLockClrVersionCallback = WINAPI(HRESULT)
~

ff mscoree.LockClrVersion HRESULT hostCallback FLockClrVersionCallback pBeginHostSetup PVOID pEndHostSetup PVOID
ff mscoree.CreateDebuggingInterfaceFromVersion HRESULT iDebuggerVersion INT szDebuggeeVersion LPCWSTR ppCordb P.P.IUnknown
ff mscoree.GetVersionFromProcess HRESULT hProcess HANDLE pVersion LPWSTR cchBuffer DWORD dwLength PDWORD

ed HOST_TYPE
{
	ee HOST_TYPE_DEFAULT
	ee HOST_TYPE_APPLAUNCH
	ee HOST_TYPE_CORFLAG
}

ff mscoree.CorLaunchApplication HRESULT dwClickOnceHost HOST_TYPE pwzAppFullName LPCWSTR dwManifestPaths DWORD ppwzManifestPaths P.LPCWSTR dwActivationData DWORD ppwzActivationData P.LPCWSTR lpProcessInformation P.PROCESS_INFORMATION

~FExecuteInAppDomainCallback = WINAPI(HRESULT, PVOID)
~

ed STARTUP_FLAGS
{
~STARTUP_CONCURRENT_GC = 0x1
~STARTUP_LOADER_OPTIMIZATION_MASK = ( 0x3 << 1 )
~STARTUP_LOADER_OPTIMIZATION_SINGLE_DOMAIN = ( 0x1 << 1 )
~STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN = ( 0x2 << 1 )
~STARTUP_LOADER_OPTIMIZATION_MULTI_DOMAIN_HOST = ( 0x3 << 1 )
~STARTUP_LOADER_SAFEMODE = 0x10
~STARTUP_LOADER_SETPREFERENCE = 0x100
~STARTUP_SERVER_GC = 0x1000
~STARTUP_HOARD_GC_VM = 0x2000
~STARTUP_SINGLE_VERSION_HOSTING_INTERFACE = 0x4000
~STARTUP_LEGACY_IMPERSONATION = 0x10000
~STARTUP_DISABLE_COMMITTHREADSTACK = 0x20000
~STARTUP_ALWAYSFLOW_IMPERSONATION = 0x40000
~STARTUP_TRIM_GC_COMMIT = 0x80000
~STARTUP_ETW = 0x100000
~STARTUP_ARM = 0x400000
}

ed CLSID_RESOLUTION_FLAGS
{
	ee CLSID_RESOLUTION_DEFAULT
	ee CLSID_RESOLUTION_REGISTERED
}

ed RUNTIME_INFO_FLAGS
{
	ee RUNTIME_INFO_UPGRADE_VERSION 1
	ee RUNTIME_INFO_REQUEST_IA64 2
	ee RUNTIME_INFO_REQUEST_AMD64 4
	ee RUNTIME_INFO_REQUEST_X86 8
	ee RUNTIME_INFO_DONT_RETURN_DIRECTORY 16
	ee RUNTIME_INFO_DONT_RETURN_VERSION 32
	ee RUNTIME_INFO_DONT_SHOW_ERROR_DIALOG 64
	ee RUNTIME_INFO_IGNORE_ERROR_MODE 4096
}

ed APPDOMAIN_SECURITY_FLAGS
{
	ee APPDOMAIN_SECURITY_DEFAULT 0
	ee APPDOMAIN_SECURITY_SANDBOXED 1
	ee APPDOMAIN_SECURITY_FORBID_CROSSAD_REVERSE_PINVOKE 2
	ee APPDOMAIN_FORCE_TRIVIAL_WAIT_OPERATIONS 8
}

ff mscoree.GetRequestedRuntimeVersionForCLSID HRESULT rclsid R.CLSID pVersion LPWSTR cchBuffer DWORD dwLength PDWORD dwResolutionFlags CLSID_RESOLUTION_FLAGS

IU IObjectHandle
{
	iid C460E2B4-E199-412a-8456-84DC3E4838C3
	cf Unwrap ppv P.VARIANT
}

IU IAppDomainBinding
{
	iid 5C2B07A7-1E98-11d3-872F-00C04F79ED0D
	cf OnAppDomain pAppdomain P.IUnknown
}

IU IGCThreadControl
{
	iid F31D1788-C397-4725-87A5-6AF3472C2791
	cf ThreadIsBlockingForSuspension
	cf SuspensionStarting
	cf SuspensionEnding Generation DWORD
}

IU IGCHostControl
{
	iid 5513D564-8374-4cb9-AED9-0083F4160A1D
	cf RequestVirtualMemLimit sztMaxVirtualMemMB SIZE_T psztNewMaxVirtualMemMB P.SIZE_T
}

~PTLS_CALLBACK_FUNCTION = WINAPI(VOID, PVOID)
~

IU ICorThreadpool
{
	iid 84680D3A-B2C1-46e8-ACC2-DBC0A359159A
	cf CorRegisterWaitForSingleObject phNewWaitObject P.HANDLE hWaitObject HANDLE Callback WAITORTIMERCALLBACK Context PVOID timeout ULONG executeOnlyOnce BOOL result PBOOL
	cf CorUnregisterWait hWaitObject HANDLE CompletionEvent HANDLE result PBOOL
	cf CorQueueUserWorkItem Function LPTHREAD_START_ROUTINE Context PVOID executeOnlyOnce BOOL result PBOOL
	cf CorCreateTimer phNewTimer P.HANDLE Callback WAITORTIMERCALLBACK Parameter PVOID DueTime DWORD Period DWORD result PBOOL
	cf CorChangeTimer Timer HANDLE DueTime ULONG Period ULONG result PBOOL
	cf CorDeleteTimer Timer HANDLE CompletionEvent HANDLE result PBOOL
	cf CorBindIoCompletionCallback fileHandle HANDLE callback LPOVERLAPPED_COMPLETION_ROUTINE
	cf CorCallOrQueueUserWorkItem Function LPTHREAD_START_ROUTINE Context PVOID result PBOOL
	cf CorSetMaxThreads MaxWorkerThreads DWORD MaxIOCompletionThreads DWORD
	cf CorGetMaxThreads MaxWorkerThreads PDWORD MaxIOCompletionThreads PDWORD
	cf CorGetAvailableThreads AvailableWorkerThreads PDWORD AvailableIOCompletionThreads PDWORD
}

IU IDebuggerThreadControl
{
	iid 23D86786-0BB5-4774-8FB5-E3522ADD6246
	cf ThreadIsBlockingForDebugger
	cf ReleaseAllRuntimeThreads
	cf StartBlockingForDebugger dwUnused DWORD
}

IU IDebuggerInfo
{
	iid BF24142D-A47D-4d24-A66D-8C2141944E44
	cf IsDebuggerAttached pbAttached PBOOL
}

IU ICorConfiguration
{
	cf SetGCThreadControl pGCThreadControl P.IGCThreadControl
	cf SetGCHostControl pGCHostControl P.IGCHostControl
	cf SetDebuggerThreadControl pDebuggerThreadControl P.IDebuggerThreadControl
	cf AddDebuggerSpecialThread dwSpecialThreadId DWORD
}

eq HDOMAINENUM PVOID

~

IU ICorRuntimeHost
{
	iid CB2F6722-AB3A-11d2-9C40-00C04FA30A3E
	cf CreateLogicalThreadState
	cf DeleteLogicalThreadState
	cf SwitchInLogicalThreadState pFiberCookie PDWORD
	cf SwitchOutLogicalThreadState pFiberCookie P.P.DWORD
	cf LocksHeldByLogicalThread pCount PDWORD
	cf MapFile hFile HANDLE hMapAddress P.HMODULE
	cf GetConfiguration pConfiguration P.P.ICorConfiguration
	cf Start
	cf Stop
	cf CreateDomain pwzFriendlyName LPCWSTR pIdentityArray P.IUnknown pAppDomain P.P.IUnknown
	cf GetDefaultDomain pAppDomain P.P.IUnknown
	cf EnumDomains hEnum P.HDOMAINENUM
	cf NextDomain hEnum HDOMAINENUM pAppDomain P.P.IUnknown
	cf CloseEnum hEnum HDOMAINENUM
	cf CreateDomainEx pwzFriendlyName LPCWSTR pSetup P.IUnknown pEvidence P.IUnknown pAppDomain P.P.IUnknown
	cf CreateDomainSetup pAppDomainSetup P.P.IUnknown
	cf CreateEvidence pEvidence P.P.IUnknown
	cf UnloadDomain pAppDomain P.IUnknown
	cf CurrentDomain pAppDomain P.P.IUnknown
}

ed EMemoryAvailable
{
	ee eMemoryAvailableLow 1
	ee eMemoryAvailableNeutral
	ee eMemoryAvailableHigh
}

ed EMemoryCriticalLevel
{
	ee eTaskCritical
	ee eAppDomainCritical
	ee eProcessCritical
}

ed WAIT_OPTION
{
	ee WAIT_MSGPUMP 1
	ee WAIT_ALERTABLE 2
	ee WAIT_NOTINDEADLOCK 4
}

IU ICLRMemoryNotificationCallback
{
	iid 47EB8E57-0846-4546-AF76-6F42FCFC2649
	cf OnMemoryNotification eMemoryAvailable EMemoryAvailable
}

IU IHostMalloc
{
	iid 1831991C-CC53-4A31-B218-04E910446479
	cf Alloc cbSize SIZE_T eCriticalLevel EMemoryCriticalLevel ppMem P.PVOID
	cf DebugAlloc cbSize SIZE_T eCriticalLevel EMemoryCriticalLevel pszFileName LPSTR iLineNo INT ppMem P.PVOID
	cf Free pMem PVOID
}

ed MALLOC_TYPE
{
	ee MALLOC_THREADSAFE 1
	ee MALLOC_EXECUTABLE
}

IU IHostMemoryManager
{
	iid 7BC698D1-F9E3-4460-9CDE-D04248E9FA25
	cf CreateMalloc dwMallocType DWORD ppMalloc P.P.IHostMalloc
	cf VirtualAlloc pAddress PVOID dwSize SIZE_T flAllocationType DWORD flProtect DWORD eCriticalLevel EMemoryCriticalLevel ppMem P.PVOID
	cf VirtualFree lpAddress LPVOID dwSize SIZE_T dwFreeType DWORD
	cf VirtualQuery lpAddress PVOID lpBuffer PVOID dwLength SIZE_T pResult P.SIZE_T
	cf VirtualProtect lpAddress PVOID dwSize SIZE_T flNewProtect DWORD pflOldProtect PDWORD
	cf GetMemoryLoad pMemoryLoad PDWORD pAvailableBytes P.SIZE_T
	cf RegisterMemoryNotificationCallback pCallback P.ICLRMemoryNotificationCallback
	cf NeedsVirtualAddressSpace startAddress LPVOID size SIZE_T
	cf AcquiredVirtualAddressSpace startAddress LPVOID size SIZE_T
	cf ReleasedVirtualAddressSpace startAddress LPVOID
}

eq TASKID UINT64
eq CONNID DWORD

~

al int TASKID CONNID

IU ICLRTask
{
	iid 28E66A4A-9906-4225-B231-9187C3EB8611
	cf SwitchIn threadHandle HANDLE
	cf SwitchOut
	cf GetMemStats memUsage P.COR_GC_THREAD_STATS
	cf Reset fFull BOOL
	cf ExitTask
	cf Abort
	cf RudeAbort
	cf NeedsPriorityScheduling pbNeedsPriorityScheduling PBOOL
	cf YieldTask
	cf LocksHeld pLockCount P.SIZE_T
	cf SetTaskIdentifier asked TASKID
}

I ICLRTask2 ex ICLRTask
{
	iid 28E66A4A-9906-4225-B231-9187C3EB8612
	cf BeginPreventAsyncAbort
	cf EndPreventAsyncAbort
}

IU IHostTask
{
	iid C2275828-C4B1-4B55-82C9-92135F74DF1A
	cf Start
	cf Alert
	cf Join dwMilliseconds DWORD option DWORD
	cf SetPriority newPriority INT
	cf GetPriority pPriority PINT
	cf SetCLRTask pCLRTask P.ICLRTask
}

ed ETaskType
{
	ee TT_DEBUGGERHELPER 0x1
	ee TT_GC 0x2
	ee TT_FINALIZER 0x4
	ee TT_THREADPOOL_TIMER 0x8
	ee TT_THREADPOOL_GATE 0x10
	ee TT_THREADPOOL_WORKER 0x20
	ee TT_THREADPOOL_IOCOMPLETION 0x40
	ee TT_ADUNLOAD 0x80
	ee TT_USER 0x100
	ee TT_THREADPOOL_WAIT 0x200
	ee TT_UNKNOWN 0x80000000
}

IU ICLRTaskManager
{
	iid 4862efbe-3ae5-44f8-8feb-346190ee8a34
	cf CreateTask pTask P.P.ICLRTask
	cf GetCurrentTask pTask P.P.ICLRTask
	cf SetUILocale lcid LCID
	cf SetLocale lcid LCID
	cf GetCurrentTaskType pTaskType P.ETaskType
}

IU IHostTaskManager
{
	iid 997FF24C-43B7-4352-8667-0DC04FAFD354
	cf GetCurrentTask pTask P.P.IHostTask
	cf CreateTask dwStackSize DWORD pStartAddress LPTHREAD_START_ROUTINE pParameter PVOID ppTask P.P.IHostTask
	cf Sleep dwMilliseconds DWORD option DWORD
	cf SwitchToTask option DWORD
	cf SetUILocale lcid LCID
	cf SetLocale lcid LCID
	cf CallNeedsHostHook target SIZE_T pbCallNeedsHostHook PBOOL
	cf LeaveRuntime target SIZE_T
	cf EnterRuntime
	cf ReverseLeaveRuntime
	cf ReverseEnterRuntime
	cf BeginDelayAbort
	cf EndDelayAbort
	cf BeginThreadAffinity
	cf EndThreadAffinity
	cf SetStackGuarantee guarantee ULONG
	cf GetStackGuarantee pGuarantee PULONG
	cf SetCLRTaskManager ppManager P.ICLRTaskManager
}

IU IHostThreadpoolManager
{
	iid 983D50E2-CB15-466B-80FC-845DC6E8C5FD
	cf QueueUserWorkItem Function LPTHREAD_START_ROUTINE Context PVOID Flags ULONG
	cf SetMaxThreads dwMaxWorkerThreads DWORD
	cf GetMaxThreads pdwMaxWorkerThreads PDWORD
	cf GetAvailableThreads pdwAvailableWorkerThreads PDWORD
	cf SetMinThreads dwMinIOCompletionThreads DWORD
	cf GetMinThreads pdwMinIOCompletionThreads PDWORD
}

IU ICLRIoCompletionManager
{
	iid 2d74ce86-b8d6-4c84-b3a7-9768933b3c12
	cf OnComplete dwErrorCode DWORD NumberOfBytesTransferred DWORD pvOverlapped PVOID
}

IU IHostIoCompletionManager
{
	iid 8bde9d80-ec06-41d6-83e6-22580effcc20
	cf CreateIoCompletionPort phPort P.HANDLE
	cf CloseIoCompletionPort hPort HANDLE
	cf SetMaxThreads dwMaxIOCompletionThreads DWORD
	cf GetMaxThread pdwMaxIOCompletionThreads PDWORD
	cf GetAvailableThreads pdwMaxIOCompletionThreads PDWORD
	cf GetHostOverlappedSize pcbSize PDWORD
	cf SetCLRIoCompletionManager pManager P.ICLRIoCompletionManager
	cf InitializeHostOverlapped pvOverlapped PVOID
	cf Bind hPort HANDLE hHandle HANDLE
	cf SetMinThreads dwMinIOCompletionThreads DWORD
	cf GetMinThreads pdwMinIOCompletionThreads PDWORD
}

ed ESymbolReadingPolicy
{
	ee eSymbolReadingNever
	ee eSymbolReadingAlways
	ee eSymbolReadingFullTrustOnly
}

IU ICLRDebugManager
{
	iid 00DCAEC6-2AC0-43a9-ACF9-1E36C139B10D
	cf BeginConnection dwConnectionId CONNID szConnectionName LPWSTR
	cf SetConnectionTasks id CONNID dwCount DWORD ppCLRTask P.P.ICLRTask
	cf EndConnection dwConnectionId CONNID
	cf SetDacl pacl P.ACL
	cf GetDacl pacl P.ACL
	cf IsDebuggerAttached pbAttached PBOOL
	cf SetSymbolReadingPolicy policy ESymbolReadingPolicy
}

ed ECustomDumpFlavor
{
	ee DUMP_FLAVOR_Mini
	ee DUMP_FLAVOR_CriticalCLRState
	ee DUMP_FLAVOR_NonHeapCLRState
~DUMP_FLAVOR_DEFAULT = DUMP_FLAVOR_Mini
}

ed ECustomDumpItemKind
{
	ee DUMP_ITEM_None
}

sd CustomDumpItem
{
	sf ECustomDumpItemKind itemKind

~
~    @CUnion.make
~    class U(CUnion):
~        pReserved: IUIntPtr
~

	sf IAnonymous[U] _u
}

eq BucketParamsCount 10
eq BucketParamLength 255

ed BucketParameterIndex
{
	ee Parameter1
	ee Parameter2
	ee Parameter3
	ee Parameter4
	ee Parameter5
	ee Parameter6
	ee Parameter7
	ee Parameter8
	ee Parameter9
	ee InvalidBucketParamIndex
}

sd BucketParameters
{
	sf IBool fInited
	sf IArrayFixedSize[IWideChar,255] pszEventTypeName
	sf IArrayFixedSize[IArrayFixedSize[IWideChar,10],255] pszParams
}

IU ICLRErrorReportingManager
{
	iid 980D2F1A-BF79-4c08-812A-BB9778928F78
	cf GetBucketParametersForCurrentException pParams P.BucketParameters
	cf BeginCustomDump dwFlavor ECustomDumpFlavor dwNumItems DWORD items P.CustomDumpItem dwReserved DWORD
	cf EndCustomDump
}

IU IHostCrst
{
	iid 6DF710A6-26A4-4a65-8CD5-7237B8BDA8DC
	cf Enter option DWORD
	cf Leave
	cf TryEnter option DWORD pbSucceeded PBOOL
	cf SetSpinCount dwSpinCount DWORD
}

IU IHostAutoEvent
{
	iid 50B0CFCE-4063-4278-9673-E5CB4ED0BDB8
	cf Wait dwMilliseconds DWORD option DWORD
	cf Set
}

IU IHostManualEvent
{
	iid 1BF4EC38-AFFE-4fb9-85A6-525268F15B54
	cf Wait dwMilliseconds DWORD option DWORD
	cf Reset
	cf Set
}

IU IHostSemaphore
{
	iid 855efd47-cc09-463a-a97d-16acab882661
	cf Wait dwMilliseconds DWORD option DWORD
	cf ReleaseSemaphore lReleaseCount LONG lpPreviousCount PLONG
}

IU ICLRSyncManager
{
	iid 55FF199D-AD21-48f9-A16C-F24EBBB8727D
	cf GetMonitorOwner Cookie SIZE_T ppOwnerHostTask P.P.IHostTask
	cf CreateRWLockOwnerIterator Cookie SIZE_T pIterator P.SIZE_T
	cf GetRWLockOwnerNext Iterator SIZE_T ppOwnerHostTask P.P.IHostTask
	cf DeleteRWLockOwnerIterator Iterator SIZE_T
}

IU IHostSyncManager
{
	iid 234330c7-5f10-4f20-9615-5122dab7a0ac
	cf SetCLRSyncManager pManager P.ICLRSyncManager
	cf CreateCrst ppCrst P.P.IHostCrst
	cf CreateCrstWithSpinCount dwSpinCount DWORD ppCrst P.P.IHostCrst
	cf CreateAutoEvent ppEvent P.P.IHostAutoEvent
	cf CreateManualEvent bInitialState BOOL ppEvent P.P.IHostManualEvent
	cf CreateMonitorEvent Cookie SIZE_T ppEvent P.P.IHostAutoEvent
	cf CreateRWLockWriterEvent Cookie SIZE_T ppEvent P.P.IHostAutoEvent
	cf CreateRWLockReaderEvent bInitialState BOOL Cookie SIZE_T ppEvent P.P.IHostManualEvent
	cf CreateSemaphore dwInitial DWORD dwMax DWORD ppSemaphore P.P.IHostSemaphore
}

ed EClrOperation
{
	ee OPR_ThreadAbort
	ee OPR_ThreadRudeAbortInNonCriticalRegion
	ee OPR_ThreadRudeAbortInCriticalRegion
	ee OPR_AppDomainUnload
	ee OPR_AppDomainRudeUnload
	ee OPR_ProcessExit
	ee OPR_FinalizerRun
	ee MaxClrOperation
}

ed EClrFailure
{
	ee FAIL_NonCriticalResource
	ee FAIL_CriticalResource
	ee FAIL_FatalRuntime
	ee FAIL_OrphanedLock
	ee FAIL_StackOverflow
	ee FAIL_AccessViolation
	ee FAIL_CodeContract
	ee MaxClrFailure
}

ed EClrUnhandledException
{
	ee eRuntimeDeterminedPolicy
	ee eHostDeterminedPolicy
}

ed EPolicyAction
{
	ee eNoAction
	ee eThrowException
	ee eAbortThread
	ee eRudeAbortThread
	ee eUnloadAppDomain
	ee eRudeUnloadAppDomain
	ee eExitProcess
	ee eFastExitProcess
	ee eRudeExitProcess
	ee eDisableRuntime
	ee MaxPolicyAction 
}

IU ICLRPolicyManager
{
	iid 7D290010-D781-45da-A6F8-AA5D711A730E
	cf SetDefaultAction operation EClrOperation action EPolicyAction
	cf SetTimeout operation EClrOperation dwMilliseconds DWORD
	cf SetActionOnTimeout operation EClrOperation action EPolicyAction
	cf SetTimeoutAndAction operation EClrOperation dwMilliseconds DWORD action EPolicyAction
	cf SetActionOnFailure failure EClrFailure action EPolicyAction
	cf SetUnhandledExceptionPolicy policy EClrUnhandledException
}

IU IHostPolicyManager
{
	iid 7AE49844-B1E3-4683-BA7C-1E8212EA3B79
	cf OnDefaultAction operation EClrOperation action EPolicyAction
	cf OnTimeout operation EClrOperation action EPolicyAction
	cf OnFailure failure EClrFailure action EPolicyAction
}

ed EClrEvent
{
	ee Event_DomainUnload
	ee Event_ClrDisabled
	ee Event_MDAFired
	ee Event_StackOverflow
	ee MaxClrEvent
}

sd MDAInfo
{
	sf LPCWSTR lpMDACaption
	sf LPCWSTR lpMDAMessage
	sf LPCWSTR lpStackTrace
}

ed StackOverflowType
{
	ee SO_Managed
	ee SO_ClrEngine
	ee SO_Other
}

sd StackOverflowInfo
{
	sf IInteger[StackOverflowType] soType
	sf IPointer[EXCEPTION_POINTERS] pExceptionInfo
}

IU IActionOnCLREvent
{
	iid 607BE24B-D91B-4E28-A242-61871CE56E35
	cf OnEvent event EClrEvent data PVOID
}

IU ICLROnEventManager
{
	iid 1D0E0132-E64F-493D-9260-025C0E32C175
	cf RegisterActionOnEvent event EClrEvent pAction P.IActionOnCLREvent
	cf UnregisterActionOnEvent event EClrEvent pAction P.IActionOnCLREvent
}

IU IHostGCManager
{
	iid 5D4EC34E-F248-457B-B603-255FAABA0D21
	cf ThreadIsBlockingForSuspension
	cf SuspensionStarting
	cf SuspensionEnding Generation DWORD
}

IU ICLRAssemblyReferenceList
{
	iid 1b2c9750-2e66-4bda-8b44-0a642c5cd733
	cf IsStringAssemblyReferenceInList pwzAssemblyName LPCWSTR
	cf IsAssemblyReferenceInList pName P.IUnknown
}

IU ICLRReferenceAssemblyEnum
{
	iid d509cb5d-cf32-4876-ae61-67770cf91973
	cf Get dwIndex DWORD pwzBuffer LPWSTR pcchBufferSize PDWORD
}

IU ICLRProbingAssemblyEnum
{
	iid d0c5fb1f-416b-4f97-81f4-7ac7dc24dd5d
	cf Get dwIndex DWORD pwzBuffer LPWSTR pcchBufferSize PDWORD
}

ed ECLRAssemblyIdentityFlags
{
	ee CLR_ASSEMBLY_IDENTITY_FLAGS_DEFAULT
}

IU ICLRAssemblyIdentityManager
{
	iid 15f0a9da-3ff6-4393-9da9-fdfd284e6972
	cf GetCLRAssemblyReferenceList ppwzAssemblyReferences P.LPCWSTR dwNumOfReferences DWORD ppReferenceList P.P.ICLRAssemblyReferenceList
	cf GetBindingIdentityFromFile pwzFilePath LPCWSTR dwFlags DWORD pwzBuffer LPWSTR pcchBufferSize PDWORD
	cf GetBindingIdentityFromStream pStream P.IStream dwFlags DWORD pwzBuffer LPWSTR pcchBufferSize PDWORD
	cf GetReferencedAssembliesFromFile pwzFilePath LPCWSTR dwFlags DWORD pExcludeAssembliesList P.ICLRAssemblyReferenceList ppReferenceEnum P.P.ICLRReferenceAssemblyEnum
	cf GetReferencedAssembliesFromStream pStream P.IStream dwFlags DWORD pExcludeAssembliesList P.ICLRAssemblyReferenceList ppReferenceEnum P.P.ICLRReferenceAssemblyEnum
	cf GetProbingAssembliesFromReference dwMachineType DWORD dwFlags DWORD pwzReferenceIdentity LPCWSTR ppProbingAssemblyEnum P.P.ICLRProbingAssemblyEnum
	cf IsStronglyNamed pwzAssemblyIdentity LPCWSTR pbIsStronglyNamed PBOOL
}

ed EHostBindingPolicyModifyFlags
{
	ee HOST_BINDING_POLICY_MODIFY_DEFAULT
	ee HOST_BINDING_POLICY_MODIFY_CHAIN
	ee HOST_BINDING_POLICY_MODIFY_REMOVE
	ee HOST_BINDING_POLICY_MODIFY_MAX
}

IU ICLRHostBindingPolicyManager
{
	iid 4b3545e7-1856-48c9-a8ba-24b21a753c09
	cf ModifyApplicationPolicy pwzSourceAssemblyIdentity LPCWSTR pwzTargetAssemblyIdentity LPCWSTR pbApplicationPolicy PBYTE cbAppPolicySize DWORD dwPolicyModifyFlags DWORD pbNewApplicationPolicy PBYTE pcbNewAppPolicySize PDWORD
	cf EvaluatePolicy pwzReferenceIdentity LPCWSTR pbApplicationPolicy PBYTE cbAppPolicySize DWORD pwzPostPolicyReferenceIdentity LPWSTR pcchPostPolicyReferenceIdentity PDWORD pdwPoliciesApplied PDWORD
}

IU ICLRGCManager
{
	iid 54D9007E-A8E2-4885-B7BF-F998DEEE4F2A
	cf Collect Generation LONG
	cf GetStats pStats P.COR_GC_STATS
	cf SetGCStartupLimits SegmentSize DWORD MaxGen0Size DWORD
}

I ICLRGCManager2 ex ICLRGCManager
{
	iid 0603B793-A97A-4712-9CB4-0CD1C74C0F7C
	cf SetGCStartupLimitsEx SegmentSize SIZE_T MaxGen0Size SIZE_T
}

ed EBindPolicyLevels
{
	ee ePolicyLevelNone
	ee ePolicyLevelRetargetable 0x1
	ee ePolicyUnifiedToCLR 0x2
	ee ePolicyLevelApp 0x4
	ee ePolicyLevelPublisher 0x8
	ee ePolicyLevelHost 0x10
	ee ePolicyLevelAdmin 0x20
	ee ePolicyPortability 0x40
}

sd AssemblyBindInfo
{
	sf IDword dwAppDomainId
	sf LPCWSTR lpReferencedIdentity
	sf LPCWSTR lpPostPolicyIdentity
	sf IDword ePolicyLevel
}

sd ModuleBindInfo
{
	sf IDword dwAppDomainId
	sf LPCWSTR lpAssemblyIdentity
	sf LPCWSTR lpModuleName
}

ed EHostApplicationPolicy
{
	ee HOST_APPLICATION_BINDING_POLICY 1
}

IU IHostAssemblyStore
{
	iid 7b102a88-3f7f-496d-8fa2-c35374e01af3
	cf ProvideAssembly pBindInfo P.AssemblyBindInfo pAssemblyId P.UINT64 pContext P.UINT64 ppStmAssemblyImage P.P.IStream ppStmPDB P.P.IStream
	cf ProvideModule pBindInfo P.ModuleBindInfo pdwModuleId PDWORD ppStmModuleImage P.P.IStream ppStmPDB P.P.IStream
}

IU IHostAssemblyManager
{
	iid 613dabd7-62b2-493e-9e65-c1e32a1e0c5e
	cf GetNonHostStoreAssemblies ppReferenceList P.P.ICLRAssemblyReferenceList
	cf GetAssemblyStore ppAssemblyStore P.P.IHostAssemblyStore
}

ff mscoree.GetCLRIdentityManager HRESULT riid R.IID ppManager P.P.IUnknown

IU IHostControl
{
	iid 02CA073C-7079-4860-880A-C2F7A449C991
	cf GetHostManager riid R.IID ppObject P.PVOID
	cf SetAppDomainManager dwAppDomainId DWORD pUnkAppDomainManager P.IUnknown
}

IU ICLRControl
{
	iid 9065597E-D1A1-4fb2-B6BA-7E1FCE230F61
	cf GetCLRManager riid R.IID ppObject P.PVOID
	cf SetAppDomainManagerType pwzAppDomainManagerAssembly LPCWSTR pwzAppDomainManagerType LPCWSTR
}

IU ICLRRuntimeHost
{
	iid 90F1A06C-7712-4762-86B5-7A5EBA6BDB02
	cf Start
	cf Stop
	cf SetHostControl pHostControl P.IHostControl
	cf GetCLRControl pCLRControl P.P.ICLRControl
	cf UnloadAppDomain dwAppDomainId DWORD fWaitUntilDone BOOL
	cf ExecuteInAppDomain dwAppDomainId DWORD pCallback FExecuteInAppDomainCallback cookie PVOID
	cf GetCurrentAppDomainId pdwAppDomainId PDWORD
	cf ExecuteApplication pwzAppFullName LPCWSTR dwManifestPaths DWORD ppwzManifestPaths P.LPCWSTR dwActivationData DWORD ppwzActivationData P.LPCWSTR pReturnValue PINT
	cf ExecuteInDefaultAppDomain pwzAssemblyPath LPCWSTR pwzTypeName LPCWSTR pwzMethodName LPCWSTR pwzArgument LPCWSTR pReturnValue PDWORD
}

ed EApiCategories
{
	ee eNoChecks
	ee eSynchronization 0x1
	ee eSharedState 0x2
	ee eExternalProcessMgmt 0x4
	ee eSelfAffectingProcessMgmt 0x8
	ee eExternalThreading 0x10
	ee eSelfAffectingThreading 0x20
	ee eSecurityInfrastructure 0x40
	ee eUI 0x80
	ee eMayLeakOnAbort 0x100
	ee eAll 0x1ff
}

IU ICLRHostProtectionManager
{
	iid 89F25F5C-CEEF-43e1-9CFA-A68CE863AAAC
	cf SetProtectedCategories categories EApiCategories
	cf SetEagerSerializeGrantSets
}

ed EInitializeNewDomainFlags
{
	ee eInitializeNewDomainFlags_None
	ee eInitializeNewDomainFlags_NoSecurityChanges 2
}

IU ICLRDomainManager
{
	iid 270D00A2-8E15-4d0b-ADEB-37BC3E47DF77
	cf SetAppDomainManagerType wszAppDomainManagerAssembly LPCWSTR wszAppDomainManagerType LPCWSTR dwInitializeDomainFlags EInitializeNewDomainFlags
	cf SetPropertiesForDefaultAppDomain nProperties DWORD pwszPropertyNames P.LPCWSTR pwszPropertyValues P.LPCWSTR
}

IU ITypeName
{
	iid B81FF171-20F3-11d2-8DCC-00A0C9B00522
	cf GetNameCount pCount PDWORD
	cf GetNames count DWORD rgbszNames P.BSTR pCount PDWORD
	cf GetTypeArgumentCount pCount PDWORD
	cf GetTypeArguments count DWORD rgpArguments FD.P.P.ITypeName pCount PDWORD
	cf GetModifierLength pCount PDWORD
	cf GetModifiers count DWORD rgModifiers PDWORD pCount PDWORD
	cf GetAssemblyName rgbszAssemblyNames P.BSTR
}

IU ITypeNameBuilder
{
	iid B81FF171-20F3-11d2-8DCC-00A0C9B00523
	cf OpenGenericArguments
	cf CloseGenericArguments
	cf OpenGenericArgument
	cf CloseGenericArgument
	cf AddName szName LPCWSTR
	cf AddPointer
	cf AddByRef
	cf AddSzArray
	cf AddArray rank DWORD
	cf AddAssemblySpec szAssemblySpec LPCWSTR
	cf ToString pszStringRepresentation P.BSTR
	cf Clear
}

IU ITypeNameFactory
{
	iid B81FF171-20F3-11d2-8DCC-00A0C9B00521
	cf ParseTypeName szName LPCWSTR pError PDWORD ppTypeName P.P.ITypeName
	cf GetTypeNameBuilder ppTypeBuilder P.P.ITypeNameBuilder
}

IU IApartmentCallback
{
	iid 178E5337-1528-4591-B1C9-1C6E484686D8
	cf DoCallback pFunc SIZE_T pData SIZE_T
}

IU IManagedObject
{
	iid C3FCC19E-A970-11d2-8B5A-00A0C9B7C9C4
	cf GetSerializedBuffer pBSTR P.BSTR
	cf GetObjectIdentity pBSTRGUID P.BSTR pAppDomainID PINT pCCW PINT
}

IU ICatalogServices
{
	iid 04C6BE1E-1DB1-4058-AB7A-700CCCFBF254
	cf Autodone
	cf NotAutodone
}

C ComCallUnmarshal
{
	clsid 3F281000-E95A-11d2-886B-00C04F869F04
}

C ComCallUnmarshalV4
{
	clsid 45FB4600-E6E8-4928-B25E-50476FF79425
}

C CorRuntimeHost
{
	clsid CB2F6723-AB3A-11d2-9C40-00C04FA30A3E
}

C CLRRuntimeHost
{
	clsid 90F1A06E-7712-4762-86B5-7A5EBA6BDB02
}

C TypeNameFactory
{
	clsid B81FF171-20F3-11d2-8DCC-00A0C9B00525
}

ed EContextType
{
	ee eCurrentContext
	ee eRestrictedContext
}

IU IHostSecurityContext
{
	iid 7E573CE4-0343-4423-98D7-6318348A1D3C
	cf Capture ppClonedContext FD.P.P.IHostSecurityContext
}

IU IHostSecurityManager
{
	iid 75ad2468-a349-4d02-a764-76a68aee0c4f
	cf ImpersonateLoggedOnUser hToken HANDLE
	cf RevertToSelf
	cf OpenThreadToken dwDesiredAccess DWORD bOpenAsSelf BOOL phThreadToken P.HANDLE
	cf SetThreadToken hToken HANDLE
	cf GetSecurityContext eContextType EContextType ppSecurityContext P.P.IHostSecurityContext
	cf SetSecurityContext eContextType EContextType pSecurityContext P.IHostSecurityContext
}

IU ICLRAppDomainResourceMonitor
{
	iid c62de18c-2e23-4aea-8423-b40c1fc59eae
	cf GetCurrentAllocated dwAppDomainId DWORD pBytesAllocated P.ULONGLONG
	cf GetCurrentSurvived dwAppDomainId DWORD pAppDomainBytesSurvived P.ULONGLONG pTotalBytesSurvived P.ULONGLONG
	cf GetCurrentCpuTime dwAppDomainId DWORD pMilliseconds P.ULONGLONG
}