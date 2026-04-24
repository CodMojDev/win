from ..minwindef import *

class EventRegistrationToken(CStructure):
    _fields_ = [('value', INT64)]
    value: int