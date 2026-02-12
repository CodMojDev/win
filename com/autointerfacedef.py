#
# autointerfacedef.py
#

from .objinterfacedef import *
from .automationbase import *
from .oleidl import *
from .bstr import *

CURRENCY = CY

# #########################################################################
#      SAFEARRAY
# #########################################################################

class SAFEARRAYBOUND(CStructure):
    _fields_ = [
        ('cElements', ULONG),
        ('lLbound', LONG)
    ]
    
    cElements: int
    lLbound: int
    
LPSAFEARRAYBOUND = SAFEARRAYBOUND.PTR()

class wireBRECORD(CStructure):
    _fields_ = [
        ('fFlags', ULONG),
        ('clSize', ULONG),
        ('_pRecInfo', PVOID),
        ('pRecord', PBYTE)
    ]
    
    @property
    def pRecInfo(self) -> IPointer['IRecordInfo']:
        return i_cast(self._pRecInfo, LPRECORDINFO)
    
    pRecord: PBYTE
    fFlags: int
    clSize: int
    
class wireVARIANT(CStructure):
    class U(CUnion):
        _fields_ = [
            ('llVal', LONGLONG),
            ('lVal', LONG),
            ('bVal', BYTE),
            ('iVal', SHORT),
            ('fltVal', FLOAT),
            ('dblVal', DOUBLE),
            ('boolVal', VARIANT_BOOL),
            ('__OBSOLETE__VARIANT_BOOL', VARIANT_BOOL),
            ('scode', SCODE),
            ('cyVal', CY),
            ('date', DATE),
            ('bstrVal', BSTR),
            ('punkVal', LPUNKNOWN),
            ('brecVal', wireBRECORD),
            ('pbVal', PBYTE),
            ('piVal', PSHORT),
            ('plVal', PLONG),
            ('pllVal', PLONGLONG),
            ('pfltVal', PFLOAT),
            ('pdblVal', PTR(DOUBLE)),
            ('pboolVal', PTR(VARIANT_BOOL)),
            ('__OBSOLETE__VARIANT_PBOOL', PTR(VARIANT_BOOL)),
            ('pscode', PTR(SCODE)),
            ('pcyVal', LPCY),
            ('pdate', PTR(DATE)),
            ('pbstrVal', PTR(BSTR)),
            ('ppunkVal', PTR(LPUNKNOWN)),
            ('byref', PVOID),
            ('cVal', CHAR),
            ('uiVal', USHORT),
            ('ulVal', ULONG),
            ('ullVal', ULONGLONG),
            ('intVal', INT),
            ('uintVal', UINT),
            ('pdecVal', LPDECIMAL),
            ('pcVal', PCHAR),
            ('puiVal', PUSHORT),
            ('pulVal', PULONG),
            ('pullVal', PULONGLONG),
            ('pintVal', PINT),
            ('puintVal', PUINT)
        ]
    _fields_ = [
        ('clSize', DWORD),
        ('rpcReserved', DWORD),
        ('vt', USHORT),
        ('wReserved1', USHORT),
        ('wReserved2', USHORT),
        ('wReserved3', USHORT),
        ('u', U)
    ]
    
    vt: VARTYPE
    clSize: int
    
    llVal: int
    lVal: int
    bVal: int
    iVal: int
    fltVal: float
    dblVal: float
    boolVal: int
    scode: int
    cyVal: CY
    date: int
    bstrVal: wireBSTR
    punkVal: IPointer[IUnknown]
    parray: IPointer['wireSAFEARRAY']
    pbVal: PBYTE
    piVal: PSHORT
    plVal: PLONG
    pllVal: IPointer[LONGLONG]
    pfltVal: PFLOAT
    pdblVal: IPointer[DOUBLE]
    pboolVal: PINT
    pscode: PINT
    pcyVal: IPointer[CY]
    pdate: PFLOAT
    pbstrVal: IPointer[wireBSTR]
    ppunkVal: IDoublePtr[IUnknown]
    pparray: IDoublePtr['wireSAFEARRAY']
    byref: PVOID
    cVal: bytes
    uiVal: int
    ulVal: int
    ullVal: int
    intVal: int
    uintVal: int
    pdecVal: IPointer[DECIMAL]
    pcVal: PCHAR
    puiVal: PUSHORT
    pulVal: PULONG
    pullVal: IPointer[ULONGLONG]
    pintVal: PINT
    puintVal: PUINT
    pvRecord: PVOID
    
    @property
    def pvarVal(self) -> IPointer['wireVARIANT']:
        return i_cast(self.byref, wireVARIANT.PTR())
    
    @property
    def parray(self) -> IPointer['wireSAFEARRAY']:
        return i_cast(self.byref, wirePSAFEARRAY)
    
    @property
    def pparray(self) -> IDoublePtr['wireSAFEARRAY']:
        return i_cast(self.byref, PTR(wirePSAFEARRAY))
    
    @property
    def pdispVal(self) -> IPointer['IDispatch']:
        return i_cast(self, byref, LPDISPATCH)
    
    @property
    def ppdispVal(self) -> IDoublePtr['IDispatch']:
        return i_cast(self.byref, PTR(LPDISPATCH))

class SAFEARR_BSTR(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('aBstr', PTR(wireBSTR))
    ]
    
    aBstr: IDoublePtr[FLAGGED_WORD_BLOB]
    Size: int
    
class SAFEARR_UNKNOWN(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', PTR(LPUNKNOWN))
    ]
    
    apUnknown: IDoublePtr[IUnknown]
    Size: int
    
class SAFEARR_DISPATCH(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('_apDispatch', PVOID)
    ]
    
    @property
    def apDispatch(self) -> IDoublePtr['IDispatch']:
        return i_cast(self._apDispatch, PTR(LPDISPATCH))
    
    Size: int
    
class SAFEARR_VARIANT(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('aVariant', PTR(wireVARIANT))
    ]
    
class SAFEARR_BRECORD(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('aRecord', PTR(wireBRECORD))
    ]

class SAFEARR_HAVEIID(CStructure):
    _fields_ = [
        ('Size', ULONG),
        ('apUnknown', PTR(LPUNKNOWN)),
        ('iid', IID)
    ]
    
    apUnknown: IDoublePtr[IUnknown]
    Size: int
    iid: IID

SF_ERROR    = VT_ERROR,
SF_I1    = VT_I1,
SF_I2    = VT_I2,
SF_I4    = VT_I4,
SF_I8    = VT_I8,
SF_BSTR    = VT_BSTR,
SF_UNKNOWN    = VT_UNKNOWN,
SF_DISPATCH    = VT_DISPATCH,
SF_VARIANT    = VT_VARIANT,
SF_RECORD    = VT_RECORD,
SF_HAVEIID    = ( VT_UNKNOWN | VT_RESERVED ) 
SF_TYPE = INT

class SAFEARRAYUNION(CStructure):
    class U(CUnion):
        _fields_ = [
            ('BstrStr', SAFEARR_BSTR),
            ('UnknownStr', SAFEARR_UNKNOWN),
            ('DispatchStr', SAFEARR_DISPATCH),
            ('VariantStr', SAFEARR_VARIANT),
            ('RecordStr', SAFEARR_BRECORD),
            ('HaveIidStr', SAFEARR_HAVEIID),
            ('ByteStr', BYTE_SIZEDARR),
            ('WordStr', WORD_SIZEDARR),
            ('LongStr', DWORD_SIZEDARR),
            ('HyperStr', HYPER_SIZEDARR)
        ]
    _fields_ = [
        ('sfType', ULONG),
        ('u', U)
    ]
    _anonymous_ = ['u']
    
    BstrStr: SAFEARR_BSTR
    UnknownStr: SAFEARR_UNKNOWN
    DispatchStr: SAFEARR_DISPATCH
    VariantStr: SAFEARR_VARIANT
    RecordStr: SAFEARR_BRECORD
    HaveIidStr: SAFEARR_HAVEIID
    ByteStr: BYTE_SIZEDARR
    WordStr: WORD_SIZEDARR
    LongStr: DWORD_SIZEDARR
    HyperStr: HYPER_SIZEDARR
    sfType: int
    
class wireSAFEARRAY(CStructure):
    _fields_ = [
        ('cDims', USHORT),
        ('fFeatures', USHORT),
        ('cbElements', ULONG),
        ('cLocks', ULONG),
        ('uArrayStructs', SAFEARRAYUNION)
    ]
    
    rgsaBound: IPointer[SAFEARRAYBOUND]
    uArrayStructs: SAFEARRAYUNION
    cbElements: int
    fFeatures: int
    cLocks: int
    cDims: int
    
array_after_structure(wireSAFEARRAY, 'rgsaBound', SAFEARRAYBOUND)
wirePSAFEARRAY = wireSAFEARRAY.PTR()

class SAFEARRAY(CStructure):
    _fields_ = [
        ('cDims', USHORT),
        ('fFeatures', USHORT),
        ('cbElements', ULONG),
        ('cLocks', ULONG),
        ('pvData', PVOID)
    ]
    
    rgsaBound: IPointer[SAFEARRAYBOUND]
    cbElements: int
    fFeatures: int
    pvData: PVOID
    cLocks: int
    cDims: int
    
array_after_structure(SAFEARRAY, 'rgsaBound', SAFEARRAYBOUND)

LPSAFEARRAY = SAFEARRAY.PTR()

FADF_AUTO    = ( 0x1 )

FADF_STATIC    = ( 0x2 )

FADF_EMBEDDED    = ( 0x4 )

FADF_FIXEDSIZE    = ( 0x10 )

FADF_RECORD    = ( 0x20 )

FADF_HAVEIID    = ( 0x40 )

FADF_HAVEVARTYPE    = ( 0x80 )

FADF_BSTR    = ( 0x100 )

FADF_UNKNOWN    = ( 0x200 )

FADF_DISPATCH    = ( 0x400 )

FADF_VARIANT    = ( 0x800 )

FADF_RESERVED    = ( 0xf008 )

class VARIANT(CStructure):
    """
    ```
    VARIANT STRUCTURE
    *
    *  VARTYPE vt;
    *  WORD wReserved1;
    *  WORD wReserved2;
    *  WORD wReserved3;
    *  union {
    *    LONGLONG       VT_I8
    *    LONG           VT_I4
    *    BYTE           VT_UI1
    *    SHORT          VT_I2
    *    FLOAT          VT_R4
    *    DOUBLE         VT_R8
    *    VARIANT_BOOL   VT_BOOL
    *    SCODE          VT_ERROR
    *    CY             VT_CY
    *    DATE           VT_DATE
    *    BSTR           VT_BSTR
    *    IUnknown *     VT_UNKNOWN
    *    IDispatch *    VT_DISPATCH
    *    SAFEARRAY *    VT_ARRAY
    *    BYTE *         VT_BYREF|VT_UI1
    *    SHORT *        VT_BYREF|VT_I2
    *    LONG *         VT_BYREF|VT_I4
    *    LONGLONG *     VT_BYREF|VT_I8
    *    FLOAT *        VT_BYREF|VT_R4
    *    DOUBLE *       VT_BYREF|VT_R8
    *    VARIANT_BOOL * VT_BYREF|VT_BOOL
    *    SCODE *        VT_BYREF|VT_ERROR
    *    CY *           VT_BYREF|VT_CY
    *    DATE *         VT_BYREF|VT_DATE
    *    BSTR *         VT_BYREF|VT_BSTR
    *    IUnknown **    VT_BYREF|VT_UNKNOWN
    *    IDispatch **   VT_BYREF|VT_DISPATCH
    *    SAFEARRAY **   VT_BYREF|VT_ARRAY
    *    VARIANT *      VT_BYREF|VT_VARIANT
    *    PVOID          VT_BYREF (Generic ByRef)
    *    CHAR           VT_I1
    *    USHORT         VT_UI2
    *    ULONG          VT_UI4
    *    ULONGLONG      VT_UI8
    *    INT            VT_INT
    *    UINT           VT_UINT
    *    DECIMAL *      VT_BYREF|VT_DECIMAL
    *    CHAR *         VT_BYREF|VT_I1
    *    USHORT *       VT_BYREF|VT_UI2
    *    ULONG *        VT_BYREF|VT_UI4
    *    ULONGLONG *    VT_BYREF|VT_UI8
    *    INT *          VT_BYREF|VT_INT
    *    UINT *         VT_BYREF|VT_UINT
    *  }
    ```
    """
    class VARIANT_UNION(CUnion):
        class tagVARIANT(CStructure):
            class tagVARIANT_UNION(CUnion):
                class tagBRECORD(CStructure):
                    _fields_ = [
                        ('pvRecord', PVOID),
                        ('_pRecInfo', PVOID)
                    ]
                ############################
                ############################
                _anonymous_ = ['_s001']
                _fields_ = [
                    ('llVal', LONGLONG),
                    ('lVal', LONG),
                    ('bVal', BYTE),
                    ('iVal', SHORT),
                    ('fltVal', FLOAT),
                    ('dblVal', DOUBLE),
                    ('boolVal', VARIANT_BOOL),
                    ('__OBSOLETE__VARIANT_BOOL', VARIANT_BOOL),
                    ('scode', SCODE),
                    ('cyVal', CY),
                    ('date', DATE),
                    ('bstrVal', BSTR),
                    ('punkVal', LPUNKNOWN),
                    ('parray', LPSAFEARRAY),
                    ('pbVal', PBYTE),
                    ('piVal', PSHORT),
                    ('plVal', PLONG),
                    ('pllVal', PLONGLONG),
                    ('pfltVal', PFLOAT),
                    ('pdblVal', PTR(DOUBLE)),
                    ('pboolVal', PTR(VARIANT_BOOL)),
                    ('__OBSOLETE__VARIANT_PBOOL', PTR(VARIANT_BOOL)),
                    ('pscode', PTR(SCODE)),
                    ('pcyVal', LPCY),
                    ('pdate', PTR(DATE)),
                    ('pbstrVal', PTR(BSTR)),
                    ('ppunkVal', PTR(LPUNKNOWN)),
                    ('pparray', PTR(LPSAFEARRAY)),
                    ('byref', PVOID),
                    ('cVal', c_byte),
                    ('uiVal', USHORT),
                    ('ulVal', ULONG),
                    ('ullVal', ULONGLONG),
                    ('intVal', INT),
                    ('uintVal', UINT),
                    ('pdecVal', LPDECIMAL),
                    ('pcVal', PTR(c_byte)),
                    ('puiVal', PUSHORT),
                    ('pulVal', PULONG),
                    ('pullVal', PULONGLONG),
                    ('pintVal', PINT),
                    ('puintVal', PUINT),
                    ('_s001', tagBRECORD)
                ]
                ############################
                ############################
            
            _anonymous_ = ['_u001']
            _fields_ = [
                ('vt', VARTYPE),
                ('wReserved1', WORD),
                ('wReserved2', WORD),
                ('wReserved3', WORD),
                ('_u001', tagVARIANT_UNION)
            ]
        
        _anonymous_ = ['_s002']
        
        _fields_ = [
            ('_s002', tagVARIANT),
            ('decVal', DECIMAL)
        ]
    
    _anonymous_ = ['_u002']
    _fields_ = [
        ('_u002', VARIANT_UNION)
    ]
    
    vt: VARTYPE
    
    llVal: int
    lVal: int
    bVal: int
    iVal: int
    fltVal: float
    dblVal: float
    boolVal: int
    scode: int
    cyVal: CY
    date: int
    bstrVal: BSTR
    punkVal: IPointer[IUnknown]
    parray: IPointer[SAFEARRAY]
    pbVal: PBYTE
    piVal: PSHORT
    plVal: PLONG
    pllVal: IPointer[LONGLONG]
    pfltVal: PFLOAT
    pdblVal: IPointer[DOUBLE]
    pboolVal: PINT
    pscode: PINT
    pcyVal: IPointer[CY]
    pdate: PFLOAT
    pbstrVal: IPointer[BSTR]
    ppunkVal: IDoublePtr[IUnknown]
    pparray: IDoublePtr[SAFEARRAY]
    byref: PVOID
    cVal: int
    uiVal: int
    ulVal: int
    ullVal: int
    intVal: int
    uintVal: int
    pdecVal: IPointer[DECIMAL]
    pcVal: IPointer[c_byte]
    puiVal: PUSHORT
    pulVal: PULONG
    pullVal: IPointer[ULONGLONG]
    pintVal: PINT
    puintVal: PUINT
    pvRecord: PVOID
    
    @property
    def pvarVal(self) -> IPointer['VARIANT']:
        return i_cast(self.byref, LPVARIANT)
    
    @property
    def pRecInfo(self) -> IPointer['IRecordInfo']:
        return i_cast(self._pRecInfo, LPRECORDINFO)
    
    @property
    def pdispVal(self) -> IPointer['IDispatch']:
        return i_cast(self.byref, LPDISPATCH)
    
    @property
    def ppdispVal(self) -> IDoublePtr['IDispatch']:
        return i_cast(self.byref, PTR(LPDISPATCH))
        
LPVARIANTARG = REFVARIANT = LPVARIANT = VARIANT.PTR()
VARIANTARG = VARIANT

MEMBERID = DISPID = LONG
HREFTYPE = DWORD

TKIND_ENUM    = 0
TKIND_RECORD    = ( TKIND_ENUM + 1 )
TKIND_MODULE    = ( TKIND_RECORD + 1 )
TKIND_INTERFACE    = ( TKIND_MODULE + 1 )
TKIND_DISPATCH    = ( TKIND_INTERFACE + 1 )
TKIND_COCLASS    = ( TKIND_DISPATCH + 1 )
TKIND_ALIAS    = ( TKIND_COCLASS + 1 )
TKIND_UNION    = ( TKIND_ALIAS + 1 )
TKIND_MAX    = ( TKIND_UNION + 1 ) 
TYPEKIND = INT

class TYPEDESC(CStructure):
    class U(CUnion):
        _fields_ = [
            ('_lptdesc', PVOID),
            ('_lpadesc', PVOID),
            ('hreftype', HREFTYPE)
        ]
    _fields_ = [
        ('vt', VARTYPE),
        ('u', U)
    ]
    _anonymous_ = ['u']
    
    vt: int
    
    @property
    def lptdesc(self) -> IPointer['TYPEDESC']:
        return i_cast(self._lptdesc, TYPEDESC.PTR())
    
    @property
    def lpadesc(self) -> IPointer['ARRAYDESC']:
        return i_cast(self._lpadesc, ARRAYDESC.PTR())
    
class ARRAYDESC(CStructure):
    _fields_ = [
        ('tdescElem', TYPEDESC),
        ('cDims', USHORT)
    ]
    
    rgbounds: IPointer[SAFEARRAYBOUND]
    tdescElem: TYPEDESC
    cDims: int
    
array_after_structure(ARRAYDESC, 'rgbounds', SAFEARRAYBOUND)

class PARAMDESCEX(CStructure):
    _fields_ = [
        ('cBytes', ULONG),
        ('varDefault', VARIANTARG)
    ]
    
    varDefault: VARIANT
    cBytes: int
    
LPPARAMDESCEX = PARAMDESCEX.PTR()

class PARAMDESC(CStructure):
    _fields_ = [
        ('pparamdescex', LPPARAMDESCEX),
        ('wParamFlags', USHORT)
    ]
    
    pparamdescex: IPointer[PARAMDESCEX]
    wParamFlags: int
    
LPPARAMDESC = PARAMDESC.PTR()

PARAMFLAG_NONE    = ( 0 )

PARAMFLAG_FIN    = ( 0x1 )

PARAMFLAG_FOUT    = ( 0x2 )

PARAMFLAG_FLCID    = ( 0x4 )

PARAMFLAG_FRETVAL    = ( 0x8 )

PARAMFLAG_FOPT    = ( 0x10 )

PARAMFLAG_FHASDEFAULT    = ( 0x20 )

PARAMFLAG_FHASCUSTDATA    = ( 0x40 )

class IDLDESC(CStructure):
    _fields_ = [
        ('dwReserved', ULONG_PTR),
        ('wIDLFlags', USHORT)
    ]
    
    dwReserved: int
    wIDLFlags: int
    
LPIDLDESC = IDLDESC.PTR()

IDLFLAG_NONE    = ( PARAMFLAG_NONE )

IDLFLAG_FIN    = ( PARAMFLAG_FIN )

IDLFLAG_FOUT    = ( PARAMFLAG_FOUT )

IDLFLAG_FLCID    = ( PARAMFLAG_FLCID )

IDLFLAG_FRETVAL    = ( PARAMFLAG_FRETVAL )

class ELEMDESC(CStructure):
    class U(CUnion):
        _fields_ = [
            ('idldesc', IDLDESC),
            ('paramdesc', PARAMDESC)
        ]
    _fields_ = [
        ('tdesc', TYPEDESC),
        ('u', U)
    ]
    _anonymous_ = ['u']
    
    tdesc: TYPEDESC # the type of the element
    idldesc: int # info for remoting the element
    paramdesc: PARAMDESC # info about the parameter
    
LPELEMDESC = ELEMDESC.PTR()

class TYPEATTR(CStructure):
    _fields_ = [
        ('guid', GUID),
        ('lcid', LCID),
        ('dwReserved', DWORD),
        ('memidConstructor', MEMBERID),
        ('memidDestructor', MEMBERID),
        ('lpstrSchema', LPOLESTR),
        ('cbSizeInstance', ULONG),
        ('typekind', TYPEKIND),
        ('cFuncs', WORD),
        ('cVars', WORD),
        ('cImplTypes', WORD),
        ('cbSizeVft', WORD),
        ('cbAlignment', WORD),
        ('wTypeFlags', WORD),
        ('wMajorVerNum', WORD),
        ('wMinorVerNum', WORD),
        ('tdescAlias', TYPEDESC),
        ('idldescType', IDLDESC)
    ]
    
    guid: GUID
    lcid: LCID
    dwReserved: int
    memidConstructor: int
    memidDestructor: int
    lpstrSchema: LPOLESTR
    cbSizeInstance: int
    typekind: TYPEKIND
    cFuncs: int
    cVars: int
    cImplTypes: int
    cbSizeVft: int
    cbAlignment: int
    wTypeFlags: int
    wMajorVerNum: int
    wMinorVerNum:  int
    tdescAlias: TYPEDESC
    idldescType: int
    
LPTYPEATTR = TYPEATTR.PTR()

class DISPPARAMS(CStructure):
    _fields_ = [
        ("rgvarg", VARIANTARG.PTR()),
        ("rgdispidNamedArgs", PTR(DISPID)),
        ("cArgs", UINT),
        ("cNamedArgs", UINT),
    ]
    
    rgvarg: IArray[VARIANT]
    rgdispidNamedArgs: IPointer[DISPID]
    cArgs: int
    cNamedArgs: int
    
class EXCEPINFO(CStructure):
    _fields_ = [
        ('wCode', WORD),
        ('wReserved', WORD),
        ('bstrSource', BSTR),
        ('bstrDescription', BSTR),
        ('bstrHelpFile', BSTR),
        ('dwHelpContext', DWORD),
        ('pvReserved', PVOID),
        ('pfnDeferredFillIn', PVOID),
        ('scode', SCODE)
    ]
    
    bstrDescription: BSTR
    bstrHelpFile: BSTR
    dwHelpContext: int
    bstrSource: BSTR
    pvReserved: PVOID
    scode: int
    wCode: int
    
LPEXCEPINFO = EXCEPINFO.PTR()
    
CC_FASTCALL    = 0
CC_CDECL    = 1
CC_MSCPASCAL    = ( CC_CDECL + 1 )
CC_PASCAL    = CC_MSCPASCAL
CC_MACPASCAL    = ( CC_PASCAL + 1 )
CC_STDCALL    = ( CC_MACPASCAL + 1 )
CC_FPFASTCALL    = ( CC_STDCALL + 1 )
CC_SYSCALL    = ( CC_FPFASTCALL + 1 )
CC_MPWCDECL    = ( CC_SYSCALL + 1 )
CC_MPWPASCAL    = ( CC_MPWCDECL + 1 )
CC_MAX    = ( CC_MPWPASCAL + 1 ) 
CALLCONV = INT

FUNC_VIRTUAL    = 0
FUNC_PUREVIRTUAL    = ( FUNC_VIRTUAL + 1 )
FUNC_NONVIRTUAL    = ( FUNC_PUREVIRTUAL + 1 )
FUNC_STATIC    = ( FUNC_NONVIRTUAL + 1 )
FUNC_DISPATCH    = ( FUNC_STATIC + 1 ) 
FUNCKIND = INT

INVOKE_FUNC    = 1
INVOKE_PROPERTYGET    = 2
INVOKE_PROPERTYPUT    = 4
INVOKE_PROPERTYPUTREF    = 8
INVOKEKIND = INT

class FUNCDESC(CStructure):
    _fields_ = [
        ('memid', MEMBERID),
        ('lprgscode', PTR(SCODE)),
        ('lprgelemdescParam', LPELEMDESC),
        ('funckind', FUNCKIND),
        ('invkind', INVOKEKIND),
        ('callConv', CALLCONV),
        ('cParams', SHORT),
        ('cParamsOpt', SHORT),
        ('oVft', SHORT),
        ('cScodes', SHORT),
        ('elemdescFunc', ELEMDESC),
        ('wFuncFlags', WORD)
    ]
    
    lprgelemdescParam: IPointer[ELEMDESC]
    elemdescFunc: int
    wFuncFlags: int
    lprgscode: PINT
    cParamsOpt: int
    funckind: int
    callConv: int
    cParams: int
    cScodes: int
    invkind: int
    memid: int
    oVft: int
    
LPFUNCDESC = FUNCDESC.PTR()

VAR_PERINSTANCE    = 0
VAR_STATIC    = ( VAR_PERINSTANCE + 1 )
VAR_CONST    = ( VAR_STATIC + 1 )
VAR_DISPATCH    = ( VAR_CONST + 1 ) 
VARKIND = INT

IMPLTYPEFLAG_FDEFAULT    = ( 0x1 )

IMPLTYPEFLAG_FSOURCE    = ( 0x2 )

IMPLTYPEFLAG_FRESTRICTED    = ( 0x4 )

IMPLTYPEFLAG_FDEFAULTVTABLE    = ( 0x8 )

class VARDESC(CStructure):
    class U(CUnion):
        _fields_ = [
            ('oInst', ULONG),
            ('lpvarValue', LPVARIANT)
        ]
    _fields_ = [
        ('memid', MEMBERID),
        ('lpstrSchema', LPOLESTR),
        ('u', U),
        ('elemdescVar', ELEMDESC),
        ('wVarFlags', WORD),
        ('varkind', VARKIND)
    ]
    _anonymous_ = ['u']

    lpvarValue: IPointer[VARIANT]
    lpstrSchema: LPOLESTR
    elemdescVar: ELEMDESC
    wVarFlags: int
    varkind: int
    oInst: int
    memid: int
    
LPVARDESC = VARDESC.PTR()

TYPEFLAG_FAPPOBJECT    = 0x1
TYPEFLAG_FCANCREATE    = 0x2
TYPEFLAG_FLICENSED    = 0x4
TYPEFLAG_FPREDECLID    = 0x8
TYPEFLAG_FHIDDEN    = 0x10
TYPEFLAG_FCONTROL    = 0x20
TYPEFLAG_FDUAL    = 0x40
TYPEFLAG_FNONEXTENSIBLE    = 0x80
TYPEFLAG_FOLEAUTOMATION    = 0x100
TYPEFLAG_FRESTRICTED    = 0x200
TYPEFLAG_FAGGREGATABLE    = 0x400
TYPEFLAG_FREPLACEABLE    = 0x800
TYPEFLAG_FDISPATCHABLE    = 0x1000
TYPEFLAG_FREVERSEBIND    = 0x2000
TYPEFLAG_FPROXY    = 0x4000
TYPEFLAGS = INT

FUNCFLAG_FRESTRICTED    = 0x1
FUNCFLAG_FSOURCE    = 0x2
FUNCFLAG_FBINDABLE    = 0x4
FUNCFLAG_FREQUESTEDIT    = 0x8
FUNCFLAG_FDISPLAYBIND    = 0x10
FUNCFLAG_FDEFAULTBIND    = 0x20
FUNCFLAG_FHIDDEN    = 0x40
FUNCFLAG_FUSESGETLASTERROR    = 0x80
FUNCFLAG_FDEFAULTCOLLELEM    = 0x100
FUNCFLAG_FUIDEFAULT    = 0x200
FUNCFLAG_FNONBROWSABLE    = 0x400
FUNCFLAG_FREPLACEABLE    = 0x800
FUNCFLAG_FIMMEDIATEBIND    = 0x1000
FUNCFLAGS = INT

VARFLAG_FREADONLY    = 0x1
VARFLAG_FSOURCE    = 0x2
VARFLAG_FBINDABLE    = 0x4
VARFLAG_FREQUESTEDIT    = 0x8
VARFLAG_FDISPLAYBIND    = 0x10
VARFLAG_FDEFAULTBIND    = 0x20
VARFLAG_FHIDDEN    = 0x40
VARFLAG_FRESTRICTED    = 0x80
VARFLAG_FDEFAULTCOLLELEM    = 0x100
VARFLAG_FUIDEFAULT    = 0x200
VARFLAG_FNONBROWSABLE    = 0x400
VARFLAG_FREPLACEABLE    = 0x800
VARFLAG_FIMMEDIATEBIND    = 0x1000
VARFLAGS = INT

class CLEANLOCALSTORAGE(CStructure):
    _fields_ = [
        ('pInterface', LPUNKNOWN),
        ('pStorage', PVOID),
        ('flags', DWORD)
    ]
    
    pInterface: IPointer[IUnknown]
    pStorage: PVOID
    flags: int
    
class CUSTDATAITEM(CStructure):
    _fields_ = [
        ('guid', GUID),
        ('varValue', VARIANTARG)
    ]
    
    varValue: VARIANT
    guid: GUID
    
LPCUSTDATAITEM = CUSTDATAITEM.PTR()

class CUSTDATA(CStructure):
    _fields_ = [
        ('cCustData', DWORD),
        ('prgCustData', LPCUSTDATAITEM)
    ]
    
    prgCustData: IPointer[CUSTDATAITEM]
    cCustData: int
    
LPCUSTDATA = CUSTDATA.PTR()

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 14:11:27 2026
# Generated from ICL: oaidl0.icl
# {
class ICreateTypeInfo(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00020405-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPGUID, intermediate_method = True)
    def SetGuid(self, guid: GUID, **kwargs) -> int:
        return self.virt_delegate(guid.ref())

    @virtual_table.com_function(UINT)
    def SetTypeFlags(self, uTypeFlags: int) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetDocString(self, pStrDoc: LPOLESTR) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetHelpContext(self, dwHelpContext: int) -> int: ...

    @virtual_table.com_function(WORD, WORD)
    def SetVersion(self, wMajorVerNum: int, wMinorVerNum: int) -> int: ...

    @virtual_table.com_function(PVOID, PTR(HREFTYPE))
    def AddRefTypeInfo(self, pTInfo: IPointer['ITypeInfo'], phRefType: IPointer[HREFTYPE]) -> int: ...

    @virtual_table.com_function(UINT, PTR(FUNCDESC))
    def AddFuncDesc(self, index: int, pFuncDesc: IPointer[FUNCDESC]) -> int: ...

    @virtual_table.com_function(UINT, HREFTYPE)
    def AddImplType(self, index: int, hRefType: HREFTYPE) -> int: ...

    @virtual_table.com_function(UINT, INT)
    def SetImplTypeFlags(self, index: int, implTypeFlags: int) -> int: ...

    @virtual_table.com_function(WORD)
    def SetAlignment(self, cbAlignment: int) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetSchema(self, pStrSchema: LPOLESTR) -> int: ...

    @virtual_table.com_function(UINT, PTR(VARDESC))
    def AddVarDesc(self, index: int, pVarDesc: IPointer[VARDESC]) -> int: ...

    @virtual_table.com_function(UINT, PTR(LPOLESTR), UINT)
    def SetFuncAndParamNames(self, index: int, rgszNames: IPointer[LPOLESTR], cNames: int) -> int: ...

    @virtual_table.com_function(UINT, LPOLESTR)
    def SetVarName(self, index: int, szName: LPOLESTR) -> int: ...

    @virtual_table.com_function(PTR(TYPEDESC))
    def SetTypeDescAlias(self, pTDescAlias: IPointer[TYPEDESC]) -> int: ...

    @virtual_table.com_function(UINT, LPOLESTR, LPOLESTR)
    def DefineFuncAsDllEntry(self, index: int, szDllName: LPOLESTR, szProcName: LPOLESTR) -> int: ...

    @virtual_table.com_function(UINT, LPOLESTR)
    def SetFuncDocString(self, index: int, szDocString: LPOLESTR) -> int: ...

    @virtual_table.com_function(UINT, LPOLESTR)
    def SetVarDocString(self, index: int, szDocString: LPOLESTR) -> int: ...

    @virtual_table.com_function(UINT, DWORD)
    def SetFuncHelpContext(self, index: int, dwHelpContext: int) -> int: ...

    @virtual_table.com_function(UINT, DWORD)
    def SetVarHelpContext(self, index: int, dwHelpContext: int) -> int: ...

    @virtual_table.com_function(UINT, BSTR)
    def SetMops(self, index: int, bstrMops: BSTR) -> int: ...

    @virtual_table.com_function(PTR(IDLDESC))
    def SetTypeIdldesc(self, pIdlDesc: IPointer[IDLDESC]) -> int: ...

    @virtual_table.com_function()
    def LayOut(self) -> int: ...

    virtual_table.build()

LPCREATETYPEINFO = ICreateTypeInfo.PTR()

class ICreateTypeInfo2(ICreateTypeInfo):
    virtual_table = COMVirtualTable.from_ancestor(ICreateTypeInfo)
    _iid_ = IID("{0002040E-0000-0000-C000-000000000046}")

    @virtual_table.com_function(UINT)
    def DeleteFuncDesc(self, index: int) -> int: ...

    @virtual_table.com_function(MEMBERID, INVOKEKIND)
    def DeleteFuncDescByMemId(self, memid: MEMBERID, invKind: INVOKEKIND) -> int: ...

    @virtual_table.com_function(UINT)
    def DeleteVarDesc(self, index: int) -> int: ...

    @virtual_table.com_function(MEMBERID)
    def DeleteVarDescByMemId(self, memid: MEMBERID) -> int: ...

    @virtual_table.com_function(UINT)
    def DeleteImplType(self, index: int) -> int: ...

    @virtual_table.com_function(LPGUID, LPVARIANT, intermediate_method = True)
    def SetCustData(self, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(guid.ref(), pVarVal)

    @virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
    def SetFuncCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(index, guid.ref(), pVarVal)

    @virtual_table.com_function(UINT, UINT, LPGUID, LPVARIANT, intermediate_method = True)
    def SetParamCustData(self, indexFunc: int, indexParam: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(indexFunc, indexParam, guid.ref(), pVarVal)

    @virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
    def SetVarCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(index, guid.ref(), pVarVal)

    @virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
    def SetImplTypeCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(index, guid.ref(), pVarVal)

    @virtual_table.com_function(ULONG)
    def SetHelpStringContext(self, dwHelpStringContext: int) -> int: ...

    @virtual_table.com_function(UINT, ULONG)
    def SetFuncHelpStringContext(self, index: int, dwHelpStringContext: int) -> int: ...

    @virtual_table.com_function(UINT, ULONG)
    def SetVarHelpStringContext(self, index: int, dwHelpStringContext: int) -> int: ...

    @virtual_table.com_function()
    def Invalidate(self) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetName(self, szName: LPOLESTR) -> int: ...

    virtual_table.build()

LPCREATETYPEINFO2 = ICreateTypeInfo2.PTR()

class ICreateTypeLib(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00020406-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPOLESTR, TYPEKIND, DOUBLE_PTR(ICreateTypeInfo))
    def CreateTypeInfo(self, szName: LPOLESTR, tkind: TYPEKIND, ppCTInfo: IDoublePtr[ICreateTypeInfo]) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetName(self, szName: LPOLESTR) -> int: ...

    @virtual_table.com_function(WORD, WORD)
    def SetVersion(self, wMajorVerNum: int, wMinorVerNum: int) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetDocString(self, szDoc: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPGUID, intermediate_method = True)
    def SetGuid(self, guid: GUID, **kwargs) -> int:
        return self.virt_delegate(guid.ref())

    @virtual_table.com_function(LPOLESTR)
    def SetDocString(self, szDoc: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetHelpFileName(self, szHelpFileName: LPOLESTR) -> int: ...

    @virtual_table.com_function(DWORD)
    def SetHelpContext(self, dwHelpContext: int) -> int: ...

    @virtual_table.com_function(LCID)
    def SetLcid(self, lcid: LCID) -> int: ...

    @virtual_table.com_function(UINT)
    def SetLibFlags(self, uLibFlags: int) -> int: ...

    @virtual_table.com_function()
    def SaveAllChanges(self) -> int: ...

    virtual_table.build()

LPCREATETYPELIB = ICreateTypeLib.PTR()

class ICreateTypeLib2(ICreateTypeLib):
    virtual_table = COMVirtualTable.from_ancestor(ICreateTypeLib)
    _iid_ = IID("{0002040F-0000-0000-C000-000000000046}")

    @virtual_table.com_function(LPOLESTR)
    def DeleteTypeInfo(self, szName: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPGUID, LPVARIANT, intermediate_method = True)
    def SetCustData(self, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
        return self.virt_delegate(guid.ref(), pVarVal)

    @virtual_table.com_function(ULONG)
    def SetHelpStringContext(self, dwHelpStringContext: int) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def SetHelpStringDll(self, szFileName: LPOLESTR) -> int: ...

    virtual_table.build()

LPCREATETYPELIB2 = ICreateTypeLib2.PTR()

#  DISPID reserved to indicate an "unknown" name
# only reserved for data members (properties); reused as a method dispid below
DISPID_UNKNOWN	= ( -1 )

# DISPID reserved for the "value" property
DISPID_VALUE	= ( 0 )

"""
    The following DISPID is reserved to indicate the param
    that is the right-hand-side (or "put" value) of a PropertyPut
"""
DISPID_PROPERTYPUT	= ( -3 )

# DISPID reserved for the standard "NewEnum" method
DISPID_NEWENUM	= ( -4 )

# DISPID reserved for the standard "Evaluate" method
DISPID_EVALUATE	= ( -5 )

DISPID_CONSTRUCTOR	= ( -6 )

DISPID_DESTRUCTOR	= ( -7 )

DISPID_COLLECT	= ( -8 )

DISPATCH_METHOD = 0x1
DISPATCH_PROPERTYGET = 0x2
DISPATCH_PROPERTYPUT = 0x4
DISPATCH_PROPERTYPUTREF = 0x8
    
class IDispatch(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00020400-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(PUINT)
    def GetTypeInfoCount(self) -> int: 
        """
        Retrieves the number of type information interfaces that an object provides (either 0 or 1).
        """
    
    @virtual_table.com_function(UINT, LCID, PVOID)
    def GetTypeInfo(self, iTInfo: int, lcid: int, 
                    ppTInfo: IDoublePtr['ITypeInfo']) -> int: 
        """
        Retrieves the type information for an object, which can then be used to get the type information for an interface.
        """
        
    @virtual_table.com_function(REFIID, POINTER(LPOLESTR), UINT, LCID, POINTER(DISPID),
                                intermediate_method=True)
    def GetIDsOfNames(self, iid: IID, rgszNames: str, cNames: int, lcid: int, rgDispId: IPointer[int], **kwargs) -> int:
        """
        Maps a single member and an optional set of argument names to a corresponding set of integer DISPIDs, which can be used on subsequent calls to Invoke. The dispatch function DispGetIDsOfNames provides a standard implementation of GetIDsOfNames.
        """
        return self.virt_delegate(iid.ref(), rgszNames, cNames, lcid, rgDispId)
    
    @virtual_table.com_function(DISPID, REFIID, LCID, WORD, 
                            PVOID, PVOID,
                            POINTER(EXCEPINFO), PUINT)
    def Invoke(self, dispIdMember: int, riid: IPointer[IID], 
               lcid: int, wFlags: int, pDispParams: IPointer[DISPPARAMS],
               pVarResult: IPointer[VARIANT],
               pExcepInfo: IPointer[EXCEPINFO],
               puArgErr: PUINT) -> int: 
        """
        Provides access to properties and methods exposed by an object. The dispatch function `DispInvoke` provides a standard implementation of **Invoke**.
        """
        
    virtual_table.build()
    
LPDISPATCH = IDispatch.PTR()

class IEnumVARIANT(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00020404-0000-0000-C000-000000000046}')

    @virtual_table.com_function(ULONG, LPVARIANT, PULONG)
    def Next(self, celt: int, rgVar: IPointer[VARIANT], pCeltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppEnum: IDoublePtr['IEnumVARIANT']) -> int: ...

    virtual_table.build()

# }

DESCKIND_NONE	= 0
DESCKIND_FUNCDESC	= ( DESCKIND_NONE + 1 )
DESCKIND_VARDESC	= ( DESCKIND_FUNCDESC + 1 )
DESCKIND_TYPECOMP	= ( DESCKIND_VARDESC + 1 )
DESCKIND_IMPLICITAPPOBJ	= ( DESCKIND_TYPECOMP + 1 )
DESCKIND_MAX	= ( DESCKIND_IMPLICITAPPOBJ + 1 ) 
DESCKIND = INT

class BINDPTR(CUnion):
    _fields_ = [
        ('lpfuncdesc', LPFUNCDESC),
        ('lpvardesc', LPVARDESC),
        ('_lptcomp', PVOID)
    ]
    
    lpfuncdesc: IPointer[FUNCDESC]
    lpvardesc: IPointer[VARDESC]
    
    @property
    def lptcomp(self) -> IPointer['ITypeComp']:
        return i_cast(self._lptcomp, LPTYPECOMP)
    
LPBINDPTR = PTR(BINDPTR)

class ITypeComp(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00020403-0000-0000-C000-000000000046}')
    
    @virtual_table.function(HRESULT, LPOLESTR, 
                        ULONG, WORD, PVOID, 
                        PTR(DESCKIND),
                        PTR(BINDPTR))
    def Bind(self, szName: str, lHashVal: int, 
             wFlags: int, ppTInfo: IPointer['ITypeInfo'],
             pDescKind: IPointer[DESCKIND],
             pBindPtr: IPointer[BINDPTR]) -> int: ...
    
    @virtual_table.function(HRESULT, LPOLESTR, 
                            ULONG, PVOID, PVOID)
    def BindType(self, szName: str, lHashVal: int, 
                 ppTInfo: IDoublePtr['ITypeInfo'],
                 ppTComp: IDoublePtr['ITypeComp']) -> int: ...
    
    virtual_table.build()
    
LPTYPECOMP = ITypeComp.PTR()

class ITypeInfo(IUnknown): 
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00020401-0000-0000-C000-000000000046}')
    
    @virtual_table.function(HRESULT, PTR(LPTYPEATTR))
    def GetTypeAttr(self, ppTypeAttr: IDoublePtr[TYPEATTR]) -> int: ...
    
    @virtual_table.function(HRESULT, PVOID)
    def GetTypeComp(self, ppTComp: IDoublePtr['ITypeComp']) -> int: ...
    
    @virtual_table.function(HRESULT, UINT, PTR(LPFUNCDESC))
    def GetFuncDesc(self, index: int, ppFuncDesc: IDoublePtr[FUNCDESC]) -> int: ...
    
    @virtual_table.function(HRESULT, UINT, PTR(LPVARDESC))
    def GetVarDesc(self, index: int, ppVarDesc: IDoublePtr[VARDESC]) -> int: ...
    
    @virtual_table.function(HRESULT, MEMBERID, PTR(BSTR), UINT, PUINT)
    def GetNames(self, memid: int, rgBstrNames: IPointer[BSTR], 
                 cMaxNames: int, pcNames: PUINT) -> int: ...
    
    @virtual_table.function(HRESULT, UINT, PTR(HREFTYPE))
    def GetRefTypeOfImplType(self, index: int, pRefType: IPointer[HREFTYPE]) -> int: ...
    
    @virtual_table.function(HRESULT, UINT, PINT)
    def GetImplTypeFlags(self, index: int, pImplTypeFlags: PINT) -> int: ...
    
    @virtual_table.function(HRESULT, PTR(LPOLESTR), UINT, PTR(MEMBERID))
    def GetIDsOfNames(self, rgszNames: IPointer[LPOLESTR], 
                      cNames: int, pMemId: IPointer[MEMBERID]) -> int: ...
    
    @virtual_table.function(HRESULT, PVOID, MEMBERID, 
                        WORD, PTR(DISPPARAMS), 
                        LPVARIANT,
                        PTR(EXCEPINFO),
                        PUINT)
    def Invoke(self, pvInstance: PVOID, memid: int, 
               wFlags: int, pDispParams: IPointer[DISPPARAMS],
               pVarResult: IPointer[VARIANT],
               pExcepInfo: IPointer[EXCEPINFO],
               puArgErr: PUINT) -> int: ...
    
    @virtual_table.function(HRESULT, MEMBERID, PTR(BSTR), PTR(BSTR), 
                        PDWORD, PTR(BSTR))
    def GetDocumentation(self, memid: int, pBstrName: IPointer[BSTR],
                         pBstrDocString: IPointer[BSTR],
                         pdwHelpContext: PDWORD,
                         pBstrHelpFile: IPointer[BSTR]) -> int: ...
    
    @virtual_table.function(HRESULT, MEMBERID, INVOKEKIND, 
                        PTR(BSTR), PTR(BSTR), PWORD)
    def GetDllEntry(self, memid: int, invKind: int,
                    pBstrDllName: IPointer[BSTR],
                    pBstrName: IPointer[BSTR],
                    pwOrdinal: PWORD) -> int: ...
    
    @virtual_table.function(HRESULT, HREFTYPE, PVOID)
    def GetRefTypeInfo(self, hRefType: int, ppTInfo: IDoublePtr['ITypeInfo']) -> int: ...
    
    @virtual_table.function(HRESULT, MEMBERID, INVOKEKIND, PVOID)
    def AddressOfMember(self, memid: int, invKind: int, ppv: IPointer[PVOID]) -> int: ...
    
    @virtual_table.function(HRESULT, LPUNKNOWN, REFIID, PVOID)
    def CreateInstance(self, pUnkOuter: IPointer[IUnknown], 
                       riid: IPointer[IID], ppvObj: IPointer[PVOID]) -> int: ...
    
    @virtual_table.function(HRESULT, MEMBERID, PTR(BSTR))
    def GetMops(self, memid: int, pBstrMops: IPointer[BSTR]) -> int: ...
    
    @virtual_table.function(HRESULT, PVOID, PUINT)
    def GetContainingTypeLib(self, ppTLib: IDoublePtr['ITypeLib'], 
                             pIndex: PUINT) -> int: ...
    
    @virtual_table.function(HRESULT, LPTYPEATTR)
    def ReleaseTypeAttr(self, pTypeAttr: IPointer[TYPEATTR]) -> int: ...
    
    @virtual_table.function(HRESULT, LPFUNCDESC)
    def ReleaseFuncDesc(self, pTypeAttr: IPointer[FUNCDESC]) -> int: ...
    
    @virtual_table.function(HRESULT, LPVARDESC)
    def ReleaseVarDesc(self, pTypeAttr: IPointer[VARDESC]) -> int: ...
    
    virtual_table.build()
    
LPTYPEINFO = ITypeInfo.PTR()

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 14:50:05 2026
# Generated from ICL: oaidl1.icl
# {
class ITypeInfo2(ITypeInfo):
	virtual_table = COMVirtualTable.from_ancestor(ITypeInfo)
	_iid_ = IID("{00020412-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PTR(TYPEKIND))
	def GetTypeKind(self, pTypeKind: IPointer[TYPEKIND]) -> int: ...

	@virtual_table.com_function(PULONG)
	def GetTypeFlags(self, pTypeFlags: PULONG) -> int: ...

	@virtual_table.com_function(MEMBERID, INVOKEKIND, PUINT)
	def GetFuncIndexOfMemId(self, memid: MEMBERID, invKind: INVOKEKIND, pFuncIndex: PUINT) -> int: ...

	@virtual_table.com_function(MEMBERID, PUINT)
	def GetVarIndexOfMemId(self, memid: MEMBERID, pVarIndex: PUINT) -> int: ...

	@virtual_table.com_function(LPGUID, LPVARIANT, intermediate_method = True)
	def GetCustData(self, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(guid.ref(), pVarVal)

	@virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
	def GetFuncCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(index, guid.ref(), pVarVal)

	@virtual_table.com_function(UINT, UINT, LPGUID, LPVARIANT, intermediate_method = True)
	def GetParamCustData(self, indexFunc: int, indexParam: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(indexFunc, indexParam, guid.ref(), pVarVal)

	@virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
	def GetVarCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(index, guid.ref(), pVarVal)

	@virtual_table.com_function(UINT, LPGUID, LPVARIANT, intermediate_method = True)
	def GetImplTypeCustData(self, index: int, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(index, guid.ref(), pVarVal)

	@virtual_table.com_function(MEMBERID, LCID, PTR(BSTR), PDWORD, PTR(BSTR))
	def GetDocumentation2(self, memid: MEMBERID, lcid: LCID, pbstrHelpString: IPointer[BSTR], pdwHelpStringContext: PDWORD, pbstrHelpStringDll: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPCUSTDATA)
	def GetAllCustData(self, pCustData: IPointer[CUSTDATA]) -> int: ...

	@virtual_table.com_function(UINT, LPCUSTDATA)
	def GetAllFuncCustData(self, index: int, pCustData: IPointer[CUSTDATA]) -> int: ...

	@virtual_table.com_function(UINT, UINT, LPCUSTDATA)
	def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: IPointer[CUSTDATA]) -> int: ...

	@virtual_table.com_function(UINT, LPCUSTDATA)
	def GetAllVarCustData(self, index: int, pCustData: IPointer[CUSTDATA]) -> int: ...

	@virtual_table.com_function(UINT, LPCUSTDATA)
	def GetAllImplTypeCustData(self, index: int, pCustData: IPointer[CUSTDATA]) -> int: ...

	virtual_table.build()

# }

SYS_WIN16	= 0
SYS_WIN32	= ( SYS_WIN16 + 1 )
SYS_MAC	= ( SYS_WIN32 + 1 )
SYS_WIN64	= ( SYS_MAC + 1 ) 
SYSKIND = INT

LIBFLAG_FRESTRICTED	= 0x1
LIBFLAG_FCONTROL	= 0x2
LIBFLAG_FHIDDEN	= 0x4
LIBFLAG_FHASDISKIMAGE	= 0x8
LIBFLAGS = INT

class TLIBATTR(CStructure):
    _fields_ = [
        ('guid', GUID),
        ('lcid', LCID),
        ('syskind', SYSKIND),
        ('wMajorVerNum', WORD),
        ('wMinorVerNum', WORD),
        ('wLibFlags', WORD)
    ]
    
    wMajorVerNum: int
    wMinorVerNum: int
    wLibFlags: int
    syskind: int
    guid: GUID
    lcid: int

LPTLIBATTR = TLIBATTR.PTR()

class ITypeLib(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    
    @virtual_table.function(HRESULT, UINT, PVOID)
    def GetTypeInfo(self, index: int, ppTInfo: IDoublePtr['ITypeInfo']) -> int: ...
    
    @virtual_table.function(HRESULT, UINT, PTR(TYPEKIND))
    def GetTypeInfoType(self, index: int, pTKind: IPointer[TYPEKIND]) -> int: ...
    
    @virtual_table.function(HRESULT, REFGUID, PVOID, intermediate_method=True)
    def GetTypeInfoOfGuid(self, guid: GUID, ppTinfo: IDoublePtr['ITypeInfo'], **kwargs) -> int: 
        return self.virt_delegate(guid.ref(), ppTinfo)
    
    @virtual_table.function(HRESULT, PTR(LPTLIBATTR))
    def GetLibAttr(self, ppTLibAttr: IDoublePtr[TLIBATTR]) -> int: ...
    
    @virtual_table.function(HRESULT, PVOID)
    def GetTypeComp(self, ppTComp: IDoublePtr['ITypeComp']) -> int: ...
    
    @virtual_table.function(HRESULT, INT, PTR(BSTR), 
                        PTR(BSTR), PDWORD, PTR(BSTR))
    def GetDocumentation(self, index: int, pBstrName: IPointer[BSTR],
                         pBstrDocString: IPointer[BSTR],
                         pdwHelpContext: PDWORD,
                         pBstrHelpFile: IPointer[BSTR]) -> int: ...
    
    @virtual_table.function(HRESULT, LPOLESTR, ULONG, PBOOL)
    def IsName(self, szNameBuf: str, lHashVal: int, pfName: PBOOL) -> int: ...

    @virtual_table.function(HRESULT, LPOLESTR, ULONG, PVOID, PTR(MEMBERID), PUSHORT)
    def FindName(self, szNameBuf: str, lHashVal: int, 
                 ppTInfo: IDoublePtr['ITypeInfo'],
                 rgMemId: IPointer[MEMBERID],
                 pcFound: PUSHORT) -> int: ...

    @virtual_table.function(HRESULT, POINTER(TLIBATTR))
    def ReleaseTLibAttr(self, pTLibAttr: IPointer[TLIBATTR]) -> int: ...
    
    virtual_table.build()

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 15:04:10 2026
# Generated from ICL: oaidl2.icl
# {
class ITypeLib2(ITypeLib):
	virtual_table = COMVirtualTable.from_ancestor(ITypeLib)
	_iid_ = IID("{00020411-0000-0000-C000-000000000046}")

	@virtual_table.com_function(LPGUID, LPVARIANT, intermediate_method = True)
	def GetCustData(self, guid: GUID, pVarVal: IPointer[VARIANT], **kwargs) -> int:
		return self.virt_delegate(guid.ref(), pVarVal)

	@virtual_table.com_function(PULONG, PULONG)
	def GetLibStatistics(self, pcUniqueNames: PULONG, pcchUniqueNames: PULONG) -> int: ...

	@virtual_table.com_function(INT, LCID, PTR(BSTR), PDWORD, PTR(BSTR))
	def GetDocumentation2(self, index: int, lcid: LCID, pbstrHelpString: IPointer[BSTR], pdwHelpStringContext: PDWORD, pbstrHelpStringDll: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(LPCUSTDATA)
	def GetAllCustData(self, pCustData: IPointer[CUSTDATA]) -> int: ...

	virtual_table.build()

LPTYPELIB2 = ITypeLib2.PTR()

# }

CHANGEKIND_ADDMEMBER	= 0
CHANGEKIND_DELETEMEMBER	= ( CHANGEKIND_ADDMEMBER + 1 )
CHANGEKIND_SETNAMES	= ( CHANGEKIND_DELETEMEMBER + 1 )
CHANGEKIND_SETDOCUMENTATION	= ( CHANGEKIND_SETNAMES + 1 )
CHANGEKIND_GENERAL	= ( CHANGEKIND_SETDOCUMENTATION + 1 )
CHANGEKIND_INVALIDATE	= ( CHANGEKIND_GENERAL + 1 )
CHANGEKIND_CHANGEFAILED	= ( CHANGEKIND_INVALIDATE + 1 )
CHANGEKIND_MAX	= ( CHANGEKIND_CHANGEFAILED + 1 ) 
CHANGEKIND = INT

# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 15:26:35 2026
# Generated from ICL: oaidl3.icl
# {
class ITypeChangeEvents(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00020410-0000-0000-C000-000000000046}")

	@virtual_table.com_function(CHANGEKIND, LPTYPEINFO, LPOLESTR, PINT)
	def RequestTypeChange(self, changeKind: CHANGEKIND, pTInfoBefore: IPointer[ITypeInfo], pStrName: LPOLESTR, pfCancel: PINT) -> int: ...

	@virtual_table.com_function(CHANGEKIND, LPTYPEINFO, LPOLESTR)
	def AfterTypeChange(self, changeKind: CHANGEKIND, pTInfoAfter: IPointer[ITypeInfo], pStrName: LPOLESTR) -> int: ...

	virtual_table.build()

LPTYCHANGEEVENTS = ITypeChangeEvents.PTR()

class IErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{1CF2B120-547D-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPGUID)
	def GetGUID(self, pGUID: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetSource(self, pBstrSource: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetDescription(self, pBstrDescription: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetHelpFile(self, pBstrHelpFile: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetHelpContext(self, pdwHelpContext: PDWORD) -> int: ...

	virtual_table.build()

LPERRORINFO = IErrorInfo.PTR()

class ICreateErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{22F03340-547D-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPGUID, intermediate_method = True)
	def SetGUID(self, guid: GUID, **kwargs) -> int:
		return self.virt_delegate(guid.ref())

	@virtual_table.com_function(LPOLESTR)
	def SetSource(self, szSource: LPOLESTR) -> int: ...

	@virtual_table.com_function(LPOLESTR)
	def SetDescription(self, szDescription: LPOLESTR) -> int: ...

	@virtual_table.com_function(LPOLESTR)
	def SetHelpFile(self, szHelpFile: LPOLESTR) -> int: ...

	@virtual_table.com_function(DWORD)
	def SetHelpContext(self, dwHelpContext: int) -> int: ...

	virtual_table.build()

LPCREATEERRORINFO = ICreateErrorInfo.PTR()

class ISupportErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{DF0B3D60-548F-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPIID, intermediate_method = True)
	def InterfaceSupportsErrorInfo(self, iid: IID, **kwargs) -> int:
		return self.virt_delegate(iid.ref())

	virtual_table.build()

LPSUPPORTERRORINFO = ISupportErrorInfo.PTR()

class ITypeFactory(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)

	@virtual_table.com_function(LPTYPEINFO, LPIID, DOUBLE_PTR(IUnknown), intermediate_method = True)
	def CreateFromTypeInfo(self, pTypeInfo: IPointer[ITypeInfo], iid: IID, ppv: IDoublePtr[IUnknown], **kwargs) -> int:
		return self.virt_delegate(pTypeInfo, iid.ref(), ppv)

	virtual_table.build()

class ITypeMarshal(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000002D-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PVOID, DWORD, PVOID, PULONG)
	def Size(self, pvType: PVOID, dwDestContext: int, pvDestContext: PVOID, pSize: PULONG) -> int: ...

	@virtual_table.com_function(PVOID, DWORD, PVOID, ULONG, PBYTE, PULONG)
	def Marshal(self, pvType: PVOID, dwDestContext: int, pvDestContext: PVOID, cbBufferLength: int, pBuffer: PBYTE, pcbWritten: PULONG) -> int: ...

	@virtual_table.com_function(PVOID, DWORD, ULONG, PBYTE, PULONG)
	def Unmarshal(self, pvType: PVOID, dwFlags: int, cbBufferLength: int, pBuffer: PBYTE, pcbRead: PULONG) -> int: ...

	@virtual_table.com_function(PVOID)
	def Free(self, pvType: PVOID) -> int: ...

	virtual_table.build()

class IRecordInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000002F-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PVOID)
	def RecordInit(self, pvNew: PVOID) -> int: ...

	@virtual_table.com_function(PVOID)
	def RecordClear(self, pvExisting: PVOID) -> int: ...

	@virtual_table.com_function(PVOID, PVOID)
	def RecordCopy(self, pvExisting: PVOID, pvNew: PVOID) -> int: ...

	@virtual_table.com_function(LPGUID)
	def GetGuid(self, pguid: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetName(self, pbstrName: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PULONG)
	def GetSize(self, pcbSize: PULONG) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(ITypeInfo))
	def GetTypeInfo(self, ppTypeInfo: IDoublePtr[ITypeInfo]) -> int: ...

	@virtual_table.com_function(PVOID, LPCOLESTR, LPVARIANT)
	def GetField(self, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(PVOID, LPCOLESTR, LPVARIANT, PTR(PVOID))
	def GetFieldNoCopy(self, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT], ppvDataCArray: PVOID) -> int: ...

	@virtual_table.com_function(ULONG, PVOID, LPCOLESTR, LPVARIANT)
	def PutField(self, wFlags: int, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(ULONG, PVOID, LPCOLESTR, LPVARIANT)
	def PutFieldNoCopy(self, wFlags: int, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(PULONG, PTR(BSTR))
	def GetFieldNames(self, pcNames: PULONG, rgBstrNames: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PVOID)
	def IsMatchingType(self, pRecordInfo: IPointer['IRecordInfo']) -> int: ...

	@virtual_table.com_function()
	def RecordCreate(self) -> int: ...

	@virtual_table.com_function(PVOID, PTR(PVOID))
	def RecordCreateCopy(self, pvSource: PVOID, ppvDest: PVOID) -> int: ...

	@virtual_table.com_function(PVOID)
	def RecordDestroy(self, pvRecord: PVOID) -> int: ...

	virtual_table.build()

LPRECORDINFO = IRecordInfo.PTR()

class IErrorLog(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{3127CA40-446E-11CE-8135-00AA004BB851}")

	@virtual_table.com_function(LPCOLESTR, LPEXCEPINFO)
	def AddError(self, pszPropName: LPCOLESTR, pExcepInfo: IPointer[EXCEPINFO]) -> int: ...

	virtual_table.build()

LPERRORLOG = IErrorLog.PTR()

class IPropertyBag(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{55272A00-42CB-11CE-8135-00AA004BB851}")

	@virtual_table.com_function(LPCOLESTR, LPVARIANT, PTR(IErrorLog))
	def Read(self, pszPropName: LPCOLESTR, pVar: IPointer[VARIANT], pErrorLog: IPointer[IErrorLog]) -> int: ...

	@virtual_table.com_function(LPCOLESTR, LPVARIANT)
	def Write(self, pszPropName: LPCOLESTR, pVar: IPointer[VARIANT]) -> int: ...

	virtual_table.build()

LPPROPERTYBAG = IPropertyBag.PTR()

class ITypeLibRegistrationReader(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{ED6A8A2A-B160-4E77-8F73-AA7435CD5C27}")

	@virtual_table.com_function(DOUBLE_PTR(IEnumUnknown))
	def EnumTypeLibRegistrations(self, ppEnumUnknown: IDoublePtr[IEnumUnknown]) -> int: ...

	virtual_table.build()


	@virtual_table.com_function(IUnknown)
	def ITypeLibRegistration(self, ex: IUnknown) -> int: ...

	_iid_ = IID("{76A3E735-02DF-4A12-98EB-043AD3600AF3}")
	@virtual_table.com_function(LPGUID)
	def GetGuid(self, pGuid: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetVersion(self, pVersion: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(LCID))
	def GetLcid(self, pLcid: IPointer[LCID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetWin32Path(self, pWin32Path: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetWin64Path(self, pWin64Path: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetDisplayName(self, pDisplayName: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetFlags(self, pFlags: PDWORD) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetHelpDir(self, pHelpDir: PDWORD) -> int: ...

	virtual_table.build()

# }
