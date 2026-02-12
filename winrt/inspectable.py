from ..com.autointerfacedef import *
from .hstring import *

BaseTrust	 = 0
PartialTrust = ( BaseTrust + 1 )
FullTrust	 = ( PartialTrust + 1 )
TrustLevel   = INT

class IInspectable(IUnknown):
    """
    Provides functionality required for all Windows Runtime classes.
    """
    
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IInspectable')
    _iid_ = IID('{AF86E2E0-B12D-4c6a-9C5A-D7AA65101E90}')
    
    @virtual_table.com_function(PULONG, PTR(LPIID))
    def GetIids(self, iidCount: PULONG, iids: IDoublePtr[IID]) -> int:
        """
        Gets the interfaces that are implemented by the current Windows Runtime class.
        """
    
    @virtual_table.com_function(PTR(HSTRING))
    def GetRuntimeClassName(self, className: IPointer[HSTRING]) -> int:
        """
        Gets the fully qualified name of the current Windows Runtime object.
        """
    
    @virtual_table.com_function(PTR(TrustLevel))
    def GetTrustLevel(self, trustLevel: IPointer[TrustLevel]) -> int:
        """
        Gets the trust level of the current Windows Runtime object.
        """
    
    virtual_table.build()