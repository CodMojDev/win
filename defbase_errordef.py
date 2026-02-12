#
# defbase_errordef.py
#

from .winnt import LPTSTR, MAKELANGID, LANG_NEUTRAL, SUBLANG_DEFAULT
from .errhandlingapi import GetLastError
from .minwindef import *
from .defbase import *

from typing import *

class WinErrors:
    _kernel32 = W_WinDLL('kernel32.dll')
    _FormatMessage = unicode(
        declare(_kernel32.FormatMessageW, DWORD, DWORD, LPCVOID, DWORD, DWORD, LPWSTR, DWORD),
        declare(_kernel32.FormatMessageA, DWORD, DWORD, LPCVOID, DWORD, DWORD, LPSTR, DWORD)
    )
    _LocalFree = declare(_kernel32.LocalFree, HLOCAL, HLOCAL)
    _LANGUAGE = MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT)
    _FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x100
    _FORMAT_MESSAGE_IGNORE_INSERTS = 0x200
    _FORMAT_MESSAGE_FROM_SYSTEM = 0x1000
    _FLAGS = _FORMAT_MESSAGE_ALLOCATE_BUFFER | \
             _FORMAT_MESSAGE_FROM_SYSTEM | \
             _FORMAT_MESSAGE_IGNORE_INSERTS
    
    _cached: Dict[int, str]
    
    def __init__(self):
        self._cached = {}
    
    def __getitem__(self, error_id: int) -> str:
        if not isinstance(error_id, int):
            raise TypeError('Error ID type must be integer.')
        
        if error_id in self._cached:
            return self._cached[error_id]
        
        message_buffer = LPTSTR(NULL)
        size: int = self._FormatMessage(self._FLAGS, NULL, error_id, self._LANGUAGE,
                                        i_cast(byref(message_buffer), LPWSTR), 0)
        
        if size > 0:
            result = message_buffer.value
            self._cached[error_id] = result
            self._LocalFree(message_buffer)
            return result
        
        return ''
            
win_errors: WinErrors = WinErrors()

class WinException(OSError):
    def __init__(self, error_code: Optional[int] = None):
        if error_code is None:
            error_code = GetLastError()
        super().__init__(win_errors[error_code])