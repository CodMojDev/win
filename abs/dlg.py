from .window import *
from .core.io import MemoryIO

class Dialog(Window):
    """
    Class, wrapping functionality of Win32 Dialog window.
    """
    
    def __init__(self, width: int, height: int, himetric: bool = False):
        super().__init__()
        
        # predefined parameters
        self._width = width
        self._height = height
        self._parent = NULL
        self._himetric = himetric
        
        # dialog window styles
        self._style &= ~WS_OVERLAPPEDWINDOW
        self._style |= WS_CAPTION | WS_SYSMENU
        
        # bind dialog handlers to the window events
        self.on_unknown_message += self.Dialog_on_unknown_message
        self.on_close += self.on_close_dialog
        
        # remove standard window destroy procedure
        self.on_destroy -= self.Window_on_nc_destroy
        
        # dialog is modal by default
        self.modal = True
        
        # dialog-specific events
        self.on_init_dialog = Event()
    
    def end(self, ret: int = 0): 
        """
        End the modal or modeless dialog.
        """
        
        if self.modal:
            if not EndDialog(self, ret):
                raise WinException()
        else: # dialog is modeless
            self.destroy() # modeless dialogs destroyed by dialog.destroy()
            
            app = Application()
            # remove the modeless dialog from application-held list
            app.modeless_dialogs.remove(self.value)
            # notify application about app.windows changed
            app.windows -= 1
            app.notify()
        
    def on_close_dialog(self):
        # gracefully end the dialog
        self.end(IDCANCEL)
    
    def Dialog_on_unknown_message(self, hwnd: int, message: int, wParam: int, lParam: int) -> int:
        # handle the WM_INITDIALOG
        if message == WM_INITDIALOG:
            self.value = hwnd
            # if all handlers, returned True, when return TRUE
            if all(self.on_init_dialog.execute()):
                return TRUE
            return FALSE # FALSE otherwise
        return None
    
    def wnd_proc_fallback(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return FALSE # Dialog procedure is not for DefWindowProc.
    
    def create(self, x: int, y: int, window_name: str = 'Dialog', parent: int | HWND = NULL):
        """
        Create the modal or modeless dialog.
        """
        
        # allocate DLGTEMPLATE structure as buffer of 256 bytes
        buffer = (CHAR * 256)()
        pDlg = i_cast(buffer, LPDLGTEMPLATE)
        dlg = pDlg.contents
        
        # save refs on dialog structure and dialog buffer for GC safety
        self.dlg = dlg
        self._buffer = buffer
        
        # save the parent argument and dialog pointer for modal dialog
        self._parent = parent
        self.pDlg = pDlg
        
        # setup dialog template coordinates
        dlg.x = x
        dlg.y = y
        
        # setup dialog template size
        dlg.cx = self._width
        dlg.cy = self._height
        
        # setup dialog template style
        dlg.style = self._style
        
        # flexible data section starts
        pData = PtrArithmetic.add(pDlg, 1)
        
        # directly write to after-structure data with MemoryIO
        with MemoryIO(pData, len(buffer) - sizeof(DLGTEMPLATE)) as data:
            # write the dialog data
            data.write_uint16(0) # dialog menu
            data.write_uint16(0) # class
            data.write((window_name + '\0').encode('utf-16-le')) # write the dialog window name
            # write the font data
            data.write_uint16(8) # height
            data.write_uint16(0) # weight
            data.write_uint16(0) # italic
            data.write_uint16(0) # charset
            data.write('MS Shell Dlg\0'.encode('utf-16-le')) # write the font name
        
        if not self.modal: # if dialog is modeless, when create it
            # setup dialog procedure
            self.pfnWndProc = DLGPROC(self.window_proc)
            
            # create the modeless dialog and assign HWND to self
            self.value = CreateDialogIndirectW(GetModuleHandleW(NULL), pDlg, parent, self.pfnWndProc)
            if not self.value:
                raise WinException()
            
            # append modeless dialog HWND into application-held list and increment app.windows
            app = Application()
            app.modeless_dialogs.append(self.value)
            app.windows += 1
    
    def launch(self) -> int:
        """
        Launch the modal dialog.
        """
        
        if not self.modal:
            raise ValueError('dialog.launch() called while dialog.modal is false.')
        
        # setup the dialog procedure
        self.pfnWndProc = DLGPROC(self.window_proc)
        # create and launch the modal dialog
        return DialogBoxIndirectW(
            GetModuleHandleW(NULL), 
            self.pDlg, self._parent, 
            self.pfnWndProc)