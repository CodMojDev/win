from .window import *
from win.com.ctlinterfacedef import *

atl = get_win_library('atl.dll')

@atl.foreign(BOOL)
def AtlAxWinInit() -> int: ...
    
@atl.foreign(HRESULT, HWND, PTR(LPUNKNOWN))
def AtlAxGetControl(h: int, pp: IDoublePtr[IUnknown]) -> int: ...

@atl.foreign(HRESULT, LPUNKNOWN, HWND, PTR(LPUNKNOWN))
def AtlAxAttachControl(pControl: IPointer[IUnknown], hWnd: int, ppUnkContainer: IDoublePtr[IUnknown]) -> int: ...
    
@atl.foreign(HRESULT, HWND, PTR(LPUNKNOWN))
def AtlAxGetHost(h: int, pp: IDoublePtr[IUnknown]) -> int: ...

@atl.foreign(HRESULT, LPCOLESTR, HWND, LPSTREAM, PVOID, PVOID, REFIID, LPUNKNOWN, intermediate_method=True)
def AtlAxCreateControlEx(lpszName: WT_LPWSTR, hWnd: WT_HANDLE, pStream: IPointer[IStream], ppUnkContainer: IDoublePtr[IUnknown], ppUnkControl: IDoublePtr[IUnknown], iidSink: IID, punkSink: IPointer[IUnknown], **kwargs) -> int:
    return delegate(lpszName, hWnd, pStream, ppUnkContainer, ppUnkControl, iidSink.ref(), punkSink)

class AxHost(Control):
    """
    ActiveX Control host, based on ATL infrastructure.
    """
    ATLAXWIN_INITED: ClassVar[bool] = False
    
    _width: int
    _height: int
    _clsid: str | CLSID | None
    _license: str | None
    _stream: IStream | None
    _sink: tuple[IT, type[IT]] | None
    
    def __init__(self, clsid: str | CLSID | None, width: int, height: int, parent: int | HWND, identifier: int | HMENU, stream: IStream | None = None, sink: tuple[IT, type[IT]] | None = None):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self._clsid = clsid
        if stream is not None:
            stream.AddRef()
        self._stream = stream
        if sink is not None:
            if not isinstance(sink, (tuple, list)):
                raise TypeError(f"'sink' argument must be a tuple or a list, not '{type(sink).__qualname__}'")
            sink[0].AddRef()
        self._sink = sink
        self.class_name = 'AtlAxWin'
        if not AxHost.ATLAXWIN_INITED:
            AtlAxWinInit()
            AxHost.ATLAXWIN_INITED = True
    
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, None, relative)
        if self._clsid is not None:
            if self._sink is None:
                sink = NULL
                sink_iid = IID_NULL
            else:
                sink = self._sink[0]
                sink_iid = self._sink[1]._iid_
            if self._stream is None:
                stm = NULL
            else:
                stm = self._stream.ref()
            hr = AtlAxCreateControlEx(str(self._clsid), self, stm, NULL, NULL, sink_iid, sink)
            if self._stream is not None:
                self._stream.Release()
                self._stream = None
            if self._sink is not None:
                self._sink[0].Release()
                self._sink = None
            if FAILED(hr): raise COMError(hr)
    
    def get_control(self, itf: type[IT] = IUnknown) -> IT:
        """
        Retrieve the ActiveX control interface.
        """
        pItf = LPUNKNOWN()
        hr = AtlAxGetControl(self, byref(pItf))
        if FAILED(hr): raise COMError(hr)
        pDesiredItf = itf.NULL()
        hr = pItf.contents.QueryInterface(itf, byref(pDesiredItf))
        if FAILED(hr): raise COMError(hr)
        pItf.contents.Release()
        return pDesiredItf.contents
        
    def get_host(self, itf: type[IT] = IUnknown) -> IT:
        """
        Retrieve the ActiveX host interface.
        """
        pItf = LPUNKNOWN()
        hr = AtlAxGetHost(self, byref(pItf))
        if FAILED(hr): raise COMError(hr)
        pDesiredItf = itf.NULL()
        hr = pItf.contents.QueryInterface(itf, byref(pDesiredItf))
        if FAILED(hr): raise COMError(hr)
        pItf.contents.Release()
        return pDesiredItf.contents
    
    def attach(self, itf: IUnknown):
        """
        Attach control IUnknown to ActiveX host.
        """
        hr = AtlAxAttachControl(itf.ref(), self, NULL)
        if FAILED(hr): raise COMError(hr)
        
    def __del__(self):
        if self._stream is not None:
            self._stream.Release()
        if self._sink is not None:
            self._sink[0].Release()