from ..icl.codegen import *
from .factory import *
from .baseface import *
from win.winerror import *

ICL_GUID_INTERFACE = 0
ICL_GUID_CLASS = 1
ICL_GUID = INT

ICL_APPEND_NOT_BREAKLINE = 0x01
ICL_APPEND_INDENTED = 0x02
ICL_APPEND_FLAGS = INT

ICL_COMMENT_NOT_BREAKLINE = 0x01
ICL_COMMENT_EXT = 0x02
ICL_COMMENT_FLAGS = INT

class IICLGenerator(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID('{203FB4A1-B7FB-43BB-89C9-827802AB914F}')
    
    @virtual_table.com_function(LPCWSTR)
    def Open(self, lpszFilePath: LPCWSTR) -> int: ...
    
    @virtual_table.com_function()
    def Close(self) -> int: ...
    
    @virtual_table.com_function(UINT)
    def EmitVersionData(self, uiVersion: int) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitBlock(self, lpszBlock: LPCWSTR) -> int: ...
    
    @virtual_table.com_function()
    def EmitBlockEnd(self) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, LPCWSTR)
    def EmitInterface(self, lpszInterfaceName: LPCWSTR, lpszBaseName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitInterfaceUnknown(self, lpszInterfaceName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(ICL_GUID, GUID)
    def EmitGUID(self, guidType: int, guid: GUID) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitStructure(self, lpszStructureName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitUnion(self, lpszUnionName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, LPCWSTR)
    def EmitField(self, lpszFieldName: LPCWSTR, lpszFieldType: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, ICL_APPEND_FLAGS)
    def Append(self, lpszText: LPCWSTR, dwFlags: int) -> int: ...
    
    @virtual_table.com_function()
    def EmitNewLine(self) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitImport(self, lpszImportName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitDocumentation(self, lpszDocumentation: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, ICL_COMMENT_FLAGS)
    def EmitComment(self, lpszComment: LPCWSTR, dwFlags: int) -> int: ...
    
    @virtual_table.com_function(BOOL)
    def EmitGencomment(self, bLW: int) -> int: ...
    
    @virtual_table.com_function(LPCWSTR)
    def EmitEnum(self, lpszEnumName: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, INT)
    def EmitEnumEntry(self, lpszEnumEntry: LPCWSTR, iEntryValue: int) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, LPCWSTR)
    def EmitEnumEntryForce(self, lpszEnumEntry: LPCWSTR, lpszEntryValue: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, LPCWSTR)
    def EmitEqual(self, lpszEq1: LPCWSTR, lpszEq2: LPCWSTR) -> int: ...
    
    @virtual_table.com_function(PTR(LPCWSTR))
    def QueryIndent(self, lplpszIndent: IPointer[LPWSTR]) -> int: ...
    
    @virtual_table.com_function(PTR(LPCWSTR))
    def MakeIndents(self, lplpszIndents: IPointer[LPWSTR]) -> int: ...
    
    @virtual_table.com_function(LPCWSTR, LPCWSTR, BYTE, PTR(LPCWSTR))
    def EmitFunction(
        self, lpszFunctionName: LPCWSTR, lpszFunctionResult: LPCWSTR,
        bArgumentsCount: int, lpszFunctionArguments: IPointer[LPCWSTR]) -> int: ...
    
    @virtual_table.com_function()
    def Indent(self) -> int: ...
    
    @virtual_table.com_function()
    def Unindent(self) -> int: ...
    
    virtual_table.build()
    
class ICLGenerator(CComClass, IICLGenerator):
    _clsid_ = CLSID('{24ECC486-D5B0-4CE7-B457-5E05C065E4F2}')
    _creatable_ = True
    
    def __init__(self):
        super().__init__()
        self.implement_interface(IICLGenerator)
        self.code = None
    
    def Valid(self) -> bool:
        return hasattr(self, 'code') and not self.code.file.closed
    
    def Open_Impl(self, lpszFilePath: LPCWSTR) -> int: 
        if not lpszFilePath:
            return E_POINTER
        if hasattr(self, 'code'):
            return S_FALSE
        try:
            self.code = Code(lpszFilePath.value)
        except FileNotFoundError:
            return MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_PATH_NOT_FOUND)
        except AccessError:
            return MAKE_HRESULT(SEVERITY_ERROR, FACILITY_WIN32, ERROR_ACCESS_DENIED)
        except Exception:
            return E_FAIL
        return S_OK
    
    def Close_Impl(self) -> int: 
        if not self.Valid():
            return S_FALSE
        self.code.file.close()
        return S_OK
    
    def EmitVersionData_Impl(self, uiVersion: int) -> int:
        if not self.Valid():
            return E_FAIL
        self.code.add_version_data(uiVersion)
        return S_OK
    
    def EmitBlock_Impl(self, lpszBlock: LPCWSTR) -> int: 
        if not lpszBlock:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_block(lpszBlock.value)
        return S_OK
    
    def EmitBlockEnd_Impl(self) -> int: 
        if not self.Valid():
            return E_FAIL
        self.code.end_block()
        return S_OK
    
    def EmitInterface_Impl(self, lpszInterfaceName: LPCWSTR, lpszBaseName: LPCWSTR) -> int:
        if not lpszInterfaceName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        if not lpszBaseName:
            self.code.add_interface(lpszInterfaceName.value)
        else:
            self.code.add_interface(lpszInterfaceName.value, lpszBaseName.value)
        return S_OK
    
    def EmitInterfaceUnknown_Impl(self, lpszInterfaceName: LPCWSTR) -> int: 
        if not lpszInterfaceName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_interface_unknown(lpszInterfaceName.value)
        return S_OK
    
    def EmitGUID_Impl(self, guidType: int, guid: GUID) -> int: 
        if not self.Valid():
            return E_FAIL
        if guidType == ICL_GUID_INTERFACE:
            self.code.add_iid(str(guid))
        elif guidType == ICL_GUID_CLASS:
            self.code.add_clsid(str(guid))
        else:
            return E_INVALIDARG
        return S_OK
    
    def EmitStructure_Impl(self, lpszStructureName: LPCWSTR) -> int: 
        if not lpszStructureName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_structure(lpszStructureName.value)
        return S_OK
    
    def EmitUnion_Impl(self, lpszUnionName: LPCWSTR) -> int: 
        if not lpszUnionName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_union(lpszUnionName.value)
        return S_OK
    
    def EmitField_Impl(self, lpszFieldName: LPCWSTR, lpszFieldType: LPCWSTR) -> int: 
        if not (lpszFieldName and lpszFieldType):
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_structure_field(lpszFieldName.value, lpszFieldType.value)
        return S_OK
    
    def Append_Impl(self, lpszText: LPCWSTR, dwFlags: int) -> int: 
        if not lpszText:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        not_breakline = (dwFlags & ICL_APPEND_NOT_BREAKLINE) != 0
        if dwFlags & ICL_APPEND_INDENTED:
            self.code.append_indented(lpszText.value, not_breakline=not_breakline)
        else:
            self.code.append(lpszText.value, not_breakline=not_breakline)
        return S_OK
    
    def EmitNewLine_Impl(self) -> int: 
        if not self.Valid():
            return E_FAIL
        self.code.append_newline()
        return S_OK
    
    def EmitImport_Impl(self, lpszImportName: LPCWSTR) -> int: 
        if not lpszImportName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_import(lpszImportName.value)
        return S_OK
    
    def EmitDocumentation_Impl(self, lpszDocumentation: LPCWSTR) -> int: 
        if not lpszDocumentation:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_documentation(lpszDocumentation.value)
        return S_OK
    
    def EmitComment_Impl(self, lpszComment: LPCWSTR, dwFlags: int) -> int: 
        if not self.Valid():
            return E_FAIL
        if dwFlags & ICL_COMMENT_EXT:
            if not lpszComment:
                return E_POINTER
            self.code.append_commentext(lpszComment.value)
        else:
            self.code.append_comment(
                lpszComment.value if lpszComment else '', 
                (dwFlags & ICL_COMMENT_NOT_BREAKLINE) != 0)
        return S_OK
    
    def EmitGencomment_Impl(self, bLW: int) -> int: 
        if not self.Valid():
            return E_FAIL
        if bLW:
            self.code.append_gencommentlw()
        else:
            self.code.append_gencomment()
        return S_OK
    
    def EmitEnum_Impl(self, lpszEnumName: LPCWSTR) -> int: 
        if not lpszEnumName:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_enum(lpszEnumName.value)
        return S_OK

    def EmitEnumEntry_Impl(self, lpszEnumEntry: LPCWSTR, iEntryValue: int) -> int: 
        if not lpszEnumEntry:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_enum_entry(lpszEnumEntry.value, iEntryValue)
        return S_OK
    
    def EmitEnumEntryForce_Impl(self, lpszEnumEntry: LPCWSTR, lpszEntryValue: LPCWSTR) -> int: 
        if not (lpszEnumEntry and lpszEntryValue):
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.add_enum_entry_force(lpszEnumEntry.value, lpszEntryValue.value)
        return S_OK
    
    def EmitEqual_Impl(self, lpszEq1: LPCWSTR, lpszEq2: LPCWSTR) -> int: 
        if not (lpszEq1 and lpszEq2):
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        self.code.append_equal(lpszEq1.value, lpszEq2.value)
        return S_OK
    
    def QueryIndent_Impl(self, lplpszIndent: IPointer[LPWSTR]) -> int: 
        if not lplpszIndent:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        TlWritePvToPpv(lplpszIndent, TlAllocateString(self.code.INDENT))
        return S_OK
    
    def MakeIndents_Impl(self, lplpszIndents: IPointer[LPWSTR]) -> int:
        if not lplpszIndents:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        TlWritePvToPpv(lplpszIndents, TlAllocateString(self.code.make_indents()))
        return S_OK
    
    def EmitFunction_Impl(
        self, lpszFunctionName: LPCWSTR, lpszFunctionResult: LPCWSTR,
        bArgumentsCount: int, lpszFunctionArguments: IPointer[LPCWSTR]) -> int: 
        if not lpszFunctionName:
            return E_POINTER
        if bArgumentsCount != 0 and not lpszFunctionArguments:
            return E_POINTER
        if not self.Valid():
            return E_FAIL
        arguments = []
        for i in range(bArgumentsCount):
            arguments.append(lpszFunctionArguments[i].value)
        if not lpszFunctionResult:
            self.code.add_com_function(lpszFunctionName.value, arguments)
        else:
            self.code.add_virtual_function(lpszFunctionName.value, lpszFunctionResult.value, arguments)
        return S_OK
    
    def Indent_Impl(self) -> int: 
        if not self.Valid():
            return E_FAIL
        self.code.indent()
        return S_OK
    
    def Unindent_Impl(self) -> int: 
        if not self.Valid():
            return E_FAIL
        self.code.unindent()
        return S_OK