"""
*****************************************************************************
*                                                                           *
* minwindef.h -- Basic Windows Type Definitions for minwin partition        *
*                                                                           *
* Copyright (c) Microsoft Corporation. All rights reserved.                 *
*                                                                           *
*****************************************************************************
"""

from . import cpreproc

from .defbase import CStructure

from .basetsd import *

if cpreproc.pragma_once("_MINWINDEF_"):
    PSZ = PCHAR

    FALSE = 0
    TRUE = 1

    #def CFUNCTYPE(restype, *argtypes, **kw): ...
    
    #def WINFUNCTYPE(restype, *argtypes, **kw): ...
    
    CDECL = CFUNCTYPE
    CALLBACK = WINFUNCTYPE
    WINAPI = WINFUNCTYPE
    APIENTRY = WINAPI
    APIPRIVATE = WINFUNCTYPE
    WINAPIV = CDECL

    LRESULT = LONG_PTR

    VOID = None
    PVOID = LPVOID
    PPVOID = POINTER(PVOID)
    PLPVOID = PPVOID
    
    NULL = VOID

    GLOBALHANDLE = HANDLE
    LOCALHANDLE = HANDLE
    SPHANDLE = LPHANDLE

    MAKEWORD = lambda a, b: (WORD((BYTE(DWORD_PTR(a).value & 0xFF).value) | (WORD(BYTE(DWORD_PTR(b).value & 0xFF).value)).value << 8)).value
    MAKELONG = lambda a, b: (LONG((WORD(DWORD_PTR(a).value & 0xFFFF).value) | (DWORD(WORD(DWORD_PTR(b).value & 0xFFFF).value)).value << 16)).value
    LOWORD = lambda l: (WORD((DWORD_PTR(l)).value & 0xFFFF)).value
    HIWORD = lambda l: (WORD((DWORD_PTR(l).value >> 16) & 0xFFFF)).value
    LOBYTE = lambda w: (BYTE((DWORD_PTR(w)).value & 0xFF)).value
    HIBYTE = lambda w: (WORD((DWORD_PTR(w).value >> 8) & 0xFF)).value

    PROC = WINAPI(INT)
    FARPROC = PROC
    NEARPROC = PROC

    HSPRITE = HANDLE
    HLSURF = HANDLE
    HFILE = INT
    
    #
    #  File System time stamps are represented with the following structure:
    #

    class FILETIME(CStructure):
        _fields_ = [
            ("dwLowDateTime", DWORD),
            ("dwHighDateTime", DWORD)
        ]
    _FILETIME = FILETIME
    PFILETIME = POINTER(FILETIME)
    LPFILETIME = PFILETIME
    cpreproc.define("_FILETIME_")

    LSTATUS = LONG