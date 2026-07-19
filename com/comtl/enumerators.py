from .object import *
from .baseface import _TL_ENUMERATOR

class ValueEnumerator(CComObject, _TL_ENUMERATOR):
    """
    Value Enumerator implementation
    """
    
    _interface_: ClassVar[type[COMInterface]]
    _type_: ClassVar[type]
    _index: int
    
    def __init__(self, array: list, vtable: COMVirtualTable | None = None):
        if vtable is None: vtable = self.virtual_table
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        self.set_vtable_on_ctx(vtable)
        self.implement_interface(_TL_ENUMERATOR)
        self.array = array
        self._index = 0
        
    def Next_Impl(self, celt: int, rgelt: IDoublePtr,
             pceltFetched: IPointer[ULONG]) -> int: 
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
        
        rgelt = i_cast(rgelt, PTR(self._type_))
        
        # iterate in range(0, celt)
        for i in range(celt):
            index = self._index + i
            
            # if reached out of bounds
            if index == len(self.array):
                self._index += celt # move the index
                
                if pceltFetched: # if pceltFetched, return the fetched elements count
                    pceltFetched.contents.value = i
                    
                self.dbg_trace(provider, f'S_FALSE, fetched {i}')
                
                return S_FALSE # enumeration stopped
            
            # otherwise, write the provider pointer to rgelt[i]
            rgelt[i] = self.array[index]
        
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
    
    def Clone_Impl(self, ppenum: IDoublePtr['ValueEnumerator']) -> int:
        if not ppenum:
            self.dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        # clone the enumerator and its state
        enum = self.__class__(self.array)
        enum._index = self._index
        ppenum.contents = enum.ptr()
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
class StructurePtrEnumerator(CComObject, _TL_ENUMERATOR):
    """
    Structure pointer Enumerator implementation
    """
    
    _interface_: ClassVar[type[COMInterface]]
    _type_: ClassVar[type]
    _index: int
    
    def __init__(self, array: list, vtable: COMVirtualTable | None = None):
        if vtable is None: vtable = self.virtual_table
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        self.set_vtable_on_ctx(vtable)
        self.implement_interface(_TL_ENUMERATOR)
        self.array = array
        self._index = 0
        
    def Next_Impl(self, celt: int, rgelt: IDoublePtr,
             pceltFetched: IPointer[ULONG]) -> int: 
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
        
        rgelt = i_cast(rgelt, PTR(self._type_))
        
        # iterate in range(0, celt)
        for i in range(celt):
            index = self._index + i
            
            # if reached out of bounds
            if index == len(self.array):
                self._index += celt # move the index
                
                if pceltFetched: # if pceltFetched, return the fetched elements count
                    pceltFetched.contents.value = i
                    
                self.dbg_trace(provider, f'S_FALSE, fetched {i}')
                
                return S_FALSE # enumeration stopped
            
            # otherwise, write the provider pointer to rgelt[i]
            rgelt[i] = self.array[index].ptr()
        
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
    
    def Clone_Impl(self, ppenum: IDoublePtr['ValueEnumerator']) -> int:
        if not ppenum:
            self.dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        # clone the enumerator and its state
        enum = self.__class__(self.array)
        enum._index = self._index
        ppenum.contents = enum.ptr()
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK