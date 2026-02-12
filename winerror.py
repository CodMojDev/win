
"""
 *************************************************************************
 *                                                                       *
 *                                                                       *
 *   Copyright (c) Microsoft Corp. All rights reserved.                  *
 *                                                                       *
 *************************************************************************
"""

from . import cpreproc

if cpreproc.pragma_once("_WINERROR_"):
	#
	# Note: There is a slightly modified layout for HRESULT values below,
	#        after the heading "COM Error Codes".
	#
	# Search for "**** Available SYSTEM error codes ****" to find where to
	# insert new error codes
	#
	#  Values are 32 bit values laid out as follows:
	#
	#   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
	#   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
	#  +---+-+-+-----------------------+-------------------------------+
	#  |Sev|C|R|     Facility          |               Code            |
	#  +---+-+-+-----------------------+-------------------------------+
	#
	#  where
	#
	#      Sev - is the severity code
	#
	#          00 - Success
	#          01 - Informational
	#          10 - Warning
	#          11 - Error
	#
	#      C - is the Customer code flag
	#
	#      R - is a reserved bit
	#
	#      Facility - is the facility code
	#
	#      Code - is the facility's status code
	#
	#
	# Define the facility codes
	#
	FACILITY_NULL = 0 
	FACILITY_RPC = 1 
	FACILITY_DISPATCH = 2 
	FACILITY_STORAGE = 3 
	FACILITY_ITF = 4 
	FACILITY_WIN32 = 7 
	FACILITY_WINDOWS = 8 
	FACILITY_SSPI = 9 
	FACILITY_SECURITY = 9 
	FACILITY_CONTROL = 10 
	FACILITY_CERT = 11 
	FACILITY_INTERNET = 12 
	FACILITY_MEDIASERVER = 13 
	FACILITY_MSMQ = 14 
	FACILITY_SETUPAPI = 15 
	FACILITY_SCARD = 16 
	FACILITY_COMPLUS = 17 
	FACILITY_AAF = 18 
	FACILITY_URT = 19 
	FACILITY_ACS = 20 
	FACILITY_DPLAY = 21 
	FACILITY_UMI = 22 
	FACILITY_SXS = 23 
	FACILITY_WINDOWS_CE = 24 
	FACILITY_HTTP = 25 
	FACILITY_USERMODE_COMMONLOG = 26 
	FACILITY_WER = 27 
	FACILITY_USERMODE_FILTER_MANAGER = 31 
	FACILITY_BACKGROUNDCOPY = 32 
	FACILITY_CONFIGURATION = 33 
	FACILITY_WIA = 33 
	FACILITY_STATE_MANAGEMENT = 34 
	FACILITY_METADIRECTORY = 35 
	FACILITY_WINDOWSUPDATE = 36 
	FACILITY_DIRECTORYSERVICE = 37 
	FACILITY_GRAPHICS = 38 
	FACILITY_SHELL = 39 
	FACILITY_NAP = 39 
	FACILITY_TPM_SERVICES = 40 
	FACILITY_TPM_SOFTWARE = 41 
	FACILITY_UI = 42 
	FACILITY_XAML = 43 
	FACILITY_ACTION_QUEUE = 44 
	FACILITY_PLA = 48 
	FACILITY_WINDOWS_SETUP = 48 
	FACILITY_FVE = 49 
	FACILITY_FWP = 50 
	FACILITY_WINRM = 51 
	FACILITY_NDIS = 52 
	FACILITY_USERMODE_HYPERVISOR = 53 
	FACILITY_CMI = 54 
	FACILITY_USERMODE_VIRTUALIZATION = 55 
	FACILITY_USERMODE_VOLMGR = 56 
	FACILITY_BCD = 57 
	FACILITY_USERMODE_VHD = 58 
	FACILITY_USERMODE_HNS = 59 
	FACILITY_SDIAG = 60 
	FACILITY_WEBSERVICES = 61 
	FACILITY_WINPE = 61 
	FACILITY_WPN = 62 
	FACILITY_WINDOWS_STORE = 63 
	FACILITY_INPUT = 64 
	FACILITY_QUIC = 65 
	FACILITY_EAP = 66 
	FACILITY_WINDOWS_DEFENDER = 80 
	FACILITY_OPC = 81 
	FACILITY_XPS = 82 
	FACILITY_MBN = 84 
	FACILITY_POWERSHELL = 84 
	FACILITY_RAS = 83 
	FACILITY_P2P_INT = 98 
	FACILITY_P2P = 99 
	FACILITY_DAF = 100 
	FACILITY_BLUETOOTH_ATT = 101 
	FACILITY_AUDIO = 102 
	FACILITY_STATEREPOSITORY = 103 
	FACILITY_VISUALCPP = 109 
	FACILITY_SCRIPT = 112 
	FACILITY_PARSE = 113 
	FACILITY_BLB = 120 
	FACILITY_BLB_CLI = 121 
	FACILITY_WSBAPP = 122 
	FACILITY_BLBUI = 128 
	FACILITY_USN = 129 
	FACILITY_USERMODE_VOLSNAP = 130 
	FACILITY_TIERING = 131 
	FACILITY_WSB_ONLINE = 133 
	FACILITY_ONLINE_ID = 134 
	FACILITY_DEVICE_UPDATE_AGENT = 135 
	FACILITY_DRVSERVICING = 136 
	FACILITY_DLS = 153 
	FACILITY_DELIVERY_OPTIMIZATION = 208 
	FACILITY_USERMODE_SPACES = 231 
	FACILITY_USER_MODE_SECURITY_CORE = 232 
	FACILITY_USERMODE_LICENSING = 234 
	FACILITY_SOS = 160 
	FACILITY_DEBUGGERS = 176 
	FACILITY_SPP = 256 
	FACILITY_RESTORE = 256 
	FACILITY_DMSERVER = 256 
	FACILITY_DEPLOYMENT_SERVICES_SERVER = 257 
	FACILITY_DEPLOYMENT_SERVICES_IMAGING = 258 
	FACILITY_DEPLOYMENT_SERVICES_MANAGEMENT = 259 
	FACILITY_DEPLOYMENT_SERVICES_UTIL = 260 
	FACILITY_DEPLOYMENT_SERVICES_BINLSVC = 261 
	FACILITY_DEPLOYMENT_SERVICES_PXE = 263 
	FACILITY_DEPLOYMENT_SERVICES_TFTP = 264 
	FACILITY_DEPLOYMENT_SERVICES_TRANSPORT_MANAGEMENT = 272 
	FACILITY_DEPLOYMENT_SERVICES_DRIVER_PROVISIONING = 278 
	FACILITY_DEPLOYMENT_SERVICES_MULTICAST_SERVER = 289 
	FACILITY_DEPLOYMENT_SERVICES_MULTICAST_CLIENT = 290 
	FACILITY_DEPLOYMENT_SERVICES_CONTENT_PROVIDER = 293 
	FACILITY_LINGUISTIC_SERVICES = 305 
	FACILITY_AUDIOSTREAMING = 1094 
	FACILITY_TTD = 1490 
	FACILITY_ACCELERATOR = 1536 
	FACILITY_WMAAECMA = 1996 
	FACILITY_DIRECTMUSIC = 2168 
	FACILITY_DIRECT3D10 = 2169 
	FACILITY_DXGI = 2170 
	FACILITY_DXGI_DDI = 2171 
	FACILITY_DIRECT3D11 = 2172 
	FACILITY_DIRECT3D11_DEBUG = 2173 
	FACILITY_DIRECT3D12 = 2174 
	FACILITY_DIRECT3D12_DEBUG = 2175 
	FACILITY_DXCORE = 2176 
	FACILITY_LEAP = 2184 
	FACILITY_AUDCLNT = 2185 
	FACILITY_WINCODEC_DWRITE_DWM = 2200 
	FACILITY_WINML = 2192 
	FACILITY_DIRECT2D = 2201 
	FACILITY_DEFRAG = 2304 
	FACILITY_USERMODE_SDBUS = 2305 
	FACILITY_JSCRIPT = 2306 
	FACILITY_PIDGENX = 2561 
	FACILITY_EAS = 85 
	FACILITY_WEB = 885 
	FACILITY_WEB_SOCKET = 886 
	FACILITY_MOBILE = 1793 
	FACILITY_SQLITE = 1967 
	FACILITY_UTC = 1989 
	FACILITY_WEP = 2049 
	FACILITY_SYNCENGINE = 2050 
	FACILITY_XBOX = 2339 
	FACILITY_GAME = 2340 
	FACILITY_PIX = 2748 
	#
	# Define the severity codes
	#
	#
	# MessageId: ERROR_SUCCESS
	#
	# MessageText:
	#
	# The operation completed successfully.
	#
	ERROR_SUCCESS = 0 
	NO_ERROR = 0 # dderror
	SEC_E_OK = 0x00000000
	#
	# MessageId: ERROR_INVALID_FUNCTION
	#
	# MessageText:
	#
	# Incorrect function.
	#
	ERROR_INVALID_FUNCTION = 1 # dderror
	#
	# MessageId: ERROR_FILE_NOT_FOUND
	#
	# MessageText:
	#
	# The system cannot find the file specified.
	#
	ERROR_FILE_NOT_FOUND = 2 
	#
	# MessageId: ERROR_PATH_NOT_FOUND
	#
	# MessageText:
	#
	# The system cannot find the path specified.
	#
	ERROR_PATH_NOT_FOUND = 3 
	#
	# MessageId: ERROR_TOO_MANY_OPEN_FILES
	#
	# MessageText:
	#
	# The system cannot open the file.
	#
	ERROR_TOO_MANY_OPEN_FILES = 4 
	#
	# MessageId: ERROR_ACCESS_DENIED
	#
	# MessageText:
	#
	# Access is denied.
	#
	ERROR_ACCESS_DENIED = 5 
	#
	# MessageId: ERROR_INVALID_HANDLE
	#
	# MessageText:
	#
	# The handle is invalid.
	#
	ERROR_INVALID_HANDLE = 6 
	#
	# MessageId: ERROR_ARENA_TRASHED
	#
	# MessageText:
	#
	# The storage control blocks were destroyed.
	#
	ERROR_ARENA_TRASHED = 7 
	#
	# MessageId: ERROR_NOT_ENOUGH_MEMORY
	#
	# MessageText:
	#
	# Not enough memory resources are available to process this command.
	#
	ERROR_NOT_ENOUGH_MEMORY = 8 # dderror
	#
	# MessageId: ERROR_INVALID_BLOCK
	#
	# MessageText:
	#
	# The storage control block address is invalid.
	#
	ERROR_INVALID_BLOCK = 9 
	#
	# MessageId: ERROR_BAD_ENVIRONMENT
	#
	# MessageText:
	#
	# The environment is incorrect.
	#
	ERROR_BAD_ENVIRONMENT = 10 
	#
	# MessageId: ERROR_BAD_FORMAT
	#
	# MessageText:
	#
	# An attempt was made to load a program with an incorrect format.
	#
	ERROR_BAD_FORMAT = 11 
	#
	# MessageId: ERROR_INVALID_ACCESS
	#
	# MessageText:
	#
	# The access code is invalid.
	#
	ERROR_INVALID_ACCESS = 12 
	#
	# MessageId: ERROR_INVALID_DATA
	#
	# MessageText:
	#
	# The data is invalid.
	#
	ERROR_INVALID_DATA = 13 
	#
	# MessageId: ERROR_OUTOFMEMORY
	#
	# MessageText:
	#
	# Not enough memory resources are available to complete this operation.
	#
	ERROR_OUTOFMEMORY = 14 
	#
	# MessageId: ERROR_INVALID_DRIVE
	#
	# MessageText:
	#
	# The system cannot find the drive specified.
	#
	ERROR_INVALID_DRIVE = 15 
	#
	# MessageId: ERROR_CURRENT_DIRECTORY
	#
	# MessageText:
	#
	# The directory cannot be removed.
	#
	ERROR_CURRENT_DIRECTORY = 16 
	#
	# MessageId: ERROR_NOT_SAME_DEVICE
	#
	# MessageText:
	#
	# The system cannot move the file to a different disk drive.
	#
	ERROR_NOT_SAME_DEVICE = 17 
	#
	# MessageId: ERROR_NO_MORE_FILES
	#
	# MessageText:
	#
	# There are no more files.
	#
	ERROR_NO_MORE_FILES = 18 
	#
	# MessageId: ERROR_WRITE_PROTECT
	#
	# MessageText:
	#
	# The media is write protected.
	#
	ERROR_WRITE_PROTECT = 19 
	#
	# MessageId: ERROR_BAD_UNIT
	#
	# MessageText:
	#
	# The system cannot find the device specified.
	#
	ERROR_BAD_UNIT = 20 
	#
	# MessageId: ERROR_NOT_READY
	#
	# MessageText:
	#
	# The device is not ready.
	#
	ERROR_NOT_READY = 21 
	#
	# MessageId: ERROR_BAD_COMMAND
	#
	# MessageText:
	#
	# The device does not recognize the command.
	#
	ERROR_BAD_COMMAND = 22 
	#
	# MessageId: ERROR_CRC
	#
	# MessageText:
	#
	# Data error (cyclic redundancy check).
	#
	ERROR_CRC = 23 
	#
	# MessageId: ERROR_BAD_LENGTH
	#
	# MessageText:
	#
	# The program issued a command but the command length is incorrect.
	#
	ERROR_BAD_LENGTH = 24 
	#
	# MessageId: ERROR_SEEK
	#
	# MessageText:
	#
	# The drive cannot locate a specific area or track on the disk.
	#
	ERROR_SEEK = 25 
	#
	# MessageId: ERROR_NOT_DOS_DISK
	#
	# MessageText:
	#
	# The specified disk or diskette cannot be accessed.
	#
	ERROR_NOT_DOS_DISK = 26 
	#
	# MessageId: ERROR_SECTOR_NOT_FOUND
	#
	# MessageText:
	#
	# The drive cannot find the sector requested.
	#
	ERROR_SECTOR_NOT_FOUND = 27 
	#
	# MessageId: ERROR_OUT_OF_PAPER
	#
	# MessageText:
	#
	# The printer is out of paper.
	#
	ERROR_OUT_OF_PAPER = 28 
	#
	# MessageId: ERROR_WRITE_FAULT
	#
	# MessageText:
	#
	# The system cannot write to the specified device.
	#
	ERROR_WRITE_FAULT = 29 
	#
	# MessageId: ERROR_READ_FAULT
	#
	# MessageText:
	#
	# The system cannot read from the specified device.
	#
	ERROR_READ_FAULT = 30 
	#
	# MessageId: ERROR_GEN_FAILURE
	#
	# MessageText:
	#
	# A device attached to the system is not functioning.
	#
	ERROR_GEN_FAILURE = 31 
	#
	# MessageId: ERROR_SHARING_VIOLATION
	#
	# MessageText:
	#
	# The process cannot access the file because it is being used by another process.
	#
	ERROR_SHARING_VIOLATION = 32 
	#
	# MessageId: ERROR_LOCK_VIOLATION
	#
	# MessageText:
	#
	# The process cannot access the file because another process has locked a portion of the file.
	#
	ERROR_LOCK_VIOLATION = 33 
	#
	# MessageId: ERROR_WRONG_DISK
	#
	# MessageText:
	#
	# The wrong diskette is in the drive.
	# Insert %2 (Volume Serial Number: %3) into drive %1.
	#
	ERROR_WRONG_DISK = 34 
	#
	# MessageId: ERROR_SHARING_BUFFER_EXCEEDED
	#
	# MessageText:
	#
	# Too many files opened for sharing.
	#
	ERROR_SHARING_BUFFER_EXCEEDED = 36 
	#
	# MessageId: ERROR_HANDLE_EOF
	#
	# MessageText:
	#
	# Reached the end of the file.
	#
	ERROR_HANDLE_EOF = 38 
	#
	# MessageId: ERROR_HANDLE_DISK_FULL
	#
	# MessageText:
	#
	# The disk is full.
	#
	ERROR_HANDLE_DISK_FULL = 39 
	#
	# MessageId: ERROR_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The request is not supported.
	#
	ERROR_NOT_SUPPORTED = 50 
	#
	# MessageId: ERROR_REM_NOT_LIST
	#
	# MessageText:
	#
	# Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator.
	#
	ERROR_REM_NOT_LIST = 51 
	#
	# MessageId: ERROR_DUP_NAME
	#
	# MessageText:
	#
	# You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name.
	#
	ERROR_DUP_NAME = 52 
	#
	# MessageId: ERROR_BAD_NETPATH
	#
	# MessageText:
	#
	# The network path was not found.
	#
	ERROR_BAD_NETPATH = 53 
	#
	# MessageId: ERROR_NETWORK_BUSY
	#
	# MessageText:
	#
	# The network is busy.
	#
	ERROR_NETWORK_BUSY = 54 
	#
	# MessageId: ERROR_DEV_NOT_EXIST
	#
	# MessageText:
	#
	# The specified network resource or device is no longer available.
	#
	ERROR_DEV_NOT_EXIST = 55 # dderror
	#
	# MessageId: ERROR_TOO_MANY_CMDS
	#
	# MessageText:
	#
	# The network BIOS command limit has been reached.
	#
	ERROR_TOO_MANY_CMDS = 56 
	#
	# MessageId: ERROR_ADAP_HDW_ERR
	#
	# MessageText:
	#
	# A network adapter hardware error occurred.
	#
	ERROR_ADAP_HDW_ERR = 57 
	#
	# MessageId: ERROR_BAD_NET_RESP
	#
	# MessageText:
	#
	# The specified server cannot perform the requested operation.
	#
	ERROR_BAD_NET_RESP = 58 
	#
	# MessageId: ERROR_UNEXP_NET_ERR
	#
	# MessageText:
	#
	# An unexpected network error occurred.
	#
	ERROR_UNEXP_NET_ERR = 59 
	#
	# MessageId: ERROR_BAD_REM_ADAP
	#
	# MessageText:
	#
	# The remote adapter is not compatible.
	#
	ERROR_BAD_REM_ADAP = 60 
	#
	# MessageId: ERROR_PRINTQ_FULL
	#
	# MessageText:
	#
	# The printer queue is full.
	#
	ERROR_PRINTQ_FULL = 61 
	#
	# MessageId: ERROR_NO_SPOOL_SPACE
	#
	# MessageText:
	#
	# Space to store the file waiting to be printed is not available on the server.
	#
	ERROR_NO_SPOOL_SPACE = 62 
	#
	# MessageId: ERROR_PRINT_CANCELLED
	#
	# MessageText:
	#
	# Your file waiting to be printed was deleted.
	#
	ERROR_PRINT_CANCELLED = 63 
	#
	# MessageId: ERROR_NETNAME_DELETED
	#
	# MessageText:
	#
	# The specified network name is no longer available.
	#
	ERROR_NETNAME_DELETED = 64 
	#
	# MessageId: ERROR_NETWORK_ACCESS_DENIED
	#
	# MessageText:
	#
	# Network access is denied.
	#
	ERROR_NETWORK_ACCESS_DENIED = 65 
	#
	# MessageId: ERROR_BAD_DEV_TYPE
	#
	# MessageText:
	#
	# The network resource type is not correct.
	#
	ERROR_BAD_DEV_TYPE = 66 
	#
	# MessageId: ERROR_BAD_NET_NAME
	#
	# MessageText:
	#
	# The network name cannot be found.
	#
	ERROR_BAD_NET_NAME = 67 
	#
	# MessageId: ERROR_TOO_MANY_NAMES
	#
	# MessageText:
	#
	# The name limit for the local computer network adapter card was exceeded.
	#
	ERROR_TOO_MANY_NAMES = 68 
	#
	# MessageId: ERROR_TOO_MANY_SESS
	#
	# MessageText:
	#
	# The network BIOS session limit was exceeded.
	#
	ERROR_TOO_MANY_SESS = 69 
	#
	# MessageId: ERROR_SHARING_PAUSED
	#
	# MessageText:
	#
	# The remote server has been paused or is in the process of being started.
	#
	ERROR_SHARING_PAUSED = 70 
	#
	# MessageId: ERROR_REQ_NOT_ACCEP
	#
	# MessageText:
	#
	# No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.
	#
	ERROR_REQ_NOT_ACCEP = 71 
	#
	# MessageId: ERROR_REDIR_PAUSED
	#
	# MessageText:
	#
	# The specified printer or disk device has been paused.
	#
	ERROR_REDIR_PAUSED = 72 
	#
	# MessageId: ERROR_FILE_EXISTS
	#
	# MessageText:
	#
	# The file exists.
	#
	ERROR_FILE_EXISTS = 80 
	#
	# MessageId: ERROR_CANNOT_MAKE
	#
	# MessageText:
	#
	# The directory or file cannot be created.
	#
	ERROR_CANNOT_MAKE = 82 
	#
	# MessageId: ERROR_FAIL_I24
	#
	# MessageText:
	#
	# Fail on INT 24.
	#
	ERROR_FAIL_I24 = 83 
	#
	# MessageId: ERROR_OUT_OF_STRUCTURES
	#
	# MessageText:
	#
	# Storage to process this request is not available.
	#
	ERROR_OUT_OF_STRUCTURES = 84 
	#
	# MessageId: ERROR_ALREADY_ASSIGNED
	#
	# MessageText:
	#
	# The local device name is already in use.
	#
	ERROR_ALREADY_ASSIGNED = 85 
	#
	# MessageId: ERROR_INVALID_PASSWORD
	#
	# MessageText:
	#
	# The specified network password is not correct.
	#
	ERROR_INVALID_PASSWORD = 86 
	#
	# MessageId: ERROR_INVALID_PARAMETER
	#
	# MessageText:
	#
	# The parameter is incorrect.
	#
	ERROR_INVALID_PARAMETER = 87 # dderror
	#
	# MessageId: ERROR_NET_WRITE_FAULT
	#
	# MessageText:
	#
	# A write fault occurred on the network.
	#
	ERROR_NET_WRITE_FAULT = 88 
	#
	# MessageId: ERROR_NO_PROC_SLOTS
	#
	# MessageText:
	#
	# The system cannot start another process at this time.
	#
	ERROR_NO_PROC_SLOTS = 89 
	#
	# MessageId: ERROR_TOO_MANY_SEMAPHORES
	#
	# MessageText:
	#
	# Cannot create another system semaphore.
	#
	ERROR_TOO_MANY_SEMAPHORES = 100 
	#
	# MessageId: ERROR_EXCL_SEM_ALREADY_OWNED
	#
	# MessageText:
	#
	# The exclusive semaphore is owned by another process.
	#
	ERROR_EXCL_SEM_ALREADY_OWNED = 101 
	#
	# MessageId: ERROR_SEM_IS_SET
	#
	# MessageText:
	#
	# The semaphore is set and cannot be closed.
	#
	ERROR_SEM_IS_SET = 102 
	#
	# MessageId: ERROR_TOO_MANY_SEM_REQUESTS
	#
	# MessageText:
	#
	# The semaphore cannot be set again.
	#
	ERROR_TOO_MANY_SEM_REQUESTS = 103 
	#
	# MessageId: ERROR_INVALID_AT_INTERRUPT_TIME
	#
	# MessageText:
	#
	# Cannot request exclusive semaphores at interrupt time.
	#
	ERROR_INVALID_AT_INTERRUPT_TIME = 104 
	#
	# MessageId: ERROR_SEM_OWNER_DIED
	#
	# MessageText:
	#
	# The previous ownership of this semaphore has ended.
	#
	ERROR_SEM_OWNER_DIED = 105 
	#
	# MessageId: ERROR_SEM_USER_LIMIT
	#
	# MessageText:
	#
	# Insert the diskette for drive %1.
	#
	ERROR_SEM_USER_LIMIT = 106 
	#
	# MessageId: ERROR_DISK_CHANGE
	#
	# MessageText:
	#
	# The program stopped because an alternate diskette was not inserted.
	#
	ERROR_DISK_CHANGE = 107 
	#
	# MessageId: ERROR_DRIVE_LOCKED
	#
	# MessageText:
	#
	# The disk is in use or locked by another process.
	#
	ERROR_DRIVE_LOCKED = 108 
	#
	# MessageId: ERROR_BROKEN_PIPE
	#
	# MessageText:
	#
	# The pipe has been ended.
	#
	ERROR_BROKEN_PIPE = 109 
	#
	# MessageId: ERROR_OPEN_FAILED
	#
	# MessageText:
	#
	# The system cannot open the device or file specified.
	#
	ERROR_OPEN_FAILED = 110 
	#
	# MessageId: ERROR_BUFFER_OVERFLOW
	#
	# MessageText:
	#
	# The file name is too long.
	#
	ERROR_BUFFER_OVERFLOW = 111 
	#
	# MessageId: ERROR_DISK_FULL
	#
	# MessageText:
	#
	# There is not enough space on the disk.
	#
	ERROR_DISK_FULL = 112 
	#
	# MessageId: ERROR_NO_MORE_SEARCH_HANDLES
	#
	# MessageText:
	#
	# No more internal file identifiers available.
	#
	ERROR_NO_MORE_SEARCH_HANDLES = 113 
	#
	# MessageId: ERROR_INVALID_TARGET_HANDLE
	#
	# MessageText:
	#
	# The target internal file identifier is incorrect.
	#
	ERROR_INVALID_TARGET_HANDLE = 114 
	#
	# MessageId: ERROR_INVALID_CATEGORY
	#
	# MessageText:
	#
	# The IOCTL call made by the application program is not correct.
	#
	ERROR_INVALID_CATEGORY = 117 
	#
	# MessageId: ERROR_INVALID_VERIFY_SWITCH
	#
	# MessageText:
	#
	# The verify-on-write switch parameter value is not correct.
	#
	ERROR_INVALID_VERIFY_SWITCH = 118 
	#
	# MessageId: ERROR_BAD_DRIVER_LEVEL
	#
	# MessageText:
	#
	# The system does not support the command requested.
	#
	ERROR_BAD_DRIVER_LEVEL = 119 
	#
	# MessageId: ERROR_CALL_NOT_IMPLEMENTED
	#
	# MessageText:
	#
	# This function is not supported on this system.
	#
	ERROR_CALL_NOT_IMPLEMENTED = 120 
	#
	# MessageId: ERROR_SEM_TIMEOUT
	#
	# MessageText:
	#
	# The semaphore timeout period has expired.
	#
	ERROR_SEM_TIMEOUT = 121 
	#
	# MessageId: ERROR_INSUFFICIENT_BUFFER
	#
	# MessageText:
	#
	# The data area passed to a system call is too small.
	#
	ERROR_INSUFFICIENT_BUFFER = 122 # dderror
	#
	# MessageId: ERROR_INVALID_NAME
	#
	# MessageText:
	#
	# The filename, directory name, or volume label syntax is incorrect.
	#
	ERROR_INVALID_NAME = 123 # dderror
	#
	# MessageId: ERROR_INVALID_LEVEL
	#
	# MessageText:
	#
	# The system call level is not correct.
	#
	ERROR_INVALID_LEVEL = 124 
	#
	# MessageId: ERROR_NO_VOLUME_LABEL
	#
	# MessageText:
	#
	# The disk has no volume label.
	#
	ERROR_NO_VOLUME_LABEL = 125 
	#
	# MessageId: ERROR_MOD_NOT_FOUND
	#
	# MessageText:
	#
	# The specified module could not be found.
	#
	ERROR_MOD_NOT_FOUND = 126 
	#
	# MessageId: ERROR_PROC_NOT_FOUND
	#
	# MessageText:
	#
	# The specified procedure could not be found.
	#
	ERROR_PROC_NOT_FOUND = 127 
	#
	# MessageId: ERROR_WAIT_NO_CHILDREN
	#
	# MessageText:
	#
	# There are no child processes to wait for.
	#
	ERROR_WAIT_NO_CHILDREN = 128 
	#
	# MessageId: ERROR_CHILD_NOT_COMPLETE
	#
	# MessageText:
	#
	# The %1 application cannot be run in Win32 mode.
	#
	ERROR_CHILD_NOT_COMPLETE = 129 
	#
	# MessageId: ERROR_DIRECT_ACCESS_HANDLE
	#
	# MessageText:
	#
	# Attempt to use a file handle to an open disk partition for an operation other than raw disk I/O.
	#
	ERROR_DIRECT_ACCESS_HANDLE = 130 
	#
	# MessageId: ERROR_NEGATIVE_SEEK
	#
	# MessageText:
	#
	# An attempt was made to move the file pointer before the beginning of the file.
	#
	ERROR_NEGATIVE_SEEK = 131 
	#
	# MessageId: ERROR_SEEK_ON_DEVICE
	#
	# MessageText:
	#
	# The file pointer cannot be set on the specified device or file.
	#
	ERROR_SEEK_ON_DEVICE = 132 
	#
	# MessageId: ERROR_IS_JOIN_TARGET
	#
	# MessageText:
	#
	# A JOIN or SUBST command cannot be used for a drive that contains previously joined drives.
	#
	ERROR_IS_JOIN_TARGET = 133 
	#
	# MessageId: ERROR_IS_JOINED
	#
	# MessageText:
	#
	# An attempt was made to use a JOIN or SUBST command on a drive that has already been joined.
	#
	ERROR_IS_JOINED = 134 
	#
	# MessageId: ERROR_IS_SUBSTED
	#
	# MessageText:
	#
	# An attempt was made to use a JOIN or SUBST command on a drive that has already been substituted.
	#
	ERROR_IS_SUBSTED = 135 
	#
	# MessageId: ERROR_NOT_JOINED
	#
	# MessageText:
	#
	# The system tried to delete the JOIN of a drive that is not joined.
	#
	ERROR_NOT_JOINED = 136 
	#
	# MessageId: ERROR_NOT_SUBSTED
	#
	# MessageText:
	#
	# The system tried to delete the substitution of a drive that is not substituted.
	#
	ERROR_NOT_SUBSTED = 137 
	#
	# MessageId: ERROR_JOIN_TO_JOIN
	#
	# MessageText:
	#
	# The system tried to join a drive to a directory on a joined drive.
	#
	ERROR_JOIN_TO_JOIN = 138 
	#
	# MessageId: ERROR_SUBST_TO_SUBST
	#
	# MessageText:
	#
	# The system tried to substitute a drive to a directory on a substituted drive.
	#
	ERROR_SUBST_TO_SUBST = 139 
	#
	# MessageId: ERROR_JOIN_TO_SUBST
	#
	# MessageText:
	#
	# The system tried to join a drive to a directory on a substituted drive.
	#
	ERROR_JOIN_TO_SUBST = 140 
	#
	# MessageId: ERROR_SUBST_TO_JOIN
	#
	# MessageText:
	#
	# The system tried to SUBST a drive to a directory on a joined drive.
	#
	ERROR_SUBST_TO_JOIN = 141 
	#
	# MessageId: ERROR_BUSY_DRIVE
	#
	# MessageText:
	#
	# The system cannot perform a JOIN or SUBST at this time.
	#
	ERROR_BUSY_DRIVE = 142 
	#
	# MessageId: ERROR_SAME_DRIVE
	#
	# MessageText:
	#
	# The system cannot join or substitute a drive to or for a directory on the same drive.
	#
	ERROR_SAME_DRIVE = 143 
	#
	# MessageId: ERROR_DIR_NOT_ROOT
	#
	# MessageText:
	#
	# The directory is not a subdirectory of the root directory.
	#
	ERROR_DIR_NOT_ROOT = 144 
	#
	# MessageId: ERROR_DIR_NOT_EMPTY
	#
	# MessageText:
	#
	# The directory is not empty.
	#
	ERROR_DIR_NOT_EMPTY = 145 
	#
	# MessageId: ERROR_IS_SUBST_PATH
	#
	# MessageText:
	#
	# The path specified is being used in a substitute.
	#
	ERROR_IS_SUBST_PATH = 146 
	#
	# MessageId: ERROR_IS_JOIN_PATH
	#
	# MessageText:
	#
	# Not enough resources are available to process this command.
	#
	ERROR_IS_JOIN_PATH = 147 
	#
	# MessageId: ERROR_PATH_BUSY
	#
	# MessageText:
	#
	# The path specified cannot be used at this time.
	#
	ERROR_PATH_BUSY = 148 
	#
	# MessageId: ERROR_IS_SUBST_TARGET
	#
	# MessageText:
	#
	# An attempt was made to join or substitute a drive for which a directory on the drive is the target of a previous substitute.
	#
	ERROR_IS_SUBST_TARGET = 149 
	#
	# MessageId: ERROR_SYSTEM_TRACE
	#
	# MessageText:
	#
	# System trace information was not specified in your CONFIG.SYS file, or tracing is disallowed.
	#
	ERROR_SYSTEM_TRACE = 150 
	#
	# MessageId: ERROR_INVALID_EVENT_COUNT
	#
	# MessageText:
	#
	# The number of specified semaphore events for DosMuxSemWait is not correct.
	#
	ERROR_INVALID_EVENT_COUNT = 151 
	#
	# MessageId: ERROR_TOO_MANY_MUXWAITERS
	#
	# MessageText:
	#
	# DosMuxSemWait did not execute; too many semaphores are already set.
	#
	ERROR_TOO_MANY_MUXWAITERS = 152 
	#
	# MessageId: ERROR_INVALID_LIST_FORMAT
	#
	# MessageText:
	#
	# The DosMuxSemWait list is not correct.
	#
	ERROR_INVALID_LIST_FORMAT = 153 
	#
	# MessageId: ERROR_LABEL_TOO_LONG
	#
	# MessageText:
	#
	# The volume label you entered exceeds the label character limit of the target file system.
	#
	ERROR_LABEL_TOO_LONG = 154 
	#
	# MessageId: ERROR_TOO_MANY_TCBS
	#
	# MessageText:
	#
	# Cannot create another thread.
	#
	ERROR_TOO_MANY_TCBS = 155 
	#
	# MessageId: ERROR_SIGNAL_REFUSED
	#
	# MessageText:
	#
	# The recipient process has refused the signal.
	#
	ERROR_SIGNAL_REFUSED = 156 
	#
	# MessageId: ERROR_DISCARDED
	#
	# MessageText:
	#
	# The segment is already discarded and cannot be locked.
	#
	ERROR_DISCARDED = 157 
	#
	# MessageId: ERROR_NOT_LOCKED
	#
	# MessageText:
	#
	# The segment is already unlocked.
	#
	ERROR_NOT_LOCKED = 158 
	#
	# MessageId: ERROR_BAD_THREADID_ADDR
	#
	# MessageText:
	#
	# The address for the thread ID is not correct.
	#
	ERROR_BAD_THREADID_ADDR = 159 
	#
	# MessageId: ERROR_BAD_ARGUMENTS
	#
	# MessageText:
	#
	# One or more arguments are not correct.
	#
	ERROR_BAD_ARGUMENTS = 160 
	#
	# MessageId: ERROR_BAD_PATHNAME
	#
	# MessageText:
	#
	# The specified path is invalid.
	#
	ERROR_BAD_PATHNAME = 161 
	#
	# MessageId: ERROR_SIGNAL_PENDING
	#
	# MessageText:
	#
	# A signal is already pending.
	#
	ERROR_SIGNAL_PENDING = 162 
	#
	# MessageId: ERROR_MAX_THRDS_REACHED
	#
	# MessageText:
	#
	# No more threads can be created in the system.
	#
	ERROR_MAX_THRDS_REACHED = 164 
	#
	# MessageId: ERROR_LOCK_FAILED
	#
	# MessageText:
	#
	# Unable to lock a region of a file.
	#
	ERROR_LOCK_FAILED = 167 
	#
	# MessageId: ERROR_BUSY
	#
	# MessageText:
	#
	# The requested resource is in use.
	#
	ERROR_BUSY = 170 # dderror
	#
	# MessageId: ERROR_DEVICE_SUPPORT_IN_PROGRESS
	#
	# MessageText:
	#
	# Device's command support detection is in progress.
	#
	ERROR_DEVICE_SUPPORT_IN_PROGRESS = 171 
	#
	# MessageId: ERROR_CANCEL_VIOLATION
	#
	# MessageText:
	#
	# A lock request was not outstanding for the supplied cancel region.
	#
	ERROR_CANCEL_VIOLATION = 173 
	#
	# MessageId: ERROR_ATOMIC_LOCKS_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The file system does not support atomic changes to the lock type.
	#
	ERROR_ATOMIC_LOCKS_NOT_SUPPORTED = 174 
	#
	# MessageId: ERROR_INVALID_SEGMENT_NUMBER
	#
	# MessageText:
	#
	# The system detected a segment number that was not correct.
	#
	ERROR_INVALID_SEGMENT_NUMBER = 180 
	#
	# MessageId: ERROR_INVALID_ORDINAL
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_ORDINAL = 182 
	#
	# MessageId: ERROR_ALREADY_EXISTS
	#
	# MessageText:
	#
	# Cannot create a file when that file already exists.
	#
	ERROR_ALREADY_EXISTS = 183 
	#
	# MessageId: ERROR_INVALID_FLAG_NUMBER
	#
	# MessageText:
	#
	# The flag passed is not correct.
	#
	ERROR_INVALID_FLAG_NUMBER = 186 
	#
	# MessageId: ERROR_SEM_NOT_FOUND
	#
	# MessageText:
	#
	# The specified system semaphore name was not found.
	#
	ERROR_SEM_NOT_FOUND = 187 
	#
	# MessageId: ERROR_INVALID_STARTING_CODESEG
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_STARTING_CODESEG = 188 
	#
	# MessageId: ERROR_INVALID_STACKSEG
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_STACKSEG = 189 
	#
	# MessageId: ERROR_INVALID_MODULETYPE
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_MODULETYPE = 190 
	#
	# MessageId: ERROR_INVALID_EXE_SIGNATURE
	#
	# MessageText:
	#
	# Cannot run %1 in Win32 mode.
	#
	ERROR_INVALID_EXE_SIGNATURE = 191 
	#
	# MessageId: ERROR_EXE_MARKED_INVALID
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_EXE_MARKED_INVALID = 192 
	#
	# MessageId: ERROR_BAD_EXE_FORMAT
	#
	# MessageText:
	#
	# %1 is not a valid Win32 application.
	#
	ERROR_BAD_EXE_FORMAT = 193 
	#
	# MessageId: ERROR_ITERATED_DATA_EXCEEDS_64k
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_ITERATED_DATA_EXCEEDS_64k = 194 
	#
	# MessageId: ERROR_INVALID_MINALLOCSIZE
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_MINALLOCSIZE = 195 
	#
	# MessageId: ERROR_DYNLINK_FROM_INVALID_RING
	#
	# MessageText:
	#
	# The operating system cannot run this application program.
	#
	ERROR_DYNLINK_FROM_INVALID_RING = 196 
	#
	# MessageId: ERROR_IOPL_NOT_ENABLED
	#
	# MessageText:
	#
	# The operating system is not presently configured to run this application.
	#
	ERROR_IOPL_NOT_ENABLED = 197 
	#
	# MessageId: ERROR_INVALID_SEGDPL
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INVALID_SEGDPL = 198 
	#
	# MessageId: ERROR_AUTODATASEG_EXCEEDS_64k
	#
	# MessageText:
	#
	# The operating system cannot run this application program.
	#
	ERROR_AUTODATASEG_EXCEEDS_64k = 199 
	#
	# MessageId: ERROR_RING2SEG_MUST_BE_MOVABLE
	#
	# MessageText:
	#
	# The code segment cannot be greater than or equal to 64K.
	#
	ERROR_RING2SEG_MUST_BE_MOVABLE = 200 
	#
	# MessageId: ERROR_RELOC_CHAIN_XEEDS_SEGLIM
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_RELOC_CHAIN_XEEDS_SEGLIM = 201 
	#
	# MessageId: ERROR_INFLOOP_IN_RELOC_CHAIN
	#
	# MessageText:
	#
	# The operating system cannot run %1.
	#
	ERROR_INFLOOP_IN_RELOC_CHAIN = 202 
	#
	# MessageId: ERROR_ENVVAR_NOT_FOUND
	#
	# MessageText:
	#
	# The system could not find the environment option that was entered.
	#
	ERROR_ENVVAR_NOT_FOUND = 203 
	#
	# MessageId: ERROR_NO_SIGNAL_SENT
	#
	# MessageText:
	#
	# No process in the command subtree has a signal handler.
	#
	ERROR_NO_SIGNAL_SENT = 205 
	#
	# MessageId: ERROR_FILENAME_EXCED_RANGE
	#
	# MessageText:
	#
	# The filename or extension is too long.
	#
	ERROR_FILENAME_EXCED_RANGE = 206 
	#
	# MessageId: ERROR_RING2_STACK_IN_USE
	#
	# MessageText:
	#
	# The ring 2 stack is in use.
	#
	ERROR_RING2_STACK_IN_USE = 207 
	#
	# MessageId: ERROR_META_EXPANSION_TOO_LONG
	#
	# MessageText:
	#
	# The global filename characters, * or ?, are entered incorrectly or too many global filename characters are specified.
	#
	ERROR_META_EXPANSION_TOO_LONG = 208 
	#
	# MessageId: ERROR_INVALID_SIGNAL_NUMBER
	#
	# MessageText:
	#
	# The signal being posted is not correct.
	#
	ERROR_INVALID_SIGNAL_NUMBER = 209 
	#
	# MessageId: ERROR_THREAD_1_INACTIVE
	#
	# MessageText:
	#
	# The signal handler cannot be set.
	#
	ERROR_THREAD_1_INACTIVE = 210 
	#
	# MessageId: ERROR_LOCKED
	#
	# MessageText:
	#
	# The segment is locked and cannot be reallocated.
	#
	ERROR_LOCKED = 212 
	#
	# MessageId: ERROR_TOO_MANY_MODULES
	#
	# MessageText:
	#
	# Too many dynamic-link modules are attached to this program or dynamic-link module.
	#
	ERROR_TOO_MANY_MODULES = 214 
	#
	# MessageId: ERROR_NESTING_NOT_ALLOWED
	#
	# MessageText:
	#
	# Cannot nest calls to LoadModule.
	#
	ERROR_NESTING_NOT_ALLOWED = 215 
	#
	# MessageId: ERROR_EXE_MACHINE_TYPE_MISMATCH
	#
	# MessageText:
	#
	# This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher.
	#
	ERROR_EXE_MACHINE_TYPE_MISMATCH = 216 
	#
	# MessageId: ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY
	#
	# MessageText:
	#
	# The image file %1 is signed, unable to modify.
	#
	ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY = 217 
	#
	# MessageId: ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY
	#
	# MessageText:
	#
	# The image file %1 is strong signed, unable to modify.
	#
	ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY = 218 
	#
	# MessageId: ERROR_FILE_CHECKED_OUT
	#
	# MessageText:
	#
	# This file is checked out or locked for editing by another user.
	#
	ERROR_FILE_CHECKED_OUT = 220 
	#
	# MessageId: ERROR_CHECKOUT_REQUIRED
	#
	# MessageText:
	#
	# The file must be checked out before saving changes.
	#
	ERROR_CHECKOUT_REQUIRED = 221 
	#
	# MessageId: ERROR_BAD_FILE_TYPE
	#
	# MessageText:
	#
	# The file type being saved or retrieved has been blocked.
	#
	ERROR_BAD_FILE_TYPE = 222 
	#
	# MessageId: ERROR_FILE_TOO_LARGE
	#
	# MessageText:
	#
	# The file size exceeds the limit allowed and cannot be saved.
	#
	ERROR_FILE_TOO_LARGE = 223 
	#
	# MessageId: ERROR_FORMS_AUTH_REQUIRED
	#
	# MessageText:
	#
	# Access Denied. Before opening files in this location, you must first add the web site to your trusted sites list, browse to the web site, and select the option to login automatically.
	#
	ERROR_FORMS_AUTH_REQUIRED = 224 
	#
	# MessageId: ERROR_VIRUS_INFECTED
	#
	# MessageText:
	#
	# Operation did not complete successfully because the file contains a virus or potentially unwanted software.
	#
	ERROR_VIRUS_INFECTED = 225 
	#
	# MessageId: ERROR_VIRUS_DELETED
	#
	# MessageText:
	#
	# This file contains a virus or potentially unwanted software and cannot be opened. Due to the nature of this virus or potentially unwanted software, the file has been removed from this location.
	#
	ERROR_VIRUS_DELETED = 226 
	#
	# MessageId: ERROR_PIPE_LOCAL
	#
	# MessageText:
	#
	# The pipe is local.
	#
	ERROR_PIPE_LOCAL = 229 
	#
	# MessageId: ERROR_BAD_PIPE
	#
	# MessageText:
	#
	# The pipe state is invalid.
	#
	ERROR_BAD_PIPE = 230 
	#
	# MessageId: ERROR_PIPE_BUSY
	#
	# MessageText:
	#
	# All pipe instances are busy.
	#
	ERROR_PIPE_BUSY = 231 
	#
	# MessageId: ERROR_NO_DATA
	#
	# MessageText:
	#
	# The pipe is being closed.
	#
	ERROR_NO_DATA = 232 
	#
	# MessageId: ERROR_PIPE_NOT_CONNECTED
	#
	# MessageText:
	#
	# No process is on the other end of the pipe.
	#
	ERROR_PIPE_NOT_CONNECTED = 233 
	#
	# MessageId: ERROR_MORE_DATA
	#
	# MessageText:
	#
	# More data is available.
	#
	ERROR_MORE_DATA = 234 # dderror
	#
	# MessageId: ERROR_NO_WORK_DONE
	#
	# MessageText:
	#
	# The action requested resulted in no work being done. Error-style clean-up has been performed.
	#
	ERROR_NO_WORK_DONE = 235 
	#
	# MessageId: ERROR_VC_DISCONNECTED
	#
	# MessageText:
	#
	# The session was canceled.
	#
	ERROR_VC_DISCONNECTED = 240 
	#
	# MessageId: ERROR_INVALID_EA_NAME
	#
	# MessageText:
	#
	# The specified extended attribute name was invalid.
	#
	ERROR_INVALID_EA_NAME = 254 
	#
	# MessageId: ERROR_EA_LIST_INCONSISTENT
	#
	# MessageText:
	#
	# The extended attributes are inconsistent.
	#
	ERROR_EA_LIST_INCONSISTENT = 255 
	#
	# MessageId: WAIT_TIMEOUT
	#
	# MessageText:
	#
	# The wait operation timed out.
	#
	WAIT_TIMEOUT = 258 # dderror
	#
	# MessageId: ERROR_NO_MORE_ITEMS
	#
	# MessageText:
	#
	# No more data is available.
	#
	ERROR_NO_MORE_ITEMS = 259 
	#
	# MessageId: ERROR_CANNOT_COPY
	#
	# MessageText:
	#
	# The copy functions cannot be used.
	#
	ERROR_CANNOT_COPY = 266 
	#
	# MessageId: ERROR_DIRECTORY
	#
	# MessageText:
	#
	# The directory name is invalid.
	#
	ERROR_DIRECTORY = 267 
	#
	# MessageId: ERROR_EAS_DIDNT_FIT
	#
	# MessageText:
	#
	# The extended attributes did not fit in the buffer.
	#
	ERROR_EAS_DIDNT_FIT = 275 
	#
	# MessageId: ERROR_EA_FILE_CORRUPT
	#
	# MessageText:
	#
	# The extended attribute file on the mounted file system is corrupt.
	#
	ERROR_EA_FILE_CORRUPT = 276 
	#
	# MessageId: ERROR_EA_TABLE_FULL
	#
	# MessageText:
	#
	# The extended attribute table file is full.
	#
	ERROR_EA_TABLE_FULL = 277 
	#
	# MessageId: ERROR_INVALID_EA_HANDLE
	#
	# MessageText:
	#
	# The specified extended attribute handle is invalid.
	#
	ERROR_INVALID_EA_HANDLE = 278 
	#
	# MessageId: ERROR_EAS_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The mounted file system does not support extended attributes.
	#
	ERROR_EAS_NOT_SUPPORTED = 282 
	#
	# MessageId: ERROR_NOT_OWNER
	#
	# MessageText:
	#
	# Attempt to release mutex not owned by caller.
	#
	ERROR_NOT_OWNER = 288 
	#
	# MessageId: ERROR_TOO_MANY_POSTS
	#
	# MessageText:
	#
	# Too many posts were made to a semaphore.
	#
	ERROR_TOO_MANY_POSTS = 298 
	#
	# MessageId: ERROR_PARTIAL_COPY
	#
	# MessageText:
	#
	# Only part of a ReadProcessMemory or WriteProcessMemory request was completed.
	#
	ERROR_PARTIAL_COPY = 299 
	#
	# MessageId: ERROR_OPLOCK_NOT_GRANTED
	#
	# MessageText:
	#
	# The oplock request is denied.
	#
	ERROR_OPLOCK_NOT_GRANTED = 300 
	#
	# MessageId: ERROR_INVALID_OPLOCK_PROTOCOL
	#
	# MessageText:
	#
	# An invalid oplock acknowledgment was received by the system.
	#
	ERROR_INVALID_OPLOCK_PROTOCOL = 301 
	#
	# MessageId: ERROR_DISK_TOO_FRAGMENTED
	#
	# MessageText:
	#
	# The volume is too fragmented to complete this operation.
	#
	ERROR_DISK_TOO_FRAGMENTED = 302 
	#
	# MessageId: ERROR_DELETE_PENDING
	#
	# MessageText:
	#
	# The file cannot be opened because it is in the process of being deleted.
	#
	ERROR_DELETE_PENDING = 303 
	#
	# MessageId: ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING
	#
	# MessageText:
	#
	# Short name settings may not be changed on this volume due to the global registry setting.
	#
	ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING = 304 
	#
	# MessageId: ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME
	#
	# MessageText:
	#
	# Short names are not enabled on this volume.
	#
	ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME = 305 
	#
	# MessageId: ERROR_SECURITY_STREAM_IS_INCONSISTENT
	#
	# MessageText:
	#
	# The security stream for the given volume is in an inconsistent state.
	# Please run CHKDSK on the volume.
	#
	ERROR_SECURITY_STREAM_IS_INCONSISTENT = 306 
	#
	# MessageId: ERROR_INVALID_LOCK_RANGE
	#
	# MessageText:
	#
	# A requested file lock operation cannot be processed due to an invalid byte range.
	#
	ERROR_INVALID_LOCK_RANGE = 307 
	#
	# MessageId: ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT
	#
	# MessageText:
	#
	# The subsystem needed to support the image type is not present.
	#
	ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT = 308 
	#
	# MessageId: ERROR_NOTIFICATION_GUID_ALREADY_DEFINED
	#
	# MessageText:
	#
	# The specified file already has a notification GUID associated with it.
	#
	ERROR_NOTIFICATION_GUID_ALREADY_DEFINED = 309 
	#
	# MessageId: ERROR_INVALID_EXCEPTION_HANDLER
	#
	# MessageText:
	#
	# An invalid exception handler routine has been detected.
	#
	ERROR_INVALID_EXCEPTION_HANDLER = 310 
	#
	# MessageId: ERROR_DUPLICATE_PRIVILEGES
	#
	# MessageText:
	#
	# Duplicate privileges were specified for the token.
	#
	ERROR_DUPLICATE_PRIVILEGES = 311 
	#
	# MessageId: ERROR_NO_RANGES_PROCESSED
	#
	# MessageText:
	#
	# No ranges for the specified operation were able to be processed.
	#
	ERROR_NO_RANGES_PROCESSED = 312 
	#
	# MessageId: ERROR_NOT_ALLOWED_ON_SYSTEM_FILE
	#
	# MessageText:
	#
	# Operation is not allowed on a file system internal file.
	#
	ERROR_NOT_ALLOWED_ON_SYSTEM_FILE = 313 
	#
	# MessageId: ERROR_DISK_RESOURCES_EXHAUSTED
	#
	# MessageText:
	#
	# The physical resources of this disk have been exhausted.
	#
	ERROR_DISK_RESOURCES_EXHAUSTED = 314 
	#
	# MessageId: ERROR_INVALID_TOKEN
	#
	# MessageText:
	#
	# The token representing the data is invalid.
	#
	ERROR_INVALID_TOKEN = 315 
	#
	# MessageId: ERROR_DEVICE_FEATURE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The device does not support the command feature.
	#
	ERROR_DEVICE_FEATURE_NOT_SUPPORTED = 316 
	#
	# MessageId: ERROR_MR_MID_NOT_FOUND
	#
	# MessageText:
	#
	# The system cannot find message text for message number 0x%1 in the message file for %2.
	#
	ERROR_MR_MID_NOT_FOUND = 317 
	#
	# MessageId: ERROR_SCOPE_NOT_FOUND
	#
	# MessageText:
	#
	# The scope specified was not found.
	#
	ERROR_SCOPE_NOT_FOUND = 318 
	#
	# MessageId: ERROR_UNDEFINED_SCOPE
	#
	# MessageText:
	#
	# The Central Access Policy specified is not defined on the target machine.
	#
	ERROR_UNDEFINED_SCOPE = 319 
	#
	# MessageId: ERROR_INVALID_CAP
	#
	# MessageText:
	#
	# The Central Access Policy obtained from Active Directory is invalid.
	#
	ERROR_INVALID_CAP = 320 
	#
	# MessageId: ERROR_DEVICE_UNREACHABLE
	#
	# MessageText:
	#
	# The device is unreachable.
	#
	ERROR_DEVICE_UNREACHABLE = 321 
	#
	# MessageId: ERROR_DEVICE_NO_RESOURCES
	#
	# MessageText:
	#
	# The target device has insufficient resources to complete the operation.
	#
	ERROR_DEVICE_NO_RESOURCES = 322 
	#
	# MessageId: ERROR_DATA_CHECKSUM_ERROR
	#
	# MessageText:
	#
	# A data integrity checksum error occurred. Data in the file stream is corrupt.
	#
	ERROR_DATA_CHECKSUM_ERROR = 323 
	#
	# MessageId: ERROR_INTERMIXED_KERNEL_EA_OPERATION
	#
	# MessageText:
	#
	# An attempt was made to modify both a KERNEL and normal Extended Attribute (EA) in the same operation.
	#
	ERROR_INTERMIXED_KERNEL_EA_OPERATION = 324 
	#
	# MessageId: ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED
	#
	# MessageText:
	#
	# Device does not support file-level TRIM.
	#
	ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED = 326 
	#
	# MessageId: ERROR_OFFSET_ALIGNMENT_VIOLATION
	#
	# MessageText:
	#
	# The command specified a data offset that does not align to the device's granularity/alignment.
	#
	ERROR_OFFSET_ALIGNMENT_VIOLATION = 327 
	#
	# MessageId: ERROR_INVALID_FIELD_IN_PARAMETER_LIST
	#
	# MessageText:
	#
	# The command specified an invalid field in its parameter list.
	#
	ERROR_INVALID_FIELD_IN_PARAMETER_LIST = 328 
	#
	# MessageId: ERROR_OPERATION_IN_PROGRESS
	#
	# MessageText:
	#
	# An operation is currently in progress with the device.
	#
	ERROR_OPERATION_IN_PROGRESS = 329 
	#
	# MessageId: ERROR_BAD_DEVICE_PATH
	#
	# MessageText:
	#
	# An attempt was made to send down the command via an invalid path to the target device.
	#
	ERROR_BAD_DEVICE_PATH = 330 
	#
	# MessageId: ERROR_TOO_MANY_DESCRIPTORS
	#
	# MessageText:
	#
	# The command specified a number of descriptors that exceeded the maximum supported by the device.
	#
	ERROR_TOO_MANY_DESCRIPTORS = 331 
	#
	# MessageId: ERROR_SCRUB_DATA_DISABLED
	#
	# MessageText:
	#
	# Scrub is disabled on the specified file.
	#
	ERROR_SCRUB_DATA_DISABLED = 332 
	#
	# MessageId: ERROR_NOT_REDUNDANT_STORAGE
	#
	# MessageText:
	#
	# The storage device does not provide redundancy.
	#
	ERROR_NOT_REDUNDANT_STORAGE = 333 
	#
	# MessageId: ERROR_RESIDENT_FILE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# An operation is not supported on a resident file.
	#
	ERROR_RESIDENT_FILE_NOT_SUPPORTED = 334 
	#
	# MessageId: ERROR_COMPRESSED_FILE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# An operation is not supported on a compressed file.
	#
	ERROR_COMPRESSED_FILE_NOT_SUPPORTED = 335 
	#
	# MessageId: ERROR_DIRECTORY_NOT_SUPPORTED
	#
	# MessageText:
	#
	# An operation is not supported on a directory.
	#
	ERROR_DIRECTORY_NOT_SUPPORTED = 336 
	#
	# MessageId: ERROR_NOT_READ_FROM_COPY
	#
	# MessageText:
	#
	# The specified copy of the requested data could not be read.
	#
	ERROR_NOT_READ_FROM_COPY = 337 
	#
	# MessageId: ERROR_FT_WRITE_FAILURE
	#
	# MessageText:
	#
	# The specified data could not be written to any of the copies.
	#
	ERROR_FT_WRITE_FAILURE = 338 
	#
	# MessageId: ERROR_FT_DI_SCAN_REQUIRED
	#
	# MessageText:
	#
	# One or more copies of data on this device may be out of sync. No writes may be performed until a data integrity scan is completed.
	#
	ERROR_FT_DI_SCAN_REQUIRED = 339 
	#
	# MessageId: ERROR_INVALID_KERNEL_INFO_VERSION
	#
	# MessageText:
	#
	# The supplied kernel information version is invalid.
	#
	ERROR_INVALID_KERNEL_INFO_VERSION = 340 
	#
	# MessageId: ERROR_INVALID_PEP_INFO_VERSION
	#
	# MessageText:
	#
	# The supplied PEP information version is invalid.
	#
	ERROR_INVALID_PEP_INFO_VERSION = 341 
	#
	# MessageId: ERROR_OBJECT_NOT_EXTERNALLY_BACKED
	#
	# MessageText:
	#
	# This object is not externally backed by any provider.
	#
	ERROR_OBJECT_NOT_EXTERNALLY_BACKED = 342 
	#
	# MessageId: ERROR_EXTERNAL_BACKING_PROVIDER_UNKNOWN
	#
	# MessageText:
	#
	# The external backing provider is not recognized.
	#
	ERROR_EXTERNAL_BACKING_PROVIDER_UNKNOWN = 343 
	#
	# MessageId: ERROR_COMPRESSION_NOT_BENEFICIAL
	#
	# MessageText:
	#
	# Compressing this object would not save space.
	#
	ERROR_COMPRESSION_NOT_BENEFICIAL = 344 
	#
	# MessageId: ERROR_STORAGE_TOPOLOGY_ID_MISMATCH
	#
	# MessageText:
	#
	# The request failed due to a storage topology ID mismatch.
	#
	ERROR_STORAGE_TOPOLOGY_ID_MISMATCH = 345 
	#
	# MessageId: ERROR_BLOCKED_BY_PARENTAL_CONTROLS
	#
	# MessageText:
	#
	# The operation was blocked by parental controls.
	#
	ERROR_BLOCKED_BY_PARENTAL_CONTROLS = 346 
	#
	# MessageId: ERROR_BLOCK_TOO_MANY_REFERENCES
	#
	# MessageText:
	#
	# A file system block being referenced has already reached the maximum reference count and can't be referenced any further.
	#
	ERROR_BLOCK_TOO_MANY_REFERENCES = 347 
	#
	# MessageId: ERROR_MARKED_TO_DISALLOW_WRITES
	#
	# MessageText:
	#
	# The requested operation failed because the file stream is marked to disallow writes.
	#
	ERROR_MARKED_TO_DISALLOW_WRITES = 348 
	#
	# MessageId: ERROR_ENCLAVE_FAILURE
	#
	# MessageText:
	#
	# The requested operation failed with an architecture-specific failure code.
	#
	ERROR_ENCLAVE_FAILURE = 349 
	#
	# MessageId: ERROR_FAIL_NOACTION_REBOOT
	#
	# MessageText:
	#
	# No action was taken as a system reboot is required.
	#
	ERROR_FAIL_NOACTION_REBOOT = 350 
	#
	# MessageId: ERROR_FAIL_SHUTDOWN
	#
	# MessageText:
	#
	# The shutdown operation failed.
	#
	ERROR_FAIL_SHUTDOWN = 351 
	#
	# MessageId: ERROR_FAIL_RESTART
	#
	# MessageText:
	#
	# The restart operation failed.
	#
	ERROR_FAIL_RESTART = 352 
	#
	# MessageId: ERROR_MAX_SESSIONS_REACHED
	#
	# MessageText:
	#
	# The maximum number of sessions has been reached.
	#
	ERROR_MAX_SESSIONS_REACHED = 353 
	#
	# MessageId: ERROR_NETWORK_ACCESS_DENIED_EDP
	#
	# MessageText:
	#
	# Windows Information Protection policy does not allow access to this network resource.
	#
	ERROR_NETWORK_ACCESS_DENIED_EDP = 354 
	#
	# MessageId: ERROR_DEVICE_HINT_NAME_BUFFER_TOO_SMALL
	#
	# MessageText:
	#
	# The device hint name buffer is too small to receive the remaining name.
	#
	ERROR_DEVICE_HINT_NAME_BUFFER_TOO_SMALL = 355 
	#
	# MessageId: ERROR_EDP_POLICY_DENIES_OPERATION
	#
	# MessageText:
	#
	# The requested operation was blocked by Windows Information Protection policy. For more information, contact your system administrator.
	#
	ERROR_EDP_POLICY_DENIES_OPERATION = 356 
	#
	# MessageId: ERROR_EDP_DPL_POLICY_CANT_BE_SATISFIED
	#
	# MessageText:
	#
	# The requested operation cannot be performed because hardware or software configuration of the device does not comply with Windows Information Protection under Lock policy. Please, verify that user PIN has been created. For more information, contact your system administrator.
	#
	ERROR_EDP_DPL_POLICY_CANT_BE_SATISFIED = 357 
	#
	# MessageId: ERROR_CLOUD_FILE_SYNC_ROOT_METADATA_CORRUPT
	#
	# MessageText:
	#
	# The cloud sync root metadata is corrupted.
	#
	ERROR_CLOUD_FILE_SYNC_ROOT_METADATA_CORRUPT = 358 
	#
	# MessageId: ERROR_DEVICE_IN_MAINTENANCE
	#
	# MessageText:
	#
	# The device is in maintenance mode.
	#
	ERROR_DEVICE_IN_MAINTENANCE = 359 
	#
	# MessageId: ERROR_NOT_SUPPORTED_ON_DAX
	#
	# MessageText:
	#
	# This operation is not supported on a DAX volume.
	#
	ERROR_NOT_SUPPORTED_ON_DAX = 360 
	#
	# MessageId: ERROR_DAX_MAPPING_EXISTS
	#
	# MessageText:
	#
	# The volume has active DAX mappings.
	#
	ERROR_DAX_MAPPING_EXISTS = 361 
	#
	# MessageId: ERROR_CLOUD_FILE_PROVIDER_NOT_RUNNING
	#
	# MessageText:
	#
	# The cloud file provider is not running.
	#
	ERROR_CLOUD_FILE_PROVIDER_NOT_RUNNING = 362 
	#
	# MessageId: ERROR_CLOUD_FILE_METADATA_CORRUPT
	#
	# MessageText:
	#
	# The cloud file metadata is corrupt and unreadable.
	#
	ERROR_CLOUD_FILE_METADATA_CORRUPT = 363 
	#
	# MessageId: ERROR_CLOUD_FILE_METADATA_TOO_LARGE
	#
	# MessageText:
	#
	# The cloud file metadata is too large.
	#
	ERROR_CLOUD_FILE_METADATA_TOO_LARGE = 364 
	#
	# MessageId: ERROR_CLOUD_FILE_PROPERTY_BLOB_TOO_LARGE
	#
	# MessageText:
	#
	# The cloud file property is too large.
	#
	ERROR_CLOUD_FILE_PROPERTY_BLOB_TOO_LARGE = 365 
	#
	# MessageId: ERROR_CLOUD_FILE_PROPERTY_BLOB_CHECKSUM_MISMATCH
	#
	# MessageText:
	#
	# The cloud file property is possibly corrupt. The on-disk checksum does not match the computed checksum.
	#
	ERROR_CLOUD_FILE_PROPERTY_BLOB_CHECKSUM_MISMATCH = 366 
	#
	# MessageId: ERROR_CHILD_PROCESS_BLOCKED
	#
	# MessageText:
	#
	# The process creation has been blocked.
	#
	ERROR_CHILD_PROCESS_BLOCKED = 367 
	#
	# MessageId: ERROR_STORAGE_LOST_DATA_PERSISTENCE
	#
	# MessageText:
	#
	# The storage device has lost data or persistence.
	#
	ERROR_STORAGE_LOST_DATA_PERSISTENCE = 368 
	#
	# MessageId: ERROR_FILE_SYSTEM_VIRTUALIZATION_UNAVAILABLE
	#
	# MessageText:
	#
	# The provider that supports file system virtualization is temporarily unavailable.
	#
	ERROR_FILE_SYSTEM_VIRTUALIZATION_UNAVAILABLE = 369 
	#
	# MessageId: ERROR_FILE_SYSTEM_VIRTUALIZATION_METADATA_CORRUPT
	#
	# MessageText:
	#
	# The metadata for file system virtualization is corrupt and unreadable.
	#
	ERROR_FILE_SYSTEM_VIRTUALIZATION_METADATA_CORRUPT = 370 
	#
	# MessageId: ERROR_FILE_SYSTEM_VIRTUALIZATION_BUSY
	#
	# MessageText:
	#
	# The provider that supports file system virtualization is too busy to complete this operation.
	#
	ERROR_FILE_SYSTEM_VIRTUALIZATION_BUSY = 371 
	#
	# MessageId: ERROR_FILE_SYSTEM_VIRTUALIZATION_PROVIDER_UNKNOWN
	#
	# MessageText:
	#
	# The provider that supports file system virtualization is unknown.
	#
	ERROR_FILE_SYSTEM_VIRTUALIZATION_PROVIDER_UNKNOWN = 372 
	#
	# MessageId: ERROR_GDI_HANDLE_LEAK
	#
	# MessageText:
	#
	# GDI handles were potentially leaked by the application.
	#
	ERROR_GDI_HANDLE_LEAK = 373 
	#
	# MessageId: ERROR_CLOUD_FILE_TOO_MANY_PROPERTY_BLOBS
	#
	# MessageText:
	#
	# The maximum number of cloud file properties has been reached.
	#
	ERROR_CLOUD_FILE_TOO_MANY_PROPERTY_BLOBS = 374 
	#
	# MessageId: ERROR_CLOUD_FILE_PROPERTY_VERSION_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The version of the cloud file property store is not supported.
	#
	ERROR_CLOUD_FILE_PROPERTY_VERSION_NOT_SUPPORTED = 375 
	#
	# MessageId: ERROR_NOT_A_CLOUD_FILE
	#
	# MessageText:
	#
	# The file is not a cloud file.
	#
	ERROR_NOT_A_CLOUD_FILE = 376 
	#
	# MessageId: ERROR_CLOUD_FILE_NOT_IN_SYNC
	#
	# MessageText:
	#
	# The file is not in sync with the cloud.
	#
	ERROR_CLOUD_FILE_NOT_IN_SYNC = 377 
	#
	# MessageId: ERROR_CLOUD_FILE_ALREADY_CONNECTED
	#
	# MessageText:
	#
	# The cloud sync root is already connected with another cloud sync provider.
	#
	ERROR_CLOUD_FILE_ALREADY_CONNECTED = 378 
	#
	# MessageId: ERROR_CLOUD_FILE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The operation is not supported by the cloud sync provider.
	#
	ERROR_CLOUD_FILE_NOT_SUPPORTED = 379 
	#
	# MessageId: ERROR_CLOUD_FILE_INVALID_REQUEST
	#
	# MessageText:
	#
	# The cloud operation is invalid.
	#
	ERROR_CLOUD_FILE_INVALID_REQUEST = 380 
	#
	# MessageId: ERROR_CLOUD_FILE_READ_ONLY_VOLUME
	#
	# MessageText:
	#
	# The cloud operation is not supported on a read-only volume.
	#
	ERROR_CLOUD_FILE_READ_ONLY_VOLUME = 381 
	#
	# MessageId: ERROR_CLOUD_FILE_CONNECTED_PROVIDER_ONLY
	#
	# MessageText:
	#
	# The operation is reserved for a connected cloud sync provider.
	#
	ERROR_CLOUD_FILE_CONNECTED_PROVIDER_ONLY = 382 
	#
	# MessageId: ERROR_CLOUD_FILE_VALIDATION_FAILED
	#
	# MessageText:
	#
	# The cloud sync provider failed to validate the downloaded data.
	#
	ERROR_CLOUD_FILE_VALIDATION_FAILED = 383 
	#
	# MessageId: ERROR_SMB1_NOT_AVAILABLE
	#
	# MessageText:
	#
	# You can't connect to the file share because it's not secure. This share requires the obsolete SMB1 protocol, which is unsafe and could expose your system to attack.
	# Your system requires SMB2 or higher. For more info on resolving this issue, see: https:#go.microsoft.com/fwlink/?linkid=852747
	#
	ERROR_SMB1_NOT_AVAILABLE = 384 
	#
	# MessageId: ERROR_FILE_SYSTEM_VIRTUALIZATION_INVALID_OPERATION
	#
	# MessageText:
	#
	# The virtualization operation is not allowed on the file in its current state.
	#
	ERROR_FILE_SYSTEM_VIRTUALIZATION_INVALID_OPERATION = 385 
	#
	# MessageId: ERROR_CLOUD_FILE_AUTHENTICATION_FAILED
	#
	# MessageText:
	#
	# The cloud sync provider failed user authentication.
	#
	ERROR_CLOUD_FILE_AUTHENTICATION_FAILED = 386 
	#
	# MessageId: ERROR_CLOUD_FILE_INSUFFICIENT_RESOURCES
	#
	# MessageText:
	#
	# The cloud sync provider failed to perform the operation due to low system resources.
	#
	ERROR_CLOUD_FILE_INSUFFICIENT_RESOURCES = 387 
	#
	# MessageId: ERROR_CLOUD_FILE_NETWORK_UNAVAILABLE
	#
	# MessageText:
	#
	# The cloud sync provider failed to perform the operation due to network being unavailable.
	#
	ERROR_CLOUD_FILE_NETWORK_UNAVAILABLE = 388 
	#
	# MessageId: ERROR_CLOUD_FILE_UNSUCCESSFUL
	#
	# MessageText:
	#
	# The cloud operation was unsuccessful.
	#
	ERROR_CLOUD_FILE_UNSUCCESSFUL = 389 
	#
	# MessageId: ERROR_CLOUD_FILE_NOT_UNDER_SYNC_ROOT
	#
	# MessageText:
	#
	# The operation is only supported on files under a cloud sync root.
	#
	ERROR_CLOUD_FILE_NOT_UNDER_SYNC_ROOT = 390 
	#
	# MessageId: ERROR_CLOUD_FILE_IN_USE
	#
	# MessageText:
	#
	# The operation cannot be performed on cloud files in use.
	#
	ERROR_CLOUD_FILE_IN_USE = 391 
	#
	# MessageId: ERROR_CLOUD_FILE_PINNED
	#
	# MessageText:
	#
	# The operation cannot be performed on pinned cloud files.
	#
	ERROR_CLOUD_FILE_PINNED = 392 
	#
	# MessageId: ERROR_CLOUD_FILE_REQUEST_ABORTED
	#
	# MessageText:
	#
	# The cloud operation was aborted.
	#
	ERROR_CLOUD_FILE_REQUEST_ABORTED = 393 
	#
	# MessageId: ERROR_CLOUD_FILE_PROPERTY_CORRUPT
	#
	# MessageText:
	#
	# The cloud file's property store is corrupt.
	#
	ERROR_CLOUD_FILE_PROPERTY_CORRUPT = 394 
	#
	# MessageId: ERROR_CLOUD_FILE_ACCESS_DENIED
	#
	# MessageText:
	#
	# Access to the cloud file is denied.
	#
	ERROR_CLOUD_FILE_ACCESS_DENIED = 395 
	#
	# MessageId: ERROR_CLOUD_FILE_INCOMPATIBLE_HARDLINKS
	#
	# MessageText:
	#
	# The cloud operation cannot be performed on a file with incompatible hardlinks.
	#
	ERROR_CLOUD_FILE_INCOMPATIBLE_HARDLINKS = 396 
	#
	# MessageId: ERROR_CLOUD_FILE_PROPERTY_LOCK_CONFLICT
	#
	# MessageText:
	#
	# The operation failed due to a conflicting cloud file property lock.
	#
	ERROR_CLOUD_FILE_PROPERTY_LOCK_CONFLICT = 397 
	#
	# MessageId: ERROR_CLOUD_FILE_REQUEST_CANCELED
	#
	# MessageText:
	#
	# The cloud operation was canceled by user.
	#
	ERROR_CLOUD_FILE_REQUEST_CANCELED = 398 
	#
	# MessageId: ERROR_EXTERNAL_SYSKEY_NOT_SUPPORTED
	#
	# MessageText:
	#
	# An externally encrypted syskey has been configured, but the system no longer supports this feature.  Please see https:#go.microsoft.com/fwlink/?linkid=851152 for more information.
	#
	ERROR_EXTERNAL_SYSKEY_NOT_SUPPORTED = 399 
	#
	# MessageId: ERROR_THREAD_MODE_ALREADY_BACKGROUND
	#
	# MessageText:
	#
	# The thread is already in background processing mode.
	#
	ERROR_THREAD_MODE_ALREADY_BACKGROUND = 400 
	#
	# MessageId: ERROR_THREAD_MODE_NOT_BACKGROUND
	#
	# MessageText:
	#
	# The thread is not in background processing mode.
	#
	ERROR_THREAD_MODE_NOT_BACKGROUND = 401 
	#
	# MessageId: ERROR_PROCESS_MODE_ALREADY_BACKGROUND
	#
	# MessageText:
	#
	# The process is already in background processing mode.
	#
	ERROR_PROCESS_MODE_ALREADY_BACKGROUND = 402 
	#
	# MessageId: ERROR_PROCESS_MODE_NOT_BACKGROUND
	#
	# MessageText:
	#
	# The process is not in background processing mode.
	#
	ERROR_PROCESS_MODE_NOT_BACKGROUND = 403 
	#
	# MessageId: ERROR_CLOUD_FILE_PROVIDER_TERMINATED
	#
	# MessageText:
	#
	# The cloud file provider exited unexpectedly.
	#
	ERROR_CLOUD_FILE_PROVIDER_TERMINATED = 404 
	#
	# MessageId: ERROR_NOT_A_CLOUD_SYNC_ROOT
	#
	# MessageText:
	#
	# The file is not a cloud sync root.
	#
	ERROR_NOT_A_CLOUD_SYNC_ROOT = 405 
	#
	# MessageId: ERROR_FILE_PROTECTED_UNDER_DPL
	#
	# MessageText:
	#
	# The read or write operation to an encrypted file could not be completed because the file can only be accessed when the device is unlocked.
	#
	ERROR_FILE_PROTECTED_UNDER_DPL = 406 
	#
	# MessageId: ERROR_VOLUME_NOT_CLUSTER_ALIGNED
	#
	# MessageText:
	#
	# The volume is not cluster aligned on the disk.
	#
	ERROR_VOLUME_NOT_CLUSTER_ALIGNED = 407 
	#
	# MessageId: ERROR_NO_PHYSICALLY_ALIGNED_FREE_SPACE_FOUND
	#
	# MessageText:
	#
	# No physically aligned free space was found on the volume.
	#
	ERROR_NO_PHYSICALLY_ALIGNED_FREE_SPACE_FOUND = 408 
	#
	# MessageId: ERROR_APPX_FILE_NOT_ENCRYPTED
	#
	# MessageText:
	#
	# The APPX file can not be accessed because it is not encrypted as expected.
	#
	ERROR_APPX_FILE_NOT_ENCRYPTED = 409 
	#
	# MessageId: ERROR_RWRAW_ENCRYPTED_FILE_NOT_ENCRYPTED
	#
	# MessageText:
	#
	# A read or write of raw encrypted data cannot be performed because the file is not encrypted.
	#
	ERROR_RWRAW_ENCRYPTED_FILE_NOT_ENCRYPTED = 410 
	#
	# MessageId: ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_FILEOFFSET
	#
	# MessageText:
	#
	# An invalid file offset in the encrypted data info block was passed for read or write operation of file's raw encrypted data.
	#
	ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_FILEOFFSET = 411 
	#
	# MessageId: ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_FILERANGE
	#
	# MessageText:
	#
	# An invalid offset and length combination in the encrypted data info block was passed for read or write operation of file's raw encrypted data.
	#
	ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_FILERANGE = 412 
	#
	# MessageId: ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_PARAMETER
	#
	# MessageText:
	#
	# An invalid parameter in the encrypted data info block was passed for read or write operation of file's raw encrypted data.
	#
	ERROR_RWRAW_ENCRYPTED_INVALID_EDATAINFO_PARAMETER = 413 
	#
	# MessageId: ERROR_LINUX_SUBSYSTEM_NOT_PRESENT
	#
	# MessageText:
	#
	# The Windows Subsystem for Linux has not been enabled.
	#
	ERROR_LINUX_SUBSYSTEM_NOT_PRESENT = 414 
	#
	# MessageId: ERROR_FT_READ_FAILURE
	#
	# MessageText:
	#
	# The specified data could not be read from any of the copies.
	#
	ERROR_FT_READ_FAILURE = 415 
	#
	# MessageId: ERROR_STORAGE_RESERVE_ID_INVALID
	#
	# MessageText:
	#
	# The specified storage reserve ID is invalid.
	#
	ERROR_STORAGE_RESERVE_ID_INVALID = 416 
	#
	# MessageId: ERROR_STORAGE_RESERVE_DOES_NOT_EXIST
	#
	# MessageText:
	#
	# The specified storage reserve does not exist.
	#
	ERROR_STORAGE_RESERVE_DOES_NOT_EXIST = 417 
	#
	# MessageId: ERROR_STORAGE_RESERVE_ALREADY_EXISTS
	#
	# MessageText:
	#
	# The specified storage reserve already exists.
	#
	ERROR_STORAGE_RESERVE_ALREADY_EXISTS = 418 
	#
	# MessageId: ERROR_STORAGE_RESERVE_NOT_EMPTY
	#
	# MessageText:
	#
	# The specified storage reserve is not empty.
	#
	ERROR_STORAGE_RESERVE_NOT_EMPTY = 419 
	#
	# MessageId: ERROR_NOT_A_DAX_VOLUME
	#
	# MessageText:
	#
	# This operation requires a DAX volume.
	#
	ERROR_NOT_A_DAX_VOLUME = 420 
	#
	# MessageId: ERROR_NOT_DAX_MAPPABLE
	#
	# MessageText:
	#
	# This stream is not DAX mappable.
	#
	ERROR_NOT_DAX_MAPPABLE = 421 
	#
	# MessageId: ERROR_TIME_SENSITIVE_THREAD
	#
	# MessageText:
	#
	# Operation cannot be performed on a time critical thread.
	#
	ERROR_TIME_SENSITIVE_THREAD = 422 
	#
	# MessageId: ERROR_DPL_NOT_SUPPORTED_FOR_USER
	#
	# MessageText:
	#
	# User data protection is not supported for the current or provided user.
	#
	ERROR_DPL_NOT_SUPPORTED_FOR_USER = 423 
	#
	# MessageId: ERROR_CASE_DIFFERING_NAMES_IN_DIR
	#
	# MessageText:
	#
	# This directory contains entries whose names differ only in case.
	#
	ERROR_CASE_DIFFERING_NAMES_IN_DIR = 424 
	#
	# MessageId: ERROR_FILE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The file cannot be safely opened because it is not supported by this version of Windows.
	#
	ERROR_FILE_NOT_SUPPORTED = 425 
	#
	# MessageId: ERROR_CLOUD_FILE_REQUEST_TIMEOUT
	#
	# MessageText:
	#
	# The cloud operation was not completed before the time-out period expired.
	#
	ERROR_CLOUD_FILE_REQUEST_TIMEOUT = 426 
	#
	# MessageId: ERROR_NO_TASK_QUEUE
	#
	# MessageText:
	#
	# A task queue is required for this operation but none is available.
	#
	ERROR_NO_TASK_QUEUE = 427 
	#
	# MessageId: ERROR_SRC_SRV_DLL_LOAD_FAILED
	#
	# MessageText:
	#
	# Failed loading a valid version of srcsrv.dll.
	#
	ERROR_SRC_SRV_DLL_LOAD_FAILED = 428 
	#
	# MessageId: ERROR_NOT_SUPPORTED_WITH_BTT
	#
	# MessageText:
	#
	# This operation is not supported with BTT enabled.
	#
	ERROR_NOT_SUPPORTED_WITH_BTT = 429 
	#
	# MessageId: ERROR_ENCRYPTION_DISABLED
	#
	# MessageText:
	#
	# This operation cannot be performed because encryption is currently disabled.
	#
	ERROR_ENCRYPTION_DISABLED = 430 
	#
	# MessageId: ERROR_ENCRYPTING_METADATA_DISALLOWED
	#
	# MessageText:
	#
	# This encryption operation cannot be performed on filesystem metadata.
	#
	ERROR_ENCRYPTING_METADATA_DISALLOWED = 431 
	#
	# MessageId: ERROR_CANT_CLEAR_ENCRYPTION_FLAG
	#
	# MessageText:
	#
	# Encryption cannot be cleared on this file/directory because it still has an encrypted attribute.
	#
	ERROR_CANT_CLEAR_ENCRYPTION_FLAG = 432 
	#
	# MessageId: ERROR_NO_SUCH_DEVICE
	#
	# MessageText:
	#
	# A device which does not exist was specified.
	#
	ERROR_NO_SUCH_DEVICE = 433 
	#
	# MessageId: ERROR_CLOUD_FILE_DEHYDRATION_DISALLOWED
	#
	# MessageText:
	#
	# Dehydration of the cloud file is disallowed by the cloud sync provider.
	#
	ERROR_CLOUD_FILE_DEHYDRATION_DISALLOWED = 434 
	#
	# MessageId: ERROR_FILE_SNAP_IN_PROGRESS
	#
	# MessageText:
	#
	# A file snapshot operation was attempted when one is already in progress.
	#
	ERROR_FILE_SNAP_IN_PROGRESS = 435 
	#
	# MessageId: ERROR_FILE_SNAP_USER_SECTION_NOT_SUPPORTED
	#
	# MessageText:
	#
	# A snapshot of the file cannot be taken because a user-mapped section is present.
	#
	ERROR_FILE_SNAP_USER_SECTION_NOT_SUPPORTED = 436 
	#
	# MessageId: ERROR_FILE_SNAP_MODIFY_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The file snapshot operation was terminated because one of the files was modified in a way incompatible with a snapshot operation.  Please try again.
	#
	ERROR_FILE_SNAP_MODIFY_NOT_SUPPORTED = 437 
	#
	# MessageId: ERROR_FILE_SNAP_IO_NOT_COORDINATED
	#
	# MessageText:
	#
	# An I/O request could not be coordinated with a file snapshot operation.
	#
	ERROR_FILE_SNAP_IO_NOT_COORDINATED = 438 
	#
	# MessageId: ERROR_FILE_SNAP_UNEXPECTED_ERROR
	#
	# MessageText:
	#
	# An unexpected error occurred while processing a file snapshot operation.
	#
	ERROR_FILE_SNAP_UNEXPECTED_ERROR = 439 
	#
	# MessageId: ERROR_FILE_SNAP_INVALID_PARAMETER
	#
	# MessageText:
	#
	# A file snapshot operation received an invalid parameter.
	#
	ERROR_FILE_SNAP_INVALID_PARAMETER = 440 
	#
	# MessageId: ERROR_UNSATISFIED_DEPENDENCIES
	#
	# MessageText:
	#
	# The operation could not be completed due to one or more unsatisfied dependencies.
	#
	ERROR_UNSATISFIED_DEPENDENCIES = 441 
	#
	# MessageId: ERROR_CASE_SENSITIVE_PATH
	#
	# MessageText:
	#
	# The file cannot be opened because the path has a case-sensitive directory.
	#
	ERROR_CASE_SENSITIVE_PATH = 442 
	#
	# MessageId: ERROR_UNEXPECTED_NTCACHEMANAGER_ERROR
	#
	# MessageText:
	#
	# The filesystem couldn't handle one of the CacheManager's callback error codes.
	#
	ERROR_UNEXPECTED_NTCACHEMANAGER_ERROR = 443 
	#
	# MessageId: ERROR_LINUX_SUBSYSTEM_UPDATE_REQUIRED
	#
	# MessageText:
	#
	# WSL 2 requires an update to its kernel component. For information please visit https:#aka.ms/wsl2kernel
	#
	ERROR_LINUX_SUBSYSTEM_UPDATE_REQUIRED = 444 
	#
	# MessageId: ERROR_DLP_POLICY_WARNS_AGAINST_OPERATION
	#
	# MessageText:
	#
	# This action is blocked, but you can choose to allow it. Please refer to the data loss prevention notification for further information.
	#
	ERROR_DLP_POLICY_WARNS_AGAINST_OPERATION = 445 
	#
	# MessageId: ERROR_DLP_POLICY_DENIES_OPERATION
	#
	# MessageText:
	#
	# This action is blocked. Please refer to the data loss prevention notification for further information.
	#
	ERROR_DLP_POLICY_DENIES_OPERATION = 446 
	# Data Loss Prevention error code to suppress showing UX/error message. Still adding error text for consistency.
	#
	# MessageId: ERROR_DLP_POLICY_SILENTLY_FAIL
	#
	# MessageText:
	#
	# This action is blocked. Please refer to the data loss prevention notification for further information.
	#
	ERROR_DLP_POLICY_SILENTLY_FAIL = 449 
	#
	# **** Available SYSTEM error codes ****
	#
	#########################/
	#                                               #
	#    Capability Authorization Error codes       #
	#                                               #
	#                 0450 to 0460                  #
	#########################/
	#
	# MessageId: ERROR_CAPAUTHZ_NOT_DEVUNLOCKED
	#
	# MessageText:
	#
	# Neither developer unlocked mode nor side loading mode is enabled on the device.
	#
	ERROR_CAPAUTHZ_NOT_DEVUNLOCKED = 450 
	#
	# MessageId: ERROR_CAPAUTHZ_CHANGE_TYPE
	#
	# MessageText:
	#
	# Can not change application type during upgrade or re-provision.
	#
	ERROR_CAPAUTHZ_CHANGE_TYPE = 451 
	#
	# MessageId: ERROR_CAPAUTHZ_NOT_PROVISIONED
	#
	# MessageText:
	#
	# The application has not been provisioned.
	#
	ERROR_CAPAUTHZ_NOT_PROVISIONED = 452 
	#
	# MessageId: ERROR_CAPAUTHZ_NOT_AUTHORIZED
	#
	# MessageText:
	#
	# The requested capability can not be authorized for this application.
	#
	ERROR_CAPAUTHZ_NOT_AUTHORIZED = 453 
	#
	# MessageId: ERROR_CAPAUTHZ_NO_POLICY
	#
	# MessageText:
	#
	# There is no capability authorization policy on the device.
	#
	ERROR_CAPAUTHZ_NO_POLICY = 454 
	#
	# MessageId: ERROR_CAPAUTHZ_DB_CORRUPTED
	#
	# MessageText:
	#
	# The capability authorization database has been corrupted.
	#
	ERROR_CAPAUTHZ_DB_CORRUPTED = 455 
	#
	# MessageId: ERROR_CAPAUTHZ_SCCD_INVALID_CATALOG
	#
	# MessageText:
	#
	# The custom capability's SCCD has an invalid catalog.
	#
	ERROR_CAPAUTHZ_SCCD_INVALID_CATALOG = 456 
	#
	# MessageId: ERROR_CAPAUTHZ_SCCD_NO_AUTH_ENTITY
	#
	# MessageText:
	#
	# None of the authorized entity elements in the SCCD matched the app being installed; either the PFNs don't match, or the element's signature hash doesn't validate.
	#
	ERROR_CAPAUTHZ_SCCD_NO_AUTH_ENTITY = 457 
	#
	# MessageId: ERROR_CAPAUTHZ_SCCD_PARSE_ERROR
	#
	# MessageText:
	#
	# The custom capability's SCCD failed to parse.
	#
	ERROR_CAPAUTHZ_SCCD_PARSE_ERROR = 458 
	#
	# MessageId: ERROR_CAPAUTHZ_SCCD_DEV_MODE_REQUIRED
	#
	# MessageText:
	#
	# The custom capability's SCCD requires developer mode.
	#
	ERROR_CAPAUTHZ_SCCD_DEV_MODE_REQUIRED = 459 
	#
	# MessageId: ERROR_CAPAUTHZ_SCCD_NO_CAPABILITY_MATCH
	#
	# MessageText:
	#
	# There not all declared custom capabilities are found in the SCCD.
	#
	ERROR_CAPAUTHZ_SCCD_NO_CAPABILITY_MATCH = 460 
	#
	# MessageId: ERROR_CIMFS_IMAGE_CORRUPT
	#
	# MessageText:
	#
	# The CimFS image is corrupt.
	#
	ERROR_CIMFS_IMAGE_CORRUPT = 470 
	#
	# **** Available SYSTEM error codes ****
	#
	#
	# MessageId: ERROR_PNP_QUERY_REMOVE_DEVICE_TIMEOUT
	#
	# MessageText:
	#
	# The operation timed out waiting for this device to complete a PnP query-remove request due to a potential hang in its device stack. The system may need to be rebooted to complete the request.
	#
	ERROR_PNP_QUERY_REMOVE_DEVICE_TIMEOUT = 480 
	#
	# MessageId: ERROR_PNP_QUERY_REMOVE_RELATED_DEVICE_TIMEOUT
	#
	# MessageText:
	#
	# The operation timed out waiting for this device to complete a PnP query-remove request due to a potential hang in the device stack of a related device. The system may need to be rebooted to complete the operation.
	#
	ERROR_PNP_QUERY_REMOVE_RELATED_DEVICE_TIMEOUT = 481 
	#
	# MessageId: ERROR_PNP_QUERY_REMOVE_UNRELATED_DEVICE_TIMEOUT
	#
	# MessageText:
	#
	# The operation timed out waiting for this device to complete a PnP query-remove request due to a potential hang in the device stack of an unrelated device. The system may need to be rebooted to complete the operation.
	#
	ERROR_PNP_QUERY_REMOVE_UNRELATED_DEVICE_TIMEOUT = 482 
	#
	# MessageId: ERROR_DEVICE_HARDWARE_ERROR
	#
	# MessageText:
	#
	# The request failed due to a fatal device hardware error.
	#
	ERROR_DEVICE_HARDWARE_ERROR = 483 
	#
	# MessageId: ERROR_INVALID_ADDRESS
	#
	# MessageText:
	#
	# Attempt to access invalid address.
	#
	ERROR_INVALID_ADDRESS = 487 
	#
	# MessageId: ERROR_HAS_SYSTEM_CRITICAL_FILES
	#
	# MessageText:
	#
	# The volume contains paging, crash dump or other system critical files.
	#
	ERROR_HAS_SYSTEM_CRITICAL_FILES = 488 
	#
	# MessageId: ERROR_VRF_CFG_AND_IO_ENABLED
	#
	# MessageText:
	#
	# Driver Verifier Volatile settings cannot be set when CFG and IO are enabled.
	#
	ERROR_VRF_CFG_AND_IO_ENABLED = 1183 
	#
	# MessageId: ERROR_PARTITION_TERMINATING
	#
	# MessageText:
	#
	# An attempt was made to access a partition that has begun termination.
	#
	ERROR_PARTITION_TERMINATING = 1184 
	#
	# **** Available SYSTEM error codes ****
	#
	#
	# MessageId: ERROR_USER_PROFILE_LOAD
	#
	# MessageText:
	#
	# User profile cannot be loaded.
	#
	ERROR_USER_PROFILE_LOAD = 500 
	#
	# **** Available SYSTEM error codes ****
	#
	#
	# MessageId: ERROR_ARITHMETIC_OVERFLOW
	#
	# MessageText:
	#
	# Arithmetic result exceeded 32 bits.
	#
	ERROR_ARITHMETIC_OVERFLOW = 534 
	#
	# MessageId: ERROR_PIPE_CONNECTED
	#
	# MessageText:
	#
	# There is a process on other end of the pipe.
	#
	ERROR_PIPE_CONNECTED = 535 
	#
	# MessageId: ERROR_PIPE_LISTENING
	#
	# MessageText:
	#
	# Waiting for a process to open the other end of the pipe.
	#
	ERROR_PIPE_LISTENING = 536 
	#
	# MessageId: ERROR_VERIFIER_STOP
	#
	# MessageText:
	#
	# Application verifier has found an error in the current process.
	#
	ERROR_VERIFIER_STOP = 537 
	#
	# MessageId: ERROR_ABIOS_ERROR
	#
	# MessageText:
	#
	# An error occurred in the ABIOS subsystem.
	#
	ERROR_ABIOS_ERROR = 538 
	#
	# MessageId: ERROR_WX86_WARNING
	#
	# MessageText:
	#
	# A warning occurred in the WX86 subsystem.
	#
	ERROR_WX86_WARNING = 539 
	#
	# MessageId: ERROR_WX86_ERROR
	#
	# MessageText:
	#
	# An error occurred in the WX86 subsystem.
	#
	ERROR_WX86_ERROR = 540 
	#
	# MessageId: ERROR_TIMER_NOT_CANCELED
	#
	# MessageText:
	#
	# An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.
	#
	ERROR_TIMER_NOT_CANCELED = 541 
	#
	# MessageId: ERROR_UNWIND
	#
	# MessageText:
	#
	# Unwind exception code.
	#
	ERROR_UNWIND = 542 
	#
	# MessageId: ERROR_BAD_STACK
	#
	# MessageText:
	#
	# An invalid or unaligned stack was encountered during an unwind operation.
	#
	ERROR_BAD_STACK = 543 
	#
	# MessageId: ERROR_INVALID_UNWIND_TARGET
	#
	# MessageText:
	#
	# An invalid unwind target was encountered during an unwind operation.
	#
	ERROR_INVALID_UNWIND_TARGET = 544 
	#
	# MessageId: ERROR_INVALID_PORT_ATTRIBUTES
	#
	# MessageText:
	#
	# Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort
	#
	ERROR_INVALID_PORT_ATTRIBUTES = 545 
	#
	# MessageId: ERROR_PORT_MESSAGE_TOO_LONG
	#
	# MessageText:
	#
	# Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.
	#
	ERROR_PORT_MESSAGE_TOO_LONG = 546 
	#
	# MessageId: ERROR_INVALID_QUOTA_LOWER
	#
	# MessageText:
	#
	# An attempt was made to lower a quota limit below the current usage.
	#
	ERROR_INVALID_QUOTA_LOWER = 547 
	#
	# MessageId: ERROR_DEVICE_ALREADY_ATTACHED
	#
	# MessageText:
	#
	# An attempt was made to attach to a device that was already attached to another device.
	#
	ERROR_DEVICE_ALREADY_ATTACHED = 548 
	#
	# MessageId: ERROR_INSTRUCTION_MISALIGNMENT
	#
	# MessageText:
	#
	# An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.
	#
	ERROR_INSTRUCTION_MISALIGNMENT = 549 
	#
	# MessageId: ERROR_PROFILING_NOT_STARTED
	#
	# MessageText:
	#
	# Profiling not started.
	#
	ERROR_PROFILING_NOT_STARTED = 550 
	#
	# MessageId: ERROR_PROFILING_NOT_STOPPED
	#
	# MessageText:
	#
	# Profiling not stopped.
	#
	ERROR_PROFILING_NOT_STOPPED = 551 
	#
	# MessageId: ERROR_COULD_NOT_INTERPRET
	#
	# MessageText:
	#
	# The passed ACL did not contain the minimum required information.
	#
	ERROR_COULD_NOT_INTERPRET = 552 
	#
	# MessageId: ERROR_PROFILING_AT_LIMIT
	#
	# MessageText:
	#
	# The number of active profiling objects is at the maximum and no more may be started.
	#
	ERROR_PROFILING_AT_LIMIT = 553 
	#
	# MessageId: ERROR_CANT_WAIT
	#
	# MessageText:
	#
	# Used to indicate that an operation cannot continue without blocking for I/O.
	#
	ERROR_CANT_WAIT = 554 
	#
	# MessageId: ERROR_CANT_TERMINATE_SELF
	#
	# MessageText:
	#
	# Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.
	#
	ERROR_CANT_TERMINATE_SELF = 555 
	#
	# MessageId: ERROR_UNEXPECTED_MM_CREATE_ERR
	#
	# MessageText:
	#
	# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
	# In this case information is lost, however, the filter correctly handles the exception.
	#
	ERROR_UNEXPECTED_MM_CREATE_ERR = 556 
	#
	# MessageId: ERROR_UNEXPECTED_MM_MAP_ERROR
	#
	# MessageText:
	#
	# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
	# In this case information is lost, however, the filter correctly handles the exception.
	#
	ERROR_UNEXPECTED_MM_MAP_ERROR = 557 
	#
	# MessageId: ERROR_UNEXPECTED_MM_EXTEND_ERR
	#
	# MessageText:
	#
	# If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.
	# In this case information is lost, however, the filter correctly handles the exception.
	#
	ERROR_UNEXPECTED_MM_EXTEND_ERR = 558 
	#
	# MessageId: ERROR_BAD_FUNCTION_TABLE
	#
	# MessageText:
	#
	# A malformed function table was encountered during an unwind operation.
	#
	ERROR_BAD_FUNCTION_TABLE = 559 
	#
	# MessageId: ERROR_NO_GUID_TRANSLATION
	#
	# MessageText:
	#
	# Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.
	# This causes the protection attempt to fail, which may cause a file creation attempt to fail.
	#
	ERROR_NO_GUID_TRANSLATION = 560 
	#
	# MessageId: ERROR_INVALID_LDT_SIZE
	#
	# MessageText:
	#
	# Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.
	#
	ERROR_INVALID_LDT_SIZE = 561 
	#
	# MessageId: ERROR_INVALID_LDT_OFFSET
	#
	# MessageText:
	#
	# Indicates that the starting value for the LDT information was not an integral multiple of the selector size.
	#
	ERROR_INVALID_LDT_OFFSET = 563 
	#
	# MessageId: ERROR_INVALID_LDT_DESCRIPTOR
	#
	# MessageText:
	#
	# Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.
	#
	ERROR_INVALID_LDT_DESCRIPTOR = 564 
	#
	# MessageId: ERROR_TOO_MANY_THREADS
	#
	# MessageText:
	#
	# Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.
	#
	ERROR_TOO_MANY_THREADS = 565 
	#
	# MessageId: ERROR_THREAD_NOT_IN_PROCESS
	#
	# MessageText:
	#
	# An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.
	#
	ERROR_THREAD_NOT_IN_PROCESS = 566 
	#
	# MessageId: ERROR_PAGEFILE_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# Page file quota was exceeded.
	#
	ERROR_PAGEFILE_QUOTA_EXCEEDED = 567 
	#
	# MessageId: ERROR_LOGON_SERVER_CONFLICT
	#
	# MessageText:
	#
	# The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.
	#
	ERROR_LOGON_SERVER_CONFLICT = 568 
	#
	# MessageId: ERROR_SYNCHRONIZATION_REQUIRED
	#
	# MessageText:
	#
	# The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.
	#
	ERROR_SYNCHRONIZATION_REQUIRED = 569 
	#
	# MessageId: ERROR_NET_OPEN_FAILED
	#
	# MessageText:
	#
	# The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.
	#
	ERROR_NET_OPEN_FAILED = 570 
	#
	# MessageId: ERROR_IO_PRIVILEGE_FAILED
	#
	# MessageText:
	#
	# {Privilege Failed}
	# The I/O permissions for the process could not be changed.
	#
	ERROR_IO_PRIVILEGE_FAILED = 571 
	#
	# MessageId: ERROR_CONTROL_C_EXIT
	#
	# MessageText:
	#
	# {Application Exit by CTRL+C}
	# The application terminated as a result of a CTRL+C.
	#
	ERROR_CONTROL_C_EXIT = 572 # winnt
	#
	# MessageId: ERROR_MISSING_SYSTEMFILE
	#
	# MessageText:
	#
	# {Missing System File}
	# The required system file %hs is bad or missing.
	#
	ERROR_MISSING_SYSTEMFILE = 573 
	#
	# MessageId: ERROR_UNHANDLED_EXCEPTION
	#
	# MessageText:
	#
	# {Application Error}
	# The exception %s (0x%08lx) occurred in the application at location 0x%08lx.
	#
	ERROR_UNHANDLED_EXCEPTION = 574 
	#
	# MessageId: ERROR_APP_INIT_FAILURE
	#
	# MessageText:
	#
	# {Application Error}
	# The application was unable to start correctly (0x%lx). Click OK to close the application.
	#
	ERROR_APP_INIT_FAILURE = 575 
	#
	# MessageId: ERROR_PAGEFILE_CREATE_FAILED
	#
	# MessageText:
	#
	# {Unable to Create Paging File}
	# The creation of the paging file %hs failed (%lx). The requested size was %ld.
	#
	ERROR_PAGEFILE_CREATE_FAILED = 576 
	#
	# MessageId: ERROR_INVALID_IMAGE_HASH
	#
	# MessageText:
	#
	# Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.
	#
	ERROR_INVALID_IMAGE_HASH = 577 
	#
	# MessageId: ERROR_NO_PAGEFILE
	#
	# MessageText:
	#
	# {No Paging File Specified}
	# No paging file was specified in the system configuration.
	#
	ERROR_NO_PAGEFILE = 578 
	#
	# MessageId: ERROR_ILLEGAL_FLOAT_CONTEXT
	#
	# MessageText:
	#
	# {EXCEPTION}
	# A real-mode application issued a floating-point instruction and floating-point hardware is not present.
	#
	ERROR_ILLEGAL_FLOAT_CONTEXT = 579 
	#
	# MessageId: ERROR_NO_EVENT_PAIR
	#
	# MessageText:
	#
	# An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.
	#
	ERROR_NO_EVENT_PAIR = 580 
	#
	# MessageId: ERROR_DOMAIN_CTRLR_CONFIG_ERROR
	#
	# MessageText:
	#
	# A Windows Server has an incorrect configuration.
	#
	ERROR_DOMAIN_CTRLR_CONFIG_ERROR = 581 
	#
	# MessageId: ERROR_ILLEGAL_CHARACTER
	#
	# MessageText:
	#
	# An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.
	#
	ERROR_ILLEGAL_CHARACTER = 582 
	#
	# MessageId: ERROR_UNDEFINED_CHARACTER
	#
	# MessageText:
	#
	# The Unicode character is not defined in the Unicode character set installed on the system.
	#
	ERROR_UNDEFINED_CHARACTER = 583 
	#
	# MessageId: ERROR_FLOPPY_VOLUME
	#
	# MessageText:
	#
	# The paging file cannot be created on a floppy diskette.
	#
	ERROR_FLOPPY_VOLUME = 584 
	#
	# MessageId: ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT
	#
	# MessageText:
	#
	# The system BIOS failed to connect a system interrupt to the device or bus for which the device is connected.
	#
	ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT = 585 
	#
	# MessageId: ERROR_BACKUP_CONTROLLER
	#
	# MessageText:
	#
	# This operation is only allowed for the Primary Domain Controller of the domain.
	#
	ERROR_BACKUP_CONTROLLER = 586 
	#
	# MessageId: ERROR_MUTANT_LIMIT_EXCEEDED
	#
	# MessageText:
	#
	# An attempt was made to acquire a mutant such that its maximum count would have been exceeded.
	#
	ERROR_MUTANT_LIMIT_EXCEEDED = 587 
	#
	# MessageId: ERROR_FS_DRIVER_REQUIRED
	#
	# MessageText:
	#
	# A volume has been accessed for which a file system driver is required that has not yet been loaded.
	#
	ERROR_FS_DRIVER_REQUIRED = 588 
	#
	# MessageId: ERROR_CANNOT_LOAD_REGISTRY_FILE
	#
	# MessageText:
	#
	# {Registry File Failure}
	# The registry cannot load the hive (file):
	# %hs
	# or its log or alternate.
	# It is corrupt, absent, or not writable.
	#
	ERROR_CANNOT_LOAD_REGISTRY_FILE = 589 
	#
	# MessageId: ERROR_DEBUG_ATTACH_FAILED
	#
	# MessageText:
	#
	# {Unexpected Failure in DebugActiveProcess}
	# An unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.
	#
	ERROR_DEBUG_ATTACH_FAILED = 590 
	#
	# MessageId: ERROR_SYSTEM_PROCESS_TERMINATED
	#
	# MessageText:
	#
	# {Fatal System Error}
	# The %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).
	# The system has been shut down.
	#
	ERROR_SYSTEM_PROCESS_TERMINATED = 591 
	#
	# MessageId: ERROR_DATA_NOT_ACCEPTED
	#
	# MessageText:
	#
	# {Data Not Accepted}
	# The TDI client could not handle the data received during an indication.
	#
	ERROR_DATA_NOT_ACCEPTED = 592 
	#
	# MessageId: ERROR_VDM_HARD_ERROR
	#
	# MessageText:
	#
	# NTVDM encountered a hard error.
	#
	ERROR_VDM_HARD_ERROR = 593 
	#
	# MessageId: ERROR_DRIVER_CANCEL_TIMEOUT
	#
	# MessageText:
	#
	# {Cancel Timeout}
	# The driver %hs failed to complete a cancelled I/O request in the allotted time.
	#
	ERROR_DRIVER_CANCEL_TIMEOUT = 594 
	#
	# MessageId: ERROR_REPLY_MESSAGE_MISMATCH
	#
	# MessageText:
	#
	# {Reply Message Mismatch}
	# An attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.
	#
	ERROR_REPLY_MESSAGE_MISMATCH = 595 
	#
	# MessageId: ERROR_LOST_WRITEBEHIND_DATA
	#
	# MessageText:
	#
	# {Delayed Write Failed}
	# Windows was unable to save all the data for the file %hs. The data has been lost.
	# This error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.
	#
	ERROR_LOST_WRITEBEHIND_DATA = 596 
	#
	# MessageId: ERROR_CLIENT_SERVER_PARAMETERS_INVALID
	#
	# MessageText:
	#
	# The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.
	#
	ERROR_CLIENT_SERVER_PARAMETERS_INVALID = 597 
	#
	# MessageId: ERROR_NOT_TINY_STREAM
	#
	# MessageText:
	#
	# The stream is not a tiny stream.
	#
	ERROR_NOT_TINY_STREAM = 598 
	#
	# MessageId: ERROR_STACK_OVERFLOW_READ
	#
	# MessageText:
	#
	# The request must be handled by the stack overflow code.
	#
	ERROR_STACK_OVERFLOW_READ = 599 
	#
	# MessageId: ERROR_CONVERT_TO_LARGE
	#
	# MessageText:
	#
	# Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.
	#
	ERROR_CONVERT_TO_LARGE = 600 
	#
	# MessageId: ERROR_FOUND_OUT_OF_SCOPE
	#
	# MessageText:
	#
	# The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.
	#
	ERROR_FOUND_OUT_OF_SCOPE = 601 
	#
	# MessageId: ERROR_ALLOCATE_BUCKET
	#
	# MessageText:
	#
	# The bucket array must be grown. Retry transaction after doing so.
	#
	ERROR_ALLOCATE_BUCKET = 602 
	#
	# MessageId: ERROR_MARSHALL_OVERFLOW
	#
	# MessageText:
	#
	# The user/kernel marshalling buffer has overflowed.
	#
	ERROR_MARSHALL_OVERFLOW = 603 
	#
	# MessageId: ERROR_INVALID_VARIANT
	#
	# MessageText:
	#
	# The supplied variant structure contains invalid data.
	#
	ERROR_INVALID_VARIANT = 604 
	#
	# MessageId: ERROR_BAD_COMPRESSION_BUFFER
	#
	# MessageText:
	#
	# The specified buffer contains ill-formed data.
	#
	ERROR_BAD_COMPRESSION_BUFFER = 605 
	#
	# MessageId: ERROR_AUDIT_FAILED
	#
	# MessageText:
	#
	# {Audit Failed}
	# An attempt to generate a security audit failed.
	#
	ERROR_AUDIT_FAILED = 606 
	#
	# MessageId: ERROR_TIMER_RESOLUTION_NOT_SET
	#
	# MessageText:
	#
	# The timer resolution was not previously set by the current process.
	#
	ERROR_TIMER_RESOLUTION_NOT_SET = 607 
	#
	# MessageId: ERROR_INSUFFICIENT_LOGON_INFO
	#
	# MessageText:
	#
	# There is insufficient account information to log you on.
	#
	ERROR_INSUFFICIENT_LOGON_INFO = 608 
	#
	# MessageId: ERROR_BAD_DLL_ENTRYPOINT
	#
	# MessageText:
	#
	# {Invalid DLL Entrypoint}
	# The dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.
	# The entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.
	#
	ERROR_BAD_DLL_ENTRYPOINT = 609 
	#
	# MessageId: ERROR_BAD_SERVICE_ENTRYPOINT
	#
	# MessageText:
	#
	# {Invalid Service Callback Entrypoint}
	# The %hs service is not written correctly. The stack pointer has been left in an inconsistent state.
	# The callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.
	#
	ERROR_BAD_SERVICE_ENTRYPOINT = 610 
	#
	# MessageId: ERROR_IP_ADDRESS_CONFLICT1
	#
	# MessageText:
	#
	# There is an IP address conflict with another system on the network
	#
	ERROR_IP_ADDRESS_CONFLICT1 = 611 
	#
	# MessageId: ERROR_IP_ADDRESS_CONFLICT2
	#
	# MessageText:
	#
	# There is an IP address conflict with another system on the network
	#
	ERROR_IP_ADDRESS_CONFLICT2 = 612 
	#
	# MessageId: ERROR_REGISTRY_QUOTA_LIMIT
	#
	# MessageText:
	#
	# {Low On Registry Space}
	# The system has reached the maximum size allowed for the system part of the registry. Additional storage requests will be ignored.
	#
	ERROR_REGISTRY_QUOTA_LIMIT = 613 
	#
	# MessageId: ERROR_NO_CALLBACK_ACTIVE
	#
	# MessageText:
	#
	# A callback return system service cannot be executed when no callback is active.
	#
	ERROR_NO_CALLBACK_ACTIVE = 614 
	#
	# MessageId: ERROR_PWD_TOO_SHORT
	#
	# MessageText:
	#
	# The password provided is too short to meet the policy of your user account.
	# Please choose a longer password.
	#
	ERROR_PWD_TOO_SHORT = 615 
	#
	# MessageId: ERROR_PWD_TOO_RECENT
	#
	# MessageText:
	#
	# The policy of your user account does not allow you to change passwords too frequently.
	# This is done to prevent users from changing back to a familiar, but potentially discovered, password.
	# If you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.
	#
	ERROR_PWD_TOO_RECENT = 616 
	#
	# MessageId: ERROR_PWD_HISTORY_CONFLICT
	#
	# MessageText:
	#
	# You have attempted to change your password to one that you have used in the past.
	# The policy of your user account does not allow this. Please select a password that you have not previously used.
	#
	ERROR_PWD_HISTORY_CONFLICT = 617 
	#
	# MessageId: ERROR_UNSUPPORTED_COMPRESSION
	#
	# MessageText:
	#
	# The specified compression format is unsupported.
	#
	ERROR_UNSUPPORTED_COMPRESSION = 618 
	#
	# MessageId: ERROR_INVALID_HW_PROFILE
	#
	# MessageText:
	#
	# The specified hardware profile configuration is invalid.
	#
	ERROR_INVALID_HW_PROFILE = 619 
	#
	# MessageId: ERROR_INVALID_PLUGPLAY_DEVICE_PATH
	#
	# MessageText:
	#
	# The specified Plug and Play registry device path is invalid.
	#
	ERROR_INVALID_PLUGPLAY_DEVICE_PATH = 620 
	#
	# MessageId: ERROR_QUOTA_LIST_INCONSISTENT
	#
	# MessageText:
	#
	# The specified quota list is internally inconsistent with its descriptor.
	#
	ERROR_QUOTA_LIST_INCONSISTENT = 621 
	#
	# MessageId: ERROR_EVALUATION_EXPIRATION
	#
	# MessageText:
	#
	# {Windows Evaluation Notification}
	# The evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.
	#
	ERROR_EVALUATION_EXPIRATION = 622 
	#
	# MessageId: ERROR_ILLEGAL_DLL_RELOCATION
	#
	# MessageText:
	#
	# {Illegal System DLL Relocation}
	# The system DLL %hs was relocated in memory. The application will not run properly.
	# The relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.
	#
	ERROR_ILLEGAL_DLL_RELOCATION = 623 
	#
	# MessageId: ERROR_DLL_INIT_FAILED_LOGOFF
	#
	# MessageText:
	#
	# {DLL Initialization Failed}
	# The application failed to initialize because the window station is shutting down.
	#
	ERROR_DLL_INIT_FAILED_LOGOFF = 624 
	#
	# MessageId: ERROR_VALIDATE_CONTINUE
	#
	# MessageText:
	#
	# The validation process needs to continue on to the next step.
	#
	ERROR_VALIDATE_CONTINUE = 625 
	#
	# MessageId: ERROR_NO_MORE_MATCHES
	#
	# MessageText:
	#
	# There are no more matches for the current index enumeration.
	#
	ERROR_NO_MORE_MATCHES = 626 
	#
	# MessageId: ERROR_RANGE_LIST_CONFLICT
	#
	# MessageText:
	#
	# The range could not be added to the range list because of a conflict.
	#
	ERROR_RANGE_LIST_CONFLICT = 627 
	#
	# MessageId: ERROR_SERVER_SID_MISMATCH
	#
	# MessageText:
	#
	# The server process is running under a SID different than that required by client.
	#
	ERROR_SERVER_SID_MISMATCH = 628 
	#
	# MessageId: ERROR_CANT_ENABLE_DENY_ONLY
	#
	# MessageText:
	#
	# A group marked use for deny only cannot be enabled.
	#
	ERROR_CANT_ENABLE_DENY_ONLY = 629 
	#
	# MessageId: ERROR_FLOAT_MULTIPLE_FAULTS
	#
	# MessageText:
	#
	# {EXCEPTION}
	# Multiple floating point faults.
	#
	ERROR_FLOAT_MULTIPLE_FAULTS = 630 # winnt
	#
	# MessageId: ERROR_FLOAT_MULTIPLE_TRAPS
	#
	# MessageText:
	#
	# {EXCEPTION}
	# Multiple floating point traps.
	#
	ERROR_FLOAT_MULTIPLE_TRAPS = 631 # winnt
	#
	# MessageId: ERROR_NOINTERFACE
	#
	# MessageText:
	#
	# The requested interface is not supported.
	#
	ERROR_NOINTERFACE = 632 
	#
	# MessageId: ERROR_DRIVER_FAILED_SLEEP
	#
	# MessageText:
	#
	# {System Standby Failed}
	# The driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.
	#
	ERROR_DRIVER_FAILED_SLEEP = 633 
	#
	# MessageId: ERROR_CORRUPT_SYSTEM_FILE
	#
	# MessageText:
	#
	# The system file %1 has become corrupt and has been replaced.
	#
	ERROR_CORRUPT_SYSTEM_FILE = 634 
	#
	# MessageId: ERROR_COMMITMENT_MINIMUM
	#
	# MessageText:
	#
	# {Virtual Memory Minimum Too Low}
	# Your system is low on virtual memory. Windows is increasing the size of your virtual memory paging file.
	# During this process, memory requests for some applications may be denied. For more information, see Help.
	#
	ERROR_COMMITMENT_MINIMUM = 635 
	#
	# MessageId: ERROR_PNP_RESTART_ENUMERATION
	#
	# MessageText:
	#
	# A device was removed so enumeration must be restarted.
	#
	ERROR_PNP_RESTART_ENUMERATION = 636 
	#
	# MessageId: ERROR_SYSTEM_IMAGE_BAD_SIGNATURE
	#
	# MessageText:
	#
	# {Fatal System Error}
	# The system image %s is not properly signed.
	# The file has been replaced with the signed file.
	# The system has been shut down.
	#
	ERROR_SYSTEM_IMAGE_BAD_SIGNATURE = 637 
	#
	# MessageId: ERROR_PNP_REBOOT_REQUIRED
	#
	# MessageText:
	#
	# Device will not start without a reboot.
	#
	ERROR_PNP_REBOOT_REQUIRED = 638 
	#
	# MessageId: ERROR_INSUFFICIENT_POWER
	#
	# MessageText:
	#
	# There is not enough power to complete the requested operation.
	#
	ERROR_INSUFFICIENT_POWER = 639 
	#
	# MessageId: ERROR_MULTIPLE_FAULT_VIOLATION
	#
	# MessageText:
	#
	#  ERROR_MULTIPLE_FAULT_VIOLATION
	#
	ERROR_MULTIPLE_FAULT_VIOLATION = 640 
	#
	# MessageId: ERROR_SYSTEM_SHUTDOWN
	#
	# MessageText:
	#
	# The system is in the process of shutting down.
	#
	ERROR_SYSTEM_SHUTDOWN = 641 
	#
	# MessageId: ERROR_PORT_NOT_SET
	#
	# MessageText:
	#
	# An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.
	#
	ERROR_PORT_NOT_SET = 642 
	#
	# MessageId: ERROR_DS_VERSION_CHECK_FAILURE
	#
	# MessageText:
	#
	# This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.
	#
	ERROR_DS_VERSION_CHECK_FAILURE = 643 
	#
	# MessageId: ERROR_RANGE_NOT_FOUND
	#
	# MessageText:
	#
	# The specified range could not be found in the range list.
	#
	ERROR_RANGE_NOT_FOUND = 644 
	#
	# MessageId: ERROR_NOT_SAFE_MODE_DRIVER
	#
	# MessageText:
	#
	# The driver was not loaded because the system is booting into safe mode.
	#
	ERROR_NOT_SAFE_MODE_DRIVER = 646 
	#
	# MessageId: ERROR_FAILED_DRIVER_ENTRY
	#
	# MessageText:
	#
	# The driver was not loaded because it failed its initialization call.
	#
	ERROR_FAILED_DRIVER_ENTRY = 647 
	#
	# MessageId: ERROR_DEVICE_ENUMERATION_ERROR
	#
	# MessageText:
	#
	# The "%hs" encountered an error while applying power or reading the device configuration.
	# This may be caused by a failure of your hardware or by a poor connection.
	#
	ERROR_DEVICE_ENUMERATION_ERROR = 648 
	#
	# MessageId: ERROR_MOUNT_POINT_NOT_RESOLVED
	#
	# MessageText:
	#
	# The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.
	#
	ERROR_MOUNT_POINT_NOT_RESOLVED = 649 
	#
	# MessageId: ERROR_INVALID_DEVICE_OBJECT_PARAMETER
	#
	# MessageText:
	#
	# The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.
	#
	ERROR_INVALID_DEVICE_OBJECT_PARAMETER = 650 
	#
	# MessageId: ERROR_MCA_OCCURED
	#
	# MessageText:
	#
	# A Machine Check Error has occurred. Please check the system eventlog for additional information.
	#
	ERROR_MCA_OCCURED = 651 
	#
	# MessageId: ERROR_DRIVER_DATABASE_ERROR
	#
	# MessageText:
	#
	# There was error [%2] processing the driver database.
	#
	ERROR_DRIVER_DATABASE_ERROR = 652 
	#
	# MessageId: ERROR_SYSTEM_HIVE_TOO_LARGE
	#
	# MessageText:
	#
	# System hive size has exceeded its limit.
	#
	ERROR_SYSTEM_HIVE_TOO_LARGE = 653 
	#
	# MessageId: ERROR_DRIVER_FAILED_PRIOR_UNLOAD
	#
	# MessageText:
	#
	# The driver could not be loaded because a previous version of the driver is still in memory.
	#
	ERROR_DRIVER_FAILED_PRIOR_UNLOAD = 654 
	#
	# MessageId: ERROR_VOLSNAP_PREPARE_HIBERNATE
	#
	# MessageText:
	#
	# {Volume Shadow Copy Service}
	# Please wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.
	#
	ERROR_VOLSNAP_PREPARE_HIBERNATE = 655 
	#
	# MessageId: ERROR_HIBERNATION_FAILURE
	#
	# MessageText:
	#
	# The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.
	#
	ERROR_HIBERNATION_FAILURE = 656 
	#
	# MessageId: ERROR_PWD_TOO_LONG
	#
	# MessageText:
	#
	# The password provided is too long to meet the policy of your user account.
	# Please choose a shorter password.
	#
	ERROR_PWD_TOO_LONG = 657 
	#
	# MessageId: ERROR_FILE_SYSTEM_LIMITATION
	#
	# MessageText:
	#
	# The requested operation could not be completed due to a file system limitation
	#
	ERROR_FILE_SYSTEM_LIMITATION = 665 
	#
	# MessageId: ERROR_ASSERTION_FAILURE
	#
	# MessageText:
	#
	# An assertion failure has occurred.
	#
	ERROR_ASSERTION_FAILURE = 668 
	#
	# MessageId: ERROR_ACPI_ERROR
	#
	# MessageText:
	#
	# An error occurred in the ACPI subsystem.
	#
	ERROR_ACPI_ERROR = 669 
	#
	# MessageId: ERROR_WOW_ASSERTION
	#
	# MessageText:
	#
	# WOW Assertion Error.
	#
	ERROR_WOW_ASSERTION = 670 
	#
	# MessageId: ERROR_PNP_BAD_MPS_TABLE
	#
	# MessageText:
	#
	# A device is missing in the system BIOS MPS table. This device will not be used.
	# Please contact your system vendor for system BIOS update.
	#
	ERROR_PNP_BAD_MPS_TABLE = 671 
	#
	# MessageId: ERROR_PNP_TRANSLATION_FAILED
	#
	# MessageText:
	#
	# A translator failed to translate resources.
	#
	ERROR_PNP_TRANSLATION_FAILED = 672 
	#
	# MessageId: ERROR_PNP_IRQ_TRANSLATION_FAILED
	#
	# MessageText:
	#
	# A IRQ translator failed to translate resources.
	#
	ERROR_PNP_IRQ_TRANSLATION_FAILED = 673 
	#
	# MessageId: ERROR_PNP_INVALID_ID
	#
	# MessageText:
	#
	# Driver %2 returned invalid ID for a child device (%3).
	#
	ERROR_PNP_INVALID_ID = 674 
	#
	# MessageId: ERROR_WAKE_SYSTEM_DEBUGGER
	#
	# MessageText:
	#
	# {Kernel Debugger Awakened}
	# the system debugger was awakened by an interrupt.
	#
	ERROR_WAKE_SYSTEM_DEBUGGER = 675 
	#
	# MessageId: ERROR_HANDLES_CLOSED
	#
	# MessageText:
	#
	# {Handles Closed}
	# Handles to objects have been automatically closed as a result of the requested operation.
	#
	ERROR_HANDLES_CLOSED = 676 
	#
	# MessageId: ERROR_EXTRANEOUS_INFORMATION
	#
	# MessageText:
	#
	# {Too Much Information}
	# The specified access control list (ACL) contained more information than was expected.
	#
	ERROR_EXTRANEOUS_INFORMATION = 677 
	#
	# MessageId: ERROR_RXACT_COMMIT_NECESSARY
	#
	# MessageText:
	#
	# This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.
	# The commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).
	#
	ERROR_RXACT_COMMIT_NECESSARY = 678 
	#
	# MessageId: ERROR_MEDIA_CHECK
	#
	# MessageText:
	#
	# {Media Changed}
	# The media may have changed.
	#
	ERROR_MEDIA_CHECK = 679 
	#
	# MessageId: ERROR_GUID_SUBSTITUTION_MADE
	#
	# MessageText:
	#
	# {GUID Substitution}
	# During the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.
	# A substitute prefix was used, which will not compromise system security. However, this may provide a more restrictive access than intended.
	#
	ERROR_GUID_SUBSTITUTION_MADE = 680 
	#
	# MessageId: ERROR_STOPPED_ON_SYMLINK
	#
	# MessageText:
	#
	# The create operation stopped after reaching a symbolic link
	#
	ERROR_STOPPED_ON_SYMLINK = 681 
	#
	# MessageId: ERROR_LONGJUMP
	#
	# MessageText:
	#
	# A long jump has been executed.
	#
	ERROR_LONGJUMP = 682 
	#
	# MessageId: ERROR_PLUGPLAY_QUERY_VETOED
	#
	# MessageText:
	#
	# The Plug and Play query operation was not successful.
	#
	ERROR_PLUGPLAY_QUERY_VETOED = 683 
	#
	# MessageId: ERROR_UNWIND_CONSOLIDATE
	#
	# MessageText:
	#
	# A frame consolidation has been executed.
	#
	ERROR_UNWIND_CONSOLIDATE = 684 
	#
	# MessageId: ERROR_REGISTRY_HIVE_RECOVERED
	#
	# MessageText:
	#
	# {Registry Hive Recovered}
	# Registry hive (file):
	# %hs
	# was corrupted and it has been recovered. Some data might have been lost.
	#
	ERROR_REGISTRY_HIVE_RECOVERED = 685 
	#
	# MessageId: ERROR_DLL_MIGHT_BE_INSECURE
	#
	# MessageText:
	#
	# The application is attempting to run executable code from the module %hs. This may be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?
	#
	ERROR_DLL_MIGHT_BE_INSECURE = 686 
	#
	# MessageId: ERROR_DLL_MIGHT_BE_INCOMPATIBLE
	#
	# MessageText:
	#
	# The application is loading executable code from the module %hs. This is secure, but may be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?
	#
	ERROR_DLL_MIGHT_BE_INCOMPATIBLE = 687 
	#
	# MessageId: ERROR_DBG_EXCEPTION_NOT_HANDLED
	#
	# MessageText:
	#
	# Debugger did not handle the exception.
	#
	ERROR_DBG_EXCEPTION_NOT_HANDLED = 688 # winnt
	#
	# MessageId: ERROR_DBG_REPLY_LATER
	#
	# MessageText:
	#
	# Debugger will reply later.
	#
	ERROR_DBG_REPLY_LATER = 689 
	#
	# MessageId: ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE
	#
	# MessageText:
	#
	# Debugger cannot provide handle.
	#
	ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE = 690 
	#
	# MessageId: ERROR_DBG_TERMINATE_THREAD
	#
	# MessageText:
	#
	# Debugger terminated thread.
	#
	ERROR_DBG_TERMINATE_THREAD = 691 # winnt
	#
	# MessageId: ERROR_DBG_TERMINATE_PROCESS
	#
	# MessageText:
	#
	# Debugger terminated process.
	#
	ERROR_DBG_TERMINATE_PROCESS = 692 # winnt
	#
	# MessageId: ERROR_DBG_CONTROL_C
	#
	# MessageText:
	#
	# Debugger got control C.
	#
	ERROR_DBG_CONTROL_C = 693 # winnt
	#
	# MessageId: ERROR_DBG_PRINTEXCEPTION_C
	#
	# MessageText:
	#
	# Debugger printed exception on control C.
	#
	ERROR_DBG_PRINTEXCEPTION_C = 694 
	#
	# MessageId: ERROR_DBG_RIPEXCEPTION
	#
	# MessageText:
	#
	# Debugger received RIP exception.
	#
	ERROR_DBG_RIPEXCEPTION = 695 
	#
	# MessageId: ERROR_DBG_CONTROL_BREAK
	#
	# MessageText:
	#
	# Debugger received control break.
	#
	ERROR_DBG_CONTROL_BREAK = 696 # winnt
	#
	# MessageId: ERROR_DBG_COMMAND_EXCEPTION
	#
	# MessageText:
	#
	# Debugger command communication exception.
	#
	ERROR_DBG_COMMAND_EXCEPTION = 697 # winnt
	#
	# MessageId: ERROR_OBJECT_NAME_EXISTS
	#
	# MessageText:
	#
	# {Object Exists}
	# An attempt was made to create an object and the object name already existed.
	#
	ERROR_OBJECT_NAME_EXISTS = 698 
	#
	# MessageId: ERROR_THREAD_WAS_SUSPENDED
	#
	# MessageText:
	#
	# {Thread Suspended}
	# A thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.
	#
	ERROR_THREAD_WAS_SUSPENDED = 699 
	#
	# MessageId: ERROR_IMAGE_NOT_AT_BASE
	#
	# MessageText:
	#
	# {Image Relocated}
	# An image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.
	#
	ERROR_IMAGE_NOT_AT_BASE = 700 
	#
	# MessageId: ERROR_RXACT_STATE_CREATED
	#
	# MessageText:
	#
	# This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.
	#
	ERROR_RXACT_STATE_CREATED = 701 
	#
	# MessageId: ERROR_SEGMENT_NOTIFICATION
	#
	# MessageText:
	#
	# {Segment Load}
	# A virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.
	# An exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.
	#
	ERROR_SEGMENT_NOTIFICATION = 702 # winnt
	#
	# MessageId: ERROR_BAD_CURRENT_DIRECTORY
	#
	# MessageText:
	#
	# {Invalid Current Directory}
	# The process cannot switch to the startup current directory %hs.
	# Select OK to set current directory to %hs, or select CANCEL to exit.
	#
	ERROR_BAD_CURRENT_DIRECTORY = 703 
	#
	# MessageId: ERROR_FT_READ_RECOVERY_FROM_BACKUP
	#
	# MessageText:
	#
	# {Redundant Read}
	# To satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.
	# This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.
	#
	ERROR_FT_READ_RECOVERY_FROM_BACKUP = 704 
	#
	# MessageId: ERROR_FT_WRITE_RECOVERY
	#
	# MessageText:
	#
	# {Redundant Write}
	# To satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.
	# This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.
	#
	ERROR_FT_WRITE_RECOVERY = 705 
	#
	# MessageId: ERROR_IMAGE_MACHINE_TYPE_MISMATCH
	#
	# MessageText:
	#
	# {Machine Type Mismatch}
	# The image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.
	#
	ERROR_IMAGE_MACHINE_TYPE_MISMATCH = 706 
	#
	# MessageId: ERROR_RECEIVE_PARTIAL
	#
	# MessageText:
	#
	# {Partial Data Received}
	# The network transport returned partial data to its client. The remaining data will be sent later.
	#
	ERROR_RECEIVE_PARTIAL = 707 
	#
	# MessageId: ERROR_RECEIVE_EXPEDITED
	#
	# MessageText:
	#
	# {Expedited Data Received}
	# The network transport returned data to its client that was marked as expedited by the remote system.
	#
	ERROR_RECEIVE_EXPEDITED = 708 
	#
	# MessageId: ERROR_RECEIVE_PARTIAL_EXPEDITED
	#
	# MessageText:
	#
	# {Partial Expedited Data Received}
	# The network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.
	#
	ERROR_RECEIVE_PARTIAL_EXPEDITED = 709 
	#
	# MessageId: ERROR_EVENT_DONE
	#
	# MessageText:
	#
	# {TDI Event Done}
	# The TDI indication has completed successfully.
	#
	ERROR_EVENT_DONE = 710 
	#
	# MessageId: ERROR_EVENT_PENDING
	#
	# MessageText:
	#
	# {TDI Event Pending}
	# The TDI indication has entered the pending state.
	#
	ERROR_EVENT_PENDING = 711 
	#
	# MessageId: ERROR_CHECKING_FILE_SYSTEM
	#
	# MessageText:
	#
	# Checking file system on %wZ
	#
	ERROR_CHECKING_FILE_SYSTEM = 712 
	#
	# MessageId: ERROR_FATAL_APP_EXIT
	#
	# MessageText:
	#
	# {Fatal Application Exit}
	# %hs
	#
	ERROR_FATAL_APP_EXIT = 713 
	#
	# MessageId: ERROR_PREDEFINED_HANDLE
	#
	# MessageText:
	#
	# The specified registry key is referenced by a predefined handle.
	#
	ERROR_PREDEFINED_HANDLE = 714 
	#
	# MessageId: ERROR_WAS_UNLOCKED
	#
	# MessageText:
	#
	# {Page Unlocked}
	# The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.
	#
	ERROR_WAS_UNLOCKED = 715 
	#
	# MessageId: ERROR_SERVICE_NOTIFICATION
	#
	# MessageText:
	#
	# %hs
	#
	ERROR_SERVICE_NOTIFICATION = 716 
	#
	# MessageId: ERROR_WAS_LOCKED
	#
	# MessageText:
	#
	# {Page Locked}
	# One of the pages to lock was already locked.
	#
	ERROR_WAS_LOCKED = 717 
	#
	# MessageId: ERROR_LOG_HARD_ERROR
	#
	# MessageText:
	#
	# Application popup: %1 : %2
	#
	ERROR_LOG_HARD_ERROR = 718 
	#
	# MessageId: ERROR_ALREADY_WIN32
	#
	# MessageText:
	#
	#  ERROR_ALREADY_WIN32
	#
	ERROR_ALREADY_WIN32 = 719 
	#
	# MessageId: ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE
	#
	# MessageText:
	#
	# {Machine Type Mismatch}
	# The image file %hs is valid, but is for a machine type other than the current machine.
	#
	ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE = 720 
	#
	# MessageId: ERROR_NO_YIELD_PERFORMED
	#
	# MessageText:
	#
	# A yield execution was performed and no thread was available to run.
	#
	ERROR_NO_YIELD_PERFORMED = 721 
	#
	# MessageId: ERROR_TIMER_RESUME_IGNORED
	#
	# MessageText:
	#
	# The resumable flag to a timer API was ignored.
	#
	ERROR_TIMER_RESUME_IGNORED = 722 
	#
	# MessageId: ERROR_ARBITRATION_UNHANDLED
	#
	# MessageText:
	#
	# The arbiter has deferred arbitration of these resources to its parent
	#
	ERROR_ARBITRATION_UNHANDLED = 723 
	#
	# MessageId: ERROR_CARDBUS_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The inserted CardBus device cannot be started because of a configuration error on "%hs".
	#
	ERROR_CARDBUS_NOT_SUPPORTED = 724 
	#
	# MessageId: ERROR_MP_PROCESSOR_MISMATCH
	#
	# MessageText:
	#
	# The CPUs in this multiprocessor system are not all the same revision level. To use all processors the operating system restricts itself to the features of the least capable processor in the system. Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.
	#
	ERROR_MP_PROCESSOR_MISMATCH = 725 
	#
	# MessageId: ERROR_HIBERNATED
	#
	# MessageText:
	#
	# The system was put into hibernation.
	#
	ERROR_HIBERNATED = 726 
	#
	# MessageId: ERROR_RESUME_HIBERNATION
	#
	# MessageText:
	#
	# The system was resumed from hibernation.
	#
	ERROR_RESUME_HIBERNATION = 727 
	#
	# MessageId: ERROR_FIRMWARE_UPDATED
	#
	# MessageText:
	#
	# Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].
	#
	ERROR_FIRMWARE_UPDATED = 728 
	#
	# MessageId: ERROR_DRIVERS_LEAKING_LOCKED_PAGES
	#
	# MessageText:
	#
	# A device driver is leaking locked I/O pages causing system degradation. The system has automatically enabled tracking code in order to try and catch the culprit.
	#
	ERROR_DRIVERS_LEAKING_LOCKED_PAGES = 729 
	#
	# MessageId: ERROR_WAKE_SYSTEM
	#
	# MessageText:
	#
	# The system has awoken
	#
	ERROR_WAKE_SYSTEM = 730 
	#
	# MessageId: ERROR_WAIT_1
	#
	# MessageText:
	#
	#  ERROR_WAIT_1
	#
	ERROR_WAIT_1 = 731 
	#
	# MessageId: ERROR_WAIT_2
	#
	# MessageText:
	#
	#  ERROR_WAIT_2
	#
	ERROR_WAIT_2 = 732 
	#
	# MessageId: ERROR_WAIT_3
	#
	# MessageText:
	#
	#  ERROR_WAIT_3
	#
	ERROR_WAIT_3 = 733 
	#
	# MessageId: ERROR_WAIT_63
	#
	# MessageText:
	#
	#  ERROR_WAIT_63
	#
	ERROR_WAIT_63 = 734 
	#
	# MessageId: ERROR_ABANDONED_WAIT_0
	#
	# MessageText:
	#
	#  ERROR_ABANDONED_WAIT_0
	#
	ERROR_ABANDONED_WAIT_0 = 735 # winnt
	#
	# MessageId: ERROR_ABANDONED_WAIT_63
	#
	# MessageText:
	#
	#  ERROR_ABANDONED_WAIT_63
	#
	ERROR_ABANDONED_WAIT_63 = 736 
	#
	# MessageId: ERROR_USER_APC
	#
	# MessageText:
	#
	#  ERROR_USER_APC
	#
	ERROR_USER_APC = 737 # winnt
	#
	# MessageId: ERROR_KERNEL_APC
	#
	# MessageText:
	#
	#  ERROR_KERNEL_APC
	#
	ERROR_KERNEL_APC = 738 
	#
	# MessageId: ERROR_ALERTED
	#
	# MessageText:
	#
	#  ERROR_ALERTED
	#
	ERROR_ALERTED = 739 
	#
	# MessageId: ERROR_ELEVATION_REQUIRED
	#
	# MessageText:
	#
	# The requested operation requires elevation.
	#
	ERROR_ELEVATION_REQUIRED = 740 
	#
	# MessageId: ERROR_REPARSE
	#
	# MessageText:
	#
	# A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.
	#
	ERROR_REPARSE = 741 
	#
	# MessageId: ERROR_OPLOCK_BREAK_IN_PROGRESS
	#
	# MessageText:
	#
	# An open/create operation completed while an oplock break is underway.
	#
	ERROR_OPLOCK_BREAK_IN_PROGRESS = 742 
	#
	# MessageId: ERROR_VOLUME_MOUNTED
	#
	# MessageText:
	#
	# A new volume has been mounted by a file system.
	#
	ERROR_VOLUME_MOUNTED = 743 
	#
	# MessageId: ERROR_RXACT_COMMITTED
	#
	# MessageText:
	#
	# This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.
	# The commit has now been completed.
	#
	ERROR_RXACT_COMMITTED = 744 
	#
	# MessageId: ERROR_NOTIFY_CLEANUP
	#
	# MessageText:
	#
	# This indicates that a notify change request has been completed due to closing the handle which made the notify change request.
	#
	ERROR_NOTIFY_CLEANUP = 745 
	#
	# MessageId: ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED
	#
	# MessageText:
	#
	# {Connect Failure on Primary Transport}
	# An attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.
	# The computer WAS able to connect on a secondary transport.
	#
	ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED = 746 
	#
	# MessageId: ERROR_PAGE_FAULT_TRANSITION
	#
	# MessageText:
	#
	# Page fault was a transition fault.
	#
	ERROR_PAGE_FAULT_TRANSITION = 747 
	#
	# MessageId: ERROR_PAGE_FAULT_DEMAND_ZERO
	#
	# MessageText:
	#
	# Page fault was a demand zero fault.
	#
	ERROR_PAGE_FAULT_DEMAND_ZERO = 748 
	#
	# MessageId: ERROR_PAGE_FAULT_COPY_ON_WRITE
	#
	# MessageText:
	#
	# Page fault was a demand zero fault.
	#
	ERROR_PAGE_FAULT_COPY_ON_WRITE = 749 
	#
	# MessageId: ERROR_PAGE_FAULT_GUARD_PAGE
	#
	# MessageText:
	#
	# Page fault was a demand zero fault.
	#
	ERROR_PAGE_FAULT_GUARD_PAGE = 750 
	#
	# MessageId: ERROR_PAGE_FAULT_PAGING_FILE
	#
	# MessageText:
	#
	# Page fault was satisfied by reading from a secondary storage device.
	#
	ERROR_PAGE_FAULT_PAGING_FILE = 751 
	#
	# MessageId: ERROR_CACHE_PAGE_LOCKED
	#
	# MessageText:
	#
	# Cached page was locked during operation.
	#
	ERROR_CACHE_PAGE_LOCKED = 752 
	#
	# MessageId: ERROR_CRASH_DUMP
	#
	# MessageText:
	#
	# Crash dump exists in paging file.
	#
	ERROR_CRASH_DUMP = 753 
	#
	# MessageId: ERROR_BUFFER_ALL_ZEROS
	#
	# MessageText:
	#
	# Specified buffer contains all zeros.
	#
	ERROR_BUFFER_ALL_ZEROS = 754 
	#
	# MessageId: ERROR_REPARSE_OBJECT
	#
	# MessageText:
	#
	# A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.
	#
	ERROR_REPARSE_OBJECT = 755 
	#
	# MessageId: ERROR_RESOURCE_REQUIREMENTS_CHANGED
	#
	# MessageText:
	#
	# The device has succeeded a query-stop and its resource requirements have changed.
	#
	ERROR_RESOURCE_REQUIREMENTS_CHANGED = 756 
	#
	# MessageId: ERROR_TRANSLATION_COMPLETE
	#
	# MessageText:
	#
	# The translator has translated these resources into the global space and no further translations should be performed.
	#
	ERROR_TRANSLATION_COMPLETE = 757 
	#
	# MessageId: ERROR_NOTHING_TO_TERMINATE
	#
	# MessageText:
	#
	# A process being terminated has no threads to terminate.
	#
	ERROR_NOTHING_TO_TERMINATE = 758 
	#
	# MessageId: ERROR_PROCESS_NOT_IN_JOB
	#
	# MessageText:
	#
	# The specified process is not part of a job.
	#
	ERROR_PROCESS_NOT_IN_JOB = 759 
	#
	# MessageId: ERROR_PROCESS_IN_JOB
	#
	# MessageText:
	#
	# The specified process is part of a job.
	#
	ERROR_PROCESS_IN_JOB = 760 
	#
	# MessageId: ERROR_VOLSNAP_HIBERNATE_READY
	#
	# MessageText:
	#
	# {Volume Shadow Copy Service}
	# The system is now ready for hibernation.
	#
	ERROR_VOLSNAP_HIBERNATE_READY = 761 
	#
	# MessageId: ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY
	#
	# MessageText:
	#
	# A file system or file system filter driver has successfully completed an FsFilter operation.
	#
	ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY = 762 
	#
	# MessageId: ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED
	#
	# MessageText:
	#
	# The specified interrupt vector was already connected.
	#
	ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED = 763 
	#
	# MessageId: ERROR_INTERRUPT_STILL_CONNECTED
	#
	# MessageText:
	#
	# The specified interrupt vector is still connected.
	#
	ERROR_INTERRUPT_STILL_CONNECTED = 764 
	#
	# MessageId: ERROR_WAIT_FOR_OPLOCK
	#
	# MessageText:
	#
	# An operation is blocked waiting for an oplock.
	#
	ERROR_WAIT_FOR_OPLOCK = 765 
	#
	# MessageId: ERROR_DBG_EXCEPTION_HANDLED
	#
	# MessageText:
	#
	# Debugger handled exception
	#
	ERROR_DBG_EXCEPTION_HANDLED = 766 # winnt
	#
	# MessageId: ERROR_DBG_CONTINUE
	#
	# MessageText:
	#
	# Debugger continued
	#
	ERROR_DBG_CONTINUE = 767 # winnt
	#
	# MessageId: ERROR_CALLBACK_POP_STACK
	#
	# MessageText:
	#
	# An exception occurred in a user mode callback and the kernel callback frame should be removed.
	#
	ERROR_CALLBACK_POP_STACK = 768 
	#
	# MessageId: ERROR_COMPRESSION_DISABLED
	#
	# MessageText:
	#
	# Compression is disabled for this volume.
	#
	ERROR_COMPRESSION_DISABLED = 769 
	#
	# MessageId: ERROR_CANTFETCHBACKWARDS
	#
	# MessageText:
	#
	# The data provider cannot fetch backwards through a result set.
	#
	ERROR_CANTFETCHBACKWARDS = 770 
	#
	# MessageId: ERROR_CANTSCROLLBACKWARDS
	#
	# MessageText:
	#
	# The data provider cannot scroll backwards through a result set.
	#
	ERROR_CANTSCROLLBACKWARDS = 771 
	#
	# MessageId: ERROR_ROWSNOTRELEASED
	#
	# MessageText:
	#
	# The data provider requires that previously fetched data is released before asking for more data.
	#
	ERROR_ROWSNOTRELEASED = 772 
	#
	# MessageId: ERROR_BAD_ACCESSOR_FLAGS
	#
	# MessageText:
	#
	# The data provider was not able to interpret the flags set for a column binding in an accessor.
	#
	ERROR_BAD_ACCESSOR_FLAGS = 773 
	#
	# MessageId: ERROR_ERRORS_ENCOUNTERED
	#
	# MessageText:
	#
	# One or more errors occurred while processing the request.
	#
	ERROR_ERRORS_ENCOUNTERED = 774 
	#
	# MessageId: ERROR_NOT_CAPABLE
	#
	# MessageText:
	#
	# The implementation is not capable of performing the request.
	#
	ERROR_NOT_CAPABLE = 775 
	#
	# MessageId: ERROR_REQUEST_OUT_OF_SEQUENCE
	#
	# MessageText:
	#
	# The client of a component requested an operation which is not valid given the state of the component instance.
	#
	ERROR_REQUEST_OUT_OF_SEQUENCE = 776 
	#
	# MessageId: ERROR_VERSION_PARSE_ERROR
	#
	# MessageText:
	#
	# A version number could not be parsed.
	#
	ERROR_VERSION_PARSE_ERROR = 777 
	#
	# MessageId: ERROR_BADSTARTPOSITION
	#
	# MessageText:
	#
	# The iterator's start position is invalid.
	#
	ERROR_BADSTARTPOSITION = 778 
	#
	# MessageId: ERROR_MEMORY_HARDWARE
	#
	# MessageText:
	#
	# The hardware has reported an uncorrectable memory error.
	#
	ERROR_MEMORY_HARDWARE = 779 
	#
	# MessageId: ERROR_DISK_REPAIR_DISABLED
	#
	# MessageText:
	#
	# The attempted operation required self healing to be enabled.
	#
	ERROR_DISK_REPAIR_DISABLED = 780 
	#
	# MessageId: ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE
	#
	# MessageText:
	#
	# The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.
	#
	ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE = 781 
	#
	# MessageId: ERROR_SYSTEM_POWERSTATE_TRANSITION
	#
	# MessageText:
	#
	# The system power state is transitioning from %2 to %3.
	#
	ERROR_SYSTEM_POWERSTATE_TRANSITION = 782 
	#
	# MessageId: ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION
	#
	# MessageText:
	#
	# The system power state is transitioning from %2 to %3 but could enter %4.
	#
	ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION = 783 
	#
	# MessageId: ERROR_MCA_EXCEPTION
	#
	# MessageText:
	#
	# A thread is getting dispatched with MCA EXCEPTION because of MCA.
	#
	ERROR_MCA_EXCEPTION = 784 
	#
	# MessageId: ERROR_ACCESS_AUDIT_BY_POLICY
	#
	# MessageText:
	#
	# Access to %1 is monitored by policy rule %2.
	#
	ERROR_ACCESS_AUDIT_BY_POLICY = 785 
	#
	# MessageId: ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY
	#
	# MessageText:
	#
	# Access to %1 has been restricted by your Administrator by policy rule %2.
	#
	ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY = 786 
	#
	# MessageId: ERROR_ABANDON_HIBERFILE
	#
	# MessageText:
	#
	# A valid hibernation file has been invalidated and should be abandoned.
	#
	ERROR_ABANDON_HIBERFILE = 787 
	#
	# MessageId: ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED
	#
	# MessageText:
	#
	# {Delayed Write Failed}
	# Windows was unable to save all the data for the file %hs; the data has been lost.
	# This error may be caused by network connectivity issues. Please try to save this file elsewhere.
	#
	ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED = 788 
	#
	# MessageId: ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR
	#
	# MessageText:
	#
	# {Delayed Write Failed}
	# Windows was unable to save all the data for the file %hs; the data has been lost.
	# This error was returned by the server on which the file exists. Please try to save this file elsewhere.
	#
	ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR = 789 
	#
	# MessageId: ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR
	#
	# MessageText:
	#
	# {Delayed Write Failed}
	# Windows was unable to save all the data for the file %hs; the data has been lost.
	# This error may be caused if the device has been removed or the media is write-protected.
	#
	ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR = 790 
	#
	# MessageId: ERROR_BAD_MCFG_TABLE
	#
	# MessageText:
	#
	# The resources required for this device conflict with the MCFG table.
	#
	ERROR_BAD_MCFG_TABLE = 791 
	#
	# MessageId: ERROR_DISK_REPAIR_REDIRECTED
	#
	# MessageText:
	#
	# The volume repair could not be performed while it is online.
	# Please schedule to take the volume offline so that it can be repaired.
	#
	ERROR_DISK_REPAIR_REDIRECTED = 792 
	#
	# MessageId: ERROR_DISK_REPAIR_UNSUCCESSFUL
	#
	# MessageText:
	#
	# The volume repair was not successful.
	#
	ERROR_DISK_REPAIR_UNSUCCESSFUL = 793 
	#
	# MessageId: ERROR_CORRUPT_LOG_OVERFULL
	#
	# MessageText:
	#
	# One of the volume corruption logs is full. Further corruptions that may be detected won't be logged.
	#
	ERROR_CORRUPT_LOG_OVERFULL = 794 
	#
	# MessageId: ERROR_CORRUPT_LOG_CORRUPTED
	#
	# MessageText:
	#
	# One of the volume corruption logs is internally corrupted and needs to be recreated. The volume may contain undetected corruptions and must be scanned.
	#
	ERROR_CORRUPT_LOG_CORRUPTED = 795 
	#
	# MessageId: ERROR_CORRUPT_LOG_UNAVAILABLE
	#
	# MessageText:
	#
	# One of the volume corruption logs is unavailable for being operated on.
	#
	ERROR_CORRUPT_LOG_UNAVAILABLE = 796 
	#
	# MessageId: ERROR_CORRUPT_LOG_DELETED_FULL
	#
	# MessageText:
	#
	# One of the volume corruption logs was deleted while still having corruption records in them. The volume contains detected corruptions and must be scanned.
	#
	ERROR_CORRUPT_LOG_DELETED_FULL = 797 
	#
	# MessageId: ERROR_CORRUPT_LOG_CLEARED
	#
	# MessageText:
	#
	# One of the volume corruption logs was cleared by chkdsk and no longer contains real corruptions.
	#
	ERROR_CORRUPT_LOG_CLEARED = 798 
	#
	# MessageId: ERROR_ORPHAN_NAME_EXHAUSTED
	#
	# MessageText:
	#
	# Orphaned files exist on the volume but could not be recovered because no more new names could be created in the recovery directory. Files must be moved from the recovery directory.
	#
	ERROR_ORPHAN_NAME_EXHAUSTED = 799 
	#
	# MessageId: ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE
	#
	# MessageText:
	#
	# The oplock that was associated with this handle is now associated with a different handle.
	#
	ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE = 800 
	#
	# MessageId: ERROR_CANNOT_GRANT_REQUESTED_OPLOCK
	#
	# MessageText:
	#
	# An oplock of the requested level cannot be granted.  An oplock of a lower level may be available.
	#
	ERROR_CANNOT_GRANT_REQUESTED_OPLOCK = 801 
	#
	# MessageId: ERROR_CANNOT_BREAK_OPLOCK
	#
	# MessageText:
	#
	# The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.
	#
	ERROR_CANNOT_BREAK_OPLOCK = 802 
	#
	# MessageId: ERROR_OPLOCK_HANDLE_CLOSED
	#
	# MessageText:
	#
	# The handle with which this oplock was associated has been closed.  The oplock is now broken.
	#
	ERROR_OPLOCK_HANDLE_CLOSED = 803 
	#
	# MessageId: ERROR_NO_ACE_CONDITION
	#
	# MessageText:
	#
	# The specified access control entry (ACE) does not contain a condition.
	#
	ERROR_NO_ACE_CONDITION = 804 
	#
	# MessageId: ERROR_INVALID_ACE_CONDITION
	#
	# MessageText:
	#
	# The specified access control entry (ACE) contains an invalid condition.
	#
	ERROR_INVALID_ACE_CONDITION = 805 
	#
	# MessageId: ERROR_FILE_HANDLE_REVOKED
	#
	# MessageText:
	#
	# Access to the specified file handle has been revoked.
	#
	ERROR_FILE_HANDLE_REVOKED = 806 
	#
	# MessageId: ERROR_IMAGE_AT_DIFFERENT_BASE
	#
	# MessageText:
	#
	# {Image Relocated}
	# An image file was mapped at a different address from the one specified in the image file but fixups will still be automatically performed on the image.
	#
	ERROR_IMAGE_AT_DIFFERENT_BASE = 807 
	#
	# MessageId: ERROR_ENCRYPTED_IO_NOT_POSSIBLE
	#
	# MessageText:
	#
	# The read or write operation to an encrypted file could not be completed because the file has not been opened for data access.
	#
	ERROR_ENCRYPTED_IO_NOT_POSSIBLE = 808 
	#
	# MessageId: ERROR_FILE_METADATA_OPTIMIZATION_IN_PROGRESS
	#
	# MessageText:
	#
	# File metadata optimization is already in progress.
	#
	ERROR_FILE_METADATA_OPTIMIZATION_IN_PROGRESS = 809 
	#
	# MessageId: ERROR_QUOTA_ACTIVITY
	#
	# MessageText:
	#
	# The requested operation failed due to quota operation is still in progress.
	#
	ERROR_QUOTA_ACTIVITY = 810 
	#
	# MessageId: ERROR_HANDLE_REVOKED
	#
	# MessageText:
	#
	# Access to the specified handle has been revoked.
	#
	ERROR_HANDLE_REVOKED = 811 
	#
	# MessageId: ERROR_CALLBACK_INVOKE_INLINE
	#
	# MessageText:
	#
	# The callback function must be invoked inline.
	#
	ERROR_CALLBACK_INVOKE_INLINE = 812 
	#
	# MessageId: ERROR_CPU_SET_INVALID
	#
	# MessageText:
	#
	# The specified CPU Set IDs are invalid.
	#
	ERROR_CPU_SET_INVALID = 813 
	#
	# MessageId: ERROR_ENCLAVE_NOT_TERMINATED
	#
	# MessageText:
	#
	# The specified enclave has not yet been terminated.
	#
	ERROR_ENCLAVE_NOT_TERMINATED = 814 
	#
	# MessageId: ERROR_ENCLAVE_VIOLATION
	#
	# MessageText:
	#
	# An attempt was made to access protected memory in violation of its secure access policy.
	#
	ERROR_ENCLAVE_VIOLATION = 815 
	#
	# **** Available SYSTEM error codes ****
	#
	#
	# MessageId: ERROR_EA_ACCESS_DENIED
	#
	# MessageText:
	#
	# Access to the extended attribute was denied.
	#
	ERROR_EA_ACCESS_DENIED = 994 
	#
	# MessageId: ERROR_OPERATION_ABORTED
	#
	# MessageText:
	#
	# The I/O operation has been aborted because of either a thread exit or an application request.
	#
	ERROR_OPERATION_ABORTED = 995 
	#
	# MessageId: ERROR_IO_INCOMPLETE
	#
	# MessageText:
	#
	# Overlapped I/O event is not in a signaled state.
	#
	ERROR_IO_INCOMPLETE = 996 
	#
	# MessageId: ERROR_IO_PENDING
	#
	# MessageText:
	#
	# Overlapped I/O operation is in progress.
	#
	ERROR_IO_PENDING = 997 # dderror
	#
	# MessageId: ERROR_NOACCESS
	#
	# MessageText:
	#
	# Invalid access to memory location.
	#
	ERROR_NOACCESS = 998 
	#
	# MessageId: ERROR_SWAPERROR
	#
	# MessageText:
	#
	# Error performing inpage operation.
	#
	ERROR_SWAPERROR = 999 
	#
	# MessageId: ERROR_STACK_OVERFLOW
	#
	# MessageText:
	#
	# Recursion too deep; the stack overflowed.
	#
	ERROR_STACK_OVERFLOW = 1001 
	#
	# MessageId: ERROR_INVALID_MESSAGE
	#
	# MessageText:
	#
	# The window cannot act on the sent message.
	#
	ERROR_INVALID_MESSAGE = 1002 
	#
	# MessageId: ERROR_CAN_NOT_COMPLETE
	#
	# MessageText:
	#
	# Cannot complete this function.
	#
	ERROR_CAN_NOT_COMPLETE = 1003 
	#
	# MessageId: ERROR_INVALID_FLAGS
	#
	# MessageText:
	#
	# Invalid flags.
	#
	ERROR_INVALID_FLAGS = 1004 
	#
	# MessageId: ERROR_UNRECOGNIZED_VOLUME
	#
	# MessageText:
	#
	# The volume does not contain a recognized file system.
	# Please make sure that all required file system drivers are loaded and that the volume is not corrupted.
	#
	ERROR_UNRECOGNIZED_VOLUME = 1005 
	#
	# MessageId: ERROR_FILE_INVALID
	#
	# MessageText:
	#
	# The volume for a file has been externally altered so that the opened file is no longer valid.
	#
	ERROR_FILE_INVALID = 1006 
	#
	# MessageId: ERROR_FULLSCREEN_MODE
	#
	# MessageText:
	#
	# The requested operation cannot be performed in full-screen mode.
	#
	ERROR_FULLSCREEN_MODE = 1007 
	#
	# MessageId: ERROR_NO_TOKEN
	#
	# MessageText:
	#
	# An attempt was made to reference a token that does not exist.
	#
	ERROR_NO_TOKEN = 1008 
	#
	# MessageId: ERROR_BADDB
	#
	# MessageText:
	#
	# The configuration registry database is corrupt.
	#
	ERROR_BADDB = 1009 
	#
	# MessageId: ERROR_BADKEY
	#
	# MessageText:
	#
	# The configuration registry key is invalid.
	#
	ERROR_BADKEY = 1010 
	#
	# MessageId: ERROR_CANTOPEN
	#
	# MessageText:
	#
	# The configuration registry key could not be opened.
	#
	ERROR_CANTOPEN = 1011 
	#
	# MessageId: ERROR_CANTREAD
	#
	# MessageText:
	#
	# The configuration registry key could not be read.
	#
	ERROR_CANTREAD = 1012 
	#
	# MessageId: ERROR_CANTWRITE
	#
	# MessageText:
	#
	# The configuration registry key could not be written.
	#
	ERROR_CANTWRITE = 1013 
	#
	# MessageId: ERROR_REGISTRY_RECOVERED
	#
	# MessageText:
	#
	# One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.
	#
	ERROR_REGISTRY_RECOVERED = 1014 
	#
	# MessageId: ERROR_REGISTRY_CORRUPT
	#
	# MessageText:
	#
	# The registry is corrupted. The structure of one of the files containing registry data is corrupted, or the system's memory image of the file is corrupted, or the file could not be recovered because the alternate copy or log was absent or corrupted.
	#
	ERROR_REGISTRY_CORRUPT = 1015 
	#
	# MessageId: ERROR_REGISTRY_IO_FAILED
	#
	# MessageText:
	#
	# An I/O operation initiated by the registry failed unrecoverably. The registry could not read in, or write out, or flush, one of the files that contain the system's image of the registry.
	#
	ERROR_REGISTRY_IO_FAILED = 1016 
	#
	# MessageId: ERROR_NOT_REGISTRY_FILE
	#
	# MessageText:
	#
	# The system has attempted to load or restore a file into the registry, but the specified file is not in a registry file format.
	#
	ERROR_NOT_REGISTRY_FILE = 1017 
	#
	# MessageId: ERROR_KEY_DELETED
	#
	# MessageText:
	#
	# Illegal operation attempted on a registry key that has been marked for deletion.
	#
	ERROR_KEY_DELETED = 1018 
	#
	# MessageId: ERROR_NO_LOG_SPACE
	#
	# MessageText:
	#
	# System could not allocate the required space in a registry log.
	#
	ERROR_NO_LOG_SPACE = 1019 
	#
	# MessageId: ERROR_KEY_HAS_CHILDREN
	#
	# MessageText:
	#
	# Cannot create a symbolic link in a registry key that already has subkeys or values.
	#
	ERROR_KEY_HAS_CHILDREN = 1020 
	#
	# MessageId: ERROR_CHILD_MUST_BE_VOLATILE
	#
	# MessageText:
	#
	# Cannot create a stable subkey under a volatile parent key.
	#
	ERROR_CHILD_MUST_BE_VOLATILE = 1021 
	#
	# MessageId: ERROR_NOTIFY_ENUM_DIR
	#
	# MessageText:
	#
	# A notify change request is being completed and the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.
	#
	ERROR_NOTIFY_ENUM_DIR = 1022 
	#
	# MessageId: ERROR_DEPENDENT_SERVICES_RUNNING
	#
	# MessageText:
	#
	# A stop control has been sent to a service that other running services are dependent on.
	#
	ERROR_DEPENDENT_SERVICES_RUNNING = 1051 
	#
	# MessageId: ERROR_INVALID_SERVICE_CONTROL
	#
	# MessageText:
	#
	# The requested control is not valid for this service.
	#
	ERROR_INVALID_SERVICE_CONTROL = 1052 
	#
	# MessageId: ERROR_SERVICE_REQUEST_TIMEOUT
	#
	# MessageText:
	#
	# The service did not respond to the start or control request in a timely fashion.
	#
	ERROR_SERVICE_REQUEST_TIMEOUT = 1053 
	#
	# MessageId: ERROR_SERVICE_NO_THREAD
	#
	# MessageText:
	#
	# A thread could not be created for the service.
	#
	ERROR_SERVICE_NO_THREAD = 1054 
	#
	# MessageId: ERROR_SERVICE_DATABASE_LOCKED
	#
	# MessageText:
	#
	# The service database is locked.
	#
	ERROR_SERVICE_DATABASE_LOCKED = 1055 
	#
	# MessageId: ERROR_SERVICE_ALREADY_RUNNING
	#
	# MessageText:
	#
	# An instance of the service is already running.
	#
	ERROR_SERVICE_ALREADY_RUNNING = 1056 
	#
	# MessageId: ERROR_INVALID_SERVICE_ACCOUNT
	#
	# MessageText:
	#
	# The account name is invalid or does not exist, or the password is invalid for the account name specified.
	#
	ERROR_INVALID_SERVICE_ACCOUNT = 1057 
	#
	# MessageId: ERROR_SERVICE_DISABLED
	#
	# MessageText:
	#
	# The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.
	#
	ERROR_SERVICE_DISABLED = 1058 
	#
	# MessageId: ERROR_CIRCULAR_DEPENDENCY
	#
	# MessageText:
	#
	# Circular service dependency was specified.
	#
	ERROR_CIRCULAR_DEPENDENCY = 1059 
	#
	# MessageId: ERROR_SERVICE_DOES_NOT_EXIST
	#
	# MessageText:
	#
	# The specified service does not exist as an installed service.
	#
	ERROR_SERVICE_DOES_NOT_EXIST = 1060 
	#
	# MessageId: ERROR_SERVICE_CANNOT_ACCEPT_CTRL
	#
	# MessageText:
	#
	# The service cannot accept control messages at this time.
	#
	ERROR_SERVICE_CANNOT_ACCEPT_CTRL = 1061 
	#
	# MessageId: ERROR_SERVICE_NOT_ACTIVE
	#
	# MessageText:
	#
	# The service has not been started.
	#
	ERROR_SERVICE_NOT_ACTIVE = 1062 
	#
	# MessageId: ERROR_FAILED_SERVICE_CONTROLLER_CONNECT
	#
	# MessageText:
	#
	# The service process could not connect to the service controller.
	#
	ERROR_FAILED_SERVICE_CONTROLLER_CONNECT = 1063 
	#
	# MessageId: ERROR_EXCEPTION_IN_SERVICE
	#
	# MessageText:
	#
	# An exception occurred in the service when handling the control request.
	#
	ERROR_EXCEPTION_IN_SERVICE = 1064 
	#
	# MessageId: ERROR_DATABASE_DOES_NOT_EXIST
	#
	# MessageText:
	#
	# The database specified does not exist.
	#
	ERROR_DATABASE_DOES_NOT_EXIST = 1065 
	#
	# MessageId: ERROR_SERVICE_SPECIFIC_ERROR
	#
	# MessageText:
	#
	# The service has returned a service-specific error code.
	#
	ERROR_SERVICE_SPECIFIC_ERROR = 1066 
	#
	# MessageId: ERROR_PROCESS_ABORTED
	#
	# MessageText:
	#
	# The process terminated unexpectedly.
	#
	ERROR_PROCESS_ABORTED = 1067 
	#
	# MessageId: ERROR_SERVICE_DEPENDENCY_FAIL
	#
	# MessageText:
	#
	# The dependency service or group failed to start.
	#
	ERROR_SERVICE_DEPENDENCY_FAIL = 1068 
	#
	# MessageId: ERROR_SERVICE_LOGON_FAILED
	#
	# MessageText:
	#
	# The service did not start due to a logon failure.
	#
	ERROR_SERVICE_LOGON_FAILED = 1069 
	#
	# MessageId: ERROR_SERVICE_START_HANG
	#
	# MessageText:
	#
	# After starting, the service hung in a start-pending state.
	#
	ERROR_SERVICE_START_HANG = 1070 
	#
	# MessageId: ERROR_INVALID_SERVICE_LOCK
	#
	# MessageText:
	#
	# The specified service database lock is invalid.
	#
	ERROR_INVALID_SERVICE_LOCK = 1071 
	#
	# MessageId: ERROR_SERVICE_MARKED_FOR_DELETE
	#
	# MessageText:
	#
	# The specified service has been marked for deletion.
	#
	ERROR_SERVICE_MARKED_FOR_DELETE = 1072 
	#
	# MessageId: ERROR_SERVICE_EXISTS
	#
	# MessageText:
	#
	# The specified service already exists.
	#
	ERROR_SERVICE_EXISTS = 1073 
	#
	# MessageId: ERROR_ALREADY_RUNNING_LKG
	#
	# MessageText:
	#
	# The system is currently running with the last-known-good configuration.
	#
	ERROR_ALREADY_RUNNING_LKG = 1074 
	#
	# MessageId: ERROR_SERVICE_DEPENDENCY_DELETED
	#
	# MessageText:
	#
	# The dependency service does not exist or has been marked for deletion.
	#
	ERROR_SERVICE_DEPENDENCY_DELETED = 1075 
	#
	# MessageId: ERROR_BOOT_ALREADY_ACCEPTED
	#
	# MessageText:
	#
	# The current boot has already been accepted for use as the last-known-good control set.
	#
	ERROR_BOOT_ALREADY_ACCEPTED = 1076 
	#
	# MessageId: ERROR_SERVICE_NEVER_STARTED
	#
	# MessageText:
	#
	# No attempts to start the service have been made since the last boot.
	#
	ERROR_SERVICE_NEVER_STARTED = 1077 
	#
	# MessageId: ERROR_DUPLICATE_SERVICE_NAME
	#
	# MessageText:
	#
	# The name is already in use as either a service name or a service display name.
	#
	ERROR_DUPLICATE_SERVICE_NAME = 1078 
	#
	# MessageId: ERROR_DIFFERENT_SERVICE_ACCOUNT
	#
	# MessageText:
	#
	# The account specified for this service is different from the account specified for other services running in the same process.
	#
	ERROR_DIFFERENT_SERVICE_ACCOUNT = 1079 
	#
	# MessageId: ERROR_CANNOT_DETECT_DRIVER_FAILURE
	#
	# MessageText:
	#
	# Failure actions can only be set for Win32 services, not for drivers.
	#
	ERROR_CANNOT_DETECT_DRIVER_FAILURE = 1080 
	#
	# MessageId: ERROR_CANNOT_DETECT_PROCESS_ABORT
	#
	# MessageText:
	#
	# This service runs in the same process as the service control manager.
	# Therefore, the service control manager cannot take action if this service's process terminates unexpectedly.
	#
	ERROR_CANNOT_DETECT_PROCESS_ABORT = 1081 
	#
	# MessageId: ERROR_NO_RECOVERY_PROGRAM
	#
	# MessageText:
	#
	# No recovery program has been configured for this service.
	#
	ERROR_NO_RECOVERY_PROGRAM = 1082 
	#
	# MessageId: ERROR_SERVICE_NOT_IN_EXE
	#
	# MessageText:
	#
	# The executable program that this service is configured to run in does not implement the service.
	#
	ERROR_SERVICE_NOT_IN_EXE = 1083 
	#
	# MessageId: ERROR_NOT_SAFEBOOT_SERVICE
	#
	# MessageText:
	#
	# This service cannot be started in Safe Mode
	#
	ERROR_NOT_SAFEBOOT_SERVICE = 1084 
	#
	# MessageId: ERROR_END_OF_MEDIA
	#
	# MessageText:
	#
	# The physical end of the tape has been reached.
	#
	ERROR_END_OF_MEDIA = 1100 
	#
	# MessageId: ERROR_FILEMARK_DETECTED
	#
	# MessageText:
	#
	# A tape access reached a filemark.
	#
	ERROR_FILEMARK_DETECTED = 1101 
	#
	# MessageId: ERROR_BEGINNING_OF_MEDIA
	#
	# MessageText:
	#
	# The beginning of the tape or a partition was encountered.
	#
	ERROR_BEGINNING_OF_MEDIA = 1102 
	#
	# MessageId: ERROR_SETMARK_DETECTED
	#
	# MessageText:
	#
	# A tape access reached the end of a set of files.
	#
	ERROR_SETMARK_DETECTED = 1103 
	#
	# MessageId: ERROR_NO_DATA_DETECTED
	#
	# MessageText:
	#
	# No more data is on the tape.
	#
	ERROR_NO_DATA_DETECTED = 1104 
	#
	# MessageId: ERROR_PARTITION_FAILURE
	#
	# MessageText:
	#
	# Tape could not be partitioned.
	#
	ERROR_PARTITION_FAILURE = 1105 
	#
	# MessageId: ERROR_INVALID_BLOCK_LENGTH
	#
	# MessageText:
	#
	# When accessing a new tape of a multivolume partition, the current block size is incorrect.
	#
	ERROR_INVALID_BLOCK_LENGTH = 1106 
	#
	# MessageId: ERROR_DEVICE_NOT_PARTITIONED
	#
	# MessageText:
	#
	# Tape partition information could not be found when loading a tape.
	#
	ERROR_DEVICE_NOT_PARTITIONED = 1107 
	#
	# MessageId: ERROR_UNABLE_TO_LOCK_MEDIA
	#
	# MessageText:
	#
	# Unable to lock the media eject mechanism.
	#
	ERROR_UNABLE_TO_LOCK_MEDIA = 1108 
	#
	# MessageId: ERROR_UNABLE_TO_UNLOAD_MEDIA
	#
	# MessageText:
	#
	# Unable to unload the media.
	#
	ERROR_UNABLE_TO_UNLOAD_MEDIA = 1109 
	#
	# MessageId: ERROR_MEDIA_CHANGED
	#
	# MessageText:
	#
	# The media in the drive may have changed.
	#
	ERROR_MEDIA_CHANGED = 1110 
	#
	# MessageId: ERROR_BUS_RESET
	#
	# MessageText:
	#
	# The I/O bus was reset.
	#
	ERROR_BUS_RESET = 1111 
	#
	# MessageId: ERROR_NO_MEDIA_IN_DRIVE
	#
	# MessageText:
	#
	# No media in drive.
	#
	ERROR_NO_MEDIA_IN_DRIVE = 1112 
	#
	# MessageId: ERROR_NO_UNICODE_TRANSLATION
	#
	# MessageText:
	#
	# No mapping for the Unicode character exists in the target multi-byte code page.
	#
	ERROR_NO_UNICODE_TRANSLATION = 1113 
	#
	# MessageId: ERROR_DLL_INIT_FAILED
	#
	# MessageText:
	#
	# A dynamic link library (DLL) initialization routine failed.
	#
	ERROR_DLL_INIT_FAILED = 1114 
	#
	# MessageId: ERROR_SHUTDOWN_IN_PROGRESS
	#
	# MessageText:
	#
	# A system shutdown is in progress.
	#
	ERROR_SHUTDOWN_IN_PROGRESS = 1115 
	#
	# MessageId: ERROR_NO_SHUTDOWN_IN_PROGRESS
	#
	# MessageText:
	#
	# Unable to abort the system shutdown because no shutdown was in progress.
	#
	ERROR_NO_SHUTDOWN_IN_PROGRESS = 1116 
	#
	# MessageId: ERROR_IO_DEVICE
	#
	# MessageText:
	#
	# The request could not be performed because of an I/O device error.
	#
	ERROR_IO_DEVICE = 1117 
	#
	# MessageId: ERROR_SERIAL_NO_DEVICE
	#
	# MessageText:
	#
	# No serial device was successfully initialized. The serial driver will unload.
	#
	ERROR_SERIAL_NO_DEVICE = 1118 
	#
	# MessageId: ERROR_IRQ_BUSY
	#
	# MessageText:
	#
	# Unable to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened.
	#
	ERROR_IRQ_BUSY = 1119 
	#
	# MessageId: ERROR_MORE_WRITES
	#
	# MessageText:
	#
	# A serial I/O operation was completed by another write to the serial port.
	# (The IOCTL_SERIAL_XOFF_COUNTER reached zero.)
	#
	ERROR_MORE_WRITES = 1120 
	#
	# MessageId: ERROR_COUNTER_TIMEOUT
	#
	# MessageText:
	#
	# A serial I/O operation completed because the timeout period expired.
	# (The IOCTL_SERIAL_XOFF_COUNTER did not reach zero.)
	#
	ERROR_COUNTER_TIMEOUT = 1121 
	#
	# MessageId: ERROR_FLOPPY_ID_MARK_NOT_FOUND
	#
	# MessageText:
	#
	# No ID address mark was found on the floppy disk.
	#
	ERROR_FLOPPY_ID_MARK_NOT_FOUND = 1122 
	#
	# MessageId: ERROR_FLOPPY_WRONG_CYLINDER
	#
	# MessageText:
	#
	# Mismatch between the floppy disk sector ID field and the floppy disk controller track address.
	#
	ERROR_FLOPPY_WRONG_CYLINDER = 1123 
	#
	# MessageId: ERROR_FLOPPY_UNKNOWN_ERROR
	#
	# MessageText:
	#
	# The floppy disk controller reported an error that is not recognized by the floppy disk driver.
	#
	ERROR_FLOPPY_UNKNOWN_ERROR = 1124 
	#
	# MessageId: ERROR_FLOPPY_BAD_REGISTERS
	#
	# MessageText:
	#
	# The floppy disk controller returned inconsistent results in its registers.
	#
	ERROR_FLOPPY_BAD_REGISTERS = 1125 
	#
	# MessageId: ERROR_DISK_RECALIBRATE_FAILED
	#
	# MessageText:
	#
	# While accessing the hard disk, a recalibrate operation failed, even after retries.
	#
	ERROR_DISK_RECALIBRATE_FAILED = 1126 
	#
	# MessageId: ERROR_DISK_OPERATION_FAILED
	#
	# MessageText:
	#
	# While accessing the hard disk, a disk operation failed even after retries.
	#
	ERROR_DISK_OPERATION_FAILED = 1127 
	#
	# MessageId: ERROR_DISK_RESET_FAILED
	#
	# MessageText:
	#
	# While accessing the hard disk, a disk controller reset was needed, but even that failed.
	#
	ERROR_DISK_RESET_FAILED = 1128 
	#
	# MessageId: ERROR_EOM_OVERFLOW
	#
	# MessageText:
	#
	# Physical end of tape encountered.
	#
	ERROR_EOM_OVERFLOW = 1129 
	#
	# MessageId: ERROR_NOT_ENOUGH_SERVER_MEMORY
	#
	# MessageText:
	#
	# Not enough server memory resources are available to process this command.
	#
	ERROR_NOT_ENOUGH_SERVER_MEMORY = 1130 
	#
	# MessageId: ERROR_POSSIBLE_DEADLOCK
	#
	# MessageText:
	#
	# A potential deadlock condition has been detected.
	#
	ERROR_POSSIBLE_DEADLOCK = 1131 
	#
	# MessageId: ERROR_MAPPED_ALIGNMENT
	#
	# MessageText:
	#
	# The base address or the file offset specified does not have the proper alignment.
	#
	ERROR_MAPPED_ALIGNMENT = 1132 
	#
	# MessageId: ERROR_SET_POWER_STATE_VETOED
	#
	# MessageText:
	#
	# An attempt to change the system power state was vetoed by another application or driver.
	#
	ERROR_SET_POWER_STATE_VETOED = 1140 
	#
	# MessageId: ERROR_SET_POWER_STATE_FAILED
	#
	# MessageText:
	#
	# The system BIOS failed an attempt to change the system power state.
	#
	ERROR_SET_POWER_STATE_FAILED = 1141 
	#
	# MessageId: ERROR_TOO_MANY_LINKS
	#
	# MessageText:
	#
	# An attempt was made to create more links on a file than the file system supports.
	#
	ERROR_TOO_MANY_LINKS = 1142 
	#
	# MessageId: ERROR_OLD_WIN_VERSION
	#
	# MessageText:
	#
	# The specified program requires a newer version of Windows.
	#
	ERROR_OLD_WIN_VERSION = 1150 
	#
	# MessageId: ERROR_APP_WRONG_OS
	#
	# MessageText:
	#
	# The specified program is not a Windows or MS-DOS program.
	#
	ERROR_APP_WRONG_OS = 1151 
	#
	# MessageId: ERROR_SINGLE_INSTANCE_APP
	#
	# MessageText:
	#
	# Cannot start more than one instance of the specified program.
	#
	ERROR_SINGLE_INSTANCE_APP = 1152 
	#
	# MessageId: ERROR_RMODE_APP
	#
	# MessageText:
	#
	# The specified program was written for an earlier version of Windows.
	#
	ERROR_RMODE_APP = 1153 
	#
	# MessageId: ERROR_INVALID_DLL
	#
	# MessageText:
	#
	# One of the library files needed to run this application is damaged.
	#
	ERROR_INVALID_DLL = 1154 
	#
	# MessageId: ERROR_NO_ASSOCIATION
	#
	# MessageText:
	#
	# No application is associated with the specified file for this operation.
	#
	ERROR_NO_ASSOCIATION = 1155 
	#
	# MessageId: ERROR_DDE_FAIL
	#
	# MessageText:
	#
	# An error occurred in sending the command to the application.
	#
	ERROR_DDE_FAIL = 1156 
	#
	# MessageId: ERROR_DLL_NOT_FOUND
	#
	# MessageText:
	#
	# One of the library files needed to run this application cannot be found.
	#
	ERROR_DLL_NOT_FOUND = 1157 
	#
	# MessageId: ERROR_NO_MORE_USER_HANDLES
	#
	# MessageText:
	#
	# The current process has used all of its system allowance of handles for Window Manager objects.
	#
	ERROR_NO_MORE_USER_HANDLES = 1158 
	#
	# MessageId: ERROR_MESSAGE_SYNC_ONLY
	#
	# MessageText:
	#
	# The message can be used only with synchronous operations.
	#
	ERROR_MESSAGE_SYNC_ONLY = 1159 
	#
	# MessageId: ERROR_SOURCE_ELEMENT_EMPTY
	#
	# MessageText:
	#
	# The indicated source element has no media.
	#
	ERROR_SOURCE_ELEMENT_EMPTY = 1160 
	#
	# MessageId: ERROR_DESTINATION_ELEMENT_FULL
	#
	# MessageText:
	#
	# The indicated destination element already contains media.
	#
	ERROR_DESTINATION_ELEMENT_FULL = 1161 
	#
	# MessageId: ERROR_ILLEGAL_ELEMENT_ADDRESS
	#
	# MessageText:
	#
	# The indicated element does not exist.
	#
	ERROR_ILLEGAL_ELEMENT_ADDRESS = 1162 
	#
	# MessageId: ERROR_MAGAZINE_NOT_PRESENT
	#
	# MessageText:
	#
	# The indicated element is part of a magazine that is not present.
	#
	ERROR_MAGAZINE_NOT_PRESENT = 1163 
	#
	# MessageId: ERROR_DEVICE_REINITIALIZATION_NEEDED
	#
	# MessageText:
	#
	# The indicated device requires reinitialization due to hardware errors.
	#
	ERROR_DEVICE_REINITIALIZATION_NEEDED = 1164 # dderror
	#
	# MessageId: ERROR_DEVICE_REQUIRES_CLEANING
	#
	# MessageText:
	#
	# The device has indicated that cleaning is required before further operations are attempted.
	#
	ERROR_DEVICE_REQUIRES_CLEANING = 1165 
	#
	# MessageId: ERROR_DEVICE_DOOR_OPEN
	#
	# MessageText:
	#
	# The device has indicated that its door is open.
	#
	ERROR_DEVICE_DOOR_OPEN = 1166 
	#
	# MessageId: ERROR_DEVICE_NOT_CONNECTED
	#
	# MessageText:
	#
	# The device is not connected.
	#
	ERROR_DEVICE_NOT_CONNECTED = 1167 
	#
	# MessageId: ERROR_NOT_FOUND
	#
	# MessageText:
	#
	# Element not found.
	#
	ERROR_NOT_FOUND = 1168 
	#
	# MessageId: ERROR_NO_MATCH
	#
	# MessageText:
	#
	# There was no match for the specified key in the index.
	#
	ERROR_NO_MATCH = 1169 
	#
	# MessageId: ERROR_SET_NOT_FOUND
	#
	# MessageText:
	#
	# The property set specified does not exist on the object.
	#
	ERROR_SET_NOT_FOUND = 1170 
	#
	# MessageId: ERROR_POINT_NOT_FOUND
	#
	# MessageText:
	#
	# The point passed to GetMouseMovePoints is not in the buffer.
	#
	ERROR_POINT_NOT_FOUND = 1171 
	#
	# MessageId: ERROR_NO_TRACKING_SERVICE
	#
	# MessageText:
	#
	# The tracking (workstation) service is not running.
	#
	ERROR_NO_TRACKING_SERVICE = 1172 
	#
	# MessageId: ERROR_NO_VOLUME_ID
	#
	# MessageText:
	#
	# The Volume ID could not be found.
	#
	ERROR_NO_VOLUME_ID = 1173 
	#
	# MessageId: ERROR_UNABLE_TO_REMOVE_REPLACED
	#
	# MessageText:
	#
	# Unable to remove the file to be replaced.
	#
	ERROR_UNABLE_TO_REMOVE_REPLACED = 1175 
	#
	# MessageId: ERROR_UNABLE_TO_MOVE_REPLACEMENT
	#
	# MessageText:
	#
	# Unable to move the replacement file to the file to be replaced. The file to be replaced has retained its original name.
	#
	ERROR_UNABLE_TO_MOVE_REPLACEMENT = 1176 
	#
	# MessageId: ERROR_UNABLE_TO_MOVE_REPLACEMENT_2
	#
	# MessageText:
	#
	# Unable to move the replacement file to the file to be replaced. The file to be replaced has been renamed using the backup name.
	#
	ERROR_UNABLE_TO_MOVE_REPLACEMENT_2 = 1177 
	#
	# MessageId: ERROR_JOURNAL_DELETE_IN_PROGRESS
	#
	# MessageText:
	#
	# The volume change journal is being deleted.
	#
	ERROR_JOURNAL_DELETE_IN_PROGRESS = 1178 
	#
	# MessageId: ERROR_JOURNAL_NOT_ACTIVE
	#
	# MessageText:
	#
	# The volume change journal is not active.
	#
	ERROR_JOURNAL_NOT_ACTIVE = 1179 
	#
	# MessageId: ERROR_POTENTIAL_FILE_FOUND
	#
	# MessageText:
	#
	# A file was found, but it may not be the correct file.
	#
	ERROR_POTENTIAL_FILE_FOUND = 1180 
	#
	# MessageId: ERROR_JOURNAL_ENTRY_DELETED
	#
	# MessageText:
	#
	# The journal entry has been deleted from the journal.
	#
	ERROR_JOURNAL_ENTRY_DELETED = 1181 
	#
	# MessageId: ERROR_SHUTDOWN_IS_SCHEDULED
	#
	# MessageText:
	#
	# A system shutdown has already been scheduled.
	#
	ERROR_SHUTDOWN_IS_SCHEDULED = 1190 
	#
	# MessageId: ERROR_SHUTDOWN_USERS_LOGGED_ON
	#
	# MessageText:
	#
	# The system shutdown cannot be initiated because there are other users logged on to the computer.
	#
	ERROR_SHUTDOWN_USERS_LOGGED_ON = 1191 
	#
	# MessageId: ERROR_BAD_DEVICE
	#
	# MessageText:
	#
	# The specified device name is invalid.
	#
	ERROR_BAD_DEVICE = 1200 
	#
	# MessageId: ERROR_CONNECTION_UNAVAIL
	#
	# MessageText:
	#
	# The device is not currently connected but it is a remembered connection.
	#
	ERROR_CONNECTION_UNAVAIL = 1201 
	#
	# MessageId: ERROR_DEVICE_ALREADY_REMEMBERED
	#
	# MessageText:
	#
	# The local device name has a remembered connection to another network resource.
	#
	ERROR_DEVICE_ALREADY_REMEMBERED = 1202 
	#
	# MessageId: ERROR_NO_NET_OR_BAD_PATH
	#
	# MessageText:
	#
	# The network path was either typed incorrectly, does not exist, or the network provider is not currently available. Please try retyping the path or contact your network administrator.
	#
	ERROR_NO_NET_OR_BAD_PATH = 1203 
	#
	# MessageId: ERROR_BAD_PROVIDER
	#
	# MessageText:
	#
	# The specified network provider name is invalid.
	#
	ERROR_BAD_PROVIDER = 1204 
	#
	# MessageId: ERROR_CANNOT_OPEN_PROFILE
	#
	# MessageText:
	#
	# Unable to open the network connection profile.
	#
	ERROR_CANNOT_OPEN_PROFILE = 1205 
	#
	# MessageId: ERROR_BAD_PROFILE
	#
	# MessageText:
	#
	# The network connection profile is corrupted.
	#
	ERROR_BAD_PROFILE = 1206 
	#
	# MessageId: ERROR_NOT_CONTAINER
	#
	# MessageText:
	#
	# Cannot enumerate a noncontainer.
	#
	ERROR_NOT_CONTAINER = 1207 
	#
	# MessageId: ERROR_EXTENDED_ERROR
	#
	# MessageText:
	#
	# An extended error has occurred.
	#
	ERROR_EXTENDED_ERROR = 1208 
	#
	# MessageId: ERROR_INVALID_GROUPNAME
	#
	# MessageText:
	#
	# The format of the specified group name is invalid.
	#
	ERROR_INVALID_GROUPNAME = 1209 
	#
	# MessageId: ERROR_INVALID_COMPUTERNAME
	#
	# MessageText:
	#
	# The format of the specified computer name is invalid.
	#
	ERROR_INVALID_COMPUTERNAME = 1210 
	#
	# MessageId: ERROR_INVALID_EVENTNAME
	#
	# MessageText:
	#
	# The format of the specified event name is invalid.
	#
	ERROR_INVALID_EVENTNAME = 1211 
	#
	# MessageId: ERROR_INVALID_DOMAINNAME
	#
	# MessageText:
	#
	# The format of the specified domain name is invalid.
	#
	ERROR_INVALID_DOMAINNAME = 1212 
	#
	# MessageId: ERROR_INVALID_SERVICENAME
	#
	# MessageText:
	#
	# The format of the specified service name is invalid.
	#
	ERROR_INVALID_SERVICENAME = 1213 
	#
	# MessageId: ERROR_INVALID_NETNAME
	#
	# MessageText:
	#
	# The format of the specified network name is invalid.
	#
	ERROR_INVALID_NETNAME = 1214 
	#
	# MessageId: ERROR_INVALID_SHARENAME
	#
	# MessageText:
	#
	# The format of the specified share name is invalid.
	#
	ERROR_INVALID_SHARENAME = 1215 
	#
	# MessageId: ERROR_INVALID_PASSWORDNAME
	#
	# MessageText:
	#
	# The format of the specified password is invalid.
	#
	ERROR_INVALID_PASSWORDNAME = 1216 
	#
	# MessageId: ERROR_INVALID_MESSAGENAME
	#
	# MessageText:
	#
	# The format of the specified message name is invalid.
	#
	ERROR_INVALID_MESSAGENAME = 1217 
	#
	# MessageId: ERROR_INVALID_MESSAGEDEST
	#
	# MessageText:
	#
	# The format of the specified message destination is invalid.
	#
	ERROR_INVALID_MESSAGEDEST = 1218 
	#
	# MessageId: ERROR_SESSION_CREDENTIAL_CONFLICT
	#
	# MessageText:
	#
	# Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.
	#
	ERROR_SESSION_CREDENTIAL_CONFLICT = 1219 
	#
	# MessageId: ERROR_REMOTE_SESSION_LIMIT_EXCEEDED
	#
	# MessageText:
	#
	# An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.
	#
	ERROR_REMOTE_SESSION_LIMIT_EXCEEDED = 1220 
	#
	# MessageId: ERROR_DUP_DOMAINNAME
	#
	# MessageText:
	#
	# The workgroup or domain name is already in use by another computer on the network.
	#
	ERROR_DUP_DOMAINNAME = 1221 
	#
	# MessageId: ERROR_NO_NETWORK
	#
	# MessageText:
	#
	# The network is not present or not started.
	#
	ERROR_NO_NETWORK = 1222 
	#
	# MessageId: ERROR_CANCELLED
	#
	# MessageText:
	#
	# The operation was canceled by the user.
	#
	ERROR_CANCELLED = 1223 
	#
	# MessageId: ERROR_USER_MAPPED_FILE
	#
	# MessageText:
	#
	# The requested operation cannot be performed on a file with a user-mapped section open.
	#
	ERROR_USER_MAPPED_FILE = 1224 
	#
	# MessageId: ERROR_CONNECTION_REFUSED
	#
	# MessageText:
	#
	# The remote computer refused the network connection.
	#
	ERROR_CONNECTION_REFUSED = 1225 
	#
	# MessageId: ERROR_GRACEFUL_DISCONNECT
	#
	# MessageText:
	#
	# The network connection was gracefully closed.
	#
	ERROR_GRACEFUL_DISCONNECT = 1226 
	#
	# MessageId: ERROR_ADDRESS_ALREADY_ASSOCIATED
	#
	# MessageText:
	#
	# The network transport endpoint already has an address associated with it.
	#
	ERROR_ADDRESS_ALREADY_ASSOCIATED = 1227 
	#
	# MessageId: ERROR_ADDRESS_NOT_ASSOCIATED
	#
	# MessageText:
	#
	# An address has not yet been associated with the network endpoint.
	#
	ERROR_ADDRESS_NOT_ASSOCIATED = 1228 
	#
	# MessageId: ERROR_CONNECTION_INVALID
	#
	# MessageText:
	#
	# An operation was attempted on a nonexistent network connection.
	#
	ERROR_CONNECTION_INVALID = 1229 
	#
	# MessageId: ERROR_CONNECTION_ACTIVE
	#
	# MessageText:
	#
	# An invalid operation was attempted on an active network connection.
	#
	ERROR_CONNECTION_ACTIVE = 1230 
	#
	# MessageId: ERROR_NETWORK_UNREACHABLE
	#
	# MessageText:
	#
	# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
	#
	ERROR_NETWORK_UNREACHABLE = 1231 
	#
	# MessageId: ERROR_HOST_UNREACHABLE
	#
	# MessageText:
	#
	# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
	#
	ERROR_HOST_UNREACHABLE = 1232 
	#
	# MessageId: ERROR_PROTOCOL_UNREACHABLE
	#
	# MessageText:
	#
	# The network location cannot be reached. For information about network troubleshooting, see Windows Help.
	#
	ERROR_PROTOCOL_UNREACHABLE = 1233 
	#
	# MessageId: ERROR_PORT_UNREACHABLE
	#
	# MessageText:
	#
	# No service is operating at the destination network endpoint on the remote system.
	#
	ERROR_PORT_UNREACHABLE = 1234 
	#
	# MessageId: ERROR_REQUEST_ABORTED
	#
	# MessageText:
	#
	# The request was aborted.
	#
	ERROR_REQUEST_ABORTED = 1235 
	#
	# MessageId: ERROR_CONNECTION_ABORTED
	#
	# MessageText:
	#
	# The network connection was aborted by the local system.
	#
	ERROR_CONNECTION_ABORTED = 1236 
	#
	# MessageId: ERROR_RETRY
	#
	# MessageText:
	#
	# The operation could not be completed. A retry should be performed.
	#
	ERROR_RETRY = 1237 
	#
	# MessageId: ERROR_CONNECTION_COUNT_LIMIT
	#
	# MessageText:
	#
	# A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.
	#
	ERROR_CONNECTION_COUNT_LIMIT = 1238 
	#
	# MessageId: ERROR_LOGIN_TIME_RESTRICTION
	#
	# MessageText:
	#
	# Attempting to log in during an unauthorized time of day for this account.
	#
	ERROR_LOGIN_TIME_RESTRICTION = 1239 
	#
	# MessageId: ERROR_LOGIN_WKSTA_RESTRICTION
	#
	# MessageText:
	#
	# The account is not authorized to log in from this station.
	#
	ERROR_LOGIN_WKSTA_RESTRICTION = 1240 
	#
	# MessageId: ERROR_INCORRECT_ADDRESS
	#
	# MessageText:
	#
	# The network address could not be used for the operation requested.
	#
	ERROR_INCORRECT_ADDRESS = 1241 
	#
	# MessageId: ERROR_ALREADY_REGISTERED
	#
	# MessageText:
	#
	# The service is already registered.
	#
	ERROR_ALREADY_REGISTERED = 1242 
	#
	# MessageId: ERROR_SERVICE_NOT_FOUND
	#
	# MessageText:
	#
	# The specified service does not exist.
	#
	ERROR_SERVICE_NOT_FOUND = 1243 
	#
	# MessageId: ERROR_NOT_AUTHENTICATED
	#
	# MessageText:
	#
	# The operation being requested was not performed because the user has not been authenticated.
	#
	ERROR_NOT_AUTHENTICATED = 1244 
	#
	# MessageId: ERROR_NOT_LOGGED_ON
	#
	# MessageText:
	#
	# The operation being requested was not performed because the user has not logged on to the network. The specified service does not exist.
	#
	ERROR_NOT_LOGGED_ON = 1245 
	#
	# MessageId: ERROR_CONTINUE
	#
	# MessageText:
	#
	# Continue with work in progress.
	#
	ERROR_CONTINUE = 1246 # dderror
	#
	# MessageId: ERROR_ALREADY_INITIALIZED
	#
	# MessageText:
	#
	# An attempt was made to perform an initialization operation when initialization has already been completed.
	#
	ERROR_ALREADY_INITIALIZED = 1247 
	#
	# MessageId: ERROR_NO_MORE_DEVICES
	#
	# MessageText:
	#
	# No more local devices.
	#
	ERROR_NO_MORE_DEVICES = 1248 # dderror
	#
	# MessageId: ERROR_NO_SUCH_SITE
	#
	# MessageText:
	#
	# The specified site does not exist.
	#
	ERROR_NO_SUCH_SITE = 1249 
	#
	# MessageId: ERROR_DOMAIN_CONTROLLER_EXISTS
	#
	# MessageText:
	#
	# A domain controller with the specified name already exists.
	#
	ERROR_DOMAIN_CONTROLLER_EXISTS = 1250 
	#
	# MessageId: ERROR_ONLY_IF_CONNECTED
	#
	# MessageText:
	#
	# This operation is supported only when you are connected to the server.
	#
	ERROR_ONLY_IF_CONNECTED = 1251 
	#
	# MessageId: ERROR_OVERRIDE_NOCHANGES
	#
	# MessageText:
	#
	# The group policy framework should call the extension even if there are no changes.
	#
	ERROR_OVERRIDE_NOCHANGES = 1252 
	#
	# MessageId: ERROR_BAD_USER_PROFILE
	#
	# MessageText:
	#
	# The specified user does not have a valid profile.
	#
	ERROR_BAD_USER_PROFILE = 1253 
	#
	# MessageId: ERROR_NOT_SUPPORTED_ON_SBS
	#
	# MessageText:
	#
	# This operation is not supported on a computer running Windows Server 2003 for Small Business Server
	#
	ERROR_NOT_SUPPORTED_ON_SBS = 1254 
	#
	# MessageId: ERROR_SERVER_SHUTDOWN_IN_PROGRESS
	#
	# MessageText:
	#
	# The server machine is shutting down.
	#
	ERROR_SERVER_SHUTDOWN_IN_PROGRESS = 1255 
	#
	# MessageId: ERROR_HOST_DOWN
	#
	# MessageText:
	#
	# The remote system is not available. For information about network troubleshooting, see Windows Help.
	#
	ERROR_HOST_DOWN = 1256 
	#
	# MessageId: ERROR_NON_ACCOUNT_SID
	#
	# MessageText:
	#
	# The security identifier provided is not from an account domain.
	#
	ERROR_NON_ACCOUNT_SID = 1257 
	#
	# MessageId: ERROR_NON_DOMAIN_SID
	#
	# MessageText:
	#
	# The security identifier provided does not have a domain component.
	#
	ERROR_NON_DOMAIN_SID = 1258 
	#
	# MessageId: ERROR_APPHELP_BLOCK
	#
	# MessageText:
	#
	# AppHelp dialog canceled thus preventing the application from starting.
	#
	ERROR_APPHELP_BLOCK = 1259 
	#
	# MessageId: ERROR_ACCESS_DISABLED_BY_POLICY
	#
	# MessageText:
	#
	# This program is blocked by group policy. For more information, contact your system administrator.
	#
	ERROR_ACCESS_DISABLED_BY_POLICY = 1260 
	#
	# MessageId: ERROR_REG_NAT_CONSUMPTION
	#
	# MessageText:
	#
	# A program attempt to use an invalid register value. Normally caused by an uninitialized register. This error is Itanium specific.
	#
	ERROR_REG_NAT_CONSUMPTION = 1261 
	#
	# MessageId: ERROR_CSCSHARE_OFFLINE
	#
	# MessageText:
	#
	# The share is currently offline or does not exist.
	#
	ERROR_CSCSHARE_OFFLINE = 1262 
	#
	# MessageId: ERROR_PKINIT_FAILURE
	#
	# MessageText:
	#
	# The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon. There is more information in the system event log.
	#
	ERROR_PKINIT_FAILURE = 1263 
	#
	# MessageId: ERROR_SMARTCARD_SUBSYSTEM_FAILURE
	#
	# MessageText:
	#
	# The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.
	#
	ERROR_SMARTCARD_SUBSYSTEM_FAILURE = 1264 
	#
	# MessageId: ERROR_DOWNGRADE_DETECTED
	#
	# MessageText:
	#
	# The system cannot contact a domain controller to service the authentication request. Please try again later.
	#
	ERROR_DOWNGRADE_DETECTED = 1265 
	#
	# Do not use ID's 1266 - 1270 as the symbolicNames have been moved to SEC_E_*
	#
	#
	# MessageId: ERROR_MACHINE_LOCKED
	#
	# MessageText:
	#
	# The machine is locked and cannot be shut down without the force option.
	#
	ERROR_MACHINE_LOCKED = 1271 
	#
	# MessageId: ERROR_SMB_GUEST_LOGON_BLOCKED
	#
	# MessageText:
	#
	# You can't access this shared folder because your organization's security policies block unauthenticated guest access. These policies help protect your PC from unsafe or malicious devices on the network.
	#
	ERROR_SMB_GUEST_LOGON_BLOCKED = 1272 
	#
	# MessageId: ERROR_CALLBACK_SUPPLIED_INVALID_DATA
	#
	# MessageText:
	#
	# An application-defined callback gave invalid data when called.
	#
	ERROR_CALLBACK_SUPPLIED_INVALID_DATA = 1273 
	#
	# MessageId: ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED
	#
	# MessageText:
	#
	# The group policy framework should call the extension in the synchronous foreground policy refresh.
	#
	ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED = 1274 
	#
	# MessageId: ERROR_DRIVER_BLOCKED
	#
	# MessageText:
	#
	# This driver has been blocked from loading
	#
	ERROR_DRIVER_BLOCKED = 1275 
	#
	# MessageId: ERROR_INVALID_IMPORT_OF_NON_DLL
	#
	# MessageText:
	#
	# A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.
	#
	ERROR_INVALID_IMPORT_OF_NON_DLL = 1276 
	#
	# MessageId: ERROR_ACCESS_DISABLED_WEBBLADE
	#
	# MessageText:
	#
	# Windows cannot open this program since it has been disabled.
	#
	ERROR_ACCESS_DISABLED_WEBBLADE = 1277 
	#
	# MessageId: ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER
	#
	# MessageText:
	#
	# Windows cannot open this program because the license enforcement system has been tampered with or become corrupted.
	#
	ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER = 1278 
	#
	# MessageId: ERROR_RECOVERY_FAILURE
	#
	# MessageText:
	#
	# A transaction recover failed.
	#
	ERROR_RECOVERY_FAILURE = 1279 
	#
	# MessageId: ERROR_ALREADY_FIBER
	#
	# MessageText:
	#
	# The current thread has already been converted to a fiber.
	#
	ERROR_ALREADY_FIBER = 1280 
	#
	# MessageId: ERROR_ALREADY_THREAD
	#
	# MessageText:
	#
	# The current thread has already been converted from a fiber.
	#
	ERROR_ALREADY_THREAD = 1281 
	#
	# MessageId: ERROR_STACK_BUFFER_OVERRUN
	#
	# MessageText:
	#
	# The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.
	#
	ERROR_STACK_BUFFER_OVERRUN = 1282 
	#
	# MessageId: ERROR_PARAMETER_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# Data present in one of the parameters is more than the function can operate on.
	#
	ERROR_PARAMETER_QUOTA_EXCEEDED = 1283 
	#
	# MessageId: ERROR_DEBUGGER_INACTIVE
	#
	# MessageText:
	#
	# An attempt to do an operation on a debug object failed because the object is in the process of being deleted.
	#
	ERROR_DEBUGGER_INACTIVE = 1284 
	#
	# MessageId: ERROR_DELAY_LOAD_FAILED
	#
	# MessageText:
	#
	# An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.
	#
	ERROR_DELAY_LOAD_FAILED = 1285 
	#
	# MessageId: ERROR_VDM_DISALLOWED
	#
	# MessageText:
	#
	# %1 is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.
	#
	ERROR_VDM_DISALLOWED = 1286 
	#
	# MessageId: ERROR_UNIDENTIFIED_ERROR
	#
	# MessageText:
	#
	# Insufficient information exists to identify the cause of failure.
	#
	ERROR_UNIDENTIFIED_ERROR = 1287 
	#
	# MessageId: ERROR_INVALID_CRUNTIME_PARAMETER
	#
	# MessageText:
	#
	# The parameter passed to a C runtime function is incorrect.
	#
	ERROR_INVALID_CRUNTIME_PARAMETER = 1288 
	#
	# MessageId: ERROR_BEYOND_VDL
	#
	# MessageText:
	#
	# The operation occurred beyond the valid data length of the file.
	#
	ERROR_BEYOND_VDL = 1289 
	#
	# MessageId: ERROR_INCOMPATIBLE_SERVICE_SID_TYPE
	#
	# MessageText:
	#
	# The service start failed since one or more services in the same process have an incompatible service SID type setting. A service with restricted service SID type can only coexist in the same process with other services with a restricted SID type. If the service SID type for this service was just configured, the hosting process must be restarted in order to start this service.
	#
	ERROR_INCOMPATIBLE_SERVICE_SID_TYPE = 1290 
	#
	# MessageId: ERROR_DRIVER_PROCESS_TERMINATED
	#
	# MessageText:
	#
	# The process hosting the driver for this device has been terminated.
	#
	ERROR_DRIVER_PROCESS_TERMINATED = 1291 
	#
	# MessageId: ERROR_IMPLEMENTATION_LIMIT
	#
	# MessageText:
	#
	# An operation attempted to exceed an implementation-defined limit.
	#
	ERROR_IMPLEMENTATION_LIMIT = 1292 
	#
	# MessageId: ERROR_PROCESS_IS_PROTECTED
	#
	# MessageText:
	#
	# Either the target process, or the target thread's containing process, is a protected process.
	#
	ERROR_PROCESS_IS_PROTECTED = 1293 
	#
	# MessageId: ERROR_SERVICE_NOTIFY_CLIENT_LAGGING
	#
	# MessageText:
	#
	# The service notification client is lagging too far behind the current state of services in the machine.
	#
	ERROR_SERVICE_NOTIFY_CLIENT_LAGGING = 1294 
	#
	# MessageId: ERROR_DISK_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# The requested file operation failed because the storage quota was exceeded.
	# To free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.
	#
	ERROR_DISK_QUOTA_EXCEEDED = 1295 
	#
	# MessageId: ERROR_CONTENT_BLOCKED
	#
	# MessageText:
	#
	# The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.
	#
	ERROR_CONTENT_BLOCKED = 1296 
	#
	# MessageId: ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE
	#
	# MessageText:
	#
	# A privilege that the service requires to function properly does not exist in the service account configuration.
	# You may use the Services Microsoft Management Console (MMC) snap-in (services.msc) and the Local Security Settings MMC snap-in (secpol.msc) to view the service configuration and the account configuration.
	#
	ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE = 1297 
	#
	# MessageId: ERROR_APP_HANG
	#
	# MessageText:
	#
	# A thread involved in this operation appears to be unresponsive.
	#
	ERROR_APP_HANG = 1298 
	#########################/
	#                                               #
	#             SECURITY Error codes              #
	#                                               #
	#                 1299 to 1399                  #
	#########################/
	#
	# MessageId: ERROR_INVALID_LABEL
	#
	# MessageText:
	#
	# Indicates a particular Security ID may not be assigned as the label of an object.
	#
	ERROR_INVALID_LABEL = 1299 
	#
	# MessageId: ERROR_NOT_ALL_ASSIGNED
	#
	# MessageText:
	#
	# Not all privileges or groups referenced are assigned to the caller.
	#
	ERROR_NOT_ALL_ASSIGNED = 1300 
	#
	# MessageId: ERROR_SOME_NOT_MAPPED
	#
	# MessageText:
	#
	# Some mapping between account names and security IDs was not done.
	#
	ERROR_SOME_NOT_MAPPED = 1301 
	#
	# MessageId: ERROR_NO_QUOTAS_FOR_ACCOUNT
	#
	# MessageText:
	#
	# No system quota limits are specifically set for this account.
	#
	ERROR_NO_QUOTAS_FOR_ACCOUNT = 1302 
	#
	# MessageId: ERROR_LOCAL_USER_SESSION_KEY
	#
	# MessageText:
	#
	# No encryption key is available. A well-known encryption key was returned.
	#
	ERROR_LOCAL_USER_SESSION_KEY = 1303 
	#
	# MessageId: ERROR_NULL_LM_PASSWORD
	#
	# MessageText:
	#
	# The password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a NULL string.
	#
	ERROR_NULL_LM_PASSWORD = 1304 
	#
	# MessageId: ERROR_UNKNOWN_REVISION
	#
	# MessageText:
	#
	# The revision level is unknown.
	#
	ERROR_UNKNOWN_REVISION = 1305 
	#
	# MessageId: ERROR_REVISION_MISMATCH
	#
	# MessageText:
	#
	# Indicates two revision levels are incompatible.
	#
	ERROR_REVISION_MISMATCH = 1306 
	#
	# MessageId: ERROR_INVALID_OWNER
	#
	# MessageText:
	#
	# This security ID may not be assigned as the owner of this object.
	#
	ERROR_INVALID_OWNER = 1307 
	#
	# MessageId: ERROR_INVALID_PRIMARY_GROUP
	#
	# MessageText:
	#
	# This security ID may not be assigned as the primary group of an object.
	#
	ERROR_INVALID_PRIMARY_GROUP = 1308 
	#
	# MessageId: ERROR_NO_IMPERSONATION_TOKEN
	#
	# MessageText:
	#
	# An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.
	#
	ERROR_NO_IMPERSONATION_TOKEN = 1309 
	#
	# MessageId: ERROR_CANT_DISABLE_MANDATORY
	#
	# MessageText:
	#
	# The group may not be disabled.
	#
	ERROR_CANT_DISABLE_MANDATORY = 1310 
	#
	# MessageId: ERROR_NO_LOGON_SERVERS
	#
	# MessageText:
	#
	# We can't sign you in with this credential because your domain isn't available. Make sure your device is connected to your organization's network and try again. If you previously signed in on this device with another credential, you can sign in with that credential.
	#
	ERROR_NO_LOGON_SERVERS = 1311 
	#
	# MessageId: ERROR_NO_SUCH_LOGON_SESSION
	#
	# MessageText:
	#
	# A specified logon session does not exist. It may already have been terminated.
	#
	ERROR_NO_SUCH_LOGON_SESSION = 1312 
	#
	# MessageId: ERROR_NO_SUCH_PRIVILEGE
	#
	# MessageText:
	#
	# A specified privilege does not exist.
	#
	ERROR_NO_SUCH_PRIVILEGE = 1313 
	#
	# MessageId: ERROR_PRIVILEGE_NOT_HELD
	#
	# MessageText:
	#
	# A required privilege is not held by the client.
	#
	ERROR_PRIVILEGE_NOT_HELD = 1314 
	#
	# MessageId: ERROR_INVALID_ACCOUNT_NAME
	#
	# MessageText:
	#
	# The name provided is not a properly formed account name.
	#
	ERROR_INVALID_ACCOUNT_NAME = 1315 
	#
	# MessageId: ERROR_USER_EXISTS
	#
	# MessageText:
	#
	# The specified account already exists.
	#
	ERROR_USER_EXISTS = 1316 
	#
	# MessageId: ERROR_NO_SUCH_USER
	#
	# MessageText:
	#
	# The specified account does not exist.
	#
	ERROR_NO_SUCH_USER = 1317 
	#
	# MessageId: ERROR_GROUP_EXISTS
	#
	# MessageText:
	#
	# The specified group already exists.
	#
	ERROR_GROUP_EXISTS = 1318 
	#
	# MessageId: ERROR_NO_SUCH_GROUP
	#
	# MessageText:
	#
	# The specified group does not exist.
	#
	ERROR_NO_SUCH_GROUP = 1319 
	#
	# MessageId: ERROR_MEMBER_IN_GROUP
	#
	# MessageText:
	#
	# Either the specified user account is already a member of the specified group, or the specified group cannot be deleted because it contains a member.
	#
	ERROR_MEMBER_IN_GROUP = 1320 
	#
	# MessageId: ERROR_MEMBER_NOT_IN_GROUP
	#
	# MessageText:
	#
	# The specified user account is not a member of the specified group account.
	#
	ERROR_MEMBER_NOT_IN_GROUP = 1321 
	#
	# MessageId: ERROR_LAST_ADMIN
	#
	# MessageText:
	#
	# This operation is disallowed as it could result in an administration account being disabled, deleted or unable to logon.
	#
	ERROR_LAST_ADMIN = 1322 
	#
	# MessageId: ERROR_WRONG_PASSWORD
	#
	# MessageText:
	#
	# Unable to update the password. The value provided as the current password is incorrect.
	#
	ERROR_WRONG_PASSWORD = 1323 
	#
	# MessageId: ERROR_ILL_FORMED_PASSWORD
	#
	# MessageText:
	#
	# Unable to update the password. The value provided for the new password contains values that are not allowed in passwords.
	#
	ERROR_ILL_FORMED_PASSWORD = 1324 
	#
	# MessageId: ERROR_PASSWORD_RESTRICTION
	#
	# MessageText:
	#
	# Unable to update the password. The value provided for the new password does not meet the length, complexity, or history requirements of the domain.
	#
	ERROR_PASSWORD_RESTRICTION = 1325 
	#
	# MessageId: ERROR_LOGON_FAILURE
	#
	# MessageText:
	#
	# The user name or password is incorrect.
	#
	ERROR_LOGON_FAILURE = 1326 
	#
	# MessageId: ERROR_ACCOUNT_RESTRICTION
	#
	# MessageText:
	#
	# Account restrictions are preventing this user from signing in. For example: blank passwords aren't allowed, sign-in times are limited, or a policy restriction has been enforced.
	#
	ERROR_ACCOUNT_RESTRICTION = 1327 
	#
	# MessageId: ERROR_INVALID_LOGON_HOURS
	#
	# MessageText:
	#
	# Your account has time restrictions that keep you from signing in right now.
	#
	ERROR_INVALID_LOGON_HOURS = 1328 
	#
	# MessageId: ERROR_INVALID_WORKSTATION
	#
	# MessageText:
	#
	# This user isn't allowed to sign in to this computer.
	#
	ERROR_INVALID_WORKSTATION = 1329 
	#
	# MessageId: ERROR_PASSWORD_EXPIRED
	#
	# MessageText:
	#
	# The password for this account has expired.
	#
	ERROR_PASSWORD_EXPIRED = 1330 
	#
	# MessageId: ERROR_ACCOUNT_DISABLED
	#
	# MessageText:
	#
	# This user can't sign in because this account is currently disabled.
	#
	ERROR_ACCOUNT_DISABLED = 1331 
	#
	# MessageId: ERROR_NONE_MAPPED
	#
	# MessageText:
	#
	# No mapping between account names and security IDs was done.
	#
	ERROR_NONE_MAPPED = 1332 
	#
	# MessageId: ERROR_TOO_MANY_LUIDS_REQUESTED
	#
	# MessageText:
	#
	# Too many local user identifiers (LUIDs) were requested at one time.
	#
	ERROR_TOO_MANY_LUIDS_REQUESTED = 1333 
	#
	# MessageId: ERROR_LUIDS_EXHAUSTED
	#
	# MessageText:
	#
	# No more local user identifiers (LUIDs) are available.
	#
	ERROR_LUIDS_EXHAUSTED = 1334 
	#
	# MessageId: ERROR_INVALID_SUB_AUTHORITY
	#
	# MessageText:
	#
	# The subauthority part of a security ID is invalid for this particular use.
	#
	ERROR_INVALID_SUB_AUTHORITY = 1335 
	#
	# MessageId: ERROR_INVALID_ACL
	#
	# MessageText:
	#
	# The access control list (ACL) structure is invalid.
	#
	ERROR_INVALID_ACL = 1336 
	#
	# MessageId: ERROR_INVALID_SID
	#
	# MessageText:
	#
	# The security ID structure is invalid.
	#
	ERROR_INVALID_SID = 1337 
	#
	# MessageId: ERROR_INVALID_SECURITY_DESCR
	#
	# MessageText:
	#
	# The security descriptor structure is invalid.
	#
	ERROR_INVALID_SECURITY_DESCR = 1338 
	#
	# MessageId: ERROR_BAD_INHERITANCE_ACL
	#
	# MessageText:
	#
	# The inherited access control list (ACL) or access control entry (ACE) could not be built.
	#
	ERROR_BAD_INHERITANCE_ACL = 1340 
	#
	# MessageId: ERROR_SERVER_DISABLED
	#
	# MessageText:
	#
	# The server is currently disabled.
	#
	ERROR_SERVER_DISABLED = 1341 
	#
	# MessageId: ERROR_SERVER_NOT_DISABLED
	#
	# MessageText:
	#
	# The server is currently enabled.
	#
	ERROR_SERVER_NOT_DISABLED = 1342 
	#
	# MessageId: ERROR_INVALID_ID_AUTHORITY
	#
	# MessageText:
	#
	# The value provided was an invalid value for an identifier authority.
	#
	ERROR_INVALID_ID_AUTHORITY = 1343 
	#
	# MessageId: ERROR_ALLOTTED_SPACE_EXCEEDED
	#
	# MessageText:
	#
	# No more memory is available for security information updates.
	#
	ERROR_ALLOTTED_SPACE_EXCEEDED = 1344 
	#
	# MessageId: ERROR_INVALID_GROUP_ATTRIBUTES
	#
	# MessageText:
	#
	# The specified attributes are invalid, or incompatible with the attributes for the group as a whole.
	#
	ERROR_INVALID_GROUP_ATTRIBUTES = 1345 
	#
	# MessageId: ERROR_BAD_IMPERSONATION_LEVEL
	#
	# MessageText:
	#
	# Either a required impersonation level was not provided, or the provided impersonation level is invalid.
	#
	ERROR_BAD_IMPERSONATION_LEVEL = 1346 
	#
	# MessageId: ERROR_CANT_OPEN_ANONYMOUS
	#
	# MessageText:
	#
	# Cannot open an anonymous level security token.
	#
	ERROR_CANT_OPEN_ANONYMOUS = 1347 
	#
	# MessageId: ERROR_BAD_VALIDATION_CLASS
	#
	# MessageText:
	#
	# The validation information class requested was invalid.
	#
	ERROR_BAD_VALIDATION_CLASS = 1348 
	#
	# MessageId: ERROR_BAD_TOKEN_TYPE
	#
	# MessageText:
	#
	# The type of the token is inappropriate for its attempted use.
	#
	ERROR_BAD_TOKEN_TYPE = 1349 
	#
	# MessageId: ERROR_NO_SECURITY_ON_OBJECT
	#
	# MessageText:
	#
	# Unable to perform a security operation on an object that has no associated security.
	#
	ERROR_NO_SECURITY_ON_OBJECT = 1350 
	#
	# MessageId: ERROR_CANT_ACCESS_DOMAIN_INFO
	#
	# MessageText:
	#
	# Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.
	#
	ERROR_CANT_ACCESS_DOMAIN_INFO = 1351 
	#
	# MessageId: ERROR_INVALID_SERVER_STATE
	#
	# MessageText:
	#
	# The security account manager (SAM) or local security authority (LSA) server was in the wrong state to perform the security operation.
	#
	ERROR_INVALID_SERVER_STATE = 1352 
	#
	# MessageId: ERROR_INVALID_DOMAIN_STATE
	#
	# MessageText:
	#
	# The domain was in the wrong state to perform the security operation.
	#
	ERROR_INVALID_DOMAIN_STATE = 1353 
	#
	# MessageId: ERROR_INVALID_DOMAIN_ROLE
	#
	# MessageText:
	#
	# This operation is only allowed for the Primary Domain Controller of the domain.
	#
	ERROR_INVALID_DOMAIN_ROLE = 1354 
	#
	# MessageId: ERROR_NO_SUCH_DOMAIN
	#
	# MessageText:
	#
	# The specified domain either does not exist or could not be contacted.
	#
	ERROR_NO_SUCH_DOMAIN = 1355 
	#
	# MessageId: ERROR_DOMAIN_EXISTS
	#
	# MessageText:
	#
	# The specified domain already exists.
	#
	ERROR_DOMAIN_EXISTS = 1356 
	#
	# MessageId: ERROR_DOMAIN_LIMIT_EXCEEDED
	#
	# MessageText:
	#
	# An attempt was made to exceed the limit on the number of domains per server.
	#
	ERROR_DOMAIN_LIMIT_EXCEEDED = 1357 
	#
	# MessageId: ERROR_INTERNAL_DB_CORRUPTION
	#
	# MessageText:
	#
	# Unable to complete the requested operation because of either a catastrophic media failure or a data structure corruption on the disk.
	#
	ERROR_INTERNAL_DB_CORRUPTION = 1358 
	#
	# MessageId: ERROR_INTERNAL_ERROR
	#
	# MessageText:
	#
	# An internal error occurred.
	#
	ERROR_INTERNAL_ERROR = 1359 
	#
	# MessageId: ERROR_GENERIC_NOT_MAPPED
	#
	# MessageText:
	#
	# Generic access types were contained in an access mask which should already be mapped to nongeneric types.
	#
	ERROR_GENERIC_NOT_MAPPED = 1360 
	#
	# MessageId: ERROR_BAD_DESCRIPTOR_FORMAT
	#
	# MessageText:
	#
	# A security descriptor is not in the right format (absolute or self-relative).
	#
	ERROR_BAD_DESCRIPTOR_FORMAT = 1361 
	#
	# MessageId: ERROR_NOT_LOGON_PROCESS
	#
	# MessageText:
	#
	# The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.
	#
	ERROR_NOT_LOGON_PROCESS = 1362 
	#
	# MessageId: ERROR_LOGON_SESSION_EXISTS
	#
	# MessageText:
	#
	# Cannot start a new logon session with an ID that is already in use.
	#
	ERROR_LOGON_SESSION_EXISTS = 1363 
	#
	# MessageId: ERROR_NO_SUCH_PACKAGE
	#
	# MessageText:
	#
	# A specified authentication package is unknown.
	#
	ERROR_NO_SUCH_PACKAGE = 1364 
	#
	# MessageId: ERROR_BAD_LOGON_SESSION_STATE
	#
	# MessageText:
	#
	# The logon session is not in a state that is consistent with the requested operation.
	#
	ERROR_BAD_LOGON_SESSION_STATE = 1365 
	#
	# MessageId: ERROR_LOGON_SESSION_COLLISION
	#
	# MessageText:
	#
	# The logon session ID is already in use.
	#
	ERROR_LOGON_SESSION_COLLISION = 1366 
	#
	# MessageId: ERROR_INVALID_LOGON_TYPE
	#
	# MessageText:
	#
	# A logon request contained an invalid logon type value.
	#
	ERROR_INVALID_LOGON_TYPE = 1367 
	#
	# MessageId: ERROR_CANNOT_IMPERSONATE
	#
	# MessageText:
	#
	# Unable to impersonate using a named pipe until data has been read from that pipe.
	#
	ERROR_CANNOT_IMPERSONATE = 1368 
	#
	# MessageId: ERROR_RXACT_INVALID_STATE
	#
	# MessageText:
	#
	# The transaction state of a registry subtree is incompatible with the requested operation.
	#
	ERROR_RXACT_INVALID_STATE = 1369 
	#
	# MessageId: ERROR_RXACT_COMMIT_FAILURE
	#
	# MessageText:
	#
	# An internal security database corruption has been encountered.
	#
	ERROR_RXACT_COMMIT_FAILURE = 1370 
	#
	# MessageId: ERROR_SPECIAL_ACCOUNT
	#
	# MessageText:
	#
	# Cannot perform this operation on built-in accounts.
	#
	ERROR_SPECIAL_ACCOUNT = 1371 
	#
	# MessageId: ERROR_SPECIAL_GROUP
	#
	# MessageText:
	#
	# Cannot perform this operation on this built-in special group.
	#
	ERROR_SPECIAL_GROUP = 1372 
	#
	# MessageId: ERROR_SPECIAL_USER
	#
	# MessageText:
	#
	# Cannot perform this operation on this built-in special user.
	#
	ERROR_SPECIAL_USER = 1373 
	#
	# MessageId: ERROR_MEMBERS_PRIMARY_GROUP
	#
	# MessageText:
	#
	# The user cannot be removed from a group because the group is currently the user's primary group.
	#
	ERROR_MEMBERS_PRIMARY_GROUP = 1374 
	#
	# MessageId: ERROR_TOKEN_ALREADY_IN_USE
	#
	# MessageText:
	#
	# The token is already in use as a primary token.
	#
	ERROR_TOKEN_ALREADY_IN_USE = 1375 
	#
	# MessageId: ERROR_NO_SUCH_ALIAS
	#
	# MessageText:
	#
	# The specified local group does not exist.
	#
	ERROR_NO_SUCH_ALIAS = 1376 
	#
	# MessageId: ERROR_MEMBER_NOT_IN_ALIAS
	#
	# MessageText:
	#
	# The specified account name is not a member of the group.
	#
	ERROR_MEMBER_NOT_IN_ALIAS = 1377 
	#
	# MessageId: ERROR_MEMBER_IN_ALIAS
	#
	# MessageText:
	#
	# The specified account name is already a member of the group.
	#
	ERROR_MEMBER_IN_ALIAS = 1378 
	#
	# MessageId: ERROR_ALIAS_EXISTS
	#
	# MessageText:
	#
	# The specified local group already exists.
	#
	ERROR_ALIAS_EXISTS = 1379 
	#
	# MessageId: ERROR_LOGON_NOT_GRANTED
	#
	# MessageText:
	#
	# Logon failure: the user has not been granted the requested logon type at this computer.
	#
	ERROR_LOGON_NOT_GRANTED = 1380 
	#
	# MessageId: ERROR_TOO_MANY_SECRETS
	#
	# MessageText:
	#
	# The maximum number of secrets that may be stored in a single system has been exceeded.
	#
	ERROR_TOO_MANY_SECRETS = 1381 
	#
	# MessageId: ERROR_SECRET_TOO_LONG
	#
	# MessageText:
	#
	# The length of a secret exceeds the maximum length allowed.
	#
	ERROR_SECRET_TOO_LONG = 1382 
	#
	# MessageId: ERROR_INTERNAL_DB_ERROR
	#
	# MessageText:
	#
	# The local security authority database contains an internal inconsistency.
	#
	ERROR_INTERNAL_DB_ERROR = 1383 
	#
	# MessageId: ERROR_TOO_MANY_CONTEXT_IDS
	#
	# MessageText:
	#
	# During a logon attempt, the user's security context accumulated too many security IDs.
	#
	ERROR_TOO_MANY_CONTEXT_IDS = 1384 
	#
	# MessageId: ERROR_LOGON_TYPE_NOT_GRANTED
	#
	# MessageText:
	#
	# Logon failure: the user has not been granted the requested logon type at this computer.
	#
	ERROR_LOGON_TYPE_NOT_GRANTED = 1385 
	#
	# MessageId: ERROR_NT_CROSS_ENCRYPTION_REQUIRED
	#
	# MessageText:
	#
	# A cross-encrypted password is necessary to change a user password.
	#
	ERROR_NT_CROSS_ENCRYPTION_REQUIRED = 1386 
	#
	# MessageId: ERROR_NO_SUCH_MEMBER
	#
	# MessageText:
	#
	# A member could not be added to or removed from the local group because the member does not exist.
	#
	ERROR_NO_SUCH_MEMBER = 1387 
	#
	# MessageId: ERROR_INVALID_MEMBER
	#
	# MessageText:
	#
	# A new member could not be added to a local group because the member has the wrong account type.
	#
	ERROR_INVALID_MEMBER = 1388 
	#
	# MessageId: ERROR_TOO_MANY_SIDS
	#
	# MessageText:
	#
	# Too many security IDs have been specified.
	#
	ERROR_TOO_MANY_SIDS = 1389 
	#
	# MessageId: ERROR_LM_CROSS_ENCRYPTION_REQUIRED
	#
	# MessageText:
	#
	# A cross-encrypted password is necessary to change this user password.
	#
	ERROR_LM_CROSS_ENCRYPTION_REQUIRED = 1390 
	#
	# MessageId: ERROR_NO_INHERITANCE
	#
	# MessageText:
	#
	# Indicates an ACL contains no inheritable components.
	#
	ERROR_NO_INHERITANCE = 1391 
	#
	# MessageId: ERROR_FILE_CORRUPT
	#
	# MessageText:
	#
	# The file or directory is corrupted and unreadable.
	#
	ERROR_FILE_CORRUPT = 1392 
	#
	# MessageId: ERROR_DISK_CORRUPT
	#
	# MessageText:
	#
	# The disk structure is corrupted and unreadable.
	#
	ERROR_DISK_CORRUPT = 1393 
	#
	# MessageId: ERROR_NO_USER_SESSION_KEY
	#
	# MessageText:
	#
	# There is no user session key for the specified logon session.
	#
	ERROR_NO_USER_SESSION_KEY = 1394 
	#
	# MessageId: ERROR_LICENSE_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.
	#
	ERROR_LICENSE_QUOTA_EXCEEDED = 1395 
	#
	# MessageId: ERROR_WRONG_TARGET_NAME
	#
	# MessageText:
	#
	# The target account name is incorrect.
	#
	ERROR_WRONG_TARGET_NAME = 1396 
	#
	# MessageId: ERROR_MUTUAL_AUTH_FAILED
	#
	# MessageText:
	#
	# Mutual Authentication failed. The server's password is out of date at the domain controller.
	#
	ERROR_MUTUAL_AUTH_FAILED = 1397 
	#
	# MessageId: ERROR_TIME_SKEW
	#
	# MessageText:
	#
	# There is a time and/or date difference between the client and server.
	#
	ERROR_TIME_SKEW = 1398 
	#
	# MessageId: ERROR_CURRENT_DOMAIN_NOT_ALLOWED
	#
	# MessageText:
	#
	# This operation cannot be performed on the current domain.
	#
	ERROR_CURRENT_DOMAIN_NOT_ALLOWED = 1399 
	#########################/
	#                                               #
	#              WinUser Error codes              #
	#                                               #
	#                 1400 to 1499                  #
	#########################/
	#
	# MessageId: ERROR_INVALID_WINDOW_HANDLE
	#
	# MessageText:
	#
	# Invalid window handle.
	#
	ERROR_INVALID_WINDOW_HANDLE = 1400 
	#
	# MessageId: ERROR_INVALID_MENU_HANDLE
	#
	# MessageText:
	#
	# Invalid menu handle.
	#
	ERROR_INVALID_MENU_HANDLE = 1401 
	#
	# MessageId: ERROR_INVALID_CURSOR_HANDLE
	#
	# MessageText:
	#
	# Invalid cursor handle.
	#
	ERROR_INVALID_CURSOR_HANDLE = 1402 
	#
	# MessageId: ERROR_INVALID_ACCEL_HANDLE
	#
	# MessageText:
	#
	# Invalid accelerator table handle.
	#
	ERROR_INVALID_ACCEL_HANDLE = 1403 
	#
	# MessageId: ERROR_INVALID_HOOK_HANDLE
	#
	# MessageText:
	#
	# Invalid hook handle.
	#
	ERROR_INVALID_HOOK_HANDLE = 1404 
	#
	# MessageId: ERROR_INVALID_DWP_HANDLE
	#
	# MessageText:
	#
	# Invalid handle to a multiple-window position structure.
	#
	ERROR_INVALID_DWP_HANDLE = 1405 
	#
	# MessageId: ERROR_TLW_WITH_WSCHILD
	#
	# MessageText:
	#
	# Cannot create a top-level child window.
	#
	ERROR_TLW_WITH_WSCHILD = 1406 
	#
	# MessageId: ERROR_CANNOT_FIND_WND_CLASS
	#
	# MessageText:
	#
	# Cannot find window class.
	#
	ERROR_CANNOT_FIND_WND_CLASS = 1407 
	#
	# MessageId: ERROR_WINDOW_OF_OTHER_THREAD
	#
	# MessageText:
	#
	# Invalid window; it belongs to other thread.
	#
	ERROR_WINDOW_OF_OTHER_THREAD = 1408 
	#
	# MessageId: ERROR_HOTKEY_ALREADY_REGISTERED
	#
	# MessageText:
	#
	# Hot key is already registered.
	#
	ERROR_HOTKEY_ALREADY_REGISTERED = 1409 
	#
	# MessageId: ERROR_CLASS_ALREADY_EXISTS
	#
	# MessageText:
	#
	# Class already exists.
	#
	ERROR_CLASS_ALREADY_EXISTS = 1410 
	#
	# MessageId: ERROR_CLASS_DOES_NOT_EXIST
	#
	# MessageText:
	#
	# Class does not exist.
	#
	ERROR_CLASS_DOES_NOT_EXIST = 1411 
	#
	# MessageId: ERROR_CLASS_HAS_WINDOWS
	#
	# MessageText:
	#
	# Class still has open windows.
	#
	ERROR_CLASS_HAS_WINDOWS = 1412 
	#
	# MessageId: ERROR_INVALID_INDEX
	#
	# MessageText:
	#
	# Invalid index.
	#
	ERROR_INVALID_INDEX = 1413 
	#
	# MessageId: ERROR_INVALID_ICON_HANDLE
	#
	# MessageText:
	#
	# Invalid icon handle.
	#
	ERROR_INVALID_ICON_HANDLE = 1414 
	#
	# MessageId: ERROR_PRIVATE_DIALOG_INDEX
	#
	# MessageText:
	#
	# Using private DIALOG window words.
	#
	ERROR_PRIVATE_DIALOG_INDEX = 1415 
	#
	# MessageId: ERROR_LISTBOX_ID_NOT_FOUND
	#
	# MessageText:
	#
	# The list box identifier was not found.
	#
	ERROR_LISTBOX_ID_NOT_FOUND = 1416 
	#
	# MessageId: ERROR_NO_WILDCARD_CHARACTERS
	#
	# MessageText:
	#
	# No wildcards were found.
	#
	ERROR_NO_WILDCARD_CHARACTERS = 1417 
	#
	# MessageId: ERROR_CLIPBOARD_NOT_OPEN
	#
	# MessageText:
	#
	# Thread does not have a clipboard open.
	#
	ERROR_CLIPBOARD_NOT_OPEN = 1418 
	#
	# MessageId: ERROR_HOTKEY_NOT_REGISTERED
	#
	# MessageText:
	#
	# Hot key is not registered.
	#
	ERROR_HOTKEY_NOT_REGISTERED = 1419 
	#
	# MessageId: ERROR_WINDOW_NOT_DIALOG
	#
	# MessageText:
	#
	# The window is not a valid dialog window.
	#
	ERROR_WINDOW_NOT_DIALOG = 1420 
	#
	# MessageId: ERROR_CONTROL_ID_NOT_FOUND
	#
	# MessageText:
	#
	# Control ID not found.
	#
	ERROR_CONTROL_ID_NOT_FOUND = 1421 
	#
	# MessageId: ERROR_INVALID_COMBOBOX_MESSAGE
	#
	# MessageText:
	#
	# Invalid message for a combo box because it does not have an edit control.
	#
	ERROR_INVALID_COMBOBOX_MESSAGE = 1422 
	#
	# MessageId: ERROR_WINDOW_NOT_COMBOBOX
	#
	# MessageText:
	#
	# The window is not a combo box.
	#
	ERROR_WINDOW_NOT_COMBOBOX = 1423 
	#
	# MessageId: ERROR_INVALID_EDIT_HEIGHT
	#
	# MessageText:
	#
	# Height must be less than 256.
	#
	ERROR_INVALID_EDIT_HEIGHT = 1424 
	#
	# MessageId: ERROR_DC_NOT_FOUND
	#
	# MessageText:
	#
	# Invalid device context (DC) handle.
	#
	ERROR_DC_NOT_FOUND = 1425 
	#
	# MessageId: ERROR_INVALID_HOOK_FILTER
	#
	# MessageText:
	#
	# Invalid hook procedure type.
	#
	ERROR_INVALID_HOOK_FILTER = 1426 
	#
	# MessageId: ERROR_INVALID_FILTER_PROC
	#
	# MessageText:
	#
	# Invalid hook procedure.
	#
	ERROR_INVALID_FILTER_PROC = 1427 
	#
	# MessageId: ERROR_HOOK_NEEDS_HMOD
	#
	# MessageText:
	#
	# Cannot set nonlocal hook without a module handle.
	#
	ERROR_HOOK_NEEDS_HMOD = 1428 
	#
	# MessageId: ERROR_GLOBAL_ONLY_HOOK
	#
	# MessageText:
	#
	# This hook procedure can only be set globally.
	#
	ERROR_GLOBAL_ONLY_HOOK = 1429 
	#
	# MessageId: ERROR_JOURNAL_HOOK_SET
	#
	# MessageText:
	#
	# The journal hook procedure is already installed.
	#
	ERROR_JOURNAL_HOOK_SET = 1430 
	#
	# MessageId: ERROR_HOOK_NOT_INSTALLED
	#
	# MessageText:
	#
	# The hook procedure is not installed.
	#
	ERROR_HOOK_NOT_INSTALLED = 1431 
	#
	# MessageId: ERROR_INVALID_LB_MESSAGE
	#
	# MessageText:
	#
	# Invalid message for single-selection list box.
	#
	ERROR_INVALID_LB_MESSAGE = 1432 
	#
	# MessageId: ERROR_SETCOUNT_ON_BAD_LB
	#
	# MessageText:
	#
	# LB_SETCOUNT sent to non-lazy list box.
	#
	ERROR_SETCOUNT_ON_BAD_LB = 1433 
	#
	# MessageId: ERROR_LB_WITHOUT_TABSTOPS
	#
	# MessageText:
	#
	# This list box does not support tab stops.
	#
	ERROR_LB_WITHOUT_TABSTOPS = 1434 
	#
	# MessageId: ERROR_DESTROY_OBJECT_OF_OTHER_THREAD
	#
	# MessageText:
	#
	# Cannot destroy object created by another thread.
	#
	ERROR_DESTROY_OBJECT_OF_OTHER_THREAD = 1435 
	#
	# MessageId: ERROR_CHILD_WINDOW_MENU
	#
	# MessageText:
	#
	# Child windows cannot have menus.
	#
	ERROR_CHILD_WINDOW_MENU = 1436 
	#
	# MessageId: ERROR_NO_SYSTEM_MENU
	#
	# MessageText:
	#
	# The window does not have a system menu.
	#
	ERROR_NO_SYSTEM_MENU = 1437 
	#
	# MessageId: ERROR_INVALID_MSGBOX_STYLE
	#
	# MessageText:
	#
	# Invalid message box style.
	#
	ERROR_INVALID_MSGBOX_STYLE = 1438 
	#
	# MessageId: ERROR_INVALID_SPI_VALUE
	#
	# MessageText:
	#
	# Invalid system-wide (SPI_*) parameter.
	#
	ERROR_INVALID_SPI_VALUE = 1439 
	#
	# MessageId: ERROR_SCREEN_ALREADY_LOCKED
	#
	# MessageText:
	#
	# Screen already locked.
	#
	ERROR_SCREEN_ALREADY_LOCKED = 1440 
	#
	# MessageId: ERROR_HWNDS_HAVE_DIFF_PARENT
	#
	# MessageText:
	#
	# All handles to windows in a multiple-window position structure must have the same parent.
	#
	ERROR_HWNDS_HAVE_DIFF_PARENT = 1441 
	#
	# MessageId: ERROR_NOT_CHILD_WINDOW
	#
	# MessageText:
	#
	# The window is not a child window.
	#
	ERROR_NOT_CHILD_WINDOW = 1442 
	#
	# MessageId: ERROR_INVALID_GW_COMMAND
	#
	# MessageText:
	#
	# Invalid GW_* command.
	#
	ERROR_INVALID_GW_COMMAND = 1443 
	#
	# MessageId: ERROR_INVALID_THREAD_ID
	#
	# MessageText:
	#
	# Invalid thread identifier.
	#
	ERROR_INVALID_THREAD_ID = 1444 
	#
	# MessageId: ERROR_NON_MDICHILD_WINDOW
	#
	# MessageText:
	#
	# Cannot process a message from a window that is not a multiple document interface (MDI) window.
	#
	ERROR_NON_MDICHILD_WINDOW = 1445 
	#
	# MessageId: ERROR_POPUP_ALREADY_ACTIVE
	#
	# MessageText:
	#
	# Popup menu already active.
	#
	ERROR_POPUP_ALREADY_ACTIVE = 1446 
	#
	# MessageId: ERROR_NO_SCROLLBARS
	#
	# MessageText:
	#
	# The window does not have scroll bars.
	#
	ERROR_NO_SCROLLBARS = 1447 
	#
	# MessageId: ERROR_INVALID_SCROLLBAR_RANGE
	#
	# MessageText:
	#
	# Scroll bar range cannot be greater than MAXLONG.
	#
	ERROR_INVALID_SCROLLBAR_RANGE = 1448 
	#
	# MessageId: ERROR_INVALID_SHOWWIN_COMMAND
	#
	# MessageText:
	#
	# Cannot show or remove the window in the way specified.
	#
	ERROR_INVALID_SHOWWIN_COMMAND = 1449 
	#
	# MessageId: ERROR_NO_SYSTEM_RESOURCES
	#
	# MessageText:
	#
	# Insufficient system resources exist to complete the requested service.
	#
	ERROR_NO_SYSTEM_RESOURCES = 1450 
	#
	# MessageId: ERROR_NONPAGED_SYSTEM_RESOURCES
	#
	# MessageText:
	#
	# Insufficient system resources exist to complete the requested service.
	#
	ERROR_NONPAGED_SYSTEM_RESOURCES = 1451 
	#
	# MessageId: ERROR_PAGED_SYSTEM_RESOURCES
	#
	# MessageText:
	#
	# Insufficient system resources exist to complete the requested service.
	#
	ERROR_PAGED_SYSTEM_RESOURCES = 1452 
	#
	# MessageId: ERROR_WORKING_SET_QUOTA
	#
	# MessageText:
	#
	# Insufficient quota to complete the requested service.
	#
	ERROR_WORKING_SET_QUOTA = 1453 
	#
	# MessageId: ERROR_PAGEFILE_QUOTA
	#
	# MessageText:
	#
	# Insufficient quota to complete the requested service.
	#
	ERROR_PAGEFILE_QUOTA = 1454 
	#
	# MessageId: ERROR_COMMITMENT_LIMIT
	#
	# MessageText:
	#
	# The paging file is too small for this operation to complete.
	#
	ERROR_COMMITMENT_LIMIT = 1455 
	#
	# MessageId: ERROR_MENU_ITEM_NOT_FOUND
	#
	# MessageText:
	#
	# A menu item was not found.
	#
	ERROR_MENU_ITEM_NOT_FOUND = 1456 
	#
	# MessageId: ERROR_INVALID_KEYBOARD_HANDLE
	#
	# MessageText:
	#
	# Invalid keyboard layout handle.
	#
	ERROR_INVALID_KEYBOARD_HANDLE = 1457 
	#
	# MessageId: ERROR_HOOK_TYPE_NOT_ALLOWED
	#
	# MessageText:
	#
	# Hook type not allowed.
	#
	ERROR_HOOK_TYPE_NOT_ALLOWED = 1458 
	#
	# MessageId: ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION
	#
	# MessageText:
	#
	# This operation requires an interactive window station.
	#
	ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION = 1459 
	#
	# MessageId: ERROR_TIMEOUT
	#
	# MessageText:
	#
	# This operation returned because the timeout period expired.
	#
	ERROR_TIMEOUT = 1460 
	#
	# MessageId: ERROR_INVALID_MONITOR_HANDLE
	#
	# MessageText:
	#
	# Invalid monitor handle.
	#
	ERROR_INVALID_MONITOR_HANDLE = 1461 
	#
	# MessageId: ERROR_INCORRECT_SIZE
	#
	# MessageText:
	#
	# Incorrect size argument.
	#
	ERROR_INCORRECT_SIZE = 1462 
	#
	# MessageId: ERROR_SYMLINK_CLASS_DISABLED
	#
	# MessageText:
	#
	# The symbolic link cannot be followed because its type is disabled.
	#
	ERROR_SYMLINK_CLASS_DISABLED = 1463 
	#
	# MessageId: ERROR_SYMLINK_NOT_SUPPORTED
	#
	# MessageText:
	#
	# This application does not support the current operation on symbolic links.
	#
	ERROR_SYMLINK_NOT_SUPPORTED = 1464 
	#
	# MessageId: ERROR_XML_PARSE_ERROR
	#
	# MessageText:
	#
	# Windows was unable to parse the requested XML data.
	#
	ERROR_XML_PARSE_ERROR = 1465 
	#
	# MessageId: ERROR_XMLDSIG_ERROR
	#
	# MessageText:
	#
	# An error was encountered while processing an XML digital signature.
	#
	ERROR_XMLDSIG_ERROR = 1466 
	#
	# MessageId: ERROR_RESTART_APPLICATION
	#
	# MessageText:
	#
	# This application must be restarted.
	#
	ERROR_RESTART_APPLICATION = 1467 
	#
	# MessageId: ERROR_WRONG_COMPARTMENT
	#
	# MessageText:
	#
	# The caller made the connection request in the wrong routing compartment.
	#
	ERROR_WRONG_COMPARTMENT = 1468 
	#
	# MessageId: ERROR_AUTHIP_FAILURE
	#
	# MessageText:
	#
	# There was an AuthIP failure when attempting to connect to the remote host.
	#
	ERROR_AUTHIP_FAILURE = 1469 
	#
	# MessageId: ERROR_NO_NVRAM_RESOURCES
	#
	# MessageText:
	#
	# Insufficient NVRAM resources exist to complete the requested service. A reboot might be required.
	#
	ERROR_NO_NVRAM_RESOURCES = 1470 
	#
	# MessageId: ERROR_NOT_GUI_PROCESS
	#
	# MessageText:
	#
	# Unable to finish the requested operation because the specified process is not a GUI process.
	#
	ERROR_NOT_GUI_PROCESS = 1471 
	#########################/
	#                                               #
	#             EventLog Error codes              #
	#                                               #
	#                 1500 to 1549                  #
	#########################/
	#
	# MessageId: ERROR_EVENTLOG_FILE_CORRUPT
	#
	# MessageText:
	#
	# The event log file is corrupted.
	#
	ERROR_EVENTLOG_FILE_CORRUPT = 1500 
	#
	# MessageId: ERROR_EVENTLOG_CANT_START
	#
	# MessageText:
	#
	# No event log file could be opened, so the event logging service did not start.
	#
	ERROR_EVENTLOG_CANT_START = 1501 
	#
	# MessageId: ERROR_LOG_FILE_FULL
	#
	# MessageText:
	#
	# The event log file is full.
	#
	ERROR_LOG_FILE_FULL = 1502 
	#
	# MessageId: ERROR_EVENTLOG_FILE_CHANGED
	#
	# MessageText:
	#
	# The event log file has changed between read operations.
	#
	ERROR_EVENTLOG_FILE_CHANGED = 1503 
	#
	# MessageId: ERROR_CONTAINER_ASSIGNED
	#
	# MessageText:
	#
	# The specified Job already has a container assigned to it.
	#
	ERROR_CONTAINER_ASSIGNED = 1504 
	#
	# MessageId: ERROR_JOB_NO_CONTAINER
	#
	# MessageText:
	#
	# The specified Job does not have a container assigned to it.
	#
	ERROR_JOB_NO_CONTAINER = 1505 
	#########################/
	#                                               #
	#            Class Scheduler Error codes        #
	#                                               #
	#                 1550 to 1599                  #
	#########################/
	#
	# MessageId: ERROR_INVALID_TASK_NAME
	#
	# MessageText:
	#
	# The specified task name is invalid.
	#
	ERROR_INVALID_TASK_NAME = 1550 
	#
	# MessageId: ERROR_INVALID_TASK_INDEX
	#
	# MessageText:
	#
	# The specified task index is invalid.
	#
	ERROR_INVALID_TASK_INDEX = 1551 
	#
	# MessageId: ERROR_THREAD_ALREADY_IN_TASK
	#
	# MessageText:
	#
	# The specified thread is already joining a task.
	#
	ERROR_THREAD_ALREADY_IN_TASK = 1552 
	#########################/
	#                                               #
	#                MSI Error codes                #
	#                                               #
	#                 1600 to 1699                  #
	#########################/
	#
	# MessageId: ERROR_INSTALL_SERVICE_FAILURE
	#
	# MessageText:
	#
	# The Windows Installer Service could not be accessed. This can occur if the Windows Installer is not correctly installed. Contact your support personnel for assistance.
	#
	ERROR_INSTALL_SERVICE_FAILURE = 1601 
	#
	# MessageId: ERROR_INSTALL_USEREXIT
	#
	# MessageText:
	#
	# User cancelled installation.
	#
	ERROR_INSTALL_USEREXIT = 1602 
	#
	# MessageId: ERROR_INSTALL_FAILURE
	#
	# MessageText:
	#
	# Fatal error during installation.
	#
	ERROR_INSTALL_FAILURE = 1603 
	#
	# MessageId: ERROR_INSTALL_SUSPEND
	#
	# MessageText:
	#
	# Installation suspended, incomplete.
	#
	ERROR_INSTALL_SUSPEND = 1604 
	#
	# MessageId: ERROR_UNKNOWN_PRODUCT
	#
	# MessageText:
	#
	# This action is only valid for products that are currently installed.
	#
	ERROR_UNKNOWN_PRODUCT = 1605 
	#
	# MessageId: ERROR_UNKNOWN_FEATURE
	#
	# MessageText:
	#
	# Feature ID not registered.
	#
	ERROR_UNKNOWN_FEATURE = 1606 
	#
	# MessageId: ERROR_UNKNOWN_COMPONENT
	#
	# MessageText:
	#
	# Component ID not registered.
	#
	ERROR_UNKNOWN_COMPONENT = 1607 
	#
	# MessageId: ERROR_UNKNOWN_PROPERTY
	#
	# MessageText:
	#
	# Unknown property.
	#
	ERROR_UNKNOWN_PROPERTY = 1608 
	#
	# MessageId: ERROR_INVALID_HANDLE_STATE
	#
	# MessageText:
	#
	# Handle is in an invalid state.
	#
	ERROR_INVALID_HANDLE_STATE = 1609 
	#
	# MessageId: ERROR_BAD_CONFIGURATION
	#
	# MessageText:
	#
	# The configuration data for this product is corrupt. Contact your support personnel.
	#
	ERROR_BAD_CONFIGURATION = 1610 
	#
	# MessageId: ERROR_INDEX_ABSENT
	#
	# MessageText:
	#
	# Component qualifier not present.
	#
	ERROR_INDEX_ABSENT = 1611 
	#
	# MessageId: ERROR_INSTALL_SOURCE_ABSENT
	#
	# MessageText:
	#
	# The installation source for this product is not available. Verify that the source exists and that you can access it.
	#
	ERROR_INSTALL_SOURCE_ABSENT = 1612 
	#
	# MessageId: ERROR_INSTALL_PACKAGE_VERSION
	#
	# MessageText:
	#
	# This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.
	#
	ERROR_INSTALL_PACKAGE_VERSION = 1613 
	#
	# MessageId: ERROR_PRODUCT_UNINSTALLED
	#
	# MessageText:
	#
	# Product is uninstalled.
	#
	ERROR_PRODUCT_UNINSTALLED = 1614 
	#
	# MessageId: ERROR_BAD_QUERY_SYNTAX
	#
	# MessageText:
	#
	# SQL query syntax invalid or unsupported.
	#
	ERROR_BAD_QUERY_SYNTAX = 1615 
	#
	# MessageId: ERROR_INVALID_FIELD
	#
	# MessageText:
	#
	# Record field does not exist.
	#
	ERROR_INVALID_FIELD = 1616 
	#
	# MessageId: ERROR_DEVICE_REMOVED
	#
	# MessageText:
	#
	# The device has been removed.
	#
	ERROR_DEVICE_REMOVED = 1617 
	#
	# MessageId: ERROR_INSTALL_ALREADY_RUNNING
	#
	# MessageText:
	#
	# Another installation is already in progress. Complete that installation before proceeding with this install.
	#
	ERROR_INSTALL_ALREADY_RUNNING = 1618 
	#
	# MessageId: ERROR_INSTALL_PACKAGE_OPEN_FAILED
	#
	# MessageText:
	#
	# This installation package could not be opened. Verify that the package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer package.
	#
	ERROR_INSTALL_PACKAGE_OPEN_FAILED = 1619 
	#
	# MessageId: ERROR_INSTALL_PACKAGE_INVALID
	#
	# MessageText:
	#
	# This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.
	#
	ERROR_INSTALL_PACKAGE_INVALID = 1620 
	#
	# MessageId: ERROR_INSTALL_UI_FAILURE
	#
	# MessageText:
	#
	# There was an error starting the Windows Installer service user interface. Contact your support personnel.
	#
	ERROR_INSTALL_UI_FAILURE = 1621 
	#
	# MessageId: ERROR_INSTALL_LOG_FAILURE
	#
	# MessageText:
	#
	# Error opening installation log file. Verify that the specified log file location exists and that you can write to it.
	#
	ERROR_INSTALL_LOG_FAILURE = 1622 
	#
	# MessageId: ERROR_INSTALL_LANGUAGE_UNSUPPORTED
	#
	# MessageText:
	#
	# The language of this installation package is not supported by your system.
	#
	ERROR_INSTALL_LANGUAGE_UNSUPPORTED = 1623 
	#
	# MessageId: ERROR_INSTALL_TRANSFORM_FAILURE
	#
	# MessageText:
	#
	# Error applying transforms. Verify that the specified transform paths are valid.
	#
	ERROR_INSTALL_TRANSFORM_FAILURE = 1624 
	#
	# MessageId: ERROR_INSTALL_PACKAGE_REJECTED
	#
	# MessageText:
	#
	# This installation is forbidden by system policy. Contact your system administrator.
	#
	ERROR_INSTALL_PACKAGE_REJECTED = 1625 
	#
	# MessageId: ERROR_FUNCTION_NOT_CALLED
	#
	# MessageText:
	#
	# Function could not be executed.
	#
	ERROR_FUNCTION_NOT_CALLED = 1626 
	#
	# MessageId: ERROR_FUNCTION_FAILED
	#
	# MessageText:
	#
	# Function failed during execution.
	#
	ERROR_FUNCTION_FAILED = 1627 
	#
	# MessageId: ERROR_INVALID_TABLE
	#
	# MessageText:
	#
	# Invalid or unknown table specified.
	#
	ERROR_INVALID_TABLE = 1628 
	#
	# MessageId: ERROR_DATATYPE_MISMATCH
	#
	# MessageText:
	#
	# Data supplied is of wrong type.
	#
	ERROR_DATATYPE_MISMATCH = 1629 
	#
	# MessageId: ERROR_UNSUPPORTED_TYPE
	#
	# MessageText:
	#
	# Data of this type is not supported.
	#
	ERROR_UNSUPPORTED_TYPE = 1630 
	#
	# MessageId: ERROR_CREATE_FAILED
	#
	# MessageText:
	#
	# The Windows Installer service failed to start. Contact your support personnel.
	#
	ERROR_CREATE_FAILED = 1631 
	#
	# MessageId: ERROR_INSTALL_TEMP_UNWRITABLE
	#
	# MessageText:
	#
	# The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.
	#
	ERROR_INSTALL_TEMP_UNWRITABLE = 1632 
	#
	# MessageId: ERROR_INSTALL_PLATFORM_UNSUPPORTED
	#
	# MessageText:
	#
	# This installation package is not supported by this processor type. Contact your product vendor.
	#
	ERROR_INSTALL_PLATFORM_UNSUPPORTED = 1633 
	#
	# MessageId: ERROR_INSTALL_NOTUSED
	#
	# MessageText:
	#
	# Component not used on this computer.
	#
	ERROR_INSTALL_NOTUSED = 1634 
	#
	# MessageId: ERROR_PATCH_PACKAGE_OPEN_FAILED
	#
	# MessageText:
	#
	# This update package could not be opened. Verify that the update package exists and that you can access it, or contact the application vendor to verify that this is a valid Windows Installer update package.
	#
	ERROR_PATCH_PACKAGE_OPEN_FAILED = 1635 
	#
	# MessageId: ERROR_PATCH_PACKAGE_INVALID
	#
	# MessageText:
	#
	# This update package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer update package.
	#
	ERROR_PATCH_PACKAGE_INVALID = 1636 
	#
	# MessageId: ERROR_PATCH_PACKAGE_UNSUPPORTED
	#
	# MessageText:
	#
	# This update package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.
	#
	ERROR_PATCH_PACKAGE_UNSUPPORTED = 1637 
	#
	# MessageId: ERROR_PRODUCT_VERSION
	#
	# MessageText:
	#
	# Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use Add/Remove Programs on the Control Panel.
	#
	ERROR_PRODUCT_VERSION = 1638 
	#
	# MessageId: ERROR_INVALID_COMMAND_LINE
	#
	# MessageText:
	#
	# Invalid command line argument. Consult the Windows Installer SDK for detailed command line help.
	#
	ERROR_INVALID_COMMAND_LINE = 1639 
	#
	# MessageId: ERROR_INSTALL_REMOTE_DISALLOWED
	#
	# MessageText:
	#
	# Only administrators have permission to add, remove, or configure server software during a Terminal services remote session. If you want to install or configure software on the server, contact your network administrator.
	#
	ERROR_INSTALL_REMOTE_DISALLOWED = 1640 
	#
	# MessageId: ERROR_SUCCESS_REBOOT_INITIATED
	#
	# MessageText:
	#
	# The requested operation completed successfully. The system will be restarted so the changes can take effect.
	#
	ERROR_SUCCESS_REBOOT_INITIATED = 1641 
	#
	# MessageId: ERROR_PATCH_TARGET_NOT_FOUND
	#
	# MessageText:
	#
	# The upgrade cannot be installed by the Windows Installer service because the program to be upgraded may be missing, or the upgrade may update a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade.
	#
	ERROR_PATCH_TARGET_NOT_FOUND = 1642 
	#
	# MessageId: ERROR_PATCH_PACKAGE_REJECTED
	#
	# MessageText:
	#
	# The update package is not permitted by software restriction policy.
	#
	ERROR_PATCH_PACKAGE_REJECTED = 1643 
	#
	# MessageId: ERROR_INSTALL_TRANSFORM_REJECTED
	#
	# MessageText:
	#
	# One or more customizations are not permitted by software restriction policy.
	#
	ERROR_INSTALL_TRANSFORM_REJECTED = 1644 
	#
	# MessageId: ERROR_INSTALL_REMOTE_PROHIBITED
	#
	# MessageText:
	#
	# The Windows Installer does not permit installation from a Remote Desktop Connection.
	#
	ERROR_INSTALL_REMOTE_PROHIBITED = 1645 
	#
	# MessageId: ERROR_PATCH_REMOVAL_UNSUPPORTED
	#
	# MessageText:
	#
	# Uninstallation of the update package is not supported.
	#
	ERROR_PATCH_REMOVAL_UNSUPPORTED = 1646 
	#
	# MessageId: ERROR_UNKNOWN_PATCH
	#
	# MessageText:
	#
	# The update is not applied to this product.
	#
	ERROR_UNKNOWN_PATCH = 1647 
	#
	# MessageId: ERROR_PATCH_NO_SEQUENCE
	#
	# MessageText:
	#
	# No valid sequence could be found for the set of updates.
	#
	ERROR_PATCH_NO_SEQUENCE = 1648 
	#
	# MessageId: ERROR_PATCH_REMOVAL_DISALLOWED
	#
	# MessageText:
	#
	# Update removal was disallowed by policy.
	#
	ERROR_PATCH_REMOVAL_DISALLOWED = 1649 
	#
	# MessageId: ERROR_INVALID_PATCH_XML
	#
	# MessageText:
	#
	# The XML update data is invalid.
	#
	ERROR_INVALID_PATCH_XML = 1650 
	#
	# MessageId: ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT
	#
	# MessageText:
	#
	# Windows Installer does not permit updating of managed advertised products. At least one feature of the product must be installed before applying the update.
	#
	ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT = 1651 
	#
	# MessageId: ERROR_INSTALL_SERVICE_SAFEBOOT
	#
	# MessageText:
	#
	# The Windows Installer service is not accessible in Safe Mode. Please try again when your computer is not in Safe Mode or you can use System Restore to return your machine to a previous good state.
	#
	ERROR_INSTALL_SERVICE_SAFEBOOT = 1652 
	#
	# MessageId: ERROR_FAIL_FAST_EXCEPTION
	#
	# MessageText:
	#
	# A fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.
	#
	ERROR_FAIL_FAST_EXCEPTION = 1653 
	#
	# MessageId: ERROR_INSTALL_REJECTED
	#
	# MessageText:
	#
	# The app that you are trying to run is not supported on this version of Windows.
	#
	ERROR_INSTALL_REJECTED = 1654 
	#
	# MessageId: ERROR_DYNAMIC_CODE_BLOCKED
	#
	# MessageText:
	#
	# The operation was blocked as the process prohibits dynamic code generation.
	#
	ERROR_DYNAMIC_CODE_BLOCKED = 1655 
	#
	# MessageId: ERROR_NOT_SAME_OBJECT
	#
	# MessageText:
	#
	# The objects are not identical.
	#
	ERROR_NOT_SAME_OBJECT = 1656 
	#
	# MessageId: ERROR_STRICT_CFG_VIOLATION
	#
	# MessageText:
	#
	# The specified image file was blocked from loading because it does not enable a feature required by the process: Control Flow Guard.
	#
	ERROR_STRICT_CFG_VIOLATION = 1657 
	#
	# MessageId: ERROR_SET_CONTEXT_DENIED
	#
	# MessageText:
	#
	# The thread context could not be updated because this has been restricted for the process.
	#
	ERROR_SET_CONTEXT_DENIED = 1660 
	#
	# MessageId: ERROR_CROSS_PARTITION_VIOLATION
	#
	# MessageText:
	#
	# An invalid cross-partition private file/section access was attempted.
	#
	ERROR_CROSS_PARTITION_VIOLATION = 1661 
	#
	# MessageId: ERROR_RETURN_ADDRESS_HIJACK_ATTEMPT
	#
	# MessageText:
	#
	# A return address hijack is being attempted. This is supported by the operating system when user-mode shadow stacks are enabled.
	#
	ERROR_RETURN_ADDRESS_HIJACK_ATTEMPT = 1662 
	#########################/
	#                                               #
	#               RPC Error codes                 #
	#                                               #
	#                 1700 to 1999                  #
	#########################/
	#
	# MessageId: RPC_S_INVALID_STRING_BINDING
	#
	# MessageText:
	#
	# The string binding is invalid.
	#
	RPC_S_INVALID_STRING_BINDING = 1700 
	#
	# MessageId: RPC_S_WRONG_KIND_OF_BINDING
	#
	# MessageText:
	#
	# The binding handle is not the correct type.
	#
	RPC_S_WRONG_KIND_OF_BINDING = 1701 
	#
	# MessageId: RPC_S_INVALID_BINDING
	#
	# MessageText:
	#
	# The binding handle is invalid.
	#
	RPC_S_INVALID_BINDING = 1702 
	#
	# MessageId: RPC_S_PROTSEQ_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The RPC protocol sequence is not supported.
	#
	RPC_S_PROTSEQ_NOT_SUPPORTED = 1703 
	#
	# MessageId: RPC_S_INVALID_RPC_PROTSEQ
	#
	# MessageText:
	#
	# The RPC protocol sequence is invalid.
	#
	RPC_S_INVALID_RPC_PROTSEQ = 1704 
	#
	# MessageId: RPC_S_INVALID_STRING_UUID
	#
	# MessageText:
	#
	# The string universal unique identifier (UUID) is invalid.
	#
	RPC_S_INVALID_STRING_UUID = 1705 
	#
	# MessageId: RPC_S_INVALID_ENDPOINT_FORMAT
	#
	# MessageText:
	#
	# The endpoint format is invalid.
	#
	RPC_S_INVALID_ENDPOINT_FORMAT = 1706 
	#
	# MessageId: RPC_S_INVALID_NET_ADDR
	#
	# MessageText:
	#
	# The network address is invalid.
	#
	RPC_S_INVALID_NET_ADDR = 1707 
	#
	# MessageId: RPC_S_NO_ENDPOINT_FOUND
	#
	# MessageText:
	#
	# No endpoint was found.
	#
	RPC_S_NO_ENDPOINT_FOUND = 1708 
	#
	# MessageId: RPC_S_INVALID_TIMEOUT
	#
	# MessageText:
	#
	# The timeout value is invalid.
	#
	RPC_S_INVALID_TIMEOUT = 1709 
	#
	# MessageId: RPC_S_OBJECT_NOT_FOUND
	#
	# MessageText:
	#
	# The object universal unique identifier (UUID) was not found.
	#
	RPC_S_OBJECT_NOT_FOUND = 1710 
	#
	# MessageId: RPC_S_ALREADY_REGISTERED
	#
	# MessageText:
	#
	# The object universal unique identifier (UUID) has already been registered.
	#
	RPC_S_ALREADY_REGISTERED = 1711 
	#
	# MessageId: RPC_S_TYPE_ALREADY_REGISTERED
	#
	# MessageText:
	#
	# The type universal unique identifier (UUID) has already been registered.
	#
	RPC_S_TYPE_ALREADY_REGISTERED = 1712 
	#
	# MessageId: RPC_S_ALREADY_LISTENING
	#
	# MessageText:
	#
	# The RPC server is already listening.
	#
	RPC_S_ALREADY_LISTENING = 1713 
	#
	# MessageId: RPC_S_NO_PROTSEQS_REGISTERED
	#
	# MessageText:
	#
	# No protocol sequences have been registered.
	#
	RPC_S_NO_PROTSEQS_REGISTERED = 1714 
	#
	# MessageId: RPC_S_NOT_LISTENING
	#
	# MessageText:
	#
	# The RPC server is not listening.
	#
	RPC_S_NOT_LISTENING = 1715 
	#
	# MessageId: RPC_S_UNKNOWN_MGR_TYPE
	#
	# MessageText:
	#
	# The manager type is unknown.
	#
	RPC_S_UNKNOWN_MGR_TYPE = 1716 
	#
	# MessageId: RPC_S_UNKNOWN_IF
	#
	# MessageText:
	#
	# The interface is unknown.
	#
	RPC_S_UNKNOWN_IF = 1717 
	#
	# MessageId: RPC_S_NO_BINDINGS
	#
	# MessageText:
	#
	# There are no bindings.
	#
	RPC_S_NO_BINDINGS = 1718 
	#
	# MessageId: RPC_S_NO_PROTSEQS
	#
	# MessageText:
	#
	# There are no protocol sequences.
	#
	RPC_S_NO_PROTSEQS = 1719 
	#
	# MessageId: RPC_S_CANT_CREATE_ENDPOINT
	#
	# MessageText:
	#
	# The endpoint cannot be created.
	#
	RPC_S_CANT_CREATE_ENDPOINT = 1720 
	#
	# MessageId: RPC_S_OUT_OF_RESOURCES
	#
	# MessageText:
	#
	# Not enough resources are available to complete this operation.
	#
	RPC_S_OUT_OF_RESOURCES = 1721 
	#
	# MessageId: RPC_S_SERVER_UNAVAILABLE
	#
	# MessageText:
	#
	# The RPC server is unavailable.
	#
	RPC_S_SERVER_UNAVAILABLE = 1722 
	#
	# MessageId: RPC_S_SERVER_TOO_BUSY
	#
	# MessageText:
	#
	# The RPC server is too busy to complete this operation.
	#
	RPC_S_SERVER_TOO_BUSY = 1723 
	#
	# MessageId: RPC_S_INVALID_NETWORK_OPTIONS
	#
	# MessageText:
	#
	# The network options are invalid.
	#
	RPC_S_INVALID_NETWORK_OPTIONS = 1724 
	#
	# MessageId: RPC_S_NO_CALL_ACTIVE
	#
	# MessageText:
	#
	# There are no remote procedure calls active on this thread.
	#
	RPC_S_NO_CALL_ACTIVE = 1725 
	#
	# MessageId: RPC_S_CALL_FAILED
	#
	# MessageText:
	#
	# The remote procedure call failed.
	#
	RPC_S_CALL_FAILED = 1726 
	#
	# MessageId: RPC_S_CALL_FAILED_DNE
	#
	# MessageText:
	#
	# The remote procedure call failed and did not execute.
	#
	RPC_S_CALL_FAILED_DNE = 1727 
	#
	# MessageId: RPC_S_PROTOCOL_ERROR
	#
	# MessageText:
	#
	# A remote procedure call (RPC) protocol error occurred.
	#
	RPC_S_PROTOCOL_ERROR = 1728 
	#
	# MessageId: RPC_S_PROXY_ACCESS_DENIED
	#
	# MessageText:
	#
	# Access to the HTTP proxy is denied.
	#
	RPC_S_PROXY_ACCESS_DENIED = 1729 
	#
	# MessageId: RPC_S_UNSUPPORTED_TRANS_SYN
	#
	# MessageText:
	#
	# The transfer syntax is not supported by the RPC server.
	#
	RPC_S_UNSUPPORTED_TRANS_SYN = 1730 
	#
	# MessageId: RPC_S_UNSUPPORTED_TYPE
	#
	# MessageText:
	#
	# The universal unique identifier (UUID) type is not supported.
	#
	RPC_S_UNSUPPORTED_TYPE = 1732 
	#
	# MessageId: RPC_S_INVALID_TAG
	#
	# MessageText:
	#
	# The tag is invalid.
	#
	RPC_S_INVALID_TAG = 1733 
	#
	# MessageId: RPC_S_INVALID_BOUND
	#
	# MessageText:
	#
	# The array bounds are invalid.
	#
	RPC_S_INVALID_BOUND = 1734 
	#
	# MessageId: RPC_S_NO_ENTRY_NAME
	#
	# MessageText:
	#
	# The binding does not contain an entry name.
	#
	RPC_S_NO_ENTRY_NAME = 1735 
	#
	# MessageId: RPC_S_INVALID_NAME_SYNTAX
	#
	# MessageText:
	#
	# The name syntax is invalid.
	#
	RPC_S_INVALID_NAME_SYNTAX = 1736 
	#
	# MessageId: RPC_S_UNSUPPORTED_NAME_SYNTAX
	#
	# MessageText:
	#
	# The name syntax is not supported.
	#
	RPC_S_UNSUPPORTED_NAME_SYNTAX = 1737 
	#
	# MessageId: RPC_S_UUID_NO_ADDRESS
	#
	# MessageText:
	#
	# No network address is available to use to construct a universal unique identifier (UUID).
	#
	RPC_S_UUID_NO_ADDRESS = 1739 
	#
	# MessageId: RPC_S_DUPLICATE_ENDPOINT
	#
	# MessageText:
	#
	# The endpoint is a duplicate.
	#
	RPC_S_DUPLICATE_ENDPOINT = 1740 
	#
	# MessageId: RPC_S_UNKNOWN_AUTHN_TYPE
	#
	# MessageText:
	#
	# The authentication type is unknown.
	#
	RPC_S_UNKNOWN_AUTHN_TYPE = 1741 
	#
	# MessageId: RPC_S_MAX_CALLS_TOO_SMALL
	#
	# MessageText:
	#
	# The maximum number of calls is too small.
	#
	RPC_S_MAX_CALLS_TOO_SMALL = 1742 
	#
	# MessageId: RPC_S_STRING_TOO_LONG
	#
	# MessageText:
	#
	# The string is too long.
	#
	RPC_S_STRING_TOO_LONG = 1743 
	#
	# MessageId: RPC_S_PROTSEQ_NOT_FOUND
	#
	# MessageText:
	#
	# The RPC protocol sequence was not found.
	#
	RPC_S_PROTSEQ_NOT_FOUND = 1744 
	#
	# MessageId: RPC_S_PROCNUM_OUT_OF_RANGE
	#
	# MessageText:
	#
	# The procedure number is out of range.
	#
	RPC_S_PROCNUM_OUT_OF_RANGE = 1745 
	#
	# MessageId: RPC_S_BINDING_HAS_NO_AUTH
	#
	# MessageText:
	#
	# The binding does not contain any authentication information.
	#
	RPC_S_BINDING_HAS_NO_AUTH = 1746 
	#
	# MessageId: RPC_S_UNKNOWN_AUTHN_SERVICE
	#
	# MessageText:
	#
	# The authentication service is unknown.
	#
	RPC_S_UNKNOWN_AUTHN_SERVICE = 1747 
	#
	# MessageId: RPC_S_UNKNOWN_AUTHN_LEVEL
	#
	# MessageText:
	#
	# The authentication level is unknown.
	#
	RPC_S_UNKNOWN_AUTHN_LEVEL = 1748 
	#
	# MessageId: RPC_S_INVALID_AUTH_IDENTITY
	#
	# MessageText:
	#
	# The security context is invalid.
	#
	RPC_S_INVALID_AUTH_IDENTITY = 1749 
	#
	# MessageId: RPC_S_UNKNOWN_AUTHZ_SERVICE
	#
	# MessageText:
	#
	# The authorization service is unknown.
	#
	RPC_S_UNKNOWN_AUTHZ_SERVICE = 1750 
	#
	# MessageId: EPT_S_INVALID_ENTRY
	#
	# MessageText:
	#
	# The entry is invalid.
	#
	EPT_S_INVALID_ENTRY = 1751 
	#
	# MessageId: EPT_S_CANT_PERFORM_OP
	#
	# MessageText:
	#
	# The server endpoint cannot perform the operation.
	#
	EPT_S_CANT_PERFORM_OP = 1752 
	#
	# MessageId: EPT_S_NOT_REGISTERED
	#
	# MessageText:
	#
	# There are no more endpoints available from the endpoint mapper.
	#
	EPT_S_NOT_REGISTERED = 1753 
	#
	# MessageId: RPC_S_NOTHING_TO_EXPORT
	#
	# MessageText:
	#
	# No interfaces have been exported.
	#
	RPC_S_NOTHING_TO_EXPORT = 1754 
	#
	# MessageId: RPC_S_INCOMPLETE_NAME
	#
	# MessageText:
	#
	# The entry name is incomplete.
	#
	RPC_S_INCOMPLETE_NAME = 1755 
	#
	# MessageId: RPC_S_INVALID_VERS_OPTION
	#
	# MessageText:
	#
	# The version option is invalid.
	#
	RPC_S_INVALID_VERS_OPTION = 1756 
	#
	# MessageId: RPC_S_NO_MORE_MEMBERS
	#
	# MessageText:
	#
	# There are no more members.
	#
	RPC_S_NO_MORE_MEMBERS = 1757 
	#
	# MessageId: RPC_S_NOT_ALL_OBJS_UNEXPORTED
	#
	# MessageText:
	#
	# There is nothing to unexport.
	#
	RPC_S_NOT_ALL_OBJS_UNEXPORTED = 1758 
	#
	# MessageId: RPC_S_INTERFACE_NOT_FOUND
	#
	# MessageText:
	#
	# The interface was not found.
	#
	RPC_S_INTERFACE_NOT_FOUND = 1759 
	#
	# MessageId: RPC_S_ENTRY_ALREADY_EXISTS
	#
	# MessageText:
	#
	# The entry already exists.
	#
	RPC_S_ENTRY_ALREADY_EXISTS = 1760 
	#
	# MessageId: RPC_S_ENTRY_NOT_FOUND
	#
	# MessageText:
	#
	# The entry is not found.
	#
	RPC_S_ENTRY_NOT_FOUND = 1761 
	#
	# MessageId: RPC_S_NAME_SERVICE_UNAVAILABLE
	#
	# MessageText:
	#
	# The name service is unavailable.
	#
	RPC_S_NAME_SERVICE_UNAVAILABLE = 1762 
	#
	# MessageId: RPC_S_INVALID_NAF_ID
	#
	# MessageText:
	#
	# The network address family is invalid.
	#
	RPC_S_INVALID_NAF_ID = 1763 
	#
	# MessageId: RPC_S_CANNOT_SUPPORT
	#
	# MessageText:
	#
	# The requested operation is not supported.
	#
	RPC_S_CANNOT_SUPPORT = 1764 
	#
	# MessageId: RPC_S_NO_CONTEXT_AVAILABLE
	#
	# MessageText:
	#
	# No security context is available to allow impersonation.
	#
	RPC_S_NO_CONTEXT_AVAILABLE = 1765 
	#
	# MessageId: RPC_S_INTERNAL_ERROR
	#
	# MessageText:
	#
	# An internal error occurred in a remote procedure call (RPC).
	#
	RPC_S_INTERNAL_ERROR = 1766 
	#
	# MessageId: RPC_S_ZERO_DIVIDE
	#
	# MessageText:
	#
	# The RPC server attempted an integer division by zero.
	#
	RPC_S_ZERO_DIVIDE = 1767 
	#
	# MessageId: RPC_S_ADDRESS_ERROR
	#
	# MessageText:
	#
	# An addressing error occurred in the RPC server.
	#
	RPC_S_ADDRESS_ERROR = 1768 
	#
	# MessageId: RPC_S_FP_DIV_ZERO
	#
	# MessageText:
	#
	# A floating-point operation at the RPC server caused a division by zero.
	#
	RPC_S_FP_DIV_ZERO = 1769 
	#
	# MessageId: RPC_S_FP_UNDERFLOW
	#
	# MessageText:
	#
	# A floating-point underflow occurred at the RPC server.
	#
	RPC_S_FP_UNDERFLOW = 1770 
	#
	# MessageId: RPC_S_FP_OVERFLOW
	#
	# MessageText:
	#
	# A floating-point overflow occurred at the RPC server.
	#
	RPC_S_FP_OVERFLOW = 1771 
	#
	# MessageId: RPC_X_NO_MORE_ENTRIES
	#
	# MessageText:
	#
	# The list of RPC servers available for the binding of auto handles has been exhausted.
	#
	RPC_X_NO_MORE_ENTRIES = 1772 
	#
	# MessageId: RPC_X_SS_CHAR_TRANS_OPEN_FAIL
	#
	# MessageText:
	#
	# Unable to open the character translation table file.
	#
	RPC_X_SS_CHAR_TRANS_OPEN_FAIL = 1773 
	#
	# MessageId: RPC_X_SS_CHAR_TRANS_SHORT_FILE
	#
	# MessageText:
	#
	# The file containing the character translation table has fewer than 512 bytes.
	#
	RPC_X_SS_CHAR_TRANS_SHORT_FILE = 1774 
	#
	# MessageId: RPC_X_SS_IN_NULL_CONTEXT
	#
	# MessageText:
	#
	# A null context handle was passed from the client to the host during a remote procedure call.
	#
	RPC_X_SS_IN_NULL_CONTEXT = 1775 
	#
	# MessageId: RPC_X_SS_CONTEXT_DAMAGED
	#
	# MessageText:
	#
	# The context handle changed during a remote procedure call.
	#
	RPC_X_SS_CONTEXT_DAMAGED = 1777 
	#
	# MessageId: RPC_X_SS_HANDLES_MISMATCH
	#
	# MessageText:
	#
	# The binding handles passed to a remote procedure call do not match.
	#
	RPC_X_SS_HANDLES_MISMATCH = 1778 
	#
	# MessageId: RPC_X_SS_CANNOT_GET_CALL_HANDLE
	#
	# MessageText:
	#
	# The stub is unable to get the remote procedure call handle.
	#
	RPC_X_SS_CANNOT_GET_CALL_HANDLE = 1779 
	#
	# MessageId: RPC_X_NULL_REF_POINTER
	#
	# MessageText:
	#
	# A null reference pointer was passed to the stub.
	#
	RPC_X_NULL_REF_POINTER = 1780 
	#
	# MessageId: RPC_X_ENUM_VALUE_OUT_OF_RANGE
	#
	# MessageText:
	#
	# The enumeration value is out of range.
	#
	RPC_X_ENUM_VALUE_OUT_OF_RANGE = 1781 
	#
	# MessageId: RPC_X_BYTE_COUNT_TOO_SMALL
	#
	# MessageText:
	#
	# The byte count is too small.
	#
	RPC_X_BYTE_COUNT_TOO_SMALL = 1782 
	#
	# MessageId: RPC_X_BAD_STUB_DATA
	#
	# MessageText:
	#
	# The stub received bad data.
	#
	RPC_X_BAD_STUB_DATA = 1783 
	#
	# MessageId: ERROR_INVALID_USER_BUFFER
	#
	# MessageText:
	#
	# The supplied user buffer is not valid for the requested operation.
	#
	ERROR_INVALID_USER_BUFFER = 1784 
	#
	# MessageId: ERROR_UNRECOGNIZED_MEDIA
	#
	# MessageText:
	#
	# The disk media is not recognized. It may not be formatted.
	#
	ERROR_UNRECOGNIZED_MEDIA = 1785 
	#
	# MessageId: ERROR_NO_TRUST_LSA_SECRET
	#
	# MessageText:
	#
	# The workstation does not have a trust secret.
	#
	ERROR_NO_TRUST_LSA_SECRET = 1786 
	#
	# MessageId: ERROR_NO_TRUST_SAM_ACCOUNT
	#
	# MessageText:
	#
	# The security database on the server does not have a computer account for this workstation trust relationship.
	#
	ERROR_NO_TRUST_SAM_ACCOUNT = 1787 
	#
	# MessageId: ERROR_TRUSTED_DOMAIN_FAILURE
	#
	# MessageText:
	#
	# The trust relationship between the primary domain and the trusted domain failed.
	#
	ERROR_TRUSTED_DOMAIN_FAILURE = 1788 
	#
	# MessageId: ERROR_TRUSTED_RELATIONSHIP_FAILURE
	#
	# MessageText:
	#
	# The trust relationship between this workstation and the primary domain failed.
	#
	ERROR_TRUSTED_RELATIONSHIP_FAILURE = 1789 
	#
	# MessageId: ERROR_TRUST_FAILURE
	#
	# MessageText:
	#
	# The network logon failed.
	#
	ERROR_TRUST_FAILURE = 1790 
	#
	# MessageId: RPC_S_CALL_IN_PROGRESS
	#
	# MessageText:
	#
	# A remote procedure call is already in progress for this thread.
	#
	RPC_S_CALL_IN_PROGRESS = 1791 
	#
	# MessageId: ERROR_NETLOGON_NOT_STARTED
	#
	# MessageText:
	#
	# An attempt was made to logon, but the network logon service was not started.
	#
	ERROR_NETLOGON_NOT_STARTED = 1792 
	#
	# MessageId: ERROR_ACCOUNT_EXPIRED
	#
	# MessageText:
	#
	# The user's account has expired.
	#
	ERROR_ACCOUNT_EXPIRED = 1793 
	#
	# MessageId: ERROR_REDIRECTOR_HAS_OPEN_HANDLES
	#
	# MessageText:
	#
	# The redirector is in use and cannot be unloaded.
	#
	ERROR_REDIRECTOR_HAS_OPEN_HANDLES = 1794 
	#
	# MessageId: ERROR_PRINTER_DRIVER_ALREADY_INSTALLED
	#
	# MessageText:
	#
	# The specified printer driver is already installed.
	#
	ERROR_PRINTER_DRIVER_ALREADY_INSTALLED = 1795 
	#
	# MessageId: ERROR_UNKNOWN_PORT
	#
	# MessageText:
	#
	# The specified port is unknown.
	#
	ERROR_UNKNOWN_PORT = 1796 
	#
	# MessageId: ERROR_UNKNOWN_PRINTER_DRIVER
	#
	# MessageText:
	#
	# The printer driver is unknown.
	#
	ERROR_UNKNOWN_PRINTER_DRIVER = 1797 
	#
	# MessageId: ERROR_UNKNOWN_PRINTPROCESSOR
	#
	# MessageText:
	#
	# The print processor is unknown.
	#
	ERROR_UNKNOWN_PRINTPROCESSOR = 1798 
	#
	# MessageId: ERROR_INVALID_SEPARATOR_FILE
	#
	# MessageText:
	#
	# The specified separator file is invalid.
	#
	ERROR_INVALID_SEPARATOR_FILE = 1799 
	#
	# MessageId: ERROR_INVALID_PRIORITY
	#
	# MessageText:
	#
	# The specified priority is invalid.
	#
	ERROR_INVALID_PRIORITY = 1800 
	#
	# MessageId: ERROR_INVALID_PRINTER_NAME
	#
	# MessageText:
	#
	# The printer name is invalid.
	#
	ERROR_INVALID_PRINTER_NAME = 1801 
	#
	# MessageId: ERROR_PRINTER_ALREADY_EXISTS
	#
	# MessageText:
	#
	# The printer already exists.
	#
	ERROR_PRINTER_ALREADY_EXISTS = 1802 
	#
	# MessageId: ERROR_INVALID_PRINTER_COMMAND
	#
	# MessageText:
	#
	# The printer command is invalid.
	#
	ERROR_INVALID_PRINTER_COMMAND = 1803 
	#
	# MessageId: ERROR_INVALID_DATATYPE
	#
	# MessageText:
	#
	# The specified datatype is invalid.
	#
	ERROR_INVALID_DATATYPE = 1804 
	#
	# MessageId: ERROR_INVALID_ENVIRONMENT
	#
	# MessageText:
	#
	# The environment specified is invalid.
	#
	ERROR_INVALID_ENVIRONMENT = 1805 
	#
	# MessageId: RPC_S_NO_MORE_BINDINGS
	#
	# MessageText:
	#
	# There are no more bindings.
	#
	RPC_S_NO_MORE_BINDINGS = 1806 
	#
	# MessageId: ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT
	#
	# MessageText:
	#
	# The account used is an interdomain trust account. Use your global user account or local user account to access this server.
	#
	ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT = 1807 
	#
	# MessageId: ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT
	#
	# MessageText:
	#
	# The account used is a computer account. Use your global user account or local user account to access this server.
	#
	ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT = 1808 
	#
	# MessageId: ERROR_NOLOGON_SERVER_TRUST_ACCOUNT
	#
	# MessageText:
	#
	# The account used is a server trust account. Use your global user account or local user account to access this server.
	#
	ERROR_NOLOGON_SERVER_TRUST_ACCOUNT = 1809 
	#
	# MessageId: ERROR_DOMAIN_TRUST_INCONSISTENT
	#
	# MessageText:
	#
	# The name or security ID (SID) of the domain specified is inconsistent with the trust information for that domain.
	#
	ERROR_DOMAIN_TRUST_INCONSISTENT = 1810 
	#
	# MessageId: ERROR_SERVER_HAS_OPEN_HANDLES
	#
	# MessageText:
	#
	# The server is in use and cannot be unloaded.
	#
	ERROR_SERVER_HAS_OPEN_HANDLES = 1811 
	#
	# MessageId: ERROR_RESOURCE_DATA_NOT_FOUND
	#
	# MessageText:
	#
	# The specified image file did not contain a resource section.
	#
	ERROR_RESOURCE_DATA_NOT_FOUND = 1812 
	#
	# MessageId: ERROR_RESOURCE_TYPE_NOT_FOUND
	#
	# MessageText:
	#
	# The specified resource type cannot be found in the image file.
	#
	ERROR_RESOURCE_TYPE_NOT_FOUND = 1813 
	#
	# MessageId: ERROR_RESOURCE_NAME_NOT_FOUND
	#
	# MessageText:
	#
	# The specified resource name cannot be found in the image file.
	#
	ERROR_RESOURCE_NAME_NOT_FOUND = 1814 
	#
	# MessageId: ERROR_RESOURCE_LANG_NOT_FOUND
	#
	# MessageText:
	#
	# The specified resource language ID cannot be found in the image file.
	#
	ERROR_RESOURCE_LANG_NOT_FOUND = 1815 
	#
	# MessageId: ERROR_NOT_ENOUGH_QUOTA
	#
	# MessageText:
	#
	# Not enough quota is available to process this command.
	#
	ERROR_NOT_ENOUGH_QUOTA = 1816 
	#
	# MessageId: RPC_S_NO_INTERFACES
	#
	# MessageText:
	#
	# No interfaces have been registered.
	#
	RPC_S_NO_INTERFACES = 1817 
	#
	# MessageId: RPC_S_CALL_CANCELLED
	#
	# MessageText:
	#
	# The remote procedure call was cancelled.
	#
	RPC_S_CALL_CANCELLED = 1818 
	#
	# MessageId: RPC_S_BINDING_INCOMPLETE
	#
	# MessageText:
	#
	# The binding handle does not contain all required information.
	#
	RPC_S_BINDING_INCOMPLETE = 1819 
	#
	# MessageId: RPC_S_COMM_FAILURE
	#
	# MessageText:
	#
	# A communications failure occurred during a remote procedure call.
	#
	RPC_S_COMM_FAILURE = 1820 
	#
	# MessageId: RPC_S_UNSUPPORTED_AUTHN_LEVEL
	#
	# MessageText:
	#
	# The requested authentication level is not supported.
	#
	RPC_S_UNSUPPORTED_AUTHN_LEVEL = 1821 
	#
	# MessageId: RPC_S_NO_PRINC_NAME
	#
	# MessageText:
	#
	# No principal name registered.
	#
	RPC_S_NO_PRINC_NAME = 1822 
	#
	# MessageId: RPC_S_NOT_RPC_ERROR
	#
	# MessageText:
	#
	# The error specified is not a valid Windows RPC error code.
	#
	RPC_S_NOT_RPC_ERROR = 1823 
	#
	# MessageId: RPC_S_UUID_LOCAL_ONLY
	#
	# MessageText:
	#
	# A UUID that is valid only on this computer has been allocated.
	#
	RPC_S_UUID_LOCAL_ONLY = 1824 
	#
	# MessageId: RPC_S_SEC_PKG_ERROR
	#
	# MessageText:
	#
	# A security package specific error occurred.
	#
	RPC_S_SEC_PKG_ERROR = 1825 
	#
	# MessageId: RPC_S_NOT_CANCELLED
	#
	# MessageText:
	#
	# Thread is not canceled.
	#
	RPC_S_NOT_CANCELLED = 1826 
	#
	# MessageId: RPC_X_INVALID_ES_ACTION
	#
	# MessageText:
	#
	# Invalid operation on the encoding/decoding handle.
	#
	RPC_X_INVALID_ES_ACTION = 1827 
	#
	# MessageId: RPC_X_WRONG_ES_VERSION
	#
	# MessageText:
	#
	# Incompatible version of the serializing package.
	#
	RPC_X_WRONG_ES_VERSION = 1828 
	#
	# MessageId: RPC_X_WRONG_STUB_VERSION
	#
	# MessageText:
	#
	# Incompatible version of the RPC stub.
	#
	RPC_X_WRONG_STUB_VERSION = 1829 
	#
	# MessageId: RPC_X_INVALID_PIPE_OBJECT
	#
	# MessageText:
	#
	# The RPC pipe object is invalid or corrupted.
	#
	RPC_X_INVALID_PIPE_OBJECT = 1830 
	#
	# MessageId: RPC_X_WRONG_PIPE_ORDER
	#
	# MessageText:
	#
	# An invalid operation was attempted on an RPC pipe object.
	#
	RPC_X_WRONG_PIPE_ORDER = 1831 
	#
	# MessageId: RPC_X_WRONG_PIPE_VERSION
	#
	# MessageText:
	#
	# Unsupported RPC pipe version.
	#
	RPC_X_WRONG_PIPE_VERSION = 1832 
	#
	# MessageId: RPC_S_COOKIE_AUTH_FAILED
	#
	# MessageText:
	#
	# HTTP proxy server rejected the connection because the cookie authentication failed.
	#
	RPC_S_COOKIE_AUTH_FAILED = 1833 
	#
	# MessageId: RPC_S_DO_NOT_DISTURB
	#
	# MessageText:
	#
	# The RPC server is suspended, and could not be resumed for this request. The call did not execute.
	#
	RPC_S_DO_NOT_DISTURB = 1834 
	#
	# MessageId: RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED
	#
	# MessageText:
	#
	# The RPC call contains too many handles to be transmitted in a single request.
	#
	RPC_S_SYSTEM_HANDLE_COUNT_EXCEEDED = 1835 
	#
	# MessageId: RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH
	#
	# MessageText:
	#
	# The RPC call contains a handle that differs from the declared handle type.
	#
	RPC_S_SYSTEM_HANDLE_TYPE_MISMATCH = 1836 
	#
	# MessageId: RPC_S_GROUP_MEMBER_NOT_FOUND
	#
	# MessageText:
	#
	# The group member was not found.
	#
	RPC_S_GROUP_MEMBER_NOT_FOUND = 1898 
	#
	# MessageId: EPT_S_CANT_CREATE
	#
	# MessageText:
	#
	# The endpoint mapper database entry could not be created.
	#
	EPT_S_CANT_CREATE = 1899 
	#
	# MessageId: RPC_S_INVALID_OBJECT
	#
	# MessageText:
	#
	# The object universal unique identifier (UUID) is the nil UUID.
	#
	RPC_S_INVALID_OBJECT = 1900 
	#
	# MessageId: ERROR_INVALID_TIME
	#
	# MessageText:
	#
	# The specified time is invalid.
	#
	ERROR_INVALID_TIME = 1901 
	#
	# MessageId: ERROR_INVALID_FORM_NAME
	#
	# MessageText:
	#
	# The specified form name is invalid.
	#
	ERROR_INVALID_FORM_NAME = 1902 
	#
	# MessageId: ERROR_INVALID_FORM_SIZE
	#
	# MessageText:
	#
	# The specified form size is invalid.
	#
	ERROR_INVALID_FORM_SIZE = 1903 
	#
	# MessageId: ERROR_ALREADY_WAITING
	#
	# MessageText:
	#
	# The specified printer handle is already being waited on
	#
	ERROR_ALREADY_WAITING = 1904 
	#
	# MessageId: ERROR_PRINTER_DELETED
	#
	# MessageText:
	#
	# The specified printer has been deleted.
	#
	ERROR_PRINTER_DELETED = 1905 
	#
	# MessageId: ERROR_INVALID_PRINTER_STATE
	#
	# MessageText:
	#
	# The state of the printer is invalid.
	#
	ERROR_INVALID_PRINTER_STATE = 1906 
	#
	# MessageId: ERROR_PASSWORD_MUST_CHANGE
	#
	# MessageText:
	#
	# The user's password must be changed before signing in.
	#
	ERROR_PASSWORD_MUST_CHANGE = 1907 
	#
	# MessageId: ERROR_DOMAIN_CONTROLLER_NOT_FOUND
	#
	# MessageText:
	#
	# Could not find the domain controller for this domain.
	#
	ERROR_DOMAIN_CONTROLLER_NOT_FOUND = 1908 
	#
	# MessageId: ERROR_ACCOUNT_LOCKED_OUT
	#
	# MessageText:
	#
	# The referenced account is currently locked out and may not be logged on to.
	#
	ERROR_ACCOUNT_LOCKED_OUT = 1909 
	#
	# MessageId: OR_INVALID_OXID
	#
	# MessageText:
	#
	# The object exporter specified was not found.
	#
	OR_INVALID_OXID = 1910 
	#
	# MessageId: OR_INVALID_OID
	#
	# MessageText:
	#
	# The object specified was not found.
	#
	OR_INVALID_OID = 1911 
	#
	# MessageId: OR_INVALID_SET
	#
	# MessageText:
	#
	# The object resolver set specified was not found.
	#
	OR_INVALID_SET = 1912 
	#
	# MessageId: RPC_S_SEND_INCOMPLETE
	#
	# MessageText:
	#
	# Some data remains to be sent in the request buffer.
	#
	RPC_S_SEND_INCOMPLETE = 1913 
	#
	# MessageId: RPC_S_INVALID_ASYNC_HANDLE
	#
	# MessageText:
	#
	# Invalid asynchronous remote procedure call handle.
	#
	RPC_S_INVALID_ASYNC_HANDLE = 1914 
	#
	# MessageId: RPC_S_INVALID_ASYNC_CALL
	#
	# MessageText:
	#
	# Invalid asynchronous RPC call handle for this operation.
	#
	RPC_S_INVALID_ASYNC_CALL = 1915 
	#
	# MessageId: RPC_X_PIPE_CLOSED
	#
	# MessageText:
	#
	# The RPC pipe object has already been closed.
	#
	RPC_X_PIPE_CLOSED = 1916 
	#
	# MessageId: RPC_X_PIPE_DISCIPLINE_ERROR
	#
	# MessageText:
	#
	# The RPC call completed before all pipes were processed.
	#
	RPC_X_PIPE_DISCIPLINE_ERROR = 1917 
	#
	# MessageId: RPC_X_PIPE_EMPTY
	#
	# MessageText:
	#
	# No more data is available from the RPC pipe.
	#
	RPC_X_PIPE_EMPTY = 1918 
	#
	# MessageId: ERROR_NO_SITENAME
	#
	# MessageText:
	#
	# No site name is available for this machine.
	#
	ERROR_NO_SITENAME = 1919 
	#
	# MessageId: ERROR_CANT_ACCESS_FILE
	#
	# MessageText:
	#
	# The file cannot be accessed by the system.
	#
	ERROR_CANT_ACCESS_FILE = 1920 
	#
	# MessageId: ERROR_CANT_RESOLVE_FILENAME
	#
	# MessageText:
	#
	# The name of the file cannot be resolved by the system.
	#
	ERROR_CANT_RESOLVE_FILENAME = 1921 
	#
	# MessageId: RPC_S_ENTRY_TYPE_MISMATCH
	#
	# MessageText:
	#
	# The entry is not of the expected type.
	#
	RPC_S_ENTRY_TYPE_MISMATCH = 1922 
	#
	# MessageId: RPC_S_NOT_ALL_OBJS_EXPORTED
	#
	# MessageText:
	#
	# Not all object UUIDs could be exported to the specified entry.
	#
	RPC_S_NOT_ALL_OBJS_EXPORTED = 1923 
	#
	# MessageId: RPC_S_INTERFACE_NOT_EXPORTED
	#
	# MessageText:
	#
	# Interface could not be exported to the specified entry.
	#
	RPC_S_INTERFACE_NOT_EXPORTED = 1924 
	#
	# MessageId: RPC_S_PROFILE_NOT_ADDED
	#
	# MessageText:
	#
	# The specified profile entry could not be added.
	#
	RPC_S_PROFILE_NOT_ADDED = 1925 
	#
	# MessageId: RPC_S_PRF_ELT_NOT_ADDED
	#
	# MessageText:
	#
	# The specified profile element could not be added.
	#
	RPC_S_PRF_ELT_NOT_ADDED = 1926 
	#
	# MessageId: RPC_S_PRF_ELT_NOT_REMOVED
	#
	# MessageText:
	#
	# The specified profile element could not be removed.
	#
	RPC_S_PRF_ELT_NOT_REMOVED = 1927 
	#
	# MessageId: RPC_S_GRP_ELT_NOT_ADDED
	#
	# MessageText:
	#
	# The group element could not be added.
	#
	RPC_S_GRP_ELT_NOT_ADDED = 1928 
	#
	# MessageId: RPC_S_GRP_ELT_NOT_REMOVED
	#
	# MessageText:
	#
	# The group element could not be removed.
	#
	RPC_S_GRP_ELT_NOT_REMOVED = 1929 
	#
	# MessageId: ERROR_KM_DRIVER_BLOCKED
	#
	# MessageText:
	#
	# The printer driver is not compatible with a policy enabled on your computer that blocks NT 4.0 drivers.
	#
	ERROR_KM_DRIVER_BLOCKED = 1930 
	#
	# MessageId: ERROR_CONTEXT_EXPIRED
	#
	# MessageText:
	#
	# The context has expired and can no longer be used.
	#
	ERROR_CONTEXT_EXPIRED = 1931 
	#
	# MessageId: ERROR_PER_USER_TRUST_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# The current user's delegated trust creation quota has been exceeded.
	#
	ERROR_PER_USER_TRUST_QUOTA_EXCEEDED = 1932 
	#
	# MessageId: ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# The total delegated trust creation quota has been exceeded.
	#
	ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED = 1933 
	#
	# MessageId: ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED
	#
	# MessageText:
	#
	# The current user's delegated trust deletion quota has been exceeded.
	#
	ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED = 1934 
	#
	# MessageId: ERROR_AUTHENTICATION_FIREWALL_FAILED
	#
	# MessageText:
	#
	# The computer you are signing into is protected by an authentication firewall. The specified account is not allowed to authenticate to the computer.
	#
	ERROR_AUTHENTICATION_FIREWALL_FAILED = 1935 
	#
	# MessageId: ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED
	#
	# MessageText:
	#
	# Remote connections to the Print Spooler are blocked by a policy set on your machine.
	#
	ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED = 1936 
	#
	# MessageId: ERROR_NTLM_BLOCKED
	#
	# MessageText:
	#
	# Authentication failed because NTLM authentication has been disabled.
	#
	ERROR_NTLM_BLOCKED = 1937 
	#
	# MessageId: ERROR_PASSWORD_CHANGE_REQUIRED
	#
	# MessageText:
	#
	# Logon Failure: EAS policy requires that the user change their password before this operation can be performed.
	#
	ERROR_PASSWORD_CHANGE_REQUIRED = 1938 
	#
	# MessageId: ERROR_LOST_MODE_LOGON_RESTRICTION
	#
	# MessageText:
	#
	# An administrator has restricted sign in. To sign in, make sure your device is connected to the Internet, and have your administrator sign in first.
	#
	ERROR_LOST_MODE_LOGON_RESTRICTION = 1939 
	#########################/
	#                                               #
	#              OpenGL Error codes               #
	#                                               #
	#                 2000 to 2009                  #
	#########################/
	#
	# MessageId: ERROR_INVALID_PIXEL_FORMAT
	#
	# MessageText:
	#
	# The pixel format is invalid.
	#
	ERROR_INVALID_PIXEL_FORMAT = 2000 
	#
	# MessageId: ERROR_BAD_DRIVER
	#
	# MessageText:
	#
	# The specified driver is invalid.
	#
	ERROR_BAD_DRIVER = 2001 
	#
	# MessageId: ERROR_INVALID_WINDOW_STYLE
	#
	# MessageText:
	#
	# The window style or class attribute is invalid for this operation.
	#
	ERROR_INVALID_WINDOW_STYLE = 2002 
	#
	# MessageId: ERROR_METAFILE_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The requested metafile operation is not supported.
	#
	ERROR_METAFILE_NOT_SUPPORTED = 2003 
	#
	# MessageId: ERROR_TRANSFORM_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The requested transformation operation is not supported.
	#
	ERROR_TRANSFORM_NOT_SUPPORTED = 2004 
	#
	# MessageId: ERROR_CLIPPING_NOT_SUPPORTED
	#
	# MessageText:
	#
	# The requested clipping operation is not supported.
	#
	ERROR_CLIPPING_NOT_SUPPORTED = 2005 
	#########################/
	#                                               #
	#       Image Color Management Error codes      #
	#                                               #
	#                 2010 to 2049                  #
	#########################/
	#
	# MessageId: ERROR_INVALID_CMM
	#
	# MessageText:
	#
	# The specified color management module is invalid.
	#
	ERROR_INVALID_CMM = 2010 
	#
	# MessageId: ERROR_INVALID_PROFILE
	#
	# MessageText:
	#
	# The specified color profile is invalid.
	#
	ERROR_INVALID_PROFILE = 2011 
	#
	# MessageId: ERROR_TAG_NOT_FOUND
	#
	# MessageText:
	#
	# The specified tag was not found.
	#
	ERROR_TAG_NOT_FOUND = 2012 
	#
	# MessageId: ERROR_TAG_NOT_PRESENT
	#
	# MessageText:
	#
	# A required tag is not present.
	#
	ERROR_TAG_NOT_PRESENT = 2013 
	#
	# MessageId: ERROR_DUPLICATE_TAG
	#
	# MessageText:
	#
	# The specified tag is already present.
	#
	ERROR_DUPLICATE_TAG = 2014 
	#
	# MessageId: ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE
	#
	# MessageText:
	#
	# The specified color profile is not associated with the specified device.
	#
	ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE = 2015 
	#
	# MessageId: ERROR_PROFILE_NOT_FOUND
	#
	# MessageText:
	#
	# The specified color profile was not found.
	#
	ERROR_PROFILE_NOT_FOUND = 2016 
	#
	# MessageId: ERROR_INVALID_COLORSPACE
	#
	# MessageText:
	#
	# The specified color space is invalid.
	#
	ERROR_INVALID_COLORSPACE = 2017 
	#
	# MessageId: ERROR_ICM_NOT_ENABLED
	#
	# MessageText:
	#
	# Image Color Management is not enabled.
	#
	ERROR_ICM_NOT_ENABLED = 2018 
	#
	# MessageId: ERROR_DELETING_ICM_XFORM
	#
	# MessageText:
	#
	# There was an error while deleting the color transform.
	#
	ERROR_DELETING_ICM_XFORM = 2019 
	#
	# MessageId: ERROR_INVALID_TRANSFORM
	#
	# MessageText:
	#
	# The specified color transform is invalid.
	#
	ERROR_INVALID_TRANSFORM = 2020 
	#
	# MessageId: ERROR_COLORSPACE_MISMATCH
	#
	# MessageText:
	#
	# The specified transform does not match the bitmap's color space.
	#
	ERROR_COLORSPACE_MISMATCH = 2021 
	#
	# MessageId: ERROR_INVALID_COLORINDEX
	#
	# MessageText:
	#
	# The specified named color index is not present in the profile.
	#
	ERROR_INVALID_COLORINDEX = 2022 
	#
	# MessageId: ERROR_PROFILE_DOES_NOT_MATCH_DEVICE
	#
	# MessageText:
	#
	# The specified profile is intended for a device of a different type than the specified device.
	#
	ERROR_PROFILE_DOES_NOT_MATCH_DEVICE = 2023 
	#########################/
	#                                               #
	#             Winnet32 Error codes              #
	#                                               #
	#                 2100 to 2999                  #
	#                                               #
	# The range 2100 through 2999 is reserved for   #
	# network status codes. See lmerr.h for a       #
	# complete listing                              #
	#########################/
	#
	# MessageId: ERROR_CONNECTED_OTHER_PASSWORD
	#
	# MessageText:
	#
	# The network connection was made successfully, but the user had to be prompted for a password other than the one originally specified.
	#
	ERROR_CONNECTED_OTHER_PASSWORD = 2108 
	#
	# MessageId: ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT
	#
	# MessageText:
	#
	# The network connection was made successfully using default credentials.
	#
	ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT = 2109 
	#
	# MessageId: ERROR_BAD_USERNAME
	#
	# MessageText:
	#
	# The specified username is invalid.
	#
	ERROR_BAD_USERNAME = 2202 
	#
	# MessageId: ERROR_NOT_CONNECTED
	#
	# MessageText:
	#
	# This network connection does not exist.
	#
	ERROR_NOT_CONNECTED = 2250 
	#
	# MessageId: ERROR_OPEN_FILES
	#
	# MessageText:
	#
	# This network connection has files open or requests pending.
	#
	ERROR_OPEN_FILES = 2401 
	#
	# MessageId: ERROR_ACTIVE_CONNECTIONS
	#
	# MessageText:
	#
	# Active connections still exist.
	#
	ERROR_ACTIVE_CONNECTIONS = 2402 
	#
	# MessageId: ERROR_DEVICE_IN_USE
	#
	# MessageText:
	#
	# The device is in use by an active process and cannot be disconnected.
	#
	ERROR_DEVICE_IN_USE = 2404 
	#########################/
	#                                               #
	#           Win32 Spooler Error codes           #
	#                                               #
	#                 3000 to 3049                  #
	#########################/
	#
	# MessageId: ERROR_UNKNOWN_PRINT_MONITOR
	#
	# MessageText:
	#
	# The specified print monitor is unknown.
	#
	ERROR_UNKNOWN_PRINT_MONITOR = 3000 
	#
	# MessageId: ERROR_PRINTER_DRIVER_IN_USE
	#
	# MessageText:
	#
	# The specified printer driver is currently in use.
	#
	ERROR_PRINTER_DRIVER_IN_USE = 3001 
	#
	# MessageId: ERROR_SPOOL_FILE_NOT_FOUND
	#
	# MessageText:
	#
	# The spool file was not found.
	#
	ERROR_SPOOL_FILE_NOT_FOUND = 3002 
	#
	# MessageId: ERROR_SPL_NO_STARTDOC
	#
	# MessageText:
	#
	# A StartDocPrinter call was not issued.
	#
	ERROR_SPL_NO_STARTDOC = 3003 
	#
	# MessageId: ERROR_SPL_NO_ADDJOB
	#
	# MessageText:
	#
	# An AddJob call was not issued.
	#
	ERROR_SPL_NO_ADDJOB = 3004 
	#
	# MessageId: ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED
	#
	# MessageText:
	#
	# The specified print processor has already been installed.
	#
	ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED = 3005 
	#
	# MessageId: ERROR_PRINT_MONITOR_ALREADY_INSTALLED
	#
	# MessageText:
	#
	# The specified print monitor has already been installed.
	#
	ERROR_PRINT_MONITOR_ALREADY_INSTALLED = 3006 
	#
	# MessageId: ERROR_INVALID_PRINT_MONITOR
	#
	# MessageText:
	#
	# The specified print monitor does not have the required functions.
	#
	ERROR_INVALID_PRINT_MONITOR = 3007 
	#
	# MessageId: ERROR_PRINT_MONITOR_IN_USE
	#
	# MessageText:
	#
	# The specified print monitor is currently in use.
	#
	ERROR_PRINT_MONITOR_IN_USE = 3008 
	#
	# MessageId: ERROR_PRINTER_HAS_JOBS_QUEUED
	#
	# MessageText:
	#
	# The requested operation is not allowed when there are jobs queued to the printer.
	#
	ERROR_PRINTER_HAS_JOBS_QUEUED = 3009 
	#
	# MessageId: ERROR_SUCCESS_REBOOT_REQUIRED
	#
	# MessageText:
	#
	# The requested operation is successful. Changes will not be effective until the system is rebooted.
	#
	ERROR_SUCCESS_REBOOT_REQUIRED = 3010 
	#
	# MessageId: ERROR_SUCCESS_RESTART_REQUIRED
	#
	# MessageText:
	#
	# The requested operation is successful. Changes will not be effective until the service is restarted.
	#
	ERROR_SUCCESS_RESTART_REQUIRED = 3011 
	#
	# MessageId: ERROR_PRINTER_NOT_FOUND
	#
	# MessageText:
	#
	# No printers were found.
	#
	ERROR_PRINTER_NOT_FOUND = 3012 
	#
	# MessageId: ERROR_PRINTER_DRIVER_WARNED
	#
	# MessageText:
	#
	# The printer driver is known to be unreliable.
	#
	ERROR_PRINTER_DRIVER_WARNED = 3013 
	#
	# MessageId: ERROR_PRINTER_DRIVER_BLOCKED
	#
	# MessageText:
	#
	# The printer driver is known to harm the system.
	#
	ERROR_PRINTER_DRIVER_BLOCKED = 3014 
	#
	# MessageId: ERROR_PRINTER_DRIVER_PACKAGE_IN_USE
	#
	# MessageText:
	#
	# The specified printer driver package is currently in use.
	#
	ERROR_PRINTER_DRIVER_PACKAGE_IN_USE = 3015 
	#
	# MessageId: ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND
	#
	# MessageText:
	#
	# Unable to find a core driver package that is required by the printer driver package.
	#
	ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND = 3016 
	#
	# MessageId: ERROR_FAIL_REBOOT_REQUIRED
	#
	# MessageText:
	#
	# The requested operation failed. A system reboot is required to roll back changes made.
	#
	ERROR_FAIL_REBOOT_REQUIRED = 3017 
	#
	# MessageId: ERROR_FAIL_REBOOT_INITIATED
	#
	# MessageText:
	#
	# The requested operation failed. A system reboot has been initiated to roll back changes made.
	#
	ERROR_FAIL_REBOOT_INITIATED = 3018 
	#
	# MessageId: ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED
	#
	# MessageText:
	#
	# The specified printer driver was not found on the system and needs to be downloaded.
	#
	ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED = 3019 
	#
	# MessageId: ERROR_PRINT_JOB_RESTART_REQUIRED
	#
	# MessageText:
	#
	# The requested print job has failed to print. A print system update requires the job to be resubmitted.
	#
	ERROR_PRINT_JOB_RESTART_REQUIRED = 3020 
	#
	# MessageId: ERROR_INVALID_PRINTER_DRIVER_MANIFEST
	#
	# MessageText:
	#
	# The printer driver does not contain a valid manifest, or contains too many manifests.
	#
	ERROR_INVALID_PRINTER_DRIVER_MANIFEST = 3021 
	#
	# MessageId: ERROR_PRINTER_NOT_SHAREABLE
	#
	# MessageText:
	#
	# The specified printer cannot be shared.
	#
	ERROR_PRINTER_NOT_SHAREABLE = 3022 
	#########################/
	#                                               #
	#           CopyFile ext. Error codes           #
	#                                               #
	#                 3050 to 3059                  #
	#########################/
	#
	# MessageId: ERROR_REQUEST_PAUSED
	#
	# MessageText:
	#
	# The operation was paused.
	#
	ERROR_REQUEST_PAUSED = 3050 
	#########################/
	#                                               #
	#           AppExec Error codes                 #
	#                                               #
	#                 3060 to 3079                  #
	#########################/
	#
	# MessageId: ERROR_APPEXEC_CONDITION_NOT_SATISFIED
	#
	# MessageText:
	#
	# The condition supplied for the app execution request was not satisfied, so the request was not performed.
	#
	ERROR_APPEXEC_CONDITION_NOT_SATISFIED = 3060 
	#
	# MessageId: ERROR_APPEXEC_HANDLE_INVALIDATED
	#
	# MessageText:
	#
	# The supplied handle has been invalidated and may not be used for the requested operation.
	#
	ERROR_APPEXEC_HANDLE_INVALIDATED = 3061 
	#
	# MessageId: ERROR_APPEXEC_INVALID_HOST_GENERATION
	#
	# MessageText:
	#
	# The supplied host generation has been invalidated and may not be used for the requested operation.
	#
	ERROR_APPEXEC_INVALID_HOST_GENERATION = 3062 
	#
	# MessageId: ERROR_APPEXEC_UNEXPECTED_PROCESS_REGISTRATION
	#
	# MessageText:
	#
	# An attempt to register a process failed because the target host was not in a valid state to receive process registrations.
	#
	ERROR_APPEXEC_UNEXPECTED_PROCESS_REGISTRATION = 3063 
	#
	# MessageId: ERROR_APPEXEC_INVALID_HOST_STATE
	#
	# MessageText:
	#
	# The host is not in a valid state to support the execution request.
	#
	ERROR_APPEXEC_INVALID_HOST_STATE = 3064 
	#
	# MessageId: ERROR_APPEXEC_NO_DONOR
	#
	# MessageText:
	#
	# The operation was not completed because a required resource donor was not found for the host.
	#
	ERROR_APPEXEC_NO_DONOR = 3065 
	#
	# MessageId: ERROR_APPEXEC_HOST_ID_MISMATCH
	#
	# MessageText:
	#
	# The operation was not completed because an unexpected host ID was encountered.
	#
	ERROR_APPEXEC_HOST_ID_MISMATCH = 3066 
	#
	# MessageId: ERROR_APPEXEC_UNKNOWN_USER
	#
	# MessageText:
	#
	# The operation was not completed because the specified user was not known to the service.
	#
	ERROR_APPEXEC_UNKNOWN_USER = 3067 
	#########################/
	#                                               #
	#                  Available                    #
	#                                               #
	#                 3080 to 3199                  #
	#########################/
	#
	#               the message range
	#                 3200 to 3299
	#      is reserved and used in isolation lib
	#
	#########################/
	#                                               #
	#                  Available                    #
	#                                               #
	#                 3300 to 3899                  #
	#########################/
	#########################/
	#                                               #
	#                IO Error Codes                 #
	#                                               #
	#                 3900 to 3999                  #
	#########################/
	#
	# MessageId: ERROR_IO_REISSUE_AS_CACHED
	#
	# MessageText:
	#
	# Reissue the given operation as a cached IO operation
	#
	ERROR_IO_REISSUE_AS_CACHED = 3950 
	#########################/
	#                                               #
	#                Wins Error codes               #
	#                                               #
	#                 4000 to 4049                  #
	#########################/
	#
	# MessageId: ERROR_WINS_INTERNAL
	#
	# MessageText:
	#
	# WINS encountered an error while processing the command.
	#
	ERROR_WINS_INTERNAL = 4000 
	#
	# MessageId: ERROR_CAN_NOT_DEL_LOCAL_WINS
	#
	# MessageText:
	#
	# The local WINS cannot be deleted.
	#
	ERROR_CAN_NOT_DEL_LOCAL_WINS = 4001 
	#
	# MessageId: ERROR_STATIC_INIT
	#
	# MessageText:
	#
	# The importation from the file failed.
	#
	ERROR_STATIC_INIT = 4002 
	#
	# MessageId: ERROR_INC_BACKUP
	#
	# MessageText:
	#
	# The backup failed. Was a full backup done before?
	#
	ERROR_INC_BACKUP = 4003 
	#
	# MessageId: ERROR_FULL_BACKUP
	#
	# MessageText:
	#
	# The backup failed. Check the directory to which you are backing the database.
	#
	ERROR_FULL_BACKUP = 4004 
	#
	# MessageId: ERROR_REC_NON_EXISTENT
	#
	# MessageText:
	#
	# The name does not exist in the WINS database.
	#
	ERROR_REC_NON_EXISTENT = 4005 
	#
	# MessageId: ERROR_RPL_NOT_ALLOWED
	#
	# MessageText:
	#
	# Replication with a nonconfigured partner is not allowed.
	#
	ERROR_RPL_NOT_ALLOWED = 4006 
	#########################/
	#                                               #
	#              PeerDist Error codes             #
	#                                               #
	#                 4050 to 4099                  #
	#########################/
	#
	# MessageId: PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED
	#
	# MessageText:
	#
	# The version of the supplied content information is not supported.
	#
	PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED = 4050 
	#
	# MessageId: PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO
	#
	# MessageText:
	#
	# The supplied content information is malformed.
	#
	PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO = 4051 
	#
	# MessageId: PEERDIST_ERROR_MISSING_DATA
	#
	# MessageText:
	#
	# The requested data cannot be found in local or peer caches.
	#
	PEERDIST_ERROR_MISSING_DATA = 4052 
	#
	# MessageId: PEERDIST_ERROR_NO_MORE
	#
	# MessageText:
	#
	# No more data is available or required.
	#
	PEERDIST_ERROR_NO_MORE = 4053 
	#
	# MessageId: PEERDIST_ERROR_NOT_INITIALIZED
	#
	# MessageText:
	#
	# The supplied object has not been initialized.
	#
	PEERDIST_ERROR_NOT_INITIALIZED = 4054 
	#
	# MessageId: PEERDIST_ERROR_ALREADY_INITIALIZED
	#
	# MessageText:
	#
	# The supplied object has already been initialized.
	#
	PEERDIST_ERROR_ALREADY_INITIALIZED = 4055 
	#
	# MessageId: PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS
	#
	# MessageText:
	#
	# A shutdown operation is already in progress.
	#
	PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS = 4056 
	#
	# MessageId: PEERDIST_ERROR_INVALIDATED
	#
	# MessageText:
	#
	# The supplied object has already been invalidated.
	#
	PEERDIST_ERROR_INVALIDATED = 4057 
	#
	# MessageId: PEERDIST_ERROR_ALREADY_EXISTS
	#
	# MessageText:
	#
	# An element already exists and was not replaced.
	#
	PEERDIST_ERROR_ALREADY_EXISTS = 4058 
	#
	# MessageId: PEERDIST_ERROR_OPERATION_NOTFOUND
	#
	# MessageText:
	#
	# Can not cancel the requested operation as it has already been completed.
	#
	PEERDIST_ERROR_OPERATION_NOTFOUND = 4059 
	#
	# MessageId: PEERDIST_ERROR_ALREADY_COMPLETED
	#
	# MessageText:
	#
	# Can not perform the requested operation because it has already been carried out.
	#
	PEERDIST_ERROR_ALREADY_COMPLETED = 4060 
	#
	# MessageId: PEERDIST_ERROR_OUT_OF_BOUNDS
	#
	# MessageText:
	#
	# An operation accessed data beyond the bounds of valid data.
	#
	PEERDIST_ERROR_OUT_OF_BOUNDS = 4061 
	#
	# MessageId: PEERDIST_ERROR_VERSION_UNSUPPORTED
	#
	# MessageText:
	#
	# The requested version is not supported.
	#
	PEERDIST_ERROR_VERSION_UNSUPPORTED = 4062 
	#
	# MessageId: PEERDIST_ERROR_INVALID_CONFIGURATION
	#
	# MessageText:
	#
	# A configuration value is invalid.
	#
	PEERDIST_ERROR_INVALID_CONFIGURATION = 4063 
	#
	# MessageId: PEERDIST_ERROR_NOT_LICENSED
	#
	# MessageText:
	#
	# The SKU is not licensed.
	#
	PEERDIST_ERROR_NOT_LICENSED = 4064 
	#
	# MessageId: PEERDIST_ERROR_SERVICE_UNAVAILABLE
	#
	# MessageText:
	#
	# PeerDist Service is still initializing and will be available shortly.
	#
	PEERDIST_ERROR_SERVICE_UNAVAILABLE = 4065 
	#
	# MessageId: PEERDIST_ERROR_TRUST_FAILURE
	#
	# MessageText:
	#
	# Communication with one or more computers will be temporarily blocked due to recent errors.
	#
	PEERDIST_ERROR_TRUST_FAILURE = 4066 
	#########################/
	#                                               #
	#               DHCP Error codes                #
	#                                               #
	#                 4100 to 4149                  #
	#########################/
	#
	# MessageId: ERROR_DHCP_ADDRESS_CONFLICT
	#
	# MessageText:
	#
	# The DHCP client has obtained an IP address that is already in use on the network. The local interface will be disabled until the DHCP client can obtain a new address.
	#
	ERROR_DHCP_ADDRESS_CONFLICT = 4100 
	#########################/
	#                                               #
	#                  Available                    #
	#                                               #
	#                 4150 to 4199                  #
	#########################/
	#########################/
	#                                               #
	#               WMI Error codes                 #
	#                                               #
	#                 4200 to 4249                  #
	#########################/
	#
	# MessageId: ERROR_WMI_GUID_NOT_FOUND
	#
	# MessageText:
	#
	# The GUID passed was not recognized as valid by a WMI data provider.
	#
	ERROR_WMI_GUID_NOT_FOUND = 4200 
	#
	# MessageId: ERROR_WMI_INSTANCE_NOT_FOUND
	#
	# MessageText:
	#
	# The instance name passed was not recognized as valid by a WMI data provider.
	#
	ERROR_WMI_INSTANCE_NOT_FOUND = 4201 
	#
	# MessageId: ERROR_WMI_ITEMID_NOT_FOUND
	#
	# MessageText:
	#
	# The data item ID passed was not recognized as valid by a WMI data provider.
	#
	ERROR_WMI_ITEMID_NOT_FOUND = 4202 
	#
	# MessageId: ERROR_WMI_TRY_AGAIN
	#
	# MessageText:
	#
	# The WMI request could not be completed and should be retried.
	#
	ERROR_WMI_TRY_AGAIN = 4203 
	#
	# MessageId: ERROR_WMI_DP_NOT_FOUND
	#
	# MessageText:
	#
	# The WMI data provider could not be located.
	#
	ERROR_WMI_DP_NOT_FOUND = 4204 
	#
	# MessageId: ERROR_WMI_UNRESOLVED_INSTANCE_REF
	#
	# MessageText:
	#
	# The WMI data provider references an instance set that has not been registered.
	#
	ERROR_WMI_UNRESOLVED_INSTANCE_REF = 4205 
	#
	# MessageId: ERROR_WMI_ALREADY_ENABLED
	#
	# MessageText:
	#
	# The WMI data block or event notification has already been enabled.
	#
	ERROR_WMI_ALREADY_ENABLED = 4206 
	#
	# MessageId: ERROR_WMI_GUID_DISCONNECTED
	#
	# MessageText:
	#
	# The WMI data block is no longer available.
	#
	ERROR_WMI_GUID_DISCONNECTED = 4207 
	#
	# MessageId: ERROR_WMI_SERVER_UNAVAILABLE
	#
	# MessageText:
	#
	# The WMI data service is not available.
	#
	ERROR_WMI_SERVER_UNAVAILABLE = 4208 
	#
	# MessageId: ERROR_WMI_DP_FAILED
	#
	# MessageText:
	#
	# The WMI data provider failed to carry out the request.
	#
	ERROR_WMI_DP_FAILED = 4209 
	#
	# MessageId: ERROR_WMI_INVALID_MOF
	#
	# MessageText:
	#
	# The WMI MOF information is not valid.
	#
	ERROR_WMI_INVALID_MOF = 4210 
	#
	# MessageId: ERROR_WMI_INVALID_REGINFO
	#
	# MessageText:
	#
	# The WMI registration information is not valid.
	#
	ERROR_WMI_INVALID_REGINFO = 4211 
	#
	# MessageId: ERROR_WMI_ALREADY_DISABLED
	#
	# MessageText:
	#
	# The WMI data block or event notification has already been disabled.
	#
	ERROR_WMI_ALREADY_DISABLED = 4212 
	#
	# MessageId: ERROR_WMI_READ_ONLY
	#
	# MessageText:
	#
	# The WMI data item or data block is read only.
	#
	ERROR_WMI_READ_ONLY = 4213 
	#
	# MessageId: ERROR_WMI_SET_FAILURE
	#
	# MessageText:
	#
	# The WMI data item or data block could not be changed.
	#
	ERROR_WMI_SET_FAILURE = 4214 
