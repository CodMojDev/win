#
# com/comtl/baseface.py
#

from ..unknwn import *

# *****************
# * Ancient parts *
# *****************

# {

# TODO: Rewrite class logic
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
        
# }

from ..oleauto import *

# ***************
# * Helpers     *
# ***************

def TlAllocateString(String: str) -> int:
    """
    Allocate COM String.
    """
    buffer_length = (len(String) + 1) << 1
    string_buffer = CoTaskMemAlloc(buffer_length)
    memmove(string_buffer, String, buffer_length)
    return string_buffer

def TlAllocateOAString(String: str) -> int:
    """
    Allocate Ole Automation BSTR.
    """
    string_buffer = SysAllocString(String)
    return string_buffer

def TlWritePointerToPpv(pvPpv: int, Ptr: IPointer):
    """
    Write generic pointer to `void**`-like argument.
    """
    i_cast(pvPpv, PLPVOID).contents.value = PtrUtil.get_address(Ptr)
    
def TlWritePvToPpv(pvPpv: int, Pv: int):
    """
    Indirectly write generic address to `void**`-like argument.
    """
    ppv = i_cast(pvPpv, PLPVOID)
    ppv.contents.value = Pv
    
def TlAccessPpv(pvPpv: int, type_object: type[WT]) -> WT:
    """
    Access the `void**`-like argument and get the accessable object.
    """
    return i_cast(pvPpv, PTR(type_object)).contents

if TYPE_CHECKING:
    from .unknown import CUnknown

def TlNullPtrCheck(*pointers, pointer_names: list[str] = [], provider: WET_PROVIDER = None, comobj: 'CUnknown' = None) -> bool:
    """
    Check the pointers non-null.
    """
    for pointer_no, pointer in enumerate(pointers):
        if not pointer:
            if provider is None: return True
            pointer_name = pointer_names[pointer_no]
            comobj.dbg_trace(provider, f'{pointer_name} == NULL!')
            return True
    return False
    
def TlGetRef(obj: CStructure):
    """
    Safely get reference to object.
    """
    return obj.ref() if obj else NULL

def TlTypeField(obj: CStructure, field: str, typ_callable: Callable):
    """
    Contracted shortcut version of `field_typed`.
    """
    field_typed(obj, field, '_' + field, typ_callable)

def TlIsMain(stack_level: int = 0) -> bool:
    """
    Check code executed as main script.
    """
    return get_py_frame(1 + stack_level).f_locals['__name__'] == '__main__'

def _TlUnpackArguments(arguments: tuple) -> list:
    result_arguments = []
    
    for argument in arguments:
        if isinstance(argument, (tuple, list)):
            result_arguments.extend(argument)
        else:
            result_arguments.append(argument)
    
    return result_arguments

def TlMakeArray(array_type: type[WT], *initialize_arguments: Any) -> IArray[WT]:
    """
    Make array from array type and initialize arguments.
    """
    initialize_arguments = _TlUnpackArguments(initialize_arguments)
    return (array_type * len(initialize_arguments))(*initialize_arguments)

def TlEntryPoint(entry_point: Callable, *args, **kwargs) -> Any:
    """
    Execute entry point if code executed as main.
    """
    if TlIsMain(1): return entry_point(*args, **kwargs)
    return None

def TlEntryPoint_Contract(*args, **kwargs) -> Any:
    """
    Execute contracted entry point if code executed as main.
    Entry point: `TlMain`
    """
    if TlIsMain(1):
        entry_point = get_caller_frame().f_locals['TlMain']
        return entry_point(*args, **kwargs)
    return None

def TlOAToBool(bool_value: bool) -> int:
    """
    Convert `bool` value to `VARIANT_BOOL` value.
    """
    return VARIANT_TRUE if bool_value else VARIANT_FALSE

def TlOAFromBool(bool_value: int) -> bool:
    """
    Convert `VARIANT_BOOL` value to `bool` value.
    """
    return bool_value == VARIANT_TRUE

def TlIsItfSupported(unk: IUnknown, itf: type[COMInterface]) -> bool:
    """
    Check is interface supported.
    """
    unusedItf = itf.NULL()
    hr = unk.QueryInterface(itf, byref(unusedItf))
    if FAILED(hr): return False
    if issubclass(itf, IUnknown):
        unusedItf: IPointer[IUnknown]
        unusedItf.contents.Release()
    return True

def TlTryInterfaces(unk: IUnknown, itf_array: list[type[COMInterface]]) -> list[type[COMInterface]]:
    """
    Try to query all given interfaces from `IUnknown` and return success query list.
    """
    result = []
    for itf in itf_array:
        supported = TlIsItfSupported(unk, itf)
        if supported:
            result.append(itf)
    return result

def TlTryInterfacesStr(unk: IUnknown, itf_array: list[type[COMInterface]]) -> list[str]:
    """
    Try to query all given interfaces from `IUnknown` and return
    success query list in interface names.
    """
    interfaces = TlTryInterfaces(unk, itf_array)
    result = []
    for itf in interfaces:
        result.append(itf.__name__)
    return result

def TlQueryInterface(unk: IT, itf: type[IT2]) -> IT2:
    """
    Query interface from `IUnknown`.
    """
    itf_instance = itf.NULL()
    hr = unk.QueryInterface(itf, byref(itf_instance))
    if FAILED(hr): raise COMError(hr)
    return itf_instance.contents

def TlQueryInterfacePtr(unk: IT, itf: type[IT2]) -> IPointer[IT2]:
    """
    Query interface pointer from `IUnknown`.
    """
    itf_instance = itf.NULL()
    hr = unk.QueryInterface(itf, byref(itf_instance))
    if FAILED(hr): raise COMError(hr)
    return itf_instance

def TlAccessOAStringAndFree(bstr: BSTR) -> str:
    """
    Access OLE Automation string and free it.
    """
    string = bstr.value
    SysFreeString(bstr)
    return string

#
# COM TL Context utilities
#

class _TL_CONTEXT:
    __slots__ = ['_virtual_table_on_ctx', '_property_store', '_local_contexts']
    
    _local_contexts: list['_TL_CONTEXT']
    _virtual_table_on_ctx: VirtualTable
    _property_store: dict
    
_tl_context = _TL_CONTEXT()

def _TlContext_InitEx(context: _TL_CONTEXT):
    context._virtual_table_on_ctx = None
    context._property_store = {}
    context._local_contexts = []
    
    context._property_store['_object_refs'] = []

def _TlContext_Init():
    _TlContext_InitEx(_TlContext_AutomaticGet())

def _TlContext_GetLocalContext() -> _TL_CONTEXT:
    local_contexts = _tl_context._local_contexts
    
    if not local_contexts:
        return None
    
    return local_contexts[-1]

def _TlContext_GetLocalContext_Guarantee() -> _TL_CONTEXT:
    context = _TlContext_GetLocalContext()
    
    if context is None:
        raise RuntimeError('Local context is not set.')
    
    return context

def _TlContext_AutomaticGet() -> _TL_CONTEXT:
    local_context = _TlContext_GetLocalContext()
    
    if local_context is None:
        return _tl_context
    
    return local_context
    
# Property store is global
def TlContext_SetProperty(property: str, value: Any):
    """
    Set property in Context Property store.
    """
    _tl_context._property_store[property] = value
    
def TlContext_GetProperty(property: str) -> Any:
    """
    Get property from Context Property store.
    """
    return _tl_context._property_store[property]

# For maintainability object refs lists storaged as local
def TlAddRef(obj: Any):
    """
    Add reference to the object.
    """
    object_refs: list[Any] = _TlContext_AutomaticGet()._property_store['_object_refs']
    object_refs.append(obj)

def TlReleaseRef(obj: Any):
    """
    Release reference to the object.
    """
    property_store = _TlContext_AutomaticGet()._property_store
    for i, obj_ref in enumerate(property_store['_object_refs']):
        if obj_ref is obj:
            property_store['_object_refs'].pop(i)
            break
    
# Vtable manipulation is local
def TlContext_GetVtable() -> VirtualTable:
    """
    Get the virtual table from local context.
    """
    return _TlContext_GetLocalContext_Guarantee()._virtual_table_on_ctx

def TlOverride(method: Callable):
    """
    Override the method from local context.
    Naming contract: `<function name>`_Impl
    """
    _TlContext_GetLocalContext_Guarantee()._virtual_table_on_ctx.override(method.__self__, method)

def TlContext_SetVtable(vtable: VirtualTable):
    """
    Assign the virtual table to local context.
    """
    _TlContext_GetLocalContext_Guarantee()._virtual_table_on_ctx = vtable

def TlContext_Contract_SetVtable(self):
    """
    Contracted version of `TlContext_SetVtable`.
    Requires setted `virtual_table` field in `self`.
    """
    virtual_table = getattr(self, 'virtual_table', None)
    if virtual_table is None:
        raise ArgumentError('Contract for x.virtual_table is broken.')
    TlContext_SetVtable(virtual_table)
    
def TlInitVtableEx(self, virtual_table: VirtualTable):
    """
    Indirectly initialize virtual table.
    """
    vtable = virtual_table.VType()
    TlAddRef(vtable)
    setattr(self, virtual_table.field_name, 
                i_cast(pointer(vtable), PVOID))

def TlInitVtable(self): 
    """
    Initialize virtual table by local context.
    """
    TlInitVtableEx(self, TlContext_GetVtable())

def TlGetVtablePtrEx(self, virtual_table: VirtualTable) -> int:
    """
    Indirectly get virtual table pointer.
    """
    return getattr(self, virtual_table.field_name)

def TlGetVtablePtr(self) -> int:
    """
    Get virtual table pointer by local context.
    """
    return TlGetVtablePtrEx(self, TlContext_GetVtable())

def TlGetVtableEx(self, virtual_table: VirtualTable) -> CStructure:
    """
    Indirectly get virtual table structure.
    """
    return i_cast(TlGetVtablePtrEx(self, virtual_table), virtual_table.VType.PTR()).contents

def TlGetVtable(self) -> CStructure:
    """
    Get virtual table structure by local context.
    """
    return TlGetVtableEx(self, TlContext_GetVtable())

def TlCopyVtableEx(self, virtual_table: VirtualTable):
    """
    Indirectly copy virtual table.
    """
    vtableOld = TlGetVtablePtrEx(self, virtual_table)
    TlInitVtableEx(self, virtual_table)
    memmove(TlGetVtablePtrEx(self, virtual_table), vtableOld, 
            sizeof(virtual_table.VType))
    
def TlCopyVtable(self): 
    """
    Copy virtual table by local context.
    """
    TlCopyVtableEx(self, TlContext_GetVtable())
    
def TlGetMethodPtrEx(self, method_name: str, virtual_table: VirtualTable) -> int:
    """
    Indiectly get the method pointer in virtual table.
    """
    vtable_ptr = TlGetVtablePtrEx(self, virtual_table)
    method_offset = virtual_table.VType.offset(method_name)
    return vtable_ptr + method_offset

def TlGetMethodPtr(self, method_name: str) -> int:
    """
    Get the method pointer in virtual table by local-context virtual table.
    """
    return TlGetMethodPtrEx(self, method_name, TlContext_GetVtable())
    
# Misc `sys.path` manipulation
def TlPath_Add(path: str, first: bool = False):
    """
    Append path to `sys.path`.
    """
    if first:
        sys.path.insert(0, path)
    else:
        sys.path.append(path)
    
def TlPath_AddInterpreter(path: str, first: bool = False):
    """
    Add Python interpreter paths to `sys.paths`.
    """
    TlPath_Add(path + '\\Lib', first)
    TlPath_Add(path + '\\Lib\\site-packages', first)

# Local context manipulation
def TlContext_Hold(context_holder = None):
    """
    Hold the local context.
    """
    if context_holder is None:
        context = _TL_CONTEXT()
    else:
        context = getattr(context_holder, '_local_context', None)
        if context is None:
            raise ArgumentError('Invalid context holder.')
    
    _tl_context._local_contexts.append(context)
    _TlContext_Init()
    
def TlContext_Acquire(context = None):
    """
    Acquire the local context.
    """
    TlContext_Hold(context)
    
def TlContext_Release():
    """
    Release the local context.
    """
    if not _tl_context._local_contexts:
        raise RuntimeError('No active local context.')
    
    _tl_context._local_contexts.pop()
    
def TlContext_Save(self):
    """
    Opaquely save local context to context holder.
    """
    context = _TlContext_GetLocalContext_Guarantee()
    setattr(self, '_local_context', context)
    
def TlContext_Destroy(self):
    """
    Destroy previously saved local context from context holder.
    """
    delattr(self, '_local_context')
    
# initialize TL Context
_TlContext_InitEx(_tl_context)