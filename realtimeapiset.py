"""
 *********************************************************************************
 *                                                                               *
 * realtimeapi.h -- ApiSet Contract for api-ms-win-core-realtime-l1              *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *
from .winnt import PULONG64, VOID, PULONGLONG, ULONGLONG

from .defbase import *

if cpreproc.pragma_once("_APISETREALTIME_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Desktop Family or OneCore Family ***

    QueryThreadCycleTime = declare(kernel32.QueryThreadCycleTime, BOOL, HANDLE, PULONG64)
    QueryProcessCycleTime = declare(kernel32.QueryProcessCycleTime, BOOL, HANDLE, PULONG64)
    QueryIdleProcessorCycleTime = declare(kernel32.QueryIdleProcessorCycleTime, BOOL, PULONG, PULONG64)
    QueryIdleProcessorCycleTimeEx = declare(kernel32.QueryIdleProcessorCycleTimeEx, BOOL, USHORT, PULONG, PULONG64)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    QueryInterruptTimePrecise = declare(kernel32.QueryInterruptTimePrecise, VOID, PULONGLONG)
    QueryUnbiasedInterruptTimePrecise = declare(kernel32.QueryUnbiasedInterruptTimePrecise, VOID, PULONGLONG)
    QueryInterruptTime = declare(kernel32.QueryInterruptTime, VOID, PULONGLONG)
    QueryUnbiasedInterruptTime = declare(kernel32.QueryUnbiasedInterruptTime, BOOL, PULONGLONG)
    QueryAuxiliaryCounterFrequency = declare(kernel32.QueryAuxiliaryCounterFrequency, HRESULT, PULONGLONG)
    ConvertAuxiliaryCounterToPerformanceCounter = declare(kernel32.ConvertAuxiliaryCounterToPerformanceCounter, HRESULT, ULONGLONG, PULONGLONG, PULONGLONG)
    ConvertPerformanceCounterToAuxiliaryCounter = declare(kernel32.ConvertPerformanceCounterToAuxiliaryCounter, HRESULT, ULONGLONG, PULONGLONG, PULONGLONG)

    # REGION ***
# _APISETREALTIME_