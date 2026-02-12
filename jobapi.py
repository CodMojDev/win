"""
/********************************************************************************
*                                                                               *
* jobapiset.h -- ApiSet Contract for api-ms-win-core-job-l1                     *  
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

from .minwindef import BOOL, HANDLE, PBOOL, windll

from .sdkddkver import WIN32_WINNT_WINXP

from .defbase import *

if cpreproc.pragma_once("_JOBAPISET_H_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Desktop Family or OneCore Family ***

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP:
        IsProcessInJob = declare(kernel32.IsProcessInJob, BOOL, HANDLE, HANDLE, PBOOL)

    # REGION ***

# _JOBAPISET_H_
