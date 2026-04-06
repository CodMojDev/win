.icl
.ver 100
.gencommentlw
.inc ocidl9.icl

I IPropertyBag2 ex IUnknown
{
	iid 22F55882-280B-11d0-A8A9-00A0C90C2004
	cf Read cProperties ULONG pPropBag P.PROPBAG2 pErrLog P.IErrorLog pvarValue P.VARIANT phrError P.HRESULT
	cf Write cProperties ULONG pPropBag P.PROPBAG2 pvarValue P.VARIANT
	cf CountProperties pcProperties PULONG
	cf GetPropertyInfo iProperty ULONG cProperties ULONG pPropBag P.PROPBAG2 pcProperties PULONG
	cf LoadObject pstrName LPCOLESTR dwHint DWORD pUnkObject P.IUnknown pErrLog P.IErrorLog
}

pi LPPROPERTYBAG2

I IPersistPropertyBag2 ex IPersist
{
	iid 22F55881-280B-11d0-A8A9-00A0C90C2004
	cf InitNew
	cf Load pPropBag P.IPropertyBag2 pErrLog P.IErrorLog
	cf Save pPropBag P.IPropertyBag2 fClearDirty BOOL fSaveAllProperties BOOL
	cf IsDirty
}

pi LPPERSISTPROPERTYBAG2

I IAdviseSinkEx ex IAdviseSink
{
	iid 3AF24290-0C96-11CE-A0CF-00AA00600AB8
	cf OnViewStatusChange dwViewStatus DWORD
}

pi LPADVISESINKEX