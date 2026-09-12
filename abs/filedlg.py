from win.commdlg import *
from .window import *

class FileDialog(Window):
    """
    File dialog class.
    """
    
    open_file: tagOFNW
    on_message: SingleEvent
    lpfnHook: FARPROC
    lpstrFileTitle: IWideCharArray
    lpstrFile: IWideCharArray
    lpstrInitialDir: IWideCharArray | None
    lpstrFilter: IWideCharArray | None
    
    def __init__(self, owner: int | HANDLE = NULL, show_help: bool = False,
                 filter: str = None, initial_dir: str = None, 
                 filter_index: int = 0, extra_flags: int = 0):
        super().__init__()
        
        # initialize OFNW structure
        self.open_file = tagOFNW()
        self.open_file.lStructSize = self.open_file.size()
        
        # initialize OFN flags
        self.open_file.Flags = extra_flags
        self.open_file.Flags |= OFN_ENABLEHOOK
        
        # set hook
        self.lpfnHook = self.open_file.lpfnHook = LPOFNHOOKPROC(self.hook_proc)
        
        # set owner
        self.open_file.hwndOwner = owner
        
        # help button support
        if show_help:
            self.open_file.Flags |= OFN_SHOWHELP
            
        # filter support
        if filter is not None:
            # escape the "|" with "\0" and save "\|" to resulting "|"
            filter = filter.replace('\\|', '\\%').replace('|', '\0').replace('\\%', '|')
            
            # allocate filter and 
            self.lpstrFilter = (WCHAR * len(filter))(*filter)
            self.open_file.lpstrFilter = i_cast(self.lpstrFilter, LPWSTR)
            self.open_file.nFilterIndex = filter_index
        
        # allocate file title buffer
        self.lpstrFileTitle = create_unicode_buffer(4096)
        self.open_file.lpstrFileTitle = i_cast(self.lpstrFileTitle, LPWSTR)
        self.open_file.nMaxFileTitle = len(self.lpstrFileTitle)
        
        # allocate file path buffer
        self.lpstrFile = create_unicode_buffer(16384)
        self.open_file.lpstrFile = i_cast(self.lpstrFile, LPWSTR)
        self.open_file.nMaxFile = len(self.lpstrFile)
        
        # support for initial directory
        if initial_dir is not None:
            self.lpstrInitialDir = create_unicode_buffer(initial_dir)
            self.open_file.lpstrInitialDir = i_cast(self.lpstrInitialDir, LPWSTR)
        else:
            self.lpstrInitialDir = None
        
        # event for dlgproc handling
        self.on_message = SingleEvent()
    
    @property
    def file_title(self) -> str:
        file_title = i_cast(self.open_file.lpstrFileTitle, PTR(CHAR * (self.open_file.nMaxFileTitle * sizeof(WCHAR)))).contents.raw.decode('utf-16-le')
        return file_title[:file_title.find('\0\0')]
    
    @property
    def file(self) -> str:
        file = i_cast(self.open_file.lpstrFile, PTR(CHAR * (self.open_file.nMaxFile * sizeof(WCHAR)))).contents.raw.decode('utf-16-le')
        return file[:file.find('\0\0')]
    
    @property
    def files(self) -> tuple[str, ...]:
        if (self.open_file.Flags & OFN_ALLOWMULTISELECT) == 0:
            return (self.file,)
        
        directory, *files = self.file.split('\0')
        for i, file in enumerate(files):
            files[i] = directory + '\\' + file
        
        return tuple(files)
    
    @property
    def file_titles(self) -> tuple[str, ...]:
        if (self.open_file.Flags & OFN_ALLOWMULTISELECT) == 0:
            return (self.file_title,)
        
        return tuple(self.file.split('\0')[1:])
    
    def open(self) -> bool:
        """
        Open "Open file" dialog.
        """
        result = GetOpenFileNameW(self.open_file.ref()) != FALSE
        if not result:
            code = CommDlgExtendedError()
            if code != 0:
                raise CommonDialogError(code)
        return result
    
    def save(self) -> bool:
        """
        Open "Save as..." dialog.
        """
        result = GetSaveFileNameW(self.open_file.ref()) != FALSE
        if not result:
            code = CommDlgExtendedError()
            if code != 0:
                raise CommonDialogError(code)
        return result
    
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        if uMsg == WM_INITDIALOG:
            self.value = hWnd
        if self.on_message.empty(): return FALSE
        return self.on_message.execute(hWnd, uMsg, wParam, lParam)