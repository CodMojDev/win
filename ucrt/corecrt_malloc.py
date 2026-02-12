#
# corecrt_malloc.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# The memory allocation library.  These pieces of the allocation library are
# shared by both <stdlib.h> and <malloc.h>.
#

from .. import cpreproc

if cpreproc.pragma_once():
    from .corecrt import *

    @ucrtbased.foreign(c_void_p, size_t, size_t)
    def _calloc_base(_Count: int, _Size: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, size_t, size_t)
    def calloc(_Count: int, _Size: int) -> IVoidPtr: ...

    @ucrtbased.foreign(int_t, size_t)
    def _callnewh(_Size: int) -> int: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t)
    def _expand(_Block: IVoidPtr, _Size: int) -> IVoidPtr: ...

    @ucrtbased.foreign(None, c_void_p)
    def _free_base(_Block: IVoidPtr): ...

    @ucrtbased.foreign(None, c_void_p)
    def free(_Block: IVoidPtr): ...

    @ucrtbased.foreign(c_void_p, size_t)
    def _malloc_base(_Size: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, size_t)
    def malloc(_Size: int) -> IVoidPtr: ...
    
    #@ucrtbased.foreign(size_t, c_void_p)
    #def _msize_base(_Block: IVoidPtr) -> int: ...
    
    @ucrtbased.foreign(size_t, c_void_p)
    def _msize(_Block: IVoidPtr) -> int: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t)
    def _realloc_base(_Block: IVoidPtr, _Size: int) -> IVoidPtr: ...
    
    @ucrtbased.foreign(c_void_p, c_void_p, size_t)
    def realloc(_Block: IVoidPtr, _Size: int) -> IVoidPtr: ...
    
    #@ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t)
    #def _recalloc_base(_Block: IVoidPtr, _Count: int, _Size: int) -> IVoidPtr: ...

    #@ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t)
    #def recalloc(_Block: IVoidPtr, _Count: int, _Size: int) -> IVoidPtr: ...

    @ucrtbased.foreign(None, c_void_p)
    def _aligned_free(_Block: IVoidPtr): ...

    @ucrtbased.foreign(c_void_p, size_t, size_t)
    def _aligned_malloc(_Size: int, _Alignment: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, size_t, size_t, size_t)
    def _aligned_offset_malloc(_Size: int, _Alignment: int, _Offset: int) -> IVoidPtr: ...

    @ucrtbased.foreign(size_t, c_void_p, size_t, size_t)
    def _aligned_msize(_Block: IVoidPtr, _Alignment: int, _Offset: int) -> int: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t, size_t)
    def _aligned_offset_realloc(_Block: IVoidPtr, _Size: int, _Alignment: int, _Offset: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t, size_t, size_t)
    def _aligned_offset_recalloc(_Block: IVoidPtr, _Count: int, _Size: int, _Alignment: int, _Offset: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t)
    def _aligned_realloc(_Block: IVoidPtr, _Size: int, _Alignment: int) -> IVoidPtr: ...

    @ucrtbased.foreign(c_void_p, c_void_p, size_t, size_t, size_t)
    def _aligned_recalloc(_Block: IVoidPtr, _Count: int, _Size: int, _Alignment: int) -> IVoidPtr: ...