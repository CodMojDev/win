.icl
.ver 100
.gencommentlw

// forward-declare pointer types to generator parser
silent
{
	pie VARIANT LPVARIANT
	pie IEnumUnknown LPENUMUNKNOWN
	pie ITypeInfo LPTYPEINFO
	pie EXCEPINFO LPEXCEPINFO
}

I ITypeChangeEvents ex IUnknown
{
	iid 00020410-0000-0000-C000-000000000046
	cf RequestTypeChange changeKind CHANGEKIND pTInfoBefore P.ITypeInfo pStrName LPOLESTR pfCancel PINT
	cf AfterTypeChange changeKind CHANGEKIND pTInfoAfter P.ITypeInfo pStrName LPOLESTR
}

pi LPTYCHANGEEVENTS

I IErrorInfo ex IUnknown
{
	iid 1CF2B120-547D-101B-8E65-08002B2BD119
	cf GetGUID pGUID P.GUID
	cf GetSource pBstrSource P.BSTR
	cf GetDescription pBstrDescription P.BSTR
	cf GetHelpFile pBstrHelpFile P.BSTR
	cf GetHelpContext pdwHelpContext PDWORD
}

pi LPERRORINFO

I ICreateErrorInfo ex IUnknown
{
	iid 22F03340-547D-101B-8E65-08002B2BD119
	cf SetGUID guid R.GUID
	cf SetSource szSource LPOLESTR
	cf SetDescription szDescription LPOLESTR
	cf SetHelpFile szHelpFile LPOLESTR
	cf SetHelpContext dwHelpContext DWORD
}

pi LPCREATEERRORINFO

I ISupportErrorInfo ex IUnknown
{
	iid DF0B3D60-548F-101B-8E65-08002B2BD119
	cf InterfaceSupportsErrorInfo iid R.IID
}

pi LPSUPPORTERRORINFO

I ITypeFactory ex IUnknown
{
	cf CreateFromTypeInfo pTypeInfo P.ITypeInfo iid R.IID ppv P.P.IUnknown
}

I ITypeMarshal ex IUnknown
{
	iid 0000002D-0000-0000-C000-000000000046
	cf Size pvType PVOID dwDestContext DWORD pvDestContext PVOID pSize PULONG
	cf Marshal pvType PVOID dwDestContext DWORD pvDestContext PVOID cbBufferLength ULONG pBuffer PBYTE pcbWritten PULONG
	cf Unmarshal pvType PVOID dwFlags DWORD cbBufferLength ULONG pBuffer PBYTE pcbRead PULONG
	cf Free pvType PVOID
}

I IRecordInfo ex IUnknown
{
	iid 0000002F-0000-0000-C000-000000000046
	cf RecordInit pvNew PVOID
	cf RecordClear pvExisting PVOID
	cf RecordCopy pvExisting PVOID pvNew PVOID
	cf GetGuid pguid P.GUID
	cf GetName pbstrName P.BSTR
	cf GetSize pcbSize PULONG
	cf GetTypeInfo ppTypeInfo P.P.ITypeInfo
	cf GetField pvData PVOID szFieldName LPCOLESTR pvarField P.VARIANT
	cf GetFieldNoCopy pvData PVOID szFieldName LPCOLESTR pvarField P.VARIANT ppvDataCArray P.PVOID
	cf PutField wFlags ULONG pvData PVOID szFieldName LPCOLESTR pvarField P.VARIANT
	cf PutFieldNoCopy wFlags ULONG pvData PVOID szFieldName LPCOLESTR pvarField P.VARIANT
	cf GetFieldNames pcNames PULONG rgBstrNames P.BSTR
	cf IsMatchingType pRecordInfo P.IRecordInfo
	cf RecordCreate
	cf RecordCreateCopy pvSource PVOID ppvDest P.PVOID
	cf RecordDestroy pvRecord PVOID
}

pi LPRECORDINFO

I IErrorLog ex IUnknown
{
	iid 3127CA40-446E-11CE-8135-00AA004BB851
	cf AddError pszPropName LPCOLESTR pExcepInfo P.EXCEPINFO
}

pi LPERRORLOG

I IPropertyBag ex IUnknown
{
	iid 55272A00-42CB-11CE-8135-00AA004BB851
	cf Read pszPropName LPCOLESTR pVar P.VARIANT pErrorLog P.IErrorLog
	cf Write pszPropName LPCOLESTR pVar P.VARIANT
}

pi LPPROPERTYBAG

I ITypeLibRegistrationReader ex IUnknown
{
	iid ED6A8A2A-B160-4E77-8F73-AA7435CD5C27
	cf EnumTypeLibRegistrations ppEnumUnknown P.P.IEnumUnknown
}

cf ITypeLibRegistration ex IUnknown
{
	iid 76A3E735-02DF-4A12-98EB-043AD3600AF3
	cf GetGuid pGuid P.GUID
	cf GetVersion pVersion P.BSTR
	cf GetLcid pLcid P.LCID
	cf GetWin32Path pWin32Path P.BSTR
	cf GetWin64Path pWin64Path P.BSTR
	cf GetDisplayName pDisplayName P.BSTR
	cf GetFlags pFlags PDWORD
	cf GetHelpDir pHelpDir PDWORD
}