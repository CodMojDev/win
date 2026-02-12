"""
*** IPEXPORT.H - IP public definitions.
*
*  This file contains public definitions exported to transport layer and
*  application software.
*

/********************************************************************/
/**                     Microsoft LAN Manager                      **/
/**     Copyright (c) Microsoft Corporation. All rights reserved.  **/
/********************************************************************/
/* :ts=4 */
"""

from . import cpreproc

if cpreproc.ifndef("IP_EXPORT_INCLUDED"):
    cpreproc.define("IP_EXPORT_INCLUDED", 1)

    from .sdkddkver import WIN32_WINNT_WINXP, WIN32_WINNT_NT4
    from .minwindef import *

    # REGION *** App Family or OneCore Family or Games Family ***

    #
    # IP type definitions.
    #
    IPAddr = ULONG       # An IP address.
    IPMask = ULONG       # An IP subnet mask.
    IP_STATUS = ULONG    # Status code returned from IP APIs.

    from .in6addr import *

    IPv6Addr = in6_addr

    from .inaddr import *

    #
    # The ip_option_information structure describes the options to be
    # included in the header of an IP packet. The TTL, TOS, and Flags
    # values are carried in specific fields in the header. The OptionsData
    # bytes are carried in the options area following the standard IP header.
    # With the exception of source route options, this data must be in the
    # format to be transmitted on the wire as specified in RFC 791. A source
    # route option should contain the full route - first hop thru final
    # destination - in the route data. The first hop will be pulled out of the
    # data and the option will be reformatted accordingly. Otherwise, the route
    # option should be formatted as specified in RFC 791.
    #

    class ip_option_information(CStructure):
        _fields_ = [
            ("Ttl", BYTE),                # Time To Live
            ("Tos", BYTE),                # Type Of Service
            ("Flags", BYTE),              # IP header flags
            ("OptionsSize", BYTE),        # Size in bytes of options data
            ("OptionsData", PCHAR)        # Pointer to options data
        ]
    IP_OPTION_INFORMATION = ip_option_information
    PIP_OPTION_INFORMATION = POINTER(IP_OPTION_INFORMATION)

    if cpreproc.ifdef("_WIN64"):
        class ip_option_information32(CStructure):
            _fields_ = [
                ("Ttl", BYTE),                # Time To Live
                ("Tos", BYTE),                # Type Of Service
                ("Flags", BYTE),              # IP header flags
                ("OptionsSize", BYTE),        # Size in bytes of options data
                ("OptionsData", DWORD)        # Pointer to options data
            ]
        IP_OPTION_INFORMATION32 = ip_option_information32
        PIP_OPTION_INFORMATION32 = POINTER(IP_OPTION_INFORMATION32)
    # _WIN64

    #
    # The icmp_echo_reply structure describes the data returned in response
    # to an echo request.
    #

    class icmp_echo_reply(CStructure):
        _fields_ = [
            ("Address", IPAddr),               # Replying address
            ("Status", ULONG),                 # Reply IP_STATUS
            ("RoundTripTime", ULONG),          # RTT in milliseconds
            ("DataSize", USHORT),              # Reply data size in bytes
            ("Reserved", USHORT),              # Reserved for system use
            ("Data", PVOID),                   # Pointer to the reply data
            ("Options", ip_option_information) # Reply options
        ]
    ICMP_ECHO_REPLY = icmp_echo_reply
    PICMP_ECHO_REPLY = POINTER(ICMP_ECHO_REPLY)

    if cpreproc.ifdef("_WIN64"):
        class icmp_echo_reply32(CStructure):
            _fields_ = [
                ("Address", IPAddr),                 # Replying address
                ("Status", ULONG),                   # Reply IP_STATUS
                ("RoundTripTime", ULONG),            # RTT in milliseconds
                ("DataSize", USHORT),                # Reply data size in bytes
                ("Reserved", USHORT),                # Reserved for system use
                ("Data", DWORD),                     # Pointer to the reply data
                ("Options", ip_option_information32) # Reply options
            ]
        ICMP_ECHO_REPLY32 = icmp_echo_reply32
        PICMP_ECHO_REPLY32 = POINTER(ICMP_ECHO_REPLY32)
    # _WIN64

    if cpreproc.get_version() >= WIN32_WINNT_WINXP:
        class IPV6_ADDRESS_EX(CStructure):
            _pack_ = 1
            _fields_ = [
                ("sin6_port", USHORT),
                ("sin6_flowinfo", ULONG),
                ("sin6_addr", USHORT * 8),
                ("sin6_scope_id", ULONG)
            ]
        PIPV6_ADDRESS_EX = POINTER(IPV6_ADDRESS_EX)

        class icmpv6_echo_reply_lh(CStructure):
            _fields_ = [
                ("Address", IPV6_ADDRESS_EX),    # Replying address.
                ("Status", ULONG),               # Reply IP_STATUS.
                ("RoundTripTime", UINT)          # RTT in milliseconds.
                # Reply data follows this structure in memory.
            ]
        ICMPV6_ECHO_REPLY_LH = icmpv6_echo_reply_lh
        PICMPV6_ECHO_REPLY_LH = POINTER(ICMPV6_ECHO_REPLY_LH)

        ICMPV6_ECHO_REPLY = ICMPV6_ECHO_REPLY_LH
        PICMPV6_ECHO_REPLY = PICMPV6_ECHO_REPLY_LH

    class arp_send_reply(CStructure):
        _fields_ = [
            ("DestAddress", IPAddr),
            ("SrcAddress", IPAddr)
        ]
    ARP_SEND_REPLY = arp_send_reply
    PARP_SEND_REPLY = POINTER(arp_send_reply)

    class tcp_reserve_port_range(CStructure):
        _fields_ = [
            ("UpperRange", USHORT),
            ("LowerRange", USHORT)
        ]
    TCP_RESERVE_PORT_RANGE = tcp_reserve_port_range
    PTCP_RESERVE_PORT_RANGE = POINTER(TCP_RESERVE_PORT_RANGE)

    MAX_ADAPTER_NAME = 128

    class IP_ADAPTER_INDEX_MAP(CStructure):
        _fields_ = [
            ("Index", ULONG),
            ("Name", WCHAR * MAX_ADAPTER_NAME)
        ]
    PIP_ADAPTER_INDEX_MAP = POINTER(IP_ADAPTER_INDEX_MAP)

    class IP_INTERFACE_INFO(CStructure):
        _fields_ = [
            ("NumAdapters", LONG),
            ("Adapter", PIP_ADAPTER_INDEX_MAP)
        ]
    PIP_INTERFACE_INFO = POINTER(IP_INTERFACE_INFO)

    class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(CStructure):
        _fields_ = [
            ("NumAdapters", ULONG),
            ("Address", PIN_ADDR)
        ]
    PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS = POINTER(IP_UNIDIRECTIONAL_ADAPTER_ADDRESS)

    class IP_ADAPTER_ORDER_MAP(CStructure):
        _fields_ = [
            ("NumAdapters", ULONG),
            ("AdapterOrder", ULONG)
        ]
    PIP_ADAPTER_ORDER_MAP = POINTER(IP_ADAPTER_ORDER_MAP)

    class IP_MCAST_COUNTER_INFO(CStructure):
        _fields_ = [
            ("InMcastOctets", ULONG64),
            ("OutMcastOctets", ULONG64),
            ("InMcastPkts", ULONG64),
            ("OutMcastPkts", ULONG64)
        ]
    PIP_MCAST_COUNTER_INFO = POINTER(IP_MCAST_COUNTER_INFO)

    #
    # IP_STATUS codes returned from IP APIs
    #

    IP_STATUS_BASE             = 11000

    IP_SUCCESS                 = 0
    IP_BUF_TOO_SMALL           = (IP_STATUS_BASE + 1)
    IP_DEST_NET_UNREACHABLE    = (IP_STATUS_BASE + 2)
    IP_DEST_HOST_UNREACHABLE   = (IP_STATUS_BASE + 3)
    IP_DEST_PROT_UNREACHABLE   = (IP_STATUS_BASE + 4)
    IP_DEST_PORT_UNREACHABLE   = (IP_STATUS_BASE + 5)
    IP_NO_RESOURCES            = (IP_STATUS_BASE + 6)
    IP_BAD_OPTION              = (IP_STATUS_BASE + 7)
    IP_HW_ERROR                = (IP_STATUS_BASE + 8)
    IP_PACKET_TOO_BIG          = (IP_STATUS_BASE + 9)
    IP_REQ_TIMED_OUT           = (IP_STATUS_BASE + 10)
    IP_BAD_REQ                 = (IP_STATUS_BASE + 11)
    IP_BAD_ROUTE               = (IP_STATUS_BASE + 12)
    IP_TTL_EXPIRED_TRANSIT     = (IP_STATUS_BASE + 13)
    IP_TTL_EXPIRED_REASSEM     = (IP_STATUS_BASE + 14)
    IP_PARAM_PROBLEM           = (IP_STATUS_BASE + 15)
    IP_SOURCE_QUENCH           = (IP_STATUS_BASE + 16)
    IP_OPTION_TOO_BIG          = (IP_STATUS_BASE + 17)
    IP_BAD_DESTINATION         = (IP_STATUS_BASE + 18)

    #
    # Variants of the above using IPv6 terminology, where different
    #

    IP_DEST_NO_ROUTE            = (IP_STATUS_BASE + 2)
    IP_DEST_ADDR_UNREACHABLE    = (IP_STATUS_BASE + 3)
    IP_DEST_PROHIBITED          = (IP_STATUS_BASE + 4)
    IP_DEST_PORT_UNREACHABLE    = (IP_STATUS_BASE + 5)
    IP_HOP_LIMIT_EXCEEDED       = (IP_STATUS_BASE + 13)
    IP_REASSEMBLY_TIME_EXCEEDED = (IP_STATUS_BASE + 14)
    IP_PARAMETER_PROBLEM        = (IP_STATUS_BASE + 15)

    #
    # IPv6-only status codes
    #

    IP_DEST_UNREACHABLE         = (IP_STATUS_BASE + 40)
    IP_TIME_EXCEEDED            = (IP_STATUS_BASE + 41)
    IP_BAD_HEADER               = (IP_STATUS_BASE + 42)
    IP_UNRECOGNIZED_NEXT_HEADER = (IP_STATUS_BASE + 43)
    IP_ICMP_ERROR               = (IP_STATUS_BASE + 44)
    IP_DEST_SCOPE_MISMATCH      = (IP_STATUS_BASE + 45)

    #
    # The next group are status codes passed up on status indications to
    # transport layer protocols.
    #
    IP_ADDR_DELETED            = (IP_STATUS_BASE + 19)
    IP_SPEC_MTU_CHANGE         = (IP_STATUS_BASE + 20)
    IP_MTU_CHANGE              = (IP_STATUS_BASE + 21)
    IP_UNLOAD                  = (IP_STATUS_BASE + 22)
    IP_ADDR_ADDED              = (IP_STATUS_BASE + 23)
    IP_MEDIA_CONNECT           = (IP_STATUS_BASE + 24)
    IP_MEDIA_DISCONNECT        = (IP_STATUS_BASE + 25)
    IP_BIND_ADAPTER            = (IP_STATUS_BASE + 26)
    IP_UNBIND_ADAPTER          = (IP_STATUS_BASE + 27)
    IP_DEVICE_DOES_NOT_EXIST   = (IP_STATUS_BASE + 28)
    IP_DUPLICATE_ADDRESS       = (IP_STATUS_BASE + 29)
    IP_INTERFACE_METRIC_CHANGE = (IP_STATUS_BASE + 30)
    IP_RECONFIG_SECFLTR        = (IP_STATUS_BASE + 31)
    IP_NEGOTIATING_IPSEC       = (IP_STATUS_BASE + 32)
    IP_INTERFACE_WOL_CAPABILITY_CHANGE = (IP_STATUS_BASE + 33)
    IP_DUPLICATE_IPADD         = (IP_STATUS_BASE + 34)

    IP_GENERAL_FAILURE         = (IP_STATUS_BASE + 50)
    MAX_IP_STATUS              = IP_GENERAL_FAILURE
    IP_PENDING                 = (IP_STATUS_BASE + 255)


    #
    # Values used in the Flags field of IP_OPTION_INFORMATION.
    # 
    IP_FLAG_REVERSE = 0x1         # Do a round-trip echo request.
    IP_FLAG_DF      = 0x2         # Don't fragment this packet.

    #
    # Supported IP Option Types.
    #
    # These types define the options which may be used in the OptionsData field
    # of the ip_option_information structure.  See RFC 791 for a complete
    # description of each.
    #
    IP_OPT_EOL      = 0          # End of list option
    IP_OPT_NOP      = 1          # No operation
    IP_OPT_SECURITY = 0x82       # Security option
    IP_OPT_LSRR     = 0x83       # Loose source route
    IP_OPT_SSRR     = 0x89       # Strict source route
    IP_OPT_RR       = 0x7        # Record route
    IP_OPT_TS       = 0x44       # Timestamp
    IP_OPT_SID      = 0x88       # Stream ID (obsolete)
    IP_OPT_ROUTER_ALERT = 0x94  # Router Alert Option

    MAX_OPT_SIZE    = 40         # Maximum length of IP options in bytes

    if cpreproc.get_version() == WIN32_WINNT_NT4:
        # Ioctls code exposed by Memphis tcpip stack.
        # For NT these ioctls are define in ntddip.h  (private\inc)

        IOCTL_IP_RTCHANGE_NOTIFY_REQUEST   = 101
        IOCTL_IP_ADDCHANGE_NOTIFY_REQUEST  = 102
        IOCTL_ARP_SEND_REQUEST             = 103
        IOCTL_IP_INTERFACE_INFO            = 104
        IOCTL_IP_GET_BEST_INTERFACE        = 105
        IOCTL_IP_UNIDIRECTIONAL_ADAPTER_ADDRESS       = 106

    # REGION ***

# IP_EXPORT_INCLUDED