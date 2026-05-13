# Win32 errors stringification and WinException
from win.defbase_errordef import *

# WinAPI header files
from win.handleapi import *
from win.synchapi import *
from win.winuser import *
from win.wingdi import *
from win.winnt import *

class Rect(RECT, CStructure):
    """
    Rectangle.
    """
    
    def __init__(self, left: int = 0, top: int = 0,
                 right: int = 0, bottom: int = 0):
        super().__init__(left, top, right, bottom)
        
    @classmethod
    def create(self, left: int = 0, top: int = 0,
               width: int = 0, height: int = 0) -> 'Rect':
        """
        Create the rectangle by x/y + width/height.
        """
        
        return Rect(left, top, left + width, top + height)
    
    @property
    def width(self) -> int:
        return self.right - self.left
    
    @width.setter
    def width(self, width: int):
        self.right = self.left + width
    
    @property
    def height(self) -> int:
        return self.bottom - self.top

    @height.setter
    def height(self, height: int):
        self.bottom = self.top + height
        
    def offset(self, dx: int, dy: int):
        """
        Offset the rect by delta X and delta Y.
        """
        
        OffsetRect(byref(self), int(dx), int(dy))
    
    def deflate(self, dx: int, dy: int):
        """
        Deflate the rect by delta X and delta Y.
        (Inflate by {-dx, -dy})
        """
        
        InflateRect(byref(self), -int(dx), -int(dy))
    
    def inflate(self, dx: int, dy: int):
        """
        Deflate the rect by delta X and delta Y.
        """
        
        InflateRect(byref(self), int(dx), int(dy))
    
    def __contains__(self, pt: 'GraphicUtils.Point') -> bool:
        pt = GraphicUtils.point(pt)
        return PtInRect(byref(self), pt)
    
class Point(POINT, CStructure): ...
    
class Size(SIZE, CStructure): ...

class Handle(HANDLE):
    """
    Main Win32 abstract handle wrapper.
    """
    
    _released: bool
    _closed: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._released = False
        self._closed = False
    
    @classmethod
    def foreign_owner(cls, val: int | HANDLE) -> Self:
        """
        Create the handle instance from foreign handle.
        """
        
        if not val: return None # if invalid handle was provided, when return None
        instance = cls(val)
        instance._closed = True # formally the handle is closed (by logic if it is already closed, 
                                # it cannot be closed, so it is our variant)
        return instance
    
    def exchange_owner(self):
        """
        Exchange the owner of handle from local -> foreign, or foreign -> local.
        """
        
        self._closed = not self._closed
        return self
    
    def __enter__(self):
        self._released = False
        self._closed = False
        return self
        
    def __exit__(self, *_):
        if not self._released:
            self._released = True
            if self.value:
                self.close()
            
    def __del__(self):
        if not self._closed and self.value:
            self.close()
    
    @interface_abstract_method 
    def close(self):
        """
        Abstract method to release the handle.
        """
        
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

# i don't know why UxTheme is there, but let it stay here
uxtheme = get_win_library('uxtheme.dll')

@uxtheme.foreign(HRESULT, HWND, HDC, PRECT)
def DrawThemeParentBackground(hwnd: int | HANDLE, hdc: int | HANDLE, prc: PRECT) -> int: ...

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
            
            def __getitem__(self, y: int) -> 'Color.RGB':
                return Color.RGB(GetPixel(self.dc, self.x, y))
            
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
    def get(self, hwnd: int | HWND = NULL) -> 'DC':
        """
        Get the device context for HWND.
        """
        
        hDC = GetDC(hwnd)
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
        
    def set_pixel(self, x: int, y: int, color: TUnion[int, 'Color.IColor']) -> 'Color.RGB':
        """
        Set the pixel by given coordinates to given color.
        """
        
        crColor = SetPixel(self, x, y, int(color))
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.RGB(crColor)
    
    @property
    def text_color(self) -> 'Color.RGB':
        crColor = GetTextColor(self)
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.RGB(crColor)
    
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
    def bk_color(self) -> 'Color.RGB':
        crColor = GetBkColor(self)
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.RGB(crColor)
    
    @bk_color.setter
    def bk_color(self, bk_color: TUnion[int, 'Color.IColor']):
        self.set_bk_color(bk_color)
    
    def set_bk_color(self, color: TUnion[int, 'Color.IColor']) -> 'Color.RGB':
        """
        Set the background color.
        """
        
        crColor = SetBkColor(self, int(color))
        if crColor == CLR_INVALID:
            raise WinException()
        return Color.RGB(crColor)
    
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
        if not GetViewportExtEx(byref(extents)):
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
        if not GetWindowExtEx(byref(extents)):
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

class GraphicUtils:
    Point: TypeAlias = POINT | tuple[SupportsInt, SupportsInt]
    Size: TypeAlias = SIZE | tuple[SupportsInt, SupportsInt]
    PointArray: TypeAlias = Iterable[Point]
    
    @staticmethod
    def linear(x: int, y: int, rcSource: RECT, rcTarget: RECT) -> POINT:
        """
        Linear expansion of (x, y) by source and target rectangles.
        """
        
        x = rcTarget.left + (x - rcSource.left) * (rcTarget.right - rcTarget.left) / (rcSource.right - rcSource.left)
        y = rcTarget.top + (y - rcSource.top) * (rcTarget.bottom - rcTarget.top) / (rcSource.bottom - rcSource.top)
        return POINT(int(x), int(y))
    
    @staticmethod
    def center(x: int, y: int, rcSource: RECT, rcTarget: RECT) -> POINT:
        """
        Center expansion of (x, y) by source and target rectangles.
        """
        
        x = x + ((rcTarget.left + rcTarget.right) / 2 - (rcSource.left + rcSource.right) / 2)
        y = y + ((rcTarget.top + rcTarget.bottom) / 2 - (rcSource.top + rcSource.bottom) / 2)
        return POINT(int(x), int(y))
    
    @staticmethod
    def size_rect(rcSource: RECT, rcTarget: RECT) -> RECT:
        """
        Proportionally size the given rect into the target rect.
        """
        
        scaleX = (rcTarget.right - rcTarget.left) / (rcSource.right - rcSource.left)
        scaleY = (rcTarget.bottom - rcTarget.top) / (rcSource.bottom - rcTarget.top)
        scale = min(scaleX, scaleY)  
        newW = (rcSource.right - rcSource.left) * scale
        newH = (rcSource.bottom - rcSource.top) * scale
        left = rcTarget.left + ((rcTarget.right - rcTarget.left) - newW) / 2
        top = rcTarget.top + ((rcTarget.bottom - rcTarget.top) - newH) / 2
        right = left + newW
        bottom = top + newH
        return RECT(int(left), int(top), int(right), int(bottom))
    
    @staticmethod
    def in_rect(x: int, y: int, rc: RECT) -> bool:
        """
        Check point in rectangle.
        """
        
        return bool(PtInRect(byref(rc), POINT(x, y)))
    
    class Vertex(TRIVERTEX):
        def __init__(self, x: int, y: int, red: int, green: int, blue: int, alpha: int = 255):
            red *= 256
            green *= 256
            blue *= 256
            alpha *= 256
            
            super().__init__(x, y, red, green, blue, alpha)
    
    @staticmethod
    def size_tuple(size: 'GraphicUtils.Size') -> tuple[int, int]:
        """
        Convert SIZE/tuple to (cx, cy) tuple.
        """
        
        if isinstance(size, SIZE):
            return (size.cx, size.cy)
        return size[0:2]
    
    @staticmethod
    def size(size: 'GraphicUtils.Size') -> SIZE:
        """
        Convert SIZE/tuple to SIZE structure.
        """
        
        if isinstance(size, SIZE):
            return size
        return SIZE(*size[0:2])
    
    @staticmethod
    def point_tuple(pt: 'GraphicUtils.Point') -> tuple[int, int]:
        """
        Convert POINT/tuple to (x, y) tuple.
        """
        
        if isinstance(pt, POINT):
            return (pt.x, pt.y)
        return pt[0:2]
    
    @staticmethod
    def point(pt: 'GraphicUtils.Point') -> POINT:
        """
        Convert POINT/tuple to POINT structure.
        """
        
        if isinstance(pt, POINT):
            return pt
        return POINT(*pt[0:2])
            
    @staticmethod
    def point_array(array: 'GraphicUtils.PointArray') -> IArray[POINT]:
        """
        Convert the POINT/{x,y} iterable to ctypes POINT array.
        """
        
        result_array = []
        
        for point in array:
            if isinstance(point, POINT):
                result_array.append(point)
            elif isinstance(point, tuple):
                x, y = point[0:2]
                x, y = int(x), int(y)
                result_array.append(POINT(x, y))
            else:
                raise ValueError(type(point))
        
        c_array = (POINT * len(array))(*array)
        return c_array

class Color:
    @classmethod
    def system(cls, index: int) -> 'Color.RGB':
        """
        Get the system color.
        """
        
        return Color.BGR(GetSysColor(index))
    
    class IColor(IHasInit):
        """
        Abstract class for interfacing color functionality.
        """
        
        value: int
        
        def __init__(self, value: int = 0):
            self.value = value
        
        @interface_abstract_method
        @property
        def r(self) -> int: ...
        
        @interface_abstract_method
        @property
        def g(self) -> int: ...
        
        @interface_abstract_method
        @property
        def b(self) -> int: ...
        
        @interface_abstract_method
        @classmethod
        def color(self, r: int, g: int, b: int) -> 'Color.IColor': ...

        def rgb(self) -> 'Color.RGB':
            """
            Convert color into RGB.
            """
            
            return Color.RGB.color(self.r, self.g, self.b)
        
        def bgr(self) -> 'Color.BGR':
            """
            Convert color into BGR.
            """
            
            return Color.BGR.color(self.r, self.g, self.b)
        
        def rgba(self) -> 'Color.RGBA':
            """
            Convert color into RGBA.
            """
            
            return Color.RGBA.color(self.r, self.g, self.b, 0xff)
        
        def argb(self) -> 'Color.ARGB':
            """
            Convert color into ARGB.
            """
            
            return Color.ARGB.color(self.r, self.g, self.b, 0xff)
        
        def abgr(self) -> 'Color.ABGR':
            """
            Convert color into ABGR.
            """
            
            return Color.ABGR.color(self.r, self.g, self.b, 0xff)
        
        def bgra(self) -> 'Color.BGRA':
            """
            Convert color into BGRA.
            """
            
            return Color.BGRA.color(self.r, self.g, self.b, 0xff)
        
        def gl(self) -> 'Color.GLColor':
            """
            Convert color into OpenGL format.
            """
            
            return self.rgba().gl()
        
        def __index__(self) -> int:
            return self.value
        
        def __int__(self) -> int:
            return self.value
        
        def __str__(self) -> str:
            return format_hex(self, 6)
        
        def __repr__(self) -> str:
            return str(self)
        
        def __add__(self, value):
            return self.value + value
        
        def __sub__(self, value):
            return self.value - value
        
        def __mul__(self, value):
            return self.value * value
        
        def __truediv__(self, value):
            return self.value / value
        
        def __floordiv__(self, value):
            return self.value // value
        
        def __lshift__(self, value):
            return self.value << value
        
        def __rshift__(self, value):
            return self.value >> value
        
        def __or__(self, value):
            return self.value | value
        
        def __and__(self, value):
            return self.value & value
        
        def __inv__(self):
            return ~self.value
        
        def __neg__(self):
            return -self.value
        
        def __pos__(self):
            return +self.value
        
        def hsl(self) -> 'Color.HSL':
            """
            Convert color into HSL.
            """
            
            r_norm = self.r / 255
            g_norm = self.g / 255
            b_norm = self.b / 255
            maximum = max(r_norm, g_norm, b_norm)
            minimum = min(r_norm, g_norm, b_norm)
            delta = maximum - minimum
            if delta == 0:
                hue = 0
            elif maximum == r_norm:
                hue = 60 * (((g_norm - b_norm) / delta) % 6)
            elif maximum == g_norm:
                hue = 60 * (((b_norm - r_norm) / delta) + 2)
            elif maximum == b_norm:
                hue = 60 * (((r_norm - g_norm) / delta) + 4)
            else:
                hue = 0
            luminance = (maximum + minimum) / 2
            if delta == 0:
                saturation = 0
            else:
                saturation = delta / (1 - abs(2 * luminance - 1))
            return Color.HSL(hue, luminance, saturation)

    class IColorAlpha(IColor):
        """
        Abstract class for interfacing color functionality with alpha channel.
        """
        
        @interface_abstract_method
        @property
        def a(self) -> int: ...
        
        @interface_abstract_method
        @classmethod
        def color(self, r: int, g: int, b: int, a: int) -> 'Color.IColorAlpha': ...
        
        def rgba(self) -> 'Color.RGBA':
            return Color.RGBA(self.r, self.g, self.b, self.a)
        
        def argb(self) -> 'Color.ARGB':
            return Color.ARGB.color(self.r, self.g, self.b, self.a)
        
        def abgr(self) -> 'Color.ABGR':
            return Color.ABGR.color(self.r, self.g, self.b, self.a)
        
        def bgra(self) -> 'Color.BGRA':
            return Color.BGRA.color(self.r, self.g, self.b, self.a)
        
        def gl(self) -> 'Color.GLColor':
            return Color.GLColor(self)
        
        def __str__(self) -> str:
            return format_hex(self, 8)
        
    class RGB(IColor):
        """
        RGB Representation of color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int) -> 'Color.RGB':
            return cls((r << 8 | g) << 8 | b)
        
        @property
        def r(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 8 & 0xff
        
        @property
        def b(self) -> int:
            return self & 0xff
        
        @r.setter
        def r(self, r: int):
            self.value = (r << 8 | self.g) << 8 | self.b
        
        @g.setter
        def g(self, g: int):
            self.value = (self.r << 8 | g) << 8 | self.b
        
        @b.setter
        def b(self, b: int):
            self.value = (self.r << 8 | self.g) << 8 | b
        
        def __iter__(self):
            return iter((self.r, self.g, self.b))

    class RGBA(IColorAlpha):
        """
        RGBA Representation of alpha-channeled color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.RGBA':
            return cls(((r << 8 | g) << 8 | b) << 8 | a)
        
        @property
        def a(self) -> int: 
            return self & 0xff

        @property
        def r(self) -> int:
            return self >> 24 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def b(self) -> int:
            return self >> 8 & 0xff
        
        @r.setter
        def r(self, r: int):
            self.value = ((r << 8 | self.g) << 8 | self.b) << 8 | self.a
        
        @g.setter
        def g(self, g: int):
            self.value = ((self.r << 8 | g) << 8 | self.b) << 8 | self.a
        
        @b.setter
        def b(self, b: int):
            self.value = ((self.r << 8 | self.g) << 8 | b) << 8 | self.a

        @a.setter
        def a(self, a: int):
            self.value = ((self.r << 8 | self.g) << 8 | self.b) << 8 | a
        
        def __iter__(self):
            return iter((self.r, self.g, self.b, self.a))
        
    class BGR(IColor):
        """
        BGR Representation of color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int) -> 'Color.BGR':
            return cls((b << 8 | g) << 8 | r)
        
        @property
        def b(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 8 & 0xff
        
        @property
        def r(self) -> int:
            return self & 0xff
        
        @b.setter
        def b(self, b: int):
            self.value = (b << 8 | self.g) << 8 | self.r
        
        @g.setter
        def g(self, g: int):
            self.value = (self.b << 8 | g) << 8 | self.r
        
        @r.setter
        def r(self, r: int):
            self.value = (self.b << 8 | self.g) << 8 | r
        
        def __iter__(self):
            return iter((self.b, self.g, self.r))
        
    class BGRA(IColorAlpha):
        """
        BGRA Representation of alpha-channeled color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.BGRA':
            return cls(((b << 8 | g) << 8 | r) << 8 | a)
        
        @property
        def b(self) -> int:
            return self >> 24 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def r(self) -> int:
            return self >> 8 & 0xff
        
        @property
        def a(self) -> int:
            return self & 0xff
        
        @b.setter
        def b(self, b: int):
            self.value = ((b << 8 | self.g) << 8 | self.r) << 8 | self.a
        
        @g.setter
        def g(self, g: int):
            self.value = ((self.b << 8 | g) << 8 | self.r) << 8 | self.a
        
        @r.setter
        def r(self, r: int):
            self.value = ((self.b << 8 | self.g) << 8 | r) << 8 | self.a

        @a.setter
        def a(self, a: int):
            self.value = ((self.b << 8 | self.g) << 8 | self.r) << 8 | a
        
        def __iter__(self):
            return iter((self.b, self.g, self.r, self.a))
        
    class ARGB(IColorAlpha):
        """
        ARGB Representation of alpha-channeled color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.ARGB':
            return cls(((a << 8 | r) << 8 | g) << 8 | b)
        
        @property
        def a(self) -> int:
            return self >> 24 & 0xff
        
        @property
        def r(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 8 & 0xff
        
        @property
        def b(self) -> int:
            return self & 0xff
        
        @a.setter
        def a(self, a: int):
            self.value = ((a << 8 | self.r) << 8 | self.g) << 8 | self.b
            
        @r.setter
        def r(self, r: int):
            self.value = ((self.a << 8 | r) << 8 | self.g) << 8 | self.b
        
        @g.setter
        def g(self, g: int):
            self.value = ((self.a << 8 | self.r) << 8 | g) << 8 | self.b
        
        @b.setter
        def b(self, b: int):
            self.value = ((self.a << 8 | self.r) << 8 | self.g) << 8 | b
        
        def __iter__(self):
            return iter((self.a, self.r, self.g, self.b))
        
    class ABGR(IColorAlpha):
        """
        ABGR Representation of alpha-channeled color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.ABGR':
            return cls(((a << 8 | b) << 8 | g) << 8 | r)
        
        @property
        def a(self) -> int:
            return self >> 24 & 0xff
        
        @property
        def b(self) -> int:
            return self >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self >> 8 & 0xff
        
        @property
        def r(self) -> int:
            return self & 0xff
        
        @a.setter
        def a(self, a: int):
            self.value = ((a << 8 | self.b) << 8 | self.g) << 8 | self.r
        
        @b.setter
        def b(self, b: int):
            self.value = ((self.a << 8 | b) << 8 | self.g) << 8 | self.r
        
        @g.setter
        def g(self, g: int):
            self.value = ((self.a << 8 | self.b) << 8 | g) << 8 | self.r
        
        @r.setter
        def r(self, r: int):
            self.value = ((self.a << 8 | self.b) << 8 | self.g) << 8 | r
        
        def __iter__(self):
            return iter((self.a, self.b, self.g, self.r))
        
    class HSL:
        """
        HSL Representation of color.
        """
        
        def __init__(self, hue: float = 0.0, saturation: float = 0.0, luminance: float = 0.0):
            self.hue = hue
            self.saturation = saturation
            self.luminance = luminance
            
        @property
        def h(self) -> int:
            return round(self.hue * 360)
        
        @h.setter
        def h(self, h: int):
            self.hue = h * 360.0
        
        @property
        def s(self) -> int:
            return round(self.saturation * 100)
        
        @s.setter
        def s(self, s: int):
            self.saturation = s * 100.0
        
        @property
        def l(self) -> int:
            return round(self.luminance * 100)
        
        @l.setter
        def l(self, l: int):
            self.luminance = l * 360.0
            
        def __iter__(self):
            return iter((self.h, self.s, self.l))
        
        def __str__(self):
            return f'({self.h} {self.s} {self.l})'
            
        def __repr__(self):
            return str(self)

        def rgb(self) -> 'Color.RGB':
            """
            Convert color into RGB.
            """
            
            r = MathUtil.clamp(abs(self.hue * 6.0 - 3.0) - 1.0, 0.0, 1.0)
            g = MathUtil.clamp(2.0 - abs(self.hue * 6.0 - 2.0), 0.0, 1.0)
            b = MathUtil.clamp(2.0 - abs(self.hue * 6.0 - 4.0), 0.0, 1.0)
            c = (1.0 - abs(2.0 * self.luminance - 1.0)) * self.saturation
            r = (r - 0.5) * c + self.luminance
            g = (g - 0.5) * c + self.luminance
            b = (b - 0.5) * c + self.luminance
            return Color.RGB.color(int(r * 255), int(g * 255), int(b * 255))
        
        def rgba(self) -> 'Color.RGBA':
            """
            Convert color into RGBA.
            """
            
            return self.rgb().rgba()
        
        def bgr(self) -> 'Color.BGR':
            """
            Convert color into BGR.
            """
            
            return self.rgb().bgr()
        
        def bgra(self) -> 'Color.BGRA':
            """
            Convert color into BGRA.
            """
            
            return self.rgb().bgra()
        
        def argb(self) -> 'Color.ARGB':
            """
            Convert color into ARGB.
            """
            
            return self.rgb().argb()
        
        def abgr(self) -> 'Color.ABGR':
            """
            Convert color into ABGR.
            """
            
            return self.rgb().abgr()
    
    class GLColor:
        """
        OpenGL format color representation.
        """
        value: 'Color.IColorAlpha'
        
        def __init__(self, value: 'Color.IColorAlpha'):
            self.value = value
        
        @property
        def r(self) -> float:
            return self.value.r / 255
        
        @r.setter
        def r(self, r: float):
            self.value.r = int(r * 255)
        
        @property
        def g(self) -> float:
            return self.value.g / 255
        
        @g.setter
        def g(self, g: float):
            self.value.g = int(g * 255)
        
        @property
        def b(self) -> float:
            return self.value.b / 255
        
        @b.setter
        def b(self, b: float):
            self.value.b = int(b * 255)
        
        @property
        def a(self) -> float:
            return self.value.a / 255
        
        @a.setter
        def a(self, a: float):
            self.value.a = int(a * 255)
            
        def rgb(self) -> 'Color.RGB':
            """
            Convert color into RGB.
            """
            return self.value.rgb()
            
        def bgr(self) -> 'Color.BGR':
            """
            Convert color into BGR.
            """
            return self.value.bgr()
            
        def rgba(self) -> 'Color.RGBA'
            """
            Convert color into RGBA.
            """:
            return self.value.rgba()
            
        def argb(self) -> 'Color.ARGB':
            """
            Convert color into ARGB.
            """
            return self.value.argb()
            
        def abgr(self) -> 'Color.ABGR':
            """
            Convert color into ABGR.
            """
            return self.value.abgr()
            
        def bgra(self) -> 'Color.BGRA':
            """
            Convert color into BGRA.
            """
            return self.value.bgra()
        
        def hsl(self) -> 'Color.HSL':
            """
            Convert color into HSL.
            """
            return self.value.hsl()
        
        def gl(self) -> 'Color.GLColor':
            """
            Convert color into OpenGL format.
            """
            return self
        
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
        if not self.value:
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
        if not self.value:
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
    def from_bitmap(self, bitmap: int | HANDLE) -> 'Icon':
        """
        Create an icon from bitmap.
        """
        
        if not isinstance(bitmap, Bitmap):
            bitmap = Bitmap.foreign_owner(bitmap)
        
        bm = bitmap.object
        mask = Bitmap(bm.bmWidth, bm.bmHeight, bit_count=1)
        
        with DC.create_compatible(NULL) as bitmapDC, DC.create_compatible(NULL) as maskDC:
            with bitmapDC.select_ex(bitmap), maskDC.select_ex(mask):
                maskDC.bit_blt(0, 0, 0, 0, bm.bmWidth, bm.bmHeight, bitmapDC, SRCCOPY)
        
        info = IconInfo.foreign_owner()
        info.is_icon = True
        info.color = bitmap
        info.mask = mask
        
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
        
class Event(Handle):
    """
    Class, representing Win32 Event.
    """
    
    def __init__(self, name: str = None, initial: bool = False, manual_reset: bool = True, 
                 security_attributes: SECURITY_ATTRIBUTES = NULL):
        super().__init__()
        name = '\\Local\\' + name
        pSecurityAttributes = security_attributes.ref() if security_attributes is not None else NULL
        self.value = CreateEventW(pSecurityAttributes, manual_reset, initial, name)
        if not self.value:
            raise WinException()
    
    def close(self):
        CloseHandle(self)
        self._closed = True