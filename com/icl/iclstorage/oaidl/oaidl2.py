# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 15:04:10 2026
# Generated from ICL: oaidl2.icl
# {
class ITypeLib2(ITypeLib):
	virtual_table = COMVirtualTable.from_ancestor(ITypeLib)
	_iid_ = IID("{00020411-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPGUID, LPVARIANT, intermediate_method = True)
	def GetCustData(self, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(guid.ref(), pVarVal)

	@virtual_table.com_function(PULONG, PULONG)
	def GetLibStatistics(self, pcUniqueNames: PULONG, pcchUniqueNames: PULONG) -> int: ...

	@virtual_table.com_function(INT, LCID, PTR(BSTR), PDWORD, PTR(BSTR))
	def GetDocumentation2(self, index: int, lcid: LCID, pbstrHelpString: IPointer[BSTR], pdwHelpStringContext: PDWORD, pbstrHelpStringDll: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPCUSTDATA)
	def GetAllCustData(self, pCustData: IPointer[CUSTDATA]) -> int: ...

	virtual_table.build()

LPTYPELIB2 = ITypeLib2.PTR()

# }
