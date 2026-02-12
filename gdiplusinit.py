"""
/**************************************************************************
*
* Copyright (c) 2000-2003 Microsoft Corporation
*
* Module Name:
*
*   Gdiplus initialization
*
* Abstract:
*
*   GDI+ Startup and Shutdown APIs
*
**************************************************************************/
"""

from . import cpreproc

from .minwindef import *

from .defbase import *

if cpreproc.pragma_once("_GDIPLUSINIT_H"):
    
    from .gdiplustypes import Status

    gdiplus = W_WinDLL("gdiplus.dll")

    # REGION *** Desktop Family ***

    DebugEventLevel = INT
    if True:
        DebugEventLevelFatal = 0
        DebugEventLevelWarning = 1

    # Callback function that GDI+ can call, on debug builds, for assertions
    # and warnings.

    DebugEventProc = WINAPI(VOID, DebugEventLevel, PCHAR)

    # Notification functions which the user must call appropriately if
    # "SuppressBackgroundThread" (below) is set.

    NotificationHookProc = WINAPI(Status, PULONG_PTR)
    NotificationUnhookProc = WINAPI(VOID, ULONG_PTR)

    # Input structure for GdiplusStartup()

    class GdiplusStartupInput(CStructure):
        _pack_ = 8
        _fields_ = [
            ("GdiplusVersion", UINT32),             # Must be 1  (or 2 for the Ex version)
            ("DebugEventCallback", DebugEventProc), # Ignored on free builds
            ("SuppressBackgroundThread", BOOL),     # FALSE unless you're prepared to call 
                                                    # the hook/unhook functions properly
            ("SuppressExternalCodecs", BOOL)        # FALSE unless you want GDI+ only to use
                                                    # its internal image codecs.
        ]
        def __init__(self, 
                    debugEventCallback = cast(NULL, DebugEventProc),
                    suppressBackgroundThread = False,
                    suppressExternalCodecs = False):
            self.GdiplusVersion = 1
            self.DebugEventCallback = debugEventCallback
            self.SuppressBackgroundThread = suppressBackgroundThread
            self.SuppressExternalCodecs = suppressExternalCodecs

    #if (GDIPVER >= 0x0110)
    class GdiplusStartupInputEx(CStructure):
        _pack_ = 8
        _fields_ = [
            ("GdiplusVersion", UINT32),             # Must be 1  (or 2 for the Ex version)
            ("DebugEventCallback", DebugEventProc), # Ignored on free builds
            ("SuppressBackgroundThread", BOOL),     # FALSE unless you're prepared to call 
                                                    # the hook/unhook functions properly
            ("SuppressExternalCodecs", BOOL),       # FALSE unless you want GDI+ only to use
                                                    # its internal image codecs.
            ("StartupParameters", INT)              # Do we not set the FPU rounding mode
        ]
        def __init__(self, 
                    startupParameters = 0,
                    debugEventCallback = cast(NULL, DebugEventProc),
                    suppressBackgroundThread = False,
                    suppressExternalCodecs = False):
            self.GdiplusVersion = 2
            self.DebugEventCallback = debugEventCallback
            self.SuppressBackgroundThread = suppressBackgroundThread
            self.SuppressExternalCodecs = suppressExternalCodecs
            self.StartupParameters = startupParameters

    GdiplusStartupParams = INT
    if True:
        GdiplusStartupDefault = 0
        GdiplusStartupNoSetRound = 1
        GdiplusStartupSetPSValue = 2
        GdiplusStartupTransparencyMask = 0xFF000000

    # Output structure for GdiplusStartup()

    class GdiplusStartupOutput(CStructure):
        _pack_ = 8
        _fields_ = [
            # The following 2 fields are NULL if SuppressBackgroundThread is FALSE.
            # Otherwise, they are functions which must be called appropriately to
            # replace the background thread.
            #
            # These should be called on the application's main message loop - i.e.
            # a message loop which is active for the lifetime of GDI+.
            # "NotificationHook" should be called before starting the loop,
            # and "NotificationUnhook" should be called after the loop ends.
            ("NotificationHook", NotificationHookProc),
            ("NotificationUnhook", NotificationUnhookProc)
        ]

    """
    // GDI+ initialization. Must not be called from DllMain - can cause deadlock.
    //
    // Must be called before GDI+ API's or constructors are used.
    //
    // token  - may not be NULL - accepts a token to be passed in the corresponding
    //          GdiplusShutdown call.
    // input  - may not be NULL
    // output - may be NULL only if input->SuppressBackgroundThread is FALSE.
    """

    GdiplusStartup = declare(gdiplus.GdiplusStartup, Status, PULONG_PTR, POINTER(GdiplusStartupInput), POINTER(GdiplusStartupOutput))

    """
    // GDI+ termination. Must be called before GDI+ is unloaded. 
    // Must not be called from DllMain - can cause deadlock.
    //
    // GDI+ API's may not be called after GdiplusShutdown. Pay careful attention
    // to GDI+ object destructors.
    """
    GdiplusShutdown = declare(gdiplus.GdiplusShutdown, VOID, ULONG_PTR)

    # REGION ***
