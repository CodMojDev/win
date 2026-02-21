#
# rpcdef.py
#

from typing import Optional, Callable
from ...vcrt.excpt import *

rpcrt4 = get_win_library('rpcrt4.dll')

I_RPC_HANDLE = PVOID
RPC_STATUS = LONG
RPC_S_OK = 0

def rpcrt_foreign(*args: type, 
            name: Optional[str] = None,
            intermediate_method: bool = False) -> Callable:
    """
    Foreign method declare
    """
    return foreign_optimized(RPC_STATUS, 
                             *args, 
                             library=rpcrt4, 
                             name=name, 
                             intermediate_method=intermediate_method)

def RpcExceptionCode():
    return GetExceptionCode()

def RpcAbnormalTermination():
    return AbnormalTermination()