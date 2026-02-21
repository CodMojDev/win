#
# com/rpc/dce.py
#

from ...defbase_errordef import *
from ...guiddef import *
from .coredef import *

RPC_CSTR = LPSTR
RPC_WSTR = LPWSTR
RPC_CWSTR = LPCWSTR

RPC_BINDING_HANDLE = I_RPC_HANDLE
handle_t = RPC_BINDING_HANDLE
rpc_binding_handle_t = RPC_BINDING_HANDLE

class UUID(GUID):
    def __str__(self) -> str:
        RpcStringUuid = RPC_WSTR()
        RpcStatus = UuidToStringW(self.ref(), byref(RpcStringUuid))
        if RpcStatus != RPC_S_OK: raise WinException(RpcStatus)
        StringUuid = RpcStringUuid.value
        RpcStringFreeW(RpcStringUuid)
        return StringUuid
    
    @classmethod
    def nil(cls) -> Self:
        uuid = cls()
        RpcStatus = UuidCreateNil(uuid.ref())
        if RpcStatus != RPC_S_OK: raise WinException(RpcStatus)
        return uuid
    
    @classmethod
    def create(cls) -> Self:
        uuid = cls()
        RpcStatus = UuidCreate(uuid.ref())
        if RpcStatus != RPC_S_OK: raise WinException(RpcStatus)
        return uuid
    
    @classmethod
    def sequential(cls) -> Self:
        uuid = cls()
        RpcStatus = UuidCreateSequential(uuid.ref())
        if RpcStatus != RPC_S_OK: raise WinException(RpcStatus)
        return uuid
    
    def __bool__(self) -> bool:
        return UuidIsNil(self.ref(), NULL) != RPC_S_OK
    
    def __eq__(self, Uuid: Self) -> bool:
        return UuidEqual(self.ref(), Uuid.ref(), NULL) == RPC_S_OK
    
uuid_t = UUID

class RPC_BINDING_VECTOR(CStructure):
    _fields_ = [
        ('Count', ULONG)
    ]
    
    BindingH: IArray[RPC_BINDING_HANDLE]
    Count: int
    
flexible_array(RPC_BINDING_VECTOR, 'BindingH', RPC_BINDING_HANDLE)
rpc_binding_vector_t = RPC_BINDING_VECTOR

class UUID_VECTOR(CStructure):
    _fields_ = [
        ('Count', ULONG)
    ]
    
    Uuid: IArray[UUID]
    Count: int
    
flexible_array(UUID_VECTOR, 'Uuid', UUID)
uuid_vector_t = UUID_VECTOR

RPC_IF_HANDLE = PVOID

class RPC_IF_ID(CStructure):
    _fields_ = [
        ('Uuid', UUID),
        ('VersMajor', USHORT),
        ('VersMinor', USHORT)
    ]
    
    VersMajor: int
    VersMinor: int
    Uuid: UUID

RPC_C_BINDING_INFINITE_TIMEOUT = 10
RPC_C_BINDING_MIN_TIMEOUT = 0
RPC_C_BINDING_DEFAULT_TIMEOUT = 5
RPC_C_BINDING_MAX_TIMEOUT = 9

RPC_C_CANCEL_INFINITE_TIMEOUT = -1

RPC_C_LISTEN_MAX_CALLS_DEFAULT = 1234
RPC_C_PROTSEQ_MAX_REQS_DEFAULT = 10

# RPC_POLICY EndpointFlags.
RPC_C_BIND_TO_ALL_NICS          = 1
RPC_C_USE_INTERNET_PORT         = 0x1
RPC_C_USE_INTRANET_PORT         = 0x2
RPC_C_DONT_FAIL                 = 0x4
RPC_C_RPCHTTP_USE_LOAD_BALANCE  = 0x8
RPC_C_TRY_ENFORCE_MAX_CALLS     = 0x10

from ...sdkddkver import *
_version = cpreproc.get_version()

if _version < WIN32_WINNT_VISTA:
    # RPC_POLICY EndpointFlags specific to the Falcon/RPC transport (deprecated for Vista)
    RPC_C_MQ_TEMPORARY                  = 0x0000
    RPC_C_MQ_PERMANENT                  = 0x0001
    RPC_C_MQ_CLEAR_ON_OPEN              = 0x0002
    RPC_C_MQ_USE_EXISTING_SECURITY      = 0x0004
    RPC_C_MQ_AUTHN_LEVEL_NONE           = 0x0000
    RPC_C_MQ_AUTHN_LEVEL_PKT_INTEGRITY  = 0x0008
    RPC_C_MQ_AUTHN_LEVEL_PKT_PRIVACY    = 0x0010

    # Falcon/Rpc options are deprecated from Vista
    RPC_C_MQ_EXPRESS                = 0  # Client: RPC_C_MQ_DELIVERY.
    RPC_C_MQ_RECOVERABLE            = 1

    RPC_C_MQ_JOURNAL_NONE           = 0 # Client: RPC_C_MQ_JOURNAL.
    RPC_C_MQ_JOURNAL_DEADLETTER     = 1
    RPC_C_MQ_JOURNAL_ALWAYS         = 2

    # Client: RpcBindingSetOption() values for the Falcon/RPC transport (some are deprecated from Vista)

    RPC_C_OPT_MQ_DELIVERY            = 1
    RPC_C_OPT_MQ_PRIORITY            = 2
    RPC_C_OPT_MQ_JOURNAL             = 3
    RPC_C_OPT_MQ_ACKNOWLEDGE         = 4
    RPC_C_OPT_MQ_AUTHN_SERVICE       = 5
    RPC_C_OPT_MQ_AUTHN_LEVEL         = 6
    RPC_C_OPT_MQ_TIME_TO_REACH_QUEUE = 7
    RPC_C_OPT_MQ_TIME_TO_BE_RECEIVED = 8

RPC_C_OPT_BINDING_NONCAUSAL      = 9
RPC_C_OPT_SECURITY_CALLBACK      = 10
RPC_C_OPT_UNIQUE_BINDING         = 11

if _version <= WIN32_WINNT_WIN2K:
    RPC_C_OPT_MAX_OPTIONS            = 12
elif _version <= WIN32_WINNT_WS03:
    RPC_C_OPT_CALL_TIMEOUT           = 12
    RPC_C_OPT_DONT_LINGER            = 13
    RPC_C_OPT_MAX_OPTIONS            = 14
else:
    RPC_C_OPT_TRANS_SEND_BUFFER_SIZE = 5
    RPC_C_OPT_CALL_TIMEOUT           = 12
    RPC_C_OPT_DONT_LINGER            = 13
    RPC_C_OPT_TRUST_PEER             = 14
    RPC_C_OPT_ASYNC_BLOCK            = 15
    RPC_C_OPT_OPTIMIZE_TIME          = 16
    RPC_C_OPT_MAX_OPTIONS            = 17

# flags for RpcServerInqAuthClientEx
#
RPC_C_FULL_CERT_CHAIN = 0x0001

class RPC_PROTSEQ_VECTORA(CStructure):
    _fields_ = [
        ('Count', UINT)
    ]
    
    Protseq: IArray[LPSTR]
    Count: int
    
flexible_array(RPC_PROTSEQ_VECTORA, 'Protseq', LPSTR)

class RPC_PROTSEQ_VECTORW(CStructure):
    _fields_ = [
        ('Count', UINT)
    ]
    
    Protseq: IArray[LPWSTR]
    Count: int
    
flexible_array(RPC_PROTSEQ_VECTORW, 'Protseq', LPWSTR)

RPC_PROTSEQ_VECTOR = unicode(RPC_PROTSEQ_VECTORA, RPC_PROTSEQ_VECTORW)

class RPC_POLICY(CStructure):
    _fields_ = [
        ('Length', UINT),
        ('EndpointFlags', ULONG),
        ('NICFlags', ULONG)
    ]
    
    EndpointFlags: int
    NICFlags: int
    Length: int
    
PRPC_POLICY = RPC_POLICY.PTR()

RPC_OBJECT_INQ_FN = WINAPI(VOID, UUID.PTR(), UUID.PTR(), PTR(RPC_STATUS))
RPC_IF_CALLBACK_FN = WINAPI(RPC_STATUS, RPC_IF_HANDLE, PVOID)
RPC_SECURITY_CALLBACK_FN = WINAPI(VOID, PVOID)

RPC_MGR_EPV = VOID

class RPC_STATS_VECTOR(CStructure):
    _fields_ = [
        ('Count', UINT),
    ]
    
    Stats: IArray[ULONG]
    Count: int
    
flexible_array(RPC_STATS_VECTOR, 'Stats', ULONG)

RPC_C_STATS_CALLS_IN = 0
RPC_C_STATS_CALLS_OUT = 1
RPC_C_STATS_PKTS_IN = 2
RPC_C_STATS_PKTS_OUT = 3

class RPC_IF_ID_VECTOR(CStructure):
    _fields_ = [
        ('Count', ULONG)
    ]
    
    IfId: IArray[RPC_IF_ID]
    Count: int
    
flexible_array(RPC_IF_ID_VECTOR, 'IfId', RPC_IF_ID.PTR())

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_BINDING_HANDLE))
def RpcBindingCopy(SourceBinding: WT_HANDLE, DestinationBinding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

@rpcrt_foreign(PTR(RPC_BINDING_HANDLE))
def RpcBindingFree(Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, ULONG_PTR)
def RpcBindingSetOption(hBinding: WT_HANDLE, option: int, optionValue: int) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, PULONG_PTR)
def RpcBindingInqOption(hBinding: WT_HANDLE, option: int, pOptionValue: IPointer[ULONG_PTR]) -> int: ...

@rpcrt_foreign(RPC_CSTR, PTR(RPC_BINDING_HANDLE))
def RpcBindingFromStringBindingA(StringBinding: WT_LPSTR, Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

@rpcrt_foreign(RPC_WSTR, PTR(RPC_BINDING_HANDLE))
def RpcBindingFromStringBindingW(StringBinding: WT_LPWSTR, Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

RpcBindingFromStringBinding = unicode(RpcBindingFromStringBindingW, RpcBindingFromStringBindingA)

@rpcrt_foreign(PVOID, PTR(RPC_BINDING_HANDLE))
def RpcSsGetContextBinding(ContextHandle: IVoidPtr, Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, UUID.PTR())
def RpcBindingInqObject(Binding: WT_HANDLE, ObjectUuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcBindingReset(Binding: WT_HANDLE) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, UUID.PTR())
def RpcBindingSetObject(Binding: WT_HANDLE, ObjectUuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(ULONG, PULONG)
def RpcMgmtInqDefaultProtectLevel(AuthnSvc: int, AuthnLevel: PULONG) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_CSTR))
def RpcBindingToStringBindingA(Binding: WT_HANDLE, StringBinding: IPointer[RPC_CSTR]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_WSTR))
def RpcBindingToStringBindingW(Binding: WT_HANDLE, StringBinding: IPointer[RPC_WSTR]) -> int: ...

RpcBindingToStringBinding = unicode(RpcBindingToStringBindingW, RpcBindingToStringBindingA)

@rpcrt_foreign(RPC_BINDING_VECTOR.DOUBLE_PTR())
def RpcBindingVectorFree(BindingVector: IDoublePtr[RPC_BINDING_VECTOR]) -> int: ...

@rpcrt_foreign(RPC_CSTR, RPC_CSTR, RPC_CSTR, RPC_CSTR, RPC_CSTR, PTR(RPC_CSTR))
def RpcStringBindingComposeA(
    ObjUuid: WT_LPSTR, 
    ProtSeq: WT_LPSTR,
    NetworkAddr: WT_LPSTR,
    Endpoint: WT_LPSTR,
    Options: WT_LPSTR,
    StringBinding: IPointer[RPC_CSTR]
    ) -> int: ...

@rpcrt_foreign(RPC_WSTR, RPC_WSTR, RPC_WSTR, RPC_WSTR, RPC_WSTR, PTR(RPC_WSTR))
def RpcStringBindingComposeW(
    ObjUuid: WT_LPWSTR, 
    ProtSeq: WT_LPWSTR,
    NetworkAddr: WT_LPWSTR,
    Endpoint: WT_LPWSTR,
    Options: WT_LPWSTR,
    StringBinding: IPointer[RPC_WSTR]
    ) -> int: ...

RpcStringBindingCompose = unicode(RpcStringBindingComposeW, RpcStringBindingComposeA)

@rpcrt_foreign(RPC_CSTR, PTR(RPC_CSTR), PTR(RPC_CSTR), PTR(RPC_CSTR), PTR(RPC_CSTR), PTR(RPC_CSTR))
def RpcStringBindingParseA(
    StringBinding: WT_LPSTR,
    ObjUuid: IPointer[RPC_CSTR],
    Protseq: IPointer[RPC_CSTR],
    NetworkAddr: IPointer[RPC_CSTR],
    Endpoint: IPointer[RPC_CSTR],
    NetworkOptions: IPointer[RPC_CSTR]
    ) -> int: ...

@rpcrt_foreign(RPC_WSTR, PTR(RPC_WSTR), PTR(RPC_WSTR), PTR(RPC_WSTR), PTR(RPC_WSTR), PTR(RPC_WSTR))
def RpcStringBindingParseW(
    StringBinding: WT_LPWSTR,
    ObjUuid: IPointer[RPC_WSTR],
    Protseq: IPointer[RPC_WSTR],
    NetworkAddr: IPointer[RPC_WSTR],
    Endpoint: IPointer[RPC_WSTR],
    NetworkOptions: IPointer[RPC_WSTR]
    ) -> int: ...

RpcStringBindingParse = unicode(RpcStringBindingParseW, RpcStringBindingParseA)

@rpcrt_foreign(PTR(RPC_CSTR))
def RpcStringFreeA(String: IPointer[RPC_CSTR]) -> int: ...

@rpcrt_foreign(PTR(RPC_WSTR))
def RpcStringFreeW(String: IPointer[RPC_WSTR]) -> int: ...

RpcStringFree = unicode(RpcStringFreeW, RpcStringFreeA)

@rpcrt_foreign(RPC_IF_HANDLE, RPC_IF_ID.PTR())
def RpcIfInqId(RpcIfHandle: WT_HANDLE, RpcIfId: IPointer[RPC_IF_ID]) -> int: ...

@rpcrt_foreign(RPC_CSTR)
def RpcNetworkIsProtseqValidA(Protseq: WT_LPSTR) -> int: ...

@rpcrt_foreign(RPC_WSTR)
def RpcNetworkIsProtseqValidW(Protseq: WT_LPWSTR) -> int: ...

RpcNetworkIsProtseqValid = unicode(RpcNetworkIsProtseqValidW, RpcNetworkIsProtseqValidA)

@rpcrt_foreign(RPC_BINDING_HANDLE, PUINT)
def RpcMgmtInqComTimeout(Binding: WT_HANDLE, Timeout: PUINT) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, UINT)
def RpcMgmtSetComTimeout(Binding: WT_HANDLE, Timeout: int) -> int: ...

@rpcrt_foreign(LONG)
def RpcMgmtSetCancelTimeout(Timeout: int) -> int: ...

@rpcrt_foreign(RPC_PROTSEQ_VECTORA.DOUBLE_PTR())
def RpcNetworkInqProtseqA(ProtseqVector: IDoublePtr[RPC_PROTSEQ_VECTORA]) -> int: ...

@rpcrt_foreign(RPC_PROTSEQ_VECTORW.DOUBLE_PTR())
def RpcNetworkInqProtseqW(ProtseqVector: IDoublePtr[RPC_PROTSEQ_VECTORW]) -> int: ...

RpcNetworkInqProtseq = unicode(RpcNetworkInqProtseqW, RpcNetworkInqProtseqA)

@rpcrt_foreign(UUID.PTR(), UUID.PTR())
def RpcObjectInqType(ObjUuid: IPointer[UUID],
                     TypeUuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(PTR(RPC_OBJECT_INQ_FN))
def RpcObjectSetInqFn(InquiryFn: IPointer[FARPROC]) -> int: ...

@rpcrt_foreign(UUID.PTR(), UUID.PTR())
def RpcObjectSetType(ObjUuid: IPointer[UUID],
                     TypeUuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(RPC_PROTSEQ_VECTORA.DOUBLE_PTR())
def RpcProtseqVectorFreeA(ProtseqVector: IDoublePtr[RPC_PROTSEQ_VECTORA]) -> int: ...

@rpcrt_foreign(RPC_PROTSEQ_VECTORW.DOUBLE_PTR())
def RpcProtseqVectorFreeW(ProtseqVector: IDoublePtr[RPC_PROTSEQ_VECTORW]) -> int: ...

RpcProtseqVectorFree = unicode(RpcProtseqVectorFreeW, RpcProtseqVectorFreeA)

@rpcrt_foreign(DOUBLE_PTR(RPC_BINDING_VECTOR))
def RpcServerInqBindings(BindingVector: IDoublePtr[RPC_BINDING_VECTOR]) -> int: ...

@rpcrt_foreign(PVOID, RPC_BINDING_VECTOR.DOUBLE_PTR())
def RpcServerInqBindingsEx(SecurityDescriptor: IVoidPtr, 
                           BindingVector: IDoublePtr[RPC_BINDING_VECTOR]) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), DOUBLE_PTR(RPC_MGR_EPV))
def RpcServerInqIf(
    IfSpec: WT_HANDLE, 
    MgrTypeUuid: IPointer[UUID],
    MgrEpv: IPointer[PVOID]) -> int: ...

@rpcrt_foreign(UINT, UINT, UINT)
def RpcServerListen(
    MinimumCallThreads: int,
    MaxCalls: int,
    DontWait: int) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), PTR(RPC_MGR_EPV))
def RpcServerRegisterIf(
    IfSpec: WT_HANDLE, 
    MgrTypeUuid: IPointer[UUID],
    MgrEpv: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), PTR(RPC_MGR_EPV),
               UINT, UINT, PTR(RPC_IF_CALLBACK_FN))
def RpcServerRegisterIfEx(
    IfSpec: WT_HANDLE,
    MgrTypeUuid: IPointer[UUID],
    MgrEpv: IVoidPtr,
    Flags: int,
    MaxCalls: int,
    IfCallback: IPointer[FARPROC]) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), PTR(RPC_MGR_EPV),
               UINT, UINT, UINT, PTR(RPC_IF_CALLBACK_FN))
def RpcServerRegisterIf2(
    IfSpec: WT_HANDLE,
    MgrTypeUuid: IPointer[UUID],
    MgrEpv: IVoidPtr,
    Flags: int,
    MaxCalls: int,
    MaxRpcSize: int,
    IfCallbackFn: IPointer[FARPROC]) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), PTR(RPC_MGR_EPV),
               UINT, UINT, UINT, PTR(RPC_IF_CALLBACK_FN), PVOID)
def RpcServerRegisterIf3(
    IfSpec: WT_HANDLE,
    MgrTypeUuid: IPointer[UUID],
    MgrEpv: IVoidPtr,
    Flags: int,
    MaxCalls: int,
    MaxRpcSize: int,
    IfCallback: IPointer[FARPROC],
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), UINT)
def RpcServerUnregisterIf(
    IfSpec: WT_HANDLE, 
    MgrTypeUuid: IPointer[UUID],
    WaitForCallsToComplete: int) -> int: ...

@rpcrt_foreign(RPC_IF_HANDLE, UUID.PTR(), INT)
def RpcServerUnregisterIfEx(
    IfSpec: WT_HANDLE, 
    MgrTypeUuid: IPointer[UUID],
    RundownContextHandles: int) -> int: ...

@rpcrt_foreign(UINT, PVOID)
def RpcServerUseAllProtseqs(
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(UINT, PVOID, PRPC_POLICY)
def RpcServerUseAllProtseqsEx(
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

@rpcrt_foreign(UINT, RPC_IF_HANDLE, PVOID)
def RpcServerUseAllProtseqsIf(
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(UINT, RPC_IF_HANDLE, PVOID, PRPC_POLICY)
def RpcServerUseAllProtseqsIfEx(
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

@rpcrt_foreign(RPC_CSTR, UINT, PVOID)
def RpcServerUseProtseqA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_CSTR, UINT, PVOID, PRPC_POLICY)
def RpcServerUseProtseqExA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, PVOID)
def RpcServerUseProtseqW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, PVOID, PRPC_POLICY)
def RpcServerUseProtseqExW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

RpcServerUseProtseq = unicode(RpcServerUseProtseqW, RpcServerUseProtseqA)
RpcServerUseProtseqEx = unicode(RpcServerUseProtseqExW, RpcServerUseProtseqExA)

@rpcrt_foreign(RPC_CSTR, UINT, RPC_CSTR, PVOID)
def RpcServerUseProtseqEpA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    Endpoint: WT_LPSTR,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_CSTR, UINT, RPC_CSTR, PVOID, PRPC_POLICY)
def RpcServerUseProtseqEpExA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    Endpoint: WT_LPSTR,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, RPC_WSTR, PVOID)
def RpcServerUseProtseqEpW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    Endpoint: WT_LPWSTR,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, RPC_WSTR, PVOID, PRPC_POLICY)
def RpcServerUseProtseqEpExW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    Endpoint: WT_LPWSTR,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

RpcServerUseProtseqEp = unicode(RpcServerUseProtseqEpW, RpcServerUseProtseqEpA)
RpcServerUseProtseqEpEx = unicode(RpcServerUseProtseqEpExW, RpcServerUseProtseqEpExA)

@rpcrt_foreign(RPC_CSTR, UINT, RPC_IF_HANDLE, PVOID)
def RpcServerUseProtseqIfA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_CSTR, UINT, RPC_IF_HANDLE, PVOID, PRPC_POLICY)
def RpcServerUseProtseqIfExA(
    Protseq: WT_LPSTR, 
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, RPC_IF_HANDLE, PVOID)
def RpcServerUseProtseqIfW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_WSTR, UINT, RPC_IF_HANDLE, PVOID, PRPC_POLICY)
def RpcServerUseProtseqIfExW(
    Protseq: WT_LPWSTR, 
    MaxCalls: int,
    IfSpec: WT_HANDLE,
    SecurityDescriptor: IVoidPtr,
    Policy: IPointer[RPC_POLICY]) -> int: ...

RpcServerUseProtseqIf = unicode(RpcServerUseProtseqIfW, RpcServerUseProtseqIfA)
RpcServerUseProtseqIfEx = unicode(RpcServerUseProtseqIfExW, RpcServerUseProtseqIfExA)

@rpcrt4.foreign(VOID)
def RpcServerYield(): ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_STATS_VECTOR.DOUBLE_PTR())
def RpcMgmtInqStats(
    Binding: WT_HANDLE,
    Statistics: IDoublePtr[RPC_STATS_VECTOR]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcMgmtIsServerListening(Binding: WT_HANDLE) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcMgmtStopServerListening(Binding: WT_HANDLE) -> int: ...

@rpcrt_foreign()
def RpcMgmtWaitServerListen() -> int: ...

@rpcrt_foreign(ULONG)
def RpcMgmtSetServerStackSize(ThreadStackSize: int) -> int: ...

@rpcrt4.foreign(VOID)
def RpcSsDontSerializeContext() -> int: ...

@rpcrt_foreign()
def RpcMgmtEnableIdleCleanup() -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_IF_ID_VECTOR.DOUBLE_PTR())
def RpcMgmtInqIfIds(
    Binding: WT_HANDLE,
    IfIdVector: IDoublePtr[RPC_IF_ID_VECTOR]) -> int: ...

@rpcrt_foreign(RPC_IF_ID_VECTOR.DOUBLE_PTR())
def RpcIfIdVectorFree(IfIdVector: IDoublePtr[RPC_IF_ID_VECTOR]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, PTR(RPC_CSTR))
def RpcMgmtInqServerPrincNameA(
    Binding: WT_HANDLE,
    AuthnSvc: int,
    ServerPrincName: IPointer[RPC_CSTR]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, PTR(RPC_WSTR))
def RpcMgmtInqServerPrincNameW(
    Binding: WT_HANDLE,
    AuthnSvc: int,
    ServerPrincName: IPointer[RPC_WSTR]) -> int: ...

RpcMgmtInqServerPrincName = unicode(RpcMgmtInqServerPrincNameW, RpcMgmtInqServerPrincNameA)

@rpcrt_foreign(ULONG, PTR(RPC_CSTR))
def RpcMgmtInqDefaultPrincNameA(
    AuthnSvc: int,
    PrincName: WT_LPSTR) -> int: ...

@rpcrt_foreign(ULONG, PTR(RPC_WSTR))
def RpcMgmtInqDefaultPrincNameW(
    AuthnSvc: int,
    PrincName: WT_LPWSTR) -> int: ...

RpcMgmtInqDefaultPrincName = unicode(RpcMgmtInqDefaultPrincNameW, RpcMgmtInqDefaultPrincNameA)

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_IF_HANDLE)
def RpcEpResolveBinding(
    Binding: WT_HANDLE,
    IfSpec: WT_HANDLE) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, PTR(RPC_CSTR))
def RpcNsBindingInqEntryNameA(
    Binding: WT_HANDLE,
    EntryNameSyntax: int,
    EntryName: IPointer[RPC_CSTR]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, ULONG, PTR(RPC_WSTR))
def RpcNsBindingInqEntryNameW(
    Binding: WT_HANDLE,
    EntryNameSyntax: int,
    EntryName: IPointer[RPC_WSTR]) -> int: ...

RpcNsBindingInqEntryName = unicode(RpcNsBindingInqEntryNameW, RpcNsBindingInqEntryNameA)

RPC_AUTH_IDENTITY_HANDLE = PVOID
RPC_AUTHZ_HANDLE = PVOID

RPC_C_AUTHN_LEVEL_DEFAULT       = 0
RPC_C_AUTHN_LEVEL_NONE          = 1
RPC_C_AUTHN_LEVEL_CONNECT       = 2
RPC_C_AUTHN_LEVEL_CALL          = 3
RPC_C_AUTHN_LEVEL_PKT           = 4
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY = 5
RPC_C_AUTHN_LEVEL_PKT_PRIVACY   = 6

RPC_C_IMP_LEVEL_DEFAULT      = 0
RPC_C_IMP_LEVEL_ANONYMOUS    = 1
RPC_C_IMP_LEVEL_IDENTIFY     = 2
RPC_C_IMP_LEVEL_IMPERSONATE  = 3
RPC_C_IMP_LEVEL_DELEGATE     = 4

RPC_C_QOS_IDENTITY_STATIC    = 0
RPC_C_QOS_IDENTITY_DYNAMIC   = 1

RPC_C_QOS_CAPABILITIES_DEFAULT                        = 0x0
RPC_C_QOS_CAPABILITIES_MUTUAL_AUTH                    = 0x1
RPC_C_QOS_CAPABILITIES_MAKE_FULLSIC                   = 0x2
RPC_C_QOS_CAPABILITIES_ANY_AUTHORITY                  = 0x4

if _version >= WIN32_WINNT_WS03:
    RPC_C_QOS_CAPABILITIES_IGNORE_DELEGATE_FAILURE        = 0x8
    RPC_C_QOS_CAPABILITIES_LOCAL_MA_HINT                  = 0x10

if _version >= WIN32_WINNT_VISTA:
    RPC_C_QOS_CAPABILITIES_SCHANNEL_FULL_AUTH_IDENTITY   = 0x20

RPC_C_PROTECT_LEVEL_DEFAULT       = (RPC_C_AUTHN_LEVEL_DEFAULT)
RPC_C_PROTECT_LEVEL_NONE          = (RPC_C_AUTHN_LEVEL_NONE)
RPC_C_PROTECT_LEVEL_CONNECT       = (RPC_C_AUTHN_LEVEL_CONNECT)
RPC_C_PROTECT_LEVEL_CALL          = (RPC_C_AUTHN_LEVEL_CALL)
RPC_C_PROTECT_LEVEL_PKT           = (RPC_C_AUTHN_LEVEL_PKT)
RPC_C_PROTECT_LEVEL_PKT_INTEGRITY = (RPC_C_AUTHN_LEVEL_PKT_INTEGRITY)
RPC_C_PROTECT_LEVEL_PKT_PRIVACY   = (RPC_C_AUTHN_LEVEL_PKT_PRIVACY)

RPC_C_AUTHN_NONE          = 0
RPC_C_AUTHN_DCE_PRIVATE   = 1
RPC_C_AUTHN_DCE_PUBLIC    = 2
RPC_C_AUTHN_DEC_PUBLIC    = 4
RPC_C_AUTHN_GSS_NEGOTIATE = 9
RPC_C_AUTHN_WINNT        = 10
RPC_C_AUTHN_GSS_SCHANNEL = 14
RPC_C_AUTHN_GSS_KERBEROS = 16
RPC_C_AUTHN_DPA          = 17
RPC_C_AUTHN_MSN          = 18

if _version >= WIN32_WINNT_WINXP:
    RPC_C_AUTHN_DIGEST       = 21
    
if _version >= WIN32_WINNT_WIN7:
    RPC_C_AUTHN_KERNEL         = 20

RPC_C_AUTHN_NEGO_EXTENDER = 30
RPC_C_AUTHN_PKU2U         = 31

RPC_C_AUTHN_LIVE_SSP      = 32
RPC_C_AUTHN_LIVEXP_SSP    = 35
RPC_C_AUTHN_CLOUD_AP      = 36
RPC_C_AUTHN_MSONLINE      = 82

RPC_C_AUTHN_MQ          = 100
RPC_C_AUTHN_DEFAULT     = 0xFFFFFFFF

RPC_C_NO_CREDENTIALS = RPC_AUTH_IDENTITY_HANDLE(MAXUINT_PTR)

RPC_C_SECURITY_QOS_VERSION      = 1
RPC_C_SECURITY_QOS_VERSION_1    = 1

class RPC_SECURITY_QOS(CStructure):
    _fields_ = [
        ('Version', ULONG),
        ('Capabilities', ULONG),
        ('IdentityTracking', ULONG),
        ('ImpersonationType', ULONG)
    ]
    
    ImpersonationType: int
    IdentityTracking: int
    Capabilities: int
    Version: int
    
SEC_WINNT_AUTH_IDENTITY_ANSI = 0x1
SEC_WINNT_AUTH_IDENTITY_UNICODE = 0x2

class SEC_WINNT_AUTH_IDENTITY_W(CStructure):
    _fields_ = [
        ('User', LPWSTR),
        ('UserLength', ULONG),
        ('Domain', LPWSTR),
        ('DomainLength', ULONG),
        ('Password', LPWSTR),
        ('PasswordLength', ULONG),
        ('Flags', ULONG)
    ]
    
    PasswordLength: int
    DomainLength: int
    UserLength: int
    
    Password: LPWSTR
    Domain: LPWSTR
    User: LPWSTR
    
    Flags: int
    
PSEC_WINNT_AUTH_IDENTITY_W = SEC_WINNT_AUTH_IDENTITY_W.PTR()
    
class SEC_WINNT_AUTH_IDENTITY_A(CStructure):
    _fields_ = [
        ('User', LPSTR),
        ('UserLength', ULONG),
        ('Domain', LPSTR),
        ('DomainLength', ULONG),
        ('Password', LPSTR),
        ('PasswordLength', ULONG),
        ('Flags', ULONG)
    ]
    
    PasswordLength: int
    DomainLength: int
    UserLength: int
    
    Password: LPSTR
    Domain: LPSTR
    User: LPSTR
    
    Flags: int
    
PSEC_WINNT_AUTH_IDENTITY_A = SEC_WINNT_AUTH_IDENTITY_A.PTR()

SEC_WINNT_AUTH_IDENTITY = unicode(SEC_WINNT_AUTH_IDENTITY_W, SEC_WINNT_AUTH_IDENTITY_A)
PSEC_WINNT_AUTH_IDENTITY = unicode(PSEC_WINNT_AUTH_IDENTITY_W, PSEC_WINNT_AUTH_IDENTITY_A)

if _version >= WIN32_WINNT_WINXP:
    RPC_C_SECURITY_QOS_VERSION_2 = 2

    RPC_C_AUTHN_INFO_TYPE_HTTP                  = 1

    RPC_C_HTTP_AUTHN_TARGET_SERVER              = 1
    
    if _version >= WIN32_WINNT_VISTA:
        RPC_C_HTTP_AUTHN_TARGET_PROXY               = 2

    RPC_C_HTTP_AUTHN_SCHEME_BASIC      = 0x00000001
    RPC_C_HTTP_AUTHN_SCHEME_NTLM       = 0x00000002
    RPC_C_HTTP_AUTHN_SCHEME_PASSPORT   = 0x00000004
    RPC_C_HTTP_AUTHN_SCHEME_DIGEST     = 0x00000008
    RPC_C_HTTP_AUTHN_SCHEME_NEGOTIATE  = 0x00000010
    
    if _version >= WIN32_WINNT_WS03:
        RPC_C_HTTP_AUTHN_SCHEME_CERT       = 0x00010000
    
    # 0x00020000 & 0x00040000 are reserved

    RPC_C_HTTP_FLAG_USE_SSL                     = 1
    RPC_C_HTTP_FLAG_USE_FIRST_AUTH_SCHEME       = 2

    if _version >= WIN32_WINNT_WS03:
        RPC_C_HTTP_FLAG_IGNORE_CERT_CN_INVALID      = 8
        
    if _version >= WIN32_WINNT_VISTA:
        RPC_C_HTTP_FLAG_ENABLE_CERT_REVOCATION_CHECK = 16

    class RPC_HTTP_TRANSPORT_CREDENTIALS_W(CStructure):
        _fields_ = [
            ('TransportCredentials', SEC_WINNT_AUTH_IDENTITY_W)
            ('Flags', ULONG),
            ('AuthenticationTarget', ULONG),
            ('NumberOfAuthnSchemes', ULONG),
            ('AuthnSchemes', PULONG),
            ('ServerCertificateSubject', LPWSTR)
        ]
        
        TransportCredentials: SEC_WINNT_AUTH_IDENTITY_W
        ServerCertificateSubject: LPWSTR
        AuthenticationTarget: int
        NumberOfAuthnSchemes: int
        AuthnSchemes: PULONG
        Flags: int
        
    PRPC_HTTP_TRANSPORT_CREDENTIALS_W = RPC_HTTP_TRANSPORT_CREDENTIALS_W.PTR()
    
    class RPC_HTTP_TRANSPORT_CREDENTIALS_A(CStructure):
        _fields_ = [
            ('TransportCredentials', SEC_WINNT_AUTH_IDENTITY_A)
            ('Flags', ULONG),
            ('AuthenticationTarget', ULONG),
            ('NumberOfAuthnSchemes', ULONG),
            ('AuthnSchemes', PULONG),
            ('ServerCertificateSubject', LPSTR)
        ]
        
        TransportCredentials: SEC_WINNT_AUTH_IDENTITY_A
        ServerCertificateSubject: LPSTR
        AuthenticationTarget: int
        NumberOfAuthnSchemes: int
        AuthnSchemes: PULONG
        Flags: int
        
    PRPC_HTTP_TRANSPORT_CREDENTIALS_A = RPC_HTTP_TRANSPORT_CREDENTIALS_A.PTR()
    
    if _version >= WIN32_WINNT_VISTA:
        class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W(RPC_HTTP_TRANSPORT_CREDENTIALS_W):
            _fields_ = [
                ('ProxyCredentials', SEC_WINNT_AUTH_IDENTITY_W),
                ('NumberOfProxyAuthnSchemes', ULONG),
                ('ProxyAuthnSchemes', PULONG)
            ]
            
            ProxyCredentials: SEC_WINNT_AUTH_IDENTITY_W
            NumberOfProxyAuthnSchemes: int
            ProxyAuthnSchemes: PULONG
            
        PRPC_HTTP_TRANSPORT_CREDENTIALS_V2_W = RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W.PTR()
        
        class RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A(RPC_HTTP_TRANSPORT_CREDENTIALS_A):
            _fields_ = [
                ('ProxyCredentials', SEC_WINNT_AUTH_IDENTITY_A),
                ('NumberOfProxyAuthnSchemes', ULONG),
                ('ProxyAuthnSchemes', PULONG)
            ]
            
            ProxyCredentials: SEC_WINNT_AUTH_IDENTITY_A
            NumberOfProxyAuthnSchemes: int
            ProxyAuthnSchemes: PULONG
            
        PRPC_HTTP_TRANSPORT_CREDENTIALS_V2_A = RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A.PTR()
        RPC_HTTP_TRANSPORT_CREDENTIALS_V2 = unicode(RPC_HTTP_TRANSPORT_CREDENTIALS_V2_W, RPC_HTTP_TRANSPORT_CREDENTIALS_V2_A)

    if _version >= WIN32_WINNT_WIN7:
        class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W(CStructure):
            _fields_ = [
                ('TransportCredentials', RPC_AUTH_IDENTITY_HANDLE),
                ('Flags', ULONG),
                ('AuthenticationTarget', ULONG),
                ('NumberOfAuthnSchemes', ULONG),
                ('AuthnSchemes', PULONG),
                ('ServerCertificateSubject', LPWSTR),
                ('ProxyCredentials', RPC_AUTH_IDENTITY_HANDLE),
                ('NumberOfProxyAuthnSchemes', ULONG),
                ('ProxyAuthnSchemes', PULONG)
            ]
            
            TransportCredentials: RPC_AUTH_IDENTITY_HANDLE
            ProxyCredentials: RPC_AUTH_IDENTITY_HANDLE
            
            NumberOfProxyAuthnSchemes: int
            NumberOfAuthnSchemes: int
            
            ProxyAuthnSchemes: PULONG
            AuthnSchemes: PULONG
            
            ServerCertificateSubject: LPWSTR
            AuthenticationTarget: int
            Flags: int
            
        PRPC_HTTP_TRANSPORT_CREDENTIALS_V3_W = RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W.PTR()
        
        class RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A(CStructure):
            _fields_ = [
                ('TransportCredentials', RPC_AUTH_IDENTITY_HANDLE),
                ('Flags', ULONG),
                ('AuthenticationTarget', ULONG),
                ('NumberOfAuthnSchemes', ULONG),
                ('AuthnSchemes', PULONG),
                ('ServerCertificateSubject', LPSTR),
                ('ProxyCredentials', RPC_AUTH_IDENTITY_HANDLE),
                ('NumberOfProxyAuthnSchemes', ULONG),
                ('ProxyAuthnSchemes', PULONG)
            ]
            
            TransportCredentials: RPC_AUTH_IDENTITY_HANDLE
            ProxyCredentials: RPC_AUTH_IDENTITY_HANDLE
            
            NumberOfProxyAuthnSchemes: int
            NumberOfAuthnSchemes: int
            
            ProxyAuthnSchemes: PULONG
            AuthnSchemes: PULONG
            
            ServerCertificateSubject: LPSTR
            AuthenticationTarget: int
            Flags: int
            
        PRPC_HTTP_TRANSPORT_CREDENTIALS_V3_A = RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A.PTR()
        RPC_HTTP_TRANSPORT_CREDENTIALS_V3 = unicode(RPC_HTTP_TRANSPORT_CREDENTIALS_V3_W, RPC_HTTP_TRANSPORT_CREDENTIALS_V3_A)
        
    class RPC_SECURITY_QOS_V2_W(CStructure):
        class U(CUnion):
            _fields_ = [
                ('HttpCredentials', RPC_HTTP_TRANSPORT_CREDENTIALS_W)
            ]
            
            HttpCredentials: RPC_HTTP_TRANSPORT_CREDENTIALS_W
            
        _fields_ = [
            ('Version', ULONG),
            ('Capabilities', ULONG),
            ('IdentityTracking', ULONG),
            ('ImpersonationType', ULONG),
            ('AdditionalSecurityInfoType', ULONG),
            ('u', U)
        ]
        
        HttpCredentials: RPC_HTTP_TRANSPORT_CREDENTIALS_W
        AdditionalSecurityInfoType: int
        ImpersonationType: int
        IdentityTracking: int
        Capabilities: int
        Version: int
        u: U

    PRPC_SECURITY_QOS_V2_W = RPC_SECURITY_QOS_V2_W.PTR()
    
    class RPC_SECURITY_QOS_V2_A(CStructure):
        class U(CUnion):
            _fields_ = [
                ('HttpCredentials', RPC_HTTP_TRANSPORT_CREDENTIALS_A)
            ]
            
            HttpCredentials: RPC_HTTP_TRANSPORT_CREDENTIALS_A
            
        _fields_ = [
            ('Version', ULONG),
            ('Capabilities', ULONG),
            ('IdentityTracking', ULONG),
            ('ImpersonationType', ULONG),
            ('AdditionalSecurityInfoType', ULONG),
            ('u', U)
        ]
        
        AdditionalSecurityInfoType: int
        ImpersonationType: int
        IdentityTracking: int
        Capabilities: int
        Version: int
        u: U

    PRPC_SECURITY_QOS_V2_A = RPC_SECURITY_QOS_V2_A.PTR()
    
    if _version >= WIN32_WINNT_WS03:
        RPC_C_SECURITY_QOS_VERSION_3 = 3
        
        class RPC_SECURITY_QOS_V3_W(RPC_SECURITY_QOS_V2_W):
            _fields_ = [
                ('Sid', PVOID)
            ]
            
            Sid: IVoidPtr
            
        PRPC_SECURITY_QOS_V3_W = RPC_SECURITY_QOS_V3_W.PTR()
        
        class RPC_SECURITY_QOS_V3_A(RPC_SECURITY_QOS_V2_A):
            _fields_ = [
                ('Sid', PVOID)
            ]
            
            Sid: IVoidPtr
            
        PRPC_SECURITY_QOS_V3_A = RPC_SECURITY_QOS_V3_A.PTR()
        RPC_SECURITY_QOS_V3 = unicode(RPC_SECURITY_QOS_V3_W, RPC_SECURITY_QOS_V3_A)

    if _version >= WIN32_WINNT_VISTA:
        RPC_C_SECURITY_QOS_VERSION_4 = 4

        class RPC_SECURITY_QOS_V4_W(RPC_SECURITY_QOS_V3_W):
            _fields_ = [
                ('EffectiveOnly', UINT)
            ]
            
            EffectiveOnly: int
            
        PRPC_SECURITY_QOS_V4_W = RPC_SECURITY_QOS_V4_W.PTR()
        
        class RPC_SECURITY_QOS_V4_A(RPC_SECURITY_QOS_V3_A):
            _fields_ = [
                ('EffectiveOnly', UINT)
            ]
            
            EffectiveOnly: int
            
        PRPC_SECURITY_QOS_V4_A = RPC_SECURITY_QOS_V4_A.PTR()
        RPC_SECURITY_QOS_V4 = unicode(RPC_SECURITY_QOS_V4_W, RPC_SECURITY_QOS_V4_A)

    if _version >= WIN32_WINNT_WIN8:
        RPC_C_SECURITY_QOS_VERSION_5 = 5
        
        class RPC_SECURITY_QOS_V5_W(RPC_SECURITY_QOS_V4_W):
            _fields_ = [
                ('ServerSecurityDescriptor', PVOID)
            ]
            
            ServerSecurityDescriptor: IVoidPtr
            
        PRPC_SECURITY_QOS_V5_W = RPC_SECURITY_QOS_V5_W.PTR()
        
        class RPC_SECURITY_QOS_V5_A(RPC_SECURITY_QOS_V4_A):
            _fields_ = [
                ('ServerSecurityDescriptor', PVOID)
            ]
            
            ServerSecurityDescriptor: IVoidPtr
            
        PRPC_SECURITY_QOS_V5_A = RPC_SECURITY_QOS_V5_A.PTR()
        RPC_SECURITY_QOS_V5 = unicode(RPC_SECURITY_QOS_V5_W, RPC_SECURITY_QOS_V5_A)
        
    RPC_HTTP_TRANSPORT_CREDENTIALS = unicode(RPC_HTTP_TRANSPORT_CREDENTIALS_W, RPC_HTTP_TRANSPORT_CREDENTIALS_A)
    RPC_SECURITY_QOS_V2 = unicode(RPC_SECURITY_QOS_V2_W, RPC_SECURITY_QOS_V2_A)

    RPC_PROTSEQ_TCP                             = (0x1)
    RPC_PROTSEQ_NMP                             = (0x2)
    RPC_PROTSEQ_LRPC                            = (0x3)
    RPC_PROTSEQ_HTTP                            = (0x4)

    RPC_BHT_OBJECT_UUID_VALID                   = (0x1)

    RPC_BHO_NONCAUSAL                           = (0x1)
    RPC_BHO_DONTLINGER                          = (0x2)
    RPC_BHO_EXCLUSIVE_AND_GUARANTEED            = (0x4)

    class RPC_BINDING_HANDLE_TEMPLATE_V1_W(CStructure):
        class U1(CUnion):
            _fields_ = [
                ('Reserved', LPWSTR)
            ]
            
            Reserved: LPWSTR
        
        _fields_ = [
            ('Version', ULONG),
            ('Flags', ULONG),
            ('ProtocolSequence', ULONG),
            ('NetworkAddress', LPWSTR),
            ('StringEndpoint', LPWSTR),
            ('u1', U1),
            ('ObjectUuid', UUID)
        ]
        
        NetworkAddress: LPWSTR
        StringEndpoint: LPWSTR
        
        ProtocolSequence: int
        ObjectUuid: UUID
        Version: int
        Flags: int
        u1: U1
        
    PRPC_BINDING_HANDLE_TEMPLATE_V1_W = RPC_BINDING_HANDLE_TEMPLATE_V1_W.PTR()

    class RPC_BINDING_HANDLE_TEMPLATE_V1_A(CStructure):
        class U1(CUnion):
            _fields_ = [
                ('Reserved', LPSTR)
            ]
            
            Reserved: LPSTR
        
        _fields_ = [
            ('Version', ULONG),
            ('Flags', ULONG),
            ('ProtocolSequence', ULONG),
            ('NetworkAddress', LPSTR),
            ('StringEndpoint', LPSTR),
            ('u1', U1),
            ('ObjectUuid', UUID)
        ]
        
        NetworkAddress: LPSTR
        StringEndpoint: LPSTR
        
        ProtocolSequence: int
        ObjectUuid: UUID
        Version: int
        Flags: int
        u1: U1
        
    PRPC_BINDING_HANDLE_TEMPLATE_V1_A = RPC_BINDING_HANDLE_TEMPLATE_V1_A.PTR()

    class RPC_BINDING_HANDLE_SECURITY_V1_W(CStructure):
        _fields_ = [
            ('Version', ULONG),
            ('ServerPrincName', LPWSTR),
            ('AuthnLevel', ULONG),
            ('AuthnSvc', ULONG),
            ('AuthIdentity', PSEC_WINNT_AUTH_IDENTITY_W),
            ('SecurityQos', RPC_SECURITY_QOS.PTR())
        ]
        
        AuthIdentity: IPointer[SEC_WINNT_AUTH_IDENTITY_W]
        SecurityQos: IPointer[RPC_SECURITY_QOS]
        ServerPrincName: LPWSTR
        AuthnLevel: int
        AuthnSvc: int
        Version: int
        
    PRPC_BINDING_HANDLE_SECURITY_V1_W = RPC_BINDING_HANDLE_SECURITY_V1_W.PTR()

    class RPC_BINDING_HANDLE_SECURITY_V1_A(CStructure):
        _fields_ = [
            ('Version', ULONG),
            ('ServerPrincName', LPSTR),
            ('AuthnLevel', ULONG),
            ('AuthnSvc', ULONG),
            ('AuthIdentity', PSEC_WINNT_AUTH_IDENTITY_A),
            ('SecurityQos', RPC_SECURITY_QOS.PTR())
        ]
        
        AuthIdentity: IPointer[SEC_WINNT_AUTH_IDENTITY_A]
        SecurityQos: IPointer[RPC_SECURITY_QOS]
        ServerPrincName: LPSTR
        AuthnLevel: int
        AuthnSvc: int
        Version: int
        
    PRPC_BINDING_HANDLE_SECURITY_V1_A = RPC_BINDING_HANDLE_SECURITY_V1_A.PTR()

    class RPC_BINDING_HANDLE_OPTIONS_V1(CStructure):
        _fields_ = [
            ('Version', ULONG),
            ('Flags', ULONG),
            ('ComTimeout', ULONG),
            ('CallTimeout', ULONG)
        ]
        
        CallTimeout: int
        ComTimeout: int
        Version: int
        Flags: int
        
    PRPC_BINDING_HANDLE_OPTIONS_V1 = RPC_BINDING_HANDLE_OPTIONS_V1.PTR()

    @rpcrt_foreign(PRPC_BINDING_HANDLE_TEMPLATE_V1_A,
                PRPC_BINDING_HANDLE_SECURITY_V1_A,
                PRPC_BINDING_HANDLE_OPTIONS_V1,
                PTR(RPC_BINDING_HANDLE))
    def RpcBindingCreateA(
        Template: IPointer[RPC_BINDING_HANDLE_TEMPLATE_V1_A],
        Security: IPointer[RPC_BINDING_HANDLE_SECURITY_V1_A],
        Options: IPointer[RPC_BINDING_HANDLE_OPTIONS_V1],
        Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

    @rpcrt_foreign(PRPC_BINDING_HANDLE_TEMPLATE_V1_W,
                PRPC_BINDING_HANDLE_SECURITY_V1_W,
                PRPC_BINDING_HANDLE_OPTIONS_V1,
                PTR(RPC_BINDING_HANDLE))
    def RpcBindingCreateW(
        Template: IPointer[RPC_BINDING_HANDLE_TEMPLATE_V1_W],
        Security: IPointer[RPC_BINDING_HANDLE_SECURITY_V1_W],
        Options: IPointer[RPC_BINDING_HANDLE_OPTIONS_V1],
        Binding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

    RpcBindingCreate = unicode(RpcBindingCreateW, RpcBindingCreateA)

    @rpcrt_foreign(RPC_BINDING_HANDLE, PVOID)
    def RpcBindingGetTrainingContextHandle(
        Binding: WT_HANDLE,
        ContextHandle: IPointer[PVOID]) -> int: ...

    @rpcrt_foreign(PTR(RPC_BINDING_HANDLE))
    def RpcServerInqBindingHandle(Binding: WT_HANDLE) -> int:  ...

    if _version >= WIN32_WINNT_WS03:
        RPCHTTP_RS_REDIRECT = 1
        RPCHTTP_RS_ACCESS_1 = 2
        RPCHTTP_RS_SESSION = 3
        RPCHTTP_RS_ACCESS_2 = 4
        RPCHTTP_RS_INTERFACE = 5
        RPC_HTTP_REDIRECTOR_STAGE = INT
        
        # (
        # RedirectorStage: RPC_HTTP_REDIRECTOR_STAGE
        # ServerName: WT_LPWSTR, ServerPort: WT_LPWSTR
        # RemoteUser: WT_LPWSTR, AuthType: WT_LPWSTR
        # ResourceUuid: IVoidPtr, SessionId: IVoidPtr
        # Interface: IVoidPtr, Reserved: IVoidPtr, Flags: int
        # NewServerName: WT_LPWSTR, NewServerPort: WT_LPWSTR) -> int: ...
        RPC_NEW_HTTP_PROXY_CHANNEL = WINAPI(RPC_STATUS, RPC_HTTP_REDIRECTOR_STAGE,
                                            RPC_WSTR, RPC_WSTR, RPC_WSTR, RPC_WSTR,
                                            PVOID, PVOID, PVOID, PVOID,
                                            ULONG, PTR(RPC_WSTR), PTR(RPC_WSTR))
        
    RPC_HTTP_PROXY_FREE_STRING = WINAPI(VOID, RPC_WSTR)

RPC_C_AUTHZ_NONE    = 0
RPC_C_AUTHZ_NAME    = 1
RPC_C_AUTHZ_DCE     = 2
RPC_C_AUTHZ_DEFAULT = 0xffffffff

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcImpersonateClient(BindingHandle: WT_HANDLE) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcImpersonateClient2(BindingHandle: WT_HANDLE) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcRevertToSelfEx(BindingHandle: WT_HANDLE) -> int: ...

@rpcrt_foreign()
def RpcRevertToSelf() -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcImpersonateClientContainer(BindingHandle: WT_HANDLE) -> int: ...

@rpcrt_foreign()
def RpcRevertContainerImpersonation() -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_AUTHZ_HANDLE), 
               PTR(RPC_CSTR), PULONG, PULONG, PULONG)
def RpcBindingInqAuthClientA(
    ClientBinding: WT_HANDLE,
    Privs: IPointer[RPC_AUTHZ_HANDLE],
    ServerPrincName: IPointer[RPC_CSTR],
    AuthnLevel: PULONG, 
    AuthnSvc: PULONG,
    AuthzSvc: PULONG) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_AUTHZ_HANDLE), 
               PTR(RPC_WSTR), PULONG, PULONG, PULONG)
def RpcBindingInqAuthClientW(
    ClientBinding: WT_HANDLE,
    Privs: IPointer[RPC_AUTHZ_HANDLE],
    ServerPrincName: IPointer[RPC_WSTR],
    AuthnLevel: PULONG, 
    AuthnSvc: PULONG,
    AuthzSvc: PULONG) -> int: ...


@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_AUTHZ_HANDLE), 
               PTR(RPC_CSTR), PULONG, PULONG, PULONG, ULONG)
def RpcBindingInqAuthClientExA(
    ClientBinding: WT_HANDLE,
    Privs: IPointer[RPC_AUTHZ_HANDLE],
    ServerPrincName: IPointer[RPC_CSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthzSvc: PULONG, Flags: int) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_AUTHZ_HANDLE), 
               PTR(RPC_WSTR), PULONG, PULONG, PULONG, ULONG)
def RpcBindingInqAuthClientExW(
    ClientBinding: WT_HANDLE,
    Privs: IPointer[RPC_AUTHZ_HANDLE],
    ServerPrincName: IPointer[RPC_WSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthzSvc: PULONG, Flags: int) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_CSTR), PULONG, PULONG, 
               PTR(RPC_AUTH_IDENTITY_HANDLE), PULONG)
def RpcBindingInqAuthInfoA(
    Binding: WT_HANDLE,
    ServerPrincName: IPointer[RPC_CSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthIdentity: IPointer[RPC_AUTH_IDENTITY_HANDLE],
    AuthzSvc: PULONG) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_WSTR), PULONG, PULONG, 
               PTR(RPC_AUTH_IDENTITY_HANDLE), PULONG)
def RpcBindingInqAuthInfoW(
    Binding: WT_HANDLE,
    ServerPrincName: IPointer[RPC_WSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthIdentity: IPointer[RPC_AUTH_IDENTITY_HANDLE],
    AuthzSvc: PULONG) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_CSTR, ULONG, ULONG, 
               RPC_AUTH_IDENTITY_HANDLE, ULONG)
def RpcBindingSetAuthInfoA(
    Binding: WT_HANDLE,
    ServerPrincName: WT_LPSTR,
    AuthnLevel: int,
    AuthnSvc: int,
    AuthIdentity: WT_HANDLE,
    AuthzSvc: int) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_CSTR, ULONG, ULONG, 
               RPC_AUTH_IDENTITY_HANDLE, ULONG, RPC_SECURITY_QOS.PTR())
def RpcBindingSetAuthInfoExA(
    Binding: WT_HANDLE,
    ServerPrincName: WT_LPSTR,
    AuthnLevel: int,
    AuthnSvc: int,
    AuthIdentity: WT_HANDLE,
    AuthzSvc: int,
    SecurityQos: IPointer[RPC_SECURITY_QOS]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_WSTR, ULONG, ULONG, 
               RPC_AUTH_IDENTITY_HANDLE, ULONG)
def RpcBindingSetAuthInfoW(
    Binding: WT_HANDLE,
    ServerPrincName: WT_LPWSTR,
    AuthnLevel: int,
    AuthnSvc: int,
    AuthIdentity: WT_HANDLE,
    AuthzSvc: int) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_WSTR, ULONG, ULONG, 
               RPC_AUTH_IDENTITY_HANDLE, ULONG, RPC_SECURITY_QOS.PTR())
def RpcBindingSetAuthInfoExW(
    Binding: WT_HANDLE,
    ServerPrincName: WT_LPWSTR,
    AuthnLevel: int,
    AuthnSvc: int,
    AuthIdentity: WT_HANDLE,
    AuthzSvc: int,
    SecurityQos: IPointer[RPC_SECURITY_QOS]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_CSTR), PULONG, PULONG, 
               PTR(RPC_AUTH_IDENTITY_HANDLE), PULONG, ULONG,
               RPC_SECURITY_QOS.PTR())
def RpcBindingInqAuthInfoExA(
    Binding: WT_HANDLE,
    ServerPrincName: IPointer[RPC_CSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthIdentity: IPointer[RPC_AUTH_IDENTITY_HANDLE],
    AuthzSvc: PULONG, RpcQosVersion: int,
    SecurityQos: IPointer[RPC_SECURITY_QOS]) -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_WSTR), PULONG, PULONG, 
               PTR(RPC_AUTH_IDENTITY_HANDLE), PULONG, ULONG,
               RPC_SECURITY_QOS.PTR())
def RpcBindingInqAuthInfoExW(
    Binding: WT_HANDLE,
    ServerPrincName: IPointer[RPC_WSTR],
    AuthnLevel: PULONG, AuthnSvc: PULONG,
    AuthIdentity: IPointer[RPC_AUTH_IDENTITY_HANDLE],
    AuthzSvc: PULONG, RpcQosVersion: int,
    SecurityQos: IPointer[RPC_SECURITY_QOS]) -> int: ...

RPC_AUTH_KEY_RETRIEVAL_FN = WINAPI(PVOID, RPC_WSTR, ULONG, PVOID, PTR(RPC_STATUS))

@rpcrt_foreign(RPC_BINDING_HANDLE, RPC_STATUS)
def RpcServerCompleteSecurityCallback(
    BindingHandle: WT_HANDLE, Status: int) -> int: ...

@rpcrt_foreign(RPC_CSTR, ULONG, RPC_AUTH_KEY_RETRIEVAL_FN, PVOID)
def RpcServerRegisterAuthInfoA(
    ServerPrincName: WT_LPSTR,
    AuthnSvc: int,
    GetKeyFn: FARPROC,
    Arg: IVoidPtr) -> int: ...

@rpcrt_foreign(RPC_WSTR, ULONG, RPC_AUTH_KEY_RETRIEVAL_FN, PVOID)
def RpcServerRegisterAuthInfoW(
    ServerPrincName: WT_LPWSTR,
    AuthnSvc: int,
    GetKeyFn: FARPROC,
    Arg: IVoidPtr) -> int: ...

RpcBindingInqAuthClientEx = unicode(RpcBindingInqAuthClientExW, RpcBindingInqAuthClientExA)
RpcBindingInqAuthClient = unicode(RpcBindingInqAuthClientW, RpcBindingInqAuthClientA)
RpcBindingInqAuthInfo = unicode(RpcBindingInqAuthInfoW, RpcBindingInqAuthInfoA)
RpcBindingSetAuthInfo = unicode(RpcBindingSetAuthInfoW, RpcBindingSetAuthInfoA)
RpcBindingSetAuthInfoEx = unicode(RpcBindingSetAuthInfoExW, RpcBindingSetAuthInfoExA)
RpcBindingInqAuthInfoEx = unicode(RpcBindingInqAuthInfoExW, RpcBindingInqAuthInfoExA)
RpcServerRegisterAuthInfo = unicode(RpcServerRegisterAuthInfoW, RpcServerRegisterAuthInfoA)

if _version >= WIN32_WINNT_WINXP:
    class RPC_CLIENT_INFORMATION1(CStructure):
        _fields_ = [
            ('UserName', LPSTR),
            ('ComputerName', LPSTR),
            ('Privilege', USHORT),
            ('AuthFlags', ULONG)
        ]
        
        ComputerName: LPSTR
        UserName: LPSTR
        Privilege: int
        AuthFlags: int
        
    PRPC_CLIENT_INFORMATION1 = RPC_CLIENT_INFORMATION1.PTR()

@rpcrt_foreign(RPC_BINDING_HANDLE, PTR(RPC_BINDING_HANDLE))
def RpcBindingServerFromClient(
    ClientBinding: WT_HANDLE, 
    ServerBinding: IPointer[RPC_BINDING_HANDLE]) -> int: ...

@rpcrt4.foreign(VOID, RPC_STATUS)
def RpcRaiseException(exception: int): ...

@rpcrt_foreign()
def RpcTestCancel() -> int: ...

@rpcrt_foreign(RPC_BINDING_HANDLE)
def RpcServerTestCancel(BindingHandle: WT_HANDLE) -> int: ...

@rpcrt_foreign(PVOID)
def RpcCancelThread(Thread: IVoidPtr) -> int: ...

@rpcrt_foreign(PVOID, LONG)
def RpcCancelThreadEx(Thread: IVoidPtr, Timeout: int) -> int: ...

@rpcrt_foreign(UUID.PTR())
def UuidCreate(Uuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(UUID.PTR())
def UuidCreateSequential(Uuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(UUID.PTR(), PTR(RPC_CSTR))
def UuidToStringA(Uuid: IPointer[UUID],
                  StringUuid: IPointer[RPC_CSTR]) -> int: ...

@rpcrt_foreign(UUID.PTR(), PTR(RPC_WSTR))
def UuidToStringW(Uuid: IPointer[UUID],
                  StringUuid: IPointer[RPC_WSTR]) -> int: ...

@rpcrt_foreign(RPC_CSTR, UUID.PTR())
def UuidFromStringA(StringUuid: WT_LPSTR,
                    Uuid: IPointer[UUID]) -> int: ...

@rpcrt_foreign(RPC_WSTR, UUID.PTR())
def UuidFromStringW(StringUuid: WT_LPWSTR,
                    Uuid: IPointer[UUID]) -> int: ...

UuidToString = unicode(UuidToStringW, UuidToStringA)
UuidFromString = unicode(UuidFromStringW, UuidFromStringA)

@rpcrt4.foreign(INT, UUID.PTR(), UUID.PTR(), PTR(RPC_STATUS))
def UuidCompare(Uuid1: IPointer[UUID], 
                Uuid2: IPointer[UUID],
                Status: IPointer[RPC_STATUS]) -> int: ...

@rpcrt_foreign(UUID.PTR())
def UuidCreateNil(NilUuid: IPointer[UUID]) -> int: ...

@rpcrt4.foreign(INT, UUID.PTR(), UUID.PTR(), PTR(RPC_STATUS))
def UuidEqual(Uuid1: IPointer[UUID],
              Uuid2: IPointer[UUID],
              Status: IPointer[RPC_STATUS]) -> int: ...

@rpcrt4.foreign(USHORT, UUID.PTR(), PTR(RPC_STATUS))
def UuidHash(Uuid: IPointer[UUID],
             Status: IPointer[RPC_STATUS]) -> int: ...

@rpcrt4.foreign(INT, UUID.PTR(), PTR(RPC_STATUS))
def UuidIsNil(Uuid: IPointer[UUID],
              Status: IPointer[RPC_STATUS]) -> int: ...