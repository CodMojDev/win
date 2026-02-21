from ..codegen import *
from .core import *

from ...dispatch import variant_get_value

from ....errhandlingapi import *
from ....winnt import *

@PVECTORED_EXCEPTION_HANDLER
def VEH(pExcPointers: IPointer[EXCEPTION_POINTERS]) -> int:
    if pExcPointers.contents.ExceptionRecord.contents.ExceptionCode == DWORD(STATUS_HEAP_CORRUPTION).value:
        print('NTDLL IDINAHUI')
        return -1
    return 0

AddVectoredExceptionHandler(1, VEH)

class TLBParser:
    VT_TABLE: dict[int, str] = {
        VT_INT: 'INT', VT_UINT: 'UINT',
        VT_I1: 'c_byte', VT_UI1: 'BYTE',
        VT_I2: 'SHORT', VT_UI2: 'WORD',
        VT_I4: 'LONG', VT_UI4: 'DWORD',
        VT_I8: 'INT64', VT_UI8: 'UINT64',
        VT_UINT_PTR: 'UINT_PTR', VT_INT_PTR: 'INT_PTR',
        VT_BOOL: 'BOOL', 
        VT_UNKNOWN: 'P.IUnknown', VT_DISPATCH: 'P.IDispatch',
        VT_DISPATCH | VT_PTR: 'P.P.IDispatch',
        VT_UNKNOWN | VT_PTR: 'P.P.IUnknown',
        VT_BSTR: 'BSTR', VT_VARIANT: 'VARIANT',
        VT_LPSTR: 'LPSTR', VT_LPWSTR: 'LPWSTR',
        VT_R4: 'FLOAT', VT_R8: 'DOUBLE',
        VT_PTR: 'PVOID', VT_CY: 'CY', 
        VT_DECIMAL: 'DECIMAL', VT_USERDEFINED: 'GECLO'
    }
    
    class Enumeration:
        entries: list[tuple[str, str]]
        name: str
        
        def __init__(self, name: str):
            dbg_trace()
            
            self.entries = []
            self.name = name
            
    class Interface:
        base: 'TLBParser.Interface'
        docs: Optional[str]
        flags: int
        name: str
        iid: str
        
        class Function:
            return_value: Optional[str]
            docs: Optional[str]
            vtable_offset: int
            invkind: int
            is_com: bool
            name: str
            
            class Argument:
                argument_type: str
                flags: int
                name: str
                
                def __init__(self, name: str, flags: int, argument_type: str):
                    dbg_trace()
                    
                    self.argument_type = argument_type
                    self.flags = flags
                    self.name = name
                    
            arguments: list[Argument]
            
            def __init__(self, name: str, docs: Optional[str], invkind: int,
                         vtable_offset: int):
                dbg_trace()
                
                self.vtable_offset = vtable_offset
                self.return_value = None
                self.invkind = invkind
                self.arguments = []
                self.is_com = True
                self.name = name
                self.docs = docs
            
        functions: list[Function]
            
        def __init__(self, name: str, iid: str, flags: int, docs: Optional[str]):
            dbg_trace()
            
            self.functions = []
            self.flags = flags
            self.base = None
            self.name = name
            self.docs = docs
            self.iid = iid
            
    enumerations: list[Enumeration]
    interfaces: list[Interface]
    imports: list[str]
    tlb: ITypeLib
    code: Code
    
    def __init__(self, tlb: ITypeLib):
        dbg_trace()
        
        self.code = Code(GetTLBName(tlb) + '.icl')
        self.enumerations = []
        self.interfaces = []
        self.imports = []
        self.tlb = tlb
    
    def parse_enum(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs) -> Enumeration:
        isMain = 'main' in kwargs
        
        bszEnumName = BSTR()
        hr = typeInfo.GetDocumentation(-1, byref(bszEnumName), NULL, NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        
        enumeration = self.Enumeration(bszEnumName.value)
        SysFreeString(bszEnumName)
        
        for i in range(typeAttr.cVars):
            pVarDesc = LPVARDESC()
            hr = typeInfo.GetVarDesc(i, byref(pVarDesc))
            if FAILED(hr): raise COMError(hr)
            varDesc = pVarDesc.contents
            
            bszName = BSTR()
            hr = typeInfo.GetDocumentation(varDesc.memid, byref(bszName), NULL, NULL, NULL)
            if FAILED(hr): raise COMError(hr)
            name = bszName.value
            SysFreeString(bszName)
            
            ASSERT(varDesc.varkind == VAR_CONST)
            
            var = varDesc.lpvarValue.contents
            iEnumEntry = variant_get_value(var)
            ASSERT(isinstance(iEnumEntry, int))
            
            enumeration.entries.append((name, iEnumEntry))
            typeInfo.ReleaseVarDesc(pVarDesc)
    
        if not isMain:
            return enumeration
        else:
            self.enumerations.append(enumeration)
        
    def parse_interface(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs) -> Interface:
        isMain = 'main' in kwargs
        
        bszName = BSTR.init_untracked(); bszDocs = BSTR.init_untracked()
        hr = typeInfo.GetDocumentation(-1, byref(bszName), byref(bszDocs), NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        
        ASSERT(bszName)
        name = bszName.value
        if bszDocs: 
            docs = bszDocs.value
            SysFreeString(bszDocs)
        else: docs = None
        SysFreeString(bszName)
        
        ASSERT(typeAttr.cImplTypes <= 1)
        interface = self.Interface(name, str(typeAttr.guid), typeAttr.wTypeFlags, docs)
            
        if typeAttr.cImplTypes != 0:
            hrefType = HREFTYPE()
            hr = typeInfo.GetRefTypeOfImplType(0, byref(hrefType))
            if FAILED(hr): raise COMError(hr)
            pTypeInfoOfBase = ITypeInfo.NULL()
            hr = typeInfo.GetRefTypeInfo(hrefType, byref(pTypeInfoOfBase))
            if FAILED(hr): raise COMError(hr)
            interface.base = self.parse_typeinfo(pTypeInfoOfBase.contents)
            dbg_trace(f'Base = {interface.name}')
            
        ASSERT(typeAttr.cVars == 0)
        
        for i in range(typeAttr.cFuncs):
            pFuncDesc = FUNCDESC.NULL()
            hr = typeInfo.GetFuncDesc(i, byref(pFuncDesc))
            if FAILED(hr): raise COMError(hr)
            funcDesc = pFuncDesc.contents
            
            bszFuncName = BSTR.init_untracked(); bszFuncDocs = BSTR.init_untracked()
            hr = typeInfo.GetDocumentation(funcDesc.memid, byref(bszFuncName), 
                                           byref(bszFuncDocs), NULL, NULL)
            if FAILED(hr): raise COMError(hr)
            ASSERT(bszFuncName)
            funcName = bszFuncName.value
            if bszFuncDocs: 
                funcDocs = bszFuncDocs.value
                SysFreeString(bszFuncDocs)
            else: funcDocs = None
            SysFreeString(bszFuncName)
            ASSERT(funcDesc.funckind == FUNC_PUREVIRTUAL)
            
            function = self.Interface.Function(funcName, funcDocs, funcDesc.invkind, funcDesc.oVft)
            
            returnTypeDesc = funcDesc.elemdescFunc.tdesc
            if returnTypeDesc.vt != VT_HRESULT:
                function.is_com = False
                if returnTypeDesc.vt != VT_VOID and returnTypeDesc.vt != VT_EMPTY:
                    function.return_value = self.VT_TABLE[returnTypeDesc.vt]
            
            dbg_trace(f'{funcName} {function.return_value or ""}')
            
            nBstrNames = funcDesc.cParams + 1
            bstrNames: IArray[BSTR] = (BSTR * nBstrNames)()
            cNames = UINT()
            typeInfo.GetNames(funcDesc.memid, i_cast(byref(bstrNames), LPBSTR),
                              nBstrNames, byref(cNames))
            names = []
            
            for j in range(cNames.value):
                bstrName = bstrNames[j]
                names.append(bstrName.value)
                SysFreeString(bstrName)
                
            for j in range(cNames.value - 1, funcDesc.cParams):
                names.append(f'param{j}')
            
            names = names[1:]
            
            for j in range(funcDesc.cParams):
                elemdescParam = funcDesc.lprgelemdescParam[j]
                paramTypeDesc = elemdescParam.tdesc
                paramType = self.VT_TABLE[paramTypeDesc.vt]
                name = names[j]
                paramdesc = elemdescParam.paramdesc
                ASSERT(not (paramdesc.wParamFlags & PARAMFLAG_FHASDEFAULT))
                
                argument = self.Interface.Function.Argument(name, paramdesc.wParamFlags, paramType)
                function.arguments.append(argument)
                dbg_trace(f'{name} {paramType}')
                
            interface.functions.append(function)
            typeInfo.ReleaseFuncDesc(pFuncDesc)
            
        interface.functions.sort(key=lambda function: function.vtable_offset)
        
        if not isMain:
            return interface
        else:
            self.interfaces.append(interface)
        
    def parse_typeinfo(self, typeInfo: ITypeInfo, **kwargs):
        isMain = 'main' in kwargs
        
        pTlb = ITypeLib.NULL()
        hr = typeInfo.GetContainingTypeLib(byref(pTlb), NULL)
        if FAILED(hr): raise COMError(hr)
        
        if not PtrArithmetic.equals(self.tlb.ref(), pTlb):
            importName = '.' + GetTLBName(pTlb.contents)
            if importName not in self.imports:
                self.imports.append(importName)
                dbg_trace(f'ImportAdd {importName}')
            return
        
        pTypeAttr = TYPEATTR.NULL()
        hr = typeInfo.GetTypeAttr(byref(pTypeAttr))
        if FAILED(hr): raise COMError(hr)
        typeAttr = pTypeAttr.contents
        tkind = typeAttr.typekind
        
        value = None
        if tkind == TKIND_ENUM:
            dbg_trace('TKIND_ENUM')
            value = self.parse_enum(typeInfo, typeAttr, **kwargs)
        elif tkind == TKIND_INTERFACE:
            dbg_trace('TKIND_INTERFACE')
            value = self.parse_interface(typeInfo, typeAttr, **kwargs)
    
        typeInfo.ReleaseTypeAttr(pTypeAttr)
    
        if not isMain:
            return value
    
    def parse(self):
        for i in range(self.tlb.GetTypeInfoCount()):
            pTypeInfo = ITypeInfo.NULL()
            hr = self.tlb.GetTypeInfo(i, byref(pTypeInfo))
            if FAILED(hr): raise COMError(hr)
            self.parse_typeinfo(pTypeInfo.contents, main=True)
            
    def generate(self):
        self.code.add_version_data(100)
        self.code.append_newline()
        self.code.append_gencomment()
        self.code.append_commentext('TLB2ICL Generator')
        self.code.append_commentext(f'Generated from TLB: {GetTLBPath(self.tlb)}')
        self.code.append_newline()
        
        if len(self.imports) != 0:
            self.code.add_imports()
            for import_entry in self.imports:
                self.code.add_import(import_entry)
            self.code.end_block()
        
        for enumeration in self.enumerations:
            self.code.add_enum(enumeration.name)
            for entry_name, entry_value in enumeration.entries:
                self.code.add_enum_entry(entry_name, entry_value)
            self.code.end_block()
        
        for interface in self.interfaces:
            if interface.base and interface.base.name == 'IUnknown':
                self.code.add_interface_unknown(interface.name)
            else:
                if interface.base:
                    self.code.add_interface(interface.name, interface.base.name)
                else:
                    self.code.add_interface(interface.name)
            
            self.code.add_iid(interface.iid)
            
            for function in interface.functions:
                arguments = []
                for argument in function.arguments:
                    arguments.append(f'{argument.name} {argument.argument_type}')
                if function.is_com:
                    self.code.add_com_function(function.name, arguments)
                else:
                    self.code.add_virtual_function(function.name, function.return_value, arguments)
            
            self.code.end_block()