"""
********************************************************************

  ICWCFG.H

  Copyright(c) Microsoft Corporation, 1996-1998

  *** N O T   F O R   E X T E R N A L   R E L E A S E *******
  *
  * This header file is not intended for distribution outside Microsoft.
  *
  ***********************************************************

  Header file for Internet Connection Wizard external configuration
  routines found in INETCFG.DLL.

  Routines:

  CheckConnectionWizard - Checks which parts of ICW are installed
		and if it has been run before.  It optionally will start
		either the full or manual path of ICW if it is insalled
		but has not been run before.

  History:	10/22/96	Created
		10/24/96	Added defines and typedefs
		2/25/97		Added CreateDirectoryService -- jmazner
		4/24/97		Removed InetCreate*, these are now owned
					by the Account Manager -- jmazner

  Support:	This header file (and INETCFG.DLL) is supported by the
			Internet Connection Wizard team (alias icwcore).  Please
			do not modify this directly.

*********************************************************************
"""

from . import cpreproc

if cpreproc.pragma_once("_ICWCFG_H_"):
    from .defbase import *
    from .minwindef import *
    from .winnt import PSTR
    
    # REGION *** Desktop Family ***

    inetcfg = WinDLL('Inetcfg.dll')

    #
    # defines
    #

    # ICW registry settings

    # HKEY_CURRENT_USER
    ICW_REGPATHSETTINGS	= "Software\\Microsoft\\Internet Connection Wizard"
    ICW_REGKEYCOMPLETED	= "Completed"

    # Maximum field lengths
    ICW_MAX_ACCTNAME	= 256
    ICW_MAX_PASSWORD	= 256	# PWLEN
    ICW_MAX_LOGONNAME	= 256	# UNLEN
    ICW_MAX_SERVERNAME	= 64
    ICW_MAX_RASNAME		= 256	# RAS_MaxEntryName
    ICW_MAX_EMAILNAME	= 64
    ICW_MAX_EMAILADDR	= 128

    # Bit-mapped flags

    # CheckConnectionWizard input flags
    ICW_CHECKSTATUS		= 0x0001

    ICW_LAUNCHFULL		= 0x0100
    ICW_LAUNCHMANUAL	= 0x0200
    ICW_USE_SHELLNEXT	= 0x0400
    ICW_FULL_SMARTSTART	= 0x0800

    # CheckConnectionWizard output flags
    ICW_FULLPRESENT		= 0x0001
    ICW_MANUALPRESENT	= 0x0002
    ICW_ALREADYRUN		= 0x0004

    ICW_LAUNCHEDFULL	= 0x0100
    ICW_LAUNCHEDMANUAL	= 0x0200

    # InetCreateMailNewsAccount input flags
    ICW_USEDEFAULTS		= 0x0001

    #
    # external function typedefs
    #
    PFNCHECKCONNECTIONWIZARD = WINAPI(DWORD, DWORD, LPDWORD)
    PFNSETSHELLNEXT = WINAPI(DWORD, PSTR)

    #
    # external function declarations
    #
    CheckConnectionWizard = declare(inetcfg.CheckConnectionWizard, DWORD, DWORD, LPDWORD)

    SetShellNext = declare(inetcfg.SetShellNext, DWORD, PSTR)

    # REGION ***

# _ICWCFG_H_