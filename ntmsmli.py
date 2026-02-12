"""++

  Copyright (c) Microsoft Corporation. All rights reserved.
  Copyright (c) 1996-1999 Highground Systems

  Module Name:

        NtmsMli.h

  Abstract:

        This header contains the definitions of the 
        MediaLabelInfo structure. Media label libraries use
        this structure to pass information to RSM to use to
        identify media. 

        The name of this file reflects it's history.  RSM 
        began its life as NTMS.


--"""

from . import cpreproc

if cpreproc.pragma_once("_INCL_NTMSMLI_H_"):
    from .guiddef import REFGUID
    from .minwindef import *
    
    # REGION *** Desktop Family ***

    NTMSMLI_MAXTYPE     = 64
    NTMSMLI_MAXIDSIZE   = 256
    NTMSMLI_MAXAPPDESCR = 256

    if cpreproc.ifndef("NTMS_NOREDEF"):
        class MediaLabelInfo(CStructure):
            _fields_ = [
                ("LabelType", WCHAR * NTMSMLI_MAXTYPE),
                ("LabelIDSize", DWORD),
                ("LabelID", CHAR * NTMSMLI_MAXIDSIZE),
                ("LabelAppDescr", WCHAR * NTMSMLI_MAXAPPDESCR)
            ]
        pMediaLabelInfo = POINTER(MediaLabelInfo)

    # NTMS_NOREDEF

    MAXMEDIALABEL = WINAPI(DWORD, PDWORD)
    CLAIMMEDIALABEL = WINAPI(DWORD, PBYTE, DWORD, pMediaLabelInfo)
    CLAIMMEDIALABELEX = WINAPI(DWORD, PBYTE, DWORD, pMediaLabelInfo, REFGUID)

    # REGION ***