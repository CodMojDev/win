from .window import *

class TaskDialog(Window):
    config: TASKDIALOGCONFIG
    pfCallback: FARPROC
    pszFooter: IWideCharArray | None
    pszWindowTitle: IWideCharArray | None
    pszContent: IWideCharArray | None
    pButtons: IArray[TASKDIALOG_BUTTON] | None
    pRadioButtons: IArray[TASKDIALOG_BUTTON] | None
    pszVerificationText: IWideCharArray | None
    pszExpandedInformation: IWideCharArray | None
    pszExpandedControlText: IWideCharArray | None
    pszCollapsedControlText: IWideCharArray | None
    pszMainIcon: IWideCharArray | None
    pszMainInstruction: IWideCharArray | None
    pszFooterIcon: IWideCharArray | None
    
    on_dialog_button_clicked: MultiEvent
    on_dialog_created: MultiEvent
    on_dialog_destroyed: MultiEvent
    on_dialog_constructed: MultiEvent
    on_dialog_expando_button_clicked: MultiEvent
    on_dialog_help: MultiEvent
    on_dialog_hyperlink_clicked: MultiEvent
    on_dialog_navigated: MultiEvent
    on_dialog_radio_button_clicked: MultiEvent
    on_dialog_timer: MultiEvent
    on_dialog_verification_clicked: MultiEvent
    
    button_pressed: int
    radio_button: int
    verification_flag_checked: bool
    
    def __init__(self, owner: int | HANDLE = NULL, 
                 footer: str | None = None,
                 handle: WT_ADDRLIKE = NULL, 
                 common_buttons: int = 0,
                 title: str | None = None,
                 content: str | WT_ADDRLIKE = None,
                 buttons: Iterable[TASKDIALOG_BUTTON] = [],
                 default_button: int = 0,
                 default_radio_button: int = 0,
                 radio_buttons: Iterable[TASKDIALOG_BUTTON] = [],
                 verification_text: str | WT_ADDRLIKE = None,
                 expanded_info: str | WT_ADDRLIKE = None,
                 expanded_control_text: str | WT_ADDRLIKE = None,
                 collapsed_control_text: str | WT_ADDRLIKE = None,
                 main_icon: int | HANDLE | str = None,
                 footer_icon: int | HANDLE | str = None,
                 main_instruction: str | WT_ADDRLIKE = None,
                 width: int = 0, extra_flags: int = 0):
        super().__init__()
        
        # setup TASKDIALOGCONFIG size
        self.config = TASKDIALOGCONFIG()
        self.config.cbSize = TASKDIALOGCONFIG.size()
        self.pfCallback = self.config.pfCallback = PFTASKDIALOGCALLBACK(self.taskdialog_callback)
        
        if handle is None:
            handle = GetModuleHandleW(NULL)
        self.config.hInstance = handle
        self.config.hwndParent = owner
        self.config.dwCommonButtons = common_buttons
        
        if footer is not None:
            self.pszFooter = create_unicode_buffer(footer)
            self.config.pszFooter = i_cast(self.pszFooter, LPCWSTR)
        else:
            self.pszFooter = None
            
        if title is not None:
            self.pszWindowTitle = create_unicode_buffer(title)
            self.config.pszWindowTitle = i_cast(self.pszWindowTitle, LPCWSTR)
        else:
            self.pszWindowTitle = None
        
        if content is not None:
            if isinstance(content, str):
                self.pszContent = create_unicode_buffer(content)
            else:
                self.pszContent = content
            self.config.pszContent = i_cast(self.pszContent, LPCWSTR)
        else:
            self.pszContent = None
        
        if not buttons:
            self.pButtons = None
        else:
            self.pButtons = (TASKDIALOG_BUTTON*len(buttons))(*buttons)
            self.config.cButtons = len(buttons)
            self.config.pButtons = i_cast(self.pButtons, PTR(TASKDIALOG_BUTTON))
        
        self.config.nDefaultButton = default_button
        self.config.nDefaultRadioButton = default_radio_button
        
        if not radio_buttons:
            self.config.pRadioButtons = None
        else:
            self.pRadioButtons = (TASKDIALOG_BUTTON*len(radio_buttons))(*radio_buttons)
            self.config.cRadioButtons = len(radio_buttons)
            self.config.pRadioButtons = i_cast(self.pRadioButtons, PTR(TASKDIALOG_BUTTON))
        
        if verification_text is not None:
            if isinstance(verification_text, str):
                self.pszVerificationText = create_unicode_buffer(verification_text)
            else:
                self.pszVerificationText = verification_text
            self.config.pszVerificationText = i_cast(self.pszVerificationText, LPCWSTR)
        else:
            self.pszVerificationText = None
            
        if expanded_info is not None:
            if isinstance(expanded_info, str):
                self.pszExpandedInformation = create_unicode_buffer(expanded_info)
            else:
                self.pszExpandedInformation = expanded_info
            self.config.pszExpandedInformation = i_cast(self.pszExpandedInformation, LPCWSTR)
        else:
            self.pszExpandedInformation = None
        
        if expanded_control_text is not None:
            if isinstance(expanded_control_text, str):
                self.pszExpandedControlText = create_unicode_buffer(expanded_control_text)
            else:
                self.pszExpandedControlText = expanded_control_text
            self.config.pszExpandedControlText = i_cast(self.pszExpandedControlText, LPCWSTR)
        else:
            self.pszExpandedControlText = None
        
        if collapsed_control_text is not None:
            if isinstance(collapsed_control_text, str):
                self.pszCollapsedControlText = create_unicode_buffer(collapsed_control_text)
            else:
                self.pszCollapsedControlText = collapsed_control_text
            self.config.pszCollapsedControlText = i_cast(self.pszCollapsedControlText, LPCWSTR)
        else:
            self.pszCollapsedControlText = None
        
        if main_instruction is not None:
            if isinstance(main_instruction, str):
                self.pszMainInstruction = create_unicode_buffer(main_instruction)
            else:
                self.pszMainInstruction = main_instruction
            self.config.pszMainInstruction = i_cast(self.pszMainInstruction, LPCWSTR)
        else:
            self.pszMainInstruction = None
        
        if main_icon is not None:
            extra_flags |= TDF_USE_HICON_MAIN
            if isinstance(main_icon, str):
                self.pszMainIcon = create_unicode_buffer(main_icon)
                self.config.pszMainIcon = i_cast(self.pszMainIcon, LPCWSTR)
            else:
                self.config.hMainIcon = main_icon
                self.pszMainIcon = None
        else:
            self.pszMainIcon = None
        
        if footer_icon is not None:
            extra_flags |= TDF_USE_HICON_FOOTER
            if isinstance(footer_icon, str):
                self.pszFooterIcon = create_unicode_buffer(footer_icon)
                self.config.pszFooterIcon = i_cast(self.pszFooterIcon, LPCWSTR)
            else:
                self.config.hFooterIcon = footer_icon
                self.pszFooterIcon = None
        else:
            self.pszFooterIcon = None
        
        # create the task dialog events
        self.on_dialog_button_clicked = MultiEvent()
        self.on_dialog_created = MultiEvent()
        self.on_dialog_destroyed = MultiEvent()
        self.on_dialog_constructed = MultiEvent()
        self.on_dialog_expando_button_clicked = MultiEvent()
        self.on_dialog_help = MultiEvent()
        self.on_dialog_hyperlink_clicked = MultiEvent()
        self.on_dialog_navigated = MultiEvent()
        self.on_dialog_radio_button_clicked = MultiEvent()
        self.on_dialog_timer = MultiEvent()
        self.on_dialog_verification_clicked = MultiEvent()
        
        # set the TASKDIALOGCONFIG flags
        self.config.dwFlags = extra_flags
        
    def create(self):
        nButtonPressed = INT()
        nRadioButton = INT()
        fVerificationFlagChecked = BOOL()
        
        hr = TaskDialogIndirect(
            self.config.ref(), byref(nButtonPressed), 
            NULL, NULL)
        if FAILED(hr): raise COMError(hr)
        
        self.button_pressed = nButtonPressed.value
        self.radio_button = nRadioButton.value
        self.verification_flag_checked = fVerificationFlagChecked.value != FALSE
        
    def taskdialog_callback(self, hwnd: int, msg: int, wParam: int, lParam: int, dwUnused: int) -> int:
        if msg == TDN_DIALOG_CONSTRUCTED:
            self.value = hwnd
            self.on_dialog_constructed.execute()
        elif msg == TDN_CREATED:
            self.on_dialog_created.execute()
        elif msg == TDN_DESTROYED:
            self.on_dialog_destroyed.execute()
        elif msg == TDN_EXPANDO_BUTTON_CLICKED:
            # call the handler, wParam=fExpanded
            self.on_dialog_expando_button_clicked.execute(wParam != FALSE)
        elif msg == TDN_HELP:
            # call the handler
            self.on_dialog_help.execute()
        elif msg == TDN_HYPERLINK_CLICKED:
            # call the handler, lParam=lpszURL
            self.on_dialog_hyperlink_clicked.execute(i_cast_value(lParam, LPCWSTR).value if lParam else None)
        elif msg == TDN_NAVIGATED:
            # call the handler
            self.on_dialog_navigated.execute()
        elif msg == TDN_RADIO_BUTTON_CLICKED:
            # call the handler, wParam=iRadioButtonID
            self.on_dialog_radio_button_clicked.execute(wParam)
        elif msg == TDN_TIMER:
            # call the handler, wParam=dwMsSinceCreation
            self.on_dialog_timer.execute(wParam)
        elif msg == TDN_VERIFICATION_CLICKED:
            # call the handler, wParam=fVerificationBoxChecked
            self.on_dialog_verification_clicked.execute(wParam != FALSE)
        elif msg == TDN_BUTTON_CLICKED:
            # call the handler, wParam=dwID, result=S_FALSE/S_OK
            if self.on_dialog_button_clicked.execute(wParam):
                return S_OK
            else:
                return S_FALSE
        return S_OK