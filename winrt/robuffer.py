from ..com.objinterfacedef import *
from ..com.combaseapi import *

wintypes = get_win_library('wintypes.dll')

@wintypes.foreign(HRESULT, PTR(LPMARSHAL))
def RoGetBufferMarshaler(bufferMarshaler: IDoublePtr[IMarshal]) -> int: 
    """
    Provides a standard IBuffer marshaler to implement the semantics associated with the IBuffer interface when it is marshaled.
    """

class IBufferByteAccess(IUnknown):
    """
    Represents a buffer as an array of bytes.
    """
    
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IBufferByteAccess')
    _iid_ = IID('{905a0fef-bc53-11df-8c49-001e4fc686da}')
    
    @virtual_table.com_function(DOUBLE_PTR(byte))
    def Buffer(self, value: IDoublePtr[byte]) -> int: 
        """
        Gets the array of bytes in the buffer.
        """
    
    virtual_table.build()