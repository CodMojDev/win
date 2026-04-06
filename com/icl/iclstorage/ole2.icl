.icl
.ver 100

cf ge s

// forward-pointer declarations for generator
silent
{
	pie IStorage LPSTORAGE
}

//.inc ocidl/ocidl11.icl

.commentext Contents: Main OLE2 header; Defines Linking and Emmebbeding interfaces, and API's.
.gencomment

al int CLIPFORMAT

ff ole32.OleBuildVersion DWORD
oleff WriteFmtUserTypeStg pstg P.IStorage cf CLIPFORMAT lpszUserType LPOLESTR
oleff ReadFmtUserTypeStg pstg P.IStorage pcf P.CLIPFORMAT lplpszUserType P.LPOLESTR
oleff OleInitialize pvReserved LPVOID
ff ole32.OleUninitialize VOID