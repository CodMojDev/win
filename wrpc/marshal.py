from win.com.guid import *
from .message import *
from .stream import *
from .errors import *

import typing
import types

LPDOUBLE = PTR(DOUBLE)
LPFLOAT = PTR(FLOAT)

class IWRPCMarshal(IInterface):
    _iid_: typing.ClassVar[IID]
    
    @interface_abstract_method
    def marshal(self) -> bytes:
        """
        Marshal object into buffer.
        """
    
    @interface_abstract_method
    @classmethod
    def unmarshal(self, stream: Stream) -> Any:
        """
        Unmarshal marshalled object on stream into Python object.
        """

class _WRPCState:
    __slots__ = ['registry']
    
    registry: dict[bytes, IWRPCMarshal]
    
    def __init__(self):
        self.registry = {}
        
_wrpc_state = _WRPCState()

class WRPC:
    class Context:
        marshal_cache: list[object]
        
        def __init__(self):
            self.marshal_cache = []
    
    @staticmethod
    def get(iid: GUID | bytes) -> IWRPCMarshal:
        if isinstance(iid, GUID):
            iid = bytes(iid)
        return _wrpc_state.registry[iid]
    
    @staticmethod
    def add(marshaller: IWRPCMarshal):
        iid = bytes(marshaller._iid_)
        if iid in _wrpc_state.registry:
            raise KeyError(f'Marshaller {marshaller.__qualname__} already exists.')
        _wrpc_state.registry[iid] = marshaller
    
    @staticmethod
    def marshal(value: object, udp: bool = False, ctx: 'WRPC.Context' = None) -> bytes:
        if ctx is None:
            ctx = WRPC.Context()
        
        if value is None:
            ctx.marshal_cache.append(value)
            return bytes(BYTE(WRPC_T_NONE))
        elif value is (...):
            ctx.marshal_cache.append(value)
            return bytes(BYTE(WRPC_T_ELLIPSIS))
        
        value_t = type(value)
        if value_t is int:
            ivalue: int = value
            if value > 2147483647 or value < -2147483648:
                if value in ctx.marshal_cache:
                    buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                    buffer += bytes(WORD(ctx.marshal_cache.index(value)))
                else:
                    buffer = bytes(BYTE(WRPC_T_INT))
                    digits = ivalue.to_bytes((ivalue.bit_length() + 7) // 8, 'big', signed=True)
                    buffer += bytes(WORD(len(digits)))
                    buffer += digits
            else:
                if value < 127 and value > -128:
                    buffer = bytes(BYTE(WRPC_T_INT8))
                    buffer += bytes(INT8(ivalue))
                elif value < 32767 and value > -32767:
                    buffer = bytes(BYTE(WRPC_T_INT16))
                    buffer += bytes(INT16(ivalue))
                else:
                    buffer = bytes(BYTE(WRPC_T_INT32))
                    buffer += bytes(INT32(ivalue))
        elif value_t is str:
            if value in ctx.marshal_cache:
                buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                buffer += bytes(WORD(ctx.marshal_cache.index(value)))
            else:
                svalue: str = value
                buffer = bytes(BYTE(WRPC_T_STR))
                buffer += bytes(DWORD(len(svalue)))
                buffer += svalue.encode('utf-8')
        elif value_t is float:
            fvalue: float = value
            if FLOAT(fvalue).value == fvalue:
                buffer = bytes(BYTE(WRPC_T_SMALLFLOAT))
                buffer += bytes(FLOAT(fvalue))
            else:
                buffer = bytes(BYTE(WRPC_T_FLOAT))
                buffer += bytes(DOUBLE(fvalue))
        elif value_t in (bytes, bytearray):
            bvalue: bytes = value
            buffer = bytes(BYTE(WRPC_T_BYTEARRAY))
            if value_t is bytearray:
                buffer += bytes(BYTE(WRPC_BYTEARRAYSPEC_BYTEARRAY))
            else:
                buffer += bytes(BYTE(WRPC_BYTEARRAYSPEC_BYTES))
            buffer += bytes(DWORD(len(bvalue)))
            buffer += bvalue
        elif value_t is complex:
            cvalue: complex = value
            real, imag = cvalue.real, cvalue.imag
            if FLOAT(real).value == real:
                buffer = bytes(BYTE(WRPC_T_SMALLCOMPLEX))
                buffer += bytes(FLOAT(real))
                if FLOAT(imag).value == imag:
                    buffer += bytes(BYTE(WRPC_SMALLSPEC_ALL))
                    buffer += bytes(FLOAT(imag))
                else:
                    buffer += bytes(BYTE(WRPC_SMALLSPEC_REAL))
                    buffer += bytes(DOUBLE(imag))
            elif FLOAT(imag).value == imag:
                buffer = bytes(BYTE(WRPC_T_SMALLCOMPLEX))
                buffer += bytes(BYTE(WRPC_SMALLSPEC_IMAG))
                buffer += bytes(DOUBLE(imag))
                buffer += bytes(FLOAT(imag))
            else:
                buffer = bytes(BYTE(WRPC_T_COMPLEX))
                buffer += bytes(DOUBLE(real))
                buffer += bytes(DOUBLE(imag))
        elif value_t in (list, tuple, set, frozenset):
            avalue: list | tuple = value
            empty = not value
            fully = not empty
            if fully and value in ctx.marshal_cache:
                buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                buffer += bytes(WORD(ctx.marshal_cache.index(value)))
            else:
                if empty:
                    buffer = bytes(BYTE(WRPC_T_EMPTYARRAY))
                else:
                    buffer = bytes(BYTE(WRPC_T_ARRAY))
                if value_t is list:
                    buffer += bytes(BYTE(WRPC_ARRAYSPEC_LIST))
                elif value_t is set:
                    buffer += bytes(BYTE(WRPC_ARRAYSPEC_SET))
                elif value_t is frozenset:
                    buffer += bytes(BYTE(WRPC_ARRAYSPEC_FROZENSET))
                else:
                    buffer += bytes(BYTE(WRPC_ARRAYSPEC_TUPLE))
                if fully:
                    buffer += bytes(DWORD(len(avalue)))
                    for i in avalue:
                        buffer += WRPC.marshal(i, ctx=ctx)
        elif value_t is types.BuiltinFunctionType:
            if value in ctx.marshal_cache:
                buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                buffer += bytes(WORD(ctx.marshal_cache.index(value)))
            else:
                bfvalue: types.BuiltinFunctionType = value
                buffer = bytes(BYTE(WRPC_T_EXTERNAL))
                module_name = bfvalue.__module__
                buffer += bytes(WORD(len(module_name)))
                buffer += module_name.encode('ascii')
                name = bfvalue.__name__
                buffer += bytes(WORD(len(name)))
                buffer += name.encode('ascii')
        elif value_t is dict:
            if value in ctx.marshal_cache:
                buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                buffer += bytes(WORD(ctx.marshal_cache.index(value)))
            else:
                dvalue: dict = value
                buffer = bytes(BYTE(WRPC_T_DICT))
                items = dvalue.items()
                buffer += bytes(DWORD(len(dvalue)))
                for k, v in items:
                    buffer += WRPC.marshal(k, ctx=ctx)
                    buffer += WRPC.marshal(v, ctx=ctx)
        elif value_t is bool:
            buffer = bytes(BYTE(WRPC_T_BOOL))
            buffer += bytes(BOOLEAN(value))
        elif isinstance(value, IWRPCMarshal):
            buffer = bytes(BYTE(WRPC_T_MARSHALEXT))
            buffer += bytes(value._iid_)
            buffer += value.marshal()
        else:
            if value in ctx.marshal_cache:
                buffer = bytes(BYTE(WRPC_T_MARSHALREF))
                buffer += bytes(WORD(ctx.marshal_cache.index(value)))
            else:
                buffer = bytes(BYTE(WRPC_T_OBJECTREF))
                buffer += bytes(PVOID(id(value)))
        if udp and len(buffer) > WRPC_UDP_PACKET_MAXSIZE:
            buffer = bytes(BYTE(WRPC_T_OBJECTREF))
            buffer += bytes(PVOID(id(value)))
        
        ctx.marshal_cache.append(value)
            
        return buffer
    
    @staticmethod
    def unmarshal(stream: Stream, ctx: 'WRPC.Context' = None) -> object:
        if ctx is None:
            ctx = WRPC.Context()
        
        bType = stream.read_byte()
        
        if bType == WRPC_T_INT:
            cbDigits = stream.read_word()
            digits = stream.read(cbDigits)
            integer = int.from_bytes(digits, 'big', signed=True)
            ctx.marshal_cache.append(integer)
            return integer
        elif bType == WRPC_T_STR:
            nChars = stream.read_dword()
            string = stream.read(nChars).decode('utf-8')
            ctx.marshal_cache.append(string)
            return string
        elif bType == WRPC_T_FLOAT:
            dataIEEE = stream.read(8)
            floatValue = i_cast(dataIEEE, LPDOUBLE).contents.value
            ctx.marshal_cache.append(floatValue)
            return floatValue 
        elif bType == WRPC_T_BYTEARRAY:
            bByteArraySpec = stream.read_byte()
            cbData = stream.read_dword()
            data = stream.read(cbData)
            if bByteArraySpec == WRPC_BYTEARRAYSPEC_BYTEARRAY:
                data = bytearray(data)
            ctx.marshal_cache.append(None)
            return data
        elif bType == WRPC_T_COMPLEX:
            marshalBuffer = stream.read(16)
            marshalEntry = i_cast(marshalBuffer, PWRPC_MARSHAL_DATA_COMPLEX).contents
            ctx.marshal_cache.append(None)
            return complex(marshalEntry.Real, marshalEntry.Imag)
        elif bType == WRPC_T_ARRAY:
            bArraySpec = stream.read_byte()
            dwEntries = stream.read_dword()
            
            output = []
            for _ in range(dwEntries):
                output.append(WRPC.unmarshal(stream, ctx=ctx))
                
            if bArraySpec == WRPC_ARRAYSPEC_TUPLE:
                output = tuple(output)
            elif bArraySpec == WRPC_ARRAYSPEC_SET:
                output = set(output)
            elif bArraySpec == WRPC_ARRAYSPEC_FROZENSET:
                output = frozenset(output)
                
            ctx.marshal_cache.append(output)
            
            return output
        elif bType == WRPC_T_EXTERNAL:
            refModuleNameSize = stream.read_word()
            refModuleName = stream.read(refModuleNameSize).decode('ascii')
            nameSize = stream.read_word()
            name = stream.read(nameSize).decode('ascii')
            module = __import__(refModuleName)
            external = getattr(module, name)
            ctx.marshal_cache.append(external)
            return external
        elif bType == WRPC_T_OBJECTREF:
            pyObject = stream.read_pvoid()
            if stream.protocol is None:
                obj = PtrUtil.to_python(pyObject)
                ctx.marshal_cache.append(obj)
                return obj
            obj = WRPCProxyObject(stream.protocol, pyObject)
            ctx.marshal_cache.append(obj)
            return obj
        elif bType == WRPC_T_DICT:
            dictionary = {}
            dwPairs = stream.read_dword()
            for _ in range(dwPairs):
                key = WRPC.unmarshal(stream, ctx=ctx)
                value = WRPC.unmarshal(stream, ctx=ctx)
                dictionary[key] = value
            ctx.marshal_cache.append(dictionary)
            return dictionary
        elif bType == WRPC_T_NONE:
            ctx.marshal_cache.append(None)
            return None
        elif bType == WRPC_T_BOOL:
            ctx.marshal_cache.append(None)
            return stream.read_byte() != FALSE
        elif bType == WRPC_T_INT8:
            ctx.marshal_cache.append(None)
            integer = stream.read_byte()
            if integer >= 128:
                return integer - 256
            return integer
        elif bType == WRPC_T_INT16:
            ctx.marshal_cache.append(None)
            integer = stream.read_word()
            if integer >= 32768:
                return integer - 65536
            return integer
        elif bType == WRPC_T_INT32:
            ctx.marshal_cache.append(None)
            integer = stream.read_dword()
            if integer >= 2147483648:
                return integer - 4294967296
            return integer
        elif bType == WRPC_T_EMPTYARRAY:
            ctx.marshal_cache.append(None)
            bArraySpec = stream.read_byte()
            if bArraySpec == WRPC_ARRAYSPEC_TUPLE:
                return ()
            elif bArraySpec == WRPC_ARRAYSPEC_SET:
                return set()
            elif bArraySpec == WRPC_ARRAYSPEC_FROZENSET:
                return frozenset()
            return []
        elif bType == WRPC_T_SMALLFLOAT:
            ctx.marshal_cache.append(None)
            dataIEEE = stream.read(4)
            return i_cast(dataIEEE, LPFLOAT).contents.value
        elif bType == WRPC_T_SMALLCOMPLEX:
            ctx.marshal_cache.append(None)
            bSmallSpec = stream.read_byte()
            if bSmallSpec == WRPC_SMALLSPEC_REAL:
                smallComplexBuffer = stream.read(12)
                smallComplex = i_cast(smallComplexBuffer, PWRPC_MARSHAL_DATA_SMALLCOMPLEX_REAL).contents
                return complex(smallComplex.Real, smallComplex.Imag)
            elif bSmallSpec == WRPC_SMALLSPEC_IMAG:
                smallComplexBuffer = stream.read(12)
                smallComplex = i_cast(smallComplexBuffer, PWRPC_MARSHAL_DATA_SMALLCOMPLEX_IMAG).contents
                return complex(smallComplex.Real, smallComplex.Imag)
            elif bSmallSpec == WRPC_SMALLSPEC_ALL:
                smallComplexBuffer = stream.read(8)
                smallComplex = i_cast(smallComplexBuffer, PWRPC_MARSHAL_DATA_SMALLCOMPLEX).contents
                return complex(smallComplex.Real, smallComplex.Imag)
        elif bType == WRPC_T_MARSHALREF:
            wId = stream.read_word()
            value = ctx.marshal_cache[wId]
            ctx.marshal_cache.append(value)
            return value
        elif bType == WRPC_T_MARSHALEXT:
            guid = stream.read(16)
            marshaller = _wrpc_state.registry[guid]
            return marshaller.unmarshal(stream)

WRPC_PROTOCOL_PREF_UDP = 0x01
WRPC_PROTOCOL_PREF_TCP = 0x02
WRPC_PROTOCOL_PREF_NP = 0x04

class WRPCProxyObject:
    protocol: 'IWRPCProtocol'
    obj: int
    
    def __init__(self, protocol: 'IWRPCProtocol', obj: int):
        i_setattr(self, 'protocol', protocol)
        i_setattr(self, 'obj', obj)
        
        message = WRPCUtils.message(WRPC_M_REQUEST)
        rq_data = WRPCUtils.obj_request(WRPC_RQ_T_ADDREF, obj)
        message.dwDataSize = len(rq_data)
        
        protocol: IWRPCProtocol = i_getattr(self, 'protocol')
        protocol.write_message(message, rq_data)
        protocol.wait()
    
    def __getattribute__(self, attribute: str) -> object:
        protocol: IWRPCProtocol = i_getattr(self, 'protocol')
        
        if not protocol.alive():
            raise WRPCException('WRPC Protocol is destroyed but trying to use proxy object referring to destroyed protocol.')
        
        message = WRPCUtils.message(WRPC_M_REQUEST)
        rq_data = WRPCUtils.obj_request(WRPC_RQ_T_GETATTR, i_getattr(self, 'obj'))
        rq_data += bytes(WORD(len(attribute)))
        rq_data += attribute.encode('utf-8')
        message.dwDataSize = len(rq_data)
        
        protocol.write_message(message, rq_data)
        stm = Stream(protocol.wait()[1])
        stm.protocol = protocol
        return WRPC.unmarshal(stm)
        
    def __setattr__(self, attribute: str, value: object):
        protocol: IWRPCProtocol = i_getattr(self, 'protocol')
        
        if not protocol.alive():
            raise WRPCException('WRPC Protocol is destroyed but trying to use proxy object referring to destroyed protocol.')
        
        message = WRPCUtils.message(WRPC_M_REQUEST)
        rq_data = WRPCUtils.obj_request(WRPC_RQ_T_SETATTR, i_getattr(self, 'obj'))
        rq_data += bytes(WORD(len(attribute)))
        rq_data += attribute.encode('utf-8')
        udp = protocol.get_preferences() & WRPC_PROTOCOL_PREF_UDP != 0
        rq_data += WRPC.marshal(value, udp=udp)
        message.dwDataSize = len(rq_data)
        
        protocol.write_message(message, rq_data)
        protocol.wait()
        
    def __call__(self, *args, **kwargs):
        protocol: IWRPCProtocol = i_getattr(self, 'protocol')
        
        if not protocol.alive():
            raise WRPCException('WRPC Protocol is destroyed but trying to use proxy object referring to destroyed protocol.')
        
        message = WRPCUtils.message(WRPC_M_REQUEST)
        rq_data = WRPCUtils.obj_request(WRPC_RQ_T_CALLREF, i_getattr(self, 'obj'))
        
        udp = protocol.get_preferences() & WRPC_PROTOCOL_PREF_UDP != 0
        rq_data += WRPC.marshal(args, udp=udp)
        rq_data += WRPC.marshal(kwargs, udp=udp)
        message.dwDataSize = len(rq_data)
        
        protocol.write_message(message, rq_data)
        stm = Stream(protocol.wait()[1])
        stm.protocol = protocol
        return WRPC.unmarshal(stm)
        
    def __del__(self):
        protocol: IWRPCProtocol = i_getattr(self, 'protocol')
        
        if not protocol.alive():
            return
        
        message = WRPCUtils.message(WRPC_M_REQUEST)
        rq_data = WRPCUtils.obj_request(WRPC_RQ_T_RELEASE, i_getattr(self, 'obj'))
        message.dwDataSize = len(rq_data)
        
        protocol.write_message(message, rq_data)
        protocol.wait()