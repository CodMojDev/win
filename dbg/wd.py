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
    class _WD_FUNCS:
        __slots__ = ['WD_Breakpoint', 'WD_EnableTrace', 'WD_DisableTrace', 
                     'dbg_trace', 'IsDebuggerPresent', 'DebugBreak']
    __slots__ = ['_WDProvider', '_prev_breakpointhook', '_dbg_depth',
                 '_prev_trace', '_trace_enabled', '_step_count',
                 '_dirty_frames', '_prev_excepthook', '_funcs']
    
    def __init__(self):
        self._WDProvider = WET_PROVIDER('WD')
        self._prev_breakpointhook = sys.breakpointhook
        self._prev_excepthook = sys.excepthook
        self._prev_trace = sys.gettrace()
        self._trace_enabled = False
        self._step_count = False
        self._dirty_frames = []
        self._dbg_depth = 0
        self._funcs = _WD_STATE._WD_FUNCS()
        self._funcs.WD_Breakpoint = WD_Breakpoint
        self._funcs.WD_DisableTrace = WD_DisableTrace
        self._funcs.WD_EnableTrace = WD_EnableTrace
        self._funcs.dbg_trace = dbg_trace
        self._funcs.IsDebuggerPresent = IsDebuggerPresent
        self._funcs.DebugBreak = DebugBreak
        
        if cpreproc.ifndef('WD_DISABLED'):
            sys.breakpointhook = WD_Breakpoint

if TYPE_CHECKING:
    _WD_PrivFrame: types.FrameType = None
    _WD_PrivDown_: types.FrameType = None
    _WD_PrivState: _WD_STATE = None
    _WD_TBModule_: traceback = None
    _WD_StkLevel_: int = None

def _WD_DebugRoutine():
    global _WD_PrivState, _WD_TBModule_, _WD_PrivFrame, _WD_PrivDown_, _WD_StkLevel_
    
    while True:
        try:
            _WD_Arrows = ['>>>'] * _WD_PrivState._dbg_depth
            _WD_InputData = input(f'[WD] {" | ".join(_WD_Arrows)} ')
            _WD_Cmd = _WD_InputData.lstrip()
            
            if _WD_Cmd.startswith('.exit'):
                break
            elif _WD_Cmd.startswith('.traceon'):
                if _WD_PrivState._trace_enabled:
                    print('Trace already ON.')
                else:
                    _WD_PrivState._funcs.dbg_trace(_WD_PrivState._WDProvider, 'Trace ON.', up_stack=_WD_StkLevel_+1)
                    _WD_PrivState._funcs.WD_EnableTrace(_WD_PrivFrame=_WD_PrivFrame)
                    _WD_PrivState._dirty_frames.append(_WD_PrivFrame)
            elif _WD_Cmd.startswith('.traceoff'):
                if not _WD_PrivState._trace_enabled:
                    print('Trace already OFF.')
                else:
                    _WD_PrivState._funcs.dbg_trace(_WD_PrivState._WDProvider, 'Trace OFF.', up_stack=_WD_StkLevel_+1)
                    _WD_PrivState._funcs.WD_DisableTrace()
            elif _WD_Cmd.startswith('.step'):
                if not _WD_PrivState._trace_enabled:
                    print('Command ".step" is not permitted while trace is OFF. Enable it by ".traceon" command.')
                else:
                    _WD_Cmd = _WD_Cmd.lstrip('.step').strip()
                    _WD_StepCount = 1
                    
                    if _WD_Cmd != '':
                        if not _WD_Cmd.isdigit():
                            print('Invalid step count.')
                            
                            continue
                        
                        _WD_StepCount = int(_WD_Cmd)
                    _WD_PrivState._step_count = _WD_StepCount
                    
                    break
            elif _WD_Cmd.startswith(('.int3', '.break')):
                _WD_PrivState._funcs.dbg_trace(_WD_PrivState._WDProvider, 'Break signal (INT3)', up_stack=_WD_StkLevel_+1)
                if not _WD_PrivState._funcs.IsDebuggerPresent():
                    print('Native debugger is not connected.')
                else:
                    _WD_PrivState._funcs.DebugBreak()
            elif _WD_Cmd.startswith('.restartbp'):
                _WD_PrivState._funcs.dbg_trace(_WD_PrivState._WDProvider, 'Restart BP Request', up_stack=_WD_StkLevel_+1)
                _WD_Cmd = _WD_Cmd.lstrip('.restartbp').strip()
                _WD_Frame_Local = _WD_Cmd
                
                _WD_FrameSetted = False
                if _WD_Frame_Local == '#up':
                    _WD_Frame = _WD_PrivFrame.f_back
                    if _WD_Frame is None:
                        print('No upper frame.')
                    else:
                        _WD_Frame.f_globals['_WD_PrivDown_'] = _WD_Frame
                    _WD_FrameSetted = True
                elif _WD_Frame_Local == '#down':
                    _WD_Frame = _WD_PrivDown_
                    if _WD_Frame is None:
                        print('No lower frame.')
                    _WD_FrameSetted = True
                
                if not _WD_FrameSetted:
                    _WD_Locs = locals()
                    if not _WD_Frame_Local in _WD_Locs:
                        print(f'No variable "{_WD_Frame_Local}".')
                        continue
                    _WD_Frame = _WD_Locs[_WD_Frame_Local]
                    
                if _WD_Frame is None:
                    continue
                
                _WD_PrivState._dbg_depth -= 1
                _WD_PrivState._funcs.WD_Breakpoint(_WD_PrivFrame=_WD_Frame)
                break                    
            elif _WD_Cmd.startswith('.current'):
                print(_WD_PrivFrame)
            elif _WD_Cmd.startswith('.locals'):
                _WD_Locs = locals()
                for _WD_K, _WD_V in _WD_Locs.items():
                    if not _WD_K.startswith('_WD_'):
                        print(f'{_WD_K}: "{_WD_V}"')
            else:
                _WD_Result = eval(_WD_InputData)
                if _WD_Result is not None:
                    print(_WD_Result)
        except (EOFError, KeyboardInterrupt):
            print()
            continue
        except SyntaxError:
            try:
                exec(_WD_InputData)
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
        if not '_WD_PrivDown_' in self.wd_globals:
            self.wd_globals['_WD_PrivDown_'] = None
        
        return self
    
    def _test_and_delete(self, name: str):
        if name in self.wd_globals:
            del self.wd_globals[name]
    
    def __exit__(self, *args):
        self._test_and_delete('_WD_TBModule_')
        self._test_and_delete('_WD_PrivState')
        self._test_and_delete('_WD_PrivFrame')
        self._test_and_delete('_WD_StkLevel_')
        self._test_and_delete('_WD_PrivDown_')
        
        _wd_state._dbg_depth -= 1

def WD_BPOnException():
    _wd_state._prev_excepthook = sys.excepthook
    sys.excepthook = _WD_ExceptionHook
    
def WD_BPOnExceptionOff():
    sys.excepthook = _wd_state._prev_excepthook
    
def _WD_ExceptionHook(t, exc, tb):
    last_tb = tb
    while last_tb.tb_next:
        last_tb = last_tb.tb_next
    
    frame = last_tb.tb_frame
    print(f'WD Catched Exception: {exc}')
    WD_Breakpoint(_WD_PrivFrame=frame, _WD_StackPlus=1)

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
        
def WD_CurrentFrame():
    return get_caller_frame().f_globals['_WD_PrivFrame']

def WD_Disable():
    sys.breakpointhook = _wd_state._prev_breakpointhook
    WD_DisableTrace()
    
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