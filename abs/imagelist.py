from .window import *

class ImageList(Handle):
    def __init__(self, width: int, height: int, initial: int, 
                 flags: int = ILC_COLOR32 | ILC_MASK, grow: int = 0):
        super().__init__()
        self.value = ImageList_Create(width, height, flags, initial, grow)
        if not self.value:
            raise WinException()
    
    def close(self):
        ImageList_Destroy(self)
        self._closed = True
    
    @overload
    def add(self, hIcon: Icon) -> int: ...
    
    @overload
    def add(self, hBitmap: int | HANDLE, hBmMask: int | HANDLE = NULL) -> int: ...
    
    def add(self, var: int | HANDLE, hBmMask: int | HANDLE = NULL) -> int:
        if isinstance(var, Icon):
            result = ImageList_AddIcon(self, var)
        else:
            result = ImageList_Add(self, var, hBmMask)
        if result == -1: raise WinException()
        return result
    
    def __getitem__(self, index: int):
        return Icon.foreign_owner(ImageList_GetIcon(self, index))
    
    def __setitem__(self, index: int, value: int | HANDLE | Bitmap):
        if isinstance(value, Bitmap):
            value = Icon.from_bitmap(value)
        ImageList_ReplaceIcon(self, index, value)