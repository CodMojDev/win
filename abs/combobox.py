from .window import *

class Combobox(Control):
    class Item:
        cb: 'Combobox'
        index: int
        
        def __init__(self, cb: 'Combobox', index: int):
            self.cb = cb
            self.index = index
            
        def delete(self):
            self.cb.send(CB_DELETESTRING, self.index)
            
        @property
        def data(self) -> int:
            return self.cb.send(CB_GETITEMDATA, self.index)
        
        @data.setter
        def data(self, data: WT_ADDRLIKE):
            self.cb.send(CB_SETITEMDATA, self.index, data)
        
        @property
        def text(self) -> str | None:
            length = self.cb.send(CB_GETLBTEXTLEN, self.index)
            if length == CB_ERR: return None
            text = create_unicode_buffer(length)
            if self.cb.send(CB_GETLBTEXT, self.index, text) == CB_ERR:
                return None
            return text.value
        
        @text.setter
        def text(self, text: str):
            self._buffer_cache = create_unicode_buffer(text)
            self.cb.send(CB_SETITEMDATA, self.index, self._buffer_cache)
    
    on_selection_changed: MultiEvent
    on_selection_canceled: MultiEvent
    on_selection_ok: MultiEvent
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = WC_COMBOBOXW
        
    def headless_init(self):
        super().headless_init()
        self.on_selection_changed = MultiEvent()
        self.on_selection_canceled = MultiEvent()
        self.on_selection_ok = MultiEvent()
        
    def create(self, x: int, y: int, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, '', relative)
        
    def clear(self):
        self.send(CB_RESETCONTENT)
        
    def count(self) -> int:
        return self.send(CB_GETCOUNT)
    
    def insert(self, index: int, variant: str):
        index = self.send(CB_INSERTSTRING, index, variant)
        if index == CB_ERR: raise WinException()
        return Combobox.Item(self, index)
    
    def remove(self, index: int):
        self.send(CB_DELETESTRING, index)
    
    def append(self, variant: str) -> Item:
        index = self.send(CB_ADDSTRING, 0, variant)
        if index == CB_ERR: raise WinException()
        return Combobox.Item(self, index)
        
    def limit(self, limit: int):
        self.send(CB_LIMITTEXT, limit)
    
    def __getitem__(self, index: int | Item) -> Item:
        if isinstance(index, Combobox.Item):
            index = index.index
        return Combobox.Item(self, index)
    
    @property
    def current(self) -> Item:
        return Combobox.Item(self, self.send(CB_GETCURSEL))
    
    @current.setter
    def current(self, current: int | Item):
        if isinstance(current, Combobox.Item):
            current = current.index
        self.send(CB_SETCURSEL, current)
    
    @property
    def item_height(self) -> int:
        return self.send(CB_GETITEMHEIGHT, 0, -1)
    
    @item_height.setter
    def item_height(self, item_height: int):
        self.send(CB_SETITEMHEIGHT, 0, item_height)
    
    def parent_window_on_command(self, identifier: int, notify_code: int, hwnd: int):
        if identifier == self.identifier:
            if notify_code == CBN_SETFOCUS:
                self.on_nm_focus_changed.execute()
            elif notify_code == CBN_KILLFOCUS:
                self.on_nm_focus_lost.execute()
            elif notify_code == CBN_SELCHANGE:
                self.on_selection_changed.execute()
            elif notify_code == CBN_SELENDCANCEL:
                self.on_selection_canceled.execute()
            elif notify_code == CBN_SELENDOK:
                self.on_selection_ok.execute()
            else:
                super().parent_window_on_command(identifier, notify_code, hwnd)