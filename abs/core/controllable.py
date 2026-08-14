from win.minwindef import *

class ControllableValue:
    value: int
    
    _released: bool
    _closed: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._released = False
        self._closed = False
    
    @classmethod
    def foreign_owner(cls, val: int | HANDLE, *args, **kwargs) -> defb_t.Self | None:
        """
        Create the handle instance from foreign handle.
        """
        instance = cls(val).exchange_owner()
        if instance.invalid(): return None # if invalid handle was provided, when return None
        instance.initialize_from_foreign(*args, **kwargs)
        return instance
    
    def exchange_owner(self):
        """
        Exchange the owner of handle from local -> foreign, or foreign -> local.
        """
        self._closed = not self._closed
        return self
    
    def __enter__(self):
        self._released = False
        self._closed = False
        return self
        
    def __exit__(self, *_):
        if not self._released:
            self._released = True
            if not self.invalid():
                self.close()
            
    def __del__(self):
        if not self._closed and not self.invalid():
            self.close()
    
    @interface_abstract_method 
    def close(self):
        """
        Abstract method to release the handle.
        """
        
    def invalid(self) -> bool:
        """
        Check this handle is invalid.
        """
        return not self.value
    
    def initialize_from_foreign(self, *args, **kwargs):
        """
        Virtual method for initialize handle instance from foreign arguments.
        """
        return
    
class Handle(ControllableValue, HANDLE):
    """
    Main Win32 abstract handle wrapper.
    """