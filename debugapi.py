"""
### DebugApi.py -- ApiSet Contract for api-ms-win-core-debug-l1

Forwarded to dbg/dbgapi.py

DebugApi.h -- ApiSet Contract for api-ms-win-core-debug-l1\n
Copyright (c) Microsoft Corporation. All rights reserved.
"""

from . import cpreproc

if cpreproc.pragma_once('_APISETDEBUG_'):
    from .dbg.dbgapi import *