#*********************************************************************
#*                  Microsoft Windows                               **
#*            Copyright(c) Microsoft Corp., 1996-1997               **
#*********************************************************************

#;begin_internal
"""
/***********************************************************************************************

  This is a distributed SDK component - do not put any #includes or other directives that rely
  upon files not dropped. If in doubt - build iedev

  If you add comments please include either ;BUGBUG at the beginning of a single line OR
  enclose in a ;begin_internal, ;end_internal block - such as this one!

 ***********************************************************************************************/
"""
#;end_internal

#;begin_internal

from . import cpreproc

if cpreproc.pragma_once("__XMLDSODID_H__"):
    #;end_internal

    # REGION *** Desktop Family ***

    DISPID_XMLDSO                      = 0x00010000
    DISPID_XMLDSO_DOCUMENT             = DISPID_XMLDSO  +  1
    DISPID_XMLDSO_JAVADSOCOMPATIBLE    = DISPID_XMLDSO_DOCUMENT  +  1

    # REGION ***

    #;begin_internal
# __XMLDSODID_H__

#;end_internal