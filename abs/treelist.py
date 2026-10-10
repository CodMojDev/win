from .treeview import *
from .listhdr import *

if sizeof(PVOID) == 8:
    suffix = 'x64'
else:
    suffix = 'x86'
LoadLibraryW(os.path.abspath(os.path.normpath(os.path.join(os.path.dirname(__file__), f'data/TreeList-{suffix}.dll'))))

#
# TreeList definitions
#

PFNTVCOMPAREEX = CALLBACK(INT, HWND, HTREEITEM, HTREEITEM, LPARAM, LPARAM, LPARAM)
PFNTVSORTEX = CALLBACK(INT, HWND, HTREEITEM, LPCWSTR, LPCWSTR, LPARAM, LPARAM)

class TVSORTEX(CStructure):
    _fields_ = [
        ("hParent", HTREEITEM),
        ("lpfnCompare", PFNTVSORTEX),
        ("lParam", LPARAM)
    ]
    hParent: int
    lpfnCompare: FARPROC
    lParam: int
LPTVSORTEX = LP_TVSORTEX = PTR(TVSORTEX)
TV_SORTEX = TVSORTEX

TVCOLUMNA = TV_COLUMNA = LV_COLUMNA
TVCOLUMNW = TV_COLUMNW = LV_COLUMNW
TVCOLUMN = TV_COLUMN = LV_COLUMN
    
class TVFIND(CStructure):
    _fields_ = [
        ("uFlags", UINT),
        ("uColumn", UINT),
        ("uState", UINT),
        ("uStateMask", UINT),
        ("lParam", LPARAM),
        ("pText", LPCWSTR)
    ]
    uFlags: int
    uColumn: int
    uState: int
    uStateMask: int
    lParam: int
    pText: LPCWSTR
TV_FIND = TVFIND    

class TV_KEYDOWN_EX(CStructure):
    _fields_ = [
        ("hdr", NMHDR),
        ("wVKey", WORD),
        ("wScan", WORD),
        ("flags", UINT)
    ]
    hdr: NMHDR
    wVKey: int
    wScan: int
    flags: int
    
class TV_STARTEDIT(CStructure):
    _fields_ = [
        ("hdr", NMHDR),
        ("item", TVITEM),
        ("uAction", UINT),
        ("uHeight", UINT),
        ("uMaxEntries", UINT),
        ("pTextEntries", LPCWSTR),
        ("pTextList", PTR(LPCWSTR)),
        ("ptAction", POINT)
    ]
    hdr: NMHDR
    item: TVITEMW
    uAction: int
    uHeight: int
    uMaxEntries: int
    pTextEntries: LPCWSTR
    pTextList: IPointer[LPCWSTR]
    ptAction: POINT
    
class TV_COLSIZE(CStructure):
    _fields_ = [
        ("hdr", NMHDR),
        ("uColumn", UINT),
        ("uIndex", UINT),
        ("uPosX", UINT),
        ("iSize", INT)
    ]
    hdr: NMHDR
    uColumn: int
    uIndex: int
    uPos: int
    iSize: int

TV_NOIMAGE				= (-2)
TV_NOCOLOR				= 0xFFFFFFFF
TV_NOAUTOEXPAND			= 0x20000000
TV_SECONDICON			= 0x40000000
TVLE_DONOTIFY			= 0xF5A5A500
TVIF_TEXTPTR			= 0x80000000
TVIF_TOOLTIPTIME		= 0x40000000
TVIF_TEXTCHANGED		= 0x20000000
TVIF_RETURNEXIT			= 0x10000000
TVIF_CASE				= 0x08000000
TVIF_NEXT				= 0x04000000
TVIF_CHILD				= 0x02000000
TVIF_CANCELED			= 0x01000000
TVIF_ONLYFOCUS			= 0x00800000
TVIF_SUBITEM	        = 0x8000
TVIF_SUBNUMBER			= 0x4000
TVIS_UNDERLINE			= 0x0001
TVSIL_CHECK				= 0x0003
TVSIL_SUBIMAGES			= 0x0004
TVSIL_HEADER			= 0x0005
TVN_COLUMNCLICK			= HDN_ITEMCLICK
TVN_COLUMNDBLCLICK		= HDN_ITEMDBLCLICK
TVE_EXPANDRECURSIVE		= (0x80000000)
TVE_EXPANDFORCE			= (0x40000000)
TVE_EXPANDNEXT			= (0x20000000)
TVE_ALLCHILDS			= (0x10000000)
TVE_ONLYCHILDS			= (0x00000008)
TVI_SORTEX				= HTREEITEM(0xFFFF0007).value
TVI_BEFORE				= HTREEITEM(0xFFFF0006).value
TVI_AFTER				= HTREEITEM(0xFFFF0005).value
def TVI_ROW(n: int)	-> int:
    return HTREEITEM(0xFFE00000+(n)).value
VK_DBLCLK				= 0x10000				# Edit with doubleclick
VK_ICONCLK				= 0x10001				# Edit with click on icon
VK_EDITCLK				= 0x10002				# Edit with click on augewähltes Element #visble element ?
TV_UINICODE             = 1

TVC_CLASSNAME = "TreeList"

# Color Constants (TVM_SETBKCOLOR)
TVC_BK					= 0					# Background
TVC_ODD					= 1					# alternate colors / odd    (see TVS_EX_ALTERNATECOLOR)
TVC_EVEN				= 2					# alternate colors / even	(see TVS_EX_ALTERNATECOLOR)
TVC_FRAME				= 3					# separator lines	(see TVS_EX_ITEMLINES)
TVC_TEXT				= 4					# text
TVC_LINE				= 5					# interior of the buttons
TVC_BOX					= 6					# exterior of the buttons
TVC_TRACK				= 7					# tracked item text
TVC_MARK				= 8					# selected line
TVC_MARKODD				= 8					# selected line (odd)
TVC_MARKEVEN			= 9					# selected line (even)
TVC_INSERT				= 10					# insertion point
TVC_BOXBG				= 11					# background of buttons 
TVC_COLBK				= 12					# background of marked column
TVC_COLODD				= 13					# alternate odd color of marked column
TVC_COLEVEN				= 14					# alternate even color of marked column
TVC_GRAYED				= 15					# background when disabled

# constants for GetNextItem (TVM_GETNEXTITEM)
TVGN_DROPHILITESUB		= 0x000C				# get selected column
TVGN_CARETSUB			= 0x000D				# Drophighilite Spalte holen
try:
    TVGN_NEXTSELECTED
except NameError:
    TVGN_NEXTSELECTED		= 0x000E				# next selected entry
TVGN_FOCUS				= 0x000F				# entry that has focus
TVGN_FOCUSSUB			= 0x0010				# column that has focus
TVGN_NEXTSELCHILD		= 0x0011				# next selected child entry
TVGN_LASTCHILD			= 0x0012				# last child entry
TVGN_NEXTITEM			= 0x0013				# to enumerate the entries

# constants for InsertColumn (mask)
TVCF_FMT				= LVCF_FMT			# set the text alignment
TVCF_IMAGE				= LVCF_IMAGE			# set column image
TVCF_TEXT				= LVCF_TEXT			# set column text
TVCF_WIDTH				= LVCF_WIDTH			# set fixed width
TVCF_VWIDTH				= LVCF_SUBITEM		# set variable width
TVCF_MIN				= LVCF_ORDER			# set minimum width
TVCF_MARK				= 0x80000000			# to mark a column
TVCF_FIXED				= 0x40000000			# can the column width can be changed 
TVCF_LASTSIZE			= 0x44332211			# Breite vor dem Fixieren wieder herstellen

# constants for InsertColumn (format mask)
TVCFMT_BITMAP_ON_RIGHT	= LVCFMT_BITMAP_ON_RIGHT
TVCFMT_COL_HAS_IMAGES	= LVCFMT_COL_HAS_IMAGES
TVCFMT_CENTER			= LVCFMT_CENTER
TVCFMT_IMAGE			= LVCFMT_IMAGE
TVCFMT_LEFT				= LVCFMT_LEFT
TVCFMT_RIGHT			= LVCFMT_RIGHT
TVCFMT_FIXED			= 0x20000000			# flag for fixing the column
TVCFMT_MARK				= 0x10000000			# flag for marking the column

# constants for Column AutoEdit
TVAE_MODEPOS			= 0x0008				# Mask for mode bits
TVAE_NONE				= (0<<TVAE_MODEPOS)	# no automatic edit
TVAE_EDIT				= (1<<TVAE_MODEPOS)	# automatic edit with edit box
TVAE_COMBO				= (2<<TVAE_MODEPOS)	# automatic edit with ComboBox
TVAE_CBLIST				= (3<<TVAE_MODEPOS)	# automatic edit with ComboListBox
TVAE_STEP				= (4<<TVAE_MODEPOS)	# advance with enter
TVAE_STEPED				= (5<<TVAE_MODEPOS)	# advance with enter
TVAE_CHECK				= (6<<TVAE_MODEPOS)	# automatic edit with CheckBox
TVAE_CHECKED			= (7<<TVAE_MODEPOS)	# automatic edit with CheckBox and Edit
TVAE_NEXTLINE			= 0x0001				# go to next line after edit
TVAE_DBLCLICK			= 0x0002				# edit with doubleclick
TVAE_FULLWIDTH			= 0x0004				# show combobox over the full width
TVAE_PTRLIST			= 0x0008				# data list is passed as a pointer list
TVAE_ONLYRETURN			= 0x0010				# edition can only be started with Return
TVAE_STATEENABLE		= 0x0020				# edition can be (un)locked with the TVIS_DISABLEBIT flag
TVAE_ICONCLICK			= 0x0040				# edition starts by clicking on the icon
TVAE_DROPDOWN			= 0x0080				# open the DropDownList when edition starts
def TVAE_COL(c: int) -> int:
    return (((c)&0x3F)<<11)	# column for automatic edit
def TVAE_CHAR(c: int) -> int:
    return (((c)&0xFF)<<17)	# delimiter for the data list
def TVAE_COUNT(c: int) -> int:
    return (((c)&0x7F)<<25)	# number of entries in the data list (0=auto)
TVAE_MODEMASK			= (7<<TVAE_MODEPOS)	# Mask for mode bits
TVIS_DISABLEBIT			= 0x8000				# flag for locking auto edit

# constants for HitTest (flags)
def TVHT_SUBTOCOL(u: int) -> int:
    return ((UINT(u).value)>>24)	# Convert column to column numbers mask
TVHT_SUBMASK			= 0xFF000000			# Maske in der die Spalte gespeichert wird
TVHT_ONRIGHTSPACE		= 0x00800000			# Auf rechtem Rand nach den Exträgen
TVHT_ONSUBLABEL			= 0x00400000			# Koordinate ist auf dem Text eines Extraeintrages
TVHT_ONSUBICON			= 0x00200000			# Koordinate ist auf einem Extraeintrag
TVHT_ONSUBRIGHT			= 0x00100000			# Koordinate ist auf einem Extraeintrag rechts vom Text
TVHT_ONSUBITEM			= (TVHT_ONSUBICON|TVHT_ONSUBLABEL)

# constants for GetItemRect (TVM_GETITEMRECT)
def TVIR_COLTOSUB(u: int) -> int:
    return ((u)<<24)			# specify column
TVIR_GETCOLUMN			= 0x00000080			# get only column
TVIR_TEXT				= 0x00000001			# get only text area

# constants for SelectChilds (TVM_SELECTCHILDS)
TVIS_WITHCHILDS			= 0x00000001			# get also childs
TVIS_DESELECT			= 0x00000002			# deselect all items

# constants for Options (TVM_GETSETOPTION)
TVOP_AUTOEXPANDOFF		= 0x00000001			# Icon Offset for TVS_EX_AUTOEXPANDICON
TVOP_WRITEOPTION		= 0x80000000			# write too

# constants for EditLabel (LVM_EDITLABEL)
def TVIR_EDITCOMBOCHAR(n: int) -> int:
    return (((n)&0xFF)<<8)		# Separator of the combobox entries (only for Notify message)
TVIR_EDITCOMBODEL		= 0x00000080			# Clears the buffer for the entries (only for Notify message)
TVIR_EDITCOMBODOWN		= 0x10000000			# open the combobox (only for Notify message)
TVIR_EDITCOMBOBOX		= 0x20000000			# instead of an edit, display a combobox
TVIR_EDITCOMBOLIST		= 0x40000000			# instead of an edit, display a combobox with list selection
TVIR_EDITFULL			= 0x80000000			# the edit window takes the full width
TVIR_EDITTEXT			= 0x00000001			# show the edit window over the text (only for Notify message)
def TVIR_EDITCOL(u: int) -> int:
    return ((u)&0xFF)			# auto edit column
TVIR_SELALL				= 0x00000000			# select all
def TVIR_SELAREA(a: int, b: int) -> int:
    return ((0x0C0000|(a&0x1FF)|((b&0x1FF)<<9))<<8)	# select text area
def TVIR_SETCURSOR(a: int) -> int:
    return ((0x080000|(a&0x3FFFF))<<8)					# Cursor auf Textstelle
def TVIR_SETAT(a: int) -> int:
    return ((0x040000|(a&0x3FFFF))<<8)					# Cursor auf Pixel-Offset

# constants for uStyleEx
TVS_EX_HEADEROWNIMGLIST = 0x00000400			# the header has its own TVSIL_HEADER image list (else it is shared with TVSIL_NORMAL)
TVS_EX_HEADERCHGNOTIFY	= 0x00000800			# notify when a column has been resized
TVS_EX_HEADERDRAGDROP	= 0x00001000			# columns over 1 can be sorted using drag and drop
TVS_EX_SINGLECHECKBOX	= 0x00002000			# checkboxes with single selection
TVS_EX_STEPOUT			= 0x00004000			# can leave an edit control with the cursor buttons
TVS_EX_BITCHECKBOX		= 0x00008000			# change only the first bit of the state
TVS_EX_ITEMLINES		= 0x00010000			# draw the item separating lines
TVS_EX_ALTERNATECOLOR	= 0x00020000			# use alternate lines background color 
TVS_EX_SUBSELECT		= 0x00040000			# allow to select columns
TVS_EX_FULLROWMARK		= 0x00080000			# the row mark fill the entire row
TVS_EX_TOOLTIPNOTIFY	= 0x00100000			# send a TVN_ITEMTOOLTIP notify to query for tooltip
TVS_EX_AUTOEXPANDICON	= 0x00200000			# use automaticaly the next icon for expanded items
TVS_EX_NOCHARSELCET		= 0x00400000			# disable looping selection of items via keyboard 
TVS_EX_NOCOLUMNRESIZE	= 0x00800000			# user cannot change the columns width
TVS_EX_HIDEHEADERS		= 0x01000000			# hide the header
TVS_EX_GRAYEDDISABLE	= 0x02000000			# gray out the control when disabled
TVS_EX_FULLROWITEMS		= 0x04000000			# backgrounds and lines takes the whole line (use with TVS_EX_ALTERNATECOLOR and TVS_EX_ITEMLINES)
TVS_EX_FIXEDCOLSIZE		= 0x08000000			# the width of the whole columns stays constant when resizing columns (the right margin of last column do not change)
TVS_EX_HOMEENDSELECT	= 0x10000000			# move to first / last item with Home / End keys
TVS_EX_SHAREIMAGELISTS	= 0x20000000			# image list is not deleted when the control is destroyed
TVS_EX_EDITCLICK		= 0x40000000			# enter edit mode with a single click
TVS_EX_NOCURSORSET		= 0x80000000			# VK_EDITCLK always select the entire text. Don't set the cursor to the click point, if TVS_EX_EDITCLICK is used
try:
    TVS_EX_MULTISELECT
except NameError:
    TVS_EX_MULTISELECT		= 0x00000002			# allow multiple selections
try:
    TVS_EX_AUTOHSCROLL
except NameError:
    TVS_EX_AUTOHSCROLL      = 0x00000020			# auto scroll to selected item (horizontal scrollbar stays hidden)

# constants for notify messages
TVN_ITEMTOOLTIP			= (TVN_FIRST-32)		# tooltip query
TVN_CBSTATECHANGED      = (TVN_FIRST-33)		# checkbox change
TVN_STEPSTATECHANGED	= (TVN_FIRST-34)		# autoedit state changed
TVN_STARTEDIT			= (TVN_FIRST-35)		# field edit
TVN_LBUTTONUP			= (TVN_FIRST-36)		# left button released
TVN_RBUTTONUP			= (TVN_FIRST-37)		# right button released
TVN_COLUMNCHANGED		= (TVN_FIRST-38)		# a column modified

# constants for new messages
TVM_GETHEADER			= (TV_FIRST+128-1)
TVM_GETCOLUMNCOUNT		= (TV_FIRST+128-2)
TVM_DELETECOLUMN		= (TV_FIRST+128-3)
TVM_INSERTCOLUMN		= (TV_FIRST+128-4-TV_UINICODE)
TVM_SELECTSUBITEM		= (TV_FIRST+128-6)
TVM_SELECTDROP			= (TV_FIRST+128-7)
TVM_SETITEMBKCOLOR		= (TV_FIRST+128-8)
TVM_GETITEMBKCOLOR		= (TV_FIRST+128-9)
TVM_SETITEMTEXTCOLOR	= (TV_FIRST+128-10)
TVM_GETITEMTEXTCOLOR	= (TV_FIRST+128-11)
TVM_GETITEMOFROW		= (TV_FIRST+128-12)
TVM_GETROWCOUNT			= (TV_FIRST+128-13)
TVM_GETROWOFITEM		= (TV_FIRST+128-14)
TVM_SETCOLUMN			= (TV_FIRST+128-15-TV_UINICODE)
TVM_GETCOLUMN			= (TV_FIRST+128-17-TV_UINICODE)
TVM_SETCOLUMNWIDTH		= (TV_FIRST+128-19)
TVM_GETCOLUMNWIDTH		= (TV_FIRST+128-20)
TVM_SETUSERDATASIZE		= (TV_FIRST+128-21)
TVM_GETUSERDATASIZE		= (TV_FIRST+128-22)
TVM_GETUSERDATA			= (TV_FIRST+128-23)
TVM_SORTCHILDRENEX		= (TV_FIRST+128-24)
TVM_COLUMNAUTOEDIT		= (TV_FIRST+128-25-TV_UINICODE)
TVM_COLUMNAUTOICON		= (TV_FIRST+128-27)
TVM_GETCOUNTPERPAGE		= (TV_FIRST+128-28)
TVM_FINDITEM			= (TV_FIRST+128-29-TV_UINICODE)
TVM_SELECTCHILDS		= (TV_FIRST+128-31)
TVM_GETSETOPTION		= (TV_FIRST+128-32)
TVM_ISITEMVISIBLE		= (TV_FIRST+128-33)
TVM_SETFOCUSITEM		= (TV_FIRST+128-34)
TVM_GETCOLUMNORDERARRAY	= (TV_FIRST+128-35)
TVM_SETCOLUMNORDERARRAY	= (TV_FIRST+128-36)
try:
    TVM_GETITEMSTATE
except NameError:			  
    TVM_GETITEMSTATE		= (TV_FIRST+39) 
try:										  
    TVM_GETEXTENDEDSTYLE	
except NameError:			  
    TVM_GETEXTENDEDSTYLE	= (TV_FIRST+45) 
try:
    TVM_SETEXTENDEDSTYLE
except NameError:
    TVM_SETEXTENDEDSTYLE	= (TV_FIRST+44)
try:
    TVM_GETLINECOLOR
except NameError:
    TVM_GETLINECOLOR		= (TV_FIRST+41)
try:
    TVM_SETLINECOLOR
except NameError:
    TVM_SETLINECOLOR		= (TV_FIRST+40)

try:
    TVNRET_DEFAULT
except NameError:
    TVNRET_DEFAULT			= 0
try:
    TVNRET_SKIPOLD
except NameError:
    TVNRET_SKIPOLD			= 1
try:
    TVNRET_SKIPNEW
except NameError:
    TVNRET_SKIPNEW			= 2

class TreeListItemInfo(TreeViewItemInfo):
    @property
    def sub_item(self) -> int:
        return self.cChildren
    
    @sub_item.setter
    def sub_item(self, sub_item: int):
        self.cChildren = sub_item
        self.mask |= TVIF_SUBITEM

class TreeList(TreeView):
    class Column(TVCOLUMNW):
        tv: 'TreeList'
        index: int
        
        def __init__(self, tv: 'TreeList', index: int):
            self.tv = tv
            self.index = index
        
        def delete(self):
            """
            Delete the column from tree-list view columns.
            """
            self.tv.columns.internal_columncount -= 1
            self.tv.send(TVM_DELETECOLUMN, self.index)
            
        def query(self, mask: int | None = None):
            """
            Query the column info.
            """
            if mask is None:
                mask = (TVCF_FIXED | TVCF_FMT | TVCF_IMAGE | 
                        TVCF_LASTSIZE | TVCF_MARK | TVCF_MIN | 
                        TVCF_TEXT | TVCF_VWIDTH | TVCF_WIDTH)
            if mask & TVCF_TEXT:
                text = create_unicode_buffer(256)
                setattr(self, '_buffer_cache', text)
                self.pszText = i_cast(text, LPWSTR)
                self.cchTextMax = 256
            self.tv.send(TVM_GETCOLUMN, self.index, self.ref())
            
        @property
        def text(self) -> str:
            self.query(TVCF_TEXT)
            return self.pszText.value
        
        @text.setter
        def text(self, text: str):
            self.tv.columns.set(self.index, text=text)
        
        @property
        def width(self) -> int:
            self.query(TVCF_WIDTH)
            return self.cx
        
        @width.setter
        def width(self, width: int):
            self.tv.columns.set(self.index, width=width)
        
        @property
        def image(self) -> int:
            self.query(TVCF_IMAGE)
            return self.iImage
        
        @image.setter
        def image(self, image: int):
            self.tv.columns.set(self.index, image=image)
            
        @property
        def format(self) -> int:
            self.query(TVCF_FMT)
            return self.fmt
        
        @format.setter
        def format(self, format: int):
            self.tv.columns.set(self.index, format=format)
    
    class Columns:
        tv: 'TreeList'
        internal_columncount: int
        
        def __init__(self, tv: 'TreeList'):
            self.tv = tv
            self.internal_columncount = 0
            
        def count(self):
            return self.tv.send(TVM_GETCOLUMNCOUNT)
    
        def insert(self, index: int, text: str = None, width: int = None, image: int = None,
                   format: int = None) -> 'TreeList.Column':
            """
            Insert column into tree-list view columns.
            """
            column = TreeList.Column(self.tv, 0)
            
            if text is not None:
                text = create_unicode_buffer(text)
                setattr(column, '_buffer_cache', text)
                column.pszText = i_cast(text, LPWSTR)
                column.cchTextMax = len(text)
                column.mask |= TVCF_TEXT
                
            if width is not None:
                column.cx = width
                column.mask |= TVCF_WIDTH
                
            if image is not None:
                column.iImage = image
                column.mask |= TVCF_IMAGE
                
            if format is not None:
                column.fmt = format
                column.mask |= TVCF_FMT
            
            previous_columncount = self.internal_columncount
            column.index = self.tv.send(TVM_INSERTCOLUMN, index, column.ref())
            self.internal_columncount = previous_columncount + 1
            if previous_columncount == 0:
                self.tv.header.styles.add(HDS_FULLDRAG)
            return column
        
        def add(self, text: str = None, width: int = None, image: int = None, format: int = None) -> 'TreeList.Column':
            """
            Add column into tree-list view columns.
            """
            return self.insert(self.count(), text, width, image, format)
        
        def get(self, index: int, mask: int | None = None) -> 'TreeList.Column':
            """
            Get the column from tree-list view and with the specified field mask.
            """
            column = TreeList.Column(self, index)
            column.query(mask)
            return column
    
        def set(self, index: int, text: str = None, width: int = None, image: int = None,
                format: int = None, extra: int = 0):
            """
            Set the column info in tree-list view.
            """
            column = TreeList.Column(self.tv, 0)
            column.mask = extra
            
            if text is not None:
                text = create_unicode_buffer(text)
                setattr(column, '_buffer_cache', text)
                column.pszText = i_cast(text, LPWSTR)
                column.cchTextMax = len(text)
                column.mask |= TVCF_TEXT
                
            if width is not None:
                column.cx = width
                column.mask |= TVCF_WIDTH
                
            if image is not None:
                column.iImage = image
                column.mask |= TVCF_IMAGE
                
            if format is not None:
                column.fmt = format
                column.mask |= TVCF_FMT
            
            column.index = self.tv.send(TVM_SETCOLUMN, index, column.ref())
    
    columns: Columns
    
    def __init__(self, width: int, height: int, parent: int | HANDLE, identifier: int | HANDLE):
        super().__init__(width, height, parent, identifier)
        self.styles.add(WS_CLIPCHILDREN)
        self.class_name = TVC_CLASSNAME
    
    def headless_init(self):
        super().headless_init()
        self.columns = self.Columns(self)
        
    def foreign_init(self):
        super().foreign_init()
        self.columns.internal_columncount = self.columns.count()
    
    @property
    def header(self) -> ListHeader:
        return ListHeader.foreign(self.send(TVM_GETHEADER))
    
    def focus_item(self, item: int | HTREEITEM, column: TUnion[int, 'TreeList.Column', None]):
        """
        Focus the tree item.
        """
        if isinstance(column, TreeList.Column):
            column = column.index
        self.send(TVM_SETFOCUSITEM, item, column)
        
    @property
    def header_image_list(self) -> ImageList:
        return ImageList.foreign_owner(self.send(TVM_GETIMAGELIST, TVSIL_HEADER))
    
    @header_image_list.setter
    def header_image_list(self, header_image_list: int | HANDLE):
        self.send(TVM_SETIMAGELIST, TVSIL_HEADER, header_image_list)