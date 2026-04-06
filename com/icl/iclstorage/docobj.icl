.icl
.ver 100

//
// OLE Document Object interfaces
//

.commentext Contents: OLE Document Object interfaces
.gencomment

.inc oleidl.icl

imports
{
	import .ctlinterfacedef
}

ed DOCMISC
{
	ee DOCMISC_CANCREATEMULTIPLEVIEWS 1
	ee DOCMISC_SUPPORTCOMPLEXRECTANGLES 2
	ee DOCMISC_CANTOPENEDIT 4   // fails the IOleDocumentView::Open  method
	ee DOCMISC_NOFILESUPPORT 8  // does not support read/writing to a file
}

IU IOleDocumentView
{
	iid b722bcc6-4e68-101b-a2bc-00aa00404770
	cf SetInPlaceSite pIPSite P.IOleInPlaceSite
	cf GetInPlaceSite ppIPSite P.P.IOleInPlaceSite
	cf GetDocument ppunk P.P.IUnknown
	cf SetRect prcView P.RECT
	cf GetRect prcView P.RECT
	cf SetRectComplex prcView P.RECT prcHScroll P.RECT prcVScroll P.RECT prcSizeBox P.RECT
	cf Show fShow BOOL
	cf UIActivate fUIActivate BOOL
	cf Open
	cf CloseView dwReserved DWORD
	cf SaveViewState pstm P.IStream
	cf ApplyViewState pstm P.IStream
	cf Clone pIPSiteNew P.IOleInPlaceSite ppViewNew FD.P.P.IOleDocumentView
}

pi LPOLEDOCUMENTVIEW

IU IEnumOleDocumentViews
{
	iid b722bcc8-4e68-101b-a2bc-00aa00404770
	cf Next cViews ULONG rgpView P.P.IOleDocumentView pcFetched PULONG
	cf Skip cViews ULONG
	cf Reset
	cf Clone ppEnum FD.P.P.IEnumOleDocumentViews
}

pi LPENUMOLEDOCUMENTVIEWS

IU IOleDocument
{
	iid b722bcc5-4e68-101b-a2bc-00aa00404770
	cf CreateView pIPSite P.IOleInPlaceSite pstm P.IStream dwReserved DWORD ppView P.P.IOleDocumentView
	cf GetDocMiscStatus pdwStatus PDWORD
	cf EnumViews ppEnum P.P.IEnumOleDocumentViews ppView P.P.IOleDocumentView
}

pi LPOLEDOCUMENT

IU IOleDocumentSite
{
	iid b722bcc7-4e68-101b-a2bc-00aa00404770
	cf ActivateMe pViewToActivate P.IOleDocumentView
}

pi LPOLEDOCUMENTSITE

IU IContinueCallback
{
	iid b722bcca-4e68-101b-a2bc-00aa00404770
	cf FContinue
	cf FContinuePrinting nCntPrinted LONG nCurPage LONG pwszPrintStatus LPWSTR
}

pi LPCONTINUECALLBACK

ed PRINTFLAG
{
	PRINTFLAG_MAYBOTHERUSER 1
	PRINTFLAG_PROMPTUSER 2
	PRINTFLAG_USERMAYCHANGEPRINTER 4
	PRINTFLAG_RECOMPOSETODEVICE 8
	PRINTFLAG_DONTACTUALLYPRINT 16
	PRINTFLAG_FORCEPROPERTIES 32
	PRINTFLAG_PRINTTOFILE 64
}

sd PAGERANGE
{
	sf ILong nFromPage
	sf ILong nToPage
}

sd PAGESET
{
	sf IUlong cbStruct
	sf IBool64 fOddPages
	sf IBool64 fEventPages
	sf IUlong cPageRange
	sf IArray[PAGERANGE]
}

eq PAGESET_TOLASTPAGE WORD(-1).value

IU IPrint
{
	iid b722bcc9-4e68-101b-a2bc-00aa00404770
	cf SetInitialPageNum nFirstPage LONG
	cf GetPageInfo pnFirstPage PLONG pcPages PLONG
	cf Print grfFlags DWORD pptd P.P.DVTARGETDEVICE ppPageSet P.P.PAGESET pstgmOptions P.STGMEDIUM pcallback P.IContinueCallback nFirstPage LONG pcPagesPrinted PLONG pnLastPage PLONG
}

pi LPPRINT

