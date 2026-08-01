from .window import *

class Slider(Control):
    class TickMark:
        def __init__(self, slider: 'Slider', index: int):
            self.slider = slider
            self.index = index
            
        def logical(self) -> int:
            return self.slider.send(TBM_GETTIC, self.index)
        
        def physical(self) -> int:
            return self.slider.send(TBM_GETTICPOS, self.index)
    
    class TickMarks:
        class Iterator:
            def __init__(self, slider: 'Slider'):
                self.internal_range = range(0, slider.send(TBM_GETNUMTICS))
                self.slider = slider
            
            def __iter__(self):
                return self
            
            def __next__(self) -> 'Slider.TickMark':
                return Slider.TickMark(self.slider, next(self.internal_range))
            
        def __init__(self, slider: 'Slider'):
            self.slider = slider
            
        def __getitem__(self, index: int) -> 'Slider.TickMark':
            return Slider.TickMark(self.slider, index)
        
        def count(self) -> int:
            return self.slider.send(TBM_GETNUMTICS)
        
        def set(self, logical_pos: int):
            self.slider.send(TBM_SETTIC, 0, logical_pos)
        
        @property
        def frequence(self) -> int:
            i, x = self.slider.range
            total = x - i
            return total // self.count()
        
        @frequence.setter
        def frequence(self, frequence: int):
            self.send(TBM_SETTICFREQ, frequence)
            
        def __iter__(self) -> 'Slider.TickMarks.Iterator':
            return Slider.TickMarks.Iterator(self.slider)
        
        def clear(self):
            self.slider.send(TBM_CLEARTICS, TRUE)
    
    class Selection:
        def __init__(self, slider: 'Slider'):
            self.slider = slider
            
        @property
        def range(self) -> tuple[int, int]:
            i = self.send(TBM_GETSELSTART)
            x = self.send(TBM_GETSELEND)
            return i, x
        
        @range.setter
        def range(self, range: tuple[int, int]):
            self.send(TBM_SETSEL, TRUE, MAKELPARAM(range[0], range[1]))
            
        def clear(self):
            self.send(TBM_CLEARSEL, TRUE)
    
    class Progress:
        def __init__(self, slider: 'Slider'):
            self.slider = slider
        
        @property
        def range(self) -> tuple[int, int]:
            i = self.slider.send(TBM_GETRANGEMIN)
            x = self.slider.send(TBM_GETRANGEMAX)
            return i, x
        
        @range.setter
        def range(self, range: tuple[int, int]) -> int:
            self.slider.send(TBM_SETRANGE, TRUE, MAKELPARAM(range[0], range[1]))
            
        def set(self, index: int):
            self.slider.send(TBM_SETPOS, TRUE, index)
            
        def get(self) -> int:
            return self.slider.send(TBM_GETPOS)
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = TRACKBAR_CLASSW
        self.selection = Slider.Selection(self)
        self.tick_marks = Slider.TickMarks(self)
        self.progress = Slider.Progress(self)
        
    def create(self, x: int = 0, y: int = 0, window_name: str='Slider Control', relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, window_name, relative=relative)
        
    @property
    def page_size(self) -> int:
        return self.send(TBM_GETPAGESIZE)
    
    @page_size.setter
    def page_size(self, page_size: int):
        self.send(TBM_SETPAGESIZE, 0, page_size)
        
    @property
    def line_size(self) -> int:
        return self.send(TBM_GETLINESIZE)
    
    @line_size.setter
    def line_size(self, line_size: int):
        self.send(TBM_SETLINESIZE, 0, line_size)
        
    @property
    def channel_rect(self) -> Rect:
        rc = Rect()
        self.send(TBM_GETCHANNELRECT, 0, rc.ref())
        return rc
        
    @property
    def thumb_rect(self) -> Rect:
        rc = Rect()
        self.send(TBM_GETTHUMBRECT, 0, rc.ref())
        return rc
    
    @property
    def thumb_length(self) -> int:
        return self.send(TBM_GETTHUMBLENGTH)
    
    @thumb_length.setter
    def thumb_length(self, thumb_length: int):
        self.send(TBM_SETTHUMBLENGTH, thumb_length)
    
    @property
    def left_buddy(self) -> Window:
        return Window.foreign(self.send(TBM_GETBUDDY, TRUE))
    
    @left_buddy.setter
    def left_buddy(self, left_buddy: int | HWND):
        self.send(TBM_SETBUDDY, TRUE, left_buddy)
    
    @property
    def right_buddy(self) -> Window:
        return Window.foreign(self.send(TBM_GETBUDDY, FALSE))
    
    @right_buddy.setter
    def right_buddy(self, right_buddy: int | HWND):
        self.send(TBM_SETBUDDY, FALSE, right_buddy)
    
    @property
    def upper_buddy(self) -> Window:
        return self.left_buddy
    
    @upper_buddy.setter
    def upper_buddy(self, upper_buddy: int | HWND):
        self.left_buddy = upper_buddy
    
    @property
    def lower_buddy(self) -> Window:
        return self.right_buddy
    
    @lower_buddy.setter
    def lower_buddy(self, lower_buddy: int | HWND):
        self.right_buddy = lower_buddy