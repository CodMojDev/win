from win.abs.window import *

class ToggleControl(Control):
    _width: int
    _height: int
    _toggled: bool
    _font: Font | None
    
    on_color: Color.BGR
    bk_color: Color.BGR
    on_slider_color: Color.BGR
    off_slider_color: Color.BGR
    on_text_color: Color.BGR
    off_text_color: Color.BGR
    
    border_color: Color.BGR
    border_width: int
    margin: int
    
    on: str
    off: str
    
    on_toggled: MultiEvent
    slider_width: int
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, toggled: bool = False, 
                 font: Font | None = None, on: str = 'ON', off: str = 'OFF'):
        super().__init__(parent, identifier)
        
        self._width = width
        self._height = height
        self._toggled = toggled
        self._font = font
        self.on = on
        self.off = off
        
        self.on_color = Color.BGR.from_id(Color.ID.Highlight)
        self.bk_color = Color.BGR.from_id(Color.ID.Control)
        self.border_color = Color.BGR.from_id(Color.ID.Gray)
        self.on_slider_color = Color.BGR.from_id(Color.ID.Control)
        self.off_slider_color = Color.BGR.from_id(Color.ID.Control)
        self.on_text_color = Color.BGR.from_id(Color.ID.White)
        self.off_text_color = Color.BGR.from_id(Color.ID.Black)
        
        self.border_width = 1
        self.slider_width = 12
        self.margin = 1
        
        self.class_style |= CS_HREDRAW | CS_VREDRAW
        
        self.on_left_button_down += self.ToggleControl_on_left_button_down
        self.on_set_font += self.ToggleControl_on_set_font
        self.on_toggled = MultiEvent()
    
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, None, relative)
    
    def _draw(self, dc: DC, rect: Rect, toggled: bool):
        rect = rect.copy()
        with Pen.create(PS_SOLID, self.border_width, self.border_color) as pen_Border:
            with Brush.create(self.bk_color) as brush_Background:
                with dc.select_ex(pen_Border), dc.select_ex(brush_Background):
                    dc.rectangle(rect)
            if toggled:
                area = Rect(rect.left + self.border_width + self.margin, 
                            rect.top + self.border_width + self.margin, 
                            rect.right - (self.slider_width - 1) - self.border_width - self.margin, 
                            rect.bottom - self.border_width - self.margin)
                with Brush.create(self.on_color) as brush_On:
                    with dc.select_ex(pen_Border), dc.select_ex(brush_On):
                        dc.rectangle(area)
                rect.left = rect.right - self.slider_width
                with Brush.create(self.on_slider_color) as brush_OnSlider:
                    with dc.select_ex(pen_Border), dc.select_ex(brush_OnSlider):
                        dc.rectangle(rect)
                with dc.select_ex(self._font):
                    with dc.set_bk_color_ex(self.on_color), dc.set_text_color_ex(self.on_text_color):
                        dc.draw_text(self.on, area, DT_SINGLELINE | DT_CENTER | DT_VCENTER)
            else:
                area = Rect(rect.left + (self.slider_width - 1) + self.border_width + self.margin, 
                            rect.top + self.border_width + self.margin, 
                            rect.right - self.border_width - self.margin, 
                            rect.bottom - self.border_width - self.margin)
                rect.right = rect.left + self.slider_width
                with Brush.create(self.off_slider_color) as brush_OffSlider:
                    with dc.select_ex(pen_Border), dc.select_ex(brush_OffSlider):
                        dc.rectangle(rect)
                with dc.select_ex(self._font):
                    with dc.set_bk_color_ex(self.bk_color), dc.set_text_color_ex(self.off_text_color):
                        dc.draw_text(self.off, area, DT_SINGLELINE | DT_CENTER | DT_VCENTER)
    
    def on_paint(self, dc: PaintDC) -> bool:
        self._draw(dc, self.client_rect, self._toggled)
        return True
    
    def on_erase_background(self, dc: DC) -> bool:
        return True
    
    def ToggleControl_on_left_button_down(self, flags: int, x: int, y: int):
        self._toggled = not self._toggled
        self.on_toggled.execute(self._toggled)
        self.invalidate()
        
    def ToggleControl_on_set_font(self, font: Font | None, redraw: bool):
        self._font = font
        if redraw:
            self.invalidate()
        
    @property
    def toggled(self) -> bool:
        return self._toggled
    
    @toggled.setter
    def toggled(self, toggled: bool):
        self._toggled = toggled
        self.invalidate()