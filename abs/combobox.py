from .window import *

class Combobox(Control):
    on_selection_changed: MultiEvent
    on_selection_canceled: MultiEvent
    on_selection_ok: MultiEvent
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = WC_COMBOBOXW
        self.on_selection_changed = MultiEvent()
        self.on_selection_canceled = MultiEvent()
        self.on_selection_ok = MultiEvent()
        
    def create(self, x: int, y: int, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, '', relative)
        
    def reset(self):
        self.send(CB_RESETCONTENT)
        
    def count(self) -> int:
        return self.send(CB_GETCOUNT)
    
    def insert(self, index: int, variant: str):
        self.send(CB_INSERTSTRING, index, variant)
        
    def append(self, variant: str):
        self.send(CB_ADDSTRING, 0, variant)
        
    def limit(self, limit: int):
        self.send(CB_LIMITTEXT, limit)
        
    @property
    def current(self) -> int:
        return self.send(CB_GETCURSEL)
    
    @current.setter
    def current(self, current: int):
        self.send(CB_SETCURSEL, current)
        
    def text(self, index: int) -> str | None:
        """
        Get text of the item.
        """
        length = self.send(CB_GETLBTEXTLEN, index)
        if length == CB_ERR: return None
        text = create_unicode_buffer(length)
        if self.send(CB_GETLBTEXT, index, text) == CB_ERR:
            return None
        return text.value
    
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