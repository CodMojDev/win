#
# winrtns.py
#
# WinRT Namespaces definition.
#

from .robuffer import *
from .roapi import *

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
            
        # real implementation
        @TemplateFunction[IT]
        def ActivateInstance(activatableClassId: HSTRING, 
                             instance: IDoublePtr[IT], **kwargs) -> int:
            instance.contents = NULL
            pInspectable = IInspectable.NULL()
            hr = RoActivateInstance(activatableClassId, byref(pInspectable))
            if FAILED(hr): raise COMError(hr)
            template: Template[IT] = get_template()
            template_type = template.get_single_type()
            template_ptr = template.get_pointer_type()
            if template_type.iid() == IInspectable.iid():
                instance.contents = static_cast[template_ptr](pInspectable)
            else:
                hr = pInspectable.contents.QueryInterface(
                    template_type.iid(), instance)
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
        @TemplateFunction[IT]
        def GetActivationFactory(activatableClassId: HSTRING,
                                 factory: IDoublePtr[IT]) -> int:
            template: Template[IT] = get_template()
            return RoGetActivationFactory(activatableClassId, 
                                          template.get_single_type().iid(),
                                          factory)
    class Storage(INamespace):
        class Streams(INamespace):
            IBufferByteAccess = robuffer.IBufferByteAccess
            
class ABI(INamespace):
    class Windows(INamespace):
        Foundation = Windows.Foundation