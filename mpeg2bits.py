############################################################################
#
# Copyright (c) Microsoft Corporation.  All rights reserved.
#
# Module Name:
#
#      Mpeg2Bits.h
#
# Abstract:
#
#      This file defines the MPEG-2 section header bitfields. These are
#      defined here instead of in mpegstructs.idl because of MIDL
#      compiler conflicts with bitfield definitions.
#
############################################################################

from . import cpreproc

if cpreproc.pragma_once():
    from .minwindef import *
    
    # REGION *** Desktop Family ***

    class PID_BITS(CStructure):
        """
        PID structure
        """
        _pack_ = 1
        _fields_ = [
            ("Reserved", WORD, 3),
            ("ProgramId", WORD, 13)
        ]
        Reserved: int
        ProgramId: int
    PPID_BITS = POINTER(PID_BITS)

    class MPEG_HEADER_BITS(CStructure):
        """
        Generic MPEG packet header structure
        """
        _pack_ = 1
        _fields_ = [
            ("SectionLength", WORD, 12),
            ("Reserved", WORD, 2),
            ("PrivateIndicator", WORD, 1),
            ("SectionSyntaxIndicator", WORD, 1)
        ]
        SectionLength: int
        Reserved: int
        PrivateIndicator: int
        SectionSyntaxIndicator: int
    PMPEG_HEADER_BITS = PTR(MPEG_HEADER_BITS)

    #
    # Long MPEG packet header structure
    #

    class MPEG_HEADER_VERSION_BITS(CStructure):
        _fields_ = [
            ('CurrentNextIndicator', BYTE, 1),
            ('VersionNumber', BYTE, 5),
            ('Reserved', BYTE, 2)
        ]
        CurrentNextIndicator: int
        VersionNumber: int
        Reserved: int
    PMPEG_HEADER_VERSION_BITS = PTR(MPEG_HEADER_VERSION_BITS)

    # REGION ***