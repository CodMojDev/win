.icl
.ver 100
.gencommentlw
.inc ../oaidl/oaidl0.icl
.inc ../oaidl/oaidl1.icl
.inc ../oaidl/oaidl2.icl
.inc ../oaidl/oaidl3.icl

I IClassFactory2 ex IClassFactory
{
	iid B196B28F-BAB4-101A-B69C-00AA00341D07
	cf GetLicInfo pLicInfo P.LICINFO
	cf RequestLicKey dwReserved DWORD pBstrKey P.BSTR
	cf CreateInstanceLic pUnkOuter P.IUnknown pUnkReserved P.IUnknown iid R.IID bstrKey P.BSTR ppvObj P.PVOID
}

pi LPCLASSFACTORY2

I IProvideClassInfo ex IUnknown
{
	iid B196B283-BAB4-101A-B69C-00AA00341D07
	cf GetClassInfo ppTI P.P.ITypeInfo
}

pi LPPROVIDECLASSINFO