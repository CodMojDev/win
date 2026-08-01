from win.abs.window import *

class PropertyGridView(Window):
    def __init__(self):
        super().__init__()
        
        # events
        self.on_create += self.PropertyGridView_on_create
        
        # styles
        self.styles.add(WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        
        # instance fields
        self.visible_rows = 0
        
    def PropertyGridView_on_create(self) -> bool:
        return True

class PropertyGridDocComment(Window):
    def __init__(self):
        super().__init__()
        
        # events
        self.on_create += self.PropertyGridDocComment_on_create
        
        # styles
        self.styles.add(WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        
        # instance fields
        
    def PropertyGridDocComment_on_create(self) -> bool:
        return True

class PropertyGridHotCommands(Window):
    def __init__(self):
        super().__init__()
        
        # events
        self.on_create += self.PropertyGridHotCommands_on_create
        
        # styles
        self.styles.add(WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)

        # instance fields
        
    def PropertyGridHotCommands_on_create(self) -> bool:
        return True

class PropertyGridToolStripItem:
    def __init__(self, text: str | None = None, image: Bitmap | None = None):
        self.text = text
        self.image = image
        self.size = Size(23, 23)
       
    def on_paint(self, dc: DC):
        pass
    
    def bounds(self) -> Rect:
        return Rect(0, 0, 0, 0)
        
class PropertyGridToolStripSeparator(PropertyGridToolStripItem):
    def __init__(self):
        super().__init__()
        self.renderer = PropertyGridToolStripRenderer()
        self.size.cx = 6
        self.size.cy = 6
    
    def on_paint(self, dc: DC):
        self.renderer.render_separator(dc, Rect(0, 0, self.size.cx, self.size.cy))

class PropertyGridToolStrip(Window):
    displayed_items: list[PropertyGridToolStripItem]
    items: list[PropertyGridToolStripItem]
    
    def __init__(self):
        super().__init__()
        
        # events
        self.on_create += self.PropertyGridToolStrip_on_create
        
        # styles
        self.styles.add(WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)

        # instance fields
        self.displayed_items = []
        self.items = []
        
    def PropertyGridToolStrip_on_create(self) -> bool:
        return True
    
    def on_paint(self, dc: PaintDC) -> bool:
        for item in self.displayed_items:
            rc = i_cast_structure(dc.paint_struct.rcPaint, Rect)
            bounds = item.bounds()
            rc.intersect(bounds)
            with dc.create_compatible() as mem_dc:
                with mem_dc.create_compatible_bitmap(item.size.cx, item.size.cy) as bmp:
                    with mem_dc.select_ex(bmp):
                        item.on_paint(mem_dc)
                        dc.bit_blt(0, 0, bounds.x, bounds.y, item.size.cx, item.size.cy, mem_dc, SRCCOPY)
            rc.offset(-bounds.x, -bounds.y)
        
        return True

class PropertyGridToolStripSeparator(Window):
    def __init__(self):
        super().__init__()
        
        # events
        self.on_create += self.PropertyGridToolStripSeparator_on_create
        
        # styles
        self.styles.add(WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)

        # instance fields
        
    def PropertyGridToolStripSeparator_on_create(self) -> bool:
        return True

class PropertyGridToolStripRenderer:
    def render_separator(self, dc: DC, bounds: Rect, vertical: bool):
        if vertical:
            VisualStyleElements.ToolBar.SeparatorHorizontal.NORMAL.draw_background(dc, bounds)
        else:
            VisualStyleElements.ToolBar.SeparatorVertical.NORMAL.draw_background(dc, bounds)

class PropertyGrid(Window):
    def __init__(self):
        super().__init__()
        self.on_create += self.PropertyGrid_on_create
        
    def PropertyGrid_on_create(self) -> bool:
        self.doc_comment = PropertyGridDocComment()
        self.doc_comment.create(self.width, 60, 0, self.height - 60, parent=self)
        
        self.tool_strip = PropertyGridToolStrip()
        self.tool_strip.styles.add(WS_TABSTOP)
        self.tool_strip.create(self.width, 40, parent=self)
        
        self.grid_view = PropertyGridView()
        self.grid_view.styles.add(WS_TABSTOP)
        self.grid_view.create(self.width, self.height - 60 - 40, 0, 40)
        
        return True
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.doc_comment.position = (0, height - 60)
        self.doc_comment.size = (width, 60)
        self.tool_strip.size = (width, 40)
        self.grid_view.size = (width, height - 60 - 40)
        return True
    
    def color_rop2(color: Color.IColor, dark: int, light: int) -> int:
        if color.brightness < 0.5:
            return dark
        return light
    
    def reversible_line(self, dc: DC, start: Point, end: Point, color: Color.IColor):
        rop2 = self.color_rop2(color, R2_NOTXORPEN, R2_XORPEN)
        with Pen.create(PS_SOLID, 1, color) as pen:
            last = dc.set_rop2(rop2)
            with dc.select_ex(pen):
                with dc.select_ex(Brush.stock(NULL_BRUSH)):
                    dc.move(start.x, start.y)
                    dc.line(end.x, end.y)
                    dc.rop2 = last
                    
    def draw_xor_bar(self, dc: DC, to: Window, rc: Rect):
        if rc.width < rc.height:
            for i in range(rc.width):
                self.reversible_line(dc, Point(rc.x + i, rc.y), Point(rc.x + i, rc.y + rc.height), Color.BGR.color(255, 255, 255))
        else:
            for i in range(rc.height):
                self.reversible_line(dc, Point(rc.x, rc.y + i), Point(rc.x + rc.width, rc.y + i), Color.BGR.color(255, 255, 255))
                
    def on_paint(self, dc: PaintDC) -> bool:
        return True