"""

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    socketapi.h

Abstract:

    Prototypes and Definitions for Socket API
"""

from . import cpreproc

from .minwindef import BOOL, WinDLL

from .sdkddkver import WIN32_WINNT_WIN8

from .com.comdefbase import HRESULT

from .defbase import *

if cpreproc.pragma_once("_SOCKETAPI_H"):
    
    windows_networking = WinDLL("Windows.Networking.dll")

    # REGION *** Application Family ***

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN8:
        SetSocketMediaStreamingMode = declare(windows_networking.SetSocketMediaStreamingMode, HRESULT, BOOL)

    # REGION ***

# _SOCKETAPI_H


