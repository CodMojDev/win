from typing import Callable, TYPE_CHECKING
from win.defbase_thread import *
from win.synchapi import *
from win.winuser import user32

import threading
import traceback
import queue

if TYPE_CHECKING:
    from .handle import CriticalSection, Win32Event
    from ..window import Window, Application
    
@user32.foreign(BOOL)
def SetProcessDPIAware() -> int: ...

def _abs_is_main(stack_level: int = 0) -> bool:
    # check upper frame + stack_level is running as main script (standard __name__ == __main__ check)
    return get_py_frame(1 + stack_level).f_locals['__name__'] == '__main__'

class Abs:
    """
    Main WinAbs class for entry points and threads.
    """
    
    class Object:
        """
        WinAbs object.
        """
        
        property_map: dict[str, Any]
        reference_list: list[Any]
        
        def __init__(self):
            self.property_map = {}
            self.reference_list = []
            self._abs_managed = True
            
        def add_ref(self, obj: Any):
            self.reference_list.append(obj)
            
        def remove_ref(self, obj: Any):
            self.reference_list.remove(obj)
            
    @staticmethod
    def managed(obj: Any) -> bool:
        """
        Check object is WinAbs-managed.
        """
        
        return hasattr(obj, '_abs_managed')
    
    class Thread(CThread):
        """
        WinAbs thread.
        """
        
        @classmethod
        def run(cls, callback: Callable[..., int], args=(), kwargs={}) -> 'Abs.Thread':
            """
            Run WinAbs thread with thread callback.
            """
            
            def thread_worker(lParam: int):
                ExitThread(callback(*args, **kwargs) or 0)
            thread_worker_routine = LPTHREAD_START_ROUTINE(thread_worker)
            thread = super().create(thread_worker_routine)
            thread.thread_worker_routine = thread_worker_routine
            thread.thread_worker = thread_worker
            return thread
        
    class ThreadHolder:
        """
        WinAbs thread holder.
        """
        
        queue: queue.Queue[tuple[str, ...]]
        lock: threading.Lock
        crit: 'CriticalSection'
        
        def __init__(self):
            from .handle import CriticalSection
            
            self.crit = CriticalSection()
            self.lock = threading.Lock()
            self.queue = queue.Queue()
            
        def worker(self):
            """
            WinAbs thread worker.
            """
    
    class ThreadManager:
        """
        WinAbs thread manager.
        """
        
        threads: dict[int, tuple[CThread, bool]]
        windows: dict[int, 'Window']
        window: 'Window'
        
        def __init__(self, window: 'Window'=None):
            # bind the thread manager on_close event to window on_close
            if window is not None:
                window.on_close += self.threadmgr_on_close
            
            # setup the thread manager dictionaries
            self.threads = {}
            self.windows = {}
            
        def bind_to_app(self, app: 'Application'):
            """
            Bind thread manager on-destroy event handler to application event cycle.
            """
            
            app.on_destroy += self.threadmgr_on_close
        
        def close(self, thread: CThread):
            """
            Close the thread.
            """
            
            # set the thread manager state to thread alive=False
            self.threads[thread.tid] = (thread, False)
            if thread.alive: # if thread is alive
                try: # try waiting for thread, 1 sec
                    thread.join(timeout=1000)
                except TimeoutError: # if timeout exceeded,
                    thread.terminate() # when terminate thread
                finally:
                    # finally, close the thread handle
                    thread.close()
        
        def threadmgr_on_close(self):
            # close all threads
            for thread, _ in self.threads.values():
                self.close(thread)
            # clear threads dictionary
            self.threads.clear()
            return True
                        
        def running(self):
            """
            Function for testing current thread is running in WinAbs Thread manager.
            """
            
            tid = GetCurrentThreadId()
            return tid in self.threads and self.threads[tid][1]
        
        def remove(self, thread: CThread):
            """
            Remove thread from thread manager.
            """
            
            self.close(thread)
            del self.threads[thread.tid]
        
        def add(self, thread: CThread, automatic_alive: bool = False):
            """
            Add thread to thread manager.
            """
            
            self.threads[thread.tid] = (thread, automatic_alive or thread.alive)
    
    @staticmethod
    def run(entry_point: Callable, *args, **kwargs):
        """
        Run the WinAbs entry point.
        """
        
        SetProcessDPIAware()
        if _abs_is_main(1): return entry_point(*args, **kwargs)
        return None
    
    @staticmethod
    def run_async(entry_point: Callable, *args, **kwargs) -> 'Abs.Thread':
        """
        Asynchronously run the WinAbs entry point.
        """
        
        if _abs_is_main(1):
            def thread_worker() -> int:
                try:
                    entry_point(*args, **kwargs)
                except Exception:
                    print('Exception in WinAbs entry thread:')
                    traceback.print_exc()
                    return 1
                return 0
            
            return Abs.Thread.run(thread_worker, args, kwargs)
        return None
    
    class Synchronization:
        @staticmethod
        def wait(timeout: int = INFINITE, *objects):
            length = len(objects)
            
            if length == 0:
                Sleep(timeout)
                return
            
            if length == 1:
                wait_object, = objects
                
                if isinstance(wait_object, CThread):
                    wait_object = wait_object.handle
                elif isinstance(wait_object, HANDLE):
                    wait_object = wait_object.value
                elif isinstance(wait_object, int): pass
                else:
                    raise TypeError(type(wait_object))
                
                result = WaitForSingleObject(wait_object, timeout)
            else:
                wait_objects = []
                
                for wait_object in objects:
                    if isinstance(wait_object, CThread):
                        wait_object = wait_object.handle
                    elif isinstance(wait_object, HANDLE):
                        wait_object = wait_object.value
                    elif isinstance(wait_object, int): pass
                    else:
                        raise TypeError(type(wait_object))
                    wait_objects.append(wait_object)
                
                wait_objects = (HANDLE * length)(*wait_objects)
                result = WaitForMultipleObjects(length, wait_objects, TRUE, timeout)
                
            if result == WAIT_TIMEOUT:
                raise TimeoutError('Time elapsed, 1 or more objects is not signaled.')
            elif result == WAIT_OBJECT_0: pass
            else:
                raise WinException()