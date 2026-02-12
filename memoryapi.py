"""
 *********************************************************************************
 *                                                                               *
 * memoryapi.h -- ApiSet Contract for api-ms-win-core-memory-l1-1-0              *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from .minwindef import *

from .winnt import (PVOID, SIZE_T, PSIZE_T,
                    LPSECURITY_ATTRIBUTES, VOID, PPVOID, 
                    PULONG_PTR, SECTION_MAP_READ, SECTION_MAP_WRITE,
                    SECTION_MAP_EXECUTE_EXPLICIT, SECTION_ALL_ACCESS, PMEMORY_BASIC_INFORMATION,
                    ULONG_PTR, ULONG64, PCWSTR,
                    PSECURITY_ATTRIBUTES, WINAPI, PCFG_CALL_TARGET_INFO,
                    PMEM_EXTENDED_PARAMETER)

from .defbase import *

from typing import (Callable)

from . import cpreproc

if cpreproc.pragma_once("_MEMORYAPI_H_"):
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    FILE_MAP_WRITE = SECTION_MAP_WRITE
    FILE_MAP_READ = SECTION_MAP_READ
    FILE_MAP_ALL_ACCESS = SECTION_ALL_ACCESS
    FILE_MAP_EXECUTE = SECTION_MAP_EXECUTE_EXPLICIT # not included in FILE_MAP_ALL_ACCESS
    FILE_MAP_COPY = 0x00000001
    FILE_MAP_RESERVE = 0x80000000
    FILE_MAP_TARGETS_INVALID = 0x40000000
    FILE_MAP_LARGE_PAGES = 0x20000000

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    VirtualAlloc = declare(kernel32.VirtualAlloc, LPVOID, LPVOID, SIZE_T, DWORD, DWORD)
    VirtualProtect = declare(kernel32.VirtualProtect, BOOL, LPVOID, SIZE_T, DWORD, PDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    VirtualFree = declare(kernel32.VirtualFree, BOOL, LPVOID, SIZE_T, DWORD)
    VirtualQuery = declare(kernel32.VirtualQuery, SIZE_T, LPCVOID, PMEMORY_BASIC_INFORMATION, SIZE_T)
    VirtualAllocEx = declare(kernel32.VirtualAllocEx, LPVOID, HANDLE, LPVOID, SIZE_T, DWORD, DWORD)
    VirtualProtectEx = declare(kernel32.VirtualProtectEx, BOOL, HANDLE, LPVOID, SIZE_T, DWORD, PDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    VirtualQueryEx = declare(kernel32.VirtualQueryEx, SIZE_T, HANDLE, LPCVOID, PMEMORY_BASIC_INFORMATION, SIZE_T)
    ReadProcessMemory = declare(kernel32.ReadProcessMemory, BOOL, HANDLE, LPCVOID, LPVOID, SIZE_T, PSIZE_T)
    WriteProcessMemory = declare(kernel32.WriteProcessMemory, BOOL, HANDLE, LPVOID, LPCVOID, SIZE_T, PSIZE_T)
    CreateFileMappingW = declare(kernel32.CreateFileMappingW, HANDLE, HANDLE, LPSECURITY_ATTRIBUTES, DWORD, DWORD, DWORD, LPCWSTR)
    if cpreproc.ifdef("UNICODE"):
        CreateFileMapping = CreateFileMappingW
    OpenFileMappingW = declare(kernel32.OpenFileMappingW, HANDLE, DWORD, BOOL, LPCWSTR)
    if cpreproc.ifdef("UNICODE"):
        OpenFileMapping = OpenFileMappingW
    MapViewOfFile = declare(kernel32.MapViewOfFile, LPVOID, HANDLE, DWORD, DWORD, DWORD, SIZE_T)
    MapViewOfFileEx = declare(kernel32.MapViewOfFileEx, LPVOID, HANDLE, DWORD, DWORD, DWORD, SIZE_T, LPVOID)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    VirtualFreeEx = declare(kernel32.VirtualFreeEx, BOOL, HANDLE, LPVOID, SIZE_T, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    FlushViewOfFile = declare(kernel32.FlushViewOfFile, BOOL, LPCVOID, SIZE_T)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    UnmapViewOfFile = declare(kernel32.UnmapViewOfFile, BOOL, LPCVOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetLargePageMinimum = declare(kernel32.GetLargePageMinimum, SIZE_T, VOID)
    GetProcessWorkingSetSizeEx = declare(kernel32.GetProcessWorkingSetSizeEx, BOOL, HANDLE, PSIZE_T, PSIZE_T, PDWORD)
    SetProcessWorkingSetSizeEx = declare(kernel32.SetProcessWorkingSetSizeEx, BOOL, HANDLE, SIZE_T, SIZE_T, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    VirtualLock = declare(kernel32.VirtualLock, BOOL, LPVOID, SIZE_T)
    VirtualUnlock = declare(kernel32.VirtualUnlock, BOOL, LPVOID, SIZE_T)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetWriteWatch = declare(kernel32.GetWriteWatch, UINT, DWORD, PVOID, SIZE_T, PPVOID, PULONG_PTR, LPDWORD)
    ResetWriteWatch = declare(kernel32.ResetWriteWatch, UINT, LPVOID, SIZE_T)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    MEMORY_RESOURCE_NOTIFICATION_TYPE = INT
    if True:
        LowMemoryResourceNotification = 0
        HighMemoryResourceNotification = 1

    CreateMemoryResourceNotification = declare(kernel32.CreateMemoryResourceNotification, HANDLE, MEMORY_RESOURCE_NOTIFICATION_TYPE)
    QueryMemoryResourceNotification = declare(kernel32.QueryMemoryResourceNotification, BOOL, HANDLE, PBOOL)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    cpreproc.define("FILE_CACHE_FLAGS_DEFINED")
    FILE_CACHE_MAX_HARD_ENABLE = 0x00000001
    FILE_CACHE_MAX_HARD_DISABLE = 0x00000002
    FILE_CACHE_MIN_HARD_ENABLE = 0x00000004
    FILE_CACHE_MIN_HARD_DISABLE = 0x00000008
    GetSystemFileCacheSize = declare(kernel32.GetSystemFileCacheSize, BOOL, PSIZE_T, PSIZE_T, PDWORD)
    SetSystemFileCacheSize = declare(kernel32.SetSystemFileCacheSize, BOOL, SIZE_T, SIZE_T, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    CreateFileMappingNumaW = declare(kernel32.CreateFileMappingNumaW, HANDLE, HANDLE, LPSECURITY_ATTRIBUTES, DWORD, DWORD, DWORD, LPCWSTR, DWORD)
    if cpreproc.ifdef("UNICODE"):
        CreateFileMappingNuma = CreateFileMappingNumaW

    class _WIN32_MEMORY_RANGE_ENTRY(CStructure):
        _fields_ = [
            ("VirtualAddress", PVOID),
            ("NumberOfBytes", SIZE_T)
        ]
    WIN32_MEMORY_RANGE_ENTRY = _WIN32_MEMORY_RANGE_ENTRY
    PWIN32_MEMORY_RANGE_ENTRY = POINTER(WIN32_MEMORY_RANGE_ENTRY)

    PrefetchVirtualMemory = declare(kernel32.PrefetchVirtualMemory, BOOL, HANDLE, ULONG_PTR, PWIN32_MEMORY_RANGE_ENTRY, ULONG)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    CreateFileMappingFromApp = declare(kernel32.CreateFileMappingFromApp, HANDLE, HANDLE, PSECURITY_ATTRIBUTES, ULONG, ULONG64, PCWSTR)
    MapViewOfFileFromApp = declare(kernel32.MapViewOfFileFromApp, PVOID, HANDLE, ULONG, ULONG64, SIZE_T)
    UnmapViewOfFileEx = declare(kernel32.UnmapViewOfFileEx, BOOL, PVOID, ULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    AllocateUserPhysicalPages = declare(kernel32.AllocateUserPhysicalPages, BOOL, HANDLE, PULONG_PTR, PULONG_PTR)
    FreeUserPhysicalPages = declare(kernel32.FreeUserPhysicalPages, BOOL, HANDLE, PULONG_PTR, PULONG_PTR)
    MapUserPhysicalPages = declare(kernel32.MapUserPhysicalPages, BOOL, PVOID, ULONG_PTR, PULONG_PTR)
    AllocateUserPhysicalPagesNuma = declare(kernel32.AllocateUserPhysicalPagesNuma, BOOL, HANDLE, PULONG_PTR, PULONG_PTR, DWORD)
    VirtualAllocExNuma = declare(kernel32.VirtualAllocExNuma, LPVOID, HANDLE, LPVOID, SIZE_T, DWORD, DWORD, DWORD)
    MEHC_PATROL_SCRUBBER_PRESENT = 0x1
    GetMemoryErrorHandlingCapabilities = declare(kernel32.GetMemoryErrorHandlingCapabilities, BOOL, PULONG)

    BAD_MEMORY_CALLBACK_ROUTINE = WINAPI(VOID)
    PBAD_MEMORY_CALLBACK_ROUTINE = POINTER(BAD_MEMORY_CALLBACK_ROUTINE)

    RegisterBadMemoryNotification = declare(kernel32.RegisterBadMemoryNotification, PVOID, PBAD_MEMORY_CALLBACK_ROUTINE)
    UnregisterBadMemoryNotification = declare(kernel32.UnregisterBadMemoryNotification, BOOL, PVOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    # This API is not actually available in all blue builds since it is part
    # of the S14 GDR release, however because there is no new version for GDR
    # this is the most accurate version available.  To safely use this API on
    # BLUE builds callers will need to use LoadLibrary and GetProcAddress to
    # check for the existance of the API's before calling them.


    OFFER_PRIORITY = INT
    if True:
        VmOfferPriorityVeryLow = 1
        VmOfferPriorityLow = 2
        VmOfferPriorityBelowNormal = 3
        VmOfferPriorityNormal = 4

    OfferVirtualMemory = declare(kernel32.OfferVirtualMemory, DWORD, PVOID, SIZE_T, OFFER_PRIORITY)
    ReclaimVirtualMemory = declare(kernel32.ReclaimVirtualMemory, DWORD, PVOID, SIZE_T)
    DiscardVirtualMemory = declare(kernel32.DiscardVirtualMemory, DWORD, PVOID, SIZE_T)
    SetProcessValidCallTargets = declare(kernelbase.SetProcessValidCallTargets, BOOL, HANDLE, PVOID, SIZE_T, ULONG, PCFG_CALL_TARGET_INFO)
    SetProcessValidCallTargetsForMappedView = declare(kernelbase.SetProcessValidCallTargetsForMappedView, BOOL, HANDLE, PVOID, SIZE_T, ULONG, PCFG_CALL_TARGET_INFO, HANDLE, ULONG64)
    VirtualAllocFromApp = declare(kernelbase.VirtualAllocFromApp, PVOID, PVOID, SIZE_T, ULONG, ULONG)
    VirtualProtectFromApp = declare(kernelbase.VirtualProtectFromApp, BOOL, PVOID, SIZE_T, ULONG, PULONG)
    OpenFileMappingFromApp = declare(kernelbase.OpenFileMappingFromApp, HANDLE, ULONG, BOOL, PCWSTR)

    # REGION ***

    # REGION *** Application Family ***

    CreateFileMapping = CreateFileMappingW

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    WIN32_MEMORY_INFORMATION_CLASS = INT
    if True:
        MemoryRegionInfo = 0

    class _S_PMDFMIMPFMPDMR(CStructure):
        _fields_ = [
            ("Private", ULONG, 1),
            ("MappedDataFile", ULONG, 1),
            ("MappedImage", ULONG, 1),
            ("MappedPageFile", ULONG, 1),
            ("MappedPhysical", ULONG, 1),
            ("DirectMapped", ULONG, 1),
            ("Reserved", ULONG, 26)
        ]

    class _U_FS(Union):
        _fields_ = [
            ("Flags", ULONG),
            ("s", _S_PMDFMIMPFMPDMR)
        ]

    class WIN32_MEMORY_REGION_INFORMATION(CStructure):
        _fields_ = [
            ("AllocationBase", PVOID),
            ("AllocationProtect", ULONG),
            ("u", _U_FS),
            ("RegionSize", SIZE_T),
            ("CommitSize", SIZE_T)
        ]

    QueryVirtualMemoryInformation = declare(kernelbase.QueryVirtualMemoryInformation, BOOL, HANDLE, PVOID, WIN32_MEMORY_INFORMATION_CLASS, PVOID, SIZE_T, PSIZE_T)
    MapViewOfFileNuma2 = declare(kernelbase.MapViewOfFileNuma2, PVOID, HANDLE, HANDLE, ULONG64, PVOID, SIZE_T, ULONG, ULONG, ULONG)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    UnmapViewOfFile2 = declare(kernelbase.UnmapViewOfFile2, BOOL, HANDLE, PVOID, ULONG)
    VirtualUnlockEx = declare(kernelbase.VirtualUnlockEx, BOOL, HANDLE, LPVOID, SIZE_T)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    VirtualAlloc2 = declare(kernelbase.VirtualAlloc2, PVOID, HANDLE, PVOID, SIZE_T, ULONG, ULONG, PMEM_EXTENDED_PARAMETER, ULONG)
    MapViewOfFile3 = declare(kernelbase.MapViewOfFile3, PVOID, HANDLE, HANDLE, PVOID, ULONG64, SIZE_T, ULONG, ULONG, PMEM_EXTENDED_PARAMETER, ULONG)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    VirtualAlloc2FromApp = declare(kernelbase.VirtualAlloc2FromApp, PVOID, HANDLE, PVOID, SIZE_T, ULONG, ULONG, PMEM_EXTENDED_PARAMETER, ULONG)
    MapViewOfFile3FromApp = declare(kernelbase.MapViewOfFile3FromApp, PVOID, HANDLE, HANDLE, PVOID, ULONG64, SIZE_T, ULONG, ULONG, PMEM_EXTENDED_PARAMETER, ULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    CreateFileMapping2 = declare(kernelbase.CreateFileMapping2, HANDLE, HANDLE, PSECURITY_ATTRIBUTES, ULONG, ULONG, ULONG, ULONG64, PCWSTR, PMEM_EXTENDED_PARAMETER, ULONG)

    # REGION ***
# _MEMORYAPI_H_