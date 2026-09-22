"""
+--------------------------------------------------------------------------

 Microsoft Windows
 Copyright (c) Microsoft Corporation. All rights reserved.

 File:       aclui.h

 Contents:   Definitions and prototypes for the ACLUI.DLL

---------------------------------------------------------------------------
"""

from . import cpreproc

if cpreproc.pragma_once("_ACLUI_H_"):
    aclui = get_win_library("aclui.dll")
    
    from .prsht import *
    from .com.objinterfacedef import *
    from .accctrl import *
    # from .authz import *
    
    # REGION *** Desktop Family ***
    
    class SI_OBJECT_INFO(CStructure):
        _fields_ = [
            ("dwFlags", DWORD),
            ("hInstance", HINSTANCE),  # resources (e.g. strings) reside here
            ("pszServerName", LPWSTR), # must be present
            ("pszObjectName", LPWSTR), # must be present
            ("pszPageTitle", LPWSTR),  # only valid if SI_PAGE_TITLE is set
            ("guidObjectType", GUID)   # only valid if SI_OBJECT_GUID is set
        ]
        dwFlags: int
        hInstance: int
        pszServerName: LPWSTR
        pszObjectName: LPWSTR
        pszPageTitle: LPWSTR
        guidObjectType: int
    PSI_OBJECT_INFO = PTR(SI_OBJECT_INFO)
    
    # SI_OBJECT_INFO flags
    SI_EDIT_PERMS                = 0x00000000 # always implied
    SI_EDIT_OWNER                = 0x00000001
    SI_EDIT_AUDITS               = 0x00000002
    SI_CONTAINER                 = 0x00000004
    SI_READONLY                  = 0x00000008
    SI_ADVANCED                  = 0x00000010
    SI_RESET                     = 0x00000020 #equals to SI_RESET_DACL|SI_RESET_SACL|SI_RESET_OWNER
    SI_OWNER_READONLY            = 0x00000040
    SI_EDIT_PROPERTIES           = 0x00000080
    SI_OWNER_RECURSE             = 0x00000100
    SI_NO_ACL_PROTECT            = 0x00000200
    SI_NO_TREE_APPLY             = 0x00000400
    SI_PAGE_TITLE                = 0x00000800
    SI_SERVER_IS_DC              = 0x00001000
    SI_RESET_DACL_TREE           = 0x00004000
    SI_RESET_SACL_TREE           = 0x00008000
    SI_OBJECT_GUID               = 0x00010000
    SI_EDIT_EFFECTIVE            = 0x00020000
    SI_RESET_DACL                = 0x00040000
    SI_RESET_SACL                = 0x00080000
    SI_RESET_OWNER               = 0x00100000
    SI_NO_ADDITIONAL_PERMISSION  = 0x00200000
    
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        SI_VIEW_ONLY                 = 0x00400000
        SI_PERMS_ELEVATION_REQUIRED  = 0x01000000
        SI_AUDITS_ELEVATION_REQUIRED = 0x02000000
        SI_OWNER_ELEVATION_REQUIRED  = 0x04000000

        if cpreproc.get_version() >= WIN32_WINNT_WIN8:
            SI_SCOPE_ELEVATION_REQUIRED  = 0x08000000

    SI_MAY_WRITE                 = 0x10000000 #not sure if user can write permission

    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        SI_ENABLE_EDIT_ATTRIBUTE_CONDITION = 0x20000000
        SI_ENABLE_CENTRAL_POLICY           = 0x40000000
        SI_DISABLE_DENY_ACE                = 0x80000000

    SI_EDIT_ALL = (SI_EDIT_PERMS | SI_EDIT_OWNER | SI_EDIT_AUDITS)
    
    class SI_ACCESS(CStructure):
        _fields_ = [
            ("pguid", PGUID),
            ("mask", ACCESS_MASK),
            ("pszName", LPCWSTR), # may be resource ID
            ("dwFlags", DWORD)
        ]
        pguid: IPointer[GUID]
        mask: int
        pszName: LPCWSTR
        dwFlags: int 
    PSI_ACCESS = PTR(SI_ACCESS)
    
    # SI_ACCESS flags
    SI_ACCESS_SPECIFIC  = 0x00010000
    SI_ACCESS_GENERAL   = 0x00020000
    SI_ACCESS_CONTAINER = 0x00040000 # general access, container-only
    SI_ACCESS_PROPERTY  = 0x00080000
    # ACE inheritance flags (CONTAINER_INHERIT_ACE, etc.) may also be set.
    # They will be used as the inheritance when an access is turned on.
        
    class SI_INHERIT_TYPE(CStructure):
        _fields_ = [
            ("pguid", PGUID),
            ("dwFlags", ULONG),
            ("pszName", LPCWSTR) # may be resource ID
        ]
        pguid: IPointer[GUID]
        dwFlags: int
        pszName: LPCWSTR
    PSI_INHERIT_TYPE = PTR(SI_INHERIT_TYPE)
    
    # For EditSecurityEx/2, the argument actually takes a UINT
    # The bottom half is SI_PAGE_TYPE, so the enum value for this
    # should never be greater than 0x0000ffff
    SI_PAGE_PERM = 0
    SI_PAGE_ADVPERM = 1
    SI_PAGE_AUDIT = 2
    SI_PAGE_OWNER = 3
    SI_PAGE_EFFECTIVE = 4
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        SI_PAGE_TAKEOWNERSHIP = 5
        if cpreproc.get_version() >= WIN32_WINNT_WIN8:
            SI_PAGE_SHARE = 6
    
    SI_PAGE_TYPE = DWORD

    #
    # Page types used by the new advanced ACL UI
    #
    SI_SHOW_DEFAULT = 0
    SI_SHOW_PERM_ACTIVATED = 1
    SI_SHOW_AUDIT_ACTIVATED = 2
    SI_SHOW_OWNER_ACTIVATED = 3
    SI_SHOW_EFFECTIVE_ACTIVATED = 4
    SI_SHOW_SHARE_ACTIVATED = 5
    SI_SHOW_CENTRAL_POLICY_ACTIVATED = 6
    SI_PAGE_ACTIVATED = DWORD

    def GET_PAGE_TYPE(X: int) -> int:
        return UINT(X & 0x0000ffff).value
    
    def GET_ACTIVATION_TYPE(Y: int) -> int:
        return UINT((Y >> 16) & 0x0000ffff).value
    
    def COMBINE_PAGE_ACTIVATION(X: int, Y: int) -> int:
        return UINT((Y << 16) | X).value

    DOBJ_RES_CONT           = 0x00000001
    DOBJ_RES_ROOT           = 0x00000002
    DOBJ_VOL_NTACLS         = 0x00000004     # NTFS or OFS
    DOBJ_COND_NTACLS        = 0x00000008     # Conditional aces supported.
    DOBJ_RIBBON_LAUNCH      = 0x00000010     # Invoked from explorer ribbon.

    # Message to PropertySheetPageCallback (in addition to
    # PSPCB_CREATE and PSPCB_RELEASE)
    PSPCB_SI_INITDIALOG    = (WM_USER + 1)
        
    class ISecurityInformation(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{965FC360-16FF-11d0-91CB-00AA00BBB723}")
        
        @virtual_table.com_function(PSI_OBJECT_INFO)
        def GetObjectInformation(self, pObjectInfo: IPointer[SI_OBJECT_INFO]) -> int: ...
        
        @virtual_table.com_function(SECURITY_INFORMATION, PTR(PSECURITY_DESCRIPTOR), BOOL)
        def GetSecurity(self, RequestedInformation: int, ppSecurityDescriptor: IDoublePtr[SECURITY_DESCRIPTOR], fDefault: int) -> int: ...
        
        @virtual_table.com_function(SECURITY_INFORMATION, PSECURITY_DESCRIPTOR)
        def SetSecurity(self, SecurityInformation: int, pSecurityDescriptor: IPointer[SECURITY_DESCRIPTOR]) -> int: ...
        
        @virtual_table.com_function(PGUID, PBYTE, PACCESS_MASK)
        def MapGeneric(self, pguidObjectType: IPointer[GUID], pAceFlags: IPointer[BYTE], pMask: IPointer[ACCESS_MASK]) -> int: ...
        
        @virtual_table.com_function(PTR(PSI_INHERIT_TYPE), PULONG)
        def GetInheritTypes(self, ppInheritTypes: IDoublePtr[SI_INHERIT_TYPE], pcInheritTypes: IPointer[ULONG]) -> int: ...
        
        @virtual_table.com_function(HWND, UINT, SI_PAGE_TYPE)
        def PropertySheetPageCallback(self, hwnd: int, uMsg: int, uPage: int) -> int: ...
        
        virtual_table.build()
    LPSECURITYINFO = PTR(ISecurityInformation)
    
    class ISecurityInformation2(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{c3ccfdb4-6f88-11d2-a3ce-00c04fb1782a}")
        
        @virtual_table.com_function(PACL)
        def IsDaclCanonical(self, pDacl: IPointer[ACL]) -> int: ...
        
        @virtual_table.com_function(ULONG, PTR(PSID), PTR(LPDATAOBJECT))
        def LookupSids(self, cSids: int, rgpSids: IDoublePtr[SID], ppdo: IDoublePtr[IDataObject]) -> int: ...
        
        virtual_table.build()
    LPSECURITYINFO2 = PTR(ISecurityInformation2)
    
    # HGLOBAL containing SID_INFO_LIST returned by ISecurityInformation2::LookupSids
    CFSTR_ACLUI_SID_INFO_LIST   = TEXT("CFSTR_ACLUI_SID_INFO_LIST")

    # Data structures corresponding to CFSTR_ACLUI_SID_INFO_LIST
    class SID_INFO(CStructure):
        _fields_ = [
            ("pSid", PSID),
            ("pwzCommonName", PWSTR), # Used for selecting icon, e.g. "User" or "Group"
            ("pwzClass", PWSTR),      # Optional, may be NULL
            ("pwzUPN", PWSTR)
        ]
        pSid: IPointer[SID]
        pwzCommonName: PWSTR
        pwzClass: PWSTR
        pwzUPN: PWSTR
    PSID_INFO = PTR(SID_INFO)
    
    class SID_INFO_LIST(CStructure):
        _fields_ = [
            ("cItems", ULONG),
            ("aSidInfo", SID_INFO * 1)
        ]
        cItems: int
        aSidInfo: IPointer[SID_INFO]
    PSID_INFO_LIST = PTR(SID_INFO_LIST)
    
    class IEffectivePermission(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{3853DC76-9F35-407c-88A1-D19344365FBC}")
        
        @virtual_table.com_function(PGUID, PSID, LPCWSTR, PSECURITY_DESCRIPTOR, PTR(POBJECT_TYPE_LIST), PULONG, PTR(PACCESS_MASK), PULONG)
        def GetEffectivePermission(self, pguidObjectType: IPointer[GUID], pUserSid: IPointer[SID], pszServerName: LPCWSTR, pSD: IPointer[SECURITY_DESCRIPTOR], ppObjectTypeList: IDoublePtr[OBJECT_TYPE_LIST], pcObjectTypeListLength: IPointer[ULONG], ppGrantedAccessList: IDoublePtr[ACCESS_MASK], pcGrantedAccessListLength: IPointer[ULONG]) -> int: ...
        
        virtual_table.build()        
    LPEFFECTIVEPERMISSION = PTR(IEffectivePermission)
    
    class ISecurityObjectTypeInfo(IUnknown):
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID("{FC3066EB-79EF-444b-9111-D18A75EBF2FA}")
        
        @virtual_table.com_function(SECURITY_INFORMATION, PACL, PTR(PINHERITED_FROM))
        def GetInheritSource(self, si: int, pACL: IPointer[ACL], ppInheritArray: IDoublePtr[INHERITED_FROMW]) -> int: ...
        
        virtual_table.build()
    LPSecurityObjectTypeInfo = PTR(ISecurityObjectTypeInfo)
    
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        # Support for separation of read-only ACL viewer and elevated ACL editor
        class ISecurityInformation3(IUnknown):
            virtual_table = COMVirtualTable.from_ancestor(IUnknown)
            _iid_ = IID("{E2CDC9CC-31BD-4f8f-8C8B-B641AF516A1A}")
            
            @virtual_table.com_function(PTR(LPWSTR))
            def GetFullResourceName(self, ppszResourceName: IPointer[LPWSTR]) -> int: ...
            
            @virtual_table.com_function(HWND, SI_PAGE_TYPE)
            def OpenElevatedEditor(self, hWnd: int, uPage: int) -> int: ...
            
            virtual_table.build()
        LPSECURITYINFO3 = PTR(ISecurityInformation3)
        
    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        class SECURITY_OBJECT(CStructure):
            _fields_ = [
                ("pwszName", PWSTR),
                ("pData", PVOID),
                ("cbData", DWORD),
                ("pData2", PVOID),
                ("cbData2", DWORD),
                ("Id", DWORD),
                ("fWellKnown", BOOLEAN)
            ]
            pwszName: PWSTR
            pData: int
            cbData: int
            pData2: int
            cbData2: int
            Id: int
            fWellKnown: int
        PSECURITY_OBJECT = PTR(SECURITY_OBJECT)

        SECURITY_OBJECT_ID_OBJECT_SD           = 1
        SECURITY_OBJECT_ID_SHARE               = 2
        SECURITY_OBJECT_ID_CENTRAL_POLICY      = 3
        SECURITY_OBJECT_ID_CENTRAL_ACCESS_RULE = 4
        
        class EFFPERM_RESULT_LIST(CStructure):
            _fields_ = [
                ("fEvaluated", BOOLEAN),
                ("cObjectTypeListLength", ULONG),
                ("pObjectTypeList", POBJECT_TYPE_LIST),
                ("pGrantedAccessList", PACCESS_MASK)
            ]
            fEvaluated: int
            cObjectTypeListLength: int
            pObjectTypeList: IPointer[OBJECT_TYPE_LIST]
            pGrantedAccessList: IPointer[ACCESS_MASK]
        PEFFPERM_RESULT_LIST = PTR(EFFPERM_RESULT_LIST)
        
        class ISecurityInformation4(IUnknown):
            virtual_table = COMVirtualTable.from_ancestor(IUnknown)
            _iid_ = IID("{EA961070-CD14-4621-ACE4-F63C03E583E4}")
            
            @virtual_table.com_function(PTR(PSECURITY_OBJECT), PULONG)
            def GetSecondarySecurity(self, pSecurityObjects: IDoublePtr[SECURITY_OBJECT], pSecurityObjectCount: IPointer[ULONG]) -> int: ...
            
            virtual_table.build()
        LPSECURITYINFO4 = PTR(ISecurityInformation4)
        
        # TODO: unimplemented dependency to authz.py
        # class IEffectivePermission2(IUnknown):
        #     virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        #     _iid_ = IID("{941FABCA-DD47-4FCA-90BB-B0E10255F20D}")
        #     
        #     @virtual_table.com_function(PSID, PSID, PCWSTR, PSECURITY_OBJECT, DWORD, PTOKEN_GROUPS, PAUTHZ_SID_OPERATION, PTOKEN_GROUPS, PAUTHZ_SID_OPERATION, PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION, PAUTHZ_SECURITY_ATTRIBUTE_OPERATION, PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION, PAUTHZ_SECURITY_ATTRIBUTE_OPERATION, PEFFPERM_RESULT_LIST)
        #     def ComputeEffectivePermissionWithSecondarySecurity(self, pSid: IPointer[SID], pDeviceSid: IPointer[SID], pszServerName: PCWSTR, pSecurityObjects: IPointer[SECURITY_OBJECT], dwSecurityObjectCount: int, pUserGroups: IPointer[TOKEN_GROUPS], pAuthzUserGroupsOperations: IPointer[AUTHZ_SID_OPERATION], pDeviceGroups: IPointer[TOKEN_GROUPS], pAuthzDeviceGroupsOperations: IPointer[AUTHZ_SID_OPERATION], pAuthzUserClaims: IPointer[AUTHZ_SECURITY_ATTRIBUTES_INFORMATION], pAuthzUserClaimsOperations: IPointer[AUTHZ_SECURITY_ATTRIBUTE_OPERATION], pAuthzDeviceClaims: IPointer[AUTHZ_SECURITY_ATTRIBUTES_INFORMATION], pAuthzDeviceClaimsOperations: IPointer[AUTHZ_SECURITY_ATTRIBUTE_OPERATION], pEffpermResultLists: IPointer[EFFPERM_RESULT_LIST]) -> int: ...
        #     
        #     virtual_table.build()
        # LPEFFECTIVEPERMISSION2 = PTR(IEffectivePermission2)
        
    @aclui.foreign(HPROPSHEETPAGE, LPSECURITYINFO)
    def CreateSecurityPage(psi: IPointer[ISecurityInformation]) -> int: ...
    
    @aclui.foreign(BOOL, HWND, LPSECURITYINFO)
    def EditSecurity(hwndOwner: int, psi: IPointer[ISecurityInformation]) -> int: ...
    
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        @aclui.foreign(HRESULT, HWND, LPSECURITYINFO, SI_PAGE_TYPE)
        def EditSecurityAdvanced(hwndOwner: int, psi: IPointer[ISecurityInformation], uSIPage: int) -> int: ...
    # REGION ***