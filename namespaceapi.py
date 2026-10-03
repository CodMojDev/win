"""
/********************************************************************************
*                                                                               *
* namespaceapi.h -- ApiSet Contract for api-ms-win-core-namespace-l1            *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_APISETNAMESPACE_"):
    from .winnt import *
    kernel32 = get_win_library("kernel32.dll")
    
    # REGION *** Desktop Family or OneCore Family ***

    PRIVATE_NAMESPACE_FLAG_DESTROY = 0x00000001
    CreatePrivateNamespaceW = declare(kernel32.CreatePrivateNamespaceW, HANDLE, LPSECURITY_ATTRIBUTES, LPVOID, LPCWSTR)
    OpenPrivateNamespaceW = declare(kernel32.OpenPrivateNamespaceW, HANDLE, LPVOID, LPCWSTR)
    ClosePrivateNamespace = declare(kernel32.ClosePrivateNamespace, BOOLEAN, HANDLE, ULONG)
    CreateBoundaryDescriptorW = declare(kernel32.CreateBoundaryDescriptorW, HANDLE, LPCWSTR, ULONG)
    AddSIDToBoundaryDescriptor = declare(kernel32.AddSIDToBoundaryDescriptor, BOOL, PHANDLE, PSID)
    DeleteBoundaryDescriptor = declare(kernel32.DeleteBoundaryDescriptor, VOID, HANDLE)

    # REGION ***
# _APISETNAMESPACE_