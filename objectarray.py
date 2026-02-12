from . import cpreproc

if cpreproc.pragma_once("__objectarray_h__"):
    # REGION *** Desktop Family ***

    from comtypes import COMMETHOD, IUnknown
    from .minwindef import *
    from .guiddef import *

    # generic interfaces that express a set of items

    IID_IObjectArray = IID("{92CA9DCD-5622-4bba-A805-5E9F541BD8C9}")
    class IObjectArray(IUnknown):
        """Unknown Object Array"""
        
        _iid_ = IID_IObjectArray
        _methods_ = IUnknown._methods_ + [
            COMMETHOD(["out"], HRESULT, "GetCount", ("pcObjects", PUINT)),
            COMMETHOD(["in", "in", "out"], HRESULT, "GetAt", 
                      ("uiIndex", UINT),
                      ("riid", REFIID),
                      ("ppv", PLPVOID))
        ]

    IID_IObjectCollection = IID("{5632b1a4-e38a-400a-928a-d4cd63230295}")
    class IObjectCollection(IObjectArray):
        _iid_ = IID_IObjectCollection
        _methods_ = IObjectArray._methods_ + [
            COMMETHOD(["in"], HRESULT, "AddObject", ("punk", POINTER(IUnknown))),
            COMMETHOD(["in"], HRESULT, "AddFromArray", ("poaSource", POINTER(IObjectArray))),
            COMMETHOD(["in"], HRESULT, "RemoveObjectAt", ("uiIndex", UINT)),
            COMMETHOD([], HRESULT, "Clear")
        ]

# REGION ***