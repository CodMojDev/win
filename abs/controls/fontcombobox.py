from win.abs.combobox import *
from win.abs.imagelist import *
from win.abs.core.pixelbuffer import *

class FontCombobox(Combobox):
    pitch: int
    family: int
    type: int
    imagelist_Font: ImageList
    fonts: list[Logfont]
    draw_by_font: bool
    regular_height: int
    font_names: list[IWideCharArray]
    hfonts: list[Font]
    highlight_brush: Brush
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(width, height, parent, identifier)
        self.styles.add(CBS_DROPDOWN, CBS_HASSTRINGS, CBS_OWNERDRAWFIXED, WS_VSCROLL)
        self.pitch = DEFAULT_PITCH
        self.family = FF_DONTCARE
        self.type = RASTER_FONTTYPE | DEVICE_FONTTYPE | TRUETYPE_FONTTYPE
        
        self.imagelist_Font = ImageList.load(script_relative('data/fontcombobox.bmp'), 16, 2, Color.BGR.color(255, 255, 255))
        self.draw_by_font = True
        self.font_names = []
        self.hfonts = []
        
        nc_metrics = NONCLIENTMETRICSW()
        nc_metrics.cbSize = nc_metrics.size()
        SystemParametersInfoW(SPI_GETNONCLIENTMETRICS, 0, nc_metrics.ref(), FALSE)
        
        font = Font.indirect(nc_metrics.lfStatusFont)
        dc = DC.create_compatible(None)
        dc.select(font)
        
        self.regular_height = dc.metrics().height
        self.blit_maps = []
    
    def bind(self, parent: int | HANDLE | Window):
        window = super().bind(parent)
        if window is not None:
            window.on_draw_item += self.FontCombobox_on_draw_item
            window.on_measure_item += self.FontCombobox_on_measure_item
    
    def on_fully_created(self):
        self.highlight_brush = Brush.create(Color.BGR.from_id(Color.ID.Highlight))
        self.bk_brush = Brush.create(Color.BGR.from_id(Color.ID.Control))
        self.fonts = Logfont.enumerate(pitch=self.pitch, family=self.family, type=self.type)
        for font in self.fonts:
            if font.charset == MAC_CHARSET: continue
            buffer = create_unicode_buffer(font.name)
            self.font_names.append(buffer)
            self.append('').data = buffer
            self.hfonts.append(Font.indirect(font))
    
    def FontCombobox_on_draw_item(self, id: int, dis: DrawItemStruct):
        if not self: return
        if dis.item != self: return
        dc = dis.dc
        rect = dis.rect
        
        if dis.state & ODS_FOCUS:
            dc.draw_focus_rect(rect)
        
        with dc.transact():
            if dis.state & ODS_SELECTED:
                brush = self.highlight_brush
                dc.text_color = Color.BGR.from_id(Color.ID.HighlightText)
            else:
                brush = self.bk_brush
            
            dc.bk_mode = TRANSPARENT
            dc.fill(rect, brush)
            
            if dis.item_id >= 0:
                if dis.data:
                    font = self.fonts[dis.item_id]
                    if font.type & (DEVICE_FONTTYPE | TRUETYPE_FONTTYPE):
                        index = 0 if font.type & DEVICE_FONTTYPE else 1
                        self.imagelist_Font.draw(dc, index, rect.x, rect.y + (rect.height - 16) // 2)
                    font = font.copy()
                    rect.x += 16 + 6
                    
                    if self.draw_by_font and font.charset != SYMBOL_CHARSET:
                        if font.height < 0:
                            font.height -= 4
                        else:
                            font.height += 4
                        old_font = dc.select(self.hfonts[dis.item_id])
                    else:
                        old_font = None
                
                    try:
                        text = i_cast(dis.data, LPCWSTR).value
                        dc.draw_text(text, rect, DT_SINGLELINE | DT_VCENTER | DT_NOPREFIX)
                    finally:
                        if old_font is not None:
                            dc.select(old_font)
    
    def FontCombobox_on_measure_item(self, id: int, mis: MeasureItemStruct):
        if not self: return
        if mis.item != self: return
        mis.width = self.width
        mis.height = max(16, self.regular_height)