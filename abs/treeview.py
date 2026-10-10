from .imagelist import *
from .window import *
from .edit import *
from win.defbase_allocator import *

class TreeItem(HTREEITEM):
    """
    Class, representing tree item (HTREEITEM).
    """
    
    class EditLabel:
        tree_item: 'TreeItem'
        
        def __init__(self, tree_item: 'TreeItem'):
            self.tree_item = tree_item
        
        def begin(self) -> Edit:
            """
            Begin the label editing for tree item.
            """
            
            hEdit = self.tree_item.tree_view.send(TVM_EDITLABELW, lParam=self.tree_item)
            if not hEdit: return None
            return Edit.foreign(hEdit)
        
        def end(self, dont_save: bool = False):
            """
            End the label editing for tree item.
            """
            
            self.tree_item.tree_view.send(TVM_ENDEDITLABELNOW, dont_save)
            
        def get(self) -> Edit:
            """
            Get the label edit control for tree item.
            """
            
            hEdit = self.tree_item.tree_view.send(TVM_GETEDITCONTROL)
            if not hEdit: return None
            return Edit.foreign(hEdit)
        
        def __enter__(self):
            return self.begin()
        
        def __exit__(self, exc_type, exc, tb):
            self.end()
    
    tree_view: 'TreeView'
    allocator: IAllocator
    
    def __init__(self, tree_view: 'TreeView', value: int):
        self.edit_label = TreeItem.EditLabel(self)
        self.tree_view = tree_view
        self.value = value
        self.allocator = CLocalAllocator()
        
    def select(self, action: int = TVGN_CARET):
        """
        Select the tree item.
        """
        
        self.tree_view.send(TVM_SELECTITEM, action, self)
        
    @property
    def parent(self) -> 'TreeItem':
        item = self.tree_view.send(TVM_GETNEXTITEM, TVGN_PARENT, self)
        if not item:
            return None
        return TreeItem(self.tree_view, item)
    
    def delete(self):
        """
        Delete the tree item.
        """
        
        self.tree_view.send(TVM_DELETEITEM, lParam=self)
        self.value = None
        
    def collapse(self):
        """
        Collapse the tree item.
        """
        
        self.tree_view.send(TVM_EXPAND, TVE_COLLAPSE, self)
        
    def expand(self):
        """
        Expand the tree item.
        """
        
        self.tree_view.send(TVM_EXPAND, TVE_EXPAND, self)
        
    def toggle(self):
        """
        Toggle the tree item.
        """
        
        self.tree_view.send(TVM_EXPAND, TVE_TOGGLE, self)
        
    def show_info_tip(self):
        """
        Show info tip on the tree item.
        """
        
        self.tree_view.send(TVM_SHOWINFOTIP, lParam=self)

    @property
    def item_rect(self) -> RECT:
        rect = RECT()
        i_cast_structure(rect, HTREEITEM).value = self.value
        self.tree_view.send(TVM_GETITEMRECT, FALSE, byref(rect))
        return rect

    @property
    def text_rect(self) -> RECT:
        rect = RECT()
        i_cast_structure(rect, HTREEITEM).value = self.value
        self.tree_view.send(TVM_GETITEMRECT, TRUE, byref(rect))
        return rect
    
    def state(self, mask: int) -> int:
        """
        Get tree item state.
        """
        return self.tree_view.send(TVM_GETITEMSTATE, self, mask)
    
    def insert(self, after: int | HANDLE = TVI_LAST, text: str = '',
               image_index: int | None = None, selected_image_index: int | None = None,
               value: int | None = None, children_count: int = 0) -> 'TreeItem':
        """
        Insert another item into tree item.
        """
        
        tviex = TVITEMEXW()
        tviex.mask = TVIF_TEXT | TVIF_IMAGE
        if image_index is None:
            image_index = -1
        tviex.iImage = image_index
        if selected_image_index is not None:
            tviex.mask |= TVIF_SELECTEDIMAGE
            tviex.iSelectedImage = selected_image_index
        if value is not None:
            value = PtrUtil.get_address(value)
            tviex.mask |= TVIF_PARAM
            tviex.lParam = value
        if children_count:
            tviex.mask |= TVIF_CHILDREN
        if isinstance(text, str): buffer = create_unicode_buffer(text)
        else: buffer = text
        tviex.pszText = i_cast(buffer, LPWSTR)
        tviex.cchTextMax = len(text)
        tviex.cChildren = children_count
        tvis = TVINSERTSTRUCTW()
        tvis.hInsertAfter = after
        tvis.hParent = self
        tvis.itemex = tviex
        hItem = self.tree_view.send(TVM_INSERTITEMW, lParam=tvis.addressof())
        if not hItem:
            return None
        return TreeItem(self.tree_view, hItem)
    
    def information(self, mask: int | None = None) -> TVITEMEXW:
        """
        Get information of a tree item.
        """
        
        tviex = TVITEMEXW()
        if mask is None:
            mask = (
                TVIF_TEXT | TVIF_CHILDREN | TVIF_SELECTEDIMAGE | TVIF_EXPANDEDIMAGE |
                TVIF_IMAGE | TVIF_PARAM | 
                TVIF_INTEGRAL | TVIF_STATE | 
                TVIF_STATEEX)
        tviex.mask = mask
        tviex.hItem = self.value
        if mask & TVIF_TEXT:
            text = self.allocator.allocate(512)
            tviex.pszText = i_cast(text, LPWSTR)
            tviex.cchTextMax = 256
        self.tree_view.send(TVM_GETITEMW, lParam=tviex.addressof())
        return tviex
    
    def set(self, tviex: TVITEMEXW, mask: int | None = None):
        """
        Set the information of a tree item.
        """
        if mask is None:
            if tviex.mask != 0:
                mask = tviex.mask
            else:
                mask = (
                    TVIF_TEXT | TVIF_CHILDREN | TVIF_SELECTEDIMAGE | TVIF_EXPANDEDIMAGE |
                    TVIF_IMAGE | TVIF_PARAM | 
                    TVIF_INTEGRAL | TVIF_STATE | 
                    TVIF_STATEEX)
        tviex.mask = mask
        tviex.hItem = self.value
        self.tree_view.send(TVM_SETITEMW, lParam=tviex.addressof())
        
    def next(self, tvgn: int) -> TUnion['TreeItem', None]:
        """
        Get the next tree item.
        """
        hItem = self.tree_view.send(TVM_GETNEXTITEM, tvgn, self.value)
        if not hItem: return None
        return TreeItem(self.tree_view, hItem)
    
    def focus(self):
        """
        Focus the tree item.
        """
        self.tree_view.send(TVM_SETHOT, 0, self.value)

class TreeViewItemInfo(TVITEMEXW):
    @property
    def children(self) -> int:
        return self.cChildren
    
    @children.setter
    def children(self, children: int):
        self.cChildren = children
        self.mask |= TVIF_CHILDREN
    
    @property
    def parameter(self) -> int:
        return self.lParam
    
    @parameter.setter
    def parameter(self, parameter: int):
        self.lParam = parameter
        self.mask |= TVIF_PARAM
    
    @property
    def image(self) -> int:
        return self.iImage
    
    @image.setter
    def image(self, image: int):
        self.iImage = image
        self.mask |= TVIF_IMAGE
    
    @property
    def selected_image(self) -> int:
        return self.iSelectedImage
    
    @selected_image.setter
    def selected_image(self, selected_image: int):
        self.iSelectedImage = selected_image
        self.mask |= TVIF_SELECTEDIMAGE
    
    @property
    def expanded_image(self) -> int:
        return self.iExpandedImage
    
    @expanded_image.setter
    def expanded_image(self, expanded_image: int):
        self.iExpandedImage = expanded_image
        self.mask |= TVIF_EXPANDEDIMAGE
    
    @property
    def text(self) -> int:
        return self.pszText.value
    
    @text.setter
    def text(self, text: int):
        self._buffer_cache = create_unicode_buffer(text)
        self.pszText = i_cast(self._buffer_cache, LPWSTR)
        self.cchTextMax = len(text)
        self.mask |= TVIF_TEXT
    
    @property
    def integral(self) -> int:
        return self.iIntegral
    
    @integral.setter
    def integral(self, integral: int):
        self.iIntegral = integral
        self.mask |= TVIF_INTEGRAL
    
    @property
    def state_mask(self) -> int:
        return self.stateMask
    
    @state_mask.setter
    def state_mask(self, state_mask: int):
        self.stateMask = state_mask
        self.mask |= TVIF_STATE
        
    @property
    def state_ex(self) -> int:
        return self.uStateEx
    
    @state_ex.setter
    def state_ex(self, state_ex: int):
        self.uStateEx = state_ex
        self.mask |= TVIF_STATEEX

class TreeView(Control):
    """
    Win32 Tree view common control.
    """
    
    class TreeStyles(BitGroup):
        tv: 'TreeView'
        
        def __init__(self, tv: 'TreeView'):
            self.tv = tv
        
        @property
        def value(self) -> int:
            return self.tv.send(TVM_GETEXTENDEDSTYLE)
        
        @value.setter
        def value(self, value: int):
            self.tv.send(TVM_SETEXTENDEDSTYLE, 0, value)
    
    root: TreeItem
    on_item_changed: MultiEvent
    on_item_changing: MultiEvent
    on_selection_changed: MultiEvent
    on_selection_changing: MultiEvent
    on_get_infotip: MultiEvent
    on_get_disp_info: MultiEvent
    on_set_disp_info: MultiEvent
    on_begin_label_edit: MultiEvent
    on_end_label_edit: MultiEvent
    on_item_expanded: MultiEvent
    on_item_expanding: MultiEvent
    on_item_collapsed: MultiEvent
    on_item_collapsing: MultiEvent
    on_begin_drag: MultiEvent
    on_begin_right_drag: MultiEvent
    tree_styles: TreeStyles
    
    def __init__(self, width: int, height: int, parent: int | HANDLE, identifier: int | HANDLE):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = WC_TREEVIEWW
    
    def headless_init(self):
        super().headless_init()
        self.root = TreeItem(self, TVI_ROOT)
        self.on_item_changed = MultiEvent()
        self.on_item_changing = MultiEvent()
        self.on_selection_changed = MultiEvent()
        self.on_selection_changing = MultiEvent()
        self.on_get_infotip = MultiEvent()
        self.on_get_disp_info = MultiEvent()
        self.on_set_disp_info = MultiEvent()
        self.on_begin_label_edit = MultiEvent()
        self.on_end_label_edit = MultiEvent()
        self.on_item_expanded = MultiEvent()
        self.on_item_expanding = MultiEvent()
        self.on_item_collapsed = MultiEvent()
        self.on_item_collapsing = MultiEvent()
        self.on_begin_drag = MultiEvent()
        self.on_begin_right_drag = MultiEvent()
        self.tree_styles = self.TreeStyles(self)
    
    def create(self, x: int, y: int, relative: int | HANDLE = NULL):
        """
        Create tree view control.
        """
        
        super().create(self._width, self._height, x, y, '', relative)
        
    @property
    def bk_color(self) -> Color.BGR:
        return Color.BGR(self.send(TVM_GETBKCOLOR))
    
    @bk_color.setter
    def bk_color(self, bk_color: int | Color.IColor):
        self.send(TVM_SETBKCOLOR, lParam=int(bk_color))
        
    @property
    def text_color(self) -> Color.BGR:
        return Color.BGR(self.send(TVM_GETTEXTCOLOR))
    
    @text_color.setter
    def text_color(self, text_color: int | Color.IColor):
        self.send(TVM_SETTEXTCOLOR, lParam=int(text_color))
        
    @property
    def line_color(self) -> Color.BGR:
        return Color.BGR(self.send(TVM_GETLINECOLOR))
    
    @line_color.setter
    def line_color(self, line_color: int | Color.IColor):
        self.send(TVM_SETLINECOLOR, lParam=int(line_color))
        
    @property
    def image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(TVM_GETIMAGELIST, TVSIL_NORMAL))
    
    @image_list.setter
    def image_list(self, image_list: int | HANDLE):
        self.send(TVM_SETIMAGELIST, TVSIL_NORMAL, image_list)
        
    @property
    def state_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(TVM_GETIMAGELIST, TVSIL_STATE))
    
    @state_image_list.setter
    def state_image_list(self, state_image_list: int | HANDLE):
        self.send(TVM_SETIMAGELIST, TVSIL_STATE, state_image_list)
        
    def hit(self, x: int, y: int) -> tuple[int, TreeItem]:
        """
        Hit-test the tree view control.
        """
        
        info = TVHITTESTINFO()
        info.pt.x = x
        info.pt.y = y
        
        self.send(TVM_HITTEST, lParam=info.ref())
        if not info.hItem:
            return (info.flags, None)
        return (info.flags, TreeItem(self, info.hItem))
    
    @property
    def count(self) -> int:
        return self.send(TVM_GETCOUNT)
    
    @property
    def visible_count(self) -> int:
        return self.send(TVM_GETVISIBLECOUNT)
    
    def clear(self):
        """
        Clear the tree view.
        """
        
        self.send(TVM_DELETEITEM, lParam=TVI_ROOT)
        
    @property
    def scroll_time(self) -> int:
        return self.send(TVM_GETSCROLLTIME)
    
    @scroll_time.setter
    def scroll_time(self, scroll_time: int):
        self.send(TVM_SETSCROLLTIME, scroll_time)
        
    def set_autoscroll_info(self, pixels_per_second: int, redraw_interval: int):
        """
        Set autoscroll info of list view control.
        """
        
        self.send(TVM_SETAUTOSCROLLINFO, pixels_per_second, redraw_interval)
        
    @property
    def item_height(self) -> int:
        return self.send(TVM_GETITEMHEIGHT)
    
    @item_height.setter
    def item_height(self, item_height: int):
        self.send(TVM_SETITEMHEIGHT, item_height)
        
    def parent_window_on_notify(self, nm: NMHDR):
        if nm.hwndFrom == self.value:
            code = INT(nm.code).value
            if code == TVN_ITEMCHANGEDW:
                nmtvic = i_cast_structure(nm, NMTVITEMCHANGE)
                self.on_item_changed.execute(nmtvic)
            elif code == TVN_ITEMCHANGINGW:
                nmtvic = i_cast_structure(nm, NMTVITEMCHANGE)
                self.on_item_changing.execute(nmtvic)
            elif code == TVN_GETINFOTIPW:
                nmtvgit = i_cast_structure(nm, NMTVGETINFOTIPW)
                self.on_get_infotip.execute(nmtvgit)
            elif code == TVN_GETDISPINFOW:
                nmtvdi = i_cast_structure(nm, NMTVDISPINFOW)
                self.on_get_disp_info.execute(nmtvdi)
            elif code == TVN_SETDISPINFOW:
                nmtvdi = i_cast_structure(nm, NMTVDISPINFOW)
                self.on_get_disp_info.execute(nmtvdi)
            elif code == TVN_BEGINLABELEDITW:
                nmtvdi = i_cast_structure(nm, NMTVDISPINFOW)
                self.on_begin_label_edit.execute(nmtvdi)
            elif code == TVN_ENDLABELEDITW:
                nmtvdi = i_cast_structure(nm, NMTVDISPINFOW)
                self.on_end_label_edit.execute(nmtvdi)
            elif code == TVN_KEYDOWN:
                nmtvkd = i_cast_structure(nm, NMTVKEYDOWN)
                nmkd = NMKEY(nmtvkd.hdr, nmtvkd.wVKey, nmtvkd.flags)
                self.on_nm_key_down.execute(nmkd)
            elif code == TVN_ITEMEXPANDED:
                nmtv = i_cast_structure(nm, NMTREEVIEWW)
                if nmtv.action & TVE_COLLAPSE:
                    self.on_item_collapsed.execute(nmtv)
                else:
                    self.on_item_expanded.execute(nmtv)
            elif code == TVN_ITEMEXPANDING:
                nmtv = i_cast_structure(nm, NMTREEVIEWW)
                if nmtv.action & TVE_COLLAPSE:
                    self.on_item_collapsing.execute(nmtv)
                else:
                    self.on_item_expanding.execute(nmtv)
            elif code == TVN_BEGINDRAGW:
                nmtv = i_cast_structure(nm, NMTREEVIEWW)
                self.on_begin_drag.execute(nmtv)
            elif code == TVN_BEGINRDRAGW:
                nmtv = i_cast_structure(nm, NMTREEVIEWW)
                self.on_begin_right_drag.execute(nmtv)
            else:
                super().parent_window_on_notify(nm)