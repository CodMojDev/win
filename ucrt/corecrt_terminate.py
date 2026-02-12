#
# corecrt_terminate.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# The terminate handler
#

from .corecrt import *

# terminate_handler is the standard name; terminate_function is defined for
# source compatibility.
terminate_handler = CRTDECL(None)
terminate_function = CRTDECL(None)

__terminate_function_m = CRTDECL(None)
__terminate_handler_m = CRTDECL(None)

@ucrtbased.foreign(None)
def abort(): ...

@ucrtbased.foreign(None)
def terminate(): ...

from _ctypes import CFuncPtr

@ucrtbased.foreign(terminate_handler, terminate_handler)
def set_terminate(_NewTerminateHandler: CFuncPtr) -> CFuncPtr: ...

@ucrtbased.foreign(terminate_handler)
def _get_terminate() -> CFuncPtr: ...