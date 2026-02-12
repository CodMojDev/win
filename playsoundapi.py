"""
 *********************************************************************************
 *                                                                               *
 * playsoundapi.h -- ApiSet Contract for api-ms-win-mm-playsound-l1-1-0          *
 *                                                                               *
 * Copyright (c) Microsoft Corporation. All rights reserved.                     *
 *                                                                               *
 *********************************************************************************
"""

from typing import (Callable)

from . import cpreproc
from .defbase import *

from .winnt import (BOOL, LPCSTR, UINT, LPCWSTR, DWORD, BYTE, HMODULE)

from ctypes import windll

if cpreproc.pragma_once("_PLAYSOUNDAPI_H_"):
    winmm = W_WinDLL("winmm.dll")

    # REGION *** Desktop Family ***

    if cpreproc.ifndef("MMNOSOUND"):

        """
        ***************************************************************************

            Sound support

        ***************************************************************************
        """

        if cpreproc.ifdef("_WIN32"):
                sndPlaySoundA = declare(winmm.sndPlaySoundA, BOOL, LPCSTR, UINT)
                sndPlaySoundW = declare(winmm.sndPlaySoundW, BOOL, LPCWSTR, UINT)
                sndPlaySound = unicode(sndPlaySoundW, sndPlaySoundA)
        else:

            """

            *  flag values for fuSound and fdwSound arguments on [snd]PlaySound

            """

            SND_SYNC = 0x0000 # play synchronously (default)
            SND_ASYNC = 0x0001 # play asynchronously
            SND_NODEFAULT = 0x0002 # silence (!default) if sound not found
            SND_MEMORY = 0x0004 # pszSound points to a memory file
            SND_LOOP = 0x0008 # loop the sound until next sndPlaySound
            SND_NOSTOP = 0x0010 # don't stop any currently playing sound
            SND_NOWAIT = 0x00002000 # don't wait if the driver is busy
            SND_ALIAS = 0x00010000 # name is a registry alias
            SND_ALIAS_ID = 0x00110000 # alias is a predefined ID
            SND_FILENAME = 0x00020000 # name is file name
            SND_RESOURCE = 0x00040004 # name is resource name or atom
            SND_PURGE = 0x0040 # purge non-static events for task
            SND_APPLICATION = 0x0080 # look for application specific association
            SND_SENTRY = 0x00080000 # Generate a SoundSentry event with this sound
            SND_RING = 0x00100000 # Treat this as a "ring" from a communications app - don't duck me
            SND_SYSTEM = 0x00200000 # Treat this as a system sound
            SND_ALIAS_START = 0 # alias base
            if cpreproc.ifdef("_WIN32"):
                sndAlias = lambda ch0, ch1: (SND_ALIAS_START + (DWORD(BYTE(ch0).value).value | (DWORD(BYTE(ch1).value).value << 8)))
                SND_ALIAS_SYSTEMASTERISK = sndAlias('S', '*')
                SND_ALIAS_SYSTEMQUESTION = sndAlias('S', '?')
                SND_ALIAS_SYSTEMHAND = sndAlias('S', 'H')
                SND_ALIAS_SYSTEMEXIT = sndAlias('S', 'E')
                SND_ALIAS_SYSTEMSTART = sndAlias('S', 'S')
                SND_ALIAS_SYSTEMWELCOME = sndAlias('S', 'W')
                SND_ALIAS_SYSTEMEXCLAMATION = sndAlias('S', '!')
                SND_ALIAS_SYSTEMDEFAULT = sndAlias('S', 'D')
                PlaySoundA = declare(winmm.PlaySoundA, BOOL, LPCSTR, HMODULE, DWORD)
                PlaySoundW = declare(winmm.PlaySoundW, BOOL, LPCWSTR, HMODULE, DWORD)
                PlaySound = unicode(PlaySoundW, PlaySoundA)
            else:
                PlaySound = declare(winmm.PlaySound, BOOL, LPCSTR, HMODULE, DWORD)

        # REGION ***
    # !MMNOSOUND
# _PLAYSOUNDAPI_H_