from ctypes import *

import sys

defined_Py_TRACE_REFS = hasattr(sys, 'getobjects')

if not hasattr(sys, '_is_gil_enabled'):
    GIL_ENABLED = True
else:
    GIL_ENABLED = sys._is_gil_enabled()
    
from typing import (TypeVar, Generic, Optional, 
                    Mapping, Any, Self, Dict,
                    AnyStr, Sequence, Type,
                    Iterable)
    
_CWT = TypeVar('_WT')

class IArray(Generic[_CWT]):
    def __getitem__(self, index: int) -> _CWT: ...
    
    def __setitem__(self, index: int, value: _CWT) -> _CWT: ...

class IPointer(IArray[_CWT]):   
    contents: _CWT

if sys.version_info < (3, 10):
    raise RuntimeError('Versions before 3.10 are not supported.')

if sys.version_info >= (3, 10) and sys.version_info < (3, 12):
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
        
elif sys.version_info >= (3, 12) and sys.version_info < (3, 15):
    if sys.version_info != (3, 14):
        class PyObject(Structure, Generic[_CWT]):
            fields_extra = []
            if defined_Py_TRACE_REFS:
                fields_extra = [
                    ('unusedPtr', c_void_p),
                    ('unusedPtr2', c_void_p)
                ]
            _fields_ = fields_extra + [
                ('unusedInt64', c_int64),
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
        ('unusedInt', c_int),
        ('unusedSizeT', c_ssize_t),
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
        result: list[str] = []
        
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
    # только нужные
    _fields_ = [
        ('tp_name', c_char_p),
        ('tp_basicsize', c_ssize_t),
        ('unusedSizeT', c_ssize_t),
        ('tp_dealloc', c_void_p),
        ('unusedSizeT3', c_ssize_t),
        ('unusedPtrs', c_void_p * 13),
        ('tp_flags', c_ulong),
        ('unusedPtrs2', c_void_p * 8),
        ('tp_members', PyMemberDef_PTR),
        ('unusedPtrs3', c_void_p * 2),
        ('tp_dict', PyMappingProxyObject_PTR)
    ]
    
    tp_dict: IPointer[MProxy[dict]]
    tp_members: IPointer[PyMemberDef]
    tp_dealloc: c_void_p
    tp_basicsize: int
    tp_flags: int
    
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
        result: list[str] = []
        
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
    
class PyCDataObject_HEADLESS(PyObject):
    _fields_ = [
        ('b_ptr', c_char_p)
    ]
    
    b_ptr: c_char_p
    
PyCDataObject_HEADLESS_PTR = POINTER(PyCDataObject_HEADLESS)
    
pythonapi._PyObject_GC_New.argtypes = [PyTypeObject_PTR]
pythonapi._PyObject_GC_New.restype = PyObject_PTR
        
def PyObject_GC_New(typ: type[_CWT], typeobj: IPointer[PyTypeObject]) -> IPointer[_CWT]:
    return cast(pythonapi._PyObject_GC_New(typeobj), POINTER(typ))
        
pythonapi.PyObject_GC_Track.argtypes = [c_void_p]
pythonapi.PyObject_GC_Track.restype = None

def PyObject_GC_Track(obj: IPointer[PyObject]): ...

PyObject_GC_Track = pythonapi.PyObject_GC_Track

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
        
class ICArgObject: ...

class ICData:
    _b_base_: int
    _b_needsfree_: bool
    _objects: Mapping[Any, int] | None
    def __buffer__(self, flags: int, /) -> memoryview: ...
    def __ctypes_from_outparam__(self, /) -> Self: ...
    if sys.version_info >= (3, 14):
        __pointer_type__: type

ICARG_CWT = TypeVar('ICARG_CWT', bound=ICArgObject)

def New_PyCArgObject(t: type[ICARG_CWT]) -> Optional[IPointer[PyCArgObject[ICARG_CWT]]]:
    p = PyObject_GC_New(PyCArgObject, cast(id(t), PyTypeObject_PTR))
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
    parg.contents.value.p = cast(cast(id(obj), PyCDataObject_HEADLESS_PTR).contents.b_ptr, c_void_p)
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
        
        self._index += 1
        self._member = self._members[self._index]
        
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
        
def PyType_CAST(typ: type[_CWT]) -> IPointer[PyTypeObject[_CWT]]:
    return cast(id(typ), PyTypeObject_PTR)

def PyObject_CAST(obj: _CWT) -> IPointer[PyObject[_CWT]]:
    return cast(id(obj), PyObject_PTR)

def PyType_CAST_DEREF(typ: type[_CWT]) -> PyTypeObject[_CWT]:
    return cast(id(typ), PyTypeObject_PTR).contents

def PyObject_CAST_DEREF(obj: _CWT) -> PyObject[_CWT]:
    return cast(id(obj), PyObject_PTR).contents

def To_PyObject(obj: IPointer[PyObject[_CWT]]) -> _CWT:
    return obj.contents.object

def To_PyType(typ: IPointer[PyTypeObject[_CWT]]) -> type[_CWT]:
    return typ.contents.type

def To_PyObject_DEREFERENCED(obj: PyObject[_CWT]) -> _CWT:
    return cast(byref(obj), py_object).value

def To_PyType_DEREFERENCED(typ: PyTypeObject[_CWT]) -> type[_CWT]:
    return cast(byref(typ), py_object).value

def offsetof(typ: type[Structure], field: str):
    return getattr(getattr(typ, field), 'offset')

mappingproxy = type(type.__dict__)

def Init():
    SetTPFLAG(CArgObject, Py_TPFLAGS_BASETYPE)
    SetTPFLAG(bool, Py_TPFLAGS_BASETYPE)
    Get_PyMemberDef(CArgObject, '_obj').readonly = False
    
    t_mappingproxy = PyType_CAST_DEREF(mappingproxy)
    t_mappingproxy.members = [PyMemberDef('m_proxy', _Py_T_OBJECT,
                                          MProxy.offset('mapping'))]
    t_mappingproxy.Reload()
    
"""
from types import MappingProxyType
    
class PyMappingProxy(Dict):
    _proxy: MappingProxyType
    
    def __init__(self, proxy: MappingProxyType):
        if not hasattr(proxy, 'm_proxy'):
            raise RuntimeError('Not marked proxy object')
        self._proxy = proxy
        
    
"""