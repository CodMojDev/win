"""++

Copyright (c) Microsoft Corporation

Module Name:

    udpmib.h

Abstract:

    This module contains the public definitions and structures for the
    UDP-specific parts of MIB-II.  These definitions were previously
    in iprtrmib.h, which now includes this file.

Environment:

    user mode or kernel mode

--"""

from . import cpreproc

from .minwindef import *

from .sdkddkver import *

from .winnt import UCHAR

if cpreproc.pragma_once("_UDPMIB_"):
    TCPIP_OWNING_MODULE_SIZE = 16

    class MIB_UDPROW(CStructure):
        _fields_ = [
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD)
        ]
    PMIB_UDPROW = POINTER(MIB_UDPROW)

    class MIB_UDPTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDPROW)
        ]
    PMIB_UDPTABLE = POINTER(MIB_UDPTABLE)
    SIZEOF_UDPTABLE = lambda X: MIB_UDPTABLE.table.offset + (X) * sizeof(MIB_UDPROW) + MIB_UDPTABLE._pack_
	
    class MIB_UDPROW_OWNER_PID(CStructure):
        _fields_ = [
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
			("dwOwningPid", DWORD)
        ]
    PMIB_UDPROW_OWNER_PID = POINTER(MIB_UDPROW_OWNER_PID)
	
    class MIB_UDPTABLE_OWNER_PID(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDPROW_OWNER_PID)
        ]
    PMIB_UDPTABLE_OWNER_PID = POINTER(MIB_UDPTABLE_OWNER_PID)
    SIZEOF_UDPTABLE_OWNER_PID = lambda X: MIB_UDPTABLE_OWNER_PID.table.offset + (X) * sizeof(MIB_UDPROW_OWNER_PID) + MIB_UDPTABLE_OWNER_PID._pack_

    class MIB_UDPROW_OWNER_MODULE(CStructure):
        class _DUMMYUNIONNAME(Union):
            class _DUMMYSTRUCTNAME(CStructure):
                _fields_ = [
                    ("SpecificPortBind", INT, 1)
                ]
            _fields_ = [
                ("s", _DUMMYSTRUCTNAME),
                ("dwFlags", INT)
            ]
        _fields_ = [
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
            ("dwOwningPid", DWORD),
            ("liCreateTimestamp", LARGE_INTEGER),
            ("u", _DUMMYUNIONNAME),
            ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE)
        ]
    PMIB_UDPROW_OWNER_MODULE = POINTER(MIB_UDPROW_OWNER_MODULE)

    class MIB_UDPTABLE_OWNER_MODULE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDPROW_OWNER_MODULE)
        ]
    PMIB_UDPTABLE_OWNER_MODULE = POINTER(MIB_UDPTABLE_OWNER_MODULE)
    SIZEOF_UDPTABLE_OWNER_MODULE = lambda X: MIB_UDPTABLE_OWNER_MODULE.table.offset + (X) * sizeof(MIB_UDPROW_OWNER_MODULE) + MIB_UDPTABLE_OWNER_MODULE._pack_
    
    from .in6addr import IN6_ADDR

    class MIB_UDP6ROW(CStructure):
        _fields_ = [
            ("dwLocalAddr", IN6_ADDR),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD)
        ]
    PMIB_UDP6ROW = POINTER(MIB_UDP6ROW)

    class MIB_UDP6TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDP6ROW)
        ]
    PMIB_UDP6TABLE = POINTER(MIB_UDP6TABLE)
    SIZEOF_UDP6TABLE = lambda X: MIB_UDP6TABLE.table.offset + (X) * sizeof(MIB_UDP6ROW) + MIB_UDP6TABLE._pack_

    class MIB_UDP6ROW_OWNER_PID(CStructure):
        _fields_ = [
            ("ucLocalAddr", UCHAR * 16),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("dwOwningPid", DWORD)
        ]
    PMIB_UDP6ROW_OWNER_PID = POINTER(MIB_UDP6ROW_OWNER_PID)

    class MIB_UDP6TABLE_OWNER_PID(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDP6ROW_OWNER_PID)
        ]
    PMIB_UDP6TABLE_OWNER_PID = POINTER(MIB_UDP6TABLE_OWNER_PID)
    SIZEOF_UDP6TABLE_OWNER_PID = lambda X: MIB_UDP6TABLE_OWNER_PID.table.offset + (X) * sizeof(MIB_UDP6ROW_OWNER_PID) + MIB_UDP6TABLE_OWNER_PID._pack_

    class MIB_UDP6ROW_OWNER_MODULE(CStructure):
        class _DUMMYUNIONNAME(Union):
            class _DUMMYSTRUCTNAME(CStructure):
                _fields_ = [
                    ("SpecificPortBind", INT, 1)
                ]
            _fields_ = [
                ("s", _DUMMYSTRUCTNAME),
                ("dwFlags", INT)
            ]
        _fields_ = [
            ("ucLocalAddr", UCHAR * 16),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("dwOwningPid", DWORD),
            ("liCreateTimestamp", LARGE_INTEGER),
            ("u", _DUMMYUNIONNAME),
            ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE)
        ]
    PMIB_UDP6ROW_OWNER_MODULE = POINTER(MIB_UDP6ROW_OWNER_MODULE)

    class MIB_UDP6TABLE_OWNER_MODULE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDP6ROW_OWNER_MODULE)
        ]
    PMIB_UDP6TABLE_OWNER_MODULE = POINTER(MIB_UDP6TABLE_OWNER_MODULE)
    SIZEOF_UDP6TABLE_OWNER_MODULE = lambda X: MIB_UDP6TABLE_OWNER_MODULE.table.offset + (X) * sizeof(MIB_UDP6ROW_OWNER_MODULE) + MIB_UDP6TABLE_OWNER_MODULE._pack_

    class MIB_UDPSTATS(CStructure):
        _fields_ = [
            ("dwInDatagram", DWORD),
            ("dwNoPorts", DWORD),
            ("dwInErrors", DWORD),
            ("dwOutDatagrams", DWORD),
            ("dwNumAddrs", DWORD)
        ]
    PMIB_UDPSTATS = POINTER(MIB_UDPSTATS)

    if cpreproc.getdef("_WINVER") >= WIN32_WINNT_WIN10:
        class MIB_UDPSTATS2(CStructure):
            _fields_ = [
                ("dw64InDatagram", DWORD64),
                ("dwNoPorts", DWORD),
                ("dwInErrors", DWORD),
                ("dw64OutDatagrams", DWORD64),
                ("dwNumAddrs", DWORD)
            ]
        PMIB_UDPSTATS2 = POINTER(MIB_UDPSTATS2)
