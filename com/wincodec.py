#
# wincodec.py
#
# File created by WICL generator version 1.00
# Creation timestamp: Fri May  8 23:58:00 2026
# Generated from ICL: wincodec.icl
#

from win.com.ctlinterfacedef import *

WINCODEC_SDK_VERSION1 = 0x0236
WINCODEC_SDK_VERSION2 = 0x0237
CLSID_WICImagingFactory = CLSID('{cacaf262-9370-4615-a13b-9f5539da4c0a}')
CLSID_WICImagingFactory1 = CLSID('{cacaf262-9370-4615-a13b-9f5539da4c0a}')
CLSID_WICImagingFactory2 = CLSID('{317d06e8-5f24-433d-bdf7-79ce68d8abc2}')

from win.sdkddkver import *
_version = cpreproc.get_version()

if _version >= WIN32_WINNT_WIN8:
    WINCODEC_SDK_VERSION = WINCODEC_SDK_VERSION2
    CLSID_WICImagingFactory = CLSID_WICImagingFactory2
else:
    WINCODEC_SDK_VERSION = WINCODEC_SDK_VERSION1

GUID_VendorMicrosoft = GUID.string('{f0e749ca-edef-4589-a73a-ee0e626a2a2b}')
GUID_VendorMicrosoftBuiltIn = GUID.string('{257a30fd-06b6-462b-aea4-63f70b86e533}')
CLSID_WICPngDecoder = CLSID('{389ea17b-5078-4cde-b6ef-25c15175c751}')
CLSID_WICPngDecoder1 = CLSID('{389ea17b-5078-4cde-b6ef-25c15175c751}')
CLSID_WICPngDecoder2 = CLSID('{e018945b-aa86-4008-9bd4-6777a1e40c11}')
if _version >= WIN32_WINNT_WIN8:
    CLSID_WICPngDecoder = CLSID_WICPngDecoder2

CLSID_WICBmpDecoder = CLSID('{6b462062-7cbf-400d-9fdb-813dd10f2778}')
CLSID_WICIcoDecoder = CLSID('{c61bfcdf-2e0f-4aad-a8d7-e06bafebcdfe}')
CLSID_WICJpegDecoder = CLSID('{9456a480-e88b-43ea-9e73-0b2d9b71b1ca}')
CLSID_WICGifDecoder = CLSID('{381dda3c-9ce9-4834-a23e-1f98f8fc52be}')
CLSID_WICTiffDecoder = CLSID('{b54e85d9-fe23-499f-8b88-6acea713752b}')
CLSID_WICWmpDecoder = CLSID('{a26cec36-234c-4950-ae16-e34aace71d0d}')
CLSID_WICDdsDecoder = CLSID('{9053699f-a341-429d-9e90-ee437cf80c73}')
CLSID_WICBmpEncoder = CLSID('{69be8bb4-d66d-47c8-865a-ed1589433782}')
CLSID_WICPngEncoder = CLSID('{27949969-876a-41d7-9447-568f6a35a4dc}')
CLSID_WICJpegEncoder = CLSID('{1a34f5c1-4a5a-46dc-b644-1f4567e7a676}')
CLSID_WICGifEncoder = CLSID('{114f5598-0b22-40a0-86a1-c83ea495adbd}')
CLSID_WICTiffEncoder = CLSID('{0131be10-2001-4c5f-a9b0-cc88fab64ce8}')
CLSID_WICWmpEncoder = CLSID('{ac4ce3cb-e1c1-44cd-8215-5a1665509ec2}')
CLSID_WICDdsEncoder = CLSID('{a61dde94-66ce-4ac1-881b-71680588895e}')
CLSID_WICAdngDecoder = CLSID('{981d9411-909e-42a7-8f5d-a747ff052edb}')
CLSID_WICJpegQualcommPhoneEncoder = CLSID('{68ed5c62-f534-4979-b2b3-686a12b2b34c}')
CLSID_WICHeifDecoder = CLSID('{e9A4A80a-44fe-4DE4-8971-7150B10a5199}')
CLSID_WICHeifEncoder = CLSID('{0dbecec1-9eb3-4860-9c6f-ddbe86634575}')
CLSID_WICWebpDecoder = CLSID('{7693E886-51C9-4070-8419-9F70738EC8FA}')
CLSID_WICRAWDecoder = CLSID('{41945702-8302-44A6-9445-AC98E8AFA086}')
GUID_ContainerFormatBmp = GUID.string('{0af1d87e-fcfe-4188-bdeb-a7906471cbe3}')
GUID_ContainerFormatPng = GUID.string('{1b7cfaf4-713f-473c-bbcd-6137425faeaf}')
GUID_ContainerFormatIco = GUID.string('{a3a860c4-338f-4c17-919a-fba4b5628f21}')
GUID_ContainerFormatJpeg = GUID.string('{19e4a5aa-5662-4fc5-a0c0-1758028e1057}')
GUID_ContainerFormatTiff = GUID.string('{163bcc30-e2e9-4f0b-961d-a3e9fdb788a3}')
GUID_ContainerFormatGif = GUID.string('{1f8a5601-7d4d-4cbd-9c82-1bc8d4eeb9a5}')
GUID_ContainerFormatWmp = GUID.string('{57a37caa-367a-4540-916b-f183c5093a4b}')
GUID_ContainerFormatDds = GUID.string('{9967cb95-2e85-4ac8-8ca2-83d7ccd425c9}')
GUID_ContainerFormatAdng = GUID.string('{f3ff6d0d-38c0-41c4-b1fe-1f3824f17b84}')
GUID_ContainerFormatHeif = GUID.string('{e1e62521-6787-405b-a339-500715b5763f}')
GUID_ContainerFormatWebp = GUID.string('{e094b0e2-67f2-45b3-b0ea-115337ca7cf3}')
GUID_ContainerFormatRaw = GUID.string('{fe99ce60-f19c-433c-a3ae-00acefa9ca21}')
CLSID_WICImagingCategories = CLSID('{fae3d380-fea4-4623-8c75-c6b61110b681}')
CATID_WICBitmapDecoders = GUID.string('{7ed96837-96f0-4812-b211-f13c24117ed3}')
CATID_WICBitmapEncoders = GUID.string('{ac757296-3522-4e11-9862-c17be5a1767e}')
CATID_WICPixelFormats = GUID.string('{2b46e70f-cda7-473e-89f6-dc9630a2390b}')
CATID_WICFormatConverters = GUID.string('{7835eae8-bf14-49d1-93ce-533a407b2248}')
CATID_WICMetadataReader = GUID.string('{05af94d8-7174-4cd2-be4a-4124b80ee4b8}')
CATID_WICMetadataWriter = GUID.string('{abe3b9a4-257d-4b97-bd1a-294af496222e}')
CLSID_WICDefaultFormatConverter = CLSID('{1a3f11dc-b514-4b17-8c5f-2154513852f1}')
CLSID_WICFormatConverterHighColor = CLSID('{ac75d454-9f37-48f8-b972-4e19bc856011}')
CLSID_WICFormatConverterNChannel = CLSID('{c17cabb2-d4a3-47d7-a557-339b2efbd4f1}')
CLSID_WICFormatConverterWMPhoto = CLSID('{9cb5172b-d600-46ba-ab77-77bb7e3a00d9}')
CLSID_WICPlanarFormatConverter = CLSID('{184132b8-32f8-4784-9131-dd7224b23438}')
WICColor = UINT32
@CStructure.make
class WICRect(CStructure):
    X: IInt
    Y: IInt
    Width: IInt
    Height: IInt

WICColorContextUninitialized = 0
WICColorContextProfile = 1
WICColorContextExifColorSpace = 2
WICColorContextType = INT

CODEC_FORCE_DWORD = 0x7FFFFFFF
WIC_JPEG_MAX_COMPONENT_COUNT = 4
WIC_JPEG_MAX_TABLE_INDEX = 3
WIC_JPEG_SAMPLE_FACTORS_ONE = 0x00000011
WIC_JPEG_SAMPLE_FACTORS_THREE_420 = 0x00111122
WIC_JPEG_SAMPLE_FACTORS_THREE_422 = 0x00111121
WIC_JPEG_SAMPLE_FACTORS_THREE_440 = 0x00111112
WIC_JPEG_SAMPLE_FACTORS_THREE_444 = 0x00111111
WIC_JPEG_QUANTIZATION_BASELINE_ONE = 0x00000000
WIC_JPEG_QUANTIZATION_BASELINE_THREE = 0x00010100
WIC_JPEG_HUFFMAN_BASELINE_ONE = 0x00000000
WIC_JPEG_HUFFMAN_BASELINE_THREE = 0x00111100
REFWICPixelFormatGUID = REFGUID
WICPixelFormatGUID = GUID
GUID_WICPixelFormatDontCare = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc900}')
GUID_WICPixelFormatUndefined = GUID_WICPixelFormatDontCare
GUID_WICPixelFormat1bppIndexed = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc901}')
GUID_WICPixelFormat2bppIndexed = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc902}')
GUID_WICPixelFormat4bppIndexed = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc903}')
GUID_WICPixelFormat8bppIndexed = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc904}')
GUID_WICPixelFormatBlackWhite = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc905}')
GUID_WICPixelFormat2bppGray = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc906}')
GUID_WICPixelFormat4bppGray = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc907}')
GUID_WICPixelFormat8bppGray = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc908}')
GUID_WICPixelFormat8bppAlpha = GUID.string('{e6cd0116-eeba-4161-aa85-27dd9fb3a895}')
GUID_WICPixelFormat16bppBGR555 = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc909}')
GUID_WICPixelFormat16bppBGR565 = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90a}')
GUID_WICPixelFormat16bppBGRA5551 = GUID.string('{05ec7c2b-f1e6-4961-ad46-e1cc810a87d2}')
GUID_WICPixelFormat16bppGray = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90b}')
GUID_WICPixelFormat24bppBGR = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90c}')
GUID_WICPixelFormat24bppRGB = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90d}')
GUID_WICPixelFormat32bppBGR = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90e}')
GUID_WICPixelFormat32bppBGRA = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc90f}')
GUID_WICPixelFormat32bppPBGRA = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc910}')
GUID_WICPixelFormat32bppGrayFloat = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc911}')
if _version >= WIN32_WINNT_WIN8:
    GUID_WICPixelFormat32bppRGB = GUID.string('{d98c6b95-3efe-47d6-bb25-eb1748ab0cf1}')

GUID_WICPixelFormat32bppRGBA = GUID.string('{f5c7ad2d-6a8d-43dd-a7a8-a29935261ae9}')
GUID_WICPixelFormat32bppPRGBA = GUID.string('{3cc4a650-a527-4d37-a916-3142c7ebedba}')
GUID_WICPixelFormat48bppRGB = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc915}')
GUID_WICPixelFormat48bppBGR = GUID.string('{e605a384-b468-46ce-bb2e-36f180e64313}')
if _version >= WIN32_WINNT_WIN8:
    GUID_WICPixelFormat64bppRGB = GUID.string('{a1182111-186d-4d42-bc6a-9c8303a8dff9}')

GUID_WICPixelFormat64bppRGBA = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc916}')
GUID_WICPixelFormat64bppBGRA = GUID.string('{1562ff7c-d352-46f9-979e-42976b792246}')
GUID_WICPixelFormat64bppPRGBA = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc917}')
GUID_WICPixelFormat64bppPBGRA = GUID.string('{8c518e8e-a4ec-468b-ae70-c9a35a9c5530}')
GUID_WICPixelFormat16bppGrayFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc913}')
GUID_WICPixelFormat32bppBGR101010 = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc914}')
GUID_WICPixelFormat48bppRGBFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc912}')
GUID_WICPixelFormat48bppBGRFixedPoint = GUID.string('{49ca140e-cab6-493b-9ddf-60187c37532a}')
GUID_WICPixelFormat96bppRGBFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc918}')
if _version >= WIN32_WINNT_WIN8:
    GUID_WICPixelFormat96bppRGBFloat = GUID.string('{e3fed78f-e8db-4acf-84c1-e97f6136b327}')

GUID_WICPixelFormat128bppRGBAFloat = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc919}')
GUID_WICPixelFormat128bppPRGBAFloat = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91a}')
GUID_WICPixelFormat128bppRGBFloat = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91b}')
GUID_WICPixelFormat32bppCMYK = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91c}')
GUID_WICPixelFormat64bppRGBAFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91d}')
GUID_WICPixelFormat64bppBGRAFixedPoint = GUID.string('{356de33c-54d2-4a23-bb04-9b7bf9b1d42d}')
GUID_WICPixelFormat64bppRGBFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc940}')
GUID_WICPixelFormat128bppRGBAFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91e}')
GUID_WICPixelFormat128bppRGBFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc941}')
GUID_WICPixelFormat64bppRGBAHalf = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc93a}')
if _version >= WIN32_WINNT_WIN8:
    GUID_WICPixelFormat64bppPRGBAHalf = GUID.string('{58ad26c2-c623-4d9d-b320-387e49f8c442}')

GUID_WICPixelFormat64bppRGBHalf = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc942}')
GUID_WICPixelFormat48bppRGBHalf = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc93b}')
GUID_WICPixelFormat32bppRGBE = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc93d}')
GUID_WICPixelFormat16bppGrayHalf = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc93e}')
GUID_WICPixelFormat32bppGrayFixedPoint = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc93f}')
GUID_WICPixelFormat32bppRGBA1010102 = GUID.string('{25238D72-FCF9-4522-b514-5578e5ad55e0}')
GUID_WICPixelFormat32bppRGBA1010102XR = GUID.string('{00DE6B9A-C101-434b-b502-d0165ee1122c}')
GUID_WICPixelFormat32bppR10G10B10A2 = GUID.string('{604e1bb5-8a3c-4b65-b11c-bc0b8dd75b7f}')
GUID_WICPixelFormat32bppR10G10B10A2HDR10 = GUID.string('{9c215c5d-1acc-4f0e-a4bc-70fb3ae8fd28}')
GUID_WICPixelFormat64bppCMYK = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc91f}')
GUID_WICPixelFormat24bpp3Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc920}')
GUID_WICPixelFormat32bpp4Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc921}')
GUID_WICPixelFormat40bpp5Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc922}')
GUID_WICPixelFormat48bpp6Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc923}')
GUID_WICPixelFormat56bpp7Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc924}')
GUID_WICPixelFormat64bpp8Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc925}')
GUID_WICPixelFormat48bpp3Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc926}')
GUID_WICPixelFormat64bpp4Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc927}')
GUID_WICPixelFormat80bpp5Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc928}')
GUID_WICPixelFormat96bpp6Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc929}')
GUID_WICPixelFormat112bpp7Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92a}')
GUID_WICPixelFormat128bpp8Channels = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92b}')
GUID_WICPixelFormat40bppCMYKAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92c}')
GUID_WICPixelFormat80bppCMYKAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92d}')
GUID_WICPixelFormat32bpp3ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92e}')
GUID_WICPixelFormat40bpp4ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc92f}')
GUID_WICPixelFormat48bpp5ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc930}')
GUID_WICPixelFormat56bpp6ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc931}')
GUID_WICPixelFormat64bpp7ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc932}')
GUID_WICPixelFormat72bpp8ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc933}')
GUID_WICPixelFormat64bpp3ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc934}')
GUID_WICPixelFormat80bpp4ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc935}')
GUID_WICPixelFormat96bpp5ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc936}')
GUID_WICPixelFormat112bpp6ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc937}')
GUID_WICPixelFormat128bpp7ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc938}')
GUID_WICPixelFormat144bpp8ChannelsAlpha = GUID.string('{6fddc324-4e03-4bfe-b185-3d77768dc939}')
GUID_WICPixelFormat8bppY = GUID.string('{91B4DB54-2DF9-42F0-B449-2909BB3DF88E}')
GUID_WICPixelFormat8bppCb = GUID.string('{1339F224-6BFE-4C3E-9302-E4F3A6D0CA2A}')
GUID_WICPixelFormat8bppCr = GUID.string('{B8145053-2116-49F0-8835-ED844B205C51}')
GUID_WICPixelFormat16bppCbCr = GUID.string('{FF95BA6E-11E0-4263-BB45-01721F3460A4}')
GUID_WICPixelFormat16bppYQuantizedDctCoefficients = GUID.string('{A355F433-48E8-4A42-84D8-E2AA26CA80A4}')
GUID_WICPixelFormat16bppCbQuantizedDctCoefficients = GUID.string('{D2C4FF61-56A5-49C2-8B5C-4C1925964837}')
GUID_WICPixelFormat16bppCrQuantizedDctCoefficients = GUID.string('{2FE354F0-1680-42D8-9231-E73C0565BFC1}')
WICBitmapNoCache = 0
WICBitmapCacheOnDemand = 1
WICBitmapCacheOnLoad = 2
WICBITMAPCREATECACHEOPTION_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapCreateCacheOption = INT

WICDecodeMetadataCacheOnDemand = 0
WICDecodeMetadataCacheOnLoad = 1
WICMETADATACACHEOPTION_FORCE_DWORD = CODEC_FORCE_DWORD
WICDecodeOptions = INT

WICBitmapEncoderCacheInMemory = 0
WICBitmapEncoderCacheTempFile = 1
WICBitmapEncoderNoCache = 2
WICBITMAPENCODERCACHEOPTION_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapEncoderCacheOption = INT

WICDecoder = 0x00000001
WICEncoder = 0x00000002
WICPixelFormatConverter = 0x00000004
WICMetadataReader = 0x00000008
WICMetadataWriter = 0x00000010
WICPixelFormat = 0x00000020
WICAllComponents = 0x0000003F
WICCOMPONENTTYPE_FORCE_DWORD = CODEC_FORCE_DWORD
WICComponentType = INT

WICComponentEnumerateDefault = 0x00000000
WICComponentEnumerateRefresh = 0x00000001
WICComponentEnumerateDisabled = 0x80000000
WICComponentEnumerateUnsigned = 0x40000000
WICComponentEnumerateBuiltInOnly = 0x20000000
WICCOMPONENTENUMERATEOPTIONS_FORCE_DWORD = CODEC_FORCE_DWORD
WICComponentEnumerateOptions = INT

@CStructure.make
class WICBitmapPattern(CStructure):
    Position: IUlonglong
    Length: IUlong
    Pattern: PBYTE
    Mask: PBYTE
    EndOfStream: IBool64

WICBitmapInterpolationModeNearestNeighbor = 0
WICBitmapInterpolationModeLinear = 1
WICBitmapInterpolationModeCubic = 2
WICBitmapInterpolationModeFant = 3
WICBitmapInterpolationModeHighQualityCubic = 4
WICBITMAPINTERPOLATIONMODE_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapInterpolationMode = INT

WICBitmapPaletteTypeCustom = 0
WICBitmapPaletteTypeMedianCut = 1
WICBitmapPaletteTypeFixedBW = 2
WICBitmapPaletteTypeFixedHalftone8 = 3
WICBitmapPaletteTypeFixedHalftone27 = 4
WICBitmapPaletteTypeFixedHalftone64 = 5
WICBitmapPaletteTypeFixedHalftone125 = 6
WICBitmapPaletteTypeFixedHalftone216 = 7
WICBitmapPaletteTypeFixedWebPalette = WICBitmapPaletteTypeFixedHalftone216,
WICBitmapPaletteTypeFixedHalftone252 = 8
WICBitmapPaletteTypeFixedHalftone256 = 9
WICBitmapPaletteTypeFixedGray4 = 10
WICBitmapPaletteTypeFixedGray16 = 11
WICBitmapPaletteTypeFixedGray256 = 12
WICBITMAPPALETTETYPE_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapPaletteType = INT

WICBitmapDitherTypeNone = 0
WICBitmapDitherTypeSolid = 0
WICBitmapDitherTypeOrdered4x4 = 1
WICBitmapDitherTypeOrdered8x8 = 2
WICBitmapDitherTypeOrdered16x16 = 3
WICBitmapDitherTypeSpiral4x4 = 4
WICBitmapDitherTypeSpiral8x8 = 5
WICBitmapDitherTypeDualSpiral4x4 = 6
WICBitmapDitherTypeDualSpiral8x8 = 7
WICBitmapDitherTypeErrorDiffusion = 8
WICBITMAPDITHERTYPE_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapDitherType = INT

WICBitmapUseAlpha = 0
WICBitmapUsePremultipliedAlpha = 1
WICBitmapIgnoreAlpha = 2
WICBITMAPALPHACHANNELOPTIONS_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapAlphaChannelOption = INT

WICBitmapTransformRotate0 = 0
WICBitmapTransformRotate90 = 1
WICBitmapTransformRotate180 = 2
WICBitmapTransformRotate270 = 3
WICBitmapTransformFlipHorizontal = 8
WICBitmapTransformFlipVertical = 16
WICBITMAPTRANSFORMOPTIONS_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapTransformOptions = INT

WICBitmapLockRead = 1
WICBitmapLockWrite = 2
WICBITMAPLOCKFLAGS_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapLockFlags = INT

WICBitmapDecoderCapabilitySameEncoder = 1
WICBitmapDecoderCapabilityCanDecodeAllImages = 2
WICBitmapDecoderCapabilityCanDecodeSomeImages = 4
WICBitmapDecoderCapabilityCanEnumerateMetadata = 8
WICBitmapDecoderCapabilityCanDecodeThumbnail = 16
WICBITMAPDECODERCAPABILITIES_FORCE_DWORD = CODEC_FORCE_DWORD
WICBitmapDecoderCapabilities = INT

WICProgressOperationCopyPixels = 0x00000001
WICProgressOperationWritePixels = 0x00000002
WICProgressOperationAll = 0x0000FFFF
WICPROGRESSOPERATION_FORCE_DWORD = CODEC_FORCE_DWORD
WICProgressOperation = INT

WICProgressNotificationBegin = 0x00010000
WICProgressNotificationEnd = 0x00020000
WICProgressNotificationFrequent = 0x00040000
WICProgressNotificationAll = 0xFFFF0000
WICPROGRESSNOTIFICATION_FORCE_DWORD = CODEC_FORCE_DWORD
WICProgressNotification = INT

WICComponentSigned = 0x00000001
WICComponentUnsigned = 0x00000002
WICComponentSafe = 0x00000004
WICComponentDisabled = 0x80000000
WICCOMPONENTSIGNING_FORCE_DWORD = CODEC_FORCE_DWORD
WICComponentSigning = INT

WICGifLogicalScreenSignature = 1
WICGifLogicalScreenDescriptorWidth = 2
WICGifLogicalScreenDescriptorHeight = 3
WICGifLogicalScreenDescriptorGlobalColorTableFlag = 4
WICGifLogicalScreenDescriptorColorResolution = 5
WICGifLogicalScreenDescriptorSortFlag = 6
WICGifLogicalScreenDescriptorGlobalColorTableSize = 7
WICGifLogicalScreenDescriptorBackgroundColorIndex = 8
WICGifLogicalScreenDescriptorPixelAspectRatio = 9
WICGifLogicalScreenDescriptorProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICGifLogicalScreenDescriptorProperties = INT

WICGifImageDescriptorLeft = 1
WICGifImageDescriptorTop = 2
WICGifImageDescriptorWidth = 3
WICGifImageDescriptorHeight = 4
WICGifImageDescriptorLocalColorTableFlag = 5
WICGifImageDescriptorInterlaceFlag = 6
WICGifImageDescriptorSortFlag = 7
WICGifImageDescriptorLocalColorTableSize = 8
WICGifImageDescriptorProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICGifImageDescriptorProperties = INT

WICGifGraphicControlExtensionDisposal = 1
WICGifGraphicControlExtensionUserInputFlag = 2
WICGifGraphicControlExtensionTransparencyFlag = 3
WICGifGraphicControlExtensionDelay = 4
WICGifGraphicControlExtensionTransparentColorIndex = 5
WICGifGraphicControlExtensionProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICGifGraphicControlExtensionProperties = INT

WICGifApplicationExtensionApplication = 1
WICGifApplicationExtensionData = 2
WICGifApplicationExtensionProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICGifApplicationExtensionProperties = INT

WICGifCommentExtensionText = 1
WICGifCommentExtensionProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICGifCommentExtensionProperties = INT

WICJpegCommentText = 1
WICJpegCommentProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegCommentProperties = INT

WICJpegLuminanceTable = 1
WICJpegLuminanceProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegLuminanceProperties = INT

WICJpegChrominanceTable = 1
WICJpegChrominanceProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegChrominanceProperties = INT

WIC8BIMIptcPString = 0
WIC8BIMIptcEmbeddedIPTC = 1
WIC8BIMIptcProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WIC8BIMIptcProperties = INT

WIC8BIMResolutionInfoPString = 1
WIC8BIMResolutionInfoHResolution = 2
WIC8BIMResolutionInfoHResolutionUnit = 3
WIC8BIMResolutionInfoWidthUnit = 4
WIC8BIMResolutionInfoVResolution = 5
WIC8BIMResolutionInfoVResolutionUnit = 6
WIC8BIMResolutionInfoHeightUnit = 7
WIC8BIMResolutionInfoProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WIC8BIMResolutionInfoProperties = INT

WIC8BIMIptcDigestPString = 1
WIC8BIMIptcDigestIptcDigest = 2
WIC8BIMIptcDigestProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WIC8BIMIptcDigestProperties = INT

WICPngGamaGamma = 1
WICPngGamaProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngGamaProperties = INT

WICPngBkgdBackgroundColor = 1
WICPngBkgdProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngBkgdProperties = INT

WICPngItxtKeyword = 1
WICPngItxtCompressionFlag = 2
WICPngItxtLanguageTag = 3
WICPngItxtTranslatedKeyword = 4
WICPngItxtText = 5
WICPngItxtProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngItxtProperties = INT

WICPngChrmWhitePointX = 1
WICPngChrmWhitePointY = 2
WICPngChrmRedX = 3
WICPngChrmRedY = 4
WICPngChrmGreenX = 5
WICPngChrmGreenY = 6
WICPngChrmBlueX = 7
WICPngChrmBlueY = 8
WICPngChrmProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngChrmProperties = INT

WICPngHistFrequencies = 1
WICPngHistProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngHistProperties = INT

WICPngIccpProfileName = 1
WICPngIccpProfileData = 2
WICPngIccpProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngIccpProperties = INT

WICPngSrgbRenderingIntent = 1
WICPngSrgbProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngSrgbProperties = INT

WICPngTimeYear = 1
WICPngTimeMonth = 2
WICPngTimeDay = 3
WICPngTimeHour = 4
WICPngTimeMinute = 5
WICPngTimeSecond = 6
WICPngTimeProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngTimeProperties = INT

WICHeifOrientation = 1
WICHeifProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICHeifProperties = INT

WICHeifHdrMaximumLuminanceLevel = 1
WICHeifHdrMaximumFrameAverageLuminanceLevel = 2
WICHeifHdrMinimumMasteringDisplayLuminanceLevel = 3
WICHeifHdrMaximumMasteringDisplayLuminanceLevel = 4
WICHeifHdrCustomVideoPrimaries = 5
WICHeifHdrProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICHeifHdrProperties = INT

WICWebpAnimLoopCount = 1
WICWebpAnimProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICWebpAnimProperties = INT

WICWebpAnmfFrameDuration = 1
WICWebpAnmfProperties_FORCE_DWORD = CODEC_FORCE_DWORD
WICWebpAnmfProperties = INT

WICSectionAccessLevelRead = 1
WICSectionAccessLevelReadWrite = 3
WICSectionAccessLevel_FORCE_DWORD = CODEC_FORCE_DWORD
WICSectionAccessLevel = INT

WICPixelFormatNumericRepresentationUnspecified = 0
WICPixelFormatNumericRepresentationIndexed = 1
WICPixelFormatNumericRepresentationUnsignedInteger = 2
WICPixelFormatNumericRepresentationSignedInteger = 3
WICPixelFormatNumericRepresentationFixed = 4
WICPixelFormatNumericRepresentationFloat = 5
WICPixelFormatNumericRepresentation_FORCE_DWORD = CODEC_FORCE_DWORD
WICPixelFormatNumericRepresentation = INT

WICPlanarOptionsDefault = 0
WICPlanarOptionsPreserveSubsampling = 1
WICPLANAROPTIONS_FORCE_DWORD = CODEC_FORCE_DWORD
WICPlanarOptions = INT

WICJpegIndexingOptionsGenerateOnDemand = 0
WICJpegIndexingOptionsGenerateOnLoad = 1
WICJpegIndexingOptions_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegIndexingOptions = INT

WICJpegTransferMatrixIdentity = 0
WICJpegTransferMatrixBT601 = 1
WICJpegTransferMatrix_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegTransferMatrix = INT

WICJpegScanTypeInterleaved = 0
WICJpegScanTypePlanarComponents = 1
WICJpegScanTypeProgressive = 2
WICJpegScanType_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegScanType = INT

@CStructure.make
class D2D1_PIXEL_FORMAT(CStructure):
    format: IInt
    alphaMode: IInt

if _version >= WIN32_WINNT_WIN8:
    @CStructure.make
    class WICImageParameters(CStructure):
        PixelFormat: D2D1_PIXEL_FORMAT
        DpiX: IFloat
        DpiY: IFloat
        Top: IFloat
        Left: IFloat
        PixelWidth: IUint32
        PixelHeight: IUint32


@CStructure.make
class WICBitmapPlaneDescription(CStructure):
    Format: WICPixelFormatGUID
    Width: IUint
    Height: IUint

@CStructure.make
class WICBitmapPlane(CStructure):
    Format: WICPixelFormatGUID
    pbBuffer: PBYTE
    cbStride: IUint
    cbBufferSize: IUint

@CStructure.make
class WICJpegFrameHeader(CStructure):
    Width: IUint
    Height: IUint
    TransferMatrix: IInteger[WICJpegTransferMatrix]
    ScanType: IInteger[WICJpegScanType]
    cComponents: IUint
    ComponentIdentifiers: IDword
    SampleFactors: IDword
    QuantizationTableIndices: IDword

@CStructure.make
class WICJpegScanHeader(CStructure):
    cComponents: IUint
    RestartInterval: IUint
    ComponentSelectors: IDword
    HuffmanTableIndices: IDword
    StartSpectralSelection: IByte
    EndSpectralSelection: IByte
    SuccessiveApproximationHigh: IByte
    SuccessiveApproximationLow: IByte

class IWICPalette(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00000040-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(WICBitmapPaletteType, BOOL)
    def InitializePredefined(self, ePaletteType: int, fAddTransparentColor: bool) -> int: ...

    @virtual_table.com_function(PTR(WICColor), UINT)
    def InitializeCustom(self, pColors: IPointer[WICColor], cCount: int) -> int: ...

    @virtual_table.com_function(PVOID, UINT, BOOL)
    def InitializeFromBitmap(self, pISurface: IPointer['IWICBitmapSource'], cCount: int, fAddTransparentColor: bool) -> int: ...

    @virtual_table.com_function(PVOID)
    def InitializeFromPalette(self, pIPalette: IPointer['IWICPalette']) -> int: ...

    @virtual_table.com_function(PTR(WICBitmapPaletteType))
    def GetType(self, pePaletteType: IPointer[WICBitmapPaletteType]) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetColorCount(self, pcCount: PUINT) -> int: ...

    @virtual_table.com_function(UINT, PTR(WICColor), PUINT)
    def GetColors(self, cCount: int, pColors: IPointer[WICColor], pcActualColors: PUINT) -> int: ...

    @virtual_table.com_function(PBOOL)
    def IsBlackWhite(self, pfIsBlackWhite: PBOOL) -> int: ...

    @virtual_table.com_function(PBOOL)
    def IsGrayscale(self, pfIsGrayscale: PBOOL) -> int: ...

    @virtual_table.com_function(PBOOL)
    def HasAlpha(self, pfHasAlpha: PBOOL) -> int: ...

    virtual_table.build()

class IWICBitmapSource(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00000120-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PUINT, PUINT)
    def GetSize(self, puiWidth: PUINT, puiHeight: PUINT) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID))
    def GetPixelFormat(self, pPixelFormat: IPointer[WICPixelFormatGUID]) -> int: ...

    @virtual_table.com_function(PTR(DOUBLE), PTR(DOUBLE))
    def GetResolution(self, pDpiX: IPointer[DOUBLE], pDpiY: IPointer[DOUBLE]) -> int: ...

    @virtual_table.com_function(PTR(IWICPalette))
    def CopyPalette(self, pIPalette: IPointer[IWICPalette]) -> int: ...

    @virtual_table.com_function(PTR(WICRect), UINT, UINT, PBYTE)
    def CopyPixels(self, prc: IPointer[WICRect], cbStride: int, cbBufferSize: int, pbBuffer: PBYTE) -> int: ...

    virtual_table.build()

class IWICFormatConverter(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{00000301-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PTR(IWICBitmapSource), PTR(WICPixelFormatGUID), WICBitmapDitherType, PTR(IWICPalette), DOUBLE, WICBitmapPaletteType)
    def Initialize(self, pISource: IPointer[IWICBitmapSource], dstFormat: IPointer[WICPixelFormatGUID], dither: int, pIPalette: IPointer[IWICPalette], alphaThresholdPercent: float, paletteTranslate: int) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID), PTR(WICPixelFormatGUID), PBOOL)
    def CanConvert(self, srcPixelFormat: IPointer[WICPixelFormatGUID], dstPixelFormat: IPointer[WICPixelFormatGUID], pfCanConvert: PBOOL) -> int: ...

    virtual_table.build()

class IWICPlanarFormatConverter(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{BEBEE9CB-83B0-4DCC-8132-B0AAA55EAC96}")

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapSource), UINT, PTR(WICPixelFormatGUID), WICBitmapDitherType, PTR(IWICPalette), DOUBLE, WICBitmapPaletteType)
    def Initialize(self, ppPlanes: IDoublePtr[IWICBitmapSource], cPlanes: int, dstFormat: IPointer[WICPixelFormatGUID], dither: int, pIPalette: IPointer[IWICPalette], alphaThresholdPercent: float, paletteTranslate: int) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID), UINT, PTR(WICPixelFormatGUID), PBOOL)
    def CanConvert(self, pSrcPixelFormats: IPointer[WICPixelFormatGUID], cSrcPlanes: int, dstPixelFormat: IPointer[WICPixelFormatGUID], pfCanConvert: PBOOL) -> int: ...

    virtual_table.build()

class IWICBitmapScaler(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{00000302-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PTR(IWICBitmapSource), UINT, UINT, WICBitmapInterpolationMode)
    def Initialize(self, pISource: IPointer[IWICBitmapSource], uiWidth: int, uiHeight: int, mode: int) -> int: ...

    virtual_table.build()

class IWICBitmapClipper(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{E4FBCF03-223D-4e81-9333-D635556DD1B5}")

    @virtual_table.com_function(PTR(IWICBitmapSource), PTR(WICRect))
    def Initialize(self, pISource: IPointer[IWICBitmapSource], prc: IPointer[WICRect]) -> int: ...

    virtual_table.build()

class IWICBitmapFlipRotator(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{5009834F-2D6A-41ce-9E1B-17C5AFF7A782}")

    @virtual_table.com_function(PTR(IWICBitmapSource), WICBitmapTransformOptions)
    def Initialize(self, pISource: IPointer[IWICBitmapSource], options: int) -> int: ...

    virtual_table.build()

class IWICBitmapLock(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00000123-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PUINT, PUINT)
    def GetSize(self, puiWidth: PUINT, puiHeight: PUINT) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetStride(self, pcbStride: PUINT) -> int: ...

    @virtual_table.com_function(PUINT, PTR(PBYTE))
    def GetDataPointer(self, pcbBufferSize: PUINT, ppbData: IPointer[PBYTE]) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID))
    def GetPixelFormat(self, pPixelFormat: IPointer[WICPixelFormatGUID]) -> int: ...

    virtual_table.build()

class IWICBitmap(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{00000121-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PTR(WICRect), DWORD, DOUBLE_PTR(IWICBitmapLock))
    def Lock(self, prcLock: IPointer[WICRect], flags: int, ppILock: IDoublePtr[IWICBitmapLock]) -> int: ...

    @virtual_table.com_function(PTR(IWICPalette))
    def SetPalette(self, pIPalette: IPointer[IWICPalette]) -> int: ...

    @virtual_table.com_function(DOUBLE, DOUBLE)
    def SetResolution(self, dpiX: float, dpiY: float) -> int: ...

    virtual_table.build()

class IWICColorContext(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{3C613A02-34B2-44ea-9A7C-45AEA9C6FD6D}")

    @virtual_table.com_function(LPCWSTR)
    def InitializeFromFilename(self, wzFilename: LPCWSTR) -> int: ...

    @virtual_table.com_function(PBYTE, UINT)
    def InitializeFromMemory(self, pbBuffer: PBYTE, cbBufferSize: int) -> int: ...

    @virtual_table.com_function(UINT)
    def InitializeFromExifColorSpace(self, value: int) -> int: ...

    @virtual_table.com_function(PTR(WICColorContextType))
    def GetType(self, pType: IPointer[WICColorContextType]) -> int: ...

    @virtual_table.com_function(UINT, PBYTE, PUINT)
    def GetProfileBytes(self, cbBuffer: int, pbBuffer: PBYTE, pcbActual: PUINT) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetExifColorSpace(self, pValue: PUINT) -> int: ...

    virtual_table.build()

class IWICColorTransform(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{B66F034F-D0E2-40ab-B436-6DE39E321A94}")

    @virtual_table.com_function(PTR(IWICBitmapSource), PTR(IWICColorContext), PTR(IWICColorContext), PTR(WICPixelFormatGUID))
    def Initialize(self, pIBitmapSource: IPointer[IWICBitmapSource], pIContextSource: IPointer[IWICColorContext], pIContextDest: IPointer[IWICColorContext], pixelFmtDest: IPointer[WICPixelFormatGUID]) -> int: ...

    virtual_table.build()

class IWICFastMetadataEncoder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{B84E2C09-78C9-4AC4-8BD3-524AE1663A2F}")

    @virtual_table.com_function()
    def Commit(self) -> int: ...

    @virtual_table.com_function(PVOID)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: IDoublePtr['IWICMetadataQueryWriter']) -> int: ...

    virtual_table.build()

class IWICStream(IStream):
    virtual_table = COMVirtualTable.from_ancestor(IStream)
    _iid_ = IID("{135FF860-22B7-4ddf-B0F6-218F4F299A43}")

    @virtual_table.com_function(LPSTREAM)
    def InitializeFromIStream(self, pIStream: IPointer[IStream]) -> int: ...

    @virtual_table.com_function(LPCWSTR, DWORD)
    def InitializeFromFilename(self, wzFileName: LPCWSTR, dwDesiredAccess: int) -> int: ...

    @virtual_table.com_function(PBYTE, DWORD)
    def InitializeFromMemory(self, pbBuffer: PBYTE, cbBufferSize: int) -> int: ...

    @virtual_table.com_function(LPSTREAM, ULONGLONG, ULONGLONG)
    def InitializeFromIStreamRegion(self, pIStream: IPointer[IStream], ulOffset: ULONGLONG, ulMaxSize: ULONGLONG) -> int: ...

    virtual_table.build()

class IWICBitmapEncoder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00000103-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(LPSTREAM, WICBitmapEncoderCacheOption)
    def Initialize(self, pIStream: IPointer[IStream], cacheOption: int) -> int: ...

    @virtual_table.com_function(LPGUID)
    def GetContainerFormat(self, pguidContainerFormat: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(PVOID)
    def GetEncoderInfo(self, ppIEncoderInfo: IDoublePtr['IWICBitmapEncoderInfo']) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICColorContext))
    def SetColorContexts(self, ppIColorContext: IDoublePtr[IWICColorContext]) -> int: ...

    @virtual_table.com_function(PTR(IWICPalette))
    def SetPalette(self, pIPalette: IPointer[IWICPalette]) -> int: ...

    @virtual_table.com_function(PTR(IWICBitmapSource))
    def SetThumbnail(self, pIThumbnail: IPointer[IWICBitmapSource]) -> int: ...

    @virtual_table.com_function(PTR(IWICBitmapSource))
    def SetPreview(self, pIPreview: IPointer[IWICBitmapSource]) -> int: ...

    @virtual_table.com_function(PVOID, DOUBLE_PTR(IPropertyBag2))
    def CreateNewFrame(self, ppIFrameEncode: IDoublePtr['IWICBitmapFrameEncode'], ppIEncoderOptions: IDoublePtr[IPropertyBag2]) -> int: ...

    @virtual_table.com_function()
    def Commit(self) -> int: ...

    @virtual_table.com_function(PVOID, PVOID)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: IPointer[PVOID]) -> int: ...

    virtual_table.build()

class IWICBitmapFrameEncode(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{00000105-a8f2-4877-ba0a-fd2b6645fb94}")

    @virtual_table.com_function(PTR(IPropertyBag2))
    def Initialize(self, pIEncoderOptions: IPointer[IPropertyBag2]) -> int: ...

    @virtual_table.com_function(UINT, UINT)
    def SetSize(self, uiWidth: int, uiHeight: int) -> int: ...

    @virtual_table.com_function(DOUBLE, DOUBLE)
    def SetResolution(self, dpiX: float, dpiY: float) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID))
    def SetPixelFormat(self, pPixelFormat: IPointer[WICPixelFormatGUID]) -> int: ...

    @virtual_table.com_function(UINT, DOUBLE_PTR(IWICColorContext))
    def SetColorContexts(self, cCount: int, ppIColorContext: IDoublePtr[IWICColorContext]) -> int: ...

    @virtual_table.com_function(PTR(IWICPalette))
    def SetPalette(self, pIPalette: IPointer[IWICPalette]) -> int: ...

    @virtual_table.com_function(PTR(IWICBitmapSource))
    def SetThumbnail(self, pIThumbnail: IPointer[IWICBitmapSource]) -> int: ...

    @virtual_table.com_function(UINT, UINT, UINT, PBYTE)
    def WritePixels(self, lineCount: int, cbStride: int, cbBufferSize: int, pbBixels: PBYTE) -> int: ...

    @virtual_table.com_function()
    def Commit(self) -> int: ...

    @virtual_table.com_function(PVOID, PVOID)
    def GetMetadataQueryWriter(self, ppIMetadataQueryWriter: IPointer[PVOID]) -> int: ...

    virtual_table.build()

class IWICPlanarBitmapFrameEncode(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{F928B7B8-2221-40C1-B72E-7E82F1974D1A}")

    @virtual_table.com_function(UINT, PTR(WICBitmapPlane), UINT)
    def WritePixels(self, lineCount: int, pPlanes: IPointer[WICBitmapPlane], cPlanes: int) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapSource), UINT, PTR(WICRect))
    def WriteSource(self, ppPlanes: IDoublePtr[IWICBitmapSource], cPlanes: int, prcSource: IPointer[WICRect]) -> int: ...

    virtual_table.build()

class IWICBitmapDecoder(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{9EDDE9E7-8DEE-47ea-99DF-E6FAF2ED44BF}")

    @virtual_table.com_function(LPSTREAM, PDWORD)
    def QueryCapability(self, pIStream: IPointer[IStream], pdwCapability: PDWORD) -> int: ...

    @virtual_table.com_function(LPSTREAM, WICDecodeOptions)
    def Initialize(self, pIStream: IPointer[IStream], cacheOptions: int) -> int: ...

    @virtual_table.com_function(LPGUID)
    def GetContainerFormat(self, pguidContainerFormat: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(PVOID)
    def GetDecoderInfo(self, ppIDecoderInfo: IDoublePtr['IWICBitmapDecoderInfo']) -> int: ...

    @virtual_table.com_function(PTR(IWICPalette))
    def CopyPalette(self, pIPalette: IPointer[IWICPalette]) -> int: ...

    @virtual_table.com_function(PVOID, PVOID)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapSource))
    def GetPreview(self, ppIBitmapSource: IDoublePtr[IWICBitmapSource]) -> int: ...

    @virtual_table.com_function(UINT, DOUBLE_PTR(IWICColorContext), PUINT)
    def GetColorContexts(self, cCount: int, ppIColorContexts: IDoublePtr[IWICColorContext], pcActualCount: PUINT) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapSource))
    def GetThumbnail(self, ppIThumbnail: IDoublePtr[IWICBitmapSource]) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetFrameCount(self, pCount: PUINT) -> int: ...

    @virtual_table.com_function(UINT, PVOID)
    def GetFrame(self, index: int, ppIBitmapFrame: IDoublePtr['IWICBitmapFrameDecode']) -> int: ...

    virtual_table.build()

class IWICBitmapSourceTransform(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{3B16811B-6A43-4ec9-B713-3D5A0C13B940}")

    @virtual_table.com_function(PTR(WICRect), UINT, UINT, PTR(WICPixelFormatGUID), WICBitmapTransformOptions, UINT, UINT, PBYTE)
    def CopyPixels(self, prc: IPointer[WICRect], uiWidth: int, uiHeight: int, pguidDstFormat: IPointer[WICPixelFormatGUID], dstTransform: int, nStride: int, cbBufferSize: int, pbBuffer: PBYTE) -> int: ...

    @virtual_table.com_function(PUINT, PUINT)
    def GetClosestSize(self, puiWidth: PUINT, puiHeight: PUINT) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatGUID))
    def GetClosestPixelFormat(self, pguidDstFormat: IPointer[WICPixelFormatGUID]) -> int: ...

    @virtual_table.com_function(WICBitmapTransformOptions, PBOOL)
    def DoesSupportTransform(self, dstTransform: int, pfIsSupported: PBOOL) -> int: ...

    virtual_table.build()

class IWICPlanarBitmapSourceTransform(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{3AFF9CCE-BE95-4303-B927-E7D16FF4A613}")

    @virtual_table.com_function(PUINT, PUINT, WICBitmapTransformOptions, WICPlanarOptions, PTR(WICPixelFormatGUID), PTR(WICBitmapPlaneDescription), UINT, PBOOL)
    def DoesSupportTransform(self, puiWidth: PUINT, puiHeight: PUINT, dstTransform: int, dstPlanarOptions: int, pguidDstFormats: IPointer[WICPixelFormatGUID], pPlaneDescriptions: IPointer[WICBitmapPlaneDescription], cPlanes: int, pfIsSupported: PBOOL) -> int: ...

    @virtual_table.com_function(PTR(WICRect), UINT, UINT, WICBitmapTransformOptions, WICPlanarOptions, PTR(WICBitmapPlane), UINT)
    def CopyPixels(self, prcSource: IPointer[WICRect], uiWidth: int, uiHeight: int, dstTransform: int, dstPlanarOptions: int, pDstPlanes: IPointer[WICBitmapPlane], cPlanes: int) -> int: ...

    virtual_table.build()

class IWICBitmapFrameDecode(IWICBitmapSource):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapSource)
    _iid_ = IID("{3B16811B-6A43-4ec9-A813-3D930C13B940}")

    @virtual_table.com_function(PVOID, PVOID)
    def GetMetadataQueryReader(self, ppIMetadataQueryReader: IPointer[PVOID]) -> int: ...

    @virtual_table.com_function(UINT, DOUBLE_PTR(IWICColorContext), PUINT)
    def GetColorContexts(self, cCount: int, ppIColorContexts: IDoublePtr[IWICColorContext], pcActualCount: PUINT) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapSource))
    def GetThumbnail(self, ppIThumbnail: IDoublePtr[IWICBitmapSource]) -> int: ...

    virtual_table.build()

class IWICProgressiveLevelControl(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{DAAC296F-7AA5-4dbf-8D15-225C5976F891}")

    @virtual_table.com_function(PUINT)
    def GetLevelCount(self, pcLevels: PUINT) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetCurrentLevel(self, pnLevel: PUINT) -> int: ...

    @virtual_table.com_function(UINT)
    def SetCurrentLevel(self, nLevel: int) -> int: ...

    virtual_table.build()

class IWICProgressCallback(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{4776F9CD-9517-45FA-BF24-E89C5EC5C60C}")

    @virtual_table.com_function(ULONG, WICProgressOperation, DOUBLE)
    def Notify(self, uFrameNum: int, operation: int, dblProgress: float) -> int: ...

    virtual_table.build()


PFNProgressNotification = WINAPI(HRESULT, LPVOID, ULONG, WICProgressOperation, DOUBLE)

class IWICBitmapCodecProgressNotification(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{64C1024E-C3CF-4462-8078-88C2B11C46D9}")

    @virtual_table.com_function(PFNProgressNotification, LPVOID, DWORD)
    def RegisterProgressNotification(self, pfnProgressNotification: PFNProgressNotification, pvData: LPVOID, dwProgressFlags: int) -> int: ...

    virtual_table.build()

class IWICComponentInfo(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{23BC3F0A-698B-4357-886B-F24D50671334}")

    @virtual_table.com_function(PTR(WICComponentType))
    def GetComponentType(self, pType: IPointer[WICComponentType]) -> int: ...

    @virtual_table.com_function(LPCLSID)
    def GetCLSID(self, pclsid: IPointer[CLSID]) -> int: ...

    @virtual_table.com_function(PDWORD)
    def GetSigningStatus(self, pStatus: PDWORD) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetAuthor(self, cchAuthor: int, wzAuthor: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(LPGUID)
    def GetVendorGUID(self, pguidVendor: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetVersion(self, cchVersion: int, wzVersion: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetSpecVersion(self, cchSpecVersion: int, wzSpecVersion: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetFriendlyName(self, cchFriendlyName: int, wzFriendlyName: LPWSTR, pcchActual: PUINT) -> int: ...

    virtual_table.build()

class IWICFormatConverterInfo(IWICComponentInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICComponentInfo)
    _iid_ = IID("{9F34FB65-13F4-4f15-BC57-3726B5E53D9F}")

    @virtual_table.com_function(UINT, PTR(WICPixelFormatGUID), PUINT)
    def GetPixelFormats(self, cFormats: int, pPixelFormatGUIDs: IPointer[WICPixelFormatGUID], pcActual: PUINT) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICFormatConverter))
    def CreateInstance(self, ppIConverter: IDoublePtr[IWICFormatConverter]) -> int: ...

    virtual_table.build()

class IWICBitmapCodecInfo(IWICComponentInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICComponentInfo)
    _iid_ = IID("{E87A44C4-B76E-4c47-8B09-298EB12A2714}")

    @virtual_table.com_function(LPGUID)
    def GetContainerFormat(self, pguidContainerFormat: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(UINT, LPGUID, PUINT)
    def GetPixelFormats(self, cFormats: int, pguidPixelFormats: IPointer[GUID], pcActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetColorManagementVersion(self, cchColorManagementVersion: int, wzColorManagementVersion: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetDeviceManufacturer(self, cchDeviceManufacturer: int, wzDeviceManufacturer: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetDeviceModels(self, cchDeviceModels: int, wzDeviceModels: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetMimeTypes(self, cchMimeTypes: int, wzMimeTypes: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(UINT, LPWSTR, PUINT)
    def GetFileExtensions(self, cchFileExtensions: int, wzFileExtensions: LPWSTR, pcchActual: PUINT) -> int: ...

    @virtual_table.com_function(PBOOL)
    def DoesSupportAnimation(self, pfSupportAnimation: PBOOL) -> int: ...

    @virtual_table.com_function(PBOOL)
    def DoesSupportChromakey(self, pfSupportChromakey: PBOOL) -> int: ...

    @virtual_table.com_function(PBOOL)
    def DoesSupportLossless(self, pfSupportLossless: PBOOL) -> int: ...

    @virtual_table.com_function(PBOOL)
    def DoesSupportMultiframe(self, pfSupportMultiframe: PBOOL) -> int: ...

    @virtual_table.com_function(LPCWSTR, PBOOL)
    def MatchesMimeType(self, wzMimeType: LPCWSTR, pfMatches: PBOOL) -> int: ...

    virtual_table.build()

class IWICBitmapEncoderInfo(IWICBitmapCodecInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapCodecInfo)
    _iid_ = IID("{94C9B4EE-A09F-4f92-8A1E-4A9BCE7E76FB}")

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapEncoder))
    def CreateInstance(self, ppIBitmapEncoder: IDoublePtr[IWICBitmapEncoder]) -> int: ...

    virtual_table.build()

class IWICBitmapDecoderInfo(IWICBitmapCodecInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICBitmapCodecInfo)
    _iid_ = IID("{D8CD007F-D08F-4191-9BFC-236EA7F0E4B5}")

    @virtual_table.com_function(UINT, PTR(WICBitmapPattern), PUINT, PUINT)
    def GetPatterns(self, cbSizePatterns: int, pPatterns: IPointer[WICBitmapPattern], pcPatterns: PUINT, pcbPatternsActual: PUINT) -> int: ...

    @virtual_table.com_function(LPSTREAM, PBOOL)
    def MatchesPattern(self, pIStream: IPointer[IStream], pfMatches: PBOOL) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapDecoder))
    def CreateInstance(self, ppIBitmapDecoder: IDoublePtr[IWICBitmapDecoder]) -> int: ...

    virtual_table.build()

class IWICPixelFormatInfo(IWICComponentInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICComponentInfo)
    _iid_ = IID("{E8EDA601-3D48-431a-AB44-69059BE88BBE}")

    @virtual_table.com_function(LPGUID)
    def GetFormatGUID(self, pFormat: IPointer[GUID]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICColorContext))
    def GetColorContext(self, ppIColorContext: IDoublePtr[IWICColorContext]) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetBitsPerPixel(self, puiBitsPerPixel: PUINT) -> int: ...

    @virtual_table.com_function(PUINT)
    def GetChannelCount(self, puiChannelCount: PUINT) -> int: ...

    @virtual_table.com_function(UINT, UINT, PBYTE, PUINT)
    def GetChannelMask(self, uiChannelIndex: int, cbMaskBuffer: int, pbMaskBuffer: PBYTE, pcbActual: PUINT) -> int: ...

    virtual_table.build()

class IWICPixelFormatInfo2(IWICPixelFormatInfo):
    virtual_table = COMVirtualTable.from_ancestor(IWICPixelFormatInfo)
    _iid_ = IID("{A9DB33A2-AF5F-43C7-B679-74F5984B5AA4}")

    @virtual_table.com_function(PBOOL)
    def SupportsTransparency(self, pfSupportsTransparency: PBOOL) -> int: ...

    @virtual_table.com_function(PTR(WICPixelFormatNumericRepresentation))
    def GetNumericRepresentation(self, pNumericRepresentation: IPointer[WICPixelFormatNumericRepresentation]) -> int: ...

    virtual_table.build()

class IWICImagingFactory(IUnknown):
    virtual_table = COMVirtualTable.from_ancestor(IUnknown)
    _iid_ = IID("{ec5ec8a9-c395-4314-9c77-54d7a935ff70}")

    @virtual_table.com_function(LPCWSTR, LPGUID, DWORD, WICDecodeOptions, DOUBLE_PTR(IWICBitmapDecoder))
    def CreateDecoderFromFilename(self, wzFilename: LPCWSTR, pguidVendor: IPointer[GUID], dwDesiredAccess: int, metadataOptions: int, ppIDecoder: IDoublePtr[IWICBitmapDecoder]) -> int: ...

    @virtual_table.com_function(LPSTREAM, LPGUID, WICDecodeOptions, DOUBLE_PTR(IWICBitmapDecoder))
    def CreateDecoderFromStream(self, pIStream: IPointer[IStream], pguidVendor: IPointer[GUID], metadataOptions: int, ppIDecoder: IDoublePtr[IWICBitmapDecoder]) -> int: ...

    @virtual_table.com_function(ULONG_PTR, LPGUID, WICDecodeOptions, DOUBLE_PTR(IWICBitmapDecoder))
    def CreateDecoderFromFileHandle(self, hFile: int, pguidVendor: IPointer[GUID], metadataOptions: int, ppIDecoder: IDoublePtr[IWICBitmapDecoder]) -> int: ...

    @virtual_table.com_function(LPCLSID, DOUBLE_PTR(IWICComponentInfo), intermediate_method = True)
    def CreateComponentInfo(self, clsidComponent: CLSID, ppIInfo: IDoublePtr[IWICComponentInfo], **kwargs) -> int:
        return self.virt_delegate(clsidComponent.ref() if clsidComponent else NULL, ppIInfo)

    @virtual_table.com_function(LPGUID, LPGUID, DOUBLE_PTR(IWICBitmapDecoder), intermediate_method = True)
    def CreateDecoder(self, guidContainerFormat: GUID, pguidVendor: IPointer[GUID], ppIDecoder: IDoublePtr[IWICBitmapDecoder], **kwargs) -> int:
        return self.virt_delegate(guidContainerFormat.ref() if guidContainerFormat else NULL, pguidVendor, ppIDecoder)

    @virtual_table.com_function(LPGUID, LPGUID, DOUBLE_PTR(IWICBitmapEncoder), intermediate_method = True)
    def CreateEncoder(self, guidContainerFormat: GUID, pguidVendor: IPointer[GUID], ppIEncoder: IDoublePtr[IWICBitmapEncoder], **kwargs) -> int:
        return self.virt_delegate(guidContainerFormat.ref() if guidContainerFormat else NULL, pguidVendor, ppIEncoder)

    @virtual_table.com_function(DOUBLE_PTR(IWICPalette))
    def CreatePalette(self, ppIPalette: IDoublePtr[IWICPalette]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICFormatConverter))
    def CreateFormatConverter(self, ppIFormatConverter: IDoublePtr[IWICFormatConverter]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapScaler))
    def CreateBitmapScaler(self, ppIBitmapScaler: IDoublePtr[IWICBitmapScaler]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapClipper))
    def CreateBitmapClipper(self, ppIBitmapClipper: IDoublePtr[IWICBitmapClipper]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICBitmapFlipRotator))
    def CreateBitmapFlipRotator(self, ppIBitmapFlipRotator: IDoublePtr[IWICBitmapFlipRotator]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICStream))
    def CreateStream(self, ppIWICStream: IDoublePtr[IWICStream]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICColorContext))
    def CreateColorContext(self, ppIWICColorContext: IDoublePtr[IWICColorContext]) -> int: ...

    @virtual_table.com_function(DOUBLE_PTR(IWICColorTransform))
    def CreateColorTransformer(self, ppIWICColorTransform: IDoublePtr[IWICColorTransform]) -> int: ...

    @virtual_table.com_function(UINT, UINT, PTR(WICPixelFormatGUID), WICBitmapCreateCacheOption, DOUBLE_PTR(IWICBitmap), intermediate_method = True)
    def CreateBitmap(self, uiWidth: int, uiHeight: int, pixelFormat: WICPixelFormatGUID, option: int, ppIBitmap: IDoublePtr[IWICBitmap], **kwargs) -> int:
        return self.virt_delegate(uiWidth, pixelFormat.ref() if pixelFormat else NULL, pixelFormat, option, ppIBitmap)

    @virtual_table.com_function(PTR(IWICBitmapSource), WICBitmapCreateCacheOption, DOUBLE_PTR(IWICBitmap))
    def CreateBitmapFromSource(self, pIBitmapSource: IPointer[IWICBitmapSource], option: int, ppIBitmap: IDoublePtr[IWICBitmap]) -> int: ...

    @virtual_table.com_function(PTR(IWICBitmapSource), UINT, UINT, UINT, UINT, DOUBLE_PTR(IWICBitmap))
    def CreateBitmapFromSourceRect(self, pIBitmapSource: IPointer[IWICBitmapSource], x: int, y: int, width: int, height: int, ppIBitmap: IDoublePtr[IWICBitmap]) -> int: ...

    @virtual_table.com_function(UINT, UINT, PTR(WICPixelFormatGUID), UINT, UINT, PBYTE, DOUBLE_PTR(IWICBitmap), intermediate_method = True)
    def CreateBitmapFromMemory(self, uiWidth: int, uiHeight: int, pixelFormat: WICPixelFormatGUID, cbStride: int, cbBufferSize: int, pbBuffer: PBYTE, ppIBitmap: IDoublePtr[IWICBitmap], **kwargs) -> int:
        return self.virt_delegate(uiWidth, pixelFormat.ref() if pixelFormat else NULL, pixelFormat, cbStride, cbBufferSize, pbBuffer, ppIBitmap)

    @virtual_table.com_function(HBITMAP, HPALETTE, WICBitmapAlphaChannelOption, DOUBLE_PTR(IWICBitmap))
    def CreateBitmapFromHBITMAP(self, hBitmap: HBITMAP, hPalette: HPALETTE, options: int, ppIBitmap: IDoublePtr[IWICBitmap]) -> int: ...

    @virtual_table.com_function(HICON, DOUBLE_PTR(IWICBitmap))
    def CreateBitmapFromHICON(self, hIcon: HICON, ppIBitmap: IDoublePtr[IWICBitmap]) -> int: ...

    @virtual_table.com_function(DWORD, DWORD, DOUBLE_PTR(IEnumUnknown))
    def CreateComponentEnumerator(self, componentTypes: int, options: int, ppIEnumUnknown: IDoublePtr[IEnumUnknown]) -> int: ...

    @virtual_table.com_function(PTR(IWICBitmapDecoder), DOUBLE_PTR(IWICFastMetadataEncoder))
    def CreateFastMetadataEncoderFromDecoder(self, pIDecoder: IPointer[IWICBitmapDecoder], ppIFastEncoder: IDoublePtr[IWICFastMetadataEncoder]) -> int: ...

    @virtual_table.com_function(LPGUID, LPGUID, PVOID, PVOID, intermediate_method = True)
    def CreateQueryWriter(self, guidMetadataFormat: GUID, pguidVendor: IPointer[GUID], ppIQueryWriter: IPointer[PVOID], **kwargs) -> int:
        return self.virt_delegate(guidMetadataFormat.ref() if guidMetadataFormat else NULL, pguidVendor, ppIQueryWriter)

    @virtual_table.com_function(PVOID, LPGUID, PVOID, PVOID)
    def CreateQueryWriterFromReader(self, pIQueryReader: PVOID, pguidVendor: IPointer[GUID], ppIQueryWriter: IPointer[PVOID]) -> int: ...

    virtual_table.build()


WindowsCodecs = W_WinDLL('WindowsCodecs.dll')


@WindowsCodecs.foreign(HRESULT, PTR(WICPixelFormatGUID), PTR(IWICBitmapSource), DOUBLE_PTR(IWICBitmapSource), intermediate_method = True)
def WICConvertBitmapSource(dstFormat: WICPixelFormatGUID, pISrc: IPointer[IWICBitmapSource], ppIDst: IDoublePtr[IWICBitmapSource], **kwargs) -> int:
    return delegate(dstFormat.ref() if dstFormat else NULL, pISrc, ppIDst)

@WindowsCodecs.foreign(HRESULT, UINT, UINT, PTR(WICPixelFormatGUID), HANDLE, UINT, UINT, DOUBLE_PTR(IWICBitmap), intermediate_method = True)
def WICCreateBitmapFromSection(width: int, height: int, pixelFormat: WICPixelFormatGUID, hSection: HANDLE, stride: int, offset: int, ppIBitmap: IDoublePtr[IWICBitmap], **kwargs) -> int:
    return delegate(width, height, pixelFormat.ref() if pixelFormat else NULL, hSection, stride, offset, ppIBitmap)

@WindowsCodecs.foreign(HRESULT, UINT, UINT, PTR(WICPixelFormatGUID), HANDLE, UINT, UINT, WICSectionAccessLevel, DOUBLE_PTR(IWICBitmap), intermediate_method = True)
def WICCreateBitmapFromSectionEx(width: int, height: int, pixelFormat: WICPixelFormatGUID, hSection: HANDLE, stride: int, offset: int, desiredAccessLevel: int, ppIBitmap: IDoublePtr[IWICBitmap], **kwargs) -> int:
    return delegate(width, height, pixelFormat.ref() if pixelFormat else NULL, hSection, stride, offset, desiredAccessLevel, ppIBitmap)

@WindowsCodecs.foreign(HRESULT, LPGUID, UINT, LPWSTR, PUINT, intermediate_method = True)
def WICMapGuidToShortName(guid: GUID, cchName: int, wzName: LPWSTR, pcchActual: PUINT, **kwargs) -> int:
    return delegate(guid.ref() if guid else NULL, cchName, wzName, pcchActual)

@WindowsCodecs.foreign(HRESULT, LPCWSTR, LPGUID)
def WICMapShortNameToGuid(wzName: LPCWSTR, pguid: IPointer[GUID]) -> int: ...

@WindowsCodecs.foreign(HRESULT, LPGUID, LPWSTR, UINT, LPWSTR, PUINT, intermediate_method = True)
def WICMapSchemaToName(guidMetadataFormat: GUID, pwzSchema: LPWSTR, cchName: int, wzName: LPWSTR, pcchActual: PUINT, **kwargs) -> int:
    return delegate(guidMetadataFormat.ref() if guidMetadataFormat else NULL, pwzSchema, cchName, wzName, pcchActual)

FACILITY_WINCODEC_ERR = 0x898
WINCODEC_ERR_BASE = 0x2000
WINCODEC_ERR_GENERIC_ERROR = E_FAIL
WINCODEC_ERR_INVALIDPARAMETER = E_INVALIDARG
WINCODEC_ERR_OUTOFMEMORY = E_OUTOFMEMORY
WINCODEC_ERR_NOTIMPLEMENTED = E_NOTIMPL
WINCODEC_ERR_ABORTED = E_ABORT
WINCODEC_ERR_ACCESSDENIED = E_ACCESSDENIED
WINCODEC_ERR_VALUEOVERFLOW = INTSAFE_E_ARITHMETIC_OVERFLOW
WICTiffCompressionDontCare = 0
WICTiffCompressionNone = 1
WICTiffCompressionCCITT3 = 2
WICTiffCompressionCCITT4 = 3
WICTiffCompressionLZW = 4
WICTiffCompressionRLE = 5
WICTiffCompressionZIP = 6
WICTiffCompressionLZWHDifferencing = 7
WICTIFFCOMPRESSIONOPTION_FORCE_DWORD = CODEC_FORCE_DWORD
WICTiffCompressionOption = INT

WICJpegYCrCbSubsamplingDefault = 0
WICJpegYCrCbSubsampling420 = 1
WICJpegYCrCbSubsampling422 = 2
WICJpegYCrCbSubsampling444 = 3
WICJpegYCrCbSubsampling440 = 4
WICJPEGYCRCBSUBSAMPLING_FORCE_DWORD = CODEC_FORCE_DWORD
WICJpegYCrCbSubsamplingOption = INT

WICPngFilterUnspecified = 0
WICPngFilterNone = 1
WICPngFilterSub = 2
WICPngFilterUp = 3
WICPngFilterAverage = 4
WICPngFilterPaeth = 5
WICPngFilterAdaptive = 6
WICPNGFILTEROPTION_FORCE_DWORD = CODEC_FORCE_DWORD
WICPngFilterOption = INT

WICWhitePointDefault = 0x00000001
WICWhitePointDaylight = 0x00000002
WICWhitePointCloudy = 0x00000004
WICWhitePointShade = 0x00000008
WICWhitePointTungsten = 0x00000010
WICWhitePointFluorescent = 0x00000020
WICWhitePointFlash = 0x00000040
WICWhitePointUnderwater = 0x00000080
WICWhitePointCustom = 0x00000100
WICWhitePointAutoWhiteBalance = 0x00000200
WICWhitePointAsShot = WICWhitePointDefault
WICNAMEDWHITEPOINT_FORCE_DWORD = CODEC_FORCE_DWORD
WICNamedWhitePoint = INT

WICRawCapabilityNotSupported = 0
WICRawCapabilityGetSupported = 1
WICRawCapabilityFullySupported = 2
WICRAWCAPABILITIES_FORCE_DWORD = CODEC_FORCE_DWORD
WICRawCapabilities = INT

WICRawRotationCapabilityNotSupported = 0
WICRawRotationCapabilityGetSupported = 1
WICRawRotationCapabilityNinetyDegreesSupported = 2
WICRawRotationCapabilityFullySupported = 3
WICRAWROTATIONCAPABILITIES_FORCE_DWORD = CODEC_FORCE_DWORD
WICRawRotationCapabilities = INT

@CStructure.make
class WICRawCapabilitiesInfo(CStructure):
    cbSize: IUint
    CodecMajorVersion: IUint
    CodecMinorVersion: IUint
    ExposureCompensationSupport: IInteger[WICRawCapabilities]
    ContrastSupport: IInteger[WICRawCapabilities]
    RGBWhitePointSupport: IInteger[WICRawCapabilities]
    NamedWhitePointSupport: IInteger[WICRawCapabilities]
    NamedWhitePointSupportMask: IUint
    KelvinWhitePointSupport: IInteger[WICRawCapabilities]
    GammaSupport: IInteger[WICRawCapabilities]
    TintSupport: IInteger[WICRawCapabilities]
    SaturationSupport: IInteger[WICRawCapabilities]
    SharpnessSupport: IInteger[WICRawCapabilities]
    NoiseReductionSupport: IInteger[WICRawCapabilities]
    DestinationColorProfileSupport: IInteger[WICRawCapabilities]
    ToneCurveSupport: IInteger[WICRawCapabilities]
    RotationSupport: IInteger[WICRawRotationCapabilities]
    RenderModeSupport: IInteger[WICRawCapabilities]

WICAsShotParameterSet = 1
WICUserAdjustedParameterSet = 2
WICAutoAdjustedParameterSet = 3
WICRAWPARAMETERSET_FORCE_DWORD = CODEC_FORCE_DWORD
WICRawParameterSet = INT

WICRawRenderModeDraft = 1
WICRawRenderModeNormal = 2
WICRawRenderModeBestQuality = 3
WICRAWRENDERMODE_FORCE_DWORD = CODEC_FORCE_DWORD
WICRawRenderMode = INT

@CStructure.make
class WICRawToneCurvePoint(CStructure):
    Input: IDouble
    Output: IDouble

@CStructure.make
class WICRawToneCurve(CStructure):
    cPoints: IUint

flexible_array(WICRawToneCurve, 'aPoints', WICRawToneCurvePoint)

WICRawChangeNotification_ExposureCompensation = 0x00000001
WICRawChangeNotification_NamedWhitePoint = 0x00000002
WICRawChangeNotification_KelvinWhitePoint = 0x00000004
WICRawChangeNotification_RGBWhitePoint = 0x00000008
WICRawChangeNotification_Contrast = 0x00000010
WICRawChangeNotification_Gamma = 0x00000020
WICRawChangeNotification_Sharpness = 0x00000040
WICRawChangeNotification_Saturation = 0x00000080
WICRawChangeNotification_Tint = 0x00000100
WICRawChangeNotification_NoiseReduction = 0x00000200
WICRawChangeNotification_DestinationColorContext = 0x00000400
WICRawChangeNotification_ToneCurve = 0x00000800
WICRawChangeNotification_Rotation = 0x00001000
WICRawChangeNotification_RenderMode = 0x00002000
