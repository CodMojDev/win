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
    kernelbase = W_WinDLL("kernelbase.dll")
    #
    # Constants
    #
    INVALID_HANDLE_VALUE = HANDLE(-1)

    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # Prototypes
    #
    CloseHandle = declare(kernelbase.CloseHandle, BOOL, HANDLE)
    DuplicateHandle = declare(kernelbase.DuplicateHandle, BOOL, HANDLE, HANDLE, HANDLE, LPHANDLE, DWORD, BOOL, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    CompareObjectHandles = declare(kernelbase.CompareObjectHandles, BOOL, HANDLE, HANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetHandleInformation = declare(kernelbase.GetHandleInformation, BOOL, HANDLE, LPDWORD)
    SetHandleInformation = declare(kernelbase.SetHandleInformation, BOOL, HANDLE, DWORD, DWORD)

    # REGION ***
# _APISETHANDLE_