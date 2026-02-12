"""
//------------------------------------------------------------------------------
// File: MediaErr.h
//
// Desc: Shell error codes
//
// Copyright (c) 1999 - 2001, Microsoft Corporation.  All rights reserved.
//------------------------------------------------------------------------------
"""

from . import cpreproc

if cpreproc.pragma_once("_MEDIAERR_H_"):
    DMO_E_INVALIDSTREAMINDEX = 0x80040201
    DMO_E_INVALIDTYPE        = 0x80040202
    DMO_E_TYPE_NOT_SET       = 0x80040203
    DMO_E_NOTACCEPTING       = 0x80040204
    DMO_E_TYPE_NOT_ACCEPTED  = 0x80040205
    DMO_E_NO_MORE_ITEMS      = 0x80040206

    # REGION ***

# _MEDIAERR_H_
