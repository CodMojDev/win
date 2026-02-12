"""
 *********************************************************************************
 *                                                                               *
 * HeapApi.h -- ApiSet Contract for api-ms-win-core-heap-l1                      *  
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

from .winbase import *

if cpreproc.pragma_once("_HEAPAPI_H_"):
    kernelbase = W_WinDLL("kernelbase.dll")
    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # typdefs
    #

    class HEAP_SUMMARY(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("cbAllocated", SIZE_T),
            ("cbCommited", SIZE_T),
            ("cbReserved", SIZE_T),
            ("cbMaxReserve", SIZE_T)
        ]
    PHEAP_SUMMARY = POINTER(HEAP_SUMMARY)
    LPHEAP_SUMMARY = PHEAP_SUMMARY

    #
    # Prototypes
    #
    HeapCreate = declare(kernel32.HeapCreate, HANDLE, DWORD, SIZE_T, SIZE_T)
    HeapDestroy = declare(kernel32.HeapDestroy, BOOL, HANDLE)
    HeapAlloc = declare(kernel32.HeapAlloc, LPVOID, HANDLE, DWORD, SIZE_T)
    HeapReAlloc = declare(kernel32.HeapReAlloc, LPVOID, HANDLE, DWORD, LPVOID, SIZE_T)
    HeapFree = declare(kernel32.HeapFree, BOOL, HANDLE, DWORD, LPVOID)
    HeapSize = declare(kernel32.HeapSize, SIZE_T, HANDLE, DWORD, LPCVOID)
    GetProcessHeap = declare(kernel32.GetProcessHeap, HANDLE, VOID)
    HeapCompact = declare(kernel32.HeapCompact, SIZE_T, HANDLE, DWORD)
    HeapSetInformation = declare(kernel32.HeapSetInformation, BOOL, HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    HeapValidate = declare(kernel32.HeapValidate, BOOL, HANDLE, DWORD, LPCVOID)

    # REGION ***

    # REGION *** Application Family ***

    HeapSummary = declare(kernel32.HeapSummary, BOOL, HANDLE, DWORD, LPHEAP_SUMMARY)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetProcessHeaps = declare(kernel32.GetProcessHeaps, DWORD, DWORD, PHANDLE)
    HeapLock = declare(kernel32.HeapLock, BOOL, HANDLE)
    HeapUnlock = declare(kernel32.HeapUnlock, BOOL, HANDLE)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    HeapWalk = declare(kernel32.HeapWalk, BOOL, HANDLE, LPPROCESS_HEAP_ENTRY)
    HeapQueryInformation = declare(kernel32.HeapQueryInformation, BOOL, HANDLE, HEAP_INFORMATION_CLASS, PVOID, SIZE_T, PSIZE_T)

    # REGION ***
    #
    # HeapSummary() is in minwinbase.w within ;beg_internal tags. Has to stay there for downlevel reasons.
    #
# _HEAPAPI_H_