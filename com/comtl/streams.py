from .object import *
from .baseface import *
from ..storagedef import *

import os
import io

WIN32_EPOCH_NULL_TIMESTAMP = 116444736000000000
STG_E_INVALIDFUNCTION = 0x80030001
STG_E_INVALIDPOINTER = 0x80030009
STG_E_READFAULT = 0x8003001E

class FileStream(CComObject, IStream, ILockBytes):
    ILockBytes_virtual_table = COMVirtualTable.from_ancestor(ILockBytes).with_fieldname('ILockBytes_vtable')
    _com_map_ = [(ILockBytes, ILockBytes_virtual_table)]
    _fields_ = ILockBytes_virtual_table.build()
    
    def __init__(self, file_path: str):
        super().__init__()
        
        if not os.path.exists(file_path):
            open(file_path, 'wb').close()
        
        self.initialize_vtable(self.ILockBytes_virtual_table)
        self.implement_interface(ISequentialStream)
        self.implement_interface(IStream)
        self.set_vtable_on_ctx(self.ILockBytes_virtual_table)
        self.implement_interface(ILockBytes)
        
        if file_path is not None:
            self.file = open(file_path, 'r+b')
    
    def Cleanup(self):
        self.file.close()
        
    def UnlockRegion_Impl(self, libOffset: int, cb: int, dwLockType: int) -> int:
        return STG_E_INVALIDFUNCTION
    
    def LockRegion_Impl(self, libOffset: int, cb: int, dwLockType: int) -> int:
        return STG_E_INVALIDFUNCTION
    
    def Flush_Impl(self) -> int:
        self.file.flush()
        return S_OK
    
    def Seek_Impl(self, dlibMove: int, dwOrigin: int, pLibNewPosition: IPointer[ULARGE_INTEGER]) -> int:
        if dwOrigin == STREAM_SEEK_SET:
            self.file.seek(dlibMove, os.SEEK_SET)
        elif dwOrigin == STREAM_SEEK_CUR:
            self.file.seek(dlibMove, os.SEEK_CUR)
        elif dwOrigin == STREAM_SEEK_END:
            self.file.seek(dlibMove, os.SEEK_END)
        else:
            return E_INVALIDARG
        if pLibNewPosition:
            pLibNewPosition.contents.value = self.file.tell()
        return S_OK
    
    def Stat_Impl(self, pstatstg: IPointer[STATSTG], grfStatFlag: int):
        if not pstatstg:
            return STG_E_INVALIDPOINTER
            
        stat = pstatstg.contents
        
        if (grfStatFlag & STATFLAG_NONAME) == 0:
            stat.pwcsName = i_cast(TlAllocateString(self.file.name), LPWSTR)
        
        stat.type = STGTY_STREAM
        stat.grfLocksSupported = 0
        stat.clsid = CLSID_NULL
        
        position = self.file.tell()
        self.file.seek(0, os.SEEK_END)
        stat.cbSize = self.file.tell()
        self.file.seek(position, os.SEEK_SET)
        
        stat.grfStateBits = 0
        
        if self.file.readable() and self.file.writable():
            stat.grfMode = STGM_READWRITE
        else:
            stat.grfMode = STGM_WRITE
        
        mtime = int(os.path.getmtime(self.file) * 10000000) + WIN32_EPOCH_NULL_TIMESTAMP
        ctime = int(os.path.getctime(self.file) * 10000000) + WIN32_EPOCH_NULL_TIMESTAMP
        atime = int(os.path.getatime(self.file) * 10000000) + WIN32_EPOCH_NULL_TIMESTAMP
        
        stat.mtime.dwLowDateTime = mtime & 0xFFFFFFFF
        stat.mtime.dwHighDateTime = mtime >> 32
        
        stat.ctime.dwLowDateTime = ctime & 0xFFFFFFFF
        stat.ctime.dwHighDateTime = ctime >> 32
        
        stat.atime.dwLowDateTime = atime & 0xFFFFFFFF
        stat.atime.dwHighDateTime = atime >> 32
        
        return S_OK
    
    def Read_Impl(self, pv: int, cb: int, pcbRead: IPointer[ULONG]) -> int:
        if not pv:
            return STG_E_INVALIDPOINTER
        buffer = self.file.read(cb)
        length = len(buffer)
        memmove(pv, buffer, length)
        if pcbRead:
            pcbRead.contents.value = length
        return S_OK
    
    def Write_Impl(self, pv: int, cb:  int, pcbWritten: IPointer[ULONG]) -> int:
        if not pv:
            return STG_E_INVALIDPOINTER
        buffer = create_string_buffer(cb)
        memmove(buffer, pv, cb)
        self.file.write(buffer.raw)
        if pcbWritten:
            pcbWritten.contents.value = cb
        return S_OK
    
    def Clone_Impl(self, ppstm: IDoublePtr[IStream]) -> int:
        if not ppstm:
            return STG_E_INVALIDPOINTER
        new = FileStream()
        new.file = self.file
        TlWritePointerToPpv(ppstm, new.ref())
        return S_OK
    
    def Revert_Impl(self):
        return S_OK
    
    def SetSize_Impl(self, libNewSize: int) -> int:
        return STG_E_INVALIDFUNCTION
    
    def ReadAt_Impl(self, ulOffset: int, pv: int, cb: int, pcbRead: IPointer[ULONG]) -> int:
        position = self.file.tell()
        self.file.seek(ulOffset)
        buffer = self.file.read(cb)
        self.file.seek(position)
        length = len(buffer)
        memmove(pv, buffer, length)
        if pcbRead:
            pcbRead.contents.value = length
        if length != cb:
            return STG_E_READFAULT
        
        return S_OK
    
    def WriteAt_Impl(self, ulOffset: int, pv: int, cb: int, pcbWritten: IPointer[ULONG]) -> int:
        position = self.file.tell()
        self.file.seek(ulOffset)
        buffer = create_string_buffer(cb)
        memmove(buffer, pv, cb)
        self.file.write(buffer)
        self.file.seek(position)
        if pcbWritten:
            pcbWritten.contents.value = cb
        return S_OK