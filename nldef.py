"""++

Copyright (c) 2000-2001  Microsoft Corporation

Module Name:

    nldef.h

Abstract:

    This module contains basic network layer definitions.
    Previously some of these were duplicated in both routprot.h and
    iprtrmib.h.

Author:
Environment:

    user mode or kernel mode

--"""

from . import cpreproc

from .minwindef import *

if cpreproc.pragma_once("_NLDEF_"):
    NL_PREFIX_ORIGIN = INT
    if True:
        #
        # These values are from iptypes.h.
        # They need to fit in a 4 bit field.
        #
        IpPrefixOriginOther = 0
        IpPrefixOriginManual = 1
        IpPrefixOriginWellKnown = 2
        IpPrefixOriginDhcp = 3
        IpPrefixOriginRouterAdvertisement = 4
        IpPrefixOriginUnchanged = 1 << 4

    #
    # TODO: Remove these definitions.
    #
    NlpoOther = IpPrefixOriginOther
    NlpoManual = IpPrefixOriginManual
    NlpoWellKnown = IpPrefixOriginWellKnown
    NlpoDhcp = IpPrefixOriginDhcp
    NlpoRouterAdvertisement = IpPrefixOriginRouterAdvertisement

    NL_SUFFIX_ORIGIN = INT
    if True:
        #
        # TODO: Remove the Nlso* definitions.
        #
        NlsoOther = 0
        NlsoManual = 1
        NlsoWellKnown = 2
        NlsoDhcp = 3
        NlsoLinkLayerAddress = 4
        NlsoRandom = 5

        #
        # These values are from in iptypes.h.
        # They need to fit in a 4 bit field.
        #
        IpSuffixOriginOther = 0
        IpSuffixOriginManual = 1
        IpSuffixOriginWellKnown = 2
        IpSuffixOriginDhcp = 3
        IpSuffixOriginLinkLayerAddress = 4
        IpSuffixOriginRandom = 5
        IpSuffixOriginUnchanged = 1 << 4

    NL_DAD_STATE = INT
    if True:
        #
        # TODO: Remove the Nlds* definitions.
        #
        NldsInvalid = 0
        NldsTentative = 1
        NldsDuplicate = 2
        NldsDeprecated = 3
        NldsPreferred = 4

        #
        # These values are from in iptypes.h.
        #
        IpDadStateInvalid    = 0
        IpDadStateTentative = 1
        IpDadStateDuplicate = 2
        IpDadStateDeprecated = 3
        IpDadStatePreferred = 4

    NL_MAX_METRIC_COMPONENT = (1 << 31) - 1

    #
    # MIB_IPPROTO_* values were previously in iprtrmib.h.
    # PROTO_IP_* values were previously in routprot.h.
    #
    def MAKE_ROUTE_PROTOCOL (suffix, value):  
        globals()[f"MIB_IPPROTO" + suffix] = value
        globals()[f"PROTO_IP_" + suffix] = value

    #
    # Routing protocol values from RFC.
    #
    NL_ROUTE_PROTOCOL = INT
    if True:
        #
        # TODO: Remove the RouteProtocol* definitions.
        #
        RouteProtocolOther   = 1
        RouteProtocolLocal   = 2
        RouteProtocolNetMgmt = 3
        RouteProtocolIcmp    = 4
        RouteProtocolEgp     = 5
        RouteProtocolGgp     = 6
        RouteProtocolHello   = 7
        RouteProtocolRip     = 8
        RouteProtocolIsIs    = 9
        RouteProtocolEsIs    = 10
        RouteProtocolCisco   = 11
        RouteProtocolBbn     = 12
        RouteProtocolOspf    = 13
        RouteProtocolBgp     = 14
        RouteProtocolIdpr    = 15
        RouteProtocolEigrp   = 16
        RouteProtocolDvmrp   = 17
        RouteProtocolRpl     = 18
        RouteProtocolDhcp    = 19

        MAKE_ROUTE_PROTOCOL("OTHER",   1)
        MAKE_ROUTE_PROTOCOL("LOCAL",   2)
        MAKE_ROUTE_PROTOCOL("NETMGMT", 3)
        MAKE_ROUTE_PROTOCOL("ICMP",    4)
        MAKE_ROUTE_PROTOCOL("EGP",     5)
        MAKE_ROUTE_PROTOCOL("GGP",     6)
        MAKE_ROUTE_PROTOCOL("HELLO",   7)
        MAKE_ROUTE_PROTOCOL("RIP",     8)
        MAKE_ROUTE_PROTOCOL("IS_IS",   9)
        MAKE_ROUTE_PROTOCOL("ES_IS",  10)
        MAKE_ROUTE_PROTOCOL("CISCO",  11)
        MAKE_ROUTE_PROTOCOL("BBN",    12)
        MAKE_ROUTE_PROTOCOL("OSPF",   13)
        MAKE_ROUTE_PROTOCOL("BGP",    14)
        MAKE_ROUTE_PROTOCOL("IDPR",   15)
        MAKE_ROUTE_PROTOCOL("EIGRP",  16)
        MAKE_ROUTE_PROTOCOL("DVMRP",  17)
        MAKE_ROUTE_PROTOCOL("RPL",    18)
        MAKE_ROUTE_PROTOCOL("DHCP",   19)

        #
        # Windows-specific definitions.
        #
        MAKE_ROUTE_PROTOCOL("NT_AUTOSTATIC",     10002)
        MAKE_ROUTE_PROTOCOL("NT_STATIC",         10006)
        MAKE_ROUTE_PROTOCOL("NT_STATIC_NON_DOD", 10007)
    PNL_ROUTE_PROTOCOL = POINTER(NL_ROUTE_PROTOCOL)

    NL_ADDRESS_TYPE = INT
    if True:
        NlatUnspecified = 0
        NlatUnicast = 1
        NlatAnycast = 2
        NlatMulticast = 3
        NlatBroadcast = 4
        NlatInvalid = 5
    PNL_ADDRESS_TYPE = POINTER(NL_ADDRESS_TYPE)

    #
    # NL_ROUTE_ORIGIN
    #
    # Define route origin values.
    #

    NL_ROUTE_ORIGIN = INT
    if True:
        NlroManual = 0
        NlroWellKnown = 1
        NlroDHCP = 2
        NlroRouterAdvertisement = 3
        Nlro6to4 = 4
    PNL_ROUTE_ORIGIN = POINTER(NL_ROUTE_ORIGIN)

    #
    # NL_NEIGHBOR_STATE
    #
    # Define network layer neighbor state.  RFC 2461, section 7.3.2 has details.
    # Note: Only state names are documented, we chose the values used here.
    #

    NL_NEIGHBOR_STATE = INT
    if True:
        NlnsUnreachable = 0
        NlnsIncomplete = 1
        NlnsProbe = 2
        NlnsDelay = 3
        NlnsStale = 4
        NlnsReachable = 5
        NlnsPermanent = 6
        NlnsMaximum = 7
    PNL_NEIGHBOR_STATE = POINTER(NL_NEIGHBOR_STATE)

    NL_LINK_LOCAL_ADDRESS_BEHAVIOR = INT
    if True:
        LinkLocalAlwaysOff = 0      # Never use link locals.
        LinkLocalDelayed = 1        # Use link locals only if no other addresses.
                                    # (default for IPv4).
                                    # Legacy mapping: IPAutoconfigurationEnabled.
        LinkLocalAlwaysOn = 2       # Always use link locals (default for IPv6).
        LinkLocalUnchanged = -1

    class NL_INTERFACE_OFFLOAD_ROD(CStructure):
        _fields_ = [
            ("NlChecksumSupported", BOOLEAN, 1),
            ("NlOptionsSupported", BOOLEAN, 1),
            ("TlDatagramChecksumSupported", BOOLEAN, 1),
            ("TlStreamChecksumSupported", BOOLEAN, 1),
            ("TlStreamOptionsSupported", BOOLEAN, 1),
            ("FastPathCompatible", BOOLEAN, 1),
            ("TlLargeSendOffloadSupported", BOOLEAN, 1),
            ("TlGiantSendOffloadSupported", BOOLEAN, 1)
        ]
    PNL_INTERFACE_OFFLOAD_ROD = POINTER(NL_INTERFACE_OFFLOAD_ROD)

    NL_ROUTER_DISCOVERY_BEHAVIOR = INT
    if True:
        RouterDiscoveryDisabled = 0
        RouterDiscoveryEnabled = 1
        RouterDiscoveryDhcp = 2
        RouterDiscoveryUnchanged = -1

    NL_BANDWIDTH_FLAG = INT
    if True:
        NlbwDisabled = 0
        NlbwEnabled = 1
        NlbwUnchanged = -1
    PNL_BANDWIDTH_FLAG = POINTER(NL_BANDWIDTH_FLAG)

    class NL_PATH_BANDWIDTH_ROD(CStructure):
        _fields_ = [
            ("Bandwidth", ULONG64),
            ("Instability", ULONG64),
            ("BandwidthPeaked", BOOLEAN)
        ]
    PNL_PATH_BANDWIDTH_ROD = POINTER(NL_PATH_BANDWIDTH_ROD)

    NL_NETWORK_CATEGORY = INT
    if True:
        NetworkCategoryPublic = 0
        NetworkCategoryPrivate = 1
        NetworkCategoryDomainAuthenticated = 2
        NetworkCategoryUnchanged = -1           # used in a set operation
        NetworkCategoryUnknown = -1             # returned in a query operation
    PNL_NETWORK_CATEGORY = POINTER(NL_NETWORK_CATEGORY)

    NL_INTERFACE_NETWORK_CATEGORY_STATE = INT
    if True:
        NlincCategoryUnknown = 0
        NlincPublic = 1
        NlincPrivate = 2
        NlincDomainAuthenticated = 3
        NlincCategoryStateMax = 4
    PNL_INTERFACE_NETWORK_CATEGORY_STATE = POINTER(NL_INTERFACE_NETWORK_CATEGORY_STATE)

    NL_NETWORK_CONNECTIVITY_LEVEL_HINT = INT
    if True:
        NetworkConnectivityLevelHintUnknown = 0
        NetworkConnectivityLevelHintNone = 1
        NetworkConnectivityLevelHintLocalAccess = 2
        NetworkConnectivityLevelHintInternetAccess = 3
        NetworkConnectivityLevelHintConstrainedInternetAccess = 4
        NetworkConnectivityLevelHintHidden = 5

    NL_NETWORK_CONNECTIVITY_COST_HINT = INT
    if True:
        NetworkConnectivityCostHintUnknown = 0
        NetworkConnectivityCostHintUnrestricted = 1
        NetworkConnectivityCostHintFixed = 2
        NetworkConnectivityCostHintVariable = 3

    class NL_NETWORK_CONNECTIVITY_HINT(CStructure):
        _fields_ = [
            ("ConnectivityLevel", NL_NETWORK_CONNECTIVITY_LEVEL_HINT),
            ("ConnectivityCost", NL_NETWORK_CONNECTIVITY_COST_HINT),

            #
            # Fields reflecting cost factors.
            #
            ("ApproachingDataLimit", BOOLEAN),
            ("OverDataLimit", BOOLEAN),
            ("Roaming", BOOLEAN)
        ]

    NET_IF_CURRENT_SESSION = ULONG(-1).value

    class NL_BANDWIDTH_INFORMATION(CStructure):
        _fields_ = [
            ("Bandwidth", ULONG64),
            ("Instability", ULONG64),
            ("BandwidthPeaked", BOOLEAN)
        ]
    PNL_BANDWIDTH_INFORMATION = POINTER(NL_BANDWIDTH_INFORMATION)