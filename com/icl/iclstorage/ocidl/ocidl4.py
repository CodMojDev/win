# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:41:33 2026
# Generated from ICL: ocidl4.icl
# {
class IOleControlSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B289-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function()
	def OnControlInfoChanged(self) -> int: ...

	@virtual_table.com_function(BOOL)
	def LockInPlaceActive(self, fLock: bool) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IDispatch))
	def GetExtendedControl(self, ppDisp: IDoublePtr[IDispatch]) -> int: ...

	@virtual_table.com_function(PTR(POINTL), PTR(POINTF), DWORD)
	def TransformCoords(self, pPtlHimetric: IPointer[POINTL], pPtfContainer: IPointer[POINTF], dwFlags: int) -> int: ...

	@virtual_table.com_function(PMSG, DWORD)
	def TranslateAccelerator(self, pMsg: IPointer[MSG], grfModifiers: int) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnFocus(self, fGotFocus: bool) -> int: ...

	@virtual_table.com_function()
	def ShowPropertyFrame(self) -> int: ...

	virtual_table.build()

LPOLECONTROLSITE = IOleControlSite.PTR()

# }
