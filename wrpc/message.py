from win.minwindef import *

WRPC_VERSION_LAST = 0x0001

WRPC_M_RESPONSE = 0x01
WRPC_M_REQUEST  = 0x02

WRPC_SIGNATURE = b'WRPC'

WRPC_UDP_PACKET_MAXSIZE = 0xffff
WRPC_WAIT_TIME_QUANT = 0.00001

#
# WRPC message
#
# CHAR Signature[4] // "WRPC"
# WORD WRpcVersion // WRPC_VERSION_LAST
# BYTE MessageId // WRPC_M_RESPONSE / WRPC_M_REQUEST
# BYTE nExceptions
# DWORD cbData
# CHAR MarshalData[cbData]
#

class WRPC_MESSAGE(CStructure):
    _pack_ = 1
    
    _fields_ = [
        ('Signature', CHAR * 4), # b'WRPC'
        ('WRpcVersion', SHORT), # WRPC_VERSION_LAST
        ('MessageID', BYTE), # WRPC_M_RESPONSE, WRPC_M_REQUEST
        ('nExceptions', BYTE), 
        ('dwDataSize', DWORD)
    ]
    
    Signature: bytes
    WRpcVersion: int
    MessageID: int
    nExceptions: int
    dwDataSize: int
    
WRPC_SIZEOF_MESSAGE = WRPC_MESSAGE.size()
PWRPC_MESSAGE = WRPC_MESSAGE.PTR()

#
# Structure of WRPC_MARSHAL_ENTRY
#
# BYTE Type
# CHAR MarshalData[]
#

class WRPC_MARSHAL_ENTRY(CStructure):
    _fields_ = [('Type', BYTE)]
    Type: int

#
# WRPC marshal format for Int
#
# BYTE Type
# WORD cbDigits
# CHAR Digits[cbDigits]
#

WRPC_T_INT = 0x01

#
# WRPC marshal format for Str
#
# BYTE Type
# DWORD nChars
# CHAR Chars[nChars]
#

WRPC_T_STR = 0x02

#
# WRPC marshal format for Float
#
# BYTE Type
# DOUBLE Value
#

WRPC_T_FLOAT = 0x03

#
# WRPC marshal format for ByteArray
#
# BYTE Type
# BYTE BytearraySpecifier
# DWORD cbData
# CHAR Data[cbData]
#

WRPC_T_BYTEARRAY = 0x04
WRPC_BYTEARRAYSPEC_BYTEARRAY = 0x01
WRPC_BYTEARRAYSPEC_BYTES = 0x02

#
# WRPC marshal format for Complex
#
# BYTE Type
# DOUBLE Real
# DOUBLE Imag
#

WRPC_T_COMPLEX = 0x05

class WRPC_MARSHAL_DATA_COMPLEX(CStructure):
    _fields_ = [
        ('Real', DOUBLE),
        ('Imag', DOUBLE)
    ]
    
    Real: float
    Imag: float
    
PWRPC_MARSHAL_DATA_COMPLEX = PTR(WRPC_MARSHAL_DATA_COMPLEX)

#
# WRPC marshal format for Array
#
# BYTE Type
# BYTE ArraySpec
# DWORD dwEntries
# WRPC_MARSHAL_ENTRY Entries[dwEntries]
#

WRPC_T_ARRAY = 0x06
WRPC_ARRAYSPEC_TUPLE = 0x01
WRPC_ARRAYSPEC_LIST = 0x02
WRPC_ARRAYSPEC_SET = 0x03
WRPC_ARRAYSPEC_FROZENSET = 0x04

#
# WRPC marshal format for ExternalReferenceObject
#
# BYTE Type
# WORD RefModuleNameSize
# CHAR RefModuleName[RefModuleNameSize]
# WORD NameSize
# CHAR Name[NameSize]
#

WRPC_T_EXTERNAL = 0x07

#
# WRPC marshal format for ObjectRef
#
# BYTE Type
# PVOID ObjectRef
#

WRPC_T_OBJECTREF = 0x08

#
# WRPC marshal format for Dict
#
# BYTE Type
# DWORD dwPairs
# WRPC_MARSHAL_DATA_DICT_PAIR Pairs[]
#

#
# WRPC data format for WRPC_MARSHAL_DATA_DICT_PAIR
#
# WRPC_MARSHAL_ENTRY Key
# WRPC_MARSHAL_ENTRY Value
#

WRPC_T_DICT = 0x09

#
# WRPC marshal format for None
#
# BYTE Type
#

WRPC_T_NONE = 0x0A

#
# WRPC marshal format for Ellipsis
#
# BYTE Type
#

WRPC_T_ELLIPSIS = 0x0B

#
# WRPC marshal format for Bool
# 
# BYTE Type
# BOOLEAN Value
#

WRPC_T_BOOL = 0x0C

#
# WRPC marshal format for Int8
#
# BYTE Type
# INT8 Value
#

WRPC_T_INT8 = 0x0D

#
# WRPC marshal format for Int16
#
# BYTE Type
# INT16 Value
#

WRPC_T_INT16 = 0x0E

#
# WRPC marshal format for Int32
#
# BYTE Type
# INT32 Value
# 

WRPC_T_INT32 = 0x0F

#
# WRPC marshal format for EmptyArray
#
# BYTE Type
# BYTE ArraySpec
#

WRPC_T_EMPTYARRAY = 0x10

#
# WRPC marshal format for SmallFloat
#
# BYTE Type
# FLOAT Value
#

WRPC_T_SMALLFLOAT = 0x11

#
# WRPC marshal format for SmallComplex
#
# BYTE Type
# BYTE SmallSpec
# CHAR ComplexData[]
#

WRPC_T_SMALLCOMPLEX = 0x12
WRPC_SMALLSPEC_ALL = 0x01
WRPC_SMALLSPEC_REAL = 0x02
WRPC_SMALLSPEC_IMAG = 0x04

class WRPC_MARSHAL_DATA_SMALLCOMPLEX(CStructure):
    _pack_ = 1
    
    _fields_ = [
        ('Real', FLOAT),
        ('Imag', FLOAT)
    ]
    
    Real: float
    Imag: float
    
PWRPC_MARSHAL_DATA_SMALLCOMPLEX = PTR(WRPC_MARSHAL_DATA_SMALLCOMPLEX)
    
class WRPC_MARSHAL_DATA_SMALLCOMPLEX_REAL(CStructure):
    _pack_ = 1
    
    _fields_ = [
        ('Real', DOUBLE),
        ('Imag', FLOAT)
    ]
    
    Real: float
    Imag: float
    
PWRPC_MARSHAL_DATA_SMALLCOMPLEX_REAL = PTR(WRPC_MARSHAL_DATA_SMALLCOMPLEX_REAL)
    
class WRPC_MARSHAL_DATA_SMALLCOMPLEX_IMAG(CStructure):
    _pack_ = 1
    
    _fields_ = [
        ('Real', FLOAT),
        ('Imag', DOUBLE)
    ]
    
    Real: float
    Imag: float
    
PWRPC_MARSHAL_DATA_SMALLCOMPLEX_IMAG = PTR(WRPC_MARSHAL_DATA_SMALLCOMPLEX_IMAG)

#
# WRPC marshal format for MarshalReference
#
# BYTE Type
# WORD Id
#

WRPC_T_MARSHALREF = 0x13

#
# WRPC marshal format for MarshalExtension
#
# BYTE Type
# GUID Marshaller
# CHAR MarshalData[]
#

WRPC_T_MARSHALEXT = 0x14

#
# WRPC marshal format for Exception
#
# WORD TypeNameSize
# CHAR TypeName[]
# WORD TextSize
# CHAR Text[]
#

#
# WRPC marshal format for Request
#
# BYTE Type
# CHAR RequestData[]
#

#
# WRPC data format for GetAttribute request
#
# PVOID ObjectRef
# WORD AttributeSize
# CHAR Attribute[]
#

WRPC_RQ_T_GETATTR = 0x01 # t.k

#
# WRPC data format for SetAttribute request
#
# PVOID ObjectRef
# WORD AttributeSize
# CHAR Attribute[]
# WRPC_MARSHAL_ENTRY Value
#

WRPC_RQ_T_SETATTR = 0x02 # t.k = v

#
# WRPC data format for DelAttribute request
#
# PVOID ObjectRef
# WORD AttributeSize
# CHAR Attribute[]
#

WRPC_RQ_T_DELATTR = 0x03 # del t.k

#
# WRPC data format for BinaryOperator request
#
# PVOID ObjectRef
# BYTE OpType
# WRPC_MARSHAL_ENTRY Value
#

WRPC_RQ_T_BINOP = 0x04

WRPC_BINOP_ADD = 0x01 # +
WRPC_BINOP_SUB = 0x02 # -
WRPC_BINOP_DIV = 0x03 # /
WRPC_BINOP_FDIV = 0x04 # //
WRPC_BINOP_MUL = 0x05 # *
WRPC_BINOP_OR = 0x06 # |
WRPC_BINOP_AND = 0x07 # &
WRPC_BINOP_XOR = 0x08 # ^
WRPC_BINOP_RSHIFT = 0x09 # >>
WRPC_BINOP_LSHIFT = 0x10 # <<
WRPC_BINOP_IADD = 0x11 # +=
WRPC_BINOP_ISUB = 0x12 # -=
WRPC_BINOP_IDIV = 0x13 # /=
WRPC_BINOP_IFDIV = 0x14 # //=
WRPC_BINOP_IMUL = 0x15 # *=
WRPC_BINOP_IOR = 0x16 # |=
WRPC_BINOP_IAND = 0x17 # &=
WRPC_BINOP_IXOR = 0x18 # ^=
WRPC_BINOP_IRSHIFT = 0x19 # >>=
WRPC_BINOP_ILSHIFT = 0x20 # <<=
WRPC_BINOP_MOD = 0x21 # %
WRPC_BINOP_IMOD = 0x22 # %=
WRPC_BINOP_EQ = 0x23 # ==
WRPC_BINOP_NEQ = 0x24 # !=

#
# WRPC data format for UnaryOperator request
#
# PVOID ObjectRef
# BYTE OpType
#

WRPC_RQ_T_UNARYOP = 0x05

WRPC_UNARYOP_POS = 0x01 # +t
WRPC_UNARYOP_NEG = 0x02 # -t
WRPC_UNARYOP_INV = 0x03 # ~t
WRPC_UNARYOP_ABS = 0x04 # abs(t)
WRPC_UNARYOP_BOOL = 0x05 # bool(t)
WRPC_UNARYOP_INT = 0x06 # int(t)
WRPC_UNARYOP_STR = 0x07 # str(t)
WRPC_UNARYOP_REPR = 0x08 # repr(t)

#
# WRPC data format for CallRef request
#
# PVOID ObjectRef
# WRPC_MARSHAL_ENTRY Args
# WRPC_MARSHAL_ENTRY Kwargs
#

WRPC_RQ_T_CALLREF = 0x06 # t(*args, **kwargs)

#
# WRPC data format for AddRef request
#
# PVOID ObjectRef
#

WRPC_RQ_T_ADDREF = 0x07

#
# WRPC data format for Release request
#
# PVOID ObjectRef
#

WRPC_RQ_T_RELEASE = 0x08

#
# WRPC data format for Call request
#
# PVOID ObjectRef
# WORD AttributeSize
# CHAR Attribute[]
# WRPC_MARSHAL_ENTRY Args
# WRPC_MARSHAL_ENTRY Kwargs
#

WRPC_RQ_T_CALL = 0x07 # t.k(*args, **kwargs)

class WRPCUtils:
    @staticmethod
    def get_marshal_data(buffer: bytes, message: WRPC_MESSAGE) -> bytes:
        return buffer[WRPC_SIZEOF_MESSAGE:WRPC_SIZEOF_MESSAGE+message.dwDataSize]
    
    @staticmethod
    def message(message_id: int) -> WRPC_MESSAGE:
        message = WRPC_MESSAGE()
        message.Signature = WRPC_SIGNATURE
        message.WRpcVersion = WRPC_VERSION_LAST
        message.MessageID = message_id
        return message
    
    @staticmethod
    def obj_request(rq_type: int, obj: int) -> bytes:
        buffer = bytes(BYTE(rq_type))
        buffer += bytes(PVOID(obj))
        return buffer