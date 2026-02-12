from . import cpreproc

if cpreproc.pragma_once("__tpmvscattestation_h__"):
    from .sdkddkver import WIN32_WINNT_WINTHRESHOLD
    from .minwindef import INT
    
    # REGION *** Desktop Family ***
    
    if cpreproc.get_version() >= WIN32_WINNT_WINTHRESHOLD:
        TPMVSC_ATTESTATION_TYPE = INT
        if True:
            # [v1_enum]
            TPMVSC_ATTESTATION_NONE	= 0
            TPMVSC_ATTESTATION_AIK_ONLY	= 1
            TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE = 2

    # (_WINVER >= WIN32_WINNT_WINTHRESHOLD)
    
    # REGION ***