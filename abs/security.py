from win.winnt import *
from win.defbase_errordef import *

kernel32 = get_win_library('kernel32.dll')
advapi32 = get_win_library('advapi32.dll')

@kernel32.foreign(HLOCAL, HLOCAL)
def LocalFree(hMem: int) -> int: ...

@advapi32.foreign(BOOL, PSID, PTR(LPWSTR))
def ConvertSidToStringSidW(Sid: IPointer[SID], StringSid: IPointer[LPWSTR]) -> int: ...

@advapi32.foreign(BOOL, LPCWSTR, PSID)
def ConvertStringSidToSidW(StringSid: WT_LPWSTR, Sid: IPointer[SID]) -> int: ...

@advapi32.foreign(BOOL, PSID, PSID)
def EqualSid(pSid1: IPointer[SID], pSid2: IPointer[SID]) -> int: ...

class Sid(SID):
    def __str__(self) -> str:
        StringSid = LPWSTR()
        if not ConvertSidToStringSidW(self.ref(), byref(StringSid)):
            raise WinException()
        result = StringSid.value
        LocalFree(StringSid)
        return result
    
    def __repr__(self) -> str:
        return f'<SID {self}>'
    
    def __eq__(self, other: SID) -> bool:
        return EqualSid(self.ref(), other.ref()) != FALSE
    
    def __ne__(self, other: SID) -> bool:
        return EqualSid(self.ref(), other.ref()) != TRUE
    
    @classmethod
    def string(cls, string: str) -> 'Sid':
        sid = Sid()
        if not ConvertStringSidToSidW(string, sid.ref()):
            raise WinException()
        return sid