from .window import *
from .imagelist import *
from .dragdrop import IDropTarget

class Rebar(Control):
    class Band:
        def __init__(self, rebar: 'Rebar', index: int):
            self.rebar = rebar
            self.index = index
            
        def delete(self):
            self.rebar.send(RB_DELETEBAND, self.index)
            
        def show(self, visible: bool = True):
            self.rebar.send(RB_SHOWBAND, self.index, visible)
            
        def hide(self):
            self.show(False)
        
        @property
        def rect(self) -> Rect:
            rc = Rect()
            self.rebar.send(RB_GETRECT, self.index, rc.ref())
            return rc
        
        @property
        def width(self) -> int:
            return self.rect.width
        
        @width.setter
        def width(self, width: int):
            self.rebar.send(RB_SETBANDWIDTH, self.index, width)
        
        @property
        def row_height(self) -> int:
            return self.rebar.send(RB_GETROWHEIGHT, self.index)
        
        @property
        def borders(self) -> Rect:
            rc = Rect()
            self.rebar.send(RB_GETBANDBORDERS, self.index, rc.ref())
            return rc
            
        def move(self, index: int):
            """
            Move band to given new index.
            """
            self.rebar.send(RB_MOVEBAND, self.index, index)
            
        def push_chevron(self, parameter: int = 0):
            """
            Push the chevron of band.
            """
            self.rebar.send(RB_PUSHCHEVRON, self.index, parameter)
            
        def maximize(self, ideal_width: int = 0):
            """
            Maximize the band.
            """
            self.rebar.send(RB_MAXIMIZEBAND, self.index, ideal_width)
            
        def minimize(self):
            """
            Minimize the band.
            """
            self.rebar.send(RB_MINIMIZEBAND, self.index)
            
        def begin_drag(self, x: int | None = None, y: int | None = None):
            """
            Begin drag on the rebar band.
            """
            if x is None or y is None: l = -1
            else: l = MAKELPARAM(x, y)
            self.rebar.send(RB_BEGINDRAG, self.index, l)
            
        def set(self, index: int = -1, text: str | None = None, integral_height: int | None = None,
                child: int | HANDLE | None = None, child_height: int | None = None, 
                child_min_width: int | None = None, child_min_height: int | None = None,
                width: int | None = None, style: int | None = None, ideal_width: int | None = None,
                back: int | Color.IColor | None = None, fore: int | Color.IColor | None = None,
                background: int | HANDLE | None = None, parameter: WT_ADDRLIKE | None = None,
                identifier: int | None = None, image_index: int | None = None,
                chevron_location: RECT | None = None, chevron_state: int | None = None,
                header_width: int | None = None):
            """
            Set the rebar band info.
            """
            rbbi = self.rebar.construct_band_info(
                index, text, integral_height, child,
                child_height, child_min_width, child_min_height,
                width, style, ideal_width, back, fore,
                background, parameter, identifier,
                image_index, chevron_location, 
                chevron_state, header_width)
            self.send(RB_SETBANDINFOW, self.index, rbbi.ref())
            
        def get(self, mask: int | None = None) -> REBARBANDINFOW:
            """
            Get the rebar band info.
            """
            rbbi = REBARBANDINFOW()
            rbbi.cbSize = rbbi.size()
            if mask is None:
                mask = (RBBIM_BACKGROUND | RBBIM_CHEVRONLOCATION | RBBIM_CHILD |
                        RBBIM_CHEVRONSTATE | RBBIM_CHILDSIZE | RBBIM_COLORS |
                        RBBIM_SIZE | RBBIM_ID | RBBIM_HEADERSIZE | RBBIM_IMAGE |
                        RBBIM_IDEALSIZE | RBBIM_LPARAM | RBBIM_STYLE | RBBIM_TEXT)
            if mask & RBBIM_TEXT:
                buffer = create_unicode_buffer(256)
                rbbi.lpText = i_cast(buffer, LPWSTR)
                rbbi.cch = 256
            rbbi.fMask = mask
            self.send(RB_GETBANDINFOW, self.index, rbbi.ref())
            return rbbi
        
    def __init__(self, parent: int | HANDLE, identifier: int | HMENU):
        super().__init__(parent, identifier)
        self.class_name = REBARCLASSNAMEW
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(0, 0, x, y, NULL, relative=relative)
    
    def construct_band_info(self, index: int = -1, text: str | None = None, integral_height: int | None = None,
                            child: int | HANDLE | None = None, child_height: int | None = None, 
                            child_min_width: int | None = None, child_min_height: int | None = None,
                            width: int | None = None, style: int | None = None, ideal_width: int | None = None,
                            back: int | Color.IColor | None = None, fore: int | Color.IColor | None = None,
                            background: int | HANDLE | None = None, parameter: WT_ADDRLIKE | None = None,
                            identifier: int | None = None, image_index: int | None = None,
                            chevron_location: RECT | None = None, chevron_state: int | None = None,
                            header_width: int | None = None) -> REBARBANDINFOW:
        """
        Construct REBARBANDINFOW from parameters.
        """
        rbbi = REBARBANDINFOW()
        rbbi.cbSize = rbbi.size()
        mask = 0
        if text is not None:
            mask |= RBBIM_TEXT
            rbbi.lpText = text
            rbbi.cch = len(text)
        if child is not None:
            mask |= RBBIM_CHILD
            rbbi.hwndChild = child
        if child_height is not None or child_min_width is not None or child_min_height is not None or integral_height is not None:
            mask |= RBBIM_CHILDSIZE
            rbbi.cyChild = child_height or 0
            rbbi.cxMinChild = child_min_width or 0
            rbbi.cyMinChild = child_min_height or 0
            rbbi.cyIntegral = integral_height or 0
        if style is not None:
            mask |= RBBIM_STYLE
            rbbi.fStyle = style
        if width is not None:
            mask |= RBBIM_SIZE
            rbbi.cx = width
        if ideal_width is not None:
            mask |= RBBIM_IDEALSIZE
            rbbi.cxIdeal = ideal_width
        if back is not None and fore is not None:
            mask |= RBBIM_COLORS
            rbbi.clrFore = int(fore)
            rbbi.clrBack = int(back)
        if background is not None:
            mask |= RBBIM_BACKGROUND
            rbbi.hbmBack = background
        if parameter is not None:
            mask |= RBBIM_LPARAM
            rbbi.lParam = PtrUtil.get_address(parameter)
        if identifier is not None:
            mask |= RBBIM_ID
            rbbi.wID = identifier
        if image_index is not None:
            mask |= RBBIM_IMAGE
            rbbi.iImage = image_index
        if chevron_location is not None:
            mask |= RBBIM_CHEVRONLOCATION
            rbbi.rcChevronLocation = chevron_location
        if chevron_state is not None:
            mask |= RBBIM_CHEVRONSTATE
            rbbi.uChevronState = chevron_state
        if header_width is not None:
            mask |= RBBIM_HEADERSIZE
            rbbi.cxHeader = header_width
        rbbi.fMask = mask
        return rbbi
    
    def insert(self, index: int = -1, text: str | None = None, integral_height: int | None = None,
               child: int | HANDLE | None = None, child_height: int | None = None, 
               child_min_width: int | None = None, child_min_height: int | None = None,
               width: int | None = None, style: int | None = None, ideal_width: int | None = None,
               back: int | Color.IColor | None = None, fore: int | Color.IColor | None = None,
               background: int | HANDLE | None = None, parameter: WT_ADDRLIKE | None = None,
               identifier: int | None = None, image_index: int | None = None,
               chevron_location: RECT | None = None, chevron_state: int | None = None,
               header_width: int | None = None) -> Band:
        """
        Insert item into the rebar control.
        """
        rbbi = self.construct_band_info(
            index, text, integral_height, child,
            child_height, child_min_width, child_min_height,
            width, style, ideal_width, back, fore,
            background, parameter, identifier,
            image_index, chevron_location, 
            chevron_state, header_width)
        result = self.send(RB_INSERTBANDW, index, rbbi.ref())
        if result == 0: raise WinException()
        return Rebar.Band(self, result)
    
    def hit(self, x: int, y: int) -> tuple[Band | None, int]:
        """
        Hit-test the given coordinates on rebar control.
        """
        rbhti = RBHITTESTINFO()
        rbhti.pt = POINT(x, y)
        i = self.send(RB_HITTEST, 0, rbhti.ref())
        if i == -1: return (None, 0)
        return (Rebar.Band(self, i), rbhti.flags)
    
    @property
    def palette(self) -> Palette:
        return Palette.foreign_owner(self.send(RB_GETPALETTE))
    
    @palette.setter
    def palette(self, palette: int | HANDLE):
        self.send(RB_SETPALETTE, 0, palette)
        
    @property
    def row_count(self) -> int:
        return self.send(RB_GETROWCOUNT)
    
    def count(self) -> int:
        """
        Get band count.
        """
        return self.send(RB_GETBANDCOUNT)
    
    def from_id(self, identifier: int) -> Band | None:
        """
        Get band instance from band identifier.
        """
        i = self.send(RB_IDTOINDEX, identifier)
        if i == -1: return None
        return Rebar.Band(self, i)
    
    @property
    def text_color(self) -> Color.BGR:
        return Color.BGR(self.send(RB_GETTEXTCOLOR))
    
    @text_color.setter
    def text_color(self, text_color: int | Color.IColor):
        self.send(RB_SETTEXTCOLOR, 0, text_color)
    
    @property
    def bk_color(self) -> Color.BGR:
        return Color.BGR(self.send(RB_GETBKCOLOR))
    
    @bk_color.setter
    def bk_color(self, bk_color: int | Color.IColor):
        self.send(RB_SETBKCOLOR, 0, bk_color)
        
    @property
    def color_scheme(self) -> COLORSCHEME:
        cs = COLORSCHEME()
        cs.dwSize = cs.size()
        self.send(RB_GETCOLORSCHEME, 0, cs.ref())
        return cs
    
    @color_scheme.setter
    def color_scheme(self, color_scheme: COLORSCHEME):
        color_scheme.dwSize = color_scheme.size()
        self.send(RB_SETCOLORSCHEME, 0, color_scheme.ref())
            
    @property
    def drop_target(self) -> IDropTarget | None:
        pTarget = IDropTarget.NULL()
        self.send(RB_GETDROPTARGET, 0, byref(pTarget))
        if not pTarget: return None
        return pTarget.contents
            
    def end_drag(self):
        """
        End drag on the rebar control.
        """
        self.send(RB_ENDDRAG)
        
    @property
    def bar_height(self) -> int:
        return self.send(RB_GETBARHEIGHT)
    
    @property
    def margins(self) -> tuple[int, int, int, int]:
        rc = RECT()
        self.send(RB_GETBANDMARGINS, 0, rc.ref())
        return rc.left, rc.top, rc.right, rc.bottom
    
    @property
    def image_list(self) -> ImageList:
        info = REBARINFO()
        info.cbSize = info.size()
        info.fMask = RBIM_IMAGELIST
        self.send(RB_GETBARINFO, 0, info.ref())
        return ImageList.foreign_owner(info.himl)
    
    @image_list.setter
    def image_list(self, image_list: int | HANDLE):
        info = REBARINFO()
        info.cbSize = info.size()
        info.fMask = RBIM_IMAGELIST
        info.himl = image_list
        self.send(RB_SETBARINFO, 0, info.ref())