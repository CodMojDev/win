"""
/**************************************************************************\
*
* Copyright (c) 1998-2001 Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   GdiplusEnums.h
*
* Abstract:
*
*   GDI+ Enumeration Types
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSENUMS_H"):
    
    from .wingdi import *

    # REGION *** Desktop Family ***

    #--------------------------------------------------------------------------
    # Default bezier flattening tolerance in device pixels.
    #--------------------------------------------------------------------------

    FlatnessDefault: float = 1.0/4.0

    #--------------------------------------------------------------------------
    # Graphics and Container State cookies
    #--------------------------------------------------------------------------

    GraphicsState = UINT
    GraphicsContainer = UINT

    #--------------------------------------------------------------------------
    # Fill mode constants
    #--------------------------------------------------------------------------

    FillMode = INT
    if True:
        FillModeAlternate = 0        # 0
        FillModeWinding = 1          # 1

    #--------------------------------------------------------------------------
    # Quality mode constants
    #--------------------------------------------------------------------------

    QualityMode = INT
    if True:
        QualityModeInvalid   = -1
        QualityModeDefault   = 0
        QualityModeLow       = 1 # Best performance
        QualityModeHigh      = 2 # Best rendering quality

    #--------------------------------------------------------------------------
    # Alpha Compositing mode constants
    #--------------------------------------------------------------------------

    CompositingMode = INT
    if True:
        CompositingModeSourceOver = 0    # 0
        CompositingModeSourceCopy = 1     # 1

    #--------------------------------------------------------------------------
    # Alpha Compositing quality constants
    #--------------------------------------------------------------------------

    CompositingQuality = INT
    if True:
        CompositingQualityInvalid          = QualityModeInvalid
        CompositingQualityDefault          = QualityModeDefault
        CompositingQualityHighSpeed        = QualityModeLow
        CompositingQualityHighQuality      = QualityModeHigh
        CompositingQualityGammaCorrected   = QualityModeHigh + 1
        CompositingQualityAssumeLinear     = QualityModeHigh + 2

    #--------------------------------------------------------------------------
    # Unit constants
    #--------------------------------------------------------------------------

    Unit = INT
    if True:
        UnitWorld = 0      # 0 -- World coordinate (non-physical unit)
        UnitDisplay = 1    # 1 -- Variable -- for PageTransform only
        UnitPixel = 2      # 2 -- Each unit is one device pixel.
        UnitPoint = 3      # 3 -- Each unit is a printer's point or 1/72 inch.
        UnitInch = 4       # 4 -- Each unit is 1 inch.
        UnitDocument = 5   # 5 -- Each unit is 1/300 inch.
        UnitMillimeter = 6 # 6 -- Each unit is 1 millimeter.

    #--------------------------------------------------------------------------
    # MetafileFrameUnit
    #
    # The frameRect for creating a metafile can be specified in any of these
    # units.  There is an extra frame unit value (MetafileFrameUnitGdi) so
    # that units can be supplied in the same units that GDI expects for
    # frame rects -- these units are in .01 (1/100ths) millimeter units
    # as defined by GDI.
    #--------------------------------------------------------------------------

    MetafileFrameUnit = INT
    if True:
        MetafileFrameUnitPixel      = UnitPixel
        MetafileFrameUnitPoint      = UnitPoint
        MetafileFrameUnitInch       = UnitInch
        MetafileFrameUnitDocument   = UnitDocument
        MetafileFrameUnitMillimeter = UnitMillimeter
        MetafileFrameUnitGdi        = UnitMillimeter + 1    # GDI compatible .01 MM units

    #--------------------------------------------------------------------------
    # Coordinate space identifiers
    #--------------------------------------------------------------------------

    CoordinateSpace = INT
    if True:
        CoordinateSpaceWorld = 0    # 0
        CoordinateSpacePage = 1     # 1
        CoordinateSpaceDevice = 2   # 2

    #--------------------------------------------------------------------------
    # Various wrap modes for brushes
    #--------------------------------------------------------------------------

    WrapMode = INT
    if True:
        WrapModeTile = 0       # 0
        WrapModeTileFlipX = 1  # 1
        WrapModeTileFlipY = 2  # 2
        WrapModeTileFlipXY = 3 # 3
        WrapModeClamp = 4      # 4

    #--------------------------------------------------------------------------
    # Various hatch styles
    #--------------------------------------------------------------------------

    HatchStyle = INT
    if True:
        HatchStyleHorizontal = 0                   # 0
        HatchStyleVertical = 1                     # 1
        HatchStyleForwardDiagonal = 2              # 2
        HatchStyleBackwardDiagonal = 3             # 3
        HatchStyleCross = 4                        # 4
        HatchStyleDiagonalCross = 5                # 5
        HatchStyle05Percent = 6                    # 6
        HatchStyle10Percent = 7                    # 7
        HatchStyle20Percent = 8                    # 8
        HatchStyle25Percent = 9                    # 9
        HatchStyle30Percent = 10                   # 10
        HatchStyle40Percent = 11                   # 11
        HatchStyle50Percent = 12                   # 12
        HatchStyle60Percent = 13                   # 13
        HatchStyle70Percent = 14                   # 14
        HatchStyle75Percent = 15                   # 15
        HatchStyle80Percent = 16                   # 16
        HatchStyle90Percent = 17                   # 17
        HatchStyleLightDownwardDiagonal = 18       # 18
        HatchStyleLightUpwardDiagonal = 19         # 19
        HatchStyleDarkDownwardDiagonal = 20        # 20
        HatchStyleDarkUpwardDiagonal = 21          # 21
        HatchStyleWideDownwardDiagonal = 22        # 22
        HatchStyleWideUpwardDiagonal = 23          # 23
        HatchStyleLightVertical = 24               # 24
        HatchStyleLightHorizontal = 25             # 25
        HatchStyleNarrowVertical = 26              # 26
        HatchStyleNarrowHorizontal = 27            # 27
        HatchStyleDarkVertical = 28                # 28
        HatchStyleDarkHorizontal = 29              # 29
        HatchStyleDashedDownwardDiagonal = 30      # 30
        HatchStyleDashedUpwardDiagonal = 31        # 31
        HatchStyleDashedHorizontal = 32            # 32
        HatchStyleDashedVertical = 33              # 33
        HatchStyleSmallConfetti = 34               # 34
        HatchStyleLargeConfetti = 35               # 35
        HatchStyleZigZag = 36                      # 36
        HatchStyleWave = 37                        # 37
        HatchStyleDiagonalBrick = 38               # 38
        HatchStyleHorizontalBrick = 39             # 39
        HatchStyleWeave = 40                       # 40
        HatchStylePlaid = 41                       # 41
        HatchStyleDivot = 42                       # 42
        HatchStyleDottedGrid = 43                  # 43
        HatchStyleDottedDiamond = 44               # 44
        HatchStyleShingle = 45                     # 45
        HatchStyleTrellis = 46                     # 46
        HatchStyleSphere = 47                      # 47
        HatchStyleSmallGrid = 48                   # 48
        HatchStyleSmallCheckerBoard = 49           # 49
        HatchStyleLargeCheckerBoard = 50           # 50
        HatchStyleOutlinedDiamond = 51             # 51
        HatchStyleSolidDiamond = 52                # 52

        HatchStyleTotal = 53  
        HatchStyleLargeGrid = HatchStyleCross  # 4

        HatchStyleMin       = HatchStyleHorizontal
        HatchStyleMax       = HatchStyleTotal - 1

    #--------------------------------------------------------------------------
    # Dash style constants
    #--------------------------------------------------------------------------

    DashStyle = INT
    if True:
        DashStyleSolid = 0         # 0
        DashStyleDash = 1          # 1
        DashStyleDot = 2           # 2
        DashStyleDashDot = 3       # 3
        DashStyleDashDotDot = 4    # 4
        DashStyleCustom = 5         # 5

    #--------------------------------------------------------------------------
    # Dash cap constants
    #--------------------------------------------------------------------------

    DashCap = INT
    if True:
        DashCapFlat             = 0
        DashCapRound            = 2
        DashCapTriangle         = 3

    #--------------------------------------------------------------------------
    # Line cap constants (only the lowest 8 bits are used).
    #--------------------------------------------------------------------------

    LineCap = INT
    if True:
        LineCapFlat             = 0
        LineCapSquare           = 1
        LineCapRound            = 2
        LineCapTriangle         = 3

        LineCapNoAnchor         = 0x10 # corresponds to flat cap
        LineCapSquareAnchor     = 0x11 # corresponds to square cap
        LineCapRoundAnchor      = 0x12 # corresponds to round cap
        LineCapDiamondAnchor    = 0x13 # corresponds to triangle cap
        LineCapArrowAnchor      = 0x14 # no correspondence

        LineCapCustom           = 0xff # custom cap

        LineCapAnchorMask       = 0xf0  # mask to check for anchor or not.

    #--------------------------------------------------------------------------
    # Custom Line cap type constants
    #--------------------------------------------------------------------------

    CustomLineCapType = INT
    if True:
        CustomLineCapTypeDefault         = 0
        CustomLineCapTypeAdjustableArrow = 1

    #--------------------------------------------------------------------------
    # Line join constants
    #--------------------------------------------------------------------------

    LineJoin = INT
    if True:
        LineJoinMiter        = 0
        LineJoinBevel        = 1
        LineJoinRound        = 2
        LineJoinMiterClipped = 3

    #--------------------------------------------------------------------------
    # Path point types (only the lowest 8 bits are used.)
    #  The lowest 3 bits are interpreted as point type
    #  The higher 5 bits are reserved for flags.
    #--------------------------------------------------------------------------

    PathPointType = INT
    if True:
        PathPointTypeStart           = 0    # move
        PathPointTypeLine            = 1    # line
        PathPointTypeBezier          = 3    # default Bezier (= cubic Bezier)
        PathPointTypePathTypeMask    = 0x07 # type mask (lowest 3 bits).
        PathPointTypeDashMode        = 0x10 # currently in dash mode.
        PathPointTypePathMarker      = 0x20 # a marker for the path.
        PathPointTypeCloseSubpath    = 0x80 # closed flag

        # Path types used for advanced path.

        PathPointTypeBezier3    = 3         # cubic Bezier


    #--------------------------------------------------------------------------
    # WarpMode constants
    #--------------------------------------------------------------------------

    WarpMode = INT
    if True:
        WarpModePerspective = 0   # 0
        WarpModeBilinear = 1      # 1

    #--------------------------------------------------------------------------
    # LineGradient Mode
    #--------------------------------------------------------------------------

    LinearGradientMode = INT
    if True:
        LinearGradientModeHorizontal = 0        # 0
        LinearGradientModeVertical = 1          # 1
        LinearGradientModeForwardDiagonal = 2   # 2
        LinearGradientModeBackwardDiagonal = 3  # 3

    #--------------------------------------------------------------------------
    # Region Comine Modes
    #--------------------------------------------------------------------------

    CombineMode = INT
    if True:
        CombineModeReplace = 0    # 0
        CombineModeIntersect = 1  # 1
        CombineModeUnion = 2      # 2
        CombineModeXor = 3        # 3
        CombineModeExclude = 4    # 4
        CombineModeComplement = 5 # 5 (Exclude From)

    #--------------------------------------------------------------------------
    # Image types
    #--------------------------------------------------------------------------

    ImageType = INT
    if True:
        ImageTypeUnknown = 0  # 0
        ImageTypeBitmap = 1   # 1
        ImageTypeMetafile = 2 # 2

    #--------------------------------------------------------------------------
    # Interpolation modes
    #--------------------------------------------------------------------------

    InterpolationMode = INT
    if True:
        InterpolationModeInvalid          = QualityModeInvalid
        InterpolationModeDefault          = QualityModeDefault
        InterpolationModeLowQuality       = QualityModeLow
        InterpolationModeHighQuality      = QualityModeHigh
        InterpolationModeBilinear         = QualityModeHigh + 1
        InterpolationModeBicubic          = QualityModeHigh + 2
        InterpolationModeNearestNeighbor  = QualityModeHigh + 3
        InterpolationModeHighQualityBilinear = QualityModeHigh + 4
        InterpolationModeHighQualityBicubic  = QualityModeHigh + 5

    #--------------------------------------------------------------------------
    # Pen types
    #--------------------------------------------------------------------------

    PenAlignment = INT
    if True:
        PenAlignmentCenter       = 0
        PenAlignmentInset        = 1

    #--------------------------------------------------------------------------
    # Brush types
    #--------------------------------------------------------------------------

    BrushType = INT
    if True:
        BrushTypeSolidColor       = 0
        BrushTypeHatchFill        = 1
        BrushTypeTextureFill      = 2
        BrushTypePathGradient     = 3
        BrushTypeLinearGradient   = 4

    #--------------------------------------------------------------------------
    # Pen's Fill types
    #--------------------------------------------------------------------------

    PenType = INT
    if True:
        PenTypeSolidColor       = BrushTypeSolidColor
        PenTypeHatchFill        = BrushTypeHatchFill
        PenTypeTextureFill      = BrushTypeTextureFill
        PenTypePathGradient     = BrushTypePathGradient
        PenTypeLinearGradient   = BrushTypeLinearGradient
        PenTypeUnknown          = -1

    #--------------------------------------------------------------------------
    # Matrix Order
    #--------------------------------------------------------------------------

    MatrixOrder = INT
    if True:
        MatrixOrderPrepend    = 0
        MatrixOrderAppend     = 1

    #--------------------------------------------------------------------------
    # Generic font families
    #--------------------------------------------------------------------------

    GenericFontFamily = INT
    if True:
        GenericFontFamilySerif = 0
        GenericFontFamilySansSerif = 1
        GenericFontFamilyMonospace = 2


    #--------------------------------------------------------------------------
    # FontStyle: face types and common styles
    #--------------------------------------------------------------------------

    FontStyle = INT
    if True:
        FontStyleRegular    = 0
        FontStyleBold       = 1
        FontStyleItalic     = 2
        FontStyleBoldItalic = 3
        FontStyleUnderline  = 4
        FontStyleStrikeout  = 8

    #---------------------------------------------------------------------------
    # Smoothing Mode
    #---------------------------------------------------------------------------

    SmoothingMode = INT
    if True:
        SmoothingModeInvalid     = QualityModeInvalid
        SmoothingModeDefault     = QualityModeDefault
        SmoothingModeHighSpeed   = QualityModeLow
        SmoothingModeHighQuality = QualityModeHigh
        SmoothingModeNone        = QualityModeHigh + 1
        SmoothingModeAntiAlias   = QualityModeHigh + 2
        SmoothingModeAntiAlias8x4 = SmoothingModeAntiAlias
        SmoothingModeAntiAlias8x8 = SmoothingModeAntiAlias + 1

    #---------------------------------------------------------------------------
    # Pixel Format Mode
    #---------------------------------------------------------------------------

    PixelOffsetMode = INT
    if True:
        PixelOffsetModeInvalid     = QualityModeInvalid
        PixelOffsetModeDefault     = QualityModeDefault
        PixelOffsetModeHighSpeed   = QualityModeLow
        PixelOffsetModeHighQuality = QualityModeHigh
        PixelOffsetModeNone = QualityModeHigh + 1   # No pixel offset
        PixelOffsetModeHalf = QualityModeHigh + 2   # Offset by -0.5 -0.5 for fast anti-alias perf

    #---------------------------------------------------------------------------
    # Text Rendering Hint
    #---------------------------------------------------------------------------

    TextRenderingHint = INT
    if True:
        TextRenderingHintSystemDefault = 0               # Glyph with system default rendering hint
        TextRenderingHintSingleBitPerPixelGridFit = 1    # Glyph bitmap with hinting
        TextRenderingHintSingleBitPerPixel = 2           # Glyph bitmap without hinting
        TextRenderingHintAntiAliasGridFit = 3            # Glyph anti-alias bitmap with hinting
        TextRenderingHintAntiAlias = 4                   # Glyph anti-alias bitmap without hinting
        TextRenderingHintClearTypeGridFit = 5            # Glyph CT bitmap with hinting

    #---------------------------------------------------------------------------
    # Metafile Types
    #---------------------------------------------------------------------------

    MetafileType = INT
    if True:
        MetafileTypeInvalid = 0           # Invalid metafile
        MetafileTypeWmf = 1               # Standard WMF
        MetafileTypeWmfPlaceable = 2      # Placeable WMF
        MetafileTypeEmf = 3               # EMF (not EMF+)
        MetafileTypeEmfPlusOnly = 4       # EMF+ without dual down-level records
        MetafileTypeEmfPlusDual = 5       # EMF+ with dual down-level records

    #---------------------------------------------------------------------------
    # Specifies the type of EMF to record
    #---------------------------------------------------------------------------

    EmfType = INT
    if True:
        EmfTypeEmfOnly     = MetafileTypeEmf          # no EMF+ only EMF
        EmfTypeEmfPlusOnly = MetafileTypeEmfPlusOnly  # no EMF only EMF+
        EmfTypeEmfPlusDual = MetafileTypeEmfPlusDual   # both EMF+ and EMF

    #---------------------------------------------------------------------------
    # EMF+ Persistent object types
    #---------------------------------------------------------------------------

    ObjectType = INT
    if True:
        ObjectTypeInvalid = 0
        ObjectTypeBrush = 1
        ObjectTypePen = 2
        ObjectTypePath = 3
        ObjectTypeRegion = 4
        ObjectTypeImage = 5
        ObjectTypeFont = 6
        ObjectTypeStringFormat = 7
        ObjectTypeImageAttributes = 8
        ObjectTypeCustomLineCap = 9
        if cpreproc.getdef("GDIPVER") >= 0x0110:
            ObjectTypeGraphics = 10

            ObjectTypeMax = ObjectTypeGraphics
        else:
            ObjectTypeMax = ObjectTypeCustomLineCap
        #(GDIPVER >= 0x0110)
            ObjectTypeMin = ObjectTypeBrush

    def ObjectTypeIsValid(type: int) -> bool:
        return (type >= ObjectTypeMin) and (type <= ObjectTypeMax)

    #---------------------------------------------------------------------------
    # EMF+ Records
    #---------------------------------------------------------------------------

    # We have to change the WMF record numbers so that they don't conflict with
    # the EMF and EMF+ record numbers.

    GDIP_EMFPLUS_RECORD_BASE       = 0x00004000
    GDIP_WMF_RECORD_BASE           = 0x00010000
    
    def GDIP_WMF_RECORD_TO_EMFPLUS(n: int) -> int:
        return ((n) | GDIP_WMF_RECORD_BASE)
    
    def GDIP_EMFPLUS_RECORD_TO_WMF(n: int) -> int:
        return ((n) & (~GDIP_WMF_RECORD_BASE))
    
    def GDIP_IS_WMF_RECORDTYPE(n: int) -> bool:
        return (((n) & GDIP_WMF_RECORD_BASE) != 0)

    EmfPlusRecordType = INT
    if True:
    # Since we have to enumerate GDI records right along with GDI+ records
    # We list all the GDI records here so that they can be part of the
    # same enumeration type which is used in the enumeration callback.

        WmfRecordTypeSetBkColor              = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETBKCOLOR)
        WmfRecordTypeSetBkMode               = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETBKMODE)
        WmfRecordTypeSetMapMode              = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETMAPMODE)
        WmfRecordTypeSetROP2                 = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETROP2)
        WmfRecordTypeSetRelAbs               = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETRELABS)
        WmfRecordTypeSetPolyFillMode         = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETPOLYFILLMODE)
        WmfRecordTypeSetStretchBltMode       = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETSTRETCHBLTMODE)
        WmfRecordTypeSetTextCharExtra        = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETTEXTCHAREXTRA)
        WmfRecordTypeSetTextColor            = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETTEXTCOLOR)
        WmfRecordTypeSetTextJustification    = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETTEXTJUSTIFICATION)
        WmfRecordTypeSetWindowOrg            = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETWINDOWORG)
        WmfRecordTypeSetWindowExt            = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETWINDOWEXT)
        WmfRecordTypeSetViewportOrg          = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETVIEWPORTORG)
        WmfRecordTypeSetViewportExt          = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETVIEWPORTEXT)
        WmfRecordTypeOffsetWindowOrg         = GDIP_WMF_RECORD_TO_EMFPLUS(META_OFFSETWINDOWORG)
        WmfRecordTypeScaleWindowExt          = GDIP_WMF_RECORD_TO_EMFPLUS(META_SCALEWINDOWEXT)
        WmfRecordTypeOffsetViewportOrg       = GDIP_WMF_RECORD_TO_EMFPLUS(META_OFFSETVIEWPORTORG)
        WmfRecordTypeScaleViewportExt        = GDIP_WMF_RECORD_TO_EMFPLUS(META_SCALEVIEWPORTEXT)
        WmfRecordTypeLineTo                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_LINETO)
        WmfRecordTypeMoveTo                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_MOVETO)
        WmfRecordTypeExcludeClipRect         = GDIP_WMF_RECORD_TO_EMFPLUS(META_EXCLUDECLIPRECT)
        WmfRecordTypeIntersectClipRect       = GDIP_WMF_RECORD_TO_EMFPLUS(META_INTERSECTCLIPRECT)
        WmfRecordTypeArc                     = GDIP_WMF_RECORD_TO_EMFPLUS(META_ARC)
        WmfRecordTypeEllipse                 = GDIP_WMF_RECORD_TO_EMFPLUS(META_ELLIPSE)
        WmfRecordTypeFloodFill               = GDIP_WMF_RECORD_TO_EMFPLUS(META_FLOODFILL)
        WmfRecordTypePie                     = GDIP_WMF_RECORD_TO_EMFPLUS(META_PIE)
        WmfRecordTypeRectangle               = GDIP_WMF_RECORD_TO_EMFPLUS(META_RECTANGLE)
        WmfRecordTypeRoundRect               = GDIP_WMF_RECORD_TO_EMFPLUS(META_ROUNDRECT)
        WmfRecordTypePatBlt                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_PATBLT)
        WmfRecordTypeSaveDC                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_SAVEDC)
        WmfRecordTypeSetPixel                = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETPIXEL)
        WmfRecordTypeOffsetClipRgn           = GDIP_WMF_RECORD_TO_EMFPLUS(META_OFFSETCLIPRGN)
        WmfRecordTypeTextOut                 = GDIP_WMF_RECORD_TO_EMFPLUS(META_TEXTOUT)
        WmfRecordTypeBitBlt                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_BITBLT)
        WmfRecordTypeStretchBlt              = GDIP_WMF_RECORD_TO_EMFPLUS(META_STRETCHBLT)
        WmfRecordTypePolygon                 = GDIP_WMF_RECORD_TO_EMFPLUS(META_POLYGON)
        WmfRecordTypePolyline                = GDIP_WMF_RECORD_TO_EMFPLUS(META_POLYLINE)
        WmfRecordTypeEscape                  = GDIP_WMF_RECORD_TO_EMFPLUS(META_ESCAPE)
        WmfRecordTypeRestoreDC               = GDIP_WMF_RECORD_TO_EMFPLUS(META_RESTOREDC)
        WmfRecordTypeFillRegion              = GDIP_WMF_RECORD_TO_EMFPLUS(META_FILLREGION)
        WmfRecordTypeFrameRegion             = GDIP_WMF_RECORD_TO_EMFPLUS(META_FRAMEREGION)
        WmfRecordTypeInvertRegion            = GDIP_WMF_RECORD_TO_EMFPLUS(META_INVERTREGION)
        WmfRecordTypePaintRegion             = GDIP_WMF_RECORD_TO_EMFPLUS(META_PAINTREGION)
        WmfRecordTypeSelectClipRegion        = GDIP_WMF_RECORD_TO_EMFPLUS(META_SELECTCLIPREGION)
        WmfRecordTypeSelectObject            = GDIP_WMF_RECORD_TO_EMFPLUS(META_SELECTOBJECT)
        WmfRecordTypeSetTextAlign            = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETTEXTALIGN)
        WmfRecordTypeDrawText                = GDIP_WMF_RECORD_TO_EMFPLUS(0x062F)  # META_DRAWTEXT
        WmfRecordTypeChord                   = GDIP_WMF_RECORD_TO_EMFPLUS(META_CHORD)
        WmfRecordTypeSetMapperFlags          = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETMAPPERFLAGS)
        WmfRecordTypeExtTextOut              = GDIP_WMF_RECORD_TO_EMFPLUS(META_EXTTEXTOUT)
        WmfRecordTypeSetDIBToDev             = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETDIBTODEV)
        WmfRecordTypeSelectPalette           = GDIP_WMF_RECORD_TO_EMFPLUS(META_SELECTPALETTE)
        WmfRecordTypeRealizePalette          = GDIP_WMF_RECORD_TO_EMFPLUS(META_REALIZEPALETTE)
        WmfRecordTypeAnimatePalette          = GDIP_WMF_RECORD_TO_EMFPLUS(META_ANIMATEPALETTE)
        WmfRecordTypeSetPalEntries           = GDIP_WMF_RECORD_TO_EMFPLUS(META_SETPALENTRIES)
        WmfRecordTypePolyPolygon             = GDIP_WMF_RECORD_TO_EMFPLUS(META_POLYPOLYGON)
        WmfRecordTypeResizePalette           = GDIP_WMF_RECORD_TO_EMFPLUS(META_RESIZEPALETTE)
        WmfRecordTypeDIBBitBlt               = GDIP_WMF_RECORD_TO_EMFPLUS(META_DIBBITBLT)
        WmfRecordTypeDIBStretchBlt           = GDIP_WMF_RECORD_TO_EMFPLUS(META_DIBSTRETCHBLT)
        WmfRecordTypeDIBCreatePatternBrush   = GDIP_WMF_RECORD_TO_EMFPLUS(META_DIBCREATEPATTERNBRUSH)
        WmfRecordTypeStretchDIB              = GDIP_WMF_RECORD_TO_EMFPLUS(META_STRETCHDIB)
        WmfRecordTypeExtFloodFill            = GDIP_WMF_RECORD_TO_EMFPLUS(META_EXTFLOODFILL)
        WmfRecordTypeSetLayout               = GDIP_WMF_RECORD_TO_EMFPLUS(0x0149)  # META_SETLAYOUT
        WmfRecordTypeResetDC                 = GDIP_WMF_RECORD_TO_EMFPLUS(0x014C)  # META_RESETDC
        WmfRecordTypeStartDoc                = GDIP_WMF_RECORD_TO_EMFPLUS(0x014D)  # META_STARTDOC
        WmfRecordTypeStartPage               = GDIP_WMF_RECORD_TO_EMFPLUS(0x004F)  # META_STARTPAGE
        WmfRecordTypeEndPage                 = GDIP_WMF_RECORD_TO_EMFPLUS(0x0050)  # META_ENDPAGE
        WmfRecordTypeAbortDoc                = GDIP_WMF_RECORD_TO_EMFPLUS(0x0052)  # META_ABORTDOC
        WmfRecordTypeEndDoc                  = GDIP_WMF_RECORD_TO_EMFPLUS(0x005E)  # META_ENDDOC
        WmfRecordTypeDeleteObject            = GDIP_WMF_RECORD_TO_EMFPLUS(META_DELETEOBJECT)
        WmfRecordTypeCreatePalette           = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEPALETTE)
        WmfRecordTypeCreateBrush             = GDIP_WMF_RECORD_TO_EMFPLUS(0x00F8)  # META_CREATEBRUSH
        WmfRecordTypeCreatePatternBrush      = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEPATTERNBRUSH)
        WmfRecordTypeCreatePenIndirect       = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEPENINDIRECT)
        WmfRecordTypeCreateFontIndirect      = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEFONTINDIRECT)
        WmfRecordTypeCreateBrushIndirect     = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEBRUSHINDIRECT)
        WmfRecordTypeCreateBitmapIndirect    = GDIP_WMF_RECORD_TO_EMFPLUS(0x02FD)  # META_CREATEBITMAPINDIRECT
        WmfRecordTypeCreateBitmap            = GDIP_WMF_RECORD_TO_EMFPLUS(0x06FE)  # META_CREATEBITMAP
        WmfRecordTypeCreateRegion            = GDIP_WMF_RECORD_TO_EMFPLUS(META_CREATEREGION)

        EmfRecordTypeHeader                  = EMR_HEADER
        EmfRecordTypePolyBezier              = EMR_POLYBEZIER
        EmfRecordTypePolygon                 = EMR_POLYGON
        EmfRecordTypePolyline                = EMR_POLYLINE
        EmfRecordTypePolyBezierTo            = EMR_POLYBEZIERTO
        EmfRecordTypePolyLineTo              = EMR_POLYLINETO
        EmfRecordTypePolyPolyline            = EMR_POLYPOLYLINE
        EmfRecordTypePolyPolygon             = EMR_POLYPOLYGON
        EmfRecordTypeSetWindowExtEx          = EMR_SETWINDOWEXTEX
        EmfRecordTypeSetWindowOrgEx          = EMR_SETWINDOWORGEX
        EmfRecordTypeSetViewportExtEx        = EMR_SETVIEWPORTEXTEX
        EmfRecordTypeSetViewportOrgEx        = EMR_SETVIEWPORTORGEX
        EmfRecordTypeSetBrushOrgEx           = EMR_SETBRUSHORGEX
        EmfRecordTypeEOF                     = EMR_EOF
        EmfRecordTypeSetPixelV               = EMR_SETPIXELV
        EmfRecordTypeSetMapperFlags          = EMR_SETMAPPERFLAGS
        EmfRecordTypeSetMapMode              = EMR_SETMAPMODE
        EmfRecordTypeSetBkMode               = EMR_SETBKMODE
        EmfRecordTypeSetPolyFillMode         = EMR_SETPOLYFILLMODE
        EmfRecordTypeSetROP2                 = EMR_SETROP2
        EmfRecordTypeSetStretchBltMode       = EMR_SETSTRETCHBLTMODE
        EmfRecordTypeSetTextAlign            = EMR_SETTEXTALIGN
        EmfRecordTypeSetColorAdjustment      = EMR_SETCOLORADJUSTMENT
        EmfRecordTypeSetTextColor            = EMR_SETTEXTCOLOR
        EmfRecordTypeSetBkColor              = EMR_SETBKCOLOR
        EmfRecordTypeOffsetClipRgn           = EMR_OFFSETCLIPRGN
        EmfRecordTypeMoveToEx                = EMR_MOVETOEX
        EmfRecordTypeSetMetaRgn              = EMR_SETMETARGN
        EmfRecordTypeExcludeClipRect         = EMR_EXCLUDECLIPRECT
        EmfRecordTypeIntersectClipRect       = EMR_INTERSECTCLIPRECT
        EmfRecordTypeScaleViewportExtEx      = EMR_SCALEVIEWPORTEXTEX
        EmfRecordTypeScaleWindowExtEx        = EMR_SCALEWINDOWEXTEX
        EmfRecordTypeSaveDC                  = EMR_SAVEDC
        EmfRecordTypeRestoreDC               = EMR_RESTOREDC
        EmfRecordTypeSetWorldTransform       = EMR_SETWORLDTRANSFORM
        EmfRecordTypeModifyWorldTransform    = EMR_MODIFYWORLDTRANSFORM
        EmfRecordTypeSelectObject            = EMR_SELECTOBJECT
        EmfRecordTypeCreatePen               = EMR_CREATEPEN
        EmfRecordTypeCreateBrushIndirect     = EMR_CREATEBRUSHINDIRECT
        EmfRecordTypeDeleteObject            = EMR_DELETEOBJECT
        EmfRecordTypeAngleArc                = EMR_ANGLEARC
        EmfRecordTypeEllipse                 = EMR_ELLIPSE
        EmfRecordTypeRectangle               = EMR_RECTANGLE
        EmfRecordTypeRoundRect               = EMR_ROUNDRECT
        EmfRecordTypeArc                     = EMR_ARC
        EmfRecordTypeChord                   = EMR_CHORD
        EmfRecordTypePie                     = EMR_PIE
        EmfRecordTypeSelectPalette           = EMR_SELECTPALETTE
        EmfRecordTypeCreatePalette           = EMR_CREATEPALETTE
        EmfRecordTypeSetPaletteEntries       = EMR_SETPALETTEENTRIES
        EmfRecordTypeResizePalette           = EMR_RESIZEPALETTE
        EmfRecordTypeRealizePalette          = EMR_REALIZEPALETTE
        EmfRecordTypeExtFloodFill            = EMR_EXTFLOODFILL
        EmfRecordTypeLineTo                  = EMR_LINETO
        EmfRecordTypeArcTo                   = EMR_ARCTO
        EmfRecordTypePolyDraw                = EMR_POLYDRAW
        EmfRecordTypeSetArcDirection         = EMR_SETARCDIRECTION
        EmfRecordTypeSetMiterLimit           = EMR_SETMITERLIMIT
        EmfRecordTypeBeginPath               = EMR_BEGINPATH
        EmfRecordTypeEndPath                 = EMR_ENDPATH
        EmfRecordTypeCloseFigure             = EMR_CLOSEFIGURE
        EmfRecordTypeFillPath                = EMR_FILLPATH
        EmfRecordTypeStrokeAndFillPath       = EMR_STROKEANDFILLPATH
        EmfRecordTypeStrokePath              = EMR_STROKEPATH
        EmfRecordTypeFlattenPath             = EMR_FLATTENPATH
        EmfRecordTypeWidenPath               = EMR_WIDENPATH
        EmfRecordTypeSelectClipPath          = EMR_SELECTCLIPPATH
        EmfRecordTypeAbortPath               = EMR_ABORTPATH
        EmfRecordTypeReserved_069            = 69  # Not Used
        EmfRecordTypeGdiComment              = EMR_GDICOMMENT
        EmfRecordTypeFillRgn                 = EMR_FILLRGN
        EmfRecordTypeFrameRgn                = EMR_FRAMERGN
        EmfRecordTypeInvertRgn               = EMR_INVERTRGN
        EmfRecordTypePaintRgn                = EMR_PAINTRGN
        EmfRecordTypeExtSelectClipRgn        = EMR_EXTSELECTCLIPRGN
        EmfRecordTypeBitBlt                  = EMR_BITBLT
        EmfRecordTypeStretchBlt              = EMR_STRETCHBLT
        EmfRecordTypeMaskBlt                 = EMR_MASKBLT
        EmfRecordTypePlgBlt                  = EMR_PLGBLT
        EmfRecordTypeSetDIBitsToDevice       = EMR_SETDIBITSTODEVICE
        EmfRecordTypeStretchDIBits           = EMR_STRETCHDIBITS
        EmfRecordTypeExtCreateFontIndirect   = EMR_EXTCREATEFONTINDIRECTW
        EmfRecordTypeExtTextOutA             = EMR_EXTTEXTOUTA
        EmfRecordTypeExtTextOutW             = EMR_EXTTEXTOUTW
        EmfRecordTypePolyBezier16            = EMR_POLYBEZIER16
        EmfRecordTypePolygon16               = EMR_POLYGON16
        EmfRecordTypePolyline16              = EMR_POLYLINE16
        EmfRecordTypePolyBezierTo16          = EMR_POLYBEZIERTO16
        EmfRecordTypePolylineTo16            = EMR_POLYLINETO16
        EmfRecordTypePolyPolyline16          = EMR_POLYPOLYLINE16
        EmfRecordTypePolyPolygon16           = EMR_POLYPOLYGON16
        EmfRecordTypePolyDraw16              = EMR_POLYDRAW16
        EmfRecordTypeCreateMonoBrush         = EMR_CREATEMONOBRUSH
        EmfRecordTypeCreateDIBPatternBrushPt = EMR_CREATEDIBPATTERNBRUSHPT
        EmfRecordTypeExtCreatePen            = EMR_EXTCREATEPEN
        EmfRecordTypePolyTextOutA            = EMR_POLYTEXTOUTA
        EmfRecordTypePolyTextOutW            = EMR_POLYTEXTOUTW
        EmfRecordTypeSetICMMode              = 98  # EMR_SETICMMODE
        EmfRecordTypeCreateColorSpace        = 99  # EMR_CREATECOLORSPACE
        EmfRecordTypeSetColorSpace           = 100 # EMR_SETCOLORSPACE
        EmfRecordTypeDeleteColorSpace        = 101 # EMR_DELETECOLORSPACE
        EmfRecordTypeGLSRecord               = 102 # EMR_GLSRECORD
        EmfRecordTypeGLSBoundedRecord        = 103 # EMR_GLSBOUNDEDRECORD
        EmfRecordTypePixelFormat             = 104 # EMR_PIXELFORMAT
        EmfRecordTypeDrawEscape              = 105 # EMR_RESERVED_105
        EmfRecordTypeExtEscape               = 106 # EMR_RESERVED_106
        EmfRecordTypeStartDoc                = 107 # EMR_RESERVED_107
        EmfRecordTypeSmallTextOut            = 108 # EMR_RESERVED_108
        EmfRecordTypeForceUFIMapping         = 109 # EMR_RESERVED_109
        EmfRecordTypeNamedEscape             = 110 # EMR_RESERVED_110
        EmfRecordTypeColorCorrectPalette     = 111 # EMR_COLORCORRECTPALETTE
        EmfRecordTypeSetICMProfileA          = 112 # EMR_SETICMPROFILEA
        EmfRecordTypeSetICMProfileW          = 113 # EMR_SETICMPROFILEW
        EmfRecordTypeAlphaBlend              = 114 # EMR_ALPHABLEND
        EmfRecordTypeSetLayout               = 115 # EMR_SETLAYOUT
        EmfRecordTypeTransparentBlt          = 116 # EMR_TRANSPARENTBLT
        EmfRecordTypeReserved_117            = 117 # Not Used
        EmfRecordTypeGradientFill            = 118 # EMR_GRADIENTFILL
        EmfRecordTypeSetLinkedUFIs           = 119 # EMR_RESERVED_119
        EmfRecordTypeSetTextJustification    = 120 # EMR_RESERVED_120
        EmfRecordTypeColorMatchToTargetW     = 121 # EMR_COLORMATCHTOTARGETW
        EmfRecordTypeCreateColorSpaceW       = 122 # EMR_CREATECOLORSPACEW
        EmfRecordTypeMax                     = 122
        EmfRecordTypeMin                     = 1

        # That is the END of the GDI EMF records.

        # Now we start the list of EMF+ records.  We leave quite
        # a bit of room here for the addition of any new GDI
        # records that may be added later.

        EmfPlusRecordTypeInvalid = GDIP_EMFPLUS_RECORD_BASE
        EmfPlusRecordTypeHeader = GDIP_EMFPLUS_RECORD_BASE + 1
        EmfPlusRecordTypeEndOfFile = GDIP_EMFPLUS_RECORD_BASE + 2

        EmfPlusRecordTypeComment = GDIP_EMFPLUS_RECORD_BASE + 3

        EmfPlusRecordTypeGetDC = GDIP_EMFPLUS_RECORD_BASE + 4

        EmfPlusRecordTypeMultiFormatStart = GDIP_EMFPLUS_RECORD_BASE + 5
        EmfPlusRecordTypeMultiFormatSection = GDIP_EMFPLUS_RECORD_BASE + 6
        EmfPlusRecordTypeMultiFormatEnd = GDIP_EMFPLUS_RECORD_BASE + 7

        # For all persistent objects
        
        EmfPlusRecordTypeObject = GDIP_EMFPLUS_RECORD_BASE + 8

        # Drawing Records
        
        EmfPlusRecordTypeClear = GDIP_EMFPLUS_RECORD_BASE + 9
        EmfPlusRecordTypeFillRects = GDIP_EMFPLUS_RECORD_BASE + 10
        EmfPlusRecordTypeDrawRects = GDIP_EMFPLUS_RECORD_BASE + 11
        EmfPlusRecordTypeFillPolygon = GDIP_EMFPLUS_RECORD_BASE + 12
        EmfPlusRecordTypeDrawLines = GDIP_EMFPLUS_RECORD_BASE + 13
        EmfPlusRecordTypeFillEllipse = GDIP_EMFPLUS_RECORD_BASE + 14
        EmfPlusRecordTypeDrawEllipse = GDIP_EMFPLUS_RECORD_BASE + 15
        EmfPlusRecordTypeFillPie = GDIP_EMFPLUS_RECORD_BASE + 16
        EmfPlusRecordTypeDrawPie = GDIP_EMFPLUS_RECORD_BASE + 17
        EmfPlusRecordTypeDrawArc = GDIP_EMFPLUS_RECORD_BASE + 18
        EmfPlusRecordTypeFillRegion = GDIP_EMFPLUS_RECORD_BASE + 19
        EmfPlusRecordTypeFillPath = GDIP_EMFPLUS_RECORD_BASE + 20
        EmfPlusRecordTypeDrawPath = GDIP_EMFPLUS_RECORD_BASE + 21
        EmfPlusRecordTypeFillClosedCurve = GDIP_EMFPLUS_RECORD_BASE + 22
        EmfPlusRecordTypeDrawClosedCurve = GDIP_EMFPLUS_RECORD_BASE + 23
        EmfPlusRecordTypeDrawCurve = GDIP_EMFPLUS_RECORD_BASE + 24
        EmfPlusRecordTypeDrawBeziers = GDIP_EMFPLUS_RECORD_BASE + 25
        EmfPlusRecordTypeDrawImage = GDIP_EMFPLUS_RECORD_BASE + 26
        EmfPlusRecordTypeDrawImagePoints = GDIP_EMFPLUS_RECORD_BASE + 27
        EmfPlusRecordTypeDrawString = GDIP_EMFPLUS_RECORD_BASE + 28

        # Graphics State Records
        
        EmfPlusRecordTypeSetRenderingOrigin = GDIP_EMFPLUS_RECORD_BASE + 29
        EmfPlusRecordTypeSetAntiAliasMode = GDIP_EMFPLUS_RECORD_BASE + 30
        EmfPlusRecordTypeSetTextRenderingHint = GDIP_EMFPLUS_RECORD_BASE + 31
        EmfPlusRecordTypeSetTextContrast = GDIP_EMFPLUS_RECORD_BASE + 32
        EmfPlusRecordTypeSetInterpolationMode = GDIP_EMFPLUS_RECORD_BASE + 33
        EmfPlusRecordTypeSetPixelOffsetMode = GDIP_EMFPLUS_RECORD_BASE + 34
        EmfPlusRecordTypeSetCompositingMode = GDIP_EMFPLUS_RECORD_BASE + 35
        EmfPlusRecordTypeSetCompositingQuality = GDIP_EMFPLUS_RECORD_BASE + 36
        EmfPlusRecordTypeSave = GDIP_EMFPLUS_RECORD_BASE + 37
        EmfPlusRecordTypeRestore = GDIP_EMFPLUS_RECORD_BASE + 38
        EmfPlusRecordTypeBeginContainer = GDIP_EMFPLUS_RECORD_BASE + 39
        EmfPlusRecordTypeBeginContainerNoParams = GDIP_EMFPLUS_RECORD_BASE + 40
        EmfPlusRecordTypeEndContainer = GDIP_EMFPLUS_RECORD_BASE + 41
        EmfPlusRecordTypeSetWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 42
        EmfPlusRecordTypeResetWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 43
        EmfPlusRecordTypeMultiplyWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 44
        EmfPlusRecordTypeTranslateWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 45
        EmfPlusRecordTypeScaleWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 46
        EmfPlusRecordTypeRotateWorldTransform = GDIP_EMFPLUS_RECORD_BASE + 47
        EmfPlusRecordTypeSetPageTransform = GDIP_EMFPLUS_RECORD_BASE + 48
        EmfPlusRecordTypeResetClip = GDIP_EMFPLUS_RECORD_BASE + 49
        EmfPlusRecordTypeSetClipRect = GDIP_EMFPLUS_RECORD_BASE + 50
        EmfPlusRecordTypeSetClipPath = GDIP_EMFPLUS_RECORD_BASE + 51
        EmfPlusRecordTypeSetClipRegion = GDIP_EMFPLUS_RECORD_BASE + 52
        EmfPlusRecordTypeOffsetClip = GDIP_EMFPLUS_RECORD_BASE + 53

        EmfPlusRecordTypeDrawDriverString = GDIP_EMFPLUS_RECORD_BASE + 54
        if cpreproc.getdef("GDIPVER") >= 0x0110:
            EmfPlusRecordTypeStrokeFillPath = GDIP_EMFPLUS_RECORD_BASE + 55
            EmfPlusRecordTypeSerializableObject = GDIP_EMFPLUS_RECORD_BASE + 56

            EmfPlusRecordTypeSetTSGraphics = GDIP_EMFPLUS_RECORD_BASE + 57
            EmfPlusRecordTypeSetTSClip = GDIP_EMFPLUS_RECORD_BASE + 58
        # NOTE: New records *must* be added immediately before this line.

        EmfPlusRecordTotal = GDIP_EMFPLUS_RECORD_BASE + 59

        EmfPlusRecordTypeMax = EmfPlusRecordTotal-1
        EmfPlusRecordTypeMin = EmfPlusRecordTypeHeader

    #---------------------------------------------------------------------------
    # StringFormatFlags
    #---------------------------------------------------------------------------

    #---------------------------------------------------------------------------
    # String format flags
    #
    #  DirectionRightToLeft          - For horizontal text the reading order is
    #                                  right to left. This value is called
    #                                  the base embedding level by the Unicode
    #                                  bidirectional engine.
    #                                  For vertical text columns are read from
    #                                  right to left.
    #                                  By default horizontal or vertical text is
    #                                  read from left to right.
    #
    #  DirectionVertical             - Individual lines of text are vertical. In
    #                                  each line characters progress from top to
    #                                  bottom.
    #                                  By default lines of text are horizontal
    #                                  each new line below the previous line.
    #
    #  NoFitBlackBox                 - Allows parts of glyphs to overhang the
    #                                  bounding rectangle.
    #                                  By default glyphs are first aligned
    #                                  inside the margines then any glyphs which
    #                                  still overhang the bounding box are
    #                                  repositioned to avoid any overhang.
    #                                  For example when an italic
    #                                  lower case letter f in a font such as
    #                                  Garamond is aligned at the far left of a
    #                                  rectangle the lower part of the f will
    #                                  reach slightly further left than the left
    #                                  edge of the rectangle. Setting this flag
    #                                  will ensure the character aligns visually
    #                                  with the lines above and below but may
    #                                  cause some pixels outside the formatting
    #                                  rectangle to be clipped or painted.
    #
    #  DisplayFormatControl          - Causes control characters such as the
    #                                  left-to-right mark to be shown in the
    #                                  output with a representative glyph.
    #
    #  NoFontFallback                - Disables fallback to alternate fonts for
    #                                  characters not supported in the requested
    #                                  font. Any missing characters will be
    #                                  be displayed with the fonts missing glyph
    #                                  usually an open square.
    #
    #  NoWrap                        - Disables wrapping of text between lines
    #                                  when formatting within a rectangle.
    #                                  NoWrap is implied when a point is passed
    #                                  instead of a rectangle or when the
    #                                  specified rectangle has a zero line length.
    #
    #  NoClip                        - By default text is clipped to the
    #                                  formatting rectangle. Setting NoClip
    #                                  allows overhanging pixels to affect the
    #                                  device outside the formatting rectangle.
    #                                  Pixels at the end of the line may be
    #                                  affected if the glyphs overhang their
    #                                  cells and either the NoFitBlackBox flag
    #                                  has been set or the glyph extends to far
    #                                  to be fitted.
    #                                  Pixels above/before the first line or
    #                                  below/after the last line may be affected
    #                                  if the glyphs extend beyond their cell
    #                                  ascent / descent. This can occur rarely
    #                                  with unusual diacritic mark combinations.

    #---------------------------------------------------------------------------

    StringFormatFlags = INT
    if True:
        StringFormatFlagsDirectionRightToLeft        = 0x00000001
        StringFormatFlagsDirectionVertical           = 0x00000002
        StringFormatFlagsNoFitBlackBox               = 0x00000004
        StringFormatFlagsDisplayFormatControl        = 0x00000020
        StringFormatFlagsNoFontFallback              = 0x00000400
        StringFormatFlagsMeasureTrailingSpaces       = 0x00000800
        StringFormatFlagsNoWrap                      = 0x00001000
        StringFormatFlagsLineLimit                   = 0x00002000

        StringFormatFlagsNoClip                      = 0x00004000
        StringFormatFlagsBypassGDI                   = 0x80000000

    #---------------------------------------------------------------------------
    # StringTrimming
    #---------------------------------------------------------------------------

    StringTrimming = INT
    if True:
        StringTrimmingNone              = 0
        StringTrimmingCharacter         = 1
        StringTrimmingWord              = 2
        StringTrimmingEllipsisCharacter = 3
        StringTrimmingEllipsisWord      = 4
        StringTrimmingEllipsisPath      = 5

    #---------------------------------------------------------------------------
    # National language digit substitution
    #---------------------------------------------------------------------------

    StringDigitSubstitute = INT
    if True:
        StringDigitSubstituteUser        = 0  # As NLS setting
        StringDigitSubstituteNone        = 1
        StringDigitSubstituteNational    = 2
        StringDigitSubstituteTraditional = 3

    #---------------------------------------------------------------------------
    # Hotkey prefix interpretation
    #---------------------------------------------------------------------------

    HotkeyPrefix = INT
    if True:
        HotkeyPrefixNone        = 0
        HotkeyPrefixShow        = 1
        HotkeyPrefixHide        = 2

    #---------------------------------------------------------------------------
    # String alignment flags
    #---------------------------------------------------------------------------

    StringAlignment = INT
    if True:
        # Left edge for left-to-right text
        # right for right-to-left text
        # and top for vertical
        StringAlignmentNear   = 0
        StringAlignmentCenter = 1
        StringAlignmentFar    = 2

    #---------------------------------------------------------------------------
    # DriverStringOptions
    #---------------------------------------------------------------------------

    DriverStringOptions = INT
    if True:
        DriverStringOptionsCmapLookup             = 1
        DriverStringOptionsVertical               = 2
        DriverStringOptionsRealizedAdvance        = 4
        DriverStringOptionsLimitSubpixel          = 8

    #---------------------------------------------------------------------------
    # Flush Intention flags
    #---------------------------------------------------------------------------

    FlushIntention = INT
    if True:
        FlushIntentionFlush = 0        # Flush all batched rendering operations
        FlushIntentionSync = 1          # Flush all batched rendering operations
                                        # and wait for them to complete

    #---------------------------------------------------------------------------
    # Image encoder parameter related types
    #---------------------------------------------------------------------------

    EncoderParameterValueType = INT
    if True:
        EncoderParameterValueTypeByte           = 1    # 8-bit unsigned int
        EncoderParameterValueTypeASCII          = 2    # 8-bit byte containing one 7-bit ASCII
                                                        # code. NULL terminated.
        EncoderParameterValueTypeShort          = 3    # 16-bit unsigned int
        EncoderParameterValueTypeLong           = 4    # 32-bit unsigned int
        EncoderParameterValueTypeRational       = 5    # Two Longs. The first Long is the
                                                        # numerator the second Long expresses the
                                                        # denomintor.
        EncoderParameterValueTypeLongRange      = 6    # Two longs which specify a range of
                                                        # integer values. The first Long specifies
                                                        # the lower end and the second one
                                                        # specifies the higher end. All values
                                                        # are inclusive at both ends
        EncoderParameterValueTypeUndefined      = 7    # 8-bit byte that can take any value
                                                        # depending on field definition
        EncoderParameterValueTypeRationalRange  = 8    # Two Rationals. The first Rational
                                                        # specifies the lower end and the second
                                                        # specifies the higher end. All values
                                                        # are inclusive at both ends
    #if (GDIPVER >= 0x0110)
        EncoderParameterValueTypePointer        = 9     # a pointer to a parameter defined data.
    #endif #(GDIPVER >= 0x0110)

    #---------------------------------------------------------------------------
    # Image encoder value types
    #---------------------------------------------------------------------------

    EncoderValue = INT
    if True:
        EncoderValueColorTypeCMYK = 0
        EncoderValueColorTypeYCCK = 1
        EncoderValueCompressionLZW = 2
        EncoderValueCompressionCCITT3 = 3
        EncoderValueCompressionCCITT4 = 4
        EncoderValueCompressionRle = 5
        EncoderValueCompressionNone = 6
        EncoderValueScanMethodInterlaced = 7
        EncoderValueScanMethodNonInterlaced = 8
        EncoderValueVersionGif87 = 9
        EncoderValueVersionGif89 = 10
        EncoderValueRenderProgressive = 11
        EncoderValueRenderNonProgressive = 12
        EncoderValueTransformRotate90 = 13
        EncoderValueTransformRotate180 = 14
        EncoderValueTransformRotate270 = 15
        EncoderValueTransformFlipHorizontal = 16
        EncoderValueTransformFlipVertical = 17
        EncoderValueMultiFrame = 18
        EncoderValueLastFrame = 19
        EncoderValueFlush = 20
        EncoderValueFrameDimensionTime = 21
        EncoderValueFrameDimensionResolution = 22
        EncoderValueFrameDimensionPage = 23
        if cpreproc.getdef("GDIPVER") >= 0x0110:
            EncoderValueColorTypeGray = 24
            EncoderValueColorTypeRGB = 25

    #---------------------------------------------------------------------------
    # Conversion of Emf To WMF Bits flags
    #---------------------------------------------------------------------------

    EmfToWmfBitsFlags = INT
    if True:
        EmfToWmfBitsFlagsDefault          = 0x00000000
        EmfToWmfBitsFlagsEmbedEmf         = 0x00000001
        EmfToWmfBitsFlagsIncludePlaceable = 0x00000002
        EmfToWmfBitsFlagsNoXORClip        = 0x00000004

    if cpreproc.getdef("GDIPVER") >= 0x0110:
        #---------------------------------------------------------------------------
        # Conversion of Emf To Emf+ Bits flags
        #---------------------------------------------------------------------------

        ConvertToEmfPlusFlags = INT
        if True:
            ConvertToEmfPlusFlagsDefault       = 0x00000000
            ConvertToEmfPlusFlagsRopUsed       = 0x00000001
            ConvertToEmfPlusFlagsText          = 0x00000002
            ConvertToEmfPlusFlagsInvalidRecord = 0x00000004


    #---------------------------------------------------------------------------
    # Test Control flags
    #---------------------------------------------------------------------------

    GpTestControlEnum = INT
    if True:
        TestControlForceBilinear = 0
        TestControlNoICM = 1
        TestControlGetBuildNumber = 2

    # REGION ***

# !_GDIPLUSENUMS_H