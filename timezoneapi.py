# begin_1_0
"""
/********************************************************************************
*                                                                               *
* timezoneapi.h -- ApiSet Contract for api-ms-win-core-timezone-l1              *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc
from .defbase import *

from .sdkddkver import *
from .winbase import *
from .fileapi import *

# end_1_0

if cpreproc.pragma_once("_TIMEZONEAPI_H_"):
    
    advapi32 = W_WinDLL("advapi32.dll")
    kernel32 = W_WinDLL("kernel32.dll")
    
    # REGION *** Application Family or OneCore Family or Games Family ***
    
    # begin_1_0
    
    TIME_ZONE_ID_INVALID = 0xFFFFFFFF
    
    class _TIME_ZONE_INFORMATION(CStructure):
        _fields_ = [
            ("Bias", LONG),
            ("StandardName", WCHAR * 32),
            ("StandardDate", SYSTEMTIME),
            ("StandardBias", LONG),
            ("DaylightName", WCHAR * 32),
            ("DaylightDate", SYSTEMTIME),
            ("DaylightBias", LONG)
        ]
    TIME_ZONE_INFORMATION = _TIME_ZONE_INFORMATION
    LPTIME_ZONE_INFORMATION = PTIME_ZONE_INFORMATION = POINTER(TIME_ZONE_INFORMATION)
    
    class _TIME_DYNAMIC_ZONE_INFORMATION(CStructure):
        _fields_ = [
            ("Bias", LONG),
            ("StandardName", WCHAR * 32),
            ("StandardDate", SYSTEMTIME),
            ("StandardBias", LONG),
            ("DaylightName", WCHAR * 32),
            ("DaylightDate", SYSTEMTIME),
            ("DaylightBias", LONG),
            ("TimeZoneKeyName", WCHAR * 128),
            ("DynamicDaylightTimeDisabled", BOOLEAN)
        ]
    DYNAMIC_TIME_ZONE_INFORMATION = _TIME_DYNAMIC_ZONE_INFORMATION
    PDYNAMIC_TIME_ZONE_INFORMATION = POINTER(DYNAMIC_TIME_ZONE_INFORMATION)
    
    SystemTimeToTzSpecificLocalTime = declare(kernel32.SystemTimeToTzSpecificLocalTime, BOOL, PTIME_ZONE_INFORMATION, PSYSTEMTIME, LPSYSTEMTIME)
    TzSpecificLocalTimeToSystemTime = declare(kernel32.TzSpecificLocalTimeToSystemTime, BOOL, PTIME_ZONE_INFORMATION, PSYSTEMTIME, LPSYSTEMTIME)
    FileTimeToSystemTime = declare(kernel32.FileTimeToSystemTime, BOOL, PFILETIME, LPSYSTEMTIME)
    SystemTimeToFileTime = declare(kernel32.SystemTimeToFileTime, BOOL, PSYSTEMTIME, LPFILETIME)
    GetTimeZoneInformation = declare(kernel32.GetTimeZoneInformation, DWORD, LPTIME_ZONE_INFORMATION)
    SetTimeZoneInformation = declare(kernel32.SetTimeZoneInformation, BOOL, PTIME_ZONE_INFORMATION)
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        SetDynamicTimeZoneInformation = declare(kernel32.SetDynamicTimeZoneInformation, BOOL, PDYNAMIC_TIME_ZONE_INFORMATION)
    # _WINVER >= 0x0600
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_VISTA:
        GetDynamicTimeZoneInformation = declare(kernel32.GetDynamicTimeZoneInformation, DWORD, PDYNAMIC_TIME_ZONE_INFORMATION)
    # _WINVER >= 0x0600
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN7:
        GetTimeZoneInformationForYear = declare(kernel32.GetTimeZoneInformationForYear, BOOL, USHORT, PDYNAMIC_TIME_ZONE_INFORMATION, LPTIME_ZONE_INFORMATION)
    # _WINVER >= 0x0601
    # end_1_0
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN8:
        EnumDynamicTimeZoneInformation = declare(advapi32.EnumDynamicTimeZoneInformation, DWORD, DWORD, PDYNAMIC_TIME_ZONE_INFORMATION)
        GetDynamicTimeZoneInformationEffectiveYears = declare(advapi32.GetDynamicTimeZoneInformationEffectiveYears, DWORD, PDYNAMIC_TIME_ZONE_INFORMATION, LPDWORD, LPDWORD)
        SystemTimeToTzSpecificLocalTimeEx = declare(kernel32.SystemTimeToTzSpecificLocalTimeEx, BOOL, PDYNAMIC_TIME_ZONE_INFORMATION, PSYSTEMTIME, LPSYSTEMTIME)
        TzSpecificLocalTimeToSystemTimeEx = declare(kernel32.TzSpecificLocalTimeToSystemTimeEx, BOOL, PDYNAMIC_TIME_ZONE_INFORMATION, PSYSTEMTIME, LPSYSTEMTIME)
    #(_WINVER >= _WIN32_WINNT_WIN8)
    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN10:
        LocalFileTimeToLocalSystemTime = declare(kernel32.LocalFileTimeToLocalSystemTime, BOOL, PTIME_ZONE_INFORMATION, PFILETIME, PSYSTEMTIME)
        LocalSystemTimeToLocalFileTime = declare(kernel32.LocalSystemTimeToLocalFileTime, BOOL, PTIME_ZONE_INFORMATION, PSYSTEMTIME, PFILETIME)
    #(_WINVER >= WIN32_WINNT_WIN10)
    
    # REGION ***