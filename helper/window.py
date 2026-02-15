#
# Deprecated
#

raise RuntimeError()

if False:
    from ..winuser import *
    from .base_exception import *

    class WindowClass(WNDCLASS):
        def __init__(self, name):
            self.hInstance = HINSTANCE(0x400000) 
            self.lpszClassName = name
            self.hCursor = LoadCursorW(NULL, cast(IDC_ARROW, LPCWSTR))
            self.hbrBackground = HBRUSH(COLOR_WINDOW + 1)
            self.lpszMenuName = cast(IDI_INFORMATION, LPWSTR)

        def register(self):
            if self.registered:
                raise ClassAlreadyRegisteredError("Class already registered!")
            if RegisterClassW(byref(self)):
                self.registered = True
            else:
                raise ClassRegistrationError("Class registration failed!")
        
        def unregister(self):
            if not self.registered:
                raise ClassNotRegisteredError("Class not registered!")
            if UnregisterClass(self.lpszClassName, self.hInstance):
                self.registered = False
            else:
                raise ClassUnregistrationError("Class unregistration failed!")
        
        def set_instance_handle(self, handle):
            if not self.registered:
                self.hInstance = handle
                return self
            else:
                raise ClassAlreadyRegisteredError("Class already registered!")

        def set_class_name(self, name):
            if not self.registered:
                self.lpszClassName = name
                return self
            else:
                raise ClassAlreadyRegisteredError("Class already registered!")
        
        def set_icon(self, name):
            if not self.registered:
                self

    class Window:
        def __init__(self): ...