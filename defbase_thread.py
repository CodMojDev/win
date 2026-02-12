from .processthreadsapi import *
from .defbase_process import *
from .wow64apiset import *
from .handleapi import *
from .winnt import *

from datetime import datetime, timedelta

@kernel32.foreign(HLOCAL, HLOCAL)
def LocalFree(hMem: WT_ADDRLIKE) -> WT_ADDRLIKE: ...

THREAD_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xffff)

THREAD_PRIORITY_LOWEST          = THREAD_BASE_PRIORITY_MIN
THREAD_PRIORITY_BELOW_NORMAL    = (THREAD_PRIORITY_LOWEST+1)
THREAD_PRIORITY_NORMAL          = 0
THREAD_PRIORITY_HIGHEST         = THREAD_BASE_PRIORITY_MAX
THREAD_PRIORITY_ABOVE_NORMAL    = (THREAD_PRIORITY_HIGHEST-1)
THREAD_PRIORITY_ERROR_RETURN    = (MAXLONG)

THREAD_PRIORITY_TIME_CRITICAL   = THREAD_BASE_PRIORITY_LOWRT
THREAD_PRIORITY_IDLE            = THREAD_BASE_PRIORITY_IDLE

THREAD_MODE_BACKGROUND_BEGIN    = 0x00010000
THREAD_MODE_BACKGROUND_END      = 0x00020000

class CThread:
    handle: WT_ADDRLIKE
    is_wow64: bool
    tid: int
    
    @classmethod
    def remote(cls, process: CProcess, start_routine: WT_ADDRLIKE, 
               param: Optional[WT_ADDRLIKE] = NULL, 
               flags: int = 0, stack_size: int = 0,
               thread_attributes: SECURITY_ATTRIBUTES = NULL):
        start_routine = i_cast2(start_routine, LPTHREAD_START_ROUTINE)
        
        if thread_attributes is not NULL:
            thread_attributes = thread_attributes.ptr()
            
        remote_tid = DWORD()
        remote_handle = CreateRemoteThread(process.handle, thread_attributes, 
                                           stack_size, start_routine, 
                                           param, flags, byref(remote_tid))
        
        is_wow64_process = BOOL()
        is_wow64 = IsWow64Process(process.handle, byref(is_wow64_process))
        if is_wow64: is_wow64 = bool(is_wow64_process.value)
        
        remote_thread = cls(-1, is_wow64=is_wow64)
        remote_thread.handle = remote_handle
        remote_thread.tid = remote_tid.value
        
        return remote_thread
    
    def __init__(self, tid: int = None, is_wow64: bool = False):
        if tid == -1:
            self.handle = None
            self.tid = -1
            
            self.is_wow64 = is_wow64
            
            return
        
        if tid is None:
            is_wow64_process = BOOL()
            if IsWow64Process(GetCurrentProcessId(), byref(is_wow64_process)):
                self.is_wow64 = bool(is_wow64_process.value)
            else:
                self.is_wow64 = False
                
            self.handle = GetCurrentThread()
            handle = HANDLE()
            if not DuplicateHandle(self.handle, self.handle, self.handle,
                            byref(handle), 0, FALSE, DUPLICATE_SAME_ACCESS):
                raise OSError('Cannot duplicate handle for current thread.')
            self.handle = handle.value
            
            self.tid = GetCurrentThreadId()
            
            return
        
        self.handle = OpenThread(THREAD_ALL_ACCESS, False, tid)
        self.is_wow64 = is_wow64
        self.tid = tid
        
    def suspend(self):
        if self.is_wow64:
            result = Wow64SuspendThread(self.handle)
        else:
            result = SuspendThread(self.handle)
        if result == -1:
            raise OSError(f'Cannot suspend the thread TID {self.tid}.')
        
    def resume(self):
        if ResumeThread(self.handle) == -1:
            raise OSError(f'Cannot resume the thread TID {self.tid}.')
        
    @property
    def context(self) -> CONTEXT:
        if self.is_wow64:
            raise OSError('The thread is WOW64. Use CThread::wow64_context instead.')
        
        context = CONTEXT()
        context.ContextFlags = CONTEXT_CONTROL | CONTEXT_SEGMENTS | CONTEXT_INTEGER
        GetThreadContext(self.handle, context.ref())
        return context
    
    @context.setter
    def context(self, context: CONTEXT):
        SetThreadContext(self.handle, context.ref())
        
    @property
    def wow64_context(self) -> WOW64_CONTEXT:
        if not self.is_wow64:
            raise OSError('The thread is not in the WOW64. Use CThread::context instead.')
        
        context = WOW64_CONTEXT()
        context.ContextFlags = WOW64_CONTEXT_CONTROL | WOW64_CONTEXT_SEGMENTS | WOW64_CONTEXT_INTEGER
        Wow64GetThreadContext(self.handle, context.ref())
        return context
    
    @wow64_context.setter
    def wow64_context(self, context: WOW64_CONTEXT):
        if not self.is_wow64:
            raise OSError('The thread is not in the WOW64. Use CThread::context = context instead.')
        
        Wow64SetThreadContext(self.handle, context.ref())
        
    def terminate(self, exit_code: int = 0):
        if not TerminateThread(self.handle, exit_code):
            raise OSError(f'Cannot terminate the thread TID {self.tid}.')
        
    def __repr__(self) -> str:
        return f'<CThread tid={self.tid} handle={self.handle}>'
    
    @property
    def priority(self) -> int:
        return GetThreadPriority(self.handle)
    
    @priority.setter
    def priority(self, priority: int):
        SetThreadPriority(self.handle, priority)
        
    @property
    def times(self) -> tuple[datetime, datetime, datetime, datetime]:
        creationTime = FILETIME()
        exitTime = FILETIME()
        kernelTime = FILETIME()
        userTime = FILETIME()
        
        GetThreadTimes(self.handle, 
                       creationTime.ref(), exitTime.ref(), 
                       kernelTime.ref(), userTime.ref())
        
        nCreationTime = i_cast2(creationTime.ref(), PINT64).contents.value
        nExitTime = i_cast2(exitTime.ref(), PINT64).contents.value
        nKernelTime = i_cast2(kernelTime.ref(), PINT64).contents.value
        nUserTime = i_cast2(userTime.ref(), PINT64).contents.value
        
        creation_us = (nCreationTime - 116444736000000000) // 10
        exit_us = (nExitTime - 116444736000000000) // 10
        kernel_us = (nKernelTime - 116444736000000000) // 10
        user_us = (nUserTime - 116444736000000000) // 10
        
        creation_time = datetime(1970, 1, 1) + timedelta(microseconds=creation_us)
        exit_time = datetime(1970, 1, 1) + timedelta(microseconds=exit_us)
        kernel_time = datetime(1970, 1, 1) + timedelta(microseconds=kernel_us)
        user_time = datetime(1970, 1, 1) + timedelta(microseconds=user_us)
        
        return (creation_time, exit_time, kernel_time, user_time)
    
    @property
    def creation_time(self) -> datetime:
        return self.times[0]
    
    @property
    def exit_time(self) -> datetime:
        return self.times[1]
    
    @property
    def kernel_time(self) -> datetime:
        return self.times[2]
    
    @property
    def user_time(self) -> datetime:
        return self.times[3]
    
    @property
    def description(self) -> str:
        from ctypes import POINTER
        pDesc = POINTER(WCHAR)()
        GetThreadDescription(self.handle, byref(pDesc))
        if pDesc:
            result = cast(pDesc, LPWSTR).value
            LocalFree(pDesc)
            return result
    
    @description.setter
    def description(self, description: str):
        SetThreadDescription(self.handle, description)
    
    def close(self):
        if self.handle:
            CloseHandle(self.handle)