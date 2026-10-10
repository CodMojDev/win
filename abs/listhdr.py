from .window import *
from .imagelist import *

class HeaderItemInfo(HDITEMW):
    @property
    def width(self) -> int:
        return self.cx
    
    @width.setter
    def width(self, width: int):
        self.cx = width
        self.mask |= HDI_WIDTH
    
    @property
    def text(self) -> int:
        return self.pszText.value
    
    @text.setter
    def text(self, text: str):
        self._buffer_cache = create_unicode_buffer(text)
        self.pszText = i_cast(self._buffer_cache, LPWSTR)
        self.cchTextMax = len(text)
        self.mask |= HDI_TEXT
    
    @property
    def bitmap(self) -> Bitmap | None:
        return Bitmap.foreign_owner(self.hbm)
    
    @bitmap.setter
    def bitmap(self, bitmap: int | HANDLE):
        self.hbm = bitmap
        self.mask |= HDI_BITMAP
    
    @property
    def image(self) -> int:
        return self.iImage
    
    @image.setter
    def image(self, image: int):
        self.iImage = image
        self.mask |= HDI_IMAGE
    
    @property
    def order(self) -> int:
        return self.iOrder
    
    @order.setter
    def order(self, order: int):
        self.iOrder = order
        self.mask |= HDI_ORDER
    
    @property
    def format(self) -> int:
        return self.fmt
    
    @format.setter
    def format(self, format: int):
        self.fmt = format
        self.mask |= HDI_FORMAT
    
    @property
    def parameter(self) -> int:
        return self.lParam
    
    @parameter.setter
    def parameter(self, parameter: int):
        self.lParam = parameter
        self.mask |= HDI_LPARAM

class ListHeader(Control):
    class Item:
        """
        Class representing ListHeader item/column.
        """
        
        hdr: 'ListHeader'
        index: int
        
        def __init__(self, hdr: 'ListHeader', index: int):
            self.hdr = hdr
            self.index = index
            
        @property
        def rect(self) -> Rect:
            rect = Rect()
            if not self.hdr.send(HDM_GETITEMRECT, self.index, rect.ref()):
                raise WinException()
            return rect
            
        @property
        def dropdown_rect(self) -> Rect:
            rect = Rect()
            if not self.hdr.send(HDM_GETITEMDROPDOWNRECT, self.index, rect.ref()):
                raise WinException()
            return rect
        
        def delete(self):
            """
            Delete the header item (column).
            """
            if not self.hdr.send(HDM_DELETEITEM, self.index):
                raise WinException()
            
        def create_drag_image(self) -> ImageList:
            """
            Create the image list with drag image of an header item.
            """
            return ImageList.foreign_owner(self.hdr.send(HDM_CREATEDRAGIMAGE, self.index))
    
        def get(self, mask: int | None = None) -> HDITEMW:
            """
            Get the information about list header item.
            """
            hdi = HDITEM()
            if mask is None:
                mask = (HDI_BITMAP | HDI_FILTER | HDI_DI_SETITEM |
                        HDI_LPARAM | HDI_HEIGHT | HDI_WIDTH |
                        HDI_STATE | HDI_ORDER | HDI_FORMAT |
                        HDI_IMAGE | HDI_TEXT)
            hdi.mask = mask
            if mask & HDI_TEXT:
                buffer = create_unicode_buffer(256)
                hdi.cchTextMax = 256
                setattr(hdi, '_buffer_cache', buffer)
                hdi.pszText = i_cast(buffer, LPWSTR)
            if not self.hdr.send(HDM_GETITEM, self.index, hdi.ref()):
                raise WinException()
            if mask & HDI_TEXT:
                if not PtrArithmetic.equals(hdi.pszText, buffer):
                    delattr(hdi, '_buffer_cache')
            return hdi
    
        def set(self, item: HDITEMW, mask: int | None = None):
            """
            Get the information about list header item.
            """
            if mask is None:
                if not item.mask:
                    mask = (HDI_BITMAP | HDI_FILTER | HDI_DI_SETITEM |
                            HDI_LPARAM | HDI_HEIGHT | HDI_WIDTH |
                            HDI_STATE | HDI_ORDER | HDI_FORMAT |
                            HDI_IMAGE | HDI_TEXT)
                else:
                    mask = item.mask
            item.mask = mask
            if not self.hdr.send(HDM_SETITEM, self.index, item.ref()):
                raise WinException()
    
    class Items:
        hdr: 'ListHeader'
        
        def __init__(self, hdr: 'ListHeader'):
            self.hdr = hdr
            
        def count(self) -> int:
            """
            Get the count of items in list header.
            """
            return self.hdr.send(HDM_GETITEMCOUNT)
    
        @property
        def focused(self) -> 'ListHeader.Item':
            return ListHeader.Item(self.hdr, self.hdr.send(HDM_GETFOCUSEDITEM))
    
        def from_order(self, order: int) -> 'ListHeader.Item':
            """
            Get the list header item by its order.
            """
            return ListHeader.Item(self.hdr, self.hdr.send(HDM_ORDERTOINDEX, order))
    
        def insert(self, item: HDITEMW, index: int = -1) -> 'ListHeader.Item':
            """
            Get the information about list header item.
            """
            if index == -1:
                index = self.count()
            i = self.hdr.send(HDM_INSERTITEM, index, item.ref())
            if i == -1:
                raise WinException()
            return ListHeader.Item(self.hdr, i)
    
    class Filter:
        hdr: 'ListHeader'
        
        def __init__(self, hdr: 'ListHeader'):
            self.hdr = hdr
            
        def clear(self, value: int):
            """
            Clear the list header filter.
            """
            self.hdr.send(HDM_CLEARFILTER, value)
            
        def edit(self, value: int, discard: bool):
            """
            Edit the list header filter.
            """
            self.hdr.send(HDM_EDITFILTER, value, discard)
    
        def set_change_timeout(self, change_timeout: int):
            """
            Set the change timeout of list header filter.
            """
            self.hdr.send(HDM_SETFILTERCHANGETIMEOUT, 0, change_timeout)
    
    items: Items
    filter: Filter
    
    def __init__(self):
        super().__init__()
        self.class_name = WC_HEADERW
    
    def headless_init(self):
        super().headless_init()
        self.items = self.Items(self)
        self.filter = self.Filter(self)
        
    def hit(self, x: int, y: int) -> tuple[int, Item | None]:
        """
        Hit-test the list header control.
        """
        hdhti = HDHITTESTINFO()
        hdhti.pt = Point(x, y)
        if self.send(HDM_HITTEST, 0, hdhti.ref()) == 1:
            return (hdhti.iItem, None)
        return (hdhti.iItem, ListHeader.Item(self, hdhti.iItem))
    
    @property
    def image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(HDM_GETIMAGELIST, HDSIL_NORMAL))
    
    @image_list.setter
    def image_list(self, image_list: int | HANDLE):
        self.send(HDM_SETIMAGELIST, HDSIL_NORMAL, image_list)
    
    @property
    def state_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(HDM_GETIMAGELIST, HDSIL_STATE))
    
    @state_image_list.setter
    def state_image_list(self, state_image_list: int | HANDLE):
        self.send(HDM_SETIMAGELIST, HDSIL_STATE, state_image_list)
        
    @property
    def bitmap_margin(self) -> int:
        return self.send(HDM_GETBITMAPMARGIN)
    
    @bitmap_margin.setter
    def bitmap_margin(self, bitmap_margin: int):
        self.send(HDM_SETBITMAPMARGIN, bitmap_margin)
        
    @property
    def overflow_rect(self) -> Rect:
        rect = Rect()
        if not self.send(HDM_GETOVERFLOWRECT, 0, rect.ref()):
            raise WinException()
        return rect
    
    def layout(self, rect: RECT) -> WINDOWPOS:
        """
        Set the given layout and retrieve `WINDOWPOS`.
        """
        hdl = HDLAYOUT()
        wp = WINDOWPOS()
        hdl.prc = rect.ptr()
        hdl.pwpos = wp.ptr()
        if not self.send(HDM_LAYOUT, 0, hdl.ref()):
            raise WinException()
        return wp
    
    @property
    def order_array(self) -> list[int]:
        count = self.items.count()
        array = (INT*count)()
        if not self.send(HDM_GETORDERARRAY, count, array) and count != 0:
            raise WinException()
        return list(array)
    
    @order_array.setter
    def order_array(self, order_array: Iterable[int]):
        count = self.items.count()
        array = (INT*count)(*order_array)
        if not self.send(HDM_SETORDERARRAY, count, array) and count != 0:
            raise WinException()