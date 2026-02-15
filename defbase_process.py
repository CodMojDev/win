from .processthreadsapi import *
from .wow64apiset import *
from .handleapi import *
from .memoryapi import *
from .psapi import *
from .winnt import *

from typing import TypeVar, Self, ClassVar, TYPE_CHECKING
from ctypes import _SimpleCData as SimpleCData
from . import defbase as defb
from .defbase import *

class CSimpleDataInterProcess(SimpleCData):
    remote_address: WT_ADDRLIKE
    process: 'CProcess'
    
    @classmethod
    def initialize(cls, process: 'CProcess', remote_address: WT_ADDRLIKE) -> Self:
        csdip = cls()
        
        csdip.remote_address = remote_address
        csdip.process = process
        
        return csdip
    
    _type_ = 'i' # bypass the check
    
    @property
    def c_value(self):
        self.process.read(self.remote_address, byref(self), sizeof(self))
        return self.value
    
    @c_value.setter
    def c_value(self, value):
        self.value = value
        self.process.write(self.remote_address, byref(self), sizeof(self))

class InterProcessType:
    remote_address: WT_ADDRLIKE
    process: 'CProcess'
    
    @classmethod
    def initialize(cls, process: 'CProcess', remote_address: WT_ADDRLIKE) -> Self:
        ipt = cls()
        
        ipt.remote_address = remote_address
        ipt.process = process
        
        return ipt
    
    value: Any

class CCharPointerInterProcess(InterProcessType):    
    @property
    def value(self) -> bytes:
        buffer = create_string_buffer(1024)
        self.process.read(self.remote_address, byref(buffer), 1024)
        return buffer.value
    
    @value.setter
    def value(self, value: bytes):
        buffer = create_string_buffer(value)
        self.process.write(self.remote_address, byref(buffer), len(buffer))
        
class CWideCharPointerInterProcess(InterProcessType):
    @property
    def value(self) -> bytes:
        buffer = create_unicode_buffer(1024)
        self.process.read(self.remote_address, byref(buffer), 1024)
        return buffer.value
    
    @value.setter
    def value(self, value: bytes):
        buffer = create_unicode_buffer(value)
        self.process.write(self.remote_address, byref(buffer), len(buffer))
    
from struct import calcsize
    
class InterProcessTypes:
    class py_object(CSimpleDataInterProcess):
        _type_ = "O"
        def __repr__(self):
            try:
                return super().__repr__()
            except ValueError:
                return "%s(<NULL>)" % type(self).__name__

    class c_short(CSimpleDataInterProcess):
        _type_ = "h"

    class c_ushort(CSimpleDataInterProcess):
        _type_ = "H"

    class c_long(CSimpleDataInterProcess):
        _type_ = "l"

    class c_ulong(CSimpleDataInterProcess):
        _type_ = "L"

    if calcsize("i") == calcsize("l"):
        c_int = c_long
        c_uint = c_ulong
    else:
        class c_int(CSimpleDataInterProcess):
            _type_ = "i"

        class c_uint(CSimpleDataInterProcess):
            _type_ = "I"

    class c_float(CSimpleDataInterProcess):
        _type_ = "f"

    class c_double(CSimpleDataInterProcess):
        _type_ = "d"

    class c_longdouble(CSimpleDataInterProcess):
        _type_ = "g"
    if sizeof(c_longdouble) == sizeof(c_double):
        c_longdouble = c_double

    if calcsize("l") == calcsize("q"):
        c_longlong = c_long
        c_ulonglong = c_ulong
    else:
        class c_longlong(CSimpleDataInterProcess):
            _type_ = "q"

        class c_ulonglong(CSimpleDataInterProcess):
            _type_ = "Q"

    class c_ubyte(CSimpleDataInterProcess):
        _type_ = "B"
    c_ubyte.__ctype_le__ = c_ubyte.__ctype_be__ = c_ubyte

    class c_byte(CSimpleDataInterProcess):
        _type_ = "b"
    c_byte.__ctype_le__ = c_byte.__ctype_be__ = c_byte

    class c_char(CSimpleDataInterProcess):
        _type_ = "c"
    c_char.__ctype_le__ = c_char.__ctype_be__ = c_char

    c_char_p = CCharPointerInterProcess

    class c_void_p(CSimpleDataInterProcess):
        _type_ = "P"

    class c_bool(CSimpleDataInterProcess):
        _type_ = "?"

    c_wchar_p = CWideCharPointerInterProcess

    class c_wchar(CSimpleDataInterProcess):
        _type_ = "u"
        
def _contents_from_addr(T: type, process: 'CProcess', address: int):
    if issubclass(T, CStructure):
        return T.inter_process(process, address)
    elif issubclass(T, (CSimpleDataInterProcess, InterProcessType)):
        return T.initialize(process, address)
    elif issubclass(T, CPointer32):
        remote_address = InterProcessTypes.c_void_p.initialize(process, address).c_value
        return T(process, remote_address)
    raise ValueError('Incorrect type of pointer.')

def _make_offset(T: type, value: int, index: int) -> int:
    return value + (index * sizeof(T))
        
class IPointer32(IPointer[WT], IAliasableGenericWithPayload[WT]):
    remote_address: WT_ADDRLIKE
    process: 'CProcess'
    
    @interface_abstract_method
    def __init__(self, process: 'CProcess', remote_address: WT_ADDRLIKE = NULL): ...
    
    @classmethod
    def _get_alias_(cls, **kwargs):
        generic_alias = cls.get_genericalias()
        typ, = generic_alias.__args__
        return PTR32(typ)
        
# pure implementation
class CPointer32(c_int32):
    process: 'CProcess'
    _T: ClassVar[type]
    
    @property
    def contents(self):
        return _contents_from_addr(self._T, self.process, self.value)
        
    def __getitem__(self, index: int): 
        return _contents_from_addr(self._T, self.process, _make_offset(self._T, self.value, index))
    
    def __setitem__(self, index: int, value):
        if issubclass(self._T, CSimpleDataInterProcess):
            csdip: CSimpleDataInterProcess = self[index]
            csdip.c_value = value
        elif issubclass(self._T, InterProcessType):
            ipt: InterProcessType = self[index]
            ipt.value = value
        else:
            self.process.write(_make_offset(self._T, self.value, index), byref(value), sizeof(value))
        
def PTR32(typ: type[WT]) -> type[IPointer32[WT]]:
    return type(f'LP_{typ.__name__}', (CPointer32,), {'_T': typ})

POINTER32 = PTR32

def DOUBLE_PTR32(typ: type[WT]) -> type[IPointer32[IPointer32[WT]]]:
    return PTR32(PTR32(typ))

class CStructureInterProcess(CStructure): 
    remote_address: WT_ADDRLIKE
    process: 'CProcess'
    
    @classmethod
    def initialize(cls, process: 'CProcess', remote_address: WT_ADDRLIKE) -> Self:
        cip = cls()
        
        super(cls, cip).__setattr__('remote_address', remote_address)
        super(cls, cip).__setattr__('process', process)
        
        return cip
    
    def __getattribute__(self, name: str) -> Any:
        if super().__getattribute__('has_field')(name):
            self.process.read(self.remote_address, byref(self), sizeof(self))
            
            value = super().__getattribute__(name)
            if isinstance(value, CStructure):
                value = value.inter_process(super().__getattribute__('process'), 
                                            super().__getattribute__('remote_address')+super().__getattribute__('offset')(name))
            elif isinstance(value, CPointer32):
                value.process = self.process
            return value
        
        return super().__getattribute__(name)
    
    def __setattr__(self, name: str, value: Any) -> Any:
        field_type = super().__getattribute__('field_type')(name)
        
        if field_type is not None:
            remote_address = PtrUtil.get_address(super().__getattribute__('remote_address'))
            local_address = PtrUtil.get_address(byref(self))
            offset = super().__getattribute__('offset')(name)
            
            super().__setattr__(name, value)
            self.process.write(remote_address+offset, local_address+offset, sizeof(field_type))
            return
        
        super().__setattr__(name, value)

WT_CIP = TypeVar('WT_CIP', bound=CStructureInterProcess)

if TYPE_CHECKING:
    from .defbase_module import CModule

class CProcess:
    is_current: bool
    handle: int
    pid: int
    
    def __init__(self, pid: int = None):
        if pid is None:
            self.handle = GetCurrentProcess()
            handle = HANDLE()
            if not DuplicateHandle(self.handle, self.handle, self.handle,
                            byref(handle), 0, FALSE, DUPLICATE_SAME_ACCESS):
                raise OSError('Cannot duplicate handle for current process.')
            self.handle = handle.value
            
            self.pid = GetCurrentProcessId()
            self.is_current = True
            
            return
        
        self.handle = OpenProcess(PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION, 
                                  False, pid)
        self.is_current = False
        self.pid = pid
        
        if not self.handle:
            raise OSError(f'Cannot open {self} (for Read/Write).')
        
    def __str__(self) -> str:
        return f'Process PID {self.pid}'
    
    def __repr__(self) -> str:
        return f'<CProcess pid={self.pid} handle={self.handle}>'
        
    def structure(self, cip_cls: type[WT_CIP],
                  remote_address: WT_ADDRLIKE) -> WT_CIP:
        cip = cip_cls()
        self.read(remote_address, cip.ref(), cip.size())
        return cip
        
    def write(self, remote_address: WT_ADDRLIKE, 
              local_buffer: WT_ADDRLIKE, size: int) -> int:
        if not self.handle:
            raise OSError(f'Cannot write to memory of {self}.')
        
        written = SIZE_T()
        if not WriteProcessMemory(self.handle, remote_address,
                           local_buffer, size, byref(written)):
            raise OSError(f'Cannot write to memory of {self}.')
        
        return written.value
    
    def read(self, remote_address: WT_ADDRLIKE,
             local_buffer: WT_ADDRLIKE, size: int) -> int:
        if not self.handle:
            raise OSError(f'Cannot read memory of {self}.')
        
        read = SIZE_T()
        if not ReadProcessMemory(self.handle, remote_address,
                                 local_buffer, size, byref(read)):
            raise OSError(f'Cannot read memory of {self}.')
        
        return read.value
    
    def terminate(self, exit_code: int = 0): 
        if not self.handle:
            raise OSError(f'Cannot terminate {self}.')
        
        if not TerminateProcess(self.handle, exit_code):
            raise OSError(f'Cannot terminate {self}.')
        
    def enum_modules(self) -> list['CModule']: 
        defbase_module = getattr(defb._defb_state, '_defbase_module', None)
        
        if defbase_module is None:
            from . import defbase_module
            defb._defb_state._defbase_module = defbase_module
        
        modules: list['CModule'] = []
        
        hModules = (HMODULE * 1024)()
        cbNeeded = DWORD()
        
        if EnumProcessModules(self.handle, hModules, 1024, byref(cbNeeded)):
            for i in range(cbNeeded.value // sizeof(HMODULE)):
                module = defbase_module.CModule.from_handle(hModules[i])
                if not self.is_current:
                    module.process = self
                modules.append(module)

        return modules
    
    def close(self):
        if self.handle:
            CloseHandle(self.handle)
            self.handle = None
            
    @property
    def is_wow64(self) -> bool:
        is_wow64 = BOOL()
        if IsWow64Process(self.handle, byref(is_wow64)):
            return bool(is_wow64.value)
        return False
    
    def __del__(self):
        self.close()