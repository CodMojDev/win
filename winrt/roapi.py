from .inspectable import *
from .activation import *
from .hstring import *

from ..com.combaseapi import *
from ..wtypesbase import *

RO_INIT_SINGLETHREADED     = 0      # Single-threaded application
RO_INIT_MULTITHREADED      = 1      # COM calls objects on any thread.
RO_INIT_TYPE = INT

RO_REGISTRATION_COOKIE = PVOID

PFNGETACTIVATIONFACTORY = CALLBACK(HRESULT, HSTRING, PTR(PACTIVATIONFACTORY))

@combase_foreign(RO_INIT_TYPE)
def RoInitialize(initType: RO_INIT_TYPE) -> int:
    """
    Initializes the Windows Runtime on the current thread with the specified concurrency model.
    """
    
@combase.foreign(VOID)
def RoUninitialize(): 
    """
    Closes the Windows Runtime on the current thread.
    """
    
@combase_foreign(HSTRING, DOUBLE_PTR(IInspectable))
def RoActivateInstance(activatableClassId: HSTRING,
                       instance: IDoublePtr[IInspectable]) -> int:
    """
    Activates the specified Windows Runtime class.
    """
    
@combase_foreign(PTR(HSTRING), PVOID, UINT32, RO_REGISTRATION_COOKIE)
def RoRegisterActivationFactories(activatableClassIds: HSTRING,
                                  activationFactoryCallbacks: PVOID,
                                  count: int, cookie: RO_REGISTRATION_COOKIE) -> int:
    """
    Registers an array out-of-process activation factories for a Windows Runtime exe server.
    """
    
@combase.foreign(VOID, RO_REGISTRATION_COOKIE)
def RoRevokeActivationFactories(cookie: RO_REGISTRATION_COOKIE) -> int:
    """
    Removes an array of registered activation factories from the Windows Runtime.
    """
    
@combase_foreign(HSTRING, REFIID, PVOID, intermediate_method=True)
def RoGetActivationFactory(activatableClassId: HSTRING, iid: IID, 
                           factory: IPointer[PVOID], **kwargs) -> int:
    """
    Gets the activation factory for the specified runtime class. (RoGetActivationFactory)
    """
    return delegate(activatableClassId, iid.ref(), factory)

APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = HANDLE

@combase_foreign(IApartmentShutdown.PTR(), PUINT64, 
                 PTR(APARTMENT_SHUTDOWN_REGISTRATION_COOKIE))
def RoRegisterForApartmentShutdown(callbackObject: IPointer[IApartmentShutdown],
                                   apartmentIdentifier: IPointer[UINT64],
                                   regCookie: IPointer[APARTMENT_SHUTDOWN_REGISTRATION_COOKIE]) -> int:
    """
    Registers an IApartmentShutdown callback to be invoked when the current apartment shuts down.
    """
    
@combase_foreign(APARTMENT_SHUTDOWN_REGISTRATION_COOKIE)
def RoUnregisterForApartmentShutdown(regCookie: APARTMENT_SHUTDOWN_REGISTRATION_COOKIE) -> int:
    """
    Unregisters a previously registered IApartmentShutdown interface.
    """
    
@combase_foreign(PUINT64)
def RoGetApartmentIdentifier(apartmentIdentifier: IPointer[UINT64]) -> int:
    """
    Gets a unique identifier for the current apartment.
    """