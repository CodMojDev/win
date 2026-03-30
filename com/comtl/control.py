from .factory import *

#
# Face interfaces to export from COM TL
#

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
        
    @virtual_table.function(VOID)
    def AddCrashLogging(self): 
        """
        Debug method to call first to connect debug logging.
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
        self.implement(self.AddCrashLogging)
    
    def EnableGC_Impl(self, fGCEnabled):
        if fGCEnabled:
            dbg_trace(provider, 'GC Enabled')
            gc.enable()
        else:
            dbg_trace(provider, 'GC Disabled')
            gc.disable()
        return S_OK
    
    def AddCrashLogging_Impl(self):
        RegisterStandardConsumer(STD_CONSUMER_PRINT, provider)
        StdStreamsToStandardConsumer(STD_CONSUMER_DEBUG)