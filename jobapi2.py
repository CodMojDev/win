"""
/********************************************************************************
*                                                                               *
* jobapiset2.h -- ApiSet Contract for api-ms-win-core-job-l2                    *
*                                                                               *
* Copyright (c) Microsoft Corporation. All rights reserved.                     *
*                                                                               *
********************************************************************************/
"""
from . import cpreproc

if cpreproc.pragma_once("_JOBAPISET2_H_"):
    from .winnt import *
    
    kernel32 = get_win_library('kernel32.dll')
    
    # REGION *** Desktop Family or OneCore Family ***
    
    class JOBOBJECT_IO_RATE_CONTROL_INFORMATION(CStructure):
        _fields_ = [
            ("MaxIops", ULONG64),
            ("MaxBandwidth", LONG64),
            ("ReservationIops", LONG64),
            ("VolumeName", LPCWSTR),
            ("BaseIoSize", ULONG),
            ("ControlFlags", ULONG)
        ]
        MaxIops: int
        MaxBandwidth: int
        ReservationIops: int
        VolumeName: LPCWSTR
        BaseIoSize: int
        ControlFlags: int
    
    # TODO: migrate JOBOBJECTINFOCLASS to winnt.py
    JobObjectBasicAccountingInformation = 1
    JobObjectBasicLimitInformation = 2
    JobObjectBasicUIRestrictions = 3
    JobObjectSecurityLimitInformation = 4
    JobObjectAssociateCompletionPortInformation = 5
    JobObjectBasicAndIoAccountingInformation = 6
    JobObjectExtendedLimitInformation = 7
    JobObjectJobSetInformation = 8
    JobObjectGroupInformation = 9
    JobObjectNotificationLimitInformation = 10
    JobObjectLimitViolationInformation = 11
    JobObjectGroupInformationEx = 12
    JobObjectCpuRateControlInformation = 13
    JobObjectCompletionFilterInformation = 14
    JobObjectThreadContainerInformation = 15
    JobObjectReserved1Information = 16
    JobObjectReserved2Information = 17
    JobObjectReserved3Information = 18
    JobObjectReserved4Information = 19
    JobObjectReserved5Information = 20
    JobObjectReserved6Information = 21
    JobObjectReserved7Information = 22
    JobObjectReserved8Information = 23
    JobObjectReserved9Information = 24
    MaxJobObjectInfoClass = 25
    JOBOBJECTINFOCLASS = DWORD
    
    CreateJobObjectW = declare(kernel32.CreateJobObjectW, HANDLE, LPSECURITY_ATTRIBUTES, LPCWSTR)
    FreeMemoryJobObject = declare(kernel32.FreeMemoryJobObject, VOID, PVOID)
    OpenJobObjectW = declare(kernel32.OpenJobObjectW, HANDLE, DWORD, BOOL, LPCWSTR)
    AssignProcessToJobObject = declare(kernel32.AssignProcessToJobObject, BOOL, HANDLE, HANDLE)
    TerminateJobObject = declare(kernel32.TerminateJobObject, BOOL, HANDLE, UINT)
    SetInformationJobObject = declare(kernel32.SetInformationJobObject, HANDLE, JOBOBJECTINFOCLASS, LPVOID, DWORD)
    QueryInformationJobObject = declare(kernel32.QueryInformationJobObject, BOOL, HANDLE, JOBOBJECTINFOCLASS, LPVOID, DWORD, LPDWORD)
    QueryIoRateControlInformationJobObject = declare(kernel32.QueryIoRateControlInformationJobObject, DWORD, HANDLE, LPCWSTR, DOUBLE_PTR(JOBOBJECT_IO_RATE_CONTROL_INFORMATION), PULONG)
    
    # REGION ***
    
# _JOBAPISET2_H_