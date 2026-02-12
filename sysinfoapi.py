from .minwindef import *

from .winnt import (DWORD_PTR, DWORDLONG, VOID,
                    PSYSTEMTIME, LPSYSTEMTIME, ULONGLONG, 
                    PDWORD64, UCHAR, PVOID, 
                    PULONGLONG, DWORD64, PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION,
                    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION, LOGICAL_PROCESSOR_RELATIONSHIP,
                    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX, LPOSVERSIONINFOA, LPOSVERSIONINFOW)

from .defbase import *

import sys

from typing import (Callable)

from . import cpreproc

if cpreproc.pragma_once("_SYSINFOAPI_H_"):
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    class _S_WW(CStructure):
        _fields_ = [
            ("wProcessorArchitecture", WORD),
            ("wReserved", WORD)
        ]

    class _U_DS(Union):
        _fields_ = [
            ("dwOemId", DWORD), # Obsolete field...do not use
            ("s", _S_WW)
        ]

    class _SYSTEM_INFO(CStructure):
        _fields_ = [
            ("u", _U_DS),
            ("dwPageSize", DWORD),
            ("lpMinimumApplicationAddress", LPVOID),
            ("lpMaximumApplicationAddress", LPVOID),
            ("dwActiveProcessorMask", DWORD_PTR),
            ("dwNumberOfProcessors", DWORD),
            ("dwProcessorType", DWORD),
            ("dwAllocationGranularity", WORD),
            ("wProcessorLevel", WORD),
            ("wProcessorRevision", WORD)
        ]
    SYSTEM_INFO = _SYSTEM_INFO
    LPSYSTEM_INFO = POINTER(SYSTEM_INFO)

    class _MEMORYSTATUSEX(CStructure):
        _fields_ = [
            ("dwLength", DWORD),
            ("dwMemoryLoad", DWORD),
            ("ullTotalPhys", DWORDLONG),
            ("ullAvailPhys", DWORDLONG),
            ("ullTotalPageFile", DWORDLONG),
            ("ullAvailPageFile", DWORDLONG),
            ("ullTotalVirtual", DWORDLONG),
            ("ullAvailVirtual", DWORDLONG),
            ("ullAvailExtendedVirtual", DWORDLONG)
        ]
    MEMORYSTATUSEX = _MEMORYSTATUSEX
    LPMEMORYSTATUSEX = POINTER(MEMORYSTATUSEX)

    USER_CET_ENVIRONMENT_WIN32_PROCESS = 0x00000000
    USER_CET_ENVIRONMENT_SGX2_ENCLAVE = 0x00000002
    USER_CET_ENVIRONMENT_VBS_ENCLAVE = 0x00000010
    USER_CET_ENVIRONMENT_VBS_BASIC_ENCLAVE = 0x00000011
    GlobalMemoryStatusEx = declare(kernel32.GlobalMemoryStatusEx, BOOL, LPMEMORYSTATUSEX)
    GetSystemInfo = declare(kernel32.GetSystemInfo, VOID, LPSYSTEM_INFO)
    GetSystemTime = declare(kernel32.GetSystemTime, VOID, LPSYSTEMTIME)
    GetSystemTimeAsFileTime = declare(kernel32.GetSystemTimeAsFileTime, VOID, LPFILETIME)
    GetLocalTime = declare(kernel32.GetLocalTime, VOID, LPSYSTEMTIME)
    IsUserCetAvailableInEnvironment = declare(kernel32.IsUserCetAvailableInEnvironment, BOOL, DWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetSystemLeapSecondInformation = declare(kernelbase.GetSystemLeapSecondInformation, BOOL, PBOOL, PDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetVersion = declare(kernel32.GetVersion, DWORD, VOID)
    SetLocalTime = declare(kernel32.SetLocalTime, BOOL, PSYSTEMTIME)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetTickCount = declare(kernel32.GetTickCount, DWORD, VOID)
    GetTickCount64 = declare(kernel32.GetTickCount64, ULONGLONG, VOID)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetSystemTimeAdjustment = declare(kernel32.GetSystemTimeAdjustment, BOOL, PDWORD, PDWORD, PBOOL)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetSystemTimeAdjustmentPrecise = declare(kernelbase.GetSystemTimeAdjustmentPrecise, BOOL, PDWORD64, PDWORD64, PBOOL)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetSystemDirectoryA = declare(kernel32.GetSystemDirectoryA, UINT, LPSTR, UINT)
    GetSystemDirectoryW = declare(kernel32.GetSystemDirectoryW, UINT, LPWSTR, UINT)
    GetSystemDirectory = unicode(GetSystemDirectoryW, GetSystemDirectoryA)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetWindowsDirectoryA = declare(kernel32.GetWindowsDirectoryA, UINT, LPSTR, UINT)
    GetWindowsDirectoryW = declare(kernel32.GetWindowsDirectoryW, UINT, LPWSTR, UINT)
    GetWindowsDirectory = unicode(GetWindowsDirectoryW, GetWindowsDirectoryA)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetSystemWindowsDirectoryA = declare(kernel32.GetSystemWindowsDirectoryA, UINT, LPSTR, UINT)
    GetSystemWindowsDirectoryW = declare(kernel32.GetSystemWindowsDirectoryW, UINT, LPWSTR, UINT)
    GetSystemWindowsDirectory = unicode(GetSystemWindowsDirectoryW, GetSystemWindowsDirectoryA)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    _COMPUTER_NAME_FORMAT = INT
    if True:
        ComputerNameNetBIOS = 0
        ComputerNameDnsHostname = 1
        ComputerNameDnsDomain = 2
        ComputerNameDnsFullyQualified = 3
        ComputerNamePhysicalNetBIOS = 4
        ComputerNamePhysicalDnsHostname = 5
        ComputerNamePhysicalDnsDomain = 6
        ComputerNamePhysicalDnsFullyQualified = 7
        ComputerNameMax = 8
    COMPUTER_NAME_FORMAT = _COMPUTER_NAME_FORMAT

    GetComputerNameExA = declare(kernel32.GetComputerNameExA, BOOL, COMPUTER_NAME_FORMAT, LPSTR, LPDWORD)
    GetComputerNameExW = declare(kernel32.GetComputerNameExW, BOOL, COMPUTER_NAME_FORMAT, LPWSTR, LPDWORD)
    GetComputerNameEx = unicode(GetComputerNameExW, GetComputerNameExA)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    SetComputerNameExW = declare(kernel32.SetComputerNameExW, BOOL, COMPUTER_NAME_FORMAT, LPCWSTR)
    if cpreproc.ifdef("UNICODE"):
        SetComputerNameEx = SetComputerNameExW
    SetSystemTime = declare(kernel32.SetSystemTime, BOOL, PSYSTEMTIME)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetVersionExA = declare(kernel32.GetVersionExA, BOOL, LPOSVERSIONINFOA)
    GetVersionExW = declare(kernel32.GetVersionExW, BOOL, LPOSVERSIONINFOW)
    GetVersionEx = unicode(GetVersionExW, GetVersionExA)
    GetLogicalProcessorInformation = declare(kernel32.GetLogicalProcessorInformation, BOOL, PSYSTEM_LOGICAL_PROCESSOR_INFORMATION, PDWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetLogicalProcessorInformationEx = declare(kernel32.GetLogicalProcessorInformationEx, BOOL, LOGICAL_PROCESSOR_RELATIONSHIP, PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX, PDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetNativeSystemInfo = declare(kernel32.GetNativeSystemInfo, VOID, LPSYSTEM_INFO)
    GetSystemTimePreciseAsFileTime = declare(kernel32.GetSystemTimePreciseAsFileTime, VOID, LPFILETIME)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetProductInfo = declare(kernel32.GetProductInfo, BOOL, DWORD, DWORD, DWORD, DWORD, PDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    VerSetConditionMask = declare(kernel32.VerSetConditionMask, ULONGLONG, ULONGLONG, ULONG, UCHAR)
    GetOsSafeBootMode = declare(kernelbase.GetOsSafeBootMode, BOOL, PDWORD)

    # REGION ***

    # REGION *** OneCore Family or App Family ***

    EnumSystemFirmwareTables = declare(kernel32.EnumSystemFirmwareTables, UINT, DWORD, PVOID, DWORD)
    GetSystemFirmwareTable = declare(kernel32.GetSystemFirmwareTable, UINT, DWORD, DWORD, PVOID, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    DnsHostnameToComputerNameExW = declare(kernel32.DnsHostnameToComputerNameExW, BOOL, LPCWSTR, LPWSTR, LPDWORD)
    GetPhysicallyInstalledSystemMemory = declare(kernel32.GetPhysicallyInstalledSystemMemory, BOOL, PULONGLONG)
    SCEX2_ALT_NETBIOS_NAME = 0x00000001
    SetComputerNameEx2W = declare(kernel32.SetComputerNameEx2W, BOOL, COMPUTER_NAME_FORMAT, DWORD, LPCWSTR)
    if cpreproc.ifdef("UNICODE"):
        SetComputerNameEx2 = SetComputerNameEx2W
    SetSystemTimeAdjustment = declare(kernel32.SetSystemTimeAdjustment, BOOL, DWORD, BOOL)
    SetSystemTimeAdjustmentPrecise = declare(kernelbase.SetSystemTimeAdjustmentPrecise, BOOL, DWORD64, BOOL)
    InstallELAMCertificateInfo = declare(kernel32.InstallELAMCertificateInfo, BOOL, HANDLE)

    # REGION ***
    GetProcessorSystemCycleTime = declare(kernel32.GetProcessorSystemCycleTime, BOOL, USHORT, PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION, PDWORD)

    # REGION *** Desktop Family or OneCore Family ***

    GetOsManufacturingMode = declare(kernelbase.GetOsManufacturingMode, BOOL, PBOOL)

    # REGION ***

    # REGION *** App Family or OneCore Family ***

    GetIntegratedDisplaySize = declare(kernelbase.GetIntegratedDisplaySize, HRESULT, POINTER(DOUBLE))

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    SetComputerNameA = declare(kernel32.SetComputerNameA, BOOL, LPCSTR)
    SetComputerNameW = declare(kernel32.SetComputerNameW, BOOL, LPCWSTR)
    SetComputerName = unicode(SetComputerNameW, SetComputerNameA)
    SetComputerNameExA = declare(kernel32.SetComputerNameExA, BOOL, COMPUTER_NAME_FORMAT, LPCSTR)
    if cpreproc.ifndef("UNICODE"):
        SetComputerNameEx = SetComputerNameExA

    # REGION ***