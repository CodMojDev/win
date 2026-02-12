#
# baseinterfacedef.py
#

from .interfacedef import *
from .unknwn import *
    
class ISequentialStream(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'ISequentialStream')
    _iid_ = IID('{0c733a30-2a1c-11ce-ade5-00aa0044773d}')
    
    @virtual_table.com_function(PVOID, ULONG, PULONG)
    def Read(self, pv: PVOID, cb: int, pcbRead: PULONG) -> int: ...
    
    @virtual_table.com_function(LPCVOID, ULONG, PULONG)
    def Write(self, pv: LPCVOID, cb: int, pcbWritten: PULONG) -> int: ...
    
    virtual_table.build()
    
class STATSTG(CStructure):
    _fields_ = [
        ('pwcsName', LPOLESTR),
        ('type', DWORD),
        ('cbSize', ULARGE_INTEGER),
        ('mtime', FILETIME),
        ('ctime', FILETIME),
        ('atime', FILETIME),
        ('grfMode', DWORD),
        ('grfLocksSupported', DWORD),
        ('clsid', CLSID),
        ('grfStateBits', DWORD),
        ('reserved', DWORD)
    ]
    
    pwcsName: str
    type: int
    
    cbSize: ULARGE_INTEGER
    grfLocksSupported: int
    grfMode: int
    clsid: CLSID
    
    grfStateBits: int
    reserved: int
    
STGTY_STORAGE	= 1,
STGTY_STREAM	= 2,
STGTY_LOCKBYTES	= 3,
STGTY_PROPERTY	= 4
STGTY = INT

STREAM_SEEK_SET	= 0
STREAM_SEEK_CUR	= 1
STREAM_SEEK_END	= 2
STREAM_SEEK = INT

LOCK_WRITE	= 1
LOCK_EXCLUSIVE	= 2
LOCK_ONLYONCE	= 4
LOCKTYPE = INT
    
class IStream(ISequentialStream):
    virtual_table = COMVirtualTable.from_ancestor(ISequentialStream.virtual_table, 'IStream')
    _iid_ = IID('{0000000c-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(LARGE_INTEGER, DWORD, PULARGE_INTEGER)
    def Seek(self, dlibMove: LARGE_INTEGER, dwOrigin: int, 
             pLibNewPosition: IPointer[ULARGE_INTEGER]) -> int: ...
    
    @virtual_table.com_function(ULARGE_INTEGER)
    def SetSize(self, libNewSize: ULARGE_INTEGER) -> int: ...
    
    @virtual_table.com_function(PVOID, ULARGE_INTEGER, PULARGE_INTEGER, PULARGE_INTEGER)
    def CopyTo(self, pstm: IPointer['IStream'], cb: int,
               pcbRead: IPointer[ULARGE_INTEGER],
               pcbWritten: IPointer[ULARGE_INTEGER]) -> int: ...
    
    @virtual_table.com_function(DWORD)
    def Commit(self, grfCommitFlags: int) -> int: ...
    
    @virtual_table.com_function()
    def Revert(self) -> int: ...
    
    @virtual_table.com_function(ULARGE_INTEGER, ULARGE_INTEGER, DWORD)
    def LockRegion(self, libOffset: ULARGE_INTEGER, cb: ULARGE_INTEGER, 
                   dwLockType: int) -> int: ...
    
    @virtual_table.com_function(ULARGE_INTEGER, ULARGE_INTEGER, DWORD)
    def UnlockRegion(self, libOffset: ULARGE_INTEGER, cb: ULARGE_INTEGER, 
                   dwLockType: int) -> int: ...
    
    @virtual_table.com_function(STATSTG.PTR(), DWORD)
    def Stat(self, pstatstg: IPointer[STATSTG], grfStatFlag: int) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppstm: IPointer['IStream']) -> int: ...
    
    virtual_table.build()
    
LPSTREAM = IStream.PTR()

class IMarshal(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IMarshal')
    _iid_ = IID('{00000003-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(REFIID, PVOID, DWORD, PVOID, 
                                DWORD, PCLSID, intermediate_method=True)
    def GetUnmarshalClass(self, iid: IID, pv: PVOID, dwDestContext: int,
                          pvDestContext: PVOID, mshlflags: int, 
                          pCid: IPointer[CLSID], **kwargs) -> int: 
        return self.virt_delegate(iid.ref(), pv, dwDestContext,
                                  pvDestContext, mshlflags, pCid)
    
    @virtual_table.com_function(REFIID, PVOID, DWORD, PVOID, 
                                DWORD, PDWORD, intermediate_method=True)
    def GetMarshalSizeMax(self, iid: IID, pv: PVOID, dwDestContext: int,
                          pvDestContext: PVOID, mshlflags: int, 
                          pSize: PDWORD, **kwargs) -> int: 
        return self.virt_delegate(iid.ref(), pv, dwDestContext,
                                  pvDestContext, mshlflags, pSize)
    
    @virtual_table.com_function(LPSTREAM, REFIID, PVOID, DWORD, PVOID, 
                                DWORD, intermediate_method=True)
    def MarshalInterface(self, pStm: IPointer[IStream], iid: IID, 
                         pv: PVOID, dwDestContext: int, pvDestContext: PVOID,
                         mshlflags: int, **kwargs) -> int: 
        return self.virt_delegate(pStm, iid.ref(), pv, dwDestContext,
                                  pvDestContext, mshlflags)
    
    @virtual_table.com_function(LPSTREAM, REFIID, PVOID, intermediate_method=True)
    def UnmarshalInterface(self, pStm: IPointer[IStream], 
                           iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pStm, iid.ref(), ppv)
    
    @virtual_table.com_function(LPSTREAM)
    def ReleaseMarshalData(self, pStm: IPointer[IStream]) -> int: ...
    
    @virtual_table.com_function(DWORD)
    def DisconnectObject(self, dwReserved: int) -> int: ...
    
    virtual_table.build()

LPMARSHAL = IMarshal.PTR()
    
class INoMarshal(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'INoMarshal')
    _iid_ = IID('{ecc8691b-c1db-4dc0-855e-65f6c551af49}')
    
    virtual_table.build()
    
class IAgileObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IAgileObject')
    _iid_ = IID('{94ea2b94-e9cc-49e0-c0ff-ee64ca8f5b90}')
    
    virtual_table.build()
    
ACTIVATIONTYPE_UNCATEGORIZED	= 0
ACTIVATIONTYPE_FROM_MONIKER	= 0x1
ACTIVATIONTYPE_FROM_DATA	= 0x2
ACTIVATIONTYPE_FROM_STORAGE	= 0x4
ACTIVATIONTYPE_FROM_STREAM	= 0x8
ACTIVATIONTYPE_FROM_FILE	= 0x10
ACTIVATIONTYPE = INT

class IActivationFilter(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'INoMarshal')
    _iid_ = IID('{00000017-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(DWORD, REFCLSID, PCLSID, intermediate_method=True)
    def HandleActivation(self, dwActivationType: int, clsid: CLSID,
                         pReplacementClsId: IPointer[CLSID], **kwargs) -> int:
        return self.virt_delegate(dwActivationType, clsid.ref(), pReplacementClsId)
    
    virtual_table.build()
    
class IMarshal2(IMarshal):
    virtual_table = COMVirtualTable.from_ancestor(IMarshal.virtual_table, 'IMarshal2')
    _iid_ = IID('{000001cf-0000-0000-C000-000000000046}')
    
    virtual_table.build()
    
LPMARSHAL2 = IMarshal2.PTR()
    
class IMalloc(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IMalloc')
    _iid_ = IID('{00000002-0000-0000-C000-000000000046}')
    
    @virtual_table.function(PVOID, SIZE_T)
    def Alloc(self, cb: int) -> PVOID: ...
    
    @virtual_table.function(PVOID, PVOID, SIZE_T)
    def Realloc(self, pv: PVOID, cb: int) -> PVOID: ...
    
    @virtual_table.function(VOID, PVOID)
    def Free(self, pv: PVOID): ...
    
    @virtual_table.function(SIZE_T, PVOID)
    def GetSize(self, pv: PVOID) -> int: ...
    
    @virtual_table.function(INT, PVOID)
    def DidAlloc(self, pv: PVOID) -> int: ...
    
    @virtual_table.function(VOID)
    def HeapMinimize(self): ...
    
    virtual_table.build()

LPMALLOC = IMalloc.PTR()

class IStdMarshalInfo(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IStdMarshalInfo')
    _iid_ = IID('{00000018-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(DWORD, PVOID, PCLSID)
    def GetClassForHandler(self, dwDestContext: int, pvDestContext: PVOID, 
                           pClsid: IPointer[CLSID]) -> int: ...
    
    virtual_table.build()
    
LPSTDMARSHALINFO = IStdMarshalInfo.PTR()

class IExternalConnection(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IExternalConnection')
    _iid_ = IID('{00000019-0000-0000-C000-000000000046}')
    
    @virtual_table.function(DWORD, DWORD, DWORD)
    def AddConnection(self, extconn: int, reserved: int) -> int: ...
    
    @virtual_table.function(DWORD, DWORD, DWORD, BOOL)
    def ReleaseConnection(self, extconn: int, reserved: int, 
                          fLastReleaseCloses: bool) -> int: ...
    
    virtual_table.build()

LPEXTERNALCONNECTION = IExternalConnection.PTR()

class MULTI_QI(CStructure):
    _fields_ = [
        ('pIID', LPIID),
        ('pItf', LPUNKNOWN),
        ('hr', HRESULT)
    ]
    
    pItf: IPointer[IUnknown]
    pIID: IPointer[IID]
    hr: int
    
class IMultiQI(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IMultiQI')
    _iid_ = IID('{00000020-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ULONG, MULTI_QI.PTR())
    def QueryMultipleInterfaces(self, cMQIs: int, 
                                pMQIs: IPointer[MULTI_QI]) -> int: ...
    
    virtual_table.build()
    
LPMULTIQI = MULTI_QI.PTR()

class IInternalUnknown(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IInternalUnknown')
    _iid_ = IID('{00000021-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True)
    def QueryInternalInterface(self, iid: IID, ppv: IPointer[PVOID],
                               **kwargs) -> int:
        return self.virt_delegate(iid.ref(), ppv)
    
    virtual_table.build()
    
class IEnumUnknown(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IEnumUnknown')
    _iid_ = IID('{00000100-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ULONG, POINTER(LPUNKNOWN), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[IUnknown],
             pceltFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumUnknown']) -> int: ...
    
    virtual_table.build()
        
LPENUMUNKNOWN = IEnumUnknown.PTR()
    
class IEnumString(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IMarshal.virtual_table, 'IEnumString')
    _iid_ = IID('{00000101-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ULONG, POINTER(LPOLESTR), PULONG)
    def Next(self, celt: int, rgelt: IPointer[LPOLESTR],
             pceltFetched: PULONG) -> int: ...
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumString']) -> int: ...
    
    virtual_table.build()

LPENUMSTRING = IEnumString.PTR()
    
class ISynchronize(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ISynchronize')
    _iid_ = IID('{00000030-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(DWORD, DWORD)
    def Wait(self, dwFlags: int, dwMilliseconds: int) -> int: ...
    
    @virtual_table.com_function()
    def Signal(self) -> int: ...
    
    @virtual_table.com_function()
    def Reset(self) -> int: ...
    
    virtual_table.build()
    
DCOM_NONE	= 0
DCOM_CALL_COMPLETE	= 0x1
DCOM_CALL_CANCELED	= 0x2
DCOM_CALL_STATE = INT
    
class IAsyncManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IAsyncManager')
    _iid_ = IID('{0000002A-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(HRESULT)
    def CompleteCall(self, Result: int) -> int: ...
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True)
    def GetCallContext(self, iid: IID, pInterface: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref(), pInterface)
    
    @virtual_table.com_function(PULONG)
    def GetState(self, pulStateFlags: PULONG) -> int: ...
    
    virtual_table.build()
    
RPCOLEDATAREP = ULONG

class RPCOLEMESSAGE(CStructure):
    _fields_ = [
        ('reserved1', PVOID),
        ('dataRepresentation', RPCOLEDATAREP),
        ('Buffer', PVOID),
        ('cbBuffer', ULONG),
        ('iMethod', ULONG),
        ('reserved2', PVOID * 5),
        ('rpcFlags', ULONG)
    ]
    
    dataRepresentation: int
    Buffer: PVOID
    cbBuffer: int
    rpcFlags: int
    iMethod: int

PRPCOLEMESSAGE = RPCOLEMESSAGE.PTR()
    
class IRpcChannelBuffer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IRpcChannelBuffer')
    _iid_ = IID('{D5F56B60-593B-101A-B569-08002B2DBF7A}')
    
    @virtual_table.com_function(PRPCOLEMESSAGE, REFIID, intermediate_method=True)
    def GetBuffer(self, pMessage: IPointer[RPCOLEMESSAGE], iid: IID, **kwargs) -> int:
        return self.virt_delegate(pMessage, iid.ref())
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PULONG)
    def SendReceive(self, pMessage: IPointer[RPCOLEMESSAGE], pStatus: PULONG) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE)
    def FreeBuffer(self, pMessage: IPointer[RPCOLEMESSAGE]) -> int: ...
    
    @virtual_table.com_function(PDWORD, PVOID)
    def GetDestCtx(self, pdwDestContext: PDWORD, ppvDestContext: IPointer[PVOID]) -> int: ...
    
    @virtual_table.com_function()
    def IsConnected(self) -> int: ...
    
    virtual_table.build()
    
class IRpcChannelBuffer2(IRpcChannelBuffer):
    virtual_table = COMVirtualTable.from_ancestor(
        IRpcChannelBuffer.virtual_table, 'IRpcChannelBuffer2')
    _iid_ = IID('{594f31d0-7f19-11d0-b194-00a0c90dc8bf}')
    
    @virtual_table.com_function(PDWORD)
    def GetProtocolVersion(self, pdwVersion: PDWORD) -> int: ...
    
    virtual_table.build()

class IAsyncRpcChannelBuffer(IRpcChannelBuffer2):
    virtual_table = COMVirtualTable.from_ancestor(
        IRpcChannelBuffer2.virtual_table, 'IAsyncRpcChannelBuffer')
    _iid_ = IID('{a5029fb6-3c34-11d1-9c99-00c04fb998aa}')
    
    @virtual_table.com_function(PRPCOLEMESSAGE, ISynchronize.PTR(), PULONG)
    def Send(self, pMsg: IPointer[RPCOLEMESSAGE], 
             pSync: IPointer[ISynchronize], pulStatus: PULONG) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PULONG)
    def Receive(self, pMsg: IPointer[RPCOLEMESSAGE], pulStatus: PULONG) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PDWORD, PVOID)
    def GetDestCtxEx(self, pMsg: IPointer[RPCOLEMESSAGE], 
                     pdwDestContext: PDWORD, ppvDestContext: IPointer[PVOID]) -> int: ...
    
    virtual_table.build()
    
class IRpcChannelBuffer3(IRpcChannelBuffer2):
    virtual_table = COMVirtualTable.from_ancestor(
        IRpcChannelBuffer2.virtual_table, 'IRpcChannelBuffer3')
    _iid_ = IID('{25B15600-0115-11d0-BF0D-00AA00B8DFD2}')
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PULONG)
    def Send(self, pMsg: IPointer[RPCOLEMESSAGE], pulStatus: PULONG) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, ULONG, PULONG)
    def Receive(self, pMsg: IPointer[RPCOLEMESSAGE], ulSize: int, pulStatus: PULONG) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE)
    def Cancel(self, pMsg: IPointer[RPCOLEMESSAGE]) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, REFIID, PVOID, intermediate_method=True)
    def GetCallContext(self, pMsg: IPointer[RPCOLEMESSAGE], iid: IID, 
                       pInterface: IPointer[PVOID], **kwargs) -> int: 
        return self.virt_delegate(pMsg, iid.ref(), pInterface)
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PDWORD, PVOID)
    def GetDestCtxEx(self, pMsg: IPointer[RPCOLEMESSAGE], 
                     pdwDestContext: PDWORD, ppvDestContext: IPointer[PVOID]) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, PDWORD)
    def GetState(self, pMsg: IPointer[RPCOLEMESSAGE], pState: PDWORD) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, IAsyncManager.PTR())
    def RegisterAsync(self, pMsg: IPointer[RPCOLEMESSAGE],
                      pAsyncMgr: IPointer[IAsyncManager]) -> int: ...
    
    virtual_table.build()

class IRpcSyntaxNegotiate(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IRpcSyntaxNegotiate')
    _iid_ = IID('{58a08519-24c8-4935-b482-3fd823333a4f}')
    
    @virtual_table.com_function(PRPCOLEMESSAGE)
    def NegotiateSyntax(self, pMsg: IPointer[RPCOLEMESSAGE]) -> int: ...
    
    virtual_table.build()
    
class IRpcProxyBuffer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IRpcProxyBuffer')
    _iid_ = IID('{D5F56A34-593B-101A-B569-08002B2DBF7A}')
    
    @virtual_table.com_function(IRpcChannelBuffer.PTR())
    def Connect(self, pRpcChannelBuffer: IPointer[IRpcChannelBuffer]) -> int: ...
    
    @virtual_table.com_function()
    def Disconnect(self) -> int: ...
    
    virtual_table.build()
    
class IRpcStubBuffer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IRpcStubBuffer')
    _iid_ = IID('{D5F56AFC-593B-101A-B569-08002B2DBF7A}')
    
    @virtual_table.com_function(LPUNKNOWN)
    def Connect(self, pUnkServer: IPointer[IUnknown]) -> int: ...
    
    @virtual_table.com_function()
    def Disconnect(self) -> int: ...
    
    @virtual_table.com_function(PRPCOLEMESSAGE, IRpcChannelBuffer.PTR())
    def Invoke(self, _prpcmsg: IPointer[RPCOLEMESSAGE],
               _pRpcChannelBuffer: IPointer[IRpcChannelBuffer]) -> int: ...
    
    @virtual_table.function(THIS, REFIID, intermediate_method=True)
    def IsIIDSupported(self, iid: IID, **kwargs) -> IPointer['IRpcStubBuffer']:
        result = self.virt_delegate(iid.ref())
        return reinterpret_cast[IRpcStubBuffer.PTR()](result)
    
    @virtual_table.function(ULONG)
    def CountRefs(self) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def DebugServerQueryInterface(self, ppv: IPointer[PVOID]) -> int: ...
    
    @virtual_table.com_function(PVOID)
    def DebugServerRelease(self, pv: PVOID) -> int: ...
    
    virtual_table.build()

class IPSFactoryBuffer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IPSFactoryBuffer')
    _iid_ = IID('{D5F569D0-593B-101A-B569-08002B2DBF7A}')
    
    @virtual_table.com_function(LPUNKNOWN, REFIID, POINTER(IRpcProxyBuffer.PTR()), 
                                PVOID, intermediate_method=True)
    def CreateProxy(self, pUnkOuter: IPointer[IUnknown], iid: IID,
                    ppProxy: IDoublePtr[IRpcProxyBuffer],
                    ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(pUnkOuter, iid.ref(), 
                                     ppProxy, ppv)
    
    @virtual_table.com_function(REFIID, LPUNKNOWN, POINTER(IRpcProxyBuffer.PTR()),
                                intermediate_method=True)
    def CreateStub(self, iid: IID, pUnkServer: IPointer[IUnknown],
                   ppStub: IDoublePtr[IRpcProxyBuffer], **kwargs) -> int:
        return self.virt_delegate(iid.ref(), pUnkServer, ppStub)
    
    virtual_table.build()
    
class SChannelHookCallInfo(CStructure):
    _fields_ = [
        ('iid', IID),
        ('cbSize', DWORD),
        ('uCausality', GUID),
        ('dwServerPid', DWORD),
        ('iMethod', DWORD),
        ('pObject', PVOID)
    ]
    
    dwServerPid: int
    pObject: PVOID
    iMethod: int
    cbSize: int
    
    uCausality: GUID
    iid: IID
    
class IChannelHook(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IChannelHook')
    _iid_ = IID('{1008c4a0-7613-11cf-9af1-0020af6e72f4}')
    
    @virtual_table.function(VOID, REFGUID, REFIID, PULONG, intermediate_method=True)
    def ClientGetSize(self, uExtent: GUID, iid: IID, pDataSize: PULONG, **kwargs):
        return self.virt_delegate(uExtent.ref(), iid.ref(), pDataSize)
    
    @virtual_table.function(VOID, REFGUID, REFIID, PULONG, PVOID, intermediate_method=True)
    def ClientFillBuffer(self, uExtent: GUID, iid: IID, pDataSize: PULONG,
                      pDataBuffer: PVOID, **kwargs):
        return self.virt_delegate(uExtent.ref(), iid.ref(), pDataSize, pDataBuffer)
    
    @virtual_table.function(VOID, REFGUID, REFIID, ULONG, PVOID, DWORD, HRESULT,
                            intermediate_method=True)
    def ClientNotify(self, uExtent: GUID, iid: IID, cbDataSize: int, 
                     pDataBuffer: PVOID, lDataRep: int, hrFault: int, **kwargs) -> int:
        return self.virt_delegate(uExtent.ref(), iid.ref(),
                                     cbDataSize, pDataBuffer, lDataRep, hrFault)
    
    @virtual_table.function(VOID, REFGUID, REFIID, ULONG, PVOID, DWORD, HRESULT,
                            intermediate_method=True)
    def ServerNotify(self, uExtent: GUID, iid: IID, cbDataSize: int, 
                     pDataBuffer: PVOID, lDataRep: int, **kwargs) -> int:
        return self.virt_delegate(uExtent.ref(), iid.ref(),
                                     cbDataSize, pDataBuffer, lDataRep)
    
    @virtual_table.function(VOID, REFGUID, REFIID, HRESULT, PULONG, 
                            intermediate_method=True)
    def ServerGetSize(self, uExtent: GUID, iid: IID, hrFault: int, 
                      pDataSize: PULONG, **kwargs) -> int:
        return self.virt_delegate(uExtent.ref(), iid.ref(),
                                     hrFault, pDataSize)
        
    @virtual_table.function(VOID, REFGUID, REFIID, PULONG, PVOID, 
                            HRESULT, intermediate_method=True)
    def ServerFillBuffer(self, uExtent: GUID, iid: IID, pDataSize: PULONG,
                         pDataBuffer: PVOID, hrFault: int, **kwargs) -> int: 
        return self.virt_delegate(uExtent.ref(), iid.ref(), 
                                     pDataSize, pDataBuffer, hrFault)
    
    virtual_table.build()

class SOLE_AUTHENTICATION_SERVICE(CStructure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pPrincipalName', LPOLESTR),
        ('hr', HRESULT)
    ]
    
    dwAuthnSvc: int
    dwAuthzSvc: int
    
    pPrincipalName: str
    hr: int

PSOLE_AUTHENTICATION_SERVICE = SOLE_AUTHENTICATION_SERVICE.PTR()

EOAC_NONE	= 0
EOAC_MUTUAL_AUTH	= 0x1
EOAC_STATIC_CLOAKING	= 0x20
EOAC_DYNAMIC_CLOAKING	= 0x40
EOAC_ANY_AUTHORITY	= 0x80
EOAC_MAKE_FULLSIC	= 0x100
EOAC_DEFAULT	= 0x800
EOAC_SECURE_REFS	= 0x2
EOAC_ACCESS_CONTROL	= 0x4
EOAC_APPID	= 0x8
EOAC_DYNAMIC	= 0x10
EOAC_REQUIRE_FULLSIC	= 0x200
EOAC_AUTO_IMPERSONATE	= 0x400
EOAC_DISABLE_AAA	= 0x1000
EOAC_NO_CUSTOM_MARSHAL	= 0x2000
EOAC_RESERVED1	= 0x4000
EOLE_AUTHENTICATION_CAPABILITIES = INT

COLE_DEFAULT_PRINCIPAL = i_cast(-1, LPOLESTR)
COLE_DEFAULT_AUTHINFO = i_cast(-1, PVOID)

class SOLE_AUTHENTICATION_INFO(CStructure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pAuthInfo', PVOID)
    ]
    
    pAuthInfo: PVOID
    dwAuthnSvc: int
    dwAuthzSvc: int

PSOLE_AUTHENTICATION_INFO = SOLE_AUTHENTICATION_INFO.PTR()

class SOLE_AUTHENTICATION_LIST(CStructure):
    _fields_ = [
        ('cAuthInfo', DWORD),
        ('aAuthInfo', PSOLE_AUTHENTICATION_INFO)
    ]
    
    aAuthInfo: IPointer[SOLE_AUTHENTICATION_INFO]
    cAuthInfo: int
    
PSOLE_AUTHENTICATION_LIST = SOLE_AUTHENTICATION_LIST.PTR()

class IClientSecurity(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IClientSecurity')
    _iid_ = IID('{0000013D-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(LPUNKNOWN, PDWORD, PDWORD, POINTER(LPOLESTR), 
                                PDWORD, PDWORD, PVOID, PDWORD)
    def QueryBlanket(self, pProxy: IPointer[IUnknown], pAuthnSvc: PDWORD,
                     pAuthzSvc: PDWORD, pServerPrincName: IPointer[LPOLESTR],
                     pAuthnLevel: PDWORD, pImpLevel: PDWORD, pAuthInfo: IPointer[PVOID],
                     pCapabilities: PDWORD) -> int: ...
    
    @virtual_table.com_function(LPUNKNOWN, DWORD, DWORD, LPOLESTR, 
                                DWORD, DWORD, PVOID, DWORD)
    def SetBlanket(self, pProxy: IPointer[IUnknown], dwAuthnSvc: int,
                     dwAuthzSvc: int, pServerPrincName: str,
                     dwAuthnLevel: int, dwImpLevel: int, pAuthInfo: PVOID,
                     dwCapabilities: int) -> int: ...
    
    @virtual_table.com_function(LPUNKNOWN, POINTER(LPUNKNOWN))
    def CopyProxy(self, pProxy: IPointer[IUnknown], ppCopy: IDoublePtr[IUnknown]) -> int: ...
    
    virtual_table.build()

class IServerSecurity(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IServerSecurity')
    _iid_ = IID('{000001cf-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(PDWORD, PDWORD, POINTER(LPOLESTR), 
                                PDWORD, PDWORD, PVOID, PDWORD)
    def QueryBlanket(self, pAuthnSvc: PDWORD, pAuthzSvc: PDWORD, 
                     pServerPrincName: IPointer[LPOLESTR],
                     pAuthnLevel: PDWORD, pImpLevel: PDWORD, pPrivs: IPointer[PVOID],
                     pCapabilities: PDWORD) -> int: ...
    
    @virtual_table.com_function()
    def ImpersonateClient(self) -> int: ...
    
    @virtual_table.com_function()
    def RevertToSelf(self) -> int: ...
    
    @virtual_table.function(BOOL, result_function=bool)
    def IsImpersonating(self) -> bool: ...
    
    virtual_table.build()
    
COMBND_RPCTIMEOUT	= 0x1
COMBND_SERVER_LOCALITY	= 0x2
COMBND_RESERVED1	= 0x4
COMBND_RESERVED2	= 0x5
COMBND_RESERVED3	= 0x8
COMBND_RESERVED4	= 0x10
RPCOPT_PROPERTIES = INT

SERVER_LOCALITY_PROCESS_LOCAL	= 0
SERVER_LOCALITY_MACHINE_LOCAL	= 1
SERVER_LOCALITY_REMOTE	= 2
RPCOPT_SERVER_LOCALITY_VALUES = INT

class IRpcOptions(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IRpcOptions')
    _iid_ = IID('{00000144-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(LPUNKNOWN, RPCOPT_PROPERTIES, ULONG_PTR)
    def Set(self, pPrx: IPointer[IUnknown], dwProperty: int, dwValue: int) -> int: ...
    
    @virtual_table.com_function(LPUNKNOWN, RPCOPT_PROPERTIES, PULONG_PTR)
    def Query(self, pPrx: IPointer[IUnknown], dwProperty: int, pdwValue: PULONG_PTR) -> int: ...
    
    virtual_table.build()
    
COMGLB_EXCEPTION_HANDLING	= 1
COMGLB_APPID	= 2
COMGLB_RPC_THREADPOOL_SETTING	= 3
COMGLB_RO_SETTINGS	= 4
COMGLB_UNMARSHALING_POLICY	= 5
COMGLB_PROPERTIES_RESERVED1	= 6
COMGLB_PROPERTIES_RESERVED2	= 7
COMGLB_PROPERTIES_RESERVED3	= 8
GLOBALOPT_PROPERTIES = INT

COMGLB_EXCEPTION_HANDLE	= 0
COMGLB_EXCEPTION_DONOT_HANDLE_FATAL	= 1
COMGLB_EXCEPTION_DONOT_HANDLE	= COMGLB_EXCEPTION_DONOT_HANDLE_FATAL
COMGLB_EXCEPTION_DONOT_HANDLE_ANY	= 2
GLOBALOPT_EH_VALUES = INT

COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL	= 0
COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL	= 1
GLOBALOPT_RPCTP_VALUES = INT

COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES	= 0x1
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES	= 0x2
COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES	= 0x4
COMGLB_FAST_RUNDOWN	= 0x8
COMGLB_RESERVED1	= 0x10
COMGLB_RESERVED2	= 0x20
COMGLB_RESERVED3	= 0x40
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES	= 0x80
COMGLB_RESERVED4	= 0x100
COMGLB_RESERVED5	= 0x200
COMGLB_RESERVED6	= 0x400
GLOBALOPT_RO_FLAGS = INT

COMGLB_UNMARSHALING_POLICY_NORMAL	= 0
COMGLB_UNMARSHALING_POLICY_STRONG	= 1
COMGLB_UNMARSHALING_POLICY_HYBRID	= 2
GLOBALOPT_UNMARSHALING_POLICY_VALUES = INT

class IGlobalProperties(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IGlobalProperties')
    _iid_ = IID('{0000015B-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(GLOBALOPT_PROPERTIES, ULONG_PTR)
    def Set(self, dwProperty: int, dwValue: int) -> int: ...
    
    @virtual_table.com_function(GLOBALOPT_PROPERTIES, PULONG_PTR)
    def Query(self, dwProperty: int, pdwValue: PULONG_PTR) -> int: ...
    
    virtual_table.build()
    
class ISurrogate(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ISurrogate')
    _iid_ = IID('{00000022-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(REFCLSID, intermediate_method=True)
    def LoadDllServer(self, Clsid: CLSID, **kwargs) -> int:
        return self.virt_delegate(Clsid.ref())
    
    @virtual_table.com_function()
    def FreeSurrogate(self) -> int: ...
    
    virtual_table.build()
    
LPSURROGATE = ISurrogate.PTR()

class IGlobalInterfaceTable(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IGlobalInterfaceTable')
    _iid_ = IID('{00000146-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(LPUNKNOWN, REFIID, PDWORD, intermediate_method=True)
    def RegisterInterfaceInGlobal(self, pUnk: IPointer[IUnknown], iid: IID,
                                  pdwCookie: PDWORD, **kwargs) -> int:
        return self.virt_delegate(pUnk, iid.ref(), pdwCookie)
    
    @virtual_table.com_function(DWORD)
    def RevokeInterfaceFromGlobal(self, dwCookie: int) -> int: ...
    
    @virtual_table.com_function(DWORD, REFIID, PVOID, intermediate_method=True)
    def GetInterfaceFromGlobal(self, dwCookie: int, iid: IID,
                               ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(dwCookie, iid.ref(), ppv)
    
    virtual_table.build()
    
class ISynchronizeHandle(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ISynchronizeHandle')
    _iid_ = IID('{00000031-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(PHANDLE)
    def GetHandle(self, ph: IPointer[HANDLE]) -> int: ...
    
    virtual_table.build()
    
class ISynchronizeEvent(ISynchronizeHandle):
    virtual_table = COMVirtualTable.from_ancestor(
        ISynchronizeHandle.virtual_table, 'ISynchronizeEvent')
    _iid_ = IID('{00000032-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(PHANDLE)
    def SetEventHandle(self, ph: IPointer[HANDLE]) -> int: ...
    
    virtual_table.build()
    
class ISynchronizeContainer(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ISynchronizeContainer')
    _iid_ = IID('{00000033-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ISynchronize.PTR())
    def AddSynchronize(self, pSync: IPointer[ISynchronize]) -> int: ...
    
    @virtual_table.com_function(DWORD, DWORD, POINTER(ISynchronize.PTR()))
    def WaitMultiple(self, dwFlags: int, dwTimeOut: int, 
                     ppSync: IDoublePtr[ISynchronize]) -> int: ...
    
    virtual_table.build()

class ISynchronizeMutex(ISynchronize):
    virtual_table = COMVirtualTable.from_ancestor(
        ISynchronize.virtual_table, 'ISynchronizeMutex')
    _iid_ = IID('{00000025-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function()
    def ReleaseMutex(self) -> int: ...
    
    virtual_table.build()
    
class ICancelMethodCalls(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ICancelMethodCalls')
    _iid_ = IID('{00000029-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(ULONG)
    def Cancel(self, ulSeconds: int) -> int: ...
    
    @virtual_table.com_function()
    def TestCancel(self) -> int: ...
    
    virtual_table.build()

class ICallFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'ICallFactory')
    _iid_ = IID('{1c733a30-2a1c-11ce-ade5-00aa0044773d}')
    
    @virtual_table.com_function(REFIID, LPUNKNOWN, REFIID, 
                                POINTER(LPUNKNOWN), intermediate_method=True)
    def CreateCall(self, iid: IID, pCtrlUnk: IPointer[IUnknown],
                   iid2: IID, ppv: IDoublePtr[IUnknown], **kwargs) -> int: 
        return self.virt_call_method(iid.ref(), pCtrlUnk, iid2.ref(), ppv)
    
    virtual_table.build()

class IRpcHelper(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown.virtual_table, 'IRpcHelper')
    _iid_ = IID('{00000149-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(PDWORD)
    def GetDCOMProtocolVersion(self, pComVersion: PDWORD) -> int: ...
    
    @virtual_table.com_function(PVOID, POINTER(LPIID))
    def GetIIDFromOBJREF(self, pObjRef: PVOID, piid: IDoublePtr[IID]) -> int: ...
    
    virtual_table.build()
    
class IReleaseMarshalBuffers(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IReleaseMarshalBuffers')
    _iid_ = IID('{eb0cb9e8-7996-11d2-872e-0000f8080859}')
    
    @virtual_table.com_function(PRPCOLEMESSAGE, DWORD, LPUNKNOWN)
    def ReleaseMarshalBuffer(self, pMsg: IPointer[RPCOLEMESSAGE],
                             dwFlags: int, pChnl: IPointer[IUnknown]) -> int: ...
    
    virtual_table.build()
    
class IWaitMultiple(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IWaitMultiple')
    _iid_ = IID('{0000002B-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(DWORD, POINTER(ISynchronize.PTR()))
    def WaitMultiple(self, timeout: int, pSync: IDoublePtr[ISynchronize]) -> int: ...
    
    @virtual_table.com_function(ISynchronize.PTR())
    def AddSynchronize(self, pSync: IPointer[ISynchronize]) -> int: ...
    
    virtual_table.build()
    
class IAddrTrackingControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IAddrTrackingControl')
    _iid_ = IID('{00000147-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function()
    def EnableCOMDynamicAddrTracking(self) -> int: ...
    
    @virtual_table.com_function()
    def DisableCOMDynamicAddrTracking(self) -> int: ...
    
    virtual_table.build()
    
LPADDRTRACKINGCONTROL = IAddrTrackingControl.PTR()
    
class IAddrExclusionControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IAddrExclusionControl')
    _iid_ = IID('{00000148-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True)
    def GetCurrentAddrExclusionList(self, iid: IID,
                                    ppEnumerator: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref(), ppEnumerator)
    
    @virtual_table.com_function(LPUNKNOWN)
    def UpdateAddrExclusionList(self, pEnumerator: IPointer[IUnknown]) -> int: ...
    
    virtual_table.build()

LPADDREXCLUSIONCONTROL = IAddrExclusionControl.PTR()
    
class IPipeByte(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IPipeByte')
    _iid_ = IID('{DB2F3ACA-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(PBYTE, ULONG, PULONG)
    def Pull(self, buf: PBYTE, cRequest: int, pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(PBYTE, ULONG)
    def Push(self, buf: PBYTE, cSent: int) -> int: ...
    
    virtual_table.build()
    
class AsyncIPipeByte(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'AsyncIPipeByte')
    _iid_ = IID('{DB2F3ACB-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(ULONG)
    def Begin_Pull(self, cRequest: int) -> int: ...
    
    @virtual_table.com_function(PBYTE, ULONG, PULONG)
    def Finish_Pull(self, buf: PBYTE, pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(PBYTE, ULONG)
    def Begin_Push(self, buf: PBYTE, cSent: int) -> int: ...
    
    @virtual_table.com_function()
    def Finish_Push(self) -> int: ...
    
    virtual_table.build()
    
class IPipeLong(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IPipeLong')
    _iid_ = IID('{DB2F3ACC-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(PLONG, ULONG, PULONG)
    def Pull(self, buf: PLONG, cRequest: int, pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(PLONG, ULONG)
    def Push(self, buf: PLONG, cSent: int) -> int: ...
    
    virtual_table.build()
    
class AsyncIPipeLong(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'AsyncIPipeLong')
    _iid_ = IID('{DB2F3ACD-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(ULONG)
    def Begin_Pull(self, cRequest: int) -> int: ...
    
    @virtual_table.com_function(PLONG, ULONG, PULONG)
    def Finish_Pull(self, buf: PLONG, pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(PLONG, ULONG)
    def Begin_Push(self, buf: PLONG, cSent: int) -> int: ...
    
    @virtual_table.com_function()
    def Finish_Push(self) -> int: ...
    
    virtual_table.build()
    
class IPipeDouble(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IPipeDouble')
    _iid_ = IID('{DB2F3ACE-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(POINTER(DOUBLE), ULONG, PULONG)
    def Pull(self, buf: IPointer[DOUBLE], cRequest: int, pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(POINTER(DOUBLE), ULONG)
    def Push(self, buf: IPointer[DOUBLE], cSent: int) -> int: ...
    
    virtual_table.build()
    
class AsyncIPipeDouble(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'AsyncIPipeDouble')
    _iid_ = IID('{DB2F3ACF-2F86-11d1-8E04-00C04FB9989A}')
    
    @virtual_table.com_function(ULONG)
    def Begin_Pull(self, cRequest: int) -> int: ...
    
    @virtual_table.com_function(POINTER(DOUBLE), ULONG, PULONG)
    def Finish_Pull(self, buf: IPointer[DOUBLE], pcReturned: PULONG) -> int: ...
    
    @virtual_table.com_function(POINTER(DOUBLE), ULONG)
    def Begin_Push(self, buf: IPointer[DOUBLE], cSent: int) -> int: ...
    
    @virtual_table.com_function()
    def Finish_Push(self) -> int: ...
    
    virtual_table.build()
    
APTTYPEQUALIFIER_NONE	= 0
APTTYPEQUALIFIER_IMPLICIT_MTA	= 1
APTTYPEQUALIFIER_NA_ON_MTA	= 2
APTTYPEQUALIFIER_NA_ON_STA	= 3
APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA	= 4
APTTYPEQUALIFIER_NA_ON_MAINSTA	= 5
APTTYPEQUALIFIER_APPLICATION_STA	= 6
APTTYPEQUALIFIER_RESERVED_1	= 7
APTTYPEQUALIFIER = INT

APTTYPE_CURRENT	= -1
APTTYPE_STA	= 0
APTTYPE_MTA	= 1
APTTYPE_NA	= 2
APTTYPE_MAINSTA	= 3
APTTYPE = INT
    
THDTYPE_BLOCKMESSAGES	= 0
THDTYPE_PROCESSMESSAGES	= 1
THDTYPE = INT

APARTMENTID = DWORD

class IComThreadingInfo(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IComThreadingInfo')
    _iid_ = IID('{000001ce-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(POINTER(APTTYPE))
    def GetCurrentApartmentType(self, pAptType: IPointer[APTTYPE]) -> int: ...
    
    @virtual_table.com_function(POINTER(THDTYPE))
    def GetCurrentThreadType(self, pAptType: IPointer[THDTYPE]) -> int: ...
    
    @virtual_table.com_function(POINTER(APTTYPE))
    def GetCurrentLogicalThreadId(self, pguidLogicalThreadId: IPointer[GUID]) -> int: ...
    
    @virtual_table.com_function(REFGUID, intermediate_method=True)
    def SetCurrentLogicalThreadId(self, guid: GUID, **kwargs) -> int:
        return self.virt_delegate(guid.ref())
    
    virtual_table.build()
    
class IProcessInitControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IProcessInitControl')
    _iid_ = IID('{72380d55-8d2b-43a3-8513-2b6ef31434e9}')
    
    @virtual_table.com_function(DWORD)
    def ResetInitializerTimeout(self, dwSecondsRemaining: int) -> int: ...
    
    virtual_table.build()
    
class IFastRundown(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IFastRundown')
    _iid_ = IID('{00000040-0000-0000-C000-000000000046}')
    
    virtual_table.build()
    
CO_MARSHALING_SOURCE_IS_APP_CONTAINER	= 0
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1	= 0x80000000
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2	= 0x80000001
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3	= 0x80000002
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4	= 0x80000003
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5	= 0x80000004
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6	= 0x80000005
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7	= 0x80000006
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8	= 0x80000007
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9	= 0x80000008
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10	= 0x80000009
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11	= 0x8000000a
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12	= 0x8000000b
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_13	= 0x8000000c
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_14	= 0x8000000d
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_15	= 0x8000000e
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_16	= 0x8000000f
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_17	= 0x80000010
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_18	= 0x80000011
CO_MARSHALING_CONTEXT_ATTRIBUTES = INT

class IMarshalingStream(IStream):
    virtual_table = COMVirtualTable.from_ancestor(
        IStream.virtual_table, 'IMarshalingStream')
    _iid_ = IID('{D8F2F5E6-6102-4863-9F26-389A4676EFDE}')
    
    @virtual_table.com_function(CO_MARSHALING_CONTEXT_ATTRIBUTES, PULONG_PTR)
    def GetMarshalingContextAttributes(self, attribute: int, 
                                       pAttributeValue: PULONG_PTR) -> int: ...
    
    virtual_table.build()
   
class IAgileReference(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IAgileReference')
    _iid_ = IID('{C03F6A43-65A4-9818-987E-E0B810D2A6F2}')
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True)
    def Resolve(self, iid: IID, ppvObjectReference: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(iid.ref(), ppvObjectReference)
    
    virtual_table.build()
    
class MachineGlobalObjectTableRegistrationToken(CStructure):
    _fields_ = [
        ('unused', INT)
    ]
    
class IMachineGlobalObjectTable(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IMachineGlobalObjectTable')
    _iid_ = IID('{26d709ac-f70b-4421-a96f-d2878fafb00d}')
    
    @virtual_table.com_function(REFCLSID, LPCWSTR, LPUNKNOWN,
                                MachineGlobalObjectTableRegistrationToken.PTR(),
                                intermediate_method=True)
    def RegisterObject(self, clsid: CLSID, identifier: str, object: IPointer[IUnknown],
                       token: IPointer[MachineGlobalObjectTableRegistrationToken], **kwargs) -> int:
        return self.virt_delegate(clsid.ref(), identifier, object, token)
    
    @virtual_table.com_function(REFCLSID, LPCWSTR, REFIID, PVOID, 
                                intermediate_method=True)
    def GetObject(self, clsid: CLSID, identifier: str, iid: IID,
                  ppv: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(clsid.ref(), identifier,
                                     iid.ref(), ppv)
    
    @virtual_table.com_function(MachineGlobalObjectTableRegistrationToken)
    def RevokeObject(self, token: MachineGlobalObjectTableRegistrationToken) -> int: ...
    
    virtual_table.build()
    
class ISupportAllowLowerTrustActivation(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'ISupportAllowLowerTrustActivation')
    _iid_ = IID('{e9956ef2-3828-4b4b-8fa9-7db61dee4954}')
    
    virtual_table.build()