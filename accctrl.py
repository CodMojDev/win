"""+-------------------------------------------------------------------

 Microsoft Windows
 Copyright (C) Microsoft Corporation, 1993-1998.

 File:       accctrl.h

 Contents:   common includes for new style Win32 Access Control
             APIs


--------------------------------------------------------------------"""

from . import cpreproc

if cpreproc.pragma_once("__ACCESS_CONTROL__"):
    from .winnt import *
    from .sdkddkver import *
    
    # REGION *** Application Family or OneCore Family ***
    
    #
    # Definition:
    # This enumerated type defines the objects supported by the get/set API within
    # this document.  See section 3.1, Object Types for a detailed definition of the
    # supported object types, and their name formats.
    #
    SE_UNKNOWN_OBJECT_TYPE = 0
    SE_FILE_OBJECT = 1
    SE_SERVICE = 2
    SE_PRINTER = 3
    SE_REGISTRY_KEY = 4
    SE_LMSHARE = 5
    SE_KERNEL_OBJECT = 6
    SE_WINDOW_OBJECT = 7
    SE_DS_OBJECT = 8
    SE_DS_OBJECT_ALL = 9
    SE_PROVIDER_DEFINED_OBJECT = 10
    SE_WMIGUID_OBJECT = 11
    SE_REGISTRY_WOW64_32KEY = 12
    SE_REGISTRY_WOW64_64KEY = 13
    SE_OBJECT_TYPE = DWORD

    #
    # Definition: TRUSTEE_TYPE
    # This enumerated type specifies the type of trustee account for the trustee
    # returned by the API described in this document.
    # TRUSTEE_IS_UNKNOWN - The trustee is an unknown, but not necessarily invalid
    #                      type.  This field is not validated on input to the APIs
    #                      that take Trustees.
    # TRUSTEE_IS_USER      The trustee account is a user account.
    # TRUSTEE_IS_GROUP     The trustee account is a group account.
    #

    TRUSTEE_IS_UNKNOWN = 0
    TRUSTEE_IS_USER = 1
    TRUSTEE_IS_GROUP = 2
    TRUSTEE_IS_DOMAIN = 3
    TRUSTEE_IS_ALIAS = 4
    TRUSTEE_IS_WELL_KNOWN_GROUP = 5
    TRUSTEE_IS_DELETED = 6
    TRUSTEE_IS_INVALID = 7
    TRUSTEE_IS_COMPUTER = 8
    TRUSTEE_TYPE = DWORD
    
    #
    # Definition: TRUSTEE_FORM
    # This enumerated type specifies the form the trustee identifier is in for a
    # particular trustee.
    # TRUSTEE_IS_SID       The trustee is identified with a SID rather than with a name.
    # TRUSTEE_IS_NAME      The trustee is identified with a name.
    #

    TRUSTEE_IS_SID = 0
    TRUSTEE_IS_NAME = 1
    TRUSTEE_BAD_FORM = 2
    TRUSTEE_IS_OBJECTS_AND_SID = 3
    TRUSTEE_IS_OBJECTS_AND_NAME = 4
    TRUSTEE_FORM = DWORD

    #
    # Definition: MULTIPLE_TRUSTEE_OPERATION
    # If the trustee is a multiple trustee, this enumerated type specifies the type.
    # TRUSTEE_IS_IMPERSONATE       The trustee is an impersonate trustee and the multiple
    #                          trustee field in the trustee points to another trustee
    #                          that is a trustee for the server that will be doing the
    #                          impersonation.
    #

    NO_MULTIPLE_TRUSTEE = 0
    TRUSTEE_IS_IMPERSONATE = 1
    MULTIPLE_TRUSTEE_OPERATION = DWORD

    class OBJECTS_AND_SID(CStructure):
        _fields_ = [
            ("ObjectsPresent", DWORD),
            ("ObjectTypeGuid", GUID),
            ("InheritedObjectTypeGuid", GUID),
            ("pSid", PSID)
        ]
        ObjectsPresent: int
        ObjectTypeGuid: GUID
        InheritedObjectTypeGuid: GUID
        pSid: IPointer[SID]
    POBJECTS_AND_SID = PTR(OBJECTS_AND_SID)

    class OBJECTS_AND_NAME_A(CStructure):
        _fields_ = [
            ("ObjectsPresent", DWORD),
            ("ObjectType", SE_OBJECT_TYPE),
            ("ObjectTypeName", LPSTR),
            ("InheritedObjectTypeName", LPSTR),
            ("ptstrName", LPSTR)
        ]
        ObjectsPresent: int
        ObjectType: int
        ObjectTypeName: LPSTR
        InheritedObjectTypeName: LPSTR
        ptstrName: LPSTR
    POBJECTS_AND_NAME_A = PTR(OBJECTS_AND_NAME_A)
    class OBJECTS_AND_NAME_W(CStructure):
        _fields_ = [
            ("ObjectsPresent", DWORD),
            ("ObjectType", SE_OBJECT_TYPE),
            ("ObjectTypeName", LPWSTR),
            ("InheritedObjectTypeName", LPWSTR),
            ("ptstrName", LPWSTR)
        ]
        ObjectsPresent: int
        ObjectType: int
        ObjectTypeName: LPWSTR
        InheritedObjectTypeName: LPWSTR
        ptstrName: LPWSTR
    POBJECTS_AND_NAME_W = PTR(OBJECTS_AND_NAME_W)
    
    OBJECTS_AND_NAME = unicode(OBJECTS_AND_NAME_W, OBJECTS_AND_NAME_A)
    POBJECTS_AND_NAME = unicode(POBJECTS_AND_NAME_W, POBJECTS_AND_NAME_A)

    #
    # Definition: TRUSTEE
    # This structure is used to pass account information into and out of the system
    # using the API defined in this document.
    # PMultipleTrustee     - if NON-NULL, points to another trustee structure, as
    #                    defined by the multiple trustee operation field.
    # MultipleTrusteeOperation - Defines the multiple trustee operation/type.
    # TrusteeForm - defines if the trustee is defined by name or SID.
    # TrusteeType - defines if the trustee type is unknown, a user or a group.
    # PwcsName     - points to the trustee name or the trustee SID.
    #

    class TRUSTEE_A(CStructure):
        pMultipleTrustee: IPointer['TRUSTEE_A']
        MultipleTrusteeOperation: int
        TrusteeForm: int
        TrusteeType: int
        ptstrName: LPCH
    TRUSTEE_A._fields_ = [
        ("pMultipleTrustee", PTR(TRUSTEE_A)),
        ("MultipleTrusteeOperation", MULTIPLE_TRUSTEE_OPERATION),
        ("TrusteeForm", TRUSTEE_FORM),
        ("TrusteeType", TRUSTEE_TYPE),
        # This member is not null-terminated as it may be used to hold strings, which are null-terminated or 
        # SIDs, which are not null-terminated.
        ("ptstrName", LPCH)
    ]
    TRUSTEEA = TRUSTEE_A
    PTRUSTEE_A = PTRUSTEEA = PTR(TRUSTEE_A)
    class TRUSTEE_W(CStructure):
        pMultipleTrustee: IPointer['TRUSTEE_W']
        MultipleTrusteeOperation: int
        TrusteeForm: int
        TrusteeType: int
        ptstrName: LPWCH
    TRUSTEE_W._fields_ = [
        ("pMultipleTrustee", PTR(TRUSTEE_W)),
        ("MultipleTrusteeOperation", MULTIPLE_TRUSTEE_OPERATION),
        ("TrusteeForm", TRUSTEE_FORM),
        ("TrusteeType", TRUSTEE_TYPE),
        # This member is not null-terminated as it may be used to hold strings, which are null-terminated or 
        # SIDs, which are not null-terminated.
        ("ptstrName", LPWCH)
    ]
    TRUSTEEW = TRUSTEE_W
    PTRUSTEE_W = PTRUSTEEW = PTR(TRUSTEE_W)
    TRUSTEE_ = TRUSTEE = unicode(TRUSTEE_W, TRUSTEE_A)
    PTRUSTEE_ = PTRUSTEE = unicode(PTRUSTEE_W, PTRUSTEE_A)

    #
    # Definition: ACCESS_MODE
    # This enumerated type specifies how permissions are (requested)/to be applied
    #  for the trustee by the access control entry.  On input this field can by any
    #  of the values, although it is not meaningful to mix access control and audit
    #  control entries.  On output this field will be either SET_ACCESS, DENY_ACCESS,
    # SET_AUDIT_SUCCESS, SET_AUDIT_FAILURE.
    # The following descriptions define how this type effects an explicit access
    # request to apply access permissions to an object.
    # GRANT_ACCESS - The trustee will have at least the requested permissions upon
    #                successful completion of the command. (If the trustee has
    #                additional permissions they will not be removed).
    # SET_ACCESS - The trustee will have exactly the requested permissions upon
    #              successful completion of the command.
    # DENY_ACCESS - The trustee will be denied the specified permissions.
    # REVOKE_ACCESS - Any explicit access rights the trustee has will be revoked.
    # SET_AUDIT_SUCCESS - The trustee will be audited for successful opens of the
    #                     object using the requested permissions.
    # SET_AUDIT_FAILURE - The trustee will be audited for failed opens of the object
    #                     using the requested permissions.
    #

    NOT_USED_ACCESS = 0
    GRANT_ACCESS = 1
    SET_ACCESS = 2
    DENY_ACCESS = 3
    REVOKE_ACCESS = 4
    SET_AUDIT_SUCCESS = 5
    SET_AUDIT_FAILURE = 6
    ACCESS_MODE = DWORD

    #
    # Definition: Inheritance flags
    # These bit masks are provided to allow simple application of inheritance in
    # explicit access requests on containers.
    # NO_INHERITANCE       The specific access permissions will only be applied to
    #                  the container, and will not be inherited by objects created
    #                  within the container.
    # SUB_CONTAINERS_ONLY_INHERIT  The specific access permissions will be inherited
    #                              and applied to sub containers created within the
    #                              container, and will be applied to the container
    #                              itself.
    # SUB_OBJECTS_ONLY_INHERIT     The specific access permissions will only be inherited
    #                              by objects created within the specific container.
    #                              The access permissions will not be applied to the
    #                              container itself.
    # SUB_CONTAINERS_AND_OBJECTS_INHERIT   The specific access permissions will be
    #                                      inherited by containers created within the
    #                                      specific container, will be applied to
    #                                      objects created within the container, but
    #                                      will not be applied to the container itself.
    #
    NO_INHERITANCE = 0x0
    SUB_OBJECTS_ONLY_INHERIT            = 0x1
    SUB_CONTAINERS_ONLY_INHERIT         = 0x2
    SUB_CONTAINERS_AND_OBJECTS_INHERIT  = 0x3
    INHERIT_NO_PROPAGATE                = 0x4
    INHERIT_ONLY                        = 0x8

    #
    # Informational bit that is returned
    #
    INHERITED_ACCESS_ENTRY              = 0x10

    #
    # Informational bit that tells where a node was inherited from.  Valid only
    # for NT 5 APIs
    #
    INHERITED_PARENT                    = 0x10000000
    INHERITED_GRANDPARENT               = 0x20000000

    #
    # Definition: EXPLICIT_ACCESS
    # This structure is used to pass access control entry information into and out
    # of the system using the API defined in this document.
    # grfAccessPermissions - This contains the access permissions to assign for the
    #                     trustee.  It is in the form of an NT access mask.
    # grfAccessMode - This field defines how the permissions are to be applied for
    #                 the trustee.
    # grfInheritance - For containers, this field defines how the access control
    #                  entry is/(is requested) to be inherited on
    #                  objects/sub-containers created within the container.
    # Trustee - This field contains the definition of the trustee account the
    #           explicit access applies to.
    #

    class EXPLICIT_ACCESS_A(CStructure):
        _fields_ = [
            ("grfAccessPermissions", DWORD),
            ("grfAccessMode", ACCESS_MODE),
            ("grfInheritance", DWORD),
            ("Trustee", TRUSTEE_A)
        ]
        grfAccessPermissions: int
        grfAccessMode: int
        grfInheritance: int
        Trustee: TRUSTEE_A
    EXPLICIT_ACCESSA = EXPLICIT_ACCESS_A
    PEXPLICIT_ACCESS_A = PEXPLICIT_ACCESSA = PTR(EXPLICIT_ACCESS_A)
    
    class EXPLICIT_ACCESS_W(CStructure):
        _fields_ = [
            ("grfAccessPermissions", DWORD),
            ("grfAccessMode", ACCESS_MODE),
            ("grfInheritance", DWORD),
            ("Trustee", TRUSTEE_W)
        ]
        grfAccessPermissions: int
        grfAccessMode: int
        grfInheritance: int
        Trustee: TRUSTEE_W
    EXPLICIT_ACCESSW = EXPLICIT_ACCESS_W
    PEXPLICIT_ACCESS_W = PEXPLICIT_ACCESSW = PTR(EXPLICIT_ACCESS_W)
    
    EXPLICIT_ACCESS_ = EXPLICIT_ACCESS = unicode(EXPLICIT_ACCESS_W, EXPLICIT_ACCESS_A)
    PEXPLICIT_ACCESS_ = PEXPLICIT_ACCESS = unicode(PEXPLICIT_ACCESS_W, PEXPLICIT_ACCESS_A)

    #----------------------------------------------------------------------------
    #
    #                                  NT5 APIs
    #
    #----------------------------------------------------------------------------

    #
    # Default provider
    #
    ACCCTRL_DEFAULT_PROVIDERA  = b"Windows NT Access Provider"
    ACCCTRL_DEFAULT_PROVIDERW  =  "Windows NT Access Provider"
    ACCCTRL_DEFAULT_PROVIDER   = unicode(ACCCTRL_DEFAULT_PROVIDERW, ACCCTRL_DEFAULT_PROVIDERA)
    
    #
    # Access rights
    #
    ACCESS_RIGHTS = ULONG
    PACCESS_RIGHTS = PULONG

    #
    # Inheritance flags
    #
    INHERIT_FLAGS = ULONG
    PINHERIT_FLAGS = PULONG

    #
    # Access / Audit structures
    #
    class ACTRL_ACCESS_ENTRYA(CStructure):
        _fields_ = [
            ("Trustee", TRUSTEE_A),
            ("fAccessFlags", ULONG),
            ("Access", ACCESS_RIGHTS),
            ("ProvSpecificAccess", ACCESS_RIGHTS),
            ("Inheritance", INHERIT_FLAGS),
            ("lpInheritProperty", LPSTR)
        ]
        Trustee: TRUSTEE_A
        fAccessFlags: int
        Access: int
        ProvSpecificAccess: int
        Inheritance: int
        lpInheritProperty: LPSTR
    PACTRL_ACCESS_ENTRYA = PTR(ACTRL_ACCESS_ENTRYA)
    
    #
    # Access / Audit structures
    #
    class ACTRL_ACCESS_ENTRYW(CStructure):
        _fields_ = [
            ("Trustee", TRUSTEE_W),
            ("fAccessFlags", ULONG),
            ("Access", ACCESS_RIGHTS),
            ("ProvSpecificAccess", ACCESS_RIGHTS),
            ("Inheritance", INHERIT_FLAGS),
            ("lpInheritProperty", LPWSTR)
        ]
        Trustee: TRUSTEE_W
        fAccessFlags: int
        Access: int
        ProvSpecificAccess: int
        Inheritance: int
        lpInheritProperty: LPWSTR
    PACTRL_ACCESS_ENTRYW = PTR(ACTRL_ACCESS_ENTRYW)
    
    ACTRL_ACCESS_ENTRY = unicode(ACTRL_ACCESS_ENTRYW, ACTRL_ACCESS_ENTRYA)
    PACTRL_ACCESS_ENTRY = unicode(PACTRL_ACCESS_ENTRYW, PACTRL_ACCESS_ENTRYA)

    class ACTRL_ACCESS_ENTRY_LISTA(CStructure):
        _fields_ = [
            ("cEntries", ULONG),
            ("pAccessList", PACTRL_ACCESS_ENTRYA)
        ]
        cEntries: int
        pAccessList: IPointer[ACTRL_ACCESS_ENTRYA]
    PACTRL_ACCESS_ENTRY_LISTA = PTR(ACTRL_ACCESS_ENTRY_LISTA)
    class ACTRL_ACCESS_ENTRY_LISTW(CStructure):
        _fields_ = [
            ("cEntries", ULONG),
            ("pAccessList", PACTRL_ACCESS_ENTRYW)
        ]
        cEntries: int
        pAccessList: IPointer[ACTRL_ACCESS_ENTRYW]
    PACTRL_ACCESS_ENTRY_LISTW = PTR(ACTRL_ACCESS_ENTRY_LISTW)
    
    ACTRL_ACCESS_ENTRY_LIST = unicode(ACTRL_ACCESS_ENTRY_LISTW, ACTRL_ACCESS_ENTRY_LISTA)
    PACTRL_ACCESS_ENTRY_LIST = unicode(PACTRL_ACCESS_ENTRY_LISTW, PACTRL_ACCESS_ENTRY_LISTA)
    
    class ACTRL_PROPERTY_ENTRYA(CStructure):
        _fields_ = [
            ("lpProperty", LPSTR),
            ("pAccessEntryList", PACTRL_ACCESS_ENTRY_LISTA),
            ("fListFlags", ULONG)
        ]
        lpProperty: LPSTR
        pAccessEntryList: IPointer[ACTRL_ACCESS_ENTRY_LISTA]
        fListFlags: int
    PACTRL_PROPERTY_ENTRYA = PTR(ACTRL_PROPERTY_ENTRYA)
    class ACTRL_PROPERTY_ENTRYW(CStructure):
        _fields_ = [
            ("lpProperty", LPWSTR),
            ("pAccessEntryList", PACTRL_ACCESS_ENTRY_LISTW),
            ("fListFlags", ULONG)
        ]
        lpProperty: LPWSTR
        pAccessEntryList: IPointer[ACTRL_ACCESS_ENTRY_LISTW]
        fListFlags: int
    PACTRL_PROPERTY_ENTRYW = PTR(ACTRL_PROPERTY_ENTRYW)
    
    ACTRL_PROPERTY_ENTRY = unicode(ACTRL_PROPERTY_ENTRYW, ACTRL_PROPERTY_ENTRYA)
    PACTRL_PROPERTY_ENTRY = unicode(PACTRL_PROPERTY_ENTRYW, PACTRL_PROPERTY_ENTRYA)

    class ACTRL_ALISTA(CStructure):
        _fields_ = [
            ("cEntries", ULONG),
            ("pPropertyAccessList", PACTRL_PROPERTY_ENTRYA)
        ]
        cEntries: int
        pPropertyAccessList: IPointer[ACTRL_PROPERTY_ENTRYA]
    ACTRL_ACCESSA = ACTRL_AUDITA = ACTRL_ALISTA
    PACTRL_ACCESSA = PACTRL_AUDITA = PTR(ACTRL_ALISTA)
    class ACTRL_ALISTW(CStructure):
        _fields_ = [
            ("cEntries", ULONG),
            ("pPropertyAccessList", PACTRL_PROPERTY_ENTRYW)
        ]
        cEntries: int
        pPropertyAccessList: IPointer[ACTRL_PROPERTY_ENTRYW]
    ACTRL_ACCESSW = ACTRL_AUDITW = ACTRL_ALISTW
    PACTRL_ACCESSW = PACTRL_AUDITW = PTR(ACTRL_ALISTW)
    
    ACTRL_ACCESS = ACTRL_AUDIT = unicode(ACTRL_ALISTW, ACTRL_ALISTA)
    PACTRL_ACCESS = unicode(PACTRL_ACCESSW, PACTRL_ACCESSA)
    PACTRL_AUDIT = unicode(PACTRL_AUDITW, PACTRL_AUDITA)

    #
    # TRUSTEE_ACCESS flags
    #
    TRUSTEE_ACCESS_ALLOWED      = 0x00000001
    TRUSTEE_ACCESS_READ         = 0x00000002
    TRUSTEE_ACCESS_WRITE        = 0x00000004

    TRUSTEE_ACCESS_EXPLICIT     = 0x00000001
    TRUSTEE_ACCESS_READ_WRITE   = (TRUSTEE_ACCESS_READ | \
                                   TRUSTEE_ACCESS_WRITE)

    TRUSTEE_ACCESS_ALL          = 0xFFFFFFFF

    class TRUSTEE_ACCESSA(CStructure):
        _fields_ = [
            ("lpProperty", LPSTR),
            ("fAccess", ACCESS_RIGHTS),
            ("fAccessFlags", ULONG),
            ("fReturnedAccess", ULONG)
        ]
        lpProperty: LPSTR
        fAccess: int
        fAccessFlags: int
        fReturnedAccess: int
    PTRUSTEE_ACCESSA = PTR(TRUSTEE_ACCESSA)
    
    class TRUSTEE_ACCESSW(CStructure):
        _fields_ = [
            ("lpProperty", LPWSTR),
            ("fAccess", ACCESS_RIGHTS),
            ("fAccessFlags", ULONG),
            ("fReturnedAccess", ULONG)
        ]
        lpProperty: LPWSTR
        fAccess: int
        fAccessFlags: int
        fReturnedAccess: int
    PTRUSTEE_ACCESSW = PTR(TRUSTEE_ACCESSW)
    
    TRUSTEE_ACCESS = unicode(TRUSTEE_ACCESSW, TRUSTEE_ACCESSA)
    PTRUSTEE_ACCESS = unicode(PTRUSTEE_ACCESSW, PTRUSTEE_ACCESSA)

    #
    # Generic permission values
    #
    ACTRL_RESERVED          = 0x00000000
    ACTRL_PERM_1            = 0x00000001
    ACTRL_PERM_2            = 0x00000002
    ACTRL_PERM_3            = 0x00000004
    ACTRL_PERM_4            = 0x00000008
    ACTRL_PERM_5            = 0x00000010
    ACTRL_PERM_6            = 0x00000020
    ACTRL_PERM_7            = 0x00000040
    ACTRL_PERM_8            = 0x00000080
    ACTRL_PERM_9            = 0x00000100
    ACTRL_PERM_10           = 0x00000200
    ACTRL_PERM_11           = 0x00000400
    ACTRL_PERM_12           = 0x00000800
    ACTRL_PERM_13           = 0x00001000
    ACTRL_PERM_14           = 0x00002000
    ACTRL_PERM_15           = 0x00004000
    ACTRL_PERM_16           = 0x00008000
    ACTRL_PERM_17           = 0x00010000
    ACTRL_PERM_18           = 0x00020000
    ACTRL_PERM_19           = 0x00040000
    ACTRL_PERM_20           = 0x00080000

    #
    # Access permissions
    #
    ACTRL_ACCESS_ALLOWED        = 0x00000001
    ACTRL_ACCESS_DENIED         = 0x00000002
    ACTRL_AUDIT_SUCCESS         = 0x00000004
    ACTRL_AUDIT_FAILURE         = 0x00000008

    #
    # Property list flags
    #
    ACTRL_ACCESS_PROTECTED      = 0x00000001

    #
    # Standard and object rights
    #
    ACTRL_SYSTEM_ACCESS         = 0x04000000
    ACTRL_DELETE                = 0x08000000
    ACTRL_READ_CONTROL          = 0x10000000
    ACTRL_CHANGE_ACCESS         = 0x20000000
    ACTRL_CHANGE_OWNER          = 0x40000000
    ACTRL_SYNCHRONIZE           = 0x80000000
    ACTRL_STD_RIGHTS_ALL        = 0xf8000000
    ACTRL_STD_RIGHT_REQUIRED    = ( ACTRL_STD_RIGHTS_ALL & ~ACTRL_SYNCHRONIZE )

    ACTRL_DS_OPEN                           = ACTRL_RESERVED
    ACTRL_DS_CREATE_CHILD                   = ACTRL_PERM_1
    ACTRL_DS_DELETE_CHILD                   = ACTRL_PERM_2
    ACTRL_DS_LIST                           = ACTRL_PERM_3
    ACTRL_DS_SELF                           = ACTRL_PERM_4
    ACTRL_DS_READ_PROP                      = ACTRL_PERM_5
    ACTRL_DS_WRITE_PROP                     = ACTRL_PERM_6
    ACTRL_DS_DELETE_TREE                    = ACTRL_PERM_7
    ACTRL_DS_LIST_OBJECT                    = ACTRL_PERM_8
    ACTRL_DS_CONTROL_ACCESS                 = ACTRL_PERM_9

    ACTRL_FILE_READ                         = ACTRL_PERM_1
    ACTRL_FILE_WRITE                        = ACTRL_PERM_2
    ACTRL_FILE_APPEND                       = ACTRL_PERM_3
    ACTRL_FILE_READ_PROP                    = ACTRL_PERM_4
    ACTRL_FILE_WRITE_PROP                   = ACTRL_PERM_5
    ACTRL_FILE_EXECUTE                      = ACTRL_PERM_6
    ACTRL_FILE_READ_ATTRIB                  = ACTRL_PERM_8
    ACTRL_FILE_WRITE_ATTRIB                 = ACTRL_PERM_9
    ACTRL_FILE_CREATE_PIPE                  = ACTRL_PERM_10
    ACTRL_DIR_LIST                          = ACTRL_PERM_1
    ACTRL_DIR_CREATE_OBJECT                 = ACTRL_PERM_2
    ACTRL_DIR_CREATE_CHILD                  = ACTRL_PERM_3
    ACTRL_DIR_DELETE_CHILD                  = ACTRL_PERM_7
    ACTRL_DIR_TRAVERSE                      = ACTRL_PERM_6
    ACTRL_KERNEL_TERMINATE                  = ACTRL_PERM_1
    ACTRL_KERNEL_THREAD                     = ACTRL_PERM_2
    ACTRL_KERNEL_VM                         = ACTRL_PERM_3
    ACTRL_KERNEL_VM_READ                    = ACTRL_PERM_4
    ACTRL_KERNEL_VM_WRITE                   = ACTRL_PERM_5
    ACTRL_KERNEL_DUP_HANDLE                 = ACTRL_PERM_6
    ACTRL_KERNEL_PROCESS                    = ACTRL_PERM_7
    ACTRL_KERNEL_SET_INFO                   = ACTRL_PERM_8
    ACTRL_KERNEL_GET_INFO                   = ACTRL_PERM_9
    ACTRL_KERNEL_CONTROL                    = ACTRL_PERM_10
    ACTRL_KERNEL_ALERT                      = ACTRL_PERM_11
    ACTRL_KERNEL_GET_CONTEXT                = ACTRL_PERM_12
    ACTRL_KERNEL_SET_CONTEXT                = ACTRL_PERM_13
    ACTRL_KERNEL_TOKEN                      = ACTRL_PERM_14
    ACTRL_KERNEL_IMPERSONATE                = ACTRL_PERM_15
    ACTRL_KERNEL_DIMPERSONATE               = ACTRL_PERM_16
    ACTRL_PRINT_SADMIN                      = ACTRL_PERM_1
    ACTRL_PRINT_SLIST                       = ACTRL_PERM_2
    ACTRL_PRINT_PADMIN                      = ACTRL_PERM_3
    ACTRL_PRINT_PUSE                        = ACTRL_PERM_4
    ACTRL_PRINT_JADMIN                      = ACTRL_PERM_5
    ACTRL_SVC_GET_INFO                      = ACTRL_PERM_1
    ACTRL_SVC_SET_INFO                      = ACTRL_PERM_2
    ACTRL_SVC_STATUS                        = ACTRL_PERM_3
    ACTRL_SVC_LIST                          = ACTRL_PERM_4
    ACTRL_SVC_START                         = ACTRL_PERM_5
    ACTRL_SVC_STOP                          = ACTRL_PERM_6
    ACTRL_SVC_PAUSE                         = ACTRL_PERM_7
    ACTRL_SVC_INTERROGATE                   = ACTRL_PERM_8
    ACTRL_SVC_UCONTROL                      = ACTRL_PERM_9
    ACTRL_REG_QUERY                         = ACTRL_PERM_1
    ACTRL_REG_SET                           = ACTRL_PERM_2
    ACTRL_REG_CREATE_CHILD                  = ACTRL_PERM_3
    ACTRL_REG_LIST                          = ACTRL_PERM_4
    ACTRL_REG_NOTIFY                        = ACTRL_PERM_5
    ACTRL_REG_LINK                          = ACTRL_PERM_6
    ACTRL_WIN_CLIPBRD                       = ACTRL_PERM_1
    ACTRL_WIN_GLOBAL_ATOMS                  = ACTRL_PERM_2
    ACTRL_WIN_CREATE                        = ACTRL_PERM_3
    ACTRL_WIN_LIST_DESK                     = ACTRL_PERM_4
    ACTRL_WIN_LIST                          = ACTRL_PERM_5
    ACTRL_WIN_READ_ATTRIBS                  = ACTRL_PERM_6
    ACTRL_WIN_WRITE_ATTRIBS                 = ACTRL_PERM_7
    ACTRL_WIN_SCREEN                        = ACTRL_PERM_8
    ACTRL_WIN_EXIT                          = ACTRL_PERM_9

    class ACTRL_OVERLAPPED(CStructure):
        class _U(CUnion):
            _fields_ = [
                ("Provider", PVOID),
                ("Reserved1", ULONG)
            ]
        _fields_ = [
            ("_u", _U),
            ("Reserved2", ULONG),
            ("hEvent", HANDLE)
        ]
        Provider: int
        Reserved1: int
        Reserved2: int
        hEvent: int
    PACTRL_OVERLAPPED = PTR(ACTRL_OVERLAPPED)

    class ACTRL_ACCESS_INFOA(CStructure):
        _fields_ = [
            ("fAccessPermission", ULONG),
            ("lpAccessPermissionName", LPSTR)
        ]
        fAccessPermission: int
        lpAccessPermissionName: LPSTR
    PACTRL_ACCESS_INFOA = PTR(ACTRL_ACCESS_INFOA)
    
    class ACTRL_ACCESS_INFOW(CStructure):
        _fields_ = [
            ("fAccessPermission", ULONG),
            ("lpAccessPermissionName", LPWSTR)
        ]
        fAccessPermission: int
        lpAccessPermissionName: LPWSTR
    PACTRL_ACCESS_INFOW = PTR(ACTRL_ACCESS_INFOW)
    
    ACTRL_ACCESS_INFO = unicode(ACTRL_ACCESS_INFOW, ACTRL_ACCESS_INFOA)
    PACTRL_ACCESS_INFO = unicode(PACTRL_ACCESS_INFOW, PACTRL_ACCESS_INFOA)

    class ACTRL_CONTROL_INFOA(CStructure):
        _fields_ = [
            ("lpControlId", LPSTR),
            ("lpControlName", LPSTR)
        ]
        lpControlId: LPSTR
        lpControlName: LPSTR
    PACTRL_CONTROL_INFOA = PTR(ACTRL_CONTROL_INFOA)
    class ACTRL_CONTROL_INFOW(CStructure):
        _fields_ = [
            ("lpControlId", LPWSTR),
            ("lpControlName", LPWSTR)
        ]
        lpControlId: LPWSTR
        lpControlName: LPWSTR
    PACTRL_CONTROL_INFOW = PTR(ACTRL_CONTROL_INFOW)
    
    ACTRL_CONTROL_INFO = unicode(ACTRL_CONTROL_INFOW, ACTRL_CONTROL_INFOA)
    PACTRL_CONTROL_INFO = unicode(PACTRL_CONTROL_INFOW, PACTRL_CONTROL_INFOA)

    ACTRL_ACCESS_NO_OPTIONS                 = 0x00000000
    ACTRL_ACCESS_SUPPORTS_OBJECT_ENTRIES    = 0x00000001

    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        TREE_SEC_INFO_SET                   = 0x00000001
        TREE_SEC_INFO_RESET                 = 0x00000002
        TREE_SEC_INFO_RESET_KEEP_EXPLICIT   = 0x00000003

    ProgressInvokeNever = 1            # Never invoke the progress function
    ProgressInvokeEveryObject = 2      # Invoke for each object
    ProgressInvokeOnError = 3          # Invoke only for each error case
    ProgressCancelOperation = 4        # Stop propagation and return
    ProgressRetryOperation = 5         # Retry operation on subtree
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        ProgressInvokePrePostError = 6 # Invoke Pre, Post, Error
    PROG_INVOKE_SETTING = DWORD
    PPROG_INVOKE_SETTING = PDWORD

    #
    # Progress Function:
    # Caller of tree operation implements this Progress function, then
    # passes its function pointer to tree operation.
    # Tree operation invokes Progress function to provide progress and error
    # information to the caller during the potentially long execution
    # of the tree operation.  Tree operation provides the name of the object
    # last processed and the error status of the operation on that object.
    # Tree operation also passes the current InvokeSetting value.
    # Caller may change the InvokeSetting value, for example, from "Always"
    # to "Only On Error."
    #

    """
    typedef VOID (*FN_PROGRESS) (
        IN LPWSTR                   pObjectName,    # name of object just processed
        IN DWORD                    Status,         # status of operation on object
        IN OUT PPROG_INVOKE_SETTING pInvokeSetting, # Never, always,
        IN PVOID                    Args,           # Caller specific data
        IN BOOL                     SecuritySet     # Whether security was set
        );
    """

    #
    # New Object Type function pointers.  TBD.
    # To support additional object resource managers generically, the
    # resource manager must provide it's own functions for operations
    # like:
    # GetAncestorAcl(IN ObjName, IN GenerationGap, IN DaclOrSacl?, ...)
    # GetAncestorName(...)
    # FreeNameStructure(...)
    #

    class FN_OBJECT_MGR_FUNCTIONS(CStructure):
        _fields_ = [
            ("Placeholder", ULONG)
        ]
        Placeholder: int
    PFN_OBJECT_MGR_FUNCTS = PTR(FN_OBJECT_MGR_FUNCTIONS)

    #
    # Name of ancestor and number of generations between
    # ancestor and inheriting object.
    #
    # GenerationGap:
    #     Name of ancestor from which ACE was inherited.
    #     NULL for explicit ACE.
    #
    # AncestorName:
    #     Number of levels (or generations) between the object and the ancestor.
    #     Parent, gap=1.
    #     Grandparent, gap=2.
    #     Set to 0 for explicit ACE on object.
    #

    class INHERITED_FROMA(CStructure):
        _fields_ = [
            ("GenerationGap", LONG),
            ("AncestorName", LPSTR)
        ]
        GenerationGap: int
        AncestorName: LPSTR
    PINHERITED_FROMA = PTR(INHERITED_FROMA)
    
    class INHERITED_FROMW(CStructure):
        _fields_ = [
            ("GenerationGap", LONG),
            ("AncestorName", LPWSTR)
        ]
        GenerationGap: int
        AncestorName: LPWSTR
    PINHERITED_FROMW = PTR(INHERITED_FROMW)
    
    INHERITED_FROM = unicode(INHERITED_FROMW, INHERITED_FROMA)
    PINHERITED_FROM = unicode(PINHERITED_FROMW, PINHERITED_FROMA)

    # REGION ***