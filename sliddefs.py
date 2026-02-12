"""++

Copyright (C) Microsoft Corporation, 2006

Module Name:

    sliddefs.h

Abstract:

    Software Licensing GUID definitions
   
--"""

from . import cpreproc
if cpreproc.pragma_once("_SLIDDEFS_H_"):
    if cpreproc.pragma_once("_WINDOWS_SLID_"):
        from .guiddef import GUID

        WINDOWS_SLID = GUID("{55c92734-d682-4d71-983e-d6ec3f16059f}")
