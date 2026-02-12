"""
 *********************************************************************************
 *                                                                               *
 * synchapi.h -- ApiSet Contract for api-ms-win-core-synch-l1                    *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .winnt import (RTL_SRWLOCK_INIT, PRTL_CRITICAL_SECTION, 
                    RTL_SRWLOCK, RTL_RUN_ONCE, PRTL_RUN_ONCE,
                    RTL_RUN_ONCE_INIT, RTL_RUN_ONCE_ASYNC,
                    RTL_RUN_ONCE_INIT_FAILED, RTL_RUN_ONCE_CHECK_ONLY,
                    RTL_RUN_ONCE_CTX_RESERVED_BITS, RTL_BARRIER,
                    PRTL_BARRIER, PRTL_CONDITION_VARIABLE,
                    RTL_CONDITION_VARIABLE_LOCKMODE_SHARED,
                    RTL_CONDITION_VARIABLE_INIT, MUTANT_ALL_ACCESS,
                    LPSECURITY_ATTRIBUTES, MUTANT_QUERY_STATE
                    )

from .winbase import PREASON_CONTEXT

from .defbase import *

if cpreproc.pragma_once("_SYNCHAPI_H_"):
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application or OneCore Family or Games Family ***

    #
    # Define the slim R/W lock.
    #
    SRWLOCK_INIT = RTL_SRWLOCK_INIT
    SRWLOCK = RTL_SRWLOCK
    PSRWLOCK = POINTER(SRWLOCK)
    InitializeSRWLock = declare(kernel32.InitializeSRWLock, VOID, PSRWLOCK)
    ReleaseSRWLockExclusive = declare(kernel32.ReleaseSRWLockExclusive, VOID, PSRWLOCK)
    ReleaseSRWLockShared = declare(kernel32.ReleaseSRWLockShared, VOID, PSRWLOCK)
    AcquireSRWLockExclusive = declare(kernel32.AcquireSRWLockExclusive, VOID, PSRWLOCK)
    AcquireSRWLockShared = declare(kernel32.AcquireSRWLockShared, VOID, PSRWLOCK)
    TryAcquireSRWLockExclusive = declare(kernel32.TryAcquireSRWLockExclusive, BOOLEAN, PSRWLOCK)
    TryAcquireSRWLockShared = declare(kernel32.TryAcquireSRWLockShared, BOOLEAN, PSRWLOCK)
    InitializeCriticalSection = declare(kernel32.InitializeCriticalSection, VOID, PRTL_CRITICAL_SECTION)
    InitializeCriticalSection = declare(kernel32.InitializeCriticalSection, VOID, PRTL_CRITICAL_SECTION)
    EnterCriticalSection = declare(kernel32.EnterCriticalSection, VOID, PRTL_CRITICAL_SECTION)
    LeaveCriticalSection = declare(kernel32.LeaveCriticalSection, VOID, PRTL_CRITICAL_SECTION)
    InitializeCriticalSectionAndSpinCount = declare(kernel32.InitializeCriticalSectionAndSpinCount, BOOL, PRTL_CRITICAL_SECTION, DWORD)
    InitializeCriticalSectionEx = declare(kernel32.InitializeCriticalSectionEx, BOOL, PRTL_CRITICAL_SECTION, DWORD, DWORD)
    SetCriticalSectionSpinCount = declare(kernel32.SetCriticalSectionSpinCount, DWORD, PRTL_CRITICAL_SECTION, DWORD)
    TryEnterCriticalSection = declare(kernel32.TryEnterCriticalSection, BOOL, PRTL_CRITICAL_SECTION)
    DeleteCriticalSection = declare(kernel32.DeleteCriticalSection, VOID, PRTL_CRITICAL_SECTION)
    #
    # Define one-time initialization primitive
    #
    INIT_ONCE = RTL_RUN_ONCE
    PINIT_ONCE = PRTL_RUN_ONCE
    LPINIT_ONCE = PRTL_RUN_ONCE

    INIT_ONCE_STATIC_INIT = RTL_RUN_ONCE_INIT

    #
    # Run once flags
    #

    INIT_ONCE_CHECK_ONLY = RTL_RUN_ONCE_CHECK_ONLY
    INIT_ONCE_ASYNC = RTL_RUN_ONCE_ASYNC
    INIT_ONCE_INIT_FAILED = RTL_RUN_ONCE_INIT_FAILED

    #
    # The context stored in the run once structure must leave the following number
    # of low order bits unused.
    #

    INIT_ONCE_CTX_RESERVED_BITS = RTL_RUN_ONCE_CTX_RESERVED_BITS

    PINIT_ONCE_FN = WINAPI(BOOL, PINIT_ONCE, PVOID, PPVOID)

    InitOnceInitialize = declare(kernel32.InitOnceInitialize, VOID, PINIT_ONCE)
    InitOnceExecuteOnce = declare(kernel32.InitOnceExecuteOnce, BOOL, PINIT_ONCE, PINIT_ONCE_FN, PVOID, PLPVOID)
    InitOnceBeginInitialize = declare(kernel32.InitOnceBeginInitialize, BOOL, LPINIT_ONCE, DWORD, PBOOL, PLPVOID)
    InitOnceComplete = declare(kernel32.InitOnceComplete, BOOL, LPINIT_ONCE, DWORD, LPVOID)
    # (_WIN32_WINNT >= 0x0600)
    #
    # Define condition variable
    #
    #typedef RTL_CONDITION_VARIABLE CONDITION_VARIABLE, *PCONDITION_VARIABLE;
    #
    # Static initializer for the condition variable
    #
    CONDITION_VARIABLE_INIT = RTL_CONDITION_VARIABLE_INIT
    #
    # Flags for condition variables
    #
    CONDITION_VARIABLE_LOCKMODE_SHARED = RTL_CONDITION_VARIABLE_LOCKMODE_SHARED
    InitializeConditionVariable = declare(kernel32.InitializeConditionVariable, VOID, PRTL_CONDITION_VARIABLE)
    WakeConditionVariable = declare(kernel32.WakeConditionVariable, VOID, PRTL_CONDITION_VARIABLE)
    WakeAllConditionVariable = declare(kernel32.WakeAllConditionVariable, VOID, PRTL_CONDITION_VARIABLE)
    SleepConditionVariableCS = declare(kernel32.SleepConditionVariableCS, BOOL, PRTL_CONDITION_VARIABLE, PRTL_CRITICAL_SECTION, DWORD)
    SleepConditionVariableSRW = declare(kernel32.SleepConditionVariableSRW, BOOL, PRTL_CONDITION_VARIABLE, PSRWLOCK, DWORD, ULONG)
    SetEvent = declare(kernel32.SetEvent, BOOL, HANDLE)
    ResetEvent = declare(kernel32.ResetEvent, BOOL, HANDLE)
    ReleaseSemaphore = declare(kernel32.ReleaseSemaphore, BOOL, HANDLE, LONG, LPLONG)
    ReleaseMutex = declare(kernel32.ReleaseMutex, BOOL, HANDLE)
    WaitForSingleObject = declare(kernel32.WaitForSingleObject, DWORD, HANDLE, DWORD)
    SleepEx = declare(kernel32.SleepEx, DWORD, DWORD, BOOL)
    WaitForSingleObjectEx = declare(kernel32.WaitForSingleObjectEx, DWORD, HANDLE, DWORD, BOOL)
    WaitForMultipleObjectsEx = declare(kernel32.WaitForMultipleObjectsEx, DWORD, DWORD, PHANDLE, BOOL, DWORD, BOOL)
    #
    # Synchronization APIs
    #
    MUTEX_MODIFY_STATE = MUTANT_QUERY_STATE
    MUTEX_ALL_ACCESS = MUTANT_ALL_ACCESS
    CreateMutexA = declare(kernel32.CreateMutexA, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, LPCSTR)
    CreateMutexW = declare(kernel32.CreateMutexW, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, LPCWSTR)
    CreateMutex = unicode(CreateMutexW, CreateMutexA)
    # !UNICODE
    OpenMutexA = declare(kernel32.OpenMutexA, HANDLE, DWORD, BOOL, LPCSTR)
    OpenMutexW = declare(kernel32.OpenMutexW, HANDLE, DWORD, BOOL, LPCWSTR)
    OpenMutex = unicode(OpenMutexW, OpenMutexA)
    CreateEventA = declare(kernel32.CreateEventA, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, BOOL, LPCSTR)
    CreateEventW = declare(kernel32.CreateEventW, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, BOOL, LPCWSTR)
    CreateEvent = unicode(CreateEventW, CreateEventA)
    # !UNICODE
    OpenEventA = declare(kernel32.OpenEventA, HANDLE, DWORD, BOOL, LPCSTR)
    OpenEventW = declare(kernel32.OpenEventW, HANDLE, DWORD, BOOL, LPCWSTR)
    OpenEvent = unicode(OpenEventW, OpenEventA)
    # !UNICODE
    OpenSemaphoreA = declare(kernel32.OpenSemaphoreA, HANDLE, DWORD, BOOL, LPCSTR)
    OpenSemaphoreW = declare(kernel32.OpenSemaphoreW, HANDLE, DWORD, BOOL, LPCWSTR)
    OpenSemaphore = unicode(OpenSemaphoreW, OpenSemaphoreA)
    PTIMERAPCROUTINE = APIENTRY(VOID, LPVOID, DWORD, DWORD)
    OpenWaitableTimerA = declare(kernel32.OpenWaitableTimerA, HANDLE, DWORD, BOOL, LPCSTR)
    OpenWaitableTimerW = declare(kernel32.OpenWaitableTimerW, HANDLE, DWORD, BOOL, LPCWSTR)
    OpenWaitableTimer = unicode(OpenWaitableTimerW, OpenWaitableTimerA)
    SetWaitableTimerEx = declare(kernel32.SetWaitableTimerEx, BOOL, HANDLE, PLARGE_INTEGER, LONG, PTIMERAPCROUTINE, LPVOID, PREASON_CONTEXT, ULONG)
    SetWaitableTimer = declare(kernel32.SetWaitableTimer, BOOL, HANDLE, PLARGE_INTEGER, LONG, PTIMERAPCROUTINE, LPVOID, BOOL)
    CancelWaitableTimer = declare(kernel32.CancelWaitableTimer, BOOL, HANDLE)
    CREATE_MUTEX_INITIAL_OWNER = 0x00000001
    CreateMutexExA = declare(kernel32.CreateMutexExA, HANDLE, LPSECURITY_ATTRIBUTES, LPCSTR, DWORD, DWORD)
    CreateMutexExW = declare(kernel32.CreateMutexExW, HANDLE, LPSECURITY_ATTRIBUTES, LPCWSTR, DWORD, DWORD)
    CreateMutexEx = unicode(CreateMutexExW, CreateMutexExA)
    CREATE_EVENT_MANUAL_RESET = 0x00000001
    CREATE_EVENT_INITIAL_SET = 0x00000002
    CreateEventExA = declare(kernel32.CreateEventExA, HANDLE, LPSECURITY_ATTRIBUTES, LPCSTR, DWORD, DWORD)
    CreateEventExW = declare(kernel32.CreateEventExW, HANDLE, LPSECURITY_ATTRIBUTES, LPCWSTR, DWORD, DWORD)
    CreateEventEx = unicode(CreateEventExW, CreateEventExA)
    CreateSemaphoreExA = declare(kernel32.CreateSemaphoreExA, HANDLE, LPSECURITY_ATTRIBUTES, LONG, LONG, LPCSTR, DWORD, DWORD)
    CreateSemaphoreExW = declare(kernel32.CreateSemaphoreExW, HANDLE, LPSECURITY_ATTRIBUTES, LONG, LONG, LPCWSTR, DWORD, DWORD)
    CreateSemaphoreEx = unicode(CreateSemaphoreExW, CreateSemaphoreExA)
    CREATE_WAITABLE_TIMER_MANUAL_RESET = 0x00000001
    CREATE_WAITABLE_TIMER_HIGH_RESOLUTION = 0x00000002
    CreateWaitableTimerExA = declare(kernel32.CreateWaitableTimerExA, HANDLE, LPSECURITY_ATTRIBUTES, LPCSTR, DWORD, DWORD)
    CreateWaitableTimerExW = declare(kernel32.CreateWaitableTimerExW, HANDLE, LPSECURITY_ATTRIBUTES, LPCWSTR, DWORD, DWORD)
    CreateWaitableTimerEx = unicode(CreateWaitableTimerExW, CreateWaitableTimerExA)
    SYNCHRONIZATION_BARRIER = RTL_BARRIER
    PSYNCHRONIZATION_BARRIER = PRTL_BARRIER
    LPSYNCHRONIZATION_BARRIER = PRTL_BARRIER
    SYNCHRONIZATION_BARRIER_FLAGS_SPIN_ONLY = 0x01
    SYNCHRONIZATION_BARRIER_FLAGS_BLOCK_ONLY = 0x02
    SYNCHRONIZATION_BARRIER_FLAGS_NO_DELETE = 0x04
    EnterSynchronizationBarrier = declare(kernel32.EnterSynchronizationBarrier, BOOL, LPSYNCHRONIZATION_BARRIER, DWORD)
    InitializeSynchronizationBarrier = declare(kernel32.InitializeSynchronizationBarrier, BOOL, LPSYNCHRONIZATION_BARRIER, LONG, LONG)
    DeleteSynchronizationBarrier = declare(kernel32.DeleteSynchronizationBarrier, BOOL, LPSYNCHRONIZATION_BARRIER)
    Sleep = declare(kernel32.Sleep, VOID, DWORD)
    WaitOnAddress = declare(kernelbase.WaitOnAddress, BOOL, PVOID, PVOID, SIZE_T, DWORD)
    WakeByAddressSingle = declare(kernelbase.WakeByAddressSingle, VOID, PVOID)
    WakeByAddressAll = declare(kernelbase.WakeByAddressAll, VOID, PVOID)

    # REGION ***

    # REGION *** Desktop or OneCore Family ***

    SignalObjectAndWait = declare(kernelbase.SignalObjectAndWait, DWORD, HANDLE, HANDLE, DWORD, BOOL)
    # REGION ***

    # REGION *** Application or OneCore Family or Games Partition ***

    WaitForMultipleObjects = declare(kernel32.WaitForMultipleObjects, DWORD, DWORD, PHANDLE, BOOL, DWORD)
    CreateSemaphoreA = declare(kernel32.CreateSemaphoreA, HANDLE, LPSECURITY_ATTRIBUTES, LONG, LONG, LPCSTR)
    CreateSemaphoreW = declare(kernel32.CreateSemaphoreW, HANDLE, LPSECURITY_ATTRIBUTES, LONG, LONG, LPCWSTR)
    CreateSemaphore = unicode(CreateSemaphoreW, CreateSemaphoreA)

    CreateWaitableTimerA = declare(kernel32.CreateWaitableTimerA, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, LPCSTR)
    CreateWaitableTimerW = declare(kernel32.CreateWaitableTimerW, HANDLE, LPSECURITY_ATTRIBUTES, BOOL, LPCWSTR)
    CreateWaitableTimer = unicode(CreateWaitableTimerW, CreateWaitableTimerA)

    # REGION ***
# _SYNCHAPI_H_