from .vcrt.vcruntime_string import *
from .ucrt.corecrt_malloc import *
from .defbase_process import *

class IAllocator(IInterface): 
    def __init__(self, *args): ...
    
    @interface_abstract_method
    def allocate(self, size: int, **kwargs) -> WT_ADDRLIKE: ...
    
    @interface_abstract_method
    def deallocate(self, address: WT_ADDRLIKE): ...
    
    @interface_abstract_method
    def copy(self, address: WT_ADDRLIKE, source: WT_ADDRLIKE, size: int): ...
        
class CLocalAllocator(IAllocator):
    def allocate(self, size: int, **kwargs) -> WT_ADDRLIKE:
        return malloc(size)
    
    def deallocate(self, address: WT_ADDRLIKE):
        free(address)
        
    def copy(self, address: WT_ADDRLIKE, source: WT_ADDRLIKE, size: int): 
        memcpy(address, source, size)
        
    def __repr__(self) -> str:
        return f'<allocator CLocalAllocator>'
    
class CVirtualAllocator(CLocalAllocator):
    def allocate(self, size: int, **kwargs) -> WT_ADDRLIKE:
        if 'flags' in kwargs:
            return VirtualAlloc(NULL, size, MEM_COMMIT, kwargs['flags'])
        return VirtualAlloc(NULL, size, MEM_COMMIT, PAGE_READWRITE)
    
    def deallocate(self, address: WT_ADDRLIKE):
        VirtualFree(address, 0, MEM_RELEASE)
        
    def __repr__(self) -> str:
        return f'<allocator CVirtualAllocator>'
        
class CRemoteAllocator(IAllocator):
    process: CProcess
    
    def __init__(self, process: CProcess):
        self.process = process
    
    def allocate(self, size: int, **kwargs) -> WT_ADDRLIKE:
        if 'flags' in kwargs:
            return VirtualAllocEx(self.process.handle, NULL, size, MEM_COMMIT, kwargs['flags'])
        return VirtualAllocEx(self.process.handle, NULL, size, MEM_COMMIT, PAGE_READWRITE)
        
    def deallocate(self, address: WT_ADDRLIKE):
        VirtualFreeEx(self.process.handle, address, 0, MEM_RELEASE)
        
    def copy(self, address: WT_ADDRLIKE, source: WT_ADDRLIKE, size: int): 
        self.process.write(address, source, size)
        
    def __repr__(self) -> str:
        return f'<allocator CRemoteAllocator process.pid={self.process.pid}>'
    
class PoolAllocation:
    address: int
    size: int
    
    def __init__(self, address: int, size: int):
        self.address = address
        self.size = size
    
class PoolAllocator(IAllocator):
    allocations: dict[int, PoolAllocation]
    free_blocks: list[tuple[int, int]]
    quota: int
    base: int
    
    def __init__(self, quota: int):
        self.quota = quota
        self.alloc_init()
        self.base = PtrUtil.get_address(self.base)
        
        self.free_blocks = [(self.base, self.base+quota)] # frontier
        self.allocations = {}
        
    @interface_abstract_method
    def alloc_init(self): ...
    
    @interface_abstract_method
    def alloc_init_resized(self, quota: int): ...
    
    @interface_abstract_method
    def delete(self): ...
        
    def __del__(self):
        if self.base:
            self.delete()
        
    def resize(self, quota: int):
        if quota == 0: # implicitly deallocate the pool
            self.delete()
            return
        
        if quota == self.quota: return
        
        if len(self.allocations) != 0:
            highest_address = max(self.allocations.keys())
            size = self.allocations[highest_address].size
            if self.base + quota < (highest_address + size):
                raise ValueError('Too small quota, at first deallocate the block '
                                 f'at address {format_hex(highest_address, 8)} ({size} bytes), '
                                 f'or set the quota minimally to {(highest_address + size) - self.base}.')
            
        old_quota = self.quota
        self.quota = quota
        self.alloc_init_resized(old_quota)

    def allocate_pool(self, size: int, **kwargs) -> PoolAllocation:
        return self.allocate(size, pool=True)

    def allocate(self, size: int, **kwargs) -> PoolAllocation | int:
        for i, (start, end) in enumerate(self.free_blocks):
            after_allocation = start + size
            
            if after_allocation <= end:
                if after_allocation == end:
                    del self.free_blocks[i] # block shrinked to 0 bytes, delete
                else:
                    self.free_blocks[i] = (after_allocation, end) # shrink block to (start+size, end)
                allocation = PoolAllocation(start, size)
                self.allocations[start] = allocation
                
                if 'pool' in kwargs:
                    return allocation
                else:
                    return start
            
        raise MemoryError(f'Exhausted pool quota ({self.quota} bytes) '
                          f'(Tried to allocate {size} bytes).')
        
    def deallocate(self, address: PoolAllocation | WT_ADDRLIKE):
        if isinstance(address, PoolAllocation):
            address = address.address
        address = PtrUtil.get_address(address)
        
        size = self.allocations[address].size
        address_end = address + size
        memset(address, 0, size) # clear the data
        allocation = self.allocations[address]
        # reset the allocation
        allocation.address = NULL
        allocation.size = 0
        del self.allocations[address]
        
        is_joined = False
        free_blocks = []
        
        for start, end in self.free_blocks: # avoid the redundant addresses fragmentation
            # join the blocks
            if is_joined: # if already joined the freed block, don't overhead
                free_blocks.append((start, end))
                continue
                
            if address_end == start: # (freed block)(other block)
                free_blocks.append((address, end))
                is_joined = True
            elif end == address: # (other block)(freed block)
                free_blocks.append((start, address_end))
                is_joined = True
            else:
                free_blocks.append((start, end))
        
        if not is_joined: # if not joinable, directly add the freed block
            free_blocks.append((address, address_end))
        
        self.free_blocks = free_blocks
        
class CLocalPoolAllocator(PoolAllocator, CLocalAllocator):        
    def alloc_init(self):
        self.base = malloc(self.quota)
        
    def alloc_init_resized(self, old_quota: int):
        old_base = self.base
        self.base = realloc(old_base, self.quota)
        
        if not PtrArithmetic.equals(self.base, old_base): # allocated the new base address, data already copied by realloc
            allocations = {}
            free_blocks = []
            
            for address, allocation in self.allocations.items(): # reconstruct the pool allocations list
                address -= (old_base - self.base) # arithmetically same as address = address - old_base + base, but optimized
                allocation.address = address
                allocations[address] = allocation
                
            for start, end in self.free_blocks: # reconstruct the free blocks list
                if end - old_base == old_quota: # frontier
                    end = self.base + self.quota
                else:
                    end = end - old_base + self.base
                start = start - old_base + self.base
                free_blocks.append((start, end))
                
            self.allocations = allocations
            self.free_blocks = free_blocks
        
    def delete(self):
        free(self.base)
        self.base = None
        
    def __repr__(self) -> str:
        return f'<allocator CLocalPoolAllocator, quota={self.quota}>'
    
class CVirtualPoolAllocator(CLocalPoolAllocator):
    flags: int
    
    def __init__(self, quota: int, flags: Optional[int] = None):
        if flags is None:
            flags = PAGE_READWRITE
            
        self.flags = flags
        super().__init__(quota)
        
    def alloc_init(self):
        self.base = VirtualAlloc(NULL, self.quota, 5, self.flags)
        
    def alloc_init_resized(self, old_quota: int):
        old_base = self.base
        self.alloc_init()
        quota_to_copy = min(self.quota, old_quota) # prevent garbage copying
        memcpy(self.base, old_base, quota_to_copy) # copy the old allocation data into new allocation
        
        VirtualFree(old_base, 0, MEM_RELEASE) # free the old pool allocation
        
        allocations = {}
        free_blocks = []
        
        for address, allocation in self.allocations.items(): # reconstruct the pool allocations list
            address -= (old_base - self.base) # arithmetically same as address = address - old_base + base, but optimized
            allocation.address = address
            allocations[address] = allocation
        
        for start, end in self.free_blocks: # reconstruct the free blocks list
            if end - old_base == old_quota: # frontier
                end = self.base + self.quota
            else:
                end = end - old_base + self.base
            start = start - old_base + self.base
            free_blocks.append((start, end))
        
        self.allocations = allocations
        self.free_blocks = free_blocks
        
    def delete(self):
        VirtualFree(self.base, 0, MEM_RELEASE)
        
    def __repr__(self) -> str:
        return f'<allocator CVirtualPoolAllocator, quota={self.quota}>'
        
class CRemotePoolAllocator(PoolAllocator, CRemoteAllocator):
    process: CProcess
    flags: int
    
    def __init__(self, process: CProcess, quota: int, 
                 flags: Optional[int] = None):
        if flags is None:
            flags = PAGE_READWRITE
        self.flags = flags
            
        self.process = process
        
        super().__init__(quota)
        
    def alloc_init(self):
        self.base = VirtualAllocEx(self.process.handle, NULL, self.quota, MEM_COMMIT, self.flags)
        
    def delete(self):
        VirtualFreeEx(self.process.handle, self.base, 0, MEM_RELEASE)
        self.base = None
        
    def alloc_init_resized(self, old_quota: int):
        old_base = self.base
        self.alloc_init()
        quota_to_copy = min(self.quota, old_quota) # prevent garbage copying
        old_data = (CHAR * old_quota)()
        self.process.read(old_base, old_data, quota_to_copy) # read the old allocation data from process
        self.process.write(self.base, old_data, quota_to_copy) # write the old allocation data into new allocation
        
        VirtualFreeEx(self.process.handle, old_base, 0, MEM_RELEASE) # free the old pool allocation
        
        allocations = {}
        free_blocks = []
        
        for address, allocation in self.allocations.items(): # reconstruct the pool allocations  list
            address -= (old_base - self.base) # arithmetically same as address = address - old_base + base, but optimized
            allocation.address = address
            allocations[address] = allocation
        
        for start, end in self.free_blocks: # reconstruct the free blocks list
            if end - old_base == old_quota: # frontier
                end = self.base + self.quota
            else:
                end = end - old_base + self.base
            start = start - old_base + self.base
            free_blocks.append((start, end))
        
        self.allocations = allocations
        self.free_blocks = free_blocks
        
    def __repr__(self) -> str:
        return f'<allocator CRemotePoolAllocator, process.pid={self.process.pid}, quota={self.quota}>'