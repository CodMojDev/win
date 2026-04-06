.icl
.ver 100

.gencomment
.commentext TLB2ICL Generator
.commentext Generated from TLB: C:\Windows\System32\stdole2.tlb

ed OLE_TRISTATE
{
    ee Unchecked 0
    ee Checked 1
    ee Gray 2
}

ed LoadPictureConstants
{
    ee Default 0
    ee Monochrome 1
    ee VgaColor 2
    ee Color 4
}

I IUnknown
{
    iid {00000000-0000-0000-C000-000000000046}
    cf QueryInterface riid PVOID ppvObj PVOID
    cf AddRef DWORD 
    cf Release DWORD 
}

IU IDispatch
{
    iid {00020400-0000-0000-C000-000000000046}
    cf GetTypeInfoCount pctinfo PVOID
    cf GetTypeInfo itinfo UINT lcid DWORD pptinfo PVOID
    cf GetIDsOfNames riid PVOID rgszNames PVOID cNames UINT lcid DWORD rgdispid PVOID
    cf Invoke dispidMember LONG riid PVOID lcid DWORD wFlags WORD pdispparams PVOID pvarResult PVOID pexcepinfo PVOID puArgErr PVOID
}

IU IEnumVARIANT
{
    iid {00020404-0000-0000-C000-000000000046}
    cf Next celt DWORD rgvar PVOID pceltFetched PVOID
    cf Skip celt DWORD
    cf Reset 
    cf Clone ppenum PVOID
}

IU IFont
{
    iid {BEF6E002-A874-101A-8BBA-00AA00300CAB}
    cf Name pname PVOID
    cf Name pname BSTR
    cf Size psize PVOID
    cf Size psize CY
    cf Bold pbold PVOID
    cf Bold pbold BOOL
    cf Italic pitalic PVOID
    cf Italic pitalic BOOL
    cf Underline punderline PVOID
    cf Underline punderline BOOL
    cf Strikethrough pstrikethrough PVOID
    cf Strikethrough pstrikethrough BOOL
    cf Weight pweight PVOID
    cf Weight pweight SHORT
    cf Charset pcharset PVOID
    cf Charset pcharset SHORT
    cf hFont phfont PVOID
    cf Clone ppfont PVOID
    cf IsEqual pfontOther PVOID
    cf SetRatio cyLogical LONG cyHimetric LONG
    cf AddRefHfont hFont GECLO
    cf ReleaseHfont hFont GECLO
}

IU IPicture
{
    iid {7BF80980-BF32-101A-8BBB-00AA00300CAB}
    cf Handle phandle PVOID
    cf hPal phpal PVOID
    cf Type ptype PVOID
    cf Width pwidth PVOID
    cf Height pheight PVOID
    cf Render hdc INT x LONG y LONG cx LONG cy LONG xSrc GECLO ySrc GECLO cxSrc GECLO cySrc GECLO prcWBounds PVOID
    cf hPal phpal GECLO
    cf CurDC phdcOut PVOID
    cf SelectPicture hdcIn INT phdcOut PVOID phbmpOut PVOID
    cf KeepOriginalFormat pfkeep PVOID
    cf KeepOriginalFormat pfkeep BOOL
    cf PictureChanged 
    cf SaveAsFile pstm PVOID fSaveMemCopy BOOL pcbSize PVOID
    cf Attributes pdwAttr PVOID
    cf SetHdc hdc GECLO
}

