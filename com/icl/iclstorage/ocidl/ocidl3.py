# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:35:25 2026
# Generated from ICL: ocidl3.icl
# {
class IOleControl(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B288-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(LPCONTROLINFO)
	def GetControlInfo(self, pCI: IPointer[CONTROLINFO]) -> int: ...

	@virtual_table.com_function(PMSG)
	def OnMnemonic(self, pMsg: IPointer[MSG]) -> int: ...

	@virtual_table.com_function(DISPID)
	def OnAmbientPropertyChange(self, dispID: DISPID) -> int: ...

	@virtual_table.com_function(BOOL)
	def FreezeEvents(self, bFreeze: bool) -> int: ...

	virtual_table.build()

LPOLECONTROL = IOleControl.PTR()

# }
