"""
/**************************************************************************\
*
* Copyright (c) 1998-2001 Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   Gdiplus Pixel Formats
*
* Abstract:
*
*   GDI+ Pixel Formats
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSPIXELFORMATS_H"):
    
    from .winbase import *

    # REGION *** Desktop Family ***

    ARGB = DWORD
    ARGB64 = DWORDLONG

    ALPHA_SHIFT = 24
    RED_SHIFT   = 16
    GREEN_SHIFT = 8
    BLUE_SHIFT  = 0
    ALPHA_MASK  = (ARGB(0xff << ALPHA_SHIFT)).value

    # In-memory pixel data formats:
    # bits 0-7 = format index
    # bits 8-15 = pixel size (in bits)
    # bits 16-23 = flags
    # bits 24-31 = reserved

    PixelFormat = INT

    PixelFormatIndexed     = 0x00010000 # Indexes into a palette
    PixelFormatGDI         = 0x00020000 # Is a GDI-supported format
    PixelFormatAlpha       = 0x00040000 # Has an alpha component
    PixelFormatPAlpha      = 0x00080000 # Pre-multiplied alpha
    PixelFormatExtended    = 0x00100000 # Extended color 16 bits/channel
    PixelFormatCanonical   = 0x00200000 

    PixelFormatUndefined      = 0
    PixelFormatDontCare       = 0

    PixelFormat1bppIndexed    = (1 | ( 1 << 8) | PixelFormatIndexed | PixelFormatGDI)
    PixelFormat4bppIndexed    = (2 | ( 4 << 8) | PixelFormatIndexed | PixelFormatGDI)
    PixelFormat8bppIndexed    = (3 | ( 8 << 8) | PixelFormatIndexed | PixelFormatGDI)
    PixelFormat16bppGrayScale = (4 | (16 << 8) | PixelFormatExtended)
    PixelFormat16bppRGB555    = (5 | (16 << 8) | PixelFormatGDI)
    PixelFormat16bppRGB565    = (6 | (16 << 8) | PixelFormatGDI)
    PixelFormat16bppARGB1555  = (7 | (16 << 8) | PixelFormatAlpha | PixelFormatGDI)
    PixelFormat24bppRGB       = (8 | (24 << 8) | PixelFormatGDI)
    PixelFormat32bppRGB       = (9 | (32 << 8) | PixelFormatGDI)
    PixelFormat32bppARGB      = (10 | (32 << 8) | PixelFormatAlpha | PixelFormatGDI | PixelFormatCanonical)
    PixelFormat32bppPARGB     = (11 | (32 << 8) | PixelFormatAlpha | PixelFormatPAlpha | PixelFormatGDI)
    PixelFormat48bppRGB       = (12 | (48 << 8) | PixelFormatExtended)
    PixelFormat64bppARGB      = (13 | (64 << 8) | PixelFormatAlpha  | PixelFormatCanonical | PixelFormatExtended)
    PixelFormat64bppPARGB     = (14 | (64 << 8) | PixelFormatAlpha  | PixelFormatPAlpha | PixelFormatExtended)
    PixelFormat32bppCMYK      = (15 | (32 << 8))
    PixelFormatMax            = 16

    GetPixelFormatSize = lambda pixfmt: (pixfmt >> 8) & 0xff
    IsIndexedPixelFormat = lambda pixfmt: (pixfmt & PixelFormatIndexed) != 0
    IsAlphaPixelFormat = lambda pixfmt: (pixfmt & PixelFormatAlpha) != 0
    IsExtendedPixelFormat = lambda pixfmt: (pixfmt & PixelFormatExtended) != 0

    #--------------------------------------------------------------------------
    # Determine if the Pixel Format is Canonical format:
    #   PixelFormat32bppARGB
    #   PixelFormat32bppPARGB
    #   PixelFormat64bppARGB
    #   PixelFormat64bppPARGB
    #--------------------------------------------------------------------------

    IsCanonicalPixelFormat = lambda pixfmt: (pixfmt & PixelFormatCanonical) != 0

    if cpreproc.getdef("GDIPVER") >= 0x0110:
        #----------------------------------------------------------------------------
        # Color format conversion parameters
        #----------------------------------------------------------------------------

        PaletteType = INT
        if True:
            # Arbitrary custom palette provided by caller.
            
            PaletteTypeCustom           = 0
            
            # Optimal palette generated using a median-cut algorithm.
            
            PaletteTypeOptimal        = 1
            
            # Black and white palette.
            
            PaletteTypeFixedBW          = 2
            
            # Symmetric halftone palettes.
            # Each of these halftone palettes will be a superset of the system palette.
            # E.g. Halftone8 will have it's 8-color on-off primaries and the 16 system
            # colors added. With duplicates removed, that leaves 16 colors.
            
            PaletteTypeFixedHalftone8   = 3 # 8-color, on-off primaries
            PaletteTypeFixedHalftone27  = 4 # 3 intensity levels of each color
            PaletteTypeFixedHalftone64  = 5 # 4 intensity levels of each color
            PaletteTypeFixedHalftone125 = 6 # 5 intensity levels of each color
            PaletteTypeFixedHalftone216 = 7 # 6 intensity levels of each color

            # Assymetric halftone palettes.
            # These are somewhat less useful than the symmetric ones, but are 
            # included for completeness. These do not include all of the system
            # colors.
            
            PaletteTypeFixedHalftone252 = 8 # 6-red, 7-green, 6-blue intensities
            PaletteTypeFixedHalftone256 = 9 # 8-red, 8-green, 4-blue intensities

        DitherType = INT
        if True:
            DitherTypeNone          = 0
            
            # Solid color - picks the nearest matching color with no attempt to 
            # halftone or dither. May be used on an arbitrary palette.
            
            DitherTypeSolid         = 1
            
            # Ordered dithers and spiral dithers must be used with a fixed palette.
            
            # NOTE: DitherOrdered4x4 is unique in that it may apply to 16bpp 
            # conversions also.
            
            DitherTypeOrdered4x4    = 2
            
            DitherTypeOrdered8x8    = 3
            DitherTypeOrdered16x16  = 4
            DitherTypeSpiral4x4     = 5
            DitherTypeSpiral8x8     = 6
            DitherTypeDualSpiral4x4 = 7
            DitherTypeDualSpiral8x8 = 8
            
            # Error diffusion. May be used with any palette.
            
            DitherTypeErrorDiffusion   = 9

            DitherTypeMax              = 10
    #(GDIPVER >= 0x0110)

    PaletteFlags = INT
    if True:
        PaletteFlagsHasAlpha    = 0x0001
        PaletteFlagsGrayScale   = 0x0002
        PaletteFlagsHalftone    = 0x0004

    class ColorPalette(CStructure):
        _pack_ = 8
        _fields_ = [
            ("Flags", UINT),             # Palette flags
            ("Count", UINT),             # Number of color entries
            ("Entries", POINTER(ARGB))   # Palette color entries
        ]
        
    # REGION ***