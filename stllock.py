"""
***************************************************************************

  Copyright (c) Microsoft Corporation.  All rights reserved.

  stllock.h

  Purpose: Critical section class

******************************************************************************
"""

from . import cpreproc
from .synchapi import (EnterCriticalSection, 
                       InitializeCriticalSection, 
                       LeaveCriticalSection,
                       DeleteCriticalSection)
from .winnt import RTL_CRITICAL_SECTION, byref

if cpreproc.pragma_once("_STLLOCK_H_"):
    # REGION *** Desktop Family ***

    class CCritSec(RTL_CRITICAL_SECTION):
        def __init__(self):
            InitializeCriticalSection(byref(self))
            
        def __del__(self):
            DeleteCriticalSection(byref(self))
            
        def __enter__(self):
            self.Enter()
            
        def __exit__(self, *_):
            self.Leave()
            
        def Enter(self):
            EnterCriticalSection(byref(self))
            
        def Leave(self):
            LeaveCriticalSection(byref(self))

    # REGION ***