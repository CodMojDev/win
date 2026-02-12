"""
/********************************************************
*                                                       *
*   Copyright (C) Microsoft. All rights reserved.       *
*                                                       *
********************************************************/

//-----------------------------------------------------------------------------
// File:        ADODEF.H
//
// Contents:    ADO version definition.
//          
// 
// Comments:
//
//-----------------------------------------------------------------------------
"""

from . import cpreproc

from .guiddef import GUID

if cpreproc.pragma_once("_ADODEF_H_"):
    # Change the version numbers below when there are any updates in the version of the type libraries, 
    # which should be changed after some updates to the type libraries

    # TYPELIB MAJOR VERSIONS
    ADO_MAJOR           = 6
    ADOR_MAJOR          = 6
    ADOX_MAJOR          = 6
    ADOMD_MAJOR         = 6
    JRO_MAJOR           = 2

    # TYPELIB MINOR VERSION
    ADO_MINOR           = 1
    ADOR_MINOR          = 0
    ADOX_MINOR          = 0
    ADOMD_MINOR         = 0
    JRO_MINOR           = 6

    ADO_VERSION         = f"{ADO_MAJOR}.{ADO_MINOR}"
    ADOR_VERSION        = f"{ADOR_MAJOR}.{ADOR_MINOR}"
    ADOX_VERSION        = f"{ADOX_MAJOR}.{ADOX_MINOR}"
    ADOMD_VERSION       = f"{ADOMD_MAJOR}.{ADOMD_MINOR}"
    JRO_VERSION         = f"{JRO_MAJOR}.{JRO_MINOR}"

    ADO_LIBRARYNAME     = "Microsoft ActiveX Data Objects 6.1 Library"
    ADOR_LIBRARYNAME    = "Microsoft ActiveX Data Objects Recordset 6.0 Library"
    ADOX_LIBRARYNAME    = "Microsoft ADO Ext. 6.0 for DDL and = Security"
    ADOMD_LIBRARYNAME   = "Microsoft ActiveX Data Objects (Multi-dimensional) 6.0 Library"
    JRO_LIBRARYNAME     = "Microsoft Jet and Replication Objects 2.6 Library"

    ADOMD_TYPELIB_UUID  = GUID("{22813728-8BD3-11D0-B4EF-00A0C9138CA4}")
    JRO_TYPELIB_UUID    = GUID("{AC3B8B4C-B6CA-11d1-9F31-00C04FC29D52}")

# _ADODEF_H_