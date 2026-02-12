from .inspectable import *

class IActivationFactory(IInspectable):
    """
    Enables classes to be activated by the Windows Runtime.
    """
    
    virtual_table = COMVirtualTable.from_ancestor(
        IInspectable.virtual_table, 'IActivationFactory')
    _iid_ = IID('{00000035-0000-0000-C000-000000000046}')
    
    @virtual_table.com_function(DOUBLE_PTR(IInspectable))
    def ActivateInstance(self, instance: IDoublePtr[IInspectable]) -> int:
        """
        Creates a new instance of the Windows Runtime class that is associated with the current activation factory.
        """
    
    virtual_table.build()
    
PACTIVATIONFACTORY = IActivationFactory.PTR()