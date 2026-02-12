"""
****************************************************************************\
 *                                                                             *
 *                                                                             *
 * Version 1.0                                                                 *
 *                                                                             *
 * Copyright (c) Microsoft Corporation. All rights reserved.                   *
 *                                                                             *
\****************************************************************************
"""

from . import cpreproc

from .minwindef import *
from .winnt import PCSTR, PCWSTR, PWSTR, PSTR
from .defbase import *
from .shtypes import *

if cpreproc.pragma_once("_INC_SHLWAPI"):
    shlwapi = W_WinDLL("shlwapi.dll")
    if cpreproc.ifndef("NOSHLWAPI"):

        # REGION *** Desktop Family or OneCore Family ***


        # REGION ***

        # REGION *** Application Family or OneCore Family ***

        # REGION ***

        # REGION *** Desktop Family or OneCore Family ***

        # REGION ***
        #
        # Users of this header may define any number of these constants to avoid
        # the definitions of each functional group.
        #
        #    NO_SHLWAPI_STRFCNS    String functions
        #    NO_SHLWAPI_PATH       Path functions
        #    NO_SHLWAPI_REG        Registry functions
        #    NO_SHLWAPI_STREAM     Stream functions
        #    NO_SHLWAPI_GDI        GDI helper functions
        if cpreproc.ifndef("NO_SHLWAPI_STRFCNS"):
            #
            #=============== String Routines ===================================
            #

            # REGION *** Desktop Family ***

            if cpreproc.ifdef("USE_STRICT_CONST"):
                StrChrA = declare(shlwapi.StrChrA, PCSTR, PCSTR, WORD)
                StrChrW = declare(shlwapi.StrChrW, PCWSTR, PCWSTR, WCHAR)
                StrChrIA = declare(shlwapi.StrChrIA, PCSTR, PCSTR, WORD)
                StrChrIW = declare(shlwapi.StrChrIW, PCWSTR, PCWSTR, WCHAR)
                StrChrNW = declare(shlwapi.StrChrNW, PCWSTR, PCWSTR, WCHAR, UINT)
                StrChrNIW = declare(shlwapi.StrChrNIW, PCWSTR, PCWSTR, WCHAR, UINT)
                StrChrA = declare(shlwapi.StrChrA, PSTR, PCSTR, WORD)
                StrChrW = declare(shlwapi.StrChrW, PWSTR, PCWSTR, WCHAR)
                StrChrIA = declare(shlwapi.StrChrIA, PSTR, PCSTR, WORD)
                StrChrIW = declare(shlwapi.StrChrIW, PWSTR, PCWSTR, WCHAR)
                StrChrNW = declare(shlwapi.StrChrNW, PWSTR, PCWSTR, WCHAR, UINT)
                StrChrNIW = declare(shlwapi.StrChrNIW, PWSTR, PCWSTR, WCHAR, UINT)
                StrCmpNA = declare(shlwapi.StrCmpNA, INT, PCSTR, PCSTR, INT)
                StrCmpNW = declare(shlwapi.StrCmpNW, INT, PCWSTR, PCWSTR, INT)
                StrCmpNIA = declare(shlwapi.StrCmpNIA, INT, PCSTR, PCSTR, INT)
                StrCmpNIW = declare(shlwapi.StrCmpNIW, INT, PCWSTR, PCWSTR, INT)
                StrCSpnA = declare(shlwapi.StrCSpnA, INT, PCSTR, PCSTR)
                StrCSpnW = declare(shlwapi.StrCSpnW, INT, PCWSTR, PCWSTR)
                StrCSpnIA = declare(shlwapi.StrCSpnIA, INT, PCSTR, PCSTR)
                StrCSpnIW = declare(shlwapi.StrCSpnIW, INT, PCWSTR, PCWSTR)
                StrDupA = declare(shlwapi.StrDupA, PSTR, PCSTR)
                StrDupW = declare(shlwapi.StrDupW, PWSTR, PCWSTR)
                # StrFormatByteSizeEx takes a ULONGLONG as a byte count and formats a string
                # representing that number of bytes in an appropriately concise manner, where
                # "appropriate manner" is determine by several factors:
                #
                # 1) order - is this most appropriately expressed as KB? MB? GB?
                #    for example: 1039 -> "1.01 KB", 5454608466 -> "5.08 GB", etc
                #
                # 2) number of whole number places shown - if there are more than a few whole
                #    number places to display, decimal places are omitted.
                #    for example: 1024 -> "1.00 KB", 12288 -> "12.0 KB", 125952 -> "123 KB"
                #
                # 3) the caller can specify whether the result should involve rounding to the
                #    nearest displayed digit, or truncation of undisplayed digits. the caller
                #    must specify either rounding or truncation when calling the API.
                #    for example: with rounding,   2147483647 -> "2.00 GB"
                #                 with truncation, 2147483647 -> "1.99 GB"
                SFBS_FLAGS = INT
                if True:
                    SFBS_FLAGS_ROUND_TO_NEAREST_DISPLAYED_DIGIT     = 0x0001   # round to the nearest displayed digit
                    SFBS_FLAGS_TRUNCATE_UNDISPLAYED_DECIMAL_DIGITS  = 0x0002   # discard undisplayed digits
                StrFormatByteSizeEx = declare(shlwapi.StrFormatByteSizeEx, VOID, ULONGLONG, SFBS_FLAGS, PWSTR)
                # (NTDDI_VERSION >= NTDDI_VISTASP1)
                StrFormatByteSizeA = declare(shlwapi.StrFormatByteSizeA, PSTR, DWORD, PSTR, UINT)
                StrFormatByteSize64A = declare(shlwapi.StrFormatByteSize64A, PSTR, LONGLONG, PSTR, UINT)
                StrFormatByteSizeW = declare(shlwapi.StrFormatByteSizeW, PSTR, LONGLONG, PWSTR, UINT)
                StrFormatKBSizeW = declare(shlwapi.StrFormatKBSizeW, PWSTR, LONGLONG, PWSTR, UINT)
                StrFormatKBSizeA = declare(shlwapi.StrFormatKBSizeA, PSTR, LONGLONG, PSTR, UINT)
                StrFromTimeIntervalA = declare(shlwapi.StrFromTimeIntervalA, INT, PSTR, UINT, DWORD, INT)
                StrFromTimeIntervalW = declare(shlwapi.StrFromTimeIntervalW, INT, PWSTR, UINT, DWORD, INT)
                StrIsIntlEqualA = declare(shlwapi.StrIsIntlEqualA, BOOL, BOOL, PCSTR, PCSTR, INT)
                StrIsIntlEqualW = declare(shlwapi.StrIsIntlEqualW, BOOL, BOOL, PCWSTR, PCWSTR, INT)
                StrNCatA = declare(shlwapi.StrNCatA, PSTR, PSTR, PCSTR, INT)
                StrNCatW = declare(shlwapi.StrNCatW, PWSTR, PWSTR, PCWSTR, INT)
                if cpreproc.ifdef("USE_STRICT_CONST"):
                    StrPBrkA = declare(shlwapi.StrPBrkA, PCSTR, PCSTR, PCSTR)
                    StrPBrkW = declare(shlwapi.StrPBrkW, PCWSTR, PCWSTR, PCWSTR)
                    StrRChrA = declare(shlwapi.StrRChrA, PCSTR, PCSTR, PCSTR, WORD)
                    StrRChrW = declare(shlwapi.StrRChrW, PCWSTR, PCWSTR, PCWSTR, WCHAR)
                    StrRChrIA = declare(shlwapi.StrRChrIA, PCSTR, PCSTR, PCSTR, WORD)
                    StrRChrIW = declare(shlwapi.StrRChrIW, PCWSTR, PCWSTR, PCWSTR, WCHAR)
                    StrRStrIA = declare(shlwapi.StrRStrIA, PCSTR, PCSTR, PCSTR, PCSTR)
                    StrRStrIW = declare(shlwapi.StrRStrIW, PCWSTR, PCWSTR, PCWSTR, PCWSTR)
                else:
                    StrPBrkA = declare(shlwapi.StrPBrkA, PCSTR, PCSTR, PCSTR)
                    StrPBrkW = declare(shlwapi.StrPBrkW, PCWSTR, PCWSTR, PCWSTR)
                    StrRChrA = declare(shlwapi.StrRChrA, PCSTR, PCSTR, PCSTR, WORD)
                    StrRChrW = declare(shlwapi.StrRChrW, PCWSTR, PCWSTR, PCWSTR, WCHAR)
                    StrRChrIA = declare(shlwapi.StrRChrIA, PCSTR, PCSTR, PCSTR, WORD)
                    StrRChrIW = declare(shlwapi.StrRChrIW, PCWSTR, PCWSTR, PCWSTR, WCHAR)
                    StrRStrIA = declare(shlwapi.StrRStrIA, PCSTR, PCSTR, PCSTR, PCSTR)
                    StrRStrIW = declare(shlwapi.StrRStrIW, PCWSTR, PCWSTR, PCWSTR, PCWSTR)
                StrSpnA = declare(shlwapi.StrSpnA, INT, PCSTR, PCSTR)
                StrSpnW = declare(shlwapi.StrSpnW, INT, PCWSTR, PCWSTR)
                if cpreproc.ifdef("USE_STRICT_CONST"):
                    StrStrA = declare(shlwapi.StrStrA, PCSTR, PCSTR, PCSTR)
                    StrStrW = declare(shlwapi.StrStrW, PCWSTR, PCWSTR, PCWSTR)
                    StrStrIA = declare(shlwapi.StrStrIA, PCSTR, PCSTR, PCSTR)
                    StrStrIW = declare(shlwapi.StrStrIW, PCWSTR, PCWSTR, PCWSTR)
                    StrStrNW = declare(shlwapi.StrStrNW, PCWSTR, PCWSTR, PCWSTR, UINT)
                    StrStrNIW = declare(shlwapi.StrStrNIW, PCWSTR, PCWSTR, PCWSTR, UINT)
                else:
                    StrStrA = declare(shlwapi.StrStrA, PSTR, PCSTR, PCSTR)
                    StrStrW = declare(shlwapi.StrStrW, PWSTR, PCWSTR, PCWSTR)
                    StrStrIA = declare(shlwapi.StrStrIA, PSTR, PCSTR, PCSTR)
                    StrStrIW = declare(shlwapi.StrStrIW, PCWSTR, PCWSTR, PCWSTR)
                    StrStrNW = declare(shlwapi.StrStrNW, PWSTR, PCWSTR, PCWSTR, UINT)
                    StrStrNIW = declare(shlwapi.StrStrNIW, PWSTR, PCWSTR, PCWSTR, UINT)
                STIF_DEFAULT = 0x00000000
                STIF_SUPPORT_HEX = 0x00000001
                STIF_FLAGS = INT
                StrToIntA = declare(shlwapi.StrToIntA, INT, PCSTR)
                StrToIntW = declare(shlwapi.StrToIntW, INT, PCWSTR)
                StrToIntExA = declare(shlwapi.StrToIntExA, BOOL, PCSTR, STIF_FLAGS, PINT)
                StrToIntExW = declare(shlwapi.StrToIntExW, BOOL, PCWSTR, STIF_FLAGS, PINT)
                StrToInt64ExA = declare(shlwapi.StrToInt64ExA, BOOL, PCSTR, STIF_FLAGS, PLONGLONG)
                StrToInt64ExW = declare(shlwapi.StrToInt64ExW, BOOL, PCWSTR, STIF_FLAGS, PLONGLONG)
                StrTrimA = declare(shlwapi.StrTrimA, BOOL, PSTR, PCSTR)
                StrTrimW = declare(shlwapi.StrTrimW, BOOL, PWSTR, PCWSTR)
                StrCatW = declare(shlwapi.StrCatW, PWSTR, PWSTR, PCWSTR)
                StrCmpW = declare(shlwapi.StrCmpW, INT, PCWSTR, PCWSTR)
                StrCmpIW = declare(shlwapi.StrCmpIW, INT, PCWSTR, PCWSTR)
                StrCpyW = declare(shlwapi.StrCpyW, PWSTR, PWSTR, PCWSTR)
                StrCpyNW = declare(shlwapi.StrCpyNW, PWSTR, PWSTR, PCWSTR)
                StrCatBuffW = declare(shlwapi.StrCatBuffW, PWSTR, PWSTR, PCWSTR, INT)
                StrCatBuffA = declare(shlwapi.StrCatBuffA, PSTR, PSTR, PCSTR, INT)
                ChrCmpIA = declare(shlwapi.ChrCmpIA, BOOL, WORD, WORD)
                ChrCmpIW = declare(shlwapi.ChrCmpIW, BOOL, WCHAR, WCHAR)
                wvnsprintfA = declare(shlwapi.wvnsprintfA, INT, PSTR, INT, PCSTR)
                wvnsprintfW = declare(shlwapi.wvnsprintfW, INT, PWSTR, INT, PCWSTR)
                wnsprintfA = declare(shlwapi.wnsprintfA, INT, PSTR, INT, PCSTR)
                wnsprintfW = declare(shlwapi.wnsprintfW, INT, PWSTR, INT, PCWSTR)
                StrIntlEqNA = lambda s1, s2, nChar: StrIsIntlEqualA(TRUE, s1, s2, nChar)
                StrIntlEqNW = lambda s1, s2, nChar: StrIsIntlEqualW(TRUE, s1, s2, nChar)
                StrIntlEqNIA = lambda s1, s2, nChar: StrIsIntlEqualA(FALSE, s1, s2, nChar)
                StrIntlEqNIW = lambda s1, s2, nChar: StrIsIntlEqualW(FALSE, s1, s2, nChar)
                StrRetToStrA = declare(shlwapi.StrRetToStrA, VOID, LPSTRRET, PCUITEMID_CHILD, POINTER(LPSTR))
                StrRetToStrW = declare(shlwapi.StrRetToStrW, VOID, LPSTRRET, PCUITEMID_CHILD, POINTER(LPWSTR))
                StrRetToStr = unicode(StrRetToStrW, StrRetToStrA)
                # !UNICODE
                StrRetToBufA = declare(shlwapi.StrRetToBufA, VOID, LPSTRRET, PCUITEMID_CHILD, LPSTR, UINT)
                StrRetToBufW = declare(shlwapi.StrRetToBufW, VOID, LPSTRRET, PCUITEMID_CHILD, LPWSTR, UINT)
                StrRetToBuf = unicode(StrRetToBufW, StrRetToBufA)
                # !UNICODE
                # helper to duplicate a string using the task allocator
                SHStrDupA = declare(shlwapi.SHStrDupA, VOID, LPCSTR, POINTER(LPWSTR))
                SHStrDupW = declare(shlwapi.SHStrDupW, VOID, LPCWSTR, POINTER(LPWSTR))
                SHStrDup = unicode(SHStrDupW, SHStrDupA)
                # !UNICODE
# TODO
# NOT REALIZED