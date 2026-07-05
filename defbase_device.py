from .defbase_errordef import *
from .handleapi import *
from .ioapiset import *
from .synchapi import *
from .fileapi import *
from .winnt import *

INFINITE = 0xffffffff

class CDevice:
    overlapped: OVERLAPPED
    out: ICharArray
    handle: int
    event: int
    
    def __init__(self, name: str, attributes: SECURITY_ATTRIBUTES = NULL):
        if attributes is not NULL:
            attributes = attributes.ref()
            
        self.handle = CreateFileW(name, 0, FILE_SHARE_READ | FILE_SHARE_WRITE, attributes, OPEN_EXISTING, 0, NULL)
        if not self.handle or self.handle == INVALID_HANDLE_VALUE:
            raise WinException()
        
        self.event = CreateEventW(NULL, True, False, NULL)
        self.overlapped = OVERLAPPED(hEvent=self.event)
        self.out = create_string_buffer(8192)
    
    def write(self, ctl: int, data: bytes, size: int=-1):
        if size == -1: size = len(data)
        if not DeviceIoControl(self.handle, ctl, data, size, self.out, len(self.out), NULL, self.overlapped.ref()):
            raise WinException()
        
    def read(self, timeout: int = INFINITE) -> bytes:
        status = WaitForSingleObject(self.event, timeout)
        if status == WAIT_TIMEOUT:
            raise TimeoutError('Read from I/O Device timeout.')
        transferred = DWORD()
        if not GetOverlappedResult(self.handle, self.overlapped.ref(), byref(transferred), False):
            ResetEvent(self.event)
            raise WinException()
        ResetEvent(self.event)
        return self.out.raw[transferred.value:]
    
    def close(self):
        CloseHandle(self.handle)