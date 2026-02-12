"""++

Copyright (c) Microsoft Corporation

Module Name:

    inaddr.h

Environment:

    user mode or kernel mode

--"""

from . import cpreproc

if cpreproc.pragma_once("s_addr"):
    from .minwindef import *

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    #
    # IPv4 Internet address
    # This is an 'on-wire' format structure.
    #
    class in_addr(CStructure):
        class CLS_S_un(Union):
            class CLS_S_un_b(CStructure):
                _fields_ = [
                    ("s_b1", BYTE),
                    ("s_b2", BYTE),
                    ("s_b3", BYTE),
                    ("s_b4", BYTE)
                ]
            class CLS_S_un_w(CStructure):
                _fields_ = [
                    ("s_w1", USHORT),
                    ("s_w2", USHORT)
                ]
            _fields_ = [
                ("S_un_b", CLS_S_un_b),
                ("S_un_w", CLS_S_un_w),
                ("S_addr", ULONG)
            ]
        _fields_ = [
            ("S_un", CLS_S_un)
        ]
    IN_ADDR = in_addr
    PIN_ADDR = LPIN_ADDR = POINTER(IN_ADDR)
    
    s_addr  = lambda x: x.S_un.S_addr         # can be used for most tcp & ip code
    s_host  = lambda x: x.S_un.S_un_b.s_b2    # host on imp
    s_net   = lambda x: x.S_un.S_un_b.s_b1    # network
    s_imp   = lambda x: x.S_un.S_un_w.s_w2    # imp
    s_impno = lambda x: x.S_un.S_un_b.s_b4    # imp #
    s_lh    = lambda x: x.S_un.S_un_b.s_b3    # logical host

    # REGION ***