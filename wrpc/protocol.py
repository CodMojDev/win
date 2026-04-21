
from win.abs.pipe.handle import *

from .message import *
from .marshal import *

import threading
import random
import socket
import errno
import time

from win.wet.trace import *
from win.inaddr import *

wudp = WET_PROVIDER('WRPC-UDP')

WRPC_PROTOCOL_PREF_UDP = 0x01
WRPC_PROTOCOL_PREF_TCP = 0x02
WRPC_PROTOCOL_PREF_NP = 0x04

class IWRPCHost(IInterface):
    def get_preferences(self) -> int:
        """
        Get WRPC protocol preferences.
        """

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
        
    def wait(self, timeout: Optional[float] = None) -> tuple[WRPC_MESSAGE, bytes]:
        """
        Wait for response arrived and get it.
        """
        
    def destroy(self):
        """
        Destroy the protocol.
        """
        
    def host_stopped(self, soft: bool, *args):
        """
        On host stopped.
        """

class WRPCUDPHost(IWRPCHost):
    """
    WRPC Host Implementation for UDP.
    """
    
    sock: socket.socket
    port: int
    ip: str
    
    response: tuple[WRPC_MESSAGE, bytes]
    connected: list[tuple[str, int]]
    protocols: list[IWRPCProtocol]
    waiting_response: bool
    global_data: list[Any]
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
        self.global_data = []
        self.response = None
        self.hold_list = []
        self.protocols = []
        self.pending = {}
        self.alive = True
        
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
        while self.alive:
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
                    stm = Stream(marshal_data)
                    for type_name, text in WRPC.unmarshal_exceptions(stm, message.nExceptions):
                        dbg_trace(wudp, f'[WRPC Expection] {type_name}: {text}')
                    continue
                
                if not self.waiting_response:
                    self._send_exception_packet(client_address, (WRPCProtocolException('Unexpected WRPC Response Message.'),))
                    continue
                
                dbg_trace(wudp, 'WRPC Response received')
                self.waiting_response = False
                marshal_data = WRPCUtils.get_marshal_data(data, message)
                self.response = (message, marshal_data)
            elif message.MessageID == WRPC_M_SIGNAL:
                if message.nExceptions != 0:
                    self._send_exception_packet(client_address, (WRPCProtocolException('Invalid WRPC Message. Exception count != 0.'),))
                    continue
                
                marshal_data = WRPCUtils.get_marshal_data(data, message)
                
                stm = Stream(marshal_data)
                bSignal = stm.read_byte()
                
                # Stop signal received
                if bSignal == WRPC_SIG_STOP:
                    bSoft = stm.read_byte()
                    wPreferences = stm.read_word()
                    
                    # Stopping server is UDP
                    if wPreferences & WRPC_PROTOCOL_PREF_UDP:
                        ip = socket.inet_ntoa(stm.read(4))
                        port = stm.read_word()
                        
                        # Destroy the connected to stopped server protocols
                        for protocol in self.protocols:
                            protocol.host_stopped(bool(bSoft), ip, port)
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
            got = getattr(obj, attribute)
            dbg_trace(wudp, f'Get attr "{attribute}" of object "{obj}" => "{got}"')
            return WRPC.marshal(got, udp=True)
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
            dbg_trace(wudp, f'AddRef "{obj}"')
            self.hold_list.append(obj)
            return b''
        elif bType == WRPC_RQ_T_RELEASE:
            obj = PtrUtil.to_python(stream.read_pvoid())
            dbg_trace(wudp, f'Release "{obj}"')
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
        elif bType == WRPC_RQ_T_GLOBALDATA:
            dbg_trace(wudp, 'GlobalData Request')
            dwDataID = stream.read_dword()
            if dwDataID >= len(self.global_data):
                raise WRPCProtocolException('Request with Rq-Type GlobalData has invalid Data ID.')
            return WRPC.marshal(self.global_data[dwDataID], udp=True)
        elif bType == WRPC_RQ_T_GETITEM:
            obj = PtrUtil.to_python(stream.read_pvoid())
            key = WRPC.unmarshal(stream)
            dbg_trace(wudp, f'GetItem {obj}[{key}]')
            return WRPC.marshal(obj[key])
        elif bType == WRPC_RQ_T_SETITEM:
            obj = PtrUtil.to_python(stream.read_pvoid())
            key = WRPC.unmarshal(stream)
            value = WRPC.unmarshal(stream)
            dbg_trace(wudp, f'SetItem {obj}[{key}] = {value}')
            obj[key] = value
            return b''
        elif bType == WRPC_RQ_T_DELITEM:
            obj = PtrUtil.to_python(stream.read_pvoid())
            key = WRPC.unmarshal(stream)
            dbg_trace(wudp, f'GetItem {obj}[{key}]')
            del obj[key]
            return b''
            
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
        
    def store(self, obj):
        self.global_data.append(obj)
        
    def stop(self):
        # host stopped, destroy local-binded protocols
        for protocol in self.protocols:
            protocol.destroy()
        
        ip, port = self.sock.getsockname()
        ip = socket.inet_aton(ip)
        
        msg = WRPCUtils.message(WRPC_M_SIGNAL)
        
        sig = WRPCUtils.signal(
            WRPC_SIG_STOP, True, 
            self.get_preferences())
        
        sig += ip
        sig += bytes(WORD(port))
        
        msg.dwDataSize = len(sig)
        buf = bytes(msg) + sig
        
        # connected clients
        for client in self.connected:
            self.sock.sendto(buf, client)
        
        # destroy socket instance
        self.sock.close()
        self.alive = False
        
    def bind(self, protocol: IWRPCProtocol):
        self.protocols.append(protocol)
        
    def get_preferences(self):
        return WRPC_PROTOCOL_PREF_UDP
    
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
        try:
            self.host.sock.sendto(bytes(message) + marshal_data, (self.ip, self.port))
        except ConnectionResetError:
            self.destroy()
    
    def get_preferences(self):
        return WRPC_PROTOCOL_PREF_UDP
        
    def wait(self, timeout: Optional[float] = None) -> tuple[WRPC_MESSAGE, bytes]:
        if timeout is None:
            while self.host.response is None:
                time.sleep(WRPC_WAIT_TIME_QUANT)
        else:
            time_elapsed = 0.0
            while self.host.response is None:
                if time_elapsed >= timeout:
                    raise WRPCProtocolException('WRPC Response wait Time-out')
                time.sleep(WRPC_WAIT_TIME_QUANT)
                time_elapsed += WRPC_WAIT_TIME_QUANT
        response = self.host.response
        self.host.response = None
        return response
    
    def alive(self):
        return self.alive_state
    
    def destroy(self):
        self.alive_state = False
        
    def host_stopped(self, soft, ip, port):
        if ip == self.ip and port == self.port:
            self.destroy()

class WRPCNP(IWRPCProtocol):
    """
    WRPC Protocol Implementation for named pipes.
    """
    
    pipe: Pipe
    
    def __init__(self, pipe: str):
        self.pipe = Pipe(pipe)
        
        
    def open(self, pipe: str):
        self.pipe = Pipe(pipe)
        
class WRPCProtocolUtils:
    @staticmethod
    def get(protocol: IWRPCProtocol, dwDataID: int) -> Any:
        message = WRPCUtils.message(WRPC_M_REQUEST)
        request = WRPCUtils.request(WRPC_RQ_T_GLOBALDATA)
        request += bytes(DWORD(dwDataID))
        message.dwDataSize = len(request)
        protocol.write_message(message, request)
        msg, marshal_data = protocol.wait(timeout=5.0)
        stm = Stream(marshal_data)
        stm.protocol = protocol
        if msg.nExceptions != 0:
            raise WRPCException(WRPC.unmarshal_exceptions(stm, msg.nExceptions))
        return WRPC.unmarshal(stm)