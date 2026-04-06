.icl
.ver 100
.gencommentlw
.inc ocidl5.icl

I IPropertyPageSite ex IUnknown
{
	iid B196B28C-BAB4-101A-B69C-00AA00341D07
	cf OnStatusChange dwFlags DWORD
	cf GetLocaleID pLocaleID P.LCID
	cf GetPageContainer ppUnk P.P.IUnknown
	cf TranslateAccelerator pMsg P.MSG
}

pi LPPROPERTYPAGESITE

I IPropertyNotifySink ex IUnknown
{
	iid 9BFBBC02-EFF1-101A-84ED-00AA00341D07
	cf OnChanged dispID DISPID
	cf OnRequestEdit dispID DISPID
}

pi LPPROPERTYNOTIFYSINK