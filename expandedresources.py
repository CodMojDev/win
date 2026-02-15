"""
//
// Copyright (c) Microsoft Corporation. All rights reserved.
//

//
// API Set Contract:
//
//    api-ms-win-gaming-expandedresources-l1-1-*
//
// Abstract:
//
//    This header file provides API function signatures for expanded resources / GameMode apps.
//
"""

from . import cpreproc

from .com.comdefbase import HRESULT

from .minwindef import windll, HRESULT, PULONG, PBOOL

from .defbase import *

if cpreproc.pragma_once("_APISET_EXPANDEDRESOURCES_"):
    gamemode = W_WinDLL("gamemode.dll")

    HasExpandedResources = declare(gamemode.HasExpandedResources, HRESULT, PBOOL)

    GetExpandedResourceExclusiveCpuCount = declare(gamemode.GetExpandedResourceExclusiveCpuCount, HRESULT, PULONG)

    ReleaseExclusiveCpuSets = declare(gamemode.ReleaseExclusiveCpuSets, HRESULT)

# _APISET_EXPANDEDRESOURCES_
