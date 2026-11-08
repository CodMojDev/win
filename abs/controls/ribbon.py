#
# WinAbs Ribbons \ Under construction
#

from win.abs.window import *
from win.abs.tabctl import *
from win.abs.core.gdiplus import *
from win.abs.combobox import *
from win.abs.button import *

class RibbonGalleryItemState:
    Normal = 0
    Highlight = 1
    Pushed = 2
    Disabled = 3

    HighlightAsAfterPushed = 128

RGIP_NORMAL = 0
RGIP_PAINTABLE = 1

class RibbonGalleryItem:
    """
    Ribbon gallery item.
    """
    
    state: int
    x: int
    y: int
    width: int
    height: int
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.state = RibbonGalleryItemState.Normal
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def measure(self, rect: Rect):
        """
        Measure the given rectangle by in-place modify.
        """
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        """
        The gallery item is being hosted in ribbon gallery.
        """
    
    def paint(self, dc: DC, rect: Rect):
        """
        Paint the gallery item.
        """
    
    def show(self):
        """
        Show the gallery item.
        """
    
    def hide(self):
        """
        Hide the gallery item.
        """
        
    def preferences(self) -> int:
        """
        Get gallery item preferences.
        """
        return RGIP_NORMAL

class IRibbonGalleryFoldListener:
    @interface_abstract_method
    def fold(self): pass
    
    @interface_abstract_method
    def unfold(self): pass

class RibbonGalleryItemText(RibbonGalleryItem):
    text: str
    ribbon: TUnion['Ribbon', None]
    gallery_rect: Rect | None
    format: int
    color: Color.BGR
    
    def __init__(self, x: int, y: int, width: int, height: int, 
                 text: int = 'Text', font: Font | None = None, 
                 format: int = DT_LEFT, color: Color.BGR = Color.BGR.from_id(Color.ID.Black)):
        super().__init__(x, y, width, height)
        self.text = text
        self.ribbon = None
        self.gallery_rect = None
        if font is None:
            font = Font.create('Arial', 16)
        self.font = font
        self.format = format
        self.color = color
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        if self.ribbon is None:
            self.ribbon = ribbon
        if self.gallery_rect != gallery.rect:
            self.gallery_rect = gallery.rect
    
    def measure(self, rect: Rect):
        rect.width = min(self.gallery_rect.width, rect.width)
    
    def paint(self, dc: DC, rect: Rect):
        with Gdiplus.Graphics.create(dc) as graphics:
            graphics.clear(Color.ARGB.from_id(Color.ID.White))
            graphics.smoothing_mode = SmoothingModeAntiAlias
            with Gdiplus.StringFormat.generic() as string_format:
                string_format.trimming = StringTrimmingEllipsisWord
                string_format.flags = StringFormatFlagsNoWrap
                if self.format & DT_LEFT:
                    string_format.align = StringAlignmentNear
                elif self.format & DT_RIGHT:
                    string_format.align = StringAlignmentFar
                elif self.format & DT_CENTER:
                    string_format.align = StringAlignmentCenter
                if self.format & DT_TOP:
                    string_format.line_align = StringAlignmentNear
                elif self.format & DT_BOTTOM:
                    string_format.line_align = StringAlignmentFar
                elif self.format & DT_VCENTER:
                    string_format.line_align = StringAlignmentCenter
                with Gdiplus.Font.from_font(self.font, dc) as font:
                    with Gdiplus.SolidBrush.create(self.color) as brush:
                        graphics.draw_string(self.text, font, rect, brush, string_format)
    
    def preferences(self) -> int:
        return RGIP_PAINTABLE

class RibbonGalleryItemButton(RibbonGalleryItem, IRibbonGalleryFoldListener):
    class IconAlignment:
        Left = 0
        Top = 1
        Right = 2
        Bottom = 3
    
    image: Gdiplus.Image | None
    text: str | None
    icon_alignment: int
    ribbon: TUnion['Ribbon', None]
    gallery_rect: Rect | None
    on_click: MultiEvent
    tracking_mouse: bool
    font: Font
    icon_margins: Margins
    gallery: TUnion['RibbonGallery', None]
    
    def __init__(self, x: int, y: int, width: int, height: int,
                 text: str | None = None, image: Bitmap | Icon | None = None,
                 icon_alignment: int = IconAlignment.Top,
                 font: Font | None = None):
        super().__init__(x, y, width, height)
        self.text = text
        if image is not None:
            if isinstance(image, Icon):
                image = Gdiplus.Bitmap.from_hicon(image)
            elif isinstance(image, Bitmap):
                image = Gdiplus.Bitmap.from_hbitmap(image)
        self.image = image
        self.icon_alignment = icon_alignment
        self.ribbon = None
        self.gallery_rect = None
        self.on_click = MultiEvent()
        self.tracking_mouse = False
        if font is None:
            font = Font.create('Arial', 16)
        self.font = font
        self.icon_margins = Margins(3, 3, 3, 3)
        self.gallery = None
    
    def fold(self):
        self.ribbon.render_area.on_mouse_move -= self.on_mouse_move
        self.ribbon.render_area.on_left_button_down -= self.on_left_button_down
        self.ribbon.render_area.on_left_button_up -= self.on_left_button_up
        self.ribbon.render_area.on_mouse_leave -= self.on_mouse_leave
        
        self.gallery.window.on_mouse_move += self.on_mouse_move
        self.gallery.window.on_left_button_down += self.on_left_button_down
        self.gallery.window.on_left_button_up += self.on_left_button_up
        self.gallery.window.on_mouse_leave += self.on_mouse_leave
    
    def unfold(self):
        self.gallery.window.on_mouse_move -= self.on_mouse_move
        self.gallery.window.on_left_button_down -= self.on_left_button_down
        self.gallery.window.on_left_button_up -= self.on_left_button_up
        self.gallery.window.on_mouse_leave -= self.on_mouse_leave
        
        self.ribbon.render_area.on_mouse_move += self.on_mouse_move
        self.ribbon.render_area.on_left_button_down += self.on_left_button_down
        self.ribbon.render_area.on_left_button_up += self.on_left_button_up
        self.ribbon.render_area.on_mouse_leave += self.on_mouse_leave
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        if self.ribbon is None:
            self.ribbon = ribbon
            self.ribbon.render_area.on_mouse_move += self.on_mouse_move
            self.ribbon.render_area.on_left_button_down += self.on_left_button_down
            self.ribbon.render_area.on_left_button_up += self.on_left_button_up
            self.ribbon.render_area.on_mouse_leave += self.on_mouse_leave
        if self.gallery is None:
            self.gallery = gallery
        if self.gallery_rect != gallery.rect:
            self.gallery_rect = gallery.rect
    
    def on_mouse_move(self, flags: int, x: int, y: int):
        if self.state == RibbonGalleryItemState.Disabled: return
        if self.ribbon.hit_element(x, y) == self:
            if self.state == RibbonGalleryItemState.Normal:
                self.state = RibbonGalleryItemState.Highlight
                self.ribbon.render_area.invalidate(self.gallery_rect)
            elif self.state & RibbonGalleryItemState.HighlightAsAfterPushed:
                self.state = RibbonGalleryItemState.Pushed
                self.ribbon.render_area.invalidate(self.gallery_rect)
        else:
            if self.state == RibbonGalleryItemState.Pushed:
                self.state = RibbonGalleryItemState.Highlight | RibbonGalleryItemState.HighlightAsAfterPushed
                self.ribbon.render_area.invalidate(self.gallery_rect)
            elif self.state != RibbonGalleryItemState.Normal:
                if not (self.state & RibbonGalleryItemState.HighlightAsAfterPushed):
                    self.state = RibbonGalleryItemState.Normal
                    self.ribbon.render_area.invalidate(self.gallery_rect)
            
    def on_left_button_down(self, flags: int, x: int, y: int):
        if self.state == RibbonGalleryItemState.Disabled: return
        if self.ribbon.hit_element(x, y) == self:
            if self.state != RibbonGalleryItemState.Pushed:
                if not self.tracking_mouse:
                    self.tracking_mouse = True
                    Mouse.track(self.ribbon.render_area, TME_LEAVE)
                self.state = RibbonGalleryItemState.Pushed
                self.ribbon.render_area.invalidate(self.gallery_rect)
                
    def on_left_button_up(self, flags: int, x: int, y: int):
        if self.state == RibbonGalleryItemState.Disabled: return
        if self.ribbon.hit_element(x, y) == self:
            if self.state == RibbonGalleryItemState.Pushed:
                self.state = RibbonGalleryItemState.Highlight
                self.on_click.execute()
                self.ribbon.render_area.invalidate(self.gallery_rect)
        else:
            if self.state & RibbonGalleryItemState.HighlightAsAfterPushed:
                self.state = RibbonGalleryItemState.Normal
                self.ribbon.render_area.invalidate(self.gallery_rect)
                
    def on_mouse_leave(self):
        self.tracking_mouse = False
        if self.state == RibbonGalleryItemState.Disabled: return
        if self.state == RibbonGalleryItemState.Pushed:
            self.state = RibbonGalleryItemState.Normal
            self.ribbon.render_area.invalidate(self.gallery_rect)
        elif self.state & RibbonGalleryItemState.Highlight:
            self.state = RibbonGalleryItemState.Normal
            self.ribbon.render_area.invalidate(self.gallery_rect)
    
    def paint(self, dc: DC, rect: Rect):
        with Gdiplus.Graphics.create(dc) as graphics:
            graphics.clear(Color.ARGB.from_id(Color.ID.White))
            graphics.compositing_mode = CompositingModeSourceOver
            if self.image is not None:
                attributes = Gdiplus.ImageAttributes.create()
            if self.state == RibbonGalleryItemState.Disabled:
                if self.image is not None:
                    color = ((0.299, 0.299, 0.299, 0.0, 0.0),
                             (0.587, 0.587, 0.587, 0.0, 0.0),
                             (0.114, 0.114, 0.114, 0.0, 0.0),
                             (0.0, 0.0, 0.0, 1.0, 0.0),
                             (0.0, 0.0, 0.0, 0.0, 1.0))
                    attributes.set_color_matrix(None, color, ColorAdjustTypeBitmap)
            elif self.state != RibbonGalleryItemState.Normal:
                if self.state & RibbonGalleryItemState.Highlight:
                    color = Color.ARGB.color(0, 120, 212, 25)
                    with Gdiplus.SolidBrush.create(color) as brush:
                        graphics.fill(rect, brush)
                    with Gdiplus.Pen.create(Color.ARGB.color(color.r, color.g, color.b, 200), 1.0) as pen:
                        graphics.draw_rectangle(rect.copy().deflate_rect(1, 1), pen)
                elif self.state == RibbonGalleryItemState.Pushed:
                    color = Color.ARGB.color(0, 120, 212, 51)
                    with Gdiplus.SolidBrush.create(color) as brush:
                        graphics.fill(rect, brush)
                    with Gdiplus.Pen.create(Color.ARGB.color(color.r, color.g, color.b, 200), 1.0) as pen:
                        graphics.draw_rectangle(rect.copy().deflate_rect(1, 1), pen)
            if self.text is not None:
                string_format = Gdiplus.StringFormat.generic()
                string_format.trimming = StringTrimmingEllipsisCharacter
                string_format.align = StringAlignmentCenter
                string_format.line_align = StringAlignmentCenter
                font = Gdiplus.Font.from_font(self.font, dc)
                brush = Gdiplus.SolidBrush.create(Color.ARGB.from_id(Color.ID.Black))
            if self.image is None:
                if self.text is not None:
                    graphics.smoothing_mode = SmoothingModeAntiAlias
                    text_rect = rect.copy()
                    if self.state == RibbonGalleryItemState.Pushed:
                        text_rect.offset_rect(1, 1)
                    graphics.draw_string(self.text, font, text_rect, brush, string_format)
            else:
                width = self.image.width
                height = self.image.height
                if self.text is None:
                    bounds = Rect(rect.x+self.icon_margins.left, 
                                  rect.y+self.icon_margins.top,
                                  rect.right-self.icon_margins.right,
                                  rect.bottom-self.icon_margins.bottom)
                else:
                    bounds = Rect.create(0, 0, width, height)
                    if self.icon_alignment == self.IconAlignment.Left:
                        place_rect = Rect.create(
                            rect.x, rect.y,
                            width, rect.height)
                    elif self.icon_alignment == self.IconAlignment.Top:
                        place_rect = Rect.create(
                            rect.x, rect.y,
                            rect.width, height)
                    elif self.icon_alignment == self.IconAlignment.Right:
                        place_rect = Rect.create(
                            rect.right - width, rect.y,
                            width, rect.height)
                    elif self.icon_alignment == self.IconAlignment.Bottom:
                        place_rect = Rect.create(
                            rect.x, rect.bottom - height,
                            rect.width, height)
                    margins = self.icon_margins.copy()
                    if self.icon_alignment == self.IconAlignment.Left:
                        margins.right = 0
                    elif self.icon_alignment == self.IconAlignment.Top:
                        margins.bottom = 0
                    elif self.icon_alignment == self.IconAlignment.Right:
                        margins.left = 0
                    elif self.icon_alignment == self.IconAlignment.Bottom:
                        margins.top = 0
                    place_rect.offset_rect(margins.left, margins.top)
                    place_rect.deflate_rect(margins.right, margins.bottom)
                    bounds.x = place_rect.x + ((place_rect.width - bounds.width) // 2)
                    bounds.y = place_rect.y + ((place_rect.height - bounds.height) // 2)
                    if self.icon_alignment == self.IconAlignment.Left:
                        text_rect = Rect(bounds.right, rect.y, rect.right, rect.bottom)
                    elif self.icon_alignment == self.IconAlignment.Top:
                        text_rect = Rect(rect.x, bounds.bottom, rect.right, rect.bottom)
                    elif self.icon_alignment == self.IconAlignment.Right:
                        text_rect = Rect(rect.x, rect.y, bounds.x, rect.bottom)
                    elif self.icon_alignment == self.IconAlignment.Bottom:
                        text_rect = Rect(rect.x, rect.y, rect.right, bounds.y)
                if self.state == RibbonGalleryItemState.Pushed:
                    bounds.offset_rect(1, 1)
                    if self.text is not None:
                        text_rect.offset_rect(1, 1)
                graphics.draw_image_ex(
                    self.image, 
                    Rect(0, 0, 
                         self.image.width, 
                         self.image.height), 
                    bounds, UnitPixel, attributes)
                if self.text is not None:
                    graphics.smoothing_mode = SmoothingModeAntiAlias
                    graphics.draw_string(self.text, font, text_rect, brush, string_format)
    
    def preferences(self) -> int:
        return RGIP_PAINTABLE

class RibbonGalleryItemWindowHost(RibbonGalleryItem):
    window: Window | None
    ribbon: TUnion['Ribbon', None]
    gallery_rect: Rect | None
    gallery: TUnion['RibbonGallery', None]
    on_hosted: MultiEvent
    
    def __init__(self, x: int, y: int, width: int, height: int, window: int | HANDLE | None = None):
        super().__init__(x, y, width, height)
        if window is not None and not isinstance(window, Window):
            window = Window.foreign(window)
        self.window = window
        self.ribbon = None
        self.gallery_rect = None
        self.gallery = None
        self.on_hosted = MultiEvent()
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        if self.ribbon is None:
            self.ribbon = ribbon
        if self.gallery is None:
            self.gallery = gallery
        if self.gallery_rect != gallery.rect:
            self.gallery_rect = gallery.rect
            self.recalculate(gallery.rect)
        
    def show(self):
        if self.window is not None and self.window.invisible:
            self.window.show()
        
    def hide(self):
        if self.window is not None and self.window.visible:
            self.window.hide()
    
    def recalculate(self, rect: Rect):
        if self.window is not None:
            width, height = self.window.size
            self.window.size = (min(rect.width, width), 
                                min(rect.height, height))
            parent = self.window.parent
            if self.gallery.folded:
                if parent == self.ribbon.render_area:
                    self.window.parent = self.gallery.window
                    x1, y1 = self.window.position
                    x2, y2 = self.gallery.rect.position
                    x1 = x1 - x2
                    y1 = y1 - y2
                    self.window.position = (x1, y1)
            else:
                if parent != self.ribbon.render_area:
                    self.window.parent = self.ribbon.render_area
                    x1, y1 = self.window.position
                    x2, y2 = self.gallery.rect.position
                    x1 = x1 + x2
                    y1 = y1 + y2
                    self.window.position = (x1, y1)

class RibbonGalleryItemCombobox(RibbonGalleryItemWindowHost, IRibbonGalleryFoldListener):
    variants: Iterable[str]
    current: int
    font: Font
    
    on_selection_changed: MultiEvent | None
    on_selection_canceled: MultiEvent | None
    on_selection_ok: MultiEvent | None
    
    def __init__(self, x: int, y: int, width: int, height: int, 
                 variants: Iterable[str] = [], current: int = 0,
                 font: Font | None = None):
        super().__init__(x, y, width, height)
        self.variants = variants
        self.current = current
        if font is None:
            font = Font.create('Arial', 16)
        self.font = font
        self.on_selection_changed = None
        self.on_selection_canceled = None
        self.on_selection_ok = None
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        super().host(ribbon, gallery)
        if self.window is None:
            self.window = Combobox(self.width, self.height, ribbon.render_area, Identifiers[f'WinAbs.Ribbon->Ribbon-Combobox[{id(self)}]'])
            self.window.styles.add(CBS_DROPDOWNLIST)
            self.window.create(gallery.rect.x+self.x, gallery.rect.y+self.y)
            for variant in self.variants:
                self.window.append(variant)
            self.window.current = self.current
            self.window.font = self.font
            self.on_selection_changed = self.window.on_selection_changed
            self.on_selection_canceled = self.window.on_selection_canceled
            self.on_selection_ok = self.window.on_selection_ok
            self.recalculate(gallery.rect)
            self.on_hosted.execute()

class RibbonGalleryItemCheckbox(RibbonGalleryItemWindowHost, IRibbonGalleryFoldListener):
    font: Font
    checked: bool
    text: str
    on_click: MultiEvent | None
    
    def __init__(self, x: int, y: int, width: int, height: int,
                 text: str = '', checked: bool = False, font: Font | None = None):
        super().__init__(x, y, width, height)
        self.text = text
        self.checked = checked
        if font is None:
            font = Font.create('Arial', 16)
        self.font = font
        self.on_click = None
    
    def host(self, ribbon: 'Ribbon', gallery: 'RibbonGallery'):
        super().host(ribbon, gallery)
        if self.window is None:
            self.window = Checkbox(self.width, self.height, ribbon.render_area, Identifiers[f'WinAbs.Ribbon->Ribbon-Button[{id(self)}]'], self.text, True)
            self.window.create(gallery.rect.x+self.x, gallery.rect.y+self.y)
            if self.checked:
                self.window.click()
            self.on_click = self.window.on_click
            self.recalculate(gallery.rect)
            self.on_hosted.execute()

class RibbonGalleryFoldedWindow(Window):
    gallery: 'RibbonGallery'
    
    def __init__(self, gallery: 'RibbonGallery'):
        super().__init__()
        self.gallery = gallery
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add(WS_POPUP)
    
    def create(self):
        rect = self.gallery.rect.relative()
        super().create(
            rect.width,
            rect.height,
            rect.x, rect.bottom, NULL)
    
    def on_paint(self, dc: PaintDC) -> bool:
        self.gallery.paint(dc, self.gallery.rect.relative(), [], self.gallery.ribbon)
        return True
    
    def on_erase_background(self, dc: DC) -> bool:
        return True

class RibbonGallery:
    elements: list[RibbonGalleryItem]
    name: str
    gallery_font: Font
    width: int
    rect: Rect | None
    folded: bool
    image: Gdiplus.Image | None
    window: RibbonGalleryFoldedWindow | None
    ribbon: TUnion['Ribbon', None]
    item_ht_map: list[tuple[Rect, RibbonGalleryItem]]
    
    def __init__(self, name: str, width: int, elements: list[RibbonGalleryItem] = [],
                 image: Bitmap | Icon | Gdiplus.Image | None = None):
        if image is not None:
            if isinstance(image, Icon):
                image = Gdiplus.Bitmap.from_hicon(image)
            elif isinstance(image, Bitmap):
                image = Gdiplus.Bitmap.from_hbitmap(image)
        self.image = image
        self.elements = elements
        self.name = name
        self.width = width
        self.item_ht_map = []
        
        self.gallery_font = Font.create('Arial', 14, weight=FW_BOLD)
        self.rect = None
        self.folded = False
        self.window = None
        self.ribbon = None

    def host(self, ribbon: 'Ribbon', rect: Rect):
        if self.ribbon is None:
            self.ribbon = ribbon
        if self.rect != rect:
            self.rect = rect.copy()

    def paint(self, dc: DC, rect: Rect, item_ht_map: list[tuple[Rect, RibbonGalleryItem]], ribbon: 'Ribbon'):
        rect = rect.copy()
        y = rect.top
        with Pen.create(PS_SOLID, 1, Color.BGR.from_id(Color.ID.Gray)) as pen_Gray:
            with Brush.create(Color.BGR.from_id(Color.ID.Control)) as brush_Control:
                with dc.select_ex(pen_Gray), dc.select_ex(Brush.stock(NULL_BRUSH)):
                    dc.rectangle(rect)
                    rect.top = rect.bottom - 19
                    dc.fill(rect.copy().deflate_rect(1, 1), brush_Control)
        if self.name:
            with dc.select_ex(self.gallery_font):
                with dc.set_bk_mode_ex(TRANSPARENT), dc.set_text_color_ex(Color.BGR.from_id(Color.ID.InfoText)):
                    dc.draw_text(self.name, rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER | DT_WORD_ELLIPSIS)
        rect.top = y
        rect.bottom -= 19
        self.item_ht_map.clear()
        for element in self.elements:
            draw_rect = Rect.create(element.x, element.y, element.width, element.height)
            draw_rect.right = min(rect.right-rect.left, draw_rect.right)
            draw_rect.bottom = min(rect.bottom-rect.top, draw_rect.bottom)
            element.host(ribbon, self)
            element.show()
            preferences = element.preferences()
            if preferences & RGIP_PAINTABLE:
                element.measure(draw_rect)
                window_draw_rect = Rect.create(rect.x+draw_rect.x, rect.y+draw_rect.y, draw_rect.width, draw_rect.height)
                item_ht_map.append((window_draw_rect, element))
                self.item_ht_map.append((draw_rect.copy().offset_rect(rect.x, rect.y), element))
                memory = MemoryIO()
                info = BitmapInfo(draw_rect.width, draw_rect.height, 32)
                with Bitmap.section(info, memory, dc=dc) as mem_bmp:
                    with dc.create_compatible() as mem_dc:
                        mem_dc.select(mem_bmp)
                        element.paint(mem_dc, draw_rect.relative())
                        dc.alpha_blend(window_draw_rect,
                                       draw_rect.relative(), mem_dc)

    def fold(self):
        self.window = RibbonGalleryFoldedWindow(self)
        self.window.create()
        self.window.hide()
        self.folded = True
        for element in self.elements:
            if isinstance(element, IRibbonGalleryFoldListener):
                element.fold()
    
    def unfold(self):
        self.window.close()
        self.folded = False
        for element in self.elements:
            if isinstance(element, IRibbonGalleryFoldListener):
                element.unfold()

    def invalidate(self, rect: RECT | None = None):
        if rect is None:
            rect = self.rect
        if self.window is not None:
            self.window.invalidate(rect.relative() if rect is not None else None)
        elif not self.folded and self.ribbon is not None:
            self.ribbon.invalidate(rect)

class RibbonView:
    galleries: list[RibbonGallery]
    background_color: Color.BGR
    text_color: Color.BGR
    bk_brush: Brush
    name: str
    
    def __init__(self, name: str, galleries: list[RibbonGallery] = []):
        self.name = name
        self.galleries = galleries
        self.background_color = Color.BGR.from_id(Color.ID.White)
        self.bk_brush = Brush.create(self.background_color)
        
    def paint(self, dc: DC, rect: Rect, item_ht_map: list[tuple[Rect, RibbonGalleryItem]], ribbon: 'Ribbon'):
        """
        Paint the ribbon view.
        """
        width = ribbon.width
        rect = rect.copy()
        dc.fill(rect, self.bk_brush)
        rect.y += 3
        is_boundary = False
        for gallery in self.galleries:
            if rect.right > width:
                if is_boundary:
                    break
                is_boundary = True
            if gallery.folded:
                with Gdiplus.Graphics.create(dc) as graphics:
                    with Gdiplus.Font.from_font(gallery.gallery_font, dc) as font:
                        bounds, *_ = graphics.measure_string(gallery.name, font)
                        bounds = Gdiplus.RectF_to_Rect(bounds)
                        bounds.offset_rect(-2, -2)
                        bounds.inflate_rect(2, 2)
                        
            else:
                rect.width = gallery.width
                gallery.host(ribbon, rect)
                gallery.paint(dc, rect, item_ht_map, ribbon)
                rect.x += rect.width + 3

class RibbonRenderArea(Control):
    ribbon: 'Ribbon'
    
    def __init__(self, parent: 'Ribbon'):
        super().__init__(parent, Identifiers['WinAbs.Ribbon->Render-Area'])
        self.ribbon = parent
    
    def create(self, rect: Rect):
        super().create(rect.width, rect.height, rect.x, rect.y, NULL)
        
    def on_paint(self, dc: PaintDC) -> bool:
        self.ribbon.item_ht_map.clear()
        if self.ribbon.current is None:
            if len(self.ribbon.views):
                self.ribbon.current = self.ribbon.views[0]
            else:
                return True
        self.ribbon.current.paint(dc, self.client_rect, self.ribbon.item_ht_map, self.ribbon)
        return True
    
    def on_erase_background(self, dc: DC) -> bool:
        return True

class Ribbon(Control):
    tabs: TabControl | None
    views: list[RibbonView]
    current: RibbonView | None
    _height: int
    item_ht_map: list[tuple[Rect, RibbonGalleryItem]]
    
    def __init__(self, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self.on_create += self.ribbon_created
        self._height = height
        self.views = []
        self.current = None
        self.tabs = None
        self.item_ht_map = []
        
    def ribbon_created(self) -> bool:
        width, height = self.size
        self.tabs = TabControl(width, height, self, Identifiers['WinAbs.Ribbon->Tab-Control'])
        self.tabs.styles.add(WS_CLIPSIBLINGS)
        self.tabs.create(0, 0)
        self.tabs.on_selection_changed += self.tab_changed
        logfont = VisualStyleElements.Status.Bar.NORMAL.get_system_font(TMT_STATUSFONT)
        self.tabs_font = self.tabs.font = Font.indirect(logfont)
        self.render_area = RibbonRenderArea(self)
        self.render_area.create(self.tabs.adjust_display(Rect(0, 0, width, height)))
        return True
    
    def create(self):
        parent = self._parent
        if not isinstance(self._parent, Window):
            parent = Window.foreign(parent)
        super().create(parent.width, self._height, 0, 0, NULL)
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        if self.tabs:
            self.tabs.size = (width, height)
        if self.render_area:
            rect = self.tabs.adjust_display(Rect(0, 0, width, height))
            self.render_area.set_position(x=rect.x, y=rect.y, width=rect.width, height=rect.height)
        self.invalidate()
        return True
    
    def add(self, view: RibbonView):
        self.views.append(view)
        self.tabs.insert(len(self.views), view.name)
    
    def set(self, index: int):
        self.current = self.views[index]
        self.tabs.selected_tab = index
    
    def tab_changed(self):
        if self.current is not None:
            for gallery in self.current.galleries:
                for item in gallery.elements:
                    item.hide()
        self.current = self.views[self.tabs.selected_tab.index]
        self.invalidate()
        
    def on_erase_background(self, dc: DC) -> bool:
        return True
    
    def hit_element(self, x: int, y: int) -> RibbonGalleryItem | None:
        for rc, item in self.item_ht_map:
            if (x, y) in rc:
                return item
        return None