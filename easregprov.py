"""*++ 

Copyright (c) Microsoft Corporation

Module Name:

    easregprov.h

Abstract:

    This file contains the function which a 3rd Party Encryption software installation 
    package calls to register & unregister their provider that supports EAS.

Environment:

    User Mode - Win32

Notes:

--"""

from . import cpreproc

from .sdkddkver import WIN32_WINNT_WINBLUE

from .defbase import *

from .minwindef import windll, LPCWSTR, VOID

from .com.comdefbase import HRESULT

#
# User Function
#

if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WINBLUE:
    if cpreproc.pragma_once("_EASREGPROV_"):
        easwrt = W_WinDLL("easwrt.dll")

        # REGION *** Desktop Family ***

        EasRegisterEncryptionProvider = declare(easwrt.EasRegisterEncryptionProvider, HRESULT, LPCWSTR)

        EasUnRegisterEncryptionProvider = declare(easwrt.EasUnRegisterEncryptionProvider, HRESULT, VOID)

        # REGION ***

    # _EASREGPROV_
