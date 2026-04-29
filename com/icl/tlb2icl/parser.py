from ..codegen import *
from .core import *

from ...dispatch import variant_get_value

from ....errhandlingapi import *
from ....winnt import *

import importlib as imp

tlb2icl_provider = WET_PROVIDER('TLB-To-ICL')

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
        VT_CY: 'CY', VT_DECIMAL: 'DECIMAL', 
        VT_HRESULT: 'HRESULT', VT_ERROR: 'LONG',
        VT_DATE: 'DOUBLE'
    }
    STRUCTURE_VT_TABLE: dict[int, str] = {
        VT_INT: 'IInt', VT_UINT: 'IUint',
        VT_I1: 'IInt8', VT_UI1: 'IUint8',
        VT_I2: 'IShort', VT_UI2: 'IUshort',
        VT_I4: 'ILong', VT_UI4: 'IUlong',
        VT_I8: 'IInt64', VT_UI8: 'IUint64',
        VT_UINT_PTR: 'IUintPtr', VT_INT_PTR: 'IIntPtr',
        VT_BOOL: 'IBool64', 
        VT_UNKNOWN: 'IPointer[IUnknown]', VT_DISPATCH: 'P.IDispatch',
        VT_DISPATCH | VT_PTR: 'IDoublePtr[IDispatch]',
        VT_UNKNOWN | VT_PTR: 'IDoublePtr[IUnknown]',
        VT_BSTR: 'BSTR', VT_VARIANT: 'VARIANT',
        VT_LPSTR: 'LPSTR', VT_LPWSTR: 'LPWSTR',
        VT_R4: 'IFloat', VT_R8: 'IDouble',
        VT_CY: 'CY', VT_DECIMAL: 'DECIMAL', 
        VT_HRESULT: 'ILong', VT_ERROR: 'ILong',
        VT_DATE: 'IDouble'
    }
    
    class Enumeration:
        entries: list[tuple[str, str]]
        name: str
        
        def __init__(self, name: str):
            dbg_trace(tlb2icl_provider)
            
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
                    dbg_trace(tlb2icl_provider)
                    
                    self.argument_type = argument_type
                    self.flags = flags
                    self.name = name
                    
            arguments: list[Argument]
            
            def __init__(self, name: str, docs: Optional[str], invkind: int,
                         vtable_offset: int):
                dbg_trace(tlb2icl_provider)
                
                self.vtable_offset = vtable_offset
                self.return_value = None
                self.invkind = invkind
                self.arguments = []
                self.is_com = True
                self.name = name
                self.docs = docs
            
        functions: list[Function]
            
        def __init__(self, name: str, iid: str, flags: int, docs: Optional[str]):
            dbg_trace(tlb2icl_provider)
            
            self.functions = []
            self.flags = flags
            self.base = None
            self.name = name
            self.docs = docs
            self.iid = iid
            
    class Record:
        fields: list[tuple[str, str]]
        name: str
        docs: str
        
        def __init__(self, name: str, docs: Optional[str]):
            dbg_trace(tlb2icl_provider)
            
            self.fields = []
            self.name = name
            self.docs = docs
            
    class Union:
        fields: list[tuple[str, str]]
        name: str
        docs: str
        
        def __init__(self, name: str, docs: Optional[str]):
            dbg_trace(tlb2icl_provider)
            
            self.fields = []
            self.name = name
            self.docs = docs
    
    class CoClass:
        clsid: str
        name: str
        docs: str
        
        def __init__(self, name: str, clsid: str, docs: Optional[str]):
            dbg_trace(tlb2icl_provider)
            
            self.clsid = clsid
            self.name = name
            self.docs = docs
    
    defined_types: dict[str, str]
    objects: list[Any]
    enumerations: list[Enumeration]
    interfaces: list[Interface]
    imports: list[str]
    tlb: ITypeLib
    code: Code
    
    def __init__(self, tlb: ITypeLib):
        dbg_trace(tlb2icl_provider)
        
        self.code = Code(GetTLBName(tlb) + '.icl')
        self.enumerations = []
        self.interfaces = []
        self.imports = ['win.com.autointerfacedef']
        self.objects = []
        self.tlb = tlb
        self.defined_types = {}
        for moduleName in ('win.com.baseinterfacedef',
                           'win.com.objinterfacedef',
                           'win.com.oleidl',
                           'win.com.autointerfacedef',
                           'win.com.ctlinterfacedef',
                           'win.winrt.eventtoken',
                           'win.winrt.inspectable',
                           'win.winrt.activation'):
            module = imp.import_module(moduleName)
            attributes = dir(module)
            for attribute in attributes:
                value = getattr(module, attribute)
                if isinstance(value, type) and issubclass(value, (COMInterface, CStructure, CUnion)):
                    if attribute not in self.defined_types:
                        self.defined_types[attribute] = moduleName
                elif value == INT and attribute not in self.defined_types:
                    self.defined_types[attribute] = moduleName
    
    def tdesc_to_type(self, typeInfo: ITypeInfo, tdesc: TYPEDESC) -> str:
        typeInTable = self.VT_TABLE.get(tdesc.vt)
        
        if typeInTable is not None:
            return typeInTable

        if tdesc.vt == VT_USERDEFINED:
            tinfo = LPTYPEINFO()
            hr = typeInfo.GetRefTypeInfo(tdesc.hreftype, byref(tinfo))
            if FAILED(hr): raise COMError(hr)
            bszUDTName = BSTR()
            hr = tinfo.contents.GetDocumentation(-1, byref(bszUDTName), NULL, NULL, NULL)
            if FAILED(hr): 
                tinfo.contents.Release()
                raise COMError(hr)
            tinfo.contents.Release()
            udtName = bszUDTName.value
            SysFreeString(bszUDTName)
            return udtName
        elif tdesc.vt == VT_PTR:
            if not tdesc.lptdesc:
                return 'PVOID'
            tdescUnter = tdesc.lptdesc.contents
            if tdescUnter.vt == VT_VOID:
                return 'PVOID'
            return 'P.' + self.tdesc_to_type(typeInfo, tdescUnter)
        elif tdesc.vt == VT_CARRAY:
            if not tdesc.lptdesc:
                return 'PVOID'
            tdescUnter = tdesc.lptdesc.contents
            if tdescUnter.vt == VT_VOID:
                return 'PVOID'
            return 'P.' + self.tdesc_to_type(typeInfo, tdescUnter)
        
        raise ValueError(tdesc.vt)
    
    def tdesc_to_type_of_structure(self, typeInfo: ITypeInfo, tdesc: TYPEDESC) -> str:
        typeInTable = self.STRUCTURE_VT_TABLE.get(tdesc.vt)
        
        if typeInTable is not None:
            return typeInTable
        
        if tdesc.vt == VT_USERDEFINED:
            return self.tdesc_to_type(typeInfo, tdesc)
        elif tdesc.vt == VT_PTR:
            if not tdesc.lptdesc:
                return 'IVoidPtrT'
            tdescUnter = tdesc.lptdesc.contents
            if tdescUnter.vt == VT_VOID:
                return 'IVoidPtrT'
            t = self.tdesc_to_type_of_structure(typeInfo, tdescUnter)
            return f'IPointer[{t}]'
        elif tdesc.vt == VT_CARRAY:
            if not tdesc.lptdesc:
                return 'IVoidPtrT'
            tdescUnter = tdesc.lptdesc.contents
            if tdescUnter.vt == VT_VOID:
                return 'IVoidPtrT'
            t = self.tdesc_to_type_of_structure(typeInfo, tdescUnter)
            return f'IPointer[{t}]'
        
        raise ValueError(tdesc.vt)
    
    def parse_enum(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs) -> Enumeration:
        bszEnumName = BSTR()
        hr = typeInfo.GetDocumentation(-1, byref(bszEnumName), NULL, NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        enumName = bszEnumName.value
        SysFreeString(bszEnumName)
        module = self.defined_types.get(enumName)
        if module is None:
            enumeration = self.Enumeration(enumName)
            
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
        
            return self.add_object(enumeration, kwargs)
        else:
            if module not in self.imports:
                self.imports.append(module)
        
    def parse_interface(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs) -> Interface:
        bszName = BSTR(); bszDocs = BSTR()
        hr = typeInfo.GetDocumentation(-1, byref(bszName), byref(bszDocs), NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        
        ASSERT(bszName)
        name = bszName.value
        if bszDocs: 
            docs = bszDocs.value
            SysFreeString(bszDocs)
        else: docs = None
        SysFreeString(bszName)
        
        module = self.defined_types.get(name)
        if module is None:
            ASSERT(typeAttr.cImplTypes <= 1)
            interface = self.Interface(name, str(typeAttr.guid), typeAttr.wTypeFlags, docs)
                
            if typeAttr.cImplTypes != 0:
                hrefType = HREFTYPE()
                hr = typeInfo.GetRefTypeOfImplType(0, byref(hrefType))
                if FAILED(hr): raise COMError(hr)
                pTypeInfoOfBase = ITypeInfo.NULL()
                hr = typeInfo.GetRefTypeInfo(hrefType, byref(pTypeInfoOfBase))
                if FAILED(hr): raise COMError(hr)
                bszName = BSTR()
                hr = pTypeInfoOfBase.contents.GetDocumentation(MEMBERID_NIL, byref(bszName), NULL, NULL, NULL)
                if FAILED(hr): raise COMError(hr)
                name = bszName.value
                SysFreeString(bszName)
                if name in self.defined_types:
                    interface.base = self.Interface(name, '', 0, None)
                else:
                    interface.base = self.parse_typeinfo(pTypeInfoOfBase.contents)
                dbg_trace(tlb2icl_provider, f'Base = {interface.name}')
                
            ASSERT(typeAttr.cVars == 0)
            
            for i in range(typeAttr.cFuncs):
                pFuncDesc = FUNCDESC.NULL()
                hr = typeInfo.GetFuncDesc(i, byref(pFuncDesc))
                if FAILED(hr): raise COMError(hr)
                funcDesc = pFuncDesc.contents
                
                bszFuncName = BSTR()
                bszFuncDocs = BSTR()
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
                if funcName in ('QueryInterface', 'AddRef', 'Release', 'GetTypeInfoCount', 'GetTypeInfo', 'GetIDsOfNames', 'Invoke'):
                    continue
                ASSERT(funcDesc.funckind in (FUNC_PUREVIRTUAL, FUNC_DISPATCH))
                
                invkind = funcDesc.invkind
                if invkind == INVOKE_PROPERTYGET:
                    funcName = 'get_' + funcName
                elif invkind == INVOKE_PROPERTYPUT:
                    funcName = 'put_' + funcName
                function = self.Interface.Function(funcName, funcDocs, invkind, funcDesc.oVft)
                
                returnTypeDesc = funcDesc.elemdescFunc.tdesc
                if funcDesc.funckind != FUNC_DISPATCH:
                    if returnTypeDesc.vt != VT_HRESULT:
                        function.is_com = False
                        if returnTypeDesc.vt != VT_VOID and returnTypeDesc.vt != VT_EMPTY:
                            function.return_value = self.tdesc_to_type(typeInfo, returnTypeDesc)
                        else:
                            function.return_value = 'VOID'
                else:
                    if returnTypeDesc.vt != VT_VOID and returnTypeDesc.vt != VT_EMPTY:
                        function.return_value = 'P.' + self.tdesc_to_type(typeInfo, returnTypeDesc)
                    else:
                        function.return_value = 'VOID'
                
                dbg_trace(tlb2icl_provider, f'{funcName} {function.return_value or ""}')
                
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
                    paramType = self.tdesc_to_type(typeInfo, paramTypeDesc)
                    name = names[j]
                    paramdesc = elemdescParam.paramdesc
                    if paramdesc.wParamFlags & PARAMFLAG_FRETVAL and funcDesc.funckind == FUNC_DISPATCH:
                        paramType = 'P.' + paramType
                    ASSERT(not (paramdesc.wParamFlags & PARAMFLAG_FHASDEFAULT))
                    
                    argument = self.Interface.Function.Argument(name, paramdesc.wParamFlags, paramType)
                    function.arguments.append(argument)
                    dbg_trace(tlb2icl_provider, f'{name} {paramType}')
                    
                if funcDesc.funckind == FUNC_DISPATCH:
                    if function.return_value != 'VOID':
                        function.arguments.append(self.Interface.Function.Argument(('p' * function.return_value.count('P.')) + 'Out', 0, function.return_value))
                    
                interface.functions.append(function)
                typeInfo.ReleaseFuncDesc(pFuncDesc)
                
            interface.functions.sort(key=lambda function: function.vtable_offset)
        
            return self.add_object(interface, kwargs)
        else:
            if module not in self.imports:
                self.imports.append(module)
        
    def parse_record(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs):
        bszName = BSTR()
        bszDocs = BSTR()
        hr = typeInfo.GetDocumentation(
            MEMBERID_NIL, byref(bszName), 
            byref(bszDocs), NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        ASSERT(bszName)
        name = bszName.value
        if bszDocs: 
            docs = bszDocs.value
            SysFreeString(bszDocs)
        else: docs = None
        SysFreeString(bszName)
        module = self.defined_types.get(name)
        if module is None:
            if 'union' in kwargs:
                object = self.Union(name, docs)
            else:
                object = self.Record(name, docs)
            for i in range(typeAttr.cVars):
                pVarDesc = LPVARDESC()
                hr = typeInfo.GetVarDesc(i, byref(pVarDesc))
                if FAILED(hr): raise COMError(hr)
                varDesc = pVarDesc.contents
                bszName = BSTR()
                hr = typeInfo.GetDocumentation(varDesc.memid, byref(bszName), NULL, NULL, NULL)
                if FAILED(hr):
                    typeInfo.ReleaseVarDesc(pVarDesc)
                    raise COMError(hr)
                ASSERT(bszName)
                name = bszName.value
                SysFreeString(bszName)
                fieldType = self.tdesc_to_type_of_structure(typeInfo, varDesc.elemdescVar.tdesc)
                object.fields.append((name, fieldType))
                typeInfo.ReleaseVarDesc(pVarDesc)
            return self.add_object(object, kwargs)
        else:
            if module not in self.imports:
                self.imports.append(module)

    def parse_typeinfo(self, typeInfo: ITypeInfo, **kwargs):
        pTlb = ITypeLib.NULL()
        hr = typeInfo.GetContainingTypeLib(byref(pTlb), NULL)
        if FAILED(hr): raise COMError(hr)
        
        if not PtrArithmetic.equals(self.tlb.ref(), pTlb):
            importName = '.' + GetTLBName(pTlb.contents)
            if importName not in self.imports:
                self.imports.append(importName)
                dbg_trace(tlb2icl_provider, f'ImportAdd {importName}')
            return
        
        pTypeAttr = TYPEATTR.NULL()
        hr = typeInfo.GetTypeAttr(byref(pTypeAttr))
        if FAILED(hr): raise COMError(hr)
        typeAttr = pTypeAttr.contents
        tkind = typeAttr.typekind
        
        value = None
        if tkind == TKIND_ENUM:
            dbg_trace(tlb2icl_provider, 'TKIND_ENUM')
            value = self.parse_enum(typeInfo, typeAttr, **kwargs)
        elif tkind == TKIND_INTERFACE:
            dbg_trace(tlb2icl_provider, 'TKIND_INTERFACE')
            value = self.parse_interface(typeInfo, typeAttr, **kwargs)
        elif tkind == TKIND_RECORD:
            dbg_trace(tlb2icl_provider, 'TKIND_RECORD')
            value = self.parse_record(typeInfo, typeAttr, **kwargs)
        elif tkind == TKIND_UNION:
            dbg_trace(tlb2icl_provider, 'TKIND_UNION')
            value = self.parse_record(typeInfo, typeAttr, **kwargs, union=True)
        elif tkind == TKIND_DISPATCH:
            dbg_trace(tlb2icl_provider, 'TKIND_DISPATCH')
            value = self.parse_dispinterface(typeInfo, typeAttr, **kwargs)
        elif tkind == TKIND_COCLASS:
            dbg_trace(tlb2icl_provider, 'TKIND_COCLASS')
            value = self.parse_coclass(typeInfo, typeAttr, **kwargs)
    
        typeInfo.ReleaseTypeAttr(pTypeAttr)
    
        return self.add_object(value, kwargs)
        
    def parse_coclass(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs):
        bszName = BSTR()
        bszDocs = BSTR()
        hr = typeInfo.GetDocumentation(
            MEMBERID_NIL, byref(bszName), 
            byref(bszDocs), NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        ASSERT(bszName)
        name = bszName.value
        if bszDocs: 
            docs = bszDocs.value
            SysFreeString(bszDocs)
        else: docs = None
        SysFreeString(bszName)
        coclass = self.CoClass(name, str(typeAttr.guid), docs)
        return self.add_object(coclass, kwargs)
    
    def parse_dispinterface(self, typeInfo: ITypeInfo, typeAttr: TYPEATTR, **kwargs):
        if typeAttr.wTypeFlags & TYPEFLAG_FDUAL:
            return self.parse_interface(typeInfo, typeAttr, **kwargs)
        
    def add_object(self, object, kwargs):
        if 'main' in kwargs:
            self.objects.append(object)
            return None
        else:
            return object
    
    def parse(self):
        for i in range(self.tlb.GetTypeInfoCount()):
            pTypeInfo = ITypeInfo.NULL()
            hr = self.tlb.GetTypeInfo(i, byref(pTypeInfo))
            if FAILED(hr): raise COMError(hr)
            self.parse_typeinfo(pTypeInfo.contents, main=True)
    
    def add_standard_alises(self):
        self.code.add_block('silent')
        self.code.add_pointer_explicit('SHORT', 'PSHORT')
        self.code.add_pointer_explicit('LONG', 'PLONG')
        self.code.add_pointer_explicit('UINT', 'PUINT')
        self.code.add_pointer_explicit('INT', 'PINT')
        self.code.add_pointer_explicit('DWORD', 'PDWORD')
        self.code.add_pointer_explicit('WORD', 'PWORD')
        self.code.end_block()
    
    def generate(self):
        self.code.add_version_data(100)
        self.code.append_newline()
        self.code.append_comment()
        self.code.append_comment('Interface Contract Language')
        self.code.append_comment()
        self.code.append_newline()
        self.code.append_commentext('TLB2ICL Generator')
        
        try:
            self.code.append_commentext(f'Generated from TLB: {GetTLBPath(self.tlb)}')
        except: 
            self.code.append_commentext(f'Generated from TLB: {GetTLBName(self.tlb)}')
        self.code.append_gencomment()
        self.code.append_newline()
        
        self.add_standard_alises()
        
        if len(self.imports) != 0:
            self.code.add_imports()
            for import_entry in self.imports:
                self.code.add_import(import_entry)
            self.code.end_block()
        
        standard_structure_types = (*self.STRUCTURE_VT_TABLE.values(), 'PVOID')
        standard_types = (*self.VT_TABLE.values(), 'PVOID')
        defined = []
        
        for i, object in enumerate(self.objects):
            if isinstance(object, self.Enumeration):
                self.objects.pop(i)
                self.objects.insert(0, object)
            elif isinstance(object, self.Record):
                for field, type in object.fields:
                    if type not in defined and type not in self.defined_types and type not in standard_structure_types:
                        break
                self.objects.pop(i)
                self.objects.insert(0, object)
        
        for object in self.objects:
            if isinstance(object, self.Enumeration):
                self.code.add_enum(object.name)
                for entry_name, entry_value in object.entries:
                    self.code.add_enum_entry(entry_name, entry_value)
                self.code.end_block()
            elif isinstance(object, self.Interface):
                if not object.base or (object.base and (object.base.name in defined or object.base.name in self.defined_types)):
                    if object.docs is not None:
                        self.code.add_documentation(object.docs)
                    if object.base and object.base.name == 'IUnknown':
                        self.code.add_interface_unknown(object.name)
                    else:
                        if object.base:
                            self.code.add_interface(object.name, object.base.name)
                        else:
                            self.code.add_interface(object.name)
                
                    self.code.add_iid(object.iid.lstrip('{').rstrip('}'))
                
                    for function in object.functions:
                        if function.docs is not None:
                            self.code.add_documentation(function.docs)
                        arguments = []
                        for argument in function.arguments:
                            components = argument.argument_type.split('.')
                            spec, type = components[:-1], components[-1]
                            if (type not in defined and type not in standard_types and type not in self.defined_types) and 'P' in spec:
                                type = 'FD.' + argument.argument_type
                            else:
                                type = argument.argument_type
                            arguments.append(f'{argument.name} {type}')
                        if function.is_com:
                            self.code.add_com_function(function.name, arguments)
                        else:
                            self.code.add_virtual_function(function.name, function.return_value, arguments)
                            
                    defined.append(object.name)
                    self.code.end_block()
                else:
                    self.objects.append(object)
            elif isinstance(object, self.Record):
                defined.append(object.name)
                if object.docs is not None:
                    self.code.add_documentation(object.docs)
                self.code.add_structure(object.name)
                for field, field_type in object.fields:
                    self.code.add_structure_field(field, field_type)
                self.code.end_block()
            elif isinstance(object, self.Union):
                defined.append(object.name)
                if object.docs is not None:
                    self.code.add_documentation(object.docs)
                self.code.add_union(object.name)
                for field, field_type in object.fields:
                    self.code.add_structure_field(field, field_type)
                self.code.end_block()
            elif isinstance(object, self.CoClass):
                if object.docs is not None:
                    self.code.add_documentation(object.docs)
                self.code.add_class(object.name)
                self.code.add_clsid(object.clsid.lstrip('{').rstrip('}'))
                self.code.end_block()