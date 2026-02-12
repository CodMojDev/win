"""
/**************************************************************************\
*
* Copyright (c) 1998-2001, Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   GdiplusColorMatrix.h
*
* Abstract:
*
*  GDI+ Color Matrix object, used with Graphics.DrawImage
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSCOLORMATRIX_H"):
    
    from .gdiplustypes import INT, REAL, BYTE, CStructure
    from .gdipluscolor import Color

    # REGION *** Desktop Family ***


    if cpreproc.getdef("GDIPVER") >= 0x0110:
        #----------------------------------------------------------------------------
        # Color channel look up table (LUT)
        #----------------------------------------------------------------------------

        ColorChannelLUT = BYTE * 256

        #----------------------------------------------------------------------------
        # Per-channel Histogram for 8bpp images.
        #----------------------------------------------------------------------------

        HistogramFormat = INT
        if True:
            HistogramFormatARGB = 0
            HistogramFormatPARGB = 1
            HistogramFormatRGB = 2
            HistogramFormatGray = 3
            HistogramFormatB = 4
            HistogramFormatG = 5
            HistogramFormatR = 6
            HistogramFormatA = 7
    #(GDIPVER >= 0x0110)

    #----------------------------------------------------------------------------
    # Color matrix
    #----------------------------------------------------------------------------

    class ColorMatrix(CStructure):
        _fields_ = [
            ("m", REAL * 5 * 5)
        ]

    #----------------------------------------------------------------------------
    # Color Matrix flags
    #----------------------------------------------------------------------------

    ColorMatrixFlags = INT
    if True:
        ColorMatrixFlagsDefault   = 0
        ColorMatrixFlagsSkipGrays = 1
        ColorMatrixFlagsAltGray   = 2

    #----------------------------------------------------------------------------
    # Color Adjust Type
    #----------------------------------------------------------------------------

    ColorAdjustType = INT
    if True:
        ColorAdjustTypeDefault = 0
        ColorAdjustTypeBitmap = 1
        ColorAdjustTypeBrush = 2
        ColorAdjustTypePen = 3
        ColorAdjustTypeText = 4
        ColorAdjustTypeCount = 5
        ColorAdjustTypeAny = 6     # Reserved

    #----------------------------------------------------------------------------
    # Color Map
    #----------------------------------------------------------------------------

    class ColorMap(CStructure):
        _fields_ = [
            ("oldColor", Color),
            ("newColor", Color)
        ]


    # REGION ***