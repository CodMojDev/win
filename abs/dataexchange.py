# COM TL imports
from win.com.comtl.object import *
from win.com.comtl.baseface import *
from win.com.comtl.enumerators import *

# COM OleIDL import
from win.com.oleidl import *

# WinAbs imports
from .core.io import *

# DataExchange HRESULTS
DV_E_TYMED = HRESULT(0x80040069).value
DV_E_DVASPECT = HRESULT(0x8004016B).value
DV_E_FORMATETC = HRESULT(0x80040064).value
STG_E_MEDIUMFULL = HRESULT(0x80030070).value

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
    
    def __init__(self, format_or_name: str | int = None, aspect: int = DVASPECT_CONTENT, tymed: int = TYMED_HGLOBAL, lindex: int = -1):
        # if name != None, then set cfFormat to RegisterClipboardFormat result to retrieve/register format ID from name
        if format_or_name is not None:
            if isinstance(format_or_name, int):
                self.cfFormat = format_or_name
            else:
                format_or_name = create_string_buffer(format_or_name)
                self.cfFormat = RegisterClipboardFormatW(format_or_name)
        
        # dwAspect = standard DVASPECT_CONTENT
        self.dwAspect = aspect
        
        # tymed = standard TYMED_HGLOBAL, can be changed
        self.tymed = tymed
        
        # lindex = standard -1
        self.lindex = lindex
        
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
        
    class FormatEtcEnumerator(ValueEnumerator):
        _interface_ = IEnumFORMATETC
        _type_ = FORMATETC
    
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
            result = StreamIO(stg.pstm.contents) # this calls pstm->AddRef
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
    
    def EnumFormatEtc_Impl(self, dwDirection: int, ppenumFormatEtc: IDoublePtr[IEnumFORMATETC]) -> int: 
        if not ppenumFormatEtc:
            return E_POINTER
        if dwDirection == DATADIR_GET:
            enumerator = self.FormatEtcEnumerator(self.get_formats())
            TlWritePointerToPpv(ppenumFormatEtc, enumerator.ref())
        else:
            return E_INVALIDARG
        return S_OK
    
    def GetCanonicalFormatEtc_Impl(self, pformatetcIn: IPointer[FORMATETC], pformatetcOut: IPointer[FORMATETC]) -> int: 
        if not pformatetcOut: return E_POINTER
        pformatetcOut.contents.ptd = NULL
        return E_NOTIMPL
    
    def DAdvise_Impl(self, pformatetc: IPointer[FORMATETC], advf: int, pAdvSink: IPointer[IAdviseSink], pdwConnection: PDWORD) -> int: 
        if not pdwConnection: return E_POINTER
        pdwConnection.contents.value = 0
        return E_NOTIMPL

    def DUnadvise_Impl(self, dwConnection: int) -> int: 
        return E_NOTIMPL

    def EnumDAdvise_Impl(self, ppenumAdvise: IDoublePtr[IEnumSTATDATA]) -> int: 
        if not ppenumAdvise: return E_POINTER
        TlWritePvToPpv(ppenumAdvise, 0)
        return E_NOTIMPL
    
    def SetData_Impl(self, pformatetc: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM], fRelease: int) -> int: 
        if not pformatetc: return E_POINTER
        if not pmedium: return E_POINTER
        return self.on_set_data(i_cast_value(pformatetc, FormatEtc), pmedium.contents, fRelease != 0)
    
    def QueryGetData_Impl(self, pformatetc: IPointer[FORMATETC]) -> int: 
        if not pformatetc: return E_POINTER
        format_etc_in = pformatetc.contents
        for format_etc in self.get_formats():
            if hash(format_etc) == hash(format_etc_in):
                return S_OK
        return DV_E_FORMATETC
    
    def GetData_Impl(self, pformatetcIn: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM]) -> int:
        if not pmedium: return E_POINTER
        hr = self.QueryGetData_Impl(pformatetcIn)
        if hr != S_OK: return hr
        return self.on_get_data(i_cast_value(pformatetcIn, FormatEtc), pmedium.contents, False)

    def GetDataHere_Impl(self, pformatetc: IPointer[FORMATETC], pmedium: IPointer[STGMEDIUM]) -> int: 
        if not pmedium: return E_POINTER
        hr = self.QueryGetData_Impl(pformatetc)
        if hr != S_OK: return hr
        return self.on_get_data(i_cast_value(pformatetc, FormatEtc), pmedium.contents, True)
    
    def get_formats(self) -> list[FormatEtc]:
        return []
    
    def on_set_data(self, format_etc: FormatEtc, medium: STGMEDIUM, release: bool) -> int:
        return E_NOTIMPL
    
    def on_get_data(self, format_etc: FormatEtc, medium: STGMEDIUM, direct: bool) -> int:
        return E_NOTIMPL
    
    AddRef_Impl = CComObject.AddRef_Impl
    Release_Impl = CComObject.Release_Impl
    QueryInterface_Impl = CComObject.QueryInterface_Impl
    dbg_trace = CComObject.dbg_trace
    Cleanup = CComObject.Cleanup
    
    _mta_ = True
    _com_map_ = [(IDataObject, IDataObject.virtual_table)]
    
    def setup(self):
        CUnknown.__init__(self)
        CComObject.InitComObject(self)
        self.implement_interface(IDataObject)