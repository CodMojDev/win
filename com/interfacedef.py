#
# com/interfacedef.py
#

from typing import ClassVar
from functools import wraps
from .comdefbase import *
from .guid import *
from ..wtypes import *

from datetime import datetime, timedelta

REGDB_E_CLASSNOTREG = 0x80040154

#
# RetVal helper functions
#

def RetVal_GetValue(retval):
    return retval.value

def RetVal_Dereference(retval: IPointer[WT]) -> WT:
    if not retval:
        return None
    return retval.contents

def RetVal_FILETIMEToDatetime(retval: FILETIME) -> datetime:
    int64 = i_cast2(retval.ref(), PINT64).contents.value
    microseconds = (int64 - 116444736000000000) // 10
    return datetime(1970, 1, 1) + timedelta(microseconds=microseconds)

if TYPE_CHECKING:
    from . import dispatch as _dispatch
    from .dispatch import Dispatch
else:
    _dispatch = None

def RetVal_Dispatch(retval) -> 'Dispatch':
    global _dispatch
    
    dispatch = _dispatch
    if dispatch is None:
        from . import dispatch
        _dispatch = dispatch
        
    return dispatch.Dispatch(retval.contents)

def RetVal_Bool(retval) -> bool:
    return retval.value == -1

class COMVirtualTable(VirtualTable):
    """
    Class representing a virtual table of COM Interface.
    """
    
    @staticmethod
    def from_ancestor(ancestor: TUnion['VirtualTable', 'COMInterface'], name: str=None) -> 'COMVirtualTable':
        """
        Initialize descendant virtual table from ancestor virtual table.
        """
        if name is None:
            name = get_caller_frame().f_locals['__qualname__']
        if (isinstance(ancestor, type) and 
            issubclass(ancestor, COMInterface)):
            ancestor = ancestor.virtual_table
        ancestor: VirtualTable
        virtual_table = COMVirtualTable(name)
        virtual_table.fields.extend(ancestor.fields)
        return virtual_table
    
    #def __del__(self):
    #    dbg_trace('COM-TL', f'DELETE {self.name}Vtbl!!!')
    
    def with_fieldname(self, field_name: str):
        """
        1-line variant to set the field name.
        """
        self.field_name = field_name
        return self
    
    def com_function(self, *args: type, exists: bool = False,
                     intermediate_method: bool = False) -> Callable:
        """
        Declare COM function.
        """
        return super().function(HRESULT, *args, exists=exists, intermediate_method=intermediate_method)

    def com_function_vbstyle(self, *args: type, exists: bool = False,
                     intermediate_method: bool = False, retval_index: int = -1,
                     retval_type: type = type(None), retval_function: Callable = None) -> Callable:
        """
        Declare COM function in VB style (Visual Basic).
        """
        from .dispatch import VARIANT, variant_get_value, variant_set_value, SAFEARRAY
        
        def _com_function_vbstyle(f: Callable):
            name = self._pack_name(f.__name__)
            if not exists:
                self._add(name)
            
            def _virtual_wrapper(f_self, *f_args, **kwargs) -> Callable: 
                field_name = self.field_name
                get_vtable = getattr(f_self, f'__get_{self.name}__', None)
                if get_vtable is not None:
                    field_name = get_vtable()
                vtable = i_cast(getattr(f_self, field_name), 
                                POINTER(self.VType))
                address = getattr(vtable.contents, name)
                callback = VirtualTable.func_ptr(PtrUtil.get_address(address))
                callback.restype = HRESULT
                
                if retval_index != -1:
                    list_args = list(args)
                    list_args.insert(retval_index, PTR(retval_type))
                    callback.argtypes = (THIS, *list_args)
                else:
                    list_args = list(args)
                    callback.argtypes = (THIS, *args)
                
                list_f_args = list(f_args)
                if retval_index != -1:
                    retval = retval_type()
                    list_f_args.insert(retval_index, byref(retval))
                list_f_args_result = []
                
                for i, f_arg in enumerate(list_f_args):
                    arg_type = list_args[i]
                    
                    if issubclass(arg_type, VARIANT):
                        if not isinstance(f_arg, VARIANT):
                            var = VARIANT()
                            variant_set_value(var, f_arg)
                            f_arg = var
                    
                    elif issubclass(arg_type, IMarshaller):
                        f_arg = arg_type.static_marshal_value(f_arg)
                        
                    elif PtrUtil.is_pointer_type(list_args[i]):
                        ptr_type = PtrUtil.get_type(list_args[i])
                        
                        if isinstance(f_arg, IReferenceable):
                            if issubclass(ptr_type, IReferenceable):
                                if ptr_type.allow_reference(f_arg):
                                    f_arg = f_arg.get_reference()
                            else:
                                if f_arg.allow_other_type(ptr_type):
                                    f_arg = f_arg.get_reference()
                                    
                    list_f_args_result.append(f_arg)
                    
                hr = callback(byref(f_self), *list_f_args_result)
                if FAILED(hr): raise COMError(hr)
                
                if retval_index != -1:
                    if isinstance(retval, VARIANT):
                        return variant_get_value(retval)
                    if isinstance(retval, IUnpackable):
                        retval = retval.unpack()
                    if callable(retval_function):
                        return retval_function(retval)
                    return retval
                return None
            
            if not intermediate_method:
                _virtual_wrapper = wraps(f)(_virtual_wrapper)
            else:
                @wraps(f)
                def _intermediate(*args, **kwargs):
                    return f(*args, **kwargs, function=_virtual_wrapper)
                
            if intermediate_method:
                setattr(_intermediate, 'proto', WINFUNCTYPE(HRESULT, THIS, *args))
                setattr(_intermediate, 'f', f)
                
                return _intermediate
            
            setattr(_virtual_wrapper, 'proto', WINFUNCTYPE(HRESULT, THIS, *args))
            setattr(_virtual_wrapper, 'f', f)
            
            return _virtual_wrapper
    
        return _com_function_vbstyle
    
    def com_function_vbstyle_nonvariant(self, *args: type, exists: bool = False,
                     intermediate_method: bool = False, retval_index: int = -1,
                     retval_type: type = type(None), retval_function: Callable = None) -> Callable:
        """
        Declare COM function in VB style (Visual Basic).
        Without support of VARIANT type.
        """
        def _com_function_vbstyle(f: Callable):
            name = self._pack_name(f.__name__)
            if not exists:
                self._add(name)
            
            def _virtual_wrapper(f_self, *f_args, **kwargs) -> Callable: 
                callback = getattr(f, 'callback', None)
                if callback is None:
                    field_name = self.field_name
                    get_vtable = getattr(f_self, f'__get_{self.name}__', None)
                    if get_vtable is not None:
                        field_name = get_vtable()
                    vtable = i_cast(getattr(f_self, field_name), 
                                    POINTER(self.VType))
                    address = getattr(vtable.contents, name)
                    callback = VirtualTable.func_ptr(PtrUtil.get_address(address))
                    callback.restype = HRESULT
                    
                    if retval_index != -1:
                        list_args = list(args)
                        list_args.insert(retval_index, PTR(retval_type))
                        callback.argtypes = (THIS, *list_args)
                    else:
                        callback.argtypes = (THIS, *args)
                    
                    setattr(f, 'callback', callback)
                
                list_f_args = list(f_args)
                if retval_index != -1:
                    retval = retval_type()
                    list_f_args.insert(retval_index, byref(retval))
                    
                hr = callback(byref(f_self), *list_f_args)
                if FAILED(hr): raise COMError(hr)
                
                if retval_index != -1:
                    if isinstance(retval_type, IReferenceable):
                        retval = retval_type.dereference(retval)
                    if PtrUtil.is_pointer(retval_type):
                        ptr_type = PtrUtil.get_type(retval_type)
                        if issubclass(ptr_type, IReferenceable):
                            retval = ptr_type.dereference(retval.contents if retval else NULL)
                    if callable(retval_function):
                        return retval_function(retval)
                    return retval
                return None
            
            if not intermediate_method:
                _virtual_wrapper = wraps(f)(_virtual_wrapper)
            else:
                @wraps(f)
                def _intermediate(*args, **kwargs):
                    return f(*args, **kwargs, function=_virtual_wrapper)
                
            if intermediate_method:
                setattr(_intermediate, 'proto', WINFUNCTYPE(HRESULT, THIS, *args))
                setattr(_intermediate, 'f', f)
                
                return _intermediate
            
            setattr(_virtual_wrapper, 'proto', WINFUNCTYPE(HRESULT, THIS, *args))
            setattr(_virtual_wrapper, 'f', f)
            
            return _virtual_wrapper
    
        return _com_function_vbstyle

from .. import _defbase_ctypinit as _defb_ci

from ..wet.trace import *

dbgplus_provider = WET_PROVIDER('DbgPlus')

class COMInterface(CStructure, IReferenceable, IUnpackable):
    """
    Class representing a COM Interface.
    """
    
    virtual_table: ClassVar[COMVirtualTable]
    _iid_: ClassVar[IID]
    
    _virtual_table_on_ctx: COMVirtualTable
    _registry: list
    
    @classmethod
    def iid(self) -> IID:
        """
        IID of the interface.
        """
        return self._iid_
    
    def implement(self, function: Callable):
        """
        Implement the given function in current on-context virtual table.
        Name declaring contract: `<function name>_Impl`.
        
        Needs setted on-context virtual table with `set_vtable_on_ctx`.
        """
        dbg_trace(dbgplus_provider, f'{self.virtual_table.name}::{function.__name__}')
        
        virtual_table = self._virtual_table_on_ctx
        function_name = function.__name__
        
        def thunk(this, *args, **kwargs):
            thunk.__name__ = f'{virtual_table.name}_{function_name}_Thunk'
            thunk.__qualname__ = thunk.__code__.co_name = thunk.__code__.co_qualname = thunk.__name__
            dbg_trace(dbgplus_provider, f'UnusedThis={this}, This={self.virtual_table.name}')
            return getattr(self, function_name + '_Impl')(*args)
        
        callback = getattr(function, 'proto')(thunk)
        self.stub(function, callback)
        registry = getattr(self, '_registry', None)
        if registry is None:
            registry = []
            self._registry = registry
        registry.append(callback)
        
    def stub(self, function: Callable, stub: WINFUNCTYPE):
        """
        Implement the given function as a stub
        (or implement a function bypassing the naming contract)
        in current on-context virtual table.
        
        Needs setted on-context virtual table with `set_vtable_on_ctx`.
        """
        virtual_table = self._virtual_table_on_ctx
        setattr(i_cast(getattr(self, virtual_table.field_name), 
                       PTR(virtual_table.VType)).contents, function.__name__, i_cast(stub, PVOID))
        
    def initialize_vtable(self, virtual_table: COMVirtualTable):
        """
        Initialize the given virtual table to use.
        """
        setattr(self, virtual_table.field_name, 
                i_cast(pointer(virtual_table.VType()), PVOID))
        
    def set_vtable_on_ctx(self, virtual_table: COMVirtualTable):
        """
        Set current on-context virtual table.
        Used in `implement` and `stub` to 
        resolve what virtual table needed to use.
        """
        self._virtual_table_on_ctx = virtual_table
        
    def get_reference(self):
        return self.ref()
    
    def allow_other_type(self, typ):
        return False
    
    @classmethod
    def allow_reference(cls, value):
        return isinstance(value, cls)
    
    @classmethod
    def dereference(cls, reference):
        if not reference: return NULL
        return i_cast(reference, PTR(cls)).contents
    
class COMLibrary:
    """
    Class representing a COM Library.
    """
    
    _version_: ClassVar[tuple[int, int] | list[int] | str]
    _libid_: ClassVar[CLSID]
    
    @classmethod
    def libid(cls) -> CLSID:
        """
        LIBID of the library.
        """
        return cls._libid_
    
    @classmethod
    def version(cls) -> tuple[int, int] | list[int] | str:
        """
        Version of the library.
        
        Held as tuple/list[int, int] or as string in format '%d.%d'.
        """
        return cls._version_