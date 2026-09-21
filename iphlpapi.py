"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    iphlpapi.h

Abstract:
    Header file for functions to interact with the IP Stack for MIB-II and
    related functionality

--"""

from . import cpreproc

if cpreproc.pragma_once("__IPHLPAPI_H__"):
    from .defbase import *
    iphlpapi = get_win_library("iphlpapi.dll")
    
    # REGION *** Application Family or OneCore Family or Games Family ***
    
    """
    //////////////////////////////////////////////////////////////////////////////
    //                                                                          //
    // IPRTRMIB.H has the definitions of the structures used to set and get     //
    // information                                                              //
    //                                                                          //
    //////////////////////////////////////////////////////////////////////////////
    """
    
    from .winbase import *
    from .iprtrmib import *
    from .ipexport import *
    from .iptypes import *
    from .tcpestats import *
    
    # REGION ***
    
    # REGION *** Desktop Family or OneCore Family or Games Family ***
    
    ############################################################################
    #                                                                          #
    # The GetXXXTable APIs take a buffer and a size of buffer.  If the buffer  #
    # is not large enough, the APIs return ERROR_INSUFFICIENT_BUFFER  and      #
    # *pdwSize is the required buffer size                                     #
    # The bOrder is a BOOLEAN, which if TRUE sorts the table according to      #
    # MIB-II(RFC XXXX)                                                         #
    #                                                                          #
    ############################################################################
    ############################################################################
    #                                                                          #
    # Retrieves the number of interfaces in the system. These include LAN and  #
    # WAN interfaces                                                           #
    #                                                                          #
    ############################################################################
    GetNumberOfInterfaces = declare(iphlpapi.GetNumberOfInterfaces, DWORD, PDWORD)
    ############################################################################
    #                                                                          #
    # Gets the MIB-II ifEntry                                                  #
    # The dwIndex field of the MIB_IFROW should be set to the index of the     #
    # interface being queried                                                  #
    #                                                                          #
    ############################################################################
    GetIfEntry = declare(iphlpapi.GetIfEntry, DWORD, PMIB_IFROW)
    ############################################################################
    #                                                                          #
    # Gets the MIB-II IfTable                                                  #
    #                                                                          #
    ############################################################################
    GetIfTable = declare(iphlpapi.GetIfTable, DWORD, PMIB_IFTABLE, PULONG, BOOL)
    ############################################################################
    #                                                                          #
    # Gets the Interface to IP Address mapping                                 #
    #                                                                          #
    ############################################################################
    GetIpAddrTable = declare(iphlpapi.GetIpAddrTable, DWORD, PMIB_IPADDRTABLE, PULONG, BOOL)
    ############################################################################
    #                                                                          #
    # Gets the current IP Address to Physical Address(ARP) mapping             #
    #                                                                          #
    ############################################################################
    GetIpNetTable = declare(iphlpapi.GetIpNetTable, ULONG, PMIB_IPNETTABLE, PULONG, BOOL)
    ############################################################################
    #                                                                          #
    # Gets the IP Routing Table (RFX XXXX)                                     #
    #                                                                          #
    ############################################################################
    GetIpForwardTable = declare(iphlpapi.GetIpForwardTable, DWORD, PMIB_IPFORWARDTABLE, PULONG, BOOL)
    ############################################################################
    #                                                                          #
    # Gets TCP Connection/UDP Listener Table                                   #
    #                                                                          #
    ############################################################################
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetTcpTable = declare(iphlpapi.GetTcpTable, ULONG, PMIB_TCPTABLE, PULONG, BOOL)
    GetExtendedTcpTable = declare(iphlpapi.GetExtendedTcpTable, DWORD, PVOID, PDWORD, BOOL, ULONG, TCP_TABLE_CLASS, ULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetOwnerModuleFromTcpEntry = declare(iphlpapi.GetOwnerModuleFromTcpEntry, DWORD, PMIB_TCPROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, PDWORD)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    GetUdpTable = declare(iphlpapi.GetUdpTable, ULONG, PMIB_UDPTABLE, PULONG, BOOL)
    GetExtendedUdpTable = declare(iphlpapi.GetExtendedUdpTable, DWORD, PVOID, PDWORD, BOOL, ULONG, UDP_TABLE_CLASS, ULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetOwnerModuleFromUdpEntry = declare(iphlpapi.GetOwnerModuleFromUdpEntry, DWORD, PMIB_UDPROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, PDWORD)
    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        GetTcpTable2 = declare(iphlpapi.GetTcpTable2, ULONG, PMIB_TCPTABLE2, PULONG, BOOL)

    # REGION ***

    # REGION *** Desktop Family ***

    if cpreproc.get_version() < WIN32_WINNT_VISTA:
        #
        # Deprecated APIs, Added for documentation.
        #
        AllocateAndGetTcpExTableFromStack = declare(iphlpapi.AllocateAndGetTcpExTableFromStack, DWORD, PPVOID, BOOL, HANDLE, DWORD, DWORD)
        AllocateAndGetUdpExTableFromStack = declare(iphlpapi.AllocateAndGetUdpExTableFromStack, DWORD, PPVOID, BOOL, HANDLE, DWORD, DWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_VISTA:
        GetTcp6Table = declare(iphlpapi.GetTcp6Table, ULONG, PMIB_TCP6TABLE, PULONG, BOOL)
        GetTcp6Table2 = declare(iphlpapi.GetTcp6Table2, ULONG, PMIB_TCP6TABLE2, PULONG, BOOL)
        GetPerTcpConnectionEStats = declare(iphlpapi.GetPerTcpConnectionEStats, ULONG, PMIB_TCPROW, TCP_ESTATS_TYPE, PVOID, ULONG, ULONG, PVOID, ULONG, ULONG, PVOID, ULONG, ULONG)
        SetPerTcpConnectionEStats = declare(iphlpapi.SetPerTcpConnectionEStats, ULONG, PMIB_TCPROW, TCP_ESTATS_TYPE, PVOID, ULONG, ULONG, ULONG)
        GetPerTcp6ConnectionEStats = declare(iphlpapi.GetPerTcp6ConnectionEStats, ULONG, PMIB_TCP6ROW, TCP_ESTATS_TYPE, PVOID, ULONG, ULONG, PVOID, ULONG, ULONG, PVOID, ULONG, ULONG)
        SetPerTcp6ConnectionEStats = declare(iphlpapi.SetPerTcp6ConnectionEStats, ULONG, PMIB_TCP6ROW, TCP_ESTATS_TYPE, PVOID, ULONG, ULONG, ULONG)
        GetOwnerModuleFromTcp6Entry = declare(iphlpapi.GetOwnerModuleFromTcp6Entry, DWORD, PMIB_TCP6ROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, PDWORD)
        GetUdp6Table = declare(iphlpapi.GetUdp6Table, ULONG, PMIB_UDP6TABLE, PULONG, BOOL)
        GetOwnerModuleFromUdp6Entry = declare(iphlpapi.GetOwnerModuleFromUdp6Entry, DWORD, PMIB_UDP6ROW_OWNER_MODULE, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, PDWORD)
    
    #
    # Because this function isn't marked with WINAPI, it is not marked with
    # IPHLPAPI_DLL_LINKAGE in order to prevent build breaks with managed projects.
    #
    GetOwnerModuleFromPidAndInfo = declare(iphlpapi.GetOwnerModuleFromPidAndInfo, DWORD, ULONG, PULONGLONG, TCPIP_OWNER_MODULE_INFO_CLASS, PVOID, PDWORD)
    #######################################
    #                                                                          #
    # Gets IP/ICMP/TCP/UDP Statistics                                          #
    #                                                                          #
    #######################################
    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        GetIpStatistics = declare(iphlpapi.GetIpStatistics, ULONG, PMIB_IPSTATS)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        GetIcmpStatistics = declare(iphlpapi.GetIcmpStatistics, ULONG, PMIB_ICMP)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        GetTcpStatistics = declare(iphlpapi.GetTcpStatistics, ULONG, PMIB_TCPSTATS)
        GetUdpStatistics = declare(iphlpapi.GetUdpStatistics, ULONG, PMIB_UDPSTATS)
    if cpreproc.get_version() >= WIN32_WINNT_WINXP:
        SetIpStatisticsEx = declare(iphlpapi.SetIpStatisticsEx, ULONG, PMIB_IPSTATS, ULONG)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_WINXP:
        GetIpStatisticsEx = declare(iphlpapi.GetIpStatisticsEx, ULONG, PMIB_IPSTATS, ULONG)
        GetIcmpStatisticsEx = declare(iphlpapi.GetIcmpStatisticsEx, ULONG, PMIB_ICMP_EX, ULONG)
        GetTcpStatisticsEx = declare(iphlpapi.GetTcpStatisticsEx, ULONG, PMIB_TCPSTATS, ULONG)
        GetUdpStatisticsEx = declare(iphlpapi.GetUdpStatisticsEx, ULONG, PMIB_UDPSTATS, ULONG)
    if cpreproc.get_version() >= WIN32_WINNT_WIN10:
        GetTcpStatisticsEx2 = declare(iphlpapi.GetTcpStatisticsEx2, ULONG, PMIB_TCPSTATS2, ULONG)
        GetUdpStatisticsEx2 = declare(iphlpapi.GetUdpStatisticsEx2, ULONG, PMIB_UDPSTATS2, ULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    ############################################################################
    #                                                                          #
    # Used to set the ifAdminStatus on an interface.  The only fields of the   #
    # MIB_IFROW that are relevant are the dwIndex(index of the interface       #
    # whose status needs to be set) and the dwAdminStatus which can be either  #
    # MIB_IF_ADMIN_STATUS_UP or MIB_IF_ADMIN_STATUS_DOWN                       #
    #                                                                          #
    ############################################################################
    SetIfEntry = declare(iphlpapi.SetIfEntry, DWORD, PMIB_IFROW)
    ############################################################################
    #                                                                          #
    # Used to create, modify or delete a route.  In all cases the              #
    # dwForwardIfIndex, dwForwardDest, dwForwardMask, dwForwardNextHop and     #
    # dwForwardPolicy MUST BE SPECIFIED. Currently dwForwardPolicy is unused   #
    # and MUST BE 0.                                                           #
    # For a set, the complete MIB_IPFORWARDROW structure must be specified     #
    #                                                                          #
    ############################################################################
    CreateIpForwardEntry = declare(iphlpapi.CreateIpForwardEntry, DWORD, PMIB_IPFORWARDROW)
    SetIpForwardEntry = declare(iphlpapi.SetIpForwardEntry, DWORD, PMIB_IPFORWARDROW)
    DeleteIpForwardEntry = declare(iphlpapi.DeleteIpForwardEntry, DWORD, PMIB_IPFORWARDROW)
    ############################################################################
    #                                                                          #
    # Used to set the ipForwarding to ON or OFF(currently only ON->OFF is      #
    # allowed) and to set the defaultTTL.  If only one of the fields needs to  #
    # be modified and the other needs to be the same as before the other field #
    # needs to be set to MIB_USE_CURRENT_TTL or MIB_USE_CURRENT_FORWARDING as  #
    # the case may be                                                          #
    #                                                                          #
    ############################################################################
    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        SetIpStatistics = declare(iphlpapi.SetIpStatistics, DWORD, PMIB_IPSTATS)
    ############################################################################
    #                                                                          #
    # Used to set the defaultTTL.                                              #
    #                                                                          #
    ############################################################################
    SetIpTTL = declare(iphlpapi.SetIpTTL, DWORD, UINT)
    ############################################################################
    #                                                                          #
    # Used to create, modify or delete an ARP entry.  In all cases the dwIndex #
    # dwAddr field MUST BE SPECIFIED.                                          #
    # For a set, the complete MIB_IPNETROW structure must be specified         #
    #                                                                          #
    ############################################################################
    CreateIpNetEntry = declare(iphlpapi.CreateIpNetEntry, DWORD, PMIB_IPNETROW)
    SetIpNetEntry = declare(iphlpapi.SetIpNetEntry, DWORD, PMIB_IPNETROW)
    DeleteIpNetEntry = declare(iphlpapi.DeleteIpNetEntry, DWORD, PMIB_IPNETROW)
    FlushIpNetTable = declare(iphlpapi.FlushIpNetTable, DWORD, DWORD)
    ############################################################################
    #                                                                          #
    # Used to create or delete a Proxy ARP entry. The dwIndex is the index of  #
    # the interface on which to PARP for the dwAddress.  If the interface is   #
    # of a type that doesnt support ARP, e.g. PPP, then the call will fail     #
    #                                                                          #
    ############################################################################
    CreateProxyArpEntry = declare(iphlpapi.CreateProxyArpEntry, DWORD, DWORD, DWORD, DWORD)
    DeleteProxyArpEntry = declare(iphlpapi.DeleteProxyArpEntry, DWORD, DWORD, DWORD, DWORD)
    ############################################################################
    #                                                                          #
    # Used to set the state of a TCP Connection. The only state that it can be #
    # set to is MIB_TCP_STATE_DELETE_TCB.  The complete MIB_TCPROW structure   #
    # MUST BE SPECIFIED                                                        #
    #                                                                          #
    ############################################################################
    SetTcpEntry = declare(iphlpapi.SetTcpEntry, DWORD, PMIB_TCPROW)
    GetInterfaceInfo = declare(iphlpapi.GetInterfaceInfo, DWORD, PIP_INTERFACE_INFO, PULONG)
    GetUniDirectionalAdapterInfo = declare(iphlpapi.GetUniDirectionalAdapterInfo, DWORD, PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS, PULONG)
    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        if cpreproc.ifndef("NHPALLOCATEANDGETINTERFACEINFOFROMSTACK_DEFINED"):
            cpreproc.define("NHPALLOCATEANDGETINTERFACEINFOFROMSTACK_DEFINED")
            NhpAllocateAndGetInterfaceInfoFromStack = declare(iphlpapi.NhpAllocateAndGetInterfaceInfoFromStack, DWORD, PIP_INTERFACE_NAME_INFO, PDWORD, BOOL, HANDLE, DWORD)
    ############################################################################
    #                                                                          #
    # Gets the "best" outgoing interface for the specified destination address #
    #                                                                          #
    ############################################################################
    GetBestInterface = declare(iphlpapi.GetBestInterface, DWORD, IPAddr, PDWORD)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    # TODO: dependency to sockaddr (ws2def.h / winsock2.h / ws2ipdef.h)
    # GetBestInterfaceEx = declare(iphlpapi.GetBestInterfaceEx, DWORD, sockaddr, PDWORD)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    ############################################################################
    #                                                                          #
    # Gets the best(longest matching prefix) route for the given destination   #
    # If the source address is also specified(i.e. is not 0x00000000), and     #
    # there are multiple "best" routes to the given destination, the returned  #
    # route will be one that goes out over the interface which has an address  #
    # that matches the source address                                          #
    #                                                                          #
    ############################################################################
    GetBestRoute = declare(iphlpapi.GetBestRoute, DWORD, DWORD, DWORD, PMIB_IPFORWARDROW)
    NotifyAddrChange = declare(iphlpapi.NotifyAddrChange, DWORD, PHANDLE, LPOVERLAPPED)
    NotifyRouteChange = declare(iphlpapi.NotifyRouteChange, DWORD, PHANDLE, LPOVERLAPPED)
    CancelIPChangeNotify = declare(iphlpapi.CancelIPChangeNotify, BOOL, LPOVERLAPPED)
    GetAdapterIndex = declare(iphlpapi.GetAdapterIndex, DWORD, LPWSTR, PULONG)
    AddIPAddress = declare(iphlpapi.AddIPAddress, DWORD, IPAddr, IPMask, DWORD, PULONG, PULONG)
    DeleteIPAddress = declare(iphlpapi.DeleteIPAddress, DWORD, ULONG)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***

    if cpreproc.get_version() >= WIN32_WINNT_WIN2K:
        GetNetworkParams = declare(iphlpapi.GetNetworkParams, DWORD, PFIXED_INFO, PULONG)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    GetAdaptersInfo = declare(iphlpapi.GetAdaptersInfo, ULONG, PIP_ADAPTER_INFO, PULONG)
    GetAdapterOrderMap = declare(iphlpapi.GetAdapterOrderMap, PIP_ADAPTER_ORDER_MAP, VOID)

    # REGION ***

    # REGION *** Application Family or OneCore Family or Games Family ***
    
    # TODO: Winsock2-dependent functions definitions
    
    # REGION ***
    
    # REGION ***