from ..objinterfacedef import *

class IRpcStubBufferVtbl(CStructure):
    _fields_ = []
    
class ICallFactoryVtbl(CStructure):
    _fields_ = []
    
class IReleaseMarshalBuffersVtbl(CStructure):
    _fields_ = []
    
class IPSFactoryBufferVtbl(CStructure):
    _fields_ = []
    
class CInterfaceStubVtbl(CStructure):
    _fields_ = []
    
class CInterfaceProxyHeader(CStructure):
    fields = []
    
    if cpreproc.ifdef('USE_STUBLESS_PROXY'):
        fields.append(('pStublessProxyInfo', PVOID))
        pStublessProxyInfo: IVoidPtr
    
    fields.append(('piid', PIID))
    piid: IPointer[IID]
    
declare_fields(CInterfaceProxyHeader)

class CInterfaceProxyVtbl(CStructure):
    _fields_ = [
        ('header', CInterfaceProxyHeader)
    ]
    
    header: CInterfaceProxyHeader
    Vtbl: IArray[PVOID]
    
flexible_array(CInterfaceProxyVtbl, 'Vtbl', PVOID)
    
PCInterfaceStubVtblList = CInterfaceStubVtbl.PTR()
PCInterfaceProxyVtblList = CInterfaceProxyVtbl.PTR()
PCInterfaceName = LPSTR
IIDLookupRtn = WINAPI(INT, PIID, PINT)
PIIDLookup = PTR(IIDLookupRtn)

# Uses a default lookup mechanism
NdrDefaultIIDLookup = i_cast(-1, PIIDLookup)

class ProxyFileInfo(CStructure):
    _fields_ = [
        ('pProxyVtblList', PTR(PCInterfaceProxyVtblList)),
        ('pStubVtblList', PTR(PCInterfaceStubVtblList)),
        ('pNamesArray', PTR(PCInterfaceName)),
        ('pDelegatedIIDs', PTR(PIID)),
        ('pIIDLookupRtn', PIIDLookup),
        ('TableSize', USHORT),
        ('TableVersion', USHORT),
        ('pAsyncIIDLookup', PTR(PIID)),
        ('Filler2', LONG_PTR),
        ('Filler3', LONG_PTR),
        ('Filler4', LONG_PTR)
    ]
    
    pProxyVtblList: IDoublePtr[CInterfaceProxyVtbl]
    pStubVtblList: IDoublePtr[CInterfaceStubVtbl]
    pNamesArray: IPointer[LPSTR]
    pDelegatedIIDs: IDoublePtr[IID]
    pIIDLookupRtn: IPointer[FARPROC]
    
    TableSize: int
    TableVersion: int
    
    pAsyncIIDLookup: IDoublePtr[IID]
    
    Filler2: int
    Filler3: int
    Filler4: int
        
# Macro used for ANSI compatible stubs.

def CINTERFACE_PROXY_VTABLE(n: int):
    class ProxyVtblStructure(CStructure):
        _fields_ = [
            ('header', CInterfaceProxyHeader),
            ('Vtbl', PVOID * n)
        ]
        
        header: CInterfaceProxyHeader
        Vtbl: IArray[PVOID]
        
    return ProxyVtblStructure

IInspectableInterfaceProxyTag = PVOID(-1)
IUnknownInterfaceProxyTag = PVOID(-2)

PRPC_STUB_FUNCTION = WINAPI(VOID, IRpcStubBuffer.PTR(),
                            IRpcChannelBuffer.PTR(),
                            PRPC_MESSAGE,
                            PDWORD)