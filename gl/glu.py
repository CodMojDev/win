"""++ BUILD Version: 0004    // Increment this if a change has global effects

Copyright (c) 1985-95, Microsoft Corporation

Module Name:

    glu.h

Abstract:

    Procedure declarations, constant definitions and macros for the OpenGL
    Utility Library.

--"""

from .gl import *

from ..defbase import unicode

if cpreproc.ifndef("__glu_h__"):
    if cpreproc.pragma_once("__GLU_H__"):
        cpreproc.define("__GLU_H__")

        glu32 = W_WinDLL("glu32.dll")

        """
        ** Copyright 1991-1993, Silicon Graphics, Inc.
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

        gluErrorString = declare(glu32.gluErrorString, POINTER(GLubyte), GLenum)
        
        """
        ** Return the error string associated with a particular error code.
        ** This will return 0 for an invalid error code.
        **
        ** The generic function prototype that can be compiled for ANSI or Unicode
        ** is defined as follows:
        **
        ** LPCTSTR APIENTRY gluErrorStringWIN (GLenum errCode);
        """
        gluErrorStringWIN = unicode(
            lambda errCode: cast(gluErrorString(errCode), LPCSTR).value,
            lambda errCode: cast(gluErrorString(errCode), LPCWSTR.value)
        )
        gluErrorUnicodeStringEXT = declare(glu32.gluErrorUnicodeStringEXT, LPCWSTR, GLenum)
        gluGetString = declare(glu32.gluGetString, POINTER(GLubyte), GLenum)
        gluOrtho2D = declare(glu32.gluOrtho2D, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        gluPerspective = declare(glu32.gluPerspective, VOID, GLdouble, GLdouble, GLdouble, GLdouble)
        gluPickMatrix = declare(glu32.gluPickMatrix, VOID, GLdouble, GLdouble, GLdouble, GLdouble, (GLint * 4))
        gluLookAt = declare(glu32.gluLookAt, VOID, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble)
        gluProject = declare(glu32.gluProject, INT, GLdouble, GLdouble, GLdouble, (GLdouble * 16), (GLdouble * 16), (GLint * 4), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble))
        gluUnProject = declare(glu32.gluUnProject, INT, GLdouble, GLdouble, GLdouble, (GLdouble * 16), (GLdouble * 16), (GLint * 4), POINTER(GLdouble), POINTER(GLdouble), POINTER(GLdouble))
        gluScaleImage = declare(glu32.gluScaleImage, INT, GLenum, GLint, GLint, GLenum, PVOID, GLint, GLint, GLenum, PVOID)
        gluBuild1DMipmaps = declare(glu32.gluBuild1DMipmaps, INT, GLenum, GLint, GLint, GLenum, GLenum, PVOID)
        gluBuild2DMipmaps = declare(glu32.gluBuild2DMipmaps, INT, GLenum, GLint, GLint, GLint, GLenum, GLenum, PVOID)
        gluNewQuadric = declare(glu32.gluNewQuadric, PVOID, VOID)
        gluDeleteQuadric = declare(glu32.gluDeleteQuadric, VOID, PVOID)
        gluQuadricNormals = declare(glu32.gluQuadricNormals, VOID, PVOID, GLenum)
        gluQuadricTexture = declare(glu32.gluQuadricTexture, VOID, PVOID, GLboolean)
        gluQuadricOrientation = declare(glu32.gluQuadricOrientation, VOID, PVOID, GLenum)
        gluQuadricDrawStyle = declare(glu32.gluQuadricDrawStyle, VOID, PVOID, GLenum)
        gluCylinder = declare(glu32.gluCylinder, VOID, PVOID, GLdouble, GLdouble, GLdouble, GLint, GLint)
        gluDisk = declare(glu32.gluDisk, VOID, PVOID, GLdouble, GLdouble, GLint, GLint)
        gluPartialDisk = declare(glu32.gluPartialDisk, VOID, PVOID, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble)
        gluSphere = declare(glu32.gluSphere, VOID, PVOID, GLdouble, GLint, GLint)
        gluQuadricCallback = declare(glu32.gluQuadricCallback, VOID, PVOID, GLenum, PVOID)
        gluNewTess = declare(glu32.gluNewTess, PVOID, VOID)
        gluDeleteTess = declare(glu32.gluDeleteTess, VOID, PVOID)
        gluTessBeginPolygon = declare(glu32.gluTessBeginPolygon, VOID, PVOID, PVOID)
        gluTessBeginContour = declare(glu32.gluTessBeginContour, VOID, PVOID)
        gluTessVertex = declare(glu32.gluTessVertex, VOID, PVOID, (GLdouble * 3), PVOID)
        gluTessEndContour = declare(glu32.gluTessEndContour, VOID, PVOID)
        gluTessEndPolygon = declare(glu32.gluTessEndPolygon, VOID, PVOID)
        gluTessProperty = declare(glu32.gluTessProperty, VOID, PVOID, GLenum, GLdouble)
        gluTessNormal = declare(glu32.gluTessNormal, VOID, PVOID, GLdouble, GLdouble, GLdouble)
        gluTessCallback = declare(glu32.gluTessCallback, VOID, PVOID, GLenum, PVOID)
        gluGetTessProperty = declare(glu32.gluGetTessProperty, VOID, PVOID, GLenum, POINTER(GLdouble))
        gluDeleteNurbsRenderer = declare(glu32.gluDeleteNurbsRenderer, VOID, PVOID)
        gluBeginSurface = declare(glu32.gluBeginSurface, VOID, PVOID)
        gluBeginCurve = declare(glu32.gluBeginCurve, VOID, PVOID)
        gluEndCurve = declare(glu32.gluEndCurve, VOID, PVOID)
        gluEndSurface = declare(glu32.gluEndSurface, VOID, PVOID)
        gluBeginTrim = declare(glu32.gluBeginTrim, VOID, PVOID)
        gluEndTrim = declare(glu32.gluEndTrim, VOID, PVOID)
        gluPwlCurve = declare(glu32.gluPwlCurve, VOID, PVOID, GLint, POINTER(GLfloat), GLint, GLenum)
        #gluQuadricCurve = declare(glu32.gluQuadricCurve, VOID, PVOID, GLint, POINTER(GLfloat), GLint, POINTER(GLfloat), GLint, GLenum)
        #gluQuadricSurface = declare(glu32.gluQuadricSurface, VOID, PVOID, GLint, PFLOAT, GLint, POINTER(GLfloat), GLint, GLint, POINTER(GLfloat), GLint, GLint, GLenum)
        gluLoadSamplingMatrices = declare(glu32.gluLoadSamplingMatrices, VOID, PVOID, (GLfloat * 16), (GLfloat * 16), (GLint * 4))
        #gluQuadricProperty = declare(glu32.gluQuadricProperty, VOID, PVOID, GLenum, GLfloat)
        gluGetNurbsProperty = declare(glu32.gluGetNurbsProperty, VOID, PVOID, GLenum, POINTER(GLfloat))
        gluQuadricCallback = declare(glu32.gluQuadricCallback, VOID, PVOID, GLenum, PVOID)
    #***           Generic constants               ***
        # Version
        GLU_VERSION_1_1 = 1
        GLU_VERSION_1_2 = 1
        # Errors:(return value 0 = no error)
        GLU_INVALID_ENUM = 100900
        GLU_INVALID_VALUE = 100901
        GLU_OUT_OF_MEMORY = 100902
        GLU_INCOMPATIBLE_GL_VERSION = 100903
        # StringName
        GLU_VERSION = 100800
        GLU_EXTENSIONS = 100801
        # Boolean
        GLU_TRUE = GL_TRUE
        GLU_FALSE = GL_FALSE
        #***           Quadric constants               ***
        # QuadricNormal
        GLU_SMOOTH = 100000
        GLU_FLAT = 100001
        GLU_NONE = 100002
        # QuadricDrawStyle
        GLU_POINT = 100010
        GLU_LINE = 100011
        GLU_FILL = 100012
        GLU_SILHOUETTE = 100013
        # QuadricOrientation
        GLU_OUTSIDE = 100020
        GLU_INSIDE = 100021
        # Callback types:
        #      GLU_ERROR               100103
        #***           Tesselation constants           ***
        GLU_TESS_MAX_COORD = 1.0e150
        # TessProperty
        GLU_TESS_WINDING_RULE = 100140
        GLU_TESS_BOUNDARY_ONLY = 100141
        GLU_TESS_TOLERANCE = 100142
        # TessWinding
        GLU_TESS_WINDING_ODD = 100130
        GLU_TESS_WINDING_NONZERO = 100131
        GLU_TESS_WINDING_POSITIVE = 100132
        GLU_TESS_WINDING_NEGATIVE = 100133
        GLU_TESS_WINDING_ABS_GEQ_TWO = 100134
        # TessCallback
        GLU_TESS_BEGIN = 100100 # void(CALLBACK*)(GLenum    type)
        GLU_TESS_VERTEX = 100101 # void(CALLBACK*)(void      *data)
        GLU_TESS_END = 100102 # void(CALLBACK*)(void)
        GLU_TESS_ERROR = 100103 # void(CALLBACK*)(GLenum    errno)
        GLU_TESS_EDGE_FLAG = 100104 # void(CALLBACK*)(GLboolean boundaryEdge)
        GLU_TESS_COMBINE = 100105 # void(CALBACK*)(GLdouble coords[3],
        #void      **dataOut)

        GLU_TESS_BEGIN_DATA = 100106 # void(CALBACK*)(GLenum type,
        #void      *polygon_data)

        GLU_TESS_VERTEX_DATA = 100107 # void(CALBACK*)(void *data,
        #void      *polygon_data)

        GLU_TESS_END_DATA = 100108 # void(CALLBACK*)(void      *polygon_data)
        GLU_TESS_ERROR_DATA = 100109 #/* void(CALBACK*)(GLenum errno,
        #void      *polygon_data)

        GLU_TESS_EDGE_FLAG_DATA = 100110 # void(CALBACK*)(GLboolean boundaryEdge,
        #void      *polygon_data)

        GLU_TESS_COMBINE_DATA = 100111 #/* void(CALBACK*)(GLdouble coords[3],
        #void      *polygon_data)

        # TessError
        GLU_TESS_ERROR1 = 100151
        GLU_TESS_ERROR2 = 100152
        GLU_TESS_ERROR3 = 100153
        GLU_TESS_ERROR4 = 100154
        GLU_TESS_ERROR5 = 100155
        GLU_TESS_ERROR6 = 100156
        GLU_TESS_ERROR7 = 100157
        GLU_TESS_ERROR8 = 100158
        GLU_TESS_MISSING_BEGIN_POLYGON = GLU_TESS_ERROR1
        GLU_TESS_MISSING_BEGIN_CONTOUR = GLU_TESS_ERROR2
        GLU_TESS_MISSING_END_POLYGON = GLU_TESS_ERROR3
        GLU_TESS_MISSING_END_CONTOUR = GLU_TESS_ERROR4
        GLU_TESS_COORD_TOO_LARGE = GLU_TESS_ERROR5
        GLU_TESS_NEED_COMBINE_CALLBACK = GLU_TESS_ERROR6
        #***           NURBS constants                 ***
        # NurbsProperty
        GLU_AUTO_LOAD_MATRIX = 100200
        GLU_CULLING = 100201
        GLU_SAMPLING_TOLERANCE = 100203
        GLU_DISPLAY_MODE = 100204
        GLU_PARAMETRIC_TOLERANCE = 100202
        GLU_SAMPLING_METHOD = 100205
        GLU_U_STEP = 100206
        GLU_V_STEP = 100207
        # NurbsSampling
        GLU_PATH_LENGTH = 100215
        GLU_PARAMETRIC_ERROR = 100216
        GLU_DOMAIN_DISTANCE = 100217
        # NurbsTrim
        GLU_MAP1_TRIM_2 = 100210
        GLU_MAP1_TRIM_3 = 100211
        # NurbsDisplay
        #      GLU_FILL                100012
        GLU_OUTLINE_POLYGON = 100240
        GLU_OUTLINE_PATCH = 100241
        # NurbsCallback
        #      GLU_ERROR               100103
        # NurbsErrors
        GLU_NURBS_ERROR1 = 100251
        GLU_NURBS_ERROR2 = 100252
        GLU_NURBS_ERROR3 = 100253
        GLU_NURBS_ERROR4 = 100254
        GLU_NURBS_ERROR5 = 100255
        GLU_NURBS_ERROR6 = 100256
        GLU_NURBS_ERROR7 = 100257
        GLU_NURBS_ERROR8 = 100258
        GLU_NURBS_ERROR9 = 100259
        GLU_NURBS_ERROR10 = 100260
        GLU_NURBS_ERROR11 = 100261
        GLU_NURBS_ERROR12 = 100262
        GLU_NURBS_ERROR13 = 100263
        GLU_NURBS_ERROR14 = 100264
        GLU_NURBS_ERROR15 = 100265
        GLU_NURBS_ERROR16 = 100266
        GLU_NURBS_ERROR17 = 100267
        GLU_NURBS_ERROR18 = 100268
        GLU_NURBS_ERROR19 = 100269
        GLU_NURBS_ERROR20 = 100270
        GLU_NURBS_ERROR21 = 100271
        GLU_NURBS_ERROR22 = 100272
        GLU_NURBS_ERROR23 = 100273
        GLU_NURBS_ERROR24 = 100274
        GLU_NURBS_ERROR25 = 100275
        GLU_NURBS_ERROR26 = 100276
        GLU_NURBS_ERROR27 = 100277
        GLU_NURBS_ERROR28 = 100278
        GLU_NURBS_ERROR29 = 100279
        GLU_NURBS_ERROR30 = 100280
        GLU_NURBS_ERROR31 = 100281
        GLU_NURBS_ERROR32 = 100282
        GLU_NURBS_ERROR33 = 100283
        GLU_NURBS_ERROR34 = 100284
        GLU_NURBS_ERROR35 = 100285
        GLU_NURBS_ERROR36 = 100286
        GLU_NURBS_ERROR37 = 100287
        #***           Backwards compatibility for old tesselator           ***
        gluBeginPolygon = declare(glu32.gluBeginPolygon, VOID, PVOID)
        gluNextContour = declare(glu32.gluNextContour, VOID, PVOID, GLenum)
        gluEndPolygon = declare(glu32.gluEndPolygon, VOID, PVOID)
        # Contours types -- obsolete!
        GLU_CW = 100120
        GLU_CCW = 100121
        GLU_INTERIOR = 100122
        GLU_EXTERIOR = 100123
        GLU_UNKNOWN = 100124
        # Names without "TESS_" prefix
        GLU_BEGIN = GLU_TESS_BEGIN
        GLU_VERTEX = GLU_TESS_VERTEX
        GLU_END = GLU_TESS_END
        GLU_ERROR = GLU_TESS_ERROR
        GLU_EDGE_FLAG = GLU_TESS_EDGE_FLAG
        # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)

        # REGION ***
    # __GLU_H__
# __glu_h__