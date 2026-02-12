from ..minwindef import *
from ..winnt import (
    MAKELANGID, LANG_NEUTRAL,
    SUBLANG_DEFAULT
)
from ..defbase import *

kernel32 = W_WinDLL('kernel32.dll')

@kernel32.foreign(HLOCAL, HLOCAL)
def LocalFree(hMem: int) -> int: ...

@kernel32.foreign(DWORD, DWORD, LPCVOID, DWORD, DWORD, LPWSTR, DWORD)
def FormatMessageW(dwFlags: int, lpSource: LPCVOID, dwMessageId: int,
                   dwLanguageId: int, lpBuffer: LPWSTR, nSize: int, *args) -> int: ...

FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x100
FORMAT_MESSAGE_IGNORE_INSERTS = 0x200
FORMAT_MESSAGE_FROM_SYSTEM = 0x1000

def GetErrorMessage(hr: int) -> str:
    flags: int = (FORMAT_MESSAGE_ALLOCATE_BUFFER | 
                  FORMAT_MESSAGE_FROM_SYSTEM | 
                  FORMAT_MESSAGE_IGNORE_INSERTS)
    message: LPCWSTR = i_cast(NULL, LPCWSTR)
    length: int = FormatMessageW(
        flags,
        NULL,
        hr,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        i_cast(byref(message), LPWSTR),
        0
    )
    
    if length > 0:
        result = message.value
        LocalFree(message)
        return result
    
    return None