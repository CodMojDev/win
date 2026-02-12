"""
++

 Copyright (c) 2009 Microsoft Corporation

 Module Name:

 sas.h

 Abstract:

 This header defines SendSAS().

 Author:

 felixk 3/8/2009

--
"""

from . import cpreproc

from .minwindef import VOID, BOOL, windll

from .defbase import *

# REGION *** Desktop Family ***

sas = W_WinDLL("sas.dll")
SendSAS = declare(sas.SendSAS, VOID, BOOL)

# REGION ***