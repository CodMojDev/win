.icl
.ver 100
.gencommentlw
.inc ocidl2.icl

// forward-pointer declarations for generator
silent
{
	pie CONTROLINFO LPCONTROLINFO
	pie MSG PMSG
}

I IOleControl ex IUnknown
{
	iid B196B288-BAB4-101A-B69C-00AA00341D07
	cf GetControlInfo pCI P.CONTROLINFO
	cf OnMnemonic pMsg P.MSG
	cf OnAmbientPropertyChange dispID DISPID
	cf FreezeEvents bFreeze BOOL
}

pi LPOLECONTROL