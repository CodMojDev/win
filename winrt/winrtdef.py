from .roapi import *

class WinRTInterfaceBase(COMInterface):
    _priv_checked_from_: type = None
    _exclusive_to_: list[str]
    
    def __init_subclass__(cls, *args, **kwargs):
        if cls._priv_checked_from_ != cls:
            for mro_cls in cls.__mro__:
                if mro_cls.__name__ == cls.__name__: continue
                if issubclass(mro_cls, WinRTInterfaceBase):
                    exclusive_to = getattr(mro_cls, '_exclusive_to_', None)
                    if exclusive_to is not None and cls.__name__ not in exclusive_to:
                        raise TypeError(f'Interface {mro_cls.__name__} is exclusive to {exclusive_to} classes.')
            cls._priv_checked_from_ = cls
        return super().__init_subclass__(*args, **kwargs)
    
class WinRTInterface(WinRTInterfaceBase, IInspectable):
    ...