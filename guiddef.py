###################
# IN CONSTRUCTION
###################

from .basetsd import *

from . import cpreproc

from .defbase import *

from .com.guid import *

if cpreproc.pragma_once("GUID_DEFINED"):
    DEFINE_OLEGUID = lambda l, w1, w2: GUID(f"{str(l).zfill(8)}-{str(w1).zfill(4)}-{str(w2).zfill(4)}-C000000000046")
    if cpreproc.pragma_once("_GUIDDEF_H_"): ...