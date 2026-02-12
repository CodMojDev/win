"""
 *********************************************************************************
 *                                                                               *
 * errhandlingapi.h - ApiSet Contract for api-ms-win-core-errorhandling-l1       *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .basetsd import *

from .winnt import (PVOID, SIZE_T, PULONG_PTR, 
                    PCONTEXT, VOID, EXCEPTION_RECORD,
                    WINAPI, PEXCEPTION_POINTERS, TEXT,
                    PVECTORED_EXCEPTION_HANDLER)

from typing import (Callable)

from .defbase import *

if cpreproc.pragma_once("_ERRHANDLING_H_"):
    
    kernel32 = W_WinDLL("kernel32.dll")
    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # Typedefs
    #

    PTOP_LEVEL_EXCEPTION_FILTER = WINAPI(LONG, PEXCEPTION_POINTERS)
    LPTOP_LEVEL_EXCEPTION_FILTER = PTOP_LEVEL_EXCEPTION_FILTER

    #
    # Prototypes
    #
    RaiseException = declare(kernel32.RaiseException, VOID, DWORD, DWORD, DWORD, PULONG_PTR)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    UnhandledExceptionFilter = declare(kernel32.UnhandledExceptionFilter, LONG, PEXCEPTION_POINTERS)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    SetUnhandledExceptionFilter = declare(kernel32.SetUnhandledExceptionFilter, LPTOP_LEVEL_EXCEPTION_FILTER, LPTOP_LEVEL_EXCEPTION_FILTER)
    GetLastError = declare(kernel32.GetLastError, DWORD, VOID)
    SetLastError = declare(kernel32.SetLastError, VOID, DWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetErrorMode = declare(kernel32.GetErrorMode, UINT, VOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    SetErrorMode = declare(kernel32.SetErrorMode, UINT, UINT)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    AddVectoredExceptionHandler = declare(kernel32.AddVectoredExceptionHandler, PVOID, ULONG, PVECTORED_EXCEPTION_HANDLER)
    RemoveVectoredExceptionHandler = declare(kernel32.RemoveVectoredExceptionHandler, ULONG, PVOID)
    AddVectoredContinueHandler = declare(kernel32.AddVectoredContinueHandler, PVOID, ULONG, PVECTORED_EXCEPTION_HANDLER)
    RemoveVectoredContinueHandler = declare(kernel32.RemoveVectoredContinueHandler, ULONG, PVOID)
    # RC warns because "WINBASE_DECLARE_RESTORE_LAST_ERROR" is a bit long.
    
    RestoreLastError = declare(kernel32.RestoreLastError, VOID, DWORD)

    PRESTORE_LAST_ERROR = WINAPI(VOID, DWORD)
    
    RESTORE_LAST_ERROR_NAME_A = "RestoreLastError"
    RESTORE_LAST_ERROR_NAME_W = u"RestoreLastError"
    RESTORE_LAST_ERROR_NAME = TEXT("RestoreLastError")

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    RaiseFailFastException = declare(kernel32.RaiseFailFastException, VOID, POINTER(EXCEPTION_RECORD), PCONTEXT, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    FatalAppExitA = declare(kernel32.FatalAppExitA, VOID, UINT, LPCSTR)
    FatalAppExitW = declare(kernel32.FatalAppExitW, VOID, UINT, LPCWSTR)
    FatalAppExit = unicode(FatalAppExitW, FatalAppExitA)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetThreadErrorMode = declare(kernel32.GetThreadErrorMode, DWORD, VOID)
    SetThreadErrorMode = declare(kernel32.SetThreadErrorMode, BOOL, DWORD, LPDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    TerminateProcessOnMemoryExhaustion = declare(kernelbase.TerminateProcessOnMemoryExhaustion, VOID, SIZE_T)

    # REGION ***
# _ERRHANDLING_H_