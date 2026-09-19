from win.wingdi import *
from win.winuser import *
from typing import TypeVar
from typing_extensions import Self
from .geom import *

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
        
        @classmethod
        @interface_abstract_method
        def length(cls) -> int: ...
        
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
            return self.__class__(self.value + value)
        
        def __sub__(self, value):
            return self.__class__(self.value - value)
        
        def __mul__(self, value):
            return self.__class__(self.value * value)
        
        def __truediv__(self, value):
            return self.__class__(self.value / value)
        
        def __floordiv__(self, value):
            return self.__class__(self.value // value)
        
        def __lshift__(self, value):
            return self.__class__(self.value << value)
        
        def __rshift__(self, value):
            return self.__class__(self.value >> value)
        
        def __or__(self, value):
            return self.__class__(self.value | value)
        
        def __and__(self, value):
            return self.__class__(self.value & value)
        
        def __inv__(self):
            return self.__class__(~self.value)
        
        def __neg__(self):
            return self.__class__(-self.value)
        
        def __pos__(self):
            return self.__class__(+self.value)
        
        def __eq__(self, other: 'Color.IColor') -> bool:
            return self.value == other.value
        
        def __ne__(self, other: 'Color.IColor') -> bool:
            return self.value != other.value
        
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
            return Color.HSL(hue, saturation, luminance)
        
        def copy(self) -> Self:
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
        def string(cls, color: str) -> Self:
            color = color.lstrip('#')
            components = []
            i = 0
            while i < len(color):
                components.append(int(color[i:i+2], 16))
                i += 2
            return cls.color(*components)
        
        def invert(self) -> 'Self':
            """
            Invert the color.
            """
            return self.__class__.color(*map(lambda x: (~x)&0xff, self))
        
        @classmethod
        def from_id(cls, id: int, table: type['Color.IColorTable'] | None = None) -> Self:
            if table is None:
                table = Color.Table
            return cls.color(*(tuple(table._color_(table.ensure()[id]).rgba())[0:cls.length()]))

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
            return Color.RGBA.color(self.r, self.g, self.b, self.a)
        
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
        def length(cls) -> int:
            return 3
        
        @classmethod
        def color(cls, r: int, g: int, b: int) -> 'Color.RGB':
            return cls((r << 8 | g) << 8 | b)
        
        @property
        def r(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 8 & 0xff
        
        @property
        def b(self) -> int:
            return self.value & 0xff
        
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
        def length(cls) -> int:
            return 4
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.RGBA':
            return cls(((r << 8 | g) << 8 | b) << 8 | a)
        
        @property
        def a(self) -> int: 
            return self.value & 0xff

        @property
        def r(self) -> int:
            return self.value >> 24 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def b(self) -> int:
            return self.value >> 8 & 0xff
        
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
        def length(cls) -> int:
            return 3
        
        @classmethod
        def color(cls, r: int, g: int, b: int) -> 'Color.BGR':
            return cls((b << 8 | g) << 8 | r)
        
        @property
        def b(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 8 & 0xff
        
        @property
        def r(self) -> int:
            return self.value & 0xff
        
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
        def length(cls) -> int:
            return 4
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.BGRA':
            return cls(((b << 8 | g) << 8 | r) << 8 | a)
        
        @property
        def b(self) -> int:
            return self.value >> 24 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def r(self) -> int:
            return self.value >> 8 & 0xff
        
        @property
        def a(self) -> int:
            return self.value & 0xff
        
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
        def length(cls) -> int:
            return 4
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.ARGB':
            return cls(((a << 8 | r) << 8 | g) << 8 | b)
        
        @property
        def a(self) -> int:
            return self.value >> 24 & 0xff
        
        @property
        def r(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 8 & 0xff
        
        @property
        def b(self) -> int:
            return self.value & 0xff
        
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
        def length(cls) -> int:
            return 4
        
        @classmethod
        def color(cls, r: int, g: int, b: int, a: int) -> 'Color.ABGR':
            return cls(((a << 8 | b) << 8 | g) << 8 | r)
        
        @property
        def a(self) -> int:
            return self.value >> 24 & 0xff
        
        @property
        def b(self) -> int:
            return self.value >> 16 & 0xff
        
        @property
        def g(self) -> int:
            return self.value >> 8 & 0xff
        
        @property
        def r(self) -> int:
            return self.value & 0xff
        
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

    class ID:
        ActiveBorder = 1
        ActiveCaption = 2
        ActiveCaptionText = 3
        AppWorkspace = 4
        Control = 5
        ControlDark = 6
        ControlDarkDark = 7
        ControlLight = 8
        ControlLightLight = 9
        ControlText = 10
        Desktop = 11
        GrayText = 12
        Highlight = 13
        HighlightText = 14
        HotTrack = 15
        InactiveBorder = 16
        InactiveCaption = 17
        InactiveCaptionText = 18
        Info = 19
        InfoText = 20
        Menu = 21
        MenuText = 22
        ScrollBar = 23
        Window = 24
        WindowFrame = 25
        WindowText = 26
        Transparent = 27
        AliceBlue = 28
        AntiqueWhite = 29
        Aqua = 30
        Aquamarine = 31
        Azure = 32
        Beige = 33
        Bisque = 34
        Black = 35
        BlanchedAlmond = 36
        Blue = 37
        BlueViolet = 38
        Brown = 39
        BurlyWood = 40
        CadetBlue = 41
        Chartreuse = 42
        Chocolate = 43
        Coral = 44
        CornflowerBlue = 45
        Cornsilk = 46
        Crimson = 47
        Cyan = 48
        DarkBlue = 49
        DarkCyan = 50
        DarkGoldenrod = 51
        DarkGray = 52
        DarkGreen = 53
        DarkKhaki = 54
        DarkMagenta = 55
        DarkOliveGreen = 56
        DarkOrange = 57
        DarkOrchid = 58
        DarkRed = 59
        DarkSalmon = 60
        DarkSeaGreen = 61
        DarkSlateBlue = 62
        DarkSlateGray = 63
        DarkTurquoise = 64
        DarkViolet = 65
        DeepPink = 66
        DeepSkyBlue = 67
        DimGray = 68
        DodgerBlue = 69
        Firebrick = 70
        FloralWhite = 71
        ForestGreen = 72
        Fuchsia = 73
        Gainsboro = 74
        GhostWhite = 75
        Gold = 76
        Goldenrod = 77
        Gray = 78
        Green = 79
        GreenYellow = 80
        Honeydew = 81
        HotPink = 82
        IndianRed = 83
        Indigo = 84
        Ivory = 85
        Khaki = 86
        Lavender = 87
        LavenderBlush = 88
        LawnGreen = 89
        LemonChiffon = 90
        LightBlue = 91
        LightCoral = 92
        LightCyan = 93
        LightGoldenrodYellow = 94
        LightGray = 95
        LightGreen = 96
        LightPink = 97
        LightSalmon = 98
        LightSeaGreen = 99
        LightSkyBlue = 100
        LightSlateGray = 101
        LightSteelBlue = 102
        LightYellow = 103
        Lime = 104
        LimeGreen = 105
        Linen = 106
        Magenta = 107
        Maroon = 108
        MediumAquamarine = 109
        MediumBlue = 110
        MediumOrchid = 111
        MediumPurple = 112
        MediumSeaGreen = 113
        MediumSlateBlue = 114
        MediumSpringGreen = 115
        MediumTurquoise = 116
        MediumVioletRed = 117
        MidnightBlue = 118
        MintCream = 119
        MistyRose = 120
        Moccasin = 121
        NavajoWhite = 122
        Navy = 123
        OldLace = 124
        Olive = 125
        OliveDrab = 126
        Orange = 127
        OrangeRed = 128
        Orchid = 129
        PaleGoldenrod = 130
        PaleGreen = 131
        PaleTurquoise = 132
        PaleVioletRed = 133
        PapayaWhip = 134
        PeachPuff = 135
        Peru = 136
        Pink = 137
        Plum = 138
        PowderBlue = 139
        Purple = 140
        Red = 141
        RosyBrown = 142
        RoyalBlue = 143
        SaddleBrown = 144
        Salmon = 145
        SandyBrown = 146
        SeaGreen = 147
        SeaShell = 148
        Sienna = 149
        Silver = 150
        SkyBlue = 151
        SlateBlue = 152
        SlateGray = 153
        Snow = 154
        SpringGreen = 155
        SteelBlue = 156
        Tan = 157
        Teal = 158
        Thistle = 159
        Tomato = 160
        Turquoise = 161
        Violet = 162
        Wheat = 163
        White = 164
        WhiteSmoke = 165
        Yellow = 166
        YellowGreen = 167
        ButtonFace = 168
        ButtonHighlight = 169
        ButtonShadow = 170
        GradientActiveCaption = 171
        GradientInactiveCaption = 172
        MenuBar = 173
        MenuHighlight = 174
    
    class IColorTable:
        _color_: type['Color.IColor']
        
        @staticmethod
        def ensure() -> list[int]:
            """
            Get the color table list.
            """
    
    class Table(IColorTable):
        array: list[int] | None = None
        
        @staticmethod
        def ensure() -> list[int]:
            if Color.Table.array is None:
                Color.Table.array = array = [0] * 175
                array[1] = int(Color.system(COLOR_ACTIVEBORDER).argb())
                array[2] = int(Color.system(COLOR_ACTIVECAPTION).argb())
                array[3] = int(Color.system(COLOR_CAPTIONTEXT).argb())
                array[4] = int(Color.system(COLOR_APPWORKSPACE).argb())
                array[168] = int(Color.system(COLOR_BTNFACE).argb())
                array[169] = int(Color.system(COLOR_BTNHILIGHT).argb())
                array[170] = int(Color.system(COLOR_BTNSHADOW).argb())
                array[5] = int(Color.system(COLOR_BTNFACE).argb())
                array[6] = int(Color.system(COLOR_BTNHILIGHT).argb())
                array[7] = int(Color.system(COLOR_3DDKSHADOW).argb())
                array[8] = int(Color.system(COLOR_3DLIGHT).argb())
                array[9] = int(Color.system(COLOR_BTNHILIGHT).argb())
                array[10] = int(Color.system(COLOR_BTNTEXT).argb())
                array[11] = int(Color.system(COLOR_BACKGROUND).argb())
                array[171] = int(Color.system(COLOR_GRADIENTACTIVECAPTION).argb())
                array[172] = int(Color.system(COLOR_GRADIENTINACTIVECAPTION).argb())
                array[12] = int(Color.system(COLOR_GRAYTEXT).argb())
                array[13] = int(Color.system(COLOR_HIGHLIGHT).argb())
                array[14] = int(Color.system(COLOR_HIGHLIGHTTEXT).argb())
                array[15] = int(Color.system(COLOR_HOTLIGHT).argb())
                array[16] = int(Color.system(COLOR_INACTIVEBORDER).argb())
                array[17] = int(Color.system(COLOR_INACTIVECAPTION).argb())
                array[18] = int(Color.system(COLOR_INACTIVECAPTIONTEXT).argb())
                array[19] = int(Color.system(COLOR_INFOBK).argb())
                array[20] = int(Color.system(COLOR_INFOTEXT).argb())
                array[21] = int(Color.system(COLOR_MENU).argb())
                array[173] = int(Color.system(COLOR_MENUBAR).argb())
                array[174] = int(Color.system(COLOR_MENUHILIGHT).argb())
                array[22] = int(Color.system(COLOR_MENUTEXT).argb())
                array[23] = int(Color.system(COLOR_SCROLLBAR).argb())
                array[24] = int(Color.system(COLOR_WINDOW).argb())
                array[25] = int(Color.system(COLOR_WINDOWFRAME).argb())
                array[26] = int(Color.system(COLOR_WINDOWTEXT).argb())
                array[27] = 16777215
                array[28] = -984833
                array[29] = -332841
                array[30] = -16711681
                array[31] = -8388652
                array[32] = -983041
                array[33] = -657956
                array[34] = -6972
                array[35] = -16777216
                array[36] = -5171
                array[37] = -16776961
                array[38] = -7722014
                array[39] = -5952982
                array[40] = -2180985
                array[41] = -10510688
                array[42] = -8388864
                array[43] = -2987746
                array[44] = -32944
                array[45] = -10185235
                array[46] = -1828
                array[47] = -2354116
                array[48] = -16711681
                array[49] = -16777077
                array[50] = -16741493
                array[51] = -4684277
                array[52] = -5658199
                array[53] = -16751616
                array[54] = -4343957
                array[55] = -7667573
                array[56] = -11179217
                array[57] = -29696
                array[58] = -6737204
                array[59] = -7667712
                array[60] = -1468806
                array[61] = -7357301
                array[62] = -12042869
                array[63] = -13676721
                array[64] = -16724271
                array[65] = -7077677
                array[66] = -60269
                array[67] = -16728065
                array[68] = -9868951
                array[69] = -14774017
                array[70] = -5103070
                array[71] = -1296
                array[72] = -14513374
                array[73] = -65281
                array[74] = -2302756
                array[75] = -460545
                array[76] = -10496
                array[77] = -2448096
                array[78] = -8355712
                array[79] = -16744448
                array[80] = -5374161
                array[81] = -983056
                array[82] = -38476
                array[83] = -3318692
                array[84] = -11861886
                array[85] = -16
                array[86] = -989556
                array[87] = -1644806
                array[88] = -3851
                array[89] = -8586240
                array[90] = -1331
                array[91] = -5383962
                array[92] = -1015680
                array[93] = -2031617
                array[94] = -329006
                array[95] = -2894893
                array[96] = -7278960
                array[97] = -18751
                array[98] = -24454
                array[99] = -14634326
                array[100] = -7876870
                array[101] = -8943463
                array[102] = -5192482
                array[103] = -32
                array[104] = -16711936
                array[105] = -13447886
                array[106] = -331546
                array[107] = -65281
                array[108] = -8388608
                array[109] = -10039894
                array[110] = -16777011
                array[111] = -4565549
                array[112] = -7114533
                array[113] = -12799119
                array[114] = -8689426
                array[115] = -16713062
                array[116] = -12004916
                array[117] = -3730043
                array[118] = -15132304
                array[119] = -655366
                array[120] = -6943
                array[121] = -6987
                array[122] = -8531
                array[123] = -16777088
                array[124] = -133658
                array[125] = -8355840
                array[126] = -9728477
                array[127] = -23296
                array[128] = -47872
                array[129] = -2461482
                array[130] = -1120086
                array[131] = -6751336
                array[132] = -5247250
                array[133] = -2396013
                array[134] = -4139
                array[135] = -9543
                array[136] = -3308225
                array[137] = -16181
                array[138] = -2252579
                array[139] = -5185306
                array[140] = -8388480
                array[141] = -65536
                array[142] = -4419697
                array[143] = -12490271
                array[144] = -7650029
                array[145] = -360334
                array[146] = -744352
                array[147] = -13726889
                array[148] = -2578
                array[149] = -6270419
                array[150] = -4144960
                array[151] = -7876885
                array[152] = -9807155
                array[153] = -9404272
                array[154] = -1286
                array[155] = -16711809
                array[156] = -12156236
                array[157] = -2968436
                array[158] = -16744320
                array[159] = -2572328
                array[160] = -40121
                array[161] = -12525360
                array[162] = -1146130
                array[163] = -663885
                array[164] = -1
                array[165] = -657931
                array[166] = -256
                array[167] = -6632142
            return Color.Table.array
        
    Table._color_ = ARGB
        
WT_COLOR = TypeVar('WT_COLOR', bound=Color.IColor)
WT_COLORALPHA = TypeVar('WT_COLORALPHA', bound=Color.IColorAlpha)