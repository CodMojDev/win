# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 18:20:38 2026
# Generated from ICL: ocidl11.icl
# {
class IQuickActivate(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{CF51ED10-62FE-11CF-BF86-00A0C9034836}")

	@virtual_table.com_function(PTR(QACONTAINER), PTR(QACONTROL))
	def QuickActivate(self, pQaContainer: IPointer[QACONTAINER], pQaControl: IPointer[QACONTROL]) -> int: ...

	@virtual_table.com_function(LPSIZEL)
	def SetContentExtent(self, pSizel: LPSIZEL) -> int: ...

	@virtual_table.com_function(LPSIZEL)
	def GetContentExtent(self, pSizel: LPSIZEL) -> int: ...

	virtual_table.build()

LPQUICKACTIVATE = IQuickActivate.PTR()

# }
