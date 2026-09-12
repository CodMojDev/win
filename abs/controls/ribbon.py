#
# UNDER CONSTRUCTION
#

from win.abs.window import *
from win.abs.tabctl import *

class RibbonGalleryItemState:
    Normal = 0
    Highlight = 1
    Pushed = 2

class RibbonGalleryItem:
    """
    Ribbon gallery item.
    """
    
    state: int
    
    def __init__(self):
        self.state = RibbonGalleryItemState.Normal
    
    def measure(self, rect: Rect):
        """
        Measure the given rectangle by in-place modify.
        """
    
    def host(self, ribbon: 'Ribbon', rect: Rect):
        """
        The gallery item is being hosted in ribbon gallery.
        """
    
    def paint(self, dc: DC, state: int):
        """
        Paint the gallery item.
        """
    
    def hide(self):
        """
        Hide the gallery item.
        """

class RibbonGallery:
    elements: list[RibbonGalleryItem]
    margins: Margins
    name: str
    gallery_font: Font
    
    def __init__(self, name: str, elements: list[RibbonGalleryItem] = []):
        self.elements = elements
        self.margins = Margins(5, 5, 5, 0)
        self.name = name
        
        logfont = VisualStyleElements.Status.Bar.NORMAL.get_system_font(TMT_STATUSFONT)
        self.gallery_font = Font.indirect(logfont)

    def paint(self, dc: DC, rect: Rect, item_ht_map: list[tuple[Rect, RibbonGalleryItem]]):
        rect = rect.copy()
        with dc.select_ex(self.gallery_font):
            width, height = dc.get_text_extent_point(self.name).width
        rect.bottom

class RibbonView:
    galleries: list[RibbonGallery]
    background_color: Color.BGR
    text_color: Color.BGR
    bk_brush: Brush
    name: str
    
    def __init__(self, name: str, galleries: list[RibbonGallery] = []):
        self.name = name
        self.galleries = galleries
        self.background_color = Color.BGR.from_id(Color.ID.Control)
        self.text_color = Color.BGR.from_id(Color.ID.InfoText)
        self.bk_brush = Brush.create(self.background_color)
        
    def paint(self, dc: DC, rect: Rect, item_ht_map: list[tuple[Rect, RibbonGalleryItem]]):
        """
        Paint the ribbon view.
        """
        dc.fill(rect, self.bk_brush)
        for gallery in self.galleries:
            gallery.paint(dc, rect, item_ht_map)

class Ribbon(Window):
    tabs: TabControl | None
    views: list[RibbonView]
    current: RibbonView | None
    _height: int
    item_ht_map: list[tuple[Rect, RibbonGalleryItem]]
    
    def __init__(self, height: int):
        super().__init__()
        self.on_create += self.ribbon_created
        self._height = height
        self.views = []
        self.current = None
        self.tabs = None
        self.item_ht_map = []
        
    def ribbon_created(self) -> bool:
        self.tabs = TabControl()
        return True
    
    def create(self, parent: int | HANDLE, identifier: int | HMENU):
        if not isinstance(parent, Window):
            parent = Window.foreign(parent)
        super().create(parent.width, self._height, 0, 0, NULL, parent, identifier)
        
    def on_paint(self, dc: PaintDC) -> bool:
        self.item_ht_map.clear()
        if self.current is None and len(self.views):
            self.current = self.views[0]
        else: return True
        display = self.tabs.adjust_display(self.client_rect)
        with dc.create_compatible_bitmap(display.width, display.height) as bmp:
            with dc.create_compatible() as mem_dc:
                with mem_dc.select_ex(bmp):
                    self.current.paint(mem_dc, display, self.item_ht_map)
                    dc.bit_blt(display.x, display.y, 0, 0, display.width, display.height, mem_dc, SRCCOPY)
        return True
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        if self.tabs:
            self.tabs.size = (width, height)
        return True
    
    def add(self, view: RibbonView):
        self.views.append(view)
        self.tabs.insert(len(self.views), view.name)
    
    def set(self, index: int):
        self.current = self.views[index]