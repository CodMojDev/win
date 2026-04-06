.icl
.ver 100

// forward pointer declarations for readability
pie IDispatch LPDISPATCH
pie BSTR LPBSTR
pie VARIANT LPVARIANT
pie SAFEARRAY LPSAFEARRAY

I IAccessible ex IDispatch
{
	iid 618736e0-3c3d-11cf-810c-00aa00389b71
	cf get_accParent ppdispParent P.P.IDispatch
	cf get_accChildCount pcountChildren PLONG
	cf get_accChild varChild VARIANT ppdispChild P.P.IDispatch
	cf get_accName varChild VARIANT pszName P.BSTR
	cf get_accValue varChild VARIANT pszValue P.BSTR
	cf get_accDescription varChild VARIANT pszDescription P.BSTR
	cf get_accRole varChild VARIANT pvarRole P.VARIANT
	cf get_accState varChild VARIANT pvarState P.VARIANT
	cf get_accHelp varChild VARIANT pszHelp P.BSTR
	cf get_accHelpTopic pszHelpFile P.BSTR varChild VARIANT pidTopic PLONG
	cf get_accKeyboardShortcut varChild VARIANT pszKeyboardShortcut P.BSTR
	cf get_accFocus pvarChild P.VARIANT
	cf get_accSelection pvarChildren P.VARIANT
	cf get_accDefaultAction varChild VARIANT pszDefaultAction P.BSTR
	cf accSelect flagsSelect LONG varChild VARIANT
	cf accLocation pxLeft PLONG pyTop PLONG pcxWidth PLONG pcyHeight PLONG varChild VARIANT
	cf accNavigate navDir LONG varStart VARIANT pvarEndUpAt P.VARIANT
	cf accHitTest xLeft LONG yTop LONG pvarChild P.VARIANT
	cf accDoDefaultAction varChild VARIANT
	cf put_accName varChild VARIANT szName BSTR
	cf put_accValue varChild VARIANT szValue BSTR
}

pi LPACCESSIBLE

I IAccessibleHandler ex IUnknown
{
	iid 03022430-ABC4-11d0-BDE2-00AA001A1953
	cf AccessibleObjectFromID hwnd LONG lObjectID LONG pIAccessible P.P.IAccessible
}

pi LPACCESSIBLEHANDLER

I IAccessibleWindowlessSite ex IUnknown
{
	iid BF3ABD9C-76DA-4389-9EB6-1427D25ABAB7
	cf AcquireObjectIdRange rangeSize LONG pRangeOwner P.IAccessibleHandler pRangeBase PLONG
	cf ReleaseObjectIdRange rangeBase LONG pRangeOwner P.IAccessibleHandler
	cf QueryObjectIdRanges pRangesOwner P.IAccessibleHandler psaRanges P.P.SAFEARRAY
	cf GetParentAccessible ppParent P.P.IAccessible
}

pi LPACCESSIBLEWINDOWLESSSITE

// Python definition of enumeration
~ANNO_THIS = 0
~ANNO_CONTAINER = 1
~AnnoScope = INT
~
~MSAAPROPID = GUID

I IAccIdentity ex IUnknown
{
	iid 7852b78d-1cfd-41c1-a615-9c0c85960b5f
	cf GetIdentityString dwIDChild DWORD ppIDString P.PBYTE pdwIDStringLen PDWORD
}

I IAccPropServer ex IUnknown
{
	iid 76c0dbbb-15e0-4e7b-b61b-20eeea2001e0
	cf GetPropValue pIDString LPSTR dwIDStringLen DWORD idProp MSAAPROPID pvarValue P.VARIANT pfHasProp PBOOL
}

I IAccPropServices ex IUnknown
{
	iid 6e26e776-04f0-495d-80e4-3330352e3169
	cf SetPropValue pIDString LPSTR dwIDStringLen DWORD idProp MSAAPROPID var VARIANT
	cf SetPropServer pIDString LPSTR dwIDStringLen DWORD paProps P.MSAAPROPID cProps INT pServer P.IAccPropServer annoScope AnnoScope
	cf ClearProps pIDString LPSTR dwIDStringLen DWORD paProps P.MSAAPROPID cProps INT
	cf SetHwndProp hwnd HWND idObject DWORD idChild DWORD idProp MSAAPROPID var VARIANT
	cf SetHwndPropStr hwnd HWND idObject DWORD idChild DWORD idProp MSAAPROPID str LPCWSTR
	cf SetHwndPropServer hwnd HWND idObject DWORD idChild DWORD paProps P.MSAAPROPID cProps INT pServer P.IAccPropServer annoScope AnnoScope
	cf ClearHwndProps hwnd HWND idObject DWORD idChild DWORD paProps P.MSAAPROPID cProps INT
	cf ComposeHwndIdentityString hwnd HWND idObject DWORD idChild DWORD ppIDString P.LPSTR pdwIDStringLen PDWORD
	cf DecomposeHwndIdentityString pIDString LPSTR dwIDStringLen DWORD phwnd P.HWND pidObject PDWORD pidChild PDWORD
	cf SetHmenuProp hmenu HMENU idChild DWORD idProp MSAAPROPID var VARIANT
	cf SetHmenuPropStr hmenu HMENU idChild DWORD idProp MSAAPROPID str LPCWSTR
	cf SetHmenuPropServer hmenu HMENU idChild DWORD paProps P.MSAAPROPID cProps INT pServer P.IAccPropServer annoScope AnnoScope
	cf ClearHmenuProps hmenu HMENU idChild DWORD ppIDString P.LPSTR pdwIDStringLen PDWORD
	cf ComposeHmenuIdentityString hmenu HMENU idChild DWORD ppIDString P.LPSTR
	cf DecomposeHmenuIdentityString pIDString P.LPSTR dwIDStringLen DWORD phmenu P.HMENU pidChild PDWORD
}