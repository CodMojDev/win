# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 17:18:53 2026
# Generated from ICL: ocidl7.icl
# {
class ISpecifyPropertyPages(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{B196B28B-BAB4-101A-B69C-00AA00341D07}")

	@virtual_table.com_function(LPCAUUID)
	def GetPages(self, pPages: IPointer[CAUUID]) -> int: ...

	virtual_table.build()

LPSPECIFYPROPERTYPAGES = ISpecifyPropertyPages.PTR()

class IPersistMemory(IPersist):
	virtual_table = COMVirtualTable.from_ancestor(IPersist)
	_iid_ = IID("{BD1AE5E0-A6AE-11CE-BD37-504200C10000}")

	@virtual_table.com_function()
	def IsDirty(self) -> int: ...

	@virtual_table.com_function(LPVOID, ULONG)
	def Load(self, pMem: LPVOID, cbSize: int) -> int: ...

	@virtual_table.com_function(LPVOID, BOOL, ULONG)
	def Save(self, pMem: LPVOID, fClearDirty: bool, cbSize: int) -> int: ...

	@virtual_table.com_function(PULONG)
	def GetSizeMax(self, pCbSize: PULONG) -> int: ...

	@virtual_table.com_function()
	def InitNew(self) -> int: ...

	virtual_table.build()

LPPERSISTMEMORY = IPersistMemory.PTR()

class IPersistStreamInit(IPersist):
	virtual_table = COMVirtualTable.from_ancestor(IPersist)
	_iid_ = IID("{7FD52380-4E07-101B-AE2D-08002B2EC713}")

	@virtual_table.com_function()
	def IsDirty(self) -> int: ...

	@virtual_table.com_function(LPSTREAM)
	def Load(self, pStm: IPointer[IStream]) -> int: ...

	@virtual_table.com_function(LPSTREAM, BOOL)
	def Save(self, pStm: IPointer[IStream], fClearDirty: bool) -> int: ...

	@virtual_table.com_function(PULARGE_INTEGER)
	def GetSizeMax(self, pCbSize: IPointer[ULARGE_INTEGER]) -> int: ...

	@virtual_table.com_function()
	def InitNew(self) -> int: ...

	virtual_table.build()

LPPERSISTSTREAMINIT = IPersistStreamInit.PTR()

class IPersistPropertyBag(IPersist):
	virtual_table = COMVirtualTable.from_ancestor(IPersist)
	_iid_ = IID("{37D84F60-42CB-11CE-8135-00AA004BB851}")

	@virtual_table.com_function()
	def InitNew(self) -> int: ...

	@virtual_table.com_function(PTR(IPropertyBag), PTR(IErrorLog))
	def Load(self, pPropBag: IPointer[IPropertyBag], pErrorLog: IPointer[IErrorLog]) -> int: ...

	@virtual_table.com_function(PTR(IPropertyBag), BOOL, BOOL)
	def Save(self, pPropBag: IPointer[IPropertyBag], fClearDirty: bool, fSaveAllProperties: bool) -> int: ...

	virtual_table.build()

LPPERSISTPROPERTYBAG = IPersistPropertyBag.PTR()

class ISimpleFrameSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{742B0E01-14E6-101B-914E-00AA00300CAB}")

	@virtual_table.com_function(HWND, UINT, WPARAM, LPARAM, PTR(LRESULT), PDWORD)
	def PreMessageFilter(self, hWnd: HWND, msg: int, wp: int, lp: int, plResult: IPointer[LRESULT], pdwCookie: PDWORD) -> int: ...

	@virtual_table.com_function(HWND, UINT, WPARAM, LPARAM, PTR(LRESULT), DWORD)
	def PostMessageFilter(self, hWnd: HWND, msg: int, wp: int, lp: int, plResult: IPointer[LRESULT], dwCookie: int) -> int: ...

	virtual_table.build()

LPSIMPLEFRAMESITE = ISimpleFrameSite.PTR()

TEXTMETRICOLE = TEXTMETRICW
LPTEXTMETRICOLE = LPTEXTMETRICW

class IFont(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{BEF6E002-A874-101A-8BBA-00AA00300CAB}")

	@virtual_table.com_function(PTR(BSTR))
	def get_Name(self, pNmae: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(BSTR)
	def put_Name(self, name: BSTR) -> int: ...

	@virtual_table.com_function(LPCY)
	def get_Size(self, pSize: IPointer[CY]) -> int: ...

	@virtual_table.com_function(CY)
	def put_Size(self, size: CY) -> int: ...

	@virtual_table.com_function(PBOOL)
	def get_Bold(self, pBold: PBOOL) -> int: ...

	@virtual_table.com_function(BOOL)
	def put_bold(self, bold: bool) -> int: ...

	@virtual_table.com_function(PBOOL)
	def get_Italic(self, pItalic: PBOOL) -> int: ...

	@virtual_table.com_function(BOOL)
	def put_Italic(self, italic: bool) -> int: ...

	@virtual_table.com_function(PBOOL)
	def get_Underline(self, pUnderline: PBOOL) -> int: ...

	@virtual_table.com_function(BOOL)
	def put_Underline(self, underline: bool) -> int: ...

	@virtual_table.com_function(PBOOL)
	def get_Strikethrough(self, pStrikethrough: PBOOL) -> int: ...

	@virtual_table.com_function(BOOL)
	def put_Strikethrough(self, strikethrough: bool) -> int: ...

	@virtual_table.com_function(PSHORT)
	def get_Weight(self, pWeight: PSHORT) -> int: ...

	@virtual_table.com_function(SHORT)
	def put_Weight(self, weight: int) -> int: ...

	@virtual_table.com_function(PSHORT)
	def get_Charset(self, pCharset: PSHORT) -> int: ...

	@virtual_table.com_function(SHORT)
	def put_Charset(self, charset: int) -> int: ...

	@virtual_table.com_function(PTR(HFONT))
	def get_hFont(self, phFont: IPointer[HFONT]) -> int: ...

	@virtual_table.com_function(PVOID)
	def Clone(self, ppFont: IDoublePtr['IFont']) -> int: ...

	@virtual_table.com_function(PVOID)
	def IsEqual(self, pFontOther: IPointer['IFont']) -> int: ...

	@virtual_table.com_function(LONG, LONG)
	def SetRatio(self, cyLogical: int, cyHimetric: int) -> int: ...

	@virtual_table.com_function(PTR(TEXTMETRICOLE))
	def QueryTextMetrics(self, pTM: IPointer[TEXTMETRICOLE]) -> int: ...

	@virtual_table.com_function(HFONT)
	def AddRefHfont(self, hFont: HFONT) -> int: ...

	@virtual_table.com_function(HFONT)
	def ReleaseHfont(self, hFont: HFONT) -> int: ...

	@virtual_table.com_function(HDC)
	def SetHdc(self, hDC: HDC) -> int: ...

	virtual_table.build()

LPFONT = IFont.PTR()

PICTURE_SCALABLE = 0x1
PICTURE_TRANSPARENT = 0x2
PICTUREATTRIBUTES = INT

OLE_HANDLE = UINT
OLE_XPOS_HIMETRIC = LONG
OLE_YPOS_HIMETRIC = LONG
OLE_XSIZE_HIMETRIC = LONG
OLE_YSIZE_HIMETRIC = LONG

class IPicture(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{7BF80980-BF32-101A-8BBB-00AA00300CAB}")

	@virtual_table.com_function(PTR(OLE_HANDLE))
	def get_Handle(self, pHandle: IPointer[OLE_HANDLE]) -> int: ...

	@virtual_table.com_function(PTR(OLE_HANDLE))
	def get_hPal(self, phPal: IPointer[OLE_HANDLE]) -> int: ...

	@virtual_table.com_function(PSHORT)
	def get_Type(self, pType: PSHORT) -> int: ...

	@virtual_table.com_function(PTR(OLE_XSIZE_HIMETRIC))
	def get_Width(self, pWidth: IPointer[OLE_XSIZE_HIMETRIC]) -> int: ...

	@virtual_table.com_function(PTR(OLE_YSIZE_HIMETRIC))
	def get_Height(self, pHeight: IPointer[OLE_YSIZE_HIMETRIC]) -> int: ...

	@virtual_table.com_function(HDC, LONG, LONG, LONG, LONG, OLE_XPOS_HIMETRIC, OLE_YPOS_HIMETRIC, OLE_XSIZE_HIMETRIC, OLE_YSIZE_HIMETRIC, LPCRECT)
	def Render(self, hDC: HDC, x: int, y: int, cx: int, cy: int, xSrc: OLE_XPOS_HIMETRIC, ySrc: OLE_YPOS_HIMETRIC, cxSrc: OLE_XSIZE_HIMETRIC, cySrc: OLE_YSIZE_HIMETRIC, pRcWBounds: LPCRECT) -> int: ...

	@virtual_table.com_function(OLE_HANDLE)
	def set_hPal(self, hPal: OLE_HANDLE) -> int: ...

	@virtual_table.com_function(PTR(HDC))
	def get_CurDC(self, phDC: IPointer[HDC]) -> int: ...

	@virtual_table.com_function(HDC, PTR(HDC), PTR(OLE_HANDLE))
	def SelectPicture(self, hDCIn: HDC, phDCOut: IPointer[HDC], phBmpOut: IPointer[OLE_HANDLE]) -> int: ...

	@virtual_table.com_function(PBOOL)
	def get_KeepOriginalFormat(self, pKeep: PBOOL) -> int: ...

	@virtual_table.com_function(BOOL)
	def put_KeepOriginalFormat(self, keep: bool) -> int: ...

	@virtual_table.com_function()
	def PictureChanged(self) -> int: ...

	@virtual_table.com_function(LPSTREAM, BOOL, PLONG)
	def SaveAsFile(self, pStream: IPointer[IStream], fSaveMemCopy: bool, pCbSize: PLONG) -> int: ...

	@virtual_table.com_function(PDWORD)
	def get_Attributes(self, pDwAttr: PDWORD) -> int: ...

	virtual_table.build()

LPPICTURE = IPicture.PTR()

HHANDLE = UINT_PTR

class IPicture2(IPicture):
	virtual_table = COMVirtualTable.from_ancestor(IPicture)
	_iid_ = IID("{F5185DD8-2012-4b0b-AAD9-F052C6BD482B}")
	virtual_table.build()

LPPICTURE2 = IPicture2.PTR()

class IFontEventsDisp(IDispatch):
	virtual_table = COMVirtualTable.from_ancestor(IDispatch)
	_iid_ = IID("{4EF6100A-AF88-11D0-9846-00C04FC29993}")
	virtual_table.build()

LPFONTEVENTS = IFontEventsDisp.PTR()

class IFontDisp(IDispatch):
	virtual_table = COMVirtualTable.from_ancestor(IDispatch)
	_iid_ = IID("{BEF6E003-A874-101A-8BBA-00AA00300CAB}")
	virtual_table.build()

LPFONTDISP = IFontDisp.PTR()

class IPictureDisp(IDispatch):
	virtual_table = COMVirtualTable.from_ancestor(IDispatch)
	_iid_ = IID("{7BF80981-BF32-101A-8BBB-00AA00300CAB}")
	virtual_table.build()

LPPICTUREDISP = IPictureDisp.PTR()

class IOleInPlaceObjectWindowless(IOleInPlaceObject):
	virtual_table = COMVirtualTable.from_ancestor(IOleInPlaceObject)
	_iid_ = IID("{1C2056CC-5EF4-101B-8BC8-00AA003E3B29}")

	@virtual_table.com_function(UINT, WPARAM, LPARAM, PTR(LRESULT))
	def OnWindowMessage(self, msg: int, wParam: int, lParam: int, plResult: IPointer[LRESULT]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IDropTarget))
	def GetDropTarget(self, ppDropTarget: IDoublePtr[IDropTarget]) -> int: ...

	virtual_table.build()

LPOLEINPLACEOBJECTWINDOWLESS = IOleInPlaceObjectWindowless.PTR()

ACTIVATE_WINDOWLESS = 1
ACTIVATEFLAGS = INT

class IOleInPlaceSiteEx(IOleInPlaceSite):
	virtual_table = COMVirtualTable.from_ancestor(IOleInPlaceSite)
	_iid_ = IID("{9C2CAD80-3424-11CF-B670-00AA004CD6D8}")

	@virtual_table.com_function(PBOOL, DWORD)
	def OnInPlaceActivateEx(self, pfNoRedraw: PBOOL, dwFlags: int) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnInPlaceDeactivateEx(self, fNoRedraw: bool) -> int: ...

	@virtual_table.com_function()
	def RequestUIActivate(self) -> int: ...

	virtual_table.build()

LPOLEINPLACESITEEX = IOleInPlaceSiteEx.PTR()

OLEDC_NODRAW = 0x1
OLEDC_PAINTBKGND = 0x2
OLEDC_OFFSCREEN = 0x4
OLEDCFLAGS = INT

class IOleInPlaceSiteWindowless(IOleInPlaceSiteEx):
	virtual_table = COMVirtualTable.from_ancestor(IOleInPlaceSiteEx)
	_iid_ = IID("{922EADA0-3424-11CF-B670-00AA004CD6D8}")

	@virtual_table.com_function()
	def CanWindowlessActivate(self) -> int: ...

	@virtual_table.com_function()
	def GetCapture(self) -> int: ...

	@virtual_table.com_function(BOOL)
	def SetCapture(self, fCapture: bool) -> int: ...

	@virtual_table.com_function()
	def GetFocus(self) -> int: ...

	@virtual_table.com_function(BOOL)
	def SetFocus(self, fFocus: bool) -> int: ...

	@virtual_table.com_function(LPCRECT, DWORD, PTR(HDC))
	def GetDC(self, pRect: LPCRECT, grfFlags: int, phDC: IPointer[HDC]) -> int: ...

	@virtual_table.com_function(HDC)
	def ReleaseDC(self, hDC: HDC) -> int: ...

	@virtual_table.com_function(LPCRECT, BOOL)
	def InvalidateRect(self, pRect: LPCRECT, fErase: bool) -> int: ...

	@virtual_table.com_function(HRGN, BOOL)
	def InvalidateRgn(self, hRGN: HRGN, fErase: bool) -> int: ...

	@virtual_table.com_function(INT, INT, LPCRECT, LPCRECT)
	def ScrollRect(self, dx: int, dy: int, pRectScroll: LPCRECT, pRectClip: LPCRECT) -> int: ...

	@virtual_table.com_function(LPRECT)
	def AdjustRect(self, prc: LPRECT) -> int: ...

	@virtual_table.com_function(UINT, WPARAM, LPARAM, PTR(LRESULT))
	def OnDefWindowMessage(self, msg: int, wParam: int, lParam: int, plResult: IPointer[LRESULT]) -> int: ...

	virtual_table.build()

LPOLEINPLACESITEWINDOWLESS = IOleInPlaceSiteWindowless.PTR()

# }
