from win.com.comdefbase import *

class WRPCException(RuntimeError): ...

class WRPCProtocolException(RuntimeError): ...

WRPC_S_OK = S_OK
WRPC_E_FAIL = E_FAIL
WRPC_E_POINTER = E_POINTER
WRPC_E_NOTIMPL = E_NOTIMPL
WRPC_E_MARSHAL = MAKE_HRESULT(SEVERITY_ERROR, FACILITY_ITF, 0x800)