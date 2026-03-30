from ..unknwn import *

from ... import _defbase_ctypinit as _defb_ci
from threading import Lock
from ._provider import *
    
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
        _defb_ci.PyObject_GC_UnTrack(self) # unmanage self from GC controlship
        
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
        
        # C isn't now holding refs on COM Object, so return control to Python GC
        _defb_ci.PyObject_GC_Track(self) # manage self into GC controlship
        
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