from typing import (Callable)

from . import cpreproc
from .defbase import *
import os

from .basetsd import *
from .windef  import *

# WinNT.h & WinDef.h
if cpreproc.pragma_once("_WINNT_"):
    NTAPI = WINFUNCTYPE
    
    LPWCH = PWCHAR
    PWCH = PWCHAR
    LPCWCH = PWCHAR
    PCWCH = PWCHAR
    
    NWPSTR = PWCHAR
    PWSTR = PWCHAR
    
    PZPWSTR = PWSTR
    PCZPWSTR = PWSTR
    
    LPUWSTR = PWCHAR
    PUWSTR = PWCHAR
    
    PCWSTR = PWCHAR
    
    PZPCWSTR = PCWSTR
    
    PCZPCWSTR = PCWSTR
    
    LPCUWSTR = PWCHAR
    PCUWSTR = PWCHAR
    
    PZZWSTR = PWCHAR
    
    PCZZWSTR = PZZWSTR
    
    PUZZWSTR = PZZWSTR
    
    PCUZZWSTR = PZZWSTR
    
    PNZWCH = PWCH
    
    PCNZWCH = PWCH
    
    PUNZWCH = PWCH
    
    PCUNZWCH = PWCH
    
    LPCWCHAR = PWCHAR
    PCWCHAR = PWCHAR
    
    LPCUWCHAR = PWCHAR
    PCUWCHAR = PWCHAR
    
    UCSCHAR = c_ulong
    
    UCSCHAR_INVALID_CHARACTER = 0xFFFFFFFF
    MIN_UCSCHAR = 0
    MAX_UCSCHAR = 0x0010FFFF
    
    PUCSCHAR = POINTER(UCSCHAR)
    
    PCUCSCHAR = PUCSCHAR
    
    PUCSSTR = PUCSCHAR
    PUUCSSTR = PUCSSTR
    
    PCUCSSTR = PUCSSTR
    PCUUCSSTR = PUUCSSTR
    
    PUUCSCHAR = PUCSCHAR
    PCUUCSCHAR = PUUCSCHAR
    
    LPCH = PCHAR
    PCH = PCHAR
    
    LPCCH = LPCH
    PCCH = PCH
    
    NPSTR = LPSTR
    PSTR = LPSTR
    
    PZPSTR = LPSTR
    PCZPSTR = PZPSTR
    
    PCSTR = LPCSTR
    
    PZPCSTR = PCSTR
    PCZPCSTR = PZPCSTR
    
    PZZSTR = PCSTR
    PCZZSTR = PZZSTR
    
    PNZCH = PCHAR
    PCNZCH = PNZCH
    
    if cpreproc.ifdef("UNICODE"):
        if cpreproc.ifndef("_TCHAR_DEFINED"):
            TCHAR = WCHAR
            PTCHAR = PWCHAR
            
            TBYTE = WCHAR
            CTBYTE = PWCHAR
            
            cpreproc.define("_TCHAR_DEFINED")
        LPTCH = LPWCH
        PTCH = PWCH
        
        PCTCH = PCWCH
        LPCTCH = LPCWCH
        
        PTSTR = LPWSTR
        LPTSTR = LPWSTR
        
        PCTSTR = LPCWSTR
        LPCTSTR = LPCWSTR
        
        PUTSTR = PUWSTR
        LPUTSTR = LPUWSTR
        
        PCUTSTR = PCUWSTR
        LPCUTSTR = LPCUWSTR
        
        LP = LPWSTR
        
        PZZTSTR = PZZWSTR
        PCZZTSTR = PCZZWSTR
        
        PUZZTSTR = PUZZWSTR
        PCUZZTSTR = PCUZZWSTR
        
        PZPTSTR = PZPWSTR
        PNZTCH = PNZWCH
        
        PCNZTCH = PCNZWCH
        PUNZTCH = PUNZWCH
        
        PCUNZTCH = PCUNZWCH
        __TEXT = lambda quote: quote.decode('utf-8') if isinstance(quote, bytes) else quote
    else:
        if cpreproc.ifndef("_TCHAR_DEFINED"):
            TCHAR = CHAR
            PTCHAR = PCHAR
            
            TBYTE = CHAR
            PTBYTE = PCHAR
            
            cpreproc.define("_TCHAR_DEFINED")
        LPTCH = LPCH
        PTCH = LPCH
        
        PCTCH = LPCCH
        LPCTCH = LPCCH
        
        PTSTR = LPSTR
        LPTSTR = LPSTR
        
        PCTSTR = LPCSTR
        LPCTSTR = LPCSTR
        
        PUTSTR = LPSTR
        LPUTSTR = LPSTR
        
        PCUTSTR = LPCSTR
        LPCUTSTR = LPCSTR
        
        PZZTSTR = PZZSTR
        PCZZTSTR = PCZZSTR
        
        PUZZTSTR = PZZSTR
        PCUZZTSTR = PCZZSTR
        
        PZPTSTR = PZPSTR
        PNZTCH = PCNZCH
        
        PCNZTCH = PCNZWCH
        PUNZTCH = PNZCH
        
        PCUNZTCH = PCNZCH
        __TEXT = lambda quote: quote
    TEXT = lambda quote: __TEXT(quote)

    if cpreproc.ifndef("OLE2ANSI"):
        OLECHAR = WCHAR
        LPOLESTR = POINTER(OLECHAR)
        LPCOLESTR = LPOLESTR
        OLESTR = lambda str: TEXT(str)
    else:
        OLECHAR = CHAR
        LPOLESTR = POINTER(OLECHAR)
        LPCOLESTR = LPOLESTR
        OLESTR = lambda str: str
    
    class _QUAD(CStructure):
        _fields_ = [
            ("u", INT64)
        ]
        
    QUAD = _QUAD
    PQUAD = POINTER(QUAD)
    
    UQUAD = QUAD
    PUQUAD = PQUAD
    
    UCHAR = CHAR
    PUCHAR = PCHAR
    
    PCUCHAR = PUCHAR
    PCUSHORT = PUSHORT
    PCULONG = PULONG
    PCUQUAD = PUQUAD
    
    SCHAR = BYTE
    PSCHAR = PBYTE
    
    PCSCHAR = PBYTE
    
    ALL_PROCESSOR_GROUPS = 0xFFFF
    
    class _PROCESSOR_NUMBER(CStructure):
        _fields_ = [
            ("Group", WORD),
            ("Number", BYTE),
            ("Reserved", BYTE)
        ]
        
    PROCESSOR_NUMBER = _PROCESSOR_NUMBER
    PPROCESSOR_NUMBER = POINTER(PROCESSOR_NUMBER)
    
    class _GROUP_AFFINITY(CStructure):
        _fields_ = [
            ("Mask", KAFFINITY),
            ("Group", WORD),
            ("Reserved", WORD * 3)
        ]
        
    GROUP_AFFINITY = _GROUP_AFFINITY
    PGROUP_AFFINITY = POINTER(GROUP_AFFINITY)
    
    if os.environ['PROCESSOR_ARCHITECTURE'].endswith('64'):
        MAXIMUM_PROC_PER_GROUP = 64
    else:
        MAXIMUM_PROC_PER_GROUP = 32
    MAXIMUM_PROCESSORS = MAXIMUM_PROC_PER_GROUP
    
    FCHAR = BYTE
    FSHORT = WORD
    FLONG = DWORD
    
    HRESULT = LONG
    
    CCHAR = CHAR
    CSHORT = SHORT
    CLONG = ULONG
    PCCHAR = PCHAR
    PCSHORT = PSHORT
    PCLONG = PULONG
    LCID = DWORD
    PLCID = PDWORD
    LANGID = WORD
    
    if cpreproc.pragma_once("__COMPARTMENT_ID_DEFINED__"):
        _COMPARTMENT_ID = INT
        if True:
            UNSPECIFIED_COMPARTMENT_ID = 0
            DEFAULT_COMPARTMENT_ID = 1
        COMPARTMENT_ID = _COMPARTMENT_ID
        PCOMPARTMENT_ID = POINTER(COMPARTMENT_ID)

    ucrtbased = W_WinDLL("ucrtbased.dll")
    _get_wide_winmain_command_line = declare(ucrtbased._get_wide_winmain_command_line, LPWSTR, VOID)
        
    LOGICAL = ULONG
    PLOGICALL = PULONG
    
    NTSTATUS = LONG
    PNTSTATUS = PLONG
    PCNTSTATUS = PCLONG
    
    NT_SUCCESS = lambda Status: (NTSTATUS(Status).value) >= 0
    NT_INFORMATION = lambda Status: (ULONG(Status).value >> 30) == 1
    NT_WARNING = lambda Status: (ULONG(Status).value >> 30) == 2
    NT_ERROR = lambda Status: (ULONG(Status).value >> 30) == 3

    APPLICATION_ERROR_MASK = 0x20000000
    ERROR_SEVERITY_SUCCESS = 0x00000000
    ERROR_SEVERITY_INFORMATIONAL = 0x40000000
    ERROR_SEVERITY_WARNING = 0x80000000
    ERROR_SEVERITY_ERROR = 0xC0000000

    class tagPOINTS(CStructure):
        _fields_ = [
            ("x", SHORT),
            ("y", SHORT)
        ]
    POINTS = tagPOINTS
    PPOINTS = POINTER(POINTS)
    LPPOINTS = PPOINTS

    PAPCFUNC = NTAPI(VOID, ULONG_PTR)
    
    if cpreproc.pragma_once("__SECSTATUS_DEFINED__"):
        SECURITY_STATUS = LONG
        
    class _LOWHIGH(CStructure):
        _fields_ = [
            ("LowPart", DWORD),
            ("HighPart", LONG)
        ]
    
    class _ULOWHIGH(CStructure):
        _fields_ = [
            ("LowPart", DWORD),
            ("HighPart", DWORD)
        ]
    
    class _ULARGE_INTEGER(Union):
        _fields_ = [
            ("s", _ULOWHIGH),
            ("u", _ULOWHIGH),
            ("QuadPart", LONGLONG)
        ]
        
    ULARGE_INTEGER = _ULARGE_INTEGER
    PULARGE_INTEGER = POINTER(ULARGE_INTEGER)
        
    class _LARGE_INTEGER(Union):
        _fields_ = [
            ("s", _LOWHIGH),
            ("u", _LOWHIGH),
            ("QuadPart", LONGLONG)
        ]

    LARGE_INTEGER = _LARGE_INTEGER
    PLARGE_INTEGER = POINTER(LARGE_INTEGER)
    TIME = LARGE_INTEGER
    _TIME = _LARGE_INTEGER
    PTIME = PLARGE_INTEGER
    LowTime = "LowPart"
    HighTime = "HighPart"
        
    class _FLOAT128(CStructure):
        _fields_ = [
            ("LowPart", INT64),
            ("HighPart", INT64)
        ]

    if cpreproc.pragma_once("_SYSTEMTIME_"):
        class SYSTEMTIME(CStructure):
            _fields_ = [
                ("wYear", WORD),
                ("wMonth", WORD),
                ("wDayOfWeek", WORD),
                ("wDay", WORD),
                ("wHour", WORD),
                ("wMinute", WORD),
                ("wSecond", WORD),
                ("wMilliseconds", WORD)
            ]
        PSYSTEMTIME = POINTER(SYSTEMTIME)
        LPSYSTEMTIME = PSYSTEMTIME
    if cpreproc.pragma_once("_SECURITY_ATTRIBUTES_"):
        class _SECURITY_ATTRIBUTES(CStructure):
            _fields_ = [
                ("nLength", DWORD),
                ("lpSecurityDescriptor", LPVOID),
                ("bInheritHandle", BOOL)
            ]
        SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
        PSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
        LPSECURITY_ATTRIBUTES = PSECURITY_ATTRIBUTES
    if cpreproc.ifndef("SECURITY_DESCRIPTOR_REVISIO"):
        SECURITY_DESCRIPTOR_CONTROL = USHORT

        PSECURITY_DESCRIPTOR_CONTROL = PUSHORT

        PSID = PVOID
        
    FLOAT128 = _FLOAT128
    PFLOAT128 = POINTER(FLOAT128)
    
    USN = LONGLONG
    
    RTL_REFERENCE_COUNT = LONG_PTR
    PRTL_REFERENCE_COUNT = POINTER(RTL_REFERENCE_COUNT)
    
    RTL_REFERENCE_COUNT32 = LONG
    PRTL_REFERENCE_COUNT32 = POINTER(RTL_REFERENCE_COUNT32)
    
    _LUID = _LOWHIGH
    LUID = _LUID
    PLUID = POINTER(LUID)
    
    DWORDLONG = ULONGLONG
    PDWORDLONG = PULONGLONG
    
    PHYSICAL_ADDRESS = LARGE_INTEGER
    PPHYSICAL_ADDRESS = PLARGE_INTEGER
    
    ANSI_NULL = CHAR(0)
    UNICODE_NULL = WCHAR(u"\x00")
    
    UNICODE_STRING_MAX_BYTES = WORD(65534)
    UNICODE_STRING_MAX_CHARS = 32767
    
    _EVENT_TYPE = INT
    if True:
        NotificationEvent = 0
        SynchronizationEvent = 1
    EVENT_TYPE = _EVENT_TYPE

    _TIMER_TYPE = INT
    if True:
        NotificationTimer = 0
        SynchronizationTimer = 1
    TIMER_TYPE = _TIMER_TYPE

    _WAIT_TYPE = INT
    if True:
        WaitAll = 0
        WaitAny = 1
        WaitNotification = 2
        WaitDequeue = 3
    WAIT_TYPE = _WAIT_TYPE
    
    PSZ = PZZSTR
    PCSZ = PCZZSTR
    
    RTL_STRING_LENGTH_TYPE = USHORT
    
    class _STRING(CStructure):
        _fields_ = [
            ("Length", USHORT),
            ("MaximumLength", USHORT),
            ("Buffer", PCHAR)
        ]
        
    STRING = _STRING
    PSTRING = POINTER(STRING)
    ANSI_STRING = STRING
    PANSI_STRING = PSTRING
    
    OEM_STRING = STRING
    POEM_STRING = PSTRING
    PCOEM_STRING = POEM_STRING
        
    class _CSTRING(CStructure):
        _fields_ = [
            ("Length", USHORT),
            ("MaximumLength", USHORT),
            ("Buffer", PCCHAR)
        ]
        
    CSTRING = _CSTRING
    PCSTRING = POINTER(CSTRING)
    
    CANSI_STRING = STRING
    PCANSI_STRING = PSTRING
    
    UTF8_STRING = STRING
    PUTF8_STRING = PSTRING
    
    class _UNICODE_STRING(CStructure):
        _fields_ = [
            ("Length", USHORT),
            ("MaximumLength", USHORT),
            ("Buffer", PWCH)
        ]
        
    UNICODE_STRING = _UNICODE_STRING
    PUNICODE_STRING = POINTER(_UNICODE_STRING)
    PCUNICODE_STRING = PUNICODE_STRING
    
    DECLARE_CONST_UNICODE_STRING = lambda _var, _string: exec(f"{_var}_buffer = WCHAR(TEXT({_string}))")
    DECLARE_GLOBAL_CONST_UNICODE_STRING = lambda _var, _str: DECLARE_CONST_UNICODE_STRING(_var, _str)
    DECLARE_UNICODE_STRING_SIZE = lambda _var, _size: exec(f"{_var}_buffer = (WCHAR * {_size})()")
    
    BOOLEAN = BYTE
    PBOOLEAN = PBYTE
    
    class _LIST_ENTRY(CStructure): pass
    _LIST_ENTRY._fields_ = [
        ("Flink", POINTER(_LIST_ENTRY)),
        ("Blink", POINTER(_LIST_ENTRY))
    ]
    
    LIST_ENTRY = _LIST_ENTRY
    PLIST_ENTRY = POINTER(LIST_ENTRY)
    
    class _SINGLE_LIST_ENTRY(CStructure): pass
    _SINGLE_LIST_ENTRY._fields_ = [
        ("Next", POINTER(_SINGLE_LIST_ENTRY))
    ]
    
    SINGLE_LIST_ENTRY = _SINGLE_LIST_ENTRY
    PSINGLE_LIST_ENTRY = POINTER(SINGLE_LIST_ENTRY)
    SLIST_ENTRY = SINGLE_LIST_ENTRY
    PSLIST_ENTRY = PSINGLE_LIST_ENTRY
    
    class _LIST_ENTRY32(CStructure):
        _fields_ = [
            ("Flink", DWORD),
            ("Blink", DWORD)
        ]
    
    LIST_ENTRY32 = _LIST_ENTRY32
    PLIST_ENTRY32 = POINTER(LIST_ENTRY32)
    
    class _LIST_ENTRY64(CStructure):
        _fields_ = [
            ("Flink", ULONGLONG),
            ("Blink", ULONGLONG)
        ]
    
    LIST_ENTRY64 = _LIST_ENTRY64
    PLIST_ENTRY64 = POINTER(LIST_ENTRY64)
    
    if cpreproc.pragma_once("_DEFINED__WNF_STATE_NAME"):
        class _WNF_STATE_NAME(CStructure):
            _fields_ = [
                ("Data", ULONG * 2)
            ]
        WNF_STATE_NAME = _WNF_STATE_NAME
        PWNF_STATE_NAME = POINTER(WNF_STATE_NAME)
        PCWNF_STATE_NAME = PWNF_STATE_NAME
        
    class _STRING32(CStructure):
        _fields_ = [
            ("Length", USHORT),
            ("MaximumLength", USHORT),
            ("Buffer", ULONG)
        ]
        
    STRING32 = _STRING32
    PSTRING32 = POINTER(STRING32)

    UNICODE_STRING32 = STRING32
    PUNICODE_STRING32 = PSTRING32

    ANSI_STRING32 = STRING32
    PANSI_STRING32 = PSTRING32

    class _STRING64(CStructure):
        _fields_ = [
            ("Length", USHORT),
            ("MaximumLength", USHORT),
            ("Buffer", ULONGLONG)
        ]
        
    STRING64 = _STRING64
    PSTRING64 = POINTER(STRING64)

    UNICODE_STRING64 = STRING64
    PUNICODE_STRING64 = PSTRING64

    ANSI_STRING64 = STRING64
    PANSI_STRING64 = PSTRING64
    
    OBJ_INHERIT = 0x00000002
    OBJ_PERMANENT = 0x00000010
    OBJ_EXCLUSIVE = 0x00000020
    OBJ_CASE_INSENSITIVE = 0x00000040
    OBJ_OPENIF = 0x00000080
    OBJ_OPENLINK = 0x00000100
    OBJ_KERNEL_HANDLE = 0x00000200
    OBJ_FORCE_ACCESS_CHECK = 0x00000400
    OBJ_IGNORE_IMPERSONATED_DEVICEMAP = 0x00000800
    OBJ_DONT_REPARSE = 0x00001000
    OBJ_VALID_ATTRIBUTES = 0x00001FF2
    
    class _OBJECT_ATTRIBUTES64(CStructure):
        _fields_ = [
            ("Length", ULONG),
            ("RootDirectory", ULONG64),
            ("ObjectName", ULONG64),
            ("Attributes", ULONG),
            ("SecurityDescriptor", ULONG64),
            ("SecurityQualityOfService", ULONG64)
        ]
        
    OBJECT_ATTRIBUTES64 = _OBJECT_ATTRIBUTES64
    POBJECT_ATTRIBUTES64 = POINTER(OBJECT_ATTRIBUTES64)
    PCOBJECT_ATTRIBUTES64 = POBJECT_ATTRIBUTES64
    
    class _OBJECT_ATTRIBUTES32(CStructure):
        _fields_ = [
            ("Length", ULONG),
            ("RootDirectory", ULONG),
            ("ObjectName", ULONG),
            ("Attributes", ULONG),
            ("SecurityDescriptor", ULONG),
            ("SecurityQualityOfService", ULONG)
        ]
        
    OBJECT_ATTRIBUTES32 = _OBJECT_ATTRIBUTES32
    POBJECT_ATTRIBUTES32 = POINTER(OBJECT_ATTRIBUTES32)
    PCOBJECT_ATTRIBUTES32 = POBJECT_ATTRIBUTES32
    
    class _OBJECT_ATTRIBUTES(CStructure):
        _fields_ = [
            ("Length", ULONG),
            ("RootDirectory", HANDLE),
            ("ObjectName", PUNICODE_STRING),
            ("Attributes", ULONG),
            ("SecurityDescriptor", PVOID),
            ("SecurityQualityOfService", PVOID)
        ]
        
    OBJECT_ATTRIBUTES = _OBJECT_ATTRIBUTES
    POBJECT_ATTRIBUTES = POINTER(OBJECT_ATTRIBUTES)
    PCOBJECT_ATTRIBUTES = POBJECT_ATTRIBUTES
    
    def InitializeObjectAttributes( p, n, a, r, s ):
        p.Length = sizeof(OBJECT_ATTRIBUTES)
        p.RootDirectory = r
        p.Attributes = a
        p.ObjectName = n
        p.SecurityDescriptor = s
        p.SecurityQualityOfService = LPVOID(0)
        
    FALSE = 0
    TRUE = 1

    NULL = VOID
    NULL64 = NULL

    DLL_DIRECTORY_COOKIE = PVOID
    
    from .guiddef import *
    
    if cpreproc.pragma_once("__OBJECTID_DEFINED"):
        class _OBJECTID(CStructure):
            _fields_ = [
                ("Lineage", GUID),
                ("Uniquifier", DWORD)
            ]
        OBJECTID = _OBJECTID
    
    if True:
        MINCHAR = 0x80
        MAXCHAR = 0x7F
        MINSHORT = 0x8000
        MAXSHPRT = 0x7FFF
        MINLONG = 0x80000000  
        MAXLONG = 0x7fffffff  
        MAXBYTE = 0xff        
        MAXWORD = 0xffff      
        MAXDWORD = 0xffffffff  
        
        def FIELD_OFFSET(typ, field_name):
            null_ptr = cast(0, POINTER(typ))
            field_ptr = addressof(getattr(null_ptr.contents, field_name))
            offset = field_ptr
            return LONG(offset)

        def UFIELD_OFFSET(typ, field_name):
            null_ptr = cast(0, POINTER(typ))
            field_ptr = addressof(getattr(null_ptr.contents, field_name))
            offset = field_ptr
            return ULONG(offset)
            
        def RTL_FIELD_SIZE(typ, field_name):
            null_ptr = cast(addressof(typ()), POINTER(typ))
            field_ptr = getattr(null_ptr.contents, field_name)
            return sizeof(field_ptr)
            
        def RTL_SIZEOF_THROUGH_FIELD(typ, field_name):
            return FIELD_OFFSET(typ, field_name) + RTL_FIELD_SIZE(typ, field_name)
            
        def RTL_NUMBER_OF_V1(A):
            return sizeof(A) // sizeof(A[0])
            
        def RTL_NUMBER_OF_V2(A):
            return RTL_NUMBER_OF_V1(A)

        if cpreproc.ifdef("ENABLE_RTL_NUMBER_OF_V2"):
            def RTL_NUMBER_OF(A):
                return RTL_NUMBER_OF_V2(A)
        else:
            def RTL_NUMBER_OF(A):
                return RTL_NUMBER_OF_V1(A)
                
        def ARRAYSIZE(A):
            return RTL_NUMBER_OF_V2(A)
        def _ARRAYSIZE(A):
            return RTL_NUMBER_OF_V1(A)

        def RTL_FIELD_TYPE(typ, field_name):
            null_ptr = cast(0, POINTER(typ))
            field = getattr(null_ptr.contents, field_name)
            return field
            
        def RTL_NUMBER_OF_FIELD(typ, field_name):
            return RTL_NUMBER_OF(RTL_FIELD_TYPE(typ, field_name))

        def RTL_PADDING_BETWEEN_FIELDS(T, F1, F2):
            return (FIELD_OFFSET(T, F2) - FIELD_OFFSET(T, F1) - RTL_FIELD_SIZE(T, F1)) if (FIELD_OFFSET(T, F2) > FIELD_OFFSET(T, F1)) else (FIELD_OFFSET(T, F1) - FIELD_OFFSET(T, F2) - RTL_FIELD_SIZE(T, F2))

        def RTL_BITS_OF(sizeOfArg):
            return sizeof(sizeOfArg) * 8

        def RTL_BITS_OF_FIELD(typ, field_name):
            return RTL_BITS_OF(RTL_FIELD_TYPE(typ, field_name))
            
        EXCEPTION_MAXIMUM_PARAMETERS = 15
            
        class _M128A(CStructure):
            _fields_ = [("Low", DWORD64), ("High", DWORD64)]
            
        M128A = _M128A
        PM128A = POINTER(M128A)

        class XMM_SAVE_AREA32(CStructure):
            _fields_ = [
                ("ControlWord", WORD),
                ("StatusWord", WORD),
                ("TagWord", WORD),
                ("ErrorOffset", WORD),
                ("ErrorSelector", WORD),
                ("DataOffset", WORD),
                ("DataSelector", WORD),
                ("RegisterArea", UINT8 * 80),
                ("Cr0NpxState", DWORD)
            ]

        class _CONTEXT(CStructure):
            _fields_ = [
                ("P1Home", DWORD64),
                ("P2Home", DWORD64),
                ("P3Home", DWORD64),
                ("P4Home", DWORD64),
                ("P5Home", DWORD64),
                ("P6Home", DWORD64),
                ("ContextFlags", DWORD),
                ("MxCsr", DWORD),
                ("SegCs", WORD),
                ("SegDs", WORD),
                ("SegEs", WORD),
                ("SegFs", WORD),
                ("SegGs", WORD),
                ("SegSs", WORD),
                ("EFlags", DWORD),
                ("Dr0", DWORD64),
                ("Dr1", DWORD64),
                ("Dr2", DWORD64),
                ("Dr3", DWORD64),
                ("Dr6", DWORD64),
                ("Dr7", DWORD64),
                ("Rax", DWORD64),
                ("Rcx", DWORD64),
                ("Rdx", DWORD64),
                ("Rbx", DWORD64),
                ("Rsp", DWORD64),
                ("Rbp", DWORD64),
                ("Rsi", DWORD64),
                ("Rdi", DWORD64),
                ("R8", DWORD64),
                ("R9", DWORD64),
                ("R10", DWORD64),
                ("R11", DWORD64),
                ("R12", DWORD64),
                ("R13", DWORD64),
                ("R14", DWORD64),
                ("R15", DWORD64),
                ("Rip", DWORD64),
                ("FltSave", XMM_SAVE_AREA32),
                ("VectorRegister", M128A * 26),
                ("VectorControl", DWORD64),
                ("DebugControl", DWORD64),
                ("LastBranchToRip", DWORD64),
                ("LastBranchFromRip", DWORD64),
                ("LastExceptionToRip", DWORD64),
                ("LastExceptionFromRip", DWORD64)
            ]
            
            VectorRegister: IArray[M128A]
            FltSave: XMM_SAVE_AREA32
            LastExceptionFromRip: int
            LastExceptionToRip: int
            LastBranchFromRip: int
            LastBranchToRip: int
            VectorControl: int
            ContextFlags: int
            DebugControl: int
            P1Home: int
            P2Home: int
            P3Home: int
            P4Home: int
            P5Home: int
            P6Home: int
            EFlags: int
            MxCsr: int
            SegCs: int
            SegDs: int
            SegEs: int
            SegFs: int
            SegGs: int
            SegSs: int
            Dr0: int
            Dr1: int
            Dr2: int
            Dr3: int
            Dr6: int
            Dr7: int
            Rax: int
            Rcx: int
            Rdx: int
            Rbx: int
            Rsp: int
            Rbp: int
            Rsi: int
            Rdi: int
            R10: int
            R11: int
            R12: int
            R13: int
            R14: int
            R15: int
            Rip: int
            R8: int
            R9: int
        
        _EXCEPTION_DISPOSITION = INT
        if True:
            ExceptionContinueExecution = 0
            ExceptionContinueSearch = 1
            ExceptionNestedException = 2
            ExceptionCollidedUnwind = 3
        EXCEPTION_DISPOSITION = _EXCEPTION_DISPOSITION
            
        class _EXCEPTION_RECORD(CStructure): 
            ExceptionCode: int
            ExceptionFlags: int
            ExceptionRecord: IPointer['_EXCEPTION_RECORD']
            ExceptionAddress: PVOID
            NumberParameters: int
            ExceptionInformation: IPointer[ULONG_PTR]
            
        _EXCEPTION_RECORD._fields_ = [
            ("ExceptionCode", DWORD),
            ("ExceptionFlags", DWORD),
            ("ExceptionRecord", POINTER(_EXCEPTION_RECORD)),
            ("ExceptionAddress", PVOID),
            ("NumberParameters", DWORD),
            ("ExceptionInformation", ULONG_PTR * EXCEPTION_MAXIMUM_PARAMETERS)
        ]
        EXCEPTION_RECORD = _EXCEPTION_RECORD
            
        CONTEXT = _CONTEXT
        PCONTEXT = POINTER(CONTEXT)
        EXCEPTION_ROUTINE = NTAPI(
            EXCEPTION_DISPOSITION,
            POINTER(EXCEPTION_RECORD),
            PVOID,
            POINTER(CONTEXT),
            PVOID
        )

        class _EXCEPTION_POINTERS(CStructure):
            _fields_ = [
                ("ExceptionRecord", POINTER(EXCEPTION_RECORD)),
                ("ContextRecord", PCONTEXT)
            ]
            
            ExceptionRecord: IPointer[EXCEPTION_RECORD]
            ContextRecord: IPointer[CONTEXT]
            
        EXCEPTION_POINTERS = _EXCEPTION_POINTERS
        PEXCEPTION_POINTERS = POINTER(EXCEPTION_POINTERS)

        PVECTORED_EXCEPTION_HANDLER = NTAPI(LONG, PEXCEPTION_POINTERS)

        WOW64_CONTEXT_i386 = 0x00010000
        WOW64_CONTEXT_CONTROL = (WOW64_CONTEXT_i386 | 0x00000001)
        WOW64_CONTEXT_INTEGER = (WOW64_CONTEXT_i386 | 0x00000002)
        WOW64_CONTEXT_SEGMENTS = (WOW64_CONTEXT_i386 | 0x00000004)
        WOW64_CONTEXT_FLOATING_POINT = (WOW64_CONTEXT_i386 | 0x00000008)
        WOW64_CONTEXT_DEBUG_REGISTERS = (WOW64_CONTEXT_i386 | 0x00000010)
        WOW64_CONTEXT_EXTENDED_REGISTERS = (WOW64_CONTEXT_i386 | 0x00000020)
        WOW64_CONTEXT_FULL = (WOW64_CONTEXT_CONTROL | WOW64_CONTEXT_INTEGER | WOW64_CONTEXT_SEGMENTS)
        WOW64_CONTEXT_ALL = (WOW64_CONTEXT_CONTROL | WOW64_CONTEXT_INTEGER | WOW64_CONTEXT_SEGMENTS |
                            WOW64_CONTEXT_FLOATING_POINT | WOW64_CONTEXT_DEBUG_REGISTERS |
                            WOW64_CONTEXT_EXTENDED_REGISTERS)
        WOW64_CONTEXT_XSTATE = (WOW64_CONTEXT_i386 | 0x00000040)
        WOW64_CONTEXT_EXCEPTION_ACTIVE = 0x08000000
        WOW64_CONTEXT_SERVICE_ACTIVE = 0x10000000
        WOW64_CONTEXT_EXCEPTION_REQUEST = 0x40000000
        WOW64_CONTEXT_EXCEPTION_REPORTING = 0x80000000
        WOW64_SIZE_OF_80387_REGISTERS = 80
        WOW64_MAXIMUM_SUPPORTED_EXTENSION = 512

        class WOW64_FLOATING_SAVE_AREA(CStructure):
            _fields_ = [
                ("ControlWord", DWORD),
                ("StatusWord", DWORD),
                ("TagWord", DWORD),
                ("ErrorOffset", DWORD),
                ("ErrorSelector", DWORD),
                ("DataOffset", DWORD),
                ("DataSelector", DWORD),
                ("RegisterArea", BYTE * WOW64_SIZE_OF_80387_REGISTERS),
                ("Cr0NpxState", DWORD)
            ]

        class WOW64_CONTEXT(CStructure):
            _fields_ = [
                ("ContextFlags", DWORD),
                ("Dr0", DWORD),
                ("Dr1", DWORD),
                ("Dr2", DWORD),
                ("Dr3", DWORD),
                ("Dr6", DWORD),
                ("Dr7", DWORD),
                ("FloatSave", WOW64_FLOATING_SAVE_AREA),
                ("SegGs", DWORD),
                ("SegFs", DWORD),
                ("SegEs", DWORD),
                ("SegDs", DWORD),
                ("Edi", DWORD),
                ("Esi", DWORD),
                ("Ebx", DWORD),
                ("Edx", DWORD),
                ("Ecx", DWORD),
                ("Eax", DWORD),
                ("Ebp", DWORD),
                ("Eip", DWORD),
                ("SegCs", DWORD),
                ("EFlags", DWORD),
                ("Esp", DWORD),
                ("SegSs", DWORD),
                ("ExtendedRegisters", BYTE * WOW64_MAXIMUM_SUPPORTED_EXTENSION)
            ]
            
            ExtendedRegisters: IArrayFixedSize[BYTE, 512]
            FloatSave: WOW64_FLOATING_SAVE_AREA
            ContextFlags: int
            EFlags: int
            SegGs: int
            SegFs: int
            SegEs: int
            SegDs: int
            SegCs: int
            SegSs: int
            Dr0: int
            Dr1: int
            Dr2: int
            Dr3: int
            Dr6: int
            Dr7: int
            Edi: int
            Esi: int
            Ebx: int
            Edx: int
            Ecx: int
            Eax: int
            Ebp: int
            Eip: int
            Esp: int

        PWOW64_FLOATING_SAVE_AREA = POINTER(WOW64_FLOATING_SAVE_AREA)
        PWOW64_CONTEXT = POINTER(WOW64_CONTEXT)

        ENCLAVE_SHORT_ID_LENGTH = 16
        ENCLAVE_LONG_ID_LENGTH = 32


        VER_SERVER_NT = 0x80000000
        VER_WORKSTATION_NT = 0x40000000
        VER_SUITE_SMALLBUSINESS = 0x00000001
        VER_SUITE_ENTERPRISE = 0x00000002
        VER_SUITE_BACKOFFICE = 0x00000004
        VER_SUITE_COMMUNICATIONS = 0x00000008
        VER_SUITE_TERMINAL = 0x00000010
        VER_SUITE_SMALLBUSINESS_RESTRICTED = 0x00000020
        VER_SUITE_EMBEDDEDNT = 0x00000040
        VER_SUITE_DATACENTER = 0x00000080
        VER_SUITE_SINGLEUSERTS = 0x00000100
        VER_SUITE_PERSONAL = 0x00000200
        VER_SUITE_BLADE = 0x00000400
        VER_SUITE_EMBEDDED_RESTRICTED = 0x00000800
        VER_SUITE_SECURITY_APPLIANCE = 0x00001000
        VER_SUITE_STORAGE_SERVER = 0x00002000
        VER_SUITE_COMPUTE_SERVER = 0x00004000
        VER_SUITE_WH_SERVER = 0x00008000
        VER_SUITE_MULTIUSERTS = 0x00020000
        
        PRODUCT_UNDEFINED = 0x00000000
        PRODUCT_ULTIMATE = 0x00000001
        PRODUCT_HOME_BASIC = 0x00000002
        PRODUCT_HOME_PREMIUM = 0x00000003
        PRODUCT_ENTERPRISE = 0x00000004
        PRODUCT_HOME_BASIC_N = 0x00000005
        PRODUCT_BUSINESS = 0x00000006
        PRODUCT_STANDARD_SERVER = 0x00000007
        PRODUCT_DATACENTER_SERVER = 0x00000008
        PRODUCT_SMALLBUSINESS_SERVER = 0x00000009
        PRODUCT_ENTERPRISE_SERVER = 0x0000000A
        PRODUCT_STARTER = 0x0000000B
        PRODUCT_DATACENTER_SERVER_CORE = 0x0000000C
        PRODUCT_STANDARD_SERVER_CORE = 0x0000000D
        PRODUCT_ENTERPRISE_SERVER_CORE = 0x0000000E
        PRODUCT_ENTERPRISE_SERVER_IA64 = 0x0000000F
        PRODUCT_BUSINESS_N = 0x00000010
        PRODUCT_WEB_SERVER = 0x00000011
        PRODUCT_CLUSTER_SERVER = 0x00000012
        PRODUCT_HOME_SERVER = 0x00000013
        PRODUCT_STORAGE_EXPRESS_SERVER = 0x00000014
        PRODUCT_STORAGE_STANDARD_SERVER = 0x00000015
        PRODUCT_STORAGE_WORKGROUP_SERVER = 0x00000016
        PRODUCT_STORAGE_ENTERPRISE_SERVER = 0x00000017
        PRODUCT_SERVER_FOR_SMALLBUSINESS = 0x00000018
        PRODUCT_SMALLBUSINESS_SERVER_PREMIUM = 0x00000019
        PRODUCT_HOME_PREMIUM_N = 0x0000001A
        PRODUCT_ENTERPRISE_N = 0x0000001B
        PRODUCT_ULTIMATE_N = 0x0000001C
        PRODUCT_WEB_SERVER_CORE = 0x0000001D
        PRODUCT_MEDIUMBUSINESS_SERVER_MANAGEMENT = 0x0000001E
        PRODUCT_MEDIUMBUSINESS_SERVER_SECURITY = 0x0000001F
        PRODUCT_MEDIUMBUSINESS_SERVER_MESSAGING = 0x00000020
        PRODUCT_SERVER_FOUNDATION = 0x00000021
        PRODUCT_HOME_PREMIUM_SERVER = 0x00000022
        PRODUCT_SERVER_FOR_SMALLBUSINESS_V = 0x00000023
        PRODUCT_STANDARD_SERVER_V = 0x00000024
        PRODUCT_DATACENTER_SERVER_V = 0x00000025
        PRODUCT_ENTERPRISE_SERVER_V = 0x00000026
        PRODUCT_DATACENTER_SERVER_CORE_V = 0x00000027
        PRODUCT_STANDARD_SERVER_CORE_V = 0x00000028
        PRODUCT_ENTERPRISE_SERVER_CORE_V = 0x00000029
        PRODUCT_HYPERV = 0x0000002A
        PRODUCT_STORAGE_EXPRESS_SERVER_CORE = 0x0000002B
        PRODUCT_STORAGE_STANDARD_SERVER_CORE = 0x0000002C
        PRODUCT_STORAGE_WORKGROUP_SERVER_CORE = 0x0000002D
        PRODUCT_STORAGE_ENTERPRISE_SERVER_CORE = 0x0000002E
        PRODUCT_STARTER_N = 0x0000002F
        PRODUCT_PROFESSIONAL = 0x00000030
        PRODUCT_PROFESSIONAL_N = 0x00000031
        PRODUCT_SB_SOLUTION_SERVER = 0x00000032
        PRODUCT_SERVER_FOR_SB_SOLUTIONS = 0x00000033
        PRODUCT_STANDARD_SERVER_SOLUTIONS = 0x00000034
        PRODUCT_STANDARD_SERVER_SOLUTIONS_CORE = 0x00000035
        PRODUCT_SB_SOLUTION_SERVER_EM = 0x00000036
        PRODUCT_SERVER_FOR_SB_SOLUTIONS_EM = 0x00000037
        PRODUCT_SOLUTION_EMBEDDEDSERVER = 0x00000038
        PRODUCT_SOLUTION_EMBEDDEDSERVER_CORE = 0x00000039
        PRODUCT_PROFESSIONAL_EMBEDDED = 0x0000003A
        PRODUCT_ESSENTIALBUSINESS_SERVER_MGMT = 0x0000003B
        PRODUCT_ESSENTIALBUSINESS_SERVER_ADDL = 0x0000003C
        PRODUCT_ESSENTIALBUSINESS_SERVER_MGMTSVC = 0x0000003D
        PRODUCT_ESSENTIALBUSINESS_SERVER_ADDLSVC = 0x0000003E
        PRODUCT_SMALLBUSINESS_SERVER_PREMIUM_CORE = 0x0000003F
        PRODUCT_CLUSTER_SERVER_V = 0x00000040
        PRODUCT_EMBEDDED = 0x00000041
        PRODUCT_STARTER_E = 0x00000042
        PRODUCT_HOME_BASIC_E = 0x00000043
        PRODUCT_HOME_PREMIUM_E = 0x00000044
        PRODUCT_PROFESSIONAL_E = 0x00000045
        PRODUCT_ENTERPRISE_E = 0x00000046
        PRODUCT_ULTIMATE_E = 0x00000047
        PRODUCT_ENTERPRISE_EVALUATION = 0x00000048
        PRODUCT_MULTIPOINT_STANDARD_SERVER = 0x0000004C
        PRODUCT_MULTIPOINT_PREMIUM_SERVER = 0x0000004D
        PRODUCT_STANDARD_EVALUATION_SERVER = 0x0000004F
        PRODUCT_DATACENTER_EVALUATION_SERVER = 0x00000050
        PRODUCT_ENTERPRISE_N_EVALUATION = 0x00000054
        PRODUCT_EMBEDDED_AUTOMOTIVE = 0x00000055
        PRODUCT_EMBEDDED_INDUSTRY_A = 0x00000056
        PRODUCT_THINPC = 0x00000057
        PRODUCT_EMBEDDED_A = 0x00000058
        PRODUCT_EMBEDDED_INDUSTRY = 0x00000059
        PRODUCT_EMBEDDED_E = 0x0000005A
        PRODUCT_EMBEDDED_INDUSTRY_E = 0x0000005B
        PRODUCT_EMBEDDED_INDUSTRY_A_E = 0x0000005C
        PRODUCT_STORAGE_WORKGROUP_EVALUATION_SERVER = 0x0000005F
        PRODUCT_STORAGE_STANDARD_EVALUATION_SERVER = 0x00000060
        PRODUCT_CORE_ARM = 0x00000061
        PRODUCT_CORE_N = 0x00000062
        PRODUCT_CORE_COUNTRYSPECIFIC = 0x00000063
        PRODUCT_CORE_SINGLELANGUAGE = 0x00000064
        PRODUCT_CORE = 0x00000065
        PRODUCT_PROFESSIONAL_WMC = 0x00000067
        PRODUCT_EMBEDDED_INDUSTRY_EVAL = 0x00000069
        PRODUCT_EMBEDDED_INDUSTRY_E_EVAL = 0x0000006A
        PRODUCT_EMBEDDED_EVAL = 0x0000006B
        PRODUCT_EMBEDDED_E_EVAL = 0x0000006C
        PRODUCT_NANO_SERVER = 0x0000006D
        PRODUCT_CLOUD_STORAGE_SERVER = 0x0000006E
        PRODUCT_CORE_CONNECTED = 0x0000006F
        PRODUCT_PROFESSIONAL_STUDENT = 0x00000070
        PRODUCT_CORE_CONNECTED_N = 0x00000071
        PRODUCT_PROFESSIONAL_STUDENT_N = 0x00000072
        PRODUCT_CORE_CONNECTED_SINGLELANGUAGE = 0x00000073
        PRODUCT_CORE_CONNECTED_COUNTRYSPECIFIC = 0x00000074
        PRODUCT_CONNECTED_CAR = 0x00000075
        PRODUCT_INDUSTRY_HANDHELD = 0x00000076
        PRODUCT_PPI_PRO = 0x00000077
        PRODUCT_ARM64_SERVER = 0x00000078
        PRODUCT_EDUCATION = 0x00000079
        PRODUCT_EDUCATION_N = 0x0000007A
        PRODUCT_IOTUAP = 0x0000007B
        PRODUCT_CLOUD_HOST_INFRASTRUCTURE_SERVER = 0x0000007C
        PRODUCT_ENTERPRISE_S = 0x0000007D
        PRODUCT_ENTERPRISE_S_N = 0x0000007E
        PRODUCT_PROFESSIONAL_S = 0x0000007F
        PRODUCT_PROFESSIONAL_S_N = 0x00000080
        PRODUCT_ENTERPRISE_S_EVALUATION = 0x00000081
        PRODUCT_ENTERPRISE_S_N_EVALUATION = 0x00000082
        PRODUCT_HOLOGRAPHIC = 0x00000087
        PRODUCT_HOLOGRAPHIC_BUSINESS = 0x00000088
        PRODUCT_PRO_SINGLE_LANGUAGE = 0x0000008A
        PRODUCT_PRO_CHINA = 0x0000008B
        PRODUCT_ENTERPRISE_SUBSCRIPTION = 0x0000008C
        PRODUCT_ENTERPRISE_SUBSCRIPTION_N = 0x0000008D
        PRODUCT_DATACENTER_NANO_SERVER = 0x0000008F
        PRODUCT_STANDARD_NANO_SERVER = 0x00000090
        PRODUCT_DATACENTER_A_SERVER_CORE = 0x00000091
        PRODUCT_STANDARD_A_SERVER_CORE = 0x00000092
        PRODUCT_DATACENTER_WS_SERVER_CORE = 0x00000093
        PRODUCT_STANDARD_WS_SERVER_CORE = 0x00000094
        PRODUCT_UTILITY_VM = 0x00000095
        PRODUCT_DATACENTER_EVALUATION_SERVER_CORE = 0x0000009F
        PRODUCT_STANDARD_EVALUATION_SERVER_CORE = 0x000000A0
        PRODUCT_PRO_WORKSTATION = 0x000000A1
        PRODUCT_PRO_WORKSTATION_N = 0x000000A2
        PRODUCT_PRO_FOR_EDUCATION = 0x000000A4
        PRODUCT_PRO_FOR_EDUCATION_N = 0x000000A5
        PRODUCT_AZURE_SERVER_CORE = 0x000000A8
        PRODUCT_AZURE_NANO_SERVER = 0x000000A9
        PRODUCT_ENTERPRISEG = 0x000000AB
        PRODUCT_ENTERPRISEGN = 0x000000AC
        PRODUCT_SERVERRDSH = 0x000000AF
        PRODUCT_CLOUD = 0x000000B2
        PRODUCT_CLOUDN = 0x000000B3
        PRODUCT_HUBOS = 0x000000B4
        PRODUCT_ONECOREUPDATEOS = 0x000000B6
        PRODUCT_CLOUDE = 0x000000B7
        PRODUCT_ANDROMEDA = 0x000000B8
        PRODUCT_IOTOS = 0x000000B9
        PRODUCT_CLOUDEN = 0x000000BA
        PRODUCT_IOTEDGEOS = 0x000000BB
        PRODUCT_IOTENTERPRISE = 0x000000BC
        PRODUCT_LITE = 0x000000BD
        PRODUCT_IOTENTERPRISES = 0x000000BF
        PRODUCT_XBOX_SYSTEMOS = 0x000000C0
        PRODUCT_XBOX_NATIVEOS = 0x000000C1
        PRODUCT_XBOX_GAMEOS = 0x000000C2
        PRODUCT_XBOX_ERAOS = 0x000000C3
        PRODUCT_XBOX_DURANGOHOSTOS = 0x000000C4
        PRODUCT_XBOX_SCARLETTHOSTOS = 0x000000C5
        PRODUCT_UNLICENSED = 0xABCDABCD
        
        LANG_NEUTRAL = 0x00
        LANG_INVARIANT = 0x7f
        LANG_AFRIKAANS = 0x36
        LANG_ALBANIAN = 0x1c
        LANG_ALSATIAN = 0x84
        LANG_AMHARIC = 0x5e
        LANG_ARABIC = 0x01
        LANG_ARMENIAN = 0x2b
        LANG_ASSAMESE = 0x4d
        LANG_AZERI = 0x2c
        LANG_AZERBAIJANI = 0x2c
        LANG_BANGLA = 0x45
        LANG_BASHKIR = 0x6d
        LANG_BASQUE = 0x2d
        LANG_BELARUSIAN = 0x23
        LANG_BENGALI = 0x45
        LANG_BRETON = 0x7e
        LANG_BOSNIAN = 0x1a
        LANG_BOSNIAN_NEUTRAL = 0x781a
        LANG_BULGARIAN = 0x02
        LANG_CATALAN = 0x03
        LANG_CENTRAL_KURDISH = 0x92
        LANG_CHEROKEE = 0x5c
        LANG_CHINESE = 0x04
        LANG_CHINESE_SIMPLIFIED = 0x04
        LANG_CHINESE_TRADITIONAL = 0x7c04
        LANG_CORSICAN = 0x83
        LANG_CROATIAN = 0x1a
        LANG_CZECH = 0x05
        LANG_DANISH = 0x06
        LANG_DARI = 0x8c
        LANG_DIVEHI = 0x65
        LANG_DUTCH = 0x13
        LANG_ENGLISH = 0x09
        LANG_ESTONIAN = 0x25
        LANG_FAEROESE = 0x38
        LANG_FARSI = 0x29
        LANG_FILIPINO = 0x64
        LANG_FINNISH = 0x0b
        LANG_FRENCH = 0x0c
        LANG_FRISIAN = 0x62
        LANG_FULAH = 0x67
        LANG_GALICIAN = 0x56
        LANG_GEORGIAN = 0x37
        LANG_GERMAN = 0x07
        LANG_GREEK = 0x08
        LANG_GREENLANDIC = 0x6f
        LANG_GUJARATI = 0x47
        LANG_HAUSA = 0x68
        LANG_HAWAIIAN = 0x75
        LANG_HEBREW = 0x0d
        LANG_HINDI = 0x39
        LANG_HUNGARIAN = 0x0e
        LANG_ICELANDIC = 0x0f
        LANG_IGBO = 0x70
        LANG_INDONESIAN = 0x21
        LANG_INUKTITUT = 0x5d
        LANG_IRISH = 0x3c
        LANG_ITALIAN = 0x10
        LANG_JAPANESE = 0x11
        LANG_KANNADA = 0x4b
        LANG_KASHMIRI = 0x60
        LANG_KAZAK = 0x3f
        LANG_KHMER = 0x53
        LANG_KICHE = 0x86
        LANG_KINYARWANDA = 0x87
        LANG_KONKANI = 0x57
        LANG_KOREAN = 0x12
        LANG_KYRGYZ = 0x40
        LANG_LAO = 0x54
        LANG_LATVIAN = 0x26
        LANG_LITHUANIAN = 0x27
        LANG_LOWER_SORBIAN = 0x2e
        LANG_LUXEMBOURGISH = 0x6e
        LANG_MACEDONIAN = 0x2f
        LANG_MALAY = 0x3e
        LANG_MALAYALAM = 0x4c
        LANG_MALTESE = 0x3a
        LANG_MANIPURI = 0x58
        LANG_MAORI = 0x81
        LANG_MAPUDUNGUN = 0x7a
        LANG_MARATHI = 0x4e
        LANG_MOHAWK = 0x7c
        LANG_MONGOLIAN = 0x50
        LANG_NEPALI = 0x61
        LANG_NORWEGIAN = 0x14
        LANG_OCCITAN = 0x82
        LANG_ODIA = 0x48
        LANG_ORIYA = 0x48
        LANG_PASHTO = 0x63
        LANG_PERSIAN = 0x29
        LANG_POLISH = 0x15
        LANG_PORTUGUESE = 0x16
        LANG_PULAR = 0x67
        LANG_PUNJABI = 0x46
        LANG_QUECHUA = 0x6b
        LANG_ROMANIAN = 0x18
        LANG_ROMANSH = 0x17
        LANG_RUSSIAN = 0x19
        LANG_SAKHA = 0x85
        LANG_SAMI = 0x3b
        LANG_SANSKRIT = 0x4f
        LANG_SCOTTISH_GAELIC = 0x91
        LANG_SERBIAN = 0x1a
        LANG_SERBIAN_NEUTRAL = 0x7c1a
        LANG_SINDHI = 0x59
        LANG_SINHALESE = 0x5b
        LANG_SLOVAK = 0x1b
        LANG_SLOVENIAN = 0x24
        LANG_SOTHO = 0x6c
        LANG_SPANISH = 0x0a
        LANG_SWAHILI = 0x41
        LANG_SWEDISH = 0x1d
        LANG_SYRIAC = 0x5a
        LANG_TAJIK = 0x28
        LANG_TAMAZIGHT = 0x5f
        LANG_TAMIL = 0x49
        LANG_TATAR = 0x44
        LANG_TELUGU = 0x4a
        LANG_THAI = 0x1e
        LANG_TIBETAN = 0x51
        LANG_TIGRIGNA = 0x73
        LANG_TIGRINYA = 0x73
        LANG_TSWANA = 0x32
        LANG_TURKISH = 0x1f
        LANG_TURKMEN = 0x42
        LANG_UIGHUR = 0x80
        LANG_UKRAINIAN = 0x22
        LANG_UPPER_SORBIAN = 0x2e
        LANG_URDU = 0x20
        LANG_UZBEK = 0x43
        LANG_VALENCIAN = 0x03
        LANG_VIETNAMESE = 0x2a
        LANG_WELSH = 0x52
        LANG_WOLOF = 0x88
        LANG_XHOSA = 0x34
        LANG_YAKUT = 0x85
        LANG_YI = 0x78
        LANG_YORUBA = 0x6a
        LANG_ZULU = 0x35
        SUBLANG_NEUTRAL = 0x00
        SUBLANG_DEFAULT = 0x01
        SUBLANG_SYS_DEFAULT = 0x02
        SUBLANG_CUSTOM_DEFAULT = 0x03
        SUBLANG_CUSTOM_UNSPECIFIED = 0x04
        SUBLANG_UI_CUSTOM_DEFAULT = 0x05
        SUBLANG_AFRIKAANS_SOUTH_AFRICA = 0x01
        SUBLANG_ALBANIAN_ALBANIA = 0x01
        SUBLANG_ALSATIAN_FRANCE = 0x01
        SUBLANG_AMHARIC_ETHIOPIA = 0x01
        SUBLANG_ARABIC_SAUDI_ARABIA = 0x01
        SUBLANG_ARABIC_IRAQ = 0x02
        SUBLANG_ARABIC_EGYPT = 0x03
        SUBLANG_ARABIC_LIBYA = 0x04
        SUBLANG_ARABIC_ALGERIA = 0x05
        SUBLANG_ARABIC_MOROCCO = 0x06
        SUBLANG_ARABIC_TUNISIA = 0x07
        SUBLANG_ARABIC_OMAN = 0x08
        SUBLANG_ARABIC_YEMEN = 0x09
        SUBLANG_ARABIC_SYRIA = 0x0a
        SUBLANG_ARABIC_JORDAN = 0x0b
        SUBLANG_ARABIC_LEBANON = 0x0c
        SUBLANG_ARABIC_KUWAIT = 0x0d
        SUBLANG_ARABIC_UAE = 0x0e
        SUBLANG_ARABIC_BAHRAIN = 0x0f
        SUBLANG_ARABIC_QATAR = 0x10
        SUBLANG_ARMENIAN_ARMENIA = 0x01
        SUBLANG_ASSAMESE_INDIA = 0x01
        SUBLANG_AZERI_LATIN = 0x01
        SUBLANG_AZERI_CYRILLIC = 0x02
        SUBLANG_AZERBAIJANI_AZERBAIJAN_LATIN = 0x01
        SUBLANG_AZERBAIJANI_AZERBAIJAN_CYRILLIC = 0x02
        SUBLANG_BANGLA_INDIA = 0x01
        SUBLANG_BANGLA_BANGLADESH = 0x02
        SUBLANG_BASHKIR_RUSSIA = 0x01
        SUBLANG_BASQUE_BASQUE = 0x01
        SUBLANG_BELARUSIAN_BELARUS = 0x01
        SUBLANG_BENGALI_INDIA = 0x01
        SUBLANG_BENGALI_BANGLADESH = 0x02
        SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_LATIN = 0x05
        SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_CYRILLIC = 0x08
        SUBLANG_BRETON_FRANCE = 0x01
        SUBLANG_BULGARIAN_BULGARIA = 0x01
        SUBLANG_CATALAN_CATALAN = 0x01
        SUBLANG_CENTRAL_KURDISH_IRAQ = 0x01
        SUBLANG_CHEROKEE_CHEROKEE = 0x01
        SUBLANG_CHINESE_TRADITIONAL = 0x01
        SUBLANG_CHINESE_SIMPLIFIED = 0x02
        SUBLANG_CHINESE_HONGKONG = 0x03
        SUBLANG_CHINESE_SINGAPORE = 0x04
        SUBLANG_CHINESE_MACAU = 0x05
        SUBLANG_CORSICAN_FRANCE = 0x01
        SUBLANG_CZECH_CZECH_REPUBLIC = 0x01
        SUBLANG_CROATIAN_CROATIA = 0x01
        SUBLANG_CROATIAN_BOSNIA_HERZEGOVINA_LATIN = 0x04
        SUBLANG_DANISH_DENMARK = 0x01
        SUBLANG_DARI_AFGHANISTAN = 0x01
        SUBLANG_DIVEHI_MALDIVES = 0x01
        SUBLANG_DUTCH = 0x01
        SUBLANG_DUTCH_BELGIAN = 0x02
        SUBLANG_ENGLISH_US = 0x01
        SUBLANG_ENGLISH_UK = 0x02
        SUBLANG_ENGLISH_AUS = 0x03
        SUBLANG_ENGLISH_CAN = 0x04
        SUBLANG_ENGLISH_NZ = 0x05
        SUBLANG_ENGLISH_EIRE = 0x06
        SUBLANG_ENGLISH_SOUTH_AFRICA = 0x07
        SUBLANG_ENGLISH_JAMAICA = 0x08
        SUBLANG_ENGLISH_CARIBBEAN = 0x09
        SUBLANG_ENGLISH_BELIZE = 0x0a
        SUBLANG_ENGLISH_TRINIDAD = 0x0b
        SUBLANG_ENGLISH_ZIMBABWE = 0x0c
        SUBLANG_ENGLISH_PHILIPPINES = 0x0d
        SUBLANG_ENGLISH_INDIA = 0x10
        SUBLANG_ENGLISH_MALAYSIA = 0x11
        SUBLANG_ENGLISH_SINGAPORE = 0x12
        SUBLANG_ESTONIAN_ESTONIA = 0x01
        SUBLANG_FAEROESE_FAROE_ISLANDS = 0x01
        SUBLANG_FILIPINO_PHILIPPINES = 0x01
        SUBLANG_FINNISH_FINLAND = 0x01
        SUBLANG_FRENCH = 0x01
        SUBLANG_FRENCH_BELGIAN = 0x02
        SUBLANG_FRENCH_CANADIAN = 0x03
        SUBLANG_FRENCH_SWISS = 0x04
        SUBLANG_FRENCH_LUXEMBOURG = 0x05
        SUBLANG_FRENCH_MONACO = 0x06
        SUBLANG_FRISIAN_NETHERLANDS = 0x01
        SUBLANG_FULAH_SENEGAL = 0x02
        SUBLANG_GALICIAN_GALICIAN = 0x01
        SUBLANG_GEORGIAN_GEORGIA = 0x01
        SUBLANG_GERMAN = 0x01
        SUBLANG_GERMAN_SWISS = 0x02
        SUBLANG_GERMAN_AUSTRIAN = 0x03
        SUBLANG_GERMAN_LUXEMBOURG = 0x04
        SUBLANG_GERMAN_LIECHTENSTEIN = 0x05
        SUBLANG_GREEK_GREECE = 0x01
        SUBLANG_GREENLANDIC_GREENLAND = 0x01
        SUBLANG_GUJARATI_INDIA = 0x01
        SUBLANG_HAUSA_NIGERIA_LATIN = 0x01
        SUBLANG_HAWAIIAN_US = 0x01
        SUBLANG_HEBREW_ISRAEL = 0x01
        SUBLANG_HINDI_INDIA = 0x01
        SUBLANG_HUNGARIAN_HUNGARY = 0x01
        SUBLANG_ICELANDIC_ICELAND = 0x01
        SUBLANG_IGBO_NIGERIA = 0x01
        SUBLANG_INDONESIAN_INDONESIA = 0x01
        SUBLANG_INUKTITUT_CANADA = 0x01
        SUBLANG_INUKTITUT_CANADA_LATIN = 0x02
        SUBLANG_IRISH_IRELAND = 0x02
        SUBLANG_ITALIAN = 0x01
        SUBLANG_ITALIAN_SWISS = 0x02
        SUBLANG_JAPANESE_JAPAN = 0x01
        SUBLANG_KANNADA_INDIA = 0x01
        SUBLANG_KASHMIRI_SASIA = 0x02
        SUBLANG_KASHMIRI_INDIA = 0x02
        SUBLANG_KAZAK_KAZAKHSTAN = 0x01
        SUBLANG_KHMER_CAMBODIA = 0x01
        SUBLANG_KICHE_GUATEMALA = 0x01
        SUBLANG_KINYARWANDA_RWANDA = 0x01
        SUBLANG_KONKANI_INDIA = 0x01
        SUBLANG_KOREAN = 0x01
        SUBLANG_KYRGYZ_KYRGYZSTAN = 0x01
        SUBLANG_LAO_LAO = 0x01
        SUBLANG_LATVIAN_LATVIA = 0x01
        SUBLANG_LITHUANIAN = 0x01
        SUBLANG_LOWER_SORBIAN_GERMANY = 0x02
        SUBLANG_LUXEMBOURGISH_LUXEMBOURG = 0x01
        SUBLANG_MACEDONIAN_MACEDONIA = 0x01
        SUBLANG_MALAY_MALAYSIA = 0x01
        SUBLANG_MALAY_BRUNEI_DARUSSALAM = 0x02
        SUBLANG_MALAYALAM_INDIA = 0x01
        SUBLANG_MALTESE_MALTA = 0x01
        SUBLANG_MAORI_NEW_ZEALAND = 0x01
        SUBLANG_MAPUDUNGUN_CHILE = 0x01
        SUBLANG_MARATHI_INDIA = 0x01
        SUBLANG_MOHAWK_MOHAWK = 0x01
        SUBLANG_MONGOLIAN_CYRILLIC_MONGOLIA = 0x01
        SUBLANG_MONGOLIAN_PRC = 0x02
        SUBLANG_NEPALI_INDIA = 0x02
        SUBLANG_NEPALI_NEPAL = 0x01
        SUBLANG_NORWEGIAN_BOKMAL = 0x01
        SUBLANG_NORWEGIAN_NYNORSK = 0x02
        SUBLANG_OCCITAN_FRANCE = 0x01
        SUBLANG_ODIA_INDIA = 0x01
        SUBLANG_ORIYA_INDIA = 0x01
        SUBLANG_PASHTO_AFGHANISTAN = 0x01
        SUBLANG_PERSIAN_IRAN = 0x01
        SUBLANG_POLISH_POLAND = 0x01
        SUBLANG_PORTUGUESE = 0x02
        SUBLANG_PORTUGUESE_BRAZILIAN = 0x01
        SUBLANG_PULAR_SENEGAL = 0x02
        SUBLANG_PUNJABI_INDIA = 0x01
        SUBLANG_PUNJABI_PAKISTAN = 0x02
        SUBLANG_QUECHUA_BOLIVIA = 0x01
        SUBLANG_QUECHUA_ECUADOR = 0x02
        SUBLANG_QUECHUA_PERU = 0x03
        SUBLANG_ROMANIAN_ROMANIA = 0x01
        SUBLANG_ROMANSH_SWITZERLAND = 0x01
        SUBLANG_RUSSIAN_RUSSIA = 0x01
        SUBLANG_SAKHA_RUSSIA = 0x01
        SUBLANG_SAMI_NORTHERN_NORWAY = 0x01
        SUBLANG_SAMI_NORTHERN_SWEDEN = 0x02
        SUBLANG_SAMI_NORTHERN_FINLAND = 0x03
        SUBLANG_SAMI_LULE_NORWAY = 0x04
        SUBLANG_SAMI_LULE_SWEDEN = 0x05
        SUBLANG_SAMI_SOUTHERN_NORWAY = 0x06
        SUBLANG_SAMI_SOUTHERN_SWEDEN = 0x07
        SUBLANG_SAMI_SKOLT_FINLAND = 0x08
        SUBLANG_SAMI_INARI_FINLAND = 0x09
        SUBLANG_SANSKRIT_INDIA = 0x01
        SUBLANG_SCOTTISH_GAELIC = 0x01
        SUBLANG_SERBIAN_BOSNIA_HERZEGOVINA_LATIN = 0x06
        SUBLANG_SERBIAN_BOSNIA_HERZEGOVINA_CYRILLIC = 0x07
        SUBLANG_SERBIAN_MONTENEGRO_LATIN = 0x0b
        SUBLANG_SERBIAN_MONTENEGRO_CYRILLIC = 0x0c
        SUBLANG_SERBIAN_SERBIA_LATIN = 0x09
        SUBLANG_SERBIAN_SERBIA_CYRILLIC = 0x0a
        SUBLANG_SERBIAN_CROATIA = 0x01
        SUBLANG_SERBIAN_LATIN = 0x02
        SUBLANG_SERBIAN_CYRILLIC = 0x03
        SUBLANG_SINDHI_INDIA = 0x01
        SUBLANG_SINDHI_PAKISTAN = 0x02
        SUBLANG_SINDHI_AFGHANISTAN = 0x02
        SUBLANG_SINHALESE_SRI_LANKA = 0x01
        SUBLANG_SOTHO_NORTHERN_SOUTH_AFRICA = 0x01
        SUBLANG_SLOVAK_SLOVAKIA = 0x01
        SUBLANG_SLOVENIAN_SLOVENIA = 0x01
        SUBLANG_SPANISH = 0x01
        SUBLANG_SPANISH_MEXICAN = 0x02
        SUBLANG_SPANISH_MODERN = 0x03
        SUBLANG_SPANISH_GUATEMALA = 0x04
        SUBLANG_SPANISH_COSTA_RICA = 0x05
        SUBLANG_SPANISH_PANAMA = 0x06
        SUBLANG_SPANISH_DOMINICAN_REPUBLIC = 0x07
        SUBLANG_SPANISH_VENEZUELA = 0x08
        SUBLANG_SPANISH_COLOMBIA = 0x09
        SUBLANG_SPANISH_PERU = 0x0a
        SUBLANG_SPANISH_ARGENTINA = 0x0b
        SUBLANG_SPANISH_ECUADOR = 0x0c
        SUBLANG_SPANISH_CHILE = 0x0d
        SUBLANG_SPANISH_URUGUAY = 0x0e
        SUBLANG_SPANISH_PARAGUAY = 0x0f
        SUBLANG_SPANISH_BOLIVIA = 0x10
        SUBLANG_SPANISH_EL_SALVADOR = 0x11
        SUBLANG_SPANISH_HONDURAS = 0x12
        SUBLANG_SPANISH_NICARAGUA = 0x13
        SUBLANG_SPANISH_PUERTO_RICO = 0x14
        SUBLANG_SPANISH_US = 0x15
        SUBLANG_SWAHILI_KENYA = 0x01
        SUBLANG_SWEDISH = 0x01
        SUBLANG_SWEDISH_FINLAND = 0x02
        SUBLANG_SYRIAC_SYRIA = 0x01
        SUBLANG_TAJIK_TAJIKISTAN = 0x01
        SUBLANG_TAMAZIGHT_ALGERIA_LATIN = 0x02
        SUBLANG_TAMAZIGHT_MOROCCO_TIFINAGH = 0x04
        SUBLANG_TAMIL_INDIA = 0x01
        SUBLANG_TAMIL_SRI_LANKA = 0x02
        SUBLANG_TATAR_RUSSIA = 0x01
        SUBLANG_TELUGU_INDIA = 0x01
        SUBLANG_THAI_THAILAND = 0x01
        SUBLANG_TIBETAN_PRC = 0x01
        SUBLANG_TIGRIGNA_ERITREA = 0x02
        SUBLANG_TIGRINYA_ERITREA = 0x02
        SUBLANG_TIGRINYA_ETHIOPIA = 0x01
        SUBLANG_TSWANA_BOTSWANA = 0x02
        SUBLANG_TSWANA_SOUTH_AFRICA = 0x01
        SUBLANG_TURKISH_TURKEY = 0x01
        SUBLANG_TURKMEN_TURKMENISTAN = 0x01
        SUBLANG_UIGHUR_PRC = 0x01
        SUBLANG_UKRAINIAN_UKRAINE = 0x01
        SUBLANG_UPPER_SORBIAN_GERMANY = 0x01
        SUBLANG_URDU_PAKISTAN = 0x01
        SUBLANG_URDU_INDIA = 0x02
        SUBLANG_UZBEK_LATIN = 0x01
        SUBLANG_UZBEK_CYRILLIC = 0x02
        SUBLANG_VALENCIAN_VALENCIA = 0x02
        SUBLANG_VIETNAMESE_VIETNAM = 0x01
        SUBLANG_WELSH_UNITED_KINGDOM = 0x01
        SUBLANG_WOLOF_SENEGAL = 0x01
        SUBLANG_XHOSA_SOUTH_AFRICA = 0x01
        SUBLANG_YAKUT_RUSSIA = 0x01
        SUBLANG_YI_PRC = 0x01
        SUBLANG_YORUBA_NIGERIA = 0x01
        SUBLANG_ZULU_SOUTH_AFRICA = 0x01
        SORT_DEFAULT = 0x0
        SORT_INVARIANT_MATH = 0x1
        SORT_JAPANESE_XJIS = 0x0
        SORT_JAPANESE_UNICODE = 0x1
        SORT_JAPANESE_RADICALSTROKE = 0x4
        SORT_CHINESE_BIG5 = 0x0
        SORT_CHINESE_PRCP = 0x0
        SORT_CHINESE_UNICODE = 0x1
        SORT_CHINESE_PRC = 0x2
        SORT_CHINESE_BOPOMOFO = 0x3
        SORT_CHINESE_RADICALSTROKE = 0x4
        SORT_KOREAN_KSC = 0x0
        SORT_KOREAN_UNICODE = 0x1
        SORT_GERMAN_PHONE_BOOK = 0x1
        SORT_HUNGARIAN_DEFAULT = 0x0
        SORT_HUNGARIAN_TECHNICAL = 0x1
        SORT_GEORGIAN_TRADITIONAL = 0x0
        SORT_GEORGIAN_MODERN = 0x1
        
        MAKELANGID = lambda p, s: (WORD(s).value << 10) | WORD(p).value
        PRIMARYLANGID = lambda lgid: (WORD(lgid).value & 0x3ff)
        SUBLANGID = lambda lgid: (WORD(lgid) >> 10)

        NLS_VALID_LOCALE_MASK = 0x000fffff

        MAKELCID = lambda lgid, srtid: DWORD((DWORD(WORD(srtid).value).value << 16) | DWORD(WORD(lgid).value).value).value
        MAKESORTLCID = lambda lgid, srtid, ver: (DWORD((MAKELCID(lgid, srtid)) | (DWORD(WORD(ver).value).value << 20))).value
        LANGIDFROMLCID = lambda lcid: WORD(lcid).value
        SORTIDFROMLCID = lambda lcid: (WORD(DWORD(lcid).value >> 16) & 0xF).value
        SORTVERSIONFROMLCID = lambda lcid: (WORD((DWORD(lcid).value >> 20) & 0xF)).value
        
        LOCALE_NAME_MAX_LENGTH = 85
        
        LANG_SYSTEM_DEFAULT = (MAKELANGID(LANG_NEUTRAL, SUBLANG_SYS_DEFAULT))
        LANG_USER_DEFAULT = (MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT))

        LOCALE_SYSTEM_DEFAULT = (MAKELCID(LANG_SYSTEM_DEFAULT, SORT_DEFAULT))
        LOCALE_USER_DEFAULT = (MAKELCID(LANG_USER_DEFAULT, SORT_DEFAULT))

        LOCALE_CUSTOM_DEFAULT = (MAKELCID(MAKELANGID(LANG_NEUTRAL, SUBLANG_CUSTOM_DEFAULT), SORT_DEFAULT))

        LOCALE_CUSTOM_UNSPECIFIED = (MAKELCID(MAKELANGID(LANG_NEUTRAL, SUBLANG_CUSTOM_UNSPECIFIED), SORT_DEFAULT))

        LOCALE_CUSTOM_UI_DEFAULT = (MAKELCID(MAKELANGID(LANG_NEUTRAL, SUBLANG_UI_CUSTOM_DEFAULT), SORT_DEFAULT))

        LOCALE_NEUTRAL = (MAKELCID(MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL), SORT_DEFAULT))

        LOCALE_INVARIANT = (MAKELCID(MAKELANGID(LANG_INVARIANT, SUBLANG_NEUTRAL), SORT_DEFAULT))
        
        LOCALE_TRANSIENT_KEYBOARD1 = 0x2000
        LOCALE_TRANSIENT_KEYBOARD2 = 0x2400
        LOCALE_TRANSIENT_KEYBOARD3 = 0x2800
        LOCALE_TRANSIENT_KEYBOARD4 = 0x2c00
        
        LOCALE_UNASSIGNED_LCID = LOCALE_CUSTOM_UNSPECIFIED
        
        if cpreproc.ifndef("UMDF_USING_NTSTATUS"):
            if cpreproc.ifndef("WIN32_NO_STATUS"):
                STATUS_WAIT_0 = NTSTATUS(0x00000000).value
                STATUS_ABANDONED_WAIT_0 = NTSTATUS(0x00000080).value
                STATUS_USER_APC = NTSTATUS(0x000000C0).value
                STATUS_TIMEOUT = NTSTATUS(0x00000102).value
                STATUS_PENDING = NTSTATUS(0x00000103).value
                DBG_EXCEPTION_HANDLED = NTSTATUS(0x00010001).value
                DBG_CONTINUE = NTSTATUS(0x00010002).value
                STATUS_SEGMENT_NOTIFICATION = NTSTATUS(0x40000005).value
                STATUS_FATAL_APP_EXIT = NTSTATUS(0x40000015).value
                DBG_REPLY_LATER = NTSTATUS(0x40010001).value
                DBG_TERMINATE_THREAD = NTSTATUS(0x40010003).value
                DBG_TERMINATE_PROCESS = NTSTATUS(0x40010004).value
                DBG_CONTROL_C = NTSTATUS(0x40010005).value
                DBG_PRINTEXCEPTION_C = NTSTATUS(0x40010006).value
                DBG_RIPEXCEPTION = NTSTATUS(0x40010007).value
                DBG_CONTROL_BREAK = NTSTATUS(0x40010008).value
                DBG_COMMAND_EXCEPTION = NTSTATUS(0x40010009).value
                DBG_PRINTEXCEPTION_WIDE_C = NTSTATUS(0x4001000A).value
                STATUS_GUARD_PAGE_VIOLATION = NTSTATUS(0x80000001).value
                STATUS_DATATYPE_MISALIGNMENT = NTSTATUS(0x80000002).value
                STATUS_BREAKPOINT = NTSTATUS(0x80000003).value
                STATUS_SINGLE_STEP = NTSTATUS(0x80000004).value
                STATUS_LONGJUMP = NTSTATUS(0x80000026).value
                STATUS_UNWIND_CONSOLIDATE = NTSTATUS(0x80000029).value
                DBG_EXCEPTION_NOT_HANDLED = NTSTATUS(0x80010001).value
                STATUS_ACCESS_VIOLATION = NTSTATUS(0xC0000005).value
                STATUS_IN_PAGE_ERROR = NTSTATUS(0xC0000006).value
                STATUS_INVALID_HANDLE = NTSTATUS(0xC0000008).value
                STATUS_INVALID_PARAMETER = NTSTATUS(0xC000000D).value
                STATUS_NO_MEMORY = NTSTATUS(0xC0000017).value
                STATUS_ILLEGAL_INSTRUCTION = NTSTATUS(0xC000001D).value
                STATUS_NONCONTINUABLE_EXCEPTION = NTSTATUS(0xC0000025).value
                STATUS_INVALID_DISPOSITION = NTSTATUS(0xC0000026).value
                STATUS_ARRAY_BOUNDS_EXCEEDED = NTSTATUS(0xC000008C).value
                STATUS_FLOAT_DENORMAL_OPERAND = NTSTATUS(0xC000008D).value
                STATUS_FLOAT_DIVIDE_BY_ZERO = NTSTATUS(0xC000008E).value
                STATUS_FLOAT_INEXACT_RESULT = NTSTATUS(0xC000008F).value
                STATUS_FLOAT_INVALID_OPERATION = NTSTATUS(0xC0000090).value
                STATUS_FLOAT_OVERFLOW = NTSTATUS(0xC0000091).value
                STATUS_FLOAT_STACK_CHECK = NTSTATUS(0xC0000092).value
                STATUS_FLOAT_UNDERFLOW = NTSTATUS(0xC0000093).value
                STATUS_INTEGER_DIVIDE_BY_ZERO = NTSTATUS(0xC0000094).value
                STATUS_INTEGER_OVERFLOW = NTSTATUS(0xC0000095).value
                STATUS_PRIVILEGED_INSTRUCTION = NTSTATUS(0xC0000096).value
                STATUS_STACK_OVERFLOW = NTSTATUS(0xC00000FD).value
                STATUS_DLL_NOT_FOUND = NTSTATUS(0xC0000135).value
                STATUS_ORDINAL_NOT_FOUND = NTSTATUS(0xC0000138).value
                STATUS_ENTRYPOINT_NOT_FOUND = NTSTATUS(0xC0000139).value
                STATUS_CONTROL_C_EXIT = NTSTATUS(0xC000013A).value
                STATUS_DLL_INIT_FAILED = NTSTATUS(0xC0000142).value
                STATUS_CONTROL_STACK_VIOLATION = NTSTATUS(0xC00001B2).value
                STATUS_FLOAT_MULTIPLE_FAULTS = NTSTATUS(0xC00002B4).value
                STATUS_FLOAT_MULTIPLE_TRAPS = NTSTATUS(0xC00002B5).value
                STATUS_REG_NAT_CONSUMPTION = NTSTATUS(0xC00002C9).value
                STATUS_HEAP_CORRUPTION = NTSTATUS(0xC0000374).value
                STATUS_STACK_BUFFER_OVERRUN = NTSTATUS(0xC0000409).value
                STATUS_INVALID_CRUNTIME_PARAMETER = NTSTATUS(0xC0000417).value
                STATUS_ASSERTION_FAILURE = NTSTATUS(0xC0000420).value
                STATUS_ENCLAVE_VIOLATION = NTSTATUS(0xC00004A2).value
                STATUS_INTERRUPTED = NTSTATUS(0xC0000515).value
                STATUS_THREAD_NOT_RUNNING = NTSTATUS(0xC0000516).value
                STATUS_ALREADY_REGISTERED = NTSTATUS(0xC0000718).value
                STATUS_SXS_EARLY_DEACTIVATION = NTSTATUS(0xC015000F).value
                STATUS_SXS_INVALID_DEACTIVATION = NTSTATUS(0xC0150010).value
                MAXIMUM_WAIT_OBJECTS = 64
                MAXIMUM_SUSPEND_COUNT = MAXCHAR
                
        KSPIN_LOCK = ULONG_PTR
        PKSPIN_LOCK = PULONG_PTR
        
        KIRQL = UCHAR
        PKIRQL = PUCHAR
        
        _NT_PRODUCT_TYPE = INT
        if True:
            NtProductWinNt = 1
            NtProductLanManNt = 2
            NtProductServer = 3
        
        NT_PRODUCT_TYPE = _NT_PRODUCT_TYPE
        PNT_PRODUCT_TYPE = POINTER(NT_PRODUCT_TYPE)

        _SUITE_TYPE = INT
        if True:
            SmallBusiness = 0
            Enterprise = 1
            BackOffice = 2
            CommunicationServer = 3
            TerminalServer = 4
            SmallBusinessRestricted = 5
            EmbeddedNT = 6
            DataCenter = 7
            SingleUserTS = 8
            Personal = 9
            Blade = 10
            EmbeddedRestricted = 11
            SecurityAppliance = 12
            StorageServer = 13
            ComputeServer = 14
            WHServer = 15
            PhoneNT = 16
            MultiUserTS = 17
            MaxSuiteType = 18
            
        SUITE_TYPE = _SUITE_TYPE
        
        class _XSAVE_FORMAT(CStructure):
            _fields_ = [
                ("ControlWord", WORD),
                ("StatusWord", WORD),
                ("TagWord", BYTE),
                ("Reserved1", BYTE),
                ("ErrorOpcode", WORD),
                ("ErrorOffset", DWORD),
                ("ErrorSelector", WORD),
                ("Reserved2", WORD),
                ("DataOffset", DWORD),
                ("DataSelector", WORD),
                ("Reserved3", WORD),
                ("MxCsr", DWORD),
                ("MxCsr_Mask", DWORD),
                ("FloatRegisters", M128A * 8),
                ("XmmRegisters", M128A * 16),
                ("Reserved4", BYTE * 96),
                ("XmmRegisters", M128A * 8),
                ("Reserved4", BYTE * 224)
            ]
        XSAVE_FORMAT = _XSAVE_FORMAT
        PXSAVE_FORMAT = POINTER(XSAVE_FORMAT)
        
        class _XSAVE_CET_U_FORMAT(CStructure):
            _fields_ = [
                ("Ia32CetUMsr", DWORD64),
                ("Ia32Pl3SspMsr", DWORD64)
            ]
            
        XSAVE_CET_U_FORMAT = _XSAVE_CET_U_FORMAT
        PXSAVE_CET_U_FORMAT = POINTER(XSAVE_CET_U_FORMAT)
            
        class XSAVE_ARM64_SVE_HEADER(CStructure):
            _fields_ = [
                ("VectorLength", DWORD),
                ("VectorRegisterOffset", DWORD),
                ("PredicateRegisterOffset", DWORD),
                ("Reserved", DWORD * 5)
            ]
        
        PXSAVE_ARM64_SVE_HEADER = POINTER(XSAVE_ARM64_SVE_HEADER)
            
        class _XSAVE_AREA_HEADER(CStructure):
            _pack_ = 8
            _fields_ = [
                ("Mask", DWORD64),
                ("CompactionMask", DWORD64),
                ("Reserved2", DWORD64 * 6)
            ]
            
        XSAVE_AREA_HEADER = _XSAVE_AREA_HEADER
        PXSAVE_AREA_HEADER = POINTER(XSAVE_AREA_HEADER)
            
        class _XSAVE_AREA(CStructure):
            _pack_ = 16
            _fields_ = [
                ("LegacyState", XSAVE_FORMAT),
                ("Header", XSAVE_AREA_HEADER)
            ]
            
        XSAVE_AREA = _XSAVE_AREA
        PXSAVE_AREA = POINTER(XSAVE_AREA)
        
        class _XSTATE_CONTEXT(CStructure):
            _fields_ = [
                ("Mask", DWORD64),
                ("Length", DWORD),
                ("Reserved1", DWORD),
                ("Area", PXSAVE_AREA),
                ("Reserved2", DWORD),
                ("Buffer", LPVOID),
                ("Reserved3", DWORD)
            ]
            
        XSTATE_CONTEXT = _XSTATE_CONTEXT
        PXSTATE_CONTEXT = POINTER(XSTATE_CONTEXT)
        
        class _SCOPERECORD(CStructure):
            _fields_ = [
                ("BeginAddress", DWORD),
                ("EndAddress", DWORD),
                ("HandlerAddress", DWORD),
                ("JumpTarget", DWORD)
            ]
            
        class _SCOPE_TABLE_AMD64(CStructure):
            _fields_ = [
                ("Count", DWORD),
                ("ScopeRecord", _SCOPERECORD * 1)
            ]
            
        SCOPE_TABLE_AMD64 = _SCOPE_TABLE_AMD64
        PSCOPE_TABLE_AMD64 = POINTER(SCOPE_TABLE_AMD64)
        
        EXCEPTION_READ_FAULT = 0
        EXCEPTION_WRITE_FAULT = 1
        EXCEPTION_EXECUTE_FAULT = 8
        
        CONTEXT_AMD64 = 0x00100000
        CONTEXT_CONTROL = (CONTEXT_AMD64 | 0x00000001)
        CONTEXT_INTEGER = (CONTEXT_AMD64 | 0x00000002)
        CONTEXT_SEGMENTS = (CONTEXT_AMD64 | 0x00000004)
        CONTEXT_FLOATING_POINT = (CONTEXT_AMD64 | 0x00000008)
        CONTEXT_DEBUG_REGISTERS = (CONTEXT_AMD64 | 0x00000010)
        CONTEXT_FULL = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_FLOATING_POINT)
        CONTEXT_ALL = (CONTEXT_CONTROL | CONTEXT_INTEGER | CONTEXT_SEGMENTS | CONTEXT_FLOATING_POINT | CONTEXT_DEBUG_REGISTERS)
        CONTEXT_XSTATE = (CONTEXT_AMD64 | 0x00000040)
        CONTEXT_KERNEL_DEBUGGER = 0x04000000
        CONTEXT_EXCEPTION_ACTIVE = 0x08000000
        CONTEXT_SERVICE_ACTIVE = 0x10000000
        CONTEXT_EXCEPTION_REQUEST = 0x40000000
        CONTEXT_EXCEPTION_REPORTING = 0x80000000
        
        INITIAL_MXCSR = 0x1f80
        INITIAL_FPCSR = 0x027f
        
        XMM_SAVE_AREA32 = XSAVE_FORMAT
        PXMM_SAVE_AREA32 = PXSAVE_FORMAT
        
        RUNTIME_FUNCTION_INDIRECT = 0x1
        UNW_FLAG_NHANDLER = 0x0
        UNW_FLAG_EHANDLER = 0x1
        UNW_FLAG_UHANDLER = 0x2
        UNW_FLAG_CHAININFO = 0x4
        UNW_FLAG_NO_EPILOGUE = 0x80000000
        UNWIND_CHAIN_LIMIT = 32
        UNWIND_HISTORY_TABLE_SIZE = 12
        
        _MM_HINT_T0 = 1
        _MM_HINT_T1 = 2
        _MM_HINT_T2 = 3
        _MM_HINT_NTA = 0
        PF_TEMPORAL_LEVEL_1 = _MM_HINT_T0
        PF_TEMPORAL_LEVEL_2 = _MM_HINT_T1
        PF_TEMPORAL_LEVEL_3 = _MM_HINT_T2
        PF_NON_TEMPORAL_LEVEL_ALL = _MM_HINT_NTA
        
        EXCEPTION_READ_FAULT = 0
        EXCEPTION_WRITE_FAULT = 1
        EXCEPTION_EXECUTE_FAULT = 8
        
        PACCESS_TOKEN = PVOID
        PSECURITY_DESCRIPTOR = PVOID
        PSID = PVOID
        PCLAIMS_BLOB = PVOID
        
        ACCESS_MASK = DWORD
        PACCESS_MASK = PDWORD

        SECURITY_INFORMATION = DWORD
        PSECURITY_INFORMATION = PDWORD
        
        DELETE = (0x00010000)
        READ_CONTROL = (0x00020000)
        WRITE_DAC = (0x00040000)
        WRITE_OWNER = (0x00080000)
        SYNCHRONIZE = (0x00100000)
        STANDARD_RIGHTS_REQUIRED = (0x000F0000)
        STANDARD_RIGHTS_READ = (READ_CONTROL)
        STANDARD_RIGHTS_WRITE = (READ_CONTROL)
        STANDARD_RIGHTS_EXECUTE = (READ_CONTROL)
        STANDARD_RIGHTS_ALL = (0x001F0000)
        SPECIFIC_RIGHTS_ALL = (0x0000FFFF)
        ACCESS_SYSTEM_SECURITY = (0x01000000)
        MAXIMUM_ALLOWED = (0x02000000)
        GENERIC_READ = (0x80000000)
        GENERIC_WRITE = (0x40000000)
        GENERIC_EXECUTE = (0x20000000)
        GENERIC_ALL = (0x10000000)
        
        class _GENERIC_MAPPING(CStructure):
            _fields_ = [
                ("GenericRead", ACCESS_MASK),
                ("GenericWrite", ACCESS_MASK),
                ("GenericExecute", ACCESS_MASK),
                ("GenericAll", ACCESS_MASK),
            ]
            
        GENERIC_MAPPING = _GENERIC_MAPPING
        PGENERIC_MAPPING = POINTER(GENERIC_MAPPING)
        
        class _LUID_AND_ATTRIBUTES(CStructure):
            _fields_ = [
                ("Luid", LUID),
                ("Attributes", DWORD)
            ]
        
        LUID_AND_ATTRIBUTES = _LUID_AND_ATTRIBUTES
        PLUID_AND_ATTRIBUTES = POINTER(LUID_AND_ATTRIBUTES)
        LUID_AND_ATTRIBUTES_ARRAY = PLUID_AND_ATTRIBUTES
        PLUID_AND_ATTRIBUTES_ARRAY = POINTER(LUID_AND_ATTRIBUTES_ARRAY)
        
        if cpreproc.pragma_once("SID_IDENTIFIER_AUTHORITY_DEFINED"):
            class _SID_IDENTIFIER_AUTHORITY(CStructure):
                _fields_ = [
                    ("Value", BYTE * 6)
                ]
            SID_IDENTIFIER_AUTHORITY = _SID_IDENTIFIER_AUTHORITY
            PSID_IDENTIFIER_AUTHORITY = POINTER(SID_IDENTIFIER_AUTHORITY)

        if cpreproc.pragma_once("SID_DEFINED"):
            class _SID(CStructure):
                _fields_ = [
                    ("Revision", BYTE),
                    ("SubAuthorityCount", BYTE),
                    ("IdentifierAuthority", SID_IDENTIFIER_AUTHORITY),
                    ("SubAuthority", PDWORD)
                ]
            SID = _SID
            PISID = POINTER(SID)

        SID_REVISION = (1)
        SID_MAX_SUB_AUTHORITIES = 15
        SID_RECOMMENDED_SUB_AUTHORITIES = 1
        
        SECURITY_MAX_SID_SIZE = (sizeof(SID) - sizeof(DWORD) + (SID_MAX_SUB_AUTHORITIES * sizeof(DWORD)))
        SECURITY_SID_SIZE = lambda SubAuthorityCount_: (sizeof(SID) - sizeof(DWORD) + (SubAuthorityCount_) * sizeof(DWORD))
        
        class _SE_SID(Union):
            _fields_ = [
                ("Sid", SID),
                ("Buffer", BYTE * SECURITY_MAX_SID_SIZE)
            ]
        SE_SID = _SE_SID
        PSE_SID = POINTER(SE_SID)

        _SID_NAME_USE = INT
        if True:
            SidTypeUser = 1
            SidTypeGroup = 2
            SidTypeDomain = 3
            SidTypeAlias = 4
            SidTypeWellKnownGroup = 5
            SidTypeDeletedAccount = 6
            SidTypeInvalid = 7
            SidTypeUnknown = 8
            SidTypeComputer = 9
            SidTypeLabel = 10
            SidTypeLogonSession = 11
        SID_NAME_USE = _SID_NAME_USE
        PSID_NAME_USE = POINTER(SID_NAME_USE)

        class _SID_AND_ATTRIBUTES(CStructure):
            _fields_ = [
                ("Sid", PISID),
                ("Attributes", DWORD)
            ]
        
        SID_AND_ATTRIBUTES = _SID_AND_ATTRIBUTES
        PSID_AND_ATTRIBUTES = POINTER(SID_AND_ATTRIBUTES)

        SID_AND_ATTRIBUTES_ARRAY = PSID_AND_ATTRIBUTES
        PSID_AND_ATTRIBUTES_ARRAY = POINTER(SID_AND_ATTRIBUTES_ARRAY)

        SID_HASH_SIZE = 32
        
        SID_HASH_ENTRY = ULONG_PTR
        PSID_HASH_ENTRY = PULONG_PTR

        class _SID_AND_ATTRIBUTES_HASH(CStructure):
            _fields_ = [
                ("SidCount", DWORD),
                ("SidAttr", PSID_AND_ATTRIBUTES),
                ("Hash", SID_HASH_ENTRY * SID_HASH_SIZE)
            ]
        SID_AND_ATTRIBUTES_HASH = _SID_AND_ATTRIBUTES_HASH
        PSID_AND_ATTRIBUTES_HASH = POINTER(SID_AND_ATTRIBUTES_HASH)
        
        SECURITY_NULL_SID_AUTHORITY = 0,0,0,0,0,0
        SECURITY_WORLD_SID_AUTHORITY = 0,0,0,0,0,1
        SECURITY_LOCAL_SID_AUTHORITY = 0,0,0,0,0,2
        SECURITY_CREATOR_SID_AUTHORITY = 0,0,0,0,0,3
        SECURITY_NON_UNIQUE_AUTHORITY = 0,0,0,0,0,4
        SECURITY_RESOURCE_MANAGER_AUTHORITY = 0,0,0,0,0,9
        SECURITY_NULL_RID = (0x00000000)
        SECURITY_WORLD_RID = (0x00000000)
        SECURITY_LOCAL_RID = (0x00000000)
        SECURITY_LOCAL_LOGON_RID = (0x00000001)
        SECURITY_CREATOR_OWNER_RID = (0x00000000)
        SECURITY_CREATOR_GROUP_RID = (0x00000001)
        SECURITY_CREATOR_OWNER_SERVER_RID = (0x00000002)
        SECURITY_CREATOR_GROUP_SERVER_RID = (0x00000003)
        SECURITY_CREATOR_OWNER_RIGHTS_RID = (0x00000004)
        
        SECURITY_NT_AUTHORITY = 0,0,0,0,0,5
        SECURITY_DIALUP_RID = (0x00000001)
        SECURITY_NETWORK_RID = (0x00000002)
        SECURITY_BATCH_RID = (0x00000003)
        SECURITY_INTERACTIVE_RID = (0x00000004)
        SECURITY_LOGON_IDS_RID = (0x00000005)
        SECURITY_LOGON_IDS_RID_COUNT = (3)
        SECURITY_SERVICE_RID = (0x00000006)
        SECURITY_ANONYMOUS_LOGON_RID = (0x00000007)
        SECURITY_PROXY_RID = (0x00000008)
        SECURITY_ENTERPRISE_CONTROLLERS_RID = (0x00000009)
        SECURITY_SERVER_LOGON_RID = SECURITY_ENTERPRISE_CONTROLLERS_RID
        SECURITY_PRINCIPAL_SELF_RID = (0x0000000A)
        SECURITY_AUTHENTICATED_USER_RID = (0x0000000B)
        SECURITY_RESTRICTED_CODE_RID = (0x0000000C)
        SECURITY_TERMINAL_SERVER_RID = (0x0000000D)
        SECURITY_REMOTE_LOGON_RID = (0x0000000E)
        SECURITY_THIS_ORGANIZATION_RID = (0x0000000F)
        SECURITY_IUSER_RID = (0x00000011)
        SECURITY_LOCAL_SYSTEM_RID = (0x00000012)
        SECURITY_LOCAL_SERVICE_RID = (0x00000013)
        SECURITY_NETWORK_SERVICE_RID = (0x00000014)
        SECURITY_NT_NON_UNIQUE = (0x00000015)
        SECURITY_NT_NON_UNIQUE_SUB_AUTH_COUNT = (3)
        SECURITY_ENTERPRISE_READONLY_CONTROLLERS_RID = (0x00000016)
        SECURITY_BUILTIN_DOMAIN_RID = (0x00000020)
        SECURITY_WRITE_RESTRICTED_CODE_RID = (0x00000021)
        SECURITY_PACKAGE_BASE_RID = (0x00000040)
        SECURITY_PACKAGE_RID_COUNT = (2)
        SECURITY_PACKAGE_NTLM_RID = (0x0000000A)
        SECURITY_PACKAGE_SCHANNEL_RID = (0x0000000E)
        SECURITY_PACKAGE_DIGEST_RID = (0x00000015)
        SECURITY_CRED_TYPE_BASE_RID = (0x00000041)
        SECURITY_CRED_TYPE_RID_COUNT = (2)
        SECURITY_CRED_TYPE_THIS_ORG_CERT_RID = (0x00000001)
        SECURITY_MIN_BASE_RID = (0x00000050)
        SECURITY_SERVICE_ID_BASE_RID = (0x00000050)
        SECURITY_SERVICE_ID_RID_COUNT = (6)
        SECURITY_RESERVED_ID_BASE_RID = (0x00000051)
        SECURITY_APPPOOL_ID_BASE_RID = (0x00000052)
        SECURITY_APPPOOL_ID_RID_COUNT = (6)
        SECURITY_VIRTUALSERVER_ID_BASE_RID = (0x00000053)
        SECURITY_VIRTUALSERVER_ID_RID_COUNT = (6)
        SECURITY_USERMODEDRIVERHOST_ID_BASE_RID = (0x00000054)
        SECURITY_USERMODEDRIVERHOST_ID_RID_COUNT = (6)
        SECURITY_CLOUD_INFRASTRUCTURE_SERVICES_ID_BASE_RID = (0x00000055)
        SECURITY_CLOUD_INFRASTRUCTURE_SERVICES_ID_RID_COUNT = (6)
        SECURITY_WMIHOST_ID_BASE_RID = (0x00000056)
        SECURITY_WMIHOST_ID_RID_COUNT = (6)
        SECURITY_TASK_ID_BASE_RID = (0x00000057)
        SECURITY_NFS_ID_BASE_RID = (0x00000058)
        SECURITY_COM_ID_BASE_RID = (0x00000059)
        SECURITY_WINDOW_MANAGER_BASE_RID = (0x0000005A)
        SECURITY_RDV_GFX_BASE_RID = (0x0000005B)
        SECURITY_DASHOST_ID_BASE_RID = (0x0000005C)
        SECURITY_DASHOST_ID_RID_COUNT = (6)
        SECURITY_USERMANAGER_ID_BASE_RID = (0x0000005D)
        SECURITY_USERMANAGER_ID_RID_COUNT = (6)
        SECURITY_WINRM_ID_BASE_RID = (0x0000005E)
        SECURITY_WINRM_ID_RID_COUNT = (6)
        SECURITY_CCG_ID_BASE_RID = (0x0000005F)
        SECURITY_UMFD_BASE_RID = (0x00000060)
        SECURITY_VIRTUALACCOUNT_ID_RID_COUNT = (6)
        SECURITY_MAX_BASE_RID = (0x0000006F)
        SECURITY_MAX_ALWAYS_FILTERED = (0x000003E7)
        SECURITY_MIN_NEVER_FILTERED = (0x000003E8)
        SECURITY_OTHER_ORGANIZATION_RID = (0x000003E8)
        SECURITY_WINDOWSMOBILE_ID_BASE_RID = (0x00000070)
        SECURITY_INSTALLER_GROUP_CAPABILITY_BASE = (0x20)
        SECURITY_INSTALLER_GROUP_CAPABILITY_RID_COUNT = (9)
        SECURITY_INSTALLER_CAPABILITY_RID_COUNT = (10)
        SECURITY_LOCAL_ACCOUNT_RID = (0x00000071)
        SECURITY_LOCAL_ACCOUNT_AND_ADMIN_RID = (0x00000072)
        DOMAIN_GROUP_RID_AUTHORIZATION_DATA_IS_COMPOUNDED = (0x000001F0)
        DOMAIN_GROUP_RID_AUTHORIZATION_DATA_CONTAINS_CLAIMS = (0x000001F1)
        DOMAIN_GROUP_RID_ENTERPRISE_READONLY_DOMAIN_CONTROLLERS = (0x000001F2)
        FOREST_USER_RID_MAX = (0x000001F3)
        DOMAIN_USER_RID_ADMIN = (0x000001F4)
        DOMAIN_USER_RID_GUEST = (0x000001F5)
        DOMAIN_USER_RID_KRBTGT = (0x000001F6)
        DOMAIN_USER_RID_DEFAULT_ACCOUNT = (0x000001F7)
        DOMAIN_USER_RID_WDAG_ACCOUNT = (0x000001F8)
        DOMAIN_USER_RID_MAX = (0x000003E7)
        DOMAIN_GROUP_RID_ADMINS = (0x00000200)
        DOMAIN_GROUP_RID_USERS = (0x00000201)
        DOMAIN_GROUP_RID_GUESTS = (0x00000202)
        DOMAIN_GROUP_RID_COMPUTERS = (0x00000203)
        DOMAIN_GROUP_RID_CONTROLLERS = (0x00000204)
        DOMAIN_GROUP_RID_CERT_ADMINS = (0x00000205)
        DOMAIN_GROUP_RID_SCHEMA_ADMINS = (0x00000206)
        DOMAIN_GROUP_RID_ENTERPRISE_ADMINS = (0x00000207)
        DOMAIN_GROUP_RID_POLICY_ADMINS = (0x00000208)
        DOMAIN_GROUP_RID_READONLY_CONTROLLERS = (0x00000209)
        DOMAIN_GROUP_RID_CLONEABLE_CONTROLLERS = (0x0000020A)
        DOMAIN_GROUP_RID_CDC_RESERVED = (0x0000020C)
        DOMAIN_GROUP_RID_PROTECTED_USERS = (0x0000020D)
        DOMAIN_GROUP_RID_KEY_ADMINS = (0x0000020E)
        DOMAIN_GROUP_RID_ENTERPRISE_KEY_ADMINS = (0x0000020F)
        DOMAIN_ALIAS_RID_ADMINS = (0x00000220)
        DOMAIN_ALIAS_RID_USERS = (0x00000221)
        DOMAIN_ALIAS_RID_GUESTS = (0x00000222)
        DOMAIN_ALIAS_RID_POWER_USERS = (0x00000223)
        DOMAIN_ALIAS_RID_ACCOUNT_OPS = (0x00000224)
        DOMAIN_ALIAS_RID_SYSTEM_OPS = (0x00000225)
        DOMAIN_ALIAS_RID_PRINT_OPS = (0x00000226)
        DOMAIN_ALIAS_RID_BACKUP_OPS = (0x00000227)
        DOMAIN_ALIAS_RID_REPLICATOR = (0x00000228)
        DOMAIN_ALIAS_RID_RAS_SERVERS = (0x00000229)
        DOMAIN_ALIAS_RID_PREW2KCOMPACCESS = (0x0000022A)
        DOMAIN_ALIAS_RID_REMOTE_DESKTOP_USERS = (0x0000022B)
        DOMAIN_ALIAS_RID_NETWORK_CONFIGURATION_OPS = (0x0000022C)
        DOMAIN_ALIAS_RID_INCOMING_FOREST_TRUST_BUILDERS = (0x0000022D)
        DOMAIN_ALIAS_RID_MONITORING_USERS = (0x0000022E)
        DOMAIN_ALIAS_RID_LOGGING_USERS = (0x0000022F)
        DOMAIN_ALIAS_RID_AUTHORIZATIONACCESS = (0x00000230)
        DOMAIN_ALIAS_RID_TS_LICENSE_SERVERS = (0x00000231)
        DOMAIN_ALIAS_RID_DCOM_USERS = (0x00000232)
        DOMAIN_ALIAS_RID_IUSERS = (0x00000238)
        DOMAIN_ALIAS_RID_CRYPTO_OPERATORS = (0x00000239)
        DOMAIN_ALIAS_RID_CACHEABLE_PRINCIPALS_GROUP = (0x0000023B)
        DOMAIN_ALIAS_RID_NON_CACHEABLE_PRINCIPALS_GROUP = (0x0000023C)
        DOMAIN_ALIAS_RID_EVENT_LOG_READERS_GROUP = (0x0000023D)
        DOMAIN_ALIAS_RID_CERTSVC_DCOM_ACCESS_GROUP = (0x0000023E)
        DOMAIN_ALIAS_RID_RDS_REMOTE_ACCESS_SERVERS = (0x0000023F)
        DOMAIN_ALIAS_RID_RDS_ENDPOINT_SERVERS = (0x00000240)
        DOMAIN_ALIAS_RID_RDS_MANAGEMENT_SERVERS = (0x00000241)
        DOMAIN_ALIAS_RID_HYPER_V_ADMINS = (0x00000242)
        DOMAIN_ALIAS_RID_ACCESS_CONTROL_ASSISTANCE_OPS = (0x00000243)
        DOMAIN_ALIAS_RID_REMOTE_MANAGEMENT_USERS = (0x00000244)
        DOMAIN_ALIAS_RID_DEFAULT_ACCOUNT = (0x00000245)
        DOMAIN_ALIAS_RID_STORAGE_REPLICA_ADMINS = (0x00000246)
        DOMAIN_ALIAS_RID_DEVICE_OWNERS = (0x00000247)
        SECURITY_APP_PACKAGE_AUTHORITY = 0,0,0,0,0,15
        SECURITY_APP_PACKAGE_BASE_RID = (0x00000002)
        SECURITY_BUILTIN_APP_PACKAGE_RID_COUNT = (2)
        SECURITY_APP_PACKAGE_RID_COUNT = (8)
        SECURITY_CAPABILITY_BASE_RID = (0x00000003)
        SECURITY_CAPABILITY_APP_RID = (0x000000400)
        SECURITY_BUILTIN_CAPABILITY_RID_COUNT = (2)
        SECURITY_CAPABILITY_RID_COUNT = (5)
        SECURITY_PARENT_PACKAGE_RID_COUNT = (SECURITY_APP_PACKAGE_RID_COUNT)
        SECURITY_CHILD_PACKAGE_RID_COUNT = (12)
        SECURITY_BUILTIN_PACKAGE_ANY_PACKAGE =  (0x00000001)
        SECURITY_BUILTIN_PACKAGE_ANY_RESTRICTED_PACKAGE = (0x00000002)
        SECURITY_CAPABILITY_INTERNET_CLIENT = (0x00000001)
        SECURITY_CAPABILITY_INTERNET_CLIENT_SERVER = (0x00000002)
        SECURITY_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER = (0x00000003)
        SECURITY_CAPABILITY_PICTURES_LIBRARY = (0x00000004)
        SECURITY_CAPABILITY_VIDEOS_LIBRARY = (0x00000005)
        SECURITY_CAPABILITY_MUSIC_LIBRARY = (0x00000006)
        SECURITY_CAPABILITY_DOCUMENTS_LIBRARY = (0x00000007)
        SECURITY_CAPABILITY_ENTERPRISE_AUTHENTICATION = (0x00000008)
        SECURITY_CAPABILITY_SHARED_USER_CERTIFICATES = (0x00000009)
        SECURITY_CAPABILITY_REMOVABLE_STORAGE = (0x0000000A)
        SECURITY_CAPABILITY_APPOINTMENTS = (0x0000000B)
        SECURITY_CAPABILITY_CONTACTS = (0x0000000C)
        SECURITY_CAPABILITY_INTERNET_EXPLORER = (0x00001000)
        SECURITY_MANDATORY_LABEL_AUTHORITY = 0,0,0,0,0,16
        SECURITY_MANDATORY_UNTRUSTED_RID = (0x00000000)
        SECURITY_MANDATORY_LOW_RID = (0x00001000)
        SECURITY_MANDATORY_MEDIUM_RID = (0x00002000)
        SECURITY_MANDATORY_MEDIUM_PLUS_RID = (SECURITY_MANDATORY_MEDIUM_RID + 0x100)
        SECURITY_MANDATORY_HIGH_RID = (0x00003000)
        SECURITY_MANDATORY_SYSTEM_RID = (0x00004000)
        SECURITY_MANDATORY_PROTECTED_PROCESS_RID = (0x00005000)
        SECURITY_MANDATORY_MAXIMUM_USER_RID = SECURITY_MANDATORY_SYSTEM_RID
        MANDATORY_LEVEL_TO_MANDATORY_RID = lambda IL: IL * 0x1000
        SECURITY_SCOPED_POLICY_ID_AUTHORITY = 0,0,0,0,0,17
        SECURITY_AUTHENTICATION_AUTHORITY = 0,0,0,0,0,18
        SECURITY_AUTHENTICATION_AUTHORITY_RID_COUNT = (1)
        SECURITY_AUTHENTICATION_AUTHORITY_ASSERTED_RID = (0x00000001)
        SECURITY_AUTHENTICATION_SERVICE_ASSERTED_RID = (0x00000002)
        SECURITY_AUTHENTICATION_FRESH_KEY_AUTH_RID = (0x00000003)
        SECURITY_AUTHENTICATION_KEY_TRUST_RID = (0x00000004)
        SECURITY_AUTHENTICATION_KEY_PROPERTY_MFA_RID = (0x00000005)
        SECURITY_AUTHENTICATION_KEY_PROPERTY_ATTESTATION_RID = (0x00000006)
        SECURITY_PROCESS_TRUST_AUTHORITY = 0,0,0,0,0,19
        SECURITY_PROCESS_TRUST_AUTHORITY_RID_COUNT = (2)
        SECURITY_PROCESS_PROTECTION_TYPE_FULL_RID = (0x00000400)
        SECURITY_PROCESS_PROTECTION_TYPE_LITE_RID = (0x00000200)
        SECURITY_PROCESS_PROTECTION_TYPE_NONE_RID = (0x00000000)
        SECURITY_PROCESS_PROTECTION_LEVEL_WINTCB_RID = (0x00002000)
        SECURITY_PROCESS_PROTECTION_LEVEL_WINDOWS_RID = (0x00001000)
        SECURITY_PROCESS_PROTECTION_LEVEL_APP_RID = (0x00000800)
        SECURITY_PROCESS_PROTECTION_LEVEL_ANTIMALWARE_RID = (0x00000600)
        SECURITY_PROCESS_PROTECTION_LEVEL_AUTHENTICODE_RID = (0x00000400)
        SECURITY_PROCESS_PROTECTION_LEVEL_NONE_RID = (0x00000000)
        SECURITY_TRUSTED_INSTALLER_RID1 = 956008885
        SECURITY_TRUSTED_INSTALLER_RID2 = 3418522649
        SECURITY_TRUSTED_INSTALLER_RID3 = 1831038044
        SECURITY_TRUSTED_INSTALLER_RID4 = 1853292631
        SECURITY_TRUSTED_INSTALLER_RID5 = 2271478464
        
        WELL_KNOWN_SID_TYPE = INT
        if True:
            WinNullSid = 0
            WinWorldSid = 1
            WinLocalSid = 2
            WinCreatorOwnerSid = 3
            WinCreatorGroupSid = 4
            WinCreatorOwnerServerSid = 5
            WinCreatorGroupServerSid = 6
            WinNtAuthoritySid = 7
            WinDialupSid = 8
            WinNetworkSid = 9
            WinBatchSid = 10
            WinInteractiveSid = 11
            WinServiceSid = 12
            WinAnonymousSid = 13
            WinProxySid = 14
            WinEnterpriseControllersSid = 15
            WinSelfSid = 16
            WinAuthenticatedUserSid = 17
            WinRestrictedCodeSid = 18
            WinTerminalServerSid = 19
            WinRemoteLogonIdSid = 20
            WinLogonIdsSid = 21
            WinLocalSystemSid = 22
            WinLocalServiceSid = 23
            WinNetworkServiceSid = 24
            WinBuiltinDomainSid = 25
            WinBuiltinAdministratorsSid = 26
            WinBuiltinUsersSid = 27
            WinBuiltinGuestsSid = 28
            WinBuiltinPowerUsersSid = 29
            WinBuiltinAccountOperatorsSid = 30
            WinBuiltinSystemOperatorsSid = 31
            WinBuiltinPrintOperatorsSid = 32
            WinBuiltinBackupOperatorsSid = 33
            WinBuiltinReplicatorSid = 34
            WinBuiltinPreWindows2000CompatibleAccessSid = 35
            WinBuiltinRemoteDesktopUsersSid = 36
            WinBuiltinNetworkConfigurationOperatorsSid = 37
            WinAccountAdministratorSid = 38
            WinAccountGuestSid = 39
            WinAccountKrbtgtSid = 40
            WinAccountDomainAdminsSid = 41
            WinAccountDomainUsersSid = 42
            WinAccountDomainGuestsSid = 43
            WinAccountComputersSid = 44
            WinAccountControllersSid = 45
            WinAccountCertAdminsSid = 46
            WinAccountSchemaAdminsSid = 47
            WinAccountEnterpriseAdminsSid = 48
            WinAccountPolicyAdminsSid = 49
            WinAccountRasAndIasServersSid = 50
            WinNTLMAuthenticationSid = 51
            WinDigestAuthenticationSid = 52
            WinSChannelAuthenticationSid = 53
            WinThisOrganizationSid = 54
            WinOtherOrganizationSid = 55
            WinBuiltinIncomingForestTrustBuildersSid = 56
            WinBuiltinPerfMonitoringUsersSid = 57
            WinBuiltinPerfLoggingUsersSid = 58
            WinBuiltinAuthorizationAccessSid = 59
            WinBuiltinTerminalServerLicenseServersSid = 60
            WinBuiltinDCOMUsersSid = 61
            WinBuiltinIUsersSid = 62
            WinIUserSid = 63
            WinBuiltinCryptoOperatorsSid = 64
            WinUntrustedLabelSid = 65
            WinLowLabelSid = 66
            WinMediumLabelSid = 67
            WinHighLabelSid = 68
            WinSystemLabelSid = 69
            WinWriteRestrictedCodeSid = 70
            WinCreatorOwnerRightsSid = 71
            WinCacheablePrincipalsGroupSid = 72
            WinNonCacheablePrincipalsGroupSid = 73
            WinEnterpriseReadonlyControllersSid = 74
            WinAccountReadonlyControllersSid = 75
            WinBuiltinEventLogReadersGroup = 76
            WinNewEnterpriseReadonlyControllersSid = 77
            WinBuiltinCertSvcDComAccessGroup = 78
            WinMediumPlusLabelSid = 79
            WinLocalLogonSid = 80
            WinConsoleLogonSid = 81
            WinThisOrganizationCertificateSid = 82
            WinApplicationPackageAuthoritySid = 83
            WinBuiltinAnyPackageSid = 84
            WinCapabilityInternetClientSid = 85
            WinCapabilityInternetClientServerSid = 86
            WinCapabilityPrivateNetworkClientServerSid = 87
            WinCapabilityPicturesLibrarySid = 88
            WinCapabilityVideosLibrarySid = 89
            WinCapabilityMusicLibrarySid = 90
            WinCapabilityDocumentsLibrarySid = 91
            WinCapabilitySharedUserCertificatesSid = 92
            WinCapabilityEnterpriseAuthenticationSid = 93
            WinCapabilityRemovableStorageSid = 94
            WinBuiltinRDSRemoteAccessServersSid = 95
            WinBuiltinRDSEndpointServersSid = 96
            WinBuiltinRDSManagementServersSid = 97
            WinUserModeDriversSid = 98
            WinBuiltinHyperVAdminsSid = 99
            WinAccountCloneableControllersSid = 100
            WinBuiltinAccessControlAssistanceOperatorsSid = 101
            WinBuiltinRemoteManagementUsersSid = 102
            WinAuthenticationAuthorityAssertedSid = 103
            WinAuthenticationServiceAssertedSid = 104
            WinLocalAccountSid = 105
            WinLocalAccountAndAdministratorSid = 106
            WinAccountProtectedUsersSid = 107
            WinCapabilityAppointmentsSid = 108
            WinCapabilityContactsSid = 109
            WinAccountDefaultSystemManagedSid = 110
            WinBuiltinDefaultSystemManagedGroupSid = 111
            WinBuiltinStorageReplicaAdminsSid = 112
            WinAccountKeyAdminsSid = 113
            WinAccountEnterpriseKeyAdminsSid = 114
            WinAuthenticationKeyTrustSid = 115
            WinAuthenticationKeyPropertyMFASid = 116
            WinAuthenticationKeyPropertyAttestationSid = 117
            WinAuthenticationFreshKeyAuthSid = 118
            WinBuiltinDeviceOwnersSid = 119
            
        ANONYMOUS_LOGON_LUID = 0x3e6, 0x0
        LOCALSERVICE_LUID = 0x3e5, 0x0
        NETWORKSERVICE_LUID = 0x3e4, 0x0
        IUSER_LUID = 0x3e3, 0x0
        PROTECTED_TO_SYSTEM_LUID = 0x3e2, 0x0
        SE_GROUP_MANDATORY = (0x00000001)
        SE_GROUP_ENABLED_BY_DEFAULT = (0x00000002)
        SE_GROUP_ENABLED = (0x00000004)
        SE_GROUP_OWNER = (0x00000008)
        SE_GROUP_USE_FOR_DENY_ONLY = (0x00000010)
        SE_GROUP_INTEGRITY = (0x00000020)
        SE_GROUP_INTEGRITY_ENABLED = (0x00000040)
        SE_GROUP_LOGON_ID = (0xC0000000)
        SE_GROUP_RESOURCE = (0x20000000)
        
        SE_GROUP_VALID_ATTRIBUTES = SE_GROUP_MANDATORY | SE_GROUP_ENABLED_BY_DEFAULT | SE_GROUP_ENABLED | SE_GROUP_OWNER | SE_GROUP_USE_FOR_DENY_ONLY | SE_GROUP_LOGON_ID | SE_GROUP_RESOURCE | SE_GROUP_INTEGRITY | SE_GROUP_INTEGRITY_ENABLED
        
        ACL_REVISION = (2)
        ACL_REVISION_DS = (4)
        ACL_REVISION1 = (1)
        ACL_REVISION2 = (2)
        MIN_ACL_REVISION = ACL_REVISION2
        ACL_REVISION3 = (3)
        ACL_REVISION4 = (4)
        MAX_ACL_REVISION = ACL_REVISION4
        
        class ACL(CStructure):
            _fields_ = [
                ("AclRevision", BYTE),
                ("Sbz1", BYTE),
                ("AclSize", WORD),
                ("AceCount", WORD),
                ("Sbz2", WORD)
            ]
        
        PACL = POINTER(ACL)

        class _ACE_HEADER(CStructure):
            _fields_ = [
                ("AceType", BYTE),
                ("AceFlags", BYTE),
                ("AceSize", WORD)
            ]
        
        ACE_HEADER = _ACE_HEADER
        PACE_HEADER = POINTER(ACE_HEADER)
        
        ACCESS_MIN_MS_ACE_TYPE = (0x0)
        ACCESS_ALLOWED_ACE_TYPE = (0x0)
        ACCESS_DENIED_ACE_TYPE = (0x1)
        SYSTEM_AUDIT_ACE_TYPE = (0x2)
        SYSTEM_ALARM_ACE_TYPE = (0x3)
        ACCESS_MAX_MS_V2_ACE_TYPE = (0x3)
        ACCESS_ALLOWED_COMPOUND_ACE_TYPE = (0x4)
        ACCESS_MAX_MS_V3_ACE_TYPE = (0x4)
        ACCESS_MIN_MS_OBJECT_ACE_TYPE = (0x5)
        ACCESS_ALLOWED_OBJECT_ACE_TYPE = (0x5)
        ACCESS_DENIED_OBJECT_ACE_TYPE = (0x6)
        SYSTEM_AUDIT_OBJECT_ACE_TYPE = (0x7)
        SYSTEM_ALARM_OBJECT_ACE_TYPE = (0x8)
        ACCESS_MAX_MS_OBJECT_ACE_TYPE = (0x8)
        ACCESS_MAX_MS_V4_ACE_TYPE = (0x8)
        ACCESS_MAX_MS_ACE_TYPE = (0x8)
        ACCESS_ALLOWED_CALLBACK_ACE_TYPE = (0x9)
        ACCESS_DENIED_CALLBACK_ACE_TYPE = (0xA)
        ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE = (0xB)
        ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE = (0xC)
        SYSTEM_AUDIT_CALLBACK_ACE_TYPE = (0xD)
        SYSTEM_ALARM_CALLBACK_ACE_TYPE = (0xE)
        SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE = (0xF)
        SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE = (0x10)
        SYSTEM_MANDATORY_LABEL_ACE_TYPE = (0x11)
        SYSTEM_RESOURCE_ATTRIBUTE_ACE_TYPE = (0x12)
        SYSTEM_SCOPED_POLICY_ID_ACE_TYPE = (0x13)
        SYSTEM_PROCESS_TRUST_LABEL_ACE_TYPE = (0x14)
        SYSTEM_ACCESS_FILTER_ACE_TYPE = (0x15)
        ACCESS_MAX_MS_V5_ACE_TYPE = (0x15)
        OBJECT_INHERIT_ACE = (0x1)
        CONTAINER_INHERIT_ACE = (0x2)
        NO_PROPAGATE_INHERIT_ACE = (0x4)
        INHERIT_ONLY_ACE = (0x8)
        INHERITED_ACE = (0x10)
        VALID_INHERIT_FLAGS = (0x1F)
        CRITICAL_ACE_FLAG = (0x20)
        SUCCESSFUL_ACCESS_ACE_FLAG = (0x40)
        FAILED_ACCESS_ACE_FLAG = (0x80)
        TRUST_PROTECTED_FILTER_ACE_FLAG = (0x40)

        _SECURITY_IMPERSONATION_LEVEL = INT
        if True:
            SecurityAnonymous = 0
            SecurityIdentification = 1
            SecurityImpersonation = 2
            SecurityDelegation = 3
        SECURITY_IMPERSONATION_LEVEL = _SECURITY_IMPERSONATION_LEVEL
        PSECURITY_IMPERSONATION_LEVEL = POINTER(SECURITY_IMPERSONATION_LEVEL)
        
        THREAD_DYNAMIC_CODE_ALLOW   = 1     # Opt-out of dynamic code generation.

        THREAD_BASE_PRIORITY_LOWRT  = 15  # value that gets a thread to LowRealtime-1
        THREAD_BASE_PRIORITY_MAX    = 2   # maximum thread base priority boost
        THREAD_BASE_PRIORITY_MIN    = (-2)  # minimum thread base priority boost
        THREAD_BASE_PRIORITY_IDLE   = (-15) # value that gets a thread to idle
        
        _PROCESS_MITIGATION_POLICY = INT
        if True:
            ProcessDEPPolicy = 0
            ProcessASLRPolicy = 1
            ProcessDynamicCodePolicy = 2
            ProcessStrictHandleCheckPolicy = 3
            ProcessSystemCallDisablePolicy = 4
            ProcessMitigationOptionsMask = 5
            ProcessExtensionPointDisablePolicy = 6
            ProcessControlFlowGuardPolicy = 7
            ProcessSignaturePolicy = 8
            ProcessFontDisablePolicy = 9
            ProcessImageLoadPolicy = 10
            ProcessSystemCallFilterPolicy = 11
            ProcessPayloadRestrictionPolicy = 12
            ProcessChildProcessPolicy = 13
            ProcessSideChannelIsolationPolicy = 14
            ProcessUserShadowStackPolicy = 15
            MaxProcessMitigationPolicy = 16
        PROCESS_MITIGATION_POLICY = _PROCESS_MITIGATION_POLICY
        PPROCESS_MITIGATION_POLICY = POINTER(PROCESS_MITIGATION_POLICY)
        
        #
        # Page/memory priorities.
        #

        MEMORY_PRIORITY_LOWEST = 0
        MEMORY_PRIORITY_VERY_LOW = 1
        MEMORY_PRIORITY_LOW = 2
        MEMORY_PRIORITY_MEDIUM = 3
        MEMORY_PRIORITY_BELOW_NORMAL = 4
        MEMORY_PRIORITY_NORMAL = 5


        #
        # Process dynamic exception handling continuation targets information.
        #
        # Information class - ProcessDynamicEHContinuationTargets.
        #

        #
        # Dynamic exception handling continuation target should be added. If not set,
        # the target is removed. Input flag.
        #

        DYNAMIC_EH_CONTINUATION_TARGET_ADD = (0x00000001)

        #
        # Dynamic exception handling continuation target has been successfully
        # processed. Used to report to the caller how much progress has been made.
        # Output flag.
        #

        DYNAMIC_EH_CONTINUATION_TARGET_PROCESSED = (0x00000002)

        class _PROCESS_DYNAMIC_EH_CONTINUATION_TARGET(CStructure):
            _fields_ = [
                ("TargetAddress", ULONG_PTR),
                ("Flags", ULONG_PTR)
            ]
        PROCESS_DYNAMIC_EH_CONTINUATION_TARGET = _PROCESS_DYNAMIC_EH_CONTINUATION_TARGET
        PPROCESS_DYNAMIC_EH_CONTINUATION_TARGET = POINTER(PROCESS_DYNAMIC_EH_CONTINUATION_TARGET)

        class _PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION(CStructure):
            _fields_ = [
                ("NumberOfTargets", WORD),
                ("Reserved", WORD),
                ("Reserved2", DWORD),
                ("Targets", PPROCESS_DYNAMIC_EH_CONTINUATION_TARGET)
            ]
        PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION = _PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION
        PPROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION = POINTER(PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION)

        #
        # Process dynamic enforced address ranges information, used for dynamic
        # enforced CETCOMPAT ranges.
        #
        # Information class - ProcessDynamicEnforcedCetCompatibleRanges.
        #

        #
        # Dynamic enforced address range should be added. If not set, the range is
        # removed. Input flag.
        #

        DYNAMIC_ENFORCED_ADDRESS_RANGE_ADD = (0x00000001)

        #
        # Dynamic enforced address range has been successfully processed. Used to
        # report to the caller how much progress has been made. Output flag.
        #

        DYNAMIC_ENFORCED_ADDRESS_RANGE_PROCESSED = (0x00000002)

        class _PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE(CStructure):
            _fields_ = [
                ("BaseAddress", ULONG_PTR),
                ("Size", SIZE_T),
                ("Flags", DWORD)
            ]
        PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE = _PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE
        PPROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE = POINTER(PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE)

        class _PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION(CStructure):
            _fields_ = [
                ("NumberOfRanges", WORD),
                ("Reserved", WORD),
                ("Reserved2", DWORD),
                ("Ranges", PPROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE)
            ]
        PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION = _PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION
        PPROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION = POINTER(PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGES_INFORMATION)

        _CPU_SET_INFORMATION_TYPE = INT
        if True:
            CpuSetInformation = 0
        CPU_SET_INFORMATION_TYPE = _CPU_SET_INFORMATION_TYPE
        PCPU_SET_INFORMATION_TYPE = POINTER(CPU_SET_INFORMATION_TYPE)
        
        SYSTEM_CPU_SET_INFORMATION_PARKED = 0x1
        SYSTEM_CPU_SET_INFORMATION_ALLOCATED = 0x2
        SYSTEM_CPU_SET_INFORMATION_ALLOCATED_TO_TARGET_PROCESS = 0x4
        SYSTEM_CPU_SET_INFORMATION_REALTIME = 0x8

        CPU_SET_INFORMATION_TYPE = INT
        if True:
            CpuSetInformation = 0

        class _S_PAARR(CStructure):
            _fields_ = [
                ("Parked", BYTE, 1),
                ("Allocated", BYTE, 1),
                ("AllocatedToTargetProcess", BYTE, 1),
                ("RealTime", BYTE, 1),
                ("ReservedFlags", BYTE, 4)
            ]

        class _S_AS(Union):
            _fields_ = [
                ("AllFlags", BYTE),
                ("DUMMYSTRUCTNAME", _S_PAARR)
            ]

        class _S_CPISET_IGLCLNEURA(CStructure):
            _fields_ = [
                ("Id", DWORD),
                ("Group", WORD),
                ("LogicalProcessorIndex", BYTE),
                ("CoreIndex", BYTE),
                ("LastLevelCacheIndex", BYTE),
                ("NumaNodeIndex", BYTE),
                ("EfficiencyClass", BYTE),
                ("DUMMYUNIONNAME2", _S_AS),
                ("Reserved", DWORD),  # Overlay with SchedulingClass (BYTE)
                ("AllocationTag", ULONGLONG)
            ]

        class _U_CPUSET_C(Union):
            _fields_ = [
                ("CpuSet", _S_CPISET_IGLCLNEURA),
            ]


        class _SYSTEM_CPU_SET_INFORMATION(CStructure):
            _fields_ = [
                ("Size", c_uint),
                ("Type", CPU_SET_INFORMATION_TYPE),
                ("DUMMYUNIONNAME", _U_CPUSET_C)
            ]

        SYSTEM_CPU_SET_INFORMATION = _SYSTEM_CPU_SET_INFORMATION
        PSYSTEM_CPU_SET_INFORMATION = POINTER(SYSTEM_CPU_SET_INFORMATION)

        class SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION(CStructure):
            _fields_ = [
                ("CycleTime", UINT64)
            ]
        PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION = POINTER(SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION)

        # begin_access
        #
        # Define access rights to files and directories
        #
        #
        # The FILE_READ_DATA and FILE_WRITE_DATA constants are also defined in
        # devioctl.h as FILE_READ_ACCESS and FILE_WRITE_ACCESS. The values for these
        # constants *MUST* always be in sync.
        # The values are redefined in devioctl.h because they must be available to
        # both DOS and NT.
        #
        FILE_READ_DATA = (0x0001) # file & pipe
        FILE_LIST_DIRECTORY = (0x0001) # directory
        FILE_WRITE_DATA = (0x0002) # file & pipe
        FILE_ADD_FILE = (0x0002) # directory
        FILE_APPEND_DATA = (0x0004) # file
        FILE_ADD_SUBDIRECTORY = (0x0004) # directory
        cpreproc.define("FILE_CREATE_PIPE_INSTANCE(0x0004)")
        FILE_READ_EA = (0x0008) # file & directory
        FILE_WRITE_EA = (0x0010) # file & directory
        FILE_EXECUTE = (0x0020) # file
        FILE_TRAVERSE = (0x0020) # directory
        FILE_DELETE_CHILD = (0x0040) # directory
        FILE_READ_ATTRIBUTES = (0x0080) # all
        FILE_WRITE_ATTRIBUTES = (0x0100) # all
        FILE_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x1FF)
        FILE_GENERIC_READ = (STANDARD_RIGHTS_READ |
                            FILE_READ_DATA |
                            FILE_READ_ATTRIBUTES |
                            FILE_READ_EA |
                            SYNCHRONIZE) 
        FILE_GENERIC_WRITE = (STANDARD_RIGHTS_WRITE |
                            FILE_WRITE_DATA |
                            FILE_WRITE_ATTRIBUTES |
                            FILE_WRITE_EA |
                            FILE_APPEND_DATA |
                            SYNCHRONIZE)
        FILE_GENERIC_EXECUTE = (STANDARD_RIGHTS_EXECUTE |
                            FILE_READ_ATTRIBUTES |
                            FILE_EXECUTE |
                            SYNCHRONIZE)
        # end_access
        FILE_SHARE_READ = 0x00000001
        FILE_SHARE_WRITE = 0x00000002
        FILE_SHARE_DELETE = 0x00000004
        FILE_ATTRIBUTE_READONLY = 0x00000001
        FILE_ATTRIBUTE_HIDDEN = 0x00000002
        FILE_ATTRIBUTE_SYSTEM = 0x00000004
        FILE_ATTRIBUTE_DIRECTORY = 0x00000010
        FILE_ATTRIBUTE_ARCHIVE = 0x00000020
        FILE_ATTRIBUTE_DEVICE = 0x00000040
        FILE_ATTRIBUTE_NORMAL = 0x00000080
        FILE_ATTRIBUTE_TEMPORARY = 0x00000100
        FILE_ATTRIBUTE_SPARSE_FILE = 0x00000200
        FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
        FILE_ATTRIBUTE_COMPRESSED = 0x00000800
        FILE_ATTRIBUTE_OFFLINE = 0x00001000
        FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 0x00002000
        FILE_ATTRIBUTE_ENCRYPTED = 0x00004000
        FILE_ATTRIBUTE_INTEGRITY_STREAM = 0x00008000
        FILE_ATTRIBUTE_VIRTUAL = 0x00010000
        FILE_ATTRIBUTE_NO_SCRUB_DATA = 0x00020000
        FILE_ATTRIBUTE_EA = 0x00040000
        FILE_ATTRIBUTE_PINNED = 0x00080000
        FILE_ATTRIBUTE_UNPINNED = 0x00100000
        FILE_ATTRIBUTE_RECALL_ON_OPEN = 0x00040000
        FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 0x00400000
        TREE_CONNECT_ATTRIBUTE_PRIVACY = 0x00004000
        TREE_CONNECT_ATTRIBUTE_INTEGRITY = 0x00008000
        TREE_CONNECT_ATTRIBUTE_GLOBAL = 0x00000004
        TREE_CONNECT_ATTRIBUTE_PINNED = 0x00000002
        FILE_ATTRIBUTE_STRICTLY_SEQUENTIAL = 0x20000000
        FILE_NOTIFY_CHANGE_FILE_NAME = 0x00000001
        FILE_NOTIFY_CHANGE_DIR_NAME = 0x00000002
        FILE_NOTIFY_CHANGE_ATTRIBUTES = 0x00000004
        FILE_NOTIFY_CHANGE_SIZE = 0x00000008
        FILE_NOTIFY_CHANGE_LAST_WRITE = 0x00000010
        FILE_NOTIFY_CHANGE_LAST_ACCESS = 0x00000020
        FILE_NOTIFY_CHANGE_CREATION = 0x00000040
        FILE_NOTIFY_CHANGE_SECURITY = 0x00000100
        FILE_ACTION_ADDED = 0x00000001
        FILE_ACTION_REMOVED = 0x00000002
        FILE_ACTION_MODIFIED = 0x00000003
        FILE_ACTION_RENAMED_OLD_NAME = 0x00000004
        FILE_ACTION_RENAMED_NEW_NAME = 0x00000005
        MAILSLOT_NO_MESSAGE = DWORD(-1).value
        MAILSLOT_WAIT_FOREVER = DWORD(-1).value
        FILE_CASE_SENSITIVE_SEARCH = 0x00000001
        FILE_CASE_PRESERVED_NAMES = 0x00000002
        FILE_UNICODE_ON_DISK = 0x00000004
        FILE_PERSISTENT_ACLS = 0x00000008
        FILE_FILE_COMPRESSION = 0x00000010
        FILE_VOLUME_QUOTAS = 0x00000020
        FILE_SUPPORTS_SPARSE_FILES = 0x00000040
        FILE_SUPPORTS_REPARSE_POINTS = 0x00000080
        FILE_SUPPORTS_REMOTE_STORAGE = 0x00000100
        FILE_RETURNS_CLEANUP_RESULT_INFO = 0x00000200
        FILE_SUPPORTS_POSIX_UNLINK_RENAME = 0x00000400
        FILE_VOLUME_IS_COMPRESSED = 0x00008000
        FILE_SUPPORTS_OBJECT_IDS = 0x00010000
        FILE_SUPPORTS_ENCRYPTION = 0x00020000
        FILE_NAMED_STREAMS = 0x00040000
        FILE_READ_ONLY_VOLUME = 0x00080000
        FILE_SEQUENTIAL_WRITE_ONCE = 0x00100000
        FILE_SUPPORTS_TRANSACTIONS = 0x00200000
        FILE_SUPPORTS_HARD_LINKS = 0x00400000
        FILE_SUPPORTS_EXTENDED_ATTRIBUTES = 0x00800000
        FILE_SUPPORTS_OPEN_BY_FILE_ID = 0x01000000
        FILE_SUPPORTS_USN_JOURNAL = 0x02000000
        FILE_SUPPORTS_INTEGRITY_STREAMS = 0x04000000
        FILE_SUPPORTS_BLOCK_REFCOUNTING = 0x08000000
        FILE_SUPPORTS_SPARSE_VDL = 0x10000000
        FILE_DAX_VOLUME = 0x20000000
        FILE_SUPPORTS_GHOSTING = 0x40000000
        FILE_INVALID_FILE_ID = -1
        
        # begin_access

        #
        # Object Manager Symbolic Link Specific Access Rights.
        #

        DUPLICATE_CLOSE_SOURCE     = 0x00000001  
        DUPLICATE_SAME_ACCESS      = 0x00000002  

        #
        # Mutant Specific Access Rights
        #
        MUTANT_QUERY_STATE = 0x0001
        MUTANT_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED|SYNCHRONIZE|
                             MUTANT_QUERY_STATE)
        SEMAPHORE_MODIFY_STATE = 0x0002
        SEMAPHORE_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED|SYNCHRONIZE|0x3)
        #
        # Timer Specific Access Rights.
        #
        TIMER_QUERY_STATE = 0x0001
        TIMER_MODIFY_STATE = 0x0002
        TIMER_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED|SYNCHRONIZE|
                            TIMER_QUERY_STATE|TIMER_MODIFY_STATE)
        # begin_nthal
        TIME_ZONE_ID_UNKNOWN = 0
        TIME_ZONE_ID_STANDARD = 1
        TIME_ZONE_ID_DAYLIGHT = 2
        # end_nthal

        _LOGICAL_PROCESSOR_RELATIONSHIP = INT
        if True:
            RelationProcessorCore = 0
            RelationNumaNode = 1
            RelationCache = 2
            RelationProcessorPackage = 3
            RelationGroup = 4
            RelationProcessorDie = 5
            RelationNumaNodeEx = 6
            RelationProcessorModule = 7
            RelationAll = 0xffff
        LOGICAL_PROCESSOR_RELATIONSHIP = _LOGICAL_PROCESSOR_RELATIONSHIP

        _PROCESSOR_CACHE_TYPE = INT
        if True:
            CacheUnified = 0
            CacheInstruction = 1
            CacheData = 2
            CacheTrace = 3
            CacheUnknown = 4
        PROCESSOR_CACHE_TYPE = _PROCESSOR_CACHE_TYPE
        PPROCESSOR_CACHE_TYPE = POINTER(PROCESSOR_CACHE_TYPE)

        class _CACHE_DESCRIPTOR(CStructure):
            _fields_ = [
                ("Level", BYTE),
                ("Associativity", BYTE),
                ("LineSize", WORD),
                ("Size", DWORD),
                ("Type", PROCESSOR_CACHE_TYPE)
            ]
        CACHE_DESCRIPTOR = _CACHE_DESCRIPTOR
        PCACHE_DESCRIPTOR = POINTER(CACHE_DESCRIPTOR)

        class _S_PCF(CStructure):
            _fields_ = [
                ("Flags", BYTE)
            ]

        class _S_NNNN(CStructure):
            _fields_ = [
                ("NodeNumber", DWORD)
            ]

        class _U_SPCNNCR(Union):
            _fields_ = [
                ("ProcessorCore", _S_PCF),
                ("NumaNode", _S_NNNN),
                ("Cache", CACHE_DESCRIPTOR),
                ("Reserved", ULONGLONG * 2)
            ]

        class _SYSTEM_LOGICAL_PROCESSOR_INFORMATION(CStructure):
            _fields_ = [
                ("ProcessorMask", ULONG_PTR),
                ("Relationship", LOGICAL_PROCESSOR_RELATIONSHIP),
                ("u", _U_SPCNNCR)
            ]
        SYSTEM_LOGICAL_PROCESSOR_INFORMATION = _SYSTEM_LOGICAL_PROCESSOR_INFORMATION
        PSYSTEM_LOGICAL_PROCESSOR_INFORMATION = POINTER(SYSTEM_LOGICAL_PROCESSOR_INFORMATION)

        class _PROCESSOR_RELATIONSHIP(CStructure):
            _fields_ = [
                ("Flags", BYTE),
                ("EfficiencyClass", BYTE),
                ("Reserved", BYTE * 20),
                ("GroupCount", WORD),
                ("GroupMask", PGROUP_AFFINITY)
            ]
        PROCESSOR_RELATIONSHIP = _PROCESSOR_RELATIONSHIP
        PPROCESSOR_RELATIONSHIP = POINTER(PROCESSOR_RELATIONSHIP)

        class _U_GMGMAR(Union):
            _fields_ = [
                ("GroupMask", PGROUP_AFFINITY),
                ("GroupMasks", PGROUP_AFFINITY)
            ]

        class _NUMA_NODE_RELATIONSHIP(CStructure):
            _fields_ = [
                ("NodeNumber", DWORD),
                ("Reserved", BYTE * 18),
                ("GroupCount", WORD),
                ("u", _U_GMGMAR)
            ]
        NUMA_NODE_RELATIONSHIP = _NUMA_NODE_RELATIONSHIP
        PNUMA_NODE_RELATIONSHIP = POINTER(NUMA_NODE_RELATIONSHIP)

        class _CACHE_RELATIONSHIP(CStructure):
            _fields_ = [
                ("Level", BYTE),
                ("Associativity", BYTE),
                ("LineSize", WORD),
                ("CacheSize", DWORD),
                ("Type", PROCESSOR_CACHE_TYPE),
                ("Reserved", BYTE * 18),
                ("GroupCount", WORD),
                ("u", _U_GMGMAR)
            ]
        CACHE_RELATIONSHIP = _CACHE_RELATIONSHIP
        PCACHE_RELATIONSHIP = POINTER(CACHE_RELATIONSHIP)

        class _PROCESSOR_GROUP_INFO(CStructure):
            _fields_ = [
                ("MaximumProcessorCount", BYTE),
                ("ActiveProcessorCount", BYTE),
                ("Reserved", BYTE * 38),
                ("ActiveProcessorMask", KAFFINITY)
            ]
        PROCESSOR_GROUP_INFO = _PROCESSOR_GROUP_INFO
        PPROCESSOR_GROUP_INFO = POINTER(PROCESSOR_GROUP_INFO)

        class _GROUP_RELATIONSHIP(CStructure):
            _fields_ = [
                ("MaximumGroupCount", WORD),
                ("Reserved", BYTE * 20),
                ("GroupInfo", PPROCESSOR_GROUP_INFO)
            ]
        GROUP_RELATIONSHIP = _GROUP_RELATIONSHIP
        PGROUP_RELATIONSHIP = POINTER(GROUP_RELATIONSHIP)

        class _U_PNNCG(Union):
            _fields_ = [
                ("Processor", PROCESSOR_RELATIONSHIP),
                ("NumaNode", NUMA_NODE_RELATIONSHIP),
                ("Cache", CACHE_RELATIONSHIP),
                ("Group", GROUP_RELATIONSHIP)
            ]

        class _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX(CStructure):
            _fields_ = [
                ("Relationship", LOGICAL_PROCESSOR_RELATIONSHIP),
                ("Size", DWORD),
                ("u", _U_PNNCG)
            ]
        SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX = _SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX
        PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX = POINTER(SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX)

        class _OSVERSIONINFOA(CStructure):
            _fields_ = [
                ("dwOSVersionInfoSize", DWORD),
                ("dwMajorVersion", DWORD),
                ("dwMinorVersion", DWORD),
                ("dwBuildNumber", DWORD),
                ("dwPlatformId", DWORD),
                ("dzCSDVersion", CHAR * 128)
            ]
        OSVERSIONINFOA = _OSVERSIONINFOA
        POSVERSIONINFOA = POINTER(OSVERSIONINFOA)
        LPOSVERSIONINFOA = POSVERSIONINFOA

        class _OSVERSIONINFOW(CStructure):
            _fields_ = [
                ("dwOSVersionInfoSize", DWORD),
                ("dwMajorVersion", DWORD),
                ("dwMinorVersion", DWORD),
                ("dwBuildNumber", DWORD),
                ("dwPlatformId", DWORD),
                ("dzCSDVersion", WCHAR * 128)
            ]
        OSVERSIONINFOW = _OSVERSIONINFOW
        POSVERSIONINFOW = POINTER(OSVERSIONINFOW)
        LPOSVERSIONINFOW = POSVERSIONINFOW

        RTL_OSVERSIONINFOW = OSVERSIONINFOW
        PRTL_OSVERSIONINFOW = LPOSVERSIONINFOW

        OSVERSIONINFO = unicode(OSVERSIONINFOW, OSVERSIONINFOA)
        POSVERSIONINFO = unicode(POSVERSIONINFOW, POSVERSIONINFOA)
        LPOSVERSIONINFO = unicode(LPOSVERSIONINFOW, LPOSVERSIONINFOA)

        PROCESSOR_INTEL_386 = 386
        PROCESSOR_INTEL_486 = 486
        PROCESSOR_INTEL_PENTIUM = 586
        PROCESSOR_INTEL_IA64 = 2200
        PROCESSOR_AMD_X8664 = 8664
        PROCESSOR_MIPS_R4000 = 4000 # incl R4101 & R3910 for Windows CE
        PROCESSOR_ALPHA_21064 = 21064
        PROCESSOR_PPC_601 = 601
        PROCESSOR_PPC_603 = 603
        PROCESSOR_PPC_604 = 604
        PROCESSOR_PPC_620 = 620
        PROCESSOR_HITACHI_SH3 = 10003 # Windows CE
        PROCESSOR_HITACHI_SH3E = 10004 # Windows CE
        PROCESSOR_HITACHI_SH4 = 10005 # Windows CE
        PROCESSOR_MOTOROLA_821 = 821 # Windows CE
        PROCESSOR_SHx_SH3 = 103 # Windows CE
        PROCESSOR_SHx_SH4 = 104 # Windows CE
        PROCESSOR_STRONGARM = 2577 # Windows CE - 0xA11
        PROCESSOR_ARM720 = 1824 # Windows CE - 0x720
        PROCESSOR_ARM820 = 2080 # Windows CE - 0x820
        PROCESSOR_ARM920 = 2336 # Windows CE - 0x920
        PROCESSOR_ARM_7TDMI = 70001 # Windows CE
        PROCESSOR_OPTIL = 0x494f # MSIL
        PROCESSOR_ARCHITECTURE_INTEL = 0
        PROCESSOR_ARCHITECTURE_MIPS = 1
        PROCESSOR_ARCHITECTURE_ALPHA = 2
        PROCESSOR_ARCHITECTURE_PPC = 3
        PROCESSOR_ARCHITECTURE_SHX = 4
        PROCESSOR_ARCHITECTURE_ARM = 5
        PROCESSOR_ARCHITECTURE_IA64 = 6
        PROCESSOR_ARCHITECTURE_ALPHA64 = 7
        PROCESSOR_ARCHITECTURE_MSIL = 8
        PROCESSOR_ARCHITECTURE_AMD64 = 9
        PROCESSOR_ARCHITECTURE_IA32_ON_WIN64 = 10
        PROCESSOR_ARCHITECTURE_NEUTRAL = 11
        PROCESSOR_ARCHITECTURE_ARM64 = 12
        PROCESSOR_ARCHITECTURE_ARM32_ON_WIN64 = 13
        PROCESSOR_ARCHITECTURE_IA32_ON_ARM64 = 14
        PROCESSOR_ARCHITECTURE_UNKNOWN = 0xFFFF
        PF_FLOATING_POINT_PRECISION_ERRATA = 0
        PF_FLOATING_POINT_EMULATED = 1
        PF_COMPARE_EXCHANGE_DOUBLE = 2
        PF_MMX_INSTRUCTIONS_AVAILABLE = 3
        PF_PPC_MOVEMEM_64BIT_OK = 4
        PF_ALPHA_BYTE_INSTRUCTIONS = 5
        PF_XMMI_INSTRUCTIONS_AVAILABLE = 6
        PF_3DNOW_INSTRUCTIONS_AVAILABLE = 7
        PF_RDTSC_INSTRUCTION_AVAILABLE = 8
        PF_PAE_ENABLED = 9
        PF_XMMI64_INSTRUCTIONS_AVAILABLE = 10
        PF_SSE_DAZ_MODE_AVAILABLE = 11
        PF_NX_ENABLED = 12
        PF_SSE3_INSTRUCTIONS_AVAILABLE = 13
        PF_COMPARE_EXCHANGE128 = 14
        PF_COMPARE64_EXCHANGE128 = 15
        PF_CHANNELS_ENABLED = 16
        PF_XSAVE_ENABLED = 17
        PF_ARM_VFP_32_REGISTERS_AVAILABLE = 18
        PF_ARM_NEON_INSTRUCTIONS_AVAILABLE = 19
        PF_SECOND_LEVEL_ADDRESS_TRANSLATION = 20
        PF_VIRT_FIRMWARE_ENABLED = 21
        PF_RDWRFSGSBASE_AVAILABLE = 22
        PF_FASTFAIL_AVAILABLE = 23
        PF_ARM_DIVIDE_INSTRUCTION_AVAILABLE = 24
        PF_ARM_64BIT_LOADSTORE_ATOMIC = 25
        PF_ARM_EXTERNAL_CACHE_AVAILABLE = 26
        PF_ARM_FMAC_INSTRUCTIONS_AVAILABLE = 27
        PF_RDRAND_INSTRUCTION_AVAILABLE = 28
        PF_ARM_V8_INSTRUCTIONS_AVAILABLE = 29
        PF_ARM_V8_CRYPTO_INSTRUCTIONS_AVAILABLE = 30
        PF_ARM_V8_CRC32_INSTRUCTIONS_AVAILABLE = 31
        PF_RDTSCP_INSTRUCTION_AVAILABLE = 32
        PF_RDPID_INSTRUCTION_AVAILABLE = 33
        PF_ARM_V81_ATOMIC_INSTRUCTIONS_AVAILABLE = 34
        PF_MONITORX_INSTRUCTION_AVAILABLE = 35
        PF_SSSE3_INSTRUCTIONS_AVAILABLE = 36
        PF_SSE4_1_INSTRUCTIONS_AVAILABLE = 37
        PF_SSE4_2_INSTRUCTIONS_AVAILABLE = 38
        PF_AVX_INSTRUCTIONS_AVAILABLE = 39
        PF_AVX2_INSTRUCTIONS_AVAILABLE = 40
        PF_AVX512F_INSTRUCTIONS_AVAILABLE = 41

        SECTION_QUERY = 0x0001
        SECTION_MAP_WRITE = 0x0002
        SECTION_MAP_READ = 0x0004
        SECTION_MAP_EXECUTE = 0x0008
        SECTION_EXTEND_SIZE = 0x0010
        SECTION_MAP_EXECUTE_EXPLICIT = 0x0020 # not included in SECTION_ALL_ACCESS
        SECTION_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SECTION_QUERY|
                              SECTION_MAP_WRITE                       |      
                              SECTION_MAP_READ                        |       
                              SECTION_MAP_EXECUTE                     |    
                              SECTION_EXTEND_SIZE)

        class _MEMORY_BASIC_INFORMATION(CStructure):
            _fields_ = [
                ("BaseAddress", PVOID),           # 8 байт
                ("AllocationBase", PVOID),        # 8 байт
                ("AllocationProtect", DWORD),     # 4 байта
                ("PartitionId", WORD),            # 2 байта (только для _WIN64)
                ("__alignment_padding", WORD),    # 2 байта (выравнивание до 8 байт)
                ("RegionSize", SIZE_T),           # 8 байт (c_ulonglong)
                ("State", DWORD),                 # 4 байта
                ("Protect", DWORD),               # 4 байта
                ("Type", DWORD)                   # 4 байта
            ]
            
            BaseAddress: PVOID
            AllocationBase: PVOID
            AllocationProtect: int
            PartitionId: int
            RegionSize: int
            State: int
            Protect: int
            Type: int
            
        MEMORY_BASIC_INFORMATION = _MEMORY_BASIC_INFORMATION
        PMEMORY_BASIC_INFORMATION = POINTER(MEMORY_BASIC_INFORMATION)

        class _CFG_CALL_TARGET_INFO(CStructure):
            _fields_ = [
                ("Offset", ULONG_PTR),
                ("Flags", ULONG_PTR)
            ]
        CFG_CALL_TARGET_INFO = _CFG_CALL_TARGET_INFO
        PCFG_CALL_TARGET_INFO = POINTER(CFG_CALL_TARGET_INFO)

        MEM_EXTENDED_PARAMETER_TYPE_BITS = 8

        class _S_TR(CStructure):
            _fields_ = [
                ("Type", DWORD64, MEM_EXTENDED_PARAMETER_TYPE_BITS),
                ("Reserved", DWORD64, 64 - MEM_EXTENDED_PARAMETER_TYPE_BITS)
            ]

        class _U_ULPSHU(Union):
            _fields_ = [
                ("ULong64", DWORD64),
                ("Pointer", PVOID),
                ("Size", SIZE_T),
                ("Handle", HANDLE),
                ("ULong", DWORD)
            ]

        class MEM_EXTENDED_PARAMETER(CStructure):
            _pack_ = 8
            _fields_ = [
                ("s", _S_TR),
                ("u", _U_ULPSHU)
            ]
        PMEM_EXTENDED_PARAMETER = POINTER(MEM_EXTENDED_PARAMETER)

        PROCESS_TERMINATE = (0x0001)
        PROCESS_CREATE_THREAD = (0x0002)
        PROCESS_SET_SESSIONID = (0x0004)
        PROCESS_VM_OPERATION = (0x0008)
        PROCESS_VM_READ = (0x0010)
        PROCESS_VM_WRITE = (0x0020)
        PROCESS_DUP_HANDLE = (0x0040)
        PROCESS_CREATE_PROCESS = (0x0080)
        PROCESS_SET_QUOTA = (0x0100)
        PROCESS_SET_INFORMATION = (0x0200)
        PROCESS_QUERY_INFORMATION = (0x0400)
        PROCESS_SUSPEND_RESUME = (0x0800)
        PROCESS_QUERY_LIMITED_INFORMATION = (0x1000)
        PROCESS_SET_LIMITED_INFORMATION = (0x2000)
        PROCESS_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFFF)

        # end_access
        PAGE_NOACCESS = 0x01
        PAGE_READONLY = 0x02
        PAGE_READWRITE = 0x04
        PAGE_WRITECOPY = 0x08
        PAGE_EXECUTE = 0x10
        PAGE_EXECUTE_READ = 0x20
        PAGE_EXECUTE_READWRITE = 0x40
        PAGE_EXECUTE_WRITECOPY = 0x80
        PAGE_GUARD = 0x100
        PAGE_NOCACHE = 0x200
        PAGE_WRITECOMBINE = 0x400
        PAGE_GRAPHICS_NOACCESS = 0x0800
        PAGE_GRAPHICS_READONLY = 0x1000
        PAGE_GRAPHICS_READWRITE = 0x2000
        PAGE_GRAPHICS_EXECUTE = 0x4000
        PAGE_GRAPHICS_EXECUTE_READ = 0x8000
        PAGE_GRAPHICS_EXECUTE_READWRITE = 0x10000
        PAGE_GRAPHICS_COHERENT = 0x20000
        PAGE_GRAPHICS_NOCACHE = 0x40000
        PAGE_ENCLAVE_THREAD_CONTROL = 0x80000000
        PAGE_REVERT_TO_FILE_MAP = 0x80000000
        PAGE_TARGETS_NO_UPDATE = 0x40000000
        PAGE_TARGETS_INVALID = 0x40000000
        PAGE_ENCLAVE_UNVALIDATED = 0x20000000
        PAGE_ENCLAVE_MASK = 0x10000000
        PAGE_ENCLAVE_DECOMMIT = (PAGE_ENCLAVE_MASK | 0)
        PAGE_ENCLAVE_SS_FIRST = (PAGE_ENCLAVE_MASK | 1)
        PAGE_ENCLAVE_SS_REST = (PAGE_ENCLAVE_MASK | 2)
        MEM_COMMIT = 0x00001000
        MEM_RESERVE = 0x00002000
        MEM_REPLACE_PLACEHOLDER = 0x00004000
        MEM_RESERVE_PLACEHOLDER = 0x00040000
        MEM_RESET = 0x00080000
        MEM_TOP_DOWN = 0x00100000
        MEM_WRITE_WATCH = 0x00200000
        MEM_PHYSICAL = 0x00400000
        MEM_ROTATE = 0x00800000
        MEM_DIFFERENT_IMAGE_BASE_OK = 0x00800000
        MEM_RESET_UNDO = 0x01000000
        MEM_LARGE_PAGES = 0x20000000
        MEM_4MB_PAGES = 0x80000000
        MEM_64K_PAGES = (MEM_LARGE_PAGES | MEM_PHYSICAL)
        MEM_UNMAP_WITH_TRANSIENT_BOOST = 0x00000001
        MEM_COALESCE_PLACEHOLDERS = 0x00000001
        MEM_PRESERVE_PLACEHOLDER = 0x00000002
        MEM_DECOMMIT = 0x00004000
        MEM_RELEASE = 0x00008000
        MEM_FREE = 0x00010000
        MEM_PRIVATE = 0x00020000  
        MEM_MAPPED = 0x00040000  
        MEM_IMAGE = 0x01000000  

        WAITORTIMERCALLBACKFUNC = NTAPI(VOID, PVOID, BOOLEAN)
        WORKERCALLBACKFUNC = NTAPI(VOID, PVOID)
        APC_CALLBACK_FUNCTION = NTAPI(VOID, DWORD, PVOID, PVOID)
        WAITORTIMERCALLBACK = WAITORTIMERCALLBACKFUNC
        
        IMAGE_DOS_SIGNATURE    =             0x5A4D         #  MZ
        IMAGE_OS2_SIGNATURE    =             0x454E         #  NE
        IMAGE_OS2_SIGNATURE_LE =             0x454C         #  LE
        IMAGE_VXD_SIGNATURE    =             0x454C         #  LE
        IMAGE_NT_SIGNATURE     =             0x00004550     #  PE00

        from .defbase import *

        class IMAGE_DOS_HEADER(CStructure):     # DOS .EXE header
            _pack_ = 2
            _fields_ = [
                ("e_magic", WORD),      # Magic number
                ("e_cblp", WORD),       # Bytes on last page of file
                ("e_cp", WORD),         # Pages in file
                ("e_crlc", WORD),       # Relocations
                ("e_cparhdr", WORD),    # Size of header in paragraphs
                ("e_minalloc", WORD),   # Minimum extra paragraphs needed
                ("e_maxalloc", WORD),   # Maximum extra paragraphs needed
                ("e_ss", WORD),         # Initial (relative) SS value
                ("e_sp", WORD),         # Initial SP value
                ("e_csum", WORD),       # Checksum
                ("e_ip", WORD),         # Initial IP value
                ("e_cs", WORD),         # Initial (relative) CS value
                ("e_lfarlc", WORD),     # File address of relocation table
                ("e_ovno", WORD),       # Overlay number
                ("e_res", WORD * 4),    # Reserved words
                ("e_oemid", WORD),      # OEM identifier (for e_oeminfo)
                ("e_oeminfo", WORD),    # OEM information; e_oemid specific
                ("e_res2", WORD * 10),  # Reserved words
                ("e_lfanew", LONG)      # File address of new exe header
            ]
            
            e_res2: IArray[WORD]
            e_res: IArray[WORD]
            e_minalloc: int
            e_maxalloc: int
            e_cparhdr: int
            e_oeminfo: int
            e_lfarlc: int
            e_lfanew: int
            e_magic: int
            e_oemid: int
            e_cblp: int
            e_crlc: int
            e_csum: int
            e_ovno: int
            e_cp: int
            e_ss: int
            e_sp: int
            e_ip: int
            e_cs: int
            
        PIMAGE_DOS_HEADER = POINTER(IMAGE_DOS_HEADER)

        class IMAGE_OS2_HEADER(CStructure):  # OS/2 .EXE header
            _pack_ = 2
            _fields_ = [
                ("ne_magic", WORD),         # Magic number
                ("ne_ver", CHAR),           # Version number
                ("ne_rev", CHAR),           # Revision number
                ("ne_enttab", WORD),        # Offset of Entry Table
                ("ne_cbenttab", WORD),      # Number of bytes in Entry Table
                ("ne_crc", LONG),           # Check
                ("ne_flags", WORD),         # Flag wordsum of whole file
                ("ne_autodata", WORD),      # Automatic data segment number
                ("ne_heap", WORD),          # Initial heap allocation
                ("ne_stack", WORD),         # Initial stack allocation
                ("ne_csip", LONG),          # Initial CS:IP setting
                ("ne_ssip", LONG),          # Initial SS:SP setting
                ("ne_cseg", WORD),          # Count of file segments
                ("ne_cmod", WORD),          # Entries in Module Reference Table
                ("ne_cbnrestab", WORD),     # Size of non-resident name table
                ("ne_segtab", WORD),        # Offset of Segment Table
                ("ne_rsrctab", WORD),       # Offset of Resource Table
                ("ne_restab", WORD),        # Offset of resident name table
                ("ne_modtab", WORD),        # Offset of Module Reference Table
                ("ne_imptab", WORD),        # Offset of Imported Names Table
                ("ne_nrestab", LONG),       # Offset of Non-resident Names Table
                ("ne_cmovent", WORD),       # Count of movable entries
                ("ne_align", WORD),         # Segment alignment shift count
                ("ne_cres", WORD),          # Count of resource segments
                ("ne_exetyp", BYTE),        # Target Operating system
                ("ne_flagsothers", BYTE),   # Other .EXE flags
                ("ne_pretthunks", WORD),    # offset to return thunks
                ("ne_psegrefbytes", WORD),  # offset to segment ref. bytes
                ("ne_swaparea", WORD),      # Minimum code swap area size
                ("ne_expver", WORD)         # Expected Windows version number
            ]
            
            ne_psegrefbytes: int
            ne_flagsothers: int
            ne_pretthunks: int
            ne_cbnrestab: int
            ne_cbenttab: int
            ne_autodata: int
            ne_swaparea: int
            ne_rsrctab: int
            ne_nrestab: int
            ne_cmovent: int
            ne_enttab: int
            ne_segtab: int
            ne_restab: int
            ne_modtab: int
            ne_imptab: int
            ne_exetyp: int
            ne_expver: int
            ne_magic: int
            ne_flags: int
            ne_stack: int
            ne_align: int
            ne_heap: int
            ne_csip: int
            ne_ssip: int
            ne_cseg: int
            ne_cmod: int
            ne_cres: int
            ne_ver: int
            ne_rev: int
            ne_crc: int
            
        PIMAGE_OS2_HEADER = POINTER(IMAGE_OS2_HEADER)

        class IMAGE_VXD_HEADER(CStructure):      # Windows VXD header
            _pack_ = 2
            _fields_ = [
                ("e32_magic", WORD),            # Magic number
                ("e32_border", BYTE),           # The byte ordering for the VXD
                ("e32_worder", BYTE),           # The word ordering for the VXD
                ("e32_level", DWORD),           # The EXE format level for now = 0
                ("e32_cpu", WORD),              # The CPU type
                ("e32_os", WORD),               # The OS type
                ("e32_ver", DWORD),             # Module version
                ("e32_mflags", DWORD),          # Module flags
                ("e32_mpages", DWORD),          # Module # pages
                ("e32_startobj", DWORD),        # Object # for instruction pointer
                ("e32_eip", DWORD),             # Extended instruction pointer
                ("e32_stackobj", DWORD),        # Object # for stack pointer
                ("e32_esp", DWORD),             # Extended stack pointer
                ("e32_pagesize", DWORD),        # VXD page size
                ("e32_lastpagesize", DWORD),    # Last page size in VXD
                ("e32_fixupsize", DWORD),       # Fixup section size
                ("e32_fixupsum", DWORD),        # Fixup section checksum
                ("e32_ldrsize", DWORD),         # Loader section size
                ("e32_ldrsum", DWORD),          # Loader section checksum
                ("e32_objtab", DWORD),          # Object table offset
                ("e32_objcnt", DWORD),          # Number of objects in module
                ("e32_objmap", DWORD),          # Object page map offset
                ("e32_itermap", DWORD),         # Object iterated data map offset
                ("e32_rsrctab", DWORD),         # Offset of Resource Table
                ("e32_rsrccnt", DWORD),         # Number of resource entries
                ("e32_restab", DWORD),          # Offset of resident name table
                ("e32_enttab", DWORD),          # Offset of Entry Table
                ("e32_dirtab", DWORD),          # Offset of Module Directive Table
                ("e32_dircnt", DWORD),          # Number of module directives
                ("e32_fpagetab", DWORD),        # Offset of Fixup Page Table
                ("e32_frectab", DWORD),         # Offset of Fixup Record Table
                ("e32_impmod", DWORD),          # Offset of Import Module Name Table
                ("e32_impmodcnt", DWORD),       # Number of entries in Import Module Name Table
                ("e32_impproc", DWORD),         # Offset of Import Procedure Name Table
                ("e32_pagesum", DWORD),         # Offset of Per-Page Checksum Table
                ("e32_datapage", DWORD),        # Offset of Enumerated Data Pages
                ("e32_preload", DWORD),         # Number of preload pages
                ("e32_nrestab", DWORD),         # Offset of Non-resident Names Table
                ("e32_cbnrestab", DWORD),       # Size of Non-resident Name Table
                ("e32_nressum", DWORD),         # Non-resident Name Table Checksum
                ("e32_autodata", DWORD),        # Object # for automatic data object
                ("e32_debuginfo", DWORD),       # Offset of the debugging information
                ("e32_debuglen", DWORD),        # The length of the debugging info. in bytes
                ("e32_instpreload", DWORD),     # Number of instance pages in preload section of VXD file
                ("e32_instdemand", DWORD),      # Number of instance pages in demand load section of VXD file
                ("e32_heapsize", DWORD),        # Size of heap - for 16-bit apps
                ("e32_res3", BYTE * 12),        # Reserved words
                ("e32_winresoff", DWORD),
                ("e32_winreslen", DWORD),
                ("e32_devid", DWORD),           # Device ID for VxD
                ("e32_ddkver", DWORD)           # DDK version for VxD
            ]
            
            e32_res3: IArray[BYTE]
            e32_lastpagesize: int
            e32_instpreload: int
            e32_instdemand: int
            e32_fixupsize: int
            e32_impmodcnt: int
            e32_cbnrestab: int
            e32_debuginfo: int
            e32_winresoff: int
            e32_winreslen: int
            e32_startobj: int
            e32_stackobj: int
            e32_pagesize: int
            e32_fixupsum: int
            e32_fpagetab: int
            e32_datapage: int
            e32_autodata: int
            e32_debuglen: int
            e32_heapsize: int
            e32_ldrsize: int
            e32_itermap: int
            e32_rsrctab: int
            e32_rsrccnt: int
            e32_frectab: int
            e32_impproc: int
            e32_pagesum: int
            e32_preload: int
            e32_nrestab: int
            e32_nressum: int
            e32_border: int
            e32_worder: int
            e32_mflags: int
            e32_mpages: int
            e32_ldrsum: int
            e32_objtab: int
            e32_objcnt: int
            e32_objmap: int
            e32_restab: int
            e32_enttab: int
            e32_dirtab: int
            e32_dircnt: int
            e32_impmod: int
            e32_ddkver: int
            e32_magic: int
            e32_level: int
            e32_devid: int
            e32_cpu: int
            e32_ver: int
            e32_eip: int
            e32_esp: int
            e32_os: int
            
        PIMAGE_VXD_HEADER = POINTER(IMAGE_VXD_HEADER)

        #
        # File header format.
        #

        class IMAGE_FILE_HEADER(CStructure):
            _fields_ = [
                ("Machine", WORD),
                ("NumberOfSections", WORD),
                ("TimeDateStamp", DWORD),
                ("PointerToSymbolTable", DWORD),
                ("NumberOfSymbols", DWORD),
                ("SizeOfOptionalHeader", WORD),
                ("Characteristics", WORD)
            ]
            
            PointerToSymbolTable: int
            SizeOfOptionalHeader: int
            NumberOfSections: int
            NumberOfSymbols: int
            Characteristics: int
            TimeDateStamp: int
            Machine: int
            
        PIMAGE_FILE_HEADER = POINTER(IMAGE_FILE_HEADER)

        IMAGE_SIZEOF_FILE_HEADER             = 20

        IMAGE_FILE_RELOCS_STRIPPED           = 0x0001  # Relocation info stripped from file.
        IMAGE_FILE_EXECUTABLE_IMAGE          = 0x0002  # File is executable  (i.e. no unresolved external references).
        IMAGE_FILE_LINE_NUMS_STRIPPED        = 0x0004  # Line nunbers stripped from file.
        IMAGE_FILE_LOCAL_SYMS_STRIPPED       = 0x0008  # Local symbols stripped from file.
        IMAGE_FILE_AGGRESIVE_WS_TRIM         = 0x0010  # Aggressively trim working set
        IMAGE_FILE_LARGE_ADDRESS_AWARE       = 0x0020  # App can handle >2gb addresses
        IMAGE_FILE_BYTES_REVERSED_LO         = 0x0080  # Bytes of machine word are reversed.
        IMAGE_FILE_32BIT_MACHINE             = 0x0100  # 32 bit word machine.
        IMAGE_FILE_DEBUG_STRIPPED            = 0x0200  # Debugging info stripped from file in .DBG file
        IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP   = 0x0400  # If Image is on removable media, copy and run from the swap file.
        IMAGE_FILE_NET_RUN_FROM_SWAP         = 0x0800  # If Image is on Net, copy and run from the swap file.
        IMAGE_FILE_SYSTEM                    = 0x1000  # System File.
        IMAGE_FILE_DLL                       = 0x2000  # File is a DLL.
        IMAGE_FILE_UP_SYSTEM_ONLY            = 0x4000  # File should only be run on a UP machine
        IMAGE_FILE_BYTES_REVERSED_HI         = 0x8000  # Bytes of machine word are reversed.

        IMAGE_FILE_MACHINE_UNKNOWN           = 0
        IMAGE_FILE_MACHINE_TARGET_HOST       = 0x0001  # Useful for indicating we want to interact with the host and not a WoW guest.
        IMAGE_FILE_MACHINE_I386              = 0x014c  # Intel 386.
        IMAGE_FILE_MACHINE_R3000             = 0x0162  # MIPS little-endian, 0x160 big-endian
        IMAGE_FILE_MACHINE_R4000             = 0x0166  # MIPS little-endian
        IMAGE_FILE_MACHINE_R10000            = 0x0168  # MIPS little-endian
        IMAGE_FILE_MACHINE_WCEMIPSV2         = 0x0169  # MIPS little-endian WCE v2
        IMAGE_FILE_MACHINE_ALPHA             = 0x0184  # Alpha_AXP
        IMAGE_FILE_MACHINE_SH3               = 0x01a2  # SH3 little-endian
        IMAGE_FILE_MACHINE_SH3DSP            = 0x01a3
        IMAGE_FILE_MACHINE_SH3E              = 0x01a4  # SH3E little-endian
        IMAGE_FILE_MACHINE_SH4               = 0x01a6  # SH4 little-endian
        IMAGE_FILE_MACHINE_SH5               = 0x01a8  # SH5
        IMAGE_FILE_MACHINE_ARM               = 0x01c0  # ARM Little-Endian
        IMAGE_FILE_MACHINE_THUMB             = 0x01c2  # ARM Thumb/Thumb-2 Little-Endian
        IMAGE_FILE_MACHINE_ARMNT             = 0x01c4  # ARM Thumb-2 Little-Endian
        IMAGE_FILE_MACHINE_AM33              = 0x01d3
        IMAGE_FILE_MACHINE_POWERPC           = 0x01F0  # IBM PowerPC Little-Endian
        IMAGE_FILE_MACHINE_POWERPCFP         = 0x01f1
        IMAGE_FILE_MACHINE_IA64              = 0x0200  # Intel 64
        IMAGE_FILE_MACHINE_MIPS16            = 0x0266  # MIPS
        IMAGE_FILE_MACHINE_ALPHA64           = 0x0284  # ALPHA64
        IMAGE_FILE_MACHINE_MIPSFPU           = 0x0366  # MIPS
        IMAGE_FILE_MACHINE_MIPSFPU16         = 0x0466  # MIPS
        IMAGE_FILE_MACHINE_AXP64             = IMAGE_FILE_MACHINE_ALPHA64
        IMAGE_FILE_MACHINE_TRICORE           = 0x0520  # Infineon
        IMAGE_FILE_MACHINE_CEF               = 0x0CEF
        IMAGE_FILE_MACHINE_EBC               = 0x0EBC  # EFI Byte Code
        IMAGE_FILE_MACHINE_AMD64             = 0x8664  # AMD64 (K8)
        IMAGE_FILE_MACHINE_M32R              = 0x9041  # M32R little-endian
        IMAGE_FILE_MACHINE_ARM64             = 0xAA64  # ARM64 Little-Endian
        IMAGE_FILE_MACHINE_CEE               = 0xC0EE

        #
        # Directory format.
        #

        class IMAGE_DATA_DIRECTORY(CStructure):
            _fields_ = [
                ("VirtualAddress", DWORD),
                ("Size", DWORD)
            ]
            
            VirtualAddress: int
            Size: int
            
        PIMAGE_DATA_DIRECTORY = POINTER(IMAGE_DATA_DIRECTORY)

        IMAGE_NUMBEROF_DIRECTORY_ENTRIES = 16

        #
        # Optional header format.
        #

        class IMAGE_OPTIONAL_HEADER32(CStructure):
            _fields_ = [
                #
                # Standard fields.
                #
                ("Magic", WORD),
                ("MajorLinkerVersion", BYTE),
                ("MinorLinkerVersion", BYTE),
                ("SizeOfCode", DWORD),
                ("SizeOfInitializedData", DWORD),
                ("SizeOfUninitializedData", DWORD),
                ("AddressOfEntryPoint", DWORD),
                ("BaseOfCode", DWORD),
                ("BaseOfData", DWORD),

                #
                # NT additional fields.
                #
                ("ImageBase", DWORD),
                ("SectionAlignment", DWORD),
                ("FileAlignment", DWORD),
                ("MajorOperatingSystemVersion", WORD),
                ("MinorOperatingSystemVersion", WORD),
                ("MajorImageVersion", WORD),
                ("MinorImageVersion", WORD),
                ("MajorSubsystemVersion", WORD),
                ("MinorSubsystemVersion", WORD),
                ("Win32VersionValue", DWORD),
                ("SizeOfImage", DWORD),
                ("SizeOfHeaders", DWORD),
                ("CheckSum", DWORD),
                ("Subsystem", WORD),
                ("DllCharacteristics", WORD),
                ("SizeOfStackReserve", DWORD),
                ("SizeOfStackCommit", DWORD),
                ("SizeOfHeapReserve", DWORD),
                ("SizeOfHeapCommit", DWORD),
                ("LoaderFlags", DWORD),
                ("NumberOfRvaAndSizes", DWORD),
                ("DataDirectory", IMAGE_DATA_DIRECTORY * IMAGE_NUMBEROF_DIRECTORY_ENTRIES)
            ]
            
            DataDirectory: IPointer[IMAGE_DATA_DIRECTORY]
            MajorOperatingSystemVersion: int
            MinorOperatingSystemVersion: int
            SizeOfUninitializedData: int
            SizeOfInitializedData: int
            MajorSubsystemVersion: int
            MinorSubsystemVersion: int
            AddressOfEntryPoint: int
            NumberOfRvaAndSizes: int
            MajorLinkerVersion: int
            MinorLinkerVersion: int
            DllCharacteristics: int
            SizeOfStackReserve: int
            MajorImageVersion: int
            MinorImageVersion: int
            Win32VersionValue: int
            SizeOfStackCommit: int
            SizeOfHeapReserve: int
            SectionAlignment: int
            SizeOfHeapCommit: int
            FileAlignment: int
            SizeOfHeaders: int
            SizeOfImage: int
            LoaderFlags: int
            SizeOfCode: int
            BaseOfCode: int
            BaseOfData: int
            ImageBase: int
            Subsystem: int
            CheckSum: int
            Magic: int
            
        PIMAGE_OPTIONAL_HEADER32 = POINTER(IMAGE_OPTIONAL_HEADER32)

        class IMAGE_ROM_OPTIONAL_HEADER(CStructure):
            _fields_ = [
                ("Magic", WORD),
                ("MajorLinkerVersion", BYTE),
                ("MinorLinkerVersion", BYTE),
                ("SizeOfCode", DWORD),
                ("SizeOfInitializedData", DWORD),
                ("SizeOfUninitializedData", DWORD),
                ("AddressOfEntryPoint", DWORD),
                ("BaseOfCode", DWORD),
                ("BaseOfData", DWORD),
                ("BaseOfBss", DWORD),
                ("GprMask", DWORD),
                ("CprMask", DWORD * 4),
                ("GpValue", DWORD)
            ]
            
            SizeOfUninitializedData: int
            SizeOfInitializedData: int
            AddressOfEntryPoint: int
            MajorLinkerVersion: int
            MinorLinkerVersion: int
            CprMask: IArray[DWORD]
            SizeOfCode: int
            BaseOfCode: int
            BaseOfData: int
            BaseOfBss: int
            GprMask: int
            GpValue: int
            Magic: int
            
        PIMAGE_ROM_OPTIONAL_HEADER = POINTER(IMAGE_ROM_OPTIONAL_HEADER)

        class IMAGE_OPTIONAL_HEADER64(CStructure):
            _fields_ = [
                #
                # Standard fields.
                #
                ("Magic", WORD),
                ("MajorLinkerVersion", BYTE),
                ("MinorLinkerVersion", BYTE),
                ("SizeOfCode", DWORD),
                ("SizeOfInitializedData", DWORD),
                ("SizeOfUninitializedData", DWORD),
                ("AddressOfEntryPoint", DWORD),
                ("BaseOfCode", DWORD),

                #
                # NT additional fields.
                #
                ("ImageBase", ULONGLONG),
                ("SectionAlignment", DWORD),
                ("FileAlignment", DWORD),
                ("MajorOperatingSystemVersion", WORD),
                ("MinorOperatingSystemVersion", WORD),
                ("MajorImageVersion", WORD),
                ("MinorImageVersion", WORD),
                ("MajorSubsystemVersion", WORD),
                ("MinorSubsystemVersion", WORD),
                ("Win32VersionValue", DWORD),
                ("SizeOfImage", DWORD),
                ("SizeOfHeaders", DWORD),
                ("CheckSum", DWORD),
                ("Subsystem", WORD),
                ("DllCharacteristics", WORD),
                ("SizeOfStackReserve", ULONGLONG),
                ("SizeOfStackCommit", ULONGLONG),
                ("SizeOfHeapReserve", ULONGLONG),
                ("SizeOfHeapCommit", ULONGLONG),
                ("LoaderFlags", DWORD),
                ("NumberOfRvaAndSizes", DWORD),
                ("DataDirectory", IMAGE_DATA_DIRECTORY * IMAGE_NUMBEROF_DIRECTORY_ENTRIES)
            ]
            
            DataDirectory: IArray[IMAGE_DATA_DIRECTORY]
            MajorOperatingSystemVersion: int
            MinorOperatingSystemVersion: int
            SizeOfUninitializedData: int
            SizeOfInitializedData: int
            MajorSubsystemVersion: int
            MinorSubsystemVersion: int
            AddressOfEntryPoint: int
            NumberOfRvaAndSizes: int
            MajorLinkerVersion: int
            MinorLinkerVersion: int
            DllCharacteristics: int
            SizeOfStackReserve: int
            MajorImageVersion: int
            MinorImageVersion: int
            Win32VersionValue: int
            SizeOfStackCommit: int
            SizeOfHeapReserve: int
            SectionAlignment: int
            SizeOfHeapCommit: int
            FileAlignment: int
            SizeOfHeaders: int
            SizeOfImage: int
            LoaderFlags: int
            SizeOfCode: int
            BaseOfCode: int
            ImageBase: int
            Subsystem: int
            CheckSum: int
            Magic: int
            
        PIMAGE_OPTIONAL_HEADER64 = POINTER(IMAGE_OPTIONAL_HEADER64)

        IMAGE_NT_OPTIONAL_HDR32_MAGIC      = 0x10b
        IMAGE_NT_OPTIONAL_HDR64_MAGIC      = 0x20b
        IMAGE_ROM_OPTIONAL_HDR_MAGIC       = 0x107

        class IMAGE_NT_HEADERS64(CStructure):
            _fields_ = [
                ("Signature", DWORD),
                ("FileHeader", IMAGE_FILE_HEADER),
                ("OptionalHeader", IMAGE_OPTIONAL_HEADER64)
            ]
            
            OptionalHeader: IMAGE_OPTIONAL_HEADER64
            FileHeader: IMAGE_FILE_HEADER
            Signature: int
            
        PIMAGE_NT_HEADERS64 = POINTER(IMAGE_NT_HEADERS64)

        class IMAGE_NT_HEADERS32(CStructure):
            _fields_ = [
                ("Signature", DWORD),
                ("FileHeader", IMAGE_FILE_HEADER),
                ("OptionalHeader", IMAGE_OPTIONAL_HEADER32)
            ]
            
            OptionalHeader: IMAGE_OPTIONAL_HEADER32
            FileHeader: IMAGE_FILE_HEADER
            Signature: int
            
        PIMAGE_NT_HEADERS32 = POINTER(IMAGE_NT_HEADERS32)
        IMAGE_NT_HEADERS = IMAGE_NT_HEADERS32

        class IMAGE_ROM_HEADERS(CStructure):
            _fields_ = [
                ("FileHeader", IMAGE_FILE_HEADER),
                ("OptionalHeader", IMAGE_ROM_OPTIONAL_HEADER)
            ]
            
            OptionalHeader: IMAGE_ROM_OPTIONAL_HEADER
            FileHeader: IMAGE_FILE_HEADER
            
        PIMAGE_ROM_HEADERS = POINTER(IMAGE_ROM_HEADERS)

        import typing as t

        # IMAGE_FIRST_SECTION doesn't need 32/64 versions since the file header is the same either way.

        def IMAGE_FIRST_SECTION(ntheader: IPointer[t.Union[IMAGE_NT_HEADERS32, IMAGE_NT_HEADERS64]]):
            ntheader_addr = cast(ntheader, PVOID).value
            return ntheader_addr + FIELD_OFFSET(IMAGE_NT_HEADERS32, "OptionalHeader") + ntheader.contents.FileHeader.SizeOfOptionalHeader

        # Subsystem Values

        IMAGE_SUBSYSTEM_UNKNOWN              = 0   # Unknown subsystem.
        IMAGE_SUBSYSTEM_NATIVE               = 1   # Image doesn't require a subsystem.
        IMAGE_SUBSYSTEM_WINDOWS_GUI          = 2   # Image runs in the Windows GUI subsystem.
        IMAGE_SUBSYSTEM_WINDOWS_CUI          = 3   # Image runs in the Windows character subsystem.
        IMAGE_SUBSYSTEM_OS2_CUI              = 5   # image runs in the OS/2 character subsystem.
        IMAGE_SUBSYSTEM_POSIX_CUI            = 7   # image runs in the Posix character subsystem.
        IMAGE_SUBSYSTEM_NATIVE_WINDOWS       = 8   # image is a native Win9x driver.
        IMAGE_SUBSYSTEM_WINDOWS_CE_GUI       = 9   # Image runs in the Windows CE subsystem.
        IMAGE_SUBSYSTEM_EFI_APPLICATION      = 10  #
        IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER  = 11   #
        IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER   = 12  #
        IMAGE_SUBSYSTEM_EFI_ROM              = 13
        IMAGE_SUBSYSTEM_XBOX                 = 14
        IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION = 16
        IMAGE_SUBSYSTEM_XBOX_CODE_CATALOG    = 17

        # DllCharacteristics Entries

        IMAGE_LIBRARY_PROCESS_INIT           = 0x0001     # Reserved.
        IMAGE_LIBRARY_PROCESS_TERM           = 0x0002      # Reserved.
        IMAGE_LIBRARY_THREAD_INIT            = 0x0004      # Reserved.
        IMAGE_LIBRARY_THREAD_TERM            = 0x0008      # Reserved.
        IMAGE_DLLCHARACTERISTICS_HIGH_ENTROPY_VA = 0x0020  # Image can handle a high entropy = 64-bit virtual address space.
        IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE = 0x0040     # DLL can move.
        IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY    = 0x0080     # Code Integrity Image
        IMAGE_DLLCHARACTERISTICS_NX_COMPAT    = 0x0100     # Image is NX compatible
        IMAGE_DLLCHARACTERISTICS_NO_ISOLATION = 0x0200     # Image understands isolation and doesn't want it
        IMAGE_DLLCHARACTERISTICS_NO_SEH       = 0x0400     # Image does not use SEH.  No SE handler may reside in this image
        IMAGE_DLLCHARACTERISTICS_NO_BIND      = 0x0800     # Do not bind this image.
        IMAGE_DLLCHARACTERISTICS_APPCONTAINER = 0x1000     # Image should execute in an AppContainer
        IMAGE_DLLCHARACTERISTICS_WDM_DRIVER   = 0x2000     # Driver uses WDM model
        IMAGE_DLLCHARACTERISTICS_GUARD_CF     = 0x4000     # Image supports Control Flow Guard.
        IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE     = 0x8000

        # Directory Entries

        IMAGE_DIRECTORY_ENTRY_EXPORT          = 0   # Export Directory
        IMAGE_DIRECTORY_ENTRY_IMPORT          = 1   # Import Directory
        IMAGE_DIRECTORY_ENTRY_RESOURCE        = 2   # Resource Directory
        IMAGE_DIRECTORY_ENTRY_EXCEPTION       = 3   # Exception Directory
        IMAGE_DIRECTORY_ENTRY_SECURITY        = 4   # Security Directory
        IMAGE_DIRECTORY_ENTRY_BASERELOC       = 5   # Base Relocation Table
        IMAGE_DIRECTORY_ENTRY_DEBUG           = 6   # Debug Directory
        IMAGE_DIRECTORY_ENTRY_COPYRIGHT       = 7   # (X86 usage)
        IMAGE_DIRECTORY_ENTRY_ARCHITECTURE    = 7   # Architecture Specific Data
        IMAGE_DIRECTORY_ENTRY_GLOBALPTR       = 8   # RVA of GP
        IMAGE_DIRECTORY_ENTRY_TLS             = 9   # TLS Directory
        IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG    = 10   # Load Configuration Directory
        IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT   = 11   # Bound Import Directory in headers
        IMAGE_DIRECTORY_ENTRY_IAT            = 12   # Import Address Table
        IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT   = 13   # Delay Load Import Descriptors
        IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR = 14   # COM Runtime descriptor

        #
        # Non-COFF Object file header
        #

        from .guiddef import CLSID

        class ANON_OBJECT_HEADER(CStructure):
            _fields_ = [
                ("Sig1", WORD),            # Must be IMAGE_FILE_MACHINE_UNKNOWN
                ("Sig2", WORD),            # Must be 0xffff
                ("Version", WORD),         # >= 1 (implies the CLSID field is present)
                ("Machine", WORD),
                ("TimeDateStamp", DWORD),
                ("ClassID", CLSID),        # Used to invoke CoCreateInstance
                ("SizeOfData", DWORD)      # Size of data that follows the header
            ]

        class ANON_OBJECT_HEADER_V2(CStructure):
            _fields_ = [
                ("Sig1", WORD),            # Must be IMAGE_FILE_MACHINE_UNKNOWN
                ("Sig2", WORD),            # Must be 0xffff
                ("Version", WORD),         # >= 1 (implies the CLSID field is present)
                ("Machine", WORD),
                ("TimeDateStamp", DWORD),
                ("ClassID", CLSID),        # Used to invoke CoCreateInstance
                ("SizeOfData", DWORD),     # Size of data that follows the header
                ("Flags", DWORD),          # 0x1 -> contains metadata
                ("MetaDataSize", DWORD),   # Size of CLR metadata
                ("MetaDataOffset", DWORD)  # Offset of CLR metadata
            ]

        class ANON_OBJECT_HEADER_BIGOBJ(CStructure):
            _fields_ = [
                ("Sig1", WORD),              # Must be IMAGE_FILE_MACHINE_UNKNOWN
                ("Sig2", WORD),              # Must be 0xffff
                ("Version", WORD),           # >= 2 (implies the Flags field is present)
                ("Machine", WORD),           # Actual machine - IMAGE_FILE_MACHINE_xxx
                ("TimeDateStamp", DWORD),
                ("ClassID", CLSID),          # {D1BAA1C7-BAEE-4ba9-AF20-FAF66AA4DCB8}
                ("SizeOfData", DWORD),       # Size of data that follows the header
                ("Flags", DWORD),            # 0x1 -> contains metadata
                ("MetaDataSize", DWORD),     # Size of CLR metadata
                ("MetaDataOffset", DWORD),   # Offset of CLR metadata
                # bigobj specifics
                ("NumberOfSections", DWORD), # extended from WORD
                ("PointerToSymbolTable", DWORD),
                ("NumberOfSymbols", DWORD)
            ]

        #
        # Section header format.
        #

        IMAGE_SIZEOF_SHORT_NAME             = 8

        class IMAGE_SECTION_HEADER(CStructure):
            class _Misc(Union):
                _fields_ = [
                    ("PhysicalAddress", DWORD),
                    ("VirtualSize" , DWORD)
                ]
                
                PhysicalAddress: int
                VirtualSize: int
                
            _fields_ = [
                ("Name", CHAR * IMAGE_SIZEOF_SHORT_NAME),
                ("Misc", _Misc),
                ("VirtualAddress", DWORD),
                ("SizeOfRawData", DWORD),
                ("PointerToRawData", DWORD),
                ("PointerToRelocations", DWORD),
                ("PointerToLinenumbers", DWORD),
                ("NumberOfRelocations", WORD),
                ("NumberOfLinenumbers", WORD),
                ("Characteristics", DWORD)
            ]
            
            PointerToRelocations: int
            PointerToLinenumbers: int
            NumberOfRelocations: int
            NumberOfLinenumbers: int
            PointerToRawData: int
            Characteristics: int
            VirtualAddress: int
            SizeOfRawData: int
            Name: IArray[CHAR]
            Misc: _Misc
            
        PIMAGE_SECTION_HEADER = POINTER(IMAGE_SECTION_HEADER)

        #
        # Section characteristics.
        #
        IMAGE_SCN_TYPE_REG                  = 0x00000000  # Reserved.
        IMAGE_SCN_TYPE_DSECT                = 0x00000001  # Reserved.
        IMAGE_SCN_TYPE_NOLOAD               = 0x00000002  # Reserved.
        IMAGE_SCN_TYPE_GROUP                = 0x00000004  # Reserved.
        IMAGE_SCN_TYPE_NO_PAD = 0x00000008 # Reserved.
        IMAGE_SCN_TYPE_COPY                 = 0x00000010  # Reserved.
        IMAGE_SCN_CNT_CODE = 0x00000020 # Section contains code.
        IMAGE_SCN_CNT_INITIALIZED_DATA = 0x00000040 # Section contains initialized data.
        IMAGE_SCN_CNT_UNINITIALIZED_DATA = 0x00000080 # Section contains uninitialized data.
        IMAGE_SCN_LNK_OTHER = 0x00000100 # Reserved.
        IMAGE_SCN_LNK_INFO = 0x00000200 # Section contains comments or some other type of information.
        IMAGE_SCN_TYPE_OVER                 = 0x00000400  # Reserved.
        IMAGE_SCN_LNK_REMOVE = 0x00000800 # Section contents will not become part of image.
        IMAGE_SCN_LNK_COMDAT = 0x00001000 # Section contents comdat.
        #                                           0x00002000  # Reserved.
        #      IMAGE_SCN_MEM_PROTECTED - Obsolete   0x00004000
        IMAGE_SCN_NO_DEFER_SPEC_EXC = 0x00004000 # Reset speculative exceptions handling bits in the TLB entries for this section.
        IMAGE_SCN_GPREL = 0x00008000 # Section content can be accessed relative to GP
        IMAGE_SCN_MEM_FARDATA = 0x00008000
        #      IMAGE_SCN_MEM_SYSHEAP  - Obsolete    0x00010000
        IMAGE_SCN_MEM_PURGEABLE = 0x00020000
        IMAGE_SCN_MEM_16BIT = 0x00020000
        IMAGE_SCN_MEM_LOCKED = 0x00040000
        IMAGE_SCN_MEM_PRELOAD = 0x00080000
        IMAGE_SCN_ALIGN_1BYTES = 0x00100000 #
        IMAGE_SCN_ALIGN_2BYTES = 0x00200000 #
        IMAGE_SCN_ALIGN_4BYTES = 0x00300000 #
        IMAGE_SCN_ALIGN_8BYTES = 0x00400000 #
        IMAGE_SCN_ALIGN_16BYTES = 0x00500000 # Default alignment if no others are specified.
        IMAGE_SCN_ALIGN_32BYTES = 0x00600000 #
        IMAGE_SCN_ALIGN_64BYTES = 0x00700000 #
        IMAGE_SCN_ALIGN_128BYTES = 0x00800000 #
        IMAGE_SCN_ALIGN_256BYTES = 0x00900000 #
        IMAGE_SCN_ALIGN_512BYTES = 0x00A00000 #
        IMAGE_SCN_ALIGN_1024BYTES = 0x00B00000 #
        IMAGE_SCN_ALIGN_2048BYTES = 0x00C00000 #
        IMAGE_SCN_ALIGN_4096BYTES = 0x00D00000 #
        IMAGE_SCN_ALIGN_8192BYTES = 0x00E00000 #
        # Unused                                    0x00F00000
        IMAGE_SCN_ALIGN_MASK = 0x00F00000
        IMAGE_SCN_LNK_NRELOC_OVFL = 0x01000000 # Section contains extended relocations.
        IMAGE_SCN_MEM_DISCARDABLE = 0x02000000 # Section can be discarded.
        IMAGE_SCN_MEM_NOT_CACHED = 0x04000000 # Section is not cachable.
        IMAGE_SCN_MEM_NOT_PAGED = 0x08000000 # Section is not pageable.
        IMAGE_SCN_MEM_SHARED = 0x10000000 # Section is shareable.
        IMAGE_SCN_MEM_EXECUTE = 0x20000000 # Section is executable.
        IMAGE_SCN_MEM_READ = 0x40000000 # Section is readable.
        IMAGE_SCN_MEM_WRITE = 0x80000000 # Section is writeable.
        #
        # TLS Characteristic Flags
        #
        IMAGE_SCN_SCALE_INDEX = 0x00000001 # Tls index is scaled

        #
        # Symbol format.
        #

        class IMAGE_SYMBOL(CStructure):
            _pack_ = 2
            class _N(Union):
                _pack_ = 2
                class _Name(CStructure):
                    _pack_ = 2
                    _fields_ = [
                        ("Short", DWORD),     # if 0, use LongName
                        ("Long", DWORD),      # offset into string table
                    ]
                _fields_ = [
                    ("ShortName", CHAR * 8),
                    ("Name", _Name),
                    ("LongName", DWORD * 2)
                ]
            _fields_ = [
                ("N", _N),
                ("Value", DWORD),
                ("SectionNumber", SHORT),
                ("Type", WORD),
                ("StorageClass", BYTE),
                ("NumberOfAuxSymbols", BYTE)
            ]
        PIMAGE_SYMBOL = POINTER(IMAGE_SYMBOL)

        IMAGE_SIZEOF_SYMBOL                 = 18

        class IMAGE_SYMBOL_EX(CStructure):
            _pack_ = 2
            class _N(Union):
                _pack_ = 2
                class _Name(CStructure):
                    _pack_ = 2
                    _fields_ = [
                        ("Short", DWORD),     # if 0, use LongName
                        ("Long", DWORD),      # offset into string table
                    ]
                _fields_ = [
                    ("ShortName", CHAR * 8),
                    ("Name", _Name),
                    ("LongName", DWORD * 2)
                ]
            _fields_ = [
                ("N", _N),
                ("Value", DWORD),
                ("SectionNumber", LONG),
                ("Type", WORD),
                ("StorageClass", BYTE),
                ("NumberOfAuxSymbols", BYTE)
            ]
        PIMAGE_SYMBOL_EX = POINTER(IMAGE_SYMBOL_EX)

        #
        # Section values.
        #
        # Symbols have a section number of the section in which they are
        # defined. Otherwise, section numbers have the following meanings:
        #
        IMAGE_SYM_UNDEFINED = 0 # Symbol is undefined or is common.
        IMAGE_SYM_ABSOLUTE = -1 # Symbol is an absolute value.
        IMAGE_SYM_DEBUG = -2 # Symbol is a special debug item.
        IMAGE_SYM_SECTION_MAX = 0xFEFF # Values 0xFF00-0xFFFF are special
        IMAGE_SYM_SECTION_MAX_EX = MAXLONG
        #
        # Type (fundamental) values.
        #
        IMAGE_SYM_TYPE_NULL = 0x0000 # no type.
        IMAGE_SYM_TYPE_VOID = 0x0001 #
        IMAGE_SYM_TYPE_CHAR = 0x0002 # type character.
        IMAGE_SYM_TYPE_SHORT = 0x0003 # type short integer.
        IMAGE_SYM_TYPE_INT = 0x0004 #
        IMAGE_SYM_TYPE_LONG = 0x0005 #
        IMAGE_SYM_TYPE_FLOAT = 0x0006 #
        IMAGE_SYM_TYPE_DOUBLE = 0x0007 #
        IMAGE_SYM_TYPE_STRUCT = 0x0008 #
        IMAGE_SYM_TYPE_UNION = 0x0009 #
        IMAGE_SYM_TYPE_ENUM = 0x000A # enumeration.
        IMAGE_SYM_TYPE_MOE = 0x000B # member of enumeration.
        IMAGE_SYM_TYPE_BYTE = 0x000C #
        IMAGE_SYM_TYPE_WORD = 0x000D #
        IMAGE_SYM_TYPE_UINT = 0x000E #
        IMAGE_SYM_TYPE_DWORD = 0x000F #
        IMAGE_SYM_TYPE_PCODE = 0x8000 #
        #
        # Type (derived) values.
        #
        IMAGE_SYM_DTYPE_NULL = 0 # no derived type.
        IMAGE_SYM_DTYPE_POINTER = 1 # pointer.
        IMAGE_SYM_DTYPE_FUNCTION = 2 # function.
        IMAGE_SYM_DTYPE_ARRAY = 3 # array.
        #
        # Storage classes.
        #
        IMAGE_SYM_CLASS_END_OF_FUNCTION = BYTE(-1).value
        IMAGE_SYM_CLASS_NULL = 0x0000
        IMAGE_SYM_CLASS_AUTOMATIC = 0x0001
        IMAGE_SYM_CLASS_EXTERNAL = 0x0002
        IMAGE_SYM_CLASS_STATIC = 0x0003
        IMAGE_SYM_CLASS_REGISTER = 0x0004
        IMAGE_SYM_CLASS_EXTERNAL_DEF = 0x0005
        IMAGE_SYM_CLASS_LABEL = 0x0006
        IMAGE_SYM_CLASS_UNDEFINED_LABEL = 0x0007
        IMAGE_SYM_CLASS_MEMBER_OF_STRUCT = 0x0008
        IMAGE_SYM_CLASS_ARGUMENT = 0x0009
        IMAGE_SYM_CLASS_STRUCT_TAG = 0x000A
        IMAGE_SYM_CLASS_MEMBER_OF_UNION = 0x000B
        IMAGE_SYM_CLASS_UNION_TAG = 0x000C
        IMAGE_SYM_CLASS_TYPE_DEFINITION = 0x000D
        IMAGE_SYM_CLASS_UNDEFINED_STATIC = 0x000E
        IMAGE_SYM_CLASS_ENUM_TAG = 0x000F
        IMAGE_SYM_CLASS_MEMBER_OF_ENUM = 0x0010
        IMAGE_SYM_CLASS_REGISTER_PARAM = 0x0011
        IMAGE_SYM_CLASS_BIT_FIELD = 0x0012
        IMAGE_SYM_CLASS_FAR_EXTERNAL = 0x0044 #
        IMAGE_SYM_CLASS_BLOCK = 0x0064
        IMAGE_SYM_CLASS_FUNCTION = 0x0065
        IMAGE_SYM_CLASS_END_OF_STRUCT = 0x0066
        IMAGE_SYM_CLASS_FILE = 0x0067
        # new
        IMAGE_SYM_CLASS_SECTION = 0x0068
        IMAGE_SYM_CLASS_WEAK_EXTERNAL = 0x0069
        IMAGE_SYM_CLASS_CLR_TOKEN = 0x006B
        # type packing constants
        N_BTMASK = 0x000F
        N_TMASK = 0x0030
        N_TMASK1 = 0x00C0
        N_TMASK2 = 0x00F0
        N_BTSHFT = 4
        N_TSHIFT = 2
        # MACROS
        # Basic Type of  x
        BTYPE  = lambda x: ((x) & N_BTMASK)
        # Is x a pointer?
        ISPTR = lambda x: (((x) & N_TMASK) == (IMAGE_SYM_DTYPE_POINTER << N_BTSHFT))
        # Is x a function?
        ISFCN = lambda x: (((x) & N_TMASK) == (IMAGE_SYM_DTYPE_FUNCTION << N_BTSHFT))
        # Is x an array?
        ISARY = lambda x: (((x) & N_TMASK) == (IMAGE_SYM_DTYPE_ARRAY << N_BTSHFT))
        # Is x a structure, union, or enumeration TAG?
        ISTAG = lambda x: ((x)==IMAGE_SYM_CLASS_STRUCT_TAG or (x)==IMAGE_SYM_CLASS_UNION_TAG or (x)==IMAGE_SYM_CLASS_ENUM_TAG)
        INCREF = lambda x: ((((x)&~N_BTMASK)<<N_TSHIFT)|(IMAGE_SYM_DTYPE_POINTER<<N_BTSHFT)|((x)&N_BTMASK))
        DECREF = lambda x: ((((x)>>N_TSHIFT)&~N_BTMASK)|((x)&N_BTMASK))

        class IMAGE_AUX_SYMBOL_TOKEN_DEF(CStructure):
            _pack_ = 2
            _fields_ = [
                ("bAuxType", BYTE),                  # IMAGE_AUX_SYMBOL_TYPE
                ("bReserved", BYTE),                 # Must be 0
                ("SymbolTableIndex", DWORD),
                ("rgbReserved", BYTE * 12)           # Must be 0
            ]
        PIMAGE_AUX_SYMBOL_TOKEN_DEF = POINTER(IMAGE_AUX_SYMBOL_TOKEN_DEF)

        #
        # Auxiliary entry format.
        #

        class IMAGE_AUX_SYMBOL(CStructure):
            class _Sym(CStructure):
                class _Misc(Union):
                    class _LnSz(CStructure):
                        _fields_ = [
                            ("Linenumber", WORD),             # declaration line number
                            ("Size", WORD)                    # size of struct, union, or enum
                        ]
                    _fields_ = [
                        ("LnSz", _LnSz),
                        ("TotalSize", DWORD)
                    ]
                class _FcnAry(Union):
                    class _Function(CStructure):
                        # if ISFCN, tag, or .bb
                        _fields_ = [
                            ("PointerToLinenumber", DWORD),
                            ("PointerToNextFunction", DWORD)
                        ]
                    class _Array(CStructure):
                        # if ISARY, up to 4 dimen.
                        _fields_ = [
                            ("Dimension", WORD * 4)
                        ]
                _fields_ = [
                    ("TagIndex", DWORD),                      # struct, union, or enum tag index
                    ("Misc", _Misc),
                    ("FcnAry", _FcnAry),
                    ("TvIndex", WORD)                         # tv index
                ]
            class _File(CStructure):
                _fields_ = [
                    ("Name", CHAR * IMAGE_SIZEOF_SYMBOL)
                ]
            class _Section(CStructure):
                _fields_ = [
                    ("Length", DWORD),                        # section length
                    ("NumberOfRelocations", WORD),            # number of relocation entries
                    ("NumberOfLinenumbers", WORD),            # number of line numbers
                    ("CheckSum", DWORD),                      # checksum for communal
                    ("Number", SHORT),                        # section number to associate with
                    ("Selection", BYTE),                      # communal selection type
                    ("bReserved", BYTE),
                    ("HighNumber", SHORT)                     # high bits of the section number
                ]
            class _CRC(CStructure):
                _fields_ = [
                    ("crc", DWORD),
                    ("rgbReserved", BYTE * 16)
                ]
            _fields_ = [
                ("Sym", _Sym),
                ("File", _File),
                ("Section", _Section),
                ("TokenDef", IMAGE_AUX_SYMBOL_TOKEN_DEF),
                ("CRC", _CRC)
            ]
        PIMAGE_AUX_SYMBOL = POINTER(IMAGE_AUX_SYMBOL)

        class IMAGE_AUX_SYMBOL_EX(CStructure):
            class _Sym(CStructure):
                _fields_ = [
                    ("WeakDefaultSymIndex", DWORD),                       # the weak extern default symbol index
                    ("WeakSearchType", DWORD),
                    ("rgbReserved", BYTE * 12)
                ]
            class _File(CStructure):
                _fields_ = [
                    ("Name", CHAR * sizeof(IMAGE_SYMBOL_EX))
                ]
            class _Section(CStructure):
                _fields_ = [
                    ("Length", DWORD),                        # section length
                    ("NumberOfRelocations", WORD),            # number of relocation entries
                    ("NumberOfLinenumbers", WORD),            # number of line numbers
                    ("CheckSum", DWORD),                      # checksum for communal
                    ("Number", SHORT),                        # section number to associate with
                    ("Selection", BYTE),                      # communal selection type
                    ("bReserved", BYTE),
                    ("HighNumber", SHORT),                    # high bits of the section number
                    ("rgbReserved", BYTE * 2)
                ]
            class _DUMMYSTRUCTNAME(CStructure):
                _fields_ = [
                    ("TokenDef", IMAGE_AUX_SYMBOL_TOKEN_DEF),
                    ("rgbReserved", BYTE * 2)
                ]
            class _CRC(CStructure):
                _fields_ = [
                    ("crc", DWORD),
                    ("rgbReserved", BYTE * 16)
                ]
            _fields_ = [
                ("Sym", _Sym),
                ("File", _File),
                ("Section", _Section),
                ("s", _DUMMYSTRUCTNAME),
                ("CRC", _CRC)
            ]
        PIMAGE_AUX_SYMBOL_EX = POINTER(IMAGE_AUX_SYMBOL_EX)

        IMAGE_AUX_SYMBOL_TYPE = INT
        IMAGE_AUX_SYMBOL_TYPE_TOKEN_DEF = 1

        #
        # Communal selection types.
        #

        IMAGE_COMDAT_SELECT_NODUPLICATES   = 1
        IMAGE_COMDAT_SELECT_ANY            = 2
        IMAGE_COMDAT_SELECT_SAME_SIZE      = 3
        IMAGE_COMDAT_SELECT_EXACT_MATCH    = 4
        IMAGE_COMDAT_SELECT_ASSOCIATIVE    = 5
        IMAGE_COMDAT_SELECT_LARGEST        = 6
        IMAGE_COMDAT_SELECT_NEWEST         = 7

        IMAGE_WEAK_EXTERN_SEARCH_NOLIBRARY = 1
        IMAGE_WEAK_EXTERN_SEARCH_LIBRARY   = 2
        IMAGE_WEAK_EXTERN_SEARCH_ALIAS     = 3
        IMAGE_WEAK_EXTERN_ANTI_DEPENDENCY  = 4

        #
        # Relocation format.
        #

        class IMAGE_RELOCATION(CStructure):
            class _DUMMYUNIONNAME(CStructure):
                _fields_ = [
                    ("VirtualAddress", DWORD),
                    ("RelocCount", DWORD)             # Set to the real count when IMAGE_SCN_LNK_NRELOC_OVFL is set
                ]
            _fields_ = [
                ("u", _DUMMYUNIONNAME),
                ("SymbolTableIndex", DWORD),
                ("Type", WORD)
            ]
        PIMAGE_RELOCATION = POINTER(IMAGE_RELOCATION)

        #
        # I386 relocation types.
        #
        IMAGE_REL_I386_ABSOLUTE = 0x0000 # Reference is absolute, no relocation is necessary
        IMAGE_REL_I386_DIR16 = 0x0001 # Direct 16-bit reference to the symbols virtual address
        IMAGE_REL_I386_REL16 = 0x0002 # PC-relative 16-bit reference to the symbols virtual address
        IMAGE_REL_I386_DIR32 = 0x0006 # Direct 32-bit reference to the symbols virtual address
        IMAGE_REL_I386_DIR32NB = 0x0007 # Direct 32-bit reference to the symbols virtual address, base not included
        IMAGE_REL_I386_SEG12 = 0x0009 # Direct 16-bit reference to the segment-selector bits of a 32-bit virtual address
        IMAGE_REL_I386_SECTION = 0x000A
        IMAGE_REL_I386_SECREL = 0x000B
        IMAGE_REL_I386_TOKEN = 0x000C # clr token
        IMAGE_REL_I386_SECREL7 = 0x000D # 7 bit offset from base of section containing target
        IMAGE_REL_I386_REL32 = 0x0014 # PC-relative 32-bit reference to the symbols virtual address
        #
        # MIPS relocation types.
        #
        IMAGE_REL_MIPS_ABSOLUTE = 0x0000 # Reference is absolute, no relocation is necessary
        IMAGE_REL_MIPS_REFHALF = 0x0001
        IMAGE_REL_MIPS_REFWORD = 0x0002
        IMAGE_REL_MIPS_JMPADDR = 0x0003
        IMAGE_REL_MIPS_REFHI = 0x0004
        IMAGE_REL_MIPS_REFLO = 0x0005
        IMAGE_REL_MIPS_GPREL = 0x0006
        IMAGE_REL_MIPS_LITERAL = 0x0007
        IMAGE_REL_MIPS_SECTION = 0x000A
        IMAGE_REL_MIPS_SECREL = 0x000B
        IMAGE_REL_MIPS_SECRELLO = 0x000C # Low 16-bit section relative referemce (used for >32k TLS)
        IMAGE_REL_MIPS_SECRELHI = 0x000D # High 16-bit section relative reference (used for >32k TLS)
        IMAGE_REL_MIPS_TOKEN = 0x000E # clr token
        IMAGE_REL_MIPS_JMPADDR16 = 0x0010
        IMAGE_REL_MIPS_REFWORDNB = 0x0022
        IMAGE_REL_MIPS_PAIR = 0x0025
        #
        # Alpha Relocation types.
        #
        IMAGE_REL_ALPHA_ABSOLUTE = 0x0000
        IMAGE_REL_ALPHA_REFLONG = 0x0001
        IMAGE_REL_ALPHA_REFQUAD = 0x0002
        IMAGE_REL_ALPHA_GPREL32 = 0x0003
        IMAGE_REL_ALPHA_LITERAL = 0x0004
        IMAGE_REL_ALPHA_LITUSE = 0x0005
        IMAGE_REL_ALPHA_GPDISP = 0x0006
        IMAGE_REL_ALPHA_BRADDR = 0x0007
        IMAGE_REL_ALPHA_HINT = 0x0008
        IMAGE_REL_ALPHA_INLINE_REFLONG = 0x0009
        IMAGE_REL_ALPHA_REFHI = 0x000A
        IMAGE_REL_ALPHA_REFLO = 0x000B
        IMAGE_REL_ALPHA_PAIR = 0x000C
        IMAGE_REL_ALPHA_MATCH = 0x000D
        IMAGE_REL_ALPHA_SECTION = 0x000E
        IMAGE_REL_ALPHA_SECREL = 0x000F
        IMAGE_REL_ALPHA_REFLONGNB = 0x0010
        IMAGE_REL_ALPHA_SECRELLO = 0x0011 # Low 16-bit section relative reference
        IMAGE_REL_ALPHA_SECRELHI = 0x0012 # High 16-bit section relative reference
        IMAGE_REL_ALPHA_REFQ3 = 0x0013 # High 16 bits of 48 bit reference
        IMAGE_REL_ALPHA_REFQ2 = 0x0014 # Middle 16 bits of 48 bit reference
        IMAGE_REL_ALPHA_REFQ1 = 0x0015 # Low 16 bits of 48 bit reference
        IMAGE_REL_ALPHA_GPRELLO = 0x0016 # Low 16-bit GP relative reference
        IMAGE_REL_ALPHA_GPRELHI = 0x0017 # High 16-bit GP relative reference
        #
        # IBM PowerPC relocation types.
        #
        IMAGE_REL_PPC_ABSOLUTE = 0x0000 # NOP
        IMAGE_REL_PPC_ADDR64 = 0x0001 # 64-bit address
        IMAGE_REL_PPC_ADDR32 = 0x0002 # 32-bit address
        IMAGE_REL_PPC_ADDR24 = 0x0003 # 26-bit address, shifted left 2 (branch absolute)
        IMAGE_REL_PPC_ADDR16 = 0x0004 # 16-bit address
        IMAGE_REL_PPC_ADDR14 = 0x0005 # 16-bit address, shifted left 2 (load doubleword)
        IMAGE_REL_PPC_REL24 = 0x0006 # 26-bit PC-relative offset, shifted left 2 (branch relative)
        IMAGE_REL_PPC_REL14 = 0x0007 # 16-bit PC-relative offset, shifted left 2 (br cond relative)
        IMAGE_REL_PPC_TOCREL16 = 0x0008 # 16-bit offset from TOC base
        IMAGE_REL_PPC_TOCREL14 = 0x0009 # 16-bit offset from TOC base, shifted left 2 (load doubleword)
        IMAGE_REL_PPC_ADDR32NB = 0x000A # 32-bit addr w/o image base
        IMAGE_REL_PPC_SECREL = 0x000B # va of containing section (as in an image sectionhdr)
        IMAGE_REL_PPC_SECTION = 0x000C # sectionheader number
        IMAGE_REL_PPC_IFGLUE = 0x000D # substitute TOC restore instruction iff symbol is glue code
        IMAGE_REL_PPC_IMGLUE = 0x000E # symbol is glue code; virtual address is TOC restore instruction
        IMAGE_REL_PPC_SECREL16 = 0x000F # va of containing section (limited to 16 bits)
        IMAGE_REL_PPC_REFHI = 0x0010
        IMAGE_REL_PPC_REFLO = 0x0011
        IMAGE_REL_PPC_PAIR = 0x0012
        IMAGE_REL_PPC_SECRELLO = 0x0013 # Low 16-bit section relative reference (used for >32k TLS)
        IMAGE_REL_PPC_SECRELHI = 0x0014 # High 16-bit section relative reference (used for >32k TLS)
        IMAGE_REL_PPC_GPREL = 0x0015
        IMAGE_REL_PPC_TOKEN = 0x0016 # clr token
        IMAGE_REL_PPC_TYPEMASK = 0x00FF # mask to isolate above values in IMAGE_RELOCATION.Type
        # Flag bits in IMAGE_RELOCATION.TYPE
        IMAGE_REL_PPC_NEG = 0x0100 # subtract reloc value rather than adding it
        IMAGE_REL_PPC_BRTAKEN = 0x0200 # fix branch prediction bit to predict branch taken
        IMAGE_REL_PPC_BRNTAKEN = 0x0400 # fix branch prediction bit to predict branch not taken
        IMAGE_REL_PPC_TOCDEFN = 0x0800 # toc slot defined in file (or, data in toc)
        #
        # Hitachi SH3 relocation types.
        #
        IMAGE_REL_SH3_ABSOLUTE = 0x0000 # No relocation
        IMAGE_REL_SH3_DIRECT16 = 0x0001 # 16 bit direct
        IMAGE_REL_SH3_DIRECT32 = 0x0002 # 32 bit direct
        IMAGE_REL_SH3_DIRECT8 = 0x0003 # 8 bit direct, -128..255
        IMAGE_REL_SH3_DIRECT8_WORD = 0x0004 # 8 bit direct .W (0 ext.)
        IMAGE_REL_SH3_DIRECT8_LONG = 0x0005 # 8 bit direct .L (0 ext.)
        IMAGE_REL_SH3_DIRECT4 = 0x0006 # 4 bit direct (0 ext.)
        IMAGE_REL_SH3_DIRECT4_WORD = 0x0007 # 4 bit direct .W (0 ext.)
        IMAGE_REL_SH3_DIRECT4_LONG = 0x0008 # 4 bit direct .L (0 ext.)
        IMAGE_REL_SH3_PCREL8_WORD = 0x0009 # 8 bit PC relative .W
        IMAGE_REL_SH3_PCREL8_LONG = 0x000A # 8 bit PC relative .L
        IMAGE_REL_SH3_PCREL12_WORD = 0x000B # 12 LSB PC relative .W
        IMAGE_REL_SH3_STARTOF_SECTION = 0x000C # Start of EXE section
        IMAGE_REL_SH3_SIZEOF_SECTION = 0x000D # Size of EXE section
        IMAGE_REL_SH3_SECTION = 0x000E # Section table index
        IMAGE_REL_SH3_SECREL = 0x000F # Offset within section
        IMAGE_REL_SH3_DIRECT32_NB = 0x0010 # 32 bit direct not based
        IMAGE_REL_SH3_GPREL4_LONG = 0x0011 # GP-relative addressing
        IMAGE_REL_SH3_TOKEN = 0x0012 # clr token
        IMAGE_REL_SHM_PCRELPT = 0x0013 # Offset from current
        #  instruction in longwords
        #  if not NOMODE, insert the
        #  inverse of the low bit at
        #  bit 32 to select PTA/PTB
        IMAGE_REL_SHM_REFLO = 0x0014 # Low bits of 32-bit address
        IMAGE_REL_SHM_REFHALF = 0x0015 # High bits of 32-bit address
        IMAGE_REL_SHM_RELLO = 0x0016 # Low bits of relative reference
        IMAGE_REL_SHM_RELHALF = 0x0017 # High bits of relative reference
        IMAGE_REL_SHM_PAIR = 0x0018 # offset operand for relocation
        IMAGE_REL_SH_NOMODE = 0x8000 # relocation ignores section mode
        IMAGE_REL_ARM_ABSOLUTE = 0x0000 # No relocation required
        IMAGE_REL_ARM_ADDR32 = 0x0001 # 32 bit address
        IMAGE_REL_ARM_ADDR32NB = 0x0002 # 32 bit address w/o image base
        IMAGE_REL_ARM_BRANCH24 = 0x0003 # 24 bit offset << 2 & sign ext.
        IMAGE_REL_ARM_BRANCH11 = 0x0004 # Thumb: 2 11 bit offsets
        IMAGE_REL_ARM_TOKEN = 0x0005 # clr token
        IMAGE_REL_ARM_GPREL12 = 0x0006 # GP-relative addressing (ARM)
        IMAGE_REL_ARM_GPREL7 = 0x0007 # GP-relative addressing (Thumb)
        IMAGE_REL_ARM_BLX24 = 0x0008
        IMAGE_REL_ARM_BLX11 = 0x0009
        IMAGE_REL_ARM_SECTION = 0x000E # Section table index
        IMAGE_REL_ARM_SECREL = 0x000F # Offset within section
        IMAGE_REL_ARM_MOV32A = 0x0010 # ARM: MOVW/MOVT
        IMAGE_REL_ARM_MOV32 = 0x0010 # ARM: MOVW/MOVT (deprecated)
        IMAGE_REL_ARM_MOV32T = 0x0011 # Thumb: MOVW/MOVT
        IMAGE_REL_THUMB_MOV32 = 0x0011 # Thumb: MOVW/MOVT (deprecated)
        IMAGE_REL_ARM_BRANCH20T = 0x0012 # Thumb: 32-bit conditional B
        IMAGE_REL_THUMB_BRANCH20 = 0x0012 # Thumb: 32-bit conditional B (deprecated)
        IMAGE_REL_ARM_BRANCH24T = 0x0014 # Thumb: 32-bit B or BL
        IMAGE_REL_THUMB_BRANCH24 = 0x0014 # Thumb: 32-bit B or BL (deprecated)
        IMAGE_REL_ARM_BLX23T = 0x0015 # Thumb: BLX immediate
        IMAGE_REL_THUMB_BLX23 = 0x0015 # Thumb: BLX immediate (deprecated)
        IMAGE_REL_AM_ABSOLUTE = 0x0000
        IMAGE_REL_AM_ADDR32 = 0x0001
        IMAGE_REL_AM_ADDR32NB = 0x0002
        IMAGE_REL_AM_CALL32 = 0x0003
        IMAGE_REL_AM_FUNCINFO = 0x0004
        IMAGE_REL_AM_REL32_1 = 0x0005
        IMAGE_REL_AM_REL32_2 = 0x0006
        IMAGE_REL_AM_SECREL = 0x0007
        IMAGE_REL_AM_SECTION = 0x0008
        IMAGE_REL_AM_TOKEN = 0x0009
        #
        # ARM64 relocations types.
        #
        IMAGE_REL_ARM64_ABSOLUTE = 0x0000 # No relocation required
        IMAGE_REL_ARM64_ADDR32 = 0x0001 # 32 bit address. Review! do we need it?
        IMAGE_REL_ARM64_ADDR32NB = 0x0002 # 32 bit address w/o image base (RVA: for Data/PData/XData)
        IMAGE_REL_ARM64_BRANCH26 = 0x0003 # 26 bit offset << 2 & sign ext. for B & BL
        IMAGE_REL_ARM64_PAGEBASE_REL21 = 0x0004 # ADRP
        IMAGE_REL_ARM64_REL21 = 0x0005 # ADR
        IMAGE_REL_ARM64_PAGEOFFSET_12A = 0x0006 # ADD/ADDS (immediate) with zero shift, for page offset
        IMAGE_REL_ARM64_PAGEOFFSET_12L = 0x0007 # LDR (indexed, unsigned immediate), for page offset
        IMAGE_REL_ARM64_SECREL = 0x0008 # Offset within section
        IMAGE_REL_ARM64_SECREL_LOW12A = 0x0009 # ADD/ADDS (immediate) with zero shift, for bit 0:11 of section offset
        IMAGE_REL_ARM64_SECREL_HIGH12A = 0x000A # ADD/ADDS (immediate) with zero shift, for bit 12:23 of section offset
        IMAGE_REL_ARM64_SECREL_LOW12L = 0x000B # LDR (indexed, unsigned immediate), for bit 0:11 of section offset
        IMAGE_REL_ARM64_TOKEN = 0x000C
        IMAGE_REL_ARM64_SECTION = 0x000D # Section table index
        IMAGE_REL_ARM64_ADDR64 = 0x000E # 64 bit address
        IMAGE_REL_ARM64_BRANCH19 = 0x000F # 19 bit offset << 2 & sign ext. for conditional B
        #
        # x64 relocations
        #
        IMAGE_REL_AMD64_ABSOLUTE = 0x0000 # Reference is absolute, no relocation is necessary
        IMAGE_REL_AMD64_ADDR64 = 0x0001 # 64-bit address (VA).
        IMAGE_REL_AMD64_ADDR32 = 0x0002 # 32-bit address (VA).
        IMAGE_REL_AMD64_ADDR32NB = 0x0003 # 32-bit address w/o image base (RVA).
        IMAGE_REL_AMD64_REL32 = 0x0004 # 32-bit relative address from byte following reloc
        IMAGE_REL_AMD64_REL32_1 = 0x0005 # 32-bit relative address from byte distance 1 from reloc
        IMAGE_REL_AMD64_REL32_2 = 0x0006 # 32-bit relative address from byte distance 2 from reloc
        IMAGE_REL_AMD64_REL32_3 = 0x0007 # 32-bit relative address from byte distance 3 from reloc
        IMAGE_REL_AMD64_REL32_4 = 0x0008 # 32-bit relative address from byte distance 4 from reloc
        IMAGE_REL_AMD64_REL32_5 = 0x0009 # 32-bit relative address from byte distance 5 from reloc
        IMAGE_REL_AMD64_SECTION = 0x000A # Section index
        IMAGE_REL_AMD64_SECREL = 0x000B # 32 bit offset from base of section containing target
        IMAGE_REL_AMD64_SECREL7 = 0x000C # 7 bit unsigned offset from base of section containing target
        IMAGE_REL_AMD64_TOKEN = 0x000D # 32 bit metadata token
        IMAGE_REL_AMD64_SREL32 = 0x000E # 32 bit signed span-dependent value emitted into object
        IMAGE_REL_AMD64_PAIR = 0x000F
        IMAGE_REL_AMD64_SSPAN32 = 0x0010 # 32 bit signed span-dependent value applied at link time
        IMAGE_REL_AMD64_EHANDLER = 0x0011
        IMAGE_REL_AMD64_IMPORT_BR = 0x0012 # Indirect branch to an import
        IMAGE_REL_AMD64_IMPORT_CALL = 0x0013 # Indirect call to an import
        IMAGE_REL_AMD64_CFG_BR = 0x0014 # Indirect branch to a CFG check
        IMAGE_REL_AMD64_CFG_BR_REX = 0x0015 # Indirect branch to a CFG check, with REX.W prefix
        IMAGE_REL_AMD64_CFG_CALL = 0x0016 # Indirect call to a CFG check
        IMAGE_REL_AMD64_INDIR_BR = 0x0017 # Indirect branch to a target in RAX (no CFG)
        IMAGE_REL_AMD64_INDIR_BR_REX = 0x0018 # Indirect branch to a target in RAX, with REX.W prefix (no CFG)
        IMAGE_REL_AMD64_INDIR_CALL = 0x0019 # Indirect call to a target in RAX (no CFG)
        IMAGE_REL_AMD64_INDIR_BR_SWITCHTABLE_FIRST = 0x0020 # Indirect branch for a switch table using Reg 0 (RAX)
        IMAGE_REL_AMD64_INDIR_BR_SWITCHTABLE_LAST = 0x002F # Indirect branch for a switch table using Reg 15 (R15)
        #
        # IA64 relocation types.
        #
        IMAGE_REL_IA64_ABSOLUTE = 0x0000
        IMAGE_REL_IA64_IMM14 = 0x0001
        IMAGE_REL_IA64_IMM22 = 0x0002
        IMAGE_REL_IA64_IMM64 = 0x0003
        IMAGE_REL_IA64_DIR32 = 0x0004
        IMAGE_REL_IA64_DIR64 = 0x0005
        IMAGE_REL_IA64_PCREL21B = 0x0006
        IMAGE_REL_IA64_PCREL21M = 0x0007
        IMAGE_REL_IA64_PCREL21F = 0x0008
        IMAGE_REL_IA64_GPREL22 = 0x0009
        IMAGE_REL_IA64_LTOFF22 = 0x000A
        IMAGE_REL_IA64_SECTION = 0x000B
        IMAGE_REL_IA64_SECREL22 = 0x000C
        IMAGE_REL_IA64_SECREL64I = 0x000D
        IMAGE_REL_IA64_SECREL32 = 0x000E
        #
        IMAGE_REL_IA64_DIR32NB = 0x0010
        IMAGE_REL_IA64_SREL14 = 0x0011
        IMAGE_REL_IA64_SREL22 = 0x0012
        IMAGE_REL_IA64_SREL32 = 0x0013
        IMAGE_REL_IA64_UREL32 = 0x0014
        IMAGE_REL_IA64_PCREL60X = 0x0015 # This is always a BRL and never converted
        IMAGE_REL_IA64_PCREL60B = 0x0016 # If possible, convert to MBB bundle with NOP.B in slot 1
        IMAGE_REL_IA64_PCREL60F = 0x0017 # If possible, convert to MFB bundle with NOP.F in slot 1
        IMAGE_REL_IA64_PCREL60I = 0x0018 # If possible, convert to MIB bundle with NOP.I in slot 1
        IMAGE_REL_IA64_PCREL60M = 0x0019 # If possible, convert to MMB bundle with NOP.M in slot 1
        IMAGE_REL_IA64_IMMGPREL64 = 0x001A
        IMAGE_REL_IA64_TOKEN = 0x001B # clr token
        IMAGE_REL_IA64_GPREL32 = 0x001C
        IMAGE_REL_IA64_ADDEND = 0x001F
        #
        # CEF relocation types.
        #
        IMAGE_REL_CEF_ABSOLUTE = 0x0000 # Reference is absolute, no relocation is necessary
        IMAGE_REL_CEF_ADDR32 = 0x0001 # 32-bit address (VA).
        IMAGE_REL_CEF_ADDR64 = 0x0002 # 64-bit address (VA).
        IMAGE_REL_CEF_ADDR32NB = 0x0003 # 32-bit address w/o image base (RVA).
        IMAGE_REL_CEF_SECTION = 0x0004 # Section index
        IMAGE_REL_CEF_SECREL = 0x0005 # 32 bit offset from base of section containing target
        IMAGE_REL_CEF_TOKEN = 0x0006 # 32 bit metadata token
        #
        # clr relocation types.
        #
        IMAGE_REL_CEE_ABSOLUTE = 0x0000 # Reference is absolute, no relocation is necessary
        IMAGE_REL_CEE_ADDR32 = 0x0001 # 32-bit address (VA).
        IMAGE_REL_CEE_ADDR64 = 0x0002 # 64-bit address (VA).
        IMAGE_REL_CEE_ADDR32NB = 0x0003 # 32-bit address w/o image base (RVA).
        IMAGE_REL_CEE_SECTION = 0x0004 # Section index
        IMAGE_REL_CEE_SECREL = 0x0005 # 32 bit offset from base of section containing target
        IMAGE_REL_CEE_TOKEN = 0x0006 # 32 bit metadata token
        IMAGE_REL_M32R_ABSOLUTE = 0x0000 # No relocation required
        IMAGE_REL_M32R_ADDR32 = 0x0001 # 32 bit address
        IMAGE_REL_M32R_ADDR32NB = 0x0002 # 32 bit address w/o image base
        IMAGE_REL_M32R_ADDR24 = 0x0003 # 24 bit address
        IMAGE_REL_M32R_GPREL16 = 0x0004 # GP relative addressing
        IMAGE_REL_M32R_PCREL24 = 0x0005 # 24 bit offset << 2 & sign ext.
        IMAGE_REL_M32R_PCREL16 = 0x0006 # 16 bit offset << 2 & sign ext.
        IMAGE_REL_M32R_PCREL8 = 0x0007 # 8 bit offset << 2 & sign ext.
        IMAGE_REL_M32R_REFHALF = 0x0008 # 16 MSBs
        IMAGE_REL_M32R_REFHI = 0x0009 # 16 MSBs; adj for LSB sign ext.
        IMAGE_REL_M32R_REFLO = 0x000A # 16 LSBs
        IMAGE_REL_M32R_PAIR = 0x000B # Link HI and LO
        IMAGE_REL_M32R_SECTION = 0x000C # Section table index
        IMAGE_REL_M32R_SECREL32 = 0x000D # 32 bit section relative reference
        IMAGE_REL_M32R_TOKEN = 0x000E # clr token
        IMAGE_REL_EBC_ABSOLUTE = 0x0000 # No relocation required
        IMAGE_REL_EBC_ADDR32NB = 0x0001 # 32 bit address w/o image base
        IMAGE_REL_EBC_REL32 = 0x0002 # 32-bit relative address from byte following reloc
        IMAGE_REL_EBC_SECTION = 0x0003 # Section table index
        IMAGE_REL_EBC_SECREL = 0x0004 # Offset within section
        
        def EXT_IMM64(Value, Address, Size, InstPos, ValPos) -> int:
            Value |= ULONGLONG((Address.contents.value >> InstPos) & ((1 << Size) - 1)).value << ValPos # Intel-IA64-Filler
            return Value
        
        def INS_IMM64(Value, Address, Size, InstPos, ValPos) -> int:
            cast(Address, PDWORD).contents = (cast(Address, PDWORD).contents.value & ~(((1 << Size) - 1) << InstPos) | 
                                              (DWORD(((ULONGLONG(Value).value >> ValPos) & ((1 << Size) - 1)).value) << InstPos)) # Intel-IA64-Filler
        
        EMARCH_ENC_I17_IMM7B_INST_WORD_X = 3 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM7B_SIZE_X = 7 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM7B_INST_WORD_POS_X = 4 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM7B_VAL_POS_X = 0 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM9D_INST_WORD_X = 3 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM9D_SIZE_X = 9 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM9D_INST_WORD_POS_X = 18 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM9D_VAL_POS_X = 7 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM5C_INST_WORD_X = 3 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM5C_SIZE_X = 5 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM5C_INST_WORD_POS_X = 13 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM5C_VAL_POS_X = 16 # Intel-IA64-Filler
        EMARCH_ENC_I17_IC_INST_WORD_X = 3 # Intel-IA64-Filler
        EMARCH_ENC_I17_IC_SIZE_X = 1 # Intel-IA64-Filler
        EMARCH_ENC_I17_IC_INST_WORD_POS_X = 12 # Intel-IA64-Filler
        EMARCH_ENC_I17_IC_VAL_POS_X = 21 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41a_INST_WORD_X = 1 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41a_SIZE_X = 10 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41a_INST_WORD_POS_X = 14 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41a_VAL_POS_X = 22 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41b_INST_WORD_X = 1 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41b_SIZE_X = 8 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41b_INST_WORD_POS_X = 24 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41b_VAL_POS_X = 32 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41c_INST_WORD_X = 2 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41c_SIZE_X = 23 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41c_INST_WORD_POS_X = 0 # Intel-IA64-Filler
        EMARCH_ENC_I17_IMM41c_VAL_POS_X = 40 # Intel-IA64-Filler
        EMARCH_ENC_I17_SIGN_INST_WORD_X = 3 # Intel-IA64-Filler
        EMARCH_ENC_I17_SIGN_SIZE_X = 1 # Intel-IA64-Filler
        EMARCH_ENC_I17_SIGN_INST_WORD_POS_X = 27 # Intel-IA64-Filler
        EMARCH_ENC_I17_SIGN_VAL_POS_X = 63 # Intel-IA64-Filler
        X3_OPCODE_INST_WORD_X = 3 # Intel-IA64-Filler
        X3_OPCODE_SIZE_X = 4 # Intel-IA64-Filler
        X3_OPCODE_INST_WORD_POS_X = 28 # Intel-IA64-Filler
        X3_OPCODE_SIGN_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_I_INST_WORD_X = 3 # Intel-IA64-Filler
        X3_I_SIZE_X = 1 # Intel-IA64-Filler
        X3_I_INST_WORD_POS_X = 27 # Intel-IA64-Filler
        X3_I_SIGN_VAL_POS_X = 59 # Intel-IA64-Filler
        X3_D_WH_INST_WORD_X = 3 # Intel-IA64-Filler
        X3_D_WH_SIZE_X = 3 # Intel-IA64-Filler
        X3_D_WH_INST_WORD_POS_X = 24 # Intel-IA64-Filler
        X3_D_WH_SIGN_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_IMM20_INST_WORD_X = 3 # Intel-IA64-Filler
        X3_IMM20_SIZE_X = 20 # Intel-IA64-Filler
        X3_IMM20_INST_WORD_POS_X = 4 # Intel-IA64-Filler
        X3_IMM20_SIGN_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_IMM39_1_INST_WORD_X = 2 # Intel-IA64-Filler
        X3_IMM39_1_SIZE_X = 23 # Intel-IA64-Filler
        X3_IMM39_1_INST_WORD_POS_X = 0 # Intel-IA64-Filler
        X3_IMM39_1_SIGN_VAL_POS_X = 36 # Intel-IA64-Filler
        X3_IMM39_2_INST_WORD_X = 1 # Intel-IA64-Filler
        X3_IMM39_2_SIZE_X = 16 # Intel-IA64-Filler
        X3_IMM39_2_INST_WORD_POS_X = 16 # Intel-IA64-Filler
        X3_IMM39_2_SIGN_VAL_POS_X = 20 # Intel-IA64-Filler
        X3_P_INST_WORD_X = 3 # Intel-IA64-Filler
        X3_P_SIZE_X = 4 # Intel-IA64-Filler
        X3_P_INST_WORD_POS_X = 0 # Intel-IA64-Filler
        X3_P_SIGN_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_TMPLT_INST_WORD_X = 0 # Intel-IA64-Filler
        X3_TMPLT_SIZE_X = 4 # Intel-IA64-Filler
        X3_TMPLT_INST_WORD_POS_X = 0 # Intel-IA64-Filler
        X3_TMPLT_SIGN_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_BTYPE_QP_INST_WORD_X = 2 # Intel-IA64-Filler
        X3_BTYPE_QP_SIZE_X = 9 # Intel-IA64-Filler
        X3_BTYPE_QP_INST_WORD_POS_X = 23 # Intel-IA64-Filler
        X3_BTYPE_QP_INST_VAL_POS_X = 0 # Intel-IA64-Filler
        X3_EMPTY_INST_WORD_X = 1 # Intel-IA64-Filler
        X3_EMPTY_SIZE_X = 2 # Intel-IA64-Filler
        X3_EMPTY_INST_WORD_POS_X = 14 # Intel-IA64-Filler
        X3_EMPTY_INST_VAL_POS_X = 0 # Intel-IA64-Filler

        #
        # Line number format.
        #
        
        class IMAGE_LINENUMBER(CStructure):
            class _Type(CUnion):
                _fields_ = [
                    ('SymbolTableIndex', DWORD),
                    ('VirtualAddress', DWORD)
                ]
                
                SymbolTableIndex: int # Symbol table index of function name if Linenumber is 0.
                VirtualAddress: int # Virtual address of line number.
            _fields_ = [
                ('Type', _Type),
                ('Linenumber', WORD)
            ]
            
            Linenumber: int
            Type: _Type
            
        PIMAGE_LINENUMBER = IMAGE_LINENUMBER.PTR()
        
        #
        # Based relocation format.
        #
        
        class IMAGE_BASE_RELOCATION(CStructure):
            _fields_ = [
                ('VirtualAddress', DWORD),
                ('SizeOfBlock', DWORD)
            ]
            
            VirtualAddress: int
            SizeOfBlock: int
            
        PIMAGE_BASE_RELOCATION = IMAGE_BASE_RELOCATION.PTR()
        
        #
        # Based relocation types.
        #

        IMAGE_REL_BASED_ABSOLUTE              = 0
        IMAGE_REL_BASED_HIGH                  = 1
        IMAGE_REL_BASED_LOW                   = 2
        IMAGE_REL_BASED_HIGHLOW               = 3
        IMAGE_REL_BASED_HIGHADJ               = 4
        IMAGE_REL_BASED_MACHINE_SPECIFIC_5    = 5
        IMAGE_REL_BASED_RESERVED              = 6
        IMAGE_REL_BASED_MACHINE_SPECIFIC_7    = 7
        IMAGE_REL_BASED_MACHINE_SPECIFIC_8    = 8
        IMAGE_REL_BASED_MACHINE_SPECIFIC_9    = 9
        IMAGE_REL_BASED_DIR64                 = 10

        #
        # Platform-specific based relocation types.
        #

        IMAGE_REL_BASED_IA64_IMM64            = 9

        IMAGE_REL_BASED_MIPS_JMPADDR          = 5
        IMAGE_REL_BASED_MIPS_JMPADDR16        = 9

        IMAGE_REL_BASED_ARM_MOV32             = 5
        IMAGE_REL_BASED_THUMB_MOV32           = 7

        #
        # Archive format.
        #

        IMAGE_ARCHIVE_START_SIZE             = 8
        IMAGE_ARCHIVE_START                  = b"!<arch>\n"
        IMAGE_ARCHIVE_END                    = b"`\n"
        IMAGE_ARCHIVE_PAD                    = b"\n"
        IMAGE_ARCHIVE_LINKER_MEMBER          = b"/               "
        IMAGE_ARCHIVE_LONGNAMES_MEMBER       = b"//              "
        IMAGE_ARCHIVE_HYBRIDMAP_MEMBER       = b"/<HYBRIDMAP>/   "

        class IMAGE_ARCHIVE_MEMBER_HEADER(CStructure):
            _fields_ = [
                ('Name', CHAR * 16),
                ('Date', BYTE * 12),
                ('UserID', BYTE * 6),
                ('GroupID', BYTE * 6),
                ('Mode', BYTE * 8),
                ('Size', BYTE * 10),
                ('EndHeader', CHAR * 2)
            ]
            
            Name: ICharArray
            Date: IArrayFixedSize[IByte, 12]
            UserID: IArrayFixedSize[IByte, 6]
            GroupID: IArrayFixedSize[IByte, 6]
            Mode: IArrayFixedSize[IByte, 8]
            Size: IArrayFixedSize[IByte, 10]
            EndHeader: ICharArray
            
        PIMAGE_ARCHIVE_MEMBER_HEADER = IMAGE_ARCHIVE_MEMBER_HEADER.PTR()

        IMAGE_SIZEOF_ARCHIVE_MEMBER_HDR      = 60

        #
        # DLL support.
        #

        #
        # Export Format
        #

        class IMAGE_EXPORT_DIRECTORY(CStructure):
            _fields_ = [
                ("Characteristics", DWORD),
                ("TimeDateStamp", DWORD),
                ("MajorVersion", WORD),
                ("MinorVersion", WORD),
                ("Name", DWORD),
                ("Base", DWORD),
                ("NumberOfFunctions", DWORD),
                ("NumberOfNames", DWORD),
                ("AddressOfFunctions", DWORD),   # RVA from base of image
                ("AddressOfNames", DWORD),       # RVA from base of image
                ("AddressOfNameOrdinals", DWORD) # RVA from base of image
            ]
            
            AddressOfNameOrdinals: int
            AddressOfFunctions: int
            NumberOfFunctions: int
            Characteristics: int
            AddressOfNames: int
            TimeDateStamp: int
            NumberOfNames: int
            MajorVersion: int
            MinorVersion: int
            Name: int
            Base: int
            
        PIMAGE_EXPORT_DIRECTORY = POINTER(IMAGE_EXPORT_DIRECTORY)
        
        #
        # Import Format
        #
        
        class IMAGE_IMPORT_BY_NAME(CStructure):
            _fields_ = [
                ('Hint', WORD)
            ]
            
            Name: ICharArray
            Hint: int
            
        array_after_structure(IMAGE_IMPORT_BY_NAME, 'Name', CHAR)
        
        PIMAGE_IMPORT_BY_NAME = IMAGE_IMPORT_BY_NAME.PTR()
        
        class IMAGE_THUNK_DATA64(CStructure):
            class U1(CUnion):
                _fields_ = [
                    ('ForwarderString', ULONGLONG),
                    ('Function', ULONGLONG),
                    ('Ordinal', ULONGLONG),
                    ('AddressOfData', ULONGLONG)
                ]
                
                ForwarderString: int
                Function: int
                Ordinal: int
                AddressOfData: int
                
            _fields_ = [
                ('u1', U1)
            ]
            
            u1: U1
            
        PIMAGE_THUNK_DATA64 = IMAGE_THUNK_DATA64.PTR()
            
        class IMAGE_THUNK_DATA32(CStructure):
            class U1(CUnion):
                _fields_ = [
                    ('ForwarderString', DWORD),
                    ('Function', DWORD),
                    ('Ordinal', DWORD),
                    ('AddressOfData', DWORD)
                ]
                
                ForwarderString: int
                Function: int
                Ordinal: int
                AddressOfData: int
                
            _fields_ = [
                ('u1', U1)
            ]
            
            u1: U1
            
        PIMAGE_THUNK_DATA32 = IMAGE_THUNK_DATA32.PTR()
        
        IMAGE_ORDINAL_FLAG64 = 0x8000000000000000
        IMAGE_ORDINAL_FLAG32 = 0x80000000
        
        def IMAGE_ORDINAL64(Ordinal: int) -> int:
            return (Ordinal & 0xffff)
        
        def IMAGE_ORDINAL32(Ordinal: int) -> int:
            return (Ordinal & 0xffff)
        
        def IMAGE_SNAP_BY_ORDINAL64(Ordinal: int) -> bool:
            return ((Ordinal & IMAGE_ORDINAL_FLAG64) != 0)
        
        def IMAGE_SNAP_BY_ORDINAL32(Ordinal: int) -> bool:
            return ((Ordinal & IMAGE_ORDINAL_FLAG32) != 0)
        
        #
        # Thread Local Storage
        #
        
        PIMAGE_TLS_CALLBACK = NTAPI(VOID, PVOID, DWORD, PVOID)
        
        class IMAGE_TLS_DIRECTORY64(CStructure):
            class _U(CUnion):
                class _S(CStructure):
                    _fields_ = [
                        ('Reserved0', DWORD, 20),
                        ('Alignment', DWORD, 4),
                        ('Reserved1', DWORD, 8)
                    ]
                _fields_  = [
                    ('Characteristics', DWORD),
                    ('_s', _S)
                ]
                _anonymous_ = ['_s']
            _fields_ = [
                ('StartAddressOfRawData', ULONGLONG),
                ('EndAddressOfRawData', ULONGLONG),
                ('AddressOfIndex', ULONGLONG),
                ('AddressOfCallBacks', ULONGLONG),
                ('SizeOfZeroFill', DWORD),
                ('_u', _U)
            ]
            _anonymous_ = ['_u']
            
            Alignment: int
            Characteristics: int
            StartAddressOfRawData: int
            EndAddressOfRawData: int
            AddressOfIndex: int
            AddressOfCallBacks: int
            SizeOfZeroFill: int
            
        PIMAGE_TLS_DIRECTORY64 = IMAGE_TLS_DIRECTORY64.PTR()
        
        class IMAGE_TLS_DIRECTORY32(CStructure):
            class _U(CUnion):
                class _S(CStructure):
                    _fields_ = [
                        ('Reserved0', DWORD, 20),
                        ('Alignment', DWORD, 4),
                        ('Reserved1', DWORD, 8)
                    ]
                _fields_  = [
                    ('Characteristics', DWORD),
                    ('_s', _S)
                ]
                _anonymous_ = ['_s']
            _fields_ = [
                ('StartAddressOfRawData', DWORD),
                ('EndAddressOfRawData', DWORD),
                ('AddressOfIndex', DWORD),
                ('AddressOfCallBacks', DWORD),
                ('SizeOfZeroFill', DWORD),
                ('_u', _U)
            ]
            _anonymous_ = ['_u']
            
            Alignment: int
            Characteristics: int
            StartAddressOfRawData: int
            EndAddressOfRawData: int
            AddressOfIndex: int
            AddressOfCallBacks: int
            SizeOfZeroFill: int
            
        PIMAGE_TLS_DIRECTORY32 = IMAGE_TLS_DIRECTORY32.PTR()

        if cpreproc.ifdef("_WIN64"):
            IMAGE_ORDINAL_FLAG = IMAGE_ORDINAL_FLAG64
            
            def IMAGE_ORDINAL(Ordinal: int) -> int:
                return IMAGE_ORDINAL64(Ordinal)
            
            IMAGE_THUNK_DATA = IMAGE_THUNK_DATA64
            PIMAGE_THUNK_DATA = PIMAGE_THUNK_DATA64
            
            def IMAGE_SNAP_BY_ORDINAL(Ordinal: int) -> bool:
                return IMAGE_SNAP_BY_ORDINAL64(Ordinal)
            
            IMAGE_TLS_DIRECTORY = IMAGE_TLS_DIRECTORY64
            PIMAGE_TLS_DIRECTORY = PIMAGE_TLS_DIRECTORY64
        else: 
            IMAGE_ORDINAL_FLAG = IMAGE_ORDINAL_FLAG32
            
            def IMAGE_ORDINAL(Ordinal: int) -> int:
                return IMAGE_ORDINAL32(Ordinal)
            
            IMAGE_THUNK_DATA = IMAGE_THUNK_DATA32
            PIMAGE_THUNK_DATA = PIMAGE_THUNK_DATA32
            
            def IMAGE_SNAP_BY_ORDINAL(Ordinal: int) -> bool:
                return IMAGE_SNAP_BY_ORDINAL32(Ordinal)
            
            IMAGE_TLS_DIRECTORY = IMAGE_TLS_DIRECTORY32
            PIMAGE_TLS_DIRECTORY = PIMAGE_TLS_DIRECTORY32
            
        class IMAGE_IMPORT_DESCRIPTOR(CStructure):
            class _U(CUnion):
                _fields_ = [
                    ('Characteristics', DWORD),
                    ('OriginalFirstThunk', DWORD)
                ]
            _fields_ = [
                ('_u', _U),
                ('TimeDateStamp', DWORD),
                ('ForwarderChain', DWORD),
                ('Name', DWORD),
                ('FirstThunk', DWORD)
            ]
            _anonymous_ = ['_u']
            
            Characteristics: int            # 0 for terminating null import descriptor
            OriginalFirstThunk: int         # RVA to original unbound IAT (PIMAGE_THUNK_DATA)
            
            TimeDateStamp: int              # 0 if not bound,
                                            # -1 if bound, and real date\time stamp
                                            #     in IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT (new BIND)
                                            # O.W. date/time stamp of DLL bound to (Old BIND)
                                                
            ForwarderChain: int             # -1 if no forwarders
            Name: int
            FirstThunk: int                 # RVA to IAT (if bound this IAT has actual addresses)
    
        PIMAGE_IMPORT_DESCRIPTOR = IMAGE_IMPORT_DESCRIPTOR.PTR()

        #
        # New format import descriptors pointed to by DataDirectory[ IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT ]
        #
        
        class IMAGE_BOUND_IMPORT_DESCRIPTOR(CStructure):
            _fields_ = [
                ('TimeDateStamp', DWORD),
                ('OffsetModuleName', WORD),
                ('NumberOfModuleForwarderRefs', WORD)
            ]
            
            TimeDateStamp: int
            OffsetModuleName: int
            NumberOfModuleForwarderRefs: int
            
            # Array of zero or more IMAGE_BOUND_FORWARDER_REF follows

        PIMAGE_BOUND_IMPORT_DESCRIPTOR = IMAGE_BOUND_IMPORT_DESCRIPTOR.PTR()
        
        class IMAGE_BOUND_FORWARDER_REF(CStructure):
            _fields_ = [
                ('TimeDateStamp', DWORD),
                ('OffsetModuleName', WORD),
                ('Reserved', WORD)
            ]
            
            TimeDateStamp: int
            OffsetModuleName: int

        PIMAGE_BOUND_FORWARDER_REF = IMAGE_BOUND_FORWARDER_REF.PTR()
        
        class IMAGE_DELAYLOAD_DESCRIPTOR(CStructure):
            class _Attributes(CUnion):
                class _S(CStructure):
                    _fields_ = [
                        ('RvaBased', DWORD, 1),
                        ('ReservedAttributes', DWORD, 31)
                    ]
                _fields_ = [
                    ('AllAttributes', DWORD),
                    ('_s', _S)
                ]
                _anonymous_ = ['_s']
                
                RvaBased: int             # Delay load version 2
                AllAttributes: int
                
            _fields_ = [
                ('Attributes', _Attributes),
                ('DllNameRVA', DWORD),
                ('ModuleHandleRVA', DWORD),
                ('ImportAddressTableRVA', DWORD),
                ('ImportNameTableRVA', DWORD),
                ('BoundImportAddressTableRVA', DWORD),
                ('UnloadInformationTableRVA', DWORD),
                ('TimeDateStamp', DWORD)
            ]
            
            Attributes: _Attributes
            DllNameRVA: int                       # RVA to the name of the target library (NULL-terminate ASCII string)
            ModuleHandleRVA: int                  # RVA to the HMODULE caching location (PHMODULE)
            ImportAddressTableRVA: int            # RVA to the start of the IAT (PIMAGE_THUNK_DATA)
            ImportNameTableRVA: int               # RVA to the start of the name table (PIMAGE_THUNK_DATA::AddressOfData)
            BoundImportAddressTableRVA: int       # RVA to an optional bound IAT
            UnloadInformationTableRVA: int        # RVA to an optional unload info table
            TimeDateStamp: int                    # 0 if not bound,
                                                  # Otherwise, date/time of the target DLL

        PIMAGE_DELAYLOAD_DESCRIPTOR = PCIMAGE_DELAYLOAD_DESCRIPTOR = IMAGE_DELAYLOAD_DESCRIPTOR.PTR()

        if cpreproc.ifdef("_WIN64"):
            IMAGE_NT_HEADERS = IMAGE_NT_HEADERS64
            PIMAGE_NT_HEADERS = PIMAGE_NT_HEADERS64
            IMAGE_OPTIONAL_HEADER = IMAGE_OPTIONAL_HEADER64
        else:
            IMAGE_NT_HEADERS = IMAGE_NT_HEADERS32
            PIMAGE_NT_HEADERS = PIMAGE_NT_HEADERS32
            IMAGE_OPTIONAL_HEADER = IMAGE_OPTIONAL_HEADER32
        
        # Directory Entries

        IMAGE_DIRECTORY_ENTRY_EXPORT          = 0   # Export Directory
        IMAGE_DIRECTORY_ENTRY_IMPORT          = 1   # Import Directory
        IMAGE_DIRECTORY_ENTRY_RESOURCE        = 2   # Resource Directory
        IMAGE_DIRECTORY_ENTRY_EXCEPTION       = 3   # Exception Directory
        IMAGE_DIRECTORY_ENTRY_SECURITY        = 4   # Security Directory
        IMAGE_DIRECTORY_ENTRY_BASERELOC       = 5   # Base Relocation Table
        IMAGE_DIRECTORY_ENTRY_DEBUG           = 6   # Debug Directory
        IMAGE_DIRECTORY_ENTRY_COPYRIGHT       = 7   # (X86 usage)
        IMAGE_DIRECTORY_ENTRY_ARCHITECTURE    = 7   # Architecture Specific Data
        IMAGE_DIRECTORY_ENTRY_GLOBALPTR       = 8   # RVA of GP
        IMAGE_DIRECTORY_ENTRY_TLS             = 9   # TLS Directory
        IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG    = 10   # Load Configuration Directory
        IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT   = 11   # Bound Import Directory in headers
        IMAGE_DIRECTORY_ENTRY_IAT            = 12   # Import Address Table
        IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT   = 13   # Delay Load Import Descriptors
        IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR = 14   # COM Runtime descriptor

        if cpreproc.pragma_once("_RTL_RUN_ONCE_DEF"):
            #
            # Run once
            #

            RTL_RUN_ONCE_INIT = lambda: RTL_RUN_ONCE()   # Static initializer

            #
            # Run once flags
            #

            RTL_RUN_ONCE_CHECK_ONLY = 0x00000001
            RTL_RUN_ONCE_ASYNC = 0x00000002
            RTL_RUN_ONCE_INIT_FAILED = 0x00000004

            #
            # The context stored in the run once structure must leave the following number
            # of low order bits unused.
            #

            RTL_RUN_ONCE_CTX_RESERVED_BITS = 2

            class RTL_RUN_ONCE(Union):
                _fields_ = [
                    ("Ptr", PVOID)
                ]
            PRTL_RUN_ONCE = POINTER(RTL_RUN_ONCE)

        # _RTL_RUN_ONCE_DEF

        class RTL_BARRIER(CStructure):
            _fields_ = [
                ("Reserved1", DWORD),
                ("Reserved2", DWORD),
                ("Reserved3", ULONG_PTR * 2),
                ("Reserved4", DWORD),
                ("Reserved5", DWORD)
            ]                      
        PRTL_BARRIER = POINTER(RTL_BARRIER)          

        class RTL_CRITICAL_SECTION_DEBUG(CStructure):
            pass
        PRTL_CRITICAL_SECTION_DEBUG = POINTER(RTL_CRITICAL_SECTION_DEBUG)
        RTL_RESOURCE_DEBUG = RTL_CRITICAL_SECTION_DEBUG
        PRTL_RESOURCE_DEBUG = PRTL_CRITICAL_SECTION_DEBUG

        class RTL_CRITICAL_SECTION(CStructure):
            _pack_ = 8
        PRTL_CRITICAL_SECTION = POINTER(RTL_CRITICAL_SECTION)

        RTL_CRITICAL_SECTION_DEBUG._fields_ = [
            ("Type", WORD),
            ("CreatorBackTraceIndex", WORD),
            ("CriticalSection", PRTL_CRITICAL_SECTION),
            ("ProcessLocksList", LIST_ENTRY),
            ("EntryCount", DWORD),
            ("ContentionCount", DWORD),
            ("Flags", DWORD),
            ("CreatorBackTraceIndexHigh", WORD),
            ("SpareWORD", WORD)
        ]

        RTL_CRITICAL_SECTION._fields_ = [
            ("DebugInfo",  PRTL_CRITICAL_SECTION_DEBUG),
            #
            #  The following three fields control entering and exiting the critical
            #  section for the resource
            #
            ("LockCount", LONG),
            ("RecursionCount", LONG),
            ("OwningThread", HANDLE),  # from the thread's ClientId->UniqueThread
            ("LockSemaphore", HANDLE),
            ("SpinCount", ULONG_PTR)   # force size on 64-bit systems when packed
        ]

        #
        # These flags define the upper byte of the critical section SpinCount field
        #
        RTL_CRITICAL_SECTION_FLAG_NO_DEBUG_INFO = 0x01000000
        RTL_CRITICAL_SECTION_FLAG_DYNAMIC_SPIN = 0x02000000
        RTL_CRITICAL_SECTION_FLAG_STATIC_INIT = 0x04000000
        RTL_CRITICAL_SECTION_FLAG_RESOURCE_TYPE = 0x08000000
        RTL_CRITICAL_SECTION_FLAG_FORCE_DEBUG_INFO = 0x10000000
        RTL_CRITICAL_SECTION_ALL_FLAG_BITS = 0xFF000000
        RTL_CRITICAL_SECTION_FLAG_RESERVED = (RTL_CRITICAL_SECTION_ALL_FLAG_BITS & (~(RTL_CRITICAL_SECTION_FLAG_NO_DEBUG_INFO | RTL_CRITICAL_SECTION_FLAG_DYNAMIC_SPIN | RTL_CRITICAL_SECTION_FLAG_STATIC_INIT | RTL_CRITICAL_SECTION_FLAG_RESOURCE_TYPE | RTL_CRITICAL_SECTION_FLAG_FORCE_DEBUG_INFO)))

        #
        # These flags define possible values stored in the Flags field of a critsec debuginfo.
        #
        RTL_CRITICAL_SECTION_DEBUG_FLAG_STATIC_INIT = 0x00000001

        class RTL_SRWLOCK(CStructure):
            _fields_ = [
                ("Ptr", PVOID)
            ]                
        PRTL_SRWLOCK = POINTER(RTL_SRWLOCK)                        
        RTL_SRWLOCK_INIT = lambda: RTL_SRWLOCK()                            
        class RTL_CONDITION_VARIABLE(CStructure):
            _fields_ = [
                ("Ptr", PVOID)
            ]                
        PRTL_CONDITION_VARIABLE = POINTER(RTL_CONDITION_VARIABLE)   
        RTL_CONDITION_VARIABLE_INIT = lambda: RTL_CONDITION_VARIABLE()                 
        RTL_CONDITION_VARIABLE_LOCKMODE_SHARED = 0x1

        HEAP_INFORMATION_CLASS = INT
        if True:
            HeapCompatibilityInformation = 0
            HeapEnableTerminationOnCorruption = 1
            HeapOptimizeResources = 3
            HeapTag = 4

        class PROCESS_HEAP_ENTRY(CStructure):
            class _DUMMYUNIONNAME(Union):
                class _Block(CStructure):
                    _fields_ = [
                        ("hMem", HANDLE),
                        ("dwReserved", DWORD * 3)
                    ]
                class _Region(CStructure):
                    _fields_ = [
                        ("dwCommittedSize", DWORD),
                        ("dwUnCommittedSize", DWORD),
                        ("lpFirstBlock", LPVOID),
                        ("lpLastBlock", LPVOID)
                    ]
                _fields_ = [
                    ("Block", _Block),
                    ("Region", _Region)
                ]
            _fields_ = [
                ("lpData", PVOID),
                ("cbData", DWORD),
                ("cbOverhead", BYTE),
                ("iRegionIndex", BYTE),
                ("wFlags", WORD),
                ("u", _DUMMYUNIONNAME)
            ]
        LPPROCESS_HEAP_ENTRY = POINTER(PROCESS_HEAP_ENTRY)
        PPROCESS_HEAP_ENTRY = LPPROCESS_HEAP_ENTRY

    class XSTATE_FEATURE(CStructure):
        _fields_ = [
            ("Offset", USHORT),  # Offset in the XState area
            ("Size", USHORT)    # Size of the feature in bytes
        ]

    class XSTATE_CONFIGURATION(CStructure):
        _fields_ = [
            ("EnabledFeatures", ULONG),  # Bitmask of enabled features
            ("Size", USHORT),            # Size of the XState area
            ("OptimizedSize", USHORT, 1),  # Optimized size of the XState area
            ("Features", XSTATE_FEATURE * 64)  # Array of features
        ]

    class KSYSTEM_TIME(CStructure):
        _fields_ = [
            ("LowPart", ULONG),
            ("High1Time", LONG),
            ("High2Time", LONG)
        ]
    
    class KUSER_SHARED_DATA(CStructure):
        _fields_ = [
            ("TickCountMultiplier", ULONG),
            ("InterruptTime", KSYSTEM_TIME),
            ("SystemTime", KSYSTEM_TIME),
            ("TimeZoneBias", KSYSTEM_TIME),
            ("ImageNumberLow", USHORT),
            ("ImageNumberHigh", USHORT),
            ("NtSystemRoot", WCHAR * 260),
            ("MaxStackTraceDepth", ULONG),
            ("CryptoExponent", ULONG),
            ("TimeZoneId", ULONG),
            ("LargePageMinimum", ULONG),
            ("AitSamplingValue", ULONG),
            ("AppCompatFlag", ULONG),
            ("RNGSeedVersion", ULONGLONG),
            ("GlobalValidationRunlevel", ULONG),
            ("TimeZoneBiasStamp", LONG),
            ("NtBuildNumber", ULONG),
            ("NtProductType", INT),
            ("ProductTypeIsValid", BOOLEAN),
            ("Reserved0", BOOLEAN * 1),
            ("NativeProcessorArchitecture", USHORT),
            ("NtMajorVersion", ULONG),
            ("NtMinorVersion", ULONG),
            ("ProcessorFeatures", BOOLEAN * 64),
            ("Reserved1", ULONG),
            ("Reserved3", ULONG),
            ("TimeSlip", ULONG),
            ("AlternativeArchitecture", INT),
            ("BootId", ULONG),
            ("SystemExpirationDate", LARGE_INTEGER),
            ("SuiteMask", ULONG),
            ("KdDebuggerEnabled", BOOLEAN),
            ("MitigationPolicies", UCHAR),
            ("CyclesPerYield", USHORT),
            ("ActiveConsoleId", ULONG),
            ("DismountCount", ULONG),
            ("ComPlusPackage", ULONG),
            ("LastSystemRITEventTickCount", ULONG),
            ("NumberOfPhysicalPages", ULONG),
            ("SafeBootMode", BOOLEAN),
            ("VirtualizationFlags", UCHAR),
            ("Reserved12", UCHAR * 2),
            ("SharedDataFlags", ULONG),
            ("DataFlagsPad", ULONG * 1),
            ("TestRetInstruction", ULONGLONG),
            ("QpcFrequency", LONGLONG),
            ("SystemCall", ULONG),
            ("Reserved2", ULONG),
            ("FullNumberOfPhysicalPages", ULONGLONG),
            ("SystemCallPad", ULONGLONG * 1),
            ("TickCount", KSYSTEM_TIME),
            ("Cookie", ULONG),
            ("CookiePad", ULONG * 1),
            ("ConsoleSessionForegroundProcessId", LONGLONG),
            ("TimeUpdateLock", ULONGLONG),
            ("BaselineSystemTimeQpc", ULONGLONG),
            ("BaselineInterruptTimeQpc", ULONGLONG),
            ("QpcSystemTimeIncrement", ULONGLONG),
            ("QpcInterruptTimeIncrement", ULONGLONG),
            ("QpcSystemTimeIncrementShift", UCHAR),
            ("QpcInterruptTimeIncrementShift", UCHAR),
            ("UnparkedProcessorCount", USHORT),
            ("EnclaveFeatureMask", ULONG * 4),
            ("TelemetryCoverageRound", ULONG),
            ("UserModeGlobalLogger", USHORT * 16),
            ("ImageFileExecutionOptions", ULONG),
            ("LangGenerationCount", ULONG),
            ("Reserved4", ULONGLONG),
            ("InterruptTimeBias", ULONGLONG),
            ("QpcBias", ULONGLONG),
            ("ActiveProcessorCount", ULONG),
            ("ActiveGroupCount", UCHAR),
            ("Reserved9", UCHAR),
            ("QpcData", USHORT), # QPC bypass enabled, reserved
            ("TimeZoneBiasEffectiveStart", LARGE_INTEGER), # Effective start of the time zone bias
            ("TimeZoneBiasEffectiveEnd", LARGE_INTEGER), # Effective end of the time zone bias
            ("XState", XSTATE_CONFIGURATION), # XState configuration
            ("FeatureConfigurationChangeStamp", KSYSTEM_TIME), # Feature configuration change stamp
            ("Spare", ULONG), # Spare field for future use
            ("UserPointerAuthMask", ULONGLONG), # User pointer authentication mask
            ("XStateArm64", XSTATE_CONFIGURATION), # XState configuration for ARM64
            ("Reserved10", ULONG * 210) # Reserved for future use
        ]
    PKUSER_SHARED_DATA = POINTER(KUSER_SHARED_DATA)