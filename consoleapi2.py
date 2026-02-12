"""
/********************************************************************************
*                                                                               *
* consoleapi2.h -- ApiSet Contract for api-ms-win-core-console-l2               *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from .winbase import PSECURITY_ATTRIBUTES

from .defbase import *

if cpreproc.pragma_once("_APISETCONSOLEL2_"):
    kernel32 = W_WinDLL("kernel32.dll")

    from .wincontypes import *

    # REGION *** Application Family or OneCore Family ***

    #
    # Attributes flags:
    #
    FOREGROUND_BLUE = 0x0001 # text color contains blue.
    FOREGROUND_GREEN = 0x0002 # text color contains green.
    FOREGROUND_RED = 0x0004 # text color contains red.
    FOREGROUND_INTENSITY = 0x0008 # text color is intensified.
    BACKGROUND_BLUE = 0x0010 # background color contains blue.
    BACKGROUND_GREEN = 0x0020 # background color contains green.
    BACKGROUND_RED = 0x0040 # background color contains red.
    BACKGROUND_INTENSITY = 0x0080 # background color is intensified.
    COMMON_LVB_LEADING_BYTE = 0x0100 # Leading Byte of DBCS
    COMMON_LVB_TRAILING_BYTE = 0x0200 # Trailing Byte of DBCS
    COMMON_LVB_GRID_HORIZONTAL = 0x0400 # DBCS: Grid attribute: top horizontal.
    COMMON_LVB_GRID_LVERTICAL = 0x0800 # DBCS: Grid attribute: left vertical.
    COMMON_LVB_GRID_RVERTICAL = 0x1000 # DBCS: Grid attribute: right vertical.
    COMMON_LVB_REVERSE_VIDEO = 0x4000 # DBCS: Reverse fore/back ground attribute.
    COMMON_LVB_UNDERSCORE = 0x8000 # DBCS: Underscore.
    COMMON_LVB_SBCSDBCS = 0x0300 # SBCS or DBCS flag.
    FillConsoleOutputCharacterA = declare(kernel32.FillConsoleOutputCharacterA, BOOL, HANDLE, CHAR, DWORD, COORD, LPDWORD)
    FillConsoleOutputCharacterW = declare(kernel32.FillConsoleOutputCharacterW, BOOL, HANDLE, WCHAR, DWORD, COORD, LPDWORD)
    FillConsoleOutputCharacter = unicode(FillConsoleOutputCharacterW, FillConsoleOutputCharacterA)
    FillConsoleOutputAttribute = declare(kernel32.FillConsoleOutputAttribute, BOOL, HANDLE, WORD, DWORD, COORD, LPDWORD)
    GenerateConsoleCtrlEvent = declare(kernel32.GenerateConsoleCtrlEvent, BOOL, DWORD, DWORD)
    CreateConsoleScreenBuffer = declare(kernel32.CreateConsoleScreenBuffer, HANDLE, DWORD, DWORD, PSECURITY_ATTRIBUTES, DWORD, LPVOID)
    SetConsoleActiveScreenBuffer = declare(kernel32.SetConsoleActiveScreenBuffer, BOOL, HANDLE)
    FlushConsoleInputBuffer = declare(kernel32.FlushConsoleInputBuffer, BOOL, HANDLE)
    SetConsoleCP = declare(kernel32.SetConsoleCP, BOOL, UINT)
    SetConsoleOutputCP = declare(kernel32.SetConsoleOutputCP, BOOL, UINT)

    class CONSOLE_CURSOR_INFO(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("bVisible", BOOL)
        ]
    PCONSOLE_CURSOR_INFO = POINTER(CONSOLE_CURSOR_INFO)

    GetConsoleCursorInfo = declare(kernel32.GetConsoleCursorInfo, BOOL, HANDLE, PCONSOLE_CURSOR_INFO)
    SetConsoleCursorInfo = declare(kernel32.SetConsoleCursorInfo, BOOL, HANDLE, PCONSOLE_CURSOR_INFO)

    class CONSOLE_SCREEN_BUFFER_INFO(CStructure):
        _fields_ = [
            ("dwSize", COORD),
            ("dwCursorPosition", COORD),
            ("wAttributes", WORD),
            ("srWindow", SMALL_RECT),
            ("dwMaximumWindowSize", COORD)
        ]
    PCONSOLE_SCREEN_BUFFER_INFO = POINTER(CONSOLE_SCREEN_BUFFER_INFO)

    GetConsoleScreenBufferInfo = declare(kernel32.GetConsoleScreenBufferInfo, BOOL, HANDLE, PCONSOLE_SCREEN_BUFFER_INFO)

    class CONSOLE_SCREEN_BUFFER_INFOEX(CStructure):
        _fields_ = [
            ("cbSize", ULONG),
            ("dwSize", COORD),
            ("dwCursorPosition", COORD),
            ("wAttributes", WORD),
            ("srWindow", SMALL_RECT),
            ("dwMaximumWindowSize", COORD),
            ("wPopupAttributes", WORD),
            ("bFullscreenSupported", BOOL),
            ("ColorTable", COLORREF * 16)
        ]
    PCONSOLE_SCREEN_BUFFER_INFOEX = POINTER(CONSOLE_SCREEN_BUFFER_INFOEX)

    GetConsoleScreenBufferInfoEx = declare(kernel32.GetConsoleScreenBufferInfoEx, BOOL, HANDLE, PCONSOLE_SCREEN_BUFFER_INFOEX)
    SetConsoleScreenBufferInfoEx = declare(kernel32.SetConsoleScreenBufferInfoEx, BOOL, HANDLE, PCONSOLE_SCREEN_BUFFER_INFOEX)
    SetConsoleScreenBufferSize = declare(kernel32.SetConsoleScreenBufferSize, BOOL, HANDLE, COORD)
    SetConsoleCursorPosition = declare(kernel32.SetConsoleCursorPosition, BOOL, HANDLE, COORD)
    GetLargestConsoleWindowSize = declare(kernel32.GetLargestConsoleWindowSize, COORD, HANDLE)
    SetConsoleTextAttribute = declare(kernel32.SetConsoleTextAttribute, BOOL, HANDLE, WORD)
    SetConsoleWindowInfo = declare(kernel32.SetConsoleWindowInfo, BOOL, HANDLE, BOOL, PSMALL_RECT)
    WriteConsoleOutputCharacterA = declare(kernel32.WriteConsoleOutputCharacterA, BOOL, HANDLE, LPCSTR, DWORD, COORD, LPDWORD)
    WriteConsoleOutputCharacterW = declare(kernel32.WriteConsoleOutputCharacterW, BOOL, HANDLE, LPCWSTR, DWORD, COORD, LPDWORD)
    WriteConsoleOutputCharacter = unicode(WriteConsoleOutputCharacterW, WriteConsoleOutputCharacterA)
    WriteConsoleOutputAttribute = declare(kernel32.WriteConsoleOutputAttribute, BOOL, HANDLE, PWORD, DWORD, COORD, LPDWORD)
    ReadConsoleOutputCharacterA = declare(kernel32.ReadConsoleOutputCharacterA, BOOL, HANDLE, LPSTR, DWORD, COORD, LPDWORD)
    ReadConsoleOutputCharacterW = declare(kernel32.ReadConsoleOutputCharacterW, BOOL, HANDLE, LPWSTR, DWORD, COORD, LPDWORD)
    ReadConsoleOutputCharacter = unicode(ReadConsoleOutputCharacterW, ReadConsoleOutputCharacterA)
    ReadConsoleOutputAttribute = declare(kernel32.ReadConsoleOutputAttribute, BOOL, HANDLE, LPWORD, DWORD, COORD, LPDWORD)
    WriteConsoleInputA = declare(kernel32.WriteConsoleInputA, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    WriteConsoleInputW = declare(kernel32.WriteConsoleInputW, BOOL, HANDLE, PINPUT_RECORD, DWORD, LPDWORD)
    WriteConsoleInput = unicode(WriteConsoleInputW, WriteConsoleInputA)
    ScrollConsoleScreenBufferA = declare(kernel32.ScrollConsoleScreenBufferA, BOOL, HANDLE, PSMALL_RECT, PSMALL_RECT, COORD, PCHAR_INFO)
    ScrollConsoleScreenBufferW = declare(kernel32.ScrollConsoleScreenBufferW, BOOL, HANDLE, PSMALL_RECT, PSMALL_RECT, COORD, PCHAR_INFO)
    ScrollConsoleScreenBuffer = unicode(ScrollConsoleScreenBufferW, ScrollConsoleScreenBufferA)
    WriteConsoleOutputA = declare(kernel32.WriteConsoleOutputA, BOOL, HANDLE, PCHAR_INFO, COORD, COORD, PSMALL_RECT)
    WriteConsoleOutputW = declare(kernel32.WriteConsoleOutputW, BOOL, HANDLE, PCHAR_INFO, COORD, COORD, PSMALL_RECT)
    WriteConsoleOutput = unicode(WriteConsoleOutputW, WriteConsoleOutputA)
    ReadConsoleOutputA = declare(kernel32.ReadConsoleOutputA, BOOL, HANDLE, PCHAR_INFO, COORD, COORD, PSMALL_RECT)
    ReadConsoleOutputW = declare(kernel32.ReadConsoleOutputW, BOOL, HANDLE, PCHAR_INFO, COORD, COORD, PSMALL_RECT)
    ReadConsoleOutput = unicode(ReadConsoleOutputW, ReadConsoleOutputA)
    GetConsoleTitleA = declare(kernel32.GetConsoleTitleA, DWORD, LPSTR, DWORD)
    GetConsoleTitleW = declare(kernel32.GetConsoleTitleW, DWORD, LPWSTR, DWORD)
    GetConsoleTitle = unicode(GetConsoleTitleW, GetConsoleTitleA)
    if cpreproc.getdef("_WINVER") >= 0x0600:
        GetConsoleOriginalTitleA = declare(kernel32.GetConsoleOriginalTitleA, DWORD, LPSTR, DWORD)
        GetConsoleOriginalTitleW = declare(kernel32.GetConsoleOriginalTitleW, DWORD, LPWSTR, DWORD)
        GetConsoleOriginalTitle = unicode(GetConsoleOriginalTitleW, GetConsoleOriginalTitleA)
    SetConsoleTitleA = declare(kernel32.SetConsoleTitleA, BOOL, LPCSTR)
    SetConsoleTitleW = declare(kernel32.SetConsoleTitleW, BOOL, LPCWSTR)
    SetConsoleTitle = unicode(SetConsoleTitleW, SetConsoleTitleA)

    # REGION ***
# _APISETCONSOLEL2_