"""
 *********************************************************************************
 *                                                                               *
 * ioapiset.h -- ApiSet Contract for api-ms-win-core-io-l1                       *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *

from .winnt import ULONG_PTR, PULONG_PTR

from .winbase import LPOVERLAPPED, LPOVERLAPPED_ENTRY

from .defbase import *

if cpreproc.pragma_once("_IO_APISET_H_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    CreateIoCompletionPort = declare(kernel32.CreateIoCompletionPort, HANDLE, HANDLE, HANDLE, ULONG_PTR, DWORD)
    GetQueuedCompletionStatus = declare(kernel32.GetQueuedCompletionStatus, BOOL, HANDLE, LPDWORD, PULONG_PTR, POINTER(LPOVERLAPPED), DWORD)
    GetQueuedCompletionStatusEx = declare(kernel32.GetQueuedCompletionStatusEx, BOOL, HANDLE, LPOVERLAPPED_ENTRY, ULONG, PULONG, DWORD, BOOL)
    PostQueuedCompletionStatus = declare(kernel32.PostQueuedCompletionStatus, BOOL, HANDLE, DWORD, ULONG_PTR, LPOVERLAPPED)

    # REGION ***

    # REGION ***  Desktop Family or OneCore Family or Application Family or Games Family ***

    DeviceIoControl = declare(kernel32.DeviceIoControl, BOOL, HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, LPOVERLAPPED)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetOverlappedResult = declare(kernel32.GetOverlappedResult, BOOL, HANDLE, LPOVERLAPPED, LPDWORD, BOOL)
    CancelIoEx = declare(kernel32.CancelIoEx, BOOL, HANDLE, LPOVERLAPPED)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    CancelIo = declare(kernel32.CancelIo, BOOL, HANDLE)
    GetOverlappedResultEx = declare(kernel32.GetOverlappedResultEx, BOOL, HANDLE, LPOVERLAPPED, LPDWORD, DWORD, BOOL)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    CancelSynchronousIo = declare(kernel32.CancelSynchronousIo, BOOL, HANDLE)

    # REGION ***
# _IO_APISET_H_