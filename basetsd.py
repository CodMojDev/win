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

from .defbase import WT, IPointer, W_CDLL
from typing import overload, Any, Type

from ctypes import pointer as _pointer

from ctypes import *
from ctypes.wintypes import *
from .defbase import *

import sys

POINTER
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
        
    MAXUINT_PTR = UINT_PTR(~0).value
    MAXINT_PTR = UINT_PTR(MAXUINT_PTR.value >> 1).value
    MININT_PTR = INT_PTR(~MAXINT_PTR.value).value
    
    MAXULONG_PTR = ULONG_PTR(~0).value
    MAXLONG_PTR = ULONG_PTR(MAXULONG_PTR.value >> 1).value
    MINLONG_PTR = LONG_PTR(~MAXLONG_PTR.value).value
    
    MAXUHALF_PTR = UHALF_PTR(~0).value
    MAXHALF_PTR = UHALF_PTR(MAXUHALF_PTR.value >> 1).value
    MINHALF_PTR = HALF_PTR(~MAXHALF_PTR.value).value
    
    KAFFINITY = ULONG_PTR
    PKAFFINITY = PULONG_PTR
