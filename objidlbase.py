#+-------------------------------------------------------------------------
#+-------------------------------------------------------------------------
#
#  Microsoft Windows
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
#--------------------------------------------------------------------------

from . import cpreproc

from .minwindef import *

from comtypes import COMMETHOD, HRESULT, COAUTHINFO, IID, IUnknown, GUID

if cpreproc.pragma_once("_OBJIDLBASE_"):
    class COSERVERINFO(CStructure):
        _fields_ = [
            ("dwReserved1", DWORD),
            ("pwszName", LPWSTR),
            ("pAuthInfo", POINTER(COAUTHINFO)),
            ("dwReserved2", DWORD)
        ]

    IStream = VOID
    IID_IMarshal = IID("{00000003-0000-0000-C000-000000000046}")
    class IMarshal(IUnknown):
        _iid_ = IID_IMarshal
        _methods_ = IUnknown._methods_ + [
            COMMETHOD(['in', 'in', 'in', 'in', 'in', 'out'], HRESULT, "GetUnmarshalClass", 
                    ("riid", POINTER(IID)),
                    ("pv", PVOID),
                    ("dwDestContext", DWORD),
                    ("pvDestContext", PVOID),
                    ("mshlFlags", DWORD),
                    ("pCid", POINTER(GUID))
                    ),
            COMMETHOD(['in', 'in', 'in', 'in', 'in', 'out'], HRESULT, "GetMarshalSizeMax",
                    ("riid", POINTER(IID)), 
                    ("pv", PVOID),
                    ("dwDestContext", DWORD),
                    ("pvDestContext", PVOID),
                    ("mshlFlags", DWORD),
                    ("pSize", PDWORD)),
            COMMETHOD(['in', 'in', 'in', 'in', 'in', 'in'], HRESULT, "MarshalInterface",
                    ("pStm", POINTER(IStream)),
                    ("riid", POINTER(IID)),
                    ("pv", PVOID),
                    ("dwDestContext", DWORD),
                    ("pvDestContext", PVOID),
                    ("mshlFlags", DWORD)),
            COMMETHOD(['in', 'in', 'out'], HRESULT, "UnmarshalInterface",
                    ("pStm", POINTER(IStream)),
                    ("riid", POINTER(IID)),
                    ("ppv", PPVOID)),
            COMMETHOD(['in'], HRESULT, "ReleaseMarshalData",
                    ("pStm", POINTER(IStream))),
            COMMETHOD(['in'], HRESULT, "DisconnectObject",
                    ("dwReserved", DWORD))
        ]