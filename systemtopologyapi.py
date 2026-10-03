"""
/********************************************************************************
*                                                                               *
* systemtopologyapi.h -- ApiSet Contract for api-ms-win-core-systemtopology-l1  *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_SYSTEMTOPOLOGY_H_"):
    from .winnt import *
    from .sdkddkver import *
    kernel32 = get_win_library("kernel32.dll")
    
    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetNumaHighestNodeNumber = declare(kernel32.GetNumaHighestNodeNumber, BOOL, PULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    if cpreproc.get_version() >= WIN32_WINNT_WIN7:
        GetNumaNodeProcessorMaskEx = declare(kernel32.GetNumaNodeProcessorMaskEx, BOOL, USHORT, PGROUP_AFFINITY)
    if cpreproc.get_version() >= WIN32_WINNT_WIN7:
        GetNumaProximityNodeEx = declare(kernel32.GetNumaProximityNodeEx, BOOL, ULONG, PUSHORT)

    # REGION ***