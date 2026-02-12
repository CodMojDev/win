#+---------------------------------------------------------------------------
#
#  Microsoft Windows
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
#  File: tpmvscmgr.idl
#
#----------------------------------------------------------------------------

# REGION *** Desktop Family ***

from . import cpreproc

if cpreproc.pragma_once("__tpmvscmgr_h__"):
    from .sdkddkver import *

    from comtypes import IUnknown, COMMETHOD, CoClass
    from .tpmvscattestation import *
    from .guiddef import IID, CLSID
    from .minwindef import *
    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        TPMVSCMGR_STATUS = INT
        if True:
            # [v1_enum]
            TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING = 0 # Initializing the Virtual Smart Card component...
            TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING = 1 # Creating the Virtual Smart Card component...
            TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING = 2 # Destroying the Virtual Smart Card component...

            TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING = 3 # Initializing the Virtual Smart Card Simulator...
            TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING = 4 # Creating the Virtual Smart Card Simulator...
            TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING = 5 # Destroying the Virtual Smart Card Simulator...

            TPMVSCMGR_STATUS_VREADER_INITIALIZING = 6 # Initializing the Virtual Smart Card Reader...
            TPMVSCMGR_STATUS_VREADER_CREATING = 7 # Creating the Virtual Smart Card Reader...
            TPMVSCMGR_STATUS_VREADER_DESTROYING = 8 # Destroying the Virtual Smart Card Reader...

            TPMVSCMGR_STATUS_GENERATE_WAITING = 9 # Waiting for TPM Smart Card Device...
            TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING = 10 # Authenticating to the TPM Smart Card...
            TPMVSCMGR_STATUS_GENERATE_RUNNING = 11 # Generating filesystem on the TPM Smart Card...

            TPMVSCMGR_STATUS_CARD_CREATED = 12 # TPM Smart Card created.
            TPMVSCMGR_STATUS_CARD_DESTROYED = 13 # TPM Smart Card destroyed.
            
        TPMVSCMGR_ERROR = INT
        if True:
            # [v1_enum]
            TPMVSCMGR_ERROR_IMPERSONATION = 0 # Failed to impersonate the caller
            TPMVSCMGR_ERROR_PIN_COMPLEXITY = 1 # Ensure that your PIN/PUK meets the length or complexity requirements of your organization.
            TPMVSCMGR_ERROR_READER_COUNT_LIMIT = 2 # The limit on the number of Smart Card Readers has been reached.
            TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION = 3 # TPM Virtual Smart Card management cannot be used within a Terminal Services session.

            TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE = 4 # Failed to initialize the Virtual Smart Card component.
            TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE = 5 # Failed to create the Virtual Smart Card component.
            TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY = 6 # Failed to destroy the Virtual Smart Card.

            TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE = 7 # Failed to initialize the Virtual Smart Card Simulator.
            TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE = 8 # Failed to create the Virtual Smart Card Simulator.
            TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY = 9 # Failed to destroy the Virtual Smart Card Simulator.
            TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY = 10 # Failed to configure the Virtual Smart Card Simulator.
            TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY = 11 # Failed to find the specified Virtual Smart Card Simulator.

            TPMVSCMGR_ERROR_VREADER_INITIALIZE = 12 # Failed to initialize the Virtual Smart Card Reader.
            TPMVSCMGR_ERROR_VREADER_CREATE = 13 # Failed to create the Virtual Smart Card Reader.
            TPMVSCMGR_ERROR_VREADER_DESTROY = 14 # Failed to destroy the Virtual Smart Card Reader.

            TPMVSCMGR_ERROR_GENERATE_LOCATE_READER = 15 # Failed to connect to the TPM Smart Card.
            TPMVSCMGR_ERROR_GENERATE_FILESYSTEM = 16 # Failed to generate the filesystem on the TPM Smart Card.

            TPMVSCMGR_ERROR_CARD_CREATE = 17 # Unable to create TPM Smart Card.
            TPMVSCMGR_ERROR_CARD_DESTROY = 18 # Unable to destroy TPM Smart Card.

        IID_ITpmVirtualSmartCardManagerStatusCallback = IID("{1A1BB35F-ABB8-451C-A1AE-33D98F1BEF4A}")
        class ITpmVirtualSmartCardManagerStatusCallback(IUnknown):
            _iid_ = IID_ITpmVirtualSmartCardManagerStatusCallback
            _methods_ = IUnknown._methods_ + [
                COMMETHOD(["in", HRESULT, "ReportProgress", ("Status", TPMVSCMGR_STATUS)]),
                COMMETHOD(["in", HRESULT, "ReportError", ("Error", TPMVSCMGR_ERROR)])
            ]

        #
        # TPM Virtual Smart Card Default Admin Key Algorithm ID
        # 0x82 = 0x02 (3-key triple DES) |
        #        0x80 (ISO/IEC 9797 padding method 2) |
        #        0x00 (CBC mode)
        #

        TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID = 0x82

        IID_ITpmVirtualSmartCardManager = IID("{112B1DFF-D9DC-41F7-869F-D67FEE7CB591}")
        class ITpmVirtualSmartCardManager(IUnknown):
            _iid_ = IID_ITpmVirtualSmartCardManager
            _methods_ = IUnknown._methods_ + [
                COMMETHOD(["in", "in", "in", "in", 
                           "in", "in", "in", "in", 
                           "in", "in", "in", "in", 
                           "out", "out"],
                          HRESULT, "CreateVirtualSmartCard", 
                          ("pszFriendlyName", LPCWSTR),
                          ("bAdminAlgId", BYTE),
                          ("pbAdminKey", PBYTE),
                          ("cbAdminKey", DWORD),
                          ("pbAdminKcv", PBYTE),
                          ("cbAdminKcv", DWORD),
                          ("pbPuk", PBYTE),
                          ("cbPuk", DWORD),
                          ("pbPin", PBYTE),
                          ("cbPin", DWORD),
                          ("fGenerate", BOOL),
                          ("pStatusCallback", POINTER(ITpmVirtualSmartCardManagerStatusCallback)),
                          ("ppszInstanceId", POINTER(LPWSTR)),
                          ("pfNeedReboot", PBOOL)),
                COMMETHOD(["in", "in", "out"], HRESULT, "DestroyVirtualSmartCard",
                          ("pszInstanceId", LPCWSTR),
                          ("pStatusCallback", POINTER(ITpmVirtualSmartCardManagerStatusCallback)),
                          ("pfNeedReboot", PBOOL))
            ]

        # (_WINVER >= WIN32_WINNT_WIN8)")

        if cpreproc.get_version() >= WIN32_WINNT_WINBLUE:
            IID_ITpmVirtualSmartCardManager2 = IID("{FDF8A2B9-02DE-47F4-BC26-AA85AB5E5267}")
            class ITpmVirtualSmartCardManager2(ITpmVirtualSmartCardManager):
                _iid_ = IID_ITpmVirtualSmartCardManager2
                _methods_ = ITpmVirtualSmartCardManager._methods_ + [
                    COMMETHOD(["in", "in", "in", "in", 
                               "in", "in", "in", "in", 
                               "in", "in", "in", "in", 
                               "in", "in", "out", "out"], HRESULT, "CreateVirtualSmartCardWithPinPolicy",
                          ("pszFriendlyName", LPCWSTR),
                          ("bAdminAlgId", BYTE),
                          ("pbAdminKey", PBYTE),
                          ("cbAdminKey", DWORD),
                          ("pbAdminKcv", PBYTE),
                          ("cbAdminKcv", DWORD),
                          ("pbPuk", PBYTE),
                          ("cbPuk", DWORD),
                          ("pbPin", PBYTE),
                          ("cbPin", DWORD),
                          ("pbPinPolicy", PBYTE),
                          ("cbPinPolicy", DWORD),
                          ("fGenerate", BOOL),
                          ("pStatusCallback", POINTER(ITpmVirtualSmartCardManagerStatusCallback)),
                          ("ppszInstanceId", POINTER(LPWSTR)),
                          ("pfNeedReboot", PBOOL))
                ]

        # (_WINVER >= WIN32_WINNT_WINBLUE)")

        if cpreproc.get_version() >= WIN32_WINNT_WINTHRESHOLD:
            IID_ITpmVirtualSmartCardManager3 = IID("{3C745A97-F375-4150-BE17-5950F694C699}")
            class ITpmVirtualSmartCardManager3(ITpmVirtualSmartCardManager2):
                _iid_ = IID_ITpmVirtualSmartCardManager3
                _methods_ = ITpmVirtualSmartCardManager2._methods_ + [
                    COMMETHOD(["in", "in", "in", "in", 
                               "in", "in", "in", "in", 
                               "in", "in", "in", "in", 
                               "in", "in", "in", "out", 
                               "out"], HRESULT, "CreateVirtualSmartCardWithAttestation",
                          ("pszFriendlyName", LPCWSTR),
                          ("bAdminAlgId", BYTE),
                          ("pbAdminKey", PBYTE),
                          ("cbAdminKey", DWORD),
                          ("pbAdminKcv", PBYTE),
                          ("cbAdminKcv", DWORD),
                          ("pbPuk", PBYTE),
                          ("cbPuk", DWORD),
                          ("pbPin", PBYTE),
                          ("cbPin", DWORD),
                          ("pbPinPolicy", PBYTE),
                          ("cbPinPolicy", DWORD),
                          ("attestationType", TPMVSC_ATTESTATION_TYPE),
                          ("fGenerate", BOOL),
                          ("pStatusCallback", POINTER(ITpmVirtualSmartCardManagerStatusCallback)),
                          ("ppszInstanceId", POINTER(LPWSTR)),
                          ("pfNeedReboot", PBOOL))
                ]

        # (_WINVER >= WIN32_WINNT_WINTHRESHOLD)")

        
        if cpreproc.get_version() >= WIN32_WINNT_WIN8:
            CLSID_TpmVirtualSmartCardManagers = CLSID("{1C60A923-2D86-46AA-928A-E7F3E37577AF}")
            CLSID_TpmVirtualSmartCardManager = CLSID("{16A18E86-7F6E-4C20-AD89-4FFC0DB7A96A}")
            CLSID_RemoteTpmVirtualSmartCardManager = CLSID("{152EA2A8-70DC-4C59-8B2A-32AA3CA0DCAC}")
            class TpmVirtualSmartCardManagers(CoClass):
                _reg_clsid_ = CLSID_TpmVirtualSmartCardManagers
                class TpmVirtualSmartCardManager(CoClass):
                    _reg_clsid_ = CLSID_TpmVirtualSmartCardManager
                    _com_interfaces_ = [ITpmVirtualSmartCardManager, ITpmVirtualSmartCardManager2, ITpmVirtualSmartCardManager3]
                
                class RemoteTpmVirtualSmartCardManager(CoClass):
                    _reg_clsid_ = CLSID_RemoteTpmVirtualSmartCardManager
                    _com_interfaces_ = [ITpmVirtualSmartCardManager, ITpmVirtualSmartCardManager2, ITpmVirtualSmartCardManager3]

    # (_WINVER >= WIN32_WINNT_WIN8)")

# REGION ***