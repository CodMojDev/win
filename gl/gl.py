"""++ BUILD Version: 0004    // Increment this if a change has global effects

Copyright (c) 1985-96, Microsoft Corporation

Module Name:

    gl.h

Abstract:

    Procedure declarations, constant definitions and macros for the OpenGL
    component.

--"""

from .. import cpreproc

from ..minwindef import *

from ..defbase import declare

if cpreproc.ifndef("__gl_h_"):
    if cpreproc.ifndef("__GL_H__"):
        cpreproc.define("__gl_h_")
        cpreproc.define("__GL_H__")

        opengl32 = W_WinDLL("opengl32.dll")

        """
        ** Copyright 1996 Silicon Graphics, Inc.
        ** All Rights Reserved.
        **
        ** This is UNPUBLISHED PROPRIETARY SOURCE CODE of Silicon Graphics, Inc.;
        ** the contents of this file may not be disclosed to third parties, copied or
        ** duplicated in any form, in whole or in part, without the prior written
        ** permission of Silicon Graphics, Inc.
        **
        ** RESTRICTED RIGHTS LEGEND:
        ** Use, duplication or disclosure by the Government is subject to restrictions
        ** as set forth in subdivision (c)(1)(ii) of the Rights in Technical Data
        ** and Computer Software clause at DFARS 252.227-7013, and/or in similar or
        ** successor clauses in the FAR, DOD or NASA FAR Supplement. Unpublished -
        ** rights reserved under the Copyright Laws of the United States.
        """

        # REGION *** Desktop Family ***

        GLenum = UINT
        GLboolean = BOOLEAN
        GLbitfield = UINT
        GLbyte = c_byte
        GLshort = SHORT
        GLint = INT
        GLsizei = INT
        GLubyte = BYTE
        GLushort = USHORT
        GLuint = UINT
        GLfloat = FLOAT
        GLclampf = FLOAT
        GLdouble = DOUBLE
        GLclampd = DOUBLE
        GLvoid = VOID

        #***********************************************************
        # Version
        GL_VERSION_1_1 = 1
        # AccumOp
        GL_ACCUM = 0x0100
        GL_LOAD = 0x0101
        GL_RETURN = 0x0102
        GL_MULT = 0x0103
        GL_ADD = 0x0104
        # AlphaFunction
        GL_NEVER = 0x0200
        GL_LESS = 0x0201
        GL_EQUAL = 0x0202
        GL_LEQUAL = 0x0203
        GL_GREATER = 0x0204
        GL_NOTEQUAL = 0x0205
        GL_GEQUAL = 0x0206
        GL_ALWAYS = 0x0207
        # AttribMask
        GL_CURRENT_BIT = 0x00000001
        GL_POINT_BIT = 0x00000002
        GL_LINE_BIT = 0x00000004
        GL_POLYGON_BIT = 0x00000008
        GL_POLYGON_STIPPLE_BIT = 0x00000010
        GL_PIXEL_MODE_BIT = 0x00000020
        GL_LIGHTING_BIT = 0x00000040
        GL_FOG_BIT = 0x00000080
        GL_DEPTH_BUFFER_BIT = 0x00000100
        GL_ACCUM_BUFFER_BIT = 0x00000200
        GL_STENCIL_BUFFER_BIT = 0x00000400
        GL_VIEWPORT_BIT = 0x00000800
        GL_TRANSFORM_BIT = 0x00001000
        GL_ENABLE_BIT = 0x00002000
        GL_COLOR_BUFFER_BIT = 0x00004000
        GL_HINT_BIT = 0x00008000
        GL_EVAL_BIT = 0x00010000
        GL_LIST_BIT = 0x00020000
        GL_TEXTURE_BIT = 0x00040000
        GL_SCISSOR_BIT = 0x00080000
        GL_ALL_ATTRIB_BITS = 0x000fffff
        # BeginMode
        GL_POINTS = 0x0000
        GL_LINES = 0x0001
        GL_LINE_LOOP = 0x0002
        GL_LINE_STRIP = 0x0003
        GL_TRIANGLES = 0x0004
        GL_TRIANGLE_STRIP = 0x0005
        GL_TRIANGLE_FAN = 0x0006
        GL_QUADS = 0x0007
        GL_QUAD_STRIP = 0x0008
        GL_POLYGON = 0x0009
        # BlendingFactorDest
        GL_ZERO = 0
        GL_ONE = 1
        GL_SRC_COLOR = 0x0300
        GL_ONE_MINUS_SRC_COLOR = 0x0301
        GL_SRC_ALPHA = 0x0302
        GL_ONE_MINUS_SRC_ALPHA = 0x0303
        GL_DST_ALPHA = 0x0304
        GL_ONE_MINUS_DST_ALPHA = 0x0305
        # BlendingFactorSrc
        #      GL_ZERO
        #      GL_ONE
        GL_DST_COLOR = 0x0306
        GL_ONE_MINUS_DST_COLOR = 0x0307
        GL_SRC_ALPHA_SATURATE = 0x0308
        #      GL_SRC_ALPHA
        #      GL_ONE_MINUS_SRC_ALPHA
        #      GL_DST_ALPHA
        #      GL_ONE_MINUS_DST_ALPHA
        # Boolean
        GL_TRUE = 1
        GL_FALSE = 0
        # ClearBufferMask
        #      GL_COLOR_BUFFER_BIT
        #      GL_ACCUM_BUFFER_BIT
        #      GL_STENCIL_BUFFER_BIT
        #      GL_DEPTH_BUFFER_BIT
        # ClientArrayType
        #      GL_VERTEX_ARRAY
        #      GL_NORMAL_ARRAY
        #      GL_COLOR_ARRAY
        #      GL_INDEX_ARRAY
        #      GL_TEXTURE_COORD_ARRAY
        #      GL_EDGE_FLAG_ARRAY
        # ClipPlaneName
        GL_CLIP_PLANE0 = 0x3000
        GL_CLIP_PLANE1 = 0x3001
        GL_CLIP_PLANE2 = 0x3002
        GL_CLIP_PLANE3 = 0x3003
        GL_CLIP_PLANE4 = 0x3004
        GL_CLIP_PLANE5 = 0x3005
        # ColorMaterialFace
        #      GL_FRONT
        #      GL_BACK
        #      GL_FRONT_AND_BACK
        # ColorMaterialParameter
        #      GL_AMBIENT
        #      GL_DIFFUSE
        #      GL_SPECULAR
        #      GL_EMISSION
        #      GL_AMBIENT_AND_DIFFUSE
        # ColorPointerType
        #      GL_BYTE
        #      GL_UNSIGNED_BYTE
        #      GL_SHORT
        #      GL_UNSIGNED_SHORT
        #      GL_INT
        #      GL_UNSIGNED_INT
        #      GL_FLOAT
        #      GL_DOUBLE
        # CullFaceMode
        #      GL_FRONT
        #      GL_BACK
        #      GL_FRONT_AND_BACK
        # DataType
        GL_BYTE = 0x1400
        GL_UNSIGNED_BYTE = 0x1401
        GL_SHORT = 0x1402
        GL_UNSIGNED_SHORT = 0x1403
        GL_INT = 0x1404
        GL_UNSIGNED_INT = 0x1405
        GL_FLOAT = 0x1406
        GL_2_BYTES = 0x1407
        GL_3_BYTES = 0x1408
        GL_4_BYTES = 0x1409
        GL_DOUBLE = 0x140A
        # DepthFunction
        #      GL_NEVER
        #      GL_LESS
        #      GL_EQUAL
        #      GL_LEQUAL
        #      GL_GREATER
        #      GL_NOTEQUAL
        #      GL_GEQUAL
        #      GL_ALWAYS
        # DrawBufferMode
        GL_NONE = 0
        GL_FRONT_LEFT = 0x0400
        GL_FRONT_RIGHT = 0x0401
        GL_BACK_LEFT = 0x0402
        GL_BACK_RIGHT = 0x0403
        GL_FRONT = 0x0404
        GL_BACK = 0x0405
        GL_LEFT = 0x0406
        GL_RIGHT = 0x0407
        GL_FRONT_AND_BACK = 0x0408
        GL_AUX0 = 0x0409
        GL_AUX1 = 0x040A
        GL_AUX2 = 0x040B
        GL_AUX3 = 0x040C
        # Enable
        #      GL_FOG
        #      GL_LIGHTING
        #      GL_TEXTURE_1D
        #      GL_TEXTURE_2D
        #      GL_LINE_STIPPLE
        #      GL_POLYGON_STIPPLE
        #      GL_CULL_FACE
        #      GL_ALPHA_TEST
        #      GL_BLEND
        #      GL_INDEX_LOGIC_OP
        #      GL_COLOR_LOGIC_OP
        #      GL_DITHER
        #      GL_STENCIL_TEST
        #      GL_DEPTH_TEST
        #      GL_CLIP_PLANE0
        #      GL_CLIP_PLANE1
        #      GL_CLIP_PLANE2
        #      GL_CLIP_PLANE3
        #      GL_CLIP_PLANE4
        #      GL_CLIP_PLANE5
        #      GL_LIGHT0
        #      GL_LIGHT1
        #      GL_LIGHT2
        #      GL_LIGHT3
        #      GL_LIGHT4
        #      GL_LIGHT5
        #      GL_LIGHT6
        #      GL_LIGHT7
        #      GL_TEXTURE_GEN_S
        #      GL_TEXTURE_GEN_T
        #      GL_TEXTURE_GEN_R
        #      GL_TEXTURE_GEN_Q
        #      GL_MAP1_VERTEX_3
        #      GL_MAP1_VERTEX_4
        #      GL_MAP1_COLOR_4
        #      GL_MAP1_INDEX
        #      GL_MAP1_NORMAL
        #      GL_MAP1_TEXTURE_COORD_1
        #      GL_MAP1_TEXTURE_COORD_2
        #      GL_MAP1_TEXTURE_COORD_3
        #      GL_MAP1_TEXTURE_COORD_4
        #      GL_MAP2_VERTEX_3
        #      GL_MAP2_VERTEX_4
        #      GL_MAP2_COLOR_4
        #      GL_MAP2_INDEX
        #      GL_MAP2_NORMAL
        #      GL_MAP2_TEXTURE_COORD_1
        #      GL_MAP2_TEXTURE_COORD_2
        #      GL_MAP2_TEXTURE_COORD_3
        #      GL_MAP2_TEXTURE_COORD_4
        #      GL_POINT_SMOOTH
        #      GL_LINE_SMOOTH
        #      GL_POLYGON_SMOOTH
        #      GL_SCISSOR_TEST
        #      GL_COLOR_MATERIAL
        #      GL_NORMALIZE
        #      GL_AUTO_NORMAL
        #      GL_VERTEX_ARRAY
        #      GL_NORMAL_ARRAY
        #      GL_COLOR_ARRAY
        #      GL_INDEX_ARRAY
        #      GL_TEXTURE_COORD_ARRAY
        #      GL_EDGE_FLAG_ARRAY
        #      GL_POLYGON_OFFSET_POINT
        #      GL_POLYGON_OFFSET_LINE
        #      GL_POLYGON_OFFSET_FILL
        # ErrorCode
        GL_NO_ERROR = 0
        GL_INVALID_ENUM = 0x0500
        GL_INVALID_VALUE = 0x0501
        GL_INVALID_OPERATION = 0x0502
        GL_STACK_OVERFLOW = 0x0503
        GL_STACK_UNDERFLOW = 0x0504
        GL_OUT_OF_MEMORY = 0x0505
        # FeedBackMode
        GL_2D = 0x0600
        GL_3D = 0x0601
        GL_3D_COLOR = 0x0602
        GL_3D_COLOR_TEXTURE = 0x0603
        GL_4D_COLOR_TEXTURE = 0x0604
        # FeedBackToken
        GL_PASS_THROUGH_TOKEN = 0x0700
        GL_POINT_TOKEN = 0x0701
        GL_LINE_TOKEN = 0x0702
        GL_POLYGON_TOKEN = 0x0703
        GL_BITMAP_TOKEN = 0x0704
        GL_DRAW_PIXEL_TOKEN = 0x0705
        GL_COPY_PIXEL_TOKEN = 0x0706
        GL_LINE_RESET_TOKEN = 0x0707
        # FogMode
        #      GL_LINEAR
        GL_EXP = 0x0800
        GL_EXP2 = 0x0801
        # FogParameter
        #      GL_FOG_COLOR
        #      GL_FOG_DENSITY
        #      GL_FOG_END
        #      GL_FOG_INDEX
        #      GL_FOG_MODE
        #      GL_FOG_START
        # FrontFaceDirection
        GL_CW = 0x0900
        GL_CCW = 0x0901
        # GetMapTarget
        GL_COEFF = 0x0A00
        GL_ORDER = 0x0A01
        GL_DOMAIN = 0x0A02
        # GetPixelMap
        #      GL_PIXEL_MAP_I_TO_I
        #      GL_PIXEL_MAP_S_TO_S
        #      GL_PIXEL_MAP_I_TO_R
        #      GL_PIXEL_MAP_I_TO_G
        #      GL_PIXEL_MAP_I_TO_B
        #      GL_PIXEL_MAP_I_TO_A
        #      GL_PIXEL_MAP_R_TO_R
        #      GL_PIXEL_MAP_G_TO_G
        #      GL_PIXEL_MAP_B_TO_B
        #      GL_PIXEL_MAP_A_TO_A
        # GetPointerTarget
        #      GL_VERTEX_ARRAY_POINTER
        #      GL_NORMAL_ARRAY_POINTER
        #      GL_COLOR_ARRAY_POINTER
        #      GL_INDEX_ARRAY_POINTER
        #      GL_TEXTURE_COORD_ARRAY_POINTER
        #      GL_EDGE_FLAG_ARRAY_POINTER
        # GetTarget
        GL_CURRENT_COLOR = 0x0B00
        GL_CURRENT_INDEX = 0x0B01
        GL_CURRENT_NORMAL = 0x0B02
        GL_CURRENT_TEXTURE_COORDS = 0x0B03
        GL_CURRENT_RASTER_COLOR = 0x0B04
        GL_CURRENT_RASTER_INDEX = 0x0B05
        GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
        GL_CURRENT_RASTER_POSITION = 0x0B07
        GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
        GL_CURRENT_RASTER_DISTANCE = 0x0B09
        GL_POINT_SMOOTH = 0x0B10
        GL_POINT_SIZE = 0x0B11
        GL_POINT_SIZE_RANGE = 0x0B12
        GL_POINT_SIZE_GRANULARITY = 0x0B13
        GL_LINE_SMOOTH = 0x0B20
        GL_LINE_WIDTH = 0x0B21
        GL_LINE_WIDTH_RANGE = 0x0B22
        GL_LINE_WIDTH_GRANULARITY = 0x0B23
        GL_LINE_STIPPLE = 0x0B24
        GL_LINE_STIPPLE_PATTERN = 0x0B25
        GL_LINE_STIPPLE_REPEAT = 0x0B26
        GL_LIST_MODE = 0x0B30
        GL_MAX_LIST_NESTING = 0x0B31
        GL_LIST_BASE = 0x0B32
        GL_LIST_INDEX = 0x0B33
        GL_POLYGON_MODE = 0x0B40
        GL_POLYGON_SMOOTH = 0x0B41
        GL_POLYGON_STIPPLE = 0x0B42
        GL_EDGE_FLAG = 0x0B43
        GL_CULL_FACE = 0x0B44
        GL_CULL_FACE_MODE = 0x0B45
        GL_FRONT_FACE = 0x0B46
        GL_LIGHTING = 0x0B50
        GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
        GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
        GL_LIGHT_MODEL_AMBIENT = 0x0B53
        GL_SHADE_MODEL = 0x0B54
        GL_COLOR_MATERIAL_FACE = 0x0B55
        GL_COLOR_MATERIAL_PARAMETER = 0x0B56
        GL_COLOR_MATERIAL = 0x0B57
        GL_FOG = 0x0B60
        GL_FOG_INDEX = 0x0B61
        GL_FOG_DENSITY = 0x0B62
        GL_FOG_START = 0x0B63
        GL_FOG_END = 0x0B64
        GL_FOG_MODE = 0x0B65
        GL_FOG_COLOR = 0x0B66
        GL_DEPTH_RANGE = 0x0B70
        GL_DEPTH_TEST = 0x0B71
        GL_DEPTH_WRITEMASK = 0x0B72
        GL_DEPTH_CLEAR_VALUE = 0x0B73
        GL_DEPTH_FUNC = 0x0B74
        GL_ACCUM_CLEAR_VALUE = 0x0B80
        GL_STENCIL_TEST = 0x0B90
        GL_STENCIL_CLEAR_VALUE = 0x0B91
        GL_STENCIL_FUNC = 0x0B92
        GL_STENCIL_VALUE_MASK = 0x0B93
        GL_STENCIL_FAIL = 0x0B94
        GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
        GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
        GL_STENCIL_REF = 0x0B97
        GL_STENCIL_WRITEMASK = 0x0B98
        GL_MATRIX_MODE = 0x0BA0
        GL_NORMALIZE = 0x0BA1
        GL_VIEWPORT = 0x0BA2
        GL_MODELVIEW_STACK_DEPTH = 0x0BA3
        GL_PROJECTION_STACK_DEPTH = 0x0BA4
        GL_TEXTURE_STACK_DEPTH = 0x0BA5
        GL_MODELVIEW_MATRIX = 0x0BA6
        GL_PROJECTION_MATRIX = 0x0BA7
        GL_TEXTURE_MATRIX = 0x0BA8
        GL_ATTRIB_STACK_DEPTH = 0x0BB0
        GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
        GL_ALPHA_TEST = 0x0BC0
        GL_ALPHA_TEST_FUNC = 0x0BC1
        GL_ALPHA_TEST_REF = 0x0BC2
        GL_DITHER = 0x0BD0
        GL_BLEND_DST = 0x0BE0
        GL_BLEND_SRC = 0x0BE1
        GL_BLEND = 0x0BE2
        GL_LOGIC_OP_MODE = 0x0BF0
        GL_INDEX_LOGIC_OP = 0x0BF1
        GL_COLOR_LOGIC_OP = 0x0BF2
        GL_AUX_BUFFERS = 0x0C00
        GL_DRAW_BUFFER = 0x0C01
        GL_READ_BUFFER = 0x0C02
        GL_SCISSOR_BOX = 0x0C10
        GL_SCISSOR_TEST = 0x0C11
        GL_INDEX_CLEAR_VALUE = 0x0C20
        GL_INDEX_WRITEMASK = 0x0C21
        GL_COLOR_CLEAR_VALUE = 0x0C22
        GL_COLOR_WRITEMASK = 0x0C23
        GL_INDEX_MODE = 0x0C30
        GL_RGBA_MODE = 0x0C31
        GL_DOUBLEBUFFER = 0x0C32
        GL_STEREO = 0x0C33
        GL_RENDER_MODE = 0x0C40
        GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
        GL_POINT_SMOOTH_HINT = 0x0C51
        GL_LINE_SMOOTH_HINT = 0x0C52
        GL_POLYGON_SMOOTH_HINT = 0x0C53
        GL_FOG_HINT = 0x0C54
        GL_TEXTURE_GEN_S = 0x0C60
        GL_TEXTURE_GEN_T = 0x0C61
        GL_TEXTURE_GEN_R = 0x0C62
        GL_TEXTURE_GEN_Q = 0x0C63
        GL_PIXEL_MAP_I_TO_I = 0x0C70
        GL_PIXEL_MAP_S_TO_S = 0x0C71
        GL_PIXEL_MAP_I_TO_R = 0x0C72
        GL_PIXEL_MAP_I_TO_G = 0x0C73
        GL_PIXEL_MAP_I_TO_B = 0x0C74
        GL_PIXEL_MAP_I_TO_A = 0x0C75
        GL_PIXEL_MAP_R_TO_R = 0x0C76
        GL_PIXEL_MAP_G_TO_G = 0x0C77
        GL_PIXEL_MAP_B_TO_B = 0x0C78
        GL_PIXEL_MAP_A_TO_A = 0x0C79
        GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
        GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
        GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
        GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
        GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
        GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
        GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
        GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
        GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
        GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
        GL_UNPACK_SWAP_BYTES = 0x0CF0
        GL_UNPACK_LSB_FIRST = 0x0CF1
        GL_UNPACK_ROW_LENGTH = 0x0CF2
        GL_UNPACK_SKIP_ROWS = 0x0CF3
        GL_UNPACK_SKIP_PIXELS = 0x0CF4
        GL_UNPACK_ALIGNMENT = 0x0CF5
        GL_PACK_SWAP_BYTES = 0x0D00
        GL_PACK_LSB_FIRST = 0x0D01
        GL_PACK_ROW_LENGTH = 0x0D02
        GL_PACK_SKIP_ROWS = 0x0D03
        GL_PACK_SKIP_PIXELS = 0x0D04
        GL_PACK_ALIGNMENT = 0x0D05
        GL_MAP_COLOR = 0x0D10
        GL_MAP_STENCIL = 0x0D11
        GL_INDEX_SHIFT = 0x0D12
        GL_INDEX_OFFSET = 0x0D13
        GL_RED_SCALE = 0x0D14
        GL_RED_BIAS = 0x0D15
        GL_ZOOM_X = 0x0D16
        GL_ZOOM_Y = 0x0D17
        GL_GREEN_SCALE = 0x0D18
        GL_GREEN_BIAS = 0x0D19
        GL_BLUE_SCALE = 0x0D1A
        GL_BLUE_BIAS = 0x0D1B
        GL_ALPHA_SCALE = 0x0D1C
        GL_ALPHA_BIAS = 0x0D1D
        GL_DEPTH_SCALE = 0x0D1E
        GL_DEPTH_BIAS = 0x0D1F
        GL_MAX_EVAL_ORDER = 0x0D30
        GL_MAX_LIGHTS = 0x0D31
        GL_MAX_CLIP_PLANES = 0x0D32
        GL_MAX_TEXTURE_SIZE = 0x0D33
        GL_MAX_PIXEL_MAP_TABLE = 0x0D34
        GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
        GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
        GL_MAX_NAME_STACK_DEPTH = 0x0D37
        GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
        GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
        GL_MAX_VIEWPORT_DIMS = 0x0D3A
        GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
        GL_SUBPIXEL_BITS = 0x0D50
        GL_INDEX_BITS = 0x0D51
        GL_RED_BITS = 0x0D52
        GL_GREEN_BITS = 0x0D53
        GL_BLUE_BITS = 0x0D54
        GL_ALPHA_BITS = 0x0D55
        GL_DEPTH_BITS = 0x0D56
        GL_STENCIL_BITS = 0x0D57
        GL_ACCUM_RED_BITS = 0x0D58
        GL_ACCUM_GREEN_BITS = 0x0D59
        GL_ACCUM_BLUE_BITS = 0x0D5A
        GL_ACCUM_ALPHA_BITS = 0x0D5B
        GL_NAME_STACK_DEPTH = 0x0D70
        GL_AUTO_NORMAL = 0x0D80
        GL_MAP1_COLOR_4 = 0x0D90
        GL_MAP1_INDEX = 0x0D91
        GL_MAP1_NORMAL = 0x0D92
        GL_MAP1_TEXTURE_COORD_1 = 0x0D93
        GL_MAP1_TEXTURE_COORD_2 = 0x0D94
        GL_MAP1_TEXTURE_COORD_3 = 0x0D95
        GL_MAP1_TEXTURE_COORD_4 = 0x0D96
        GL_MAP1_VERTEX_3 = 0x0D97
        GL_MAP1_VERTEX_4 = 0x0D98
        GL_MAP2_COLOR_4 = 0x0DB0
        GL_MAP2_INDEX = 0x0DB1
        GL_MAP2_NORMAL = 0x0DB2
        GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
        GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
        GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
        GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
        GL_MAP2_VERTEX_3 = 0x0DB7
        GL_MAP2_VERTEX_4 = 0x0DB8
        GL_MAP1_GRID_DOMAIN = 0x0DD0
        GL_MAP1_GRID_SEGMENTS = 0x0DD1
        GL_MAP2_GRID_DOMAIN = 0x0DD2
        GL_MAP2_GRID_SEGMENTS = 0x0DD3
        GL_TEXTURE_1D = 0x0DE0
        GL_TEXTURE_2D = 0x0DE1
        GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
        GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
        GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
        GL_SELECTION_BUFFER_POINTER = 0x0DF3
        GL_SELECTION_BUFFER_SIZE = 0x0DF4
        #      GL_TEXTURE_BINDING_1D
        #      GL_TEXTURE_BINDING_2D
        #      GL_VERTEX_ARRAY
        #      GL_NORMAL_ARRAY
        #      GL_COLOR_ARRAY
        #      GL_INDEX_ARRAY
        #      GL_TEXTURE_COORD_ARRAY
        #      GL_EDGE_FLAG_ARRAY
        #      GL_VERTEX_ARRAY_SIZE
        #      GL_VERTEX_ARRAY_TYPE
        #      GL_VERTEX_ARRAY_STRIDE
        #      GL_NORMAL_ARRAY_TYPE
        #      GL_NORMAL_ARRAY_STRIDE
        #      GL_COLOR_ARRAY_SIZE
        #      GL_COLOR_ARRAY_TYPE
        #      GL_COLOR_ARRAY_STRIDE
        #      GL_INDEX_ARRAY_TYPE
        #      GL_INDEX_ARRAY_STRIDE
        #      GL_TEXTURE_COORD_ARRAY_SIZE
        #      GL_TEXTURE_COORD_ARRAY_TYPE
        #      GL_TEXTURE_COORD_ARRAY_STRIDE
        #      GL_EDGE_FLAG_ARRAY_STRIDE
        #      GL_POLYGON_OFFSET_FACTOR
        #      GL_POLYGON_OFFSET_UNITS
        # GetTextureParameter
        #      GL_TEXTURE_MAG_FILTER
        #      GL_TEXTURE_MIN_FILTER
        #      GL_TEXTURE_WRAP_S
        #      GL_TEXTURE_WRAP_T
        GL_TEXTURE_WIDTH = 0x1000
        GL_TEXTURE_HEIGHT = 0x1001
        GL_TEXTURE_INTERNAL_FORMAT = 0x1003
        GL_TEXTURE_BORDER_COLOR = 0x1004
        GL_TEXTURE_BORDER = 0x1005
        #      GL_TEXTURE_RED_SIZE
        #      GL_TEXTURE_GREEN_SIZE
        #      GL_TEXTURE_BLUE_SIZE
        #      GL_TEXTURE_ALPHA_SIZE
        #      GL_TEXTURE_LUMINANCE_SIZE
        #      GL_TEXTURE_INTENSITY_SIZE
        #      GL_TEXTURE_PRIORITY
        #      GL_TEXTURE_RESIDENT
        # HintMode
        GL_DONT_CARE = 0x1100
        GL_FASTEST = 0x1101
        GL_NICEST = 0x1102
        # HintTarget
        #      GL_PERSPECTIVE_CORRECTION_HINT
        #      GL_POINT_SMOOTH_HINT
        #      GL_LINE_SMOOTH_HINT
        #      GL_POLYGON_SMOOTH_HINT
        #      GL_FOG_HINT
        #      GL_PHONG_HINT
        # IndexPointerType
        #      GL_SHORT
        #      GL_INT
        #      GL_FLOAT
        #      GL_DOUBLE
        # LightModelParameter
        #      GL_LIGHT_MODEL_AMBIENT
        #      GL_LIGHT_MODEL_LOCAL_VIEWER
        #      GL_LIGHT_MODEL_TWO_SIDE
        # LightName
        GL_LIGHT0 = 0x4000
        GL_LIGHT1 = 0x4001
        GL_LIGHT2 = 0x4002
        GL_LIGHT3 = 0x4003
        GL_LIGHT4 = 0x4004
        GL_LIGHT5 = 0x4005
        GL_LIGHT6 = 0x4006
        GL_LIGHT7 = 0x4007
        # LightParameter
        GL_AMBIENT = 0x1200
        GL_DIFFUSE = 0x1201
        GL_SPECULAR = 0x1202
        GL_POSITION = 0x1203
        GL_SPOT_DIRECTION = 0x1204
        GL_SPOT_EXPONENT = 0x1205
        GL_SPOT_CUTOFF = 0x1206
        GL_CONSTANT_ATTENUATION = 0x1207
        GL_LINEAR_ATTENUATION = 0x1208
        GL_QUADRATIC_ATTENUATION = 0x1209
        # InterleavedArrays
        #      GL_V2F
        #      GL_V3F
        #      GL_C4UB_V2F
        #      GL_C4UB_V3F
        #      GL_C3F_V3F
        #      GL_N3F_V3F
        #      GL_C4F_N3F_V3F
        #      GL_T2F_V3F
        #      GL_T4F_V4F
        #      GL_T2F_C4UB_V3F
        #      GL_T2F_C3F_V3F
        #      GL_T2F_N3F_V3F
        #      GL_T2F_C4F_N3F_V3F
        #      GL_T4F_C4F_N3F_V4F
        # ListMode
        GL_COMPILE = 0x1300
        GL_COMPILE_AND_EXECUTE = 0x1301
        # ListNameType
        #      GL_BYTE
        #      GL_UNSIGNED_BYTE
        #      GL_SHORT
        #      GL_UNSIGNED_SHORT
        #      GL_INT
        #      GL_UNSIGNED_INT
        #      GL_FLOAT
        #      GL_2_BYTES
        #      GL_3_BYTES
        #      GL_4_BYTES
        # LogicOp
        GL_CLEAR = 0x1500
        GL_AND = 0x1501
        GL_AND_REVERSE = 0x1502
        GL_COPY = 0x1503
        GL_AND_INVERTED = 0x1504
        GL_NOOP = 0x1505
        GL_XOR = 0x1506
        GL_OR = 0x1507
        GL_NOR = 0x1508
        GL_EQUIV = 0x1509
        GL_INVERT = 0x150A
        GL_OR_REVERSE = 0x150B
        GL_COPY_INVERTED = 0x150C
        GL_OR_INVERTED = 0x150D
        GL_NAND = 0x150E
        GL_SET = 0x150F
        # MapTarget
        #      GL_MAP1_COLOR_4
        #      GL_MAP1_INDEX
        #      GL_MAP1_NORMAL
        #      GL_MAP1_TEXTURE_COORD_1
        #      GL_MAP1_TEXTURE_COORD_2
        #      GL_MAP1_TEXTURE_COORD_3
        #      GL_MAP1_TEXTURE_COORD_4
        #      GL_MAP1_VERTEX_3
        #      GL_MAP1_VERTEX_4
        #      GL_MAP2_COLOR_4
        #      GL_MAP2_INDEX
        #      GL_MAP2_NORMAL
        #      GL_MAP2_TEXTURE_COORD_1
        #      GL_MAP2_TEXTURE_COORD_2
        #      GL_MAP2_TEXTURE_COORD_3
        #      GL_MAP2_TEXTURE_COORD_4
        #      GL_MAP2_VERTEX_3
        #      GL_MAP2_VERTEX_4
        # MaterialFace
        #      GL_FRONT
        #      GL_BACK
        #      GL_FRONT_AND_BACK
        # MaterialParameter
        GL_EMISSION = 0x1600
        GL_SHININESS = 0x1601
        GL_AMBIENT_AND_DIFFUSE = 0x1602
        GL_COLOR_INDEXES = 0x1603
        #      GL_AMBIENT
        #      GL_DIFFUSE
        #      GL_SPECULAR
        # MatrixMode
        GL_MODELVIEW = 0x1700
        GL_PROJECTION = 0x1701
        GL_TEXTURE = 0x1702
        # MeshMode1
        #      GL_POINT
        #      GL_LINE
        # MeshMode2
        #      GL_POINT
        #      GL_LINE
        #      GL_FILL
        # NormalPointerType
        #      GL_BYTE
        #      GL_SHORT
        #      GL_INT
        #      GL_FLOAT
        #      GL_DOUBLE
        # PixelCopyType
        GL_COLOR = 0x1800
        GL_DEPTH = 0x1801
        GL_STENCIL = 0x1802
        # PixelFormat
        GL_COLOR_INDEX = 0x1900
        GL_STENCIL_INDEX = 0x1901
        GL_DEPTH_COMPONENT = 0x1902
        GL_RED = 0x1903
        GL_GREEN = 0x1904
        GL_BLUE = 0x1905
        GL_ALPHA = 0x1906
        GL_RGB = 0x1907
        GL_RGBA = 0x1908
        GL_LUMINANCE = 0x1909
        GL_LUMINANCE_ALPHA = 0x190A
        # PixelMap
        #      GL_PIXEL_MAP_I_TO_I
        #      GL_PIXEL_MAP_S_TO_S
        #      GL_PIXEL_MAP_I_TO_R
        #      GL_PIXEL_MAP_I_TO_G
        #      GL_PIXEL_MAP_I_TO_B
        #      GL_PIXEL_MAP_I_TO_A
        #      GL_PIXEL_MAP_R_TO_R
        #      GL_PIXEL_MAP_G_TO_G
        #      GL_PIXEL_MAP_B_TO_B
        #      GL_PIXEL_MAP_A_TO_A
        # PixelStore
        #      GL_UNPACK_SWAP_BYTES
        #      GL_UNPACK_LSB_FIRST
        #      GL_UNPACK_ROW_LENGTH
        #      GL_UNPACK_SKIP_ROWS
        #      GL_UNPACK_SKIP_PIXELS
        #      GL_UNPACK_ALIGNMENT
        #      GL_PACK_SWAP_BYTES
        #      GL_PACK_LSB_FIRST
        #      GL_PACK_ROW_LENGTH
        #      GL_PACK_SKIP_ROWS
        #      GL_PACK_SKIP_PIXELS
        #      GL_PACK_ALIGNMENT
        # PixelTransfer
        #      GL_MAP_COLOR
        #      GL_MAP_STENCIL
        #      GL_INDEX_SHIFT
        #      GL_INDEX_OFFSET
        #      GL_RED_SCALE
        #      GL_RED_BIAS
        #      GL_GREEN_SCALE
        #      GL_GREEN_BIAS
        #      GL_BLUE_SCALE
        #      GL_BLUE_BIAS
        #      GL_ALPHA_SCALE
        #      GL_ALPHA_BIAS
        #      GL_DEPTH_SCALE
        #      GL_DEPTH_BIAS
        # PixelType
        GL_BITMAP = 0x1A00
        #      GL_BYTE
        #      GL_UNSIGNED_BYTE
        #      GL_SHORT
        #      GL_UNSIGNED_SHORT
        #      GL_INT
        #      GL_UNSIGNED_INT
        #      GL_FLOAT
        # PolygonMode
        GL_POINT = 0x1B00
        GL_LINE = 0x1B01
        GL_FILL = 0x1B02
        # ReadBufferMode
        #      GL_FRONT_LEFT
        #      GL_FRONT_RIGHT
        #      GL_BACK_LEFT
        #      GL_BACK_RIGHT
        #      GL_FRONT
        #      GL_BACK
        #      GL_LEFT
        #      GL_RIGHT
        #      GL_AUX0
        #      GL_AUX1
        #      GL_AUX2
        #      GL_AUX3
        # RenderingMode
        GL_RENDER = 0x1C00
        GL_FEEDBACK = 0x1C01
        GL_SELECT = 0x1C02
        # ShadingModel
        GL_FLAT = 0x1D00
        GL_SMOOTH = 0x1D01
        # StencilFunction
        #      GL_NEVER
        #      GL_LESS
        #      GL_EQUAL
        #      GL_LEQUAL
        #      GL_GREATER
        #      GL_NOTEQUAL
        #      GL_GEQUAL
        #      GL_ALWAYS
        # StencilOp
        #      GL_ZERO
        GL_KEEP = 0x1E00
        GL_REPLACE = 0x1E01
        GL_INCR = 0x1E02
        GL_DECR = 0x1E03
        #      GL_INVERT
        # StringName
        GL_VENDOR = 0x1F00
        GL_RENDERER = 0x1F01
        GL_VERSION = 0x1F02
        GL_EXTENSIONS = 0x1F03
        # TextureCoordName
        GL_S = 0x2000
        GL_T = 0x2001
        GL_R = 0x2002
        GL_Q = 0x2003
        # TexCoordPointerType
        #      GL_SHORT
        #      GL_INT
        #      GL_FLOAT
        #      GL_DOUBLE
        # TextureEnvMode
        GL_MODULATE = 0x2100
        GL_DECAL = 0x2101
        #      GL_BLEND
        #      GL_REPLACE
        # TextureEnvParameter
        GL_TEXTURE_ENV_MODE = 0x2200
        GL_TEXTURE_ENV_COLOR = 0x2201
        # TextureEnvTarget
        GL_TEXTURE_ENV = 0x2300
        # TextureGenMode
        GL_EYE_LINEAR = 0x2400
        GL_OBJECT_LINEAR = 0x2401
        GL_SPHERE_MAP = 0x2402
        # TextureGenParameter
        GL_TEXTURE_GEN_MODE = 0x2500
        GL_OBJECT_PLANE = 0x2501
        GL_EYE_PLANE = 0x2502
        # TextureMagFilter
        GL_NEAREST = 0x2600
        GL_LINEAR = 0x2601
        # TextureMinFilter
        #      GL_NEAREST
        #      GL_LINEAR
        GL_NEAREST_MIPMAP_NEAREST = 0x2700
        GL_LINEAR_MIPMAP_NEAREST = 0x2701
        GL_NEAREST_MIPMAP_LINEAR = 0x2702
        GL_LINEAR_MIPMAP_LINEAR = 0x2703
        # TextureParameterName
        GL_TEXTURE_MAG_FILTER = 0x2800
        GL_TEXTURE_MIN_FILTER = 0x2801
        GL_TEXTURE_WRAP_S = 0x2802
        GL_TEXTURE_WRAP_T = 0x2803
        #      GL_TEXTURE_BORDER_COLOR
        #      GL_TEXTURE_PRIORITY
        # TextureTarget
        #      GL_TEXTURE_1D
        #      GL_TEXTURE_2D
        #      GL_PROXY_TEXTURE_1D
        #      GL_PROXY_TEXTURE_2D
        # TextureWrapMode
        GL_CLAMP = 0x2900
        GL_REPEAT = 0x2901
        # VertexPointerType
        #      GL_SHORT
        #      GL_INT
        #      GL_FLOAT
        #      GL_DOUBLE
        # ClientAttribMask
        GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
        GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
        GL_CLIENT_ALL_ATTRIB_BITS = 0xffffffff
        # polygon_offset
        GL_POLYGON_OFFSET_FACTOR = 0x8038
        GL_POLYGON_OFFSET_UNITS = 0x2A00
        GL_POLYGON_OFFSET_POINT = 0x2A01
        GL_POLYGON_OFFSET_LINE = 0x2A02
        GL_POLYGON_OFFSET_FILL = 0x8037
        # texture
        GL_ALPHA4 = 0x803B
        GL_ALPHA8 = 0x803C
        GL_ALPHA12 = 0x803D
        GL_ALPHA16 = 0x803E
        GL_LUMINANCE4 = 0x803F
        GL_LUMINANCE8 = 0x8040
        GL_LUMINANCE12 = 0x8041
        GL_LUMINANCE16 = 0x8042
        GL_LUMINANCE4_ALPHA4 = 0x8043
        GL_LUMINANCE6_ALPHA2 = 0x8044
        GL_LUMINANCE8_ALPHA8 = 0x8045
        GL_LUMINANCE12_ALPHA4 = 0x8046
        GL_LUMINANCE12_ALPHA12 = 0x8047
        GL_LUMINANCE16_ALPHA16 = 0x8048
        GL_INTENSITY = 0x8049
        GL_INTENSITY4 = 0x804A
        GL_INTENSITY8 = 0x804B
        GL_INTENSITY12 = 0x804C
        GL_INTENSITY16 = 0x804D
        GL_R3_G3_B2 = 0x2A10
        GL_RGB4 = 0x804F
        GL_RGB5 = 0x8050
        GL_RGB8 = 0x8051
        GL_RGB10 = 0x8052
        GL_RGB12 = 0x8053
        GL_RGB16 = 0x8054
        GL_RGBA2 = 0x8055
        GL_RGBA4 = 0x8056
        GL_RGB5_A1 = 0x8057
        GL_RGBA8 = 0x8058
        GL_RGB10_A2 = 0x8059
        GL_RGBA12 = 0x805A
        GL_RGBA16 = 0x805B
        GL_TEXTURE_RED_SIZE = 0x805C
        GL_TEXTURE_GREEN_SIZE = 0x805D
        GL_TEXTURE_BLUE_SIZE = 0x805E
        GL_TEXTURE_ALPHA_SIZE = 0x805F
        GL_TEXTURE_LUMINANCE_SIZE = 0x8060
        GL_TEXTURE_INTENSITY_SIZE = 0x8061
        GL_PROXY_TEXTURE_1D = 0x8063
        GL_PROXY_TEXTURE_2D = 0x8064
        # texture_object
        GL_TEXTURE_PRIORITY = 0x8066
        GL_TEXTURE_RESIDENT = 0x8067
        GL_TEXTURE_BINDING_1D = 0x8068
        GL_TEXTURE_BINDING_2D = 0x8069
        # vertex_array
        GL_VERTEX_ARRAY = 0x8074
        GL_NORMAL_ARRAY = 0x8075
        GL_COLOR_ARRAY = 0x8076
        GL_INDEX_ARRAY = 0x8077
        GL_TEXTURE_COORD_ARRAY = 0x8078
        GL_EDGE_FLAG_ARRAY = 0x8079
        GL_VERTEX_ARRAY_SIZE = 0x807A
        GL_VERTEX_ARRAY_TYPE = 0x807B
        GL_VERTEX_ARRAY_STRIDE = 0x807C
        GL_NORMAL_ARRAY_TYPE = 0x807E
        GL_NORMAL_ARRAY_STRIDE = 0x807F
        GL_COLOR_ARRAY_SIZE = 0x8081
        GL_COLOR_ARRAY_TYPE = 0x8082
        GL_COLOR_ARRAY_STRIDE = 0x8083
        GL_INDEX_ARRAY_TYPE = 0x8085
        GL_INDEX_ARRAY_STRIDE = 0x8086
        GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
        GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
        GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
        GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
        GL_VERTEX_ARRAY_POINTER = 0x808E
        GL_NORMAL_ARRAY_POINTER = 0x808F
        GL_COLOR_ARRAY_POINTER = 0x8090
        GL_INDEX_ARRAY_POINTER = 0x8091
        GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
        GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
        GL_V2F = 0x2A20
        GL_V3F = 0x2A21
        GL_C4UB_V2F = 0x2A22
        GL_C4UB_V3F = 0x2A23
        GL_C3F_V3F = 0x2A24
        GL_N3F_V3F = 0x2A25
        GL_C4F_N3F_V3F = 0x2A26
        GL_T2F_V3F = 0x2A27
        GL_T4F_V4F = 0x2A28
        GL_T2F_C4UB_V3F = 0x2A29
        GL_T2F_C3F_V3F = 0x2A2A
        GL_T2F_N3F_V3F = 0x2A2B
        GL_T2F_C4F_N3F_V3F = 0x2A2C
        GL_T4F_C4F_N3F_V4F = 0x2A2D
        # Extensions
        GL_EXT_vertex_array = 1
        GL_EXT_bgra = 1
        GL_EXT_paletted_texture = 1
        GL_WIN_swap_hint = 1
        GL_WIN_draw_range_elements = 1
        # #define GL_WIN_phong_shading              1
        # #define GL_WIN_specular_fog               1
        # EXT_vertex_array
        GL_VERTEX_ARRAY_EXT = 0x8074
        GL_NORMAL_ARRAY_EXT = 0x8075
        GL_COLOR_ARRAY_EXT = 0x8076
        GL_INDEX_ARRAY_EXT = 0x8077
        GL_TEXTURE_COORD_ARRAY_EXT = 0x8078
        GL_EDGE_FLAG_ARRAY_EXT = 0x8079
        GL_VERTEX_ARRAY_SIZE_EXT = 0x807A
        GL_VERTEX_ARRAY_TYPE_EXT = 0x807B
        GL_VERTEX_ARRAY_STRIDE_EXT = 0x807C
        GL_VERTEX_ARRAY_COUNT_EXT = 0x807D
        GL_NORMAL_ARRAY_TYPE_EXT = 0x807E
        GL_NORMAL_ARRAY_STRIDE_EXT = 0x807F
        GL_NORMAL_ARRAY_COUNT_EXT = 0x8080
        GL_COLOR_ARRAY_SIZE_EXT = 0x8081
        GL_COLOR_ARRAY_TYPE_EXT = 0x8082
        GL_COLOR_ARRAY_STRIDE_EXT = 0x8083
        GL_COLOR_ARRAY_COUNT_EXT = 0x8084
        GL_INDEX_ARRAY_TYPE_EXT = 0x8085
        GL_INDEX_ARRAY_STRIDE_EXT = 0x8086
        GL_INDEX_ARRAY_COUNT_EXT = 0x8087
        GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 0x8088
        GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 0x8089
        GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 0x808A
        GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 0x808B
        GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 0x808C
        GL_EDGE_FLAG_ARRAY_COUNT_EXT = 0x808D
        GL_VERTEX_ARRAY_POINTER_EXT = 0x808E
        GL_NORMAL_ARRAY_POINTER_EXT = 0x808F
        GL_COLOR_ARRAY_POINTER_EXT = 0x8090
        GL_INDEX_ARRAY_POINTER_EXT = 0x8091
        GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 0x8092
        GL_EDGE_FLAG_ARRAY_POINTER_EXT = 0x8093
        GL_DOUBLE_EXT = GL_DOUBLE
        # EXT_bgra
        GL_BGR_EXT = 0x80E0
        GL_BGRA_EXT = 0x80E1
        # EXT_paletted_texture
        # These must match the GL_COLOR_TABLE_*_SGI enumerants
        GL_COLOR_TABLE_FORMAT_EXT = 0x80D8
        GL_COLOR_TABLE_WIDTH_EXT = 0x80D9
        GL_COLOR_TABLE_RED_SIZE_EXT = 0x80DA
        GL_COLOR_TABLE_GREEN_SIZE_EXT = 0x80DB
        GL_COLOR_TABLE_BLUE_SIZE_EXT = 0x80DC
        GL_COLOR_TABLE_ALPHA_SIZE_EXT = 0x80DD
        GL_COLOR_TABLE_LUMINANCE_SIZE_EXT = 0x80DE
        GL_COLOR_TABLE_INTENSITY_SIZE_EXT = 0x80DF
        GL_COLOR_INDEX1_EXT = 0x80E2
        GL_COLOR_INDEX2_EXT = 0x80E3
        GL_COLOR_INDEX4_EXT = 0x80E4
        GL_COLOR_INDEX8_EXT = 0x80E5
        GL_COLOR_INDEX12_EXT = 0x80E6
        GL_COLOR_INDEX16_EXT = 0x80E7
        # WIN_draw_range_elements
        GL_MAX_ELEMENTS_VERTICES_WIN = 0x80E8
        GL_MAX_ELEMENTS_INDICES_WIN = 0x80E9
        # WIN_phong_shading
        GL_PHONG_WIN = 0x80EA
        GL_PHONG_HINT_WIN = 0x80EB
        # WIN_specular_fog
        GL_FOG_SPECULAR_TEXTURE_WIN = 0x80EC
        # For compatibility with OpenGL v1.0
        GL_LOGIC_OP = GL_INDEX_LOGIC_OP
        GL_TEXTURE_COMPONENTS = GL_TEXTURE_INTERNAL_FORMAT
        #***********************************************************
        glAccum = declare(opengl32.glAccum, VOID, GLenum, GLfloat)
        glAlphaFunc = declare(opengl32.glAlphaFunc, VOID, GLenum, GLclampf)
        glAreTexturesResident = declare(opengl32.glAreTexturesResident, GLboolean, GLsizei, POINTER(GLuint), POINTER(GLboolean))
        glArrayElement = declare(opengl32.glArrayElement, VOID, GLint)
        glBegin = declare(opengl32.glBegin, VOID, GLenum)
        glBindTexture = declare(opengl32.glBindTexture, VOID, GLenum, GLuint)
        glBitmap = declare(opengl32.glBitmap, VOID, GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, POINTER(GLubyte))
        glBlendFunc = declare(opengl32.glBlendFunc, VOID, GLenum, GLenum)
        glCallList = declare(opengl32.glCallList, VOID, GLuint)
        glCallLists = declare(opengl32.glCallLists, VOID, GLsizei, GLenum, POINTER(GLvoid))
        glClear = declare(opengl32.glClear, VOID, GLbitfield)
        glClearAccum = declare(opengl32.glClearAccum, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glClearColor = declare(opengl32.glClearColor, VOID, GLclampf, GLclampf, GLclampf, GLclampf)
        glClearDepth = declare(opengl32.glClearDepth, VOID, GLclampd)
        glClearIndex = declare(opengl32.glClearIndex, VOID, GLfloat)
        glClearStencil = declare(opengl32.glClearStencil, VOID, GLint)
        glClipPlane = declare(opengl32.glClipPlane, VOID, GLenum, POINTER(GLdouble))
        glColor3b = declare(opengl32.glColor3b, VOID, GLbyte, GLbyte, GLbyte)
        glColor3bv = declare(opengl32.glColor3bv, VOID, POINTER(GLbyte))
        glColor3d = declare(opengl32.glColor3d, VOID, GLdouble, GLdouble, GLdouble)
        glColor3dv = declare(opengl32.glColor3dv, VOID, POINTER(GLdouble))
        glColor3f = declare(opengl32.glColor3f, VOID, GLfloat, GLfloat, GLfloat)
        glColor3fv = declare(opengl32.glColor3fv, VOID, POINTER(GLfloat))
        glColor3i = declare(opengl32.glColor3i, VOID, GLint, GLint, GLint)
        glColor3iv = declare(opengl32.glColor3iv, VOID, POINTER(GLint))
        glColor3s = declare(opengl32.glColor3s, VOID, GLshort, GLshort, GLshort)
        glColor3sv = declare(opengl32.glColor3sv, VOID, POINTER(GLshort))
        glColor3ub = declare(opengl32.glColor3ub, VOID, GLubyte, GLubyte, GLubyte)
        glColor3ubv = declare(opengl32.glColor3ubv, VOID, POINTER(GLubyte))
        glColor3ui = declare(opengl32.glColor3ui, VOID, GLuint, GLuint, GLuint)
        glColor3uiv = declare(opengl32.glColor3uiv, VOID, POINTER(GLuint))
        glColor3us = declare(opengl32.glColor3us, VOID, GLushort, GLushort, GLushort)
        glColor3usv = declare(opengl32.glColor3usv, VOID, POINTER(GLushort))
        glColor4b = declare(opengl32.glColor4b, VOID, GLbyte, GLbyte, GLbyte, GLbyte)
        glColor4bv = declare(opengl32.glColor4bv, VOID, POINTER(GLbyte))
        glColor4d = declare(opengl32.glColor4d, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glColor4dv = declare(opengl32.glColor4dv, VOID, POINTER(GLdouble))
        glColor4f = declare(opengl32.glColor4f, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glColor4fv = declare(opengl32.glColor4fv, VOID, POINTER(GLfloat))
        glColor4i = declare(opengl32.glColor4i, VOID, GLint, GLint, GLint, GLint)
        glColor4iv = declare(opengl32.glColor4iv, VOID, POINTER(GLint))
        glColor4s = declare(opengl32.glColor4s, VOID, GLshort, GLshort, GLshort, GLshort)
        glColor4sv = declare(opengl32.glColor4sv, VOID, POINTER(GLshort))
        glColor4ub = declare(opengl32.glColor4ub, VOID, GLubyte, GLubyte, GLubyte, GLubyte)
        glColor4ubv = declare(opengl32.glColor4ubv, VOID, POINTER(GLubyte))
        glColor4ui = declare(opengl32.glColor4ui, VOID, GLuint, GLuint, GLuint, GLuint)
        glColor4uiv = declare(opengl32.glColor4uiv, VOID, POINTER(GLuint))
        glColor4us = declare(opengl32.glColor4us, VOID, GLushort, GLushort, GLushort, GLushort)
        glColor4usv = declare(opengl32.glColor4usv, VOID, POINTER(GLushort))
        glColorMask = declare(opengl32.glColorMask, VOID, GLboolean, GLboolean, GLboolean, GLboolean)
        glColorMaterial = declare(opengl32.glColorMaterial, VOID, GLenum, GLenum)
        glColorPointer = declare(opengl32.glColorPointer, VOID, GLint, GLenum, GLsizei, POINTER(GLvoid))
        glCopyPixels = declare(opengl32.glCopyPixels, VOID, GLint, GLint, GLsizei, GLsizei, GLenum)
        glCopyTexImage1D = declare(opengl32.glCopyTexImage1D, VOID, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint)
        glCopyTexImage2D = declare(opengl32.glCopyTexImage2D, VOID, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint)
        glCopyTexSubImage1D = declare(opengl32.glCopyTexSubImage1D, VOID, GLenum, GLint, GLint, GLint, GLint, GLsizei)
        glCopyTexSubImage2D = declare(opengl32.glCopyTexSubImage2D, VOID, GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)
        glCullFace = declare(opengl32.glCullFace, VOID, GLenum)
        glDeleteLists = declare(opengl32.glDeleteLists, VOID, GLuint, GLsizei)
        glDeleteTextures = declare(opengl32.glDeleteTextures, VOID, GLsizei, POINTER(GLuint))
        glDepthFunc = declare(opengl32.glDepthFunc, VOID, GLenum)
        glDepthMask = declare(opengl32.glDepthMask, VOID, GLboolean)
        glDepthRange = declare(opengl32.glDepthRange, VOID, GLclampd, GLclampd)
        glDisable = declare(opengl32.glDisable, VOID, GLenum)
        glDisableClientState = declare(opengl32.glDisableClientState, VOID, GLenum)
        glDrawArrays = declare(opengl32.glDrawArrays, VOID, GLenum, GLint, GLsizei)
        glDrawBuffer = declare(opengl32.glDrawBuffer, VOID, GLenum)
        glDrawElements = declare(opengl32.glDrawElements, VOID, GLenum, GLsizei, GLenum, POINTER(GLvoid))
        glDrawPixels = declare(opengl32.glDrawPixels, VOID, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        glEdgeFlag = declare(opengl32.glEdgeFlag, VOID, GLboolean)
        glEdgeFlagPointer = declare(opengl32.glEdgeFlagPointer, VOID, GLsizei, POINTER(GLvoid))
        glEdgeFlagv = declare(opengl32.glEdgeFlagv, VOID, POINTER(GLboolean))
        glEnable = declare(opengl32.glEnable, VOID, GLenum)
        glEnableClientState = declare(opengl32.glEnableClientState, VOID, GLenum)
        glEnd = declare(opengl32.glEnd, VOID, VOID)
        glEndList = declare(opengl32.glEndList, VOID, VOID)
        glEvalCoord1d = declare(opengl32.glEvalCoord1d, VOID, GLdouble)
        glEvalCoord1dv = declare(opengl32.glEvalCoord1dv, VOID, POINTER(GLdouble))
        glEvalCoord1f = declare(opengl32.glEvalCoord1f, VOID, GLfloat)
        glEvalCoord1fv = declare(opengl32.glEvalCoord1fv, VOID, POINTER(GLfloat))
        glEvalCoord2d = declare(opengl32.glEvalCoord2d, VOID, GLdouble, GLdouble)
        glEvalCoord2dv = declare(opengl32.glEvalCoord2dv, VOID, POINTER(GLdouble))
        glEvalCoord2f = declare(opengl32.glEvalCoord2f, VOID, GLfloat, GLfloat)
        glEvalCoord2fv = declare(opengl32.glEvalCoord2fv, VOID, POINTER(GLfloat))
        glEvalMesh1 = declare(opengl32.glEvalMesh1, VOID, GLenum, GLint, GLint)
        glEvalMesh2 = declare(opengl32.glEvalMesh2, VOID, GLenum, GLint, GLint, GLint, GLint)
        glEvalPoint1 = declare(opengl32.glEvalPoint1, VOID, GLint)
        glEvalPoint2 = declare(opengl32.glEvalPoint2, VOID, GLint, GLint)
        glFeedbackBuffer = declare(opengl32.glFeedbackBuffer, VOID, GLsizei, GLenum, POINTER(GLfloat))
        glFinish = declare(opengl32.glFinish, VOID, VOID)
        glFlush = declare(opengl32.glFlush, VOID, VOID)
        glFogf = declare(opengl32.glFogf, VOID, GLenum, GLfloat)
        glFogfv = declare(opengl32.glFogfv, VOID, GLenum, POINTER(GLfloat))
        glFogi = declare(opengl32.glFogi, VOID, GLenum, GLint)
        glFogiv = declare(opengl32.glFogiv, VOID, GLenum, POINTER(GLint))
        glFrontFace = declare(opengl32.glFrontFace, VOID, GLenum)
        glFrustum = declare(opengl32.glFrustum, VOID, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble)
        glGenLists = declare(opengl32.glGenLists, GLuint, GLsizei)
        glGenTextures = declare(opengl32.glGenTextures, VOID, GLsizei, POINTER(GLuint))
        glGetBooleanv = declare(opengl32.glGetBooleanv, VOID, GLenum, POINTER(GLboolean))
        glGetClipPlane = declare(opengl32.glGetClipPlane, VOID, GLenum, POINTER(GLdouble))
        glGetDoublev = declare(opengl32.glGetDoublev, VOID, GLenum, POINTER(GLdouble))
        glGetError = declare(opengl32.glGetError, GLenum, VOID)
        glGetFloatv = declare(opengl32.glGetFloatv, VOID, GLenum, POINTER(GLfloat))
        glGetIntegerv = declare(opengl32.glGetIntegerv, VOID, GLenum, POINTER(GLint))
        glGetLightfv = declare(opengl32.glGetLightfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetLightiv = declare(opengl32.glGetLightiv, VOID, GLenum, GLenum, POINTER(GLint))
        glGetMapdv = declare(opengl32.glGetMapdv, VOID, GLenum, GLenum, POINTER(GLdouble))
        glGetMapfv = declare(opengl32.glGetMapfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetMapiv = declare(opengl32.glGetMapiv, VOID, GLenum, GLenum, POINTER(GLint))
        glGetMaterialfv = declare(opengl32.glGetMaterialfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetMaterialiv = declare(opengl32.glGetMaterialiv, VOID, GLenum, GLenum, POINTER(GLint))
        glGetPixelMapfv = declare(opengl32.glGetPixelMapfv, VOID, GLenum, POINTER(GLfloat))
        glGetPixelMapuiv = declare(opengl32.glGetPixelMapuiv, VOID, GLenum, POINTER(GLuint))
        glGetPixelMapusv = declare(opengl32.glGetPixelMapusv, VOID, GLenum, POINTER(GLushort))
        glGetPointerv = declare(opengl32.glGetPointerv, VOID, GLenum, POINTER(GLvoid))
        glGetPolygonStipple = declare(opengl32.glGetPolygonStipple, VOID, POINTER(GLubyte))
        glGetString = declare(opengl32.glGetString, LPSTR, GLenum)
        glGetTexEnvfv = declare(opengl32.glGetTexEnvfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetTexEnviv = declare(opengl32.glGetTexEnviv, VOID, GLenum, GLenum, POINTER(GLint))
        glGetTexGendv = declare(opengl32.glGetTexGendv, VOID, GLenum, GLenum, POINTER(GLdouble))
        glGetTexGenfv = declare(opengl32.glGetTexGenfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetTexGeniv = declare(opengl32.glGetTexGeniv, VOID, GLenum, GLenum, POINTER(GLint))
        glGetTexImage = declare(opengl32.glGetTexImage, VOID, GLenum, GLint, GLenum, GLenum, POINTER(GLvoid))
        glGetTexLevelParameterfv = declare(opengl32.glGetTexLevelParameterfv, VOID, GLenum, GLint, GLenum, POINTER(GLfloat))
        glGetTexLevelParameteriv = declare(opengl32.glGetTexLevelParameteriv, VOID, GLenum, GLint, GLenum, POINTER(GLint))
        glGetTexParameterfv = declare(opengl32.glGetTexParameterfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glGetTexParameteriv = declare(opengl32.glGetTexParameteriv, VOID, GLenum, GLenum, POINTER(GLint))
        glHint = declare(opengl32.glHint, VOID, GLenum, GLenum)
        glIndexMask = declare(opengl32.glIndexMask, VOID, GLuint)
        glIndexPointer = declare(opengl32.glIndexPointer, VOID, GLenum, GLsizei, POINTER(GLvoid))
        glIndexd = declare(opengl32.glIndexd, VOID, GLdouble)
        glIndexdv = declare(opengl32.glIndexdv, VOID, POINTER(GLdouble))
        glIndexf = declare(opengl32.glIndexf, VOID, GLfloat)
        glIndexfv = declare(opengl32.glIndexfv, VOID, POINTER(GLfloat))
        glIndexi = declare(opengl32.glIndexi, VOID, GLint)
        glIndexiv = declare(opengl32.glIndexiv, VOID, POINTER(GLint))
        glIndexs = declare(opengl32.glIndexs, VOID, GLshort)
        glIndexsv = declare(opengl32.glIndexsv, VOID, POINTER(GLshort))
        glIndexub = declare(opengl32.glIndexub, VOID, GLubyte)
        glIndexubv = declare(opengl32.glIndexubv, VOID, POINTER(GLubyte))
        glInitNames = declare(opengl32.glInitNames, VOID, VOID)
        glInterleavedArrays = declare(opengl32.glInterleavedArrays, VOID, GLenum, GLsizei, POINTER(GLvoid))
        glIsEnabled = declare(opengl32.glIsEnabled, GLboolean, GLenum)
        glIsList = declare(opengl32.glIsList, GLboolean, GLuint)
        glIsTexture = declare(opengl32.glIsTexture, GLboolean, GLuint)
        glLightModelf = declare(opengl32.glLightModelf, VOID, GLenum, GLfloat)
        glLightModelfv = declare(opengl32.glLightModelfv, VOID, GLenum, POINTER(GLfloat))
        glLightModeli = declare(opengl32.glLightModeli, VOID, GLenum, GLint)
        glLightModeliv = declare(opengl32.glLightModeliv, VOID, GLenum, POINTER(GLint))
        glLightf = declare(opengl32.glLightf, VOID, GLenum, GLenum, GLfloat)
        glLightfv = declare(opengl32.glLightfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glLighti = declare(opengl32.glLighti, VOID, GLenum, GLenum, GLint)
        glLightiv = declare(opengl32.glLightiv, VOID, GLenum, GLenum, POINTER(GLint))
        glLineStipple = declare(opengl32.glLineStipple, VOID, GLint, GLushort)
        glLineWidth = declare(opengl32.glLineWidth, VOID, GLfloat)
        glListBase = declare(opengl32.glListBase, VOID, GLuint)
        glLoadIdentity = declare(opengl32.glLoadIdentity, VOID, VOID)
        glLoadMatrixd = declare(opengl32.glLoadMatrixd, VOID, POINTER(GLdouble))
        glLoadMatrixf = declare(opengl32.glLoadMatrixf, VOID, POINTER(GLfloat))
        glLoadName = declare(opengl32.glLoadName, VOID, GLuint)
        glLogicOp = declare(opengl32.glLogicOp, VOID, GLenum)
        glMap1d = declare(opengl32.glMap1d, VOID, GLenum, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble))
        glMap1f = declare(opengl32.glMap1f, VOID, GLenum, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat))
        glMap2d = declare(opengl32.glMap2d, VOID, GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, POINTER(GLdouble))
        glMap2f = declare(opengl32.glMap2f, VOID, GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, POINTER(GLfloat))
        glMapGrid1d = declare(opengl32.glMapGrid1d, VOID, GLint, GLdouble, GLdouble)
        glMapGrid1f = declare(opengl32.glMapGrid1f, VOID, GLint, GLfloat, GLfloat)
        glMapGrid2d = declare(opengl32.glMapGrid2d, VOID, GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble)
        glMapGrid2f = declare(opengl32.glMapGrid2f, VOID, GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat)
        glMaterialf = declare(opengl32.glMaterialf, VOID, GLenum, GLenum, GLfloat)
        glMaterialfv = declare(opengl32.glMaterialfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glMateriali = declare(opengl32.glMateriali, VOID, GLenum, GLenum, GLint)
        glMaterialiv = declare(opengl32.glMaterialiv, VOID, GLenum, GLenum, POINTER(GLint))
        glMatrixMode = declare(opengl32.glMatrixMode, VOID, GLenum)
        glMultMatrixd = declare(opengl32.glMultMatrixd, VOID, POINTER(GLdouble))
        glMultMatrixf = declare(opengl32.glMultMatrixf, VOID, POINTER(GLfloat))
        glNewList = declare(opengl32.glNewList, VOID, GLuint, GLenum)
        glNormal3b = declare(opengl32.glNormal3b, VOID, GLbyte, GLbyte, GLbyte)
        glNormal3bv = declare(opengl32.glNormal3bv, VOID, POINTER(GLbyte))
        glNormal3d = declare(opengl32.glNormal3d, VOID, GLdouble, GLdouble, GLdouble)
        glNormal3dv = declare(opengl32.glNormal3dv, VOID, POINTER(GLdouble))
        glNormal3f = declare(opengl32.glNormal3f, VOID, GLfloat, GLfloat, GLfloat)
        glNormal3fv = declare(opengl32.glNormal3fv, VOID, POINTER(GLfloat))
        glNormal3i = declare(opengl32.glNormal3i, VOID, GLint, GLint, GLint)
        glNormal3iv = declare(opengl32.glNormal3iv, VOID, POINTER(GLint))
        glNormal3s = declare(opengl32.glNormal3s, VOID, GLshort, GLshort, GLshort)
        glNormal3sv = declare(opengl32.glNormal3sv, VOID, POINTER(GLshort))
        glNormalPointer = declare(opengl32.glNormalPointer, VOID, GLenum, GLsizei, POINTER(GLvoid))
        glOrtho = declare(opengl32.glOrtho, VOID, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble)
        glPassThrough = declare(opengl32.glPassThrough, VOID, GLfloat)
        glPixelMapfv = declare(opengl32.glPixelMapfv, VOID, GLenum, GLsizei, POINTER(GLfloat))
        glPixelMapuiv = declare(opengl32.glPixelMapuiv, VOID, GLenum, GLsizei, POINTER(GLuint))
        glPixelMapusv = declare(opengl32.glPixelMapusv, VOID, GLenum, GLsizei, POINTER(GLushort))
        glPixelStoref = declare(opengl32.glPixelStoref, VOID, GLenum, GLfloat)
        glPixelStorei = declare(opengl32.glPixelStorei, VOID, GLenum, GLint)
        glPixelTransferf = declare(opengl32.glPixelTransferf, VOID, GLenum, GLfloat)
        glPixelTransferi = declare(opengl32.glPixelTransferi, VOID, GLenum, GLint)
        glPixelZoom = declare(opengl32.glPixelZoom, VOID, GLfloat, GLfloat)
        glPointSize = declare(opengl32.glPointSize, VOID, GLfloat)
        glPolygonMode = declare(opengl32.glPolygonMode, VOID, GLenum, GLenum)
        glPolygonOffset = declare(opengl32.glPolygonOffset, VOID, GLfloat, GLfloat)
        glPolygonStipple = declare(opengl32.glPolygonStipple, VOID, POINTER(GLubyte))
        glPopAttrib = declare(opengl32.glPopAttrib, VOID, VOID)
        glPopClientAttrib = declare(opengl32.glPopClientAttrib, VOID, VOID)
        glPopMatrix = declare(opengl32.glPopMatrix, VOID, VOID)
        glPopName = declare(opengl32.glPopName, VOID, VOID)
        glPrioritizeTextures = declare(opengl32.glPrioritizeTextures, VOID, GLsizei, POINTER(GLuint), POINTER(GLclampf))
        glPushAttrib = declare(opengl32.glPushAttrib, VOID, GLbitfield)
        glPushClientAttrib = declare(opengl32.glPushClientAttrib, VOID, GLbitfield)
        glPushMatrix = declare(opengl32.glPushMatrix, VOID, VOID)
        glPushName = declare(opengl32.glPushName, VOID, GLuint)
        glRasterPos2d = declare(opengl32.glRasterPos2d, VOID, GLdouble, GLdouble)
        glRasterPos2dv = declare(opengl32.glRasterPos2dv, VOID, POINTER(GLdouble))
        glRasterPos2f = declare(opengl32.glRasterPos2f, VOID, GLfloat, GLfloat)
        glRasterPos2fv = declare(opengl32.glRasterPos2fv, VOID, POINTER(GLfloat))
        glRasterPos2i = declare(opengl32.glRasterPos2i, VOID, GLint, GLint)
        glRasterPos2iv = declare(opengl32.glRasterPos2iv, VOID, POINTER(GLint))
        glRasterPos2s = declare(opengl32.glRasterPos2s, VOID, GLshort, GLshort)
        glRasterPos2sv = declare(opengl32.glRasterPos2sv, VOID, POINTER(GLshort))
        glRasterPos3d = declare(opengl32.glRasterPos3d, VOID, GLdouble, GLdouble, GLdouble)
        glRasterPos3dv = declare(opengl32.glRasterPos3dv, VOID, POINTER(GLdouble))
        glRasterPos3f = declare(opengl32.glRasterPos3f, VOID, GLfloat, GLfloat, GLfloat)
        glRasterPos3fv = declare(opengl32.glRasterPos3fv, VOID, POINTER(GLfloat))
        glRasterPos3i = declare(opengl32.glRasterPos3i, VOID, GLint, GLint, GLint)
        glRasterPos3iv = declare(opengl32.glRasterPos3iv, VOID, POINTER(GLint))
        glRasterPos3s = declare(opengl32.glRasterPos3s, VOID, GLshort, GLshort, GLshort)
        glRasterPos3sv = declare(opengl32.glRasterPos3sv, VOID, POINTER(GLshort))
        glRasterPos4d = declare(opengl32.glRasterPos4d, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glRasterPos4dv = declare(opengl32.glRasterPos4dv, VOID, POINTER(GLdouble))
        glRasterPos4f = declare(opengl32.glRasterPos4f, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glRasterPos4fv = declare(opengl32.glRasterPos4fv, VOID, POINTER(GLfloat))
        glRasterPos4i = declare(opengl32.glRasterPos4i, VOID, GLint, GLint, GLint, GLint)
        glRasterPos4iv = declare(opengl32.glRasterPos4iv, VOID, POINTER(GLint))
        glRasterPos4s = declare(opengl32.glRasterPos4s, VOID, GLshort, GLshort, GLshort, GLshort)
        glRasterPos4sv = declare(opengl32.glRasterPos4sv, VOID, POINTER(GLshort))
        glReadBuffer = declare(opengl32.glReadBuffer, VOID, GLenum)
        glReadPixels = declare(opengl32.glReadPixels, VOID, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        glRectd = declare(opengl32.glRectd, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glRectdv = declare(opengl32.glRectdv, VOID, POINTER(GLdouble), POINTER(GLdouble))
        glRectf = declare(opengl32.glRectf, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glRectfv = declare(opengl32.glRectfv, VOID, POINTER(GLfloat), POINTER(GLfloat))
        glRecti = declare(opengl32.glRecti, VOID, GLint, GLint, GLint, GLint)
        glRectiv = declare(opengl32.glRectiv, VOID, POINTER(GLint), POINTER(GLint))
        glRects = declare(opengl32.glRects, VOID, GLshort, GLshort, GLshort, GLshort)
        glRectsv = declare(opengl32.glRectsv, VOID, POINTER(GLshort), POINTER(GLshort))
        glRenderMode = declare(opengl32.glRenderMode, GLint, GLenum)
        glRotated = declare(opengl32.glRotated, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glRotatef = declare(opengl32.glRotatef, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glScaled = declare(opengl32.glScaled, VOID, GLdouble, GLdouble, GLdouble)
        glScalef = declare(opengl32.glScalef, VOID, GLfloat, GLfloat, GLfloat)
        glScissor = declare(opengl32.glScissor, VOID, GLint, GLint, GLsizei, GLsizei)
        glSelectBuffer = declare(opengl32.glSelectBuffer, VOID, GLsizei, POINTER(GLuint))
        glShadeModel = declare(opengl32.glShadeModel, VOID, GLenum)
        glStencilFunc = declare(opengl32.glStencilFunc, VOID, GLenum, GLint, GLuint)
        glStencilMask = declare(opengl32.glStencilMask, VOID, GLuint)
        glStencilOp = declare(opengl32.glStencilOp, VOID, GLenum, GLenum, GLenum)
        glTexCoord1d = declare(opengl32.glTexCoord1d, VOID, GLdouble)
        glTexCoord1dv = declare(opengl32.glTexCoord1dv, VOID, POINTER(GLdouble))
        glTexCoord1f = declare(opengl32.glTexCoord1f, VOID, GLfloat)
        glTexCoord1fv = declare(opengl32.glTexCoord1fv, VOID, POINTER(GLfloat))
        glTexCoord1i = declare(opengl32.glTexCoord1i, VOID, GLint)
        glTexCoord1iv = declare(opengl32.glTexCoord1iv, VOID, POINTER(GLint))
        glTexCoord1s = declare(opengl32.glTexCoord1s, VOID, GLshort)
        glTexCoord1sv = declare(opengl32.glTexCoord1sv, VOID, POINTER(GLshort))
        glTexCoord2d = declare(opengl32.glTexCoord2d, VOID, GLdouble, GLdouble)
        glTexCoord2dv = declare(opengl32.glTexCoord2dv, VOID, POINTER(GLdouble))
        glTexCoord2f = declare(opengl32.glTexCoord2f, VOID, GLfloat, GLfloat)
        glTexCoord2fv = declare(opengl32.glTexCoord2fv, VOID, POINTER(GLfloat))
        glTexCoord2i = declare(opengl32.glTexCoord2i, VOID, GLint, GLint)
        glTexCoord2iv = declare(opengl32.glTexCoord2iv, VOID, POINTER(GLint))
        glTexCoord2s = declare(opengl32.glTexCoord2s, VOID, GLshort, GLshort)
        glTexCoord2sv = declare(opengl32.glTexCoord2sv, VOID, POINTER(GLshort))
        glTexCoord3d = declare(opengl32.glTexCoord3d, VOID, GLdouble, GLdouble, GLdouble)
        glTexCoord3dv = declare(opengl32.glTexCoord3dv, VOID, POINTER(GLdouble))
        glTexCoord3f = declare(opengl32.glTexCoord3f, VOID, GLfloat, GLfloat, GLfloat)
        glTexCoord3fv = declare(opengl32.glTexCoord3fv, VOID, POINTER(GLfloat))
        glTexCoord3i = declare(opengl32.glTexCoord3i, VOID, GLint, GLint, GLint)
        glTexCoord3iv = declare(opengl32.glTexCoord3iv, VOID, POINTER(GLint))
        glTexCoord3s = declare(opengl32.glTexCoord3s, VOID, GLshort, GLshort, GLshort)
        glTexCoord3sv = declare(opengl32.glTexCoord3sv, VOID, POINTER(GLshort))
        glTexCoord4d = declare(opengl32.glTexCoord4d, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glTexCoord4dv = declare(opengl32.glTexCoord4dv, VOID, POINTER(GLdouble))
        glTexCoord4f = declare(opengl32.glTexCoord4f, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glTexCoord4fv = declare(opengl32.glTexCoord4fv, VOID, POINTER(GLfloat))
        glTexCoord4i = declare(opengl32.glTexCoord4i, VOID, GLint, GLint, GLint, GLint)
        glTexCoord4iv = declare(opengl32.glTexCoord4iv, VOID, POINTER(GLint))
        glTexCoord4s = declare(opengl32.glTexCoord4s, VOID, GLshort, GLshort, GLshort, GLshort)
        glTexCoord4sv = declare(opengl32.glTexCoord4sv, VOID, POINTER(GLshort))
        glTexCoordPointer = declare(opengl32.glTexCoordPointer, VOID, GLint, GLenum, GLsizei, POINTER(GLvoid))
        glTexEnvf = declare(opengl32.glTexEnvf, VOID, GLenum, GLenum, GLfloat)
        glTexEnvfv = declare(opengl32.glTexEnvfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glTexEnvi = declare(opengl32.glTexEnvi, VOID, GLenum, GLenum, GLint)
        glTexEnviv = declare(opengl32.glTexEnviv, VOID, GLenum, GLenum, POINTER(GLint))
        glTexGend = declare(opengl32.glTexGend, VOID, GLenum, GLenum, GLdouble)
        glTexGendv = declare(opengl32.glTexGendv, VOID, GLenum, GLenum, POINTER(GLdouble))
        glTexGenf = declare(opengl32.glTexGenf, VOID, GLenum, GLenum, GLfloat)
        glTexGenfv = declare(opengl32.glTexGenfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glTexGeni = declare(opengl32.glTexGeni, VOID, GLenum, GLenum, GLint)
        glTexGeniv = declare(opengl32.glTexGeniv, VOID, GLenum, GLenum, POINTER(GLint))
        glTexImage1D = declare(opengl32.glTexImage1D, VOID, GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid))
        glTexImage2D = declare(opengl32.glTexImage2D, VOID, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, POINTER(GLvoid))
        glTexParameterf = declare(opengl32.glTexParameterf, VOID, GLenum, GLenum, GLfloat)
        glTexParameterfv = declare(opengl32.glTexParameterfv, VOID, GLenum, GLenum, POINTER(GLfloat))
        glTexParameteri = declare(opengl32.glTexParameteri, VOID, GLenum, GLenum, GLint)
        glTexParameteriv = declare(opengl32.glTexParameteriv, VOID, GLenum, GLenum, POINTER(GLint))
        glTexSubImage1D = declare(opengl32.glTexSubImage1D, VOID, GLenum, GLint, GLint, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        glTexSubImage2D = declare(opengl32.glTexSubImage2D, VOID, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        glTranslated = declare(opengl32.glTranslated, VOID, GLdouble, GLdouble, GLdouble)
        glTranslatef = declare(opengl32.glTranslatef, VOID, GLfloat, GLfloat, GLfloat)
        glVertex2d = declare(opengl32.glVertex2d, VOID, GLdouble, GLdouble)
        glVertex2dv = declare(opengl32.glVertex2dv, VOID, POINTER(GLdouble))
        glVertex2f = declare(opengl32.glVertex2f, VOID, GLfloat, GLfloat)
        glVertex2fv = declare(opengl32.glVertex2fv, VOID, POINTER(GLfloat))
        glVertex2i = declare(opengl32.glVertex2i, VOID, GLint, GLint)
        glVertex2iv = declare(opengl32.glVertex2iv, VOID, POINTER(GLint))
        glVertex2s = declare(opengl32.glVertex2s, VOID, GLshort, GLshort)
        glVertex2sv = declare(opengl32.glVertex2sv, VOID, POINTER(GLshort))
        glVertex3d = declare(opengl32.glVertex3d, VOID, GLdouble, GLdouble, GLdouble)
        glVertex3dv = declare(opengl32.glVertex3dv, VOID, POINTER(GLdouble))
        glVertex3f = declare(opengl32.glVertex3f, VOID, GLfloat, GLfloat, GLfloat)
        glVertex3fv = declare(opengl32.glVertex3fv, VOID, POINTER(GLfloat))
        glVertex3i = declare(opengl32.glVertex3i, VOID, GLint, GLint, GLint)
        glVertex3iv = declare(opengl32.glVertex3iv, VOID, POINTER(GLint))
        glVertex3s = declare(opengl32.glVertex3s, VOID, GLshort, GLshort, GLshort)
        glVertex3sv = declare(opengl32.glVertex3sv, VOID, POINTER(GLshort))
        glVertex4d = declare(opengl32.glVertex4d, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        glVertex4dv = declare(opengl32.glVertex4dv, VOID, POINTER(GLdouble))
        glVertex4f = declare(opengl32.glVertex4f, VOID, GLfloat, GLfloat, GLfloat, GLfloat)
        glVertex4fv = declare(opengl32.glVertex4fv, VOID, POINTER(GLfloat))
        glVertex4i = declare(opengl32.glVertex4i, VOID, GLint, GLint, GLint, GLint)
        glVertex4iv = declare(opengl32.glVertex4iv, VOID, POINTER(GLint))
        glVertex4s = declare(opengl32.glVertex4s, VOID, GLshort, GLshort, GLshort, GLshort)
        glVertex4sv = declare(opengl32.glVertex4sv, VOID, POINTER(GLshort))
        glVertexPointer = declare(opengl32.glVertexPointer, VOID, GLint, GLenum, GLsizei, POINTER(GLvoid))
        glViewport = declare(opengl32.glViewport, VOID, GLint, GLint, GLsizei, GLsizei)

        # EXT_vertex_array
        PFNGLARRAYELEMENTEXTPROC = APIENTRY(VOID, GLint)
        PFNGLDRAWARRAYSEXTPROC = APIENTRY(VOID, GLenum, GLint, GLsizei)
        PFNGLVERTEXPOINTEREXTPROC = APIENTRY(VOID, GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid))
        PFNGLNORMALPOINTEREXTPROC = APIENTRY(VOID, GLenum, GLsizei, GLsizei, POINTER(GLvoid))
        PFNGLCOLORPOINTEREXTPROC = APIENTRY(VOID, GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid))
        PFNGLINDEXPOINTEREXTPROC = APIENTRY(VOID,  GLenum, GLsizei, GLsizei, POINTER(GLvoid))
        PFNGLTEXCOORDPOINTEREXTPROC = APIENTRY(VOID, GLint, GLenum, GLsizei, GLsizei, POINTER(GLvoid))
        PFNGLEDGEFLAGPOINTEREXTPROC = APIENTRY(VOID, GLsizei, GLsizei, POINTER(GLboolean))
        PFNGLGETPOINTERVEXTPROC = APIENTRY(VOID, GLenum, POINTER(POINTER(GLvoid)))
        PFNGLARRAYELEMENTARRAYEXTPROC = APIENTRY(VOID, GLenum, GLsizei, POINTER(GLvoid))

        # WIN_draw_range_elements
        PFNGLDRAWRANGEELEMENTSWINPROC = APIENTRY(VOID, GLenum, GLuint, GLuint, GLsizei, GLenum, POINTER(GLvoid))

        # WIN_swap_hint
        PFNGLADDSWAPHINTRECTWINPROC = APIENTRY(VOID, GLint, GLint, GLsizei, GLsizei)

        # EXT_paletted_texture
        PFNGLCOLORTABLEEXTPROC = APIENTRY(VOID, GLenum, GLenum, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        PFNGLCOLORSUBTABLEEXTPROC = APIENTRY(VOID, GLenum, GLsizei, GLsizei, GLenum, GLenum, POINTER(GLvoid))
        PFNGLGETCOLORTABLEEXTPROC = APIENTRY(VOID, GLenum, GLenum, GLenum, POINTER(GLvoid))
        PFNGLGETCOLORTABLEPARAMETERIVEXTPROC = APIENTRY(VOID, GLenum, GLenum, POINTER(GLint))
        PFNGLGETCOLORTABLEPARAMETERFVEXTPROC = APIENTRY(VOID, GLenum, GLenum, POINTER(GLfloat))

        # REGION ***

    # __GL_H__
# __gl_h_