from ..minwindef import LPCWSTR, UINT, VOID, cdll

from ..defbase import declare

import inspect

ucrtbase = cdll.ucrtbased

wassert = declare(ucrtbase._wassert, VOID, LPCWSTR, LPCWSTR, UINT)

def cassert(cond: bool, expression: str):
    assert isinstance(expression, str)
    if not cond:
        cframe = inspect.currentframe().f_back
        lineno = cframe.f_lineno
        file = cframe.f_code.co_filename
        wassert(expression, file, lineno)