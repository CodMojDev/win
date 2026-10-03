from .window import *
from .dataexchange import *
from win.com.ole2 import *

class Clipboard(Handle):
    """
    Classic Win32 Clipboard.
    """
    
    @classmethod
    def open(cls, owner: int | HANDLE = NULL):
        """
        Open the clipboard.
        """
        if isinstance(owner, HANDLE):
            owner = owner.value
        if not OpenClipboard(owner):
            raise WinException()
        return cls()
    
    def close(self):
        """
        Close the clipboard.
        """
        CloseClipboard()
        self._closed = True
        
    def set(self, clipboard_format: int, hData: int):
        """
        Insert the data to clipboard.
        """
        if not SetClipboardData(clipboard_format, hData):
            raise WinException()
        
class ClipboardEx:
    """
    Extended OLE Clipboard.
    """
    
    def set(self, data_object: IDataObject):
        """
        Insert the data object to clipboard.
        """
        hr = OleSetClipboard(data_object.ref())
        if FAILED(hr): raise COMError(hr)
        
    def get(self) -> DataObject:
        """
        Retrieve the data object from clipboard.
        """
        dataObj = DataObject.NULL()
        hr = OleGetClipboard(byref(dataObj))
        if FAILED(hr): raise COMError(hr)
        return dataObj.contents