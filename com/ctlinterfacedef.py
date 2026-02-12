#
# ctlinterfacedef.py
#

from .autointerfacedef import *
from .servprovdef import *

UAS_NORMAL	= 0
UAS_BLOCKED	= 0x1
UAS_NOPARENTENABLE	= 0x2
UAS_MASK	= 0x3
UASFLAGS = INT

# State values for the DISPID_READYSTATE property
READYSTATE_UNINITIALIZED	= 0
READYSTATE_LOADING	= 1
READYSTATE_LOADED	= 2
READYSTATE_INTERACTIVE	= 3
READYSTATE_COMPLETE	= 4
READYSTATE = INT

class CONNECTDATA(CStructure):
    _fields_ = [
        ('pUnk', LPUNKNOWN),
        ('dwCookie', DWORD)
    ]
    
    pUnk: IPointer[IUnknown]
    dwCookie: int
    
LPCONNECTDATA = CONNECTDATA.PTR()

class IEnumConnections(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IEnumConnections')
    _iid_ = IID('{B196B287-BAB4-101A-B69C-00AA00341D07}')
    
    @virtual_table.com_function(ULONG, LPCONNECTDATA, PULONG)
    def Next(self, cConnections: int,
             rgcd: IPointer[CONNECTDATA],
             pcFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, cConnections: int) -> int: ...
    
    @virtual_table.com_function()
    def Reset(self) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppEnum: IDoublePtr['IEnumConnections']) -> int: ...
    
    virtual_table.build()

LPENUMCONNECTIONS = IEnumConnections.PTR()
    
class IEnumConnectionPoints(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IEnumConnections')
    _iid_ = IID('{B196B285-BAB4-101A-B69C-00AA00341D07}')
    
    @virtual_table.com_function(ULONG, PVOID, PULONG)
    def Next(self, cConnections: int,
             ppCP: IPointer['IConnectionPoint'],
             pcFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, cConnections: int) -> int: ...
    
    @virtual_table.com_function()
    def Reset(self) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppEnum: IDoublePtr['IEnumConnectionPoints']) -> int: ...
    
    virtual_table.build()
    
LPENUMCONNECTIONPOINTS = IEnumConnectionPoints.PTR()
    
class IConnectionPointContainer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IConnectionPointContainer')
    _iid_ = IID('{B196B284-BAB4-101A-B69C-00AA00341D07}')
    
    @virtual_table.com_function(POINTER(LPENUMCONNECTIONS))
    def EnumConnectionPoints(self, ppEnum: IDoublePtr[IEnumConnections]) -> int: ...
    
    @virtual_table.com_function(REFIID, PVOID)
    def FindConnectionPoint(self, riid: IPointer[IID],
                            ppCP: IDoublePtr['IConnectionPoint']) -> int: ...
    
    virtual_table.build()

LPCONNECTIONPOINTCONTAINER = IConnectionPointContainer.PTR()
    
class IConnectionPoint(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IConnectionPoint')
    _iid_ = IID('{B196B286-BAB4-101A-B69C-00AA00341D07}')
    
    @virtual_table.com_function(LPIID)
    def GetConnectionInterface(self, pIID: IPointer[IID]) -> int: ...
    
    @virtual_table.com_function(POINTER(LPCONNECTIONPOINTCONTAINER))
    def GetConnectionPointContainer(self, ppCPC: IDoublePtr[IConnectionPointContainer]) -> int: ...
    
    @virtual_table.com_function(LPUNKNOWN, PDWORD)
    def Advise(self, pUnkSink: IPointer[IUnknown], pdwCookie: PDWORD) -> int: ...
    
    @virtual_table.com_function(DWORD)
    def Unadvise(self, dwCookie: int) -> int: ...
    
    @virtual_table.com_function(POINTER(LPENUMCONNECTIONS))
    def EnumConnections(self, ppEnum: IDoublePtr[IEnumConnections]) -> int: ...
    
    virtual_table.build()
    
LPCONNECTIONPOINT = IConnectionPoint.PTR()

class LICINFO(CStructure):
    _fields_ = [
        ('cbLicInfo', LONG),
        ('fRuntimeKeyAvail', BOOL),
        ('fLicVerified', BOOL)
    ]
    
    fRuntimeKeyAvail: int
    fLicVerified: int
    cbLicInfo: int
    
LPLICINFO = LICINFO.PTR()

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

GUIDKIND_DEFAULT_SOURCE_DISP_IID	= 1
GUIDKIND = INT

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:23:20 2026
# Generated from ICL: ocidl1.icl
# {
class IProvideClassInfo2(IProvideClassInfo):
	virtual_table = COMVirtualTable.from_ancestor(IProvideClassInfo)
	_iid_ = IID("{A6BC3AC0-DBAA-11CE-9DE3-00AA004BB851}")

	@virtual_table.com_function(DWORD, LPGUID)
	def GetGUID(self, dwGuidKind: int, pGUID: IPointer[GUID]) -> int: ...

	virtual_table.build()

LPPROVIDECLASSINFO2 = IProvideClassInfo2.PTR()

# }

MULTICLASSINFO_GETTYPEINFO           = 0x00000001
MULTICLASSINFO_GETNUMRESERVEDDISPIDS = 0x00000002
MULTICLASSINFO_GETIIDPRIMARY         = 0x00000004
MULTICLASSINFO_GETIIDSOURCE          = 0x00000008
TIFLAGS_EXTENDDISPATCHONLY           = 0x00000001

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:23:23 2026
# Generated from ICL: ocidl2.icl
# {
class IProvideMultipleClassInfo(IProvideClassInfo2):
	virtual_table = COMVirtualTable.from_ancestor(IProvideClassInfo2)
	_iid_ = IID("{A7ABA9C1-8983-11cf-8F20-00805F2CD064}")

	@virtual_table.com_function(PULONG)
	def GetMultiTypeInfoCount(self, pcti: PULONG) -> int: ...

	@virtual_table.com_function(ULONG, DWORD, DOUBLE_PTR(ITypeInfo), PDWORD, PULONG, LPIID, LPIID)
	def GetInfoOfIndex(self, iti: int, dwFlags: int, pptiCoClass: IDoublePtr[ITypeInfo], pdwTIFlags: PDWORD, pcdispidReserved: PULONG, piidPrimary: IPointer[IID], piidSource: IPointer[IID]) -> int: ...

	virtual_table.build()

LPPROVIDEMULTIPLECLASSINFO = IProvideMultipleClassInfo.PTR()

# }

class CONTROLINFO(CStructure):
    _fields_ = [
        ('cb', ULONG),
        ('hAccel', HACCEL),
        ('cAccel', USHORT),
        ('dwFlags', DWORD)
    ]
    
    dwFlags: int
    hAccel: int
    cAccel: int
    cb: int

LPCONTROLINFO = CONTROLINFO.PTR()

CTRLINFO_EATS_RETURN	= 1
CTRLINFO_EATS_ESCAPE	= 2
CTRLINFO = INT

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

class POINTF(CStructure):
    _fields_ = [ ('x', FLOAT), ('y', FLOAT) ]
    
    x: float; y: float
    
LPPOINTF = POINTF.PTR()

XFORMCOORDS_POSITION	= 0x1
XFORMCOORDS_SIZE	= 0x2
XFORMCOORDS_HIMETRICTOCONTAINER	= 0x4
XFORMCOORDS_CONTAINERTOHIMETRIC	= 0x8
XFORMCOORDS_EVENTCOMPAT	= 0x10
XFORMCOORDS = INT

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:35:46 2026
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

class PROPPAGEINFO(CStructure):
    _fields_ = [
        ('cb', ULONG),
        ('pszTitle', LPOLESTR),
        ('size', SIZE),
        ('pszDocString', LPOLESTR),
        ('pszHelpFile', LPOLESTR),
        ('dwHelpContext', DWORD)
    ]
    
    pszDocString: LPOLESTR
    pszHelpFile: LPOLESTR
    dwHelpContext: int
    pszTitle: LPOLESTR
    size: SIZE
    cb: int
    
LPPROPPAGEINFO = PROPPAGEINFO.PTR()

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

PROPPAGESTATUS_DIRTY	= 0x1
PROPPAGESTATUS_VALIDATE	= 0x2
PROPPAGESTATUS_CLEAN	= 0x4
PROPPAGESTATUS = INT

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

class CAUUID(CStructure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', PGUID)
    ]
    
    pElems: IPointer[GUID]
    cElems: ULONG
    
LPCAUUID = CAUUID.PTR()

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

VIEWSTATUS_OPAQUE	= 1
VIEWSTATUS_SOLIDBKGND	= 2
VIEWSTATUS_DVASPECTOPAQUE	= 4
VIEWSTATUS_DVASPECTTRANSPARENT	= 8
VIEWSTATUS_SURFACE	= 16
VIEWSTATUS_3DSURFACE	= 32
VIEWSTATUS = INT

HITRESULT_OUTSIDE	= 0
HITRESULT_TRANSPARENT	= 1
HITRESULT_CLOSE	= 2
HITRESULT_HIT	= 3
HITRESULT = INT

DVASPECT_OPAQUE	= 16
DVASPECT_TRANSPARENT	= 32
DVASPECT2 = INT

class DVEXTENTINFO(CStructure):
    _fields_ = [
        ('cb', ULONG),
        ('dwExtentMode', DWORD),
        ('sizelProposed', SIZEL)
    ]
    
    sizelProposed: SIZEL
    dwExtentMode: int
    cb: int

DVEXTENT_CONTENT	= 0
DVEXTENT_INTEGRAL	= ( DVEXTENT_CONTENT + 1 ) 
DVEXTENTMODE = INT

DVASPECTINFOFLAG_CANOPTIMIZE	= 1
DVASPECTINFOFLAG = INT

class DVASPECTINFO(CStructure):
    _fields_ = [
        ('cb', ULONG),
        ('dwFlags', DWORD)
    ]
    
    dwFlags: int
    cb: int
    
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

class CALPOLESTR(CStructure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', PTR(LPOLESTR))
    ]
    
    pElems: IPointer[LPOLESTR]
    cElems: int
    
LPCALPOLESTR = CALPOLESTR.PTR()

class CADWORD(CStructure):
    _fields_ = [
        ('cElems', ULONG),
        ('pElems', PDWORD)
    ]
    
    pElems: PDWORD
    cElems: int
    
LPCADWORD = CADWORD.PTR()

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 17:55:57 2026
# Generated from ICL: ocidl9.icl
# {
class IPerPropertyBrowsing(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{376BD3AA-3845-101B-84ED-08002B2EC713}")

	@virtual_table.com_function(DISPID, PTR(BSTR))
	def GetDisplayString(self, dispID: DISPID, pBstr: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(DISPID, LPCLSID)
	def MapPropertyToPage(self, dispID: DISPID, pClsid: IPointer[CLSID]) -> int: ...

	@virtual_table.com_function(DISPID, LPCALPOLESTR, LPCADWORD)
	def GetPredefinedStrings(self, dispID: DISPID, pCaStringsOut: IPointer[CALPOLESTR], pCaCookiesOut: IPointer[CADWORD]) -> int: ...

	@virtual_table.com_function(DISPID, DWORD, LPVARIANT)
	def GetPredefinedValue(self, dispID: DISPID, dwCookie: int, pVarOut: IPointer[VARIANT]) -> int: ...

	virtual_table.build()

LPPERPROPERTYBROWSING = IPerPropertyBrowsing.PTR()

# }

PROPBAG2_TYPE_UNDEFINED	= 0
PROPBAG2_TYPE_DATA	= 1
PROPBAG2_TYPE_URL	= 2
PROPBAG2_TYPE_OBJECT	= 3
PROPBAG2_TYPE_STREAM	= 4
PROPBAG2_TYPE_STORAGE	= 5
PROPBAG2_TYPE_MONIKER	= 6
PROPBAG2_TYPE = INT

class PROPBAG2(CStructure):
    _fields_ = [
        ('dwType', DWORD),
        ('vt', VARTYPE),
        ('cfType', CLIPFORMAT),
        ('dwHint', DWORD),
        ('pstrName', LPOLESTR),
        ('clsid', CLSID)
    ]
    
    pstrName: LPOLESTR
    clsid: CLSID
    cfType: int
    dwHint: int
    dwType: int
    vt: int
    
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

QACONTAINER_SHOWHATCHING	= 0x1
QACONTAINER_SHOWGRABHANDLES	= 0x2
QACONTAINER_USERMODE	= 0x4
QACONTAINER_DISPLAYASDEFAULT	= 0x8
QACONTAINER_UIDEAD	= 0x10
QACONTAINER_AUTOCLIP	= 0x20
QACONTAINER_MESSAGEREFLECT	= 0x40
QACONTAINER_SUPPORTSMNEMONICS	= 0x80
QACONTAINERFLAGS = INT

OLE_COLOR = DWORD

class QACONTAINER(CStructure):
    _fields_ = [
        ('cbSize', ULONG),
        ('pClientSite', LPOLECLIENTSITE),
        ('pAdviseSink', LPADVISESINKEX),
        ('pPropertyNotifySink', LPPROPERTYNOTIFYSINK),
        ('pUnkEventSink', LPUNKNOWN),
        ('dwAmbientFlags', DWORD),
        ('colorFore', OLE_COLOR),
        ('colorBack', OLE_COLOR),
        ('pFont', LPFONT),
        ('pUndoMgr', LPOLEUNDOMANAGER),
        ('dwAppearance', DWORD),
        ('lcid', LONG),
        ('hpal', HPALETTE),
        ('pBindHost', PVOID), # urlmon is not implemented now
        ('pOleControlSite', LPOLECONTROLSITE),
        ('pServiceProvider', LPSERVICEPROVIDER)
    ]
    
    pPropertyNotifySink: IPointer[IPropertyNotifySink]
    pServiceProvider: IPointer[IServiceProvider]
    pOleControlSite: IPointer[IOleControlSite]
    pClientSite: IPointer[IOleClientSite]
    pAdviseSink: IPointer[IAdviseSinkEx]
    pUndoMgr: IPointer[IOleUndoManager]
    pUnkEventSink: IPointer[IUnknown]
    pFont: IPointer[IFont]
    dwAmbientFlags: int
    dwAppearance: int
    pBindHost: PVOID
    colorFore: int
    colorBack: int
    cbSize: int
    lcid: int
    hpal: int

class QACONTROL(CStructure):
    _fields_ = [
        ('cbSize', ULONG),
        ('dwMiscStatus', DWORD),
        ('dwViewStatus', DWORD),
        ('dwEventCookie', DWORD),
        ('dwPropNotifyCookie', DWORD),
        ('dwPointerActivationPolicy', DWORD)
    ]
    
    dwPointerActivationPolicy: int
    dwPropNotifyCookie: int
    dwEventCookie: int
    dwViewStatus: int
    dwMiscStatus: int
    cbSize: int
    
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
