from win.abs.window import *

import enum
import math

DEFAULT_WIDTH_OF_LUMINANCE_BAR = 20
DEFAULT_OFFSET_OF_LUMINANCE_BAR = 5
LUMINANCE_CURSOR_SIZE = 9
DEFAULT_LUMINANCE = 0.50
PICKER_CURSOR_SIZE = 19

GRAY_CELLS_NUM = 15 # + 2 (Black and white)
TAN30 = 0.57735026918962
PI = 3.14159265358979
YOFFSET = (1.5 * TAN30)
NUM_LEVELS = 7
CELL_EDGES = 6

CFX_OFFSET = [ -0.5, -1.0, -0.5, 0.5, 1.0, 0.5 ]
CFY_OFFSET = [ YOFFSET, 0.0, -YOFFSET, -YOFFSET, 0.0, YOFFSET ]

WHITE = Color.RGB.color(255, 255, 255)
BLACK = Color.RGB.color(0, 0, 0)
BITS_PER_PIXEL = 24

class CAbsColorPicker(Control):
    class ColorType(enum.Enum):
        HEX = 1
        HEX_GREYSCALE = 2
        CURRENT = 3
        PICKER = 4
        LUMINANCE = 5
        
    class Cell:
        palette: Palette
        color: Color.RGB
        width: int
        delta: int
        x: int
        y: int
        
        def align_color(self, part: int, delta: int) -> int:
            if delta == 0:
                return part
            
            if part < delta:
                return 0
            
            if part > 255 - delta:
                return 255
            
            if abs(part - 128) < delta:
                return 128
            
            if abs(part - 192) < delta:
                return 192
            
            return part
        
        def __init__(self, palette: Palette, color: Color.RGB, x: int, y: int, width: int, delta: int):
            self.palette = palette
            self.width = width
            self.delta = delta
            self.x = int(x)
            self.y = int(y)
            
            self.color = Color.RGB.color(
                self.align_color(color.r, delta), 
                self.align_color(color.g, delta),
                self.align_color(color.b, delta))
            
            self.draw_color = self.color
            self.points = []
            self.get_points(int(x), int(y), width, self.points)
        
        def get_points(self, x: int, y: int, width: int, points: GraphicUtils.PointArray):
            half_width = width // 2
            side_length = int(width * TAN30)
            temp = side_length // 2
            
            points.append((x - half_width, y - temp))
            points.append((x, y - half_width))
            points.append((x + half_width, y - temp))
            points.append((x + half_width, y + temp))
            points.append((x, y + half_width))
            points.append((x - half_width, y + temp))
        
        def hit(self, x: int, y: int) -> bool:
            return (x, y) in Region.polygon(self.points, ALTERNATE)
        
        def draw(self, dc: DC):
            brush = Brush.create(self.draw_color)
            pen = Pen.create(PS_SOLID, 1, self.draw_color)
            
            with dc.select_ex(brush), dc.select_ex(pen):
                dc.polygon(self.points)
                
        def draw_selected(self, dc: DC, focused: bool):
            white_brush = Brush.stock(WHITE_BRUSH if focused else GRAY_BRUSH)
            black_brush = Brush.stock(BLACK_BRUSH)
            
            array_two = []
            self.get_points(self.x, self.y - 1, self.width + 2, array_two)
            
            region_two = Region.polygon(array_two, ALTERNATE)
            dc.frame_region(region_two, white_brush, 2, 2)
            
            array_three = []
            self.get_points(self.x, self.y, self.width + 2, array_three)
            
            region_three = Region.polygon(array_three, ALTERNATE)
            dc.frame_region(region_three, black_brush, 1, 1)
            
            array_one = []
            self.get_points(self.x, self.y, self.width - 1, array_one)
            
            region_one = Region.polygon(array_one, ALTERNATE)
            dc.frame_region(region_one, black_brush, 1, 1)
        
    cells: list[Cell]
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, NULL, relative)
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HANDLE):
        super().__init__(parent, identifier)
        self.color_type = self.ColorType.HEX
        self.luminance_bar_width = DEFAULT_WIDTH_OF_LUMINANCE_BAR
        self.color_new = Color.RGB()
        self.color_original = Color.RGB()
        self.palette = None
        self.color_hsl = Color.HSL(luminance=DEFAULT_LUMINANCE)
        self.picker_bitmap = Bitmap()
        self.cells = []
        self._width = width
        self._height = height
        
        self.on_palette_changed += self.set_color_picker_palette
        self.on_erase_background += self.erase_color_picker_background
        self.on_left_button_down += self.picker_left_button_down
        self.on_left_button_up += self.picker_left_button_up
        self.on_mouse_move += self.picker_mouse_move
        self.on_paint += self.color_picker_paint
        self.on_size += self.picker_sized
        self.on_focus_lost += self.picker_focus_lost
        
    def color_picker_paint(self, dc_draw: PaintDC):
        current = dc_draw.select_palette(self.palette, False)
        dc_draw.realize.begin()
        
        clip = dc_draw.clip_box
        client_rect = i_cast_structure(dc_draw.paint_struct.rcPaint, Rect)
        
        with dc_draw.create_compatible() as dc:
            with dc_draw.create_compatible_bitmap(client_rect.width, client_rect.height) as bitmap:
                with dc.select_ex(bitmap):
                    current_mem = dc.select_palette(self.palette, False)
                    dc.realize.begin()
                    WindowUtils.draw_parent_background(self, dc)
                    if self.color_type == self.ColorType.HEX:
                        self.create_hexagon()
                        self.draw_hex(dc)
                    elif self.color_type == self.ColorType.HEX_GREYSCALE:
                        self.create_hex_grey_scale_bar()
                        self.draw_hex(dc)
                    elif self.color_type == self.ColorType.CURRENT:
                        text_color = dc.text_color
                        half = client_rect.height // 2
                        with Brush.create(self.color_new) as brush_new, Brush.create(self.color_original) as brush_original:
                            dc.fill(Rect.create(0, 0, client_rect.width, half), brush_new)
                            dc.fill(Rect.create(0, half, client_rect.width, half), brush_original)
                            # Draw frame
                            dc.draw_3d_rect(client_rect.left, client_rect.top, client_rect.width, client_rect.height,
                                            Color.system(COLOR_3DDKSHADOW), Color.system(COLOR_3DDKSHADOW))
                    elif self.color_type == self.ColorType.PICKER:
                        self.draw_picker(dc)
                        self.draw_cursor(dc, self.cursor_rect)
                        dc.draw_3d_rect(client_rect.left, client_rect.top, client_rect.width, client_rect.height,
                                        Color.system(COLOR_3DDKSHADOW), Color.system(COLOR_BTNHILIGHT))
                    elif self.color_type == self.ColorType.LUMINANCE:
                        self.draw_luminance_bar(dc)
                        
                        # Draw marker:
                        WindowUtils.draw_parent_background(self, dc, Rect.create(
                            self.luminance_bar_width, 0, client_rect.width - self.luminance_bar_width, client_rect.height))
                        self.draw_cursor(dc, self.cursor_rect)
                    
                    dc_draw.bit_blt(clip.left, clip.top, clip.left, clip.top, clip.width, clip.height, dc, SRCCOPY)
                    if current_mem:
                        dc.select_palette(current_mem, False)
                    
        if current:
            draw_dc.select_palette(current, FALSE)
    
    def create_hex_grey_scale_bar(self):
        if self.cells:
            return
        
        area = self.client_rect
        size = min(area.height // 2 - 2, area.width // (GRAY_CELLS_NUM // 2 + 6))
        if (size % 2) != 0:
            size += 1
        large_size = size * 2
        y_center = (area.top + area.bottom) // 2
        side_length = int(size * TAN30 * 1.5)
        y1 = y_center - side_length // 2
        y2 = y1 + side_length
        rgb_offset = 255 // (GRAY_CELLS_NUM + 2)
        start_offset = area.left
        for row_num in range(2):
            if row_num == 1:
                # Draw large white cell:
                x1 = start_offset + (large_size // 2)
                self.cells.append(self.Cell(self.palette, WHITE, x1, y_center, large_size, 0))
            x = large_size + size + start_offset
            curry = y1
            rgb = 255 - rgb_offset
            for i in range(GRAY_CELLS_NUM):
                color = Color.RGB.color(rgb, rgb, rgb)
                if row_num == 1:
                    self.cells.append(self.Cell(self.palette, color, x, curry, size, 7))
                x += (size // 2)
                curry = y2 if curry == y1 else y1
                rgb -= rgb_offset
            if row_num == 1:
                # Draw large black cell:
                x1 = (x + size + (size // 2)) - 1
                self.cells.append(self.Cell(self.palette, BLACK, x1, y_center, large_size, 0))
            x += large_size + (size // 2)
            if row_num == 0:
                start_offset = (area.right - x) // 2
    
    def notify_parent(self):
        return
        parent = self.parent
        if parent:
            parent.send(WM_COMMAND, MAKEWPARAM())
    
    def picker_focus_lost(self, focus_now: Window):
        self.invalidate()
        
    def picker_sized(self, type: int, width: int, height: int):
        if self.picker_bitmap:
            self.picker_bitmap.close()
            
        self.invalidate()
        self.update()
        
    def picker_left_button_down(self, flags: int, x: int, y: int):
        self.capturing = True
        self.focus()
        self.picker_mouse_move(flags, x, y)
        
    def picker_left_button_up(self, flags: int, x: int, y: int):
        if self.capturing:
            self.capturing = False
        
    def picker_mouse_move(self, flags: int, x: int, y: int):
        if not self.capturing:
            return
        
        client_rect = self.client_rect
        
        x = min(max(client_rect.left, x), client_rect.right)
        y = min(max(client_rect.top, y), client_rect.bottom)
        
        if self.color_type == self.ColorType.LUMINANCE:
            cursor_rect_old = self.cursor_rect
            cursor_rect_old.inflate(1, 1)
            
            self.color_hsl.luminance = self.luminance_from_point(y)
            self.color_new = self.color_hsl.rgb()
            
            self.invalidate(cursor_rect_old)
            self.invalidate(self.cursor_rect)
        elif self.color_type == self.ColorType.PICKER:
            cursor_rect_old = self.cursor_rect
            cursor_rect_old.inflate(1, 1)
            
            if flags & MK_CONTROL:
                x, _ = self.cursor_position
            
            if flags & MK_SHIFT:
                _, y = self.cursor_position
                
            self.hsl.hue = x / client_rect.width
            self.hsl.saturation = 1 - y / client_rect.height
            self.color_new = self.hsl.rgb()
            
            self.invalidate(cursor_rect_old)
            self.invalidate(self.cursor_rect)
        elif self.color_type in (self.ColorType.HEX, self.ColorType.HEX_GREYSCALE):
            if not self.select_cell_hexagon(x, y):
                return
            
            self.invalidate()
        
        self.notify_parent()
        self.update()
    
    def create_hexagon(self):
        if self.cells:
            return
        
        client_rect = self.client_rect
        
        # Normalize to squere
        if client_rect.height < client_rect.width:
            client_rect.deflate((client_rect.width - client_rect.height) / 2, 0)
        else:
            client_rect.deflate(0, (client_rect.height - client_rect.width) / 2)
            
        ASSERT((abs(client_rect.height) - client_rect.width) <= 1)
        size = client_rect.height // (2 * NUM_LEVELS - 1) + 1
        x = (client_rect.left + client_rect.right) // 2
        y = (client_rect.top + client_rect.bottom) // 2
        
        # Add center cell
        self.cells.append(self.Cell(self.palette, WHITE, x, y, size, 0))
        
        for level in range(1, NUM_LEVELS): 
            # store the level start position
            pos_x = x + (size * level)
            pos_y = y
            
            # for each side
            for side in range(NUM_LEVELS - 1):
                # set the deltas for the side
                dx = size * CFX_OFFSET[side]
                dy = size * CFY_OFFSET[side]
                
                # for each cell per side
                for i in range(level):
                    angle = self.angle_from_point(pos_x - x, pos_y - y)
                    L = 1.0 * (NUM_LEVELS - level) / NUM_LEVELS + 1.0
                    self.cells.append(self.Cell(self.palette, Color.HSL(angle, 1.0, L).rgb(), pos_x, pos_y, size, 16))
                    
                    # offset the position
                    pos_x += dx
                    pos_y += dy
                    
    def draw_hex(self, dc: DC):
        WindowUtils.draw_parent_background(self, dc)
        sel_cell = None
        
        for cell in self.cells:
            cell.draw(dc)
            if cell.color == self.color_new:
                sel_cell = cell
        
        if sel_cell:
            sel_cell.draw_selected(dc, self.focused)
            
    def draw_picker(self, dc: DC):
        client_rect = self.client_rect
        if not self.picker_bitmap:
            self.picker_bitmap = Bitmap.create(client_rect.width, client_rect.height)
        if self.picker_bitmap:
            # Prepare picker's bitmap:
            with dc.create_compatible() as memDC:
                with dc.create_compatible_bitmap(client_rect.width, client_rect.height):
                    with dc.select_ex(self.picker_bitmap):
                        step = 1 if BITS_PER_PIXEL > 8 else 4
                        for i in range(0, client_rect.height, step):
                            for j in range(0, client_rect.width, step):
                                pt = Point(j, client_rect.height - i - step)
                                color = Color.HSL(j/client_rect.width, i/client_rect.height, DEFAULT_LUMINANCE).rgb()
                                if BITS_PER_PIXEL > 8: # High/True color
                                    # Draw exact color:
                                    memDC.pixels[pt.x][pt.y] = color
                                else:
                                    # Draw ditgered rectangle
                                    brush = Brush.create(color)
                                    memDC.fill(Rect(pt.x, pt.y, step, step), brush)
            dc.draw_state(0, 0, DST_BITMAP, lData=self.picker_bitmap, 
                        width=client_rect.width, height=client_rect.height)
        
    def draw_luminance_bar(self, dc: DC):
        client_rect = self.client_rect
        client_rect.deflate(0, DEFAULT_OFFSET_OF_LUMINANCE_BAR)
        
        for y in range(client_rect.top, client_rect.bottom+1):
            col = Color.HSL(self.color_hsl.hue, self.color_hsl.saturation, self.luminance_from_point(y)).rgb()
            with Brush.create(col) as brush:
                dc.fill(Rect.create(0, y, self.luminance_bar_width, y + 1), brush)
                
    def draw_cursor(self, dc: DC, rect: Rect):
        half_size = rect.width // 2
        if self.color_type == self.ColorType.PICKER:
            color_focus = BLACK if self.focused else WHITE
            with Brush.create(color_focus) as brush:
                dc.fill(Rect.create((rect.left + half_size) - 1, rect.top, 3, 5), brush) # Top
                dc.fill(Rect.create((rect.left + half_size) - 1, rect.bottom - 5, 3, 5), brush) # Bottom
                dc.fill(Rect.create(rect.left, (rect.top + half_size) - 1, 5, 3), brush) # Left
                dc.fill(Rect.create(rect.right - 5, (rect.top + half_size) - 1, 5, 3), brush) # Right
        elif self.color_type == self.ColorType.LUMINANCE:
            points = [(rect.left, rect.top + half_size),
                      (rect.right - 1, rect.top),
                      (rect.right - 1, rect.bottom - 1)]
            with Pen.create(PS_SOLID, 1, Color.system(COLOR_BTNTEXT)) as pen:
                color_focus = Color.system(COLOR_BTNTEXT) if self.focused else Color.system(COLOR_BTNSHADOW)
                
                with Brush.create(color_focus) as brush:
                    with dc.select_ex(brush), dc.select_ex(pen):
                        dc.polygon(points)
    
    def angle_from_point(self, x: int, y: int) -> int:
        return int(math.atan2(y, x) * 180/PI)
    
    def select_cell_hexagon(self, x: int, y: int) -> bool:
        for cell in self.cells:
            if cell.hit(x, y):
                self.color_new = cell.color
                self.color_hsl = self.color_new.hsl()
                return True
        return False
    
    def set_luminance_bar_width(self, width: int):
        width = min(width, self.client_rect.width * 3 // 4)
        self.luminance_bar_width = width
        self.invalidate()
       
    def set_color_picker_palette(self, palette: Palette):
        if self.picker_bitmap:
            self.picker_bitmap.close()
        
        self.palette = palette
        self.invalidate()
        self.update()
        
    def erase_color_picker_background(self, dc: DC):
        return True
    
    @property
    def hsl(self) -> Color.HSL:
        return self.color_hsl
    
    @hsl.setter
    def hsl(self, hsl: Color.HSL):
        self.color_hsl = hsl
        self.color_new = hsl.rgb()
        self.invalidate()
        self.update()
    
    @property
    def cursor_position(self) -> tuple[int, int]:
        client_rect = self.client_rect
        
        if self.color_type == self.ColorType.LUMINANCE:
            return (client_rect.width + self.luminance_bar_width + 6, self.point_from_luminance(self.color_hsl.luminance))
        elif self.color_type == self.ColorType.PICKER:
            return (int(client_rect.width * self.color_hsl.hue), int((1 - self.color_hsl.saturation) * client_rect.height))
        else:
            ASSERT(NEVER)
        
        return (0, 0)
    
    @property
    def cursor_rect(self) -> Rect:
        if self.color_type == self.ColorType.PICKER:
            x, y = self.cursor_position
            rect = Rect.create(x, y, PICKER_CURSOR_SIZE, PICKER_CURSOR_SIZE)
        elif self.color_type == self.ColorType.LUMINANCE:
            x, y = self.cursor_position
            rect = Rect(x, y, LUMINANCE_CURSOR_SIZE, LUMINANCE_CURSOR_SIZE)
        else:
            ASSERT(NEVER)
        
        rect.offset(-rect.width / 2, -rect.height / 2)
        return rect
    
    def luminance_from_point(self, y: int) -> float:
        client_rect = self.client_rect
        client_rect.deflate(0, DEFAULT_OFFSET_OF_LUMINANCE_BAR)
        y = min(max(client_rect.top, y), client_rect.bottom)
        return (float(client_rect.bottom) - y) / client_rect.height
    
    def point_from_luminance(self, luminance: float) -> int:
        client_rect = self.client_rect
        client_rect.deflate(0, DEFAULT_OFFSET_OF_LUMINANCE_BAR)
        return client_rect.top + int((1 - self.color_hsl.luminance) * client_rect.height)