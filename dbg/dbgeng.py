"""
Debugger engine interfaces.
"""

from ..com.objbase import *

DbgEng = get_win_library('DbgEng.dll')

#----------------------------------------------------------------------------
#
# Special exception code extensions could throw
#
#----------------------------------------------------------------------------
ERROR_DBG_CANCELLED = 0xC00004C7 # 0xC0000000 + ERROR_CANCELLED
ERROR_DBG_TIMEOUT   = 0xC00005B4 # 0xC0000000 + ERROR_TIMEOUT

#----------------------------------------------------------------------------
#
# GUIDs and interface forward declarations.
#
#----------------------------------------------------------------------------

IID_IDebugAdvanced = IID('{f2df5f53-071f-47bd-9de6-5734c3fed689}')
IID_IDebugAdvanced2 = IID('{716d14c9-119b-4ba5-af1f-0890e672416a}')
IID_IDebugAdvanced3 = IID('{cba4abb4-84c4-444d-87ca-a04e13286739}')
IID_IDebugAdvanced4 = IID('{d1069067-2a65-4bf0-ae97-76184b67856b}')
IID_IDebugBreakpoint = IID('{5bd9d474-5975-423a-b88b-65a8e7110e65}')
IID_IDebugBreakpoint2 = IID('{1b278d20-79f2-426e-a3f9-c1ddf375d48e}')
IID_IDebugBreakpoint3 = IID('{38f5c249-b448-43bb-9835-579d4ec02249}')
IID_IDebugClient = IID('{27fe5639-8407-4f47-8364-ee118fb08ac8}')
IID_IDebugClient2 = IID('{edbed635-372e-4dab-bbfe-ed0d2f63be81}')
IID_IDebugClient3 = IID('{dd492d7f-71b8-4ad6-a8dc-1c887479ff91}')
IID_IDebugClient4 = IID('{ca83c3de-5089-4cf8-93c8-d892387f2a5e}')
IID_IDebugClient5 = IID('{e3acb9d7-7ec2-4f0c-a0da-e81e0cbbe628}')
IID_IDebugClient6 = IID('{fd28b4c5-c498-4686-a28e-62cad2154eb3}')
IID_IDebugClient7 = IID('{13586be3-542e-481e-b1f2-8497ba74f9a9}')
IID_IDebugPlmClient = IID('{a02b66c4-aea3-4234-a9f7-fe4c383d4e29}')
IID_IDebugPlmClient2 = IID('{597c980d-e7bd-4309-962c-9d9b69a7372c}')
IID_IDebugPlmClient3 = IID('{cdf48669-901f-4791-b868-7d2cb3a2d7fc}')
IID_IDebugOutputStream = IID('{7782d8f2-2b85-4059-ab88-28ceddca1c80}')
IID_IDebugControl = IID('{5182e668-105e-416e-ad92-24ef800424ba}')
IID_IDebugControl2 = IID('{d4366723-44df-4bed-8c7e-4c05424f4588}')
IID_IDebugControl3 = IID('{7df74a86-b03f-407f-90ab-a20dadcead08}')
IID_IDebugControl4 = IID('{94e60ce9-9b41-4b19-9fc0-6d9eb35272b3}')
IID_IDebugControl5 = IID('{b2ffe162-2412-429f-8d1d-5bf6dd824696}')
IID_IDebugControl6 = IID('{bc0d583f-126d-43a1-9cc4-a860ab1d537b}')
IID_IDebugControl7 = IID('{b86fb3b1-80d4-475b-aea3-cf06539cf63a}')
IID_IDebugDataSpaces = IID('{88f7dfab-3ea7-4c3a-aefb-c4e8106173aa}')
IID_IDebugDataSpaces2 = IID('{7a5e852f-96e9-468f-ac1b-0b3addc4a049}')
IID_IDebugDataSpaces3 = IID('{23f79d6c-8aaf-4f7c-a607-9995f5407e63}')
IID_IDebugDataSpaces4 = IID('{d98ada1f-29e9-4ef5-a6c0-e53349883212}')
IID_IDebugEventCallbacks = IID('{337be28b-5036-4d72-b6bf-c45fbb9f2eaa}')
IID_IDebugEventCallbacksWide = IID('{0690e046-9c23-45ac-a04f-987ac29ad0d3}')
IID_IDebugEventContextCallbacks = IID('{61a4905b-23f9-4247-b3c5-53d087529ab7}')
IID_IDebugInputCallbacks = IID('{9f50e42c-f136-499e-9a97-73036c94ed2d}')
IID_IDebugOutputCallbacks = IID('{4bf58045-d654-4c40-b0af-683090f356dc}')
IID_IDebugOutputCallbacksWide = IID('{4c7fd663-c394-4e26-8ef1-34ad5ed3764c}')
IID_IDebugOutputCallbacks2 = IID('{67721fe9-56d2-4a44-a325-2b65513ce6eb}')
IID_IDebugRegisters = IID('{ce289126-9e84-45a7-937e-67bb18691493}')
IID_IDebugRegisters2 = IID('{1656afa9-19c6-4e3a-97e7-5dc9160cf9c4}')
IID_IDebugSymbolGroup = IID('{f2528316-0f1a-4431-aeed-11d096e1e2ab}')
IID_IDebugSymbolGroup2 = IID('{6a7ccc5f-fb5e-4dcc-b41c-6c20307bccc7}')
IID_IDebugSymbols = IID('{8c31e98c-983a-48a5-9016-6fe5d667a950}')
IID_IDebugSymbols2 = IID('{3a707211-afdd-4495-ad4f-56fecdf8163f}')
IID_IDebugSymbols3 = IID('{f02fbecc-50ac-4f36-9ad9-c975e8f32ff8}')
IID_IDebugSymbols4 = IID('{e391bbd8-9d8c-4418-840b-c006592a1752}')
IID_IDebugSymbols5 = IID('{c65fa83e-1e69-475e-8e0e-b5d79e9cc17e}')
IID_IDebugSystemObjects = IID('{6b86fe2c-2c4f-4f0c-9da2-174311acc327}')
IID_IDebugSystemObjects2 = IID('{0ae9f5ff-1852-4679-b055-494bee6407ee}')
IID_IDebugSystemObjects3 = IID('{e9676e2f-e286-4ea3-b0f9-dfe5d9fc330e}')
IID_IDebugSystemObjects4 = IID('{489468e6-7d0f-4af5-87ab-25207454d553}')

#----------------------------------------------------------------------------
#
# Macros.
#
#----------------------------------------------------------------------------

# Extends a 32-bit address into a 64-bit address.
def DEBUG_EXTEND64(Addr: int) -> int:
    return ULONG64(LONG64(LONG(Addr).value).value).value

#----------------------------------------------------------------------------
#
# Client creation functions.
#
#----------------------------------------------------------------------------

# RemoteOptions specifies connection types and
# their parameters.  Supported strings are:
#    npipe:Server=<Machine>,Pipe=<Pipe name>
#    tcp:Server=<Machine>,Port=<IP port>

@DbgEng.foreign(HRESULT, PCSTR, REFIID, PVOID, intermediate_method=True)
def DebugConnect(RemoteOptions: PCSTR, InterfaceId: IID,
                 Interface: PVOID, **kwargs) -> int:
    return delegate(RemoteOptions, InterfaceId.ref() or NULL, Interface)

@DbgEng.foreign(HRESULT, PCWSTR, REFIID, PVOID, intermediate_method=True)
def DebugConnectWide(RemoteOptions: PCWSTR, InterfaceId: IID,
                     Interface: IPointer[PVOID], **kwargs) -> int:
    return delegate(RemoteOptions, InterfaceId.ref() if InterfaceId else NULL, Interface)

@DbgEng.foreign(HRESULT, REFIID, PVOID, intermediate_method=True)
def DebugCreate(InterfaceId: IID, Interface: IPointer[PVOID]) -> int:
    return delegate(InterfaceId.ref() if InterfaceId else NULL, Interface)

@DbgEng.foreign(HRESULT, REFIID, DWORD, PVOID, intermediate_method=True)
def DebugCreateEx(InterfaceId: IID, DbgEngOptions: int,
                  Interface: IPointer[PVOID]) -> int:
    return delegate(InterfaceId.ref() if InterfaceId else NULL, 
                    DbgEngOptions, Interface)

#----------------------------------------------------------------------------
#
# IDebugAdvanced.
#
#----------------------------------------------------------------------------

class DEBUG_OFFSET_REGION(CStructure):
    _fields_ = [
        ('Base', ULONG64),
        ('Size', ULONG64)
    ]
    
    Base: int; Size: int
    
PDEBUG_OFFSET_REGION = DEBUG_OFFSET_REGION.PTR()

class IDebugAdvanced(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IDebugAdvanced
    
    @virtual_table.com_function(PVOID, ULONG)
    def GetThreadContext(self, Context: PVOID, ContextSize: int) -> int:
        """
        Get/SetThreadContext offer control over
        the full processor context for a thread.
        Higher-level functions, such as the
        IDebugRegisters interface, allow similar
        access in simpler and more generic ways.
        Get/SetThreadContext are useful when
        large amounts of thread context must
        be changed and processor-specific code
        is not a problem.
        """
    
    @virtual_table.com_function(PVOID, ULONG)
    def SetThreadContext(self, Context: PVOID, ContextSize: int) -> int:
        """
        Get/SetThreadContext offer control over
        the full processor context for a thread.
        Higher-level functions, such as the
        IDebugRegisters interface, allow similar
        access in simpler and more generic ways.
        Get/SetThreadContext are useful when
        large amounts of thread context must
        be changed and processor-specific code
        is not a problem.
        """
    
    virtual_table.build()
    
PDEBUG_ADVANCED = IDebugAdvanced.PTR()

class DEBUG_READ_USER_MINIDUMP_STREAM(CStructure):
    _fields_ = [
        ('StreamType', ULONG),
        ('Flags', ULONG),
        ('Offset', ULONG64),
        ('Buffer', PVOID),
        ('BufferSize', ULONG),
        ('BufferUsed', ULONG)
    ]
    
    StreamType: int # IN
    BufferSize: int # IN
    Offset: int # IN
    Flags: int # IN
    
    BufferUsed: int # OUT
    Buffer: int # OUT
    
PDEBUG_READ_USER_MINIDUMP_STREAM = DEBUG_READ_USER_MINIDUMP_STREAM.PTR()

DEBUG_GET_TEXT_COMPLETIONS_NO_DOT_COMMANDS       = 0x00000001
DEBUG_GET_TEXT_COMPLETIONS_NO_EXTENSION_COMMANDS = 0x00000002
DEBUG_GET_TEXT_COMPLETIONS_NO_SYMBOLS            = 0x00000004

class DEBUG_GET_TEXT_COMPLETIONS_IN(CStructure):
    _fields_ = [
        ('Flags', ULONG),
        ('MatchCountLimit', ULONG),
        ('Reserved', ULONG64 * 3)
    ]
    
    Reserved: IArray[ULONG64]
    MatchCountLimit: int
    Flags: int
    
PDEBUG_GET_TEXT_COMPLETIONS_IN = DEBUG_GET_TEXT_COMPLETIONS_IN.PTR()

class DEBUG_CACHED_SYMBOL_INFO(CStructure):
    _fields_ = [
        ('ModBase', ULONG64),
        ('Arg1', ULONG64),
        ('Arg2', ULONG64),
        ('Id', ULONG),
        ('Arg3', ULONG)
    ]
    
    Arg1: int; Arg2: int; Arg3: int
    ModBase: int
    Id: int
    
PDEBUG_CACHED_SYMBOL_INFO = DEBUG_CACHED_SYMBOL_INFO.PTR()

class PROCESS_NAME_ENTRY(CStructure):
    _fields_ = [
        ('ProcessId', ULONG),
        ('NameOffset', ULONG),
        ('NameSize', ULONG),
        ('NextEntry', ULONG)
    ]
    
    NameOffset: int # offset for the process name string.
    ProcessId: int
    NextEntry: int # offset for next entry, 0 if the last.
    NameSize: int # ProcessName will always be NULL terminated, NameSize is for struct align and safeguard.
    
PPROCESS_NAME_ENTRY = PROCESS_NAME_ENTRY.PTR()

#
# Request requests.
#

# InBuffer - Unused.
# OutBuffer - Unused.
DEBUG_REQUEST_SOURCE_PATH_HAS_SOURCE_SERVER = 0

# InBuffer - Unused.
# OutBuffer - Machine-specific CONTEXT.
DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT = 1

# InBuffer - Unused.
# OutBuffer - ULONG system ID of thread.
DEBUG_REQUEST_TARGET_EXCEPTION_THREAD = 2

# InBuffer - Unused.
# OutBuffer - EXCEPTION_RECORD64.
DEBUG_REQUEST_TARGET_EXCEPTION_RECORD = 3

# InBuffer - Unused.
# OutBuffer - DEBUG_CREATE_PROCESS_OPTIONS.
DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS = 4

# InBuffer - DEBUG_CREATE_PROCESS_OPTIONS.
# OutBuffer - Unused.
DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS = 5

# InBuffer - Unused.
# OutBuffer - ULONG[2] major/minor.
DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS = 6

# InBuffer - DEBUG_READ_USER_MINIDUMP_STREAM.
# OutBuffer - Unused.
DEBUG_REQUEST_READ_USER_MINIDUMP_STREAM = 7

# InBuffer - Unused.
# OutBuffer - Unused.
DEBUG_REQUEST_TARGET_CAN_DETACH = 8

# InBuffer - PTSTR.
# OutBuffer - Unused.
DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE = 9

# InBuffer - Unused.
# OutBuffer - Event code stream offset.
DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET = 10

# InBuffer - Unused.
# OutBuffer - Event code stream information.
DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM = 11

# InBuffer - Input data block.
# OutBuffer - Processed data block.
DEBUG_REQUEST_EXT_TYPED_DATA_ANSI = 12

# InBuffer - Unused.
# OutBuffer - Returned path.
DEBUG_REQUEST_GET_EXTENSION_SEARCH_PATH_WIDE = 13

# InBuffer - DEBUG_GET_TEXT_COMPLETIONS_IN.
# OutBuffer - DEBUG_GET_TEXT_COMPLETIONS_OUT.
DEBUG_REQUEST_GET_TEXT_COMPLETIONS_WIDE = 14

# InBuffer - ULONG64 cookie.
# OutBuffer - DEBUG_CACHED_SYMBOL_INFO.
DEBUG_REQUEST_GET_CACHED_SYMBOL_INFO = 15

# InBuffer - DEBUG_CACHED_SYMBOL_INFO.
# OutBuffer - ULONG64 cookie.
DEBUG_REQUEST_ADD_CACHED_SYMBOL_INFO = 16

# InBuffer - ULONG64 cookie.
# OutBuffer - Unused.
DEBUG_REQUEST_REMOVE_CACHED_SYMBOL_INFO = 17

# InBuffer - DEBUG_GET_TEXT_COMPLETIONS_IN.
# OutBuffer - DEBUG_GET_TEXT_COMPLETIONS_OUT.
DEBUG_REQUEST_GET_TEXT_COMPLETIONS_ANSI = 18

# InBuffer - Unused.
# OutBuffer - Unused.
DEBUG_REQUEST_CURRENT_OUTPUT_CALLBACKS_ARE_DML_AWARE = 19

# InBuffer - ULONG64 offset.
# OutBuffer - Unwind information.
DEBUG_REQUEST_GET_OFFSET_UNWIND_INFORMATION = 20

# InBuffer - Unused
# OutBuffer - returned DUMP_HEADER32/DUMP_HEADER64 structure.
DEBUG_REQUEST_GET_DUMP_HEADER = 21

# InBuffer - DUMP_HEADER32/DUMP_HEADER64 structure.
# OutBuffer - Unused
DEBUG_REQUEST_SET_DUMP_HEADER = 22

# InBuffer - Midori specific
# OutBuffer - Midori specific
DEBUG_REQUEST_MIDORI = 23

# InBuffer - Unused
# OutBuffer - PROCESS_NAME_ENTRY blocks
DEBUG_REQUEST_PROCESS_DESCRIPTORS = 24

# InBuffer - Unused
# OutBuffer - MINIDUMP_MISC_INFO_N blocks
DEBUG_REQUEST_MISC_INFORMATION = 25

# InBuffer - Unused
# OutBuffer - ULONG64 as TokenHandle value
DEBUG_REQUEST_OPEN_PROCESS_TOKEN = 26

# InBuffer - Unused
# OutBuffer - ULONG64 as TokenHandle value
DEBUG_REQUEST_OPEN_THREAD_TOKEN = 27

# InBuffer -  ULONG64 as TokenHandle being duplicated
# OutBuffer - ULONG64 as new duplicated TokenHandle
DEBUG_REQUEST_DUPLICATE_TOKEN = 28

# InBuffer - a ULONG64 as TokenHandle and a ULONG as NtQueryInformationToken() request code
# OutBuffer - NtQueryInformationToken() return
DEBUG_REQUEST_QUERY_INFO_TOKEN = 29

# InBuffer - ULONG64 as TokenHandle
# OutBuffer - Unused
DEBUG_REQUEST_CLOSE_TOKEN = 30

# InBuffer - ULONG64 for process server identification and ULONG as PID
# OutBuffer - Unused
DEBUG_REQUEST_WOW_PROCESS = 31

# InBuffer - ULONG64 for process server identification and PWSTR as module path
# OutBuffer - Unused
DEBUG_REQUEST_WOW_MODULE = 32

# InBuffer - Unused
# OutBuffer - Unused
# return - S_OK if non-invasive user-mode attach, S_FALSE if not (but still live user-mode), E_FAIL otherwise.
DEBUG_LIVE_USER_NON_INVASIVE = 33

# InBuffer - TID
# OutBuffer - Unused
# return - ResumeThreads() return.
DEBUG_REQUEST_RESUME_THREAD = 34

# InBuffer - LONG32 - 0:query current state; >0:enable inline queries; <0: disable inline queries
# OutBuffer - Unused
# return - S_OK: inline queries are enabled; S_FALSE: inline queries are disabled; others: errors.
DEBUG_REQUEST_INLINE_QUERY = 35

# InBuffer - Unused
# OutBuffer - Unused
# return - S_OK.
DEBUG_REQUEST_TL_INSTRUMENTATION_AWARE = 36

# InBuffer - Unused
# OutBuffer - ULONG for version number supported
# return - S_OK.
DEBUG_REQUEST_GET_INSTRUMENTATION_VERSION = 37

# InBuffer - ULONG for module index
# OutBuffer - ULONG for architecture
# return - S_OK
DEBUG_REQUEST_GET_MODULE_ARCHITECTURE = 38

#
# GetSourceFileInformation requests.
#

# Arg64 - Module base.
# Arg32 - Unused.
DEBUG_SRCFILE_SYMBOL_TOKEN = 0

# Arg64 - Module base.
# Arg32 - Unused.
DEBUG_SRCFILE_SYMBOL_TOKEN_SOURCE_COMMAND_WIDE = 1

# Arg64 - Module base.
# Arg32 - Unused
DEBUG_SRCFILE_SYMBOL_CHECKSUMINFO = 2

#
# GetSymbolInformation requests.
#

# Arg64 - Unused.
# Arg32 - Breakpoint ID.
# Buffer - ULONG line number.
# String - File name.
DEBUG_SYMINFO_BREAKPOINT_SOURCE_LINE = 0

# Arg64 - Module base.
# Arg32 - Unused.
# Buffer - IMAGEHLP_MODULEW64.
# String - Unused.
DEBUG_SYMINFO_IMAGEHLP_MODULEW64 = 1

# Arg64 - Offset.
# Arg32 - Symbol tag.
# Buffer - Unicode symbol name strings.  Could have multiple strings.
# String - Unused, strings are returned in Buffer as there
#          may be more than one.
DEBUG_SYMINFO_GET_SYMBOL_NAME_BY_OFFSET_AND_TAG_WIDE = 2

# Arg64 - Module base.
# Arg32 - Symbol tag.
# Buffer - Array of symbol addresses.
# String - Concatenated symbol strings.  Individual symbol
#          strings are zero-terminated and the final string in
#          a symbol is double-zero-terminated.
DEBUG_SYMINFO_GET_MODULE_SYMBOL_NAMES_AND_OFFSETS = 3

#
# GetSystemObjectInformation requests.
#

# Arg64 - Unused.
# Arg32 - Debugger thread ID.
# Buffer - DEBUG_THREAD_BASIC_INFORMATION.
DEBUG_SYSOBJINFO_THREAD_BASIC_INFORMATION = 0

# Arg64 - Unused.
# Arg32 - Debugger thread ID.
# Buffer - Unicode name string.
DEBUG_SYSOBJINFO_THREAD_NAME_WIDE = 1

# Arg64 - Unused.
# Arg32 - Unused.
# Buffer - ULONG cookie value.
DEBUG_SYSOBJINFO_CURRENT_PROCESS_COOKIE = 2

DEBUG_TBINFO_EXIT_STATUS    = 0x00000001
DEBUG_TBINFO_PRIORITY_CLASS = 0x00000002
DEBUG_TBINFO_PRIORITY       = 0x00000004
DEBUG_TBINFO_TIMES          = 0x00000008
DEBUG_TBINFO_START_OFFSET   = 0x00000010
DEBUG_TBINFO_AFFINITY       = 0x00000020
DEBUG_TBINFO_ALL            = 0x0000003f

class DEBUG_THREAD_BASIC_INFORMATION(CStructure):
    _fields_  = [
        # Valid members have a DEBUG_TBINFO bit set in Valid.
        ('Valid', ULONG),
        ('ExitStatus', ULONG),
        ('PriorityClass', ULONG),
        ('Priority', ULONG),
        ('CreateTime', ULONG64),
        ('ExitTime', ULONG64),
        ('KernelTime', ULONG64),
        ('UserTime', ULONG64),
        ('StartOffset', ULONG64),
        ('Affinity', ULONG64)
    ]
    
    PriorityClass: int
    StartOffset: int
    ExitStatus: int
    KernelTime: int
    CreateTime: int
    ExitTime: int
    UserTime: int
    Priority: int
    Affinity: int
    Valid: int
    
class IDebugAdvanced2(IDebugAdvanced):
    virtual_table = COMVirtualTable.from_ancestor(IDebugAdvanced)
    _iid_ = IID_IDebugAdvanced2
    
    @virtual_table.com_function(ULONG, PVOID, ULONG, PVOID, ULONG, PULONG)
    def Request(self, Request: int, InBuffer: PVOID, InBufferSize: int,
                OutBuffer: PVOID, OutBufferSize: int, OutSize: PULONG) -> int: ...
    
    
    
    virtual_table.build()
    
# To be continued