from .window import *
from win.commdlg import *

commdlg_FindReplace = Messages[FINDMSGSTRINGW]

class FindReplaceDialog(Window):
    """
    Find/Replace dialog class.
    """
    
    on_message: SingleEvent
    lpfnHook: FARPROC
    findreplace: FINDREPLACEW
    lpTemplateName: IWideCharArray | None
    lpstrFindWhat: IWideCharArray
    lpstrReplaceWith: IWideCharArray
    on_action: MultiEvent
    
    
    def __init__(self, owner: int | HANDLE, find_what: str | None = None,
                 replace_with: str | None = None, 
                 extra_flags: int = 0, 
                 handle: WT_ADDRLIKE = None,
                 template: str | None = None):
        super().__init__()
        
        # setup FINDREPLACEW structure
        self.findreplace = FINDREPLACEW()
        self.findreplace.lStructSize = FINDREPLACEW.size()
        self.findreplace.lpfnHook = self.lpfnHook = LPFRHOOKPROC(self.hook_proc)
        self.findreplace.hwndOwner = owner
        # hook is automatically set
        extra_flags |= FR_ENABLEHOOK
        
        # if template is given, then adjust it and add flag
        if template is not None:
            extra_flags |= FR_ENABLETEMPLATE
            self.lpTemplateName = create_unicode_buffer(template)
            self.findreplace.lpTemplateName = i_cast(self.lpTemplateName, LPCWSTR)
        # if instance handle is given, then add it and add flag
        if handle is not None:
            extra_flags |= FR_ENABLETEMPLATEHANDLE
            self.findreplace.hInstance = handle
        # allocate "find what" and "replace with" arrays
        self.lpstrFindWhat = create_unicode_buffer(256)
        self.lpstrReplaceWith = create_unicode_buffer(256)
        # set their fields as cast from buffer to LPWSTR
        self.findreplace.lpstrFindWhat = i_cast(self.lpstrFindWhat, LPWSTR)
        self.findreplace.lpstrReplaceWith = i_cast(self.lpstrReplaceWith, LPWSTR)
        # set their size fields as 256 wchars
        self.findreplace.wFindWhatLen = 256
        self.findreplace.wReplaceWithLen = 256
        # if given init value of "find what", when init it
        if find_what is not None:
            self.lpstrFindWhat.value = find_what
        # if given init value of "replace with", when init it
        if replace_with is not None:
            self.lpstrReplaceWith.value = replace_with
        # adjust flags into FINDREPLACEW structure
        self.findreplace.Flags = extra_flags
        
        # common events for Find/Replace dialog
        self.on_message = SingleEvent()
        self.on_action = MultiEvent()
        
        # if owner is WinAbs-window and managed, then subscribe to its findreplace message
        if isinstance(owner, Window) and Abs.managed(owner):
            owner.on_unknown_message += self.parent_on_unknown_message
        
    def find(self):
        """
        Open the "Find text" dialog.
        """
        self.value = FindTextW(self.findreplace.ref())
        if not self.value: raise CommonDialogError()
        
    def replace(self):
        """
        Open the "Replace text" dialog.
        """
        self.value = ReplaceTextW(self.findreplace.ref())
        if not self.value: raise CommonDialogError()
        
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        if self.on_message.empty(): return FALSE
        return self.on_message.execute(hWnd, uMsg, wParam, lParam)
    
    def parent_on_unknown_message(self, hwnd: int, msg: int, wParam: int, lParam: int) -> int | None:
        if msg == commdlg_FindReplace:
            self.on_action.execute(self.findreplace.Flags)
            return 0
        return None
    
    def set_operation_result(self, flags: int):
        """
        Set the operation result of Find/Replace dialog.
        """
        self.send(FRM_SETOPERATIONRESULT, flags, self.findreplace.ref())
        
    def set_operation_result_text(self, text: str):
        """
        Set the operation text of Find/Replace dialog.
        """
        self.send(FRM_SETOPERATIONRESULTTEXT, 0, text)