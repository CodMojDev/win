from win.com.comtl import *
from .roapi import *
from .roparameterizediid import *

import typing
import uuid

class IStringable(IInspectable):
    virtual_table = COMVirtualTable.from_ancestor(IInspectable)
    _iid_ = IID('{96369f54-8eb6-48f0-abce-c1b211e627c3}')
    
    @virtual_table.com_function(PTR(HSTRING))
    def ToString(self, value: IPointer[HSTRING]) -> int: ...
    
    virtual_table.build()

class Detail_WinRTInterfaceBase(COMInterface):
    _priv_checked_from_: type = None
    _exclusive_to_: list[str]
    
    def __init_subclass__(cls, *args, **kwargs):
        if cls._priv_checked_from_ != cls:
            for mro_cls in cls.__mro__:
                if mro_cls.__name__ == cls.__name__: continue
                if issubclass(mro_cls, Detail_WinRTInterfaceBase):
                    exclusive_to = getattr(mro_cls, '_exclusive_to_', None)
                    if exclusive_to is not None and cls.__name__ not in exclusive_to:
                        raise TypeError(f'Interface {mro_cls.__name__} is exclusive to {exclusive_to} classes.')
            cls._priv_checked_from_ = cls
        return super().__init_subclass__(*args, **kwargs)

#def detail_parameterized_iid(args)

class WinRTInterfaceMeta(Detail_WinRTInterfaceBase.__class__):
    def __getitem__(self, args):
        if not isinstance(args, tuple):
            args = (args,)
        self.args = args

class WinRTInterface(Detail_WinRTInterfaceBase, IInspectable, metaclass=WinRTInterfaceMeta):
    def __str__(self):
        istringable = IStringable.NULL()
        hr = self.QueryInterface(IStringable, byref(istringable))
        if FAILED(hr):
            return ''
        string = HSTRING()
        hr = istringable.contents.ToString(byref(string))
        if FAILED(hr): raise COMError(hr)
        value = string.string.value
        string.delete()
        return value
    
    @property
    def runtime_class_name(self) -> str:
        string = HSTRING()
        hr = self.GetRuntimeClassName(byref(string))
        if FAILED(hr): raise COMError(hr)
        value = string.string.value
        string.delete()
        return value
    
    def __repr__(self):
        string = str(self)
        if len(string) != 0:
            string = f' "{string}"'
        return f'<{self.runtime_class_name}{string}>'
    
class WinRuntimeClass(WinRTInterface):
    factory_qi_cache: ClassVar[dict[type[IT], IT]] = {}
    factory: ClassVar[IActivationFactory] = None
    qi_cache: dict[type[IT], IT]
    _name_: ClassVar[str]
    
    def __init__(self):
        self.qi_cache = {}
        
    def __del__(self):
        self.Release()
    
def detail_rt_interfacespec(spec: type[IT]):
    def _detail_rt_interfacespec(f: Callable):
        def _detail_specified_method(self: WinRuntimeClass, *args, **kwargs):
            itf = self.qi_cache.get(spec)
            
            if itf is None:
                itf = TlQueryInterface(self, spec)
                self.qi_cache[spec] = itf
                TlAddRefGuard(itf)
                
            return getattr(itf, f.__name__)(*args, **kwargs)
        return _detail_specified_method
    return _detail_rt_interfacespec

def detail_rt_classmethod(spec: type[IT]):
    def _detail_rt_classmethod(f: Callable):
        def _detail_specified_classmethod(cls: type[WinRuntimeClass], *args, **kwargs):
            factory = cls.factory
            
            if factory is None:
                factory = IActivationFactory.NULL()
                hstrName = HSTRING(cls._name_)
                hr = RoGetActivationFactory(hstrName, IActivationFactory._iid_, byref(factory))
                if FAILED(hr): raise COMError(hr)
                hstrName.delete()
                cls.factory = factory.contents
                TlAddRefGuard(cls.factory)
            
            itf = cls.factory_qi_cache.get(spec)
            
            if itf is None:
                itf = TlQueryInterface(cls.factory, spec)
                cls.factory_qi_cache[spec] = itf
                TlAddRefGuard(itf)
                
            return getattr(itf, f.__name__)(*args, **kwargs)
        return _detail_specified_classmethod
    return _detail_rt_classmethod

class Detail_IllegalIID(IID):
    def __eq__(self, other: IID):
        return False

def detail_name_T(cls: type, T: type):
    cls.__name__ += f'_{T.__qualname__}'

def detail_IVectorView(generic: WT, iid: IID):
    class Detail_IVectorView_T(IInspectable):
        virtual_table = COMVirtualTable.from_ancestor(IInspectable)
        _iid_ = iid
        
        @virtual_table.com_function(UINT, PTR(generic))
        def GetAt(self, index: int, item: IPointer[WT]) -> int: ...
        
        @virtual_table.com_function(generic, PUINT, PBOOLEAN)
        def IndexOf(self, value: WT, index: PUINT, found: PBOOLEAN) -> int: ...
        
        @virtual_table.com_function(UINT, UINT, PTR(generic), PUINT)
        def GetMany(self, startIndex: int, capacity: int, value: IPointer[WT], actual: PUINT) -> int: ...
        
        virtual_table.build()
        
    detail_name_T(Detail_IVectorView_T, generic)
    return Detail_IVectorView_T

def detail_IVector(generic: WT, iid: IID):
    class Detail_IVector_T(IInspectable):
        virtual_table = COMVirtualTable.from_ancestor(IInspectable)
        _iid_ = iid
        
        @virtual_table.com_function(UINT, PTR(generic))
        def GetAt(self, index: int, item: IPointer[WT]) -> int: ...
        
        @virtual_table.com_function(PUINT)
        def get_Size(self, size: PUINT) -> int: ...
        
        @virtual_table.com_function(PVOID)
        def GetView(self, view: IDoublePtr) -> int: ...
        
        @virtual_table.com_function(generic, PUINT, PBOOLEAN)
        def IndexOf(self, value: WT, index: PUINT, found: PBOOLEAN) -> int: ...
        
        @virtual_table.com_function(UINT, generic)
        def SetAt(self, index: int, item: WT) -> int: ...
        
        @virtual_table.com_function(UINT, generic)
        def InsertAt(self, index: int, item: WT) -> int: ...
        
        @virtual_table.com_function(UINT)
        def RemoveAt(self, index: int) -> int: ...
        
        @virtual_table.com_function(generic)
        def Append(self, value: WT) -> int: ...
        
        @virtual_table.com_function()
        def RemoveAtEnd(self) -> int: ...
        
        @virtual_table.com_function()
        def Clear(self) -> int: ...
        
        @virtual_table.com_function(UINT, UINT, PTR(generic), PUINT)
        def GetMany(self, startIndex: int, capacity: int, value: IPointer[WT], actual: PUINT) -> int: ...
        
        @virtual_table.com_function(UINT, PTR(generic))
        def ReplaceAll(self, count: int, value: IPointer[WT]) -> int: ...
        
        virtual_table.build()
        
    detail_name_T(Detail_IVector_T, generic)
    return Detail_IVector_T

def detail_IIterator(generic: WT, iid: IID):
    class Detail_IIterator_T(IInspectable):
        virtual_table = COMVirtualTable.from_ancestor(IInspectable)
        _iid_ = iid
        
        @virtual_table.com_function(PTR(generic))
        def get_Current(self, current: IPointer[WT]) -> int: ...
        
        @virtual_table.com_function(PBOOLEAN)
        def get_HasCurrent(self, hasCurrent: PBOOLEAN) -> int: ...
        
        @virtual_table.com_function(PBOOLEAN)
        def MoveNext(self, hasCurrent: PBOOLEAN) -> int: ...
        
        @virtual_table.com_function(UINT, PTR(generic), PUINT)
        def GetMany(self, capacity: int, value: IPointer[WT], actual: PUINT) -> int: ...
        
        virtual_table.build()
        
    detail_name_T(Detail_IIterator_T, generic)
    return Detail_IIterator_T

def detail_IIterable(generic: WT, iterator: type[WT2], iid: IID):
    class Detail_IIterable_T(IInspectable):
        virtual_table = COMVirtualTable.from_ancestor(IInspectable)
        _iid_ = iid
        
        @virtual_table.com_function(PVOID)
        def First(self, iterator: IDoublePtr[WT2]) -> int: ...
        
        virtual_table.build()
        
    detail_name_T(Detail_IIterable_T, generic)
    return Detail_IIterable_T

class Detail_Inspectable(CComObject, IInspectable):
    _name_: ClassVar[str] = 'Windows.Foundation.Inspectable'
    
    def __init__(self):
        super().__init__()
        self.implement(self.GetIids)
        self.implement(self.GetRuntimeClassName)
        self.implement(self.GetTrustLevel)
        
    def GetIids_Impl(self, iidCount: IPointer[ULONG], iids: IDoublePtr[IID]) -> int:
        if not (iids and iidCount):
            return E_POINTER
        map = self._com_map_ + [(IUnknown, None), (IInspectable, None)]
        length = len(map)
        iidCount.contents.value = length
        lpIIDs = i_cast(CoTaskMemAlloc(PtrArithmetic.size(IID, length)), LPIID)
        for i in range(length):
            itf, _ = map[i]
            lpIIDs[i] = itf._iid_
        TlWritePointerToPpv(iids, lpIIDs)
        return S_OK
        
    def GetRuntimeClassName_Impl(self, className: IPointer[HSTRING]) -> int:
        buffer = create_unicode_buffer(self._name_)
        return WindowsCreateString(buffer, len(self._name_), className)
        
    def GetTrustLevel_Impl(self, trustLevel: IPointer[TrustLevel]) -> int:
        if not trustLevel:
            return E_POINTER
        trustLevel.contents.value = FullTrust
        return S_OK

def detail_item_to_out(generic: WT, pOut: int, item):
    if PtrUtil.is_pointer(generic) and issubclass(PtrUtil.get_type(generic), IUnknown):
        TlWritePointerToPpv(pOut, generic.ref())
    else:
        pGenericOut = i_cast(pOut, PTR(generic))
        contents = pGenericOut.contents
        if hasattr(contents, 'value'):
            contents.value = item
        else:
            pGenericOut.contents = item

def detail_vector_impl(generic: WT, iids: dict[str, IID]):
    illegalIID = Detail_IllegalIID()
    IVectorView_T = detail_IVectorView(generic, iids.get('IVectorView', illegalIID))
    IIterator_T = detail_IIterator(generic, iids.get('IIterator', illegalIID))
    IIterable_T = detail_IIterable(generic, IIterator_T, iids.get('IIterable', illegalIID))
    IVector_T = detail_IVector(generic, iids['IVector'])
    
    class Detail_IIterator_impl(Detail_Inspectable, IIterator_T):
        _name_ = f'Windows.Foundation.IIterator`1[[{generic}]]'
        
        iterator: typing.Iterator
        current: typing.Any
        has_current: bool
    
        def __init__(self, iterator: typing.Iterator, first: typing.Any):
            super().__init__()
            self.iterator = iterator
            self.has_current = first is not None
            self.current = first
            self.implement(self.get_Current)
            self.implement(self.get_HasCurrent)
            self.implement(self.MoveNext)
            self.implement(self.GetMany)
            
        def get_Current_Impl(self, current: IPointer[WT]) -> int:
            if not current:
                return E_POINTER
            detail_item_to_out(generic, current, self.current)
            return S_OK
            
        def get_HasCurrent(self, hasCurrent: PBOOLEAN) -> int:
            if not hasCurrent:
                return E_POINTER
            hasCurrent.contents.value = self.has_current
            return S_OK
        
        def MoveNext_Impl(self, hasCurrent: PBOOLEAN) -> int:
            try:
                current = next(self.iterator)
                self.current = current
                self.has_current = True
            except StopIteration:
                self.has_current = False
            hasCurrent.contents.value = self.has_current
            return S_OK
        
        def GetMany_Impl(self, capacity: int, value: IPointer[WT], actual: PUINT) -> int:
            if not (value and actual):
                return E_POINTER
            many = []
            while True:
                try:
                    current = next(self.iterator)
                    many.append(current)
                    self.current = current
                    self.has_current = True
                except StopIteration:
                    self.has_current = False
                    break
            length = len(many)
            actual.contents.value = length
            for i in range(length):
                detail_item_to_out(generic, PtrArithmetic.add(value, i), many[i])
            return S_OK
    
    class Detail_IVector_impl(Detail_Inspectable, IVector_T, IVectorView_T, IIterable_T):
        IVectorView_T_virtual_table = COMVirtualTable.from_ancestor(IVectorView_T).with_fieldname('IVectorView_T_vtable')
        IIterable_T_virtual_table = COMVirtualTable.from_ancestor(IIterable_T).with_fieldname('IIterable_T_vtable')
        _fields_ = IVectorView_T_virtual_table.build()
        _com_map_ = [(IVectorView_T, IVectorView_T_virtual_table)]
        _name_ = f'Windows.Foundation.Vector`1[[{generic}]]'
        
        def __init__(self, vector: list[WT]):
            super().__init__()
            self.vector = vector
            self.initialize_vtable(self.IVectorView_T_virtual_table)
            self.implement_interface(IVector_T)
            self.set_vtable_on_ctx(self.IVectorView_T_virtual_table)
            self.implement_interface(IUnknown)
            self.implement_interface(IVectorView_T)
            self.set_vtable_on_ctx(self.IIterable_T_virtual_table)
            self.implement_interface(IUnknown)
            self.implement_interface(IIterable_T)
            
        def GetIterator(self, iterator) -> int:
            if not iterator:
                return E_POINTER
            impl = Detail_IIterator_impl(iter(self.vector), self.vector[0] if self.vector else None)
            TlWritePointerToPpv(iterator, impl.ref())
            return S_OK
        
        def GetAt_Impl(self, index, item):
            if len(self.vector) <= index:
                return E_BOUNDS
            if not item:
                return E_POINTER
            detail_item_to_out(generic, item, self.vector[index])
            return S_OK
            
        def get_Size_Impl(self, size):
            if not size:
                return E_POINTER
            size.contents.value = len(self.vector)
            return S_OK
            
        def GetView_Impl(self, view):
            return self.QueryInterface(IVectorView_T._iid_, view)
            
        def IndexOf_Impl(self, value, index, found):
            if not (index and found):
                return E_POINTER
            try:
                detail_item_to_out(generic, value, self.vector.index(value))
                found.contents.value = True
                return S_OK
            except ValueError:
                found.contents.value = False
                memset(value, 0, sizeof(generic))
                return S_OK
                
        def SetAt_Impl(self, index, item):
            if len(self.vector) <= index:
                return E_BOUNDS
            self.vector[index] = item
            return S_OK
            
        def InsertAt_Impl(self, index, item):
            self.vector.insert(index, item)
            return S_OK
            
        def RemoveAt_Impl(self, index):
            if len(self.vector) <= index:
                return E_BOUNDS
            self.vector.pop(index)
            return S_OK
            
        def Append_Impl(self, value):
            self.vector.append(value)
            return S_OK
            
        def RemoveAtEnd_Impl(self):
            self.vector.pop()
            return S_OK
            
        def Clear_Impl(self):
            self.vector.clear()
            return S_OK
            
        def GetMany_Impl(self, startIndex, capacity, value, actual):
            if len(self.vector) <= startIndex:
                return E_BOUNDS
            if not (value and actual):
                return E_POINTER
            many = self.vector[startIndex:startIndex+capacity]
            length = len(many)
            actual.contents.value = length
            for i in range(length):
                detail_item_to_out(generic, PtrArithmetic.add(value, i), many[i])
            return S_OK
            
        def ReplaceAll_Impl(self, count, value):
            self.vector.clear()
            for i in range(count):
                self.vector.append(value[i])
            return S_OK
        
    detail_name_T(Detail_IVector_impl, generic)
    return Detail_IVector_impl