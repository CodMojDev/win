from .ctlinterfacedef import *

#############################################################################
## OCPFIPARAMS structure - parameters for OleCreatePropertyFrameIndirect

class OCPFIPARAMS(CStructure):
    _fields_ = [
        ('cbStructSize', ULONG),
        ('hWndOwner', HWND),
        ('x', INT),
        ('y', INT),
        ('lpszCaption', LPCOLESTR),
        ('cObjects', ULONG),
        ('lplpUnk', PTR(LPUNKNOWN)),
        ('cPages', ULONG),
        ('lpPages', LPCLSID),
        ('lcid', LCID),
        ('dispidInitialProperty', DISPID)
    ]
    cbStructSize: int
    hWndOwner: int
    x: int
    y: int
    lpszCaption: LPCOLESTR
    cObjects: int
    lplpUnk: IDoublePtr[IUnknown]
    cPages: int
    lpPages: IPointer[CLSID]
    lcid: int
    dispidInitialProperty: int

LPOCPFIPARAMS = PTR(OCPFIPARAMS)

##############################
## FONTDESC structure

def FONTISZE(n: int) -> CY: return CY(n * 10000)

class FONTDESC(CStructure):
    _fields_ = [
        ('cbSizeofstruct', UINT),
        ('lpstrName', LPOLESTR),
        ('cySize', CY),
        ('sWeight', SHORT),
        ('sCharset', SHORT),
        ('fItalic', BOOL),
        ('fUnderline', BOOL),
        ('fStrikethrough', BOOL)
    ]
    cbSizeofstruct: int
    lpstrName: LPOLESTR
    cySize: CY
    sWeight: int
    sCharset: int
    fItalic: int
    fUnderline: int
    fStrikethrough: int
    
LPFONTDESC = PTR(FONTDESC)

#############################
## PICTDESC structure

PICTYPE_UNINITIALIZED   = (-1)
PICTYPE_NONE            = 0
PICTYPE_BITMAP          = 1
PICTYPE_METAFILE        = 2
PICTYPE_ICON            = 3
PICTYPE_ENHMETAFILE     = 4

class PICTDESC(CStructure):
    class _U(CUnion):
        class Bmp(CStructure):
            _fields_ = [
                ('hbitmap', HBITMAP),
                ('hpal', HPALETTE)
            ]
            hbitmap: int
            hpal: int
        class Wmf(CStructure):
            _fields_ = [
                ('hmeta', HMETAFILE),
                ('xExt', INT),
                ('yExt', INT)
            ]
            hmeta: int
            xExt: int
            yExt: int
        class Icon(CStructure):
            _fields_ = [
                ('hicon', HICON)
            ]
            hicon: int
        class Emf(CStructure):
            _fields_ = [
                ('hemf', HENHMETAFILE)
            ]
            hemf: int
        _fields_ = [
            ('bmp', Bmp),
            ('wmf', Wmf),
            ('icon', Icon),
            ('emf', Emf)
        ]
    _fields_ = [
        ('cbSizeofStruct', UINT),
        ('picType', UINT),
        ('_u', _U)
    ]
    _anonymous_ = ['_u']
    cbSizeofStruct: int
    picType: int
    bmp: _U.Bmp
    wmf: _U.Wmf
    icon: _U.Icon
    emf: _U.Emf
    
LPPICTDESC = PTR(PICTDESC)

########################################
## Typedefs for standard scalar types

OLE_XPOS_PIXELS = LONG
OLE_YPOS_PIXELS = LONG
OLE_XSIZE_PIXELS = LONG
OLE_YSIZE_PIXELS = LONG
OLE_XPOS_CONTAINER = FLOAT
OLE_YPOS_CONTAINER = FLOAT
OLE_XSIZE_CONTAINER = FLOAT
OLE_YSIZE_CONTAINER = FLOAT
triUnchecked = 0
triChecked = 1
triGray = 2
OLE_TRISTATE = UINT
OLE_OPTEXCLUSIVE = VARIANT_BOOL
OLE_CANCELBOOL = VARIANT_BOOL
OLE_ENABLEDEFAULTBOOL = VARIANT_BOOL

#############################
## OLEIVERB_ constants

OLEIVERB_PROPERTIES = (-7)

###############################################
## Variant type (VT_) tags for property sets

VT_STREAMED_PROPSET = 73  ##       [P]  Stream contains a property set
VT_STORED_PROPSET   = 74  ##       [P]  Storage contains a property set
VT_BLOB_PROPSET     = 75  ##       [P]  Blob contains a property set
VT_VERBOSE_ENUM     = 76  ##       [P]  Enum value with text string


#############################################################
## Variant type (VT_) tags that are just aliases for others

VT_COLOR            = VT_I4
VT_XPOS_PIXELS      = VT_I4
VT_YPOS_PIXELS      = VT_I4
VT_XSIZE_PIXELS     = VT_I4
VT_YSIZE_PIXELS     = VT_I4
VT_XPOS_HIMETRIC    = VT_I4
VT_YPOS_HIMETRIC    = VT_I4
VT_XSIZE_HIMETRIC   = VT_I4
VT_YSIZE_HIMETRIC   = VT_I4
VT_TRISTATE         = VT_I2
VT_OPTEXCLUSIVE     = VT_BOOL
VT_FONT             = VT_DISPATCH
VT_PICTURE          = VT_DISPATCH

#######################################
## Property frame APIs

@oleaut32.foreign(HRESULT, HWND, UINT, UINT, LPCOLESTR, ULONG, PVOID, ULONG, LPCLSID, LCID, DWORD, LPVOID)
def OleCreatePropertyFrame(hwndOwner: int, x: int, y: int, lpszCaption: LPCOLESTR, cObjects: int, ppUnk: WT_ADDRLIKE, cPages: int, pPageClsID: IPointer[CLSID], lcid: int, dwReserved: int, pvReserved: WT_ADDRLIKE) -> int: ...

@oleaut32.foreign(HRESULT, LPOCPFIPARAMS)
def OleCreatePropertyFrameIndirect(lpParams: IPointer[OCPFIPARAMS]) -> int: ...

#######################################
## Standard type APIs

@oleaut32.foreign(HRESULT, OLE_COLOR, HPALETTE, LPCOLORREF)
def OleTranslateColor(clr: int, hpal: int, lpcolorref: IPointer[COLORREF]) -> int: ...

@oleaut32.foreign(HRESULT, LPFONTDESC, REFIID, PVOID, intermediate_method=True)
def OleCreateFontIndirect(self, lpFontDesc: IPointer[FONTDESC], iid: IID, lplpvObj: WT_ADDRLIKE, **kwargs) -> int:
    return delegate(lpFontDesc, iid.ref(), lplpvObj)

@oleaut32.foreign(HRESULT, LPPICTDESC, REFIID, BOOL, PVOID, intermediate_method=True)
def OleCreatePictureIndirect(lpPictDesc: IPointer[PICTDESC], iid: IID, fOwn: bool, lplpvObj: WT_ADDRLIKE, **kwargs) -> int: 
    return delegate(lpPictDesc, iid.ref(), fOwn, lplpvObj)

@oleaut32.foreign(HRESULT, LPSTREAM, LONG, BOOL, REFIID, PVOID, intermediate_method=True)
def OleLoadPicture(lpstream: IPointer[IStream], lSize: int, fRunmode: int, iid: IID, lplpvObj: WT_ADDRLIKE, **kwargs) -> int:
    return delegate(lpstream, lSize, fRunmode, iid.ref(), lplpvObj)

@oleaut32.foreign(HRESULT, LPSTREAM, LONG, BOOL, REFIID, DWORD, DWORD, DWORD, PVOID, intermediate_method=True)
def OleLoadPictureEx(lpstream: IPointer[IStream], lSize: int, fRunmode: int, iid: IID, xSizeDesired: int, ySizeDesired: int, dwFlags: int, lplpvObj: WT_ADDRLIKE, **kwargs) -> int:
    return delegate(lpstream, lSize, fRunmode, iid.ref(), xSizeDesired, ySizeDesired, dwFlags, lplpvObj)

@oleaut32.foreign(HRESULT, LPOLESTR, LPUNKNOWN, DWORD, OLE_COLOR, REFIID, PVOID, intermediate_method=True)
def OleLoadPicturePath(szURLorPath: WT_LPWSTR, punkCaller: IPointer[IUnknown], dwReserved: int, clrReserved: int, iid: IID, ppvRet: WT_ADDRLIKE, **kwargs) -> int:
    return delegate(szURLorPath, punkCaller, dwReserved, clrReserved, iid.ref(), ppvRet)

@oleaut32.foreign(HRESULT, VARIANT, PTR(LPDISPATCH))
def OleLoadPictureFile(varFileName: VARIANT, lplpdispPicture: IDoublePtr[IDispatch]) -> int: ...

@oleaut32.foreign(HRESULT, VARIANT, DWORD, DWORD, DWORD, PTR(LPDISPATCH))
def OleLoadPictureFileEx(varFileName: VARIANT, xSizeDesired: int, ySizeDesired: int, dwFlags: int, lplpdispPicture: IDoublePtr[IDispatch]) -> int: ...

@oleaut32.foreign(HRESULT, LPDISPATCH, BSTR)
def OleSavePictureFile(lpdispPicture: IPointer[IDispatch], bstrFileName: BSTR) -> int: ...

@oleaut32.foreign(HCURSOR, HINSTANCE, HICON)
def OleIconToCursor(hinstExe: WT_ADDRLIKE, hIcon: WT_ADDRLIKE) -> int: ...

LP_DEFAULT      = 0x00
LP_MONOCHROME	= 0x01
LP_VGACOLOR     = 0x02
LP_COLOR        = 0x04