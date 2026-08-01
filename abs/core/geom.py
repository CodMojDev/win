from win.winuser import *
from typing import TypeAlias, SupportsInt, Iterable
from win.wingdi import *
    
class Point(POINT, CStructure):
    def __str__(self):
        return f'{{{self.x}, {self.y}}}'
    
    def __repr__(self) -> str:
        return f'<POINT {self}>'
    
class Size(SIZE, CStructure):
    def __str__(self):
        return f'{{{self.x}, {self.y}}}'
    
    def __repr__(self) -> str:
        return f'<SIZE {self}>'

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
        
    def intersect(self, rc: RECT):
        """
        Intersect the rectangle.
        """
        IntersectRect(self.ref(), self.ref(), rc.ref())
        
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
        return (self.left, self.top, self.right, self.bottom)

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