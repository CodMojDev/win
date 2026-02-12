"""
 *********************************************************************************
 *                                                                               *
 * threadpoolapi.h -- ApiSet Contract for api-ms-win-core-threadpool-l1          *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .defbase import *

from .minwindef import (BOOL, PVOID, ULONG,
                    HANDLE, PHANDLE, VOID, 
                    DWORD, windll)
from .winbase import (LPTHREAD_START_ROUTINE)
from .winnt import WAITORTIMERCALLBACK

if cpreproc.pragma_once("_THREADPOOLLEGACYAPISET_H_"):
    kernel32 = W_WinDLL("kernel32.dll")
    #
    # Thread pool API's
    #

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    QueueUserWorkItem = declare(kernel32.QueueUserWorkItem, BOOL, LPTHREAD_START_ROUTINE, PVOID, ULONG)
    UnregisterWaitEx = declare(kernel32.UnregisterWaitEx, BOOL, HANDLE, HANDLE)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    CreateTimerQueue = declare(kernel32.CreateTimerQueue, HANDLE, VOID)
    CreateTimerQueueTimer = declare(kernel32.CreateTimerQueueTimer, BOOL, PHANDLE, HANDLE, WAITORTIMERCALLBACK, PVOID, DWORD, DWORD, ULONG)
    ChangeTimerQueueTimer = declare(kernel32.ChangeTimerQueueTimer, BOOL, HANDLE, HANDLE, ULONG, ULONG)
    DeleteTimerQueueTimer = declare(kernel32.DeleteTimerQueueTimer, BOOL, HANDLE, HANDLE, HANDLE)
    DeleteTimerQueueEx = declare(kernel32.DeleteTimerQueueEx, BOOL, HANDLE, HANDLE)

    # REGION ***
# _THREADPOOLLEGACYAPISET_H_