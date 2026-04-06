.icl
.ver 100
.gencomment

~
~from ..com.unknwn import *
~

al int SIZE_T

ed COR_GC_STAT_TYPES
{
	ee COR_GC_COUNTS 1
	ee COR_GC_MEMORYUSAGE 2
}

ed COR_GC_THREAD_STATS_TYPES
{
	ee COR_GC_THREAD_HAS_PROMOTED_BYTES 1
}

sd COR_GC_STATS
{
	sf IUlong Flags
	sf ISizeT ExplicitGCCount
	sf IArrayFixedSize[ISizeT,3] GenCollectionsTaken
	sf ISizeT CommittedKBytes 
	sf ISizeT ReservedKBytes
	sf ISizeT Gen0HeapSizeKBytes
	sf ISizeT Gen1HeapSizeKBytes
	sf ISizeT Gen2HeapSizeKBytes
	sf ISizeT LargeObjectHeapSizeKBytes
	sf ISizeT KBytesPromotedFromGen0
	sf ISizeT KBytesPromotedFromGen1
}

sd COR_GC_THREAD_STATS
{
	sf IUnsignedLongLong PerThreadAllocation
	sf IUlong Flags
}

I IGCHost ex IUnknown
{
	iid FAC34F6E-0DCD-47b5-8021-531BC5ECCA63
	cf SetGCStartupLimits SegmentSize DWORD MaxGen0Size DWORD
	cf Collect Generation LONG
	cf GetStats pStats P.COR_GC_STATS
	cf GetThreadStats pFiberCookie PDWORD pStats P.COR_GC_THREAD_STATS
	cf SetVirtualMemLimit sztMaxVirtualMemMB SIZE_T
}

I IGCHost2 ex IGCHost
{
	iid A1D70CEC-2DBE-4E2F-9291-FDF81438A1DF
	cf SetGCStartupLimitsEx SegmentSize SIZE_T MaxGen0Size SIZE_T
}