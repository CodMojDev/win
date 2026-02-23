from ..libloaderapi import *
from ..dbg.dbghelp import *
from .guidmaintain import *

import winreg
import shutil
import os

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
    
    def _OpenSubKey(self, SubKey: str) -> winreg.HKEYType:
        try:
            Key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, SubKey, 0, winreg.KEY_WRITE)
        except FileNotFoundError:
            Key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, SubKey)
        return Key
    
    def RegisterCLSID(self, ClsidName: str, ScriptPath: str, 
                      ProgID: Optional[str] = None):
        FacadePath = self.Facade(ScriptPath)
        Clsid = NewClsid(ClsidName)
        ClsidPath = f'CLSID\\{Clsid}'
        with self._OpenSubKey(ClsidPath) as ClsidKey:
            winreg.SetValue(ClsidKey, None, winreg.REG_SZ, ClsidName)
            with self._OpenSubKey(f'{ClsidPath}\\InprocServer32') as InprocServer32Key:
                winreg.SetValue(InprocServer32Key, None, winreg.REG_SZ, FacadePath)
                winreg.SetValue(InprocServer32Key, 'ThreadingModel', winreg.REG_SZ, 'Both')
            if ProgID is not None:
                with self._OpenSubKey(f'{ClsidPath}\\ProgID') as ProgIDKey:
                    winreg.SetValue(ProgIDKey, None, winreg.REG_SZ, ProgID)