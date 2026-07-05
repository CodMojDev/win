from win.com.wincodec import *
from .core.handle import *
from win.com.comtl.baseface import *

class ImagingFactory(IWICImagingFactory):
    INST: 'ImagingFactory' = None
    
    @classmethod
    def instance(cls) -> 'ImagingFactory':
        if cls.INST is not None:
            return cls.INST
        
        factory = cls.Create(CLSID_WICImagingFactory).contents
        TlAddRefGuard(factory)
        cls.INST = factory
        
        return factory

class ImagingPalette(IWICPalette):
    ...

class BitmapSource(IWICBitmapSource):
    @property
    def size(self) -> tuple[int, int]:
        width, height = UINT(), UINT()
        hr = self.GetSize(byref(width), byref(height))
        if FAILED(hr): raise COMError(hr)
        return (width.value, height.value)
    
    @property
    def width(self) -> int:
        return self.size[0]
    
    @property
    def height(self) -> int:
        return self.size[1]
    
    @property
    def resolution(self) -> tuple[float, float]:
        dpiX, dpiY = DOUBLE(), DOUBLE()
        hr = self.GetResolution(byref(dpiX), byref(dpiY))
        if FAILED(hr): raise COMError(hr)
        return (dpiX.value, dpiY.value)
    
    def copy(self, buffer: WT_ADDRLIKE, stride: int, size: int, rc: RECT):
        hr = self.CopyPixels(i_cast(byref(rc) if rc else NULL, PTR(WICRect)), stride, size, i_cast(buffer, PBYTE))
        if FAILED(hr): raise COMError(hr)

class FormatConverter(BitmapSource, IWICFormatConverter):
    def __new__(cls):
        factory = ImagingFactory.instance()
        pConverter = cls.NULL()
        hr = factory.CreateFormatConverter(i_cast(byref(pConverter), IWICFormatConverter.DOUBLE_PTR()))
        if FAILED(hr): raise COMError(hr)
        TlAddRefGuard(pConverter)
        return pConverter.contents
    
    def initialize(self, source: 'BitmapSource', destination: GUID, dither: int = WICBitmapDitherTypeNone, 
                   palette: ImagingPalette = None, alpha_threshold: int = 0.0, translate: int = WICBitmapPaletteTypeCustom):
        hr = self.Initialize(source.ref(), destination, dither, palette.ref() if palette else NULL, alpha_threshold, translate)
        if FAILED(hr): raise COMError(hr)

class BitmapFrame:
    class Decoder(BitmapSource, IWICBitmapFrameDecode):
        @property
        def thumbnail(self) -> BitmapSource:
            source = BitmapSource.NULL()
            hr = self.GetThumbnail(i_cast(byref(source), IWICBitmapSource.PTR()))
            if FAILED(hr): raise COMError(hr)
            return source
        
    class Encoder(BitmapSource, IWICBitmapFrameEncode):
        @property
        def size(self) -> tuple[int, int]:
            return super().size
        
        @size.setter
        def size(self, size: tuple[int, int]):
            hr = self.SetSize(size[0], size[1])
            if FAILED(hr): raise COMError(hr)
            
        @property
        def resolution(self) -> tuple[float, float]:
            return super().resolution
        
        @resolution.setter
        def resolution(self, resolution: tuple[float, float]):
            hr = self.SetResolution(resolution[0], resolution[1])
            if FAILED(hr): raise COMError(hr)
            
        def _thumbnail(self, thumbnail: IWICBitmapSource):
            hr = self.SetThumbnail(i_cast(thumbnail.ref(), IWICBitmapSource.PTR()))
            if FAILED(hr): raise COMError(hr)
            
        def commit(self):
            hr = self.Commit()
            if FAILED(hr): raise COMError(hr)
            
        thumbnail = property(fset=_thumbnail)

class BitmapDecoder(IWICBitmapDecoder):
    frames: 'BitmapDecoder.Frames'
    
    class Frames:
        decoder: 'BitmapDecoder'
        
        def __init__(self, decoder: 'BitmapDecoder'):
            self.decoder = decoder
            
        def __getitem__(self, index: int) -> 'BitmapFrame.Decoder':
            pFrame = BitmapFrame.Decoder.NULL()
            hr = self.decoder.GetFrame(0, i_cast(byref(pFrame), IWICBitmapFrameDecode.PTR()))
            if FAILED(hr): raise COMError(hr)
            TlAddRefGuard(pFrame)
            return pFrame.contents
        
        def __len__(self) -> int:
            count = UINT()
            hr = self.decoder.GetFrameCount(byref(count))
            if FAILED(hr): raise COMError(hr)
            return count.value
    
    @classmethod
    def from_filename(cls, filename: str, access: int = GENERIC_READ, options: int = WICDecodeMetadataCacheOnLoad) -> 'BitmapDecoder':
        wzFilename = create_unicode_buffer(filename)
        factory = ImagingFactory.instance()
        pDecoder = cls.NULL()
        hr = factory.CreateDecoderFromFilename(wzFilename, NULL, access, options, i_cast(byref(pDecoder), IWICBitmapDecoder.DOUBLE_PTR()))
        if FAILED(hr): raise COMError(hr)
        decoder = pDecoder.contents
        TlAddRefGuard(decoder)
        decoder.frames = BitmapDecoder.Frames(decoder)
        return decoder

class BitmapEx(Bitmap):
    @classmethod
    def from_image(self, file_name: str) -> 'BitmapEx':
        decoder = BitmapDecoder.from_filename(file_name)
        frame = decoder.frames[0]
        converter = FormatConverter()
        converter.initialize(frame, GUID_WICPixelFormat32bppBGR)
        width, height = frame.size
        info = BitmapInfo(width, height, 32)
        pvBits = PVOID()
        hBitmap = CreateDIBSection(NULL, info.ref(), DIB_RGB_COLORS, byref(pvBits), NULL, 0)
        if not hBitmap: raise WinException()
        bitmap = BitmapEx(hBitmap)
        stride = width * 4
        size = stride * height
        converter.copy(pvBits, stride, size, NULL)
        return bitmap
        