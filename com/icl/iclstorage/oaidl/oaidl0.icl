.icl
.ver 100
.gencommentlw

// forward-declare pointer types to generator parser
silent
{
	pie VARIANT LPVARIANT
	pie IDispatch LPDISPATCH
}

I ICreateTypeInfo ex IUnknown
{
	iid 00020405-0000-0000-C000-000000000046
	cf SetGuid guid R.GUID
	cf SetTypeFlags uTypeFlags UINT
	cf SetDocString pStrDoc LPOLESTR
	cf SetHelpContext dwHelpContext DWORD
	cf SetVersion wMajorVerNum WORD wMinorVerNum WORD
	cf AddRefTypeInfo pTInfo P.ITypeInfo phRefType P.HREFTYPE
	cf AddFuncDesc index UINT pFuncDesc P.FUNCDESC
	cf AddImplType index UINT hRefType HREFTYPE
	cf SetImplTypeFlags index UINT implTypeFlags INT
	cf SetAlignment cbAlignment WORD
	cf SetSchema pStrSchema LPOLESTR
	cf AddVarDesc index UINT pVarDesc P.VARDESC
	cf SetFuncAndParamNames index UINT rgszNames P.LPOLESTR cNames UINT
	cf SetVarName index UINT szName LPOLESTR
	cf SetTypeDescAlias pTDescAlias P.TYPEDESC
	cf DefineFuncAsDllEntry index UINT szDllName LPOLESTR szProcName LPOLESTR
	cf SetFuncDocString index UINT szDocString LPOLESTR
	cf SetVarDocString index UINT szDocString LPOLESTR
	cf SetFuncHelpContext index UINT dwHelpContext DWORD
	cf SetVarHelpContext index UINT dwHelpContext DWORD
	cf SetMops index UINT bstrMops BSTR
	cf SetTypeIdldesc pIdlDesc P.IDLDESC
	cf LayOut
}

pi LPCREATETYPEINFO

I ICreateTypeInfo2 ex ICreateTypeInfo
{
	iid 0002040E-0000-0000-C000-000000000046
	cf DeleteFuncDesc index UINT
	cf DeleteFuncDescByMemId memid MEMBERID invKind INVOKEKIND
	cf DeleteVarDesc index UINT
	cf DeleteVarDescByMemId memid MEMBERID
	cf DeleteImplType index UINT
	cf SetCustData guid R.GUID pVarVal P.VARIANT
	cf SetFuncCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf SetParamCustData indexFunc UINT indexParam UINT guid R.GUID pVarVal P.VARIANT
	cf SetVarCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf SetImplTypeCustData index UINT guid R.GUID pVarVal P.VARIANT
	cf SetHelpStringContext dwHelpStringContext ULONG
	cf SetFuncHelpStringContext index UINT dwHelpStringContext ULONG
	cf SetVarHelpStringContext index UINT dwHelpStringContext ULONG
	cf Invalidate
	cf SetName szName LPOLESTR
}

pi LPCREATETYPEINFO2

I ICreateTypeLib ex IUnknown
{
	iid 00020406-0000-0000-C000-000000000046
	cf CreateTypeInfo szName LPOLESTR tkind TYPEKIND ppCTInfo P.P.ICreateTypeInfo
	cf SetName szName LPOLESTR
	cf SetVersion wMajorVerNum WORD wMinorVerNum WORD
	cf SetDocString szDoc LPOLESTR
	cf SetGuid guid R.GUID
	cf SetDocString szDoc LPOLESTR
	cf SetHelpFileName szHelpFileName LPOLESTR
	cf SetHelpContext dwHelpContext DWORD
	cf SetLcid lcid LCID
	cf SetLibFlags uLibFlags UINT
	cf SaveAllChanges
}

pi LPCREATETYPELIB

I ICreateTypeLib2 ex ICreateTypeLib
{
	iid 0002040F-0000-0000-C000-000000000046
	cf DeleteTypeInfo szName LPOLESTR
	cf SetCustData guid R.GUID pVarVal P.VARIANT
	cf SetHelpStringContext dwHelpStringContext ULONG
	cf SetHelpStringDll szFileName LPOLESTR
}

pi LPCREATETYPELIB2

I IEnumVARIANT ex IUnknown
{
	cf Next celt ULONG rgVar P.VARIANT pCeltFetched PULONG
	cf Skip celt ULONG
	cf Reset
	cf Clone ppEnum FD.P.P.IEnumVARIANT
}