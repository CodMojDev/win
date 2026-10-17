from win.shlwapi import *
from win.com.comdefbase import *
from typing import Self

URLIS_APPLIABLE = 0
URLIS_DIRECTORY = 1
URLIS_FILEURL = 2
URLIS_HASQUERY = 3
URLIS_NOHISTORY = 4
URLIS_OPAQUE = 5
URLIS_URL = 6
URLIS = UINT

@shlwapi.foreign(BOOL, LPCWSTR, URLIS)
def UrlIsW(pszUrl: WT_LPWSTR, UrlIs: int) -> int: ...

@shlwapi.foreign(HRESULT, LPCWSTR, PBYTE, DWORD)
def UrlHashW(pszUrl: WT_LPWSTR, pbHash: IPointer[BYTE], cbHash: int) -> int: ...

@shlwapi.foreign(HRESULT, LPCWSTR, LPWSTR, PDWORD, DWORD)
def UrlCreateFromPathW(pszPath: WT_LPWSTR, pszUrl: WT_LPWSTR, pcchUrl: IPointer[DWORD], dwFlags: int) -> int: ...

class URI:
    value: str
    
    def __init__(self, value: str):
        self.value = value
    
class URL(URI):
    def __hash__(self) -> int:
        nHash = SSIZE_T()
        hr = UrlHashW(self.value, i_cast(byref(nHash), PBYTE), sizeof(SSIZE_T))
        if FAILED(hr): raise COMError(hr)
        return nHash.value
    
    def is_file(self) -> bool:
        return UrlIsW(self.value, URLIS_FILEURL) != FALSE
    
    def is_opaque(self) -> bool:
        return UrlIsW(self.value, URLIS_OPAQUE) != FALSE
    
    @classmethod
    def path(cls, path: str) -> Self:
        """
        Create URL from path.
        """
        url = (WCHAR*512)()
        path = create_unicode_buffer(path)
        cchUrl = DWORD(512)
        hr = UrlCreateFromPathW(path, url, byref(cchUrl), 0)
        if FAILED(hr): raise COMError(hr)
        return cls(url.value)