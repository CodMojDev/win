#
# vcruntime_string.h
#
#      Copyright (c) Microsoft Corporation. All rights reserved.
#
# <string.h> functionality that is implemented in the VCRuntime.
#

from .. import cpreproc

if cpreproc.pragma_once():
    from .vcruntime import *

    @vcruntime140d.foreign(c_void_p, c_void_p, c_int, c_size_t)
    def memchr(_Buf: IVoidPtr, _Val: int, _MaxCount: int) -> IVoidPtr: ...
    
    @vcruntime140d.foreign(c_int, c_void_p, c_void_p, c_size_t)
    def memcmp(_Buf1: IVoidPtr, _Buf2: IVoidPtr, _Size: int) -> int: ...
    
    @vcruntime140d.foreign(c_void_p, c_void_p, c_void_p, c_size_t)
    def memcpy(_Dst: IVoidPtr, _Src: IVoidPtr, _Size: int) -> IVoidPtr: ...

    @vcruntime140d.foreign(c_void_p, c_void_p, c_void_p, c_size_t)
    def memmove(_Dst: IVoidPtr, _Src: IVoidPtr, _Size: int) -> IVoidPtr: ...

    @vcruntime140d.foreign(c_void_p, c_void_p, c_int, c_size_t)
    def memset(_Dst: IVoidPtr, _Val: int, _Size: int) -> IVoidPtr: ...

    @vcruntime140d.foreign(c_char_p, c_char_p, c_char)
    def strchr(_Str: WT_LPSTR, _Val: IChar) -> c_char_p: ...
    
    @vcruntime140d.foreign(c_char_p, c_char_p, c_char)
    def strrchr(_Str: WT_LPSTR, _Ch: IChar) -> c_char_p: ...
    
    @vcruntime140d.foreign(c_char_p, c_char_p, c_char_p)
    def strstr(_Str: WT_LPSTR, _SubStr: WT_LPSTR) -> c_char_p: ...
    
    @vcruntime140d.foreign(c_wchar_p, c_wchar_p, c_wchar)
    def wcschr(_Str: WT_LPWSTR, _Val: IWideChar) -> c_wchar_p: ...
    
    @vcruntime140d.foreign(c_wchar_p, c_wchar_p, c_wchar)
    def wcsrchr(_Str: WT_LPWSTR, _Ch: IWideChar) -> c_wchar_p: ...
    
    @vcruntime140d.foreign(c_wchar_p, c_wchar_p, c_wchar_p)
    def wcsstr(_Str: WT_LPWSTR, _SubStr: WT_LPSTR) -> c_wchar_p: ...
