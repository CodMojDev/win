#
#    Copyright (C) Microsoft.  All rights reserved.
#

from . import cpreproc

if cpreproc.pragma_once("_IME_CMODES_"):
    # bit field for conversion mode
    IME_CMODE_ALPHANUMERIC         = 0x0000
    IME_CMODE_NATIVE               = 0x0001
    IME_CMODE_CHINESE              = IME_CMODE_NATIVE
    IME_CMODE_HANGUL               = IME_CMODE_NATIVE
    IME_CMODE_JAPANESE             = IME_CMODE_NATIVE
    IME_CMODE_KATAKANA             = 0x0002  # only effect under IME_CMODE_NATIVE
    IME_CMODE_LANGUAGE             = 0x0003
    IME_CMODE_FULLSHAPE            = 0x0008
    IME_CMODE_ROMAN                = 0x0010
    IME_CMODE_CHARCODE             = 0x0020
    IME_CMODE_HANJACONVERT         = 0x0040
    IME_CMODE_NATIVESYMBOL         = 0x0080

# _IME_CMODES_

