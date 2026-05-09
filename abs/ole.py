from .dragdrop import *

class OLE:
    def __enter__(self):
        hr = OleInitialize(NULL)
        if FAILED(hr): raise COMError(hr)
        
    def __exit__(self, exc_type, exc, tb):
        hr = OleUninitialize()
        if FAILED(hr): raise COMError(hr)