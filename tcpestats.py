"""++

Copyright (c) 2000-2001  Microsoft Corporation

Module Name:

    tcpestats.w

Abstract:

    This module contains the definitions and structures for TCP extended
    statistics.

Author:

    Xinyan Zan (xinyanz) 30-June-2006

Environment:

    User mode and kernel mode

--"""

from . import cpreproc

if cpreproc.pragma_once("_TCPESTATS_"):
    from .minwindef import *
    
    # REGION *** Desktop Family or OneCore Family or Games Family ***
    
    #
    # Please don't change the order of this enum. The order defined in this
    # enum needs to match the order in EstatsToTcpObjectMappingTable.
    #
    
    TcpConnectionEstatsSynOpts = 0
    TcpConnectionEstatsData = 1
    TcpConnectionEstatsSndCong = 2
    TcpConnectionEstatsPath = 3
    TcpConnectionEstatsSendBuff = 4
    TcpConnectionEstatsRec = 5
    TcpConnectionEstatsObsRec = 6
    TcpConnectionEstatsBandwidth = 7
    TcpConnectionEstatsFineRtt = 8
    TcpConnectionEstatsMaximum = 9
    TCP_ESTATS_TYPE = DWORD
    PTCP_ESTATS_TYPE = PDWORD
    
    #
    # TCP_BOOLEAN_OPTIONAL
    #
    # Define the states that a caller can specify when updating a boolean field.
    #
    
    TcpBoolOptDisabled = 0
    TcpBoolOptEnabled = 1
    TcpBoolOptUnchanged = -1
    TCP_BOOLEAN_OPTIONAL = DWORD
    PTCP_BOOLEAN_OPTIONAL = PDWORD
    
    #
    # TCP_ESTATS_SYN_OPTS_ROS
    #
    # Define extended SYN-exchange information maintained for TCP connections.
    #
    
    class TCP_ESTATS_SYN_OPTS_ROS_v0(CStructure):
        _fields_ = [
            ("ActiveOpen", BOOLEAN),
            ("MssRcvd", ULONG),
            ("MssSent", ULONG)
        ]
        ActiveOpen: int
        MssRcvd: int
        MssSent: int
    PTCP_ESTATS_SYN_OPTS_ROS_v0 = PTR(TCP_ESTATS_SYN_OPTS_ROS_v0)

    #
    # TCP_SOFT_ERROR
    #
    # Enumerate the non-fatal errors recorded on each connection.
    #

    TcpErrorNone = 0
    TcpErrorBelowDataWindow = 1
    TcpErrorAboveDataWindow = 2
    TcpErrorBelowAckWindow = 3
    TcpErrorAboveAckWindow = 4
    TcpErrorBelowTsWindow = 5
    TcpErrorAboveTsWindow = 6
    TcpErrorDataChecksumError = 7
    TcpErrorDataLengthError = 8
    TcpErrorMaxSoftError = 9
    TCP_SOFT_ERROR = DWORD
    PTCP_SOFT_ERROR = PDWORD

    #
    # TCP_ESTATS_DATA_ROD
    #
    # Define extended data-transfer information for TCP connections.
    #

    class TCP_ESTATS_DATA_ROD_v0(CStructure):
        _fields_ = [
            ("DataBytesOut", ULONG64),
            ("DataSegsOut", ULONG64),
            ("DataBytesIn", ULONG64),
            ("DataSegsIn", ULONG64),
            ("SegsOut", ULONG64),
            ("SegsIn", ULONG64),
            ("SoftErrors", ULONG),
            ("SoftErrorReason", ULONG),
            ("SndUna", ULONG),
            ("SndNxt", ULONG),
            ("SndMax", ULONG),
            ("ThruBytesAcked", ULONG64),
            ("RcvNxt", ULONG),
            ("ThruBytesReceived", ULONG64)
        ]
        DataBytesOut: int
        DataSegsOut: int
        DataBytesIn: int
        DataSegsIn: int
        SegsOut: int
        SegsIn: int
        SoftErrors: int
        SoftErrorReason: int
        SndUna: int
        SndNxt: int
        SndMax: int
        ThruBytesAcked: int
        RcvNxt: int
        ThruBytesReceived: int
    PTCP_ESTATS_DATA_ROD_v0 = PTR(TCP_ESTATS_DATA_ROD_v0)

    #
    # TCP_ESTATS_DATA_RW
    #
    # Define structure for enabling extended data-transfer information.
    #

    class TCP_ESTATS_DATA_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_DATA_RW_v0 = PTR(TCP_ESTATS_DATA_RW_v0)

    #
    # TCP_ESTATS_SND_CONG_ROD
    #
    # Define extended sender-congestion information for TCP connections.
    #

    class TCP_ESTATS_SND_CONG_ROD_v0(CStructure):
        _fields_ = [
            ("SndLimTransRwin", ULONG),
            ("SndLimTimeRwin", ULONG),
            ("SndLimBytesRwin", SIZE_T),
            ("SndLimTransCwnd", ULONG),
            ("SndLimTimeCwnd", ULONG),
            ("SndLimBytesCwnd", SIZE_T),
            ("SndLimTransSnd", ULONG),
            ("SndLimTimeSnd", ULONG),
            ("SndLimBytesSnd", SIZE_T),
            ("SlowStart", ULONG),
            ("CongAvoid", ULONG),
            ("OtherReductions", ULONG),
            ("CurCwnd", ULONG),
            ("MaxSsCwnd", ULONG),
            ("CurrSsthresh", ULONG),
            ("MaxSsthresh", ULONG),
            ("MinSsthresh", ULONG)
        ]
        SndLimTransRwin: int
        SndLimTimeRwin: int
        SndLimBytesRwin: int
        SndLimTransCwnd: int
        SndLimTimeCwnd: int
        SndLimBytesCwnd: int
        SndLimTransSnd: int
        SndLimTimeSnd: int
        SndLimBytesSnd: int
        SlowStart: int
        CongAvoid: int
        OtherReductions: int
        CurCwnd: int
        MaxSsCwnd: int
        CurrSsthresh: int
        MaxSsthresh: int
        MinSsthresh: int
    PTCP_ESTATS_SND_CONG_ROD_v0 = PTR(TCP_ESTATS_SND_CONG_ROD_v0)

    #
    # TCP_ESTATS_SND_CONG_ROS
    #
    # Define static extended sender-congestion information for TCP connections.

    class TCP_ESTATS_SND_CONG_ROS_v0(CStructure):
        _fields_ = [
            ("LimCwnd", ULONG)
        ]
        LimCwnd: int
    PTCP_ESTATS_SND_CONG_ROS_v0 = PTR(TCP_ESTATS_SND_CONG_ROS_v0)

    #
    # TCP_ESTATS_SND_CONG_RW
    #
    # Define structure for enabling extended sender-congestion information.
    #

    class TCP_ESTATS_SND_CONG_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_SND_CONG_RW_v0 = PTR(TCP_ESTATS_SND_CONG_RW_v0)

    #
    # TCP_ESTATS_PATH_ROD
    #
    # Define extended path-measurement information for TCP connections.
    #

    class TCP_ESTATS_PATH_ROD_v0(CStructure):
        _fields_ = [
            ("FastRetran", ULONG),
            ("Timeouts", ULONG),
            ("SubsequentTimeouts", ULONG),
            ("CurTimeoutCount", ULONG),
            ("AbruptTimeouts", ULONG),
            ("PktsRetrans", ULONG),
            ("BytesRetrans", ULONG),
            ("DupAcksIn", ULONG),
            ("SacksRcvd", ULONG),
            ("SackBlocksRcvd", ULONG),
            ("CongSignals", ULONG),
            ("PreCongSumCwnd", ULONG),
            ("PreCongSumRtt", ULONG),
            ("PostCongSumRtt", ULONG),
            ("PostCongCountRtt", ULONG),
            ("EcnSignals", ULONG),
            ("EceRcvd", ULONG),
            ("SendStall", ULONG),
            ("QuenchRcvd", ULONG),
            ("RetranThresh", ULONG),
            ("SndDupAckEpisodes", ULONG),
            ("SumBytesReordered", ULONG),
            ("NonRecovDa", ULONG),
            ("NonRecovDaEpisodes", ULONG),
            ("AckAfterFr", ULONG),
            ("DsackDups", ULONG),
            ("SampleRtt", ULONG),
            ("SmoothedRtt", ULONG),
            ("RttVar", ULONG),
            ("MaxRtt", ULONG),
            ("MinRtt", ULONG),
            ("SumRtt", ULONG),
            ("CountRtt", ULONG),
            ("CurRto", ULONG),
            ("MaxRto", ULONG),
            ("MinRto", ULONG),
            ("CurMss", ULONG),
            ("MaxMss", ULONG),
            ("MinMss", ULONG),
            ("SpuriousRtoDetections", ULONG)
        ]
        FastRetran: int
        Timeouts: int
        SubsequentTimeouts: int
        CurTimeoutCount: int
        AbruptTimeouts: int
        PktsRetrans: int
        BytesRetrans: int
        DupAcksIn: int
        SacksRcvd: int
        SackBlocksRcvd: int
        CongSignals: int
        PreCongSumCwnd: int
        PreCongSumRtt: int
        PostCongSumRtt: int
        PostCongCountRtt: int
        EcnSignals: int
        EceRcvd: int
        SendStall: int
        QuenchRcvd: int
        RetranThresh: int
        SndDupAckEpisodes: int
        SumBytesReordered: int
        NonRecovDa: int
        NonRecovDaEpisodes: int
        AckAfterFr: int
        DsackDups: int
        SampleRtt: int
        SmoothedRtt: int
        RttVar: int
        MaxRtt: int
        MinRtt: int
        SumRtt: int
        CountRtt: int
        CurRto: int
        MaxRto: int
        MinRto: int
        CurMss: int
        MaxMss: int
        MinMss: int
        SpuriousRtoDetections: int
    PTCP_ESTATS_PATH_ROD_v0 = PTR(TCP_ESTATS_PATH_ROD_v0)

    #
    # TCP_ESTATS_PATH_ROS
    #
    # Define structure for enabling path-measurement information.
    #

    class TCP_ESTATS_PATH_RW_v0(CStructure):
        _fields_  = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_PATH_RW_v0 = PTR(TCP_ESTATS_PATH_RW_v0)

    #
    # TCP_ESTATS_SEND_BUFF_ROD
    #
    # Define extended output-queuing information for TCP connections.
    #

    class TCP_ESTATS_SEND_BUFF_ROD_v0(CStructure):
        _fields_ = [
            ("CurRetxQueue", SIZE_T),
            ("MaxRetxQueue", SIZE_T),
            ("CurAppWQueue", SIZE_T),
            ("MaxAppWQueue", SIZE_T)
        ]
        CurRetxQueue: int
        MaxRetxQueue: int
        CurAppWQueue: int
        MaxAppWQueue: int
    PTCP_ESTATS_SEND_BUFF_ROD_v0 = PTR(TCP_ESTATS_SEND_BUFF_ROD_v0)

    #
    # TCP_ESTATS_SEND_BUFF_RW
    #
    # Define structure for enabling output-queuing information.
    #

    class TCP_ESTATS_SEND_BUFF_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_SEND_BUFF_RW_v0 = PTR(TCP_ESTATS_SEND_BUFF_RW_v0)

    #
    # TCP_ESTATS_REC_ROD
    #
    # Define extended local-receiver information for TCP connections.
    #

    class TCP_ESTATS_REC_ROD_v0(CStructure):
        _fields_ = [
            ("CurRwinSent", ULONG),
            ("MaxRwinSent", ULONG),
            ("MinRwinSent", ULONG),
            ("LimRwin", ULONG),
            ("DupAckEpisodes", ULONG),
            ("DupAcksOut", ULONG),
            ("CeRcvd", ULONG),
            ("EcnSent", ULONG),
            ("EcnNoncesRcvd", ULONG),
            ("CurReasmQueue", ULONG),
            ("MaxReasmQueue", ULONG),
            ("CurAppRQueue", SIZE_T),
            ("MaxAppRQueue", SIZE_T),
            ("WinScaleSent", BYTE)
        ]
        CurRwinSent: int
        MaxRwinSent: int
        MinRwinSent: int
        LimRwin: int
        DupAckEpisodes: int
        DupAcksOut: int
        CeRcvd: int
        EcnSent: int
        EcnNoncesRcvd: int
        CurReasmQueue: int
        MaxReasmQueue: int
        CurAppRQueue: int
        MaxAppRQueue: int
        WinScaleSent: int
    PTCP_ESTATS_REC_ROD_v0 = PTR(TCP_ESTATS_REC_ROD_v0)

    #
    # TCP_ESTATS_REC_RW
    #
    # Define structure for enabling local-receiver information.
    #

    class TCP_ESTATS_REC_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_REC_RW_v0 = PTR(TCP_ESTATS_REC_RW_v0)

    #
    # TCP_ESTATS_OBS_REC_ROD
    #
    # Define extended remote-receiver information for TCP connections.
    #

    class TCP_ESTATS_OBS_REC_ROD_v0(CStructure):
        _fields_ = [
            ("CurRwinRcvd", ULONG),
            ("MaxRwinRcvd", ULONG),
            ("MinRwinRcvd", ULONG),
            ("WinScaleRcvd", BYTE)
        ]
        CurRwinRcvd: int
        MaxRwinRcvd: int
        MinRwinRcvd: int
        WinScaleRcvd: int
    PTCP_ESTATS_OBS_REC_ROD_v0 = PTR(TCP_ESTATS_OBS_REC_ROD_v0)

    #
    # TCP_ESTATS_OBS_REC_RW
    #
    # Define structure for enabling remote-receiver information.
    #

    class TCP_ESTATS_OBS_REC_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_OBS_REC_RW_v0 = PTR(TCP_ESTATS_OBS_REC_RW_v0)

    #
    # TCP_ESTATS_BW_RW
    #
    # Define the structure for enabling bandwidth estimation for TCP connections.
    #

    class TCP_ESTATS_BANDWIDTH_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollectionOutbound", TCP_BOOLEAN_OPTIONAL),
            ("EnableCollectionInbound", TCP_BOOLEAN_OPTIONAL)
        ]
        EnableCollectionOutbound: TCP_BOOLEAN_OPTIONAL
        EnableCollectionInbound: TCP_BOOLEAN_OPTIONAL
    PTCP_ESTATS_BANDWIDTH_RW_v0 = PTR(TCP_ESTATS_BANDWIDTH_RW_v0)

    #
    # TCP_ESTATS_BW_ROD
    #
    # Define bandwidth estimation statistics for TCP connections.
    #
    # Bandwidth and Instability metrics are expressed as bits per second.
    #

    class TCP_ESTATS_BANDWIDTH_ROD_v0(CStructure):
        _fields_ = [
            ("OutboundBandwidth", ULONG64),
            ("InboundBandwidth", ULONG64),
            ("OutboundInstability", ULONG64),
            ("InboundInstability", ULONG64),
            ("OutboundBandwidthPeaked", BOOLEAN),
            ("InboundBandwidthPeaked", BOOLEAN)
        ]
        OutboundBandwidth: int
        InboundBandwidth: int
        OutboundInstability: int
        InboundInstability: int
        OutboundBandwidthPeaked: int
        InboundBandwidthPeaked: int
    PTCP_ESTATS_BANDWIDTH_ROD_v0 = PTR(TCP_ESTATS_BANDWIDTH_ROD_v0)

    #
    # TCP_ESTATS_FINE_RTT_RW
    #
    # Define the structure for enabling fine-grained RTT estimation for TCP
    # connections.
    #

    class TCP_ESTATS_FINE_RTT_RW_v0(CStructure):
        _fields_ = [
            ("EnableCollection", BOOLEAN)
        ]
        EnableCollection: int
    PTCP_ESTATS_FINE_RTT_RW_v0 = PTR(TCP_ESTATS_FINE_RTT_RW_v0)

    #
    # TCP_ESTATS_FINE_RTT_ROD
    #
    # Define fine-grained RTT estimation statistics for TCP connections.
    #

    class TCP_ESTATS_FINE_RTT_ROD_v0(CStructure):
        _fields_ = [
            ("RttVar", ULONG),
            ("MaxRtt", ULONG),
            ("MinRtt", ULONG),
            ("SumRtt", ULONG)
        ]
        RttVar: int
        MaxRtt: int
        MinRtt: int
        SumRtt: int
    PTCP_ESTATS_FINE_RTT_ROD_v0 = PTR(TCP_ESTATS_FINE_RTT_ROD_v0)
    
    # REGION ***