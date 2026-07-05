from .imagelist import *
from .window import *

class ListView(Control):
    """
    Win32 List view common control
    """
    
    class Columns:
        class Column(LVCOLUMNW):
            list_view: 'ListView'
            
            def __init__(self, list_view: 'ListView'):
                super().__init__()
                self.list_view = list_view
                self.index = 0
                
            index: int
            
            def select(self):
                """
                Select column.
                """
                
                self.list_view.send(LVM_SETSELECTEDCOLUMN, self.index)
            
            @property
            def width(self) -> int:
                return self.list_view.send(LVM_GETCOLUMNWIDTH, self.index)
            
            @width.setter
            def width(self, width: int):
                self.list_view.send(LVM_SETCOLUMNWIDTH, self.index, width)
            
        list_view: 'ListView'
        
        def __init__(self, list_view: 'ListView'):
            self.list_view = list_view
    
        def insert(self, index: int, text: str = None, width: int = None, image: int = None,
                   ideal_width: int = None, minimal_width: int = None, format: int = None,
                   order: int = None, default_width: int = None, sub_item: int = None) -> 'ListView.Columns.Column':
            """
            Insert column into list view columns.
            """
            
            column = ListView.Columns.Column(self.list_view)
            
            if text is not None:
                text = create_unicode_buffer(text)
                column.pszText = i_cast(text, LPWSTR)
                column.cchTextMax = len(text)
                column.mask |= LVCF_TEXT
                
            if width is not None:
                column.cx = width
                column.mask |= LVCF_WIDTH
                
            if image is not None:
                column.iImage = image
                column.mask |= LVCF_IMAGE
                
            if minimal_width is not None:
                column.cxMin = minimal_width
                column.mask |= LVCF_MINWIDTH
                
            if ideal_width is not None:
                column.cxIdeal = ideal_width
                column.mask |= LVCF_IDEALWIDTH
                
            if format is not None:
                column.fmt = format
                column.mask |= LVCF_FMT
                
            if order is not None:
                column.iOrder = order
                column.mask |= LVCF_ORDER
                
            if default_width is not None:
                column.cxDefault = default_width
                column.mask |= LVCF_DEFAULTWIDTH
                
            if sub_item is not None:
                column.iSubItem = sub_item
                column.mask |= LVCF_SUBITEM
            
            column.index = self.list_view.send(LVM_INSERTCOLUMNW, index, column.ref())
            return column
        
        def __getitem__(self, index: int) -> 'ListView.Columns.Column':
            column = ListView.Columns.Column(self.list_view)
            column.mask = (LVCF_IMAGE | LVCF_FMT | LVCF_MINWIDTH | LVCF_WIDTH | LVCF_SUBITEM |
                           LVCF_DEFAULTWIDTH | LVCF_IDEALWIDTH | LVCF_ORDER | LVCF_TEXT)
            if not self.list_view.send(LVM_GETCOLUMNW, index, column.ref()):
                raise IndexError(f'Invalid item index: {index}')
            column.index = index
            return column
        
        def __setitem__(self, index: int, column: 'ListView.Columns.Column'):
            column.mask = (LVCF_IMAGE | LVCF_FMT | LVCF_MINWIDTH | LVCF_WIDTH | LVCF_SUBITEM |
                           LVCF_DEFAULTWIDTH | LVCF_IDEALWIDTH | LVCF_ORDER | LVCF_TEXT)
            if not self.list_view.send(LVM_SETCOLUMNW, index, column.ref()):
                raise IndexError(f'Invalid item index: {index}')
        
    class Items:
        class Item(LVITEMW):
            list_view: 'ListView'
            index: int
            
            def __init__(self, list_view: 'ListView'):
                super().__init__()
                self.list_view = list_view
                self.index = 0
                
            @property
            def visible(self) -> bool:
                return bool(self.list_view.send(LVM_ISITEMVISIBLE, self.index))
                
        list_view: 'ListView'
        
        def __init__(self, list_view: 'ListView'):
            self.list_view = list_view
            
        def make_item(self, index: int, text: str = None, param: int = None, 
                   group_id: int = None, indent: int = None, state: tuple[int, int] = None, 
                   columns: Iterable['ListView.Columns.Column'] = None, sub_item: int = None) -> 'ListView.Items.Item':
            """
            Make item from arguments.
            """
            
            item = ListView.Items.Item(self.list_view)
            item.iItem = index
            
            if param is not None:
                item.lParam = param
                item.mask |= LVIF_PARAM
            
            if sub_item is not None:
                item.iSubItem = sub_item
            
            if text is not None:
                text = create_unicode_buffer(text)
                item.pszText = i_cast(text, LPWSTR)
                item.cchTextMax = len(text)
                item.mask |= LVIF_TEXT
                
            if group_id is not None:
                item.iGroupId = group_id
                item.mask |= LVIF_GROUPID
                
            if indent is not None:
                item.iIndent = indent
                item.mask |= LVIF_INDENT
                
            if state is not None:
                item.state, item.stateMask = state
                item.mask |= LVIF_STATE
                
            if columns is not None:
                if columns == I_COLUMNSCALLBACK:
                    item.cColumns = columns
                else:
                    cColumns = len(columns)
                    item.cColumns = cColumns
                    puColumns = (ULONG * cColumns)(*[column.index for column in columns])
                    item.puColumns = puColumns
                    piColFmt = (INT * cColumns)(*[column.fmt for column in columns])
                    item.piColFmt = piColFmt
                    
                item.mask |= LVIF_COLUMNS
                item.mask |= LVIF_COLFMT
            
            return item
            
        def insert(self, index: int, text: str = None, param: int = None, 
                   group_id: int = None, indent: int = None, state: tuple[int, int] = None, 
                   columns: Iterable['ListView.Columns.Column'] = None, sub_item: int = None) -> 'ListView.Items.Item':
            """
            Insert item into list view items.
            """
            
            item = self.make_item(index, text, param, group_id, indent, state, columns, sub_item)
            item.index = self.list_view.send(LVM_INSERTITEMW, lParam=item.ref())
            return item
            
        def set(self, index: int, text: str = None, param: int = None, 
                group_id: int = None, indent: int = None, state: tuple[int, int] = None, 
                columns: Iterable['ListView.Columns.Column'] = None, sub_item: int = None):
            item = self.make_item(index, text, param, group_id, indent, state, columns, sub_item)
            self.list_view.post(LVM_SETITEMW, lParam=item.ref())
            
        def delete(self, index: int):
            self.list_view.post(LVM_DELETEITEM, index)
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HWND):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = WC_LISTVIEWW
        self.columns = ListView.Columns(self)
        self.items = ListView.Items(self)
    
    def create(self, x: int, y: int, relative: int | HANDLE = NULL):
        """
        Create list view control.
        """
        
        super().create(self._width, self._height, x, y, '', relative)
        
    @property
    def view(self) -> int:
        return self.send(LVM_GETVIEW)
    
    @view.setter
    def view(self, view: int):
        if self.send(LVM_SETVIEW, view) == -1:
            raise ValueError(f'Invalid view: {format_hex(view)}')
        
    @property
    def view_rect(self) -> Rect:
        rc = Rect()
        self.send(LVM_GETVIEWRECT, lParam=byref(rc))
        return rc
    
    def redraw_items(self, first: int, last: int):
        """
        Redraw list view items.
        """
        
        self.send(LVM_REDRAWITEMS, first, last)
        
    def scroll(self, horizontal: int, vertical: int):
        """
        Scroll the list view control.
        """
        
        self.send(LVM_SCROLL, horizontal, vertical)
        
    @property
    def bk_color(self) -> Color.BGR:
        return Color.BGR(self.send(LVM_GETBKCOLOR))
    
    @bk_color.setter
    def bk_color(self, bk_color: int | Color.IColor):
        self.send(LVM_SETBKCOLOR, lParam=int(bk_color))
        
    @property
    def text_color(self) -> Color.BGR:
        return Color.BGR(self.send(LVM_GETTEXTCOLOR))
    
    @text_color.setter
    def text_color(self, text_color: int | Color.IColor):
        self.send(LVM_SETTEXTCOLOR, lParam=int(text_color))
        
    @property
    def text_bk_color(self) -> Color.BGR:
        return Color.BGR(self.send(LVM_GETTEXTBKCOLOR))
    
    @text_bk_color.setter
    def text_bk_color(self, text_bk_color: int | Color.IColor):
        self.send(LVM_SETTEXTBKCOLOR, lParam=int(text_bk_color))
        
    @property
    def image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(LVM_GETIMAGELIST, LVSIL_NORMAL))
    
    @image_list.setter
    def image_list(self, image_list: int | HANDLE):
        self.send(TVM_SETIMAGELIST, LVSIL_NORMAL, image_list)
        
    @property
    def state_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(LVM_GETIMAGELIST, LVSIL_STATE))
    
    @state_image_list.setter
    def state_image_list(self, image_list: int | HANDLE):
        self.send(LVM_SETIMAGELIST, LVSIL_STATE, image_list)
        
    @property
    def small_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(LVM_GETIMAGELIST, LVSIL_SMALL))
    
    @small_image_list.setter
    def small_image_list(self, image_list: int | HANDLE):
        self.send(LVM_SETIMAGELIST, LVSIL_SMALL, image_list)
        
    @property
    def group_header_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(LVM_GETIMAGELIST, LVSIL_GROUPHEADER))
    
    @group_header_image_list.setter
    def group_header_image_list(self, image_list: int | HANDLE):
        self.send(LVM_SETIMAGELIST, LVSIL_GROUPHEADER, image_list)
        
    def hit(self, x: int, y: int) -> tuple[int, 'ListView.Items.Item']:
        """
        Hit-test the list view control.
        """
        
        lvhti = LVHITTESTINFO()
        lvhti.pt.x = x
        lvhti.pt.y = y
        i = self.send(LVM_HITTEST, 0, lvhti.ref())
        if i == -1: return (lvhti.flags, None)
        return (lvhti.flags, self.items[i])