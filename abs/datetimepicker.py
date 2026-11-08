from .window import *
from .updown import *
from .edit import *
from .monthcalendar import *
from win.abs.core.datetime import *

class DateTimePickerInfo(DATETIMEPICKERINFO):
    @property
    def checkbox_rect(self) -> Rect:
        return i_cast_structure(self.rcCheck, Rect)
    
    @checkbox_rect.setter
    def checkbox_rect(self, checkbox_rect: RECT):
        self.rcCheck = checkbox_rect
    
    @property
    def checkbox_state(self) -> int:
        return self.stateCheck
    
    @checkbox_state.setter
    def checkbox_state(self, checkbox_state: int):
        self.stateCheck = checkbox_state
    
    @property
    def button_rect(self) -> Rect:
        return i_cast_structure(self.rcButton, Rect)
    
    @button_rect.setter
    def button_rect(self, button_rect: RECT):
        self.rcButton = button_rect
    
    @property
    def button_state(self) -> int:
        return self.stateButton
    
    @button_state.setter
    def button_state(self, button_state: int):
        self.stateButton = button_state
    
    @property
    def edit_window(self) -> Edit:
        return Edit.foreign(self.hwndEdit)
    
    @edit_window.setter
    def edit_window(self, edit_window: int | HWND):
        self.hwndEdit = edit_window
    
    @property
    def updown_window(self) -> UpDown:
        return UpDown.foreign(self.hwndUD)
    
    @updown_window.setter
    def updown_window(self, updown_window: int | HWND):
        self.hwndUD = updown_window
    
    @property
    def dropdown_window(self) -> Window:
        return Window.foreign(self.hwndDropDown)
    
    @dropdown_window.setter
    def dropdown_window(self, dropdown_window: int | HWND):
        self.hwndDropDown = dropdown_window

class DateTimePicker(Control):
    """
    Date/Time Picker Control
    """
    
    class MonthCalendarStyles(BitGroup):
        dtp: 'DateTimePicker'
        
        def __init__(self, dtp: 'DateTimePicker'):
            self.dtp = dtp
        
        @property
        def value(self) -> int:
            return self.dtp.send(DTM_GETMCSTYLE)
        
        @value.setter
        def value(self, value: int):
            self.dtp.send(DTM_SETMCSTYLE, 0, value)
    
    _width: int
    _height: int
    _format: str | None
    month_calendar_styles: MonthCalendarStyles
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = DATETIMEPICK_CLASSW
        
    def headless_init(self):
        super().headless_init()
        self._format = None
        self.month_calendar_styles = self.MonthCalendarStyles(self)
    
    def create(self, x: int, y: int, relative: int | HANDLE = NULL):
        """
        Create Date/Time picker control.
        """
        super().create(self._width, self._height, x, y, None, relative)
        
    def close_calendar(self):
        self.send(DTM_CLOSEMONTHCAL)
        
    def info(self) -> DateTimePickerInfo:
        dtpi = DateTimePickerInfo()
        dtpi.cbSize = dtpi.size()
        self.send(DTM_GETDATETIMEPICKERINFO, 0, dtpi.ref())
        return dtpi
    
    @property
    def ideal_size(self) -> tuple[int, int]:
        size = SIZE()
        self.send(DTM_GETIDEALSIZE, 0, size.ref())
        return size.cx, size.cy
    
    def month_calendar_color(self, color: int) -> Color.BGR | None:
        color = self.send(DTM_GETMCCOLOR, color)
        if color == -1:
            return None
        return Color.BGR(color)
    
    @property
    def month_calendar_font(self) -> Font:
        return Font.foreign_owner(self.send(DTM_GETMCFONT))
    
    @month_calendar_font.setter
    def month_calendar_font(self, month_calendar_font: int | HANDLE):
        self.send(DTM_SETMCFONT, month_calendar_font, TRUE)
    
    @property
    def range(self) -> tuple[DateTime, DateTime]:
        times = (SYSTEMTIME*2)()
        self.send(DTM_GETRANGE, 0, times)
        return DateTime(times[0]), DateTime(times[1])
    
    @range.setter
    def range(self, range: Iterable[DateTime | SYSTEMTIME | None]):
        time0, time1 = range
        flags = 0
        if time0 is not None:
            flags |= GDTR_MIN
        if time1 is not None:
            flags |= GDTR_MAX
        if flags == 0:
            raise ValueError('One of ranges must be specified.')
        if isinstance(time0, DateTime):
            time0 = time0.systemtime
        if isinstance(time1, DateTime):
            time1 = time1.systemtime
        array = (SYSTEMTIME*2)()
        if time0 is not None:
            array[0] = time0
        if time1 is not None:
            array[1] = time1
        self.send(DTM_SETRANGE, flags, array)
    
    @property
    def time(self) -> DateTime:
        time = SYSTEMTIME()
        self.send(DTM_GETSYSTEMTIME, 0, time.ref())
        return DateTime(time)
    
    @time.setter
    def time(self, time: DateTime | SYSTEMTIME):
        if isinstance(time, DateTime):
            time = time.systemtime
        self.send(DTM_SETSYSTEMTIME, GDT_VALID, time.ref())
        
    def clear(self):
        self.send(DTM_SETSYSTEMTIME, GDT_NONE)
    
    @property
    def format(self) -> str | None:
        return self._format
    
    @format.setter
    def format(self, format: str | None):
        self._format = format
        self.send(DTM_SETFORMAT, 0, format)
        
    @property
    def month_calendar(self) -> MonthCalendar:
        return MonthCalendar.foreign(self.send(DTM_GETMONTHCAL))