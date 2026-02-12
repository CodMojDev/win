from . import cpreproc

if cpreproc.pragma_once("__identitycommon_h__"):
    # REGION *** Desktop Family
    
    from .minwindef import INT
    
    IDENTITY_TYPE = INT
    _IdentityType = IDENTITY_TYPE
    if True:
        IDENTITIES_ALL	= 0
        IDENTITIES_ME_ONLY	= 0x1

    # REGION ***