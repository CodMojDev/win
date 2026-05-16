from typing import Callable, TYPE_CHECKING
from win.defbase_thread import *
from win.synchapi import *

import traceback

if TYPE_CHECKING:
    from ..window import Window

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
        
        def __init__(self):
            self.property_map = {}
            self._abs_managed = True
            
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
        
    class ThreadManager:
        """
        WinAbs thread manager.
        """
        
        threads: dict[int, tuple[CThread, bool]]
        windows: dict[int, 'Window']
        window: 'Window'
        
        def __init__(self, window: 'Window'):
            # bind the thread manager on_close event to window on_close
            window.on_close += self.threadmgr_on_close
            
            # setup the thread manager dictionaries
            self.threads = {}
            self.windows = {}
        
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
                    print('[Abs.Thread] Exception')
                    traceback.print_exc()
                    return 1
                return 0
            
            return Abs.Thread.run(thread_worker, args, kwargs)
        return None