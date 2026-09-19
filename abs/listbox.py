from .window import *

class ListBox(Control):
    class Item:
        box: 'ListBox'
        index: int
        
        def __init__(self, box: 'ListBox', index: int):
            self.box = box
            self.index = index
            
        def select(self):
            """
            Select the listbox item.
            """
            self.box.send(LB_SETSEL, TRUE, self.index)
            
        def deselect(self):
            """
            Deselect the listbox item.
            """
            self.box.send(LB_SETSEL, FALSE, self.index)
            
        @property
        def text(self) -> str:
            length = self.box.send(LB_GETTEXTLEN)
            buffer = create_unicode_buffer(length)
            self.box.send(LB_GETTEXT, self.index, buffer)
            return buffer.value
        
        @property
        def data(self) -> int:
            value = self.box.send(LB_GETITEMDATA, self.index)
            if value == LB_ERR:
                raise WinException()
            return value
        
        @data.setter
        def data(self, data: WT_ADDRLIKE):
            data = PtrUtil.get_address(data)
            result = self.box.send(LB_SETITEMDATA, self.index, data)
            if result == LB_ERR:
                raise WinException()
            
        def anchor(self):
            """
            Anchor the item.
            """
            self.box.send(LB_SETANCHORINDEX, self.index)
            
        def focus(self):
            """
            Gain focus (set caret index) to the item.
            """
            self.box.send(LB_SETCARETINDEX, self.index, FALSE)
            
        @property
        def rect(self) -> Rect:
            rect = Rect()
            if self.box.send(LB_GETITEMRECT, self.index, rect.ref()) == LB_ERR:
                raise WinException()
            return rect
        
        def delete(self):
            """
            Delete the item.
            """
            if self.box.send(LB_DELETESTRING, self.index) == LB_ERR:
                raise WinException()
            
        def select_range(self, count: int):
            """
            Select the range from this item to this+count.
            """
            self.select_to(self.index+count)
            
        def deselect_range(self, count: int):
            """
            Select the range from this item to this+count.
            """
            self.deselect_to(self.index+count)
            
        def select_to(self, item: TUnion['ListBox.Item', int]):
            """
            Select the range from this to item.
            """
            if isinstance(item, ListBox.Item):
                item = item.index
            index = self.index
            if index >= item:
                index, item = item, index
            if self.box.send(LB_SELITEMRANGEEX, index, item) == LB_ERR:
                raise WinException()
            
        def deselect_to(self, item: TUnion['ListBox.Item', int]):
            """
            Deselect the range from this to item.
            """
            if isinstance(item, ListBox.Item):
                item = item.index
            index = self.index
            if index <= item:
                index, item = item, index
            if self.box.send(LB_SELITEMRANGEEX, index, item) == LB_ERR:
                raise WinException()
            
        @property
        def item_height(self) -> int:
            result = self.box.send(LB_GETITEMHEIGHT, self.index)
            if result == LB_ERR:
                raise WinException()
            return result
    
    class Selection:
        box: 'ListBox'
        
        def __init__(self, box: 'ListBox'):
            self.box = box
            
        def items(self) -> list['ListBox.Item']:
            """
            Get the multiple selected items.
            """
            count = self.box.send(LB_GETSELCOUNT)
            if count == LB_ERR:
                item = self.item()
                if item is None:
                    return []
                return [item]
            buffer = (INT * count)()
            self.box.send(LB_GETSELITEMS, count, buffer)
            result = []
            for i in buffer:
                result.append(ListBox.Item(self.box, i))
            return result
            
        def item(self) -> TUnion['ListBox.Item', None]:
            """
            Get the selected item.
            """
            index = self.box.send(LB_GETSEL)
            if index == LB_ERR:
                return None
            if index == 0:
                style = self.box.style
                if (style & LBS_EXTENDEDSEL) or (style & LBS_MULTIPLESEL):
                    if self.count() in (LB_ERR, 0):
                        return None
            return ListBox.Item(self, index)
        
        def count(self) -> int:
            """
            Get the selection count in the listbox.
            """
            result = self.box.send(LB_GETSELCOUNT)
            if result == LB_ERR:
                return 1
            return result
    
        def select_all(self):
            """
            Select all items.
            """
            self.box.send(LB_SETSEL, TRUE, -1)
    
        def deselect_all(self):
            """
            Deselect all items.
            """
            self.box.send(LB_SETSEL, FALSE, -1)
        
        def has(self) -> bool:
            """
            Check if anything in listbox is selected.
            """
            style = self.box.style
            if (style & LBS_EXTENDEDSEL) or (style & LBS_MULTIPLESEL):
                if self.count() in (LB_ERR, 0):
                    return False
            return self.box.send(LB_GETSEL) != LB_ERR
        
        def anchor(self) -> TUnion['ListBox.Item', None]:
            """
            Get the anchor item.
            """
            count = self.box.send(LB_GETSELCOUNT)
            if count in (LB_ERR, 0):
                return None
            index = self.box.send(LB_GETANCHORINDEX)
            if index == LB_ERR:
                return None
            return ListBox.Item(self.box, index)
        
        def focus(self) -> TUnion['ListBox.Item', None]:
            """
            Get the focused item (get caret index).
            """
            index = self.box.send(LB_GETCARETINDEX)
            if index == LB_ERR:
                return None
            if self.count() == 0:
                return None
            return ListBox.Item(self.box, index)
    
    class Items:
        class Iterator:
            box: 'ListBox'
            index: int
            count: int
            
            def __init__(self, box: 'ListBox', index: int = 0):
                self.box = box
                self.index = index
                self.count = box.count()
            
            def __iter__(self):
                return self
            
            def __next__(self) -> 'ListBox.Item':
                if self.index >= self.count:
                    raise StopIteration
                item = ListBox.Item(self.box, self.index)
                self.index += 1
                return item
            
        box: 'ListBox'
        
        def __init__(self, box: 'ListBox'):
            self.box = box
            
        def __iter__(self) -> Iterator:
            return self.Iterator(self)
        
        def __getitem__(self, index: int) -> 'ListBox.Item':
            if index >= self.box.count():
                raise IndexError('list index out of range')
            return ListBox.Item(self.box, index)
    
    _width: int
    _height: int
    selection: Selection
    items: Items
    on_err_space: MultiEvent
    on_selection_cancel: MultiEvent
    on_selection_change: MultiEvent
    
    def __init__(self, width: int, height: int, parent: int | HANDLE, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.selection = self.Selection(self)
        self.items = self.Items(self)
        self.on_err_space = MultiEvent()
        self.on_selection_cancel = MultiEvent()
        self.on_selection_change = MultiEvent()
      
    def reserve(self, number: int, extra: int = 0):
        """
        Reserve the storage for listbox.
        """
        if self.send(LB_INITSTORAGE, number, extra) == LB_ERRSPACE:
            raise MemoryError('not enough memory')
        
    def insert(self, index: int, text: str) -> Item:
        """
        Insert the new string.
        """
        buffer = create_unicode_buffer(text)
        result = self.send(LB_INSERTSTRING, index, buffer)
        if result == LB_ERR:
            raise WinException()
        if result == LB_ERRSPACE:
            raise MemoryError('not enough memory')
        return ListBox.Item(self, result)
    
    def add(self, text: str) -> Item:
        """
        Add the new string.
        """
        buffer = create_unicode_buffer(text)
        result = self.send(LB_ADDSTRING, 0, buffer)
        if result == LB_ERR:
            raise WinException()
        if result == LB_ERRSPACE:
            raise MemoryError('not enough memory')
        return ListBox.Item(self, result)
    
    def find(self, text: str, exact: bool = False, index: int = -1) -> Item | None:
        """
        Find the string in listbox (by beginning or by exact equivalence).
        """
        buffer = create_unicode_buffer(text)
        if exact:
            result = self.send(LB_FINDSTRINGEXACT, index, buffer)
        else:
            result = self.send(LB_FINDSTRING, index, buffer)
        if result == LB_ERR:
            return None
        return ListBox.Item(self, result)
    
    @property
    def lcid(self) -> int:
        return self.send(LB_GETLOCALE)
    
    @lcid.setter
    def lcid(self, lcid: int):
        self.send(LB_SETLOCALE, lcid)
        
    def count(self) -> int:
        """
        Get the count of items.
        """
        result = self.send(LB_GETCOUNT)
        if result == LB_ERR:
            raise WinException()
        return result
    
    @property
    def horizontal_extent(self) -> int:
        return self.send(LB_GETHORIZONTALEXTENT)
    
    @horizontal_extent.setter
    def horizontal_extent(self, horizontal_extent: int):
        self.send(LB_SETHORIZONTALEXTENT, horizontal_extent)
        
    @property
    def top_item(self) -> Item | None:
        if self.count() == 0:
            return None
        result = self.send(LB_GETTOPINDEX)
        if result == LB_ERR:
            return None
        return ListBox.Item(self, result)
    
    @top_item.setter
    def top_item(self, top_item: int | Item):
        if isinstance(top_item, ListBox.Item):
            top_item = top_item.index
        if self.send(LB_SETTOPINDEX, top_item) == LB_ERR:
            raise WinException()
        
    def clear(self):
        """
        Clear the contents.
        """
        self.send(LB_RESETCONTENT)
        
    def parent_window_on_notify(self, nm: NMHDR):
        if nm.hwndFrom == self.value:
            code = INT(nm.code).value
            if code == LBN_SETFOCUS:
                self.on_nm_focus_changed.execute()
            elif code == LBN_KILLFOCUS:
                self.on_nm_focus_lost.execute()
            elif code == LBN_ERRSPACE:
                self.on_err_space.execute()
            elif code == LBN_SELCANCEL:
                self.on_selection_cancel.execute()
            elif code == LBN_SELCHANGE:
                self.on_selection_change.execute()
            else:
                super().parent_window_on_notify(nm)
                
    def hit(self, x: int, y: int) -> Item | None:
        """
        Hit the listbox to get item under clickable point.
        """
        result = self.send(LB_ITEMFROMPOINT, 0, MAKELPARAM(x, y))
        outside = HIWORD(result)
        if outside:
            return None
        index = LOWORD(result)
        return ListBox.Item(self, index)
    
    @property
    def item_height(self) -> int:
        result = self.send(LB_GETITEMHEIGHT)
        if result == LB_ERR:
            raise WinException()
        return result