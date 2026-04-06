.icl
.ver 100
.gencommentlw
.inc ocidl4.icl

I IPropertyPage ex IUnknown
{
	iid B196B28D-BAB4-101A-B69C-00AA00341D07
	cf SetPageSite pPageSite FD.P.IPropertyPageSite
	cf Activate hWndParent HWND pRect LPCRECT bModal BOOL
	cf Deactivate
	cf GetPageInfo pPageInfo P.PROPPAGEINFO
	cf SetObjects cObjects ULONG ppUnk P.P.IUnknown
	cf Show nCmdShow UINT
	cf Move pRect LPCRECT
	cf IsPageDirty
	cf Apply
	cf Help pszHelpDir LPCOLESTR
	cf TranslateAccelerator pMsg P.MSG
}

pi LPPROPERTYPAGE

I IPropertyPage2 ex IPropertyPage
{
	iid 01E44665-24AC-101B-84ED-08002B2EC713
	cf EditProperty dispID DISPID
}

pi LPPROPERTYPAGE2