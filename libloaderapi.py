"""
*********************************************************************************
*                                                                               *
* libloaderapi.h -- ApiSet Contract for api-ms-win-core-libraryloader-l1        *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
*********************************************************************************
"""

from . import cpreproc

from .minwindef import *

from .winnt import (PVOID, LANGID, CALLBACK, 
                    LONG_PTR, FARPROC, VOID, 
                    PCSTR, PVOID, PCWSTR, 
                    DLL_DIRECTORY_COOKIE, WINAPI)

from typing import Union
from .defbase import *

if cpreproc.pragma_once("_APISETLIBLOADER_"):
    kernel32 = W_WinDLL("kernel32.dll")
    user32  = W_WinDLL("user32.dll")

    # REGION *** Desktop Family or OneCore Family ***

    FIND_RESOURCE_DIRECTORY_TYPES = (0x0100)
    FIND_RESOURCE_DIRECTORY_NAMES = (0x0200)
    FIND_RESOURCE_DIRECTORY_LANGUAGES = (0x0400)
    RESOURCE_ENUM_LN = (0x0001)
    RESOURCE_ENUM_MUI = (0x0002)
    RESOURCE_ENUM_MUI_SYSTEM = (0x0004)
    RESOURCE_ENUM_VALIDATE = (0x0008)
    RESOURCE_ENUM_MODULE_EXACT = (0x0010)
    SUPPORT_LANG_NUMBER = 32

    class tagENUMUILANG(CStructure):
        _fields_ = [
            ("NumOfEnumUILang", ULONG), # Acutall number of enumerated languages
            ("SizeOfEnumUIBuffer", ULONG), # Buffer size of pMUIEnumUILanguages
            ("pEnumUIBuffer", POINTER(LANGID))
        ]
        
        NumOfEnumUILang: int
        SizeOfEnumUIBuffer: int
        pEnumUIBuffer: IPointer[int]
        
    ENUMUILANG = tagENUMUILANG
    PENUMUILANG = POINTER(ENUMUILANG)

    ENUMRESLANGPROCA = CALLBACK(BOOL, HMODULE, LPCSTR, LPCSTR, WORD, LONG_PTR)
    ENUMRESLANGPROCW = CALLBACK(BOOL, HMODULE, LPCWSTR, LPCWSTR, WORD, LONG_PTR)
    ENUMRESLANGPROC = unicode(ENUMRESLANGPROCW, ENUMRESLANGPROCA)

    ENUMRESNAMEPROCA = CALLBACK(BOOL, HMODULE, LPCSTR, LPSTR, LONG_PTR)
    ENUMRESNAMEPROCW = CALLBACK(BOOL, HMODULE, LPCWSTR, LPWSTR, LONG_PTR)
    ENUMRESNAMEPROC = unicode(ENUMRESNAMEPROCW, ENUMRESNAMEPROCA)

    ENUMRESTYPEPROCA = CALLBACK(BOOL, HMODULE, LPSTR, LONG_PTR)
    ENUMRESTYPEPROCW = CALLBACK(BOOL, HMODULE, LPWSTR, LONG_PTR)
    ENUMRESTYPEPROC = unicode(ENUMRESTYPEPROCW, ENUMRESTYPEPROCA)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    @kernel32.foreign(BOOL, HMODULE, result_function=bool)
    def DisableThreadLibraryCalls(hLibModule: int) -> bool: 
        """
        Disables the DLL_THREAD_ATTACH and DLL_THREAD_DETACH notifications for the specified dynamic-link library (DLL). This can reduce the size of the working set for some applications.
        """

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    @kernel32.foreign(HRSRC, HMODULE, LPCWSTR, LPCWSTR, WORD, name='FindResourceExW')
    def FindResourceEx(hModule: int, lpType: str, lpName: str, wLanguage: int) -> int:
        """
        Determines the location of the resource with the specified type, name, and language in the specified module.
        """
        
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    @kernel32.foreign(INT, DWORD, LPCWSTR, INT, LPCWSTR, INT, BOOL)
    def FindStringOrdinal(dwFindStringOrdinalFlags: int, 
                          lpStringSource: str, 
                          cchSource: int, 
                          pStringValue: str,
                          cchValue: int, 
                          bIgnoreCase: bool) -> int: 
        """
        Locates a Unicode string (wide characters) in another Unicode string for a non-linguistic comparison.
        """
        
    @kernel32.foreign(BOOL, HMODULE, result_function=bool)
    def FreeLibrary(hLibModule: int) -> bool:
        """
        Frees the loaded dynamic-link library (DLL) module and, if necessary, decrements its reference count. When the reference count reaches zero, the module is unloaded from the address space of the calling process and the handle is no longer valid.
        """
        
    @kernel32.foreign(VOID, HMODULE, DWORD)
    def FreeLibraryAndExitThread(hLibModule: int, dwExitCode: int): 
        """
        Decrements the reference count of a loaded dynamic-link library (DLL) by one, then calls ExitThread to terminate the calling thread. The function does not return.
        """

    # REGION ***

    # REGION *** Application Family or OneCore Family ***

    @kernel32.foreign(BOOL, HGLOBAL, result_function=bool)
    def FreeResource(hResData: int) -> bool:
        """
        Decrements (decreases by one) the reference count of a loaded resource. When the reference count reaches zero, the memory occupied by the resource is freed.
        """

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    @kernel32.foreign(DWORD, HMODULE, LPSTR, DWORD)
    def GetModuleFileNameA(hModule: int, lpFilename: bytes, nSize: int) -> int:
        """
        Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.

        To locate the file for a module that was loaded by another process, use the GetModuleFileNameEx function.
        """
        
    @kernel32.foreign(DWORD, HMODULE, LPWSTR, DWORD)
    def GetModuleFileNameW(hModule: int, lpFilename: str, nSize: int) -> int:
        """
        Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.

        To locate the file for a module that was loaded by another process, use the GetModuleFileNameEx function.
        """
        
    def GetModuleFileName(hModule: int, lpFilename: str, nSize: int) -> int:
        """
        Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.

        To locate the file for a module that was loaded by another process, use the GetModuleFileNameEx function.
        """
    
        return GetModuleFileNameW(hModule, lpFilename, nSize)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    @kernel32.foreign(HMODULE, LPCSTR)
    def GetModuleHandleA(lpModuleName: bytes) -> int:
        """
        Retrieves a module handle for the specified module. The module must have been loaded by the calling process.

        To avoid the race conditions described in the Remarks section, use the GetModuleHandleEx function.
        """
        
    @kernel32.foreign(HMODULE, LPCWSTR)
    def GetModuleHandleW(lpModuleName: str) -> int:
        """
        Retrieves a module handle for the specified module. The module must have been loaded by the calling process.

        To avoid the race conditions described in the Remarks section, use the GetModuleHandleEx function.
        """
        
    def GetModuleHandle(lpModuleName: str) -> int:
        """
        Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.

        To locate the file for a module that was loaded by another process, use the GetModuleFileNameEx function.
        """
        
        return GetModuleHandleW(lpModuleName)
        
    GET_MODULE_HANDLE_EX_FLAG_PIN = (0x00000001)
    GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT = (0x00000002)
    GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS = (0x00000004)
    PGET_MODULE_HANDLE_EXA = WINAPI(BOOL, DWORD, LPCSTR, POINTER(HMODULE))
    PGET_MODULE_HANDLE_EXW = WINAPI(BOOL, DWORD, LPCWSTR, POINTER(HMODULE))
    PGET_MODULE_HANDLE_EX = unicode(PGET_MODULE_HANDLE_EXW, PGET_MODULE_HANDLE_EXA)

    @kernel32.foreign(BOOL, DWORD, LPCSTR, POINTER(HMODULE), result_function=bool)
    def GetModuleHandleExA(dwFlags: int, lpModuleName: bytes, phModule: IPointer[int]) -> bool:
        """
        Retrieves a module handle for the specified module and increments the module's reference count unless GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT is specified. The module must have been loaded by the calling process.
        """
        
    @kernel32.foreign(BOOL, DWORD, LPCWSTR, POINTER(HMODULE), result_function=bool)
    def GetModuleHandleExW(dwFlags: int, lpModuleName: str, phModule: IPointer[int]) -> bool:
        """
        Retrieves a module handle for the specified module and increments the module's reference count unless GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT is specified. The module must have been loaded by the calling process.
        """
        
    def GetModuleHandleEx(dwFlags: int, lpModuleName: str, phModule: IPointer[int]) -> int:
        """
        Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.

        To locate the file for a module that was loaded by another process, use the GetModuleFileNameEx function.
        """
        
        return GetModuleFileNameW(dwFlags, lpModuleName, phModule)
    
    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    @kernel32.foreign(FARPROC, HMODULE, LPCSTR, name='GetProcAddress')
    def _GetProcAddress(hModule: int, lpProcName: bytes) -> FARPROC:
        """
        Retrieves the address of an exported function (also known as a procedure) or variable from the specified dynamic-link library (DLL).
        """
        
    def GetProcAddress(hModule: int, lpProcName: Union[str, bytes]) -> FARPROC:
        """
        Retrieves the address of an exported function (also known as a procedure) or variable from the specified dynamic-link library (DLL).
        """
        
        if isinstance(lpProcName, bytes):
            return _GetProcAddress(hModule, lpProcName)
        elif isinstance(lpProcName, str):
            lpProcName = lpProcName.encode()
        else:
            raise TypeError('Procedure name type must be str or bytes.')
        
    CURRENT_IMPORT_REDIRECTION_VERSION = 1

    class _REDIRECTION_FUNCTION_DESCRIPTOR(CStructure):
        _fields_ = [
            ("DllName", PCSTR),
            ("FunctionName", PCSTR),
            ("RedirectionTarget", PVOID)
        ]
        
        DllName: str
        FunctionName: str
        RedirectionTarget: PVOID
        
    REDIRECTION_FUNCTION_DESCRIPTOR = _REDIRECTION_FUNCTION_DESCRIPTOR
    PREDIRECTION_FUNCTION_DESCRIPTOR = POINTER(REDIRECTION_FUNCTION_DESCRIPTOR)
    PCREDIRECTION_FUNCTION_DESCRIPTOR = PREDIRECTION_FUNCTION_DESCRIPTOR

    class _REDIRECTION_DESCRIPTOR(CStructure):
        _fields_ = [
            ("Version", ULONG),
            ("FunctionCount", ULONG),
            ("Redirections", PCREDIRECTION_FUNCTION_DESCRIPTOR)
        ]
        
        Version: int
        FunctionCount: int
        Redirections: IPointer[REDIRECTION_FUNCTION_DESCRIPTOR]
        
    REDIRECTION_DESCRIPTOR = _REDIRECTION_DESCRIPTOR
    PREDIRECTION_DESCRIPTOR = POINTER(REDIRECTION_DESCRIPTOR)
    PCREDIRECTION_DESCRIPTOR = PREDIRECTION_DESCRIPTOR

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    @kernel32.foreign(HMODULE, LPCSTR, HANDLE, DWORD)
    def LoadLibraryExA(lpLibFileName: bytes, hFile: int, dwFlags: int) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.
        """
        
    @kernel32.foreign(HMODULE, LPCWSTR, HANDLE, DWORD)
    def LoadLibraryExW(lpLibFileName: str, hFile: int, dwFlags: int) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.
        """
        
    def LoadLibraryEx(lpLibFileName: str, hFile: int, dwFlags: int) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.
        """
        
        return LoadLibraryExW(lpLibFileName, hFile, dwFlags)
    
    DONT_RESOLVE_DLL_REFERENCES = 0x00000001
    LOAD_LIBRARY_AS_DATAFILE = 0x00000002
    # reserved for internal LOAD_PACKAGED_LIBRARY: 0x00000004
    LOAD_WITH_ALTERED_SEARCH_PATH = 0x00000008
    LOAD_IGNORE_CODE_AUTHZ_LEVEL = 0x00000010
    LOAD_LIBRARY_AS_IMAGE_RESOURCE = 0x00000020
    LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 0x00000040
    LOAD_LIBRARY_REQUIRE_SIGNED_TARGET = 0x00000080
    LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 0x00000100
    LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 0x00000200
    LOAD_LIBRARY_SEARCH_USER_DIRS = 0x00000400
    LOAD_LIBRARY_SEARCH_SYSTEM32 = 0x00000800
    LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 0x00001000
    LOAD_LIBRARY_SAFE_CURRENT_DIRS = 0x00002000
    LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER = 0x00004000
    #
    # For anything building for downlevel, set the flag to be the same as LOAD_LIBRARY_SEARCH_SYSTEM32
    # such that they're treated the same when running on older version of OS.
    #
    LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER = LOAD_LIBRARY_SEARCH_SYSTEM32
    LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY = 0x00008000
    
    @kernel32.foreign(HGLOBAL, HMODULE, HRSRC)
    def LoadResource(hModule: int, hResInfo: int) -> int: 
        """
        Retrieves a handle that can be used to obtain a pointer to the first byte of the specified resource in memory.
        """

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    @user32.foreign(INT, HINSTANCE, UINT, LPSTR, INT)
    def LoadStringA(hInstance: int, uID: int, lpBuffer: bytes, cchBufferMax: int) -> int:
        """
        Loads a string resource from the executable file associated with a specified module and either copies the string into a buffer with a terminating null character or returns a read-only pointer to the string resource itself.
        """
        
    @user32.foreign(INT, HINSTANCE, UINT, LPSTR, INT)
    def LoadStringW(hInstance: int, uID: int, lpBuffer: str, cchBufferMax: int) -> int:
        """
        Loads a string resource from the executable file associated with a specified module and either copies the string into a buffer with a terminating null character or returns a read-only pointer to the string resource itself.
        """
        
    def LoadString(hInstance: int, uID: int, lpBuffer: str, cchBufferMax: int) -> int:
        """
        Loads a string resource from the executable file associated with a specified module and either copies the string into a buffer with a terminating null character or returns a read-only pointer to the string resource itself.
        """
        
        return LoadStringW(hInstance, uID, lpBuffer, cchBufferMax)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    @kernel32.foreign(LPVOID, HGLOBAL)
    def LockResource(hResData: int) -> PVOID:
        """
        Retrieves a pointer to the specified resource in memory.
        """
        
    @kernel32.foreign(DWORD, HMODULE, HRSRC)
    def SizeofResource(hModule: int, hResInfo: int) -> int:
        """
        Retrieves the size, in bytes, of the specified resource.
        """

    # REGION ***

    # REGION *** App Family or OneCore Family ***

    @kernel32.foreign(DLL_DIRECTORY_COOKIE, PCWSTR)
    def AddDllDirectory(NewDirectory: str) -> DLL_DIRECTORY_COOKIE: 
        """
        Adds a directory to the process DLL search path.
        """
        
    @kernel32.foreign(BOOL, DLL_DIRECTORY_COOKIE, result_function=bool)
    def RemoveDllDirectory(Cookie: DLL_DIRECTORY_COOKIE) -> bool:
        """
        Removes a directory that was added to the process DLL search path by using AddDllDirectory.
        """
        
    @kernel32.foreign(BOOL, DWORD, result_function=bool)
    def SetDefaultDllDirectories(DirectoryFlags: int) -> bool:
        """
        Specifies a default set of directories to search when the calling process loads a DLL. This search path is used when LoadLibraryEx is called with no LOAD_LIBRARY_SEARCH flags.
        """

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    @kernel32.foreign(BOOL, HMODULE, LPCSTR, LPCSTR, ENUMRESLANGPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceLanguagesExA(hModule: int, 
                                 lpType: bytes, 
                                 lpName: bytes, 
                                 lpEnumFunc: FARPROC, 
                                 lParam: int, 
                                 dwFlags: int, 
                                 LangId: int) -> bool:
        """
        Enumerates language-specific resources, of the specified type and name, associated with a specified binary module. Extends EnumResourceLanguages by allowing more control over the enumeration.
        """
        
    @kernel32.foreign(BOOL, HMODULE, LPCWSTR, LPCWSTR, ENUMRESLANGPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceLanguagesExW(hModule: int, 
                                 lpType: str, 
                                 lpName: str, 
                                 lpEnumFunc: FARPROC, 
                                 lParam: int, 
                                 dwFlags: int, 
                                 LangId: int) -> bool:
        """
        Enumerates language-specific resources, of the specified type and name, associated with a specified binary module. Extends EnumResourceLanguages by allowing more control over the enumeration.
        """
        
    def EnumResourceLanguagesExA(hModule: int, 
                                 lpType: str, 
                                 lpName: str, 
                                 lpEnumFunc: FARPROC, 
                                 lParam: int, 
                                 dwFlags: int, 
                                 LangId: int) -> bool:
        """
        Enumerates language-specific resources, of the specified type and name, associated with a specified binary module. Extends EnumResourceLanguages by allowing more control over the enumeration.
        """
        return EnumResourceLanguagesExW(hModule, lpType, lpName, lpEnumFunc, lParam, dwFlags, LangId)
    
    @kernel32.foreign(BOOL, HMODULE, LPCSTR, ENUMRESNAMEPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceNamesExA(hModule: int, lpType: bytes, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
    @kernel32.foreign(BOOL, HMODULE, LPCSTR, ENUMRESNAMEPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceNamesExW(hModule: int, lpType: str, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
    def EnumResourceNamesEx(hModule: int, lpType: str, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
        return EnumResourceLanguagesExW(hModule, lpType, lpEnumFunc, lParam)
    
    @kernel32.foreign(BOOL, HMODULE, ENUMRESTYPEPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceTypesExA(hModule: int, lpEnumFunc: FARPROC, lParam: int, dwFlags: int, LangId: int) -> bool: 
        """
        Enumerates resource types associated with a specified binary module. The search can include both a language-neutral Portable Executable file (LN file) and its associated .mui files. Alternately, it can be limited to a single binary module of any type, or to the .mui files associated with a single LN file. The search can also be limited to a single associated .mui file that contains resources for a specific language.

        For each resource type found, **EnumResourceTypesEx** calls an application-defined callback function _lpEnumFunc_, passing the resource type it finds, as well as the various other parameters that were passed to **EnumResourceTypesEx**.
        """
        
    @kernel32.foreign(BOOL, HMODULE, ENUMRESTYPEPROCA, LONG_PTR, DWORD, LANGID, result_function=bool)
    def EnumResourceTypesExW(hModule: int, lpEnumFunc: FARPROC, lParam: int, dwFlags: int, LangId: int) -> bool: 
        """
        Enumerates resource types associated with a specified binary module. The search can include both a language-neutral Portable Executable file (LN file) and its associated .mui files. Alternately, it can be limited to a single binary module of any type, or to the .mui files associated with a single LN file. The search can also be limited to a single associated .mui file that contains resources for a specific language.

        For each resource type found, **EnumResourceTypesEx** calls an application-defined callback function _lpEnumFunc_, passing the resource type it finds, as well as the various other parameters that were passed to **EnumResourceTypesEx**.
        """
        
    def EnumResourceTypesEx(hModule: int, lpEnumFunc: FARPROC, lParam: int, dwFlags: int, LangId: int) -> bool: 
        """
        Enumerates resource types associated with a specified binary module. The search can include both a language-neutral Portable Executable file (LN file) and its associated .mui files. Alternately, it can be limited to a single binary module of any type, or to the .mui files associated with a single LN file. The search can also be limited to a single associated .mui file that contains resources for a specific language.

        For each resource type found, **EnumResourceTypesEx** calls an application-defined callback function _lpEnumFunc_, passing the resource type it finds, as well as the various other parameters that were passed to **EnumResourceTypesEx**.
        """
        return EnumResourceTypesExW(hModule, lpEnumFunc, lParam, dwFlags, LangId)
    
    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    @kernel32.foreign(HRSRC, HMODULE, LPCWSTR, LPCWSTR, name='FindResourceW')
    def FindResource(hModule: int, lpName: str, lpType: str) -> int: 
        """
        Determines the location of a resource with the specified type and name in the specified module.

        To specify a language, use the FindResourceEx function.
        """
        
    @kernel32.foreign(HMODULE, LPCSTR)
    def LoadLibraryA(lpLibFileName: bytes) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.

        For additional load options, use the LoadLibraryEx function.
        """
        
    @kernel32.foreign(HMODULE, LPCWSTR)
    def LoadLibraryW(lpLibFileName: str) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.

        For additional load options, use the LoadLibraryEx function.
        """
        
    def LoadLibrary(lpLibFileName: str) -> int:
        """
        Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.

        For additional load options, use the LoadLibraryEx function.
        """
        
        return LoadLibraryW(lpLibFileName)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    @kernel32.foreign(BOOL, HMODULE, LPCSTR, ENUMRESNAMEPROCA, LONG_PTR, result_function=bool)
    def EnumResourceNamesA(hModule: int, lpType: bytes, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
    @kernel32.foreign(BOOL, HMODULE, LPCWSTR, ENUMRESNAMEPROCA, LONG_PTR, result_function=bool)
    def EnumResourceNamesW(hModule: int, lpType: str, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
    def EnumResourceNames(hModule: int, lpType: str, lpEnumFunc: FARPROC, lParam: int) -> bool:
        """
        Enumerates resources of a specified type within a binary module. For Windows Vista and later, this is typically a language-neutral Portable Executable (LN file), and the enumeration will also include resources from the corresponding language-specific resource files (.mui files) that contain localizable language resources. It is also possible for hModule to specify an .mui file, in which case only that file is searched for resources.
        """
        
        return EnumResourceNamesW(hModule, lpType, lpEnumFunc, lParam)

    # REGION ***