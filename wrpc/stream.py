from win import cpreproc

import typing
import io

if typing.TYPE_CHECKING:
    from .protocol import IWRPCProtocol

class Stream(io.BytesIO):
    protocol: 'IWRPCProtocol'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol = None
    
    def read_byte(self) -> int:
        return self.read(1)[0]
    
    def read_word(self) -> int:
        buffer = self.read(2)
        return buffer[1] << 8 | buffer[0]
    
    def read_dword(self) -> int:
        buffer = self.read(4)
        return ((buffer[3] << 8 | buffer[2]) << 8 | buffer[1]) << 8 | buffer[0]
    
    def read_qword(self) -> int:
        buffer = self.read(8)
        return (((((((buffer[7] 
                     << 8 | buffer[6]) 
                    << 8 | buffer[5])
                   << 8 | buffer[4]) 
                  << 8 | buffer[3]) 
                 << 8 | buffer[2]) 
                << 8 | buffer[1]) 
                << 8 | buffer[0])
    
    def read_pvoid(self) -> int:
        if cpreproc.ifdef('_WIN32'):
            return self.read_dword()
        return self.read_qword()