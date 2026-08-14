from win.gdiplustypes import *
from win.gdiplusenums import *
from .handle import *
from win.com.comdefbase import *
from win.defbase_errordef import *
from win.gdiplusinit import *
from .io import *

gdiplus = get_win_library('gdiplus.dll')

LPGPGFX = PVOID
LPGPBMP = PVOID
LPGPFONT = PVOID
LPGPICON = PVOID
LPGPFONTFAMILY = PVOID
LPGPFONTCOLLECTION = PVOID
LPGPPEN = PVOID
LPGPBRUSH = PVOID
LPGPCUSTOMLINECAP = PVOID
LPGPMATRIX = PVOID
LPGPIMAGE = PVOID
LPGPADJUSTABLEARROWCAP = PVOID
LPGPPATH = PVOID

GPSTATUS = DWORD

@gdiplus.foreign(GPSTATUS, HDC, PTR(LPGPGFX))
def GdipCreateFromHDC(hdc: int | HANDLE, graphics: IPointer[LPGPGFX]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX)
def GdipDeleteGraphics(graphics: LPGPGFX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, HDC, PTR(LPGPFONT))
def GdipCreateFontFromDC(hdc: int | HANDLE, font: IPointer[LPGPFONT]) -> int: ...

@gdiplus.foreign(GPSTATUS, HDC, LPLOGFONTW, PTR(LPGPFONT))
def GdipCreateFontFromLogfontW(hdc: int | HANDLE, logfont: IPointer[LOGFONT], font: IPointer[LPGPFONT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, PTR(LPGPFONT))
def GdipCloneFont(font: LPGPFONT | int, cloneFont: IPointer[LPGPFONT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT)
def GdipDeleteFont(font: LPGPFONT | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, LPFLOAT)
def GdipGetFontSize(font: LPGPFONT | int, size: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, PINT)
def GdipGetFontStyle(font: LPGPFONT | int, style: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, PTR(Unit))
def GdipGetFontUnit(font: LPGPFONT | int, unit: IPointer[Unit]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, FLOAT, PFLOAT)
def GdipGetFontHeightGivenDPI(font: LPGPFONT | int, dpi: float, height: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, LPGPGFX, PFLOAT)
def GdipGetFontHeight(font: LPGPFONT | int, graphics: LPGPGFX | int, height: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, LPGPGFX, LPLOGFONTW)
def GdipGetLogFontW(font: LPGPFONT | int, graphics: LPGPGFX | int, logfont: IPointer[LOGFONTW]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTFAMILY)
def GdipDeleteFontFamily(fontFamily: LPGPFONTFAMILY | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, PTR(LPGPFONT))
def GdipCloneFontFamily(FontFamily: LPGPFONTFAMILY | int, clonedFontFamily: IPointer[LPGPFONTFAMILY]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONT))
def GdipGetGenericFontFamilySansSerif(nativeFamily: IPointer[LPGPFONTFAMILY]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONT))
def GdipGetGenericFontFamilySerif(nativeFamily: IPointer[LPGPFONTFAMILY]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONT))
def GdipGetGenericFontFamilyMonospace(nativeFamily: IPointer[LPGPFONTFAMILY]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONT, PTR(LPGPFONTFAMILY))
def GdipGetFamily(font: LPGPFONT | int, family: IPointer[LPGPFONTFAMILY]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTFAMILY, FLOAT, INT, Unit, PTR(LPGPFONT))
def GdipCreateFont(family: LPGPFONTFAMILY | int, emSize: float, style: int, unit: int, font: IPointer[LPGPFONT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTCOLLECTION, PINT)
def GdipGetFontCollectionFamilyCount(fontCollection: LPGPFONTCOLLECTION | int, numFound: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTCOLLECTION, INT, PTR(LPGPFONTFAMILY), PINT)
def GdipGetFontCollectionFamilyList(fontCollection: LPGPFONTCOLLECTION | int, numSought: int, gpfamilies: IPointer[LPGPFONTCOLLECTION], numFound: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONTCOLLECTION))
def GdipDeletePrivateFontCollection(fontCollection: IPointer[LPGPFONTCOLLECTION]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTCOLLECTION, LPWSTR)
def GdipPrivateAddFontFile(fontCollection: LPGPFONTCOLLECTION | int, filename: WT_LPWSTR) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPFONTCOLLECTION, PVOID, INT)
def GdipPrivateAddMemoryFont(fontCollection: LPGPFONTCOLLECTION | int, memory: WT_ADDRLIKE, length: int) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONTCOLLECTION))
def GdipNewInstalledFontCollection(fontCollection: IPointer[LPGPFONTCOLLECTION]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPFONTCOLLECTION))
def GdipNewPrivateFontCollection(fontCollection: IPointer[LPGPFONTCOLLECTION]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN)
def GdipDeletePen(pen: LPGPPEN | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LPGPPEN))
def GdipClonePen(pen: LPGPPEN | int, clonepen: IPointer[LPGPPEN]) -> int: ...

@gdiplus.foreign(GPSTATUS, DWORD, FLOAT, Unit, PTR(LPGPPEN))
def GdipCreatePen1(color: int, width: float, unit: int, pen: IPointer[LPGPPEN]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPBRUSH, FLOAT, Unit, PTR(LPGPPEN))
def GdipCreatePen2(brush: LPGPBRUSH | int, width: float, unit: int, pen: IPointer[LPGPPEN]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT)
def GdipSetPenWidth(pen: LPGPPEN | int, width: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT)
def GdipGetPenWidth(pen: LPGPPEN | int, width: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, Unit)
def GdipSetPenUnit(pen: LPGPPEN | int, unit: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(Unit))
def GdipGetPenUnit(pen: LPGPPEN | int, unit: IPointer[Unit]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LineCap, LineCap, DashCap)
def GdipSetPenLineCap197819(pen: LPGPPEN | int, startCap: int, endCap: int, dashCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LineCap)
def GdipSetPenStartCap(pen: LPGPPEN | int, startCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LineCap)
def GdipSetPenEndCap(pen: LPGPPEN | int, endCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, DashCap)
def GdipSetPenDashCap197819(pen: LPGPPEN | int, dashCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LineCap))
def GdipGetPenStartCap(pen: LPGPPEN | int, startCap: IPointer[LineCap]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LineCap))
def GdipGetPenEndCap(pen: LPGPPEN | int, endCap: IPointer[LineCap]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(DashCap))
def GdipGetPenDashCap197819(pen: LPGPPEN | int, dashCap: IPointer[DashCap]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LineJoin)
def GdipSetPenLineJoin(pen: LPGPPEN | int, lineJoin: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LineJoin))
def GdipGetPenLineJoin(pen: LPGPPEN | int, lineJoin: IPointer[LineJoin]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPCUSTOMLINECAP)
def GdipSetPenCustomStartCap(pen: LPGPPEN | int, customCap: LPGPCUSTOMLINECAP | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LPGPCUSTOMLINECAP))
def GdipGetPenCustomStartCap(pen: LPGPPEN | int, customCap: IPointer[LPGPCUSTOMLINECAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPCUSTOMLINECAP)
def GdipSetPenCustomEndCap(pen: LPGPPEN | int, customCap: LPGPCUSTOMLINECAP | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LPGPCUSTOMLINECAP))
def GdipGetPenCustomEndCap(pen: LPGPPEN | int, customCap: IPointer[LPGPCUSTOMLINECAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT)
def GdipSetPenMiterLimit(pen: LPGPPEN | int, miterLimit: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT)
def GdipGetPenMiterLimit(pen: LPGPPEN | int, miterLimit: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PenAlignment)
def GdipSetPenMode(pen: LPGPPEN | int, penMode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(PenAlignment))
def GdipGetPenMode(pen: LPGPPEN | int, penMode: IPointer[PenAlignment]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPMATRIX)
def GdipSetPenTransform(pen: LPGPPEN | int, matrix: LPGPMATRIX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPMATRIX)
def GdipGetPenTransform(pen: LPGPPEN | int, matrix: LPGPMATRIX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN)
def GdipResetPenTransform(pen: LPGPPEN | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPMATRIX, MatrixOrder)
def GdipMultiplyPenTransform(pen: LPGPPEN | int, matrix: LPGPMATRIX | int, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT, FLOAT, MatrixOrder)
def GdipTranslatePenTransform(pen: LPGPPEN | int, dx: float, dy: float, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT, FLOAT, MatrixOrder)
def GdipScalePenTransform(pen: LPGPPEN | int, sx: float, sy: float, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT, MatrixOrder)
def GdipRotatePenTransform(pen: LPGPPEN | int, angle: float, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, DWORD)
def GdipSetPenColor(pen: LPGPPEN | int, argb: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PDWORD)
def GdipGetPenColor(pen: LPGPPEN | int, argb: IPointer[DWORD]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, LPGPBRUSH)
def GdipSetPenBrushFill(pen: LPGPPEN | int, brush: LPGPBRUSH | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(LPGPBRUSH))
def GdipGetPenBrushFill(pen: LPGPPEN | int, brush: IPointer[LPGPBRUSH]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(PenType))
def GdipGetPenFillType(pen: LPGPPEN | int, type: IPointer[PenType]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PTR(DashStyle))
def GdipGetPenDashStyle(pen: LPGPPEN | int, dashstyle: IPointer[DashStyle]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, DashStyle)
def GdipSetPenDashStyle(pen: LPGPPEN | int, dashstyle: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT)
def GdipGetPenDashOffset(pen: LPGPPEN | int, offset: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, FLOAT)
def GdipSetPenDashOffset(pen: LPGPPEN | int, offset: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PINT)
def GdipGetPenDashCount(pen: LPGPPEN | int, count: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT, INT)
def GdipSetPenDashArray(pen: LPGPPEN | int, dash: IPointer[FLOAT], count: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT, INT)
def GdipGetPenDashArray(pen: LPGPPEN | int, dash: IPointer[FLOAT], count: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PINT)
def GdipGetPenCompoundCount(pen: LPGPPEN | int, count: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT, INT)
def GdipSetPenCompoundArray(pen: LPGPPEN | int, dash: IPointer[FLOAT], count: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPEN, PFLOAT, INT)
def GdipGetPenCompoundArray(pen: LPGPPEN | int, dash: IPointer[FLOAT], count: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPPATH, LPGPPATH, LineCap, FLOAT, PTR(LPGPCUSTOMLINECAP))
def GdipCreateCustomLineCap(fillPath: LPGPPATH | int, strokePath: LPGPPATH | int, baseCap: int, baseInset: float, customCap: IPointer[LPGPCUSTOMLINECAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP)
def GdipDeleteCustomLineCap(customCap: LPGPCUSTOMLINECAP | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PTR(LPGPCUSTOMLINECAP))
def GdipCloneCustomLineCap(customCap: LPGPCUSTOMLINECAP | int, clonedCap: IPointer[LPGPCUSTOMLINECAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PTR(CustomLineCapType))
def GdipGetCustomLineCapType(customCap: LPGPCUSTOMLINECAP | int, capType: IPointer[CustomLineCapType]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, LineCap, LineCap)
def GdipSetCustomLineCapStrokeCaps(customCap: LPGPCUSTOMLINECAP | int, startCap: int, endCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PTR(LineCap), PTR(LineCap))
def GdipGetCustomLineCapStrokeCaps(customCap: LPGPCUSTOMLINECAP | int, startCap: IPointer[LineCap], endCap: IPointer[LineCap]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, LineJoin)
def GdipSetCustomLineCapStrokeJoin(customCap: LPGPCUSTOMLINECAP | int, lineJoin: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PTR(LineJoin))
def GdipGetCustomLineCapStrokeJoin(customCap: LPGPCUSTOMLINECAP | int, lineJoin: IPointer[LineJoin]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, LineCap)
def GdipSetCustomLineCapBaseCap(customCap: LPGPCUSTOMLINECAP | int, baseCap: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PTR(LineCap))
def GdipGetCustomLineCapBaseCap(customCap: LPGPCUSTOMLINECAP | int, baseCap: IPointer[LineCap]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, FLOAT)
def GdipSetCustomLineCapBaseInset(customCap: LPGPCUSTOMLINECAP | int, inset: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PFLOAT)
def GdipGetCustomLineCapBaseInset(customCap: LPGPCUSTOMLINECAP | int, inset: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, FLOAT)
def GdipSetCustomLineCapWidthScale(customCap: LPGPCUSTOMLINECAP | int, widthScale: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPCUSTOMLINECAP, PFLOAT)
def GdipGetCustomLineCapWidthScale(customCap: LPGPCUSTOMLINECAP | int, widthScale: IPointer[FLOAT]) -> int: ...



class GdipError(RuntimeError):
    GDIP_ERROR_MAP: dict[int, int] = {
        Ok: S_OK,
        GenericError: E_FAIL,
        InvalidParameter: E_INVALIDARG,
        ObjectBusy: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_BUSY),
        InsufficientBuffer: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_INSUFFICIENT_BUFFER),
        NotImplemented: E_NOTIMPL,
        Aborted: E_ABORT,
        FileNotFound: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_FILE_NOT_FOUND),
        ValueOverflow: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_ARITHMETIC_OVERFLOW),
        AccessDenied: E_ACCESSDENIED,
        UnknownImageFormat: HRESULT(0x88982F07).value, # WINCODEC_ERR_UNKNOWNIMAGEFORMAT
        FontFamilyNotFound: HRESULT(0x88985002).value, # DWRITE_E_NOFONT
        FontStyle: HRESULT(0x88985009).value, # DWRITE_E_UNSUPPORTEDOPERATION
        NotTrueTypeFont: HRESULT(0x88985000).value, # DWRITE_E_FILEFORMAT
        UnsupportedGdiplusVersion: HRESULT(0x88982F0B).value, # WINCODEC_ERR_UNSUPPORTEDVERSION
        PropertyNotFound: E_INVALIDARG,
        PropertyNotSupported: E_INVALIDARG,
        ProfileNotFound: MAKE_HRESULT(SEVERITY_ERORR, FACILITY_WIN32, ERROR_PROFILE_NOT_FOUND),
        GdiplusNotInitialized: HRESULT(0x88982F0C).value # WINCODEC_ERR_NOTINITIALIZED
    }
    
    def __init__(self, code: int):
        if code == Win32Error:
            code = MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, GetLastError())
        else:
            code = self.GDIP_ERROR_MAP.get(code, E_UNEXPECTED)
        super().__init__(f'{COMError(code)}')

class Gdiplus:
    @staticmethod
    def startup():
        """
        Initialize the GDI+.
        """
        status = GdiplusStartup()
        if status != Ok:
            raise GdipError(status)
        
    @staticmethod
    def shutdown(self):
        """
        Uninitialize the GDI+.
        """
        GdiplusShutdown()
    
    class Graphics(Handle):
        """
        The GDI+ graphics class.
        """
        
        @classmethod
        def create(cls, dc: int | HANDLE) -> 'Gdiplus.Graphics':
            """
            Create the GDI+ Graphics from `win.abs.core.handle.DC` or `HDC`.
            """
            gfx = Gdiplus.Graphics()
            status = GdipCreateFromHDC(dc, byref(gfx))
            if status != Ok:
                raise GdipError(status)
            return gfx
        
        def close(self):
            status = GdipDeleteGraphics(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
    class Font(Handle):
        """
        The GDI+ font.
        """
        
        @classmethod
        def create(cls, family: 'Gdiplus.FontFamily', em: int, style: int, unit: int) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from GDI+ font family, size in EM, font style and unit enumeration.
            """
            font = Gdiplus.Font()
            status = GdipCreateFont(family, em, style, unit, byref(font))
            if status != Ok:
                raise GdipError(status)
            return font
        
        @classmethod
        def from_dc(cls, dc: int | HANDLE) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from `win.abs.core.handle.DC` or `HDC`.
            """
            font = Gdiplus.Font()
            status = GdipCreateFontFromDC(dc, byref(dc))
            if status != Ok:
                raise GdipError(status)
            return font
        
        @classmethod
        def from_font(cls, font: int | HANDLE) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from `win.abs.core.handle.Font` or `HFONT`.
            """
            with DC.create_compatible(None) as dc:
                return cls.from_dc(dc)
        
        @classmethod
        def indirect(cls, logfont: LOGFONTW) -> 'Gdiplus.Font':
            """
            Create the GDI+ font indirectly from `LOGFONTW`.
            """
            font = Gdiplus.Font()
            with DC.create_compatible(None) as dc:
                status = GdipCreateFontFromLogfontW(dc, logfont.ref(), byref(font))
            if status != Ok:
                raise GdipError(status)
            return font
        
        def close(self):
            status = GdipDeleteFont(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def clone(self) -> 'Gdiplus.Font':
            """
            Clone the GDI+ font.
            """
            font = Gdiplus.Font()
            status = GdipCloneFont(self, byref(font))
            if status != Ok:
                raise GdipError(status)
            return font
        
        @property
        def size(self) -> float:
            size = FLOAT()
            status = GdipGetFontSize(self, byref(size))
            if status != Ok:
                raise GdipError(status)
            return size.value
        
        @property
        def style(self) -> int:
            style = INT()
            status = GdipGetFontStyle(self, byref(style))
            if status != Ok:
                raise GdipError(status)
            return style.value
        
        @property
        def unit(self) -> int:
            unit = Unit()
            status = GdipGetFontUnit(self, byref(unit))
            if status != Ok:
                raise GdipError(status)
            return unit.value
        
        def font_height_for_dpi(self, dpi: float) -> float:
            """
            Get the GDI+ font height for given DPI.
            """
            height = FLOAT()
            status = GdipGetFontHeightGivenDPI(self, dpi, byref(height))
            if status != Ok:
                raise GdipError(status)
            return height.value
        
        def font_height(self, graphics: 'Gdiplus.Graphics') -> float:
            """
            Get the GDI+ font height for given graphics.
            """
            height = FLOAT()
            status = GdipGetFontHeight(self, graphics, byref(height))
            if status != Ok:
                raise GdipError(status)
            return height.value
        
        def logfont(self, graphics: 'Gdiplus.Graphics' | None = None) -> LOGFONTW:
            """
            Get the `LOGFONTW` from GDI+ font.
            """
            if graphics is None:
                with DC.create_compatible(None) as dc:
                    with Gdiplus.Graphics.create(dc) as graphics:
                        return self.logfont(graphics)
            else:
                logfont = LOGFONTW()
                status = GdipGetLogFontW(self, graphics, logfont.ref())
                if status != Ok:
                    raise GdipError(status)
                return logfont
            
        @property
        def family(self) -> 'Gdiplus.FontFamily':
            family = Gdiplus.FontFamily()
            status = GdipGetFamily(self, byref(family))
            if status != Ok:
                raise GdipError(status)
            return family
            
    class FontFamily(Handle):
        """
        The GDI+ font family.
        """
        
        @classmethod
        def serif(cls) -> 'Gdiplus.FontFamily':
            family = Gdiplus.FontFamily()
            status = GdipGetGenericFontFamilySerif(byref(family))
            if status != Ok:
                raise GdipError(status)
            return family
        
        @classmethod
        def sans_serif(cls) -> 'Gdiplus.FontFamily':
            family = Gdiplus.FontFamily()
            status = GdipGetGenericFontFamilySansSerif(byref(family))
            if status != Ok:
                raise GdipError(status)
            return family
        
        @classmethod
        def monospace(cls) -> 'Gdiplus.FontFamily':
            family = Gdiplus.FontFamily()
            status = GdipGetGenericFontFamilyMonospace(byref(family))
            if status != Ok:
                raise GdipError(status)
            return family
        
        def close(self):
            status = GdipDeleteFontFamily(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def clone(self) -> 'Gdiplus.FontFamily':
            """
            Clone the GDI+ font family.
            """
            family = Gdiplus.FontFamily()
            status = GdipCloneFontFamily(self, byref(family))
            if status != Ok:
                raise GdipError(status)
            return family
        
    class FontCollection(Handle):
        """
        The GDI+ font collection.
        """
        
        @property
        def family_count(self) -> int:
            count = INT()
            status = GdipGetFontCollectionFamilyCount(self, byref(count))
            if status != Ok:
                raise GdipError(status)
            return count.value
        
        @property
        def families(self) -> list['Gdiplus.FontFamily']:
            count = self.family_count
            families = (Gdiplus.FontFamily * count)()
            iUnused = INT()
            status = GdipGetFontCollectionFamilyList(self, count, families, byref(iUnused))
            if status != Ok:
                raise GdipError(status)
            return list(families)
        
    class PrivateFontCollection(FontCollection):
        """
        The GDI+ private font collection.
        """
        
        @classmethod
        def create(cls) -> 'Gdiplus.PrivateFontCollection':
            collection = Gdiplus.PrivateFontCollection()
            status = GdipNewPrivateFontCollection(byref(collection))
            if status != Ok:
                raise GdipError(status)
            return collection
        
        def close(self):
            status = GdipDeletePrivateFontCollection(byref(self))
            self._closed = True
        
        @overload
        def add(self, name: str):
            """
            Add the font file by name into private font collection.
            """
            
        @overload
        def add(self, memory: MemoryIO):
            """
            Add the memory font as `Memory I/O` into private font collection.
            """
        
        @overload
        def add(self, buffer: WT_ADDRLIKE, length: int):
            """
            Add the memory font file by buffer and length into private font collection.
            """
        
        def add(self, *args):
            if len(args) == 1:
                v, = args
                if isinstance(v, MemoryIO):
                    status = GdipPrivateAddMemoryFont(self, v.memory_address+v.memory_position, v.memory_size-v.memory_position)
                else:
                    status = GdipPrivateAddFontFile(self, name)
            else:
                buffer, length = args
                status = GdipPrivateAddMemoryFont(self, buffer, length)
            if status != Ok:
                raise GdipError(status)
            
    class InstalledFontCollection(FontCollection):
        """
        The GDI+ installed font collection.
        """
        
        @classmethod
        def create(cls) -> 'Gdiplus.InstalledFontCollection':
            collection = Gdiplus.InstalledFontCollection()
            status = GdipNewInstalledFontCollection(byref(collection))
            if status != Ok:
                raise GdipError(status)
            return collection
        
    class Pen(Handle):
        """
        The GDI+ pen.
        """
        @classmethod
        def create(cls, value: int | IColor, width: float = 1.0, unit: int = UnitPixel) -> 'Gdiplus.Pen':
            """
            Create the GDI+ pen from ARGB color, width and unit enumeration.
            """
            pen = Gdiplus.Pen()
            status = GdipCreatePen1(int(value), width, unit, byref(pen))
            if status != Ok:
                raise GdipError(status)
            return pen
        
        @classmethod
        def from_brush(cls, brush: 'Gdiplus.Brush', width: float = 1.0, unit: int = UnitPixel) -> 'Gdiplus.Pen':
            """
            Create the GDI+ pen from GDI+ brush, width and unit enumeration.
            """
            pen = Gdiplus.Pen()
            status = GdipCreatePen2(brush, width, unit, byref(pen))
            if status != Ok:
                raise GdipError(status)
            return pen
        
        def close(self):
            status = GdipDeletePen(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def clone(self) -> 'Gdiplus.Pen':
            """
            Clone the GDI+ pen.
            """
            pen = Gdiplus.Pen()
            status = GdipClonePen(self, byref(pen))
            if status != Ok:
                raise GdipError(status)
            return pen
        
        @property
        def width(self) -> float:
            width = FLOAT()
            status = GdipGetPenWidth(self, byref(width))
            if status != Ok:
                raise GdipError(status)
            return width.value
        
        @width.setter
        def width(self, width: float):
            status = GdipSetPenWidth(self, width)
            if status != Ok:
                raise GdipError(status)
            
        @property
        def unit(self) -> int:
            unit = Unit()
            status = GdipGetPenUnit(self, byref(unit))
            if status != Ok:
                raise GdipError(status)
            return unit.value
        
        @unit.setter
        def unit(self, unit: int):
            status = GdipSetPenUnit(self, unit)
            
        @property
        def miter_limit(self) -> float:
            limit = FLOAT()
            status = GdipGetPenMiterLimit(self, byref(limit))
            if status != Ok:
                raise GdipError(status)
            return limit.value
        
        @miter_limit.setter
        def miter_limit(self, miter_limit: float):
            status = GdipSetPenMiterLimit(self, miter_limit)
            if status != Ok:
                raise GdipError(status)
            
        @property
        def mode(self) -> int:
            mode = PenAlignment()
            status = GdipGetPenMode(self, byref(mode))
            if status != Ok:
                raise GdipError(status)
            return mode.value
        
        @mode.setter
        def mode(self, mode: int):
            status = GdipSetPenMode(self, mode)
            if status != Ok:
                raise GdipError(status)
            
        @property
        def color(self) -> Color.ARGB:
            color = DWORD()
            status = GdipGetPenColor(self, byref(color))
            if status != Ok:
                raise GdipError(status)
            return Color.ARGB(color.value)
        
        @color.setter
        def color(self, color: int | Color.IColor):
            status = GdipSetPenColor(self, int(color))
            if status != Ok:
                raise GdipError(status)
        
        @property
        def fill_type(self) -> int:
            fill_type = PenType()
            status = GdipGetPenFillType(self, byref(fill_type))
            if status != Ok:
                raise GdipError(status)
            return fill_type.value
        
        @property
        def line_join(self) -> int:
            line_join = LineJoin()
            status = GdipGetPenLineJoin(self, byref(line_join))
            if status != Ok:
                raise GdipError(status)
            return line_join.value
        
        @line_join.setter
        def line_join(self, line_join: int):
            status = GdipSetPenLineJoin(self, line_join)
            if status != Ok:
                raise GdipError(status)
        
    class SolidBrush(Handle):
        ...
        
    class HatchBrush(Handle):
        ...
        
    class Brush(Handle):
        ...
        
    class Image(Handle):
        ...
        
    class Bitmap(Handle):
        ...
        
    class Icon(Handle):
        ...
        
    class Region(Handle):
        ...