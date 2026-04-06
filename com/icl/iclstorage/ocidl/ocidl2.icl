.icl
.ver 100
.gencommentlw
.inc ocidl1.icl

I IProvideMultipleClassInfo ex IProvideClassInfo2
{
	iid A7ABA9C1-8983-11cf-8F20-00805F2CD064
	cf GetMultiTypeInfoCount pcti PULONG
	cf GetInfoOfIndex iti ULONG dwFlags DWORD pptiCoClass P.P.ITypeInfo pdwTIFlags PDWORD pcdispidReserved PULONG piidPrimary P.IID piidSource P.IID
}

pi LPPROVIDEMULTIPLECLASSINFO