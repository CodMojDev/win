import os

if os.name != 'nt':
    raise SystemError("The OS is not WinNT! Other Systems don't supported!")