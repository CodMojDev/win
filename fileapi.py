"""
 *********************************************************************************
 *                                                                               *
 * FileApi.h -- ApiSet Contract for api-ms-win-core-file-l1                      *
 *                                                                               *
 * Copyright(c) Microsoft Corporation. All rights reserved.                      *
 *                                                                               *
 *********************************************************************************
"""

from . import cpreproc

from .defbase import *

from .winbase import *

from .minwindef import *

if cpreproc.pragma_once("_APISETFILE_"):
    kernel32 = W_WinDLL("kernel32.dll")

    # REGION *** Application Family or OneCore Family or Games Family ***

    #
    # Constants
    #
    CREATE_NEW = 1
    CREATE_ALWAYS = 2
    OPEN_EXISTING = 3
    OPEN_ALWAYS = 4
    TRUNCATE_EXISTING = 5
    INVALID_FILE_SIZE = DWORD(0xFFFFFFFF).value
    INVALID_SET_FILE_POINTER = DWORD(-1).value
    INVALID_FILE_ATTRIBUTES = DWORD(-1).value
    CompareFileTime = declare(kernel32.CompareFileTime, LONG, PFILETIME, PFILETIME)
    CreateDirectoryA = declare(kernel32.CreateDirectoryA, BOOL, LPCSTR, LPSECURITY_ATTRIBUTES)
    CreateDirectoryW = declare(kernel32.CreateDirectoryW, BOOL, LPCWSTR, LPSECURITY_ATTRIBUTES)
    CreateDirectory = unicode(CreateDirectoryW, CreateDirectoryA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    CreateFileA = declare(kernel32.CreateFileA, HANDLE, LPCSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE)
    CreateFileW = declare(kernel32.CreateFileW, HANDLE, LPCWSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE)
    CreateFile = unicode(CreateFileW, CreateFileA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    DefineDosDeviceA = declare(kernel32.DefineDosDeviceA, BOOL, DWORD, LPCSTR, LPCSTR)
    DefineDosDeviceW = declare(kernel32.DefineDosDeviceW, BOOL, DWORD, LPCWSTR, LPCWSTR)
    DefineDosDevice = unicode(DefineDosDeviceW, DefineDosDeviceA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    DeleteFileA = declare(kernel32.DeleteFileA, BOOL, LPCSTR)
    DeleteFileW = declare(kernel32.DeleteFileW, BOOL, LPCWSTR)
    DeleteFile = unicode(DeleteFileW, DeleteFileA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    DeleteVolumeMountPointA = declare(kernel32.DeleteVolumeMountPointA, BOOL, LPWSTR)
    DeleteVolumeMountPointW = declare(kernel32.DeleteVolumeMountPointW, BOOL, LPCWSTR)
    DeleteVolumeMountPoint = unicode(DeleteVolumeMountPointW, DeleteVolumeMountPointA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    FileTimeToLocalFileTime = declare(kernel32.FileTimeToLocalFileTime, BOOL, PFILETIME, LPFILETIME)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    FindClose = declare(kernel32.FindClose, BOOL, HANDLE)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    FindCloseChangeNotification = declare(kernel32.FindCloseChangeNotification, BOOL, HANDLE)
    FindFirstChangeNotificationA = declare(kernel32.FindFirstChangeNotificationA, HANDLE, LPCSTR, BOOL, DWORD)
    FindFirstChangeNotificationW = declare(kernel32.FindFirstChangeNotificationW, HANDLE, LPCWSTR, BOOL, DWORD)
    FindFirstChangeNotification = unicode(FindFirstChangeNotificationW, FindFirstChangeNotificationA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    FindFirstFileA = declare(kernel32.FindFirstFileA, HANDLE, LPCSTR, LPWIN32_FIND_DATAA)
    FindFirstFileW = declare(kernel32.FindFirstFileW, HANDLE, LPCWSTR, LPWIN32_FIND_DATAW)
    FindFirstFile = unicode(FindFirstFileW, FindFirstFileA)
    if cpreproc.getdef("_WINVER") >= 0x0400:
        FindFirstFileExA = declare(kernel32.FindFirstFileExA, HANDLE, LPCSTR, INT, LPVOID, INT, LPVOID, DWORD)
        FindFirstFileExW = declare(kernel32.FindFirstFileExW, HANDLE, LPCWSTR, INT, LPVOID, INT, LPVOID, DWORD)
    FindFirstFileEx = unicode(FindFirstFileExW, FindFirstFileExA)
    # !UNICODE
    # _WINVER >= 0x0400
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    FindFirstVolumeA = declare(kernel32.FindFirstVolumeA, HANDLE, LPSTR, DWORD)
    FindFirstVolumeW = declare(kernel32.FindFirstVolumeW, HANDLE, LPWSTR, DWORD)
    FindFirstVolume = unicode(FindFirstVolumeW, FindFirstVolumeA)
    FindNextChangeNotification = declare(kernel32.FindNextChangeNotification, BOOL, HANDLE)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    FindNextFileA = declare(kernel32.FindNextFileA, BOOL, HANDLE, LPWIN32_FIND_DATAA)
    FindNextFileW = declare(kernel32.FindNextFileW, BOOL, HANDLE, LPWIN32_FIND_DATAW)
    FindNextFile = unicode(FindNextFileW, FindNextFileA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    FindNextVolumeA = declare(kernel32.FindNextVolumeA, BOOL, HANDLE, LPSTR, DWORD)
    FindNextVolumeW = declare(kernel32.FindNextVolumeW, BOOL, HANDLE, LPWSTR, DWORD)
    FindNextVolume = unicode(FindNextVolumeW, FindNextVolumeA)
    FindVolumeClose = declare(kernel32.FindVolumeClose, BOOL, HANDLE)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    FlushFileBuffers = declare(kernel32.FlushFileBuffers, BOOL, HANDLE)
    GetDiskFreeSpaceA = declare(kernel32.GetDiskFreeSpaceA, BOOL, LPCSTR, LPDWORD, LPDWORD, LPDWORD, LPDWORD)
    GetDiskFreeSpaceW = declare(kernel32.GetDiskFreeSpaceW, BOOL, LPCWSTR, LPDWORD, LPDWORD, LPDWORD, LPDWORD)
    GetDiskFreeSpace = unicode(GetDiskFreeSpaceW, GetDiskFreeSpaceA)
    GetDiskFreeSpaceExA = declare(kernel32.GetDiskFreeSpaceExA, BOOL, LPCSTR, PULARGE_INTEGER, PULARGE_INTEGER, PULARGE_INTEGER)
    GetDiskFreeSpaceExW = declare(kernel32.GetDiskFreeSpaceExW, BOOL, LPCWSTR, PULARGE_INTEGER, PULARGE_INTEGER, PULARGE_INTEGER)
    GetDiskFreeSpaceEx = unicode(GetDiskFreeSpaceExW, GetDiskFreeSpaceExA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    #
    #  The structure definition must be same as the one
    # (FILE_FS_FULL_SIZE_INFORMATION_EX) defined in ntioapi_x.w
    #
    class DISK_SPACE_INFORMATION(CStructure):
        _fields_ = [
            #
            #  AllocationUnits are actually file system clusters.
            #  AllocationUnits * SectorsPerAllocationUnit * BytesPerSector
            #  will get you the sizes in bytes.
            #

            #
            #  The Actual*AllocationUnits are volume sizes without considering Quota
            #  setting.
            #  ActualPoolUnavailableAllocationUnits is the unavailable space for the
            #  volume due to insufficient free pool space (PoolAvailableAllocationUnits).
            #  Be aware AllocationUnits are mesured in clusters, see comments at the beginning.
            #
            #  ActualTotalAllocationUnits = ActualAvailableAllocationUnits +
            #                               ActualPoolUnavailableAllocationUnits +
            #                               UsedAllocationUnits +
            #                               TotalReservedAllocationUnits
            #

            ("ActualTotalAllocationUnits", ULONGLONG),
            ("ActualAvailableAllocationUnits", ULONGLONG),
            ("ActualPoolUnavailableAllocationUnits", ULONGLONG),

            #
            #  The Caller*AllocationUnits are limited by Quota setting.
            #  CallerAvailableAllocationUnits is the unavailable space for the
            #  volume due to insufficient free pool space (PoolAvailableAllocationUnits).
            #  Be aware AllocationUnits are mesured in clusters, see comments at the beginning.
            #
            #  CallerTotalAllocationUnits = CallerAvailableAllocationUnits +
            #                               CallerPoolUnavailableAllocationUnits +
            #                               UsedAllocationUnits +
            #                               TotalReservedAllocationUnits
            #

            ("CallerTotalAllocationUnits", ULONGLONG),
            ("CallerAvailableAllocationUnits", ULONGLONG),
            ("CallerPoolUnavailableAllocationUnits", ULONGLONG),

            #
            #  The used space (in clusters) of the volume.
            #

            ("UsedAllocationUnits", ULONGLONG),

            #
            #  Total reserved space (in clusters).
            #

            ("TotalReservedAllocationUnits", ULONGLONG),

            #
            #  A special type of reserved space (in clusters) for per-volume storage
            #  reserve and this is included in the above TotalReservedAllocationUnits.
            #

            ("VolumeStorageReserveAllocationUnits", ULONGLONG),

            #
            #  This refers to the space (in clusters) that has been committed by
            #  storage pool but has not been allocated by file system.
            #
            #  s1 = (ActualTotalAllocationUnits - UsedAllocationUnits - TotalReservedAllocationUnits)
            #  s2 = (AvailableCommittedAllocationUnits + PoolAvailableAllocationUnits)
            #  ActualAvailableAllocationUnits = min( s1, s2 )
            #
            #  When s1 >= s2, ActualPoolUnavailableAllocationUnits = 0
            #  When s1 < s2, ActualPoolUnavailableAllocationUnits = s2 - s1.
            #

            ("AvailableCommittedAllocationUnits", ULONGLONG),

            #
            #  Available space (in clusters) in corresponding storage pool. If the volume
            #  is not a spaces volume, the PoolAvailableAllocationUnits is set to zero.
            #

            ("PoolAvailableAllocationUnits", ULONGLONG),

            ("SectorsPerAllocationUnit", DWORD),
            ("BytesPerSector", DWORD)
        ]
    PDISK_SPACE_INFORMATION = POINTER(DISK_SPACE_INFORMATION)
    GetDiskSpaceInformationA = declare(kernel32.GetDiskSpaceInformationA, HRESULT, LPCSTR, PDISK_SPACE_INFORMATION)
    GetDiskSpaceInformationW = declare(kernel32.GetDiskSpaceInformationW, HRESULT, LPCWSTR, PDISK_SPACE_INFORMATION)
    GetDiskSpaceInformation = unicode(GetDiskSpaceInformationW, GetDiskSpaceInformationA)
    # !UNICODE
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetDriveTypeA = declare(kernel32.GetDriveTypeA, UINT, LPCSTR)
    GetDriveTypeW = declare(kernel32.GetDriveTypeW, UINT, LPCWSTR)
    GetDriveType = unicode(GetDriveTypeW, GetDriveTypeA)

    class WIN32_FILE_ATTRIBUTE_DATA(CStructure):
        _fields_ = [
            ("dwFileAttributes", DWORD),
            ("ftCreationTime", FILETIME),
            ("ftLastAccessTime", FILETIME),
            ("ftLastWriteTime", FILETIME),
            ("nFileSizeHigh", DWORD),
            ("nFileSizeLow", DWORD)
        ]
    LPWIN32_FILE_ATTRIBUTE_DATA = POINTER(WIN32_FILE_ATTRIBUTE_DATA)

    GetFileAttributesA = declare(kernel32.GetFileAttributesA, DWORD, LPCSTR)
    GetFileAttributesW = declare(kernel32.GetFileAttributesW, DWORD, LPCWSTR)
    GetFileAttributes = unicode(GetFileAttributesW, GetFileAttributesA)
    # !UNICODE
    GetFileAttributesExA = declare(kernel32.GetFileAttributesExA, BOOL, LPCSTR, INT, LPVOID)
    GetFileAttributesExW = declare(kernel32.GetFileAttributesExW, BOOL, LPCWSTR, INT, LPVOID)
    GetFileAttributesEx = unicode(GetFileAttributesExW, GetFileAttributesExA)
    # !UNICODE

    class BY_HANDLE_FILE_INFORMATION(CStructure):
        _fields_ = [
            ("dwFileAttributes", DWORD),
            ("ftCreationTime", FILETIME),
            ("ftLastAccessTime", FILETIME),
            ("ftLastWriteTime", FILETIME),
            ("dwVolumeSerialNumber", DWORD),
            ("nFileSizeHigh", DWORD),
            ("nFileSizeLow", DWORD),
            ("nNumberOfLinks", DWORD),
            ("nFileIndexHigh", DWORD),
            ("nFileIndexLow", DWORD)
        ]
    PBY_HANDLE_FILE_INFORMATION = LPBY_HANDLE_FILE_INFORMATION = POINTER(BY_HANDLE_FILE_INFORMATION)

    GetFileInformationByHandle = declare(kernel32.GetFileInformationByHandle, BOOL, HANDLE, LPBY_HANDLE_FILE_INFORMATION)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetFileSize = declare(kernel32.GetFileSize, DWORD, HANDLE, LPDWORD)

    # REGION ***

    # REGION *** Application Family or Games Family ***

    GetFileSizeEx = declare(kernel32.GetFileSizeEx, BOOL, HANDLE, PLARGE_INTEGER)
    GetFileType = declare(kernel32.GetFileType, DWORD, HANDLE)
    if (cpreproc.getdef("_WINVER") >= 0x0600):
        GetFinalPathNameByHandleA = declare(kernel32.GetFinalPathNameByHandleA, DWORD, HANDLE, LPSTR, DWORD, DWORD)
        GetFinalPathNameByHandleW = declare(kernel32.GetFinalPathNameByHandleW, DWORD, HANDLE, LPWSTR, DWORD, DWORD)
        GetFinalPathNameByHandle = unicode(GetFinalPathNameByHandleW, GetFinalPathNameByHandleA)
    #(_WINVER >= 0x0600)
    GetFileTime = declare(kernel32.GetFileTime, BOOL, HANDLE, LPFILETIME, LPFILETIME, LPFILETIME)
    GetFullPathNameW = declare(kernel32.GetFullPathNameW, DWORD, LPCWSTR, DWORD, LPWSTR, POINTER(LPWSTR))
    GetFullPathNameA = declare(kernel32.GetFullPathNameA, DWORD, LPCSTR, DWORD, LPSTR, POINTER(LPSTR))
    GetFullPathName = unicode(GetFullPathNameW, GetFullPathNameA)
    if cpreproc.ifndef("UNICODE"):
        GetFullPathName = GetFullPathNameA
    GetLogicalDrives = declare(kernel32.GetLogicalDrives, DWORD, VOID)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetLogicalDriveStringsA = declare(kernel32.GetLogicalDriveStringsA, DWORD, DWORD, LPSTR)
    GetLogicalDriveStringsW = declare(kernel32.GetLogicalDriveStringsW, DWORD, DWORD, LPWSTR)
    GetLogicalDriveStrings = unicode(GetLogicalDriveStringsW, GetLogicalDriveStringsA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetLongPathNameA = declare(kernel32.GetLongPathNameA, DWORD, LPCSTR, LPSTR, DWORD)
    if cpreproc.ifndef("UNICODE"):
        GetLongPathName = GetLongPathNameA
        GetLongPathNameW = declare(kernel32.GetLongPathNameW, DWORD, LPCWSTR, LPWSTR, DWORD)
        GetLongPathName = unicode(GetLongPathNameW)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    GetShortPathNameA = declare(kernel32.GetShortPathNameA, DWORD, LPCSTR, LPSTR, DWORD)
    GetShortPathNameW = declare(kernel32.GetShortPathNameW, DWORD, LPCWSTR, LPWSTR, DWORD)
    GetShortPathName = unicode(GetShortPathNameW, GetShortPathNameA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetTempFileNameA = declare(kernel32.GetTempFileNameA, UINT, LPCSTR, LPCSTR, UINT, LPSTR)
    GetTempFileNameW = declare(kernel32.GetTempFileNameW, UINT, LPCWSTR, LPCWSTR, UINT, LPWSTR)
    GetTempFileName = unicode(GetTempFileNameW, GetTempFileNameA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    if cpreproc.getdef("_WINVER") >= 0x0600:
        GetVolumeInformationByHandleW = declare(kernel32.GetVolumeInformationByHandleW, BOOL, HANDLE, LPWSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)
        GetVolumeInformationA = declare(kernel32.GetVolumeInformationA, BOOL, LPCSTR, LPSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPSTR, DWORD)
        GetVolumeInformationW = declare(kernel32.GetVolumeInformationW, BOOL, LPCWSTR, LPWSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPWSTR, DWORD)
        GetVolumeInformation = unicode(GetVolumeInformationW, GetVolumeInformationA)
        GetVolumePathNameA = declare(kernel32.GetVolumePathNameA, BOOL, LPWSTR, LPSTR, DWORD)
        GetVolumePathNameW = declare(kernel32.GetVolumePathNameW, BOOL, LPCWSTR, LPWSTR, DWORD)
        GetVolumePathName = unicode(GetVolumePathNameW, GetVolumePathNameA)
    LocalFileTimeToFileTime = declare(kernel32.LocalFileTimeToFileTime, BOOL, PFILETIME, LPFILETIME)
    LockFile = declare(kernel32.LockFile, BOOL, HANDLE, DWORD, DWORD, DWORD, DWORD)
    LockFileEx = declare(kernel32.LockFileEx, BOOL, HANDLE, DWORD, DWORD, DWORD, DWORD, LPOVERLAPPED)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    QueryDosDeviceA = declare(kernel32.QueryDosDeviceA, DWORD, LPCSTR, LPSTR, DWORD)
    QueryDosDeviceW = declare(kernel32.QueryDosDeviceW, DWORD, LPCWSTR, LPWSTR, DWORD)
    QueryDosDevice = unicode(QueryDosDeviceW, QueryDosDeviceA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    ReadFile = declare(kernel32.ReadFile, BOOL, HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED)
    LPOVERLAPPED_COMPLETION_ROUTINE = WINAPI(VOID) # Remainder
    ReadFileEx = declare(kernel32.ReadFileEx, BOOL, HANDLE, LPVOID, DWORD, LPOVERLAPPED, LPOVERLAPPED_COMPLETION_ROUTINE)
    PFILE_SEGMENT_ELEMENT = PVOID
    ReadFileScatter = declare(kernel32.ReadFileScatter, BOOL, HANDLE, PFILE_SEGMENT_ELEMENT, DWORD, LPDWORD, LPOVERLAPPED) # Remainder
    RemoveDirectoryA = declare(kernel32.RemoveDirectoryA, BOOL, LPCSTR)
    RemoveDirectoryW = declare(kernel32.RemoveDirectoryW, BOOL, LPCWSTR)
    RemoveDirectory = unicode(RemoveDirectoryW, RemoveDirectoryA)
    SetEndOfFile = declare(kernel32.SetEndOfFile, BOOL, HANDLE)
    SetFileAttributesA = declare(kernel32.SetFileAttributesA, BOOL, LPCSTR, DWORD)
    SetFileAttributesW = declare(kernel32.SetFileAttributesW, BOOL, LPCWSTR, DWORD)
    SetFileAttributes = unicode(SetFileAttributesW, SetFileAttributesA)
    # !UNICODE
    if (cpreproc.getdef("_WINVER") >= 0x0600):
        SetFileInformationByHandle = declare(kernel32.SetFileInformationByHandle, BOOL, HANDLE, INT, LPVOID, DWORD)
    SetFilePointer = declare(kernel32.SetFilePointer, DWORD, HANDLE, LONG, PLONG, DWORD)
    SetFilePointerEx = declare(kernel32.SetFilePointerEx, BOOL, HANDLE, LARGE_INTEGER, PLARGE_INTEGER, DWORD)
    SetFileTime = declare(kernel32.SetFileTime, BOOL, HANDLE, PFILETIME, PFILETIME, PFILETIME)
    if cpreproc.getdef("_WINVER") >= 0x0501:
        SetFileValidData = declare(kernel32.SetFileValidData, BOOL, HANDLE, LONGLONG)
    #(_WINVER >= 0x0501)
    UnlockFile = declare(kernel32.UnlockFile, BOOL, HANDLE, DWORD, DWORD, DWORD, DWORD)
    UnlockFileEx = declare(kernel32.UnlockFileEx, BOOL, HANDLE, DWORD, DWORD, DWORD, LPOVERLAPPED)
    WriteFile = declare(kernel32.WriteFile, BOOL, HANDLE, LPCVOID, DWORD, LPDWORD, LPOVERLAPPED)
    WriteFileEx = declare(kernel32.WriteFileEx, BOOL, HANDLE, LPCVOID, DWORD, LPOVERLAPPED, LPOVERLAPPED_COMPLETION_ROUTINE)
    PFILE_SEGMENT_ELEMENT = PVOID
    WriteFileGather = declare(kernel32.WriteFileGather, BOOL, HANDLE, PFILE_SEGMENT_ELEMENT, DWORD, LPDWORD, LPOVERLAPPED) # REMAINDER
    GetTempPathA = declare(kernel32.GetTempPathA, DWORD, DWORD, LPSTR)
    GetTempPathW = declare(kernel32.GetTempPathW, DWORD, DWORD, LPWSTR)
    GetTempPath = unicode(GetTempPathW, GetTempPathA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    GetVolumeNameForVolumeMountPointA = declare(kernel32.GetVolumeNameForVolumeMountPointA, BOOL, LPCSTR, LPSTR, DWORD)
    GetVolumeNameForVolumeMountPointW = declare(kernel32.GetVolumeNameForVolumeMountPointW, BOOL, LPCWSTR, LPWSTR, DWORD)
    GetVolumeNameForVolumeMountPoint = unicode(GetVolumeNameForVolumeMountPointW, GetVolumeNameForVolumeMountPointA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    if (cpreproc.getdef("_WINVER") >= 0x0501):
        GetVolumePathNamesForVolumeNameA = declare(kernel32.GetVolumePathNamesForVolumeNameA, BOOL, LPCSTR, LPCH, DWORD, PDWORD)
        GetVolumePathNamesForVolumeNameW = declare(kernel32.GetVolumePathNamesForVolumeNameW, BOOL, LPCWSTR, LPWCH, DWORD, PDWORD)
        GetVolumePathNamesForVolumeName = unicode(GetVolumePathNamesForVolumeNameW, GetVolumePathNamesForVolumeNameA)
    # _WINVER >= 0x0501
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    if (cpreproc.getdef("_WINVER") >= 0x0602):
        class CREATEFILE2_EXTENDED_PARAMETERS(CStructure):
            _fields_ = [
                ("dwSize", DWORD),
                ("dwFileAttributes", DWORD),
                ("dwFileFlags", DWORD),
                ("dwSecurityQosFlags", DWORD),
                ("lpSecurityAttributes", LPSECURITY_ATTRIBUTES),
                ("hTemplateFile", HANDLE)
            ]
        PCREATEFILE2_EXTENDED_PARAMETERS = LPCREATEFILE2_EXTENDED_PARAMETERS = POINTER(CREATEFILE2_EXTENDED_PARAMETERS)
        CreateFile2 = declare(kernel32.CreateFile2, HANDLE, LPCWSTR, DWORD, DWORD, DWORD, LPCREATEFILE2_EXTENDED_PARAMETERS)
    # _WIN32_WINNT >= 0x0602
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    if (cpreproc.getdef("_WINVER") >= 0x0600):
        SetFileIoOverlappedRange = declare(kernel32.SetFileIoOverlappedRange, BOOL, HANDLE, PUCHAR, ULONG)
    if cpreproc.getdef("_WINVER") >= 0x0501:
        GetCompressedFileSizeA = declare(kernel32.GetCompressedFileSizeA, DWORD, LPCSTR, LPDWORD)
        GetCompressedFileSizeW = declare(kernel32.GetCompressedFileSizeW, DWORD, LPCWSTR, LPDWORD)
        GetCompressedFileSize = unicode(GetCompressedFileSizeW, GetCompressedFileSizeA)
    # !UNICODE
    # _WIN32_WINNT >= 0x0501