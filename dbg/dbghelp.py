"""
    This module defines the prototypes and constants required for the image
    help routines.

    Contains debugging support routines that are redistributable.
"""

from ..winnt import *

if cpreproc.pragma_once('_DBGHELP_'):
    DbgHelp = get_win_library('DbgHelp.dll')
    
    IMAGE_SEPARATION = (64*1024)
    
    # Observant readers may notice that 2 new fields,
    # 'fReadOnly' and 'Version' have been added to
    # the LOADED_IMAGE structure after 'fDOSImage'.
    # This does not change the size of the structure
    # from previous headers.  That is because while
    # 'fDOSImage' is a byte, it is padded by the
    # compiler to 4 bytes.  So the 2 new fields are
    # slipped into the extra space.

    @CStructure.make
    class LOADED_IMAGE(CStructure):
        ModuleName: PSTR
        hFile: IHandle
        MappedAddress: PUCHAR
        
        if cpreproc.ifdef('_WIN64'):
            FileHeader: IPointer[IMAGE_NT_HEADERS64]
        else:
            FileHeader: IPointer[IMAGE_NT_HEADERS32]
            
        LastRvaSection: IPointer[IMAGE_SECTION_HEADER]
        NumberOfSections: int
        Sections: IPointer[IMAGE_SECTION_HEADER]
        Characteristics: int
        fSystemImage: IBool
        fDOSImage: IBool
        fReadOnly: IBool
        Version: IInt8
        Links: LIST_ENTRY
        SizeOfImage: int
        
    PLOADED_IMAGE = LOADED_IMAGE.PTR()
    
    # Error codes set by dbghelp functions.  Call GetLastError
    # to see them.
    # Dbghelp also sets error codes found in winerror.h

    ERROR_IMAGE_NOT_STRIPPED    = 0x8800  # the image is not stripped.  No dbg file available.
    ERROR_NO_DBG_POINTER        = 0x8801  # image is stripped but there is no pointer to a dbg file
    ERROR_NO_PDB_POINTER        = 0x8802  # image does not point to a pdb file
    
    PFIND_DEBUG_FILE_CALLBACK = WINAPI(BOOL, HANDLE, PCSTR, PVOID)
    PFIND_DEBUG_FILE_CALLBACKW = WINAPI(BOOL, HANDLE, PCWSTR, PVOID)
    
    @DbgHelp.foreign(HANDLE, HANDLE, PCSTR, PSTR, PFIND_DEBUG_FILE_CALLBACK, PVOID)
    def SymFindDebugInfoFile(
        hProcess: HANDLE,
        FileName: PCSTR,
        DebugFilePath: PSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, HANDLE, PCWSTR, PWSTR, PFIND_DEBUG_FILE_CALLBACKW, PVOID)
    def SymFindDebugInfoFileW(
        hProcess: HANDLE,
        FileName: PCWSTR,
        DebugFilePath: PWSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCSTR, PCSTR, PSTR)
    def FindDebugInfoFile(
        FileName: PCSTR, 
        SymbolPath: PCSTR,
        DebugFilePath: PSTR) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCSTR, PCSTR, PSTR,
                     PFIND_DEBUG_FILE_CALLBACK, PVOID)
    def FindDebugInfoFileEx(
        FileName: PCSTR, 
        SymbolPath: PCSTR,
        DebugFilePath: PSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCWSTR, PCWSTR, PSTR)
    def FindDebugInfoFileW(
        FileName: PCWSTR, 
        SymbolPath: PCWSTR,
        DebugFilePath: PWSTR) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCWSTR, PCWSTR, PWSTR,
                     PFIND_DEBUG_FILE_CALLBACKW, PVOID)
    def FindDebugInfoFileExW(
        FileName: PCWSTR, 
        SymbolPath: PCWSTR,
        DebugFilePath: PWSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    PFINDFILEINPATHCALLBACK = WINAPI(BOOL, PCSTR, PVOID)
    
    @DbgHelp.foreign(BOOL, HANDLE, PCSTR, PCSTR, PVOID,
                     DWORD, DWORD, DWORD, PSTR,
                     PFINDFILEINPATHCALLBACK, PVOID,
                     result_function=bool)
    def SymFindFileInPath(
        hprocess: HANDLE,
        SearchPath: PCSTR,
        FileName: PCSTR,
        id: PVOID,
        two: int,
        three: int,
        flags: int,
        FoundFile: PSTR,
        callback: FARPROC,
        context: PVOID) -> bool: ...
    
    PFINDFILEINPATHCALLBACKW = WINAPI(BOOL, PCWSTR, PVOID)
    
    @DbgHelp.foreign(BOOL, HANDLE, PCWSTR, PCWSTR, PVOID,
                     DWORD, DWORD, DWORD, PWSTR,
                     PFINDFILEINPATHCALLBACKW, PVOID,
                     result_function=bool)
    def SymFindFileInPathW(
        hprocess: HANDLE,
        SearchPath: PCWSTR,
        FileName: PCWSTR,
        id: PVOID,
        two: int,
        three: int,
        flags: int,
        FoundFile: PWSTR,
        callback: FARPROC,
        context: PVOID) -> bool: ...
    
    PFIND_EXE_FILE_CALLBACK = WINAPI(BOOL, HANDLE, PCSTR, PVOID)
    PFIND_EXE_FILE_CALLBACKW = WINAPI(BOOL, HANDLE, PCWSTR, PVOID)
    
    @DbgHelp.foreign(HANDLE, HANDLE, PCSTR, PSTR, 
                     PFIND_EXE_FILE_CALLBACK, PVOID)
    def SymFindExecutableImage(
        hProcess: HANDLE,
        FileName: PCSTR,
        ImageFilePath: PSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, HANDLE, PCWSTR, PWSTR, 
                     PFIND_EXE_FILE_CALLBACKW, PVOID)
    def SymFindExecutableImageW(
        hProcess: HANDLE,
        FileName: PCWSTR,
        ImageFilePath: PWSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCSTR, PCSTR, PSTR)
    def FindExecutableImage(
        FileName: PCSTR,
        SymbolPath: PCSTR,
        ImageFilePath: PSTR) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCSTR, PCSTR, PSTR, 
                     PFIND_EXE_FILE_CALLBACK, PVOID)
    def FindExecutableImageEx(
        FileName: PCSTR,
        SymbolPath: PCSTR,
        ImageFilePath: PSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCWSTR, PCWSTR, PWSTR)
    def FindExecutableImageW(
        FileName: PCWSTR,
        SymbolPath: PCWSTR,
        ImageFilePath: PWSTR) -> int: ...
    
    @DbgHelp.foreign(HANDLE, PCWSTR, PCWSTR, PWSTR,
                     PFIND_DEBUG_FILE_CALLBACKW, PVOID)
    def FindExecutableImageExW(
        FileName: PCWSTR,
        SymbolPath: PCWSTR,
        ImageFilePath: PWSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> int: ...
    
    @DbgHelp.foreign(PIMAGE_NT_HEADERS, PVOID)
    def ImageNtHeader(Base: PVOID) -> IPointer[IMAGE_NT_HEADERS64 | IMAGE_NT_HEADERS32]: ...
    
    @DbgHelp.foreign(PVOID, PVOID, BOOLEAN, USHORT, PULONG,
                     PTR(PIMAGE_SECTION_HEADER))
    def ImageDirectoryEntryToDataEx(
        Base: PVOID,
        MappedAsImage: bool,
        DirectoryEntry: int,
        Size: PULONG,
        FoundHeader: IDoublePtr[IMAGE_SECTION_HEADER]) -> int: ...
    
    @DbgHelp.foreign(PVOID, PVOID, BOOLEAN, USHORT, PULONG)
    def ImageDirectoryEntryToData(
        Base: PVOID,
        MappedAsImage: bool,
        DirectoryEntry: int,
        Size: PULONG) -> int: ...
    
    @DbgHelp.foreign(PIMAGE_SECTION_HEADER,
                     PIMAGE_NT_HEADERS,
                     PVOID, ULONG)
    def ImageRvaToSection(
        NtHeaders: IPointer[IMAGE_NT_HEADERS64 | IMAGE_NT_HEADERS32],
        Base: PVOID, Rva: int) -> IPointer[IMAGE_SECTION_HEADER]: ...
    
    @DbgHelp.foreign(PVOID, PIMAGE_NT_HEADERS, PVOID, ULONG,
                     PTR(PIMAGE_SECTION_HEADER))
    def ImageRvaToVa(
        NtHeaders: IPointer[IMAGE_NT_HEADERS64 | IMAGE_NT_HEADERS32],
        Base: PVOID, Rva: int, 
        LastRvaSection: IDoublePtr[IMAGE_SECTION_HEADER]) -> int: ...
    
    if cpreproc.ifndef('_WIN64'):
        @CStructure.make
        class IMAGE_DEBUG_INFORMATION(CStructure):
            List: LIST_ENTRY
            ReservedSize: IDword
            ReservedMappedBase: IVoidPtr
            ReservedMachine: IUshort
            ReservedCharacteristics: IUshort
            ReservedCheckSum: IDword
            ImageBase: IDword
            SizeOfImage: IDword
            
            ReservedNumberOfSections: IDword
            ReservedSections: IPointer[IMAGE_SECTION_HEADER]
            
            ReservedExportedNamesSize: IDword
            ReservedExportedNames: PSTR
            
            ReservedNumberOfFunctionTableEntries: IDword
            ReservedFunctionTableEntries: IVoidPtr # IPointer[IMAGE_FUNCTION_ENTRY]
            ReservedLowestFunctionStartingAddress: IDword
            ReservedHighestFunctionEndingAddress: IDword
            
            ReservedNumberOfFpoTableEntries: IDword
            ReservedFpoTableEntries: IVoidPtr # IPointer[FPO_DATA]
            
            SizeOfCoffSymbols: IDword
            CoffSymbols: IVoidPtr # IPointer[IMAGE_COFF_SYMBOLS_HEADER]
            
            ReservedSizeOfCodeViewSymbols: IDword
            ReservedCodeViewSymbols: IVoidPtr
            
            ImageFilePath: PSTR
            ImageFileName: PSTR
            ReservedDebugFilePath: PSTR
            
            ReservedTimeDateStamp: IDword
            
            ReservedRomImage: IBool
            ReservedDebugDirectory: IVoidPtr # IPointer[IMAGE_DEBUG_DIRECTORY]
            ReservedNumberOfDebugDirectories: IDword
            
            ReservedOriginalFunctionTableBaseAddress: IDword
            
            Reserved: IArrayFixedSize[DWORD, 2]
            
        PIMAGE_DEBUG_INFORMATION = IMAGE_DEBUG_INFORMATION.PTR()
        
        @DbgHelp.foreign(PIMAGE_DEBUG_INFORMATION, HANDLE,
                         PCSTR, PCSTR, ULONG)
        def MapDebugInformation(
            FileHandle: HANDLE, 
            FileName: PCSTR,
            SymbolPath: PCSTR,
            ImageBase: int) -> IPointer[IMAGE_DEBUG_INFORMATION]: ...
        
        @DbgHelp.foreign(BOOL, PIMAGE_DEBUG_INFORMATION,
                         result_function=bool)
        def UnmapDebugInformation(DebugInfo: IPointer[IMAGE_DEBUG_INFORMATION]) -> bool: ...
        
    @DbgHelp.foreign(BOOL, PCSTR, PCSTR, PSTR,
                     result_function=bool)
    def SearchTreeForFile(
        RootPath: PCSTR, 
        InputPathName: PCSTR,
        OutputPathBuffer: PSTR) -> bool: ...
    
    @DbgHelp.foreign(BOOL, PCWSTR, PCWSTR, PWSTR,
                     result_function=bool)
    def SearchTreeForFileW(
        RootPath: PCWSTR, 
        InputPathName: PCWSTR,
        OutputPathBuffer: PWSTR) -> bool: ...
    
    PENUMDIRTREE_CALLBACK = CALLBACK(BOOL, PCSTR, PVOID)
    
    @DbgHelp.foreign(BOOL, HANDLE, PCSTR, PCSTR,
                     PSTR, PENUMDIRTREE_CALLBACK, 
                     PVOID, result_function=bool)
    def EnumDirTree(
        hProcess: HANDLE,
        RootPath: PCSTR,
        InputPathName: PCSTR,
        OutputPathBuffer: PSTR,
        cb: FARPROC,
        data: PVOID) -> bool: ...
    
    PENUMDIRTREE_CALLBACKW = CALLBACK(BOOL, PCWSTR, PVOID)
    
    @DbgHelp.foreign(BOOL, HANDLE, PCWSTR, PCWSTR,
                     PWSTR, PENUMDIRTREE_CALLBACKW, 
                     PVOID, result_function=bool)
    def EnumDirTreeW(
        hProcess: HANDLE,
        RootPath: PCWSTR,
        InputPathName: PCWSTR,
        OutputPathBuffer: PWSTR,
        cb: FARPROC,
        data: PVOID) -> bool: ...
    
    @DbgHelp.foreign(BOOL, PCSTR, result_function=bool)
    def MakeSureDirectoryPathExists(DirPath: PCSTR) -> bool: ...
    
    #
    # UnDecorateSymbolName Flags
    #

    UNDNAME_COMPLETE                 = (0x0000)  # Enable full undecoration
    UNDNAME_NO_LEADING_UNDERSCORES   = (0x0001)  # Remove leading underscores from MS extended keywords
    UNDNAME_NO_MS_KEYWORDS           = (0x0002)  # Disable expansion of MS extended keywords
    UNDNAME_NO_FUNCTION_RETURNS      = (0x0004)  # Disable expansion of return type for primary declaration
    UNDNAME_NO_ALLOCATION_MODEL      = (0x0008)  # Disable expansion of the declaration model
    UNDNAME_NO_ALLOCATION_LANGUAGE   = (0x0010)  # Disable expansion of the declaration language specifier
    UNDNAME_NO_MS_THISTYPE           = (0x0020)  # NYI Disable expansion of MS keywords on the 'this' type for primary declaration
    UNDNAME_NO_CV_THISTYPE           = (0x0040)  # NYI Disable expansion of CV modifiers on the 'this' type for primary declaration
    UNDNAME_NO_THISTYPE              = (0x0060)  # Disable all modifiers on the 'this' type
    UNDNAME_NO_ACCESS_SPECIFIERS     = (0x0080)  # Disable expansion of access specifiers for members
    UNDNAME_NO_THROW_SIGNATURES      = (0x0100)  # Disable expansion of 'throw-signatures' for functions and pointers to functions
    UNDNAME_NO_MEMBER_TYPE           = (0x0200)  # Disable expansion of 'static' or 'virtual'ness of members
    UNDNAME_NO_RETURN_UDT_MODEL      = (0x0400)  # Disable expansion of MS model for UDT returns
    UNDNAME_32_BIT_DECODE            = (0x0800)  # Undecorate 32-bit decorated names
    UNDNAME_NAME_ONLY                = (0x1000)  # Crack only the name for primary declaration;
                                                 #  return just [scope::]name.  Does expand template params
    UNDNAME_NO_ARGUMENTS             = (0x2000)  # Don't undecorate arguments to function
    UNDNAME_NO_SPECIAL_SYMS          = (0x4000)  # Don't undecorate special names (v-table, vcall, vector xxx, metatype, etc)
    
    @DbgHelp.foreign(DWORD, PCSTR, PSTR, DWORD, DWORD)
    def UnDecorateSymbolName(
        name: PCSTR, 
        outputString: PSTR,
        maxStringLength: int,
        flags: int) -> int: ...
    
    @DbgHelp.foreign(DWORD, PCWSTR, PWSTR, DWORD, DWORD)
    def UnDecorateSymbolNameW(
        name: PCWSTR, 
        outputString: PWSTR,
        maxStringLength: int,
        flags: int) -> int: ...
    
    #
    # these values are used for synthesized file types
    # that can be passed in as image headers instead of
    # the standard ones from ntimage.h
    #

    DBHHEADER_DEBUGDIRS     = 0x1
    DBHHEADER_CVMISC        = 0x2
    DBHHEADER_PDBGUID       = 0x3

    @CStructure.make
    class MODLOAD_DATA(CStructure):
        ssize: IDword                  # size of this struct
        ssig: IDword                   # signature identifying the passed data
        data: IVoidPtr                 # pointer to passed data
        size: IDword                   # size of passed data
        flags: IDword                  # options
        
    PMODLOAD_DATA = MODLOAD_DATA.PTR()

    @CStructure.make
    class MODLOAD_CVMISC(CStructure):
        oCV: IDword                    # ofset to the codeview record
        cCV: ISizeT                    # size of the codeview record
        oMisc: IDword                  # offset to the misc record
        cMisc: ISizeT                  # size of the misc record
        dtImage: IDword                # datetime stamp of the image
        cImage: IDword                 # size of the image
        
    PMODLOAD_CVMISC = MODLOAD_CVMISC.PTR()

    @CStructure.make
    class MODLOAD_PDBGUID_PDBAGE(CStructure):
        PdbGuid: GUID                # Pdb Guid
        PdbAge: IDword               # Pdb Age
        
    PMODLOAD_PDBGUID_PDBAGE = MODLOAD_PDBGUID_PDBAGE.PTR()

    #
    # StackWalking API
    #
    AddrMode1616 = 0
    AddrMode1632 = 1
    AddrModeReal = 2
    AddrModeFlat = 3
    ADDRESS_MODE = INT

    @CStructure.make
    class ADDRESS64(CStructure):
        Offset: IUInt64
        Segment: IWord
        Mode: IInteger[ADDRESS_MODE]
        
    LPADDRESS64 = ADDRESS64.PTR()

    if cpreproc.ifdef('_WIN64'):
        ADDRESS = ADDRESS64
        LPADDRESS = LPADDRESS64
    else:
        @CStructure.make
        class ADDRESS(CStructure):
            Offset: IDword
            Segment: IWord
            Mode: IInteger[ADDRESS_MODE]
            
        LPADDRESS = ADDRESS.PTR()
        
        def Address32To64(a32: IPointer[ADDRESS],
                          a64: IPointer[ADDRESS64]):
            a64.contents.Offset = ULONG64(LONG64(LONG(a32.contents.Offset).value).value).value
            a64.contents.Segment = a32.contents.Segment
            a64.contents.Mode = a32.contents.Mode
            
        def Address64To32(a64: IPointer[ADDRESS64],
                          a32: IPointer[ADDRESS]):
            a32.contents.Offset = ULONG(a64.contents.Offset).value
            a32.contents.Segment = a64.contents.Segment
            a32.contents.Mode = a64.contents.Mode

    
    # This structure is included in the STACKFRAME structure,
    # and is used to trace through usermode callbacks in a thread's
    # kernel stack.  The values must be copied by the kernel debugger
    # from the DBGKD_GET_VERSION and WAIT_STATE_CHANGE packets.
    
    @CStructure.make
    class KDHELP64(CStructure):
        """
        New KDHELP structure for 64 bit system support.
        This structure is preferred in new code.
        """

        #
        # address of kernel thread object, as provided in the
        # WAIT_STATE_CHANGE packet.
        #
        Thread: IInt64

        #
        # offset in thread object to pointer to the current callback frame
        # in kernel stack.
        #
        ThCallbackStack: IDword

        #
        # offset in thread object to pointer to the current callback backing
        # store frame in kernel stack.
        #
        ThCallbackBStore: IDword

        #
        # offsets to values in frame:
        #
        # address of next callback frame
        NextCallback: IDword

        # address of saved frame pointer (if applicable)
        FramePointer: IDword


        #
        # Address of the kernel function that calls out to user mode
        #
        KiCallUserMode: IInt64

        #
        # Address of the user mode dispatcher function
        #
        KeUserCallbackDispatcher: IInt64

        #
        # Lowest kernel mode address
        #
        SystemRangeStart: IInt64

        #
        # Address of the user mode exception dispatcher function.
        # Added in API version 10.
        #
        KiUserExceptionDispatcher: IInt64

        #
        # Stack bounds, added in API version 11.
        #
        StackBase: IInt64
        StackLimit: IInt64

        #
        # Target OS build number. Added in API version 12.
        #
        BuildVersion: IDword
        RetpolineStubFunctionTableSize: IDword
        RetpolineStubFunctionTable: IInt64
        RetpolineStubOffset: IDword
        RetpolineStubSize: IDword
        Reserved0: IArrayFixedSize[DWORD64, 2]

    PKDHELP64 = KDHELP64.PTR()

    if cpreproc.ifdef('_WIN64'):
        KDHELP = KDHELP64
        PKDHELP = PKDHELP64
    else:
        @CStructure.make
        class KDHELP(CStructure):
            #
            # address of kernel thread object, as provided in the
            # WAIT_STATE_CHANGE packet.
            #
            Thread: IDword

            #
            # offset in thread object to pointer to the current callback frame
            # in kernel stack.
            #
            ThCallbackStack: IDword

            #
            # offsets to values in frame:
            #
            # address of next callback frame
            NextCallback: IDword

            # address of saved frame pointer (if applicable)
            FramePointer: IDword

            #
            # Address of the kernel function that calls out to user mode
            #
            KiCallUserMode: IDword

            #
            # Address of the user mode dispatcher function
            #
            KeUserCallbackDispatcher: IDword

            #
            # Lowest kernel mode address
            #
            SystemRangeStart: IDword

            #
            # offset in thread object to pointer to the current callback backing
            # store frame in kernel stack.
            #
            ThCallbackBStore: IDword

            #
            # Address of the user mode exception dispatcher function.
            # Added in API version 10.
            #
            KiUserExceptionDispatcher: IDword

            #
            # Stack bounds, added in API version 11.
            #
            StackBase: IDword
            StackLimit: IDword

            Reserved: IArrayFixedSize[DWORD, 5]

        PKDHELP = KDHELP.PTR()

    def KdHelp32To64(p32: IPointer[KDHELP],
                     p64: IPointer[KDHELP64]):
        p64.contents.Thread = p32.contents.Thread
        p64.contents.ThCallbackStack = p32.contents.ThCallbackStack
        p64.contents.NextCallback = p32.contents.NextCallback
        p64.contents.FramePointer = p32.contents.FramePointer
        p64.contents.KiCallUserMode = p32.contents.KiCallUserMode
        p64.contents.KeUserCallbackDispatcher = p32.contents.KeUserCallbackDispatcher
        p64.contents.SystemRangeStart = p32.contents.SystemRangeStart
        p64.contents.KiUserExceptionDispatcher = p32.contents.KiUserExceptionDispatcher
        p64.contents.StackBase = p32.contents.StackBase
        p64.contents.StackLimit = p32.contents.StackLimit
        
    @CStructure.make
    class STACKFRAME64(CStructure):
        AddrPc: ADDRESS64                       # program counter
        AddrReturn: ADDRESS64                   # return address
        AddrFrame: ADDRESS64                    # frame pointer
        AddrStack: ADDRESS64                    # stack pointer
        AddrBStore: ADDRESS64                   # backing store pointer
        FuncTableEntry: IVoidPtr                # pointer to pdata/fpo or NULL
        Params: IArrayFixedSize[DWORD64, 4]     # possible arguments to the function
        Far: IBool                              # WOW far call
        Virtual: IBool                          # is this a virtual frame?
        Reserved: IArrayFixedSize[DWORD64, 3]
        KdHelp: KDHELP64

    LPSTACKFRAME64 = STACKFRAME64.PTR()

    INLINE_FRAME_CONTEXT_INIT   = 0
    INLINE_FRAME_CONTEXT_IGNORE = 0xFFFFFFFF

    @CStructure.make
    class STACKFRAME_EX(CStructure):
        # First, STACKFRAME64 structure
        AddrPC: ADDRESS64                   # program counter
        AddrReturn: ADDRESS64               # return address
        AddrFrame: ADDRESS64                # frame pointer
        AddrStack: ADDRESS64                # stack pointer
        AddrBStore: ADDRESS64               # backing store pointer
        FuncTableEntry: IVoidPtr            # pointer to pdata/fpo or NULL
        Params: IArrayFixedSize[DWORD64, 4] # possible arguments to the function
        Far: IBool                          # WOW far call
        Virtual: IBool                      # is this a virtual frame?
        Reserved: IArrayFixedSize[DWORD64, 3]
        KdHelp: KDHELP64

        # Extended STACKFRAME fields
        StackFrameSize: IDword
        InlineFrameContext: IDword
        
    LPSTACKFRAME_EX = STACKFRAME_EX.PTR()

    if cpreproc.ifdef('_WIN64'):
        STACKFRAME = STACKFRAME64
        LPSTACKFRAME = LPSTACKFRAME64
    else:
        @CStructure.make
        class STACKFRAME(CStructure):
            AddrPC: ADDRESS                     # program counter
            AddrReturn: ADDRESS                 # return address
            AddrFrame: ADDRESS                  # frame pointer
            AddrStack: ADDRESS                  # stack pointer
            FuncTableEntry: IVoidPtr            # pointer to pdata/fpo or NULL
            Params: IArrayFixedSize[DWORD, 4]   # possible arguments to the function
            Far: IBool                          # WOW far call
            Virtual: IBool                      # is this a virtual frame?
            Reserved: IArrayFixedSize[DWORD, 3]
            KdHelp: KDHELP
            AddrBStore: ADDRESS                 # backing store pointer
            
        LPSTACKFRAME = STACKFRAME.PTR()

    PREAD_PROCESS_MEMORY_ROUTINE64 = WINAPI(BOOL, HANDLE, DWORD64, PVOID, DWORD, LPDWORD)
    PFUNCTION_TABLE_ACCESS_ROUTINE64 = WINAPI(PVOID, HANDLE, DWORD64)
    PGET_MODULE_BASE_ROUTINE64 = WINAPI(DWORD64, HANDLE, DWORD64)
    PTRANSLATE_ADDRESS_ROUTINE64 = WINAPI(DWORD64, HANDLE, HANDLE, LPADDRESS64)

    # Target Attributes:
    #

    # Asks the caller to return a 64-bit mask which indicates which bits in a code address are PAC
    # bits.  This attribute is only relevant for ARM64 debug targets.  The attribute data must be the address
    # for which the PAC mask is being fetched.  This allows the caller to deal with differences in PAC masks for
    # ARM64 EL0/1/2.  If PAC is disabled or the attribute does not apply, FALSE should be returned from the attribute 
    # getter.  If the special value TARGET_ATTRIBUTE_PACMASK_LIVETARGET is returned, the PAC mask for the call 
    # is assumed to be the same as the PAC mask for the currently running process.
    #
    TARGET_ATTRIBUTE_PACMASK = 0x00000001

    # Target Attribute Special Values:
    #
    TARGET_ATTRIBUTE_PACMASK_LIVETARGET = 0xFFFFFFFFFFFFFFFF

    PGET_TARGET_ATTRIBUTE_VALUE64 = WINAPI(BOOL, HANDLE, DWORD, DWORD64, DWORD64)
    
    @DbgHelp.foreign(BOOL, DWORD, HANDLE, HANDLE, LPSTACKFRAME64,
                     PVOID, PREAD_PROCESS_MEMORY_ROUTINE64,
                     PFUNCTION_TABLE_ACCESS_ROUTINE64,
                     PGET_MODULE_BASE_ROUTINE64,
                     PTRANSLATE_ADDRESS_ROUTINE64, result_function=bool)
    def StackWalk64(
        MachineType: int,
        hProcess: HANDLE,
        hThread: HANDLE,
        StackFrame: IPointer[STACKFRAME64],
        ContextRecord: PVOID,
        ReadMemoryRoutine: FARPROC,
        FunctionTableAccessRoutine: FARPROC,
        GetModuleBaseRoutine: FARPROC,
        TranslateAddress: FARPROC) -> bool: ...

    SYM_STKWALK_DEFAULT         = 0x00000000
    SYM_STKWALK_FORCE_FRAMEPTR  = 0x00000001
    SYM_STKWALK_ZEROEXTEND_PTRS = 0x00000002
    
    @DbgHelp.foreign(BOOL, DWORD, HANDLE, HANDLE, 
                     LPSTACKFRAME_EX, PVOID,
                     PREAD_PROCESS_MEMORY_ROUTINE64,
                     PFUNCTION_TABLE_ACCESS_ROUTINE64,
                     PGET_MODULE_BASE_ROUTINE64,
                     PTRANSLATE_ADDRESS_ROUTINE64,
                     DWORD, result_function=bool)
    def StackWalkEx(
        MachineType: int,
        hProcess: HANDLE,
        hThread: HANDLE,
        StackFrame: IPointer[STACKFRAME_EX],
        ContextRecord: PVOID,
        ReadMemoryRoutine: FARPROC,
        FunctionTableAccessRoutine: FARPROC,
        GetModuleBaseRoutine: FARPROC,
        TranslateAddress: FARPROC,
        Flags: int) -> bool: ...
    
    @DbgHelp.foreign(BOOL, DWORD, HANDLE, HANDLE, 
                     LPSTACKFRAME_EX, PVOID,
                     PREAD_PROCESS_MEMORY_ROUTINE64,
                     PFUNCTION_TABLE_ACCESS_ROUTINE64,
                     PGET_MODULE_BASE_ROUTINE64,
                     PTRANSLATE_ADDRESS_ROUTINE64,
                     PGET_TARGET_ATTRIBUTE_VALUE64,
                     DWORD, result_function=bool)
    def StackWalk2(
        MachineType: int,
        hProcess: HANDLE,
        hThread: HANDLE,
        StackFrame: IPointer[STACKFRAME_EX],
        ContextRecord: PVOID,
        ReadMemoryRoutine: FARPROC,
        FunctionTableAccessRoutine: FARPROC,
        GetModuleBaseRoutine: FARPROC,
        TranslateAddress: FARPROC,
        GetTargetAttributeValue: FARPROC,
        Flags: int) -> bool: ...
    
    if cpreproc.ifdef('_WIN64'):
        PREAD_PROCESS_MEMORY_ROUTINE = PREAD_PROCESS_MEMORY_ROUTINE64
        PFUNCTION_TABLE_ACCESS_ROUTINE = PFUNCTION_TABLE_ACCESS_ROUTINE64
        PGET_MODULE_BASE_ROUTINE = PGET_MODULE_BASE_ROUTINE64
        PTRANSLATE_ADDRESS_ROUTINE = PTRANSLATE_ADDRESS_ROUTINE64
        PGET_TARGET_ATTRIBUTE_VALUE = PGET_TARGET_ATTRIBUTE_VALUE64
        
        StackWalk = StackWalk64
    else:
        PREAD_PROCESS_MEMORY_ROUTINE = WINAPI(BOOL, HANDLE, DWORD, PVOID, DWORD, LPDWORD)
        PFUNCTION_TABLE_ACCESS_ROUTINE = WINAPI(PVOID, HANDLE, DWORD)
        PGET_MODULE_BASE_ROUTINE = WINAPI(DWORD, HANDLE, DWORD)
        PTRANSLATE_ADDRESS_ROUTINE = WINAPI(DWORD, HANDLE, HANDLE, LPADDRESS)
        PGET_TARGET_ATTRIBUTE_VALUE = WINAPI(BOOL, HANDLE, DWORD, DWORD, DWORD)
        
        @DbgHelp.foreign(BOOL, DWORD, HANDLE, HANDLE, LPSTACKFRAME,
                        PVOID, PREAD_PROCESS_MEMORY_ROUTINE,
                        PFUNCTION_TABLE_ACCESS_ROUTINE,
                        PGET_MODULE_BASE_ROUTINE,
                        PTRANSLATE_ADDRESS_ROUTINE, result_function=bool)
        def StackWalk(
            MachineType: int,
            hProcess: HANDLE,
            hThread: HANDLE,
            StackFrame: IPointer[STACKFRAME],
            ContextRecord: PVOID,
            ReadMemoryRoutine: FARPROC,
            FunctionTableAccessRoutine: FARPROC,
            GetModuleBaseRoutine: FARPROC,
            TranslateAddress: FARPROC) -> bool: ...
        
    @CStructure.make
    class API_VERSION(CStructure):
        MajorVersion: IUshort
        MinorVersion: IUshort
        Revision: IUshort
        Reserved: IUshort
        
    LPAPI_VERSION = API_VERSION.PTR()
    
    @DbgHelp.foreign(LPAPI_VERSION)
    def ImagehlpApiVersion() -> IPointer[API_VERSION]: ...
    
    @DbgHelp.foreign(LPAPI_VERSION, LPAPI_VERSION)
    def ImagehlpApiVersionEx(
        AppVersion: IPointer[API_VERSION]
        ) -> IPointer[API_VERSION]: ...
    
    @DbgHelp.foreign(DWORD, HMODULE)
    def GetTimestampForLoadedLibrary(Module: HMODULE) -> int: ...
    
    #
    # typedefs for function pointers
    #
    
    PSYM_ENUMMODULES_CALLBACK64 = CALLBACK(BOOL, PCSTR, DWORD64, PVOID)
    PSYM_ENUMMODULES_CALLBACKW64 = CALLBACK(BOOL, PCWSTR, DWORD64, PVOID)
    PENUMLOADED_MODULES_CALLBACK64 = CALLBACK(BOOL, PCSTR, DWORD64, ULONG, PVOID)
    PENUMLOADED_MODULES_CALLBACKW64 = CALLBACK(BOOL, PCSTR, DWORD64, ULONG, PVOID)
    PSYM_ENUMSYMBOLS_CALLBACK64 = CALLBACK(BOOL, PCSTR, DWORD64, ULONG, PVOID)
    PSYM_ENUMSYMBOLS_CALLBACK64W = CALLBACK(BOOL, PCWSTR, DWORD64, ULONG, PVOID)
    PSYMBOL_REGISTERED_CALLBACK64 = CALLBACK(BOOL, HANDLE, ULONG, ULONG64, ULONG64)
    PSYMBOL_FUNCENTRY_CALLBACK = CALLBACK(PVOID, HANDLE, DWORD, PVOID)
    PSYMBOL_FUNCENTRY_CALLBACK64 = CALLBACK(PVOID, HANDLE, ULONG64, ULONG64)
    
    if cpreproc.ifdef('_WIN64'):
        PSYM_ENUMMODULES_CALLBACK = PSYM_ENUMMODULES_CALLBACK64
        PSYM_ENUMSYMBOLS_CALLBACK = PSYM_ENUMSYMBOLS_CALLBACK64
        PSYM_ENUMSYMBOLS_CALLBACKW = PSYM_ENUMSYMBOLS_CALLBACK64W
        PENUMLOADED_MODULES_CALLBACK = PENUMLOADED_MODULES_CALLBACK64
        PSYMBOL_REGISTERED_CALLBACK = PSYMBOL_REGISTERED_CALLBACK64
        PSYMBOL_FUNCENTRY_CALLBACK = PSYMBOL_FUNCENTRY_CALLBACK64
    else:
        PSYM_ENUMMODULES_CALLBACK = CALLBACK(BOOL, PCSTR, DWORD, PVOID)
        PSYM_ENUMMODULES_CALLBACKW = CALLBACK(BOOL, PCWSTR, DWORD, PVOID)
        PENUMLOADED_MODULES_CALLBACK = CALLBACK(BOOL, PCSTR, DWORD, ULONG, PVOID)
        PENUMLOADED_MODULES_CALLBACKW = CALLBACK(BOOL, PCSTR, DWORD, ULONG, PVOID)
        PSYM_ENUMSYMBOLS_CALLBACK = CALLBACK(BOOL, PCSTR, DWORD, ULONG, PVOID)
        PSYM_ENUMSYMBOLS_CALLBACKW = CALLBACK(BOOL, PCWSTR, DWORD, ULONG, PVOID)
        PSYMBOL_REGISTERED_CALLBACK = CALLBACK(BOOL, HANDLE, ULONG, ULONG, ULONG)
        PSYMBOL_FUNCENTRY_CALLBACK = CALLBACK(PVOID, HANDLE, DWORD, PVOID)
        PSYMBOL_FUNCENTRY_CALLBACK = CALLBACK(PVOID, HANDLE, ULONG, ULONG)
        
    # values found in SYMBOL_INFO.Tag
    #
    # This was taken from cvconst.h and should
    # not override any values found there.
    #
    # #define _NO_CVCONST_H_ if you don't
    # have access to that file...

    if cpreproc.ifdef('_NO_CVCONST_H'):
        # DIA enums
        SymTagNull = 0
        SymTagExe = 1
        SymTagCompiland = 2
        SymTagCompilandDetails = 3
        SymTagCompilandEnv = 4
        SymTagFunction = 5
        SymTagBlock = 6
        SymTagData = 7
        SymTagAnnotation = 8
        SymTagLabel = 9
        SymTagPublicSymbol = 10
        SymTagUDT = 11
        SymTagEnum = 12
        SymTagFunctionType = 13
        SymTagPointerType = 14
        SymTagArrayType = 15
        SymTagBaseType = 16
        
        SymTagTypedef = 17
        SymTagBaseClass = 18
        SymTagFriend = 19
        SymTagFunctionArgType = 20
        SymTagFuncDebugStart = 21
        SymTagFuncDebugEnd = 22
        SymTagUsingNamespace = 23
        SymTagVTableShape = 24
        SymTagVTable = 25
        SymTagCustom = 26
        SymTagThunk = 27
        SymTagCustomType = 28
        SymTagManagedType = 29
        SymTagDimension = 30
        SymTagCallSite = 31
        SymTagInlineSite = 32
        SymTagBaseInterface = 33
        SymTagVectorType = 34
        SymTagMatrixType = 35
        SymTagHLSLType = 36
        SymTagCaller = 37
        SymTagCallee = 38
        SymTagExport = 39
        SymTagHeapAllocationSite = 40
        SymTagCoffGroup = 41
        SymTagMax = 42
        SymTagEnum = INT

    #
    # flags found in SYMBOL_INFO.Flags
    #

    SYMFLAG_VALUEPRESENT        = 0x00000001
    SYMFLAG_REGISTER            = 0x00000008
    SYMFLAG_REGREL              = 0x00000010
    SYMFLAG_FRAMEREL            = 0x00000020
    SYMFLAG_PARAMETER           = 0x00000040
    SYMFLAG_LOCAL               = 0x00000080
    SYMFLAG_CONSTANT            = 0x00000100
    SYMFLAG_EXPORT              = 0x00000200
    SYMFLAG_FORWARDER           = 0x00000400
    SYMFLAG_FUNCTION            = 0x00000800
    SYMFLAG_VIRTUAL             = 0x00001000
    SYMFLAG_THUNK               = 0x00002000
    SYMFLAG_TLSREL              = 0x00004000
    SYMFLAG_SLOT                = 0x00008000
    SYMFLAG_ILREL               = 0x00010000
    SYMFLAG_METADATA            = 0x00020000
    SYMFLAG_CLR_TOKEN           = 0x00040000
    SYMFLAG_NULL                = 0x00080000
    SYMFLAG_FUNC_NO_RETURN      = 0x00100000
    SYMFLAG_SYNTHETIC_ZEROBASE  = 0x00200000
    SYMFLAG_PUBLIC_CODE         = 0x00400000
    SYMFLAG_REGREL_ALIASINDIR   = 0x00800000
    SYMFLAG_FIXUP_ARM64X        = 0x01000000
    SYMFLAG_GLOBAL              = 0x02000000
    SYMFLAG_COMPLEX             = 0x04000000

    # this resets SymNext/Prev to the beginning
    # of the module passed in the address field

    SYMFLAG_RESET            = 0x80000000

    #
    # symbol type enumeration
    #
    SymNone = 0
    SymCoff = 1
    SymCv = 2
    SymPdb = 3
    SymExport = 4
    SymDeferred = 5
    SymSym = 6       # .sym file
    SymDia = 7
    SymVirtual = 8
    NumSymTypes = 9
    SYM_TYPE = INT

    #
    # symbol data structure
    #

    @CStructure.make
    class IMAGEHLP_SYMBOL64(CStructure):
        Name: ICharArray               # symbol name (null terminated string)
        reset_annotations()
        SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_SYMBOL64)
        Address: IInt64                # virtual address including dll base address
        Size: IDword                   # estimated size of symbol, can be zero
        Flags: IDword                  # info about the symbols, see the SYMF defines
        MaxNameLength: IDword          # maximum size of symbol name in 'Name'
    
    PIMAGEHLP_SYMBOL64 = IMAGEHLP_SYMBOL64.PTR()
    """

    typedef struct _IMAGEHLP_SYMBOL64_PACKAGE {
        IMAGEHLP_SYMBOL64 sym;
        CHAR              name[MAX_SYM_NAME + 1];
    } IMAGEHLP_SYMBOL64_PACKAGE, *PIMAGEHLP_SYMBOL64_PACKAGE;

    typedef struct _IMAGEHLP_SYMBOLW64 {
        SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_SYMBOLW64)
        Address: IInt64                # virtual address including dll base address
        Size: IDword                   # estimated size of symbol, can be zero
        Flags: IDword                  # info about the symbols, see the SYMF defines
        MaxNameLength: IDword          # maximum size of symbol name in 'Name'
        WCHAR   Name[1];                # symbol name (null terminated string)
    } IMAGEHLP_SYMBOLW64, *PIMAGEHLP_SYMBOLW64;

    typedef struct _IMAGEHLP_SYMBOLW64_PACKAGE {
        IMAGEHLP_SYMBOLW64 sym;
        WCHAR              name[MAX_SYM_NAME + 1];
    } IMAGEHLP_SYMBOLW64_PACKAGE, *PIMAGEHLP_SYMBOLW64_PACKAGE;

    #if !defined(_IMAGEHLP_SOURCE_) && defined(_IMAGEHLP64)

     IMAGEHLP_SYMBOL IMAGEHLP_SYMBOL64
     PIMAGEHLP_SYMBOL PIMAGEHLP_SYMBOL64
     IMAGEHLP_SYMBOL_PACKAGE IMAGEHLP_SYMBOL64_PACKAGE
     PIMAGEHLP_SYMBOL_PACKAGE PIMAGEHLP_SYMBOL64_PACKAGE
     IMAGEHLP_SYMBOLW IMAGEHLP_SYMBOLW64
     PIMAGEHLP_SYMBOLW PIMAGEHLP_SYMBOLW64
     IMAGEHLP_SYMBOLW_PACKAGE IMAGEHLP_SYMBOLW64_PACKAGE
     PIMAGEHLP_SYMBOLW_PACKAGE PIMAGEHLP_SYMBOLW64_PACKAGE

    #else

    typedef struct _IMAGEHLP_SYMBOL {
        DWORD SizeOfStruct;           # set to sizeof(IMAGEHLP_SYMBOL)
        DWORD Address;                # virtual address including dll base address
        DWORD Size;                   # estimated size of symbol, can be zero
        DWORD Flags;                  # info about the symbols, see the SYMF defines
                            MaxNameLength: IDword          # maximum size of symbol name in 'Name'
        CHAR                        Name[1];                # symbol name (null terminated string)
    } IMAGEHLP_SYMBOL, *PIMAGEHLP_SYMBOL;

    typedef struct _IMAGEHLP_SYMBOL_PACKAGE {
        IMAGEHLP_SYMBOL sym;
        CHAR            name[MAX_SYM_NAME + 1];
    } IMAGEHLP_SYMBOL_PACKAGE, *PIMAGEHLP_SYMBOL_PACKAGE;

    typedef struct _IMAGEHLP_SYMBOLW {
        DWORD SizeOfStruct;           # set to sizeof(IMAGEHLP_SYMBOLW)
        DWORD Address;                # virtual address including dll base address
        DWORD Size;                   # estimated size of symbol, can be zero
        DWORD Flags;                  # info about the symbols, see the SYMF defines
                            MaxNameLength: IDword          # maximum size of symbol name in 'Name'
        WCHAR                       Name[1];                # symbol name (null terminated string)
    } IMAGEHLP_SYMBOLW, *PIMAGEHLP_SYMBOLW;

    typedef struct _IMAGEHLP_SYMBOLW_PACKAGE {
        IMAGEHLP_SYMBOLW sym;
        WCHAR            name[MAX_SYM_NAME + 1];
    } IMAGEHLP_SYMBOLW_PACKAGE, *PIMAGEHLP_SYMBOLW_PACKAGE;

    #endif

    #
    # module data structure
    #

    #
    # ANSI Module Information
    #

    typedef struct _IMAGEHLP_MODULE64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_MODULE64)
         BaseOfImage: IInt64            # base load address of module
         ImageSize: IDword              # virtual size of the loaded module
         TimeDateStamp: IDword          # date/time stamp from pe header
         CheckSum: IDword               # checksum from the pe header
         NumSyms: IDword                # number of symbols in the symbol table
        SYM_TYPE SymType;                # type of symbols loaded
        CHAR     ModuleName[32];         # module name
        CHAR     ImageName[256];         # image name
        CHAR     LoadedImageName[256];   # symbol file name
        # new elements: 07-Jun-2002
        CHAR     LoadedPdbName[256];     # pdb file name
         CVSig: IDword                  # Signature of the CV record in the debug directories
        CHAR     CVData[MAX_PATH * 3];   # Contents of the CV record
         PdbSig: IDword                 # Signature of PDB
        GUID     PdbSig70;               # Signature of PDB (VC 7 and up)
         PdbAge: IDword                 # DBI age of pdb
        BOOL     PdbUnmatched;           # loaded an unmatched pdb
        BOOL     DbgUnmatched;           # loaded an unmatched dbg
        BOOL     LineNumbers;            # we have line number information
        BOOL     GlobalSymbols;          # we have internal symbol information
        BOOL     TypeInfo;               # we have type information
        # new elements: 17-Dec-2003
        BOOL     SourceIndexed;          # pdb supports source server
        BOOL     Publics;                # contains public symbols
        # new element: 15-Jul-2009
         MachineType: IDword            # IMAGE_FILE_MACHINE_XXX from ntimage.h and winnt.h
         Reserved: IDword               # Padding - don't remove.
    } IMAGEHLP_MODULE64, *PIMAGEHLP_MODULE64;

    # (Extended) ANSI version of IMAGEHLP_MODULE64 that supports Search Hints
    typedef struct _IMAGEHLP_MODULE64_EX {
        IMAGEHLP_MODULE64 Module;
         RegionFlags: IDword            # Region Search Flags - IMAGEHLP_MODULE_REGION_XXX
    } IMAGEHLP_MODULE64_EX, *PIMAGEHLP_MODULE64_EX;

    #
    # WIDE Module Information
    #

    typedef struct _IMAGEHLP_MODULEW64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_MODULE64)
         BaseOfImage: IInt64            # base load address of module
         ImageSize: IDword              # virtual size of the loaded module
         TimeDateStamp: IDword          # date/time stamp from pe header
         CheckSum: IDword               # checksum from the pe header
         NumSyms: IDword                # number of symbols in the symbol table
        SYM_TYPE SymType;                # type of symbols loaded
        WCHAR    ModuleName[32];         # module name
        WCHAR    ImageName[256];         # image name
        # new elements: 07-Jun-2002
        WCHAR    LoadedImageName[256];   # symbol file name
        WCHAR    LoadedPdbName[256];     # pdb file name
         CVSig: IDword                  # Signature of the CV record in the debug directories
        WCHAR        CVData[MAX_PATH * 3];   # Contents of the CV record
         PdbSig: IDword                 # Signature of PDB
        GUID     PdbSig70;               # Signature of PDB (VC 7 and up)
         PdbAge: IDword                 # DBI age of pdb
        BOOL     PdbUnmatched;           # loaded an unmatched pdb
        BOOL     DbgUnmatched;           # loaded an unmatched dbg
        BOOL     LineNumbers;            # we have line number information
        BOOL     GlobalSymbols;          # we have internal symbol information
        BOOL     TypeInfo;               # we have type information
        # new elements: 17-Dec-2003
        BOOL     SourceIndexed;          # pdb supports source server
        BOOL     Publics;                # contains public symbols
        # new element: 15-Jul-2009
         MachineType: IDword            # IMAGE_FILE_MACHINE_XXX from ntimage.h and winnt.h
         Reserved: IDword               # Padding - don't remove.
    } IMAGEHLP_MODULEW64, *PIMAGEHLP_MODULEW64;

    # (Extended) WIDE version of IMAGEHLP_MODULEW64 that supports Search Hints
    typedef struct _IMAGEHLP_MODULEW64_EX {
        IMAGEHLP_MODULEW64 Module;
         RegionFlags: IDword            # Region Search Flags - IMAGEHLP_MODULE_REGION_XXX
    } IMAGEHLP_MODULEW64_EX, *PIMAGEHLP_MODULEW64_EX;


     IMAGEHLP_MODULE_REGION_DLLBASE       0x01
     IMAGEHLP_MODULE_REGION_DLLRANGE      0x02
     IMAGEHLP_MODULE_REGION_ADDITIONAL    0x04
     IMAGEHLP_MODULE_REGION_JIT           0x08
     IMAGEHLP_MODULE_REGION_ALL           0xFF


    #if !defined(_IMAGEHLP_SOURCE_) && defined(_IMAGEHLP64)
     IMAGEHLP_MODULE IMAGEHLP_MODULE64
     PIMAGEHLP_MODULE PIMAGEHLP_MODULE64
     IMAGEHLP_MODULEW IMAGEHLP_MODULEW64
     PIMAGEHLP_MODULEW PIMAGEHLP_MODULEW64
    #else
    typedef struct _IMAGEHLP_MODULE {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_MODULE)
         BaseOfImage: IDword            # base load address of module
         ImageSize: IDword              # virtual size of the loaded module
         TimeDateStamp: IDword          # date/time stamp from pe header
         CheckSum: IDword               # checksum from the pe header
         NumSyms: IDword                # number of symbols in the symbol table
        SYM_TYPE SymType;                # type of symbols loaded
        CHAR     ModuleName[32];         # module name
        CHAR     ImageName[256];         # image name
        CHAR     LoadedImageName[256];   # symbol file name
    } IMAGEHLP_MODULE, *PIMAGEHLP_MODULE;

    typedef struct _IMAGEHLP_MODULEW {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_MODULE)
         BaseOfImage: IDword            # base load address of module
         ImageSize: IDword              # virtual size of the loaded module
         TimeDateStamp: IDword          # date/time stamp from pe header
         CheckSum: IDword               # checksum from the pe header
         NumSyms: IDword                # number of symbols in the symbol table
        SYM_TYPE SymType;                # type of symbols loaded
        WCHAR    ModuleName[32];         # module name
        WCHAR    ImageName[256];         # image name
        WCHAR    LoadedImageName[256];   # symbol file name
    } IMAGEHLP_MODULEW, *PIMAGEHLP_MODULEW;
    #endif

    #
    # source file line data structure
    #

    typedef struct _IMAGEHLP_LINE64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_LINE64)
        PVOID    Key;                    # internal
         LineNumber: IDword             # line number in file
        PCHAR    FileName;               # full filename
         Address: IInt64                # first instruction of line
    } IMAGEHLP_LINE64, *PIMAGEHLP_LINE64;

    typedef struct _IMAGEHLP_LINEW64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_LINE64)
        PVOID    Key;                    # internal
         LineNumber: IDword             # line number in file
        PWSTR    FileName;               # full filename
         Address: IInt64                # first instruction of line
    } IMAGEHLP_LINEW64, *PIMAGEHLP_LINEW64;

    #if !defined(_IMAGEHLP_SOURCE_) && defined(_IMAGEHLP64)
     IMAGEHLP_LINE IMAGEHLP_LINE64
     PIMAGEHLP_LINE PIMAGEHLP_LINE64
    #else
    typedef struct _IMAGEHLP_LINE {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_LINE)
        PVOID    Key;                    # internal
         LineNumber: IDword             # line number in file
        PCHAR    FileName;               # full filename
         Address: IDword                # first instruction of line
    } IMAGEHLP_LINE, *PIMAGEHLP_LINE;

    typedef struct _IMAGEHLP_LINEW {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_LINE64)
        PVOID    Key;                    # internal
         LineNumber: IDword             # line number in file
        PCHAR    FileName;               # full filename
         Address: IInt64                # first instruction of line
    } IMAGEHLP_LINEW, *PIMAGEHLP_LINEW;
    #endif

    #
    # source file structure
    #

    typedef struct _SOURCEFILE {
         ModBase: IInt64                # base address of loaded module
        PCHAR    FileName;               # full filename of source
    } SOURCEFILE, *PSOURCEFILE;

    typedef struct _SOURCEFILEW {
         ModBase: IInt64                # base address of loaded module
        PWSTR    FileName;               # full filename of source
    } SOURCEFILEW, *PSOURCEFILEW;

    #endif /* WINAPI_FAMILY_PARTITION(NONGAMESPARTITIONS | WINAPI_PARTITION_GAMES) */
    #pragma endregion

    #pragma region Desktop Family
    #if WINAPI_FAMILY_PARTITION(NONGAMESPARTITIONS)

    #
    # data structures used for registered symbol callbacks
    #

     CBA_DEFERRED_SYMBOL_LOAD_START          0x00000001
     CBA_DEFERRED_SYMBOL_LOAD_COMPLETE       0x00000002
     CBA_DEFERRED_SYMBOL_LOAD_FAILURE        0x00000003
     CBA_SYMBOLS_UNLOADED                    0x00000004
     CBA_DUPLICATE_SYMBOL                    0x00000005
     CBA_READ_MEMORY                         0x00000006
     CBA_DEFERRED_SYMBOL_LOAD_CANCEL         0x00000007
     CBA_SET_OPTIONS                         0x00000008
     CBA_EVENT                               0x00000010
     CBA_DEFERRED_SYMBOL_LOAD_PARTIAL        0x00000020
     CBA_DEBUG_INFO                          0x10000000
     CBA_SRCSRV_INFO                         0x20000000
     CBA_SRCSRV_EVENT                        0x40000000
     CBA_UPDATE_STATUS_BAR                   0x50000000
     CBA_ENGINE_PRESENT                      0x60000000
     CBA_CHECK_ENGOPT_DISALLOW_NETWORK_PATHS 0x70000000
     CBA_CHECK_ARM_MACHINE_THUMB_TYPE_OVERRIDE 0x80000000
     CBA_XML_LOG                             0x90000000
     CBA_MAP_JIT_SYMBOL                      0xA0000000


    typedef struct _IMAGEHLP_CBA_READ_MEMORY {
          addr: IInt64                                     # address to read from
        PVOID     buf;                                      # buffer to read to
          bytes: IDword                                    # amount of bytes to read
         *bytesread: IDword                                # pointer to store amount of bytes read
    } IMAGEHLP_CBA_READ_MEMORY, *PIMAGEHLP_CBA_READ_MEMORY;

    enum {
        sevInfo = 0,
        sevProblem,
        sevAttn,
        sevFatal,
        sevMax  # unused
    };

     EVENT_SRCSPEW_START 100
     EVENT_SRCSPEW       100
     EVENT_SRCSPEW_END   199

    typedef struct _IMAGEHLP_CBA_EVENT {
        DWORD severity;                                     # values from sevInfo to sevFatal
        DWORD code;                                         # numerical code IDs the error
        PCHAR desc;                                         # may contain a text description of the error
        PVOID object;                                       # value dependant upon the error code
    } IMAGEHLP_CBA_EVENT, *PIMAGEHLP_CBA_EVENT;

    typedef struct _IMAGEHLP_CBA_EVENTW {
        DWORD  severity;                                     # values from sevInfo to sevFatal
        DWORD  code;                                         # numerical code IDs the error
        PCWSTR desc;                                         # may contain a text description of the error
        PVOID  object;                                       # value dependant upon the error code
    } IMAGEHLP_CBA_EVENTW, *PIMAGEHLP_CBA_EVENTW;

    typedef struct _IMAGEHLP_DEFERRED_SYMBOL_LOAD64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_DEFERRED_SYMBOL_LOAD64)
         BaseOfImage: IInt64            # base load address of module
         CheckSum: IDword               # checksum from the pe header
         TimeDateStamp: IDword          # date/time stamp from pe header
        CHAR     FileName[MAX_PATH];     # symbols file or image name
        BOOLEAN  Reparse;                # load failure reparse
        HANDLE   hFile;                  # file handle, if passed
         Flags: IDword                     #
    } IMAGEHLP_DEFERRED_SYMBOL_LOAD64, *PIMAGEHLP_DEFERRED_SYMBOL_LOAD64;

    typedef struct _IMAGEHLP_DEFERRED_SYMBOL_LOADW64 {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_DEFERRED_SYMBOL_LOADW64)
         BaseOfImage: IInt64            # base load address of module
         CheckSum: IDword               # checksum from the pe header
         TimeDateStamp: IDword          # date/time stamp from pe header
        WCHAR    FileName[MAX_PATH + 1]; # symbols file or image name
        BOOLEAN  Reparse;                # load failure reparse
        HANDLE   hFile;                  # file handle, if passed
         Flags: IDword         #
    } IMAGEHLP_DEFERRED_SYMBOL_LOADW64, *PIMAGEHLP_DEFERRED_SYMBOL_LOADW64;

     DSLFLAG_MISMATCHED_PDB              0x1
     DSLFLAG_MISMATCHED_DBG              0x2
     FLAG_ENGINE_PRESENT                 0x4
     FLAG_ENGOPT_DISALLOW_NETWORK_PATHS  0x8
     FLAG_OVERRIDE_ARM_MACHINE_TYPE      0x10


    #if !defined(_IMAGEHLP_SOURCE_) && defined(_IMAGEHLP64)
     IMAGEHLP_DEFERRED_SYMBOL_LOAD IMAGEHLP_DEFERRED_SYMBOL_LOAD64
     PIMAGEHLP_DEFERRED_SYMBOL_LOAD PIMAGEHLP_DEFERRED_SYMBOL_LOAD64
    #else
    typedef struct _IMAGEHLP_DEFERRED_SYMBOL_LOAD {
         SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_DEFERRED_SYMBOL_LOAD)
         BaseOfImage: IDword            # base load address of module
         CheckSum: IDword               # checksum from the pe header
         TimeDateStamp: IDword          # date/time stamp from pe header
        CHAR     FileName[MAX_PATH];     # symbols file or image name
        BOOLEAN  Reparse;                # load failure reparse
        HANDLE   hFile;                  # file handle, if passed
    } IMAGEHLP_DEFERRED_SYMBOL_LOAD, *PIMAGEHLP_DEFERRED_SYMBOL_LOAD;
    #endif

    typedef struct _IMAGEHLP_DUPLICATE_SYMBOL64 {
                   SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_DUPLICATE_SYMBOL64)
                   NumberOfDups: IDword           # number of duplicates in the Symbol array
        PIMAGEHLP_SYMBOL64 Symbol;                 # array of duplicate symbols
                   SelectedSymbol: IDword         # symbol selected (-1 to start)
    } IMAGEHLP_DUPLICATE_SYMBOL64, *PIMAGEHLP_DUPLICATE_SYMBOL64;

    #if !defined(_IMAGEHLP_SOURCE_) && defined(_IMAGEHLP64)
     IMAGEHLP_DUPLICATE_SYMBOL IMAGEHLP_DUPLICATE_SYMBOL64
     PIMAGEHLP_DUPLICATE_SYMBOL PIMAGEHLP_DUPLICATE_SYMBOL64
    #else
    typedef struct _IMAGEHLP_DUPLICATE_SYMBOL {
                 SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_DUPLICATE_SYMBOL)
                 NumberOfDups: IDword           # number of duplicates in the Symbol array
        PIMAGEHLP_SYMBOL Symbol;                 # array of duplicate symbols
                 SelectedSymbol: IDword         # symbol selected (-1 to start)
    } IMAGEHLP_DUPLICATE_SYMBOL, *PIMAGEHLP_DUPLICATE_SYMBOL;
    #endif

    typedef struct _IMAGEHLP_JIT_SYMBOL_MAP {
                 SizeOfStruct: IDword           # set to sizeof(IMAGEHLP_JIT_SYMBOL_MAP)
                 Address: IInt64                # address to map to JIT association with an image
                 BaseOfImage: IInt64            # base load address (0 == unmapped)
    } IMAGEHLP_JIT_SYMBOLMAP, *PIMAGEHLP_JIT_SYMBOLMAP;

    # If dbghelp ever needs to display graphical UI, it will use this as the parent window.
    """