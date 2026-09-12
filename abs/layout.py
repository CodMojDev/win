from .window import *

class Anchor:
    Normal = 0
    
    # Horizontal anchors
    Left = 1
    Right = 2
    
    # Vertical anchors
    Top = 1
    Bottom = 2

class LayoutManagerEx:
    windows: list[tuple[Window, Callable[[Window, int, int], tuple[int, int]]]]
    
    def __init__(self):
        self.windows = []
        
    def update(self, width: int, height: int):
        for window, converter in self.windows:
            x, y = window.position
            window.position = converter(window, x, y)
            
class LayoutManager(LayoutManagerEx):
    def add(self, 
            window: Window, 
            horizontal_anchor: int, 
            vertical_anchor: int,
            horizontal_offset: int,
            vertical_offset: int):
        if horizontal_anchor == Anchor.Right:
            horizontal_offset = -horizontal_offset
        if vertical_anchor == Anchor.Bottom:
            vertical_offset = -vertical_offset
        
        def converter(wnd: Window, x: int, y: int) -> tuple[int, int]:
            nonlocal horizontal_offset, vertical_offset
            rc = wnd.parent.client_rect
                
            if horizontal_anchor == Anchor.Right:
                x = rc.right
                x -= wnd.width
            else:
                x = rc.left
            
            if vertical_anchor == Anchor.Bottom:
                y = rc.bottom
                y -= wnd.height
            else:
                y = rc.top
            
            x += horizontal_offset
            y += vertical_offset
            
            return x, y
        self.windows.append((window, converter))