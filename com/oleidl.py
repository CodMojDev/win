#
# oleidl.py
# 
# File created by WICL generator version 1.00
# Creation timestamp: Sun Jan 11 17:08:12 2026
# Generated from ICL: oleidl.icl
#

from .objinterfacedef import *

class IOleAdviseHolder(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000111-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPADVISESINK, PDWORD)
	def Advise(self, pAdvise: IPointer[IAdviseSink], pdwConnection: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD)
	def Unadvise(self, dwConnection: int) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IEnumSTATDATA))
	def EnumAdvise(self, ppenumAdvise: IDoublePtr[IEnumSTATDATA]) -> int: ...

	@virtual_table.com_function(LPMONIKER)
	def SendOnRename(self, pmk: IPointer[IMoniker]) -> int: ...

	@virtual_table.com_function()
	def SendOnSave(self) -> int: ...

	@virtual_table.com_function()
	def SendOnClose(self) -> int: ...

	virtual_table.build()

LPOLEADVISEHOLDER = IOleAdviseHolder.PTR()

class IOleCache(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000011e-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPFORMATETC, DWORD, PDWORD)
	def Cache(self, pformatetc: IPointer[FORMATETC], advf: int, pdwConnection: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD)
	def Uncache(self, dwConnection: int) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IEnumSTATDATA))
	def EnumCache(self, ppenumSTATDATA: IDoublePtr[IEnumSTATDATA]) -> int: ...

	@virtual_table.com_function(LPDATAOBJECT)
	def InitCache(self, pDataObject: IPointer[IDataObject]) -> int: ...

	@virtual_table.com_function(LPFORMATETC, LPSTGMEDIUM, BOOL)
	def SetData(self, pformatetc: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM], fRelease: bool) -> int: ...

	virtual_table.build()

# Cache update Flags

UPDFCACHE_NODATACACHE   =       0x00000001
UPDFCACHE_ONSAVECACHE   =       0x00000002
UPDFCACHE_ONSTOPCACHE   =       0x00000004
UPDFCACHE_NORMALCACHE   =       0x00000008
UPDFCACHE_IFBLANK       =       0x00000010
UPDFCACHE_ONLYIFBLANK   =       0x80000000

UPDFCACHE_IFBLANKORONSAVECACHE = (UPDFCACHE_IFBLANK | UPDFCACHE_ONSAVECACHE)
UPDFCACHE_ALL = (DWORD((UPDFCACHE_ONLYIFBLANK)).value)
UPDFCACHE_ALLBUTNODATACACHE = (UPDFCACHE_ALL & (DWORD(UPDFCACHE_NODATACACHE).value))

# IOleCache2::DiscardCache options
DISCARDCACHE_SAVEIFDIRTY =  0  # Save all dirty cache before discarding
DISCARDCACHE_NOSAVE      =  1  # Don't save dirty caches before discarding
DISCARDCACHE = INT

class IOleCache2(IOleCache):
	virtual_table = COMVirtualTable.from_ancestor(IOleCache)
	_iid_ = IID("{00000128-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPDATAOBJECT, DWORD, LPVOID)
	def UpdateCache(self, pDataObject: IPointer[IDataObject], grfUpdf: int, pReserved: LPVOID) -> int: ...

	@virtual_table.com_function(DWORD)
	def DiscardCache(self, dwDiscardOptions: int) -> int: ...

	virtual_table.build()

LPOLECACHE = IOleCache2.PTR()

class IOleCacheControl(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000129-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPDATAOBJECT)
	def OnRun(self, pDataObject: IPointer[IDataObject]) -> int: ...

	@virtual_table.com_function()
	def OnStop(self) -> int: ...

	virtual_table.build()

LPOLECACHECONTROL = IOleCacheControl.PTR()

class IParseDisplayName(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000011a-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPBINDCTX, LPOLESTR, PULONG, DOUBLE_PTR(IMoniker))
	def ParseDisplayName(self, pbc: IPointer[IBindCtx], pszDisplayName: LPOLESTR, pchEaten: PULONG, ppmkOut: IDoublePtr[IMoniker]) -> int: ...

	virtual_table.build()

LPPARSEDISPLAYNAME = IParseDisplayName.PTR()

class IOleContainer(IParseDisplayName):
	virtual_table = COMVirtualTable.from_ancestor(IParseDisplayName)
	_iid_ = IID("{0000011b-0000-0000-C000-000000000046}")

	@virtual_table.com_function(DWORD, DOUBLE_PTR(IEnumUnknown))
	def EnumObjects(self, grfFlags: int, ppenum: IDoublePtr[IEnumUnknown]) -> int: ...

	@virtual_table.com_function(BOOL)
	def LockContainer(self, fLock: bool) -> int: ...

	virtual_table.build()

LPOLECONTAINER = IOleContainer.PTR()

class IOleClientSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000118-0000-0000-C000-000000000046}")

	@virtual_table.com_function()
	def SaveObject(self) -> int: ...

	@virtual_table.com_function(DWORD, DWORD, DOUBLE_PTR(IMoniker))
	def GetMoniker(self, dwAssign: int, dwWhichMoniker: int, ppmk: IDoublePtr[IMoniker]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IOleContainer))
	def GetContainer(self, ppContainer: IDoublePtr[IOleContainer]) -> int: ...

	@virtual_table.com_function()
	def ShowObject(self) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnShowWindow(self, fShow: bool) -> int: ...

	@virtual_table.com_function()
	def RequestNewObjectLayout(self) -> int: ...

	virtual_table.build()

LPOLECLIENTSITE = IOleClientSite.PTR()

OLEGETMONIKER_ONLYIFTHERE = 1
OLEGETMONIKER_FORCEASSIGN = 2
OLEGETMONIKER_UNASSIGN    = 3
OLEGETMONIKER_TEMPFORUSER = 4
OLEGETMONIKER = INT

OLEWHICHMK_CONTAINER = 1
OLEWHICHMK_OBJREL    = 2
OLEWHICHMK_OBJFULL   = 3
OLEWHICHMK = INT

USERCLASSTYPE_FULL    = 1
USERCLASSTYPE_SHORT   = 2
USERCLASSTYPE_APPNAME = 3
USERCLASSTYPE = INT

OLEMISC_RECOMPOSEONRESIZE           = 0x00000001
OLEMISC_ONLYICONIC                  = 0x00000002
OLEMISC_INSERTNOTREPLACE            = 0x00000004
OLEMISC_STATIC                      = 0x00000008
OLEMISC_CANTLINKINSIDE              = 0x00000010
OLEMISC_CANLINKBYOLE1               = 0x00000020
OLEMISC_ISLINKOBJECT                = 0x00000040
OLEMISC_INSIDEOUT                   = 0x00000080
OLEMISC_ACTIVATEWHENVISIBLE         = 0x00000100
OLEMISC_RENDERINGISDEVICEINDEPENDENT= 0x00000200
OLEMISC_INVISIBLEATRUNTIME          = 0x00000400
OLEMISC_ALWAYSRUN                   = 0x00000800
OLEMISC_ACTSLIKEBUTTON              = 0x00001000
OLEMISC_ACTSLIKELABEL               = 0x00002000
OLEMISC_NOUIACTIVATE                = 0x00004000
OLEMISC_ALIGNABLE                   = 0x00008000
OLEMISC_SIMPLEFRAME                 = 0x00010000
OLEMISC_SETCLIENTSITEFIRST          = 0x00020000
OLEMISC_IMEMODE                     = 0x00040000
OLEMISC_IGNOREACTIVATEWHENVISIBLE   = 0x00080000
OLEMISC_WANTSTOMENUMERGE            = 0x00100000
OLEMISC_SUPPORTSMULTILEVELUNDO      = 0x00200000
OLEMISC = INT

OLECLOSE_SAVEIFDIRTY = 0
OLECLOSE_NOSAVE      = 1
OLECLOSE_PROMPTSAVE  = 2
OLECLOSE = INT

class IOleObject(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000112-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PTR(IOleClientSite))
	def SetClientSite(self, pClientSite: IPointer[IOleClientSite]) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IOleClientSite))
	def GetClientSite(self, ppClientSite: IDoublePtr[IOleClientSite]) -> int: ...

	@virtual_table.com_function(LPCOLESTR, LPCOLESTR)
	def SetHostNames(self, szContainerApp: LPCOLESTR, szContainerObj: LPCOLESTR) -> int: ...

	@virtual_table.com_function(DWORD)
	def Close(self, dwSaveOption: int) -> int: ...

	@virtual_table.com_function(DWORD, LPMONIKER)
	def SetMoniker(self, dwWhichMoniker: int, pmk: IPointer[IMoniker]) -> int: ...

	@virtual_table.com_function(DWORD, DWORD, DOUBLE_PTR(IMoniker))
	def GetMoniker(self, dwAssign: int, dwWhichMoniker: int, ppmk: IDoublePtr[IMoniker]) -> int: ...

	@virtual_table.com_function(LPDATAOBJECT, BOOL, DWORD)
	def InitFromData(self, pDataObject: IPointer[IDataObject], fCreation: bool, dwReserved: int) -> int: ...

	@virtual_table.com_function(DWORD, DOUBLE_PTR(IDataObject))
	def GetClipboardData(self, dwReserved: int, ppDataObject: IDoublePtr[IDataObject]) -> int: ...

	@virtual_table.com_function(LONG, LPMSG, PTR(IOleClientSite), LONG, HWND, LPCRECT)
	def DoVerb(self, iVerb: int, lpmsg: LPMSG, pActiveSite: IPointer[IOleClientSite], lindex: int, hwndParent: HWND, lprcPosRect: LPCRECT) -> int: ...

	@virtual_table.com_function(PVOID)
	def EnumVerbs(self, ppEnumOleVerb: IDoublePtr['IEnumOLEVERB']) -> int: ...

	@virtual_table.com_function()
	def Update(self) -> int: ...

	@virtual_table.com_function()
	def IsUpToDate(self) -> int: ...

	@virtual_table.com_function(LPCLSID)
	def GetUserClassID(self, pClsid: IPointer[CLSID]) -> int: ...

	@virtual_table.com_function(DWORD, PTR(LPOLESTR))
	def GetUserType(self, dwFormOfType: int, pszUserType: IPointer[LPOLESTR]) -> int: ...

	@virtual_table.com_function(DWORD, PSIZEL)
	def SetExtent(self, dwDrawAspect: int, psizel: PSIZEL) -> int: ...

	@virtual_table.com_function(DWORD, PSIZEL)
	def GetExtent(self, dwDrawAspect: int, psizel: PSIZEL) -> int: ...

	@virtual_table.com_function(LPADVISESINK, PDWORD)
	def Advise(self, pAdvSink: IPointer[IAdviseSink], pdwConnection: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD)
	def Unadvise(self, dwConnection: int) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IEnumSTATDATA))
	def EnumAdvise(self, ppenumAdvise: IDoublePtr[IEnumSTATDATA]) -> int: ...

	@virtual_table.com_function(DWORD, PDWORD)
	def GetMiscStatus(self, dwAspect: int, pdwStatus: PDWORD) -> int: ...

	@virtual_table.com_function(LPLOGPALETTE)
	def SetColorScheme(self, pLogpal: IPointer[LOGPALETTE]) -> int: ...

	virtual_table.build()

LPOLEOBJECT = IOleObject.PTR()

###### OLE value types ###############################################

# rendering options
OLERENDER_NONE   = 0
OLERENDER_DRAW   = 1
OLERENDER_FORMAT = 2
OLERENDER_ASIS   = 3
OLERENDER = INT
LPOLERENDER = PINT

###### Clipboard Data structures #########################################

class OBJECTDESCRIPTOR(CStructure):
	_fields_ = [
		('cbSize', ULONG),		 		# Size of structure in bytes
		('clsid', CLSID),  	 		# CLSID of data being transferred
		('dwDrawAspect', DWORD), 		# Display aspect of the object
										# normally DVASPECT_CONTENT or ICON.
										# dwDrawAspect will be 0 (which is NOT
										# DVASPECT_CONTENT) if the copier or
										# dragsource didn't draw the object to
										# begin with.
		('sizel', SIZEL),		 		# size of the object in HIMETRIC
										# sizel is opt.: will be (0,0) for apps
										# which don't draw the object being
										# transferred
		('pointl', POINTL),		 		# Offset in HIMETRIC units from the
										# upper-left corner of the obj where the
										# mouse went down for the drag.
										# NOTE: y coordinates increase downward.
										#       x coordinates increase to right
										# pointl is opt.; it is only meaningful
										# if object is transfered via drag/drop.
										# (0, 0) if mouse position is unspecified
										# (eg. when obj transfered via clipboard)
		('dwStatus', DWORD),	 		# Misc. status flags for object. Flags are
										# defined by OLEMISC enum. these flags
										# are as would be returned
										# by IOleObject::GetMiscStatus.
		('dwFullUserTypeName', DWORD),  # Offset from beginning of structure to
										# null-terminated string that specifies
										# Full User Type Name of the object.
										# 0 indicates string not present.
		('dwSrcOfCopy', DWORD)			# Offset from beginning of structure to
										# null-terminated string that specifies
										# source of the transfer.
										# dwSrcOfCOpy is normally implemented as
										# the display name of the temp-for-user
										# moniker which identifies the source of
										# the data.
										# 0 indicates string not present.
										# NOTE: moniker assignment is NOT forced.
										# see IOleObject::GetMoniker(
										#             OLEGETMONIKER_TEMPFORUSER)
		# variable sized string data may appear here
	]

	dwFullUserTypeName: int
	dwDrawAspect: DVASPECT
	dwSrcOfCopy: int
	pointl: POINTL
	dwStatus: int
	sizel: SIZEL
	clsid: CLSID
	cbSize: int

POBJECTDESCRIPTOR = LPOBJECTDESCRIPTOR = \
PLINKSRCDESCRIPTOR = LPLINKSRCDESCRIPTOR = OBJECTDESCRIPTOR.PTR()
LINKSRCDESCRIPTOR = OBJECTDESCRIPTOR

class IOleWindow(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000114-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PTR(HWND))
	def GetWindow(self, phwnd: IPointer[HWND]) -> int: ...

	@virtual_table.com_function(BOOL)
	def ContextSensitiveHelp(self, fEnterMode: bool) -> int: ...

	virtual_table.build()

LPOLEWINDOW = IOleWindow.PTR()

# Link update options
OLEUPDATE_ALWAYS=1
OLEUPDATE_ONCALL=3
OLEUPDATE = INT
LPOLEUPDATE = POLEUPDATE = PINT
OLELINKBIND_EVENIFCLASSDIFF = 1
OLELINKBIND = INT

class IOleLink(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000011d-0000-0000-C000-000000000046}")

	@virtual_table.com_function(DWORD)
	def SetUpdateOptions(self, dwUpdateOpt: int) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetUpdateOptions(self, pdwUpdateOpt: PDWORD) -> int: ...

	@virtual_table.com_function(LPMONIKER, LPCLSID, intermediate_method = True)
	def SetSourceMoniker(self, pmk: IPointer[IMoniker], clsid: CLSID, **kwargs) -> int:
		return self.virt_delegate(pmk, clsid.ref())

	@virtual_table.com_function(DOUBLE_PTR(IMoniker))
	def GetSourceMoniker(self, ppmk: IDoublePtr[IMoniker]) -> int: ...

	@virtual_table.com_function(LPCOLESTR)
	def SetSourceDisplayName(self, pszStatusText: LPCOLESTR) -> int: ...

	@virtual_table.com_function(PTR(LPOLESTR))
	def GetSourceDisplayName(self, ppszDisplayName: IPointer[LPOLESTR]) -> int: ...

	@virtual_table.com_function(DWORD, LPBINDCTX)
	def BindToSource(self, bindflags: int, pbc: IPointer[IBindCtx]) -> int: ...

	@virtual_table.com_function()
	def BindIfRunning(self) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IUnknown))
	def GetBoundSource(self, ppunk: IDoublePtr[IUnknown]) -> int: ...

	@virtual_table.com_function()
	def UnbindSource(self) -> int: ...

	@virtual_table.com_function(LPBINDCTX)
	def Update(self, pbc: IPointer[IBindCtx]) -> int: ...

	virtual_table.build()

LPOLELINK = IOleLink.PTR()

BINDSPEED_INDEFINITE    = 1
BINDSPEED_MODERATE      = 2
BINDSPEED_IMMEDIATE     = 3
BINDSPEED = INT

OLECONTF_EMBEDDINGS     = 1
OLECONTF_LINKS          = 2
OLECONTF_OTHERS         = 4
OLECONTF_ONLYUSER       = 8
OLECONTF_ONLYIFRUNNING  = 16
OLECONTF = INT

class IOleItemContainer(IOleContainer):
	virtual_table = COMVirtualTable.from_ancestor(IOleContainer)
	_iid_ = IID("{0000011c-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPOLESTR, DWORD, LPBINDCTX, LPIID, PTR(PVOID), intermediate_method = True)
	def GetObject(self, pszItem: LPOLESTR, dwSpeedNeeded: int, pbc: IPointer[IBindCtx], iid: IID, ppvObject: PVOID, **kwargs) -> int:
		return self.virt_delegate(pszItem, dwSpeedNeeded, pbc, iid.ref(), ppvObject)

	@virtual_table.com_function(LPOLESTR, LPBINDCTX, LPIID, PTR(PVOID), intermediate_method = True)
	def GetObjectStorage(self, pszItem: LPOLESTR, pbc: IPointer[IBindCtx], iid: IID, ppvStorage: PVOID, **kwargs) -> int:
		return self.virt_delegate(pszItem, pbc, iid.ref(), ppvStorage)

	@virtual_table.com_function(LPOLESTR)
	def IsRunning(self, pszItem: LPOLESTR) -> int: ...

	virtual_table.build()

LPOLEITEMCONTAINER = IOleItemContainer.PTR()

BORDERWIDTHS = RECT
LPBORDERWIDTHS = LPCBORDERWIDTHS = PRECT

class IOleInPlaceUIWindow(IOleWindow):
	virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
	_iid_ = IID("{00000115-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPRECT)
	def GetBorder(self, lprectBorder: LPRECT) -> int: ...

	@virtual_table.com_function(LPBORDERWIDTHS)
	def RequestBorderSpace(self, pborderwidths: IPointer[BORDERWIDTHS]) -> int: ...

	@virtual_table.com_function(LPBORDERWIDTHS)
	def SetBorderSpace(self, pborderwidths: IPointer[BORDERWIDTHS]) -> int: ...

	@virtual_table.com_function(PVOID, LPCOLESTR)
	def SetActiveObject(self, pActiveObject: IPointer['IOleInPlaceActiveObject'], pszObjName: LPCOLESTR) -> int: ...

	virtual_table.build()

LPOLEINPLACEUIWINDOW = IOleInPlaceUIWindow.PTR()

class IOleInPlaceActiveObject(IOleWindow):
	virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
	_iid_ = IID("{00000117-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPMSG)
	def TranslateAccelerator(self, lpmsg: LPMSG) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnFrameWindowActivate(self, fActivate: bool) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnDocWindowActivate(self, fActivate: bool) -> int: ...

	@virtual_table.com_function(LPCRECT, PTR(IOleInPlaceUIWindow), BOOL)
	def ResizeBorder(self, prcBorder: LPCRECT, pUIWindow: IPointer[IOleInPlaceUIWindow], fFrameWindow: bool) -> int: ...

	@virtual_table.com_function(BOOL)
	def EnableModeless(self, fEnable: bool) -> int: ...

	virtual_table.build()

LPOLEINPLACEACTIVEOBJECT = IOleInPlaceActiveObject.PTR()

class OLEINPLACEFRAMEINFO(CStructure):
	_fields_ = [
		('cb', UINT),
		('fMDIApp', BOOL),
		('hwndFrame', HWND),
		('haccel', HACCEL),
		('cAccelEntries', UINT)
	]

	cAccelEntries: int
	hwndFrame: int
	fMDIApp: bool
	hAccel: int
	cb: int

LPOLEINPLACEFRAMEINFO = OLEINPLACEFRAMEINFO.PTR()

class OLEMENUGROUPWIDTHS(CStructure):
	_fields_ = [('width', LONG * 6)]

LPOLEMENUGROUPWIDTHS = OLEMENUGROUPWIDTHS.PTR()

HOLEMENU = HGLOBAL

class IOleInPlaceFrame(IOleInPlaceUIWindow):
	virtual_table = COMVirtualTable.from_ancestor(IOleInPlaceUIWindow)
	_iid_ = IID("{00000116-0000-0000-C000-000000000046}")

	@virtual_table.com_function(HMENU, LPOLEMENUGROUPWIDTHS)
	def InsertMenus(self, hmenuShared: HMENU, lpMenuWidths: IPointer[OLEMENUGROUPWIDTHS]) -> int: ...

	@virtual_table.com_function(HMENU, HOLEMENU, HWND)
	def SetMenu(self, hmenuShared: HMENU, holemenu: HOLEMENU, hwndActiveObject: HWND) -> int: ...

	@virtual_table.com_function(HMENU)
	def RemoveMenus(self, hmenuShared: HMENU) -> int: ...

	@virtual_table.com_function(LPCOLESTR)
	def SetStatusText(self, pszStatusText: LPCOLESTR) -> int: ...

	@virtual_table.com_function(BOOL)
	def EnableModeless(self, fEnable: bool) -> int: ...

	@virtual_table.com_function(LPMSG, WORD)
	def TranslateAccelerator(self, lpmsg: LPMSG, wID: int) -> int: ...

	virtual_table.build()

LPOLEINPLACEFRAME = IOleInPlaceFrame.PTR()

class IOleInPlaceObject(IOleWindow):
	virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
	_iid_ = IID("{00000119-0000-0000-C000-000000000046}")

	@virtual_table.com_function()
	def InPlaceDeactivate(self) -> int: ...

	@virtual_table.com_function()
	def UIDeactivate(self) -> int: ...

	@virtual_table.com_function(LPCRECT, LPCRECT)
	def SetObjectRects(self, lprcPosRect: LPCRECT, lprcClipRect: LPCRECT) -> int: ...

	@virtual_table.com_function()
	def ReactivateAndUndo(self) -> int: ...

	virtual_table.build()

LPOLEINPLACEOBJECT = IOleInPlaceObject.PTR()

class IOleInPlaceSite(IOleWindow):
	virtual_table = COMVirtualTable.from_ancestor(IOleWindow)
	_iid_ = IID("{00000119-0000-0000-C000-000000000046}")

	@virtual_table.com_function()
	def CanInPlaceActivate(self) -> int: ...

	@virtual_table.com_function()
	def OnInPlaceActivate(self) -> int: ...

	@virtual_table.com_function()
	def OnUIActivate(self) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(IOleInPlaceFrame), DOUBLE_PTR(IOleInPlaceUIWindow), LPRECT, LPRECT, PTR(OLEINPLACEFRAMEINFO))
	def GetWindowContext(self, ppFrame: IDoublePtr[IOleInPlaceFrame], ppDoc: IDoublePtr[IOleInPlaceUIWindow], lprcPosRect: LPRECT, lprcClipRect: LPRECT, lpFrameInfo: IPointer[OLEINPLACEFRAMEINFO]) -> int: ...

	@virtual_table.com_function(SIZEL)
	def Scroll(self, scrollExtant: SIZEL) -> int: ...

	@virtual_table.com_function(BOOL)
	def OnUIDeactivate(self, fUndoable: bool) -> int: ...

	@virtual_table.com_function()
	def OnInPlaceDeactivate(self) -> int: ...

	@virtual_table.com_function()
	def DiscardUndoState(self) -> int: ...

	@virtual_table.com_function()
	def DeactivateAndUndo(self) -> int: ...

	@virtual_table.com_function(LPCRECT)
	def OnPosRectChange(self, lprcPosRect: LPCRECT) -> int: ...

	virtual_table.build()

LPOLEINPLACESITE = IOleInPlaceSite.PTR()

class IContinue(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000012a-0000-0000-C000-000000000046}")

	@virtual_table.com_function()
	def FContinue(self) -> int: ...

	virtual_table.build()

class IViewObject(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000010d-0000-0000-C000-000000000046}")

	@virtual_table.com_function(DWORD, LONG, PVOID, PTR(DVTARGETDEVICE), HDC, HDC, LPCRECTL, LPCRECTL, PVOID, ULONG_PTR)
	def Draw(self, dwDrawAspect: int, lindex: int, pvAspect: PVOID, ptd: IPointer[DVTARGETDEVICE], hdcTargetDev: HDC, hdcDraw: HDC, lprcBounds: LPCRECTL, lprcWBounds: LPCRECTL, pfnContinue: PVOID, dwContinue: int) -> int: ...

	@virtual_table.com_function(DWORD, LONG, PVOID, PTR(DVTARGETDEVICE), HDC, DOUBLE_PTR(LOGPALETTE))
	def GetColorSet(self, dwDrawAspect: int, lindex: int, pvAspect: PVOID, ptd: IPointer[DVTARGETDEVICE], hicTargetDev: HDC, ppColorSet: IDoublePtr[LOGPALETTE]) -> int: ...

	@virtual_table.com_function(DWORD, LONG, PVOID, PDWORD)
	def Freeze(self, dwDrawAspect: int, lindex: int, pvAspect: PVOID, pdwFreeze: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD)
	def Unfreeze(self, dwFreeze: int) -> int: ...

	@virtual_table.com_function(DWORD, DWORD, LPADVISESINK)
	def SetAdvise(self, aspects: int, advf: int, pAdvSink: IPointer[IAdviseSink]) -> int: ...

	@virtual_table.com_function(PDWORD, PDWORD, DOUBLE_PTR(IAdviseSink))
	def GetAdvise(self, pAspects: PDWORD, pAdvf: PDWORD, ppAdvSink: IDoublePtr[IAdviseSink]) -> int: ...

	virtual_table.build()

LPVIEWOBJECT = IViewObject.PTR()

class IViewObject2(IViewObject):
	virtual_table = COMVirtualTable.from_ancestor(IViewObject)
	_iid_ = IID("{00000127-0000-0000-C000-000000000046}")

	@virtual_table.com_function(DWORD, LONG, PTR(DVTARGETDEVICE), LPSIZEL)
	def GetExtent(self, dwDrawAspect: int, lindex: int, ptd: IPointer[DVTARGETDEVICE], lpsizel: LPSIZEL) -> int: ...

	virtual_table.build()

LPVIEWOBJECT2 = IViewObject2.PTR()

class IDropSource(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000121-0000-0000-C000-000000000046}")

	@virtual_table.com_function(BOOL, DWORD)
	def QueryContinueDrag(self, fEscapePressed: bool, grfKeyState: int) -> int: ...

	@virtual_table.com_function(DWORD)
	def GiveFeedback(self, dwEffect: int) -> int: ...

	virtual_table.build()

LPDROPSOURCE = IDropSource.PTR()

MK_ALT = 0x0020

DROPEFFECT_NONE = 0
DROPEFFECT_COPY = 1
DROPEFFECT_MOVE = 2
DROPEFFECT_LINK = 4
DROPEFFECT_SCROLL = 0x80000000

# default inset-width of the hot zone, in pixels
#   typical use: GetProfileInt("windows","DragScrollInset",DD_DEFSCROLLINSET)
DD_DEFSCROLLINSET = 11

# default delay before scrolling, in milliseconds
#   typical use: GetProfileInt("windows","DragScrollDelay",DD_DEFSCROLLDELAY)
DD_DEFSCROLLDELAY = 50

# default scroll interval, in milliseconds
#   typical use: GetProfileInt("windows","DragScrollInterval", DD_DEFSCROLLINTERVAL)
DD_DEFSCROLLINTERVAL = 50

# default delay before dragging should start, in milliseconds
#   typical use: GetProfileInt("windows", "DragDelay", DD_DEFDRAGDELAY)
DD_DEFDRAGDELAY = 200

# default minimum distance (radius) before dragging should start, in pixels
#   typical use: GetProfileInt("windows", "DragMinDist", DD_DEFDRAGMINDIST)
DD_DEFDRAGMINDIST = 2

class IDropTarget(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000122-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPDATAOBJECT, DWORD, POINTL, PDWORD)
	def DragEnter(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: ...

	@virtual_table.com_function(DWORD, POINTL, PDWORD)
	def DragOver(self, grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: ...

	@virtual_table.com_function()
	def DragLeave(self) -> int: ...

	@virtual_table.com_function(LPDATAOBJECT, DWORD, POINTL, PDWORD)
	def Drop(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: ...

	virtual_table.build()

LPDROPTARGET = IDropTarget.PTR()

class IDropSourceNotify(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000012b-0000-0000-C000-000000000046}")

	@virtual_table.com_function(HWND)
	def DragEnterTarget(self, hwndTarget: HWND) -> int: ...

	@virtual_table.com_function()
	def DragLeaveTarget(self) -> int: ...

	virtual_table.build()

class IEnterpriseDropTarget(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{390E3878-FD55-4E18-819D-4682081C0CFD}")

	@virtual_table.com_function(LPCWSTR)
	def SetDropSourceEnterpriseId(self, identity: LPCWSTR) -> int: ...

	@virtual_table.com_function(PBOOL)
	def IsEvaluatingEdpPolicy(self, value: PBOOL) -> int: ...

	virtual_table.build()

class OLEVERB(CStructure):
    _fields_ = [
        ('lVerb', LONG),
        ('lpszVerbName', LPOLESTR),
        ('fuFlags', DWORD),
        ('grfAttribs', DWORD)
    ]

    lpszVerbName: LPOLESTR
    grfAttribs: int
    fuFlags: int
    lVerb: int

OLEVERBATTRIB_NEVERDIRTIES = 1
OLEVERBATTRIB_ONCONTAINERMENU = 2
OLEVERBATTRIB = INT

LPOLEVERB = OLEVERB.PTR()

class IEnumOLEVERB(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00000104-0000-0000-C000-000000000046}")

	@virtual_table.com_function(ULONG, LPOLEVERB, PULONG)
	def Next(self, celt: int, rgelt: IPointer[OLEVERB], pceltFetched: PULONG) -> int: ...

	@virtual_table.com_function(ULONG)
	def Skip(self, celt: int) -> int: ...

	@virtual_table.com_function()
	def Reset(self) -> int: ...

	@virtual_table.com_function(PVOID)
	def Clone(self, ppenum: IDoublePtr['IEnumOLEVERB']) -> int: ...

	virtual_table.build()

LPENUMOLEVERB = IEnumOLEVERB.PTR()

