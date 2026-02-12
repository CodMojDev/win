"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    sensapi.h

Abstract:

    Public header file for the SENS Connectivity APIs.

Author:

    Gopal Parupudi    <GopalP>

[Notes:]

    optional-notes

Revision History:

    GopalP          10/12/1997         Start.

--"""

from . import cpreproc

from .minwindef import (DWORD, LPDWORD, LPCSTR, 
                        LPCWSTR, BOOL, 
                        windll, Structure, POINTER)

from .defbase import *

if cpreproc.pragma_once("__SENSAPI_H__"):
    sensapi = W_WinDLL("sensapi.dll")

    NETWORK_ALIVE_LAN = 0x00000001
    NETWORK_ALIVE_WAN = 0x00000002
    NETWORK_ALIVE_AOL = 0x00000004
    NETWORK_ALIVE_INTERNET = 0x00000008

    class tagQOCINFO(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("dwFlags", DWORD),
            ("dwInSpeed", DWORD),
            ("dwOutSpeed", DWORD)
        ]
    QOCINFO = tagQOCINFO
    LPQOCINFO = POINTER(QOCINFO)
    IsDestinationReachableA = declare(sensapi.IsDestinationReachableA, BOOL, LPCSTR, LPQOCINFO)
    IsDestinationReachableW = declare(sensapi.IsDestinationReachableW, BOOL, LPCWSTR, LPQOCINFO)
    IsNetworkAlive = declare(sensapi.IsNetworkAlive, BOOL, LPDWORD)