from win.defbase_errordef import *
from win.minwindef import *
from win.com.objinterfacedef import *

kernel32 = get_win_library('kernel32.dll')

import socket
import os
import io

@kernel32.foreign(PVOID, HGLOBAL)
def GlobalLock(hMem: int) -> int: ...

@kernel32.foreign(SIZE_T, HGLOBAL)
def GlobalSize(hMem: int) -> int: ...

@kernel32.foreign(BOOL, HGLOBAL)
def GlobalUnlock(hMem: int) -> int: ...

@kernel32.foreign(HGLOBAL, UINT, SIZE_T)
def GlobalAlloc(uFlags: int, dwBytes: int) -> int: ...

@kernel32.foreign(HGLOBAL, HGLOBAL)
def GlobalFree(hMem: int) -> int: ...

class MemoryIO(io.IOBase):
    """
    Class, wrapping the direct memory operations with Python I/O-compatible class.
    """
    
    memory_position: int
    memory_address: int
    memory_size: int
    
    def __init__(self, address: WT_ADDRLIKE, size: int = -1):
        self.memory_address = PtrUtil.get_address(address)
        self.memory_position = 0
        self.memory_size = size
    
    def __iter__(self) -> int:
        if self.memory_size == -1:
            raise io.UnsupportedOperation('Tried to call __iter__ on continuous memory block I/O.')
        return self
    
    def __next__(self) -> bytes:
        if self.memory_size == -1:
            raise io.UnsupportedOperation('Tried to call __next__ on continuous memory block I/O.')
        data = self.read(1)
        if not data:
            raise StopIteration
        return data
    
    def tell(self) -> int:
        return self.memory_position
    
    def readable(self) -> bool:
        return True
    
    def writable(self):
        return True
    
    def seekable(self):
        return True
    
    def seek(self, offset: int, whence: int = os.SEEK_SET) -> int:
        if whence == os.SEEK_SET:
            self.memory_position = offset
        elif whence == os.SEEK_CUR:
            self.memory_position += offset
        elif whence == os.SEEK_END:
            if self.memory_size == -1:
                raise io.UnsupportedOperation('Tried to call seek(offset, os.SEEK_END) on continuous memory block I/O.')
            self.memory_position = self.memory_size - offset
        else:
            raise ValueError('Invalid whence value.')
        return self.memory_position
    
    def read(self, size: int = -1) -> bytes:
        if size == -1:
            if self.memory_size == -1:
                raise io.UnsupportedOperation('Tried to call read() on continuous memory block I/O.')
            
            size = self.memory_size - self.memory_position
            buffer = i_cast(self.memory_address + self.memory_position, PTR(CHAR * size)).contents.raw
            self.memory_position += size
            
            return buffer
        
        memory_position = self.memory_position + size
        if self.memory_size != -1:
            if memory_position >= self.memory_size:
                size_new = -self.memory_size + memory_position
                memory_position -= (size - size_new)
                size = size_new
        
        buffer = i_cast(self.memory_address + self.memory_position, PTR(CHAR * size)).contents.raw
        self.memory_position = memory_position
        return buffer
    
    def write(self, data: bytes):
        data_length = len(data)
        
        if self.memory_size != -1:
            if data_length >= self.memory_size:
                data_length = -self.memory_size + self.memory_position
            data = data[:data_length]
        
        buffer = create_string_buffer(data)
        memmove(self.memory_address + self.memory_position, buffer, data_length)
        self.memory_position += data_length
        
        return data_length
    
    def can_read(self) -> bool:
        """
        Can read now.
        """
        return self.memory_position < self.memory_size
    
    def read_int8(self) -> int:
        """
        Read the 8-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PINT8).contents.value
        self.memory_position += 1
        return data
    
    def read_uint8(self) -> int:
        """
        Read the unsigned 8-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PUINT8).contents.value
        self.memory_position += 1
        return data
    
    def read_int16(self) -> int:
        """
        Read the 16-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PINT16).contents.value
        self.memory_position += 2
        return data
    
    def read_uint16(self) -> int:
        """
        Read the unsigned 16-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PUINT16).contents.value
        self.memory_position += 2
        return data
    
    def read_int32(self) -> int:
        """
        Read the 32-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PINT32).contents.value
        self.memory_position += 4
        return data
    
    def read_uint32(self) -> int:
        """
        Read the unsigned 32-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PUINT32).contents.value
        self.memory_position += 4
        return data
    
    def read_int64(self) -> int:
        """
        Read the 64-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PINT64).contents.value
        self.memory_position += 8
        return data
    
    def read_uint64(self) -> int:
        """
        Read the unsigned 64-bit integer from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PUINT64).contents.value
        self.memory_position += 8
        return data
    
    def read_float(self) -> float:
        """
        Read the single float from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PFLOAT).contents.value
        self.memory_position += 4
        return data
    
    def read_double(self) -> float:
        """
        Read the double float from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PDOUBLE).contents.value
        self.memory_position += 8
        return data
    
    def read_structure(self, type: type[WT_SIMPLESTRUCTURE]) -> WT_SIMPLESTRUCTURE:
        """
        Read the structure from memory.
        """
        data = i_cast(self.memory_address + self.memory_position, PTR(type)).contents
        self.memory_position += sizeof(type)
        return data
    
    def read_bool(self) -> bool:
        """
        Read the boolean from memory.
        """
        return self.read_int8() != 0
    
    def read_bool32(self) -> bool:
        """
        Read the 32-bit boolean from memory.
        """
        return self.read_int32() != 0
    
    def write_int8(self, integer: int) -> int:
        """
        Write the 8-bit integer into memory.
        """
        return self.write(bytes(INT8(integer)))
    
    def write_uint8(self, integer: int) -> int:
        """
        Write the unsigned 8-bit integer into memory.
        """
        return self.write(bytes(UINT8(integer)))
    
    def write_int16(self, integer: int) -> int:
        """
        Write the 16-bit integer into memory.
        """
        return self.write(bytes(INT16(integer)))
    
    def write_uint16(self, integer: int) -> int:
        """
        Write the unsigned 16-bit integer into memory.
        """
        return self.write(bytes(UINT16(integer)))
    
    def write_int32(self, integer: int) -> int:
        """
        Write the 32-bit integer into memory.
        """
        return self.write(bytes(INT32(integer)))
    
    def write_uint32(self, integer: int) -> int:
        """
        Write the unsigned 32-bit integer into memory.
        """
        return self.write(bytes(UINT32(integer)))
    
    def write_int64(self, integer: int) -> int:
        """
        Write the 64-bit integer into memory.
        """
        return self.write(bytes(INT64(integer)))
    
    def write_uint64(self, integer: int) -> int:
        """
        Write the unsigned 64-bit integer into memory.
        """
        return self.write(bytes(UINT64(integer)))
    
    def write_float(self, value: float) -> int:
        """
        Write the single float value into memory.
        """
        return self.write(bytes(FLOAT(value)))
    
    def write_double(self, value: float) -> int:
        """
        Write the double float value into memory.
        """
        return self.write(bytes(DOUBLE(value)))
    
    def write_structure(self, structure: WT_SIMPLESTRUCTURE) -> int:
        """
        Write the structure into memory.
        """
        return self.write(bytes(structure))
    
    def write_bool(self, boolean: bool) -> int:
        """
        Write the boolean into memory.
        """
        return self.write(bytes(BYTE(boolean)))
    
    def write_bool32(self, boolean: bool) -> int:
        """
        Write the 32-bit boolean into memory.
        """
        return self.write(bytes(BOOL(boolean)))
    
GMEM_FIXED = 0x0000
GMEM_MOVEABLE = 0x0002
GMEM_ZEROINIT = 0x0040
GMEM_MODIFY = 0x0080
GMEM_DISCARDABLE = 0x0100
    
class GlobalIO(MemoryIO):
    """
    Class, wrapping the functionality of HGLOBAL, extending the MemoryIO.
    """
    
    handle: int
    
    def __init__(self, hMem: int):
        pMem = GlobalLock(hMem)
        if not pMem:
            raise WinException()
        self.handle = hMem
        super().__init__(pMem, GlobalSize(hMem))
        self._owning = False
        self._locked = True
    
    def owning(self, owning: bool = True):
        """
        Set the owner of this Global I/O, local or foreign.
        """
        self._owning = owning
        return self
    
    def unlock(self):
        """
        Unlock the Global I/O memory.
        """
        if self._locked:
            GlobalUnlock(self.handle)
            self._locked = False
    
    def close(self):
        if self._locked:
            GlobalUnlock(self.handle)
        if self._owning:
            GlobalFree(self.handle)
        super().close()
        
    @classmethod
    def allocate(cls, size: int, flags: int = GMEM_FIXED):
        """
        Allocate the global memory.
        """
        pIOMemory = GlobalAlloc(flags, size)
        if not pIOMemory: raise WinException()
        global_io = cls(pIOMemory).owning()
        return global_io
        
class StreamIO(io.IOBase):
    """
    Class, wrapping the functionality of IStream with Python I/O-compatible class.
    """
    
    stream: IStream
    
    def __init__(self, stream: IStream):
        self.stream = stream
        stream.AddRef()
        
    def seek(self, offset: int, whence: int = 0) -> int:
        new = ULARGE_INTEGER()
        if whence == os.SEEK_SET:
            hr = self.stream.Seek(offset, STREAM_SEEK_SET, byref(new))
        elif whence == os.SEEK_CUR:
            hr = self.stream.Seek(offset, STREAM_SEEK_CUR, byref(new))
        elif whence == os.SEEK_END:
            hr = self.stream.Seek(offset, STREAM_SEEK_END, byref(new))
        else:
            raise ValueError('Invalid whence value.')
        if FAILED(hr):
            raise COMError(hr)
        return new.value
    
    def flush(self):
        self.stream.Commit(STGC_DEFAULT)
    
    def close(self):
        self.stream.Release()
        super().close()
    
    def read(self, size: int = -1) -> bytes:
        if size == -1:
            stat = STATSTG()
            hr = self.stream.Stat(stat.ref(), STATFLAG_NONAME)
            if FAILED(hr): raise COMError(hr)
            size = stat.cbSize
        buffer = (CHAR * size)()
        read = ULONG()
        hr = self.stream.Read(buffer, size, byref(read))
        if FAILED(hr): raise COMError(hr)
        return i_cast(buffer, PTR(CHAR * read.value)).contents.raw
    
    def write(self, data: bytes) -> int:
        buffer = create_string_buffer(data)
        written = ULONG()
        hr = self.stream.Write(buffer, len(data), byref(written))
        if FAILED(hr): raise COMError(hr)
        return written.value
    
    def tell(self) -> int:
        position = ULARGE_INTEGER()
        hr = self.stream.Seek(0, STREAM_SEEK_CUR, byref(position))
        if FAILED(hr): raise COMError(hr)
        return position.value
    
    def readable(self) -> bool:
        return True
    
    def writable(self):
        return True
    
    def seekable(self):
        return True

class SocketIO(io.IOBase):
    sock: socket.socket
    
    def __init__(self, sock: socket.socket):
        self.sock = sock
        
    def readable(self) -> bool:
        return True
    
    def writable(self) -> bool:
        return True
    
    def seekable(self) -> bool:
        return False
    
    def write(self, data: bytes) -> int:
        return self.sock.send(data)
    
    def read(self, size: int = -1) -> bytes:
        if size == -1:
            data = b''
            received = self.sock.recv(2048)
            data += received
            while len(received) == 2048:
                received = self.sock.recv(2048)
                data += received
            return data
        else:
            return self.sock.recv(size)
    
class DelegatingStream(io.IOBase):
    incorporated_stream: io.IOBase
    
    def __init__(self, incorporated_stream: io.IOBase):
        self.incorporated_stream = incorporated_stream

    def read(self, size: int = -1) -> bytes:
        return self.incorporated_stream.read(size)

    def write(self, data: bytes) -> int:
        return self.incorporated_stream.write(data)
    
    def seekable(self) -> bool:
        return self.incorporated_stream.seekable()
    
    def writable(self) -> bool:
        return self.incorporated_stream.writable()
    
    def readable(self) -> bool:
        return self.incorporated_stream.readable()
    
    def seek(self, offset: int, whence: int = os.SEEK_SET) -> int:
        return self.incorporated_stream.seek(offset, whence)
    
    def tell(self) -> int:
        return self.incorporated_stream.tell()
    
class ToolStreamOverIO(DelegatingStream):
    def read_int8(self) -> int:
        """
        Read the 8-bit integer from stream.
        """
        return INT8.from_buffer_copy(self.read(1)).value
    
    def read_uint8(self) -> int:
        """
        Read the unsigned 8-bit integer from stream.
        """
        return UINT8.from_buffer_copy(self.read(1)).value
    
    def read_int16(self) -> int:
        """
        Read the 16-bit integer from stream.
        """
        return INT16.from_buffer_copy(self.read(2)).value
    
    def read_uint16(self) -> int:
        """
        Read the unsigned 16-bit integer from stream.
        """
        return UINT16.from_buffer_copy(self.read(2)).value
    
    def read_int32(self) -> int:
        """
        Read the 32-bit integer from stream.
        """
        return INT32.from_buffer_copy(self.read(4)).value
    
    def read_uint32(self) -> int:
        """
        Read the unsigned 32-bit integer from stream.
        """
        return UINT32.from_buffer_copy(self.read(4)).value
    
    def read_int64(self) -> int:
        """
        Read the 64-bit integer from stream.
        """
        return INT64.from_buffer_copy(self.read(8)).value
    
    def read_uint64(self) -> int:
        """
        Read the unsigned 64-bit integer from stream.
        """
        return UINT64.from_buffer_copy(self.read(8)).value
    
    def read_float(self) -> float:
        """
        Read the single float from stream.
        """
        return FLOAT.from_buffer_copy(self.read(4)).value
    
    def read_double(self) -> float:
        """
        Read the double float from stream.
        """
        return DOUBLE.from_buffer_copy(self.read(8)).value
    
    def read_structure(self, structure: type[WT_SIMPLESTRUCTURE]) -> WT_SIMPLESTRUCTURE:
        """
        Read the structure from stream.
        """
        return structure.from_buffer_copy(self.read(sizeof(structure)))
    
    def read_bool(self) -> bool:
        """
        Read the 8-bit boolean from stream.
        """
        return self.read(1)[0] != 0
    
    def read_bool32(self) -> bool:
        """
        Read the 32-bit boolean from stream.
        """
        return self.read_uint32() != 0
    
    def read_zstr(self, encoding: str='ascii') -> str:
        """
        Read the zero-terminated string from stream.
        """
        char = self.read(1)
        data = b''
        
        while char[0]:
            data += char
            char = self.read(1)
            
        return data.decode(encoding, errors='replace')
    
    def read_zwstr(self) -> str:
        """
        Read the zero-terminated wide string from stream.
        """
        char = self.read(2)
        data = b''
        
        while char[0] != 0 or char[1] != 0:
            data += char
            char = self.read(2)
            
        return data.decode('utf-16-le')
    
    def read_lstr(self, length_size: int, length_order: str = 'little', encoding: str = 'ascii') -> str:
        """
        Read the length-prefixed string from stream.
        """
        return self.read(int.from_bytes(self.read(length_size), length_order)).decode(encoding, errors='replace')
    
    def read_lwstr(self, length_size: int, length_order: str = 'little') -> str:
        """
        Read the length-prefixed string from stream.
        """
        return self.read(int.from_bytes(self.read(length_size<<1), length_order)).decode('utf-16-le', errors='replace')
    
    def read_str(self, length: int, encoding: str = 'ascii') -> str:
        """
        Read the string with explicit length from stream.
        """
        return self.read(length).decode(encoding, errors='replace')
    
    def read_wstr(self, length: int) -> str:
        """
        Read the wide string with explicit length from stream.
        """
        return self.read(length<<1).decode('utf-16-le', errors='replace')
    
    def read_zestr(self, length: int, encoding: str = 'ascii') -> str:
        """
        Read the zero-terminated string with explicit length from stream.
        """
        return self.read(length).split(b'\x00', 1)[0].decode(encoding, errors='replace')
    
    def read_zewstr(self, length: int) -> str:
        """
        Read the zero-terminated string with explicit length from stream.
        """
        return self.read(length<<1).split(b'\x00', 1)[0].decode('utf-16-le', errors='replace')
    
    def write_int8(self, integer: int) -> int:
        """
        Write the 8-bit integer into stream.
        """
        return self.write(bytes(INT8(integer)))
    
    def write_uint8(self, integer: int) -> int:
        """
        Write the unsigned 8-bit integer into stream.
        """
        return self.write(bytes(UINT8(integer)))
    
    def write_int16(self, integer: int) -> int:
        """
        Write the 16-bit integer into memory.
        """
        return self.write(bytes(INT16(integer)))
    
    def write_uint16(self, integer: int) -> int:
        """
        Write the unsigned 16-bit integer into stream.
        """
        return self.write(bytes(UINT16(integer)))
    
    def write_int32(self, integer: int) -> int:
        """
        Write the 32-bit integer into stream.
        """
        return self.write(bytes(INT32(integer)))
    
    def write_uint32(self, integer: int) -> int:
        """
        Write the unsigned 32-bit integer into stream.
        """
        return self.write(bytes(UINT32(integer)))
    
    def write_int64(self, integer: int) -> int:
        """
        Write the 64-bit integer into stream.
        """
        return self.write(bytes(INT64(integer)))
    
    def write_uint64(self, integer: int) -> int:
        """
        Write the unsigned 64-bit integer into stream.
        """
        return self.write(bytes(UINT64(integer)))
    
    def write_float(self, value: float) -> int:
        """
        Write the single float value into stream.
        """
        return self.write(bytes(FLOAT(value)))
    
    def write_double(self, value: float) -> int:
        """
        Write the double float value into stream.
        """
        return self.write(bytes(DOUBLE(value)))
    
    def write_structure(self, structure: WT_SIMPLESTRUCTURE) -> int:
        """
        Write the structure into stream.
        """
        return self.write(bytes(structure))
    
    def write_bool(self, boolean: bool) -> int:
        """
        Write the boolean into stream.
        """
        return self.write(bytes(BYTE(boolean)))
    
    def write_bool32(self, boolean: bool) -> int:
        """
        Write the 32-bit boolean into stream.
        """
        return self.write(bytes(BOOL(boolean)))
    
    def write_zstr(self, value: str, encoding: str = 'ascii') -> int:
        """
        Write the zero-terminated string into stream.
        """
        return self.write((value+'\x00').encode(encoding, errors='replace'))
    
    def write_zwstr(self, value: str) -> int:
        """
        Write the zero-terminated wide string into stream.
        """
        return self.write((value+'\x00').encode('utf-16-le', errors='replace'))
    
    def write_lstr(self, value: str, length_size: int, encoding: str = 'ascii', length_order: str = 'little') -> int:
        """
        Write the length-prefixed string into stream.
        """
        return self.write(len(value).to_bytes(length_size, length_order)) + self.write(value.encode(encoding, errors='replace'))
    
    def write_lwstr(self, value: str, length_size: int, length_order: str = 'little') -> int:
        """
        Write the length-prefixed wide string into stream.
        """
        return self.write(len(value).to_bytes(length_size, length_order)) + self.write(value.encode('utf-16-le', errors='replace'))
    
    def write_str(self, string: str, length: int, encoding: str = 'ascii') -> int:
        """
        Write the string with explicit length into stream.
        """
        string = string[0:length]
        while len(string) != length:
            string += '\x00'
        return self.write(string.encode(encoding, errors='replace'))
    
    def write_wstr(self, string: str, length: int) -> int:
        """
        Write the wide string with explicit length into stream.
        """
        string = string[0:length]
        while len(string) != length:
            string += '\x00'
        return self.write(string.encode('utf-16-le', errors='replace'))

# TODO: Bit stream write & additions
class ToolBitStream(DelegatingStream):
    bits_in_byte: int
    
    def __init__(self, incorporated_stream: io.IOBase):
        super().__init__(incorporated_stream)
        self.bits_in_byte = 8
    
    def read_bits(self, bits: int, order: str = 'little') -> bytes:
        if bits == 8 and self.bits_in_byte == 8:
            return self.incorporated_stream.read(1)
        else:
            data = b''
            while bits > 0:
                revert = 0
                if self.bits_in_byte == 0:
                    self.bits_in_byte = 8
                subtract = min(8, bits)
                if subtract != 8:
                    revert += 1
                byte = self.incorporated_stream.read(1)[0]
                byte = (byte >> (8 - self.bits_in_byte)) & ((1 << subtract) - 1)
                self.bits_in_byte -= subtract
                if order == 'big':
                    byte = (byte & 0xf0) >> 4 | (byte & 0x0f) << 4
                    byte = (byte & 0xcc) >> 2 | (byte & 0x33) << 2
                    byte = (byte & 0xaa) >> 1 | (byte & 0x55) << 1
                data += byte.to_bytes(1)
                
                if self.bits_in_byte < 0:
                    self.bits_in_byte = 8 - self.bits_in_byte
                    byte = self.incorporated_stream.read(1)[0] & ((1 << self.bits_in_byte) - 1)
                    revert += 1
                    data += byte.to_bytes(1)
                    
                bits -= 8
                self.seek(-revert, os.SEEK_CUR)
            return data
        
    def read_integer_bits(self, bits: int, order: str = 'little') -> int:
        return int.from_bytes(self.read_bits(bits), order)