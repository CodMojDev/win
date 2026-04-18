
from win.abs.pipe.handle import *

from .message import *
from .marshal import *

import threading
import random
import socket
import errno
import time

from win.wet.trace import *

wudp = WET_PROVIDER('WRPC-UDP')

WRPC_PROTOCOL_PREF_UDP = 0x01
WRPC_PROTOCOL_PREF_TCP = 0x02
WRPC_PROTOCOL_PREF_NP = 0x04

class IWRPCHost(IInterface):
    ...

class IWRPCProtocol(IInterface):
    def get_preferences(self) -> int:
        """
        Get WRPC protocol preferences.
        """
    
    def read_message(self) -> tuple[WRPC_MESSAGE, bytes]:
        """
        Read the message from protocol transport layer.
        """
        
    def write_message(self, message: WRPC_MESSAGE, marshal_data: bytes):
        """
        Write the message to protocol transport layer.
        """
        
    def alive(self) -> bool:
        """
        Check WRPC protocol instance is alive.
        """
        
    def wait(self) -> tuple[WRPC_MESSAGE, bytes]:
        """
        Wait for response arrived and get it.
        """

class WRPCUDPHost(IWRPCHost):
    """
    WRPC Host Implementation for UDP.
    """
    
    sock: socket.socket
    port: int
    ip: str
    
    response: tuple[WRPC_MESSAGE, bytes]
    waiting_response: bool
    pending: dict
    
    hold_list: list[object]
    
    def __init__(self, ip: str = '127.0.0.1', port: int = None):
        if port is None:
            port = random.randint(10000, 49151)
        
        self.port = port
        self.ip = ip
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._bind()
        
        self.waiting_response = False
        self.response = None
        self.hold_list = []
        self.pending = {}
        
        self.worker = threading.Thread(target=self._worker, name='WRPC UDP Worker')
        self.worker.start()
                
    def _bind(self):
        try:
            self.sock.bind((self.ip, self.port))
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                self.port = random.randint(10000, 49151)
                self._bind()
            else:
                raise e from None
    
    def _worker(self):
        while True:
            data, client_address = self.sock.recvfrom(WRPC_UDP_PACKET_MAXSIZE)
            if client_address not in self.pending:
                self.pending[client_address] = (False, None)
            message = i_cast(data, PWRPC_MESSAGE).contents
            if message.Signature != WRPC_SIGNATURE:
                self._send_exception_packet(client_address, (WRPCProtocolException('Invalid WRPC Signature.'),))
                continue
            if message.MessageID == WRPC_M_REQUEST:
                if message.nExceptions != 0:
                    self._send_exception_packet(client_address, (WRPCProtocolException('Invalid WRPC Message. Exception count != 0.'),))
                    continue
                self.waiting_response = True
                response = WRPCUtils.message(WRPC_M_RESPONSE)
                rq_data = WRPCUtils.get_marshal_data(data, message)
                try:
                    buffer = self._request(rq_data)
                    response.dwDataSize = len(buffer)
                    buffer = bytes(response) + buffer
                    self.sock.sendto(buffer, client_address)
                except BaseException as e:
                    self._send_exception_packet(client_address, (e,))
            elif message.MessageID == WRPC_M_RESPONSE:
                if message.nExceptions != 0:
                    marshal_data = WRPCUtils.get_marshal_data(data, message)
                    for _ in range(message.nExceptions):
                        stm = Stream(marshal_data)
                        type_name = stm.read(stm.read_word()).decode('utf-8')
                        text = stm.read(stm.read_word()).decode('utf-8')
                        dbg_trace(wudp, f'\n[WRPC Expection] {type_name}: {text}')
                    continue
                
                if not self.waiting_response:
                    self._send_exception_packet(client_address, (WRPCProtocolException('Unexpected WRPC Response Message.'),))
                    continue
                self.waiting_response = False
                marshal_data = WRPCUtils.get_marshal_data(data, message)
                self.response = (message, marshal_data)
            else:
                self._send_exception_packet(client_address, (WRPCProtocolException(f'Invalid WRPC Message ID {hex(message.MessageID)}.'),))
                continue
            
    def _request(self, rq_data: bytes) -> bytes:
        stream = Stream(rq_data)
        stream.protocol = self
        bType = stream.read_byte()
        
        if bType == WRPC_RQ_T_GETATTR:
            obj = PtrUtil.to_python(stream.read_pvoid())
            attributeSize = stream.read_word()
            attribute = stream.read(attributeSize).decode('utf-8')
            dbg_trace(wudp, f'Get attr "{attribute}" of object "{obj}"')
            return WRPC.marshal(getattr(obj, attribute), udp=True)
        elif bType == WRPC_RQ_T_SETATTR:
            obj = PtrUtil.to_python(stream.read_pvoid())
            attributeSize = stream.read_word()
            attribute = stream.read(attributeSize).decode('utf-8')
            value = WRPC.unmarshal(stream)
            dbg_trace(wudp, f'Set attr "{attribute}" of object "{obj}"')
            setattr(obj, attribute, value)
            return b''
        elif bType == WRPC_RQ_T_CALLREF:
            obj = PtrUtil.to_python(stream.read_pvoid())
            args = WRPC.unmarshal(stream)
            kwargs = WRPC.unmarshal(stream)
            return WRPC.marshal(obj(*args, **kwargs), udp=True)
        elif bType == WRPC_RQ_T_DELATTR:
            obj = PtrUtil.to_python(stream.read_pvoid())
            attributeSize = stream.read_word()
            attribute = stream.read(attributeSize).decode('utf-8')
            delattr(obj, attribute)
            return b''
        elif bType == WRPC_RQ_T_ADDREF:
            obj = PtrUtil.to_python(stream.read_pvoid())
            dbg_trace(wudp, f'"{obj}" Add ref')
            self.hold_list.append(obj)
            return b''
        elif bType == WRPC_RQ_T_RELEASE:
            obj = PtrUtil.to_python(stream.read_pvoid())
            dbg_trace(wudp, f'"{obj}" Release ref')
            self.hold_list.remove(obj)
            return b''
        elif bType == WRPC_RQ_T_UNARYOP:
            obj = PtrUtil.to_python(stream.read_pvoid())
            optype = stream.read_byte()
            if optype == WRPC_UNARYOP_POS:
                result = +obj
            elif optype == WRPC_UNARYOP_NEG:
                result = -obj
            elif optype == WRPC_UNARYOP_INV:
                result = ~obj
            elif optype == WRPC_UNARYOP_BOOL:
                result = bool(obj)
            elif optype == WRPC_UNARYOP_REPR:
                result = repr(obj)
            elif optype == WRPC_UNARYOP_STR:
                result = str(obj)
            elif optype == WRPC_UNARYOP_INT:
                result = int(obj)
            elif optype == WRPC_UNARYOP_ABS:
                result = abs(obj)
            return WRPC.marshal(result, udp=True)
        elif bType == WRPC_RQ_T_BINOP:
            obj = PtrUtil.to_python(stream.read_pvoid())
            optype = stream.read_byte()
            arg = WRPC.unmarshal(stream)
            if optype == WRPC_BINOP_ADD:
                result = obj + arg
            elif optype == WRPC_BINOP_SUB:
                result = obj - arg
            elif optype == WRPC_BINOP_DIV:
                result = obj / arg
            elif optype == WRPC_BINOP_FDIV:
                result = obj // arg
            elif optype == WRPC_BINOP_MUL:
                result = obj * arg
            elif optype == WRPC_BINOP_AND:
                result = obj & arg
            elif optype == WRPC_BINOP_OR:
                result = obj | arg
            elif optype == WRPC_BINOP_XOR:
                result = obj ^ arg
            elif optype == WRPC_BINOP_RSHIFT:
                result = obj >> arg
            elif optype == WRPC_BINOP_LSHIFT:
                result = obj << arg
            elif optype == WRPC_BINOP_EQ:
                result = obj == arg
            elif optype == WRPC_BINOP_NEQ:
                result = obj != arg
            elif optype == WRPC_BINOP_IADD:
                result = obj.__iadd__(arg)
            elif optype == WRPC_BINOP_ISUB:
                result = obj.__isub__(arg)
            elif optype == WRPC_BINOP_IDIV:
                result = obj.__itruediv__(arg)
            elif optype == WRPC_BINOP_IFDIV:
                result = obj.__ifloordiv__(arg)
            elif optype == WRPC_BINOP_IMUL:
                result = obj.__imul__(arg)
            elif optype == WRPC_BINOP_IAND:
                result = obj.__iand__(arg)
            elif optype == WRPC_BINOP_IOR:
                result = obj.__ior__(arg)
            elif optype == WRPC_BINOP_IXOR:
                result = obj.__ixor__(arg)
            elif optype == WRPC_BINOP_ILSHIFT:
                result = obj.__ilshift__(arg)
            elif optype == WRPC_BINOP_IRSHIFT:
                result = obj.__irshift__(arg)
            elif optype == WRPC_BINOP_IMOD:
                result = obj.__imod__(arg)
            elif optype == WRPC_BINOP_MOD:
                result = obj % arg
            return WRPC.marshal(result, udp=True)
                
    def _send_exception_packet(self, client_address,
                               exceptions: list[BaseException]):
        message = WRPCUtils.message(WRPC_M_RESPONSE)
        message.nExceptions = len(exceptions)
        marshal_data = b''
        
        for exception in exceptions:
            type_name = type(exception).__qualname__
            marshal_data += bytes(WORD(len(type_name)))
            marshal_data += type_name.encode('utf-8')
            text = str(exception)
            marshal_data += bytes(WORD(len(text)))
            marshal_data += text.encode('utf-8')
            
        message.dwDataSize = len(marshal_data)
        self.sock.sendto(bytes(message) + marshal_data, client_address)
    
class WRPCUDP(IWRPCProtocol):
    """
    WRPC Protocol Implementation for UDP.
    """
    
    host: WRPCUDPHost
    alive_state: bool
    port: int
    ip: str
    
    def __init__(self, port: int, host: WRPCUDPHost, ip: str = '127.0.0.1'):
        if not isinstance(host, WRPCUDPHost):
            raise TypeError(type(host))
        
        self.alive_state = True
        self.host = host
        self.port = port
        self.ip = ip
        
    def write_message(self, message, marshal_data):
        if message.MessageID == WRPC_M_REQUEST:
            self.host.waiting_response = True
        self.host.sock.sendto(bytes(message) + marshal_data, (self.ip, self.port))
    
    def get_preferences(self):
        return WRPC_PROTOCOL_PREF_UDP
        
    def wait(self) -> tuple[WRPC_MESSAGE, bytes]:
        while self.host.response is None:
            time.sleep(WRPC_WAIT_TIME_QUANT)
        response = self.host.response
        self.host.response = None
        return response
    
    def alive(self):
        return self.alive_state

class WRPCNP(IWRPCProtocol):
    """
    WRPC Protocol Implementation for named pipes.
    """
    
    pipe: Pipe
    
    def __init__(self, pipe: str):
        self.pipe = Pipe(pipe)
        
        
    def open(self, pipe: str):
        self.pipe = Pipe(pipe)