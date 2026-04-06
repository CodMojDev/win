# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 16:23:20 2026
# Generated from ICL: ocidl1.icl
# {
class IProvideClassInfo2(IProvideClassInfo):
	virtual_table = COMVirtualTable.from_ancestor(IProvideClassInfo)
	_iid_ = IID("{A6BC3AC0-DBAA-11CE-9DE3-00AA004BB851}")

	@virtual_table.com_function(DWORD, LPGUID)
	def GetGUID(self, dwGuidKind: int, pGUID: IPointer[GUID]) -> int: ...

	virtual_table.build()

LPPROVIDECLASSINFO2 = IProvideClassInfo2.PTR()

# }
