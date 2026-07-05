from .interfacedef import *
from .errors import *

from typing import TypeVar, Self
from ..wtypesbase import *

import types

WT_CI = TypeVar('WT_CI', bound=COMInterface)

class IUnknown(COMInterface):
    _iid_ = IID('{00000000-0000-0000-C000-000000000046}')
    virtual_table = COMVirtualTable('IUnknown')
    
    @classmethod
    def Create(cls, clsid: CLSID, clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer['IUnknown'] = NULL) -> IPointer[Self]:
        if cpreproc.ifdef('DBGPLUS'):
            dbg_trace()
        pUnk = cls.NULL()
        hr = CoCreateInstance(clsid, pUnkOuter, clsctx, 
                              cls._iid_, byref(pUnk))
        if cpreproc.ifdef('DBGPLUS'):
            dbg_trace('Created instance')
        if FAILED(hr): raise COMError(hr)
        return pUnk
    
    if TYPE_CHECKING:
        @overload
        def QueryInterface(self, interface: COMInterface, ppvObject: IPointer[PVOID]) -> int: ...
        
        @overload
        def QueryInterface(self, iid: IID, ppvObject: IPointer[PVOID]) -> int: ...
    
    def QueryInterface(self, iid_or_interface,
                       ppvObject: IPointer[PVOID], **kwargs):
        if isinstance(iid_or_interface, IID):
            return self.virt_delegate(iid_or_interface.ref(), ppvObject)
        if issubclass(iid_or_interface, COMInterface):
            return self.virt_delegate(iid_or_interface._iid_.ref(), ppvObject)
        raise TypeError('Unknown type. Expected IID/Interface.')
    
    QueryInterface = virtual_table.com_function(REFIID, PVOID, intermediate_method=True)(QueryInterface)
    
    @virtual_table.function(ULONG)
    def AddRef(self): ...
    
    @virtual_table.function(ULONG)
    def Release(self): ...
    
    _fields_ = virtual_table.build()
    
IT = TypeVar('IT', bound=IUnknown)
IT2 = TypeVar('IT2', bound=IUnknown)

class _COM_REF_GUARD:
    itf: IT
    
    def __init__(self, itf: IT):
        self.itf = itf
    
    def __del__(self):
        self.itf.Release()

def com_interfacespec(spec: type[IT]):
    def _com_interfacespec(f: Callable):
        def _specified_method(self: IT, *args, **kwargs):
            qi_cache = getattr(self, 'qi_cache', None)
            if qi_cache is None:
                qi_cache = {}
                setattr(self, 'qi_cache', qi_cache)
            itf = qi_cache.get(spec)
            
            if itf is None:
                itf = spec.NULL()
                hr = self.QueryInterface(spec, byref(itf))
                if FAILED(hr): raise COMError(hr)
                itf = itf.contents
                qi_cache[spec] = itf
                guard = _COM_REF_GUARD(itf)
                setattr(itf, '_com_ref_guard', guard)
                
            return getattr(itf, f.__name__)(*args, **kwargs)
        return _specified_method
    return _com_interfacespec

class COMClass:
    _clsid_: ClassVar[CLSID]
    unk: IUnknown
    
    def __init__(self, clsctx: int = CLSCTX_INPROC_SERVER):
        self.unk = self.create_deref(IUnknown._iid_, clsctx, NULL)
    
    def QueryInterface(self, itf: type[IT], ppv: IDoublePtr[IT]) -> int:
        return self.unk.QueryInterface(itf, ppv)
    
    def __init_subclass__(cls):
        interfaces = list(set(COMClass.build_interfaces(cls)))
        for interface in interfaces:
            for k, v in interface.__dict__.items():
                if isinstance(v, types.FunctionType) and hasattr(v, 'proto'):
                    if v.__name__ != 'QueryInterface':
                        setattr(cls, k, com_interfacespec(interface)(v))
        
    @staticmethod
    def build_interfaces(cls) -> list[COMInterface]:
        if issubclass(cls, COMClass):
            result = []
        else:
            if not hasattr(cls, '_iid_'):
                return []
            
            result = [cls]
            
        for base in cls.__bases__:
            result.extend(COMClass.build_interfaces(base))
        
        return result
    
    @classmethod
    def clsid(cls) -> CLSID:
        return cls._clsid_
    
    @overload
    @classmethod
    def create(cls, iid: IID, clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer[IUnknown] = NULL) -> IPointer[IUnknown]: ...
    
    @overload
    @classmethod
    def create(cls, itf: type[IT], clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer[IUnknown] = NULL) -> IPointer[IT]: ...
    
    @classmethod
    def create(cls, var, clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer[IUnknown] = NULL) -> IPointer[IT]:
        is_interface = isinstance(var, type) and issubclass(var, COMInterface)
        iid: IID
        if isinstance(var, IID):
            iid = var
        elif is_interface:
            iid = var.iid()
        else:
            raise TypeError(type(var))
        pUnk = LPUNKNOWN()
        hr = CoCreateInstance(cls.clsid(), pUnkOuter, 
                              clsctx, iid, byref(pUnk))
        if FAILED(hr): raise COMError(hr)
        if is_interface:
            return i_cast(pUnk, var.PTR())
        return pUnk
    
    @overload
    @classmethod
    def create_deref(
        cls, iid: IID, clsctx: int = CLSCTX_INPROC_SERVER,
        pUnkOuter: IPointer[IUnknown] = NULL) -> IUnknown: ...
    
    @overload
    @classmethod
    def create_deref(
        cls, itf: type[IT], clsctx: int = CLSCTX_INPROC_SERVER,
        pUnkOuter: IPointer[IUnknown] = NULL) -> IT: ...
    
    @classmethod
    def create_deref(
        cls, var, clsctx: int = CLSCTX_INPROC_SERVER,
        pUnkOuter: IPointer[IUnknown] = NULL) -> IPointer[IT]:
        return cls.create(var, clsctx, pUnkOuter).contents
    
LPUNKNOWN = POINTER(IUnknown)

@ole_foreign(REFCLSID, LPUNKNOWN, DWORD, REFIID, PVOID, 
            intermediate_method=True)
def CoCreateInstance(clsid: CLSID, pUnkOuter: IPointer[IUnknown],
                    dwClsContext: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(clsid.ref(), pUnkOuter, dwClsContext, iid.ref(), ppv)

class IClassFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IClassFactory')
    _iid_ = IID('{00000001-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(LPUNKNOWN, REFIID, PVOID, intermediate_method=True)
    def CreateInstance(self, pUnkOuter: IPointer[IUnknown], iid: IID, ppvObject: IPointer[PVOID], **kwargs) -> int:
        """
        Creates an uninitialized object.
        """
        return self.virt_delegate(pUnkOuter, iid.ref(), ppvObject)
    
    @virtual_table.com_function(BOOL)
    def LockServer(self, fLock: bool) -> int:
        """
        Locks an object application open in memory. This enables instances to be created more quickly.
        """
    
    virtual_table.build()