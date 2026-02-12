"""
 *************************************************************************\
 *
 * Copyright (c) 1998-2001, Microsoft Corp.  All Rights Reserved.
 *
 * Module Name:
 *
 *   GdiplusMem.h
 *
 * Abstract:
 *
 *
 \*************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

if cpreproc.pragma_once("_GDIPLUSMEM_H"):
    gdiplus = W_WinDLL("gdiplus.dll")

    # REGION *** Desktop Family ***

    #----------------------------------------------------------------------------
    # Memory Allocation APIs
    #----------------------------------------------------------------------------
    
    @gdiplus.foreign(PVOID, SIZE_T)
    def GdipAlloc(size: int) -> PVOID: ...
    
    @gdiplus.foreign(VOID, PVOID)
    def GdipFree(ptr: PVOID): ...

    # REGION ***
# !_GDIPLUSMEM_H
