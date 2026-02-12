"""
 * Windows demo licensing API
 *
 * External definitions for Windows demo licensing API
 *
 *  Copyright (c) Microsoft Corporation. All Rights Reserved.
"""

from . import cpreproc
from .defbase import *
from .minwindef import *
from .sdkddkver import WIN32_WINNT_WIN8

if cpreproc.pragma_once("_WS_DEMO_LICENSING_H_"):
    
    oemlicense = W_WinDLL("oemlicense.dll")

    # REGION *** Desktop Family ***

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN8:
        AddDemoAppLicense = declare(oemlicense.AddDemoAppLicense, VOID, UINT, PBYTE)
        RemoveDemoAppLicense = declare(oemlicense.RemoveDemoAppLicense, VOID, LPCWSTR)
        
    # REGION ***