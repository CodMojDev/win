from . import cpreproc

if cpreproc.pragma_once('_MINWINBASE_'):
    from .sdkddkver import *
    from .winnt import *
    
    #
    # Typedefs
    #
    
    @CStructure.make
    class OVERLAPPED(CStructure):
        Offset: int
        OffsetHigh: int
        Pointer: IVoidPtr
        reset_annotations()
        
        Internal: IUlonglong
        InternalHigh: IUlonglong
        
        @CUnion.make
        class U(CUnion):
            @CStructure.make
            class S(CStructure):
                Offset: IDword
                OffsetHigh: IDword
            
            _s: IAnonymous[S]
            Pointer: IVoidPtr
        
        _u: IAnonymous[U]
    
    LPOVERLAPPED = OVERLAPPED.PTR()
    
    @CStructure.make
    class OVERLAPPED_ENTRY(CStructure):
        lpCompletionKey: IUlongPtr
        lpOverlapped: IPointer[OVERLAPPED]
        Internal: IUlongPtr
        dwNumberOfBytesTransferred: IDword
        
    LPOVERLAPPED_ENTRY = OVERLAPPED_ENTRY.PTR()
    
    if cpreproc.get_version() >= WIN32_WINNT_NT4:
        FINDEX_INFO_LEVELS = INT
        FindExInfoStandard = 0
        FindExInfoBasic = 1
        FindExInfoMaxInfoLevel = 2
        FIND_FIRST_EX_CASE_SENSITIVE = 0x00000001
        FIND_FIRST_EX_LARGE_FETCH = 0x00000002
        if cpreproc.get_version() >= WIN32_WINNT_WIN10:
            FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY = 0x00000004
            
            READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = INT
            PREAD_DIRECTORY_NOTIFY_INFORMATION_CLASS = PINT
            ReadDirectoryNotifyInformation           = 1
            ReadDirectoryNotifyExtendedInformation = 2
            ReadDirectoryNotifyFullInformation = 3
            ReadDirectoryNotifyMaximumInformation = 4

        FINDEX_SEARCH_OPS = INT
        FindExSearchNameMatch = 0
        FindExSearchLimitToDirectories = 1
        FindExSearchLimitToDevices = 2
        FindExSearchMaxSearchOp = 3

    GET_FILEEX_INFO_LEVELS = INT
    GetFileExInfoStandard = 0
    GetFileExMaxInfoLevel = 1

    if cpreproc.get_version() >= WIN32_WINNT_LONGHORN:
        FILE_INFO_BY_HANDLE_CLASS = INT
        PFILE_INFO_BY_HANDLE_CLASS = PINT
        FileBasicInfo = 0
        FileStandardInfo = 1
        FileNameInfo = 2
        FileRenameInfo = 3
        FileDispositionInfo = 4
        FileAllocationInfo = 5
        FileEndOfFileInfo = 6
        FileStreamInfo = 7
        FileCompressionInfo = 8
        FileAttributeTagInfo = 9
        FileIdBothDirectoryInfo = 10
        FileIdBothDirectoryRestartInfo = 11
        FileIoPriorityHintInfo = 12
        FileRemoteProtocolInfo = 13
        FileFullDirectoryInfo = 14
        FileFullDirectoryRestartInfo = 15
        if cpreproc.get_version() >= WIN32_WINNT_WIN8:
            FileStorageInfo = 16
            FileAlignmentInfo = 17
            FileIdInfo = 18
            FileIdExtdDirectoryInfo = 19
            FileIdExtdDirectoryRestartInf = 20
            MaximumFileInfoByHandleClass = 21
            if cpreproc.get_version() >= WIN32_WINNT_WIN10:
                FileDispositionInfoEx = 21
                FileRenameInfoEx = 22
                FileCaseSensitiveInfo = 23
                FileNormalizedNameInfo = 24
                MaximumFileInfoByHandleClass = 25
        else:
            MaximumFileInfoByHandleClass = 16

    LPOVERLAPPED_COMPLETION_ROUTINE = WINAPI(DWORD, DWORD, LPOVERLAPPED)

    LOCKFILE_FAIL_IMMEDIATELY =  0x00000001
    LOCKFILE_EXCLUSIVE_LOCK   =  0x00000002

    PROCESS_HEAP_REGION            =  0x0001
    PROCESS_HEAP_UNCOMMITTED_RANGE = 0x0002
    PROCESS_HEAP_ENTRY_BUSY        = 0x0004
    PROCESS_HEAP_SEG_ALLOC         = 0x0008
    PROCESS_HEAP_ENTRY_MOVEABLE    = 0x0010
    PROCESS_HEAP_ENTRY_DDESHARE    = 0x0020

    @CStructure.make
    class REASON_CONTEXT(CStructure):
        LocalizedReasonModule: HMODULE
        LocalizedReasonId: IUlong
        ReasonStringCount: IUlong
        ReasonStrings: IPointer[LPWSTR]
        reset_annotations()
        
        Version: IUlong
        Flags: IDword
        
        @CUnion.make
        class _Reason(CUnion):
            @CStructure.make
            class _Detailed(CStructure):
                LocalizedReasonModule: HMODULE
                LocalizedReasonId: IUlong
                ReasonStringCount: IUlong
                ReasonStrings: IPointer[LPWSTR]
                
            Detailed: _Detailed
            SimpleReasonStrings: LPWSTR
            
        Reason: _Reason
        
    PREASON_CONTEXT = REASON_CONTEXT.PTR()

    # 
    #  Debug APIs
    # 
    EXCEPTION_DEBUG_EVENT       = 1
    CREATE_THREAD_DEBUG_EVENT   = 2
    CREATE_PROCESS_DEBUG_EVENT  = 3
    EXIT_THREAD_DEBUG_EVENT     = 4
    EXIT_PROCESS_DEBUG_EVENT    = 5
    LOAD_DLL_DEBUG_EVENT        = 6
    UNLOAD_DLL_DEBUG_EVENT      = 7
    OUTPUT_DEBUG_STRING_EVENT   = 8
    RIP_EVENT                   = 9

    PTHREAD_START_ROUTINE = LPTHREAD_START_ROUTINE = WINAPI(DWORD, LPVOID)
    PENCLAVE_ROUTINE = LPENCLAVE_REOUTINE = WINAPI(LPVOID, LPVOID)

    @CStructure.make
    class EXCEPTION_DEBUG_INFO(CStructure):
        ExceptionRecord: EXCEPTION_RECORD
        dwFirstChance: IDword
    
    LPEXCEPTION_DEBUG_INFO = EXCEPTION_DEBUG_INFO.PTR()

    @CStructure.make
    class CREATE_THREAD_DEBUG_INFO(CStructure):
        hThread: IHandle
        lpThreadLocalBase: IVoidPtr
        lpStartAddress: LPTHREAD_START_ROUTINE
        
    LPCREATE_THREAD_DEBUG_INFO = CREATE_THREAD_DEBUG_INFO.PTR()


    @CStructure.make
    class CREATE_PROCESS_DEBUG_INFO(CStructure):
        hFile: IHandle
        hProcess: IHandle
        hThread: IHandle
        lpBaseOfImage: IVoidPtr
        dwDebugInfoFileOffset: IDword
        nDebugInfoSize: IDword
        lpThreadLocalBase: IVoidPtr
        lpStartAddress: LPTHREAD_START_ROUTINE
        lpImageName: IVoidPtr
        fUnicode: IWord
        
    LPCREATE_PROCESS_DEBUG_INFO = CREATE_PROCESS_DEBUG_INFO.PTR()
    
    @CStructure.make
    class EXIT_THREAD_DEBUG_INFO(CStructure):
        dwExitCode: IDword
        
    LPEXIT_THREAD_DEBUG_INFO = EXIT_THREAD_DEBUG_INFO.PTR()
    
    @CStructure.make
    class EXIT_PROCESS_DEBUG_INFO(CStructure):
        dwExitCode: IDword
        
    LPEXIT_PROCESS_DEBUG_INFO = EXIT_PROCESS_DEBUG_INFO.PTR()
    
    @CStructure.make
    class LOAD_DLL_DEBUG_INFO(CStructure):
        hFile: IHandle
        lpBaseOfDll: IVoidPtr
        dwDebugInfoFileOffset: IDword
        nDebugInfoSize: IDword
        lpImageName: IVoidPtr
        fUnicode: IWord
        
    LPLOAD_DLL_DEBUG_INFO = LOAD_DLL_DEBUG_INFO.PTR()
    
    @CStructure.make
    class UNLOAD_DLL_DEBUG_INFO(CStructure):
        lpBaseOfDll: IVoidPtr
        
    LPUNLOAD_DLL_DEBUG_INFO = UNLOAD_DLL_DEBUG_INFO.PTR()
    
    @CStructure.make
    class OUTPUT_DEBUG_STRING_INFO(CStructure):
        lpDebugStringData: LPSTR
        fUnicode: IWord
        nDebugStringLength: IWord
        
    LPOUTPUT_DEBUG_STRING_INFO = OUTPUT_DEBUG_STRING_INFO.PTR()
    
    @CStructure.make
    class RIP_INFO(CStructure):
        dwError: IDword
        dwType: IDword

    LPRIP_INFO = RIP_INFO.PTR()
    
    @CStructure.make
    class DEBUG_EVENT(CStructure):
        Exception: EXCEPTION_DEBUG_INFO
        CreateThread: CREATE_THREAD_DEBUG_INFO
        CreateProcessInfo: CREATE_PROCESS_DEBUG_INFO
        ExitThread: EXIT_THREAD_DEBUG_INFO
        ExitProcess: EXIT_PROCESS_DEBUG_INFO
        LoadDll: LOAD_DLL_DEBUG_INFO
        UnloadDll: UNLOAD_DLL_DEBUG_INFO
        DebugString: OUTPUT_DEBUG_STRING_INFO
        RipInfo: RIP_INFO
        
        reset_annotations()
        
        dwDebugEventCode: IDword
        dwProcessId: IDword
        dwThreadId: IDword
        
        @CUnion.make
        class U(CUnion):
            Exception: EXCEPTION_DEBUG_INFO
            CreateThread: CREATE_THREAD_DEBUG_INFO
            CreateProcessInfo: CREATE_PROCESS_DEBUG_INFO
            ExitThread: EXIT_THREAD_DEBUG_INFO
            ExitProcess: EXIT_PROCESS_DEBUG_INFO
            LoadDll: LOAD_DLL_DEBUG_INFO
            UnloadDll: UNLOAD_DLL_DEBUG_INFO
            DebugString: OUTPUT_DEBUG_STRING_INFO
            RipInfo: RIP_INFO
            
        _u: IAnonymous[U]
        
    LPDEBUG_EVENT = DEBUG_EVENT.PTR()

    # 
    #  Context definitions
    # 

    # 
    #  macros
    # 

    # compatibility macros
    STILL_ACTIVE                       = STATUS_PENDING
    EXCEPTION_ACCESS_VIOLATION         = STATUS_ACCESS_VIOLATION
    EXCEPTION_DATATYPE_MISALIGNMENT    = STATUS_DATATYPE_MISALIGNMENT
    EXCEPTION_BREAKPOINT               = STATUS_BREAKPOINT
    EXCEPTION_SINGLE_STEP              = STATUS_SINGLE_STEP
    EXCEPTION_ARRAY_BOUNDS_EXCEEDED    = STATUS_ARRAY_BOUNDS_EXCEEDED
    EXCEPTION_FLT_DENORMAL_OPERAND     = STATUS_FLOAT_DENORMAL_OPERAND
    EXCEPTION_FLT_DIVIDE_BY_ZERO       = STATUS_FLOAT_DIVIDE_BY_ZERO
    EXCEPTION_FLT_INEXACT_RESULT       = STATUS_FLOAT_INEXACT_RESULT
    EXCEPTION_FLT_INVALID_OPERATION    = STATUS_FLOAT_INVALID_OPERATION
    EXCEPTION_FLT_OVERFLOW             = STATUS_FLOAT_OVERFLOW
    EXCEPTION_FLT_STACK_CHECK          = STATUS_FLOAT_STACK_CHECK
    EXCEPTION_FLT_UNDERFLOW            = STATUS_FLOAT_UNDERFLOW
    EXCEPTION_INT_DIVIDE_BY_ZERO       = STATUS_INTEGER_DIVIDE_BY_ZERO
    EXCEPTION_INT_OVERFLOW             = STATUS_INTEGER_OVERFLOW
    EXCEPTION_PRIV_INSTRUCTION         = STATUS_PRIVILEGED_INSTRUCTION
    EXCEPTION_IN_PAGE_ERROR            = STATUS_IN_PAGE_ERROR
    EXCEPTION_ILLEGAL_INSTRUCTION      = STATUS_ILLEGAL_INSTRUCTION
    EXCEPTION_NONCONTINUABLE_EXCEPTION = STATUS_NONCONTINUABLE_EXCEPTION
    EXCEPTION_STACK_OVERFLOW           = STATUS_STACK_OVERFLOW
    EXCEPTION_INVALID_DISPOSITION      = STATUS_INVALID_DISPOSITION
    EXCEPTION_GUARD_PAGE               = STATUS_GUARD_PAGE_VIOLATION
    EXCEPTION_INVALID_HANDLE           = STATUS_INVALID_HANDLE
    # EXCEPTION_POSSIBLE_DEADLOCK        = STATUS_POSSIBLE_DEADLOCK
    CONTROL_C_EXIT                     = STATUS_CONTROL_C_EXIT

    # Local Memory Flags
    LMEM_FIXED         = 0x0000
    LMEM_MOVEABLE      = 0x0002
    LMEM_NOCOMPACT     = 0x0010
    LMEM_NODISCARD     = 0x0020
    LMEM_ZEROINIT      = 0x0040
    LMEM_MODIFY        = 0x0080
    LMEM_DISCARDABLE   = 0x0F00
    LMEM_VALID_FLAGS   = 0x0F72
    LMEM_INVALID_HANDLE= 0x8000

    LHND               = (LMEM_MOVEABLE | LMEM_ZEROINIT)
    LPTR               = (LMEM_FIXED | LMEM_ZEROINIT)

    NONZEROLHND        = (LMEM_MOVEABLE)
    NONZEROLPTR        = (LMEM_FIXED)

    # LocalDiscard( h )  = LocalReAlloc( (h), 0, LMEM_MOVEABLE )

    # Flags returned by LocalFlags (in addition to LMEM_DISCARDABLE)
    LMEM_DISCARDED     = 0x4000
    LMEM_LOCKCOUNT     = 0x00FF

    # 
    #  NUMA values
    # 

    NUMA_NO_PREFERRED_NODE = DWORD(-1).value