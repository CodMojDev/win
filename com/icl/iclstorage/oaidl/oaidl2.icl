.icl
.ver 100
.gencommentlw

// forward-declare pointer types to generator parser
silent
{
	pie VARIANT LPVARIANT
	pie CUSTDATA LPCUSTDATA
}

I ITypeLib2 ex ITypeLib
{
	iid 00020411-0000-0000-C000-000000000046
	cf GetCustData guid R.GUID pVarVal P.VARIANT
	cf GetLibStatistics pcUniqueNames PULONG pcchUniqueNames PULONG
	cf GetDocumentation2 index INT lcid LCID pbstrHelpString P.BSTR pdwHelpStringContext PDWORD pbstrHelpStringDll P.BSTR
	cf GetAllCustData pCustData P.CUSTDATA
}

pi LPTYPELIB2