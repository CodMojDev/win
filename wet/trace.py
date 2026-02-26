#
# WET (Windows Event Tracing) core infrastructure
#

from typing import TypeAlias, Callable, ClassVar
from datetime import datetime
from ..sysinfoapi import *

import random

ConsumerCallback: TypeAlias = Callable[[IPointer['WET_EVENT']], None]

def _GenCookie() -> int:
    return random.randint(0, 2 ** 32 - 1)

class WET_PROVIDER(CStructure):
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
        cookie = _GenCookie()
        self._consumers.append((cookie, consumer))
        return cookie
    
    def Unsubscribe(self, consumer_cookie: int):
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
              level: int = WET_LEVEL_INFO):
    """
    Debug trace.
    """
    
    caller = get_caller_frame()
    cls = None
    
    additional_info = None
    
    if trace_id != -1:
        additional_info = WET_ADDITIONAL_INFO(IsComObject=True, TraceID=trace_id)
    
    name = caller.f_code.co_qualname
    if 'self' in caller.f_locals:
        if additional_info is None:
            additional_info = WET_ADDITIONAL_INFO(IsClassMethod=True, Class=cls.__qualname__)
        else:
            additional_info.IsClassMethod = True
            additional_info.Class = cls.__qualname__
        
        self = caller.f_locals['self']
        cls = self.__class__
        
        components = name.split('.')
        components.pop(-2)
        name = '.'.join(components)
    
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
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    return provider.Subscribe(Consumer)
    
def WETProvider_Unsubscribe(RegName: str, Cookie: int) -> int:
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    provider.Unsubscribe(Cookie)
    
class STDCONSUMER_FILE(CStructure):
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
    if StdConsumerId == STD_CONSUMER_PRINT:
        StdConsumerFile = i_cast(pData, PSTDCONSUMER_FILE).contents
        _FILE_GLOBAL_STATE._file_name = StdConsumerFile.FileName
        _FILE_GLOBAL_STATE._file = open(_FILE_GLOBAL_STATE._file_name)
    
STD_CONSUMER_PRINT = 0x0001
STD_CONSUMER_FILE  = 0x0002
    
def ConsumerPrint(pEvent: IPointer[WET_EVENT]):
    Event = pEvent.contents
    DateTime = datetime.fromtimestamp(Event.TimeDateStamp)
    TimeStr = DateTime.strftime('%d.%m.%Y %H:%M:%S')
    Provider = Event.pWetProvider.contents
    FunctionName = Event.FunctionName
    
    AdditionalInfo = None
    if Event.AdditionalInfo:
        AdditionalInfo = Event.AdditionalInfo.contents
        if AdditionalInfo.IsClassMethod:
            FunctionName = f'{AdditionalInfo.Class}::{FunctionName}'
    
    print(f'[{TimeStr}] [{Provider.RegName}] {FunctionName}()', end=' ')
    
    if AdditionalInfo is not None:
        if AdditionalInfo.IsComObject:
            print(f'TraceID {AdditionalInfo.TraceID}', end=' ')
    
    for i in range(Event.nTraceComponents):
        TraceComponent = Event.TraceComponents[i]
        
        if TraceComponent.Type == WET_TRACE_TYPE_STRING:
            print(TraceComponent.TraceString, end=' ')
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
            print(f'{Parameter.Parameter}={Value}')
    print()
    
def ConsumerFile(pEvent: IPointer[WET_EVENT]):
    if not _FILE_GLOBAL_STATE._file_name:
        raise RuntimeError('STD_CONSUMER_FILE is not configured.')
    
    Event = pEvent.contents
    DateTime = datetime.fromtimestamp(Event.TimeDateStamp)
    TimeStr = DateTime.strftime('%d.%m.%Y %H:%M:%S')
    Provider = Event.pWetProvider.contents
    FunctionName = Event.FunctionName
    
    AdditionalInfo = None
    if Event.AdditionalInfo:
        AdditionalInfo = Event.AdditionalInfo.contents
        if AdditionalInfo.IsClassMethod:
            FunctionName = f'{AdditionalInfo.Class}::{FunctionName}'
    
    _FILE_GLOBAL_STATE._file.write(f'[{TimeStr}] [{Provider.RegName}] {FunctionName}() ')
    
    if AdditionalInfo is not None:
        if AdditionalInfo.IsComObject:
            _FILE_GLOBAL_STATE._file.write(f'TraceID {AdditionalInfo.TraceID} ')
    
    for i in range(Event.nTraceComponents):
        TraceComponent = Event.TraceComponents[i]
        
        if TraceComponent.Type == WET_TRACE_TYPE_STRING:
            _FILE_GLOBAL_STATE._file.write(f'{TraceComponent.TraceString} ')
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
            _FILE_GLOBAL_STATE._file.write(f'{Parameter.Parameter}={Value}')
            
    _FILE_GLOBAL_STATE._file.write('\n')
    _FILE_GLOBAL_STATE._file.flush()
    
def RegisterStandardConsumer(StdConsumerId: int, Provider: WET_PROVIDER | str) -> int:
    if isinstance(Provider, str):
        ProviderName = Provider
        Provider = _WET_GLOBAL_STATE.LookupProvider(ProviderName)
        if Provider is None:
            raise ValueError(f'Unknown provider "{ProviderName}".')
        
    if StdConsumerId == STD_CONSUMER_PRINT:
        Provider.Subscribe(ConsumerPrint)
    elif StdConsumerId == STD_CONSUMER_FILE:
        Provider.Subscribe(ConsumerFile)
        
import sys
        
def StdStreamsToStandardConsumer(StdConsumerId: int):
    if StdConsumerId == STD_CONSUMER_FILE:
        if not _FILE_GLOBAL_STATE._file_name:
            raise RuntimeError('STD_CONSUMER_FILE is not configured.')
        
        sys.stdout = sys.stderr = _FILE_GLOBAL_STATE._file