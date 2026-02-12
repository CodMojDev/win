"""
 *********************************************************************************
 *                                                                               *
 * datetimeapi.h -- ApiSet Contract for api-ms-win-core-datetime-l1              *
 *                                                                               *
 * Copyright(c) Microsoft Corporation. All rights reserved.                      *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc
from .defbase import *

from .winbase import *

if cpreproc.pragma_once("_DATETIMEAPI_H_"):
    
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Desktop Family or OneCore or Games Family ***

    # For Windows Vista and above GetDateFormatEx is preferred
    GetDateFormatA = declare(kernel32.GetDateFormatA, INT, LCID, DWORD, PSYSTEMTIME, LPCSTR, LPSTR, INT)
    GetDateFormatW = declare(kernel32.GetDateFormatW, INT, LCID, DWORD, PSYSTEMTIME, LPCWSTR, LPWSTR, INT)
    GetDateFormat = unicode(GetDateFormatW, GetDateFormatA)
    # For Windows Vista and above GetTimeFormatEx is preferred
    GetTimeFormatA = declare(kernel32.GetTimeFormatA, INT, LCID, DWORD, PSYSTEMTIME, LPCSTR, LPSTR, INT)
    GetTimeFormatW = declare(kernel32.GetTimeFormatW, INT, LCID, DWORD, PSYSTEMTIME, LPCWSTR, LPWSTR, INT)
    GetTimeFormat = unicode(GetTimeFormatW, GetTimeFormatA)

    # REGION ***

    # REGION *** Application Family or OneCore or Games Family ***

    GetTimeFormatEx = declare(kernel32.GetTimeFormatEx, INT, LPCWSTR, DWORD, PSYSTEMTIME, LPCWSTR, LPWSTR, INT)
    GetDateFormatEx = declare(kernel32.GetDateFormatEx, INT, LPCWSTR, DWORD, PSYSTEMTIME, LPCWSTR, LPWSTR, INT, LPCWSTR)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    cpreproc.define("GetDurationFormatEx_DEFINED")
    GetDurationFormatEx = declare(kernel32.GetDurationFormatEx, INT, LPCWSTR, DWORD, PSYSTEMTIME, ULONGLONG, LPCWSTR, LPWSTR, INT)

    # REGION ***
# DATETIMEAPI