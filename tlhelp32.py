"""
/*****************************************************************************
*                                                                             *
* tlhelp32.h -  WIN32 tool help functions, types, and definitions             *
*                                                                             *
* Version 1.0                                                                 *
*                                                                             *
* NOTE: windows.h/winbase.h must be #included first                           *
*                                                                             *
* Copyright (c) Microsoft Corp.  All rights reserved.                         *
*                                                                             *
 *****************************************************************************/
"""

from .minwindef import *

from . import cpreproc

from .defbase import *

if cpreproc.pragma_once("_INC_TOOLHELP32"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Desktop Family ***

    MAX_MODULE_NAME32 = 255

    ### Shapshot function #######################

    CreateToolhelp32Snapshot = declare(kernel32.CreateToolhelp32Snapshot, HANDLE, DWORD, DWORD)

    #
    # The th32ProcessID argument is only used if TH32CS_SNAPHEAPLIST or
    # TH32CS_SNAPMODULE is specified. th32ProcessID == 0 means the current
    # process.
    #
    # NOTE that all of the snapshots are global except for the heap and module
    #      lists which are process specific. To enumerate the heap or module
    #      state for all WIN32 processes call with TH32CS_SNAPALL and the
    #      current process. Then for each process in the TH32CS_SNAPPROCESS
    #      list that isn't the current process, do a call with just
    #      TH32CS_SNAPHEAPLIST and/or TH32CS_SNAPMODULE.
    #
    # dwFlags
    #
    TH32CS_SNAPHEAPLIST = 0x00000001
    TH32CS_SNAPPROCESS  = 0x00000002
    TH32CS_SNAPTHREAD   = 0x00000004
    TH32CS_SNAPMODULE   = 0x00000008
    TH32CS_SNAPMODULE32 = 0x00000010
    TH32CS_SNAPALL      = (TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE)
    TH32CS_INHERIT      = 0x80000000
    #
    # Use CloseHandle to destroy the snapshot
    #

    ##### heap walking ##############################

    class HEAPLIST32(CStructure):
        _fields_ = [
            ("dwSize", SIZE_T),
            ("th32ProcessID", DWORD),  # owning process
            ("th32HeapID", ULONG_PTR), # heap (in owning process's context!)
            ("dwFlags", DWORD)
        ]
    PHEAPLIST32 = LPHEAPLIST32 = POINTER(HEAPLIST32)
    #
    # dwFlags
    #
    HF32_DEFAULT     = 1  # process's default heap
    HF32_SHARED      = 2  # is shared heap

    Heap32ListFirst = declare(kernel32.Heap32ListFirst, BOOL, HANDLE, LPHEAPLIST32)

    Heap32ListNext = declare(kernel32.Heap32ListNext, BOOL, HANDLE, LPHEAPLIST32)

    class HEAPENTRY32(CStructure):
        _fields_ = [
            ("dwSize", SIZE_T),
            ("hHandle", HANDLE),     # Handle of this heap block
            ("dwAddress", ULONG_PTR),   # Linear address of start of block
            ("dwBlockSize", SIZE_T), # Size of block in bytes
            ("dwFlags", DWORD),
            ("dwLockCount", DWORD),
            ("dwResvd", DWORD),
            ("th32ProcessID", DWORD),   # owning process
            ("th32HeapID", ULONG_PTR)      # heap block is in
        ]
    PHEAPENTRY32 = LPHEAPENTRY32 = POINTER(HEAPENTRY32)
    #
    # dwFlags
    #
    LF32_FIXED    = 0x00000001
    LF32_FREE     = 0x00000002
    LF32_MOVEABLE = 0x00000004

    Heap32First = declare(kernel32.Heap32First, BOOL, LPHEAPENTRY32, DWORD, ULONG_PTR)

    Heap32Next = declare(kernel32.Heap32Next, BOOL, LPHEAPENTRY32, DWORD, ULONG_PTR)

    Toolhelp32ReadProcessMemory = declare(kernel32.Toolhelp32ReadProcessMemory, BOOL, DWORD, LPCVOID, LPVOID, SIZE_T, PSIZE_T)


    #### Process walking ######################

    class PROCESSENTRY32W(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("cntUsage", DWORD),
            ("th32ProcessID", DWORD),          # this process
            ("th32DefaultHeapId", ULONG_PTR),
            ("th32ModuleID", DWORD),           # associated exe
            ("cntThreads", DWORD),
            ("th32ParentProcessID", DWORD),    # this process's parent process
            ("pcPriClassBase", LONG),          # Base priority of process's threads
            ("dwFlags", DWORD),
            ("szExeFile", WCHAR * MAX_PATH)    # Path
        ]
    PPROCESSENTRY32W = LPPROCESSENTRY32W = POINTER(PROCESSENTRY32W)

    Process32FirstW = declare(kernel32.Process32FirstW, BOOL, HANDLE, LPPROCESSENTRY32W)

    Process32NextW = declare(kernel32.Process32NextW, BOOL, HANDLE, LPPROCESSENTRY32W)

    class PROCESSENTRY32(CStructure):
        create_string_buffer = [
            ("dwSize", DWORD),
            ("cntUsage", DWORD),
            ("th32ProcessID", DWORD),          # this process
            ("th32DefaultHeapID", DWORD),
            ("th32ModuleID", DWORD),           # associated exe
            ("cntThreads", DWORD),
            ("th32ParentProcessID", DWORD),    # this process's parent process
            ("pcPriClassBase", LONG),          # Base priority of process's threads
            ("dwFlags", DWORD),
            ("szExeFile", CHAR * MAX_PATH)     # Path
        ]
    PPROCESSENTRY32 = LPPROCESSENTRY32 = POINTER(PROCESSENTRY32)

    Process32First = declare(kernel32.Process32First, BOOL, HANDLE, LPPROCESSENTRY32)

    Process32Next = declare(kernel32.Process32Next, BOOL, HANDLE, LPPROCESSENTRY32)


    if cpreproc.ifdef("UNICODE"):
        Process32First = Process32FirstW
        Process32Next = Process32NextW
        PROCESSENTRY32 = PROCESSENTRY32W
        PPROCESSENTRY32 = PPROCESSENTRY32W
        LPPROCESSENTRY32 = LPPROCESSENTRY32W

    ##### Thread walking #############################

    class THREADENTRY32(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("cntUsage", DWORD),
            ("th32ThreadID", DWORD),       # this thread
            ("th32OwnerProcessID", DWORD), # Process this thread is associated wit
            ("tpBasePri", LONG),
            ("tpDeltaPri", LONG),
            ("dwFlags", DWORD)
        ]
    PTHREADENTRY32 = LPTHREADENTRY32 = POINTER(THREADENTRY32)

    Thread32First = declare(kernel32.Thread32First, BOOL, HANDLE, LPTHREADENTRY32)

    Thread32Next = declare(kernel32.Thread32Next, BOOL, HANDLE, LPTHREADENTRY32)

    ##### Module walking ##########################

    class MODULEENTRY32W(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("th32ModuleID", DWORD),       # This module
            ("th32ProcessID", DWORD),      # owning process
            ("GlblcntUsage", DWORD),       # Global usage count on the module
            ("ProccntUsage", DWORD),       # Module usage count in th32ProcessID's context
            ("modBaseAddr", PBYTE),        # Base address of module in th32ProcessID's context
            ("modBaseSize", DWORD),        # Size in bytes of module starting at modBaseAddr
            ("hModule", HMODULE),          # The hModule of this module in th32ProcessID's context
            ("szModule", WCHAR * (MAX_MODULE_NAME32 + 1)),
            ("szExePath", WCHAR * MAX_PATH)
        ]
    PMODULEENTRY32W = LPMODULEENTRY32W = POINTER(MODULEENTRY32W)

    Module32FirstW = declare(kernel32.Module32FirstW, BOOL, HANDLE, LPMODULEENTRY32W)

    Module32NextW = declare(kernel32.Module32NextW, BOOL, HANDLE, LPMODULEENTRY32W)

    class MODULEENTRY32(CStructure):
        _fields_ = [
            ("dwSize", DWORD),
            ("th32ModuleID", DWORD),       # This module
            ("th32ProcessID", DWORD),      # owning process
            ("GlblcntUsage", DWORD),       # Global usage count on the module
            ("ProccntUsage", DWORD),       # Module usage count in th32ProcessID's context
            ("modBaseAddr", PBYTE),        # Base address of module in th32ProcessID's context
            ("modBaseSize", DWORD),        # Size in bytes of module starting at modBaseAddr
            ("hModule", HMODULE),          # The hModule of this module in th32ProcessID's context
            ("szModule", CHAR * (MAX_MODULE_NAME32 + 1)),
            ("szExePath", CHAR * MAX_PATH)
        ]
    PMODULEENTRY32 = LPMODULEENTRY32 = POINTER(MODULEENTRY32)

    #
    # NOTE CAREFULLY that the modBaseAddr and hModule fields are valid ONLY
    # in th32ProcessID's process context.
    #

    Module32First = declare(kernel32.Module32First, BOOL, HANDLE, LPMODULEENTRY32)

    Module32Next = declare(kernel32.Module32Next, BOOL, HANDLE, LPMODULEENTRY32)

    if cpreproc.ifdef("UNICODE"):
        Module32First = Module32FirstW
        Module32Next = Module32NextW
        MODULEENTRY32 = MODULEENTRY32W
        PMODULEENTRY32 = PMODULEENTRY32W
        LPMODULEENTRY32 = LPMODULEENTRY32W

    # REGION ***

# _INC_TOOLHELP32
