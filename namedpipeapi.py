"""
 *******************************************************************************
 *                                                                               *
 * namedpipeapi.h - ApiSet Contract for api-ms-win-core-namedpipe-l1-1-0         *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *******************************************************************************
"""

from . import cpreproc

from .winbase import *

from .defbase import *

if cpreproc.pragma_once("_NAMEDPIPE_H_"):
    CreatePipe = declare(kernel32.CreatePipe, BOOL, PHANDLE, PHANDLE, LPSECURITY_ATTRIBUTES, DWORD)
    ConnectNamedPipe = declare(kernel32.ConnectNamedPipe, BOOL, HANDLE, LPOVERLAPPED)
    DisconnectNamedPipe = declare(kernel32.DisconnectNamedPipe, BOOL, HANDLE)
    SetNamedPipeHandleState = declare(kernel32.SetNamedPipeHandleState, BOOL, HANDLE, LPDWORD, LPDWORD, LPDWORD)
    PeekNamedPipe = declare(kernel32.PeekNamedPipe, BOOL, HANDLE, LPVOID, DWORD, LPDWORD, LPDWORD, LPDWORD)
    TransactNamedPipe = declare(kernel32.TransactNamedPipe, BOOL, HANDLE, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, LPOVERLAPPED)
    CreateNamedPipeA = declare(kernel32.CreateNamedPipeA, HANDLE, LPCSTR, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, LPSECURITY_ATTRIBUTES)
    CreateNamedPipeW = declare(kernel32.CreateNamedPipeW, HANDLE, LPCWSTR, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, LPSECURITY_ATTRIBUTES)
    CreateNamedPipe = unicode(CreateNamedPipeW, CreateNamedPipeA)
    WaitNamedPipeA = declare(kernel32.WaitNamedPipeA, BOOL, LPCSTR, DWORD)
    WaitNamedPipeW = declare(kernel32.WaitNamedPipeW, BOOL, LPCWSTR, DWORD)
    WaitNamedPipe = unicode(WaitNamedPipeA)
    if cpreproc.getdef("_WINVER") >= 0x0600:
        GetNamedPipeClientComputerNameA = declare(kernel32.GetNamedPipeClientComputerNameA, BOOL, HANDLE, LPSTR, ULONG)
        GetNamedPipeClientComputerNameW = declare(kernel32.GetNamedPipeClientComputerNameW, BOOL, HANDLE, LPWSTR, ULONG)
        GetNamedPipeClientComputerName = unicode(GetNamedPipeClientComputerNameW, GetNamedPipeClientComputerNameA)
        ImpersonateNamedPipeClient = declare(kernel32.ImpersonateNamedPipeClient, BOOL, HANDLE)

    # REGION *** Application Family or OneCore Family ***

    GetNamedPipeInfo = declare(kernel32.GetNamedPipeInfo, BOOL, HANDLE, LPDWORD, LPDWORD, LPDWORD, LPDWORD)
    GetNamedPipeHandleStateA = declare(kernel32.GetNamedPipeHandleStateA, BOOL, HANDLE, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPSTR, DWORD)
    GetNamedPipeHandleStateW = declare(kernel32.GetNamedPipeHandleStateW, BOOL, HANDLE, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)
    GetNamedPipeHandleState = unicode(GetNamedPipeHandleStateW, GetNamedPipeHandleStateA)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    CallNamedPipeW = declare(kernel32.CallNamedPipeW, BOOL, LPCWSTR, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, DWORD)
    CallNamedPipeA = declare(kernel32.CallNamedPipeA, BOOL, LPCSTR, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, DWORD)
    CallNamedPipe = unicode(CallNamedPipeW, CallNamedPipeA)

    # REGION ***
# _NAMEDPIPE_H_