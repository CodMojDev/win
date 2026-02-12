"""
/*
 * isguids.h - Internet Shortcut GUID definitions.
 *
 * Copyright (c) Microsoft Corporation. All rights reserved.
 */


/* GUIDs
 ********/
"""

from . import cpreproc

from .guiddef import GUID

from .defbase import *

if cpreproc.pragma_once("_ISGUIDS_H_"):
    # REGION *** Desktop Family ***

    CLSID_InternetShortcut       = GUID("{fbf23b40-e3f0-101b-8488-00aa003e56f8}")
    IID_IUniformResourceLocatorA = GUID("{fbf23b80-e3f0-101b-8488-00aa003e56f8}")
    IID_IUniformResourceLocatorW = GUID("{cabb0da0-da57-11cf-9974-0020afd79762}")
    IID_IUniformResourceLocator  = unicode(IID_IUniformResourceLocatorW, IID_IUniformResourceLocatorA)

    # REGION ***
