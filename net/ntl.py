from .interop import _AppDomain
from .interop import *

import atexit

#
# .NET Template Library API 
#

provider = WET_PROVIDER('NTL')

class NtlPolicy(int):
    Bool = 0
    Throw = 1
    
def _NtlPolicyIntToString(policy: int) -> str:
    if policy == NtlPolicy.Bool:
        return 'NtlPolicy.Bool'
    elif policy == NtlPolicy.Throw:
        return 'NtlPolicy.Throw'
    return 'NtlPolicy.Unknown'

class _NTL_STATE:
    __slots__ = ['_corRTHost', '_rtHostRunning', '_lastExc',
                 '_appDomain', '_policy', '_errored']

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
        self._errored = False
        self._lastExc = None

_ntl_state = _NTL_STATE()

def NtlHasException():
    hasException = _ntl_state._lastExc is not None
    dbg_trace(provider, 'Has exception' if hasException else "Hasn't exception")
    return hasException

def NtlSetExceptionPolicy(policy: NtlPolicy):
    dbg_trace(provider, f'NTL Exception policy = {_NtlPolicyIntToString(policy)}')
    _ntl_state._policy = policy

def NtlThrow():
    dbg_trace(provider, level=WET_LEVEL_ERROR)
    exc = NtlException()
    NtlResetException()
    raise exc

def NtlException():
    return _ntl_state._lastExc

def NtlResetException():
    dbg_trace(provider, f'Resetted exception')
    _ntl_state._lastExc = None

def _NtlSetExcHR(hr: int):
    _ntl_state._lastExc = COMError(hr)
    _ntl_state._errored = True

def NtlInitCLR(version: str = 'v4.0.30319') -> bool:
    pCorRTHost = ICorRuntimeHost.NULL()
    hr = CorBindToRuntime(
        version, 'wks',
        CLSID_CorRuntimeHost,
        IID_ICorRuntimeHost,
        byref(pCorRTHost))
    if FAILED(hr): 
        if _ntl_state._policy == NtlPolicy.Throw:
            _ntl_state._errored = True
            dbg_trace(provider, 'CLR Host creation failure', level=WET_LEVEL_ERROR)
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            dbg_trace(provider, f'CLR Host creation failure: "{str(_ntl_state._lastExc)}"', level=WET_LEVEL_ERROR)
            return False
    
    corRTHost = pCorRTHost.contents
    _ntl_state._corRTHost = corRTHost
    
    hr = corRTHost.Start()
    if FAILED(hr):
        corRTHost.Release()
        if _ntl_state._policy == NtlPolicy.Throw:
            dbg_trace(provider, 'CLR Host startup failure', level=WET_LEVEL_ERROR)
            _ntl_state._errored = True
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            dbg_trace(provider, f'CLR Host startup failure: "{str(_ntl_state._lastExc)}"', level=WET_LEVEL_ERROR)
            return False
    
    pAppDomain = _AppDomain.NULL()
    hr = corRTHost.GetDefaultDomain(byref(pAppDomain))
    if FAILED(hr):
        corRTHost.Stop()
        corRTHost.Release()
        if _ntl_state._policy == NtlPolicy.Throw:
            _ntl_state._errored = True
            dbg_trace(provider, 'App Domain obtaining failure', level=WET_LEVEL_ERROR)
            raise COMError(hr)
        else:
            _NtlSetExcHR(hr)
            dbg_trace(provider, f'App Domain obtaining failure: "{str(_ntl_state._lastExc)}"', level=WET_LEVEL_ERROR)
            return False
    
    appDomain = pAppDomain.contents
    _ntl_state._appDomain = appDomain
    _ntl_state._rtHostRunning = True
    dbg_trace(provider, 'CLR Initialized', level=WET_LEVEL_ERROR)
    
    return True

def NtlUnload():
    if not _ntl_state._rtHostRunning:
        return
    
    del Object._saved_mscorlib_for_interop
    del Object._saved_system_for_interop
    
    _ntl_state._appDomain.Release()
    hr = _ntl_state._corRTHost.Stop()
    if FAILED(hr): 
        if _ntl_state._policy == NtlPolicy.Throw:
            _ntl_state._corRTHost.Release()
            _ntl_state._errored = True
            dbg_trace(provider, 'CLR Host stopping failure', level=WET_LEVEL_ERROR)
            raise COMError(hr)
        else:
            dbg_trace(provider, f'CLR Host stopping failure: "{str(_ntl_state._lastExc)}"', level=WET_LEVEL_ERROR)
            _NtlSetExcHR(hr)
    _ntl_state._corRTHost.Release()

def NtlAutoUnload():
    atexit.register(NtlUnload)

def NtlIsRunning() -> bool:
    return _ntl_state._rtHostRunning

def NtlLoadMscorlib() -> Assembly:
    if not _ntl_state._rtHostRunning:
        return None
    
    if Object._saved_mscorlib_for_interop is not None:
        return Object._saved_mscorlib_for_interop
    
    dbg_trace(provider, 'Loading MSCORLIB...')
    
    mscorlib = Assembly(_ntl_state._appDomain.GetType().Assembly)
    mscorlib.Initialize()
    
    dbg_trace(provider, 'MSCORLIB Loaded.')
    
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
    if provider._consumers:
        names = [namespace.__name__ for namespace in namespaces]
        
        if len(namespaces) == 2:
            logMessage = ' and '.join(names)
        else:
            logMessage = ', '.join(names) + ' and ' + names[-1]    
            
        dbg_trace(provider, logMessage)
        
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