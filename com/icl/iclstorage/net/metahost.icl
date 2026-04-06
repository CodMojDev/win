.icl
.ver 100
.gencomment

silent
{
	pie CLSID LPCLSID
}

al int INT32 ULONG64 BOOLEAN

~
~from .mscoree import *
~

ff mscoree.CLRCreateInstance rclsid R.CLSID riid R.IID ppInterface P.PVOID

dcl CLSID_CLRStrongName 0xB79B0ACD 0xF5CD 0x409b 0xB5 0xA5 0xA1 0x62 0x44 0x61 0x0B 0x92
dii IID_ICLRMetaHost 0xD332DB9E 0xB9B3 0x4125 0x82 0x07 0xA1 0x48 0x84 0xF5 0x32 0x16
dcl CLSID_CLRMetaHost 0x9280188d 0xe8e 0x4867 0xb3 0xc 0x7f 0xa8 0x38 0x84 0xe8 0xde
dii IID_ICLRMetaHostPolicy 0xE2190695 0x77B2 0x492e 0x8E 0x14 0xC4 0xB3 0xA7 0xFD 0xD5 0x93
dcl CLSID_CLRMetaHostPolicy 0x2ebcd49a 0x1b47 0x4a61 0xb1 0x3a 0x4a 0x3 0x70 0x1e 0x59 0x4b
dii IID_ICLRDebugging 0xd28f3c5a 0x9634 0x4206 0xa5 0x9 0x47 0x75 0x52 0xee 0xfb 0x10
dcl CLSID_CLRDebugging 0xbacc578d 0xfbdd 0x48a4 0x96 0x9f 0x2 0xd9 0x32 0xb7 0x46 0x34
dii IID_ICLRRuntimeInfo 0xBD39D1D2 0xBA2F 0x486a 0x89 0xB0 0xB4 0xB0 0xCB 0x46 0x68 0x91
dii IID_ICLRStrongName 0x9FD93CCF 0x3280 0x4391 0xB3 0xA9 0x96 0xE1 0xCD 0xE7 0x7C 0x8D
dii IID_ICLRStrongName2 0xC22ED5C5 0x4B59 0x4975 0x90 0xEB 0x85 0xEA 0x55 0xC0 0x06 0x9B
dii IID_ICLRStrongName3 0x22c7089b 0xbbd3 0x414a 0xb6 0x98 0x21 0x0f 0x26 0x3f 0x1f 0xed
dcl CLSID_CLRDebuggingLegacy 0xDF8395B5 0xA4BA 0x450b 0xA7 0x7C 0xA9 0xA4 0x77 0x62 0xC5 0x20
dcl CLSID_CLRProfiling 0xbd097ed8 0x733e 0x43fe 0x8e 0xd7 0xa9 0x5f 0xf9 0xa8 0x44 0x8c
dii IID_ICLRProfiling 0xb349abe3 0xb56f 0x4689 0xbf 0xcd 0x76 0xbf 0x39 0xd8 0x88 0xea
dii IID_ICLRDebuggingLibraryProvider 0x3151c08d 0x4d09 0x4f9b 0x88 0x38 0x28 0x80 0xbf 0x18 0xfe 0x51

~
~CLRCreateInstanceFnPtr = WINAPI(HRESULT, REFCLSID, REFIID, PVOID)
~CreateInterfaceFnPtr = WINAPI(HRESULT, REFCLSID, REFIID, PVOID)
~CallbackThreadSetFnPtr = WINAPI(HRESULT)
~CallbackThreadUnsetFnPtr = WINAPI(HRESULT)
~RuntimeLoadedCallbackFnPtr = WINAPI(PVOID, CallbackThreadSetFnPtr, CallbackThreadUnsetFnPtr)
~

al FARPROC CLRCreateInstanceFnPtr CreateInterfaceFnPtr CallbackThreadSetFnPtr CallbackThreadUnsetFnPtr RuntimeLoadedCallbackFnPtr

IU ICLRMetaHost
{
	iid D332DB9E-B9B3-4125-8207-A14884F53216
	cf GetRuntime pwzVersion LPCWSTR riid R.IID ppRuntime P.PVOID
	cf GetVersionFromFile pwzFilePath LPCWSTR pwzBuffer LPWSTR pcchBuffer PDWORD
	cf EnumerateInstalledRuntimes ppEnumerator P.P.IEnumUnknown
	cf EnumerateLoadedRuntimes hndProcess HANDLE ppEnumerator P.P.IEnumUnknown
	cf RequestRuntimeLoadedNotification pCallbackFunction RuntimeLoadedCallbackFnPtr
	cf QueryLegacyV2RuntimeBinding riid R.IID ppUnk P.PVOID
	cf ExitProcess iExitCode INT32
}

ed METAHOST_POLICY_FLAGS
{
	ee METAHOST_POLICY_HIGHCOMPAT
	ee METAHOST_POLICY_APPLY_UPGRADE_POLICY 0x8
	ee METAHOST_POLICY_EMULATE_EXE_LAUNCH 0x10
	ee METAHOST_POLICY_SHOW_ERROR_DIALOG 0x20
	ee METAHOST_POLICY_USE_PROCESS_IMAGE_PATH 0x40
	ee METAHOST_POLICY_ENSURE_SKU_SUPPORTED 0x80
	ee METAHOST_POLICY_IGNORE_ERROR_MODE 0x1000
}

ed METAHOST_CONFIG_FLAGS
{
	ee METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_UNSET
	ee METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_TRUE
	ee METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_FALSE
	ee METAHOST_CONFIG_FLAGS_LEGACY_V2_ACTIVATION_POLICY_MASK
}

IU ICLRMetaHostPolicy
{
	iid E2190695-77B2-492e-8E14-C4B3A7FDD593
	cf GetRequestedRuntime dwPolicyFlags METAHOST_POLICY_FLAGS pwzBinary LPCWSTR pCfgStream P.IStream pwzVersion LPWSTR pcchVersion PDWORD pwzImageVersion LPWSTR pcchImageVersion PDWORD pdwConfigFlags PDWORD riid R.IID ppRuntime P.PVOID
}

IU ICLRProfiling
{
	iid B349ABE3-B56F-4689-BFCD-76BF39D888EA
	cf AttachProfiler dwProfileeProcessID DWORD dwMillisecondsMax DWORD pClsidProfiler P.CLSID wszProfilerPath LPCWSTR pvClientData PVOID cbClientData UINT
}

sd CLR_DEBUGGING_VERSION
{
	sf IWord wStructVersion
	sf IWord wMajor
	sf IWord wMinor
	sf IWord wBuild
	sf IWord wRevision
}

ed CLR_DEBUGGING_PROCESS_FLAGS
{
	ee CLR_DEBUGGING_MANAGED_EVENT_PENDING 1
	ee CLR_DEBUGGING_MANAGED_EVENT_DEBUGGER_LAUNCH
}

IU ICLRDebuggingLibraryProvider
{
	iid 3151C08D-4D09-4f9b-8838-2880BF18FE51
	cf ProvideLibrary pwszFileName LPCWSTR dwTimestamp DWORD dwSizeOfImage DWORD phModule P.HANDLE
}

IU ICLRDebugging
{
	iid D28F3C5A-9634-4206-A509-477552EEFB10
	cf OpenVirtualProcess moduleBaseAddress ULONG64 pDataTarget P.IUnknown pLibraryProvider P.ICLRDebuggingLibraryProvider pMaxDebuggerSupportedVersion P.CLR_DEBUGGING_VERSION riidProcess P.IID ppProcess P.P.IUnknown pVersion P.CLR_DEBUGGING_VERSION pdwFlags P.CLR_DEBUGGING_PROCESS_FLAGS
	cf CanUnloadNow hModule HMODULE
}

IU ICLRRuntimeInfo
{
	iid BD39D1D2-BA2F-486a-89B0-B4B0CB466891
	cf GetVersionString pwzBuffer LPWSTR pcchBuffer PDWORD
	cf GetRuntimeDirectory pwzBuffer LPWSTR pcchBuffer PDWORD
	cf IsLoaded hndProcess HANDLE pbLoaded PBOOL
	cf LoadErrorString iResourceID UINT pwzBuffer LPWSTR pcchBuffer PDWORD iLocaleID LONG
	cf LoadLibrary pwzDllName LPCWSTR phndModule P.HMODULE
	cf GetProcAddress pszProcName LPCSTR ppProc P.PVOID
	cf GetInterface rclsid R.CLSID riid R.IID ppUnk P.PVOID
	cf IsLoadable pbLoadable PBOOL
	cf SetDefaultStartupFlags dwStartupFlags DWORD pwzHostConfigFile LPCWSTR
	cf GetDefaultStartupFlags pdwStartupFlags PDWORD pwzHostConfigFile LPWSTR pcchHostConfigFile PDWORD
	cf BindAsLegacyV2Runtime
	cf IsStarted pbStarted PBOOL pdwStartupFlags PDWORD
}

IU ICLRStrongName
{
	iid 9FD93CCF-3280-4391-B3A9-96E1CDE77C8D
	cf GetHashFromAssemblyFile pszFilePath LPCSTR piHashAlg PUINT pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf GetHashFromAssemblyFileW pwzFilePath LPCWSTR piHashAlg PUINT pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf GetHashFromBlob pbBlob PBYTE cchBlob DWORD piHashAlg PUINT pbHash PBYTE pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf GetHashFromFile pszFilePath LPCSTR piHashAlg PUINT pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf GetHashFromFileW pszFilePath LPCWSTR piHashAlg PUINT pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf GetHashFromHandle hFile HANDLE piHashAlg PUINT pbHash PBYTE cchHash DWORD pchHash PDWORD
	cf StrongNameCompareAssemblies pwzAssembly1 LPCWSTR pwzAssembly2 LPCWSTR pdwResult PDWORD
	cf StrongNameFreeBuffer pbMemory PBYTE
	cf StrongNameGetBlob pwzFilePath LPCWSTR pbBlob PBYTE pcbBlob PDWORD
	cf StrongNameGetBlobFromImage pbBase PBYTE dwLength DWORD pbBlob PBYTE pcbBlob PDWORD
	cf StrongNameGetPublicKey pwzKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG ppbPublicKeyBlob P.PBYTE pcbPublicKeyBlob PULONG
	cf StrongNameHashSize ulHashAlg ULONG pcbSize PDWORD
	cf StrongNameKeyDelete pwzKeyContainer LPCWSTR
	cf StrongNameKeyGen pwzKeyContainer LPCWSTR dwFlags DWORD ppbKeyBlob P.PBYTE pcbKeyBlob PULONG
	cf StrongNameKeyGenEx pwzKeyContainer LPCWSTR dwFlags DWORD dwKeySize DWORD ppbKeyBlob P.PBYTE pcbKeyBlob PULONG
	cf StrongNameKeyInstall pwzKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG
	cf StrongNameSignatureGeneration pwzFilePath LPCWSTR pwzKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG ppbSignatureBlob P.PBYTE pcbSignatureBlob PULONG
	cf StrongNameSignatureGenerationEx wszFilePath LPCWSTR wszKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG ppbSignatureBlob P.PBYTE pcbSignatureBlob PULONG dwFlags DWORD
	cf StrongNameSignatureSize pbPublicKeyBlob PBYTE cbPublicKeyBlob ULONG pcbSize PDWORD
	cf StrongNameSignatureVerification pwzFilePath LPCWSTR dwInFlags DWORD pdwOutFlags PDWORD
	cf StrongNameSignatureVerificationEx pwzFilePath LPCWSTR fForceVerification BOOLEAN pfWasVerified P.BOOLEAN
	cf StrongNameSignatureVerificationFromImage pbBase PBYTE dwLength DWORD dwInFlags DWORD pdwOutFlags PDWORD
	cf StrongNameTokenFromAssembly pwzFilePath LPCWSTR ppbStrongNameToken P.PBYTE pcbStrongNameToken PULONG
	cf StrongNameTokenFromAssembly pwzFilePath LPCWSTR ppbStrongNameToken P.PBYTE pcbStrongNameToken PULONG ppbPublicKeyBlob P.PBYTE pcbPublicKeyBlob PULONG
	cf StrongNameTokenFromPublicKey pbPublicKeyBlob PBYTE cbPublicKeyBlob ULONG ppbStrongNameToken P.PBYTE pcbStrongNameToken PULONG
}

IU ICLRStrongName2
{
	iid C22ED5C5-4B59-4975-90EB-85EA55C0069B
	cf StrongNameGetPublicKeyEx pwzKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG ppbPublicKeyBlob P.PBYTE pcbPublicKeyBlob PULONG uHashAlgId ULONG uReserved ULONG
	cf StrongNameSignatureVerificationEx2 wszFilePath LPCWSTR fForceVerification BOOLEAN pbEcmaPublicKey PBYTE cbEcmaPublicKey DWORD pfWasVerified P.BOOLEAN
}

IU ICLRStrongName3
{
	iid 22c7089b-bbd3-414a-b698-210f263f1fed
	cf StrongNameDigestGenerate wszFilePath LPCWSTR ppbDigestBlob P.PBYTE pcbDigestBlob PULONG dwFlags DWORD
	cf StrongNameDigestSign wszKeyContainer LPCWSTR pbKeyBlob PBYTE cbKeyBlob ULONG pbDigestBlob PBYTE cbDigestBlob ULONG hashAlgId DWORD ppbSignatureBlob P.PBYTE pcbSignatureBlob PULONG dwFlags DWORD
	cf StrongNameDigestEmbed wszFilePath LPCWSTR pbSignatureBlob PBYTE cbSignatureBlob ULONG
}