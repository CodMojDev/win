"""++

Copyright (c) Microsoft Corporation

Module Name:

    tcpmib.h

Abstract:

    This module contains the public definitions and structures for the
    TCP-specific parts of MIB-II.  These definitions were previously
    in iprtrmib.h, which now includes this file.

Environment:

    user mode or kernel mode

--"""

from . import cpreproc

from .sdkddkver import *

from .minwindef import *

from .winnt import UCHAR

if cpreproc.pragma_once("_TCPMIB_"):
    TCPIP_OWNING_MODULE_SIZE = 16

    #
    # TCP states, as defined in the MIB.
    #
    MIB_TCP_STATE = INT
    if True:
        MIB_TCP_STATE_CLOSED     =  1
        MIB_TCP_STATE_LISTEN     =  2
        MIB_TCP_STATE_SYN_SENT   =  3
        MIB_TCP_STATE_SYN_RCVD   =  4
        MIB_TCP_STATE_ESTAB      =  5
        MIB_TCP_STATE_FIN_WAIT1  =  6
        MIB_TCP_STATE_FIN_WAIT2  =  7
        MIB_TCP_STATE_CLOSE_WAIT =  8
        MIB_TCP_STATE_CLOSING    =  9
        MIB_TCP_STATE_LAST_ACK   = 10
        MIB_TCP_STATE_TIME_WAIT  = 11
        MIB_TCP_STATE_DELETE_TCB = 12
        #
        # Extra TCP states not defined in the MIB
        #
        MIB_TCP_STATE_RESERVED      = 100

    #
    # Various Offload states a TCP connection can be in.
    #
    TCP_CONNECTION_OFFLOAD_STATE = INT
    if True:
        TcpConnectionOffloadStateInHost = 0
        TcpConnectionOffloadStateOffloading = 1
        TcpConnectionOffloadStateOffloaded = 2
        TcpConnectionOffloadStateUploading = 3
        TcpConnectionOffloadStateMax = 4
    PTCP_CONNECTION_OFFLOAD_STATE = POINTER(TCP_CONNECTION_OFFLOAD_STATE)

    class MIB_TCPROW_LH(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("dwState", DWORD), # Old field used DWORD type.
                ("State", MIB_TCP_STATE) # New field uses enum type.
            ]
        _fields_ = [
                ("u", _DUMMYUNIONNAME),
                ("dwLocalAddr", DWORD),
                ("dwLocalPort", DWORD),
                ("dwRemoteAddr", DWORD),
                ("dwRemotePort", DWORD)
        ]
    PMIB_TCPROW_LH = POINTER(MIB_TCPROW_LH)

    class MIB_TCPROW_W2K(CStructure):
        _fields_ = [
            ("dwState", DWORD),
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
            ("dwRemoteAddr", DWORD),
            ("dwRemotePort", DWORD)
        ]
    PMIB_TCPROW_W2K = POINTER(MIB_TCPROW_W2K)

    _version = cpreproc.getdef("_WINVER")
    if _version >= WIN32_WINNT_VISTA:
        MIB_TCPROW = MIB_TCPROW_LH
        PMIB_TCPROW = PMIB_TCPROW_LH
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_TCPROW = MIB_TCPROW_W2K
        PMIB_TCPROW = PMIB_TCPROW_W2K
    else:
        MIB_TCPROW = MIB_TCPROW_LH
        PMIB_TCPROW = PMIB_TCPROW_LH

    class MIB_TCPTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCPROW)
        ]
    PMIB_TCPTABLE = POINTER(MIB_TCPTABLE)

    SIZEOF_TCPTABLE = lambda X: MIB_TCPTABLE.table.offset + (X) * sizeof(MIB_TCPROW) + MIB_TCPTABLE._pack_

    class MIB_TCPROW2(CStructure):
        _fields_ = [
            ("dwState", DWORD),
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
            ("dwRemoteAddr", DWORD),
            ("dwRemotePort", DWORD),
            ("dwOwningPid", DWORD),
            ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE)
        ]
    PMIB_TCPROW2 = POINTER(MIB_TCPROW2)

    class MIB_TCPTABLE2(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCPROW2)
        ]
    PMIB_TCPTABLE2 = POINTER(MIB_TCPTABLE2)

    SIZEOF_TCPTABLE2 = lambda X: MIB_TCPTABLE2.table.offset + (X) * sizeof(MIB_TCPROW2) + MIB_TCPTABLE2._pack_

    class MIB_TCPROW_OWNER_PID(CStructure):
        _fields_ = [
            ("dwState", DWORD),
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
            ("dwRemoteAddr", DWORD),
            ("dwRemotePort", DWORD),
            ("dwOwningPid", DWORD),
            ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE)
        ]
    PMIB_TCPROW_OWNER_PID = POINTER(MIB_TCPROW2)

    class MIB_TCPTABLE_OWNER_PID(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCPROW_OWNER_PID)
        ]
    PMIB_TCPTABLE_OWNER_PID = POINTER(MIB_TCPTABLE_OWNER_PID)

    SIZEOF_TCPTABLE_OWNER_PID = lambda X: MIB_TCPTABLE_OWNER_PID.table.offset + (X) * sizeof(MIB_TCPROW_OWNER_PID) + MIB_TCPTABLE_OWNER_PID._pack_

    class MIB_TCPROW_OWNER_MODULE(CStructure):
        _fields_ = [
            ("dwState", DWORD),
            ("dwLocalAddr", DWORD),
            ("dwLocalPort", DWORD),
            ("dwRemoteAddr", DWORD),
            ("dwRemotePort", DWORD),
            ("dwOwningPid", DWORD),
            ("liCreateTimestamp", LARGE_INTEGER),
            ("OwningModuleInfo", ULONGLONG * TCPIP_OWNING_MODULE_SIZE)
        ]
    PMIB_TCPROW_OWNER_MODULE = POINTER(MIB_TCPROW_OWNER_MODULE)

    class MIB_TCPTABLE_OWNER_MODULE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCPROW_OWNER_MODULE)
        ]
    PMIB_TCPTABLE_OWNER_MODULE = POINTER(MIB_TCPTABLE_OWNER_MODULE)

    SIZEOF_TCPTABLE_OWNER_MODULE = lambda X: MIB_TCPTABLE_OWNER_MODULE.table.offset + (X) * sizeof(MIB_TCPROW_OWNER_MODULE) + MIB_TCPTABLE_OWNER_MODULE._pack_

    from .in6addr import IN6_ADDR

    class MIB_TCP6ROW(CStructure):
        _fields_ = [
            ("State", MIB_TCP_STATE),
            ("LocalAddr", IN6_ADDR),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("RemoteAddr", IN6_ADDR),
            ("dwRemoteScopeId", DWORD),
            ("dwRemotePort", DWORD)
        ]
    PMIB_TCP6ROW = POINTER(MIB_TCP6ROW)

    class MIB_TCP6TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCP6ROW)
        ]
    PMIB_TCP6TABLE = POINTER(MIB_TCP6TABLE)

    SIZEOF_TCP6TABLE = lambda X: MIB_TCP6TABLE.table.offset + (X) * sizeof(MIB_TCP6ROW) + MIB_TCP6TABLE._pack_

    class MIB_TCP6ROW2(CStructure):
        _fields_ = [
            ("LocalAddr", IN6_ADDR),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("RemoteAddr", IN6_ADDR),
            ("dwRemoteScopeId", DWORD),
            ("dwRemotePort", DWORD),
            ("State", MIB_TCP_STATE),
            ("dwOwningPid", DWORD),
            ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE)
        ]
    PMIB_TCP6ROW2 = POINTER(MIB_TCP6ROW2)

    class MIB_TCP6TABLE2(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCP6ROW2)
        ]
    PMIB_TCP6TABLE2 = POINTER(MIB_TCP6TABLE2)

    SIZEOF_TCP6TABLE2 = lambda X: MIB_TCP6TABLE2.table.offset + (X) * sizeof(MIB_TCP6ROW2) + MIB_TCP6TABLE2._pack_

    class MIB_TCP6ROW_OWNER_PID(CStructure):
        _fields_ = [
            ("ucLocalAddr", UCHAR * 16),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("ucRemoteAddr", UCHAR * 16),
            ("dwRemoteScopeId", DWORD),
            ("dwRemotePort", DWORD),
            ("dwState", DWORD),
            ("dwOwningPid", DWORD)
        ]
    PMIB_TCP6ROW_OWNER_PID = POINTER(MIB_TCP6ROW_OWNER_PID)

    class MIB_TCP6TABLE_OWNER_PID(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCP6ROW_OWNER_PID)
        ]
    PMIB_TCP6TABLE_OWNER_PID = POINTER(MIB_TCP6TABLE_OWNER_PID)

    SIZEOF_TCP6TABLE_OWNER_PID = lambda X: MIB_TCP6TABLE_OWNER_PID.table.offset + (X) * sizeof(MIB_TCP6ROW_OWNER_PID) + MIB_TCPTABLE_OWNER_PID._pack_

    class MIB_TCP6ROW_OWNER_MODULE(CStructure):
        _fields_ = [
            ("ucLocalAddr", UCHAR * 16),
            ("dwLocalScopeId", DWORD),
            ("dwLocalPort", DWORD),
            ("ucRemoteAddr", UCHAR * 16),
            ("dwRemoteScopeId", DWORD),
            ("dwRemotePort", DWORD),
            ("dwState", DWORD),
            ("dwOwningPid", DWORD),
            ("liCreateTimestamp", LARGE_INTEGER),
            ("OwningModuleInfp", ULONGLONG * TCPIP_OWNING_MODULE_SIZE)
        ]
    PMIB_TCP6ROW_OWNER_MODULE = POINTER(MIB_TCP6ROW_OWNER_MODULE)

    class MIB_TCP6TABLE_OWNER_MODULE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_TCPROW)
        ]
    PMIB_TCP6TABLE_OWNER_MODULE = POINTER(MIB_TCP6TABLE_OWNER_MODULE)

    SIZEOF_TCP6TABLE_OWNER_MODULE = lambda X: MIB_TCP6TABLE_OWNER_MODULE.table.offset + (X) * sizeof(MIB_TCP6ROW_OWNER_MODULE) + MIB_TCP6TABLE_OWNER_MODULE._pack_

    MIB_TCP_MAXCONN_DYNAMIC = ULONG(-1).value

    #
    # The algorithm used to determine the timeout value used for retransmitting
    # unacknowledged octets.
    #
    TCP_RTO_ALGORITHM = INT
    if True:
        TcpRtoAlgorithmOther  = 1
        TcpRtoAlgorithmConstant = 2
        TcpRtoAlgorithmRsre = 3
        TcpRtoAlgorithmVanj = 4

        MIB_TCP_RTO_OTHER     = 1
        MIB_TCP_RTO_CONSTANT  = 2
        MIB_TCP_RTO_RSRE      = 3
        MIB_TCP_RTO_VANJ      = 4
    PTCP_RTO_ALGORITHM = POINTER(TCP_RTO_ALGORITHM)

    class MIB_TCPSTATS_LH(CStructure):
        class _DUMMYUNIONNAME(Union):
            _fields_ = [
                ("dwRtoAlgorithm", DWORD),
                ("RtoAlgorithm", TCP_RTO_ALGORITHM)
            ]
        _fields_ = [
            ("u", _DUMMYUNIONNAME),
            ("dwRtoMin", DWORD),
            ("dwRtoMax", DWORD),
            ("dwMaxConn", DWORD),
            ("dwActiveOpens", DWORD),
            ("dwPassiveOpens", DWORD),
            ("dwAttemptFails", DWORD),
            ("dwEstabResets", DWORD),
            ("dwCurrEstab", DWORD),
            ("dwInSegs", DWORD),
            ("dwOutSegs", DWORD),
            ("dwRetransSegs", DWORD),
            ("dwInErrs", DWORD),
            ("dwOutRsts", DWORD),
            ("dwNumConns", DWORD)
        ]
    PMIB_TCPSTATS_LH = POINTER(MIB_TCPSTATS_LH)

    class MIB_TCPSTATS_W2K(CStructure):
        _fields_ = [
            ("dwRtoAlgorithm", DWORD),
            ("dwRtoMin", DWORD),
            ("dwRtoMax", DWORD),
            ("dwMaxConn", DWORD),
            ("dwActiveOpens", DWORD),
            ("dwPassiveOpens", DWORD),
            ("dwAttemptFails", DWORD),
            ("dwEstabResets", DWORD),
            ("dwCurrEstab", DWORD),
            ("dwInSegs", DWORD),
            ("dwOutSegs", DWORD),
            ("dwRetransSegs", DWORD),
            ("dwInErrs", DWORD),
            ("dwOutRsts", DWORD),
            ("dwNumConns", DWORD)
        ]
    PMIB_TCPSTATS_W2K = POINTER(MIB_TCPSTATS_W2K)

    if _version >= WIN32_WINNT_VISTA:
        MIB_TCPSTATS = MIB_TCPSTATS_LH
        PMIB_TCPSTATS = PMIB_TCPSTATS_LH
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_TCPSTATS = MIB_TCPSTATS_W2K
        PMIB_TCPSTATS = PMIB_TCPSTATS_W2K

    if _version >= WIN32_WINNT_WIN10:
        class MIB_TCPSTATS2(CStructure):
            _fields_ = [
                ("RtoAlgorithm", TCP_RTO_ALGORITHM),
                ("dwRtoMin", DWORD),
                ("dwRtoMax", DWORD),
                ("dwMaxConn", DWORD),
                ("dwActiveOpens", DWORD),
                ("dwPassiveOpens", DWORD),
                ("dwAttemptFails", DWORD),
                ("dwEstabResets", DWORD),
                ("dwCurrEstab", DWORD),
                ("dw64InSegs", DWORD64),
                ("dw64OutSegs", DWORD64),
                ("dwRetransSegs", DWORD),
                ("dwInErrs", DWORD),
                ("dwOutRsts", DWORD),
                ("dwNumConns", DWORD)
            ]
        PMIB_TCPSTATS2 = POINTER(MIB_TCPSTATS2)