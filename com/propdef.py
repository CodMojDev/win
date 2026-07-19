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

class PROPSPEC(CStructure):
    class _U(CUnion):
        _fields_ = [
            ('propid', PROPID),
            ('lpwstr', LPOLESTR)
        ]
    _fields_ = [
        ('ulKind', ULONG),
        ('_u', _U)
    ]
    _anonymous_ = ['_u']
    propid: int
    lpwstr: LPOLESTR
    ulKind: int

class STATPROPSTG(CStructure):
    _fields_ = [
        ('lpwstrName', LPOLESTR),
        ('propid', PROPID),
        ('vt', VARTYPE)
    ]
    lpwstrName: LPOLESTR
    propid: int
    vt: int
    
class STATPROPSETSTG(CStructure):
    _fields_ = [
        ('fmtid', GUID),
        ('clsid', CLSID),
        ('grfFlags', DWORD),
        ('mtime', FILETIME),
        ('ctime', FILETIME),
        ('atime', FILETIME),
        ('dwOsVersion', DWORD)
    ]
    fmtid: GUID
    clsid: CLSID
    grfFlags: int
    mtime: FILETIME
    ctime: FILETIME
    atime: FILETIME
    dwOsVersion: int
    
class IInitializeWithFile(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{b7d14566-0509-4cce-a71f-0a554233bd9b}')
    
    @virtual_table.com_function(LPCWSTR, DWORD)
    def Initialize(self, pszFilePath: WT_LPWSTR, grfMode: int) -> int: ...
    
    virtual_table.build()
    
class IInitializeWithStream(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{b824b49d-22ac-4161-ac8a-9916e8fa3f7f}')
    
    @virtual_table.com_function(LPSTREAM, DWORD)
    def Initialize(self, pstream: IPointer[IStream], grfMode: int) -> int: ...
    
    virtual_table.build()
    
class IPropertyStore(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{886d8eeb-8cf2-4446-8d02-cdba1dbdcf99}')
    
    @virtual_table.com_function(PDWORD)
    def GetCount(self, cProps: IPointer[DWORD]) -> int: ...
    
    @virtual_table.com_function(DWORD, LPPROPERTYKEY)
    def GetAt(self, iProp: int, pkey: IPointer[PROPERTYKEY]) -> int: ...
    
    @virtual_table.com_function(REFPROPERTYKEY, LPPROPVARIANT, intermediate_method=True, marshal_scheme=[(0, RetVal_Dereference)])
    def GetValue(self, key: PROPERTYKEY, pv: IPointer[PROPVARIANT], **kwargs) -> int:
        return self.virt_delegate(key.ref(), pv)
    
    @virtual_table.com_function(REFPROPERTYKEY, REFPROPVARIANT, intermediate_method=True, marshal_scheme=[(0, RetVal_Dereference), (1, RetVal_Dereference)])
    def SetValue(self, key: PROPERTYKEY, propvar: PROPVARIANT, **kwargs) -> int:
        return self.virt_delegate(key.ref(), propvar.ref())
    
    virtual_table.build()
    
LPPROPERTYSTORE = PTR(IPropertyStore)

class INamedPropertyStore(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{71604b0f-97b0-4764-8577-2f13e98a1422}')
    
    @virtual_table.com_function(LPCWSTR, REFPROPERTYKEY, LPPROPVARIANT, intermediate_method=True, marshal_scheme=[(1, RetVal_Dereference)])
    def GetNamedValue(self, pszName: WT_LPWSTR, key: PROPERTYKEY, ppropvar: IPointer[PROPVARIANT], **kwargs) -> int:
        return self.virt_delegate(pszName, key.ref(), ppropvar)
    
    @virtual_table.com_function(LPCWSTR, REFPROPERTYKEY, REFPROPVARIANT, intermediate_method=True, marshal_scheme=[(1, RetVal_Dereference), (2, RetVal_Dereference)])
    def SetNamedValue(self, pszName: WT_LPWSTR, key: PROPERTYKEY, propvar: PROPVARIANT, **kwargs) -> int:
        return self.virt_delegate(pszName, key.ref(), propvar.ref())
    
    @virtual_table.com_function(PDWORD)
    def GetNameCount(self, pdwCount: IPointer[DWORD]) -> int: ...
    
    @virtual_table.com_function(DWORD, LPBSTR)
    def GetNameAt(self, iProp: int, pbstrName: IPointer[BSTR]) -> int: ...
    
    virtual_table.build()
    
class IObjectWithPropertyKey(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{fc0ca0a7-c316-4fd2-9031-3e628e6d4f23}')
    
    @virtual_table.com_function(REFPROPERTYKEY, intermediate_method=True, marshal_scheme=[(0, RetVal_Dereference)])
    def SetPropertyKey(self, key: PROPERTYKEY, **kwargs) -> int:
        return self.virt_delegate(key.ref())
    
    @virtual_table.com_function(LPPROPERTYKEY)
    def GetPropertyKey(self, pkey: IPointer[PROPERTYKEY]) -> int: ...
    
    virtual_table.build()
    
class IPropertyChange(IObjectWithPropertyKey):
    virtual_table = COMVirtualTable.from_ancestor(IObjectWithPropertyKey)
    _iid_ = IID('{f917bc8a-1bba-4478-a245-1bde03eb9431}')
    
    @virtual_table.com_function(REFPROPVARIANT, LPPROPVARIANT, intermediate_method=True, marshal_scheme=[(0, RetVal_Dereference)])
    def ApplyToPropVariant(self, propvarIn: PROPVARIANT, ppropvarOut: IPointer[PROPVARIANT]) -> int: ...
    
    virtual_table.build()
    
class IPropertyChangeArray(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{380f5cad-1b5e-42f2-805d-637fd392d31e}')
    
    @virtual_table.com_function(PUINT)
    def GetCount(self, pcOperations: IPointer[UINT]) -> int: ...
    
    @virtual_table.com_function(UINT, REFIID, PVOID, intermediate_method=True, marshal_scheme=[(1, RetVal_Dereference)])
    def GetAt(self, iIndex: int, riid: IID, ppv: IDoublePtr) -> int:
        return self.virt_delegate(iIndex, riid.ref(), ppv)
    
    @virtual_table.com_function(UINT, IPropertyChange.PTR())
    def InsertAt(self, iIndex: int, ppropChange: IPointer[IPropertyChange]) -> int: ...
    
    @virtual_table.com_function(IPropertyChange.PTR())
    def Append(self, ppropChange: IPointer[IPropertyChange]) -> int: ...
    
    @virtual_table.com_function(IPropertyChange.PTR())
    def AppendOrReplace(self, ppropChange: IPointer[IPropertyChange]) -> int: ...
    
    @virtual_table.com_function(UINT)
    def RemoveAt(self, iIndex: int): ...
    
    @virtual_table.com_function(REFPROPERTYKEY, marshal_scheme=[(0, RetVal_Dereference)], intermediate_method=True)
    def IsKeyInArray(self, key: PROPERTYKEY, **kwargs) -> int:
        return self.virt_delegate(key.ref())
    
    virtual_table.build()