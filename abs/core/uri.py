from win.shlwapi import *
from win.com.comdefbase import *

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

class URI:
    ...
    
class URL:
    url: str
    
    def __init__(self, url: str):
        self.url = url
        
    def __hash__(self) -> int:
        nHash = SSIZE_T()
        hr = UrlHashW(self.url, i_cast(byref(nHash), PBYTE), sizeof(SSIZE_T))
        if FAILED(hr): raise COMError(hr)
        return nHash.value
    
    def is_file(self) -> bool:
        return UrlIsW(self.url, URLIS_FILEURL) != FALSE
    
    def is_opaque(self) -> bool:
        return UrlIsW(self.url, URLIS_OPAQUE) != FALSE
    
    def uri(self) -> URI:
        ...