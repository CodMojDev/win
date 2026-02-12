"""++

Copyright (c) Microsoft Corporation.  All rights reserved.

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.

Module Name:

    FxsSnd.h

Abstract:

    This header file contains prototypes for "Send to Fax Recipient" functionality.

--"""

from . import cpreproc

from .defbase import *

from .minwindef import BOOL, DWORD, windll, INT, LPCWSTR, VOID, INT

if cpreproc.pragma_once("_FXS_UTILITY_H_"):
    fxsutility = W_WinDLL("fxsutility.dll")

    # REGION *** Desktop Family ***

    SendToMode = INT
    if True:
        SEND_TO_FAX_RECIPIENT_ATTACHMENT = 0

    CanSendToFaxRecipient = declare(fxsutility.CanSendToFaxRecipient, BOOL, VOID)
    SendToFaxRecipient = declare(fxsutility.SendToFaxRecipient, DWORD, SendToMode, LPCWSTR)

    # REGION ***
