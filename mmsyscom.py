"""
/*==========================================================================
 *
 *  mmsyscom.h -- Common Include file for Multimedia API's
 *
 *  Version 4.00
 *
 *  Copyright (C) 1992-1998 Microsoft Corporation.  All Rights Reserved.
 *
 *==========================================================================
 */
"""

from . import cpreproc
if cpreproc.pragma_once("_INC_MMSYSCOM"):
    from .minwindef import *
    from .sdkddkver import WIN32_WINNT_NT4
    
    # REGION *** Desktop Family or OneCore Family ***
    
    """
    /****************************************************************************

                    General constants and data types

    ****************************************************************************/
    """
    
    # general constants
    MAXPNAMELEN = 32 # max product name length(including NULL)
    MAXERRORLENGTH = 256 # max error text length(including NULL)
    MAX_JOYSTICKOEMVXDNAME = 260 # max oem vxd name length(including NULL)

    """

    *  Microsoft Manufacturer and Product ID's(these have been moved to
    *  MMREG.H for Windows 4.00 and above).

    """

    if cpreproc.get_version() <= WIN32_WINNT_NT4:
        if cpreproc.ifndef("MM_MICROSOFT"):
            MM_MICROSOFT = 1 # Microsoft Corporation
    if cpreproc.ifndef("MM_MIDI_MAPPER"):
        MM_MIDI_MAPPER = 1 # MIDI Mapper
        MM_WAVE_MAPPER = 2 # Wave Mapper
        MM_SNDBLST_MIDIOUT = 3 # Sound Blaster MIDI output port
        MM_SNDBLST_MIDIIN = 4 # Sound Blaster MIDI input port
        MM_SNDBLST_SYNTH = 5 # Sound Blaster internal synthesizer
        MM_SNDBLST_WAVEOUT = 6 # Sound Blaster waveform output
        MM_SNDBLST_WAVEIN = 7 # Sound Blaster waveform input
        MM_ADLIB = 9 # Ad Lib-compatible synthesizer
        MM_MPU401_MIDIOUT = 10 # MPU401-compatible MIDI output port
        MM_MPU401_MIDIIN = 11 # MPU401-compatible MIDI input port
        MM_PC_JOYSTICK = 12 # Joystick adapter
    # general data types
    
    MMVERSION = UINT
    VERSION = UINT
    MMRESULT = UINT
    
    class mmtime_tag(CStructure):
        class U(CUnion):
            class SMPTE(CStructure):
                _fields_ = [
                    ("hour", BYTE), # hours
                    ("min", BYTE), # minutes
                    ("sec", BYTE), # seconds
                    ("frame", BYTE), # frames
                    ("fps", BYTE), # frames per second
                    ("dummy", BYTE), # pad
                    ("pad", BYTE * 2)
                ]
                hour: int
                min: int
                sec: int
                frame: int
                fps: int
                dummy: int
                pad: IArray[int]
            class MIDI(CStructure):
                _fields_ = [
                    ("songptrpos", DWORD) # song pointer position
                ]
                songptrpos: int
            _fields_ = [
                ("ms", DWORD), # milliseconds
                ("sample", DWORD), # samples
                ("cb", DWORD), # byte count
                ("ticks", DWORD), # ticks in MIDI stream
                # SMPTE
                ("smpte", SMPTE),
                # MIDI
                ("midi", MIDI)
            ]
            ms: int
            sample: int
            cb: int
            ticks: int
            smpte: SMPTE
            midi: MIDI
        _fields_ = [
            ("wType", UINT), # indicates the contents of the union
            ("u", U)
        ]
        wType: int
        u: U
    
    MMTIME = mmtime_tag
    PMMTIME = NPMMTIME = LPMMTIME = PTR(MMTIME)
    
    # types for wType field in MMTIME struct
    TIME_MS         = 0x0001  # time in milliseconds
    TIME_SAMPLES    = 0x0002  # number of wave samples
    TIME_BYTES      = 0x0004  # current byte offset
    TIME_SMPTE      = 0x0008  # SMPTE time
    TIME_MIDI       = 0x0010  # MIDI time
    TIME_TICKS      = 0x0020  # Ticks within MIDI stream
    
    MAKEFOURCC = lambda ch0, ch1, ch2, ch3: \
        (DWORD(BYTE(ch0).value).value | \
        (DWORD(BYTE(ch1).value).value) << 8) | \
        (DWORD(BYTE(ch3).value).value << 16) | (DWORD(BYTE(ch4).value).value << 24)
    
    """
    ***************************************************************************

    Multimedia Extensions Window Messages

    ***************************************************************************
    """

    MM_JOY1MOVE = 0x3A0 # joystick
    MM_JOY2MOVE = 0x3A1
    MM_JOY1ZMOVE = 0x3A2
    MM_JOY2ZMOVE = 0x3A3
    MM_JOY1BUTTONDOWN = 0x3B5
    MM_JOY2BUTTONDOWN = 0x3B6
    MM_JOY1BUTTONUP = 0x3B7
    MM_JOY2BUTTONUP = 0x3B8
    MM_MCINOTIFY = 0x3B9 # MCI
    MM_WOM_OPEN = 0x3BB # waveform output
    MM_WOM_CLOSE = 0x3BC
    MM_WOM_DONE = 0x3BD
    MM_WIM_OPEN = 0x3BE # waveform input
    MM_WIM_CLOSE = 0x3BF
    MM_WIM_DATA = 0x3C0
    MM_MIM_OPEN = 0x3C1 # MIDI input
    MM_MIM_CLOSE = 0x3C2
    MM_MIM_DATA = 0x3C3
    MM_MIM_LONGDATA = 0x3C4
    MM_MIM_ERROR = 0x3C5
    MM_MIM_LONGERROR = 0x3C6
    MM_MOM_OPEN = 0x3C7 # MIDI output
    MM_MOM_CLOSE = 0x3C8
    MM_MOM_DONE = 0x3C9
    # these are also in msvideo.h
    MM_DRVM_OPEN = 0x3D0 # installable drivers
    MM_DRVM_CLOSE = 0x3D1
    MM_DRVM_DATA = 0x3D2
    MM_DRVM_ERROR = 0x3D3
    # these are used by msacm.h
    MM_STREAM_OPEN = 0x3D4
    MM_STREAM_CLOSE = 0x3D5
    MM_STREAM_DONE = 0x3D6
    MM_STREAM_ERROR = 0x3D7
    if cpreproc.get_version() >= WIN32_WINNT_NT4:
        MM_MOM_POSITIONCB = 0x3CA # Callback for MEVT_POSITIONCB
        MM_MCISIGNAL = 0x3CB
        MM_MIM_MOREDATA = 0x3CC # MIM_DONE w/ pending events
    # _WINVER >= 0x0400
    MM_MIXM_LINE_CHANGE = 0x3D0 # mixer line change notify
    MM_MIXM_CONTROL_CHANGE = 0x3D1 # mixer control change notify

    """
    ***************************************************************************

    String resource number bases(internal use)

    ***************************************************************************
    """

    MMSYSERR_BASE = 0
    WAVERR_BASE = 32
    MIDIERR_BASE = 64
    TIMERR_BASE = 96
    JOYERR_BASE = 160
    MCIERR_BASE = 256
    MIXERR_BASE = 1024
    MCI_STRING_OFFSET = 512
    MCI_VD_OFFSET = 1024
    MCI_CD_OFFSET = 1088
    MCI_WAVE_OFFSET = 1152
    MCI_SEQ_OFFSET = 1216

    """
    ***************************************************************************

    General error return values

    ***************************************************************************
    """

    # general error return values
    MMSYSERR_NOERROR = 0 # no error
    MMSYSERR_ERROR = (MMSYSERR_BASE + 1) # unspecified error
    MMSYSERR_BADDEVICEID = (MMSYSERR_BASE + 2) # device ID out of range
    MMSYSERR_NOTENABLED = (MMSYSERR_BASE + 3) # driver failed enable
    MMSYSERR_ALLOCATED = (MMSYSERR_BASE + 4) # device already allocated
    MMSYSERR_INVALHANDLE = (MMSYSERR_BASE + 5) # device handle is invalid
    MMSYSERR_NODRIVER = (MMSYSERR_BASE + 6) # no device driver present
    MMSYSERR_NOMEM = (MMSYSERR_BASE + 7) # memory allocation error
    MMSYSERR_NOTSUPPORTED = (MMSYSERR_BASE = + 8) # function isn't supported
    MMSYSERR_BADERRNUM = (MMSYSERR_BASE + 9) # error value out of range
    MMSYSERR_INVALFLAG = (MMSYSERR_BASE + 10) # invalid flag passed
    MMSYSERR_INVALPARAM = (MMSYSERR_BASE + 11) # invalid parameter passed
    MMSYSERR_HANDLEBUSY = (MMSYSERR_BASE + 12) # handle being used
    # simultaneously on another
    # thread(eg callback)
    MMSYSERR_INVALIDALIAS = (MMSYSERR_BASE = + 13) # specified alias not found
    MMSYSERR_BADDB = (MMSYSERR_BASE + 14) # bad registry database
    MMSYSERR_KEYNOTFOUND = (MMSYSERR_BASE + 15) # registry key not found
    MMSYSERR_READERROR = (MMSYSERR_BASE + 16) # registry read error
    MMSYSERR_WRITEERROR = (MMSYSERR_BASE + 17) # registry write error
    MMSYSERR_DELETEERROR = (MMSYSERR_BASE + 18) # registry delete error
    MMSYSERR_VALNOTFOUND = (MMSYSERR_BASE + 19) # registry value not found
    MMSYSERR_NODRIVERCB = (MMSYSERR_BASE + 20) # driver does not call DriverCallback
    MMSYSERR_MOREDATA = (MMSYSERR_BASE + 21) # more data to be returned
    MMSYSERR_LASTERROR = (MMSYSERR_BASE + 21) # last error in range
    HDRVR = HANDLE

    """
    ***************************************************************************

    Driver callback support

    ***************************************************************************
    """

    # flags used with waveOutOpen(), waveInOpen(), midiInOpen(), and
    # midiOutOpen() to specify the type of the dwCallback parameter.
    CALLBACK_TYPEMASK = 0x00070000 # callback type mask
    CALLBACK_NULL = 0x00000000 # no callback
    CALLBACK_WINDOW = 0x00010000 # dwCallback is a HWND
    CALLBACK_TASK = 0x00020000 # dwCallback is a HTASK
    CALLBACK_FUNCTION = 0x00030000 # dwCallback is a FARPROC
    CALLBACK_THREAD = (CALLBACK_TASK) # thread ID replaces 16 bit task
    CALLBACK_EVENT = 0x00050000 # dwCallback is an EVENT Handle
    
    DRVCALLBACK = CALLBACK(VOID, HDRVR, UINT, DWORD_PTR, DWORD_PTR, DWORD_PTR)
    LPDRVCALLBACK = PDRVCALLBACK = PTR(DRVCALLBACK)
    
    # REGION ***
# _INC_MMSYSCOM