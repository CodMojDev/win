"""
/**************************************************************************\
*
* Copyright (c) 2000-2001, Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   GdiplusImageCodec.h
*
* Abstract:
*
*   GDI+ Codec Image APIs
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSIMAGECODEC_H"):
    from .minwindef import *

    # REGION *** Desktop Family ***

    #--------------------------------------------------------------------------
    # Codec Management APIs
    #--------------------------------------------------------------------------

    def GetImageDecodersSize(numDecoders: PUINT, size: PUINT) -> int:
        from .gdiplus import Gdiplus
        return Gdiplus.DllExports.GdipGetImageDecodersSize(numDecoders, size)


    def GetImageDecoders(numDecoders: int, size: int, decoders) -> int:
        from .gdiplus import Gdiplus
        return Gdiplus.DllExports.GdipGetImageDecoders(numDecoders, size, decoders)


    def GetImageEncodersSize(numEncoders: PUINT, size: PUINT) -> int:
        from .gdiplus import Gdiplus
        return Gdiplus.DllExports.GdipGetImageEncodersSize(numEncoders, size)


    def GetImageEncoders(numEncoders: int, size: int, encoders) -> int:
        from .gdiplus import Gdiplus
        return Gdiplus.DllExports.GdipGetImageEncoders(numEncoders, size, encoders)

    # REGION ***

# _GDIPLUSIMAGECODEC_H