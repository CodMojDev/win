.icl
.ver 100
.gencommentlw

// forward-declare pointer types to generator parser
silent
{
	pie VARIANT LPVARIANT
	pie CUSTDATA LPCUSTDATA
}

I ITypeInfo2 ex ITypeInfo
{
	iid 00020412-0000-0000-C000-000000000046
	cf GetTypeKind pTypeKind P.TYPEKIND
	cf GetTypeFlags pTypeFlags PULONG
	cf GetFuncIndexOfMemId memid MEMBERID invKind INVOKEKIND pFuncIndex PUINT
	cf GetVarIndexOfMemId memid MEMBERID pVarIndex PUINT
	cf GetCustData guid R.GUID pVarVal P.VARIANT
	cf GetFuncCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf GetParamCustData indexFunc UINT indexParam UINT guid R.GUID pVarVal P.VARIANT
	cf GetVarCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf GetImplTypeCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf GetDocumentation2 memid MEMBERID lcid LCID pbstrHelpString P.BSTR pdwHelpStringContext PDWORD pbstrHelpStringDll P.BSTR
	cf GetAllCustData pCustData P.CUSTDATA
	cf GetAllFuncCustData index UINT pCustData P.CUSTDATA
	cf GetAllParamCustData indexFunc UINT indexParam UINT pCustData P.CUSTDATA
	cf GetAllVarCustData index UINT pCustData P.CUSTDATA
	cf GetAllImplTypeCustData index UINT pCustData P.CUSTDATA
}