"""
//------------------------------------------------------------------------------
// File: ActiveCf.h
//
// Desc: Contains the data formats for the transfer of VfW4 filters via the
//       clipboard.
//
// Copyright (c) 1992 - 2001, Microsoft Corporation.  All rights reserved.
//------------------------------------------------------------------------------
"""

from .minwindef import CStructure, UINT
from .guiddef import CLSID

# REGION *** Desktop Family ***

CFSTR_VFW_FILTERLIST = "Video for Windows 4 Filters"

class VFW_FILTERLIST(CStructure):
    _fields_ = [
        ("cFilters", UINT), # number of CLSIDs in aClsId
        ("aClsId", CLSID),  # ClsId of each filter
    ]
    
    cFilters: int
    aClsId: CLSID

# REGION ***
