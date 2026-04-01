from .interop import _AppDomain
from .interop import *

import atexit

#
# .NET Template Library API 
#

class NtlPolicy(int):
    Bool = 0
    Throw = 1

class _NTL_STATE:
    __slots__ = ['_corRTHost', '_rtHostRunning', '_lastExc',
                 '_appDomain', '_policy']

    _corRTHost: ICorRuntimeHost
    _appDomain: _AppDomain
    _rtHostRunning: bool
    _lastExc: Exception
    _policy: NtlPolicy
    
    def __init__(self):
        self._policy = NtlPolicy.Bool
        self._rtHostRunning = False
        self._corRTHost = None
        self._appDomain = None
        self._lastExc = None

_ntl_state = _NTL_STATE()

def NtlHasException():
    return _ntl_state._lastExc is not None

def NtlSetExceptionPolicy(policy: NtlPolicy):
    _ntl_state._policy = policy

def NtlThrow():
    exc = NtlException()
    NtlResetException()
    raise exc

def NtlException():
    return _ntl_state._lastExc

def NtlResetException():
    _ntl_state._lastExc = None

def _NtlSetExcHR(hr: int):
    _ntl_state._lastExc = COMError(hr)

def NtlInitCLR(version: str = 'v4.0.30319') -> bool:
    pCorRTHost = ICorRuntimeHost.NULL()
    hr = CorBindToRuntime(
        version, 'wks',
        CLSID_CorRuntimeHost,
        IID_ICorRuntimeHost,
        byref(pCorRTHost))
    if FAILED(hr): 
        if _ntl_state._policy == NtlPolicy.Throw:
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            return False
    
    corRTHost = pCorRTHost.contents
    _ntl_state._corRTHost = corRTHost
    
    hr = corRTHost.Start()
    if FAILED(hr):
        corRTHost.Release()
        if _ntl_state._policy == NtlPolicy.Throw:
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            return False
    
    pAppDomain = _AppDomain.NULL()
    hr = corRTHost.GetDefaultDomain(byref(pAppDomain))
    if FAILED(hr):
        corRTHost.Stop()
        corRTHost.Release()
        if _ntl_state._policy == NtlPolicy.Throw:
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            return False
    
    appDomain = pAppDomain.contents
    _ntl_state._appDomain = appDomain
    _ntl_state._rtHostRunning = True
    
    return True

def NtlUnload():
    if not _ntl_state._rtHostRunning:
        return
    
    _ntl_state._appDomain.Release()
    hr = _ntl_state._corRTHost.Stop()
    if FAILED(hr): 
        if _ntl_state._policy == NtlPolicy.Throw:
            _ntl_state._corRTHost.Release()
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
    _ntl_state._corRTHost.Release()

def NtlAutoUnload():
    atexit.register(NtlUnload)

def NtlIsRunning() -> bool:
    return _ntl_state._rtHostRunning

def NtlLoadMscorlib() -> Assembly:
    if not _ntl_state._rtHostRunning:
        return None
    
    mscorlib = Assembly(_ntl_state._appDomain.GetType().Assembly)
    mscorlib.initialize()
    
    return mscorlib

def NtlGetAppDomain() -> _AppDomain:
    if not _ntl_state._rtHostRunning:
        return None
    
    return _ntl_state._appDomain

def NtlGetCLRHost() -> ICorRuntimeHost:
    if not _ntl_state._rtHostRunning:
        return None
    
    return _ntl_state._corRTHost

def NtlAggregate(*namespaces):
    for namespace in namespaces:
        for attr in dir(namespace):
            if attr.startswith('__'): continue
            for namespace_ in namespaces:
                if isinstance(namespace_, type) and issubclass(namespace_, INamespace):
                    if not namespace_ is namespace:
                        if hasattr(namespace_, attr):
                            NtlAggregate(getattr(namespace_, attr), getattr(namespace, attr))
                        else:
                            builtins.type.__setattr__(namespace_, attr, getattr(namespace, attr))