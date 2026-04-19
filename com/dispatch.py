from typing import List, Dict, Iterable
from .errors import *

from ..winnt import LOCALE_USER_DEFAULT

from ..defbase_allocator import *
from .autointerfacedef import *
from .oleauto import *

import builtins
import datetime
import decimal

class DispatchPolicy:
    MarshalBSTR = 1

class Dispatch:
    _dispids: Dict[str, int]
    _methods: List[str]
    _disp: IDispatch
    
    policy: int = 0
    
    def __init__(self, disp: IDispatch):
        disp.AddRef()
        
        super().__setattr__('_methods', [])
        super().__setattr__('_dispids', {})
        super().__setattr__('_disp', disp)
        try: 
            self.initialize()
        except: ...
        
    def initialize(self):
        pTypeInfo = ITypeInfo.NULL()
        
        hr = self._disp.GetTypeInfo(0, LOCALE_USER_DEFAULT, byref(pTypeInfo))
        if FAILED(hr): raise COMError(hr)
        
        pTypeAttr = TYPEATTR.NULL()
        hr = pTypeInfo.contents.GetTypeAttr(byref(pTypeAttr))
        
        if SUCCEEDED(hr):
            for i in range(pTypeAttr.contents.cFuncs):
                pFuncDesc = FUNCDESC.NULL()
                hr = pTypeInfo.contents.GetFuncDesc(i, byref(pFuncDesc))
                
                if SUCCEEDED(hr):
                    bstrName: BSTR = BSTR()
                    cNames: UINT = UINT()
                    
                    hr = pTypeInfo.contents.GetNames(pFuncDesc.contents.memid, byref(bstrName), 1, byref(cNames))
                    
                    if SUCCEEDED(hr) and cNames.value > 0:
                        if pFuncDesc.contents.invkind == INVOKE_FUNC:
                            self._methods.append(bstrName.value)
                
                if pFuncDesc:            
                    pTypeInfo.contents.ReleaseFuncDesc(pFuncDesc)
                    
        if pTypeAttr:        
            pTypeInfo.contents.ReleaseTypeAttr(pTypeAttr)
            
        pTypeInfo.contents.Release()
             
    def _get_dispid(self, name: str) -> int:
        dispId = self._dispids.get(name)
        
        if dispId is None:
            dispId = DISPID()
            lpOleName = LPOLESTR(name)
            
            hr = self._disp.GetIDsOfNames(IID_NULL, byref(lpOleName),
                                    1, LOCALE_USER_DEFAULT, 
                                    byref(dispId))
            if FAILED(hr): raise COMError(hr)
            
            self._dispids[name] = dispId.value
            
            return dispId.value
        
        return dispId
    
    def _call_method(self, dispId: int, *args) -> Any:
        arguments = (Variant * len(args))()
        
        for index, arg in enumerate(args[::-1]):
            variant = Variant()
            variant.value = arg
            arguments[index].value = variant
        
        dispParams = DISPPARAMS()
        dispParams.rgvarg = i_cast(arguments, LPVARIANT)
        dispParams.cArgs = len(args)
        result = Variant()
        
        hr = self._disp.Invoke(dispId, IID_NULL, LOCALE_USER_DEFAULT,
                               DISPATCH_METHOD, byref(dispParams),
                               byref(result), NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        
        value = result.value
        if isinstance(value, BSTR) and Dispatch.policy & DispatchPolicy.MarshalBSTR:
            result = value.value
            SysFreeString(value)
            return result
        return value
                            
    def __getattr__(self, name: str):
        if name in self._methods:
            dispId = self._get_dispid(name)
            
            def _function(*args, **kwargs):
                return self._call_method(dispId, *args)

            _function.__name__ = name

            return _function
        else:
            dispId = self._get_dispid(name)
            dispParams = DISPPARAMS()
            result = Variant()
            
            hr = self._disp.Invoke(dispId, IID_NULL, LOCALE_USER_DEFAULT,
                                   DISPATCH_PROPERTYGET, byref(dispParams),
                                   byref(result), NULL, NULL)
            if FAILED(hr): raise COMError(hr)
            
            value = result.value
            if isinstance(value, BSTR) and Dispatch.policy & DispatchPolicy.MarshalBSTR:
                result = value.value
                SysFreeString(value)
                return result
            return value
        
    def put_property(self, dispid: int, pVar: IPointer[VARIANT]):
        dispparams = DISPPARAMS(NULL, NULL, 1, 1)
        dispparams.rgvarg = pVar
        dispidPut = DISPID_PROPERTYPUT
        dispparams.rgdispidNamedArgs = pointer(DISPID(dispidPut))
        
        if (pVar.contents.vt == VT_UNKNOWN or pVar.contents.vt == VT_DISPATCH or
            (pVar.contents.vt & VT_ARRAY) or (pVar.contents.vt & VT_BYREF)):
            hr = self._disp.Invoke(dispid, IID_NULL,
                                   LOCALE_USER_DEFAULT, 
                                   DISPATCH_PROPERTYPUTREF,
                                   dispparams)
        
    def __setattr__(self, name: str, value):
        if name == 'policy':
            return i_setattr(self, name, value)
        
        if name in self._methods:
            raise AttributeError('Methods are immutable properties.')
        
        dispId = self._get_dispid(name)
        
        var = VARIANT()
        variant_set_value(var, value)
        
        dispParams = DISPPARAMS()
        dispParams.rgvarg = pointer(var)
        dispParams.cArgs = 1
        dispParams.cNamedArgs = 1
        dispParams.rgdispidNamedArgs = pointer(DISPID(DISPATCH_PROPERTYPUT))
        
        excepInfo = EXCEPINFO()
        argErr = UINT()
        hr = self._disp.Invoke(dispId, IID_NULL, LOCALE_USER_DEFAULT,
                                DISPATCH_PROPERTYPUT, byref(dispParams),
                                NULL, byref(excepInfo), byref(argErr))
        
        if FAILED(hr): raise COMError(hr)
        
    def __del__(self):
        self._disp.Release()

class IVariantBool(IAliasable, ICustomizable, bool):
    _alias_ = VARIANT_BOOL
    _custom_ = bool
            
class Variant(VARIANT):
    @property
    def value(self):
        return variant_get_value(self)
    
    @value.setter
    def value(self, value):
        return variant_set_value(self, value)
    
    def __init__(self, initialize: bool = True):
        if initialize:
            VariantInit(self.ref())
        
    def copy(self) -> 'Variant':
        newVariant = Variant(initialize=False)
        VariantCopy(newVariant.ref(), self.ref())
        return newVariant
    
    def clear(self):
        VariantClear(self.ref())

if TYPE_CHECKING:
    from win.defbase import ICData

class _Ctype2VT(dict):
    def __getitem__(self, type_obj: type) -> type:
        try:
            return super().__getitem__(type_obj)
        except KeyError:
            for base in type_obj.__bases__:
                return self[base]
            return None
        
ctype_to_vt: Dict[Type['ICData'], int] = _Ctype2VT({
    byte: VT_I1,
    BYTE: VT_UI1,
    SHORT: VT_I2,
    USHORT: VT_UI2,
    LONG: VT_I4,
    ULONG: VT_UI4,
    FLOAT: VT_R4,
    DOUBLE: VT_R8,
    LONGLONG: VT_I8,
    ULONGLONG: VT_UI8,
    VARIANT_BOOL: VT_BOOL,
    BSTR: VT_BSTR,
    HRESULT: VT_HRESULT,
    VARIANT: VT_VARIANT,
    Variant: VT_VARIANT,
    LPVARIANT: VT_BYREF | VT_VARIANT,
    LPBSTR: VT_BYREF | VT_BSTR
})

vt_to_ctype: Dict[int, Type['ICData']] = _Ctype2VT({
    VT_I1: byte,
    VT_UI1: BYTE,
    VT_I2: SHORT,
    VT_UI2: USHORT,
    VT_I4: LONG,
    VT_UI4: ULONG,
    VT_R4: FLOAT,
    VT_R8: DOUBLE,
    VT_I8: LONGLONG,
    VT_UI8: ULONGLONG,
    VT_BOOL: VARIANT_BOOL,
    VT_BSTR: BSTR,
    VT_HRESULT: HRESULT,
    VT_VARIANT: VARIANT,
    VT_VARIANT: Variant,
    VT_BYREF | VT_VARIANT: LPVARIANT,
    VT_BYREF | VT_BSTR: LPBSTR,
    VT_UNKNOWN: IUnknown,
    VT_DISPATCH: IDispatch
})

class SafeArray(SAFEARRAY, IAliasableGenericWithPayload[WT],
                IReferenceable):
    _delayed_execution: ClassVar[list[tuple['SafeArray', DelayedTypeStorage]]] = []
    _type_cache_: ClassVar[dict[type, type['SafeArray']]] = {}
    _item_type_: ClassVar[type[WT]]
    _extra_: Any = NULL
    _vt_: int

    @classmethod
    def from_psa(cls, psa: IPointer[SAFEARRAY]) -> 'SafeArray':
        return i_cast(psa, PTR(cls)).contents

    @classmethod
    def _setup(cls, item_type: type, vt: int = None):
        if vt is not None:
            cls._vt_ = vt
        else:
            if isinstance(item_type, type):
                vt = ctype_to_vt[item_type]
                
                if vt is not None:
                    cls._vt_ = vt
                else:
                    if issubclass(item_type, IUnknown):
                        unk_type: type[IUnknown] = item_type
                        
                        if issubclass(item_type, IDispatch):
                            cls._vt_ = VT_DISPATCH
                        else:
                            cls._vt_ = VT_UNKNOWN
                        
                        cls._extra_ = pointer(unk_type.iid())
                    elif issubclass(item_type, CStructure):
                        cls._vt_ = VT_RECORD
                    
                    vt = cls._vt_
                        
            elif isinstance(item_type, DelayedTypeStorage):
                SafeArray._delayed_execution.append((cls, item_type))
                cls._vt_ = 0
                vt = 0
        
        if vt == VT_HRESULT:
            raise TypeError('Cannot create SafeArray with type VT_HRESULT.')

    @classmethod
    def typed(cls, item_type: type, vt: int = None) -> type['SafeArray']:
        SafeArrayTyped = cls._type_cache_.get(item_type, None)
        if SafeArrayTyped is not None:
            return SafeArrayTyped
        
        class SafeArrayTyped(SafeArray):
            _item_type_ = item_type
        
        if isinstance(item_type, DelayedTypeStorage):
            name = 'DelayedType'
        else:
            name = item_type.__name__
        
        SafeArrayTyped.__qualname__ += f'_{name}'
        cls._type_cache_[item_type] = SafeArrayTyped
        
        SafeArrayTyped._setup(item_type, vt)
            
        return SafeArrayTyped
    
    @staticmethod
    def release_delay_execution():
        for cls, delayed in SafeArray._delayed_execution:
            cls._setup(delayed.unpack())
    
    @classmethod # support for @CStructure.make type resolution system
    def _get_alias_(cls, **kwargs) -> type['SafeArray']:
        genericalias = cls.get_genericalias()
        item_type = genericalias_single_type(genericalias)
        
        if is_genericalias(item_type):
            item_type = resolve_genericalias(item_type)
        else:
            item_type = resolve_type(item_type)
            
        return cls.typed(item_type)
    
    @classmethod
    def create(cls, value: Iterable, extra=None) -> 'SafeArray[WT]':
        if extra is None:
            extra = cls._extra_
            
        psaNew = SafeArrayCreateVectorEx(cls._vt_, 0, len(value), extra)
        
        if not psaNew:
            raise RuntimeError('SafeArrayCreateVectorEx failed.')
        
        psaNew = i_cast(psaNew, cls.PTR())
        pData = PTR(cls._item_type_)()
        
        hr = SafeArrayAccessData(psaNew, byref(pData))
        if FAILED(hr): raise COMError(hr)
        
        for index, item in enumerate(value):
            pData[index] = item
        
        hr = SafeArrayUnaccessData(psaNew)
        if FAILED(hr): raise COMError(hr)
        
        return psaNew.contents
    
    def allow_other_type(self, typ):
        return issubclass(typ, SAFEARRAY)
    
    def get_reference(self):
        return self.ref()
    
    @classmethod
    def allow_reference(self, value):
        return True
    
    def __len__(self) -> int:
        dimensions = self.dimensions
        
        if dimensions == 0: return 0
        if self.dimensions != 1:
            raise ValueError('Tried to get length of non-1-dimensional array.')
        
        return self.get_size(1)
    
    def __getitem__(self, index: int):
        if self.dimensions != 1:
            raise ValueError('Tried to index non-1-dimensional array.')
    
        return self.get_data(self.get_size(1))[index]
    
    @property
    def dimensions(self) -> int:
        return SafeArrayGetDim(self.ref())
    
    def get_ubound(self, dimension: int) -> int:
        ubound = LONG()
        
        hr = SafeArrayGetUBound(self.ref(), dimension, byref(ubound))
        if FAILED(hr): raise COMError(hr)
        
        return ubound.value
    
    def get_lbound(self, dimension: int) -> int:
        lbound = LONG()
        
        hr = SafeArrayGetLBound(self.ref(), dimension, byref(lbound))
        if FAILED(hr): raise COMError(hr)
        
        return lbound.value
    
    def get_size(self, dimension: int) -> int:
        return self.get_ubound(dimension) - self.get_lbound(dimension) + 1
    
    @property
    def value(self) -> list[WT]:
        dimensions = self.dimensions
        
        match dimensions:
            case 0:
                return ()
            case 1: 
                size = self.get_size(1)
                return self.get_data(size)
            case _:
                psaThis = self.ref()
                lbounds = []
                ubounds = []
                
                for dimension in range(1, dimensions + 1):
                    lbound = LONG()
                    hr = SafeArrayGetLBound(psaThis, dimension, byref(lbound))
                    if FAILED(hr): raise COMError(hr)
                    lbounds.append(lbound.value)
                
                for dimension in range(1, dimensions + 1):
                    ubound = LONG()
                    hr = SafeArrayGetUBound(psaThis, dimension, byref(ubound))
                    if FAILED(hr): raise COMError(hr)
                    ubounds.append(ubound.value)
                
                indices = (LONG * dimensions)(*lbounds)
                row = self.get_row(psaThis, 0, indices, ubounds)
                return row
            
    def get_type(self):
        item_type = self._item_type_
        if isinstance(item_type, DelayedTypeStorage):
            item_type = item_type.storaged_type
        if issubclass(item_type, IUnknown):
            return PTR(item_type)
        elif issubclass(item_type, VARIANT):
            return Variant
        return item_type
    
    def get_unptred_type(self):
        item_type = self.get_type()
        if PtrUtil.is_pointer_type(item_type):
            return PtrUtil.get_type(item_type)
        return item_type
            
    def get_data(self, size: int):
        item_type = self.get_type()
        unptred = self.get_unptred_type()
        psaThis = self.ref()
            
        array_pointer = PTR(item_type)()
        hr = SafeArrayAccessData(psaThis, byref(array_pointer))
        if FAILED(hr): raise COMError(hr)
        result = tuple(array_pointer[:size])
        
        if issubclass(item_type, Variant):
            result = tuple(variant.value for variant in result)
        elif issubclass(item_type, VARIANT_BOOL):
            result = tuple(VARIANT_BOOL_ToBool(value) for value in result)
        elif issubclass(unptred, IUnknown) and not unptred is IDispatch:
            result = tuple(itf.contents for itf in result)
        elif issubclass(unptred, IDispatch):
            result = tuple(Dispatch(disp) for disp in result)
            
        hr = SafeArrayUnaccessData(psaThis)
        if FAILED(hr): raise COMError(hr)
        return result
    
    def get_row(self, psaThis: IPointer[SAFEARRAY],
                dimension: int, indices: IArray[int], 
                ubounds: list[int]):
        restore = indices[dimension]
        item_type = self.get_type()
        obj = item_type()
        is_variant = issubclass(item_type, Variant)
        pObj = byref(obj)
        result = []
        
        if dimension + 1 == len(indices):
            for i in range(indices[dimension], ubounds[dimension] + 1):
                indices[dimension] = i
                hr = SafeArrayGetElement(psaThis, indices, pObj)
                if FAILED(hr): raise COMError(hr)
                if is_variant:
                    result.append(obj.value)
                else:
                    result.append(obj)
        else:
            for i in range(indices[dimension], ubounds[dimension] + 1):
                indices[dimension] = i
                result.append(self.get_row(psaThis, dimension + 1, indices, ubounds))
        
        indices[dimension] = restore
        return tuple(result)

class Record:
    _allocator_: ClassVar[IAllocator] = CLocalAllocator()
    _record_cache: ClassVar[dict[GUID, 'Record']] = {}
    _record_info_: ClassVar[IRecordInfo] = None
    _guid_: ClassVar[GUID] = GUID_NULL
    _size_: ClassVar[int] = 0
    _fields_: list[str] = []
    
    allocation_base: int
    
    def __init__(self, allocation_base: int):
        if allocation_base:
            self.allocation_base = allocation_base
        else:
            self.allocation_base = self._allocator_.allocate(self._size_)
    
    def __getattr__(self, name: str) -> Any:
        if name not in self._fields_:
            return
        
        varField = VARIANT()
        self._record_info_.GetField(self.allocation_base, name, varField.ref())
        
        return variant_get_value(varField)
    
    def __setattr__(self, name: str, value: Any) -> Any:
        if name not in self._fields_:
            return builtins.object.__setattr__(self, name, value)
        
        if isinstance(value, VARIANT):
            var = value
        else:
            var = VARIANT()
            variant_set_value(var, value)
        
        hr = self._record_info_.PutField(
            INVOKE_PROPERTYPUT, self.allocation_base,
            name, var.ref())
        if hr == E_INVALIDARG:
            hr = self._record_info_.PutField(
                INVOKE_PROPERTYPUTREF, self.allocation_base,
                name, var.ref())
            if FAILED(hr): raise COMError(hr)
    
    @classmethod
    def construct(cls, record_info: IRecordInfo) -> 'Record':
        guid = Record.guid_from_record(record_info)
        cached_record = Record._record_cache.get(guid, None)
        
        if cached_record is not None:
            return cached_record
        
        class RecordExt(Record):
            _fields_ = Record.fields_from_record(record_info)
            _size_ = Record.size_from_record(record_info)
            _record_info_ = record_info
            _guid_ = guid
        
        RecordExt.__name__ = Record.name_from_record(record_info)
        Record._record_cache[guid] = RecordExt
        
        return RecordExt
        
    @classmethod
    def guid_from_record(cls, record_info: IRecordInfo) -> GUID:
        guid = GUID()
        
        hr = record_info.GetGuid(guid.ref())
        if FAILED(hr): raise COMError(hr)
        
        return guid
    
    @classmethod
    def name_from_record(cls, record_info: IRecordInfo) -> str:
        bstrName = BSTR()
        
        hr = record_info.GetName(byref(bstrName))
        if FAILED(hr): raise COMError(hr)
        
        name = bstrName.value
        SysFreeString(bstrName)
        
        return name
    
    @classmethod
    def size_from_record(cls, record_info: IRecordInfo) -> int:
        cbSize = ULONG()
        
        hr = record_info.GetSize(byref(cbSize))
        if FAILED(hr): raise COMError(hr)
        
        return cbSize.value
    
    @classmethod
    def fields_from_record(cls, record_info: IRecordInfo) -> list[str]:
        cNames = ULONG()
        hr = record_info.GetFieldNames(byref(cNames), NULL)
        
        if FAILED(hr): raise COMError(hr)
        bstrNames = (BSTR * cNames.value)()
        
        hr = record_info.GetFieldNames(NULL, bstrNames)
        if FAILED(hr): raise COMError(hr)
        
        result = []
        
        for bstrName in bstrNames:
            result.append(bstrName.value)
            SysFreeString(bstrName)
            
        return result
    
    @classmethod
    def from_variant(cls, variant: VARIANT) -> 'Record':
        record_info = Record.construct(variant.pRecInfo.contents)
        return record_info(variant.byref)
        
OA_NULL_DATE = datetime.datetime(1899, 12, 30, 0, 0, 0)
        
def variant_get_value(var: VARIANT):
    vt = var.vt
    if vt in (VT_EMPTY, VT_NULL):
        return None
    elif vt == VT_UNKNOWN:
        if not var.byref:
            return None
        
        return var.punkVal
    elif vt == (VT_UNKNOWN | VT_BYREF):
        if not var.byref:
            return None
        
        return var.ppunkVal
    elif vt == VT_DISPATCH:
        if not var.byref:
            return None
        
        return Dispatch(var.pdispVal.contents)
    elif vt == (VT_DISPATCH | VT_BYREF):
        if not var.byref:
            return None
        
        return var.ppdispVal
    elif vt == VT_I1:
        return var.cVal
    elif vt == (VT_I1 | VT_BYREF):
        return var.pcVal
    elif vt == VT_UI1:
        return var.bVal
    elif vt == (VT_UI1 | VT_BYREF):
        return var.pbVal
    elif vt == VT_I2:
        return var.iVal
    elif vt == (VT_I2 | VT_BYREF):
        return var.piVal
    elif vt == VT_UI2:
        return var.uiVal
    elif vt == (VT_UI2 | VT_BYREF):
        return var.puiVal
    elif vt == VT_I4 or vt == VT_INT:
        return var.lVal
    elif vt == (VT_I4 | VT_BYREF) or vt == (VT_INT | VT_BYREF):
        return var.plVal
    elif vt == VT_UI4 or vt == VT_UINT:
        return var.ulVal
    elif vt == (VT_UI4 | VT_BYREF) or vt == (VT_UINT | VT_BYREF):
        return var.pulVal
    elif vt == VT_I8:
        return var.llVal
    elif vt == (VT_I8 | VT_BYREF):
        return var.pllVal
    elif vt == VT_UI8:
        return var.ullVal
    elif vt == (VT_UI8 | VT_BYREF):
        return var.pullVal
    elif vt == VT_BSTR:
        var.bstrVal._allocated = True
        return var.bstrVal
    elif vt == (VT_BSTR | VT_BYREF):
        return var.pbstrVal
    elif vt == VT_R4:
        return var.fltVal
    elif vt == (VT_R4 | VT_BYREF):
        return var.pfltVal
    elif vt == VT_R8:
        return var.dblVal
    elif vt == (VT_R8 | VT_BYREF):
        return var.pdblVal
    elif vt == VT_BOOL:
        return var.boolVal == VARIANT_TRUE
    elif vt == (VT_BOOL | VT_BYREF):
        return var.pboolVal
    elif vt == VT_CY:
        return var.cyVal.int64 / decimal.Decimal('10000')
    elif vt == (VT_CY | VT_BYREF):
        return var.pcyVal
    elif vt == (VT_DECIMAL | VT_BYREF):
        return var.pdecVal.contents.as_decimal()
    elif vt == VT_ARRAY:
        return var.parray
    elif vt == (VT_ARRAY | VT_BYREF):
        return var.pparray
    elif vt & VT_ARRAY:
        vt &= ~VT_ARRAY
        return SafeArray.typed(vt_to_ctype[vt]).from_psa(var.parray)
    elif vt == VT_BYREF:
        return var.byref
    elif vt == VT_RECORD:
        return Record.from_variant(var)
    elif vt == VT_DATE:
        return datetime.timedelta(days=var.dblVal) + OA_NULL_DATE
    
    raise NotImplementedError(f'VARTYPE: {hex(vt)}')
    
def variant_set_value(var: VARIANT, value):
    vt = var.vt
    VariantClear(var.ref())
    var.vt = vt
    
    if isinstance(value, VARIANT):
        VariantCopy(var.ref(), value.ref())
        return
    
    if value is None:
        var.vt = VT_NULL
    elif isinstance(value, str):
        var.vt = VT_BSTR
        var.bstrVal = BSTR.new(value)
    elif isinstance(value, BSTR):
        var.vt = VT_BSTR
        var.bstrVal = value
    elif isinstance(value, bool):
        var.vt = VT_BOOL
        var.boolVal = -1 if value else 0
    elif isinstance(value, SafeArray):
        var.vt = VT_ARRAY | value._vt_
        var.parray = i_cast(pointer(value), LPSAFEARRAY)
    elif isinstance(value, byte):
        var.vt = VT_I1
        var.cVal = value.value
    elif isinstance(value, BYTE):
        var.vt = VT_UI1
        var.bVal = value.value
    elif isinstance(value, SHORT):
        var.vt = VT_I2
        var.iVal = value.value
    elif isinstance(value, USHORT):
        var.vt = VT_UI2
        var.uiVal = value.value
    elif isinstance(value, INT):
        var.vt = VT_I4
        var.lVal = value.value
    elif isinstance(value, UINT):
        var.vt = VT_UI4
        var.ulVal = value.value
    elif isinstance(value, LONGLONG):
        var.vt = VT_I8
        var.llVal = value.value
    elif isinstance(value, ULONGLONG):
        var.vt = VT_UI8
        var.ullVal = value.value
    elif isinstance(value, int):
        vt_defined = var.vt in (
            VT_I1, VT_UI1, 
            VT_I2, VT_UI2,
            VT_I4, VT_UI4,
            VT_I8, VT_UI8)
        
        if not vt_defined:
            vt = VT_I1
        else:
            vt = var.vt
        
        if not vt_defined:
            if -(2**7) < value and (2**7-1) > value:
                if value >= 0:
                    var.bVal = value
                    vt = VT_UI1
                else:
                    var.cVal = value
                    vt = VT_I1
            else:
                success = False
                    
                if -(2**63) > value or (2**63-1) < value:
                    raise OverflowError(value)
                    
                if -(2**31) > value or (2**31-1) < value:
                    if value >= 0:
                        var.ulVal = value
                        vt = VT_UI8
                    else: 
                        var.lVal = value
                        vt = VT_I8
                    success = True
                    
                if -(2**15) > value or (2**15-1) < value:
                    if value >= 0:
                        var.ulVal = value
                        vt = VT_UI4
                    else: 
                        var.lVal = value
                        vt = VT_I4
                    success = True
                    
                if not success:
                    if value >= 0:
                        var.uiVal = value
                        vt = VT_UI2
                    else: 
                        var.iVal = value
                        vt = VT_I2
        
        if vt_defined:
            if vt in (VT_I1, VT_UI1):
                if -(2**7) > value or (2**7-1) < value:
                    raise OverflowError(value)
                if vt == VT_I1:
                    var.cVal = value
                else:
                    var.bVal = value
            elif vt in (VT_I2, VT_UI2):
                if -(2**15) > value or (2**15-1) < value:
                    raise OverflowError(value)
                if vt == VT_I2:
                    var.iVal = value
                else:
                    var.uiVal = value
            elif vt in (VT_I4, VT_UI4):
                if -(2**31) > value or (2**31-1) < value:
                    raise OverflowError(value)
                if vt == VT_I4:
                    var.lVal = value
                else:
                    var.ulVal = value
            elif vt in (VT_I8, VT_UI8):
                if -(2**63) > value or (2**63-1) < value:
                    raise OverflowError(value)
                if vt == VT_I8:
                    var.llVal = value
                else:
                    var.ullVal = value
        else: 
            var.vt = vt
        
    elif isinstance(value, float):
        var.vt = VT_R8
        var.dblVal = value
    elif isinstance(value, c_float):
        var.vt = VT_R4
        var.dblVal = value.value
    elif isinstance(value, c_double):
        var.vt = VT_R8
        var.dblVal = value.value
    elif isinstance(value, IDispatch):
        var.vt = VT_DISPATCH
        var.byref = PtrUtil.get_address(value.ptr())
    elif isinstance(value, IUnknown):
        var.vt = VT_UNKNOWN
        var.byref = PtrUtil.get_address(value.ptr())
    elif isinstance(value, Dispatch):
        var.vt = VT_DISPATCH
        var.byref = PtrUtil.get_address(value._disp.ptr())
    elif isinstance(value, PVOID):
        var.vt = VT_BYREF
        var.byref = PtrUtil.get_address(value)
    elif isinstance(value, Record):
        var.vt = VT_RECORD
        var.byref = value.allocation_base
        var.pRecInfo = value._record_info_.ptr()
    else:
        raise NotImplementedError(f'{value}')