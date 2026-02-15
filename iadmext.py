"""
    iadmext.h

    This module contains the interface for extensions to the IISADMIN service.


    FILE HISTORY:
    7/8/97      michth      created

/**********************************************************************/
/**                       Microsoft Windows NT                       **/
/**                Copyright(c) Microsoft Corp., 1997-1999           **/
/**********************************************************************/

"""

from . import cpreproc

if cpreproc.pragma_once("__iadmext_h__"):
    # REGION *** Desktop Family ***

    # header files for imported files
    from .com.unknwn import *
    from .winnt import TEXT
    from .guiddef import *
    from .iiscnfg import *

    # The Main Interface. All extensions must support this interface.
    # {51DFE970-F6F2-11d0-B9BD-00A0C922E750}
    IID_IADMEXT = IID("{51DFE970-F6F2-11d0-B9BD-00A0C922E750}")

    # InProcess COM Registration. All extensions must write a subkey name by the
    # CLSID for the above interface under this key in the Registry.
    IISADMIN_EXTENSIONS_REG_KEYA         = "SOFTWARE\\Microsoft\\InetStp\\Extensions"
    IISADMIN_EXTENSIONS_REG_KEYW         = u"SOFTWARE\\Microsoft\\InetStp\\Extensions"
    IISADMIN_EXTENSIONS_REG_KEY          = TEXT("SOFTWARE\\Microsoft\\InetStp\\Extensions")

    """
    DCOM Registration. CLSIDS for the DCOM interface provided by these extensions will
    be written to this key and ID by IISADMIN as a multisz property.

    This is intended for use by other applications which need to find out what classid's are
    registered.
    """

    IISADMIN_EXTENSIONS_CLSID_MD_KEYA     = "LM/IISADMIN/EXTENSIONS/DCOMCLSIDS"
    IISADMIN_EXTENSIONS_CLSID_MD_KEYW     = u"LM/IISADMIN/EXTENSIONS/DCOMCLSIDS"
    IISADMIN_EXTENSIONS_CLSID_MD_KEY      = TEXT("LM/IISADMIN/EXTENSIONS/DCOMCLSIDS")
    IISADMIN_EXTENSIONS_CLSID_MD_ID       = MD_IISADMIN_EXTENSIONS

    if cpreproc.pragma_once("__IADMEXT_INTERFACE_DEFINED__"):
        class IADMEXT(IUnknown):
            virtual_table = COMVirtualTable.from_ancestor(IUnknown)
            _iid_ = IID_IADMEXT
            
            #
            # All methods below will be called under a thread which has called
            # CoInitializeEx(NULL, COINIT_MULTITHREADED).
            #
            # The IMSAdminBase Object will be available during all of these calls.
            #
            
            @virtual_table.com_function()
            def Initialize(self) -> int:
                """
                Initialize will be called by IISADMIN when it initializes.
                """
                
            @virtual_table.com_function(LPCLSID, DWORD)
            def EnumDcomCLSIDs(self, pclsidDcom: IPointer[CLSID], dwEnumIndex: int) -> int:
                """
                EnumDcomCLSIDs will be called by IISADMIN when it initializes,
                and the returned CLSIDs will be written to the metabase at
                the path IISADMIN_EXTENSIONS_CLSID_MD_KEY.
                """
                
            @virtual_table.com_function()
            def Terminate(self) -> int:
                """
                Terminate will be called by IISADMIN when it terminates.
                """
            
            virtual_table.build()
        
    # __IADMEXT_INTERFACE_DEFINED__
    
    # REGION ***

# __iadmext_h__