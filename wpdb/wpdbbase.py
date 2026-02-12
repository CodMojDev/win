from gzip import GzipFile, open as gzip_open
from typing import ClassVar
    
class WPDBFile:
    _mode_: ClassVar[str]
    file: GzipFile
    
    def __init__(self, file_path: str):
        self.file = gzip_open(file_path, self._mode_+'b')
    
    def __del__(self):
        if not self.file.closed:
            self.file.close()
            
    def end(self):
        if not self.file.closed:
            self.file.close()