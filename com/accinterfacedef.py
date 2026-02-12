from .autointerfacedef import *
from .accbase import *
from .bstr import *

DISPID_ACC_PARENT = -5000

DISPID_ACC_CHILDCOUNT = -5001

DISPID_ACC_CHILD = -5002

DISPID_ACC_NAME = -5003

DISPID_ACC_VALUE = -5004

DISPID_ACC_DESCRIPTION = -5005

DISPID_ACC_ROLE = -5006

DISPID_ACC_STATE = -5007

DISPID_ACC_HELP = -5008

DISPID_ACC_HELPTOPIC = -5009

DISPID_ACC_KEYBOARDSHORTCUT = -5010

DISPID_ACC_FOCUS = -5011

DISPID_ACC_SELECTION = -5012

DISPID_ACC_DEFAULTACTION = -5013

DISPID_ACC_SELECT = -5014

DISPID_ACC_LOCATION = -5015

DISPID_ACC_NAVIGATE = -5016

DISPID_ACC_HITTEST = -5017

DISPID_ACC_DODEFAULTACTION = -5018

NAVDIR_MIN = 0

NAVDIR_UP = 0x1

NAVDIR_DOWN = 0x2

NAVDIR_LEFT = 0x3

NAVDIR_RIGHT = 0x4

NAVDIR_NEXT = 0x5

NAVDIR_PREVIOUS = 0x6

NAVDIR_FIRSTCHILD = 0x7

NAVDIR_LASTCHILD = 0x8

NAVDIR_MAX = 0x9

SELFLAG_NONE = 0

SELFLAG_TAKEFOCUS = 0x1

SELFLAG_TAKESELECTION = 0x2

SELFLAG_EXTENDSELECTION = 0x4

SELFLAG_ADDSELECTION = 0x8

SELFLAG_REMOVESELECTION = 0x10

SELFLAG_VALID = 0x1f

STATE_SYSTEM_NORMAL = 0

STATE_SYSTEM_UNAVAILABLE = 0x1

STATE_SYSTEM_SELECTED = 0x2

STATE_SYSTEM_FOCUSED = 0x4

STATE_SYSTEM_PRESSED = 0x8

STATE_SYSTEM_CHECKED = 0x10

STATE_SYSTEM_MIXED = 0x20

STATE_SYSTEM_INDETERMINATE = STATE_SYSTEM_MIXED

STATE_SYSTEM_READONLY = 0x40

STATE_SYSTEM_HOTTRACKED = 0x80

STATE_SYSTEM_DEFAULT = 0x100

STATE_SYSTEM_EXPANDED = 0x200

STATE_SYSTEM_COLLAPSED = 0x400

STATE_SYSTEM_BUSY = 0x800

STATE_SYSTEM_FLOATING = 0x1000

STATE_SYSTEM_MARQUEED = 0x2000

STATE_SYSTEM_ANIMATED = 0x4000

STATE_SYSTEM_INVISIBLE = 0x8000

STATE_SYSTEM_OFFSCREEN = 0x10000

STATE_SYSTEM_SIZEABLE = 0x20000

STATE_SYSTEM_MOVEABLE = 0x40000

STATE_SYSTEM_SELFVOICING = 0x80000

STATE_SYSTEM_FOCUSABLE = 0x100000

STATE_SYSTEM_SELECTABLE = 0x200000

STATE_SYSTEM_LINKED = 0x400000

STATE_SYSTEM_TRAVERSED = 0x800000

STATE_SYSTEM_MULTISELECTABLE = 0x1000000

STATE_SYSTEM_EXTSELECTABLE = 0x2000000

STATE_SYSTEM_ALERT_LOW = 0x4000000

STATE_SYSTEM_ALERT_MEDIUM = 0x8000000

STATE_SYSTEM_ALERT_HIGH = 0x10000000

STATE_SYSTEM_PROTECTED = 0x20000000

STATE_SYSTEM_VALID = 0x7fffffff

STATE_SYSTEM_HASPOPUP = 0x40000000

ROLE_SYSTEM_TITLEBAR = 0x1

ROLE_SYSTEM_MENUBAR = 0x2

ROLE_SYSTEM_SCROLLBAR = 0x3

ROLE_SYSTEM_GRIP = 0x4

ROLE_SYSTEM_SOUND = 0x5

ROLE_SYSTEM_CURSOR = 0x6

ROLE_SYSTEM_CARET = 0x7

ROLE_SYSTEM_ALERT = 0x8

ROLE_SYSTEM_WINDOW = 0x9

ROLE_SYSTEM_CLIENT = 0xa

ROLE_SYSTEM_MENUPOPUP = 0xb

ROLE_SYSTEM_MENUITEM = 0xc

ROLE_SYSTEM_TOOLTIP = 0xd

ROLE_SYSTEM_APPLICATION = 0xe

ROLE_SYSTEM_DOCUMENT = 0xf

ROLE_SYSTEM_PANE = 0x10

ROLE_SYSTEM_CHART = 0x11

ROLE_SYSTEM_DIALOG = 0x12

ROLE_SYSTEM_BORDER = 0x13

ROLE_SYSTEM_GROUPING = 0x14

ROLE_SYSTEM_SEPARATOR = 0x15

ROLE_SYSTEM_TOOLBAR = 0x16

ROLE_SYSTEM_STATUSBAR = 0x17

ROLE_SYSTEM_TABLE = 0x18

ROLE_SYSTEM_COLUMNHEADER = 0x19

ROLE_SYSTEM_ROWHEADER = 0x1a

ROLE_SYSTEM_COLUMN = 0x1b

ROLE_SYSTEM_ROW = 0x1c

ROLE_SYSTEM_CELL = 0x1d

ROLE_SYSTEM_LINK = 0x1e

ROLE_SYSTEM_HELPBALLOON = 0x1f

ROLE_SYSTEM_CHARACTER = 0x20

ROLE_SYSTEM_LIST = 0x21

ROLE_SYSTEM_LISTITEM = 0x22

ROLE_SYSTEM_OUTLINE = 0x23

ROLE_SYSTEM_OUTLINEITEM = 0x24

ROLE_SYSTEM_PAGETAB = 0x25

ROLE_SYSTEM_PROPERTYPAGE = 0x26

ROLE_SYSTEM_INDICATOR = 0x27

ROLE_SYSTEM_GRAPHIC = 0x28

ROLE_SYSTEM_STATICTEXT = 0x29

ROLE_SYSTEM_TEXT = 0x2a

ROLE_SYSTEM_PUSHBUTTON = 0x2b

ROLE_SYSTEM_CHECKBUTTON = 0x2c

ROLE_SYSTEM_RADIOBUTTON = 0x2d

ROLE_SYSTEM_COMBOBOX = 0x2e

ROLE_SYSTEM_DROPLIST = 0x2f

ROLE_SYSTEM_PROGRESSBAR = 0x30

ROLE_SYSTEM_DIAL = 0x31

ROLE_SYSTEM_HOTKEYFIELD = 0x32

ROLE_SYSTEM_SLIDER = 0x33

ROLE_SYSTEM_SPINBUTTON = 0x34

ROLE_SYSTEM_DIAGRAM = 0x35

ROLE_SYSTEM_ANIMATION = 0x36

ROLE_SYSTEM_EQUATION = 0x37

ROLE_SYSTEM_BUTTONDROPDOWN = 0x38

ROLE_SYSTEM_BUTTONMENU = 0x39

ROLE_SYSTEM_BUTTONDROPDOWNGRID = 0x3a

ROLE_SYSTEM_WHITESPACE = 0x3b

ROLE_SYSTEM_PAGETABLIST = 0x3c

ROLE_SYSTEM_CLOCK = 0x3d

ROLE_SYSTEM_SPLITBUTTON = 0x3e

ROLE_SYSTEM_IPADDRESS = 0x3f

ROLE_SYSTEM_OUTLINEBUTTON = 0x40

class IAccessible(IDispatch):
	virtual_table = COMVirtualTable.from_ancestor(IDispatch.virtual_table, 'IAccessible')
	_iid_ = IID('{618736e0-3c3d-11cf-810c-00aa00389b71}')

	@virtual_table.com_function(POINTER(LPDISPATCH))
	def get_accParent(self, ppdispParent: IDoublePtr[IDispatch]) -> int: ...

	@virtual_table.com_function(PLONG)
	def get_accChildCount(self, pcountChildren: PLONG) -> int: ...

	@virtual_table.com_function(VARIANT, POINTER(LPDISPATCH))
	def get_accChild(self, varChild: VARIANT, ppdispChild: IDoublePtr[IDispatch]) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accName(self, varChild: VARIANT, pszName: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accValue(self, varChild: VARIANT, pszValue: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accDescription(self, varChild: VARIANT, pszDescription: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(VARIANT, LPVARIANT)
	def get_accRole(self, varChild: VARIANT, pvarRole: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(VARIANT, LPVARIANT)
	def get_accState(self, varChild: VARIANT, pvarState: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accHelp(self, varChild: VARIANT, pszHelp: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPBSTR, VARIANT, PLONG)
	def get_accHelpTopic(self, pszHelpFile: IPointer[BSTR], varChild: VARIANT, pidTopic: PLONG) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accKeyboardShortcut(self, varChild: VARIANT, pszKeyboardShortcut: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPVARIANT)
	def get_accFocus(self, pvarChild: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(LPVARIANT)
	def get_accSelection(self, pvarChildren: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(VARIANT, LPBSTR)
	def get_accDefaultAction(self, varChild: VARIANT, pszDefaultAction: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LONG, VARIANT)
	def accSelect(self, flagsSelect: int, varChild: VARIANT) -> int: ...

	@virtual_table.com_function(PLONG, PLONG, PLONG, PLONG, VARIANT)
	def accLocation(self, pxLeft: PLONG, pyTop: PLONG, pcxWidth: PLONG, pcyHeight: PLONG, varChild: VARIANT) -> int: ...

	@virtual_table.com_function(LONG, VARIANT, LPVARIANT)
	def accNavigate(self, navDir: int, varStart: VARIANT, pvarEndUpAt: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(LONG, LONG, LPVARIANT)
	def accHitTest(self, xLeft: int, yTop: int, pvarChild: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(VARIANT)
	def accDoDefaultAction(self, varChild: VARIANT) -> int: ...

	@virtual_table.com_function(VARIANT, BSTR)
	def put_accName(self, varChild: VARIANT, szName: BSTR) -> int: ...

	@virtual_table.com_function(VARIANT, BSTR)
	def put_accValue(self, varChild: VARIANT, szValue: BSTR) -> int: ...

	virtual_table.build()

LPACCESSIBLE = IAccessible.PTR()

class IAccessibleHandler(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAccessibleHandler')
	_iid_ = IID('{03022430-ABC4-11d0-BDE2-00AA001A1953}')

	@virtual_table.com_function(LONG, LONG, POINTER(IAccessible.PTR()))
	def AccessibleObjectFromID(self, hwnd: int, lObjectID: int, pIAccessible: IDoublePtr[IAccessible]) -> int: ...

	virtual_table.build()

LPACCESSIBLEHANDLER = IAccessibleHandler.PTR()

class IAccessibleWindowlessSite(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAccessibleWindowlessSite')
	_iid_ = IID('{BF3ABD9C-76DA-4389-9EB6-1427D25ABAB7}')

	@virtual_table.com_function(LONG, IAccessibleHandler.PTR(), PLONG)
	def AcquireObjectIdRange(self, rangeSize: int, pRangeOwner: IPointer[IAccessibleHandler], pRangeBase: PLONG) -> int: ...

	@virtual_table.com_function(LONG, IAccessibleHandler.PTR())
	def ReleaseObjectIdRange(self, rangeBase: int, pRangeOwner: IPointer[IAccessibleHandler]) -> int: ...

	@virtual_table.com_function(IAccessibleHandler.PTR(), POINTER(LPSAFEARRAY))
	def QueryObjectIdRanges(self, pRangesOwner: IPointer[IAccessibleHandler], psaRanges: IDoublePtr[SAFEARRAY]) -> int: ...

	@virtual_table.com_function(POINTER(IAccessible.PTR()))
	def GetParentAccessible(self, ppParent: IDoublePtr[IAccessible]) -> int: ...

	virtual_table.build()

LPACCESSIBLEWINDOWLESSSITE = IAccessibleWindowlessSite.PTR()

ANNO_THIS = 0
ANNO_CONTAINER = 1
AnnoScope = INT

MSAAPROPID = GUID

class IAccIdentity(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAccIdentity')
	_iid_ = IID('{7852b78d-1cfd-41c1-a615-9c0c85960b5f}')

	@virtual_table.com_function(DWORD, POINTER(LPSTR), PDWORD)
	def GetIdentityString(self, dwIDChild: int, ppIDString: IPointer[LPSTR], pdwIDStringLen: PDWORD) -> int: ...

	virtual_table.build()

class IAccPropServer(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAccPropServer')
	_iid_ = IID('{76c0dbbb-15e0-4e7b-b61b-20eeea2001e0}')

	@virtual_table.com_function(LPSTR, DWORD, MSAAPROPID, LPVARIANT, PBOOL)
	def GetPropValue(self, pIDString: LPSTR, dwIDStringLen: int, idProp: MSAAPROPID, pvarValue: IPointer[VARIANT], pfHasProp: PBOOL) -> int: ...

	virtual_table.build()

class IAccPropServices(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAccPropServices')
	_iid_ = IID('{6e26e776-04f0-495d-80e4-3330352e3169}')

	@virtual_table.com_function(LPSTR, DWORD, MSAAPROPID, VARIANT)
	def SetPropValue(self, pIDString: LPSTR, dwIDStringLen: int, idProp: MSAAPROPID, var: VARIANT) -> int: ...

	@virtual_table.com_function(LPSTR, DWORD, POINTER(MSAAPROPID), INT, IAccPropServer.PTR(), AnnoScope)
	def SetPropServer(self, pIDString: LPSTR, dwIDStringLen: int, paProps: IPointer[MSAAPROPID], cProps: int, pServer: IPointer[IAccPropServer], annoScope: AnnoScope) -> int: ...

	@virtual_table.com_function(LPSTR, DWORD, POINTER(MSAAPROPID), INT)
	def ClearProps(self, pIDString: LPSTR, dwIDStringLen: int, paProps: IPointer[MSAAPROPID], cProps: int) -> int: ...

	@virtual_table.com_function(HWND, DWORD, DWORD, MSAAPROPID, VARIANT)
	def SetHwndProp(self, hwnd: HWND, idObject: int, idChild: int, idProp: MSAAPROPID, var: VARIANT) -> int: ...

	@virtual_table.com_function(HWND, DWORD, DWORD, MSAAPROPID, LPCWSTR)
	def SetHwndPropStr(self, hwnd: HWND, idObject: int, idChild: int, idProp: MSAAPROPID, str: LPCWSTR) -> int: ...

	@virtual_table.com_function(HWND, DWORD, DWORD, POINTER(MSAAPROPID), INT, IAccPropServer.PTR(), AnnoScope)
	def SetHwndPropServer(self, hwnd: HWND, idObject: int, idChild: int, paProps: IPointer[MSAAPROPID], cProps: int, pServer: IPointer[IAccPropServer], annoScope: AnnoScope) -> int: ...

	@virtual_table.com_function(HWND, DWORD, DWORD, POINTER(MSAAPROPID), INT)
	def ClearHwndProps(self, hwnd: HWND, idObject: int, idChild: int, paProps: IPointer[MSAAPROPID], cProps: int) -> int: ...

	@virtual_table.com_function(HWND, DWORD, DWORD, POINTER(LPSTR), PDWORD)
	def ComposeHwndIdentityString(self, hwnd: HWND, idObject: int, idChild: int, ppIDString: IPointer[LPSTR], pdwIDStringLen: PDWORD) -> int: ...

	@virtual_table.com_function(LPSTR, DWORD, POINTER(HWND), PDWORD, PDWORD)
	def DecomposeHwndIdentityString(self, pIDString: LPSTR, dwIDStringLen: int, phwnd: IPointer[HWND], pidObject: PDWORD, pidChild: PDWORD) -> int: ...

	@virtual_table.com_function(HMENU, DWORD, MSAAPROPID, VARIANT)
	def SetHmenuProp(self, hmenu: HMENU, idChild: int, idProp: MSAAPROPID, var: VARIANT) -> int: ...

	@virtual_table.com_function(HMENU, DWORD, MSAAPROPID, LPCWSTR)
	def SetHmenuPropStr(self, hmenu: HMENU, idChild: int, idProp: MSAAPROPID, str: LPCWSTR) -> int: ...

	@virtual_table.com_function(HMENU, DWORD, POINTER(MSAAPROPID), INT, IAccPropServer.PTR(), AnnoScope)
	def SetHmenuPropServer(self, hmenu: HMENU, idChild: int, paProps: IPointer[MSAAPROPID], cProps: int, pServer: IPointer[IAccPropServer], annoScope: AnnoScope) -> int: ...

	@virtual_table.com_function(HMENU, DWORD, POINTER(LPSTR), PDWORD)
	def ClearHmenuProps(self, hmenu: HMENU, idChild: int, ppIDString: IPointer[LPSTR], pdwIDStringLen: PDWORD) -> int: ...

	@virtual_table.com_function(HMENU, DWORD, POINTER(LPSTR))
	def ComposeHmenuIdentityString(self, hmenu: HMENU, idChild: int, ppIDString: IPointer[LPSTR]) -> int: ...

	@virtual_table.com_function(POINTER(LPSTR), DWORD, POINTER(HMENU), PDWORD)
	def DecomposeHmenuIdentityString(self, pIDString: IPointer[LPSTR], dwIDStringLen: int, phmenu: IPointer[HMENU], pidChild: PDWORD) -> int: ...

	virtual_table.build()

#=--------------------------------------------------------------------------=
# GUIDs
#=--------------------------------------------------------------------------=

LIBID_Accessibility     = CLSID('{1ea4dbf0-3c3b-11cf-810c-00aa00389b71}')
IID_IAccessible         = IID('{618736e0-3c3d-11cf-810c-00aa00389b71}')
IID_IAccessibleHandler  = IID('{03022430-ABC4-11d0-BDE2-00AA001A1953}')
IID_IAccIdentity        = IID('{7852b78d-1cfd-41c1-a615-9c0c85960b5f}')
IID_IAccPropServer      = IID('{76c0dbbb-15e0-4e7b-b61b-20eeea2001e0}')
IID_IAccPropServices    = IID('{6e26e776-04f0-495d-80e4-3330352e3169}')
IID_IAccPropMgrInternal = IID('{2bd370a9-3e7f-4edd-8a85-f8fed1f8e51f}')
CLSID_AccPropServices   = CLSID('{b5f8350b-0548-48b1-a6ee-88bd00b4a5e7}')
IIS_IsOleaccProxy       = IID('{902697fa-80e4-4560-802a-a13f22a64709}')
IIS_ControlAccessible   = IID('{38c682a6-9731-43f2-9fae-e901e641b101}')

#=--------------------------------------------------------------------------=
# MSAA API Prototypes
#=--------------------------------------------------------------------------=

@oleacc.foreign(LRESULT, REFIID, WPARAM, LPUNKNOWN, intermediate_method=True)
def LresultFromObject(iid: IID, wParam: int, 
                      punk: IPointer[IUnknown], **kwargs) -> int: 
    return delegate(iid.ref(), wParam, punk)

@oleacc_foreign(LRESULT, REFIID, WPARAM, PVOID, intermediate_method=True)
def ObjectFromLresult(lResult: int, iid: IID, wParam: int, 
                      ppvObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(lResult, iid.ref(), wParam, ppvObject)

@oleacc_foreign(LPACCESSIBLE, PTR(HWND))
def WindowFromAccessibleObject(pacc: IPointer[IAccessible],
                               phwnd: IPointer[HWND]) -> int: ...

@oleacc_foreign(HWND, DWORD, REFIID, PVOID, intermediate_method=True)
def AccessibleObjectFromWindow(hwnd: int, dwId: int, iid: IID, 
                               ppvObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(hwnd, dwId, iid.ref(), ppvObject)

@oleacc_foreign(HWND, DWORD, DWORD, PTR(LPACCESSIBLE), LPVARIANT)
def AccessibleObjectFromEvent(hwnd: int, dwId: int, dwChildId: int, 
                              ppacc: IDoublePtr[IAccessible], 
                              pvarChild: IPointer[VARIANT]) -> int: ...

@oleacc_foreign(POINT, PTR(LPACCESSIBLE), LPVARIANT)
def AccessibleObjectFromPoint(ptScreen: POINT, ppacc: IDoublePtr[IAccessible],
                              pvarChild: IPointer[VARIANT]) -> int: ...

@oleacc_foreign(LPACCESSIBLE, LONG, LONG, LPVARIANT, PLONG)
def AccessibleChildren(paccContainer: IPointer[IAccessible], iChildStart: int, cChildren: int, 
                       rgvarChildren: IPointer[VARIANT], pcObtained: PLONG) -> int: ...

@oleacc.foreign(UINT, DWORD, LPSTR, UINT)
def GetRoleTextA(lRole: int, lpszRole: LPSTR, cchRoleMax: int) -> int: ...

@oleacc.foreign(UINT, DWORD, LPWSTR, UINT)
def GetRoleTextW(lRole: int, lpszRole: LPWSTR, cchRoleMax: int) -> int: ...

GetRoleText = unicode(GetRoleTextW, GetRoleTextA)

@oleacc.foreign(UINT, DWORD, LPSTR, UINT)
def GetStateTextA(lStateBit: int, lpszState: LPSTR, cchState: int) -> int: ...

@oleacc.foreign(UINT, DWORD, LPWSTR, UINT)
def GetStateTextW(lStateBit: int, lpszState: LPWSTR, cchState: int) -> int: ...

GetStateText = unicode(GetStateTextW, GetStateTextA)

@oleacc.foreign(VOID, PDWORD, PDWORD)
def GetOleaccVersionInfo(pVer: PDWORD, pBuild: PDWORD): ...

@oleacc_foreign(HWND, LONG, REFIID, PVOID, intermediate_method=True)
def CreateStdAccessibleObject(hwnd: int, idObject: int, iid: IID, 
                              ppvObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(hwnd, idObject, iid.ref(), ppvObject)

@oleacc_foreign(HWND, LPCSTR, LONG, REFIID, PVOID, intermediate_method=True)
def CreateStdAccessibleProxyA(hwnd: int, pClassName: LPCSTR, idObject: int,
                              iid: IID, ppvObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(hwnd, pClassName, idObject, iid.ref(), ppvObject)

@oleacc_foreign(HWND, LPCWSTR, LONG, REFIID, PVOID, intermediate_method=True)
def CreateStdAccessibleProxyW(hwnd: int, pClassName: LPCWSTR, idObject: int,
                              iid: IID, ppvObject: IPointer[PVOID], **kwargs) -> int:
    return delegate(hwnd, pClassName, idObject, iid.ref(), ppvObject)

CreateStdAccessibleProxy = unicode(CreateStdAccessibleProxyW, CreateStdAccessibleProxyA)

ANRUS_ON_SCREEN_KEYBOARD_ACTIVE = 0x0000001
ANRUS_TOUCH_MODIFICATION_ACTIVE = 0x0000002
ANRUS_PRIORITY_AUDIO_ACTIVE     = 0x0000004
ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK = 0x0000008
ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK = 0x0000010

@oleacc_foreign(HWND, DWORD, DWORD)
def AccSetRunningUtilityState(hwndApp: int, dwUtilityStateMask: int, dwUtilityState: int) -> int: ...

@oleacc_foreign(HWND, HWND, POINT)
def AccNotifyTouchInteraction(hwndApp: int, hwndTarget: int, ptTarget: POINT) -> int: ...