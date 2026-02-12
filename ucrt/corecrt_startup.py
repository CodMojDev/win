#
# corecrt_startup.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# Declarations for the CoreCRT startup functionality, used while initializing
# the CRT and during app startup and termination.
#

from .corecrt import *
#include <math.h>
from ..vcrt.vcruntime_startup import *

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Exception Filters for main() and DllMain()
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from ..winnt import PEXCEPTION_POINTERS, EXCEPTION_POINTERS

@ucrtbased.foreign(ULONG, PEXCEPTION_POINTERS)
def _seh_filter_dll(_ExceptionNum: int, _ExceptionPtr: IPointer[EXCEPTION_POINTERS]) -> int: ...

@ucrtbased.foreign(ULONG, PEXCEPTION_POINTERS)
def _seh_filter_exe(_ExceptionNum: int, _ExceptionPtr: IPointer[EXCEPTION_POINTERS]) -> int: ...

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Miscellaneous Runtime Support
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
_crt_app_type = INT
_crt_unknown_app = 0
_crt_console_app = 1
_crt_gui_app = 2

@ucrtbased.foreign(_crt_app_type)
def _query_app_type() -> int: ...

@ucrtbased.foreign(VOID, _crt_app_type)
def _set_app_type(_Type: int): ...

_UserMathErrorFunctionPointer = CALLBACK(INT, _exception)

@ucrtbased.foreign(VOID, _UserMathErrorFunctionPointer)
def __setusermatherr(_UserMathErrorFunction: _UserMathErrorFunctionPointer): ...

@ucrtbased.foreign(INT)
def _is_c_termination_complete() -> int: ...

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Arguments API for main() et al.
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

@ucrtbased.foreign(errno_t, _crt_argv_mode)
def _configure_narrow_argv(mode: int) -> int: ...

@ucrtbased.foreign(errno_t, _crt_argv_mode)
def _configure_wide_argv(mode: int) -> int: ...

# There is a linkopt for these to disable environment initialization when using
# the static CRT, so they are not declared _ACRTIMP.
@ucrtbased.foreign(INT)
def _initialize_narrow_environment() -> int: ...

@ucrtbased.foreign(INT)
def _initialize_wide_environment() -> int: ...

@ucrtbased.foreign(PTR(LPSTR))
def _get_initial_narrow_environment() -> IPointer[LPSTR]: ...

@ucrtbased.foreign(PTR(LPWSTR))
def _get_initial_wide_environment() -> IPointer[LPWSTR]: ...

@ucrtbased.foreign(LPSTR)
def _get_narrow_winmain_command_line() -> LPSTR: ...

@ucrtbased.foreign(LPWSTR)
def _get_wide_winmain_command_line() -> LPWSTR: ...

@ucrtbased.foreign(PTR(LPSTR))
def __p__acmdln() -> IPointer[LPSTR]: ...

@ucrtbased.foreign(PTR(LPSTR))
def __p__wcmdln() -> IPointer[LPWSTR]: ... 

_acmdln = LPSTR.in_dll(ucrtbased, '_acmdln')
_wcmdln = LPWSTR.in_dll(ucrtbased, '_wcmdln')

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Initializer and Terminator Support
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
_PVFV = CALLBACK(VOID)
_PIFV = CALLBACK(INT)
_PVFI = CALLBACK(VOID, INT)

from _ctypes import CFuncPtr

@ucrtbased.foreign(VOID, PTR(_PVFV), PTR(_PVFV))
def _initterm(_First: IPointer[CFuncPtr], 
              _Last: IPointer[CFuncPtr]): ...

@ucrtbased.foreign(VOID, PTR(_PIFV), PTR(_PIFV))
def _initterm_e(_First: IPointer[CFuncPtr], 
              _Last: IPointer[CFuncPtr]): ...

_onexit_t = CALLBACK(INT)
_onexit_m_t = CALLBACK(INT)

class _onexit_table_t(CStructure):
    _fields_ = [
        ('_first', PTR(_PVFV)),
        ('_last', PTR(_PVFV)),
        ('_end', PTR(_PVFV))
    ]

@ucrtbased.foreign(INT, _onexit_table_t.PTR())
def _initialize_onexit_table(_Table: IPointer[_onexit_table_t]) -> int: ...

@ucrtbased.foreign(INT, _onexit_table_t.PTR(), _onexit_t)
def _register_onexit_function(_Table: IPointer[_onexit_table_t],
                              _Function: CFuncPtr) -> int: ...

@ucrtbased.foreign(INT, _onexit_table_t.PTR())
def _execute_onexit_table(_Table: IPointer[_onexit_table_t]) -> int: ..

@ucrtbased.foreign(INT, _PVFV)
def _crt_atexit(_Function: CFuncPtr) -> int: ...

@ucrtbased.foreign(INT, _PVFV)
def _crt_at_quick_exit(_Function: CFuncPtr) -> int: ...

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# Static CRT Initialization Support
#
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

@ucrtbased.foreign(BOOL, result_function=bool)
def __acrt_initialize() -> bool: ...

@ucrtbased.foreign(BOOL, BOOL, result_function=bool)
def __acrt_uninitialize(_Terminating: bool) -> bool: ...

@ucrtbased.foreign(BOOL, BOOL, result_function=bool)
def __acrt_uninitialize_critical(_Terminating: bool) -> bool: ...

@ucrtbased.foreign(BOOL, result_function=bool)
def __acrt_thread_attach() -> bool: ...

@ucrtbased.foreign(BOOL, result_function=bool)
def __acrt_thread_detach() -> bool: ...