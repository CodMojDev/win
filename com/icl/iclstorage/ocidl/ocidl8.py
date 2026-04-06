# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 17:50:23 2026
# Generated from ICL: ocidl8.icl
# {
class IViewObjectEx(IViewObject2):
	virtual_table = COMVirtualTable.from_ancestor(IViewObject2)
	_iid_ = IID("{3AF24292-0C96-11CE-A0CF-00AA00600AB8}")

	@virtual_table.com_function(DWORD, LPRECTL)
	def GetRect(self, dwAspect: int, pRect: LPRECTL) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetViewStatus(self, pdwStatus: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD, LPCRECT, POINT, LONG, PDWORD)
	def QueryHitPoint(self, dwAspect: int, pRectBounds: LPCRECT, ptlLoc: POINT, lCloseHint: int, pHitResult: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD, LPCRECT, LPCRECT, LONG, PDWORD)
	def QueryHitRect(self, dwAspect: int, pRectBounds: LPCRECT, pRectLoc: LPCRECT, lCloseHint: int, pHitResult: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD, LONG, PTR(DVTARGETDEVICE), HDC, PTR(DVEXTENTINFO), LPSIZEL)
	def GetNaturalExtent(self, dwAspect: int, lindex: int, ptd: IPointer[DVTARGETDEVICE], hicTargetDev: HDC, pExtentInfo: IPointer[DVEXTENTINFO], pSizel: LPSIZEL) -> int: ...

	virtual_table.build()

LPVIEWOBJECTEX = IViewObjectEx.PTR()

class IOleUndoUnit(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{894AD3B0-EF97-11CE-9BC9-00AA00608E01}")

	@virtual_table.com_function(PVOID)
	def Do(self, pUndoManager: IPointer['IOleUndoManager']) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetDescription(self, pBstr: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPCLSID, PLONG)
	def GetUnitType(self, pClsid: IPointer[CLSID], plID: PLONG) -> int: ...

	@virtual_table.com_function()
	def OnNextAdd(self) -> int: ...

	virtual_table.build()

LPOLEUNDOUNIT = IOleUndoUnit.PTR()

class IOleParentUndoUnit(IOleUndoUnit):
	virtual_table = COMVirtualTable.from_ancestor(IOleUndoUnit)
	_iid_ = IID("{A1FAF330-EF97-11CE-9BC9-00AA00608E01}")

	@virtual_table.com_function(PVOID)
	def Open(self, pPUU: IPointer['IOleParentUndoUnit']) -> int: ...

	@virtual_table.com_function(PVOID, BOOL)
	def Close(self, pPUU: IPointer['IOleParentUndoUnit'], fCommit: bool) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def Add(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def FindUnit(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetParentState(self, pdwState: PDWORD) -> int: ...

	virtual_table.build()

LPOLEPARENTUNDOUNIT = IOleParentUndoUnit.PTR()

class IEnumOleUndoUnits(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B3E7C340-EF97-11CE-9BC9-00AA00608E01}")

	@virtual_table.com_function(ULONG, DOUBLE_PTR(IOleUndoUnit))
	def Next(self, cElt: int, rgElt: IDoublePtr[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(ULONG)
	def Skip(self, cElt: int) -> int: ...

	@virtual_table.com_function()
	def Reset(self) -> int: ...

	@virtual_table.com_function(PVOID)
	def Clone(self, ppEnum: IDoublePtr['IEnumOleUndoUnits']) -> int: ...

	virtual_table.build()

LPENUMOLEUNDOUNITS = IEnumOleUndoUnits.PTR()

class IOleUndoManager(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{D001F200-EF97-11CE-9BC9-00AA00608E01}")

	@virtual_table.com_function(PTR(IOleParentUndoUnit))
	def Open(self, pPUU: IPointer[IOleParentUndoUnit]) -> int: ...

	@virtual_table.com_function(PTR(IOleParentUndoUnit), BOOL)
	def Close(self, pPUU: IPointer[IOleParentUndoUnit], fCommit: bool) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def Add(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetOpenParentState(self, pdwState: PDWORD) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def DiscardFrom(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def UndoTo(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(PTR(IOleUndoUnit))
	def RedoTo(self, pUU: IPointer[IOleUndoUnit]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IEnumOleUndoUnits))
	def EnumUndoable(self, ppEnum: IDoublePtr[IEnumOleUndoUnits]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IEnumOleUndoUnits))
	def EnumRedoable(self, ppEnum: IDoublePtr[IEnumOleUndoUnits]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetLastUndoDescription(self, pBstr: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetLastRedoDescription(self, pBstr: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(BOOL)
	def Enable(self, fEnable: bool) -> int: ...

	virtual_table.build()

LPOLEUNDOMANAGER = IOleUndoManager.PTR()

POINTERINACTIVE_ACTIVATEONENTRY = 1
POINTERINACTIVE_DEACTIVATEONLEAVE = 2
POINTERINACTIVE_ACTIVATEONDRAG = 4
POINTERINACTIVE = INT

class IPointerInactive(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{55980BA0-35AA-11CF-B671-00AA004CD6D8}")

	@virtual_table.com_function(PDWORD)
	def GetActivationPolicy(self, pdwPolicy: PDWORD) -> int: ...

	@virtual_table.com_function(LPCRECT, LONG, LONG, DWORD)
	def OnInactiveMouseMove(self, pRectBounds: LPCRECT, x: int, y: int, grfKeyState: int) -> int: ...

	@virtual_table.com_function(LPCRECT, LONG, LONG, DWORD, BOOL)
	def OnInactiveSetCursor(self, pRectBounds: LPCRECT, x: int, y: int, dwMouseArg: int, fSetAlways: bool) -> int: ...

	virtual_table.build()

LPPOINTERINACTIVE = IPointerInactive.PTR()

class IObjectWithSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{FC4801A3-2BA9-11CF-A229-00AA003D7352}")

	@virtual_table.com_function(LPUNKNOWN)
	def SetSite(self, pUnkSite: IPointer[IUnknown]) -> int: ...

	@virtual_table.com_function(LPIID, PVOID, PVOID, intermediate_method = True)
	def GetSite(self, iid: IID, ppvSite: IPointer[PVOID], **kwargs) -> int:
		return self.virt_delegate(iid.ref(), ppvSite)

	virtual_table.build()

LPOBJECTWITHSITE = IObjectWithSite.PTR()

# }
