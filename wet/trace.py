#
# WET (Windows Event Tracing) core infrastructure
#

from typing import TypeAlias, Callable, ClassVar
from datetime import datetime
from ..sysinfoapi import *
from ..dbg.dbgapi import *

import random

ConsumerCallback: TypeAlias = Callable[[IPointer['WET_EVENT']], None]

def _GenCookie() -> int:
    return random.randint(0, 2 ** 32 - 1)

class WET_PROVIDER(CStructure):
    """
    Structure representing WET Provider
    """
    
    _fields_ = [
        ('RegName', LPCWSTR),
        ('fEnabled', BOOL)
    ]
    
    _consumers: list[tuple[int, ConsumerCallback]]
    
    fEnabled: int
    RegName: str
    
    def __init__(self, reg_name: str, enabled: bool = True):
        self.RegName = reg_name
        self.fEnabled = enabled
        self._consumers = []
        
        _WET_GLOBAL_STATE._providers_.append(self)
        
    def SendEvent(self, event: 'WET_EVENT'):
        if not self.fEnabled: return
        pEvent = event.ptr()
        for _, consumer in self._consumers:
            consumer(pEvent)
            
    def Subscribe(self, consumer: ConsumerCallback) -> int:
        """
        Subscribe to provider and get the cookie.
        """
        cookie = _GenCookie()
        self._consumers.append((cookie, consumer))
        return cookie
    
    def Unsubscribe(self, consumer_cookie: int):
        """
        Unsubscribe from provider by cookie.
        """
        consumers = []
        for cookie, consumer in self._consumers:
            if cookie != consumer_cookie:
                consumers.append((cookie, consumer))
        self._consumers = consumers
    
PWET_PROVIDER = WET_PROVIDER.PTR()

WET_PARAMETER_TYPE_NULL   = 0x0000
WET_PARAMETER_TYPE_STRING = 0x0001
WET_PARAMETER_TYPE_PYTHON = 0x0002
WET_PARAMETER_TYPE_INT    = 0x0003
WET_PARAMETER_TYPE_UINT   = 0x0004
WET_PARAMETER_TYPE = UINT
    
class WET_PARAMETER(CStructure):
    """
    Structure representing WET Event Parameter
    """
    
    class _Value(CUnion):
        _fields_ = [
            ('String', LPCWSTR),
            ('PyObject', PVOID),
            ('SignedInt', INT),
            ('UnsignedInt', UINT)
        ]
        
        UnsignedInt: int
        SignedInt: int
        PyObject: int
        String: str
        
    _fields_ = [
        ('Parameter', LPCWSTR),
        ('ParameterType', WET_PARAMETER_TYPE),
        ('Value', _Value)
    ]
    
    ParameterType: int
    Parameter: LPCWSTR
    Value: _Value
    
WET_TRACE_TYPE_NULL   = 0x0000
WET_TRACE_TYPE_STRING = 0x0001
WET_TRACE_TYPE_PARAMETER = 0x0002
WET_TRACE_TYPE = UINT
    
class WET_TRACE_COMPONENT(CStructure):
    """
    Structure representing WET Event Trace Component
    """
    
    class _U(CUnion):
        _fields_ = [
            ('TraceString', LPCWSTR),
            ('WetParameter', WET_PARAMETER)
        ]
        
    _fields_ = [
        ('Type', WET_TRACE_TYPE),
        ('_u', _U)
    ]
    _anonymous_ = ['_u']
    
    pWetParameter: IPointer[WET_PARAMETER]
    TraceString: str
    Type: int
    
PWET_TRACE_COMPONENT = WET_TRACE_COMPONENT.PTR()

class WET_ADDITIONAL_INFO(CStructure):
    """
    Structure representing the WET Event Additional Info (may be NULL)
    """
    
    _fields_ = [
        ('IsComObject', BOOLEAN),
        ('IsClassMethod', BOOLEAN),
        ('Class', LPCWSTR),
        ('TraceID', UINT)
    ]
    
    IsClassMethod: int
    IsComObject: int
    TraceID: int
    Class: str

PWET_ADDITIONAL_INFO = WET_ADDITIONAL_INFO.PTR()

WET_LEVEL_INFO = 0x0000
WET_LEVEL_WARNING = 0x0001
WET_LEVEL_ERROR = 0x0002
WET_LEVEL_FATAL = 0x0003
WET_LEVEL = INT

class WET_EVENT(CStructure):
    """
    Structure representing the WET Event.
    """
    
    _fields_ = [
        ('TimeDateStamp', ULONG_PTR),
        ('pWetProvider', PWET_PROVIDER),
        ('FunctionName', LPCWSTR),
        ('nTraceComponents', UINT),
        ('TraceComponents', PWET_TRACE_COMPONENT),
        ('AdditionalInfo', PWET_ADDITIONAL_INFO),
        ('Level', WET_LEVEL)
    ]
    
    TraceComponents: IPointer[WET_TRACE_COMPONENT]
    AdditionalInfo: IPointer[WET_ADDITIONAL_INFO]
    pWetProvider: IPointer[WET_PROVIDER]
    nTraceComponents: int
    TimeDateStamp: int
    FunctionName: str
    Level: int
    
PWET_EVENT = WET_EVENT.PTR()
    
class _WET_GLOBAL_STATE:
    _providers_: ClassVar[list[WET_PROVIDER]] = []
    
    @classmethod
    def LookupProvider(cls, reg_name: str) -> WET_PROVIDER:
        for provider in cls._providers_:
            if provider.RegName == reg_name:
                return provider
        return None
    
PWET_EVENT_CALLBACK = CALLBACK(VOID, PWET_EVENT)

def dbg_trace(provider: WET_PROVIDER | str, message: str = '', trace_id: int = -1,
              level: int = WET_LEVEL_INFO, up_stack: int = 0):
    """
    Debug trace.
    """
    
    caller = get_py_frame(1 + up_stack)
    cls = None
    
    additional_info = None
    
    if trace_id != -1:
        additional_info = WET_ADDITIONAL_INFO(IsComObject=True, TraceID=trace_id)
    
    name = caller.f_code.co_qualname
       
    if 'self' in caller.f_locals: 
        self = caller.f_locals['self']
        cls = self.__class__
        
        if additional_info is None:
            additional_info = WET_ADDITIONAL_INFO(IsClassMethod=True, Class=cls.__qualname__)
        else:
            additional_info.IsClassMethod = True
            additional_info.Class = cls.__qualname__
    
    name = name.replace('.', '::')
    
    if name.endswith('_Impl'):
        name = name[:-5]
    elif name.endswith('__init__'):
        name = f'new {name[:-10]}'
    
    # 
    # send event to WET
    #
    
    if isinstance(provider, str):
        provider_name = provider
        provider = _WET_GLOBAL_STATE.LookupProvider(provider_name)
        if provider is None:
            raise ValueError(f'Unknown provider "{provider_name}".')
    
    TraceComponent = WET_TRACE_COMPONENT(TraceString=message, Type=WET_TRACE_TYPE_STRING)
    event = WET_EVENT(FunctionName=name, nTraceComponents=1, 
                      TraceComponents=TraceComponent.ptr(),
                      pWetProvider=provider.ptr(), Level=level,
                      TimeDateStamp = round(datetime.now().timestamp()))
    
    if additional_info is not None:
        event.AdditionalInfo = additional_info.ptr()
        
    provider.SendEvent(event)
    
def WETProvider_Subscribe(RegName: str, Consumer: ConsumerCallback) -> int:
    """
    Subscribe to WET Provider by its name and get the cookie.
    """
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    return provider.Subscribe(Consumer)
    
def WETProvider_Unsubscribe(RegName: str, Cookie: int) -> int:
    """
    Unsubscribe from WET Provider by its name and cookie.
    """
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    provider.Unsubscribe(Cookie)
    
class STDCONSUMER_FILE(CStructure):
    """
    Configuration structure for standard consumer `STD_CONSUMER_FILE`.
    """
    
    _fields_ = [
        ('FileName', LPCWSTR)
    ]
    
    FileName: str
    
PSTDCONSUMER_FILE = STDCONSUMER_FILE.PTR()
    
from io import TextIOWrapper
    
class _FILE_GLOBAL_STATE:
    _file: ClassVar[TextIOWrapper] = None
    _file_name: ClassVar[str] = None
    
def ConfigureStandardConsumer(StdConsumerId: int, pData: IVoidPtr):
    """
    Configure the standard consumer.
    
    Supported standard consumers: `STD_CONSUMER_FILE` by STDCONSUMER_FILE structure.
    """
    if StdConsumerId == STD_CONSUMER_FILE:
        if pData:
            StdConsumerFile = i_cast(pData, PSTDCONSUMER_FILE).contents
            _FILE_GLOBAL_STATE._file_name = StdConsumerFile.FileName
            _FILE_GLOBAL_STATE._file = open(_FILE_GLOBAL_STATE._file_name, 'w')
        else: # ConfigureStandardConsumer(STD_CONSUMER_FILE, NULL) releases the opened log file
            if _FILE_GLOBAL_STATE._file and not _FILE_GLOBAL_STATE._file.closed:
                _FILE_GLOBAL_STATE._file_name = None
                _FILE_GLOBAL_STATE._file.close()
                _FILE_GLOBAL_STATE._file = None
    
STD_CONSUMER_PRINT = 0x0001
STD_CONSUMER_FILE  = 0x0002
STD_CONSUMER_DEBUG = 0x0003
STD_CONSUMER = INT
    
# construct the standard message text from PWET_EVENT
def ConstructMessage(pEvent: IPointer[WET_EVENT]):
    Event = pEvent.contents
    DateTime = datetime.fromtimestamp(Event.TimeDateStamp)
    TimeStr = DateTime.strftime('%d.%m.%Y %H:%M:%S')
    Provider = Event.pWetProvider.contents
    FunctionName = Event.FunctionName
    
    AdditionalInfo = None
    if Event.AdditionalInfo:
        AdditionalInfo = Event.AdditionalInfo.contents
        
    Message = f'[{TimeStr}] [{Provider.RegName}] {FunctionName}() '
    
    if AdditionalInfo is not None:
        if AdditionalInfo.IsComObject:
            Message += f'TraceID {AdditionalInfo.TraceID} '
    
    for i in range(Event.nTraceComponents):
        TraceComponent = Event.TraceComponents[i]
        
        if TraceComponent.Type == WET_TRACE_TYPE_STRING:
            Message += f'{TraceComponent.TraceString} '
        elif TraceComponent.Type == WET_TRACE_TYPE_PARAMETER:
            Parameter = TraceComponent.pWetParameter.contents
            ParameterType = Parameter.ParameterType
            if ParameterType == WET_PARAMETER_TYPE_NULL:
                Value = 'None'
            elif ParameterType == WET_PARAMETER_TYPE_INT:
                Value = str(Parameter.Value.SignedInt)
            elif ParameterType == WET_PARAMETER_TYPE_UINT:
                Value = str(Parameter.Value.UnsignedInt)
            elif ParameterType == WET_PARAMETER_TYPE_STRING:
                Value = f'"{Parameter.Value.String}"'
            elif ParameterType == WET_PARAMETER_TYPE_PYTHON:
                PyObject = i_cast(Parameter.Value.PyObject, py_object).contents
                Value = f'{PyObject}'
            else: Value = '[Unknown Type]'
            Message += f'{Parameter.Parameter}={Value} '
            
    Message += '\n'
    return Message
    
# standard consumer implementation for STD_CONSUMER_PRINT
def ConsumerPrint(pEvent: IPointer[WET_EVENT]):
    print(ConstructMessage(pEvent), end='')
    
# standard consumer implementation for STD_CONSUMER_FILE
def ConsumerFile(pEvent: IPointer[WET_EVENT]):
    if not _FILE_GLOBAL_STATE._file:
        raise RuntimeError('STD_CONSUMER_FILE is not configured.')
    
    if _FILE_GLOBAL_STATE._file.closed: return
    
    _FILE_GLOBAL_STATE._file.write(ConstructMessage(pEvent))
    _FILE_GLOBAL_STATE._file.flush()
    
# standard consumer implementation for STD_CONSUMER_DEBUG
def ConsumerDebug(pEvent: IPointer[WET_EVENT]):
    if not IsDebuggerPresent(): return 
    
    OutputDebugString(ConstructMessage(pEvent))
    
def RegisterStandardConsumer(StdConsumerId: int, Provider: WET_PROVIDER | str) -> int:
    """
    Subscribe the standard consumer to provider and get the cookie.
    
    Supported standard consumers: `STD_CONSUMER_PRINT`, 
    `STD_CONSUMER_FILE`, `STD_CONSUMER_DEBUG`
    """
    if isinstance(Provider, str):
        ProviderName = Provider
        Provider = _WET_GLOBAL_STATE.LookupProvider(ProviderName)
        if Provider is None:
            raise ValueError(f'Unknown provider "{ProviderName}".')
        
    if StdConsumerId == STD_CONSUMER_PRINT:
        return Provider.Subscribe(ConsumerPrint)
    elif StdConsumerId == STD_CONSUMER_FILE:
        return Provider.Subscribe(ConsumerFile)
    elif StdConsumerId == STD_CONSUMER_DEBUG:
        return Provider.Subscribe(ConsumerDebug)
    else:
        return -1
        
import sys
import io

class StdStreamDebug(io.TextIOWrapper):
    def write(self, s: str):
        OutputDebugString(s)
        
def StdStreamsToStandardConsumer(StdConsumerId: int):
    """
    Direct the Std streams to standard consumer.
    
    Supported consumers: `STD_CONSUMER_FILE`, `STD_CONSUMER_DEBUG`
    """
    if StdConsumerId == STD_CONSUMER_FILE:
        if not _FILE_GLOBAL_STATE._file_name:
            raise RuntimeError('STD_CONSUMER_FILE is not configured.')
        
        sys.stdout = sys.stderr = _FILE_GLOBAL_STATE._file
    elif StdConsumerId == STD_CONSUMER_DEBUG:
        sys.stdout = StdStreamDebug(sys.stdout.buffer)
        sys.stderr = StdStreamDebug(sys.stderr.buffer)
        
def RestoreStdStreams():
    """
    Restore the Std streams after `StdStreamsToStandardConsumer` call.
    """
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__