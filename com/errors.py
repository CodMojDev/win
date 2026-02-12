class COMError(OSError):
    _errisolated = None
    
    @classmethod
    def _acquire_errisolated(cls):
        if cls._errisolated is None:
            from . import errisolated
            cls._errisolated = errisolated
    
    def __init__(self, hr: int):
        self._acquire_errisolated()
        super().__init__(self._errisolated.GetErrorMessage(hr))