from win.winreg import *
from win.defbase_errordef import *

import winreg
import errno

def DeleteTree(key: winreg.HKEYType | int, subkey: str):
    lStatus = RegDeleteTreeW(int(key), subkey)
    if lStatus == 0: return
    if lStatus == ERROR_PATH_NOT_FOUND or lStatus == ERROR_FILE_NOT_FOUND:
        raise FileNotFoundError(errno.ENOENT, win_errors[lStatus], subkey, lStatus)
    elif lStatus == ERROR_ACCESS_DENIED:
        raise PermissionError(errno.EACCES, win_errors[lStatus], subkey, lStatus)
    raise WinException(lStatus)

def CopyTree(key_src: winreg.HKEYType | int, subkey: str | None, key_dest: winreg.HKEYType | int):
    lStatus = RegCopyTreeW(int(key), subkey, int(key_dest))
    if lStatus == 0: return
    if lStatus == ERROR_PATH_NOT_FOUND or lStatus == ERROR_FILE_NOT_FOUND:
        raise FileNotFoundError(errno.ENOENT, win_errors[lStatus], subkey, lStatus)
    elif lStatus == ERROR_ACCESS_DENIED:
        raise PermissionError(errno.EACCES, win_errors[lStatus], subkey, lStatus)
    raise WinException(lStatus)