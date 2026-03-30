from ..com.combaseapi import *

ROPARAMIIDHANDLE = HANDLE

class IRoSimpleMetaDataBuilder(COMInterface):
    virtual_table = COMVirtualTable('IRoSimpleMetaDataBuilder')
    
    @virtual_table.com_function(GUID)
    def SetWinRtInterface(self, iid: GUID) -> int: ...
    
    @virtual_table.com_function(GUID)
    def SetDelegate(self, iid: GUID) -> int: ...
    
    @virtual_table.com_function(PCWSTR, PCWSTR, PGUID)
    def SetInterfaceGroupSimpleDefault(self, name: str, defaultInterfaceName: str,
                                       defaultInterfaceIID: IPointer[GUID]) -> int: ...
    
    @virtual_table.com_function(PCWSTR, UINT32, PTR(PCWSTR))
    def SetInterfaceGroupParameterizedDefault(self, name: str, elementCount: int,
                                              defaultInterfaceNameElements: IPointer[PCWSTR]) -> int: ...
    
    @virtual_table.com_function(PCWSTR, UINT32, PGUID)
    def SetRuntimeClassSimpleDefault(self, name: str, defaultInterfaceName: str,
                                     defaultInterfaceIID: IPointer[GUID]) -> int: ...
    
    @virtual_table.com_function(PCWSTR, UINT32, PTR(PCWSTR))
    def SetRuntimeClassParameterizedDefault(self, name: str, elementCount: int,
                                            defaultInterfaceNameElements: IPointer[PCWSTR]) -> int: ...
    
    @virtual_table.com_function(PCWSTR, UINT32, PTR(PCWSTR))
    def SetStruct(self, name: str, numFields: int, 
                  fieldTypeNames: IPointer[PCWSTR]) -> int: ...
    
    @virtual_table.com_function(PCWSTR, PCWSTR)
    def SetEnum(self, name: str, baseType: str) -> int: ...
    
    @virtual_table.com_function(GUID, UINT32)
    def SetParameterizedInterface(self, piid: GUID, numArgs: int) -> int: ...
    
    @virtual_table.com_function(GUID, UINT32)
    def SetParameterizedDelegate(self, piid: GUID, numArgs: int) -> int: ...
    
    virtual_table.build()
    
class IRoMetaDataLocator(COMInterface):
    virtual_table = COMVirtualTable('IRoMetaDataLocator')
    
    @virtual_table.com_function(PCWSTR, IRoSimpleMetaDataBuilder.PTR(),
                                intermediate_method=True)
    def Locate(self, nameElement: str, metaDataDestination: IRoSimpleMetaDataBuilder,
               **kwargs) -> int: 
        return self.virt_delegate(nameElement, metaDataDestination.ref() if metaDataDestination else NULL)
    
    virtual_table.build()
    
@combase_foreign(UINT32, PTR(LPCWSTR), IRoMetaDataLocator.PTR(), PGUID, PTR(ROPARAMIIDHANDLE),
                 intermediate_method=True)
def RoGetParameterizedTypeInstanceIID(
    nameElementCount: int,
    nameElements: IPointer[LPCWSTR],
    metaDataLocator: IRoMetaDataLocator,
    iid: IPointer[GUID],
    pExtra: IPointer[ROPARAMIIDHANDLE],
    **kwargs) -> int:
    return delegate(nameElementCount, nameElements,
                    metaDataLocator.ref() if metaDataLocator else NULL,
                    iid, pExtra)
    
@combase.foreign(VOID, ROPARAMIIDHANDLE)
def RoFreeParameterizedTypeExtra(extra: ROPARAMIIDHANDLE): ...

@combase.foreign(PCSTR, ROPARAMIIDHANDLE)
def RoParameterizedTypeExtraGetTypeSignature(extra: ROPARAMIIDHANDLE) -> str: ...