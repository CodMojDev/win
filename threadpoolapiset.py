
"""
*******************************************************************************
 *                                                                               *
 * threadpoolapi.h -- ApiSet Contract for api-ms-win-core-threadpool-l1          *
 *                                                                               *
 * Copyright(c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
*******************************************************************************
"""

from .sdkddkver import *
from .minwindef import *
from .winnt import PRTL_CRITICAL_SECTION as PCRITICAL_SECTION

if cpreproc.pragma_once("_THREADPOOLAPISET_H_"):
    kernel32 = get_win_library('kernel32.dll')
    
    #
    # Thread pool API's
    #

    # REGION *** Application Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        class _TP_WORK(CStructure):
            _fields_ = []
        PTP_WORK = PTR(_TP_WORK)
        class _TP_TIMER(CStructure):
            _fields_ = []
        PTP_TIMER = PTR(_TP_TIMER)
        class _TP_POOL(CStructure):
            _fields_ = []
        PTP_POOL = PTR(_TP_POOL)
        class _TP_WAIT(CStructure):
            _fields_ = []
        PTP_WAIT = PTR(_TP_WAIT)
        class _TP_IO(CStructure):
            _fields_ = []
        PTP_IO = PTR(_TP_IO)
        class _TP_CLEANUP_GROUP(CStructure):
            _fields_ = []
        PTP_CLEANUP_GROUP = PTR(_TP_CLEANUP_GROUP)
        class _TP_CALLBACK_INSTANCE(CStructure):
            _fields_ = []
        PTP_CALLBACK_INSTANCE = PTR(_TP_CALLBACK_INSTANCE)
        class _TP_POOL_STACK_INFORMATION(CStructure):
            _fields_ = [
                ('StackReserve', SIZE_T),
                ('StackCommit', SIZE_T)
            ]
            StackReserve: int
            StackCommit: int
        PTP_POOL_STACK_INFORMATION = PTR(_TP_POOL_STACK_INFORMATION)
        PTP_WORK_CALLBACK = WINAPI(VOID, PTP_CALLBACK_INSTANCE, PVOID, PTP_WORK)
        PTP_TIMER_CALLBACK = WINAPI(VOID, PTP_CALLBACK_INSTANCE, PVOID, PTP_TIMER)
        PTP_SIMPLE_CALLBACK = WINAPI(VOID, PTP_CALLBACK_INSTANCE, PVOID)
        TP_WAIT_RESULT = DWORD
        PTP_WAIT_CALLBACK = WINAPI(VOID, PTP_CALLBACK_INSTANCE, PVOID, PTP_WAIT, TP_WAIT_RESULT)
        PTP_WIN32_IO_CALLBACK = WINAPI(VOID, PTP_CALLBACK_INSTANCE, PVOID, PVOID, ULONG, ULONG_PTR, PTP_IO)
        PTP_CLEANUP_GROUP_CANCEL_CALLBACK = WINAPI(VOID, PVOID, PVOID)
        TP_VERSION = DWORD
        TP_CALLBACK_PRIORITY_HIGH = 0
        TP_CALLBACK_PRIORITY_NORMAL = 1
        TP_CALLBACK_PRIORITY_LOW = 2
        TP_CALLBACK_PRIORITY_INVALID = 3
        TP_CALLBACK_PRIORITY_COUNT = TP_CALLBACK_PRIORITY_INVALID
        TP_CALLBACK_PRIORITY = DWORD
        class _TP_CALLBACK_ENVIRON(CStructure):
            class _U(CUnion):
                class _S(CStructure):
                    _fields_ = [
                        ('LongFunction', DWORD, 1),
                        ('Persistent', DWORD, 1),
                        ('Private', DWORD, 30)
                    ]
                _fields_ = [
                    ('Flags', DWORD),
                    ('_s', _S)
                ]
                _anonymous_ = ['_s']
            _fields_ = [
                ('Version', TP_VERSION),
                ('Pool', PTP_POOL),
                ('CleanupGroup', PTP_CLEANUP_GROUP),
                ('CleanupGroupCancelCallback', PTP_CLEANUP_GROUP_CANCEL_CALLBACK),
                ('RaceDll', PVOID),
                ('ActivationContext', PVOID),
                ('FinalizationCallback', PTP_SIMPLE_CALLBACK),
                ('_u', _U),
                ('CallbackPriority', TP_CALLBACK_PRIORITY),
                ('Size', DWORD)
            ]
            _anonymous_ = ['_u']
            Version: int
            Pool: int
            CleanupGroup: IPointer[_TP_CLEANUP_GROUP]
            CleanupGroupCancelCallback: FARPROC
            RaceDll: int
            ActivationContext: int
            FinalizationCallback: FARPROC
            Flags: int
            LongFunction: int
            Persistent: int
            Private: int
            CallbackPriority: int
            Size: int
        PTP_CALLBACK_ENVIRON = PTR(_TP_CALLBACK_ENVIRON)
        
        CreateThreadpool = declare(kernel32.CreateThreadpool, PTP_POOL, PVOID)
        SetThreadpoolThreadMaximum = declare(kernel32.SetThreadpoolThreadMaximum, VOID, PTP_POOL, DWORD)
        SetThreadpoolThreadMinimum = declare(kernel32.SetThreadpoolThreadMinimum, BOOL, PTP_POOL, DWORD)
        SetThreadpoolStackInformation = declare(kernel32.SetThreadpoolStackInformation, BOOL, PTP_POOL, PTP_POOL_STACK_INFORMATION)
        QueryThreadpoolStackInformation = declare(kernel32.QueryThreadpoolStackInformation, BOOL, PTP_POOL, PTP_POOL_STACK_INFORMATION)
        CloseThreadpool = declare(kernel32.CloseThreadpool, VOID, PTP_POOL)
        CreateThreadpoolCleanupGroup = declare(kernel32.CreateThreadpoolCleanupGroup, PTP_CLEANUP_GROUP, VOID)
        CloseThreadpoolCleanupGroupMembers = declare(kernel32.CloseThreadpoolCleanupGroupMembers, VOID, PTP_CLEANUP_GROUP, BOOL, PVOID)
        CloseThreadpoolCleanupGroup = declare(kernel32.CloseThreadpoolCleanupGroup, VOID, PTP_CLEANUP_GROUP)
        SetEventWhenCallbackReturns = declare(kernel32.SetEventWhenCallbackReturns, VOID, PTP_CALLBACK_INSTANCE, HANDLE)
        ReleaseSemaphoreWhenCallbackReturns = declare(kernel32.ReleaseSemaphoreWhenCallbackReturns, VOID, PTP_CALLBACK_INSTANCE, HANDLE, DWORD)
        ReleaseMutexWhenCallbackReturns = declare(kernel32.ReleaseMutexWhenCallbackReturns, VOID, PTP_CALLBACK_INSTANCE, HANDLE)
        LeaveCriticalSectionWhenCallbackReturns = declare(kernel32.LeaveCriticalSectionWhenCallbackReturns, VOID, PTP_CALLBACK_INSTANCE, PCRITICAL_SECTION)
        FreeLibraryWhenCallbackReturns = declare(kernel32.FreeLibraryWhenCallbackReturns, VOID, PTP_CALLBACK_INSTANCE, HMODULE)
        CallbackMayRunLong = declare(kernel32.CallbackMayRunLong, BOOL, PTP_CALLBACK_INSTANCE)
        DisassociateCurrentThreadFromCallback = declare(kernel32.DisassociateCurrentThreadFromCallback, VOID, PTP_CALLBACK_INSTANCE)
        TrySubmitThreadpoolCallback = declare(kernel32.TrySubmitThreadpoolCallback, BOOL, PTP_SIMPLE_CALLBACK, PVOID, PTP_CALLBACK_ENVIRON)
        CreateThreadpoolWork = declare(kernel32.CreateThreadpoolWork, PTP_WORK, PTP_WORK_CALLBACK, PVOID, PTP_CALLBACK_ENVIRON)
        SubmitThreadpoolWork = declare(kernel32.SubmitThreadpoolWork, VOID, PTP_WORK)
        WaitForThreadpoolWorkCallbacks = declare(kernel32.WaitForThreadpoolWorkCallbacks, VOID, PTP_WORK, BOOL)
        CloseThreadpoolWork = declare(kernel32.CloseThreadpoolWork, VOID, PTP_WORK)
        CreateThreadpoolTimer = declare(kernel32.CreateThreadpoolTimer, PTP_TIMER, PTP_TIMER_CALLBACK, PVOID, PTP_CALLBACK_ENVIRON)
        SetThreadpoolTimer = declare(kernel32.SetThreadpoolTimer, VOID, PTP_TIMER, PFILETIME, DWORD, DWORD)
        IsThreadpoolTimerSet = declare(kernel32.IsThreadpoolTimerSet, BOOL, PTP_TIMER)
        WaitForThreadpoolTimerCallbacks = declare(kernel32.WaitForThreadpoolTimerCallbacks, VOID, PTP_TIMER, BOOL)
        CloseThreadpoolTimer = declare(kernel32.CloseThreadpoolTimer, VOID, PTP_TIMER)
        CreateThreadpoolWait = declare(kernel32.CreateThreadpoolWait, PTP_WAIT, PTP_WAIT_CALLBACK, PVOID, PTP_CALLBACK_ENVIRON)
        SetThreadpoolWait = declare(kernel32.SetThreadpoolWait, VOID, PTP_WAIT, HANDLE, PFILETIME)
        WaitForThreadpoolWaitCallbacks = declare(kernel32.WaitForThreadpoolWaitCallbacks, VOID, PTP_WAIT, BOOL)
        CloseThreadpoolWait = declare(kernel32.CloseThreadpoolWait, VOID, PTP_WAIT)
        CreateThreadpoolIo = declare(kernel32.CreateThreadpoolIo, PTP_IO, HANDLE, PTP_WIN32_IO_CALLBACK, PVOID, PTP_CALLBACK_ENVIRON)
        StartThreadpoolIo = declare(kernel32.StartThreadpoolIo, VOID, PTP_IO)
        CancelThreadpoolIo = declare(kernel32.CancelThreadpoolIo, VOID, PTP_IO)
        WaitForThreadpoolIoCallbacks = declare(kernel32.WaitForThreadpoolIoCallbacks, VOID, PTP_IO, BOOL)
        CloseThreadpoolIo = declare(kernel32.CloseThreadpoolIo, VOID, PTP_IO)

        # REGION ***

        # REGION *** Application Family or OneCore Family ***

        SetThreadpoolTimerEx = declare(kernel32.SetThreadpoolTimerEx, BOOL, PTP_TIMER, PFILETIME, DWORD, DWORD)
        SetThreadpoolWaitEx = declare(kernel32.SetThreadpoolWaitEx, BOOL, PTP_WAIT, HANDLE, PFILETIME, PVOID)

        # REGION ***

        # REGION *** Desktop Family or OneCore Family or Games Family ***

        # REGION ***
# _THREADPOOLAPISET_H_