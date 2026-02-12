"""
//
// corecrt_share.h
//
//      Copyright (c) Microsoft Corporation. All rights reserved.
//
// Defines the file sharing modes for the sopen() family of functions.  These
// declarations are split out to support the Windows build.
//
"""

SH_DENYRW       = 0x10    # deny read/write mode
SH_DENYWR       = 0x20    # deny write mode
SH_DENYRD       = 0x30    # deny read mode
SH_DENYNO       = 0x40    # deny none mode
SH_SECURE       = 0x80    # secure mode