from .color import *
from .handle import *

class PixelBufferMeta(type):
    _generic_cache_ = {}
    
    def __getitem__(cls, color: type[WT_COLOR]) -> 'PixelBuffer[WT_COLOR]':
        pixelbuffer_t = cls._generic_cache_.get(color, None)
        if pixelbuffer_t is None:
            class pixelbuffer_t(PixelBuffer):
                T = color
        return pixelbuffer_t
        
class PixelBuffer(Generic[WT_COLOR], metaclass=PixelBufferMeta):
    T: ClassVar[type[WT_COLOR]]
    
    class PxBufferLine(Generic[WT_COLOR]):
        buffer: 'PixelBuffer[WT_COLOR]'
        x: int
        def __init__(self, x: int, buffer: 'PixelBuffer'):
            self.x = x
            self.buffer = buffer
            
        def __getitem__(self, y: int) -> 'WT_COLOR':
            return self.buffer.T(self.buffer.get(self.x, y))
        
        def __setitem__(self, y: int, color: WT_COLOR | int):
            self.buffer.set(self.x, y, int(color))
    
    def __init__(self, width: int, height: int, allocator: IAllocator = CLocalAllocator()):
        self.buffer = allocator.allocate(width * height * self.T.length())
        self.color_size = self.T.length()
        self.allocator = allocator
        self.width = width
        self.height = height
        self.info = BitmapInfo(self.width, self.height, self.color_size<<3)
    
    def __getitem__(self, x: int) -> PxBufferLine[WT_COLOR]:
        return self.T(PixelBuffer.PxBufferLine(x, self))   
     
    def get(self, x: int, y: int) -> int:
        return int.from_bytes(bytes(i_cast(self.buffer+((x+y*self.width)*self.color_size), PTR(BYTE * self.color_size)).contents), 'little')
    
    def set(self, x: int, y: int, color: int):
        self.allocator.copy(self.buffer+((x+y*self.width)*self.color_size), int.to_bytes(color, self.color_size, 'little'), self.color_size)
        
    def map(self, dc: DC, x: int, y: int, width: int, height: int):
        dc.stretch_di_bits(x, y, 0, 0, width, height, self.width, self.height, self.buffer, self.info)