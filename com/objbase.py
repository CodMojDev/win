from ..sdkddkver import *
from .storagedef import *

# COM initialization flags; passed to CoInitialize.
COINIT_APARTMENTTHREADED  = 0x2      # Apartment model
# These constants are only valid on Windows NT 4.0
COINIT_MULTITHREADED      = COINITBASE_MULTITHREADED
COINIT_DISABLE_OLE1DDE    = 0x4      # Don't use DDE for Ole1 support.
COINIT_SPEED_OVER_MEMORY  = 0x8      # Trade memory for speed.
COINIT = INT

# interface marshaling definitions
MARSHALINTERFACE_MIN = 500 # minimum number of bytes for interface marshal

# flags for internet asynchronous and layout docfile
ASYNC_MODE_COMPATIBILITY   = 0x00000001
ASYNC_MODE_DEFAULT         = 0x00000000

STGTY_REPEAT               = 0x00000100
STG_TOEND                  = 0xFFFFFFFF

STG_LAYOUT_SEQUENTIAL      = 0x00000000
STG_LAYOUT_INTERLEAVED     = 0x00000001

@ole32.foreign(DWORD)
def CoBuildVersion() -> int: 
    """
    Gets the build version of the DLL.
    """

cpreproc.define('COM_SUPPORT_MALLOC_SPIES')

@ole_foreign(LPMALLOCSPY)
def CoRegisterMallocSpy(pMallocSpy: IPointer[IMallocSpy]) -> int: 
    """
    Registers an implementation of the `IMallocSpy` interface, thereafter requiring OLE to call its wrapper methods around every call to the corresponding `IMalloc` method.
    """
    
@ole_foreign()
def CoRevokeMallocSpy() -> int: 
    """
    Revokes a registered `IMallocSpy` object.
    """
    
def CoCreateStandardMalloc(memctx: int, ppMalloc: IDoublePtr[IMalloc], **kwargs) -> int:
    """
    This function is obsolete. Refer to `CoGetMalloc`.
    """
    return CoGetMalloc(memctx, ppMalloc)
    
_version = cpreproc.get_version()
if _version >= WIN32_WINNT_WINXP:
    @ole_foreign(LPINITIALIZESPY, PULARGE_INTEGER)
    def CoRegisterInitializeSpy(pSpy: IPointer[IInitializeSpy],
                               puliCookie: IPointer[ULARGE_INTEGER]) -> int:
        """
        Registers an implementation of the IInitializeSpy interface. The IInitializeSpy interface is defined to allow developers to perform initialization and cleanup on COM apartments.
        """
        
    @ole_foreign(ULARGE_INTEGER)
    def CoRevokeInitializeSpy(uliCookie: ULARGE_INTEGER) -> int:
        """
        Revokes a registered implementation of the IInitializeSpy interface.
        """
        
    # COM System Security Descriptors (used when the corresponding registry
    # entries are absent)
    SD_LAUNCHPERMISSIONS = 0       # Machine wide launch permissions
    SD_ACCESSPERMISSIONS = 1       # Machine wide acesss permissions
    SD_LAUNCHRESTRICTIONS = 2      # Machine wide launch limits
    SD_ACCESSRESTRICTIONS = 3      # Machine wide access limits
    COMSD = INT
    
    @ole_foreign(COMSD, PTR(PSECURITY_DESCRIPTOR))
    def CoGetSystemSecurityPermissions(comSDType: COMSD, ppSD: IDoublePtr[SECURITY_DESCRIPTOR]) -> int:
        """
        Returns the default values of the Security Descriptors of the machine-wide launch and access permissions, as well as launch and access limits.
        """
        
# dll loading helpers; keeps track of ref counts and unloads all on exit
@ole32.foreign(HINSTANCE, LPOLESTR, BOOL)
def CoLoadLibrary(lpszLibName: LPOLESTR, bAutoFree: bool) -> int: 
    """
    Loads a specific DLL into the caller's process.
    """
    
@ole32.foreign(VOID, HINSTANCE)
def CoFreeLibrary(hInst: int) -> int: 
    """
    Frees a library that, when loaded, was specified to be freed explicitly.
    """
    
@ole32.foreign(VOID)
def CoFreeAllLibraries() -> int:
    """
    Frees all the DLLs that have been loaded with the CoLoadLibrary function (called internally by CoGetClassObject), regardless of whether they are currently in use.
    """
    
if _version >= WIN32_WINNT_NT4:
    @ole_foreign(COSERVERINFO.PTR(), PCLSID, LPUNKNOWN, DWORD, DWORD, LPOLESTR, DWORD, MULTI_QI.PTR())
    def CoGetInstanceFromFile(pServerInfo: IPointer[COSERVERINFO], pClsid: IPointer[CLSID],
                              punkOuter: IPointer[IUnknown], dwClsCtx: int, grfMode: int,
                              pwszName: LPOLESTR, dwCount: int, pResults: IPointer[MULTI_QI]) -> int: 
        """
        Creates a new object and initializes it from a file using IPersistFile::Load.
        """
        
    @ole_foreign(COSERVERINFO.PTR(), PCLSID, LPUNKNOWN, DWORD, LPSTORAGE, DWORD, MULTI_QI.PTR())
    def CoGetInstanceFromIStorage(pServerInfo: IPointer[COSERVERINFO], pClsid: IPointer[CLSID], punkOuter: IPointer[IUnknown],
                                  dwClsCtx: int, pstg: IPointer[IStorage], dwCount: int, pResults: IPointer[MULTI_QI]) -> int:
        """
        Creates a new object and initializes it from a storage object through an internal call to IPersistFile::Load.
        """
        
# Call related APIs
if _version >= WIN32_WINNT_WIN2K:
    @ole_foreign(LPUNKNOWN, LPVOID)
    def CoAllowSetForegroundWindow(pUnk: IPointer[IUnknown], lpvReserved: LPVOID) -> int:
        """
        This function passes the foreground privilege (the privilege to set the foreground window) from one process to another. The process that has the foreground privilege can call this function to pass that privilege on to a local COM server process.
        """
        
    @ole_foreign(LPVOID, PULONG, HRESULT)
    def DcomChannelSetHResult(pvReserved: LPVOID, pulReserved: PULONG, appsHR: HRESULT) -> int: ...

# other helpers
@ole32.foreign(BOOL, REFCLSID, intermediate_method=True, result_function=bool)
def CoIsOle1Class(clsid: CLSID, **kwargs) -> bool:
    """
    Determines whether the specified CLSID represents an OLE 1 object.
    """
    return delegate(clsid.ref())

@ole32.foreign(BOOL, PFILETIME, LPWORD, LPWORD, result_function=bool)
def CoFileTimeToDosDateTime(lpFileTime: IPointer[FILETIME], 
                            lpDosDate: LPWORD, lpDosTime: LPWORD) -> bool: 
    """
    Converts a FILETIME into MS-DOS date and time values.
    """
    
@ole32.foreign(BOOL, WORD, WORD, PFILETIME, result_function=bool)
def CoDosDateTimeToFileTime(nDosDate: int, nDosTime: int, 
                            lpFileTime: IPointer[FILETIME]) -> bool:
    """
    Converts the MS-DOS representation of the time and date to a FILETIME structure used by Windows.
    """
  
@ole_foreign(LPMESSAGEFILTER, PTR(LPMESSAGEFILTER))
def CoRegisterMessageFilter(lpMessageFilter: IPointer[IMessageFilter], 
                            lplpMessageFilter: IDoublePtr[IMessageFilter]) -> int: 
    """
    Registers with OLE the instance of an IMessageFilter interface, which is to be used for handling concurrency issues on the current thread.
    """
    
if _version >= WIN32_WINNT_NT4:
    @ole_foreign(REFGUID, IChannelHook.PTR(), intermediate_method=True)
    def CoRegisterChannelHook(ExtensionUuid: GUID, pChannelHook: IPointer[IChannelHook], 
                              **kwargs) -> int:
        """
        Registers a channel hook.
        """
        return delegate(ExtensionUuid.ref(), pChannelHook)
        
##### DV APIs ##########################################

@ole_foreign(PTR(LPDATAADVISEHOLDER))
def CreateDataAdviseHolder(ppDAHolder: IDoublePtr[IDataAdviseHolder]) -> int:
    """
    The CreateDataAdviseHolder function (objinterfacedef.py) retrieves a pointer to the OLE implementation of IDataAdviseHolder on the data advise holder object.
    """
    
@ole_foreign(LPUNKNOWN, REFCLSID, REFIID, PVOID, intermediate_method=True)
def CreateDataCache(pUnkOuter: IPointer[IUnknown], clsid: CLSID,
                    iid: IID, ppv: IPointer[LPVOID], **kwargs) -> int:
    """
    Retrieves a pointer to a new instance of an OLE-provided implementation of a data cache.
    """
    return delegate(pUnkOuter, clsid.ref(), iid.ref(), ppv)

@ole_foreign(IFillLockBytes.PTR(), DWORD, DWORD, PTR(LPSTORAGE))
def StgOpenAsyncDocfileOnIFillLockBytes(pflb: IPointer[IFillLockBytes],
                                        grfMode: int, asyncFlags: int,
                                        ppstgOpen: IDoublePtr[IStorage]) -> int:
    """
    Opens an existing root asynchronous storage object on a byte-array wrapper object provided by the caller.
    """
    
@ole_foreign(LPLOCKBYTES, IFillLockBytes.DOUBLE_PTR())
def StgGetIFillLockBytesOnILockBytes(pilb: IPointer[ILockBytes], 
                                     ppflb: IDoublePtr[IFillLockBytes]) -> int:
    """
    Creates a new wrapper object on a byte array object provided by the caller.
    """
    
@ole_foreign(LPLOCKBYTES, IFillLockBytes.DOUBLE_PTR())
def StgGetIFillLockBytesOnFile(pwcsName: LPOLESTR, ppflb: IDoublePtr[IFillLockBytes]) -> int:
    """
    Opens a wrapper object on a temporary file.
    """
    
@ole_foreign(LPBINDCTX, DWORD, uCLSSPEC.PTR(), QUERYCONTEXT.PTR(), LPWSTR)
def CoInstall(pbc: IPointer[IBindCtx], dwFlags: int, pClassSpec: IPointer[uCLSSPEC],
              pQuery: IPointer[QUERYCONTEXT], pszCodeBase: LPWSTR) -> int:
    """
    Installs the requested COM server application.
    """
    
#
# Moniker APIs
#

@ole_foreign(LPMONIKER, DWORD, REFIID, PVOID, intermediate_method=True)
def BindMoniker(pmk: IPointer[IMoniker], grfOpt: int, iidResult: IID,
                ppvResult: IPointer[PVOID], **kwargs) -> int:
    """
    Locates an object by means of its moniker, activates the object if it is inactive, and retrieves a pointer to the specified interface on that object.
    """
    return delegate(pmk, grfOpt, iidResult.ref(), ppvResult)

@ole_foreign(LPCWSTR, LPBIND_OPTS, REFIID, PVOID, intermediate_method=True)
def CoGetObject(pszName: LPCWSTR, pBindOptions: IPointer[BIND_OPTS], 
                iid: IID, ppv: IPointer[PVOID], **kwargs) -> int:
    """
    Converts a display name into a moniker that identifies the object named, and then binds to the object identified by the moniker.
    """
    return delegate(pszName, pBindOptions, iid.ref(), ppv)

@ole_foreign(LPBC, LPCOLESTR, PULONG, PTR(LPMONIKER))
def MkParseDisplayName(pbc: IPointer[IBindCtx], szUserName: LPCOLESTR,
                       pchEaten: PULONG, ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Converts a string into a moniker that identifies the object named by the string.
    """

@ole_foreign(LPMONIKER, LPMONIKER, PTR(LPMONIKER), BOOL)
def MonikerRelativePathTo(pmkSrc: IPointer[IMoniker], pmkDest: IPointer[IMoniker],
                          ppmkRelPath: IDoublePtr[IMoniker], dwReserved: bool) -> int:
    """
    Provides a moniker that, when composed onto the end of the first specified moniker (or one with a similar structure), yields the second specified moniker.
    """
    
@ole_foreign(LPMONIKER, LPMONIKER, PTR(LPMONIKER))
def MonikerCommonPrefixWith(pmkThis: IPointer[IMoniker], pmkOther: IPointer[IMoniker],
                            ppmkCommon: IDoublePtr[IMoniker]) -> int: 
    """
    Creates a new moniker based on the common prefix that this moniker (the one comprising the data of this moniker object) shares with another moniker.
    """

@ole_foreign(DWORD, PTR(LPBC))
def CreateBindCtx(reserved: int, ppbc: IDoublePtr[IBindCtx]) -> int:
    """
    Returns a pointer to an implementation of IBindCtx (a bind context object). This object stores information about a particular moniker-binding operation.
    """

@ole_foreign(LPMONIKER, LPMONIKER, PTR(LPMONIKER))
def CreateGenericComposite(pmkFirst: IPointer[IMoniker], pmkRest: IPointer[IMoniker],
                           ppmkComposite: IDoublePtr[IMoniker]) -> int:
    """
    Performs a generic composition of two monikers and supplies a pointer to the resulting composite moniker.
    """

@ole_foreign(LPCOLESTR, PCLSID)
def GetClassFile(szFileName: LPCOLESTR, pclsid: IPointer[CLSID]) -> int:
    """
    Returns the CLSID associated with the specified file name.
    """

@ole_foreign(REFCLSID, PTR(LPMONIKER), intermediate_method=True)
def CreateClassMoniker(clsid: CLSID, ppmk: IDoublePtr[IMoniker], **kwargs) -> int:
    """
    Creates a class moniker that refers to the specified class.
    """
    return delegate(clsid.ref(), ppmk)

@ole_foreign(LPCOLESTR, PTR(LPMONIKER))
def CreateFileMoniker(lpszPathname: LPCOLESTR, ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Creates a file moniker based on the specified path.
    """

@ole_foreign(LPCOLESTR, LPCOLESTR, PTR(LPMONIKER))
def CreateItemMoniker(lpszDelim: LPCOLESTR, lpszItem: LPCOLESTR, 
                      ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Creates an item moniker that identifies an object within a containing object (typically a compound document).
    """
    
@ole_foreign(PTR(LPMONIKER))
def CreateAntiMoniker(ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Creates and returns a new anti-moniker.
    """

@ole_foreign(LPUNKNOWN, PTR(LPMONIKER))
def CreatePointerMoniker(punk: IPointer[IUnknown], ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Creates a pointer moniker based on a pointer to an object.
    """

@ole_foreign(LPUNKNOWN, PTR(LPMONIKER))
def CreateObjrefMoniker(punk: IPointer[IUnknown], ppmk: IDoublePtr[IMoniker]) -> int:
    """
    Creates an OBJREF moniker based on a pointer to an object.
    """

@ole_foreign(DWORD, PTR(LPRUNNINGOBJECTTABLE))
def GetRunningObjectTable(reserved: int, pprot: IDoublePtr[IRunningObjectTable]) -> int:
    """
    Returns a pointer to the IRunningObjectTable interface on the local running object table (ROT).
    """