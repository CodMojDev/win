#
# winrtns.py
#
# WinRT Namespaces definition.
#

from .roparameterizediid import *
from .robuffer import *
from .roapi import *

from . import roparameterizediid
from . import robuffer

class Windows(INamespace):
    class Foundation(INamespace):
        @staticmethod
        def Initialize(initType: RO_INIT_TYPE) -> int:
            """
            Initializes a thread to use Windows Runtime APIs.
            """
            return RoInitialize(initType)
        
        @staticmethod
        def Uninitialize():
            """
            Closes the Windows Runtime on the current thread.
            """
            RoUninitialize()
        
        # typed function
        @staticmethod
        def ActivateInstance(activatableClassId: HSTRING, 
                             instance: IDoublePtr[IT], **kwargs) -> int: 
            """
            Registers and retrieves an instance of a specified type defined in a specified class ID.
            """
        
        def ActivateInstance(activatableClassId: HSTRING, 
                             instance: IDoublePtr[IT], **kwargs) -> int:
            instance.contents = NULL
            pInspectable = IInspectable.NULL()
            hr = RoActivateInstance(activatableClassId, byref(pInspectable))
            if FAILED(hr): raise COMError(hr)
            pTy = PtrUtil.get_type(instance)
            ty = PtrUtil.get_type(pTy)
            if ty.iid() == IInspectable.iid():
                instance.contents = static_cast[pTy](pInspectable)
            else:
                hr = pInspectable.contents.QueryInterface(
                    ty.iid(), instance)
                pInspectable.contents.Release()
                if FAILED(hr): raise COMError(hr)
            return hr
        
        @staticmethod
        def RegisterActivationFactories(activatableClassIds: HSTRING,
                                  activationFactoryCallbacks: PVOID,
                                  count: int, cookie: RO_REGISTRATION_COOKIE) -> int:
            """
            Registers an array out-of-process activation factories for a Windows Runtime exe server.
            """
            return RoRegisterActivationFactories(activatableClassIds,
                                                 activationFactoryCallbacks,
                                                 count, cookie)
            
        @staticmethod
        def RevokeActivationFactories(cookie: RO_REGISTRATION_COOKIE) -> int:
            """
            Removes an array of registered activation factories from the Windows Runtime.
            """
            RoRevokeActivationFactories(cookie)
            
        # typed function
        @staticmethod
        def GetActivationFactory(activatableClassId: HSTRING,
                                 factory: IDoublePtr[IT]) -> int:
            """
            Retrieves an activation factory for the type specified by the template parameter.
            """
            
        # real implementation
        def GetActivationFactory(activatableClassId: HSTRING,
                                 factory: IDoublePtr[IT], **kwargs) -> int:
            return RoGetActivationFactory(activatableClassId, 
                                          PtrUtil.get_type(PtrUtil.get_type(factory)).iid(),
                                          factory)
    class Storage(INamespace):
        class Streams(INamespace):
            IBufferByteAccess = robuffer.IBufferByteAccess
            
class ABI(INamespace):
    class Windows(INamespace):
        Foundation = Windows.Foundation