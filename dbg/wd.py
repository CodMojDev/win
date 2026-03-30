#
# Win Debugger
#

from ..defbase import get_caller_frame, get_py_frame
from .dbgapi import IsDebuggerPresent, DebugBreak
from ..wet.trace import WET_PROVIDER, dbg_trace
from typing import TYPE_CHECKING
from .. import cpreproc

import traceback
import types
import sys

class _WD_STATE:
    __slots__ = ['_WDProvider', '_prev_breakpointhook', '_dbg_depth',
                 '_prev_trace', '_trace_enabled', '_step_count',
                 '_dirty_frames']
    
    def __init__(self):
        self._WDProvider = WET_PROVIDER('WD')
        self._prev_breakpointhook = sys.breakpointhook
        self._prev_trace = sys.gettrace()
        self._trace_enabled = False
        self._step_count = False
        self._dirty_frames = []
        self._dbg_depth = 0
        
        if cpreproc.ifndef('WD_DISABLED'):
            sys.breakpointhook = WD_Breakpoint

if TYPE_CHECKING:
    _WD_PrivFrame: types.FrameType = None
    _WD_PrivState: _WD_STATE = None
    _WD_TBModule_: traceback = None
    _WD_StkLevel_: int = None

def _WD_DebugRoutine():
    global _WD_PrivState, _WD_TBModule_, _WD_PrivFrame
    
    while True:
        try:
            arrows = ['>>>'] * _WD_PrivState._dbg_depth
            input_data = input(f'[WD] {" | ".join(arrows)} ')
            cmd = input_data.lstrip()
            
            if cmd.startswith('.exit'):
                break
            elif cmd.startswith('.traceon'):
                if _WD_PrivState._trace_enabled:
                    print('Trace already ON.')
                else:
                    dbg_trace(_WD_PrivState._WDProvider, 'Trace ON.', up_stack=_WD_StkLevel_+1)
                    WD_EnableTrace(_WD_PrivFrame=_WD_PrivFrame)
                    _WD_PrivState._dirty_frames.append(_WD_PrivFrame)
            elif cmd.startswith('.traceoff'):
                if not _WD_PrivState._trace_enabled:
                    print('Trace already OFF.')
                else:
                    dbg_trace(_WD_PrivState._WDProvider, 'Trace OFF.', up_stack=_WD_StkLevel_+1)
                    WD_DisableTrace()
            elif cmd.startswith('.step'):
                if not _WD_PrivState._trace_enabled:
                    print('Command ".step" is not permitted while trace is OFF. Enable it by ".traceon" command.')
                else:
                    cmd = cmd.lstrip('.step').strip()
                    step_count = 1
                    
                    if cmd != '':
                        if not cmd.isdigit():
                            print('Invalid step count.')
                            
                            continue
                        
                        step_count = int(cmd)
                    _WD_PrivState._step_count = step_count
                    
                    break
            elif cmd.startswith(('.int3', '.break')):
                dbg_trace(_WD_PrivState._WDProvider, 'Break signal (INT3)', up_stack=_WD_StkLevel_+1)
                if not IsDebuggerPresent():
                    print('Native debugger is not connected.')
                else:
                    DebugBreak()
            else:
                print(eval(input_data))
        except (EOFError, KeyboardInterrupt):
            print()
            continue
        except SyntaxError:
            try:
                exec(input_data)
            except Exception as e:
                e.__cause__ = None
                _WD_TBModule_.print_exception(e)
                continue
        except Exception as e:
            e.__cause__ = None
            _WD_TBModule_.print_exception(e)
            continue
        
def _WD_TraceRoutine(frame: types.FrameType, event: str, arg):
    if frame.f_code.co_qualname.startswith(('_WD_', 'WD_')):
        return _WD_TraceRoutine
    
    if event == 'line':
        if _wd_state._step_count == -1:
            return _WD_TraceRoutine
        
        if _wd_state._step_count != 0:
            _wd_state._step_count -= 1
        else:
            WD_Breakpoint(_WD_PrivFrame=frame, _WD_StackPlus=1)
            _wd_state._step_count = -1
            
    return _WD_TraceRoutine

class _WD_Context:
    _wd_caller_frame: types.FrameType
    _wd_stack_level: int
    wd_globals: dict
    
    def __init__(self, caller_frame: types.FrameType, stack_level: int=0):
        self._wd_caller_frame = caller_frame
        self._wd_stack_level = stack_level
    
    def __enter__(self):
        self.wd_globals = self._wd_caller_frame.f_globals
        _wd_state._dbg_depth += 1
        
        self.wd_globals['_WD_TBModule_'] = traceback
        self.wd_globals['_WD_PrivState'] = _wd_state
        self.wd_globals['_WD_PrivFrame'] = self._wd_caller_frame
        self.wd_globals['_WD_StkLevel_'] = self._wd_stack_level
        
        return self
    
    def __exit__(self, *args):
        del self.wd_globals['_WD_TBModule_']
        del self.wd_globals['_WD_PrivState']
        del self.wd_globals['_WD_PrivFrame']
        del self.wd_globals['_WD_StkLevel_']
        
        _wd_state._dbg_depth -= 1

def WD_Breakpoint(*args, **kwargs):
    if '_WD_PrivFrame' in kwargs:
        caller_frame = kwargs['_WD_PrivFrame']
    else:
        caller_frame = get_caller_frame()
    stack_level = 1
    if '_WD_StackPlus' in kwargs:
        stack_level += kwargs['_WD_StackPlus']
    
    dbg_trace(_wd_state._WDProvider, 'Breakpoint called', up_stack=1)
    
    with _WD_Context(caller_frame, stack_level) as ctx:
        exec(_WD_DebugRoutine.__code__, ctx.wd_globals, caller_frame.f_locals)
        
def WD_Disable():
    sys.breakpointhook = _wd_state._prev_breakpointhook
    WD_DisableTrace(**kwargs)
    
def WD_Enable():
    _wd_state._prev_breakpointhook = sys.breakpointhook
    sys.breakpointhook = WD_Breakpoint

def WD_EnableTrace(**kwargs):
    _wd_state._prev_trace = sys.gettrace()
    _wd_state._trace_enabled = True
    sys.settrace(_WD_TraceRoutine)
    
    if '_WD_PrivFrame' in kwargs:
        caller_frame = kwargs['_WD_PrivFrame']
        caller_frame: types.FrameType
        caller_frame.f_trace = _WD_TraceRoutine

def WD_DisableTrace():
    sys.settrace(_wd_state._prev_trace)
    _wd_state._trace_enabled = False
    
    for frame in _wd_state._dirty_frames:
        frame: types.FrameType
        frame.f_trace = _wd_state._prev_trace

_wd_state = _WD_STATE()