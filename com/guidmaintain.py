from typing import Tuple, Dict, TypeVar
from io import BufferedReader
from .guid import *

T = TypeVar('T')

import shutil
import struct
import os

class _BaseGuidsFile:
    file: BufferedReader
    
    def __init__(self, file_path: str, mode: str):
        self.file = open(file_path, mode)
        
    def end(self):
        if not self.file.closed:
            self.file.close()
    
class _GuidsReader(_BaseGuidsFile):
    def __init__(self, file_path: str):
        super().__init__(file_path, 'rb')

    def read_guid(self) -> GUID:
        try:
            guid = GUID()
            
            guid_size = GUID.size()
            guid_data = self.file.read(guid_size)
            
            if len(guid_data) < guid_size:
                del guid
                return None
            
            memmove(guid.ref(), guid_data, guid_size)
            return guid
        except Exception: return None

    def read_string(self) -> str:
        try:
            length_data = self.file.read(4)
            length = struct.unpack('I', length_data)[0]
            if length == 0:
                return None
            string = self.file.read(length).decode()
        except Exception: return None
        return string
            
class _GuidsWriter(_BaseGuidsFile):
    file: BufferedReader
    
    def __init__(self, file_path: str):
        super().__init__(file_path, 'wb')
        
    def write_guid(self, guid: GUID) -> bool:
        try:
            guid_data = bytes(guid)
            self.file.write(guid_data)
        except Exception: return False
        return True
    
    def write_string(self, string: str) -> bool:
        try:
            length_data = struct.pack('I', len(string))
            string_data = string.encode()
            self.file.write(length_data)
            self.file.write(string_data)
        except Exception: return False
        return True

registry: Dict[str, GUID] = {}

def _SetupFilePathsToCopy() -> Tuple[str, str]:
    guidsPath = _SetupFilePath()
    guidsName, guidsExt = os.path.splitext(guidsPath)
    copyPath = guidsName+'2'+guidsExt
    return guidsPath, copyPath

def _SetupFilePath() -> str:
    dirname = os.path.dirname(__file__)
    datapath = os.path.join(dirname, 'data')
    guidsPath = os.path.join(datapath, 'guids.dat')
    return guidsPath

def _SetupFile(fileType: Type[T]) -> T:
    file = fileType(_SetupFilePath())
    
    return file

def _Initialize():
    global registry
    
    guidsReader = _SetupFile(_GuidsReader)
    
    while True:
        string = guidsReader.read_string()
        if string is None: break
        guid = guidsReader.read_guid()
        if guid is None: break
        registry[string] = guid
        
    guidsReader.end()
    
def _Save():
    global registry
    
    guidsPath, copyPath = _SetupFilePathsToCopy()
    shutil.copy(guidsPath, copyPath)
    guidsWriter = _GuidsWriter(guidsPath)
    
    for guidName, guid in registry.items():
        result = guidsWriter.write_string(guidName)
        if result:
            result = guidsWriter.write_guid(guid)
        if not result:
            try: 
                guidsWriter.end()
            except: ...
            os.remove(guidsPath)
            os.rename(copyPath, guidsPath)
            return
    
    os.remove(copyPath)
    guidsWriter.end()

def NewGuid(guidName: str, force: bool = False) -> GUID:
    global registry
    
    if guidName in registry and not force:
        return registry[guidName]
    
    guid = GUID.new()
    registry[guidName] = guid
    
    _Save()
    
    return guid

_Initialize()