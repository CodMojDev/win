from .minwindef import *
from .basetsd import *

from .winnt import (LongToHandle, PPOINTS, BYTE,
                    ULONG_PTR, LOBYTE, UINT32,
                    UINT64, LUID, UINT16,
                    PSTR, CALLBACK, VOID, PROC,
                    PVOID, WINAPI, PLPVOID, HGLRC)

from .defbase import *

from . import cpreproc

if cpreproc.pragma_once("_WINGDI_"):
    if cpreproc.ifndef("NOGDI"):
        gdi32 = W_WinDLL("gdi32.dll")
        msimg32 = W_WinDLL("msimg32.dll")
        winspool = W_WinDLL('winspool.drv')
        opengl32 = W_WinDLL("opengl32.dll")
        if cpreproc.ifndef("NORASTEROPS"):
            # Binary raster ops
            R2_BLACK = 1 #  0
            R2_NOTMERGEPEN = 2 # DPon
            R2_MASKNOTPEN = 3 # DPna
            R2_NOTCOPYPEN = 4 # PN
            R2_MASKPENNOT = 5 # PDna
            R2_NOT = 6 # Dn
            R2_XORPEN = 7 # DPx
            R2_NOTMASKPEN = 8 # DPan
            R2_MASKPEN = 9 # DPa
            R2_NOTXORPEN = 10 # DPxn
            R2_NOP = 11 # D
            R2_MERGENOTPEN = 12 # DPno
            R2_COPYPEN = 13 # P
            R2_MERGEPENNOT = 14 # PDno
            R2_MERGEPEN = 15 # DPo
            R2_WHITE = 16 #  1
            R2_LAST = 16
            # Ternary raster operations
            SRCCOPY = DWORD(0x00CC0020).value # dest = source
            SRCPAINT = DWORD(0x00EE0086).value # dest = source OR dest
            SRCAND = DWORD(0x008800C6).value # dest = source AND dest
            SRCINVERT = DWORD(0x00660046).value # dest = source XOR dest
            SRCERASE = DWORD(0x00440328).value # dest = source AND (NOT dest )
            NOTSRCCOPY = DWORD(0x00330008).value # dest = (NOT source)
            NOTSRCERASE = DWORD(0x001100A6).value # dest = (NOT src) AND (NOT dest)
            MERGECOPY = DWORD(0x00C000CA).value # dest = (source AND pattern)
            MERGEPAINT = DWORD(0x00BB0226).value # dest = (NOT source) OR dest
            PATCOPY = DWORD(0x00F00021).value # dest = pattern
            PATPAINT = DWORD(0x00FB0A09).value # dest = DPSnoo
            PATINVERT = DWORD(0x005A0049).value # dest = pattern XOR dest
            DSTINVERT = DWORD(0x00550009).value # dest = (NOT dest)
            BLACKNESS = DWORD(0x00000042).value # dest = BLACK
            WHITENESS = DWORD(0x00FF0062).value # dest = WHITE
            NOMIRRORBITMAP = DWORD(0x80000000).value # Do not Mirror the bitmap in this call
            CAPTUREBLT = DWORD(0x40000000).value # Include layered windows
            # Quaternary raster codes
            MAKEROP4 = lambda fore,back: DWORD(((((back) << 8) & 0xFF000000) | (fore))).value
        # NORASTEROPS
        GDI_ERROR = (0xFFFFFFFF)
        HGDI_ERROR = (LongToHandle(0xFFFFFFFF))
        HGDI_ERROR = HANDLE(-1)
        # Region Flags
        ERROR = 0
        NULLREGION = 1
        SIMPLEREGION = 2
        COMPLEXREGION = 3
        RGN_ERROR = ERROR
        # CombineRgn() Styles
        RGN_AND = 1
        RGN_OR = 2
        RGN_XOR = 3
        RGN_DIFF = 4
        RGN_COPY = 5
        RGN_MIN = RGN_AND
        RGN_MAX = RGN_COPY
        # StretchBlt() Modes
        BLACKONWHITE = 1
        WHITEONBLACK = 2
        COLORONCOLOR = 3
        HALFTONE = 4
        MAXSTRETCHBLTMODE = 4
        # New StretchBlt() Modes
        STRETCH_ANDSCANS = BLACKONWHITE
        STRETCH_ORSCANS = WHITEONBLACK
        STRETCH_DELETESCANS = COLORONCOLOR
        STRETCH_HALFTONE = HALFTONE
        # PolyFill() Modes
        ALTERNATE = 1
        WINDING = 2
        POLYFILL_LAST = 2
        # Layout Orientation Options
        LAYOUT_RTL = 0x00000001 # Right to left
        LAYOUT_BTT = 0x00000002 # Bottom to top
        LAYOUT_VBH = 0x00000004 # Vertical before horizontal
        LAYOUT_ORIENTATIONMASK = (LAYOUT_RTL | LAYOUT_BTT | LAYOUT_VBH)
        LAYOUT_BITMAPORIENTATIONPRESERVED = 0x00000008
        # Text Alignment Options
        TA_NOUPDATECP = 0
        TA_UPDATECP = 1
        TA_LEFT = 0
        TA_RIGHT = 2
        TA_CENTER = 6
        TA_TOP = 0
        TA_BOTTOM = 8
        TA_BASELINE = 24
        TA_RTLREADING = 256
        TA_MASK = (TA_BASELINE+TA_CENTER+TA_UPDATECP+TA_RTLREADING)
        TA_MASK = (TA_BASELINE+TA_CENTER+TA_UPDATECP)
        VTA_BASELINE = TA_BASELINE
        VTA_LEFT = TA_BOTTOM
        VTA_RIGHT = TA_TOP
        VTA_CENTER = TA_CENTER
        VTA_BOTTOM = TA_RIGHT
        VTA_TOP = TA_LEFT
        ETO_OPAQUE = 0x0002
        ETO_CLIPPED = 0x0004
        ETO_GLYPH_INDEX = 0x0010
        ETO_RTLREADING = 0x0080
        ETO_NUMERICSLOCAL = 0x0400
        ETO_NUMERICSLATIN = 0x0800
        ETO_IGNORELANGUAGE = 0x1000
        ETO_PDY = 0x2000
        ETO_REVERSE_INDEX_MAP = 0x10000
        ASPECT_FILTERING = 0x0001
        # Bounds Accumulation APIs
        DCB_RESET = 0x0001
        DCB_ACCUMULATE = 0x0002
        DCB_DIRTY = DCB_ACCUMULATE
        DCB_SET = (DCB_RESET | DCB_ACCUMULATE)
        DCB_ENABLE = 0x0004
        DCB_DISABLE = 0x0008
        if cpreproc.ifndef("NOMETAFILE"):
            # Metafile Functions
            META_SETBKCOLOR = 0x0201
            META_SETBKMODE = 0x0102
            META_SETMAPMODE = 0x0103
            META_SETROP2 = 0x0104
            META_SETRELABS = 0x0105
            META_SETPOLYFILLMODE = 0x0106
            META_SETSTRETCHBLTMODE = 0x0107
            META_SETTEXTCHAREXTRA = 0x0108
            META_SETTEXTCOLOR = 0x0209
            META_SETTEXTJUSTIFICATION = 0x020A
            META_SETWINDOWORG = 0x020B
            META_SETWINDOWEXT = 0x020C
            META_SETVIEWPORTORG = 0x020D
            META_SETVIEWPORTEXT = 0x020E
            META_OFFSETWINDOWORG = 0x020F
            META_SCALEWINDOWEXT = 0x0410
            META_OFFSETVIEWPORTORG = 0x0211
            META_SCALEVIEWPORTEXT = 0x0412
            META_LINETO = 0x0213
            META_MOVETO = 0x0214
            META_EXCLUDECLIPRECT = 0x0415
            META_INTERSECTCLIPRECT = 0x0416
            META_ARC = 0x0817
            META_ELLIPSE = 0x0418
            META_FLOODFILL = 0x0419
            META_PIE = 0x081A
            META_RECTANGLE = 0x041B
            META_ROUNDRECT = 0x061C
            META_PATBLT = 0x061D
            META_SAVEDC = 0x001E
            META_SETPIXEL = 0x041F
            META_OFFSETCLIPRGN = 0x0220
            META_TEXTOUT = 0x0521
            META_BITBLT = 0x0922
            META_STRETCHBLT = 0x0B23
            META_POLYGON = 0x0324
            META_POLYLINE = 0x0325
            META_ESCAPE = 0x0626
            META_RESTOREDC = 0x0127
            META_FILLREGION = 0x0228
            META_FRAMEREGION = 0x0429
            META_INVERTREGION = 0x012A
            META_PAINTREGION = 0x012B
            META_SELECTCLIPREGION = 0x012C
            META_SELECTOBJECT = 0x012D
            META_SETTEXTALIGN = 0x012E
            META_CHORD = 0x0830
            META_SETMAPPERFLAGS = 0x0231
            META_EXTTEXTOUT = 0x0a32
            META_SETDIBTODEV = 0x0d33
            META_SELECTPALETTE = 0x0234
            META_REALIZEPALETTE = 0x0035
            META_ANIMATEPALETTE = 0x0436
            META_SETPALENTRIES = 0x0037
            META_POLYPOLYGON = 0x0538
            META_RESIZEPALETTE = 0x0139
            META_DIBBITBLT = 0x0940
            META_DIBSTRETCHBLT = 0x0b41
            META_DIBCREATEPATTERNBRUSH = 0x0142
            META_STRETCHDIB = 0x0f43
            META_EXTFLOODFILL = 0x0548
            META_SETLAYOUT = 0x0149
            META_DELETEOBJECT = 0x01f0
            META_CREATEPALETTE = 0x00f7
            META_CREATEPATTERNBRUSH = 0x01F9
            META_CREATEPENINDIRECT = 0x02FA
            META_CREATEFONTINDIRECT = 0x02FB
            META_CREATEBRUSHINDIRECT = 0x02FC
            META_CREATEREGION = 0x06FF

            # REGION *** Desktop Family ***

            class _DRAWPATRECT(CStructure):
                _fields_ = [
                    ("ptPosition", POINT),
                    ("ptSize", POINT),
                    ("wStyle", WORD),
                    ("wPattern", WORD)
                ]
            DRAWPATRECT = _DRAWPATRECT
            PDRAWPATRECT = POINTER(DRAWPATRECT)

            # REGION ***
        # NOMETAFILE
        # GDI Escapes
        NEWFRAME = 1
        ABORTDOC = 2
        NEXTBAND = 3
        SETCOLORTABLE = 4
        GETCOLORTABLE = 5
        FLUSHOUTPUT = 6
        DRAFTMODE = 7
        QUERYESCSUPPORT = 8
        SETABORTPROC = 9
        STARTDOC = 10
        ENDDOC = 11
        GETPHYSPAGESIZE = 12
        GETPRINTINGOFFSET = 13
        GETSCALINGFACTOR = 14
        MFCOMMENT = 15
        GETPENWIDTH = 16
        SETCOPYCOUNT = 17
        SELECTPAPERSOURCE = 18
        DEVICEDATA = 19
        PASSTHROUGH = 19
        GETTECHNOLGY = 20
        GETTECHNOLOGY = 20
        SETLINECAP = 21
        SETLINEJOIN = 22
        SETMITERLIMIT = 23
        BANDINFO = 24
        DRAWPATTERNRECT = 25
        GETVECTORPENSIZE = 26
        GETVECTORBRUSHSIZE = 27
        ENABLEDUPLEX = 28
        GETSETPAPERBINS = 29
        GETSETPRINTORIENT = 30
        ENUMPAPERBINS = 31
        SETDIBSCALING = 32
        EPSPRINTING = 33
        ENUMPAPERMETRICS = 34
        GETSETPAPERMETRICS = 35
        POSTSCRIPT_DATA = 37
        POSTSCRIPT_IGNORE = 38
        MOUSETRAILS = 39
        GETDEVICEUNITS = 42
        GETEXTENDEDTEXTMETRICS = 256
        GETEXTENTTABLE = 257
        GETPAIRKERNTABLE = 258
        GETTRACKKERNTABLE = 259
        EXTTEXTOUT = 512
        GETFACENAME = 513
        DOWNLOADFACE = 514
        ENABLERELATIVEWIDTHS = 768
        ENABLEPAIRKERNING = 769
        SETKERNTRACK = 770
        SETALLJUSTVALUES = 771
        SETCHARSET = 772
        STRETCHBLT = 2048
        METAFILE_DRIVER = 2049
        GETSETSCREENPARAMS = 3072
        QUERYDIBSUPPORT = 3073
        BEGIN_PATH = 4096
        CLIP_TO_PATH = 4097
        END_PATH = 4098
        EXT_DEVICE_CAPS = 4099
        RESTORE_CTM = 4100
        SAVE_CTM = 4101
        SET_ARC_DIRECTION = 4102
        SET_BACKGROUND_COLOR = 4103
        SET_POLY_MODE = 4104
        SET_SCREEN_ANGLE = 4105
        SET_SPREAD = 4106
        TRANSFORM_CTM = 4107
        SET_CLIP_BOX = 4108
        SET_BOUNDS = 4109
        SET_MIRROR_MODE = 4110
        OPENCHANNEL = 4110
        DOWNLOADHEADER = 4111
        CLOSECHANNEL = 4112
        POSTSCRIPT_PASSTHROUGH = 4115
        ENCAPSULATED_POSTSCRIPT = 4116
        POSTSCRIPT_IDENTIFY = 4117 # new escape for NT5 pscript driver
        POSTSCRIPT_INJECTION = 4118 # new escape for NT5 pscript driver
        CHECKJPEGFORMAT = 4119
        CHECKPNGFORMAT = 4120
        GET_PS_FEATURESETTING = 4121 # new escape for NT5 pscript driver
        GDIPLUS_TS_QUERYVER = 4122 # private escape
        GDIPLUS_TS_RECORD = 4123 # private escape

        """

        * Return Values for MILCORE_TS_QUERYVER

        """

        MILCORE_TS_QUERYVER_RESULT_FALSE = 0x0
        MILCORE_TS_QUERYVER_RESULT_TRUE = 0x7FFFFFFF
        SPCLPASSTHROUGH2 = 4568 # new escape for NT5 pscript driver

        """

        * Parameters for POSTSCRIPT_IDENTIFY escape

        """

        PSIDENT_GDICENTRIC = 0
        PSIDENT_PSCENTRIC = 1

        # REGION *** Desktop Family ***


        """

        * Header structure for the input buffer to POSTSCRIPT_INJECTION escape

        """

        class _PSINJECTDATA(CStructure):
            _fields_ = [
                ("DataBytes", DWORD), # number of raw data bytes (NOT including this header)
                ("InjectionPoint", WORD), # injection point
                ("PageNumber", WORD) # page number to apply the injection
            ]

            # Followed by raw data to be injected

        PSINJECTDATA = _PSINJECTDATA
        PPSINJECTDATA = POINTER(PSINJECTDATA)

        """

        * Constants for PSINJECTDATA.InjectionPoint field

        """

        PSINJECT_BEGINSTREAM = 1
        PSINJECT_PSADOBE = 2
        PSINJECT_PAGESATEND = 3
        PSINJECT_PAGES = 4
        PSINJECT_DOCNEEDEDRES = 5
        PSINJECT_DOCSUPPLIEDRES = 6
        PSINJECT_PAGEORDER = 7
        PSINJECT_ORIENTATION = 8
        PSINJECT_BOUNDINGBOX = 9
        PSINJECT_DOCUMENTPROCESSCOLORS = 10
        PSINJECT_COMMENTS = 11
        PSINJECT_BEGINDEFAULTS = 12
        PSINJECT_ENDDEFAULTS = 13
        PSINJECT_BEGINPROLOG = 14
        PSINJECT_ENDPROLOG = 15
        PSINJECT_BEGINSETUP = 16
        PSINJECT_ENDSETUP = 17
        PSINJECT_TRAILER = 18
        PSINJECT_EOF = 19
        PSINJECT_ENDSTREAM = 20
        PSINJECT_DOCUMENTPROCESSCOLORSATEND = 21
        PSINJECT_PAGENUMBER = 100
        PSINJECT_BEGINPAGESETUP = 101
        PSINJECT_ENDPAGESETUP = 102
        PSINJECT_PAGETRAILER = 103
        PSINJECT_PLATECOLOR = 104
        PSINJECT_SHOWPAGE = 105
        PSINJECT_PAGEBBOX = 106
        PSINJECT_ENDPAGECOMMENTS = 107
        PSINJECT_VMSAVE = 200
        PSINJECT_VMRESTORE = 201

        """

        * InjectionPoint for publisher mode PScript5 OEM plugin to
        * generate DSC comment for included font resource

        """

        PSINJECT_DLFONT = 0xdddddddd

        """

        * Parameter for GET_PS_FEATURESETTING escape

        """

        FEATURESETTING_NUP = 0
        FEATURESETTING_OUTPUT = 1
        FEATURESETTING_PSLEVEL = 2
        FEATURESETTING_CUSTPAPER = 3
        FEATURESETTING_MIRROR = 4
        FEATURESETTING_NEGATIVE = 5
        FEATURESETTING_PROTOCOL = 6
        #
        # The range of selectors between FEATURESETTING_PRIVATE_BEGIN and
        # FEATURESETTING_PRIVATE_END is reserved by Microsoft for private use
        #
        FEATURESETTING_PRIVATE_BEGIN = 0x1000
        FEATURESETTING_PRIVATE_END = 0x1FFF

        # REGION *** Desktop Family ***


        """

        * Information about output options

        """

        class _PSFEATURE_OUTPUT(CStructure):
            _fields_ = [
                ("bPageIndependent", BOOL),
                ("bSetPageDevice", BOOL)
            ]
        PSFEATURE_OUTPUT = _PSFEATURE_OUTPUT
        PPSFEATURE_OUTPUT = POINTER(PSFEATURE_OUTPUT)

        """
        * Information about custom paper size
        """

        class _PSFEATURE_CUSTPAPER(CStructure):
            _fields_ = [
                ("lOrientation", LONG),
                ("lWidth", LONG),
                ("lHeight", LONG),
                ("lWidthOffset", LONG),
                ("lHeightOffset", LONG)
            ]
        PSFEATURE_CUSTPAPER = _PSFEATURE_CUSTPAPER
        PPSFEATURE_CUSTPAPER = POINTER(PSFEATURE_CUSTPAPER)

        # REGION ***
        # Value returned for FEATURESETTING_PROTOCOL
        PSPROTOCOL_ASCII = 0
        PSPROTOCOL_BCP = 1
        PSPROTOCOL_TBCP = 2
        PSPROTOCOL_BINARY = 3
        # Flag returned from QUERYDIBSUPPORT
        QDI_SETDIBITS = 1
        QDI_GETDIBITS = 2
        QDI_DIBTOSCREEN = 4
        QDI_STRETCHDIB = 8
        # Spooler Error Codes
        SP_NOTREPORTED = 0x4000
        SP_ERROR = (-1)
        SP_APPABORT = (-2)
        SP_USERABORT = (-3)
        SP_OUTOFDISK = (-4)
        SP_OUTOFMEMORY = (-5)
        PR_JOBSTATUS = 0x0000
        # Object Definitions for EnumObjects()
        OBJ_PEN = 1
        OBJ_BRUSH = 2
        OBJ_DC = 3
        OBJ_METADC = 4
        OBJ_PAL = 5
        OBJ_FONT = 6
        OBJ_BITMAP = 7
        OBJ_REGION = 8
        OBJ_METAFILE = 9
        OBJ_MEMDC = 10
        OBJ_EXTPEN = 11
        OBJ_ENHMETADC = 12
        OBJ_ENHMETAFILE = 13
        OBJ_COLORSPACE = 14
        GDI_OBJ_LAST = OBJ_COLORSPACE
        # xform stuff
        MWT_IDENTITY = 1
        MWT_LEFTMULTIPLY = 2
        MWT_RIGHTMULTIPLY = 3
        MWT_MIN = MWT_IDENTITY
        MWT_MAX = MWT_RIGHTMULTIPLY
        cpreproc.define("_XFORM_")

        # REGION *** Application Family ***

        class tagXFORM(CStructure):
            _fields_ = [
                ("eM11", FLOAT),
                ("eM12", FLOAT),
                ("eM21", FLOAT),
                ("eM22", FLOAT),
                ("eDx", FLOAT),
                ("eDy", FLOAT)
            ]
        XFORM = tagXFORM
        PXFORM = POINTER(XFORM)
        LPXFORM = PXFORM

        # Bitmap Header Definition
        class tagBITMAP(CStructure):
            _fields_ = [
                ("bmType", LONG),
                ("bmWidth", LONG),
                ("bmHeight", LONG),
                ("bmWidthBytes", LONG),
                ("bmPlanes", WORD),
                ("bmBitsPixel", WORD),
                ("bmBits", LPVOID)
            ]
        BITMAP = tagBITMAP
        PBITMAP = POINTER(BITMAP)
        NPBITMAP = PBITMAP
        LPBITMAP = PBITMAP

        # REGION ****

        # REGION *** Application Family ***

        class tagRGBTRIPLE(CStructure):
            _pack_ = 1
            _fields_ = [
                ("rgbtBlue", BYTE),
                ("rgbtGreen", BYTE),
                ("rgbtRed", BYTE)
            ]
        RGBTRIPLE = tagRGBTRIPLE
        PRGBTRIPLE = POINTER(RGBTRIPLE)
        NPRGBTRIPLE = PRGBTRIPLE
        LPRGBTRIPLE = PRGBTRIPLE

        # REGION ***

        # REGION *** Application Family ***

        class tagRGBQUAD(CStructure):
            _fields_ = [
                ("rgbBlue", BYTE),
                ("rgbGreen", BYTE),
                ("rgbRed", BYTE),
                ("rgbReserved", BYTE)
            ]
        RGBQUAD = tagRGBQUAD

        # REGION ***

        # REGION *** Desktop Family ***

        LPRGBQUAD = POINTER(RGBQUAD)
        PRGBQUAD = LPRGBQUAD

        # REGION ***

        # Image Color Matching color definitions
        CS_ENABLE = 0x00000001
        CS_DISABLE = 0x00000002
        CS_DELETE_TRANSFORM = 0x00000003
        # Logcolorspace signature
        LCS_SIGNATURE = 'PSOC'
        # Logcolorspace lcsType values
        LCS_sRGB = 'sRGB'
        LCS_WINDOWS_COLOR_SPACE = 'Win ' # Windows default color space

        # REGION *** Application Family ***

        LCSCSTYPE = LONG

        LCS_CALIBRATED_RGB = 0x00000000

        LCSGAMUTMATCH = LONG

        LCS_GM_BUSINESS = 0x00000001
        LCS_GM_GRAPHICS = 0x00000002
        LCS_GM_IMAGES = 0x00000004
        LCS_GM_ABS_COLORIMETRIC = 0x00000008
        # ICM Defines for results from CheckColorInGamut()
        CM_OUT_OF_GAMUT = 255
        CM_IN_GAMUT = 0
        # UpdateICMRegKey Constants
        ICM_ADDPROFILE = 1
        ICM_DELETEPROFILE = 2
        ICM_QUERYPROFILE = 3
        ICM_SETDEFAULTPROFILE = 4
        ICM_REGISTERICMATCHER = 5
        ICM_UNREGISTERICMATCHER = 6
        ICM_QUERYMATCH = 7
        # Macros to retrieve CMYK values from a COLORREF
        GetKValue = lambda cmyk: BYTE(cmyk).value
        GetYValue = lambda cmyk: BYTE(cmyk>> 8).value
        GetMValue = lambda cmyk: BYTE(cmyk>>16).value
        GetCValue = lambda cmyk: BYTE(cmyk>>24).value

        CMYK = lambda c, m, y, k: COLORREF(((BYTE(k).value | (BYTE(y).value << 8)) | (DWORD(BYTE(m).value).value << 16)) | (DWORD(BYTE(c).value).value << 24)).value
        
        FXPT16DOT16 = LONG
        LPFXPT16DOT16 = PLONG
        FXPT2DOT30 = LONG
        LPFXPT2DOT30 = PLONG
        # ICM Color Definitions
        # The following two structures are used for defining RGB's in terms of CIEXYZ.

        class tagCIEXYZ(CStructure):
            _fields_ = [
                ("ciexyzX", FXPT2DOT30),
                ("ciexyzY", FXPT2DOT30),
                ("ciexyzZ", FXPT2DOT30)
            ]
        CIEXYZ = tagCIEXYZ

        # REGION ***

        # REGION *** Desktop Family ***

        LPCIEXYZ = POINTER(tagCIEXYZ)

        # REGION ***

        # REGION *** Application Family ***

        class tagICEXYZTRIPLE(CStructure):
            _fields_ = [
                ("ciexyzRed", CIEXYZ),
                ("ciexyzGreen", CIEXYZ),
                ("ciexyzBlue", CIEXYZ)
            ]
        CIEXYZTRIPLE = tagICEXYZTRIPLE

        # REGION ***

        # REGION *** Application Family ***

        class tagLOGCOLORSPACEA(CStructure):
            _fields_ = [
                ("lcsSignature", DWORD),
                ("lcsVersion", DWORD),
                ("lcsSize", DWORD),
                ("lcsCSType", LCSCSTYPE),
                ("lcsIntent", LCSGAMUTMATCH),
                ("lcsEndpoints", CIEXYZTRIPLE),
                ("lcsGammaRed", DWORD),
                ("lcsGammaGreen", DWORD),
                ("lcsGammaBlue", DWORD),
                ("lcsFilename", CHAR * MAX_PATH)
            ]
        LOGCOLORSPACEA = tagLOGCOLORSPACEA
        LPLOGCOLORSPACEA = POINTER(LOGCOLORSPACEA)

        class tagLOGCOLORSPACEW(CStructure):
            _fields_ = [
                ("lcsSignature", DWORD),
                ("lcsVersion", DWORD),
                ("lcsSize", DWORD),
                ("lcsCSType", LCSCSTYPE),
                ("lcsIntent", LCSGAMUTMATCH),
                ("lcsEndpoints", CIEXYZTRIPLE),
                ("lcsGammaRed", DWORD),
                ("lcsGammaGreen", DWORD),
                ("lcsGammaBlue", DWORD),
                ("lcsFilename", WCHAR * MAX_PATH)
            ]
        LOGCOLORSPACEW = tagLOGCOLORSPACEW
        LPLOGCOLORSPACEW = POINTER(LOGCOLORSPACEW)

        # REGION ***

        # REGION *** Desktop Family ***

        LPCIEXYZTRIPLE = POINTER(CIEXYZTRIPLE)

        # REGION ***

        # REGION *** Desktop Family ***

        # structures for defining DIBs
        class tagBITMAPCOREHEADER(CStructure):
            _fields_ = [
                ("bcSize", DWORD), # used to get to color table
                ("bcWidth", WORD),
                ("bcHeight", WORD),
                ("bcPlanes", WORD),
                ("bcBitCount", WORD)
            ]
        BITMAPCOREHEADER = tagBITMAPCOREHEADER
        LPBITMAPCOREHEADER = POINTER(BITMAPCOREHEADER)
        PBITMAPCOREHEADER = LPBITMAPCOREHEADER

        # REGION ***

        # REGION *** Application Family or OneCore Family or Games Family ***

        class tagBITMAPINFOHEADER(CStructure):
            _fields_ = [
                ("biSize", DWORD),
                ("biWidth", LONG),
                ("biHeight", LONG),
                ("biPlanes", WORD),
                ("biBitCount", WORD),
                ("biCompression", DWORD),
                ("biSizeImage", DWORD),
                ("biXPelsPerMeter", LONG),
                ("biYPelsPerMeter", LONG),
                ("biClrUsed", DWORD),
                ("biClrImportant", DWORD)
            ]
        BITMAPINFOHEADER = tagBITMAPINFOHEADER
        LPBITMAPINFOHEADER = POINTER(BITMAPINFOHEADER)
        PBITMAPINFOHEADER = LPBITMAPINFOHEADER

        # REGION ***

        # REGION *** Desktop Family ***

        
        class BITMAPV4HEADER(CStructure):
            _fields_ = [
                ("bV4Size", DWORD),
                ("bV4Width", LONG),
                ("bV4Height", LONG),
                ("bV4Planes", WORD),
                ("bV4BitCount", WORD),
                ("bV4V4Compression", DWORD),
                ("bV4SizeImage", DWORD),
                ("bV4XPelsPerMeter", LONG),
                ("bV4YPelsPerMeter", LONG),
                ("bV4ClrUsed", DWORD),
                ("bV4ClrImportant", DWORD),
                ("bV4RedMask", DWORD),
                ("bV4GreenMask", DWORD),
                ("bV4BlueMask", DWORD),
                ("bV4AlphaMask", DWORD),
                ("bV4CSType", DWORD),
                ("bV4Endpoints", CIEXYZTRIPLE),
                ("bV4GammaRed", DWORD),
                ("bV4GammaGreen", DWORD),
                ("bV4GammaBlue", DWORD)
            ]
        LPBITMAPV4HEADER = POINTER(BITMAPV4HEADER)
        PBITMAPV4HEADER = LPBITMAPV4HEADER

        class BITMAPV5HEADER(CStructure):
            _fields_ = [
                ("bV5Size", DWORD),
                ("bV5Width", LONG),
                ("bV5Height", LONG),
                ("bV5Planes", WORD),
                ("bV5BitCount", WORD),
                ("bV5Compression", DWORD),
                ("bV5SizeImage", DWORD),
                ("bV5XPelsPerMeter", LONG),
                ("bV5YPelsPerMeter", LONG),
                ("bV5ClrUsed", DWORD),
                ("bV5ClrImportant", DWORD),
                ("bV5RedMask", DWORD),
                ("bV5GreenMask", DWORD),
                ("bV5BlueMask", DWORD),
                ("bV5AlphaMask", DWORD),
                ("bV5CSType", DWORD),
                ("bV5Endpoints", CIEXYZTRIPLE),
                ("bV5GammaRed", DWORD),
                ("bV5GammaGreen", DWORD),
                ("bV5GammaBlue", DWORD),
                ("bV5Intent", DWORD),
                ("bV5ProfileData", DWORD),
                ("bV5ProfileSize", DWORD),
                ("bV5Reserved", DWORD)
            ]
        LPBITMAPV5HEADER = POINTER(BITMAPV5HEADER)
        PBITMAPV5HEADER = LPBITMAPV5HEADER

        # REGION ***

        # Values for bV5CSType
        PROFILE_LINKED = 'LINK'
        PROFILE_EMBEDDED = 'MBED'
        # constants for the biCompression field
        BI_RGB = 0
        BI_RLE8 = 1
        BI_RLE4 = 2
        BI_BITFIELDS = 3
        BI_JPEG = 4
        BI_PNG = 5

        # REGION *** Application Family ***

        class tagBITMAPINFO(CStructure):
            _fields_ = [
                ("bmiHeader", BITMAPINFOHEADER),
                ("bmiColors", RGBQUAD * 1)
            ]
        BITMAPINFO = tagBITMAPINFO
        LPBITMAPINFO = POINTER(BITMAPINFO)
        PBITMAPINFO = LPBITMAPINFO

        # REGION ***

        # REGION *** Desktop Family ***

        class tagBITMAPCOREINFO(CStructure):
            _fields_ = [
                ("bmciHeader", BITMAPCOREHEADER),
                ("bmciColors", RGBTRIPLE * 1)
            ]
        BITMAPCOREINFO = tagBITMAPCOREINFO
        LPBITMAPCOREINFO = POINTER(BITMAPCOREINFO)
        PBITMAPCOREINFO = LPBITMAPCOREINFO

        class tagBITMAPFILEHEADER(CStructure):
            _pack_ = 2
            _fields_ = [
                ("bfType", WORD),
                ("bfSize", DWORD),
                ("bfReserved1", WORD),
                ("bfReserved2", WORD),
                ("bfOffBits", DWORD)
            ]
        BITMAPFILEHEADER = tagBITMAPFILEHEADER
        LPBITMAPFILEHEADER = POINTER(BITMAPFILEHEADER)
        PBITMAPFILEHEADER = LPBITMAPFILEHEADER

        # REGION ***

        MAKEPOINTS = lambda l: cast(addressof(INT(l)), PPOINTS).contents

        # REGION *** Application Family ***

        class tagFONTSIGNATURE(CStructure):
            _fields_ = [
                ("fsUsb", DWORD * 4),
                ("fsCsb", DWORD * 2)
            ]
        FONTSIGNATURE = tagFONTSIGNATURE
        PFONTSIGNATURE = POINTER(FONTSIGNATURE)
        LPFONTSIGNATURE = PFONTSIGNATURE

        # REGION ***

        # REGION *** Desktop Family ***

        class tagCHARSETINFO(CStructure):
            _fields_  = [
                ("ciCharset", UINT),
                ("ciACP", UINT),
                ("fs", FONTSIGNATURE)
            ]
        CHARSETINFO = tagCHARSETINFO
        NPCHARSETINFO = POINTER(CHARSETINFO)
        LPCHARSETINFO = NPCHARSETINFO

        # REGION ***
        TCI_SRCCHARSET = 1
        TCI_SRCCODEPAGE = 2
        TCI_SRCFONTSIG = 3
        TCI_SRCLOCALE = 0x1000

        # REGION *** Application Family ***

        class tagLOCALESIGNATURE(CStructure):
            _fields_ = [
                ("lsUsb", DWORD * 4),
                ("lsCsbDefault", DWORD * 2),
                ("lsCsbSupported", DWORD * 2)
            ]
        LOCALESIGNATURE = tagLOCALESIGNATURE
        PLOCALESIGNATURE = POINTER(LOCALESIGNATURE)
        LPLOCALESIGNATURE = PLOCALESIGNATURE

        # REGION ***

        if cpreproc.ifndef("NOMETAFILE"):

            # REGION *** Application Family ***

            # Clipboard Metafile Picture Structure

            class tagHANDLETABLE(CStructure):
                _fields_ = [
                    ("objectHandle", HGDIOBJ * 1)
                ]
            HANDLETABLE = tagHANDLETABLE
            PHANDLETABLE = POINTER(HANDLETABLE)
            LPHANDLETABLE = PHANDLETABLE

            class tagMETARECORD(CStructure):
                _fields_ = [
                    ("rdSize", DWORD),
                    ("rdFunction", WORD),
                    ("rdParm", WORD * 1)
                ]
            METARECORD = tagMETARECORD

            # REGION ***

            # REGION *** Desktop Family ***

            PMETARECORD = POINTER(METARECORD)

            # REGION ***

            # REGION *** Application Family ***

            LPMETARECORD = PMETARECORD

            class tagMETAFILEPICT(CStructure):
                _fields_ = [
                    ("mm", LONG),
                    ("xExt", LONG),
                    ("yExt", LONG),
                    ("hMF", HMETAFILE)
                ]
            METAFILEPICT = tagMETAFILEPICT
            PMETAFILEPICT = POINTER(METAFILEPICT)
            LPMETAFILEPICT = PMETAFILEPICT

            # REGION ***

            # REGION *** Desktop Family ***

            class tagMETAHEADER(CStructure):
                _fields_ = [
                    ("mtType", WORD),
                    ("mtHeaderSize", WORD),
                    ("mtVersion", DWORD),
                    ("mtNoObjects", WORD),
                    ("mtMaxRecord", DWORD),
                    ("mtNoParameters", WORD)
                ]
            METAHEADER = tagMETAHEADER
            PMETAHEADER = POINTER(METAHEADER)
            LPMETAHEADER = PMETAHEADER

            # REGION ***

            # REGION *** Application Family ***

            # Enhanced Metafile structures 
            class tagENHMETARECORD(CStructure):
                _fields_ = [
                    ("iType", DWORD), # Record type EMR_XXX
                    ("nSize", DWORD), # Record size in bytes
                    ("dParm", DWORD * 1) # Parameters
                ]
            ENHMETARECORD = tagENHMETARECORD
            PENHMETARECORD = POINTER(ENHMETARECORD)
            LPENHMETARECORD = PENHMETARECORD

            class tagENHMETAHEADER(CStructure):
                _fields_ = [
                    ("iType", DWORD),          # Record typeEMR_HEADER
                    ("nSize", DWORD),          # Record size in bytes.  This may be greater
                                               # than the sizeof(ENHMETAHEADER).
                    ("rclBounds", RECTL),      # Inclusive-inclusive bounds in device units
                    ("rclFrame", RECTL),       # Inclusive-inclusive Picture Frame of metafile in .01 mm units
                    ("dSignature", DWORD),     # Signature.  Must be ENHMETA_SIGNATURE.
                    ("nVersion", DWORD),       # Version number
                    ("nBytes", DWORD),         # Size of the metafile in bytes
                    ("nRecords", DWORD),       # Number of records in the metafile
                    ("nHandles", WORD),        # Number of handles in the handle table
                                               # Handle index zero is reserved.
                    ("sReserved", WORD),       # Reserved.  Must be zero.
                    ("nDescription", DWORD),   # Number of chars in the unicode description string
                                               # This is 0 if there is no description string
                    ("offDescription", DWORD), # Offset to the metafile description record.
                                               # This is 0 if there is no description string
                    ("nPalEntries", DWORD),    # Number of entries in the metafile palette.
                    ("szlDevice", SIZEL),      # Size of the reference device in pels
                    ("szlMillimeters", SIZEL), # Size of the reference device in millimeters
                    ("cbPixelFormat", DWORD),  # Size of PIXELFORMATDESCRIPTOR information
                                               # This is 0 if no pixel format is set
                    ("offPixelFormat", DWORD), # Offset to PIXELFORMATDESCRIPTOR
                                               # This is 0 if no pixel format is set
                    ("bOpenGL", DWORD),        # TRUE if OpenGL commands are present in
                                               # the metafile, otherwise FALSE
                    ("szlMicrometers", SIZEL), # Size of the reference device in micrometers
                ]
            ENHMETAHEADER = tagENHMETAHEADER
            PENHMETAHEADER = POINTER(ENHMETAHEADER)
            LPENHMETAHEADER = PENHMETAHEADER

            # REGION ***

        # NOMETAFILE
        if cpreproc.ifndef("NOTEXTMETRIC"):
            # tmPitchAndFamily flags
            TMPF_FIXED_PITCH = 0x01
            TMPF_VECTOR = 0x02
            TMPF_DEVICE = 0x08
            TMPF_TRUETYPE = 0x04

            # REGION *** Desktop Family ***

            #
            # BCHAR definition for APPs
            #
            BCHAR = unicode(WCHAR, CHAR)

            # REGION ***
            if cpreproc.pragma_once("_TEXTMETRIC_DEFINED"):
                # REGION *** Application Family ***

                class tagTEXTMETRICA(CStructure):
                    _fields_ = [
                        ("tmHeight", LONG),
                        ("tmAscent", LONG),
                        ("tmDescent", LONG),
                        ("tmInternalLeading", LONG),
                        ("tmExternalLeading", LONG),
                        ("tmAveCharWidth", LONG),
                        ("tmMaxCharWidth", LONG),
                        ("tmWeight", LONG),
                        ("tmOverhang", LONG),
                        ("tmDigitizedAspectX", LONG),
                        ("tmDigitizedAspectY", LONG),
                        ("tmFirstChar", CHAR),
                        ("tmLastChar", CHAR),
                        ("tmDefaultChar", CHAR),
                        ("tmBreakChar", CHAR),
                        ("tmItalic", BYTE),
                        ("tmUnderlined", BYTE),
                        ("tmStruckOut", BYTE),
                        ("tmPitchAndFamily", BYTE),
                        ("tmCharSet", BYTE)
                    ]
                TEXTMETRICA = tagTEXTMETRICA
                PTEXTMETRICA = TEXTMETRICA
                NPTEXTMETRICA = PTEXTMETRICA
                LPTEXTMETRICA = PTEXTMETRICA

                class tagTEXTMETRICW(CStructure):
                    _pack_ = 4
                    _fields_ = [
                        ("tmHeight", LONG),
                        ("tmAscent", LONG),
                        ("tmDescent", LONG),
                        ("tmInternalLeading", LONG),
                        ("tmExternalLeading", LONG),
                        ("tmAveCharWidth", LONG),
                        ("tmMaxCharWidth", LONG),
                        ("tmWeight", LONG),
                        ("tmOverhang", LONG),
                        ("tmDigitizedAspectX", LONG),
                        ("tmDigitizedAspectY", LONG),
                        ("tmFirstChar", WCHAR),
                        ("tmLastChar", WCHAR),
                        ("tmDefaultChar", WCHAR),
                        ("tmBreakChar", WCHAR),
                        ("tmItalic", BYTE),
                        ("tmUnderlined", BYTE),
                        ("tmStruckOut", BYTE),
                        ("tmPitchAndFamily", BYTE),
                        ("tmCharSet", BYTE)
                    ]
                TEXTMETRICW = tagTEXTMETRICW
                PTEXTMETRICW = TEXTMETRICW
                NPTEXTMETRICW = PTEXTMETRICW
                LPTEXTMETRICW = PTEXTMETRICW

                TEXTMETRIC = unicode(TEXTMETRICW, TEXTMETRICA)
                PTEXTMETRIC = unicode(PTEXTMETRICW, PTEXTMETRICA)
                NPTEXTMETRIC = unicode(NPTEXTMETRICW, NPTEXTMETRICA)
                LPTEXTMETRIC = unicode(LPTEXTMETRICW, LPTEXTMETRICA)
            # !_TEXTMETRIC_DEFINED
            # ntmFlags field flags
            NTM_REGULAR = 0x00000040
            NTM_BOLD = 0x00000020
            NTM_ITALIC = 0x00000001
            # new in NT 5.0
            NTM_NONNEGATIVE_AC = 0x00010000
            NTM_PS_OPENTYPE = 0x00020000
            NTM_TT_OPENTYPE = 0x00040000
            NTM_MULTIPLEMASTER = 0x00080000
            NTM_TYPE1 = 0x00100000
            NTM_DSIG = 0x00200000

            # REGION *** Desktop Family ***

            class tagNEWTEXTMETRICA(CStructure):
                _fields_ = [
                    ("tmHeight", LONG),
                    ("tmAscent", LONG),
                    ("tmDescent", LONG),
                    ("tmInternalLeading", LONG),
                    ("tmExternalLeading", LONG),
                    ("tmAveCharWidth", LONG),
                    ("tmMaxCharWidth", LONG),
                    ("tmWeight", LONG),
                    ("tmOverhang", LONG),
                    ("tmDigitizedAspectX", LONG),
                    ("tmDigitizedAspectY", LONG),
                    ("tmFirstChar", CHAR),
                    ("tmLastChar", CHAR),
                    ("tmDefaultChar", CHAR),
                    ("tmBreakChar", CHAR),
                    ("tmItalic", BYTE),
                    ("tmUnderlined", BYTE),
                    ("tmStruckOut", BYTE),
                    ("tmPitchAndFamily", BYTE),
                    ("tmCharSet", BYTE),
                    ("ntmFlags", DWORD),
                    ("ntmSizeEM", UINT),
                    ("ntmCellHeight", UINT),
                    ("ntmAvgWidth", UINT)
                ]
            NEWTEXTMETRICA = tagNEWTEXTMETRICA
            PNEWTEXTMETRICA = NEWTEXTMETRICA
            NPNEWTEXTMETRICA = PNEWTEXTMETRICA
            LPNEWTEXTMETRICA = PNEWTEXTMETRICA

            class tagNEWTEXTMETRICW(CStructure):
                _pack_ = 4
                _fields_ = [
                    ("tmHeight", LONG),
                    ("tmAscent", LONG),
                    ("tmDescent", LONG),
                    ("tmInternalLeading", LONG),
                    ("tmExternalLeading", LONG),
                    ("tmAveCharWidth", LONG),
                    ("tmMaxCharWidth", LONG),
                    ("tmWeight", LONG),
                    ("tmOverhang", LONG),
                    ("tmDigitizedAspectX", LONG),
                    ("tmDigitizedAspectY", LONG),
                    ("tmFirstChar", WCHAR),
                    ("tmLastChar", WCHAR),
                    ("tmDefaultChar", WCHAR),
                    ("tmBreakChar", WCHAR),
                    ("tmItalic", BYTE),
                    ("tmUnderlined", BYTE),
                    ("tmStruckOut", BYTE),
                    ("tmPitchAndFamily", BYTE),
                    ("tmCharSet", BYTE),
                    ("ntmFlags", DWORD),
                    ("ntmSizeEM", UINT),
                    ("ntmCellHeight", UINT),
                    ("ntmAvgWidth", UINT)
                ]
            NEWTEXTMETRICW = tagNEWTEXTMETRICW
            PNEWTEXTMETRICW = NEWTEXTMETRICW
            NPNEWTEXTMETRICW = PNEWTEXTMETRICW
            LPNEWTEXTMETRICW = PNEWTEXTMETRICW

            NEWTEXTMETRIC = unicode(NEWTEXTMETRICW, NEWTEXTMETRICA)
            PNEWTEXTMETRIC = unicode(PNEWTEXTMETRICW, PNEWTEXTMETRICA)
            NPNEWTEXTMETRIC = unicode(NPNEWTEXTMETRICW, NPNEWTEXTMETRICA)
            LPNEWTEXTMETRIC = unicode(LPNEWTEXTMETRICW, LPNEWTEXTMETRICA)

            # REGION ***

            # REGION *** Desktop Family ***

            class tagNEWTEXTMETRICEXA(CStructure):
                _fields_ = [
                    ("ntmTm", NEWTEXTMETRICA),
                    ("ntmFontSig", FONTSIGNATURE)
                ]
            NEWTEXTMETRICEXA = tagNEWTEXTMETRICEXA

            class tagNEWTEXTMETRICEXW(CStructure):
                _fields_ = [
                    ("ntmTm", NEWTEXTMETRICW),
                    ("ntmFontSig", FONTSIGNATURE)
                ]
            NEWTEXTMETRICEXW = tagNEWTEXTMETRICEXW

            # REGION ***
        # !NOTEXTMETRIC
        
        # GDI Logical Objects:

        # Pel Array
        # REGION *** Desktop Family ***

        class tagPELARRAY(CStructure):
            _fields_ = [
                ("paXCount", LONG),
                ("paYCount", LONG),
                ("paXExt", LONG),
                ("paYExt", LONG),
                ("paRGBs", BYTE)
            ]
        PELARRAY = tagPELARRAY
        PPELARRAY = POINTER(PELARRAY)
        NPPELARRAY = PPELARRAY
        LPPELARRAY = PPELARRAY

        # REGION ***

        # REGION *** Application Family ***

        # Logical Brush (or Pattern)
        class tagLOGBRUSH(CStructure):
            _fields_ = [
                ("lbStyle", UINT),
                ("lbColor", COLORREF),
                ("lbHatch", ULONG_PTR)
            ]
        LOGBRUSH = tagLOGBRUSH
        PLOGBRUSH = POINTER(LOGBRUSH)
        NPLOGBRUSH = PLOGBRUSH
        LPLOGBRUSH = PLOGBRUSH

        class tagLOGBRUSH32(CStructure):
            _fields_ = [
                ("lbStyle", UINT),
                ("lbColor", COLORREF),
                ("lbHatch", ULONG)
            ]
        LOGBRUSH32 = tagLOGBRUSH32
        PLOGBRUSH32 = POINTER(LOGBRUSH32)
        NPLOGBRUSH32 = PLOGBRUSH32

        # REGION ***

        # REGION *** Desktop Family ***

        PATTERN = LOGBRUSH
        PPATTERN = PLOGBRUSH
        NPPATTERN = NPLOGBRUSH
        LPPATTERN = LPLOGBRUSH

        # REGION ***

        # REGION *** Application Family ***

        # Logical Pen
        class tagLOGPEN(CStructure):
            _fields_ = [
                ("lopnStyle", UINT),
                ("lopnWidth", POINT),
                ("lopnColor", COLORREF)
            ]
        LOGPEN = tagLOGPEN
        PLOGPEN = POINTER(LOGPEN)
        NPLOGPEN = PLOGPEN
        LPLOGPEN = PLOGPEN

        # REGION ***

        # REGION *** Desktop Family ***

        class tagEXTLOGPEN(CStructure):
            _fields_ = [
                ("elpPenStyle", DWORD),
                ("elpWidth", DWORD),
                ("elpBrushStyle", UINT),
                ("elpColor", COLORREF),
                ("elpHatch", ULONG_PTR),
                ("elpNumEntries", DWORD),
                ("elpStyleEntry", DWORD * 1)
            ]
        EXTLOGPEN = tagEXTLOGPEN
        PEXTLOGPEN = POINTER(EXTLOGPEN)
        NPEXTLOGPEN = PEXTLOGPEN
        LPEXTLOGPEN = PEXTLOGPEN

        # REGION ***

        # REGION *** Application Family ***

        class tagEXTLOGPEN32(CStructure):
            _fields_ = [
                ("elpPenStyle", DWORD),
                ("elpWidth", DWORD),
                ("elpBrushStyle", UINT),
                ("elpColor", COLORREF),
                ("elpHatch", ULONG),
                ("elpNumEntries", DWORD),
                ("elpStyleEntry", DWORD * 1)
            ]
        EXTLOGPEN32 = tagEXTLOGPEN32
        PEXTLOGPEN32 = POINTER(EXTLOGPEN32)
        NPEXTLOGPEN32 = PEXTLOGPEN32
        LPEXTLOGPEN32 = PEXTLOGPEN32

        if cpreproc.pragma_once("_PALETTEENTRY_DEFINED"):
            class tagPALETTEENTRY(CStructure):
                _fields_ = [
                    ("peRed", BYTE),
                    ("peGreen", BYTE),
                    ("peBlue", BYTE),
                    ("peFlags", BYTE)
                ]
            PALETTEENTRY = tagPALETTEENTRY
            PPALETTEENTRY = POINTER(PALETTEENTRY)
            LPPALETTEENTRY = PPALETTEENTRY
        # !_PALETTEENTRY_DEFINED

        if cpreproc.pragma_once("_LOGPALETTE_DEFINED"):
            # Logical Palette
            class tagLOGPALETTE(CStructure):
                _fields_ = [
                    ("palVersion", WORD),
                    ("palNumEntries", WORD),
                    ("palPalEntry", PALETTEENTRY * 1)
                ]
            LOGPALETTE = tagLOGPALETTE
            PLOGPALETTE = POINTER(LOGPALETTE)
            NPLOGPALETTE = PLOGPALETTE
            LPLOGPALETTE = PLOGPALETTE
        # !_LOGPALETTE_DEFINED


        # Logical Font
        LF_FACESIZE = 32

        class tagLOGFONTA(CStructure):
            _fields_ = [
                ("lfHeight", LONG),
                ("lfWidth", LONG),
                ("lfEscapement", LONG),
                ("lfOrientation", LONG),
                ("lfWeight", LONG),
                ("lfItalic", BYTE),
                ("lfUnderline", BYTE),
                ("lfStrikeOut", BYTE),
                ("lfCharSet", BYTE),
                ("lfOutPrecision", BYTE),
                ("lfClipPrecision", BYTE),
                ("lfQuality", BYTE),
                ("lfPitchAndFamily", BYTE),
                ("lfFaceName", CHAR * LF_FACESIZE)
            ]
        LOGFONTA = tagLOGFONTA
        PLOGFONTA = POINTER(LOGFONTA)
        NPLOGFONTA = PLOGFONTA
        LPLOGFONTA = PLOGFONTA

        class tagLOGFONTW(CStructure):
            _fields_ = [
                ("lfHeight", LONG),
                ("lfWidth", LONG),
                ("lfEscapement", LONG),
                ("lfOrientation", LONG),
                ("lfWeight", LONG),
                ("lfItalic", BYTE),
                ("lfUnderline", BYTE),
                ("lfStrikeOut", BYTE),
                ("lfCharSet", BYTE),
                ("lfOutPrecision", BYTE),
                ("lfClipPrecision", BYTE),
                ("lfQuality", BYTE),
                ("lfPitchAndFamily", BYTE),
                ("lfFaceName", WCHAR * LF_FACESIZE)
            ]
        LOGFONTW = tagLOGFONTW
        PLOGFONTW = POINTER(LOGFONTW)
        NPLOGFONTW = PLOGFONTW
        LPLOGFONTW = PLOGFONTW

        LOGFONT = unicode(LOGFONTW, LOGFONTA)
        PLOGFONT = unicode(PLOGFONTW, PLOGFONTA)
        NPLOGFONT = unicode(NPLOGFONTW, NPLOGFONTA)
        LPLOGFONT = unicode(LPLOGFONTW, LPLOGFONTA)

        # REGION ***

        LF_FULLFACESIZE = 64

        # REGION *** Desktop Family ***

        # Structure passed to FONTENUMPROC
        class tagENUMLOGFONTA(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTA),
                ("elfFullName", CHAR * LF_FULLFACESIZE),
                ("elfStyle", CHAR * LF_FACESIZE)
            ]
        ENUMLOGFONTA = tagENUMLOGFONTA
        LPENUMLOGFONTA = POINTER(ENUMLOGFONTA)

        # Structure passed to FONTENUMPROC
        class tagENUMLOGFONTW(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTW),
                ("elfFullName", WCHAR * LF_FULLFACESIZE),
                ("elfStyle", WCHAR * LF_FACESIZE)
            ]
        ENUMLOGFONTW = tagENUMLOGFONTW
        LPENUMLOGFONTW = POINTER(ENUMLOGFONTW)

        ENUMLOGFONT = unicode(ENUMLOGFONTW, ENUMLOGFONTA)
        LPENUMLOGFONT = unicode(LPENUMLOGFONTW, LPENUMLOGFONTA)

        class tagENUMLOGFONTEXA(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTA),
                ("elfFullName", CHAR * LF_FULLFACESIZE),
                ("elfStyle", CHAR * LF_FACESIZE),
                ("elfScript", CHAR * LF_FACESIZE)
            ]
        ENUMLOGFONTEXA = tagENUMLOGFONTEXA
        LPENUMLOGFONTEXA = POINTER(ENUMLOGFONTEXA)

        class tagENUMLOGFONTEXW(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTW),
                ("elfFullName", WCHAR * LF_FULLFACESIZE),
                ("elfStyle", WCHAR * LF_FACESIZE),
                ("elfScript", WCHAR * LF_FACESIZE)
            ]
        ENUMLOGFONTEXW = tagENUMLOGFONTEXW
        LPENUMLOGFONTEXW = POINTER(ENUMLOGFONTEXW)

        ENUMLOGFONTEX = unicode(ENUMLOGFONTEXW, ENUMLOGFONTEXA)
        LPENUMLOGFONTEX = unicode(LPENUMLOGFONTEXW, LPENUMLOGFONTEXA)

        # REGION ***
        
        OUT_DEFAULT_PRECIS = 0
        OUT_STRING_PRECIS = 1
        OUT_CHARACTER_PRECIS = 2
        OUT_STROKE_PRECIS = 3
        OUT_TT_PRECIS = 4
        OUT_DEVICE_PRECIS = 5
        OUT_RASTER_PRECIS = 6
        OUT_TT_ONLY_PRECIS = 7
        OUT_OUTLINE_PRECIS = 8
        OUT_SCREEN_OUTLINE_PRECIS = 9
        OUT_PS_ONLY_PRECIS = 10
        CLIP_DEFAULT_PRECIS = 0
        CLIP_CHARACTER_PRECIS = 1
        CLIP_STROKE_PRECIS = 2
        CLIP_MASK = 0xf
        CLIP_LH_ANGLES = (1<<4)
        CLIP_TT_ALWAYS = (2<<4)
        CLIP_DFA_DISABLE = (4<<4)
        CLIP_EMBEDDED = (8<<4)
        DEFAULT_QUALITY = 0
        DRAFT_QUALITY = 1
        PROOF_QUALITY = 2
        NONANTIALIASED_QUALITY = 3
        ANTIALIASED_QUALITY = 4
        CLEARTYPE_QUALITY = 5
        CLEARTYPE_NATURAL_QUALITY = 6
        DEFAULT_PITCH = 0
        FIXED_PITCH = 1
        VARIABLE_PITCH = 2
        MONO_FONT = 8
        ANSI_CHARSET = 0
        DEFAULT_CHARSET = 1
        SYMBOL_CHARSET = 2
        SHIFTJIS_CHARSET = 128
        HANGEUL_CHARSET = 129
        HANGUL_CHARSET = 129
        GB2312_CHARSET = 134
        CHINESEBIG5_CHARSET = 136
        OEM_CHARSET = 255
        JOHAB_CHARSET = 130
        HEBREW_CHARSET = 177
        ARABIC_CHARSET = 178
        GREEK_CHARSET = 161
        TURKISH_CHARSET = 162
        VIETNAMESE_CHARSET = 163
        THAI_CHARSET = 222
        EASTEUROPE_CHARSET = 238
        RUSSIAN_CHARSET = 204
        MAC_CHARSET = 77
        BALTIC_CHARSET = 186
        FS_LATIN1 = 0x00000001
        FS_LATIN2 = 0x00000002
        FS_CYRILLIC = 0x00000004
        FS_GREEK = 0x00000008
        FS_TURKISH = 0x00000010
        FS_HEBREW = 0x00000020
        FS_ARABIC = 0x00000040
        FS_BALTIC = 0x00000080
        FS_VIETNAMESE = 0x00000100
        FS_THAI = 0x00010000
        FS_JISJAPAN = 0x00020000
        FS_CHINESESIMP = 0x00040000
        FS_WANSUNG = 0x00080000
        FS_CHINESETRAD = 0x00100000
        FS_JOHAB = 0x00200000
        FS_SYMBOL = 0x80000000
        # Font Families
        FF_DONTCARE = (0<<4) # Don't care or don't know.
        FF_ROMAN = (1<<4) # Variable stroke width, serifed.
        # Times Roman, Century Schoolbook, etc.
        FF_SWISS = (2<<4) # Variable stroke width, sans-serifed.
        # Helvetica, Swiss, etc.
        FF_MODERN = (3<<4) # Constant stroke width, serifed or sans-serifed.
        # Pica, Elite, Courier, etc.
        FF_SCRIPT = (4<<4) # Cursive, etc.
        FF_DECORATIVE = (5<<4) # Old English, etc.
        # Font Weights
        FW_DONTCARE = 0
        FW_THIN = 100
        FW_EXTRALIGHT = 200
        FW_LIGHT = 300
        FW_NORMAL = 400
        FW_MEDIUM = 500
        FW_SEMIBOLD = 600
        FW_BOLD = 700
        FW_EXTRABOLD = 800
        FW_HEAVY = 900
        FW_ULTRALIGHT = FW_EXTRALIGHT
        FW_REGULAR = FW_NORMAL
        FW_DEMIBOLD = FW_SEMIBOLD
        FW_ULTRABOLD = FW_EXTRABOLD
        FW_BLACK = FW_HEAVY
        PANOSE_COUNT = 10
        PAN_FAMILYTYPE_INDEX = 0
        PAN_SERIFSTYLE_INDEX = 1
        PAN_WEIGHT_INDEX = 2
        PAN_PROPORTION_INDEX = 3
        PAN_CONTRAST_INDEX = 4
        PAN_STROKEVARIATION_INDEX = 5
        PAN_ARMSTYLE_INDEX = 6
        PAN_LETTERFORM_INDEX = 7
        PAN_MIDLINE_INDEX = 8
        PAN_XHEIGHT_INDEX = 9
        PAN_CULTURE_LATIN = 0

        # REGION *** Application Family ***

        class tagPANOSE(CStructure):
            _fields_ = [
                ("bFamilyType", BYTE),
                ("bSerifStyle", BYTE),
                ("bWeight", BYTE),
                ("bProportion", BYTE),
                ("bContrast", BYTE),
                ("bStrokeVariation", BYTE),
                ("bArmStyle", BYTE),
                ("bLetterForm", BYTE),
                ("bMidline", BYTE),
                ("bXHeight", BYTE)
            ]
        PANOSE = tagPANOSE
        LPPANOSE = POINTER(PANOSE)

        PAN_ANY = 0 # Any
        PAN_NO_FIT = 1 # No Fit
        PAN_FAMILY_TEXT_DISPLAY = 2 # Text and Display
        PAN_FAMILY_SCRIPT = 3 # Script
        PAN_FAMILY_DECORATIVE = 4 # Decorative
        PAN_FAMILY_PICTORIAL = 5 # Pictorial
        PAN_SERIF_COVE = 2 # Cove
        PAN_SERIF_OBTUSE_COVE = 3 # Obtuse Cove
        PAN_SERIF_SQUARE_COVE = 4 # Square Cove
        PAN_SERIF_OBTUSE_SQUARE_COVE = 5 # Obtuse Square Cove
        PAN_SERIF_SQUARE = 6 # Square
        PAN_SERIF_THIN = 7 # Thin
        PAN_SERIF_BONE = 8 # Bone
        PAN_SERIF_EXAGGERATED = 9 # Exaggerated
        PAN_SERIF_TRIANGLE = 10 # Triangle
        PAN_SERIF_NORMAL_SANS = 11 # Normal Sans
        PAN_SERIF_OBTUSE_SANS = 12 # Obtuse Sans
        PAN_SERIF_PERP_SANS = 13 # Prep Sans
        PAN_SERIF_FLARED = 14 # Flared
        PAN_SERIF_ROUNDED = 15 # Rounded
        PAN_WEIGHT_VERY_LIGHT = 2 # Very Light
        PAN_WEIGHT_LIGHT = 3 # Light
        PAN_WEIGHT_THIN = 4 # Thin
        PAN_WEIGHT_BOOK = 5 # Book
        PAN_WEIGHT_MEDIUM = 6 # Medium
        PAN_WEIGHT_DEMI = 7 # Demi
        PAN_WEIGHT_BOLD = 8 # Bold
        PAN_WEIGHT_HEAVY = 9 # Heavy
        PAN_WEIGHT_BLACK = 10 # Black
        PAN_WEIGHT_NORD = 11 # Nord
        PAN_PROP_OLD_STYLE = 2 # Old Style
        PAN_PROP_MODERN = 3 # Modern
        PAN_PROP_EVEN_WIDTH = 4 # Even Width
        PAN_PROP_EXPANDED = 5 # Expanded
        PAN_PROP_CONDENSED = 6 # Condensed
        PAN_PROP_VERY_EXPANDED = 7 # Very Expanded
        PAN_PROP_VERY_CONDENSED = 8 # Very Condensed
        PAN_PROP_MONOSPACED = 9 # Monospaced
        PAN_CONTRAST_NONE = 2 # None
        PAN_CONTRAST_VERY_LOW = 3 # Very Low
        PAN_CONTRAST_LOW = 4 # Low
        PAN_CONTRAST_MEDIUM_LOW = 5 # Medium Low
        PAN_CONTRAST_MEDIUM = 6 # Medium
        PAN_CONTRAST_MEDIUM_HIGH = 7 # Mediim High
        PAN_CONTRAST_HIGH = 8 # High
        PAN_CONTRAST_VERY_HIGH = 9 # Very High
        PAN_STROKE_GRADUAL_DIAG = 2 # Gradual/Diagonal
        PAN_STROKE_GRADUAL_TRAN = 3 # Gradual/Transitional
        PAN_STROKE_GRADUAL_VERT = 4 # Gradual/Vertical
        PAN_STROKE_GRADUAL_HORZ = 5 # Gradual/Horizontal
        PAN_STROKE_RAPID_VERT = 6 # Rapid/Vertical
        PAN_STROKE_RAPID_HORZ = 7 # Rapid/Horizontal
        PAN_STROKE_INSTANT_VERT = 8 # Instant/Vertical
        PAN_STRAIGHT_ARMS_HORZ = 2 # Straight Arms/Horizontal
        PAN_STRAIGHT_ARMS_WEDGE = 3 # Straight Arms/Wedge
        PAN_STRAIGHT_ARMS_VERT = 4 # Straight Arms/Vertical
        PAN_STRAIGHT_ARMS_SINGLE_SERIF = 5 # Straight Arms/Single-Serif
        PAN_STRAIGHT_ARMS_DOUBLE_SERIF = 6 # Straight Arms/Double-Serif
        PAN_BENT_ARMS_HORZ = 7 # Non-Straight Arms/Horizontal
        PAN_BENT_ARMS_WEDGE = 8 # Non-Straight Arms/Wedge
        PAN_BENT_ARMS_VERT = 9 # Non-Straight Arms/Vertical
        PAN_BENT_ARMS_SINGLE_SERIF = 10 # Non-Straight Arms/Single-Serif
        PAN_BENT_ARMS_DOUBLE_SERIF = 11 # Non-Straight Arms/Double-Serif
        PAN_LETT_NORMAL_CONTACT = 2 # Normal/Contact
        PAN_LETT_NORMAL_WEIGHTED = 3 # Normal/Weighted
        PAN_LETT_NORMAL_BOXED = 4 # Normal/Boxed
        PAN_LETT_NORMAL_FLATTENED = 5 # Normal/Flattened
        PAN_LETT_NORMAL_ROUNDED = 6 # Normal/Rounded
        PAN_LETT_NORMAL_OFF_CENTER = 7 # Normal/Off Center
        PAN_LETT_NORMAL_SQUARE = 8 # Normal/Square
        PAN_LETT_OBLIQUE_CONTACT = 9 # Oblique/Contact
        PAN_LETT_OBLIQUE_WEIGHTED = 10 # Oblique/Weighted
        PAN_LETT_OBLIQUE_BOXED = 11 # Oblique/Boxed
        PAN_LETT_OBLIQUE_FLATTENED = 12 # Oblique/Flattened
        PAN_LETT_OBLIQUE_ROUNDED = 13 # Oblique/Rounded
        PAN_LETT_OBLIQUE_OFF_CENTER = 14 # Oblique/Off Center
        PAN_LETT_OBLIQUE_SQUARE = 15 # Oblique/Square
        PAN_MIDLINE_STANDARD_TRIMMED = 2 # Standard/Trimmed
        PAN_MIDLINE_STANDARD_POINTED = 3 # Standard/Pointed
        PAN_MIDLINE_STANDARD_SERIFED = 4 # Standard/Serifed
        PAN_MIDLINE_HIGH_TRIMMED = 5 # High/Trimmed
        PAN_MIDLINE_HIGH_POINTED = 6 # High/Pointed
        PAN_MIDLINE_HIGH_SERIFED = 7 # High/Serifed
        PAN_MIDLINE_CONSTANT_TRIMMED = 8 # Constant/Trimmed
        PAN_MIDLINE_CONSTANT_POINTED = 9 # Constant/Pointed
        PAN_MIDLINE_CONSTANT_SERIFED = 10 # Constant/Serifed
        PAN_MIDLINE_LOW_TRIMMED = 11 # Low/Trimmed
        PAN_MIDLINE_LOW_POINTED = 12 # Low/Pointed
        PAN_MIDLINE_LOW_SERIFED = 13 # Low/Serifed
        PAN_XHEIGHT_CONSTANT_SMALL = 2 # Constant/Small
        PAN_XHEIGHT_CONSTANT_STD = 3 # Constant/Standard
        PAN_XHEIGHT_CONSTANT_LARGE = 4 # Constant/Large
        PAN_XHEIGHT_DUCKING_SMALL = 5 # Ducking/Small
        PAN_XHEIGHT_DUCKING_STD = 6 # Ducking/Standard
        PAN_XHEIGHT_DUCKING_LARGE = 7 # Ducking/Large
        ELF_VENDOR_SIZE = 4
        # The extended logical font
        # An extension of the ENUMLOGFONT

        class tagEXTLOGFONTA(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTA),
                ("elfFullName", CHAR * LF_FULLFACESIZE),
                ("elfStyle", CHAR * LF_FACESIZE),
                ("elfVersion", DWORD), # 0 for the first release of NT
                ("elfStyleSize", DWORD),
                ("elfMatch", DWORD),
                ("elfReserved", DWORD),
                ("elfVendored", CHAR * ELF_VENDOR_SIZE),
                ("elfCulture", DWORD), # 0 for Latin                   
                ("elfPanose", PANOSE)
            ]
        EXTLOGFONTA = tagEXTLOGFONTA
        PEXTLOGFONTA = POINTER(EXTLOGFONTA)
        NPEXTLOGFONTA = PEXTLOGFONTA
        LPEXTLOGFONTA = PEXTLOGFONTA

        class tagEXTLOGFONTW(CStructure):
            _fields_ = [
                ("elfLogFont", LOGFONTW),
                ("elfFullName", WCHAR * LF_FULLFACESIZE),
                ("elfStyle", WCHAR * LF_FACESIZE),
                ("elfVersion", DWORD), # 0 for the first release of NT
                ("elfStyleSize", DWORD),
                ("elfMatch", DWORD),
                ("elfReserved", DWORD),
                ("elfVendored", WCHAR * ELF_VENDOR_SIZE),
                ("elfCulture", DWORD), # 0 for Latin                   
                ("elfPanose", PANOSE)
            ]
        EXTLOGFONTW = tagEXTLOGFONTW
        PEXTLOGFONTW = POINTER(EXTLOGFONTW)
        NPEXTLOGFONTW = PEXTLOGFONTW
        LPEXTLOGFONTW = PEXTLOGFONTW

        EXTLOGFONT = unicode(EXTLOGFONTW, EXTLOGFONTA)
        PEXTLOGFONT = unicode(PEXTLOGFONTW, PEXTLOGFONTA)
        NPEXTLOGFONT = unicode(NPEXTLOGFONTW, NPEXTLOGFONTA)
        LPEXTLOGFONT = unicode(LPEXTLOGFONTW, LPEXTLOGFONTA)

        # REGION ***
        ELF_VERSION = 0
        ELF_CULTURE_LATIN = 0
        # EnumFonts Masks
        RASTER_FONTTYPE = 0x0001
        DEVICE_FONTTYPE = 0x0002
        TRUETYPE_FONTTYPE = 0x0004
        RGB = lambda r,g,b: COLORREF(BYTE(r).value | (WORD(BYTE(g).value).value << 8) | (DWORD(BYTE(b).value).value << 16)).value
        PALETTERGB = lambda r,g,b: 0x02000000 | RGB(r,g,b)
        PALETTEINDEX = lambda i: COLORREF(0x01000000 | DWORD(WORD(i).value).value).value
        # palette entry flags
        PC_RESERVED = 0x01 # palette index used for animation
        PC_EXPLICIT = 0x02 # palette index is explicit to device
        PC_NOCOLLAPSE = 0x04 # do not match color to system palette
        GetRValue = lambda rgb: LOBYTE(rgb)
        GetGValue = lambda rgb: LOBYTE(WORD(rgb).value >> 8)
        GetBValue = lambda rgb: LOBYTE(rgb >> 16)
        # Background Modes
        TRANSPARENT = 1
        OPAQUE = 2
        BKMODE_LAST = 2
        # Graphics Modes
        GM_COMPATIBLE = 1
        GM_ADVANCED = 2
        GM_LAST = 2
        # PolyDraw and GetPath point types
        PT_CLOSEFIGURE = 0x01
        PT_LINETO = 0x02
        PT_BEZIERTO = 0x04
        PT_MOVETO = 0x06
        # Mapping Modes
        MM_TEXT = 1
        MM_LOMETRIC = 2
        MM_HIMETRIC = 3
        MM_LOENGLISH = 4
        MM_HIENGLISH = 5
        MM_TWIPS = 6
        MM_ISOTROPIC = 7
        MM_ANISOTROPIC = 8
        # Min and Max Mapping Mode values
        MM_MIN = MM_TEXT
        MM_MAX = MM_ANISOTROPIC
        MM_MAX_FIXEDSCALE = MM_TWIPS
        # Coordinate Modes
        ABSOLUTE = 1
        RELATIVE = 2
        # Stock Logical Objects
        WHITE_BRUSH = 0
        LTGRAY_BRUSH = 1
        GRAY_BRUSH = 2
        DKGRAY_BRUSH = 3
        BLACK_BRUSH = 4
        NULL_BRUSH = 5
        HOLLOW_BRUSH = NULL_BRUSH
        WHITE_PEN = 6
        BLACK_PEN = 7
        NULL_PEN = 8
        OEM_FIXED_FONT = 10
        ANSI_FIXED_FONT = 11
        ANSI_VAR_FONT = 12
        SYSTEM_FONT = 13
        DEVICE_DEFAULT_FONT = 14
        DEFAULT_PALETTE = 15
        SYSTEM_FIXED_FONT = 16
        DEFAULT_GUI_FONT = 17
        DC_BRUSH = 18
        DC_PEN = 19
        STOCK_LAST = 19
        STOCK_LAST = 17
        STOCK_LAST = 16
        CLR_INVALID = 0xFFFFFFFF
        # Brush Styles
        BS_SOLID = 0
        BS_NULL = 1
        BS_HOLLOW = BS_NULL
        BS_HATCHED = 2
        BS_PATTERN = 3
        BS_INDEXED = 4
        BS_DIBPATTERN = 5
        BS_DIBPATTERNPT = 6
        BS_PATTERN8X8 = 7
        BS_DIBPATTERN8X8 = 8
        BS_MONOPATTERN = 9
        # Hatch Styles
        HS_HORIZONTAL = 0 # -----
        HS_VERTICAL = 1 # |||||
        HS_FDIAGONAL = 2 # \\\\\
        HS_BDIAGONAL = 3 # /////
        HS_CROSS = 4 # +++++
        HS_DIAGCROSS = 5 # xxxxx
        HS_API_MAX = 12
        # Pen Styles
        PS_SOLID = 0
        PS_DASH = 1 # -------
        PS_DOT = 2 # .......
        PS_DASHDOT = 3 # _._._._
        PS_DASHDOTDOT = 4 # _.._.._
        PS_NULL = 5
        PS_INSIDEFRAME = 6
        PS_USERSTYLE = 7
        PS_ALTERNATE = 8
        PS_STYLE_MASK = 0x0000000F
        PS_ENDCAP_ROUND = 0x00000000
        PS_ENDCAP_SQUARE = 0x00000100
        PS_ENDCAP_FLAT = 0x00000200
        PS_ENDCAP_MASK = 0x00000F00
        PS_JOIN_ROUND = 0x00000000
        PS_JOIN_BEVEL = 0x00001000
        PS_JOIN_MITER = 0x00002000
        PS_JOIN_MASK = 0x0000F000
        PS_COSMETIC = 0x00000000
        PS_GEOMETRIC = 0x00010000
        PS_TYPE_MASK = 0x000F0000
        AD_COUNTERCLOCKWISE = 1
        AD_CLOCKWISE = 2
        # Device Parameters for GetDeviceCaps()
        DRIVERVERSION = 0 # Device driver version
        TECHNOLOGY = 2 # Device classification
        HORZSIZE = 4 # Horizontal size in millimeters
        VERTSIZE = 6 # Vertical size in millimeters
        HORZRES = 8 # Horizontal width in pixels
        VERTRES = 10 # Vertical height in pixels
        BITSPIXEL = 12 # Number of bits per pixel
        PLANES = 14 # Number of planes
        NUMBRUSHES = 16 # Number of brushes the device has
        NUMPENS = 18 # Number of pens the device has
        NUMMARKERS = 20 # Number of markers the device has
        NUMFONTS = 22 # Number of fonts the device has
        NUMCOLORS = 24 # Number of colors the device supports
        PDEVICESIZE = 26 # Size required for device descriptor
        CURVECAPS = 28 # Curve capabilities
        LINECAPS = 30 # Line capabilities
        POLYGONALCAPS = 32 # Polygonal capabilities
        TEXTCAPS = 34 # Text capabilities
        CLIPCAPS = 36 # Clipping capabilities
        RASTERCAPS = 38 # Bitblt capabilities
        ASPECTX = 40 # Length of the X leg
        ASPECTY = 42 # Length of the Y leg
        ASPECTXY = 44 # Length of the hypotenuse
        LOGPIXELSX = 88 # Logical pixels/inch in X
        LOGPIXELSY = 90 # Logical pixels/inch in Y
        SIZEPALETTE = 104 # Number of entries in physical palette
        NUMRESERVED = 106 # Number of reserved entries in palette
        COLORRES = 108 # Actual color resolution
        # Printing related DeviceCaps. These replace the appropriate Escapes
        PHYSICALWIDTH = 110 # Physical Width in device units
        PHYSICALHEIGHT = 111 # Physical Height in device units
        PHYSICALOFFSETX = 112 # Physical Printable Area x margin
        PHYSICALOFFSETY = 113 # Physical Printable Area y margin
        SCALINGFACTORX = 114 # Scaling factor x
        SCALINGFACTORY = 115 # Scaling factor y
        # Display driver specific
        VREFRESH = 116 # Current vertical refresh rate of the
        # display device (for displays only) in Hz
        DESKTOPVERTRES = 117 # Horizontal width of entire desktop in
        # pixels
        DESKTOPHORZRES = 118 # Vertical height of entire desktop in
        # pixels
        BLTALIGNMENT = 119 # Preferred blt alignment
        SHADEBLENDCAPS = 120 # Shading and blending caps
        COLORMGMTCAPS = 121 # Color Management caps
        if cpreproc.ifndef("NOGDICAPMASKS"):
            # Device Capability Masks:
            # Device Technologies
            DT_PLOTTER = 0 # Vector plotter
            DT_RASDISPLAY = 1 # Raster display
            DT_RASPRINTER = 2 # Raster printer
            DT_RASCAMERA = 3 # Raster camera
            DT_CHARSTREAM = 4 # Character-stream, PLP
            DT_METAFILE = 5 # Metafile, VDM
            DT_DISPFILE = 6 # Display-file
            # Curve Capabilities
            CC_NONE = 0 # Curves not supported
            CC_CIRCLES = 1 # Can do circles
            CC_PIE = 2 # Can do pie wedges
            CC_CHORD = 4 # Can do chord arcs
            CC_ELLIPSES = 8 # Can do ellipese
            CC_WIDE = 16 # Can do wide lines
            CC_STYLED = 32 # Can do styled lines
            CC_WIDESTYLED = 64 # Can do wide styled lines
            CC_INTERIORS = 128 # Can do interiors
            CC_ROUNDRECT = 256 #
            # Line Capabilities
            LC_NONE = 0 # Lines not supported
            LC_POLYLINE = 2 # Can do polylines
            LC_MARKER = 4 # Can do markers
            LC_POLYMARKER = 8 # Can do polymarkers
            LC_WIDE = 16 # Can do wide lines
            LC_STYLED = 32 # Can do styled lines
            LC_WIDESTYLED = 64 # Can do wide styled lines
            LC_INTERIORS = 128 # Can do interiors
            # Polygonal Capabilities
            PC_NONE = 0 # Polygonals not supported
            PC_POLYGON = 1 # Can do polygons
            PC_RECTANGLE = 2 # Can do rectangles
            PC_WINDPOLYGON = 4 # Can do winding polygons
            PC_TRAPEZOID = 4 # Can do trapezoids
            PC_SCANLINE = 8 # Can do scanlines
            PC_WIDE = 16 # Can do wide borders
            PC_STYLED = 32 # Can do styled borders
            PC_WIDESTYLED = 64 # Can do wide styled borders
            PC_INTERIORS = 128 # Can do interiors
            PC_POLYPOLYGON = 256 # Can do polypolygons
            PC_PATHS = 512 # Can do paths
            # Clipping Capabilities
            CP_NONE = 0 # No clipping of output
            CP_RECTANGLE = 1 # Output clipped to rects
            CP_REGION = 2 # obsolete
            # Text Capabilities
            TC_OP_CHARACTER = 0x00000001 # Can do OutputPrecision   CHARACTER
            TC_OP_STROKE = 0x00000002 # Can do OutputPrecision   STROKE
            TC_CP_STROKE = 0x00000004 # Can do ClipPrecision     STROKE
            TC_CR_90 = 0x00000008 # Can do CharRotAbility    90
            TC_CR_ANY = 0x00000010 # Can do CharRotAbility    ANY
            TC_SF_X_YINDEP = 0x00000020 # Can do ScaleFreedom      X_YINDEPENDENT
            TC_SA_DOUBLE = 0x00000040 # Can do ScaleAbility      DOUBLE
            TC_SA_INTEGER = 0x00000080 # Can do ScaleAbility      INTEGER
            TC_SA_CONTIN = 0x00000100 # Can do ScaleAbility      CONTINUOUS
            TC_EA_DOUBLE = 0x00000200 # Can do EmboldenAbility   DOUBLE
            TC_IA_ABLE = 0x00000400 # Can do ItalisizeAbility  ABLE
            TC_UA_ABLE = 0x00000800 # Can do UnderlineAbility  ABLE
            TC_SO_ABLE = 0x00001000 # Can do StrikeOutAbility  ABLE
            TC_RA_ABLE = 0x00002000 # Can do RasterFontAble    ABLE
            TC_VA_ABLE = 0x00004000 # Can do VectorFontAble    ABLE
            TC_RESERVED = 0x00008000
            TC_SCROLLBLT = 0x00010000 # Don't do text scroll with blt
        # NOGDICAPMASKS
        # Raster Capabilities
        cpreproc.define("RC_NONE")
        RC_BITBLT = 1 # Can do standard BLT.
        RC_BANDING = 2 # Device requires banding support
        RC_SCALING = 4 # Device requires scaling support
        RC_BITMAP64 = 8 # Device can support >64K bitmap
        RC_GDI20_OUTPUT = 0x0010 # has 2.0 output calls
        RC_GDI20_STATE = 0x0020
        RC_SAVEBITMAP = 0x0040
        RC_DI_BITMAP = 0x0080 # supports DIB to memory
        RC_PALETTE = 0x0100 # supports a palette
        RC_DIBTODEV = 0x0200 # supports DIBitsToDevice
        RC_BIGFONT = 0x0400 # supports >64K fonts
        RC_STRETCHBLT = 0x0800 # supports StretchBlt
        RC_FLOODFILL = 0x1000 # supports FloodFill
        RC_STRETCHDIB = 0x2000 # supports StretchDIBits
        RC_OP_DX_OUTPUT = 0x4000
        RC_DEVBITS = 0x8000
        # Shading and blending caps
        SB_NONE = 0x00000000
        SB_CONST_ALPHA = 0x00000001
        SB_PIXEL_ALPHA = 0x00000002
        SB_PREMULT_ALPHA = 0x00000004
        SB_GRAD_RECT = 0x00000010
        SB_GRAD_TRI = 0x00000020
        # Color Management caps
        CM_NONE = 0x00000000
        CM_DEVICE_ICM = 0x00000001
        CM_GAMMA_RAMP = 0x00000002
        CM_CMYK_COLOR = 0x00000004
        # DIB color table identifiers
        DIB_RGB_COLORS = 0 # color table in RGBs
        DIB_PAL_COLORS = 1 # color table in palette indices
        # constants for Get/SetSystemPaletteUse()
        SYSPAL_ERROR = 0
        SYSPAL_STATIC = 1
        SYSPAL_NOSTATIC = 2
        SYSPAL_NOSTATIC256 = 3
        # constants for CreateDIBitmap
        CBM_INIT = 0x04 # initialize bitmap
        # ExtFloodFill style flags
        FLOODFILLBORDER = 0
        FLOODFILLSURFACE = 1
        # size of a device name string
        CCHDEVICENAME = 32
        # size of a form name string
        CCHFORMNAME = 32

        # REGION *** Application Family ***

        class _S_DODPSDPLDPWDSDCDDDPQ(CStructure):
            _fields_ = [
                ("dmOrientation", SHORT),
                ("dmPaperSize", SHORT),
                ("dmPaperLength", SHORT),
                ("dmPaperWidth", SHORT),
                ("dmScale", SHORT),
                ("dmCopies", SHORT),
                ("dmDefaultSource", SHORT),
                ("dmPrintQuality", SHORT)
            ]

        class _S2_DPDDDD(CStructure):
            _fields_ = [
                ("dmPosition", POINTL),
                ("dmDisplayOrientation", DWORD),
                ("dmDisplayFixedOutput", DWORD)
            ]

        class _U_SS2(Union):
            _fields_ = [
                ("s", _S_DODPSDPLDPWDSDCDDDPQ),
                ("s2", _S2_DPDDDD)
            ]

        class _U2_DDFDN(Union):
            _fields_ = [
                ("dmDisplayFlags", DWORD),
                ("dmNup", DWORD)
            ]

        class _devicemodeA(CStructure):
            _fields_ = [
                ("dmDeviceName", CHAR * CCHDEVICENAME),
                ("dmSpecVersion", WORD),
                ("dmDriverVersion", WORD),
                ("dmSize", WORD),
                ("dmDriverExtra", WORD),
                ("dmFields", DWORD),
                ("u", _U_SS2),
                ("dmColor", SHORT),
                ("dmDuplex", SHORT),
                ("dmYResolution", SHORT),
                ("dmTTOption", SHORT),
                ("dmCollate", SHORT),
                ("dmFormName", CHAR * CCHFORMNAME),
                ("dmLogPixels", WORD),
                ("dmBitsPerPel",  DWORD),
                ("dmPelsWidth", DWORD),
                ("dmPelsHeight", DWORD),
                ("u2", _U2_DDFDN),
                ("dmICMMethod", DWORD),
                ("dmICMIntent", DWORD),
                ("dmMediaType", DWORD),
                ("dmDitherType", DWORD),
                ("dmReserved1", DWORD),
                ("dmReserved2", DWORD),
                ("dmPanningWidth", DWORD),
                ("dmPanningHeight", DWORD)
            ]

        DEVMODEA = _devicemodeA
        PDEVMODEA = POINTER(DEVMODEA)
        NPDEVMODEA = PDEVMODEA
        LPDEVMODEA = PDEVMODEA

        class _devicemodeW(CStructure):
            _fields_ = [
                ("dmDeviceName", WCHAR * CCHDEVICENAME),
                ("dmSpecVersion", WORD),
                ("dmDriverVersion", WORD),
                ("dmSize", WORD),
                ("dmDriverExtra", WORD),
                ("dmFields", DWORD),
                ("u", _U_SS2),
                ("dmColor", SHORT),
                ("dmDuplex", SHORT),
                ("dmYResolution", SHORT),
                ("dmTTOption", SHORT),
                ("dmCollate", SHORT),
                ("dmFormName", WCHAR * CCHFORMNAME),
                ("dmLogPixels", WORD),
                ("dmBitsPerPel",  DWORD),
                ("dmPelsWidth", DWORD),
                ("dmPelsHeight", DWORD),
                ("u2", _U2_DDFDN),
                ("dmICMMethod", DWORD),
                ("dmICMIntent", DWORD),
                ("dmMediaType", DWORD),
                ("dmDitherType", DWORD),
                ("dmReserved1", DWORD),
                ("dmReserved2", DWORD),
                ("dmPanningWidth", DWORD),
                ("dmPanningHeight", DWORD)
            ]

        DEVMODEW = _devicemodeW
        PDEVMODEW = POINTER(DEVMODEW)
        NPDEVMODEW = PDEVMODEW
        LPDEVMODEW = PDEVMODEW

        DEVMODE = unicode(DEVMODEW, DEVMODEA)
        PDEVMODE = unicode(PDEVMODEW, PDEVMODEA)
        NPDEVMODE = unicode(NPDEVMODEW, NPDEVMODEA)
        LPDEVMODE = unicode(LPDEVMODEW, LPDEVMODEA)

        # REGION ***

        # current version of specification
        DM_SPECVERSION = 0x0401
        DM_SPECVERSION = 0x0400
        DM_SPECVERSION = 0x0320
        # field selection bits
        DM_ORIENTATION = 0x00000001
        DM_PAPERSIZE = 0x00000002
        DM_PAPERLENGTH = 0x00000004
        DM_PAPERWIDTH = 0x00000008
        DM_SCALE = 0x00000010
        DM_POSITION = 0x00000020
        DM_NUP = 0x00000040
        DM_DISPLAYORIENTATION = 0x00000080
        DM_COPIES = 0x00000100
        DM_DEFAULTSOURCE = 0x00000200
        DM_PRINTQUALITY = 0x00000400
        DM_COLOR = 0x00000800
        DM_DUPLEX = 0x00001000
        DM_YRESOLUTION = 0x00002000
        DM_TTOPTION = 0x00004000
        DM_COLLATE = 0x00008000
        DM_FORMNAME = 0x00010000
        DM_LOGPIXELS = 0x00020000
        DM_BITSPERPEL = 0x00040000
        DM_PELSWIDTH = 0x00080000
        DM_PELSHEIGHT = 0x00100000
        DM_DISPLAYFLAGS = 0x00200000
        DM_DISPLAYFREQUENCY = 0x00400000
        DM_ICMMETHOD = 0x00800000
        DM_ICMINTENT = 0x01000000
        DM_MEDIATYPE = 0x02000000
        DM_DITHERTYPE = 0x04000000
        DM_PANNINGWIDTH = 0x08000000
        DM_PANNINGHEIGHT = 0x10000000
        DM_DISPLAYFIXEDOUTPUT = 0x20000000
        # orientation selections
        DMORIENT_PORTRAIT = 1
        DMORIENT_LANDSCAPE = 2
        # paper selections
        DMPAPER_FIRST = 1
        DMPAPER_LETTER = 1 # Letter 8 1/2 x 11 in
        DMPAPER_LETTERSMALL = 2 # Letter Small 8 1/2 x 11 in
        DMPAPER_TABLOID = 3 # Tabloid 11 x 17 in
        DMPAPER_LEDGER = 4 # Ledger 17 x 11 in
        DMPAPER_LEGAL = 5 # Legal 8 1/2 x 14 in
        DMPAPER_STATEMENT = 6 # Statement 5 1/2 x 8 1/2 in
        DMPAPER_EXECUTIVE = 7 # Executive 7 1/4 x 10 1/2 in
        DMPAPER_A3 = 8 # A3 297 x 420 mm
        DMPAPER_A4 = 9 # A4 210 x 297 mm
        DMPAPER_A4SMALL = 10 # A4 Small 210 x 297 mm
        DMPAPER_A5 = 11 # A5 148 x 210 mm
        DMPAPER_B4 = 12 # B4 (JIS) 250 x 354
        DMPAPER_B5 = 13 # B5 (JIS) 182 x 257 mm
        DMPAPER_FOLIO = 14 # Folio 8 1/2 x 13 in
        DMPAPER_QUARTO = 15 # Quarto 215 x 275 mm
        DMPAPER_10X14 = 16 # 10x14 in
        DMPAPER_11X17 = 17 # 11x17 in
        DMPAPER_NOTE = 18 # Note 8 1/2 x 11 in
        DMPAPER_ENV_9 = 19 # Envelope #9 3 7/8 x 8 7/8
        DMPAPER_ENV_10 = 20 # Envelope #10 4 1/8 x 9 1/2
        DMPAPER_ENV_11 = 21 # Envelope #11 4 1/2 x 10 3/8
        DMPAPER_ENV_12 = 22 # Envelope #12 4 \276 x 11
        DMPAPER_ENV_14 = 23 # Envelope #14 5 x 11 1/2
        DMPAPER_CSHEET = 24 # C size sheet
        DMPAPER_DSHEET = 25 # D size sheet
        DMPAPER_ESHEET = 26 # E size sheet
        DMPAPER_ENV_DL = 27 # Envelope DL 110 x 220mm
        DMPAPER_ENV_C5 = 28 # Envelope C5 162 x 229 mm
        DMPAPER_ENV_C3 = 29 # Envelope C3  324 x 458 mm
        DMPAPER_ENV_C4 = 30 # Envelope C4  229 x 324 mm
        DMPAPER_ENV_C6 = 31 # Envelope C6  114 x 162 mm
        DMPAPER_ENV_C65 = 32 # Envelope C65 114 x 229 mm
        DMPAPER_ENV_B4 = 33 # Envelope B4  250 x 353 mm
        DMPAPER_ENV_B5 = 34 # Envelope B5  176 x 250 mm
        DMPAPER_ENV_B6 = 35 # Envelope B6  176 x 125 mm
        DMPAPER_ENV_ITALY = 36 # Envelope 110 x 230 mm
        DMPAPER_ENV_MONARCH = 37 # Envelope Monarch 3.875 x 7.5 in
        DMPAPER_ENV_PERSONAL = 38 # 6 3/4 Envelope 3 5/8 x 6 1/2 in
        DMPAPER_FANFOLD_US = 39 # US Std Fanfold 14 7/8 x 11 in
        DMPAPER_FANFOLD_STD_GERMAN = 40 # German Std Fanfold 8 1/2 x 12 in
        DMPAPER_FANFOLD_LGL_GERMAN = 41 # German Legal Fanfold 8 1/2 x 13 in
        DMPAPER_ISO_B4 = 42 # B4 (ISO) 250 x 353 mm
        DMPAPER_JAPANESE_POSTCARD = 43 # Japanese Postcard 100 x 148 mm
        DMPAPER_9X11 = 44 # 9 x 11 in
        DMPAPER_10X11 = 45 # 10 x 11 in
        DMPAPER_15X11 = 46 # 15 x 11 in
        DMPAPER_ENV_INVITE = 47 # Envelope Invite 220 x 220 mm
        DMPAPER_RESERVED_48 = 48 # RESERVED--DO NOT USE
        DMPAPER_RESERVED_49 = 49 # RESERVED--DO NOT USE
        DMPAPER_LETTER_EXTRA = 50 # Letter Extra 9 \275 x 12 in
        DMPAPER_LEGAL_EXTRA = 51 # Legal Extra 9 \275 x 15 in
        DMPAPER_TABLOID_EXTRA = 52 # Tabloid Extra 11.69 x 18 in
        DMPAPER_A4_EXTRA = 53 # A4 Extra 9.27 x 12.69 in
        DMPAPER_LETTER_TRANSVERSE = 54 # Letter Transverse 8 \275 x 11 in
        DMPAPER_A4_TRANSVERSE = 55 # A4 Transverse 210 x 297 mm
        DMPAPER_LETTER_EXTRA_TRANSVERSE = 56 # Letter Extra Transverse 9\275 x 12 in
        DMPAPER_A_PLUS = 57 # SuperA/SuperA/A4 227 x 356 mm
        DMPAPER_B_PLUS = 58 # SuperB/SuperB/A3 305 x 487 mm
        DMPAPER_LETTER_PLUS = 59 # Letter Plus 8.5 x 12.69 in
        DMPAPER_A4_PLUS = 60 # A4 Plus 210 x 330 mm
        DMPAPER_A5_TRANSVERSE = 61 # A5 Transverse 148 x 210 mm
        DMPAPER_B5_TRANSVERSE = 62 # B5 (JIS) Transverse 182 x 257 mm
        DMPAPER_A3_EXTRA = 63 # A3 Extra 322 x 445 mm
        DMPAPER_A5_EXTRA = 64 # A5 Extra 174 x 235 mm
        DMPAPER_B5_EXTRA = 65 # B5 (ISO) Extra 201 x 276 mm
        DMPAPER_A2 = 66 # A2 420 x 594 mm
        DMPAPER_A3_TRANSVERSE = 67 # A3 Transverse 297 x 420 mm
        DMPAPER_A3_EXTRA_TRANSVERSE = 68 # A3 Extra Transverse 322 x 445 mm
        DMPAPER_DBL_JAPANESE_POSTCARD = 69 # Japanese Double Postcard 200 x 148 mm
        DMPAPER_A6 = 70 # A6 105 x 148 mm
        DMPAPER_JENV_KAKU2 = 71 # Japanese Envelope Kaku #2
        DMPAPER_JENV_KAKU3 = 72 # Japanese Envelope Kaku #3
        DMPAPER_JENV_CHOU3 = 73 # Japanese Envelope Chou #3
        DMPAPER_JENV_CHOU4 = 74 # Japanese Envelope Chou #4
        DMPAPER_LETTER_ROTATED = 75 # Letter Rotated 11 x 8 1/2 11 in
        DMPAPER_A3_ROTATED = 76 # A3 Rotated 420 x 297 mm
        DMPAPER_A4_ROTATED = 77 # A4 Rotated 297 x 210 mm
        DMPAPER_A5_ROTATED = 78 # A5 Rotated 210 x 148 mm
        DMPAPER_B4_JIS_ROTATED = 79 # B4 (JIS) Rotated 364 x 257 mm
        DMPAPER_B5_JIS_ROTATED = 80 # B5 (JIS) Rotated 257 x 182 mm
        DMPAPER_JAPANESE_POSTCARD_ROTATED = 81 # Japanese Postcard Rotated 148 x 100 mm
        DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED = 82 # Double Japanese Postcard Rotated 148 x 200 mm
        DMPAPER_A6_ROTATED = 83 # A6 Rotated 148 x 105 mm
        DMPAPER_JENV_KAKU2_ROTATED = 84 # Japanese Envelope Kaku #2 Rotated
        DMPAPER_JENV_KAKU3_ROTATED = 85 # Japanese Envelope Kaku #3 Rotated
        DMPAPER_JENV_CHOU3_ROTATED = 86 # Japanese Envelope Chou #3 Rotated
        DMPAPER_JENV_CHOU4_ROTATED = 87 # Japanese Envelope Chou #4 Rotated
        DMPAPER_B6_JIS = 88 # B6 (JIS) 128 x 182 mm
        DMPAPER_B6_JIS_ROTATED = 89 # B6 (JIS) Rotated 182 x 128 mm
        DMPAPER_12X11 = 90 # 12 x 11 in
        DMPAPER_JENV_YOU4 = 91 # Japanese Envelope You #4
        DMPAPER_JENV_YOU4_ROTATED = 92 # Japanese Envelope You #4 Rotated
        DMPAPER_P16K = 93 # PRC 16K 146 x 215 mm
        DMPAPER_P32K = 94 # PRC 32K 97 x 151 mm
        DMPAPER_P32KBIG = 95 # PRC 32K(Big) 97 x 151 mm
        DMPAPER_PENV_1 = 96 # PRC Envelope #1 102 x 165 mm
        DMPAPER_PENV_2 = 97 # PRC Envelope #2 102 x 176 mm
        DMPAPER_PENV_3 = 98 # PRC Envelope #3 125 x 176 mm
        DMPAPER_PENV_4 = 99 # PRC Envelope #4 110 x 208 mm
        DMPAPER_PENV_5 = 100 # PRC Envelope #5 110 x 220 mm
        DMPAPER_PENV_6 = 101 # PRC Envelope #6 120 x 230 mm
        DMPAPER_PENV_7 = 102 # PRC Envelope #7 160 x 230 mm
        DMPAPER_PENV_8 = 103 # PRC Envelope #8 120 x 309 mm
        DMPAPER_PENV_9 = 104 # PRC Envelope #9 229 x 324 mm
        DMPAPER_PENV_10 = 105 # PRC Envelope #10 324 x 458 mm
        DMPAPER_P16K_ROTATED = 106 # PRC 16K Rotated
        DMPAPER_P32K_ROTATED = 107 # PRC 32K Rotated
        DMPAPER_P32KBIG_ROTATED = 108 # PRC 32K(Big) Rotated
        DMPAPER_PENV_1_ROTATED = 109 # PRC Envelope #1 Rotated 165 x 102 mm
        DMPAPER_PENV_2_ROTATED = 110 # PRC Envelope #2 Rotated 176 x 102 mm
        DMPAPER_PENV_3_ROTATED = 111 # PRC Envelope #3 Rotated 176 x 125 mm
        DMPAPER_PENV_4_ROTATED = 112 # PRC Envelope #4 Rotated 208 x 110 mm
        DMPAPER_PENV_5_ROTATED = 113 # PRC Envelope #5 Rotated 220 x 110 mm
        DMPAPER_PENV_6_ROTATED = 114 # PRC Envelope #6 Rotated 230 x 120 mm
        DMPAPER_PENV_7_ROTATED = 115 # PRC Envelope #7 Rotated 230 x 160 mm
        DMPAPER_PENV_8_ROTATED = 116 # PRC Envelope #8 Rotated 309 x 120 mm
        DMPAPER_PENV_9_ROTATED = 117 # PRC Envelope #9 Rotated 324 x 229 mm
        DMPAPER_PENV_10_ROTATED = 118 # PRC Envelope #10 Rotated 458 x 324 mm
        DMPAPER_LAST = DMPAPER_PENV_10_ROTATED
        DMPAPER_LAST = DMPAPER_A3_EXTRA_TRANSVERSE
        DMPAPER_LAST = DMPAPER_FANFOLD_LGL_GERMAN
        DMPAPER_USER = 256
        # bin selections
        DMBIN_FIRST = 1
        DMBIN_UPPER = 1
        DMBIN_ONLYONE = 1
        DMBIN_LOWER = 2
        DMBIN_MIDDLE = 3
        DMBIN_MANUAL = 4
        DMBIN_ENVELOPE = 5
        DMBIN_ENVMANUAL = 6
        DMBIN_AUTO = 7
        DMBIN_TRACTOR = 8
        DMBIN_SMALLFMT = 9
        DMBIN_LARGEFMT = 10
        DMBIN_LARGECAPACITY = 11
        DMBIN_CASSETTE = 14
        DMBIN_FORMSOURCE = 15
        DMBIN_LAST = DMBIN_FORMSOURCE
        DMBIN_USER = 256 # device specific bins start here
        # print qualities
        DMRES_DRAFT = (-1)
        DMRES_LOW = (-2)
        DMRES_MEDIUM = (-3)
        DMRES_HIGH = (-4)
        # color enable/disable for color printers
        DMCOLOR_MONOCHROME = 1
        DMCOLOR_COLOR = 2
        # duplex enable
        DMDUP_SIMPLEX = 1
        DMDUP_VERTICAL = 2
        DMDUP_HORIZONTAL = 3
        # TrueType options
        DMTT_BITMAP = 1 # print TT fonts as graphics
        DMTT_DOWNLOAD = 2 # download TT fonts as soft fonts
        DMTT_SUBDEV = 3 # substitute device fonts for TT fonts
        DMTT_DOWNLOAD_OUTLINE = 4 # download TT fonts as outline soft fonts
        # Collation selections
        DMCOLLATE_FALSE = 0
        DMCOLLATE_TRUE = 1
        # DEVMODE dmDisplayOrientation specifiations
        DMDO_DEFAULT = 0
        DMDO_90 = 1
        DMDO_180 = 2
        DMDO_270 = 3
        # DEVMODE dmDisplayFixedOutput specifiations
        DMDFO_DEFAULT = 0
        DMDFO_STRETCH = 1
        DMDFO_CENTER = 2
        # DEVMODE dmDisplayFlags flags
        # DM_GRAYSCALE = 0x00000001 /* This flag is no longer valid */
        DM_INTERLACED = 0x00000002
        DMDISPLAYFLAGS_TEXTMODE = 0x00000004
        # dmNup , multiple logical page per physical page options
        DMNUP_SYSTEM = 1
        DMNUP_ONEUP = 2
        # ICM methods
        DMICMMETHOD_NONE = 1 # ICM disabled
        DMICMMETHOD_SYSTEM = 2 # ICM handled by system
        DMICMMETHOD_DRIVER = 3 # ICM handled by driver
        DMICMMETHOD_DEVICE = 4 # ICM handled by device
        DMICMMETHOD_USER = 256 # Device-specific methods start here
        # ICM Intents
        DMICM_SATURATE = 1 # Maximize color saturation
        DMICM_CONTRAST = 2 # Maximize color contrast
        DMICM_COLORIMETRIC = 3 # Use specific color metric
        DMICM_ABS_COLORIMETRIC = 4 # Use specific color metric
        DMICM_USER = 256 # Device-specific intents start here
        # Media types
        DMMEDIA_STANDARD = 1 # Standard paper
        DMMEDIA_TRANSPARENCY = 2 # Transparency
        DMMEDIA_GLOSSY = 3 # Glossy paper
        DMMEDIA_USER = 256 # Device-specific media start here
        # Dither types
        DMDITHER_NONE = 1 # No dithering
        DMDITHER_COARSE = 2 # Dither with a coarse brush
        DMDITHER_FINE = 3 # Dither with a fine brush
        DMDITHER_LINEART = 4 # LineArt dithering
        DMDITHER_ERRORDIFFUSION = 5 # LineArt dithering
        DMDITHER_RESERVED6 = 6 # LineArt dithering
        DMDITHER_RESERVED7 = 7 # LineArt dithering
        DMDITHER_RESERVED8 = 8 # LineArt dithering
        DMDITHER_RESERVED9 = 9 # LineArt dithering
        DMDITHER_GRAYSCALE = 10 # Device does grayscaling
        DMDITHER_USER = 256 # Device-specific dithers start here

        # REGION *** Application Family ***

        class _DISPLAY_DEVICEA(CStructure):
            _fields_ = [
                ("cb", DWORD),
                ("DeviceName", CHAR * 32),
                ("DeviceString", CHAR * 128),
                ("StateFlags", DWORD),
                ("DeviceID", CHAR * 128),
                ("DeviceKey", CHAR * 128)
            ]
        DISPLAY_DEVICEA = _DISPLAY_DEVICEA
        PDISPLAY_DEVICEA = POINTER(DISPLAY_DEVICEA)
        LPDISPLAY_DEVICEA = PDISPLAY_DEVICEA

        class _DISPLAY_DEVICEW(CStructure):
            _fields_ = [
                ("cb", DWORD),
                ("DeviceName", WCHAR * 32),
                ("DeviceString", WCHAR * 128),
                ("StateFlags", DWORD),
                ("DeviceID", WCHAR * 128),
                ("DeviceKey", WCHAR * 128)
            ]
        DISPLAY_DEVICEW = _DISPLAY_DEVICEW
        PDISPLAY_DEVICEW = POINTER(DISPLAY_DEVICEW)
        LPDISPLAY_DEVICEW = PDISPLAY_DEVICEW

        DISPLAY_DEVICE = unicode(DISPLAY_DEVICEW, DISPLAY_DEVICEA)
        PDISPLAY_DEVICE = unicode(PDISPLAY_DEVICEW, PDISPLAY_DEVICEA)
        LPDISPLAY_DEVICE = unicode(LPDISPLAY_DEVICEW, LPDISPLAY_DEVICEA)

        # REGION ***
        DISPLAY_DEVICE_ATTACHED_TO_DESKTOP = 0x00000001
        DISPLAY_DEVICE_MULTI_DRIVER = 0x00000002
        DISPLAY_DEVICE_PRIMARY_DEVICE = 0x00000004
        DISPLAY_DEVICE_MIRRORING_DRIVER = 0x00000008
        DISPLAY_DEVICE_VGA_COMPATIBLE = 0x00000010
        DISPLAY_DEVICE_REMOVABLE = 0x00000020
        DISPLAY_DEVICE_ACC_DRIVER = 0x00000040
        DISPLAY_DEVICE_MODESPRUNED = 0x08000000
        DISPLAY_DEVICE_RDPUDD = 0x01000000
        DISPLAY_DEVICE_REMOTE = 0x04000000
        DISPLAY_DEVICE_DISCONNECT = 0x02000000
        DISPLAY_DEVICE_TS_COMPATIBLE = 0x00200000
        DISPLAY_DEVICE_UNSAFE_MODES_ON = 0x00080000
        # Child device state
        DISPLAY_DEVICE_ACTIVE = 0x00000001
        DISPLAY_DEVICE_ATTACHED = 0x00000002
        DISPLAYCONFIG_MAXPATH = 1024 # Maximum display path in system.
                                     # Max adapter (16) * Max source (16) *
                                     # Max clone pre source (4)

        # REGION *** Application Family ***

        class DISPLAYCONFIG_RATIONAL(CStructure):
            _fields_ = [
                ("Numerator", UINT32),
                ("Denominator", UINT32)
            ]

        DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY = INT
        if True:
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_OTHER                   = -1
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HD15                    =  0
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SVIDEO                  =  1
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPOSITE_VIDEO         =  2
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPONENT_VIDEO         =  3
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DVI                     =  4
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HDMI                    =  5
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_LVDS                    =  6
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_D_JPN                   =  8
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDI                     =  9
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EXTERNAL    = 10
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EMBEDDED    = 11
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EXTERNAL            = 12
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EMBEDDED            = 13
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDTVDONGLE              = 14
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST                = 15
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_WIRED          = 16
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_VIRTUAL        = 17
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INTERNAL                = 0x80000000
            DISPLAYCONFIG_OUTPUT_TECHNOLOGY_FORCE_UINT32            = 0xFFFFFFFF

        DISPLAYCONFIG_SCANLINE_ORDERING = INT
        if True:
            DISPLAYCONFIG_SCANLINE_ORDERING_UNSPECIFIED                 = 0
            DISPLAYCONFIG_SCANLINE_ORDERING_PROGRESSIVE                 = 1
            DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED                  = 2
            DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_UPPERFIELDFIRST  = DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED
            DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_LOWERFIELDFIRST  = 3
            DISPLAYCONFIG_SCANLINE_ORDERING_FORCE_UINT32                = 0xFFFFFFFF

        class DISPLAYCONFIG_2DREGION(CStructure):
            _fields_ = [
                ("cx", UINT32),
                ("cy", UINT32)
            ]

        class _S_VSVSFDR(CStructure):
            _fields_ = [
                ("videoStandard", UINT32, 16),

                # Vertical refresh frequency divider

                ("vSyncFreqDivider", UINT32, 6),
                ("reserved", UINT32, 10)
            ]

        class _U_SVS(Union):
            _fields_ = [
                ("s", _S_VSVSFDR),
                ("videoStandard", UINT32)
            ]

        class DISPLAYCONFIG_VIDEO_SIGNAL_INFO(CStructure):
            _fields_ = [
                ("pixelRate", UINT64),
                ("hSyncFreq", DISPLAYCONFIG_RATIONAL),
                ("vSyncFreq", DISPLAYCONFIG_RATIONAL),
                ("activeSize", DISPLAYCONFIG_2DREGION),
                ("totalSize", DISPLAYCONFIG_2DREGION),
                ("u", _U_SVS),

                # Scan line ordering (e.g. progressive, interlaced).
                ("scanLineOrdering", DISPLAYCONFIG_SCANLINE_ORDERING)
            ]

        DISPLAYCONFIG_SCALING = INT
        if True:
            DISPLAYCONFIG_SCALING_IDENTITY                  = 1
            DISPLAYCONFIG_SCALING_CENTERED                  = 2
            DISPLAYCONFIG_SCALING_STRETCHED                 = 3
            DISPLAYCONFIG_SCALING_ASPECTRATIOCENTEREDMAX    = 4
            DISPLAYCONFIG_SCALING_CUSTOM                    = 5
            DISPLAYCONFIG_SCALING_PREFERRED                 = 128
            DISPLAYCONFIG_SCALING_FORCE_UINT32              = 0xFFFFFFFF

        DISPLAYCONFIG_ROTATION = INT
        if True:
            DISPLAYCONFIG_ROTATION_IDENTITY     = 1
            DISPLAYCONFIG_ROTATION_ROTATE90     = 2
            DISPLAYCONFIG_ROTATION_ROTATE180    = 3
            DISPLAYCONFIG_ROTATION_ROTATE270    = 4
            DISPLAYCONFIG_ROTATION_FORCE_UINT32 = 0xFFFFFFFF

        DISPLAYCONFIG_MODE_INFO_TYPE = INT
        if True:
            DISPLAYCONFIG_MODE_INFO_TYPE_SOURCE        = 1
            DISPLAYCONFIG_MODE_INFO_TYPE_TARGET        = 2
            DISPLAYCONFIG_MODE_INFO_TYPE_DESKTOP_IMAGE = 3
            DISPLAYCONFIG_MODE_INFO_TYPE_FORCE_UINT32 = 0xFFFFFFFF

        DISPLAYCONFIG_PIXELFORMAT = INT
        if True:
            DISPLAYCONFIG_PIXELFORMAT_8BPP          = 1
            DISPLAYCONFIG_PIXELFORMAT_16BPP         = 2
            DISPLAYCONFIG_PIXELFORMAT_24BPP         = 3
            DISPLAYCONFIG_PIXELFORMAT_32BPP         = 4
            DISPLAYCONFIG_PIXELFORMAT_NONGDI        = 5
            DISPLAYCONFIG_PIXELFORMAT_FORCE_UINT32  = 0xffffffff

        class DISPLAYCONFIG_SOURCE_MODE(CStructure):
            _fields_ = [
                ("width", UINT32),
                ("height", UINT32),
                ("pixelFormat", DISPLAYCONFIG_PIXELFORMAT),
                ("position", POINTL)
            ]

        class DISPLAYCONFIG_TARGET_MODE(CStructure):
            _fields_ = [
                ("targetVideoSignalInfo", DISPLAYCONFIG_VIDEO_SIGNAL_INFO)
            ]

        class DISPLAYCONFIG_DESKTOP_IMAGE_INFO(CStructure):
            _fields_ = [
                ("PathSourceSize", POINTL),
                ("DesktopImageRegion", RECTL),
                ("DesktopImageClip", RECTL)
            ]

        class _U_TMSMDII(Union):
            _fields_ = [
                ("targetMode", DISPLAYCONFIG_TARGET_MODE),
                ("sourceMode", DISPLAYCONFIG_SOURCE_MODE),
                ("desktopImageInfo", DISPLAYCONFIG_DESKTOP_IMAGE_INFO)
            ]

        class DISPLAYCONFIG_MODE_INFO(CStructure):
            _fields_ = [
                ("infoType", DISPLAYCONFIG_MODE_INFO_TYPE),
                ("id", UINT32),
                ("adapterId", LUID),
                ("u", _U_TMSMDII)
            ]

        DISPLAYCONFIG_PATH_MODE_IDX_INVALID = 0xffffffff
        DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID = 0xffff
        DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID = 0xffff
        DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID = 0xffff
        DISPLAYCONFIG_PATH_CLONE_GROUP_INVALID = 0xffff

        class _S_CGISMII(CStructure):
            _fields_ = [
                ("cloneGroupId", UINT32, 16),
                ("sourceModeInfoIdx", UINT32, 16)
            ]

        class _U_MIIS(Union):
            _fields_ = [
                ("modeInfoIdx", UINT32),
                ("s", _S_CGISMII)
            ]

        class DISPLAYCONFIG_PATH_SOURCE_INFO(CStructure):
            _fields_ = [
                ("adapterId", LUID),
                ("id", UINT32),
                ("u", _U_MIIS),
                ("statusFlags", UINT32)
            ]

        #
        # Flags for source info structure (from OS to application through QDC)
        #

        DISPLAYCONFIG_SOURCE_IN_USE = 0x00000001

        class _S_DMIITMII(CStructure):
            _fields_ = [
                ("desktopModeInfoIdx", UINT32, 16),
                ("targetModeInfoIdx", UINT32, 16)
            ]
        
        class _U_MIIS2(Union):
            _fields_ = [
                ("modeInfoIdx", UINT32),
                ("s", _S_DMIITMII)
            ]

        class DISPLAYCONFIG_PATH_TARGET_INFO(CStructure):
            _fields_ = [
                ("adapterId", LUID),
                ("id", UINT32),
                ("outputTechnology", DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY),
                ("rotation", DISPLAYCONFIG_ROTATION),
                ("scaling", DISPLAYCONFIG_SCALING),
                ("refreshRate", DISPLAYCONFIG_RATIONAL),
                ("scanLineOrdering", DISPLAYCONFIG_SCANLINE_ORDERING),
                ("targetAvailable", BOOL),
                ("statusFlags", UINT32)
            ]

        #
        # Status flags for target info structure (from OS to application through QDC)
        #
        DISPLAYCONFIG_TARGET_IN_USE = 0x00000001
        DISPLAYCONFIG_TARGET_FORCIBLE = 0x00000002
        DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_BOOT = 0x00000004
        DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_PATH = 0x00000008
        DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_SYSTEM = 0x00000010
        DISPLAYCONFIG_TARGET_IS_HMD = 0x00000020

        class DISPLAYCONFIG_PATH_INFO(CStructure):
            _fields_ = [
                ("sourceInfo", DISPLAYCONFIG_PATH_SOURCE_INFO),
                ("flags", UINT32)
            ]

        #
        # Flags for path info structure (from OS to application through QDC)
        #

        DISPLAYCONFIG_PATH_ACTIVE = 0x00000001
        DISPLAYCONFIG_PATH_PREFERRED_UNSCALED = 0x00000004 # Not implemented
        DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE = 0x00000008
        DISPLAYCONFIG_PATH_VALID_FLAGS = 0x0000000D

        DISPLAYCONFIG_TOPOLOGY_ID = INT
        if True:
            DISPLAYCONFIG_TOPOLOGY_INTERNAL       = 0x00000001
            DISPLAYCONFIG_TOPOLOGY_CLONE          = 0x00000002
            DISPLAYCONFIG_TOPOLOGY_EXTEND         = 0x00000004
            DISPLAYCONFIG_TOPOLOGY_EXTERNAL       = 0x00000008
            DISPLAYCONFIG_TOPOLOGY_FORCE_UINT32   = 0xFFFFFFFF


        DISPLAYCONFIG_DEVICE_INFO_TYPE = INT
        if True:
            DISPLAYCONFIG_DEVICE_INFO_GET_SOURCE_NAME                 = 1
            DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME                 = 2
            DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_PREFERRED_MODE       = 3
            DISPLAYCONFIG_DEVICE_INFO_GET_ADAPTER_NAME                = 4
            DISPLAYCONFIG_DEVICE_INFO_SET_TARGET_PERSISTENCE          = 5
            DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_BASE_TYPE            = 6
            DISPLAYCONFIG_DEVICE_INFO_GET_SUPPORT_VIRTUAL_RESOLUTION  = 7
            DISPLAYCONFIG_DEVICE_INFO_SET_SUPPORT_VIRTUAL_RESOLUTION  = 8
            DISPLAYCONFIG_DEVICE_INFO_GET_ADVANCED_COLOR_INFO         = 9
            DISPLAYCONFIG_DEVICE_INFO_SET_ADVANCED_COLOR_STATE        = 10
            DISPLAYCONFIG_DEVICE_INFO_GET_SDR_WHITE_LEVEL             = 11
            DISPLAYCONFIG_DEVICE_INFO_FORCE_UINT32                = 0xFFFFFFFF


        # REGION ***


        # REGION *** Application Family ***

        class DISPLAYCONFIG_DEVICE_INFO_HEADER(CStructure):
            _fields_ = [
                ("type", DISPLAYCONFIG_DEVICE_INFO_TYPE),
                ("size", UINT32),
                ("adapterId", LUID),
                ("id", UINT32)
            ]

        # REGION ***

        # REGION *** Desktop Family ***

        class DISPLAYCONFIG_SOURCE_DEVICE_NAME(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("viewGdiDeviceName", WCHAR * CCHDEVICENAME)
            ]

        class _S_FNFEFNFEIVR(CStructure):
            _fields_ = [
                ("friendlyNameFromEdid", UINT32, 1),
                ("friendlyNameForced", UINT32, 1),
                ("edidIdsValid", UINT32, 1),
                ("reserved", UINT32, 29)
            ]

        class _U_SV(Union):
            _fields_ = [
                ("s", _S_FNFEFNFEIVR),
                ("value", UINT32)
            ]

        class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS(CStructure):
            _fields_ = [
                ("u", _U_SV)
            ]

        class DISPLAYCONFIG_TARGET_DEVICE_NAME(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("flags", DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS),
                ("outputTechnology", DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY),
                ("edidManufactureId", UINT16),
                ("edidProductCodeId", UINT16),
                ("connectorInstance", UINT32),
                ("monitorFriendlyDeviceName", WCHAR * 64),
                ("monitorDevicePath", WCHAR * 128)
            ]

        class DISPLAYCONFIG_TARGET_PREFERRED_MODE(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("width", UINT32),
                ("height", UINT32),
                ("targetMode", DISPLAYCONFIG_TARGET_MODE)
            ]

        class DISPLAYCONFIG_ADAPTER_NAME(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("adapterDevicePath", WCHAR * 128)
            ]

        class DISPLAYCONFIG_TARGET_BASE_TYPE(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("baseOutputTechnology", DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY)
            ]

        class _S_BPOR(CStructure):
            _fields_ = [
                ("bootPersistenceOn", UINT32, 1),
                ("reserved", UINT32, 31)
            ]
        
        class _U_SV2(Union):
            _fields_ = [
                ("s", _S_BPOR),
                ("value", UINT32)
            ]

        class DISPLAYCONFIG_SET_TARGET_PERSISTENCE(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("u", _U_SV2)
            ]

        class _S_DMVRR(CStructure):
            _fields_ = [
                ("disableMonitorVirtualResolution", UINT32, 1),
                ("reserved", UINT32, 1)
            ]
        
        class _U_SV3(Union):
            _fields_ = [
                ("s", _S_DMVRR),
                ("value", UINT32)
            ]

        class DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("u", _U_SV3)
            ]

        _DISPLAYCONFIG_COLOR_ENCODING = INT
        if True:
            DISPLAYCONFIG_COLOR_ENCODING_RGB           = 0
            DISPLAYCONFIG_COLOR_ENCODING_YCBCR444      = 1
            DISPLAYCONFIG_COLOR_ENCODING_YCBCR422      = 2
            DISPLAYCONFIG_COLOR_ENCODING_YCBCR420      = 3
            DISPLAYCONFIG_COLOR_ENCODING_INTENSITY     = 4
            DISPLAYCONFIG_COLOR_ENCODING_FORCE_UINT32  = 0xFFFFFFFF
        DISPLAYCONFIG_COLOR_ENCODING = _DISPLAYCONFIG_COLOR_ENCODING

        class _S_ACSACEWCEACFER(CStructure):
            _fields_ = [
                ("advancedColorSupported", UINT32, 1), # A type of advanced color is supported
                ("advancedColorEnabled", UINT32, 1), # A type of advanced color is enabled
                ("wideColorEnforced", UINT32, 1), # Wide color gamut is enabled
                ("advancedColorForceDisabled", UINT32, 1), # Advanced color is force disabled due to system/OS policy
                ("reserved", UINT32, 28)
            ]

        class _U_SV4(Union):
            _fields_ = [
                ("s", _S_ACSACEWCEACFER),
                ("value", UINT32)
            ]

        class _DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("u", _U_SV4),
                ("colorEncoding", DISPLAYCONFIG_COLOR_ENCODING),
                ("bitsPerColorChannel", UINT32)
            ]
        DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO = _DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO

        class _S_EACR(CStructure):
            _fields_ = [
                ("enableAdvancedColor", UINT32, 1),
                ("reserved", UINT32, 31)
            ]

        class _U_SV5(Union):
            _fields_ = [
                ("s", _S_EACR),
                ("value", UINT32)
            ]

        class _DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),
                ("u", _U_SV5)
            ]
        DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE = _DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE

        class _DISPLAYCONFIG_SDR_WHITE_LEVEL(CStructure):
            _fields_ = [
                ("header", DISPLAYCONFIG_DEVICE_INFO_HEADER),

                # SDRWhiteLevel represents a multiplier for standard SDR white
                # peak value i.e. 80 nits represented as fixed point.
                # To get value in nits use the following conversion
                # SDRWhiteLevel in nits = (SDRWhiteLevel / 1000 ) * 80
                ("SDRWhiteLevel", ULONG)
            ]
        DISPLAYCONFIG_SDR_WHITE_LEVEL = _DISPLAYCONFIG_SDR_WHITE_LEVEL

        # REGION ***


        #
        # Definitions to be used by GetDisplayConfigBufferSizes and QueryDisplayConfig.
        #

        QDC_ALL_PATHS = 0x00000001
        QDC_ONLY_ACTIVE_PATHS = 0x00000002
        QDC_DATABASE_CURRENT = 0x00000004
        QDC_VIRTUAL_MODE_AWARE = 0x00000010
        QDC_INCLUDE_HMD = 0x00000020

        #
        # Definitions used by SetDisplayConfig.
        #

        SDC_TOPOLOGY_INTERNAL = 0x00000001
        SDC_TOPOLOGY_CLONE = 0x00000002
        SDC_TOPOLOGY_EXTEND = 0x00000004
        SDC_TOPOLOGY_EXTERNAL = 0x00000008
        SDC_TOPOLOGY_SUPPLIED = 0x00000010
        SDC_USE_DATABASE_CURRENT = (SDC_TOPOLOGY_INTERNAL | SDC_TOPOLOGY_CLONE | SDC_TOPOLOGY_EXTEND | SDC_TOPOLOGY_EXTERNAL)

        SDC_USE_SUPPLIED_DISPLAY_CONFIG = 0x00000020
        SDC_VALIDATE = 0x00000040
        SDC_APPLY = 0x00000080
        SDC_NO_OPTIMIZATION = 0x00000100
        SDC_SAVE_TO_DATABASE = 0x00000200
        SDC_ALLOW_CHANGES = 0x00000400
        SDC_PATH_PERSIST_IF_REQUIRED = 0x00000800
        SDC_FORCE_MODE_ENUMERATION = 0x00001000
        SDC_ALLOW_PATH_ORDER_CHANGES = 0x00002000
        SDC_VIRTUAL_MODE_AWARE = 0x00008000

        # GetRegionData/ExtCreateRegion

        RDH_RECTANGLES = 1

        #pragma region Application Family
        #if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_SYSTEM)

        class _RGNDATAHEADER(CStructure):
            _fields_ = [
                ("dwSize", DWORD),
                ("iType", DWORD),
                ("nCount", DWORD),
                ("nRgnSize", DWORD),
                ("rcBound", RECT)
            ]
        RGNDATAHEADER = _RGNDATAHEADER
        PRGNDATAHEADER = POINTER(RGNDATAHEADER)

        class _RGNDATA(CStructure):
            _fields_ = [
                ("rdh", RGNDATAHEADER),
                ("Buffer", CHAR * 1)
            ]
        RGNDATA = _RGNDATA
        PRGNDATA = POINTER(RGNDATA)
        NPRGNDATA = PRGNDATA
        LPRGNDATA = PRGNDATA

        # REGION ***

        # for GetRandomRgn
        SYSRGN = 4


        # REGION *** Desktop Family ***

        class _ABC(CStructure):
            _fields_ = [
                ("abcA", INT),
                ("abcB", UINT),
                ("abcC", INT)
            ]
        ABC = _ABC
        PABC = POINTER(ABC)
        NPABC = PABC
        LPABC = PABC

        class _ABCFLOAT(CStructure):
            _fields_ = [
                ("abcfA", FLOAT),
                ("abcfB", FLOAT),
                ("abcfC", FLOAT)
            ]
        ABCFLOAT = _ABCFLOAT
        PABCFLOAT = POINTER(ABCFLOAT)
        NPABCFLOAT = PABCFLOAT
        LPABCFLOAT = PABCFLOAT
        
        # REGION ***

        if cpreproc.ifndef("NOTEXTMETRIC"):

            # REGION *** Desktop Family ***

            class _OUTLINETEXTMETRICA(CStructure):
                _fields_ = [
                    ("otmSize", UINT),
                    ("otmTextMetrics", TEXTMETRICA),
                    ("otmFiller", BYTE),
                    ("otmPanoseNumber", PANOSE),
                    ("otmfsSelection", UINT),
                    ("otmfsType", UINT),
                    ("otmsCharSlopeRise", INT),
                    ("otmsCharSlopeRun", INT),
                    ("otmItalicAngle", INT),
                    ("otmEMSquare", UINT),
                    ("otmAscent", INT),
                    ("otmDescent", INT),
                    ("otmLineGap", UINT),
                    ("otmsCapEmHeight", UINT),
                    ("otmsXHeight", UINT),
                    ("otmrcFontBox", RECT),
                    ("otmMacAscent", INT),
                    ("otmMacDescent", INT),
                    ("otmMacLineGap", UINT),
                    ("otmusMinimumPPEM", UINT),
                    ("otmptSubscriptSize", POINT),
                    ("otmptSubscriptOffset", POINT),
                    ("otmptSuperscriptSize", POINT),
                    ("otmptSuperscriptOffset", POINT),
                    ("otmsStrikeoutSize", UINT),
                    ("otmsStrikeoutPosition", INT),
                    ("otmsUnderscoreSize", INT),
                    ("otmsUnderscorePosition", INT),
                    ("otmpFamilyName", PSTR),
                    ("otmpFaceName", PSTR),
                    ("otmpStyleName", PSTR),
                    ("otmpFullName", PSTR)
                ]
            OUTLINETEXTMETRICA = _OUTLINETEXTMETRICA
            POUTLINETEXTMETRICA = POINTER(OUTLINETEXTMETRICA)
            NPOUTLINETEXTMETRICA = POUTLINETEXTMETRICA
            LPOUTLINETEXTMETRICA = POUTLINETEXTMETRICA


            class _OUTLINETEXTMETRICW(CStructure):
                _fields_ = [
                    ("otmSize", UINT),
                    ("otmTextMetrics", TEXTMETRICW),
                    ("otmFiller", BYTE),
                    ("otmPanoseNumber", PANOSE),
                    ("otmfsSelection", UINT),
                    ("otmfsType", UINT),
                    ("otmsCharSlopeRise", INT),
                    ("otmsCharSlopeRun", INT),
                    ("otmItalicAngle", INT),
                    ("otmEMSquare", UINT),
                    ("otmAscent", INT),
                    ("otmDescent", INT),
                    ("otmLineGap", UINT),
                    ("otmsCapEmHeight", UINT),
                    ("otmsXHeight", UINT),
                    ("otmrcFontBox", RECT),
                    ("otmMacAscent", INT),
                    ("otmMacDescent", INT),
                    ("otmMacLineGap", UINT),
                    ("otmusMinimumPPEM", UINT),
                    ("otmptSubscriptSize", POINT),
                    ("otmptSubscriptOffset", POINT),
                    ("otmptSuperscriptSize", POINT),
                    ("otmptSuperscriptOffset", POINT),
                    ("otmsStrikeoutSize", UINT),
                    ("otmsStrikeoutPosition", INT),
                    ("otmsUnderscoreSize", INT),
                    ("otmsUnderscorePosition", INT),
                    ("otmpFamilyName", PSTR),
                    ("otmpFaceName", PSTR),
                    ("otmpStyleName", PSTR),
                    ("otmpFullName", PSTR)
                ]
            OUTLINETEXTMETRICW = _OUTLINETEXTMETRICW
            POUTLINETEXTMETRICW = POINTER(OUTLINETEXTMETRICW)
            NPOUTLINETEXTMETRICW = POUTLINETEXTMETRICW
            LPOUTLINETEXTMETRICW = POUTLINETEXTMETRICW
            
            OUTLINETEXTMETRIC = unicode(OUTLINETEXTMETRICW, OUTLINETEXTMETRICA)
            POUTLINETEXTMETRIC = unicode(POUTLINETEXTMETRICW, POUTLINETEXTMETRICA)
            NPOUTLINETEXTMETRIC = unicode(NPOUTLINETEXTMETRICW, NPOUTLINETEXTMETRICA)
            LPOUTLINETEXTMETRIC = unicode(LPOUTLINETEXTMETRICW, LPOUTLINETEXTMETRICA)

            # REGION ***
        # NOTEXTMETRIC

        # REGION *** Application Family ***

        class tagPOLYTEXTA(CStructure):
            _fields_ = [
                ("x", INT),
                ("y", INT),
                ("n", UINT),
                ("lpstr", LPCSTR),
                ("uiFlags", UINT),
                ("rcl", RECT),
                ("pdx", PINT)
            ]
        POLYTEXTA = tagPOLYTEXTA
        PPOLYTEXTA = POINTER(POLYTEXTA)
        NPPOLYTEXTA = PPOLYTEXTA
        LPPOLYTEXTA = PPOLYTEXTA

        class tagPOLYTEXTW(CStructure):
            _fields_ = [
                ("x", INT),
                ("y", INT),
                ("n", UINT),
                ("lpstr", LPCWSTR),
                ("uiFlags", UINT),
                ("rcl", RECT),
                ("pdx", PINT)
            ]
        POLYTEXTW = tagPOLYTEXTW
        PPOLYTEXTW = POINTER(POLYTEXTW)
        NPPOLYTEXTW = PPOLYTEXTW
        LPPOLYTEXTW = PPOLYTEXTW

        POLYTEXT = unicode(POLYTEXTW, POLYTEXTA)
        PPOLYTEXT = unicode(PPOLYTEXTW, PPOLYTEXTA)
        NPPOLYTEXT = unicode(NPPOLYTEXTW, NPPOLYTEXTA)
        LPPOLYTEXT = unicode(LPPOLYTEXTW, LPPOLYTEXTA)

        # REGION *** 

        # REGION *** Desktop Family ***

        class _FIXED(CStructure):
            _fields_ = [
                ("value", SHORT),
                ("fract", WORD)
            ]
        FIXED = _FIXED

        class _MAT2(CStructure):
            _fields_ = [
                ("eM11", FIXED),
                ("eM12", FIXED),
                ("eM21", FIXED),
                ("eM22", FIXED)
            ]
        MAT2 = _MAT2
        LPMAT2 = POINTER(MAT2)
        PMAT2 = LPMAT2

        class _GLYPHMETRICS(CStructure):
            _fields_ = [
                ("gmBlackBoxX", UINT),
                ("gmBlackBoxY", UINT),
                ("gmptGlyphOrigin", POINT),
                ("gmCellIncX", SHORT),
                ("gmCellIncY", SHORT)
            ]
        GLYPHMETRICS = _GLYPHMETRICS
        LPGLYPHMETRICS = POINTER(GLYPHMETRICS)

        # REGION ***

        #  GetGlyphOutline constants
        GGO_METRICS = 0
        GGO_BITMAP = 1
        GGO_NATIVE = 2
        GGO_BEZIER = 3
        GGO_GRAY2_BITMAP = 4
        GGO_GRAY4_BITMAP = 5
        GGO_GRAY8_BITMAP = 6
        GGO_GLYPH_INDEX = 0x0080
        GGO_UNHINTED = 0x0100
        TT_POLYGON_TYPE = 24
        TT_PRIM_LINE = 1
        TT_PRIM_QSPLINE = 2
        TT_PRIM_CSPLINE = 3

        # REGION *** Desktop Family ***

        class tagPOINTFX(CStructure):
            _fields_ = [
                ("x", FIXED),
                ("y", FIXED)
            ]
        POINTFX = tagPOINTFX
        LPPOINTFX = POINTER(POINTFX)

        class tagTTPOLYCURVE(CStructure):
            _fields_ = [
                ("wType", WORD),
                ("cpfx", WORD),
                ("apfx", POINTFX * 1)
            ]
        TTPOLYCURVE = tagTTPOLYCURVE
        LPTTPOLYCURVE = POINTER(TTPOLYCURVE)

        class tagTTPOLYGONHEADER(CStructure):
            _fields_ = [
                ("cb", DWORD),
                ("dwType", DWORD),
                ("pfxStart", POINTFX)
            ]
        TTPOLYGONHEADER = tagTTPOLYGONHEADER
        LPTTPOLYGONHEADER = POINTER(TTPOLYGONHEADER)

        # REGION ***

        GCP_DBCS = 0x0001
        GCP_REORDER = 0x0002
        GCP_USEKERNING = 0x0008
        GCP_GLYPHSHAPE = 0x0010
        GCP_LIGATE = 0x0020
        GCP_GLYPHINDEXING = 0x0080
        GCP_DIACRITIC = 0x0100
        GCP_KASHIDA = 0x0400
        GCP_ERROR = 0x8000
        FLI_MASK = 0x103B
        GCP_JUSTIFY = 0x00010000
        GCP_NODIACRITICS = 0x00020000
        FLI_GLYPHS = 0x00040000
        GCP_CLASSIN = 0x00080000
        GCP_MAXEXTENT = 0x00100000
        GCP_JUSTIFYIN = 0x00200000
        GCP_DISPLAYZWG = 0x00400000
        GCP_SYMSWAPOFF = 0x00800000
        GCP_NUMERICOVERRIDE = 0x01000000
        GCP_NEUTRALOVERRIDE = 0x02000000
        GCP_NUMERICSLATIN = 0x04000000
        GCP_NUMERICSLOCAL = 0x08000000
        GCPCLASS_LATIN = 1
        GCPCLASS_HEBREW = 2
        GCPCLASS_ARABIC = 2
        GCPCLASS_NEUTRAL = 3
        GCPCLASS_LOCALNUMBER = 4
        GCPCLASS_LATINNUMBER = 5
        GCPCLASS_LATINNUMERICTERMINATOR = 6
        GCPCLASS_LATINNUMERICSEPARATOR = 7
        GCPCLASS_NUMERICSEPARATOR = 8
        GCPCLASS_PREBOUNDLTR = 0x80
        GCPCLASS_PREBOUNDRTL = 0x40
        GCPCLASS_POSTBOUNDLTR = 0x20
        GCPCLASS_POSTBOUNDRTL = 0x10
        GCPGLYPH_LINKBEFORE = 0x8000
        GCPGLYPH_LINKAFTER = 0x4000

        # REGION *** Desktop Family ***

        class tagGCP_RESULTSA(CStructure):
            _fields_ = [
                ("lStructSize", DWORD),
                ("lpOutString", LPSTR),
                ("lpOrder", LPUINT),
                ("lpDx", LPINT),
                ("lpCaretPos", LPINT),
                ("lpClass", LPSTR),
                ("lpGlyphs", LPWSTR),
                ("nGlyphs", UINT),
                ("nMaxFit", INT)
            ]
        GCP_RESULTSA = tagGCP_RESULTSA
        LPGCP_RESULTSA = POINTER(GCP_RESULTSA)

        class tagGCP_RESULTSW(CStructure):
            _fields_ = [
                ("lStructSize", DWORD),
                ("lpOutString", LPWSTR),
                ("lpOrder", LPUINT),
                ("lpDx", LPINT),
                ("lpCaretPos", LPINT),
                ("lpClass", LPSTR),
                ("lpGlyphs", LPWSTR),
                ("nGlyphs", UINT),
                ("nMaxFit", INT)
            ]
        GCP_RESULTSW = tagGCP_RESULTSW
        LPGCP_RESULTSW = POINTER(GCP_RESULTSW)

        GCP_RESULT = unicode(GCP_RESULTSW, GCP_RESULTSA)
        LPGCP_RESULT = unicode(LPGCP_RESULTSW, LPGCP_RESULTSA)

        # REGION ***
                               
        # REGION *** Desktop Family ***

        class _RASTERIZER_STATUS(CStructure):
            _fields_ = [
                ("nSize", SHORT),
                ("wFlags", SHORT),
                ("nLanguageID", SHORT)
            ]
        RASTERIZER_STATUS = _RASTERIZER_STATUS
        LPRASTERIZER_STATUS = POINTER(RASTERIZER_STATUS)

        # REGION ***

        # bits defined in wFlags of RASTERIZER_STATUS
        TT_AVAILABLE = 0x0001
        TT_ENABLED = 0x0002

        # REGION *** Application Family ***

        # Pixel format descriptor
        class tagPIXELFORMATDESCRIPTOR(CStructure):
            _fields_ = [
                ("nSize", WORD),
                ("nVersion", WORD),
                ("dwFlags", DWORD),
                ("iPixelType", BYTE),
                ("cColorBits", BYTE),
                ("cRedBits", BYTE),
                ("cRedShift", BYTE),
                ("cGreenBits", BYTE),
                ("cGreenShift", BYTE),
                ("cBlueBits", BYTE),
                ("cBlueShift", BYTE),
                ("cAlphaBits", BYTE),
                ("cAlphaShift", BYTE),
                ("cAccumBits", BYTE),
                ("cAccumRedBits", BYTE),
                ("cAccumGreenBits", BYTE),
                ("cAccumBlueBits", BYTE),
                ("cAccumAlphaBits", BYTE),
                ("cDepthBits", BYTE),
                ("cStencilBits", BYTE),
                ("cAuxBuffers", BYTE),
                ("iLayerType", BYTE),
                ("bReserved", BYTE),
                ("dwLayerMask", DWORD),
                ("dwVisibleMask", DWORD),
                ("dwDamageMask", DWORD)
            ]
        PIXELFORMATDESCRIPTOR = tagPIXELFORMATDESCRIPTOR
        PPIXELFORMATDESCRIPTOR = POINTER(PIXELFORMATDESCRIPTOR)
        LPPIXELFORMATDESCRIPTOR = PPIXELFORMATDESCRIPTOR

        # REGION ***

        # pixel types
        PFD_TYPE_RGBA = 0
        PFD_TYPE_COLORINDEX = 1
        # layer types
        PFD_MAIN_PLANE = 0
        PFD_OVERLAY_PLANE = 1
        PFD_UNDERLAY_PLANE = (-1)
        # PIXELFORMATDESCRIPTOR flags
        PFD_DOUBLEBUFFER = 0x00000001
        PFD_STEREO = 0x00000002
        PFD_DRAW_TO_WINDOW = 0x00000004
        PFD_DRAW_TO_BITMAP = 0x00000008
        PFD_SUPPORT_GDI = 0x00000010
        PFD_SUPPORT_OPENGL = 0x00000020
        PFD_GENERIC_FORMAT = 0x00000040
        PFD_NEED_PALETTE = 0x00000080
        PFD_NEED_SYSTEM_PALETTE = 0x00000100
        PFD_SWAP_EXCHANGE = 0x00000200
        PFD_SWAP_COPY = 0x00000400
        PFD_SWAP_LAYER_BUFFERS = 0x00000800
        PFD_GENERIC_ACCELERATED = 0x00001000
        PFD_SUPPORT_DIRECTDRAW = 0x00002000
        PFD_DIRECT3D_ACCELERATED = 0x00004000
        PFD_SUPPORT_COMPOSITION = 0x00008000
        # PIXELFORMATDESCRIPTOR flags for use in ChoosePixelFormat only
        PFD_DEPTH_DONTCARE = 0x20000000
        PFD_DOUBLEBUFFER_DONTCARE = 0x40000000
        PFD_STEREO_DONTCARE = 0x80000000

        # REGION *** Desktop Family ***

        OLDFONTENUMPROCA = CALLBACK(INT, PLOGFONTA, PTEXTMETRICA, DWORD, LPARAM)
        OLDFONTENUMPROCW = CALLBACK(INT, PLOGFONTW, PTEXTMETRICW, DWORD, LPARAM)
        OLDFONTENUMPROC = unicode(OLDFONTENUMPROCW, OLDFONTENUMPROCA)

        FONTENUMPROCA = OLDFONTENUMPROCA
        FONTENUMPROCW = OLDFONTENUMPROCW
        FONTENUMPROC = unicode(FONTENUMPROCW, FONTENUMPROCA)

        GOBJENUMPROC = CALLBACK(INT, LPVOID, LPARAM)
        LINEDDAPROC = CALLBACK(VOID, INT, INT, LPARAM)

        # REGION ***

        # REGION *** Desktop Family ***

        AddFontResourceA = declare(gdi32.AddFontResourceA, INT, LPCSTR)
        AddFontResourceW = declare(gdi32.AddFontResourceW, INT, LPCWSTR)
        AddFontResource = unicode(AddFontResourceW, AddFontResourceA)
        AnimatePalette = declare(gdi32.AnimatePalette, BOOL, HPALETTE, UINT, UINT, PPALETTEENTRY)
        Arc = declare(gdi32.Arc, BOOL, HDC, INT, INT, INT, INT, INT, INT, INT, INT)
        BitBlt = declare(gdi32.BitBlt, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, DWORD)
        CancelDC = declare(gdi32.CancelDC, BOOL, HDC)
        Chord = declare(gdi32.Chord, BOOL, HDC, INT, INT, INT, INT, INT, INT, INT, INT)
        ChoosePixelFormat = declare(gdi32.ChoosePixelFormat, INT, HDC, PPIXELFORMATDESCRIPTOR)
        CloseMetaFile = declare(gdi32.CloseMetaFile, HMETAFILE, HDC)
        CombineRgn = declare(gdi32.CombineRgn, INT, HRGN, HRGN, HRGN, INT)
        CopyMetaFileA = declare(gdi32.CopyMetaFileA, HMETAFILE, HMETAFILE, LPCSTR)
        CopyMetaFileW = declare(gdi32.CopyMetaFileW, HMETAFILE, HMETAFILE, LPCWSTR)
        CopyMetaFile = unicode(CopyMetaFileW, CopyMetaFileA)
        
        CreateBitmap = declare(gdi32.CreateBitmap, HBITMAP, INT, INT, UINT, UINT, PVOID)
        CreateBitmapIndirect = declare(gdi32.CreateBitmapIndirect, HBITMAP, PBITMAP)
        CreateBrushIndirect = declare(gdi32.CreateBrushIndirect, HBRUSH, PLOGBRUSH)
        CreateCompatibleBitmap = declare(gdi32.CreateCompatibleBitmap, HBITMAP, HDC, INT, INT)
        CreateDiscardableBitmap = declare(gdi32.CreateDiscardableBitmap, HBITMAP, HDC, INT, INT)
        CreateCompatibleDC = declare(gdi32.CreateCompatibleDC, HDC, HDC)
        CreateDCA = declare(gdi32.CreateDCA, HDC, LPCSTR, LPCSTR, LPCSTR, PDEVMODEA)
        CreateDCW = declare(gdi32.CreateDCW, HDC, LPCWSTR, LPCWSTR, LPCWSTR, PDEVMODEW)
        CreateDC = unicode(CreateDCW, CreateDCA)
        
        CreateDIBitmap = declare(gdi32.CreateDIBitmap, HBITMAP, HDC, DWORD, PVOID, UINT)
        CreateDIBPatternBrush = declare(gdi32.CreateDIBPatternBrush, HBRUSH, HGLOBAL, UINT)
        CreateDIBPatternBrushPt = declare(gdi32.CreateDIBPatternBrushPt, HBRUSH, PVOID, UINT)
        CreateEllipticRgn = declare(gdi32.CreateEllipticRgn, HRGN, INT, INT, INT, INT)
        CreateEllipticRgnIndirect = declare(gdi32.CreateEllipticRgnIndirect, HRGN, PRECT)
        CreateFontIndirectA = declare(gdi32.CreateFontIndirectA, HFONT, PLOGFONTA)
        CreateFontIndirectW = declare(gdi32.CreateFontIndirectW, HFONT, PLOGFONTW)
        CreateFontIndirect = unicode(CreateFontIndirectW, CreateFontIndirectA)
        
        CreateFontA = declare(gdi32.CreateFontA, HFONT, INT, INT, INT, INT, INT, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, LPCSTR)
        CreateFontW = declare(gdi32.CreateFontW, HFONT, INT, INT, INT, INT, INT, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, LPCWSTR)
        CreateFont = unicode(CreateFontW, CreateFontA)
        
        CreateHatchBrush = declare(gdi32.CreateHatchBrush, HBRUSH, INT, COLORREF)
        CreateICA = declare(gdi32.CreateICA, HDC, LPCSTR, LPCSTR, LPCSTR, PDEVMODEA)
        CreateICW = declare(gdi32.CreateICW, HDC, LPCWSTR, LPCWSTR, LPCWSTR, PDEVMODEW)
        CreateIC = unicode(CreateICW, CreateICA)
        
        CreateMetaFileA = declare(gdi32.CreateMetaFileA, HDC, LPCSTR)
        CreateMetaFileW = declare(gdi32.CreateMetaFileW, HDC, LPCWSTR)
        CreateMetaFile = unicode(CreateMetaFileW, CreateMetaFileA)
        
        CreatePalette = declare(gdi32.CreatePalette, HPALETTE, PLOGPALETTE)
        CreatePen = declare(gdi32.CreatePen, HPEN, INT, INT, COLORREF)
        CreatePenIndirect = declare(gdi32.CreatePenIndirect, HPEN, PLOGPEN)
        CreatePolyPolygonRgn = declare(gdi32.CreatePolyPolygonRgn, HRGN, PPOINT, PINT, INT, INT)
        CreatePatternBrush = declare(gdi32.CreatePatternBrush, HBRUSH, HBITMAP)
        CreateRectRgn = declare(gdi32.CreateRectRgn, HRGN, INT, INT, INT, INT)
        CreateRectRgnIndirect = declare(gdi32.CreateRectRgnIndirect, HRGN, PRECT)
        CreateRoundRectRgn = declare(gdi32.CreateRoundRectRgn, HRGN, INT, INT, INT, INT, INT, INT)
        CreateScalableFontResourceA = declare(gdi32.CreateScalableFontResourceA, BOOL, DWORD, LPCSTR, LPCSTR, LPCSTR)
        CreateScalableFontResourceW = declare(gdi32.CreateScalableFontResourceW, BOOL, DWORD, LPCWSTR, LPCWSTR, LPCWSTR)
        CreateScalableFontResource = unicode(CreateScalableFontResourceW, CreateScalableFontResourceA)
        
        CreateSolidBrush = declare(gdi32.CreateSolidBrush, HBRUSH, COLORREF)
        DeleteDC = declare(gdi32.DeleteDC, BOOL, HDC)
        DeleteMetaFile = declare(gdi32.DeleteMetaFile, BOOL, HMETAFILE)
        DeleteObject = declare(gdi32.DeleteObject, BOOL, HGDIOBJ)
        DescribePixelFormat = declare(gdi32.DescribePixelFormat, INT, HDC, INT, UINT, LPPIXELFORMATDESCRIPTOR)

        """
        define types of pointers to ExtDeviceMode() and DeviceCapabilities()
        * functions for Win 3.1 compatibility

        """

        LPFNDEVMODE = CALLBACK(UINT, HWND, HMODULE, LPDEVMODE, LPSTR, LPSTR, LPDEVMODE, LPSTR, UINT)
        LPFNDEVCAPS = CALLBACK(DWORD, LPSTR, LPSTR, UINT, LPSTR, LPDEVMODE)

        # REGION ***

        # mode selections for the device mode function
        DM_UPDATE = 1
        DM_COPY = 2
        DM_PROMPT = 4
        DM_MODIFY = 8
        DM_IN_BUFFER = DM_MODIFY
        DM_IN_PROMPT = DM_PROMPT
        DM_OUT_BUFFER = DM_COPY
        DM_OUT_DEFAULT = DM_UPDATE
        # device capabilities indices
        DC_FIELDS = 1
        DC_PAPERS = 2
        DC_PAPERSIZE = 3
        DC_MINEXTENT = 4
        DC_MAXEXTENT = 5
        DC_BINS = 6
        DC_DUPLEX = 7
        DC_SIZE = 8
        DC_EXTRA = 9
        DC_VERSION = 10
        DC_DRIVER = 11
        DC_BINNAMES = 12
        DC_ENUMRESOLUTIONS = 13
        DC_FILEDEPENDENCIES = 14
        DC_TRUETYPE = 15
        DC_PAPERNAMES = 16
        DC_ORIENTATION = 17
        DC_COPIES = 18
        DC_BINADJUST = 19
        DC_EMF_COMPLIANT = 20
        DC_DATATYPE_PRODUCED = 21
        DC_COLLATE = 22
        DC_MANUFACTURER = 23
        DC_MODEL = 24
        DC_PERSONALITY = 25
        DC_PRINTRATE = 26
        DC_PRINTRATEUNIT = 27
        PRINTRATEUNIT_PPM = 1
        PRINTRATEUNIT_CPS = 2
        PRINTRATEUNIT_LPM = 3
        PRINTRATEUNIT_IPM = 4
        DC_PRINTERMEM = 28
        DC_MEDIAREADY = 29
        DC_STAPLE = 30
        DC_PRINTRATEPPM = 31
        DC_COLORDEVICE = 32
        DC_NUP = 33
        DC_MEDIATYPENAMES = 34
        DC_MEDIATYPES = 35
        # bit fields of the return value (DWORD) for DC_TRUETYPE
        DCTT_BITMAP = 0x0000001
        DCTT_DOWNLOAD = 0x0000002
        DCTT_SUBDEV = 0x0000004
        DCTT_DOWNLOAD_OUTLINE = 0x0000008
        # return values for DC_BINADJUST
        DCBA_FACEUPNONE = 0x0000
        DCBA_FACEUPCENTER = 0x0001
        DCBA_FACEUPLEFT = 0x0002
        DCBA_FACEUPRIGHT = 0x0003
        DCBA_FACEDOWNNONE = 0x0100
        DCBA_FACEDOWNCENTER = 0x0101
        DCBA_FACEDOWNLEFT = 0x0102
        DCBA_FACEDOWNRIGHT = 0x0103

        # REGION *** Desktop Family ***

        DeviceCapabilitiesA = declare(winspool.DeviceCapabilitiesA, INT, LPCSTR, LPCSTR, WORD, LPSTR, PDEVMODEA)
        DeviceCapabilitiesW = declare(winspool.DeviceCapabilitiesW, INT, LPCWSTR, LPCWSTR, WORD, LPWSTR, PDEVMODEW)
        DeviceCapabilities = unicode(DeviceCapabilitiesW, DeviceCapabilitiesA)
        # !UNICODE
        DrawEscape = declare(gdi32.DrawEscape, INT, HDC, INT, INT, LPCSTR)
        Ellipse = declare(gdi32.Ellipse, BOOL, HDC, INT, INT, INT, INT)
        EnumFontFamiliesExA = declare(gdi32.EnumFontFamiliesExA, INT, HDC, LPLOGFONTA, FONTENUMPROCA, LPARAM, DWORD)
        EnumFontFamiliesExW = declare(gdi32.EnumFontFamiliesExW, INT, HDC, LPLOGFONTW, FONTENUMPROCW, LPARAM, DWORD)
        EnumFontFamiliesEx = unicode(EnumFontFamiliesExW, EnumFontFamiliesExA)
        # WINVER >= 0x0400
        EnumFontFamiliesA = declare(gdi32.EnumFontFamiliesA, INT, HDC, LPCSTR, FONTENUMPROCA, LPARAM)
        EnumFontFamiliesW = declare(gdi32.EnumFontFamiliesW, INT, HDC, LPCWSTR, FONTENUMPROCW, LPARAM)
        EnumFontFamilies = unicode(EnumFontFamiliesW, EnumFontFamiliesA)
        # !UNICODE
        EnumFontsA = declare(gdi32.EnumFontsA, INT, HDC, LPCSTR, FONTENUMPROCA, LPARAM)
        EnumFontsW = declare(gdi32.EnumFontsW, INT, HDC, LPCWSTR, FONTENUMPROCW, LPARAM)
        EnumFonts = unicode(EnumFontsW, EnumFontsA)
        # !UNICODE
        EnumObjects = declare(gdi32.EnumObjects, INT, HDC, INT, GOBJENUMPROC, LPARAM)
        EqualRgn = declare(gdi32.EqualRgn, BOOL, HRGN, HRGN)
        Escape = declare(gdi32.Escape, INT, HDC, INT, INT, LPCSTR, LPVOID)
        ExtEscape = declare(gdi32.ExtEscape, INT, HDC, INT, INT, LPCSTR, INT, LPSTR)
        ExcludeClipRect = declare(gdi32.ExcludeClipRect, INT, HDC, INT, INT, INT, INT)
        ExtCreateRegion = declare(gdi32.ExtCreateRegion, HRGN, PXFORM, DWORD, PRGNDATA)
        ExtFloodFill = declare(gdi32.ExtFloodFill, BOOL, HDC, INT, INT, COLORREF, UINT)
        FillRgn = declare(gdi32.FillRgn, BOOL, HDC, HRGN, HBRUSH)
        FloodFill = declare(gdi32.FloodFill, BOOL, HDC, INT, INT, COLORREF)
        FrameRgn = declare(gdi32.FrameRgn, BOOL, HDC, HRGN, HBRUSH, INT, INT)
        GetROP2 = declare(gdi32.GetROP2, INT, HDC)
        GetAspectRatioFilterEx = declare(gdi32.GetAspectRatioFilterEx, BOOL, HDC, LPSIZE)
        GetBkColor = declare(gdi32.GetBkColor, COLORREF, HDC)
        GetDCBrushColor = declare(gdi32.GetDCBrushColor, COLORREF, HDC)
        GetDCPenColor = declare(gdi32.GetDCPenColor, COLORREF, HDC)
        GetBkMode = declare(gdi32.GetBkMode, INT, HDC)
        GetBitmapBits = declare(gdi32.GetBitmapBits, LONG, HBITMAP, LONG, LPVOID)
        GetBitmapDimensionEx = declare(gdi32.GetBitmapDimensionEx, BOOL, HBITMAP, LPSIZE)
        GetBoundsRect = declare(gdi32.GetBoundsRect, UINT, HDC, LPRECT, UINT)
        GetBrushOrgEx = declare(gdi32.GetBrushOrgEx, BOOL, HDC, LPPOINT)
        GetCharWidthA = declare(gdi32.GetCharWidthA, BOOL, HDC, UINT, UINT, LPINT)
        GetCharWidthW = declare(gdi32.GetCharWidthW, BOOL, HDC, UINT, UINT, LPINT)
        GetCharWidth = unicode(GetCharWidthW, GetCharWidthA)
        # !UNICODE
        GetCharWidth32A = declare(gdi32.GetCharWidth32A, BOOL, HDC, UINT, UINT, LPINT)
        GetCharWidth32W = declare(gdi32.GetCharWidth32W, BOOL, HDC, UINT, UINT, LPINT)
        GetCharWidth32 = unicode(GetCharWidth32W, GetCharWidth32A)
        # !UNICODE
        GetCharWidthFloatA = declare(gdi32.GetCharWidthFloatA, BOOL, HDC, UINT, UINT, PFLOAT)
        GetCharWidthFloatW = declare(gdi32.GetCharWidthFloatW, BOOL, HDC, UINT, UINT, PFLOAT)
        GetCharWidthFloat = unicode(GetCharWidthFloatW, GetCharWidthFloatA)
        # !UNICODE
        GetCharABCWidthsA = declare(gdi32.GetCharABCWidthsA, BOOL, HDC, UINT, UINT, LPABC)
        GetCharABCWidthsW = declare(gdi32.GetCharABCWidthsW, BOOL, HDC, UINT, UINT, LPABC)
        GetCharABCWidths = unicode(GetCharABCWidthsW, GetCharABCWidthsA)
        # !UNICODE
        GetCharABCWidthsFloatA = declare(gdi32.GetCharABCWidthsFloatA, BOOL, HDC, UINT, UINT, LPABCFLOAT)
        GetCharABCWidthsFloatW = declare(gdi32.GetCharABCWidthsFloatW, BOOL, HDC, UINT, UINT, LPABCFLOAT)
        GetCharABCWidthsFloat = unicode(GetCharABCWidthsFloatW, GetCharABCWidthsFloatA)
        # !UNICODE
        GetClipBox = declare(gdi32.GetClipBox, INT, HDC, LPRECT)
        GetClipRgn = declare(gdi32.GetClipRgn, INT, HDC, HRGN)
        GetMetaRgn = declare(gdi32.GetMetaRgn, INT, HDC, HRGN)
        GetCurrentObject = declare(gdi32.GetCurrentObject, HGDIOBJ, HDC, UINT)
        GetCurrentPositionEx = declare(gdi32.GetCurrentPositionEx, BOOL, HDC, LPPOINT)
        GetDeviceCaps = declare(gdi32.GetDeviceCaps, INT, HDC, INT)
        GetDIBits = declare(gdi32.GetDIBits, INT, HDC, HBITMAP, UINT, UINT, LPVOID, UINT)
        GetGlyphOutlineA = declare(gdi32.GetGlyphOutlineA, DWORD, HDC, UINT, UINT, LPGLYPHMETRICS, DWORD, LPVOID, PMAT2)
        GetGlyphOutlineW = declare(gdi32.GetGlyphOutlineW, DWORD, HDC, UINT, UINT, LPGLYPHMETRICS, DWORD, LPVOID, PMAT2)
        GetGlyphOutline = unicode(GetGlyphOutlineW, GetGlyphOutlineA)
        # !UNICODE
        GetGraphicsMode = declare(gdi32.GetGraphicsMode, INT, HDC)
        GetMapMode = declare(gdi32.GetMapMode, INT, HDC)
        GetMetaFileBitsEx = declare(gdi32.GetMetaFileBitsEx, UINT, HMETAFILE, UINT, LPVOID)
        GetMetaFileA = declare(gdi32.GetMetaFileA, HMETAFILE, LPCSTR)
        GetMetaFileW = declare(gdi32.GetMetaFileW, HMETAFILE, LPCWSTR)
        GetMetaFile = unicode(GetMetaFileW, GetMetaFileA)
        # !UNICODE
        GetNearestColor = declare(gdi32.GetNearestColor, COLORREF, HDC, COLORREF)
        GetNearestPaletteIndex = declare(gdi32.GetNearestPaletteIndex, UINT, HPALETTE, COLORREF)
        GetObjectType = declare(gdi32.GetObjectType, DWORD, HGDIOBJ)
        if cpreproc.ifndef("NOTEXTMETRIC"):
                GetOutlineTextMetricsA = declare(gdi32.GetOutlineTextMetricsA, UINT, HDC, UINT, LPOUTLINETEXTMETRICA)
                GetOutlineTextMetricsW = declare(gdi32.GetOutlineTextMetricsW, UINT, HDC, UINT, LPOUTLINETEXTMETRICW)
        GetOutlineTextMetrics = unicode(GetOutlineTextMetricsW, GetOutlineTextMetricsA)
        # !UNICODE
        # NOTEXTMETRIC
        GetPaletteEntries = declare(gdi32.GetPaletteEntries, UINT, HPALETTE, UINT, UINT, LPPALETTEENTRY)
        GetPixel = declare(gdi32.GetPixel, COLORREF, HDC, INT, INT)
        GetPixelFormat = declare(gdi32.GetPixelFormat, INT, HDC)
        GetPolyFillMode = declare(gdi32.GetPolyFillMode, INT, HDC)
        GetRasterizerCaps = declare(gdi32.GetRasterizerCaps, BOOL, LPRASTERIZER_STATUS, UINT)
        GetRegionData = declare(gdi32.GetRegionData, DWORD, HRGN, DWORD, LPRGNDATA)
        GetRgnBox = declare(gdi32.GetRgnBox, INT, HRGN, LPRECT)
        GetStockObject = declare(gdi32.GetStockObject, HGDIOBJ, INT)
        GetStretchBltMode = declare(gdi32.GetStretchBltMode, INT, HDC)
        GetSystemPaletteEntries = declare(gdi32.GetSystemPaletteEntries, UINT, HDC, UINT, UINT, LPPALETTEENTRY)
        GetSystemPaletteUse = declare(gdi32.GetSystemPaletteUse, UINT, HDC)
        GetTextCharacterExtra = declare(gdi32.GetTextCharacterExtra, INT, HDC)
        GetTextAlign = declare(gdi32.GetTextAlign, UINT, HDC)
        GetTextColor = declare(gdi32.GetTextColor, COLORREF, HDC)
        GetTextExtentPointA = declare(gdi32.GetTextExtentPointA, BOOL, HDC, LPCSTR, INT, LPSIZE)
        GetTextExtentPointW = declare(gdi32.GetTextExtentPointW, BOOL, HDC, LPCWSTR, INT, LPSIZE)
        GetTextExtentPoint = unicode(GetTextExtentPointW, GetTextExtentPointA)
        # !UNICODE
        GetTextExtentPoint32A = declare(gdi32.GetTextExtentPoint32A, BOOL, HDC, LPCSTR, INT, LPSIZE)
        GetTextExtentPoint32W = declare(gdi32.GetTextExtentPoint32W, BOOL, HDC, LPCWSTR, INT, LPSIZE)
        GetTextExtentPoint32 = unicode(GetTextExtentPoint32W, GetTextExtentPoint32A)
        # !UNICODE
        GetTextExtentExPointA = declare(gdi32.GetTextExtentExPointA, BOOL, HDC, LPCSTR, INT, INT, LPINT, LPINT, LPSIZE)
        GetTextExtentExPointW = declare(gdi32.GetTextExtentExPointW, BOOL, HDC, LPCWSTR, INT, INT, LPINT, LPINT, LPSIZE)
        GetTextExtentExPoint = unicode(GetTextExtentExPointW, GetTextExtentExPointA)
        # !UNICODE
        GetTextCharset = declare(gdi32.GetTextCharset, INT, HDC)
        GetTextCharsetInfo = declare(gdi32.GetTextCharsetInfo, INT, HDC, LPFONTSIGNATURE, DWORD)
        TranslateCharsetInfo = declare(gdi32.TranslateCharsetInfo, BOOL, PDWORD, LPCHARSETINFO, DWORD)
        GetFontLanguageInfo = declare(gdi32.GetFontLanguageInfo, DWORD, HDC)
        GetCharacterPlacementA = declare(gdi32.GetCharacterPlacementA, DWORD, HDC, LPCSTR, INT, INT, LPGCP_RESULTSA, DWORD)
        GetCharacterPlacementW = declare(gdi32.GetCharacterPlacementW, DWORD, HDC, LPCWSTR, INT, INT, LPGCP_RESULTSW, DWORD)
        GetCharacterPlacement = unicode(GetCharacterPlacementW, GetCharacterPlacementA)
        # WINVER >= 0x0400
        # _FAMILY_PARTITION(_PARTITION_DESKTOP)

        # REGION ***

        # REGION *** Desktop Family ***

        class tagWCRANGE(CStructure):
            _fields_ = [
                ("wcLow", WCHAR),
                ("cGlyphs", USHORT)
            ]
        WCRANGE = tagWCRANGE
        PWCRANGE = POINTER(WCRANGE)
        LPWCRANGE = PWCRANGE


        class tagGLYPHSET(CStructure):
            _fields_ = [
                ("cbThis", DWORD),
                ("flAccel", DWORD),
                ("cGlyphsSupported", DWORD),
                ("cRanges", DWORD),
                ("ranges", WCRANGE * 1)
            ]
        GLYPHSET = tagGLYPHSET
        PGLYPHSET = POINTER(GLYPHSET)
        LPGLYPHSET = PGLYPHSET

        # flAccel flags for the GLYPHSET structure above

        GS_8BIT_INDICES = 0x00000001

        # flags for GetGlyphIndices

        GGI_MARK_NONEXISTING_GLYPHS = 0x0001

        # REGION ***

        GetFontUnicodeRanges = declare(gdi32.GetFontUnicodeRanges, DWORD, HDC, LPGLYPHSET)
        GetGlyphIndicesA = declare(gdi32.GetGlyphIndicesA, DWORD, HDC, LPCSTR, INT, LPWORD, DWORD)
        GetGlyphIndicesW = declare(gdi32.GetGlyphIndicesW, DWORD, HDC, LPCWSTR, INT, LPWORD, DWORD)
        GetGlyphIndices = unicode(GetGlyphIndicesW, GetGlyphIndicesA)
        # !UNICODE
        GetTextExtentPointI = declare(gdi32.GetTextExtentPointI, BOOL, HDC, LPWORD, INT, LPSIZE)
        GetCharWidthI = declare(gdi32.GetCharWidthI, BOOL, HDC, UINT, UINT, LPWORD, LPINT)
        GetCharABCWidthsI = declare(gdi32.GetCharABCWidthsI, BOOL, HDC, UINT, UINT, LPWORD, LPABC)
        STAMP_DESIGNVECTOR = (0x8000000 + ord('d') + (ord('v') << 8))
        STAMP_AXESLIST = (0x8000000 + ord('a') + (ord('l') << 8))
        STAMP_TRUETYPE_VARIATION = (0x8000000 + ord('t') + (ord('v') << 8))
        STAMP_CFF2 = (0x8000000 + ord('c') + (ord('v') << 8))
        MM_MAX_NUMAXES = 16

        class tagDESIGNVECTOR(CStructure):
            _fields_ = [
                ("dvReserved", DWORD),
                ("dvNumAxes", DWORD),
                ("dvValues", LONG * MM_MAX_NUMAXES)
            ]
        DESIGNVECTOR = tagDESIGNVECTOR
        PDESIGNVECTOR = POINTER(DESIGNVECTOR)
        LPDESIGNVECTOR = PDESIGNVECTOR

        AddFontResourceExA = declare(gdi32.AddFontResourceExA, INT, LPCSTR, DWORD, PVOID)
        AddFontResourceExW = declare(gdi32.AddFontResourceExW, INT, LPCWSTR, DWORD, PVOID)
        AddFontResourceEx = unicode(AddFontResourceExW, AddFontResourceExA)
        # !UNICODE
        RemoveFontResourceExA = declare(gdi32.RemoveFontResourceExA, BOOL, LPCSTR, DWORD, PVOID)
        RemoveFontResourceExW = declare(gdi32.RemoveFontResourceExW, BOOL, LPCWSTR, DWORD, PVOID)
        RemoveFontResourceEx = unicode(RemoveFontResourceExW, RemoveFontResourceExA)
        # !UNICODE
        AddFontMemResourceEx = declare(gdi32.AddFontMemResourceEx, HANDLE, PVOID, DWORD, PVOID, PDWORD)
        RemoveFontMemResourceEx = declare(gdi32.RemoveFontMemResourceEx, BOOL, HANDLE)
        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20
        # The actual size of the DESIGNVECTOR and ENUMLOGFONTEXDV structures
        # is determined by dvNumAxes,
        # MM_MAX_NUMAXES only detemines the maximal size allowed
        MM_MAX_AXES_NAMELEN = 16

        class tagAXISINFOA(CStructure):
            _fields_ = [
                ("axMinValue", LONG),
                ("axMaxValue", LONG),
                ("axAxisName", CHAR * MM_MAX_AXES_NAMELEN)
            ]
        AXISINFOA = tagAXISINFOA
        PAXISINFOA = POINTER(AXISINFOA)
        LPAXISINFOA = PAXISINFOA

        class tagAXISINFOW(CStructure):
            _fields_ = [
                ("axMinValue", LONG),
                ("axMaxValue", LONG),
                ("axAxisName", WCHAR * MM_MAX_AXES_NAMELEN)
            ]
        AXISINFOW = tagAXISINFOW
        PAXISINFOW = POINTER(AXISINFOW)
        LPAXISINFOW = PAXISINFOW

        AXISINFO = unicode(AXISINFOW, AXISINFOA)
        PAXISINFO = unicode(PAXISINFOW, PAXISINFOA)
        LPAXISINFO = unicode(LPAXISINFOW, LPAXISINFOA)

        class tagAXESLISTA(CStructure):
            _fields_ = [
                ("axlReserved", DWORD),
                ("axlNumAxes", DWORD),
                ("axlAxisInfo", AXISINFOA * MM_MAX_NUMAXES)
            ]
        AXESLISTA = tagAXESLISTA
        PAXESLISTA = POINTER(AXESLISTA)
        LPAXESLISTA = PAXESLISTA

        class tagAXESLISTW(CStructure):
            _fields_ = [
                ("axlReserved", DWORD),
                ("axlNumAxes", DWORD),
                ("axlAxisInfo", AXISINFOW * MM_MAX_NUMAXES)
            ]
        AXESLISTW = tagAXESLISTW
        PAXESLISTW = POINTER(AXESLISTW)
        LPAXESLISTW = PAXESLISTW

        AXESLIST = unicode(AXESLISTW, AXESLISTA)
        PAXESLIST = unicode(PAXESLISTW, PAXESLISTA)
        LPAXESLIST = unicode(LPAXESLISTW, LPAXESLISTA)

        # The actual size of the AXESLIST and ENUMTEXTMETRIC structure is
        # determined by axlNumAxes,
        # MM_MAX_NUMAXES only detemines the maximal size allowed

        class tagENUMLOGFONTEXDVA(CStructure):
            _fields_ = [
                ("elfEnumLogfontEx", ENUMLOGFONTEXA),
                ("elfDesignVector", DESIGNVECTOR)
            ]
        ENUMLOGFONTEXDVA = tagENUMLOGFONTEXDVA
        PENUMLOGFONTEXDVA = POINTER(ENUMLOGFONTEXDVA)
        LPENUMLOGFONTEXDVA = PENUMLOGFONTEXDVA

        class tagENUMLOGFONTEXDVW(CStructure):
            _fields_ = [
                ("elfEnumLogfontEx", ENUMLOGFONTEXW),
                ("elfDesignVector", DESIGNVECTOR)
            ]
        ENUMLOGFONTEXDVW = tagENUMLOGFONTEXDVW
        PENUMLOGFONTEXDVW = POINTER(ENUMLOGFONTEXDVW)
        LPENUMLOGFONTEXDVW = PENUMLOGFONTEXDVW

        ENUMLOGFONTEXDV = unicode(ENUMLOGFONTEXDVW, ENUMLOGFONTEXDVA)
        PENUMLOGFONTEXDV = unicode(PENUMLOGFONTEXDVW, PENUMLOGFONTEXDVA)
        LPENUMLOGFONTEXDV = unicode(LPENUMLOGFONTEXDVW, LPENUMLOGFONTEXDVA)

        CreateFontIndirectExA = declare(gdi32.CreateFontIndirectExA, HFONT, PENUMLOGFONTEXDVA)
        CreateFontIndirectExW = declare(gdi32.CreateFontIndirectExW, HFONT, PENUMLOGFONTEXDVW)

        if cpreproc.ifndef("NOTEXTMETRIC"):
            class tagENUMTEXTMETRICA(CStructure):
                _fields_ = [
                    ("etmNewTextMetricEx", NEWTEXTMETRICEXA),
                    ("etmAxesList", AXESLISTA)
                ]
            ENUMTEXTMETRICA = tagENUMTEXTMETRICA
            PENUMTEXTMETRICA = POINTER(ENUMTEXTMETRICA)
            LPENUMTEXTMETRICA = PENUMTEXTMETRICA

            class tagENUMTEXTMETRICW(CStructure):
                _fields_ = [
                    ("etmNewTextMetricEx", NEWTEXTMETRICEXW),
                    ("etmAxesList", AXESLISTW)
                ]
            ENUMTEXTMETRICW = tagENUMTEXTMETRICW
            PENUMTEXTMETRICW = POINTER(ENUMTEXTMETRICW)
            LPENUMTEXTMETRICW = PENUMTEXTMETRICW

            ENUMTEXTMETRIC = unicode(ENUMTEXTMETRICW, ENUMTEXTMETRICA)
            PENUMTEXTMETRIC = unicode(PENUMTEXTMETRICW, PENUMTEXTMETRICA)
            LPENUMTEXTMETRIC = unicode(LPENUMTEXTMETRICW, LPENUMTEXTMETRICA)
        # NOTEXTMETRIC

        # REGION ***

        # REGION *** Desktop Family ***

        GetViewportExtEx = declare(gdi32.GetViewportExtEx, BOOL, HDC, LPSIZE)
        GetViewportOrgEx = declare(gdi32.GetViewportOrgEx, BOOL, HDC, LPPOINT)
        GetWindowExtEx = declare(gdi32.GetWindowExtEx, BOOL, HDC, LPSIZE)
        GetWindowOrgEx = declare(gdi32.GetWindowOrgEx, BOOL, HDC, LPPOINT)
        IntersectClipRect = declare(gdi32.IntersectClipRect, INT, HDC, INT, INT, INT, INT)
        InvertRgn = declare(gdi32.InvertRgn, BOOL, HDC, HRGN)
        LineDDA = declare(gdi32.LineDDA, BOOL, INT, INT, INT, INT, LINEDDAPROC, LPARAM)
        LineTo = declare(gdi32.LineTo, BOOL, HDC, INT, INT)
        MaskBlt = declare(gdi32.MaskBlt, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, HBITMAP, INT, INT, DWORD)
        PlgBlt = declare(gdi32.PlgBlt, BOOL, HDC, PPOINT, HDC, INT, INT, INT, INT, HBITMAP, INT, INT)
        OffsetClipRgn = declare(gdi32.OffsetClipRgn, INT, HDC, INT, INT)
        OffsetRgn = declare(gdi32.OffsetRgn, INT, HRGN, INT, INT)
        PatBlt = declare(gdi32.PatBlt, BOOL, HDC, INT, INT, INT, INT, DWORD)
        Pie = declare(gdi32.Pie, BOOL, HDC, INT, INT, INT, INT, INT, INT, INT, INT)
        PlayMetaFile = declare(gdi32.PlayMetaFile, BOOL, HDC, HMETAFILE)
        PaintRgn = declare(gdi32.PaintRgn, BOOL, HDC, HRGN)
        PolyPolygon = declare(gdi32.PolyPolygon, BOOL, HDC, PPOINT, PINT, INT)
        PtInRegion = declare(gdi32.PtInRegion, BOOL, HRGN, INT, INT)
        PtVisible = declare(gdi32.PtVisible, BOOL, HDC, INT, INT)
        RectInRegion = declare(gdi32.RectInRegion, BOOL, HRGN, PRECT)
        RectVisible = declare(gdi32.RectVisible, BOOL, HDC, PRECT)
        Rectangle = declare(gdi32.Rectangle, BOOL, HDC, INT, INT, INT, INT)
        RestoreDC = declare(gdi32.RestoreDC, BOOL, HDC, INT)
        ResetDCA = declare(gdi32.ResetDCA, HDC, HDC, PDEVMODEA)
        ResetDCW = declare(gdi32.ResetDCW, HDC, HDC, PDEVMODEW)
        ResetDC = unicode(ResetDCW, ResetDCA)
        RealizePalette = declare(gdi32.RealizePalette, UINT, HDC)
        RemoveFontResourceA = declare(gdi32.RemoveFontResourceA, BOOL, LPCSTR)
        RemoveFontResourceW = declare(gdi32.RemoveFontResourceW, BOOL, LPCWSTR)
        RemoveFontResource = unicode(RemoveFontResourceW, RemoveFontResourceA)
        # !UNICODE
        RoundRect = declare(gdi32.RoundRect, BOOL, HDC, INT, INT, INT, INT, INT, INT)
        ResizePalette = declare(gdi32.ResizePalette, BOOL, HPALETTE, UINT)
        SaveDC = declare(gdi32.SaveDC, INT, HDC)
        SelectClipRgn = declare(gdi32.SelectClipRgn, INT, HDC, HRGN)
        ExtSelectClipRgn = declare(gdi32.ExtSelectClipRgn, INT, HDC, HRGN, INT)
        SetMetaRgn = declare(gdi32.SetMetaRgn, INT, HDC)
        SelectObject = declare(gdi32.SelectObject, HGDIOBJ, HDC, HGDIOBJ)
        SelectPalette = declare(gdi32.SelectPalette, HPALETTE, HDC, HPALETTE, BOOL)
        SetBkColor = declare(gdi32.SetBkColor, COLORREF, HDC, COLORREF)
        SetDCBrushColor = declare(gdi32.SetDCBrushColor, COLORREF, HDC, COLORREF)
        SetDCPenColor = declare(gdi32.SetDCPenColor, COLORREF, HDC, COLORREF)
        SetBkMode = declare(gdi32.SetBkMode, INT, HDC, INT)
        SetBitmapBits = declare(gdi32.SetBitmapBits, LONG, HBITMAP, DWORD, PVOID)
        SetBoundsRect = declare(gdi32.SetBoundsRect, UINT, HDC, PRECT, UINT)
        SetDIBits = declare(gdi32.SetDIBits, INT, HDC, HBITMAP, UINT, UINT, PVOID, UINT)
        SetDIBitsToDevice = declare(gdi32.SetDIBitsToDevice, INT, HDC, INT, INT, DWORD, DWORD, INT, INT, UINT, UINT, PVOID, UINT)
        SetMapperFlags = declare(gdi32.SetMapperFlags, DWORD, HDC, DWORD)
        SetGraphicsMode = declare(gdi32.SetGraphicsMode, INT, HDC, INT)
        SetMapMode = declare(gdi32.SetMapMode, INT, HDC, INT)
        SetLayout = declare(gdi32.SetLayout, DWORD, HDC, DWORD)
        GetLayout = declare(gdi32.GetLayout, DWORD, HDC)
        SetMetaFileBitsEx = declare(gdi32.SetMetaFileBitsEx, HMETAFILE, UINT, PBYTE)
        SetPaletteEntries = declare(gdi32.SetPaletteEntries, UINT, HPALETTE, UINT, UINT, PPALETTEENTRY)
        SetPixel = declare(gdi32.SetPixel, COLORREF, HDC, INT, INT, COLORREF)
        SetPixelV = declare(gdi32.SetPixelV, BOOL, HDC, INT, INT, COLORREF)
        SetPixelFormat = declare(gdi32.SetPixelFormat, BOOL, HDC, INT, PPIXELFORMATDESCRIPTOR)
        SetPolyFillMode = declare(gdi32.SetPolyFillMode, INT, HDC, INT)
        StretchBlt = declare(gdi32.StretchBlt, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, INT, INT, DWORD)
        SetRectRgn = declare(gdi32.SetRectRgn, BOOL, HRGN, INT, INT, INT, INT)
        StretchDIBits = declare(gdi32.StretchDIBits, INT, HDC, INT, INT, INT, INT, INT, INT, INT, INT, PVOID, UINT)
        SetROP2 = declare(gdi32.SetROP2, INT, HDC, INT)
        SetStretchBltMode = declare(gdi32.SetStretchBltMode, INT, HDC, INT)
        SetSystemPaletteUse = declare(gdi32.SetSystemPaletteUse, UINT, HDC, UINT)
        SetTextCharacterExtra = declare(gdi32.SetTextCharacterExtra, INT, HDC, INT)
        SetTextColor = declare(gdi32.SetTextColor, COLORREF, HDC, COLORREF)
        SetTextAlign = declare(gdi32.SetTextAlign, UINT, HDC, UINT)
        SetTextJustification = declare(gdi32.SetTextJustification, BOOL, HDC, INT, INT)
        UpdateColors = declare(gdi32.UpdateColors, BOOL, HDC)
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        if cpreproc.ifdef("COMBOX_SANDBOX"):

            # REGION *** Desktop Family ***

            GDIMARSHALLOC = WINAPI(PVOID, DWORD, LPVOID)
            DDRAWMARSHCALLBACKMARSHAL = WINAPI(HRESULT, HGDIOBJ, LPVOID, PLPVOID)
            DDRAWMARSHCALLBACKUNMARSHAL = WINAPI(HRESULT, LPVOID, POINTER(HDC), PLPVOID)
            DDRAWMARSHCALLBACKRELEASE = WINAPI(HRESULT, LPVOID)

            GDIREGISTERDDRAWPACKETVERSION = 0x1

            class GDIREGISTERDDRAWPACKET(CStructure):
                _fields_ = [
                    ("dwSize", DWORD),
                    ("dwVersion", DWORD),
                    ("pfnDdMarshal", DDRAWMARSHCALLBACKMARSHAL),
                    ("pfnDdUnmarshal", DDRAWMARSHCALLBACKUNMARSHAL),
                    ("pfnDdRelease", DDRAWMARSHCALLBACKRELEASE)
                ]
            PGDIREGISTERDDRAWPACKET = POINTER(GDIREGISTERDDRAWPACKET)

            GdiRegisterDdraw = declare(gdi32.GdiRegisterDdraw, BOOL, PGDIREGISTERDDRAWPACKET, POINTER(GDIMARSHALLOC))
            GdiMarshalSize = declare(gdi32.GdiMarshalSize, ULONG, VOID)
            GdiMarshal = declare(gdi32.GdiMarshal, VOID, DWORD, HGDIOBJ, PVOID, ULONG)
            GdiUnmarshal = declare(gdi32.GdiUnmarshal, HGDIOBJ, PVOID, ULONG)

            # REGION ***
        # COMBOX_SANDBOX
        
        #
        # image blt
        #

        # REGION *** Application Family ***

        COLOR16 = USHORT

        class _TRIVERTEX(CStructure):
            _fields_ = [
                ("x", LONG),
                ("y", LONG),
                ("Red", COLOR16),
                ("Green", COLOR16),
                ("Blue", COLOR16),
                ("Alpha", COLOR16)
            ]
        TRIVERTEX = _TRIVERTEX
        PTRIVERTEX = POINTER(TRIVERTEX)
        LPTRIVERTEX = PTRIVERTEX

        # REGION ***

        # REGION *** Desktop Family ***

        class _GRADIENT_TRIANGLE(CStructure):
            _fields_ = [
                ("Vertex1", ULONG),
                ("Vertex2", ULONG),
                ("Vertex3", ULONG)
            ]
        GRADIENT_TRIANGLE = _GRADIENT_TRIANGLE
        PGRADIENT_TRIANGLE = POINTER(GRADIENT_TRIANGLE)
        LPGRADIENT_TRIANGLE = PGRADIENT_TRIANGLE

        class _GRADIENT_RECT(CStructure):
            _fields_ = [
                ("UpperLeft", ULONG),
                ("LowerRight", ULONG)
            ]
        GRADIENT_RECT = _GRADIENT_RECT
        PGRADIENT_RECT = POINTER(GRADIENT_RECT)
        LPGRADIENT_RECT = PGRADIENT_RECT

        # REGION ***

        # REGION *** Application Family ***

        class _BLENDFUNCTION(CStructure):
            _fields_ = [
                ("BlendOp", BYTE),
                ("BlendFlags", BYTE),
                ("SourceConstantAlpha", BYTE),
                ("AlphaFormat", BYTE)
            ]
        BLENDFUNCTION = _BLENDFUNCTION
        PBLENDFUNCTION = POINTER(BLENDFUNCTION)

        # REGION ***

        # REGION *** Desktop Family ***

        #
        # currentlly defined blend function
        #

        AC_SRC_OVER = 0x00

        #
        # alpha format flags
        #
        AC_SRC_ALPHA = 0x01

        AlphaBlend = declare(msimg32.AlphaBlend, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, INT, INT, BLENDFUNCTION)
        TransparentBlt = declare(msimg32.TransparentBlt, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, INT, INT, UINT)
        #
        # gradient drawing modes
        #
        GRADIENT_FILL_RECT_H = 0x00000000
        GRADIENT_FILL_RECT_V = 0x00000001
        GRADIENT_FILL_TRIANGLE = 0x00000002
        GRADIENT_FILL_OP_FLAG = 0x000000ff
        GradientFill = declare(msimg32.GradientFill, BOOL, HDC, PTRIVERTEX, ULONG, PVOID, ULONG, ULONG, )
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
        # (WINVER >= 0x0400)

        # REGION *** Desktop Family ***

        GdiAlphaBlend = declare(gdi32.GdiAlphaBlend, BOOL, HDC, INT, INT, INT, INT, HDC, INT, INT, INT, INT, BLENDFUNCTION)
        if cpreproc.ifndef("NOMETAFILE"):
            PlayMetaFileRecord = declare(gdi32.PlayMetaFileRecord, BOOL, HDC, LPHANDLETABLE, LPMETARECORD, UINT)
            MFENUMPROC = CALLBACK(INT, HDC, LPHANDLETABLE, LPMETARECORD, INT, LPARAM)
            EnumMetaFile = declare(gdi32.EnumMetaFile, BOOL, HDC, HMETAFILE, MFENUMPROC, LPARAM)
            ENHMFENUMPROC = CALLBACK(INT, HDC, LPHANDLETABLE, PENHMETARECORD, INT, LPARAM)
            # Enhanced Metafile Function Declarations
            CloseEnhMetaFile = declare(gdi32.CloseEnhMetaFile, HENHMETAFILE, HDC)
            CopyEnhMetaFileA = declare(gdi32.CopyEnhMetaFileA, HENHMETAFILE, HENHMETAFILE, LPCSTR)
            CopyEnhMetaFileW = declare(gdi32.CopyEnhMetaFileW, HENHMETAFILE, HENHMETAFILE, LPCWSTR)
            CopyEnhMetaFile = unicode(CopyEnhMetaFileW, CopyEnhMetaFileA)
            CreateEnhMetaFileA = declare(gdi32.CreateEnhMetaFileA, HDC, HDC, LPCSTR, PRECT, LPCSTR)
            CreateEnhMetaFileW = declare(gdi32.CreateEnhMetaFileW, HDC, HDC, LPCWSTR, PRECT, LPCWSTR)
            CreateEnhMetaFile = unicode(CreateEnhMetaFileW, CreateEnhMetaFileA)
            # !UNICODE
            DeleteEnhMetaFile = declare(gdi32.DeleteEnhMetaFile, BOOL, HENHMETAFILE)
            EnumEnhMetaFile = declare(gdi32.EnumEnhMetaFile, BOOL, HDC, HENHMETAFILE, ENHMFENUMPROC, LPVOID, PRECT)
            GetEnhMetaFileA = declare(gdi32.GetEnhMetaFileA, HENHMETAFILE, LPCSTR)
            GetEnhMetaFileW = declare(gdi32.GetEnhMetaFileW, HENHMETAFILE, LPCWSTR)
            GetEnhMetaFile = unicode(GetEnhMetaFileW, GetEnhMetaFileA)
            # !UNICODE
            GetEnhMetaFileBits = declare(gdi32.GetEnhMetaFileBits, UINT, HENHMETAFILE, UINT, LPBYTE)
            GetEnhMetaFileDescriptionA = declare(gdi32.GetEnhMetaFileDescriptionA, UINT, HENHMETAFILE, UINT, LPSTR)
            GetEnhMetaFileDescriptionW = declare(gdi32.GetEnhMetaFileDescriptionW, UINT, HENHMETAFILE, UINT, LPWSTR)
            GetEnhMetaFileDescription = unicode(GetEnhMetaFileDescriptionW, GetEnhMetaFileDescriptionA)
            # !UNICODE
            GetEnhMetaFileHeader = declare(gdi32.GetEnhMetaFileHeader, UINT, HENHMETAFILE, UINT, LPENHMETAHEADER)
            GetEnhMetaFilePaletteEntries = declare(gdi32.GetEnhMetaFilePaletteEntries, UINT, HENHMETAFILE, UINT, LPPALETTEENTRY)
            GetEnhMetaFilePixelFormat = declare(gdi32.GetEnhMetaFilePixelFormat, UINT, HENHMETAFILE, UINT, PPIXELFORMATDESCRIPTOR)
            GetWinMetaFileBits = declare(gdi32.GetWinMetaFileBits, UINT, HENHMETAFILE, UINT, LPBYTE, INT, HDC)
            PlayEnhMetaFile = declare(gdi32.PlayEnhMetaFile, BOOL, HDC, HENHMETAFILE, PRECT)
            PlayEnhMetaFileRecord = declare(gdi32.PlayEnhMetaFileRecord, BOOL, HDC, LPHANDLETABLE, PENHMETARECORD, UINT)
            SetEnhMetaFileBits = declare(gdi32.SetEnhMetaFileBits, HENHMETAFILE, UINT, PBYTE)
            SetWinMetaFileBits = declare(gdi32.SetWinMetaFileBits, HENHMETAFILE, UINT, PBYTE, HDC, PMETAFILEPICT)
            GdiComment = declare(gdi32.GdiComment, BOOL, HDC, UINT, PBYTE)
        # NOMETAFILE
        if cpreproc.ifndef("NOTEXTMETRIC"):
            GetTextMetricsA = declare(gdi32.GetTextMetricsA, BOOL, HDC, LPTEXTMETRICA)
            GetTextMetricsW = declare(gdi32.GetTextMetricsW, BOOL, HDC, LPTEXTMETRICW)
        GetTextMetrics = unicode(GetTextMetricsW, GetTextMetricsA)
        # !UNICODE
        # new GDI
        class tagDIBSECTION(CStructure):
            _fields_ = [
                ("dsBm", BITMAP),
                ("dsBmih", BITMAPINFOHEADER),
                ("dsBitfields", DWORD * 3),
                ("dsOffset", DWORD)
            ]
        DIBSECTION = tagDIBSECTION
        LPDIBSECTION = POINTER(DIBSECTION)
        PDIBSECTION = LPDIBSECTION

        GDI_WIDTHBYTES = lambda bits: DWORD(((bits)+31) & (~31)).value // 8
        GDI_DIBWIDTHBYTES = lambda bi: DWORD(GDI_WIDTHBYTES(DWORD(bi.biWidth).value * DWORD(bi.biBitCount).value)).value
        GDI__DIBSIZE = lambda bi: GDI_DIBWIDTHBYTES(bi) * DWORD(bi.biHeight)
        GDI_DIBSIZE = lambda bi: (-1 * GDI__DIBSIZE(bi) if bi.biHeight < 0 else GDI__DIBSIZE(bi))

        CreateDIBSection = declare(gdi32.CreateDIBSection, HBITMAP, HDC, UINT, PVOID, HANDLE, DWORD)
        GetDIBColorTable = declare(gdi32.GetDIBColorTable, UINT, HDC, UINT, UINT, PRGBQUAD)
        SetDIBColorTable = declare(gdi32.SetDIBColorTable, UINT, HDC, UINT, UINT, PRGBQUAD)
        # Flags value for COLORADJUSTMENT
        CA_NEGATIVE = 0x0001
        CA_LOG_FILTER = 0x0002
        # IlluminantIndex values
        ILLUMINANT_DEVICE_DEFAULT = 0
        ILLUMINANT_A = 1
        ILLUMINANT_B = 2
        ILLUMINANT_C = 3
        ILLUMINANT_D50 = 4
        ILLUMINANT_D55 = 5
        ILLUMINANT_D65 = 6
        ILLUMINANT_D75 = 7
        ILLUMINANT_F2 = 8
        ILLUMINANT_MAX_INDEX = ILLUMINANT_F2
        ILLUMINANT_TUNGSTEN = ILLUMINANT_A
        ILLUMINANT_DAYLIGHT = ILLUMINANT_C
        ILLUMINANT_FLUORESCENT = ILLUMINANT_F2
        ILLUMINANT_NTSC = ILLUMINANT_C
        # Min and max for RedGamma, GreenGamma, BlueGamma
        RGB_GAMMA_MIN = 2500
        RGB_GAMMA_MAX = 65000
        # Min and max for ReferenceBlack and ReferenceWhite
        REFERENCE_WHITE_MIN = 6000
        REFERENCE_WHITE_MAX = 10000
        REFERENCE_BLACK_MIN = 0
        REFERENCE_BLACK_MAX = 4000
        # Min and max for Contrast, Brightness, Colorfulness, RedGreenTint
        COLOR_ADJ_MIN = -100
        COLOR_ADJ_MAX = 100

        class  tagCOLORADJUSTMENT(CStructure):
            _fields_ = [
                ("caSize", WORD),
                ("caFlags", WORD),
                ("caIlluminantIndex", WORD),
                ("caRedGamma", WORD),
                ("caGreenGamma", WORD),
                ("caBlueGamma", WORD),
                ("caReferenceBlack", WORD),
                ("caReferenceWhite", WORD),
                ("caContrast", SHORT),
                ("caBrightness", SHORT),
                ("caColorfulness", SHORT),
                ("caRedGreenTint", SHORT)
            ]
        COLORADJUSTMENT = tagCOLORADJUSTMENT
        PCOLORADJUSTMENT = POINTER(COLORADJUSTMENT)
        LPCOLORADJUSTMENT = PCOLORADJUSTMENT

        SetColorAdjustment = declare(gdi32.SetColorAdjustment, BOOL, HDC, PCOLORADJUSTMENT)
        GetColorAdjustment = declare(gdi32.GetColorAdjustment, BOOL, HDC, LPCOLORADJUSTMENT)
        CreateHalftonePalette = declare(gdi32.CreateHalftonePalette, HPALETTE, HDC)

        ABORTPROC = CALLBACK(BOOL, HDC, INT)

        class _DOCINFOA(CStructure):
            _fields_ = [
                ("cbSize", INT),
                ("lpszDocName", LPCSTR),
                ("lpszOutput", LPCSTR),
                ("lpszDatatype", LPCSTR),
                ("fwType", DWORD)
            ]
        DOCINFOA = _DOCINFOA
        PDOCINFOA = POINTER(DOCINFOA)
        LPDOCINFOA = PDOCINFOA

        class _DOCINFOW(CStructure):
            _fields_ = [
                ("cbSize", INT),
                ("lpszDocName", LPCWSTR),
                ("lpszOutput", LPCWSTR),
                ("lpszDatatype", LPCWSTR),
                ("fwType", DWORD)
            ]
        DOCINFOW = _DOCINFOW
        PDOCINFOW = POINTER(DOCINFOW)
        LPDOCINFOW = PDOCINFOW

        DOCINFO = unicode(DOCINFOW, DOCINFOA)
        LPDOCINFO = unicode(LPDOCINFOW, LPDOCINFOA)

        DI_APPBANDING = 0x00000001
        DI_ROPS_READ_DESTINATION = 0x00000002
        # WINVER >= 0x0400
        StartDocA = declare(gdi32.StartDocA, INT, HDC, PDOCINFOA)
        StartDocW = declare(gdi32.StartDocW, INT, HDC, PDOCINFOW)
        StartDoc = unicode(StartDocW, StartDocA)
        # !UNICODE
        EndDoc = declare(gdi32.EndDoc, INT, HDC)
        StartPage = declare(gdi32.StartPage, INT, HDC)
        EndPage = declare(gdi32.EndPage, INT, HDC)
        AbortDoc = declare(gdi32.AbortDoc, INT, HDC)
        SetAbortProc = declare(gdi32.SetAbortProc, INT, HDC, ABORTPROC)
        AbortPath = declare(gdi32.AbortPath, BOOL, HDC)
        ArcTo = declare(gdi32.ArcTo, BOOL, HDC, INT, INT, INT, INT, INT, INT, INT, INT)
        BeginPath = declare(gdi32.BeginPath, BOOL, HDC)
        CloseFigure = declare(gdi32.CloseFigure, BOOL, HDC)
        EndPath = declare(gdi32.EndPath, BOOL, HDC)
        FillPath = declare(gdi32.FillPath, BOOL, HDC)
        FlattenPath = declare(gdi32.FlattenPath, BOOL, HDC)
        GetPath = declare(gdi32.GetPath, INT, HDC, LPPOINT, LPBYTE)
        PathToRegion = declare(gdi32.PathToRegion, HRGN, HDC)
        PolyDraw = declare(gdi32.PolyDraw, BOOL, HDC, PPOINT, PBYTE, INT)
        SelectClipPath = declare(gdi32.SelectClipPath, BOOL, HDC, INT)
        SetArcDirection = declare(gdi32.SetArcDirection, INT, HDC, INT)
        SetMiterLimit = declare(gdi32.SetMiterLimit, BOOL, HDC, FLOAT, PFLOAT)
        StrokeAndFillPath = declare(gdi32.StrokeAndFillPath, BOOL, HDC)
        StrokePath = declare(gdi32.StrokePath, BOOL, HDC)
        WidenPath = declare(gdi32.WidenPath, BOOL, HDC)
        ExtCreatePen = declare(gdi32.ExtCreatePen, HPEN, DWORD, DWORD, PLOGBRUSH, DWORD, PDWORD)
        GetMiterLimit = declare(gdi32.GetMiterLimit, BOOL, HDC, PFLOAT)
        GetArcDirection = declare(gdi32.GetArcDirection, INT, HDC)
        GetObjectA = declare(gdi32.GetObjectA, INT, HANDLE, INT, LPVOID)
        GetObjectW = declare(gdi32.GetObjectW, INT, HANDLE, INT, LPVOID)
        GetObject = unicode(GetObjectW, GetObjectA)
        # !UNICODE
        MoveToEx = declare(gdi32.MoveToEx, BOOL, HDC, INT, INT, LPPOINT)
        TextOutA = declare(gdi32.TextOutA, BOOL, HDC, INT, INT, LPCSTR, INT)
        TextOutW = declare(gdi32.TextOutW, BOOL, HDC, INT, INT, LPCWSTR, INT)
        TextOut = unicode(TextOutW, TextOutA)
        # !UNICODE
        ExtTextOutA = declare(gdi32.ExtTextOutA, BOOL, HDC, INT, INT, UINT, PRECT, LPCSTR, UINT, PINT)
        ExtTextOutW = declare(gdi32.ExtTextOutW, BOOL, HDC, INT, INT, UINT, PRECT, LPCWSTR, UINT, PINT)
        ExtTextOut = unicode(ExtTextOutW, ExtTextOutA)
        # !UNICODE
        PolyTextOutA = declare(gdi32.PolyTextOutA, BOOL, HDC, PPOLYTEXTA, INT)
        PolyTextOutW = declare(gdi32.PolyTextOutW, BOOL, HDC, PPOLYTEXTW, INT)
        PolyTextOut = unicode(PolyTextOutW, PolyTextOutA)
        # !UNICODE
        CreatePolygonRgn = declare(gdi32.CreatePolygonRgn, HRGN, PPOINT, INT, INT)
        DPtoLP = declare(gdi32.DPtoLP, BOOL, HDC, LPPOINT, INT)
        LPtoDP = declare(gdi32.LPtoDP, BOOL, HDC, LPPOINT, INT)
        Polygon = declare(gdi32.Polygon, BOOL, HDC, PPOINT, INT)
        Polyline = declare(gdi32.Polyline, BOOL, HDC, PPOINT, INT)
        PolyBezier = declare(gdi32.PolyBezier, BOOL, HDC, PPOINT, DWORD)
        PolyBezierTo = declare(gdi32.PolyBezierTo, BOOL, HDC, PPOINT, DWORD)
        PolylineTo = declare(gdi32.PolylineTo, BOOL, HDC, PPOINT, DWORD)
        SetViewportExtEx = declare(gdi32.SetViewportExtEx, BOOL, HDC, INT, INT, LPSIZE)
        SetViewportOrgEx = declare(gdi32.SetViewportOrgEx, BOOL, HDC, INT, INT, LPPOINT)
        SetWindowExtEx = declare(gdi32.SetWindowExtEx, BOOL, HDC, INT, INT, LPSIZE)
        SetWindowOrgEx = declare(gdi32.SetWindowOrgEx, BOOL, HDC, INT, INT, LPPOINT)
        OffsetViewportOrgEx = declare(gdi32.OffsetViewportOrgEx, BOOL, HDC, INT, INT, LPPOINT)
        OffsetWindowOrgEx = declare(gdi32.OffsetWindowOrgEx, BOOL, HDC, INT, INT, LPPOINT)
        ScaleViewportExtEx = declare(gdi32.ScaleViewportExtEx, BOOL, HDC, INT, INT, INT, INT, LPSIZE)
        ScaleWindowExtEx = declare(gdi32.ScaleWindowExtEx, BOOL, HDC, INT, INT, INT, INT, LPSIZE)
        SetBitmapDimensionEx = declare(gdi32.SetBitmapDimensionEx, BOOL, HBITMAP, INT, INT, LPSIZE)
        SetBrushOrgEx = declare(gdi32.SetBrushOrgEx, BOOL, HDC, INT, INT, LPPOINT)
        GetTextFaceA = declare(gdi32.GetTextFaceA, INT, HDC, INT, LPSTR)
        GetTextFaceW = declare(gdi32.GetTextFaceW, INT, HDC, INT, LPWSTR)
        GetTextFace = unicode(GetTextFaceW, GetTextFaceA)
        # !UNICODE
        FONTMAPPER_MAX = 10

        class tagKERNINGPAIR(CStructure):
            _fields_ = [
                ("wFirst", WORD),
                ("wSecond", WORD),
                ("iKernAmount", INT)
            ]
        KERNINGPAIR = tagKERNINGPAIR
        LPKERNINGPAIR = POINTER(KERNINGPAIR)

        GetKerningPairsA = declare(gdi32.GetKerningPairsA, DWORD, HDC, DWORD, LPKERNINGPAIR)
        GetKerningPairsW = declare(gdi32.GetKerningPairsW, DWORD, HDC, DWORD, LPKERNINGPAIR)
        GetKerningPairs = unicode(GetKerningPairsW, GetKerningPairsA)
        # !UNICODE
        GetDCOrgEx = declare(gdi32.GetDCOrgEx, BOOL, HDC, LPPOINT)
        FixBrushOrgEx = declare(gdi32.FixBrushOrgEx, BOOL, HDC, INT, INT)
        UnrealizeObject = declare(gdi32.UnrealizeObject, BOOL, HGDIOBJ)
        GdiSetBatchLimit = declare(gdi32.GdiSetBatchLimit, DWORD, DWORD)
        ICM_OFF = 1
        ICM_ON = 2
        ICM_QUERY = 3
        ICM_DONE_OUTSIDEDC = 4
        ICMENUMPROCA = CALLBACK(INT, LPSTR, LPARAM)
        ICMENUMPROCW = CALLBACK(INT, LPWSTR, LPARAM)
        ICMENUMPROC = unicode(ICMENUMPROCW, ICMENUMPROCA)
        SetICMMode = declare(gdi32.SetICMMode, INT, HDC, INT)
        CheckColorsInGamut = declare(gdi32.CheckColorsInGamut, BOOL, HDC, LPRGBTRIPLE, LPVOID, DWORD)
        GetColorSpace = declare(gdi32.GetColorSpace, HCOLORSPACE, HDC)
        GetLogColorSpaceA = declare(gdi32.GetLogColorSpaceA, BOOL, HCOLORSPACE, LPLOGCOLORSPACEA, DWORD)
        GetLogColorSpaceW = declare(gdi32.GetLogColorSpaceW, BOOL, HCOLORSPACE, LPLOGCOLORSPACEW, DWORD)
        GetLogColorSpace = unicode(GetLogColorSpaceW, GetLogColorSpaceA)
        # !UNICODE
        CreateColorSpaceA = declare(gdi32.CreateColorSpaceA, HCOLORSPACE, LPLOGCOLORSPACEA)
        CreateColorSpaceW = declare(gdi32.CreateColorSpaceW, HCOLORSPACE, LPLOGCOLORSPACEW)
        CreateColorSpace = unicode(CreateColorSpaceW, CreateColorSpaceA)
        # !UNICODE
        SetColorSpace = declare(gdi32.SetColorSpace, HCOLORSPACE, HDC, HCOLORSPACE)
        DeleteColorSpace = declare(gdi32.DeleteColorSpace, BOOL, HCOLORSPACE)
        GetICMProfileA = declare(gdi32.GetICMProfileA, BOOL, HDC, LPDWORD, LPSTR)
        GetICMProfileW = declare(gdi32.GetICMProfileW, BOOL, HDC, LPDWORD, LPWSTR)
        GetICMProfile = unicode(GetICMProfileW, GetICMProfileA)
        # !UNICODE
        SetICMProfileA = declare(gdi32.SetICMProfileA, BOOL, HDC, LPSTR)
        SetICMProfileW = declare(gdi32.SetICMProfileW, BOOL, HDC, LPWSTR)
        SetICMProfile = unicode(SetICMProfileW, SetICMProfileA)
        # !UNICODE
        GetDeviceGammaRamp = declare(gdi32.GetDeviceGammaRamp, BOOL, HDC, LPVOID)
        SetDeviceGammaRamp = declare(gdi32.SetDeviceGammaRamp, BOOL, HDC, LPVOID)
        ColorMatchToTarget = declare(gdi32.ColorMatchToTarget, BOOL, HDC, HDC, DWORD)
        EnumICMProfilesA = declare(gdi32.EnumICMProfilesA, INT, HDC, ICMENUMPROCA, LPARAM)
        EnumICMProfilesW = declare(gdi32.EnumICMProfilesW, INT, HDC, ICMENUMPROCW, LPARAM)
        EnumICMProfiles = unicode(EnumICMProfilesW, EnumICMProfilesA)
        # !UNICODE
        # The Win95 update API UpdateICMRegKeyA is deprecated to set last error to ERROR_NOT_SUPPORTED and return FALSE
        UpdateICMRegKeyA = declare(gdi32.UpdateICMRegKeyA, BOOL, DWORD, LPSTR, LPSTR, UINT)
        # The Win95 update API UpdateICMRegKeyW is deprecated to set last error to ERROR_NOT_SUPPORTED and return FALSE
        UpdateICMRegKeyW = declare(gdi32.UpdateICMRegKeyW, BOOL, DWORD, LPWSTR, LPWSTR, UINT)
        UpdateICMRegKey = unicode(UpdateICMRegKeyW, UpdateICMRegKeyA)
        # !UNICODE
        # WINVER >= 0x0400
        ColorCorrectPalette = declare(gdi32.ColorCorrectPalette, BOOL, HDC, HPALETTE, DWORD, DWORD)
        if cpreproc.ifndef("NOMETAFILE"):
            # Enhanced metafile constants.
            ENHMETA_SIGNATURE = 0x464D4520
            # Stock object flag used in the object handle index in the enhanced
            # metafile records.
            # E.g. The object handle index (META_STOCK_OBJECT | BLACK_BRUSH)
            # represents the stock object BLACK_BRUSH.
            ENHMETA_STOCK_OBJECT = 0x80000000
            # Enhanced metafile record types.
            EMR_HEADER = 1
            EMR_POLYBEZIER = 2
            EMR_POLYGON = 3
            EMR_POLYLINE = 4
            EMR_POLYBEZIERTO = 5
            EMR_POLYLINETO = 6
            EMR_POLYPOLYLINE = 7
            EMR_POLYPOLYGON = 8
            EMR_SETWINDOWEXTEX = 9
            EMR_SETWINDOWORGEX = 10
            EMR_SETVIEWPORTEXTEX = 11
            EMR_SETVIEWPORTORGEX = 12
            EMR_SETBRUSHORGEX = 13
            EMR_EOF = 14
            EMR_SETPIXELV = 15
            EMR_SETMAPPERFLAGS = 16
            EMR_SETMAPMODE = 17
            EMR_SETBKMODE = 18
            EMR_SETPOLYFILLMODE = 19
            EMR_SETROP2 = 20
            EMR_SETSTRETCHBLTMODE = 21
            EMR_SETTEXTALIGN = 22
            EMR_SETCOLORADJUSTMENT = 23
            EMR_SETTEXTCOLOR = 24
            EMR_SETBKCOLOR = 25
            EMR_OFFSETCLIPRGN = 26
            EMR_MOVETOEX = 27
            EMR_SETMETARGN = 28
            EMR_EXCLUDECLIPRECT = 29
            EMR_INTERSECTCLIPRECT = 30
            EMR_SCALEVIEWPORTEXTEX = 31
            EMR_SCALEWINDOWEXTEX = 32
            EMR_SAVEDC = 33
            EMR_RESTOREDC = 34
            EMR_SETWORLDTRANSFORM = 35
            EMR_MODIFYWORLDTRANSFORM = 36
            EMR_SELECTOBJECT = 37
            EMR_CREATEPEN = 38
            EMR_CREATEBRUSHINDIRECT = 39
            EMR_DELETEOBJECT = 40
            EMR_ANGLEARC = 41
            EMR_ELLIPSE = 42
            EMR_RECTANGLE = 43
            EMR_ROUNDRECT = 44
            EMR_ARC = 45
            EMR_CHORD = 46
            EMR_PIE = 47
            EMR_SELECTPALETTE = 48
            EMR_CREATEPALETTE = 49
            EMR_SETPALETTEENTRIES = 50
            EMR_RESIZEPALETTE = 51
            EMR_REALIZEPALETTE = 52
            EMR_EXTFLOODFILL = 53
            EMR_LINETO = 54
            EMR_ARCTO = 55
            EMR_POLYDRAW = 56
            EMR_SETARCDIRECTION = 57
            EMR_SETMITERLIMIT = 58
            EMR_BEGINPATH = 59
            EMR_ENDPATH = 60
            EMR_CLOSEFIGURE = 61
            EMR_FILLPATH = 62
            EMR_STROKEANDFILLPATH = 63
            EMR_STROKEPATH = 64
            EMR_FLATTENPATH = 65
            EMR_WIDENPATH = 66
            EMR_SELECTCLIPPATH = 67
            EMR_ABORTPATH = 68
            EMR_GDICOMMENT = 70
            EMR_FILLRGN = 71
            EMR_FRAMERGN = 72
            EMR_INVERTRGN = 73
            EMR_PAINTRGN = 74
            EMR_EXTSELECTCLIPRGN = 75
            EMR_BITBLT = 76
            EMR_STRETCHBLT = 77
            EMR_MASKBLT = 78
            EMR_PLGBLT = 79
            EMR_SETDIBITSTODEVICE = 80
            EMR_STRETCHDIBITS = 81
            EMR_EXTCREATEFONTINDIRECTW = 82
            EMR_EXTTEXTOUTA = 83
            EMR_EXTTEXTOUTW = 84
            EMR_POLYBEZIER16 = 85
            EMR_POLYGON16 = 86
            EMR_POLYLINE16 = 87
            EMR_POLYBEZIERTO16 = 88
            EMR_POLYLINETO16 = 89
            EMR_POLYPOLYLINE16 = 90
            EMR_POLYPOLYGON16 = 91
            EMR_POLYDRAW16 = 92
            EMR_CREATEMONOBRUSH = 93
            EMR_CREATEDIBPATTERNBRUSHPT = 94
            EMR_EXTCREATEPEN = 95
            EMR_POLYTEXTOUTA = 96
            EMR_POLYTEXTOUTW = 97
            EMR_SETICMMODE = 98
            EMR_CREATECOLORSPACE = 99
            EMR_SETCOLORSPACE = 100
            EMR_DELETECOLORSPACE = 101
            EMR_GLSRECORD = 102
            EMR_GLSBOUNDEDRECORD = 103
            EMR_PIXELFORMAT = 104
            EMR_RESERVED_105 = 105
            EMR_RESERVED_106 = 106
            EMR_RESERVED_107 = 107
            EMR_RESERVED_108 = 108
            EMR_RESERVED_109 = 109
            EMR_RESERVED_110 = 110
            EMR_COLORCORRECTPALETTE = 111
            EMR_SETICMPROFILEA = 112
            EMR_SETICMPROFILEW = 113
            EMR_ALPHABLEND = 114
            EMR_SETLAYOUT = 115
            EMR_TRANSPARENTBLT = 116
            EMR_RESERVED_117 = 117
            EMR_GRADIENTFILL = 118
            EMR_RESERVED_119 = 119
            EMR_RESERVED_120 = 120
            EMR_COLORMATCHTOTARGETW = 121
            EMR_CREATECOLORSPACEW = 122
            EMR_MIN = 1
            EMR_MAX = 122
            EMR_MAX = 104
            EMR_MAX = 97
            # Base record type for the enhanced metafile.

            # RECORD TYPES
            # TODO: REALIZE STRUCTURES

            # WINVER >= 0x0500
            GDICOMMENT_IDENTIFIER = 0x43494447
            GDICOMMENT_WINDOWS_METAFILE = 0x80000001
            GDICOMMENT_BEGINGROUP = 0x00000002
            GDICOMMENT_ENDGROUP = 0x00000003
            GDICOMMENT_MULTIFORMATS = 0x40000004
            EPS_SIGNATURE = 0x46535045
            GDICOMMENT_UNICODE_STRING = 0x00000040
            GDICOMMENT_UNICODE_END = 0x00000080
        # NOMETAFILE
        # OpenGL wgl prototypes
        wglCopyContext = declare(opengl32.wglCopyContext, BOOL, HGLRC)
        wglCreateContext = declare(opengl32.wglCreateContext, HGLRC, HDC)
        wglCreateLayerContext = declare(opengl32.wglCreateLayerContext, HGLRC, HDC, INT)
        wglDeleteContext = declare(opengl32.wglDeleteContext, BOOL, HGLRC)
        wglGetCurrentContext = declare(opengl32.wglGetCurrentContext, HGLRC, VOID)
        wglGetCurrentDC = declare(opengl32.wglGetCurrentDC, HDC, VOID)
        wglGetProcAddress = declare(opengl32.wglGetProcAddress, PROC, LPCSTR)
        wglMakeCurrent = declare(opengl32.wglMakeCurrent, BOOL, HDC, HGLRC)
        wglShareLists = declare(opengl32.wglShareLists, BOOL, HGLRC, HGLRC)
        wglUseFontBitmapsA = declare(opengl32.wglUseFontBitmapsA, BOOL, HDC, DWORD, DWORD, DWORD)
        wglUseFontBitmapsW = declare(opengl32.wglUseFontBitmapsW, BOOL, HDC, DWORD, DWORD, DWORD)
        wglUseFontBitmaps = unicode(wglUseFontBitmapsW, wglUseFontBitmapsA)
        # !UNICODE
        SwapBuffers = declare(gdi32.SwapBuffers, BOOL, HDC)

        # TODO: END STRUCTURES + SOME WGL METHODS