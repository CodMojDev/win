#
#       Copyright (C) Microsoft.   All rights reserved
#

from . import cpreproc

from .minwindef import Structure, DWORD, BOOL, BYTE

if cpreproc.pragma_once("__SAC_H__"):
    
    HMAC = DWORD

    RSA_KEY_LEN = 64
    SAC_SESSION_KEYLEN = 8

    SAC_PROTOCOL_WMDM = 1
    SAC_PROTOCOL_V1 = 2

    SAC_CERT_X509 = 1
    SAC_CERT_V1 = 2

    class __MACINFO(CStructure):
        _fields_ = [
            ("fUsed", BOOL),
            ("abMacState", BYTE * 36)
        ]
    MACINFO = __MACINFO