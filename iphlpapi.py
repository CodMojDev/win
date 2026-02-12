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
    cpreproc.undef('__IPHLPAPI_H__')