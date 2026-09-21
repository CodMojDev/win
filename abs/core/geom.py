from win.winuser import *
from typing import TypeAlias, SupportsInt, Iterable, ClassVar
from win.wingdi import *
    
class Point(POINT, CStructure):
    EMPTY: ClassVar['Point']
    
    def __str__(self):
        return f'{{{self.x}, {self.y}}}'
    
    def __repr__(self) -> str:
        return f'<Point {self}>'
        
    def __iter__(self) -> defb_t.Iterator:
        return iter((self.x, self.y))
    
    def __neg__(self) -> 'Point':
        return Point(-self.x, -self.y)
    
    def __sub__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar subtract
            return Point(self.x - round(V), self.y - round(V))
        # otherwise point subtract
        V = GraphicUtils.point(V)
        return Point(self.x - V.x, self.y - V.y)
    
    def __add__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar add
            return Point(self.x + round(V), self.y + round(V))
        # otherwise point add
        V = GraphicUtils.point(V)
        return Point(self.x + V.x, self.y + V.y)
    
    def __isub__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar subtract
            self.x -= round(V)
            self.y -= round(V)
            return self
        # otherwise point subtract
        V = GraphicUtils.point(V)
        self.x -= V.x
        self.y -= V.y
        return self
    
    def __iadd__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar add
            self.x += round(V)
            self.y += round(V)
            return self
        # otherwise point add
        V = GraphicUtils.point(V)
        self.x += V.x
        self.y += V.y
        return self
    
    def __imul__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar add
            self.x *= round(V)
            self.y *= round(V)
            return self
        # otherwise point add
        V = GraphicUtils.point(V)
        self.x *= V.x
        self.y *= V.y
        return self
    
    def __mul__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar multiply
            return Point(round(self.x * V), round(self.y * V))
        # otherwise point multiply
        V = GraphicUtils.point(V)
        return Point(self.x * V.x, self.y * V.y)
    
    def __floordiv__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar floor division
            return Point(self.x // round(V), self.y // round(V))
        # otherwise point floor division
        V = GraphicUtils.point(V)
        return Point(self.x // V.x, self.y // V.y)
    
    def __truediv__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar add
            return Point(round(self.x / V), round(self.y / V))
        # otherwise point add
        V = GraphicUtils.point(V)
        return Point(round(self.x / V.x), round(self.y / V.y))
    
    def __itruediv__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar true division
            self.x = round(self.x / V)
            self.y += round(self.x / V)
            return self
        # otherwise point true division
        V = GraphicUtils.point(V)
        self.x = round(self.x / V.x)
        self.y = round(self.x / V.y)
        return self
    
    def __ifloordiv__(self, V) -> 'Point':
        if isinstance(V, (int, float)): # scalar floor division
            self.x //= round(V)
            self.y //= round(V)
            return self
        # otherwise point floor division
        V = GraphicUtils.point(V)
        self.x //= V.x
        self.y //= V.y
        return self
    
    def __eq__(self, V: 'GraphicUtils.Point') -> bool:
        V = GraphicUtils.point(V)
        return self.x == V.x and self.y == V.y
    
    def __ne__(self, V: 'GraphicUtils.Point') -> bool:
        V = GraphicUtils.point(V)
        return self.x != V.x or self.y != V.y
    
    def __bool__(self) -> bool:
        return self.x and self.y

Point.EMPTY = Point()

class Size(SIZE, CStructure):
    EMPTY: ClassVar['Size']
    
    def __str__(self):
        return f'{{{self.cx}, {self.cy}}}'
    
    def __repr__(self) -> str:
        return f'<Size {self}>'
    
    @property
    def width(self) -> int:
        return self.cx
    
    @width.setter
    def width(self, width: int):
        self.cx = width
    
    @property
    def height(self) -> int:
        return self.cy
    
    @height.setter
    def height(self, height: int):
        self.cy = height
        
    def __iter__(self) -> defb_t.Iterator:
        return iter((self.cx, self.cy))
    
    def __neg__(self) -> 'Size':
        return Size(-self.cx, -self.cy)
    
    def __sub__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar subtract
            return Size(self.cx - round(V), self.cy - round(V))
        # otherwise size subtract
        V = GraphicUtils.size(V)
        return Size(self.cx - V.cx, self.cy - V.cy)
    
    def __add__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar add
            return Size(self.cx + round(V), self.cy + round(V))
        # otherwise size add
        V = GraphicUtils.size(V)
        return Size(self.cx + V.cx, self.cy + V.cy)
    
    def __isub__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar subtract
            self.cx -= round(V)
            self.cy -= round(V)
            return self
        # otherwise size subtract
        V = GraphicUtils.size(V)
        self.cx -= V.cx
        self.cy -= V.cy
        return self
    
    def __iadd__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar add
            self.cx += round(V)
            self.cy += round(V)
            return self
        # otherwise size add
        V = GraphicUtils.size(V)
        self.cx += V.cx
        self.cy += V.cy
        return self
    
    def __imul__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar add
            self.cx *= round(V)
            self.cy *= round(V)
            return self
        # otherwise size add
        V = GraphicUtils.size(V)
        self.cx *= V.cx
        self.cy *= V.cy
        return self
    
    def __mul__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar multiply
            return Size(round(self.cx * V), round(self.cy * V))
        # otherwise size multiply
        V = GraphicUtils.size(V)
        return Size(self.cx * V.cx, self.cy * V.cy)
    
    def __floordiv__(self, V) -> 'SIze':
        if isinstance(V, (int, float)): # scalar floor division
            return Size(self.cx // round(V), self.cy // round(V))
        # otherwise size floor division
        V = GraphicUtils.size(V)
        return Size(self.cx // V.cx, self.cy // V.cy)
    
    def __truediv__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar add
            return Size(round(self.cx / V), round(self.cy / V))
        # otherwise size add
        V = GraphicUtils.size(V)
        return Size(round(self.cx / V.cx), round(self.cy / V.cy))
    
    def __itruediv__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar true division
            self.cx = round(self.cx / V)
            self.cy += round(self.cx / V)
            return self
        # otherwise size true division
        V = GraphicUtils.size(V)
        self.cx = round(self.cx / V.x)
        self.cy = round(self.cx / V.y)
        return self
    
    def __ifloordiv__(self, V) -> 'Size':
        if isinstance(V, (int, float)): # scalar floor division
            self.cx //= round(V)
            self.cy //= round(V)
            return self
        # otherwise size floor division
        V = GraphicUtils.point(V)
        self.cx //= V.cx
        self.cy //= V.cy
        return self
    
    def __eq__(self, V: 'GraphicUtils.Size') -> bool:
        V = GraphicUtils.size(V)
        return self.cx == V.cx and self.cy == V.cy
    
    def __ne__(self, V: 'GraphicUtils.Size') -> bool:
        V = GraphicUtils.size(V)
        return self.cx != V.cx or self.cy != V.cy
    
    def __bool__(self) -> bool:
        return self.cx and self.cy

Size.EMPTY = Size()

class Rect(RECT, CStructure):
    """
    Rectangle.
    """
    EMPTY: ClassVar['Rect']
    
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
        
    def union(self, rect: 'Rect'):
        """
        Union with the rect.
        """
        UnionRect(byref(self), byref(self), byref(rect))
    
    def __contains__(self, pt: 'GraphicUtils.Point') -> bool:
        pt = GraphicUtils.point(pt)
        return PtInRect(byref(self), pt)
    
    def __str__(self) -> str:
        return f'{{{{{self.left}, {self.top}}}, {{{self.right}, {self.bottom}}}}}'
    
    def __repr__(self) -> str:
        return f'<RECT {self}>'
    
    @property
    def x(self) -> int:
        return self.left
    
    @x.setter
    def x(self, x: int):
        width = self.width
        self.left = x
        self.width = width
    
    @property
    def y(self) -> int:
        return self.top
    
    @y.setter
    def y(self, y: int):
        height = self.height
        self.top = y
        self.height = height
        
    def intersect(self, rc: RECT) -> bool:
        """
        Intersect the rectangle.
        """
        return IntersectRect(self.ref(), self.ref(), rc.ref()) != FALSE
        
    def offset(self, x: int, y: int):
        """
        Offset the rectangle.
        """
        OffsetRect(self.ref(), x, y)
        
    def split(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Split the rectangle to left,top and right,bottom points.
        """
        return (self.left, self.top), (self.right, self.bottom)
    
    @classmethod
    def build(cls, left_top: 'GraphicUtils.Point', right_bottom: 'GraphicUtils.Point') -> 'Rect':
        """
        Build the rectangle from left,top and right, bottom
        """
        left_top = GraphicUtils.point(left_top)
        right_bottom = GraphicUtils.point(right_bottom)
        return cls(left_top.x, left_top.y, right_bottom.x, right_bottom.y)
    
    def __neg__(self) -> 'Rect':
        return Rect(-self.left, -self.top, -self.right, -self.bottom)
    
    def __iter__(self) -> defb_t.Iterator:
        return iter((self.left, self.top, self.right, self.bottom))
    
    def __eq__(self, V: 'Rect') -> bool:
        return self.left == V.left and self.top == V.top and self.right == V.right and self.bottom == V.bottom
    
    def __ne__(self, V: 'Rect') -> bool:
        return self.left != V.left or self.top != V.top or self.right != V.right or self.bottom != V.bottom
    
    def __bool__(self) -> bool:
        return self.left and self.top and self.right and self.bottom

    def relative(self) -> 'Rect':
        return Rect.create(0, 0, self.width, self.height)
    
    @property
    def rect_size(self) -> tuple[int, int]:
        return self.width, self.height
    
    @rect_size.setter
    def rect_size(self, size: 'GraphicUtils.Size'):
        self.width, self.height = GraphicUtils.size_tuple(size)

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y
    
    @position.setter
    def position(self, position: 'GraphicUtils.Point'):
        self.x, self.y = GraphicUtils.point_tuple(position)

Rect.EMPTY = Rect()

class MARGINS(CStructure):
    _fields_ = [
        ('cxLeftWidth', INT),
        ('cxRightWidth', INT),
        ('cyTopHeight', INT),
        ('cyBottomHeight', INT)
    ]
    cxLeftWidth: int
    cxRightWidth: int
    cyTopHeight: int
    cyBottomHeight: int
    
PMARGINS = LPMARGINS = PTR(MARGINS)
    
class Margins(MARGINS):
    def __str__(self) -> str:
        return f'{{{{{self.cxLeftWidth},{self.cxRightWidth}}},{{{self.cyTopHeight},{self.cyBottomHeight}}}}}'

    def __repr__(self) -> str:
        return f'<MARGINS {self}>'
    
    @property
    def left(self) -> int:
        return self.cxLeftWidth
    
    @left.setter
    def left(self, left: int):
        self.cxLeftWidth = left
    
    @property
    def right(self) -> int:
        return self.cxRightWidth
    
    @right.setter
    def right(self, right: int):
        self.cxRightWidth = right
    
    @property
    def top(self) -> int:
        return self.cyTopHeight
    
    @top.setter
    def top(self, top: int):
        self.cyTopHeight = top
    
    @property
    def bottom(self) -> int:
        return self.cyBottomHeight
    
    @bottom.setter
    def bottom(self, bottom: int):
        self.cyBottomHeight = bottom

class GraphicUtils:
    Point: TypeAlias = POINT | tuple[SupportsInt, SupportsInt]
    Size: TypeAlias = SIZE | tuple[SupportsInt, SupportsInt]
    PointArray: TypeAlias = Iterable[Point]
    
    @staticmethod
    def linear(x: int, y: int, rcSource: RECT, rcTarget: RECT) -> tuple[int, int]:
        """
        Linear expansion of (x, y) by source and target rectangles.
        """
        
        x = rcTarget.left + (x - rcSource.left) * (rcTarget.right - rcTarget.left) / (rcSource.right - rcSource.left)
        y = rcTarget.top + (y - rcSource.top) * (rcTarget.bottom - rcTarget.top) / (rcSource.bottom - rcSource.top)
        return int(x), int(y)
    
    @staticmethod
    def center(x: int, y: int, rcSource: RECT, rcTarget: RECT) -> tuple[int, int]:
        """
        Center expansion of (x, y) by source and target rectangles.
        """
        
        x = x + ((rcTarget.left + rcTarget.right) / 2 - (rcSource.left + rcSource.right) / 2)
        y = y + ((rcTarget.top + rcTarget.bottom) / 2 - (rcSource.top + rcSource.bottom) / 2)
        return int(x), int(y)
    
    @staticmethod
    def size_rect(rcSource: RECT, rcTarget: RECT) -> Rect:
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
        return Rect(int(left), int(top), int(right), int(bottom))
    
    @staticmethod
    def in_rect(x: int, y: int, rc: RECT) -> bool:
        """
        Check point in rectangle.
        """
        
        return bool(PtInRect(byref(rc), POINT(x, y)))
    
    class Vertex(TRIVERTEX):
        def __init__(self, x: int, y: int, red: int, green: int, blue: int, alpha: int = 255):
            red <<= 8
            green <<= 8
            blue <<= 8
            alpha <<= 8
            
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
    def size(size: 'GraphicUtils.Size') -> Size:
        """
        Convert SIZE/tuple to SIZE structure.
        """
        
        if isinstance(size, SIZE):
            return i_cast_structure(size, Size)
        return Size(*size[0:2])
    
    @staticmethod
    def point_tuple(pt: 'GraphicUtils.Point') -> tuple[int, int]:
        """
        Convert POINT/tuple to (x, y) tuple.
        """
        
        if isinstance(pt, POINT):
            return (pt.x, pt.y)
        return pt[0:2]
    
    @staticmethod
    def point(pt: 'GraphicUtils.Point') -> Point:
        """
        Convert POINT/tuple to POINT structure.
        """
        
        if isinstance(pt, POINT):
            return i_cast_structure(pt, Point)
        return Point(*pt[0:2])
            
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