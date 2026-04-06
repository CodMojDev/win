.icl
.ver 100
.gencomment

silent
{
	pie IUnknown LPUNKNOWN
	pie SAFEARRAY LPSAFEARRAY
}

~
~from .ivehandler import *
~

ed ValidatorFlags
{
	ee VALIDATOR_EXTRA_VERBOSE 1
	ee VALIDATOR_SHOW_SOURCE_LINES 2
	ee VALIDATOR_CHECK_ILONLY 4
	ee VALIDATOR_CHECK_PEFORMAT_ONLY 8
	ee VALIDATOR_NOCHECK_PEFORMAT 16
	ee VALIDATOR_TRANSPARENT_ONLY 32
}

I IValidator ex IUnknown
{
	iid 63DF8730-DC81-4062-84A2-1FF943F59FAC
	cf Validate veh P.IVEHandler pAppDomain P.IUnknown ulFlags ULONG ulMaxError ULONG token ULONG fileName LPWSTR pe PBYTE ulSize ULONG
	cf FormatEventInfo hVECode HRESULT Context VEContext msg LPWSTR ulMaxLength ULONG psa P.SAFEARRAY
}

I ICLRValidator ex IUnknown
{
	iid 63DF8730-DC81-4062-84A2-1FF943F59FDD
	cf Validate veh P.IVEHandler ulAppDomainId ULONG ulFlags ULONG ulMaxError ULONG token ULONG fileName LPWSTR pe PBYTE ulSize ULONG
	cf FormatEventInfo hVECode HRESULT Context VEContext msg LPWSTR ulMaxLength ULONG psa P.SAFEARRAY
}