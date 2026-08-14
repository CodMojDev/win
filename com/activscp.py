from .autointerfacedef import *

CATID_ActiveScript = GUID.string("{F0B7A1A1-9847-11cf-8F20-00805F2CD064}")
CATID_ActiveScriptParse = GUID.string("{F0B7A1A2-9847-11cf-8F20-00805F2CD064}")
CATID_ActiveScriptEncode = GUID.string("{F0B7A1A3-9847-11cf-8F20-00805F2CD064}")

IID_IActiveScript = IID.string("{BB1A2AE1-A4F9-11cf-8F20-00805F2CD064}")
IID_IActiveScriptParse32 = IID.string("{BB1A2AE2-A4F9-11cf-8F20-00805F2CD064}")
IID_IActiveScriptParse64 = IID.string("{C7EF7658-E1EE-480E-97EA-D52CB4D76D17}")
IID_IActiveScriptEncode = IID.string("{BB1A2AE3-A4F9-11cf-8F20-00805F2CD064}")
IID_IActiveScriptHostEncode = IID.string("{BEE9B76E-CFE3-11d1-B747-00C04FC2B085}")
IID_IActiveScriptParseProcedureOld32 = IID.string("{1CFF0050-6FDD-11d0-9328-00A0C90DCAA9}")
IID_IActiveScriptParseProcedureOld64 = IID.string("{21F57128-08C9-4638-BA12-22D15D88DC5C}")
IID_IActiveScriptParseProcedure32 = IID.string("{AA5B6A80-B834-11d0-932F-00A0C90DCAA9}")
IID_IActiveScriptParseProcedure64 = IID.string("{C64713B6-E029-4CC5-9200-438B72890B6A}")
IID_IActiveScriptParseProcedure2_32 = IID.string("{71EE5B20-FB04-11d1-B3A8-00A0C911E8B2}")
IID_IActiveScriptParseProcedure2_64 = IID.string("{FE7C4271-210C-448D-9F54-76DAB7047B28}")
IID_IActiveScriptSite = IID.string("{DB01A1E3-A42B-11cf-8F20-00805F2CD064}")
IID_IActiveScriptSiteTraceInfo = IID.string("{4B7272AE-1955-4bfe-98B0-780621888569}")
IID_IActiveScriptSiteWindow = IID.string("{D10F6761-83E9-11cf-8F20-00805F2CD064}")
IID_IActiveScriptSiteInterruptPoll = IID.string("{539698A0-CDCA-11CF-A5EB-00AA0047A063}")
IID_IActiveScriptSiteUIControl = IID.string("{AEDAE97E-D7EE-4796-B960-7F092AE844AB}")
IID_IActiveScriptError = IID.string("{EAE1BA61-A4ED-11cf-8F20-00805F2CD064}")
IID_IActiveScriptError64 = IID.string("{B21FB2A1-5B8F-4963-8C21-21450F84ED7F}")
IID_IBindEventHandler = IID.string("{63CDBCB0-C1B1-11d0-9336-00A0C90DCAA9}")
IID_IActiveScriptStats = IID.string("{B8DA6310-E19B-11d0-933C-00A0C90DCAA9}")
IID_IActiveScriptProperty = IID.string("{4954E0D0-FBC7-11D1-8410-006008C3FBFC}")
IID_ITridentEventSink = IID.string("{1DC9CA50-06EF-11d2-8415-006008C3FBFC}")
IID_IActiveScriptGarbageCollector = IID.string("{6AA2C4A0-2B53-11d4-A2A0-00104BD35090}")
IID_IActiveScriptSIPInfo = IID.string("{764651D0-38DE-11d4-A2A3-00104BD35090}")
IID_IActiveScriptTraceInfo = IID.string("{C35456E7-BEBF-4a1b-86A9-24D56BE8B369}")

OID_VBSSIP = GUID.string("{1629F04E-2799-4db5-8FE5-ACE10F17EBAB}")
OID_JSSIP = GUID.string("{06C9E010-38CE-11d4-A2A3-00104BD35090}")
OID_WSFSIP = GUID.string("{1A610570-38CE-11d4-A2A3-00104BD35090}")

IID_IActiveScriptStringCompare = IID.string("{58562769-ED52-42f7-8403-4963514E1F11}")

SCRIPTITEM_ISVISIBLE = 0x0002
SCRIPTITEM_ISSOURCE = 0x0004
SCRIPTITEM_GLOBALMEMBERS = 0x0008
SCRIPTITEM_ISPERSISTENT = 0x0040
SCRIPTITEM_CODEONLY = 0x0200
SCRIPTITEM_NOCODE = 0x0400
SCRIPTITEM_ALL_FLAGS = (SCRIPTITEM_ISSOURCE | SCRIPTITEM_ISVISIBLE | SCRIPTITEM_ISPERSISTENT | SCRIPTITEM_CODEONLY | SCRIPTITEM_NOCODE)

SCRIPT_ENCODE_SECTION         = 0x0000000
SCRIPT_ENCODE_DEFAULT_LANGUAGE        = 0x0000000
SCRIPT_ENCODE_NO_ASP_LANGUAGE         = 0x0000000

SCRIPTTYPELIB_ISCONTROL         0x00000010
SCRIPTTYPELIB_ISPERSISTENT      0x00000040
SCRIPTTYPELIB_ALL_FLAGS         (SCRIPTTYPELIB_ISCONTROL | SCRIPTTYPELIB_ISPERSISTENT)

SCRIPTTEXT_DELAYEXECUTION       = 0x00000001
SCRIPTTEXT_ISVISIBLE            = 0x00000002
SCRIPTTEXT_ISEXPRESSION         = 0x00000020
SCRIPTTEXT_ISPERSISTENT         = 0x00000040
SCRIPTTEXT_HOSTMANAGESSOURCE    = 0x00000080
SCRIPTTEXT_ISXDOMAIN            = 0x00000100
SCRIPTTEXT_ISNONUSERCODE        = 0x00000200
SCRIPTTEXT_ALL_FLAGS            = (SCRIPTTEXT_DELAYEXECUTION | \
                                   SCRIPTTEXT_ISVISIBLE | \
                                   SCRIPTTEXT_ISEXPRESSION | \
                                   SCRIPTTEXT_ISPERSISTENT | \
                                   SCRIPTTEXT_HOSTMANAGESSOURCE | \
                                   SCRIPTTEXT_ISXDOMAIN | \
                                   SCRIPTTEXT_ISNONUSERCODE)

SCRIPTPROC_ISEXPRESSION         = 0x00000020
SCRIPTPROC_HOSTMANAGESSOURCE    = 0x00000080
SCRIPTPROC_IMPLICIT_THIS        = 0x00000100
SCRIPTPROC_IMPLICIT_PARENTS     = 0x00000200
SCRIPTPROC_ISXDOMAIN            = 0x00000400
SCRIPTPROC_ALL_FLAGS            = SCRIPTPROC_HOSTMANAGESSOURCE | \
                                  SCRIPTPROC_ISEXPRESSION | \
                                  SCRIPTPROC_IMPLICIT_THIS | \
                                  SCRIPTPROC_IMPLICIT_PARENTS | \
                                  SCRIPTPROC_ISXDOMAIN

SCRIPTINFO_IUNKNOWN             = 0x00000001
SCRIPTINFO_ITYPEINFO            = 0x00000002
SCRIPTINFO_ALL_FLAGS            = (SCRIPTINFO_IUNKNOWN | \
                                   SCRIPTINFO_ITYPEINFO)

SCRIPTINTERRUPT_DEBUG           = 0x00000001
SCRIPTINTERRUPT_RAISEEXCEPTION  = 0x00000002
SCRIPTINTERRUPT_ALL_FLAGS       = (SCRIPTINTERRUPT_DEBUG | \
                                   SCRIPTINTERRUPT_RAISEEXCEPTION)

SCRIPTSTAT_STATEMENT_COUNT  = 1
SCRIPTSTAT_INSTRUCTION_COUNT = 2  
SCRIPTSTAT_INTSTRUCTION_TIME = 3 
SCRIPTSTAT_TOTAL_TIME = 4  

SCRIPTPROP_NAME = 0x00000000
SCRIPTPROP_MAJORVERSION = 0x00000001
SCRIPTPROP_MINORVERSION = 0x00000002
SCRIPTPROP_BUILDNUMBER = 0x00000003
SCRIPTPROP_DELAYEDEVENTSINKING = 0x00001000
SCRIPTPROP_CATCHEXCEPTION = 0x00001001
SCRIPTPROP_CONVERSIONLCID = 0x00001002
SCRIPTPROP_HOSTSTACKREQUIRED = 0x00001003
SCRIPTPROP_SCRIPTSAREFULLYTRUSTED = 0x00001004
SCRIPTPROP_DEBUGGER = 0x00001100
SCRIPTPROP_JITDEBUG = 0x00001101
SCRIPTPROP_GCCONTROLSOFTCLOSE = 0x00002000
SCRIPTPROP_INTEGERMODE = 0x00003000
SCRIPTPROP_STRINGCOMPAREINSTANCE = 0x00003001
SCRIPTPROP_INVOKEVERSIONING = 0x00004000
SCRIPTPROP_HACK_FIBERSUPPORT = 0x70000000
SCRIPTPROP_HACK_TRIDENTEVENTSINK = 0x70000001
SCRIPTPROP_ABBREVIATE_GLOBALNAME_RESOLUTION = 0x70000002
SCRIPTPROP_HOSTKEEPALIVE = 0x70000004

SCRIPT_E_RECORDED = HRESULT(0x86664004).value
SCRIPT_E_REPORTED = HRESULT(0x80020101).value
SCRIPT_E_PROPAGATE = HRESULT(0x80020102).value

SCRIPTLANGUAGEVERSION_DEFAULT = 0
SCRIPTLANGUAGEVERSION_5_7 = 1
SCRIPTLANGUAGEVERSION_5_8 = 2
SCRIPTLANGUAGEVERSION_MAX = 255
SCRIPTLANGUAGEVERSION = INT

SCRIPTSTATE_UNINITIALIZED = 0
SCRIPTSTATE_INITIALIZED = 5
SCRIPTSTATE_STARTED = 1
SCRIPTSTATE_CONNECTED = 2
SCRIPTSTATE_DISCONNECTED = 3
SCRIPTSTATE_CLOSED = 4
SCRIPTSTATE = INT

SCRIPTTRACEINFO_SCRIPTSTART = 0
SCRIPTTRACEINFO_SCRIPTEND = 1
SCRIPTTRACEINFO_COMCALLSTART = 2
SCRIPTTRACEINFO_COMCALLEND = 3
SCRIPTTRACEINFO_CREATEOBJSTART = 4
SCRIPTTRACEINFO_CREATEOBJEND = 5
SCRIPTTRACEINFO_GETOBJSTART = 6
SCRIPTTRACEINFO_GETOBJEND = 7
SCRIPTTRACEINFO = INT

SCRIPTTHREADSTATE_NOTINSCRIPT = 0
SCRIPTTHREADSTATE_RUNNING = 1
SCRIPTTHREADSTATE = INT

SCRIPTGCTYPE_NORMAL = 0
SCRIPTGCTYPE_EXHAUSTIVE = 1
SCRIPTGCTYPE = INT

SCRIPTUICITEM_INPUTBOX = 1
SCRIPTUICITEM_MSGBOX = 2
SCRIPTUICITEM = INT

SCRIPTUICHANDLING_ALLOW = 0
SCRIPTUICHANDLING_NOUIERROR = 1
SCRIPTUICHANDLING_NOUIDEFAULT = 2
SCRIPTUICHANDLING = INT

SCRIPTTHREADID = DWORD
SCRIPTTHREADID_CURRENT = SCRIPTTHREADID(-1).value
SCRIPTTHREADID_BASE = SCRIPTTHREADID(-1).value
SCRIPTTHREADID_ALL = SCRIPTTHREADID(-1).value

class IActiveScriptError(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScriptError
    
    @virtual_table.com_function(LPEXCEPINFO)
    def GetExceptionInfo(self, pexcepinfo: IPointer[EXCEPINFO]) -> int: ...
    
    @virtual_table.com_function(PDWORD, PULONG, PLONG)
    def GetSourcePosition(self, pdwSourceContext: IPointer[DWORD], pulLineNumber: IPointer[ULONG], plCharacterPosition: IPointer[LONG]) -> int: ...
    
    @virtual_table.com_function(LPBSTR)
    def GetSourceLineText(self, pbstrSourceLine: IPointer[BSTR]) -> int: ...
    
    virtual_table.build()

class IActiveScriptSite(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScriptSite
    
    @virtual_table.com_function(PTR(LCID))
    def GetLCID(self, plcid: IPointer[LCID]) -> int: ...
    
    @virtual_table.com_function(LPCOLESTR, DWORD, PTR(LPUNKNOWN), PTR(LPTYPEINFO))
    def GetItemInfo(self, pstrName: LPCOLESTR, dwReturnMask: int, ppiunkItem:: IDoublePtr[IUnknown], ppti: IDoublePtr[ITypeInfo]) -> int: ...
    
    @virtual_table.com_function(LPBSTR)
    def GetDocVersionString(self, pbstrVersion: IPointer[BSTR]) -> int: ...
    
    @virtual_table.com_function(LPVARIANT, LPEXCEPINFO)
    def OnScriptTerminate(self, pvarResult: IPointer[VARIANT], pexcepinfo: IPointer[EXCEPINFO]) -> int: ...
    
    @virtual_table.com_function(SCRIPTSTATE)
    def OnStateChange(self, ssScriptState: int) -> int: ...
    
    @virtual_table.com_function(IActiveScriptError.PTR())
    def OnScriptError(self, pscripterror: IPointer[IActiveScriptError]) -> int: ...
    
    @virtual_table.com_function()
    def OnEnterScript(self) -> int: ...
    
    @virtual_table.com_function()
    def OnLeaveScript(self) -> int: ...
    
    virtual_table.build()
    
class IActiveScriptSiteWindow(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScriptSiteWindow
    
    @virtual_table.com_function(PHWND)
    def GetWindow(self, phwnd: IPointer[HWND]) -> int: ...
    
    @virtual_table.com_function(BOOL)
    def EnableModeless(self, fEnable: int) -> int: ...
    
    virtual_table.build()
    
class IActiveScriptSiteUOControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScriptSiteUIControl
    
    @virtual_table.com_function(SCRIPTUICITEM, PTR(SCRIPTUICHANDLING))
    def GetUIBehavior(self, UicItem: int, pUicHandling: IPointer[SCRIPTUICHANDLING]) -> int: ...
    
    virtual_table.build()
    
class IActiveScriptSiteInterruptPoll(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScriptSiteInterruptPoll
    
    @virtual_table.com_function()
    def QueryContinue(self) -> int: ...
    
    virtual_table.build()

IActiveScript_MSHL = DelayedMarshaller()

class IActiveScript(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID_IActiveScript
    
    @virtual_table.com_function(IActiveScriptSite.PTR())
    def SetScriptSite(self, pSite: IPointer[IActiveScriptSite]) -> int: ...
    
    @virtual_table.com_function(REFIID, PVOID, intermediate_method=True, marshal_scheme=[(0, RetVal_Dereference)])
    def GetScriptSite(self, riid: IID, ppvObject: IDoublePtr, **kwargs) -> int:
        return self.virt_delegate(riid.ref(), ppvObject)
    
    @virtual_table.com_function(SCRIPTSTATE)
    def SetScriptState(self, ss: int) -> int: ...
    
    @virtual_table.com_function(PTR(SCRIPTSTATE))
    def GetScriptState(self, pssState: IPointer[SCRIPTSTATE]) -> int: ...
    
    @virtual_table.com_function()
    def Close(self) -> int: ...
    
    @virtual_table.com_function(LPCOLESTR, DWORD)
    def AddNamedItem(self, pstrName: LPCOLESTR, dwFlags: int) -> int: ...
    
    @virtual_table.com_function(REFGUID, DWORD, DWORD, DWORD, marshal_scheme=[(0, RetVal_Dereference)], intermediate_method=True)
    def AddTypeLib(self, rguidTypeLib: GUID, dwMajor: int, dwMinor: int, dwFlags: int, **kwargs) -> int:
        return self.virt_delegate(rguidTypeLib.ref(), dwMajor, dwMinor, dwFlags)
    
    @virtual_table.com_function(LPCOLESTR, PTR(LPDISPATCH))
    def GetScriptDispatch(self, pstrItemName: LPCOLESTR, ppdisp: IDoublePtr[IDispatch]) -> int: ...
    
    @virtual_table.com_function(DWORD, PTR(SCRIPTTHREADID))
    def GetCurrentScriptThreadID(self, pstidThread: IPointer[SCRIPTTHREADID]) -> int: ...
    
    @virtual_table.com_function(SCRIPTTHREADID, PTR(SCRIPTTHREADSTATE))
    def GetScriptThreadState(self, stidThread: int, pstsState: IPointer[SCRIPTTHREADSTATE]) -> int: ...
    
    @virtual_table.com_function(SCRIPTTHREADID, LPEXCEPINFO, DWORD)
    def InterruptScriptThread(self, stidThread: int, pexcepinfo: IPointer[EXCEPINFO], dwFlags: int) -> int: ...
    
    @virtual_table.com_function(PVOID, marshal_scheme=[(0, IActiveScript_MSHL)])
    def Clone(self, ppscript: IDoublePtr['IActiveScript']) -> int: ...
    
    virtual_table.build()
    
IActiveScript_MSHL.marshal_func = lambda x: i_cast(x, IActiveScript.PTR())

