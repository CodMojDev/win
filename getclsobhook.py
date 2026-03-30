from win import _defbase_ctypinit as dc
from win.com.baseinterfacedef import *
from win.defbase_errordef import *
from win.cimpl.cimpldef import *
from win.libloaderapi import *
from win.memoryapi import *
from win.com.comtl import *
from win.winnt import *

import keystone as KS

rpcrt4 = get_win_library('rpcrt4.dll')
NdrDllGetClassObject_address = PtrUtil.get_address(rpcrt4.NdrDllGetClassObject)

@CStructure.make
class CInterfaceProxyHeader(CStructure):
    pStublessProxyInfo: IVoidPtr
    piid: IPointer[IID]

@CStructure.make
class CInterfaceProxyVtbl(CStructure):
    Vtbl: IArray[IVoidPtr]
    reset_annotations()
    header: CInterfaceProxyHeader

array_after_structure(CInterfaceProxyVtbl, 'Vtbl', PVOID)

@CStructure.make
class CInterfaceStubHeader(CStructure):
    piid: IPointer[IID]
    pServerInfo: IVoidPtr
    DispatchTableCount: IUInt32
    pDispatchTable: IPointer[PVOID]

IRpcStubBufferVtbl = IRpcStubBuffer.virtual_table.VType

@CStructure.make
class CInterfaceStubVtbl(CStructure):
    header: CInterfaceStubHeader
    Vtbl: IRpcStubBufferVtbl # pyright: ignore[reportInvalidTypeForm]

@CStructure.make
class ProxyFileInfo(CStructure): 
    pProxyVtblList: IPointer[CInterfaceProxyVtbl]
    pStubVtblList: IPointer[CInterfaceStubVtbl]
    pNamesArray: IPointer[LPCSTR]
    pDelegatedIIDs: IDoublePtr[IID]
    pIIDLookupRtn: IVoidPtr
    TableSize: IUShort
    TableVersion: IUShort
    pAsyncIIDLookup: IDoublePtr[IID]
    Filler2: ILongPtr
    Filler3: ILongPtr
    Filler4: ILongPtr

@rpcrt4.foreign(HRESULT, REFCLSID, REFIID, PVOID, DOUBLE_PTR(ProxyFileInfo), LPCLSID, PVOID)
def NdrDllGetClassObject(rclsid: IPointer[CLSID], riid: IPointer[IID], ppv: IPointer[PVOID], 
                         pProxyFileList: IDoublePtr[ProxyFileInfo], pClsid: IPointer[CLSID],
                         pPSFactoryBuffer: IVoidPtr) -> IInteger[HRESULT]: ...

#NdrDllGetClassObject_T = CFUNCTYPE(HRESULT, REFCLSID, REFIID, PVOID, DOUBLE_PTR(ProxyFileInfo), LPCLSID, PVOID)

def Py_NdrDllGetClassObject_Hooked(rclsid: IPointer[CLSID], riid: IPointer[IID], ppv: IPointer[PVOID], 
                         pProxyFileList: IDoublePtr[ProxyFileInfo], pClsid: IPointer[CLSID],
                         pPSFactoryBuffer: IVoidPtr) -> IInteger[HRESULT]:
    print('NdrDllGetClassObject hooked!')
    return E_NOTIMPL

PyObject_CallFunction_address = addressof(pythonapi.PyObject_CallFunction)
PyLong_FromLongLong_address = addressof(pythonapi.PyLong_FromLongLong)
PyLong_AsLong_address = addressof(pythonapi.PyLong_AsLong)
PyObject_CallFunction_format = b'OOOOOO'
PyObject_CallFunction_format_array = create_string_buffer(PyObject_CallFunction_format)
PyObject_CallFunction_format_address = addressof(PyObject_CallFunction_format_array)

context = CImplContext() # create the CIMPL context
function = CImplFunction() # create the CIMPL function
assembly = CImplAssembly() # create the CIMPL assembly

function.instructions = [
    CImplInstruction(
        ['mov []'], CImplInstruction.ASSEMBLY
    )
    CImplInstruction(
        [PyLong_FromLongLong_address], CImplInstruction.INVOKE
    )
    CImplInstruction(
        [], CImplInstruction.INVOKE
    )
]

NdrDllGetClassObject_Hooked = ...

print(hex(id(NdrDllGetClassObject_Hooked)))
print(hex(addressof(NdrDllGetClassObject_Hooked)))

def Patch(library: W_WinDLL):
    library_base = library.handle
    
    dos_header = i_cast2(library_base, PIMAGE_DOS_HEADER).contents
    nt_headers = i_cast2(library_base + dos_header.e_lfanew, PIMAGE_NT_HEADERS64).contents
    
    imports_directory = nt_headers.OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT]
    import_descriptor = i_cast2(imports_directory.VirtualAddress + library_base, PIMAGE_IMPORT_DESCRIPTOR)
    
    while import_descriptor.contents.Name:
        library_name = i_cast2(import_descriptor.contents.Name + library_base, LPCSTR)
        
        if LoadLibraryA(library_name):
            original_first_thunk = i_cast2(library_base + import_descriptor.contents.OriginalFirstThunk, PIMAGE_THUNK_DATA64)
            first_thunk = i_cast2(library_base + import_descriptor.contents.FirstThunk, PIMAGE_THUNK_DATA64)
            
            while original_first_thunk.contents.u1.AddressOfData:
                function_name = i_cast2(library_base + original_first_thunk.contents.u1.AddressOfData, PIMAGE_IMPORT_BY_NAME).contents
                
                if function_name.Name.value == b'NdrDllGetClassObject':
                    oldProtect = DWORD()
                    succeeded = VirtualProtect(PtrUtil.get_address(first_thunk) + first_thunk.contents.u1.offset('Function'),
                                   sizeof(first_thunk.contents.u1.field_type('Function')), PAGE_READWRITE, byref(oldProtect))
                    
                    if not succeeded:
                        raise WinException()
                    
                    first_thunk.contents.u1.Function = addressof(NdrDllGetClassObject_Hooked)
                    break
                    
                original_first_thunk = PtrArithmetic.increment(original_first_thunk)
                first_thunk = PtrArithmetic.increment(first_thunk)
                
        import_descriptor = PtrArithmetic.increment(import_descriptor)
        
actxprxy = COMModule('actxprxy.dll') # for example
Patch(actxprxy)

pv = PVOID()
clsid = CLSID()
iid = IID()

oldProtect = DWORD()
succeeded = VirtualProtect(addressof(NdrDllGetClassObject_Hooked), 1024, PAGE_EXECUTE_READWRITE, byref(oldProtect))
print(succeeded)

def test():
    print(f'actxprxy.dll!DllGetClassObject(NULL, NULL, NULL) => {hex(actxprxy.DllGetClassObject(clsid, iid, byref(pv))&0xffffffff)}')
    
test()