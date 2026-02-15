#+-------------------------------------------------------------------------
#
#  Microsoft Windows
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
#  File: wtypesbase.idl
#
#  Contents: This interface definition contains typedefs for remotable
#            data types.
#--------------------------------------------------------------------------

from . import cpreproc

if cpreproc.pragma_once():
    from .minwindef import *
    
    OLECHAR = WCHAR
    UCHAR = BYTE
    
    class _SECURITY_ATTRIBUTES(CStructure):
        _fields_ = [
            ("nLength", DWORD),
            ("lpSecurityDescriptor", LPVOID),
            ("_bInheritHandle", BOOL)
        ]
        
        lpSecurityDescriptor: PVOID
        nLength: int
        
        @property
        def bInheritHandle(self): return bool(self._bInheritHandle)
        
    SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
    PSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
    LPSECURITY_ATTRIBUTES = PSECURITY_ATTRIBUTES
        
    SECURITY_DESCRIPTOR_CONTROL = USHORT
    PSECURITY_DESCRIPTOR_CONTROL = PUSHORT
    PSID = PVOID
    
    class ACL(CStructure):
        _fields_ = [
            ("AclRevision", BYTE),
            ("Sbz1", BYTE),
            ("AclSize", WORD),
            ("AceCount", WORD),
            ("Sbz2", WORD)
        ]
        
        AclRevision: int
        AceCount: int
        AclSize: int
        Sbz1: int
        Sbz2: int
    
    PACL = POINTER(ACL)
    
    class SECURITY_DESCRIPTOR(CStructure):
        _fields_ = [
            ('Revision', UCHAR),
            ('Sbz1', UCHAR),
            ('Control', SECURITY_DESCRIPTOR_CONTROL),
            ('Owner', PSID),
            ('Group', PSID),
            ('Sacl', PACL),
            ('Dacl', PACL)
        ]
        
        Control: SECURITY_DESCRIPTOR_CONTROL
        Revision: int
        Owner: PSID
        Group: PSID
        Sbz1: int
        
        Sacl: IPointer[ACL]
        Dacl: IPointer[ACL]
    
    PSECURITY_DESCRIPTOR = POINTER(SECURITY_DESCRIPTOR)
    
    class COAUTHIDENTITY(CStructure):
        # User and Password length from lmcons.h
        # Domain length === FQDN length which is 256
        _fields_ = [
            ('User', PUSHORT),
            ('UserLength', ULONG),
            ('Domain', PUSHORT),
            ('DomainLength', ULONG),
            ('Password', PUSHORT),
            ('PasswordLength', ULONG),
            ('Flags', ULONG)
        ]
        
        User: PUSHORT
        UserLength: int
        
        Domain: PUSHORT
        DomainLength: int
        
        Password: PUSHORT
        PasswordLength: int
        
        Flags: int
        
    class COAUTHINFO(CStructure):
        _fields_ = [
            ('dwAuthnSvc', DWORD),
            ('dwAuthzSvc', DWORD),
            ('pwszServerPrincName', LPWSTR),
            ('dwAuthnLevel', DWORD),
            ('dwImpersonationLevel', DWORD),
            ('pAuthIdentityData', COAUTHIDENTITY.PTR()),
            ('dwCapabilities', DWORD)
        ]
        
        dwAuthnSvc: int
        dwAuthzSvc: int
        
        pwszServerPrincName: str
        
        dwImpersonationLevel: int
        dwAuthnLevel: int
        
        pAuthIdentityData: IPointer[COAUTHIDENTITY]
        dwCapabilities: int

    #
    # SCODE, HRESULT
    #
    #
    #  Status values are 32 bit values layed out as follows:
    #
    #   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
    #   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
    #  +-+-----------------------------+-------------------------------+
    #  |S|       Facility              |               Code            |
    #  +-+-----------------------------+-------------------------------+
    #
    #  where
    #
    #      S - is the severity code
    #
    #          0 - Success
    #          1 - Error
    #
    #
    #      Facility - is the facility code
    #
    #      Code - is the facility's status code
    #
    # SCODE and HRESULT are mktyplib base types.
    #
    SCODE = LONG
    PSCODE = PLONG

    class COSERVERINFO(CStructure):
        _fields_ = [
            ('dwReserved1', DWORD),
            ('pwszName', LPWSTR),
            ('pAuthInfo', COAUTHINFO.PTR()),
            ('dwReserved2', DWORD)
        ]
        
        pAuthInfo: IPointer[COAUTHINFO]
        pwszName: str
    
    from .guiddef import *
    
    class _OBJECTID(CStructure):
        _fields_ = [
            ("Lineage", GUID),
            ("Uniquifier", DWORD)
        ]
    OBJECTID = _OBJECTID
        
    ######################### Misc types ###################################/

    # Common typdefs used in API paramaters, gleamed from compobj.h

    # memory context values; passed to CoGetMalloc
    MEMCTX_TASK = 1            # task (private) memory
    MEMCTX_SHARED = 2          # shared memory (between processes)
    MEMCTX_MACSYSTEM = 3       # on the mac, the system heap
    # these are mostly for internal use...
    MEMCTX_UNKNOWN = -1        # unknown context (when asked about it)
    MEMCTX_SAME = -2           # same context (as some other pointer)
    MEMCTX = INT
    
    # For ROT registry flags under AppID
    if cpreproc.pragma_once('_ROTREGFLAGS_DEFINED'):
        ROTREGFLAGS_ALLOWANYCLIENT = 0x1
    # !_ROTREGFLAGS_DEFINED

    # For AppID registry flags under AppID
    if cpreproc.pragma_once('_APPIDREGFLAGS_DEFINED'):
        APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP = 0x1
        APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND = 0x2
        APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY = 0x4
        APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN = 0x8
        APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION = 0x10
        APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY = 0x20
        APPIDREGFLAGS_RESERVED1 = 0x40
        APPIDREGFLAGS_RESERVED2 = 0x80
        APPIDREGFLAGS_RESERVED3 = 0x100
        APPIDREGFLAGS_RESERVED4 = 0x200
        APPIDREGFLAGS_RESERVED5 = 0x400
        APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU = 0x800
        APPIDREGFLAGS_RESERVED7 = 0x1000
        APPIDREGFLAGS_RESERVED8 = 0x2000
        APPIDREGFLAGS_RESERVED9 = 0x4000
    # !_APPIDREGFLAGS_DEFINED

    # Flags controlling security behavior of SCM/Resolver calls from RPCSS
    if cpreproc.pragma_once('_DCOMSCM_REMOTECALL_FLAGS_DEFINED'):
        DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES = 0x1
        DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL = 0x2
        DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES = 0x4
        DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL = 0x8
        DCOMSCM_PING_USE_MID_AUTHNSERVICE = 0x10
        DCOMSCM_PING_DISALLOW_UNSECURE_CALL = 0x20
    # !_DCOMSCM_REMOTECALL_FLAGS_DEFINED


    # class context: used to determine what scope and kind of class object to use
    # NOTE: this is a bitwise enum
    CLSCTX_INPROC_SERVER = 0x01     # server dll (runs in same process as caller)
    CLSCTX_INPROC_HANDLER = 0x02    # handler dll (runs in same process as caller)
    CLSCTX_LOCAL_SERVER = 0x04      # server exe (runs on same machine; diff proc)
    CLSCTX_INPROC_SERVER16 = 0x08   # 16-bit server dll (runs in same process as caller)
    CLSCTX_REMOTE_SERVER = 0x10     # remote server exe (runs on different machine)
    CLSCTX_INPROC_HANDLER16 = 0x20  # 16-bit handler dll (runs in same process as caller)
    CLSCTX_RESERVED1 = 0x40         # formerly INPROC_SERVERX86, deprecated
    CLSCTX_RESERVED2 = 0x80         # formerly INPROC_HANDLERX86, deprecated
    CLSCTX_RESERVED3 = 0x100        # formerly ESERVER_HANDLER, deprecated
    CLSCTX_RESERVED4 = 0x200        # formerly CLSCTX_KERNEL_SERVER, now used only in kmode
    CLSCTX_NO_CODE_DOWNLOAD = 0x400 # disallow code download from the Directory Service (if any) or the internet
    CLSCTX_RESERVED5 = 0x800        # formerly NO_WX86_TRANSLATION, deprecated
    CLSCTX_NO_CUSTOM_MARSHAL = 0x1000
    CLSCTX_ENABLE_CODE_DOWNLOAD = 0x2000
                                    # allow code download from the Directory Service (if any) or the internet
    CLSCTX_NO_FAILURE_LOG = 0x4000  # do not log messages about activation failure (should one occur) to Event Log
    CLSCTX_DISABLE_AAA   = 0x8000   # Disable activate-as-activator capability for this activation only
    CLSCTX_ENABLE_AAA   = 0x10000   # Enable activate-as-activator capability for this activation only
    CLSCTX_FROM_DEFAULT_CONTEXT = 0x20000   # Begin this activation from the default context of the current apartment
    CLSCTX_ACTIVATE_X86_SERVER    = 0x40000 # Pick x86 server only
    CLSCTX_ACTIVATE_32_BIT_SERVER = CLSCTX_ACTIVATE_X86_SERVER, # Old name for CLSCTX_ACTIVATE_X86_SERVER; value must be identical for compatibility
    CLSCTX_ACTIVATE_64_BIT_SERVER = 0x80000 # Pick 64-bit server only
    CLSCTX_ENABLE_CLOAKING = 0x100000 	      # Use the thread token (if present) for the activation.
    # The following flag is internal only
    CLSCTX_APPCONTAINER = 0x400000  # Internal CLSCTX used to indicate activation is for app container
    CLSCTX_ACTIVATE_AAA_AS_IU = 0x800000 # Interactive User activation behavior for As-Activator servers.
    CLSCTX_RESERVED6 = 0x1000000 # reserved
    CLSCTX_ACTIVATE_ARM32_SERVER  = 0x2000000 # Pick ARM32 server only
    CLSCTX_ALLOW_LOWER_TRUST_REGISTRATION = 0x4000000 # allow activations of servers configured in insufficiently trusted locations.
    CLSCTX_PS_DLL = 0x80000000 # Internal CLSCTX used for loading Proxy/Stub DLLs
    CLSCTX = INT

    CLSCTX_VALID_MASK = \
       (CLSCTX_INPROC_SERVER | \
        CLSCTX_INPROC_HANDLER | \
        CLSCTX_LOCAL_SERVER | \
        CLSCTX_INPROC_SERVER16 | \
        CLSCTX_REMOTE_SERVER | \
        CLSCTX_NO_CODE_DOWNLOAD | \
        CLSCTX_NO_CUSTOM_MARSHAL | \
        CLSCTX_ENABLE_CODE_DOWNLOAD | \
        CLSCTX_NO_FAILURE_LOG | \
        CLSCTX_DISABLE_AAA | \
        CLSCTX_ENABLE_AAA | \
        CLSCTX_FROM_DEFAULT_CONTEXT | \
        CLSCTX_ACTIVATE_X86_SERVER | \
        CLSCTX_ACTIVATE_64_BIT_SERVER | \
        CLSCTX_ENABLE_CLOAKING | \
        CLSCTX_APPCONTAINER | \
        CLSCTX_ACTIVATE_AAA_AS_IU | \
        CLSCTX_RESERVED6 | \
        CLSCTX_ACTIVATE_ARM32_SERVER | \
        CLSCTX_ALLOW_LOWER_TRUST_REGISTRATION | \
        CLSCTX_PS_DLL)

    # marshaling flags; passed to CoMarshalInterface
    MSHLFLAGS_NORMAL = 0       # normal marshaling via proxy/stub
    MSHLFLAGS_TABLESTRONG = 1  # keep object alive; must explicitly release
    MSHLFLAGS_TABLEWEAK = 2    # doesn't hold object alive; still must release
    MSHLFLAGS_NOPING = 4       # remote clients dont 'ping' to keep objects alive
    MSHLFLAGS_RESERVED1 = 8    # reserved
    MSHLFLAGS_RESERVED2 = 16   # reserved
    MSHLFLAGS_RESERVED3 = 32   # reserved
    MSHLFLAGS_RESERVED4 = 64   # reserved
    MSHLFLAGS = INT

    # marshal context: determines the destination context of the marshal operation
    MSHCTX_LOCAL = 0           # unmarshal context is local (e.g. shared memory)
    MSHCTX_NOSHAREDMEM = 1     # unmarshal context has no shared memory access
    MSHCTX_DIFFERENTMACHINE = 2# unmarshal context is on a different machine
    MSHCTX_INPROC = 3          # unmarshal context is on different thread
    MSHCTX_CROSSCTX = 4        # unmarshal context is on different context
    MSHCTX_RESERVED1 = 5       # reserved
    MSHCTX = INT

    # #######################################################################
    #
    #  User marshal support for Windows data types.

    #
    #  Frequently used helpers: sized blobs
    #
    #      Never put [user_marshal] or [wire_marshal] on the helpers directly.
    #

    # Simple blobs.
    
    class BYTE_BLOB(CStructure):
        _fields_ = [('clSize', ULONG)]
        
        abData: PBYTE
        
    array_after_structure(BYTE_BLOB, 'abData', BYTE)
    UP_BYTE_BLOB = BYTE_BLOB.PTR()
    
    class WORD_BLOB(CStructure):
        _fields_ = [('clSize', ULONG)]
        
        asData: PWORD
    
    array_after_structure(WORD_BLOB, 'asData', WORD)
    UP_WORD_BLOB = WORD_BLOB.PTR()
    
    class DWORD_BLOB(CStructure):
        _fields_ = [('clSize', ULONG)]
        
        alData: PDWORD
    
    array_after_structure(DWORD_BLOB, 'alData', DWORD)
    UP_DWORD_BLOB = DWORD_BLOB.PTR()
    
    # Flagged blobs.
    
    class FLAGGED_BYTE_BLOB(CStructure):
        _fields_ = [('fFlags', ULONG), ('clSize', ULONG)]
        
        abData: PBYTE
        fFlags: int
    
    array_after_structure(FLAGGED_BYTE_BLOB, 'abData', BYTE)
    UP_FLAGGED_BYTE_BLOB = FLAGGED_BYTE_BLOB.PTR()
    
    class FLAGGED_WORD_BLOB(CStructure):
        _fields_ = [('fFlags', ULONG), ('clSize', ULONG)]
        
        asData: PWORD
        fFlags: int
    
    array_after_structure(FLAGGED_WORD_BLOB, 'asData', WORD)
    UP_FLAGGED_WORD_BLOB = FLAGGED_WORD_BLOB.PTR()
    
    class FLAGGED_DWORD_BLOB(CStructure):
        _fields_ = [('fFlags', ULONG), ('clSize', ULONG)]
        
        alData: PDWORD
        fFlags: int
    
    array_after_structure(FLAGGED_DWORD_BLOB, 'abData', DWORD)
    UP_FLAGGED_DWORD_BLOB = FLAGGED_DWORD_BLOB.PTR()
    
    # Frequently used helpers with sized pointers.
    
    class BYTE_SIZEDARR(CStructure):
        _fields_ = [('clSize', ULONG), ('pData', PBYTE)]
        
        pData: PBYTE
        clSize: int
    
    class WORD_SIZEDARR(CStructure):
        _fields_ = [('clSize', ULONG), ('pData', PUSHORT)]
        
        pData: PUSHORT
        clSize: int
    
    class DWORD_SIZEDARR(CStructure):
        _fields_ = [('clSize', ULONG), ('pData', PULONG)]
        
        pData: PULONG
        clSize: int
    
    class HYPER_SIZEDARR(CStructure):
        _fields_ = [('clSize', ULONG), ('pData', PUINT64)]
        
        pData: IPointer[UINT64]
        clSize: int
    
    # #########################################################################
    #
    
    if cpreproc.pragma_once('_tagBLOB_DEFINED'):
        cpreproc.define('_BLOB_DEFINED')
        cpreproc.define('_LPBLOB_DEFINED')
        
        class BLOB(CStructure):
            _fields_ = [('cbSize', ULONG), ('pBlobData', PBYTE)]
        
            pBlobData: PBYTE
            cbSize: int
        
        LPBLOB = BLOB.PTR()
        
        # Access control - ntseapi.h
        class SID_IDENTIFIER_AUTHORITY(CStructure):
            _fields_ = [
                ("Value", BYTE * 6)
            ]
        PSID_IDENTIFIER_AUTHORITY = POINTER(SID_IDENTIFIER_AUTHORITY)
            
        class SID(CStructure):
            _fields_ = [
                ("Revision", BYTE),
                ("SubAuthorityCount", BYTE),
                ("IdentifierAuthority", SID_IDENTIFIER_AUTHORITY),
                ("SubAuthority", PDWORD)
            ]
        PISID = POINTER(SID)