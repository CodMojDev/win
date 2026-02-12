"""
/********************************************************************************
*                                                                               *
* consoleapi3.h -- ApiSet Contract for api-ms-win-core-console-l3               *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

from .wincontypes import *

from .defbase import *

if cpreproc.pragma_once("_APISETCONSOLEL3_"):
    kernel32 = W_WinDLL("kernel32.dll")

    if cpreproc.ifndef("NOGDI"):
        from .wingdi import *

    # REGION *** Application Family or OneCore Family ***

    GetNumberOfConsoleMouseButtons = declare(kernel32.GetNumberOfConsoleMouseButtons, BOOL, LPDWORD)
    if cpreproc.getdef("_WINVER") >= 0x0500:
        GetConsoleFontSize = declare(kernel32.GetConsoleFontSize, COORD, HANDLE, DWORD)
        GetCurrentConsoleFont = declare(kernel32.GetCurrentConsoleFont, BOOL, HANDLE, BOOL, PCONSOLE_FONT_INFO)
        if cpreproc.ifndef("NOGDI"):

            class CONSOLE_FONT_INFOEX(CStructure):
                _fields_ = [
                    ("cbSize", ULONG),
                    ("nFont", DWORD),
                    ("dwFontSize", COORD),
                    ("FontFamily", UINT),
                    ("FontWeight", UINT),
                    ("FaceName", WCHAR * LF_FACESIZE)
                ]
            PCONSOLE_FONT_INFOEX = POINTER(CONSOLE_FONT_INFOEX)

            GetCurrentConsoleFontEx = declare(kernel32.GetCurrentConsoleFontEx, BOOL, HANDLE, BOOL, PCONSOLE_FONT_INFOEX)

            SetCurrentConsoleFontEx = declare(kernel32.SetCurrentConsoleFontEx, BOOL, HANDLE, BOOL, PCONSOLE_FONT_INFOEX)
        #
        # Selection flags
        #

        CONSOLE_NO_SELECTION           = 0x0000
        CONSOLE_SELECTION_IN_PROGRESS  = 0x0001   # selection has begun
        CONSOLE_SELECTION_NOT_EMPTY    = 0x0002   # non-null select rectangle
        CONSOLE_MOUSE_SELECTION        = 0x0004   # selecting with mouse
        CONSOLE_MOUSE_DOWN             = 0x0008   # mouse is down

        class CONSOLE_SELECTION_INFO(CStructure):
            _fields_ = [
                ("dwFlags", DWORD),
                ("dwSelectionAnchor", COORD),
                ("srSelection", SMALL_RECT)
            ]
        PCONSOLE_SELECTION_INFO = POINTER(CONSOLE_SELECTION_INFO)

        GetConsoleSelectionInfo = declare(kernel32.GetConsoleSelectionInfo, BOOL, PCONSOLE_SELECTION_INFO)

        #
        # History flags
        #

        HISTORY_NO_DUP_FLAG = 0x1

        class CONSOLE_HISTORY_INFO(CStructure):
            _fields_ = [
                ("cbSize", UINT),
                ("HistoryBufferSize", UINT),
                ("NumberOfHistoryBuffers", UINT),
                ("dwFlags", DWORD)
            ]
        PCONSOLE_HISTORY_INFO = POINTER(CONSOLE_HISTORY_INFO)

        GetConsoleHistoryInfo = declare(kernel32.GetConsoleHistoryInfo, BOOL, PCONSOLE_HISTORY_INFO)
        SetConsoleHistoryInfo = declare(kernel32.SetConsoleHistoryInfo, BOOL, PCONSOLE_HISTORY_INFO)
        CONSOLE_FULLSCREEN = 1 # fullscreen console
        CONSOLE_FULLSCREEN_HARDWARE = 2 # console owns the hardware
        GetConsoleDisplayMode = declare(kernel32.GetConsoleDisplayMode, BOOL, LPDWORD)
        CONSOLE_FULLSCREEN_MODE = 1
        CONSOLE_WINDOWED_MODE = 2
        SetConsoleDisplayMode = declare(kernel32.SetConsoleDisplayMode, BOOL, HANDLE, DWORD, PCOORD)
        GetConsoleWindow = declare(kernel32.GetConsoleWindow, HWND, VOID)
    if cpreproc.getdef("_WINVER") >= 0x0501:
        AddConsoleAliasA = declare(kernel32.AddConsoleAliasA, BOOL, LPSTR, LPSTR, LPSTR)
        AddConsoleAliasW = declare(kernel32.AddConsoleAliasW, BOOL, LPWSTR, LPWSTR, LPWSTR)
        AddConsoleAlias = unicode(AddConsoleAliasW, AddConsoleAliasA)
        GetConsoleAliasA = declare(kernel32.GetConsoleAliasA, DWORD, LPSTR, LPSTR, DWORD, LPSTR)
        GetConsoleAliasW = declare(kernel32.GetConsoleAliasW, DWORD, LPWSTR, LPWSTR, DWORD, LPWSTR)
        GetConsoleAlias = unicode(GetConsoleAliasW, GetConsoleAliasA)
        GetConsoleAliasesLengthA = declare(kernel32.GetConsoleAliasesLengthA, DWORD, LPSTR)
        GetConsoleAliasesLengthW = declare(kernel32.GetConsoleAliasesLengthW, DWORD, LPWSTR)
        GetConsoleAliasesLength = unicode(GetConsoleAliasesLengthW, GetConsoleAliasesLengthA)
        GetConsoleAliasExesLengthA = declare(kernel32.GetConsoleAliasExesLengthA, DWORD, VOID)
        GetConsoleAliasExesLengthW = declare(kernel32.GetConsoleAliasExesLengthW, DWORD, VOID)
        GetConsoleAliasExesLength = unicode(GetConsoleAliasExesLengthW, GetConsoleAliasExesLengthA)
        GetConsoleAliasesA = declare(kernel32.GetConsoleAliasesA, DWORD, LPSTR, DWORD, LPSTR)
        GetConsoleAliasesW = declare(kernel32.GetConsoleAliasesW, DWORD, LPWSTR, DWORD, LPWSTR)
        GetConsoleAliases = unicode(GetConsoleAliasesW, GetConsoleAliasesA)
        GetConsoleAliasExesA = declare(kernel32.GetConsoleAliasExesA, DWORD, LPSTR, DWORD)
        GetConsoleAliasExesW = declare(kernel32.GetConsoleAliasExesW, DWORD, LPWSTR, DWORD)
        GetConsoleAliasExes = unicode(GetConsoleAliasExesW, GetConsoleAliasExesA)
    ExpungeConsoleCommandHistoryA = declare(kernel32.ExpungeConsoleCommandHistoryA, VOID, LPSTR)
    ExpungeConsoleCommandHistoryW = declare(kernel32.ExpungeConsoleCommandHistoryW, VOID, LPWSTR)
    ExpungeConsoleCommandHistory = unicode(ExpungeConsoleCommandHistoryW, ExpungeConsoleCommandHistoryA)
    SetConsoleNumberOfCommandsA = declare(kernel32.SetConsoleNumberOfCommandsA, BOOL, DWORD, LPSTR)
    SetConsoleNumberOfCommandsW = declare(kernel32.SetConsoleNumberOfCommandsW, BOOL, DWORD, LPWSTR)
    SetConsoleNumberOfCommands = unicode(SetConsoleNumberOfCommandsW, SetConsoleNumberOfCommandsA)
    GetConsoleCommandHistoryLengthA = declare(kernel32.GetConsoleCommandHistoryLengthA, DWORD, LPSTR)
    GetConsoleCommandHistoryLengthW = declare(kernel32.GetConsoleCommandHistoryLengthW, DWORD, LPWSTR)
    GetConsoleCommandHistoryLength = unicode(GetConsoleCommandHistoryLengthW, GetConsoleCommandHistoryLengthA)
    GetConsoleCommandHistoryA = declare(kernel32.GetConsoleCommandHistoryA, DWORD, LPSTR, DWORD, LPSTR)
    GetConsoleCommandHistoryW = declare(kernel32.GetConsoleCommandHistoryW, DWORD, LPWSTR, DWORD, LPWSTR)
    GetConsoleCommandHistory = unicode(GetConsoleCommandHistoryW, GetConsoleCommandHistoryA)
    if cpreproc.getdef("_WINVER") >= 0x0501:
        GetConsoleProcessList = declare(kernel32.GetConsoleProcessList, DWORD, LPDWORD, DWORD)

    # REGION ***
# _APISETCONSOLEL3_