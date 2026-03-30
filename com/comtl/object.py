from .unknown import *

from ... import _defbase_ctypinit as _defb_ci

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