#
# com/rpc/ndr.py
#

# Definitions for stub data structures and prototypes of helper functions.

from ..baseinterfacedef import *
from .dcepriv import *

"""
/****************************************************************************

     Network Computing Architecture (NCA) definition:

     Network Data Representation: (NDR) Label format:
     An unsigned long (32 bits) with the following layout:

     3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
     1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    +---------------+---------------+---------------+-------+-------+
    |   Reserved    |   Reserved    |Floating point | Int   | Char  |
    |               |               |Representation | Rep.  | Rep.  |
    +---------------+---------------+---------------+-------+-------+

     Where

         Reserved:

             Must be zero (0) for NCA 1.5 and NCA 2.0.

         Floating point Representation is:

             0 - IEEE
             1 - VAX
             2 - Cray
             3 - IBM

         Int Rep. is Integer Representation:

             0 - Big Endian
             1 - Little Endian

         Char Rep. is Character Representation:

             0 - ASCII
             1 - EBCDIC

     The Microsoft Local Data Representation (for all platforms which are
     of interest currently is edefined below:

 ****************************************************************************/
"""

NDR_CHAR_REP_MASK               = 0x0000000F
NDR_INT_REP_MASK                = 0x000000F0
NDR_FLOAT_REP_MASK              = 0x0000FF00

NDR_LITTLE_ENDIAN               = 0x00000010
NDR_BIG_ENDIAN                  = 0x00000000

NDR_IEEE_FLOAT                  = 0x00000000
NDR_VAX_FLOAT                   = 0x00000100
NDR_IBM_FLOAT                   = 0x00000300

NDR_ASCII_CHAR                  = 0x00000000
NDR_EBCDIC_CHAR                 = 0x00000001

NDR_LOCAL_DATA_REPRESENTATION   = 0x00000010
NDR_LOCAL_ENDIAN                = NDR_LITTLE_ENDIAN

# ***************************************************************************
# *  Other MIDL base types / predefined types:
# ***************************************************************************

small = c_byte
byte = c_ubyte
cs_byte = byte
boolean = c_ubyte

hyper = c_int64
MIDL_uhyper = c_uint64

wchar_t = c_wchar

size_t = c_size_t

@rpcrt4.foreign(PVOID, size_t)
def MIDL_user_allocate(size: int) -> int: ...

@rpcrt4.foreign(VOID, PVOID)
def MIDL_user_free(pv: PVOID): ...

PFN_RPC_ALLOCATE = WINAPI(PVOID, size_t)
PFN_RPC_FREE = WINAPI(VOID, PVOID)

@rpcrt4.foreign(PVOID, handle_t, size_t, PFN_RPC_ALLOCATE)
def I_RpcDefaultAllocate(bh: handle_t, size: int, RealAlloc: FARPROC) -> int: ...

@rpcrt4.foreign(VOID, handle_t, PVOID, PFN_RPC_FREE)
def I_RpcDefaultFree(bh: handle_t, pv: PVOID, RealFree: FARPROC): ...

# ***************************************************************************
# * Context handle management related definitions:
# *
# * Client and Server Contexts.
# *
# ***************************************************************************

NDR_CCONTEXT = PVOID

class _NDR_SCONTEXT(CStructure):
    _fields_ = [
        ('pad', PVOID * 2),
        ('userContext', PVOID)
    ]
    
    pad: IArray[PVOID]
    userContext: int
    
NDR_SCONTEXT = _NDR_SCONTEXT.PTR()

def NDRSContextValue(hContext: IPointer[_NDR_SCONTEXT]) -> IPointer[PVOID]:
    return PtrUtil.get_address(hContext) + sizeof(PVOID)*2

cbNDRContext = 20 # size of context on WIRE

NDR_RUNDOWN = WINAPI(VOID, PVOID)
NDR_NOTIFY_ROUTINE = WINAPI(VOID, VOID)
NDR_NOTIFY2_ROUTINE = WINAPI(VOID, boolean)

class SCONTEXT_QUEUE(CStructure):
    _fields_ = [
        ('NumberOfObjects', ULONG),
        ('ArrayOfObjects', PTR(NDR_SCONTEXT))
    ]
    
    ArrayOfObjects: IDoublePtr[_NDR_SCONTEXT]
    NumberOfObjects: int
    
PSCONTEXT_QUEUE = SCONTEXT_QUEUE.PTR()

@rpcrt4.foreign(RPC_BINDING_HANDLE, NDR_CCONTEXT)
def NDRCContextBinding(CContext: NDR_CCONTEXT) -> int: ...

@rpcrt4.foreign(VOID, NDR_CCONTEXT, PVOID)
def NDRCContextMarshall(CContext: NDR_CCONTEXT, pBuff: PVOID): ...

@rpcrt4.foreign(VOID, PTR(NDR_CCONTEXT), RPC_BINDING_HANDLE, PVOID, ULONG)
def NDRCContextUnmarshall(pCContext: IPointer[NDR_CCONTEXT],
                          hBinding: RPC_BINDING_HANDLE,
                          pBuff: PVOID,
                          DataRepresentation: int): ...

@rpcrt4.foreign(VOID, PTR(NDR_CCONTEXT), RPC_BINDING_HANDLE, PVOID, ULONG)
def NDRCContextUnmarshall2(pCContext: IPointer[NDR_CCONTEXT],
                          hBinding: RPC_BINDING_HANDLE,
                          pBuff: PVOID,
                          DataRepresentation: int): ...

@rpcrt4.foreign(VOID, NDR_SCONTEXT, PVOID, NDR_RUNDOWN)
def NDRSContextMarshall(CContext: IPointer[_NDR_SCONTEXT],
                        pBuff: PVOID,
                        userRunDownIn: FARPROC): ...

@rpcrt4.foreign(NDR_SCONTEXT, PVOID, ULONG)
def NDRSContextUnmarshall(pBuff: PVOID, DataRepresentation: int
                          ) -> IPointer[_NDR_SCONTEXT]: ...

@rpcrt4.foreign(VOID, RPC_BINDING_HANDLE, NDR_SCONTEXT, PVOID, NDR_RUNDOWN)
def NDRSContextMarshallEx(BindingHandle: RPC_BINDING_HANDLE,
                          CContext: IPointer[_NDR_SCONTEXT],
                          pBuff: PVOID,
                          userRunDownIn: FARPROC): ...

@rpcrt4.foreign(VOID, RPC_BINDING_HANDLE, NDR_SCONTEXT, PVOID, NDR_RUNDOWN, PVOID, ULONG)
def NDRSContextMarshall2(BindingHandle: RPC_BINDING_HANDLE,
                          CContext: IPointer[_NDR_SCONTEXT],
                          pBuff: PVOID,
                          userRunDownIn: FARPROC,
                          CtxGuard: PVOID,
                          Flags: int): ...

@rpcrt4.foreign(NDR_SCONTEXT, RPC_BINDING_HANDLE, PVOID, ULONG)
def NDRSContextUnmarshallEx(BindingHandle: RPC_BINDING_HANDLE,
                            pBuff: PVOID,
                            DataRepresentation: int) -> IPointer[_NDR_SCONTEXT]: ...

@rpcrt4.foreign(NDR_SCONTEXT, RPC_BINDING_HANDLE, PVOID, ULONG, PVOID, ULONG)
def NDRSContextUnmarshall2(BindingHandle: RPC_BINDING_HANDLE,
                            pBuff: PVOID,
                            DataRepresentation: int,
                            CtxGuard: PVOID,
                            Flags: int) -> IPointer[_NDR_SCONTEXT]: ...

@rpcrt4.foreign(VOID, PLPVOID)
def RpcSsDestroyClientContext(ContextHandle: IPointer[PVOID]): ...

# ***************************************************************************
#    NDR conversion related definitions.
# ***************************************************************************

# -------------------------
# -    Not Implemented    -
# -------------------------

# byte_from_ndr
# byte_array_from_ndr
# boolean_from_ndr
# boolean_array_from_ndr
# small_from_ndr
# small_from_ndr_temp
# small_array_from_ndr

# ****************************************************************************
#    Platform specific mapping of c-runtime functions.
# ****************************************************************************

# -------------------------
# -    Not Implemented    -
# -------------------------

# MIDL_ascii_strlen
# MIDL_ascii_strcpy
# MIDL_memset

# ****************************************************************************
#    MIDL 2.0 ndr definitions.
# ****************************************************************************

error_status_t = ULONG

# -------------------------
# -    Not Implemented    -
# -------------------------

# _midl_ma1
# _midl_ma2
# _midl_ma4
# _midl_ma8
# _midl_unma1
# _midl_unma2
# _midl_unma3
# _midl_unma4

# Some alignment specific macros.

# RKK64
# these appear to be used in fossils inside MIDL

# -------------------------
# -    Not Implemented    -
# -------------------------

# _midl_fa2
# _midl_fa4
# _midl_fa8
# _midl_addp

# Marshalling macros

# -------------------------
# -    Not Implemented    -
# -------------------------

# _midl_marsh_lhs
# _midl_marsh_up
# _midl_advmp
# _midl_unmarsh_up

######################################
# Ndr macros.
######################################

# RKK64
# these appear to be used in fossils inside MIDL

# -------------------------
# -    Not Implemented    -
# -------------------------

# NdrMarshConfStringHdr
# NdrUnMarshConfStringHdr
# NdrMarshCCtxtHdl
# NdrUnMarshCCtxtHdl
# NdrUnarshSCtxtHdl
# NdrMarshSCtxtHdl

# def NdrMarshCCtxtHdl(pc: NDR_CCONTEXT, p: int):
#     NDRCContextMarshall(pc, p)
    
# def NdrUnMarshCCtxtHdl(pc: NDR_CCONTEXT, p: int, h: int, drep: int):
#     NDRCContextUnmarshall(pc, h, p, drep)

# end of unused

def NdrFieldOffset(s: CStructure, f: str) -> int:
    return s.offset(f)

def NdrFieldPad(s: CStructure, f: str, p: str, t) -> int:
    return ((NdrFieldOffset(s, f) - NdrFieldOffset(s, p)) - sizeof(t))

def NdrFcShort(s: int) -> tuple[int, int]:
    return c_ubyte(s & 0xff).value, c_ubyte(s >> 8).value

def NdrFcLong(s: int) -> tuple[int, int, int, int]:
    return (c_ubyte(s & 0xff).value, c_ubyte((s & 0x0000ff00) >> 8).value,
            c_ubyte((s & 0x00ff0000) >> 16).value, c_ubyte(s >> 24).value)
    
#
# On the server side, the following exceptions are mapped to
# the bad stub data exception if -error stub_data is used.
#

# -------------------------
# -    Not Implemented    -
# -------------------------

# RPC_BAD_STUB_DATA_EXCEPTION_FILTER

######################################
# Some stub helper functions.
######################################

######################################
# Stub helper structures.
######################################

RPC_BUFPTR = PTR(c_ubyte)
RPC_LENGTH = ULONG

# Expression evaluation callback routine prototype.
EXPR_EVAL = WINAPI(VOID, PVOID)

PFORMAT_STRING = LPCSTR

class ARRAY_INFO(CStructure):
    """
    Multidimensional conformant/varying array struct.
    """
    _fields_ = [
        ('Dimension', LONG),
        
        # These fields MUST be (unsigned long*)
        ('BufferConformanceMark', PULONG),
        ('BufferVarianceMark', PULONG),
        
        # Count arrays, used for top level arrays in -Os stubs
        ('MaxCountArray', PULONG),
        ('OffsetArray', PULONG),
        ('ActualCountArray', PULONG)
    ]
    
    BufferConformanceMark: PULONG
    BufferVarianceMark: PULONG
    ActualCountArray: PULONG
    MaxCountArray: PULONG
    OffsetArray: PULONG
    Dimension: int
    
PARRAY_INFO = ARRAY_INFO.PTR()

class NDR_ALLOC_ALL_NODES_CONTEXT(CStructure):
    _fields_ = []
    
class NDR_POINTER_QUEUE_STATE(CStructure):
    _fields_ = []
    
class _NDR_PROC_CONTEXT(CStructure):
    _fields_ = []
    
class _NDR_ASYNC_MESSAGE(CStructure):
    _fields_ = []
    
class _NDR_CORRELATION_INFO(CStructure):
    _fields_ = []

#
# Generic handle bind/unbind routine pair.
#
GENERIC_BINDING_ROUTINE = WINAPI(PVOID, PVOID)
GENERIC_UNBIND_ROUTINE = WINAPI(VOID, PVOID, PBYTE)

class GENERIC_BINDING_ROUTINE_PAIR(CStructure):
    _fields_ = [
        ('pfnBind', GENERIC_BINDING_ROUTINE),
        ('pfnUnbind', GENERIC_UNBIND_ROUTINE)
    ]
    
    pfnUnbind: FARPROC
    pfnBind: FARPROC
    
PGENERIC_BINDING_ROUTINE_PAIR = GENERIC_BINDING_ROUTINE_PAIR.PTR()

class GENERIC_BINDING_INFO(CStructure):
    _fields_ = [
        ('pObj', PVOID),
        ('Size', UINT),
        ('pfnBind', GENERIC_BINDING_ROUTINE),
        ('pfnUnbind', GENERIC_UNBIND_ROUTINE)
    ]
    
    pfnUnbind: FARPROC
    pfnBind: FARPROC
    pObj: int
    Size: int
    
PGENERIC_BINDING_INFO = GENERIC_BINDING_INFO.PTR()

# typedef EXPR_EVAL - see above
# typedefs for xmit_as

XMIT_HELPER_ROUTINE = WINAPI(VOID, PVOID)

class XMIT_ROUTINE_QUINTUPLE(CStructure):
    _fields_ = [
        ('pfnTranslateToXmit', XMIT_HELPER_ROUTINE),
        ('pfnTranslateFromXmit', XMIT_HELPER_ROUTINE),
        ('pfnFreeXmit', XMIT_HELPER_ROUTINE),
        ('pfnFreeInst', XMIT_HELPER_ROUTINE)
    ]
    
    pfnTranslationFromXmit: FARPROC
    pfnTranslateToXmit: FARPROC
    pfnFreeXmit: FARPROC
    pfnFreeInst: FARPROC

PXMIT_ROUTINE_QUINTUPLE = XMIT_ROUTINE_QUINTUPLE.PTR()

USER_MARSHAL_SIZING_ROUTINE = WINAPI(ULONG, PULONG, ULONG, PVOID)

USER_MARSHAL_MARSHALLING_ROUTINE = WINAPI(PBYTE, PULONG, PBYTE, PVOID)

USER_MARSHAL_UNMARSHALLING_ROUTINE = WINAPI(PBYTE, PULONG, PBYTE, PVOID)

USER_MARSHAL_FREEING_ROUTINE = WINAPI(VOID, PULONG, PVOID)

class USER_MARSHAL_ROUTINE_QUADRUPLE(CStructure):
    _fields_ = [
        ('pfnBufferSize', USER_MARSHAL_SIZING_ROUTINE),
        ('pfnMarshall', USER_MARSHAL_MARSHALLING_ROUTINE),
        ('pfnUnmarshall', USER_MARSHAL_UNMARSHALLING_ROUTINE),
        ('pfnFree', USER_MARSHAL_FREEING_ROUTINE)
    ]
    
    pfnBufferSize: FARPROC
    pfnUnmarshall: FARPROC
    pfnMarshall: FARPROC
    pfnFree: FARPROC

USER_MARSHAL_CB_SIGNATURE = b'USRC'

USER_MARSHAL_CB_BUFFER_SIZE = 0
USER_MARSHAL_CB_MARSHALL = 1
USER_MARSHAL_CB_UNMARSHALL = 2
USER_MARSHAL_CB_FREE = 3
USER_MARSHAL_CB_TYPE = INT

class USER_MARSHAL_CB(CStructure):
    _fields_ = [
        ('Flags', ULONG),
        ('_pStubMsg', PVOID),
        ('pReserve', PFORMAT_STRING),
        ('Signature', ULONG),
        ('CBType', USER_MARSHAL_CB_TYPE),
        ('pFormat', PFORMAT_STRING),
        ('pTypeFormat', PFORMAT_STRING)
    ]
    
    pStubMsg: IPointer['MIDL_STUB_MESSAGE']
    pTypeFormat: bytes
    pReserve: bytes
    Signature: int
    pFormat: bytes
    CBType: int
    Flags: int
    
def USER_CALL_CTXT_MASK(f: int) -> int:
    return ((f) & 0x00ff)

def USER_CALL_AUX_MASK(f: int) -> int:
    return ((f) & 0xff00)

def GET_USER_DATA_REP(f: int) -> int:
    return ((f) >> 16)

USER_CALL_IS_ASYNC             = 0x0100 # aux flag: in an [async] call
USER_CALL_NEW_CORRELATION_DESC = 0x0200
    
class NDR_EXPR_DESC(CStructure):
    _fields_ = [
        ('pOffset', PCUSHORT),
        ('pFormatExpr', PFORMAT_STRING)
    ]
    
    pFormatExpr: bytes
    pOffset: PCUSHORT
    
class MALLOC_FREE_STRUCT(CStructure):
    _fields_ = [
        ('pfnAllocate', PFN_RPC_ALLOCATE),
        ('pfnFree', PFN_RPC_FREE)
    ]
    
    pfnAllocate: FARPROC
    pfnFree: FARPROC
    
class COMM_FAULT_OFFSETS(CStructure):
    _fields_ = [
        ('CommOffset', SHORT),
        ('FaultOffset', SHORT)
    ]
    
    FaultOffset: int
    CommOffset: int
    
#
# International character support definitions
#

IDL_CS_NO_CONVERT = 0
IDL_CS_IN_PLACE_CONVERT = 1
IDL_CS_NEW_BUFFER_CONVERT = 2
IDL_CS_CONVERT = INT

CS_TYPE_NET_SIZE_ROUTINE = WINAPI(VOID, RPC_BINDING_HANDLE, ULONG, ULONG, PTR(IDL_CS_CONVERT), PULONG, PTR(error_status_t))

CS_TYPE_LOCAL_SIZE_ROUTINE = WINAPI(VOID, RPC_BINDING_HANDLE, ULONG, ULONG, PTR(IDL_CS_CONVERT), PULONG, PTR(error_status_t))

CS_TYPE_TO_NETCS_ROUTINE = WINAPI(VOID, RPC_BINDING_HANDLE, ULONG, PVOID, ULONG, PBYTE, PULONG, PTR(error_status_t))

CS_TYPE_FROM_NETCS_ROUTINE = WINAPI(VOID, RPC_BINDING_HANDLE, ULONG, PBYTE, ULONG, ULONG, PVOID, PULONG, PTR(error_status_t))

CS_TAG_GETTING_ROUTINE = WINAPI(VOID, RPC_BINDING_HANDLE, INT, PULONG, PULONG, PULONG, PTR(error_status_t))

@rpcrt4.foreign(VOID, RPC_BINDING_HANDLE, INT, PULONG, PULONG, PULONG, PTR(error_status_t))
def RpcCsGetTags(hBinding: RPC_BINDING_HANDLE,
                 fServerSide: int,
                 pulSendingTag: PULONG,
                 pulDesiredReceivingTag: PULONG,
                 pulReceivingTag: PULONG,
                 pStatus: IPointer[error_status_t]): ...

class NDR_CS_SIZE_CONVERT_ROUTINES(CStructure):
    _fields_ = [
        ('pfnNetSize', CS_TYPE_NET_SIZE_ROUTINE),
        ('pfnToNetCs', CS_TYPE_TO_NETCS_ROUTINE),
        ('pfnLocalSize', CS_TYPE_LOCAL_SIZE_ROUTINE),
        ('pfnFromNetCs', CS_TYPE_FROM_NETCS_ROUTINE)
    ]
    
    pfnFromNetCs: FARPROC
    pfnLocalSize: FARPROC
    pfnToNetCs: FARPROC
    pfnNetSize: FARPROC
    
class NDR_CS_ROUTINES(CStructure):
    _fields_ = [
        ('pSizeConvertRoutines', NDR_CS_SIZE_CONVERT_ROUTINES.PTR()),
        ('pTagGettingRoutines', PTR(CS_TAG_GETTING_ROUTINE))
    ]
    
    pSizeConvertRoutines: IPointer[NDR_CS_SIZE_CONVERT_ROUTINES]
    pTagGettingRoutines: IPointer[FARPROC]
    
@CStructure.make
class MIDL_STUB_DESC(CStructure):
    """
    MIDL Stub Descriptor
    """
    class IMPLICIT_HANDLE_INFO(CUnion):
        _fields_ = [
            ('pAutoHandle', PTR(handle_t)),
            ('pPrimitiveHandle', PTR(handle_t)),
            ('pGenericBindingInfo', PGENERIC_BINDING_INFO)
        ]
        
    RpcInterfaceInformation: IVoidPtrT
    pfnAllocate: FARPROC
    pfnFree: FARPROC
    
    add_annotation('pfnAllocate', PFN_RPC_ALLOCATE)
    add_annotation('pfnFree', PFN_RPC_FREE)
    
    _IMPLICIT_HANDLE_INFO: IAnonymous[IMPLICIT_HANDLE_INFO]
    
    apfnNdrRundownRoutines: IPointer[FARPROC]
    add_annotation('apfnNdrRundownRoutines', IPointer[NDR_RUNDOWN])
    
    aGenericBindingRoutinePairs: IPointer[GENERIC_BINDING_ROUTINE_PAIR]
    
    apfnExprEval: IPointer[FARPROC]
    add_annotation('apfnExprEval', IPointer[EXPR_EVAL])
    
    aXmitQuintuple: IPointer[XMIT_ROUTINE_QUINTUPLE]
    pFormatTypes: IPointer[byte]
    fCheckBounds: IInt
    
    # Ndr library version.
    Version: IUlong
    
    pMallocFreeStruct: IPointer[MALLOC_FREE_STRUCT]
    
    MIDLVersion: ILong
    
    CommFaultOffsets: IPointer[COMM_FAULT_OFFSETS]
    
    # New fields for version 3.0+
    aUserMarshalQuadruple: IPointer[USER_MARSHAL_ROUTINE_QUADRUPLE]
    
    # Notify routines - added for NT5, MIDL 5.0
    NotifyRoutineTable: IPointer[FARPROC]
    add_annotation('NotifyRoutineTable', IPointer[NDR_NOTIFY_ROUTINE])
    
    #
    # Reserved for future use.
    #
    
    mFlags: IUlongPtr
    
    # International support routines - added for 64bit post NT5
    CsRoutineTables: IPointer[NDR_CS_ROUTINES]
    
    ProxyServerInfo: IVoidPtrT
    pExprInfo: IPointer[NDR_EXPR_DESC]
    
    # Fields up to now present in win2000 release.

PMIDL_STUB_DESC = MIDL_STUB_DESC.PTR()

# BUGBUG: can we get rid of this defintion altogether, just leave void * here?
XLAT_SERVER = 1
XLAT_CLIENT = 2
XLAT_SIDE = INT

class FULL_PTR_XLAT_TABLES(CStructure):
    _fields_ = [
        ('RefIdToPointer', PVOID),
        ('PointerToRefId', PVOID),
        ('NextRefId', ULONG),
        ('XlatSide', XLAT_SIDE)
    ]
    
    RefIdToPointer: int
    PointerToRefId: int
    NextRefId: int
    XlatSide: int
    
PFULL_PTR_XLAT_TABLES = FULL_PTR_XLAT_TABLES.PTR()

@CStructure.make
class MIDL_STUB_MESSAGE(CStructure):
    # RPC message structure.
    RpcMsg: IPointer[RPC_MESSAGE]
    
    # Pointer into RPC message buffer.
    Buffer: IPointer[byte]
    
    #
    # These are used internally by the Ndr routines to mark the beginning
    # and end of an incoming RPC buffer.
    #
    BufferStart: IPointer[byte]
    BufferEnd: IPointer[byte]
    
    #
    # Used internally by the Ndr routines as a place holder in the buffer.
    # On the marshalling side it's used to mark the location where conformance
    # size should be marshalled.
    # On the unmarshalling side it's used to mark the location in the buffer
    # used during pointer unmarshalling to base pointer offsets off of.
    #
    BufferMark: IPointer[byte]
    
    # Set by the buffer sizing routines.
    BufferLength: IUlong
    
    # Set by the memory sizing routines.
    MemorySize: IUlong
    
    # Pointer to user memory.
    Memory: IPointer[byte]
    
    # Is the Ndr routine begin called from a client side stub.
    IsClient: IByte
    Pad: IByte
    uFlags2: IUshort
    
    # Can the buffer be re-used for memory on unmarshalling.
    ReuseBuffer: IInt
    
    # Hold the context for allocate all nodes
    pAllocAllNodesContext: IPointer[NDR_ALLOC_ALL_NODES_CONTEXT]
    pPointerQueueState: IPointer[NDR_POINTER_QUEUE_STATE]
    
    #
    # Stuff needed while handling complex structures
    #
    
    # Ignore imbeded pointers while computing buffer or memory sizes.
    IgnoreEmbeddedPointers: IInt
    
    #
    # This marks the location in the buffer where pointees of a complex
    # struct reside.
    #
    PointerBufferMark: IPointer[byte]
    
    #
    # Used to catch errors in SendReceive.
    #
    CorrDespIncrement: IByte
    
    uFlags: IByte
    UniquePtrCount: IUshort
    
    #
    # Used internally by the Ndr routines.  Holds the max counts for
    # a conformant array.
    #
    MaxCount: IUlongPtr
    
    #
    # Used internally by the Ndr routines.  Holds the offsets for a varying
    # array.
    #
    Offset: IUlong
    
    #
    # Used internally by the Ndr routines.  Holds the actual counts for
    # a varying array.
    #
    ActualCount: IUlong
    
    # Allocation and Free routine to be used by the Ndr routines.
    pfnAllocate: FARPROC
    pfnFree: FARPROC
    
    remove_annotations('pfnAllocate', 'pfnFree')
    add_annotation('pfnAllocate', PFN_RPC_ALLOCATE)
    add_annotation('pfnFree', PFN_RPC_FREE)
    
    #
    # Top of parameter stack.  Used for "single call" stubs during marshalling
    # to hold the beginning of the parameter list on the stack.  Needed to
    # extract parameters which hold attribute values for top level arrays and
    # pointers.
    #
    StackTop: IPointer[byte]
    
    #
    #  Fields used for the transmit_as and represent_as objects.
    #  For represent_as the mapping is: presented=local, transmit=named.
    #
    pPresentedType: IPointer[byte]
    pTransmitType: IPointer[byte]
    
    #
    # When we first construct a binding on the client side, stick it
    # in the rpcmessage and later call RpcGetBuffer, the handle field
    # in the rpcmessage is changed. That's fine except that we need to
    # have that original handle for use in unmarshalling context handles
    # (the second argument in NDRCContextUnmarshall to be exact). So
    # stash the contructed handle here and extract it when needed.
    #
    SavedHandle: IHandle
    
    #
    # Pointer back to the stub descriptor.  Use this to get all handle info.
    #
    StubDesc: IPointer[MIDL_STUB_DESC]
    
    #
    # Full pointer stuff.
    FullPtrXlatTables: IPointer[FULL_PTR_XLAT_TABLES]
    FullPtrRefId: IUlong
    
    PointerLength: IUlong
    
    fInDontFree: IBool64
    fDontCallFreeInst: IBool64
    fUnused1: IBool64
    fHasReturn: IBool64
    fHasExtensions: IBool64
    fHasNewCorrDesc: IBool64
    fIsIn: IBool64
    fIsOut: IBool64
    fIsOicf: IBool64
    fBufferValid: IBool64
    fHasMemoryValidateCallback: IBool64
    fInFree: IBool64
    fNeedMCCP: IBool64
    fUnused2: IBool64
    fUnused3: IBool64
    
    size_annotations(
        ('fInDontFree', 1),
        ('fDontCallFreeInst', 1),
        ('fUnused1', 1),
        ('fHasReturn', 1),
        ('fHasExtensions', 1),
        ('fHasNewCorrDesc', 1),
        ('fIsIn', 1),
        ('fIsOut', 1),
        ('fIsOicf', 1),
        ('fBufferValid', 1),
        ('fHasMemoryValidateCallback', 1),
        ('fInFree', 1),
        ('fNeedMCCP', 1),
        ('fUnused2', 3),
        ('fUnused3', 16)
    )
    
    dwDestContext: IUlong
    pvDestContext: IVoidPtrT
    
    SavedContextHandles: IDoublePtr[_NDR_SCONTEXT]
    
    ParamNumber: ILong
    
    pRpcChannelBuffer: IPointer[IRpcChannelBuffer]
    
    pArrayInfo: IPointer[ARRAY_INFO]
    SizePtrCountArray: PULONG
    SizePtrOffsetArray: PULONG
    SizePtrLengthArray: PULONG
    
    #
    # Interpreter argument queue.  Used on server side only.
    #
    pArgQueue: IVoidPtrT
    
    dwStubPhase: IUlong
    
    LowStackMark: IVoidPtrT
    
    #
    #  Async message pointer, correlation data - NT 5.0 features.
    #
    pAsyncMsg: IPointer[_NDR_ASYNC_MESSAGE]
    pCorrInfo: IPointer[_NDR_CORRELATION_INFO]
    pCorrMemory: IPointer[byte]
    
    pMemoryList: IVoidPtrT
    
    #
    #  Reserved fields up to this point present since the 3.50 release.
    #  Reserved fields below were introduced for Windows 2000 release.
    #  (but not used).
    #
    
    #
    # International character support information - NT 5.1 feature.
    #
    pCSInfo: IIntPtr
    
    ConformanceMark: IPointer[byte]
    VarianceMark: IPointer[byte]
    
    Unused: IIntPtr
    
    pContext: IPointer[_NDR_PROC_CONTEXT]
    
    #
    #  Reserved fields up to this point present since Windows 2000 release.
    #  Fields added for NT5.1
    #
    #  pUserMarshalList is used to keep a linked list of nodes pointing to
    #  marshalled data to be freed.  This list can contain (as the name
    #  implies) User Marshalled data, but also can contain Interface Pointer
    #  data.
    #
    
    ContextHandleHash: IVoidPtrT
    pUserMarshalList: IVoidPtrT
    pFullPtrFormat: IPointer[byte]
    Reserved51_4: IIntPtr
    Reserved51_5: IIntPtr
    
    #
    #  Reserved fields up to this point present since NT5.1 release.
    #
    
PMIDL_STUB_MESSAGE = MIDL_STUB_MESSAGE.PTR()

class MIDL_FORMAT_STRING(CStructure):
    _fields_ = [
        ('Pad', SHORT)
    ]
    
    Format: IPointer[byte]
    Pad: int
    
flexible_array(MIDL_FORMAT_STRING, 'Format', byte)

STUB_THUNK = WINAPI(VOID, PMIDL_STUB_MESSAGE)

SERVER_ROUTINE = WINAPI(LONG)

class MIDL_METHOD_PROPERTY(CStructure):
    _fields_ = [
        ('Id', ULONG),
        ('Value', ULONG_PTR)
    ]
    
    Value: int
    Id: int
    
PMIDL_METHOD_PROPERTY = MIDL_METHOD_PROPERTY.PTR()

class MIDL_METHOD_PROPERTY_MAP(CStructure):
    _fields_ = [
        ('Count', ULONG),
        ('Properties', PMIDL_METHOD_PROPERTY)
    ]
    
PMIDL_METHOD_PROPERTY_MAP = MIDL_METHOD_PROPERTY_MAP.PTR()

class MIDL_INTERFACE_METHOD_PROPERTIES(CStructure):
    _fields_ = [
        ('MethodCount', USHORT),
        ('MethodProperties', PMIDL_METHOD_PROPERTY_MAP)
    ]
    
    MethodProperties: IPointer[MIDL_METHOD_PROPERTY_MAP]
    MethodCount: int
    
class MIDL_SYNTAX_INFO(CStructure):
    """
    Multiple transfer syntax information.
    """
    _fields_ = [
        ('TransferSyntax', RPC_SYNTAX_IDENTIFIER),
        ('DispatchTable', PRPC_DISPATCH_TABLE),
        ('ProcString', PFORMAT_STRING),
        ('FmtStringOffset', PCUSHORT),
        ('TypeString', PFORMAT_STRING),
        ('aUserMarshalQuadruple', LPCVOID),
        ('pMethodProperties', MIDL_INTERFACE_METHOD_PROPERTIES.PTR()),
        ('pReserved2', ULONG_PTR)
    ]
    
    pMethodProperties: IPointer[MIDL_INTERFACE_METHOD_PROPERTIES]
    DispatchTable: IPointer[RPC_DISPATCH_TABLE]
    TransferSyntax: RPC_SYNTAX_IDENTIFIER
    aUserMarshalQuadruple: int
    FmtStringOffset: PCUSHORT
    ProcString: bytes
    TypeString: bytes
    pReserved2: int
    
PMIDL_SYNTAX_INFO = MIDL_SYNTAX_INFO.PTR()

class MIDL_SERVER_INFO(CStructure):
    """
    Server Interpreter's information strucuture.
    """
    _fields_ = [
        ('pStubDesc', PMIDL_STUB_DESC),
        ('DispatchTable', PTR(SERVER_ROUTINE)),
        ('ProcString', PFORMAT_STRING),
        ('FmtStringOffset', PCUSHORT),
        ('ThunkTable', PTR(STUB_THUNK)),
        ('pTransferSyntax', PRPC_SYNTAX_IDENTIFIER),
        ('nCount', ULONG_PTR),
        ('pSyntaxInfo', PMIDL_SYNTAX_INFO)
    ]
    
    pTransferSyntax: IPointer[RPC_SYNTAX_IDENTIFIER]
    pSyntaxInfo: IPointer[MIDL_SYNTAX_INFO]
    pStubDesc: IPointer[MIDL_STUB_DESC]
    DispatchTable: IPointer[FARPROC]
    ThunkTable: IPointer[FARPROC]
    FmtStringOffset: PCUSHORT
    ProcString: bytes
    nCount: int
    
PMIDL_SERVER_INFO = MIDL_SERVER_INFO.PTR()
    
class MIDL_STUBLESS_PROXY_INFO(CStructure):
    _fields_ = [
        ('pStubDesc', PMIDL_STUB_DESC),
        ('ProcFormatString', PFORMAT_STRING),
        ('FormatStringOffset', PCUSHORT),
        ('pTransferSyntax', PRPC_SYNTAX_IDENTIFIER),
        ('nCount', ULONG_PTR),
        ('pSyntaxInfo', PMIDL_SYNTAX_INFO)
    ]
    
    pTransferSyntax: IPointer[RPC_SYNTAX_IDENTIFIER]
    pSyntaxInfo: IPointer[MIDL_SYNTAX_INFO]
    pStubDesc: IPointer[MIDL_STUB_DESC]
    FormatStringOffset: PCUSHORT
    ProcFormatString: bytes
    nCount: int
    
PMIDL_STUBLESS_PROXY_INFO = MIDL_STUBLESS_PROXY_INFO.PTR()

class CLIENT_CALL_RETURN(CUnion):
    """
    This is the return value from NdrClientCall.
    """
    _fields_ = [
        ('Pointer', PVOID),
        ('Simple', LONG_PTR)
    ]
    
    Pointer: int
    Simple: int

#
# Different types of System Handles
#

SYSTEM_HANDLE_FILE = 0
SYSTEM_HANDLE_SEMAPHORE = 1
SYSTEM_HANDLE_EVENT = 2
SYSTEM_HANDLE_MUTEX = 3
SYSTEM_HANDLE_PROCESS = 4
SYSTEM_HANDLE_TOKEN = 5
SYSTEM_HANDLE_SECTION = 6
SYSTEM_HANDLE_REG_KEY = 7
SYSTEM_HANDLE_THREAD = 8
SYSTEM_HANDLE_COMPOSITION_OBJECT = 9
SYSTEM_HANDLE_SOCKET = 10
SYSTEM_HANDLE_JOB = 11
SYSTEM_HANDLE_PIPE = 12
SYSTEM_HANDLE_MAX = 12
SYSTEM_HANDLE_INVALID = 0xFF
system_handle_t = INT

#
# Interception info.
#

MidlInterceptionInfoVersionOne = 1

MidlWinrtTypeSerializationInfoVersionOne = 1

MIDL_WINRT_TYPE_SERIALIZATION_INFO_CURRENT_VERSION = MidlWinrtTypeSerializationInfoVersionOne

class MIDL_INTERCEPTION_INFO(CStructure):
    _fields_ = [
        ('Version', ULONG),
        ('ProcString', PFORMAT_STRING),
        ('ProcFormatOffsetTable', PCUSHORT),
        ('ProcCount', ULONG),
        ('TypeString', PFORMAT_STRING)
    ]
    
    ProcFormatOffsetTable: PCUSHORT
    ProcString: bytes
    TypeString: bytes
    ProcCount: int
    Version: int
    
PMIDL_INTERCEPTION_INFO = MIDL_INTERCEPTION_INFO.PTR()

class MIDL_WINRT_TYPE_SERIALIZATION_INFO(CStructure):
    _fields_ = [
        ('Version', ULONG),
        ('TypeFormatString', PFORMAT_STRING),
        ('FormatStringSize', USHORT),
        ('TypeOffset', USHORT),
        ('StubDesc', PMIDL_STUB_DESC)
    ]
    
    StubDesc: IPointer[MIDL_STUB_DESC]
    TypeFormatString: bytes
    FormatStringSize: int
    TypeOffset: int
    Version: int
    
PMIDL_WINRT_TYPE_SERIALIZATION_INFO = MIDL_WINRT_TYPE_SERIALIZATION_INFO.PTR()

# **************************************************************************
# ** New MIDL 2.0 Ndr routine templates
# **************************************************************************

@rpcrt_foreign(PRPC_CLIENT_INTERFACE, PULONG, PTR(PMIDL_SYNTAX_INFO))
def NdrClientGetSupportedSyntaxes(
    pInf: IPointer[RPC_CLIENT_INTERFACE],
    pCount: PULONG,
    pArr: IDoublePtr[MIDL_SYNTAX_INFO]) -> int: ...

@rpcrt_foreign(PRPC_SERVER_INTERFACE, PULONG, PTR(PMIDL_SYNTAX_INFO), PULONG)
def NdrServerGetSupportedSyntaxes(
    pInf: IPointer[RPC_SERVER_INTERFACE],
    pCount: PULONG,
    pArr: IDoublePtr[MIDL_SYNTAX_INFO],
    pPreferSyntaxIndex: PULONG) -> int: ...

#
# Marshall routines
#

@rpcrt4.foreign(VOID, PMIDL_STUB_MESSAGE, PTR(byte), byte)
def NdrSimpleTypeMarshall(
    pStubMsg: IPointer[MIDL_STUB_MESSAGE],
    pMemory: IPointer[byte],
    FormatChar: int): ...

# -------------------------
# -    Not Implemented    -
# -------------------------

# ... Functions