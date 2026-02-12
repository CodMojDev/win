from .objinterfacedef import *
from .combaseapi import *

#
# Common typedefs for paramaters used in Storage API's, gleamed from storage.h
# Also contains Storage error codes, which should be moved into the storage
# idl files.
#

CWCSTORAGENAME = 32

# Storage instantiation modes
STGM_DIRECT            = 0x00000000
STGM_TRANSACTED        = 0x00010000
STGM_SIMPLE            = 0x08000000

STGM_READ              = 0x00000000
STGM_WRITE             = 0x00000001
STGM_READWRITE         = 0x00000002

STGM_SHARE_DENY_NONE   = 0x00000040
STGM_SHARE_DENY_READ   = 0x00000030
STGM_SHARE_DENY_WRITE  = 0x00000020
STGM_SHARE_EXCLUSIVE   = 0x00000010

STGM_PRIORITY          = 0x00040000
STGM_DELETEONRELEASE   = 0x04000000
STGM_NOSCRATCH         = 0x00100000

STGM_CREATE            = 0x00001000
STGM_CONVERT           = 0x00020000
STGM_FAILIFTHERE       = 0x00000000

STGM_NOSNAPSHOT        = 0x00200000
STGM_DIRECT_SWMR       = 0x00400000

STGFMT = DWORD

STGFMT_STORAGE         = 0
STGFMT_NATIVE          = 1
STGFMT_FILE            = 3
STGFMT_ANY             = 4
STGFMT_DOCFILE         = 5

# This is a legacy define to allow old component to builds
STGFMT_DOCUMENT        = 0

# Structured storage APIs
@ole_foreign(LPWSTR, DWORD, DWORD, PTR(LPSTORAGE))
def StgCreateDocfile(pwcsName: LPWSTR, grfMode: int, reserved: int,
                     ppstgOpen: IDoublePtr[IStorage]) -> int: 
    """
    The `StgCreateDocfile` function creates a new compound file storage object using the COM-provided *compound file implementation* for the `IStorage` interface.
    """
    
@ole_foreign(LPLOCKBYTES, DWORD, DWORD, PTR(LPSTORAGE))
def StgCreateDocfileOnILockBytes(plkbyt: IPointer[ILockBytes], grfMode: int, 
                                 reserved: int, ppstgOpen: IDoublePtr[IStorage]) -> int: 
    """
    The `StgCreateDocfileOnILockBytes` function creates and opens a new compound file storage object on top of a byte-array object provided by the caller. The storage object supports the COM-provided, compound-file implementation for the `IStorage` interface.
    """
    
@ole_foreign(LPWSTR, LPSTORAGE, DWORD, SNB, DWORD, PTR(LPSTORAGE))
def StgOpenStorage(pwcsName: LPWSTR, pstgPriority: IPointer[IStream],
                   grfMode: int, snbExclude: IPointer[LPOLESTR],
                   reserved: int, ppstgOpen: IDoublePtr[IStorage]) -> int:
    """
    The `StgOpenStorage` function opens an existing root storage object in the file system. Use this function to open compound files. Do not use it to open directories, files, or summary catalogs. Nested storage objects can only be opened using their parent `IStorage::OpenStorage` method.
    """
    
@ole_foreign(LPLOCKBYTES, LPSTORAGE, DWORD, SNB, DWORD, PTR(LPSTORAGE))
def StgOpenStorageOnILockBytes(plkbyt: IPointer[ILockBytes],
                               pstgPriority: IPointer[IStream], 
                               grfMode: int, snbExclude: IPointer[LPOLESTR], 
                               reserved: int, ppstgOpen: IDoublePtr[IStorage]) -> int:
    """
    The `StgOpenStorageOnILockBytes` function opens an existing storage object that does not reside in a disk file, but instead has an underlying byte array provided by the caller.
    """
    
@ole_foreign(LPWSTR)
def StgIsStorageFile(pwcsName: LPWSTR) -> int:
    """
    The `StgIsStorageFile` function indicates whether a particular disk file contains a storage object.
    """
    
@ole_foreign(LPLOCKBYTES)
def StgIsStorageILockBytes(pwcsName: IPointer[ILockBytes]) -> int:
    """
    The `StgIsStorageILockBytes` function indicates whether the specified byte array contains a storage object.
    """
    
@ole_foreign(LPWSTR, PFILETIME, PFILETIME, PFILETIME)
def StgSetTimes(lpszName: LPWSTR, pctime: IPointer[FILETIME],
                patime: IPointer[FILETIME], pmtime: IPointer[FILETIME]) -> int:
    """
    The `StgSetTimes` function sets the creation, access, and modification times of the indicated file, if supported by the underlying file system.
    """
    
_version = cpreproc.get_version()
if _version == WIN32_WINNT_WINXP:
    STGOPTIONS_VERSION = 1
elif _version > WIN32_WINNT_WINXP:
    STGOPTIONS_VERSION = 2
else:
    STGOPTIONS_VERSION = 0
    
class STGOPTIONS(CStructure):
    _fields_ = [
        ('usVersion', USHORT),            # Versions 1 and 2 supported
        ('reserved', USHORT),             # must be 0 for padding
        ('ulSectorSize', ULONG),          # docfile header sector size (512)
        ('pwcsTemplateFile', LPWSTR)      # version 2 or above
    ]
    
    pwcsTemplateFile: LPWSTR
    ulSectorSize: int
    usVersion: int
    reserved: int
    
@ole_foreign(LPWSTR, DWORD, DWORD, DWORD, STGOPTIONS.PTR(),
             PSECURITY_DESCRIPTOR, REFIID, PVOID,
             intermediate_method=True)
def StgCreateStorageEx(pwcsName: LPWSTR, grfMode: int, 
                       stgfmt: int, grfAttrs: int,
                       pStgOptions: IPointer[STGOPTIONS],
                       pSecurityDescriptor: IPointer[SECURITY_DESCRIPTOR],
                       iid: IID, ppObjectOpen: IPointer[PVOID], **kwargs) -> int:
    """
    The `StgCreateStorageEx` function creates a new storage object using a provided implementation for the `IStorage` or `IPropertySetStorage` interfaces. To open an existing file, use the `StgOpenStorageEx` function instead.

    Applications written for Windows 2000, Windows Server 2003 and Windows XP must use `StgCreateStorageEx` rather than `StgCreateDocfile` to take advantage of the enhanced Windows 2000 and Windows XP Structured Storage features.
    """
    return delegate(pwcsName, grfMode, stgfmt, grfAttrs, pStgOptions, 
                    pSecurityDescriptor, iid.ref(), ppObjectOpen)

@ole_foreign(LPWSTR, DWORD, DWORD, DWORD, STGOPTIONS.PTR(),
             PSECURITY_DESCRIPTOR, REFIID, PVOID,
             intermediate_method=True)
def StgOpenStorageEx(pwcsName: LPWSTR, grfMode: int, 
                       stgfmt: int, grfAttrs: int,
                       pStgOptions: IPointer[STGOPTIONS],
                       pSecurityDescriptor: IPointer[SECURITY_DESCRIPTOR],
                       iid: IID, ppObjectOpen: IPointer[PVOID], **kwargs) -> int:
    """
    The `StgOpenStorageEx` function opens an existing root storage object in the file system. Use this function to open Compound Files and regular files. To create a new file, use the `StgCreateStorageEx` function.
    """
    return delegate(pwcsName, grfMode, stgfmt, grfAttrs, pStgOptions, 
                    pSecurityDescriptor, iid.ref(), ppObjectOpen)
    
# Helper functions
@ole_foreign(LPSTORAGE, LPCLSID)
def ReadClassStg(pStg: IPointer[IStorage], pclsid: IPointer[CLSID]) -> int:
    """
    The `ReadClassStg` function reads the CLSID previously written to a storage object with the `WriteClassStg` function.
    """
    
@ole_foreign(LPSTORAGE, REFCLSID, intermediate_method=True)
def WriteClassStg(pStg: IPointer[IStorage], clsid: CLSID) -> int:
    """
    The `WriteClassStg` function stores the specified class identifier (CLSID) in a storage object.
    """
    return delegate(pStg, clsid.ref())

@ole_foreign(LPSTREAM, LPCLSID)
def ReadClassStm(pStg: IPointer[IStream], pclsid: IPointer[CLSID]) -> int:
    """
    The `ReadClassStm` function reads the CLSID previously written to a stream object with the `WriteClassStm` function.
    """
    
@ole_foreign(LPSTREAM, REFCLSID, intermediate_method=True)
def WriteClassStm(pStg: IPointer[IStream], clsid: CLSID) -> int:
    """
    The `WriteClassStm` function stores the specified CLSID in the stream.
    """
    return delegate(pStg, clsid.ref())

# Storage utility APIs
@ole_foreign(LPLOCKBYTES, PTR(HGLOBAL))
def GetHGlobalFromILockBytes(plkbyt: IPointer[ILockBytes],
                             phglobal: IPointer[HGLOBAL]) -> int:
    """
    The `GetHGlobalFromILockBytes` function retrieves a global memory handle to a byte array object created using the `CreateILockBytesOnHGlobal` function.
    """
    
@ole_foreign(HGLOBAL, BOOL, PTR(LPLOCKBYTES))
def CreateILockBytesOnHGlobal(hGlobal: HGLOBAL, fDeleteOnRelease: bool,
                              pplkByt: IDoublePtr[ILockBytes]) -> int:
    """
    The `CreateILockBytesOnHGlobal` function creates a byte array object that uses an `HGLOBAL` memory handle to store the bytes intended for in-memory storage of a compound file. This object is the OLE-provided implementation of the `ILockBytes` interface.

    The returned byte array object supports both reading and writing, but does not support region locking. The object calls the `GlobalReAlloc` function to grow the memory block as required.
    """

# ConvertTo APIs
@ole_foreign(LPSTORAGE)
def GetConvertStg(pStg: IPointer[IStorage]) -> int:
    """
    The `GetConvertStg` function returns the current value of the convert bit for the specified storage object.
    """