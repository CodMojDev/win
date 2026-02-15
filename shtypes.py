#+-------------------------------------------------------------------------
#
#  Microsoft Windows
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
#--------------------------------------------------------------------------

from . import cpreproc
from .wtypes import *

if cpreproc.ifndef("__shtypes_h__"):
    cpreproc.define("__shtypes_h__")
    #===========================================================================
    #
    # Object identifiers in the explorer's name space (ItemID and IDList)
    #
    #  All the items that the user can browse with the explorer (such as files,
    # directories, servers, work-groups, etc.) has an identifier which is unique
    # among items within the parent folder. Those identifiers are called item
    # IDs (SHITEMID). Since all its parent folders have their own item IDs,
    # any items can be uniquely identified by a list of item IDs, which is called
    # an ID list (ITEMIDLIST).
    #
    #  ID lists are almost always allocated by the task allocator (see some
    # description below as well as OLE 2.0 SDK) and may be passed across
    # some of shell interfaces (such as IShellFolder). Each item ID in an ID list
    # is only meaningful to its parent folder (which has generated it), and all
    # the clients must treat it as an opaque binary data except the first two
    # bytes, which indicates the size of the item ID.
    #
    #  When a shell extension -- which implements the IShellFolder interace --
    # generates an item ID, it may put any information in it, not only the data
    # with that it needs to identifies the item, but also some additional
    # information, which would help implementing some other functions efficiently.
    # For example, the shell's IShellFolder implementation of file system items
    # stores the primary (long) name of a file or a directory as the item
    # identifier, but it also stores its alternative (short) name, size and date
    # etc.
    #
    #  When an ID list is passed to one of shell APIs (such as SHGetPathFromIDList),
    # it is always an absolute path -- relative from the root of the name space,
    # which is the desktop folder. When an ID list is passed to one of IShellFolder
    # member function, it is always a relative path from the folder (unless it
    # is explicitly specified).
    #
    #===========================================================================
    #
    # SHITEMID -- Item ID  (mkid)
    #     USHORT      cb;             # Size of the ID (including cb itself)
    #     BYTE        abID[];         # The item ID (variable length)
    #
    class SHITEMID(CStructure):
        _pack_ = 1
        _fields_ = [
            ("cb", USHORT),
            ("abID", BYTE * 1)
        ]

    LPSHITEMID = POINTER(SHITEMID)
    LPCSHITEMID = LPSHITEMID

    #
    # ITEMIDLIST -- List if item IDs (combined with 0-terminator)
    #
    class ITEMIDLIST(CStructure):
        _pack_ = 1
        _fields_ = [
            ("mkid", SHITEMID)
        ]

    ITEMIDLIST_RELATIVE = ITEMIDLIST
    ITEMID_CHILD = ITEMIDLIST
    ITEMIDLIST_ABSOLUTE = ITEMIDLIST

    LPITEMIDLIST = POINTER(ITEMIDLIST)
    LPCITEMIDLIST = LPITEMIDLIST

    PIDLIST_ABSOLUTE = LPITEMIDLIST
    PCIDLIST_ABSOLUTE = LPCITEMIDLIST
    PCUIDLIST_ABSOLUTE = LPCITEMIDLIST
    PIDLIST_RELATIVE = LPITEMIDLIST
    PCIDLIST_RELATIVE = LPCITEMIDLIST
    PUIDLIST_RELATIVE = LPITEMIDLIST
    PCUIDLIST_RELATIVE = LPCITEMIDLIST
    PITEMID_CHILD = LPITEMIDLIST
    PCITEMID_CHILD = LPCITEMIDLIST
    PUITEMID_CHILD = LPITEMIDLIST
    PCUITEMID_CHILD = LPCITEMIDLIST
    PCUITEMID_CHILD_ARRAY = POINTER(LPCITEMIDLIST)
    PCUIDLIST_RELATIVE_ARRAY = POINTER(LPCITEMIDLIST)
    PCIDLIST_ABSOLUTE_ARRAY = POINTER(LPCITEMIDLIST)
    PCUIDLIST_ABSOLUTE_ARRAY = POINTER(LPCITEMIDLIST)

    #typedef /* [unique] */  __RPC_unique_pointer BYTE_BLOB *wirePIDL;

    #-------------------------------------------------------------------------
    #
    # struct STRRET
    #
    # structure for returning strings from IShellFolder member functions
    #
    #-------------------------------------------------------------------------
    #
    #  uType indicate which union member to use 
    #    STRRET_WSTR    Use STRRET.pOleStr     must be freed by caller of GetDisplayNameOf
    #    STRRET_OFFSET  Use STRRET.uOffset     Offset into SHITEMID for ANSI string 
    #    STRRET_CSTR    Use STRRET.cStr        ANSI Buffer
    #
    STRRET_TYPE = INT
    if True:
        STRRET_WSTR	= 0
        STRRET_OFFSET	= 0x1
        STRRET_CSTR	= 0x2

    #if defined(_MSC_VER) && (_MSC_VER >= 1200)
    #pragma warning(push)
    #pragma warning(disable:4201) /* nonstandard extension used : nameless struct/union */
    #pragma once
    #endif
    #include <pshpack8.h>
    class STRRET(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("pOleStr", LPOLESTR),
                ("uOffset", UINT),
                ("cStr", CHAR * 260)
            ]
        _pack_ = 8
        _fields_ = [
            ("uType", UINT),
            ("u", _DUMMYUNIONNAME)
        ]
        _anonymous_ = ['u']
        
        cStr: IWideCharArrayFixedSize[260]
        pOleStr: LPOLESTR
        uOffset: int
        uType: int
        
    LPSTRRET = POINTER(STRRET)

    #-------------------------------------------------------------------------
    #
    # struct SHELLDETAILS
    #
    # structure for returning strings from IShellDetails
    #
    #-------------------------------------------------------------------------
    #
    #  fmt;            # LVCFMT_* value (header only)
    #  cxChar;         # Number of 'average' characters (header only)
    #  str;            # String information
    #
    #include <pshpack1.h>
    class SHELLDETAILS(CStructure):
        _fields_ = [
            ("fmt", INT),
            ("cxChar", INT),
            ("str", STRRET)
        ]
        
        cxChar: int
        str: STRRET
        fmt: int
        
    LPSHELLDETAILS = POINTER(SHELLDETAILS)

    #if (_WIN32_IE >= _WIN32_IE_IE60SP2)
    PERCEIVED = INT
    if True:
        PERCEIVED_TYPE_FIRST	= -3
        PERCEIVED_TYPE_CUSTOM	= -3
        PERCEIVED_TYPE_UNSPECIFIED	= -2
        PERCEIVED_TYPE_FOLDER	= -1
        PERCEIVED_TYPE_UNKNOWN	= 0
        PERCEIVED_TYPE_TEXT	= 1
        PERCEIVED_TYPE_IMAGE	= 2
        PERCEIVED_TYPE_AUDIO	= 3
        PERCEIVED_TYPE_VIDEO	= 4
        PERCEIVED_TYPE_COMPRESSED	= 5
        PERCEIVED_TYPE_DOCUMENT	= 6
        PERCEIVED_TYPE_SYSTEM	= 7
        PERCEIVED_TYPE_APPLICATION	= 8
        PERCEIVED_TYPE_GAMEMEDIA	= 9
        PERCEIVED_TYPE_CONTACTS	= 10
        PERCEIVED_TYPE_LAST	= 10

    PERCEIVEDFLAG_UNDEFINED = 0x0000
    PERCEIVEDFLAG_SOFTCODED = 0x0001
    PERCEIVEDFLAG_HARDCODED = 0x0002
    PERCEIVEDFLAG_NATIVESUPPORT = 0x0004
    PERCEIVEDFLAG_GDIPLUS = 0x0010
    PERCEIVEDFLAG_WMSDK = 0x0020
    PERCEIVEDFLAG_ZIPFOLDER = 0x0040
    PERCEIVEDFLAG = DWORD

    class COMDLG_FILTERSPEC(CStructure):
        _fields_ = [
            ("pszName", LPCWSTR),
            ("pszSpec", LPCWSTR)
        ]

    KNOWNFOLDERID = GUID

    REFKNOWNFOLDERID = POINTER(KNOWNFOLDERID)

    KF_REDIRECT_FLAGS = DWORD
    FOLDERTYPEID = GUID

    REFFOLDERTYPEID = POINTER(FOLDERTYPEID)

    TASKOWNERID = GUID

    REFTASKOWNERID = POINTER(TASKOWNERID)

    ELEMENTID = GUID

    REFELEMENTID = POINTER(ELEMENTID)

    SHCOLSTATE = INT
    if True:
        SHCOLSTATE_DEFAULT	= 0
        SHCOLSTATE_TYPE_STR	= 0x1
        SHCOLSTATE_TYPE_INT	= 0x2
        SHCOLSTATE_TYPE_DATE	= 0x3
        SHCOLSTATE_TYPEMASK	= 0xf
        SHCOLSTATE_ONBYDEFAULT	= 0x10
        SHCOLSTATE_SLOW	= 0x20
        SHCOLSTATE_EXTENDED	= 0x40
        SHCOLSTATE_SECONDARYUI	= 0x80
        SHCOLSTATE_HIDDEN	= 0x100
        SHCOLSTATE_PREFER_VARCMP	= 0x200
        SHCOLSTATE_PREFER_FMTCMP	= 0x400
        SHCOLSTATE_NOSORTBYFOLDERNESS	= 0x800
        SHCOLSTATE_VIEWONLY	= 0x10000
        SHCOLSTATE_BATCHREAD	= 0x20000
        SHCOLSTATE_NO_GROUPBY	= 0x40000
        SHCOLSTATE_FIXED_WIDTH	= 0x1000
        SHCOLSTATE_NODPISCALE	= 0x2000
        SHCOLSTATE_FIXED_RATIO	= 0x4000
        SHCOLSTATE_DISPLAYMASK	= 0xf000

    SHCOLSTATEF = DWORD

    SHCOLUMNID = PROPERTYKEY
    LPCSHCOLUMNID = PTR(SHCOLUMNID)

    DEVICE_SCALE_FACTOR = INT
    if True:
        DEVICE_SCALE_FACTOR_INVALID	= 0
        SCALE_100_PERCENT	= 100
        SCALE_120_PERCENT	= 120
        SCALE_125_PERCENT	= 125
        SCALE_140_PERCENT	= 140
        SCALE_150_PERCENT	= 150
        SCALE_160_PERCENT	= 160
        SCALE_175_PERCENT	= 175
        SCALE_180_PERCENT	= 180
        SCALE_200_PERCENT	= 200
        SCALE_225_PERCENT	= 225
        SCALE_250_PERCENT	= 250
        SCALE_300_PERCENT	= 300
        SCALE_350_PERCENT	= 350
        SCALE_400_PERCENT	= 400
        SCALE_450_PERCENT	= 450
        SCALE_500_PERCENT	= 500
