from win.abs.window import *

import time

class ArrowType:
    Vertical = 1
    Horizontal = 2
    PlusMinus = 4

class ArrowControl(Control):
    _width: int
    _height: int
    display_type: int
    
    hovered_0: bool
    hovered_1: bool
    pressed_0: bool
    pressed_1: bool
    disabled_0: bool
    disabled_1: bool
    mouse_tracked: bool
    has_uxtheme: bool
    
    on_0_clicked: MultiEvent
    on_1_clicked: MultiEvent
    
    hold_interval: float
    click_time_0: float
    click_time_1: float
    hold_timer_rate: float
    hold_timer_id: int
    hold_delay: float
    hold_delay_in_work: bool
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU, display_type: int = ArrowType.Vertical):
        super().__init__(parent, identifier)
        
        self._width = width
        self._height = height
        self.display_type = display_type
        
        self.hovered_0 = False
        self.hovered_1 = False
        self.pressed_0 = False
        self.pressed_1 = False
        self.disabled_0 = False
        self.disabled_1 = False
        self.mouse_tracked = False
        self.ArrowControl_reload_themes(False)
        
        self.on_0_clicked = MultiEvent()
        self.on_1_clicked = MultiEvent()
        
        self.hold_interval = 0.1
        self.click_time_0 = 0.0
        self.click_time_1 = 0.0
        self.hold_timer_rate = 0.1
        self.hold_timer_id = 0
        self.hold_delay = 0.3
        self.hold_delay_in_work = False
        
        self.on_mouse_move += self.ArrowControl_on_mouse_move
        self.on_left_button_down += self.ArrowControl_on_left_button_down
        self.on_left_button_up += self.ArrowControl_on_left_button_up
        self.on_mouse_leave += self.ArrowControl_on_mouse_leave
        self.on_theme_changed += self.ArrowControl_on_theme_changed
    
    def ArrowControl_reload_themes(self, refresh: bool):
        if isinstance(uxtheme, NullLibrary):
            self.has_uxtheme = False
        else:
            try:
                Theme.create(None, 'TREEVIEW')
                Theme.create(None, 'SPIN')
                self.has_uxtheme = True
            except WinException:
                self.has_uxtheme = False
        if self.has_uxtheme:
            if refresh:
                VisualStyleElement.refresh()
    
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, None, relative)
    
    def ArrowControl_get_rects(self) -> tuple[Rect, Rect]:
        rc_0 = self.client_rect
        rc_1 = rc_0.copy()
        if self.display_type & ArrowType.Vertical:
            bottom = rc_0.bottom
            rc_0.bottom //= 2
            rc_1.top = bottom - rc_0.bottom
        elif self.display_type & ArrowType.Horizontal:
            right = rc_0.right
            rc_0.right //= 2
            rc_1.left = right - rc_0.right
        return rc_0, rc_1
    
    def ArrowControl_hold_timer_tick(self, *_):
        if self.click_time_0 != 0.0 and self.pressed_0:
            t0 = self.click_time_0
            t1 = self.click_time_0 = time.perf_counter()
            while t1 - t0 >= self.hold_interval:
                t0 += self.hold_interval
                self.on_0_clicked.execute()
        if self.click_time_1 != 0.0 and self.pressed_1:
            t0 = self.click_time_1
            t1 = self.click_time_1 = time.perf_counter()
            while t1 - t0 >= self.hold_interval:
                t0 += self.hold_interval
                self.on_1_clicked.execute()
    
    def on_paint(self, dc: PaintDC) -> bool:
        rc_0, rc_1 = self.ArrowControl_get_rects()
        if self.has_uxtheme:
            if self.display_type & ArrowType.PlusMinus:
                vs_0 = VisualStyleElements.TreeView.Glyph.CLOSED
                vs_1 = VisualStyleElements.TreeView.Glyph.OPENED
            elif self.display_type & ArrowType.Vertical:
                if self.disabled_0:
                    vs_0 = VisualStyleElements.Spin.Up.DISABLED
                elif self.pressed_0:
                    vs_0 = VisualStyleElements.Spin.Up.PRESSED
                elif self.hovered_0:
                    vs_0 = VisualStyleElements.Spin.Up.HOT
                else:
                    vs_0 = VisualStyleElements.Spin.Up.NORMAL
                if self.disabled_1:
                    vs_1 = VisualStyleElements.Spin.Down.DISABLED
                elif self.pressed_1:
                    vs_1 = VisualStyleElements.Spin.Down.PRESSED
                elif self.hovered_1:
                    vs_1 = VisualStyleElements.Spin.Down.HOT
                else:
                    vs_1 = VisualStyleElements.Spin.Down.NORMAL
            elif self.display_type & ArrowType.Horizontal:
                if self.disabled_0:
                    vs_0 = VisualStyleElements.Spin.UpHorizontal.DISABLED
                elif self.pressed_0:
                    vs_0 = VisualStyleElements.Spin.UpHorizontal.PRESSED
                elif self.hovered_0:
                    vs_0 = VisualStyleElements.Spin.UpHorizontal.HOT
                else:
                    vs_0 = VisualStyleElements.Spin.UpHorizontal.NORMAL
                if self.disabled_1:
                    vs_1 = VisualStyleElements.Spin.DownHorizontal.DISABLED
                elif self.pressed_1:
                    vs_1 = VisualStyleElements.Spin.DownHorizontal.PRESSED
                elif self.hovered_1:
                    vs_1 = VisualStyleElements.Spin.DownHorizontal.HOT
                else:
                    vs_1 = VisualStyleElements.Spin.DownHorizontal.NORMAL
            else:
                vs_0 = None
                vs_1 = None
            if vs_0 is not None:
                vs_0.draw_background(dc, rc_0)
            if vs_1 is not None:
                vs_1.draw_background(dc, rc_1)
        else:
            self.ArrowControl_draw_arrows(rc_0, rc_1, dc)
        return True
    
    def ArrowControl_on_mouse_move(self, flags: int, x: int, y: int):
        rc_0, rc_1 = self.ArrowControl_get_rects()
        if (x, y) in rc_0:
            self.hovered_0 = True
            self.hovered_1 = False
        elif (x, y) in rc_1:
            self.hovered_1 = True
            self.hovered_0 = False
        else:
            self.hovered_0 = False
            self.hovered_1 = False
        self.invalidate()
        if not self.mouse_tracked:
            Mouse.track(self, TME_LEAVE)
            self.mouse_tracked = True
    
    def ArrowControl_delayed_add_hold_timer(self, event_id: int, _):
        self.hold_delay_in_work = False
        self.kill_timer(event_id)
        if self.pressed_0 or self.pressed_1:
            self.hold_timer_id = self.timer(self.ArrowControl_hold_timer_tick, round(self.hold_timer_rate*1000))
    
    def ArrowControl_add_hold_timer(self):
        if self.hold_delay_in_work: return
        self.hold_delay_in_work = True
        if self.hold_timer_id != 0:
            self.kill_timer(self.hold_timer_id)
        self.timer(self.ArrowControl_delayed_add_hold_timer, round(self.hold_delay * 1000))
    
    def ArrowControl_on_left_button_down(self, flags: int, x: int, y: int):
        rc_0, rc_1 = self.ArrowControl_get_rects()
        if (x, y) in rc_0:
            self.pressed_0 = True
            self.hovered_0 = False
            self.pressed_1 = False
            self.hovered_1 = False
            self.click_time_0 = time.perf_counter()
            self.on_0_clicked.execute()
            self.ArrowControl_add_hold_timer()
            self.invalidate()
        elif (x, y) in rc_1:
            self.pressed_1 = True
            self.hovered_1 = False
            self.pressed_0 = False
            self.hovered_0 = False
            self.click_time_1 = time.perf_counter()
            self.on_1_clicked.execute()
            self.ArrowControl_add_hold_timer()
            self.invalidate()
        else:
            self.pressed_0 = False
            self.pressed_1 = False
            
    def ArrowControl_on_left_button_up(self, flags: int, x: int, y: int):
        rc_0, rc_1 = self.ArrowControl_get_rects()
        if (x, y) in rc_0 or (x, y) in rc_1:
            self.pressed_0 = False
            self.pressed_1 = False
            self.ArrowControl_on_mouse_move(flags, x, y)
            self.invalidate()
        if self.hold_timer_id != 0:
            self.kill_timer(self.hold_timer_id)
            self.hold_timer_id = 0
    
    def ArrowControl_on_mouse_leave(self):
        self.pressed_0 = False
        self.pressed_1 = False
        self.hovered_0 = False
        self.hovered_1 = False
        if self.hold_timer_id != 0:
            self.kill_timer(self.hold_timer_id)
            self.hold_timer_id = 0
        self.invalidate()
        self.mouse_tracked = False
        
    def ArrowControl_on_theme_changed(self):
        self.ArrowControl_reload_themes(True)
        self.invalidate()
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.invalidate()
        return True
    
    def on_erase_background(self, dc: DC) -> bool:
        return True
    
    def ArrowControl_draw_plus_minus(self, rc: Rect, plus: bool, dc: DC):
        width = rc.width
        height = rc.height
        
        size = min(width, height)
        if size < 5: return
        
        x = rc.x + (width - size) // 2
        y = rc.y + (height - size) // 2
        
        pen_width = max(1, size // 9)
        with Pen.create(PS_SOLID, pen_width, Color.BGR.from_id(Color.ID.ButtonShadow)) as pen:
            with Brush.create(Color.BGR.from_id(Color.ID.Control)) as brush:
                with dc.select_ex(pen):
                    with dc.select_ex(brush):
                        dc.rectangle(Rect.create(x, y, size, size))
                        with Pen.create(PS_SOLID, pen_width, Color.BGR.from_id(Color.ID.WindowText)) as pen_sign:
                            with dc.select_ex(pen_sign):
                                padding = size * 22 // 100
                                
                                middle_x = x + size // 2
                                middle_y = y + size // 2
                                
                                dc.move(x + padding, middle_y)
                                dc.line(x + size - padding, middle_y)
                                
                                if plus:
                                    dc.move(middle_x, y + padding)
                                    dc.line(middle_x, y + size - padding)
    
    def ArrowControl_draw_arrow_0(self, rc: Rect, dc: DC):
        if self.display_type & ArrowType.PlusMinus:
            self.ArrowControl_draw_plus_minus(rc, True, dc)
        elif self.display_type & ArrowType.Vertical:
            if self.disabled_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLUP | DFCS_INACTIVE)
            elif self.pressed_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLUP | DFCS_PUSHED)
            elif self.hovered_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLUP | DFCS_HOT)
            else:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLUP)
        elif self.display_type & ArrowType.Horizontal:
            if self.disabled_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLLEFT | DFCS_INACTIVE)
            elif self.pressed_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLLEFT | DFCS_PUSHED)
            elif self.hovered_0:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLLEFT | DFCS_HOT)
            else:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLLEFT)
    
    def ArrowControl_draw_arrow_1(self, rc: Rect, dc: DC):
        if self.display_type & ArrowType.PlusMinus:
            self.ArrowControl_draw_plus_minus(rc, False, dc)
        elif self.display_type & ArrowType.Vertical:
            if self.disabled_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLDOWN | DFCS_INACTIVE)
            elif self.pressed_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLDOWN | DFCS_PUSHED)
            elif self.hovered_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLDOWN | DFCS_HOT)
            else:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLDOWN)
        elif self.display_type & ArrowType.Horizontal:
            if self.disabled_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLRIGHT | DFCS_INACTIVE)
            elif self.pressed_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLRIGHT | DFCS_PUSHED)
            elif self.hovered_1:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLRIGHT | DFCS_HOT)
            else:
                dc.draw_frame_control(rc, DFC_SCROLL, DFCS_SCROLLRIGHT)
    
    def ArrowControl_draw_arrows(self, rc_0: Rect, rc_1: Rect, dc: DC):
        self.ArrowControl_draw_arrow_0(rc_0, dc)
        self.ArrowControl_draw_arrow_1(rc_1, dc)