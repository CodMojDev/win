"""
    This module defines the prototypes and constants required for the image
    help routines.

    Contains debugging support routines that are redistributable.
"""

from ..winnt import *

if cpreproc.pragma_once('_DBGHELP_'):
    DbgHelp = get_win_library('DbgHelp.dll')
    
    IMAGE_SEPARATION = (64*1024)
    
    # Observant readers may notice that 2 new fields,
    # 'fReadOnly' and 'Version' have been added to
    # the LOADED_IMAGE structure after 'fDOSImage'.
    # This does not change the size of the structure
    # from previous headers.  That is because while
    # 'fDOSImage' is a byte, it is padded by the
    # compiler to 4 bytes.  So the 2 new fields are
    # slipped into the extra space.

    @CStructure.make
    class LOADED_IMAGE(CStructure):
        ModuleName: PSTR
        hFile: IHandle
        MappedAddress: PUCHAR
        
        if cpreproc.ifdef('_WIN64'):
            FileHeader: IPointer[IMAGE_NT_HEADERS64]
        else:
            FileHeader: IPointer[IMAGE_NT_HEADERS32]
            
        LastRvaSection: IPointer[IMAGE_SECTION_HEADER]
        NumberOfSections: int
        Sections: IPointer[IMAGE_SECTION_HEADER]
        Characteristics: int
        fSystemImage: IBool
        fDOSImage: IBool
        fReadOnly: IBool
        Version: IInt8
        Links: LIST_ENTRY
        SizeOfImage: int
        
    PLOADED_IMAGE = LOADED_IMAGE.PTR()
    
    # Error codes set by dbghelp functions.  Call GetLastError
    # to see them.
    # Dbghelp also sets error codes found in winerror.h

    ERROR_IMAGE_NOT_STRIPPED    = 0x8800  # the image is not stripped.  No dbg file available.
    ERROR_NO_DBG_POINTER        = 0x8801  # image is stripped but there is no pointer to a dbg file
    ERROR_NO_PDB_POINTER        = 0x8802  # image does not point to a pdb file
    
    PFIND_DEBUG_FILE_CALLBACK = WINAPI(BOOL, HANDLE, PCSTR, PVOID)
    
    @DbgHelp.foreign(HANDLE, HANDLE, PCSTR, PSTR, PFIND_DEBUG_FILE_CALLBACK, PVOID)
    def SymFindDebugInfoFile(
        hProcess: HANDLE,
        FileName: PCSTR,
        DebugFilePath: PSTR,
        Callback: FARPROC,
        CallerData: PVOID) -> WT_HANDLE: ...