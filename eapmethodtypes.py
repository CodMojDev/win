#######################################################################
#
# Copyright (c) Microsoft Corporation
#
# SYNOPSIS
#
#   Declares datastructures that executes the peer eap state machine.
#
#######################################################################

from . import cpreproc

if cpreproc.pragma_once("EAPMETHODAPIS_H"):
    from .minwindef import INT, BYTE, PBYTE, PVOID, CStructure
    
    # REGION *** Desktop Family ***

    # structure that represents EAP packet on the wire
    class tagEapPacket(CStructure):
        _fields_ = [
            ("Code", BYTE),
            ("Id", BYTE),
            ("Length", BYTE * 2),
            ("Data", PBYTE)
            # Any additional data following the first byte. The length of
            # the data can be deduced by the length fields.
        ]
    EapPacket = tagEapPacket

    #
    # EAP packet codes from EAP spec.
    #

    # possible values for 'code' in EAPPacket
    tagEapCode = INT
    if True:
        # [v1_enum]
        EapCodeMinimum = 1
        EapCodeRequest = 1
        EapCodeResponse = 2
        EapCodeSuccess = 3
        EapCodeFailure = 4
        EapCodeMaximum = EapCodeFailure
    EapCode = tagEapCode

    # This is a handle to an eap session owned by the individual eap methods.
    EAP_SESSION_HANDLE = PVOID
    
    # REGION ***

# EAPMETHODAPIS_H