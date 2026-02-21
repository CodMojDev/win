from .automationbase import *

class BSTR(LPOLESTR):
    _allocated: bool
    
    def __init__(self):
        self._allocated = False
        
    @classmethod
    def init_untracked(cls):
        instance = cls()
        instance._allocated = True
        return instance
        
    @classmethod
    def from_param(cls, value):
        if value is NULL: return NULL
        if isinstance(value, str): return cls.new(value)
        if isinstance(value, BSTR): return value
        raise TypeError(f'Expected str/BSTR/NULL, got {type(value).__name__}')
    
    @classmethod
    def new(cls, string: str, length: int = -1) -> 'BSTR':
        if length != -1:
            bstr = SysAllocStringLen(string, length)
        else:
            bstr = SysAllocString(string)
        bstr._allocated = True
        return bstr
    
    @classmethod
    def new_untracked(cls, string: str, length: int = -1) -> 'BSTR':
        if length != -1:
            bstr = SysAllocStringLen(string, length)
        else:
            bstr = SysAllocString(string)
        bstr._allocated = False
        return bstr
        
    def __del__(self):
        if getattr(self, '_allocated', True):
            SysFreeString(self)
            self._allocated = False
            
    def __bool__(self) -> bool:
        return self._allocated and bool(self.value)
    
    def __str__(self) -> str:
        if getattr(self, '_allocated', True): return self.value
        return '<NULL>'
    
    def __repr__(self) -> str:
        address = hex(PtrUtil.get_address(self))
        value = str(self)
        if len(value) > 25:
            value = value[:25] + '...'
        return f'<BSTR at {address}, value="{value}">'

LPBSTR = POINTER(BSTR)
BSTR_NULL = BSTR()
    
@oleaut32.foreign(VOID, BSTR)
def SysFreeString(bstrString: BSTR):
    """
    Deallocates a string allocated previously by `SysAllocString`, 
    `SysAllocStringByteLen`, `SysReAllocString`, `SysAllocStringLen`, or
    `SysReAllocStringLen`.
    """
    
@oleaut32.foreign(BSTR, LPOLESTR)
def SysAllocString(psz: LPOLESTR) -> BSTR:
    """
    Allocates a new string and copies the passed string into it.
    """
    
@oleaut32.foreign(BSTR, LPOLESTR, UINT)
def SysAllocStringLen(strIn: LPOLESTR, ui: int) -> BSTR:
    """
    Allocates a new string, copies the specified number of characters from the passed string, and appends a null-terminating character.
    """