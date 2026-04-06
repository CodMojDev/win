# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 18:05:53 2026
# Generated from ICL: ocidl10.icl
# {
class IPropertyBag2(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{22F55882-280B-11d0-A8A9-00A0C90C2004}")

	@virtual_table.com_function(ULONG, PTR(PROPBAG2), PTR(IErrorLog), LPVARIANT, PTR(HRESULT))
	def Read(self, cProperties: int, pPropBag: IPointer[PROPBAG2], pErrLog: IPointer[IErrorLog], pvarValue: IPointer[VARIANT], phrError: IPointer[HRESULT]) -> int: ...

	@virtual_table.com_function(ULONG, PTR(PROPBAG2), LPVARIANT)
	def Write(self, cProperties: int, pPropBag: IPointer[PROPBAG2], pvarValue: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(PULONG)
	def CountProperties(self, pcProperties: PULONG) -> int: ...

	@virtual_table.com_function(ULONG, ULONG, PTR(PROPBAG2), PULONG)
	def GetPropertyInfo(self, iProperty: int, cProperties: int, pPropBag: IPointer[PROPBAG2], pcProperties: PULONG) -> int: ...

	@virtual_table.com_function(LPCOLESTR, DWORD, LPUNKNOWN, PTR(IErrorLog))
	def LoadObject(self, pstrName: LPCOLESTR, dwHint: int, pUnkObject: IPointer[IUnknown], pErrLog: IPointer[IErrorLog]) -> int: ...

	virtual_table.build()

LPPROPERTYBAG2 = IPropertyBag2.PTR()

class IPersistPropertyBag2(IPersist):
	virtual_table = COMVirtualTable.from_ancestor(IPersist)
	_iid_ = IID("{22F55881-280B-11d0-A8A9-00A0C90C2004}")

	@virtual_table.com_function()
	def InitNew(self) -> int: ...

	@virtual_table.com_function(PTR(IPropertyBag2), PTR(IErrorLog))
	def Load(self, pPropBag: IPointer[IPropertyBag2], pErrLog: IPointer[IErrorLog]) -> int: ...

	@virtual_table.com_function(PTR(IPropertyBag2), BOOL, BOOL)
	def Save(self, pPropBag: IPointer[IPropertyBag2], fClearDirty: bool, fSaveAllProperties: bool) -> int: ...

	@virtual_table.com_function()
	def IsDirty(self) -> int: ...

	virtual_table.build()

LPPERSISTPROPERTYBAG2 = IPersistPropertyBag2.PTR()

class IAdviseSinkEx(IAdviseSink):
	virtual_table = COMVirtualTable.from_ancestor(IAdviseSink)
	_iid_ = IID("{3AF24290-0C96-11CE-A0CF-00AA00600AB8}")

	@virtual_table.com_function(DWORD)
	def OnViewStatusChange(self, dwViewStatus: int) -> int: ...

	virtual_table.build()

LPADVISESINKEX = IAdviseSinkEx.PTR()

# }
