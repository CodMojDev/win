from .winnt import *
from .sdkddkver import *

class RUNTIME_FUNCTION(CStructure):
    class _U(CUnion):
        _fields_ = [
            ('UnwindInfoAddress', DWORD),
            ('UnwindData', DWORD)
        ]
    _fields_ = [
        ('BeginAddress', DWORD),
        ('EndAddress', DWORD),
        ('_u', _U)
    ]
    _anonymous_ = ['_u']
    BeginAddress: int
    EndAddress: int
    UnwindInfoAddress: int
    UnwindData: int

PRUNTIME_FUNCTION = PTR(RUNTIME_FUNCTION)

class STACKFRAME32(CStructure):
    _fields_ = [
        ('EbpNext', DWORD),
        ('Ret', DWORD)
    ]
    EbpNext: int
    Ret: int
    
PSTACKFRAME32 = PTR(STACKFRAME32)

ntdll = get_win_library('ntdll.dll')
if cpreproc.get_version() >= WIN32_WINNT_VISTA:
    _STACK_BUFFER = (PVOID * 65535)()
else:
    _STACK_BUFFER = (PVOID * 62)()

@ntdll.foreign(USHORT, ULONG, ULONG, PLPVOID, PULONG)
def RtlCaptureStackBackTrace(FramesToSkip: int, FramesToCapture: int, BackTrace: IPointer[PVOID], BackTraceHash: IPointer[ULONG]) -> int: ...

if not cpreproc.defined('_M_IX86'):
    @ntdll.foreign(PRUNTIME_FUNCTION, DWORD64, PDWORD64, PVOID)
    def RtlLookupFunctionEntry(ControlPc: int, ImageBase: IPointer[DWORD64], HistoryTable: WT_ADDRLIKE) -> IPointer[RUNTIME_FUNCTION]: ...
    
    @ntdll.foreign(PVOID, DWORD, DWORD64, DWORD64, PRUNTIME_FUNCTION, PCONTEXT, PLPVOID, PDWORD64, PVOID)
    def RtlVirtualUnwind(HandlerType: int, ImageBase: int, ControlPc: int, FunctionEntry: IPointer[RUNTIME_FUNCTION], ContextRecord: IPointer[CONTEXT], HandlerData: IPointer[PVOID], EstablisherFrame: IPointer[DWORD64], ContextPointers: int) -> int: ...

kernel32 = get_win_library('kernel32.dll')

@kernel32.foreign(BOOL, PVOID, UINT_PTR)
def IsBadReadPtr(lp: WT_ADDRLIKE, cb: int) -> int: ...

def get_native_stack(context: CONTEXT | None = None) -> list[int]:
    if context is None:
        number = RtlCaptureStackBackTrace(0, len(_STACK_BUFFER), _STACK_BUFFER, NULL)
        buffer = i_cast(_STACK_BUFFER, PTR(PVOID * number)).contents
        return list(buffer)
    if cpreproc.defined('_M_IX86'):
        stack = [context.Eip]
        frame = i_cast(context.Ebp, PSTACKFRAME32)
        valid = context.Esp
        while frame:
            p = PtrUtil.get_address(frame)
            if p < valid or p & 3:
                break
            if not IsBadReadPtr(frame, sizeof(STACKFRAME32)):
                break
            stack.append(frame.contents.Ret)
            if frame.contents.EbpNext <= PtrUtil.get_address(frame):
                break
            valid = p + sizeof(STACKFRAME32)
            frame = i_cast(frame.contents.EbpNext, PSTACKFRAME32)
        return stack
    elif cpreproc.defined('_M_AMD64'):
        context = context.copy()
        image_base = DWORD64()
        handler = PVOID()
        establisher = ULONG64()
        entry = RtlLookupFunctionEntry(context.Rip, byref(image_base), NULL)
        stack = []
        while context.Rip != 0:
            stack.append(context.Rip)
            if entry:
                RtlVirtualUnwind(UNW_FLAG_NHANDLER, image_base, context.Rip, entry, context, byref(handler), byref(establisher), NULL)
            else:
                break
        return stack
    else:
        raise RuntimeError('Invalid Processor architecture.')