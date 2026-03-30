from .object import *

class CComClass(CComObject, COMClass):
    """
    Class representing COM Class.
    Can be aggregatable and creatable.
    """
    
    _aggregatable_: ClassVar[bool] = False
    _creatable_: ClassVar[bool] = False
    _factory: 'CFactory'

    def __init_subclass__(cls, *args, **kwargs):
        if cls._creatable_:
            Name = f'{cls.__name__}_Factory'
            
            class Factory(CFactory):
                _com_class_ = cls
                
            # Initialize the Factory object
            Factory.__qualname__ = Name; Factory.__name__ = Name
            CFactory.g_Factories.append(Factory) # add to global list of factories
            
    def Cleanup(self):
        super().Cleanup()
        
        factory = getattr(self, '_factory', None)
        if factory is not None:
            factory.Release()

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
    caller_frame.f_locals['I_DllCanUnloadNow'] = TlDllCanUnloadNow
    caller_frame.f_locals['I_DllGetClassObject'] = TlDllGetClassObject

class CFactory(CComObject, IClassFactory):
    """
    Class representing the class factory.
    """
    _com_map_ = [(IClassFactory, IClassFactory.virtual_table)]
    _com_class_: ClassVar[type[CComClass]]
    
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
                com_class._factory = self
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
def TlDllCanUnloadNow() -> int:
    # if any factory has refs and locks, then don't unload library
    for factory in CFactory.g_Factories:
        if factory.g_cRefs == 0 and CFactory.g_cLocks == 0:
            return S_FALSE
    # otherwise, let COM unload
    return S_OK

# DllGetClassObject implementation
def TlDllGetClassObject(rclsid: int, riid: int, ppv: int) -> int:
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

from ..guidmaintain import NewClsid, NewIid, SetGuid

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