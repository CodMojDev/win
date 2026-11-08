from win import cpreproc
if cpreproc.ifndef("GDIPVER"):
    cpreproc.define("GDIPVER", 0x0100)

from win.gdiplustypes import *
from win.gdiplusenums import *
from .handle import *
from win.com.comdefbase import *
from win.defbase_errordef import *
from win.gdiplusinit import *
from .io import *
from win.com.comtl.streams import *
from win.gdipluscolormatrix import *
from win.gdipluspixelformats import *

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
LPGPSTRINGFORMAT = PVOID
LPGPBITMAP = PVOID
LPGPIMAGEATTRIBUTES = PVOID

GPSTATUS = DWORD

@gdiplus.foreign(GPSTATUS, HDC, PTR(LPGPGFX))
def GdipCreateFromHDC(hdc: int | HANDLE, graphics: IPointer[LPGPGFX]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX)
def GdipDeleteGraphics(graphics: LPGPGFX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, HDC, PTR(LPGPFONT))
def GdipCreateFontFromDC(hdc: int | HANDLE, font: IPointer[LPGPFONT]) -> int: ...

@gdiplus.foreign(GPSTATUS, HDC, LPLOGFONTW, PTR(LPGPFONT))
def GdipCreateFontFromLogfontW(hdc: int | HANDLE, logfont: IPointer[LOGFONTW], font: IPointer[LPGPFONT]) -> int: ...

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

# *****
@gdiplus.foreign(GPSTATUS, LPGPGFX, LPWSTR, INT, LPGPFONT, PTR(RectF), LPGPSTRINGFORMAT, LPGPBRUSH)
def GdipDrawString(graphics: LPGPGFX | int, string: WT_LPWSTR, length: int, font: LPGPFONT | int, layoutRect: IPointer[RectF], stringFormat: LPGPSTRINGFORMAT | int, brush: LPGPBRUSH | int) -> int: ...

# SolidFill
@gdiplus.foreign(GPSTATUS, LPGPBRUSH)
def GdipDeleteBrush(brush: LPGPBRUSH | int) -> int: ...

@gdiplus.foreign(GPSTATUS, DWORD, PTR(LPGPBRUSH))
def GdipCreateSolidFill(color: int, brush: IPointer[LPGPBRUSH]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPBRUSH, DWORD)
def GdipSetSolidFillColor(brush: LPGPBRUSH | int, color: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPBRUSH, PDWORD)
def GdipGetSolidFillColor(brush: LPGPBRUSH | int, color: IPointer[DWORD]) -> int: ...

# StringFormat
@gdiplus.foreign(GPSTATUS, INT, LANGID, PTR(LPGPSTRINGFORMAT))
def GdipCreateStringFormat(formatAttributes: int, language: int, format: IPointer[LPGPSTRINGFORMAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPSTRINGFORMAT))
def GdipStringFormatGetGenericDefault(format: IPointer[LPGPSTRINGFORMAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPSTRINGFORMAT))
def GdipStringFormatGetGenericTypographic(format: IPointer[LPGPSTRINGFORMAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, PTR(LPGPSTRINGFORMAT))
def GdipDeleteStringFormat(format: int | LPGPSTRINGFORMAT) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(LPGPSTRINGFORMAT))
def GdipCloneStringFormat(format: int | LPGPSTRINGFORMAT, newFormat: IPointer[LPGPSTRINGFORMAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, INT)
def GdipSetStringFormatFlags(format: int | LPGPSTRINGFORMAT, flags: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PINT)
def GdipGetStringFormatFlags(format: int | LPGPSTRINGFORMAT, flags: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, StringAlignment)
def GdipSetStringFormatAlign(self, format: int | LPGPSTRINGFORMAT, align: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(StringAlignment))
def GdipGetStringFormatAlign(self, format: int | LPGPSTRINGFORMAT, align: IPointer[StringAlignment]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, StringAlignment)
def GdipSetStringFormatLineAlign(self, format: int | LPGPSTRINGFORMAT, align: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(StringAlignment))
def GdipGetStringFormatLineAlign(self, format: int | LPGPSTRINGFORMAT, align: IPointer[StringAlignment]) -> int: ...


@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, StringTrimming)
def GdipSetStringFormatTrimming(self, format: int | LPGPSTRINGFORMAT, trimming: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(StringTrimming))
def GdipGetStringFormatTrimming(self, format: int | LPGPSTRINGFORMAT, trimming: IPointer[StringTrimming]) -> int: ...


@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, INT)
def GdipSetStringFormatHotkeyPrefix(self, format: int | LPGPSTRINGFORMAT, hotkeyPrefix: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(INT))
def GdipGetStringFormatHotkeyPrefix(self, format: int | LPGPSTRINGFORMAT, hotkeyPrefix: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, FLOAT, INT, PFLOAT)
def GdipSetStringFormatTabStops(self, format: int | LPGPSTRINGFORMAT, firstTabOffset: float, count: int, tabStops: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, INT, PFLOAT, PFLOAT)
def GdipGetStringFormatTabStops(self, format: int | LPGPSTRINGFORMAT, count: int, firstTabOffset: IPointer[FLOAT], tabStops: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PINT)
def GdipGetStringFormatTabStopCount(self, format: int | LPGPSTRINGFORMAT, count: IPointer[int]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, LANGID, StringDigitSubstitute)
def GdipSetStringFormatDigitSubstitution(self, format: int | LPGPSTRINGFORMAT, language: int, substitute: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(LANGID), PTR(StringDigitSubstitute))
def GdipGetStringFormatDigitSubstitution(self, format: int | LPGPSTRINGFORMAT, language: IPointer[LANGID], substitute: IPointer[StringDigitSubstitute]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, PTR(INT))
def GdipGetStringFormatMeasurableCharacterRangeCount(self, format: int | LPGPSTRINGFORMAT, count: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPSTRINGFORMAT, INT, PTR(CharacterRange))
def GdipSetStringFormatMeasurableCharacterRanges(self, format: int | LPGPSTRINGFORMAT, rangeCount: int, ranges: IPointer[CharacterRange]) -> int: ...

# Brush

@gdiplus.foreign(GPSTATUS, LPGPBRUSH, PTR(LPGPBRUSH))
def GdipCloneBrush(brush: LPGPBRUSH | int, cloneBrush: IPointer[LPGPBRUSH]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPBRUSH)
def GdipDeleteBrush(brush: LPGPBRUSH | int) -> int: ...

BrushTypeSolidColor     = 0
BrushTypeHatchFill      = 1
BrushTypeTextureFill    = 2
BrushTypePathGradient   = 3
BrushTypeLinearGradient = 4

@gdiplus.foreign(GPSTATUS, LPGPBRUSH, PTR(BrushType))
def GdipGetBrushType(brush: LPGPBRUSH | int, type: IPointer[BrushType]) -> int: ...

# Graphics

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPBRUSH, REAL, REAL, REAL, REAL)
def GdipFillRectangle(graphics: LPGPGFX | int, brush: LPGPBRUSH | int, x: int, y: int, width: int, height: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, CompositingMode)
def GdipSetCompositingMode(graphics: LPGPGFX | int, compositingMode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(CompositingMode))
def GdipGetCompositingMode(graphics: LPGPGFX | int, compositingMode: IPointer[CompositingMode]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, INT, INT)
def GdipSetRenderingOrigin(graphics: LPGPGFX | int, x: int, y: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PINT, PINT)
def GdipGetRenderingOrigin(graphics: LPGPGFX | int, x: IPointer[INT], y: IPointer[INT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, CompositingQuality)
def GdipSetCompositingQuality(graphics: LPGPGFX | int, compositingQuality: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(CompositingQuality))
def GdipGetCompositingQuality(graphics: LPGPGFX | int, compositingQuality: IPointer[CompositingQuality]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(SmoothingMode))
def GdipGetSmoothingMode(graphics: LPGPGFX | int, smoothingMode: IPointer[SmoothingMode]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, SmoothingMode)
def GdipSetSmoothingMode(graphics: LPGPGFX | int, smoothingMode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PixelOffsetMode)
def GdipSetPixelOffsetMode(graphics: LPGPGFX | int, pixelOffsetMode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(PixelOffsetMode))
def GdipGetPixelOffsetMode(graphics: LPGPGFX | int, pixelOffsetMode: IPointer[PixelOffsetMode]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, TextRenderingHint)
def GdipSetTextRenderingHint(graphics: LPGPGFX | int, mode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(TextRenderingHint))
def GdipGetTextRenderingHint(graphics: LPGPGFX | int, mode: IPointer[TextRenderingHint]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, UINT)
def GdipSetTextContrast(graphics: LPGPGFX | int, contrast: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(UINT))
def GdipGetTextContrast(graphics: LPGPGFX | int, contrast: IPointer[UINT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, InterpolationMode)
def GdipSetInterpolationMode(graphics: LPGPGFX | int, interpolationMode: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(InterpolationMode))
def GdipGetInterpolationMode(graphics: LPGPGFX | int, interpolationMode: IPointer[InterpolationMode]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPMATRIX)
def GdipSetWorldTransform(graphics: LPGPGFX | int, matrix: LPGPMATRIX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX)
def GdipResetWorldTransform(graphics: LPGPGFX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, MatrixOrder)
def GdipMultiplyWorldTransform(graphics: LPGPGFX | int, matrix: LPGPMATRIX | int, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, FLOAT, FLOAT, MatrixOrder)
def GdipTranslateWorldTransform(graphics: LPGPGFX | int, dx: float, dy: float, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, FLOAT, FLOAT, MatrixOrder)
def GdipScaleWorldTransform(graphics: LPGPGFX | int, sx: float, sy: float, order: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPMATRIX)
def GdipGetWorldTransform(graphics: LPGPGFX | int, matrix: LPGPMATRIX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX)
def GdipResetPageTransform(graphics: LPGPGFX | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(FLOAT))
def GdipGetDpiX(graphics: LPGPGFX | int, dpi: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, PTR(FLOAT))
def GdipGetDpiY(graphics: LPGPGFX | int, dpi: IPointer[FLOAT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, DWORD)
def GdipGraphicsClear(graphics: LPGPGFX | int, color: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE, FLOAT, FLOAT)
def GdipDrawImage(graphics: LPGPGFX | int, image: LPGPIMAGE | int, x: float, y: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE, INT, INT)
def GdipDrawImageI(graphics: LPGPGFX | int, image: LPGPIMAGE | int, x: int, y: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPIMAGE, FLOAT, FLOAT, FLOAT, FLOAT)
def GdipDrawImageRect(graphics: LPGPGFX | int, image: LPGPIMAGE | int, x: float, y: float, width: float, height: float) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPIMAGE, FLOAT, FLOAT, FLOAT, FLOAT, FLOAT, FLOAT, FLOAT, FLOAT, Unit, LPGPIMAGEATTRIBUTES, DrawImageAbort, PVOID)
def GdipDrawImageRectRect(graphics: LPGPGFX | int, image: LPGPIMAGE | int, dstx: float, dsty: float, dstwidth: float, dstheight: float, srcx: float, srcy: float, srcwidth: float, srcheight: float, srcUnit: int, imageAttributes: LPGPIMAGEATTRIBUTES | int, callback: FARPROC, callbackData: WT_ADDRLIKE) -> int: ...

# Image
@gdiplus.foreign(GPSTATUS, LPSTREAM, PTR(LPGPIMAGE))
def GdipLoadImageFromStream(stream: IPointer[IStream], image: IPointer[LPGPIMAGE]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPWSTR, PTR(LPGPIMAGE))
def GdipLoadImageFromFile(filename: WT_LPWSTR, image: IPointer[LPGPIMAGE]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE, PTR(LPGPIMAGE))
def GdipCloneImage(image: LPGPIMAGE | int, cloneImage: IPointer[LPGPIMAGE]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE)
def GdipDisposeImage(image: LPGPIMAGE | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE, PUINT)
def GdipGetImageWidth(image: LPGPIMAGE | int, width: IPointer[UINT]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGE, PUINT)
def GdipGetImageHeight(image: LPGPIMAGE | int, height: IPointer[UINT]) -> int: ...

# Bitmap
@gdiplus.foreign(GPSTATUS, HBITMAP, HPALETTE, PTR(LPGPBITMAP))
def GdipCreateBitmapFromHBITMAP(hbm: int, hpal: int, bitmap: IPointer[LPGPBITMAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, HICON, PTR(LPGPBITMAP))
def GdipCreateBitmapFromHICON(hicon: int, bitmap: IPointer[LPGPBITMAP]) -> int: ...

@gdiplus.foreign(GPSTATUS, FLOAT, FLOAT, FLOAT, FLOAT, PixelFormat, LPGPBITMAP, PTR(LPGPBITMAP))
def GdipCloneBitmapArea(x: float, y: float, width: float, height: float, format: int, srcBitmap: LPGPBITMAP | int, dstBitmap: IPointer[LPGPBITMAP]) -> int: ...

# ImageAttributes
@gdiplus.foreign(GPSTATUS, PTR(LPGPIMAGEATTRIBUTES))
def GdipCreateImageAttributes(imageattr: IPointer[LPGPIMAGEATTRIBUTES]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGEATTRIBUTES, PTR(LPGPIMAGEATTRIBUTES))
def GdipCloneImageAttributes(imageattr: LPGPIMAGEATTRIBUTES | int, cloneImageattr: IPointer[LPGPIMAGEATTRIBUTES]) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGEATTRIBUTES)
def GdipDisposeImageAttributes(imageattr: LPGPIMAGEATTRIBUTES | int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGEATTRIBUTES, ColorAdjustType)
def GdipResetImageAttributes(imageattr: LPGPIMAGEATTRIBUTES | int, type: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPIMAGEATTRIBUTES, ColorAdjustType, BOOL, PTR(ColorMatrix), PTR(ColorMatrix), ColorMatrixFlags)
def GdipSetImageAttributesColorMatrix(imageattr: LPGPIMAGEATTRIBUTES | int, type: int, enableFlag: int, colorMatrix: IPointer[ColorMatrix], grayMatrix: IPointer[ColorMatrix], flags: int) -> int: ...

@gdiplus.foreign(GPSTATUS, LPGPGFX, LPGPPEN, FLOAT, FLOAT, FLOAT, FLOAT)
def GdipDrawRectangle(graphics: LPGPGFX | int, pen: LPGPPEN | int, x: float, y: float, width: float, height: float) -> int: ...

# Text
@gdiplus.foreign(GPSTATUS, LPGPGFX, LPWSTR, INT, LPGPFONT, PTR(RectF), LPGPSTRINGFORMAT, PTR(RectF), PINT, PINT)
def GdipMeasureString(graphics: LPGPGFX | int, string: WT_LPWSTR, length: int, font: LPGPFONT | int, layoutRect: IPointer[RectF], stringFormat: LPGPSTRINGFORMAT | int, boundingBox: IPointer[RectF], codepointsFitted: IPointer[INT], linesFilled: IPointer[INT]) -> int: ...

# *****

class GdipError(RuntimeError):
    GDIP_ERROR_MAP: dict[int, int] = {
        Ok: S_OK,
        GenericError: E_FAIL,
        InvalidParameter: E_INVALIDARG,
        OutOfMemory: E_OUTOFMEMORY,
        ObjectBusy: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_BUSY),
        InsufficientBuffer: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_INSUFFICIENT_BUFFER),
        NotImplemented: E_NOTIMPL,
        Aborted: E_ABORT,
        FileNotFound: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_FILE_NOT_FOUND),
        ValueOverflow: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_ARITHMETIC_OVERFLOW),
        AccessDenied: E_ACCESSDENIED,
        UnknownImageFormat: HRESULT(0x88982F07).value, # WINCODEC_ERR_UNKNOWNIMAGEFORMAT
        FontFamilyNotFound: HRESULT(0x88985002).value, # DWRITE_E_NOFONT
        FontStyleNotFound: HRESULT(0x88985009).value, # DWRITE_E_UNSUPPORTEDOPERATION
        NotTrueTypeFont: HRESULT(0x88985000).value, # DWRITE_E_FILEFORMAT
        UnsupportedGdiplusVersion: HRESULT(0x88982F0B).value, # WINCODEC_ERR_UNSUPPORTEDVERSION
        PropertyNotFound: E_INVALIDARG,
        PropertyNotSupported: E_INVALIDARG,
        ProfileNotFound: MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_PROFILE_NOT_FOUND),
        GdiplusNotInitialized: HRESULT(0x88982F0C).value # WINCODEC_ERR_NOTINITIALIZED
    }
    
    def __init__(self, code: int):
        if code == Win32Error:
            code = MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, GetLastError())
        else:
            print(code)
            code = self.GDIP_ERROR_MAP.get(code, E_UNEXPECTED)
        super().__init__(f'{COMError(code)}')

class Gdiplus:
    def RectF_to_Rect(rect: RectF) -> Rect:
        return Rect.create(rect.X, rect.Y, rect.Width, rect.Height)
    
    def Rect_to_RectF(rect: RECT) -> RectF:
        return RectF(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
    
    TOKEN = ULONG_PTR()
    
    @classmethod
    def startup(cls):
        """
        Initialize the GDI+.
        """
        input = GdiplusStartupInput()
        status = GdiplusStartup(byref(cls.TOKEN), input.ref(), NULL)
        if status != Ok:
            raise GdipError(status)
        
    @classmethod
    def shutdown(cls):
        """
        Uninitialize the GDI+.
        """
        GdiplusShutdown(cls.TOKEN.value)
    
    class Graphics(Handle):
        """
        The GDI+ graphics class.
        """
        
        @classmethod
        def create(cls, dc: int | HANDLE) -> 'Gdiplus.Graphics':
            """
            Create the GDI+ Graphics from `win.abs.core.handle.DC` or `HDC`.
            """
            gfx = LPGPGFX()
            status = GdipCreateFromHDC(dc, byref(gfx))
            if status != Ok:
                raise GdipError(status)
            return cls(gfx.value)
        
        def close(self):
            status = GdipDeleteGraphics(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def draw_string(self, text: str, font: 'Gdiplus.Font', rect: RECT | RectF, brush: 'Gdiplus.Brush', format: TUnion['Gdiplus.StringFormat', None] = None):
            """
            Draw the string.
            """
            if isinstance(rect, RECT):
                rect = RectF(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
            status = GdipDrawString(self, text, len(text), font, rect.ref(), format, brush)
            if status != Ok:
                raise GdipError(status)
        
        @property
        def smoothing_mode(self) -> int:
            smoothing_mode = SmoothingMode()
            status = GdipGetSmoothingMode(self, byref(smoothing_mode))
            if status != Ok:
                raise GdipError(status)
            return smoothing_mode.value
        
        @smoothing_mode.setter
        def smoothing_mode(self, smoothing_mode: int):
            status = GdipSetSmoothingMode(self, smoothing_mode)
            if status != Ok:
                raise GdipError(status)
            
        def fill(self, rect: RECT | RectF, brush: 'Gdiplus.Brush'):
            if isinstance(rect, RECT):
                rect = RectF(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
            status = GdipFillRectangle(self, brush, rect.X, rect.Y, rect.Width, rect.Height)
            if status != Ok:
                raise GdipError(status)
            
        @property
        def compositing_mode(self) -> int:
            compositing_mode = CompositingMode()
            status = GdipGetCompositingMode(self, byref(compositing_mode))
            if status != Ok:
                raise GdipError(status)
            return compositing_mode.value
        
        @compositing_mode.setter
        def compositing_mode(self, compositing_mode: int):
            status = GdipSetCompositingMode(self, compositing_mode)
            if status != Ok:
                raise GdipError(status)
            
        def draw_image(self, image: 'Gdiplus.Image', x: float, y: float):
            status = GdipDrawImage(self, image, x, y)
            if status != Ok:
                raise GdipError(status)
            
        def draw_image_rect(self, image: 'Gdiplus.Image', x: float, y: float, width: float, height: float):
            status = GdipDrawImageRect(self, image, x, y, width, height)
            if status != Ok:
                raise GdipError(status)
            
        def draw_image_ex(self, image: 'Gdiplus.Image', source: RECT | RectF, destination: RECT | RectF, unit: int, attributes: TUnion['Gdiplus.ImageAttributes', None]):
            if isinstance(source, RECT):
                source = RectF(source.left, source.top, source.right - source.left, source.bottom - source.top)
            if isinstance(destination, RECT):
                destination = RectF(destination.left, destination.top, destination.right - destination.left, destination.bottom - destination.top)
            status = GdipDrawImageRectRect(self, image, destination.X, destination.Y, destination.Width, destination.Height, source.X, source.Y, source.Width, source.Height, unit, attributes, i_cast(NULL, DrawImageAbort), NULL)
            if status != Ok:
                raise GdipError(status)
            
        def draw_rectangle(self, rect: RECT | RectF, pen: 'Gdiplus.Pen'):
            if isinstance(rect, RECT):
                rect = RectF(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
            status = GdipDrawRectangle(self, pen, rect.X, rect.Y, rect.Width, rect.Height)
            if status != Ok:
                raise GdipError(status)
            
        def clear(self, color: Color.IColor):
            status = GdipGraphicsClear(self, int(color.argb()))
            if status != Ok:
                raise GdipError(status)
            
        def measure_string(self, string: str, font: 'Gdiplus.Font', layout: RECT | RectF | None = None, format: TUnion['Gdiplus.StringFormat', None] = None) -> tuple[RectF, int, int]:
            if layout is None:
                layout = RectF(0.0, 0.0, 999999.0, 999999.0)
            if isinstance(layout, RECT):
                layout = Gdiplus.Rect_to_RectF(layout)
            bounds = RectF()
            codepoints = INT()
            lines = INT()
            status = GdipMeasureString(self, string, len(string), font, layout.ref(), format, bounds.ref(), byref(codepoints), byref(lines))
            if status != Ok:
                raise GdipError(status)
            return bounds, codepoints.value, lines.value  
            
    class Font(Handle):
        """
        The GDI+ font.
        """
        
        @classmethod
        def create(cls, family: 'Gdiplus.FontFamily', em: int, style: int, unit: int) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from GDI+ font family, size in EM, font style and unit enumeration.
            """
            font = LPGPFONT()
            status = GdipCreateFont(family, em, style, unit, byref(font))
            if status != Ok:
                raise GdipError(status)
            return cls(font.value)
        
        @classmethod
        def from_dc(cls, dc: int | HANDLE) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from `win.abs.core.handle.DC` or `HDC`.
            """
            font = LPGPFONT()
            status = GdipCreateFontFromDC(dc, byref(font))
            if status != Ok:
                raise GdipError(status)
            return cls(font.value)
        
        @classmethod
        def from_font(cls, font: int | HANDLE, dc: int | HANDLE | None = None) -> 'Gdiplus.Font':
            """
            Create the GDI+ font from `win.abs.core.handle.Font` or `HFONT`.
            """
            if dc is None:
                dc = DC.create_compatible(None)
            if not isinstance(font, GDIObjectHandle):
                font = GDIObjectHandle.foreign_owner(font)
            lf = font.object
            font = LPGPFONT()
            status = GdipCreateFontFromLogfontW(dc, lf.ref(), byref(font))
            if status != Ok:
                raise GdipError(status)
            return cls(font.value)
        
        @classmethod
        def indirect(cls, logfont: LOGFONTW) -> 'Gdiplus.Font':
            """
            Create the GDI+ font indirectly from `LOGFONTW`.
            """
            font = LPGPFONT()
            with DC.create_compatible(None) as dc:
                status = GdipCreateFontFromLogfontW(dc, logfont.ref(), byref(font))
            if status != Ok:
                raise GdipError(status)
            return cls(font.value)
        
        def close(self):
            status = GdipDeleteFont(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def clone(self) -> 'Gdiplus.Font':
            """
            Clone the GDI+ font.
            """
            font = LPGPFONT()
            status = GdipCloneFont(self, byref(font))
            if status != Ok:
                raise GdipError(status)
            return self.__class__(font.value)
        
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
        
        def logfont(self, graphics: TUnion['Gdiplus.Graphics', None] = None) -> Logfont:
            """
            Get the `LOGFONTW` from GDI+ font.
            """
            if graphics is None:
                with DC.create_compatible(None) as dc:
                    with Gdiplus.Graphics.create(dc) as graphics:
                        return self.logfont(graphics)
            else:
                logfont = Logfont()
                status = GdipGetLogFontW(self, graphics, logfont.ref())
                if status != Ok:
                    raise GdipError(status)
                return logfont
            
        @property
        def family(self) -> 'Gdiplus.FontFamily':
            family = LPGPFONTFAMILY()
            status = GdipGetFamily(self, byref(family))
            if status != Ok:
                raise GdipError(status)
            return Gdiplus.FontFamily(family.value)
            
    class FontFamily(Handle):
        """
        The GDI+ font family.
        """
        
        @classmethod
        def serif(cls) -> 'Gdiplus.FontFamily':
            family = LPGPFONTFAMILY()
            status = GdipGetGenericFontFamilySerif(byref(family))
            if status != Ok:
                raise GdipError(status)
            return cls(family.value)
        
        @classmethod
        def sans_serif(cls) -> 'Gdiplus.FontFamily':
            family = LPGPFONTFAMILY()
            status = GdipGetGenericFontFamilySansSerif(byref(family))
            if status != Ok:
                raise GdipError(status)
            return cls(family.value)
        
        @classmethod
        def monospace(cls) -> 'Gdiplus.FontFamily':
            family = LPGPFONTFAMILY()
            status = GdipGetGenericFontFamilyMonospace(byref(family))
            if status != Ok:
                raise GdipError(status)
            return cls(family.value)
        
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
            collection = LPGPFONTCOLLECTION()
            status = GdipNewPrivateFontCollection(byref(collection))
            if status != Ok:
                raise GdipError(status)
            return cls(collection.value)
        
        def close(self):
            status = GdipDeletePrivateFontCollection(byref(self))
            if status != Ok:
                raise GdipError(status)
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
                    status = GdipPrivateAddFontFile(self, v)
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
            collection = LPGPFONTCOLLECTION()
            status = GdipNewInstalledFontCollection(byref(collection))
            if status != Ok:
                raise GdipError(status)
            return cls(collection.value)
        
    class Pen(Handle):
        """
        The GDI+ pen.
        """
        @classmethod
        def create(cls, value: Color.IColor, width: float = 1.0, unit: int = UnitPixel) -> 'Gdiplus.Pen':
            """
            Create the GDI+ pen from ARGB color, width and unit enumeration.
            """
            pen = LPGPPEN()
            status = GdipCreatePen1(int(value.argb()), width, unit, byref(pen))
            if status != Ok:
                raise GdipError(status)
            return cls(pen.value)
        
        @classmethod
        def from_brush(cls, brush: 'Gdiplus.Brush', width: float = 1.0, unit: int = UnitPixel) -> 'Gdiplus.Pen':
            """
            Create the GDI+ pen from GDI+ brush, width and unit enumeration.
            """
            pen = LPGPPEN()
            status = GdipCreatePen2(brush, width, unit, byref(pen))
            if status != Ok:
                raise GdipError(status)
            return cls(pen.value)
        
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
            if status != Ok:
                raise GdipError(status)
            
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
        def color(self, color: Color.IColor):
            status = GdipSetPenColor(self, int(color.argb()))
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
        
    class Brush(Handle):
        def clone(self) -> Self:
            brush = LPGPBRUSH()
            status = GdipCloneBrush(self, byref(brush))
            if status != Ok:
                raise GdipError(status)
            return self.__class__(brush.value)
        
        def close(self):
            status = GdipDeleteBrush(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        @property
        def type(self) -> int:
            brush_type = BrushType()
            status = GdipGetBrushType(self, byref(brush_type))
            if status != Ok:
                raise GdipError(status)
            return brush_type.value
        
    class SolidBrush(Brush):
        @classmethod
        def create(cls, color: Color.IColor) -> Self:
            brush = LPGPBRUSH()
            status = GdipCreateSolidFill(int(color.argb()), byref(brush))
            if status != Ok:
                raise GdipError(status)
            return cls(brush.value)
        
        @property
        def color(self) -> Color.ARGB:
            color = DWORD()
            status = GdipGetSolidFillColor(self, byref(color))
            if status != Ok:
                raise GdipError(status)
            return Color.ARGB(status.value)
        
        @color.setter
        def color(self, color: Color.IColor):
            status = GdipSetSolidFillColor(self, int(color.argb()))
            if status != Ok:
                raise GdipError(status)
        
    class HatchBrush(Brush):
        ...
        
    class Image(Handle):
        @classmethod
        def from_stream(cls, stream: io.IOBase | IStream) -> Self:
            if not isinstance(stream, IStream):
                stream = StreamOverIO(stream)
                TlAddRefGuard(stream)
            image = LPGPIMAGE()
            status = GdipLoadImageFromStream(stream.ref(), byref(image))
            if status != Ok:
                raise GdipError(status)
            return cls(image.value)
        
        @classmethod
        def from_file(cls, file: str) -> Self:
            image = LPGPIMAGE()
            status = GdipLoadImageFromFile(file, byref(image))
            if status != Ok:
                raise GdipError(status)
            return cls(image.value)
        
        def close(self):
            status = GdipDisposeImage(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        @property
        def width(self) -> int:
            width = UINT()
            status = GdipGetImageWidth(self, byref(width))
            if status != Ok:
                raise GdipError(status)
            return width.value
            
        @property
        def height(self) -> int:
            height = UINT()
            status = GdipGetImageHeight(self, byref(height))
            if status != Ok:
                raise GdipError(status)
            return height.value
        
    class Bitmap(Image):
        @classmethod
        def from_hbitmap(cls, hbm: int | HANDLE, palette: int | HANDLE = NULL) -> Self:
            bitmap = LPGPBITMAP()
            status = GdipCreateBitmapFromHBITMAP(hbm, palette, byref(bitmap))
            if status != Ok:
                raise GdipError(status)
            return cls(bitmap.value)

        @classmethod
        def from_hicon(cls, hicon: int | HANDLE) -> Self:
            bitmap = LPGPBITMAP()
            status = GdipCreateBitmapFromHICON(hicon, byref(bitmap))
            if status != Ok:
                raise GdipError(status)
            return cls(bitmap.value)
        
        def clone_area(self, rect: RECT | RectF, format: int) -> Self:
            if isinstance(rect, RECT):
                rect = RectF(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
            bitmap = LPGPBITMAP()
            status = GdipCloneBitmapArea(rect.X, rect.Y, rect.Width, rect.Height, format, self, byref(bitmap))
            if status != Ok:
                raise GdipError(status)
            return self.__class__(bitmap.value)
        
    class Icon(Handle):
        ...
        
    class Region(Handle):
        ...
        
    class StringFormat(Handle):
        @classmethod
        def create(cls, attributes: int, language: int) -> Self:
            format = LPGPSTRINGFORMAT()
            status = GdipCreateStringFormat(attributes, language, byref(format))
            if status != Ok:
                raise GdipError(status)
            return cls(format.value)
        
        @classmethod
        def generic(cls) -> Self:
            format = LPGPSTRINGFORMAT()
            status = GdipStringFormatGetGenericDefault(byref(format))
            if status != Ok:
                raise GdipError(status)
            return cls(format.value)
        
        @classmethod
        def typographic(cls) -> Self:
            format = LPGPSTRINGFORMAT()
            status = GdipStringFormatGetGenericTypographic(byref(format))
            if status != Ok:
                raise GdipError(status)
            return cls(format.value)
        
        def close(self):
            try:
                status = GdipDeleteStringFormat(self)
            except:
                status = Ok
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def clone(self) -> Self:
            format = LPGPSTRINGFORMAT()
            status = GdipCloneStringFormat(self, byref(format))
            if status != Ok:
                raise GdipError(status)
            return self.__class__(format.value)
        
        @property
        def flags(self) -> int:
            flags = INT()
            status = GdipGetStringFormatFlags(self, byref(flags))
            if status != Ok:
                raise GdipError(status)
            return flags.value
        
        @flags.setter
        def flags(self, flags: int):
            status = GdipSetStringFormatFlags(self, flags)
            if status != Ok:
                raise GdipError(status)
        
        @property
        def align(self) -> int:
            align = StringAlignment()
            status = GdipGetStringFormatAlign(self, byref(align))
            if status != Ok:
                raise GdipError(status)
            return align.value
        
        @align.setter
        def align(self, align: int):
            status = GdipSetStringFormatAlign(self, align)
            if status != Ok:
                raise GdipError(status)
        
        @property
        def line_align(self) -> int:
            align = StringAlignment()
            status = GdipGetStringFormatLineAlign(self, byref(align))
            if status != Ok:
                raise GdipError(status)
            return align.value
        
        @line_align.setter
        def line_align(self, line_align: int):
            status = GdipSetStringFormatLineAlign(self, line_align)
            if status != Ok:
                raise GdipError(status)
        
        @property
        def trimming(self) -> int:
            trimming = StringTrimming()
            status = GdipGetStringFormatTrimming(self, byref(trimming))
            if status != Ok:
                raise GdipError(status)
            return trimming.value
        
        @trimming.setter
        def trimming(self, trimming: int):
            status = GdipSetStringFormatTrimming(self, trimming)
            if status != Ok:
                raise GdipError(status)
        
        @property
        def hotkey_prefix(self) -> int:
            hotkey_prefix = INT()
            status = GdipGetStringFormatHotkeyPrefix(self, byref(hotkey_prefix))
            if status != Ok:
                raise GdipError(status)
            return hotkey_prefix.value
        
        @hotkey_prefix.setter
        def hotkey_prefix(self, hotkey_prefix: int):
            status = GdipSetStringFormatHotkeyPrefix(self, hotkey_prefix)
            if status != Ok:
                raise GdipError(status)
            
    class ImageAttributes(Handle):
        @classmethod
        def create(cls) -> Self:
            attributes = LPGPIMAGEATTRIBUTES()
            status = GdipCreateImageAttributes(byref(attributes))
            if status != Ok:
                raise GdipError(status)
            return cls(attributes.value)
        
        def close(self):
            status = GdipDisposeImageAttributes(self)
            if status != Ok:
                raise GdipError(status)
            self._closed = True
            
        def reset(self, adjust: int = ColorAdjustTypeAny):
            status = GdipResetImageAttributes(self, adjust)
            if status != Ok:
                raise GdipError(status)
            
        def set_color_matrix(self, grayscale: ColorMatrix | Iterable[float] | Iterable[Iterable[float]] | None, color: ColorMatrix | Iterable[float] | Iterable[Iterable[float]] | None, adjust: int = ColorAdjustTypeAny, flags: int = ColorMatrixFlagsDefault, enable_flag: bool = True):
            if grayscale is not None:
                if not isinstance(grayscale, ColorMatrix):
                    l = []
                    def recursive(u):
                        try:
                            for x in u:
                                recursive(x)
                        except:
                            l.append(u)
                    recursive(grayscale)
                    if len(l) != 5*5:
                        raise ValueError('Invalid grayscale matrix')
                    grayscale_mem = (FLOAT*(5*5))(*l)
                    grayscale = i_cast(grayscale_mem, PTR(ColorMatrix)).contents
            if color is not None:
                if not isinstance(color, ColorMatrix):
                    l = []
                    def recursive(u):
                        try:
                            for x in u:
                                recursive(x)
                        except:
                            l.append(u)
                    recursive(color)
                    if len(l) != 5*5:
                        raise ValueError('Invalid color matrix')
                    color_mem = (FLOAT*(5*5))(*l)
                    color = i_cast(color_mem, PTR(ColorMatrix)).contents
            status = GdipSetImageAttributesColorMatrix(self, adjust, enable_flag, color.ref() if color else NULL, grayscale.ref() if grayscale else NULL, flags)
            if status != Ok:
                raise GdipError(status)