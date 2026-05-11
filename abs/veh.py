from win.vcrt.excpt import EXCEPTION_CONTINUE_EXECUTION, EXCEPTION_CONTINUE_SEARCH, EXCEPTION_EXECUTE_HANDLER
from win.winnt import EXCEPTION_POINTERS
from win.errhandlingapi import *

class IAbsVEH(IInterface):
    @interface_abstract_method
    @classmethod
    def execute(cls, pointers: IPointer[EXCEPTION_POINTERS]) -> int: ...

class _ABS_VEH_STATE:
    __slots__ = ['handlers', 'handler']
    handlers: list[type[IAbsVEH]]
    handler: int
    def __init__(self):
        self.handlers = []
        self.handler = 0
        
_abs_veh_state = _ABS_VEH_STATE()

@PVECTORED_EXCEPTION_HANDLER
def VEH(pointers: IPointer[EXCEPTION_POINTERS]) -> int: 
    for handler in _abs_veh_state.handlers:
        result = handler.execute(pointers)
        if result != EXCEPTION_CONTINUE_SEARCH:
            return result
    return EXCEPTION_CONTINUE_SEARCH

def abs_enable_veh(first: bool=False):
    _abs_veh_state.handler = AddVectoredExceptionHandler(first, VEH)
    
def abs_disable_veh():
    if _abs_veh_state.handler:
        RemoveVectoredExceptionHandler(_abs_veh_state.handler)
        
def abs_add_veh(veh: type[IAbsVEH]):
    _abs_veh_state.handlers.append(veh)
    
def abs_remove_veh(veh: type[IAbsVEH]):
    _abs_veh_state.handlers.remove(veh)