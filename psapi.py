from . import cpreproc

from .defbase import *

from .minwindef import *

from typing import (Callable)

if cpreproc.pragma_once("_PSAPI_H_"):
    kernelbase = W_WinDLL("kernelbase.dll")

    EnumProcesses = declare(kernelbase.EnumProcesses, BOOL, PDWORD, DWORD, LPDWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    EnumProcessModules = declare(kernelbase.EnumProcessModules, BOOL, HANDLE, POINTER(HMODULE), DWORD, LPDWORD)
    EnumProcessModulesEx = declare(kernelbase.EnumProcessModulesEx, BOOL, HANDLE, POINTER(HMODULE), DWORD, LPDWORD, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetModuleBaseNameA = declare(kernelbase.GetModuleBaseNameA, DWORD, HANDLE, HMODULE, LPSTR, DWORD)
    GetModuleBaseNameW = declare(kernelbase.GetModuleBaseNameW, DWORD, HANDLE, HMODULE, LPWSTR, DWORD)
    GetModuleBaseName = unicode(GetModuleBaseNameW, GetModuleBaseNameA)
    GetModuleFileNameExA = declare(kernelbase.GetModuleFileNameExA, DWORD, HANDLE, HMODULE, LPSTR, DWORD)
    GetModuleFileNameExW = declare(kernelbase.GetModuleFileNameExW, DWORD, HANDLE, HMODULE, LPWSTR, DWORD)
    GetModuleFileNameEx = unicode(GetModuleFileNameExW, GetModuleFileNameExA)
    # !UNICODE

    class MODULEINFO(CStructure):
        _fields_ = [
            ("lpBaseOfDll", LPVOID),
            ("SizeOfImage", DWORD),
            ("EntryPoint", LPVOID)
        ]
        
        lpBaseOfDll: LPVOID
        EntryPoint: LPVOID
        
        SizeOfImage: int
        
    LPMODULEINFO = POINTER(MODULEINFO)

    GetModuleInformation = declare(kernelbase.GetModuleInformation, BOOL, HANDLE, HMODULE, LPMODULEINFO, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    EmptyWorkingSet = declare(kernelbase.EmptyWorkingSet, BOOL, HANDLE)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    #
    # Working set information structures. All non-specified bits are reserved.
    #

    class PSAPI_WORKING_SET_BLOCK(Union):
        class _DUMMYSTRUCTNAME(CStructure):
            _fields_ = [
                ("Protection", ULONG_PTR, 5),
                ("ShareCount", ULONG_PTR, 3),
                ("Shared", ULONG_PTR, 1),
                ("Reserved", ULONG_PTR, 3),
                ("VirtualPage", ULONG_PTR, 52 if cpreproc.ifdef("_WIN64") else 20)
            ]
        _fields_ = [
            ("Flags", ULONG_PTR),
            ("s", _DUMMYSTRUCTNAME)
        ]
        
        VirtualPage: int
        Protection: int
        ShareCount: int
        Shared: int
        Flags: int
        
    PPSAPI_WORKING_SET_BLOCK = POINTER(PSAPI_WORKING_SET_BLOCK)

    class PSAPI_WORKING_SET_INFORMATION(CStructure):
        _fields_ = [
            ("NumberOfEntries", ULONG_PTR)
        ]
        
        WorkingSetInfo: IPointer[PSAPI_WORKING_SET_BLOCK]
        NumberOfEntries: int
        
    array_after_structure(PSAPI_WORKING_SET_BLOCK, 'WorkingSetInfo', 
                          PSAPI_WORKING_SET_BLOCK)
    PPSAPI_WORKING_SET_INFORMATION = POINTER(PSAPI_WORKING_SET_INFORMATION)

    class PSAPI_WORKING_SET_EX_BLOCK(Union):
        class _DUMMYUNIONNAME(Union):
            class _DUMMYSTRUCTNAME(CStructure):
                _prefields_ = [
                    ("Valid", ULONG_PTR, 1),
                    ("ShareCount", ULONG_PTR, 3),
                    ("Win32Protection", ULONG_PTR, 11),
                    ("Shared", ULONG_PTR, 1),
                    ("Node", ULONG_PTR, 6),
                    ("Locked", ULONG_PTR, 1),
                    ("LargePage", ULONG_PTR, 1),
                    ("Reserved", ULONG_PTR, 7),
                    ("Bad", ULONG_PTR, 1)
                ]
                if cpreproc.ifdef("_WIN64"):
                    _prefields_.append(("ReservedUlong", ULONG_PTR, 32))
                _fields_ = _prefields_
                del _prefields_
                
            class _DUMMYSTRUCTNAME2(CStructure):
                _prefields_ = [
                    ("Valid", ULONG_PTR, 1), # Valid = 0 in this format.
                    ("Reserved0", ULONG_PTR, 14),
                    ("Shared", ULONG_PTR, 1),
                    ("Reserved1", ULONG_PTR, 15),
                    ("Bad", ULONG_PTR, 1)
                ]
                if cpreproc.ifdef("_WIN64"):
                    _prefields_.append(("ReservedUlong", ULONG_PTR, 32))
                _fields_ = _prefields_
                del _prefields_
            _fields_ = [
                ("s", _DUMMYSTRUCTNAME),
                ("Invalid", _DUMMYSTRUCTNAME2)
            ]
        _fields_ = [
            ("Flags", ULONG_PTR),
            ("u", _DUMMYUNIONNAME)
        ]
        
    PPSAPI_WORKING_SET_EX_BLOCK = POINTER(PSAPI_WORKING_SET_EX_BLOCK)

    class PSAPI_WORKING_SET_EX_INFORMATION(CStructure):
        _fields_ = [
            ("VirtualAddress", PVOID),
            ("VirtualAttributes", PSAPI_WORKING_SET_EX_BLOCK)
        ]
        
        VirtualAttributes: PSAPI_WORKING_SET_EX_BLOCK
        VirtualAddress: PVOID
        
    PPSAPI_WORKING_SET_EX_INFORMATION = POINTER(PSAPI_WORKING_SET_EX_INFORMATION)

    QueryWorkingSet = declare(kernelbase.QueryWorkingSet, BOOL, HANDLE, PVOID, DWORD)
    QueryWorkingSetEx = declare(kernelbase.QueryWorkingSetEx, BOOL, HANDLE, PVOID, DWORD)
    InitializeProcessForWsWatch = declare(kernelbase.InitializeProcessForWsWatch, BOOL, HANDLE)

    class PSAPI_WS_WATCH_INFORMATION(CStructure):
        _fields_ = [
            ("FaultingPc", LPVOID),
            ("FaultingVa", LPVOID)
        ]
        
        FaultingPc: LPVOID
        FaultingVa: LPVOID
        
    PPSAPI_WS_WATCH_INFORMATION = POINTER(PSAPI_WS_WATCH_INFORMATION)

    class PSAPI_WS_WATCH_INFORMATION_EX(CStructure):
        _fields_ = [
            ("BasicInfo", PSAPI_WS_WATCH_INFORMATION),
            ("FaultingThreadId", ULONG_PTR),
            ("Flags", ULONG_PTR) # Reserved
        ]
        
        BasicInfo: PSAPI_WS_WATCH_INFORMATION
        FaultingThreadId: int
        Flags: int
        
    GetWsChanges = declare(kernelbase.GetWsChanges, BOOL, HANDLE, DWORD)
    GetWsChangesEx = declare(kernelbase.GetWsChangesEx, BOOL, HANDLE, PDWORD)
    GetMappedFileNameW = declare(kernelbase.GetMappedFileNameW, DWORD, HANDLE, LPVOID, LPWSTR, DWORD)
    GetMappedFileNameA = declare(kernelbase.GetMappedFileNameA, DWORD, HANDLE, LPVOID, LPSTR, DWORD)
    GetMappedFileName = unicode(GetMappedFileNameW, GetMappedFileNameA)
    EnumDeviceDrivers = declare(kernelbase.EnumDeviceDrivers, BOOL, PLPVOID, DWORD, LPDWORD)
    GetDeviceDriverBaseNameA = declare(kernelbase.GetDeviceDriverBaseNameA, DWORD, LPVOID, LPSTR, DWORD)
    GetDeviceDriverBaseNameW = declare(kernelbase.GetDeviceDriverBaseNameW, DWORD, LPVOID, LPWSTR, DWORD)
    GetDeviceDriverBaseName = unicode(GetDeviceDriverBaseNameW, GetDeviceDriverBaseNameA)
    # !UNICODE
    GetDeviceDriverFileNameA = declare(kernelbase.GetDeviceDriverFileNameA, DWORD, LPVOID, LPSTR, DWORD)
    GetDeviceDriverFileNameW = declare(kernelbase.GetDeviceDriverFileNameW, DWORD, LPVOID, LPWSTR, DWORD)
    GetDeviceDriverFileName = unicode(GetDeviceDriverFileNameW, GetDeviceDriverFileNameA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    # Structure for GetProcessMemoryInfo()

    class PROCESS_MEMORY_COUNTERS(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("PageFaultCount", DWORD),
            ("PeakWorkingSetSize", SIZE_T),
            ("WorkingSetSize", SIZE_T),
            ("QuotaPeakPagedPoolUsage", SIZE_T),
            ("QuotaPagedPoolUsage", SIZE_T),
            ("QuotaPeakNonPagedPoolUsage", SIZE_T),
            ("QuotaNonPagedPoolUsage", SIZE_T),
            ("PagefileUsage", SIZE_T),
            ("PeakPagefileUsage", SIZE_T)
        ]
        
        QuotaPeakNonPagedPoolUsage: int
        QuotaPeakPagedPoolUsage: int
        QuotaNonPagedPoolUsage: int
        QuotaPagedPoolUsage: int
        PeakWorkingSetSize: int
        PeakPagefileUsage: int
        WorkingSetSize: int
        PageFaultCount: int
        cb: int
        
    PPROCESS_MEMORY_COUNTERS = POINTER(PROCESS_MEMORY_COUNTERS)

    class PROCESS_MEMORY_COUNTERS_EX(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("PageFaultCount", DWORD),
            ("PeakWorkingSetSize", SIZE_T),
            ("WorkingSetSize", SIZE_T),
            ("QuotaPeakPagedPoolUsage", SIZE_T),
            ("QuotaPagedPoolUsage", SIZE_T),
            ("QuotaPeakNonPagedPoolUsage", SIZE_T),
            ("QuotaNonPagedPoolUsage", SIZE_T),
            ("PagefileUsage", SIZE_T),
            ("PeakPagefileUsage", SIZE_T),
            ("PrivateUsage", SIZE_T)
        ]
        
        QuotaPeakNonPagedPoolUsage: int
        QuotaPeakPagedPoolUsage: int
        QuotaNonPagedPoolUsage: int
        QuotaPagedPoolUsage: int
        PeakWorkingSetSize: int
        PeakPagefileUsage: int
        WorkingSetSize: int
        PageFaultCount: int
        PrivateUsage: int
        cb: int
        
    PPROCESS_MEMORY_COUNTERS_EX = POINTER(PROCESS_MEMORY_COUNTERS_EX)

    GetProcessMemoryInfo = declare(kernelbase.GetProcessMemoryInfo, BOOL, HANDLE, PPROCESS_MEMORY_COUNTERS, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    class PERFORMANCE_INFORMATION(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("CommitTotal", SIZE_T),
            ("CommitLimit", SIZE_T),
            ("CommitPeak", SIZE_T),
            ("PhysicalTotal", SIZE_T),
            ("PhysicalAvailable", SIZE_T),
            ("SystemCache", SIZE_T),
            ("KernelTotal", SIZE_T),
            ("KernelPaged", SIZE_T),
            ("KernelNonpaged", SIZE_T),
            ("PageSize", SIZE_T),
            ("HandleCount", DWORD),
            ("ProcessCount", DWORD),
            ("ThreadCount", DWORD)
        ]
        
        PhysicalAvailable: int
        KernelNonpaged: int
        PhysicalTotal: int
        ProcessCount: int
        ThreadCount: int
        KernelPaged: int
        KernelTotal: int
        CommitTotal: int
        CommitLimit: int
        HandleCount: int
        SystemCache: int
        CommitPeak: int
        PageSize: int
        cb: int
        
    PPERFORMANCE_INFORMATION = POINTER(PERFORMANCE_INFORMATION)

    GetPerformanceInfo = declare(kernelbase.GetPerformanceInfo, BOOL, PPERFORMANCE_INFORMATION, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***


    class ENUM_PAGE_FILE_INFORMATION(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("Reserved", DWORD),
            ("TotalSize", SIZE_T),
            ("TotalInUse", SIZE_T),
            ("PeakUsage", SIZE_T)
        ]
        
        TotalInUse: int
        TotalSize: int
        PeakUsage: int
        cb: int
        
    PENUM_PAGE_FILE_INFORMATION = POINTER(ENUM_PAGE_FILE_INFORMATION)

    PENUM_PAGE_FILE_CALLBACKW = CALLBACK(BOOL, LPVOID, PENUM_PAGE_FILE_INFORMATION, LPCWSTR)
    PENUM_PAGE_FILE_CALLBACKA = CALLBACK(BOOL, LPVOID, PENUM_PAGE_FILE_INFORMATION, LPCSTR)
    
    EnumPageFilesW = declare(kernelbase.EnumPageFilesW, BOOL, PENUM_PAGE_FILE_CALLBACKW, LPVOID)
    EnumPageFilesA = declare(kernelbase.EnumPageFilesA, BOOL, PENUM_PAGE_FILE_CALLBACKA, LPVOID)
    EnumPageFiles = unicode(EnumPageFilesW, EnumPageFilesA)
    PENUM_PAGE_FILE_CALLBACK = unicode(PENUM_PAGE_FILE_CALLBACKW, PENUM_PAGE_FILE_CALLBACKA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetProcessImageFileNameA = declare(kernelbase.GetProcessImageFileNameA, DWORD, HANDLE, LPSTR, DWORD)
    GetProcessImageFileNameW = declare(kernelbase.GetProcessImageFileNameW, DWORD, HANDLE, LPWSTR, DWORD)
    GetProcessImageFileName = unicode(GetProcessImageFileNameW, GetProcessImageFileNameA)