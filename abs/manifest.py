from .core.controllable import *
from win.defbase_errordef import *
from win.handleapi import INVALID_HANDLE_VALUE

import time
import os

kernel32 = get_win_library('kernel32.dll')

class ACTCTXW(CStructure):
    _fields_ = [
        ('cbSize', ULONG),
        ('dwFlags', DWORD),
        ('lpSource', LPCWSTR),
        ('wProcessorArchitecture', WORD),
        ('wLangId', LANGID),
        ('lpAssemblyDirectory', LPCWSTR),
        ('lpResourceName', LPCWSTR),
        ('lpApplicationName', LPCWSTR),
        ('hModule', HMODULE)
    ]
    cbSize: int
    dwFlags: int
    lpSource: LPCWSTR
    wProcessorArchitecture: int
    wLangId: int
    lpAssemblyDirectory: LPCWSTR
    lpResourceName: LPCWSTR
    lpApplicationName: LPCWSTR
    hModule: int

PCACTCTXW = PACTCTXW = PTR(ACTCTXW)

@kernel32.foreign(BOOL, DWORD, ULONG_PTR)
def DeactivateActCtx(dwFlags: int, ulCookie: int) -> int: ...

@kernel32.foreign(BOOL, HANDLE, PULONG_PTR)
def ActivateActCtx(hActCtx: int, lpCookie: IPointer[ULONG_PTR]) -> int: ...

@kernel32.foreign(HANDLE, PCACTCTXW)
def CreateActCtxW(pActCtx: IPointer[ACTCTXW]) -> int: ...

@kernel32.foreign(VOID, HANDLE)
def ReleaseActCtx(hActCtx: int): ...

ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID = 1
ACTCTX_FLAG_LANGID_VALID = 2
ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID = 4
ACTCTX_FLAG_RESOURCE_NAME_VALID = 8
ACTCTX_FLAG_SET_PROCESS_DEFAULT = 16
ACTCTX_FLAG_APPLICATION_NAME_VALID = 32
ACTCTX_FLAG_HMODULE_VALID = 128

class ActivationContext(Handle):
    """
    The SxS activation context.
    """
    
    class ActiveActivationContext(ControllableValue, ULONG_PTR):
        """
        The active SxS activation context.
        """
        
        def close(self):
            DeactivateActCtx(0, self)
            self._closed = True
    
    @classmethod
    def create(self, source: str | None = None, lang_id: int | None = None,
               architecture: int | None = None, assembly_directory: str | None = None,
               resource_name: str | None = None, module: int | None = None,
               application_name: str | None = None, process_default: bool = False):
        ac = ACTCTXW()
        ac.cbSize = ac.size()
        flags = 0
        if source is not None:
            ac.lpSource = source
        if lang_id is not None:
            ac.wLangId = lang_id
            flags |= ACTCTX_FLAG_LANGID_VALID
        if architecture is not None:
            ac.wProcessorArchitecture = architecture
            flags |= ACTCTX_FLAG_PROCESSOR_ARCHITECTURE_VALID
        if assembly_directory is not None:
            ac.lpAssemblyDirectory = assembly_directory
            flags |= ACTCTX_FLAG_ASSEMBLY_DIRECTORY_VALID
        if application_name is not None:
            ac.lpApplicationName = application_name
            flags |= ACTCTX_FLAG_APPLICATION_NAME_VALID
        if module is not None:
            ac.hModule = module
            flags |= ACTCTX_FLAG_HMODULE_VALID
        if resource_name is not None:
            ac.lpResourceName = resource_name
            flags |= ACTCTX_FLAG_RESOURCE_NAME_VALID
        if process_default:
            flags |= ACTCTX_FLAG_SET_PROCESS_DEFAULT
        ac.dwFlags = flags
        ctx = ActivationContext(CreateActCtxW(ac.ref()))
        if ctx.invalid(): raise WinException()
        return ctx
    
    def activate(self) -> ActiveActivationContext:
        """
        Activate the activation context.
        """
        ulpCookie = ULONG_PTR()
        if not ActivateActCtx(self, byref(ulpCookie)):
            raise WinException()
        return ActivationContext.ActiveActivationContext(ulpCookie.value)
    
    def close(self):
        ReleaseActCtx(self)
        self._closed = True
        
    def invalid(self) -> bool:
        return self.value == INVALID_HANDLE_VALUE

class Manifest:
    """
    The SxS manifest object class.
    """
    
    class XMLNode:
        """
        Class, representing XML node.
        """
        
        data: str | list['Manifest.XMLNode'] | None
        tag: str
        indentation: int
        attributes: dict
        
        def __init__(self, tag: str, data: str | Iterable['Manifest.XMLNode'] | None = None, attributes: dict = {}):
            if not isinstance(data, str) and data is not None:
                data = list(data)
            self.data = data
            self.tag = tag
            self.indentation = 0
            self.attributes = attributes
            
        def __str__(self) -> str:
            indents = '    ' * self.indentation
            attributes = ' '.join([f'{k}="{v}"' for k, v in self.attributes.items()])
            if attributes: attributes = ' ' + attributes
            if self.data is None:
                return f'\n{indents}<{self.tag}{attributes} />'
            if isinstance(self.data, str):
                return f'\n{indents}<{self.tag}{attributes}>{self.data}</{self.tag}>'
            data = ''
            for node in self.data:
                node.indentation = self.indentation + 1
                data += str(node)
            data += '\n'
            return f'\n{indents}<{self.tag}{attributes}>{data}{indents}</{self.tag}>'
    
        def find(self, tag: str) -> TUnion['Manifest.XMLNode', None]:
            """
            Find the tag in XML node.
            """
            for node in self.data:
                if node.tag == tag:
                    return node
            return None
    
        def find_all(self, tag: str) -> list[TUnion['Manifest.XMLNode', None]]:
            """
            Find all the tags in XML node.
            """
            result = []
            for node in self.data:
                if node.tag == tag:
                    result.append(tag)
            return result
        
        def delete(self, tag: str):
            """
            Delete the XML node.
            """
            for i, node in enumerate(self.data):
                if node.tag == tag:
                    self.data.pop(i)
                    return
    
    file_name: str
    root: XMLNode
    
    def __init__(self):
        st = time.localtime()
        self.file_name = os.path.expandvars(f'%TEMP%\\WinAbs-Manifest-{st.tm_year}-{st.tm_mon}-{st.tm_mday}.{st.tm_hour}-{st.tm_min}-{st.tm_sec}.xml')
        self.root = Manifest.XMLNode('assembly', [], {'xmlns': 'urn:schemas-microsoft-com:asm.v1', 'manifestVersion': '1.0'})
    
    def save(self):
        """
        Save the manifest to file.
        """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
            file.write(str(self.root))
    
    @property
    def description(self) -> str:
        node = self.root.find('description')
        return '' if node is None else node.data
    
    @description.setter
    def description(self, description: str):
        node = self.root.find('description')
        if node is None:
            node = Manifest.XMLNode('description', description)
            self.root.data.append(node)
        else:
            node.data = description
        
    def identity(self, version: str, name: str, architecture: str = '*', type: str = 'win32'):
        """
        Set the identity of the manifest.
        """
        attributes = {'version': version, 'processorArchitecture': architecture, 'name': name, 'type': type}
        node = self.root.find('assemblyIdentity')
        if node is None:
            node = Manifest.XMLNode('assemblyIdentity', None, attributes)
            self.root.data.append(node)
        else:
            node.attributes = attributes
        
    def dependency(self, name: str, version: str, architecture: str = '*', token: str = '0000000000000000', type: str = 'win32', language: str = '*'):
        """
        Add dependency to the manifest.
        """
        attributes = {'type': type, 'name': name, 'version': version, 'processorArchitecture': architecture, 'publicKeyToken': token, 'language': language}
        node = Manifest.XMLNode('dependency', [Manifest.XMLNode('dependentAssembly', [Manifest.XMLNode('assemblyIdentity', None, attributes)])])
        self.root.data.append(node)
        
    @property
    def dpi_aware(self) -> bool:
        application = self.root.find('application')
        if application is None: return False
        windowsSettings = application.find('windowsSettings')
        if windowsSettings is None: return False
        return windowsSettings.find('dpiAware') is not None
    
    @dpi_aware.setter
    def dpi_aware(self, dpi_aware: bool):
        application = self.root.find('application')
        if application is None:
            application = Manifest.XMLNode('application', [], {'xmlns': 'urn:schemas-microsoft-com:asm.v3'})
            self.root.data.append(application)
        windowsSettings = application.find('windowsSettings')
        if windowsSettings is None:
            windowsSettings = Manifest.XMLNode('windowsSettings', [])
            application.data.append(windowsSettings)
        dpiAware = windowsSettings.find('dpiAware')
        if dpiAware is None:
            dpiAware = Manifest.XMLNode('dpiAware', 'true' if dpi_aware else 'false', {'xmlns': 'http://schemas.microsoft.com/SMI/2005/WindowsSettings'})
            windowsSettings.data.append(dpiAware)
        else:
            windowsSettings.data = 'true' if dpi_aware else 'false'
            
    def apply(self) -> ActivationContext:
        """
        Apply the manifest to activation context.
        """
        return ActivationContext.create(source=self.file_name)
    
    def __del__(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)