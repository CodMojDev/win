from .window import *

class ProgressBar(Control):
    """
    Win32 Progress bar common control.
    """
    
    class Progress:
        progress_bar: 'ProgressBar'
        
        def __init__(self, progress_bar: 'ProgressBar'):
            self.progress_bar = progress_bar
            
        def set(self, position: int):
            """
            Set current progress bar progress.
            """
            
            self.progress_bar.send(PBM_SETPOS, position)
        
        def get(self):
            """
            Get current progress bar progress.
            """
            
            return self.progress_bar.send(PBM_GETPOS)
        
        def __iadd__(self, delta: int):
            self.progress_bar.send(PBM_DELTAPOS, delta)
            return self
            
        def __isub__(self, delta: int):
            self.progress_bar.send(PBM_DELTAPOS, -delta)
            return self
        
        def step(self):
            """
            Step the progress bar progress.
            """
            
            self.progress_bar.send(PBM_STEPIT)
    
    def __init__(self, width: int, height: int, 
                 parent: int | HWND, identifier: int | HANDLE):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.progress = ProgressBar.Progress(self)
        self.class_name = PROGRESS_CLASSW
        
    def create(self, x: int, y: int, relative: int | HWND=NULL):
        """
        Create progress bar control.
        """
        
        super().create(self._width, self._height, x, y, relative=relative)
        
    def marquee(self, marquee: bool = True, update: int = 0):
        """
        Set current progress bar as marquee (or not).
        """
        
        self.send(PBM_SETMARQUEE, marquee, update)
        
    @property
    def state(self) -> int:
        return self.send(PBM_GETSTATE)
    
    @state.setter
    def state(self, state: int):
        self.send(PBM_SETSTATE, state)
        
    @property
    def range(self) -> tuple[int, int]:
        progressbar_range = PBRANGE()
        self.send(PBM_GETRANGE, FALSE, progressbar_range.ref())
        return (progressbar_range.iLow, progressbar_range.iHigh)
    
    @range.setter
    def range(self, range: tuple[int, int]):
        if not self.send(PBM_SETRANGE, lParam=MAKELPARAM(range[0], range[1])):
            raise ValueError(f'Invalid progress bar range: {range}')
        
    @property
    def step(self) -> int:
        return self.send(PBM_GETSTEP)
    
    @step.setter
    def step(self, step: int):
        self.send(PBM_SETSTEP, step)
        
    @property
    def bk_color(self) -> int:
        return self.send(PBM_GETBKCOLOR)
    
    @bk_color.setter
    def bk_color(self, bk_color: int):
        self.send(PBM_SETBKCOLOR, lParam=bk_color)
        
    @property
    def color(self) -> int:
        return self.send(PBM_GETBARCOLOR)
    
    @color.setter
    def color(self, color: int):
        self.send(PBM_SETBARCOLOR, lParam=color)