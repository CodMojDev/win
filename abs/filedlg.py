from win.commdlg import *
from .window import *

class FileDialog:
    def __init__(self, owner: int | HANDLE = NULL, show_help: bool = False,
                 filter: str = None, initial_dir: str = None, 
                 filter_index: int = 0, extra_flags: int = 0):
        self.open_file = tagOFNW()
        self.open_file.lStructSize = self.open_file.size()
        self.open_file.Flags = extra_flags
        self.open_file.Flags |= OFN_ENABLEHOOK
        self.lpfnHook = self.open_file.lpfnHook = LPOFNHOOKPROC(self.hook_proc)
        self.open_file.hwndOwner = owner
        
        if show_help:
            self.open_file.Flags |= OFN_SHOWHELP
            
        if filter is not None:
            filter = filter.replace('\\|', '\\%').replace('|', '\0').replace('\\%', '|')
            self.lpstrFilter = (WCHAR * len(filter))(*filter)
            self.open_file.lpstrFilter = i_cast(self.lpstrFilter, LPWSTR)
            self.open_file.nFilterIndex = filter_index
        
        self.lpstrFileTitle = create_unicode_buffer(4096)
        self.open_file.lpstrFileTitle = i_cast(self.lpstrFileTitle, LPWSTR)
        self.open_file.nMaxFileTitle = len(self.lpstrFileTitle)
        
        self.lpstrFile = create_unicode_buffer(16384)
        self.open_file.lpstrFile = i_cast(self.lpstrFile, LPWSTR)
        self.open_file.nMaxFile = len(self.lpstrFile)
        
        if initial_dir is not None:
            self.lpstrInitialDir = create_unicode_buffer(initial_dir)
            self.open_file.lpstrInitialDir = i_cast(self.lpstrInitialDir, LPWSTR)
    
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
        return bool(GetOpenFileNameW(self.open_file.ref()))
    
    def save(self) -> bool:
        return bool(GetSaveFileNameW(self.open_file.ref()))
    
    def on_message(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        return FALSE
    
    def hook_proc(self, hWnd: int, uMsg: int, wParam: int, lParam: int) -> int:
        return self.on_message(hWnd, uMsg, wParam, lParam)