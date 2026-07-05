"""++

Copyright (c) Microsoft Corporation.  All rights reserved.

Module Name:

    basetsd.h

Abstract:

    Type definitions for the basic sized types.

Author:

Revision History:

--"""

from . import cpreproc

from ctypes import pointer as _pointer

from ctypes import *
from .defbase import *

#
# type definitions for independence from ctypes.wintypes
#

BYTE = c_ubyte
WORD = c_ushort
DWORD = c_ulong
CHAR = c_char
WCHAR = c_wchar
UINT = c_uint
INT = c_int
DOUBLE = c_double
FLOAT = c_float
BOOLEAN = BYTE
BOOL = c_long
ULONG = c_ulong
LONG = c_long
USHORT = c_ushort
SHORT = c_short
LARGE_INTEGER = c_longlong
ULARGE_INTEGER = c_ulonglong
LPCVOID = LPVOID = c_void_p
if sizeof(c_void_p) == 4:
    WPARAM = c_ulong
    LPARAM = c_long
else:
    WPARAM = c_ulonglong
    LPARAM = c_longlong
ATOM = WORD
LANGID = WORD
COLORREF = DWORD
LGRPID = DWORD
LCTYPE = DWORD
LCID = DWORD
HANDLE = c_void_p
HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HCURSOR = HANDLE
HDC = HANDLE
HDESK = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE
MAX_PATH = 260
HRESULT = LONG

class RECT(CStructure):
    _fields_ = [
        ('left', LONG),
        ('top', LONG),
        ('right', LONG),
        ('bottom', LONG)
    ]
    left: int
    top: int
    right: int
    bottom: int

RECTL = RECT
    
class SMALL_RECT(CStructure):
    _fields_ = [('Left', SHORT),
                ('Top', SHORT),
                ('Right', SHORT),
                ('Bottom', SHORT)]
    Left: int
    Top: int
    Right: int
    Bottom: int
tagSMALL_RECT = SMALL_RECT

class COORD(CStructure):
    _fields_ = [('X', SHORT), ('Y', SHORT)]
    X: int
    Y: int
tagCOORD = COORD

class POINT(CStructure):
    _fields_ = [("x", LONG),
                ("y", LONG)]
    x: int
    y: int
tagPOINT = POINTL = POINT

class SIZE(CStructure):
    _fields_ = [("cx", LONG),
                ("cy", LONG)]
    cx: int
    cy: int
tagSIZE = SIZEL = SIZE

class MSG(CStructure):
    _fields_ = [("hWnd", HWND),
                ("message", UINT),
                ("wParam", WPARAM),
                ("lParam", LPARAM),
                ("time", DWORD),
                ("pt", POINT)]
    hWnd: int
    message: int
    wParam: int
    lParam: int
    time: int
    pt: POINT

_PWCH = PTRD(WCHAR)
_PCH = PTRD(CHAR)

class LPWSTR(c_wchar_p):
    from_param = c_wchar_p.from_param
    
    def __getitem__(self, i: int) -> str:
        return i_cast(addressof(self), _PWCH)[i]
    
    def __setitem__(self, i: int, c: str):
        i_cast(addressof(self), _PWCH)[i] = c
    
class LPSTR(c_char_p):
    from_param = c_char_p.from_param
    
    def __getitem__(self, i: int) -> int:
        return i_cast(addressof(self), _PCH)[i][0]
    
    def __setitem__(self, i: int, c: bytes):
        i_cast(addressof(self), _PCH)[i] = c

LPCOLESTR = LPOLESTR = OLESTR = LPCWSTR = LPWSTR
LPCSTR = LPSTR

from typing import overload, Any, Type
        
import ctypes.wintypes
        
LPBOOL = PBOOL = PTR(BOOL)
PBOOLEAN = LPBOOLEAN = PTR(BOOLEAN)
LPBYTE = PBYTE = PTR(BYTE)
PCHAR = LPCHAR = LPSTR
LPCOLORREF = PTR(COLORREF)
LPDWORD = PDWORD = PTR(DWORD)
PFLOAT = PTR(FLOAT)
LPHANDLE = PHANDLE = PTR(HANDLE)
PHKEY = PTR(HKEY)
LPHKL = PHKL = PTR(HKL)
LPINT = PINT = PTR(INT)
PLARGE_INTEGER = PTR(LARGE_INTEGER)
PLCID = PTR(LCID)
LPLONG = PLONG = PTR(LONG)
LPMSG = PMSG = PTR(MSG)
LPPOINT = PPOINT = PTR(POINT)
PPOINTL = PTR(POINTL)
LPRECT = LPCRECT = PRECT = PTR(RECT)
LPRECTL = LPCRECTL = PRECTL = PTR(RECTL)
LPSC_HANDLE = PTR(SC_HANDLE)
PSHORT = LPSHORT = LPCSHORT = PTR(SHORT)
LPSIZE = LPCSIZE = PSIZE = PTR(SIZE)
LPSIZEL = LPCSIZEL = PSIZEL = PTR(SIZEL)
PSMALL_RECT = LPSMALL_RECT = PTR(SMALL_RECT)
LPUINT = PUINT = PTR(UINT)
PULARGE_INTEGER = PTR(ULARGE_INTEGER)
PULONG = LPULONG = PTR(ULONG)
PUSHORT = LPUSHORT = PTR(USHORT)
PWCHAR = PTR(WCHAR)
LPWORD = PWORD = PTR(WORD)

class FILETIME(ctypes.Structure):
    _fields_ = [("dwLowDateTime", DWORD),
                ("dwHighDateTime", DWORD)]
_FILETIME = FILETIME

class WIN32_FIND_DATAA(CStructure):
    _fields_ = [("dwFileAttributes", DWORD),
                ("ftCreationTime", FILETIME),
                ("ftLastAccessTime", FILETIME),
                ("ftLastWriteTime", FILETIME),
                ("nFileSizeHigh", DWORD),
                ("nFileSizeLow", DWORD),
                ("dwReserved0", DWORD),
                ("dwReserved1", DWORD),
                ("cFileName", CHAR * MAX_PATH),
                ("cAlternateFileName", CHAR * 14)]

LPWIN32_FIND_DATAA = PTR(WIN32_FIND_DATAA)

class WIN32_FIND_DATAW(CStructure):
    _fields_ = [("dwFileAttributes", DWORD),
                ("ftCreationTime", FILETIME),
                ("ftLastAccessTime", FILETIME),
                ("ftLastWriteTime", FILETIME),
                ("nFileSizeHigh", DWORD),
                ("nFileSizeLow", DWORD),
                ("dwReserved0", DWORD),
                ("dwReserved1", DWORD),
                ("cFileName", WCHAR * MAX_PATH),
                ("cAlternateFileName", WCHAR * 14)]

LPWIN32_FIND_DATAW = PTR(WIN32_FIND_DATAW)

import sys

def pointer(obj: WT, /) -> IPointer[WT]: ...

pointer = _pointer

if cpreproc.pragma_once("_BASETSD_H_"):
    INT8 = c_int8
    PINT8 = POINTER(INT8)
    
    INT16 = c_int16
    PINT16 = POINTER(INT16)
    
    INT32 = c_int32
    PINT32 = POINTER(INT32)
    
    INT64 = c_int64
    PINT64 = POINTER(INT64)
    
    UINT8 = c_uint8
    PUINT8 = POINTER(UINT8)
    
    UINT16 = c_uint16
    PUINT16 = POINTER(UINT16)
    
    UINT32 = c_uint32
    PUINT32 = POINTER(UINT32)
    
    UINT64 = c_uint64
    PUINT64 = POINTER(UINT64)
    
    LONG32 = INT
    PLONG32 = PINT
    
    ULONG32 = UINT
    PULONG32 = PUINT
    
    DWORD32 = UINT
    PDWORD32 = PUINT
    
    INT_PTR = INT
    PINT_PTR = PINT
    UINT_PTR = UINT
    PUINT_PTR = PUINT

    LONGLONG = INT64
    ULONGLONG = UINT64
    
    MAXLONGLONG = 0x7fffffffffffffff
    
    PLONGLONG = POINTER(LONGLONG)
    PULONGLONG = POINTER(ULONGLONG)

    LONG_PTR = LONGLONG
    PLONG_PTR = PLONGLONG
    ULONG_PTR = ULONGLONG
    PULONG_PTR = PULONGLONG

    ADDRESS_TAG_BIT = 0x40000000000

    SHANDLE_PTR = INT64
    HANDLE_PTR = INT64

    UHALF_PTR = UINT
    PUHALF_PTR = PUINT

    HALF_PTR = INT
    PHALF_PTR = PINT

    HandleToULong = lambda h: ULONG(h.value)
    HandleToLong = lambda h: LONG(h.value)
    
    ULongToHandle = lambda ul: cast(ul, HANDLE)
    LongToHandle = lambda h: cast(h, HANDLE)
    
    PtrToUlong = lambda p: ULONG(cast(p, LPVOID).value)
    PtrToLong = lambda p: LONG(cast(p, LPVOID).value)
    
    PtrToUint = lambda p: UINT(cast(p, LPVOID).value)
    PtrToInt = lambda p: INT(cast(p, LPVOID).value)
    
    PtrToUshort = lambda p: USHORT(cast(p, LPVOID).value)
    PtrToShort = lambda p: SHORT(cast(p, LPVOID).value)
    
    IntToPtr = lambda i: cast(i, LPVOID)
    UIntToPtr = lambda i: cast(i, LPVOID)

    LongToPtr = lambda i: cast(i, LPVOID)
    ULongToPtr = lambda i: cast(i, LPVOID)

    LONG64 = INT64
    PLONG64 = POINTER(LONG64)
    
    ULONG64 = UINT64
    PULONG64 = POINTER(ULONG64)
    
    DWORD64 = ULONG64
    PDWORD64 = PULONG64

    if cpreproc.ifdef("_WIN64"): # 64-bit
        INT_PTR   = INT64
        UINT_PTR  = UINT64
        LONG_PTR  = INT64
        ULONG_PTR = UINT64
        UHALF_PTR = UINT64  # or c_uint32 depending on definition
        SIZE_T    = UINT64
        SSIZE_T   = INT64
        PSIZE_T   = PUINT64
        PSSIZE_T  = PINT64
        DWORD_PTR = UINT64
        PDWORD_PTR = PUINT64
    else: # 32-bit
        INT_PTR   = INT
        UINT_PTR  = UINT
        LONG_PTR  = LONG
        ULONG_PTR = ULONG
        UHALF_PTR = UINT
        PHALF_PTR = PINT
        SIZE_T    = UINT
        SSIZE_T   = INT
        PSIZE_T   = PUINT
        PSSIZE_T  = PINT
        DWORD_PTR = UINT
        PDWORD_PTR = PUINT
        
    MAXUINT_PTR = UINT_PTR(~0).value
    MAXINT_PTR = UINT_PTR(MAXUINT_PTR >> 1).value
    MININT_PTR = INT_PTR(~MAXINT_PTR).value
    
    MAXULONG_PTR = ULONG_PTR(~0).value
    MAXLONG_PTR = ULONG_PTR(MAXULONG_PTR >> 1).value
    MINLONG_PTR = LONG_PTR(~MAXLONG_PTR).value
    
    MAXUHALF_PTR = UHALF_PTR(~0).value
    MAXHALF_PTR = UHALF_PTR(MAXUHALF_PTR >> 1).value
    MINHALF_PTR = HALF_PTR(~MAXHALF_PTR).value
    
    KAFFINITY = ULONG_PTR
    PKAFFINITY = PULONG_PTR
