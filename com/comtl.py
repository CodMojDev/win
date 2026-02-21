#
# COM Templates Library
#

from .unknwn import *

class CComPtr(CStructure, Template[IT]):
    _cached_reinterpret_cast: reinterpret_cast
    _fields_ = [('_p', PVOID)]
    
    @property
    def p(self) -> IPointer[IT]:
        return self._cached_reinterpret_cast(self._p)
    
    @p.setter
    def p(self, value: IPointer[IT]):
        self._p = i_cast(value, PVOID)
    
    def __init__(self, ptr: IPointer[IT] = NULL):
        self.save_template()
        if ptr:
            ptr.contents.AddRef()
        self._cached_reinterpret_cast = reinterpret_cast[self.get_pointer_type()]
        self.p = ptr
        
    def __del__(self):
        if self.p:
            self.p.contents.Release()
            
    def Swap(self, other: 'CComPtr'):
        pTemp = self.p
        self.p = other.p
        other.p = pTemp
        
    def __static_cast__(self, typ: TUnion[Type[IPointer[IT]], 
                                         Type[IT]]) -> IPointer[IUnknown]:
        template_type = self.get_single_type()
        if (PtrUtil.is_pointer(typ) and
            issubclass(PtrUtil.get_type(typ), template_type)):
            return self._cached_reinterpret_cast(self.p)
        if issubclass(typ, template_type):
            return self._cached_reinterpret_cast(self.p).contents
        return NotImplemented
    
    def ref(self) -> IPointer[IT]:
        return i_cast(byref(self), PTR(self._cached_reinterpret_cast.typ))
    
    @property
    def contents(self) -> IT:
        ASSERT(self.p)
        return self.p.contents
    
    def __bool__(self) -> bool:
        return bool(self.p)
    
    def __eq__(self, other: TUnion[IPointer[IT], 'CComPtr']) -> bool:
        if (PtrUtil.is_pointer(other) and
            issubclass(PtrUtil.get_type(other), self.get_single_type())):
            return PtrArithmetic.equals(self.p, other)
        if issubclass(other, CComPtr):
            return PtrArithmetic.equals(self.p, other.p)
        return NotImplemented
    
    def __lt__(self, pT: IPointer[IT]) -> bool:
        if (PtrUtil.is_pointer(pT) and
            issubclass(PtrUtil.get_type(pT), self.get_single_type())):
            return PtrArithmetic.equals(self.p, pT)
        return NotImplemented
    
    def Release(self):
        """
        Release the interface and set to NULL
        """
        
        if self.p:
            self.p.contents.Release()
            self.p = self._cached_reinterpret_cast(NULL)
            
    def Attach(self, p2: IPointer[IT]):
        """
        Attach to an existing interface (does not AddRef)
        """
        
        if self.p:
            ref = self.p.contents.Release()
            # Attaching to the same object only works if duplicate references are being coalesced.  Otherwise
            # re-attaching will cause the pointer to be released and may cause a crash on a subsequent dereference.
            ASSERT(ref != 0 or not PtrArithmetic.equals(self.p, p2))
        self.p = p2
        
    def Detach(self) -> IPointer[IT]:
        """
        Detach the interface (does not Release)
        """
        
        pt = self.p
        self.p = self._cached_reinterpret_cast(NULL)
        return pt
    
    def CopyTo(self, ppT: IDoublePtr[IT]) -> int:
        ppT_is_null = PtrArithmetic.equals(ppT, NULL)
        ASSERT(not ppT_is_null)
        
        if ppT_is_null:
            return E_POINTER
        
        ppT.contents = self.p
        if self.p:
            self.p.contents.AddRef()
        
        return S_OK
    
    @TemplateFunction[IT2]
    def QueryInterface(self, pp: IDoublePtr[IT2], **kwargs) -> int:
        template: Template[IT2] = get_template()
        pp = i_cast(pp, template.get_pointer_type())
        ASSERT(not PtrArithmetic.equals(pp, NULL))
        template_type = template.get_single_type()
        return self.p.contents.QueryInterface(template_type._iid_, pp)
    
class COMModule(W_WinDLL):
    def __init__(self, name: str):
        super().__init__(name)
        
        @self.foreign(HRESULT, REFCLSID, REFIID, PVOID, intermediate_method=True)
        def DllGetClassObject(*args, **kwargs):
            args = filter_self(args, COMModule)
            clsid: CLSID; iid: IID
            clsid, iid, ppv = args
            return delegate(clsid.ref(), iid.ref(), ppv)
        
        self.DllGetClassObject = DllGetClassObject
        
        @self.foreign(HRESULT, intermediate_method=True)
        def DllCanUnloadNow(*args, **kwargs):
            return delegate()
        
        self.DllCanUnloadNow = DllCanUnloadNow
        
    @staticmethod
    def DllGetClassObject(clsid: CLSID, iid: IID, ppv: IPointer[PVOID]) -> int: 
        """
        Retrieves the class object from a DLL object handler or object application.

        OLE does not provide this function. DLLs that support the OLE Component Object Model (COM) must implement DllGetClassObject in OLE object handlers or DLL applications.
        """
    
    @staticmethod
    def DllCanUnloadNow() -> int: 
        """
        Determines whether the DLL that implements this function is in use. If not, the caller can unload the DLL from memory.

        OLE does not provide this function. DLLs that support the OLE Component Object Model (COM) should implement and export DllCanUnloadNow.
        """
        
class CUnknown(IUnknown):
    STA: type['CUnknown']
    MTA: type['CUnknownMTA']
    
    _refcnt: int
    
    def __init__(self):
        dbg_trace()
        
        # Virtual table Initialization
        self.initialize_vtable(self.virtual_table)
        
        # IUnknown
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.QueryInterface)
        self.implement(self.AddRef)
        self.implement(self.Release)
        
        # class fields
        self._refcnt = 0
        
    def AddRef_Impl(self) -> int:
        self._refcnt += 1
        dbg_trace(f'refcnt = {self._refcnt}')
        return self._refcnt
    
    def Release_Impl(self) -> int:
        self._refcnt -= 1
        if self._refcnt == 0:
            self.Release_Internal()
        
        dbg_trace(f'refcnt = {self._refcnt}')
        
        return self._refcnt
            
    def Release_Internal(self):
        dbg_trace()
        
from threading import Lock
        
class CUnknownMTA(IUnknown):
    _refcnt: int
    _lock: Lock
    
    def __init__(self):
        dbg_trace()
        
        # Virtual table Initialization
        self.initialize_vtable(self.virtual_table)
        
        # IUnknown
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.QueryInterface)
        self.implement(self.AddRef)
        self.implement(self.Release)
        
        # class fields
        self._lock = Lock()
        self._refcnt = 0
        
    def AddRef_Impl(self) -> int:
        with self._lock:
            self._refcnt += 1
            
        dbg_trace(f'refcnt = {self._refcnt}')
        
        return self._refcnt
    
    def Release_Impl(self) -> int:
        with self._lock:
            self._refcnt -= 1
            
        if self._refcnt == 0:
            self.Release_Internal()
        
        dbg_trace(f'refcnt = {self._refcnt}')
        
        return self._refcnt
            
    def Release_Internal(self):
        dbg_trace()
        
CUnknown.STA = CUnknown
CUnknown.MTA = CUnknownMTA
        
def QI_SetInterface(itf: COMInterface, ppvObject: IVoidPtr, virtual_table: COMVirtualTable) -> int:
    if not ppvObject: # unmanaged parameter needs check
        dbg_trace('E_POINTER')
        return E_POINTER

    lpVtbl = PVOID(getattr(itf, virtual_table.field_name))
    i_cast(ppvObject, PLPVOID).contents.value = PtrUtil.get_address(pointer(lpVtbl))
    
    dbg_trace('S_OK')
    return S_OK

class CComObject(CUnknown):
    _com_map_: ClassVar[list[tuple[COMInterface, COMVirtualTable]]]
    
    def __init__(self):
        dbg_trace()
        super().__init__()
        
        self.implement(self.QueryInterface)
    
    def QueryInterface_Impl(self, piid: IPointer[IID], ppv: IVoidPtr) -> int:
        iid = piid.contents
        if iid == IUnknown.iid() or iid == self.iid():
            dbg_trace(f'IUnknown | {self.__class__.__name__}')
            return QI_SetInterface(self, ppv, self.virtual_table)
        for ci, virtual_table in self._com_map_:
            if iid == ci.iid():
                dbg_trace(virtual_table.name)
                return QI_SetInterface(self, ppv, virtual_table)
        dbg_trace(f'No interface {iid}')
        i_cast(ppv, PLPVOID).contents.value = NULL
        return E_NOINTERFACE

def I_DllCanUnloadNow() -> int:
    return 0

def I_DllGetClassObject(): ...