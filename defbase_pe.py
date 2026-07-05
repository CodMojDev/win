from .minwindef import *
from .fileapi import *
from .winnt import *
from typing import *

from .abs.core.io import *

import io

class CPEFile:
    class CHeaders:
        f: 'CPEFile'
        
        def __init__(self, f: 'CPEFile'):
            self.f = f
            
        def dos(self) -> IMAGE_DOS_HEADER:
            return self.dos_ptr().contents
        
        def dos_ptr(self) -> IPointer[IMAGE_DOS_HEADER]:
            return i_cast(self.f.buffer, PIMAGE_DOS_HEADER)
            
        def nt64_ptr(self) -> IPointer[IMAGE_NT_HEADERS64]:
            return i_cast(self.f.address() + self.dos().e_lfanew, PIMAGE_NT_HEADERS64)
            
        def nt64(self) -> IMAGE_NT_HEADERS64:
            return self.nt64_ptr().contents
            
        def nt32_ptr(self) -> IPointer[IMAGE_NT_HEADERS32]:
            return i_cast(self.f.address() + self.dos().e_lfanew, PIMAGE_NT_HEADERS32)
        
        def nt32(self) -> IMAGE_NT_HEADERS32:
            return self.nt32_ptr().contents
        
        def nt(self) -> IMAGE_NT_HEADERS32 | IMAGE_NT_HEADERS64:
            return self.nt32() if self.f.bit32() else self.nt64()
        
        def nt_ptr(self) -> IPointer[IMAGE_NT_HEADERS32] | IPointer[IMAGE_NT_HEADERS64]:
            return self.nt32_ptr() if self.f.bit32() else self.nt64_ptr()
        
    headers: CHeaders
    fd: io.IOBase
    is_file: bool
    
    def __init__(self, fd: io.IOBase):
        self.headers = self.CHeaders(self)
        self.is_file = False
        self.fd = fd
    
    @classmethod
    def load(cls, file_name: str) -> 'CPEFile':
        instance = cls(open(file_name, 'rb+'))
        instance.is_file = True
        return instance
    
    def address(self):
        return PtrUtil.get_address(self.buffer)
        
    def init(self):
        if self.is_file:
            self.buffer = create_string_buffer(self.fd.read())
        elif isinstance(self.fd, MemoryIO):
            self.buffer = self.fd.memory_address
        self.buffer = i_cast(self.buffer, PBYTE)
        
    def bit32(self) -> bool:
        nt = self.headers.nt32()
        magic = nt.OptionalHeader.Magic
        if magic == IMAGE_NT_OPTIONAL_HDR32_MAGIC:
            return True
        elif magic == IMAGE_NT_OPTIONAL_HDR64_MAGIC:
            return False
        raise RuntimeError('Invalid PE File magic')
    
    def bit64(self) -> bool:
        return not self.bit32()