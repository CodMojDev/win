"""
*******************************************************************************
*                                                                             *
* profileapi.h -- ApiSet Contract for api-ms-win-core-profile-l1              *
*                                                                             *
* Copyright(c) Microsoft Corporation. All rights reserved.                    *
*                                                                             *
*******************************************************************************
"""

from .minwindef import *

if cpreproc.pragma_once("_PROFILEAPI_H_"):
    kernel32 = get_win_library('kernel32.dll')
    
    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # Performance counter API's
    #
    QueryPerformanceCounter = declare(kernel32.QueryPerformanceCounter, BOOL, PLARGE_INTEGER)
    QueryPerformanceFrequency = declare(kernel32.QueryPerformanceFrequency, BOOL, PLARGE_INTEGER)

    # REGION ***
# _PROFILEAPI_H_