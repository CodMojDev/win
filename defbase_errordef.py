#
# defbase_errordef.py
#

from .winnt import LPTSTR, MAKELANGID, LANG_NEUTRAL, SUBLANG_DEFAULT
from .errhandlingapi import GetLastError
from .minwindef import *
from .winerror import *
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
    _FORMAT_MESSAGE_FROM_HMODULE = 0x800
    _FORMAT_MESSAGE_FROM_SYSTEM = 0x1000
    
    _cached: Dict[int, str]
    _handle: int
    
    def __init__(self, handle: Optional[int] = NULL):
        self._cached = {}
        self._flags = self._FORMAT_MESSAGE_ALLOCATE_BUFFER | self._FORMAT_MESSAGE_IGNORE_INSERTS
        self._handle = handle
        if handle is NULL:
            self._flags |= self._FORMAT_MESSAGE_FROM_SYSTEM
        else:
            self._flags |= self._FORMAT_MESSAGE_FROM_HMODULE
    
    def __getitem__(self, error_id: int) -> str:
        if not isinstance(error_id, int):
            raise TypeError('Error ID type must be integer.')
        
        if error_id in self._cached:
            return self._cached[error_id]
        
        message_buffer = LPTSTR(NULL)
        size: int = self._FormatMessage(self._flags, self._handle, error_id, self._LANGUAGE,
                                        i_cast(byref(message_buffer), LPWSTR), 0)
        
        if size > 0:
            result = message_buffer.value.rstrip('\r\n')
            self._cached[error_id] = result
            self._LocalFree(message_buffer)
            return result
        
        return ''
            
win_errors: WinErrors = WinErrors()

class WinException(OSError):
    _win_errors_ = win_errors
    error_code: int
    
    def __init__(self, error_code: Optional[int] = None):
        if error_code is None:
            error_code = GetLastError()
        self.error_code = error_code
        error = self._win_errors_[error_code]
        if error == '':
            super().__init__(format_hex(error_code & 0xffffffff, 8))
        else:
            super().__init__(error)