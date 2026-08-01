# Win32 errors stringification and WinException
from win.defbase_errordef import *

# WinAPI header files
from win.handleapi import *
from win.synchapi import *
from win.winuser import *
from win.wingdi import *
from win.winnt import *

# Win DEFB Allocator API
from win.defbase_allocator import *

# WinAbs I/O API
from .io import *

# WinAbs utilities
from .absutils import *

# WinAbs controllable value
from .controllable import *

# WinAbs color API
from .color import *

# WinAbs geometric definitions
from .geom import *

class BitGroup:
    value: int
    
    def __init__(self, value: int):
        self.value = value
        
    def add(self, *bits: int):
        for bit in bits:
            self.value |= bit
        
    def remove(self, *bits: int):
        for bit in bits:
            self.value &= ~bit
        
    def has(self, *bits: int) -> bool:
        bit = 0
        for i in bits:
            bit |= i
        return (self.value & bit) != 0
    
    def __and__(self, bit: int) -> 'BitGroup':
        return BitGroup(self.value & bit)
    
    def __iand__(self, bit: int) -> 'BitGroup':
        self.value &= bit
        return self
    
    def __xor__(self, bit: int) -> 'BitGroup':
        return BitGroup(self.value ^ bit)
    
    def __ixor__(self, bit: int) -> 'BitGroup':
        self.value ^= bit
        return self
    
    def __or__(self, bit: int) -> 'BitGroup':
        return BitGroup(self.value | bit)
    
    def __ior__(self, bit: int) -> 'BitGroup':
        self.value |= bit
        return self
    
    def __int__(self) -> 'BitGroup':
        return self.value
    
    def __lshift__(self, bit: int) -> 'BitGroup':
        return BitGroup(self.value << bit)
    
    def __ilshift__(self, bit: int) -> 'BitGroup':
        self.value <<= bit
        return self
    
    def __rshift__(self, bit: int) -> 'BitGroup':
        return BitGroup(self.value >> bit)
    
    def __irshift__(self, bit: int) -> 'BitGroup':
        self.value >>= bit
        return self
    
    def test(self, mapping: dict[int, str]) -> list[str]:
        result = []
        for k, v in mapping.items():
            if self.value & v: result.append(k)
        return result
        
class GDIObjectHandle(Handle):
    def close(self):
        DeleteObject(self)
        self._closed = True
        
    @classmethod
    def stock(cls, type: int) -> Self:
        """
        Get the GDI stock object.
        """
        
        instance = cls.foreign_owner(GetStockObject(type))
        if not instance.value:
            raise WinException()
        return instance
    
    @property
    def type(self) -> int:
        return GetObjectType(self)
    
    @property
    def object(self):
        object_type = self.type
        if object_type == OBJ_BITMAP:
            bm = BITMAP()
            if not GetObject(self, sizeof(bm), bm.ref()):
                raise WinException()
            return bm
        elif object_type == OBJ_EXTPEN:
            elp = EXTLOGPEN()
            if not GetObject(self, sizeof(elp), elp.ref()):
                raise WinException()
            return elp
        elif object_type == OBJ_PEN:
            lp = LOGPEN()
            if not GetObject(self, sizeof(lp), lp.ref()):
                raise WinException()
            return lp
        elif object_type == OBJ_BRUSH:
            lb = LOGBRUSH()
            if not GetObject(self, sizeof(lb), lb.ref()):
                raise WinException()
            return lb
        elif object_type == OBJ_FONT:
            lf = LOGFONTW()
            if not GetObject(self, sizeof(lf), lf.ref()):
                raise WinException()
            return lf
        
# duplication shortcut for not to write GDIObjectHandle.stock for unknown stock object types
class StockObject(GDIObjectHandle):
    """
    Stock object class.
    """
    
    def __init__(self, type: int):
        hObject = GetStockObject(type)
        if not hObject:
            raise WinException()
        super().__init__(hObject)
    
    def close(self):
        self._closed = True

class DC(Handle):
    """
    Class, representing GDI Device Context (DC).
    """
    
    class Select:
        object: int | HANDLE
        dc: 'DC'
        
        def __init__(self, dc: 'DC', object: int | HANDLE):
            self.object = dc.select(object)
            self.dc = dc
            
        def __enter__(self):
            return self.object
        
        def __exit__(self, *_):
            self.dc.select(self.object)
    
    class PathPoint(POINT):
        type: int
        
        def __init__(self, x: int = 0, y: int = 0, type: int = 0):
            super().__init__()
            self.type = type
    
    class Path:
        dc: 'DC'
        
        def __init__(self, dc: 'DC'):
            self.dc = dc
            
        def stroke(self):
            """
            Stroke the path.
            """
            
            if not StrokePath(self.dc):
                raise WinException()
        
        def stroke_and_fill(self):
            """
            Stroke and fill the path.
            """
            
            if not StrokeAndFillPath(self.dc):
                raise WinException()
            
        def fill(self):
            """
            Fill the path.
            """
            
            if not FillPath(self.dc):
                raise WinException()
            
        def begin(self):
            """
            Begin the path.
            """
            
            if not BeginPath(self.dc):
                raise WinException()
            
        def end(self):
            """
            End the path.
            """
            
            if not EndPath(self.dc):
                raise WinException()
            
        def __enter__(self):
            self.begin()
            
        def __exit__(self, exc_type, exc, tb):
            self.end()
            
        def abort(self):
            """
            Abort the path.
            """
            
            if not AbortPath(self.dc):
                raise WinException()
            
        def flatten(self):
            """
            Flatten the path.
            """
            
            if not FlattenPath(self.dc):
                raise WinException()
            
        def get(self) -> tuple['DC.PathPoint']:
            """
            Get the path points into tuple.
            """
            
            paths: IArray[DC.PathPoint]
            types: IArray[BYTE]
            nPaths: int
            
            nPaths = GetPath(self.dc, NULL, NULL, 0)
            paths = (DC.PathPoint * nPaths)()
            types = (BYTE * nPaths)()
            nPaths = GetPath(self.dc, paths, types)
            
            paths = list(paths)
            for i in range(nPaths):
                paths[i].type = types[i]
                
            return tuple(paths)
    
    class Pixels:
        class PixelsLine:
            dc: 'DC'
            x: int
            
            def __init__(self, dc: 'DC'):
                self.dc = dc
                self.x = 0
            
            def __getitem__(self, y: int) -> 'Color.BGR':
                return Color.BGR(GetPixel(self.dc, self.x, y))
            
            def __setitem__(self, y: int, color: TUnion[int, 'Color.IColor']):
                self.dc.set_pixel(self.x, y, color)
        
        dc: 'DC'
        
        def __init__(self, dc: 'DC'):
            self.line = DC.Pixels.PixelsLine(dc)
            self.dc = dc
            
        def __getitem__(self, x: int) -> 'DC.Pixels.PixelsLine':
            self.line.x = x
            return self.line
    
    class Realize:
        dc: 'DC'
        
        def __init__(self, dc: 'DC'):
            self.dc = dc
            
        def begin(self, palette: int | HANDLE=NULL):
            """
            Realize the palette.
            """
            
            with self.dc.select_ex(palette):
                RealizePalette(self.dc)
                
        def end(self, palette: int | HANDLE):
            """
            Unrealize the palette.
            """
            
            UnrealizeObject(palette)
            
        def __enter__(self):
            self.begin()
            
        def __exit__(self, exc_type, exc, tb):
            self.end()
    
    class ClipRegion:
        class Select:
            clip_region: 'DC.ClipRegion'
            region: int | HANDLE
            
            def __init__(self, clip_region: 'DC.ClipRegion', region: int | HANDLE):
                self.clip_region = clip_region
                self.region = region
                
            def __enter__(self):
                return self.clip_region.select(self.region)
            
            def __exit__(self, exc_type, exc, tb):
                self.clip_region.select(NULL)
                
        dc: 'DC'
        
        def __init__(self, dc: 'DC'):
            self.dc = dc
            
        def select(self, region: int | HANDLE) -> int:
            """
            Select the clip region.
            """
            
            complexity = SelectClipRgn(self.dc, region)
            if complexity == ERROR: raise WinException()
            return complexity
        
        def select_ex(self, region: int | HANDLE) -> 'DC.ClipRegion.Select':
            """
            Select the clip region, extended version with RAII.
            """
            
            return DC.ClipRegion.Select(self, region)
        
        def offset(self, x: int, y: int) -> int:
            """
            Offset the clip region.
            """
            
            complexity = OffsetClipRgn(self.dc, x, y)
            if complexity == ERROR: raise WinException()
            return complexity
        
        def exclude(self, x: int, y: int, width: int, height: int) -> int:
            """
            Exclude the rectangle from clip region.
            """
            complexity = ExcludeClipRect(self.dc, x, y, x+width, y+height)
            if complexity == ERROR: raise WinException()
            return complexity
    
    pixels: 'DC.Pixels'
    _created: bool
    path: 'DC.Path'
    
    def __init__(self, dc: int = NULL, hwnd: int = NULL):
        super().__init__(dc)
        self._created = False
        self._hwnd = hwnd
        self.path = DC.Path(self)
        self.pixels = DC.Pixels(self)
        self.realize = DC.Realize(self)
        self.clip_region = DC.ClipRegion(self)
    
    def close(self):
        if self._created:
            DeleteDC(self)
        else:
            ReleaseDC(self._hwnd, self)
        self._closed = True
            
    def create_compatible(self) -> 'DC':
        """
        Create compatible GDI device context from DC.
        """
        
        hDC = CreateCompatibleDC(self)
        if not hDC:
            raise WinException()
        dc = DC(hDC)
        dc._created = True
        return dc
    
    def create_compatible_bitmap(self, width: int, height: int) -> 'Bitmap':
        """
        Create compatible bitmap by provided width and height.
        """
        
        bitmap = Bitmap()
        bitmap.value = CreateCompatibleBitmap(self, width, height)
        if not bitmap.value:
            raise WinException()
        return bitmap
        
    @classmethod
    def get(cls, hwnd: int | HWND = NULL, region: int | HANDLE = NULL, flags: int = 0) -> 'DC':
        """
        Get the device context for HWND (for client area).
        """
        
        if region is None:
            hDC = GetDC(hwnd)
        else:
            hDC = GetDCEx(hwnd, region, flags)
        if not hDC:
            raise WinException()
        return DC(hDC)
        
    @classmethod
    def window(self, window: int | HWND) -> 'DC':
        """
        Get the device context for HWND (for window area).
        """
        hDC = GetWindowDC(window)
        if not hDC:
            raise WinException()
        return DC(hDC)
        
    @property
    def clip_box(self) -> Rect:
        rc = Rect()
        if not GetClipBox(self, byref(rc)):
            raise WinException()
        return rc
        
    def select(self, hGdiObject: int | HANDLE) -> int:
        """
        Select the GDI object on DC.
        """
        
        return GDIObjectHandle.foreign_owner(SelectObject(self, hGdiObject))
    
    def select_ex(self, hGdiObject: int | HANDLE) -> 'DC.Select':
        """
        Select the GDI object on DC, extended version with RAII.
        """
        
        return DC.Select(self, hGdiObject)
    
    def text_out(self, x: int, y: int, text: str):
        """
        Output the text to screen.
        """
        
        buf = create_unicode_buffer(text)
        if not TextOutW(self, x, y, buf, len(text)):
            raise WinException()
        
    def set_pixel(self, x: int, y: int, color: TUnion[int, 'Color.IColor']) -> 'Color.BGR':
        """
        Set the pixel by given coordinates to given color.
        """
        
        crColor = SetPixel(self, x, y, int(color))
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.BGR(crColor)
    
    @property
    def text_color(self) -> 'Color.BGR':
        crColor = GetTextColor(self)
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.BGR(crColor)
    
    @text_color.setter
    def text_color(self, text_color: TUnion[int, 'Color.IColor']):
        self.set_text_color(text_color)
    
    def set_text_color(self, color: TUnion[int, 'Color.IColor']) -> int:
        """
        Set the text color.
        """
        
        crColor = SetTextColor(self, int(color))
        if crColor == CLR_INVALID:
            raise WinException()
        return crColor
    
    @property
    def bk_color(self) -> 'Color.BGR':
        crColor = GetBkColor(self)
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.BGR(crColor)
    
    @bk_color.setter
    def bk_color(self, bk_color: TUnion[int, 'Color.IColor']):
        self.set_bk_color(bk_color)
    
    def set_bk_color(self, color: TUnion[int, 'Color.IColor']) -> 'Color.BGR':
        """
        Set the background color.
        """
        
        crColor = SetBkColor(self, int(color))
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.BGR(crColor)
    
    @property
    def bk_mode(self) -> int:
        mode = GetBkMode(self)
        if mode == 0:
            raise WinException()
        return mode
    
    @bk_mode.setter
    def bk_mode(self, bk_mode: int):
        self.set_bk_mode(bk_mode)
    
    def set_bk_mode(self, mode: int) -> int:
        """
        Set the background mode.
        """
        
        dwPrevMode = SetBkMode(self, mode)
        if dwPrevMode == 0:
            raise WinException()
        return dwPrevMode
    
    @property
    def text_align(self) -> int:
        dwAlign = GetTextAlign(self)
        if dwAlign == GDI_ERROR:
            raise WinException()
        return dwAlign
    
    @text_align.setter
    def text_align(self, text_align: int):
        self.set_text_align(text_align)
    
    def set_text_align(self, text_align: int) -> int:
        """
        Set the text align.
        """
        
        dwPrevAlign = SetTextAlign(self, text_align)
        if dwPrevAlign == GDI_ERROR:
            raise WinException()
        return dwPrevAlign
    
    def bit_blt(self, dstX: int, dstY: int, srcX: int, srcY: int, 
                width: int, height: int, srcHdc: int | HDC, rop: int):
        """
        GDI Device context BitBlt.
        """
        
        if not BitBlt(self, dstX, dstY, width, height, srcHdc, srcX, srcY, rop):
            raise WinException()
    
    def stretch_blt(self, dstX: int, dstY: int, srcX: int, srcY: int, 
                dstWidth: int, dstHeight: int, srcWidth: int, srcHeight: int, 
                srcHdc: int | HDC, rop: int):
        """
        GDI Device context StretchBlt.
        """
        
        if not StretchBlt(self, dstX, dstY, dstWidth, dstHeight,
                      srcHdc, srcX, srcY, srcWidth, srcHeight, rop):
            raise WinException()
    
    def pat_blt(self, x: int, y: int, width: int, height: int, rop: int):
        """
        GDI Device context PatBlt.
        """
        
        if not PatBlt(self, x, y, width, height, rop):
            raise WinException()
        
    def transparent_blt(self, srcX: int, srcY: int, dstX: int, dstY: int, 
                        srcHdc: int | HANDLE, srcWidth: int, srcHeight: int,
                        dstWidth: int, dstHeight: int, transparent: int):
        """
        GDI Device context TransparentBlt.
        """
        
        if not TransparentBlt(self, srcX, srcY, dstWidth, dstHeight, 
                              srcHdc, dstX, dstY, srcWidth, srcHeight, transparent):
            raise WinException()
    
    def ellipse(self, rcEllps: RECT):
        """
        Draw an ellipse.
        """
        
        if not Ellipse(self, rcEllps.left, rcEllps.top, rcEllps.right, rcEllps.bottom):
            raise WinException()
        
    def fill(self, rect: RECT, hbr: int | HANDLE):
        """
        Fill the given rect with brush.
        """
        
        if not FillRect(self, byref(rect), hbr):
            raise WinException()
        
    def invert_rect(self, rect: RECT):
        """
        Invert the given rect
        """
        
        if not InvertRect(self, byref(rect)):
            raise WinException()
        
    def get_text_extent_point(self, text: str) -> SIZE:
        """
        Get text extent point by text.
        """
        
        sizeText = SIZE()
        buf = create_unicode_buffer(text)
        GetTextExtentPointW(self, buf, len(text), byref(sizeText))
        return sizeText
    
    def draw_icon(self, x: int, y: int, width: int, height: int,
                  icon: int | HANDLE, step: int = 0, 
                  flicker_free_draw: int | HANDLE = NULL,
                  flags: int = DI_NORMAL):
        """
        Draw the icon on device context.
        """
        
        if not DrawIconEx(self, x, y, icon, width, height, step, flicker_free_draw, flags):
            raise WinException()
        
    def draw_state(self, x: int, y: int, flags: int, fore_brush: int | HANDLE = NULL, callback: Callable = None,
                   width: int = 0, height: int = 0, lData: int = NULL, wData: int = NULL):
        """
        GDI device context DrawState.
        """
        
        if callback is not None:
            callback = DRAWSTATEPROC(callback)
        if not DrawStateW(self, fore_brush, i_cast(callback, DRAWSTATEPROC),
                          PtrUtil.get_address(lData), 
                          PtrUtil.get_address(wData),
                          x, y, width, height, flags):
            raise WinException()
        
    def move(self, x: int, y: int) -> POINT:
        """
        Move the pointer to (x, y) and return previous position.
        """
        
        pt = POINT()
        if not MoveToEx(self, x, y, byref(pt)):
            raise WinException()
        return pt
    
    def line(self, x: int, y: int):
        """
        Line to (x, y).
        """
        
        if not LineTo(self, x, y):
            raise WinException()
    
    @property
    def rop2(self) -> int:
        rop2 = GetROP2(self)
        if not rop2:
            raise WinException()
        return rop2
    
    @rop2.setter
    def rop2(self, rop2: int):
        self.set_rop2(rop2)
        
    def set_rop2(self, rop2: int) -> int:
        """
        Set the ROP2.
        """
        
        iPrevROP2 = SetROP2(self, rop2)
        if not iPrevROP2:
            raise WinException()
        return iPrevROP2
        
    @property
    def poly_fill_mode(self) -> int:
        iMode = GetPolyFillMode(self)
        if not iMode:
            raise WinException()
        return iMode
    
    @poly_fill_mode.setter
    def poly_fill_mode(self, poly_fill_mode: int):
        self.set_poly_fill_mode(poly_fill_mode)
        
    def set_poly_fill_mode(self, poly_fill_mode: int) -> int:
        """
        Set the polygon fill mode.
        """
        
        dwPrevPolyFillMode = SetPolyFillMode(self, poly_fill_mode)
        if not dwPrevPolyFillMode:
            raise WinException()
        return dwPrevPolyFillMode
        
    def gradient(self, vertices: Iterable[TRIVERTEX],
                 meshes: Iterable[GRADIENT_TRIANGLE | GRADIENT_RECT],
                 mode: int):
        """
        Draw the gradient triangle/rectangle.
        """
        
        nVertex = len(vertices)
        pVertices = (TRIVERTEX * nVertex)(*vertices)
        nMesh = len(meshes)
        pMeshes = (type(meshes[0]) * nMesh)(*meshes)
        if not GradientFill(self, pVertices, nVertex, pMeshes, nMesh, mode):
            raise WinException()
        
    def polygon(self, vertices: 'GraphicUtils.PointArray'):
        """
        Draw the polygon.
        """
        
        pVertices = GraphicUtils.point_array(vertices)
        if not Polygon(self, pVertices, len(vertices)):
            raise WinException()
        
    def frame(self, rc: RECT, brush: int | HANDLE):
        """
        Frame the given rect.
        """
        
        if not FrameRect(self, byref(rc), brush):
            raise WinException()
        
    def frame_region(self, region: int | HANDLE, brush: int | HANDLE,
                     width: int, height: int):
        """
        Frame the given region.
        """
        
        if not FrameRgn(self, region, brush, width, height):
            raise WinException()
        
    @property
    def bounds(self) -> Rect:
        bounds = Rect()
        if not GetBoundsRect(self, byref(bounds), 0):
            raise WinException()
        return bounds
    
    @bounds.setter
    def bounds(self, bounds: RECT):
        if not SetBoundsRect(self, byref(bounds), 0):
            raise WinException()
        
    def select_palette(self, palette: int | HANDLE, force_background: bool = False):
        """
        Select the given palette.
        """
        
        hPalettePrev = SelectPalette(self, palette, force_background)
        return Palette.foreign_owner(hPalettePrev)
    
    def draw_3d_rect(self, x: int, y: int, width: int, height: int,
                     top_left: TUnion[int, 'Color.IColor'],
                     bottom_right: TUnion[int, 'Color.IColor']):
        """
        Draw 3D rect on device context. Direct CDC::Draw3dRect reimplementation.
        """
        
        top_left, bottom_right = int(top_left), int(bottom_right)
        
        with Brush.create(top_left) as top_left_brush, Brush.create(bottom_right) as bottom_right_brush:
            self.fill(Rect.create(x, y, width - 1, 1), top_left_brush)
            self.fill(Rect.create(x, y, 1, height - 1), top_left_brush)
            
            self.fill(Rect.create(x + width, y, -1, height), bottom_right_brush)
            self.fill(Rect.create(x, y + height, width, -1), bottom_right_brush)
    
    @property
    def viewport_origin(self) -> tuple[int, int]:
        pt = POINT()
        if not GetViewportOrgEx(self, byref(pt)):
            raise WinException()
        return (pt.x, pt.y)
    
    @viewport_origin.setter
    def viewport_origin(self, viewport_origin: 'GraphicUtils.Point'):
        x, y = GraphicUtils.point_tuple(viewport_origin)
        if not SetViewportOrgEx(self, x, y, NULL):
            raise WinException()
        
    @property
    def viewport_extents(self) -> tuple[int, int]:
        extents = SIZE()
        if not GetViewportExtEx(self, byref(extents)):
            raise WinException()
        return (extents.cx, extents.cy)
    
    @viewport_extents.setter
    def viewport_extents(self, viewport_extents: 'GraphicUtils.Size'):
        x, y = GraphicUtils.size_tuple(viewport_extents)
        if not SetViewportExtEx(self, x, y, NULL):
            raise WinException()
    
    @property
    def window_origin(self) -> tuple[int, int]:
        pt = POINT()
        if not GetWindowOrgEx(self, byref(pt)):
            raise WinException()
        return (pt.x, pt.y)
    
    @viewport_origin.setter
    def window_origin(self, window_origin: 'GraphicUtils.Point'):
        x, y = GraphicUtils.point_tuple(window_origin)
        if not SetWindowOrgEx(self, x, y, NULL):
            raise WinException()
        
    @property
    def window_extents(self) -> tuple[int, int]:
        extents = SIZE()
        if not GetWindowExtEx(self, byref(extents)):
            raise WinException()
        return (extents.cx, extents.cy)
    
    @window_extents.setter
    def window_extents(self, window_extents: 'GraphicUtils.Size'):
        x, y = GraphicUtils.size_tuple(window_extents)
        if not SetWindowExtEx(self, x, y, NULL):
            raise WinException()
        
    def offset_viewport_origin(self, *args) -> tuple[int, int]:
        """
        Offset the viewport origin.
        """
        
        if len(args) == 1:
            x, y = GraphicUtils.point_tuple(args[0])
        else:
            x, y = GraphicUtils.point_tuple(args)
        pt = POINT()
        if not OffsetViewportOrgEx(self, x, y, byref(pt)):
            raise WinException()
        return (pt.x, pt.y)
        
    def offset_window_origin(self, *args) -> tuple[int, int]:
        """
        Offset the window origin.
        """
        
        if len(args) == 1:
            x, y = GraphicUtils.point_tuple(args[0])
        else:
            x, y = GraphicUtils.point_tuple(args)
        pt = POINT()
        if not OffsetWindowOrgEx(self, x, y, byref(pt)):
            raise WinException()
        return (pt.x, pt.y)
    
    def stretch_di_bits(
        self, x0: int, y0: int, x1: int, y1: int, 
        w0: int, h0: int, w1: int, h1: int,
        bits: bytes | int, bmi: BITMAPINFO, 
        rop: int = SRCCOPY, usage: int = DIB_RGB_COLORS):
        """
        Stretch DIB bits from buffer to window.
        """
        if not StretchDIBits(self, x0, y0, w0, h0, x1, y1, w1, h1, bits, bmi.ref(), usage, rop):
            raise WinException()
        
    def get_di_bits(self, bm: int | HANDLE, bits: WT_ADDRLIKE, info: BITMAPINFO, 
                    start: int = 0, lines: int = 0, usage: int = DIB_RGB_COLORS):
        """
        Get DIB bits from bitmap.
        """
        if not GetDIBits(self, bm, start, lines, bits, info.ref(), usage):
            raise WinException()
        
    def draw_edge(self, rect: RECT, edge: int, flags: int):
        """
        Draw 1 edge or 1+ edges of rectangle.
        """
        if not DrawEdge(self, rect.ref(), edge, flags):
            raise WinException()
        
    def draw_focus_rect(self, rect: RECT):
        """
        Draw rectangle in focused style.
        """
        if not DrawFocusRect(self, rect.ref()):
            raise WinException()
        
    def draw_frame_control(self, rect: RECT, type: int, state: int):
        """
        Draw frame control of the specified type and style.
        """
        if not DrawFrameControl(self, rect.ref(), type, state):
            raise WinException()
        
    def draw_border_3d(self, rect: RECT, style: int, sides: int):
        """
        Draw the 3D border.
        """
        self.draw_edge(rect, style & 0xf, sides | (style & 0xf))
        
    def capabilities(self, index: int) -> int:
        """
        Get the device context capabilities.
        """
        return GetDeviceCaps(self, index)

class Monitor(HMONITOR):
    @classmethod
    def from_window(cls, window: int | HWND, flags: int = MONITOR_DEFAULTTONULL) -> TUnion['Monitor', None]:
        hm = MonitorFromWindow(window, flags)
        if not hm: return None
        return Monitor(hm)
    
    @classmethod
    def from_rect(cls, rc: RECT, flags: int = MONITOR_DEFAULTTONULL) -> TUnion['Monitor', None]:
        hm = MonitorFromRect(rc.ref(), flags)
        if not hm: return None
        return Monitor(hm)
    
    @classmethod
    def from_point(cls, x: int, y: int, flags: int = MONITOR_DEFAULTTONULL) -> TUnion['Monitor', None]:
        hm = MonitorFromPoint(Point(x, y), flags)
        if not hm: return None
        return Monitor(hm)
    
    def information(self) -> MONITORINFOEXW:
        miex = MONITORINFOEXW()
        miex.cbSize = miex.size()
        if not GetMonitorInfoW(self, miex.ref()):
            raise WinException()
        return miex
    
    @property
    def width(self) -> int:
        return i_cast_structure(self.information().rcMonitor, Rect).width
    
    @property
    def height(self) -> int:
        return i_cast_structure(self.information().rcMonitor, Rect).height

class DPIUtil:
    system_dpi = DC.get().capabilities(LOGPIXELSX)
    scale_factor = system_dpi / 96.0
    
    @staticmethod
    def adjust(lx: int, ly: int) -> tuple[int, int]:
        return DPIUtil.adjust_single(lx), DPIUtil.adjust_single(ly)
    
    @staticmethod
    def adjust_single(li: int) -> int:
        return round(DPIUtil.scale_factor * li)

class BitmapInfo(BITMAPINFO):
    def __init__(self, width: int, height: int, bpp: int, **kwargs):
        super().__init__(**kwargs)
        self.bmiHeader.biSize = BITMAPINFOHEADER.size()
        if bpp == -1: return
        self.bmiHeader.biWidth = width
        self.bmiHeader.biHeight = -height
        self.bmiHeader.biPlanes = 1
        self.bmiHeader.biBitCount = bpp
        
    @property
    def width(self) -> int:
        return self.bmiHeader.biWidth
    
    @width.setter
    def width(self, width: int):
        self.bmiHeader.biWidth = width
        
    @property
    def height(self) -> int:
        return self.bmiHeader.biHeight
    
    @height.setter
    def height(self, height: int):
        self.bmiHeader.biHeight = height
        
    @property
    def image_size(self) -> int:
        return self.bmiHeader.biSizeImage
    
    @image_size.setter
    def image_size(self, image_size: int):
        self.bmiHeader.biSizeImage = image_size
        
    @property
    def bpp(self) -> int:
        return self.bmiHeader.biBitCount
    
    @bpp.setter
    def bpp(self, bpp: int):
        self.bmiHeader.biBitCount = bpp
        
class MathUtil:
    """
    Math utilities.
    """
    
    @staticmethod
    def clamp(value: int | float, min_value: int | float, max_value: int | float) -> int | float:
        """
        Clamp the value into [min, max]
        """
        
        return max(min_value, min(max_value, value))
        
class StringUtil:
    """
    String and stringify utilities.
    """
    
    @staticmethod
    def to_string(obj: Any) -> str:
        if isinstance(obj, RECT):
            return f'<RECT {{{{{obj.left}, {obj.top}}}, {{{obj.right}, {obj.bottom}}}}}>'
        elif isinstance(obj, POINT):
            return f'<POINT {{{obj.x}, {obj.y}}}>'
        else:
            return repr(obj)
    
class Pen(GDIObjectHandle):
    """
    Class, representing GDI Pen object.
    """
    
    @classmethod
    def create(cls, style: int, width: int, color: int | Color.IColor) -> 'Pen':
        """
        Create the pen.
        """
        
        pen = cls()
        pen.value = CreatePen(style, width, int(color))
        if not pen.value:
            raise WinException()
        return pen

class Brush(GDIObjectHandle):
    """
    Class, representing GDI Brush object.
    """
    
    @classmethod
    def create(cls, color: int | Color.IColor, hatch: int | Color.IColor = None) -> 'Brush':
        """
        Create the brush.
        """
        
        brush = Brush()
        if hatch is None:
            brush.value = CreateSolidBrush(int(color))
        else:
            brush.value = CreateHatchBrush(int(color), int(hatch))
        if not brush.value:
            raise WinException()
        return brush
        
class PatternBrush(GDIObjectHandle):
    """
    Class, representing GDI Pattern brush object.
    """
    @classmethod
    def create(cls, hbm: int | HANDLE) -> 'PatternBrush':
        """
        Create the pattern brush.
        """
        brush = cls(CreatePatternBrush(hbm))
        if not brush.value:
            raise WinException()
        return brush
    
class Font(GDIObjectHandle):
    """
    Class, representing GDI Font object.
    """
    @classmethod
    def create(cls, name: str, height: int, width: int = 0, 
               escapement: int = 0, orientation: int = 0,
               weight: int = FW_DONTCARE, italic: bool = False,
               underline: bool = False, strike_out: bool = False,
               charset: int = DEFAULT_CHARSET, 
               out_precision: int = OUT_DEFAULT_PRECIS,
               clip_precision: int = CLIP_DEFAULT_PRECIS,
               quality: int = DEFAULT_QUALITY, 
               pitch_and_family: int = DEFAULT_PITCH | FF_DONTCARE) -> 'Font':
        font = cls(
            CreateFontW(
                height, width, escapement,
                orientation, weight, italic,
                underline, strike_out, charset,
                out_precision, clip_precision,
                quality, pitch_and_family, name)
            )
        if not font.value:
            print('Sheize')
            raise WinException()
        return font
        
class Region(GDIObjectHandle):
    """
    Class, representing GDI Region object.
    """
    
    def offset(self, dx: int, dy: int):
        """
        Offset the region to given delta X and delta Y.
        """
        
        if not OffsetRgn(self, dx, dy):
            raise WinException()
    
    def __contains__(self, point: GraphicUtils.Point) -> bool:
        x, y = GraphicUtils.point_tuple(point)
        return PtInRegion(self, x, y)
    
    @overload
    @classmethod
    def rect(cls, rc: RECT) -> 'Region':
        """
        Create the rectangle region.
        """
    
    @overload
    @classmethod
    def rect(cls, x1: int, y1: int, x2: int, y2: int, *args) -> 'Region': 
        """
        Create the rectangle region.
        """
    
    @classmethod
    def rect(cls, rc, *args) -> 'Region':
        rgn = cls()
        
        if isinstance(rc, int):
            rgn.value = CreateRectRgn(rc, *args)
        else:
            rgn.value = CreateRectRgnIndirect(byref(rc))
        
        if not rgn.value:
            raise WinException()
        
        return rgn
    
    @overload
    @classmethod
    def elliptic(cls, rc: RECT) -> 'Region': 
        """
        Create the elliptic region.
        """
    
    @overload
    @classmethod
    def elliptic(cls, x1: int, y1: int, x2: int, y2: int, *args) -> 'Region':
        """
        Create the elliptic region.
        """
    
    @classmethod
    def elliptic(cls, rc, *args) -> 'Region':
        rgn = cls()
        
        if isinstance(rc, int):
            rgn.value = CreateEllipticRgn(rc, *args)
        else:
            rgn.value = CreateEllipticRgnIndirect(byref(rc))
        
        if not rgn.value:
            raise WinException()
        
        return rgn
    
    @classmethod
    def polygon(cls, points: GraphicUtils.PointArray, mode: int) -> 'Region':
        """
        Create the polygonal region.
        """
        
        rgn = cls(CreatePolygonRgn(GraphicUtils.point_array(points), len(points), mode))
        
        if not rgn.value:
            raise WinException()
        
        return rgn
    
    @overload
    @classmethod
    def round_rect(cls, rc: RECT, w: int, h: int) -> 'Region': 
        """
        Create the round rectangle region.
        """
    
    @overload
    @classmethod
    def round_rect(cls, x1: int, y1: int, x2: int, y2: int, w: int, h: int, *args) -> 'Region': 
        """
        Create the round rectangle region.
        """
    
    @classmethod
    def round_rect(cls, var, *args) -> 'Region':
        rgn = cls()
        
        if isinstance(var, int):
            rgn.value = CreateRoundRectRgn(var, *args)
        else:
            rc: RECT = var
            rgn.value = CreateRoundRectRgn(rc.left, rc.top, rc.right, rc.bottom, *args)
        
        if not rgn.value:
            raise WinException()
        
        return rgn
    
    @classmethod
    def poly_polygon(cls, points: GraphicUtils.PointArray, point_counts: Iterable[int], mode: int):
        """
        Create the poly-polygonal region.
        """
        
        pPoints = (POINT * len(points))(*points)
        cPointCount = len(point_counts)
        pcPoints = (INT * cPointCount)(*point_counts)
        rgn = cls(CreatePolyPolygonRgn(pPoints), pcPoints, cPointCount, mode)
        
        if not rgn.value:
            raise WinException()
        
        return rgn

class IconInfo(ICONINFO):
    """
    Class, representing icon info.
    """
    
    _foreign_owner: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._foreign_owner = False
    
    @classmethod
    def foreign_owner(cls, ii: ICONINFO = NULL) -> 'IconInfo':
        if ii is not NULL:
            info = i_cast_structure(ii, IconInfo)
        else:
            info = IconInfo()
        info._foreign_owner = True
    
    @property
    def is_icon(self) -> bool:
        return self.fIcon == TRUE
    
    @is_icon.setter
    def is_icon(self, is_icon: bool):
        self.fIcon = is_icon
        
    @property
    def hotspot_x(self) -> int:
        return self.xHotspot
    
    @hotspot_x.setter
    def hotspot_x(self, hotspot_x: int):
        self.xHotspot = hotspot_x
        
    @property
    def hotspot_y(self) -> int:
        return self.yHotspot
    
    @hotspot_y.setter
    def hotspot_y(self, hotspot_y: int):
        self.yHotspot = hotspot_y
        
    @property
    def mask(self) -> 'Bitmap':
        return Bitmap.foreign_owner(self.hbmMask)
    
    @mask.setter
    def mask(self, mask: int | HANDLE):
        self.hbmMask = mask
        
    @property
    def color(self) -> 'Bitmap':
        return Bitmap.foreign_owner(self.hbmColor)
    
    @color.setter
    def color(self, color: int | HANDLE):
        self.hbmColor = color
        
    def __del__(self):
        if not self._foreign_owner:
            self.color.close()
            self.mask.close()

class ICONDIRENTRY(CStructure):
    _fields_ = [
        ('nWidth', BYTE),
        ('nHeight', BYTE),
        ('nNumColorsInPalette', BYTE),
        ('nReserved', BYTE),
        ('nNumColorPlanes', WORD),
        ('nBitsPerPixel', WORD),
        ('nDataLength', ULONG),
        ('nOffset', ULONG)
    ]
    nWidth: int
    nHeight: int
    nNumColorsInPalette: int
    nReserved: int
    nNumColorPlanes: int
    nBitsPerPixel: int
    nDataLength: int
    nOffset: int

class Icon(Handle):
    """
    Class, representing Win32 ICO icon.
    """
    
    def close(self):
        DestroyIcon(self)
        self._closed = True
        
    @property
    def icon_info(self) -> IconInfo:
        ii = IconInfo()
        if not GetIconInfo(self, ii.ref()):
            raise WinException()
        return ii
    
    @property
    def icon_info_ex(self) -> ICONINFOEXW:
        iiex = ICONINFOEXW()
        if not GetIconInfoExW(self, iiex.ref()):
            raise WinException()
        return iiex
    
    @classmethod
    def from_bitmap(self, bitmap: int | HANDLE, mask: int | Color.IColor | None = None) -> 'Icon':
        if not isinstance(bitmap, Bitmap):
            bitmap = Bitmap.foreign_owner(bitmap)
        
        bm = bitmap.object
        mask_bitmap = Bitmap.create(bm.bmWidth, bm.bmHeight, bit_count=1)
        
        with DC.create_compatible(NULL) as bitmapDC, DC.create_compatible(NULL) as maskDC:
            with bitmapDC.select_ex(bitmap), maskDC.select_ex(mask_bitmap):
                if mask is not None:
                    bitmapDC.bk_color = mask
                    maskDC.bit_blt(0, 0, 0, 0, bm.bmWidth, bm.bmHeight, bitmapDC, SRCCOPY)
                else:
                    maskDC.bit_blt(0, 0, 0, 0, bm.bmWidth, bm.bmHeight, bitmapDC, SRCCOPY)
        
        info = IconInfo()
        info.is_icon = True
        info.color = bitmap
        info.mask = mask_bitmap
        
        icon = Icon()
        icon.value = CreateIconIndirect(info.ref())
        
        if not icon.value:
            raise WinException()
        
        return icon
    
    @classmethod
    def from_icon(cls, path: str, width: int = 0, height: int = 0) -> 'Icon':
        """
        Create an icon from ICO file.
        """
        
        icon = cls()
        icon.value = LoadImageW(
            NULL, path, IMAGE_ICON, width, height, 
            LR_LOADFROMFILE | LR_DEFAULTSIZE)
        
        if not icon.value:
            raise WinException()
        
        return icon
    
    @classmethod
    def load(cls, id: int, hInst: int = NULL) -> 'Icon':
        """
        Load an icon from resource.
        """
        
        icon = cls.foreign_owner(LoadIconW(hInst, i_cast(id, LPCWSTR)))
        
        if not icon.value:
            raise WinException()
        
        return icon
    
    def save(self, path: str, bpp: int=24):
        with open(path, 'wb') as icon:
            with DC.create_compatible(NULL) as dc:
                # write icon header and retrieve icon info
                icon.write(b'\x00\x00\x01\x00\x01\x00')
                info = self.icon_info
                
                # get color and mask of icon
                color = info.color.exchange_owner()
                mask = info.mask.exchange_owner()
                
                # retrieve the input color bitmap info
                bm_info = BitmapInfo(0, 0, -1)
                dc.get_di_bits(color, NULL, bm_info)
                
                # calculate out bitmap info size
                out_bm_info_size = BitmapInfo.size()
                if bpp < 24: out_bm_info_size += RGBQUAD.size() * (1 << bpp)
                
                # create instance of local allocator (malloc)
                allocator = CLocalAllocator()
                
                # allocate and fill the bitmap info
                out_bm_info = BitmapInfo.allocate(out_bm_info_size, allocator)
                allocator.copy(out_bm_info.ref(), bm_info.ref(), BitmapInfo.size())
                out_bm_info.bpp = bpp
                
                # allocate and retrieve bitmap bits
                out_bm_bits = allocator.allocate(bm_info.image_size)
                dc.get_di_bits(color, out_bm_bits, out_bm_info, lines=bm_info.height)
                
                # get mask data
                mask_info = BitmapInfo(0, 0, -1)
                dc.get_di_bits(mask, NULL, mask_info)
                
                # allocate and fill the mask bitmap info
                out_mask_info = BitmapInfo.allocate(
                    BitmapInfo.size() + 2 * RGBQUAD.size(), allocator)
                allocator.copy(out_mask_info.ref(), mask_info.ref(), mask_info.size())
                
                # allocate and retrieve mask bits
                out_mask_bits = allocator.allocate(mask_info.image_size)
                dc.get_di_bits(mask, out_mask_bits, out_mask_info, lines=mask_info.height)
                
                # create and fill the icon directory
                d = ICONDIRENTRY()
                d.nWidth = bm_info.width
                d.nHeight = bm_info.height
                d.nNumColorsInPalette = 16 if bpp == 4 else 0
                d.nBitsPerPixel = bm_info.bpp
                d.nDataLength = bm_info.image_size + mask_info.image_size + out_bm_info_size
                d.nOffset = d.size() + 6
                
                # create Memory I/O for bitmap info and write to icon
                out_bm_info_io = MemoryIO(out_bm_info.ref(), out_bm_info_size)
                icon.write(out_bm_info_io.read())
                
                # create Memory I/O for icon directory and write to icon
                icondir_io = MemoryIO(d.ref(), d.size())
                icon.write(icondir_io.read())
                
                # preserve image size for writing, we are modifying field value
                out_bm_size = out_bm_info.image_size
                # write DIB header (including color table):
                out_bm_info.height *= 2 # because the header is for both bm and mask
                out_bm_info.image_size += mask_info.image_size
                
                # write bitmap info I/O again, but with modified values
                icon.write(out_bm_info_io.read())
                
                # create Memory I/O for color bitmap bits and write to icon
                bm_bits_io = MemoryIO(out_bm_bits, out_bm_size)
                icon.write(bm_bits_io.read())
                
                # create Memory I/O for mask bitmap bits and write to icon
                mask_bits_io = MemoryIO(out_mask_bits, mask_info.image_size)
                icon.write(mask_bits_io.read())
    
class CursorMeta(Handle.__class__):
    @property
    def position(cls) -> tuple[int, int]:
        pt = POINT()
        if not GetCursorPos(byref(pt)):
            raise WinException()
        return (pt.x, pt.y)
    
    @position.setter
    def position(cls, position: GraphicUtils.Point):
        x, y = GraphicUtils.point_tuple(position)
        if not SetCursorPos(x, y):
            raise WinException()
        
    @property
    def x(cls) -> int:
        return cls.position[0]
    
    @x.setter
    def x(cls, x: int):
        cls.position = (x, cls.y) 
        
    @property
    def y(cls) -> int:
        return cls.position[1]
    
    @y.setter
    def y(cls, y: int):
        cls.position = (cls.x, y)
    
class Cursor(Handle, metaclass=CursorMeta):
    """
    Class, representing cursor.
    """
    
    def close(self):
        DestroyCursor(self)
        self._closed = True
    
    @classmethod
    def show(cls):
        ShowCursor(TRUE)
        
    @classmethod
    def hide(cls):
        ShowCursor(FALSE)
    
    @classmethod
    def set(cls, cursor: int | HANDLE) -> 'Cursor':
        return Cursor.foreign_owner(SetCursor(cursor))
        
    @classmethod
    def get(cls) -> 'Cursor':
        return Cursor.foreign_owner(GetCursor())
    
    @classmethod
    def load(cls, id: int, hInst: int = NULL) -> 'Cursor':
        """
        Load the cursor from resource.
        """
        
        icon = cls.foreign_owner(LoadCursorW(hInst, i_cast(id, LPCWSTR)))
        
        if not icon.value:
            raise WinException()
        
        return icon
    
    @classmethod
    def from_cursor(cls, path: str, width: int = 0, height: int = 0) -> 'Cursor':
        """
        Create the cursor from CUR/ANI/ICO file.
        """
        
        cursor = cls()
        cursor.value = LoadImageW(
            NULL, path, IMAGE_CURSOR, width, height, 
            LR_LOADFROMFILE | LR_DEFAULTSIZE)
        
        if not cursor.value:
            raise WinException()
        
        return cursor
    
class Palette(GDIObjectHandle):
    """
    Class, representing the GDI palette.
    """
    
    @classmethod
    def create(cls, entries: Iterable[PALETTEENTRY]) -> 'Palette':
        """
        Create the palette.
        """
        
        palNumEntries = len(entries)
        
        lp = LOGPALETTE.allocate(LOGPALETTE.size() + PtrArithmetic.size(PALETTEENTRY, palNumEntries))
        lp.palVersion = 0x300
        lp.palNumEntries = len(entries)
        
        for i, entry in enumerate(entries):
            lp.palPalEntry[i] = entry
        
        palette = cls(CreatePalette(lp.ref()))
        if not palette.value:
            raise WinException()
        
        return palette
        
class Bitmap(GDIObjectHandle):
    """
    Class, representing the GDI Bitmap object.
    """
    
    @classmethod
    def create(self, width: int, height: int, planes: int = 1, bit_count: int = 32, bits = NULL):
        """
        Create the bitmap by width/height, optionally planes, bpp and bits.
        """
        
        bitmap = Bitmap()
        if width + height != -2: # width == -1, height == -1
            bitmap.value = CreateBitmap(width, height, planes, bit_count, bits)
        return bitmap
    
    @classmethod
    def from_icon(self, icon: int | HANDLE) -> 'Bitmap':
        """
        Create the bitmap from ICO icon.
        """
        
        with DC.get().create_compatible() as dc:
            if not isinstance(icon, Icon):
                icon = Icon.foreign_owner(icon)
            
            info = icon.icon_info
            mask = info.mask
            bm = mask.object
            
            width = bm.bmWidth
            height = bm.bmHeight
            
            if not info.color:
                height //= 2
            
            bitmap = dc.create_compatible_bitmap(width, height)
            
            with dc.select_ex(bitmap):
                dc.draw_icon(0, 0, width, height, icon)
            
            return bitmap
        
    @classmethod
    def load(self, path: str) -> 'Bitmap':
        """
        Load bitmap from path.
        """
        bitmap = Bitmap(LoadImage(NULL, path, IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE))
        if not bitmap.value:
            raise WinException()
        return bitmap

class PaintDC(DC):
    """
    Class, representing GDI device context for window painting.
    """
    
    paint_struct: PAINTSTRUCT
    _hwnd: int | HWND
    
    def __init__(self, hwnd: int | HWND):
        super().__init__()
        self.paint_struct = PAINTSTRUCT()
        self._hwnd = hwnd
        self.value = BeginPaint(hwnd, self.paint_struct.ref())
        if not self.value:
            raise WinException()
        
    def close(self):
        if not EndPaint(self._hwnd, self.paint_struct.ref()):
            raise WinException()
        self._closed = True

class GLContext(Handle):
    """
    Class, representing the OpenGL context.
    """
    
    _current: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._current = False
    
    @classmethod
    def current(self, hDC: int | HANDLE) -> 'GLContext':
        """
        Create the OpenGL context and make it current.
        """
        
        hGLCtx = wglCreateContext(hDC)
        if not hGLCtx:
            raise WinException()
        return GLContext.current_external(hDC, hGLCtx).owned_current(True)
    
    @classmethod
    def current_external(self, hDC: int | HANDLE, hGLCtx: int | HANDLE) -> 'GLContext':
        """
        Make OpenGL context current.
        """
        
        glCtx = GLContext(hGLCtx)
        if not wglMakeCurrent(hDC, hGLCtx):
            raise WinException()
        return glCtx
    
    def owned_current(self, value: bool):
        """
        Exchange the "current" state of context owning to local or foreign.
        """
        
        self._current = value
        return self
    
    def close(self):
        if self._current:
            wglMakeCurrent(NULL, NULL)
        wglDeleteContext(self)
        self._closed = True

EVENT_ALL_ACCESS = 0x1F0003
EVENT_MODIFY_STATE = 0x2
INFINITE = 0xffffffff

class Event(Handle):
    """
    Class, representing Win32 Event.
    """
    
    @classmethod
    def create(cls, name: str = None, initial: bool = False, manual_reset: bool = True, 
               security_attributes: SECURITY_ATTRIBUTES = NULL, access: int = EVENT_ALL_ACCESS) -> 'Event':
        if name is not None and not name.startswith('\\'):
            name = '\\Local\\' + name
        pSecurityAttributes = security_attributes.ref() if security_attributes is not NULL else NULL
        flags = 0
        if initial:
            flags |= CREATE_EVENT_INITIAL_SET
        if manual_reset:
            flags |= CREATE_EVENT_MANUAL_RESET
        event = cls(CreateEventExW(pSecurityAttributes, name, flags, access))
        if not event.value:
            raise WinException()
        return event
    
    @classmethod
    def open(cls, name: str, access: int = EVENT_MODIFY_STATE | SYNCHRONIZE, inherit_handle: bool = False) -> 'Event':
        """
        Open event by its name.
        """
        if not name.startswith('\\'):
            name = '\\Local\\' + name
        event = cls(OpenEventW(access, inherit_handle, name))
        if not event.value:
            raise WinException()
        return event
    
    def close(self):
        CloseHandle(self)
        self._closed = True
    
    def trigger(self):
        """
        Trigger event.
        """
        SetEvent(self)
    
    def reset(self):
        """
        Reset event.
        """
        ResetEvent(self)
        
    def wait(self, time: int=INFINITE):
        """
        Wait for given time at event.
        """
        Abs.Synchronization.wait(time, self)
        
class CriticalSection(RTL_CRITICAL_SECTION):
    """
    Class, representing Win32 Critical section.
    """
    
    def __init__(self):
        InitializeCriticalSection(byref(self))
        
    def __del__(self):
        DeleteCriticalSection(byref(self))
        
    def __enter__(self):
        self.enter()
        
    def __exit__(self, *_):
        self.leave()
        
    def enter(self):
        """
        Enter critical section.
        """
        EnterCriticalSection(byref(self))
        
    def leave(self):
        """
        Leave critical section.
        """
        LeaveCriticalSection(byref(self))
        
class Semaphore(Handle):
    """
    Class, representing Win32 Semaphore.
    """
    
    @classmethod
    def create(cls, name: str = None, initial: int = 32, maximum: int = 32, access: int = SEMAPHORE_ALL_ACCESS,
               security_attributes: SECURITY_ATTRIBUTES = NULL) -> 'Event':
        if name is not None and not name.startswith('\\'):
            name = '\\Local\\' + name
        pSecurityAttributes = security_attributes.ref() if security_attributes is not NULL else NULL
        event = cls(CreateSemaphoreExW(pSecurityAttributes, initial, maximum, name, 0, access))
        if not event.value:
            raise WinException()
        return event
    
    @classmethod
    def open(cls, name: str, inherit_handle: bool=False, access: int=SEMAPHORE_MODIFY_STATE | SYNCHRONIZE) -> 'Semaphore':
        """
        Open semaphore by its name.
        """
        if name is not None and not name.startswith('\\'):
            name = '\\Local\\' + name
        event = cls(OpenSemaphoreW(access, inherit_handle, name))
        if not event.value:
            raise WinException()
        return event
    
    def __enter__(self):
        self.wait()
        
    def __exit__(self, *_):
        self.release()
    
    def release(self, count: int = 1):
        """
        Release semaphore.
        """
        if not ReleaseSemaphore(self, count, NULL):
            raise WinException()
        
    def wait(self, time: int=INFINITE):
        """
        Wait for semaphore signal state.
        """
        Abs.Synchronization.wait(time, self)
    
    def close(self):
        CloseHandle(self)
        self._closed = True