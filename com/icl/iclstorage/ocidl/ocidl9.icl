.icl
.ver 100
.gencommentlw
.inc ocidl8.icl

// forward-pointer declaration for generator
silent
{
	pie CALPOLESTR LPCALPOLESTR
	pie CADWORD LPCADWORD
}

I IPerPropertyBrowsing ex IUnknown
{
	iid 376BD3AA-3845-101B-84ED-08002B2EC713
	cf GetDisplayString dispID DISPID pBstr P.BSTR
	cf MapPropertyToPage dispID DISPID pClsid P.CLSID
	cf GetPredefinedStrings dispID DISPID pCaStringsOut P.CALPOLESTR pCaCookiesOut P.CADWORD
	cf GetPredefinedValue dispID DISPID dwCookie DWORD pVarOut P.VARIANT
}

pi LPPERPROPERTYBROWSING