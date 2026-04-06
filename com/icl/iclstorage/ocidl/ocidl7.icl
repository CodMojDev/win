.icl
.ver 100
.gencommentlw
.inc ../oleidl.icl
.inc ocidl6.icl

// forward-pointer declarations for generator
silent
{
	pie CAUUID LPCAUUID
	pie IStream LPSTREAM
	pie ULARGE_INTEGER PULARGE_INTEGER
	pie CY LPCY
}

al int WPARAM LPARAM

I ISpecifyPropertyPages ex IUnknown
{
	iid B196B28B-BAB4-101A-B69C-00AA00341D07
	cf GetPages pPages P.CAUUID
}

pi LPSPECIFYPROPERTYPAGES

I IPersistMemory ex IPersist
{
	iid BD1AE5E0-A6AE-11CE-BD37-504200C10000
	cf IsDirty
	cf Load pMem LPVOID cbSize ULONG
	cf Save pMem LPVOID fClearDirty BOOL cbSize ULONG
	cf GetSizeMax pCbSize PULONG
	cf InitNew
}

pi LPPERSISTMEMORY

I IPersistStreamInit ex IPersist
{
	iid 7FD52380-4E07-101B-AE2D-08002B2EC713
	cf IsDirty
	cf Load pStm P.IStream
	cf Save pStm P.IStream fClearDirty BOOL
	cf GetSizeMax pCbSize P.ULARGE_INTEGER
	cf InitNew
}

pi LPPERSISTSTREAMINIT

I IPersistPropertyBag ex IPersist
{
	iid 37D84F60-42CB-11CE-8135-00AA004BB851
	cf InitNew
	cf Load pPropBag P.IPropertyBag pErrorLog P.IErrorLog
	cf Save pPropBag P.IPropertyBag fClearDirty BOOL fSaveAllProperties BOOL
}

pi LPPERSISTPROPERTYBAG

I ISimpleFrameSite ex IUnknown
{
	iid 742B0E01-14E6-101B-914E-00AA00300CAB
	cf PreMessageFilter hWnd HWND msg UINT wp WPARAM lp LPARAM plResult P.LRESULT pdwCookie PDWORD
	cf PostMessageFilter hWnd HWND msg UINT wp WPARAM lp LPARAM plResult P.LRESULT dwCookie DWORD
}

pi LPSIMPLEFRAMESITE

~TEXTMETRICOLE = TEXTMETRICW
~LPTEXTMETRICOLE = LPTEXTMETRICW
~

I IFont ex IUnknown
{
	iid BEF6E002-A874-101A-8BBA-00AA00300CAB
	cf get_Name pNmae P.BSTR
	cf put_Name name BSTR
	cf get_Size pSize P.CY
	cf put_Size size CY
	cf get_Bold pBold PBOOL
	cf put_bold bold BOOL
	cf get_Italic pItalic PBOOL
	cf put_Italic italic BOOL
	cf get_Underline pUnderline PBOOL
	cf put_Underline underline BOOL
	cf get_Strikethrough pStrikethrough PBOOL
	cf put_Strikethrough strikethrough BOOL
	cf get_Weight pWeight PSHORT
	cf put_Weight weight SHORT
	cf get_Charset pCharset PSHORT
	cf put_Charset charset SHORT
	cf get_hFont phFont P.HFONT
	cf Clone ppFont FD.P.P.IFont
	cf IsEqual pFontOther FD.P.IFont
	cf SetRatio cyLogical LONG cyHimetric LONG
	cf QueryTextMetrics pTM P.TEXTMETRICOLE
	cf AddRefHfont hFont HFONT
	cf ReleaseHfont hFont HFONT
	cf SetHdc hDC HDC
}

pi LPFONT

~PICTURE_SCALABLE = 0x1
~PICTURE_TRANSPARENT = 0x2
~PICTUREATTRIBUTES = INT
~
~OLE_HANDLE = UINT
~OLE_XPOS_HIMETRIC = LONG
~OLE_YPOS_HIMETRIC = LONG
~OLE_XSIZE_HIMETRIC = LONG
~OLE_YSIZE_HIMETRIC = LONG
~

I IPicture ex IUnknown
{
	iid 7BF80980-BF32-101A-8BBB-00AA00300CAB
	cf get_Handle pHandle P.OLE_HANDLE
	cf get_hPal phPal P.OLE_HANDLE
	cf get_Type pType PSHORT
	cf get_Width pWidth P.OLE_XSIZE_HIMETRIC
	cf get_Height pHeight P.OLE_YSIZE_HIMETRIC
	cf Render hDC HDC x LONG y LONG cx LONG cy LONG xSrc OLE_XPOS_HIMETRIC ySrc OLE_YPOS_HIMETRIC cxSrc OLE_XSIZE_HIMETRIC cySrc OLE_YSIZE_HIMETRIC pRcWBounds LPCRECT
	cf set_hPal hPal OLE_HANDLE
	cf get_CurDC phDC P.HDC
	cf SelectPicture hDCIn HDC phDCOut P.HDC phBmpOut P.OLE_HANDLE
	cf get_KeepOriginalFormat pKeep PBOOL
	cf put_KeepOriginalFormat keep BOOL
	cf PictureChanged
	cf SaveAsFile pStream P.IStream fSaveMemCopy BOOL pCbSize PLONG
	cf get_Attributes pDwAttr PDWORD
}

pi LPPICTURE

~HHANDLE = UINT_PTR
~

I IPicture2 ex IPicture
{
	iid F5185DD8-2012-4b0b-AAD9-F052C6BD482B
}

pi LPPICTURE2

I IFontEventsDisp ex IDispatch
{
	iid 4EF6100A-AF88-11D0-9846-00C04FC29993
}

pi LPFONTEVENTS

I IFontDisp ex IDispatch
{
	iid BEF6E003-A874-101A-8BBA-00AA00300CAB
}

pi LPFONTDISP

I IPictureDisp ex IDispatch
{
	iid 7BF80981-BF32-101A-8BBB-00AA00300CAB
}

pi LPPICTUREDISP

I IOleInPlaceObjectWindowless ex IOleInPlaceObject
{
	iid 1C2056CC-5EF4-101B-8BC8-00AA003E3B29
	cf OnWindowMessage msg UINT wParam WPARAM lParam LPARAM plResult P.LRESULT
	cf GetDropTarget ppDropTarget P.P.IDropTarget
}

pi LPOLEINPLACEOBJECTWINDOWLESS

~ACTIVATE_WINDOWLESS = 1
~ACTIVATEFLAGS = INT
~

I IOleInPlaceSiteEx ex IOleInPlaceSite
{
	iid 9C2CAD80-3424-11CF-B670-00AA004CD6D8
	cf OnInPlaceActivateEx pfNoRedraw PBOOL dwFlags DWORD
	cf OnInPlaceDeactivateEx fNoRedraw BOOL
	cf RequestUIActivate
}

pi LPOLEINPLACESITEEX

~OLEDC_NODRAW = 0x1
~OLEDC_PAINTBKGND = 0x2
~OLEDC_OFFSCREEN = 0x4
~OLEDCFLAGS = INT
~

I IOleInPlaceSiteWindowless ex IOleInPlaceSiteEx
{
	iid 922EADA0-3424-11CF-B670-00AA004CD6D8
	cf CanWindowlessActivate
	cf GetCapture
	cf SetCapture fCapture BOOL
	cf GetFocus
	cf SetFocus fFocus BOOL
	cf GetDC pRect LPCRECT grfFlags DWORD phDC P.HDC
	cf ReleaseDC hDC HDC
	cf InvalidateRect pRect LPCRECT fErase BOOL
	cf InvalidateRgn hRGN HRGN fErase BOOL
	cf ScrollRect dx INT dy INT pRectScroll LPCRECT pRectClip LPCRECT
	cf AdjustRect prc LPRECT
	cf OnDefWindowMessage msg UINT wParam WPARAM lParam LPARAM plResult P.LRESULT
}

pi LPOLEINPLACESITEWINDOWLESS