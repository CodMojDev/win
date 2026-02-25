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
    
    RegName: LPCWSTR
    fEnabled: int
    
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
        String: LPCWSTR
        SignedInt: int
        PyObject: int
        
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
WET_TRACE_TYPE_OBJECT = 0x0002
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
    TraceString: LPCWSTR
    Type: int
    
PWET_TRACE_COMPONENT = WET_TRACE_COMPONENT.PTR()

class WET_EVENT(CStructure):
    _fields_ = [
        ('TimeDateStamp', ULONG_PTR),
        ('pWetProvider', PWET_PROVIDER),
        ('FunctionName', LPCWSTR),
        ('nTraceComponents', UINT),
        ('TraceComponents', PWET_TRACE_COMPONENT)
    ]
    
    TraceComponents: IPointer[WET_TRACE_COMPONENT]
    pWetProvider: IPointer[WET_PROVIDER]
    nTraceComponents: int
    FunctionName: LPCWSTR
    TimeDateStamp: int
    
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

def dbg_trace(provider: WET_PROVIDER | str, message: str = ''):
    """
    Debug trace.
    """
    caller = get_caller_frame()
    name = caller.f_code.co_qualname.replace('.', '::')
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
                      pWetProvider=provider.ptr())
    
    event.TimeDateStamp = round(datetime.now().timestamp())
        
    provider.SendEvent(event)
    
def WETProvider_Subscribe(RegName: str, Consumer: ConsumerCallback) -> int:
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    provider.Subscribe(Consumer)
    
def WETProvider_Unsubscribe(RegName: str, Cookie: int) -> int:
    provider = _WET_GLOBAL_STATE.LookupProvider(RegName)
    if provider is None:
        raise ValueError(f'Unknown provider "{RegName}"')
    provider.Unsubscribe(Cookie)