from .ntl import _ntl_state
from .ntl import *

provider = WET_PROVIDER('NTL-Extension')

#
# .NET Template Library Extension API
#

class NtlInitState(int):
    NotRunning = 0
    Initialized = 1
    Failure = -1

def NtlExtGetMscorlib() -> Assembly:
    dbg_trace(provider, 'MSCORLIB Requested')
    return Object._ensure_mscorlib()

def NtlExtLoadSystem() -> Assembly:
    if not NtlIsRunning():
        return None
    
    try:
        mscorlib = NtlExtGetMscorlib()
    except RuntimeError:
        mscorlib = NtlLoadMscorlib()
        
    System = mscorlib.System
    
    currentDomain = System.AppDomain.CurrentDomain
    systemAsm = currentDomain.Load(
        'System, '
        'Version=4.0.0.0, '
        'Culture=neutral, '
        'PublicKeyToken='
        'b77a5c561934e089')
    system = Assembly(systemAsm)
    system.Initialize()
    
    Object._saved_system_for_interop = system
    
    return system

def NtlExtGetSystem() -> Assembly:
    if not NtlIsRunning():
        return None
    
    return Object._saved_system_for_interop

def NtlExtGetInitState() -> NtlInitState:
    if _ntl_state._errored:
        return NtlInitState.Failure
    
    if not _ntl_state._rtHostRunning:
        return NtlInitState.NotRunning
    
    return NtlInitState.Initialized

def _NtlExtCompleteVersion(Version: str) -> str:
    components = Version.split('.')[:4]
    while len(components) < 4:
        components.append('0')
    return '.'.join(components)

def NtlExtLoadAssembly(assembly: str, version: str, publicKeyToken: str,
                       culture: str = 'neutral') -> Assembly:
    if not _ntl_state._rtHostRunning:
        return None
    
    mscorlib = NtlExtGetMscorlib()
    version = _NtlExtCompleteVersion(version)
    string = '{}, Version={}, Culture={}, PublicKeyToken={}'.format(
        assembly, version, culture, publicKeyToken)
    
    try:
        asm = mscorlib.System.AppDomain.CurrentDomain.Load(string)
    except COMError as ce:
        raise MethodEngine.COMError_to_NET_exception(ce) from None
    
    asmWrapper = Assembly(asm)
    asmWrapper.Initialize()
    
    return asmWrapper

def NtlExtLoadAssemblyPath(assemblyPath: str):
    if not _ntl_state._rtHostRunning:
        return None
    
    mscorlib = NtlExtGetMscorlib()
    assemblyName = mscorlib.System.Reflection.AssemblyName.GetAssemblyName(assemblyPath)
    
    try:
        asm = mscorlib.System.AppDomain.CurrentDomain.Load(assemblyName)
    except COMError as ce:
        raise MethodEngine.COMError_to_NET_exception(ce) from None
    
    asmWrapper = Assembly(asm)
    asmWrapper.Initialize()
    
    return asmWrapper