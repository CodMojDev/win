"""
/**************************************************************************\
*
* Copyright (c) 1998-2001, Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   GdiplusTypes.h
*
* Abstract:
*
*   GDI+ Types
*
\**************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from typing import Self

if cpreproc.pragma_once("_GDIPLUSTYPES_H"):
    
    from .gdiplusenums import EmfPlusRecordType

    # REGION *** Desktop Family ***

    #--------------------------------------------------------------------------
    # Callback functions
    #--------------------------------------------------------------------------

    ImageAbort = CALLBACK(BOOL, PVOID)
    DrawImageAbort = ImageAbort
    GetThumbnailImageAbort = ImageAbort

    # Callback for EnumerateMetafile methods.  The parameters are:

    #      recordType      WMF, EMF, or EMF+ record type
    #      flags           (always 0 for WMF/EMF records)
    #      dataSize        size of the record data (in bytes), or 0 if no data
    #      data            pointer to the record data, or NULL if no data
    #      callbackData    pointer to callbackData, if any

    # This method can then call Metafile::PlayRecord to play the
    # record that was just enumerated.  If this method  returns
    # FALSE, the enumeration process is aborted.  Otherwise, it continues.

    EnumerateMetafileProc = CALLBACK(BOOL, EmfPlusRecordType, UINT, UINT, PBYTE, PVOID)

    # This is the main GDI+ Abort interface

    class GdiplusAbort(CStructure):
        _pack_ = 8
        _fields_ = [
            ("Abort", WINFUNCTYPE(HRESULT))
        ]

    #--------------------------------------------------------------------------
    # Primitive data types
    #
    # NOTE:
    #  Types already defined in standard header files:
    #      INT8
    #      UINT8
    #      INT16
    #      UINT16
    #      INT32
    #      UINT32
    #      INT64
    #      UINT64
    #
    #  Avoid using the following types:
    #      LONG - use INT
    #      ULONG - use UINT
    #      DWORD - use UINT32
    #--------------------------------------------------------------------------

    from .ucrt.float import *

    REAL = FLOAT

    REAL_MAX = FLT_MAX
    REAL_MIN = FLT_MIN
    REAL_TOLERANCE = (FLT_MIN * 100)
    REAL_EPSILON = 1.192092896e-07        # FLT_EPSILON

    #--------------------------------------------------------------------------
    # Status return values from GDI+ methods
    #--------------------------------------------------------------------------

    Status = INT
    if True:
        Ok = 0
        GenericError = 1
        InvalidParameter = 2
        OutOfMemory = 3
        ObjectBusy = 4
        InsufficientBuffer = 5
        NotImplemented = 6
        Win32Error = 7
        WrongState = 8
        Aborted = 9
        FileNotFound = 10
        ValueOverflow = 11
        AccessDenied = 12
        UnknownImageFormat = 13
        FontFamilyNotFound = 14
        FontStyleNotFound = 15
        NotTrueTypeFont = 16
        UnsupportedGdiplusVersion = 17
        GdiplusNotInitialized = 18
        PropertyNotFound = 19
        PropertyNotSupported = 20
        ProfileNotFound = 21

    #--------------------------------------------------------------------------
    # Represents a dimension in a 2D coordinate system (floating-point coordinates)
    #--------------------------------------------------------------------------

    class SizeF:
        Width: float
        Height: float
        def __init__(self, varying_type: float | Self = 0.0, height=0.0):
            if isinstance(varying_type, self.__class__):
                self.Width = varying_type.Width
                self.Height = varying_type.Height
            else:
                self.Width = varying_type
                self.Height = height

        def __add__(self, sz: Self) -> Self:
            return self.__class__(self.Width + sz.Width,
                                    self.Height + sz.Height)
        
        def __sub__(self, sz: Self) -> Self:
            return self.__class__(self.Width - sz.Width,
                                    self.Height - sz.Height)
        
        def __eq__(self, sz: Self) -> bool:
            return (self.Width == sz.Width) and (self.Height == sz.Height)
        
        def __bool__(self) -> bool:
            return (self.Width == 0.0 and self.Height == 0.0)
    
    #--------------------------------------------------------------------------
    # Represents a dimension in a 2D coordinate system (integer coordinates)
    #--------------------------------------------------------------------------

    class Size():
        Width: int
        Height: int
        def __init__(self, varying_type: int | Self = 0, height=0):
            if isinstance(varying_type, self.__class__):
                self.Width = varying_type.Width
                self.Height = varying_type.Height
            else:
                self.Width = varying_type
                self.Height = height

        def __add__(self, sz: Self) -> Self:
            return self.__class__(self.Width + sz.Width,
                                    self.Height + sz.Height)
        
        def __sub__(self, sz: Self) -> Self:
            return self.__class__(self.Width - sz.Width,
                                    self.Height - sz.Height)
        
        def __eq__(self, sz: Self) -> bool:
            return (self.Width == sz.Width) and (self.Height == sz.Height)
        
        def __bool__(self) -> bool:
            return (self.Width == 0 and self.Height == 0)

    #--------------------------------------------------------------------------
    # Represents a location in a 2D coordinate system (floating-point coordinates)
    #--------------------------------------------------------------------------

    class PointF:
        class SPointF(CStructure):
            _pack_ = 8
            _fields_ = [
                ("X", FLOAT),
                ("Y", FLOAT)
            ]
        X: float
        Y: float
        def __init__(self, varying_type: float | Self | SizeF = 0.0, y: float = 0.0):
            if isinstance(varying_type, self.__class__):
                self.X = varying_type.X
                self.Y = varying_type.Y
            elif isinstance(varying_type, SizeF):
                self.X = varying_type.Width
                self.Y = varying_type.Height
            else:
                self.X = varying_type
                self.Y = y

        def to_ctypes(self):
            return self.SPointF(self.X, self.Y)
        
        def __add__(self, point: Self) -> Self:
            return self.__class__(self.X + point.X,
                                  self.Y + point.Y)
        
        def __sub__(self, point: Self) -> Self:
            return self.__class__(self.X - point.X,
                                  self.Y - point.Y)
        
        def __eq__(self, point: Self) -> bool:
            return (self.X == point.X) and (self.Y == point.Y)
        
    #--------------------------------------------------------------------------
    # Represents a location in a 2D coordinate system (integer coordinates)
    #--------------------------------------------------------------------------

    class Point:
        X: int
        Y: int
        def __init__(self, varying_type: int | Self | Size = 0, y: float = 0):
            if isinstance(varying_type, self.__class__):
                self.X = varying_type.X
                self.Y = varying_type.Y
            elif isinstance(varying_type, Size):
                self.X = varying_type.Width
                self.Y = varying_type.Height
            else:
                self.X = varying_type
                self.Y = y
        
        def __add__(self, point: Self) -> Self:
            return self.__class__(self.X + point.X,
                                self.Y + point.Y)
        
        def __sub__(self, point: Self) -> Self:
            return self.__class__(self.X - point.X,
                                self.Y - point.Y)
        
        def __eq__(self, point: Self) -> bool:
            return (self.X == point.X) and (self.Y == point.Y)
        
    #--------------------------------------------------------------------------
    # Represents a rectangle in a 2D coordinate system (floating-point coordinates)
    #--------------------------------------------------------------------------

    class RectF:
        X: float
        Y: float
        Width: float
        Height: float
        def __init__(self, varying_type1: float | PointF = 0.0, varying_type2: float | SizeF = 0.0, width: float = 0.0, height: float = 0.0):
            if isinstance(varying_type1, PointF):
                self.X = varying_type1.X
                self.Y = varying_type1.Y
                if isinstance(varying_type2, SizeF):
                    self.Width = varying_type2.Width
                    self.Height = varying_type2.Height
                else:
                    self.Width = width
                    self.Height = height
            else:
                self.X = varying_type1
                self.Y = varying_type2
                self.Width = width
                self.Height = height
        
        def clone(self) -> Self:
            return self.__class__(self.X, self.Y, self.Width, self.Height)

        def get_location(self, point: PointF) -> None:
            point.X = self.X
            point.Y = self.Y
        
        def get_size(self, size: SizeF) -> None:
            size.Width = self.Width
            size.Height = self.Height
        
        def get_bounds(self, rect: Self) -> None:
            rect.X = self.X
            rect.Y = self.Y
            rect.Width = self.Width
            rect.Height = self.Height
        
        def get_left(self) -> float:
            return self.X
        
        def get_top(self) -> float:
            return self.Y
        
        def get_right(self) -> float:
            return self.X + self.Width
        
        def get_bottom(self) -> float:
            return self.Y + self.Height
        
        def is_empty_area(self) -> bool:
            return (self.Width <= REAL_EPSILON) or (self.Height <= REAL_EPSILON)
        
        def __eq__(self, rect: Self) -> bool:
            return (self.X == rect.X          ) and (
                    self.Y == rect.Y          ) and (
                    self.Width == rect.Width  ) and (
                    self.Height == rect.Height)
        
        def contains(self, varying_type: float | PointF | Self, y: float = 0.0) -> bool:
            if isinstance(varying_type, PointF):
                return self.contains(varying_type.X, varying_type.Y)
            elif isinstance(varying_type, self.__class__):
                return (self.X <= varying_type.X) and (varying_type.get_right()  <= self.get_right() ) and (
                       (self.Y <= varying_type.Y) and (varying_type.get_bottom() <= self.get_bottom())     )
            else:
                return varying_type >= self.X and varying_type < self.X + self.Width  and (
                       y >= self.Y            and y            < self.Y + self.Height     )
        
        def inflate(self, varying_type: float | PointF | Self, dy: float = 0.0) -> None:
            if isinstance(varying_type, PointF):
                self.inflate(varying_type.X, varying_type.Y)
            else:
                self.X -= varying_type
                self.Y -= dy
                self.Width += 2 * varying_type
                self.Height += 2 * dy
        
        def intersect(self, c: Self, a: Self = None, b: Self = None) -> bool:
            if not a:
                return self.intersect(self, self, c)
            right = min(a.get_right(), b.get_right())
            bottom = min(a.get_bottom(), b.get_bottom())
            left = max(a.get_left(), b.get_left())
            top = max(a.get_top(), b.get_top())
            c.X = left
            c.Y = top
            c.Width = right - left
            c.Height = bottom - top
            return not c.is_empty_area()
        
        def intersects_with(self, rect: Self) -> bool:
            return (self.get_left()   < rect.get_right()   and
                    self.get_top()    < rect.get_bottom()  and
                    self.get_right()  > rect.get_left()    and
                    self.get_bottom() > rect.get_top()        )
        
        def union(self, c: Self, a: Self, b: Self) -> bool:
            right = max(a.get_right(), b.get_right())
            bottom = max(a.get_bottom(), b.get_bottom())
            left = min(a.get_left(), b.get_left())
            top = min(a.get_top(), b.get_top())
            c.X = left
            c.Y = top
            c.Width = right - left
            c.Height = bottom - top
            return not c.is_empty_area()
        
        def offset(self, varying_type: float | PointF, dy: float = 0.0) -> None:
            if isinstance(varying_type, PointF):
                return self.offset(varying_type.X, varying_type.Y)
            self.X += varying_type
            self.Y += dy

    #--------------------------------------------------------------------------
    # Represents a rectangle in a 2D coordinate system (integer coordinates)
    #--------------------------------------------------------------------------
    
    class Rect:
        X: int
        Y: int
        Width: int
        Height: int
        def __init__(self, varying_type1: int | Point = 0, varying_type2: int | Size = 0, width: int = 0, height: int = 0):
            if isinstance(varying_type1, Point):
                self.X = varying_type1.X
                self.Y = varying_type1.Y
                if isinstance(varying_type2, Size):
                    self.Width = varying_type2.Width
                    self.Height = varying_type2.Height
                else:
                    self.Width = width
                    self.Height = height
            else:
                self.X = varying_type1
                self.Y = varying_type2
                self.Width = width
                self.Height = height
        
        def clone(self) -> Self:
            return self.__class__(self.X, self.Y, self.Width, self.Height)

        def get_location(self, point: Point) -> None:
            point.X = self.X
            point.Y = self.Y
        
        def get_size(self, size: Size) -> None:
            size.Width = self.Width
            size.Height = self.Height
        
        def get_bounds(self, rect: Self) -> None:
            rect.X = self.X
            rect.Y = self.Y
            rect.Width = self.Width
            rect.Height = self.Height
        
        def get_left(self) -> int:
            return self.X
        
        def get_top(self) -> int:
            return self.Y
        
        def get_right(self) -> int:
            return self.X + self.Width
        
        def get_bottom(self) -> int:
            return self.Y + self.Height
        
        def is_empty_area(self) -> bool:
            return (self.Width <= 0) or (self.Height <= 0)
        
        def __eq__(self, rect: Self) -> bool:
            return (self.X == rect.X          ) and (
                    self.Y == rect.Y          ) and (
                    self.Width == rect.Width  ) and (
                    self.Height == rect.Height)
        
        def contains(self, varying_type: int | Point | Self, y: int = 0) -> bool:
            if isinstance(varying_type, Point):
                return self.contains(varying_type.X, varying_type.Y)
            elif isinstance(varying_type, self.__class__):
                return (self.X <= varying_type.X) and (varying_type.get_right()  <= self.get_right() ) and (
                    (self.Y <= varying_type.Y) and (varying_type.get_bottom() <= self.get_bottom())     )
            else:
                return varying_type >= self.X and varying_type < self.X + self.Width  and (
                    y >= self.Y            and y            < self.Y + self.Height     )
        
        def inflate(self, varying_type: int | Point | Self, dy: int = 0) -> None:
            if isinstance(varying_type, Point):
                self.inflate(varying_type.X, varying_type.Y)
            else:
                self.X -= varying_type
                self.Y -= dy
                self.Width += 2 * varying_type
                self.Height += 2 * dy
        
        def intersect(self, c: Self, a: Self = None, b: Self = None) -> bool:
            if not a:
                return self.intersect(self, self, c)
            right = min(a.get_right(), b.get_right())
            bottom = min(a.get_bottom(), b.get_bottom())
            left = max(a.get_left(), b.get_left())
            top = max(a.get_top(), b.get_top())
            c.X = left
            c.Y = top
            c.Width = right - left
            c.Height = bottom - top
            return not c.is_empty_area()
        
        def intersects_with(self, rect: Self) -> bool:
            return (self.get_left()   < rect.get_right()   and
                    self.get_top()    < rect.get_bottom()  and
                    self.get_right()  > rect.get_left()    and
                    self.get_bottom() > rect.get_top()        )
        
        def union(self, c: Self, a: Self, b: Self) -> bool:
            right = max(a.get_right(), b.get_right())
            bottom = max(a.get_bottom(), b.get_bottom())
            left = min(a.get_left(), b.get_left())
            top = min(a.get_top(), b.get_top())
            c.X = left
            c.Y = top
            c.Width = right - left
            c.Height = bottom - top
            return not c.is_empty_area()
        
        def offset(self, varying_type: int | Point, dy: int = 0) -> None:
            if isinstance(varying_type, Point):
                return self.offset(varying_type.X, varying_type.Y)
            self.X += varying_type
            self.Y += dy

    class PathData:
        def __init__(self):
            self.count = 0
            self.Points = NULL
            self.Types = NULL

        def __invert__(self):
            if self.Points:
                memset(cast(self.Points, PVOID), 0, sizeof(PointF.SPointF))
            if self.Types:
                memset(cast(self.Types, PVOID), 0, sizeof(BYTE))

    class CharacterRange:
        def __init__(self, first = 0, length = 0):
            self.First = first
            self.Length = length
        
        def toclass(self, rhs):
            self.First = rhs.First
            self.Length = rhs.Length