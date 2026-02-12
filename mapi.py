"""
/*
 *	M A P I . H
 *
 *  Messaging Applications Programming Interface.
 *
 *  Copyright 1993-1999 Microsoft Corporation. All Rights Reserved.
 *
 *  Purpose:
 *
 *    This file defines the structures and constants used by that
 *    subset of the Messaging Applications Programming Interface
 *    which is supported under Windows by Microsoft Mail for PC
 *    Networks version 3.x.
 */
 
"""

from . import cpreproc

from .minwindef import *

from .winnt import PWSTR

from .defbase import *

if cpreproc.pragma_once("MAPI_H"):
    # REGION *** Desktop Family ***

    mapi32 = WinDLL('mapi32.dll')

    #
    #  Types.
    #

    LPULONG = PULONG
    FLAGS = ULONG
    if cpreproc.pragma_once("__LHANDLE"):
        LHANDLE = ULONG_PTR
        LPLHANDLE = PULONG_PTR

    lhSessionNull = 0

    class MapiFileDesc(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),            # Reserved for future use (must be 0)     
            ("flFlags", ULONG),               # Flags                                   
            ("nPosition", ULONG),             # character in text to be replaced by attachment 
            ("lpszPathName", LPSTR),          # Full path name of attachment file       
            ("lpszFileName", LPSTR),          # Original file name (optional)           
            ("lpFileType", LPVOID)            # Attachment file type (can be lpMapiFileTagExt) 
        ]
    lpMapiFileDesc = POINTER(MapiFileDesc)

    class MapiFileDescW(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),
            ("flFlags", ULONG),
            ("nPosition", ULONG),
            ("lpszPathName", PWSTR),
            ("lpszFileName", PWSTR),
            ("lpFileType", PVOID)
        ]
    lpMapiFileDescW = POINTER(MapiFileDescW)


    MAPI_OLE                = 0x00000001
    MAPI_OLE_STATIC         = 0x00000002


    class MapiFileTagExt(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),           # Reserved, must be zero.                  
            ("cbTag", ULONG),                # Size (in bytes) of                       
            ("lpTag", LPBYTE),               # X.400 OID for this attachment type       
            ("cbEncoding", ULONG),           # Size (in bytes) of                       
            ("lpEncoding", LPBYTE)           # X.400 OID for this attachment's encoding 
        ]
    lpMapiFileTagExt = POINTER(MapiFileTagExt)

    class MapiRecipDesc(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),           # Reserved for future use                  
            ("ulRecipClass", ULONG),         # Recipient class                          
                                             # MAPI_TO, MAPI_CC, MAPI_BCC, MAPI_ORIG    
            ("lpszName", LPSTR),             # Recipient name                           
            ("lpszAddress", LPSTR),          # Recipient address (optional)             
            ("ulEIDSize", ULONG),            # Count in bytes of size of pEntryID       
            ("lpEntryID", LPVOID)            # System-specific recipient reference      
        ]
    lpMapiRecipDesc = POINTER(MapiRecipDesc)

    class MapiRecipDescW(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),           # Reserved for future use                  
            ("ulRecipClass", ULONG),         # Recipient class                          
                                             # MAPI_TO, MAPI_CC, MAPI_BCC, MAPI_ORIG    
            ("lpszName", LPWSTR),            # Recipient name                           
            ("lpszAddress", LPWSTR),         # Recipient address (optional)             
            ("ulEIDSize", ULONG),            # Count in bytes of size of pEntryID       
            ("lpEntryID", LPVOID)            # System-specific recipient reference      
        ]
    lpMapiRecipDescW = POINTER(MapiRecipDescW)

    if cpreproc.ifndef("MAPI_ORIG"):
        MAPI_ORIG  = 0           # Recipient is message originator          
        MAPI_TO    = 1           # Recipient is a primary recipient         
        MAPI_CC    = 2           # Recipient is a copy recipient            
        MAPI_BCC   = 3           # Recipient is blind copy recipient        

    class MapiMessage(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),             # Reserved for future use (M.B. 0)       
            ("lpszSubject", LPSTR),            # Message Subject      
            ("lpszNoteText", LPSTR),           # Message Text                      
            ("lpszMessageType", LPSTR),        # Message Class                          
            ("lpszDateReceived", LPSTR),       # in YYYY/MM/DD HH:MM format             
            ("lpszConversationID", LPSTR),     # conversation thread ID                 
            ("flFlags", FLAGS),                # unread,return receipt                  
            ("lpOriginator", lpMapiRecipDesc), # Originator descriptor     
            ("nRecipCount", ULONG),            # Number of recipients                   
            ("lpRecips", lpMapiRecipDesc),     # Recipient descriptors                  
            ("nFileCount", ULONG),             # of file attachments                  
            ("lpFiles", lpMapiFileDesc)        # Attachment descriptors                 
        ]
    lpMapiMessage = POINTER(MapiMessage)

    class MapiMessageW(CStructure):
        _fields_ = [
            ("ulReserved", ULONG),             # Reserved for future use (M.B. 0)       
            ("lpszSubject", LPWSTR),            # Message Subject      
            ("lpszNoteText", LPWSTR),           # Message Text                      
            ("lpszMessageType", LPWSTR),        # Message Class                          
            ("lpszDateReceived", LPWSTR),       # in YYYY/MM/DD HH:MM format             
            ("lpszConversationID", LPWSTR),     # conversation thread ID                 
            ("flFlags", FLAGS),                # unread,return receipt                  
            ("lpOriginator", lpMapiRecipDescW), # Originator descriptor     
            ("nRecipCount", ULONG),            # Number of recipients                   
            ("lpRecips", lpMapiRecipDescW),     # Recipient descriptors                  
            ("nFileCount", ULONG),             # of file attachments                  
            ("lpFiles", lpMapiFileDescW)        # Attachment descriptors                 
        ]
    lpMapiMessageW = POINTER(MapiMessage)

    MAPI_UNREAD             = 0x00000001
    MAPI_RECEIPT_REQUESTED  = 0x00000002
    MAPI_SENT               = 0x00000004


    """
    *  Entry points.
    """
    

    """
    *  flFlags values for Simple MAPI entry points. All documented flags are
    *  shown for each call. Duplicates are commented out but remain present
    *  for every call.
    """
    

    # MAPILogon() flags.       

    MAPI_LOGON_UI          = 0x00000001  # Display logon UI       
    if cpreproc.ifndef("MAPI_PASSWORD_UI"):      
        MAPI_PASSWORD_UI	   = 0x00020000	 # prompt for password only     
    MAPI_NEW_SESSION       = 0x00000002  # Don't use shared session     
    MAPI_FORCE_DOWNLOAD    = 0x00001000  # Get new mail before return   
    MAPI_EXTENDED          = 0x00000020  # Extended MAPI Logon          

    # MAPISendMail() flags.    

    MAPI_LOGON_UI       = 0x00000001     # Display logon UI             
    MAPI_NEW_SESSION    = 0x00000002     # Don't use shared session     

    if cpreproc.ifndef("MAPI_DIALOG"):				# also defined in property.h 
        MAPI_DIALOG            = 0x00000008  # Display a send note UI       
    MAPI_USE_DEFAULT	       = 0x00000040	 # Use default profile in logon 

    # MAPISendMailW() flags.    

    MAPI_DIALOG_MODELESS   = 0x00000004 | MAPI_DIALOG  # Display a modeless window    
    MAPI_FORCE_UNICODE     = 0x00040000  # Don't down-convert to ANSI if provider does not support Unicode 

    # MAPIFindNext() flags.    

    MAPI_UNREAD_ONLY       = 0x00000020  # Only unread messages         
    MAPI_GUARANTEE_FIFO    = 0x00000100  # use date order               
    MAPI_LONG_MSGID		   = 0x00004000	 # allow 512 char returned = ID	

    # MAPIReadMail() flags.    

    MAPI_PEEK              = 0x00000080  # Do not mark as read.         
    MAPI_SUPPRESS_ATTACH   = 0x00000800  # header + body, no files      
    MAPI_ENVELOPE_ONLY     = 0x00000040  # Only header information      
    MAPI_BODY_AS_FILE      = 0x00000200

    # MAPISaveMail() flags.    

    MAPI_LONG_MSGID		= 0x00004000    # allow 512 char returned = ID	

    # MAPIAddress() flags.     

    # MAPIDetails() flags.     

    MAPI_AB_NOMODIFY       = 0x00000400  # Don't allow mods of AB entries

    # MAPIResolveName() flags. 
     
    MAPI_DIALOG         = 0x00000008    # Prompt for choices if ambiguous 
    MAPI_AB_NOMODIFY    = 0x00000400    # Don't allow mods of AB entries 

    MAPILOGON = WINAPI(ULONG, ULONG_PTR, LPSTR, LPSTR, FLAGS, ULONG, LPLHANDLE)
    LPMAPILOGON = POINTER(MAPILOGON)
    MAPILogon = MAPILOGON.in_dll(mapi32, 'MAPILogon')

    MAPILOGOFF = WINAPI(ULONG, LHANDLE, ULONG_PTR, FLAGS, ULONG)
    LPMAPILOGOFF = POINTER(MAPILOGOFF)
    MAPILogoff = MAPILOGOFF.in_dll(mapi32, 'MAPILogoff')

    MAPISENDMAIL = WINAPI(ULONG, LHANDLE, ULONG_PTR, lpMapiMessage, FLAGS, ULONG)
    LPMAPISENDMAIL = POINTER(MAPISENDMAIL)
    MAPISendMail = MAPISENDMAIL.in_dll(mapi32, 'MAPISendMail')

    MAPISENDMAILW = WINAPI(ULONG, ULONG_PTR, lpMapiMessageW, FLAGS, ULONG)
    LPMAPISENDMAILW = POINTER(MAPISENDMAILW)
    MAPISendMailW = MAPISENDMAILW.in_dll(mapi32, 'MAPISendMailW')

    MAPISENDDOCUMENTS = WINAPI(ULONG, ULONG_PTR, LPSTR, LPSTR, LPSTR, ULONG)
    LPMAPISENDDOCUMENTS = POINTER(MAPISENDDOCUMENTS)
    MAPISendDocuments = MAPISENDDOCUMENTS.in_dll(mapi32, 'MAPISendDocuments')

    MAPIFINDNEXT = WINAPI(ULONG, LHANDLE, ULONG_PTR, LPSTR, LPSTR, FLAGS, ULONG, LPSTR)
    LPMAPIFINDNEXT = POINTER(MAPIFINDNEXT)
    MAPIFindNext = MAPIFINDNEXT.in_dll(mapi32, 'MAPIFindNext')

    MAPIREADMAIL = WINAPI(ULONG, LHANDLE, ULONG_PTR, LPSTR, FLAGS, ULONG, POINTER(lpMapiMessage))
    LPMAPIREADMAIL = POINTER(MAPISENDMAIL)
    MAPIReadMail = MAPISENDMAIL.in_dll(mapi32, 'MAPIReadMail')

    MAPISAVEMAIL = WINAPI(ULONG, LHANDLE, ULONG_PTR, lpMapiMessage, FLAGS, ULONG, LPSTR)
    LPMAPISAVEMAIL = POINTER(MAPISAVEMAIL)
    MAPISaveMail = MAPISAVEMAIL.in_dll(mapi32, 'MAPISaveMail')

    MAPIDELETEMAIL = WINAPI(ULONG, LHANDLE, ULONG_PTR, LPSTR, FLAGS, ULONG)
    LPMAPIDELETEMAIL = POINTER(MAPIDELETEMAIL)
    MAPIDeleteMail = MAPIDELETEMAIL.in_dll(mapi32, 'MAPIDeleteMail')

    LPMAPIFREEBUFFER = WINAPI(ULONG, LPVOID)
    MAPIFreeBuffer = LPMAPIFREEBUFFER.in_dll(mapi32, 'MAPIFreeBuffer')

    MAPIADDRESS = WINAPI(ULONG, LHANDLE, ULONG_PTR, LPSTR, ULONG, LPSTR, ULONG, lpMapiRecipDesc, FLAGS, ULONG, LPULONG, lpMapiRecipDesc)
    LPMAPIADDRESS = POINTER(MAPIADDRESS)
    MAPIAddress = MAPIADDRESS.in_dll(mapi32, 'MAPIAddress')

    MAPIDETAILS = WINAPI(ULONG, LHANDLE, ULONG_PTR, lpMapiRecipDesc, FLAGS, ULONG)
    LPMAPIDETAILS = POINTER(MAPIDETAILS)
    MAPIDetails = MAPIDETAILS.in_dll(mapi32, 'MAPIDetails')

    MAPIRESOLVENAME = WINAPI(ULONG, LHANDLE, ULONG_PTR, LPSTR, FLAGS, ULONG, lpMapiRecipDesc)
    LPMAPIRESOLVENAME = POINTER(MAPIRESOLVENAME)
    MAPIResolveName = MAPIRESOLVENAME.in_dll(mapi32, 'MAPIResolveName')

    SUCCESS_SUCCESS                 = 0
    MAPI_USER_ABORT                 = 1
    MAPI_E_USER_ABORT               = MAPI_USER_ABORT
    MAPI_E_FAILURE                  = 2
    MAPI_E_LOGON_FAILURE            = 3
    MAPI_E_LOGIN_FAILURE            = MAPI_E_LOGON_FAILURE
    MAPI_E_DISK_FULL                = 4
    MAPI_E_INSUFFICIENT_MEMORY      = 5
    MAPI_E_ACCESS_DENIED            = 6
    MAPI_E_TOO_MANY_SESSIONS        = 8
    MAPI_E_TOO_MANY_FILES           = 9
    MAPI_E_TOO_MANY_RECIPIENTS      = 10
    MAPI_E_ATTACHMENT_NOT_FOUND     = 11
    MAPI_E_ATTACHMENT_OPEN_FAILURE  = 12
    MAPI_E_ATTACHMENT_WRITE_FAILURE = 13
    MAPI_E_UNKNOWN_RECIPIENT        = 14
    MAPI_E_BAD_RECIPTYPE            = 15
    MAPI_E_NO_MESSAGES              = 16
    MAPI_E_INVALID_MESSAGE          = 17
    MAPI_E_TEXT_TOO_LARGE           = 18
    MAPI_E_INVALID_SESSION          = 19
    MAPI_E_TYPE_NOT_SUPPORTED       = 20
    MAPI_E_AMBIGUOUS_RECIPIENT      = 21
    MAPI_E_AMBIG_RECIP              = MAPI_E_AMBIGUOUS_RECIPIENT
    MAPI_E_MESSAGE_IN_USE           = 22
    MAPI_E_NETWORK_FAILURE          = 23
    MAPI_E_INVALID_EDITFIELDS       = 24
    MAPI_E_INVALID_RECIPS           = 25
    MAPI_E_NOT_SUPPORTED            = 26
    MAPI_E_UNICODE_NOT_SUPPORTED    = 27
    MAPI_E_ATTACHMENT_TOO_LARGE     = 28

    # REGION ***

# MAPI_H
