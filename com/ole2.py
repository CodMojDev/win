from ..winerror import *
from .objbase import *
from .oleauto import *
from .storagedef import *

# verbs
OLEIVERB_PRIMARY = (0)
OLEIVERB_SHOW = (-1)
OLEIVERB_OPEN = (-2)
OLEIVERB_HIDE = (-3)
OLEIVERB_UIACTIVATE = (-4)
OLEIVERB_INPLACEACTIVATE = (-5)
OLEIVERB_DISCARDUNDOSTATE = (-6)

# for OleCreateEmbeddingHelper flags; roles in low word; options in high word
EMBDHLP_INPROC_HANDLER = 0x0000
EMBDHLP_INPROC_SERVER = 0x0001
EMBDHLP_CREATENOW = 0x00000000
EMBDHLP_DELAYCREATE = 0x00010000

# extended create function flags
OLECREATE_LEAVERUNNING = 0x00000001

OLESTREAM_CONVERSION_DEFAULT = 0x00000000
OLESTREAM_CONVERSION_DISABLEOLELINK = 0x00000001

from .oleidl import *

@ole32.foreign(DWORD)
def OleBuildVersion() -> int: ...

# @ole32.foreign()

# Helper APIs

@ole32.foreign(HANDLE, HANDLE, CLIPFORMAT, UINT)
def OleDuplicateData(hSrc: int, cfFormat: int, uiFlags: int) -> int: ...

@ole32.foreign(HRESULT, LPUNKNOWN, DWORD, HDC, LPCRECT)
def OleDraw(pUnknown: IPointer[IUnknown], dwAspect: int, hdcDraw: int, lprcBounds: IPointer[RECT]) -> int: ...

@ole32.foreign(HRESULT, LPUNKNOWN)
def OleRun(pUnknown: IPointer[IUnknown]) -> int: ...

@ole32.foreign(BOOL, LPOLEOBJECT, result_function=bool)
def OleIsRunning(pObject: IPointer[IOleObject]) -> bool: ...

@ole32.foreign(HRESULT, LPUNKNOWN, BOOL, BOOL)
def OleLockRunning(self, pUnknown: IPointer[IUnknown], fLock: bool, fLastUnlockCloses: bool) -> int: ...

@ole32.foreign(VOID, LPSTGMEDIUM)
def ReleaseStgMedium(self, stg: IPointer[STGMEDIUM]): ...

@ole32.foreign(HRESULT, PTR(LPOLEADVISEHOLDER))
def CreateOleAdviseHolder(ppAdviseHolder: IDoublePtr[IOleAdviseHolder]) -> int: ...