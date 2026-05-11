from .window import *
from .core.io import MemoryIO

class Dialog(Window):
    def __init__(self, width: int, height: int):
        super().__init__()
        self._width = width
        self._height = height
        self._style &= ~WS_OVERLAPPEDWINDOW
        self._style |= WS_CAPTION | WS_SYSMENU
        self._parent = NULL
        self.on_unknown_message += self.Dialog_on_unknown_message
        self.on_close += self.on_close_dialog
        self.modal = True
        self.on_init_dialog = Event()
        self.on_destroy -= self.Window_on_destroy
    
    def end(self, ret: int = 0): 
        if self.modal:
            if not EndDialog(self, ret):
                raise WinException()
        else:
            self.destroy()
            app = Application()
            app.modeless_dialogs.remove(self.value)
            app.windows -= 1
            app.notify()
        
    def on_close_dialog(self):
        self.end(IDCANCEL)
    
    def Dialog_on_unknown_message(self, hwnd: int, message: int, wParam: int, lParam: int) -> int:
        if message == WM_INITDIALOG:
            self.value = hwnd
            if all(self.on_init_dialog.execute()):
                return TRUE
            return FALSE
        return None
    
    def wnd_proc_fallback(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int:
        return FALSE
    
    def create(self, x: int, y: int, window_name: str = 'Dialog', parent: int | HWND = NULL):
        buffer = (CHAR * 256)()
        pDlg = i_cast(buffer, LPDLGTEMPLATE)
        dlg = pDlg.contents
        dlg.x = x; dlg.y = y
        dlg.cx = self._width; dlg.cy = self._height
        dlg.style = self._style
        pData = PtrArithmetic.add(pDlg, 1)
        with MemoryIO(pData, len(buffer) - sizeof(DLGTEMPLATE)) as data:
            data.write_uint16(0)
            data.write_uint16(0)
            data.write((window_name + '\0').encode('utf-16-le'))
            data.write_uint16(8)
            data.write_uint16(0)
            data.write_uint16(0)
            data.write_uint16(0)
            data.write('MS Shell Dlg\0'.encode('utf-16-le'))
        self.pDlg = pDlg
        self._parent = parent
        self.dlg = dlg
        self._buffer = buffer
        if not self.modal:
            self.pfnWndProc = DLGPROC(self.window_proc)
            self.value = CreateDialogIndirectW(GetModuleHandleW(NULL), pDlg, parent, self.pfnWndProc)
            if not self.value:
                raise WinException()
            app = Application()
            app.modeless_dialogs.append(self.value)
            app.windows += 1
    
    def launch(self) -> int:
        if not self.modal:
            raise ValueError('dialog.launch() called while dialog.modal is false.')
        self.pfnWndProc = DLGPROC(self.window_proc)
        return DialogBoxIndirectW(GetModuleHandleW(NULL), self.pDlg, self._parent, self.pfnWndProc)