"""
 *********************************************************************************
 *                                                                               *
 * UtilApiSet.h -- ApiSet Contract for api-ms-win-core-util-l1-1-0               *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *

from .winnt import PVOID, PPVOID

from .defbase import *

if cpreproc.pragma_once("_APISETUTIL_"):
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    EncodePointer = declare(kernel32.EncodePointer, PVOID, PVOID)
    DecodePointer = declare(kernel32.DecodePointer, PVOID, PVOID)
    EncodeSystemPointer = declare(kernel32.EncodeSystemPointer, PVOID, PVOID)
    DecodeSystemPointer = declare(kernel32.DecodeSystemPointer, PVOID, PVOID)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    EncodeRemotePointer = declare(kernelbase.EncodeRemotePointer, HRESULT, HANDLE, PVOID, PPVOID)
    DecodeRemotePointer = declare(kernelbase.DecodeRemotePointer, HRESULT, HANDLE, PVOID, PPVOID)

    # REGION ***

    # REGION *** PC Family or OneCore Family or Games Family ***

    Beep = declare(kernel32.Beep, BOOL, DWORD, DWORD)

    # REGION ***
# _APISETUTIL_