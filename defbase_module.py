from .libloaderapi import *
from .tlhelp32 import *
from .psapi import *

from .defbase_process import *

WT_FARPROC = TypeVar('WT_FARPROC', bound=FARPROC)

class CModule:
    handle: WT_ADDRLIKE
    process: CProcess
    local: 'CModule'
    _name: str
    
    @overload
    def __init__(self): ...
    
    @overload
    def __init__(self, name: str): ...
    
    @overload
    def __init__(self, process: CProcess, name: str): ...
    
    def __init__(self, var = None, name: str = None):
        if var is None: 
            self.process = None
            self.handle = None
            self._name = None
            self.local = None
            
            return
        
        if isinstance(var, str):
            self.handle = LoadLibraryEx(var, NULL, DONT_RESOLVE_DLL_REFERENCES)
            self.process = None
            self.local = None
            self._name = None
            
            if not self.handle:
                raise OSError(f'Cannot open module handle for "{var}"')
            
        elif isinstance(var, CProcess) and name is not None:
            self.process = var
            
            if not var.handle:
                self.handle = None
                self._name = None
                self.local = None
                
                raise OSError(f'Cannot open module handle for "{name}" in {var}.')
            
            for module in var.enum_modules():
                if name.lower() in module.name.lower():
                    self.local = CModule(module._name)
                    self.handle = module.handle
                    self._name = module._name
                    
                    break
            
        else:
            raise TypeError(f'{type(var).__name__}, {type(name).__name__}')
            
    @classmethod
    def from_handle(cls, handle: int) -> 'CModule':
        module = CModule()
        module.handle = handle
        return module
    
    def __repr__(self) -> str:
        if self.process is None:
            return f'<CModule handle={self.handle} name={self.name}>'
        # remote handle
        return f'<CModule handle={self.handle}, process.pid={self.process.pid}, name={self.name}>'
    
    @property
    def name(self) -> str:
        if self._name is None:
            szModuleName = (WCHAR * MAX_PATH)()
            process = self.process
            
            if process is None:
                if GetModuleFileName(self.handle, szModuleName, MAX_PATH):
                    self._name = szModuleName.value
                else:
                    raise OSError('Cannot get module file name.')
            else: # remote handle
                if GetModuleFileNameEx(self.process.handle, self.handle, szModuleName, MAX_PATH):
                    self._name = szModuleName.value
                else:
                    raise OSError('Cannot get module file name.')
                
        return self._name
            
    def close(self):
        process_is_not_None = self.process is not None
        
        if process_is_not_None: # remote handle
            handle_to_free = self.local.handle
        else:
            handle_to_free = self.handle
            
        if handle_to_free:
            FreeLibrary(handle_to_free)
            self.handle = None
            self.local = None
            
    def procedure_address(self, name: str) -> int:
        address: FARPROC
        
        if self.process is not None: # remote handle
            address = GetProcAddress(self.local.handle, name)
            address = PtrUtil.get_address(address)
            address = (address - self.local.handle) + self.handle
        else:
            address = GetProcAddress(self.handle, name)
            
        return PtrUtil.get_address(address)
    
    def procedure(self, name: str, typ: type[WT_FARPROC]) -> WT_FARPROC:
        return i_cast2(self.procedure_address(name), typ)
    
    @property
    def size(self) -> int:
        if self.process is not None:
            modInfo = MODULEINFO()
            if not GetModuleInformation(self.process.handle, self.handle, modInfo.ref(), modInfo.size()):
                return -1
            return modInfo.SizeOfImage
        modInfo = MODULEINFO()
        if not GetModuleInformation(GetCurrentProcess(), self.handle, modInfo.ref(), modInfo.size()):
            return -1
        return modInfo.SizeOfImage
            
    def __del__(self):
        self.close()