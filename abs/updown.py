from .window import *

class UpDown(Control):
    on_number_changed: MultiEvent
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = UPDOWN_CLASSW
        self.on_number_changed = MultiEvent()
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, NULL, relative)
    
    @property
    def buddy(self) -> Window | None:
        return Window.foreign(self.send(UDM_GETBUDDY))
    
    @buddy.setter
    def buddy(self, buddy: int | HANDLE):
        self.send(UDM_SETBUDDY, buddy)
        
    @property
    def range(self) -> tuple[int, int]:
        lower = UINT32()
        upper = UINT32()
        self.send(UDM_GETRANGE32, byref(lower), byref(upper))
        return lower, upper
    
    @range.setter
    def range(self, range: tuple[int, int]):
        self.send(UDM_SETRANGE32, range[0], range[1])
        
    @property
    def number(self) -> int:
        bErrorOcurred = BOOL()
        lNumber = self.send(UDM_GETPOS32, 0, byref(bErrorOcurred))
        if bErrorOcurred.value: raise WinException()
        return lNumber
    
    @number.setter
    def number(self, number: int):
        self.send(UDM_SETPOS32, 0, number)
        
    @property
    def base(self) -> Literal[10, 16]:
        return self.send(UDM_GETBASE)
    
    @base.setter
    def base(self, base: int):
        if not self.send(UDM_SETBASE, base):
            raise ValueError(base)
        
    @property
    def accels(self) -> list[UDACCEL]:
        n = self.send(UDM_GETACCEL)
        accels = (UDACCEL*n)()
        self.send(UDM_GETACCEL, n, accels)
        return list(accels)
    
    @accels.setter
    def accels(self, accels: Iterable[UDACCEL]):
        accels = sorted(accels, key=lambda accel: accel.nSec)
        pAccels = (UDACCEL*len(accels))(*accels)
        self.send(UDM_SETACCEL, len(accels), pAccels)
        
    def parent_window_on_notify(self, nm: NMHDR):
        if nm.hwndFrom == self.value:
            code = INT(nm.code).value
            if code == UDN_DELTAPOS:
                nmupdown = i_cast_structure(nm, NMUPDOWN)
                self.on_number_changed.execute(nmupdown.iPos, nmupdown.iDelta)
            else:
                super().parent_window_on_notify(nm)