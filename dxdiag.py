"""
/*==========================================================================;
 *
 *  Copyright (C) Microsoft Corporation.  All Rights Reserved.
 *
 *  File:       dxdiag.h
 *  Content:    DirectX Diagnostic Tool include file
 *
 ****************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from .guiddef import CLSID, IID

from .com.autointerfacedef import *

if cpreproc.pragma_once("_DXDIAG_H_"):
    # REGION *** Desktop Family ***

    """
    This identifier is passed to IDxDiagProvider::Initialize in order to ensure that an
    application was built against the correct header files. This number is
    incremented whenever a header (or other) change would require applications
    to be rebuilt. If the version doesn't match, IDxDiagProvider::Initialize will fail.
    (The number itself has no meaning.)
    """
    DXDIAG_DX9_SDK_VERSION = 111

    """
    /****************************************************************************
    *
    * DxDiag Errors
    *
    ****************************************************************************/
    """
    DXDIAG_E_INSUFFICIENT_BUFFER = (0x8007007A)  # HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER)

    """
    /****************************************************************************
    *
    * DxDiag CLSIDs
    *
    ****************************************************************************/
    """

    CLSID_DxDiagProvider = CLSID("{A65B8071-3BFE-4213-9A5B-491DA4461CA7}")

    """
    /****************************************************************************
    *
    * DxDiag Interface IIDs
    *
    ****************************************************************************/
    """

    IID_IDxDiagProvider = IID("{9C6B4CB0-23F8-49CC-A3ED-45A55000A6D2}")

    IID_IDxDiagContainer = IID("{7D0F462F-4064-4862-BC7F-933E5058C10F}")


    """
    /****************************************************************************
    *
    * DxDiag Structures
    *
    ****************************************************************************/
    """

    @CStructure.make
    class DXDIAG_INIT_PARAMS(CStructure):
        dwSize: IDword                # Size of this structure.
        dwDxDiagHeaderVersion: IDword # Pass in DXDIAG_DX9_SDK_VERSION.  This verifies 
                                      # the header and dll are correctly matched.
        bAllowWHQLChecks: IBool64     # If true, allow dxdiag to check if drivers are 
                                      # digital signed as logo'd by WHQL which may
                                      # connect via internet to update WHQL certificates.
        pReserved: IVoidPtr           # Reserved. Must be NULL. 

    """
    /****************************************************************************
    *
    * DxDiag Application Interfaces
    *
    ****************************************************************************/
    """

    class IDxDiagContainer(IUnknown):
        """
        COM definition for IDxDiagContainer
        """
        class VB(IUnknown):
            virtual_table = COMVirtualTable.from_ancestor(IUnknown)
            _iid_ = IID_IDxDiagContainer
            
            @virtual_table.com_function_vbstyle(retval_index=0, retval_type=DWORD,
                                                retval_function=RetVal_GetValue)
            def GetNumberOfChildContainers(self) -> int: ...
            
            @virtual_table.com_function_vbstyle(DWORD, LPWSTR, DWORD)
            def EnumChildContainerNames(self, dwIndex: int, pwszContainer: WT_LPWSTR, cchContainer: int): ...
            
            def _RetVal_GetChildContainer(retval) -> IPointer['IDxDiagContainer']:
                return i_cast2(retval, IDxDiagContainer.PTR()).contents
            
            @virtual_table.com_function_vbstyle(LPCWSTR, retval_index=1, retval_type=PVOID,
                                                retval_function=_RetVal_GetChildContainer)
            def GetChildContainer(self, pwszContainer: WT_LPWSTR) -> 'IDxDiagContainer': ...
            
            @virtual_table.com_function_vbstyle(retval_index=0, retval_type=DWORD,
                                                retval_function=RetVal_GetValue)
            def GetNumberOfProps(self) -> int: ...
            
            @virtual_table.com_function_vbstyle(DWORD, LPWSTR, DWORD)
            def EnumPropNames(self, dwIndex: int, pwszPropName: WT_LPWSTR, cchPropName: int): ...
            
            @virtual_table.com_function_vbstyle(LPCWSTR, retval_index=0, retval_type=VARIANT)
            def GetProp(self, pwszPropName: WT_LPWSTR) -> Any: ...
            
            virtual_table.build()
            
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID_IDxDiagContainer
        
        @virtual_table.com_function(PDWORD)
        def GetNumberOfChildContainers(self, pdwCount: PDWORD) -> int: ...
        
        @virtual_table.com_function(DWORD, LPWSTR, DWORD)
        def EnumChildContainerNames(self, dwIndex: int, pwszContainer: WT_LPWSTR, cchContainer: int) -> int: ...
        
        @virtual_table.com_function(LPCWSTR, PVOID)
        def GetChildContainer(self, pwszContainer: WT_LPWSTR, ppInstance: IDoublePtr['IDxDiagContainer']) -> int: ...
        
        @virtual_table.com_function(PDWORD)
        def GetNumberOfProps(self, pdwCount: PDWORD) -> int: ...
        
        @virtual_table.com_function(DWORD, LPWSTR, DWORD)
        def EnumPropNames(self, dwIndex: int, pwszPropName: WT_LPWSTR, cchPropName: int) -> int: ...
        
        @virtual_table.com_function(LPCWSTR, LPVARIANT)
        def GetProp(self, pwszPropName: WT_LPWSTR, pvarProp: IPointer[VARIANT]) -> int: ...
        
        virtual_table.build()

    class IDxDiagProvider(IUnknown):
        """
        COM definition for IDxDiagProvider
        """
        class VB(IUnknown):
            virtual_table = COMVirtualTable.from_ancestor(IUnknown)
            _iid_ = IID_IDxDiagProvider
            
            @virtual_table.com_function_vbstyle(DXDIAG_INIT_PARAMS.PTR())
            def Initialize(self, pParams: IPointer[DXDIAG_INIT_PARAMS]): ...
            
            @virtual_table.com_function_vbstyle(retval_index=0, retval_type=IDxDiagContainer,
                                                retval_function=RetVal_Dereference)
            def GetRootContainer(self) -> 'IDxDiagContainer': ...
            
            virtual_table.build()
            
        virtual_table = COMVirtualTable.from_ancestor(IUnknown)
        _iid_ = IID_IDxDiagProvider
        
        @virtual_table.com_function(DXDIAG_INIT_PARAMS.PTR())
        def Initialize(self, pParams: IPointer[DXDIAG_INIT_PARAMS]) -> int: ...
        
        @virtual_table.com_function(IDxDiagContainer.DOUBLE_PTR())
        def GetRootContainer(self, ppInstance: IDoublePtr[IDxDiagContainer]) -> int: ...
        
        virtual_table.build()
    
    """
    /****************************************************************************
    *
    * DxDiag Interface Pointer definitions
    *
    ****************************************************************************/
    """

    LPDXDIAGPROVIDER = PDXDIAGPROVIDER = IDxDiagProvider.PTR()

    LPDXDIAGCONTAINER = PDXDIAGCONTAINER = IDxDiagContainer.PTR()

    # REGION ***

    # _DXDIAG_H_