"""++

Copyright (c) Microsoft Corporation

Module Name:

    ipmib.h

Abstract:

    This module contains the public definitions and structures for the
    IP-specific parts of MIB-II.  These definitions were previously
    in iprtrmib.h, which now includes this file.

--"""

from . import cpreproc

from .minwindef import *

from .sdkddkver import *

if cpreproc.pragma_once("_IPMIB_"):
    #
    # Pick up definitions of MAXLEN_PHYSADDR, etc.
    #
    from .ifmib import *
    from .nldef import *

    MIB_IPADDR_PRIMARY = 0x0001 # Primary ipaddr
    MIB_IPADDR_DYNAMIC = 0x0004 # Dynamic ipaddr
    MIB_IPADDR_DISCONNECTED = 0x0008 # Address is on disconnected interface
    MIB_IPADDR_DELETED = 0x0040 # Address being deleted
    MIB_IPADDR_TRANSIENT = 0x0080 # Transient address
    MIB_IPADDR_DNS_ELIGIBLE = 0X0100 # Address is published in DNS.

    class MIB_IPADDRROW_XP(CStructure):
        _fields_ = [
            ("dwAddr", DWORD),
            ("dwIndex", IF_INDEX),
            ("dwMask", DWORD),
            ("dwBCastAddr", DWORD),
            ("dwReasmSize", DWORD),
            ("unused1", USHORT),
            ("wType", USHORT)
        ]
    PMIB_IPADDRROW_XP = POINTER(MIB_IPADDRROW_XP)

    class MIB_IPADDRROW_W2K(CStructure):
        _fields_ = [
            ("dwAddr", DWORD),
            ("dwIndex", DWORD),
            ("dwMask", DWORD),
            ("dwBCastAddr", DWORD),
            ("dwReasmSize", DWORD),
            ("unused1", USHORT),
            ("unused2", USHORT)
        ]
    PMIB_IPADDRROW_W2K = POINTER(MIB_IPADDRROW_W2K)

    _version = cpreproc.get_version()
    if _version >= WIN32_WINNT_WINXP:
        MIB_IPADDRROW = MIB_IPADDRROW_XP
        PMIB_IPADDRROW = PMIB_IPADDRROW_XP
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_IPADDRROW = MIB_IPADDRROW_W2K
        PMIB_IPADDROW = PMIB_IPADDRROW_W2K
    else:
        MIB_IPADDRROW = MIB_IPADDRROW_XP
        PMIB_IPADDRROW = PMIB_IPADDRROW_XP  

    from .udpmib import PMIB_UDPROW, MIB_UDPROW

    class MIB_UDPTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_UDPROW)
        ]
    PMIB_UDPTABLE = POINTER(MIB_UDPTABLE)
    SIZEOF_UDPTABLE = lambda X: MIB_UDPTABLE.table.offset + (X) * sizeof(MIB_UDPROW) + MIB_UDPTABLE._pack_

    class MIB_IPADDRTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPADDROW)
        ]
    PMIB_IPADDRTABLE = POINTER(MIB_IPADDRTABLE)

    SIZEOF_IPADDRTABLE = lambda X: (MIB_IPADDRTABLE.table.offset) + \
                                ((X) * sizeof(MIB_IPADDRROW)) + MIB_IPADDRTABLE._pack_

    class MIB_IPFORWARDNUMBER(CStructure):
        _fields_ = [
            ("dwValue", DWORD)
        ]
    PMIB_IPFORWARDNUMBER = POINTER(MIB_IPFORWARDNUMBER)

    MIB_IPFORWARD_PROTO = NL_ROUTE_PROTOCOL;

    MIB_IPFORWARD_TYPE = INT
    if True:
        MIB_IPROUTE_TYPE_OTHER    = 1
        MIB_IPROUTE_TYPE_INVALID  = 2
        MIB_IPROUTE_TYPE_DIRECT   = 3
        MIB_IPROUTE_TYPE_INDIRECT = 4

    class MIB_IPFORWARDROW(CStructure):
        _fields_ = [
            ("dwForwardDest", DWORD),
            ("dwForwardMask", DWORD),
            ("dwForwardPolicy", DWORD),
            ("dwForwardNextHop", DWORD),
            ("dwForwardIfIndex", IF_INDEX),
            ("ForwardType", MIB_IPFORWARD_TYPE),
            ("ForwardProto", MIB_IPFORWARD_PROTO),
            ("dwForwardAge", DWORD),
            ("dwForwardNextHopAS", DWORD),
            ("dwForwardMetric1", DWORD),
            ("dwForwardMetric2", DWORD),
            ("dwForwardMetric3", DWORD),
            ("dwForwardMetric4", DWORD),
            ("dwForwardMetric5", DWORD)
        ]
    PMIB_IPFORWARDROW = POINTER(MIB_IPFORWARDROW)

    MIB_IPROUTE_TYPE_OTHER    = 1
    MIB_IPROUTE_TYPE_INVALID  = 2
    MIB_IPROUTE_TYPE_DIRECT   = 3
    MIB_IPROUTE_TYPE_INDIRECT = 4

    MIB_IPROUTE_METRIC_UNUSED = DWORD(-1).value


    class MIB_IPFORWARDTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPFORWARDROW)
        ]
    PMIB_IPFORWARDTABLE = POINTER(MIB_IPFORWARDTABLE)

    SIZEOF_IPFORWARDTABLE = lambda X: \
                (MIB_IPFORWARDTABLE.table.offset) + \
                ((X) * sizeof(MIB_IPFORWARDROW)) + MIB_IPFORWARDTABLE._pack_

    MIB_IPNET_TYPE = INT
    if True:
        MIB_IPNET_TYPE_OTHER   = 1
        MIB_IPNET_TYPE_INVALID = 2
        MIB_IPNET_TYPE_DYNAMIC = 3
        MIB_IPNET_TYPE_STATIC  = 4

    class MIB_IPNETROW_LH(CStructure):
        _fields_ = [
            ("dwIndex", IF_INDEX),
            ("dwPhysAddrLen", DWORD),
            ("bPhysAddr", UCHAR * MAXLEN_PHYSADDR),
            ("dwAddr", DWORD),
            ("Type", MIB_IPNET_TYPE)
        ]
    PMIB_IPNETROW_LH = POINTER(MIB_IPNETROW_LH)

    class MIB_IPNETROW_W2K(CStructure):
        _fields_ = [
            ("dwIndex", IF_INDEX),
            ("dwPhysAddrLen", DWORD),
            ("bPhysAddr", UCHAR * MAXLEN_PHYSADDR),
            ("dwAddr", DWORD),
            ("dwType", DWORD)
        ]
    PMIB_IPNETROW_W2K = POINTER(MIB_IPNETROW_W2K)
    
    _version = cpreproc.get_version()
    if _version >= WIN32_WINNT_VISTA:
        MIB_IPNETROW = MIB_IPNETROW_LH
        PMIB_IPNETROW = PMIB_IPNETROW_LH
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_IPNETROW = MIB_IPNETROW_W2K
        PMIB_IPNETROW = PMIB_IPNETROW_W2K
    else:
        MIB_IPNETROW = MIB_IPNETROW_LH
        PMIB_IPNETROW = PMIB_IPNETROW_LH

    class MIB_IPNETTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPNETROW)
        ]
    PMIB_IPNETTABLE = POINTER(MIB_IPNETTABLE)

    SIZEOF_IPNETTABLE = lambda X: (MIB_IPNETTABLE.table.offset) + \
                                ((X) * sizeof(MIB_IPNETROW)) + MIB_IPNETTABLE._pack_

    MIB_IPSTATS_FORWARDING = INT
    if True:
        MIB_IP_FORWARDING     = 1,
        MIB_IP_NOT_FORWARDING = 2,
    PMIB_IPSTATS_FORWARDING = POINTER(MIB_IPSTATS_FORWARDING)

    MIB_USE_CURRENT_TTL         = DWORD(-1).value
    MIB_USE_CURRENT_FORWARDING  = DWORD(-1).value

    class MIB_IPSTATS_LH(CStructure):
        _fields_ = [
            ("Forwarding", MIB_IPSTATS_FORWARDING),
            ("dwDefaultTTL", DWORD),
            ("dwInReceives", DWORD),
            ("dwInHdrErrors", DWORD),
            ("dwInAddrErrors", DWORD),
            ("dwForwDatagrams", DWORD),
            ("dwInUnknownProtos", DWORD),
            ("dwInDiscards", DWORD),
            ("dwInDelivers", DWORD),
            ("dwOutRequests", DWORD),
            ("dwRoutingDiscards", DWORD),
            ("dwOutDiscards", DWORD),
            ("dwOutNoRoutes", DWORD),
            ("dwReasmTimeout", DWORD),
            ("dwReasmReqds", DWORD),
            ("dwReasmOks", DWORD),
            ("dwReasmFails", DWORD),
            ("dwFragOks", DWORD),
            ("dwFragFails", DWORD),
            ("dwFragCreates", DWORD),
            ("dwNumIf", DWORD),
            ("dwNumAddr", DWORD),
            ("dwNumRoutes", DWORD)
        ]
    PMIB_IPSTATS_LH = POINTER(MIB_IPSTATS_LH)
    
    class MIB_IPSTATS_W2K(CStructure):
        _fields_ = [
            ("dwForwarding", DWORD),
            ("dwDefaultTTL", DWORD),
            ("dwInReceives", DWORD),
            ("dwInHdrErrors", DWORD),
            ("dwInAddrErrors", DWORD),
            ("dwForwDatagrams", DWORD),
            ("dwInUnknownProtos", DWORD),
            ("dwInDiscards", DWORD),
            ("dwInDelivers", DWORD),
            ("dwOutRequests", DWORD),
            ("dwRoutingDiscards", DWORD),
            ("dwOutDiscards", DWORD),
            ("dwOutNoRoutes", DWORD),
            ("dwReasmTimeout", DWORD),
            ("dwReasmReqds", DWORD),
            ("dwReasmOks", DWORD),
            ("dwReasmFails", DWORD),
            ("dwFragOks", DWORD),
            ("dwFragFails", DWORD),
            ("dwFragCreates", DWORD),
            ("dwNumIf", DWORD),
            ("dwNumAddr", DWORD),
            ("dwNumRoutes", DWORD)
        ]
    PMIB_IPSTATS_W2K = POINTER(MIB_IPSTATS_W2K)
    
    if _version >= WIN32_WINNT_VISTA:
        MIB_IPSTATS = MIB_IPSTATS_LH
        PMIB_IPSTATS = PMIB_IPSTATS_LH
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_IPSTATS = MIB_IPSTATS_W2K
        PMIB_IPSTATS = PMIB_IPSTATS_W2K

    class MIBICMPSTATS(CStructure):
        ("dwMsgs", DWORD),
        ("dwErrors", DWORD),
        ("dwDestUnreachs", DWORD),
        ("dwTimeExcds", DWORD),
        ("dwParmProbs", DWORD),
        ("dwSrcQuenchs", DWORD),
        ("dwRedirects", DWORD),
        ("dwEchos", DWORD),
        ("dwEchoReps", DWORD),
        ("dwTimestamps", DWORD),
        ("dwTimestampReps", DWORD),
        ("dwAddrMasks", DWORD),
        ("dwAddrMaskReps", DWORD)
    PMIBICMPSTATS = POINTER(MIBICMPSTATS)

    class MIBICMPINFO(CStructure):
        _fields_ = [
            ("icmpInStats", MIBICMPSTATS),
            ("icmpOutStats", MIBICMPSTATS)
        ]

    class MIB_ICMP(CStructure):
        _fields_ = [
            ("stats", MIBICMPINFO)
        ]
    PMIB_ICMP = POINTER(MIB_ICMP)

    class MIBICMPSTATS_EX_XPSP1(CStructure):
        _fields_ = [
            ("dwMsgs", DWORD),
            ("dwErrors", DWORD),
            ("rgdwTypeCount", DWORD * 256)
        ]
    PMIBICMPSTATS_EX_XPSP1 = POINTER(MIBICMPSTATS_EX_XPSP1)
    
    MIBICMPSTATS_EX = MIBICMPSTATS_EX_XPSP1
    PMIBICMPSTATS_EX = PMIBICMPSTATS_EX_XPSP1

    class MIB_ICMP_EX_XPSP1(CStructure):
        _fields_ = [
            ("icmpInStats", MIBICMPSTATS_EX),
            ("icmpOutStats", MIBICMPSTATS_EX)
        ]
    PMIB_ICMP_EX_XPSP1 = POINTER(MIB_ICMP_EX_XPSP1)

    MIB_ICMP_EX = MIB_ICMP_EX_XPSP1
    PMIB_ICMP_EX = PMIB_ICMP_EX_XPSP1

    #
    # ICMP6_TYPE
    #
    # ICMPv6 Type Values from RFC 2292, 2461 (ND), and 3810 (MLDv2)
    #
    ICMP6_TYPE = INT
    if True:
        ICMP6_DST_UNREACH          =   1
        ICMP6_PACKET_TOO_BIG       =   2
        ICMP6_TIME_EXCEEDED        =   3
        ICMP6_PARAM_PROB           =   4
        ICMP6_ECHO_REQUEST         = 128
        ICMP6_ECHO_REPLY           = 129
        ICMP6_MEMBERSHIP_QUERY     = 130
        ICMP6_MEMBERSHIP_REPORT    = 131
        ICMP6_MEMBERSHIP_REDUCTION = 132
        ND_ROUTER_SOLICIT          = 133
        ND_ROUTER_ADVERT           = 134
        ND_NEIGHBOR_SOLICIT        = 135
        ND_NEIGHBOR_ADVERT         = 136
        ND_REDIRECT                = 137
        ICMP6_V2_MEMBERSHIP_REPORT = 143
    PICMP6_TYPE = POINTER(ICMP6_TYPE)


    #
    # Used to identify informational/error messages.
    #
    #define ICMP6_INFOMSG_MASK 0x80
    #define ICMP6_ISTYPEINFORMATIONAL(Type) (((Type) & ICMP6_INFOMSG_MASK) != 0)
    #define ICMP6_ISTYPEERROR(Type) (!ICMP6_ISTYPEINFORMATIONAL(Type))

    #
    # ICMP4_TYPE
    #
    # There are no RFC-specified defines for ICMPv4 message types, so we try to
    # use the ICMP6 values from RFC 2292 modified to be prefixed with ICMP4.
    #
    ICMP4_TYPE = INT
    if True:
        ICMP4_ECHO_REPLY        =  0 # Echo Reply.
        ICMP4_DST_UNREACH       =  3 # Destination Unreachable.
        ICMP4_SOURCE_QUENCH     =  4 # Source Quench.
        ICMP4_REDIRECT          =  5 # Redirect.
        ICMP4_ECHO_REQUEST      =  8 # Echo Request.
        ICMP4_ROUTER_ADVERT     =  9 # Router Advertisement.
        ICMP4_ROUTER_SOLICIT    = 10 # Router Solicitation.
        ICMP4_TIME_EXCEEDED     = 11 # Time Exceeded.
        ICMP4_PARAM_PROB        = 12 # Parameter Problem.
        ICMP4_TIMESTAMP_REQUEST = 13 # Timestamp Request.
        ICMP4_TIMESTAMP_REPLY   = 14 # Timestamp Reply.
        ICMP4_MASK_REQUEST      = 17 # Address Mask Request.
        ICMP4_MASK_REPLY        = 18 # Address Mask Reply.
    PICMP4_TYPE = POINTER(ICMP4_TYPE)

    #
    # See RFC 1812, section 4.3.1.
    #
    ICMP4_ISTYPEERROR = lambda Type: \
        (((Type) == ICMP4_DST_UNREACH) or \
        ((Type) == ICMP4_SOURCE_QUENCH) or \
        ((Type) == ICMP4_REDIRECT) or \
        ((Type) == ICMP4_PARAM_PROB) or \
        ((Type) == ICMP4_TIME_EXCEEDED)) \

    class MIB_IPMCAST_OIF_XP(CStructure):
        _fields_ = [
            ("dwOutIfIndex", DWORD),
            ("dwNextHopAddr", DWORD),
            ("dwReserved", DWORD),
            ("dwReserved1", DWORD)
        ]
    PMIB_IPMCAST_OIF_XP = POINTER(MIB_IPMCAST_OIF_XP)

    class MIB_IPMCAST_OIF_W2K(CStructure):
        _fields_ = [
            ("dwOutIfIndex", DWORD),
            ("dwNextHopAddr", DWORD),
            ("pvReserved", PVOID),
            ("dwReserved", DWORD)
        ]
    PMIB_IPMCAST_OIF_W2K = POINTER(MIB_IPMCAST_OIF_W2K)

    if _version >= WIN32_WINNT_WINXP:
        MIB_IPMCAST_OIF = MIB_IPMCAST_OIF_XP
        PMIB_IPMCAST_OIF = PMIB_IPMCAST_OIF_XP
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_IPMCAST_OIF = MIB_IPMCAST_OIF_W2K
        PMIB_IPMCAST_OIF = PMIB_IPMCAST_OIF_W2K
    else:
        MIB_IPMCAST_OIF = MIB_IPMCAST_OIF_XP
        PMIB_IPMCAST_OIF = PMIB_IPMCAST_OIF_XP

    class MIB_IPMCAST_MFE(CStructure):
        _fields_ = [
            ("dwGroup", DWORD),
            ("dwSource", DWORD),
            ("dwSrcMask", DWORD),
            ("dwUpStrmNgbr", DWORD),
            ("dwInIfIndex", DWORD),
            ("dwInIfProtocol", DWORD),
            ("dwRouteProtocol", DWORD),
            ("dwRouteNetwork", DWORD),
            ("dwRouteMask", DWORD),
            ("ulUpTime", ULONG),
            ("ulExpiryTime", ULONG),
            ("ulTimeOut", ULONG),
            ("ulNumOutIf", ULONG),
            ("fFlags", DWORD),
            ("dwReserved", DWORD),
            ("rgmioOutInfo", PMIB_IPMCAST_OIF)
        ]
    PMIB_IPMCAST_MFE = POINTER(MIB_IPMCAST_MFE)

    class MIB_MFE_TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPMCAST_MFE)
        ]
    PMIB_MFE_TABLE = POINTER(MIB_MFE_TABLE)

    SIZEOF_BASIC_MIB_MFE         = \
        (MIB_IPMCAST_MFE.offset)

    SIZEOF_MIB_MFE = lambda X:             \
        (SIZEOF_BASIC_MIB_MFE + ((X) * sizeof(MIB_IPMCAST_OIF)))


    class MIB_IPMCAST_OIF_STATS_LH(CStructure):
        _fields_ = [
            ("dwOutIfIndex", DWORD),
            ("dwNextHopAddr", DWORD),
            ("dwDialContext", DWORD),
            ("ulTtlTooLow", ULONG),
            ("ulFragNeeded", ULONG),
            ("ulOutPackets", ULONG),
            ("ulOutDiscards", ULONG)
        ]
    PMIB_IPMCAST_OIF_STATS_LH = POINTER(MIB_IPMCAST_OIF_STATS_LH)

    class MIB_IPMCAST_OIF_STATS_W2K(CStructure):
        _fields_ = [
            ("dwOutIfIndex", DWORD),
            ("dwNextHopAddr", DWORD),
            ("pvDialContext", PVOID),
            ("ulTtlTooLow", ULONG),
            ("ulFragNeeded", ULONG),
            ("ulOutPackets", ULONG),
            ("ulOutDiscards", ULONG)
        ]
    PMIB_IPMCAST_OIF_STATS_W2K = POINTER(MIB_IPMCAST_OIF_STATS_W2K)
    
    if _version >= WIN32_WINNT_VISTA:
        MIB_IPMCAST_OIF_STATS = MIB_IPMCAST_OIF_STATS_LH
        PMIB_IPMCAST_OIF_STATS = PMIB_IPMCAST_OIF_STATS_LH
    elif _version >= WIN32_WINNT_WIN2K:
        MIB_IPMCAST_OIF_STATS = MIB_IPMCAST_OIF_STATS_W2K
        PMIB_IPMCAST_OIF = PMIB_IPMCAST_OIF_W2K
    else:
        MIB_IPMCAST_OIF_STATS = MIB_IPMCAST_OIF_STATS_LH
        PMIB_IPMCAST_OIF_STATS = PMIB_IPMCAST_OIF_STATS_LH

    class MIB_IPMCAST_MFE_STATS(CStructure):
        _fields_ = [
            ("dwGroup", DWORD),
            ("dwSource", DWORD),
            ("dwSrcMask", DWORD),
            ("dwUpStrmNgbr", DWORD),
            ("dwInIfIndex", DWORD),
            ("dwInIfProtocol", DWORD),
            ("dwRouteProtocol", DWORD),
            ("dwRouteNetwork", DWORD),
            ("dwRouteMask", DWORD),
            ("ulUpTime", ULONG),
            ("ulExpiryTime", ULONG),
            ("ulNumOutIf", ULONG),
            ("ulInPkts", ULONG),
            ("ulInOctets", ULONG),
            ("ulPktsDifferentIf", ULONG),
            ("ulQueueOverflow", ULONG),
            ("rgmiosOutStats", PMIB_IPMCAST_OIF_STATS)
        ]
    PMIB_IPMCAST_MFE_STATS = POINTER(MIB_IPMCAST_MFE_STATS)

    class MIB_MFE_STATS_TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPMCAST_MFE_STATS)
        ]
    PMIB_MFE_STATS_TABLE = POINTER(MIB_MFE_STATS_TABLE)

    SIZEOF_BASIC_MIB_MFE_STATS   = \
        (MIB_IPMCAST_MFE_STATS.rgmiosOutStats.offset)

    SIZEOF_MIB_MFE_STATS = lambda X:      \
        (SIZEOF_BASIC_MIB_MFE_STATS + ((X) * sizeof(MIB_IPMCAST_OIF_STATS)))

    class MIB_IPMCAST_MFE_STATS_EX_XP(CStructure):
        _fields_ = [
            ("dwGroup", DWORD),
            ("dwSource", DWORD),
            ("dwSrcMask", DWORD),
            ("dwUpStrmNgbr", DWORD),
            ("dwInIfIndex", DWORD),
            ("dwInIfProtocol", DWORD),
            ("dwRouteProtocol", DWORD),
            ("dwRouteNetwork", DWORD),
            ("dwRouteMask", DWORD),
            ("ulUpTime", ULONG),
            ("ulExpiryTime", ULONG),
            ("ulNumOutIf", ULONG),
            ("ulInPkts", ULONG),
            ("ulInOctets", ULONG),
            ("ulPktsDifferentIf", ULONG),
            ("ulQueueOverflow", ULONG),
            ("ulUninitMfe", ULONG),
            ("ulNegativeMfe", ULONG),
            ("ulInDiscards", ULONG),
            ("ulInHdrErrors", ULONG),
            ("ulTotalOutPackets", ULONG),
            ("rgmiosOutStats", PMIB_IPMCAST_OIF_STATS)
        ]
    PMIB_IPMCAST_MFE_STATS_EX_XP = POINTER(MIB_IPMCAST_MFE_STATS_EX_XP)
    
    if _version >= WIN32_WINNT_WINXP:
        MIB_IPMCAST_MFE_STATS_EX = MIB_IPMCAST_MFE_STATS_EX_XP
        PMIB_IPMCAST_MFE_STATS_EX = PMIB_IPMCAST_MFE_STATS_EX_XP

    class MIB_MFE_STATS_TABLE_EX_XP(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPMCAST_MFE_STATS_EX_XP)
        ]
    PMIB_MFE_STATS_TABLE_EX_XP = POINTER(MIB_MFE_STATS_TABLE_EX_XP)
    
    if _version >= WIN32_WINNT_WINXP:
        MIB_MFE_STATS_TABLE_EX = MIB_MFE_STATS_TABLE_EX_XP
        PMIB_MFE_STATS_TABLE_EX = PMIB_MFE_STATS_TABLE_EX_XP

        SIZEOF_BASIC_MIB_MFE_STATS_EX   = \
            (MIB_IPMCAST_MFE_STATS_EX.rgmiosOutStats.offset)

        SIZEOF_MIB_MFE_STATS_EX = lambda X:       \
            (SIZEOF_BASIC_MIB_MFE_STATS_EX + ((X) * sizeof(MIB_IPMCAST_OIF_STATS)))

    class MIB_IPMCAST_GLOBAL(CStructure):
        _fields_ = [
            ("dwEnable", DWORD)
        ]
    PMIB_IPMCAST_GLOBAL = POINTER(MIB_IPMCAST_GLOBAL)

    class MIB_IPMCAST_IF_ENTRY(CStructure):
        _fields_ = [
            ("dwIfIndex", DWORD),
            ("dwTtl", DWORD),
            ("dwProtocol", DWORD),
            ("dwRateLimit", DWORD),
            ("ulInMcastOctets", ULONG),
            ("ulOutMcastOctets", ULONG)
        ]
    PMIB_IPMCAST_IF_ENTRY = POINTER(MIB_IPMCAST_IF_ENTRY)

    class MIB_IPMCAST_IF_TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPMCAST_IF_ENTRY)
        ]
    PMIB_IPMCAST_IF_TABLE = POINTER(MIB_IPMCAST_IF_TABLE)

    SIZEOF_MCAST_IF_TABLE = lambda X: \
        (MIB_IPMCAST_IF_TABLE.table.offset) +  \
        ((X) * sizeof(MIB_IPMCAST_IF_ENTRY)) +  \
        MIB_IPMCAST_IF_TABLE._pack_

    # REGION ***

# _IPMIB_