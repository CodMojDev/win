from ...wet.trace import _WET_GLOBAL_STATE
from .factory import *

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