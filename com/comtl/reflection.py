from ..autointerfacedef import *
from typing import Iterable
from .factory import *

SetGuid('IPythonObject', IID('{69BE9AC3-E648-46F9-B600-46B9F807260F}'))

class IPythonObject(IUnknown):
    """
    Interface representing Python object.
    """
    
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(PVOID)
    def GetPyObject(self, ppv: IPointer[PVOID]) -> int:
        """
        Return the raw PyObject pointer to object.
        """
    
    @virtual_table.com_function(PTR(LPWSTR))
    def GetName(self, ppwszName: IPointer[LPWSTR]) -> int:
        """
        Get the name of object.
        """
        
    @virtual_table.com_function(PVOID)
    def GetType(self, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Get the Python type of object represented by `IPythonObject`.
        """
        
    @virtual_table.com_function(PTR(LPWSTR))
    def GetRepr(self, ppwszRepr: IPointer[LPWSTR]) -> int: 
        """
        Get the string representation of Python object.
        """
        
    @virtual_table.com_function(PTR(LPWSTR))
    def ToString(self, ppwszString: IPointer[LPWSTR]) -> int:
        """
        Return the string representation of Python object.
        """
        
    @virtual_table.com_function(PVOID)
    def GetDir(self, ppDirObj: IDoublePtr['IPythonObject']) -> int:
        """
        Return the dir(...) object.
        """
        
    @virtual_table.com_function(INT, PVOID)
    def GetObjectByIndex(self, index: int, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Get the object by index (if supports indexing).
        """
        
    @virtual_table.com_function(INT, PVOID)
    def SetObjectByIndex(self, index: int, pObject: IPointer['IPythonObject']) -> int:
        """
        Set the object by index (if supports settable indexing).
        """
        
    @virtual_table.com_function(PVOID)
    def Iterate(self, ppObjEnumerator: IDoublePtr['IEnumPythonObject']) -> int:
        """
        Get the Python object enumerator (if supported iterating).
        """
        
    @virtual_table.com_function(LPCWSTR, PVOID)
    def GetAttr(self, pwszAttr: str, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Get the Python object by attribute name.
        """
        
    @virtual_table.com_function(INT, PVOID)
    def SetAttr(self, pwszAttr: str, pObject: IPointer['IPythonObject']) -> int:
        """
        Set the Python object by attribute name.
        """
        
    @virtual_table.com_function(UINT, PVOID, PVOID, PVOID)
    def Call(self, nArguments: int, ppReturnObj: IPointer['IPythonObject'],
             ppObjArguments: IDoublePtr['IPythonObject'], 
             pObjKwargs: IPointer['IPythonObject']) -> int:
        """
        Call the Python object with provided arguments.
        """
        
    @virtual_table.com_function(LPVARIANT)
    def GetVariant(self, pVar: IPointer[VARIANT]) -> int:
        """
        Get the variant value.
        """
        
    @virtual_table.com_function(PVOID)
    def GetError(self, ppError: IDoublePtr['IPythonError']) -> int:
        """
        Get the Python error if ocurred.
        """
    
    @virtual_table.com_function(PVOID, PVOID)
    def GetItem(self, pItemIndex: IPointer['IPythonObject'],
                ppItem: IDoublePtr['IPythonObject']) -> int: 
        """
        Get the item by Python index.
        """
        
    @virtual_table.com_function(PVOID, PVOID)
    def SetItem(self, pItemIndex: IPointer['IPythonObject'],
                pItem: IDoublePtr['IPythonObject']) -> int: 
        """
        Set the item by Python index.
        """
        
    @virtual_table.com_function(PVOID)
    def DelItem(self, pItemIndex: IPointer['IPythonObject']) -> int:
        """
        Delete the item by Python index.
        """
        
    @virtual_table.com_function(PVOID, PVOID, PVOID)
    def CallTuple(self, ppReturnObj: IPointer['IPythonObject'], 
                  pObjArguments: IPointer['IPythonObject'], 
                  pObjKwargs: IPointer['IPythonObject']) -> int:
        """
        Call the Python object with provided arguments.
        """
    
    virtual_table.build()
    
LPPYTHONOBJECT = IPythonObject.PTR()
    
SetGuid('IEnumPythonObject', IID('{48E0CAD3-B773-4673-96D6-898FAD6B5449}'))
    
class IEnumPythonObject(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(ULONG, POINTER(LPPYTHONOBJECT), PULONG)
    def Next(self, celt: int, rgelt: IDoublePtr[IPythonObject],
             pceltFetched: PULONG) -> int: 
        """
        Return the next `celt` elements
        """
    
    @virtual_table.com_function(ULONG)
    def Skip(self, celt: int) -> int: 
        """
        Skip `celt` elements
        """
    
    @virtual_table.com_function()
    def Reset(self) -> int: 
        """
        Reset the enumerator state
        """
    
    @virtual_table.com_function(PVOID)
    def Clone(self, ppenum: IDoublePtr['IEnumPythonObject']) -> int: 
        """
        Clone the enumerator
        """
    
    virtual_table.build()
    
class EnumPythonObject(CComClass, IEnumPythonObject):
    """
    Python Object Enumerator implementation
    """
    
    _com_map_ = [(IEnumPythonObject, IEnumPythonObject.virtual_table)]
    
    _iterable: Iterable
    _index: int
    
    def __init__(self, iterable: Iterable):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IEnumPythonObject
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.Next)
        self.implement(self.Skip)
        self.implement(self.Reset)
        self.implement(self.Clone)
        
        self._iterable = iterable
        self._index = 0
        
    def Next_Impl(self, celt: int, rgelt: IDoublePtr[WET_PROVIDER],
             pceltFetched: PULONG) -> int: 
        if celt == 0: # celt == 0, set the pceltFetched to 0 and return S_OK
            self.dbg_trace(provider, 'celt == 0')
            
            if pceltFetched:
                pceltFetched.contents = 0
                
            return S_OK
        
        if not rgelt:
            self.dbg_trace(provider, 'rgelt == NULL!')
            return E_POINTER
        
        # if celt > 1 and pceltFetched is NULL, then return error (by COM enumerator specification)
        if celt != 1 and not pceltFetched:
            self.dbg_trace(provider, 'celt != 1 && pceltFetched == NULL!')
            return E_POINTER
        
        list_iterable = list(self._iterable)
        
        # iterate in range(0, celt)
        for i in range(celt):
            index = self._index + i
            
            # if reached out of bounds
            if index == len(list_iterable):
                self._index += celt # move the index
                
                if pceltFetched: # if pceltFetched, return the fetched elements count
                    pceltFetched.contents.value = i
                    
                self.dbg_trace(provider, f'S_FALSE, fetched {i}')
                
                return S_FALSE # enumeration stopped
            
            # otherwise, write the provider pointer to rgelt[i]
            obj = PythonObject(list_iterable[index])
            rgelt[i] = i_cast(obj.ptr(), LPPYTHONOBJECT)
        
        # if pceltFetched, return the fetched elements count
        if pceltFetched:
            pceltFetched.contents.value = celt
            
        self._index += celt # move the index
        
        self.dbg_trace(provider, f'S_OK, fetched {celt}')
        
        return S_OK
    
    def Skip_Impl(self, celt: int) -> int: 
        self._index += celt # skip the celt elements
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Reset_Impl(self) -> int:
        self._index = 0 # reset the enumerator
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Clone_Impl(self, ppenum: IDoublePtr['IEnumPythonObject']) -> int:
        if not ppenum:
            self.dbg_trace(provider, 'ppenum == NULL!')
            return E_POINTER
        
        # clone the enumerator and its state
        enum = EnumPythonObject()
        enum._index = self._index
        ppenum.contents = enum.ptr()
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
E_BOUNDS = 0x8000000B
E_ILLEGAL_METHOD_CALL = 0x8000000E
    
from .baseface import *

def TlObjectItfToPython(pvItf: int) -> Any:
    pObject = i_cast(pvItf, LPPYTHONOBJECT)
    pvPyObject = PVOID()
    pObject.contents.GetPyObject(byref(pvPyObject))
    return i_cast(pvPyObject, py_object).value

class PythonObject(CComClass, IPythonObject):
    """
    Core Python Object implementation
    """
    
    _com_map_ = [(IPythonObject, IPythonObject.virtual_table)]
    _exc: Exception
    _obj: Any
    
    def __init__(self, obj):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IPythonObject
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.GetPyObject)
        self.implement(self.GetName)
        self.implement(self.GetType)
        self.implement(self.GetRepr)
        self.implement(self.ToString)
        self.implement(self.GetDir)
        self.implement(self.Iterate)
        self.implement(self.GetObjectByIndex)
        self.implement(self.SetObjectByIndex)
        self.implement(self.GetAttr)
        self.implement(self.SetAttr)
        self.implement(self.Call)
        self.implement(self.GetVariant)
        self.implement(self.GetError)
        self.implement(self.GetItem)
        self.implement(self.SetItem)
        self.implement(self.DelItem)
        self.implement(self.CallTuple)
        
        self._obj = obj
        self._exc = None
        
    def GetPyObject_Impl(self, pvPpv: int) -> int:
        if not pvPpv:
            self.dbg_trace(provider, 'ppv == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        TlWritePvToPpv(pvPpv, id(self._obj))
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetName_Impl(self, ppwszName: IPointer[LPWSTR]) -> int:
        if not ppwszName:
            self.dbg_trace(provider, 'ppwszName == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        name = getattr(self._obj, '__name__', None)
        if name is None:
            name = getattr(self._obj, '__qualname__', None)
            if name is None:
                self.dbg_trace(provider, 'E_ILLEGAL_METHOD_CALL', level=WET_LEVEL_ERROR)
                return E_ILLEGAL_METHOD_CALL
        
        TlWritePvToPpv(ppwszName, TlAllocateString(name))
        self.dbg_trace(provider, f'*ppwszName = L"{name}" S_OK')
        
        return S_OK
    
    def GetType_Impl(self, pvPpObject: int) -> int:
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        type_obj = PythonObject(type(self._obj))
        TlWritePointerToPpv(pvPpObject, type_obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetRepr_Impl(self, ppwszRepr: IPointer[LPWSTR]) -> int:
        if not ppwszRepr:
            self.dbg_trace(provider, 'ppwszRepr == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        representation = repr(self._obj)
        TlWritePvToPpv(ppwszRepr, TlAllocateString(representation))
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def ToString_Impl(self, ppwszString: IPointer[LPWSTR]) -> int:
        if not ppwszString:
            self.dbg_trace(provider, 'ppwszString == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        string = str(self._obj)
        TlWritePvToPpv(ppwszString, TlAllocateString(string))
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetDir_Impl(self, pvPpDirObj: int) -> int:
        if not pvPpDirObj:
            self.dbg_trace(provider, 'ppDirObj == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        dir_obj = PythonObject(dir(self._obj))
        TlWritePointerToPpv(pvPpDirObj, dir_obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Iterate_Impl(self, pvPpObjEnumerator: int) -> int:
        if not pvPpObjEnumerator:
            self.dbg_trace(provider, 'ppObjEnumerator == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            iter(self._obj)
        except TypeError:
            self.dbg_trace(provider, 'E_ILLEGAL_METHOD_CALL', level=WET_LEVEL_ERROR)
            return E_ILLEGAL_METHOD_CALL
        
        enumerator = EnumPythonObject(self._obj)
        TlWritePointerToPpv(pvPpObjEnumerator, enumerator.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def SetObjectByIndex_Impl(self, index: int, pvPObject: int) -> int:
        if not pvPObject:
            self.dbg_trace(provider, 'pObject == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            iter(self._obj)
        except TypeError:
            self.dbg_trace(provider, 'E_ILLEGAL_METHOD_CALL', level=WET_LEVEL_ERROR)
            return E_ILLEGAL_METHOD_CALL
        
        Object = i_cast(pvPObject, LPPYTHONOBJECT).contents
        PyObject = PVOID()
        Object.GetPyObject(byref(PyObject))
        
        try:
            self._obj[index] = i_cast(PyObject, py_object).value
        except IndexError:
            self.dbg_trace(provider, f'Index {index} out of bounds {len(self._obj)}', level=WET_LEVEL_ERROR)
            return E_BOUNDS
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetObjectByIndex_Impl(self, index: int, pvPpObject: int) -> int:
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            iter(self._obj)
        except TypeError:
            self.dbg_trace(provider, 'E_ILLEGAL_METHOD_CALL', level=WET_LEVEL_ERROR)
            return E_ILLEGAL_METHOD_CALL
        
        try:
            byIndex = PythonObject(self._obj[index])
            TlWritePointerToPpv(pvPpObject, byIndex.ptr())
        except IndexError:
            self.dbg_trace(provider, f'Index {index} out of bounds {len(self._obj)}', level=WET_LEVEL_ERROR)
            return E_BOUNDS
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetAttr_Impl(self, pwszAttr: str, pvPpObject: int) -> int:
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        if not pwszAttr:
            self.dbg_trace(provider, 'pwszAttr == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            attribute = getattr(self._obj, pwszAttr)
        except AttributeError:
            self.dbg_trace(provider, f'No attribute L"{pwszAttr}"', level=WET_LEVEL_ERROR)
            return E_INVALIDARG
        
        obj = PythonObject(attribute)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def SetAttr_Impl(self, pwszAttr: str, pvPObject: int) -> int:
        if not pvPObject:
            self.dbg_trace(provider, 'pObject == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            setattr(self._obj, TlObjectItfToPython(pvPObject))
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def Call_Impl(self, nArguments: int, pvPpReturnObj: int, pvPpObjArguments: int,
                  pvPObjKwargs: int) -> int:
        if not pvPpObjArguments and nArguments != 0:
            self.dbg_trace(provider, 'ppObjArguments == NULL && nArguments != 0!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        ppObjArguments = i_cast(pvPpObjArguments, PTR(LPPYTHONOBJECT))
        args = []
        
        for i in range(nArguments):
            args.append(TlObjectItfToPython(ppObjArguments[i]))
        
        try:
            if pvPObjKwargs:
                kwargs = TlObjectItfToPython(pvPObjKwargs)
                return_value = self._obj(*args, **kwargs)
            else:
                return_value = self._obj(*args)
            if pvPpReturnObj:
                return_obj = PythonObject(return_value)
                TlWritePointerToPpv(pvPpReturnObj, return_obj.ptr())
                
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetVariant_Impl(self, pVar: IPointer[VARIANT]) -> int:
        if not pVar:
            self.dbg_trace(provider, 'pVar == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        var = pVar.contents
        
        if var.vt == VT_I1:
            var.cVal = int(self._obj)
        elif var.vt == VT_UI1:
            var.bVal = int(self._obj)
        elif var.vt == VT_I2:
            var.iVal = int(self._obj)
        elif var.vt == VT_UI2:
            var.uiVal = int(self._obj)
        elif var.vt in (VT_I4, VT_INT):
            var.lVal = int(self._obj)
        elif var.vt in (VT_UI4, VT_UINT):
            var.ulVal = int(self._obj)
        elif var.vt == VT_I8:
            var.llVal = int(self._obj)
        elif var.vt == VT_UI8:
            var.ullVal = int(self._obj)
        elif var.vt == VT_R4:
            var.fltVal = float(self._obj)
        elif var.vt == VT_R8:
            var.dblVal = float(self._obj)
        elif var.vt == VT_BSTR:
            var.bstrVal = TlAllocateOAString(str(self._obj)), BSTR
        elif var.vt == VT_BOOL:
            var.boolVal = VARIANT_FALSE if not bool(self._obj) else VARIANT_TRUE
        else:
            self.dbg_trace(provider, f'Unsupported VT {var.vt}', level=WET_LEVEL_ERROR)
            return E_INVALIDARG
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetError_Impl(self, pvPpError: int) -> int:
        if not pvPpError:
            self.dbg_trace(provider, 'ppError == NULL, returning exception ocurred state', level=WET_LEVEL_ERROR)
            return S_FALSE if self._exc is None else S_OK
        
        if self._exc is None:
            self.dbg_trace(provider, 'No error, S_FALSE', level=WET_LEVEL_ERROR)
            return S_FALSE
        
        obj = PythonObject(self._exc)
        TlWritePointerToPpv(pvPpError, obj.ptr())
        self._exc = None
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetItem_Impl(self, pvPItemIndex: int, pvPpItem: int) -> int:
        if not pvPItemIndex:
            self.dbg_trace(provider, 'pItemIndex == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        if not pvPpItem:
            self.dbg_trace(provider, 'ppItem == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            obj = PythonObject(self._obj[TlObjectItfToPython(pvPItemIndex)])
            TlWritePointerToPpv(pvPpItem, obj.ptr())
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def SetItem_Impl(self, pvPItemIndex: int, pvPItem: int) -> int:
        if not pvPItemIndex:
            self.dbg_trace(provider, 'pItemIndex == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        if not pvPItem:
            self.dbg_trace(provider, 'pItem == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            self._obj[TlObjectItfToPython(pvPItemIndex)] = TlObjectItfToPython(pvPItem)
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def DelItem_Impl(self, pvPItemIndex: int) -> int:
        if not pvPItemIndex:
            self.dbg_trace(provider, 'pItemIndex == NULL!', level=WET_LEVEL_ERROR)
            return E_POINTER
        
        try:
            del self._obj[TlObjectItfToPython(pvPItemIndex)]
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def CallTuple_Impl(self, pvPpReturnObj: int, pvPObjArguments: int, 
                       pvPObjKwargs: int) -> int:
        if pvPObjArguments:
            args = TlObjectItfToPython(pvPObjArguments)
        
        try:
            if pvPObjKwargs:
                kwargs = TlObjectItfToPython(pvPObjKwargs)
                if pvPObjArguments:
                    return_value = self._obj(*args, **kwargs)
                else:
                    return_value = self._obj(**kwargs)
            else:
                if pvPObjArguments:
                    return_value = self._obj(*args)
                else:
                    return_value = self._obj()
                    
            if pvPpReturnObj:
                return_obj = PythonObject(return_value)
                TlWritePointerToPpv(pvPpReturnObj, return_obj.ptr())
                
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"', level=WET_LEVEL_ERROR)
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK

SetGuid('IPythonError', IID('{B7078FA9-A02A-4EA1-AF43-FE5F441598AD}'))

class IPythonError(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(PTR(LPCWSTR))
    def GetDescription(self, ppwszDescription: IPointer[LPCWSTR]) -> int:
        """
        Get the description of error.
        """
        
    @virtual_table.com_function(PVOID)
    def GetObject(self, ppObject: IDoublePtr[IPythonObject]) -> int:
        """
        Get the IPythonObject representing error object.
        """
    
    virtual_table.build()
    
class PythonError(CComClass, IPythonError):
    _com_map_ = [IPythonError, IPythonError.virtual_table]
    
    _obj: Exception
    
    def __init__(self, obj: Exception):
        self.dbg_trace(provider, CUnknown._trace_id_next_)
        super().__init__()
        
        # IPythonError
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.GetDescription)
        self.implement(self.GetObject)
        
        self._obj = obj
        
    def GetDescription_Impl(self, ppwszDescription: IPointer[LPCWSTR]) -> int:
        if not ppwszDescription:
            self.dbg_trace(provider, 'ppwszDescription == NULL!')
            return E_POINTER
        
        TlWritePvToPpv(ppwszDescription, TlAllocateString(str(self._obj)))
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetObject_Impl(self, pvPpObject: int) -> int:
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        obj = PythonObject(self._obj)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK

SetGuid('IPythonManager', IID('{A321D739-D5BC-466F-A5A3-4EF5D9D03C54}'))
    
class IPythonManager(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = GetIID()
    
    @virtual_table.com_function(PVOID, PVOID)
    def GetPyObject(self, PyObject: IVoidPtr, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Get the IPythonObject from PyObject* address.
        """
        
    @virtual_table.com_function(LPCWSTR, PVOID)
    def GetFromGlobal(self, pwszName: str, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Get the IPythonObject from globals by Python name.
        """
        
    @virtual_table.com_function(INT64, PVOID)
    def ObjectFromInt64(self, i64: int, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Create the Python object from 64-bit integer.
        """
        
    @virtual_table.com_function(LPCWSTR, PVOID)
    def ObjectFromString(self, pwszString: str, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Create the Python object from string.
        """
        
    @virtual_table.com_function(LPCWSTR, PVOID)
    def ImportModule(self, pwszModule: str, ppObject: IDoublePtr['IPythonObject']) -> int:
        """
        Import the module by its name.
        """
        
    @virtual_table.com_function(PVOID)
    def GetError(self, ppError: IDoublePtr['IPythonError']) -> int:
        """
        Get the Python error if ocurred.
        """
    
    virtual_table.build()
    
SetGuid('PythonManager', CLSID('{BBDFA1C6-F48B-41EF-AC53-C7C5112A3A1A}'))

import builtins

class PythonManager(CComClass, IPythonManager):
    virtual_table = COMVirtualTable.from_ancestor(IPythonManager)
    _com_map_ = [(IPythonManager, IPythonManager.virtual_table)]
    _clsid_ = GetCLSID()
    _creatable_ = True
    
    _exc: Exception
    
    def __init__(self):
        self.dbg_trace(provider, trace_id=CUnknown._trace_id_next_)
        super().__init__()
        
        # IPythonManager
        self.set_vtable_on_ctx(self.virtual_table)
        self.implement(self.GetPyObject)
        self.implement(self.GetFromGlobal)
        self.implement(self.ObjectFromInt64)
        self.implement(self.ObjectFromString)
        self.implement(self.ImportModule)
        
        self._exc = None
        
    def GetPyObject_Impl(self, PyObject: int, pvPpObject: int) -> int:
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        if not PyObject:
            self.dbg_trace(provider, 'PyObject == NULL!')
            return E_POINTER
        
        pyobj = i_cast(PyObject, py_object)
        if not pyobj:
            self.dbg_trace(provider, 'Corrupted PyObject!')
            return E_POINTER
        
        obj = PythonObject(pyobj.value)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetFromGlobal_Impl(self, pwszName: str, pvPpObject: int) -> int:
        if not pwszName:
            self.dbg_trace(provider, 'pwszName == NULL!')
            return E_POINTER
        
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        if pwszName not in globals():
            if pwszName not in locals():
                if pwszName not in dir(builtins):
                    self.dbg_trace(provider, f'L"{pwszName}" not in global scope!')
                    return E_INVALIDARG
                else:
                    pyobj = getattr(builtins, pwszName)
            else:
                pyobj = locals()[pwszName]
        else:
            pyobj = globals()[pwszName]
        
        obj = PythonObject(pyobj)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def ObjectFromString_Impl(self, pwszString: str, pvPpObject: int) -> int:
        if not pwszString:
            self.dbg_trace(provider, 'pwszString == NULL!')
            return E_POINTER
        
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        obj = PythonObject(pwszString)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def ObjectFromInt64_Impl(self, i64: int, pvPpObject: int):
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        obj = PythonObject(i64)
        TlWritePointerToPpv(pvPpObject, obj.ptr())
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def ImportModule_Impl(self, pwszModule: str, pvPpObject: int) -> int:
        if not pwszModule:
            self.dbg_trace(provider, 'pwszModule == NULL!')
            return E_POINTER
        
        if not pvPpObject:
            self.dbg_trace(provider, 'ppObject == NULL!')
            return E_POINTER
        
        try:
            module = __import__(pwszModule)
            obj = PythonObject(module)
            TlWritePointerToPpv(pvPpObject, obj.ptr())
        except Exception as e:
            self.dbg_trace(provider, f'Unexpected exception "{e}"')
            self._exc = e
            return E_FAIL
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    def GetError_Impl(self, pvPpError: int) -> int:
        if not pvPpError:
            self.dbg_trace(provider, 'ppError == NULL, returning exception ocurred state')
            return S_FALSE if self._exc is None else S_OK
        
        if self._exc is None:
            self.dbg_trace(provider, 'No error, S_FALSE')
            return S_FALSE
        
        obj = PythonObject(self._exc)
        TlWritePointerToPpv(pvPpError, obj.ptr())
        self._exc = None
        
        self.dbg_trace(provider, 'S_OK')
        return S_OK
    
    virtual_table.build()