# COM TL imports
from win.com.comtl.object import *
from win.com.comtl.baseface import *

# COM OleIDL import
from win.com.oleidl import *

# COM OLE 2.0 import
from win.com.ole2 import *

# WinAbs imports
from .window import *
from .core.io import *
from .dataexchange import *

#
# OLE & Drag/Drop functions
#

def _ole_Application_on_destroy():
    OleUninitialize()

def initialize_ole():
    hr = OleInitialize(NULL)
    
    if hr in (S_OK, RPC_E_CHANGED_MODE):
        app = Application()
        app.on_destroy += _ole_Application_on_destroy
    elif FAILED(hr):
        raise COMError(hr)

class DragDropWindow(Window):
    """
    Drag & Drop window.
    """
    
    class DropTarget(CComObject, IDropTarget):
        """
        Implementation for OLE IDropTarget.
        """
        
        def __init__(self):
            super().__init__()
            
            # implement the IDropTarget interface functions
            self.implement_interface(IDropTarget)
            
            # DropTarget-specific single events
            self.on_drag_enter = SingleEvent()
            self.on_drop = SingleEvent()
            self.on_drag_leave = SingleEvent()
            self.on_drag_over = SingleEvent()
        
        def DragEnter_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            # check for the pointers validity
            if not (pDataObj and pdwEffect):
                return E_POINTER
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents # wrap IDataObject into DataObject
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drag_enter.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception: 
                return E_FAIL
            return S_OK

        def DragOver_Impl(self, grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int: 
            # check for the pointer validity
            if not pdwEffect:
                return E_POINTER
            try:
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drag_over.execute(grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK

        def DragLeave_Impl(self) -> int: 
            try:
                self.on_drag_leave.execute()
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK

        def Drop_Impl(self, pDataObj: IPointer[IDataObject], grfKeyState: int, pt: POINTL, pdwEffect: PDWORD) -> int:
            # check for the pointers validity
            if not (pDataObj and pdwEffect):
                return E_POINTER
            try:
                data_object = i_cast(pDataObj, DataObject.PTR()).contents # wrap IDataObject into DataObject
                # write handler return value into pdwEffect, handler returns DROPEFFECT
                pdwEffect.contents.value = self.on_drop.execute(data_object, grfKeyState, i_cast_structure(pt, Point))
            except COMError as e: # function threw COM exception to return a HRESULT
                return e.hresult # return exception HRESULT
            # generic exception was thrown
            except Exception:
                return E_FAIL
            return S_OK
        
    def __init__(self):
        super().__init__()
        
        # initialize OLE
        initialize_ole()
        
        # create drop target implementation
        self.drop_target = DragDropWindow.DropTarget()
        
        # bind window events on drop target events
        self.drop_target.on_drag_enter.set(self.on_drag_enter)
        self.drop_target.on_drag_over.set(self.on_drag_over)
        self.drop_target.on_drag_leave.set(self.on_drag_leave)
        self.drop_target.on_drop.set(self.on_drop)
        
        # bind to window events
        self.on_nc_destroy += self.DragDropWindow_on_nc_destroy
        self.on_create += self.DragDropWindow_on_create
    
    def DragDropWindow_on_create(self):
        # register window as drag & drop target
        hr = RegisterDragDrop(self, self.drop_target.ref())
        if FAILED(hr): raise COMError(hr)
        return True
    
    def on_drag_enter(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object entering window.
        """
        
        return DROPEFFECT_NONE
    
    def on_drag_over(self, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object is over window.
        """
        
        return DROPEFFECT_NONE
    
    def on_drag_leave(self):
        """
        This handler is called when drag & drop object leaving window.
        """
        
        return
    
    def on_drop(self, data_object: DataObject, key_state: int, pt: Point) -> int:
        """
        This handler is called when drag & drop object dropped into window.
        """
        
        return DROPEFFECT_NONE
    
    def DragDropWindow_on_nc_destroy(self):
        # release drop target
        self.drop_target.Release()
        RevokeDragDrop(self) # revoke window as drag & drop target from system