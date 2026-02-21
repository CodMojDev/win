#
# excpt.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# The declarations of the compiler-dependent intrinsics, support functions, and
# keywords which implement the structured exception handling extensions.
#
#pragma once

from ..winnt import EXCEPTION_RECORD, PCONTEXT, CONTEXT, EXCEPTION_POINTERS, PEXCEPTION_POINTERS
from .vcruntime import *

# Exception disposition return values
ExceptionContinueExecution = 0
ExceptionContinueSearch = 1
ExceptionNestedException = 2
ExceptionCollidedUnwind = 3
EXCEPTION_DISPOSITION = INT

# SEH handler
if cpreproc.defined('_M_IX86'):
    @vcruntime140d.foreign(EXCEPTION_DISPOSITION, EXCEPTION_RECORD.PTR(),
                           PVOID, PCONTEXT, PVOID)
    def _except_handler(_ExceptionRecord: IPointer[EXCEPTION_RECORD],
                        _EstablisherFrame: IVoidPtr, 
                        _ContextRecord: IPointer[CONTEXT],
                        _DispatcherContext: IVoidPtr) -> int: ...
elif cpreproc.defined('_M_X64') or cpreproc.defined('_M_ARM') or cpreproc.defined('_M_ARM64'):
    @vcruntime140d.foreign(EXCEPTION_DISPOSITION, EXCEPTION_RECORD.PTR(), 
                           PVOID, PCONTEXT, PVOID)
    def __C_specific_handler(ExceptionRecord: IPointer[EXCEPTION_RECORD], 
                             EstablisherFrame: IVoidPtr,
                             ContextRecord: IPointer[CONTEXT],
                             DispatcherContext: IVoidPtr) -> int: ...
    
@vcruntime140d.foreign(ULONG)
def _exception_code() -> int: ...

@vcruntime140d.foreign(PVOID)
def _exception_info() -> IVoidPtr: ...

@vcruntime140d.foreign(INT)
def _abnormal_termination() -> int: ...

# SEH intrinsics
def GetExceptionCode() -> int:
    return _exception_code()

def exception_code() -> int:
    return _exception_code()

def GetExceptionInformation() -> IPointer[EXCEPTION_POINTERS]:
    return i_cast(_exception_info(), PEXCEPTION_POINTERS)

def exception_info() -> IPointer[EXCEPTION_POINTERS]:
    return i_cast(_exception_info(), PEXCEPTION_POINTERS)

def AbnormalTermination() -> int:
    return _abnormal_termination()

def abnormal_termination() -> int:
    return _abnormal_termination()

# Defined values for the exception filter expression
EXCEPTION_EXECUTE_HANDLER      = 1
EXCEPTION_CONTINUE_SEARCH      = 0
EXCEPTION_CONTINUE_EXECUTION   = (-1)