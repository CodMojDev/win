"""++

Copyright (c) Microsoft Corporation.  All Rights Reserved

Module Name:

    WindowsCeip.h

Abstract:

    Public interfaces for the Windows Customer Experience Improvement Program.

--"""

from . import cpreproc

from .minwindef import BOOL, VOID, windll

from .sdkddkver import WIN32_WINNT_WIN8

from .defbase import *

kernel32 = W_WinDLL("kernel32.dll")

# REGION *** Application Family or OneCore Family ***

if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN8:
    CeipIsOptedIn = declare(kernel32.CeipIsOptedIn, BOOL, VOID)

# REGION ***
