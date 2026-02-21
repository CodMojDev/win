from .basetsd import *

from .winnt import *

kernel32 = W_WinDLL("kernel32.dll")

Yield = lambda: None

FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_END = 2
WAIT_FAILED = DWORD(0xFFFFFFFF).value
WAIT_OBJECT_0 = ((STATUS_WAIT_0) + 0)
WAIT_ABANDONED = ((STATUS_ABANDONED_WAIT_0) + 0)
WAIT_ABANDONED_0 = ((STATUS_ABANDONED_WAIT_0) + 0)
WAIT_IO_COMPLETION = STATUS_USER_APC
FILE_FLAG_WRITE_THROUGH = 0x80000000
FILE_FLAG_OVERLAPPED = 0x40000000
FILE_FLAG_NO_BUFFERING = 0x20000000
FILE_FLAG_RANDOM_ACCESS = 0x10000000
FILE_FLAG_SEQUENTIAL_SCAN = 0x08000000
FILE_FLAG_DELETE_ON_CLOSE = 0x04000000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
FILE_FLAG_POSIX_SEMANTICS = 0x01000000
FILE_FLAG_SESSION_AWARE = 0x00800000
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_OPEN_NO_RECALL = 0x00100000
FILE_FLAG_FIRST_PIPE_INSTANCE = 0x00080000
FILE_FLAG_OPEN_REQUIRING_OPLOCK = 0x00040000
PROGRESS_CONTINUE = 0
PROGRESS_CANCEL = 1
PROGRESS_STOP = 2
PROGRESS_QUIET = 3
CALLBACK_CHUNK_FINISHED = 0x00000000
CALLBACK_STREAM_SWITCH = 0x00000001
COPY_FILE_FAIL_IF_EXISTS = 0x00000001
COPY_FILE_RESTARTABLE = 0x00000002
COPY_FILE_OPEN_SOURCE_FOR_WRITE = 0x00000004
COPY_FILE_ALLOW_DECRYPTED_DESTINATION = 0x00000008
COPY_FILE_COPY_SYMLINK = 0x00000800
COPY_FILE_NO_BUFFERING = 0x00001000
COPY_FILE_REQUEST_SECURITY_PRIVILEGES = 0x00002000
COPY_FILE_RESUME_FROM_PAUSE = 0x00004000
COPY_FILE_NO_OFFLOAD = 0x00040000
COPY_FILE_IGNORE_EDP_BLOCK = 0x00400000
COPY_FILE_IGNORE_SOURCE_ENCRYPTION = 0x00800000
COPY_FILE_DONT_REQUEST_DEST_WRITE_DAC = 0x02000000
COPY_FILE_REQUEST_COMPRESSED_TRAFFIC = 0x10000000
COPY_FILE_OPEN_AND_COPY_REPARSE_POINT = 0x00200000
COPY_FILE_DIRECTORY = 0x00000080
COPY_FILE_SKIP_ALTERNATE_STREAMS = 0x00008000
COPY_FILE_DISABLE_PRE_ALLOCATION = 0x04000000
COPY_FILE_ENABLE_LOW_FREE_SPACE_MODE = 0x08000000
REPLACEFILE_WRITE_THROUGH = 0x00000001
REPLACEFILE_IGNORE_MERGE_ERRORS = 0x00000002
REPLACEFILE_IGNORE_ACL_ERRORS = 0x00000004
PIPE_ACCESS_INBOUND = 0x00000001
PIPE_ACCESS_OUTBOUND = 0x00000002
PIPE_ACCESS_DUPLEX = 0x00000003
PIPE_CLIENT_END = 0x00000000
PIPE_SERVER_END = 0x00000001
PIPE_WAIT = 0x00000000
PIPE_NOWAIT = 0x00000001
PIPE_READMODE_BYTE = 0x00000000
PIPE_READMODE_MESSAGE = 0x00000002
PIPE_TYPE_BYTE = 0x00000000
PIPE_TYPE_MESSAGE = 0x00000004
PIPE_ACCEPT_REMOTE_CLIENTS = 0x00000000
PIPE_REJECT_REMOTE_CLIENTS = 0x00000008
PIPE_UNLIMITED_INSTANCES = 255
SECURITY_ANONYMOUS = (SecurityAnonymous << 16)
SECURITY_IDENTIFICATION = (SecurityIdentification << 16)
SECURITY_IMPERSONATION = (SecurityImpersonation << 16)
SECURITY_DELEGATION = (SecurityDelegation << 16)
SECURITY_CONTEXT_TRACKING = 0x00040000
SECURITY_EFFECTIVE_ONLY = 0x00080000
SECURITY_SQOS_PRESENT = 0x00100000
SECURITY_VALID_SQOS_FLAGS = 0x001F0000

#if(_WIN32_WINNT >= 0x0400)
PFIBER_START_ROUTINE = WINAPI(VOID, LPVOID)
LPFIBER_START_ROUTINE = PFIBER_START_ROUTINE

PFIBER_CALLOUT_ROUTINE = WINAPI(LPVOID, LPVOID)
FAIL_FAST_GENERATE_EXCEPTION_ADDRESS = 0x1
FAIL_FAST_NO_HARD_ERROR_DLG = 0x2

# REGION ***

# REGION *** Application Family or OneCore Family ***

SP_SERIALCOMM = DWORD(0x00000001).value
PST_UNSPECIFIED = DWORD(0x00000000).value
PST_RS232 = DWORD(0x00000001).value
PST_PARALLELPORT = DWORD(0x00000002).value
PST_RS422 = DWORD(0x00000003).value
PST_RS423 = DWORD(0x00000004).value
PST_RS449 = DWORD(0x00000005).value
PST_MODEM = DWORD(0x00000006).value
PST_FAX = DWORD(0x00000021).value
PST_SCANNER = DWORD(0x00000022).value
PST_NETWORK_BRIDGE = DWORD(0x00000100).value
PST_LAT = DWORD(0x00000101).value
PST_TCPIP_TELNET = DWORD(0x00000102).value
PST_X25 = DWORD(0x00000103).value
PCF_DTRDSR = DWORD(0x0001).value
PCF_RTSCTS = DWORD(0x0002).value
PCF_RLSD = DWORD(0x0004).value
PCF_PARITY_CHECK = DWORD(0x0008).value
PCF_XONXOFF = DWORD(0x0010).value
PCF_SETXCHAR = DWORD(0x0020).value
PCF_TOTALTIMEOUTS = DWORD(0x0040).value
PCF_INTTIMEOUTS = DWORD(0x0080).value
PCF_SPECIALCHARS = DWORD(0x0100).value
PCF_16BITMODE = DWORD(0x0200).value
SP_PARITY = DWORD(0x0001).value
SP_BAUD = DWORD(0x0002).value
SP_DATABITS = DWORD(0x0004).value
SP_STOPBITS = DWORD(0x0008).value
SP_HANDSHAKING = DWORD(0x0010).value
SP_PARITY_CHECK = DWORD(0x0020).value
SP_RLSD = DWORD(0x0040).value
BAUD_075 = DWORD(0x00000001).value
BAUD_110 = DWORD(0x00000002).value
BAUD_134_5 = DWORD(0x00000004).value
BAUD_150 = DWORD(0x00000008).value
BAUD_300 = DWORD(0x00000010).value
BAUD_600 = DWORD(0x00000020).value
BAUD_1200 = DWORD(0x00000040).value
BAUD_1800 = DWORD(0x00000080).value
BAUD_2400 = DWORD(0x00000100).value
BAUD_4800 = DWORD(0x00000200).value
BAUD_7200 = DWORD(0x00000400).value
BAUD_9600 = DWORD(0x00000800).value
BAUD_14400 = DWORD(0x00001000).value
BAUD_19200 = DWORD(0x00002000).value
BAUD_38400 = DWORD(0x00004000).value
BAUD_56K = DWORD(0x00008000).value
BAUD_128K = DWORD(0x00010000).value
BAUD_115200 = DWORD(0x00020000).value
BAUD_57600 = DWORD(0x00040000).value
BAUD_USER = DWORD(0x10000000).value
DATABITS_5 = WORD(0x0001).value
DATABITS_6 = WORD(0x0002).value
DATABITS_7 = WORD(0x0004).value
DATABITS_8 = WORD(0x0008).value
DATABITS_16 = WORD(0x0010).value
DATABITS_16X = WORD(0x0020).value
STOPBITS_10 = WORD(0x0001).value
STOPBITS_15 = WORD(0x0002).value
STOPBITS_20 = WORD(0x0004).value
PARITY_NONE = WORD(0x0100).value
PARITY_ODD = WORD(0x0200).value
PARITY_EVEN = WORD(0x0400).value
PARITY_MARK = WORD(0x0800).value
PARITY_SPACE = WORD(0x1000).value

class _COMMPROP(CStructure):
    _fields_ = [
        ("wPacketLength", WORD),
        ("wPacketVersion", WORD),
        ("dwServiceMask", DWORD),
        ("dwReserved1", DWORD),
        ("dwMaxTxQueue", DWORD),
        ("dwMaxRxQueue", DWORD),
        ("dwMaxBaud", DWORD),
        ("dwProvSubType", DWORD),
        ("dwProvCapabilities", DWORD),
        ("dwSettableParams", DWORD),
        ("dwSettableBaud", DWORD),
        ("wSettableData", WORD),
        ("wSettableStopParity", WORD),
        ("dwCurrentTxQueue", DWORD),
        ("dwCurrentRxQueue", DWORD),
        ("dwProvSpec1", DWORD),
        ("dwProvSpec2", DWORD),
        ("wcProvChar", WCHAR * 1)
    ]
COMMPROP = _COMMPROP
LPCOMMPROP = POINTER(COMMPROP)

#
# Set dwProvSpec1 to COMMPROP_INITIALIZED to indicate that wPacketLength
# is valid before a call to GetCommProperties().
#
COMMPROP_INITIALIZED = DWORD(0xE73CF52E).value

class _COMSTAT(CStructure):
    _fields_ = [
        ("fCtsHold", DWORD, 1),
        ("fDsrHold", DWORD, 1),
        ("fRlsdHold", DWORD, 1),
        ("fXoffHold", DWORD, 1),
        ("fXoffSent", DWORD, 1),
        ("fEof", DWORD, 1),
        ("fTxim", DWORD, 1),
        ("fReserved", DWORD, 25),
        ("cbInQue", DWORD),
        ("cbOutQue", DWORD)
    ]
COMSTAT = _COMSTAT
LPCOMSTAT = POINTER(COMSTAT)

#
# DTR Control Flow Values.
#
DTR_CONTROL_DISABLE = 0x00
DTR_CONTROL_ENABLE = 0x01
DTR_CONTROL_HANDSHAKE = 0x02

#
# RTS Control Flow Values
#
RTS_CONTROL_DISABLE = 0x00
RTS_CONTROL_ENABLE = 0x01
RTS_CONTROL_HANDSHAKE = 0x02
RTS_CONTROL_TOGGLE = 0x03

class _DCB(CStructure):
    ("DCBlength", DWORD), #  sizeof(DCB)                     
    ("BaudRate", DWORD), #  Baudrate at which running       
    ("fBinary", DWORD, 1), #  Binary Mode (skip EOF check)    
    ("fParity", DWORD, 1), #  Enable parity checking          
    ("fOutxCtsFlow", DWORD, 1), #  CTS handshaking on output       
    ("fOutxDsrFlow", DWORD, 1), #  DSR handshaking on output       
    ("fDtrControl", DWORD, 2), #  DTR Flow control                
    ("fDsrSensitivity", DWORD, 1), #  DSR Sensitivity              
    ("fTXContinueOnXoff", DWORD, 1), #  Continue TX when Xoff sent 
    ("fOutX", DWORD, 1), #  Enable output X-ON/X-OFF        
    ("fInX", DWORD, 1), #  Enable input X-ON/X-OFF         
    ("fErrorChar", DWORD, 1), #  Enable Err Replacement          
    ("fNull", DWORD, 1), #  Enable Null stripping           
    ("fRtsControl", DWORD, 2), #  Rts Flow control                
    ("fAbortOnError", DWORD, 1), #  Abort all reads and writes on Error 
    ("fDummy2", DWORD, 17), #  Reserved                        
    ("wReserved", WORD), #  Not currently used              
    ("XonLim", WORD), #  Transmit X-ON threshold         
    ("XoffLim", WORD), #  Transmit X-OFF threshold        
    ("ByteSize", BYTE), #  Number of bits/byte, 4-8        
    ("Parity", BYTE), #  0-4=None,Odd,Even,Mark,Space    
    ("StopBits", BYTE), #  0,1,2 = 1, 1.5, 2               
    ("XonChar", CHAR), #  Tx and Rx X-ON character        
    ("XoffChar", CHAR), #  Tx and Rx X-OFF character       
    ("ErrorChar", CHAR), #  Error replacement char          
    ("EofChar", CHAR), #  End of Input character          
    ("EvtChar", CHAR), #  Received Event character        
    ("wReserved1", WORD), #  Fill for now.     
DCB = _DCB
LPDCB = POINTER(DCB)

class _COMMTIMEOUTS(CStructure):
    ("ReadIntervalTimeout", DWORD), #  Maximum time between read chars. 
    ("ReadTotalTimeoutMultiplier", DWORD), #  Multiplier of characters.        
    ("ReadTotalTimeoutConstant", DWORD), #  Constant in milliseconds.        
    ("WriteTotalTimeoutMultiplier", DWORD), #  Multiplier of characters.        
    ("WriteTotalTimeoutConstant", DWORD), #  Constant in milliseconds.        
COMMTIMEOUTS = _COMMTIMEOUTS
LPCOMMTIMEOUTS = POINTER(COMMTIMEOUTS)

class _COMMCONFIG(CStructure):
    ("dwSize", DWORD), #  Size of the entire struct 
    ("wVersion", WORD), #  version of the structure 
    ("wReserved", WORD), #  alignment 
    ("dcb", DCB), #  device control block 
    ("dwProviderSubType", DWORD),    # ordinal value for identifying
                                     # provider-defined data structure format
    ("dwProviderOffset", DWORD),     # Specifies the offset of provider specific
                                     #data field in bytes from the start */
    ("dwProviderSize", DWORD), #  size of the provider-specific data field 
    ("wcProviderData[1]", WCHAR) #  provider-specific data 
COMMCONFIG = _COMMCONFIG
LPCOMMCONFIG = POINTER(COMMCONFIG)

# REGION ***

# REGION *** Application Family or OneCore Family or Games Family ***

#FreeModule(hLibModule) = FreeLibrary((hLibModule))
#MakeProcInstance(lpProc,hInstance) = (lpProc)
#FreeProcInstance(lpProc) = (lpProc)
GMEM_FIXED = 0x0000
GMEM_MOVEABLE = 0x0002
GMEM_NOCOMPACT = 0x0010
GMEM_NODISCARD = 0x0020
GMEM_ZEROINIT = 0x0040
GMEM_MODIFY = 0x0080
GMEM_DISCARDABLE = 0x0100
GMEM_NOT_BANKED = 0x1000
GMEM_SHARE = 0x2000
GMEM_DDESHARE = 0x2000
GMEM_NOTIFY = 0x4000
GMEM_LOWER = GMEM_NOT_BANKED
GMEM_VALID_FLAGS = 0x7F72
GMEM_INVALID_HANDLE = 0x8000
GHND = (GMEM_MOVEABLE | GMEM_ZEROINIT)
GPTR = (GMEM_FIXED | GMEM_ZEROINIT)
GlobalLRUNewest = lambda h: (HANDLE(h))
GlobalLRUOldest = lambda h: (HANDLE(h))
#GlobalDiscard = lambda h: GlobalReAlloc((h), 0, GMEM_MOVEABLE)
GMEM_DISCARDED = 0x4000
GMEM_LOCKCOUNT = 0x00FF

# REGION ***

# REGION *** Application Family or OneCore Family ***

class _MEMORYSTATUS(CStructure):
    _fields_ = [
        ("dwLength", DWORD),
        ("dwMemoryLoad", DWORD),
        ("dwTotalPhys", SIZE_T),
        ("dwAvailPhys", SIZE_T),
        ("dwTotalPageFile", SIZE_T),
        ("dwAvailPageFile", SIZE_T),
        ("dwTotalVirtual", SIZE_T),
        ("dwAvailVirtual", SIZE_T)
    ]
MEMORYSTATUS = _MEMORYSTATUS
LPMEMORYSTATUS = POINTER(MEMORYSTATUS)

# REGION ***

# REGION *** Application Family or OneCore Family or Games Family ***

#
# Process dwCreationFlag values
#
DEBUG_PROCESS = 0x00000001
DEBUG_ONLY_THIS_PROCESS = 0x00000002
CREATE_SUSPENDED = 0x00000004
DETACHED_PROCESS = 0x00000008
CREATE_NEW_CONSOLE = 0x00000010
NORMAL_PRIORITY_CLASS = 0x00000020
IDLE_PRIORITY_CLASS = 0x00000040
HIGH_PRIORITY_CLASS = 0x00000080
REALTIME_PRIORITY_CLASS = 0x00000100
CREATE_NEW_PROCESS_GROUP = 0x00000200
CREATE_UNICODE_ENVIRONMENT = 0x00000400
CREATE_SEPARATE_WOW_VDM = 0x00000800
CREATE_SHARED_WOW_VDM = 0x00001000
CREATE_FORCEDOS = 0x00002000
BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
ABOVE_NORMAL_PRIORITY_CLASS = 0x00008000
INHERIT_PARENT_AFFINITY = 0x00010000
INHERIT_CALLER_PRIORITY = 0x00020000 # Deprecated
CREATE_PROTECTED_PROCESS = 0x00040000
EXTENDED_STARTUPINFO_PRESENT = 0x00080000
PROCESS_MODE_BACKGROUND_BEGIN = 0x00100000
PROCESS_MODE_BACKGROUND_END = 0x00200000
CREATE_SECURE_PROCESS = 0x00400000
CREATE_BREAKAWAY_FROM_JOB = 0x01000000
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = 0x02000000
CREATE_DEFAULT_ERROR_MODE = 0x04000000
CREATE_NO_WINDOW = 0x08000000
PROFILE_USER = 0x10000000
PROFILE_KERNEL = 0x20000000
PROFILE_SERVER = 0x40000000
CREATE_IGNORE_SYSTEM_DEFAULT = 0x80000000
#
# Thread dwCreationFlag values
#
#CREATE_SUSPENDED                  = 0x00000004
STACK_SIZE_PARAM_IS_A_RESERVATION = 0x00010000 # Threads only
#
# Priority flags
#
THREAD_BASE_PRIORITY_MIN = -2
THREAD_BASE_PRIORITY_MAX = 2
THREAD_BASE_PRIORITY_IDLE = -15
THREAD_BASE_PRIORITY_LOWRT = 15

THREAD_PRIORITY_LOWEST = THREAD_BASE_PRIORITY_MIN
THREAD_PRIORITY_BELOW_NORMAL = (THREAD_PRIORITY_LOWEST+1)
THREAD_PRIORITY_NORMAL = 0
THREAD_PRIORITY_HIGHEST = THREAD_BASE_PRIORITY_MAX
THREAD_PRIORITY_ABOVE_NORMAL = (THREAD_PRIORITY_HIGHEST-1)
THREAD_PRIORITY_ERROR_RETURN = (MAXLONG)
THREAD_PRIORITY_TIME_CRITICAL = THREAD_BASE_PRIORITY_LOWRT
THREAD_PRIORITY_IDLE = THREAD_BASE_PRIORITY_IDLE
THREAD_MODE_BACKGROUND_BEGIN = 0x00010000
THREAD_MODE_BACKGROUND_END = 0x00020000
#
# GetFinalPathNameByHandle
#
VOLUME_NAME_DOS = 0x0 #default
VOLUME_NAME_GUID = 0x1
VOLUME_NAME_NT = 0x2
VOLUME_NAME_NONE = 0x4
FILE_NAME_NORMALIZED = 0x0 #default
FILE_NAME_OPENED = 0x8

# REGION ***

# REGION *** Application Family or OneCore Family ***

#
# JIT Debugging Info. This structure is defined to have constant size in
# both the emulated and native environment.
#
class JIT_DEBUG_INFO(CStructure):
    _fields_ = [
        ("dwSize", DWORD),
        ("dwProcessorArchitecture", DWORD),
        ("dwThreadID", DWORD),
        ("dwReserved0", DWORD),
        ("lpExceptionAddress", ULONG64),
        ("lpExceptionRecord", ULONG64),
        ("lpContextRecord", ULONG64)
    ]
LPJIT_DEBUG_INFO = POINTER(JIT_DEBUG_INFO)

JIT_DEBUG_INFO32 = JIT_DEBUG_INFO
JIT_DEBUG_INFO64 = JIT_DEBUG_INFO
LPJIT_DEBUG_INFO32 = LPJIT_DEBUG_INFO
LPJIT_DEBUG_INFO64 = LPJIT_DEBUG_INFO

# REGION ***

# REGION *** Application Family or OneCore Family or Games Family ***

LPEXCEPTION_POINTERS = PEXCEPTION_POINTERS

DRIVE_UNKNOWN     = 0
DRIVE_NO_ROOT_DIR = 1
DRIVE_REMOVABLE   = 2
DRIVE_FIXED       = 3
DRIVE_REMOTE      = 4
DRIVE_CDROM       = 5
DRIVE_RAMDISK     = 6

# REGION ***

# REGION *** Application Family or OneCore Family ***

GetFreeSpace = lambda w:                 (0x100000)

# REGION ***

# REGION *** Application Family or OneCore Family or Games Family ***

FILE_TYPE_UNKNOWN   = 0x0000
FILE_TYPE_DISK      = 0x0001
FILE_TYPE_CHAR      = 0x0002
FILE_TYPE_PIPE      = 0x0003
FILE_TYPE_REMOTE    = 0x8000


STD_INPUT_HANDLE    = DWORD(-10).value
STD_OUTPUT_HANDLE   = DWORD(-11).value
STD_ERROR_HANDLE    = DWORD(-12).value

class _S_OO(CStructure):
    _fields_ = [
        ("Offset", DWORD),
        ("OffsetHigh", DWORD)
    ]

class _U_SP(Union):
    _fields_ = [
        ("s", _S_OO),
        ("Pointer", PVOID)
    ]

class _OVERLAPPED(CStructure):
    _fields_ = [
        ("Internal", ULONG_PTR),
        ("InternalHigh", ULONG_PTR),
        ("u", _U_SP),
        ("hEvent", HANDLE)
    ]
OVERLAPPED = _OVERLAPPED
LPOVERLAPPED = POINTER(OVERLAPPED)

class _OVERLAPPED_ENTRY(CStructure):
    _fields_ = [
        ("lpCompletionKey", ULONG_PTR),
        ("lpOverlapped", LPOVERLAPPED),
        ("Internal", ULONG_PTR),
        ("dwNumberOfBytesTransferred", DWORD)
    ]
OVERLAPPED_ENTRY = _OVERLAPPED_ENTRY
LPOVERLAPPED_ENTRY = POINTER(OVERLAPPED_ENTRY)

PTHREAD_START_ROUTINE = WINAPI(DWORD, LPVOID)
LPTHREAD_START_ROUTINE = PTHREAD_START_ROUTINE

MAXINTATOM = 0xC000
MAKEINTATOM = lambda i: cast(ULONG_PTR(WORD(i).value).value, LPTSTR)
INVALID_ATOM = ATOM(0)

lstrcpynW = declare(kernel32.lstrcpynW, LPWSTR, LPWSTR, LPCWSTR, INT)
lstrcpynA = declare(kernel32.lstrcpynA, LPSTR, LPSTR, LPCSTR, INT)

class REASON_CONTEXT(CStructure):
    class _Reason(Union):
        class _Detailed(CStructure):
            _fields_ = [
                ("LocalizedReasonModule", HMODULE),
                ("LocalizedReasonId", ULONG),
                ("ReasonStringCount", ULONG),
                ("ReasonStrings", POINTER(LPWSTR))
            ]
        _fields_ = [
            ("Detailed", _Detailed),
            ("SimpleReasonString", LPWSTR)
        ]
    _fields_ = [
        ("Version", ULONG),
        ("Flags", DWORD),
        ("Reason", _Reason)
    ]
PREASON_CONTEXT = POINTER(REASON_CONTEXT)