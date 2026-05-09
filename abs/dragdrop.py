from win.com.comtl.object import *
from win.com.comtl.baseface import *
from win.com.oleidl import *
from .window import *
from .core.io import *

@ole32.foreign(HRESULT, HWND, LPDROPTARGET)
def RegisterDragDrop(hwnd: int, pDropTarget: IPointer[IDropTarget]) -> int: ...

@ole32.foreign(HRESULT, HWND)
def RevokeDragDrop(hwnd: int) -> int: ...

@ole32.foreign(HRESULT, PVOID)
def OleInitialize(pvReserved: int) -> int: ...

@ole32.foreign(HRESULT)
def OleUninitialize() -> int: ...

DV_E_TYMED = HRESULT(0x80040069).value

class FormatEtc(FORMATETC):
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
        if name is not None:
            name = create_string_buffer(name)
            self.cfFormat = RegisterClipboardFormatW(name)
        
        self.dwAspect = DVASPECT_CONTENT
        self.tymed = TYMED_HGLOBAL
        self.lindex = -1
        
    def __str__(self) -> str:
        fmt = self.cfFormat
        string = FormatEtc.CF_FORMATS.get(fmt)
        if string is not None:
            return string
        
        buffer = create_unicode_buffer(256)
        GetClipboardFormatNameW(fmt, buffer, len(buffer))
        return buffer.value
        
    def __repr__(self) -> str:
        return f'<FormatEtc "{self}">'

class DataObject(IDataObject):
    def get(self, format_etc: FORMATETC):
        tymed = format_etc.tymed
        format_etc.tymed = TYMED_HGLOBAL
        pformatetc = format_etc.ref()
        hr = self.QueryGetData(pformatetc)
        if FAILED(hr):
            if hr == DV_E_TYMED:
                format_etc.tymed = TYMED_ISTREAM
                hr = self.QueryGetData(pformatetc)
                if FAILED(hr):
                    if hr == DV_E_TYMED:
                        format_etc.tymed = TYMED_FILE
                        hr = self.QueryGetData(pformatetc)
                        if FAILED(hr):
                            if hr == DV_E_TYMED:
                                format_etc.tymed = TYMED_GDI
                                hr = self.QueryGetData(pformatetc)
                                if FAILED(hr): raise COMError(hr)
                            else:
                                raise COMError(hr)
                    else:
                        raise COMError(hr)
            else:
                raise COMError(hr)
        stg = STGMEDIUM()
        stg.tymed = format_etc.tymed
        hr = self.GetData(pformatetc, stg.ref())
        if FAILED(hr): raise COMError(hr)
        if format_etc.tymed == TYMED_HGLOBAL:
            result = GlobalIO(stg.hGlobal).owning()
        elif format_etc.tymed == TYMED_ISTREAM:
            result = StreamIO(stg.pstm)
            stg.pstm.contents.Release()
        elif format_etc.tymed == TYMED_FILE:
            result = open(stg.lpszFileName.value, 'rb+')
            CoTaskMemFree(stg.lpszFileName)
        elif format_etc.tymed == TYMED_GDI:
            result = Bitmap(stg.hBitmap)

        format_etc.tymed = tymed
        return result
    
    @property
    def formats(self) -> tuple[FormatEtc, ...]:
        pEnumerator = IEnumFORMATETC.NULL()
        hr = self.EnumFormatEtc(DATADIR_GET, byref(pEnumerator))
        if FAILED(hr): raise COMError(hr)
        return tuple(TL_ITERATOR[FormatEtc](pEnumerator))

class DragDropWindow(Window):
    class DropTarget(CComObject, IDropTarget):
        def __init__(self):
            super().__init__()
            
            self.implement_interface(IDropTarget)
            self.on_drag_enter = SingleEvent()
            self.on_drop = SingleEvent()
            self.on_drag_leave = SingleEvent()
            self.on_drag_over = SingleEvent()
        
        def DragEnter_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            if not (pDataObj and pdwEffect):
                return E_POINTER
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents
                pdwEffect.contents.value = self.on_drag_enter.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e:
                return e.hresult
            except Exception:
                return E_FAIL
            return S_OK

        def DragOver_Impl(self, grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: 
            if not pdwEffect:
                return E_POINTER
            try:
                pdwEffect.contents.value = self.on_drag_over.execute(grfKeyState, i_cast_structure(pt, Point))
            except COMError as e:
                return e.hresult
            except Exception:
                return E_FAIL
            return S_OK

        def DragLeave_Impl(self) -> int: 
            try:
                self.on_drag_leave.execute()
            except COMError as e:
                return e.hresult
            except Exception:
                return E_FAIL
            return S_OK

        def Drop_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents
                pdwEffect.contents.value = self.on_drop.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e:
                return e.hresult
            except Exception:
                return E_FAIL
            return S_OK
        
    def __init__(self):
        super().__init__()
            
        hr = OleInitialize(NULL)
        if hr in (S_OK, RPC_E_CHANGED_MODE):
            self.ole_is_held = True
        elif FAILED(hr):
            raise COMError(hr)
        else:
            self.ole_is_held = False
        
        self.drop_target = DragDropWindow.DropTarget()
        self.drop_target.on_drag_enter.set(self.on_drag_enter)
        self.drop_target.on_drag_over.set(self.on_drag_over)
        self.drop_target.on_drag_leave.set(self.on_drag_leave)
        self.drop_target.on_drop.set(self.on_drop)
        
        self.on_create += self.DragDropWindow_on_create
        self.on_close += EventCallback(self.DragDropWindow_on_close, Priority.Max)
    
    def DragDropWindow_on_create(self):
        hr = RegisterDragDrop(self, self.drop_target.ref())
        if FAILED(hr): raise COMError(hr)
        return True
    
    def on_drag_enter(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        return DROPEFFECT_NONE
    
    def on_drag_over(self, key_state: int, pt: Point) -> int:
        return DROPEFFECT_NONE
    
    def on_drag_leave(self):
        return
    
    def on_drop(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        return DROPEFFECT_NONE
    
    def DragDropWindow_on_close(self):
        self.drop_target.Release()
        RevokeDragDrop(self)
        if self.ole_is_held:
            OleUninitialize()