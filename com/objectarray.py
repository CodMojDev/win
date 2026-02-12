from .baseinterfacedef import *

# generic interfaces that express a set of items

class IObjectArray(IUnknown):
    """
    Unknown Object Array
    """
    
    virtual_table = COMVirtualTable.from_ancestor(
        IUnknown.virtual_table, 'IObjectArray')
    _iid_ = IID('{92CA9DCD-5622-4bba-A805-5E9F541BD8C9}')

    @virtual_table.com_function(PUINT)
    def GetCount(self, pcObjects: PUINT) -> int: 
        """
        Provides a count of the objects in the collection.
        """

    @virtual_table.com_function(UINT, REFIID, PVOID, 
                                intermediate_method=True)
    def GetAt(self, uiIndex: int, iid: IID,
              ppv: IPointer[PVOID], **kwargs) -> int:
        """
        Provides a pointer to a specified object's interface. The object and interface are specified by index and interface ID.
        """
        return self.virt_delegate(uiIndex, iid.ref(), ppv)

    virtual_table.build()
    
class IObjectCollection(IObjectArray):
    """
    Extends the `IObjectArray` interface by providing methods that enable clients to add and remove objects that support `IUnknown` in a collection.
    """
    
    virtual_table = COMVirtualTable.from_ancestor(
        IObjectArray.virtual_table, 'IObjectCollection')
    _iid_ = IID('{5632b1a4-e38a-400a-928a-d4cd63230295}')

    @virtual_table.com_function(LPUNKNOWN)
    def AddObject(self, punk: IPointer[IUnknown]) -> int: 
        """
        Adds a single object to the collection.
        """

    @virtual_table.com_function(IObjectArray.PTR())
    def AddFromArray(self, poaSource: IPointer[IObjectArray]) -> int:
        """
        Adds the objects contained in an IObjectArray to the collection.
        """

    @virtual_table.com_function(UINT)
    def RemoveObjectAt(self, uiIndex: int) -> int:
        """
        Removes a single, specified object from the collection.
        """

    @virtual_table.com_function()
    def Clear(self) -> int:
        """
        Removes all objects from the collection. (IObjectCollection.Clear)
        """

    virtual_table.build()