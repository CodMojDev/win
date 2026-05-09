from win.com.comtl.baseface import TlIsMain
from typing import Callable, TYPE_CHECKING
from win.defbase_thread import *
from win.synchapi import *

import traceback

if TYPE_CHECKING:
    from ..window import Window

class Abs:
    class Thread(CThread):
        @classmethod
        def run(cls, callback: Callable[..., int], args=(), kwargs={}) -> 'Abs.Thread':
            def thread_worker(lParam: int):
                ExitThread(callback(*args, **kwargs) or 0)
            thread_worker_routine = LPTHREAD_START_ROUTINE(thread_worker)
            thread = super().create(thread_worker_routine)
            thread.thread_worker_routine = thread_worker_routine
            thread.thread_worker = thread_worker
            return thread
        
    class ThreadManager:
        threads: dict[int, tuple[CThread, bool]]
        windows: dict[int, 'Window']
        window: 'Window'
        
        def __init__(self, window: 'Window'):
            window.on_close += self.threadmgr_on_close
            self.threads = {}
            self.windows = {}
        
        def close(self, thread: CThread):
            self.threads[thread.tid] = (thread, False)
            if thread.alive:
                try:
                    thread.join(timeout=1000)
                except TimeoutError:
                    thread.terminate()
                finally:
                    thread.close()
        
        def threadmgr_on_close(self):
            for thread, alive in self.threads.values():
                self.close(thread)
            self.threads.clear()
                        
        def running(self):
            tid = GetCurrentThreadId()
            return tid in self.threads and self.threads[tid][1]
        
        def remove(self, thread: CThread):
            self.close(thread)
            del self.threads[thread.tid]
        
        def add(self, thread: CThread):
            self.threads[thread.tid] = (thread, thread.alive)
        
        def threadmgr_bindedwindow_on_message(self, msg: MSG):
            if msg.message in (WM_DESTROY, WM_QUIT):
                current = GetCurrentThreadId()
                window = self.windows[current]
                del self.windows[current]
                window.on_message -= self.threadmgr_bindedwindow_on_message
                return
                
            if msg.message != WM_CLOSE:
                if not self.running():
                    self.windows[GetCurrentThreadId()].close()
                    
        
        def bind(self, window: 'Window', tid: int):
            window.on_message += self.threadmgr_bindedwindow_on_message
            self.windows[tid] = window
    
    @staticmethod
    def run(entry_point: Callable, *args, **kwargs):
        if TlIsMain(1): return entry_point(*args, **kwargs)
        return None
    
    @staticmethod
    def run_async(entry_point: Callable, *args, **kwargs) -> 'Abs.Thread':
        if TlIsMain(1):
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