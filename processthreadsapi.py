"""
************************************************************************************
*                                                                                  *
* processthreadsapi.h -- ApiSet Contract for api-ms-win-core-processthreads-l1     *
*                                                                                  *
* Copyright (c) Microsoft Corporation. All rights reserved.                        *
*                                                                                  *
************************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .winbase import LPTHREAD_START_ROUTINE
from .winnt import (PVOID, LPSECURITY_ATTRIBUTES, DWORD_PTR, 
                   SIZE_T, ULONG_PTR, PAPCFUNC, 
                   PULONG_PTR, CONTEXT, PROCESS_MITIGATION_POLICY, PPROCESSOR_NUMBER, 
                   PPROCESS_DYNAMIC_EH_CONTINUATION_TARGET, PPROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE, PSIZE_T,
                   LPCGUID, PCWSTR, PWSTR,
                   ULONG64, PSYSTEM_CPU_SET_INFORMATION,
                   VOID)

from typing import (Callable)

from .defbase import *

if cpreproc.pragma_once("_PROCESSTHREADSAPI_H_"):
    
    kernel32 = W_WinDLL("kernel32.dll")
    
    # REGION *** Application Family or OneCore Family or Games Family ***

    class _PROCESS_INFORMATION(CStructure):
        _fields_ = [
            ("hProcess", HANDLE),
            ("hThread", HANDLE),
            ("dwProcessId", DWORD),
            ("dwThreadId", DWORD)
        ]
    PROCESS_INFORMATION = _PROCESS_INFORMATION
    PPROCESS_INFORMATION = POINTER(PROCESS_INFORMATION)
    LPPROCESS_INFORMATION = PPROCESS_INFORMATION

    class _STARTUPINFOA(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("lpReserved", LPSTR),
            ("lpDesktop", LPSTR),
            ("lpTitle", LPSTR),
            ("dwX", DWORD),
            ("dwY", DWORD),
            ("dwXSize", DWORD),
            ("dwYSize", DWORD),
            ("dwXCountChars", DWORD),
            ("dwYCountChars", DWORD),
            ("dwFlags", DWORD),
            ("wShowWindow", WORD),
            ("cbReserved2", WORD),
            ("lpReserved2", LPBYTE),
            ("hStdInput", HANDLE),
            ("hStdOutput", HANDLE),
            ("hStdError", HANDLE)
        ]
    STARTUPINFOA = _STARTUPINFOA
    LPSTARTUPINFOA = POINTER(STARTUPINFOA)

    class _STARTUPINFOW(CStructure):
        _fields_ = [
            ("cb", DWORD),
            ("lpReserved", LPWSTR),
            ("lpDesktop", LPWSTR),
            ("lpTitle", LPWSTR),
            ("dwX", DWORD),
            ("dwY", DWORD),
            ("dwXSize", DWORD),
            ("dwYSize", DWORD),
            ("dwXCountChars", DWORD),
            ("dwYCountChars", DWORD),
            ("dwFlags", DWORD),
            ("wShowWindow", WORD),
            ("cbReserved2", WORD),
            ("lpReserved2", LPBYTE),
            ("hStdInput", HANDLE),
            ("hStdOutput", HANDLE),
            ("hStdError", HANDLE)
        ]

    STARTUPINFOW = _STARTUPINFOW
    LPSTARTUPINFOW = POINTER(STARTUPINFOW)

    STARTUPINFO = unicode(STARTUPINFOW, STARTUPINFOA)
    LPSTARTUPINFO = unicode(LPSTARTUPINFOW, LPSTARTUPINFOA)

    QueueUserAPC = declare(kernel32.QueueUserAPC, DWORD, PAPCFUNC, HANDLE, ULONG_PTR)
    # _WIN32_WINNT >= 0x0400 || _WIN32_WINDOWS > 0x0400
    GetProcessTimes = declare(kernel32.GetProcessTimes, BOOL, HANDLE, LPFILETIME, LPFILETIME, LPFILETIME, LPFILETIME)
    GetCurrentProcess = declare(kernel32.GetCurrentProcess, HANDLE, VOID)
    GetCurrentProcessId = declare(kernel32.GetCurrentProcessId, DWORD, VOID)
    ExitProcess = declare(kernel32.ExitProcess, VOID, UINT)
    TerminateProcess = declare(kernel32.TerminateProcess, BOOL, HANDLE, UINT)
    GetExitCodeProcess = declare(kernel32.GetExitCodeProcess, BOOL, HANDLE, LPDWORD)
    SwitchToThread = declare(kernel32.SwitchToThread, BOOL, VOID)
    CreateThread = declare(kernel32.CreateThread, HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    CreateRemoteThread = declare(kernel32.CreateRemoteThread, HANDLE, HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetCurrentThread = declare(kernel32.GetCurrentThread, HANDLE, VOID)
    GetCurrentThreadId = declare(kernel32.GetCurrentThreadId, DWORD, VOID)
    OpenThread = declare(kernel32.OpenThread, HANDLE, DWORD, BOOL, DWORD)
    SetThreadPriority = declare(kernel32.SetThreadPriority, BOOL, HANDLE, INT)
    SetThreadPriorityBoost = declare(kernel32.SetThreadPriorityBoost, BOOL, HANDLE, BOOL)
    GetThreadPriorityBoost = declare(kernel32.GetThreadPriorityBoost, BOOL, HANDLE, PBOOL)
    GetThreadPriority = declare(kernel32.GetThreadPriority, INT, HANDLE)
    ExitThread = declare(kernel32.ExitThread, VOID, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    TerminateThread = declare(kernel32.TerminateThread, BOOL, HANDLE, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetExitCodeThread = declare(kernel32.GetExitCodeThread, BOOL, HANDLE, LPDWORD)
    SuspendThread = declare(kernel32.SuspendThread, DWORD, HANDLE)
    ResumeThread = declare(kernel32.ResumeThread, DWORD, HANDLE)
    if cpreproc.ifndef("TLS_OUT_OF_INDEXES"):
        TLS_OUT_OF_INDEXES = (DWORD(0xFFFFFFFF)).value
    TlsAlloc = declare(kernel32.TlsAlloc, DWORD, VOID)
    TlsGetValue = declare(kernel32.TlsGetValue, LPVOID, DWORD)
    TlsSetValue = declare(kernel32.TlsSetValue, BOOL, DWORD, LPVOID)
    TlsFree = declare(kernel32.TlsFree, BOOL, DWORD)
    CreateProcessA = declare(kernel32.CreateProcessA, BOOL, LPCSTR, LPSTR, LPSECURITY_ATTRIBUTES, LPSECURITY_ATTRIBUTES, BOOL, DWORD, LPVOID, LPCSTR, LPSTARTUPINFOA, LPPROCESS_INFORMATION)
    CreateProcessW = declare(kernel32.CreateProcessW, BOOL, LPCWSTR, LPWSTR, LPSECURITY_ATTRIBUTES, LPSECURITY_ATTRIBUTES, BOOL, DWORD, LPVOID, LPCWSTR, LPSTARTUPINFOW, LPPROCESS_INFORMATION)
    CreateProcess = unicode(CreateProcessW, CreateProcessA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    SetProcessShutdownParameters = declare(kernel32.SetProcessShutdownParameters, BOOL, DWORD, DWORD)
    GetProcessVersion = declare(kernel32.GetProcessVersion, DWORD, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetStartupInfoW = declare(kernel32.GetStartupInfoW, VOID, LPSTARTUPINFOW)
    if cpreproc.ifdef("UNICODE"):
        GetStartupInfo = GetStartupInfoW
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    CreateProcessAsUserW = declare(kernel32.CreateProcessAsUserW, BOOL, HANDLE, LPCWSTR, LPWSTR, LPSECURITY_ATTRIBUTES, LPSECURITY_ATTRIBUTES, BOOL, DWORD, LPVOID, LPCWSTR, LPSTARTUPINFOW, LPPROCESS_INFORMATION)
    if cpreproc.ifdef("UNICODE"):
        CreateProcessAsUser = CreateProcessAsUserW
    #
    # TODO: neerajsi-2013/12/08 - this should be moved to official documentation.
    #
    # These are shorthand ways of referring to the thread token, the process token,
    # or the "effective token" (the thread token if it exists, otherwise the
    # process token), respectively. These handles only have TOKEN_QUERY and
    # TOKEN_QUERY_SOURCE access in Windows 8 (use TOKEN_ACCESS_PSEUDO_HANDLE to
    # determine the granted access on the target version of Windows). These handles
    # do not need to be closed.
    #
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    SetThreadToken = declare(kernel32.SetThreadToken, BOOL, PHANDLE, HANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    OpenProcessToken = declare(kernel32.OpenProcessToken, BOOL, HANDLE, DWORD, PHANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    OpenThreadToken = declare(kernel32.OpenThreadToken, BOOL, HANDLE, DWORD, BOOL, PHANDLE)
    SetPriorityClass = declare(kernel32.SetPriorityClass, BOOL, HANDLE, DWORD)
    GetPriorityClass = declare(kernel32.GetPriorityClass, DWORD, HANDLE)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    SetThreadStackGuarantee = declare(kernel32.SetThreadStackGuarantee, BOOL, PULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    ProcessIdToSessionId = declare(kernel32.ProcessIdToSessionId, BOOL, DWORD, PDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    PPROC_THREAD_ATTRIBUTE_LIST = PVOID
    LPPROC_THREAD_ATTRIBUTE_LIST = PPROC_THREAD_ATTRIBUTE_LIST

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetProcessId = declare(kernel32.GetProcessId, DWORD, HANDLE)
    GetThreadId = declare(kernel32.GetThreadId, DWORD, HANDLE)
    FlushProcessWriteBuffers = declare(kernel32.FlushProcessWriteBuffers, VOID, VOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetProcessIdOfThread = declare(kernel32.GetProcessIdOfThread, DWORD, HANDLE)
    InitializeProcThreadAttributeList = declare(kernel32.InitializeProcThreadAttributeList, BOOL, LPPROC_THREAD_ATTRIBUTE_LIST, DWORD, DWORD, PSIZE_T)
    DeleteProcThreadAttributeList = declare(kernel32.DeleteProcThreadAttributeList, VOID, LPPROC_THREAD_ATTRIBUTE_LIST)
    PROC_THREAD_ATTRIBUTE_REPLACE_VALUE = 0x00000001
    UpdateProcThreadAttribute = declare(kernel32.UpdateProcThreadAttribute, BOOL, LPPROC_THREAD_ATTRIBUTE_LIST, DWORD, DWORD_PTR, PVOID, SIZE_T, PVOID, PSIZE_T)
    SetProcessDynamicEHContinuationTargets = declare(kernel32.SetProcessDynamicEHContinuationTargets, BOOL, HANDLE, USHORT, PPROCESS_DYNAMIC_EH_CONTINUATION_TARGET)
    SetProcessDynamicEnforcedCetCompatibleRanges = declare(kernel32.SetProcessDynamicEnforcedCetCompatibleRanges, BOOL, HANDLE, USHORT, PPROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    PROCESS_AFFINITY_ENABLE_AUTO_UPDATE = 0x00000001
    SetProcessAffinityUpdateMode = declare(kernel32.SetProcessAffinityUpdateMode, BOOL, HANDLE, DWORD)
    QueryProcessAffinityUpdateMode = declare(kernel32.QueryProcessAffinityUpdateMode, BOOL, HANDLE, LPDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    CreateRemoteThreadEx = declare(kernel32.CreateRemoteThreadEx, HANDLE, HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPPROC_THREAD_ATTRIBUTE_LIST, LPDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetCurrentThreadStackLimits = declare(kernel32.GetCurrentThreadStackLimits, VOID, PULONG_PTR, PULONG_PTR)
    GetThreadContext = declare(kernel32.GetThreadContext, BOOL, HANDLE, POINTER(CONTEXT))

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetProcessMitigationPolicy = declare(kernel32.GetProcessMitigationPolicy, BOOL, HANDLE, PROCESS_MITIGATION_POLICY, PVOID, SIZE_T)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    SetThreadContext = declare(kernel32.SetThreadContext, BOOL, HANDLE, POINTER(CONTEXT))

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    SetProcessMitigationPolicy = declare(kernel32.SetProcessMitigationPolicy, BOOL, PROCESS_MITIGATION_POLICY, PVOID, SIZE_T)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    FlushInstructionCache = declare(kernel32.FlushInstructionCache, BOOL, HANDLE, LPCVOID, SIZE_T)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetThreadTimes = declare(kernel32.GetThreadTimes, BOOL, HANDLE, LPFILETIME, LPFILETIME, LPFILETIME, LPFILETIME)
    OpenProcess = declare(kernel32.OpenProcess, HANDLE, DWORD, BOOL, DWORD)
    IsProcessorFeaturePresent = declare(kernel32.IsProcessorFeaturePresent, BOOL, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetProcessHandleCount = declare(kernel32.GetProcessHandleCount, BOOL, HANDLE, PDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetCurrentProcessorNumber = declare(kernel32.GetCurrentProcessorNumber, DWORD, VOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    SetThreadIdealProcessorEx = declare(kernel32.SetThreadIdealProcessorEx, BOOL, HANDLE, PPROCESSOR_NUMBER, PPROCESSOR_NUMBER)
    GetThreadIdealProcessorEx = declare(kernel32.GetThreadIdealProcessorEx, BOOL, HANDLE, PPROCESSOR_NUMBER)
    GetCurrentProcessorNumberEx = declare(kernel32.GetCurrentProcessorNumberEx, VOID, PPROCESSOR_NUMBER)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetProcessPriorityBoost = declare(kernel32.GetProcessPriorityBoost, BOOL, HANDLE, PBOOL)
    SetProcessPriorityBoost = declare(kernel32.SetProcessPriorityBoost, BOOL, HANDLE, BOOL)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetThreadIOPendingFlag = declare(kernel32.GetThreadIOPendingFlag, BOOL, HANDLE, PBOOL)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetSystemTimes = declare(kernel32.GetSystemTimes, BOOL, PFILETIME, PFILETIME, PFILETIME)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    #
    # Thread information classes.
    #
    _THREAD_INFORMATION_CLASS = INT
    if True:
        ThreadMemoryPriority = 0
        ThreadAbsoluteCpuPriority = 1
        ThreadDynamicCodePolicy = 2
        ThreadPowerThrottling = 3
        ThreadInformationClassMax = 4
    THREAD_INFORMATION_CLASS = _THREAD_INFORMATION_CLASS

    class _MEMORY_PRIORITY_INFORMATION(CStructure):
        _fields_ = [
            ("MemoryPriority", ULONG)
        ]
    MEMORY_PRIORITY_INFORMATION = _MEMORY_PRIORITY_INFORMATION
    PMEMORY_PRIORITY_INFORMATION = POINTER(MEMORY_PRIORITY_INFORMATION)

    GetThreadInformation = declare(kernel32.GetThreadInformation, BOOL, HANDLE, THREAD_INFORMATION_CLASS, LPVOID, DWORD)
    SetThreadInformation = declare(kernel32.SetThreadInformation, BOOL, HANDLE, THREAD_INFORMATION_CLASS, LPVOID, DWORD)

    THREAD_POWER_THROTTLING_CURRENT_VERSION = 1
    THREAD_POWER_THROTTLING_EXECUTION_SPEED = 0x1
    THREAD_POWER_THROTTLING_VALID_FLAGS = (THREAD_POWER_THROTTLING_EXECUTION_SPEED)

    class _THREAD_POWER_THROTTLING_STATE(CStructure):
        _fields_ = [
            ("Version", ULONG),
            ("ControlMask", ULONG),
            ("StateMask", ULONG)
        ]
    THREAD_POWER_THROTTLING_STATE = _THREAD_POWER_THROTTLING_STATE

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    IsProcessCritical = declare(kernel32.IsProcessCritical, BOOL, HANDLE, PBOOL)
    SetProtectedPolicy = declare(kernel32.SetProtectedPolicy, BOOL, LPCGUID, ULONG_PTR, PULONG_PTR)
    QueryProtectedPolicy = declare(kernel32.QueryProtectedPolicy, BOOL, LPCGUID, PULONG_PTR)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    SetThreadIdealProcessor = declare(kernel32.SetThreadIdealProcessor, DWORD, HANDLE, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    _PROCESS_INFORMATION_CLASS = INT
    if True:
        ProcessMemoryPriority = 0
        ProcessMemoryExhaustionInfo = 1
        ProcessAppMemoryInfo = 2
        ProcessInPrivateInfo = 3
        ProcessPowerThrottling = 4
        ProcessReservedValue1 = 5 # Used to be for ProcessActivityThrottlePolicyInfo
        ProcessTelemetryCoverageInfo = 6
        ProcessProtectionLevelInfo = 7
        ProcessLeapSecondInfo = 8
        ProcessInformationClassMax = 9
    PROCESS_INFORMATION_CLASS = _PROCESS_INFORMATION_CLASS

    class _APP_MEMORY_INFORMATION(CStructure):
        _fields_ = [
            ("AvailableCommit", ULONG64),
            ("PrivateCommitUsage", ULONG64),
            ("PeakPrivateCommitUsage", ULONG64),
            ("TotalCommitUsage", ULONG64)
        ]
    APP_MEMORY_INFORMATION = _APP_MEMORY_INFORMATION
    PAPP_MEMORY_INFORMATION = POINTER(APP_MEMORY_INFORMATION)

    #
    # Constants and structures needed to enable the fail fast on commit failure
    # feature.
    #

    PME_CURRENT_VERSION = 1

    _PROCESS_MEMORY_EXHAUSTION_TYPE = INT
    if True:
        PMETypeFailFastOnCommitFailure = 0
        PMETypeMax = 1
    PROCESS_MEMORY_EXHAUSTION_TYPE = _PROCESS_MEMORY_EXHAUSTION_TYPE
    PPROCESS_MEMORY_EXHAUSTION_TYPE = POINTER(PROCESS_MEMORY_EXHAUSTION_TYPE)

    PME_FAILFAST_ON_COMMIT_FAIL_DISABLE = 0x0
    PME_FAILFAST_ON_COMMIT_FAIL_ENABLE = 0x1

    class _PROCESS_MEMORY_EXHAUSTION_INFO(CStructure):
        _fields_ = [
            ("Version", USHORT),
            ("Reserved", USHORT),
            ("Type", PROCESS_MEMORY_EXHAUSTION_TYPE),
            ("Value", ULONG_PTR)
        ]
    PROCESS_MEMORY_EXHAUSTION_INFO = _PROCESS_MEMORY_EXHAUSTION_INFO
    PPROCESS_MEMORY_EXHAUSTION_INFO = POINTER(PROCESS_MEMORY_EXHAUSTION_INFO)

    PROCESS_POWER_THROTTLING_CURRENT_VERSION = 1

    PROCESS_POWER_THROTTLING_EXECUTION_SPEED = 0x1

    PROCESS_POWER_THROTTLING_VALID_FLAGS = (PROCESS_POWER_THROTTLING_EXECUTION_SPEED)

    class _PROCESS_POWER_THROTTLING_STATE(CStructure):
        _fields_ = [
            ("Version", ULONG),
            ("ControlMask", ULONG),
            ("StateMask", ULONG)
        ]
    PROCESS_POWER_THROTTLING_STATE = _PROCESS_POWER_THROTTLING_STATE
    PPROCESS_POWER_THROTTLING_STATE = POINTER(PROCESS_POWER_THROTTLING_STATE)

    class PROCESS_PROTECTION_LEVEL_INFORMATION(CStructure):
        _fields_ = [
            ("ProtectionLevel", DWORD)
        ]

    PROCESS_LEAP_SECOND_INFO_FLAG_ENABLE_SIXTY_SECOND = 0x1

    PROCESS_LEAP_SECOND_INFO_VALID_FLAGS = (PROCESS_LEAP_SECOND_INFO_FLAG_ENABLE_SIXTY_SECOND)

    class _PROCESS_LEAP_SECOND_INFO(CStructure):
        _fields_ = [
            ("Flags", ULONG),
            ("Reserved", ULONG)
        ]
    PROCESS_LEAP_SECOND_INFO = _PROCESS_LEAP_SECOND_INFO
    PPROCESS_LEAP_SECOND_INFO = POINTER(PROCESS_LEAP_SECOND_INFO)

    SetProcessInformation = declare(kernel32.SetProcessInformation, BOOL, HANDLE, PROCESS_INFORMATION_CLASS, LPVOID, DWORD)
    GetProcessInformation = declare(kernel32.GetProcessInformation, BOOL, HANDLE, PROCESS_INFORMATION_CLASS, LPVOID, DWORD)
    #(_WIN32_WINNT >= 0x0602)
    GetSystemCpuSetInformation = declare(kernel32.GetSystemCpuSetInformation, BOOL, PSYSTEM_CPU_SET_INFORMATION, ULONG, PULONG, HANDLE, ULONG)
    GetProcessDefaultCpuSets = declare(kernel32.GetProcessDefaultCpuSets, BOOL, HANDLE, PULONG, ULONG, PULONG)
    SetProcessDefaultCpuSets = declare(kernel32.SetProcessDefaultCpuSets, BOOL, HANDLE, PULONG, ULONG)
    GetThreadSelectedCpuSets = declare(kernel32.GetThreadSelectedCpuSets, BOOL, HANDLE, PULONG, ULONG, PULONG)
    SetThreadSelectedCpuSets = declare(kernel32.SetThreadSelectedCpuSets, BOOL, HANDLE, PULONG, ULONG)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    CreateProcessAsUserA = declare(kernel32.CreateProcessAsUserA, BOOL, HANDLE, LPCSTR, LPSTR, LPSECURITY_ATTRIBUTES, LPSECURITY_ATTRIBUTES, BOOL, DWORD, LPVOID, LPCSTR, LPSTARTUPINFOA, LPPROCESS_INFORMATION)
    if cpreproc.ifndef("UNICODE"):
        CreateProcessAsUser = CreateProcessAsUserA
    GetProcessShutdownParameters = declare(kernel32.GetProcessShutdownParameters, BOOL, LPDWORD, LPDWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***
    SetThreadDescription = declare(kernel32.SetThreadDescription, HRESULT, HANDLE, PCWSTR)
    GetThreadDescription = declare(kernel32.GetThreadDescription, HRESULT, HANDLE, POINTER(PWSTR))

    # REGION ***