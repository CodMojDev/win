#
# ole.py
#

#### NO IMPLEMENTATION
if False:
    from .oleidl import *

    class OLETARGETDEVICE(CStructure):
        _fields_ = [
            ('otdDeviceNameOffset', USHORT),
            ('otdDriverNameOffset', USHORT),
            ('otdPortNameOffset', USHORT),
            ('otdExtDevmodeOffset', USHORT),
            ('otdExtDevmodeSize', USHORT),
            ('otdEnvironmentOffset', USHORT),
            ('otdEnvironmentSize', USHORT)
        ]
        
        otdEnvironmentOffset: int
        otdDeviceNameOffset: int
        otdDriverNameOffset: int
        otdExtDevmodeOffset: int
        otdEnvironmentSize: int
        otdExtDevmodeSize: int
        otdPortNameOffset: int
        otdData: PBYTE
        
    array_after_structure(OLETARGETDEVICE, 'otdData', BYTE)

    # flags used in some methods
    OF_SET             = 0x0001
    OF_GET             = 0x0002
    OF_HANDLER         = 0x0004

    # return codes for OLE functions 
    OLE_OK = 0                          # 0   Function operated correctly             

    OLE_WAIT_FOR_RELEASE = 1            # 1   Command has been initiated, client      
                                        #     must wait for release. keep dispatching 
                                        #     messages till OLE_RELESE in callback    

    OLE_BUSY = 2                        # 2   Tried to execute a method while another 
                                        #     method is in progress.                  

    OLE_ERROR_PROTECT_ONLY = 3          # 3   Ole APIs are called in real mode        
    OLE_ERROR_MEMORY = 4                # 4   Could not alloc or lock memory          
    OLE_ERROR_STREAM = 5                # 5  (OLESTREAM) stream error                 
    OLE_ERROR_STATIC = 6                # 6   Non static object expected              
    OLE_ERROR_BLANK = 7                 # 7   Critical data missing                   
    OLE_ERROR_DRAW = 8                  # 8   Error while drawing                     
    OLE_ERROR_METAFILE = 9              # 9   Invalid metafile                        
    OLE_ERROR_ABORT = 10                # 10  Client chose to abort metafile drawing  
    OLE_ERROR_CLIPBOARD = 11            # 11  Failed to get/set clipboard data        
    OLE_ERROR_FORMAT = 12               # 12  Requested format is not available       
    OLE_ERROR_OBJECT = 13               # 13  Not a valid object                      
    OLE_ERROR_OPTION = 14               # 14  Invalid option(link update / render)    
    OLE_ERROR_PROTOCOL = 15             # 15  Invalid protocol                        
    OLE_ERROR_ADDRESS = 16              # 16  One of the pointers is invalid          
    OLE_ERROR_NOT_EQUAL = 17            # 17  Objects are not equal                   
    OLE_ERROR_HANDLE = 18               # 18  Invalid handle encountered              
    OLE_ERROR_GENERIC = 19              # 19  Some general error                      
    OLE_ERROR_CLASS = 20                # 20  Invalid class                           
    OLE_ERROR_SYNTAX = 21               # 21  Command syntax is invalid               
    OLE_ERROR_DATATYPE = 22             # 22  Data format is not supported            
    OLE_ERROR_PALETTE = 23              # 23  Invalid color palette                   
    OLE_ERROR_NOT_LINK = 24             # 24  Not a linked object                     
    OLE_ERROR_NOT_EMPTY = 25            # 25  Client doc contains objects.            
    OLE_ERROR_SIZE = 26                 # 26  Incorrect buffer size passed to the api 
                                        #     that places some string in caller's     
                                        #     buffer                                  

    OLE_ERROR_DRIVE = 27                # 27  Drive letter in doc name is invalid     
    OLE_ERROR_NETWORK = 28              # 28  Failed to establish connection to a     
                                        #     network share on which the document     
                                        #     is located                              

    OLE_ERROR_NAME = 29                 # 29  Invalid name(doc name, object name),    
                                        #     etc.. passed to the APIs                

    OLE_ERROR_TEMPLATE = 30             # 30  Server failed to load template          
    OLE_ERROR_NEW = 31                  # 31  Server failed to create new doc         
    OLE_ERROR_EDIT = 32                 # 32  Server failed to create embedded        
                                        #     instance                                
    OLE_ERROR_OPEN = 33                 # 33  Server failed to open document,         
                                        #     possible invalid link                   

    OLE_ERROR_NOT_OPEN = 34             # 34  Object is not open for editing          
    OLE_ERROR_LAUNCH = 35               # 35  Failed to launch server                 
    OLE_ERROR_COMM = 36                 # 36  Failed to communicate with server       
    OLE_ERROR_TERMINATE = 37            # 37  Error in termination                    
    OLE_ERROR_COMMAND = 38              # 38  Error in execute                        
    OLE_ERROR_SHOW = 39                 # 39  Error in show                           
    OLE_ERROR_DOVERB = 40               # 40  Error in sending do verb, or invalid    
                                        #     verb                                    
    OLE_ERROR_ADVISE_NATIVE = 41        # 41  Item could be missing                   
    OLE_ERROR_ADVISE_PICT = 42          # 42  Item could be missing or server doesn't 
                                        #     this format.                            

    OLE_ERROR_ADVISE_RENAME = 43        # 43  Server doesn't support rename           
    OLE_ERROR_POKE_NATIVE = 44          # 44  Failure of poking native data to server 
    OLE_ERROR_REQUEST_NATIVE = 45       # 45  Server failed to render native data     
    OLE_ERROR_REQUEST_PICT = 46         # 46  Server failed to render presentation    
                                        #     data                                    
    OLE_ERROR_SERVER_BLOCKED = 47       # 47  Trying to block a blocked server or     
                                        #     trying to revoke a blocked server       
                                        #     or document                             

    OLE_ERROR_REGISTRATION = 48         # 48  Server is not registered in regestation 
                                        #     data base                               
    OLE_ERROR_ALREADY_REGISTERED = 49   # 49  Trying to register same doc multiple    
                                        #    times                                   
    OLE_ERROR_TASK = 50                 # 50  Server or client task is invalid        
    OLE_ERROR_OUTOFDATE = 51            # 51  Object is out of date                   
    OLE_ERROR_CANT_UPDATE_CLIENT = 52   # 52 Embed doc's client doesn't accept       
                                        #     updates                                 
    OLE_ERROR_UPDATE = 53               # 53  erorr while trying to update            
    OLE_ERROR_SETDATA_FORMAT = 54       # 54  Server app doesn't understand the       
                                        #     format given to its SetData method      
    OLE_ERROR_STATIC_FROM_OTHER_OS = 55 # 55 trying to load a static object created 
                                        #    on another Operating System           
    OLE_ERROR_FILE_VER = 56

    # Following are warnings
    OLE_WARN_DELETE_DATA = 1000 #     Caller must delete the data when he is  
                                #     done with it.                           
    OLESTATUS = INT

    # Codes for CallBack events 
    OLE_CHANGED = 0             # 0                                             
    OLE_SAVED = 1               # 1                                             
    OLE_CLOSED = 2              # 2                                             
    OLE_RENAMED = 3             # 3                                             
    OLE_QUERY_PAINT = 4         # 4  Interruptible paint support                
    OLE_RELEASE = 5             # 5  Object is released(asynchronous operation  
                                #    is completed)                              
    OLE_QUERY_RETRY = 6         # 6  Query for retry when server sends busy ACK 
    OLE_NOTIFICATION = INT

    OLE_NONE = 0                # 0  no method active                           
    OLE_DELETE = 1              # 1  object delete                              
    OLE_LNKPASTE = 2            # 2  PasteLink(auto reconnect)                  
    OLE_EMBPASTE = 3            # 3  paste(and update)                          
    OLE_SHOW = 4                # 4  Show                                       
    OLE_RUN = 5                 # 5  Run                                        
    OLE_ACTIVATE = 6            # 6  Activate                                   
    OLE_UPDATE = 7              # 7  Update                                     
    OLE_CLOSE = 8               # 8  Close                                      
    OLE_RECONNECT = 9           # 9  Reconnect                                  
    OLE_SETUPDATEOPTIONS = 10   # 10 setting update options                     
    OLE_SERVERUNLAUNCH = 11     # 11 server is being unlaunched                 
    OLE_LOADFROMSTREAM = 12     # 12 LoadFromStream(auto reconnect)             
    OLE_SETDATA = 13            # 13 OleSetData                                 
    OLE_REQUESTDATA = 14        # 14 OleRequestData                             
    OLE_OTHER = 15              # 15 other misc async operations                
    OLE_CREATE = 16             # 16 create                                     
    OLE_CREATEFROMTEMPLATE = 17 # 17 CreatefromTemplate                         
    OLE_CREATELINKFROMFILE = 18 # 18 CreateLinkFromFile                         
    OLE_COPYFROMLNK = 19        # 19 CopyFromLink(auto reconnect)               
    OLE_CREATEFROMFILE = 20     # 20 CreateFromFile                             
    OLE_CREATEINVISIBLE = 20    # 21 CreateInvisible                            
    OLE_RELEASE_METHOD = INT

    # rendering options 
    olerender_none = 0
    olerender_draw = 1
    olerender_format = 2
    OLEOPT_RENDER = INT

    # standard clipboard format type 
    OLECLIPFORMAT = WORD

    # Link update options 

    oleupdate_always = 0
    oleupdate_onsave = 1
    oleupdate_oncall = 2
    oleupdate_onclose = 3
    OLEOPT_UPDATE = INT

    HOBJECT = HANDLE
    LHSERVER = LONG_PTR
    LHCLIENTDOC = LONG_PTR
    LHSERVERDOC = LONG_PTR

    class OLE1VirtualTable(VirtualTable):    
        def ole1_function(self, *args: type, exists: bool = False,
                        intermediate_method: bool = False) -> Callable:
            return super().function(OLESTATUS, *args, exists=exists, intermediate_method=intermediate_method)

    class OLECLIENT(CStructure):
        virtual_table = OLE1VirtualTable('OLECLIENT')
        
        @virtual_table.function(INT, OLE_NOTIFICATION, PVOID)
        def CallBack(self, olenotif: int, pobj: IPointer['OLEOBJECT']) -> int: ...
        
        _fields_ = virtual_table.build()

    LPOLECLIENT = OLECLIENT.PTR()

    class OLESTREAM(CStructure):
        virtual_table =  OLE1VirtualTable('OLESTREAM')
        
        @virtual_table.function(DWORD, LPVOID, DWORD)
        def Get(self, pv: LPVOID, cb: int) -> int: ...
        
        @virtual_table.function(DWORD, LPCVOID, DWORD)
        def Put(self, pv: LPCVOID, cb: int) -> int: ...
        
        _fields_ = virtual_table.build()
        
    LPOLESTREAM = OLESTREAM.PTR()

    class OLEOBJECT(CStructure):
        virtual_table = OLE1VirtualTable('OLEOBJECT')
        
        @virtual_table.function(PVOID, LPCSTR)
        def QueryProtocol(self, szProtocol: LPCSTR) -> int: ...
        
        @virtual_table.ole1_function()
        def Release(self) -> int: ...
        
        @virtual_table.ole1_function(BOOL)
        def Show(self, b: bool) -> int: ...
        
        @virtual_table.ole1_function(UINT, BOOL, BOOL)
        def DoVerb(self, iVerb: int, b1: bool, b2: bool) -> int: ...
        
        @virtual_table.ole1_function(OLECLIPFORMAT, PHANDLE)
        def GetData(self, clipformat: int, phData: IPointer[HANDLE]) -> int: ...
        
        @virtual_table.ole1_function(OLECLIPFORMAT, HANDLE)
        def SetData(self, clipformat: int, hData: int) -> int: ...
        
        @virtual_table.ole1_function(HGLOBAL)
        def SetTargetDevice(self, hGlobal: int) -> int: ...
        
        @virtual_table.ole1_function(PRECT)
        def SetBounds(self, prectBounds: IPointer[RECT]) -> int: ...
        
        @virtual_table.function(OLECLIPFORMAT, OLECLIPFORMAT)
        def EnumFormats(self, clipformat: int) -> int: ...
        
        @virtual_table.ole1_function(PLOGPALETTE)
        def SetColorScheme(self, plogpal: IPointer[LOGPALETTE]) -> int: ...
        
        # Server has to implement only the above methods.
        
        # Extra methods required for client.
        @virtual_table.ole1_function()
        def Delete(self) -> int: ...
        
        @virtual_table.ole1_function(LPCSTR, LPCSTR)
        def SetHostNames(self, szContainerApp: LPCSTR, szContainerObj: LPCSTR) -> int: ...
        
        @virtual_table.ole1_function(LPOLESTREAM)
        def SaveToStream(self, pstream: IPointer[OLESTREAM]) -> int: ...
        
        @virtual_table.ole1_function(LPOLECLIENT, LHCLIENTDOC, LPCSTR, PVOID)
        def Clone(self, pclient: IPointer[OLECLIENT], lhClientDoc: int,
                sz: LPCSTR, pobj: IPointer['OLEOBJECT']) -> int: ...
        
        @virtual_table.ole1_function(LPOLECLIENT, LHCLIENTDOC, LPCSTR, PVOID)
        def CopyFromLink(self, pclient: IPointer[OLECLIENT], lhClientDoc: int,
                sz: LPCSTR, pobj: IPointer['OLEOBJECT']) -> int: ...
        
        @virtual_table.ole1_function(PVOID)
        def Equal(self, pobj: IPointer['OLEOBJECT']) -> int: ...
        
        @virtual_table.ole1_function()
        def CopyToClipboard(self) -> int: ...
        
        @virtual_table.ole1_function(HDC, PRECT, PRECT, HDC)
        def Draw(self, hDC: int, prectbounds: IPointer[RECT],
                prect: IPointer[RECT], hDC2: int) -> int: ...
        
        @virtual_table.ole1_function(UINT, BOOL, BOOL, HWND, PRECT)
        def Activate(self, ui: int, b1: bool, b2: bool, hWnd: HWND,
                    prect: IPointer[RECT]) -> int: ...
        
        @virtual_table.ole1_function(HGLOBAL, UINT)
        def Execute(self, hGlobal: int, ui: int) -> int: ...
        
        @virtual_table.ole1_function()
        def Close(self) -> int: ...
        
        @virtual_table.ole1_function()
        def Update(self) -> int: ...
        
        @virtual_table.ole1_function()
        def Reconnect(self) -> int: ...
        
        @virtual_table.ole1_function(LPCSTR, LPOLECLIENT, LHCLIENTDOC, LPCSTR, PVOID)
        def ObjectConvert(self, sz: LPCSTR, pclient: IPointer[OLECLIENT],
                        lhClientDoc: int, sz2: LPCSTR, pobj: IPointer['OLEOBJECT']) -> int: ...
        
        @virtual_table.ole1_function(PTR(OLEOPT_UPDATE))
        def GetLinkUpdateOptions(self, popts: IPointer[OLEOPT_UPDATE]) -> int: ...
        
        @virtual_table.ole1_function(OLEOPT_UPDATE)
        def SetLinkUpdateOptions(self, opts: int) -> int: ...
        
        @virtual_table.ole1_function(LPCSTR)
        def Rename(self, newName: LPCSTR) -> int: ...
        
        @virtual_table.ole1_function(LPSTR, PUINT)
        def QueryName(self, name: LPSTR, cb: int) -> int: ...
        
        @virtual_table.ole1_function(PLONG)
        def QueryType(self, ptype: PLONG) -> int: ...
        
        @virtual_table.ole1_function(PRECT)
        def QueryBounds(self, prectbounds: IPointer[RECT]) -> int: ...
        
        @virtual_table.ole1_function(PDWORD)
        def QuerySize(self, pdwSize: PDWORD) -> int: ...
        
        @virtual_table.ole1_function()
        def QueryOpen(self) -> int: ...
        
        @virtual_table.ole1_function()
        def QueryOutOfDate(self) -> int: ...
        
        @virtual_table.ole1_function()
        def QueryReleaseStatus(self) -> int: ...
        
        @virtual_table.ole1_function()
        def QueryReleaseError(self) -> int: ...
        
        @virtual_table.function(OLE_RELEASE_METHOD)
        def QueryReleaseMethod(self) -> int: ...
        
        @virtual_table.ole1_function(OLECLIPFORMAT)
        def RequestData(self, clipformat: int) -> int: ...
        
        @virtual_table.ole1_function(UINT, PLONG)
        def ObjectLong(self, ui: int, pl: PLONG) -> int: ...
        
        @virtual_table.ole1_function(HANDLE, LPOLECLIENT, BOOL)
        def ChangeData(self, handle: int, pclient: IPointer[OLECLIENT], b: bool) -> int: ...
        
        _fields_ = virtual_table.build()
        
    def ole1_foreign(*args: type, 
                name: Optional[str] = None,
                intermediate_method: bool = False) -> Callable:
            """
            Foreign method declare
            """
            return foreign_optimized(OLESTATUS, 
                                    *args,
                                    library=ole32, 
                                    name=name, 
                                    intermediate_method=intermediate_method)
        
    def ole1oo_foreign(*args: type, 
                name: Optional[str] = None,
                intermediate_method: bool = False) -> Callable:
            """
            Foreign method declare
            """
            return foreign_optimized(OLESTATUS, LPOLEOBJECT
                                    *args,
                                    library=ole32, 
                                    name=name, 
                                    intermediate_method=intermediate_method)
            
    @ole1oo_foreign()
    def OleDelete(pobj: IPointer[OLEOBJECT]) -> int: ...
            
    @ole1oo_foreign()
    def OleRelease(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign(LPOLESTREAM)
    def OleSaveToStream(pobj: IPointer[OLEOBJECT], pstream: IPointer[OLESTREAM]) -> int: ...

    @ole1oo_foreign(LPOLEOBJECT)
    def OleEqual(pobj: IPointer[OLEOBJECT], pobj2: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign()
    def OleCopyToClipboard(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign(LPCSTR, LPCSTR)
    def OleSetHostNames(pobj: IPointer[OLEOBJECT], szContainerApp: LPCSTR, szContainerObj: LPCSTR) -> int: ...

    @ole1oo_foreign(HGLOBAL)
    def OleSetTargetDevice(pobj: IPointer[OLEOBJECT], hGlobal: int) -> int: ...

    @ole1oo_foreign(PRECT)
    def OleSetBounds(pobj: IPointer[OLEOBJECT], prectbounds: IPointer[RECT]) -> int: ...

    @ole1oo_foreign(PLOGPALETTE)
    def OleSetColorScheme(pobj: IPointer[OLEOBJECT], plogpal: IPointer[LOGPALETTE]) -> int: ...

    @ole1oo_foreign(PRECT)
    def OleQueryBounds(pobj: IPointer[OLEOBJECT], prectbounds: IPointer[RECT]) -> int: ...

    @ole1oo_foreign(PDWORD)
    def OleQuerySize(pobj: IPointer[OLEOBJECT], pdwSize: PDWORD) -> int: ...

    @ole1oo_foreign(HDC, PRECT, PRECT, HDC)
    def OleDraw(pobj: IPointer[OLEOBJECT], prect: IPointer[RECT], prect2: IPointer[RECT], hDC: int) -> int: ...

    @ole1oo_foreign()
    def OleQueryOpen(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign(UINT, BOOL, BOOL, HWND, PRECT)
    def OleQueryActivate(pobj: IPointer[OLEOBJECT], ui: int, b1: bool, b2: bool, hWnd: int, prect: IPointer[RECT]) -> int: ...

    @ole1oo_foreign(HGLOBAL, UINT)
    def OleExecute(pobj: IPointer[OLEOBJECT], hGlobal: int, ui: int) -> int: ...

    @ole1oo_foreign()
    def OleClose(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign()
    def OleUpdate(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign()
    def OleReconnect(pobj: IPointer[OLEOBJECT]) -> int: ...

    @ole1oo_foreign(PTR(OLEOPT_UPDATE))
    def OleGetLinkUpdateOptions(pobj: IPointer[OLEOBJECT], popts: IPointer[OLEOPT_UPDATE]) -> int: ...

    @ole1oo_foreign(OLEOPT_UPDATE)
    def OleSetLinkUpdateOptions(pobj: IPointer[OLEOBJECT], opts: int) -> int: ...

    @ole1oo_foreign(PVOID, LPCSTR)
    def OleQueryProtocol(pobj: IPointer[OLEOBJECT], szProtocol: LPCSTR) -> int: ...

