from .window import *
from .dataexchange import *
from win.com.ole2 import *

class Clipboard(Handle):
    @classmethod
    def open(cls, owner: int | HANDLE = NULL):
        if isinstance(owner, HANDLE):
            owner = owner.value
        if not OpenClipboard(owner):
            raise WinException()
        return cls()
    
    def close(self):
        CloseClipboard()
        self._closed = True
        
    def set(self, clipboard_format: int, hData: int):
        if not SetClipboardData(clipboard_format, hData):
            raise WinException()
        
class ClipboardEx:
    def set(self, data_object: IDataObject):
        hr = OleSetClipboard(data_object.ref())
        if FAILED(hr): raise COMError(hr)