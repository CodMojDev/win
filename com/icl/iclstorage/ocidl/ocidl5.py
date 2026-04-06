# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:41:43 2026
# Generated from ICL: ocidl5.icl
# {
class IPropertyPage(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B28D-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(PVOID)
	def SetPageSite(self, pPageSite: IPointer['IPropertyPageSite']) -> int: ...

	@virtual_table.com_function(HWND, LPCRECT, BOOL)
	def Activate(self, hWndParent: HWND, pRect: LPCRECT, bModal: bool) -> int: ...

	@virtual_table.com_function()
	def Deactivate(self) -> int: ...

	@virtual_table.com_function(PTR(PROPPAGEINFO))
	def GetPageInfo(self, pPageInfo: IPointer[PROPPAGEINFO]) -> int: ...

	@virtual_table.com_function(ULONG, DOUBLE_PTR(IUnknown))
	def SetObjects(self, cObjects: int, ppUnk: IDoublePtr[IUnknown]) -> int: ...

	@virtual_table.com_function(UINT)
	def Show(self, nCmdShow: int) -> int: ...

	@virtual_table.com_function(LPCRECT)
	def Move(self, pRect: LPCRECT) -> int: ...

	@virtual_table.com_function()
	def IsPageDirty(self) -> int: ...

	@virtual_table.com_function()
	def Apply(self) -> int: ...

	@virtual_table.com_function(LPCOLESTR)
	def Help(self, pszHelpDir: LPCOLESTR) -> int: ...

	@virtual_table.com_function(PMSG)
	def TranslateAccelerator(self, pMsg: IPointer[MSG]) -> int: ...

	virtual_table.build()

LPPROPERTYPAGE = IPropertyPage.PTR()

class IPropertyPage2(IPropertyPage):
	virtual_table = COMVirtualTable.from_ancestor(IPropertyPage)
	_iid_ = IID("{01E44665-24AC-101B-84ED-08002B2EC713}")

	@virtual_table.com_function(DISPID)
	def EditProperty(self, dispID: DISPID) -> int: ...

	virtual_table.build()

LPPROPERTYPAGE2 = IPropertyPage2.PTR()

# }
