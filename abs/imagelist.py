from .window import *

class ImageList(Handle):
    """
    Class, representing Win32 Image list object (comctl32).
    """
    
    @classmethod
    def create(cls, width: int, height: int, initial: int, 
               flags: int = ILC_COLOR32 | ILC_MASK, grow: int = 0):
        image_list = cls(ImageList_Create(width, height, flags, initial, grow))
        if not image_list.value:
            raise WinException()
        return image_list
    
    def close(self):
        ImageList_Destroy(self)
        self._closed = True
    
    @overload
    def add(self, hIcon: Icon, cache: ICacheAccessor[int] | None = None) -> int: 
        """
        Add icon to image list.
        """
    
    @overload
    def add(self, hBitmap: int | HANDLE, hBmMask: int | HANDLE = NULL, cache: ICacheAccessor[int] | None = None) -> int:
        """
        Add bitmap to image list.
        """
    
    def add(self, var: int | HANDLE, hBmMask: int | HANDLE = NULL, cache: ICacheAccessor[int] | None = None) -> int:
        if isinstance(var, Icon):
            result = ImageList_AddIcon(self, var)
        else:
            result = ImageList_Add(self, var, hBmMask)
        if result == -1: raise WinException()
        if cache is not None: cache.cache(result)
        return result
    
    def add_masked(self, bitmap: int | HANDLE, color: Color.IColor | int, cache: ICacheAccessor[int] | None = None) -> int:
        result = ImageList_AddMasked(self, bitmap, int(color))
        if result == -1: raise WinException()
        if cache is not None: cache.cache(result)
        return result
    
    def __getitem__(self, index: int):
        return Icon.foreign_owner(ImageList_GetIcon(self, index))
    
    def __setitem__(self, index: int, value: int | HANDLE | Bitmap):
        if isinstance(value, Bitmap):
            value = Icon.from_bitmap(value)
        ImageList_ReplaceIcon(self, index, value)