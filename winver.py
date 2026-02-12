"""
 *******************************************************************************
 *                                                                             *
 * winver.h -    Version management functions, types, and definitions          *
 *                                                                             *
 *               Include file for VER.DLL.  This library is                    *
 *               designed to allow version stamping of Windows executable files*
 *               and of special .VER files for DOS executable files.           *
 *                                                                             *
 *               Copyright (c) Microsoft Corporation. All rights reserved.     *
 *                                                                             *
 *******************************************************************************
"""

from . import cpreproc

from .basetsd import *

from .winnt import PLPVOID

from typing import (Callable)

from .defbase import *

if cpreproc.pragma_once("VER_H"):
    version = W_WinDLL("version.dll")

    # REGION *** Desktop Family or OneCore Family ***

    if cpreproc.ifndef("RC_INVOKED"): # RC doesn't need to see the rest of this
        # ----- Function prototypes -----
        VerFindFileA = declare(version.VerFindFileA, DWORD, DWORD, LPCSTR, LPCSTR, LPCSTR, LPSTR, PUINT, LPSTR, PUINT)
        VerFindFileW = declare(version.VerFindFileW, DWORD, DWORD, LPCWSTR, LPCWSTR, LPCWSTR, LPWSTR, PUINT, LPWSTR, PUINT)
        VerFindFile = unicode(VerFindFileW, VerFindFileA)

        # REGION ***

        # REGION *** Desktop Family ***

        VerInstallFileA = declare(version.VerInstallFileA, DWORD, DWORD, LPCSTR, LPCSTR, LPCSTR, LPCSTR, LPCSTR, LPSTR, PUINT)
        VerInstallFileW = declare(version.VerInstallFileW, DWORD, DWORD, LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, LPCWSTR, LPWSTR, PUINT)
        VerInstallFile = unicode(VerInstallFileW, VerInstallFileA)

        # REGION ***

        # REGION *** Application Family or OneCore Family ***

        # Returns size of version info in bytes
        GetFileVersionInfoSizeA = declare(version.GetFileVersionInfoSizeA, DWORD, LPCSTR, LPDWORD)
        # Returns size of version info in bytes
        GetFileVersionInfoSizeW = declare(version.GetFileVersionInfoSizeW, DWORD, LPCWSTR, LPDWORD)
        GetFileVersionInfoSize = unicode(GetFileVersionInfoSizeW, GetFileVersionInfoSizeA)
        # Read version info into buffer
        GetFileVersionInfoA = declare(version.GetFileVersionInfoA, BOOL, LPCSTR, DWORD, DWORD, LPVOID)
        # Read version info into buffer
        GetFileVersionInfoW = declare(version.GetFileVersionInfoW, BOOL, LPCWSTR, DWORD, DWORD, LPVOID)
        GetFileVersionInfo = unicode(GetFileVersionInfoW, GetFileVersionInfoA)
        
        GetFileVersionInfoSizeExA = declare(version.GetFileVersionInfoSizeExA, DWORD, DWORD, LPCSTR, LPDWORD)
        GetFileVersionInfoSizeExW = declare(version.GetFileVersionInfoSizeExW, DWORD, DWORD, LPCWSTR, LPDWORD)
        GetFileVersionInfoSizeEx = unicode(GetFileVersionInfoSizeExW, GetFileVersionInfoSizeExA)

        GetFileVersionInfoExA = declare(version.GetFileVersionInfoExA, BOOL, DWORD, LPCSTR, DWORD, DWORD, LPVOID, DWORD)
        GetFileVersionInfoExW = declare(version.GetFileVersionInfoExA, BOOL, DWORD, LPCWSTR, DWORD, DWORD, LPVOID, DWORD)
        GetFileVersionInfoEx = unicode(GetFileVersionInfoExW, GetFileVersionInfoExA)

        # REGION ***
        
        # REGION *** Application Family or OneCore Family ***
        VerLanguageNameA = declare(version.VerLanguageNameA, DWORD, DWORD, LPSTR, DWORD)
        VerLanguageNameW = declare(version.VerLanguageNameW, DWORD, DWORD, LPWSTR, DWORD)
        VerLanguageName = unicode(VerLanguageNameW, VerLanguageNameA)
        VerQueryValueA = declare(version.VerQueryValueA, BOOL, LPCVOID, LPCSTR, PLPVOID, PUINT)
        VerQueryValueW = declare(version.VerQueryValueW, BOOL, LPCVOID, LPCWSTR, PLPVOID, PUINT)
        VerQueryValue = unicode(VerQueryValueW, VerQueryValueA)
    # !RC_INVOKED

    # REGION ***
# !VER_H