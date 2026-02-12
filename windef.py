"""
*****************************************************************************
*                                                                           *
* windef.h -- Basic Windows Type Definitions                                *
*                                                                           *
* Copyright (c) Microsoft Corporation. All rights reserved.                 *
*                                                                           *
*****************************************************************************
"""

from . import cpreproc

from .minwindef import *

if cpreproc.pragma_once("_WINDEF_"):
    WINVER = 0x0A00

    HGLRC = HANDLE
    HEVENT = HANDLE
    HWINEVENTHOOK = HANDLE
    HUMPD = HANDLE

    HFILE_ERROR = HFILE(-1)

    LPCRECT = PRECT
    LPCRECTL = PRECTL
    NPRECT = PRECT

    APP_LOCAL_DEVICE_ID_SIZE = 32
    class APP_LOCAL_DEVICE_ID(CStructure):
        _fields_ = [
            ("value", CHAR * APP_LOCAL_DEVICE_ID_SIZE)
        ]

    # mode selections for the device mode function
    DM_UPDATE = 1
    DM_COPY = 2
    DM_PROMPT = 4
    DM_MODIFY = 8
    DM_IN_BUFFER = DM_MODIFY
    DM_IN_PROMPT = DM_PROMPT
    DM_OUT_BUFFER = DM_COPY
    DM_OUT_DEFAULT = DM_UPDATE
    # device capabilities indices
    DC_FIELDS = 1
    DC_PAPERS = 2
    DC_PAPERSIZE = 3
    DC_MINEXTENT = 4
    DC_MAXEXTENT = 5
    DC_BINS = 6
    DC_DUPLEX = 7
    DC_SIZE = 8
    DC_EXTRA = 9
    DC_VERSION = 10
    DC_DRIVER = 11
    DC_BINNAMES = 12
    DC_ENUMRESOLUTIONS = 13
    DC_FILEDEPENDENCIES = 14
    DC_TRUETYPE = 15
    DC_PAPERNAMES = 16
    DC_ORIENTATION = 17
    DC_COPIES = 18

    cpreproc.define("_DPI_AWARENESS_CONTEXTS_")

    DPI_AWARENESS_CONTEXT = HANDLE

    DPI_AWARENESS = INT
    if True:
        DPI_AWARENESS_INVALID           = -1
        DPI_AWARENESS_UNAWARE           = 0
        DPI_AWARENESS_SYSTEM_AWARE      = 1
        DPI_AWARENESS_PER_MONITOR_AWARE = 2

    DPI_AWARENESS_CONTEXT_UNAWARE = DPI_AWARENESS_CONTEXT(-1)
    DPI_AWARENESS_CONTEXT_SYSTEM_AWARE = DPI_AWARENESS_CONTEXT(-2)
    DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE = DPI_AWARENESS_CONTEXT(-3)
    DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = DPI_AWARENESS_CONTEXT(-4)
    DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED = DPI_AWARENESS_CONTEXT(-5)

    DPI_HOSTING_BEHAVIOR = INT
    if True:
        DPI_HOSTING_BEHAVIOR_INVALID     = -1
        DPI_HOSTING_BEHAVIOR_DEFAULT     = 0
        DPI_HOSTING_BEHAVIOR_MIXED       = 1