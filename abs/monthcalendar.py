from .window import *
from win.abs.core.datetime import *

class MonthCalendarHit(MCHITTESTINFO):
    @property
    def result(self) -> int:
        return self.uHit
    
    @result.setter
    def result(self, result: int):
        self.uHit = result
        
    @property
    def time(self) -> DateTime:
        return DateTime(self.st)
    
    @time.setter
    def time(self, time: DateTime | SYSTEMTIME):
        if isinstance(time, DateTime):
            time = time.systemtime
        self.st = time
        
    @property
    def offset(self) -> int:
        return self.iOffset
    
    @offset.setter
    def offset(self, offset: int):
        self.iOffset = offset
        
    @property
    def row(self):
        return self.iRow
        
    @row.setter
    def row(self, row: int):
        self.iRow = row
        
    @property
    def column(self) -> int:
        return self.iCol
    
    @column.setter
    def column(self, column: int) -> int:
        self.iCol = column
        
    @property
    def rect(self) -> Rect:
        return i_cast_structure(self.rc, Rect)
    
    @rect.setter
    def rect(self, rect: RECT):
        self.rc = rect

class MonthCalendarGridInfo(MCGRIDINFO):
    @property
    def selected(self) -> bool:
        return self.bSelected == TRUE
    
    @selected.setter
    def selected(self, selected: bool):
        self.bSelected = selected
        
    @property
    def start_date(self) -> DateTime:
        return DateTime(self.stStart)
    
    @start_date.setter
    def start_date(self, start_date: DateTime | SYSTEMTIME):
        if isinstance(start_date, DateTime):
            start_date = start_date.systemtime
        self.stStart = start_date
        
    @property
    def end_date(self) -> DateTime:
        return DateTime(self.stEnd)
    
    @end_date.setter
    def end_date(self, end_date: DateTime | SYSTEMTIME):
        if isinstance(end_date, DateTime):
            end_date = end_date.systemtime
        self.stEnd = end_date
        
    @property
    def rect(self) -> Rect:
        return i_cast_structure(self.rc, Rect)
    
    @rect.setter
    def rect(self, rect: RECT):
        self.rc = rect
        
    @property
    def name(self) -> str:
        return self.pszName.value
    
    @name.setter
    def name(self, name: str):
        self.pszName.value = name

class MonthCalendar(Control):
    _width: int
    _height: int
    
    def __init__(self, width: int, height: int, parent: int | HWND, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self._width = width
        self._height = height
        self.class_name = MONTHCAL_CLASSW
    
    def create(self, x: int, y: int, relative: int | HANDLE = NULL):
        """
        Create month calendar control.
        """
        super().create(self._width, self._height, x, y, None, relative)
        
    @property
    def calendar_id(self) -> int:
        return self.send(MCM_GETCALID)
    
    @calendar_id.setter
    def calendar_id(self, calendar_id: int):
        self.send(MCM_SETCALID, calendar_id)
        
    def color(self, index: int) -> Color.BGR | None:
        color = self.send(MCM_GETCOLOR, index)
        if color == -1:
            return None
        return Color.BGR(color)
    
    def set_color(self, index: int, color: Color.BGR) -> Color.BGR:
        color = self.send(MCM_SETCOLOR, index, int(color))
        if color == -1:
            raise RuntimeError('Error ocurred while setting month calendar color.')
        return Color.BGR(color)
    
    @property
    def current_view(self) -> int:
        return self.send(MCM_GETCURRENTVIEW)
    
    @current_view.setter
    def current_view(self, current_view: int):
        self.send(MCM_SETCURRENTVIEW, 0, current_view)
    
    @property
    def selection(self) -> DateTime:
        time = SYSTEMTIME()
        self.send(MCM_GETCURSEL, 0, time.ref())
        return DateTime(time)
    
    @selection.setter
    def selection(self, selection: DateTime | SYSTEMTIME):
        if isinstance(selection, DateTime):
            selection = selection.systemtime
        self.send(MCM_SETCURSEL, 0, selection.ref())
    
    @property
    def first_day_of_week(self) -> int:
        return self.send(MCM_GETFIRSTDAYOFWEEK)
    
    @first_day_of_week.setter
    def first_day_of_week(self, first_day_of_week: int):
        self.send(MCM_SETFIRSTDAYOFWEEK, 0, first_day_of_week)
    
    @property
    def max_selection_count(self) -> int:
        return self.send(MCM_GETMAXSELCOUNT)
    
    @max_selection_count.setter
    def max_selection_count(self, max_selection_count: int):
        self.send(MCM_SETMAXSELCOUNT, max_selection_count)
    
    @property
    def max_today_width(self) -> int:
        return self.send(MCM_GETMAXTODAYWIDTH)
    
    @property
    def min_required_rect(self) -> Rect:
        rect = Rect()
        self.send(MCM_GETMINREQRECT, 0, rect.ref())
        return rect
    
    @property
    def month_delta(self) -> int:
        return self.send(MCM_GETMONTHDELTA)
    
    @month_delta.setter
    def month_delta(self, month_delta: int):
        self.send(MCM_SETMONTHDELTA, month_delta)
    
    @property
    def visible_month_range(self) -> tuple[DateTime, DateTime]:
        times = (SYSTEMTIME*2)()
        self.send(MCM_GETMONTHRANGE, GMR_VISIBLE, times)
        return DateTime(times[0]), DateTime(times[1])
    
    @property
    def daystate_month_range(self) -> tuple[DateTime, DateTime]:
        times = (SYSTEMTIME*2)()
        self.send(MCM_GETMONTHRANGE, GMR_DAYSTATE, times)
        return DateTime(times[0]), DateTime(times[1])
    
    @property
    def range(self) -> tuple[DateTime | None, DateTime | None]:
        times = (SYSTEMTIME*2)()
        flags = self.send(MCM_GETRANGE, 0, times)
        if flags & GDTR_MIN and flags & GDTR_MAX:
            return DateTime(times[0]), DateTime(times[1])
        if flags & GDTR_MIN:
            return DateTime(times[0]), None
        if flags & GDTR_MAX:
            return None, DateTime(times[1])
        return None, None
    
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
        self.send(MCM_SETRANGE, flags, array)
    
    @property
    def selected_range(self) -> tuple[DateTime, DateTime]:
        times = (SYSTEMTIME*2)()
        self.send(MCM_GETSELRANGE, 0, times)
        return DateTime(times[0]), DateTime(times[1])
    
    @selected_range.setter
    def selected_range(self, selected_range: Iterable[DateTime | SYSTEMTIME]):
        time0, time1 = selected_range
        if isinstance(time0, DateTime):
            time0 = time0.systemtime
        if isinstance(time1, DateTime):
            time1 = time1.systemtime
        array = (SYSTEMTIME*2)(time0, time1)
        self.send(MCM_SETSELRANGE, 0, array)
    
    @property
    def today(self) -> DateTime:
        time = SYSTEMTIME()
        self.send(MCM_GETTODAY, 0, time.ref())
        return DateTime(time)
    
    @today.setter
    def today(self, today: DateTime | SYSTEMTIME):
        if isinstance(today, DateTime):
            today = today.systemtime
        self.send(MCM_SETTODAY, 0, today.ref())
    
    def hit(self, x: int, y: int) -> MonthCalendarHit:
        mch = MonthCalendarHit()
        mch.cbSize = mch.size()
        mch.pt = POINT(x, y)
        self.send(MCM_HITTEST, 0, mch.ref())
        return mch
    
    def information(self, part: int, flags: int = MCGIF_DATE | MCGIF_RECT | MCGIF_NAME,
                    calendar: int = 0, row: int = 0, column: int = 0) -> MonthCalendarGridInfo:
        mcgi = MonthCalendarGridInfo()
        mcgi.cbSize = mcgi.size()
        mcgi.dwPart = part
        mcgi.dwFlags = flags
        mcgi.iCalendar = calendar
        mcgi.iRow = row
        mcgi.iCol = column
        if not self.send(MCM_GETCALENDARGRIDINFO, 0, mcgi.ref()):
            raise ValueError('Invalid arguments.')
        return mcgi
    
    @property
    def calendar_count(self) -> int:
        return self.send(MCM_GETCALENDARCOUNT)
    
    @property
    def border_size(self) -> int:
        return self.send(MCM_GETCALENDARBORDER)
    
    def day_state(self, states: Iterable[int] | Iterable[Iterable[int]]):
        array = (MONTHDAYSTATE*len(states))()
        for i, x in enumerate(states):
            if not isinstance(x, int):
                state = 0
                for enabled in x:
                    state |= bool(enabled)
                    state <<= 1
                x = state
            array[i] = x
        if not self.send(MCM_SETDAYSTATE, len(states), array):
            raise RuntimeError('Error ocurred while setting day states.')
        
    def size_rect_min(self, rect: RECT) -> Rect:
        rect = rect.copy()
        self.send(MCM_SIZERECTTOMIN, 0, rect.ref())
        return rect