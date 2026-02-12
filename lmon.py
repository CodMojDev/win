"""++

Copyright (c) 1991-1999  Microsoft Corporation
All rights reserved

Module Name:

    lmon.h

--"""

from .minwindef import LPSTR, LPWSTR, DWORD, LPBYTE, Structure, POINTER

from . import cpreproc

from .defbase import *

# REGION *** Desktop Family ***

class PORT_INFO_FFA(CStructure):
    _fields_ = [
        ("pName", LPSTR),
        ("cbMonitorData", DWORD),
        ("pMonitorData", LPBYTE)
    ]
PPORT_INFO_FFA = POINTER(PORT_INFO_FFA)
LPPORT_INFO_FFA = PPORT_INFO_FFA

class PORT_INFO_FFW(CStructure):
    _fields_ = [
        ("pName", LPWSTR),
        ("cbMonitorData", DWORD),
        ("pMonitorData", LPBYTE)
    ]
PPORT_INFO_FFW = POINTER(PORT_INFO_FFW)
LPPORT_INFO_FFW = PPORT_INFO_FFW
PORT_INFO_FF = unicode(PORT_INFO_FFW, PORT_INFO_FFA)
PPORT_INFO_FF = unicode(PPORT_INFO_FFW, PPORT_INFO_FFA)
LPPORT_INFO_FF = PPORT_INFO_FF

# REGION ***
