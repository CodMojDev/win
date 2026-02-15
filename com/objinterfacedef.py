#
# objinterfacedef.py
#

from .baseinterfacedef import *

from ..wtypes import *

class IMallocSpy(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000001d-0000-0000-C000-000000000046}')
    
    @virtual_table.function(SIZE_T, SIZE_T)
    def PreAlloc(self, cbRequest: int) -> int: ...
    
    @virtual_table.function(PVOID, PVOID)
    def PostAlloc(self, pActual: PVOID) -> PVOID: ...
    
    @virtual_table.function(PVOID, PVOID, BOOL)
    def PreFree(self, pRequest: PVOID, fSpyed: bool) -> PVOID: ...
    
    @virtual_table.function(VOID, BOOL)
    def PostFree(self, fSpyed: bool): ...
    
    @virtual_table.function(SIZE_T, PVOID, SIZE_T, PVOID, BOOL)
    def PreRealloc(self, pRequest: PVOID, cbRequest: int, 
                   ppNewRequest: IPointer[PVOID], fSpyed: bool) -> int: ...
    
    @virtual_table.function(PVOID, PVOID, BOOL)
    def PostRealloc(PVOID, pActual: PVOID, fSpyed: bool) -> PVOID: ...
    
    @virtual_table.function(PVOID, PVOID, BOOL)
    def PreGetSize(self, pRequest: PVOID, fSpyed: bool) -> PVOID: ...
    
    @virtual_table.function(SIZE_T, SIZE_T, BOOL)
    def PostGetSize(self, cbActual: int, fSpyed: bool) -> int: ...
    
    @virtual_table.function(PVOID, PVOID, BOOL)
    def PreDidAlloc(self, pRequest: PVOID, fSpyed: bool) -> PVOID: ...
    
    @virtual_table.function(INT, PVOID, BOOL, INT)
    def PostDidAlloc(self, pRequest: PVOID, fSpyed: bool, fActual: int) -> int: ...
    
    @virtual_table.function(VOID)
    def PreHeapMinimize(self): ...
    
    @virtual_table.function(VOID)
    def PostHeapMinimize(self): ...
    
    virtual_table.build()
    
LPMALLOCSPY = IMallocSpy.PTR()
    
class BIND_OPTS(CStructure):
    _fields_ = [
        ('cbStruct', DWORD),
        ('grfFlags', DWORD),
        ('grfMode', DWORD),
        ('dwTickCountDeadLine', DWORD)
    ]
    
    dwTickCountDeadLine: int
    cbStruct: int
    grfFlags: int
    grfMode: int

LPBIND_OPTS = BIND_OPTS.PTR()

class BIND_OPTS2(BIND_OPTS):
    _fields_ = [
        ('dwTrackFlags', DWORD),
        ('dwClassContext', DWORD),
        ('locale', LCID),
        ('pServerInfo', COSERVERINFO.PTR())
    ]
    
    pServerInfo: IPointer[COSERVERINFO]
    
    dwClassContext: int
    dwTrackFlags: int
    locale: int

LPBIND_OPTS2 = BIND_OPTS2.PTR()

class BIND_OPTS3(BIND_OPTS2):
    _fields_ = [
        ('hwnd', HWND)
    ]
    
    hwnd: int

LPBIND_OPTS3 = BIND_OPTS3.PTR()
    
class IEnumMoniker(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000101-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ULONG, PVOID, PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr['IMoniker'],
             pceltFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumMoniker']) -> int: ...
    
    virtual_table.build()

LPENUMMONIKER = IEnumMoniker.PTR()

class IBindCtx(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000000e-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPUNKNOWN)
    def RegisterObjectBound(self, punk: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(LPUNKNOWN)
    def RevokeObjectBound(self, punk: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function()
    def ReleaseBoundObjects(self) -> int: ...

    @virtual_table.com_function(LPBIND_OPTS)
    def SetBindOptions(self, pbindopts: IPointer[BIND_OPTS]) -> int: ...

    @virtual_table.com_function(LPBIND_OPTS)
    def GetBindOptions(self, pbindopts: IPointer[BIND_OPTS]) -> int: ...

    @virtual_table.com_function(PVOID)
    def GetRunningObjectTable(self, pprot: IPointer['IRunningObjectTable']) -> int: ...

    @virtual_table.com_function(LPOLESTR, LPUNKNOWN)
    def RegisterObjectParam(self, pszKey: LPOLESTR, punk: IPointer[IUnknown]) -> int: ...

    @virtual_table.com_function(LPOLESTR, POINTER(LPUNKNOWN))
    def GetObjectParam(self, pszKey: LPOLESTR, ppunk: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(POINTER(LPENUMSTRING))
    def EnumObjectParam(self, ppenum: IDoublePtr[IEnumString]) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def RevokeObjectParam(self, pszKey: LPOLESTR) -> int: ...

    virtual_table.build()

LPBINDCTX = LPBC = IBindCtx.PTR()

class IRunnableObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000126-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPCLSID)
    def GetRunningClass(self, lpClsid: LPCLSID) -> int: ...

    @virtual_table.com_function(POINTER(IBindCtx))
    def Run(self, pbc: IPointer[IBindCtx]) -> int: ...

    @virtual_table.function(BOOL, result_function = bool)
    def IsRunning() -> bool: ...

    @virtual_table.com_function(BOOL, BOOL)
    def LockRunning(self, fLock: bool, fLastUnlockCloses: bool) -> int: ...

    @virtual_table.com_function(BOOL)
    def SetContainedObject(self, fContained: bool) -> int: ...

    virtual_table.build()

LPRUNNABLEOBJECT = IRunnableObject.PTR()

class IRunningObjectTable(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000010-0000-0000-C000-000000000046}')

    @virtual_table.com_function(DWORD, LPUNKNOWN, PVOID, PDWORD)
    def Register(self, grfFlags: int, punkObject: IPointer[IUnknown], pmkObjectName: IPointer['IMoniker'], pdwRegister: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD)
    def Revoke(self, dwRegister: int) -> int: ...

    @virtual_table.com_function(PVOID)
    def IsRunning(self, pmkObjectName: IPointer['IMoniker']) -> int: ...

    @virtual_table.com_function(PVOID, POINTER(LPUNKNOWN))
    def GetObject(self, pmkObjectName: IPointer['IMoniker'], ppunkObject: IDoublePtr[IUnknown]) -> int: ...

    @virtual_table.com_function(DWORD, POINTER(FILETIME))
    def NoteChangeTime(self, dwRegister: int, pfiletime: IPointer[FILETIME]) -> int: ... 

    @virtual_table.com_function(PVOID, POINTER(FILETIME))
    def GetTimeOfLastChange(self, pmkObjectName: IPointer['IMoniker'], pfiletime: IPointer[FILETIME]) -> int: ...

    @virtual_table.com_function(PVOID)
    def EnumRunning(self, ppenumMoniker: IDoublePtr['IEnumMoniker']) -> int: ...

    virtual_table.build()

LPRUNNINGOBJECTTABLE = IRunningObjectTable.PTR()

class IPersist(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000010c-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPCLSID)
    def GetClassID(self, pClassID: IPointer[CLSID]) -> int: ...

    virtual_table.build()

LPPERSIST = IPersist.PTR()

class IPersistStream(IPersist):
    virtual_table = COMVirtualTable.from_ancestor(IPersist)
    _iid_ = IID('{00000109-0000-0000-C000-000000000046}')

    @virtual_table.com_function()
    def IsDirty(self) -> int: ...

    @virtual_table.com_function(LPSTREAM)
    def Load(self, pStm: IPointer[IStream]) -> int: ...

    @virtual_table.com_function(LPSTREAM, BOOL)
    def Save(self, pStm: IPointer[IStream], fClearDirty: bool) -> int: ...

    @virtual_table.com_function(POINTER(ULARGE_INTEGER))
    def GetSizeMax(self, pcbSize: IPointer[ULARGE_INTEGER]) -> int: ...

    virtual_table.build()

LPPERSISTSTREAM = IPersistStream.PTR()

MKSYS_NONE    = 0
MKSYS_GENERICCOMPOSITE    = 1
MKSYS_FILEMONIKER    = 2
MKSYS_ANTIMONIKER    = 3
MKSYS_ITEMMONIKER    = 4
MKSYS_POINTERMONIKER    = 5
MKSYS_CLASSMONIKER    = 7
MKSYS_OBJREFMONIKER    = 8
MKSYS_SESSIONMONIKER    = 9
MKSYS_LUAMONIKER    = 10
MKSYS = INT

MKRREDUCE_ONE    = ( 3 << 16 )
MKRREDUCE_TOUSER    = ( 2 << 16 )
MKRREDUCE_THROUGHUSER    = ( 1 << 16 )
MKRREDUCE_ALL    = 0
MKREDUCE = INT

class IMoniker(IPersistStream):
    virtual_table = COMVirtualTable.from_ancestor(IPersistStream)
    _iid_ = IID('{0000000f-0000-0000-C000-000000000046}')

    @virtual_table.com_function(POINTER(IBindCtx), PVOID, LPIID, POINTER(PVOID), intermediate_method = True)
    def BindToObject(self, pbc: IPointer[IBindCtx], pmkToLeft: IPointer['IMoniker'], iidResult: IID, ppvResult: PVOID, **kwargs) -> int:
        return self.virt_delegate(pbc, pmkToLeft, iidResult, ppvResult)

    @virtual_table.com_function(POINTER(IBindCtx), PVOID, LPIID, POINTER(PVOID), intermediate_method = True)
    def BindToStorage(self, pbc: IPointer[IBindCtx], pmkToLeft: IPointer['IMoniker'], iid: IID, ppvObj: PVOID, **kwargs) -> int:
        return self.virt_delegate(pbc, pmkToLeft, iid, ppvObj)

    @virtual_table.com_function(POINTER(IBindCtx), DWORD, PVOID, PVOID)
    def Reduce(self, pbc: IPointer[IBindCtx], dwReduceHowFar: int, ppmkToLeft: IDoublePtr['IMoniker'], ppmkReduced: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(PVOID, BOOL, PVOID)
    def ComposeWith(self, pmkRight: IPointer['IMoniker'], fOnlyIfNotGeneric: bool, ppmkComposite: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(BOOL, PVOID)
    def Enum(self, fForward: bool, ppenumMoniker: IDoublePtr['IEnumMoniker']) -> int: ...

    @virtual_table.com_function(PVOID)
    def IsEqual(self, pmkOtherMoniker: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(PDWORD)
    def Hash(self, pdwHash: PDWORD) -> int: ...

    @virtual_table.com_function(POINTER(IBindCtx), PVOID, PVOID)
    def IsRunning(self, pbc: IPointer[IBindCtx], pmkToLeft: IPointer['IMoniker'], pmkNewlyRunning: IPointer['IMoniker']) -> int: ...

    @virtual_table.com_function(PVOID)
    def Inverse(self, ppmk: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(PVOID, PVOID)
    def CommonPrefixWith(self, pmkOther: IPointer['IMoniker'], ppmkPrefix: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(PVOID, PVOID)
    def RelativePathTo(self, pmkOther: IPointer['IMoniker'], ppmkRelPath: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(POINTER(IBindCtx), PVOID, POINTER(LPOLESTR))
    def GetDisplayName(self, pbc: IPointer[IBindCtx], pmkToLeft: IPointer['IMoniker'], ppszDisplayName: IPointer[LPOLESTR]) -> int: ...

    @virtual_table.com_function(POINTER(IBindCtx), PVOID, LPOLESTR, PULONG, PVOID)
    def ParseDisplayName(self, pbc: IPointer[IBindCtx], pmkToLeft: IPointer['IMoniker'], pszDisplayName: LPOLESTR, pchEaten: PULONG, ppmkOut: IDoublePtr['IMoniker']) -> int: ...

    @virtual_table.com_function(PDWORD)
    def IsSystemMoniker(self, pdwMksys: PDWORD) -> int: ...

    virtual_table.build()

LPMONIKER = IMoniker.PTR()

class IROTData(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{f29f6bc0-5021-11ce-aa15-00006901293f}')

    @virtual_table.com_function(PBYTE, ULONG, PULONG)
    def GetComparisonData(self, pbData: PBYTE, cbMax: int, pcbData: PULONG) -> int: ...

    virtual_table.build()

class IEnumSTATSTG(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000000d-0000-0000-C000-000000000046}')

    @virtual_table.com_function(ULONG, POINTER(STATSTG), PULONG)
    def Next(self, celt: int, rgelt: IPointer[STATSTG], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumSTATSTG']) -> int: ...

    virtual_table.build()

LPENUMSTATSTG = IEnumSTATSTG.PTR()

class RemSNB(CStructure):
    _fields_ = [
        ('ulCntStr', ULONG),
        ('ulCntChar', ULONG)
    ]
    
    rgString: LPOLESTR
    ulCntChar: int
    ulCntStr: int

array_after_structure(RemSNB, 'rgString', OLECHAR)

SNB = PTR(LPOLESTR)
wireSNB = RemSNB.PTR()

class IStorage(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000000b-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPOLESTR, DWORD, DWORD, DWORD, POINTER(LPSTREAM))
    def CreateStream(self, pwcsName: LPOLESTR, grfMode: int, reserved1: int, reserved2: int, ppstm: IDoublePtr[IStream]) -> int: ...

    @virtual_table.com_function(LPOLESTR, PVOID, DWORD, DWORD, POINTER(LPSTREAM))
    def OpenStream(self, pwcsName: LPOLESTR, reserved1: PVOID, grfMode: int, reserved2: int, ppstm: IDoublePtr[IStream]) -> int: ...

    @virtual_table.com_function(LPOLESTR, DWORD, DWORD, DWORD, PVOID)
    def CreateStorage(self, pwcsName: LPOLESTR, grfMode: int, reserved1: int, reserved2: int, ppstg: IDoublePtr['IStorage']) -> int: ...

    @virtual_table.com_function(LPOLESTR, PVOID, DWORD, SNB, DWORD, PVOID)
    def OpenStorage(self, pwcsName: LPOLESTR, pstgPriority: IPointer['IStorage'], grfMode: int, snbExclude: SNB, reserved: int, ppstg: IDoublePtr['IStorage']) -> int: ... # pyright: ignore[reportInvalidTypeForm]

    @virtual_table.com_function(DWORD, LPIID, SNB, PVOID)
    def CopyTo(self, ciidExclude: int, rgiidExclude: IPointer[IID], snbExclude: SNB, pstgDest: IPointer['IStorage']) -> int: ... # pyright: ignore[reportInvalidTypeForm]

    @virtual_table.com_function(LPOLESTR, PVOID, LPOLESTR, DWORD)
    def MoveElementTo(self, pwcsName: LPOLESTR, pstgDest: IPointer['IStorage'], pwcsNewName: LPOLESTR, grfFlags: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def Commit(self, grfCommitFlags: int) -> int: ...

    @virtual_table.com_function()
    def Revert(self) -> int: ...

    @virtual_table.com_function(DWORD, PVOID, DWORD, POINTER(POINTER(IEnumSTATSTG)))
    def EnumElements(self, reserved1: int, reserved2: PVOID, reserved3: int, ppenum: IDoublePtr[IEnumSTATSTG]) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def DestroyElement(self, pwcsName: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPOLESTR, LPOLESTR)
    def RenameElement(self, pwcsOldName: LPOLESTR, pwcsNewName: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPOLESTR, POINTER(FILETIME), POINTER(FILETIME), POINTER(FILETIME))
    def SetElementTimes(self, pwcsName: LPOLESTR, pctime: IPointer['FILETIME'], patime: IPointer[FILETIME], pmtime: IPointer[FILETIME]) -> int: ... # pyright: ignore[reportInvalidTypeForm]

    @virtual_table.com_function(LPCLSID, intermediate_method = True)
    def SetClass(self, clsid: CLSID, **kwargs) -> int:
        return self.virt_delegate(clsid.ref())

    @virtual_table.com_function(DWORD, DWORD)
    def SetStateBits(self, grfStateBits: int, grfMask: int) -> int: ...

    @virtual_table.com_function(POINTER(STATSTG), DWORD)
    def Stat(self, pstatstg: IPointer[STATSTG], grfStatFlag: int) -> int: ...

    virtual_table.build()

LPSTORAGE = IStorage.PTR()

class IPersistFile(IPersist):
    virtual_table = COMVirtualTable.from_ancestor(IPersist)
    _iid_ = IID('{0000010b-0000-0000-C000-000000000046}')

    @virtual_table.com_function()
    def IsDirty(self) -> int: ...

    @virtual_table.com_function(LPCOLESTR, DWORD)
    def Load(self, pszFileName: LPCOLESTR, dwMode: int) -> int: ...

    @virtual_table.com_function(LPCOLESTR, BOOL)
    def Save(self, pszFileName: LPCOLESTR, fRemember: bool) -> int: ...

    @virtual_table.com_function(LPCOLESTR)
    def SaveCompleted(self, pszFileName: LPCOLESTR) -> int: ...

    @virtual_table.com_function(POINTER(LPOLESTR))
    def GetCurFile(self, ppszFileName: IPointer[LPOLESTR]) -> int: ...

    virtual_table.build()

LPPERSISTFILE = IPersistFile.PTR()

class IPersistStorage(IPersist):
    virtual_table = COMVirtualTable.from_ancestor(IPersist)
    _iid_ = IID('{0000010a-0000-0000-C000-000000000046}')

    @virtual_table.com_function()
    def IsDirty(self) -> int: ...

    @virtual_table.com_function(POINTER(IStorage))
    def InitNew(self, pStg: IPointer[IStorage]) -> int: ...

    @virtual_table.com_function(POINTER(IStorage))
    def Load(self, pStg: IPointer[IStorage]) -> int: ...

    @virtual_table.com_function(POINTER(IStorage), BOOL)
    def Save(self, pStgSave: IPointer[IStorage], fSameAsLoad: bool) -> int: ...

    @virtual_table.com_function(POINTER(IStorage))
    def SaveCompleted(self, pStgNew: IPointer[IStorage]) -> int: ...

    @virtual_table.com_function()
    def HandsOffStorage(self) -> int: ...

    virtual_table.build()

LPPERSISTSTORAGE = IPersistStorage.PTR()

class ILockBytes(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000000a-0000-0000-C000-000000000046}')

    @virtual_table.com_function(ULARGE_INTEGER, PVOID, ULONG, PULONG)
    def ReadAt(self, ulOffset: ULARGE_INTEGER, pv: PVOID, cb: int, pcbRead: PULONG) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER, LPCVOID, ULONG, PULONG)
    def WriteAt(self, ulOffset: ULARGE_INTEGER, pv: LPCVOID, cb: int, pcbWritten: PULONG) -> int: ...

    @virtual_table.com_function()
    def Flush(self) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER)
    def SetSize(self, cb: ULARGE_INTEGER) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER, ULARGE_INTEGER, DWORD)
    def LockRegion(self, libOffset: ULARGE_INTEGER, cb: ULARGE_INTEGER, dwLockType: int) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER, ULARGE_INTEGER, DWORD)
    def UnlockRegion(self, libOffset: ULARGE_INTEGER, cb: ULARGE_INTEGER, dwLockType: int) -> int: ...

    @virtual_table.com_function(POINTER(STATSTG), DWORD)
    def Stat(self, pstatstg: IPointer[STATSTG], grfStatFlag: int) -> int: ...

    virtual_table.build()
    
LPLOCKBYTES = ILockBytes.PTR()

class DVTARGETDEVICE(CStructure):
    _fields_ = [
        ('tdSize', DWORD),
        ('tdDriverNameOffset', WORD),
        ('tdDeviceNameOffset', WORD),
        ('tdPortNameOffset', WORD),
        ('tdExtDevmodeOffset', WORD),
    ]
    
    tdDriverNameOffset: int
    tdDeviceNameOffset: int
    tdPortNameOffset: int
    tdData: PBYTE
    tdSize: int

array_after_structure(DVTARGETDEVICE, 'tdData', byte)

CLIPFORMAT = WORD

LPCLIPFORMAT = PWORD

class FORMATETC(CStructure):
    _fields_ = [
        ('cfFormat', CLIPFORMAT),
        ('ptd', DVTARGETDEVICE.PTR()),
        ('dwAspect', DWORD),
        ('lindex', LONG),
        ('tymed', DWORD)
    ]
    
    ptd: IPointer[DVTARGETDEVICE]
    dwAspect: int
    cfFormat: int
    lindex: int
    tymed: int

LPFORMATETC = FORMATETC.PTR()

class IEnumFORMATETC(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000000d-0000-0000-C000-000000000046}')

    @virtual_table.com_function(ULONG, LPFORMATETC, PULONG)
    def Next(self, celt: int, rgelt: IPointer[FORMATETC], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumFORMATETC']) -> int: ...

    virtual_table.build()

LPENUMFORMATETC = IEnumFORMATETC.PTR()

class IRootStorage(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000012-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPOLESTR)
    def SwitchToFile(self, pszFile: LPOLESTR) -> int: ...

    virtual_table.build()

LPROOTSTORAGE = IRootStorage.PTR()

ADVF_NODATA    = 1
ADVF_PRIMEFIRST    = 2
ADVF_ONLYONCE    = 4
ADVF_DATAONSTOP    = 64
ADVFCACHE_NOHANDLER    = 8
ADVFCACHE_FORCEBUILTIN    = 16
ADVFCACHE_ONSAVE    = 32
ADVF = INT

class STATDATA(CStructure):
    _fields_ = [
        ('formatetc', FORMATETC),
        ('advf', DWORD),
        ('_pAdvSink', PVOID),
        ('dwConnection', DWORD)
    ]
    
    formatetc: FORMATETC
    dwConnection: int
    advf: int
    
    @property
    def pAdvSink(self) -> IPointer['IAdviseSink']:
        return reinterpret_cast[LPADVISESINK](self._pAdvSink)

LPSTATDATA = STATDATA.PTR()

class IEnumSTATDATA(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000105-0000-0000-C000-000000000046}')

    @virtual_table.com_function(ULONG, LPSTATDATA, PULONG)
    def Next(self, celt: int, rgelt: IPointer[STATDATA], pceltFetched: PULONG) -> int: ...

    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...

    @virtual_table.com_function()
    def Reset(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumSTATDATA']) -> int: ...

    virtual_table.build()

LPENUMSTATDATA = IEnumSTATDATA.PTR()

TYMED_HGLOBAL = 1
TYMED_FILE = 2
TYMED_ISTREAM = 4
TYMED_ISTORAGE = 8
TYMED_GDI = 16
TYMED_MFPICT = 32
TYMED_ENHMF = 64
TYMED_NULL = 0
TYMED = INT

class RemSTGMEDIUM(CStructure):
    _fields_ = [
        ('tymed', DWORD),
        ('dwHandleType', DWORD),
        ('pData', ULONG),
        ('pUnkForRelease', ULONG),
        ('cbData', ULONG)
    ]
    
    pUnkForRelease: int
    dwHandleType: int
    pData: int
    tymed: int
    
    cbData: int
    data: PBYTE
    
array_after_structure(RemSTGMEDIUM, 'data', byte)

HMETAFILEPICT = HANDLE

class uSTGMEDIUM(CStructure):
    class U(CUnion):
        _fields_ = [
            ('hBitmap', HBITMAP),
            ('hMetaFilePict', HMETAFILEPICT),
            ('hEnhMetaFile', HENHMETAFILE),
            ('hGlobal', HGLOBAL),
            ('lpszFileName', LPOLESTR),
            ('pstm', LPSTREAM),
            ('pstg', LPSTORAGE)
        ]
    _fields_ = [
        ('tymed', DWORD),
        ('u', U),
        ('pUnkForRelease', LPUNKNOWN)
    ]
    _anonymous_ = ['u']
    
    pUnkForRelease: IPointer[IUnknown]
    tymed: int
    
    hMetaFilePict: int
    hEnhMetaFile: int
    hBitmap: int
    hGlobal: int
    
    pstg: IPointer[IStorage]
    pstm: IPointer[IStream]
    lpszFileName: LPOLESTR

#
#  wireSTGMEDIUM
#
# These flags are #defined (not enumerated) in wingdi.
# We need to repeat #defines to avoid conflict in the generated file.
#

# Object Definitions for EnumObjects()
OBJ_PEN            = 1
OBJ_BRUSH          = 2
OBJ_DC             = 3
OBJ_METADC         = 4
OBJ_PAL            = 5
OBJ_FONT           = 6
OBJ_BITMAP         = 7
OBJ_REGION         = 8
OBJ_METAFILE       = 9
OBJ_MEMDC          = 10
OBJ_EXTPEN         = 11
OBJ_ENHMETADC      = 12
OBJ_ENHMETAFILE    = 13

class GDI_OBJECT(CStructure):
    class U(CUnion):
        _fields_ = [
            ('hBitmap', wireHBITMAP),
            ('hPalette', wireHPALETTE),
            ('hGeneric', wireHGLOBAL)
        ]
    _fields_ = [
        ('ObjectType', DWORD),
        ('u', U)
    ]
    _anonymous_ = ['u']

class userSTGMEDIUM(CStructure):
    class U(CUnion):
        _fields_ = [
            ('hMetaFilePict', wireHMETAFILEPICT),
            ('hHEnhMetaFile', wireHENHMETAFILE),
            ('hGdiHandle', GDI_OBJECT.PTR()),
            ('hGlobal', wireHGLOBAL),
            ('lpszFileName', LPOLESTR),
            ('pstm', UP_BYTE_BLOB),
            ('pstg', UP_BYTE_BLOB)
        ]
        
    _fields_ = [
        ('tymed', DWORD),
        ('u', U),
        ('pUnkForRelease', LPUNKNOWN)
    ]
    _anonymous_ = ['u']
    
    pUnkForRelease: IPointer[IUnknown]
    tymed: int
    
    hMetaFilePict: IPointer[userHMETAFILEPICT]
    hHEnhMetaFile: IPointer[userHENHMETAFILE]
    hGdiHandle: IPointer[GDI_OBJECT]
    hGlobal: IPointer[userHGLOBAL]
    pstm: IPointer[BYTE_BLOB]
    pstg: IPointer[BYTE_BLOB]
    lpszFilename: LPOLESTR

wireSTGMEDIUM = userSTGMEDIUM.PTR()
STGMEDIUM = uSTGMEDIUM

ASYNC_STGMEDIUM = STGMEDIUM
wireASYNC_STGMEDIUM = wireSTGMEDIUM

LPSTGMEDIUM = STGMEDIUM.PTR()

class userFLAG_STGMEDIUM(CStructure):
    _fields_ = [
        ('ContextFlags', LONG),
        ('fPassOwnership', LONG),
        ('Stgmed', userSTGMEDIUM)
    ]
    
    Stgmed: userSTGMEDIUM
    fPassOwnership: int
    ContextFlags: int

wireFLAG_STGMEDIUM = userFLAG_STGMEDIUM.PTR()

class FLAG_STGMEDIUM(CStructure):
    _fields_ = [
        ('ContextFlags', LONG),
        ('fPassOwnership', LONG),
        ('Stgmed', STGMEDIUM)
    ]
    
    fPassOwnership: int
    Stgmed: STGMEDIUM
    ContextFlags: int

class IAdviseSink(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000010f-0000-0000-C000-000000000046}')

    @virtual_table.function(VOID, LPFORMATETC, LPSTGMEDIUM)
    def OnDataChange(self, pFormatetc: IPointer[FORMATETC], pStgmed: IPointer[STGMEDIUM]) -> int: ...

    @virtual_table.function(VOID, DWORD, LONG)
    def OnViewChange(self, dwAspect: int, lindex: int) -> int: ...

    @virtual_table.function(VOID, LPMONIKER)
    def OnRename(self, pmk: IPointer[IMoniker]) -> int: ...

    @virtual_table.function(VOID)
    def OnSave(self): ...

    @virtual_table.function(VOID)
    def OnClose(self): ...

    virtual_table.build()

LPADVISESINK = IAdviseSink.PTR()

class AsyncIAdviseSink(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000150-0000-0000-C000-000000000046}')

    @virtual_table.function(VOID, LPFORMATETC, LPSTGMEDIUM)
    def OnDataChange_Begin(self, pFormatetc: IPointer[FORMATETC], pStgmed: IPointer[STGMEDIUM]): ...
    
    @virtual_table.function(VOID)
    def OnDataChange_Finish(self): ...

    @virtual_table.function(VOID, DWORD, LONG)
    def OnViewChange_Begin(self, dwAspect: int, lindex: int): ...
    
    @virtual_table.function(VOID)
    def OnViewChange_Finish(self): ...

    @virtual_table.function(VOID, LPMONIKER)
    def OnRename_Begin(self, pmk: IPointer[IMoniker]): ...
    
    @virtual_table.function(VOID)
    def OnRename_Finish(self): ...

    @virtual_table.function(VOID)
    def OnSave_Begin(self): ...
    
    @virtual_table.function(VOID)
    def OnSave_Finish(self): ...

    @virtual_table.function(VOID)
    def OnClose_Begin(self): ...
    
    @virtual_table.function(VOID)
    def OnClose_Finish(self): ...

    virtual_table.build()

class IAdviseSink2(IAdviseSink):
    virtual_table = COMVirtualTable.from_ancestor(IAdviseSink)
    _iid_ = IID('{00000125-0000-0000-C000-000000000046}')
    
    @virtual_table.function(VOID, LPMONIKER)
    def OnLinkSrcChange(self, pmk: IPointer[IMoniker]): ...
    
    virtual_table.build()
    
class AsyncIAdviseSink2(AsyncIAdviseSink):
    virtual_table = COMVirtualTable.from_ancestor(IAdviseSink)
    _iid_ = IID('{00000151-0000-0000-C000-000000000046}')
    
    @virtual_table.function(VOID, LPMONIKER)
    def Begin_OnLinkSrcChange(self, pmk: IPointer[IMoniker]): ...
    
    @virtual_table.function(VOID)
    def Finish_OnLinkSrcChange(self): ...
    
    virtual_table.build()
    
DATADIR_GET    = 1
DATADIR_SET    = 2
DATADIR = INT

class IDataObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0000010e-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPFORMATETC, LPSTGMEDIUM)
    def GetData(self, pformatetcIn: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM]) -> int: ...

    @virtual_table.com_function(LPFORMATETC, LPSTGMEDIUM)
    def GetDataHere(self, pformatetc: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM]) -> int: ...

    @virtual_table.com_function(LPFORMATETC)
    def QueryGetData(self, pformatetc: IPointer[FORMATETC]) -> int: ...

    @virtual_table.com_function(LPFORMATETC, LPFORMATETC)
    def GetCanonicalFormatEtc(self, pformatectIn: IPointer[FORMATETC], pformatetcOut: IPointer[FORMATETC]) -> int: ...

    @virtual_table.com_function(LPFORMATETC, LPSTGMEDIUM, BOOL)
    def SetData(self, pformatetc: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM], fRelease: bool) -> int: ...

    @virtual_table.com_function(DWORD, POINTER(LPENUMFORMATETC))
    def EnumFormatEtc(self, dwDirection: int, ppenumFormatEtc: IDoublePtr[IEnumFORMATETC]) -> int: ...

    @virtual_table.com_function(LPFORMATETC, DWORD, LPADVISESINK, PDWORD)
    def DAdvise(self, pformatetc: IPointer[FORMATETC], advf: int, pAdvSink: IPointer[IAdviseSink], pdwConnection: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD)
    def DUnadvise(self, dwConnection: int) -> int: ...

    @virtual_table.com_function(IEnumSTATDATA)
    def EnumDAdvise(self, ppenumAdvise: IDoublePtr[IEnumSTATDATA]) -> int: ...

    virtual_table.build()

LPDATAOBJECT = IDataObject.PTR()

class IDataAdviseHolder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000110-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPDATAOBJECT, LPFORMATETC, DWORD, LPADVISESINK, PDWORD)
    def Advise(self, pDataObject: IPointer[IDataObject], pFetc: IPointer[FORMATETC], advf: int, pAdvise: IPointer[IAdviseSink], pdwConnection: PDWORD) -> int: ...

    @virtual_table.com_function(DWORD)
    def Unadvise(self, dwConnection: int) -> int: ...

    @virtual_table.com_function(LPDATAOBJECT, DWORD, DWORD)
    def EnumAdvise(self, pDataObject: IPointer[IDataObject], dwReserved: int, advf: int) -> int: ...

    virtual_table.build()

LPDATAADVISEHOLDER = IDataAdviseHolder.PTR()

CALLTYPE_TOPLEVEL    = 1,
CALLTYPE_NESTED    = 2,
CALLTYPE_ASYNC    = 3,
CALLTYPE_TOPLEVEL_CALLPENDING    = 4,
CALLTYPE_ASYNC_CALLPENDING    = 5
CALLTYPE = INT

SERVERCALL_ISHANDLED    = 0
SERVERCALL_REJECTED    = 1
SERVERCALL_RETRYLATER    = 2
SERVERCALL = INT

PENDINGTYPE_TOPLEVEL    = 1
PENDINGTYPE_NESTED    = 2
PENDINGTYPE = INT

PENDINGMSG_CANCELCALL    = 0
PENDINGMSG_WAITNOPROCESS    = 1
PENDINGMSG_WAITDEFPROCESS    = 2
PENDINGMSG = INT

class INTERFACEINFO(CStructure):
    _fields_ = [
        ('pUnk', LPUNKNOWN),
        ('iid', IID),
        ('wMethod', WORD)
    ]
    
LPINTERFACEINFO = INTERFACEINFO.PTR()

class IMessageFilter(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000016-0000-0000-C000-000000000046}')

    @virtual_table.function(DWORD, DWORD, HTASK, DWORD, POINTER(INTERFACEINFO))
    def HandleInComingCall(dwCallType: int, htaskCaller: HTASK, dwTickCount: int, lpInterfaceInfo: IPointer[INTERFACEINFO]) -> int: ...

    @virtual_table.function(DWORD, HTASK, DWORD, DWORD)
    def RetryRejectedCall(htaskCallee: HTASK, dwTickCount: int, dwRejectType: int) -> int: ...

    @virtual_table.function(DWORD, HTASK, DWORD, DWORD)
    def MessagePending(htaskCallee: HTASK, dwTickCount: int, dwPendingType: int) -> int: ...

    virtual_table.build()

LPMESSAGEFILTER = IMessageFilter.PTR()

class IClassActivator(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000140-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPCLSID, DWORD, LCID, LPIID, POINTER(PVOID), intermediate_method = True)
    def GetClassObject(self, clsid: CLSID, dwClassContext: int, locale: LCID, iid: IID, ppv: PVOID, **kwargs) -> int:
        return self.virt_delegate(clsid.ref(), dwClassContext, locale, iid.ref(), ppv)

    virtual_table.build()

class IFillLockBytes(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{99caf010-415e-11cf-8814-00aa00b569f5}')

    @virtual_table.com_function(LPCVOID, ULONG, PULONG)
    def FillAppend(self, pv: LPCVOID, cb: int, pcbWritten: PULONG) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER, LPCVOID, ULONG, PULONG)
    def FillAt(self, ulOffset: ULARGE_INTEGER, pv: LPCVOID, cb: int, pcbWritten: PULONG) -> int: ...

    @virtual_table.com_function(ULARGE_INTEGER)
    def SetFillSize(self, ulSize: ULARGE_INTEGER) -> int: ...

    @virtual_table.com_function(BOOL)
    def Terminate(self, bCanceled: bool) -> int: ...

    virtual_table.build()

class IProgressNotify(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{a9d758a0-4617-11cf-95fc-00aa00680db4}')

    @virtual_table.com_function(DWORD, DWORD, BOOL, BOOL)
    def OnProgress(self, dwProgressCurrent: int, dwProgressMaximum: int, fAccurate: bool, fOwner: bool) -> int: ...

    virtual_table.build()

class StorageLayout(CStructure):
    _fields_ = [
        ('LayoutType', DWORD),
        ('pwcsElementName', LPOLESTR),
        ('cOffset', LARGE_INTEGER),
        ('cBytes', LARGE_INTEGER)
    ]

    pwcsElementName: LPOLESTR
    cOffset: LARGE_INTEGER
    cBytse: LARGE_INTEGER
    LayoutType: int

class ILayoutStorage(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0e6d4d90-6738-11cf-9608-00aa00680db4}')

    @virtual_table.com_function(POINTER(StorageLayout), DWORD, DWORD)
    def LayoutScript(self, pStorageLayout: IPointer[StorageLayout], nEntries: int, glfInterleavedFlag: int) -> int: ...

    @virtual_table.com_function()
    def BeginMonitor(self) -> int: ...

    @virtual_table.com_function()
    def EndMonitor(self) -> int: ...

    @virtual_table.com_function(LPOLESTR)
    def ReLayoutDocfile(self, pwcsNewDfName: LPOLESTR) -> int: ...

    @virtual_table.com_function(LPLOCKBYTES)
    def ReLayoutDocfileOnILockBytes(self, pILockBytes: IPointer[ILockBytes]) -> int: ...

    virtual_table.build()

class IBlockingLock(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{30f3d47a-6447-11d1-8e3c-00c04fb9386d}')

    @virtual_table.com_function(DWORD)
    def Lock(self, dwTimeout: int) -> int: ...

    @virtual_table.com_function()
    def Unlock(self) -> int: ...

    virtual_table.build()

class ITimeAndNoticeControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{bc0bf6ae-8878-11d1-83e9-00c04fc2c6d4}')

    @virtual_table.com_function(DWORD, DWORD)
    def SuppressChanges(self, res1: int, res2: int) -> int: ...

    virtual_table.build()

class IOplockStorage(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{8d19c834-8879-11d1-83e9-00c04fc2c6d4}')

    @virtual_table.com_function(LPCWSTR, DWORD, DWORD, DWORD, LPIID, POINTER(PVOID), intermediate_method = True)
    def CreateStorageEx(self, pwcsName: LPCWSTR, grfMode: int, stgfmt: int, grfAttrs: int, iid: IID, ppstgOpen: PVOID, **kwargs) -> int:
        return self.virt_delegate(pwcsName, grfMode, stgfmt, grfAttrs, iid.ref(), ppstgOpen)

    @virtual_table.com_function(LPCWSTR, DWORD, DWORD, DWORD, LPIID, POINTER(PVOID), intermediate_method = True)
    def OpenStorageEx(self, pwcsName: LPCWSTR, grfMode: int, stgfmt: int, grfAttrs: int, iid: IID, ppstgOpen: PVOID, **kwargs) -> int:
        return self.virt_delegate(pwcsName, grfMode, stgfmt, grfAttrs, iid.ref(), ppstgOpen)

    virtual_table.build()

class IDirectWriterLock(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{0e6d4d92-6738-11cf-9608-00aa00680db4}')

    @virtual_table.com_function(DWORD)
    def WaitForWriteAccess(self, dwTimeout: int) -> int: ...

    @virtual_table.com_function()
    def ReleaseWriteAccess(self) -> int: ...

    @virtual_table.com_function()
    def HaveWriteAccess(self) -> int: ...

    virtual_table.build()

class IUrlMon(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000026-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPCLSID, LPCWSTR, LPCWSTR, DWORD, DWORD, LPCWSTR, LPBINDCTX, DWORD, LPIID, DWORD, intermediate_method = True)
    def AsyncGetClassBits(self, clsid: CLSID, pszType: LPCWSTR, pszExt: LPCWSTR, dwFileVersionMS: int, dwFileVersionLS: int, pszCodeBase: LPCWSTR, pbc: IPointer[IBindCtx], dwClassContext: int, iid: IID, flags: int, **kwargs) -> int:
        return self.virt_delegate(clsid.ref(), pszType, pszExt, dwFileVersionMS, dwFileVersionLS, pszCodeBase, pbc, dwClassContext, iid.ref(), flags)

    virtual_table.build()

class IForegroundTransfer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000145-0000-0000-C000-000000000046}')

    @virtual_table.com_function(PVOID)
    def AllowForegroundTransfer(self, lpvReserved: PVOID) -> int: ...

    virtual_table.build()

class IThumbnailExtractor(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{969dc708-5c76-11d1-8d86-0000f804b057}')

    @virtual_table.com_function(LPSTORAGE, ULONG, ULONG, PULONG, PULONG, POINTER(HBITMAP))
    def ExtractThumbnail(self, pStg: IPointer[IStorage], ulLength: int, ulHeight: int, pulOutputLength: PULONG, pulOutputHeight: PULONG, phOutputBitmap: IPointer[HBITMAP]) -> int: ...

    @virtual_table.com_function(LPSTORAGE)
    def OnFileUpdated(self, pStg: IPointer[IStorage]) -> int: ...

    virtual_table.build()

class IDummyHICONIncluder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{947990de-cc28-11d2-a0f7-00805f858fb1}')

    @virtual_table.com_function(HICON, HDC)
    def Dummy(self, h1: HICON, h2: HDC) -> int: ...

    virtual_table.build()

ServerApplication    = 0
LibraryApplication    = ( ServerApplication + 1 ) 
ApplicationType = INT

IdleShutdown    = 0
ForcedShutdown    = ( IdleShutdown + 1 ) 
ShutdownType = INT

class IProcessLock(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{000001d5-0000-0000-C000-000000000046}')

    @virtual_table.function(ULONG)
    def AddRefOnProcess() -> int: ...

    @virtual_table.function(ULONG)
    def ReleaseRefOnProcess() -> int: ...

    virtual_table.build()

class ISurrogateService(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{000001d4-0000-0000-C000-000000000046}')

    @virtual_table.com_function(LPGUID, POINTER(IProcessLock), PBOOL, intermediate_method = True)
    def Init(self, guidProcessID: GUID, pProcessLock: IPointer[IProcessLock], pfApplicationAware: PBOOL, **kwargs) -> int:
        return self.virt_delegate(guidProcessID.ref(), pProcessLock, pfApplicationAware)

    @virtual_table.com_function(LPGUID, ApplicationType, intermediate_method = True)
    def ApplicationLaunch(self, guidApplID: GUID, appType: ApplicationType, **kwargs) -> int:
        return self.virt_delegate(guidApplID.ref(), appType)

    @virtual_table.com_function(LPGUID, intermediate_method = True)
    def ApplicationFree(self, guidApplID: GUID, **kwargs) -> int:
        return self.virt_delegate(guidApplID.ref())

    @virtual_table.com_function(ULONG)
    def CatalogRefresh(self, ulReserved: int) -> int: ...

    @virtual_table.com_function(ULONG)
    def ProcessShutdown(self, ulReserved: int) -> int: ...

    virtual_table.build()

class IInitializeSpy(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{00000034-0000-0000-C000-000000000046}')

    @virtual_table.com_function(DWORD, DWORD)
    def PreInitialize(self, dwCoInit: int, dwCurThreadAptRefs: int) -> int: ...

    @virtual_table.com_function(HRESULT, DWORD, DWORD)
    def PostInitialize(self, hrCoInit: int, dwCoInit: int, dwNewThreadAptRefs: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def PreUninitialize(self, dwCurThreadAptRefs: int) -> int: ...

    @virtual_table.com_function(DWORD)
    def PostUninitialize(self, dwNewThreadAptRefs: int) -> int: ...

    virtual_table.build()

LPINITIALIZESPY = IInitializeSpy.PTR()

class IApartmentShutdown(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{A2F05A09-27A2-42B5-BC0E-AC163EF49D9B}')

    @virtual_table.com_function(UINT64)
    def OnUninitialize(self, ui64ApartmentIdentifier: int) -> int: ...

    virtual_table.build()