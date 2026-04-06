# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:28:38 2026
# Generated from ICL: ocidl2.icl
# {
class IProvideMultipleClassInfo(IProvideClassInfo2):
	virtual_table = COMVirtualTable.from_ancestor(IProvideClassInfo2)
	_iid_ = IID("{A7ABA9C1-8983-11cf-8F20-00805F2CD064}")

	@virtual_table.com_function(PULONG)
	def GetMultiTypeInfoCount(self, pcti: PULONG) -> int: ...

	@virtual_table.com_function(ULONG, DWORD, DOUBLE_PTR(ITypeInfo), PDWORD, PULONG, LPIID, LPIID)
	def GetInfoOfIndex(self, iti: int, dwFlags: int, pptiCoClass: IDoublePtr[ITypeInfo], pdwTIFlags: PDWORD, pcdispidReserved: PULONG, piidPrimary: IPointer[IID], piidSource: IPointer[IID]) -> int: ...

	virtual_table.build()

LPPROVIDEMULTIPLECLASSINFO = IProvideMultipleClassInfo.PTR()

# }
