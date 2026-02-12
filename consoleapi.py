# begin_consoleapi_h
"""
/********************************************************************************
*                                                                               *
* consoleapi.h -- ApiSet Contract for api-ms-win-core-console-l1                *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

if cpreproc.pragma_once("_APISETCONSOLE_"):
    from .wincontypes import *

    kernelbase = W_WinDLL("kernelbase.dll")

    # REGION *** Application Family or OneCore Family ***

    AllocConsole = declare(kernelbase.AllocConsole, BOOL, VOID)
    FreeConsole = declare(kernelbase.FreeConsole, BOOL, VOID)
    AttachConsole = declare(kernelbase.AttachConsole, BOOL, DWORD)
    ATTACH_PARENT_PROCESS = DWORD(-1).value
    GetConsoleCP = declare(kernelbase.GetConsoleCP, UINT, VOID)
    GetConsoleOutputCP = declare(kernelbase.GetConsoleOutputCP, UINT, VOID)
    #
    # Input Mode flags:
    #
    ENABLE_PROCESSED_INPUT = 0x0001
    ENABLE_LINE_INPUT = 0x0002
    ENABLE_ECHO_INPUT = 0x0004
    ENABLE_WINDOW_INPUT = 0x0008
    ENABLE_MOUSE_INPUT = 0x0010
    ENABLE_INSERT_MODE = 0x0020
    ENABLE_QUICK_EDIT_MODE = 0x0040
    ENABLE_EXTENDED_FLAGS = 0x0080
    ENABLE_AUTO_POSITION = 0x0100
    ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200
    #
    # Output Mode flags:
    #
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    DISABLE_NEWLINE_AUTO_RETURN = 0x0008
    ENABLE_LVB_GRID_WORLDWIDE = 0x0010
    GetConsoleMode = declare(kernelbase.GetConsoleMode, BOOL, HANDLE, LPDWORD)
    SetConsoleMode = declare(kernelbase.SetConsoleMode, BOOL, HANDLE, DWORD)
    GetNumberOfConsoleInputEvents = declare(kernelbase.GetNumberOfConsoleInputEvents, BOOL, HANDLE, LPDWORD)
    ReadConsoleInputA = declare(kernelbase.ReadConsoleInputA, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    ReadConsoleInputW = declare(kernelbase.ReadConsoleInputW, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    ReadConsoleInput = unicode(ReadConsoleInputW, ReadConsoleInputA)
    PeekConsoleInputA = declare(kernelbase.PeekConsoleInputA, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    PeekConsoleInputW = declare(kernelbase.PeekConsoleInputW, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    PeekConsoleInput = unicode(PeekConsoleInputW, PeekConsoleInputA)

    class CONSOLE_READCONSOLE_CONTROL(CStructure):
        _fields_ = [
            ("nLength", ULONG),
            ("nInitialChars", ULONG),
            ("dwCtrlWakeupMask", ULONG),
            ("dwControlKeyState", ULONG)
        ]
    PCONSOLE_READCONSOLE_CONTROL = POINTER(CONSOLE_READCONSOLE_CONTROL)

    ReadConsoleA = declare(kernelbase.ReadConsoleA, BOOL, HANDLE, LPVOID, DWORD, LPDWORD, PCONSOLE_READCONSOLE_CONTROL)
    ReadConsoleW = declare(kernelbase.ReadConsoleW, BOOL, HANDLE, LPVOID, DWORD, LPDWORD, PCONSOLE_READCONSOLE_CONTROL)
    ReadConsole = unicode(ReadConsoleW, ReadConsoleA)
    WriteConsoleA = declare(kernelbase.WriteConsoleA, BOOL, HANDLE, PVOID, DWORD, LPDWORD, LPVOID)
    WriteConsoleW = declare(kernelbase.WriteConsoleW, BOOL, HANDLE, PVOID, DWORD, LPDWORD, LPVOID)
    WriteConsole = unicode(WriteConsoleW, WriteConsoleA)
    #
    # Ctrl Event flags
    #
    CTRL_C_EVENT = 0
    CTRL_BREAK_EVENT = 1
    CTRL_CLOSE_EVENT = 2
    # 3 is reserved!
    # 4 is reserved!
    CTRL_LOGOFF_EVENT = 5
    CTRL_SHUTDOWN_EVENT = 6
    #
    # typedef for ctrl-c handler routines
    #
    PHANDLER_ROUTINE = WINAPI(BOOL, DWORD)
    SetConsoleCtrlHandler = declare(kernelbase.SetConsoleCtrlHandler, BOOL, PHANDLER_ROUTINE, BOOL)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    # CreatePseudoConsole Flags
    PSEUDOCONSOLE_INHERIT_CURSOR = (0x1)
    CreatePseudoConsole = declare(kernelbase.CreatePseudoConsole, HRESULT, COORD, HANDLE, HANDLE, DWORD, POINTER(HPCON))
    ResizePseudoConsole = declare(kernelbase.ResizePseudoConsole, HRESULT, HPCON, COORD)
    ClosePseudoConsole = declare(kernelbase.ClosePseudoConsole, VOID, HPCON)

    # REGION ***
# _APISETCONSOLE_
# end_consoleapi_h