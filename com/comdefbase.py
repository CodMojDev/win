############################
# COMDEFBASE.PY
#
# COM Defines base module,
# Core of the module
############################

from ..defbase import *

from ..windef import *

from .. import cpreproc

from .errors import *

from typing import Optional, Callable

def MAKE_HRESULT(sev: int, fac: int, code: int) -> int:
    return HRESULT((ULONG(sev).value<<31) | (ULONG(fac).value<<16) | (ULONG(code).value)).value

# COM initialization flags; passed to CoInitialize.
#  DCOM
# These constants are only valid on Windows NT 4.0
COINITBASE_MULTITHREADED      = 0x0      # OLE calls objects on any thread.
COINITBASE = INT

# COM initialization flags; passed to CoInitialize.
COINIT_APARTMENTTHREADED  = 0x2      # Apartment model
# These constants are only valid on Windows NT 4.0
COINIT_MULTITHREADED      = COINITBASE_MULTITHREADED
COINIT_DISABLE_OLE1DDE    = 0x4      # Don't use DDE for Ole1 support.
COINIT_SPEED_OVER_MEMORY  = 0x8      # Trade memory for speed.
COINIT = INT

S_OK = 0
S_FALSE = 1

E_UNEXPECTED = 0x8000FFFF

E_NOTIMPL = 0x80004001
E_NOINTERFACE = 0x80004002
E_POINTER = 0x80004003
E_FAIL = 0x80004005
E_INVALIDARG = 0x80070057
E_OUTOFMEMORY = 0x8007000E

CLASS_E_NOAGGREGATION = 0x80040110
CLASS_E_CLASSNOTAVAILABLE = 0x80040111

CO_E_CLASSSTRING = 0x800401F3

CONNECT_E_CANNOTCONNECT = HRESULT(-2147220990).value
CONNECT_E_ADVISELIMIT = HRESULT(-2147220991).value
CONNECT_E_NOCONNECTION = HRESULT(-2147220992).value

TYPE_E_ELEMENTNOTFOUND = 0x8002802B

TYPE_E_REGISTRYACCESS = 0x8002801C
TYPE_E_CANTLOADLIBRARY = 0x80029C4A

DISP_E_BUFFERTOOSMALL = HRESULT(-2147352557).value
DISP_E_DIVBYZERO = HRESULT(-2147352558).value
DISP_E_NOTACOLLECTION = HRESULT(-2147352559).value
DISP_E_BADCALLEE = HRESULT(-2147352560).value
DISP_E_PARAMNOTOPTIONAL = 0x8002000F
DISP_E_BADPARAMCOUNT = 0x8002000E
DISP_E_ARRAYISLOCKED = 0x8002000D
DISP_E_UNKNOWNLCID = 0x8002000C
DISP_E_BADINDEX = 0x8002000B
DISP_E_OVERFLOW = 0x8002000A
DISP_E_EXCEPTION = 0x80020009
DISP_E_BADVARTYPE = 0x80020008
DISP_E_NONAMEDARGS = 0x80020007
DISP_E_UNKNOWNNAME = 0x80020006
DISP_E_TYPEMISMATCH = 0x800020005
DISP_E_PARAMNOTFOUND = 0x80020004
DISP_E_MEMBERNOTFOUND = 0x80020003
DISP_E_UNKNOWNINTERFACE = 0x80020001

RPC_E_CHANGED_MODE = 0x80010106
RPC_E_SERVERFAULT = 0x80010105

# 'macros' and constants to create your own HRESULT values:

def MAKE_HRESULT(sev, fac, code):
    return HRESULT((sev << 31 | fac << 16 | code)).value

SEVERITY_ERROR = 1
SEVERITY_SUCCESS = 0

FACILITY_ITF = 4
FACILITY_WIN32 = 7

def HRESULT_FROM_WIN32(x):
    x = LONG(x).value
    if FAILED(x): return x
    # 0x80000000 | FACILITY_WIN32 << 16 | x & 0xFFFF
    return HRESULT(0x80070000 | (x & 0xFFFF)).value

def SUCCEEDED(hr: int) -> bool:
    return LONG(hr or 0).value >= 0

def FAILED(hr: int) -> bool:
    return LONG(hr or 0).value < 0

ole32 = get_win_library('ole32.dll')

def ole_foreign(*args: type, 
            name: Optional[str] = None,
            intermediate_method: bool = False) -> Callable:
        """
        Foreign method declare
        """
        ret = foreign_optimized(HRESULT, 
                                 *args,
                                 library=ole32, 
                                 name=name, 
                                 intermediate_method=intermediate_method)
        return ret

def check_hresult(hr: int):
    if FAILED(hr): raise COMError(hr)

from ctypes import _SimpleCData

S_OK = 0
S_FALSE = 1
E_FAIL = -2147467259

if cpreproc.ifdef('HRESULT_DEBUG'):
    class HRESULT(_SimpleCData):
        _type_ = "l"
        _check_retval_ = check_hresult
else:
    HRESULT = LONG
    
class COM_GLOBAL_STATE:
    __slots__ = ['initialized']
    
    initialized: bool
    
    def __init__(self):
        self.initialized = False

com_state = COM_GLOBAL_STATE()

from .. import _defbase_ctypinit as _defb_ci

# manually fix the CPython bug with "initialized is readonly object attribute"
_defb_ci.PyType_CAST_DEREF(COM_GLOBAL_STATE).SetTPFLAG(_defb_ci.Py_TPFLAGS_MANAGED_DICT)

def CheckCOMInitialized():
    if not com_state.initialized:
        if FAILED(CoInitialize(NULL)):
            raise RuntimeError('COM cannot initialize')

# Initialize functions
@ole_foreign(LPVOID, intermediate_method=True)
def CoInitialize(pvReserved: LPVOID, **kwargs) -> int:
    """
    Initializes the COM library on the current thread and identifies the concurrency model as single-thread apartment (STA).

    New applications should call CoInitializeEx instead of CoInitialize.
    """
    
    hr = delegate(pvReserved)
    if SUCCEEDED(hr):
        com_state.initialized = True
    return hr
    
@ole_foreign(LPVOID, DWORD, intermediate_method=True)
def CoInitializeEx(pvReserved: LPVOID, dwCoInit: int, **kwargs) -> int: 
    """
    Initializes the COM library for use by the calling thread, sets the thread's concurrency model, and creates a new apartment for the thread if one is required.
    """
    
    hr = delegate(pvReserved, dwCoInit)
    if SUCCEEDED(hr):
        com_state.initialized = True
    return hr

@ole32.foreign(VOID, intermediate_method=True)
def CoUninitialize(**kwargs):
    """
    Closes the COM library on the current thread, unloads all DLLs loaded by the thread, frees any other resources that the thread maintains, and forces all RPC connections on the thread to close.
    """
    object.__setattr__(com_state, 'initialized', False)
    delegate()
    
# Memory management
@ole32.foreign(VOID, LPVOID)
def CoTaskMemFree(pv: LPVOID):
    """
    Frees a block of task memory previously allocated through a call to the CoTaskMemAlloc or CoTaskMemRealloc function.
    """

@ole32.foreign(LPVOID, SIZE_T)
def CoTaskMemAlloc(cb: int) -> LPVOID:
    """
    Allocates a block of task memory in the same way that IMalloc::Alloc does.
    """
    
@ole32.foreign(LPVOID, LPVOID, SIZE_T)
def CoTaskMemRealloc(pv: LPVOID, cb: int) -> LPVOID:
    """
    Changes the size of a previously allocated block of task memory.
    """