from typing import List, Dict
from .errors import *

from ..winnt import LOCALE_USER_DEFAULT

from .autointerfacedef import *
from .oleauto import *

import datetime
import decimal

class Dispatch:
    _dispids: Dict[str, int]
    _methods: List[str]
    _disp: IDispatch
    
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
        
        return result.value
                            
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
            
            return result.value
        
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
        if name in self._methods:
            raise AttributeError('Methods are immutable properties.')
        
        dispId = self._get_dispid(name)
        
        var = VARIANT()
        var._set_value(value)
        
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

class SafeArray(SAFEARRAY, IAliasableGenericWithPayload[WT],
                IReferenceable):
    _type_cache_: ClassVar[dict[type, type['SafeArray']]] = {}
    _item_type_: ClassVar[type[WT]]

    @classmethod
    def typed(cls, item_type: type) -> type['SafeArray']:
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
            
        return SafeArrayTyped
    
    @classmethod # support for @CStructure.make type resolution system
    def _get_alias_(cls, **kwargs) -> type['SafeArray']:
        genericalias = cls.get_genericalias()
        item_type = genericalias_single_type(genericalias)
        
        if is_genericalias(item_type):
            item_type = resolve_genericalias(item_type)
        else:
            item_type = resolve_type(item_type)
            
        return cls.typed(item_type)
    
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
            
    def get_data(self, size: int):
        item_type = self.get_type()
        psaThis = self.ref()
            
        array_pointer = PTR(item_type)()
        hr = SafeArrayAccessData(psaThis, byref(array_pointer))
        if FAILED(hr): raise COMError(hr)
        result = tuple(array_pointer[:size])
        
        if issubclass(item_type, Variant):
            result = tuple(variant.value for variant in result)
        elif issubclass(item_type, VARIANT_BOOL):
            result = tuple(VARIANT_BOOL_ToBool(value) for value in result)
        elif issubclass(self._item_type_, IUnknown) and not self._item_type_ is IDispatch:
            result = tuple(itf.contents for itf in result)
        elif issubclass(self._item_type_, IDispatch):
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
    elif vt == VT_BYREF:
        return var.byref
    
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
        var.vt = VT_BSTR
        var.boolVal = -1 if value else 0
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
        
    elif isinstance(value, (float, c_double)):
        var.vt = VT_R8
        var.dblVal = value
    elif isinstance(value, IDispatch):
        var.vt = VT_DISPATCH
        var.byref = PtrUtil.get_address(value.ptr())
    elif isinstance(value, IUnknown):
        var.vt = VT_UNKNOWN
        var.byref = PtrUtil.get_address(value.ptr())
    elif isinstance(value, Dispatch):
        var.vt = VT_DISPATCH
        var.byref = PtrUtil.get_address(value._disp.ptr())
    else:
        raise NotImplementedError(f'{value}')