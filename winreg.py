"""++ BUILD Version: 0001    // Increment this if a change has global effects

Copyright (c) Microsoft Corporation.  All rights reserved.

Module Name:

    Winreg.h

Abstract:

    This module contains the function prototypes and constant, type and
    structure definitions for the Windows 32-Bit Registry API.

--"""

# type: ignore

from . import cpreproc

from .defbase import *

from .minwindef import *

from .winnt import SECURITY_INFORMATION, PSECURITY_DESCRIPTOR, ACCESS_MASK, LPSECURITY_ATTRIBUTES

if cpreproc.pragma_once("_WINREG_"): 
    advapi32 = W_WinDLL("advapi32.dll")

    #
    # RRF - Registry Routine Flags (for RegGetValue)
    #
    RRF_RT_REG_NONE = 0x00000001 # restrict type to REG_NONE      (other data types will not return ERROR_SUCCESS)
    RRF_RT_REG_SZ = 0x00000002 # restrict type to REG_SZ        (other data types will not return ERROR_SUCCESS) (automatically converts REG_EXPAND_SZ to REG_SZ unless RRF_NOEXPAND is specified)
    RRF_RT_REG_EXPAND_SZ = 0x00000004 # restrict type to REG_EXPAND_SZ (other data types will not return ERROR_SUCCESS) (must specify RRF_NOEXPAND or RegGetValue will fail with ERROR_INVALID_PARAMETER)
    RRF_RT_REG_BINARY = 0x00000008 # restrict type to REG_BINARY    (other data types will not return ERROR_SUCCESS)
    RRF_RT_REG_DWORD = 0x00000010 # restrict type to REG_DWORD     (other data types will not return ERROR_SUCCESS)
    RRF_RT_REG_MULTI_SZ = 0x00000020 # restrict type to REG_MULTI_SZ  (other data types will not return ERROR_SUCCESS)
    RRF_RT_REG_QWORD = 0x00000040 # restrict type to REG_QWORD     (other data types will not return ERROR_SUCCESS)
    RRF_RT_DWORD = (RRF_RT_REG_BINARY | RRF_RT_REG_DWORD) # restrict type to *32-bit* RRF_RT_REG_BINARY or RRF_RT_REG_DWORD (other data types will not return ERROR_SUCCESS)
    RRF_RT_QWORD = (RRF_RT_REG_BINARY | RRF_RT_REG_QWORD) # restrict type to *64-bit* RRF_RT_REG_BINARY or RRF_RT_REG_DWORD (other data types will not return ERROR_SUCCESS)
    RRF_RT_ANY = 0x0000ffff # no type restriction
    RRF_SUBKEY_WOW6464KEY = 0x00010000 # when opening the subkey (if provided) force open from the 64bit location (only one SUBKEY_WOW64* flag can be set or RegGetValue will fail with ERROR_INVALID_PARAMETER)
    RRF_SUBKEY_WOW6432KEY = 0x00020000 # when opening the subkey (if provided) force open from the 32bit location (only one SUBKEY_WOW64* flag can be set or RegGetValue will fail with ERROR_INVALID_PARAMETER)
    RRF_WOW64_MASK = 0x00030000
    RRF_NOEXPAND = 0x10000000 # do not automatically expand environment strings if value is of type REG_EXPAND_SZ
    RRF_ZEROONFAILURE = 0x20000000 # if pvData is not NULL, set content to all zeros on failure
    #
    # Flags for RegLoadAppKey
    #
    REG_PROCESS_APPKEY = 0x00000001
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_APP | WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Application Family or Desktop Family or OneCore Family or Games Family ***

    #
    # Requested Key access mask type.
    #
    REGSAM = ACCESS_MASK
    #
    # Reserved Key Handles.
    #
    HKEY_CLASSES_ROOT = HKEY(ULONG_PTR(LONG(0x80000000).value).value)
    HKEY_CURRENT_USER = HKEY(ULONG_PTR(LONG(0x80000001).value).value)
    HKEY_LOCAL_MACHINE = HKEY(ULONG_PTR(LONG(0x80000002).value).value)
    HKEY_USERS = HKEY(ULONG_PTR(LONG(0x80000003).value).value)
    HKEY_PERFORMANCE_DATA = HKEY(ULONG_PTR(LONG(0x80000004).value).value)
    HKEY_PERFORMANCE_TEXT = HKEY(ULONG_PTR(LONG(0x80000050).value).value)
    HKEY_PERFORMANCE_NLSTEXT = HKEY(ULONG_PTR(LONG(0x80000060).value).value)
    HKEY_CURRENT_CONFIG = HKEY(ULONG_PTR(LONG(0x80000005).value).value)
    HKEY_DYN_DATA = HKEY(ULONG_PTR(LONG(0x80000006).value).value)
    HKEY_CURRENT_USER_LOCAL_SETTINGS = HKEY(ULONG_PTR(LONG(0x80000007).value).value)

    # REGION ***

    # REGION *** Application Family or Desktop Family or OneCore Family ***

    if cpreproc.pragma_once("_PROVIDER_STRUCTS_DEFINED"):
        PROVIDER_KEEPS_VALUE_LENGTH = 0x1
        class val_context(CStructure):
            _fields_ = [
                ("valuelen", INT),          # the total length of this value
                ("value_context", LPVOID),  # provider's context
                ("val_buff_ptr", LPVOID)    # where in the ouput buffer the value is.
            ]
        PVALCONTEXT = POINTER(val_context)

        class pvalueA(CStructure):        # Provider supplied value/context.
            _fields_ = [
                ("pv_valuename", LPSTR), # The value name pointer
                ("pv_valuelen", INT),
                ("pv_value_context", LPVOID),
                ("pv_type", DWORD)
            ]
        PVALUEA = pvalueA
        PPVALUEA = POINTER(PVALUEA)

        class pvalueW(CStructure):        # Provider supplied value/context.
            _fields_ = [
                ("pv_valuename", LPWSTR), # The value name pointer
                ("pv_valuelen", INT),
                ("pv_value_context", LPVOID),
                ("pv_type", DWORD)
            ]
        PVALUEW = pvalueW
        PPVALUEW = POINTER(PVALUEW)
        PVALUE = unicode(PVALUEW, PVALUEA)
        PPVALUE = unicode(PPVALUEW, PPVALUEA)

        QUERYHANDLER = CDECL(DWORD, LPVOID, PVALCONTEXT, DWORD, LPVOID, LPDWORD, DWORD)
        PQUERYHANDLER = POINTER(QUERYHANDLER)

        class provider_info(CStructure):
            _fields_ = [
                ("pi_R0_1val", PQUERYHANDLER),
                ("pi_R0_allvals", PQUERYHANDLER),
                ("pi_R3_1val", PQUERYHANDLER),
                ("pi_R3_allvals", PQUERYHANDLER),
                ("pi_flags", DWORD), # capability flags (none defined yet).
                ("pi_key_context", LPVOID)
            ]
        REG_PROVIDER = provider_info
        PPROVIDER = POINTER(REG_PROVIDER)

        class value_entA(CStructure):
            _fields_ = [
                ("ve_valuename", LPSTR),
                ("ve_valuelen", DWORD),
                ("ve_valueptr", DWORD_PTR),
                ("ve_type", DWORD)
            ]
        VALENTA = value_entA
        PVALENTA = POINTER(VALENTA)

        class value_entW(CStructure):
            _fields_ = [
                ("ve_valuename", LPWSTR),
                ("ve_valuelen", DWORD),
                ("ve_valueptr", DWORD_PTR),
                ("ve_type", DWORD)
            ]
        VALENTW = value_entW
        PVALENTW = POINTER(VALENTW)
        VALENT = unicode(VALENTW, VALENTA)
        PVALENT = unicode(PVALENTW, PVALENTA)

    # not(_PROVIDER_STRUCTS_DEFINED)

    #
    # Default values for parameters that do not exist in the Win 3.1
    # compatible APIs.
    #

    WIN31_CLASS = NULL

    #  REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    #
    # Flags for RegLoadMUIString
    #
    REG_MUI_STRING_TRUNCATE = 0x00000001

    #
    # RegConnectRegistryEx supported flags
    #
    REG_SECURE_CONNECTION = 1

    # REGION ***

    #
    # API Prototypes.
    #

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegCloseKey = declare(advapi32.RegCloseKey, LSTATUS, HKEY)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegOverridePredefKey = declare(advapi32.RegOverridePredefKey, LSTATUS, HKEY, HKEY)
    RegOpenUserClassesRoot = declare(advapi32.RegOpenUserClassesRoot, LSTATUS, HANDLE, DWORD, REGSAM, PHKEY)
    RegOpenCurrentUser = declare(advapi32.RegOpenCurrentUser, LSTATUS, REGSAM, PHKEY)
    RegDisablePredefinedCache = declare(advapi32.RegDisablePredefinedCache, LSTATUS, VOID)
    RegDisablePredefinedCacheEx = declare(advapi32.RegDisablePredefinedCacheEx, LSTATUS, VOID)
    RegConnectRegistryA = declare(advapi32.RegConnectRegistryA, LSTATUS, LPCSTR, HKEY, PHKEY)
    RegConnectRegistryW = declare(advapi32.RegConnectRegistryW, LSTATUS, LPCWSTR, HKEY, PHKEY)
    RegConnectRegistry = unicode(RegConnectRegistryW, RegConnectRegistryA)
    RegConnectRegistryExA = declare(advapi32.RegConnectRegistryExA, LSTATUS, LPCSTR, HKEY, ULONG, PHKEY)
    RegConnectRegistryExW = declare(advapi32.RegConnectRegistryExW, LSTATUS, LPCWSTR, HKEY, ULONG, PHKEY)
    RegConnectRegistryEx = unicode(RegConnectRegistryExW, RegConnectRegistryExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegCreateKeyA = declare(advapi32.RegCreateKeyA, LSTATUS, HKEY, LPCSTR, PHKEY)
    RegCreateKeyW = declare(advapi32.RegCreateKeyW, LSTATUS, HKEY, LPCWSTR, PHKEY)
    RegCreateKey = unicode(RegCreateKeyW, RegCreateKeyA)
    RegCreateKeyExA = declare(advapi32.RegCreateKeyExA, LSTATUS, HKEY, LPCSTR, DWORD, LPSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD)
    RegCreateKeyExW = declare(advapi32.RegCreateKeyExW, LSTATUS, HKEY, LPCWSTR, DWORD, LPWSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD)
    RegCreateKeyEx = unicode(RegCreateKeyExW, RegCreateKeyExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegCreateKeyTransactedA = declare(advapi32.RegCreateKeyTransactedA, LSTATUS, HKEY, LPCSTR, DWORD, LPSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD, HANDLE, PVOID)
    RegCreateKeyTransactedW = declare(advapi32.RegCreateKeyTransactedW, LSTATUS, HKEY, LPCWSTR, DWORD, LPWSTR, DWORD, REGSAM, LPSECURITY_ATTRIBUTES, PHKEY, LPDWORD, HANDLE, PVOID)
    RegCreateKeyTransacted = unicode(RegCreateKeyTransactedW, RegCreateKeyTransactedA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegDeleteKeyA = declare(advapi32.RegDeleteKeyA, LSTATUS, HKEY, LPCSTR)
    RegDeleteKeyW = declare(advapi32.RegDeleteKeyW, LSTATUS, HKEY, LPCWSTR)
    RegDeleteKey = unicode(RegDeleteKeyW, RegDeleteKeyA)
    RegDeleteKeyExA = declare(advapi32.RegDeleteKeyExA, LSTATUS, HKEY, LPCSTR, REGSAM, DWORD)
    RegDeleteKeyExW = declare(advapi32.RegDeleteKeyExW, LSTATUS, HKEY, LPCWSTR, REGSAM, DWORD)
    RegDeleteKeyEx = unicode(RegDeleteKeyExW, RegDeleteKeyExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegDeleteKeyTransactedA = declare(advapi32.RegDeleteKeyTransactedA, LSTATUS, HKEY, LPCSTR, REGSAM, DWORD, HANDLE, PVOID)
    RegDeleteKeyTransactedW = declare(advapi32.RegDeleteKeyTransactedW, LSTATUS, HKEY, LPCWSTR, REGSAM, DWORD, HANDLE, PVOID)
    RegDeleteKeyTransacted = unicode(RegDeleteKeyTransactedW, RegDeleteKeyTransactedA)
    RegDisableReflectionKey = declare(advapi32.RegDisableReflectionKey, LONG, HKEY)
    RegEnableReflectionKey = declare(advapi32.RegEnableReflectionKey, LONG, HKEY)
    RegQueryReflectionKey = declare(advapi32.RegQueryReflectionKey, LONG, HKEY, PBOOL)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegDeleteValueA = declare(advapi32.RegDeleteValueA, LSTATUS, HKEY, LPCSTR)
    RegDeleteValueW = declare(advapi32.RegDeleteValueW, LSTATUS, HKEY, LPCWSTR)
    RegDeleteValue = unicode(RegDeleteValueW, RegDeleteValueA)
    RegEnumKeyA = declare(advapi32.RegEnumKeyA, LSTATUS, HKEY, DWORD, LPSTR, DWORD)
    RegEnumKeyW = declare(advapi32.RegEnumKeyW, LSTATUS, HKEY, DWORD, LPWSTR, DWORD)
    RegEnumKey = unicode(RegEnumKeyW, RegEnumKeyA)
    RegEnumKeyExA = declare(advapi32.RegEnumKeyExA, LSTATUS, HKEY, DWORD, LPSTR, LPDWORD, LPDWORD, LPSTR, LPDWORD, PFILETIME)
    RegEnumKeyExW = declare(advapi32.RegEnumKeyExW, LSTATUS, HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPWSTR, LPDWORD, PFILETIME)
    RegEnumKeyEx = unicode(RegEnumKeyExW, RegEnumKeyExA)
    RegEnumValueA = declare(advapi32.RegEnumValueA, LSTATUS, HKEY, DWORD, LPSTR, LPDWORD, LPDWORD, LPDWORD, LPBYTE, LPDWORD)
    RegEnumValueW = declare(advapi32.RegEnumValueW, LSTATUS, HKEY, DWORD, LPWSTR, LPDWORD, LPDWORD, LPDWORD, LPBYTE, LPDWORD)
    RegEnumValue = unicode(RegEnumValueW, RegEnumValueA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegFlushKey = declare(advapi32.RegFlushKey, LSTATUS, HKEY)
    RegGetKeySecurity = declare(advapi32.RegGetKeySecurity, LSTATUS, HKEY, SECURITY_INFORMATION, PSECURITY_DESCRIPTOR, LPDWORD)
    RegLoadKeyA = declare(advapi32.RegLoadKeyA, LSTATUS, HKEY, LPCSTR, LPCSTR)
    RegLoadKeyW = declare(advapi32.RegLoadKeyW, LSTATUS, HKEY, LPCWSTR, LPCWSTR)
    RegLoadKey = unicode(RegLoadKeyW, RegLoadKeyA)
    RegNotifyChangeKeyValue = declare(advapi32.RegNotifyChangeKeyValue, LSTATUS, HKEY, BOOL, DWORD, HANDLE, BOOL)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegOpenKeyA = declare(advapi32.RegOpenKeyA, LSTATUS, HKEY, LPCSTR, PHKEY)
    RegOpenKeyW = declare(advapi32.RegOpenKeyW, LSTATUS, HKEY, LPCWSTR, PHKEY)
    RegOpenKey = unicode(RegOpenKeyW, RegOpenKeyA)
    RegOpenKeyExA = declare(advapi32.RegOpenKeyExA, LSTATUS, HKEY, LPCSTR, DWORD, REGSAM, PHKEY)
    RegOpenKeyExW = declare(advapi32.RegOpenKeyExW, LSTATUS, HKEY, LPCWSTR, DWORD, REGSAM, PHKEY)
    RegOpenKeyEx = unicode(RegOpenKeyExW, RegOpenKeyExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegOpenKeyTransactedA = declare(advapi32.RegOpenKeyTransactedA, LSTATUS, HKEY, LPCSTR, DWORD, REGSAM, PHKEY, HANDLE, PVOID)
    RegOpenKeyTransactedW = declare(advapi32.RegOpenKeyTransactedW, LSTATUS, HKEY, LPCWSTR, DWORD, REGSAM, PHKEY, HANDLE, PVOID)
    RegOpenKeyTransacted = unicode(RegOpenKeyTransactedW, RegOpenKeyTransactedA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegQueryInfoKeyA = declare(advapi32.RegQueryInfoKeyA, LSTATUS, HKEY, LPSTR, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, PFILETIME)
    RegQueryInfoKeyW = declare(advapi32.RegQueryInfoKeyW, LSTATUS, HKEY, LPWSTR, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, LPDWORD, PFILETIME)
    RegQueryInfoKey = unicode(RegQueryInfoKeyW, RegQueryInfoKeyA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegQueryValueA = declare(advapi32.RegQueryValueA, LSTATUS, HKEY, LPCSTR, LPSTR, PLONG)
    RegQueryValueW = declare(advapi32.RegQueryValueW, LSTATUS, HKEY, LPCWSTR, LPWSTR, PLONG)
    RegQueryValue = unicode(RegQueryValueW, RegQueryValueA)
    RegQueryMultipleValuesA = declare(advapi32.RegQueryMultipleValuesA, LSTATUS, HKEY, PVALENTA, DWORD, LPSTR, LPDWORD)
    RegQueryMultipleValuesW = declare(advapi32.RegQueryMultipleValuesW, LSTATUS, HKEY, PVALENTW, DWORD, LPWSTR, LPDWORD)
    RegQueryMultipleValues = unicode(RegQueryMultipleValuesW, RegQueryMultipleValuesA)
    # WINVER >= 0x0400
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegQueryValueExA = declare(advapi32.RegQueryValueExA, LSTATUS, HKEY, LPCSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD)
    RegQueryValueExW = declare(advapi32.RegQueryValueExW, LSTATUS, HKEY, LPCWSTR, LPDWORD, LPDWORD, LPBYTE, LPDWORD)
    RegQueryValueEx = unicode(RegQueryValueExW, RegQueryValueExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegReplaceKeyA = declare(advapi32.RegReplaceKeyA, LSTATUS, HKEY, LPCSTR, LPCSTR, LPCSTR)
    RegReplaceKeyW = declare(advapi32.RegReplaceKeyW, LSTATUS, HKEY, LPCWSTR, LPCWSTR, LPCWSTR)
    RegReplaceKey = unicode(RegReplaceKeyW, RegReplaceKeyA)
    RegRestoreKeyA = declare(advapi32.RegRestoreKeyA, LSTATUS, HKEY, LPCSTR, DWORD)
    RegRestoreKeyW = declare(advapi32.RegRestoreKeyW, LSTATUS, HKEY, LPCWSTR, DWORD)
    RegRestoreKey = unicode(RegRestoreKeyW, RegRestoreKeyA)
    RegRenameKey = declare(advapi32.RegRenameKey, LSTATUS, HKEY, LPCWSTR, LPCWSTR)
    RegSaveKeyA = declare(advapi32.RegSaveKeyA, LSTATUS, HKEY, LPCSTR, LPSECURITY_ATTRIBUTES)
    RegSaveKeyW = declare(advapi32.RegSaveKeyW, LSTATUS, HKEY, LPCWSTR, LPSECURITY_ATTRIBUTES)
    RegSaveKey = unicode(RegSaveKeyW, RegSaveKeyA)
    RegSetKeySecurity = declare(advapi32.RegSetKeySecurity, LSTATUS, HKEY, SECURITY_INFORMATION, PSECURITY_DESCRIPTOR)
    RegSetValueA = declare(advapi32.RegSetValueA, LSTATUS, HKEY, LPCSTR, DWORD, LPCSTR, DWORD)
    RegSetValueW = declare(advapi32.RegSetValueW, LSTATUS, HKEY, LPCWSTR, DWORD, LPCWSTR, DWORD)
    RegSetValue = unicode(RegSetValueW, RegSetValueA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family or Games Family ***

    RegSetValueExA = declare(advapi32.RegSetValueExA, LSTATUS, HKEY, LPCSTR, DWORD, DWORD, PBYTE, DWORD)
    RegSetValueExW = declare(advapi32.RegSetValueExW, LSTATUS, HKEY, LPCWSTR, DWORD, DWORD, PBYTE, DWORD)
    RegSetValueEx = unicode(RegSetValueExW, RegSetValueExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM | WINAPI_PARTITION_GAMES)

    # REGION ***

    # REGION *** Desktop Family or OneCore Family ***

    RegUnLoadKeyA = declare(advapi32.RegUnLoadKeyA, LSTATUS, HKEY, LPCSTR)
    RegUnLoadKeyW = declare(advapi32.RegUnLoadKeyW, LSTATUS, HKEY, LPCWSTR)
    RegUnLoadKey = unicode(RegUnLoadKeyW, RegUnLoadKeyA)
    #
    # Utils wrappers
    #
    RegDeleteKeyValueA = declare(advapi32.RegDeleteKeyValueA, LSTATUS, HKEY, LPCSTR, LPCSTR)
    RegDeleteKeyValueW = declare(advapi32.RegDeleteKeyValueW, LSTATUS, HKEY, LPCWSTR, LPCWSTR)
    RegDeleteKeyValue = unicode(RegDeleteKeyValueW, RegDeleteKeyValueA)
    RegSetKeyValueA = declare(advapi32.RegSetKeyValueA, LSTATUS, HKEY, LPCSTR, LPCSTR, DWORD, LPCVOID, DWORD)
    RegSetKeyValueW = declare(advapi32.RegSetKeyValueW, LSTATUS, HKEY, LPCWSTR, LPCWSTR, DWORD, LPCVOID, DWORD)
    RegSetKeyValue = unicode(RegSetKeyValueW, RegSetKeyValueA)
    RegDeleteTreeA = declare(advapi32.RegDeleteTreeA, LSTATUS, HKEY, LPCSTR)
    RegDeleteTreeW = declare(advapi32.RegDeleteTreeW, LSTATUS, HKEY, LPCWSTR)
    RegDeleteTree = unicode(RegDeleteTreeW, RegDeleteTreeA)
    RegCopyTreeA = declare(advapi32.RegCopyTreeA, LSTATUS, HKEY, LPCSTR, HKEY)
    if cpreproc.ifndef("UNICODE"):
            RegCopyTree = RegCopyTreeA
    # _WIN32_WINNT >= 0x0600
    RegGetValueA = declare(advapi32.RegGetValueA, LSTATUS, HKEY, LPCSTR, LPCSTR, DWORD, LPDWORD, PVOID, LPDWORD)
    RegGetValueW = declare(advapi32.RegGetValueW, LSTATUS, HKEY, LPCWSTR, LPCWSTR, DWORD, LPDWORD, PVOID, LPDWORD)
    RegGetValue = unicode(RegGetValueW, RegGetValueA)
    #(_WIN32_WINNT >= 0x0502)
    RegCopyTreeA = declare(advapi32.RegCopyTreeA, LSTATUS, HKEY, LPCSTR, HKEY)
    RegCopyTreeW = declare(advapi32.RegCopyTreeW, LSTATUS, HKEY, LPCWSTR, HKEY)
    RegCopyTree = unicode(RegCopyTreeW, RegCopyTreeA)
    RegLoadMUIStringA = declare(advapi32.RegLoadMUIStringA, LSTATUS, HKEY, LPCSTR, LPSTR, DWORD, LPDWORD, DWORD, LPCSTR)
    RegLoadMUIStringW = declare(advapi32.RegLoadMUIStringW, LSTATUS, HKEY, LPCWSTR, LPWSTR, DWORD, LPDWORD, DWORD, LPCWSTR)
    RegLoadMUIString = unicode(RegLoadMUIStringW, RegLoadMUIStringA)
    RegLoadAppKeyA = declare(advapi32.RegLoadAppKeyA, LSTATUS, LPCSTR, PHKEY, REGSAM, DWORD, DWORD)
    RegLoadAppKeyW = declare(advapi32.RegLoadAppKeyW, LSTATUS, LPCWSTR, PHKEY, REGSAM, DWORD, DWORD)
    RegLoadAppKey = unicode(RegLoadAppKeyW, RegLoadAppKeyA)
    # _WIN32_WINNT >= 0x0600
    #
    # Remoteable System Shutdown APIs
    #
    InitiateSystemShutdownA = declare(advapi32.InitiateSystemShutdownA, BOOL, LPSTR, LPSTR, DWORD, BOOL, BOOL)
    InitiateSystemShutdownW = declare(advapi32.InitiateSystemShutdownW, BOOL, LPWSTR, LPWSTR, DWORD, BOOL, BOOL)
    InitiateSystemShutdown = unicode(InitiateSystemShutdownW, InitiateSystemShutdownA)
    AbortSystemShutdownA = declare(advapi32.AbortSystemShutdownA, BOOL, LPSTR)
    AbortSystemShutdownW = declare(advapi32.AbortSystemShutdownW, BOOL, LPWSTR)
    AbortSystemShutdown = unicode(AbortSystemShutdownW, AbortSystemShutdownA)
    #
    # defines for InitiateSystemShutdownEx reason codes
    #

    from .reason import * # get the public reasons
    
    # Then for Historical reasons support some old symbols, internal only
    REASON_SWINSTALL = (SHTDN_REASON_MAJOR_SOFTWARE|SHTDN_REASON_MINOR_INSTALLATION)
    REASON_HWINSTALL = (SHTDN_REASON_MAJOR_HARDWARE|SHTDN_REASON_MINOR_INSTALLATION)
    REASON_SERVICEHANG = (SHTDN_REASON_MAJOR_SOFTWARE|SHTDN_REASON_MINOR_HUNG)
    REASON_UNSTABLE = (SHTDN_REASON_MAJOR_SYSTEM|SHTDN_REASON_MINOR_UNSTABLE)
    REASON_SWHWRECONF = (SHTDN_REASON_MAJOR_SOFTWARE|SHTDN_REASON_MINOR_RECONFIG)
    REASON_OTHER = (SHTDN_REASON_MAJOR_OTHER|SHTDN_REASON_MINOR_OTHER)
    REASON_UNKNOWN = SHTDN_REASON_UNKNOWN
    REASON_LEGACY_API = SHTDN_REASON_LEGACY_API
    REASON_PLANNED_FLAG = SHTDN_REASON_FLAG_PLANNED
    #
    # MAX Shutdown TimeOut == 10 Years in seconds
    #
    cpreproc.define("MAX_SHUTDOWN_TIMEOUT(10*365*24*60*60)")
    InitiateSystemShutdownExA = declare(advapi32.InitiateSystemShutdownExA, BOOL, LPSTR, LPSTR, DWORD, BOOL, BOOL, DWORD)
    InitiateSystemShutdownExW = declare(advapi32.InitiateSystemShutdownExW, BOOL, LPWSTR, LPWSTR, DWORD, BOOL, BOOL, DWORD)
    InitiateSystemShutdownEx = unicode(InitiateSystemShutdownExW, InitiateSystemShutdownExA)
    #
    # Shutdown flags
    #
    SHUTDOWN_FORCE_OTHERS = 0x00000001
    SHUTDOWN_FORCE_SELF = 0x00000002
    SHUTDOWN_RESTART = 0x00000004
    SHUTDOWN_POWEROFF = 0x00000008
    SHUTDOWN_NOREBOOT = 0x00000010
    SHUTDOWN_GRACE_OVERRIDE = 0x00000020
    SHUTDOWN_INSTALL_UPDATES = 0x00000040
    SHUTDOWN_RESTARTAPPS = 0x00000080
    SHUTDOWN_SKIP_SVC_PRESHUTDOWN = 0x00000100
    SHUTDOWN_HYBRID = 0x00000200
    SHUTDOWN_RESTART_BOOTOPTIONS = 0x00000400
    SHUTDOWN_SOFT_REBOOT = 0x00000800
    SHUTDOWN_MOBILE_UI = 0x00001000
    SHUTDOWN_ARSO = 0x00002000
    InitiateShutdownA = declare(advapi32.InitiateShutdownA, DWORD, LPSTR, LPSTR, DWORD, DWORD, DWORD)
    InitiateShutdownW = declare(advapi32.InitiateShutdownW, DWORD, LPWSTR, LPWSTR, DWORD, DWORD, DWORD)
    InitiateShutdown = unicode(InitiateShutdownW, InitiateShutdownA)
    CheckForHiberboot = declare(advapi32.CheckForHiberboot, DWORD, PBOOLEAN, BOOLEAN)
    RegSaveKeyExA = declare(advapi32.RegSaveKeyExA, LSTATUS, HKEY, LPCSTR, LPSECURITY_ATTRIBUTES, DWORD)
    RegSaveKeyExW = declare(advapi32.RegSaveKeyExW, LSTATUS, HKEY, LPCWSTR, LPSECURITY_ATTRIBUTES, DWORD)
    RegSaveKeyEx = unicode(RegSaveKeyExW, RegSaveKeyExA)
    # WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP | WINAPI_PARTITION_SYSTEM)

    # REGION ***