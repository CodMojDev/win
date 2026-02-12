from .minwindef import *

from functools import wraps

class NOMARSHAL:
    pass

def marshal_as(*arguments):
    def _marshal_as(func):
        def marshaled_func(*args):
            return func(*[cast(j, arguments[i]) if arguments[i] is not NOMARSHAL else j for i, j in enumerate(args)])
        return marshaled_func
    return _marshal_as