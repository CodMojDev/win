from typing import Sequence

from win.defbase import *

suppress_WinWarning()

import win.com.dispatch

from ..com.ctlinterfacedef import *
from ..com.dispatch import *
from .mscoree import *
from ..com.comtl import *
from ..dbg.wd import *

unsuppress_WinWarning()

import builtins

provider = WET_PROVIDER('NET-Interop')

_TypeMarshaller = DelayedMarshaller()

class _Object(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    _iid_ = IID('{65074F7F-63C0-304E-AF0A-D51741CB4A8D}')
    
    @virtual_table.com_function_vbstyle(retval_index=0, retval_type=BSTR)
    def ToString(self) -> BSTR: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, retval_index=1, retval_type=VARIANT_BOOL)
    def Equals(self, obj) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=LONG, 
        retval_function=RetVal_GetValue)
    def GetHashCode(self) -> int: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def GetType(self) -> '_Type': ...
        
    def __hash__(self) -> int:
        return self.GetHashCode()
    
    def __str__(self) -> str:
        bstr = self.ToString()
        result = bstr.value
        SysFreeString(bstr)
        return result
    
    def __repr__(self) -> str:
        objType = self.GetType()
        bstrFullName = objType.FullName
        typeFullName = bstrFullName.value
        SysFreeString(bstrFullName)
        
        return f'<{typeFullName} object "{str(self)}">'
    
    def __eq__(self, obj) -> bool:
        return self.Equals(obj)
    
    virtual_table.build()
    
_AssemblyMarshaller = DelayedMarshaller()
    
class MemberTypes(INT):
    Constructor = 1
    Event = 2
    Field = 4
    Method = 8
    Property = 16
    TypeInfo = 32
    Custom = 64
    NestedType = 128
    All = 191
    
class RuntimeTypeHandle(CStructure):
    _fields_ = [('m_type', LPUNKNOWN)]
    
    m_type: IPointer[IUnknown]
    
class RuntimeMethodHandle(CStructure):
    _fields_ = [('m_value', LPUNKNOWN)]
    
    m_value: IPointer[IUnknown]
    
class RuntimeFieldHandle(CStructure):
    _fields_ = [('m_ptr', LPUNKNOWN)]
    
    m_ptr: IPointer[IUnknown]
    
class BindingFlags(INT):
    Default = 0
    IgnoreCase = 1
    DeclaredOnly = 2
    Instance = 4
    Static = 8
    Public = 16
    NonPublic = 32
    FlattenHierarchy = 64
    InvokeMethod = 256
    CreateInstance = 512
    GetField = 1024
    SetField = 2048
    GetProperty = 4096
    SetProperty = 8192
    PutDispProperty = 16384
    PutRefDispProperty = 32768
    ExactBinding = 0x00010000
    SuppressChangeType = 0x00020000
    OptionalParamBinding = 0x00040000
    IgnoreReturn = 0x01000000
    
class _ParameterInfo(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _Module(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class MethodImplAttributes(INT):
    CodeTypeMask = 3
    IL = 0
    Native = 1
    OPTIL = 2
    Runtime = 3
    ManagedMask = 4
    Unmanaged = 4
    Managed = 0
    ForwardRef = 16
    PreserveSig = 128
    InternalCall = 4096
    Synchronized = 32
    NoInlining = 8
    NoOptimization = 64
    MaxMethodImplVal = 65535
    
class MethodAttributes(INT):
    MemberAccessMask = 7
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    Static = 16
    Final = 32
    Virtual = 64
    HideBySig = 128
    CheckAccessOnOverride = 512
    VtableLayoutMask = 256
    ReuseSlot = 0
    NewSlot = 256
    Abstract = 1024
    SpecialName = 2048
    PinvokeImpl = 8192
    UnmanagedExport = 8
    RTSpecialName = 4096
    ReservedMask = 53248
    HasSecurity = 16384
    RequireSecObject = 32768
    
class CallingConventions(INT):
    Standard = 1
    VarArgs = 2
    Any = 3
    HasThis = 32
    ExplicitThis = 64
    
class _CultureInfo(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _MemberInfo(_Object):
    virtual_table = COMVirtualTable.from_ancestor(_Object)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=MemberTypes,
        retval_function=RetVal_GetValue)
    def MemberType(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def name(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def DeclaringType(self) -> '_Type': ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def ReflectedType(self) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, VARIANT_BOOL, retval_index=2, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes(self, attributeType: '_Type',
                            inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes_2(self, inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, VARIANT_BOOL, retval_index=2,
        retval_type=VARIANT_BOOL)
    def IsDefined(self, attributeType: '_Type',
                  inherit: bool) -> bool: ...
    
    virtual_table.build()

@CStructure.make
class ParameterModifier(CStructure):
    _byRef: SafeArray[IVariantBool]
    
class _MethodBase(_MemberInfo):
    virtual_table = COMVirtualTable.from_ancestor(_MemberInfo)
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_ParameterInfo)),
        retval_function=RetVal_Dereference)
    def GetParameters(self) -> SafeArray[_ParameterInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=MethodImplAttributes,
        retval_function=RetVal_GetValue)
    def GetMethodImplementationFlags(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=RuntimeMethodHandle)
    def MethodHandle(self) -> RuntimeMethodHandle: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=MethodAttributes,
        retval_function=RetVal_GetValue)
    def Attributes(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=CallingConventions,
        retval_function=RetVal_GetValue)
    def CallingConvention(self) -> int: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, BindingFlags, PVOID, PTR(SafeArray.typed(VARIANT)),
        _CultureInfo.PTR(), retval_index=5, 
        retval_type=VARIANT)
    def Invoke_2(self, obj, invokeAttr: int, Binder: '_Binder',
                 parameters: SafeArray[Any], culture: _CultureInfo) -> Any: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPublic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPrivate(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamily(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamilyAndAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamilyOrAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsStatic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFinal(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsVirtual(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsHideBySig(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAbstract(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSpecialName(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsConstructor(self) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, PTR(SafeArray.typed(VARIANT)),
        retval_index=2, retval_type=VARIANT)
    def Invoke_3(self, obj, parameters: SafeArray[Any]) -> Any: ...
    
    virtual_table.build()

class ICustomAttributeProvider(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    @virtual_table.com_function_vbstyle(
        PVOID, VARIANT_BOOL, retval_index=2, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes(self, attributeType: '_Type',
                            inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=2, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes_2(self, inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, VARIANT_BOOL, retval_index=2,
        retval_type=VARIANT_BOOL,
        intermediate_method=True)
    def IsDefined(self, attributeType: '_Type',
                  inherit: bool, **kwargs) -> bool:
        return self.virt_delegate(TlGetRef(attributeType), TlOAToBool(inherit))
    
    virtual_table.build()
    
_MethodInfoMarshaller = DelayedMarshaller()

class _MethodInfo(_MethodBase):
    virtual_table = COMVirtualTable.from_ancestor(_MethodBase)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def returnType(self) -> '_Type': ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(ICustomAttributeProvider),
        retval_function=RetVal_Dereference)
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_MethodInfoMarshaller)
    def GetBaseDefinition(self) -> '_MethodInfo': ...
    
    virtual_table.build()
    
def _MethodInfo_Marshal(value) -> _MethodInfo:
    return i_cast(value, _MethodInfo.PTR()).contents
    
class _PropertyInfo(_MemberInfo):
    virtual_table = COMVirtualTable.from_ancestor(_MemberInfo)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def PropertyType(self) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, PTR(SafeArray.typed(VARIANT)),
        retval_index=2, retval_type=VARIANT)
    def GetValue(self, obj, index: SafeArray[Any]) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, BindingFlags, PVOID, 
        SafeArray.typed(VARIANT), _CultureInfo.PTR(),
        retval_index=5, retval_type=VARIANT)
    def GetValue_2(self, obj, invokeAttr: int, Binder: '_Binder', 
                   index: SafeArray[Any], culture: _CultureInfo) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, VARIANT, PTR(SafeArray.typed(VARIANT)))
    def SetValue(self, obj, value, index: SafeArray[Any]): ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, VARIANT, BindingFlags, PVOID, 
        SafeArray.typed(VARIANT), _CultureInfo.PTR())
    def SetValue_2(self, obj, value, invokeAttr: int,
                   Binder: '_Binder', index: SafeArray[Any],
                   culture: _CultureInfo): ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1,
        retval_type=PTR(SafeArray.typed(_MethodInfo)),
        retval_function=RetVal_Dereference)
    def GetAccessors(self, nonPublic: bool) -> SafeArray[_MethodInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1,
        retval_type=_MethodInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetGetMethod(self, nonPublic: bool) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1,
        retval_type=_MethodInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetSetMethod(self, nonPublic: bool) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_ParameterInfo)),
        retval_function=RetVal_Dereference)
    def GetIndexParameters(self) -> SafeArray[_ParameterInfo]: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def CanRead(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def CanWrite(self) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_MethodInfo)),
        retval_function=RetVal_Dereference)
    def GetAccessors_2(self, nonPublic: bool) -> SafeArray[_MethodInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=_MethodInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetGetMethod_2(self) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=_MethodInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetSetMethod_2(self) -> _MethodInfo: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSpecialName(self) -> bool: ...
    
    virtual_table.build()
    
class FieldAttributes(INT):
    FieldAccessMask = 7
    PrivateScope = 0
    Private = 1
    FamANDAssem = 2
    Assembly = 3
    Family = 4
    FamORAssem = 5
    Public = 6
    Static = 16
    InitOnly = 32
    Literal = 64
    NotSerialized = 128
    SpecialName = 512
    PinvokeImpl = 8192
    ReservedMask = 38144
    RTSpecialName = 1024
    HasFieldMarshal = 4096
    HasDefault = 32768
    HasFieldRVA = 256
    
class _FieldInfo(_MemberInfo):
    virtual_table = COMVirtualTable.from_ancestor(_MemberInfo)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def FieldType(self) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, retval_index=1, retval_type=VARIANT)
    def GetValue(self, obj) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, retval_index=1, retval_type=VARIANT)
    def GetValueDirect(self, obj) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, VARIANT, BindingFlags, PVOID, _CultureInfo.PTR())
    def SetValue(self, obj, value, invokeAttr: int, Binder: '_Binder',
                 culture: _CultureInfo): ...
        
    @virtual_table.com_function_vbstyle(
        VARIANT, VARIANT)
    def SetValueDirect(self, obj, value): ...
        
    @virtual_table.com_function_vbstyle(
        VARIANT, VARIANT)
    def SetValue_2(self, obj, value): ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=RuntimeFieldHandle)
    def FieldHandle(self) -> RuntimeFieldHandle: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=FieldAttributes,
        retval_function=RetVal_GetValue)
    def Attributes(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPublic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPrivate(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamily(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamilyAndAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsFamilyOrAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsStatic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsInitOnly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsLiteral(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNotSerialized(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSpecialName(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPinvokeImpl(self) -> bool: ...
    
    virtual_table.build()
    
class _Binder(_Object):
    virtual_table = COMVirtualTable.from_ancestor(_Object)
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, 
        SafeArray.typed(_MethodBase),
        SafeArray.typed(VARIANT), 
        SafeArray.typed(ParameterModifier),
        _CultureInfo.PTR(),
        SafeArray.typed(BSTR),
        VARIANT, retval_index=7,
        retval_type=PTR(_MethodBase),
        retval_function=RetVal_Dereference)
    def BindToMethod(self, bindingAttr: int, 
                     match: SafeArray[_MethodBase],
                     args: SafeArray[Any],
                     modifiers: SafeArray[int],
                     culture: _CultureInfo,
                     names: SafeArray[BSTR],
                     state) -> _MethodBase: ...
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, 
        SafeArray.typed(_FieldInfo),
        VARIANT, 
        _CultureInfo.PTR(), retval_index=4,
        retval_type=PTR(_FieldInfo),
        retval_function=RetVal_Dereference)
    def BindToField(self, bindingAttr: int, 
                     match: SafeArray[_FieldInfo],
                     value, culture: _CultureInfo) -> _FieldInfo: ...
    
    # SelectMethod, SelectProperty, ChangeType, ReorderArgumentArray. i'm lazy to do this
    virtual_table.skip_count(4)
    
    virtual_table.build()
    
class _ConstructorInfo(_MethodInfo):
    virtual_table = COMVirtualTable.from_ancestor(_MethodInfo)
    
    virtual_table.build()
    
_TypeStorage = DelayedTypeStorage()
    
@CStructure.make
class InterfaceMapping(CStructure):
    TargetType: IPointer['_Type']
    interfaceType: IPointer['_Type']
    TargetMethods: SafeArray[_MethodInfo]
    InterfaceMethods: SafeArray[_MethodInfo]
   
class TypeAttributes(INT): 
    VisibilityMask = 7
    NotPublic = 0
    Public = 1
    NestedPublic = 2
    NestedPrivate = 3
    NestedFamily = 4
    NestedAssembly = 5
    NestedFamANDAssem = 6
    NestedFamORAssem = 7
    LayoutMask = 24
    AutoLayout = 0
    SequentialLayout = 8
    ExplicitLayout = 16
    ClassSemanticsMask = 32
    Class = 0
    Interface = 32
    Abstract = 128
    Sealed = 256
    SpecialName = 1024
    Import = 4096
    Serializable = 8192
    StringFormatMask = 0x00030000
    AnsiClass = 0
    UnicodeClass = 0x00010000
    AutoClass = 0x00020000
    CustomFormatClass = 0x00030000
    CustomFormatMask = 0x00c00000
    BeforeFieldInit = 0x00100000
    ReservedMask = 0x00040800
    RTSpecialName = 2048
    TypeAttributes_HasSecurity = 0x00040000
    
class _Type(_MemberInfo):
    virtual_table = COMVirtualTable.from_ancestor(_MemberInfo)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=GUID)
    def Guid(self) -> GUID: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=_Module.PTR(),
        retval_function=RetVal_Dereference)
    def Module(self) -> '_Module': ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_AssemblyMarshaller)
    def Assembly(self) -> '_Assembly': ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=RuntimeTypeHandle)
    def TypeHandle(self) -> RuntimeTypeHandle: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def FullName(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def Namespace(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def AssemblyQualifiedName(self) -> BSTR: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=LONG,
        retval_function=RetVal_GetValue)
    def GetArrayRank(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def BaseType(self) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_ConstructorInfo)),
        retval_function=RetVal_Dereference)
    def GetConstructors(self, bindingAttr: int) -> SafeArray[_ConstructorInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, VARIANT_BOOL, retval_index=3,
        retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def GetInterface(self, name: str, ignoreCase: bool, **kwargs) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_TypeStorage)),
        retval_function=RetVal_Dereference)
    def GetInterfaces(self) -> SafeArray['_Type']: ...
    
    # FindInterfaces
    virtual_table.skip()
    
    # GetEvent, GetEvents, GetEvents_2
    virtual_table.skip_count(3)
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_TypeStorage)),
        retval_function=RetVal_Dereference)
    def GetNestedTypes(self, bindingAttr: int) -> SafeArray['_Type']: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, retval_index=2,
        retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def GetNestedType(self, name: str, bindingAttr: int) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, MemberTypes, BindingFlags, retval_index=2,
        retval_type=_MemberInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetMember(self, name: str, Type: int, bindingAttr: int) -> _MemberInfo: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_MemberInfo)),
        retval_function=RetVal_Dereference)
    def GetDefaultMembers(self) -> SafeArray[_MemberInfo]: ...
    
    # FindMembers
    virtual_table.skip()
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def GetElementType(self) -> '_Type': ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, retval_index=1, retval_type=VARIANT_BOOL)
    def IsSubclassOf(self, c: '_Type') -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT, retval_index=1, retval_type=VARIANT_BOOL)
    def IsInstanceOfType(self, o) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, retval_index=1, retval_type=VARIANT_BOOL)
    def IsAssignableFrom(self, c: '_Type', **kwargs) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, retval_index=1, retval_type=InterfaceMapping.PTR(),
        retval_function=RetVal_Dereference, intermediate_method=True)
    def GetInterfaceMap(self, interfaceType: '_Type', **kwargs) -> InterfaceMapping:
        return self.virt_delegate(TlGetRef(interfaceType))
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, _Binder.PTR(), PTR(SafeArray.typed(_TypeStorage)),
        SafeArray.typed(ParameterModifier),
        retval_index=5, retval_type=PTR(_MethodInfo),
        retval_function=RetVal_Dereference)
    def GetMethod(self, name: str, bindingAttr: int, Binder: _Binder,
                  types: SafeArray['_Type'], modifiers: SafeArray[int]) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, retval_index=2, 
        retval_type=PTR(_MethodInfo),
        retval_function=RetVal_Dereference)
    def GetMethod_2(self, name: str, bindingAttr: int) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_MethodInfo)),
        retval_function=RetVal_Dereference)
    def GetMethods(self, bindingAttr: int) -> SafeArray[_MethodInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, retval_index=2,
        retval_type=_FieldInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetField(self, name: str, bindingAttr: int) -> _FieldInfo: ...
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_FieldInfo)),
        retval_function=RetVal_Dereference)
    def GetFields(self, bindingAttr: int) -> SafeArray[_FieldInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, retval_index=2,
        retval_type=_PropertyInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetProperty(self, name: str, bindingAttr: int) -> _PropertyInfo: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, _Binder.PTR(), PVOID, 
        SafeArray.typed(_TypeStorage), 
        SafeArray.typed(ParameterModifier),
        retval_index=6, retval_type=_PropertyInfo.PTR(),
        retval_function=RetVal_Dereference,
        intermediate_method=True)
    def GetProperty_2(self, name: str, bindingAttr: int,
                      Binder: _Binder, returnType: '_Type',
                      types: SafeArray['_Type'],
                      modifiers: SafeArray[ParameterModifier],
                      **kwargs) -> _PropertyInfo: 
        return self.virt_delegate(name, bindingAttr, Binder, TlGetRef(returnType), types, modifiers)
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_PropertyInfo)),
        retval_function=RetVal_Dereference)
    def GetProperties(self, bindingAttr: int) -> SafeArray[_PropertyInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, retval_index=2,
        retval_type=PTR(SafeArray.typed(_MemberInfo)),
        retval_function=RetVal_Dereference)
    def GetMember_2(self, name: str, bindingAttr: int) -> SafeArray[_MemberInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BindingFlags, retval_index=1,
        retval_type=PTR(SafeArray.typed(_MemberInfo)),
        retval_function=RetVal_Dereference)
    def GetMembers(self, bindingAttr: int) -> SafeArray[_MemberInfo]: ...
    
    # InvokeMember
    virtual_table.skip()
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PVOID,
        retval_function=_TypeMarshaller)
    def UnderlyingSystemType(self) -> '_Type': ...
    
    # 1 overload of InvokeMember
    virtual_table.skip()
    
    @virtual_table.com_function_vbstyle(
        BSTR, BindingFlags, _Binder.PTR(), VARIANT, 
        PTR(SafeArray.typed(VARIANT)), retval_index=5,
        retval_type=VARIANT)
    def InvokeMember_3(self, name: str, invokeAttr: int, Binder: _Binder,
                       Target: Any, args: SafeArray[Any]) -> Any: ...
    
    # 3 overloads of GetConstructor
    virtual_table.skip_count(3)
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_ConstructorInfo)),
        retval_function=RetVal_Dereference)
    def GetConstructors_2(self) -> _ConstructorInfo: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=_ConstructorInfo.PTR(),
        retval_function=RetVal_Dereference)
    def TypeInitializer(self) -> _ConstructorInfo: ...
    
    # 3 overloads of GetMethod
    virtual_table.skip_count(3)
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=_MethodInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetMethod_6(self, name: str) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_MethodInfo)),
        retval_function=RetVal_Dereference)
    def GetMethods_2(self) -> SafeArray[_MethodInfo]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1,
        retval_type=_FieldInfo.PTR(),
        retval_function=RetVal_Dereference)
    def GetField_2(self, name: str) -> _FieldInfo: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_FieldInfo)),
        retval_function=RetVal_Dereference)
    def GetFields_2(self) -> SafeArray[_FieldInfo]: ...
    
    # overload of GetEvent and 5 overloads of GetProperty
    virtual_table.skip_count(7)
    
    # overload of GetProperties
    virtual_table.skip()
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_TypeStorage)),
        retval_function=RetVal_Dereference)
    def GetNestedTypes_2(self) -> SafeArray['_Type']: ...
    
    # 1 overload of GetNestedType and GetMember
    virtual_table.skip_count(2)
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_MemberInfo)),
        retval_function=RetVal_Dereference)
    def GetMembers_2(self) -> SafeArray[_MemberInfo]: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=TypeAttributes,
        retval_function=RetVal_GetValue)
    def Attributes(self) -> int: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNotPublic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPublic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedPublic(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedPrivate(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedFamily(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedAssembly(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedFamANDAssem(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsNestedFamORAssem(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAutoLayout(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsLayoutSequential(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsExplicitLayout(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsClass(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsInterface(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsValueType(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAbstract(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSealed(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsEnum(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSpecialName(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsImport(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsSerializable(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAnsiClass(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsUnicodeClass(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsAutoClass(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsArray(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsByRef(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPointer(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsPrimitive(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsCOMObject(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def HasElementType(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsContextful(self) -> bool: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def IsMarshalByRef(self) -> bool: ...
    
    virtual_table.build()

def _Type_Marshal(value) -> _Type:
    return RetVal_Dereference(i_cast(value, _Type.PTR()))

_TypeMarshaller.marshal_func = _Type_Marshal
_TypeStorage.storaged_type = _Type

class _Evidence(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()

class _AssemblyName(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _ObjRef(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _ObjectHandle(_Object):
    virtual_table = COMVirtualTable.from_ancestor(_Object)
    
    # LifetimeService methods
    virtual_table.skip_count(2)
    
    @virtual_table.com_function_vbstyle(
        _Type.PTR(), retval_index=1, retval_type=PTR(_ObjRef),
        retval_function=RetVal_Dereference, intermediate_method=True)
    def CreateObjRef(self, requestedType: _Type, **kwargs) -> _ObjRef:
        return self.virt_delegate(TlGetRef(requestedType))
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT)
    def Unwrap(self) -> Any: ...
    
    virtual_table.build()
 
class _SerializationInfo(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()

class StreamingContextStates(INT):
    CrossProcess = 1
    CrossMachine = 2
    File = 4
    Persistence = 8
    Remoting = 16
    Other = 32
    Clone = 64
    CrossAppDomain = 128
    All = 255
    
class StreamingContext(CStructure):
    _fields_ = [('m_additionalContext', LPUNKNOWN), 
                ('m_state', StreamingContextStates)]
    
    m_additionalContext: IPointer[IUnknown]
    m_state: int
    
class _Stream(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _FileStream(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _ManifestResourceInfo(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _Version(IDispatch):
    virtual_table = COMVirtualTable.from_ancestor(IDispatch)
    
    virtual_table.build()
    
class _Assembly(_Object):
    virtual_table = COMVirtualTable.from_ancestor(_Object)
    _iid_ = IID('{17156360-2F1A-384A-BC52-FDE93C215C5B}')
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def CodeBase(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def EscapedCodeBase(self) -> BSTR: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(_AssemblyName),
        retval_function=RetVal_Dereference)
    def GetName(self) -> _AssemblyName: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1, 
        retval_type=PTR(_AssemblyName),
        retval_function=RetVal_Dereference)
    def GetName_2(self, copiedName: bool) -> _AssemblyName: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def FullName(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(_MethodInfo),
        retval_function=RetVal_Dereference)
    def EntryPoint(self) -> _MethodInfo: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=_Type.PTR(),
        retval_function=RetVal_Dereference)
    def GetType_2(self, name: str) -> _Type: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, VARIANT_BOOL, retval_index=2, retval_type=_Type.PTR(),
        retval_function=RetVal_Dereference)
    def GetType_3(self, name: str, throwOnError: bool) -> _Type: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_Type)),
        retval_function=RetVal_Dereference)
    def GetExportedTypes(self) -> SafeArray[_Type]: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_Type)),
        retval_function=RetVal_Dereference)
    def GetTypes(self) -> SafeArray[_Type]: ...
    
    @virtual_table.com_function_vbstyle(
        _Type.PTR(), BSTR, retval_index=2,
        retval_type=_Stream.PTR(),
        retval_function=RetVal_Dereference)
    def GetManifestResourceStream(self, Type: _Type, name: str) -> _Stream: ...
    
    @virtual_table.com_function_vbstyle(
        _Type.PTR(), retval_index=1,
        retval_type=_Stream.PTR(),
        retval_function=RetVal_Dereference)
    def GetManifestResourceStream_2(self, name: str) -> _Stream: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=_FileStream.PTR(),
        retval_function=RetVal_Dereference)
    def GetFile(self, name: str) -> _FileStream: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_FileStream)),
        retval_function=RetVal_Dereference)
    def GetFiles(self) -> SafeArray[_FileStream]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1, 
        retval_type=PTR(SafeArray.typed(_FileStream)),
        retval_function=RetVal_Dereference)
    def GetFiles_2(self, getResourceModules: bool) -> SafeArray[_FileStream]: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(BSTR)),
        retval_function=RetVal_Dereference)
    def GetManifestResourceNames(self) -> SafeArray[BSTR]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=PTR(_ManifestResourceInfo),
        retval_function=RetVal_Dereference)
    def GetManifestResourceInfo(self, resourceName: str) -> _ManifestResourceInfo: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def Location(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=_Evidence.PTR(),
        retval_function=RetVal_Dereference)
    def Evidence(self) -> _Evidence: ...
    
    @virtual_table.com_function_vbstyle(
        _Type.PTR(), VARIANT_BOOL, retval_index=2, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes(self, attributeType: _Type,
                            inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=1, 
        retval_type=PTR(SafeArray.typed(VARIANT)),
        retval_function=RetVal_Dereference)
    def GetCustomAttributes_2(self, inherit: bool) -> SafeArray[Any]: ...
    
    @virtual_table.com_function_vbstyle(
        PVOID, VARIANT_BOOL, retval_index=2,
        retval_type=VARIANT_BOOL)
    def IsDefined(self, attributeType: '_Type',
                  inherit: bool) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        _SerializationInfo.PTR(), StreamingContext)
    def GetObjectData(self, info: _SerializationInfo, 
                      Context: StreamingContext): ...
        
    # 2 add/remove ModuleResolve
    virtual_table.skip_count(2)
    
    @virtual_table.com_function_vbstyle(
        BSTR, VARIANT_BOOL, VARIANT_BOOL, retval_index=3, retval_type=_Type.PTR(),
        retval_function=RetVal_Dereference)
    def GetType_4(self, name: str, throwOnError: bool, ignoreCase: bool) -> _Type: ...
    
    @virtual_table.com_function_vbstyle(
        _CultureInfo.PTR(), retval_index=1, retval_type=PVOID,
        retval_function=_AssemblyMarshaller)
    def GetSatelliteAssembly(self, culture: _CultureInfo) -> '_Assembly': ...
    
    @virtual_table.com_function_vbstyle(
        _CultureInfo.PTR(), _Version.PTR(), retval_index=2, retval_type=PVOID,
        retval_function=_AssemblyMarshaller)
    def GetSatelliteAssembly_2(self, culture: _CultureInfo, Version: _Version) -> '_Assembly': ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, SAFEARRAY, retval_index=2,
        retval_type=_Module.PTR(), retval_function=RetVal_Dereference)
    def LoadModule(self, moduleName: str, rawModule: SAFEARRAY) -> _Module: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, SAFEARRAY, SAFEARRAY, retval_index=3,
        retval_type=_Module.PTR(), retval_function=RetVal_Dereference)
    def LoadModule_2(self, moduleName: str, rawModule: SAFEARRAY, rawSymbolStore: SAFEARRAY) -> _Module: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=VARIANT)
    def CreateInstance(self, typeName: str) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, VARIANT_BOOL, retval_index=2, retval_type=VARIANT)
    def CreateInstance_2(self, typeName: str, ignoreCase: bool) -> Any: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, VARIANT_BOOL, BindingFlags, _Binder.PTR(), PTR(SafeArray.typed(VARIANT)),
        _CultureInfo.PTR(), PTR(SafeArray.typed(VARIANT)),
        retval_index=1, retval_type=VARIANT,
        intermediate_method=True)
    def CreateInstance_3(self, typeName: str, ignoreCase: bool,
                       bindingAttr: int, Binder: _Binder, 
                       args: SafeArray[Any],
                       culture: _CultureInfo,
                       activationAttributes: SafeArray[Any], 
                       **kwargs) -> Any: 
        return self.virt_delegate(typeName, ignoreCase,
                                  bindingAttr, TlGetRef(Binder),
                                  args, TlGetRef(culture),
                                  activationAttributes)
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_Module)),
        retval_function=RetVal_Dereference)
    def GetLoadedModules(self) -> SafeArray[_Module]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=0, retval_type=PTR(SafeArray.typed(_Module)),
        retval_function=RetVal_Dereference)
    def GetLoadedModules_2(self, getResourceModules: bool) -> SafeArray[_Module]: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_Module)),
        retval_function=RetVal_Dereference)
    def GetModules(self) -> SafeArray[_Module]: ...
    
    @virtual_table.com_function_vbstyle(
        VARIANT_BOOL, retval_index=0, retval_type=PTR(SafeArray.typed(_Module)),
        retval_function=RetVal_Dereference)
    def GetModules_2(self, getResourceModules: bool) -> SafeArray[_Module]: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=0, retval_type=_Module.PTR(),
        retval_function=RetVal_Dereference)
    def GetModule(self, name: str) -> _Module: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_AssemblyName)),
        retval_function=RetVal_Dereference)
    def GetReferencedAssemblies(self) -> SafeArray[_AssemblyName]: ...

    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def GlobalAssemblyCache(self) -> bool: ...

    virtual_table.build()
    
def _Assembly_Marshal(value) -> _Assembly:
    return RetVal_Dereference(i_cast(value, _Assembly.PTR()))

_AssemblyMarshaller.marshal_func = _Assembly_Marshal

class _AppDomain(_Object):
    virtual_table = COMVirtualTable.from_ancestor(_Object)
    
    # LifetimeService methods
    virtual_table.skip_count(2)
    
    # Evidence
    virtual_table.skip()
    
    # 14 add/remove event handlers
    virtual_table.skip_count(14)
    
    # 9 overloads of DefineDynamicAssembly
    virtual_table.skip_count(9)
    
    @virtual_table.com_function_vbstyle(
        BSTR, BSTR, retval_index=2, retval_type=PTR(_ObjectHandle),
        retval_function=RetVal_Dereference)
    def CreateInstance(self, AssemblyName: str, typeName: str) -> _ObjectHandle: ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, BSTR, retval_index=2, retval_type=PTR(_ObjectHandle),
        retval_function=RetVal_Dereference)
    def CreateInstanceFrom(self, assemblyFile: str, typeName: str) -> _ObjectHandle: ...
    
    # 4 overloads of CreateInstance/CreateInstanceFrom
    virtual_table.skip_count(4)
    
    @virtual_table.com_function_vbstyle(
        _AssemblyName.PTR(), retval_index=1, retval_type=PTR(_Assembly),
        retval_function=RetVal_Dereference, intermediate_method=True)
    def Load(self, assemblyRef: _AssemblyName, **kwargs) -> _Assembly:
        return self.virt_delegate(TlGetRef(assemblyRef))
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=PTR(_Assembly),
        retval_function=RetVal_Dereference)
    def Load_2(self, assemblyString: str) -> _Assembly: ...
    
    # 5 overloads of Load
    virtual_table.skip_count(5)
    
    # ExecuteAssembly([in] BSTR, [in] _Evidence*, [out, retval] long*)
    virtual_table.skip()
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=LONG,
        retval_function=RetVal_GetValue)
    def ExecuteAssembly_2(self, assemblyFile: str) -> int: ...
    
    # ExecuteAssembly([in] BSTR, [in] _Evidence*, [in] SAFEARRAY, [out, retval] long*)
    virtual_table.skip()
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def get_FriendlyName(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def BaseDirectory(self) -> BSTR: ...
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def RelativeSearchPath(self) -> BSTR: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=VARIANT_BOOL)
    def ShadowCopyFiles(self) -> bool: ...
    
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=PTR(SafeArray.typed(_Assembly)),
        retval_function=RetVal_Dereference)
    def GetAssemblies(self) -> SafeArray[_Assembly]: ...
    
    @virtual_table.com_function_vbstyle(BSTR)
    def AppendPrivatePath(self, Path: str): ...
    
    @virtual_table.com_function_vbstyle()
    def ClearPrivatePath(self): ...
    
    @virtual_table.com_function_vbstyle(BSTR)
    def SetShadowCopyPath(self, s: str): ...
    
    @virtual_table.com_function_vbstyle()
    def ClearShadowCopyPath(self): ...
    
    @virtual_table.com_function_vbstyle(BSTR)
    def SetCachePath(self, s: str): ...
    
    @virtual_table.com_function_vbstyle(BSTR, VARIANT)
    def SetData(self, name: str, data): ...
    
    @virtual_table.com_function_vbstyle(
        BSTR, retval_index=1, retval_type=VARIANT)
    def GetData(self, name: str) -> Any: ...
    
    # SetAppDomainPolicy, SetThreadPrincipal, SetPrincipalPolicy, DoCallback
    virtual_table.skip_count(4)
    
    @property
    @virtual_table.com_function_vbstyle(
        retval_index=0, retval_type=BSTR)
    def DynamicDirectory(self) -> BSTR: ...
    
    virtual_table.build()

#
# .NET/Python Interop Executive
#

class ObjectMeta(type):
    _properties_static: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _indexers_static: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _methods_static: ClassVar[dict[str, set[_MethodInfo] | _MethodInfo]] = {}
    _fields_static: ClassVar[dict[str, set[_FieldInfo] | _FieldInfo]] = {}
    _properties: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _methods: ClassVar[dict[str, set[_MethodInfo] | _MethodInfo]] = {}
    _fields: ClassVar[dict[str, set[_FieldInfo] | _FieldInfo]] = {}
    
    _type: ClassVar[_Type]
    
    def __getattr__(cls, name: str):
        field_info = cls._fields_static.get(name, None)
        
        if field_info is not None:
            try:
                value = field_info.GetValue(None)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        property_info = cls._indexers_static.get(name, None)
        
        if property_info is not None:
            return MethodEngine.PropertyIndexer(property_info, cls._type)
        
        property_info = cls._properties_static.get(name, None)
        
        if property_info is not None:
            try:
                value = property_info.GetValue(None, None)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        method_info = cls._methods_static.get(name, None)
        
        if method_info is not None:
            return MethodEngine.Method(method_info, cls._type)
        
        raise AttributeError(name)

CData = c_int.__base__.__base__

class MarshalEngine:
    class Record(win.com.dispatch.Record):
        def __getattr__(self, name: str) -> Any:
            return MarshalEngine.marshal_value(super().__getattr__(name))
        
        def __setattr__(self, name: str, value: Any) -> Any:
            super().__setattr__(name, MarshalEngine.python_to_variant(value))
            
        def __str__(self) -> str:
            mscorlib = Object._ensure_mscorlib()
            return mscorlib.Convert.ToString(self)
        
        @classmethod
        def construct(cls, record_info: IRecordInfo) -> 'Record':
            guid = Record.guid_from_record(record_info)
            cached_record = Record._record_cache.get(guid, None)
            
            if guid is not None:
                return cached_record
            
            class RecordExt(MarshalEngine.Record):
                _fields_ = Record.fields_from_record(record_info)
                _size_ = Record.size_from_record(record_info)
                _record_info_ = record_info
                _guid_ = guid
            
            RecordExt.__name__ = Record.name_from_record(record_info)
            Record._record_cache[guid] = RecordExt
            
            return RecordExt
    
    @classmethod
    def deallocate_safearray(cls, sa: SafeArray):
        for value in sa.value:
            if isinstance(value, BSTR):
                SysFreeString(value)
            elif isinstance(value, VARIANT):
                if value.vt == VT_BSTR:
                    SysFreeString(value.bstrVal)
                elif value.vt == VT_ARRAY:
                    variant_get_value(value)
            elif isinstance(value, SafeArray):
                cls.deallocate_safearray(value)
        SafeArrayDestroy(sa.ref())
    
    @classmethod
    def python_to_variant(cls, obj: Any) -> VARIANT:
        obj_new = obj
        
        if not isinstance(obj, VARIANT):
            obj_new = Variant()
                        
            if isinstance(obj, Object):
                obj_new.value = obj._object
                obj_new.vt = VT_UNKNOWN
            elif isinstance(obj, type) and issubclass(obj, Object):
                obj_new.value = obj._type
                obj_new.vt = VT_UNKNOWN
            elif isinstance(obj, IUnknown):
                obj_new.value = obj
                obj_new.vt = VT_UNKNOWN
            else:
                obj_new.value = obj
        
        return i_cast_structure(obj_new, VARIANT)
    
    @classmethod
    def marshal_lpUnknown(cls, lpUnknown: IPointer[IUnknown]) -> 'Object':
        netObj = TlQueryInterface(lpUnknown.contents, _Object)
        return Object.construct(netObj.GetType()).from_object(netObj)
    
    @classmethod
    def marshal_unknown(cls, unknown: IUnknown) -> 'Object':
        netObj = TlQueryInterface(unknown, _Object)
        return Object.construct(netObj.GetType()).from_object(netObj)
    
    @classmethod
    def marshal_dispatch(cls, dispatch: Dispatch) -> 'Object':
        return cls.marshal_unknown(dispatch._disp)
    
    @classmethod
    def marshal_type(cls, value: Any, type_str: str) -> Any:
        return cls.MAP_TYPE_TO_FUNCTION.get(type_str, lambda Val: Val)(value)

    @classmethod
    def python_to_safearray(cls, iterable: Sequence[Any]) -> SafeArray:
        if not iterable: return NULL
        first = iterable[0]
        
        if isinstance(first, (int, INT)):
            item_type = c_int
        elif isinstance(first, CData):
            item_type = type(first)
        elif isinstance(first, str):
            item_type = BSTR
        else:
            raise TypeError(type(first))
        
        result_iterable = []
        
        for value in iterable:
            if item_type is BSTR:
                result_iterable.append(BSTR.new(value))
            else:
                result_iterable.append(value)
            
        sa = SafeArray.typed(item_type).create(result_iterable)
        return sa

    @classmethod
    def marshal_safearray(cls, value: SafeArray[WT]) -> list:
        result_list = []
        
        if value._vt_ == VT_UNKNOWN:
            for unknown in value.value:
                obj_itf = TlQueryInterface(unknown, _Object)
                obj = Object.construct(obj_itf.GetType()).from_object(obj_itf)
                result_list.append(obj)
        else:
            result_list = value.value
        
        return result_list

    @classmethod
    def marshal_record(cls, record: win.com.dispatch.Record) -> Record:
        return MarshalEngine.Record.construct(record._record_info_)(record.allocation_base)

    @classmethod
    def marshal_bstr(cls, bstr: BSTR) -> str:
        return TlAccessOAStringAndFree(bstr)

    @classmethod
    def marshal_value(cls, value: WT) -> Any:
        if PtrUtil.is_pointer(value):
            ptr_type = PtrUtil.get_type(value)
            if issubclass(ptr_type, IUnknown):
                return cls.marshal_lpUnknown(value)
        elif isinstance(value, IUnknown):
            return cls.marshal_unknown(value)
        elif isinstance(value, Dispatch):
            return cls.marshal_dispatch(value)
        elif isinstance(value, SafeArray):
            return cls.marshal_safearray(value)
        elif isinstance(value, Record):
            return cls.marshal_record(value)
        elif isinstance(value, BSTR):
            return cls.marshal_bstr(value)
        elif isinstance(value, VARIANT):
            return variant_get_value(value)
                
        return value

class MethodEngine:
    _internal_avoid_CE2NET: bool = False
    
    @classmethod
    def COMError_to_NET_exception(cls, ce: COMError) -> Exception:
        if cls._internal_avoid_CE2NET: return ce
        Object._ensure_mscorlib(f'MSCORLIB is not initialized, but underlying exception was thrown.\n'
                                f'Raw exception object: {ce}')
        mscorlib = Object._saved_mscorlib_for_interop
        
        try:
            cls._internal_avoid_CE2NET = True
            netException = mscorlib.System.Runtime.InteropServices.Marshal.GetExceptionForHR(ce.hresult)
        finally:
            cls._internal_avoid_CE2NET = False
        
        if netException is None:
            return ce
        
        return netException
    
    @classmethod
    def is_homogeneous_lengths(cls, method_infos: set[_MethodInfo]) -> bool:
        check_list: list[int] = []
        
        for method_info in method_infos:
            parameters = method_info.GetParameters()
            length = len(parameters)
            
            if length in check_list:
                return False
            
            check_list.append(length)
    
        return True
    
    @classmethod
    def build_length_mapping_dict(cls, method_infos: set[_MethodInfo]) -> dict[int, _MethodInfo]:
        length_mapping: dict[int, _MethodInfo] = {}
        
        for method_info in method_infos:
            parameters = method_info.GetParameters()
            length_mapping[len(parameters)] = method_info
            
        return length_mapping
    
    class Method:
        method_info: _MethodInfo | set[_MethodInfo]
        bound_object: 'Object'
        bound_type: _Type
        is_ctor: bool
        
        def __init__(self, method_info: _MethodInfo, bound_type: _Type,
                     bound_object: Any = None, is_ctor: bool = False):
            self.bound_object = bound_object
            self.method_info = method_info
            self.bound_type = bound_type
            self.is_ctor = is_ctor
        
        def __call__(self, *args, **kwargs) -> Any:
            mscorlib = Object._ensure_mscorlib()
            method_info = self.method_info
            
            if isinstance(method_info, set):
                method_info, type_scheme = MethodEngine.resolve_call(args, method_info)
            
            bound_object = self.bound_object
            if bound_object is not None:
                bound_object = bound_object._object
            
            if args:
                arguments = []
                
                for arg in args:
                    if isinstance(arg, (list, tuple)):
                        sa = MarshalEngine.python_to_safearray(arg)
                        arg_new = Variant()
                        arg_new.value = sa
                    else:
                        arg_new = MarshalEngine.python_to_variant(arg)
                        
                    arguments.append(arg_new)
                
                arguments = SafeArray.typed(VARIANT).create(arguments)
            else:
                arguments = NULL
            
            try:
                if self.is_ctor:
                    return_value = mscorlib.System.Activator.CreateInstance(self.bound_type, arguments)
                elif method_info is not None:
                    return_value = method_info.Invoke_3(bound_object, arguments)
                else:
                    method_infos: set[_MethodInfo] | _MethodInfo = self.method_info
                    
                    if isinstance(method_infos, set):
                        method_info = list(method_infos)[0]
                    else:
                        method_info = method_infos
                        
                    name = TlAccessOAStringAndFree(method_info.name)
                    
                    binding_attr = BindingFlags.Public
                    
                    if bound_object:
                        binding_attr |= BindingFlags.Instance
                    else:
                        binding_attr |= BindingFlags.Static
                    if self.is_ctor:
                        binding_attr |= BindingFlags.CreateInstance
                    else:
                        binding_attr |= BindingFlags.InvokeMethod
                    
                    return_value = self.bound_type.InvokeMember_3(
                        name, binding_attr, NULL, bound_object, arguments)
                    
                    if arguments:
                        MarshalEngine.deallocate_safearray(arguments)
                            
            except COMError as ce:
                exc = MethodEngine.COMError_to_NET_exception(ce)
                if isinstance(exc, Object):
                    if exc._type_name == 'System.Reflection.TargetInvocationException':
                        raise exc.InnerException from None
                raise exc from None
            
            return MarshalEngine.marshal_value(return_value)
    
    class PropertyIndexer:
        property_info: set[_PropertyInfo] | _PropertyInfo
        bound_object: 'Object'
        bound_type: _Type
        
        def __init__(self, property_info: set[_PropertyInfo] | _PropertyInfo,
                     bound_type: _Type, bound_object: 'Object' = None):
            self.property_info = property_info
            self.bound_object = bound_object
            self.bound_type = bound_type
            
        def operate(self, indexes, value=None):
            if not isinstance(indexes, (tuple, list)):
                indexes = (indexes,)
                
            bound_object = self.bound_object
            if bound_object is not None:
                bound_object = bound_object._object
            
            variants = []
            for index in indexes:
                variant = MarshalEngine.python_to_variant(index)
                variants.append(variant)
            
            property_info = self.property_info
            if isinstance(property_info, set):
                name = list(property_info)[0].name
                
                flags = BindingFlags.Public
                
                if bound_object is None:
                    flags |= BindingFlags.Static
                else:
                    flags |= BindingFlags.Instance
                    
                if value is not None:
                    variant = MarshalEngine.python_to_variant(value)
                    variants.append(variant)
                
            sa = SafeArray.typed(VARIANT).create(variants)
            
            try:
                if value is None:
                    if isinstance(property_info, set):
                        result = self.bound_type.InvokeMember_3(name, flags | BindingFlags.GetProperty, 
                                                                NULL, bound_object, sa)
                    else:
                        result = property_info.GetValue(bound_object, sa)
                else:
                    if isinstance(property_info, set):
                        result = self.bound_type.InvokeMember_3(name, flags | BindingFlags.SetProperty,
                                                                NULL, bound_object, sa)
                    else:
                        property_info.SetValue(bound_object, value, sa)
            except COMError as ce:
                exc = MethodEngine.COMError_to_NET_exception(ce)
                if isinstance(exc, Object):
                    if exc._type_name == 'System.Reflection.TargetInvocationException':
                        raise exc.InnerException from None
                raise exc from None
                
            MarshalEngine.deallocate_safearray(sa)
            
            if value is None:
                return MarshalEngine.marshal_value(result)
        
        def __getitem__(self, indexes: tuple[Any] | Any) -> Any:
            return self.operate(indexes)
        
        def __setitem__(self, indexes: tuple[Any] | Any, value: Any):
            self.operate(indexes, value)
    
    @classmethod
    def resolve_call(cls, args: list, methods: list[_MethodInfo]) -> tuple[_MethodInfo, list[str]]:
        if cls.is_homogeneous_lengths(methods): # optimization
            length_mapping_dict = cls.build_length_mapping_dict(methods)
            return (length_mapping_dict[len(args)], None)

        return (None, None)

SafeArray.release_delay_execution()

def _lightweight_issubclass(T_1: _Type, T_2: str) -> bool:
    base_class = T_1.BaseType
    
    if base_class is None:
        return False

    base_name = TlAccessOAStringAndFree(base_class.FullName)
    if base_name != T_2:
        return _lightweight_issubclass(base_class, T_2)
    
    return True

COR_E_DIVIDEBYZERO = 0x80020012

COR_E_NULLREFERENCE = 0x80004003

COR_E_ACCESSDENIED = 0x80070005
COR_E_ARGUMENT = 0x80070057
COR_E_BADIMAGEFORMAT = 0x8007000B
COR_E_OUTOFMEMORY = 0x8007000E
COR_E_ARITHMETIC = 0x80070216

COR_E_TYPEUNLOADED = 0x80131013

COR_E_SYSTEM = 0x80131501
COR_E_ARGUMENTOUTOFRANGE = 0x80131502
COR_E_ARRAYTYPEMISMATCH = 0x80131503
COR_E_CONTEXTMARSHAL = 0x80131504
COR_E_TIMEOUT = 0x80131505
COR_E_FIELDACCESS = 0x80131507
COR_E_INDEXOUTOFRANGE = 0x80131508
COR_E_MEMBERACCESS = 0x8013151A
COR_E_METHODACCESS = 0x80131510
COR_E_MISSINGFIELD = 0x80131511
COR_E_MISSINGMEMBER = 0x80131512
COR_E_MISSINGMETHOD = 0x80131513
COR_E_MULTICASTNOTSUPPORTED = 0x80131514
COR_E_CANNOTUNLOADAPPDOMAIN = 0x80131015
COR_E_OVERFLOW = 0x80131516
COR_E_RANK = 0x80131517
COR_E_TYPELOAD = 0x80131522
COR_E_DLLNOTFOUND = 0x80131524
COR_E_NOTFINITENUMBER = 0x80131528
COR_E_DUPLICATEWAITOBJECT = 0x80131529
COR_E_FORMAT = 0x80131537
COR_E_PLATFORMNOTSUPPORTED = 0x80131539
COR_E_INVALIDPROGRAM = 0x8013153A
COR_E_TARGET = 0x80131603
COR_E_TARGETINVOCATION = 0x80131604
COR_E_IO = 0x80131620
COR_E_FILELOAD = 0x80131621
COR_E_OBJECTDISPOSED = 0x80131622

class Object(metaclass=ObjectMeta):
    """
    Class representing .NET object
    """
    
# Static Fields
    _constructors: ClassVar[dict[str, set[_ConstructorInfo] | _ConstructorInfo]] = {}
    _properties_static: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _properties: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _methods_static: ClassVar[dict[str, set[_MethodInfo] | _MethodInfo]] = {}
    _indexers: ClassVar[dict[str, set[_PropertyInfo] | _PropertyInfo]] = {}
    _fields_static: ClassVar[dict[str, set[_FieldInfo] | _FieldInfo]] = {}
    _methods: ClassVar[dict[str, set[_MethodInfo] | _MethodInfo]] = {}
    _fields: ClassVar[dict[str, set[_FieldInfo] | _FieldInfo]] = {}
    _saved_mscorlib_for_interop: ClassVar['Assembly'] = None
    _saved_assembly_for_interop: ClassVar['Assembly'] = None
    _saved_system_for_interop: ClassVar['Assembly'] = None
    
    _registered_types: dict[str, type['Object']] = {}
    _constructor_info: dict[str, ]
    _type: ClassVar[_Type] = None
    _is_collection: bool = False
    _is_dictionary: bool = False
    _is_enumerator: bool = False
    _is_enumerable: bool = False
    _is_exception: bool = False
    _is_delegate: bool = False
    _is_list: bool = False
    _type_name: str = ''
    
# Class Fields
    _object: _Object
    _released: bool
    
# Constructors
    @classmethod
    def construct(cls, netType: _Type) -> type['Object']:
        name = TlAccessOAStringAndFree(netType.FullName)
        
        registered_types = cls._registered_types
        Object_NET = registered_types.get(name, None)
        
        if Object_NET is not None:
            return Object_NET
        
        is_collection = not not netType.GetInterface('System.Collections.ICollection', False)
        is_dictionary = not not netType.GetInterface('System.Collections.IDictionary', False)
        is_enumerator = not not netType.GetInterface('System.Collections.IEnumerator', False)
        is_enumerable = not not netType.GetInterface('System.Collections.IEnumerable', False)
        is_list = not not netType.GetInterface('System.Collections.IList', False)
        
        is_exception = _lightweight_issubclass(netType, 'System.Exception')
        is_delegate = _lightweight_issubclass(netType, 'System.Delegate')
        
        extra_ancestors = []
        
        if is_exception:
            extra_ancestors.append(Exception)
        
        class Object_NET(Object, *extra_ancestors):
            _constructors = {}
            
            _properties_static = {}
            _properties = {}
            
            _methods_static = {}
            _methods = {}
            
            _fields_static = {}
            _fields = {}
            
            _is_collection = is_collection
            _is_dictionary = is_dictionary
            _is_enumerable = is_enumerable
            _is_enumerator = is_enumerator
            _is_exception = is_exception
            _is_delegate = is_delegate
            _is_list = is_list
            
            _type_name = name
            _type = None
        
        Object_NET.__qualname__ = name
        Object_NET.initialize_type(netType)
        
        registered_types[name] = Object_NET
        
        return Object_NET

    def __iter__(self):
        if self._is_enumerator:
            return self
        if self._is_enumerable:
            return iter(self.GetEnumerator())
        raise TypeError(self._type_name)
    
    def __next__(self):
        if not self._is_enumerator:
            raise TypeError(self._type_name)
        
        if not self.MoveNext():
            raise StopIteration
        
        return self.Current
    
    def __getitem__(self, obj):
        if 'Item' not in self._indexers:
            raise NotImplementedError()
        
        return self.Item[obj]
    
    def __contains__(self, obj) -> bool:
        if not self._is_list and not self._is_dictionary:
            raise NotImplementedError()
        
        return self.Contains(obj)
    
    def __delitem__(self, obj):
        if self._is_list:
            self.RemoveAt(obj)
        elif self._is_dictionary:
            self.Remove(obj)
            
        raise NotImplementedError()
        
    def __setitem__(self, obj, value):
        if 'Item' not in self._indexers:
            raise NotImplementedError()
        
        self.Item[obj] = value
        
    def __len__(self) -> int:
        if not self._is_collection:
            raise NotImplementedError()
    
        return self.Count
    
    def __bool__(self) -> bool:
        if self._is_collection:
            return not not len(self)
        return True
    
    def __add__(self, obj) -> Any:
        if self._is_delegate:
            mscorlib = self._ensure_mscorlib()
            if isinstance(obj, CFuncPtr):
                obj = mscorlib.System.Runtime.InteropServices.GetDelegateForFunctionPointer(PtrUtil.get_address(obj), self._type)
            return mscorlib.System.Delegate.Combine(self, obj)
        return self.op_Addition(obj)
    
    def __sub__(self, obj) -> Any:
        if self._is_delegate:
            mscorlib = self._ensure_mscorlib()
            if isinstance(obj, CFuncPtr):
                obj = mscorlib.System.Runtime.InteropServices.GetDelegateForFunctionPointer(PtrUtil.get_address(obj), self._type)
            return mscorlib.System.Delegate.Remove(self, obj)
        return self.op_Subtraction(obj)
    
    def __mul__(self, obj) -> Any:
        return self.op_Multiply(obj)
    
    def __truediv__(self, obj) -> Any:
        return self.op_Division(obj)
    
    def __mod__(self, obj) -> Any:
        return self.op_Modulus(obj)
    
    def __and__(self, obj) -> Any:
        return self.op_BitwiseAnd(obj)
    
    def __or__(self, obj) -> Any:
        return self.op_BitwiseOr(obj)
    
    def __xor__(self, obj) -> Any:
        return self.op_BitwiseXor(obj)
    
    def __lshift__(self, obj) -> Any:
        return self.op_LeftShift(obj)
    
    def __rshift__(self, obj) -> Any:
        return self.op_RightShift(obj)
    
    @classmethod
    def _ensure_mscorlib(cls, message: str = None) -> 'Assembly':
        mscorlib = cls._saved_mscorlib_for_interop
        
        if mscorlib is None:
            if message is None:
                message = 'MSCORLIB is not initialized.'
            raise RuntimeError(message)
        
        return mscorlib

    @classmethod
    def from_object(cls, netObj: _Object) -> 'Object':
        old_type = cls._type
        cls._type = None
        
        self: Self = cls.__new__(cls)
        if cls._is_exception:
            Exception.__init__(self)
        
        cls._type = old_type
        del old_type
        
        builtins.object.__setattr__(self, '_released', False)
        builtins.object.__setattr__(self, '_object', netObj)
        
        if cls._type is None:
            cls.initialize_type(netObj.GetType())
        
        return self
    
    @classmethod
    def initialize_type(cls, typeObj: _Type):
        if cls._type is None:
            Object._registered_types[cls._type_name] = cls
            cls._type_name = TlAccessOAStringAndFree(typeObj.FullName)
            cls._type = typeObj
            
            # methods, fields and properties
            methods_static = typeObj.GetMethods(BindingFlags.Public | BindingFlags.Static)
            methods = typeObj.GetMethods(BindingFlags.Public | BindingFlags.Instance)
            
            fields_static = typeObj.GetFields(BindingFlags.Public | BindingFlags.Static)
            fields = typeObj.GetFields(BindingFlags.Public | BindingFlags.Instance)
            
            properties_static = typeObj.GetProperties(BindingFlags.Public | BindingFlags.Static)
            properties = typeObj.GetProperties(BindingFlags.Public | BindingFlags.Instance)
            
            constructors = typeObj.GetConstructors(BindingFlags.Public | BindingFlags.Instance)
            
            # build constructors, methods, fields and properties reflection lists
            cls._build_reflection_list(constructors, '_constructors')
            
            cls._build_reflection_list(methods_static, '_methods_static')
            cls._build_reflection_list(methods, '_methods')
            
            cls._build_reflection_list(fields_static, '_fields_static')
            cls._build_reflection_list(fields, '_fields')
            
            cls._build_reflection_list(properties_static, '_properties_static')
            cls._build_reflection_list(properties, '_properties')
    
    @classmethod
    def _add_to_reflection_list(cls, dictionary: dict[str, set[_MemberInfo] | _MemberInfo], 
                                name: str, member: _MemberInfo):
        value = dictionary.get(name, None)
        # add member to reflection list
        if value is None:
            dictionary[name] = member
        elif isinstance(value, set):
            value.add(member)
        else:
            dictionary[name] = {value, member}
    
    @classmethod
    def _build_reflection_list(cls, reflection_list: list[_MemberInfo],
                               dictionary_attr: str):
        dictionary: dict[str, set[_MemberInfo] | _MemberInfo] = getattr(cls, dictionary_attr)
        
        for member in reflection_list:
            # get the member name
            name = TlAccessOAStringAndFree(member.name)
            typename = TlAccessOAStringAndFree(member.ReflectedType.FullName)
            
            if typename != cls._type_name:
                continue
            
            if member.MemberType == MemberTypes.Property:
                property_info: _PropertyInfo = member
                
                index_parameters = property_info.GetIndexParameters()
                
                if index_parameters.dimensions == 1:
                    is_supporting_indexer = not not len(index_parameters)
                else:
                    is_supporting_indexer = False
                    
                if is_supporting_indexer:
                    indexers_attr = '_indexers'
                    if dictionary_attr.endswith('_static'):
                        indexers_attr += '_static'
                        
                    dictionary_indexers = getattr(cls, indexers_attr)
                    
                    cls._add_to_reflection_list(
                        dictionary_indexers, name, member)
                    
                    continue
            
            cls._add_to_reflection_list(dictionary, name, member)
            
    def __new__(cls, *args):
        if cls._type is None:
            if cls._is_exception:
                return Exception.__new__(cls)
            return builtins.object.__new__(cls)
        
        cls._ensure_type()
        
        if cls._is_delegate and args and isinstance(args[0], CFuncPtr):
            mscorlib = cls._ensure_mscorlib()
            return mscorlib.System.Runtime.InteropServices.GetDelegateForFunctionPointer(PtrUtil.get_address(obj), cls)
        
        assembly = cls._type.Assembly
            
        if not args:
            try:
                instance = assembly.CreateInstance(cls._type_name)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
        else:
            instance = MethodEngine.Method(cls._constructors['.ctor'], bound_type=cls._type, 
                                           is_ctor=True)(*args)
            
        assembly.Release()
        
        instance = MarshalEngine.marshal_value(instance)
        
        if isinstance(instance, Object):
            if instance._is_exception:
                Exception.__init__(instance, str(instance))
                
        return instance
    
# String & Repr
    def __str__(self) -> str:
        try:
            if self._is_exception:
                string = str(self._object)
                return string.replace(f'{self._type_name}: ', '')
            return str(self._object)
        except COMError as ce:
            exc = MethodEngine.COMError_to_NET_exception(ce)
            if isinstance(exc, Object):
                if exc._type_name == 'System.Reflection.TargetInvocationException':
                    raise exc.InnerException from None
            raise exc from None
    
    def __repr__(self) -> str:
        return repr(self._object)

# Hashing
    def __hash__(self) -> int:
        return hash(self._object)

# Destructors
    def __del__(self):
        if not self._released:
            self.Release()
        
    def _release_info(self, info_attr: str):
        infos: dict[str, set[_MemberInfo] | _MemberInfo]
        infos = getattr(self, info_attr)
        
        for info in infos.values():
            if isinstance(info, set):
                for info in info:
                    info.Release()
            else:
                info.Release()
        
        builtins.object.__setattr__(self, info_attr, {})
        
    def Release(self):
        dbg_trace(provider, f'Released {self}')
        
        self._object.Release()
        self._type.Release()
        builtins.object.__setattr__(self, '_released', True)
        
        self._release_info('_constructors')
        self._release_info('_methods')
        self._release_info('_methods_static')
        self._release_info('_fields')
        self._release_info('_fields_static')
        self._release_info('_properties')
        self._release_info('_properties_static')
        self._release_info('_indexers')
    
# Type System checks
    @classmethod
    def _ensure_type(cls):
        if cls._type is None:
            return RuntimeError('Object type is not initialized.')

    @classmethod
    def __instancecheck__(cls, value):
        cls._ensure_type()
        
        if isinstance(value, _Object):
            return cls._type.IsInstanceOfType(value)
        
        if isinstance(value, Object):
            return cls._type.IsInstanceOfType(value._object)
        
        return False
    
    @classmethod
    def __subclasscheck__(cls, value):
        cls._ensure_type()
        
        if not isinstance(value, type):
            return None
        
        if issubclass(value, _Type):
            return cls._type.IsSubclassOf(value)
        
        if issubclass(value, Object):
            value._ensure_type()
            
            return cls._type.IsSubclassOf(value._type)
        
        return False
    
    def __getattr__(self, name: str):
        field_info = self._fields.get(name, None)
        
        if field_info is not None:
            try:
                value = field_info.GetValue(self._object)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        property_info = self._indexers.get(name, None)
        
        if property_info is not None:
            return MethodEngine.PropertyIndexer(property_info, self._type, bound_object=self)
        
        property_info = self._properties.get(name, None)
        
        if property_info is not None:
            try:
                value = property_info.GetValue(self._object, None)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        method_info = self._methods.get(name, None)
        
        if method_info is not None:
            return MethodEngine.Method(method_info, self._type, bound_object=self)
        
        raise AttributeError(name)
    
    def __setattr__(self, name: str, value: Any):
        try:
            builtins.object.__getattribute__(self, name)
            builtins.object.__setattr__(self, name, value)
            return 
        except:
            pass
        
        field_info = self._fields.get(name, None)
        
        if field_info is not None:
            try:
                field_info.SetValue_2(self._object, MarshalEngine.python_to_variant(value))
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        property_info = self._properties.get(name, None)
        
        if property_info is not None:
            try:
                property_info.SetValue(self._object, MarshalEngine.python_to_variant(value), NULL)
            except COMError as ce:
                raise MethodEngine.COMError_to_NET_exception(ce) from None
            return MarshalEngine.marshal_value(value)
        
        raise AttributeError(name)
    
def typeof(cls) -> 'Object':
    return Object.construct(cls._type.GetType()).from_object(cls._type)
    
class Assembly:
    """
    Class representing .NET assembly.
    """
    
    _assembly: _Assembly
    
    def __init__(self, assembly: _Assembly | Object):
        if isinstance(assembly, Object):
            assembly = TlQueryInterface(assembly._object, _Assembly)
        if 'mscorlib' in TlAccessOAStringAndFree(assembly.FullName):
            Object._saved_mscorlib_for_interop = self
        self._assembly = assembly
    
    def BuildNamespace(self, namespace: str) -> Any:
        if not namespace:
            return self
        
        components = namespace.split('.')
        parent_storage = self
        
        for component in components:
            parent_storage_temp = getattr(parent_storage, component, None)
            
            if parent_storage_temp is None:
                class Namespace(INamespace): ...
                
                Namespace.__name__ = component
                setattr(parent_storage, component, Namespace)
                parent_storage = Namespace
            else:
                parent_storage = parent_storage_temp
                
        return parent_storage
    
    def Initialize(self):
        try:
            exported_types = self._assembly.GetExportedTypes().value
            
            for exported_type in exported_types:
                namespace = TlAccessOAStringAndFree(exported_type.Namespace)
                name = TlAccessOAStringAndFree(exported_type.name).replace('`', '_P')
                
                exported_type = Object.construct(exported_type)
                namespace = self.BuildNamespace(namespace)
                setattr(namespace, name, exported_type)
        except COMError as ce:
            raise MethodEngine.COMError_to_NET_exception(ce) from None
       
class DispMap:
    dispid2method_map: dict[int, str]
    method2dispid_map: dict[str, int]
    
    def __init__(self, disp_map: dict):
        self.dispid2method_map = {v: k for k, v in disp_map.items()}
        self.method2dispid_map = disp_map
        
    def get_dispid(self, method: str) -> int:
        return self.method2dispid_map.get(method, DISPID_UNKNOWN)
    
    def get_method(self, dispid: int) -> str:
        return self.dispid2method_map.get(dispid)
       
class InteropObject(CComObject, _Object, IManagedObject, IProvideClassInfo):
    IManagedObject_virtual_table = (COMVirtualTable.from_ancestor(IManagedObject)
                                    .with_fieldname('IManagedObject_vtable'))
    IProvideClassInfo_virtual_table = (COMVirtualTable.from_ancestor(IProvideClassInfo)
                                       .with_fieldname('IProvideClassInfo_vtalbe'))
    _com_map_ = [
        (IDispatch, IDispatch.virtual_table),
        (_Object, _Object.virtual_table),
        (IManagedObject, IManagedObject_virtual_table)
    ]
    _fields_ = IManagedObject_virtual_table.build() + IProvideClassInfo_virtual_table.build()
    _disp_map_ = DispMap({
        'ToString': 0x60020000,
        'Equals': 0x60020001,
        'GetHashCode': 0x60020002,
        'GetType': 0x60020003
    })
    
    _aggregated_IManagedObject: IManagedObject
    
    hashing_attributes: tuple[str, ...]
    aggregated_obj: _Object
    type_object: _Type
            
    def __init__(self, aggregated_obj: _Object, hashing_attributes: tuple[str, ...], type_object: _Type):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        self.initialize_vtable(self.IProvideClassInfo_virtual_table)
        self.initialize_vtable(self.IManagedObject_virtual_table)
        
        # IProvideClassInfo
        self.set_vtable_on_ctx(self.IProvideClassInfo_virtual_table)
        self.implement(self.GetClassInfo)
        
        # IManagedObject
        self.set_vtable_on_ctx(self.IManagedObject_virtual_table)
        self.implement(self.GetSerializedBuffer)
        self.implement(self.GetObjectIdentity)
        
        # IDispatch
        self.set_vtable_on_ctx(IDispatch.virtual_table)
        self.implement(self.GetTypeInfoCount)
        self.implement(self.GetTypeInfo)
        self.implement(self.GetIDsOfNames)
        self.implement(self.Invoke)
        
        # _Object
        self.set_vtable_on_ctx(_Object.virtual_table)
        self.implement(_Object.ToString)
        self.implement(_Object.Equals)
        self.implement(_Object.GetHashCode)
        self.implement(_Object.GetType)
        
        self.hashing_attributes = hashing_attributes
        self.type_object = type_object
        
        self._aggregated_IManagedObject = TlQueryInterface(aggregated_obj, IManagedObject)
        self.aggregated_obj = aggregated_obj
    
    #
    # IProvideClassInfo
    #
    
    def GetClassInfo_Impl(self, ppTI: IDoublePtr[ITypeInfo]) -> int:
        if not ppTI:
            self.dbg_trace(provider, 'ppTI == NULL!')
            return E_POINTER
        
        TlWritePvToPpv(ppTI, NULL)
        self.dbg_trace(provider, 'E_NOTIMPL')
        return E_NOTIMPL
    
    #   
    # IManagedObject
    #
    
    def GetSerializedBuffer_Impl(self, pBSTR: IPointer[BSTR]) -> int:
        self.dbg_trace(provider)
        return self._aggregated_IManagedObject.GetSerializedBuffer(pBSTR)
    
    def GetObjectIdentity_Impl(self, pBSTRGUID: IPointer[BSTR], pAppDomainID: PINT, pCCW: PINT) -> int:
        self.dbg_trace(provider)
        return self._aggregated_IManagedObject.GetObjectIdentity(pBSTRGUID, pAppDomainID, pCCW)
    
    #    
    # IDispatch
    #
    
    def GetTypeInfoCount_Impl(self, pnCount: IPointer[UINT]) -> int:
        if not pnCount:
            self.dbg_trace(provider, 'pnCount == NULL!')
            return S_OK
        
        TlAccessPpv(pnCount, UINT).value = 0
        self.dbg_trace(provider, '*pnCount=0')
        return S_OK
    
    def GetTypeInfo_Impl(self, iTInfo, lcid, ppTInfo):
        self.dbg_trace(provider, 'E_NOTIMPL')
        return E_NOTIMPL
    
    def GetIDsOfNames_Impl(self, riid: IPointer[IID],
                      rgszNames: IPointer[LPOLESTR], 
                      cNames: int, lcid: int, 
                      rgDispId: IPointer[DISPID], **kwargs):
        if not rgszNames:
            self.dbg_trace(provider, 'rgszNames == NULL!')
            return E_POINTER
        
        if not rgDispId:
            self.dbg_trace(provider, 'rgDispId == NULL!')
            return E_POINTER
        
        self.dbg_trace(provider, 'Begin')
        hr = S_OK
        
        for i in range(cNames):
            name = rgszNames[i]
            
            dispID = self._disp_map_.get_dispid(name)
            rgDispId[i] = dispID
            
            if dispID == DISPID_UNKNOWN:
                self.dbg_trace(provider, f'DispMethod {name} Failed')
                hr = DISP_E_UNKNOWNNAME
            else:
                self.dbg_trace(provider, f'DispMethod {name} Ok')
        
        self.dbg_trace(provider, 'End')
        return hr
    
    def Invoke_Impl(self, dispIdMember: int, riid: IPointer[IID], 
                    lcid: int, wFlags: int, pDispParams: IPointer[DISPPARAMS],
                    pVarResult: IPointer[VARIANT], pExcepInfo: IPointer[EXCEPINFO],
                    puArgErr: IPointer[ULONG]):
        if not pDispParams:
            self.dbg_trace(provider, 'pDispParams == NULL!')
            return E_POINTER
        
        if not pVarResult:
            self.dbg_trace(provider, 'pVarResult == NULL!')
            return E_POINTER
        
        pDispParams = i_cast(pDispParams, PTR(DISPPARAMS))
        pVarResult = i_cast(pVarResult, LPVARIANT)
        
        method = self._disp_map_.get_method(dispIdMember)
        if method is None:
            self.dbg_trace(provider, 'DISP_E_MEMBERNOTFOUND Method not found, '
                           f'DispID: {hex(dispIdMember)}')
            return DISP_E_MEMBERNOTFOUND
        
        if wFlags not in (DISPATCH_METHOD, DISPATCH_PROPERTYGET):
            self.dbg_trace(provider, 'DISP_E_MEMBERNOTFOUND Not DispMethod or DispProperty')
            return DISP_E_MEMBERNOTFOUND
        
        method_static = getattr(self.__class__, method)
        result = getattr(self, method)
        
        if not hasattr(method_static, 'fget'):
            if not pDispParams.contents.cArgs:
                result = method_static(self)
            else:
                arguments = []
                
                for i in range(pDispParams.contents.cArgs):
                    varArgument = pDispParams.contents.rgvarg[i]
                    arguments.append(variant_get_value(varArgument))
                    
                result = method_static(self, *arguments)
                self.dbg_trace(provider, f'S_OK DispMethod {method}')
        else:
            self.dbg_trace(provider, f'S_OK DispProperty {method}')
                
        variant_set_value(pVarResult.contents, result)
        return S_OK
    
    #
    # System.Object
    #
        
    def ToString_Impl(self, pbstrString: IPointer[BSTR]) -> int:
        if not pbstrString:
            self.dbg_trace(provider, 'ppString == NULL!')
            return E_POINTER
        
        string = '<InteropObject>'
        TlWritePointerToPpv(pbstrString, TlAllocateOAString(string))
        self.dbg_trace(provider, f'S_OK *pbstrString=L"{string}"')
        return S_OK
    
    def Equals_Impl(self, pObject: IPointer[_Object], pvarBool: IPointer[VARIANT_BOOL]) -> int:
        if not pvarBool:
            self.dbg_trace(provider, 'pvarBool == NULL!')
            TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_FALSE
            return E_POINTER
        
        if not pObject:
            self.dbg_trace(provider, 'S_OK, *pvarBool=VARIANT_FALSE')
            TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_FALSE
            return S_OK
        
        if pObject.contents.GetHashCode() == self.GetHashCode():
            self.dbg_trace(provider, 'S_OK, *pvarBool=VARIANT_TRUE')
            TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_TRUE
            return S_OK
        
        self.dbg_trace(provider, 'S_OK, *pvarBool=VARIANT_FALSE')
        TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_FALSE
        return S_OK
    
    def GetHashCode_Impl(self, plHashCode: IPointer[LONG]) -> int:
        if not plHashCode:
            self.dbg_trace(provider, 'plHashCode == NULL!')
            return E_POINTER
        
        hash_code = 0
        
        for hashing_attribute in self.hashing_attributes:
            attribute_hash = hash(getattr(self, hashing_attribute))
            
            if hash_code == 0:
                hash_code = attribute_hash
            else:
                hash_code ^= attribute_hash
        
        TlAccessPpv(plHashCode, LONG).value = hash_code
        self.dbg_trace(provider, f'S_OK *plHashCode={hash_code}')
        return S_OK
    
    def GetType_Impl(self, ppType: IDoublePtr[_Type]) -> int:
        if not ppType:
            self.dbg_trace(provider, 'ppType == NULL!')
            return E_POINTER
        
        type_object = self.type_object
        TlWritePointerToPpv(ppType, type_object.ptr())
        
        self.dbg_trace(provider, f'S_OK *ppType=&{type_object}')
        return S_OK
       
class InteropMemberInfo(InteropObject, _MemberInfo):
    _com_map_ = InteropObject._com_map_.copy()
    _com_map_.append((_MemberInfo, _MemberInfo.virtual_table))
    
    _name: str
    
    def __init__(self, type_object: _Type, name: str, hashing_attributes: tuple[str, ...]=('_name')):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        self._name = name
        
        super().__init__(hashing_attributes, type_object)
        
        # _MemberInfo
        self.set_vtable_on_ctx(_MemberInfo.virtual_table)
        self.implement(_MemberInfo.MemberType.fget)
        self.implement(_MemberInfo.name.fget)
        self.implement(_MemberInfo.DeclaringType.fget)
        self.implement(_MemberInfo.ReflectedType.fget)
        self.implement(_MemberInfo.GetCustomAttributes)
        self.implement(_MemberInfo.GetCustomAttributes_2)
        self.implement(_MemberInfo.IsDefined)
        
    #
    # System.Reflection.MemberInfo
    #
    
    def MemberType_Impl(self, pType: IPointer[MemberTypes]) -> int:
        if not pType:
            self.dbg_trace(provider, 'pType == NULL!')
            return E_POINTER
        
        TlAccessPpv(pType, MemberTypes).value = MemberTypes.All
        self.dbg_trace(provider, 'S_OK *pType=MemberTypes.All')
        return S_OK
    
    def name_Impl(self, pbstrName: IPointer[BSTR]) -> int:
        if not pbstrName:
            self.dbg_trace(provider, 'pbstrName == NULL!')
            return E_POINTER
        
        TlWritePvToPpv(pbstrName, TlAllocateOAString(self._name))
        self.dbg_trace(provider, f'S_OK *pbstrName=L"{self._name}"')
        return S_OK
    
    def DeclaringType_Impl(self, ppType: IDoublePtr[_Type]) -> int:
        if not ppType:
            self.dbg_trace(provider, 'ppType == NULL!')
            return E_POINTER
        
        TlWritePvToPpv(ppType, NULL)
        self.dbg_trace(provider, 'S_OK, *ppType=NULL')
        return S_OK
    
    def ReflectedType_Impl(self, ppType: IDoublePtr[_Type]) -> int:
        if not ppType:
            self.dbg_trace(provider, 'ppType == NULL!')
            return E_POINTER
        
        TlWritePvToPpv(ppType, NULL)
        self.dbg_trace(provider, 'S_OK, *ppType=NULL')
        return S_OK
    
    def GetCustomAttributes_Impl(self, *args):
        self.dbg_trace(provider, 'E_NOTIMPL')
        return E_NOTIMPL
    
    def GetCustomAttributes_2_Impl(self, *args):
        self.dbg_trace(provider, 'E_NOTIMPL')
        return E_NOTIMPL
    
    def IsDefined(self, attributeType: IPointer[_Type], inherit: int,
                  pvarBool: IPointer[VARIANT_BOOL]) -> int:
        if not pvarBool:
            self.dbg_trace(provider, 'pvarBool == NULL!')
            TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_FALSE
            return E_POINTER
        
        TlAccessPpv(pvarBool, VARIANT_BOOL).value = VARIANT_FALSE
        
        self.dbg_trace(provider, 'S_OK *pvarBool=VARIANT_FALSE')
        return S_OK
            
class InteropParameterInfo(CComObject, _ParameterInfo):
    ...
            
class InteropMethodInfo(InteropMemberInfo, _MethodInfo):
    _com_map_ = [
        (_Object, _Object.virtual_table),
        (_MemberInfo, _MemberInfo.virtual_table),
        (_MethodBase, _MethodBase.virtual_table),
        (_MethodInfo, _MethodInfo.virtual_table)
    ]
    
    return_type: Object
    mscorlib: Assembly
    _name: str
    
    def __init__(self, name: str, parameters: list[int], return_type: Object = None):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        
        self.mscorlib = Object._ensure_mscorlib()
        mscorlibAsm = self.mscorlib._assembly
        rtMethodInfoType = mscorlibAsm.GetType_2('System.Reflection.RuntimeMethodInfo')
        
        super().__init__()
        
        # _MethodBase
        self.set_vtable_on_ctx(_MethodBase.virtual_table)
        self.implement(_MethodBase.GetParameters)
        self.implement(_MethodBase.GetMethodImplementationFlags)
        self.implement(_MethodBase.MethodHandle.fget)
        self.implement(_MethodBase.Attributes.fget)
        self.implement(_MethodBase.CallingConvention.fget)
        self.implement(_MethodBase.Invoke_2)
        self.implement(_MethodBase.IsPublic.fget)
        self.implement(_MethodBase.IsPrivate.fget)
        self.implement(_MethodBase.IsFamily.fget)
        self.implement(_MethodBase.IsAssembly.fget)
        self.implement(_MethodBase.IsFamilyAndAssembly.fget)
        self.implement(_MethodBase.IsFamilyOrAssembly.fget)
        self.implement(_MethodBase.IsStatic.fget)
        self.implement(_MethodBase.IsFinal.fget)
        self.implement(_MethodBase.IsVirtual.fget)
        self.implement(_MethodBase.IsHideBySig.fget)
        self.implement(_MethodBase.IsAbstract.fget)
        self.implement(_MethodBase.IsSpecialName.fget)
        self.implement(_MethodBase.IsConstructor.fget)
        self.implement(_MethodBase.Invoke_3)
        
        # _MethodInfo
        self.set_vtable_on_ctx(_MethodInfo.virtual_table)
        self.implement(_MethodInfo.returnType.fget)
        self.implement(_MethodInfo.ReturnTypeCustomAttributes.fget)
        self.implement(_MethodInfo.GetBaseDefinition)
        
        
        self.return_type = return_type
        self._name = name
    
    #
    # System.Reflection.MethodBase
    #
    
    
    #
    # System.Reflection.MethodInfo
    #