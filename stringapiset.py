"""
 *********************************************************************************
 *                                                                               *
 * stringapi.h -- ApiSet Contract for api-ms-win-core-string-l1                  *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *

from .winnt import LPCWCH, PCNZWCH, LPCCH

from .defbase import *

from .winnls import LPNLSVERSIONINFO

if cpreproc.pragma_once("_APISETSTRING_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Desktop or OneCore or Application or Games Family ***

    CompareStringEx = declare(kernel32.CompareStringEx, INT, LPCWSTR, DWORD, LPCWCH, INT, LPCWCH, INT, LPNLSVERSIONINFO, LPVOID, LPARAM)
    CompareStringOrdinal = declare(kernel32.CompareStringOrdinal, INT, LPCWCH, INT, LPCWCH, INT, BOOL)
    CompareStringW = declare(kernel32.CompareStringW, INT, LCID, DWORD, PCNZWCH, INT, PCNZWCH, INT)
    if cpreproc.ifdef("UNICODE"):
        CompareString = CompareStringW
    FoldStringW = declare(kernel32.FoldStringW, INT, DWORD, LPCWCH, INT, LPWSTR, INT)
    if cpreproc.ifdef("UNICODE"):
        FoldString = FoldStringW
    GetStringTypeExW = declare(kernel32.GetStringTypeExW, BOOL, LCID, DWORD, LPCWCH, INT, LPWORD)
    if cpreproc.ifdef("UNICODE"):
        GetStringTypeEx = GetStringTypeExW
    GetStringTypeW = declare(kernel32.GetStringTypeW, BOOL, DWORD, LPCWCH, INT, LPWORD)
    #
    #  NLS Code Page Dependent APIs.
    #
    MultiByteToWideChar = declare(kernel32.MultiByteToWideChar, INT, UINT, DWORD, LPCCH, INT, LPWSTR, INT)
    WideCharToMultiByte = declare(kernel32.WideCharToMultiByte, INT, UINT, DWORD, LPCWCH, INT, LPSTR, INT, LPCCH, LPBOOL)

    # REGION ***
# _APISETSTRING_