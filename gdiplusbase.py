"""
/**************************************************************************\
*
* Copyright (c) 1998-2001, Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   GdiplusBase.h
*
* Abstract:
*
*   GDI+ base memory allocation class
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSBASE_H"):
    from .gdiplusmem import *

    # REGION *** Desktop Family ***

    class GdiplusBase:
        @staticmethod
        def delete(in_pVoid: PVOID):
            GdipFree(in_pVoid)
        
        @staticmethod
        def new(in_size: int) -> PVOID:
            return GdipAlloc(in_size)

    # REGION ***