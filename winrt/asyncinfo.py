from .inspectable import *

Started = 0
Completed = 1
Canceled = 2
Error = 3
AsyncStatus = INT

class IAsyncInfo(IInspectable):
    virtual_table = COMVirtualTable.from_ancestor(IInspectable)
    
    virtual_table.build()