"""
/**************************************************************************\
*
* Copyright (c) 1998-2001, Microsoft Corp.  All Rights Reserved.
*
* Module Name:
*
*   Metafile headers
*
* Abstract:
*
*   GDI+ Metafile Related Structures
*
\**************************************************************************/
"""

from . import cpreproc

if cpreproc.pragma_once("_GDIPLUSMETAHEADER_H"):
    from .gdiplusenums import *
    from .gdiplustypes import *
    from .wingdi import *

    # REGION *** Desktop Family ***

    class ENHMETAHEADER3(CStructure):
        _pack_ = 8
        _fields_ = [
            ("iType", DWORD),              # Record type EMR_HEADER
            ("nSize", DWORD),              # Record size in bytes.  This may be greater
                                           # than the sizeof(ENHMETAHEADER).
            ("rclBounds", RECTL),          # Inclusive-inclusive bounds in device units
            ("rclFrame", RECTL),           # Inclusive-inclusive Picture Frame .01mm unit
            ("dSignature", DWORD),         # Signature.  Must be ENHMETA_SIGNATURE.
            ("nVersion", DWORD),           # Version number
            ("nBytes", DWORD),             # Size of the metafile in bytes
            ("nRecords", DWORD),           # Number of records in the metafile
            ("nHandles", WORD),            # Number of handles in the handle table
                                           # Handle index zero is reserved.
            ("sReserved", WORD),           # Reserved.  Must be zero.
            ("nDescription", DWORD),       # Number of chars in the unicode desc string
                                           # This is 0 if there is no description string
            ("offDescription", DWORD),     # Offset to the metafile description record.
                                           # This is 0 if there is no description string
            ("nPalEntries", DWORD),        # Number of entries in the metafile palette.
            ("szlDevice", SIZEL),          # Size of the reference device in pels
            ("szlMillimeters", SIZEL)      # Size of the reference device in millimeters
        ]

    # Placeable WMFs

    # Placeable Metafiles were created as a non-standard way of specifying how 
    # a metafile is mapped and scaled on an output device.
    # Placeable metafiles are quite wide-spread, but not directly supported by
    # the Windows API. To playback a placeable metafile using the Windows API,
    # you will first need to strip the placeable metafile header from the file.
    # This is typically performed by copying the metafile to a temporary file
    # starting at file offset 22 (0x16). The contents of the temporary file may
    # then be used as input to the Windows GetMetaFile(), PlayMetaFile(),
    # CopyMetaFile(), etc. GDI functions.

    # Each placeable metafile begins with a 22-byte header,
    #  followed by a standard metafile:

    class PWMFRect16(CStructure):
        _pack_ = 2
        _fields_ = [
            ("Left", INT16),
            ("Top", INT16),
            ("Right", INT16),
            ("Bottom", INT16)
        ]

    class WmfPlaceableFileHeader(CStructure):
        _pack_ = 2
        _fields_ = [
            ("Key", UINT32),                # GDIP_WMF_PLACEABLEKEY
            ("Hmf", INT16),                 # Metafile HANDLE number (always 0)
            ("BoundingBox", PWMFRect16),    # Coordinates in metafile units
            ("Inch", INT16),                # Number of metafile units per inch
            ("Reserved", INT32),            # Reserved (always 0)
            ("Checksum", INT16),            # Checksum value for previous 10 WORDs
        ]

    # Key contains a special identification value that indicates the presence
    # of a placeable metafile header and is always 0x9AC6CDD7.

    # Handle is used to stored the handle of the metafile in memory. When written
    # to disk, this field is not used and will always contains the value 0.

    # Left, Top, Right, and Bottom contain the coordinates of the upper-left
    # and lower-right corners of the image on the output device. These are
    # measured in twips.

    # A twip (meaning "twentieth of a point") is the logical unit of measurement
    # used in Windows Metafiles. A twip is equal to 1/1440 of an inch. Thus 720
    # twips equal 1/2 inch, while 32,768 twips is 22.75 inches.

    # Inch contains the number of twips per inch used to represent the image.
    # Normally, there are 1440 twips per inch; however, this number may be
    # changed to scale the image. A value of 720 indicates that the image is
    # double its normal size, or scaled to a factor of 2:1. A value of 360
    # indicates a scale of 4:1, while a value of 2880 indicates that the image
    # is scaled down in size by a factor of two. A value of 1440 indicates
    # a 1:1 scale ratio.

    # Reserved is not used and is always set to 0.

    # Checksum contains a checksum value for the previous 10 WORDs in the header.
    # This value can be used in an attempt to detect if the metafile has become
    # corrupted. The checksum is calculated by XORing each WORD value to an
    # initial value of 0.

    # If the metafile was recorded with a reference Hdc that was a display.

    GDIP_EMFPLUSFLAGS_DISPLAY      = 0x00000001

    class MetafileHeader(CStructure):
        class DUMMYUNIONNAME1(Union):
            _fields_ = [
                ("WmfHeader", METAHEADER),
                ("EmfHeader", ENHMETAHEADER3)
            ]
        ("Type", MetafileType),
        ("Size", UINT),               # Size of the metafile (in bytes)
        ("Version", UINT),            # EMF+, EMF, or WMF version
        ("EmfPlusFlags", UINT),
        ("DpiX", REAL),
        ("DpiY", REAL),
        ("X", INT),                   # Bounds in device units
        ("Y", INT),
        ("Width", INT),
        ("Height", INT),
        ("u1", DUMMYUNIONNAME1),
        ("EmfPlusHeaderSize", INT),   # size of the EMF+ header in file
        ("LogicalDpiX", INT),         # Logical Dpi of reference Hdc
        ("LogicalDpiY", INT)          # usually valid only for EMF+
        
        Type: int
        Size: int
        Version: int
        EmfPlusFlags: int
        DpiX: float
        DpiY: float
        X: int
        Y: int
        Width: int
        Height: int
        u1: DUMMYUNIONNAME1
        EmfPlusHeaderSize: int
        LogicalDpiX: int
        LogicalDpiY: int

        def GetType(self) -> MetafileType:
            return self.Type

        def GetMetafileSize(self) -> int:
            return self.Size

        # If IsEmfPlus, this is the EMF+ version; else it is the WMF or EMF ver
        
        def GetVersion(self) -> int:
            return self.Version

        # Get the EMF+ flags associated with the metafile
        
        def GetEmfPlusFlags(self) -> int:
            return self.EmfPlusFlags

        def GetDpiX(self) -> float:
            return self.DpiX

        def GetDpiY(self) -> float:
            return self.DpiY

        def GetBounds(self, rect) -> None:
            rect.contents.X = self.X
            rect.contents.Y = self.Y
            rect.contents.Width = self.Width
            rect.contents.Height = self.Height
        
        # Is it any type of WMF (standard or Placeable Metafile)?
        
        def IsWmf(self) -> bool:
            return ((self.Type == MetafileTypeWmf) or (self.Type == MetafileTypeWmfPlaceable))

        # Is this an Placeable Metafile?

        def IsWmfPlaceable(self) -> bool:
            return (self.Type == MetafileTypeWmfPlaceable)

        # Is this an EMF (not an EMF+)?
        
        def IsEmf(self) -> bool: 
            return (self.Type == MetafileTypeEmf)

        # Is this an EMF or EMF+ file?
        
        def IsEmfOrEmfPlus(self) -> bool:
            return (self.Type >= MetafileTypeEmf)

        # Is this an EMF+ file?
        
        def IsEmfPlus(self) -> bool: 
            return (self.Type >= MetafileTypeEmfPlusOnly)

        # Is this an EMF+ dual (has dual, down-level records) file?
        
        def IsEmfPlusDual(self) -> bool: 
            return (self.Type == MetafileTypeEmfPlusDual)

        # Is this an EMF+ only (no dual records) file?
        
        def IsEmfPlusOnly(self):
            return (self.Type == MetafileTypeEmfPlusOnly)

        # If it's an EMF+ file, was it recorded against a display Hdc?
        
        def IsDisplay(self) -> bool:
            return (self.IsEmfPlus() and
                    ((self.EmfPlusFlags & GDIP_EMFPLUSFLAGS_DISPLAY) != 0))

        # Get the WMF header of the metafile (if it is a WMF)
        
        def GetWmfHeader(self):
            if (self.IsWmf()):
                return cast(byref(self.u1.WmfHeader), PMETAHEADER)
            return NULL

        # Get the EMF header of the metafile (if it is an EMF)
        
        def GetEmfHeader(self):
            if (self.IsEmfOrEmfPlus()):
                return cast(byref(self.u1.EmfHeader), POINTER(ENHMETAHEADER3))
            return NULL

    # REGION ***