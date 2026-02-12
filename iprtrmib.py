"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    iprtrmib.h

Abstract:
    This file contains:
        o Definitions of the MIB_XX structures passed to and from the IP Router Manager
            to query and set MIB variables handled by the IP Router Manager
        o The #defines for the MIB variables IDs  handled by the IP Router Manager
            and made accessible by the MprAdminMIBXXX APIs
        o The Routing PID of the IP Router Manager (as mentioned in ipinfoid.h)

--"""

from . import cpreproc

if cpreproc.pragma_once("__ROUTING_IPRTRMIB_H__"):
    # REGION *** Application Family or OneCore Family or Games Family ***

    ############################################################################
    #                                                                          #
    # Included to get the value of MAX_INTERFACE_NAME_LEN                      #
    #                                                                          #
    ############################################################################

    from .mprapidef import *

    ############################################################################
    #                                                                          #
    # Included to get the necessary constants                                  #
    #                                                                          #
    ############################################################################

    from .ipifcons import *

    ############################################################################
    #                                                                          #
    # This is the Id for IP Router Manager.  The Router Manager handles        #
    # MIB-II, Forwarding MIB and some enterprise specific information.         #
    # Calls made with any other ID are passed on to the corresponding protocol #
    # For example, an MprAdminMIBXXX call with a protocol ID of PID_IP and     #
    # a routing Id of 0xD will be sent to the IP Router Manager and then       #
    # forwarded to OSPF                                                        #
    # This lives in the same number space as the protocol Ids of RIP, OSPF     #
    # etc, so any change made to it should be done keeping this in mind        #
    #                                                                          #
    ############################################################################


    IPRTRMGR_PID = 10000

    ############################################################################
    #                                                                          #
    # The following #defines are the Ids of the MIB variables made accessible  #
    # to the user via MprAdminMIBXXX Apis.  It will be noticed that these are  #
    # not the same as RFC 1213, since the MprAdminMIBXXX APIs work on rows and #
    # groups instead of scalar variables                                       #
    #                                                                          #
    ############################################################################


    IF_NUMBER          = 0
    IF_TABLE           = (IF_NUMBER          + 1)
    IF_ROW             = (IF_TABLE           + 1)
    IP_STATS           = (IF_ROW             + 1)
    IP_ADDRTABLE       = (IP_STATS           + 1)
    IP_ADDRROW         = (IP_ADDRTABLE       + 1)
    IP_FORWARDNUMBER   = (IP_ADDRROW         + 1)
    IP_FORWARDTABLE    = (IP_FORWARDNUMBER   + 1)
    IP_FORWARDROW      = (IP_FORWARDTABLE    + 1)
    IP_NETTABLE        = (IP_FORWARDROW      + 1)
    IP_NETROW          = (IP_NETTABLE        + 1)
    ICMP_STATS         = (IP_NETROW          + 1)
    TCP_STATS          = (ICMP_STATS         + 1)
    TCP_TABLE          = (TCP_STATS          + 1)
    TCP_ROW            = (TCP_TABLE          + 1)
    UDP_STATS          = (TCP_ROW            + 1)
    UDP_TABLE          = (UDP_STATS          + 1)
    UDP_ROW            = (UDP_TABLE          + 1)
    MCAST_MFE          = (UDP_ROW            + 1)
    MCAST_MFE_STATS    = (MCAST_MFE          + 1)
    BEST_IF            = (MCAST_MFE_STATS    + 1)
    BEST_ROUTE         = (BEST_IF            + 1)
    PROXY_ARP          = (BEST_ROUTE         + 1)
    MCAST_IF_ENTRY     = (PROXY_ARP          + 1)
    MCAST_GLOBAL       = (MCAST_IF_ENTRY     + 1)
    IF_STATUS          = (MCAST_GLOBAL       + 1)
    MCAST_BOUNDARY     = (IF_STATUS          + 1)
    MCAST_SCOPE        = (MCAST_BOUNDARY     + 1)
    DEST_MATCHING      = (MCAST_SCOPE        + 1)
    DEST_LONGER        = (DEST_MATCHING      + 1)
    DEST_SHORTER       = (DEST_LONGER        + 1)
    ROUTE_MATCHING     = (DEST_SHORTER       + 1)
    ROUTE_LONGER       = (ROUTE_MATCHING     + 1)
    ROUTE_SHORTER      = (ROUTE_LONGER       + 1)
    ROUTE_STATE        = (ROUTE_SHORTER      + 1)
    MCAST_MFE_STATS_EX = (ROUTE_STATE        + 1)
    IP6_STATS          = (MCAST_MFE_STATS_EX + 1)
    UDP6_STATS         = (IP6_STATS          + 1)
    TCP6_STATS         = (UDP6_STATS         + 1)

    #if (NTDDI_VERSION >= NTDDI_VISTA)
    NUMBER_OF_EXPORTED_VARIABLES   = (TCP6_STATS + 1)
    #else
    NUMBER_OF_EXPORTED_VARIABLES   = (ROUTE_STATE + 1)
    #endif


    ############################################################################
    #                                                                          #
    # MIB_OPAQUE_QUERY is the structure filled in by the user to identify a    #
    # MIB variable                                                             #
    #                                                                          #
    #  dwVarId     ID of MIB Variable (One of the Ids #defined above)          #
    #  dwVarIndex  Variable sized array containing the indices needed to       #
    #              identify a variable. NOTE: Unlike SNMP we dont require that #
    #              a scalar variable be indexed by 0                           #
    #                                                                          #
    ############################################################################

    class MIB_OPAQUE_QUERY(CStructure):
        _fields_ = [
            ("dwVarId", DWORD),
            ("rgdwVarIndex", PDWORD)
        ]
    PMIB_OPAQUE_QUERY = POINTER(MIB_OPAQUE_QUERY)

    ############################################################################
    #                                                                          #
    # The following are the structures which are filled in and returned to the #
    # user when a query is made, OR  are filled in BY THE USER when a set is   #
    # done                                                                     #
    #                                                                          #
    ############################################################################

    from .ipmib import *
    from .tcpmib import *
    from .udpmib import *

    TCP_TABLE_CLASS = INT
    if True:
        TCP_TABLE_BASIC_LISTENER = 0
        TCP_TABLE_BASIC_CONNECTIONS = 1
        TCP_TABLE_BASIC_ALL = 2
        TCP_TABLE_OWNER_PID_LISTENER = 3
        TCP_TABLE_OWNER_PID_CONNECTIONS = 4
        TCP_TABLE_OWNER_PID_ALL = 5
        TCP_TABLE_OWNER_MODULE_LISTENER = 6
        TCP_TABLE_OWNER_MODULE_CONNECTIONS = 7
        TCP_TABLE_OWNER_MODULE_ALL = 8
    PTCP_TABLE_CLASS = POINTER(TCP_TABLE_CLASS)

    UDP_TABLE_CLASS = INT
    if True:
        UDP_TABLE_BASIC = 0
        UDP_TABLE_OWNER_PID = 1
        UDP_TABLE_OWNER_MODULE = 2
    PUDP_TABLE_CLASS = POINTER(UDP_TABLE_CLASS)

    TCPIP_OWNER_MODULE_INFO_CLASS = INT
    if True:
        TCPIP_OWNER_MODULE_INFO_BASIC = 0
    PTCPIP_OWNER_MODULE_INFO_CLASS = POINTER(TCPIP_OWNER_MODULE_INFO_CLASS)

    class TCPIP_OWNER_MODULE_BASIC_INFO(CStructure):
        _fields_ = [
            ("pModuleName", PWCHAR),
            ("pModulePath", PWCHAR)
        ]
    PTCPIP_OWNER_MODULE_BASIC_INFO = POINTER(TCPIP_OWNER_MODULE_BASIC_INFO)

    class MIB_IPMCAST_BOUNDARY(CStructure):
        _fields_ = [
            ("dwIfIndex", DWORD),
            ("dwGroupAddress", DWORD),
            ("dwGroupMask", DWORD),
            ("dwStatus", DWORD)
        ]
    PMIB_IPMCAST_BOUNDARY = POINTER(MIB_IPMCAST_BOUNDARY)

    class MIB_IPMCAST_BOUNDARY_TABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPMCAST_BOUNDARY)
        ]
    PMIB_IPMCAST_BOUNDARY_TABLE = POINTER(MIB_IPMCAST_BOUNDARY_TABLE)

    SIZEOF_BOUNDARY_TABLE = lambda X: (MIB_IPMCAST_BOUNDARY_TABLE.table.offset + ((X) * sizeof(MIB_IPMCAST_BOUNDARY))) + MIB_IPMCAST_BOUNDARY_TABLE._pack_

    class MIB_BOUNDARYROW(CStructure):
        _fields_ = [
            ("dwGroupAddress", DWORD),
            ("dwGroupMask", DWORD)
        ]
    PMIB_BOUNDARYROW = POINTER(MIB_BOUNDARYROW)

    # Structure matching what goes in the registry in a block of type
    # IP_MCAST_LIMIT_INFO.  This contains the fields of
    # MIB_IPMCAST_IF_ENTRY which are configurable.

    class MIB_MCAST_LIMIT_ROW(CStructure):
        _fields_ = [
            ("dwTtl", DWORD),
            ("dwRateLimit", DWORD)
        ]
    PMIB_MCAST_LIMIT_ROW = POINTER(MIB_MCAST_LIMIT_ROW)

    MAX_SCOPE_NAME_LEN = 255

    #
    # Scope names are unicode.  SNMP and MZAP use UTF-8 encoding.
    #

    cpreproc.define("SN_UNICODE")
    SN_CHAR = WCHAR
    SCOPE_NAME_BUFFER = SN_CHAR * (MAX_SCOPE_NAME_LEN+1)
    SCOPE_NAME = POINTER(SCOPE_NAME_BUFFER)

    class MIB_IPMCAST_SCOPE(CStructure):
        _fields_ = [
            ("dwGroupAddress", DWORD),
            ("dwGroupMask", DWORD),
            ("snNameBuffer", SCOPE_NAME_BUFFER),
            ("dwStatus", DWORD)
        ]
    PMIB_IPMCAST_SCOPE = POINTER(MIB_IPMCAST_SCOPE)

    from .ipmib import *

    class MIB_IPDESTROW(CStructure):
        _fields_ = [
            ("ForwardRow", MIB_IPFORWARDROW),
            ("dwForwardPreference", DWORD),
            ("dwForwardViewSet", DWORD)
        ]
    PMIB_IPDESTROW = POINTER(MIB_IPDESTROW)

    class MIB_IPDESTTABLE(CStructure):
        _fields_ = [
            ("dwNumEntries", DWORD),
            ("table", PMIB_IPDESTROW)
        ]
    PMIB_IPDESTTABLE = POINTER(MIB_IPDESTTABLE)

    class MIB_BEST_IF(CStructure):
        _fields_ = [
            ("dwDestAddr", DWORD),
            ("dwIfIndex", DWORD)
        ]
    PMIB_BEST_IF = POINTER(MIB_BEST_IF)

    class MIB_PROXYARP(CStructure):
        _fields_ = [
            ("dwAddress", DWORD),
            ("dwMask", DWORD),
            ("dwIfIndex", DWORD)
        ]
    PMIB_PROXYARP = POINTER(MIB_PROXYARP)

    class MIB_IFSTATUS(CStructure):
        _fields_ = [
            ("dwIfIndex", DWORD),
            ("dwAdminStatus", DWORD),
            ("dwOperationalStatus", DWORD),
            ("bMHbeatActive", BOOL),
            ("bMHbeatAlive", BOOL)
        ]
    PMIB_IFSTATUS = POINTER(MIB_IFSTATUS)

    class MIB_ROUTESTATE(CStructure):
        _fields_ = [
            ("bRoutesSetToStack", BOOL)
        ]
    PMIB_ROUTESTATE = POINTER(MIB_ROUTESTATE)

    ############################################################################
    #                                                                          #
    # All the info passed to (SET/CREATE) and from (GET/GETNEXT/GETFIRST)      #
    # IP Router Manager is encapsulated in the following "discriminated"       #
    # union.  To pass, say MIB_IFROW, use the following code                   #
    #                                                                          #
    #  PMIB_OPAQUE_INFO    pInfo;                                              #
    #  PMIB_IFROW          pIfRow;                                             #
    #  DWORD rgdwBuff[(MAX_MIB_OFFSET + sizeof(MIB_IFROW))/sizeof(DWORD) + 1]; #
    #                                                                          #
    #  pInfo   = (PMIB_OPAQUE_INFO)rgdwBuffer;                                 #
    #  pIfRow  = (MIB_IFROW *)(pInfo->rgbyData);                               #
    #                                                                          #
    #  This can also be accomplished by using the following macro              #
    #                                                                          #
    #  DEFINE_MIB_BUFFER(pInfo,MIB_IFROW, pIfRow);                             #
    #                                                                          #
    ############################################################################

    class MIB_OPAQUE_INFO(CStructure):
        _fields_ = [
            ("dwId", DWORD),
            ("rgbyData", PBYTE)
        ]
    PMIB_OPAQUE_INFO = POINTER(MIB_OPAQUE_INFO)

    MAX_MIB_OFFSET     = 8

    MIB_INFO_SIZE = lambda S: (MAX_MIB_OFFSET + sizeof(S))

    MIB_INFO_SIZE_IN_DWORDS = lambda S: ((MIB_INFO_SIZE(S))//sizeof(DWORD) + 1)
    
    # REGION ***

#__ROUTING_IPRTRMIB_H__