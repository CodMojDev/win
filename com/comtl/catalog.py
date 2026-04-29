from .baseface import *
from .factory import *
from .icl import *
from .trace import *
from .control import *
from .reflection import *

class IWinCatalog(IUnknown):
    _iid_ = IID('{FBC4CFB3-C3CA-4253-9DCB-DBADA797BA41}')
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    
    @virtual_table.com_function(REFCLSID, PTR(LPUNKNOWN))
    def Query(self, rclsid: IPointer[CLSID], ppunk: IDoublePtr[IUnknown]) -> int: ...
    
    virtual_table.build()

class WinCatalog(CComObject, IWinCatalog):
    _clsid_ = CLSID('{CA190712-91D9-42CD-9424-68F87AE8488D}')
    _catalog_: ClassVar[dict[CLSID, IT]] = {
        PythonControl._clsid_: PythonControl,
        ICLGenerator._clsid_: ICLGenerator,
        WETManager._clsid_: WETManager,
        PythonManager._clsid_: PythonManager
    }
    _creatable_ = True
    
    def __init__(self):
        super().__init__()
        self.implement_interface(IWinCatalog)
        
    def Query_Impl(self, rclsid: IPointer[CLSID], ppunk: IDoublePtr[IUnknown]) -> int:
        if not rclsid:
            return E_POINTER
        interface = self._catalog_.get(rclsid.contents)
        if interface is None:
            return CLASS_E_CLASSNOTAVAILABLE
        instance = interface()
        TlWritePointerToPpv(ppunk, instance.ref())
        return S_OK