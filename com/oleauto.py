from .autointerfacedef import *
from .automationbase import *

from ..winnt import SYSTEMTIME, PSYSTEMTIME
from ..wtypes import VARIANT_BOOL

STDOLE_MAJORVERNUM  = 0x1
STDOLE_MINORVERNUM  = 0x0
STDOLE_LCID         = 0x0000

# Version # of stdole2.tlb
STDOLE2_MAJORVERNUM = 0x2
STDOLE2_MINORVERNUM = 0x0
STDOLE2_LCID        = 0x0000

#---------------------------------------------------------------------
#                            BSTR API                                 
#---------------------------------------------------------------------

@oleaut32.foreign(LPOLESTR, LPWSTR)
def SysAllocString(psz: LPWSTR) -> LPWSTR: ...

@oleaut32.foreign(INT, LPWSTR, LPWSTR)
def SysReAllocString(pbstr: LPWSTR, psz: LPWSTR) -> int: ...

@oleaut32.foreign(LPOLESTR, LPWSTR, UINT)
def SysAllocStringLen(strIn: LPWSTR, ui: int) -> LPWSTR: ...

@oleaut32.foreign(INT, LPWSTR, LPWSTR, UINT)
def SysReAllocStringLen(pbstr: LPWSTR, psz: LPWSTR, len: int) -> int: ...

@oleaut_foreign(LPOLESTR)
def SysAddRefString(bstrString: LPWSTR) -> int: ...

@oleaut32.foreign(None, LPOLESTR)
def SysReleaseString(bstrString: LPWSTR): ...

@oleaut32.foreign(None, LPOLESTR)
def SysFreeString(bstrString: LPWSTR): ...

@oleaut32.foreign(UINT, LPOLESTR)
def SysStringLen(pbstr: LPWSTR) -> int: ...

@oleaut32.foreign(UINT, LPOLESTR)
def SysStringByteLen(bstr: LPWSTR) -> int: ...

@oleaut32.foreign(LPOLESTR, LPSTR, UINT)
def SysAllocStringByteLen(psz: LPSTR, len: int) -> LPWSTR: ...

#---------------------------------------------------------------------
#                            Time API                                 
#---------------------------------------------------------------------

@oleaut32.foreign(INT, WORD, WORD, PTR(DOUBLE))
def DosDateTimeToVariantTime(wDosDate: int, wDosTime: int, pvtime: PFLOAT) -> int: ...

@oleaut32.foreign(INT, DOUBLE, PWORD, PWORD)
def VariantTimeToDosDateTime(vtime: float, pwDosDate: PWORD, pwDosTime: PWORD) -> int: ...

@oleaut32.foreign(INT, PSYSTEMTIME, PTR(DOUBLE))
def SystemTimeToVariantTime(lpSystemTime: IPointer[SYSTEMTIME], pvtime: PFLOAT) -> int: ...

@oleaut32.foreign(INT, DOUBLE, PSYSTEMTIME)
def VariantTimeToSystemTime(vtime: float, lpSystemTime: IPointer[SYSTEMTIME]) -> int: ...

#---------------------------------------------------------------------
#                          SafeArray API                              
#---------------------------------------------------------------------

@oleaut_foreign(UINT, PTR(LPSAFEARRAY))
def SafeArrayAllocDescriptor(cDims: int, ppsaOut: IDoublePtr[SAFEARRAY]) -> int: ...

@oleaut_foreign(WORD, UINT, PTR(LPSAFEARRAY))
def SafeArrayAllocDescriptorEx(vt: int, cDims: int, ppsaOut: IDoublePtr[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayAllocData(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut32.foreign(LPSAFEARRAY, WORD, UINT, PTR(SAFEARRAYBOUND))
def SafeArrayCreate(vt: int, cDims: int, rgsabound: IPointer[SAFEARRAYBOUND]) -> IPointer[SAFEARRAY]: ...

@oleaut32.foreign(LPSAFEARRAY, WORD, UINT, PTR(SAFEARRAYBOUND), PVOID)
def SafeArrayCreateEx(vt: int, cDims: int, rgsabound: IPointer[SAFEARRAYBOUND], pvExtra: PVOID) -> IPointer[SAFEARRAY]: ...

@oleaut_foreign(LPSAFEARRAY, LPSAFEARRAY)
def SafeArrayCopyData(psaSource: IPointer[SAFEARRAY], psaTarget: IPointer[SAFEARRAY]) -> int: ...

@oleaut32.foreign(None, LPSAFEARRAY)
def SafeArrayReleaseDescriptor(psa: IPointer[SAFEARRAY]): ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayDestroyDescriptor(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut32.foreign(None, PVOID)
def SafeArrayReleaseData(pData: PVOID): ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayDestroyData(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PTR(PVOID))
def SafeArrayAddRef(psa: IPointer[SAFEARRAY], ppDataToRelease: IPointer[PVOID]) -> int: ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayDestroy(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PTR(SAFEARRAYBOUND))
def SafeArrayRedim(psa: IPointer[SAFEARRAY], psaboundNew: IPointer[SAFEARRAYBOUND]) -> int: ...

@oleaut32.foreign(UINT, LPSAFEARRAY)
def SafeArrayGetDim(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut32.foreign(UINT, LPSAFEARRAY)
def SafeArrayGetElemsize(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, UINT, PLONG)
def SafeArrayGetUBound(psa: IPointer[SAFEARRAY], nDim: int, plUbound: PLONG) -> int: ...

@oleaut_foreign(LPSAFEARRAY, UINT, PLONG)
def SafeArrayGetLBound(psa: IPointer[SAFEARRAY], nDim: int, plLbound: PLONG) -> int: ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayLock(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayUnlock(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PVOID)
def SafeArrayAccessData(psa: IPointer[SAFEARRAY], ppvData: IPointer[PVOID]) -> int: ...

@oleaut_foreign(LPSAFEARRAY)
def SafeArrayUnaccessData(psa: IPointer[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PLONG, PVOID)
def SafeArrayGetElement(psa: IPointer[SAFEARRAY], rgIndices: PLONG, pv: IVoidPtr) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PLONG, PVOID)
def SafeArrayPutElement(psa: IPointer[SAFEARRAY], rgIndices: PLONG, pv: IVoidPtr) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PTR(LPSAFEARRAY))
def SafeArrayCopy(psa: IPointer[SAFEARRAY], ppsaOut: IDoublePtr[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PLONG, PVOID)
def SafeArrayPtrOfIndex(psa: IPointer[SAFEARRAY], rgIndices: PLONG, ppvData: IPointer[PVOID]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PTR(IRecordInfo))
def SafeArraySetRecordInfo(psa: IPointer[SAFEARRAY], prinfo: IPointer[IRecordInfo]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, DOUBLE_PTR(IRecordInfo))
def SafeArrayGetRecordInfo(psa: IPointer[SAFEARRAY], prinfo: IDoublePtr[IRecordInfo]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, REFGUID, intermediate_method=True)
def SafeArraySetIID(psa: IPointer[SAFEARRAY], guid: GUID, **kwargs) -> int: 
    return delegate(psa, guid.ref())

@oleaut_foreign(LPSAFEARRAY, PGUID)
def SafeArrayGetIID(psa: IPointer[SAFEARRAY], pguid: IPointer[GUID]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, PWORD)
def SafeArrayGetVartype(psa: IPointer[SAFEARRAY], pvt: PWORD) -> int: ...

@oleaut32.foreign(LPSAFEARRAY, WORD, LONG, ULONG)
def SafeArrayCreateVector(vt: int, lLbound: int, cElements: int) -> IPointer[SAFEARRAY]: ...

@oleaut32.foreign(LPSAFEARRAY, WORD, LONG, ULONG, PVOID)
def SafeArrayCreateVectorEx(vt: int, lLbound: int, cElements: int, pvExtra: PVOID) -> IPointer[SAFEARRAY]: ...

#---------------------------------------------------------------------
#                           VARIANT API                               
#---------------------------------------------------------------------

@oleaut32.foreign(None, LPVARIANT)
def VariantInit(pvarg: IPointer[VARIANT]): ...

@oleaut_foreign(LPVARIANT)
def VariantClear(pvarg: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VariantCopy(pvargDest: IPointer[VARIANT], pvargSrc: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VariantCopyInd(pvarDest: IPointer[VARIANT], pvargSrc: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, WORD, WORD)
def VariantChangeType(pvargDest: IPointer[VARIANT], pvarSrc: IPointer[VARIANT], wFlags: int, vt: int) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, ULONG, WORD, WORD)
def VariantChangeTypeEx(pvargDest: IPointer[VARIANT], pvarSrc: IPointer[VARIANT], lcid: int, wFlags: int, vt: int) -> int: ...

# Flags for VariantChangeType/VariantChangeTypeEx
VARIANT_NOVALUEPROP      = 0x01
VARIANT_ALPHABOOL        = 0x02     # For VT_BOOL to VT_BSTR conversions,
                                    # convert to "True"/"False" instead of
                                    # "-1"/"0"
VARIANT_NOUSEROVERRIDE   = 0x04     # For conversions to/from VT_BSTR,
				                    # passes LOCALE_NOUSEROVERRIDE
				                    # to core coercion routines
VARIANT_CALENDAR_HIJRI   = 0x08
VARIANT_LOCALBOOL        = 0x10     # For VT_BOOL to VT_BSTR and back,
                                    # convert to local language rather than
                                    # English
VARIANT_CALENDAR_THAI		= 0x20  # SOUTHASIA calendar support
VARIANT_CALENDAR_GREGORIAN	= 0x40  # SOUTHASIA calendar support
VARIANT_USE_NLS             = 0x80  # NLS function call support

#---------------------------------------------------------------------
#                Vector <-> Bstr conversion APIs                      
#---------------------------------------------------------------------

@oleaut_foreign(LPOLESTR, PTR(LPSAFEARRAY))
def VectorFromBstr(bstr: LPWSTR, ppsa: IDoublePtr[SAFEARRAY]) -> int: ...

@oleaut_foreign(LPSAFEARRAY, LPWSTR)
def BstrFromVector(psa: IPointer[SAFEARRAY], pbstr: LPWSTR) -> int: ...

#---------------------------------------------------------------------
#                     Variant API Flags                               
#---------------------------------------------------------------------

# Any of the coersion functions that converts either from or to a string
# takes an additional lcid and dwFlags arguments. The lcid argument allows
# locale specific parsing to occur.  The dwFlags allow additional function
# specific condition to occur.  All function that accept the dwFlags argument
# can include either 0 or LOCALE_NOUSEROVERRIDE flag.

# The VarDateFromStr and VarBstrFromDate functions also accept the
# VAR_TIMEVALUEONLY and VAR_DATEVALUEONLY flags
VAR_TIMEVALUEONLY       = 0x00000001    # return time value
VAR_DATEVALUEONLY       = 0x00000002    # return date value

# VarDateFromUdate() only
VAR_VALIDDATE           = 0x00000004

# Accepted by all date & format APIs
VAR_CALENDAR_HIJRI      = 0x00000008    # use Hijri calender

# Booleans can optionally be accepted in localized form. Pass VAR_LOCALBOOL
# into VarBoolFromStr and VarBstrFromBool to use localized boolean names
VAR_LOCALBOOL           = 0x00000010

# When passed into VarFormat and VarFormatFromTokens, prevents substitution
# of formats in the case where a string is passed in that can not be
# coverted into the desired type. (for ex, 'Format("Hello", "General Number")')
VAR_FORMAT_NOSUBSTITUTE = 0x00000020

# For VarBstrFromDate only - forces years to be 4 digits rather than shortening
# to 2-digits when the years is in the date window.
VAR_FOURDIGITYEARS	= 0x00000040

# Use NLS functions to format date, currency, time, and number.
LOCALE_USE_NLS = 0x10000000

# SOUTHASIA START
# SOUTHASIA
# For VarBstrFromDate only - forces years to be 4 digits rather than shortening
# to 2-digits when the years is in the date window.
VAR_CALENDAR_THAI	   = 0x00000080
VAR_CALENDAR_GREGORIAN = 0x00000100
# SOUTHASIA END

VTDATEGRE_MAX = 2958465   # Dec 31, 9999, 0:0:0 in Gregorain Calendar
VTDATEGRE_MIN = -657434   # Jan  1,  100, 0:0:0 in Gregorain Calendar

#---------------------------------------------------------------------
#                     VARTYPE Coercion API                            
#---------------------------------------------------------------------

# Note: The routines that convert *from* a string are defined
# to take a OLECHAR* rather than a BSTR because no allocation is
# required, and this makes the routines a bit more generic.
# They may of course still be passed a BSTR as the strIn param.

@oleaut_foreign(SHORT, LPSTR)
def VarUI1FromI2(sIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(LONG, LPSTR)
def VarUI1FromI4(lIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(LONGLONG, LPSTR)
def VarUI1FromI8(i64In: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(FLOAT, LPSTR)
def VarUI1FromR4(fltIn: float, pbOut: LPSTR) -> int: ...

@oleaut_foreign(DOUBLE, LPSTR)
def VarUI1FromR8(dblIn: float, pbOut: LPSTR) -> int: ...

@oleaut_foreign(CY, LPSTR)
def VarUI1FromCy(cyIn: CY, pbOut: LPSTR) -> int: ...

@oleaut_foreign(DOUBLE, LPSTR)
def VarUI1FromDate(dateIn: float, pbOut: LPSTR) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, LPSTR)
def VarUI1FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, LPSTR)
def VarUI1FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(SHORT, LPSTR)
def VarUI1FromBool(boolIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(c_byte, LPSTR)
def VarUI1FromI1(cIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(WORD, LPSTR)
def VarUI1FromUI2(uiIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(ULONG, LPSTR)
def VarUI1FromUI4(ulIn: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(ULONGLONG, LPSTR)
def VarUI1FromUI8(ui64In: int, pbOut: LPSTR) -> int: ...

@oleaut_foreign(LPDECIMAL, LPSTR)
def VarUI1FromDec(pdecIn: IPointer[DEC], pbOut: LPSTR) -> int: ...

@oleaut_foreign(BYTE, PSHORT)
def VarI2FromUI1(bIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(LONG, PSHORT)
def VarI2FromI4(lIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(LONGLONG, PSHORT)
def VarI2FromI8(i64In: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(FLOAT, PSHORT)
def VarI2FromR4(fltIn: float, psOut: PSHORT) -> int: ...

@oleaut_foreign(DOUBLE, PSHORT)
def VarI2FromR8(dblIn: float, psOut: PSHORT) -> int: ...

@oleaut_foreign(CY, PSHORT)
def VarI2FromCy(cyIn: CY, psOut: PSHORT) -> int: ...

@oleaut_foreign(DOUBLE, PSHORT)
def VarI2FromDate(dateIn: float, psOut: PSHORT) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PSHORT)
def VarI2FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PSHORT)
def VarI2FromDisp(pdispIn: IPointer[IDispatch], lcid: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(SHORT, PSHORT)
def VarI2FromBool(boolIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(c_byte, PSHORT)
def VarI2FromI1(cIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(WORD, PSHORT)
def VarI2FromUI2(uiIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(ULONG, PSHORT)
def VarI2FromUI4(ulIn: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(ULONGLONG, PSHORT)
def VarI2FromUI8(ui64In: int, psOut: PSHORT) -> int: ...

@oleaut_foreign(LPDECIMAL, PSHORT)
def VarI2FromDec(pdecIn: IPointer[DEC], psOut: PSHORT) -> int: ...

@oleaut_foreign(BYTE, PLONG)
def VarI4FromUI1(bIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(SHORT, PLONG)
def VarI4FromI2(sIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(LONGLONG, PLONG)
def VarI4FromI8(i64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(FLOAT, PLONG)
def VarI4FromR4(fltIn: float, plOut: PLONG) -> int: ...

@oleaut_foreign(DOUBLE, PLONG)
def VarI4FromR8(dblIn: float, plOut: PLONG) -> int: ...

@oleaut_foreign(CY, PLONG)
def VarI4FromCy(cyIn: CY, plOut: PLONG) -> int: ...

@oleaut_foreign(DOUBLE, PLONG)
def VarI4FromDate(dateIn: float, plOut: PLONG) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PLONG)
def VarI4FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, plOut: PLONG) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PLONG)
def VarI4FromDisp(pdispIn: IPointer[IDispatch], lcid: int, plOut: PLONG) -> int: ...

@oleaut_foreign(SHORT, PLONG)
def VarI4FromBool(boolIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(c_byte, PLONG)
def VarI4FromI1(cIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(WORD, PLONG)
def VarI4FromUI2(uiIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(ULONG, PLONG)
def VarI4FromUI4(ulIn: int, plOut: PLONG) -> int: ...

@oleaut_foreign(ULONGLONG, PLONG)
def VarI4FromUI8(ui64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(LPDECIMAL, PLONG)
def VarI4FromDec(pdecIn: IPointer[DEC], plOut: PLONG) -> int: ...

@oleaut_foreign(BYTE, PLONGLONG)
def VarI8FromUI1(bIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(SHORT, PLONGLONG)
def VarI8FromI2(sIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(FLOAT, PLONGLONG)
def VarI8FromR4(fltIn: float, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(DOUBLE, PLONGLONG)
def VarI8FromR8(dblIn: float, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(CY, PLONGLONG)
def VarI8FromCy(cyIn: CY, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(DOUBLE, PLONGLONG)
def VarI8FromDate(dateIn: float, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PLONGLONG)
def VarI8FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PLONGLONG)
def VarI8FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(SHORT, PLONGLONG)
def VarI8FromBool(boolIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(c_byte, PLONGLONG)
def VarI8FromI1(cIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(WORD, PLONGLONG)
def VarI8FromUI2(uiIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(ULONG, PLONGLONG)
def VarI8FromUI4(ulIn: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(ULONGLONG, PLONGLONG)
def VarI8FromUI8(ui64In: int, pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(LPDECIMAL, PLONGLONG)
def VarI8FromDec(pdecIn: IPointer[DEC], pi64Out: IPointer[LONGLONG]) -> int: ...

@oleaut_foreign(BYTE, PFLOAT)
def VarR4FromUI1(bIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(SHORT, PFLOAT)
def VarR4FromI2(sIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(LONG, PFLOAT)
def VarR4FromI4(lIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(LONGLONG, PFLOAT)
def VarR4FromI8(i64In: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(DOUBLE, PFLOAT)
def VarR4FromR8(dblIn: float, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(CY, PFLOAT)
def VarR4FromCy(cyIn: CY, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(DOUBLE, PFLOAT)
def VarR4FromDate(dateIn: float, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PFLOAT)
def VarR4FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PFLOAT)
def VarR4FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(SHORT, PFLOAT)
def VarR4FromBool(boolIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(c_byte, PFLOAT)
def VarR4FromI1(cIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(WORD, PFLOAT)
def VarR4FromUI2(uiIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(ULONG, PFLOAT)
def VarR4FromUI4(ulIn: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(ULONGLONG, PFLOAT)
def VarR4FromUI8(ui64In: int, pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(LPDECIMAL, PFLOAT)
def VarR4FromDec(pdecIn: IPointer[DEC], pfltOut: PFLOAT) -> int: ...

@oleaut_foreign(BYTE, PTR(DOUBLE))
def VarR8FromUI1(bIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(SHORT, PTR(DOUBLE))
def VarR8FromI2(sIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(LONG, PTR(DOUBLE))
def VarR8FromI4(lIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(LONGLONG, PTR(DOUBLE))
def VarR8FromI8(i64In: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(FLOAT, PTR(DOUBLE))
def VarR8FromR4(fltIn: float, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(CY, PTR(DOUBLE))
def VarR8FromCy(cyIn: CY, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(DOUBLE, PTR(DOUBLE))
def VarR8FromDate(dateIn: float, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PTR(DOUBLE))
def VarR8FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PTR(DOUBLE))
def VarR8FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(SHORT, PTR(DOUBLE))
def VarR8FromBool(boolIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(c_byte, PTR(DOUBLE))
def VarR8FromI1(cIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(WORD, PTR(DOUBLE))
def VarR8FromUI2(uiIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(ULONG, PTR(DOUBLE))
def VarR8FromUI4(ulIn: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(ULONGLONG, PTR(DOUBLE))
def VarR8FromUI8(ui64In: int, pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(LPDECIMAL, PTR(DOUBLE))
def VarR8FromDec(pdecIn: IPointer[DEC], pdblOut: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(BYTE, PTR(DOUBLE))
def VarDateFromUI1(bIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(SHORT, PTR(DOUBLE))
def VarDateFromI2(sIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(LONG, PTR(DOUBLE))
def VarDateFromI4(lIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(LONGLONG, PTR(DOUBLE))
def VarDateFromI8(i64In: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(FLOAT, PTR(DOUBLE))
def VarDateFromR4(fltIn: float, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(DOUBLE, PTR(DOUBLE))
def VarDateFromR8(dblIn: float, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(CY, PTR(DOUBLE))
def VarDateFromCy(cyIn: CY, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PTR(DOUBLE))
def VarDateFromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PTR(DOUBLE))
def VarDateFromDisp(pdispIn: IPointer[IDispatch], lcid: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(SHORT, PTR(DOUBLE))
def VarDateFromBool(boolIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(c_byte, PTR(DOUBLE))
def VarDateFromI1(cIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(WORD, PTR(DOUBLE))
def VarDateFromUI2(uiIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(ULONG, PTR(DOUBLE))
def VarDateFromUI4(ulIn: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(ULONGLONG, PTR(DOUBLE))
def VarDateFromUI8(ui64In: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(LPDECIMAL, PTR(DOUBLE))
def VarDateFromDec(pdecIn: IPointer[DEC], pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(BYTE, LPCY)
def VarCyFromUI1(bIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(SHORT, LPCY)
def VarCyFromI2(sIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(LONG, LPCY)
def VarCyFromI4(lIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(LONGLONG, LPCY)
def VarCyFromI8(i64In: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(FLOAT, LPCY)
def VarCyFromR4(fltIn: float, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(DOUBLE, LPCY)
def VarCyFromR8(dblIn: float, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(DOUBLE, LPCY)
def VarCyFromDate(dateIn: float, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, LPCY)
def VarCyFromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, LPCY)
def VarCyFromDisp(pdispIn: IPointer[IDispatch], lcid: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(SHORT, LPCY)
def VarCyFromBool(boolIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(c_byte, LPCY)
def VarCyFromI1(cIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(WORD, LPCY)
def VarCyFromUI2(uiIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(ULONG, LPCY)
def VarCyFromUI4(ulIn: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(ULONGLONG, LPCY)
def VarCyFromUI8(ui64In: int, pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPCY)
def VarCyFromDec(pdecIn: IPointer[DEC], pcyOut: IPointer[CY]) -> int: ...

@oleaut_foreign(BYTE, ULONG, ULONG, LPWSTR)
def VarBstrFromUI1(bVal: BYTE, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(SHORT, ULONG, ULONG, LPWSTR)
def VarBstrFromI2(iVal: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LONG, ULONG, ULONG, LPWSTR)
def VarBstrFromI4(lIn: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LONGLONG, ULONG, ULONG, LPWSTR)
def VarBstrFromI8(i64In: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(FLOAT, ULONG, ULONG, LPWSTR)
def VarBstrFromR4(fltIn: float, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(DOUBLE, ULONG, ULONG, LPWSTR)
def VarBstrFromR8(dblIn: float, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(CY, ULONG, ULONG, LPWSTR)
def VarBstrFromCy(cyIn: CY, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(DOUBLE, ULONG, ULONG, LPWSTR)
def VarBstrFromDate(dateIn: float, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, ULONG, LPWSTR)
def VarBstrFromDisp(pdispIn: IPointer[IDispatch], lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(SHORT, ULONG, ULONG, LPWSTR)
def VarBstrFromBool(boolIn: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(c_byte, ULONG, ULONG, LPWSTR)
def VarBstrFromI1(cIn: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(WORD, ULONG, ULONG, LPWSTR)
def VarBstrFromUI2(uiIn: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(ULONG, ULONG, ULONG, LPWSTR)
def VarBstrFromUI4(ulIn: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(ULONGLONG, ULONG, ULONG, LPWSTR)
def VarBstrFromUI8(ui64In: int, lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPDECIMAL, ULONG, ULONG, LPWSTR)
def VarBstrFromDec(pdecIn: IPointer[DEC], lcid: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

PVARIANT_BOOL = PTR(VARIANT_BOOL)

@oleaut_foreign(BYTE, PVARIANT_BOOL)
def VarBoolFromUI1(bIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(SHORT, PVARIANT_BOOL)
def VarBoolFromI2(sIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(LONG, PVARIANT_BOOL)
def VarBoolFromI4(lIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(LONGLONG, PVARIANT_BOOL)
def VarBoolFromI8(i64In: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(FLOAT, PVARIANT_BOOL)
def VarBoolFromR4(fltIn: float, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(DOUBLE, PVARIANT_BOOL)
def VarBoolFromR8(dblIn: float, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(DOUBLE, PVARIANT_BOOL)
def VarBoolFromDate(dateIn: float, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(CY, PVARIANT_BOOL)
def VarBoolFromCy(cyIn: CY, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PVARIANT_BOOL)
def VarBoolFromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PVARIANT_BOOL)
def VarBoolFromDisp(pdispIn: IPointer[IDispatch], lcid: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(c_byte, PVARIANT_BOOL)
def VarBoolFromI1(cIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(WORD, PVARIANT_BOOL)
def VarBoolFromUI2(uiIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(ULONG, PVARIANT_BOOL)
def VarBoolFromUI4(ulIn: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(ULONGLONG, PVARIANT_BOOL)
def VarBoolFromUI8(i64In: int, pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(LPDECIMAL, PVARIANT_BOOL)
def VarBoolFromDec(pdecIn: IPointer[DEC], pboolOut: IPointer[VARIANT_BOOL]) -> int: ...

@oleaut_foreign(BYTE, LPSTR)
def VarI1FromUI1(bIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(SHORT, LPSTR)
def VarI1FromI2(uiIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(LONG, LPSTR)
def VarI1FromI4(lIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(LONGLONG, LPSTR)
def VarI1FromI8(i64In: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(FLOAT, LPSTR)
def VarI1FromR4(fltIn: float, pcOut: LPSTR) -> int: ...

@oleaut_foreign(DOUBLE, LPSTR)
def VarI1FromR8(dblIn: float, pcOut: LPSTR) -> int: ...

@oleaut_foreign(DOUBLE, LPSTR)
def VarI1FromDate(dateIn: float, pcOut: LPSTR) -> int: ...

@oleaut_foreign(CY, LPSTR)
def VarI1FromCy(cyIn: CY, pcOut: LPSTR) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, LPSTR)
def VarI1FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, LPSTR)
def VarI1FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(SHORT, LPSTR)
def VarI1FromBool(boolIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(WORD, LPSTR)
def VarI1FromUI2(uiIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(ULONG, LPSTR)
def VarI1FromUI4(ulIn: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(ULONGLONG, LPSTR)
def VarI1FromUI8(i64In: int, pcOut: LPSTR) -> int: ...

@oleaut_foreign(LPDECIMAL, LPSTR)
def VarI1FromDec(pdecIn: IPointer[DEC], pcOut: LPSTR) -> int: ...

@oleaut_foreign(BYTE, PWORD)
def VarUI2FromUI1(bIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(SHORT, PWORD)
def VarUI2FromI2(uiIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(LONG, PWORD)
def VarUI2FromI4(lIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(LONGLONG, PWORD)
def VarUI2FromI8(i64In: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(FLOAT, PWORD)
def VarUI2FromR4(fltIn: float, puiOut: PUINT) -> int: ...

@oleaut_foreign(DOUBLE, PWORD)
def VarUI2FromR8(dblIn: float, puiOut: PUINT) -> int: ...

@oleaut_foreign(DOUBLE, PWORD)
def VarUI2FromDate(dateIn: float, puiOut: PUINT) -> int: ...

@oleaut_foreign(CY, PWORD)
def VarUI2FromCy(cyIn: CY, puiOut: PUINT) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PWORD)
def VarUI2FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PWORD)
def VarUI2FromDisp(pdispIn: IPointer[IDispatch], lcid: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(SHORT, PWORD)
def VarUI2FromBool(boolIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(c_byte, PWORD)
def VarUI2FromI1(cIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(ULONG, PWORD)
def VarUI2FromUI4(ulIn: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(ULONGLONG, PWORD)
def VarUI2FromUI8(i64In: int, puiOut: PUINT) -> int: ...

@oleaut_foreign(LPDECIMAL, PWORD)
def VarUI2FromDec(pdecIn: IPointer[DEC], puiOut: PUINT) -> int: ...

@oleaut_foreign(BYTE, PULONG)
def VarUI4FromUI1(bIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(SHORT, PULONG)
def VarUI4FromI2(uiIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(LONG, PULONG)
def VarUI4FromI4(lIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(LONGLONG, PULONG)
def VarUI4FromI8(i64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(FLOAT, PULONG)
def VarUI4FromR4(fltIn: float, pulOut: PULONG) -> int: ...

@oleaut_foreign(DOUBLE, PULONG)
def VarUI4FromR8(dblIn: float, pulOut: PULONG) -> int: ...

@oleaut_foreign(DOUBLE, PULONG)
def VarUI4FromDate(dateIn: float, pulOut: PULONG) -> int: ...

@oleaut_foreign(CY, PULONG)
def VarUI4FromCy(cyIn: CY, pulOut: PULONG) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PULONG)
def VarUI4FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PULONG)
def VarUI4FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(SHORT, PULONG)
def VarUI4FromBool(boolIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(c_byte, PULONG)
def VarUI4FromI1(cIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(WORD, PULONG)
def VarUI4FromUI2(uiIn: int, pulOut: PULONG) -> int: ...

@oleaut_foreign(ULONGLONG, PULONG)
def VarUI4FromUI8(ui64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(LPDECIMAL, PULONG)
def VarUI4FromDec(pdecIn: IPointer[DEC], pulOut: PULONG) -> int: ...

@oleaut_foreign(BYTE, PULONGLONG)
def VarUI8FromUI1(bIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(SHORT, PULONGLONG)
def VarUI8FromI2(sIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

# No implementation problem
# @oleaut_foreign(LONG, PULONGLONG)
# def VarUI8FromI4(lIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(LONGLONG, PULONGLONG)
def VarUI8FromI8(ui64In: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(FLOAT, PULONGLONG)
def VarUI8FromR4(fltIn: float, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(DOUBLE, PULONGLONG)
def VarUI8FromR8(dblIn: float, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(CY, PULONGLONG)
def VarUI8FromCy(cyIn: CY, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(DOUBLE, PULONGLONG)
def VarUI8FromDate(dateIn: float, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PULONGLONG)
def VarUI8FromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, PULONGLONG)
def VarUI8FromDisp(pdispIn: IPointer[IDispatch], lcid: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(SHORT, PULONGLONG)
def VarUI8FromBool(boolIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(c_byte, PULONGLONG)
def VarUI8FromI1(cIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(WORD, PULONGLONG)
def VarUI8FromUI2(uiIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(ULONG, PULONGLONG)
def VarUI8FromUI4(ulIn: int, pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(LPDECIMAL, PULONGLONG)
def VarUI8FromDec(pdecIn: IPointer[DEC], pi64Out: IPointer[ULONGLONG]) -> int: ...

@oleaut_foreign(BYTE, LPDECIMAL)
def VarDecFromUI1(bIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(SHORT, LPDECIMAL)
def VarDecFromI2(uiIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(LONG, LPDECIMAL)
def VarDecFromI4(lIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(LONGLONG, LPDECIMAL)
def VarDecFromI8(i64In: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(FLOAT, LPDECIMAL)
def VarDecFromR4(fltIn: float, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(DOUBLE, LPDECIMAL)
def VarDecFromR8(dblIn: float, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(DOUBLE, LPDECIMAL)
def VarDecFromDate(dateIn: float, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(CY, LPDECIMAL)
def VarDecFromCy(cyIn: CY, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, LPDECIMAL)
def VarDecFromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(LPDISPATCH, ULONG, LPDECIMAL)
def VarDecFromDisp(pdispIn: IPointer[IDispatch], lcid: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(SHORT, LPDECIMAL)
def VarDecFromBool(boolIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(c_byte, LPDECIMAL)
def VarDecFromI1(cIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(WORD, LPDECIMAL)
def VarDecFromUI2(uiIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(ULONG, LPDECIMAL)
def VarDecFromUI4(ulIn: int, pdecOut: IPointer[DEC]) -> int: ...

@oleaut_foreign(ULONGLONG, LPDECIMAL)
def VarDecFromUI8(ui64In: int, pdecOut: IPointer[DEC]) -> int: ...

def VarUI4FromUI4(in_: int, pOut: PULONG):
    pOut.contents = in_
    
def VarI4FromI4(in_: int, pOut: PLONG):
    pOut.contents = in_

def VarUI8FromUI8(in_: int, pOut: IPointer[ULONGLONG]):
    pOut.contents = in_
    
def VarI8FromI8(in_: int, pOut: IPointer[LONGLONG]):
    pOut.contents = in_
    
VarUI1FromInt       = VarUI1FromI4
VarUI1FromUint      = VarUI1FromUI4
VarI2FromInt        = VarI2FromI4
VarI2FromUint       = VarI2FromUI4

VarI4FromInt        = VarI4FromI4

VarI4FromUint       = VarI4FromUI4
VarI8FromUint       = VarI8FromUI4
VarR4FromInt        = VarR4FromI4
VarR4FromUint       = VarR4FromUI4
VarR8FromInt        = VarR8FromI4
VarR8FromUint       = VarR8FromUI4
VarDateFromInt      = VarDateFromI4
VarDateFromUint     = VarDateFromUI4
VarCyFromInt        = VarCyFromI4
VarCyFromUint       = VarCyFromUI4
VarBstrFromInt      = VarBstrFromI4
VarBstrFromUint     = VarBstrFromUI4
VarBoolFromInt      = VarBoolFromI4
VarBoolFromUint     = VarBoolFromUI4
VarI1FromInt        = VarI1FromI4
VarI1FromUint       = VarI1FromUI4
VarUI2FromInt       = VarUI2FromI4
VarUI2FromUint      = VarUI2FromUI4
VarUI4FromInt       = VarUI4FromI4
VarUI4FromUint      = VarUI4FromUI4
VarDecFromInt       = VarDecFromI4
VarDecFromUint      = VarDecFromUI4
VarIntFromUI1       = VarI4FromUI1
VarIntFromI2        = VarI4FromI2
VarIntFromI4        = VarI4FromI4
VarIntFromI8        = VarI4FromI8
VarIntFromR4        = VarI4FromR4
VarIntFromR8        = VarI4FromR8
VarIntFromDate      = VarI4FromDate
VarIntFromCy        = VarI4FromCy
VarIntFromStr       = VarI4FromStr
VarIntFromDisp      = VarI4FromDisp
VarIntFromBool      = VarI4FromBool
VarIntFromI1        = VarI4FromI1
VarIntFromUI2       = VarI4FromUI2
VarIntFromUI4       = VarI4FromUI4
VarIntFromUI8       = VarI4FromUI8
VarIntFromDec       = VarI4FromDec
VarIntFromUint      = VarI4FromUI4
VarUintFromUI1      = VarUI4FromUI1
VarUintFromI2       = VarUI4FromI2
VarUintFromI4       = VarUI4FromI4
VarUintFromI8       = VarUI4FromI8
VarUintFromR4       = VarUI4FromR4
VarUintFromR8       = VarUI4FromR8
VarUintFromDate     = VarUI4FromDate
VarUintFromCy       = VarUI4FromCy
VarUintFromStr      = VarUI4FromStr
VarUintFromDisp     = VarUI4FromDisp
VarUintFromBool     = VarUI4FromBool
VarUintFromI1       = VarUI4FromI1
VarUintFromUI2      = VarUI4FromUI2
VarUintFromUI4      = VarUI4FromUI4
VarUintFromUI8      = VarUI4FromUI8
VarUintFromDec      = VarUI4FromDec
VarUintFromInt      = VarUI4FromI4

# Mac Note: On the Mac, the coersion functions support the
# Symantec C++ calling convention for float/double. To support
# float/double arguments compiled with the MPW C compiler,
# use the following APIs to move MPW float/double values into
# a VARIANT.

#---------------------------------------------------------------------
#            New VARIANT <-> string parsing functions                 
#---------------------------------------------------------------------

class NUMPARSE(CStructure):
    _fields_ = [
        ('cDig', INT),
        ('dwInFlags', ULONG),
        ('dwOutFlags', ULONG),
        ('cchUsed', INT),
        ('nBaseShift', INT),
        ('nPwr10', INT)
    ]
    
    cDig: int
    dwInFlags: int
    dwOutFlags: int
    cchUsed: int
    nBaseShift: int
    nPwr10: int

# flags used by both dwInFlags and dwOutFlags:
NUMPRS_LEADING_WHITE    = 0x0001
NUMPRS_TRAILING_WHITE   = 0x0002
NUMPRS_LEADING_PLUS     = 0x0004
NUMPRS_TRAILING_PLUS    = 0x0008
NUMPRS_LEADING_MINUS    = 0x0010
NUMPRS_TRAILING_MINUS   = 0x0020
NUMPRS_HEX_OCT          = 0x0040
NUMPRS_PARENS           = 0x0080
NUMPRS_DECIMAL          = 0x0100
NUMPRS_THOUSANDS        = 0x0200
NUMPRS_CURRENCY         = 0x0400
NUMPRS_EXPONENT         = 0x0800
NUMPRS_USE_ALL          = 0x1000
NUMPRS_STD              = 0x1FFF

# flags used by dwOutFlags only:
NUMPRS_NEG              = 0x10000
NUMPRS_INEXACT          = 0x20000

# flags used by VarNumFromParseNum to indicate acceptable result types:
VTBIT_I1        = (1 << VT_I1)
VTBIT_UI1       = (1 << VT_UI1)
VTBIT_I2        = (1 << VT_I2)
VTBIT_UI2       = (1 << VT_UI2)
VTBIT_I4        = (1 << VT_I4)
VTBIT_UI4       = (1 << VT_UI4)
VTBIT_I8		= (1 << VT_I8)
VTBIT_UI8		= (1 << VT_UI8)
VTBIT_R4        = (1 << VT_R4)
VTBIT_R8        = (1 << VT_R8)
VTBIT_CY        = (1 << VT_CY)
VTBIT_DECIMAL   = (1 << VT_DECIMAL)

@oleaut_foreign(LONGLONG, PLONG)
def VarI4FromI8(i64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(ULONGLONG, PLONG)
def VarI4FromUI8(ui64In: int, plOut: PLONG) -> int: ...

@oleaut_foreign(LPOLESTR, ULONG, ULONG, PTR(NUMPARSE), LPSTR)
def VarParseNumFromStr(strIn: LPOLESTR, lcid: int, dwFlags: int, pnumprs: IPointer[NUMPARSE], rgbDig: LPSTR) -> int: ...

@oleaut_foreign(PTR(NUMPARSE), LPSTR, ULONG, LPVARIANT)
def VarNumFromParseNum(pnumprs: IPointer[NUMPARSE], rgbDig: LPSTR, dwVtBits: int, pvar: IPointer[VARIANT]) -> int: ...

#---------------------------------------------------------------------
#                     VARTYPE Math API                                
#---------------------------------------------------------------------

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarAdd(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarAnd(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarCat(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarDiv(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarEqv(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarIdiv(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarImp(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarMod(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarMul(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarOr(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarPow(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarSub(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, LPVARIANT)
def VarXor(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VarAbs(pvarIn: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VarFix(pvarIn: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VarInt(pvarIn: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VarNeg(pvarIn: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT)
def VarNot(pvarIn: IPointer[VARIANT], pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, INT, LPVARIANT)
def VarRound(pvarIn: IPointer[VARIANT], cDecimals: int, pvarResult: IPointer[VARIANT]) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, ULONG, ULONG)
def VarCmp(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], lcid: int, dwFlags: int) -> int: ...

@oleaut_foreign(LPVARIANT, LPVARIANT, ULONG)
def VarCmp(pvarLeft: IPointer[VARIANT], pvarRight: IPointer[VARIANT], lcid: int) -> int: ...

# Decimal math
#

@oleaut_foreign(LPDECIMAL, LPDECIMAL, LPDECIMAL)
def VarDecAdd(pdecLeft: IPointer[DECIMAL], pdecRight: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL, LPDECIMAL)
def VarDecDiv(pdecLeft: IPointer[DECIMAL], pdecRight: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL, LPDECIMAL)
def VarDecMul(pdecLeft: IPointer[DECIMAL], pdecRight: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL, LPDECIMAL)
def VarDecSub(pdecLeft: IPointer[DECIMAL], pdecRight: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL)
def VarDecAbs(pdecIn: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL)
def VarDecFix(pdecIn: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL)
def VarDecInt(pdecIn: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL)
def VarDecNeg(pdecIn: IPointer[DECIMAL], pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, INT, LPDECIMAL)
def VarDecRound(pdecIn: IPointer[DECIMAL], cDecimals: int, pdecResult: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, LPDECIMAL)
def VarDecCmp(pdecLeft: IPointer[DECIMAL], pdecRight: IPointer[DECIMAL]) -> int: ...

@oleaut_foreign(LPDECIMAL, DOUBLE)
def VarDecCmpR8(pdecLeft: IPointer[DECIMAL], dblRight: float) -> int: ...

# Currency math
#

@oleaut_foreign(CY, CY, LPCY)
def VarCyAdd(cyLeft: CY, cyRight: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, CY, LPCY)
def VarCyMul(cyLeft: CY, cyRight: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LONG, LPCY)
def VarCyMulI4(cyLeft: CY, lRight: int, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LONGLONG, LPCY)
def VarCyMulI8(cyLeft: CY, lRight: int, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, CY, LPCY)
def VarCySub(cyLeft: CY, cyRight: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LPCY)
def VarCyAbs(cyIn: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LPCY)
def VarCyFix(cyIn: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LPCY)
def VarCyInt(cyIn: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, LPCY)
def VarCyNeg(cyIn: CY, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, INT, LPCY)
def VarCyRound(cyIn: CY, cDecimals: int, pcyResult: IPointer[CY]) -> int: ...

@oleaut_foreign(CY, CY)
def VarCyCmp(cyLeft: CY, cyRight: CY) -> int: ...

@oleaut_foreign(CY, DOUBLE)
def VarCyCmpR8(cyLeft: CY, dblRight: float) -> int: ...

# Misc support functions
#

@oleaut_foreign(LPOLESTR, LPOLESTR, LPBSTR)
def VarBstrCat(bstrLeft: LPWSTR, bstrRight: LPWSTR, pbstrResult: IPointer[BSTR]) -> int: ...

@oleaut_foreign(LPOLESTR, LPOLESTR, ULONG, ULONG)
def VarBstrCmp(bstrLeft: LPWSTR, bstrRight: LPWSTR, lcid: int, dwFlags: int) -> int: ...

@oleaut_foreign(DOUBLE, DOUBLE, PTR(DOUBLE))
def VarR8Pow(dblLeft: float, dblRight: float, pdblResult: IPointer[DOUBLE]) -> int: ...

@oleaut_foreign(FLOAT, DOUBLE)
def VarR4CmpR8(fltLeft: float, dblRight: float) -> int: ...

@oleaut_foreign(DOUBLE, INT, PTR(DOUBLE))
def VarR8Round(dblIn: float, cDecimals: int, pdblResult: IPointer[DOUBLE]) -> int: ...

# Compare results.  These are returned as a SUCCESS HResult.  Subtracting
# one gives the usual values of -1 for Less Than, 0 for Equal To, +1 for
# Greater Than.
#
VARCMP_LT   = 0
VARCMP_EQ   = 1
VARCMP_GT   = 2
VARCMP_NULL = 3

# VT_HARDTYPE tells the compare routine that the argument is a literal or
# otherwise declared of that specific type.  It causes comparison rules to
# change. For example, if a hard-type string is compared to a variant (not hard
# -type) number, the number is converted to string.  If a hard-type number is
# compared to a variant string, the string is converted to number.  If they're
# both variant, then number < string.
VT_HARDTYPE = VT_RESERVED

#---------------------------------------------------------------------
#                   New date functions                                
#---------------------------------------------------------------------

# The UDATE structure is used with VarDateFromUdate() and VarUdateFromDate().
# It represents an "unpacked date".

class UDATE(CStructure):
    _fields_ = [
        ('st', SYSTEMTIME),
        ('wDayOfYear', USHORT)
    ]
    
    st: SYSTEMTIME
    wDayOfYear: int

# APIs to "pack" and "unpack" dates.
# NOTE: Ex version of VarDateFromUdate obeys 2 digit year setting in
# control panel.

@oleaut_foreign(PTR(UDATE), ULONG, PTR(DOUBLE))
def VarDateFromUdate(pudateIn: IPointer[UDATE], dwFlags: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(PTR(UDATE), ULONG, ULONG, PTR(DOUBLE))
def VarDateFromUdateEx(pudateIn: IPointer[UDATE], lcid: int, dwFlags: int, pdateOut: PFLOAT) -> int: ...

@oleaut_foreign(DOUBLE, ULONG, PTR(UDATE))
def VarUdateFromDate(dateIn: float, dwFlags: int, pudateOut: IPointer[UDATE]) -> int: ...

# API to retrieve the secondary(altername) month names
# Useful for Hijri, Polish and Russian alternate month names

@oleaut_foreign(ULONG, DOUBLE_PTR(LPOLESTR))
def GetAltMonthNames(lcid: int, prgp: IDoublePtr[LPWSTR]) -> int: ...

#---------------------------------------------------------------------
#                 Format                                              
#---------------------------------------------------------------------

@oleaut_foreign(LPVARIANT, LPOLESTR, INT, INT, ULONG, LPWSTR)
def VarFormat(pvarIn: IPointer[VARIANT], pstrFormat: LPWSTR, iFirstDay: int, iFirstWeek: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPVARIANT, INT, ULONG, LPWSTR)
def VarFormatDateTime(pvarIn: IPointer[VARIANT], iNamedFormat: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPVARIANT, INT, INT, INT, INT, ULONG, LPWSTR)
def VarFormatNumber(pvarIn: IPointer[VARIANT], iNumDig: int, iIncLead: int, iUseParens: int, iGroup: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPVARIANT, INT, INT, INT, INT, ULONG, LPWSTR)
def VarFormatPercent(pvarIn: IPointer[VARIANT], iNumDig: int, iIncLead: int, iUseParens: int, iGroup: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPVARIANT, INT, INT, INT, INT, ULONG, LPWSTR)
def VarFormatCurrency(pvarIn: IPointer[VARIANT], iNumDig: int, iIncLead: int, iUseParens: int, iGroup: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(INT, INT, INT, ULONG, LPWSTR)
def VarWeekdayName(iWeekday: int, fAbbrev: int, iFirstDay: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(INT, INT, ULONG, LPWSTR)
def VarMonthName(iMonth: int, fAbbrev: int, dwFlags: int, pbstrOut: LPWSTR) -> int: ...

@oleaut_foreign(LPVARIANT, LPOLESTR, PBYTE, ULONG, LPWSTR, ULONG)
def VarFormatFromTokens(pvarIn: IPointer[VARIANT], pstrFormat: LPWSTR, pbTokCur: PBYTE, dwFlags: int, pbstrOut: LPWSTR, lcid: int) -> int: ...

@oleaut_foreign(LPOLESTR, PBYTE, INT, INT, INT, ULONG, PINT)
def VarTokenizeFormatString(pstrFormat: LPWSTR, rgbTok: PBYTE, cbTok: int, iFirstDay: int, iFirstWeek: int, lcid: int, pcbActual: PINT) -> int: ...

#---------------------------------------------------------------------
#                 ITypeLib                                            
#---------------------------------------------------------------------

LPTYPELIB = ITypeLib.PTR()

#---------------------------------------------------------------------
#                ITypeInfo                                            
#---------------------------------------------------------------------

MEMBERID_NIL = DISPID_UNKNOWN
ID_DEFAULTINST  = -2

# Flags for IDispatch::Invoke 
DISPATCH_METHOD         = 0x1
DISPATCH_PROPERTYGET    = 0x2
DISPATCH_PROPERTYPUT    = 0x4
DISPATCH_PROPERTYPUTREF = 0x8

#---------------------------------------------------------------------
#             TypeInfo API                                            
#---------------------------------------------------------------------

# compute a 16bit hash value for the given name

@oleaut32.foreign(ULONG, SYSKIND, ULONG, LPSTR)
def LHashValOfNameSysA(syskind: SYSKIND, lcid: int, szName: LPSTR) -> int: ...

@oleaut32.foreign(ULONG, SYSKIND, ULONG, LPWSTR)
def LHashValOfNameSys(syskind: SYSKIND, lcid: int, szName: LPWSTR) -> int: ...

@oleaut_foreign(LPOLESTR, PTR(LPTYPELIB))
def LoadTypeLib(szFile: LPOLESTR, pptlib: IDoublePtr[ITypeLib]) -> int: 
    """load the typelib from the file with the given filename"""

# Control how a type library is registered
REGKIND_DEFAULT = 0
REGKIND_REGISTER = 1
REGKIND_NONE = 2
REGKIND = INT

# Constants for specifying format in which TLB should be loaded
# (the default format is 32-bit on WIN32 and 64-bit on WIN64)
LOAD_TLB_AS_32BIT	= 0x20
LOAD_TLB_AS_64BIT	= 0x40
MASK_TO_RESET_TLB_BITS		= ~(LOAD_TLB_AS_32BIT | LOAD_TLB_AS_64BIT)

@oleaut_foreign(LPOLESTR, REGKIND, PTR(LPTYPELIB))
def LoadTypeLibEx(szFile: LPOLESTR, regkind: int, pptlib: IDoublePtr[ITypeLib]) -> int: ...

@oleaut_foreign(REFGUID, WORD, WORD, ULONG, PTR(LPTYPELIB), intermediate_method=True)
def LoadRegTypeLib(guid: GUID, wVerMajor: int, wVerMinor: int, lcid: int, pptlib: IDoublePtr[ITypeLib], **kwargs) -> int: 
    """load registered typelib"""
    return delegate(guid.ref(), wVerMajor, wVerMinor, lcid, pptlib)

@oleaut_foreign(REFGUID, WORD, WORD, ULONG, LPBSTR)
def QueryPathOfRegTypeLib(guid: GUID, wMaj: int, wMin: int, lcid: int, lpbstrPathName: IPointer[BSTR], **kwargs) -> int: 
    """get path to registered typelib"""
    return delegate(guid.ref(), wMaj, wMin, lcid, lpbstrPathName)

@oleaut_foreign(LPTYPELIB, LPOLESTR, LPOLESTR)
def RegisterTypeLib(ptlib: IPointer[ITypeLib], szFullPath: LPOLESTR, szHelpDir: LPOLESTR) -> int: 
    """add typelib to registry"""

@oleaut_foreign(REFGUID, WORD, WORD, ULONG, SYSKIND, intermediate_method=True)
def UnRegisterTypeLib(libID: GUID, wVerMajor: int, wVerMinor: int, lcid: int, syskind: SYSKIND, **kwargs) -> int: 
    """remove typelib from registry"""
    return delegate(libID.ref(), wVerMajor, wVerMinor, lcid, syskind)

@oleaut_foreign(LPTYPELIB, LPWSTR, LPWSTR)
def RegisterTypeLibForUser(ptlib: IPointer[ITypeLib], szFullPath: LPWSTR, szHelpDir: LPWSTR) -> int: 
    """Registers a type library for use by the calling user."""

@oleaut_foreign(REFGUID, WORD, WORD, ULONG, SYSKIND, intermediate_method=True)
def UnRegisterTypeLibForUser(libID: GUID, wMajorVerNum: int, wMinorVerNum: int, lcid: int, syskind: SYSKIND, **kwargs) -> int: 
    """Removes type library information that was registered by using RegisterTypeLibForUser."""
    return delegate(libID.ref(), wMajorVerNum, wMinorVerNum, lcid, syskind)

@oleaut_foreign(SYSKIND, LPOLESTR, DOUBLE_PTR(ICreateTypeLib))
def CreateTypeLib(syskind: SYSKIND, szFile: LPOLESTR, ppctlib: IDoublePtr[ICreateTypeLib]) -> int: ...

@oleaut_foreign(SYSKIND, LPOLESTR, DOUBLE_PTR(ICreateTypeLib2))
def CreateTypeLib2(syskind: SYSKIND, szFile: LPOLESTR, ppctlib: IDoublePtr[ICreateTypeLib2]) -> int: ...

#---------------------------------------------------------------------
#           IDispatch implementation support                          
#---------------------------------------------------------------------

class PARAMDATA(CStructure):
    _fields_ = [
        ('szName', LPOLESTR),
        ('vt', VARTYPE)
    ]
    
    szName: LPOLESTR # parameter name
    vt: int          # parameter type
    
LPPARAMDATA = PARAMDATA.PTR()

class METHODDATA(CStructure):
    _fields_ = [
        ('szName', LPOLESTR),
        ('ppdata', LPPARAMDATA),
        ('dispid', DISPID),
        ('iMeth', UINT),
        ('cc', CALLCONV),
        ('cArgs', UINT),
        ('wFlags', WORD),
        ('vtReturn', VARTYPE)
    ]
    
    szName: LPOLESTR # method name
    ppdata: IPointer[PARAMDATA] #pointer to an array of PARAMDATAs
    dispid: int # method ID
    iMeth: int # method index
    cc: int # calling convention
    cArgs: int # count of arguments
    wFlags: int # same wFlags as on IDispatch::Invoke()
    vtReturn: int

LPMETHODDATA = METHODDATA.PTR()

class INTERFACEDATA(CStructure):
    _fields_ = [
        ('pmethdata', LPMETHODDATA),
        ('cMembers', UINT)
    ]
    
    pmethdata: IPointer[METHODDATA] # pointer to an array of METHODDATAs
    cMembers: int # count of members

LPINTERFACEDATA = INTERFACEDATA.PTR()

@oleaut_foreign(PTR(DISPPARAMS), UINT, WORD, LPVARIANT, PUINT)
def DispGetParam(pdispparams: IPointer[DISPPARAMS], position: int, vtTarg: int, pvarResult: IPointer[VARIANT], puArgErr: PUINT) -> int: 
    """
    Locate the parameter indicated by the given position, and
    return it coerced to the given target VARTYPE (vtTarg).
    """

@oleaut_foreign(PTR(ITypeInfo), LPWSTR, UINT, PLONG)
def DispGetIDsOfNames(ptinfo: IPointer[ITypeInfo], rgszNames: LPWSTR, cNames: int, rgdispid: PLONG) -> int: 
    """Automatic TypeInfo driven implementation of IDispatch::GetIDsOfNames()"""

@oleaut_foreign(PVOID, PTR(ITypeInfo), LONG, WORD, PTR(DISPPARAMS), LPVARIANT, LPEXCEPINFO, PUINT)
def DispInvoke(_this: IVoidPtr, ptinfo: IPointer[ITypeInfo], dispidMember: int, wFlags: int, pparams: IPointer[DISPPARAMS], pvarResult: IPointer[VARIANT], pexcepinfo: IPointer[EXCEPINFO], puArgErr: PUINT) -> int: 
    """Automatic TypeInfo driven implementation of IDispatch::Invoke()"""

@oleaut_foreign(PTR(INTERFACEDATA), ULONG, DOUBLE_PTR(ITypeInfo))
def CreateDispTypeInfo(pidata: IPointer[INTERFACEDATA], lcid: int, pptinfo: IDoublePtr[ITypeInfo]) -> int: 
    """Construct a TypeInfo from an interface data description"""

@oleaut_foreign(PTR(IUnknown), PVOID, PTR(ITypeInfo), DOUBLE_PTR(IUnknown))
def CreateStdDispatch(punkOuter: IPointer[IUnknown], pvThis: IVoidPtr, ptinfo: IPointer[ITypeInfo], ppunkStdDisp: IDoublePtr[IUnknown]) -> int: 
    """Create an instance of the standard TypeInfo driven IDispatch implementation."""

@oleaut_foreign(PVOID, ULONGLONG, CALLCONV, WORD, UINT, PWORD, PTR(LPVARIANT), LPVARIANT)
def DispCallFunc(pvInstance: IVoidPtr, oVft: int, cc: int, vtReturn: int, cActuals: int, prgvt: PWORD, prgpvarg: IDoublePtr[VARIANT], pvargResult: IPointer[VARIANT]) -> int: 
    """
    Low-level helper for IDispatch::Invoke() provides machine independence
    for customized Invoke().
    """

#---------------------------------------------------------------------
#            Active Object Registration API                           
#---------------------------------------------------------------------

# flags for RegisterActiveObject
ACTIVEOBJECT_STRONG = 0x0
ACTIVEOBJECT_WEAK = 0x1

@oleaut_foreign(PTR(IUnknown), REFCLSID, ULONG, PULONG, intermediate_method=True)
def RegisterActiveObject(punk: IPointer[IUnknown], clsid: CLSID, dwFlags: int, pdwRegister: PUINT, **kwargs) -> int:
    return delegate(punk, clsid.ref(), dwFlags, pdwRegister)

@oleaut_foreign(ULONG, PVOID)
def RevokeActiveObject(dwRegister: int, pvReserved: IVoidPtr) -> int: ...

@oleaut_foreign(REFCLSID, PVOID, DOUBLE_PTR(IUnknown), intermediate_method=True)
def GetActiveObject(clsid: CLSID, pvReserved: IVoidPtr, ppunk: IDoublePtr[IUnknown], **kwargs) -> int: 
    return delegate(clsid.ref(), pvReserved, ppunk)

#---------------------------------------------------------------------
#                           ErrorInfo API                             
#---------------------------------------------------------------------

@oleaut_foreign(ULONG, LPERRORINFO)
def SetErrorInfo(dwReserved: int, perrinfo: IPointer[IErrorInfo]) -> int: ...

@oleaut_foreign(ULONG, PTR(LPERRORINFO))
def GetErrorInfo(dwReserved: int, pperrinfo: IDoublePtr[IErrorInfo]) -> int: ...

@oleaut_foreign(PTR(LPCREATEERRORINFO))
def CreateErrorInfo(pperrinfo: IDoublePtr[ICreateErrorInfo]) -> int: ...

#---------------------------------------------------------------------
#           User Defined Data types support                           
#---------------------------------------------------------------------

@oleaut_foreign(LPTYPEINFO, PTR(LPRECORDINFO))
def GetRecordInfoFromTypeInfo(pTypeInfo: IPointer[ITypeInfo], ppRecInfo: IDoublePtr[IRecordInfo]) -> int: ...

@oleaut_foreign(REFGUID, ULONG, ULONG, ULONG, REFGUID, PTR(LPRECORDINFO), intermediate_method=True)
def GetRecordInfoFromGuids(guidTypeLib: GUID, uVerMajor: int, uVerMinor: int, lcid: int, guidTypeInfo: GUID, ppRecInfo: IDoublePtr[IRecordInfo]) -> int: 
    return delegate(guidTypeLib.ref(), uVerMajor, uVerMinor, lcid, guidTypeInfo.ref(), ppRecInfo)

#---------------------------------------------------------------------
#                           MISC API                                  
#---------------------------------------------------------------------

@oleaut32.foreign(ULONG)
def OaBuildVersion() -> int: ...

@oleaut32.foreign(None, LPCUSTDATA)
def ClearCustData(pCustData: IPointer[CUSTDATA]): ...

@oleaut32.foreign(None)
def OaEnablePerUserTLibRegistration(): ...