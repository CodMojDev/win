"""++

Copyright (C) Microsoft Corporation, 1999

Module Name:

    mschapp - MS-CHAP Password Change API

Abstract:

    These APIs correspond to the MS-CHAP RFC -2433 sections 9 and 10. In order
    to develop an MS-CHAP RAS server that works with an NT domain, these APIs
    are required.

    Only wide (Unicode) versions of these apis will be available. These are the
    2 callable APIs:

    *   MSChapSrvChangePassword
    *   MsChapSrvChangePassword2

--"""

from . import cpreproc

if cpreproc.pragma_once("_MSCHAPP_H_"):
    from .defbase import *
    from .minwindef import *
    
    advapi32 = WinDLL('advapi32.dll')
    
    # REGION *** Desktop Family ***

    if cpreproc.ifndef("_NTCRYPT_"):
        CYPHER_BLOCK_LENGTH        = 8

        class CYPHER_BLOCK(CStructure):
            _fields_ = [
                ("data", CHAR * CYPHER_BLOCK_LENGTH)
            ]
            
        class LM_OWF_PASSWORD(CStructure):
            _fields_ = [
                ("data", CYPHER_BLOCK * 2)
            ]
        PLM_OWF_PASSWORD = POINTER(LM_OWF_PASSWORD)
        NT_OWF_PASSWORD = LM_OWF_PASSWORD
        PNT_OWF_PASSWORD = PLM_OWF_PASSWORD

        class SAMPR_ENCRYPTED_USER_PASSWORD(CStructure):
            _fields_ = [
                ("Buffer", CHAR * (512 + 4))
            ]
        PSAMPR_ENCRYPTED_USER_PASSWORD = POINTER(SAMPR_ENCRYPTED_USER_PASSWORD)

        class ENCRYPTED_LM_OWF_PASSWORD(CStructure):
            _fields_ = [
                ("data", CYPHER_BLOCK * 2)
            ]
        PENCRYPTED_LM_OWF_PASSWORD = POINTER(ENCRYPTED_LM_OWF_PASSWORD)
        ENCRYPTED_NT_OWF_PASSWORD = ENCRYPTED_LM_OWF_PASSWORD
        PENCRYPTED_NT_OWF_PASSWORD = PENCRYPTED_LM_OWF_PASSWORD
    # _NTCRYPT

    #
    # Change a password.
    #
        
    MSChapSrvChangePassword = declare(advapi32.MSChapSrvChangePassword, DWORD, LPWSTR, LPWSTR, BOOLEAN, 
                                      PLM_OWF_PASSWORD, PLM_OWF_PASSWORD, PNT_OWF_PASSWORD, PNT_OWF_PASSWORD)

    #
    # Change a password using mutual encryption.
    #

    MSChapSrvChangePassword2 = declare(advapi32.MSChapSrvChangePassword2, DWORD, LPWSTR, LPWSTR, 
                                       PSAMPR_ENCRYPTED_USER_PASSWORD, PENCRYPTED_NT_OWF_PASSWORD,
                                       BOOLEAN, PSAMPR_ENCRYPTED_USER_PASSWORD, PENCRYPTED_LM_OWF_PASSWORD)

    # REGION ***
    
# _MSCHAPP_H_
