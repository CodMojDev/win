# COM TL imports
from win.com.comtl.object import *
from win.com.comtl.baseface import *

# COM OleIDL import
from win.com.oleidl import *

# WinAbs imports
from .window import *
from .core.io import *

#
# OLE & Drag/Drop functions
#

@ole32.foreign(HRESULT, HWND, LPDROPTARGET)
def RegisterDragDrop(hwnd: int, pDropTarget: IPointer[IDropTarget]) -> int: ...

@ole32.foreign(HRESULT, HWND)
def RevokeDragDrop(hwnd: int) -> int: ...

@ole32.foreign(HRESULT, PVOID)
def OleInitialize(pvReserved: int) -> int: ...

@ole32.foreign(HRESULT)
def OleUninitialize() -> int: ...

def _ole_Application_on_destroy():
    OleUninitialize()

def initialize_ole():
    hr = OleInitialize(NULL)
    
    if hr in (S_OK, RPC_E_CHANGED_MODE):
        app = Application()
        app.on_destroy += _ole_Application_on_destroy
    elif FAILED(hr):
        raise COMError(hr)

# Invalid TYMED HRESULT
DV_E_TYMED = HRESULT(0x80040069).value

class FormatEtc(FORMATETC):
    # preinstalled formats dictionary
    CF_FORMATS: dict[int, str] = {
        CF_TEXT: 'Text',
        CF_BITMAP: 'Bitmap',
        CF_METAFILEPICT: 'Metafile',
        CF_SYLK: 'Sylk',
        CF_DIF: 'DIF',
        CF_TIFF: 'TIFF',
        CF_OEMTEXT: 'OEM Text',
        CF_DIB: 'DIB',
        CF_PALETTE: 'Palette',
        CF_PENDATA: 'Pen data',
        CF_RIFF: 'RIFF',
        CF_WAVE: 'Wave audio',
        CF_UNICODETEXT: 'Unicode text',
        CF_ENHMETAFILE: 'EMF',
        CF_HDROP: 'HDROP',
        CF_LOCALE: 'Locale',
        CF_DIBV5: 'DIB v5'
    }
    
    def __init__(self, name: str = None):
        # if name != None, then set cfFormat to RegisterClipboardFormat result to retrieve/register format ID from name
        if name is not None:
            name = create_string_buffer(name)
            self.cfFormat = RegisterClipboardFormatW(name)
        
        # dwAspect = standard DVASPECT_CONTENT
        self.dwAspect = DVASPECT_CONTENT
        
        # tymed = standard TYMED_HGLOBAL, can be changed
        self.tymed = TYMED_HGLOBAL
        
        # lindex = standard -1
        self.lindex = -1
        
    def __str__(self) -> str:
        fmt = self.cfFormat
        
        # check preinstalled formats
        string = FormatEtc.CF_FORMATS.get(fmt)
        if string is not None:
            return string
        
        # programmaticaly get the registered clipboard format and return retrieved name
        buffer = create_unicode_buffer(256)
        GetClipboardFormatNameW(fmt, buffer, len(buffer))
        return buffer.value
        
    def __repr__(self) -> str:
        return f'<FormatEtc "{self}">'

class DataObject(IDataObject):
    """
    Class, representing wrapper around IDataObject.
    """
    
    def get(self, format_etc: FORMATETC):
        """
        Get the GlobalIO/StreamIO/io.IOBase/Bitmap from FormatEtc.
        """
        
        # save the previous TYMED, starting from TYMED_HGLOBAL
        tymed = format_etc.tymed
        format_etc.tymed = TYMED_HGLOBAL
        
        # optimization for holding pointer to FORMATETC
        pformatetc = format_etc.ref()
        
        # test the FORMATETC
        hr = self.QueryGetData(pformatetc)
        
        if FAILED(hr): # HRESULT is failed
            if hr == DV_E_TYMED: # invalid TYMED
                # now try TYMED_ISTREAM
                format_etc.tymed = TYMED_ISTREAM
                hr = self.QueryGetData(pformatetc)
                
                if FAILED(hr):
                    if hr == DV_E_TYMED: # invalid TYMED
                        # now try TYMED_FILE
                        format_etc.tymed = TYMED_FILE
                        hr = self.QueryGetData(pformatetc)
                        
                        if FAILED(hr):
                            if hr == DV_E_TYMED: # invalid TYMED
                                # now try TYMED_GDI
                                format_etc.tymed = TYMED_GDI
                                hr = self.QueryGetData(pformatetc)
                                if FAILED(hr): raise COMError(hr) # last TYMED failed, throw COM exception
                            else: # other HRESULT
                                raise COMError(hr)
                    else: # other HRESULT
                        raise COMError(hr)
            else: # other HRESULT
                raise COMError(hr)
        
        # initialize STGMEDIUM by our TYMED
        stg = STGMEDIUM()
        stg.tymed = format_etc.tymed
        
        # get data to STGMEDIUM
        hr = self.GetData(pformatetc, stg.ref())
        if FAILED(hr): raise COMError(hr)
        
        # dispatcherize TYMED to various wrappers
        if format_etc.tymed == TYMED_HGLOBAL:
            # GlobalIO - wrapper around HGLOBAL handle
            result = GlobalIO(stg.hGlobal).owning()
        elif format_etc.tymed == TYMED_ISTREAM:
            # StreamIO - wrapper around IStream interface
            result = StreamIO(stg.pstm) # this calls pstm->AddRef
            stg.pstm.contents.Release() # refcount 2 -> refcount 1
        elif format_etc.tymed == TYMED_FILE:
            # open the file name as standard file system file, in rb+ mode
            result = open(stg.lpszFileName.value, 'rb+')
            CoTaskMemFree(stg.lpszFileName) # free the file name manually
        elif format_etc.tymed == TYMED_GDI:
            # convert the HBITMAP to GDI Bitmap wrapper
            result = Bitmap(stg.hBitmap)

        # restore the saved TYMED
        format_etc.tymed = tymed
        return result
    
    @property
    def formats(self) -> tuple[FormatEtc, ...]:
        pEnumerator = IEnumFORMATETC.NULL()
        hr = self.EnumFormatEtc(DATADIR_GET, byref(pEnumerator))
        if FAILED(hr): raise COMError(hr)
        return tuple(TL_ITERATOR[FormatEtc](pEnumerator))

class DragDropWindow(Window):
    """
    Drag & Drop window.
    """
    
    class DropTarget(CComObject, IDropTarget):
        """
        Implementation for OLE IDropTarget.
        """
        
        def __init__(self):
            super().__init__()
            
            # implement the IDropTarget interface functions
            self.implement_interface(IDropTarget)
            
            # DropTarget-specific single events
            self.on_drag_enter = SingleEvent()
            self.on_drop = SingleEvent()
            self.on_drag_leave = SingleEvent()
            self.on_drag_over = SingleEvent()
        
        def DragEnter_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            # check for the pointers validity
            if not (pDataObj and pdwEffect):
                return E_POINTER
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents # wrap IDataObject into DataObject
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drag_enter.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception: 
                return E_FAIL
            return S_OK

        def DragOver_Impl(self, grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: 
            # check for the pointer validity
            if not pdwEffect:
                return E_POINTER
            try:
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drag_over.execute(grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK

        def DragLeave_Impl(self) -> int: 
            try:
                self.on_drag_leave.execute()
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK

        def Drop_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            # check for the pointers validity
            if not (pDataObj and pdwEffect):
                return E_POINTER
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents # wrap IDataObject into DataObject
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drop.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK
        
    def __init__(self):
        super().__init__()
        
        # initialize OLE
        initialize_ole()
        
        # create drop target implementation
        self.drop_target = DragDropWindow.DropTarget()
        
        # bind window events on drop target events
        self.drop_target.on_drag_enter.set(self.on_drag_enter)
        self.drop_target.on_drag_over.set(self.on_drag_over)
        self.drop_target.on_drag_leave.set(self.on_drag_leave)
        self.drop_target.on_drop.set(self.on_drop)
        
        # bind to window events
        self.on_nc_destroy += self.DragDropWindow_on_nc_destroy
        self.on_create += self.DragDropWindow_on_create
    
    def DragDropWindow_on_create(self):
        # register window as drag & drop target
        hr = RegisterDragDrop(self, self.drop_target.ref())
        if FAILED(hr): raise COMError(hr)
        return True
    
    def on_drag_enter(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object entering window.
        """
        
        return DROPEFFECT_NONE
    
    def on_drag_over(self, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object is over window.
        """
        
        return DROPEFFECT_NONE
    
    def on_drag_leave(self):
        """
        This handler is called when drag & drop object leaving window.
        """
        
        return
    
    def on_drop(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object dropped into window.
        """
        
        return DROPEFFECT_NONE
    
    def DragDropWindow_on_nc_destroy(self):
        # release drop target
        self.drop_target.Release()
        RevokeDragDrop(self) # revoke window as drag & drop target from system