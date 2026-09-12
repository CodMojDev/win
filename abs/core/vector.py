from win.defbase_allocator import *

class ArrayVector(Generic[WTCT]):
    allocator: IAllocator
    vector_type: type[WTCT]
    
    base: WT_ADDRLIKE
    capacity: int
    used: int
    
    def __init__(self, allocator: IAllocator, vector_type: type[WTCT]):
        self.allocator = allocator
        self.vector_type = vector_type
        
        self.base = NULL
        self.capacity = 0
        self.used = 0
        
    def reserve(self, capacity: int):
        print(capacity != 0, capacity <= self.capacity, capacity, self.capacity)
        if capacity != 0 and capacity <= self.capacity: return
        if self.base: 
            self.allocator.deallocate(self.base)
        self.base = self.allocator.allocate(capacity*sizeof(self.vector_type))
        self.capacity = capacity
        
    def destroy(self):
        if self.base:
            self.allocator.deallocate(self.base)
            self.base = NULL
            
    def __getitem__(self, index: int) -> WTCT:
        return i_cast(self.base+index*sizeof(self.vector_type), PTR(self.vector_type)).contents
    
    def __setitem__(self, index: int, value: WTCT):
        i_cast(self.base+index*sizeof(self.vector_type), PTR(self.vector_type)).contents = value
        
    def append(self, value: WTCT):
        if self.used >= self.capacity:
            if self.capacity == 0:
                self.reserve(2)
            else:
                self.reserve(self.capacity + self.capacity//2)
        self[self.used] = value
        self.used += 1
        
    def __del__(self):
        self.destroy()