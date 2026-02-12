"""
++

 Copyright(c) 2002  Microsoft Corporation

 Module Name:

 atacct.h

 Abstract:


 Revision History:

--
"""

from . import cpreproc

from .minwindef import *
from .defbase import *

if cpreproc.pragma_once("_ATACCT_H_"):
    mstask = W_WinDLL("mstask.dll")

    # REGION *** Desktop Family ***
    
    @mstask.foreign(HRESULT, LPCWSTR, DWORD, PWCHAR)
    def GetNetScheduleAccountInformation(pwszServerName: str, ccAccount: int, wszAccount: PWCHAR) -> int: ...
    
    @mstask.foreign(HRESULT, LPCWSTR, LPCWSTR, LPCWSTR)
    def SetNetScheduleAccountInformation(pwszServerName: str, pwszAccount: str, pwszPassword: str) -> int: ...

    # REGION ***
# _ATACCT_H_