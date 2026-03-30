#
# com/rpc/dcepriv.py
#

from .dce import *

class RPC_VERSION(CStructure):
    _fields_ = [
        ('MajorVersion', USHORT),
        ('MinorVersion', USHORT)
    ]
    
    MajorVersion: int
    MinorVersion: int
    
class RPC_SYNTAX_IDENTIFIER(CStructure):
    _fields_ = [
        ('SyntaxGUID', GUID),
        ('SyntaxVersion', RPC_VERSION)
    ]
    
    SyntaxVersion: RPC_VERSION
    SyntaxGuid: GUID
    
PRPC_SYNTAX_IDENTIFIER = RPC_SYNTAX_IDENTIFIER.PTR()

class RPC_MESSAGE(CStructure):
    _fields_ = [
        ('Handle', RPC_BINDING_HANDLE),
        ('DataRepresentation', ULONG),
        ('Buffer', PVOID),
        ('BufferLength', UINT),
        ('ProcNum', UINT),
        ('TransferSyntax', PRPC_SYNTAX_IDENTIFIER),
        ('RpcInterfaceInformation', PVOID),
        ('ReservedForRuntime', PVOID),
        ('ManagerEpv', PTR(RPC_MGR_EPV)),
        ('ImportContext', PVOID),
        ('RpcFlags', ULONG)
    ]
    
    TransferSyntax: IPointer[RPC_SYNTAX_IDENTIFIER]
    RpcInterfaceInformation: int
    DataRepresentation: int
    ReservedForRuntime: int
    ImportContext: int
    BufferLength: int
    ManagerEpv: int
    RpcFlags: int
    ProcNum: int
    Buffer: int
    Handle: int
    
PRPC_MESSAGE = RPC_MESSAGE.PTR()

RPC_FORWARD_FUNCTION = WINAPI(RPC_STATUS,
                              UUID.PTR(),
                              RPC_VERSION.PTR(),
                              UUID.PTR(),
                              LPSTR,
                              PVOID)


PROTOCOL_NOT_LOADED = 1
PROTOCOL_LOADED = 2
PROTOCOL_ADDRESS_CHANGE = 3
RPC_ADDRESS_CHANGE_TYPE = INT

RPC_ADDRESS_CHANGE_FN = WINAPI(VOID, PVOID)

from ...sdkddkver import *

_version = cpreproc.get_version()

#
# New context handle flavors.
#

RPC_CONTEXT_HANDLE_DEFAULT_GUARD    = 0xFFFFF00D

RPC_CONTEXT_HANDLE_DEFAULT_FLAGS    = 0x00000000
RPC_CONTEXT_HANDLE_FLAGS            = 0x30000000
RPC_CONTEXT_HANDLE_SERIALIZE        = 0x10000000
RPC_CONTEXT_HANDLE_DONT_SERIALIZE   = 0x20000000

if _version >= WIN32_WINNT_VISTA:
    RPC_TYPE_STRICT_CONTEXT_HANDLE      = 0x40000000
    
if _version >= WIN32_WINNT_WIN10:
    RPC_TYPE_DISCONNECT_EVENT_CONTEXT_HANDLE  = 0x80000000

#
# Types of function calls for datagram rpc
#

RPC_NCA_FLAGS_DEFAULT       = 0x00000000  # 0b000...000 
RPC_NCA_FLAGS_IDEMPOTENT    = 0x00000001  # 0b000...001 
RPC_NCA_FLAGS_BROADCAST     = 0x00000002  # 0b000...010 
RPC_NCA_FLAGS_MAYBE         = 0x00000004  # 0b000...100 

if _version >= WIN32_WINNT_VISTA:
    RPCFLG_HAS_GUARANTEE        = 0x00000010

RPCFLG_WINRT_REMOTE_ASYNC   = 0x00000020

# Flags used in RpcFlag field of RPC_MESSAGE structure 

RPC_BUFFER_COMPLETE         = 0x00001000 # used by pipes 
RPC_BUFFER_PARTIAL          = 0x00002000 # used by pipes 
RPC_BUFFER_EXTRA            = 0x00004000 # used by pipes 
RPC_BUFFER_ASYNC            = 0x00008000 # used by async rpc 
RPC_BUFFER_NONOTIFY         = 0x00010000 # used by async pipes 

RPCFLG_MESSAGE              = 0x01000000
RPCFLG_AUTO_COMPLETE        = 0x08000000
RPCFLG_LOCAL_CALL           = 0x10000000
RPCFLG_INPUT_SYNCHRONOUS    = 0x20000000
RPCFLG_ASYNCHRONOUS         = 0x40000000
RPCFLG_NON_NDR              = 0x80000000

if _version >= WIN32_WINNT_WINXP:
    RPCFLG_HAS_MULTI_SYNTAXES   = 0x02000000
    RPCFLG_HAS_CALLBACK         = 0x04000000

if _version >= WIN32_WINNT_VISTA:
    # These two bits will hold the combination of
    # anonymous/admin/authenticate/mixed mode
    RPCFLG_ACCESSIBILITY_BIT1   = 0x00100000
    RPCFLG_ACCESSIBILITY_BIT2   = 0x00200000
    RPCFLG_ACCESS_LOCAL         = 0x00400000

    # This goes to MIDL_STUB_DESC only
    NDR_CUSTOM_OR_DEFAULT_ALLOCATOR = 0x10000000
    NDR_DEFAULT_ALLOCATOR           = 0x20000000

if _version >= WIN32_WINNT_WIN8:
    # NDR64 on ARM includes ARM parameter layout info
    RPCFLG_NDR64_CONTAINS_ARM_LAYOUT = 0x04000000

if _version >= WIN32_WINNT_WINBLUE:
    """
    Used by COM to inform RPC that even though this is an
    async RPC call, there is a thread waiting for the call
    to complete. Essentially, from COM perspective, this is a
    sync call. This flag will be passed down to ALPC in order
    to count the wake charges properly. 
    """

    RPCFLG_SENDER_WAITING_FOR_REPLY = 0x00800000 

RPC_FLAGS_VALID_BIT = 0x00008000

RPC_DISPATCH_FUNCTION = WINAPI(VOID, PRPC_MESSAGE)

class RPC_DISPATCH_TABLE(CStructure):
    _fields_ = [
        ('DispatchTableCount', UINT),
        ('DispatchTable', PTR(RPC_DISPATCH_FUNCTION)),
        ('Reserved', LONG_PTR)
    ]
    
    DispatchTable: IPointer[FARPROC]
    DispatchTableCount: int
    Reserved: int
    
PRPC_DISPATCH_TABLE = RPC_DISPATCH_TABLE.PTR()

class RPC_PROTSEQ_ENDPOINT(CStructure):
    _fields_ = [
        ('RpcProtocolSequence', LPSTR),
        ('Endpoint', LPSTR)
    ]
    
    RpcProtocolSequence: str
    Endpoint: str
    
PRPC_PROTSEQ_ENDPOINT = RPC_PROTSEQ_ENDPOINT.PTR()

"""
Both of these types MUST start with the InterfaceId and TransferSyntax.
Look at RpcIfInqId and I_RpcIfInqTransferSyntaxes to see why.
"""
NT351_INTERFACE_SIZE = 0x40
RPC_INTERFACE_HAS_PIPES = 0x0001

class RPC_SERVER_INTERFACE(CStructure):
    _fields_ = [
        ('Length', UINT),
        ('InterfaceId', RPC_SYNTAX_IDENTIFIER),
        ('TransferSyntax', RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', PRPC_DISPATCH_TABLE),
        ('RpcProtseqEndpointCount', UINT),
        ('RpcProtseqEndpoint', PRPC_PROTSEQ_ENDPOINT),
        ('DefaultManagerEpv', PTR(RPC_MGR_EPV)),
        ('InterpreterInfo', LPCVOID),
        ('Flags', UINT)
    ]
    
    RpcProtseqEndpoint: IPointer[RPC_PROTSEQ_ENDPOINT]
    DispatchTable: IPointer[RPC_DISPATCH_TABLE]
    TransferSyntax: RPC_SYNTAX_IDENTIFIER
    InterfaceId: RPC_SYNTAX_IDENTIFIER
    RpcProtseqEndpointCount: int
    DefaultManagerEpv: int
    InterpreterInfo: int
    Length: int
    Flags: int
    
PRPC_SERVER_INTERFACE = RPC_SERVER_INTERFACE.PTR()

class RPC_CLIENT_INTERFACE(CStructure):
    _fields_ = [
        ('Length', UINT),
        ('InterfaceId', RPC_SYNTAX_IDENTIFIER),
        ('TransferSyntax', RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', PRPC_DISPATCH_TABLE),
        ('RpcProtseqEndpointCount', UINT),
        ('RpcProtseqEndpoint', PRPC_PROTSEQ_ENDPOINT),
        ('Reserved', ULONG_PTR),
        ('InterpreterInfo', LPCVOID),
        ('Flags', UINT)
    ]
    
    RpcProtseqEndpoint: IPointer[RPC_PROTSEQ_ENDPOINT]
    DispatchTable: IPointer[RPC_DISPATCH_TABLE]
    TransferSyntax: RPC_SYNTAX_IDENTIFIER
    InterfaceId: RPC_SYNTAX_IDENTIFIER
    RpcProtseqEndpointCount: int
    InterpreterInfo: int
    Reserved: int
    Length: int
    Flags: int
    
PRPC_CLIENT_INTERFACE = RPC_CLIENT_INTERFACE.PTR()

