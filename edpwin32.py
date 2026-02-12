"""
//+-----------------------------------------------------------------------
//
// Microsoft Windows
//
// Copyright (c) Microsoft Corporation
//
// Description: Enterprise Data Protection Win32 APIs
//
//------------------------------------------------------------------------
"""

from . import cpreproc

from .winnt import PCWSTR, BOOL, POINTER, declare, W_WinDLL, CStructure, VOID

from .sdkddkver import WIN32_WINNT_WIN10

if cpreproc.pragma_once("_EDPWIN32_H_"):
    efswrt = W_WinDLL("efswrt.dll")

    # REGION *** Desktop Family ***

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN10:
        ProtectFileToEnterpriseIdentity = declare(efswrt.ProtectFileToEnterpriseIdentity, VOID, PCWSTR, PCWSTR)

        class FILE_UNPROTECT_OPTIONS(CStructure):
            _fields_ = [
                ("audit", BOOL)
            ]
            
            audit: int
        
        UnprotectFile = declare(efswrt.UnprotectFile, VOID, PCWSTR, POINTER(FILE_UNPROTECT_OPTIONS))

    # REGION ***

# _EDPWIN32_H_