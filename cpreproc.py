__all__ = [
    'define', 
    'ifdef', 
    'ifndef', 
    'getdef', 
    'undef',
    'error',
    'resetdef',
    'defined',
    'get_defines',
    'get_version',
    'timestamp',
    'PreprocessorError',
    'pragma_pack_pop',
    'pragma_pack_push',
    'pragma_pack',
    'pragma_once',
    'line', 'file'
]

class PreprocessorError(OSError): ...

from ctypes import c_uint64, c_void_p, c_int, windll, sizeof, Structure
from queue import Queue

_defines = {}

class _CPreprocStateType:
    __slots__ = ('_pack_stack', '_cur_pack', '_internal_cached_UNICODE')
    
    # friend module defbase
    
    def __init__(self):
        self._cur_pack = sizeof(c_void_p)
        self._pack_stack = Queue(-1)
        
        self._internal_cached_UNICODE = False
    
    _pack_stack: Queue
    _cur_pack: int
    
    _internal_cached_UNICODE: bool # defbase.unicode(...) optimization
    
_CPreprocState = _CPreprocStateType()

def define(k: str, e=None):
    if k == 'UNICODE':
        _CPreprocState._internal_cached_UNICODE = k
    if ifndef(k):
        _defines[k] = e
    
def ifdef(k: str) -> bool:
    return k in _defines
    
def ifndef(k: str) -> bool:
    return k not in _defines

def defined(k: str) -> bool: ...

defined = ifdef
    
def getdef(k: str):
    return _defines.get(k)
   
def undef(k: str):
    if ifdef(k):
        if k == 'UNICODE':
            _CPreprocState._internal_cached_UNICODE = False
        del _defines[k]

def resetdef():
    global _defines
    _defines = {}
    
def get_defines():
    return _defines.copy()
    
def error(message):
    raise PreprocessorError(message)

def pragma_pack_pop():
    if _CPreprocState._pack_stack.empty():
        raise PreprocessorError("Pack stack underflow.")
    _CPreprocState._cur_pack = _CPreprocState._pack_stack.get()
    
def pragma_push(n: int = 0):
    if not n:
        n = _CPreprocState._cur_pack
    _CPreprocState._pack_stack.put(n)
    
def pragma_pack(n: int):
    if n <= 0:
        raise PreprocessorError("Pack is lesser or equals 0.")
    _CPreprocState._cur_pack = n

def get_version():
    return getdef("_WINVER")

from time import strftime, localtime

import typing as t
import sys

def timestamp():
    return strftime('%a %d %b %H:%M:%S %Y', localtime())

if hasattr(sys, '_getframe'):
    from sys import _getframe as getframe
    
    def pragma_once(k: t.Optional[str] = None):
        if k is None:
            k = f'__{getframe().f_back.f_code.co_filename.replace(".", "_")}__'
        if ifndef(k):
            define(k)
            return True
        return False
    
    def line():
        return getframe().f_back.f_lineno

    def file():
        return getframe().f_back.f_code.co_filename
else:
    def pragma_once(k: t.Optional[str] = None):
        if k is None:
            raise PreprocessorError('Key cannot be None. ("sys" module doesn\'t have attribute "_getframe")')
        if ifndef(k):
            define(k)
            return True
        return False
    
    def line():
        raise RuntimeError('Method not implemented. "sys" module doesn\'t have attribute "_getframe".')
    
    def file():
        raise RuntimeError('Method not implemented. "sys" module doesn\'t have attribute "_getframe".')

from ctypes.wintypes import WORD, BYTE, DWORD

# define the default definitions

# CRITICAL SECTION START ***

def _cpreproc_init():
    import platform

    define('UNICODE')

    # for architecture specifying
    if sizeof(c_void_p) == 4:
        define("_WIN32")
        DWORD_PTR = c_int
    else:
        define("_WIN64")
        define("_M_X64", 100)
        DWORD_PTR = c_uint64
        
    # predefined macros
    arch = platform.machine().lower()
    if arch in ('arm64', 'aarch64'):
        define("_M_ARM64", 1)
    elif arch in ('arm', 'armv7l', 'armv8l'):
        define("_M_ARM", 7)
    elif arch in ('x86_64', 'amd64'):
        define("_M_AMD64")
    elif arch in ('x86', 'i386', 'i686'):
        define("_M_IX86")
    
    define("_MSC_VER", 1700)

    # for guiddef.py
    define("INITGUID")

    # for version indicating
    from .defbase import declare

    MAKEWORD = lambda a, b: (WORD((BYTE(DWORD_PTR(a).value & 0xFF).value) | (WORD(BYTE(DWORD_PTR(b).value & 0xFF).value)).value << 8)).value
    LOWORD = lambda l: (WORD((DWORD_PTR(l)).value & 0xFFFF)).value
    LOBYTE = lambda w: (BYTE((DWORD_PTR(w)).value & 0xFF)).value
    HIBYTE = lambda w: (WORD((DWORD_PTR(w).value >> 8) & 0xFF)).value
    dwVersion = declare(windll.kernel32.GetVersion, DWORD, None)()

    define("_WINVER", MAKEWORD(HIBYTE(LOWORD(dwVersion)), LOBYTE(LOWORD(dwVersion))))

_cpreproc_init()

del _cpreproc_init

# CRITICAL SECTION END ***