from win.defbase import *

import typing as t
import types
import time
import json

class Magistral(IProfileEntry):
    call_times: dict[str, list[float]] = {}
    call_stats: dict[str, int] = {}
    
    @classmethod
    def on(cls, enable_profile: bool = True):
        if enable_profile:
            profile_enable()
        profile_add(cls)
        
    @classmethod
    def off(cls, disable_profile: bool = True):
        profile_remove(cls)
        if disable_profile:
            profile_disable()
        
    @classmethod
    def on_event(cls, frame: types.FrameType, event: str, arg: t.Any): 
        if event == 'call':
            name = frame.f_code.co_qualname
            cls.call_stats[name] = cls.call_stats.get(name, 0) + 1
            if name not in cls.call_times:
                cls.call_times[name] = times = []
            else:
                times = cls.call_times[name]
            times.append(time.perf_counter())
        elif event == 'return':
            name = frame.f_code.co_qualname
            cls.call_stats[name] = cls.call_stats.get(name, 0) + 1
            if name not in cls.call_times:
                cls.call_times[name] = times = []
            else:
                times = cls.call_times[name]
            if times:
                times[-1] = time.perf_counter() - times[-1]
            
    @classmethod
    def save(self, stats_filename: str, times_filename: str):
        with open(stats_filename, 'w', encoding='utf-8') as stats_file:
            json.dump(self.call_stats, stats_file)
        with open(times_filename, 'w', encoding='utf-8') as times_file:
            json.dump(self.call_times, times_file)