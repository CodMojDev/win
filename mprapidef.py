"""
*****************************************************************************
*                                                                           *
* mprapidef.h -- MPR definitions shared between user and kernel mode        *
*                                                                           *
* Copyright (c) Microsoft Corporation. All rights reserved.                 *
*                                                                           *
*****************************************************************************
"""

from . import cpreproc

if cpreproc.pragma_once("_MPRAPIDEF_"):
    from .lmcons import *

    MAX_INTERFACE_NAME_LEN  = 256
    MAX_TRANSPORT_NAME_LEN  = 40
    MAX_MEDIA_NAME          = 16
    MAX_PORT_NAME           = 16
    MAX_DEVICE_NAME         = 128
    MAX_PHONE_NUMBER_LEN    = 128
    MAX_DEVICETYPE_NAME     = 16

# _MPRAPIDEF_