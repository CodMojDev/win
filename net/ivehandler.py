#
# ivehandler.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sun Feb  8 15:04:19 2026
# Generated from ICL: ivehandler.icl
#

from ..com.unknwn import *

@CStructure.make
class _VerError(CStructure):
    flags: IUlong
    opcode: IUlong
    uOffset: IUlong
    Token: IUlong
    item1_flags: IUlong
    item1_data: PINT
    item2_flags: IUlong
    item2_data: PINT

VEContext = _VerError

CLSID_VEHandlerClass = CLSID("{856CA1B1-7DAB-11d3-ACEC-00C04F86C309}")

class IVEHandler(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{856CA1B2-7DAB-11d3-ACEC-00C04F86C309}")

    @virtual_table.com_function(HRESULT, VEContext, LPSAFEARRAY)
    def VEHandler(self, VECode: int, Context: VEContext, psa: IPointer[SAFEARRAY]) -> int: ...

    @virtual_table.com_function(PVOID)
    def SetReporterFtn(self, lFnPtr: PVOID) -> int: ...

    virtual_table.build()

