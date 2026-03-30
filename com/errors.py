from typing import TYPE_CHECKING
from functools import wraps

if TYPE_CHECKING:
    from ..defbase  import interface_abstract_method, WT
    from ..defbase_errordef import WinErrors
else:
    def interface_abstract_method(f: 'WT') -> 'WT':
        @wraps(f)
        def _interface_abstract_method(*args, **kwargs):
            raise RuntimeError(f"'{f.__qualname__}' method is abstract.")
        _interface_abstract_method._abstract = True
        return _interface_abstract_method

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
        
class IErrorInfoProvider:
    _win_errors_list_: list['WinErrors'] = []
    
    @interface_abstract_method
    def get_win_errors_list(self) -> list['WinErrors']: ...
    
def register_error_info_provider(provider: IErrorInfoProvider):
    COMError._acquire_errisolated()
    COMError._errisolated._RegisterErrorInfoProvider(provider)
    
class _StdErrorInfoProvider(IErrorInfoProvider):
    _win_errors_list_ = None
    
    def get_win_errors_list(self) -> list['WinErrors']:
        return [COMError._errisolated.win_errors]