"""
 *********************************************************************************
 *                                                                               *
 * wow64app.h - ApiSet Contract for api-ms-win-core-wow64-l1                     *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *

from typing import (Callable)

from .winnt import PVOID, PPVOID, PWOW64_CONTEXT

from .defbase import *

# _MSC_VER
if cpreproc.ifndef("_WOW64APISET_H_"):
    kernel32 = get_win_library("kernel32.dll")
    kernelbase = get_win_library("kernelbase.dll")
    cpreproc.define("_WOW64APISET_H_")

    # REGION *** Desktop Family or OneCore Family ***

    # RC warns because "WINBASE_DECLARE_GET_SYSTEM_WOW64_DIRECTORY" is a bit long.
    Wow64DisableWow64FsRedirection = declare(kernel32.Wow64DisableWow64FsRedirection, BOOL, PPVOID)
    Wow64RevertWow64FsRedirection = declare(kernel32.Wow64RevertWow64FsRedirection, BOOL, PVOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    IsWow64Process = declare(kernel32.IsWow64Process, BOOL, HANDLE, PBOOL)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # RC warns because "WINBASE_DECLARE_GET_SYSTEM_WOW64_DIRECTORY" is a bit long.
    GetSystemWow64DirectoryA = declare(kernel32.GetSystemWow64DirectoryA, UINT, LPSTR, UINT)
    GetSystemWow64DirectoryW = declare(kernel32.GetSystemWow64DirectoryW, UINT, LPWSTR, UINT)
    GetSystemWow64Directory = unicode(GetSystemWow64DirectoryW, GetSystemWow64DirectoryA)
    Wow64SetThreadDefaultGuestMachine = declare(kernelbase.Wow64SetThreadDefaultGuestMachine, USHORT, USHORT)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    IsWow64Process2 = declare(kernel32.IsWow64Process2, BOOL, HANDLE, PUSHORT, PUSHORT)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetSystemWow64Directory2A = declare(kernelbase.GetSystemWow64Directory2A, UINT, LPSTR, UINT, WORD)
    GetSystemWow64Directory2W = declare(kernelbase.GetSystemWow64Directory2W, UINT, LPWSTR, UINT, WORD)
    GetSystemWow64Directory2 = unicode(GetSystemWow64Directory2W, GetSystemWow64Directory2A)
    IsWow64GuestMachineSupported = declare(kernel32.IsWow64GuestMachineSupported, HRESULT, USHORT, PBOOL)
    Wow64GetThreadContext = declare(kernel32.Wow64GetThreadContext, BOOL, HANDLE, PWOW64_CONTEXT)
    Wow64SetThreadContext = declare(kernel32.Wow64SetThreadContext, BOOL, HANDLE, PWOW64_CONTEXT)
    Wow64SuspendThread = declare(kernel32.Wow64SuspendThread, DWORD, HANDLE)

    # REGION ***
# _WOW64APISET_H_