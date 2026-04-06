# This code created by WICL generator version 1.00
# Creation timestamp: Sun Jan 18 15:26:35 2026
# Generated from ICL: oaidl3.icl
# {
class ITypeChangeEvents(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{00020410-0000-0000-C000-000000000046}")

	@virtual_table.com_function(CHANGEKIND, LPTYPEINFO, LPOLESTR, PINT)
	def RequestTypeChange(self, changeKind: CHANGEKIND, pTInfoBefore: IPointer[ITypeInfo], pStrName: LPOLESTR, pfCancel: PINT) -> int: ...

	@virtual_table.com_function(CHANGEKIND, LPTYPEINFO, LPOLESTR)
	def AfterTypeChange(self, changeKind: CHANGEKIND, pTInfoAfter: IPointer[ITypeInfo], pStrName: LPOLESTR) -> int: ...

	virtual_table.build()

LPTYCHANGEEVENTS = ITypeChangeEvents.PTR()

class IErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{1CF2B120-547D-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPGUID)
	def GetGUID(self, pGUID: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetSource(self, pBstrSource: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetDescription(self, pBstrDescription: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetHelpFile(self, pBstrHelpFile: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetHelpContext(self, pdwHelpContext: PDWORD) -> int: ...

	virtual_table.build()

LPERRORINFO = IErrorInfo.PTR()

class ICreateErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{22F03340-547D-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPGUID, intermediate_method = True)
	def SetGUID(self, guid: GUID, **kwargs) -> int:
		return self.virt_delegate(guid.ref())

	@virtual_table.com_function(LPOLESTR)
	def SetSource(self, szSource: LPOLESTR) -> int: ...

	@virtual_table.com_function(LPOLESTR)
	def SetDescription(self, szDescription: LPOLESTR) -> int: ...

	@virtual_table.com_function(LPOLESTR)
	def SetHelpFile(self, szHelpFile: LPOLESTR) -> int: ...

	@virtual_table.com_function(DWORD)
	def SetHelpContext(self, dwHelpContext: int) -> int: ...

	virtual_table.build()

LPCREATEERRORINFO = ICreateErrorInfo.PTR()

class ISupportErrorInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{DF0B3D60-548F-101B-8E65-08002B2BD119}")

	@virtual_table.com_function(LPIID, intermediate_method = True)
	def InterfaceSupportsErrorInfo(self, iid: IID, **kwargs) -> int:
		return self.virt_delegate(iid.ref())

	virtual_table.build()

LPSUPPORTERRORINFO = ISupportErrorInfo.PTR()

class ITypeFactory(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)

	@virtual_table.com_function(LPTYPEINFO, LPIID, DOUBLE_PTR(IUnknown), intermediate_method = True)
	def CreateFromTypeInfo(self, pTypeInfo: IPointer[ITypeInfo], iid: IID, ppv: IDoublePtr[IUnknown], **kwargs) -> int:
		return self.virt_delegate(pTypeInfo, iid.ref(), ppv)

	virtual_table.build()

class ITypeMarshal(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000002D-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PVOID, DWORD, PVOID, PULONG)
	def Size(self, pvType: PVOID, dwDestContext: int, pvDestContext: PVOID, pSize: PULONG) -> int: ...

	@virtual_table.com_function(PVOID, DWORD, PVOID, ULONG, PBYTE, PULONG)
	def Marshal(self, pvType: PVOID, dwDestContext: int, pvDestContext: PVOID, cbBufferLength: int, pBuffer: PBYTE, pcbWritten: PULONG) -> int: ...

	@virtual_table.com_function(PVOID, DWORD, ULONG, PBYTE, PULONG)
	def Unmarshal(self, pvType: PVOID, dwFlags: int, cbBufferLength: int, pBuffer: PBYTE, pcbRead: PULONG) -> int: ...

	@virtual_table.com_function(PVOID)
	def Free(self, pvType: PVOID) -> int: ...

	virtual_table.build()

class IRecordInfo(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{0000002F-0000-0000-C000-000000000046}")

	@virtual_table.com_function(PVOID)
	def RecordInit(self, pvNew: PVOID) -> int: ...

	@virtual_table.com_function(PVOID)
	def RecordClear(self, pvExisting: PVOID) -> int: ...

	@virtual_table.com_function(PVOID, PVOID)
	def RecordCopy(self, pvExisting: PVOID, pvNew: PVOID) -> int: ...

	@virtual_table.com_function(LPGUID)
	def GetGuid(self, pguid: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetName(self, pbstrName: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PULONG)
	def GetSize(self, pcbSize: PULONG) -> int: ...

	@virtual_table.com_function(DOUBLE_PTR(ITypeInfo))
	def GetTypeInfo(self, ppTypeInfo: IDoublePtr[ITypeInfo]) -> int: ...

	@virtual_table.com_function(PVOID, LPCOLESTR, LPVARIANT)
	def GetField(self, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(PVOID, LPCOLESTR, LPVARIANT, PTR(PVOID))
	def GetFieldNoCopy(self, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT], ppvDataCArray: PVOID) -> int: ...

	@virtual_table.com_function(ULONG, PVOID, LPCOLESTR, LPVARIANT)
	def PutField(self, wFlags: int, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(ULONG, PVOID, LPCOLESTR, LPVARIANT)
	def PutFieldNoCopy(self, wFlags: int, pvData: PVOID, szFieldName: LPCOLESTR, pvarField: IPointer[VARIANT]) -> int: ...

	@virtual_table.com_function(PULONG, PTR(BSTR))
	def GetFieldNames(self, pcNames: PULONG, rgBstrNames: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(IRecordInfo))
	def IsMatchingType(self, pRecordInfo: IPointer[IRecordInfo]) -> int: ...

	@virtual_table.com_function()
	def RecordCreate(self) -> int: ...

	@virtual_table.com_function(PVOID, PTR(PVOID))
	def RecordCreateCopy(self, pvSource: PVOID, ppvDest: PVOID) -> int: ...

	@virtual_table.com_function(PVOID)
	def RecordDestroy(self, pvRecord: PVOID) -> int: ...

	virtual_table.build()

LPRECORDINFO = IRecordInfo.PTR()

class IErrorLog(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{3127CA40-446E-11CE-8135-00AA004BB851}")

	@virtual_table.com_function(LPCOLESTR, LPEXCEPINFO)
	def AddError(self, pszPropName: LPCOLESTR, pExcepInfo: IPointer[EXCEPINFO]) -> int: ...

	virtual_table.build()

LPERRORLOG = IErrorLog.PTR()

class IPropertyBag(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{55272A00-42CB-11CE-8135-00AA004BB851}")

	@virtual_table.com_function(LPCOLESTR, LPVARIANT, PTR(IErrorLog))
	def Read(self, pszPropName: LPCOLESTR, pVar: IPointer[VARIANT], pErrorLog: IPointer[IErrorLog]) -> int: ...

	@virtual_table.com_function(LPCOLESTR, LPVARIANT)
	def Write(self, pszPropName: LPCOLESTR, pVar: IPointer[VARIANT]) -> int: ...

	virtual_table.build()

LPPROPERTYBAG = IPropertyBag.PTR()

class ITypeLibRegistrationReader(IUnknown):
	virtual_table = COMVirtualTable.from_ancestor(IUnknown)
	_iid_ = IID("{ED6A8A2A-B160-4E77-8F73-AA7435CD5C27}")

	@virtual_table.com_function(DOUBLE_PTR(IEnumUnknown))
	def EnumTypeLibRegistrations(self, ppEnumUnknown: IDoublePtr[IEnumUnknown]) -> int: ...

	virtual_table.build()


	@virtual_table.com_function(IUnknown)
	def ITypeLibRegistration(self, ex: IUnknown) -> int: ...

	_iid_ = IID("{76A3E735-02DF-4A12-98EB-043AD3600AF3}")
	@virtual_table.com_function(LPGUID)
	def GetGuid(self, pGuid: IPointer[GUID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetVersion(self, pVersion: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(LCID))
	def GetLcid(self, pLcid: IPointer[LCID]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetWin32Path(self, pWin32Path: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetWin64Path(self, pWin64Path: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PTR(BSTR))
	def GetDisplayName(self, pDisplayName: IPointer[BSTR]) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetFlags(self, pFlags: PDWORD) -> int: ...

	@virtual_table.com_function(PDWORD)
	def GetHelpDir(self, pHelpDir: PDWORD) -> int: ...

	virtual_table.build()

# }
