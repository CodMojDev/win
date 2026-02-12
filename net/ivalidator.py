#
# ivalidator.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sun Feb  8 15:04:19 2026
# Generated from ICL: ivalidator.icl
#

from .ivehandler import *

VALIDATOR_EXTRA_VERBOSE = 1
VALIDATOR_SHOW_SOURCE_LINES = 2
VALIDATOR_CHECK_ILONLY = 4
VALIDATOR_CHECK_PEFORMAT_ONLY = 8
VALIDATOR_NOCHECK_PEFORMAT = 16
VALIDATOR_TRANSPARENT_ONLY = 32
ValidatorFlags = INT

class IValidator(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{63DF8730-DC81-4062-84A2-1FF943F59FAC}")

    @virtual_table.com_function(PTR(IVEHandler), LPUNKNOWN, ULONG, ULONG, ULONG, LPWSTR, PBYTE, ULONG)
    def Validate(self, veh: IPointer[IVEHandler], pAppDomain: IPointer[IUnknown], ulFlags: int, ulMaxError: int, token: int, fileName: LPWSTR, pe: PBYTE, ulSize: int) -> int: ...

    @virtual_table.com_function(HRESULT, VEContext, LPWSTR, ULONG, LPSAFEARRAY)
    def FormatEventInfo(self, hVECode: int, Context: VEContext, msg: LPWSTR, ulMaxLength: int, psa: IPointer[SAFEARRAY]) -> int: ...

    virtual_table.build()

class ICLRValidator(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{63DF8730-DC81-4062-84A2-1FF943F59FDD}")

    @virtual_table.com_function(PTR(IVEHandler), ULONG, ULONG, ULONG, ULONG, LPWSTR, PBYTE, ULONG)
    def Validate(self, veh: IPointer[IVEHandler], ulAppDomainId: int, ulFlags: int, ulMaxError: int, token: int, fileName: LPWSTR, pe: PBYTE, ulSize: int) -> int: ...

    @virtual_table.com_function(HRESULT, VEContext, LPWSTR, ULONG, LPSAFEARRAY)
    def FormatEventInfo(self, hVECode: int, Context: VEContext, msg: LPWSTR, ulMaxLength: int, psa: IPointer[SAFEARRAY]) -> int: ...

    virtual_table.build()

