from ..minwindef import *

CRTDECL = CDECL

from ..defbase import declare

ucrtbased = W_CDLL('ucrtbased.dll')

errcode = INT
errno_t = INT
time32_t = LONG
time64_t = INT64

rsize_t = SIZE_T
void = VOID
size_t = SIZE_T
char = CHAR
int8_t = INT8
uint8_t = UINT8
int16_t = INT16
uint16_t = UINT16
int32_t = INT32
uint32_t = UINT32
int64_t = INT64
uint64_t = UINT64
unsigned = UINT
uint = UINT
int_t = INT
ulong = ULONG
long = LONG
ulonglong = ULONGLONG
longlong = LONGLONG
time_t = c_time_t
ptrdiff_t = SSIZE_T
intptr_t = SSIZE_T
wchar_t = WCHAR
uintptr_t = SSIZE_T

report_gsfailure = declare(ucrtbased.__report_gsfailure, void, uintptr_t)

security_cookie = uintptr_t
#vcrt_malloc_normal = lambda _Size: malloc(_Size)
#vcrt_calloc_normal = lambda _Count, _Size: calloc(_Count, _Size)
#vcrt_free_normal = lambda _Memory: free(_Memory)