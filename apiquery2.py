"""
/********************************************************************************
*                                                                               *
* apiquery2.h -- ApiSet Contract for api-ms-win-core-apiquery-l2                *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

from .minwindef import W_WinDLL, BOOL, LPCSTR

if cpreproc.pragma_once("_APIQUERY2_H_"):
    kernelbase = W_WinDLL("kernelbase.dll")

    # *** Desktop Family or OneCore Family ***

    @kernelbase.foreign(BOOL, LPCSTR, result_function=bool)
    def IsApiSetImplemented(Contract: bytes) -> bool: ...

    # REGION ***

#_APIQUERY2_H_
