#
# COM Templates Library
#

from ..wet.trace import _WET_GLOBAL_STATE
from ..wet.trace import *

from .unknwn import *

provider = WET_PROVIDER('COM-TL')

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
        
from .. import _defbase_ctypinit as _defb_ci
from threading import Lock
    
import gc
        
class CUnknown(IUnknown):
    _mta_: ClassVar[bool] = False
    _refcnt: int
    _lock: Lock
    
    _trace_id_next_: ClassVar[int] = 0
    _trace_id: int
    
    _unk_outer: Optional[IUnknown]
    
    def __init__(self, *args):
        if len(args) != 0 and isinstance(args[0], IUnknown):
            self._unk_outer = args[0]
            self._unk_outer.AddRef()
        else:
            self._unk_outer = None
        
        if self._mta_:
            self._lock = Lock()
        
        self._trace_id = CUnknown._trace_id_next_
        CUnknown._trace_id_next_ += 1
        
        dbg_trace(provider, f'TraceID {self._trace_id}')
        
        # Virtual table Initialization
        self.initialize_vtable(self.virtual_table)
        
        # IUnknown
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.AddRef)
        self.implement(self.Release)
        
        # class fields
        self._refcnt = 1
        
    def AddRef_Impl(self) -> int:
        if self._unk_outer:
            dbg_trace(provider, f'TraceID {self._trace_id} AddRef forwarded to outer IUnknown')
            return self._unk_outer.AddRef()
        
        if self._mta_:
            with self._lock:
                self._refcnt += 1
        else:
            self._refcnt += 1
            
        dbg_trace(provider, f'TraceID {self._trace_id} refcnt = {self._refcnt}')
        
        return self._refcnt
    
    def Release_Impl(self) -> int:
        if self._unk_outer:
            dbg_trace(provider, f'TraceID {self._trace_id} Release forwarded to outer IUnknown')
            return self._unk_outer.Release()
        
        if self._mta_:
            with self._lock:
                self._refcnt -= 1
        else:
            self._refcnt -= 1
            
        if self._refcnt == 0:
            self.Cleanup()
        
        dbg_trace(provider, f'TraceID {self._trace_id} refcnt = {self._refcnt}')
        
        return self._refcnt
            
    def Cleanup(self):
        dbg_trace(provider, )
        
    def __del__(self): 
        dbg_trace(provider, f'TraceID {self._trace_id} Delete COMRefCount={self._refcnt} PythonRefCount={sys.getrefcount(self)}')
        
class CUnknownMTA(CUnknown):
    _mta_ = True
        
def QI_SetInterface(itf: IUnknown, ppvObject: IVoidPtr, virtual_table: COMVirtualTable) -> int:
    if not ppvObject: # unmanaged parameter needs check
        dbg_trace(provider, 'E_POINTER')
        return E_POINTER

    lpVtbl = PVOID(getattr(itf, virtual_table.field_name))
    pItf = pointer(lpVtbl)
    _defb_ci.PyObject_GC_UnTrack(pItf) # unmanage lpVtbl from Python GC controlship
    i_cast(ppvObject, PLPVOID).contents.value = PtrUtil.get_address(pItf)
    itf.AddRef()
    
    dbg_trace(provider, 'S_OK')
    return S_OK

class CComObject(CUnknownMTA):
    _com_map_: ClassVar[list[tuple[COMInterface, COMVirtualTable]]]
    _unk_outer: IUnknown
    
    def __init__(self, *args):
        dbg_trace(provider, f'TraceID {CUnknown._trace_id_next_}')
        super().__init__()
        
        self.implement(self.QueryInterface)
    
    def QueryInterface_Impl(self, piid: IPointer[IID], ppv: IVoidPtr) -> int:
        iid = piid.contents
        
        if self._unk_outer and iid == IUnknown._iid_: 
            dbg_trace(provider, f'TraceID {self._trace_id} QueryInterface forwarded to outer IUnknown')
            return self._unk_outer.QueryInterface(iid, ppv)
        
        if iid == IUnknown.iid():
            dbg_trace(provider, f'TraceID {self._trace_id} IUnknown')
            return QI_SetInterface(self, ppv, self.virtual_table)
        elif iid == self.iid():
            dbg_trace(provider, f'TraceID {self._trace_id} {self.__class__.__name__}')
            return QI_SetInterface(self, ppv, self.virtual_table)
        
        for ci, virtual_table in self._com_map_:
            if iid == ci.iid():
                dbg_trace(provider, f'TraceID {self._trace_id} {virtual_table.name}')
                return QI_SetInterface(self, ppv, virtual_table)
            
        dbg_trace(provider, f'TraceID {self._trace_id} No interface {iid}')
        i_cast(ppv, PLPVOID).contents.value = NULL
        return E_NOINTERFACE

class CComClass(CComObject, COMClass):
    _implements_: ClassVar[list[COMInterface]] = []
    _aggregatable_: ClassVar[bool] = False
    _creatable_: ClassVar[bool] = False

    def __init_subclass__(cls, *args, **kwargs):
        if cls._creatable_:
            Name = f'{cls.__name__}_Factory'
            
            class Factory(CFactory):
                _com_class_ = cls
                
            Factory.__qualname__ = Name; Factory.__name__ = Name
            CFactory.g_Factories.append(Factory)

def Pair_Ref(itf: IUnknown) -> tuple[int, int]:
    dbg_trace(provider, itf.virtual_table.name)
    return itf.AddRef(), itf.Release()

def CI_SetInterface(itf: IUnknown, pvPpvObject: IVoidPtr):
    ppvObject = i_cast(pvPpvObject, PLPVOID)
    if itf is NULL:
        dbg_trace(provider, '*ppvObject = NULL')
        ppvObject.contents.value = NULL
    else:
        dbg_trace(provider, '*ppvObject = itf')
        ppvObject.contents.value = PtrUtil.get_address(itf.ref())

def DeclareDLLRoutines():
    """
    Insert DLL Routines into caller space
    """
    caller_frame = get_caller_frame()
    caller_frame.f_locals['I_DllCanUnloadNow'] = TL_I_DllCanUnloadNow
    caller_frame.f_locals['I_DllGetClassObject'] = TL_I_DllGetClassObject

class CFactory(CComObject, IClassFactory):
    _com_map_ = [(IClassFactory, IClassFactory.virtual_table)]
    _com_class_: ClassVar[CComClass]
    
    g_Factories: list[type['CFactory']] = []
    g_cLocks: ClassVar[int] = 0
    g_cRefs: ClassVar[int] = 0
    
    def __init__(self):
        dbg_trace(provider, f'TraceID {self._trace_id_next_}')
        super().__init__()
        
        # IClassFactory
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.CreateInstance)
        self.implement(self.LockServer)
        
        with self._lock:
            self.__class__.g_cRefs += 1
            
        self.__self__ = self # prevent unload
            
    def Cleanup(self):
        with self._lock:
            self.__class__.g_cRefs -= 1
    
    def CreateInstance_Impl(self, pUnkOuter: IPointer[IUnknown], 
                            riid: IPointer[IID], pvPpvObject: IVoidPtr, **kwargs):
        if not self._com_class_._aggregatable_ and pUnkOuter:
            dbg_trace(provider, "Class doesn't support aggregation.")
            return CLASS_E_NOAGGREGATION
        
        iid = riid.contents
        
        com_map = self._com_class_._com_map_ + [(IUnknown, None)]
        
        for com_interface, _ in com_map:
            if com_interface._iid_ == iid:
                if pUnkOuter:
                    com_class = self._com_class_(pUnkOuter.contents)
                else:
                    com_class = self._com_class_()
                CI_SetInterface(com_class, pvPpvObject)
                dbg_trace(provider, f'{com_interface.virtual_table.name} --> '
                          f'{self._com_class_.__name__}')
                return S_OK
            
        dbg_trace(provider, f'No interface was found for IID {iid}')
        CI_SetInterface(NULL, pvPpvObject)
        return E_NOINTERFACE
    
    def LockServer_Impl(self, fLock):
        with self._lock:
            if fLock:
                self.__class__.g_cLocks += 1
                dbg_trace(provider, 'Lock S_OK')
            else:
                self.__class__.g_cLocks -= 1
                dbg_trace(provider, 'Unlock S_OK')
                
        return S_OK

def TL_I_DllCanUnloadNow() -> int:
    for factory in CFactory.g_Factories:
        if factory.g_cRefs == 0 and CFactory.g_cLocks == 0:
            return S_FALSE
    return S_OK

def TL_I_DllGetClassObject(rclsid: int, riid: int, ppv: int) -> int:
    clsid = i_cast(rclsid, PIID).contents
    iid = i_cast(riid, PIID).contents
    ppv = i_cast(ppv, PVOID)
    
    for cls_factory in CFactory.g_Factories:
        if cls_factory._com_class_._clsid_ == clsid:
            factory = cls_factory()
            dbg_trace(provider, 'factory->QueryInterface(iid, ppv)')
            return factory.QueryInterface(iid, ppv)
    
    dbg_trace(provider, f'CLSID "{clsid}" not available')
    return CLASS_E_CLASSNOTAVAILABLE

from .guidmaintain import NewClsid, NewIid, SetGuid

def GetCLSID() -> CLSID:
    caller_frame = get_caller_frame()
    qualname = caller_frame.f_locals['__qualname__']
    return NewClsid(qualname)

def GetIID() -> IID:
    caller_frame = get_caller_frame()
    qualname = caller_frame.f_locals['__qualname__']
    return NewIid(qualname)

SetGuid('IPythonControl', IID('{E33B6F0E-612E-4B9D-B0EA-268FD400E1B1}'))

class IPythonControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
        
    @virtual_table.com_function(BOOL)
    def EnableGC(self, fGCEnabled: bool) -> int: 
        """
        Enable/Disable GC.
        
        Guarantee the stability of allocated vtables and objects.
        """
    
    virtual_table.build()
    
SetGuid('PythonControl', CLSID('{59434B84-E147-49A2-9ED8-84CBBEF0DD4A}'))
    
class PythonControl(CComClass, IPythonControl):
    _com_map_ = [(IPythonControl, IPythonControl.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    def __init__(self):
        dbg_trace(provider, f'Trace ID {self._trace_id_next_}')
        super().__init__()
        
        # IPythonControl
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.EnableGC)
        
        self.__self__ = self
    
    def EnableGC_Impl(self, fGCEnabled):
        if fGCEnabled:
            dbg_trace(provider, 'GC Enabled')
            gc.enable()
        else:
            dbg_trace(provider, 'GC Disabled')
            gc.disable()
        return S_OK
    
SetGuid('IEnumWETProvider', IID('{95669320-4BA5-40EF-8A36-73D2C3705302}'))
    
class IEnumWETProvider(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(ULONG, POINTER(PWET_PROVIDER), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[WET_PROVIDER],
             pceltFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumWETProvider']) -> int: ...
    
    virtual_table.build()
    
SetGuid('IWETManager', IID('{D9123535-E079-4CD9-8B4B-7CFC88DBFC27}'))
    
class IWETManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(LPCWSTR, PWET_EVENT_CALLBACK, PDWORD)
    def Subscribe(self, Provider: str, EventCallback: FARPROC, pdwCookie: PDWORD) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, DWORD)
    def Unsubscribe(self, Provider: str, dwCookie: int) -> int: ...
    
    @virtual_table.com_function(IEnumWETProvider.DOUBLE_PTR())
    def GetProviderEnumerator(self, ppenum: IDoublePtr[IEnumWETProvider]) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, PWET_EVENT)
    def SendEvent(self, Provider: str, pWetEvent: IPointer[WET_EVENT]) -> int: ...
    
    virtual_table.build()
    
SetGuid('WETManager', CLSID('{80644DEE-3A49-4574-ADDE-23EDBDC8F3DB}'))
    
class WETManager(CComClass, IWETManager):
    _com_map_ = [(IWETManager, IWETManager.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    def __init__(self):
        dbg_trace(provider, f'Trace ID {self._trace_id_next_}')
        super().__init__()
        
        # IWETManager
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.Subscribe)
        self.implement(self.Unsubscribe)
        self.implement(self.GetProviderEnumerator)
        self.implement(self.SendEvent)
        
    def Subscribe_Impl(self, Provider: str, EventCallback: FARPROC, pdwCookie: PDWORD) -> int: 
        if not EventCallback:
            dbg_trace(provider, 'EventCallback == NULL!')
            return E_POINTER
        
        if not pdwCookie:
            dbg_trace(provider, 'pdwCookie == NULL!')
            return E_POINTER
        
        if not Provider: 
            dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        try:
            cookie = WETProvider_Subscribe(Provider, EventCallback)
        except ValueError:
            dbg_trace(provider, f'No provider {Provider}')
            return E_INVALIDARG
        
        dbg_trace(provider, f'Subscribed consumer cookie "{cookie}" for provider {Provider}')
        pdwCookie.contents.value = cookie
        
        return S_OK
    
    def Unsubscribe_Impl(self, Provider: str, dwCookie: int) -> int:
        if not Provider:
            dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        try:
            WETProvider_Unsubscribe(Provider, dwCookie)
        except ValueError:
            dbg_trace(provider, f'No provider {Provider} for consumer cookie "{dwCookie}"')
            return E_INVALIDARG
        
        dbg_trace(provider, f'Unsubscribed consumer cookie "{dwCookie}" from provider {Provider}')
        return S_OK
    
    def GetProviderEnumerator_Impl(self, ppenum: IDoublePtr[IEnumWETProvider]) -> int: 
        if not ppenum:
            dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        enumerator = EnumWETProvider()
        ppenum.contents = enumerator.ptr()
        
        dbg_trace(provider, 'S_OK')
        return S_OK
    
    def SendEvent_Impl(self, Provider: str, pWetEvent: IPointer[WET_EVENT]) -> int:
        if not Provider:
            dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        if not pWetEvent:
            dbg_trace(provider, 'pWetEvent == NULL!')
            return E_POINTER
        
        WetProvider = _WET_GLOBAL_STATE.LookupProvider(Provider)
        if WetProvider is None:
            dbg_trace(provider, f'No provider "{Provider}"')
            return E_INVALIDARG
        
        pWetEvent.contents.pWetProvider = WetProvider.ptr()
        pWetEvent.contents.TimeDateStamp = round(datetime.now().timestamp())
        
        WetProvider.SendEvent(pWetEvent.contents)
        
        dbg_trace(provider, 'S_OK')
        return S_OK
    
SetGuid('EnumWETProvider', CLSID('{2F8EAAC1-D186-46F1-B2A4-7023AD1E1338}'))
    
class EnumWETProvider(CComClass, IEnumWETProvider):
    _com_map_ = [(IEnumWETProvider, IEnumWETProvider.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    _index: int
    
    def __init__(self):
        dbg_trace(provider, f'Trace ID {self._trace_id_next_}')
        super().__init__()
        
        # IEnumWETProvider
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.Next)
        self.implement(self.Skip)
        self.implement(self.Clone)
        
        self._index = 0
        
    def Next_Impl(self, celt: int, rgelt: IDoublePtr[WET_PROVIDER],
             pceltFetched: PULONG) -> int: 
        if celt == 0:
            dbg_trace(provider, 'celt == 0')
            
            if pceltFetched:
                pceltFetched.contents = 0
                
            return S_OK
        
        if not rgelt:
            dbg_trace(provider, 'rgelt == NULL!')
            return E_POINTER
        
        if celt != 1 and not pceltFetched:
            dbg_trace(provider, 'celt != 1 && pceltFetched == NULL!')
            return E_POINTER
        
        for i in range(celt):
            index = self._index + i
            
            if index == len(_WET_GLOBAL_STATE._providers_):
                self._index += celt
                
                if celt != 1:
                    pceltFetched.contents.value = i
                    
                dbg_trace(provider, f'S_FALSE, fetched {i}')
                    
                return S_FALSE
            
            rgelt[i] = _WET_GLOBAL_STATE._providers_[index].ptr()
        
        if celt != 1:
            pceltFetched.contents.value = celt
            
        self._index += celt
        
        dbg_trace(provider, f'S_OK, fetched {celt}')
        
        return S_OK
    
    def Skip_Impl(self, celt: int) -> int: 
        self._index += celt
        dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Clone_Impl(self, ppenum: IDoublePtr['IEnumWETProvider']) -> int:
        if not ppenum:
            dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        enum = EnumWETProvider()
        ppenum.contents = enum.ptr()
        enum._index = self._index
        
        dbg_trace(provider, 'S_OK')
        return S_OK