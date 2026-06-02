from win.gl.gl import *
from win.gl.glu import *
from win.wingdi import *

from functools import wraps
from typing import Callable

class GLExtState:
    methods: list[Callable] = []

class GLExtAPI:
    """
    Open GL extensions API.
    """
    
    def method(ret: type, *args: type):
        """
        Open GL extension method.
        """
        
        def _method(f: Callable):
            for method in GLExtState.methods:
                if method.__name__ == f.__name__:
                    return method
            
            def _glext_routine(*args):
                impl = _glext_routine._glext_implementation
                return impl(*args)
            
            _glext_routine._glext_implementation = None
            _glext_routine._glext_ret = ret
            _glext_routine._glext_args = args
            
            GLExtState.methods.append(_glext_routine)
            return wraps(f)(_glext_routine)
        return _method
    
    @classmethod
    def initialize(cls):
        """
        Initialize an Open GL extensions.
        """
        
        for method in GLExtState.methods:
            proto = CALLBACK(method._glext_ret, *method._glext_args)
            name = method.__name__.encode('ascii')
            address = wglGetProcAddress(name)
            if not address: 
                function = NullFunction('OpenGL', method.__name__)
            else:
                function = i_cast(address, proto)
            method._glext_implementation = function
    
class WGL_EXT_swap_control:
    @GLExtAPI.method(BOOL, INT)
    def wglSwapIntervalEXT(interval: int) -> int: ...
    
    @GLExtAPI.method(INT)
    def wglGetSwapIntervalEXT() -> int: ...

class GL_EXT_abgr:
    GL_ABGR_EXT = 0x8000
    
class GL_EXT_bgra:
    GL_BGR_EXT = 0x80E0
    GL_BGRA_EXT = 0x80E1

class WGL_EXT_pixel_format:
    WGL_NUMBER_PIXEL_FORMATS_EXT = 0x2000
    WGL_DRAW_TO_WINDOW_EXT = 0x2001
    WGL_DRAW_TO_BITMAP_EXT = 0x2002
    WGL_ACCELERATION_EXT = 0x2003
    WGL_NEED_PALETTE_EXT = 0x2004
    WGL_NEED_SYSTEM_PALETTE_EXT = 0x2005
    WGL_SWAP_LAYER_BUFFERS_EXT = 0x2006
    WGL_SWAP_METHOD_EXT = 0x2007
    WGL_NUMBER_OVERLAYS_EXT = 0x2008
    WGL_NUMBER_UNDERLAYS_EXT = 0x2009
    WGL_TRANSPARENT_EXT = 0x200A
    WGL_TRANSPARENT_VALUE_EXT = 0x200B
    WGL_SHARE_DEPTH_EXT = 0x200C
    WGL_SHARE_STENCIL_EXT = 0x200D
    WGL_SHARE_ACCUM_EXT = 0x200E
    WGL_SUPPORT_GDI_EXT = 0x200F
    WGL_SUPPORT_OPENGL_EXT = 0x2010
    WGL_DOUBLE_BUFFER_EXT = 0x2011
    WGL_STEREO_EXT = 0x2012
    WGL_PIXEL_TYPE_EXT = 0x2013
    WGL_COLOR_BITS_EXT = 0x2014
    WGL_RED_BITS_EXT = 0x2015
    WGL_RED_SHIFT_EXT = 0x2016
    WGL_GREEN_BITS_EXT = 0x2017
    WGL_GREEN_SHIFT_EXT = 0x2018
    WGL_BLUE_BITS_EXT = 0x2019
    WGL_BLUE_SHIFT_EXT = 0x201A
    WGL_ALPHA_BITS_EXT = 0x201B
    WGL_ALPHA_SHIFT_EXT = 0x201C
    WGL_ACCUM_BITS_EXT = 0x201D
    WGL_ACCUM_RED_BITS_EXT = 0x201E
    WGL_ACCUM_GREEN_BITS_EXT = 0x201F
    WGL_ACCUM_BLUE_BITS_EXT = 0x2020
    WGL_ACCUM_ALPHA_BITS_EXT = 0x2021
    WGL_DEPTH_BITS_EXT = 0x2022
    WGL_STENCIL_BITS_EXT = 0x2023
    WGL_AUX_BUFFERS_EXT = 0x2024
    WGL_NO_ACCELERATION_EXT = 0x2025
    WGL_GENERIC_ACCELERATION_EXT = 0x2026
    WGL_FULL_ACCELERATION_EXT = 0x2027
    WGL_SWAP_EXCHANGE_EXT = 0x2028
    WGL_SWAP_COPY_EXT = 0x2029
    WGL_SWAP_UNDEFINED_EXT = 0x202A
    WGL_TYPE_RGBA_EXT = 0x202B
    WGL_TYPE_COLORINDEX_EXT = 0x202C
    
    @GLExtAPI.method(BOOL, HDC, INT, INT, UINT, PINT, PINT)
    def wglGetPixelFormatAttribivEXT(
        hdc: int, iPixelFormat: int, iLayerPlane: int, nAttributes: int, 
        piAttributes: PINT, piValues: PINT) -> int: ...
    
    @GLExtAPI.method(BOOL, HDC, INT, INT, UINT, PINT, PFLOAT)
    def wglGetPixelFormatAttribfvEXT(
        hdc: int, iPixelFormat: int, iLayerPlane: int, nAttributes: int, 
        piAttributes: PINT, piValues: PFLOAT) -> int: ...
    
    @GLExtAPI.method(BOOL, PINT, PFLOAT, UINT, PINT, PUINT)
    def wglChoosePixelFormatEXT(
        hdc: int, piAttribIList: PINT, pfAttribFList: PFLOAT, 
        nMaxFormats: int, piFormats: PINT, nNumFormats: PUINT) -> int: ...

class GL_EXT_texture_swizzle:
    GL_TEXTURE_SWIZZLE_R_EXT = 0x8E42
    GL_TEXTURE_SWIZZLE_G_EXT = 0x8E43
    GL_TEXTURE_SWIZZLE_B_EXT = 0x8E44
    GL_TEXTURE_SWIZZLE_A_EXT = 0x8E45
    GL_TEXTURE_SWIZZLE_RGBA_EXT = 0x8E4
    
class GL_EXT_stencil_wrap:
    GL_INCR_WRAP_EXT = 0x8507
    GL_DECR_WRAP_EXT = 0x8508
    
class GL_EXT_fog_coord:
    GL_FOG_COORDINATE_SOURCE_EXT = 0x8450
    GL_FOG_COORDINATE_EXT = 0x8451
    GL_FRAGMENT_DEPTH_EXT = 0x8452
    GL_CURRENT_FOG_COORDINATE_EXT = 0x8453
    GL_FOG_COORDINATE_ARRAY_TYPE_EXT = 0x8454
    GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = 0x8455
    GL_FOG_COORDINATE_ARRAY_POINTER_EXT = 0x8456
    GL_FOG_COORDINATE_ARRAY_EXT = 0x8457
    
    @GLExtAPI.method(GLvoid, GLfloat)
    def glFogCoordfEXT(coord: float): ...
    
    @GLExtAPI.method(GLvoid, GLdouble)
    def glFogCoorddEXT(coord: float): ...
    
    @GLExtAPI.method(GLvoid, GLfloat)
    def glFogCoordfvEXT(coord: float): ...
    
    @GLExtAPI.method(GLvoid, GLdouble)
    def glFogCoorddvEXT(coord: float): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizei, PVOID)
    def glFogCoordPointerEXT(type: int, stride: int, pointer: int): ...

class GL_EXT_blend_color:
    GL_CONSTANT_COLOR_EXT = 0x8001
    GL_ONE_MINUS_CONSTANT_COLOR_EXT = 0x8002
    GL_CONSTANT_ALPHA_EXT = 0x8003
    GL_ONE_MINUS_CONSTANT_ALPHA_EXT = 0x8004
    GL_BLEND_COLOR_EXT = 0x8005
    
    @GLExtAPI.method(GLvoid, GLclampf, GLclampf, GLclampf, GLclampf)
    def glBlendColorEXT(red: float, green: float, blue:  float, alpha: float): ...

class GL_EXT_cull_vertex:
    GL_CULL_VERTEX_EXT = 0x81AA
    GL_CULL_VERTEX_EYE_POSITION_EXT = 0x81AB
    GL_CULL_VERTEX_OBJECT_POSITION_EXT = 0x81AC
    
    @GLExtAPI.method(GLvoid, GLenum, PTR(GLfloat))
    def glCullParameterfvEXT(pname: int, params: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLenum, PTR(GLdouble))
    def glCullParameterdvEXT(pname: int, params: IPointer[GLdouble]): ...

class GL_EXT_index_material:
    @GLExtAPI.method(GLvoid, GLenum, GLenum)
    def glIndexMaterialEXT(face: int, mode: int): ...

class GL_EXT_index_func:
    @GLExtAPI.method(GLvoid, GLenum, GLfloat)
    def glIndexFuncEXT(func: int, ref: float): ...
    
class GL_EXT_light_texture:
    GL_FRAGMENT_MATERIAL_EXT = 0x8349
    GL_FRAGMENT_NORMAL_EXT = 0x834A
    GL_FRAGMENT_DEPTH_EXT = 0x8452
    GL_FRAGMENT_COLOR_EXT = 0x834C
    GL_ATTENUATION_EXT = 0x834D
    GL_SHADOW_ATTENUATION_EXT = 0x834E
    GL_TEXTURE_APPLICATION_MODE_EXT = 0x834F
    GL_TEXTURE_LIGHT_EXT = 0x8350
    GL_TEXTURE_MATERIAL_FACE_EXT = 0x8351
    GL_TEXTURE_MATERIAL_PARAMETER_EXT = 0x8352
    
    @GLExtAPI.method(GLvoid, GLenum)
    def glApplyTextureEXT(mode: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum)
    def glTextureLightEXT(pname: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum)
    def glTextureMaterialEXT(face: int, mode: int): ...

class GL_EXT_polygon_offset:
    GL_POLYGON_OFFSET_EXT = 0x8037
    GL_POLYGON_OFFSET_FACTOR_EXT = 0x8038
    GL_POLYGON_OFFSET_BIAS_EXT = 0x8039
    
    @GLExtAPI.method(GLvoid, GLfloat, GLfloat)
    def glPolygonOffsetEXT(factor: float, bias: float): ...

class GL_EXT_texture:
    GL_ALPHA4_EXT = 0x803B
    GL_ALPHA8_EXT = 0x803C
    GL_ALPHA12_EXT = 0x803D
    GL_ALPHA16_EXT = 0x803E
    GL_LUMINANCE4_EXT = 0x803F
    GL_LUMINANCE8_EXT = 0x8040
    GL_LUMINANCE12_EXT = 0x8041
    GL_LUMINANCE16_EXT = 0x8042
    GL_LUMINANCE4_ALPHA4_EXT = 0x8043
    GL_LUMINANCE6_ALPHA2_EXT = 0x8044
    GL_LUMINANCE8_ALPHA8_EXT = 0x8045
    GL_LUMINANCE12_ALPHA4_EXT = 0x8046
    GL_LUMINANCE12_ALPHA12_EXT = 0x8047
    GL_LUMINANCE16_ALPHA16_EXT = 0x8048
    GL_INTENSITY_EXT = 0x8049
    GL_INTENSITY4_EXT = 0x804A
    GL_INTENSITY8_EXT = 0x804B
    GL_INTENSITY12_EXT = 0x804C
    GL_INTENSITY16_EXT = 0x804D
    GL_RGB2_EXT = 0x804E
    GL_RGB4_EXT = 0x804F
    GL_RGB5_EXT = 0x8050
    GL_RGB8_EXT = 0x8051
    GL_RGB10_EXT = 0x8052
    GL_RGB12_EXT = 0x8053
    GL_RGB16_EXT = 0x8054
    GL_RGBA2_EXT = 0x8055
    GL_RGBA4_EXT = 0x8056
    GL_RGB5_A1_EXT = 0x8057
    GL_RGBA8_EXT = 0x8058
    GL_RGB10_A2_EXT = 0x8059
    GL_RGBA12_EXT = 0x805A
    GL_RGBA16_EXT = 0x805B
    GL_TEXTURE_RED_SIZE_EXT = 0x805C
    GL_TEXTURE_GREEN_SIZE_EXT = 0x805D
    GL_TEXTURE_BLUE_SIZE_EXT = 0x805E
    GL_TEXTURE_ALPHA_SIZE_EXT = 0x805F
    GL_TEXTURE_LUMINANCE_SIZE_EXT = 0x8060
    GL_TEXTURE_INTENSITY_SIZE_EXT = 0x8061
    GL_REPLACE_EXT = 0x8062
    GL_PROXY_TEXTURE_1D_EXT = 0x8063
    GL_PROXY_TEXTURE_2D_EXT = 0x8064

class WGL_EXT_extensions_string:
    @GLExtAPI.method(LPSTR)
    def wglGetExtensionsStringEXT() -> LPSTR: ...
    
class GL_EXT_vertex_shader:
    GL_VERTEX_SHADER_EXT = 0x8780
    GL_VARIANT_VALUE_EXT = 0x87E4
    GL_VARIANT_DATATYPE_EXT = 0x87E5
    GL_VARIANT_ARRAY_STRIDE_EXT = 0x87E6
    GL_VARIANT_ARRAY_TYPE_EXT = 0x87E7
    GL_VARIANT_ARRAY_EXT = 0x87E8
    GL_VARIANT_ARRAY_POINTER_EXT = 0x87E9
    GL_INVARIANT_VALUE_EXT = 0x87EA
    GL_INVARIANT_DATATYPE_EXT = 0x87EB
    GL_LOCAL_CONSTANT_VALUE_EXT = 0x87EC
    GL_LOCAL_CONSTANT_DATATYPE_EXT = 0x87ED
    GL_OP_INDEX_EXT = 0x8782
    GL_OP_NEGATE_EXT = 0x8783
    GL_OP_DOT3_EXT = 0x8784
    GL_OP_DOT4_EXT = 0x8785
    GL_OP_MUL_EXT = 0x8786
    GL_OP_ADD_EXT = 0x8787
    GL_OP_MADD_EXT = 0x8788
    GL_OP_FRAC_EXT = 0x8789
    GL_OP_MAX_EXT = 0x878A
    GL_OP_MIN_EXT = 0x878B
    GL_OP_SET_GE_EXT = 0x878C
    GL_OP_SET_LT_EXT = 0x878D
    GL_OP_CLAMP_EXT = 0x878E
    GL_OP_FLOOR_EXT = 0x878F
    GL_OP_ROUND_EXT = 0x8790
    GL_OP_EXP_BASE_2_EXT = 0x8791
    GL_OP_LOG_BASE_2_EXT = 0x8792
    GL_OP_POWER_EXT = 0x8793
    GL_OP_RECIP_EXT = 0x8794
    GL_OP_RECIP_SQRT_EXT = 0x8795
    GL_OP_SUB_EXT = 0x8796
    GL_OP_CROSS_PRODUCT_EXT = 0x8797
    GL_OP_MULTIPLY_MATRIX_EXT = 0x8798
    GL_OP_MOV_EXT = 0x8799
    GL_OUTPUT_VERTEX_EXT = 0x879A
    GL_OUTPUT_COLOR0_EXT = 0x879B
    GL_OUTPUT_COLOR1_EXT = 0x879C
    GL_OUTPUT_TEXTURE_COORD0_EXT = 0x879D
    GL_OUTPUT_TEXTURE_COORD1_EXT = 0x879E
    GL_OUTPUT_TEXTURE_COORD2_EXT = 0x879F
    GL_OUTPUT_TEXTURE_COORD3_EXT = 0x87A0
    GL_OUTPUT_TEXTURE_COORD4_EXT = 0x87A1
    GL_OUTPUT_TEXTURE_COORD5_EXT = 0x87A2
    GL_OUTPUT_TEXTURE_COORD6_EXT = 0x87A3
    GL_OUTPUT_TEXTURE_COORD7_EXT = 0x87A4
    GL_OUTPUT_TEXTURE_COORD8_EXT = 0x87A5
    GL_OUTPUT_TEXTURE_COORD9_EXT = 0x87A6
    GL_OUTPUT_TEXTURE_COORD10_EXT = 0x87A7
    GL_OUTPUT_TEXTURE_COORD11_EXT = 0x87A8
    GL_OUTPUT_TEXTURE_COORD12_EXT = 0x87A9
    GL_OUTPUT_TEXTURE_COORD13_EXT = 0x87AA
    GL_OUTPUT_TEXTURE_COORD14_EXT = 0x87AB
    GL_OUTPUT_TEXTURE_COORD15_EXT = 0x87AC
    GL_OUTPUT_TEXTURE_COORD16_EXT = 0x87AD
    GL_OUTPUT_TEXTURE_COORD17_EXT = 0x87AE
    GL_OUTPUT_TEXTURE_COORD18_EXT = 0x87AF
    GL_OUTPUT_TEXTURE_COORD19_EXT = 0x87B0
    GL_OUTPUT_TEXTURE_COORD20_EXT = 0x87B1
    GL_OUTPUT_TEXTURE_COORD21_EXT = 0x87B2
    GL_OUTPUT_TEXTURE_COORD22_EXT = 0x87B3
    GL_OUTPUT_TEXTURE_COORD23_EXT = 0x87B4
    GL_OUTPUT_TEXTURE_COORD24_EXT = 0x87B5
    GL_OUTPUT_TEXTURE_COORD25_EXT = 0x87B6
    GL_OUTPUT_TEXTURE_COORD26_EXT = 0x87B7
    GL_OUTPUT_TEXTURE_COORD27_EXT = 0x87B8
    GL_OUTPUT_TEXTURE_COORD28_EXT = 0x87B9
    GL_OUTPUT_TEXTURE_COORD29_EXT = 0x87BA
    GL_OUTPUT_TEXTURE_COORD30_EXT = 0x87BB
    GL_OUTPUT_TEXTURE_COORD31_EXT = 0x87BC
    GL_OUTPUT_FOG_EXT = 0x87BD
    GL_SCALAR_EXT = 0x87BE
    GL_VECTOR_EXT = 0x87BF
    GL_MATRIX_EXT = 0x87C0
    GL_VARIANT_EXT = 0x87C1
    GL_INVARIANT_EXT = 0x87C2
    GL_LOCAL_CONSTANT_EXT = 0x87C3
    GL_LOCAL_EXT = 0x87C4
    GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87C5
    GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 0x87C6
    GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 0x87C7
    GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87C8
    GL_MAX_VERTEX_SHADER_LOCALS_EXT = 0x87C9
    GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CA
    GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 0x87CB
    GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87CC
    GL_MAX_OPTIMIZED_VERTEX_SHADER_INARIANTS_EXT = 0x87CD
    GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 0x87CE
    GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CF
    GL_VERTEX_SHADER_VARIANTS_EXT = 0x87D0
    GL_VERTEX_SHADER_INVARIANTS_EXT = 0x87D1
    GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87D2
    GL_VERTEX_SHADER_LOCALS_EXT = 0x87D3
    GL_VERTEX_SHADER_BINDING_EXT = 0x8781
    GL_VERTEX_SHADER_OPTIMIZED_EXT = 0x87D4
    GL_X_EXT = 0x87D5
    GL_Y_EXT = 0x87D6
    GL_Z_EXT = 0x87D7
    GL_W_EXT = 0x87D8
    GL_NEGATIVE_X_EXT = 0x87D9
    GL_NEGATIVE_Y_EXT = 0x87DA
    GL_NEGATIVE_Z_EXT = 0x87DB
    GL_NEGATIVE_W_EXT = 0x87DC
    GL_ZERO_EXT = 0x87dd
    GL_ONE_EXT = 0x87de
    GL_NEGATIVE_ONE_EXT = 0x87DF
    GL_NORMALIZED_RANGE_EXT = 0x87E0
    GL_FULL_RANGE_EXT = 0x87E1
    GL_CURRENT_VERTEX_EXT = 0x87E2
    GL_MVP_MATRIX_EXT = 0x87E3
    
    @GLExtAPI.method(GLvoid)
    def glBeginVertexShaderEXT(): ...
    
    @GLExtAPI.method(GLvoid)
    def glEndVertexShaderEXT(): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glBindVertexShaderEXT(id: int): ...
    
    @GLExtAPI.method(GLuint, GLuint)
    def glGenVertexShadersEXT(range: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glDeleteVertexShaderEXT(id: int): ...
    
    @GLExtAPI.method(GLenum, GLuint, GLuint)
    def glShaderOp1EXT(op: int, res: int, arg1: int) -> int: ...
    
    @GLExtAPI.method(GLenum, GLuint, GLuint, GLuint)
    def glShaderOp2EXT(op: int, res: int, arg1: int, arg2: int) -> int: ...
    
    @GLExtAPI.method(GLenum, GLuint, GLuint, GLuint, GLuint)
    def glShaderOp3EXT(op: int, res: int, arg1: int, arg3: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLuint, GLenum, GLenum, GLenum, GLenum)
    def glSwizzleEXT(res: int, in_: int, outX: int, outY: int, outZ: int, outW: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLuint, GLenum, GLenum, GLenum, GLenum)
    def glWriteMaskEXT(res: int, in_: int, outX: int, outY: int, outZ: int, outW: int): ...

    @GLExtAPI.method(GLvoid, GLuint, GLuint, GLuint)
    def glInsertComponentEXT(res: int, src: int, num: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLuint, GLuint)
    def glExtractComponentEXT(res: int, src: int, num: int): ...
    
    @GLExtAPI.method(GLuint, GLenum, GLenum, GLenum, GLuint)
    def glGenSymbolsEXT(datatype: int, storagetype: int, range: int, components: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PVOID)
    def glSetInvariantEXT(id: int, type: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PVOID)
    def glSetLocalConstantEXT(id: int, type: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantbvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantsvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantivEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantfvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantdvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantubvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantusvEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PVOID)
    def glVariantuivEXT(id: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, GLuint, PVOID)
    def glVariantPointerEXT(id: int, type: int, stride: int, addr: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glEnableVariantClientStateEXT(id: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glDisableVariantClientStateEXT(id: int): ...
    
    @GLExtAPI.method(GLuint, GLenum, GLenum)
    def glBindLightParameterEXT(light: int, value: int) -> int: ...
    
    @GLExtAPI.method(GLuint, GLenum, GLenum)
    def glBindMaterialParameterEXT(light: int, value: int) -> int: ...
    
    @GLExtAPI.method(GLuint, GLenum, GLenum, GLenum)
    def glBindTexGenParameterEXT(unit: int, light: int, value: int) -> int: ...
    
    @GLExtAPI.method(GLuint, GLenum, GLenum)
    def glBindTextureUnitParameterEXT(unit: int, value: int) -> int: ...
    
    @GLExtAPI.method(GLuint, GLenum)
    def glBindParameterEXT(value: int) -> int: ...
    
    @GLExtAPI.method(GLboolean, GLuint, GLenum)
    def glIsVariantEnabledEXT(id: int, cap: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLboolean))
    def glGetVariantBooleanvEXT(id: int, value: int, data: IPointer[GLboolean]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLint))
    def glGetVariantIntegervEXT(id: int, value: int, data: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLfloat))
    def glGetVariantFloatvEXT(id: int, value: int, data: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(PVOID))
    def glGetVariantPointervEXT(id: int, value: int, data: IPointer[PVOID]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLboolean))
    def glGetInvariantBooleanvEXT(id: int, value: int, data: IPointer[GLboolean]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLint))
    def glGetInvariantIntegervEXT(id: int, value: int, data: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLfloat))
    def glGetInvariantFloatvEXT(id: int, value: int, data: IPointer[GLfloat]): ...

    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLboolean))
    def glGetLocalConstantBooleanvEXT(id: int, value: int, data: IPointer[GLboolean]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLint))
    def glGetLocalConstantIntegervEXT(id: int, value: int, data: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLfloat))
    def glGetLocalConstantFloatvEXT(id: int, value: int, data: IPointer[GLfloat]): ...

class GL_EXT_framebuffer_object:
    GL_FRAMEBUFFER_EXT = 0x8D40
    GL_RENDERBUFFER_EXT = 0x8D41
    GL_STENCIL_INDEX1_EXT = 0x8D46
    GL_STENCIL_INDEX4_EXT = 0x8D47
    GL_STENCIL_INDEX8_EXT = 0x8D48
    GL_STENCIL_INDEX16_EXT = 0x8D49
    GL_RENDERBUFFER_WIDTH_EXT = 0x8D42
    GL_RENDERBUFFER_HEIGHT_EXT = 0x8D43
    GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 0x8D44
    GL_RENDERBUFFER_RED_SIZE_EXT = 0x8D50
    GL_RENDERBUFFER_GREEN_SIZE_EXT = 0x8D51
    GL_RENDERBUFFER_BLUE_SIZE_EXT = 0x8D52
    GL_RENDERBUFFER_ALPHA_SIZE_EXT = 0x8D53
    GL_RENDERBUFFER_DEPTH_SIZE_EXT = 0x8D54
    GL_RENDERBUFFER_STENCIL_SIZE_EXT = 0x8D55
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 0x8CD0
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 0x8CD1
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 0x8CD2
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 0x8CD3
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 0x8CD4
    GL_COLOR_ATTACHMENT0_EXT = 0x8CE0
    GL_COLOR_ATTACHMENT1_EXT = 0x8CE1
    GL_COLOR_ATTACHMENT2_EXT = 0x8CE2
    GL_COLOR_ATTACHMENT3_EXT = 0x8CE3
    GL_COLOR_ATTACHMENT4_EXT = 0x8CE4
    GL_COLOR_ATTACHMENT5_EXT = 0x8CE5
    GL_COLOR_ATTACHMENT6_EXT = 0x8CE6
    GL_COLOR_ATTACHMENT7_EXT = 0x8CE7
    GL_COLOR_ATTACHMENT8_EXT = 0x8CE8
    GL_COLOR_ATTACHMENT9_EXT = 0x8CE9
    GL_COLOR_ATTACHMENT10_EXT = 0x8CEA
    GL_COLOR_ATTACHMENT11_EXT = 0x8CEB
    GL_COLOR_ATTACHMENT12_EXT = 0x8CEC
    GL_COLOR_ATTACHMENT13_EXT = 0x8CED
    GL_COLOR_ATTACHMENT14_EXT = 0x8CEE
    GL_COLOR_ATTACHMENT15_EXT = 0x8CEF
    GL_DEPTH_ATTACHMENT_EXT = 0x8D00
    GL_STENCIL_ATTACHMENT_EXT = 0x8D20
    GL_FRAMEBUFFER_COMPLETE_EXT = 0x8CD5
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 0x8CD6
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 0x8CD7
    GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 0x8CD9
    GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 0x8CDA
    GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 0x8CDB
    GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 0x8CDC
    GL_FRAMEBUFFER_UNSUPPORTED_EXT = 0x8CDD
    GL_FRAMEBUFFER_BINDING_EXT = 0x8CA6
    GL_RENDERBUFFER_BINDING_EXT = 0x8CA7
    GL_MAX_COLOR_ATTACHMENTS_EXT = 0x8CDF
    GL_MAX_RENDERBUFFER_SIZE_EXT = 0x84E8
    GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 0x0506
    
    @GLExtAPI.method(GLboolean, GLuint)
    def glIsRenderbufferEXT(renderbuffer: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLuint)
    def glBindRenderbufferEXT(target: int, renderbuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glDeleteRenderbuffersEXT(n: int, renderbufers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glGenRenderbuffersEXT(n: int, renderbuffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLsizei, GLsizei)
    def glRenderbufferStorageEXT(target: int, internalformat: int, width: int, height: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, PTR(GLint))
    def glGetRenderbufferParameterivEXT(target: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLboolean, GLuint)
    def glIsFramebufferEXT(framebuffer: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLuint)
    def glBindFramebufferEXT(target: int, framebuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glDeleteFramebuffersEXT(n: int, framebuffers: IPointer[GLuint]): ...

    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glGenFramebuffersEXT(n: int, framebuffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLenum, GLenum)
    def glCheckFramebufferStatusEXT(target: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint)
    def glFramebufferTexture1DEXT(target: int, attachment: int, textarget: int, texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint)
    def glFramebufferTexture2DEXT(target: int, attachment: int, textarget: int, texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint, GLint)
    def glFramebufferTexture3DEXT(target: int, attachment: int, textarget: int, texture: int, level: int, zoffset: int): ...

    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint)
    def glFramebufferRenderbufferEXT(target: int, attachment: int, renderbuffertarget: int, renderbuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, PTR(GLint))
    def glGetFramebufferAttachmentParameterivEXT(target: int, attachment: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLenum)
    def glGenerateMipmapEXT(target: int): ...

GLhandleARB = HANDLE
GLcharARB = CHAR

class GL_ARB_shader_objects:
    GL_PROGRAM_OBJECT_ARB = 0x8B40
    GL_OBJECT_TYPE_ARB = 0x8B4E
    GL_OBJECT_SUBTYPE_ARB = 0x8B4F
    GL_OBJECT_DELETE_STATUS_ARB = 0x8B80
    GL_OBJECT_COMPILE_STATUS_ARB = 0x8B81
    GL_OBJECT_LINK_STATUS_ARB = 0x8B82
    GL_OBJECT_VALIDATE_STATUS_ARB = 0x8B83
    GL_OBJECT_INFO_LOG_LENGTH_ARB = 0x8B84
    GL_OBJECT_ATTACHED_OBJECTS_ARB = 0x8B85
    GL_OBJECT_ACTIVE_UNIFORMS_ARB = 0x8B86
    GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 0x8B87
    GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 0x8B88
    GL_SHADER_OBJECT_ARB = 0x8B48
    GL_FLOAT = 0x1406
    GL_FLOAT_VEC2_ARB = 0x8B50
    GL_FLOAT_VEC3_ARB = 0x8B51
    GL_FLOAT_VEC4_ARB = 0x8B52
    GL_INT = 0x1404
    GL_INT_VEC2_ARB = 0x8B53
    GL_INT_VEC3_ARB = 0x8B54
    GL_INT_VEC4_ARB = 0x8B55
    GL_BOOL_ARB = 0x8B56
    GL_BOOL_VEC2_ARB = 0x8B57
    GL_BOOL_VEC3_ARB = 0x8B58
    GL_BOOL_VEC4_ARB = 0x8B59
    GL_FLOAT_MAT2_ARB = 0x8B5A
    GL_FLOAT_MAT3_ARB = 0x8B5B
    GL_FLOAT_MAT4_ARB = 0x8B5C
    GL_SAMPLER_1D_ARB = 0x8B5D
    GL_SAMPLER_2D_ARB = 0x8B5E
    GL_SAMPLER_3D_ARB = 0x8B5F
    GL_SAMPLER_CUBE_ARB = 0x8B60
    GL_SAMPLER_1D_SHADOW_ARB = 0x8B61
    GL_SAMPLER_2D_SHADOW_ARB = 0x8B62
    GL_SAMPLER_2D_RECT_ARB = 0x8B63
    GL_SAMPLER_2D_RECT_SHADOW_ARB = 0x8B64
    
    @GLExtAPI.method(GLvoid, GLhandleARB)
    def glDeleteObjectARB(obj: int): ...
    
    @GLExtAPI.method(GLhandleARB, GLenum)
    def glGetHandleARB(pname: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLhandleARB)
    def glDetachObjectARB(containerObj: int, attachedObj: int): ...
    
    @GLExtAPI.method(GLhandleARB, GLenum)
    def glCreateShaderObjectARB(shaderType: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLsizei, PTR(LPSTR), PTR(GLint))
    def glShaderSourceARB(shaderObj: int, count: int, string: IPointer[LPSTR], length: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB)
    def glCompileShaderARB(shaderObj: int): ...
    
    @GLExtAPI.method(GLhandleARB)
    def glCreateProgramObjectARB() -> int: ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLhandleARB)
    def glAttachObjectARB(containerObj: int, obj: int): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB)
    def glLinkProgramARB(programObj: int): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB)
    def glUseProgramObjectARB(programObj: int): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB)
    def glValidateProgramARB(programObj: int): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLfloat)
    def glUniform1fARB(location: int, v0: float): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLfloat, GLfloat)
    def glUniform2fARB(location: int, v0: float, v1: float): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLfloat, GLfloat, GLfloat)
    def glUniform3fARB(location: int, v0: float, v1: float, v2: float): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLfloat, GLfloat, GLfloat, GLfloat)
    def glUniform4fARB(location: int, v0: float, v1: float, v2: float, v3: float): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLint)
    def glUniform1iARB(location: int, v0: int): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLint, GLint)
    def glUniform2iARB(location: int, v0: int, v1: int): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLint, GLint, GLint)
    def glUniform3iARB(location: int, v0: int, v1: int, v2: int): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLint, GLint, GLint, GLint)
    def glUniform4iARB(location: int, v0: int, v1: int, v2: int, v3: int): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLfloat))
    def glUniform1fvARB(location: int, count: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLfloat))
    def glUniform2fvARB(location: int, count: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLfloat))
    def glUniform3fvARB(location: int, count: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLfloat))
    def glUniform4fvARB(location: int, count: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLint))
    def glUniform1ivARB(location: int, count: int, value: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLint))
    def glUniform2ivARB(location: int, count: int, value: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLint))
    def glUniform3ivARB(location: int, count: int, value: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, PTR(GLint))
    def glUniform4ivARB(location: int, count: int, value: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, GLboolean, PTR(GLfloat))
    def glUniformMatrix2fvARB(location: int, count: int, transpose: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, GLboolean, PTR(GLfloat))
    def glUniformMatrix3fvARB(location: int, count: int, transpose: int, value: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLsizei, GLboolean, PTR(GLfloat))
    def glUniformMatrix4fvARB(location: int, count: int, transpose: int, value: IPointer[GLfloat]): ...

    @GLExtAPI.method(GLvoid, GLhandleARB, GLenum, PTR(GLfloat))
    def glGetObjectParameterfvARB(obj: int, pname: int, params: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLenum, PTR(GLint))
    def glGetObjectParameterivARB(obj: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLsizei, PTR(GLsizei), LPSTR)
    def glGetInfoLogARB(obj: int, maxLength: int, length: IPointer[GLsizei], infoLog: LPSTR): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLsizei, PTR(GLsizei), PTR(GLhandleARB))
    def glGetAttachedObjectsARB(containerObj: int, maxCount: int, count: IPointer[GLsizei], obj: IPointer[GLhandleARB]): ...
    
    @GLExtAPI.method(GLint, GLhandleARB, LPSTR)
    def glGetUniformLocationARB(programObj: int, name: LPSTR) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLuint, GLsizei, PTR(GLsizei), PTR(GLint), PTR(GLenum), LPSTR)
    def glGetActiveUniformARB(programObj: int, index: int, maxLength: int, length: IPointer[GLsizei], size: IPointer[GLint], type: IPointer[GLenum], name: LPSTR): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLint, PTR(GLfloat))
    def glGetUniformfvARB(programObj: int, location: int, params: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLint, PTR(GLint))
    def glGetUniformivARB(programObj: int, location: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLsizei, PTR(GLsizei), LPSTR)
    def glGetShaderSourceARB(programObj: int, maxLength: int, length: IPointer[GLsizei], source: LPSTR): ...

class GL_ARB_framebuffer_object:
    GL_FRAMEBUFFER = 0x8D40
    GL_READ_FRAMEBUFFER = 0x8CA8
    GL_DRAW_FRAMEBUFFER = 0x8CA9
    GL_RENDERBUFFER = 0x8D41
    GL_STENCIL_INDEX1 = 0x8D46
    GL_STENCIL_INDEX4 = 0x8D47
    GL_STENCIL_INDEX8 = 0x8D48
    GL_STENCIL_INDEX16 = 0x8D49
    GL_RENDERBUFFER_WIDTH = 0x8D42
    GL_RENDERBUFFER_HEIGHT = 0x8D43
    GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
    GL_RENDERBUFFER_RED_SIZE = 0x8D50
    GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
    GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
    GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
    GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
    GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
    GL_RENDERBUFFER_SAMPLES = 0x8CAB
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
    GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
    GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
    GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
    GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
    GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
    GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
    GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
    GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
    GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
    GL_SRGB = 0x8C40
    GL_UNSIGNED_NORMALIZED = 0x8C17
    GL_FRAMEBUFFER_DEFAULT = 0x8218
    GL_INDEX = 0x8222
    GL_COLOR_ATTACHMENT0 = 0x8CE0
    GL_COLOR_ATTACHMENT1 = 0x8CE1
    GL_COLOR_ATTACHMENT2 = 0x8CE2
    GL_COLOR_ATTACHMENT3 = 0x8CE3
    GL_COLOR_ATTACHMENT4 = 0x8CE4
    GL_COLOR_ATTACHMENT5 = 0x8CE5
    GL_COLOR_ATTACHMENT6 = 0x8CE6
    GL_COLOR_ATTACHMENT7 = 0x8CE7
    GL_COLOR_ATTACHMENT8 = 0x8CE8
    GL_COLOR_ATTACHMENT9 = 0x8CE9
    GL_COLOR_ATTACHMENT10 = 0x8CEA
    GL_COLOR_ATTACHMENT11 = 0x8CEB
    GL_COLOR_ATTACHMENT12 = 0x8CEC
    GL_COLOR_ATTACHMENT13 = 0x8CED
    GL_COLOR_ATTACHMENT14 = 0x8CEE
    GL_COLOR_ATTACHMENT15 = 0x8CEF
    GL_DEPTH_ATTACHMENT = 0x8D00
    GL_STENCIL_ATTACHMENT = 0x8D20
    GL_DEPTH_STENCIL_ATTACHMENT = 0x821A
    GL_MAX_SAMPLES = 0x8D57
    GL_FRAMEBUFFER_BINDING = 0x8CA6 # alias DRAW_FRAMEBUFFER_BINDING
    GL_DRAW_FRAMEBUFFER_BINDING = 0x8CA6
    GL_READ_FRAMEBUFFER_BINDING = 0x8CAA
    GL_RENDERBUFFER_BINDING = 0x8CA7
    GL_MAX_COLOR_ATTACHMENTS = 0x8CDF
    GL_MAX_RENDERBUFFER_SIZE = 0x84E8
    GL_FRAMEBUFFER_COMPLETE = 0x8CD5
    GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
    GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
    GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
    GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
    GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
    GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
    GL_FRAMEBUFFER_UNDEFINED = 0x8219
    GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506
    GL_DEPTH_STENCIL = 0x84F9
    GL_UNSIGNED_INT_24_8 = 0x84FA
    GL_DEPTH24_STENCIL8 = 0x88F0
    GL_TEXTURE_STENCIL_SIZE = 0x88F1
    
    @GLExtAPI.method(GLboolean, GLuint)
    def glIsRenderbuffer(renderbuffer: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLuint)
    def glBindRenderbuffer(target: int, renderbuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glDeleteRenderbuffers(n: int, renderbufers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glGenRenderbuffers(n: int, renderbuffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLsizei, GLsizei)
    def glRenderbufferStorage(target: int, internalformat: int, width: int, height: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizei, GLenum, GLsizei, GLsizei)
    def glRenderbufferStorageMultisample(target: int, samples: int, internalformat: int, width: int, height: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, PTR(GLint))
    def glGetRenderbufferParameteriv(target: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLboolean, GLuint)
    def glIsFramebuffer(framebuffer: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLuint)
    def glBindFramebuffer(target: int, framebuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glDeleteFramebuffers(n: int, framebuffers: IPointer[GLuint]): ...

    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glGenFramebuffers(n: int, framebuffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLenum, GLenum)
    def glCheckFramebufferStatus(target: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint)
    def glFramebufferTexture1D(target: int, attachment: int, textarget: int, texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint)
    def glFramebufferTexture2D(target: int, attachment: int, textarget: int, texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint, GLint, GLint)
    def glFramebufferTexture3D(target: int, attachment: int, textarget: int, texture: int, level: int, zoffset: int): ...

    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint)
    def glFramebufferTextureLayer(target: int, attachment: int, renderbuffertarget: int, renderbuffer: int): ...

    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLuint)
    def glFramebufferRenderbuffer(target: int, attachment: int, renderbuffertarget: int, renderbuffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, PTR(GLint))
    def glGetFramebufferAttachmentParameteriv(target: int, attachment: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum)
    def glBlitFramebuffer(srcX0: int, srcY0: int, srcX1: int, srcY1: INT, dstX0: int, dstY0: int, dstX1: int, dstY1: int, mask: int, filter: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum)
    def glGenerateMipmap(target: int): ...

GLintptr = INT_PTR
GLsizeiptr = ULONG_PTR
GLsizeiptrARB = ULONG_PTR
GLintptrARB = INT_PTR

class GL_ARB_invalidate_subdata:
    @GLExtAPI.method(GLvoid, GLuint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei)
    def glInvalidateTexSubImage(texture: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLint)
    def glInvalidateTexImage(texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLintptr, GLsizeiptr)
    def glInvalidateBufferSubData(buffer: int, offset: int, length: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glInvalidateBufferData(buffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizei, PTR(GLenum))
    def glInvalidateFramebuffer(target: int, numAttachments: int, attachments: IPointer[GLenum]): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizei, PTR(GLenum), GLint, GLint, GLsizei, GLsizei)
    def glInvalidateSubFramebuffer(target: int, numAttachments: int, attachments: IPointer[GLenum], x: int, y: int, width: int, height: int): ...

class GL_ARB_vertex_buffer_object:
    GL_GLX_CONTEXT_ALLOW_BUFFER_BYTE_ORDER_MISMATCH_ARB = 0x2095
    GL_ARRAY_BUFFER_ARB = 0x8892
    GL_ELEMENT_ARRAY_BUFFER_ARB = 0x8893
    GL_ARRAY_BUFFER_BINDING_ARB = 0x8894
    GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 0x8895
    GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 0x8896
    GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 0x8897
    GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x8898
    GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 0x8899
    GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 0x889A
    GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 0x889B
    GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x889C
    GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 0x889D
    GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 0x889E
    GL_STREAM_DRAW_ARB = 0x88E0
    GL_STREAM_READ_ARB = 0x88E1
    GL_STREAM_COPY_ARB = 0x88E2
    GL_STATIC_DRAW_ARB = 0x88E4
    GL_STATIC_READ_ARB = 0x88E5
    GL_STATIC_COPY_ARB = 0x88E6
    GL_DYNAMIC_DRAW_ARB = 0x88E8
    GL_DYNAMIC_READ_ARB = 0x88E9
    GL_DYNAMIC_COPY_ARB = 0x88EA
    GL_READ_ONLY_ARB = 0x88B8
    GL_WRITE_ONLY_ARB = 0x88B9
    GL_READ_WRITE_ARB = 0x88BA
    GL_BUFFER_SIZE_ARB = 0x8764
    GL_BUFFER_USAGE_ARB = 0x8765
    GL_BUFFER_ACCESS_ARB = 0x88BB
    GL_BUFFER_MAPPED_ARB = 0x88BC
    GL_BUFFER_MAP_POINTER_ARB = 0x88BD
    
    @GLExtAPI.method(GLvoid, GLenum, GLuint)
    def glBindBufferARB(target: int, buffer: int): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glDeleteBuffersARB(n: int, buffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLsizei, PTR(GLuint))
    def glGenBuffersARB(n: int, buffers: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLboolean, GLuint)
    def glIsBufferARB(buffer: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizeiptrARB, PVOID, GLenum)
    def glBufferDataARB(target: int, size: int, data: int, usage: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLsizeiptrARB, PVOID, GLenum)
    def glBufferSubDataARB(target: int, size: int, offset: int, data: int, usage: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLintptrARB, GLsizeiptrARB, PVOID)
    def glGetBufferSubDataARB(target: int, offset: int, size: int, data: int): ...
    
    @GLExtAPI.method(PVOID, GLenum, GLenum)
    def glMapBufferARB(target: int, access: int) -> int: ...
    
    @GLExtAPI.method(GLboolean, GLenum)
    def glUnmapBufferARB(target: int) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, PTR(GLint))
    def glGetBufferParameterivARB(target: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, PTR(PVOID))
    def glGetBufferPointervARB(target: int, pname: int, params: IPointer[PVOID]): ...

class GL_ARB_vertex_shader:
    GL_VERTEX_SHADER_ARB = 0x8B31
    GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 0x8B4A
    GL_MAX_VARYING_FLOATS_ARB = 0x8B4B
    GL_MAX_VERTEX_ATTRIBS_ARB = 0x8869
    GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 0x8872
    GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 0x8B4C
    GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 0x8B4D
    GL_MAX_TEXTURE_COORDS_ARB = 0x8871
    GL_VERTEX_PROGRAM_POINT_SIZE_ARB = 0x8642
    GL_VERTEX_PROGRAM_TWO_SIDE_ARB = 0x8643
    GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 0x8B89
    GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 0x8B8A
    GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = 0x8622
    GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = 0x8623
    GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = 0x8624
    GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = 0x8625
    GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = 0x886A
    GL_CURRENT_VERTEX_ATTRIB_ARB = 0x8626
    GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = 0x8645
    GL_FLOAT = 0x1406
    GL_FLOAT_VEC2_ARB = 0x8B50
    GL_FLOAT_VEC3_ARB = 0x8B51
    GL_FLOAT_VEC4_ARB = 0x8B52
    GL_FLOAT_MAT2_ARB = 0x8B5A
    GL_FLOAT_MAT3_ARB = 0x8B5B
    GL_FLOAT_MAT4_ARB = 0x8B5C
    
    @GLExtAPI.method(GLvoid, GLuint, GLfloat)
    def glVertexAttrib1fARB(index: int, v0: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLshort)
    def glVertexAttrib1sARB(index: int, v0: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLdouble)
    def glVertexAttrib1dARB(index: int, v0: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLfloat, GLfloat)
    def glVertexAttrib2fARB(index: int, v0: float, v1: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLshort, GLshort)
    def glVertexAttrib2sARB(index: int, v0: int, v1: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLdouble, GLdouble)
    def glVertexAttrib2dARB(index: int, v0: float, v1: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLfloat, GLfloat, GLfloat)
    def glVertexAttrib3fARB(index: int, v0: float, v1: float, v2: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLshort, GLshort, GLshort)
    def glVertexAttrib3sARB(index: int, v0: int, v1: int, v2: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLdouble, GLdouble, GLdouble)
    def glVertexAttrib3dARB(index: int, v0: float, v1: float, v2: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLfloat, GLfloat, GLfloat, GLfloat)
    def glVertexAttrib4fARB(index: int, v0: float, v1: float, v2: float, v3: float): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLshort, GLshort, GLshort, GLshort)
    def glVertexAttrib4sARB(index: int, v0: int, v1: int, v2: int, v3: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLdouble, GLdouble, GLdouble, GLdouble)
    def glVertexAttrib4dARB(index: int, v0: float, v1: float, v2: float, v3: float): ...

    @GLExtAPI.method(GLvoid, GLuint, GLubyte, GLubyte, GLubyte, GLubyte, GLubyte)
    def glVertexAttrib4NubARB(index: int, x: int, y: int, z: int, w: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLfloat))
    def glVertexAttrib1fvARB(index: int, v: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLshort))
    def glVertexAttrib1svARB(index: int, v: IPointer[GLshort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLdouble))
    def glVertexAttrib1dvARB(index: int, v: IPointer[GLdouble]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLfloat))
    def glVertexAttrib2fvARB(index: int, v: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLshort))
    def glVertexAttrib2svARB(index: int, v: IPointer[GLshort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLdouble))
    def glVertexAttrib2dvARB(index: int, v: IPointer[GLdouble]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLfloat))
    def glVertexAttrib3fvARB(index: int, v: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLshort))
    def glVertexAttrib3svARB(index: int, v: IPointer[GLshort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLdouble))
    def glVertexAttrib3dvARB(index: int, v: IPointer[GLdouble]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLfloat))
    def glVertexAttrib4fvARB(index: int, v: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLshort))
    def glVertexAttrib4svARB(index: int, v: IPointer[GLshort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLdouble))
    def glVertexAttrib4dvARB(index: int, v: IPointer[GLdouble]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLbyte))
    def glVertexAttrib4bvARB(index: int, v: IPointer[GLbyte]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLubyte))
    def glVertexAttrib4ubvARB(index: int, v: IPointer[GLubyte]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLushort))
    def glVertexAttrib4usvARB(index: int, v: IPointer[GLushort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLuint))
    def glVertexAttrib4uivARB(index: int, v: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLbyte))
    def glVertexAttrib4NbvARB(index: int, v: IPointer[GLbyte]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLshort))
    def glVertexAttrib4NsvARB(index: int, v: IPointer[GLshort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLint))
    def glVertexAttrib4NivARB(index: int, v: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLubyte))
    def glVertexAttrib4NubvARB(index: int, v: IPointer[GLubyte]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLushort))
    def glVertexAttrib4NusvARB(index: int, v: IPointer[GLushort]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, PTR(GLuint))
    def glVertexAttrib4NuivARB(index: int, v: IPointer[GLuint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLint, GLenum, GLboolean, GLsizei, PVOID)
    def glVertexAttribPointerARB(index: int, size: int, type: int, normalized: int, stride: int, pointer: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glEnableVertexAttribArrayARB(index: int): ...
    
    @GLExtAPI.method(GLvoid, GLuint)
    def glDisableVertexAttribArrayARB(index: int): ...
    
    @GLExtAPI.method(GLvoid, GLhandleARB, GLuint, LPSTR)
    def glBindAttribLocationARB(programObj: int, index: int, name: LPSTR): ...
    
    @GLExtAPI.method(GLint, GLhandleARB, LPSTR)
    def glGetAttribLocationARB(programObj: int, name: LPSTR) -> int: ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLdouble))
    def glGetVertexAttribdvARB(index: int, pname: int, params: IPointer[GLdouble]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLfloat))
    def glGetVertexAttribfvARB(index: int, pname: int, params: IPointer[GLfloat]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(GLint))
    def glGetVertexAttribivARB(index: int, pname: int, params: IPointer[GLint]): ...
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, PTR(PVOID))
    def glGetVertexAttribPointervARB(index: int, pname: int, params: IPointer[PVOID]): ...

class GL_ARB_fragment_shader:
    GL_FRAGMENT_SHADER_ARB = 0x8B30
    GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 0x8B49
    GL_MAX_TEXTURE_COORDS_ARB = 0x8871
    GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 0x8872
    GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 0x8B8B

class GL_EXT_geometry_shader4:
    GL_GEOMETRY_SHADER_EXT = 0x8DD9
    GL_GEOMETRY_VERTICES_OUT_EXT = 0x8DDA
    GL_GEOMETRY_INPUT_TYPE_EXT = 0x8DDB
    GL_GEOMETRY_OUTPUT_TYPE_EXT = 0x8DDC
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT = 0x8C29
    GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT = 0x8DDD
    GL_MAX_VERTEX_VARYING_COMPONENTS_EXT = 0x8DDE
    GL_MAX_VARYING_COMPONENTS_EXT = 0x8B4B
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT = 0x8DDF
    GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT = 0x8DE0
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT = 0x8DE1
    GL_LINES_ADJACENCY_EXT = 0xA
    GL_LINE_STRIP_ADJACENCY_EXT = 0xB
    GL_TRIANGLES_ADJACENCY_EXT = 0xC
    GL_TRIANGLE_STRIP_ADJACENCY_EXT = 0xD
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT = 0x8DA8
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT = 0x8DA9
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT = 0x8DA7
    GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT = 0x8CD4
    GL_PROGRAM_POINT_SIZE_EXT = 0x8642
    
    @GLExtAPI.method(GLvoid, GLuint, GLenum, GLint)
    def glProgramParameteriEXT(program: int, pname: int, value: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLuint, GLint)
    def glFramebufferTextureEXT(target: int, attachment: int, texture: int, level: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLuint, GLint, GLint)
    def glFramebufferTextureLayerEXT(target: int, attachment: int, texture: int, level: int, layer: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLuint, GLint, GLint)
    def glFramebufferTextureFaceEXT(target: int, attachment: int, texture: int, level: int, face: int): ...

class GL_EXT_blend_equation_separate:
    GL_BLEND_EQUATION_RGB_EXT = 0x8009
    GL_BLEND_EQUATION_ALPHA_EXT = 0x883D
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum)
    def glBlendEquationSeparateEXT(modeRGB: int, modeAlpha: int): ...

class GL_EXT_blend_func_separate:
    GL_BLEND_DST_RGB_EXT = 0x80C8
    GL_BLEND_SRC_RGB_EXT = 0x80C9
    GL_BLEND_DST_ALPHA_EXT = 0x80CA
    GL_BLEND_SRC_ALPHA_EXT = 0x80CB
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLenum)
    def glBlendFuncSeparateEXT(sfactorRGB: int, dfactorRGB: int, sfactorAlpha: int, dfactorAlpha: int): ...

class GL_ATI_separate_stencil:
    GL_STENCIL_BACK_FUNC_ATI = 0x8800
    GL_STENCIL_BACK_FAIL_ATI = 0x8801
    GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI = 0x8802
    GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI = 0x8803
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLenum, GLenum)
    def glStencilOpSeparateATI(face: int, sfail: int, dpfail: int, dppass: int): ...
    
    @GLExtAPI.method(GLvoid, GLenum, GLenum, GLint, GLuint)
    def glStencilFuncSeparateATI(frontfunc: int, backfunc: int, ref: int, mask: int): ...

class GL_EXT_blend_minmax:
    GL_FUNC_ADD_EXT = 0x8006
    GL_MIN_EXT = 0x8007
    GL_MAX_EXT = 0x8008
    GL_BLEND_EQUATION_EXT = 0x8009

    @GLExtAPI.method(GLvoid, GLenum)
    def glBlendEquationEXT(mode: int): ...

class GL_EXT_blend_subtract:
    GL_FUNC_SUBTRACT_EXT = 0x800A
    GL_FUNC_REVERSE_SUBTRACT_EXT = 0x800B

class GL_ARB_multisample:
    WGL_SAMPLE_BUFFERS_ARB = 0x2041
    WGL_SAMPLES_ARB = 0x2042
    GL_MULTISAMPLE_ARB = 0x809D
    GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 0x809E
    GL_SAMPLE_ALPHA_TO_ONE_ARB = 0x809F
    GL_SAMPLE_COVERAGE_ARB = 0x80A0
    GL_MULTISAMPLE_BIT_ARB = 0x20000000
    GL_SAMPLE_BUFFERS_ARB = 0x80A8
    GL_SAMPLES_ARB = 0x80A9
    GL_SAMPLE_COVERAGE_VALUE_ARB = 0x80AA
    GL_SAMPLE_COVERAGE_INVERT_ARB = 0x80AB
    
    @GLExtAPI.method(GLvoid, GLclampf, GLboolean)
    def glSampleCoverageARB(value: float, invert: int): ...

class GLExt(
    WGL_EXT_swap_control, GL_EXT_abgr, GL_EXT_bgra, WGL_EXT_pixel_format,
    GL_EXT_texture_swizzle, GL_EXT_stencil_wrap, GL_EXT_fog_coord, 
    GL_EXT_blend_color, GL_EXT_cull_vertex, GL_EXT_index_material, 
    GL_EXT_index_func, GL_EXT_light_texture, GL_EXT_polygon_offset, 
    GL_EXT_texture, WGL_EXT_extensions_string, GL_EXT_vertex_shader,
    GL_EXT_framebuffer_object, GL_ARB_shader_objects, GL_ARB_framebuffer_object,
    GL_ARB_invalidate_subdata, GL_ARB_vertex_buffer_object, GL_ARB_vertex_shader,
    GL_ARB_fragment_shader, GL_EXT_geometry_shader4, GL_EXT_blend_equation_separate,
    GL_EXT_blend_func_separate, GL_ATI_separate_stencil):
    """
    Open GL extensions collection.
    """
    