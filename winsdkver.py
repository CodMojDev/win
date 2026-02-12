"""

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    WinSDKVer.h

Abstract:

    Master include file for versioning content that ships in the Windows SDK.

"""

from . import cpreproc

if cpreproc.pragma_once("_INC_WINSDKVER"):
    # REGION *** Desktop Family ***

    # This list contains the highest version constants supported by content in the Windows SDK.

    WIN32_MAXVER           = 0x0A00
    WIN32_WINDOWS_MAXVER   = 0x0A00
    NTDDI_MAXVER            = 0x0A00
    WIN32_IE_MAXVER        = 0x0A00
    WIN32_WINNT_MAXVER     = 0x0A00
    WINVER_MAXVER           = 0x0A00

    # REGION ***