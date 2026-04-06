# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:44:20 2026
# Generated from ICL: ocidl6.icl
# {
class IPropertyPageSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B28C-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(DWORD)
	def OnStatusChange(self, dwFlags: int) -> int: ...

	@virtual_table.com_function(PTR(LCID))
	def GetLocaleID(self, pLocaleID: IPointer[LCID]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IUnknown))
	def GetPageContainer(self, ppUnk: IDoublePtr[IUnknown]) -> int: ...

	@virtual_table.com_function(PMSG)
	def TranslateAccelerator(self, pMsg: IPointer[MSG]) -> int: ...

	virtual_table.build()

LPPROPERTYPAGESITE = IPropertyPageSite.PTR()

class IPropertyNotifySink(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{9BFBBC02-EFF1-101A-84ED-00AA00341D07}")

	@virtual_table.com_function(DISPID)
	def OnChanged(self, dispID: DISPID) -> int: ...

	@virtual_table.com_function(DISPID)
	def OnRequestEdit(self, dispID: DISPID) -> int: ...

	virtual_table.build()

LPPROPERTYNOTIFYSINK = IPropertyNotifySink.PTR()

# }
