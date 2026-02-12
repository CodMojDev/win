"""++

Copyright (c) 1986-2003  Microsoft Corporation

Module Name:

    wiaintfc.h

Abstract:

    This module contains interface class GUID for WIA.

Revision History:


--"""

from . import cpreproc
from .sdkddkver import *

if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINXP: # Windows XP and later
    if cpreproc.pragma_once("_WIAINTFC_H_"):
        # REGION *** Desktop Family ***

        from .guiddef import GUID

        #
        # GUID for Image class device interface.
        #

        GUID_DEVINTERFACE_IMAGE = GUID("{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}")


        # REGION ***

    # _WIAINTFC_H_

# if (_WIN32_WINNT >= 0x0501)
