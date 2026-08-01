from win.abs.window import *

class PropertyGridItem:
    buddy: Window | None
    
    def __init__(self, name: str, buddy: Window | None = None):
        self.name = name
        self.buddy = buddy

PGVHT_NONE = 0
PGVHT_DIRBUTTON = 1
PGVHT_ITEM = 2

class PropertyGridView(Window):
    directories: dict[str, tuple[bool, list[PropertyGridItem]]]
    ht_map: list[tuple[Rect, int, int | str]]
    view_range: tuple[int, int]
    directory_color: Color.IColor
    directory_font: str
    name_font: str
    propname_width: int
    
    def invalidate(self, rect: RECT | Region = None, erase: bool = True):
        self.invalidated_from_managed = True
        super().invalidate(rect, erase)
    
    def __init__(self):
        super().__init__()
        self.styles.add(WS_BORDER, WS_CHILD, WS_VISIBLE, WS_VSCROLL)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add_ex(WS_EX_CLIENTEDGE)
        self.on_create += self.gridview_on_create
        self.directories = {}
        self.view_range = (0, 0)
        self.on_vscroll += self.gridview_on_vscroll
        self.directory_color = Color.BGR.string('#c0c0c0')
        self.directory_font = 'MS Shell Dlg'
        self.name_font = 'MS Shell Dlg'
        self.propname_width = 40
        self.ht_map = []
        self.on_left_button_up += self.gridview_on_left_button_up
        self.invalidated_from_managed = False
        self.background_color = Color.BGR.string('#ffffff')
        
    def gridview_on_create(self) -> bool:
        self.directory_brush = Brush.create(self.directory_color)
        self.background_brush = Brush.create(self.background_color)
        self.logical_directory_font = Font.create(self.directory_font, 15)
        self.logical_name_font = Font.create(self.name_font, 12)
        self.last_sb_position = 0
        self.timer(self.gridview_update_tick, 1*1000)
        return True
    
    def rows(self) -> list[tuple[str, bool] | PropertyGridItem]:
        result = []
        for k, v in self.directories.items():
            visible, rows = v
            result.append((k, visible))
            if visible:
                for row in rows:
                    result.append(row)
        return result
    
    def on_paint(self, dc: PaintDC) -> bool:
        if not self.invalidated_from_managed: return True
        self.invalidated_from_managed = False
        y = 0
        i_min, i_max = self.view_range
        i = -1
        self.ht_map.clear()
        rows = self.rows()
        si = SCROLLINFO()
        si.cbSize = si.size()
        si.fMask = SIF_RANGE | SIF_PAGE
        si.nMin = 0
        si.nMax = len(rows)-1
        si.nPage = 1
        SetScrollInfo(self, SB_VERT, si.ref(), TRUE)
        maximal_cx = 0
        with dc.select_ex(self.logical_name_font):
            for i, row in enumerate(rows):
                if isinstance(row, PropertyGridItem):
                    if i < i_min: continue
                    if i > i_max: continue
                    cx = dc.get_text_extent_point(row.name).cx
                    maximal_cx = max(cx, maximal_cx)
        if maximal_cx != 0:
            self.propname_width = maximal_cx + 10
                
        for i, row in enumerate(rows):
            if isinstance(row, PropertyGridItem):
                if i < i_min:
                    if row.buddy is not None: row.buddy.hide()
                    continue
                if i > i_max:
                    if row.buddy is not None: row.buddy.hide()
                    continue
                self.ht_map.append((Rect.create(24, y, self.propname_width, 24), PGVHT_ITEM, i))
                dc.fill(Rect.create(0, y, 24, 24), self.directory_brush)
                dc.move(24, y)
                dc.line(24, y+24)
                dc.move(24, y)
                dc.line(self.width, y)
                dc.move(24 + self.propname_width, y)
                dc.line(24 + self.propname_width, y+24)
                dc.move(24, y+23)
                dc.line(self.width, y+23)
                dc.bk_color = Color.BGR.string('#ffffff')
                with dc.select_ex(self.logical_name_font):
                    dc.text_out(27, y+3, row.name)
                if row.buddy is not None:
                    row.buddy.size = (self.width - self.propname_width - 24 - 1 - 1, 24 - 1 - 1)
                    row.buddy.position = (25 + self.propname_width, y + 1)
                    if not IsWindowVisible(row.buddy):
                        self.invalidated_from_managed = True
                        row.buddy.parent = self
                        
                        row.buddy.show()
                else:
                    dc.fill(Rect.create(24 + self.propname_width + 1, y, self.width - self.propname_width - 24 - 1 - 1, 24 - 1 - 1), self.background_brush)
            else:
                if i < i_min: continue
                if i > i_max: continue
                name, visible = row
                dc.fill(Rect.create(0, y, self.width, 24), self.directory_brush)
                if not visible:
                    element = VisualStyleElements.TreeView.Glyph.CLOSED
                    for row in self.directories[name][1]:
                        if row.buddy is not None: row.buddy.hide()
                else:
                    element = VisualStyleElements.TreeView.Glyph.OPENED
                dirbutton_rect = Rect.create(3, y+3, 16, 16)
                self.ht_map.append((dirbutton_rect, PGVHT_DIRBUTTON, name))
                element.draw_background(dc, dirbutton_rect)
                with dc.select_ex(self.logical_directory_font):
                    dc.bk_color = self.directory_color
                    dc.text_out(24, y+4, name)
            y += 24
        return True
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.invalidate()
        self.view_range = (self.view_range[0], height // 24)
        return True
    
    def row_count(self) -> int:
        n = len(self.directories)
        for v in self.directories.values():
            visible, rows = v
            if visible: n += len(rows)
        return n
    
    def gridview_update_tick(self, *_):
        self.invalidate()
    
    def gridview_on_vscroll(self, code: int, position: int, _):
        if code == SB_LINEDOWN:
            self.view_range = (self.view_range[0] + 1, self.view_range[1] + 1)
            SetScrollPos(self, SB_VERT, GetScrollPos(self, SB_VERT)+1, TRUE)
        elif code == SB_LINEUP:
            i_min = self.view_range[0] - 1
            if i_min >= 0:
                self.view_range = (i_min, self.view_range[1] - 1)
                SetScrollPos(self, SB_VERT, GetScrollPos(self, SB_VERT)-1, TRUE)
        elif code == SB_THUMBTRACK:
            diff = position - self.last_sb_position
            self.last_sb_position = position
            self.view_range = (self.view_range[0]+diff, self.view_range[1]+diff)
            SetScrollPos(self, SB_VERT, position, TRUE)
        self.invalidate()
        
    def gridview_on_left_button_up(self, flags: int, x: int, y: int):
        ht, n = self.hit_test(x, y)
        if ht == PGVHT_NONE: return
        elif ht == PGVHT_DIRBUTTON:
            visible, rows = self.directories[n]
            self.directories[n] = (not visible, rows)
            self.invalidate()
        elif ht == PGVHT_ITEM:
            ...
        
    def hit_test(self, x: int, y: int) -> tuple[int, int | None | str]:
        pt = Point(x, y)
        for rc, ht, v in self.ht_map:
            if pt in rc:
                return (ht, v)
        return (PGVHT_NONE, None)

class PropertyGridDescription(Window):
    def __init__(self):
        super().__init__()
        self.styles.add(WS_BORDER, WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add_ex(WS_EX_CLIENTEDGE)
        self.on_create += self.desc_on_create
        self.text = ''
        self.header = ''
        self.header_font = 'MS Shell Dlg'
        self.text_font = 'MS Shell Dlg'
        self.edge_cx = GetSystemMetrics(SM_CXEDGE)
        self.edge_cy = GetSystemMetrics(SM_CYEDGE)
        
    def desc_on_create(self) -> bool:
        self.logical_header_font = Font.create(self.header_font, 15, weight = FW_BOLD)
        self.logical_text_font = Font.create(self.text_font, 13)
        return True
    
    def on_paint(self, dc: PaintDC) -> bool:
        with dc.select_ex(self.logical_header_font):
            height = dc.get_text_extent_point(self.header).cy
            dc.text_out(self.edge_cx+5, self.edge_cy+4, self.header)
        with dc.select_ex(self.logical_text_font):
            rc = self.client_rect
            dx, dy = self.edge_cx, self.edge_cy
            text = self.text.replace('\r\n', '\n').replace('\n', ' \n ')
            for word in text.split(' '):
                if word == '\n':
                    dy += dc.get_text_extent_point('A').cy
                    dx = self.edge_cx
                else:
                    size = dc.get_text_extent_point(word)
                    if 5 + dx + size.cx >= rc.right:
                        dy += size.cy
                        dx = self.edge_cx
                    dc.text_out(5 + dx, 4 + height + 6 + dy, word)
                    dx += size.cx + dc.get_text_extent_point(' ').cx
        return True
    
    def get_recommended_height(self, text: str, header: str):
        with DC.create_compatible(NULL) as dc:
            with dc.select_ex(self.logical_header_font):
                height = dc.get_text_extent_point(header).cy
            with dc.select_ex(self.logical_text_font):
                rc = self.client_rect
                dx, dy = self.edge_cx, self.edge_cy + dc.get_text_extent_point('A').cy
                text = text.replace('\r\n', '\n').replace('\n', ' \n ')
                for word in text.split(' '):
                    if word == '\n':
                        dy += dc.get_text_extent_point('A').cy
                        dx = self.edge_cx
                    else:
                        size = dc.get_text_extent_point(word)
                        if 5 + dx + size.cx >= rc.right:
                            dy += size.cy
                            dx = self.edge_cx
                        dx += size.cx + dc.get_text_extent_point(' ').cx
                return 4 + dy + height + 6 + self.edge_cy
            
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.invalidate()
        return True
        
class PropertyGrid(Window):
    buddy: TUnion[Window, None]
    
    def __init__(self):
        super().__init__()
        self.on_create += self.grid_on_create
        self.styles.remove(WS_MAXIMIZEBOX, WS_MINIMIZEBOX)
        self.styles.add_ex(WS_EX_TOOLWINDOW)
        
    def grid_on_create(self) -> bool:
        self.buddy = None
        if self.buddy is not None:
            dy = self.buddy.y
        else: dy = 0
        self.description = PropertyGridDescription()
        self.description.create(self.width, self.height - 60, 0, 60, parent=self)
        self.grid_view = PropertyGridView()
        self.grid_view.create(self.width, self.height - 60 - dy, 0, dy, parent=self)
        return True
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        if self.buddy is not None:
            dy = self.buddy.y
        else: dy = 0
        recommended = self.description.get_recommended_height(self.description.text, self.description.header)
        self.description.size = (width, recommended)
        self.description.position = (0, height - recommended)
        self.grid_view.size = (width, height - self.description.height - dy - 3)
        self.grid_view.position = (0, dy)
        
        return True