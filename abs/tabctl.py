from .window import *
from .imagelist import *

class TabControl(Control):
    class Tab:
        def __init__(self, ctl: 'TabControl', index: int):
            self.index = index
            self.ctl = ctl
            
        def information(self, mask: int | None = None) -> TCITEMW:
            """
            Get the information of a tab.
            """
            tci = TCITEMW()
            if mask is None:
                mask = (TCIF_TEXT | TCIF_IMAGE | TCIF_PARAM | TCIF_STATE)
            if mask & TCIF_TEXT:
                self._buffer = create_unicode_buffer(256)
                tci.pszText = i_cast(self._buffer, LPWSTR)
                tci.cchTextMax = 256
            tci.mask = mask
            self.ctl.send(TCM_GETITEMW, self.index, tci.ref())
            return tci
        
        def set(self, text: str | None = None, image: int | None = None, state: tuple[int, int] | None = None,
                parameter: int | None = None, rtl: bool = False):
            """
            Set the information of a tab.
            """
            tci = TCITEMW()
            mask = 0
            if text is not None:
                tci.pszText = text
                mask |= TCIF_TEXT
            if image is not None:
                tci.iImage = image
                mask |= TCIF_IMAGE
            if parameter is not None:
                tci.lParam = parameter
                mask |= TCIF_PARAM
            if state is not None:
                tci.dwState = state[0]
                tci.dwStateMask = state[1]
                mask |= TCIF_STATE
            if rtl:
                mask |= TCIF_RTLREADING
            tci.mask = mask
            self.ctl.send(TCM_SETITEMW, self.index, tci.ref())
        
        @property
        def name(self) -> str:
            tc = self.information(TCIF_TEXT)
            name = tc.pszText.value
            del self._buffer
            return name
        
        @name.setter
        def name(self, name: str):
            self.set(text=name)
            
        @property
        def image(self) -> int:
            return self.information(TCIF_IMAGE).iImage
        
        @image.setter
        def image(self, image: int):
            self.set(image=image)
            
        @property
        def rect(self) -> Rect:
            rc = Rect()
            self.ctl.send(TCM_GETITEMRECT, self.index, rc.ref())
            return rc
        
        def highlight(self, highlight: bool = False):
            self.ctl.send(TCM_HIGHLIGHTITEM, self.index, highlight)
            
        def delete(self):
            self.ctl.send(TCM_DELETEITEM, self.index)
            
        def __eq__(self, tab: 'TabControl.Tab') -> bool:
            return self.index == tab.index
    
    on_selection_changing: MultiEvent
    on_selection_changed: MultiEvent
    on_get_object: MultiEvent
    on_tc_key_down: MultiEvent
    
    def __init__(self, width: int, height: int, parent: int | HANDLE, identifier: int | HANDLE):
        super().__init__(parent, identifier)
        self.class_name = WC_TABCONTROLW
        self._width = width
        self._height = height
        self.on_selection_changing = MultiEvent()
        self.on_selection_changed = MultiEvent()
        self.on_get_object = MultiEvent()
        self.on_tc_key_down = MultiEvent()
    
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, '', relative=relative)
    
    def insert(self, index: int, text: str, image: int | None = None, parameter: int | None = None, rtl: bool = False) -> Tab:
        """
        Insert tab into tab control.
        """
        tci = TCITEMW()
        mask = TCIF_TEXT | TCIF_IMAGE
        if image is None:
            image = -1
        tci.iImage = image
        if parameter is not None:
            mask |= TCIF_PARAM
            tci.lParam = parameter
        if rtl:
            mask |= TCIF_RTLREADING
        tci.pszText = text
        tci.mask = mask
        index = self.send(TCM_INSERTITEMW, index, tci.ref())
        if index == -1: raise WinException()
        return TabControl.Tab(self, index)
    
    @property
    def tab_size(self) -> tuple[int, int]:
        i = self.send(TCM_SETITEMSIZE, 0, 0)
        self.send(TCM_SETITEMSIZE, 0, i)
        return LOWORD(i), HIWORD(i)
    
    @tab_size.setter
    def tab_size(self, tab_size: tuple[int, int]):
        self.send(TCM_SETITEMSIZE, 0, MAKELPARAM(tab_size[0], tab_size[1]))
    
    @property
    def count(self) -> int:
        return self.send(TCM_GETITEMCOUNT)
    
    @property
    def minimal_tab_width(self) -> int:
        i = self.send(TCM_SETMINTABWIDTH, 0, 0)
        self.send(TCM_SETMINTABWIDTH, 0, i)
        return i
    
    @minimal_tab_width.setter
    def minimal_tab_width(self, minimal_tab_width: int):
        self.send(TCM_SETMINTABWIDTH, 0, minimal_tab_width)
    
    @property
    def row_count(self) -> int:
        return self.send(TCM_GETROWCOUNT)
    
    @property
    def selected_tab(self) -> Tab | None:
        i = self.send(TCM_GETCURSEL)
        if i == -1: return None
        return TabControl.Tab(self, i)
    
    @selected_tab.setter
    def selected_tab(self, selected_tab: int | Tab):
        if isinstance(selected_tab, TabControl.Tab):
            selected_tab = selected_tab.index
        self.send(TCM_SETCURSEL, selected_tab)
        
    @property
    def image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(TCM_GETIMAGELIST))
    
    @image_list.setter
    def image_list(self, image_list: int | HANDLE):
        self.send(TCM_SETIMAGELIST, 0, image_list)
    
    def remove_image(self, index: int):
        """
        Remove an image at the specified index from tab control image list.
        """
        self.send(TCM_REMOVEIMAGE, index)
    
    @property
    def focused_tab(self) -> Tab | None:
        i = self.send(TCM_GETCURFOCUS)
        if i == -1: return None
        return TabControl.Tab(self, i)
    
    @focused_tab.setter
    def focused_tab(self, focused_tab: int | Tab):
        if isinstance(focused_tab, TabControl.Tab):
            focused_tab = focused_tab.index
        self.send(TCM_SETCURFOCUS, focused_tab)
    
    def hit(self, x: int, y: int) -> tuple[Tab, int]:
        """
        Hit-test the given position in a tab control.
        """
        tchti = TCHITTESTINFO()
        tchti.pt = POINT(x, y)
        i = self.send(TCM_HITTEST, 0, tchti.ref())
        if i == -1:
            return (None, 0)
        return (TabControl.Tab(i), tchti.flags)
    
    def clear(self):
        """
        Clear and delete all the tabs in a tab control.
        """
        self.send(TCM_DELETEALLITEMS)
    
    def deselect_all(self, save_current: bool = False):
        """
        Deselect all the tabs in a tab control.
        """
        self.send(TCM_DESELECTALL, save_current)
    
    def adjust_display(self, window_rect: Rect) -> Rect:
        """
        Adjust window rectangle to display area rectangle.
        """
        rc = window_rect.copy()
        self.send(TCM_ADJUSTRECT, FALSE, rc.ref())
        return rc
    
    def adjust_window(self, display_rect: Rect) -> Rect:
        """
        Adjust display area rectangle to window rectangle.
        """
        rc = display_rect.copy()
        self.send(TCM_ADJUSTRECT, TRUE, rc.ref())
        return rc
    
    def parent_window_on_notify(self, nm: NMHDR):
        if nm.hwndFrom == self.value:
            code = INT(nm.code).value
            if code == TCN_SELCHANGING:
                self.on_selection_changing.execute()
            elif code == TCN_SELCHANGE:
                self.on_selection_changed.execute()
            elif code == TCN_KEYDOWN:
                self.on_tc_key_down.execute(i_cast_structure(nm, NMTCKEYDOWN))
            else:
                super().parent_window_on_notify(nm)