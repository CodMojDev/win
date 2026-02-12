"""
------------------------------------------------------------------------------
 File: COMLite.h

 Desc: This header file is to provide a migration path for users of
       ActiveMovie betas 1 and 2.

 Copyright(c) 1992 - 2001, Microsoft Corporation.  All rights reserved.
------------------------------------------------------------------------------
"""

from . import cpreproc

if cpreproc.pragma_once("_INC_COMLITE_"):
    # REGION *** Desktop Family ***

    QzInitializeEx = lambda *args, **kwargs: CoInitializeEx(*args, **kwargs) # type: ignore
    QzUninitialize = lambda *args, **kwargs: CoUninitialize(*args, **kwargs) # type: ignore
    QzFreeUnusedLibraries = lambda *args, **kwargs: CoFreeUnusedLibraries(*args, **kwargs) # type: ignore
    QzGetMalloc = lambda *args, **kwargs: CoGetMalloc(*args, **kwargs) # type: ignore
    QzTaskMemAlloc = lambda *args, **kwargs: CoTaskMemAlloc(*args, **kwargs) # type: ignore
    QzTaskMemRealloc = lambda *args, **kwargs: CoTaskMemRealloc(*args, **kwargs) # type: ignore
    QzTaskMemFree = lambda *args, **kwargs: CoTaskMemFree(*args, **kwargs) # type: ignore
    QzCreateFilterObject = lambda *args, **kwargs: CoCreateInstance(*args, **kwargs) # type: ignore
    QzCLSIDFromString = lambda *args, **kwargs: CLSIDFromString(*args, **kwargs) # type: ignore
    QzStringFromGUID2 = lambda *args, **kwargs: StringFromGUID2(*args, **kwargs) # type: ignore

    # REGION ***
# _INC_COMLITE_