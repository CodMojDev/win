# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 18:05:50 2026
# Generated from ICL: ocidl9.icl
# {
class IPerPropertyBrowsing(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{376BD3AA-3845-101B-84ED-08002B2EC713}")

	@virtual_table.com_function(DISPID, PTR(BSTR))
	def GetDisplayString(self, dispID: DISPID, pBstr: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(DISPID, LPCLSID)
	def MapPropertyToPage(self, dispID: DISPID, pClsid: IPointer[CLSID]) -> int: ...

	@virtual_table.com_function(DISPID, LPCALPOLESTR, LPCADWORD)
	def GetPredefinedStrings(self, dispID: DISPID, pCaStringsOut: IPointer[CALPOLESTR], pCaCookiesOut: IPointer[CADWORD]) -> int: ...

	@virtual_table.com_function(DISPID, DWORD, LPVARIANT)
	def GetPredefinedValue(self, dispID: DISPID, dwCookie: int, pVarOut: IPointer[VARIANT]) -> int: ...

	virtual_table.build()

LPPERPROPERTYBROWSING = IPerPropertyBrowsing.PTR()

# }
