from .autointerfacedef import *

class VERSIONEDSTREAM(CStructure):
    _fields_ = [
        ('guidVersion', GUID),
        ('pStream', LPSTREAM)
    ]
    guidVersion: GUID
    pStream: IPointer[IStream]

LPVERSIONEDSTREAM = PTR(VERSIONEDSTREAM)

class CLIPDATA(CStructure):
    _fields_ = [
        ('cbSize', ULONG),
        ('ulClipFmt', LONG),
        ('pClipData', PBYTE)
    ]
    cbSize: int
    ulClipFmt: int
    pClipData: IPointer[BYTE]

LPCLIPDATA = PCLIPDATA = PTR(CLIPDATA)

class PROPVARIANT(CStructure):
    class _U(CUnion):
        _fields_ = [
            ('cVal', byte),
            ('bVal', BYTE),
            ('iVal', SHORT),
            ('uiVal', USHORT),
            ('iVal', LONG),
            ('uiVal', ULONG),
            ('intVal', INT),
            ('uintVal', UINT),
            ('hVal', LARGE_INTEGER),
            ('uhVal', ULARGE_INTEGER),
            ('fltVal', FLOAT),
            ('dblVal', DOUBLE),
            ('boolVal', VARIANT_BOOL),
            ('scode', SCODE),
            ('cyVal', CY),
            ('date', DATE),
            ('filetime', FILETIME),
            ('puuid', LPCLSID),
            ('pclipdata', LPCLIPDATA),
            ('bstrVal', BSTR),
            ('bstrblobVal', BSTRBLOB),
            ('blob', BLOB),
            ('pszVal', LPSTR),
            ('pwszVal', LPWSTR),
            ('punkVal', LPUNKNOWN),
            ('_pdispVal', LPUNKNOWN),
            ('pStream', LPSTREAM),
            ('pStorage', LPSTORAGE),
            ('pVersionedStream', LPVERSIONEDSTREAM),
            ('parray', LPSAFEARRAY),
            ('pcVal', PTR(byte)),
            ('pbVal', PBYTE),
            ('piVal', PSHORT),
            ('puiVal', PUSHORT),
            ('plVal', PLONG),
            ('pulVal', PULONG),
            ('pintVal', PINT),
            ('puintVal', PUINT),
            ('pfltVal', PFLOAT),
            ('pdblVal', PTR(DOUBLE)),
            ('pboolVal', PTR(VARIANT_BOOL)),
            ('pdecVal', LPDECIMAL),
            ('pscode', PTR(SCODE)),
            ('pcyVal', LPCY),
            ('pdate', PTR(DATE)),
            ('pbstrVal', PTR(BSTR)),
            ('ppunkVal', PTR(LPUNKNOWN)),
            ('_ppdispVal', PVOID),
            ('pparray', PTR(LPSAFEARRAY)),
            ('_pvarVal', PVOID)
        ]
    _fields_ = [
        ('vt', VARTYPE),
        ('wReserved1', WORD),
        ('wReserved2', WORD),
        ('wReserved3', WORD),
        ('_u', _U)
    ]
    _anonymous_ = ['_u']
    vt: int
    wReserved1: int
    wReserved2: int
    wReserved3: int
    cVal: int
    bVal: int
    iVal: int
    uiVal: int
    lVal: int
    ulVal: int
    intVal: int
    uintVal: int
    hVal: int
    uhVal: int
    fltVal: float
    dblVal: float
    boolVal: int
    scode: int
    cyVal: int
    date: float
    filetime: FILETIME
    puuid: IPointer[CLSID]
    pclipdata: IPointer[CLIPDATA]
    bstrVal: BSTR
    bstrblobVal: BSTRBLOB
    blob: BLOB
    pszVal: LPSTR
    pwszVal: LPWSTR
    punkVal: IPointer[IUnknown]
    _pdispVal: int
    @property
    def pdispVal(self) -> IPointer['IDispatch']:
        return i_cast(self._pdispVal, LPDISPATCH)
    @pdispVal.setter
    def pdispVal(self, pdispVal: IPointer['IDispatch']):
        self._pdispVal = pdispVal
    pStream: IPointer[IStream]
    pStorage: IPointer[IStorage]
    pVersionedStream: IPointer[VERSIONEDSTREAM]
    parray: IPointer[SAFEARRAY]
    pcVal: IPointer[byte]
    pbVal: IPointer[BYTE]
    piVal: IPointer[SHORT]
    puiVal: IPointer[USHORT]
    plVal: IPointer[LONG]
    pulVal: IPointer[ULONG]
    pintVal: IPointer[INT]
    puintVal: IPointer[UINT]
    pfltVal: IPointer[FLOAT]
    pdblVal: IPointer[DOUBLE]
    pboolVal: IPointer[VARIANT_BOOL]
    pdecVal: IPointer[DECIMAL]
    pscode: IPointer[SCODE]
    pcyVal: IPointer[CY]
    pdate: IPointer[DATE]
    pbstrVal: IPointer[BSTR]
    ppunkVal: IDoublePtr[IUnknown]
    _ppdispVal: int
    @property
    def ppdispVal(self) -> IDoublePtr['IDispatch']:
        return i_cast(self._ppdispVal, PTR(LPDISPATCH))
    @ppdispVal.setter
    def ppdispVal(self, ppdispVal: IDoublePtr['IDispatch']):
        self._ppdispVal = ppdispVal
    pparray: IDoublePtr[SAFEARRAY]
    _pvarVal: int
    @property
    def pvarVal(self) -> IPointer['PROPVARIANT']:
        return i_cast(self._pvarVal, LPPROPVARIANT)
    @pvarVal.setter
    def pvarVal(self, pvarVal: IPointer['PROPVARIANT']):
        self._pvarVal = pvarVal

LPPROPVARIANT = PPROPVARIANT = REFPROPVARIANT = PTR(PROPVARIANT)

class PROPERTYKEY(CStructure):
    _fields_ = [
        ('fmtid', GUID),
        ('pid', DWORD)
    ]
    fmtid: GUID
    pid: int
    
LPPROPERTYKEY = PPROPERTYKEY = REFPROPERTYKEY = PTR(PROPERTYKEY)