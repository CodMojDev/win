from win.defbase_errordef import *
from win.winuser import *
from win.wingdi import *

class Handle(HANDLE):
    _released: bool
    _closed: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._released = False
        self._closed = False
    
    @classmethod
    def foreign_owner(cls, val: int | HANDLE):
        instance = cls(val)
        instance._closed = True
        return instance
    
    def __enter__(self):
        self._released = False
        self._closed = False
        return self
        
    def __exit__(self, *_):
        if not self._released:
            self._released = False
            if self.value:
                self.close()
            
    def __del__(self):
        if not self._closed and self.value:
            self.close()
    
    @interface_abstract_method 
    def close(self):
        ...
        
class GDIObjectHandle(Handle):
    def close(self):
        DeleteObject(self)
        self._closed = True
        
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
            lf = LOGFONT()
            if not GetObject(self, sizeof(lf), lf.ref()):
                raise WinException()
            return lf

class DC(Handle):
    class Select:
        object: int | HANDLE
        dc: 'DC'
        
        def __init__(self, dc: 'DC', object: int | HANDLE):
            self.object = dc.select(object)
            self.dc = dc
            
        def __enter__(self):
            return self
        
        def __exit__(self, *_):
            self.dc.select(self.object)
            
    _created: bool
    
    def __init__(self, dc: int = NULL, hwnd: int = NULL):
        super().__init__(dc)
        self._created = False
        self._hwnd = hwnd
    
    def close(self):
        if self._created:
            DeleteDC(self)
        else:
            ReleaseDC(self._hwnd, self)
        self._closed = True
            
    def create_compatible(self) -> 'DC':
        dc = DC(CreateCompatibleDC(self))
        dc._created = True
        return dc
    
    def create_compatible_bitmap(self, width: int, height: int) -> 'Bitmap':
        bitmap = Bitmap()
        bitmap.value = CreateCompatibleBitmap(self, width, height)
        if not bitmap.value:
            raise WinException()
        return bitmap
        
    @classmethod
    def get(self, hwnd: int | HWND = NULL) -> 'DC':
        return DC(GetDC(hwnd))
        
    def select(self, hGdiObject: int | HANDLE) -> int:
        return SelectObject(self, hGdiObject)
    
    def select_ex(self, hGdiObject: int | HANDLE) -> 'DC.Select':
        return DC.Select(self, hGdiObject)
    
    def text_out(self, x: int, y: int, text: str):
        buf = create_unicode_buffer(text)
        if not TextOutW(self, x, y, buf, len(text)):
            raise WinException()
        
    def set_pixel(self, x: int, y: int, color: int) -> int:
        crColor = SetPixel(self, x, y, color)
        if crColor == CLR_INVALID:
            raise WinException()
        return crColor
    
    def set_text_color(self, color: int) -> int:
        crColor = SetTextColor(self, color)
        if crColor == CLR_INVALID:
            raise WinException()
        return crColor
    
    def set_bk_color(self, color: int) -> int:
        crColor = SetBkColor(self, color)
        if crColor == CLR_INVALID:
            raise WinException()
        return crColor
    
    def set_bk_mode(self, mode: int) -> int:
        dwPrevMode = SetBkMode(self, mode)
        if dwPrevMode == 0:
            raise WinException()
        return dwPrevMode
    
    def bit_blt(self, dstX: int, dstY: int, srcX: int, srcY: int, 
                width: int, height: int, srcHdc: int | HDC, rop: int):
        if not BitBlt(self, dstX, dstY, width, height, srcHdc, srcX, srcY, rop):
            raise WinException()
    
    def pat_blt(self, x: int, y: int, width: int, height: int, rop: int):
        if not PatBlt(self, x, y, width, height, rop):
            raise WinException()
    
    def ellipse(self, rcEllps: RECT):
        if not Ellipse(self, rcEllps.left, rcEllps.top, rcEllps.right, rcEllps.bottom):
            raise WinException()
        
    def fill(self, rect: RECT, hbr: int | HANDLE):
        if not FillRect(self, byref(rect), hbr):
            raise WinException()
        
    def invert_rect(self, rect: RECT):
        if not InvertRect(self, byref(rect)):
            raise WinException()
        
    def get_text_extent_point(self, text: str) -> SIZE:
        sizeText = SIZE()
        buf = create_unicode_buffer(text)
        GetTextExtentPointW(self, buf, len(text), byref(sizeText))
        return sizeText
    
    def draw_icon(self, x: int, y: int, width: int, height: int,
                  icon: int | HANDLE, step: int = 0, 
                  flicker_free_draw: int | HANDLE = NULL,
                  flags: int = DI_NORMAL):
        if not DrawIconEx(self, x, y, icon, width, height, step, flicker_free_draw, flags):
            raise WinException()
    
class Pen(GDIObjectHandle):
    def __init__(self, style: int, width: int, color: int):
        super().__init__()
        self.value = CreatePen(style, width, color)
        if not self.value:
            raise WinException()
        
class Brush(GDIObjectHandle):
    def __init__(self, color: int, hatch: int = None):
        super().__init__()
        if hatch is None:
            self.value = CreateSolidBrush(color)
        else:
            self.value = CreateHatchBrush(color, hatch)
        if not self.value:
            raise WinException()
        
class PatternBrush(GDIObjectHandle):
    def __init__(self, hbm: int | HANDLE):
        super().__init__()
        self.value = CreatePatternBrush(hbm)
        if not self.value:
            raise WinException()
    
class Font(GDIObjectHandle):
    def __init__(self, name: str, height: int, width: int, 
                 escapement: int = 0, orientation: int = 0,
                 weight: int = FW_DONTCARE, italic: bool = False,
                 underline: bool = False, strike_out: bool = False,
                 charset: int = DEFAULT_CHARSET, 
                 out_precision: int = OUT_DEFAULT_PRECIS,
                 clip_precision: int = CLIP_DEFAULT_PRECIS,
                 quality: int = DEFAULT_QUALITY, 
                 pitch_and_family: int = DEFAULT_PITCH | FF_DONTCARE):
        super().__init__()
        self.value = CreateFontW(height, width, escapement,
                                 orientation, weight, italic,
                                 underline, strike_out, charset,
                                 out_precision, clip_precision,
                                 quality, pitch_and_family, name)
        if not self.value:
            raise WinException()

class IconInfo(ICONINFO):
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
        
class Bitmap(GDIObjectHandle):
    def __init__(self, width: int, height: int, planes: int = 1, bit_count: int = 32, bits = NULL):
        super().__init__()
        self.value = CreateBitmap(width, height, planes, bit_count, bits)
    
    @classmethod
    def from_icon(self, icon: int | HANDLE) -> 'Bitmap':
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
    _ps: PAINTSTRUCT
    _hwnd: int | HWND
    
    def __init__(self, hwnd: int | HWND):
        super().__init__()
        self._ps = PAINTSTRUCT()
        self._hwnd = hwnd
        self.value = BeginPaint(hwnd, self._ps.ref())
        if not self.value:
            raise WinException()
        
    def close(self):
        if not EndPaint(self._hwnd, self._ps.ref()):
            raise WinException()
        self._closed = True

class GLContext(Handle):
    _current: bool
    
    def __init__(self, *args):
        super().__init__(*args)
        self._current = False
    
    @classmethod
    def current(self, hDC: int | HANDLE) -> 'GLContext':
        hGLCtx = wglCreateContext(hDC)
        if not hGLCtx:
            raise WinException()
        glCtx = GLContext(hGLCtx)
        if not wglMakeCurrent(hDC, hGLCtx):
            raise WinException()
        glCtx._current = True
        return glCtx
    
    def close(self):
        if self._current:
            wglMakeCurrent(NULL, NULL)
        wglDeleteContext(self)
        self._closed = True