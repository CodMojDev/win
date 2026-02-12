from .defbase_allocator import *
from .memoryapi import *

import struct

class CAssembly:
    allocator: IAllocator
    executable: WT_ADDRLIKE
    buffer: bytes
    
    def __init__(self, allocator: IAllocator):
        self.allocator = allocator
        self.executable = None
        
    def __del__(self):
        self.allocator.deallocate(self.executable)
        
    def parse_code(self, asm_code: str):
        code = b""
        for line in asm_code.split("\n"):
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            line = line.split(";")[0].strip()
            for byte in line.split():
                if len(byte) == 1:
                    byte = "0" + byte
                if len(byte) != 2:
                    raise ValueError(f"Invalid byte: {byte}")
                code += bytes.fromhex(byte)
        self.buffer = code
    
    def allocate(self):
        buffer_length = len(self.buffer)
        self.executable = self.allocator.allocate(buffer_length, flags=PAGE_EXECUTE_READWRITE)
        self.allocator.copy(self.executable, self.buffer, buffer_length)

    def cdecl(self, ret_type, *args):
        return CDECL(ret_type, *args)(self.executable)
    
    @staticmethod
    def address(addr):
        return " ".join([hex(i)[2:].zfill(2) for i in struct.pack("<Q", addr)])
    
    @staticmethod
    def binary_address(addr):
        return struct.pack("<Q", addr)
    
    @staticmethod
    def get_bit(value, bit):
        return (value >> bit) & 1

is_32 = cpreproc.ifdef("_WIN32")