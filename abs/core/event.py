from typing import Callable, Any

import random

class Priority(int):
    Min = 0
    Max = 0xffffffff

class EventCallback:
    def __init__(self, callback: Callable, priority: int | Priority = Priority.Min):
        self._unique_id = hash(callback.__code__.co_code)
        self._callback = callback
        self._priority = priority
        
    def __eq__(self, callback: 'EventCallback'):
        return self._unique_id == callback._unique_id and self._callback.__name__ == callback._callback.__name__
        
    def execute(self, *args, **kwargs) -> Any:
        return self._callback(*args, **kwargs)

class MultiEvent:
    _callbacks: list[EventCallback]
    _blocked: bool
    
    def __init__(self):
        self._callbacks = []
        self._blocked = False
    
    def _wrap_callback(self, callback: Callable | EventCallback) -> EventCallback:
        if isinstance(callback, EventCallback):
            return callback
        return EventCallback(callback)
    
    def __iadd__(self, callback):
        callback = self._wrap_callback(callback)
        self._callbacks.append(callback)
        self._callbacks = sorted(self._callbacks, key=lambda callback: callback._priority)
        return self
    
    def __isub__(self, callback):
        callback = self._wrap_callback(callback)
        self._callbacks.remove(callback)
        self._callbacks = sorted(self._callbacks, key=lambda callback: callback._priority)
        return self
    
    def empty(self) -> bool:
        return not self._callbacks or self._blocked
    
    def execute(self, *args, **kwargs) -> tuple[Any, ...]:
        if self._blocked:
            return ()
        return tuple(callback.execute(*args, **kwargs) for callback in self._callbacks)
    
    def block(self):
        self._blocked = True
        
    def unblock(self):
        self._blocked = False
        
    def clear(self):
        self._callbacks.clear()
        
class SingleEvent:
    _callback: Callable
    _blocked: bool
    
    def __init__(self):
        self._callback = None
        self._blocked = False
    
    def set(self, callback: Callable):
        self._callback = callback
        
    def execute(self, *args, **kwargs) -> Any:
        if self._blocked or self._callback is None:
            return None
        return self._callback(*args, **kwargs)
    
    def block(self):
        self._blocked = True
        
    def unblock(self):
        self._blocked = False
        
    def clear(self):
        self._callback = None