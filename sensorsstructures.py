"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    SensorsStructures.h

Abstract:

    Sensor structures header file

--"""

from . import cpreproc

from .minwindef import FLOAT, Structure, POINTER, Union, INT

# The following flag is required to prevent structure redefinition with WpSensor.h
# we keep the #pragma above to benefit from the speed advantages this pragma brings.
if cpreproc.pragma_once("_SENSORS_STRUCTURES"):
    class VEC3D(CStructure):
        _fields_ = [
            ("X", FLOAT),
            ("Y", FLOAT),
            ("Z", FLOAT)
        ]
    PVEC3D = POINTER(VEC3D)

    class MATRIX3X3(Union):
        class U(Union):
            class S1(CStructure):
                _fields_ = [
                    ("A11", FLOAT),
                    ("A12", FLOAT),
                    ("A13", FLOAT),
                    ("A21", FLOAT),
                    ("A22", FLOAT),
                    ("A23", FLOAT),
                    ("A31", FLOAT),
                    ("A32", FLOAT),
                    ("A33", FLOAT)
                ]
            class S2(CStructure):
                _fields_ = [
                    ("V1", VEC3D),
                    ("V2", VEC3D),
                    ("V3", VEC3D)
                ]
            _fields_ = [
                ("s1", S1),
                ("s2", S2),
                ("M", FLOAT * 3 * 3)
            ]
        _fields_ = [
            ("u", U)
        ]
    PMATRIX3X3 = POINTER(MATRIX3X3)

    
    class QUATERNION(CStructure):
        """
        Simple structure representing a 4 dimensional vector used for simple 3D rotation operation. 
        The rotation is done around the axis formed by the vector v= [X, Y, Z] and is of angle ?, and we have:
        W=cos(theta/2)
        |v|=sin(theta/2)
        """
        _fields_ = [
            ("X", FLOAT),     # x component of rotation axis vector * sin(theta/2) also i (imaginary) coefficient
            ("Y", FLOAT),     # y component of rotation axis vector * sin(theta/2) also j coefficient
            ("Z", FLOAT),     # z component of rotation axis vector * sin(theta/2) also k coefficient
            ("W", FLOAT)      # real coefficient = cos(theta/2)
        ]
    PQUATERNION = POINTER(QUATERNION)


    AXIS = INT
    if True:
        AXIS_X = 0
        AXIS_Y = 1
        AXIS_Z = 2
        AXIS_MAX = 3
    PAXIS = POINTER(AXIS)

# _SENSORS_STRUCTURES