from typing import Callable, Any

class Priority(int):
    Min = 0
    Max = 0xffffffff

class EventCallback:
    def __init__(self, callback: Callable, priority: int | Priority = Priority.Min):
        self._callback = callback
        self._priority = priority
        
    def execute(self, *args, **kwargs) -> Any:
        return self._callback(*args, **kwargs)

class Event:
    _callbacks: list[EventCallback]
    
    def __init__(self):
        self._callbacks = []
    
    def _wrap_callback(self, callback: Callable | EventCallback) -> EventCallback:
        if isinstance(callback, EventCallback):
            return callback
        return EventCallback(callback)
    
    def __iadd__(self, callback):
        callback = self._wrap_callback(callback)
        self._callbacks.append(callback)    
        return self
    
    def __isub__(self, callback):
        callback = self._wrap_callback(callback)
        self._callbacks.remove(callback)
        return self
    
    def execute(self, *args, **kwargs) -> tuple[Any, ...]:
        callbacks = sorted(self._callbacks, key=lambda callback: callback._priority)
        return tuple(callback.execute(*args, **kwargs) for callback in callbacks)