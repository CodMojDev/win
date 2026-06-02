from win.namedpipeapi import *
from win.handleapi import *
from ..core.handle import *
from win.fileapi import *

class NamedPipe(Handle):
    _connected: bool
    
    @classmethod
    def create(cls, name: str, access: int = PIPE_ACCESS_DUPLEX,
               mode: int = PIPE_TYPE_BYTE, max_instances: int = PIPE_UNLIMITED_INSTANCES,
               out_buffer_size: int = 0, in_buffer_size: int = 0, 
               security_attributes: SECURITY_ATTRIBUTES = NULL) -> 'NamedPipe':
        pipe = cls()
        pipe._connected = False
        
        if not name.startswith('\\'):
            name = name + '\\\\.\\pipe'

        if security_attributes is not NULL:
            security_attributes = security_attributes.ref()
            
        pipe.value = CreateNamedPipeW(
            name, access, mode, max_instances, 
            out_buffer_size, in_buffer_size, 0, 
            security_attributes)
        if not pipe.value:
            raise WinException()
        
        return pipe
    
    def close(self):
        if self._connected:
            self.disconnect()
        CloseHandle(self)
        self._closed = True
            
    def connect(self): 
        if not ConnectNamedPipe(self, NULL):
            raise WinException()
        self._connected = True
        
    def disconnect(self):
        self._connected = False
        if not DisconnectNamedPipe(self):
            raise WinException()
        
    def read(self, size: int) -> bytes:
        buffer = create_string_buffer(size)
        nBytesRead = DWORD()
        if not ReadFile(self, buffer, size, byref(nBytesRead), NULL):
            raise WinException()
        buffer = i_cast(buffer, PTR(CHAR * nBytesRead.value)).contents
        return buffer.raw
    
    def write(self, buffer: bytes) -> int:
        buf = create_string_buffer(buffer)
        nBytesWritten = DWORD()
        if not WriteFile(self, buf, len(buf), byref(nBytesWritten), NULL):
            raise WinException()
        return nBytesWritten.value
    
    @classmethod
    def open(cls, name: str, access: int = GENERIC_READ | GENERIC_WRITE,
             share: int = 0, security_attributes: SECURITY_ATTRIBUTES = NULL,
             creation_disposition: int = OPEN_EXISTING, attributes: int = FILE_ATTRIBUTE_NORMAL,
             template_file: int | HANDLE = NULL) -> 'Pipe':
        if not name.startswith('\\'):
            name = name + '\\\\.\\pipe'
        
        if security_attributes is not NULL:
            security_attributes = security_attributes.ref()
        
        hPipe = CreateFileW(name, access, share, security_attributes, creation_disposition, attributes, template_file)
        
        if not hPipe:
            raise WinException()
        
        pipe: Pipe = cls.__new__()
        pipe.value = hPipe
        
        return pipe
    
class Pipe(Handle):
    r: int
    w: int
    
    @classmethod
    def create(cls, security_attributes: SECURITY_ATTRIBUTES = NULL, size: int = 0) -> 'Pipe':
        pipe = cls()

        if security_attributes is not NULL:
            security_attributes = security_attributes.ref()
        
        r = HANDLE()
        w = HANDLE()
        
        if not CreatePipe(byref(r), byref(w), security_attributes, size):
            raise WinException()
        
        pipe.r = r.value
        pipe.w = w.value
    
        return pipe
    
    def close(self):
        CloseHandle(self.r)
        CloseHandle(self.w)
        self._closed = True
        
    def read(self, size: int) -> bytes:
        buffer = create_string_buffer(size)
        nBytesRead = DWORD()
        if not ReadFile(self.r, buffer, size, byref(nBytesRead), NULL):
            raise WinException()
        buffer = i_cast(buffer, PTR(CHAR * nBytesRead.value)).contents
        return buffer.raw
    
    def write(self, buffer: bytes) -> int:
        buf = create_string_buffer(buffer)
        nBytesWritten = DWORD()
        if not WriteFile(self.w, buf, len(buf), byref(nBytesWritten), NULL):
            raise WinException()
        return nBytesWritten.value