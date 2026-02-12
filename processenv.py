"""
 *********************************************************************************
 *                                                                               *
 * ProcessEnv.h -- ApiSet Contract for api-ms-win-core-processenvironment-l1     *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .defbase import *

from .minwindef import *

from .winnt import LPWCH, LPCH

if cpreproc.pragma_once("_PROCESSENV_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    SetEnvironmentStringsA = declare(kernel32.SetEnvironmentStringsA, BOOL, LPCH)
    SetEnvironmentStringsW = declare(kernel32.SetEnvironmentStringsW, BOOL, LPWCH)
    SetEnvironmentStrings = unicode(SetEnvironmentStringsW, SetEnvironmentStringsA)

    # REGION ***

    # REGION *** PC Family or OneCore Family or Games Family ***

    GetStdHandle = declare(kernel32.GetStdHandle, HANDLE, DWORD)
    SetStdHandle = declare(kernel32.SetStdHandle, BOOL, DWORD, HANDLE)
    if cpreproc.getdef("_WINVER") >= 0x0600:
        SetStdHandleEx = declare(kernel32.SetStdHandleEx, BOOL, DWORD, HANDLE, PHANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetCommandLineA = declare(kernel32.GetCommandLineA, LPSTR, VOID)
    GetCommandLineW = declare(kernel32.GetCommandLineW, LPWSTR, VOID)
    GetCommandLine = unicode(GetCommandLineW, GetCommandLineA)
    GetEnvironmentStrings = declare(kernel32.GetEnvironmentStrings, LPCH, VOID)
    GetEnvironmentStringsW = declare(kernel32.GetEnvironmentStringsW, LPWCH, VOID)
    GetEnvironmentStrings = unicode(GetEnvironmentStringsW, GetEnvironmentStrings)
    FreeEnvironmentStringsA = declare(kernel32.FreeEnvironmentStringsA, BOOL, LPCH)
    FreeEnvironmentStringsW = declare(kernel32.FreeEnvironmentStringsW, BOOL, LPWCH)
    FreeEnvironmentStrings = unicode(FreeEnvironmentStringsW, FreeEnvironmentStringsA)
    GetEnvironmentVariableA = declare(kernel32.GetEnvironmentVariableA, DWORD, LPCSTR, LPSTR, DWORD)
    GetEnvironmentVariableW = declare(kernel32.GetEnvironmentVariableW, DWORD, LPCWSTR, LPWSTR, DWORD)
    GetEnvironmentVariable = unicode(GetEnvironmentVariableW, GetEnvironmentVariableA)
    SetEnvironmentVariableA = declare(kernel32.SetEnvironmentVariableA, BOOL, LPCSTR, LPCSTR)
    SetEnvironmentVariableW = declare(kernel32.SetEnvironmentVariableW, BOOL, LPCWSTR, LPCWSTR)
    SetEnvironmentVariable = unicode(SetEnvironmentVariableW, SetEnvironmentVariableA)
    ExpandEnvironmentStringsA = declare(kernel32.ExpandEnvironmentStringsA, DWORD, LPCSTR, LPSTR, DWORD)
    ExpandEnvironmentStringsW = declare(kernel32.ExpandEnvironmentStringsW, DWORD, LPCWSTR, LPWSTR, DWORD)
    ExpandEnvironmentStrings = unicode(ExpandEnvironmentStringsW, ExpandEnvironmentStringsA)
    SetCurrentDirectoryA = declare(kernel32.SetCurrentDirectoryA, BOOL, LPCSTR)
    SetCurrentDirectoryW = declare(kernel32.SetCurrentDirectoryW, BOOL, LPCWSTR)
    SetCurrentDirectory = unicode(SetCurrentDirectoryW, SetCurrentDirectoryA)
    GetCurrentDirectoryA = declare(kernel32.GetCurrentDirectoryA, DWORD, DWORD, LPSTR)
    GetCurrentDirectoryW = declare(kernel32.GetCurrentDirectoryW, DWORD, DWORD, LPWSTR)
    GetCurrentDirectory = unicode(GetCurrentDirectoryW, GetCurrentDirectoryA)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    SearchPathA = declare(kernel32.SearchPathA, DWORD, LPCSTR, LPCSTR, LPCSTR, DWORD, LPSTR, POINTER(LPSTR))
    SearchPathW = declare(kernel32.SearchPathW, DWORD, LPCWSTR, LPCWSTR, LPCWSTR, DWORD, LPWSTR, POINTER(LPWSTR))
    SearchPath = unicode(SearchPathW, SearchPathA)

    # REGION *** Desktop Family or OneCore Family ***

    if cpreproc.getdef("_WINVER") >= 0x0502:
        NeedCurrentDirectoryForExePathA = declare(kernel32.NeedCurrentDirectoryForExePathA, BOOL, LPCSTR)
        NeedCurrentDirectoryForExePathW = declare(kernel32.NeedCurrentDirectoryForExePathW, BOOL, LPCWSTR)
        NeedCurrentDirectoryForExePath = unicode(NeedCurrentDirectoryForExePathW, NeedCurrentDirectoryForExePathA)

    # REGION ***
# _PROCESSENV_