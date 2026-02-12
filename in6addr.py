"""++

Copyright (c) Microsoft Corporation

Module Name:

    in6addr.h

Environment:

    user mode or kernel mode

--"""

from . import cpreproc

from .minwindef import BYTE, USHORT, CStructure, Union, POINTER

if cpreproc.pragma_once("__IN_6_ADDR__"):
    # REGION *** Desktop Family or OneCore Family or Games Family ***
    
    
    class in6_addr(CStructure):
        """
         IPv6 Internet address (RFC 2553)
         This is an 'on-wire' format structure.
        """
        class U(Union):
            _fields_ = [
                ("Byte", BYTE * 16),
                ("Word", USHORT * 8)
            ]
        _fields_ = [
            ("u", U)
        ]
    IN6_ADDR = in6_addr
    PIN6_ADDR = LPIN6_ADDR = POINTER(IN6_ADDR)

    in_addr6 = in6_addr

    #
    # Defines to match RFC 2553.
    #
    _S6_un     = lambda x: x.u
    _S6_u8     = lambda x: x.Byte
    s6_addr    = lambda x: x._S6_un._S6_u8

    #
    # Defines for our implementation.
    #
    s6_bytes   = lambda x: x.u.Byte
    s6_words   = lambda x: x.u.Word

    # REGION ***
# __IN_6_ADDR__