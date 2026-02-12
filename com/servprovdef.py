#
# servprovdef.py
#

from .objinterfacedef import *

class IServiceProvider(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{6d5140c1-7436-11ce-8034-00aa006009fa}')
    
    @virtual_table.com_function(REFGUID, REFIID, PVOID, intermediate_method=True)
    def QueryService(self, guidService: GUID, iid: IID, ppvObject: IPointer[PVOID]) -> int:
        return self.virt_delegate(guidService.ref(), iid.ref(), ppvObject)
    
    virtual_table.build()
    
LPSERVICEPROVIDER = IServiceProvider.PTR()