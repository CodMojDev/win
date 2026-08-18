from win.com.wincodec import *
from .core.handle import *
from win.com.comtl.baseface import *
from win.com.comtl.streams import *
from win.com.ole2 import *
from win.com.olectl import *

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

class BitmapWIC(IWICBitmap):
    @classmethod
    def from_icon(cls, icon: int | HANDLE) -> 'BitmapWIC':
        factory = ImagingFactory.instance()
        pBitmap = cls.NULL()
        hr = factory.CreateBitmapFromHICON(icon, byref(pBitmap))
        if FAILED(hr): raise COMError(hr)
        TlAddRefGuard(pBitmap)
        return pBitmap.contents
    
    @classmethod
    def from_bitmap(cls, bitmap: int | HANDLE) -> 'BitmapWIC':
        factory = ImagingFactory.instance()
        pBitmap = cls.NULL()
        hr = factory.CreateBitmapFromHBITMAP(bitmap, byref(pBitmap))
        if FAILED(hr): raise COMError(hr)
        TlAddRefGuard(pBitmap)
        return pBitmap.contents

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
        
        def initialize(self, options: IPropertyBag2 | None = None):
            if options is not None:
                options = options.ref()
            hr = self.Initialize(options)
            if FAILED(hr): raise COMError(hr)
            
        def write_source(self, source: BitmapSource, rect: WICRect | None = None):
            if rect is not None:
                rect = rect.ref()
            hr = self.WriteSource(source.ref(), rect)
            if FAILED(hr): raise COMError(hr)

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

class BitmapEncoder(IWICBitmapEncoder):
    def initialize(self, stm: IStream | io.IOBase, option: int = WICBitmapEncoderNoCache):
        if isinstance(stm, io.IOBase):
            stm = StreamOverIO(stm)
            TlAddRefGuard(stm)
        hr = self.Initialize(stm.ref(), option)
        if FAILED(hr): raise COMError(hr)
        
    def commit(self):
        hr = self.Commit()
        if FAILED(hr): raise COMError(hr)
        
    def frame(self) -> tuple[BitmapFrame.Encoder, IPropertyBag2]:
        pFrame = BitmapFrame.Encoder.NULL()
        pPropbag2 = IPropertyBag2.NULL()
        hr = self.CreateNewFrame(i_cast(byref(pFrame), DOUBLE_PTR(IWICBitmapFrameEncode)), byref(pPropbag2))
        if FAILED(hr): raise COMError(hr)
        TlAddRefGuard(pFrame)
        TlAddRefGuard(pPropbag2)
        return pFrame.contents, pPropbag2.contents
    
    @classmethod
    def create(cls, format: GUID) -> 'BitmapEncoder':
        factory = ImagingFactory.instance()
        pEncoder = cls.NULL()
        hr = factory.CreateEncoder(format, NULL, i_cast(byref(pEncoder), DOUBLE_PTR(IWICBitmapEncoder)))
        if FAILED(hr): raise COMError(hr)
        TlAddRefGuard(pEncoder)
        return pEncoder.contents

class BitmapEx(Bitmap):
    @classmethod
    def from_image(self, file_name: str) -> 'BitmapEx':
        decoder = BitmapDecoder.from_filename(file_name)
        frame = decoder.frames[0]
        converter = FormatConverter()
        converter.initialize(frame, GUID_WICPixelFormat32bppBGRA)
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

class IconEx(Icon):
    def save(self, file: str | io.IOBase):
        if not isinstance(file, io.IOBase):
            stream = FileStream(file)
        else:
            stream = StreamOverIO(file)
        desc = PICTDESC()
        desc.cbSizeofStruct = desc.size()
        desc.picType = PICTYPE_ICON
        desc.icon.hicon = self
        picture = IPicture.NULL()
        hr = OleCreatePictureIndirect(desc.ref(), IPicture._iid_, False, byref(picture))
        if FAILED(hr): 
            stream.Release()
            raise COMError(hr)
        unused = LONG()
        hr = picture.contents.SaveAsFile(stream.ref(), -1, byref(unused))
        if FAILED(hr): 
            picture.contents.Release()
            stream.Release()
            raise COMError(hr)
        stream.Flush()
        picture.contents.Release()
        stream.Release()
    
    def save_ex(self, file: str | io.IOBase, format: GUID = GUID_ContainerFormatIco):
        if not isinstance(file, io.IOBase):
            file = open(file, 'wb')
        bitmap = BitmapWIC.from_icon(self)
        encoder = BitmapEncoder.create(format)
        encoder.initialize(file)
        frame, _ = encoder.frame()
        frame.initialize()
        frame.write_source(bitmap)
        frame.commit()
        encoder.commit()