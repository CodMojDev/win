"""
/**************************************************************************\
* 
* Copyright (c) 1999-2000  Microsoft Corporation
*
* Module Name:
*
*   GdiplusImaging.h
*
* Abstract:
*
*   GDI+ Imaging GUIDs
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSIMAGING_H"):
    
    from .gdipluspixelformats import PixelFormat
    from .guiddef import IID, CLSID, GUID
    from .com.unknwn import *
    from .minwindef import *
    
    PROPID = CLSID

    # REGION *** Desktop Family ***

    #---------------------------------------------------------------------------
    # Image file format identifiers
    #---------------------------------------------------------------------------

    ImageFormatUndefined = IID("{b96b3ca9-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatMemoryBMP = IID("{b96b3caa-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatBMP = IID("{b96b3cab-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatEMF = IID("{b96b3cac-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatWMF = IID("{b96b3cad-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatJPEG = IID("{b96b3cae-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatPNG = IID("{b96b3caf-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatGIF = IID("{b96b3cb0-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatTIFF = IID("{b96b3cb1-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatEXIF = IID("{b96b3cb2-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatIcon = IID("{b96b3cb5-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatHEIF = IID("{b96b3cb6-0728-11d3-9d7b-0000f81ef32e}")
    ImageFormatWEBP = IID("{b96b3cb7-0728-11d3-9d7b-0000f81ef32e}")

    #---------------------------------------------------------------------------
    # Predefined multi-frame dimension IDs
    #---------------------------------------------------------------------------

    FrameDimensionTime = IID("{6aedbd6d-3fb5-418a-83a6-7f45229dc872}")
    FrameDimensionResolution = IID("{84236f7b-3bd3-428f-8dab-4ea1439ca315}")
    FrameDimensionPage = IID("{7462dc86-6180-4c7e-8e3f-ee7333a7a483}")

    #---------------------------------------------------------------------------
    # Property sets
    #---------------------------------------------------------------------------

    FormatIDImageInformation = IID("{e5836cbe-5eef-4f1d-acde-ae4c43b608ce}")
    FormatIDJpegAppHeaders = IID("{1c4afdcd-6177-43cf-abc7-5f51af39ee85}")

    #---------------------------------------------------------------------------
    # Encoder parameter sets
    #---------------------------------------------------------------------------

    EncoderCompression = IID("{e09d739d-ccd4-44ee-8eba-3fbf8be4fc58}")
    EncoderColorDepth = IID("{66087055-ad66-4c7c-9a18-38a2310b8337}")
    EncoderScanMethod = IID("{3a4e2661-3109-4e56-8536-42c156e7dcfa}")
    EncoderVersion = IID("{24d18c76-814a-41a4-bf53-1c219cccf797}")
    EncoderRenderMethod = IID("{6d42c53a-229a-4825-8bb7-5c99e2b9a8b8}")
    EncoderQuality = IID("{1d5be4b5-fa4a-452d-9cdd-5db35105e7eb}")
    EncoderTransformation= IID("{8d0eb2d1-a58e-4ea8-aa14-108074b7b6f9}")
    EncoderLuminanceTable = IID("{edb33bce-0266-4a77-b904-27216099e717}")
    EncoderChrominanceTable = IID("{f2e455dc-09b3-4316-8260-676ada32481c}")
    EncoderSaveFlag = IID("{292266fc-ac40-47bf-8cfc-a85b89a655de}")

    if cpreproc.getdef("GDIPVER") >= 0x0110:
        EncoderColorSpace = IID("{ae7a62a0-ee2c-49d8-9d07-1ba8a927596e}")
        EncoderImageItems = IID("{63875e13-1f1d-45ab-9195-a29b6066a650}")
        EncoderSaveAsCMYK = IID("{a219bbc9-0a9d-4005-a3ee-3a421b8bb06c}")
    #(GDIPVER >= 0x0110)

    CodecIImageBytes = IID("{025d1823-6c7d-447b-bbdb-a3cbc3dfa2fc}")

    class IImageBytes(IUnknown):
        _iid_ = CodecIImageBytes
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)

        @virtual_table.com_function(PUINT)
        def CountBytes(self, pcb: PUINT) ->  int:
            """
            Return total number of bytes in the IStream
            """
            
        @virtual_table.com_function(UINT, ULONG, PVOID)
        def LockBytes(self, cb: int, ulOffset: int, ppvBytes: IPointer[PVOID]) -> int: 
            """
            Locks "cb" bytes, starting from "ulOffset" in the stream, and returns the
            pointer to the beginning of the locked memory chunk in "ppvBytes"
            """
            
        @virtual_table.com_function(PVOID, UINT, ULONG)
        def UnlockBytes(self, pvBytes: IVoidPtr, cb: int, ulOffset: int) -> int: 
            """
            Unlocks "cb" bytes, pointed by "pvBytes", starting from "ulOffset" in the
            stream
            """

        virtual_table.build()

    #--------------------------------------------------------------------------
    # ImageCodecInfo structure
    #--------------------------------------------------------------------------

    class ImageCodecInfo(CStructure):
        _fields_ = [
            ("Clsid", CLSID),
            ("FormatID", GUID),
            ("CodecName", LPWSTR),
            ("DllName", LPWSTR),
            ("FormatDescription", LPWSTR),
            ("FilenameExtension", LPWSTR),
            ("MimeType", LPWSTR),
            ("Flags", DWORD),
            ("Version", DWORD),
            ("SigCount", DWORD),
            ("SigSize", DWORD),
            ("SigPattern", PBYTE),
            ("SigMask", PBYTE)
        ]

    #--------------------------------------------------------------------------
    # Information flags about image codecs
    #--------------------------------------------------------------------------

    ImageCodecFlags = INT
    if True:
        ImageCodecFlagsEncoder            = 0x00000001
        ImageCodecFlagsDecoder            = 0x00000002
        ImageCodecFlagsSupportBitmap      = 0x00000004
        ImageCodecFlagsSupportVector      = 0x00000008
        ImageCodecFlagsSeekableEncode     = 0x00000010
        ImageCodecFlagsBlockingDecode     = 0x00000020

        ImageCodecFlagsBuiltin            = 0x00010000
        ImageCodecFlagsSystem             = 0x00020000
        ImageCodecFlagsUser               = 0x00040000

    #---------------------------------------------------------------------------
    # Access modes used when calling Image::LockBits
    #---------------------------------------------------------------------------

    ImageLockMode = INT
    if True:
        ImageLockModeRead        = 0x0001
        ImageLockModeWrite       = 0x0002
        ImageLockModeUserInputBuf= 0x0004

    #---------------------------------------------------------------------------
    # Information about image pixel data
    #---------------------------------------------------------------------------

    class BitmapData(CStructure):
        _fields_ = [
            ("Width", UINT),
            ("Height", UINT),
            ("Stride", INT),
            ("PixelFormat", PixelFormat),
            ("Scan0", PVOID),
            ("Reserved", UINT_PTR)
        ]
        
        Width: int
        Height: int
        Stride: int
        PixelFormat: int
        Scan0: IVoidPtr
        Reserved: int

    #---------------------------------------------------------------------------
    # Image flags
    #---------------------------------------------------------------------------

    ImageFlags = INT
    if True:
        ImageFlagsNone                = 0

        # Low-word: shared with SINKFLAG_x

        ImageFlagsScalable            = 0x0001
        ImageFlagsHasAlpha            = 0x0002
        ImageFlagsHasTranslucent      = 0x0004
        ImageFlagsPartiallyScalable   = 0x0008

        # Low-word: color space definition

        ImageFlagsColorSpaceRGB       = 0x0010
        ImageFlagsColorSpaceCMYK      = 0x0020
        ImageFlagsColorSpaceGRAY      = 0x0040
        ImageFlagsColorSpaceYCBCR     = 0x0080
        ImageFlagsColorSpaceYCCK      = 0x0100
    
        # Low-word: image size info

        ImageFlagsHasRealDPI          = 0x1000
        ImageFlagsHasRealPixelSize    = 0x2000

        # High-word

        ImageFlagsReadOnly            = 0x00010000
        ImageFlagsCaching             = 0x00020000

    RotateFlipType = INT
    if True:
        RotateNoneFlipNone = 0
        Rotate90FlipNone   = 1
        Rotate180FlipNone  = 2
        Rotate270FlipNone  = 3

        RotateNoneFlipX    = 4
        Rotate90FlipX      = 5
        Rotate180FlipX     = 6
        Rotate270FlipX     = 7

        RotateNoneFlipY    = Rotate180FlipX
        Rotate90FlipY      = Rotate270FlipX
        Rotate180FlipY     = RotateNoneFlipX
        Rotate270FlipY     = Rotate90FlipX

        RotateNoneFlipXY   = Rotate180FlipNone
        Rotate90FlipXY     = Rotate270FlipNone
        Rotate180FlipXY    = RotateNoneFlipNone
        Rotate270FlipXY    = Rotate90FlipNone
        
    #---------------------------------------------------------------------------
    # Encoder Parameter structure
    #---------------------------------------------------------------------------
    class EncoderParameter(CStructure):
        _fields = [
            ("Guid", GUID),                # GUID of the parameter
            ("NumberOfValues", ULONG),     # Number of the parameter values
            ("Type", ULONG),               # Value type, like ValueTypeLONG  etc.
            ("Value", PVOID),              # A pointer to the parameter values
        ]
        
        Guid: GUID
        NumberOfValues: int
        Type: int
        Value: IVoidPtr

    #---------------------------------------------------------------------------
    # Encoder Parameters structure
    #---------------------------------------------------------------------------
    class EncoderParameters(CStructure):
        _fields_ = [
            ("Count", UINT),                           # Number of parameters in this structure
            ("Parameter", POINTER(EncoderParameter))   # Parameter values
        ]
        
        Count: int
        Parameter: IPointer[EncoderParameter]

    if cpreproc.getdef("GDIPVER") >= 0x0110:
        ItemDataPosition = INT
        if True:
            ItemDataPositionAfterHeader    = 0x0
            ItemDataPositionAfterPalette   = 0x1
            ItemDataPositionAfterBits      = 0x2

        #---------------------------------------------------------------------------
        # External Data Item
        #---------------------------------------------------------------------------
        class ImageItemData(CStructure):
            _fields_ = [
                ("Size", UINT),           # size of the structure 
                ("Position", UINT),       # flags describing how the data is to be used.
                ("Desc", PVOID),          # description on how the data is to be saved.
                                          # it is different for every codec type.
                ("DescSize", UINT),       # size memory pointed by Desc
                ("Data", PVOID),          # pointer to the data that is to be saved in the
                                          # file, could be anything saved directly.
                ("DataSize", UINT),       # size memory pointed by Data
                ("Cookie", UINT)          # opaque for the apps data member used during
                                          # enumeration of image data items.
            ]
    #(GDIPVER >= 0x0110)

    #---------------------------------------------------------------------------
    # Property Item
    #---------------------------------------------------------------------------
    class PropertyItem(CStructure):
        _fields_ = [
            ("id", PROPID),                 # ID of this property
            ("length", ULONG),              # Length of the property value, in bytes
            ("type", WORD),                 # Type of the value, as one of TAG_TYPE_XXX
                                            # defined above
            ("value", PVOID)                # property value
        ]

    #---------------------------------------------------------------------------
    # Image property types 
    #---------------------------------------------------------------------------
    PropertyTagTypeByte        = 1
    PropertyTagTypeASCII       = 2
    PropertyTagTypeShort       = 3
    PropertyTagTypeLong        = 4
    PropertyTagTypeRational    = 5
    PropertyTagTypeUndefined   = 7
    PropertyTagTypeSLONG       = 9
    PropertyTagTypeSRational  = 10

    #---------------------------------------------------------------------------
    # Image property ID tags
    #---------------------------------------------------------------------------

    PropertyTagExifIFD             = 0x8769
    PropertyTagGpsIFD              = 0x8825

    PropertyTagNewSubfileType      = 0x00FE
    PropertyTagSubfileType         = 0x00FF
    PropertyTagImageWidth          = 0x0100
    PropertyTagImageHeight         = 0x0101
    PropertyTagBitsPerSample       = 0x0102
    PropertyTagCompression         = 0x0103
    PropertyTagPhotometricInterp   = 0x0106
    PropertyTagThreshHolding       = 0x0107
    PropertyTagCellWidth           = 0x0108
    PropertyTagCellHeight          = 0x0109
    PropertyTagFillOrder           = 0x010A
    PropertyTagDocumentName        = 0x010D
    PropertyTagImageDescription    = 0x010E
    PropertyTagEquipMake           = 0x010F
    PropertyTagEquipModel          = 0x0110
    PropertyTagStripOffsets        = 0x0111
    PropertyTagOrientation         = 0x0112
    PropertyTagSamplesPerPixel     = 0x0115
    PropertyTagRowsPerStrip        = 0x0116
    PropertyTagStripBytesCount     = 0x0117
    PropertyTagMinSampleValue      = 0x0118
    PropertyTagMaxSampleValue      = 0x0119
    PropertyTagXResolution         = 0x011A   # Image resolution in width direction
    PropertyTagYResolution         = 0x011B   # Image resolution in height direction
    PropertyTagPlanarConfig        = 0x011C   # Image data arrangement
    PropertyTagPageName            = 0x011D
    PropertyTagXPosition           = 0x011E
    PropertyTagYPosition           = 0x011F
    PropertyTagFreeOffset          = 0x0120
    PropertyTagFreeByteCounts      = 0x0121
    PropertyTagGrayResponseUnit    = 0x0122
    PropertyTagGrayResponseCurve   = 0x0123
    PropertyTagT4Option            = 0x0124
    PropertyTagT6Option            = 0x0125
    PropertyTagResolutionUnit      = 0x0128   # Unit of X and Y resolution
    PropertyTagPageNumber          = 0x0129
    PropertyTagTransferFuncition   = 0x012D
    PropertyTagSoftwareUsed        = 0x0131
    PropertyTagDateTime            = 0x0132
    PropertyTagArtist              = 0x013B
    PropertyTagHostComputer        = 0x013C
    PropertyTagPredictor           = 0x013D
    PropertyTagWhitePoint          = 0x013E
    PropertyTagPrimaryChromaticities = 0x013F
    PropertyTagColorMap            = 0x0140
    PropertyTagHalftoneHints       = 0x0141
    PropertyTagTileWidth           = 0x0142
    PropertyTagTileLength          = 0x0143
    PropertyTagTileOffset          = 0x0144
    PropertyTagTileByteCounts      = 0x0145
    PropertyTagInkSet              = 0x014C
    PropertyTagInkNames            = 0x014D
    PropertyTagNumberOfInks        = 0x014E
    PropertyTagDotRange            = 0x0150
    PropertyTagTargetPrinter       = 0x0151
    PropertyTagExtraSamples        = 0x0152
    PropertyTagSampleFormat        = 0x0153
    PropertyTagSMinSampleValue     = 0x0154
    PropertyTagSMaxSampleValue     = 0x0155
    PropertyTagTransferRange       = 0x0156

    PropertyTagJPEGProc            = 0x0200
    PropertyTagJPEGInterFormat     = 0x0201
    PropertyTagJPEGInterLength     = 0x0202
    PropertyTagJPEGRestartInterval = 0x0203
    PropertyTagJPEGLosslessPredictors  = 0x0205
    PropertyTagJPEGPointTransforms     = 0x0206
    PropertyTagJPEGQTables         = 0x0207
    PropertyTagJPEGDCTables        = 0x0208
    PropertyTagJPEGACTables        = 0x0209

    PropertyTagYCbCrCoefficients   = 0x0211
    PropertyTagYCbCrSubsampling    = 0x0212
    PropertyTagYCbCrPositioning    = 0x0213
    PropertyTagREFBlackWhite       = 0x0214

    PropertyTagICCProfile          = 0x8773   # This TAG is defined by ICC
                                                    # for embedded ICC in TIFF
    PropertyTagGamma               = 0x0301
    PropertyTagICCProfileDescriptor = 0x0302
    PropertyTagSRGBRenderingIntent = 0x0303

    PropertyTagImageTitle          = 0x0320
    PropertyTagCopyright           = 0x8298

    # Extra TAGs (Like Adobe Image Information tags etc.)

    PropertyTagResolutionXUnit           = 0x5001
    PropertyTagResolutionYUnit           = 0x5002
    PropertyTagResolutionXLengthUnit     = 0x5003
    PropertyTagResolutionYLengthUnit     = 0x5004
    PropertyTagPrintFlags                = 0x5005
    PropertyTagPrintFlagsVersion         = 0x5006
    PropertyTagPrintFlagsCrop            = 0x5007
    PropertyTagPrintFlagsBleedWidth      = 0x5008
    PropertyTagPrintFlagsBleedWidthScale = 0x5009
    PropertyTagHalftoneLPI               = 0x500A
    PropertyTagHalftoneLPIUnit           = 0x500B
    PropertyTagHalftoneDegree            = 0x500C
    PropertyTagHalftoneShape             = 0x500D
    PropertyTagHalftoneMisc              = 0x500E
    PropertyTagHalftoneScreen            = 0x500F
    PropertyTagJPEGQuality               = 0x5010
    PropertyTagGridSize                  = 0x5011
    PropertyTagThumbnailFormat           = 0x5012  # 1 = JPEG, 0 = RAW RGB
    PropertyTagThumbnailWidth            = 0x5013
    PropertyTagThumbnailHeight           = 0x5014
    PropertyTagThumbnailColorDepth       = 0x5015
    PropertyTagThumbnailPlanes           = 0x5016
    PropertyTagThumbnailRawBytes         = 0x5017
    PropertyTagThumbnailSize             = 0x5018
    PropertyTagThumbnailCompressedSize   = 0x5019
    PropertyTagColorTransferFunction     = 0x501A
    PropertyTagThumbnailData             = 0x501B# RAW thumbnail bits in
                                                    # JPEG format or RGB format
                                                    # depends on
                                                    # PropertyTagThumbnailFormat

    # Thumbnail related TAGs
                                                    
    PropertyTagThumbnailImageWidth       = 0x5020  # Thumbnail width
    PropertyTagThumbnailImageHeight      = 0x5021  # Thumbnail height
    PropertyTagThumbnailBitsPerSample    = 0x5022  # Number of bits per
                                                        # component
    PropertyTagThumbnailCompression      = 0x5023  # Compression Scheme
    PropertyTagThumbnailPhotometricInterp = 0x5024 # Pixel composition
    PropertyTagThumbnailImageDescription = 0x5025  # Image Tile
    PropertyTagThumbnailEquipMake        = 0x5026  # Manufacturer of Image
                                                        # Input equipment
    PropertyTagThumbnailEquipModel       = 0x5027  # Model of Image input
                                                        # equipment
    PropertyTagThumbnailStripOffsets     = 0x5028  # Image data location
    PropertyTagThumbnailOrientation      = 0x5029  # Orientation of image
    PropertyTagThumbnailSamplesPerPixel  = 0x502A  # Number of components
    PropertyTagThumbnailRowsPerStrip     = 0x502B  # Number of rows per strip
    PropertyTagThumbnailStripBytesCount  = 0x502C  # Bytes per compressed
                                                        # strip
    PropertyTagThumbnailResolutionX      = 0x502D  # Resolution in width
                                                        # direction
    PropertyTagThumbnailResolutionY      = 0x502E  # Resolution in height
                                                        # direction
    PropertyTagThumbnailPlanarConfig     = 0x502F  # Image data arrangement
    PropertyTagThumbnailResolutionUnit   = 0x5030  # Unit of X and Y
                                                        # Resolution
    PropertyTagThumbnailTransferFunction = 0x5031  # Transfer function
    PropertyTagThumbnailSoftwareUsed     = 0x5032  # Software used
    PropertyTagThumbnailDateTime         = 0x5033  # File change date and
                                                        # time
    PropertyTagThumbnailArtist           = 0x5034  # Person who created the
                                                        # image
    PropertyTagThumbnailWhitePoint       = 0x5035  # White point chromaticity
    PropertyTagThumbnailPrimaryChromaticities = 0x5036
                                                        # Chromaticities of
                                                        # primaries
    PropertyTagThumbnailYCbCrCoefficients = 0x5037 # Color space transforma-
                                                        # tion coefficients
    PropertyTagThumbnailYCbCrSubsampling = 0x5038  # Subsampling ratio of Y
                                                        # to C
    PropertyTagThumbnailYCbCrPositioning = 0x5039  # Y and C position
    PropertyTagThumbnailRefBlackWhite    = 0x503A  # Pair of black and white
                                                        # reference values
    PropertyTagThumbnailCopyRight        = 0x503B  # CopyRight holder

    PropertyTagLuminanceTable            = 0x5090
    PropertyTagChrominanceTable          = 0x5091

    PropertyTagFrameDelay                = 0x5100
    PropertyTagLoopCount                 = 0x5101

    #if (GDIPVER >= 0x0110)
    PropertyTagGlobalPalette             = 0x5102
    PropertyTagIndexBackground           = 0x5103
    PropertyTagIndexTransparent          = 0x5104
    #endif #(GDIPVER >= 0x0110)

    PropertyTagPixelUnit         = 0x5110  # Unit specifier for pixel/unit
    PropertyTagPixelPerUnitX     = 0x5111  # Pixels per unit in X
    PropertyTagPixelPerUnitY     = 0x5112  # Pixels per unit in Y
    PropertyTagPaletteHistogram  = 0x5113  # Palette histogram

    # EXIF specific tag

    PropertyTagExifExposureTime  = 0x829A
    PropertyTagExifFNumber       = 0x829D

    PropertyTagExifExposureProg  = 0x8822
    PropertyTagExifSpectralSense = 0x8824
    PropertyTagExifISOSpeed      = 0x8827
    PropertyTagExifOECF          = 0x8828

    PropertyTagExifVer            = 0x9000
    PropertyTagExifDTOrig         = 0x9003 # Date & time of original
    PropertyTagExifDTDigitized    = 0x9004 # Date & time of digital data generation

    PropertyTagExifCompConfig     = 0x9101
    PropertyTagExifCompBPP        = 0x9102

    PropertyTagExifShutterSpeed   = 0x9201
    PropertyTagExifAperture       = 0x9202
    PropertyTagExifBrightness     = 0x9203
    PropertyTagExifExposureBias   = 0x9204
    PropertyTagExifMaxAperture    = 0x9205
    PropertyTagExifSubjectDist    = 0x9206
    PropertyTagExifMeteringMode   = 0x9207
    PropertyTagExifLightSource    = 0x9208
    PropertyTagExifFlash          = 0x9209
    PropertyTagExifFocalLength    = 0x920A
    PropertyTagExifSubjectArea    = 0x9214  # exif 2.2 Subject Area
    PropertyTagExifMakerNote      = 0x927C
    PropertyTagExifUserComment    = 0x9286
    PropertyTagExifDTSubsec       = 0x9290  # Date & Time subseconds
    PropertyTagExifDTOrigSS       = 0x9291  # Date & Time original subseconds
    PropertyTagExifDTDigSS        = 0x9292  # Date & TIme digitized subseconds

    PropertyTagExifFPXVer         = 0xA000
    PropertyTagExifColorSpace     = 0xA001
    PropertyTagExifPixXDim        = 0xA002
    PropertyTagExifPixYDim        = 0xA003
    PropertyTagExifRelatedWav     = 0xA004  # related sound file
    PropertyTagExifInterop        = 0xA005
    PropertyTagExifFlashEnergy    = 0xA20B
    PropertyTagExifSpatialFR      = 0xA20C  # Spatial Frequency Response
    PropertyTagExifFocalXRes      = 0xA20E  # Focal Plane X Resolution
    PropertyTagExifFocalYRes      = 0xA20F  # Focal Plane Y Resolution
    PropertyTagExifFocalResUnit   = 0xA210  # Focal Plane Resolution Unit
    PropertyTagExifSubjectLoc     = 0xA214
    PropertyTagExifExposureIndex  = 0xA215
    PropertyTagExifSensingMethod  = 0xA217
    PropertyTagExifFileSource     = 0xA300
    PropertyTagExifSceneType      = 0xA301
    PropertyTagExifCfaPattern     = 0xA302

    # New EXIF 2.2 properties

    PropertyTagExifCustomRendered           = 0xA401
    PropertyTagExifExposureMode             = 0xA402
    PropertyTagExifWhiteBalance             = 0xA403
    PropertyTagExifDigitalZoomRatio         = 0xA404
    PropertyTagExifFocalLengthIn35mmFilm    = 0xA405
    PropertyTagExifSceneCaptureType         = 0xA406
    PropertyTagExifGainControl              = 0xA407
    PropertyTagExifContrast                 = 0xA408
    PropertyTagExifSaturation               = 0xA409
    PropertyTagExifSharpness                = 0xA40A
    PropertyTagExifDeviceSettingDesc        = 0xA40B
    PropertyTagExifSubjectDistanceRange     = 0xA40C
    PropertyTagExifUniqueImageID            = 0xA420


    PropertyTagGpsVer             = 0x0000
    PropertyTagGpsLatitudeRef     = 0x0001
    PropertyTagGpsLatitude        = 0x0002
    PropertyTagGpsLongitudeRef    = 0x0003
    PropertyTagGpsLongitude       = 0x0004
    PropertyTagGpsAltitudeRef     = 0x0005
    PropertyTagGpsAltitude        = 0x0006
    PropertyTagGpsGpsTime         = 0x0007
    PropertyTagGpsGpsSatellites   = 0x0008
    PropertyTagGpsGpsStatus       = 0x0009
    PropertyTagGpsGpsMeasureMode  = 0x00A
    PropertyTagGpsGpsDop          = 0x000B  # Measurement precision
    PropertyTagGpsSpeedRef        = 0x000C
    PropertyTagGpsSpeed           = 0x000D
    PropertyTagGpsTrackRef        = 0x000E
    PropertyTagGpsTrack           = 0x000F
    PropertyTagGpsImgDirRef       = 0x0010
    PropertyTagGpsImgDir          = 0x0011
    PropertyTagGpsMapDatum        = 0x0012
    PropertyTagGpsDestLatRef      = 0x0013
    PropertyTagGpsDestLat         = 0x0014
    PropertyTagGpsDestLongRef     = 0x0015
    PropertyTagGpsDestLong        = 0x0016
    PropertyTagGpsDestBearRef     = 0x0017
    PropertyTagGpsDestBear        = 0x0018
    PropertyTagGpsDestDistRef     = 0x0019
    PropertyTagGpsDestDist        = 0x001A
    PropertyTagGpsProcessingMethod = 0x001B
    PropertyTagGpsAreaInformation = 0x001C
    PropertyTagGpsDate            = 0x001D
    PropertyTagGpsDifferential    = 0x001E

    # REGION ***