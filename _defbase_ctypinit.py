from ctypes import *

import sys

if sys.implementation.name != 'cpython':
    raise RuntimeError('Only CPython interpreter implementation supported.')

defined_Py_TRACE_REFS = hasattr(sys, 'getobjects')

if sys.version_info[0:2] == (3, 14):
    if not hasattr(sys, '_is_gil_enabled'):
        GIL_ENABLED = True
    else:
        GIL_ENABLED = sys._is_gil_enabled()
    
from typing import (TypeVar, Generic, Optional, 
                    Mapping, Any, Dict,
                    AnyStr, Sequence, Type,
                    Iterable, Callable, List)
import typing, ctypes, types, collections.abc
import traceback

if sys.version_info < (3, 8):
    raise RuntimeError('Versions before 3.8 are not supported.')
if sys.version_info >= (3, 15):
    raise RuntimeError('Versions after 3.14 are not supported.')

_INIT_CHAIN: List[Callable[[], None]] = []
_GLOBAL_REFS: List[Any] = []

mappingproxy = type(type.__dict__)

PY_SINGLE_FUNC = PYFUNCTYPE(c_void_p, c_void_p)
PY_SINGLE_WITH_ERR_FUNC = PYFUNCTYPE(c_int, c_void_p)
PY_BINARY_FUNC = PYFUNCTYPE(c_void_p, c_void_p, c_void_p)
PY_BINARY_WITH_ERR_FUNC = PYFUNCTYPE(c_int, c_void_p, c_void_p)
PY_TERNARY_FUNC = PYFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p)
PY_TERNARY_WITH_ERR_FUNC = PYFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)

class POLYFILL_SpecialForm(typing._Final, _root=True):
    __slots__ = ('_name', '__doc__', '_getitem')
    def __init__(self, getitem):
        self._getitem = getitem
        self._name = getitem.__name__
        self.__doc__ = getitem.__doc__
    def __getattr__(self, item):
        if item in {'__name__', '__qualname__'}:
            return self._name
        raise AttributeError(item)
    def __mro_entries__(self, bases):
        raise TypeError(f"Cannot subclass {self!r}")
    def __repr__(self):
        return f'typing.{self._name}'
    def __reduce__(self):
        return self._name
    def __call__(self, *args, **kwds):
        raise TypeError(f"Cannot instantiate {self!r}")
    def __or__(self, other):
        return typing.Union[self, other]
    def __ror__(self, other):
        return typing.Union[other, self]
    def __instancecheck__(self, obj):
        raise TypeError(f"{self} cannot be used with isinstance()")
    def __subclasscheck__(self, cls):
        raise TypeError(f"{self} cannot be used with issubclass()")
    @typing._tp_cache
    def __getitem__(self, parameters):
        return self._getitem(self, parameters)
if sys.version_info < (3, 13) or typing.TYPE_CHECKING:
    def polyfill_sync_38_39_310_311_312_313():
        _pfill_initchain = []
        def p_init_39spec():
            MProxy_Access(type.__dict__)['__class_getitem__'] = classmethod(lambda cls, item: typing._GenericAlias(cls, item))
        def p_init_310spec():
            @POLYFILL_SpecialForm
            def TypeGuard(self, parameters):
                item = typing._type_check(parameters, f'{self} accepts only a single type.')
                return typing._GenericAlias(self, (item,))
            typing.TypeGuard = TypeGuard
            class _Immutable:
                __slots__ = ()
                def __copy__(self): return self
                def __deepcopy__(self, memo): return self
            class ParamSpecArgs(_Immutable):
                def __init__(self, origin):
                    self.__origin__ = origin
                def __repr__(self):
                    return f"{self.__origin__.__name__}.args"
                def __eq__(self, other):
                    if not isinstance(other, ParamSpecArgs):
                        return NotImplemented
                    return self.__origin__ == other.__origin__
            class ParamSpecKwargs(_Immutable):
                def __init__(self, origin):
                    self.__origin__ = origin
                def __repr__(self):
                    return f"{self.__origin__.__name__}.kwargs"
                def __eq__(self, other):
                    if not isinstance(other, ParamSpecKwargs):
                        return NotImplemented
                    return self.__origin__ == other.__origin__
            typing.ParamSpecArgs = ParamSpecArgs
            typing.ParamSpecKwargs = ParamSpecKwargs
            def _set_default(type_param, default):
                type_param.has_default = lambda: default is not typing.NoDefault
                type_param.__default__ = default
            class _DefaultMixin:
                __slots__ = (); __init__ = _set_default
            def _caller(depth=1, default='__main__'):
                try:
                    return sys._getframemodulename(depth + 1) or default
                except AttributeError:
                    pass
                try:
                    return sys._getframe(depth + 1).f_globals.get('__name__', default)
                except (AttributeError, ValueError):
                    pass
                return None
            class ParamSpec(list, _DefaultMixin):
                __class__ = typing.TypeVar
                @property
                def args(self):
                    return ParamSpecArgs(self)
                @property
                def kwargs(self):
                    return ParamSpecKwargs(self)
                def __init__(self, name, *, bound=None, covariant=False, contravariant=False,
                            infer_variance=False, default=typing.NoDefault):
                    list.__init__(self, [self])
                    self.__name__ = name
                    self.__covariant__ = bool(covariant)
                    self.__contravariant__ = bool(contravariant)
                    self.__infer_variance__ = bool(infer_variance)
                    if bound:
                        self.__bound__ = typing._type_check(bound, 'Bound must be a type.')
                    else: self.__bound__ = None
                    _DefaultMixin.__init__(self, default)
                    def_mod = _caller()
                    if def_mod != 'typing_extensions':
                        self.__module__ = def_mod
                def __repr__(self):
                    if self.__infer_variance__:
                        prefix = ''
                    elif self.__covariant__:
                        prefix = '+'
                    elif self.__contravariant__:
                        prefix = '-'
                    else:
                        prefix = '~'
                    return prefix + self.__name__
                def __hash__(self): return object.__hash__(self)
                def __eq__(self, other): return self is other
                def __reduce__(self): return self.__name__
                def __call__(self, *args, **kwargs): pass
            typing.ParamSpec = ParamSpec
            def _type_convert(arg, module=None, *, allow_special_forms=False):
                if arg is None: return type(None)
                if isinstance(arg, str):
                    if sys.version_info <= (3, 9, 6):
                        return typing.ForwardRef(arg)
                    if sys.version_info <= (3, 9, 7):
                        return typing.ForwardRef(arg, module=module)
                    return typing.ForwardRef(arg, module=module, is_class=allow_special_forms)
                return arg
            def _unpack_args(*args):
                newargs = []
                for arg in args:
                    subargs = getattr(arg, '__typing_unpacked_tuple_args__', None)
                    if subargs is not None and (not (subargs and subargs[-1] is ...)):
                        newargs.extend(subargs)
                    else:
                        newargs.append(arg)
                return newargs
            def _is_unpack(obj):
                return typing.get_origin(obj) is typing.Unpack
            class _ConcatenateGenericAlias(typing._ConcatenateGenericAlias, _root=True):
                __module__ = "typing"
                def copy_with(self, params):
                    if isinstance(params[-1], (list, tuple)): return (*params[:-1], *params[-1])
                    if isinstance(params[-1], typing._ConcatenateGenericAlias): params = (*params[:-1], *params[-1].__args__)
                    elif not (params[-1] is ... or isinstance(params[-1], ParamSpec)):
                        raise TypeError("The last parameter to Concatenate should be a "
                                "ParamSpec variable or ellipsis.")
                    return super(typing._ConcatenateGenericAlias, self).copy_with(params)
                def __getitem__(self, args):
                    value = super().__getitem__(args)
                    if isinstance(value, tuple) and any(_is_unpack(t) for t in value):
                        return tuple(_unpack_args(*(n for n in value)))
                    return value
            typing._ConcatenateGenericAlias = _ConcatenateGenericAlias
            @typing._tp_cache
            def _concatenate_getitem(self, parameters):
                if parameters == (): raise TypeError("Cannot take a Concatenate of no types.")
                if not isinstance(parameters, tuple): parameters = (parameters,)
                if not (parameters[-1] is ... or isinstance(parameters[-1], ParamSpec)):
                    raise TypeError("The last parameter to Concatenate should be a "
                                    "ParamSpec variable or ellipsis.")
                msg = "Concatenate[arg, ...]: each arg must be a type."
                parameters = (*(typing._type_check(p, msg) for p in parameters[:-1]), parameters[-1])
                return _create_concatenate_alias(self, parameters)
            class _EllipsisDummy: ...
            def _create_concatenate_alias(origin, parameters):
                if parameters[-1] is ... and sys.version_info < (3, 9, 2):
                    parameters = (*parameters[:-1], _EllipsisDummy)
                if sys.version_info >= (3, 10, 3):
                    concatenate = typing._ConcatenateGenericAlias(origin, parameters, _typevar_types=(TypeVar, ParamSpec), 
                                                                  _paramspec_tvars=True)
                else:
                    concatenate = typing._ConcatenateGenericAlias(origin, parameters)
                if parameters[-1] is not _EllipsisDummy: return concatenate
                concatenate.__args__ = tuple(p if p is not _EllipsisDummy else ... for p in concatenate.__args__)
                if sys.version_info < (3, 10): return concatenate
                concatenate.__parameters__ = tuple(p for p in concatenate.__parameters__
                                                    if p is not _EllipsisDummy)
                return concatenate
            def get_origin(tp):
                if isinstance(tp, typing._AnnotatedAlias): return typing.Annotated
                if isinstance(tp, (typing._BaseGenericAlias, types.GenericAlias,
                                ParamSpecArgs, ParamSpecKwargs)):
                    return tp.__origin__
                if tp is typing.Generic: return typing.Generic
                return None
            typing.get_origin = get_origin
            def get_args(tp):
                if isinstance(tp, typing._AnnotatedAlias): return (tp.__origin__, *tp.__metadata__)
                if isinstance(tp, (typing._GenericAlias, types.GenericAlias)):
                    res = tp.__args__
                    if get_origin(tp) is collections.abc.Callable and res[0] is not Ellipsis:
                        res = (list(res[:-1]), res[-1])
                    return res
                return ()
            typing.get_args = get_args
            @POLYFILL_SpecialForm
            def Concatenate(self, parameters):
                return _concatenate_getitem(self, parameters)
            typing.Concatenate = Concatenate
            @POLYFILL_SpecialForm
            def TypeAlias(self, parameters):
                raise TypeError(f"{self} is not subscriptable")
            typing.TypeAlias = TypeAlias
            def _bit_count(self):
                return bin(self).count("1")
            tp_int = PyType_CAST_DEREF(int)
            tp_int.immutable = False
            MProxy_Access(int.__dict__)['bit_count'] = _bit_count
            int.bit_count = _bit_count
        def p_init_311spec():
            def _unpack_args(*args):
                newargs = []
                for arg in args:
                    subargs = getattr(arg, '__typing_unpacked_tuple_args__', None)
                    if subargs is not None and (not (subargs and subargs[-1] is ...)):
                        newargs.extend(subargs)
                    else:
                        newargs.append(arg)
                return newargs
            def _is_unpack(obj):
                return typing.get_origin(obj) is typing.Unpack
            class _ConcatenateGenericAlias(typing._ConcatenateGenericAlias, _root=True):
                __module__ = "typing"
                def copy_with(self, params):
                    if isinstance(params[-1], (list, tuple)):
                        return (*params[:-1], *params[-1])
                    if isinstance(params[-1], typing._ConcatenateGenericAlias):
                        params = (*params[:-1], *params[-1].__args__)
                    elif not (params[-1] is ... or isinstance(params[-1], typing.ParamSpec)):
                        raise TypeError("The last parameter to Concatenate should be a "
                                "ParamSpec variable or ellipsis.")
                    return super(typing._ConcatenateGenericAlias, self).copy_with(params)
                def __getitem__(self, args):
                    value = super().__getitem__(args)
                    if isinstance(value, tuple) and any(_is_unpack(t) for t in value):
                        return tuple(_unpack_args(*(n for n in value)))
                    return value
            typing._ConcatenateGenericAlias = _ConcatenateGenericAlias
            @POLYFILL_SpecialForm
            def Self(self, parameters):
                raise TypeError(f"{self} is not subscriptable")
            typing.Self = Self
            @typing._SpecialForm
            def Never(self, params):
                raise TypeError(f"{self} is not subscriptable")
            typing.Never = Never
            @POLYFILL_SpecialForm
            def Required(self, parameters):
                item = typing._type_check(parameters, f'{self._name} accepts only a single type.')
                return typing._GenericAlias(self, (item,))
            typing.Required = Required
            @POLYFILL_SpecialForm
            def NotRequired(self, parameters):
                item = typing._type_check(parameters, f'{self._name} accepts only a single type.')
                return typing._GenericAlias(self, (item,))
            typing.NotRequired = NotRequired
            def assert_never(arg: Never) -> Never:
                value = repr(arg)
                if len(value) > 100:
                    value = value[:100] + '...'
                raise AssertionError(f"Expected code to be unreachable, but got: {value}")
            typing.assert_never = assert_never
            def dataclass_transform(
                *,
                eq_default: bool = True,
                order_default: bool = False,
                kw_only_default: bool = False,
                frozen_default: bool = False,
                field_specifiers: typing.Tuple[
                    typing.Union[typing.Type[typing.Any], typing.Callable[..., typing.Any]],
                    ...
                ] = (),
                **kwargs: typing.Any,
            ) -> typing.Callable[[T], T]:
                def decorator(cls_or_fn):
                    cls_or_fn.__dataclass_transform__ = {
                        "eq_default": eq_default,
                        "order_default": order_default,
                        "kw_only_default": kw_only_default,
                        "frozen_default": frozen_default,
                        "field_specifiers": field_specifiers,
                        "kwargs": kwargs,
                    }
                    return cls_or_fn
                return decorator
            typing.dataclass_transform = dataclass_transform
            def reveal_type(obj):
                print(f"Runtime type is {type(obj).__name__!r}", file=sys.stderr)
                return obj
            typing.reveal_type = reveal_type
        def p_init_312spec():
            class _UnpackSpecialForm(typing._SpecialForm, _root=True):
                def __init__(self, getitem):
                    super().__init__(getitem)
            class _UnpackAlias(typing._GenericAlias, _root=True):
                if sys.version_info < (3, 11):
                    __class__ = typing.TypeVar
                @property
                def __typing_unpacked_tuple_args__(self):
                    assert self.__origin__ is Unpack
                    assert len(self.__args__) == 1
                    arg, = self.__args__
                    if isinstance(arg, typing._GenericAlias):
                        if arg.__origin__ is not tuple:
                            raise TypeError("Unpack[...] must be used with a tuple type")
                        return arg.__args__
                    return None
                @property
                def __typing_is_unpacked_typevartuple__(self):
                    assert self.__origin__ is Unpack
                    assert len(self.__args__) == 1
                    return isinstance(self.__args__[0], typing.TypeVarTuple)
                def __getitem__(self, args):
                    if self.__typing_is_unpacked_typevartuple__:
                        return args
                    return super().__getitem__(args)
            @_UnpackSpecialForm
            def Unpack(self, parameters):
                item = typing._type_check(parameters, f'{self._name} accepts only a single type.')
                return _UnpackAlias(self, (item,))
            _F = typing.TypeVar("_F", bound=typing.Callable[..., typing.Any])
            def override(arg: _F) -> _F:
                try:
                    arg.__override__ = True
                except (AttributeError, TypeError):
                    pass
                return arg
            typing.override = override
            ctypes.c_time_t = c_int32 if sizeof(c_void_p) == 4 else c_int64
        def p_init_313spec():
            class SingletonMeta(type):
                def __setattr__(cls, attr, value):
                    raise TypeError(f"cannot set {attr!r} attribute of immutable type {cls.__name__!r}")
            class NoDefaultType(metaclass=SingletonMeta):
                __slots__ = ()
                def __new__(cls):
                    return globals().get("NoDefault") or object.__new__(cls)
                def __repr__(self): return "typing.NoDefault"
                def __reduce__(self): return "NoDefault"
            NoDefault = NoDefaultType()
            typing.NoDefault = NoDefault
            @POLYFILL_SpecialForm
            def ReadOnly(self, parameters):
                item = typing._type_check(parameters, f'{self._name} accepts only a single type.')
                return typing._GenericAlias(self, (item,))
            def is_protocol(tp: type, /) -> bool:
                return (
                    isinstance(tp, type)
                    and getattr(tp, '_is_protocol', False)
                    and tp is not typing.Protocol
                )
            typing.is_protocol = is_protocol
            def _get_protocol_attrs(cls):
                attrs = set()
                for base in cls.__mro__[:-1]:
                    if base.__name__ in {'Protocol', 'Generic'}:
                        continue
                    annotations = getattr(base, '__annotations__', {})
                    for attr in (*base.__dict__, *annotations):
                        if (not attr.startswith('_abc_') and attr not in _EXCLUDED_ATTRS):
                            attrs.add(attr)
                return attrs
            def get_protocol_members(tp: type, /) -> typing.FrozenSet[str]:
                if not is_protocol(tp):
                    raise TypeError(f'{tp!r} is not a Protocol')
                if hasattr(tp, '__protocol_attrs__'):
                    return frozenset(tp.__protocol_attrs__)
                return frozenset(_get_protocol_attrs(tp))
            typing.get_protocol_members = get_protocol_members
            @POLYFILL_SpecialForm
            def TypeIs(self, parameters):
                item = typing._type_check(parameters, f'{self} accepts only a single type.')
                return typing._GenericAlias(self, (item,))
            typing.TypeIs = TypeIs
        if sys.version_info >= (3, 8) or typing.TYPE_CHECKING:
            if sys.version_info >= (3, 9) or typing.TYPE_CHECKING:
                if sys.version_info >= (3, 10):
                    if sys.version_info >= (3, 11):
                        if sys.version_info >= (3, 12):
                            if sys.version_info >= (3, 13):
                                pass
                            else:
                                _pfill_initchain.append(p_init_313spec)
                        else:
                            _pfill_initchain.append(p_init_312spec)
                            _pfill_initchain.append(p_init_313spec)
                    else:
                        _pfill_initchain.append(p_init_311spec)
                        _pfill_initchain.append(p_init_312spec)
                        _pfill_initchain.append(p_init_313spec)
                else:
                    _pfill_initchain.append(p_init_310spec)
                    _pfill_initchain.append(p_init_311spec)
                    _pfill_initchain.append(p_init_312spec)
                    _pfill_initchain.append(p_init_313spec)
            else:
                _pfill_initchain.append(p_init_39spec)
                _pfill_initchain.append(p_init_310spec)
                _pfill_initchain.append(p_init_311spec)
                _pfill_initchain.append(p_init_312spec)
                _pfill_initchain.append(p_init_313spec)
        for init_cb in _pfill_initchain:
            init_cb()
    _INIT_CHAIN.append(polyfill_sync_38_39_310_311_312_313)
if sys.version_info[0:2] == (3, 8) or sys.version_info[0:2] == (3, 9) or typing.TYPE_CHECKING:
    def polyfill_310plus_to_38_39():
        tp_type = PyType_CAST_DEREF(type)
        def polyfill_type_or(a, b):
            self = cast(a, py_object).value
            item = cast(b, py_object).value
            union = typing.Union[self, item]
            Py_INCREF(union)
            return id(union)
        pfn_polyfill_type_or = PY_BINARY_FUNC(polyfill_type_or)
        _GLOBAL_REFS.append(pfn_polyfill_type_or)
        if not tp_type.tp_as_number:
            tp_type.tp_as_number = cast(PyObject_Malloc(36*sizeof(c_void_p)), POINTER(c_void_p))
            memset(tp_type.tp_as_number, 0, 36*sizeof(c_void_p))
        tp_type.tp_as_number[15] = cast(pfn_polyfill_type_or, c_void_p).value
        tp_none = PyType_CAST_DEREF(type(None))
        if not tp_none.tp_as_number:
            tp_none.tp_as_number = cast(PyObject_Malloc(36*sizeof(c_void_p)), POINTER(c_void_p))
            memset(tp_none.tp_as_number, 0, 36*sizeof(c_void_p))
        tp_none.tp_as_number[15] = cast(pfn_polyfill_type_or, c_void_p).value
        tp_specialform = PyType_CAST_DEREF(typing._SpecialForm)
        if not tp_specialform.tp_as_number:
            tp_specialform.tp_as_number = cast(PyObject_Malloc(36*sizeof(c_void_p)), POINTER(c_void_p))
            memset(tp_specialform.tp_as_number, 0, 36*sizeof(c_void_p))
        tp_specialform.tp_as_number[15] = cast(pfn_polyfill_type_or, c_void_p).value
        tp_genericalias = PyType_CAST_DEREF(typing._GenericAlias)
        if not tp_genericalias.tp_as_number:
            tp_genericalias.tp_as_number = cast(PyObject_Malloc(36*sizeof(c_void_p)), POINTER(c_void_p))
            memset(tp_genericalias.tp_as_number, 0, 36*sizeof(c_void_p))
        tp_genericalias.tp_as_number[15] = cast(pfn_polyfill_type_or, c_void_p).value
        tp_pycstructtype = PyType_CAST_DEREF(type(Structure))
        if not tp_pycstructtype.tp_as_number:
            tp_pycstructtype.tp_as_number = cast(PyObject_Malloc(36*sizeof(c_void_p)), POINTER(c_void_p))
            memset(tp_pycstructtype.tp_as_number, 0, 36*sizeof(c_void_p))
        tp_pycstructtype.tp_as_number[15] = cast(pfn_polyfill_type_or, c_void_p).value
        tp_type.Reload()
        type_check = typing._type_check
        def polyfill_typing_type_check(arg, msg, is_argument=True):
            try:
                result = type_check(arg, msg, is_argument)
            except TypeError:
                if not callable(arg):
                    return arg
                raise
            return result
        typing._type_check = polyfill_typing_type_check
    _INIT_CHAIN.append(polyfill_310plus_to_38_39)

_CWT = TypeVar('_WT')

class IArray(Generic[_CWT]):
    def __getitem__(self, index: int) -> _CWT: ...
    
    def __setitem__(self, index: int, value: _CWT) -> _CWT: ...

class IPointer(IArray[_CWT]):   
    contents: _CWT

if sys.version_info >= (3, 8) and sys.version_info < (3, 12) or typing.TYPE_CHECKING:
    class PyObject(Structure, Generic[_CWT]):
        fields_extra = []
        if defined_Py_TRACE_REFS:
            fields_extra = [
                ('unusedPtr', c_void_p),
                ('unusedPtr2', c_void_p)
            ]
        _fields_ = fields_extra + [
            ('unusedSizeT', c_ssize_t),
            ('_ob_type', c_void_p)
        ]
        
        @property
        def ob_type(self) -> IPointer['PyTypeObject']:
            return cast(self._ob_type, PyTypeObject_PTR)   
        
        @ob_type.setter
        def ob_type(self, ob_type: type):
            self._ob_type = id(ob_type)     
    
        def __repr__(self) -> str:
            return repr(cast(byref(self), py_object).value)
        
        @property
        def object(self) -> _CWT: 
            return cast(byref(self), py_object).value
        
        @classmethod
        def offset(cls, field: str) -> int:
            return getattr(cls, field).offset
        
        @property
        def refcnt(self) -> int:
            return self.unusedSizeT
        
        @refcnt.setter
        def refcnt(self, refcnt: int):
            self.unusedSizeT = refcnt
        
    class PyVarObject(PyObject[_CWT]):
        _fields_ = [
            ('unusedSizeT', c_ssize_t)
        ]
elif sys.version_info >= (3, 12) and sys.version_info < (3, 15) or typing.TYPE_CHECKING:
    if sys.version_info[0:2] != (3, 14):
        class PyObject(Structure, Generic[_CWT]):
            fields_extra = []
            if defined_Py_TRACE_REFS:
                fields_extra = [
                    ('unusedPtr', c_void_p),
                    ('unusedPtr2', c_void_p)
                ]
            _fields_ = fields_extra + [
                ('unusedInt64', c_ssize_t),
                ('_ob_type', c_void_p)
            ]
            
            @property
            def ob_type(self) -> IPointer['PyTypeObject']:
                return cast(self._ob_type, PyTypeObject_PTR) 
            
            @ob_type.setter
            def ob_type(self, ob_type: type):
                self._ob_type = id(ob_type) 
        
            def __repr__(self) -> str:
                return repr(self.object)
            
            @property
            def object(self) -> _CWT: 
                return cast(byref(self), py_object).value
            
            @classmethod
            def offset(cls, field: str) -> int:
                return getattr(cls, field).offset
            
            @property
            def refcnt(self) -> int:
                return self.unusedInt64
            
            @refcnt.setter
            def refcnt(self, refcnt: int):
                self.unusedInt64 = refcnt
    else:
        if GIL_ENABLED:
            class PyObject(Structure, Generic[_CWT]):
                class _Refcnt(Union):
                    _fields_ = [
                        ('ob_flags', c_uint16),
                        ('ob_overflow', c_uint16),
                        ('ob_refcnt', c_uint32)
                    ]
                _fields_ = [
                    ('ob_refcnt', _Refcnt),
                    ('_ob_type', c_void_p)
                ]
                
                @property
                def ob_type(self) -> IPointer['PyTypeObject']:
                    return cast(self._ob_type, PyTypeObject_PTR) 
                
                @ob_type.setter
                def ob_type(self, ob_type: type):
                    self._ob_type = id(ob_type) 
            
                def __repr__(self) -> str:
                    return repr(self.object)
                
                @property
                def object(self) -> _CWT: 
                    return cast(byref(self), py_object).value
                
                @classmethod
                def offset(cls, field: str) -> int:
                    return getattr(cls, field).offset
                
                @property
                def refcnt(self) -> int:
                    return self.unusedInt64
                
                @refcnt.setter
                def refcnt(self, refcnt: int):
                    self.unusedInt64 = refcnt
        else:
            class PyObject(Structure, Generic[_CWT]):
                _fields_ = [
                    ('ob_tid', c_int64),
                    ('ob_flags', c_uint16),
                    ('ob_mutex', c_uint8),
                    ('ob_gc_bits', c_uint8),
                    ('ob_ref_local', c_uint32),
                    ('ob_ref_shared', c_ssize_t),
                    ('_ob_type', c_void_p)
                ]
                
                @property
                def ob_type(self) -> IPointer['PyTypeObject']:
                    return cast(self._ob_type, PyTypeObject_PTR) 
                
                @ob_type.setter
                def ob_type(self, ob_type: type):
                    self._ob_type = id(ob_type) 
            
                def __repr__(self) -> str:
                    return repr(self.object)
                
                @property
                def object(self) -> _CWT: 
                    return cast(byref(self), py_object).value
                
                @classmethod
                def offset(cls, field: str) -> int:
                    return getattr(cls, field).offset
                
                @property
                def refcnt(self) -> int:
                    return self.ob_ref_local
                
                @refcnt.setter
                def refcnt(self, refcnt: int):
                    self.ob_ref_local = refcnt
            
    class PyVarObject(PyObject[_CWT]):
        _fields_ = [
            ('unusedSizeT', c_ssize_t)
        ]
        
PyObject_PTR = POINTER(PyObject)
    
def _wrap_flag(typ: type, name: str, flag: int, method_suffix: str = 'Flag'):
    has_flag = f'Has{method_suffix}'
    set_flag = f'Set{method_suffix}'
    remove_flag = f'Remove{method_suffix}'
    
    def getter(self) -> bool:
        return getattr(self, has_flag)(flag)
    
    getter.__name__ = name
    getter_prop = property(getter)
    
    def setter(self, value: bool):
        if value:
            getattr(self, set_flag)(flag)
        else:
            getattr(self, remove_flag)(flag)
            
    setter.__name__ = name
    setter_prop = getter_prop.setter(setter)
    
    setattr(typ, name, getter_prop)
    setattr(typ, name, setter_prop)
    
class PyMemberDef(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('type', c_int),
        ('offset', c_ssize_t),
        ('flags', c_int),
        ('unusedPtr', c_void_p)
    ]
    
    name: bytes
    flags: int
    
    def SetFlag(self, flag: int):
        if self.flags & flag: return
        self.flags |= flag
        
    def RemoveFlag(self, flag: int):
        if not self.flags & flag: return
        self.flags &= (~flag)
    
    def HasFlag(self, flag: int) -> bool:
        return (self.flags & flag) != 0
    
    def EnumFlags(self) -> Sequence[str]:
        result: List[str] = []
        
        if self.HasFlag(Py_READONLY):
            result.append('Py_READONLY')
        if self.HasFlag(Py_AUDIT_READ):
            result.append('Py_AUDIT_READ')
        if self.HasFlag(_Py_WRITE_RESTRICTED):
            result.append('_Py_WRITE_RESTRICTED')
        if self.HasFlag(Py_RELATIVE_OFFSET):
            result.append('Py_RELATIVE_OFFSET')
        
        return tuple(result)
    
    def __repr__(self) -> str:
        repr_string: str = f"<member '{self.name.decode()}'"
        if self.HasFlag(Py_READONLY):
            repr_string += ', read-only'
        repr_string += '>'
        return repr_string
    
    is_relative_offset: bool
    _write_restricted: bool
    audit_read: bool
    readonly: bool
    
    def __init__(self, name: AnyStr=None, 
                 type: int=0, offset: int=0, 
                 flags: int=0, doc: AnyStr=None):
        if isinstance(name, str): name = name.encode()
        if isinstance(doc, str): doc = doc.encode()
        super().__init__(name, type, offset, flags, doc)
    
    @classmethod
    def array(self, members: Iterable['PyMemberDef']) -> IArray['PyMemberDef']: 
        if not isinstance(members, list): members = list(members)
        members.append(PyMemberDef())
        members_array = (PyMemberDef * len(members))(*members)
        PyObject_CAST_DEREF(members_array).refcnt = 0xffffffff
        return members_array
    
PyMemberDef_PTR = POINTER(PyMemberDef)

PY_GETTER = PYFUNCTYPE(c_void_p, c_void_p, c_void_p)
PY_SETTER = PYFUNCTYPE(c_int, c_void_p, c_void_p, c_void_p)

class PyGetSetDef(Structure):
    _fields_ = [
        ('name', c_char_p),
        ('getter', c_void_p),
        ('setter', c_void_p),
        ('doc', c_char_p),
        ('closure', c_void_p)
    ]
    name: bytes
    getter: int
    setter: int
    doc: bytes
    closure: int
    
PyGetSetDef_PTR = POINTER(PyGetSetDef)

# Types
Py_T_SHORT     = 0
Py_T_INT       = 1
Py_T_LONG      = 2
Py_T_FLOAT     = 3
Py_T_DOUBLE    = 4
Py_T_STRING    = 5
_Py_T_OBJECT   = 6  # Deprecated, use Py_T_OBJECT_EX instead
# the ordering here is weird for binary compatibility
Py_T_CHAR      = 7   # 1-character string
Py_T_BYTE      = 8   # 8-bit signed int
# unsigned variants:
Py_T_UBYTE     = 9
Py_T_USHORT    = 10
Py_T_UINT      = 11
Py_T_ULONG     = 12

# Added by Jack: strings contained in the structure
Py_T_STRING_INPLACE    = 13

# Added by Lillo: bools contained in the structure (assumed char)
Py_T_BOOL      = 14

Py_T_OBJECT_EX = 16
Py_T_LONGLONG  = 17
Py_T_ULONGLONG = 18

Py_T_PYSSIZET  = 19      # Py_ssize_t
_Py_T_NONE     = 20 # Deprecated. Value is always None.

Py_READONLY            = 1
Py_AUDIT_READ          = 2 # Added in 3.10, harmless no-op before that
_Py_WRITE_RESTRICTED   = 4 # Deprecated, no-op. Do not reuse the value.
Py_RELATIVE_OFFSET     = 8

_wrap_flag(PyMemberDef, 'readonly', Py_READONLY)
_wrap_flag(PyMemberDef, 'audit_read', Py_AUDIT_READ)
_wrap_flag(PyMemberDef, '_write_restricted', _Py_WRITE_RESTRICTED)
_wrap_flag(PyMemberDef, 'is_relative_offset', Py_RELATIVE_OFFSET)

class MProxy(PyObject[_CWT]):
    _fields_ = [
        ('mapping', PyObject_PTR)
    ]
    
    mapping: IPointer[PyObject[_CWT]]
    
PyMappingProxyObject_PTR = POINTER(MProxy)

def PyMappingProxyObject_CAST(obj: _CWT) -> MProxy[_CWT]:
    return cast(id(obj), PyMappingProxyObject_PTR)
        
_Py_TPFLAGS_STATIC_BUILTIN = (1 << 1)
Py_TPFLAGS_MANAGED_WEAKREF = (1 << 3)

"""
Placement of dict (and values) pointers are managed by the VM, not by the type.
The VM will automatically set tp_dictoffset.
"""
Py_TPFLAGS_MANAGED_DICT = (1 << 4)

Py_TPFLAGS_PREHEADER = (Py_TPFLAGS_MANAGED_WEAKREF | Py_TPFLAGS_MANAGED_DICT)

# Set if instances of the type object are treated as sequences for pattern matching
Py_TPFLAGS_SEQUENCE = (1 << 5)
# Set if instances of the type object are treated as mappings for pattern matching
Py_TPFLAGS_MAPPING = (1 << 6)

"""
Disallow creating instances of the type: set tp_new to NULL and don't create
the "__new__" key in the type dictionary.
"""
Py_TPFLAGS_DISALLOW_INSTANTIATION = (1 << 7)
Py_TPFLAGS_IMMUTABLETYPE = (1 << 8)
Py_TPFLAGS_HEAPTYPE = (1 << 9)
Py_TPFLAGS_BASETYPE = (1 << 10)
Py_TPFLAGS_HAVE_VECTORCALL = (1 << 11)
Py_TPFLAGS_READY = (1 << 12)
Py_TPFLAGS_READYING = (1 << 13)
Py_TPFLAGS_HAVE_GC = (1 << 14)

# These two bits are preserved for Stackless Python, next after this is 17
Py_TPFLAGS_HAVE_STACKLESS_EXTENSION = (3 << 15)

# Objects behave like an unbound method
Py_TPFLAGS_METHOD_DESCRIPTOR = (1 << 17)

# Object has up-to-date type attribute cache
Py_TPFLAGS_VALID_VERSION_TAG  = (1 << 19)

# Type is abstract and cannot be instantiated
Py_TPFLAGS_IS_ABSTRACT = (1 << 20)

# This undocumented flag gives certain built-ins their unique pattern-matching
# behavior, which allows a single positional subpattern to match against the
# subject itself (rather than a mapped attribute on it):
_Py_TPFLAGS_MATCH_SELF = (1 << 22)

# Items (ob_size*tp_itemsize) are found at the end of an instance's memory
Py_TPFLAGS_ITEMS_AT_END = (1 << 23)

# These flags are used to determine if a type is a subclass.
Py_TPFLAGS_LONG_SUBCLASS        = (1 << 24)
Py_TPFLAGS_LIST_SUBCLASS        = (1 << 25)
Py_TPFLAGS_TUPLE_SUBCLASS       = (1 << 26)
Py_TPFLAGS_BYTES_SUBCLASS       = (1 << 27)
Py_TPFLAGS_UNICODE_SUBCLASS     = (1 << 28)
Py_TPFLAGS_DICT_SUBCLASS        = (1 << 29)
Py_TPFLAGS_BASE_EXC_SUBCLASS    = (1 << 30)
Py_TPFLAGS_TYPE_SUBCLASS        = (1 << 31)

Py_TPFLAGS_DEFAULT  = ( \
                 Py_TPFLAGS_HAVE_STACKLESS_EXTENSION | \
                0)

"""
NOTE: Some of the following flags reuse lower bits (removed as part of the
Python 3.0 transition).
"""

"""
The following flags are kept for compatibility; in previous
versions they indicated presence of newer tp_* fields on the
type struct.
Starting with 3.8, binary compatibility of C extensions across
feature releases of Python is not supported anymore (except when
using the stable ABI, in which all classes are created dynamically,
using the interpreter's memory layout.)
Note that older extensions using the stable ABI set these flags,
so the bits must not be repurposed.
"""
Py_TPFLAGS_HAVE_FINALIZE = (1 << 0)
Py_TPFLAGS_HAVE_VERSION_TAG   = (1 << 18)
        
def _wrap_tpflag(name: str, flag: int):
    _wrap_flag(PyTypeObject, name, flag, method_suffix='TPFLAG')
    
class PyTypeObject(PyVarObject[_CWT]):
    _fields_ = [
        ('tp_name', c_char_p),
        ('tp_basicsize', c_ssize_t),
        ('unusedSizeT', c_ssize_t),
        ('tp_dealloc', c_void_p),
        ('unusedSizeT3', c_ssize_t),
        ('unusedPtrs', c_void_p * 4),
        ('tp_as_number', POINTER(c_void_p)),
        ('tp_as_sequence', POINTER(c_void_p)),
        ('tp_as_mapping', POINTER(c_void_p)),
        ('unusedPtrs2', c_void_p * 6),
        ('tp_flags', c_ulong),
        ('tp_doc', c_char_p),
        ('unusedPtrs3', c_void_p * 3),
        ('unusedSizeT4', c_ssize_t),
        ('tp_iter', c_void_p),
        ('unusedPtrs4', c_void_p * 2),
        ('tp_members', PyMemberDef_PTR),
        ('tp_getset', PyGetSetDef_PTR),
        ('_tp_base', c_void_p),
        ('tp_dict', PyMappingProxyObject_PTR),
        ('unusedPtrs5', c_void_p * 2),
        ('unusedSizeT5', c_ssize_t),
        ('unusedPtrs6', c_void_p * 2),
        ('tp_new', c_void_p)
    ]
    
    @property 
    def tp_base(self) -> IPointer['PyTypeObject']:
        return cast(self._tp_base, PyTypeObject_PTR)
    
    tp_members: IPointer[PyMemberDef]
    tp_dict: IPointer[MProxy[dict]]
    tp_dealloc: c_void_p
    tp_basicsize: int
    tp_flags: int
    tp_as_number: IPointer[c_void_p]
    tp_as_sequence: IPointer[c_void_p]
    tp_as_mapping: IPointer[c_void_p]
    tp_new: int
    tp_getset: IPointer[PyGetSetDef]
    tp_iter: int
    
    @property
    def type(self) -> Type[_CWT]:
        return To_PyType_DEREFERENCED(self)
    
    @property
    def object(self) -> Type[_CWT]:
        return To_PyObject_DEREFERENCED(self)
    
    def SetTPFLAG(self, tp_flag: int):
        if self.tp_flags & tp_flag: return
        self.tp_flags |= tp_flag
        
    def RemoveTPFLAG(self, tp_flag: int):
        if not self.tp_flags & tp_flag: return
        self.tp_flags &= (~tp_flag)
        
    def HasTPFLAG(self, tp_flag: int) -> bool:
        return (self.tp_flags & tp_flag) != 0
    
    def EnumTPFLAGS(self) -> Sequence[str]:
        result: List[str] = []
        
        if self.HasTPFLAG(_Py_TPFLAGS_STATIC_BUILTIN):
            result.append('_Py_TPFLAGS_STATIC_BUILTIN')
            
        if self.HasTPFLAG(Py_TPFLAGS_MANAGED_WEAKREF):
            if self.HasTPFLAG(Py_TPFLAGS_MANAGED_DICT):
                result.append('Py_TPFLAGS_PREHEADER')
            else:
                result.append('Py_TPFLAGS_MANAGED_WEAKREF')
        elif self.HasTPFLAG(Py_TPFLAGS_MANAGED_DICT):
            result.append('Py_TPFLAGS_MANAGED_DICT')
            
        if self.HasTPFLAG(Py_TPFLAGS_SEQUENCE):
            result.append('Py_TPFLAGS_SEQUENCE')
        if self.HasTPFLAG(Py_TPFLAGS_MAPPING):
            result.append('Py_TPFLAGS_MAPPING')
        if self.HasTPFLAG(Py_TPFLAGS_DISALLOW_INSTANTIATION):
            result.append('Py_TPFLAGS_DISALLOW_INSTANTIATION')
        if self.HasTPFLAG(Py_TPFLAGS_IMMUTABLETYPE):
            result.append('Py_TPFLAGS_IMMUTABLETYPE')
        if self.HasTPFLAG(Py_TPFLAGS_HEAPTYPE):
            result.append('Py_TPFLAGS_HEAPTYPE')
        if self.HasTPFLAG(Py_TPFLAGS_BASETYPE):
            result.append('Py_TPFLAGS_BASETYPE')
        if self.HasTPFLAG(Py_TPFLAGS_HAVE_VECTORCALL):
            result.append('Py_TPFLAGS_HAVE_VECTORCALL')
        if self.HasTPFLAG(Py_TPFLAGS_READY):
            result.append('Py_TPFLAGS_READY')
        if self.HasTPFLAG(Py_TPFLAGS_READYING):
            result.append('Py_TPFLAGS_READYING')
        if self.HasTPFLAG(Py_TPFLAGS_HAVE_GC):
            result.append('Py_TPFLAGS_HAVE_GC')
        if self.HasTPFLAG(Py_TPFLAGS_HAVE_STACKLESS_EXTENSION):
            result.append('Py_TPFLAGS_HAVE_STACKLESS_EXTENSION')
        if self.HasTPFLAG(Py_TPFLAGS_METHOD_DESCRIPTOR):
            result.append('Py_TPFLAGS_METHOD_DESCRIPTOR')
        if self.HasTPFLAG(Py_TPFLAGS_VALID_VERSION_TAG):
            result.append('Py_TPFLAGS_VALID_VERSION_TAG')
        if self.HasTPFLAG(Py_TPFLAGS_IS_ABSTRACT):
            result.append('Py_TPFLAGS_IS_ABSTRACT')
        if self.HasTPFLAG(_Py_TPFLAGS_MATCH_SELF):
            result.append('_Py_TPFLAGS_MATCH_SELF')
        if self.HasTPFLAG(Py_TPFLAGS_ITEMS_AT_END):
            result.append('Py_TPFLAGS_ITEMS_AT_END')
        if self.HasTPFLAG(Py_TPFLAGS_LONG_SUBCLASS):
            result.append('Py_TPFLAGS_LONG_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_LIST_SUBCLASS):
            result.append('Py_TPFLAGS_LIST_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_TUPLE_SUBCLASS):
            result.append('Py_TPFLAGS_TUPLE_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_BYTES_SUBCLASS):
            result.append('Py_TPFLAGS_BYTES_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_UNICODE_SUBCLASS):
            result.append('Py_TPFLAGS_UNICODE_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_DICT_SUBCLASS):
            result.append('Py_TPFLAGS_DICT_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_BASE_EXC_SUBCLASS):
            result.append('Py_TPFLAGS_BASE_EXC_SUBCLASS')
        if self.HasTPFLAG(Py_TPFLAGS_TYPE_SUBCLASS):
            result.append('Py_TPFLAGS_TYPE_SUBCLASS')
    
        return tuple(result)
    
    def __repr__(self) -> str:
        return repr(self.type)
    
    @property
    def members(self) -> Sequence[PyMemberDef]:
        return tuple(self.GetMemberIter())
    
    @members.setter
    def members(self, members: Iterable[PyMemberDef]):
        self.tp_members = PyMemberDef.array(members)
    
    def Reload(self) -> bool:
        self.RemoveTPFLAG(Py_TPFLAGS_READY)
        return PyType_Ready_DEREFERENCED(self) == 0
    
    def GetMemberIter(self) -> 'PyMemberDef_Iterator':
        return PyMemberDef_Iterator(self.tp_members)
    
    is_static_builtin: bool
    
    is_managed_weakref: bool
    is_managed_dict: bool
    is_preheader: bool
    
    is_sequence: bool
    is_mapping: bool
    
    disallow_instantiation: bool
    is_heap_type: bool
    is_base_type: bool
    immutable: bool
    
    have_vectorcall: bool
    readying: bool
    ready: bool
    
    have_stackless_extension: bool
    have_stackless_ext: bool
    have_gc: bool
    
    is_method_descriptor: bool
    abstract: bool
    
    is_long_subclass: bool
    
    is_tuple_subclass: bool
    is_list_subclass: bool
    
    is_unicode_subclass: bool
    is_bytes_subclass: bool
    
    is_base_exc_subclass: bool
    is_dict_subclass: bool
    is_type_subclass: bool
    
_wrap_tpflag('is_static_builtin', _Py_TPFLAGS_STATIC_BUILTIN)

_wrap_tpflag('is_managed_weakref', Py_TPFLAGS_MANAGED_WEAKREF)
_wrap_tpflag('is_managed_dict', Py_TPFLAGS_MANAGED_DICT)
_wrap_tpflag('is_preheader', Py_TPFLAGS_PREHEADER)

_wrap_tpflag('is_sequence', Py_TPFLAGS_SEQUENCE)
_wrap_tpflag('is_mapping', Py_TPFLAGS_MAPPING)

_wrap_tpflag('disallow_instantiation', Py_TPFLAGS_DISALLOW_INSTANTIATION)
_wrap_tpflag('immutable', Py_TPFLAGS_IMMUTABLETYPE)
_wrap_tpflag('is_heap_type', Py_TPFLAGS_HEAPTYPE)
_wrap_tpflag('is_base_type', Py_TPFLAGS_BASETYPE)

_wrap_tpflag('have_vectorcall', Py_TPFLAGS_HAVE_VECTORCALL)
_wrap_tpflag('readying', Py_TPFLAGS_READYING)
_wrap_tpflag('ready', Py_TPFLAGS_READY)

_wrap_tpflag('have_stackless_extension', Py_TPFLAGS_HAVE_STACKLESS_EXTENSION)
_wrap_tpflag('have_stackless_ext', Py_TPFLAGS_HAVE_STACKLESS_EXTENSION)
_wrap_tpflag('have_gc', Py_TPFLAGS_HAVE_GC)

_wrap_tpflag('is_method_descriptor', Py_TPFLAGS_METHOD_DESCRIPTOR)
_wrap_tpflag('abstract', Py_TPFLAGS_IS_ABSTRACT)

_wrap_tpflag('is_long_subclass', Py_TPFLAGS_LONG_SUBCLASS)

_wrap_tpflag('is_tuple_subclass', Py_TPFLAGS_TUPLE_SUBCLASS)
_wrap_tpflag('is_list_subclass', Py_TPFLAGS_LIST_SUBCLASS)

_wrap_tpflag('is_unicode_subclass', Py_TPFLAGS_UNICODE_SUBCLASS)
_wrap_tpflag('is_bytes_subclass', Py_TPFLAGS_BYTES_SUBCLASS)

_wrap_tpflag('is_base_exc_subclass', Py_TPFLAGS_BASE_EXC_SUBCLASS)
_wrap_tpflag('is_dict_subclass', Py_TPFLAGS_DICT_SUBCLASS)
_wrap_tpflag('is_type_subclass', Py_TPFLAGS_TYPE_SUBCLASS)
    
PyTypeObject_PTR = POINTER(PyTypeObject)
        
class PyMethodDef(Structure):
    _fields_ = [
        ('ml_name', c_char_p),
        ('ml_meth', c_void_p),
        ('ml_flags', c_int),
        ('ml_doc', c_char_p)
    ]
    
    ml_name: str
    ml_meth: int
    ml_flags: int
    ml_doc: str
    
PyMethodDef_PTR = POINTER(PyMethodDef)

class PyCFunctionObject(PyObject[_CWT]):
    _fields_ = [
        ('m_ml', PyMethodDef_PTR),
        ('m_self', PyObject_PTR),
        ('m_module', PyObject_PTR),
        ('m_weakreflist', PyObject_PTR),
        ('vectorcall', c_void_p)
    ]
    m_ml: IPointer[PyMethodDef]
    m_self: IPointer[PyObject]
    m_module: IPointer[PyObject]
    m_weakreflist: IPointer[PyObject]
    vectorcall: int

PyCFunctionObject_PTR = POINTER(PyCFunctionObject)

class PyCMethodObject(Structure):
    _fields_ = [
        ('func', PyCFunctionObject),
        ('mm_class', PyTypeObject_PTR)
    ]
    func: PyCFunctionObject
    mm_class: IPointer[PyTypeObject]
    
PyCMethodObject_PTR = POINTER(PyCMethodObject)

if sys.version_info >= (3, 11):
    class PyDescrObject(PyObject[_CWT]):
        _fields_ = [
            ('d_type', PyTypeObject_PTR),
            ('d_name', PyObject_PTR),
            ('d_qualname', PyObject_PTR)
        ]
        
        d_type: IPointer[PyTypeObject]
        d_name: IPointer[PyObject]
        d_qualname: IPointer[PyObject]
else:
    class PyDescrObject(PyObject[_CWT]):
        _fields_ = [
            ('d_type', PyTypeObject_PTR),
            ('d_name', PyObject_PTR)
        ]
        
        d_type: IPointer[PyTypeObject]
        d_name: IPointer[PyObject]
    
PyDescrObject_PTR = POINTER(PyDescrObject)

class PyMethodDescrObject(PyDescrObject[_CWT]):
    _fields_ = [
        ('d_method', PyMethodDef_PTR),
        ('vectorcall', c_void_p)
    ]
    
    d_method: IPointer[PyMethodDef]
    vectorcall: int
    
PyMethodDescrObject_PTR = POINTER(PyMethodDescrObject)

class PyMemberDescrObject(PyDescrObject[_CWT]):
    _fields_ = [
        ('d_member', PyMemberDef_PTR)
    ]
    d_member: IPointer[PyMemberDef]
    
PyMemberDescrObject_PTR = POINTER(PyMemberDescrObject)

def PyCFunctionObject_CAST(obj: _CWT) -> IPointer[PyCFunctionObject[_CWT]]:
    return cast(id(obj), PyCFunctionObject_PTR)

def PyCFunctionObject_CAST_DEREF(obj: _CWT) -> PyCFunctionObject[_CWT]:
    return cast(id(obj), PyCFunctionObject_PTR).contents

def PyCMethodObject_CAST(obj: _CWT) -> IPointer[PyCMethodObject]:
    return cast(id(obj), PyCMethodObject_PTR)

def PyCMethodObject_CAST_DEREF(obj: _CWT) -> PyCMethodObject:
    return cast(id(obj), PyCMethodObject_PTR).contents

def PyDescrObject_CAST(obj: _CWT) -> IPointer[PyDescrObject]:
    return cast(id(obj), PyDescrObject_PTR)

def PyDescrObject_CAST_DEREF(obj: _CWT) -> PyDescrObject:
    return cast(id(obj), PyDescrObject_PTR).contents

def PyMethodDescrObject_CAST(obj: _CWT) -> IPointer[PyMethodDescrObject[_CWT]]:
    return cast(id(obj), PyMethodDescrObject_PTR)

def PyMethodDescrObject_CAST_DEREF(obj: _CWT) -> PyMethodDescrObject[_CWT]:
    return cast(id(obj), PyMethodDescrObject_PTR).contents

def PyMemberDescrObject_CAST(obj: _CWT) -> IPointer[PyMemberDescrObject[_CWT]]:
    return cast(id(obj), PyMemberDescrObject_PTR)

def PyMemberDescrObject_CAST_DEREF(obj: _CWT) -> PyMemberDescrObject[_CWT]:
    return cast(id(obj), PyMemberDescrObject_PTR).contents

class PyCArgObject(PyObject[_CWT]):
    class U(Union):
        _fields_ = [
            ('c', c_char),
            ('b', c_byte),
            ('h', c_short),
            ('i', c_int),
            ('l', c_long),
            ('q', c_longlong),
            ('g', c_longdouble),
            ('d', c_double),
            ('f', c_float),
            ('p', c_void_p),
            ('D', c_double * 2),
            ('F', c_float * 2),
            ('G', c_longdouble * 2)
        ]
        
        p: c_void_p 
        
    _fields_ = [
        ('pffi_type', c_void_p),
        ('tag', c_char),
        ('value', U),
        ('obj', POINTER(PyObject)),
        ('size', c_ssize_t)
    ]
    
    obj: IPointer[PyObject[_CWT]]
    pffi_type: c_void_p
    tag: c_char
    value: U
    
PyCArgObject_PTR = POINTER(PyCArgObject)
    
class PyCDataObject(PyObject):
    _fields_ = [
        ('b_ptr', c_void_p),
        ('b_needsfree', c_int),
        ('b_base', PyObject_PTR),
        ('b_size', c_ssize_t),
        ('b_length', c_ssize_t),
        ('b_index', c_ssize_t),
        ('b_objects', PyObject_PTR),
        ('b_value', c_ubyte * 16)
    ]
    
    b_ptr: int
    b_needsfree: int
    b_base: IPointer[PyObject]
    b_size: int
    b_length: int
    b_index: int
    b_objects: IPointer[PyObject]
    b_value: IArray[int]
    
PyCDataObject_PTR = POINTER(PyCDataObject)

def PyCDataObject_CAST(o: _CWT) -> IPointer[PyCDataObject]:
    return cast(id(o), PyCDataObject_PTR)

def PyCDataObject_CAST_DEREF(o: _CWT) -> PyCDataObject:
    return cast(id(o), PyCDataObject_PTR).contents

pythonapi._PyObject_GC_New.argtypes = [c_void_p]
pythonapi._PyObject_GC_New.restype = PyObject_PTR

def PyObject_GC_New(typ: Type[_CWT], typeobj) -> IPointer[_CWT]:
    return cast(pythonapi._PyObject_GC_New(id(typeobj)), POINTER(typ))

def NewObject(typeobj: Type[_CWT]) -> _CWT:
    obj = cast(pythonapi._PyObject_GC_New(id(typeobj)), py_object).value
    PyObject_GC_Track(obj)
    return obj
        
pythonapi.PyObject_GC_Track.argtypes = [c_void_p]
pythonapi.PyObject_GC_Track.restype = None

def PyObject_GC_Track(obj):
    pythonapi.PyObject_GC_Track(id(obj))

pythonapi.PyType_Ready.argtypes = [PyTypeObject_PTR]
pythonapi.PyType_Ready.restype = c_int

def PyType_Ready(typeobj: IPointer[PyTypeObject]) -> int: ...

PyType_Ready = pythonapi.PyType_Ready

def PyType_Ready_DEREFERENCED(typeobj: PyTypeObject) -> int:
    return PyType_Ready(byref(typeobj))

pythonapi.Py_IncRef.argtypes = [c_void_p]
pythonapi.Py_IncRef.restype = None

def Py_INCREF(obj):
    pythonapi.Py_IncRef(id(obj))

pythonapi.Py_DecRef.argtypes = [c_void_p]
pythonapi.Py_DecRef.restype = None

def Py_DECREF(obj):
    pythonapi.Py_DecRef(id(obj))
    
pythonapi.PyObject_GC_UnTrack.argtypes = [c_void_p]
pythonapi.PyObject_GC_UnTrack.restype = None

def PyObject_GC_UnTrack(obj):
    pythonapi.PyObject_GC_UnTrack(id(obj))
        
class ICArgObject: ...

class ICData:
    _b_base_: int
    _b_needsfree_: bool
    _objects: typing.Union[Mapping[Any, int], None]
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __ctypes_from_outparam__(self, /): ...
    if sys.version_info >= (3, 14):
        __pointer_type__: type

ICARG_CWT = TypeVar('ICARG_CWT', bound=ICArgObject)

def New_PyCArgObject(t: Type[ICARG_CWT]) -> Optional[IPointer[PyCArgObject[ICARG_CWT]]]:
    p = PyObject_GC_New(PyCArgObject, PyTypeObject_PTR)
    if not p: return None
    
    p.contents.pffi_type = None
    p.contents.tag = b'\x00'
    p.contents.obj = None
    memset(byref(p.contents.value), 0, sizeof(p.contents.value))
    pythonapi.PyObject_GC_Track(p)
    
    return p

ffi_pointer_type = c_int(8)
    
def Init_PyCArgObject(parg: IPointer[PyCArgObject[_CWT]], obj: ICData) -> _CWT:
    arg = cast(parg, py_object).value
    parg.contents.tag = b'P'
    parg.contents.pffi_type = cast(byref(ffi_pointer_type), c_void_p)
    arg._obj = obj
    parg.contents.value.p = cast(cast(id(obj), PyCDataObject_PTR).contents.b_ptr, c_void_p)
    return arg

def PyCArgObject_CAST(obj: ICArgObject) -> IPointer[PyCArgObject[ICArgObject]]:
    return cast(id(obj), PyCArgObject_PTR)

def PyCArgObject_CAST_DEREF(obj: ICArgObject) -> PyCArgObject[ICArgObject]:
    return cast(id(obj), PyCArgObject_PTR).contents

msvcrt = CDLL('msvcrt.dll')

pythonapi.PyObject_Malloc.argtypes = [c_size_t]
pythonapi.PyObject_Malloc.restype = c_void_p

msvcrt.memcpy.argtypes = [c_void_p, c_void_p, c_size_t]
msvcrt.memcpy.restype = c_void_p

msvcrt.wcscpy.argtypes = [c_void_p, c_void_p]
msvcrt.wcscpy.restype = c_void_p

msvcrt.strcpy.argtypes = [c_void_p, c_void_p]
msvcrt.strcpy.restype = c_void_p

pythonapi.PyBytes_FromStringAndSize.argtypes = [c_void_p, c_size_t]
pythonapi.PyBytes_FromStringAndSize.restype = c_void_p

def PyObject_Malloc(size: int) -> c_void_p: ...

def memcpy(dest: c_void_p, src: c_void_p, n: int) -> c_void_p: ...

PyObject_Malloc = pythonapi.PyObject_Malloc
memcpy = msvcrt.memcpy

import sys

def CopyType(type: type) -> type:
    size: int = sys.getsizeof(type)
    new_type = PyObject_Malloc(size)
    memcpy(new_type, id(type), size)
    
    py_new_type = cast(new_type, py_object).value
    
    return py_new_type

def CopyTypeIntoType(type: type, new_type: type):
    memcpy(id(type), id(new_type), sys.getsizeof(type))
    
def ReloadType(type: type) -> bool:
    t_type: IPointer[PyTypeObject] = PyType_CAST(type)
    t_type.contents.ready = False
    return PyType_Ready(t_type) == 0

CArgObject = type(byref(c_int()))
t_PyCArgObject = cast(id(CArgObject), PyTypeObject_PTR)

class PyMemberDef_Iterator:
    _members: IPointer[PyMemberDef]
    _member: PyMemberDef
    _index: int
    
    def __init__(self, tp_members: IPointer[PyMemberDef]):
        if tp_members:
            self._member = tp_members[0]
            self._index = 1
        self._members = tp_members
    
    def __iter__(self):
        return self
    
    def __next__(self) -> PyMemberDef:
        if not self._members:
            raise StopIteration
        
        member = self._member
        
        if not member.name:
            raise StopIteration
        
        self._member = self._members[self._index]
        self._index += 1
        
        return member
    
def Get_PyMemberDef(typ: type, name: AnyStr) -> PyMemberDef: 
    if isinstance(name, str):
        name = name.encode()
    
    for member in PyType_CAST_DEREF(typ).GetMemberIter():
        if member.name == name: return member
        
    return None

def Get_Members(typ: type) -> IPointer[PyMemberDef]:
    tp_members = PyType_CAST_DEREF(typ).tp_members
    if not tp_members: return None
    return tp_members

def SetTPFLAG(typ: type, tp_flag: int):
    t_typ = PyType_CAST_DEREF(typ)
    if t_typ.tp_flags & tp_flag: return
    t_typ.tp_flags |= tp_flag
    
def RemoveTPFLAG(typ: type, tp_flag: int):
    t_typ = PyType_CAST_DEREF(typ)
    if not t_typ.tp_flags & tp_flag: return
    t_typ.tp_flags &= (~tp_flag)
        
def HasTPFLAG(typ: type, tp_flag: int) -> bool:
    return (PyType_CAST_DEREF(typ).tp_flags & tp_flag) != 0

def EnumTPFLAGS(typ: type) -> Sequence[str]:
    return PyType_CAST_DEREF(typ).EnumTPFLAGS()
        
def PyType_CAST(typ: Type[_CWT]) -> IPointer[PyTypeObject[_CWT]]:
    return cast(id(typ), PyTypeObject_PTR)

def PyObject_CAST(obj: _CWT) -> IPointer[PyObject[_CWT]]:
    return cast(id(obj), PyObject_PTR)

def PyType_CAST_DEREF(typ: Type[_CWT]) -> PyTypeObject[_CWT]:
    return cast(id(typ), PyTypeObject_PTR).contents

def PyObject_CAST_DEREF(obj: _CWT) -> PyObject[_CWT]:
    return cast(id(obj), PyObject_PTR).contents

def To_PyObject(obj: IPointer[PyObject[_CWT]]) -> _CWT:
    return obj.contents.object

def To_PyType(typ: IPointer[PyTypeObject[_CWT]]) -> Type[_CWT]:
    return typ.contents.type

def To_PyObject_DEREFERENCED(obj: PyObject[_CWT]) -> _CWT:
    return cast(byref(obj), py_object).value

def To_PyType_DEREFERENCED(typ: PyTypeObject[_CWT]) -> Type[_CWT]:
    return cast(byref(typ), py_object).value

def offsetof(typ: Type[Structure], field: str):
    return getattr(getattr(typ, field), 'offset')

PY_TP_NEW_FUNC = PYFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p)

if sys.version_info >= (3, 14):
    class CFieldObject(PyObject):
        _fields_ = [
            ('byte_offset', c_ssize_t),
            ('byte_size', c_ssize_t),
            ('index', c_ssize_t),
            ('proto', PyObject_PTR),
            ('getfunc', c_void_p),
            ('setfunc', c_void_p),
            ('anonymous', c_bool, 1),
            ('bitfield_size', c_uint8),
            ('bit_offset', c_uint8),
            ('name', PyObject_PTR)
        ]
        byte_offset: int
        byte_size: int
        index: int
        proto: IPointer[PyObject]
        getfunc: int
        setfunc: int
        anonymous: bool
        bitfield_size: int
        bit_offset: int
        name: IPointer[PyObject]
else:
    class CFieldObject(PyObject):
        _fields_ = [
            ('offset', c_ssize_t),
            ('size', c_ssize_t),
            ('index', c_ssize_t),
            ('proto', PyObject_PTR),
            ('getfunc', c_void_p),
            ('setfunc', c_void_p),
            ('anonymous', c_int)
        ]
        offset: int
        size: int
        index: int
        proto: IPointer[PyObject]
        getfunc: int
        setfunc: int
        anonymous: int
        name: IPointer[PyObject]
    
CFieldObject_PTR = POINTER(CFieldObject)

def CFieldObject_CAST(obj: _CWT) -> IPointer[CFieldObject]:
    return cast(id(obj), CFieldObject_PTR)

def CFieldObject_CAST_DEREF(obj: _CWT) -> CFieldObject:
    return cast(id(obj), CFieldObject_PTR).contents

def Init_StructureUnion_fields_patch():
    PyCStructType = type(Structure)
    UnionType = type(Union)
    CField = type(PyTypeObject.tp_flags)
    tp_PyCStructType = PyType_CAST_DEREF(PyCStructType)
    tp_UnionType = PyType_CAST_DEREF(UnionType)
    pfn_PyCStructType_new = cast(tp_PyCStructType.tp_new, PY_TP_NEW_FUNC)
    pfn_UnionType_new = cast(tp_UnionType.tp_new, PY_TP_NEW_FUNC)
    def patch_genericroutine_StructUnion(p_cls):
        cls = cast(p_cls, py_object).value
        fields = getattr(cls, '_fields_', None)
        if fields is not None:
            names = []
            for field in fields:
                names.append(field[0])
            for name in names:
                field_obj = getattr(cls, name, None)
                if field_obj is None: continue
                if not isinstance(field_obj, CField): continue
                cfield = CFieldObject_CAST_DEREF(field_obj)
                if cfield.proto:
                    proto = cfield.proto.contents.object
                    ty = getattr(proto, '_type_', None)
                    if ty is not None:
                        ty2 = getattr(ty, '_type_', None)
                        if ty2 in ('u', 'c'):
                            cfield.getfunc = None
    def patch_PyCStructType_new(p_metacls, p_args, p_kwds):
        p_cls = pfn_PyCStructType_new(p_metacls, p_args, p_kwds)
        patch_genericroutine_StructUnion(p_cls)
        return p_cls
    def patch_UnionType_new(p_metacls, p_args, p_kwds):
        p_cls = pfn_UnionType_new(p_metacls, p_args, p_kwds)
        patch_genericroutine_StructUnion(p_cls)
        return p_cls
    pfn_patch_PyCStructType_new = PY_TP_NEW_FUNC(patch_PyCStructType_new)
    pfn_patch_UnionType_new = PY_TP_NEW_FUNC(patch_UnionType_new)
    _GLOBAL_REFS.append(pfn_patch_PyCStructType_new)
    _GLOBAL_REFS.append(pfn_patch_UnionType_new)
    tp_PyCStructType.tp_new = cast(pfn_patch_PyCStructType_new, c_void_p)
    tp_UnionType.tp_new = cast(pfn_patch_UnionType_new, c_void_p)
    tp_PyCStructType.Reload()
    tp_UnionType.Reload()

class CArrayIterator:
    def __init__(self, arr):
        self.arr = arr
        self.l = len(arr)
        self.i = 0
    
    def __next__(self):
        i = self.i
        if i == self.l:
            raise StopIteration
        self.i = i + 1
        return self.arr[i]

def MProxy_Access(mp) -> dict:
    return cast(id(mp), POINTER(MProxy)).contents.mapping.contents.object

def Init_Array_indexing_and_getset_patch():
    tp_Array = PyType_CAST_DEREF(Array)
    pfn_Array_subscript = cast(tp_Array.tp_as_mapping[1], PY_BINARY_FUNC)
    pfn_Array_ass_subscript = cast(tp_Array.tp_as_mapping[2], PY_TERNARY_WITH_ERR_FUNC)
    def patch_Array_subscript(p_self, p_value):
        try:
            value = cast(p_value, py_object).value
            if isinstance(value, int):
                self = cast(p_self, py_object).value
                cdata: PyCDataObject = cast(p_self, PyCDataObject_PTR).contents
                length = cdata.b_length
                ty = self._type_
                if value < 0 or value >= length:
                    b_length = cdata.b_length
                    if b_length == 0:
                        cdata.b_length = 1
                    offset = sizeof(ty) * value
                    b_ptr = cdata.b_ptr
                    cdata.b_ptr = b_ptr + offset
                    index = 0
                    p_result = pfn_Array_subscript(p_self, id(index))
                    cdata.b_ptr = b_ptr
                    if b_length == 0:
                        cdata.b_length = 0
                else:
                    p_result = pfn_Array_subscript(p_self, p_value)
                ty2 = getattr(ty, '_type_', None)
                if ty2 == 'c':
                    result = cast(p_result, py_object).value
                    result = result[0]
                    p_result = id(result)
                return p_result
            else:
                pfn_Array_subscript(p_self, p_value)
        except Exception as e:
            print('DefbCI Detected contract violation or unexpected error at (array)[x] operator')
            print(f'Exception type: {type(e).__qualname__}')
            print(f'Exception description: {e}')
            print('------------------------')
            traceback.print_tb(e.__traceback__)
            print('------------------------')
        return 0
    pfn_patch_Array_subscript = PY_BINARY_FUNC(patch_Array_subscript)
    _GLOBAL_REFS.append(pfn_patch_Array_subscript)
    def patch_Array_ass_subcript(p_self, p_item, p_value):
        try:
            item = cast(p_item, py_object).value
            if isinstance(item, int):
                self = cast(p_self, py_object).value
                cdata: PyCDataObject = cast(p_self, PyCDataObject_PTR).contents
                length = cdata.b_length
                ty = getattr(self, '_type_', None)
                if ty is not None:
                    if item < 0 or item >= length:
                        b_length = cdata.b_length
                        if b_length == 0:
                            cdata.b_length = 1
                        offset = sizeof(ty) * item
                        b_ptr = cdata.b_ptr
                        cdata.b_ptr = b_ptr + offset
                        index = 0
                        pfn_Array_ass_subscript(p_self, id(index), p_value)
                        cdata.b_ptr = b_ptr
                        if b_length == 0:
                            cdata.b_length = 0
                    else:
                        pfn_Array_ass_subscript(p_self, p_item, p_value)
            else:
                pfn_Array_ass_subscript(p_self, p_item, p_value)
        except Exception as e:
            print('DefbCI Detected contract violation or unexpected error at (array)[x] equal operator')
            print(f'Exception type: {type(e).__qualname__}')
            print(f'Exception description: {e}')
            print('------------------------')
            traceback.print_tb(e.__traceback__)
            print('------------------------')
        return 0
    pfn_patch_Array_ass_subscript = PY_TERNARY_WITH_ERR_FUNC(patch_Array_ass_subcript)
    _GLOBAL_REFS.append(pfn_patch_Array_ass_subscript)
    tp_Array.tp_as_mapping[1] = cast(pfn_patch_Array_subscript, c_void_p)
    tp_Array.tp_as_mapping[2] = cast(pfn_patch_Array_ass_subscript, c_void_p)
    PyCArrayType = type(Array)
    tp_PyCArrayType = PyType_CAST_DEREF(PyCArrayType)
    pfn_PyCArrayType_new = cast(tp_PyCArrayType.tp_new, PY_TP_NEW_FUNC)
    def patch_CharArray_getter_value(p_self, p_unused):
        self = cast(p_self, py_object).value
        result = c_char_p(addressof(self)).value
        Py_INCREF(result)
        return id(result)
    pfn_patch_CharArray_getter_value = PY_BINARY_FUNC(patch_CharArray_getter_value)
    _GLOBAL_REFS.append(pfn_patch_CharArray_getter_value)
    def patch_CharArray_setter_value(p_self, p_value, p_unused):
        self = cast(p_self, py_object).value
        value = cast(p_value, py_object).value
        if value is None:
            cast(addressof(self), POINTER(c_char))[0] = 0
        else:
            try:
                msvcrt.strcpy(self, value)
            except Exception as e:
                print('DefbCI Detected contract violation or unexpected error at (char array)::value setter')
                print(f'Exception type: {type(e).__qualname__}')
                print(f'Exception description: {e}')
                print('------------------------')
                traceback.print_tb(e.__traceback__)
                print('------------------------')
        return 0
    pfn_patch_CharArray_setter_value = PY_TERNARY_WITH_ERR_FUNC(patch_CharArray_setter_value)
    _GLOBAL_REFS.append(pfn_patch_CharArray_setter_value)
    def patch_WcharArray_getter_value(p_self, p_unused):
        self = cast(p_self, py_object).value
        result = c_wchar_p(addressof(self)).value
        Py_INCREF(result)
        return id(result)
    pfn_patch_WcharArray_getter_value = PY_BINARY_FUNC(patch_WcharArray_getter_value)
    _GLOBAL_REFS.append(pfn_patch_WcharArray_getter_value)
    def patch_WcharArray_setter_value(p_self, p_value, p_unused):
        self = cast(p_self, py_object).value
        value = cast(p_value, py_object).value
        if value is None:
            cast(addressof(self), POINTER(c_char))[0] = 0
        else:
            try:
                msvcrt.wcscpy(self, value)
            except Exception as e:
                print('DefbCI Detected contract violation or unexpected error at (wchar array)::value setter')
                print(f'Exception type: {type(e).__qualname__}')
                print(f'Exception description: {e}')
                print('------------------------')
                traceback.print_tb(e.__traceback__)
                print('------------------------')
        return 0
    pfn_patch_WcharArray_setter_value = PY_TERNARY_WITH_ERR_FUNC(patch_WcharArray_setter_value)
    _GLOBAL_REFS.append(pfn_patch_WcharArray_setter_value)
    def patch_Array_getter_raw(p_self, p_unused):
        cdata = cast(p_self, PyCDataObject_PTR).contents
        self = cast(p_self, py_object).value
        ty = getattr(self, '_type_', None)
        if ty is None:
            size_of = 1
        else:
            size_of = sizeof(ty)
        return pythonapi.PyBytes_FromStringAndSize(cdata.b_ptr, cdata.b_length * size_of)
    pfn_patch_Array_getter_raw = PY_BINARY_FUNC(patch_Array_getter_raw)
    _GLOBAL_REFS.append(pfn_patch_Array_getter_raw)
    def patch_Array_setter_raw(p_self, p_value, p_unused):
        cdata = cast(p_self, PyCDataObject_PTR).contents
        value = cast(p_value, py_object).value
        if value is None:
            cast(cdata.b_ptr, POINTER(c_char))[0] = 0
        else:
            try:
                msvcrt.strcpy(cdata.b_ptr, value)
            except Exception as e:
                print('DefbCI Detected contract violation or unexpected error at (wchar array)::raw setter')
                print(f'Exception type: {type(e).__qualname__}')
                print(f'Exception description: {e}')
                print('------------------------')
                traceback.print_tb(e.__traceback__)
                print('------------------------')
        return 0
    pfn_patch_Array_setter_raw = PY_TERNARY_WITH_ERR_FUNC(patch_Array_setter_raw)
    _GLOBAL_REFS.append(pfn_patch_Array_setter_raw)
    psz_value = create_string_buffer(b"value")
    psz_raw = create_string_buffer(b"raw")
    _GLOBAL_REFS.append(psz_value)
    _GLOBAL_REFS.append(psz_raw)
    getsets_for_CharArray = (PyGetSetDef * 3)(PyGetSetDef(cast(psz_raw, c_char_p), cast(pfn_patch_Array_getter_raw, c_void_p), cast(pfn_patch_Array_setter_raw, c_void_p)), 
                                              PyGetSetDef(cast(psz_value, c_char_p), cast(pfn_patch_CharArray_getter_value, c_void_p), cast(pfn_patch_CharArray_setter_value, c_void_p)), 
                                              PyGetSetDef())
    getsets_for_WCharArray = (PyGetSetDef * 3)(PyGetSetDef(cast(psz_raw, c_char_p), cast(pfn_patch_Array_getter_raw, c_void_p), cast(pfn_patch_Array_setter_raw, c_void_p)), 
                                               PyGetSetDef(cast(psz_value, c_char_p), cast(pfn_patch_WcharArray_getter_value, c_void_p), cast(pfn_patch_WcharArray_setter_value, c_void_p)), 
                                               PyGetSetDef())
    getsets_for_Array = (PyGetSetDef * 2)(PyGetSetDef(cast(psz_raw, c_char_p), cast(pfn_patch_Array_getter_raw, c_void_p), cast(pfn_patch_Array_setter_raw, c_void_p)), 
                                          PyGetSetDef())
    def patch_Array_iter(p_self):
        self = cast(p_self, py_object).value
        it = CArrayIterator(self)
        Py_INCREF(it)
        return id(it)
    pfn_patch_Array_iter = PY_SINGLE_FUNC(patch_Array_iter)
    def patch_PyCArrayType_new(p_metacls, p_args, p_kwds):
        p_result = pfn_PyCArrayType_new(p_metacls, p_args, p_kwds)
        tp_result: PyTypeObject = cast(p_result, PyTypeObject_PTR).contents
        tp_result.tp_as_mapping[1] = cast(pfn_patch_Array_subscript, c_void_p)
        tp_result.tp_as_mapping[2] = cast(pfn_patch_Array_ass_subscript, c_void_p)
        result = cast(p_result, py_object).value
        ty = getattr(result, '_type_', None)
        if ty is not None:
            ty2 = getattr(ty, '_type_', None)
            if ty2 == 'c':
                getsets = getsets_for_CharArray
                dictionary = MProxy_Access(result.__dict__)
                if 'value' in dictionary:
                    del dictionary['value']
                if 'raw' in dictionary:
                    del dictionary['raw']
            elif ty2 == 'u':
                getsets = getsets_for_WCharArray
                dictionary = MProxy_Access(result.__dict__)
                if 'value' in dictionary:
                    del dictionary['value']
            else:
                getsets = getsets_for_Array
            tp_result.tp_getset = cast(getsets, PyGetSetDef_PTR)
        tp_result.tp_iter = cast(pfn_patch_Array_iter, c_void_p)
        tp_result.Reload()
        return p_result
    tp_Array.tp_getset = cast(getsets_for_Array, PyGetSetDef_PTR)
    tp_Array.Reload()
    pfn_patch_PyCArrayType_new = PY_TP_NEW_FUNC(patch_PyCArrayType_new)
    _GLOBAL_REFS.append(pfn_patch_PyCArrayType_new)
    tp_PyCArrayType.tp_new = cast(pfn_patch_PyCArrayType_new, c_void_p)
    tp_PyCArrayType.Reload()

def Init():
    SetTPFLAG(CArgObject, Py_TPFLAGS_BASETYPE)
    SetTPFLAG(bool, Py_TPFLAGS_BASETYPE)
    Get_PyMemberDef(CArgObject, '_obj').readonly = False
    
    t_mappingproxy = PyType_CAST_DEREF(mappingproxy)
    t_mappingproxy.members = [PyMemberDef('m_proxy', Py_T_OBJECT_EX,
                                          MProxy.offset('mapping'))]
    t_mappingproxy.Reload()
    t_codetype = PyType_CAST_DEREF(type(HasTPFLAG.__code__))
    for member in t_codetype.members:
        member.readonly = False
    t_cdata = PyType_CAST_DEREF(Structure.__base__)
    for member in t_cdata.members:
        member.readonly = False
    
    Init_StructureUnion_fields_patch()
    Init_Array_indexing_and_getset_patch()
    
    for init_routine in _INIT_CHAIN:
        init_routine()