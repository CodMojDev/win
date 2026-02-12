"""++

Copyright (c) Microsoft Corporation

Module Name:

    ifmib.h

Abstract:

    This module contains the public definitions and structures for the
    non-TCP/IP specific parts of MIB-II.  These definitions were previously
    in iprtrmib.h, which now includes this file.

--"""

from . import cpreproc

from .minwindef import *

from .winnt import UCHAR

if cpreproc.pragma_once("_IFMIB_"):
    from .ifdef import *

    ANY_SIZE = 1

    class MIB_IFNUMBER(CStructure):
        _fields_ = [
            ("dwValue", DWORD)
        ]
    PMIB_IFNUMBER = POINTER(MIB_IFNUMBER)


    #
    # $REVIEW: This has always been defined as 8.  However, this is not
    # sufficient for all media types.
    #
    MAXLEN_PHYSADDR = 8

    MAXLEN_IFDESCR = 256

    MAX_INTERFACE_NAME_LEN = 256

    class MIB_IFROW(CStructure):
        _fields_ = [
            ("wszName", WCHAR * MAX_INTERFACE_NAME_LEN),
            ("dwIndex", IF_INDEX),
            ("dwType", IFTYPE),
            ("dwMtu", DWORD),
            ("dwSpeed", DWORD),
            ("dwPhysAddrLen", DWORD),
            ("bPhysAddr", UCHAR * MAXLEN_PHYSADDR),
            ("dwAdminStatus", DWORD),
            ("dwOperStatus", INTERNAL_IF_OPER_STATUS),
            ("dwLastChange", DWORD),
            ("dwInOctets", DWORD),
            ("dwInUcastPkts", DWORD),
            ("dwInNUcastPkts", DWORD),
            ("dwInDiscards", DWORD),
            ("dwInErrors", DWORD),
            ("dwInUnknownProtos", DWORD),
            ("dwOutOctets", DWORD),
            ("dwOutUcastPkts", DWORD),
            ("dwOutNUcastPkts", DWORD),
            ("dwOutDiscards", DWORD),
            ("dwOutErrors", DWORD),
            ("dwOutQLen", DWORD),
            ("dwDescrLen", DWORD),
            ("bDescr", UCHAR * MAXLEN_IFDESCR)
        ]
    PMIB_IFROW = POINTER(MIB_IFROW)

    class MIB_IFTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", MIB_IFROW * ANY_SIZE)
        ]
    PMIB_IFTABLE = POINTER(MIB_IFTABLE)

    SIZEOF_IFTABLE = lambda X: MIB_IFTABLE.table.offset + (X) * sizeof(MIB_IFROW) + MIB_IFTABLE._pack_
