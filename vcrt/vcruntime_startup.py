"""
#
# vcruntime_startup.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# Declarations of the VCRuntime startup functionality
#
"""

from .. import cpreproc

if cpreproc.pragma_once("__VCRUNTIME_STARTUP_H__"):
    from ..minwindef import *

    msvcrt = W_WinDLL("msvcrt.dll")

    _crt_argv_mode = INT
    _crt_argv_no_arguments = 0
    _crt_argv_unexpanded_arguments = 1
    _crt_argv_expanded_arguments = 2

    _crt_exit_return_mode = INT
    _crt_exit_terminate_process = 0
    _crt_exit_return_to_caller = 1

    _crt_exit_cleanup_mode = INT
    _crt_exit_full_cleanup = 0
    _crt_exit_quick_cleanup = 1
    _crt_exit_no_cleanup = 2

    __current_exit_return_mode = _crt_exit_return_mode.in_dll(msvcrt, "__current_exit_return_mode")

    @msvcrt.foreign(BOOL, result_function=bool)
    def __vcrt_initialize(): ...
    
    @msvcrt.foreign(BOOL, result_function=bool)
    def __vcrt_uninitialize(_Terminating: bool): ...
    
    @msvcrt.foreign(BOOL, result_function=bool)
    def __vcrt_uninitialize_critical(): ...
    
    @msvcrt.foreign(BOOL, result_function=bool)
    def __vcrt_thread_attach(): ...
    
    @msvcrt.foreign(BOOL, result_function=bool)
    def __vcrt_thread_detach(): ...

    @msvcrt.foreign(BOOL, result_function=bool)
    def __isa_available_init(): ...
    
    @msvcrt.foreign(_crt_argv_mode)
    def _get_startup_argv_mode(): ...