.icl
.ver 100
.gencommentlw
.inc ocidl3.icl

// forward-pointer declarations for generator
silent
{
	pie IDispatch LPDISPATCH
}

I IOleControlSite ex IUnknown
{
	iid B196B289-BAB4-101A-B69C-00AA00341D07
	cf OnControlInfoChanged
	cf LockInPlaceActive fLock BOOL
	cf GetExtendedControl ppDisp P.P.IDispatch
	cf TransformCoords pPtlHimetric P.POINTL pPtfContainer P.POINTF dwFlags DWORD
	cf TranslateAccelerator pMsg P.MSG grfModifiers DWORD
	cf OnFocus fGotFocus BOOL
	cf ShowPropertyFrame
}

pi LPOLECONTROLSITE