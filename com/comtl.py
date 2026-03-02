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
    """
    Class representing the IUnknown implementation.
    
    Can be MTA through `_mta_` field and aggregatable through `unkOuter`,
    passed in arguments of constructor.
    """
    _mta_: ClassVar[bool] = False
    _refcnt: int
    _lock: Lock
    
    _trace_id_next_: ClassVar[int] = 0
    _trace_id: int
    
    _unk_outer: Optional[IUnknown]
    
    def __init__(self, *args):
        # Check on aggregation
        if len(args) != 0 and isinstance(args[0], IUnknown):
            self._unk_outer = args[0]
            self._unk_outer.AddRef()
        else:
            self._unk_outer = None
        
        # Initialize lock for MTA
        if self._mta_:
            self._lock = Lock()
        
        # Initialize Trace ID for WET Trace Logging
        self._trace_id = CUnknown._trace_id_next_
        CUnknown._trace_id_next_ += 1
        
        self.dbg_trace(provider)
        
        # Virtual table Initialization
        self.initialize_vtable(self.virtual_table)
        
        # IUnknown
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.AddRef)
        self.implement(self.Release)
        
        # COM Reference count
        self._refcnt = 1
        
    def AddRef_Impl(self) -> int:
        # If object is aggregated, forward AddRef to outer IUnknown
        if self._unk_outer:
            self.dbg_trace(provider, f'AddRef forwarded to outer IUnknown')
            return self._unk_outer.AddRef()
        
        # Do interlocked increment if MTA-version, else simply increment the reference count
        if self._mta_:
            with self._lock:
                self._refcnt += 1
        else:
            self._refcnt += 1
        
        self.dbg_trace(provider, f'refcnt = {self._refcnt}')
        
        return self._refcnt
    
    def Release_Impl(self) -> int:
        # If object is aggregated, forward Release to outer IUnknown
        if self._unk_outer:
            self.dbg_trace(provider, f'Release forwarded to outer IUnknown')
            return self._unk_outer.Release()
        
        # Do interlocked decrement if MTA-version, else simply decrement the reference count
        if self._mta_:
            with self._lock:
                self._refcnt -= 1
        else:
            self._refcnt -= 1
            
        # If reference count reached 0, then cleanup the COM Object
        if self._refcnt == 0:
            self.Cleanup()
        
        self.dbg_trace(provider, f'refcnt = {self._refcnt}')
        
        return self._refcnt
            
    def Cleanup(self):
        """
        Cleanup routine. Needs to be redefined in descendants
        (if they are need to free resources).
        """
        self.dbg_trace(provider)
        
    def __del__(self): 
        # Tracing the delete procedure, as it's happening randomly and needs debug
        self.dbg_trace(provider, f'Delete COMRefCount={self._refcnt} PythonRefCount={sys.getrefcount(self)}')
        
    def dbg_trace(self, provider: WET_PROVIDER, message: str = '', trace_id: int = -1, level: int = WET_LEVEL_INFO):
        """
        Debug trace for COM Object.
        """
        dbg_trace(provider, message, getattr(self, '_trace_id', -1) if trace_id == -1 else trace_id, level, 1)
        
class CUnknownMTA(CUnknown):
    """
    Class representing the MTA Version of `IUnknown` implementation.
    """
    _mta_ = True
        
def QI_SetInterface(itf: IUnknown, ppvObject: IVoidPtr, virtual_table: COMVirtualTable) -> int:
    """
    Set interface using interface virtual table, self interface and `ppvObject`.
    Used by `IUnknown::QueryInterface` implementation.
    """
    if not ppvObject: # unmanaged parameter needs check
        dbg_trace(provider, 'E_POINTER')
        return E_POINTER

    lpVtbl = PVOID(getattr(itf, virtual_table.field_name)) # create the pointer to virtual table
    pItf = pointer(lpVtbl) # create the pointer to interface (double pointer to virtual table)
    _defb_ci.PyObject_GC_UnTrack(pItf) # unmanage lpVtbl from Python GC controlship
    i_cast(ppvObject, PLPVOID).contents.value = PtrUtil.get_address(pItf)
    itf.AddRef() # Add reference to queried interface as by COM specification
    
    dbg_trace(provider, 'S_OK')
    return S_OK

class CComObject(CUnknownMTA):
    """
    Class representing an COM Object.
    QueryInterface handled by `_com_map_`
    """
    _com_map_: ClassVar[list[tuple[COMInterface, COMVirtualTable]]]
    
    def __init__(self, *args):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IUnknown
        self.implement(self.QueryInterface)
    
    def QueryInterface_Impl(self, piid: IPointer[IID], ppv: IVoidPtr) -> int:
        iid = piid.contents
        
        # If object is aggregated, forward QueryInterface to outer IUnknown
        if self._unk_outer and iid == IUnknown._iid_: 
            self.dbg_trace(provider, f'QueryInterface forwarded to outer IUnknown')
            return self._unk_outer.QueryInterface(iid, ppv)
        
        # If queried IUnknown, return main virtual table
        if iid == IUnknown.iid():
            self.dbg_trace(provider, f'IUnknown')
            return QI_SetInterface(self, ppv, self.virtual_table)
        elif iid == self.iid(): # or if queried main interface
            self.dbg_trace(provider, f'{self.__class__.__name__}')
            return QI_SetInterface(self, ppv, self.virtual_table)
        
        # otherwise, iterate over COM Map and check by IID
        for ci, virtual_table in self._com_map_:
            if iid == ci.iid():
                self.dbg_trace(provider, f'{virtual_table.name}')
                return QI_SetInterface(self, ppv, virtual_table)
        
        # Object is not supports queried interface
        self.dbg_trace(provider, f'No interface {iid}')
        i_cast(ppv, PLPVOID).contents.value = NULL
        return E_NOINTERFACE

class CComClass(CComObject, COMClass):
    """
    Class representing COM Class.
    Can be aggregatable and creatable.
    """
    
    _aggregatable_: ClassVar[bool] = False
    _creatable_: ClassVar[bool] = False

    def __init_subclass__(cls, *args, **kwargs):
        if cls._creatable_:
            Name = f'{cls.__name__}_Factory'
            
            class Factory(CFactory):
                _com_class_ = cls
                
            # Initialize the Factory object
            Factory.__qualname__ = Name; Factory.__name__ = Name
            CFactory.g_Factories.append(Factory) # add to global list of factories

def Pair_Ref(itf: IUnknown) -> tuple[int, int]:
    """
    Pair AddRef/Release for debugging and testing
    """
    dbg_trace(provider, itf.virtual_table.name)
    return itf.AddRef(), itf.Release()

def CI_SetInterface(itf: IUnknown, pvPpvObject: IVoidPtr):
    """
    Set interface using self interface and `pvPpvObject` (void** as void*).
    Used in `IClassFactory::CreateInterface` implementation.
    """
    ppvObject = i_cast(pvPpvObject, PLPVOID) # assume void* as void**
    if itf is NULL:
        dbg_trace(provider, '*ppvObject = NULL')
        ppvObject.contents.value = NULL # if interface is NULL, then set ppvObject to NULL
    else: # otherwise, set the ppvObject to provided interface by its pointer
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
    """
    Class representing the class factory.
    """
    _com_map_ = [(IClassFactory, IClassFactory.virtual_table)]
    _com_class_: ClassVar[CComClass]
    
    g_Factories: list[type['CFactory']] = []
    g_cLocks: ClassVar[int] = 0
    g_cRefs: ClassVar[int] = 0
    
    def __init__(self):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IClassFactory
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.CreateInstance)
        self.implement(self.LockServer)
        
        with self._lock:
            self.__class__.g_cRefs += 1
            
    def Cleanup(self):
        super().Cleanup()
        
        # Decrement the refs to factory
        with self._lock:
            self.__class__.g_cRefs -= 1
    
    def CreateInstance_Impl(self, pUnkOuter: IPointer[IUnknown], 
                            riid: IPointer[IID], pvPpvObject: IVoidPtr, **kwargs):
        # if pUnkOuter provided and COM Class doesn't support aggregation, then return error
        if not self._com_class_._aggregatable_ and pUnkOuter:
            self.dbg_trace(provider, "Class doesn't support aggregation.")
            return CLASS_E_NOAGGREGATION
        
        iid = riid.contents
        
        # end the COM Map with IUnknown entry
        com_map = self._com_class_._com_map_ + [(IUnknown, None)]
        
        for com_interface, _ in com_map:
            if com_interface._iid_ == iid:
                if pUnkOuter: # if pUnkOuter provided, then create aggregated object
                    com_class = self._com_class_(pUnkOuter.contents)
                else: # otherwise, create the autonomous object
                    com_class = self._com_class_()
                CI_SetInterface(com_class, pvPpvObject) # write the interface to pvPpvObject
                self.dbg_trace(provider, f'{com_interface.virtual_table.name} --> '
                          f'{self._com_class_.__name__}')
                return S_OK
        
        # Object is not supports provided interface
        self.dbg_trace(provider, f'No interface was found for IID {iid}')
        CI_SetInterface(NULL, pvPpvObject) # set pvPpvObject to NULL
        return E_NOINTERFACE
    
    def LockServer_Impl(self, fLock):
        with self._lock:
            if fLock: # decrement the factory locks
                self.__class__.g_cLocks += 1
                self.dbg_trace(provider, 'Lock S_OK')
            else: # increment the factory locks
                self.__class__.g_cLocks -= 1
                self.dbg_trace(provider, 'Unlock S_OK')
                
        return S_OK

# DllCanUnloadNow implementation
def TL_I_DllCanUnloadNow() -> int:
    # if any factory has refs and locks, then don't unload library
    for factory in CFactory.g_Factories:
        if factory.g_cRefs == 0 and CFactory.g_cLocks == 0:
            return S_FALSE
    # otherwise, let COM unload
    return S_OK

# DllGetClassObject implementation
def TL_I_DllGetClassObject(rclsid: int, riid: int, ppv: int) -> int:
    clsid = i_cast(rclsid, PIID).contents
    iid = i_cast(riid, PIID).contents
    ppv = i_cast(ppv, PVOID)
    
    # iterate over global factories list
    for cls_factory in CFactory.g_Factories:
        if cls_factory._com_class_._clsid_ == clsid:
            factory = cls_factory()
            dbg_trace(provider, 'factory->QueryInterface(iid, ppv)')
            return factory.QueryInterface(iid, ppv) # query the provided IID of a class factory
    
    # Requested class is not creatable by this library
    dbg_trace(provider, f'CLSID "{clsid}" not available')
    return CLASS_E_CLASSNOTAVAILABLE

from .guidmaintain import NewClsid, NewIid, SetGuid

def GetCLSID() -> CLSID:
    """
    Get the CLSID for COM Class from persist GUID storage.
    """
    caller_frame = get_caller_frame()
    qualname = caller_frame.f_locals['__qualname__']
    return NewClsid(qualname)

def GetIID() -> IID:
    """
    Get the IID for COM Interface from persist GUID storage.
    """
    caller_frame = get_caller_frame()
    qualname = caller_frame.f_locals['__qualname__']
    return NewIid(qualname)

SetGuid('IPythonControl', IID('{E33B6F0E-612E-4B9D-B0EA-268FD400E1B1}'))

class IPythonControl(IUnknown):
    """
    Python Control interface
    """
    
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
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IPythonControl
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.EnableGC)
    
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
    """
    WET Provider Enumerator
    """
    
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(ULONG, POINTER(PWET_PROVIDER), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[WET_PROVIDER],
             pceltFetched: PULONG) -> int: 
        """
        Return the next `celt` elements
        """
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: 
        """
        Skip `celt` elements
        """
    
    @virtual_table.com_function()
    def Reset(self) -> int: 
        """
        Reset the enumerator state
        """
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumWETProvider']) -> int: 
        """
        Clone the enumerator
        """
    
    virtual_table.build()
    
SetGuid('IWETManager', IID('{D9123535-E079-4CD9-8B4B-7CFC88DBFC27}'))
    
class IWETManager(IUnknown):
    """
    WET Manager
    """
    
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(LPCWSTR, PWET_EVENT_CALLBACK, PDWORD)
    def Subscribe(self, Provider: str, EventCallback: FARPROC, pdwCookie: PDWORD) -> int: 
        """
        Subscribe the consumer to provider
        """
    
    @virtual_table.com_function(LPCWSTR, DWORD)
    def Unsubscribe(self, Provider: str, dwCookie: int) -> int: 
        """
        Unsubscribe the consumer from provider by cookie
        """
    
    @virtual_table.com_function(IEnumWETProvider.DOUBLE_PTR())
    def GetProviderEnumerator(self, ppenum: IDoublePtr[IEnumWETProvider]) -> int: 
        """
        Get the WET Provider Enumerator
        """
    
    @virtual_table.com_function(LPCWSTR, PWET_EVENT)
    def SendEvent(self, Provider: str, pWetEvent: IPointer[WET_EVENT]) -> int: 
        """
        Send WET Event to the WET Provider
        """
    
    @virtual_table.com_function(STD_CONSUMER, PVOID)
    def ConfigureStandardConsumer(self, StdConsumerId: int, pData: PVOID) -> int: 
        """
        Configure the standard consumer with provided configuration data structure pointer.
        """
    
    @virtual_table.com_function(STD_CONSUMER, LPCWSTR, PDWORD)
    def RegisterStandardConsumer(self, StdConsumerId: int, Provider: str, pdwCookie: PDWORD) -> int: 
        """
        Subscribe the standard consumer to provider
        """
    
    @virtual_table.com_function(STD_CONSUMER)
    def StdStreamsToStandardConsumer(self, StdConsumerId: int) -> int: 
        """
        Restream the Std Streams to standard consumer
        """
    
    @virtual_table.com_function()
    def RestoreStdStreams(self) -> int: 
        """
        Restore the Std Streams
        """
    
    virtual_table.build()
    
SetGuid('WETManager', CLSID('{80644DEE-3A49-4574-ADDE-23EDBDC8F3DB}'))
    
class WETManager(CComClass, IWETManager):
    """
    WET Manager implementation
    """
    
    _com_map_ = [(IWETManager, IWETManager.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    def __init__(self):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IWETManager
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.Subscribe)
        self.implement(self.Unsubscribe)
        self.implement(self.GetProviderEnumerator)
        self.implement(self.SendEvent)
        self.implement(self.ConfigureStandardConsumer)
        self.implement(self.RegisterStandardConsumer)
        self.implement(self.ConfigureStandardConsumer)
        self.implement(self.StdStreamsToStandardConsumer)
        self.implement(self.RestoreStdStreams)
        
    def Subscribe_Impl(self, Provider: str, EventCallback: FARPROC, pdwCookie: PDWORD) -> int: 
        if not EventCallback:
            self.dbg_trace(provider, 'EventCallback == NULL!')
            return E_POINTER
        
        if not pdwCookie:
            self.dbg_trace(provider, 'pdwCookie == NULL!')
            return E_POINTER
        
        if not Provider: 
            self.dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        # Subscribe to provider
        try:
            Cookie = WETProvider_Subscribe(Provider, EventCallback)
        except ValueError: # No provider: ValueError thrown
            self.dbg_trace(provider, f'No provider {Provider}')
            return E_INVALIDARG
        
        self.dbg_trace(provider, f'Subscribed consumer cookie "{Cookie}" for provider {Provider}')
        pdwCookie.contents.value = Cookie # Return the Cookie
        
        return S_OK
    
    def Unsubscribe_Impl(self, Provider: str, dwCookie: int) -> int:
        if not Provider:
            self.dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        # Unsubscribe from provider
        try:
            WETProvider_Unsubscribe(Provider, dwCookie)
        except ValueError: # No provider: ValueError thrown
            self.dbg_trace(provider, f'No provider {Provider} for consumer cookie "{dwCookie}"')
            return E_INVALIDARG
        
        self.dbg_trace(provider, f'Unsubscribed consumer cookie "{dwCookie}" from provider {Provider}')
        return S_OK
    
    def GetProviderEnumerator_Impl(self, ppenum: IDoublePtr[IEnumWETProvider]) -> int: 
        if not ppenum:
            self.dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        # Create and set the EnumWETProvider
        enumerator = EnumWETProvider()
        i_cast(ppenum, PLPVOID).contents.value = PtrUtil.get_address(enumerator.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def SendEvent_Impl(self, Provider: str, pWetEvent: IPointer[WET_EVENT]) -> int:
        # Pointer checks
        if not Provider:
            self.dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        if not pWetEvent:
            self.dbg_trace(provider, 'pWetEvent == NULL!')
            return E_POINTER
        
        # Lookup the provider
        WetProvider = _WET_GLOBAL_STATE.LookupProvider(Provider)
        if WetProvider is None:
            self.dbg_trace(provider, f'No provider "{Provider}"')
            return E_INVALIDARG
        
        # This fields are set by SendEvent implementation
        pWetEvent.contents.pWetProvider = WetProvider.ptr()
        pWetEvent.contents.TimeDateStamp = round(datetime.now().timestamp())
        
        WetProvider.SendEvent(pWetEvent.contents) # send event to WET Provider
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def ConfigureStandardConsumer_Impl(self, StdConsumerId: int, pData: IVoidPtr) -> int:
        ConfigureStandardConsumer(StdConsumerId, pData) # configure theh standard consumer
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def RegisterStandardConsumer_Impl(self, StdConsumerId: int, Provider: str, pdwCookie: PDWORD) -> int: 
        if not pdwCookie:
            self.dbg_trace(provider, 'pdwCookie == NULL!')
            return E_POINTER
        
        if not Provider:
            self.dbg_trace(provider, 'Provider == NULL!')
            return E_POINTER
        
        # Register the standard consumer
        try:
            Cookie = RegisterStandardConsumer(StdConsumerId, Provider)
        except ValueError: # No provider: ValueError thrown
            self.dbg_trace(provider, f'No provider {Provider}')
            return E_INVALIDARG
        
        if Cookie == -1: # no ID
            self.dbg_trace(provider, f'No standard consumer ID {StdConsumerId}')
            return E_INVALIDARG
        
        pdwCookie.contents.value = Cookie # Return the Cookie
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def StdStreamsToStandardConsumer_Impl(self, StdConsumerId: int) -> int: 
        self.dbg_trace(provider, 'S_OK')
        StdStreamsToStandardConsumer(StdConsumerId) # Restream the Std Streams to standard consumer
        return S_OK
    
    def RestoreStdStreams_Impl(self) -> int: 
        self.dbg_trace(provider, 'S_OK')
        RestoreStdStreams() # Restore the Std Streams
        return S_OK
    
SetGuid('EnumWETProvider', CLSID('{2F8EAAC1-D186-46F1-B2A4-7023AD1E1338}'))
    
class EnumWETProvider(CComClass, IEnumWETProvider):
    """
    WET Provider Enumerator implementation
    """
    
    _com_map_ = [(IEnumWETProvider, IEnumWETProvider.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    _index: int
    
    def __init__(self):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IEnumWETProvider
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.Next)
        self.implement(self.Skip)
        self.implement(self.Reset)
        self.implement(self.Clone)
        
        self._index = 0
        
    def Next_Impl(self, celt: int, rgelt: IDoublePtr[WET_PROVIDER],
             pceltFetched: PULONG) -> int: 
        if celt == 0: # celt == 0, set the pceltFetched to 0 and return S_OK
            self.dbg_trace(provider, 'celt == 0')
            
            if pceltFetched:
                pceltFetched.contents = 0
                
            return S_OK
        
        if not rgelt:
            self.dbg_trace(provider, 'rgelt == NULL!')
            return E_POINTER
        
        # if celt > 1 and pceltFetched is NULL, then return error (by COM enumerator specification)
        if celt != 1 and not pceltFetched:
            self.dbg_trace(provider, 'celt != 1 && pceltFetched == NULL!')
            return E_POINTER
        
        # iterate in range(0, celt)
        for i in range(celt):
            index = self._index + i
            
            # if reached out of bounds
            if index == len(_WET_GLOBAL_STATE._providers_):
                self._index += celt # move the index
                
                if pceltFetched: # if pceltFetched, return the fetched elements count
                    pceltFetched.contents.value = i
                    
                self.dbg_trace(provider, f'S_FALSE, fetched {i}')
                
                return S_FALSE # enumeration stopped
            
            # otherwise, write the provider pointer to rgelt[i]
            rgelt[i] = _WET_GLOBAL_STATE._providers_[index].ptr()
        
        # if pceltFetched, return the fetched elements count
        if pceltFetched:
            pceltFetched.contents.value = celt
            
        self._index += celt # move the index
        
        self.dbg_trace(provider, f'S_OK, fetched {celt}')
        
        return S_OK
    
    def Skip_Impl(self, celt: int) -> int: 
        self._index += celt # skip the celt elements
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Reset_Impl(self) -> int:
        self._index = 0 # reset the enumerator
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Clone_Impl(self, ppenum: IDoublePtr['IEnumWETProvider']) -> int:
        if not ppenum:
            self.dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        # clone the enumerator and its state
        enum = EnumWETProvider()
        enum._index = self._index
        ppenum.contents = enum.ptr()
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK