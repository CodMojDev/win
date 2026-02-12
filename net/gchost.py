#
# gchost.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Sun Feb  8 15:04:19 2026
# Generated from ICL: gchost.icl
#

from ..com.unknwn import *

COR_GC_COUNTS = 1
COR_GC_MEMORYUSAGE = 2
COR_GC_STAT_TYPES = INT

COR_GC_THREAD_HAS_PROMOTED_BYTES = 1
COR_GC_THREAD_STATS_TYPES = INT

@CStructure.make
class COR_GC_STATS(CStructure):
    Flags: IUlong
    ExplicitGCCount: ISizeT
    GenCollectionsTaken: IArrayFixedSize[ISizeT,3]
    CommittedKBytes: ISizeT
    ReservedKBytes: ISizeT
    Gen0HeapSizeKBytes: ISizeT
    Gen1HeapSizeKBytes: ISizeT
    Gen2HeapSizeKBytes: ISizeT
    LargeObjectHeapSizeKBytes: ISizeT
    KBytesPromotedFromGen0: ISizeT
    KBytesPromotedFromGen1: ISizeT

@CStructure.make
class COR_GC_THREAD_STATS(CStructure):
    PerThreadAllocation: IUnsignedLongLong
    Flags: IUlong

class IGCHost(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{FAC34F6E-0DCD-47b5-8021-531BC5ECCA63}")

    @virtual_table.com_function(DWORD, DWORD)
    def SetGCStartupLimits(self, SegmentSize: int, MaxGen0Size: int) -> int: ...

    @virtual_table.com_function(LONG)
    def Collect(self, Generation: int) -> int: ...

    @virtual_table.com_function(PTR(COR_GC_STATS))
    def GetStats(self, pStats: IPointer[COR_GC_STATS]) -> int: ...

    @virtual_table.com_function(PDWORD, PTR(COR_GC_THREAD_STATS))
    def GetThreadStats(self, pFiberCookie: PDWORD, pStats: IPointer[COR_GC_THREAD_STATS]) -> int: ...

    @virtual_table.com_function(SIZE_T)
    def SetVirtualMemLimit(self, sztMaxVirtualMemMB: int) -> int: ...

    virtual_table.build()

class IGCHost2(IGCHost):
    virtual_table = COMVirtualTable.from_ancestor(IGCHost)
    _iid_ = IID("{A1D70CEC-2DBE-4E2F-9291-FDF81438A1DF}")

    @virtual_table.com_function(SIZE_T, SIZE_T)
    def SetGCStartupLimitsEx(self, SegmentSize: int, MaxGen0Size: int) -> int: ...

    virtual_table.build()

