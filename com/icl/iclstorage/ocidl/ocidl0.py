# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:18:07 2026
# Generated from ICL: ocidl0.icl
# {
class IClassFactory2(IClassFactory):
	virtual_table = COMVirtualTable.from_ancestor(IClassFactory)
	_iid_ = IID("{B196B28F-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(PTR(LICINFO))
	def GetLicInfo(self, pLicInfo: IPointer[LICINFO]) -> int: ...

	@virtual_table.com_function(DWORD, PTR(BSTR))
	def RequestLicKey(self, dwReserved: int, pBstrKey: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPUNKNOWN, LPUNKNOWN, LPIID, PTR(BSTR), PVOID, PVOID, intermediate_method = True)
	def CreateInstanceLic(self, pUnkOuter: IPointer[IUnknown], pUnkReserved: IPointer[IUnknown], iid: IID, bstrKey: IPointer[BSTR], ppvObj: IPointer[PVOID], **kwargs) -> int:
		return self.virt_delegate(pUnkOuter, pUnkReserved, iid.ref(), bstrKey, ppvObj)

	virtual_table.build()

LPCLASSFACTORY2 = IClassFactory2.PTR()

class IProvideClassInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B283-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(DOUBLE_PTR(ITypeInfo))
	def GetClassInfo(self, ppTI: IDoublePtr[ITypeInfo]) -> int: ...

	virtual_table.build()

LPPROVIDECLASSINFO = IProvideClassInfo.PTR()

# }
