.icl
.ver 100
.gencommentlw
.inc ocidl7.icl

I IViewObjectEx ex IViewObject2
{
	iid 3AF24292-0C96-11CE-A0CF-00AA00600AB8
	cf GetRect dwAspect DWORD pRect LPRECTL
	cf GetViewStatus pdwStatus PDWORD
	cf QueryHitPoint dwAspect DWORD pRectBounds LPCRECT ptlLoc POINT lCloseHint LONG pHitResult PDWORD
	cf QueryHitRect dwAspect DWORD pRectBounds LPCRECT pRectLoc LPCRECT lCloseHint LONG pHitResult PDWORD
	cf GetNaturalExtent dwAspect DWORD lindex LONG ptd P.DVTARGETDEVICE hicTargetDev HDC pExtentInfo P.DVEXTENTINFO pSizel LPSIZEL
}

pi LPVIEWOBJECTEX

I IOleUndoUnit ex IUnknown
{
	iid 894AD3B0-EF97-11CE-9BC9-00AA00608E01
	cf Do pUndoManager FD.P.IOleUndoManager
	cf GetDescription pBstr P.BSTR
	cf GetUnitType pClsid P.CLSID plID PLONG
	cf OnNextAdd
}

pi LPOLEUNDOUNIT

I IOleParentUndoUnit ex IOleUndoUnit
{
	iid A1FAF330-EF97-11CE-9BC9-00AA00608E01
	cf Open pPUU FD.P.IOleParentUndoUnit
	cf Close pPUU FD.P.IOleParentUndoUnit fCommit BOOL
	cf Add pUU P.IOleUndoUnit
	cf FindUnit pUU P.IOleUndoUnit
	cf GetParentState pdwState PDWORD
}

pi LPOLEPARENTUNDOUNIT

I IEnumOleUndoUnits ex IUnknown
{
	iid B3E7C340-EF97-11CE-9BC9-00AA00608E01
	cf Next cElt ULONG rgElt P.P.IOleUndoUnit
	cf Skip cElt ULONG
	cf Reset
	cf Clone ppEnum FD.P.P.IEnumOleUndoUnits
}

pi LPENUMOLEUNDOUNITS

I IOleUndoManager ex IUnknown
{
	iid D001F200-EF97-11CE-9BC9-00AA00608E01
	cf Open pPUU P.IOleParentUndoUnit
	cf Close pPUU P.IOleParentUndoUnit fCommit BOOL
	cf Add pUU P.IOleUndoUnit
	cf GetOpenParentState pdwState PDWORD
	cf DiscardFrom pUU P.IOleUndoUnit
	cf UndoTo pUU P.IOleUndoUnit
	cf RedoTo pUU P.IOleUndoUnit
	cf EnumUndoable ppEnum P.P.IEnumOleUndoUnits
	cf EnumRedoable ppEnum P.P.IEnumOleUndoUnits
	cf GetLastUndoDescription pBstr P.BSTR
	cf GetLastRedoDescription pBstr P.BSTR
	cf Enable fEnable BOOL
}

pi LPOLEUNDOMANAGER

~POINTERINACTIVE_ACTIVATEONENTRY = 1
~POINTERINACTIVE_DEACTIVATEONLEAVE = 2
~POINTERINACTIVE_ACTIVATEONDRAG = 4
~POINTERINACTIVE = INT
~

I IPointerInactive ex IUnknown
{
	iid 55980BA0-35AA-11CF-B671-00AA004CD6D8
	cf GetActivationPolicy pdwPolicy PDWORD
	cf OnInactiveMouseMove pRectBounds LPCRECT x LONG y LONG grfKeyState DWORD
	cf OnInactiveSetCursor pRectBounds LPCRECT x LONG y LONG dwMouseArg DWORD fSetAlways BOOL
}

pi LPPOINTERINACTIVE

I IObjectWithSite ex IUnknown
{
	iid FC4801A3-2BA9-11CF-A229-00AA003D7352
	cf SetSite pUnkSite P.IUnknown
	cf GetSite riid R.IID ppvSite P.PVOID
}

pi LPOBJECTWITHSITE