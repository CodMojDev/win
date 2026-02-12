"""++ BUILD Version: 0002    // Increment this if a change has global effects

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    wincon.h

Abstract:

    This module contains the public data structures, data types,
    and procedures exported by the NT console subsystem.

Created:

    26-Oct-1990

Revision History:

--"""

from . import cpreproc

if cpreproc.pragma_once("_WINCON_"):
    from .wincontypes import *

    if cpreproc.ifndef("NOGDI"):
        from .wingdi import *

    if cpreproc.ifndef("NOAPISET"):
        from .consoleapi import *
        from .consoleapi2 import *
        from .consoleapi3 import *
    
    CONSOLE_REAL_OUTPUT_HANDLE = LongToHandle(-2)
    CONSOLE_REAL_INPUT_HANDLE = LongToHandle(-3)
    CONSOLE_TEXTMODE_BUFFER = 1

# _WINCON_

