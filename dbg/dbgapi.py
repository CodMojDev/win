from ..minwinbase import *
from ..sdkddkver import *

kernel32 = get_win_library('kernel32.dll')
_version = cpreproc.get_version()

if _version >= WIN32_WINNT_NT4:
    @kernel32.foreign(BOOL, VOID, result_function=bool)
    def IsDebuggerPresent() -> bool: ...

@kernel32.foreign(VOID)
def DebugBreak(): ...

@kernel32.foreign(VOID, LPCSTR)
def OutputDebugStringA(lpOutputString: WT_LPSTR): ...

@kernel32.foreign(VOID, LPCWSTR)
def OutputDebugStringW(lpOutputString: WT_LPWSTR): ...

OutputDebugString = unicode(OutputDebugStringW, OutputDebugStringA)

@kernel32.foreign(BOOL, DWORD, DWORD, DWORD,
                result_function=bool)
def ContinueDebugEvent(dwProcessId: int,
                    dwThreadId: int,
                    dwContinueStatus: int) -> bool: ...

@kernel32.foreign(BOOL, LPDEBUG_EVENT, DWORD,
                result_function=bool)
def WaitForDebugEvent(
    lpDebugEvent: IPointer[DEBUG_EVENT],
    dwMilliseconds: int) -> bool: ...

@kernel32.foreign(BOOL, DWORD, result_function=bool)
def DebugActiveProcess(dwProcessId: int) -> bool: ...

@kernel32.foreign(BOOL, DWORD, result_function=bool)
def DebugActiveProcessStop(dwProcessId: int) -> bool: ...

if _version >= WIN32_WINNT_WINXP:
    @kernel32.foreign(BOOL, HANDLE, PBOOL, result_function=bool)
    def CheckRemoteDebuggerPresent(
        hProcess: WT_HANDLE,
        pbDebuggerPresent: PBOOL) -> bool: ...

@kernel32.foreign(BOOL, LPDEBUG_EVENT, DWORD,
                result_function=bool)
def WaitForDebugEventEx(
    lpDebugEvent: IPointer[DEBUG_EVENT],
    dwMilliseconds: int) -> bool: ...