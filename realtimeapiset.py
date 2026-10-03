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
    kernel32 = get_win_library("kernel32.dll")
    kernelbase = get_win_library("kernelbase.dll")

    # REGION *** Desktop Family or OneCore Family ***

    QueryThreadCycleTime = declare(kernel32.QueryThreadCycleTime, BOOL, HANDLE, PULONG64)
    QueryProcessCycleTime = declare(kernel32.QueryProcessCycleTime, BOOL, HANDLE, PULONG64)
    QueryIdleProcessorCycleTime = declare(kernel32.QueryIdleProcessorCycleTime, BOOL, PULONG, PULONG64)
    QueryIdleProcessorCycleTimeEx = declare(kernel32.QueryIdleProcessorCycleTimeEx, BOOL, USHORT, PULONG, PULONG64)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    QueryInterruptTimePrecise = declare(kernelbase.QueryInterruptTimePrecise, VOID, PULONGLONG)
    QueryUnbiasedInterruptTimePrecise = declare(kernelbase.QueryUnbiasedInterruptTimePrecise, VOID, PULONGLONG)
    QueryInterruptTime = declare(kernelbase.QueryInterruptTime, VOID, PULONGLONG)
    QueryUnbiasedInterruptTime = declare(kernelbase.QueryUnbiasedInterruptTime, BOOL, PULONGLONG)
    QueryAuxiliaryCounterFrequency = declare(kernelbase.QueryAuxiliaryCounterFrequency, HRESULT, PULONGLONG)
    ConvertAuxiliaryCounterToPerformanceCounter = declare(kernelbase.ConvertAuxiliaryCounterToPerformanceCounter, HRESULT, ULONGLONG, PULONGLONG, PULONGLONG)
    ConvertPerformanceCounterToAuxiliaryCounter = declare(kernelbase.ConvertPerformanceCounterToAuxiliaryCounter, HRESULT, ULONGLONG, PULONGLONG, PULONGLONG)

    # REGION ***
# _APISETREALTIME_