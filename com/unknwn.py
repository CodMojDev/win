from .interfacedef import *
from .errors import *

from typing import TypeVar, Self
from ..wtypesbase import *

WT_CI = TypeVar('WT_CI', bound=COMInterface)

class IUnknown(COMInterface):
    class VB(COMInterface):
        _iid_ = IID('{00000000-0000-0000-C000-000000000046}')
        virtual_table = COMVirtualTable('IUnknown')
        
        @classmethod
        def Create(cls, clsid: CLSID, clsctx: int = CLSCTX_INPROC_SERVER,
                   unkOuter: 'IUnknown.VB' = NULL) -> 'IUnknown.VB':
            pUnk = cls.NULL()
            hr = CoCreateInstance(clsid, unkOuter.ref() if unkOuter else NULL,
                                  clsctx, cls._iid_, byref(pUnk))
            if FAILED(hr): raise COMError(hr)
            return i_cast(pUnk, cls.PTR()).contents
        
        @virtual_table.com_function_vbstyle_nonvariant(REFIID, intermediate_method=True,
                                            retval_index=1, retval_type=PVOID)
        def QueryInterface(self, itf: type[WT_CI], **kwargs) -> WT_CI:
            pv = self.virt_delegate(itf._iid_.ref())
            return i_cast2(pv, itf.PTR()).contents
        
        @virtual_table.function(ULONG)
        def AddRef(self): ...
        
        @virtual_table.function(ULONG)
        def Release(self): ...
        
        _fields_ = virtual_table.build()
        
    _iid_ = IID('{00000000-0000-0000-C000-000000000046}')
    virtual_table = COMVirtualTable('IUnknown')
    
    @classmethod
    def Create(cls, clsid: CLSID, clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer['IUnknown'] = NULL) -> IPointer[Self]:
        pUnk = cls.NULL()
        hr = CoCreateInstance(clsid, pUnkOuter, clsctx, 
                              cls._iid_, byref(pUnk))
        if FAILED(hr): raise COMError(hr)
        return pUnk
    
    @overload
    def QueryInterface(self, interface: COMInterface, ppvObject: IPointer[PVOID]) -> int: ...
    
    @overload
    def QueryInterface(self, iid: IID, ppvObject: IPointer[PVOID]) -> int: ...
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True)
    def QueryInterface(self, iid_or_interface,
                       ppvObject: IPointer[PVOID], **kwargs):
        if isinstance(iid_or_interface, IID):
            return self.virt_delegate(iid_or_interface.ref(), ppvObject)
        if issubclass(iid_or_interface, COMInterface):
            return self.virt_delegate(iid_or_interface._iid_.ref(), ppvObject)
        raise TypeError('Unknown type. Expected IID/Interface.')
    
    @virtual_table.function(ULONG)
    def AddRef(self): ...
    
    @virtual_table.function(ULONG)
    def Release(self): ...
    
    _fields_ = virtual_table.build()
    
IT = TypeVar('IT', bound=IUnknown)
IT2 = TypeVar('IT2', bound=IUnknown)

class COMClass:
    _clsid_: ClassVar[CLSID]
    
    @classmethod
    def clsid(cls) -> CLSID:
        return cls._clsid_
    
    @overload
    @classmethod
    def create_deref(cls, iid: IID, clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer[IUnknown] = NULL) -> IPointer[IUnknown]: ...
    
    @overload
    @classmethod
    def create_deref(cls, itf: type[IT], clsctx: int = CLSCTX_INPROC_SERVER,
                 pUnkOuter: IPointer[IUnknown] = NULL) -> IT: ...
    
    @classmethod
    def create_deref(cls, var, clsctx: int = CLSCTX_INPROC_SERVER,
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
            return i_cast(pUnk, var.PTR()).contents
        return pUnk.contents
    
LPUNKNOWN = POINTER(IUnknown)

@ole_foreign(REFCLSID, LPUNKNOWN, DWORD, REFIID, PVOID, 
            intermediate_method=True)
def CoCreateInstance(clsid: CLSID, pUnkOuter: IPointer[IUnknown],
                    dwClsContext: int, iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    return delegate(clsid.ref(), pUnkOuter, dwClsContext, iid.ref(), ppv)

class IClassFactory(IUnknown):
    class VB(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IClassFactory')
    
        @virtual_table.com_function_vbstyle_nonvariant(LPUNKNOWN, REFIID, intermediate_method=True, 
                                            retval_index=2, retval_type=PVOID)
        def CreateInstance(self, unkOuter: IUnknown, itf: type[WT_CI], **kwargs) -> WT_CI:
            """
            Creates an uninitialized object.
            """
            pv = self.virt_delegate(unkOuter.ref() if unkOuter else NULL, itf._iid_.ref())
            return i_cast2(pv, itf.PTR()).contents
        
        @virtual_table.com_function_vbstyle_nonvariant(BOOL)
        def LockServer(self, fLock: bool):
            """
            Locks an object application open in memory. This enables instances to be created more quickly.
            """
        
        virtual_table.build()
        
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IClassFactory')
    
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