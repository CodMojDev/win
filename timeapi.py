"""
 *******************************************************************************
 *                                                                             *
 * timerapi.h -- ApiSet Contract for api-ms-win-mm-time-l1-1-0                 *
 *                                                                             *
 * Copyright(c) Microsoft Corporation. All rights reserved.                    *
 *                                                                             *
 *******************************************************************************
"""

if cpreproc.pragma_once("_TIMERAPI_H_"):
    from .mmsyscom import *
    winmm = get_win_library("winmm.dll")
    
    # REGION *** Desktop Family or OneCore Family ***

    if cpreproc.ifndef("MMNOTIMER"):
        """
        ***************************************************************************

        Timer support

        ***************************************************************************
        """

        # timer error return values
        TIMERR_NOERROR = (0) # no error
        TIMERR_NOCANDO = (TIMERR_BASE+1) # request not completed
        TIMERR_STRUCT = (TIMERR_BASE+33) # time struct size

        # timer device capabilities data structure
        class timecaps_tag(CStructure):
            _fields_ = [
                ("wPeriodMin", UINT), # minimum period supported
                ("wPeriodMax", UINT)  # maximum period supported
            ]
            wPeriodMin: int
            wPeriodMax: int
        TIMECAPS = timecaps_tag
        PTIMECAPS = NPTIMECAPS = LPTIMECAPS = PTR(TIMECAPS)

        # timer function prototypes
        timeGetSystemTime = declare(kernel32.timeGetSystemTime, MMRESULT, LPMMTIME, UINT)
        timeGetTime = declare(kernel32.timeGetTime, DWORD, VOID)
        timeGetDevCaps = declare(kernel32.timeGetDevCaps, MMRESULT, LPTIMECAPS, UINT)
        timeBeginPeriod = declare(kernel32.timeBeginPeriod, MMRESULT, UINT)
        timeEndPeriod = declare(kernel32.timeEndPeriod, MMRESULT, UINT)

        # REGION ***
# _TIMERAPI_H_
