from ..minwindef import *
from ..winnt import (
    MAKELANGID, LANG_NEUTRAL,
    SUBLANG_DEFAULT
)
from ..defbase import *

from ..defbase_errordef import *

kernel32 = W_WinDLL('kernel32.dll')

@kernel32.foreign(HLOCAL, HLOCAL)
def LocalFree(hMem: int) -> int: ...

@kernel32.foreign(DWORD, DWORD, LPCVOID, DWORD, DWORD, LPWSTR, DWORD)
def FormatMessageW(dwFlags: int, lpSource: LPCVOID, dwMessageId: int,
                   dwLanguageId: int, lpBuffer: LPWSTR, nSize: int, *args) -> int: ...

FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x100
FORMAT_MESSAGE_IGNORE_INSERTS = 0x200
FORMAT_MESSAGE_FROM_SYSTEM = 0x1000

class IErrorInfoProvider:
    _win_errors_list_: list[WinErrors] = []
    
    @interface_abstract_method
    def get_win_errors_list(self) -> list[WinErrors]: ...

_ErrorInfoProviders = []

def _RegisterErrorInfoProvider(provider):
    global _ErrorInfoProviders
    _ErrorInfoProviders.append(provider)

def GetErrorMessage(hr: int) -> str:
    for provider in _ErrorInfoProviders:
        win_errors_list = provider._win_errors_list_
        
        if win_errors_list is None:
            win_errors_list = provider.get_win_errors_list()
            
        for win_errors in win_errors_list:
            error = win_errors[hr]
            if error:
                return error
    
    return format_hex(ULONG(hr).value, sizeof(HRESULT))