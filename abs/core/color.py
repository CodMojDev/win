from win.wingdi import *
from win.winuser import *

class Color:
    @classmethod
    def system(cls, index: int) -> 'Color.BGR':
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
        
        def copy(self) -> 'Color.IColor':
            return self.__class__(self.value)
        
        @property
        def brightness(self) -> float:
            r = self.r / 255.0
            g = self.g / 255.0
            b = self.b / 255.0
            x = y = r
            
            if g > x:
                x = g
            if b > x:
                x = b
            if g < y:
                y = g
            if b < y:
                y = b
            
            return (x + y) / 2.0
        
        @classmethod
        def string(cls, color: str) -> 'Color.IColor':
            color = color.lstrip('#')
            components = []
            i = 0
            while i < len(color):
                components.append(int(color[i:i+2], 16))
                i += 2
            return cls.color(*components)

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
        
        def rgb(self) -> 'Color.RGB':
            return self

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
        
        def rgba(self) -> 'Color.RGBA':
            return self
        
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
        
        def bgr(self) -> 'Color.BGR':
            return self
        
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
        
        def argb(self) -> 'Color.ARGB':
            return self
        
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
        
        def abgr(self) -> 'Color.ABGR':
            return self
        
    class HSL:
        """
        HSL Representation of color.
        """
        
        @classmethod
        def color(cls, r: int, g: int, b: int) -> 'Color.HSL':
            return Color.RGB.color(r, g, b).hsl()
        
        @classmethod
        def from_hsl(cls, h: float, s: float, l: float):
            return cls(h / 360, s / 100, l / 100)
        
        def __init__(self, hue: float = 0.0, saturation: float = 0.0, luminance: float = 0.0):
            self.hue = hue
            self.saturation = saturation
            self.luminance = luminance
            
        @property
        def h(self) -> int:
            return round(self.hue * 360)
        
        @h.setter
        def h(self, h: int):
            self.hue = h / 360.0
        
        @property
        def s(self) -> int:
            return round(self.saturation * 100)
        
        @s.setter
        def s(self, s: int):
            self.saturation = s / 100.0
        
        @property
        def l(self) -> int:
            return round(self.luminance * 100)
        
        @l.setter
        def l(self, l: int):
            self.luminance = l / 100.0
            
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
        
        def hsl(self) -> 'Color.HSL':
            """
            Convert color into HSL.
            """
            return self
        
        def gl(self) -> 'Color.GLColor':
            """
            Convert color into OpenGL format (by HSL->RGBA->OpenGL conversion).
            """
            return Color.GLColor(self.rgba())
    
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
            
        def rgba(self) -> 'Color.RGBA':
            """
            Convert color into RGBA.
            """
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
        
        def __eq__(self, color: TUnion['Color.IColorAlpha', 'Color.GLColor']) -> bool:
            return self.value == color.gl().value