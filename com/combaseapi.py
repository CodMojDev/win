from .baseinterfacedef import *
from ..sdkddkver import *

_version = cpreproc.get_version()
combase = W_WinDLL('combase.dll')

def combase_foreign(*args: type, 
            name: Optional[str] = None,
            intermediate_method: bool = False) -> Callable:
        """
        Foreign method declare
        """
        return foreign_optimized(HRESULT, 
                                 *args,
                                 library=combase, 
                                 name=name, 
                                 intermediate_method=intermediate_method)

CLSCTX_INPROC = (CLSCTX_INPROC_SERVER|CLSCTX_INPROC_HANDLER)

# With DCOM, CLSCTX_REMOTE_SERVER should be included
# DCOM
CLSCTX_ALL = (CLSCTX_INPROC |
              CLSCTX_LOCAL_SERVER |
              CLSCTX_REMOTE_SERVER)
CLSCTX_SERVER = (CLSCTX_INPROC_SERVER|CLSCTX_LOCAL_SERVER)

# class registration flags; passed to CoRegisterClassObject
REGCLS_SINGLEUSE = 0        # class object only generates one instance
REGCLS_MULTIPLEUSE = 1      # same class object genereates multiple inst.
                            # and local automatically goes into inproc tbl.
REGCLS_MULTI_SEPARATE = 2   # multiple use, but separate control over each
                            # context.
REGCLS_SUSPENDED      = 4   # register is as suspended, will be activated
                            # when app calls CoResumeClassObjects
REGCLS_SURROGATE      = 8   # must be used when a surrogate process
                            # is registering a class object that will be
                            # loaded in the surrogate
if _version >= WIN32_WINNT_WINTHRESHOLD:
    REGCLS_AGILE = 0x10         # Class object aggregates the free-threaded marshaler
                                # and will be made visible to all inproc apartments.
                                # Can be used together with other flags - for example,
                                # REGCLS_AGILE | REGCLS_MULTIPLEUSE to register a
                                # class object that can be used multiple times from
                                # different apartments. Without other flags, behavior
                                # will retain REGCLS_SINGLEUSE semantics in that only
                                # one instance can be generated.
REGCLS = INT

# COM initialization flags; passed to CoInitialize.
#  DCOM
# These constants are only valid on Windows NT 4.0
if _version >= WIN32_WINNT_NT4:
    COINITBASE_MULTITHREADED      = 0x0      # OLE calls objects on any thread.
COINITBASE = INT

###### STD Object API Prototypes #########################################

@ole_foreign(DWORD, PTR(LPMALLOC))
def CoGetMalloc(dwMemContext: int, ppMalloc: IDoublePtr[IMalloc]) -> int:
    """
    Retrieves a pointer to the default OLE task memory allocator
    (which supports the system implementation of the `IMalloc` interface) 
    so applications can call its methods to manage memory.
    """
    
@ole_foreign(HGLOBAL, BOOL, PTR(LPSTREAM))
def CreateStreamOnHGlobal(hGlobal: HGLOBAL, 
                          fDeleteOnRelease: bool,
                          ppstm: IDoublePtr[IMalloc]) -> int:
    """
    The **CreateStreamOnHGlobal** function creates a stream object that uses an HGLOBAL memory handle to store the stream contents. This object is the OLE-provided implementation of the `IStream` interface.

    The returned stream object supports both reading and writing, is not transacted, and does not support region locking. The object calls the `GlobalReAlloc` function to grow the memory block as required.
    """
    
@ole_foreign(LPSTREAM, PTR(HGLOBAL))
def GetHGlobalFromStream(pstm: IPointer[IStream], phglobal: IPointer[HGLOBAL]) -> int: 
    """
    The **GetHGlobalFromStream** function retrieves the global memory handle to a stream that was created through a call to the `CreateStreamOnHGlobal` function.
    """
    
@ole32.foreign(DWORD)
def CoGetCurrentProcess() -> int: 
    """
    Returns a value that is unique to the current thread. `CoGetCurrentProcess` can be used to avoid thread ID reuse problems.
    """

# DCOM
if _version >= WIN32_WINNT_NT4:
    @ole_foreign(LPVOID, DWORD, intermediate_method=True)
    def CoInitializeEx(pvReserved: LPVOID, dwCoInit: int, **kwargs) -> int: 
        """
        Initializes the COM library for use by the calling thread, sets the thread's concurrency model, and creates a new apartment for the thread if one is required.
        """
        hr = delegate(pvReserved, dwCoInit)
        if SUCCEEDED(hr): 
            COM_GLOBAL_STATE.initialized = True
        return hr
    
    @ole_foreign(LPDWORD)
    def CoGetCallerTID(lpdwTID: LPDWORD) -> int: 
        """
        Returns a pointer to a `DWORD` that contains the apartment ID of the caller's thread.
        """

    @ole_foreign(LPGUID)
    def CoGetCurrentLogicalThreadId(pguid: IPointer[GUID]) -> int: 
        """
        Returns the logical thread identifier of the current physical thread.
        """

if _version >= WIN32_WINNT_WINXP:
    @ole_foreign(PULONG_PTR)
    def CoGetContextToken(pToken: IPointer[ULONG_PTR]) -> int: 
        """
        Returns a pointer to an implementation of `IObjContext` for the current context.
        """
        
    @ole_foreign(APTTYPE, REFIID, PVOID, intermediate_method=True)
    def CoGetDefaultContext(aptType: APTTYPE, iid: IID, ppv: IPointer[PVOID],
                            **kwargs) -> int:
        """
        Retrieves a reference to the default context of the specified apartment.
        """
        delegate(aptType, iid.ref(), ppv)

# definition for Win7 new APIs
if _version >= WIN32_WINNT_WIN7:
    @ole_foreign(PTR(APTTYPE), PTR(APTTYPEQUALIFIER))
    def CoGetApartmentType(pAptType: IPointer[APTTYPE], 
                        pAptQualifier: IPointer[APTTYPEQUALIFIER]) -> int: 
        """
        Returns the current apartment type and type qualifier.
        """
        
# definition for Win8 new APIs
 
if _version >= WIN32_WINNT_WIN8:   
    class ServerInformation(CStructure):
        _fields_ = [
            ('dwServerPid', DWORD),
            ('dwServerTid', DWORD),
            ('ui64ServerAddress', UINT64)
        ]
        
        ui64ServerAddress: int
        dwServerPid: int
        dwServerTid: int
        
    PServerInformation = ServerInformation.PTR()

    @combase.foreign(HRESULT, DWORD, UINT64, PServerInformation)
    def CoDecodeProxy(dwClientPid: int, ui64ProxyAddress: int,
                    pServerInformation: IPointer[ServerInformation]) -> int:
        """
        Locates the implementation of a Component Object Model (COM) interface in a server process given an interface to a proxied object.
        """

    CO_MTA_USAGE_COOKIE = HANDLE
        
    @ole_foreign(PTR(CO_MTA_USAGE_COOKIE))
    def CoIncrementMTAUsage(pCookie: IPointer[CO_MTA_USAGE_COOKIE]) -> int:
        """
        Keeps MTA support active when no MTA threads are running.
        """
        
    @ole_foreign(CO_MTA_USAGE_COOKIE)
    def CoDecrementMTAUsage(cookie: CO_MTA_USAGE_COOKIE) -> int:
        """
        Releases the increment made by a previous call to the `CoIncrementMTAUsage` function.
        """
        
    @ole_foreign(REFCLSID, intermediate_method=True)
    def CoAllowUnmarshalerCLSID(clsid: CLSID, **kwargs) -> int:
        """
        Adds an unmarshaler CLSID to the allowed list for the calling process only.
        """
        return delegate(clsid.ref())

@ole_foreign(REFIID, PVOID, intermediate_method=True)
def CoGetObjectContext(iid: IID, ppv: IPointer[LPVOID], **kwargs) ->  int:
    """
    Returns the context for the current object.
    """
    return delegate(iid.ref(), ppv)

# register/revoke/get class objects

@ole_foreign(REFCLSID, DWORD, LPVOID, REFIID, PVOID,
             intermediate_method=True)
def CoGetClassObject(clsid: CLSID, dwClsContext: int,
                     pvReserved: LPVOID, iid: IID,
                     ppv: IPointer[LPVOID], **kwargs) -> int:
    """
    Provides a pointer to an interface on a class object associated with a specified CLSID.
    `CoGetClassObject` locates, and if necessary, dynamically loads the executable code required to do this.

    Call `CoGetClassObject` directly to create multiple objects through a class object for which there is a 
    CLSID in the system registry. You can also retrieve a class object from a specific remote computer. 
    Most class objects implement the `IClassFactory` interface. You would then call `CreateInstance` to 
    create an uninitialized object. It is not always necessary to go through this process however.
    To create a single object, call the `CoCreateInstanceEx` function, which allows you to 
    create an instance on a remote machine. This replaces the `CoCreateInstance` function, which 
    can still be used to create an instance on a local computer. Both functions encapsulate 
    connecting to the class object, creating the instance, and releasing the class object.
    Two other functions, `CoGetInstanceFromFile` and `CoGetInstanceFromIStorage`, provide
    both instance creation on a remote system and object activation. 
    There are numerous functions and interface methods whose purpose is
    to create objects of a single type and provide a pointer to an interface on that object.
    """
    return delegate(clsid.ref(), dwClsContext,
                    pvReserved, iid.ref(), ppv)
    
@ole_foreign(REFCLSID, LPUNKNOWN, DWORD, DWORD, LPDWORD,
             intermediate_method=True)
def CoRegisterClassObject(clsid: CLSID, pUnk: IPointer[IUnknown],
                          dwClsContext: int, flags: int,
                          lpdwRegister: LPDWORD, **kwargs) -> int:
    """
    Registers an EXE class object with OLE so other applications can connect to it.
    """
    return delegate(clsid.ref(), pUnk, dwClsContext,
                    flags, lpdwRegister)
    
@ole_foreign(DWORD)
def CoRevokeClassObject(dwRegister: int) -> int: 
    """
    Informs OLE that a class object, previously registered with the `CoRegisterClassObject` function, is no longer available for use.
    """
    
@ole_foreign()
def CoResumeClassObjects() -> int:
    """
    Called by a server that can register multiple class objects to inform the SCM about all registered classes, and permits activation requests for those class objects.
    """
    
@ole_foreign()
def CoSuspendClassObjects() -> int:
    """
    Prevents any new activation requests from the SCM on all class objects registered within the process.
    """
    
@ole32.foreign(ULONG)
def CoAddRefServerProcess() -> int:
    """
    Increments a global per-process reference count.
    """
    
@ole32.foreign(ULONG)
def CoReleaseServerProcess() -> int: 
    """
    Decrements the global per-process reference count.
    """
    
@ole_foreign(REFIID, LPCLSID, intermediate_method=True)
def CoGetPSClsid(iid: IID, pClsid: IPointer[CLSID], **kwargs) -> int:
    """
    Returns the CLSID of the DLL that implements the proxy and stub for the specified interface.
    """
    return delegate(iid.ref(), pClsid)
    
@ole_foreign(REFIID, REFCLSID, intermediate_method=True)
def CoRegisterPSClsid(iid: IID, clsid: CLSID, **kwargs) -> int:
    """
    Enables a downloaded DLL to register its custom interfaces within its running process so that the marshaling code will be able to marshal those interfaces.
    """
    return delegate( iid.ref(), clsid.ref())

@ole_foreign(LPSURROGATE)
def CoRegisterSurrogate(pSurrogate: IPointer[ISurrogate]) -> int:
    """
    Registers the surrogate process through its ISurrogate interface pointer.
    """
    
# marshaling interface pointers
    
@ole_foreign(PULONG, REFIID, LPUNKNOWN, DWORD, LPVOID, DWORD,
             intermediate_method=True)
def CoGetMarshalSizeMax(pulSize: PULONG, iid: IID, pUnk: IPointer[IUnknown],
                        dwDestContext: int, pvDestContext: LPVOID, 
                        mshlflags: int, **kwargs) -> int:
    """
    Returns an upper bound on the number of bytes needed to marshal the specified interface pointer to the specified object.
    """
    return delegate(pulSize, iid.ref(), pUnk, dwDestContext, 
                    pvDestContext, mshlflags)
    
@ole_foreign(LPSTREAM, REFIID, LPUNKNOWN, DWORD, LPVOID, DWORD,
             intermediate_method=True)
def CoMarshalInterface(pStm: IPointer[IStream], iid: IID,
                       pUnk: IPointer[IUnknown], dwDestContext: int,
                       pvDestContext: LPVOID, mshlflags: int, **kwargs) -> int:
    """
    Writes into a stream the data required to initialize a proxy object in some client process.
    """
    return delegate(pStm, iid.ref(), pUnk, dwDestContext,
                    pvDestContext, mshlflags)
    
@ole_foreign(LPSTREAM, REFIID, PVOID, intermediate_method=True)
def CoUnmarshalInterface(pStm: IPointer[IStream], iid: IID, 
                         ppv: IPointer[PVOID], **kwargs) -> int:
    """
    Initializes a newly created proxy using data written into the stream by a previous call to the `CoMarshalInterface` function, and returns an interface pointer to that proxy.
    """
    return delegate(pStm, iid.ref(), ppv)

@ole_foreign(LPSTREAM, HRESULT)
def CoMarshalHresult(pstm: IPointer[IStream], hresult: int) -> int: 
    """
    Marshals an `HRESULT` to the specified stream, from which it can be unmarshaled using the `CoUnmarshalHresult` function.
    """
    
@ole_foreign(LPSTREAM, PTR(HRESULT))
def CoUnmarshalHresult(pstm: IPointer[IStream], phresult: IPointer[int]) -> int: 
    """
    Unmarshals an `HRESULT` type from the specified stream.
    """
    
@ole_foreign(LPSTREAM)
def CoReleaseMarshalData(pStm: IPointer[IStream]) -> int:
    """
    Destroys a previously marshaled data packet.
    """
    
@ole_foreign(LPUNKNOWN, DWORD)
def CoDisconnectObject(pUnk: IPointer[IUnknown], dwReserved: int) -> int:
    """
    Disconnects all remote process connections being maintained on behalf of all the interface pointers that point to a specified object.

    Only the process that actually manages the object should call `CoDisconnectObject`.
    """
    
@ole_foreign(LPUNKNOWN, BOOL, BOOL)
def CoLockObjectExternal(pUnk: IPointer[IUnknown], fLock: bool,
                         fLastUnlockReleases: bool) -> int:
    """
    Called either to lock an object to ensure that it stays in memory, or to release such a lock.
    """
    
@ole_foreign(REFIID, LPUNKNOWN, DWORD, LPVOID, DWORD, PTR(LPMARSHAL),
             intermediate_method=True)
def CoGetStandardMarshal(iid: IID, pUnk: IPointer[IUnknown],
                         dwDestContext: int, pvDestContext: LPVOID,
                         mshlflags: int, ppMarshal: IDoublePtr[IMarshal], **kwargs) -> int:
    """
    Creates a default, or standard, marshaling object in either the client process or the server process, depending on the caller, and returns a pointer to that object's `IMarshal` implementation.
    """
    return delegate(iid.ref(), pUnk, dwDestContext, 
                    pvDestContext, mshlflags, ppMarshal)
    
@ole_foreign(LPUNKNOWN, DWORD, PTR(LPUNKNOWN))
def CoGetStdMarshalEx(pUnkOuter: IPointer[IUnknown], smexflags: int,
                      ppUnkInner: IDoublePtr[IUnknown]) -> int: 
    """
    Creates an aggregated standard marshaler for use with lightweight client-side handlers.
    """
   
# flags for CoGetStdMarshalEx 
SMEXF_SERVER     = 0x01        # server side aggregated std marshaler
SMEXF_HANDLER    = 0x02        # client side (handler) agg std marshaler
STDMSHLFLAGS = INT

@ole32.foreign(BOOL, LPUNKNOWN, result_function=bool)
def CoIsHandlerConnected(pUnk: IPointer[IUnknown]) -> bool: 
    """
    Determines whether a remote object is connected to the corresponding in-process object.
    """
    
@ole_foreign(REFIID, LPUNKNOWN, PTR(LPSTREAM),
             intermediate_method=True)
def CoMarshalInterThreadInterfaceInStream(iid: IID, pUnk: IPointer[IUnknown],
                                          ppStm: IDoublePtr[IStream], **kwargs) -> int:
    """
    Marshals an interface pointer from one thread to another thread in the same process.
    """
    return delegate(iid.ref(), pUnk, ppStm)

@ole_foreign(LPSTREAM, REFIID, PVOID, intermediate_method=True)
def CoGetInterfaceAndReleaseStream(pStm: IPointer[IStream], iid: IID,
                                  ppv: IPointer[PVOID], **kwargs) -> int:
    """
    Unmarshals a buffer containing an interface pointer and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.
    """
    return delegate(pStm, iid.ref(), ppv)

@ole_foreign(LPUNKNOWN, PTR(LPUNKNOWN))
def CoCreateFreeThreadedMarshaler(punkOuter: IPointer[IUnknown],
                                  ppunkMarshal: IDoublePtr[IUnknown]) -> int:
    """
    Creates an aggregatable object capable of context-dependent marshaling.
    """
    
@ole32.foreign(VOID)
def CoFreeUnusedLibraries():
    """
    Unloads any DLLs that are no longer in use, probably because the DLL no longer has any instantiated COM objects outstanding.
    """
    
if _version >= WIN32_WINNT_WINXP:
    @ole32.foreign(VOID, DWORD, DWORD)
    def CoFreeUnusedLibrariesEx(dwUnloadDelay: int, dwReserved: int):
        """
        Unloads any DLLs that are no longer in use and whose unload delay has expired.
        """
    
if _version >= WIN32_WINNT_VISTA:
    @ole_foreign(DWORD)
    def CoDisconnectContext(dwTimeout: int) -> int: 
        """
        Disconnects all proxy connections that are being maintained on behalf of all interface pointers that point to objects in the current context.

        This function blocks connections until all objects are successfully disconnected or the time-out expires. Only the context that actually manages the objects should call `CoDisconnectContext`.
        """
    
if _version >= WIN32_WINNT_NT4:
    # Call Security

    @ole_foreign(PSECURITY_DESCRIPTOR, LONG, PSOLE_AUTHENTICATION_SERVICE,
                PVOID, DWORD, DWORD, PVOID, DWORD, PVOID)
    def CoInitializeSecurity(pSecDesc: IPointer[SECURITY_DESCRIPTOR], cAuthSvc: int, 
                            asAuthSvc: IPointer[SOLE_AUTHENTICATION_INFO],
                            pReserved1: PVOID, dwAuthn: int, dwImpLevel: int, 
                            pAuthList: PVOID, wCapabilities: int, pReserved3: PVOID) -> int:
        """
        Registers security and sets the default security values for the process.
        """
        
    @ole_foreign(REFIID, PVOID, intermediate_method=True)
    def CoGetCallContext(iid: IID, ppInterface: IPointer[PVOID], **kwargs) -> int:
        """
        Retrieves the context of the current call on the current thread.
        """
        return delegate(iid.ref(), ppInterface)

    @ole_foreign(LPUNKNOWN, PDWORD, PDWORD, PTR(LPOLESTR),
                PDWORD, PDWORD, PHANDLE, PDWORD)
    def CoQueryProxyBlanket(pProxy: IPointer[IUnknown], dwAuthnSvc: PDWORD,
                            pAuthzSvc: PDWORD, pServerPrincName: IPointer[LPOLESTR],
                            pAuthnLevel: PDWORD, pImpLevel: PDWORD, 
                            pAuthInfo: PHANDLE, pCapabilities: PDWORD) -> int:
        """
        Retrieves the authentication information the client uses to make calls on the specified proxy. This is a helper function for `IClientSecurity::QueryBlanket`.
        """
        
    @ole_foreign(LPUNKNOWN, DWORD, DWORD, LPOLESTR,
                DWORD, DWORD, HANDLE, DWORD)
    def CoSetProxyBlanket(pProxy: IPointer[IUnknown], pwAuthnSvc: int,
                            pAuthzSvc: int, pServerPrincName: LPOLESTR,
                            pAuthnLevel: int, pImpLevel: int, 
                            pAuthInfo: HANDLE, pCapabilities: int) -> int:
        """
        Sets the authentication information that will be used to make calls on the specified proxy. This is a helper function for `IClientSecurity::SetBlanket`.
        """
        
    @ole_foreign(LPUNKNOWN, PTR(LPUNKNOWN))
    def CoCopyProxy(pProxy: IPointer[IUnknown], ppCopy: IDoublePtr[IUnknown]) -> int:
        """
        Makes a private copy of the specified proxy.
        """
        
    @ole_foreign(LPUNKNOWN, PDWORD, PDWORD, PTR(LPOLESTR),
                PDWORD, PDWORD, PHANDLE, PDWORD)
    def CoQueryClientBlanket(pAuthnSvc: PDWORD, pAuthzSvc: PDWORD, 
                            pServerPrincName: IPointer[LPOLESTR],
                            pAuthnLevel: PDWORD, pImpLevel: PDWORD, 
                            pPrivs: PHANDLE, pCapabilities: PDWORD) -> int:
        """
        Called by the server to find out about the client that invoked the method executing on the current thread. This is a helper function for `IServerSecurity::QueryBlanket`.
        """
        
    @ole_foreign()
    def CoImpersonateClient() -> int: 
        """
        Enables the server to impersonate the client of the current call for the duration of the call.
        """
        
    @ole_foreign()
    def CoRevertToSelf() -> int:
        """
        Restores the authentication information on a thread of execution.
        """
        
    @ole_foreign(PDWORD, PTR(PSOLE_AUTHENTICATION_INFO))
    def CoQueryAuthenticationServices(pcAuthSvc: PDWORD,
                                    asAuthSvc: IDoublePtr[SOLE_AUTHENTICATION_INFO]) -> int:
        """
        Retrieves a list of the authentication services registered when the process called `CoInitializeSecurity`.
        """
        
    @ole_foreign(LPUNKNOWN, PTR(LPUNKNOWN))
    def CoSwitchCallContext(pNewObject: IPointer[IUnknown], ppOldObject: IDoublePtr[IUnknown]) -> int:
        """
        Switches the call context object used by `CoGetCallContext`.
        """
    
    @ole_foreign(REFCLSID, LPUNKNOWN, DWORD, COSERVERINFO.PTR(), DWORD,
                MULTI_QI.PTR(), intermediate_method=True)
    def CoCreateInstanceEx(Clsid: CLSID, punkOuter: IPointer[IUnknown],
                        dwClsCtx: int, pServerInfo: IPointer[COSERVERINFO],
                        dwCount: int, pResults: IPointer[MULTI_QI], **kwargs) -> int:
        """
        Creates an instance of a specific class on a specific computer.
        """
        return delegate(Clsid.ref(), punkOuter, dwClsCtx,
                        pServerInfo, dwCount, pResults)
    
if _version >= WIN32_WINNT_WIN8:
    @ole_foreign(REFCLSID, LPUNKNOWN, DWORD, PVOID, DWORD,
                MULTI_QI.PTR(), intermediate_method=True)
    def CoCreateInstanceFromApp(Clsid: CLSID, punkOuter: IPointer[IUnknown],
                        dwClsCtx: int, reserved: PVOID, dwCount: int,
                        pResults: IPointer[MULTI_QI], **kwargs) -> int:
        """
        Creates an instance of a specific class on a specific computer from within an app container.
        """
        return delegate(Clsid.ref(), punkOuter, dwClsCtx,
                        reserved, dwCount, pResults)
    
@ole_foreign(IActivationFilter.PTR())
def CoRegisterActivationFilter(pActivationFilter: IPointer[IActivationFilter]) -> int:
    """
    Registers a process-wide filter to process activation requests.
    """
    
if _version >= WIN32_WINNT_NT4:
    @ole_foreign(DWORD, REFIID, PVOID, intermediate_method=True)
    def CoGetCancelObject(dwThreadId: int, iid: IID, 
                        ppUnk: IPointer[PVOID], **kwargs) -> int:
        """
        Obtains a pointer to a call control interface, normally `ICancelMethodCalls`, on the cancel object corresponding to an outbound COM method call pending on the same or another client thread.
        """
        return delegate(dwThreadId, iid.ref(), ppUnk)

    @ole_foreign(LPUNKNOWN)
    def CoSetCancelObject(pUnk: IPointer[IUnknown]) -> int:
        """
        Sets (registers) or resets (unregisters) a cancel object for use during subsequent cancel operations on the current thread.
        """
        
    @ole_foreign(DWORD, ULONG)
    def CoCancelCall(dwThreadId: int, ulTimeout: int) -> int:
        """
        Requests cancellation of an outbound DCOM method call pending on a specified thread.
        """
        
    @ole_foreign()
    def CoTestCancel(): 
        """
        Determines whether the call being executed on the server has been canceled by the client.
        """
        
    @ole_foreign(LPVOID)
    def CoEnableCallCancellation(pReserved: LPVOID) -> int:
        """
        Enables cancellation of synchronous calls on the calling thread.
        """
        
    @ole_foreign(LPVOID)
    def CoDisableCallCancellation(pReserved: LPVOID) -> int:
        """
        Undoes the action of a call to `CoEnableCallCancellation`. Disables cancellation of synchronous calls on the calling thread when all calls to `CoEnableCallCancellation` are balanced by calls to `CoDisableCallCancellation`.
        """
    
@ole_foreign(PFILETIME)
def CoFileTimeNow(lpFileTime: IPointer[FILETIME]) -> int:
    """
    Returns the current time as a FILETIME structure.
    """

if _version >= WIN32_WINNT_NT4:
    @ole_foreign(DWORD, DWORD, ULONG, LPHANDLE, LPDWORD)
    def CoWaitForMultipleHandles(dwFlags: int, dwTimeout: int,
                                cHandles: int, pHandles: IPointer[HANDLE],
                                lpdwindex: LPDWORD) -> int: 
        """
        Waits for specified handles to be signaled or for a specified timeout period to elapse.
        """
        
    # Flags for Synchronization API and Classes

    COWAIT_DEFAULT = 0
    COWAIT_WAITALL = 1
    COWAIT_ALERTABLE = 2
    COWAIT_INPUTAVAILABLE = 4
    COWAIT_DISPATCH_CALLS = 8
    COWAIT_DISPATCH_WINDOW_MESSAGES = 0x10
    COWAIT_FLAGS = INT

    CWMO_DEFAULT = 0
    CWMO_DISPATCH_CALLS = 1
    CWMO_DISPATCH_WINDOW_MESSAGES = 2
    CWMO_FLAGS = INT

    @ole_foreign(DWORD, DWORD, ULONG, LPHANDLE, LPDWORD)
    def CoWaitForMultipleObjects(dwFlags: int, dwTimeout: int,
                                cHandles: int, pHandles: IPointer[HANDLE],
                                lpdwindex: LPDWORD) -> int: 
        """
        A replacement for `CoWaitForMultipleHandles`. 
        This replacement API hides the options for `CoWaitForMultipleHandles` that are not supported in ASTA.
        """
        
    CWMO_MAX_HANDLES = 56

@ole_foreign(REFCLSID, LPCLSID, intermediate_method=True)
def CoGetTreatAsClass(clsidOld: CLSID,
                      pClsidNew: IPointer[CLSID], **kwargs) -> int:
    """
    Returns the CLSID of an object that can emulate the specified object.
    """
    return delegate(clsidOld.ref(), pClsidNew)

if _version >= WIN32_WINNT_WINXP:
    @ole_foreign(LPOLESTR)
    def CoInvalidateRemoteMachineBindings(pszMachineName: LPOLESTR) -> int:
        """
        Tells the [service control manager](https://learn.microsoft.com/en-us/windows/desktop/Services/service-control-manager)
        to flush any cached RPC binding handles for the specified computer.

        Only administrators may call this function.
        """
   
if _version >= WIN32_WINNT_WINBLUE:
    AgileReferenceOptions  = INT
    AGILEREFERENCE_DEFAULT        = 0
    AGILEREFERENCE_DELAYEDMARSHAL = 1

    @ole_foreign(AgileReferenceOptions, REFIID, LPUNKNOWN,
                DOUBLE_PTR(IAgileReference), intermediate_method=True)
    def RoGetAgileReference(options: AgileReferenceOptions,
                            iid: IID, pUnk: IPointer[IUnknown], 
                            ppAgileReference: IDoublePtr[IAgileReference],
                            **kwargs) ->  int:
        """
        Creates an agile reference for an object specified by the given interface.
        """
        return  delegate(options, iid.ref(), pUnk, ppAgileReference)