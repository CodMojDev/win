"""
`defbase.py`

Library core module, defining all
architecture, typing interfaces,
helper functions, C++ infrastructure and
abstraction helpers.
"""

from typing import (Callable, Any, List, 
                    Union as TUnion, Generic, TypeVar, 
                    Type, Dict, Optional, ClassVar, Self)
from functools import wraps

import warnings

__all__ = [
    "declare",
    "unicode",
    "module_to_namespace",
    "using_namespace",
    "IPointer",
    "IFunction",
    "i_cast",
    "foreign",
    "link_library",
    "IInterface",
    "IFunctionType",
    "THIS",
    "AccessError",
    "W_WinDLL",
    "W_CDLL",
    "foreign_optimized",
    "VirtualTable",
    "IDoublePtr", 
    "reinterpret_cast",
    "static_cast",
    "PtrArithmetic",
    "PtrUtil",
    "std",
    "CStructure",
    "WinWarning",
    "AccessError",
    "Ref",
    "Template",
    "W_OleDLL",
    "W_PyDLL",
    "AssertTool",
    "CClass",
    "ASSERT",
    "array_after_structure",
    "POINTER",
    "PTR",
    "DOUBLE_PTR",
    "delegate",
    "TemplateFunction",
    "get_template",
    "TUnion",
    "get_py_frame",
    "get_caller_frame",
    "frame_versioning",
    "IArray",
    "INamespace",
    "get_library",
    "get_win_library",
    "filter_self",
    "CUnion",
    "CFuncPtr",
    "declare_fields",
    "byref",
    "IVoidPtr",
    "interface_abstract_method",
    "c_void_p",
    "i_cast2",
    "WT", "WT2",
    "WT_ADDRLIKE",
    "IInteger",
    "IChar",
    "IWideChar",
    "IAliasable",
    "IAliasableGeneric",
    "IShort", "IUnsignedShort",
    "IInt", "IUnsignedInt",
    "ILong", "IUnsignedLong",
    "IInt64", "IUnsignedInt64",
    "ISizeT", "ISignedSizeT",
    "IArrayFixedSize",
    "ICustomizable",
    "IBool", "IBool64",
    "IFloat", "IDouble",
    "IInt32", "IUnsignedInt32",
    "IInt16", "IUnsignedInt16",
    "IInt8", "IUnsignedInt8",
    "reset_annotations",
    "IAnonymous",
    "IPack",
    "IAliasableGenericWithPayload",
    "format_hex",
    "WT_LPSTR", "WT_LPWSTR",
    "IUlong", "IULong",
    "IUint", "IUInt",
    "IUshort", "IUShort",
    "IByte", "IWord",
    "IDword", "IQword",
    "IUnsignedLongLong", "ILongLong",
    "IULongLong", "IUlonglong",
    "IUInt8", "IUint8", 
    "IUInt16", "IUint16",
    "IUInt32", "IUint32",
    "IUInt64", "IUint64",
    "IIntPtr", "ILongPtr",
    "IDwordPtr", "IUhalfPtr",
    "IUIntPtr", "IUnsignedIntPtr", "IUintPtr",
    "IUnsignedHalfPtr", "IUHalfPtr",
    "IUnsignedLongPtr", "IULongPtr", "IUlongPtr",
    "IHandle", 
    "ICharArray", "IWideCharArray",
    "WT_HANDLE", "flexible_array", 
    "LI",
    "IWideCharArrayFixedSize", "ICharArrayFixedSize"
]

_WT_UNSTABLE_API = True

if _WT_UNSTABLE_API:
    __all__.extend([
        'cbyref', 'CByref',
        'CVoidP'
    ])

def format_hex(value: int, zeros: int) -> str:
    """
    Format the hexadecimal value with leading `zeros`.
    """
    return '0x' + (hex(value)[2:].zfill(zeros))

WT = TypeVar('_WT')
WT2 = TypeVar('_WT2')

def interface_abstract_method(f: WT) -> WT:
    """
    Declare the interface method as abstract.
    """
    @wraps(f)
    def _interface_abstract_method(*args, **kwargs):
        raise RuntimeError(f"'{f.__qualname__}' method is abstract.")
    _interface_abstract_method._abstract = True
    return _interface_abstract_method

class IInterface:
    """
    Base class for type-safe typing interfaces.
    """
    
    @interface_abstract_method
    def __init__(self): ...
    
    @staticmethod
    def is_abstract(method: Callable) -> bool:
        """
        Check the given method is abstract
        (declared with a `@interface_abstract_method`).
        """
        return hasattr(method, '_abstract')
    
class INamespace:
    """
    Base class for "namespaces", they are not instantiable.
    """
    
    @interface_abstract_method
    def __init__(self): ...
    
class IFunctionType(IInterface):
    """
    Type-safe interface over
    ctypes library function type
    """
    
    _argtypes_: List[type]
    _restype_: type
    _flags_: int
    
    @staticmethod
    def is_self(cls: type) -> bool:
        """
        Check the `cls` function type is IFunctionType-compatible.
        """
        return (isinstance(cls, type) and 
                hasattr(cls, '_argtypes_') and 
                hasattr(cls, '_restype_') and
                hasattr(cls, '_flags_'))
    
class IFunction(IInterface):
    """
    Type-safe interface over 
    ctypes library function.
    """
    
    def __call__(*args: Any, **kwargs: Any): ...
    
    argtypes: List[type]
    restype: type
    flags: type
    
    @staticmethod
    def is_self(instance: Any) -> bool:
        """
        Check the `instance` function type is IFunction-compatible.
        """
        return (not isinstance(instance, type) and 
                hasattr(instance, 'argtypes') and 
                hasattr(instance, 'restype'))
    
import sys
    
def frame_versioning(noframe_impl: Callable) -> Callable:
    """
    Version the two implementations: function original and no-frame stub.
    
    Use in the Python interpreter versions which don't have `sys._getframe`.
    """
    def _frame_versioning(f):
        if hasattr(sys, '_getframe'):
            return f
        else:
            @wraps(f)
            def _function(*args, **kwargs):
                warnings.warn('Cannot get Python frame, '
                              f'Implementation of {f.__name__} '
                              'is inaccessible', category=WinWarning,
                              stacklevel=1)
                return noframe_impl(*args, **kwargs)
            return _function
    return _frame_versioning

def _frame_getter_throw(*args):
    raise RuntimeError('Cannot get Python frame object.')

@frame_versioning(noframe_impl=_frame_getter_throw)
def get_py_frame(depth: int): return sys._getframe(depth+1)
    
@frame_versioning(noframe_impl=_frame_getter_throw)
def get_caller_frame(): return sys._getframe(2)
    
from ctypes import Structure, byref, POINTER as _POINTER, pointer, c_int, c_void_p
from _ctypes import CFuncPtr

class IArray(IInterface, Generic[WT]):
    """
    Type-safe interface over
    ctypes array.
    """
    
    @interface_abstract_method
    def __getitem__(self, index: int) -> WT: ...
    
    @interface_abstract_method
    def __setitem__(self, index: int, value: WT) -> WT: ...
    
class IArrayFixedSize(IInterface, Generic[WT, WT2]):
    """
    Type-safe interface over 
    ctypes array by fixed size 
    (for @CStructure.make).
    """
    
    @interface_abstract_method
    def __getitem__(self, index: int) -> WT: ...
    
    @interface_abstract_method
    def __setitem__(self, index: int, value: WT) -> WT: ...

class IPointer(IArray[WT]):
    """
    Type-safe interface over
    ctypes pointer.
    """
    
    contents: WT
        
from typing import TypeAlias, Tuple, Mapping

IDoublePtr: TypeAlias = IPointer[IPointer[WT]]
    
class IVoidPtr(IInterface):
    """
    Type-safe interface over 
    ctypes void* pointer.
    """
    
    value: int

from . import _defbase_ctypinit

_defbase_ctypinit.Init()

if _WT_UNSTABLE_API:  
    from _ctypes import _SimpleCData as SimpleCData

    CData = SimpleCData.__base__

    class ICData(IInterface):
        _b_base_: int
        _b_needsfree_: bool
        _objects: Mapping[Any, int] | None
        def __buffer__(self, flags: int, /) -> memoryview: ...
        def __ctypes_from_outparam__(self, /) -> Self: ...


    # don't know how to bypass ctypes check
    # for only _CArgObject type and not its
    # descendant. This API is marked as unstable
    # so DON'T use this (if you want, use this, but i awared you).

    class CByref(_defbase_ctypinit.CArgObject, IPointer[WT]):
        """
        ## <!> UNSTABLE API !!!
        Enhanced byref class over CArgObject.
        
        Implements IPointer and IArray typing interfaces.
        """
        
        _carg: _defbase_ctypinit.PyCArgObject
        
        @property
        def contents(self) -> WT:
            """## <!> UNSTABLE API !!!"""
            return self.ptr().contents
        
        @contents.setter
        def contents(self, contents: WT):
            """## <!> UNSTABLE API !!!"""
            self.ptr().contents = _ptr_to_type(self)(contents)
            self._obj.value = contents
        
        def __getitem__(self, index: int) -> WT:
            return self.ptr()[index]
        
        def __setitem__(self, index: int, value: WT):
            if index == 0 and hasattr(self._obj, 'value'):
                self._obj.value = _ptr_to_type(self)(value)
            self.ptr()[index] = value
        
        def ptr(self) -> IPointer[WT]:
            """
            ## <!> UNSTABLE API !!!
            Explicitly convert byref type to 
            normal ctypes pointer.
            """
            
            return i_cast(self, PTR(_ptr_to_type(self)))
            
        @classmethod
        def make(cls, obj: ICData) -> Optional['CByref']:
            """
            ## <!> UNSTABLE API !!!
            Make the CByref enhanced reference to object (CData).
            """
            if not isinstance(obj, CData):
                raise TypeError('expected CData instance')
            
            parg: IPointer[_defbase_ctypinit.PyCArgObject[CByref]]
            parg = _defbase_ctypinit.New_PyCArgObject(CByref)
            
            if parg is None:
                return None
            
            cbyref: CByref = _defbase_ctypinit.Init_PyCArgObject(parg, obj)
            cbyref._carg = parg.contents
            
            return cbyref
        
    def cbyref(obj: WT) -> CByref[WT]:
        """
        ## <!> UNSTABLE API !!!
        Get the CByref enhanced sreference to object.
        """
        return CByref.make(obj)
        
    # is not fully compatible with ctypes
    # so i don't know how to deal with it.

    # This API is marked as unstable
    # so DON'T use this (if you want, use this, but i awared you).
        
    class CVoidP(c_void_p, IVoidPtr):
        """
        ## <!> UNSTABLE API !!!
        The enhanced `c_void_p` implementation
        that supports `CByref` enhanced references.
        """
        @classmethod
        def from_param(cls, param): 
            if isinstance(param, CByref):
                if _defbase_ctypinit.PyCArgObject_CAST_DEREF(param).tag == b'P':
                    return param
                
            return super().from_param(param)
        
        def __repr__(self) -> str:
            return f'<CVoidP address={format_hex(PtrUtil.get_address(self), sizeof(c_void_p))}>'
    
    # c_void_p = CVoidP

def PTR(typ: Type[WT]) -> Type[IPointer[WT]]:
    """
    Make the pointer to type.
    """
    
    if typ is None: return c_void_p
    
    if issubclass(typ, c_wchar):
        return c_wchar_p
    
    if issubclass(typ, c_char):
        return c_char_p
    
    return _POINTER(typ)

def DOUBLE_PTR(typ: Type[WT]) -> Type[IDoublePtr[WT]]:
    """
    Make the double pointer to type. Shortcut for `PTR(PTR(type))`.
    """
    return PTR(PTR(typ))

POINTER = PTR

class VirtualTable:
    """
    Class representing interface to C++ Virtual table.
    """
    
    class _FuncPtr(CFuncPtr):
        _restype_ = c_int
        _flags_ = 0x0
    
    field_name: str
    fields: list
    VType: type
    name: str
    
    func_ptr: Type[CFuncPtr] = _FuncPtr
    
    @classmethod
    def from_ancestor(cls, ancestor: Self, name: str) -> Self:
        """
        Initialize descendant virtual table from ancestor virtual table.
        """
        virtual_table = cls(name)
        virtual_table.fields.extend(ancestor.fields)
        return virtual_table
    
    def __init__(self, name: str, custom_field: str='vtable'):
        self.field_name = custom_field
        self.VType = type(None)
        self.fields = []
        self.name = name
    
    @staticmethod
    def set_func_ptr(func_ptr: Type[CFuncPtr]):
        """
        Set function pointer type in VirtualTable
        """
        VirtualTable.func_ptr = func_ptr
        
    def _pack_name(self, name: str) -> str:
        if name.startswith('__'):
            return '_P_' + name
        return name
    
    def _add(self, name: str):
        self.fields.append((name, c_void_p))
        
    def build(self) -> List[tuple]:
        """
        Build the virtual table type.
        """
        self.VType = type(self.name + '_vtbl', (CStructure,), {'_fields_': self.fields})
        return [(self.field_name, c_void_p)]
    
    def __repr__(self) -> str:
        return f'<{self.name} virtual table>'
        
    def pure(self, *args, exists: bool = False):
        """
        Pure method.
        Deprecated. Use function(...) instead. 
        Pure key argument doesn't supported anymore.
        """
        return self.function(*args, exists=exists)
    
    def skip(self):
        """
        Skip method.
        """
        self._add('_Empty' + str(len(self.fields)))
        
    def skip_count(self, count: int):
        """
        Skip N methods.
        """
        for _ in range(count):
            self.skip()
        
    def function(self, 
                 ret: type, 
                 *args: type, 
                 exists: bool = False,
                 result_function: Optional[Callable] = None,
                 intermediate_method: bool = False) -> Callable:
        """
        Virtual function decorator.
        """
        def _function(f: Callable) -> Callable:
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
                callback = VirtualTable.func_ptr(address)
                callback.restype = ret
                callback.argtypes = (THIS, *args)
                
                result = callback(byref(f_self), *f_args)
                if callable(result_function):
                    return result_function(result)
                return result
            
            if not intermediate_method:
                _virtual_wrapper = wraps(f)(_virtual_wrapper)
            else:
                @wraps(f)
                def _intermediate(*args, **kwargs):
                    return f(*args, **kwargs, function=_virtual_wrapper)
                
            if intermediate_method:
                return _intermediate
            
            return _virtual_wrapper
        
        return _function
    
    def copy(self) -> Self:
        """
        Copy the virtual table instance.
        """
        virtual_table = self.__class__(self.name)
        virtual_table.fields = self.fields.copy()
        return virtual_table
    
THIS = c_void_p
    
class AccessError(RuntimeError): 
    """
    Access Error
    """

class WinWarning(Warning): 
    """
    Windows Warning
    """

class _NullFunction:
    __slots__ = ('library', '_name')
    
    _name: TUnion[str, int]
    library: str
    
    def __init__(self, library: str, name: TUnion[str, int]):
        self.library = library
        self._name = name
        
    @property
    def name(self):
        if isinstance(self._name, int):
            return f'#{self._name}'
        return self._name
    
    def __call__(self, *args, **kwargs):
        raise RuntimeError(f'Implementation of function {self.library}!{self.name} is missing')

from _ctypes import (FUNCFLAG_STDCALL, FUNCFLAG_CDECL, FUNCFLAG_PYTHONAPI)
from ctypes import cast, CDLL
from typing import Optional

class W_CDLL(CDLL):
    """An instance of this class represents a loaded dll/shared
    library, exporting functions using the standard C calling
    convention (named 'cdecl' on Windows).

    The exported functions can be accessed as attributes, or by
    indexing with the function name.  Examples:

    lib.qsort -> IFunction
    
    **_Extended version._**
    """
    def __getitem__(self, name_or_ordinal):
        try:
            func = self._FuncPtr((name_or_ordinal, self))
            if not isinstance(name_or_ordinal, int):
                func.__name__ = name_or_ordinal
            return func
        except Exception:
            return _NullFunction(self._name, name_or_ordinal)
    
    def foreign(self,
                ret: type, 
                *args: type, 
                name: Optional[str] = None,
                ordinal: Optional[int] = None,
                class_method: bool = False,
                result_function: Optional[Callable] = None,
                intermediate_method: bool = False) -> Callable:
        """
        Foreign method declare
        """
        return foreign_optimized(ret, 
                                 *args, 
                                 library=self, 
                                 name=name, 
                                 ordinal=ordinal, 
                                 class_method=class_method,
                                 result_function=result_function,
                                 intermediate_method=intermediate_method)
        
    @property
    def handle(self) -> int:
        """
        Handle to a library. 
        In WinAPI, it is HINSTANCE/HMODULE.
        """
        return self._handle
    
    @property
    def name(self) -> str:
        """
        Name of a library.
        """
        return self._name
    
    @property
    def func_ptr(self) -> Type[CFuncPtr]:
        """
        Function pointer of a library.
        Presented as opaque _ctypes.CFuncPtr descendant.
        """
        return self._FuncPtr

class W_WinDLL(W_CDLL):
    """
    This class represents a dll exporting functions using the
    Windows stdcall calling convention.
    
    **_Extended version._**
    """
    
    _func_flags_ = FUNCFLAG_STDCALL
    
from ctypes import HRESULT

class W_OleDLL(W_WinDLL):
    """
    This class represents a dll exporting functions using the
    Windows stdcall calling convention, and returning HRESULT.
    HRESULT error values are automatically raised as OSError
    exceptions.
    
    **_Extended version._**
    """
    _func_restype_ = HRESULT
    
class W_PyDLL(W_CDLL):
    """
    This class represents the Python library itself.  It allows
    accessing Python API functions.  The GIL is not released, and
    Python exceptions are handled correctly.
    
    **_Extended version._**
    """
    _func_flags_ = FUNCFLAG_CDECL | FUNCFLAG_PYTHONAPI

# Address-like typing interface (void*, T*, Python int).
WT_ADDRLIKE: TypeAlias = TUnion[int, IVoidPtr, IPointer[WT]]

def declare(func: IFunction, ret: type, *args: type) -> IFunction:
    """
    Declare the function
    """
    if isinstance(func, _NullFunction):
        warnings.warn(f'Function {func._name} from {func.library} is not available', category=WinWarning, stacklevel=2)
        return func
    
    if not args:
        pass
    elif args[0] == None and len(args) == 1:
        args = []
        
    args = list(args)
    
    for i, arg in enumerate(args):
        if not isinstance(arg, type):
            raise RuntimeError(f"Invalid argument '{arg}' for function {func} at position {i}.")

    func.argtypes = args
    func.restype = ret

    return func

def foreign_optimized(ret: type,
                      *args: type,
                      library: CDLL = None,
                      name: Optional[str] = None,
                      ordinal: Optional[int] = None,
                      class_method: bool = False, 
                      result_function: Optional[Callable] = None, 
                      intermediate_method: bool = False) -> Callable:
    """
    Foreign Declare, optimized version.
    Recommended to use, FFI notation.
    """
    if library is None:
        raise RuntimeError('Library cannot be None.')
    
    def _foreign(f: Callable) -> Callable:
        function: Optional[IFunction] = None
        
        nonlocal name, args
        if name is None:
            if ordinal is None:
                name = f.__name__
                
        if ordinal is None:
            function = library[name]
        else:
            function = library[ordinal]
            
        if function is None:
            if ordinal is None:
                raise LookupError(f'Function {name} not found in all linked libraries.')
            raise LookupError(f'Function #{ordinal} not found in all linked libraries.')
        
        if class_method:
            args = (THIS, *args)
        function = declare(function, ret, *args)
        
        def _function(*args, **kwargs):
            if class_method:
                result = function(pointer(args[0]), *(args[1:]))
            else:
                result = function(*args)
            if callable(result_function):
                return result_function(result)
            return result
        
        if not intermediate_method:
            return wraps(f)(_function)
        else:
            @wraps(f)
            def _intermediate(*args, **kwargs):
                return f(*args, **kwargs, function=_function)
            return _intermediate
    
    return _foreign

def foreign(ret: type, 
            *args: type, 
            explicit_lib: Optional[str] = None, 
            name: Optional[str] = None,
            ordinal: Optional[int] = None,
            class_method: bool = False, 
            result_function: Optional[Callable] = None,
            intermediate_method: bool = False) -> Callable:
    """
    Foreign Declare
    Recommended to use, FFI notation.
    
    If you can, please, use the optimized version.
    """
    def _foreign(f: Callable) -> Callable:
        function: Optional[IFunction] = None
        
        nonlocal name
        if name is None:
            if ordinal is None:
                name = f.__name__
        
        if explicit_lib is not None:
            if explicit_lib not in _defb_state._linked_libraries:
                link_library(explicit_lib)
                
            library = _defb_state._linked_libraries[explicit_lib]
            if ordinal is None:
                if hasattr(library, name):
                    function = library[name]
            else:
                function = library[ordinal]
        else:
            for library in _defb_state._linked_libraries.values():
                if ordinal is None:
                    if hasattr(library, name):
                        function = library[name]
                else:
                    function = library[ordinal]
        
        if function is None:
            if ordinal is None:
                raise LookupError(f'Function {name} not found in all linked libraries.')
            raise LookupError(f'Function #{ordinal} not found in all linked libraries.')
        
        if class_method:
            args = (THIS, *args)
        function = declare(function, ret, *args)
        
        def _function(*args, **kwargs):
            if class_method:
                result = function(pointer(args[0]), *(args[1:]))
            else:
                result = function(*args)
            if callable(result_function):
                return result_function(result)
            return result
    
        if not intermediate_method:
            _function = wraps(f)(_function)
        else:
            @wraps(f)
            def _intermediate(*args, **kwargs):
                return f(*args, **kwargs, function=_function)
        
        if intermediate_method:
            return _intermediate
        
        return _function
    
    return _foreign
    
def filter_self(args_tuple: tuple, typ: type) -> tuple:
    """
    Filter the `self` from arguments tuple.
    """
    
    if len(args_tuple) == 0: return args_tuple
    
    if isinstance(args_tuple[0], typ):
        return args_tuple[1:]
    
    return args_tuple
    
class Template(Generic[WT]):
    """
    Class simulating behavior of C++ Template.
    """
    
    args: Tuple[WT]
    
    def get_pointer_type(self) -> Type[IPointer[WT]]:
        """
        Shortcut for `PTR(self.get_single_type())`.
        """
        return PTR(self.get_single_type())
    
    def get_single_type(self) -> WT:
        """
        Get single type, which passed into template type arguments.
        
        Needed `save_template` to be called before and the 
        length of arguments count must be equal 1.
        """
        assert len(self.args) == 1
        return self.args[0]
    
    def save_template(self):
        """
        Save the template into instance. 
        Necessarily needed to call this in
        object constructor.
        """
        if hasattr(self.__class__, '_args_global'):
            setattr(self, 'args', self._args_global)
            delattr(self.__class__, '_args_global')
    
    @classmethod
    def __class_getitem__(cls, args: Tuple[type, ...]) -> Type['Template']:
        cls._args_global = (args,) if not isinstance(args, tuple) else args
        
        return cls
    
class TemplateFunction(Generic[WT]):
    """
    Class simulating behavior of C++ Function Template.
    """
    
    f: Callable
        
    def __init__(self, f: Callable):
        self.f = f
        
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        self.__self__ = obj
        return self
    
    def __getitem__(self, args: Tuple[type, ...]) -> Callable:
        instance = Template()
        instance.args = (args,) if not isinstance(args, tuple) else args
        def _template_function(*f_args, **kwargs) -> Any:
            if hasattr(self, '__self__'):
                f_args = (self.__self__, *f_args)
            return self.f(*f_args, **kwargs, template=instance)
        return wraps(self.f)(_template_function)

def get_template() -> Template:
    """
    Get the template instance in the template function implementation.
    """
    return get_caller_frame().f_locals['kwargs']['template']

from ctypes import sizeof

class PtrUtil:
    def get_address(ptr: IPointer[WT]) -> int:
        return i_cast2(ptr, c_void_p).value
    
    def get_type(ptr: IPointer[WT]) -> WT:
        """
        Get pointer type.
        """
        return _ptr_to_type(ptr)
    
    def is_pointer(ptr: TUnion[IPointer[WT], Any]) -> bool:
        """
        Check object is pointer.
        """
        return _is_ptr(ptr)
    
class PtrArithmetic:
    @staticmethod
    def add(ptr: IPointer[WT], *offsets: int) -> IPointer[WT]:
        ptr_type = PtrUtil.get_type(ptr)
        return i_cast2(PtrUtil.get_address(ptr) + (sum(offsets) * sizeof(ptr_type)), POINTER(ptr_type))
    
    @staticmethod
    def sub(ptr: IPointer[WT], *offsets: int) -> IPointer[WT]:
        ptr_type = PtrUtil.get_type(ptr)
        return i_cast2(PtrUtil.get_address(ptr) - (sum(offsets) * sizeof(ptr_type)), POINTER(ptr_type))
    
    @staticmethod
    def increment(ptr: IPointer[WT]) -> IPointer[WT]:
        ptr_type = PtrUtil.get_type(ptr)
        return i_cast2(PtrUtil.get_address(ptr) + sizeof(ptr_type), POINTER(ptr_type))
    
    @staticmethod
    def decrement(ptr: IPointer[WT]) -> IPointer[WT]:
        ptr_type = PtrUtil.get_type(ptr)
        return i_cast2(PtrUtil.get_address(ptr) - sizeof(ptr_type), POINTER(ptr_type))
    
    @staticmethod
    def greater(ptr: IPointer, other: IPointer) -> bool:
        return PtrUtil.get_address(ptr) > PtrUtil.get_address(other)
    
    @staticmethod
    def lesser(ptr: IPointer, other: IPointer) -> bool:
        return PtrUtil.get_address(ptr) < PtrUtil.get_address(other)
    
    @staticmethod
    def greater_equal(ptr: IPointer, other: IPointer) -> bool:
        return PtrUtil.get_address(ptr) >= PtrUtil.get_address(other)
    
    @staticmethod
    def lesser_equals(ptr: IPointer, other: IPointer) -> bool:
        return PtrUtil.get_address(ptr) <= PtrUtil.get_address(other)
    
    @staticmethod
    def equals(ptr: IPointer, other: IPointer) -> bool:
        return PtrUtil.get_address(ptr) == PtrUtil.get_address(other)

from ctypes import Union, c_wchar_p, c_int
from .cpreproc import _CPreprocState

ucrtbased = W_WinDLL('ucrtbased.dll')
msvcrt = W_WinDLL('msvcrt.dll')

class AssertTool:
    @staticmethod
    @ucrtbased.foreign(None, c_wchar_p, c_wchar_p, 
                       c_wchar_p, c_int, c_void_p,
                       name='_invoke_watson')
    def invoke_watson(_Expression: str,
                      _FunctionName: str,
                      _FileName: str,
                      _LineNo: int,
                      _Reserved: int): 
        """
        Invoke Microsoft Watson process
        for immediately crash the program and send report.
        """
        
    @staticmethod
    @ucrtbased.foreign(c_int, c_int, c_wchar_p, c_int,
                       c_wchar_p, c_wchar_p, 
                       name='_CrtDbgReportW')
    def CrtDbgReport(reportType: int, filename: str,
                     linenumber: int, moduleName: str,
                     *args) -> int: 
        """
        Generates a report with a debugging message and sends the report to three possible destinations (debug version only).
        """
        
    @staticmethod
    @msvcrt.foreign(None, name='_CrtDbgBreak')
    def CrtDbgBreak():
        """
        Sets a break point on a particular line of code. (Used in debug mode only.)
        """
        
    @staticmethod
    @ucrtbased.foreign(None, c_wchar_p, c_wchar_p, 
                       c_int, name='_wassert')
    def wassert(message: str, filename: str, line: int): 
        """
        Evaluates an expression and, when the result is false, prints a diagnostic message and aborts the program.
        """

def _ASSERT_NoFrame(expr: bool):
    warnings.warn('ASSERT functionality is not accessed, '
                    'cannot get caller frame.',
                    category=WinWarning, stacklevel=1)
    assert expr
    
@frame_versioning(noframe_impl=_ASSERT_NoFrame)
def ASSERT(expr: bool):
    """
    Assert the given expression to True.
    """
    
    if not expr:
        caller_frame = get_caller_frame()
        filename = caller_frame.f_code.co_filename
        lineno = caller_frame.f_lineno
        
        if filename != '<stdin>':
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                line = lines[lineno-1]
        else:
            line = 'False'
        
        AssertTool.wassert(line, filename, lineno)
    
from typing import Self

GenericAlias = type(Generic[WT])

class IGenericAlias(IInterface):
    __origin__: type
    __args__: list
    
def reset_annotations():
    """
    Reset annotations in the class definition.
    Call this if you need to exclude the 
    just-defined type annotations in class
    from `__annotations__` and 
    `@CStructure.make`/`@CUnion.make` handling.
    """
    get_caller_frame().f_locals['__annotations__'] = {}
    
def _make_internal(cls: type) -> type:
    fields_customed = []
    anonymous = []
    pack = None
    fields = []
    for field, typ in cls.__annotations__.items():
        generic_alias: IGenericAlias
        
        if isinstance(typ, GenericAlias):
            generic_alias = typ
            origin = generic_alias.__origin__
            if origin is IAnonymous:
                typ, = generic_alias.__args__
                anonymous.append(field)
            elif origin is IPack:
                pack, = generic_alias.__args__
                continue
            
        if isinstance(typ, GenericAlias):
            generic_alias = typ
            typ = _resolve_genericalias(generic_alias)
        else:
            if isinstance(typ, ICustomizable):
                fields_customed.append((field, typ._custom_))
                field = '_' + field
            typ = _resolve_type(typ)
        fields.append((field, typ))
        
    dictionary = {'_fields_': fields, '_anonymous_': anonymous}
    if pack is not None:
        dictionary['_pack_'] = pack
    cls = type(cls.__name__, (cls,), dictionary)
    for field_customed, custom in fields_customed:
        field_typed(cls, field_customed, '_' + field_customed, custom)
    
    return cls
    
from typing import TYPE_CHECKING
    
class CStructure(Structure):
    """
    Enhanced structure type builded over
    ctypes.Structure class.
    """
    
    _inter_process_version: ClassVar[Type[Self]]
    fields: ClassVar[List[tuple]]
    
    def __init_subclass__(cls, *args, **kwargs):
        cls._pack_ = _CPreprocState._cur_pack
        
    @classmethod
    def size(cls):
        """
        Alias to sizeof(cls).
        """
        return sizeof(cls)
    
    @classmethod
    def PTR(cls) -> Type[IPointer[Self]]:
        """
        Alias to POINTER(cls).
        """
        return POINTER(cls)
    
    @classmethod
    def DOUBLE_PTR(cls) -> Type[IDoublePtr[Self]]:
        """
        Alias to DOUBLE_PTR(cls) or POINTER(POINTER(cls)).
        """
        return DOUBLE_PTR(cls)
    
    @classmethod
    def NULL(cls) -> IPointer[Self]:
        """
        NULL pointer to structure.
        """
        return cls.PTR()()
    
    def virt_delegate(self, *args, **kwargs) -> Any:
        """
        Part of Intermediate Methods architecture.
        
        Delegate received virtual function into
        Intermediate Methods Process and call it.
        """
        if len(args) != 0 and isinstance(args[0], dict): # deprecated, temporary explicit call
            return self.virt_call_method(args[0]['function'], *args[1:], **kwargs)
        locs = get_caller_frame().f_locals
        if 'kwargs' not in locs:
            raise TypeError('Intermediate method must have **kwargs argument.')
        return self.virt_call_method(locs['kwargs']['function'], *args, **kwargs)
    
    # internal function, deprecated to use
    def virt_call_method(self, method: Callable[..., Any], *args, **kwargs) -> Any:
        return method(self, *args, **kwargs)
    
    def delegate(self, *args, **kwargs) -> Any:
        """
        Part of Intermediate Methods architecture.
        
        Delegate received function into
        Intermediate Methods Process and call it.
        """
        if len(args) != 0 and isinstance(args[0], dict): # deprecated, temporary explicit call
            return self.call_method(args[0]['function'], *args[1:], **kwargs)
        locs = get_caller_frame().f_locals
        if 'kwargs' not in locs:
            raise TypeError('Intermediate method must have **kwargs argument.')
        return self.call_method(locs['kwargs']['function'], *args, **kwargs)
    
    # internal function, deprecated to use
    def call_method(self, method: Callable[..., Any], *args, **kwargs) -> Any:
        return method(byref(self), *args, **kwargs)
    
    def ref(self) -> IPointer['CStructure']:
        """
        Alias to byref(instance).
        """
        return byref(self)
    
    def ptr(self) -> IPointer['CStructure']:
        """
        Alias to pointer(instance).
        """
        return pointer(self)
    
    @classmethod
    def has_field(cls, field_name: str) -> bool:
        """
        Check the structure _fields_ has the field.
        """
        to_check_classes: List[Type[CStructure]] = [cls]
        cls._recursive_check_classes(cls, to_check_classes)
        
        for to_check_class in to_check_classes:
            for field in to_check_class._fields_:
                if field[0] == field_name: return True
            
        return False
    
    @classmethod
    def _recursive_check_classes(cls, cls_cs: Type['CStructure'], 
                                 to_check_classes: list[Type['CStructure']]):
        if not hasattr(cls_cs, '_anonymous_'): return
        for anonymous_field in cls_cs._anonymous_:
            typ = cls_cs._field_type_lightweight(anonymous_field)
            to_check_classes.append(typ)
            cls._recursive_check_classes(typ, to_check_classes)
    
    @classmethod
    def _field_type_lightweight(cls, field_name: str) -> Optional[type]:
        for field in cls._fields_:
            if field[0] == field_name: return field[1]
        return None
    
    @classmethod
    def field_type(cls, field_name: str) -> Optional[type]:
        """
        Get the type of field.
        """
        to_check_classes: List[Type[CStructure]] = [cls]
        cls._recursive_check_classes(cls, to_check_classes)
        
        for to_check_class in to_check_classes:
            for field in to_check_class._fields_:
                if field[0] == field_name: return field[1]
            
        return None
    
    @classmethod
    def offset(cls, field: str) -> int:
        """
        Get the offset of field.
        """
        return getattr(cls, field).offset
    
    @classmethod
    def inter_process(cls, process, remote_address: WT_ADDRLIKE) -> Self:
        """
        Create the inter-process version of the structure.
        """
        
        if TYPE_CHECKING: from .defbase_process import CStructureInterProcess
        inter_process_cls: type[CStructureInterProcess] = getattr(cls, '_inter_process_version', None)
        
        if inter_process_cls is not None:
            return inter_process_cls.initialize(process, remote_address)
        
        defbase_process = getattr(_defb_state, '_defbase_process', None)
        if defbase_process is None:
            from . import defbase_process
            _defb_state._defbase_process = defbase_process
        
        inter_process_cls: type[CStructureInterProcess]
        inter_process_cls = type(f'{cls.__name__}InterProcess', 
                                 (cls, defbase_process.CStructureInterProcess), {})
        cls._inter_process_version = inter_process_cls
        
        return inter_process_cls.initialize(process, remote_address)
    
    @classmethod
    def from_structure(cls, cls_structure: Type[WT]) -> Type[WT]:
        """
        Create the better CStructure from poor ctypes.Structure.
        """
        return type(f'C{cls_structure.__name__}', (cls, cls_structure), {})
    
    @staticmethod
    def make(cls: Type[WT]) -> Type[WT]:
        """
        Make the CStructure fields from field type annotations.
        """
        return _make_internal(cls)

def _resolve_genericalias(generic_alias: IGenericAlias) -> type:
    origin = generic_alias.__origin__
    
    if origin is IPointer:
        return _ipointer_to_pointer(generic_alias)
    elif issubclass(origin, IAliasableGeneric):
        return generic_alias.__args__[0]
    elif issubclass(origin, IWideCharArrayFixedSize):
        size, = generic_alias.__args__
        return c_wchar * size
    elif issubclass(origin, ICharArrayFixedSize):
        size, = generic_alias.__args__
        return c_char * size
    elif issubclass(origin, IArrayFixedSize):
        typ, size = generic_alias.__args__
        if isinstance(typ, GenericAlias): 
            return _resolve_genericalias(typ) * size
        return _resolve_type(typ) * size
    elif issubclass(origin, IAliasableGenericWithPayload):
        return origin._get_alias_(generic_alias=generic_alias)

from ctypes import (py_object, c_short, c_ushort, 
                    c_long, c_ulong, c_uint, c_float, 
                    c_double, c_longdouble, c_longlong,
                    c_ulonglong, c_ubyte, c_byte, c_char,
                    c_bool, c_wchar_p, c_wchar, c_char_p)

# Typing interfaces to describe LPSTR/LPWSTR in-python type representations.
WT_LPSTR: TypeAlias = TUnion[bytes, c_char_p, c_wchar]
WT_LPWSTR: TypeAlias = TUnion[str, c_wchar_p, c_wchar]

class IAliasable(IInterface): 
    """
    Describes the typing alias to `_alias_` ctypes type.
    """
    _alias_: ClassVar[type]
    
class ICustomizable(IInterface):
    """
    Describes the in-python customizable typing alias by `_custom_` attribute.
    """
    _custom_: ClassVar[type]
    
class IAliasableGeneric(IInterface, Generic[WT]): 
    """
    Describes the typing alias to ctypes type, 
    which passed in arguments to interface type.
    """

class IAliasableGenericWithPayload(IInterface, Generic[WT]):
    """
    Describes the typing alias to ctypes type,
    which received from `_get_alias_` function.
    """
    
    @interface_abstract_method
    @classmethod
    def _get_alias_(cls, **kwargs) -> type: 
        """
        Payload to make implementation to provide the ctypes type.
        """
    
    @staticmethod
    def get_genericalias() -> IGenericAlias:
        """
        Get the generic alias which passed to caller function.
        """
        return get_caller_frame().f_locals['kwargs']['generic_alias']
    
class IInteger(IAliasableGeneric[WT], int): 
    """
    Typing alias to any C integer type.
    """

class IPack(Generic[WT], IInterface): 
    """
    Pack of the structure.
    """
    
class IChar(IAliasable, bytes): 
    """
    Typing alias to `c_char`.
    """
    _alias_ = c_char
    
class ICharArray(IArray[IChar]):
    """
    Type-safe interface over
    ctypes characters array.
    """
    
    value: bytes
    raw: bytes
    
class IWideCharArray(IArray[IChar]):
    """
    Type-safe interface over
    ctypes wide characters array.
    """
    
    value: str
    
class ICharArrayFixedSize(IArrayFixedSize[IChar, WT2]):
    """
    Type-safe interface over
    ctypes characters array.
    """
    
    value: bytes
    raw: bytes
    
class IWideCharArrayFixedSize(IArrayFixedSize[IChar, WT2]):
    """
    Type-safe interface over
    ctypes wide characters array.
    """
    
    value: str

class IWideChar(IAliasable, str):
    """
    Typing alias to `c_wchar`.
    """
    
    _alias_ = c_wchar
    
class IShort(IAliasable, int):
    """
    Typing alias to `c_short`.
    """
    
    _alias_ = c_short
    
class IUnsignedShort(IAliasable, int): 
    """
    Typing alias to `c_ushort`.
    """
    
    _alias_ = c_ushort
    
class IInt(IAliasable, int):
    """
    Typing alias to `c_int`.
    """
    
    _alias_ = c_int
    
class IUnsignedInt(IAliasable, int):
    """
    Typing alias to `c_uint`.
    """
    
    _alias_ = c_uint
    
class ILong(IAliasable, int): 
    """
    Typing alias to `c_long`.
    """
    
    _alias_ = c_long
    
class IUnsignedLong(IAliasable, int):
    """
    Typing alias to `c_ulong`.
    """
    
    _alias_ = c_ulong
    
IUlong = IULong = IUnsignedLong
IUshort = IUShort = IUnsignedShort
IUint = IUInt = IUnsignedInt

warnings.filterwarnings("ignore", category=SyntaxWarning)

class IAnonymous(Generic[WT], IInterface): 
    """
    Describes the anonymous field in the structure/union.
    """
    
from ctypes import (c_int64, c_uint64, 
                    c_size_t, c_ssize_t,
                    c_int32, c_uint32,
                    c_int16, c_uint16,
                    c_int8, c_uint8)
    
class IInt64(IAliasable, int): 
    """
    Typing alias to `c_int64`.
    """
    
    _alias_ = c_int64
    
class IUnsignedInt64(IAliasable, int): 
    """
    Typing alias to `c_uint64`.
    """
    
    _alias_ = c_uint64

class IInt32(IAliasable, int):
    """
    Typing alias to `c_int32`.
    """
    
    _alias_ = c_int32
    
class IUnsignedInt32(IAliasable, int):
    """
    Typing alias to `c_uint32`.
    """
    
    _alias_ = c_uint32

class IInt16(IAliasable, int):
    """
    Typing alias to `c_int16`.
    """
    
    _alias_ = c_int16
    
class IUnsignedInt16(IAliasable, int):
    """
    Typing alias to `c_uint16`.
    """
    
    _alias_ = c_uint16

class IInt8(IAliasable, int):
    """
    Typing alias to `c_int8`.
    """
    
    _alias_ = c_int8
    
class IUnsignedInt8(IAliasable, int):
    """
    Typing alias to `c_uint8`.
    """
    
    _alias_ = c_uint8
    
IByte = IUInt8 = IUint8 = IUnsignedInt8
IWord = IUInt16 = IUint16 = IUnsignedInt16
IDword = IUInt32 = IUint32 = IUnsignedInt32
IQword = IUInt64 = IUint64 = IUnsignedLongLong = IULongLong = IUlonglong = IUnsignedInt64
ILongLong = IInt64

class ISizeT(IAliasable, int): 
    """
    Typing alias to `c_size_t`.
    """
    
    _alias_ = c_size_t

class ISignedSizeT(IAliasable, int): 
    """
    Typing alias to `c_ssize_t`.
    """
    
    _alias_ = c_ssize_t
    
class IFloat(IAliasable, float):
    """
    Typing alias to `c_float`.
    """
    
    _alias_ = c_float
    
class IDouble(IAliasable, float):
    """
    Typing alias to `c_double`.
    """
    
    _alias_ = c_double
    
class IBool(IAliasable, ICustomizable, bool):
    """
    Typing alias to `c_bool` with in-python type `bool`.
    """
    
    _alias_ = c_bool
    _custom_ = bool
    
class IBool64(IBool):
    """
    Typing alias to `BOOL` (`c_ulong`) with in-python type `bool`.
    """
    
    _alias_ = c_ulong

if TYPE_CHECKING:
    IIntPtr = IInt64
    IUnsignedIntPtr = IUIntPtr = IUintPtr = IUInt64
    
    ILongPtr = IInt64
    IUnsignedLongPtr = IULongPtr = IUlongPtr = IUInt64
    IUnsignedHalfPtr = IUHalfPtr = IUhalfPtr = IUInt64
    IDwordPtr = IUInt64
    
if not TYPE_CHECKING:
    if sys.maxsize == 2**63-1:
        IIntPtr = IInt64
        IUnsignedIntPtr = IUIntPtr = IUintPtr = IUInt64
        
        ILongPtr = IInt64
        IUnsignedLongPtr = IULongPtr = IUlongPtr = IUInt64
        IUnsignedHalfPtr = IUHalfPtr = IUhalfPtr = IUInt64
        IDwordPtr = IUInt64
    else:
        IIntPtr = IInt
        IUnsignedPtr = IUIntPtr = IUintPtr = IUInt
        ILongPtr = ILong
        IUnsignedLongPtr = IULongPtr = IUlongPtr = IUlong
        IUnsignedHalfPtr = IUHalfPtr = IUhalfPtr = IUlong
        IDwordPtr = IUInt
        
# Handle-like interfaces
IHandle = IVoidPtr
WT_HANDLE = WT_ADDRLIKE
    
def _resolve_type(typ: type) -> type:
    if typ is IVoidPtr: return c_void_p
    if typ is bytes: return c_char_p
    if typ is str: return c_wchar_p
    if typ is int: return c_int
    if typ is float: return c_float
    
    if issubclass(typ, IAliasable):
        return typ._alias_
    
    return typ

from typing import ForwardRef
    
def _ipointer_to_pointer(ipointer: IGenericAlias):
    typ = ipointer.__args__[0]
    
    if isinstance(typ, GenericAlias):
        generic_alias: IGenericAlias = typ
        origin = generic_alias.__origin__
        
        if origin is IPointer:
            typ = PTR(_ipointer_to_pointer(generic_alias))
        elif issubclass(origin, IAliasableGeneric):
            typ = PTR(generic_alias.__args__[0])
    else:
        if isinstance(typ, (ForwardRef, str)):
            typ = c_void_p
        else:
            typ = _resolve_type(typ)
            typ = PTR(typ)
    
    return typ
    
def declare_fields(cls: Type[CStructure]):
    """
    Declare the fields from `fields` contract 
    into the structure (late fields initialization).
    """
    cls._fields_ = cls.fields
    
def field_typed(cls: Type[CStructure], field: str, field_real: str, result: WT):
    """
    Make the custom in-python field type representation for field.
    """
    def getter(self) -> WT:
        return result(getattr(self, field_real))
    
    getter.__name__ = field
    getter_prop = property(getter)
    
    def setter(self, value: WT):
        setattr(self, field_real, value)
    
    setter.__name__ = field
    setter_prop = getter_prop.setter(setter)
    
    setattr(cls, field, getter_prop)
    setattr(cls, field, setter_prop)
    
class CUnion(Union):
    """
    Enhanced union type builded over
    ctypes.Union class.
    """
    
    @staticmethod
    def make(cls: Type[WT]) -> Type[WT]:
        return _make_internal(cls)
    
    @classmethod
    def _recursive_check_classes(cls, cls_cs: Type['CStructure'], 
                                 to_check_classes: list[Type['CStructure']]):
        if not hasattr(cls_cs, '_anonymous_'): return
        for anonymous_field in cls_cs._anonymous_:
            typ = cls_cs._field_type_lightweight(anonymous_field)
            to_check_classes.append(typ)
            cls._recursive_check_classes(typ, to_check_classes)
    
    @classmethod
    def _field_type_lightweight(cls, field_name: str) -> Optional[type]:
        for field in cls._fields_:
            if field[0] == field_name: return field[1]
        return None
    
    @classmethod
    def has_field(cls, field_name: str) -> bool:
        """
        Check the structure _fields_ has the field.
        """
        to_check_classes: List[Type[CStructure]] = [cls]
        cls._recursive_check_classes(cls, to_check_classes)
        
        for to_check_class in to_check_classes:
            for field in to_check_class._fields_:
                if field[0] == field_name: return True
            
        return False
    
    @classmethod
    def _recursive_check_classes(cls, cls_cs: Type['CStructure'], 
                                 to_check_classes: list[Type['CStructure']]):
        if not hasattr(cls_cs, '_anonymous_'): return
        for anonymous_field in cls_cs._anonymous_:
            typ = cls_cs.field_type(anonymous_field)
            to_check_classes.append(typ)
            cls._recursive_check_classes(typ, to_check_classes)
    
    @classmethod
    def field_type(cls, field_name: str) -> Optional[type]:
        """
        Get the type of field.
        """
        to_check_classes: List[Type[CStructure]] = [cls]
        cls._recursive_check_classes(cls, to_check_classes)
        
        for to_check_class in to_check_classes:
            for field in to_check_class._fields_:
                if field[0] == field_name: return field[1]
            
        return None
    
    @classmethod
    def offset(cls, field: str) -> int:
        """
        Get the offset of field.
        """
        return getattr(cls, field).offset
    
def delegate(*args, **kwargs) -> Any:
    """
    Part of Intermediate Methods architecture.
    
    Delegate received function into
    Intermediate Methods Process and call it.
    """
    if len(args) != 0 and isinstance(args[0], dict): # deprecated, temporary explicit call
        return args[0]['function'](*args[1:], **kwargs)
    locs = get_caller_frame().f_locals
    if 'kwargs' not in locs:
        raise TypeError('Intermediate method must have **kwargs argument.')
    return locs['kwargs']['function'](*args, **kwargs)
    
class CClass(CStructure):
    """
    Class mimics the C++ Class philosophy.
    
    The friend classes set by `_friend_classes` or by `add_friend_class`.
    The protected fields set by `_protected` or by `add_protected`.
    The private fields set by `_private` or by `add_private`.
    
    Other fields are public for anyone.
    """
    _friend_classes: ClassVar[List[str]] = []
    _protected: ClassVar[List[str]] = []
    _private: ClassVar[List[str]] = []
            
    def _check_access(self, name: str):
        is_protected = name in super().__getattribute__('_protected')
        is_private = name in super().__getattribute__('_private')
        
        if is_protected and is_private:
            raise AccessError('Incorrectly declaring access modificators: '
                                f'field "{name}" is protected and private at once.')
        
        if not (is_protected or is_private):
            return # public
        
        caller = get_py_frame(2)
        code = caller.f_code
        
        has_self = 'self' in caller.f_locals
        
        if has_self:
            instance_type: Type[object] = type(caller.f_locals['self'])
            qualname: str = instance_type.__qualname__
            if qualname in super().__getattribute__('_friend_classes'):
                return # friend class access
        
        if is_protected:
            if not has_self:
                raise AccessError(f'The field {name} is protected.')
            
            for cls in instance_type.__mro__:
                if code.co_name in cls.__dict__:
                    return # descendant access
                
            raise AccessError(f'The field {name} is protected.')
        elif is_private:
            _, qual_name = code.co_filename, code.co_qualname
            class_name = '.'.join(qual_name.split('.')[:-1])
            self_name = type(self).__qualname__
            if class_name != self_name: 
                raise AccessError(f'The field {name} is private.') # private access
    
    def __setattr__(self, name: str, value):
        if name in ('_protected', '_private', '_friend_classes'):
            raise AttributeError(f'Member "{name}" is private.')
        
        super().__getattribute__('_check_access')(name)
        super().__setattr__(name, value)
        
    def __getattribute__(self, name: str):
        if name in ('_protected', '_private', '_friend_classes'):
            raise AttributeError(f'Member "{name}" is private.')
        
        super().__getattribute__('_check_access')(name)
        return super().__getattribute__(name)
    
    @classmethod
    def add_protected(cls, field: str): 
        """
        Add the protected field into class.
        """
        protected: List[str] = cls._protected
        if field in protected:
            return
        protected.append(field)
    
    @classmethod
    def add_private(cls, field: str): 
        """
        Add the private field into class.
        """
        private: List[str] = cls._private
        if field in private:
            return
        private.append(field)
    
    @classmethod
    def add_friend_class(cls, friend: Type[object]):
        """
        Add the friend class into class.
        """
        friend_classes: List[str] = cls._friend_classes
        if friend in friend_classes:
            return
        friend_classes.append(friend.__qualname__)
   
from typing import overload
    
def i_cast(obj: Any, typ: IPointer[WT]) -> IPointer[WT]:
    """
    Type-safe interface over
    ctypes cast(...) function.
    
    Recommended to use instead of ctypes cast(...).
    """

if TYPE_CHECKING:
    def i_cast(obj: Any, typ: Type[IPointer[WT]]) -> IPointer[WT]:
        """
        Type-safe interface over
        ctypes cast(...) function.
        
        Recommended to use instead of ctypes cast(...).
        """
        
if not TYPE_CHECKING:
    if _WT_UNSTABLE_API:
        def i_cast(obj: Any, typ: Type[IPointer[WT]]) -> IPointer[WT]:
            cbyref_obj = None
            if isinstance(obj, CByref):
                cbyref_obj = _defbase_ctypinit.PyCArgObject_CAST_DEREF(obj)
                cbyref_obj.ob_type = _defbase_ctypinit.CArgObject
                
            result = cast(obj, typ)
            if cbyref_obj:
                cbyref_obj.ob_type = CByref
            
            return result
    else: # optimize, if CByref is not exists then the i_cast doesn't handle it.
        def i_cast(obj: Any, typ: Type[IPointer[WT]]) -> IPointer[WT]:
            return cast(obj, typ)

# needed to fix the typing, i_cast2 with overloading is breaks the typing interface system
# so i don't know how to add `value` show support into casting system.

# @overload
# def i_cast2(obj: Any, typ: IPointer[WT]) -> IPointer[WT]: ...
    
# @overload
# def i_cast2(obj: Any, typ: Type[IVoidPtr]) -> IVoidPtr: ...
    
def i_cast2(obj: Any, typ: Type[IPointer[WT]]) -> IPointer[WT]:
    """
    Type-safe interface over
    ctypes cast(...) function.
    
    Recommended to use instead of ctypes cast(...).
    Optimized version without CByref checking.
    """
    
    return cast(obj, typ)

class _ICast(IInterface):
    typ: WT
    
    def __init__(self, typ: WT): ...
    
    def __call__(self, obj: WT) -> TUnion[IPointer[WT], WT]: ...

class _CastMeta(type):
    def __new__(mcs, name: str, bases: tuple, dictionary: Dict[str, Any]):
        cls = super().__new__(mcs, name, bases, dictionary)
        
        return cls
    
    def __getitem__(cls, typ) -> _ICast:
        return cls(typ)
        
_ctypes_types = {
    'O': py_object,
    'h': c_short,
    'H': c_ushort,
    'l': c_long,
    'L': c_ulong,
    'i': c_int,
    'I': c_uint,
    'f': c_float,
    'd': c_double,
    'g': c_longdouble,
    'q': c_longlong,
    'Q': c_ulonglong,
    'B': c_ubyte,
    'b': c_byte,
    'c': c_char,
    'P': c_void_p,
    '?': c_bool,
    'Z': c_wchar_p,
    'u': c_wchar,
    'z': c_char_p
}
        
def _is_ptr(ptr_like) -> bool:
    return (hasattr(ptr_like, '_obj') or hasattr(ptr_like, '_type_')) and isinstance(_ptr_to_type(ptr_like), type)
        
def _has_function(obj, func_name) -> bool:
    return hasattr(obj, func_name) and callable(getattr(obj, func_name))
        
def _ptr_to_type(ptr) -> type:
    ptr_type = ptr._obj._type_ if hasattr(ptr, '_obj') else ptr._type_
    if isinstance(ptr_type, str) and ptr_type in _ctypes_types:
        return _ctypes_types[ptr_type]
    return ptr_type
        
def _is_int_like(typ: type) -> bool:
    return typ in (int, c_int, c_short, c_ushort, c_long, c_longlong, c_ulong, c_ulonglong)

def _is_ctypes_type(typ: type) -> bool:
    return typ in _ctypes_types.values()

def _is_float_like(typ: type) -> bool:
    return typ in (float, c_float, c_double, c_longdouble)
        
class reinterpret_cast(metaclass=_CastMeta):
    """
    Converts between types by reinterpreting the underlying bit pattern.
    
    ### Syntax:
    `reinterpret_cast[ target-type ]( expression )`
    """
    
    typ: Type[IPointer[WT]]
    
    def __init__(self, typ: Type[IPointer[WT]]):
        self.typ = typ
        
    def __call__(self, obj: IPointer[WT]) -> IPointer[WT]:
        return i_cast(obj, self.typ)
        
class static_cast(metaclass=_CastMeta):
    """
    Converts between types using a combination of implicit and user-defined conversions.
    
    ### Syntax:
    `static_cast[ target-type ]( expression )`
    """
    typ: type
    
    def __call__(self, obj: WT) -> WT:
        typ: type = type(obj)
        ptr_type: type = None
        if _is_ptr(obj):
            ptr_type: type = _ptr_to_type(obj)
            
        if typ is self.typ:
            return obj
        
        if _has_function(obj, '__static_cast__'):
            static_cast_value = obj.__static_cast__(self.typ)
            if static_cast_value is NotImplemented:
                raise TypeError(f'Cannot static_cast from {typ} to {self.typ}.')
            return static_cast_value
        
        if typ is int and _is_int_like(self.typ):
            if _is_ctypes_type(self.typ):
                return self.typ(obj).value
            return int(obj)
        
        if typ is float and _is_float_like(self.typ):
            if _is_ctypes_type(self.typ):
                return self.typ(obj).value
            return float(obj)
        
        if typ is c_void_p and _is_ptr(self.typ):
            return i_cast(obj, self.typ)
        
        if ptr_type is not None:
            if self.typ is c_void_p:
                return i_cast(obj, c_void_p)
        
            if _is_ptr(self.typ) and issubclass(ptr_type, _ptr_to_type(self.typ)):
                return i_cast(obj, self.typ)
        
        raise TypeError(f'Cannot static_cast from {typ} to {self.typ}.')
    
    def __init__(self, typ: type):
        self.typ = typ
       
class Ref(Generic[WT]):
    """
    Class represents the lightweight reference to object.
    """
    
    value: WT
    
    def __init__(self, value: TUnion[WT, Type[WT]]):
        if isinstance(value, type):
            self.value = value()
            return
        
        self.value = value
        
    def __int__(self) -> int:
        if isinstance(self.value, int):
            return self.value
        raise TypeError('Ref now is not holding int type.')
    
    def __bool__(self) -> bool:
        return bool(self.value)
    
    def __float__(self) -> float:
        if isinstance(self.value, int):
            return self.value
        raise TypeError('Ref now is not holding float type.')
    
    def __str__(self) -> str:
        if isinstance(self.value, str):
            return self.value
        raise TypeError('Ref now is not holding str type.')
       
    def __repr__(self) -> str:
        return repr(self.value)
       
from sys import stdout, stdin, stderr
from io import TextIOBase
       
nullptr = None

class std:
    """
    Standard namespace.
    """
    class unique_ptr(Generic[WT]):
        """
        Stores a pointer to an _owned_ object or array. The object/array is owned by **no other** `unique_ptr`. The object/array is destroyed when the `unique_ptr` is destroyed.
        """
        _ptr: IPointer[WT]
        _owning: bool
        contents: WT
        
        def __init__(self, ptr: IPointer[WT]):
            ptr = i_cast(ptr, POINTER(PtrUtil.get_type(ptr)))
            self._owning = True
            self._ptr = ptr
            
        def __bool__(self):
            return bool(self._ptr)
        
        def _check(self):
            if not self._ptr:
                if self._owning:
                    raise ValueError('NULL pointer access')
                
                raise RuntimeError('This pointer is no more owning the data pointer')
        
        def release(self):
            self._check()
            if self._ptr:
                del self._ptr
                self._ptr = nullptr
            self._owning = False
            
        def reset(self, ptr: IPointer[WT]):
            if self._owning:
                self.release()
            self.__init__(ptr)
        
        @property
        def contents(self):
            self._check()
            
            return self._ptr.contents
        
    @staticmethod
    def make_unique(typ: Type[WT]) -> unique_ptr[WT]:
        """
        Creates and returns a `unique_ptr` to an object of the specified type, which is constructed by using the specified arguments.
        """
        return std.unique_ptr(pointer(typ()))

    @staticmethod
    def move(ptr: unique_ptr[WT]) -> unique_ptr[WT]:
        """
        `std::move` is used to _indicate_ that an object `t` may be "moved from", i.e. allowing the efficient transfer of resources from t to another object.

        In particular, `std::move` produces an xvalue expression that identifies its argument `t`. It is exactly equivalent to a `static_cast` to an rvalue reference type.
        """
        new_ptr: std.unique_ptr[WT] = std.unique_ptr(ptr._ptr)
        ptr._owning = False
        ptr._ptr = nullptr
        return new_ptr
    
    class _St:
        _stream: TextIOBase
        
        def __init__(self, stream: TextIOBase):
            self._stream = stream
    
    class _StOut(_St):
        def __lshift__(self, value: str):
            if not isinstance(value, str):
                value = str(value)
                
            self._stream.write(value)
            return self
            
    class _StIn(_St):
        def _read(self) -> str:
            ended: bool = False
            buffer: str = ''
            while not ended:
                character = self._stream.read(1)
                if character.isspace():
                    ended = True
                    break
                buffer += character
            return buffer
        
        def __rshift__(self, ref: Ref[Any]): 
            if isinstance(ref.value, int):
                ref.value = int(self._read())
            elif isinstance(ref.value, str):
                ref.value = self._read()
            elif isinstance(ref.value, float): 
                ref.value = float(self._read())
            else:
                raise TypeError(f'Unknown ref type: {type(ref).__name__}.')
    
    cout = _StOut(stdout)
    cerr = _StOut(stderr)
    cin = _StIn(stdin)
    
    endl: str = '\n'

c_byte_p = PTR(c_byte)

def flexible_array(cls: Type[Structure], name: str, typ: type):
    """
    Declare the flexible array after the structure with given field name and type.
    """
    def array_property(self):
        pbThis = i_cast(byref(self), c_byte_p)
        pbData = PtrArithmetic.add(pbThis, sizeof(cls))
        return i_cast(pbData, PTR(typ))
        
    array_property.__name__ = name
    setattr(cls, name, property(array_property))
    
array_after_structure = flexible_array

def unicode(wide: WT, ansi: WT) -> WT:
    """
    Wrapper around unicode
    check to define
    Unicode/non Unicode
    functions/types. 
    
    Deprecated but without message. Recommended to use only wide functions and types.
    """
    
    if _CPreprocState._internal_cached_UNICODE: # internal optimization
        return wide
    return ansi

LI = TypeVar('LI', bound=CDLL)

class _DEFB_STATE: # internal global state
    __slots__  = ['_linked_libraries', '_defbase_process', 
                  '_defbase_module', '_interfacedef', '_unknwn']
    _linked_libraries: Dict[str, LI]
    
    def __init__(self):
        self._linked_libraries = {}
    
_defb_state: _DEFB_STATE = _DEFB_STATE()

def link_library(library: str, library_type: Type[LI] = W_CDLL):
    """
    Link library to the foreign libraries collection.
    """
    
    if not isinstance(library_type, type):
        raise ValueError('Library type must be Python type.')
    if not issubclass(library_type, CDLL):
        raise ValueError('Library type must be CDLL descendant.')
    _defb_state._linked_libraries[library] = library_type(library)

def get_library(library: str, library_type: Type[LI] = W_CDLL) -> LI:
    """
    Get library from foreign libraries collection or
    create new library of provided type.
    """
    if not isinstance(library_type, type):
        raise ValueError('Library type must be Python type.')
    if not issubclass(library_type, CDLL):
        raise ValueError('Library type must be CDLL descendant.')
    if library not in _defb_state._linked_libraries:
        link_library(library, library_type)
    return _defb_state._linked_libraries[library]

def get_win_library(library: str) -> W_WinDLL:
    """
    Get library from foreign libraries collection or
    create new library of `W_WinDLL` type.
    """
    
    return get_library(library, W_WinDLL)

from types import ModuleType

def using_namespace(namespace: Type[object]) -> None:
    """
    `using namespace ... `
    analogue in library
    """
    
    global_namespace: Dict[str, Any] = globals()
    for name in dir(namespace):
        if not name.startswith('_'):
            global_namespace[name] = getattr(namespace, name)
            
def module_to_namespace(module: ModuleType, namespace: Type[object]) -> None:
    """
    `namespace { ... }` analogue.
    """
    
    for name in dir(module):
        if not name.startswith('_'):
            setattr(namespace, name, getattr(module, name))

# internal
def _diagnostic(mod_path = '.'):
    import os, traceback, importlib as imp
    
    files = [f for f in os.listdir(mod_path) if os.path.isfile(os.path.join(mod_path, f))]
    if 'winnt.py' not in files:
        raise LookupError('The module is not win module.')
    modules = [mod for mod in files if os.path.splitext(mod)[-1] == '.py']
    for module in modules:
        try:
            imp.import_module('.' + os.path.splitext(module)[0], __package__)
        except Exception:
            traceback.print_exc()