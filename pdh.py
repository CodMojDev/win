"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    PDH.H

Abstract:

    Header file for the Performance Data Helper (PDH) DLL functions.

--"""

from . import cpreproc

from .minwindef import *

from .defbase import *

from .guiddef import GUID

from .sdkddkver import WIN32_WINNT_WINXP

from .winnt import UCHAR, PZZSTR, PZZWSTR

if cpreproc.pragma_once("_PDH_H_"):
    pdh = W_WinDLL("pdh.dll")

    # REGION *** Desktop Family and or PerfCounter Package ***

    # system include files required for datatype and constant definitions

    PDH_STATUS = LONG

    PDH_FUNCTION = lambda func, *args: declare(func, PDH_STATUS, *args)

    # version info
    PDH_CVERSION_WIN40 = 0x0400
    PDH_CVERSION_WIN50 = 0x0500
    # v1.1 revision of PDH -- basic log functions
    # v1.2 of the PDH -- adds variable instance counters
    # v1.3 of the PDH -- adds log service control & stubs for NT5/PDH v2 fn's
    # v2.0 of the PDH -- is the NT v 5.0 B2 version
    PDH_VERSION = (PDH_CVERSION_WIN50) + 0x0003

    # define severity masks
    IsSuccessSeverity = lambda ErrorCode:       ((DWORD(ErrorCode).value & (0xC0000000)) == 0x00000000)
    IsInformationalSeverity = lambda ErrorCode: ((DWORD(ErrorCode).value & (0xC0000000)) == 0x40000000)
    IsWarningSeverity = lambda ErrorCode:       ((DWORD(ErrorCode).value & (0xC0000000)) == 0x80000000)
    IsErrorSeverity = lambda ErrorCode:         ((DWORD(ErrorCode).value & (0xC0000000)) == 0xC0000000)

    MAX_COUNTER_PATH      = 256  # Maximum counter path length. This is an obsolute constance.

    PDH_MAX_COUNTER_NAME =     1024  # Maximum counter name length.
    PDH_MAX_INSTANCE_NAME =    1024  # Maximum counter instance name length.
    PDH_MAX_COUNTER_PATH =     2048  # Maximum full counter path length.
    PDH_MAX_DATASOURCE_PATH = 1024   # MAximum full counter log name length.

    PDH_OBJECT_HAS_INSTANCES =     0x00000001

    # data type definitions

    PDH_HCOUNTER = HANDLE
    PDH_HQUERY = HANDLE
    PDH_HLOG = HANDLE

    HCOUNTER = PDH_HCOUNTER
    HQUERY = PDH_HQUERY
    HLOG = PDH_HLOG

    INVALID_HANDLE_VALUE =   -1

    H_REALTIME_DATASOURCE = NULL
    H_WBEM_DATASOURCE =      INVALID_HANDLE_VALUE

    class PDH_RAW_COUNTER(CStructure):
        _fields_ = [
            ("CStatus", DWORD),
            ("TimeStamp", FILETIME),
            ("FirstValue", LONGLONG),
            ("SecondValue", LONGLONG),
            ("MultiCount", DWORD)
        ]
    PPDH_RAW_COUNTER = POINTER(PDH_RAW_COUNTER)

    class PDH_RAW_COUNTER_ITEM_A(CStructure):
        _fields_ = [
            ("szName", LPSTR),
            ("RawValue", PDH_RAW_COUNTER)
        ]
    PPDH_RAW_COUNTER_ITEM_A = POINTER(PDH_RAW_COUNTER_ITEM_A)

    class PDH_RAW_COUNTER_ITEM_W(CStructure):
        _fields_ = [
            ("szName", LPWSTR),
            ("RawValue", PDH_RAW_COUNTER)
        ]
    PPDH_RAW_COUNTER_ITEM_W = POINTER(PDH_RAW_COUNTER_ITEM_W)

    class PDH_FMT_COUNTERVALUE(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("longValue", LONG),
                ("doubleValue", DOUBLE),
                ("largeValue", LONGLONG),
                ("AnsiStringValue", LPCSTR),
                ("WideStringValue", LPCWSTR)
            ]
        _fields_ = [
            ("CStatus", DWORD),
            ("u", _DUMMYUNIONNAME)
        ]
    PPDH_FMT_COUNTERVALUE = POINTER(PDH_FMT_COUNTERVALUE)

    class PDH_FMT_COUNTERVALUE_ITEM_A(CStructure):
        _fields_ = [
            ("szName", LPSTR),
            ("FmtValue", PDH_FMT_COUNTERVALUE)
        ]
    PPDH_FMT_COUNTERVALUE_ITEM_A = POINTER(PDH_FMT_COUNTERVALUE_ITEM_A)

    class PDH_FMT_COUNTERVALUE_ITEM_W(CStructure):
        _fields_ = [
            ("szName", LPWSTR),
            ("FmtValue", PDH_FMT_COUNTERVALUE)
        ]
    PPDH_FMT_COUNTERVALUE_ITEM_W = POINTER(PDH_FMT_COUNTERVALUE_ITEM_W)

    class PDH_STATISTICS(CStructure):
        _fields_ = [
            ("dwFormat", DWORD),
            ("count", DWORD),
            ("min", PDH_FMT_COUNTERVALUE),
            ("max", PDH_FMT_COUNTERVALUE),
            ("mean", PDH_FMT_COUNTERVALUE)
        ]
    PPDH_STATISTICS = POINTER(PDH_STATISTICS)

    class PDH_COUNTER_PATH_ELEMENTS_A(CStructure):
        _fields_ = [
            ("szMachineName", LPSTR),
            ("szObjectName", LPSTR),
            ("szInstanceName", LPSTR),
            ("szParentInstance", LPSTR),
            ("dwInstanceIndex", DWORD),
            ("szCounterName", LPSTR)
        ]
    PPDH_COUNTER_PATH_ELEMENTS_A = POINTER(PDH_COUNTER_PATH_ELEMENTS_A)

    class PDH_COUNTER_PATH_ELEMENTS_W(CStructure):
        _fields_ = [
            ("szMachineName", LPWSTR),
            ("szObjectName", LPWSTR),
            ("szInstanceName", LPWSTR),
            ("szParentInstance", LPWSTR),
            ("dwInstanceIndex", DWORD),
            ("szCounterName", LPWSTR)
        ]
    PPDH_COUNTER_PATH_ELEMENTS_W = POINTER(PDH_COUNTER_PATH_ELEMENTS_W)

    class PDH_DATA_ITEM_PATH_ELEMENTS_A(CStructure):
        _fields_ = [
            ("szMachineName", LPSTR),
            ("ObjectGUID", GUID),
            ("dwItemId", DWORD),
            ("szInstanceName", LPSTR)
        ]
    PPDH_DATA_ITEM_PATH_ELEMENTS_A = POINTER(PDH_DATA_ITEM_PATH_ELEMENTS_A)

    class PDH_DATA_ITEM_PATH_ELEMENTS_W(CStructure):
        _fields_ = [
            ("szMachineName", LPWSTR),
            ("ObjectGUID", GUID),
            ("dwItemId", DWORD),
            ("szInstanceName", LPWSTR)
        ]
    PPDH_DATA_ITEM_PATH_ELEMENTS_W = POINTER(PDH_DATA_ITEM_PATH_ELEMENTS_W)

    class PDH_COUNTER_INFO_A(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("DataItemPath", PDH_DATA_ITEM_PATH_ELEMENTS_A),
                ("CounterPath", PDH_COUNTER_PATH_ELEMENTS_A)
            ]
        _fields_ = [
            ("dwLength", DWORD),
            ("dwType", DWORD),
            ("CVersion", DWORD),
            ("CStatus", DWORD),
            ("lScale", LONG),
            ("lDefaultScale", LONG),
            ("dwUserData", DWORD_PTR),
            ("dwQueryUserData", DWORD_PTR),
            ("szFullPath", LPSTR),
            ("u", _DUMMYUNIONNAME),
            ("szExplainText", LPSTR),
            ("DataBuffer", DWORD * 1)
        ]
    PPDH_COUNTER_INFO_A = POINTER(PDH_COUNTER_INFO_A)

    class PDH_COUNTER_INFO_W(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("DataItemPath", PDH_DATA_ITEM_PATH_ELEMENTS_W),
                ("CounterPath", PDH_COUNTER_PATH_ELEMENTS_W)
            ]
        _fields_ = [
            ("dwLength", DWORD),
            ("dwType", DWORD),
            ("CVersion", DWORD),
            ("CStatus", DWORD),
            ("lScale", LONG),
            ("lDefaultScale", LONG),
            ("dwUserData", DWORD_PTR),
            ("dwQueryUserData", DWORD_PTR),
            ("szFullPath", LPWSTR),
            ("u", _DUMMYUNIONNAME),
            ("szExplainText", LPWSTR),
            ("DataBuffer", DWORD * 1)
        ]
    PPDH_COUNTER_INFO_W = POINTER(PDH_COUNTER_INFO_W)

    class PDH_TIME_INFO(CStructure):
        _fields_ = [
            ("StartTime", LONGLONG),
            ("EndTime", LONGLONG),
            ("SampleCount", DWORD)
        ]
    PPDH_TIME_INFO = POINTER(PDH_TIME_INFO)

    class PDH_RAW_LOG_RECORD(CStructure):
        _fields_ = [
            ("dwStructureSize", DWORD),
            ("dwRecordType", DWORD),
            ("dwItems", DWORD),
            ("RawBytes", UCHAR * 1)
        ]
    PPDH_RAW_LOG_RECORD = POINTER(PDH_RAW_LOG_RECORD)

    class PDH_LOG_SERVICE_QUERY_INFO_A(CStructure):
        class _DUMMYUNIONNAME(Union):
            class _DUMMYSTRUCTNAME(CStructure):
                _fields_ = [
                    ("PdlAutoNameInterval", DWORD),
                    ("PdlAutoNameUnits", DWORD),
                    ("PdlCommandFilename", LPSTR),
                    ("PdlCounterList", LPSTR),
                    ("PdlAutoNameFormat", DWORD),
                    ("PdlSampleInterval", DWORD),
                    ("PdlLogStartTime", FILETIME),
                    ("PdlLogEndTime", FILETIME)
                ]
            class _DUMMYSTRUCTNAME2(CStructure):
                _fields_ = [
                    ("TlNumberOfBuffers", DWORD),
                    ("TlMinimumBuffers", DWORD),
                    ("TlMaximumBuffers", DWORD),
                    ("TlFreeBuffers", DWORD),
                    ("TlBufferSize", DWORD),
                    ("TlEventsLost", DWORD),
                    ("TlLoggerThreadId", DWORD),
                    ("TlBuffersWritten", DWORD),
                    ("TlLogHandle", DWORD),
                    ("TlLogFileName", LPSTR)
                ]
            _fields_ = [
                ("s", _DUMMYSTRUCTNAME),
                ("s2", _DUMMYSTRUCTNAME2)
            ]
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("dwLogQuota", DWORD),
            ("szLogFileCaption", LPSTR),
            ("szDefaultDir", LPSTR),
            ("szBaseFileName", LPSTR),
            ("dwFileType", DWORD),
            ("dwReserved", DWORD),
            ("u", _DUMMYUNIONNAME)
        ]
    PPDH_LOG_SERVICE_QUERY_INFO_A = POINTER(PDH_LOG_SERVICE_QUERY_INFO_A)

    class PDH_LOG_SERVICE_QUERY_INFO_W(CStructure):
        class _DUMMYUNIONNAME(Union):
            class _DUMMYSTRUCTNAME(CStructure):
                _fields_ = [
                    ("PdlAutoNameInterval", DWORD),
                    ("PdlAutoNameUnits", DWORD),
                    ("PdlCommandFilename", LPWSTR),
                    ("PdlCounterList", LPWSTR),
                    ("PdlAutoNameFormat", DWORD),
                    ("PdlSampleInterval", DWORD),
                    ("PdlLogStartTime", FILETIME),
                    ("PdlLogEndTime", FILETIME)
                ]
            class _DUMMYSTRUCTNAME2(CStructure):
                _fields_ = [
                    ("TlNumberOfBuffers", DWORD),
                    ("TlMinimumBuffers", DWORD),
                    ("TlMaximumBuffers", DWORD),
                    ("TlFreeBuffers", DWORD),
                    ("TlBufferSize", DWORD),
                    ("TlEventsLost", DWORD),
                    ("TlLoggerThreadId", DWORD),
                    ("TlBuffersWritten", DWORD),
                    ("TlLogHandle", DWORD),
                    ("TlLogFileName", LPWSTR)
                ]
            _fields_ = [
                ("s", _DUMMYSTRUCTNAME),
                ("s2", _DUMMYSTRUCTNAME2)
            ]
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("dwLogQuota", DWORD),
            ("szLogFileCaption", LPWSTR),
            ("szDefaultDir", LPWSTR),
            ("szBaseFileName", LPWSTR),
            ("dwFileType", DWORD),
            ("dwReserved", DWORD),
            ("u", _DUMMYUNIONNAME)
        ]
    PPDH_LOG_SERVICE_QUERY_INFO_W = POINTER(PDH_LOG_SERVICE_QUERY_INFO_W)

    #
    #  Time value constants
    #
    MAX_TIME_VALUE = 0x7FFFFFFFFFFFFFFF
    MIN_TIME_VALUE = 0

    # function definitions

    PdhGetDllVersion = PDH_FUNCTION(pdh.PdhGetDllVersion, LPDWORD)
    #
    #  Query Functions
    #
    PdhOpenQueryW = PDH_FUNCTION(pdh.PdhOpenQueryW, LPCWSTR, DWORD_PTR, POINTER(PDH_HQUERY))
    PdhOpenQueryA = PDH_FUNCTION(pdh.PdhOpenQueryA, LPCSTR, DWORD_PTR, POINTER(PDH_HQUERY))
    PdhAddCounterW = PDH_FUNCTION(pdh.PdhAddCounterW, PDH_HQUERY, LPCWSTR, DWORD_PTR, POINTER(PDH_HCOUNTER))
    PdhAddCounterA = PDH_FUNCTION(pdh.PdhAddCounterA, PDH_HQUERY, LPCSTR, DWORD_PTR, POINTER(PDH_HCOUNTER))
    PdhAddEnglishCounterW = PDH_FUNCTION(pdh.PdhAddEnglishCounterW, PDH_HQUERY, LPCWSTR, DWORD_PTR, POINTER(PDH_HCOUNTER))
    PdhAddEnglishCounterA = PDH_FUNCTION(pdh.PdhAddEnglishCounterA, PDH_HQUERY, LPCSTR, DWORD_PTR, POINTER(PDH_HCOUNTER))
    PdhCollectQueryDataWithTime = PDH_FUNCTION(pdh.PdhCollectQueryDataWithTime, PDH_HQUERY, PLONGLONG)
    PdhValidatePathExW = PDH_FUNCTION(pdh.PdhValidatePathExW, PDH_HLOG, LPCWSTR)
    PdhValidatePathExA = PDH_FUNCTION(pdh.PdhValidatePathExA, PDH_HLOG, LPCSTR)
    PdhRemoveCounter = PDH_FUNCTION(pdh.PdhRemoveCounter, PDH_HCOUNTER)
    PdhCollectQueryData = PDH_FUNCTION(pdh.PdhCollectQueryData, PDH_HQUERY)
    PdhCloseQuery = PDH_FUNCTION(pdh.PdhCloseQuery, PDH_HQUERY)
    #
    #  Counter Functions
    #
    PdhGetFormattedCounterValue = PDH_FUNCTION(pdh.PdhGetFormattedCounterValue, PDH_HCOUNTER, DWORD, LPDWORD, PPDH_FMT_COUNTERVALUE)
    PdhGetFormattedCounterArrayA = PDH_FUNCTION(pdh.PdhGetFormattedCounterArrayA, PDH_HCOUNTER, DWORD, LPDWORD, LPDWORD, PPDH_FMT_COUNTERVALUE_ITEM_A)
    PdhGetFormattedCounterArrayW = PDH_FUNCTION(pdh.PdhGetFormattedCounterArrayW, PDH_HCOUNTER, DWORD, LPDWORD, LPDWORD, PPDH_FMT_COUNTERVALUE_ITEM_W)
    # dwFormat flag values
    #
    PDH_FMT_RAW = (DWORD(0x00000010)).value
    PDH_FMT_ANSI = (DWORD(0x00000020)).value
    PDH_FMT_UNICODE = (DWORD(0x00000040)).value
    PDH_FMT_LONG = (DWORD(0x00000100)).value
    PDH_FMT_DOUBLE = (DWORD(0x00000200)).value
    PDH_FMT_LARGE = (DWORD(0x00000400)).value
    PDH_FMT_NOSCALE = (DWORD(0x00001000)).value
    PDH_FMT_1000 = (DWORD(0x00002000)).value
    PDH_FMT_NODATA = (DWORD(0x00004000)).value
    PDH_FMT_NOCAP100 = (DWORD(0x00008000)).value
    PERF_DETAIL_COSTLY = (DWORD(0x00010000)).value
    PERF_DETAIL_STANDARD = (DWORD(0x0000FFFF)).value
    PdhGetRawCounterValue = PDH_FUNCTION(pdh.PdhGetRawCounterValue, PDH_HCOUNTER, LPDWORD, PPDH_RAW_COUNTER)
    PdhGetRawCounterArrayA = PDH_FUNCTION(pdh.PdhGetRawCounterArrayA, PDH_HCOUNTER, LPDWORD, LPDWORD, PPDH_RAW_COUNTER_ITEM_A)
    PdhGetRawCounterArrayW = PDH_FUNCTION(pdh.PdhGetRawCounterArrayW, PDH_HCOUNTER, LPDWORD, LPDWORD, PPDH_RAW_COUNTER_ITEM_W)
    PdhCalculateCounterFromRawValue = PDH_FUNCTION(pdh.PdhCalculateCounterFromRawValue, PDH_HCOUNTER, DWORD, PPDH_RAW_COUNTER, PPDH_RAW_COUNTER, PPDH_FMT_COUNTERVALUE)
    PdhComputeCounterStatistics = PDH_FUNCTION(pdh.PdhComputeCounterStatistics, PDH_HCOUNTER, DWORD, DWORD, DWORD, PPDH_RAW_COUNTER, PPDH_STATISTICS)
    PdhGetCounterInfoW = PDH_FUNCTION(pdh.PdhGetCounterInfoW, PDH_HCOUNTER, BOOLEAN, LPDWORD, PPDH_COUNTER_INFO_W)
    PdhGetCounterInfoA = PDH_FUNCTION(pdh.PdhGetCounterInfoA, PDH_HCOUNTER, BOOLEAN, LPDWORD, PPDH_COUNTER_INFO_A)
    PDH_MAX_SCALE = (7)
    PDH_MIN_SCALE = (-7)
    PdhSetCounterScaleFactor = PDH_FUNCTION(pdh.PdhSetCounterScaleFactor, PDH_HCOUNTER, LONG)
    #
    #   Browsing and enumeration functions
    #
    PdhConnectMachineW = PDH_FUNCTION(pdh.PdhConnectMachineW, LPCWSTR)
    PdhConnectMachineA = PDH_FUNCTION(pdh.PdhConnectMachineA, LPCSTR)
    PdhEnumMachinesW = PDH_FUNCTION(pdh.PdhEnumMachinesW, LPCWSTR, PZZWSTR, LPDWORD)
    PdhEnumMachinesA = PDH_FUNCTION(pdh.PdhEnumMachinesA, LPCSTR, PZZSTR, LPDWORD)
    PdhEnumObjectsW = PDH_FUNCTION(pdh.PdhEnumObjectsW, LPCWSTR, LPCWSTR, PZZWSTR, LPDWORD, DWORD, BOOL)
    PdhEnumObjectsA = PDH_FUNCTION(pdh.PdhEnumObjectsA, LPCSTR, LPCSTR, PZZSTR, LPDWORD, DWORD, BOOL)
    PdhEnumObjectItemsW = PDH_FUNCTION(pdh.PdhEnumObjectItemsW, LPCWSTR, LPCWSTR, LPCWSTR, PZZWSTR, LPDWORD, PZZWSTR, LPDWORD, DWORD, DWORD)
    PdhEnumObjectItemsA = PDH_FUNCTION(pdh.PdhEnumObjectItemsA, LPCSTR, LPCSTR, LPCSTR, PZZSTR, LPDWORD, PZZSTR, LPDWORD, DWORD, DWORD)
    PdhMakeCounterPathW = PDH_FUNCTION(pdh.PdhMakeCounterPathW, PPDH_COUNTER_PATH_ELEMENTS_W, LPWSTR, LPDWORD, DWORD)
    PdhMakeCounterPathA = PDH_FUNCTION(pdh.PdhMakeCounterPathA, PPDH_COUNTER_PATH_ELEMENTS_A, LPSTR, LPDWORD, DWORD)
    PdhParseCounterPathW = PDH_FUNCTION(pdh.PdhParseCounterPathW, LPCWSTR, PPDH_COUNTER_PATH_ELEMENTS_W, LPDWORD, DWORD)
    PdhParseCounterPathA = PDH_FUNCTION(pdh.PdhParseCounterPathA, LPCSTR, PPDH_COUNTER_PATH_ELEMENTS_A, LPDWORD, DWORD)
    PDH_PATH_WBEM_RESULT = (DWORD(0x00000001)).value
    PDH_PATH_WBEM_INPUT = (DWORD(0x00000002)).value
    PDH_PATH_LANG_FLAGS = lambda LangId, Flags: DWORD((((LangId & 0x0000FFFF) << 16) | (Flags & 0x0000FFFF))).value
    PdhParseInstanceNameW = PDH_FUNCTION(pdh.PdhParseInstanceNameW, LPCWSTR, LPWSTR, LPDWORD, LPWSTR, LPDWORD, LPDWORD)
    PdhParseInstanceNameA = PDH_FUNCTION(pdh.PdhParseInstanceNameA, LPCSTR, LPSTR, LPDWORD, LPSTR, LPDWORD, LPDWORD)
    PdhValidatePathW = PDH_FUNCTION(pdh.PdhValidatePathW, LPCWSTR)
    PdhValidatePathA = PDH_FUNCTION(pdh.PdhValidatePathA, LPCSTR)
    PdhGetDefaultPerfObjectW = PDH_FUNCTION(pdh.PdhGetDefaultPerfObjectW, LPCWSTR, LPCWSTR, LPWSTR, LPDWORD)
    PdhGetDefaultPerfObjectA = PDH_FUNCTION(pdh.PdhGetDefaultPerfObjectA, LPCSTR, LPCSTR, LPSTR, LPDWORD)
    PdhGetDefaultPerfCounterW = PDH_FUNCTION(pdh.PdhGetDefaultPerfCounterW, LPCWSTR, LPCWSTR, LPCWSTR, LPWSTR, LPDWORD)
    PdhGetDefaultPerfCounterA = PDH_FUNCTION(pdh.PdhGetDefaultPerfCounterA, LPCSTR, LPCSTR, LPCSTR, LPSTR, LPDWORD)

    CounterPathCallBack = WINAPI(PDH_STATUS, DWORD_PTR)

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
        class BrowseDlgConfig_HW(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bShowObjectBrowser", DWORD, 1),
                ("bReserved", DWORD, 22),
                ("hWndOwner", HWND),
                ("hDataSource", PDH_HLOG),
                ("szReturnPathBuffer", LPWSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPWSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_HW = BrowseDlgConfig_HW
        PPDH_BROWSE_DLG_CONFIG_HW = POINTER(PDH_BROWSE_DLG_CONFIG_HW)

        class BrowseDlgConfig_HA(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bShowObjectBrowser", DWORD, 1),
                ("bReserved", DWORD, 22),
                ("hWndOwner", HWND),
                ("hDataSource", PDH_HLOG),
                ("szReturnPathBuffer", LPSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_HA = BrowseDlgConfig_HA
        PPDH_BROWSE_DLG_CONFIG_HA = POINTER(PDH_BROWSE_DLG_CONFIG_HA)

        class BrowseDlgConfig_W(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bShowObjectBrowser", DWORD, 1),
                ("bReserved", DWORD, 22),
                ("hWndOwner", HWND),
                ("szDataSource", LPWSTR),
                ("szReturnPathBuffer", LPWSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPWSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_W = BrowseDlgConfig_W
        PPDH_BROWSE_DLG_CONFIG_W = POINTER(PDH_BROWSE_DLG_CONFIG_W)

        class BrowseDlgConfig_A(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bShowObjectBrowser", DWORD, 1),
                ("bReserved", DWORD, 22),
                ("hWndOwner", HWND),
                ("szDataSource", LPSTR),
                ("szReturnPathBuffer", LPSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_A = BrowseDlgConfig_A
        PPDH_BROWSE_DLG_CONFIG_A = POINTER(PDH_BROWSE_DLG_CONFIG_A)

    else:
        class BrowseDlgConfig_W(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bReserved", DWORD, 23),
                ("hWndOwner", HWND),
                ("szDataSource", LPWSTR),
                ("szReturnPathBuffer", LPWSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPWSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_W = BrowseDlgConfig_W
        PPDH_BROWSE_DLG_CONFIG_W = POINTER(PDH_BROWSE_DLG_CONFIG_W)

        class BrowseDlgConfig_A(CStructure):
            _fields_ = [
                # Configuration flags
                ("bIncludeInstanceIndex", DWORD, 1),
                ("bSingleCounterPerAdd", DWORD, 1),
                ("bSingleCounterPerDialog", DWORD, 1),
                ("bLocalCountersOnly", DWORD, 1),
                ("bWildCardInstances", DWORD, 1),
                ("bHideDetailBox", DWORD, 1),
                ("bInitializePath", DWORD, 1),
                ("bDisableMachineSelection", DWORD, 1),
                ("bIncludeCostlyObjects", DWORD, 1),
                ("bReserved", DWORD, 23),
                ("hWndOwner", HWND),
                ("szDataSource", LPSTR),
                ("szReturnPathBuffer", LPSTR),
                ("cchReturnPathLength", DWORD),
                ("pCallBack", CounterPathCallBack),
                ("dwCallBackArg", DWORD_PTR),
                ("CallBackStatus", PDH_STATUS),
                ("dwDefaultDetailLevel", DWORD),
                ("szDialogBoxCaption", LPSTR)
            ]
        PDH_BROWSE_DLG_CONFIG_A = BrowseDlgConfig_A
        PPDH_BROWSE_DLG_CONFIG_A = POINTER(PDH_BROWSE_DLG_CONFIG_A)
    