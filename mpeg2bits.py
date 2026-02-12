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

    #pragma pack(push)
    #pragma pack(1)

    

    class PID_BITS(CStructure):
        """
        PID structure
        """
        _pack_ = 1
        _fields_ = [
            ("Reserved", WORD, 3),
            ("ProgramId", WORD, 13)
        ]
    PPID_BITS = POINTER(PID_BITS)

    class MPEG_HEADER_BITS(CStructure):
        """
        Generic MPEG packet header structure
        """
        _pack_ = 1
        _fields_ = [
            ("SectionLength")
        ]
        WORD SectionLength          : 12;
        WORD Reserved               :  2;
        WORD PrivateIndicator       :  1;
        WORD SectionSyntaxIndicator :  1;
    } , *PMPEG_HEADER_BITS;

    #
    # Long MPEG packet header structure
    #

    typedef struct
    {
        BYTE CurrentNextIndicator : 1;
        BYTE VersionNumber        : 5;
        BYTE Reserved             : 2;
    } MPEG_HEADER_VERSION_BITS, *PMPEG_HEADER_VERSION_BITS;

    # REGION ***