from ....defbase_errordef import *
from ....winerror import *
from ...oleauto import *

import winreg

@overload
def LoadTLB(libid: CLSID) -> ITypeLib: ...

@overload
def LoadTLB(lib: COMLibrary) -> ITypeLib:  ...

@overload
def LoadTLB(string: str) -> ITypeLib: ...

def LoadTLB(var) -> ITypeLib:
    if isinstance(var, str):
        pTlb = ITypeLib.NULL()
        
        hr = LoadTypeLibEx(var, REGKIND_NONE, byref(pTlb))
        if FAILED(hr): raise COMError(hr)
        
        return pTlb.contents
    elif isinstance(var, CLSID):
        pTlb = ITypeLib.NULL()
        
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, rf'CLSID\{var}\TypeLib') as key:
            libid = winreg.EnumValue(key, 0)[1]
        
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, rf'CLSID\{var}\Version') as key:
            ver: str = winreg.EnumValue(key, 0)[1]
            ver_components = ver.split('.')
            
        major, minor, *_ = ver_components
        major, minor = int(major), int(minor)
        
        hr = LoadRegTypeLib(CLSID(libid), major, minor, 0, byref(pTlb))
        if FAILED(hr): raise COMError(hr)
        
        return pTlb.contents
    elif isinstance(var, COMLibrary):
        pTlb = ITypeLib.NULL()
        
        version = var.version()
        if isinstance(version, (list, tuple)):
            major, minor, *_ = version
        elif isinstance(version, str):
            major, minor, *_ = version.split('.')
            major, minor = int(major), int(minor)
        else:
            raise TypeError(f'Not supported version type: {version!r}')
            
        hr = LoadRegTypeLib(var.libid(), major, minor, 0, byref(pTlb))
        if FAILED(hr): raise COMError(hr)
        
        return pTlb.contents
    else:
        raise TypeError(f'Not supported type for loading TLB: {var!r}')
    
def GetTLBName(tlb: ITypeLib) -> str:
    bszTlbName = BSTR()
    hr = tlb.GetDocumentation(-1, byref(bszTlbName), NULL, NULL, NULL)
    if FAILED(hr): raise COMError(hr)
    
    tlbName = bszTlbName.value
    SysFreeString(bszTlbName)
    
    return tlbName

def GetTLBPath(tlb: ITypeLib) -> str:
    pLibAttr = TLIBATTR.NULL()
    hr = tlb.GetLibAttr(byref(pLibAttr))
    if FAILED(hr): raise COMError(hr)
    
    libAttr = pLibAttr.contents
    bstrPathName = BSTR()
    
    hr = QueryPathOfRegTypeLib(libAttr.guid, libAttr.wMajorVerNum, libAttr.wMinorVerNum, 
                               libAttr.lcid, byref(bstrPathName))
    if FAILED(hr): raise COMError(hr)
    
    tlb.ReleaseTLibAttr(pLibAttr)
    pathName = bstrPathName.value
    SysFreeString(bstrPathName)
    
    return pathName