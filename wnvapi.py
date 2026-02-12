"""++

Copyright (c) Microsoft Corporation. All rights reserved.

Module Name:

    wnvapi.h

Abstract:
    Header file for Windows Network Virtualization API's.

--"""

from . import cpreproc

if cpreproc.pragma_once("__WNV_API_INCLUDED_"):
    # REGION *** Desktop Family or WNV Package ***

    from .defbase import *
    from .winbase import *
    from .in6addr import *
    from .inaddr import *

    wnvapi = WinDLL('wnvapi.dll')

    from .sdkddkver import WIN32_WINNT_WIN8
    
    if cpreproc.get_version() >= WIN32_WINNT_WIN8:
        WNV_NOTIFICATION_TYPE = INT
        if True:
            WnvPolicyMismatchType = 0
            WnvRedirectType = 1
            WnvObjectChangeType = 2
            WnvNotificationTypeMax = 3
        PWNV_NOTIFICATION_TYPE = POINTER(WNV_NOTIFICATION_TYPE)

        WNV_OBJECT_TYPE = INT
        if True:
            WnvProviderAddressType = 0
            WnvCustomerAddressType = 1
            WnvObjectTypeMax = 2
        PWNV_OBJECT_TYPE = POINTER(WNV_OBJECT_TYPE)

        WNV_CA_NOTIFICATION_TYPE = INT
        if True:
            WnvCustomerAddressAdded = 0
            WnvCustomerAddressDeleted = 1
            WnvCustomerAddressMoved = 2
            WnvCustomerAddressMax = 3
        PWNV_CA_NOTIFICATION_TYPE = POINTER(WNV_CA_NOTIFICATION_TYPE)

        class WNV_OBJECT_HEADER(CStructure):
            _fields_ = [
                ("MajorVersion", BYTE),
                ("MinorVersion", BYTE),
                ("Size", ULONG)
            ]
        PWNV_OBJECT_HEADER = POINTER(WNV_OBJECT_HEADER)

        class WNV_NOTIFICATION_PARAM(CStructure):
            _fields_ = [
                ("Header", WNV_OBJECT_HEADER),
                ("NotificationType", WNV_NOTIFICATION_TYPE),
                ("PendingNotifications", ULONG),
                ("Buffer", PCHAR)
            ]
        PWNV_NOTIFICATION_PARAM = POINTER(WNV_NOTIFICATION_PARAM)

        class WNV_IP_ADDRESS(CStructure):
            class _IP_UNION(Union):
                _fields_ = [
                    ("v4", IN_ADDR),
                    ("v6", IN6_ADDR),
                    ("Addr", CHAR * sizeof(IN6_ADDR))
                ]
            _fields_ = [
                ("IP", _IP_UNION)
            ]
        PWNV_IP_ADDRESS = POINTER(WNV_IP_ADDRESS)

        # TODO: need ws2def.py
        """
        class WNV_POLICY_MISMATCH_PARAM(CStructure)
            ADDRESS_FAMILY CAFamily;
            ADDRESS_FAMILY PAFamily;
            ULONG VirtualSubnetId;
            WNV_IP_ADDRESS CA;
            WNV_IP_ADDRESS PA;
        } WNV_POLICY_MISMATCH_PARAM, *PWNV_POLICY_MISMATCH_PARAM;

        WNV_PROVIDER_ADDRESS_CHANGE_PARAM {
            ADDRESS_FAMILY PAFamily;
            WNV_IP_ADDRESS PA;
            NL_DAD_STATE AddressState;
        } WNV_PROVIDER_ADDRESS_CHANGE_PARAM, *PWNV_PROVIDER_ADDRESS_CHANGE_PARAM;

        WNV_CUSTOMER_ADDRESS_CHANGE_PARAM {
            DL_EUI48 MACAddress;
            ADDRESS_FAMILY CAFamily;
            WNV_IP_ADDRESS CA;
            ULONG VirtualSubnetId;
            ADDRESS_FAMILY PAFamily;
            WNV_IP_ADDRESS PA;
            WNV_CA_NOTIFICATION_TYPE NotificationReason;
        } WNV_CUSTOMER_ADDRESS_CHANGE_PARAM, *PWNV_CUSTOMER_ADDRESS_CHANGE_PARAM;

        WNV_OBJECT_CHANGE_PARAM {
            WNV_OBJECT_TYPE ObjectType;
            union {
                WNV_PROVIDER_ADDRESS_CHANGE_PARAM ProviderAddressChange;
                WNV_CUSTOMER_ADDRESS_CHANGE_PARAM CustomerAddressChange;
            } ObjectParam;
        } WNV_OBJECT_CHANGE_PARAM, *PWNV_OBJECT_CHANGE_PARAM;

        WNV_REDIRECT_PARAM {
            ADDRESS_FAMILY CAFamily;
            ADDRESS_FAMILY PAFamily;
            ADDRESS_FAMILY NewPAFamily;
            ULONG VirtualSubnetId;
            WNV_IP_ADDRESS CA;
            WNV_IP_ADDRESS PA;
            WNV_IP_ADDRESS NewPA;
        } WNV_REDIRECT_PARAM, *PWNV_REDIRECT_PARAM;
        """

        if cpreproc.ifndef("WNV_KERNEL_MODE"):
            WnvOpen = declare(wnvapi.WnvOpen, HANDLE)

            WnvRequestNotification = declare(wnvapi.WnvRequestNotification, ULONG, HANDLE, PWNV_NOTIFICATION_PARAM, LPOVERLAPPED, PULONG)

    # _WINVER >= WIN32_WINNT_WIN8

    # REGION ***

# __WNV_API_INCLUDED_
