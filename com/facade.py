from ..libloaderapi import *
from .guidmaintain import *
from .interfacedef import *
from ..abs import winregx

DbgHelp = get_win_library('DbgHelp.dll')

@DbgHelp.foreign(PIMAGE_NT_HEADERS, PVOID)
def ImageNtHeader(Base: WT_ADDRLIKE) -> IPointer[IMAGE_NT_HEADERS64 | IMAGE_NT_HEADERS32]: ...

@DbgHelp.foreign(PIMAGE_NT_HEADERS, PVOID)
def ImageNtHeader(Base: WT_ADDRLIKE) -> IPointer[IMAGE_NT_HEADERS64 | IMAGE_NT_HEADERS32]: ...

import winreg
import shutil
import os

def OpenHKCR(SubKey: str, access = winreg.KEY_WRITE, create: bool = True) -> winreg.HKEYType:
    try:
        Key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, SubKey, 0, access)
    except FileNotFoundError as e:
        if create:
            Key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, SubKey)
        else:
            raise e from None
    return Key

class FacadeFactory:
    def Facade(self, ScriptPath: str) -> str:
        if not os.path.isfile(ScriptPath): return None
        ScriptNameW = os.path.splitext(os.path.basename(ScriptPath))[0]
        ScriptName = ScriptNameW.encode('ascii')
        assert len(ScriptName) < 128
        
        FacadeName = os.path.splitext(os.path.basename(ScriptPath))[0] + '.dll'
        FacadeDirectory = os.path.dirname(ScriptPath)
        FacadePath = os.path.join(FacadeDirectory, FacadeName)
        FacadeDLL = os.path.join(os.path.dirname(__file__), 'data\\FacadeDLL.dll')
        
        if os.path.exists(FacadePath):
            os.remove(FacadePath)
            
        shutil.copy(FacadeDLL, FacadePath)
        
        Facade = W_WinDLL(FacadeDLL, winmode=DONT_RESOLVE_DLL_REFERENCES)
        @Facade.foreign(PVOID)
        def InternalScriptNameAddr() -> int: ...
        ScriptNameRVA = InternalScriptNameAddr() - Facade.handle
        section = PIMAGE_SECTION_HEADER()
        ImageRvaToVa(
            ImageNtHeader(Facade.handle), 
            Facade.handle, ScriptNameRVA, 
            byref(section))
        assert section
        ScriptNameRAW = section.contents.PointerToRawData + (ScriptNameRVA - section.contents.VirtualAddress)
        
        with open(FacadePath, 'r+b') as FacadeFile:
            FacadeFile.seek(ScriptNameRAW)
            FacadeFile.write(ScriptName + b'\x00')
        
        return FacadePath
    
    def RegisterCLSID(self, ClsidName: str, ScriptPath: str, 
                      ProgID: Optional[str] = None):
        FacadePath = self.Facade(ScriptPath)
        Clsid = NewClsid(ClsidName)
        ClsidPath = f'CLSID\\{Clsid}'
        with OpenHKCR(ClsidPath) as ClsidKey:
            winreg.SetValue(ClsidKey, None, winreg.REG_SZ, ClsidName)
            with OpenHKCR(f'{ClsidPath}\\InprocServer32') as InprocServer32Key:
                winreg.SetValue(InprocServer32Key, None, winreg.REG_SZ, FacadePath)
                winreg.SetValue(InprocServer32Key, 'ThreadingModel', winreg.REG_SZ, 'Both')
            if ProgID is not None:
                with OpenHKCR(f'{ClsidPath}\\ProgID') as ProgIDKey:
                    winreg.SetValue(ProgIDKey, None, winreg.REG_SZ, ProgID)
                    
    def RegisterInterface(self, Interface: COMInterface):
        NumMethods = len(Interface.virtual_table.VType._fields_)
        
        ItfPath = f'Interface\\{Interface.iid()}'
        with OpenHKCR(ItfPath) as ItfKey:
            winreg.SetValue(ItfKey, None, winreg.REG_SZ, Interface.virtual_table.name)
            with OpenHKCR(f'{ItfPath}\\NumMethods') as NumMethodsKey:
                winreg.SetValue(NumMethodsKey, None, winreg.REG_SZ, str(NumMethods))
                
    def UnregisterCLSID(self, ClsidName: str):
        Clsid = NewClsid(ClsidName)
        ClsidPath = f'CLSID\\{Clsid}'
        winregx.DeleteTree(winreg.HKEY_CLASSES_ROOT, ClsidPath)
                
    def UnregisterInterface(self, onterface: COMInterface):
        winregx.DeleteTree(winreg.HKEY_CLASSES_ROOT, f'Interface\\{interface.iid()}')