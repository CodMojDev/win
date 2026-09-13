"""
 *********************************************************************************
 *                                                                               *
 * handleapi.h -- ApiSet Contract for api-ms-win-core-handle-l1-1-0              *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

if cpreproc.pragma_once("_APISETHANDLE_"):
    kernel32 = get_win_library("kernel32.dll")
    #
    # Constants
    #
    INVALID_HANDLE_VALUE = HANDLE(-1).value

    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # Prototypes
    #
    CloseHandle = declare(kernel32.CloseHandle, BOOL, HANDLE)
    DuplicateHandle = declare(kernel32.DuplicateHandle, BOOL, HANDLE, HANDLE, HANDLE, LPHANDLE, DWORD, BOOL, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    CompareObjectHandles = declare(kernel32.CompareObjectHandles, BOOL, HANDLE, HANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetHandleInformation = declare(kernel32.GetHandleInformation, BOOL, HANDLE, LPDWORD)
    SetHandleInformation = declare(kernel32.SetHandleInformation, BOOL, HANDLE, DWORD, DWORD)

    # REGION ***
# _APISETHANDLE_