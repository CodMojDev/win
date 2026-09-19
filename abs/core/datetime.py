from .handle import *
from win.timezoneapi import *
from win.datetimeapi import *
from win.winnls import *

class DateTime:
    """
    Date/Time instance representing FILETIME and SYSTEMTIME at once.
    """
    
    _st: SYSTEMTIME
    _ft: FILETIME
    lcid: int
    _buffer: IWideCharArray
    _sync: bool
    _tz: TIME_ZONE_INFORMATION
    _utc: SYSTEMTIME
    
    def __init__(self, st: SYSTEMTIME = None, ft: FILETIME = None,
                 lcid: int = LOCALE_USER_DEFAULT):
        self._tz = TIME_ZONE_INFORMATION()
        GetTimeZoneInformation(self._tz.ref())
        self._utc = SYSTEMTIME()
        if st is None and ft is not None:
            st = SYSTEMTIME()
            FileTimeToSystemTime(ft.ref(), st.ref())
            SystemTimeToTzSpecificLocalTime(self._tz.ref(), st.ref(), st.ref())
        elif st is not None and ft is None:
            ft = FILETIME()
            TzSpecificLocalTimeToSystemTime(self._tz.ref(), st.ref(), self._utc.ref())
            SystemTimeToFileTime(self._utc.ref(), ft.ref())
        else:
            st = SYSTEMTIME()
            ft = FILETIME()
        self._st = st
        self._ft = ft
        self.lcid = lcid
        self._buffer = create_unicode_buffer(256)
        self._sync = True
    
    def to_unix(self) -> int:
        """
        Convert Date/Time to UNIX timestamp format.
        """
        return ConvertUtil.filetime_to_unix(self._ft)
    
    def to_datetime(self) -> datetime.datetime:
        """
        Convert Date/Time to Python Datetime format.
        """
        return ConvertUtil.filetime_to_datetime(self._ft)
    
    def to_int(self) -> int:
        """
        Convert Date/Time FILETIME to 64-bit Integer.
        """
        return ConvertUtil.filetime_to_int(self._ft)
    
    @classmethod
    def current(cls, lcid: int = LOCALE_USER_DEFAULT) -> Self:
        """
        Retrieve the current Date/Time.
        """
        dt = cls()
        dt.lcid = lcid
        if not is_null(GetSystemTimePreciseAsFileTime):
            GetSystemTimePreciseAsFileTime(dt._ft.ref())
        else:
            GetSystemTimeAsFileTime(dt._ft.ref())
        dt._synchronize(True)
        return dt
    
    @classmethod
    def from_unix(cls, ts: int, lcid: int = LOCALE_USER_DEFAULT) -> Self:
        """
        Construct the Date/Time from UNIX timestamp format.
        """
        dt = cls()
        dt.lcid = lcid
        ft = (ts * 10000000) + 116444736000000000
        UINT64.from_address(dt._ft.addressof()).value = ft
        dt._synchronize(True)
        return dt
    
    @classmethod
    def from_datetime(cls, dt: datetime.datetime, lcid: int = LOCALE_USER_DEFAULT) -> Self:
        """
        Construct the Date/Time from Python Datetime format.
        """
        dt2 = cls()
        dt2.lcid = lcid
        dt2._st.wYear = dt.year
        dt2._st.wMonth = dt.month
        dt2._st.wDayOfWeek = (dt.weekday() + 1) % 7
        dt2._st.wDay = dt.day
        dt2._st.wHour = dt.hour
        dt2._st.wMinute = dt.minute
        dt2._st.wSecond = dt.second
        dt2._st.wMilliseconds = dt.microsecond // 1000
        dt2._synchronize(False)
        return dt2
    
    def _synchronize(self, ft_changed: bool):
        if self._sync:
            if ft_changed:
                FileTimeToSystemTime(self._ft.ref(), self._utc.ref())
                SystemTimeToTzSpecificLocalTime(self._tz.ref(), self._utc.ref(), self._st.ref())
            else:
                TzSpecificLocalTimeToSystemTime(self._tz.ref(), self._st.ref(), self._utc.ref())
                SystemTimeToFileTime(self._utc.ref(), self._ft.ref())
    
    def _synchronize_all(self):
        self._synchronize(False)
        self._synchronize(True)
    
    @property
    def year(self) -> int:
        return self._st.wYear
    
    @year.setter
    def year(self, year: int):
        self._st.wYear = year
        self._synchronize_all()
    
    @property
    def month(self) -> int:
        return self._st.wMonth
    
    @month.setter
    def month(self, month: int):
        sign = 1 if month > 0 else -1
        month = abs(month)
        prev_sync = self._sync
        self._sync = False
        while month > 12:
            month -= sign*12
            self.year += sign
        self._sync = prev_sync
        self._st.wMonth = month
        self._synchronize_all()
    
    def _is_leap_year(self) -> bool:
        year = self._st.wYear
        leap = (year % 4) == 0
        if leap:
            if (year % 400) != 0:
                if (year % 100) == 0:
                    leap = False
        return leap
    
    def _month_to_days(self, month: int) -> int:
        if month == 2:
            return 28 + self._is_leap_year()
        even = (month & 1) == 0
        if month < 8:
            return 31 if not even else 30
        else:
            return 31 if even else 30
    
    @property
    def day(self) -> int:
        return self._st.wDay
    
    @day.setter
    def day(self, day: int):
        sign = 1 if day > 0 else -1
        day = abs(day)
        days = self._month_to_days(self.month)
        prev_sync = self._sync
        self._sync = False
        while day > days:
            day -= sign*days
            self.month += sign
            days = self._month_to_days(self.month)
        self._sync = prev_sync
        self._st.wDay = day
        self._synchronize_all()
    
    @property
    def day_of_week(self) -> int:
        return (self._st.wDayOfWeek + 6) % 7
    
    @property
    def hour(self) -> int:
        return self._st.wHour
    
    @hour.setter
    def hour(self, hour: int):
        sign = 1 if hour > 0 else -1
        hour = abs(hour)
        prev_sync = self._sync
        self._sync = False
        while hour >= 24:
            hour -= sign*24
            self.day += sign
        self._sync = prev_sync
        self._st.wHour = hour
        self._synchronize_all()
    
    @property
    def minute(self) -> int:
        return self._st.wMinute
    
    @minute.setter
    def minute(self, minute: int):
        sign = 1 if minute > 0 else -1
        minute = abs(minute)
        prev_sync = self._sync
        self._sync = False
        while minute >= 60:
            minute -= sign*60
            self.hour += sign
        self._sync = prev_sync
        self._st.wMinute = minute
        self._synchronize_all()
    
    @property
    def second(self) -> int:
        return self._st.wSecond
    
    @second.setter
    def second(self, second: int):
        sign = 1 if second > 0 else -1
        second = abs(second)
        prev_sync = self._sync
        self._sync = False
        while second > 60:
            second -= sign*60
            self.minute += sign
        self._sync = prev_sync
        self._st.wSecond = second
        self._synchronize_all()
    
    @property
    def millisecond(self) -> int:
        return self._st.wMilliseconds
    
    @millisecond.setter
    def millisecond(self, millisecond: int):
        sign = 1 if millisecond > 0 else -1
        millisecond = abs(millisecond)
        prev_sync = self._sync
        self._sync = False
        while millisecond > 1000:
            millisecond -= sign*1000
            self.second += sign
        self._sync = prev_sync
        self._st.wMilliseconds = millisecond
        self._synchronize_all()
        
    @property
    def microsecond(self) -> int:
        return self._st.wMilliseconds * 1000
    
    @microsecond.setter
    def microsecond(self, microsecond: int):
        sign = 1 if microsecond > 0 else -1
        microsecond = abs(microsecond)
        prev_sync = self._sync
        self._sync = False
        while microsecond > 1000000:
            microsecond -= sign*1000000
            self.millisecond += sign
        self._sync = prev_sync
        self._st.wMilliseconds = microsecond // 1000
        self._synchronize_all()
        
    @property
    def filetime(self) -> FILETIME:
        return self._ft
    
    @filetime.setter
    def filetime(self, filetime: FILETIME):
        self._ft = filetime
        self._synchronize(True)
    
    @property
    def systemtime(self) -> SYSTEMTIME:
        return self._st
    
    @systemtime.setter
    def systemtime(self, systemtime: SYSTEMTIME):
        self._st = systemtime
        self._synchronize(False)
    
    @property
    def utc(self) -> SYSTEMTIME:
        return self._utc
    
    @utc.setter
    def utc(self, utc: SYSTEMTIME):
        self._utc = utc
        SystemTimeToTzSpecificLocalTime(self._tz.ref(), utc.ref(), self._st.ref())
        self._synchronize(False)
        
    @property
    def timezone(self) -> TIME_ZONE_INFORMATION:
        return self._tz
    
    @timezone.setter
    def timezone(self, timezone: TIME_ZONE_INFORMATION):
        tz = self._tz
        self._tz = timezone
        TzSpecificLocalTimeToSystemTime(tz.ref(), self._st.ref(), self._utc.ref())
        SystemTimeToTzSpecificLocalTime(timezone.ref(), self._utc.ref(), self._st.ref())
        self._synchronize(False)
    
    def __eq__(self, other: TUnion['DateTime', datetime.datetime, SYSTEMTIME, FILETIME]) -> bool:
        if isinstance(other, DateTime):
            return self._ft == other._ft
        elif isinstance(other, datetime.datetime):
            return self.to_unix() == round(other.timestamp())
        elif isinstance(other, FILETIME):
            return self._ft == other
        elif isinstance(other, SYSTEMTIME):
            return self._st == other
        else:
            return NotImplemented
        
    def __hash__(self) -> int:
        return hash(self._ft)
    
    def format_date(self, format: str, flags: int = 0) -> str:
        """
        Format the Date to string using flags and string format.
        """
        GetDateFormatW(self.lcid, flags, self._st.ref(), format, self._buffer, 256)
        return self._buffer.value
        
    def format_time(self, format: str, flags: int = 0):
        """
        Format the Time to string using flags and string format.
        """
        GetTimeFormatW(self.lcid, flags, self._st.ref(), format, self._buffer, 256)
        return self._buffer.value
    
    def __str__(self) -> str:
        return f'{self.format_date("dd.MM.yyyy")} {self.format_time("HH:mm:ss")}'
    
    def __repr__(self) -> str:
        return f'<DateTime {self}>'
    
    def copy(self) -> Self:
        """
        Copy the Date/Time.
        """
        dt = self.__class__()
        dt._st = self._st.copy()
        dt._ft = self._ft.copy()
        dt._utc = self._utc.copy()
        dt._tz = self._tz.copy()
        dt.lcid = self.lcid
        return dt
    
    def update(self, dt: TUnion['DateTime', None] = None):
        """
        Update the Date/Time from another instance or from system time.
        """
        if dt is None:
            if not is_null(GetSystemTimePreciseAsFileTime):
                GetSystemTimePreciseAsFileTime(self._ft.ref())
            else:
                GetSystemTimeAsFileTime(self._ft.ref())
            self._synchronize(True)
        else:
            memcpy(self._st.ref(), dt._st.ref(), SYSTEMTIME.size())
            memcpy(self._ft.ref(), dt._ft.ref(), FILETIME.size())