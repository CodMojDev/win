#+-------------------------------------------------------------------------
#
#  Microsoft Windows
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
#  File: wtypes.idl
#
#  Contents: This interface definition contains typedefs for remotable
#            data types.
#--------------------------------------------------------------------------

from . import cpreproc

if cpreproc.pragma_once():
    from .wtypesbase import *
    
    class RemHGLOBAL(CStructure):
        _fields_ = [
            ('fNullHGlobal', LONG),
            ('cbData', ULONG)
        ]
        
        fNullHGlobal: int
        cbData: int
        data: PBYTE
    
    array_after_structure(RemHGLOBAL, 'data', BYTE)
    
    class RemHMETAFILEPICT(CStructure):
        _fields_ = [
            ('mm', LONG),
            ('xExt', LONG),
            ('yExt', LONG),
            ('cbData', ULONG)
        ]
        
        cbData: int
        data: PBYTE
        
        xExt: int
        yExt: int
        mm: int
        
    array_after_structure(RemHMETAFILEPICT, 'data', BYTE)
    
    class RemHENHMETAFILE(CStructure):
        _fields_ = [('cbData', ULONG)]
        
        cbData: int
        data: PBYTE
        
    array_after_structure(RemHENHMETAFILE, 'data', BYTE)
    
    class RemHBITMAP(CStructure):
        _fields_ = [('cbData', ULONG)]
        
        cbData: int
        data: PBYTE
        
    array_after_structure(RemHBITMAP, 'data', BYTE)
    
    class RemHPALETTE(CStructure):
        _fields_ = [('cbData', ULONG)]
        
        cbData: int
        data: PBYTE
        
    array_after_structure(RemHPALETTE, 'data', BYTE)
    
    class RemBRUSH(CStructure):
        _fields_ = [('cbData', ULONG)]
        
        cbData: int
        data: PBYTE
        
    array_after_structure(RemBRUSH, 'data', BYTE)
    
    byte = c_byte
    c_long = c_long
    
    HMF = HMETAFILE
    HEMF = HENHMETAFILE
    
    class PALETTEENTRY(CStructure):
        _fields_ = [
            ("peRed", BYTE),
            ("peGreen", BYTE),
            ("peBlue", BYTE),
            ("peFlags", BYTE)
        ]
        
        peGreen: int
        peFlags: int
        peBlue: int
        peRed: int
        
    PPALETTEENTRY = POINTER(PALETTEENTRY)
    LPPALETTEENTRY = PPALETTEENTRY
    
    # Logical Palette
    class LOGPALETTE(CStructure):
        _fields_ = [
            ("palVersion", WORD),
            ("palNumEntries", WORD)
        ]
        
        palPalEntry: IPointer[PALETTEENTRY]
        palNumEntries: int
        palVersion: int
    
    array_after_structure(LOGPALETTE, 'palPalEntry', PALETTEENTRY)
        
    PLOGPALETTE = POINTER(LOGPALETTE)
    NPLOGPALETTE = PLOGPALETTE
    LPLOGPALETTE = PLOGPALETTE
    
    #########################* Misc types ###################################

    # Common typdefs used in API paramaters, gleamed from compobj.h

    # For IRunningObjectTable::Register
    if cpreproc.pragma_once('_ROTFLAGS_DEFINED'):
        ROTFLAGS_REGISTRATIONKEEPSALIVE = 0x1
        ROTFLAGS_ALLOWANYCLIENT =0x2
    # !_ROTFLAGS_DEFINED
    
    # Maximum size of comparison buffer for IROTData::GetComparisonData
    if cpreproc.pragma_once('_ROT_COMPARE_MAX_DEFINED'):
        ROT_COMPARE_MAX = 2048
    # !_ROT_COMPARE_MAX_DEFINED

    #
    # Common typedefs for paramaters used in data view API's, gleamed
    # from dvobj.h
    #

    # Data/View aspect; specifies the desired aspect of the object when
    # drawing or getting data.
    DVASPECT_CONTENT = 1
    DVASPECT_THUMBNAIL = 2
    DVASPECT_ICON = 4
    DVASPECT_DOCPRINT = 8
    DVASPECT = INT

    ####### Storage types #################################################


    # Storage commit types
    STGC_DEFAULT        = 0
    STGC_OVERWRITE      = 1
    STGC_ONLYIFCURRENT  = 2
    STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE = 4
    STGC_CONSOLIDATE    = 8
    STGC = INT

    STGMOVE_MOVE    = 0
    STGMOVE_COPY    = 1
    STGMOVE_SHALLOWCOPY = 2
    STGMOVE = INT

    STATFLAG_DEFAULT = 0
    STATFLAG_NONAME = 1
    STATFLAG_NOOPEN = 2
    STATFLAG = INT

    HCONTEXT = HANDLE
    
    # #########################################################################
    #
    #   Constants for the call context
    #

    WDT_INPROC_CALL   = 0x48746457
    WDT_REMOTE_CALL   = 0x52746457
    WDT_INPROC64_CALL = 0x50746457

    # #########################################################################
    #
    #  CLIPFORMAT
    #
    
    class userCLIPFORMAT(CStructure):
        class U(CUnion): 
            _fields_ = [
                ('dwValue', DWORD),
                ('pwszName', LPWSTR)
            ]
        _fields_ = [('fContext', LONG), ('u', U)]
        _anonymous_ = ['u']
        
        pwszName: LPWSTR
        fContext: int
        dwValue: int
    
    wireCLIPFORMAT = userCLIPFORMAT.PTR()
    CLIPFORMAT = WORD
    
    # #########################################################################
    #
    #  Good for most of the gdi handles.
    
    class GDI_NONREMOTE(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', UP_DWORD_BLOB)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[DWORD_BLOB]
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  HGLOBAL
    #
    # A global may be Null or may be non-NULL with 0 length.
    
    class userHGLOBAL(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', UP_FLAGGED_BYTE_BLOB),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[FLAGGED_BYTE_BLOB]
        hInproc64: int
        fContext: int
        hInproc: int
    
    wireHGLOBAL = userHGLOBAL.PTR()
    
    # #########################################################################
    #
    #  HMETAFILE
    #
    
    class userHMETAFILE(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', UP_BYTE_BLOB),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[BYTE_BLOB]
        hInproc64: int
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  HMETAFILEPICT
    #
    class remoteMETAFILEPICT(CStructure):
        _fields_ = [
            ('mm', LONG),
            ('xExt', LONG),
            ('yExt', LONG),
            ('hMF', userHMETAFILE.PTR())
        ]
        
        hMF: IPointer[userHMETAFILE]
        xExt: int
        yExt: int
        mm: int
        
    class userHMETAFILEPICT(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', remoteMETAFILEPICT.PTR()),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[remoteMETAFILEPICT]
        hInproc64: int
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  HENHMETAFILE
    #
    
    class userHENHMETAFILE(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', UP_BYTE_BLOB),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[BYTE_BLOB]
        hInproc64: int
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  HBITMAP
    #

    # RemHBITMAP was just a byte blob, but the whole bitmap structure was copied
    # at the beginning of the buffer.

    # So, we take BITMAP fields from wingdi.x
    
    class userBITMAP(CStructure):
        _fields_ = [
            ('bmType', LONG),
            ('bmWidth', LONG),
            ('bmHeight', LONG),
            ('bmWidthBytes', LONG),
            ('bmPlanes', WORD),
            ('bmBitsPixel', WORD),
            ('cbSize', ULONG)
        ]
        
        pBuffer: IPointer[byte]
        bmWidthBytes: int
        bmBitsPixel: int
        bmHeight: int
        bmPlanes: int
        bmWidth: int
        bmType: int
        cbSize: int
        
    array_after_structure(userBITMAP, 'pBuffer', byte)
    
    class userHBITMAP(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', userBITMAP.PTR()),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[userBITMAP]
        hInproc64: int
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  HPALETTE
    #

    # PALETTEENTRY is in wingdi.x, it is a struct with 4 bytes.
    # LOGPALETTE   is in wingdi.x, it is a conf struct with paletteentries and
    #                                    a version field

    class userHPALETTE(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', PLOGPALETTE),
                ('hInproc64', INT64)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        hRemote: IPointer[LOGPALETTE]
        hInproc64: int
        fContext: int
        hInproc: int
    
    # #########################################################################
    #
    #  Handles passed locally as longs.
    #
    
    class RemotableHandle(CStructure):
        class U(CUnion):
            _fields_ = [
                ('hInproc', LONG),
                ('hRemote', LONG)
            ]
        _fields_ = [
            ('fContext', LONG),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        fContext: int
        hRemote: int
        hInproc: int
    
    wireHWND = wireHMENU = wireHACCEL = \
        wireHBRUSH = wireHFONT = wireHDC = \
        wireHICON = wireHRGN = wireHMONITOR = RemotableHandle.PTR()
        
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
    PTEXTMETRICW = LPTEXTMETRICW = TEXTMETRICW.PTR()
    
    wireHBITMAP = userHBITMAP.PTR()
    wireHPALETTE = userHPALETTE.PTR()
    wireHENHMETAFILE = userHENHMETAFILE.PTR()
    wireHMETAFILE = userHMETAFILE.PTR()
    wireHMETAFILEPICT = userHMETAFILEPICT.PTR()
    
    DATE = DOUBLE
    
    class CY(CStructure):
        _fields_ = [('int64', LONGLONG)]
        
        int64: int
    
    LPCY = CY.PTR()
    
    import decimal
    
    class DEC(CStructure):
        _fields_ = [
            ('wReserved', USHORT),
            ('scale', BYTE),
            ('sign', BYTE),
            ('Hi32', ULONG),
            ('Lo64', ULONGLONG)
        ]
        
        scale: int
        sign: int
        Hi32: int
        Lo64: int
        
        def as_decimal(self) -> decimal.Decimal:
            digits = (self.Hi32 << 64) + self.Lo64
            sign = "-" if self.sign else ""
            return decimal.Decimal(f"{sign}{digits}e-{self.scale}")
    
    DECIMAL = DEC
    
    DECIMAL_NEG = 0x80
    def DECIMAL_SETZERO(dec: DEC):
        dec.scale = 0
        dec.Lo64 = 0
        dec.Hi32 = 0
        dec.sign = 0
        
    LPDECIMAL = DECIMAL.PTR()
    
    wireBSTR = UP_FLAGGED_WORD_BLOB
    # BSTR definition in win.com.bstr
    
    # 0 == FALSE, -1 == TRUE
    VARIANT_BOOL = SHORT
    def VARIANT_BOOL_ToBool(boolVal: int) -> bool:
        return boolVal == -1
    
    VARIANT_FALSE = 0
    VARIANT_TRUE = -1
    
    # The BSTRBLOB structure is used by some implementations
    # of the IPropertyStorage interface when marshaling BSTRs
    # on systems which don't support BSTR marshaling. 
    class BSTRBLOB(CStructure):
        _fields_ = [
            ('cbSize', ULONG),
            ('pData', PBYTE)
        ]
    LPBSTRBLOB = BSTRBLOB.PTR()
    
    class CLIPDATA(CStructure):
        _fields_ = [
            ('cbSize', ULONG),    # count that includes sizeof(ulClipFmt)
            ('ulClipFmt', LONG),  # LONG to keep alignment
            ('pClipData', PBYTE)  # cbSize-sizeof(ULONG) bytes of data in clipboard format
        ]
        
        pClipData: PBYTE
        ulClipFmt: int
        cbSize: int
       
    def CBPCLIPDATA(clipdata: CLIPDATA):
        """
        Macro to calculate the size of the above pClipData
        """
        return (clipdata.cbSize - sizeof(LONG))
    
    VARTYPE = USHORT

    # #########################################################################
    #
    #  VARTYPE
    #
    # #########################################################################


    """
     * VARENUM usage key,
     *
     * * [V] - may appear in a VARIANT
     * * [T] - may appear in a TYPEDESC
     * * [P] - may appear in an OLE property set
     * * [S] - may appear in a Safe Array
     *
     *
     *  VT_EMPTY            [V]   [P]     nothing
     *  VT_NULL             [V]   [P]     SQL style Null
     *  VT_I2               [V][T][P][S]  2 byte signed int
     *  VT_I4               [V][T][P][S]  4 byte signed int
     *  VT_R4               [V][T][P][S]  4 byte real
     *  VT_R8               [V][T][P][S]  8 byte real
     *  VT_CY               [V][T][P][S]  currency
     *  VT_DATE             [V][T][P][S]  date
     *  VT_BSTR             [V][T][P][S]  OLE Automation string
     *  VT_DISPATCH         [V][T]   [S]  IDispatch *
     *  VT_ERROR            [V][T][P][S]  SCODE
     *  VT_BOOL             [V][T][P][S]  True=-1, False=0
     *  VT_VARIANT          [V][T][P][S]  VARIANT *
     *  VT_UNKNOWN          [V][T]   [S]  IUnknown *
     *  VT_DECIMAL          [V][T]   [S]  16 byte fixed point
     *  VT_RECORD           [V]   [P][S]  user defined type
     *  VT_I1               [V][T][P][s]  signed char
     *  VT_UI1              [V][T][P][S]  unsigned char
     *  VT_UI2              [V][T][P][S]  unsigned short
     *  VT_UI4              [V][T][P][S]  ULONG
     *  VT_I8                  [T][P]     signed 64-bit int
     *  VT_UI8                 [T][P]     unsigned 64-bit int
     *  VT_INT              [V][T][P][S]  signed machine int
     *  VT_UINT             [V][T]   [S]  unsigned machine int
     *  VT_INT_PTR             [T]        signed machine register size width
     *  VT_UINT_PTR            [T]        unsigned machine register size width
     *  VT_VOID                [T]        C style void
     *  VT_HRESULT             [T]        Standard return type
     *  VT_PTR                 [T]        pointer type
     *  VT_SAFEARRAY           [T]        (use VT_ARRAY in VARIANT)
     *  VT_CARRAY              [T]        C style array
     *  VT_USERDEFINED         [T]        user defined type
     *  VT_LPSTR               [T][P]     null terminated string
     *  VT_LPWSTR              [T][P]     wide null terminated string
     *  VT_FILETIME               [P]     FILETIME
     *  VT_BLOB                   [P]     Length prefixed bytes
     *  VT_STREAM                 [P]     Name of the stream follows
     *  VT_STORAGE                [P]     Name of the storage follows
     *  VT_STREAMED_OBJECT        [P]     Stream contains an object
     *  VT_STORED_OBJECT          [P]     Storage contains an object
     *  VT_VERSIONED_STREAM       [P]     Stream with a GUID version
     *  VT_BLOB_OBJECT            [P]     Blob contains an object 
     *  VT_CF                     [P]     Clipboard format
     *  VT_CLSID                  [P]     A Class ID
     *  VT_VECTOR                 [P]     simple counted array
     *  VT_ARRAY            [V]           SAFEARRAY*
     *  VT_BYREF            [V]           void* for local use
     *  VT_BSTR_BLOB                      Reserved for system use
    """

    VT_EMPTY           = 0
    VT_NULL            = 1
    VT_I2              = 2
    VT_I4              = 3
    VT_R4              = 4
    VT_R8              = 5
    VT_CY              = 6
    VT_DATE            = 7
    VT_BSTR            = 8
    VT_DISPATCH        = 9
    VT_ERROR           = 10
    VT_BOOL            = 11
    VT_VARIANT         = 12
    VT_UNKNOWN         = 13
    VT_DECIMAL         = 14
# VBA reserves 15 for future use
    VT_I1              = 16
    VT_UI1             = 17
    VT_UI2             = 18
    VT_UI4             = 19
    VT_I8              = 20
    VT_UI8             = 21
    VT_INT             = 22
    VT_UINT            = 23
    VT_VOID            = 24
    VT_HRESULT         = 25
    VT_PTR             = 26
    VT_SAFEARRAY       = 27
    VT_CARRAY          = 28
    VT_USERDEFINED     = 29
    VT_LPSTR           = 30
    VT_LPWSTR          = 31
# VBA reserves 32-35 for future use
    VT_RECORD          = 36
    VT_INT_PTR         = 37
    VT_UINT_PTR        = 38	

    VT_FILETIME        = 64
    VT_BLOB            = 65
    VT_STREAM          = 66
    VT_STORAGE         = 67
    VT_STREAMED_OBJECT = 68
    VT_STORED_OBJECT   = 69
    VT_BLOB_OBJECT     = 70
    VT_CF              = 71
    VT_CLSID           = 72
    VT_VERSIONED_STREAM= 73

    VT_BSTR_BLOB       = 0x0fff

    VT_VECTOR          = 0x1000
    VT_ARRAY           = 0x2000
    VT_BYREF           = 0x4000
    VT_RESERVED        = 0x8000

    VT_ILLEGAL         = 0xffff
    VT_ILLEGALMASKED   = 0x0fff
    VT_TYPEMASK        = 0x0fff
    VARENUM = INT


    # Property stuff
    PROPID = ULONG
    class PROPERTYKEY(CStructure):
        _fields_ = [
            ('fmtid', GUID),
            ('pid', DWORD)
        ]
        
        fmtid: GUID
        pid: int

    # Class Store types

    #
    # Platform/Architecture Definition
    #
    class CSPLATFORM(CStructure):
        _fields_ = [
            ('dwPlatformId', DWORD),      # This is the OS Platform
            ('dwVersionHi', DWORD),      # Major Version of OS
            ('dwVersionLo', DWORD),      # Minor Version of OS
            ('dwProcessorArch', DWORD)   # This is the Processor Architecure
        ]
        
        dwProcessorArch: int
        dwPlatformId: int
        dwVersionHi: int
        dwVersionLo: int
        
    #
    # Query Context Structure
    # This contains a list of attributes used to look up a class implementation
    #
    class QUERYCONTEXT(CStructure):
        _fields_ = [
            ('dwContext', DWORD),         # Execution context
            ('Platform', CSPLATFORM),     # Client Platform/Architecture
            ('Locale', LCID),             # Locale ID
            ('dwVersionHi', DWORD),       # Low Version number
            ('dwVersionLo', DWORD),       # Hi Version number
        ]
        
        dwVersionHi: int
        dwVersionLo: int
        dwContext: int
        Platform: int
        Locale: int

    #
    # Class Specifier structure
    # All means of mapping to a Class ID
    # (Union of CLSID, File Extension, ProgId, MimeType, File Ext)
    #
    
    TYSPEC_CLSID = 0
    TYSPEC_FILEEXT = 1
    TYSPEC_MIMETYPE = 2
    TYSPEC_FILENAME = 3
    TYSPEC_PROGID = 4
    TYSPEC_PACKAGENAME = 5
    TYSPEC_OBJECTID = 6
    TYSPEC = INT

    class uCLSSPEC(CStructure):
        class U(CUnion):
            class _ByName(CStructure):
                _fields_ = [
                    ('pPackageName', LPOLESTR),
                    ('PolicyId', GUID)
                ]
            class _ByObjectId(CStructure):
                _fields_ = [
                    ('ObjectId', GUID),
                    ('PolicyId', GUID)
                ]
            _fields_ = [
                ('clsid', CLSID),
                ('pFileExt', LPOLESTR),
                ('pMimeType', LPOLESTR),
                ('pProgId', LPOLESTR),
                ('pFileName', LPOLESTR),
                ('ByName', _ByName),
                ('ByObjectId', _ByObjectId)
            ]
        _fields_ = [
            ('tyspec', DWORD),
            ('u', U)
        ]
        _anonymous_ = ['u']
        
        ByObjectID: U._ByObjectId
        ByName: U._ByName
        
        pMimeType: LPOLESTR
        pFileName: LPOLESTR
        pFileExt: LPOLESTR
        pProgId: LPOLESTR
        
        clsid: CLSID
        tyspec: int