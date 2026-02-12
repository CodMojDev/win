"""
*********************************************************************
*                  Microsoft Windows                               **
*            Copyright(c) Microsoft Corp., 1996-1997               **
*********************************************************************
"""

from . import cpreproc

if cpreproc.pragma_once("__MIMEDISP_H__"):
    # REGION *** Desktop Family ***

    DISPID_IMIMEEDIT_BASE = 100
    DISPID_IMIMEEDIT_SRC = (DISPID_IMIMEEDIT_BASE + 1)
    DISPID_IMIMEEDIT_STYLE = (DISPID_IMIMEEDIT_BASE + 2)
    DISPID_IMIMEEDIT_EDITMODE = (DISPID_IMIMEEDIT_BASE + 3)
    DISPID_IMIMEEDIT_MSGSRC = (DISPID_IMIMEEDIT_BASE + 4)
    DISPID_IMIMEEDIT_TEXT = (DISPID_IMIMEEDIT_BASE + 5)
    DISPID_IMIMEEDIT_HTML = (DISPID_IMIMEEDIT_BASE + 6)
    DISPID_IMIMEEDIT_CLEAR = (DISPID_IMIMEEDIT_BASE + 7)
    DISPID_IMIMEEDIT_DOCUMENT = (DISPID_IMIMEEDIT_BASE + 8)

    # REGION ***
#__MIMEDISP_H__