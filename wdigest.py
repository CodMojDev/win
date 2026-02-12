#+-----------------------------------------------------------------------
#
# Copyright (c) 2001 Microsoft Corporation
#
# File:        WDIGEST.H
#
# Contents:    Public WDigest Security Package structures for use
#              with APIs from SECURITY.H
#
#
# History:     28Mar01,  KDamour    Created
#
#------------------------------------------------------------------------

from . import cpreproc

from .defbase import *

if cpreproc.pragma_once("__WDIGEST_H__"):
    # REGION *** Desktop Family ***

    # begin_ntsecapi

    WDIGEST_SP_NAME_A            =  "WDigest"
    WDIGEST_SP_NAME_W            = u"WDigest"

    WDIGEST_SP_NAME = unicode(WDIGEST_SP_NAME_W, WDIGEST_SP_NAME_A)

    # end_ntsecapi

    # begin_ntsecapi

    # This flag indicates to EncryptMessage that the message is not to actually
    # be encrypted, but a header/trailer is to be produced - SECQOP_WRAP_NO_ENCRYPT

    # end_ntsecapi

    # REGION ***

# __WDIGEST_H__