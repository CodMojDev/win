#=--------------------------------------------------------------------------=
# MsCtfMonitorApi.h
#
#
# MsCtfMonitorApi declarations.

#=--------------------------------------------------------------------------=
# (C) Copyright 1995-2003 Microsoft Corporation.  All Rights Reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
# ANY KIND, EITHER EXPRESSED OR TFPLIED, INCLUDING BUT NOT LIMITED TO
# THE TFPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.
#=--------------------------------------------------------------------------=

from . import cpreproc
from .com.comdefbase import *

if cpreproc.pragma_once():
    MsCtfMonitor = get_win_library("MsCtfMonitor.dll")

    # REGION *** Desktop Family ***

    ######################################
    #
    # DoMsCtfMonitor for ctfmon.exe
    #
    ######################################

    DCM_FLAGS_TASKENG         = 0x00000001
    DCM_FLAGS_CTFMON          - 0x00000002
    DCM_FLAGS_LOCALTHREADTSF  = 0x00000004
    
    @MsCtfMonitor.foreign(BOOL, DWORD, HANDLE)
    def DoMsCtfMonitor(dwFlags: int, hEventForServiceStop: WT_HANDLE) -> int: ...

    ######################################
    #
    # Flags for InitLocalMsCtfMonitor()
    #
    # ILMCM_CHECKLAYOUTANDTIPENABLED
    #
    #    With this flag, InitLocalMsCtfMonitor() checkes the keyboard layout or 
    #    tips are enabled. If there is only one keyboard layout, it does not 
    #    initialize Text Services Framework or start the language bar.
    #
    ######################################
    ILMCM_CHECKLAYOUTANDTIPENABLED    = 0x00001    
    ######################################
    #
    # ILMCM_LANGUAGEBAROFF
    #
    #    With this flag set, InitLocalMsCtfMonitor() won't start the default 
    #    system language bar for the desktop.
    #
    ######################################
    ILMCM_LANGUAGEBAROFF              = 0x00002    

    ######################################
    #
    # InitLocalMsCtfMonitor
    #
    ######################################
    @MsCtfMonitor.foreign(HRESULT, DWORD)
    def InitLocalMsCtfMonitor(dwFlags: int) -> int: ...

    ######################################
    #
    # UninitLocalMsCtfMonitor
    #
    ######################################
    @MsCtfMonitor.foreign(HRESULT)
    def UninitLocalMsCtfMonitor() -> int: ...
    
    # REGION ***