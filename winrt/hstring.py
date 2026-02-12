from ..com.combaseapi import *
from ..winnt import *

class HSTRING_HEADER(CStructure):
    class uReserved(Union):
        _preinit_fields_ = [('Reserved1', PVOID)]
        if cpreproc.ifdef('_WIN64'):
            _preinit_fields_.append(('Reserved2', CHAR * 24))
        else:
            _preinit_fields_.append(('Reserved2', CHAR * 20))
        _fields_ = _preinit_fields_
        
        Reserved2: IArray[CHAR]
        Reserved1: PVOID
        
    _fields_ = [
        ('Reserved', uReserved)
    ]
    
    Reserved: uReserved
    
# Declare the HSTRING_BUFFER for the HSTRING's two-phase construction functions.
# 
# This route eliminates the PCWSTR string copy that happens when passing it to
# the traditional WindowsCreateString().  The caller preallocates a string buffer,
# sets the wide character string values in that buffer, and finally promotes the
# buffer to an HSTRING.  If a buffer is never promoted, it can still be deleted.
HSTRING_BUFFER = HANDLE

class HSTRING(HANDLE): 
    _allocated: bool
    
    def __init__(self, string: TUnion['HSTRING', str] = None):
        if string is None: 
            self._allocated = False
            return
        if isinstance(string, HSTRING):
            WindowsDuplicateString(string, byref(self))
        elif isinstance(string, str):
            WindowsCreateString(string, len(string), byref(self))
        self._allocated = True
            
    def __bool__(self) -> bool:
        return not WindowsIsStringEmpty(self)
    
    def __len__(self) -> int:
        return WindowsGetStringLen(self)
    
    def __str__(self) -> str:
        return WindowsGetStringRawBuffer(self, NULL).value
    
    def __del__(self): 
        if self._allocated:
            WindowsDeleteString(self)
            self._allocated = False
    
    def __add__(self, string: TUnion['HSTRING', str]) -> 'HSTRING':
        if isinstance(string, str):
            string = HSTRING(string)
        if isinstance(string, HSTRING):
            newString = HSTRING()
            length = len(string) + len(self)
            WindowsCreateString(create_unicode_buffer(length), 
                                length, byref(newString))
            WindowsConcatString(self, string, newString)
            return newString
        return NotImplemented
    
    @classmethod
    def from_param(cls, value):
        if isinstance(value, str):
            return cls(value)
        if isinstance(value, HSTRING):
            return value
        raise TypeError(f'Expected HSTRING/str, got {type(value).__name__}')

    def copy(self) -> 'HSTRING':
        return HSTRING(self)

@combase_foreign(PCNZWCH, UINT32, PTR(HSTRING))
def WindowsCreateString(sourceString: PCNZWCH, length: int,
                        string: IPointer[HSTRING]) -> int: ...
    
@combase_foreign(PCWSTR, UINT32, HSTRING_HEADER.PTR(), PTR(HSTRING))
def WindowsCreateStringReference(sourceString: PCWSTR, length: int,
                                 hstringHeader: IPointer[HSTRING_HEADER],
                                 string: IPointer[HSTRING]) -> int: ...
    
@combase_foreign(HSTRING)
def WindowsDeleteString(string: HSTRING) -> int: ...
    
@combase_foreign(HSTRING, PTR(HSTRING))
def WindowsDuplicateString(string: HSTRING, newString: IPointer[HSTRING]) -> int: ...
    
@combase.foreign(UINT32, HSTRING)
def WindowsGetStringLen(string: HSTRING) -> int: ...
    
@combase.foreign(PCWSTR, HSTRING, PUINT32)
def WindowsGetStringRawBuffer(string: HSTRING, length: IPointer[UINT32]) -> LPCWSTR: ...
    
@combase.foreign(BOOL, HSTRING, result_function=bool)
def WindowsIsStringEmpty(string: HSTRING) -> bool: ...
    
@combase_foreign(HSTRING, PBOOL)
def WindowsStringHasEmbeddedNull(string: HSTRING, hasEmbedNull: PBOOL) -> int: ...
    
@combase_foreign(HSTRING, HSTRING, PINT32)
def WindowsCompareStringOrdinal(string1: HSTRING, string2: HSTRING, 
                                result: IPointer[INT32]) -> int: ...

@combase_foreign(HSTRING, UINT32, PTR(HSTRING))
def WindowsSubstring(string: HSTRING, startIndex: int,
                    newString: IPointer[HSTRING]) -> int: ...

@combase_foreign(HSTRING, UINT32, UINT32, PTR(HSTRING))
def WindowsConcatString(string1: HSTRING, string2: HSTRING, 
                        newString: IPointer[HSTRING]) -> int: ...

@combase_foreign(HSTRING, HSTRING, HSTRING, PTR(HSTRING))
def WindowsReplaceString(string: HSTRING, stringReplaced: HSTRING,
                         stringReplacedWith: HSTRING, newString: IPointer[HSTRING]) -> int: ...

@combase_foreign(HSTRING, HSTRING, PTR(HSTRING))
def WindowsTrimStringStart(string: HSTRING, trimString: HSTRING,
                           newString: IPointer[HSTRING]) -> int: ...

@combase_foreign(HSTRING, HSTRING, PTR(HSTRING))
def WindowsTrimStringEnd(string: HSTRING, trimString: HSTRING, newString: HSTRING) -> int: ...