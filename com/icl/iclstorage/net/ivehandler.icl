.icl
.ver 100
.gencomment

silent
{
	pie SAFEARRAY LPSAFEARRAY
}

~
~from ..com.unknwn import *
~

sd _VerError
{
	sf IUlong flags
	sf IUlong opcode
	sf IUlong uOffset
	sf IUlong Token
	sf IUlong item1_flags
	sf PINT item1_data
	sf IUlong item2_flags 
	sf PINT item2_data
}

~VEContext = _VerError
~
~CLSID_VEHandlerClass = CLSID("{856CA1B1-7DAB-11d3-ACEC-00C04F86C309}")
~

I IVEHandler ex IUnknown
{
	iid 856CA1B2-7DAB-11d3-ACEC-00C04F86C309
	cf VEHandler VECode HRESULT Context VEContext psa P.SAFEARRAY
	cf SetReporterFtn lFnPtr PVOID
}