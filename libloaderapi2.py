"""
/********************************************************************************
*                                                                               *
* libloaderapi2.h -- ApiSet Contract for api-ms-win-core-libraryloader-l2       *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_APISETLIBLOADER2_"):
    from .minwindef import *
    from .sdkddkver import WIN32_WINNT_WIN8
    kernel32 = get_win_library("kernel32.dll")
    kernelbase = get_win_library("kernelbase.dll")
    
    # REGION *** Application Family or OneCore Family or Games Family ***
    
    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        @kernel32.foreign(HMODULE, LPCWSTR, DWORD)
        def LoadPackagedLibrary(lpwLibFileName: WT_LPWSTR, Reserved: int) -> int: ...
        
    # REGION ***
    
    # REGION *** Application Family or OneCore Family ***
    
    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        @kernelbase.foreign(BOOL, HMODULE, LPCSTR, LPCSTR, DWORD)
        def QueryOptionalDelayLoadedAPI(hParentModule: WT_ADDRLIKE, lpDllName: WT_LPSTR, lpProcName: WT_LPSTR, Reserved: int) -> int: ...
        
    # REGION ***
    
# _APISETLIBLOADER2_