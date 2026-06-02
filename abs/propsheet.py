from .dlg import *

class PropertySheet(Dialog):
    class Pages:
        def __init__(self, sheet: 'PropertySheet'):
            self.sheet = sheet
            
        def add(self, page: 'PropertySheet.Page'):
            self.sheet.page_handles.append(page.value)
            
        def remove(self, page: 'PropertySheet.Page'):
            self.sheet.page_handles.remove(page.value)
            
        def __len__(self) -> int:
            return len(self.sheet.page_handles)
        
        def __contains__(self, page: 'PropertySheet.Page') -> bool:
            return page.value in self.sheet.page_handles
        
        def __iter__(self) -> defb_t.Iterable:
            return [PropertySheet.Page.foreign_owner(handle) for handle in self.sheet.page_handles]
        
        @property
        def initial(self) -> int:
            return self.sheet.sheet.nStartPage
        
        @initial.setter
        def initial(self, initial: int):
            self.sheet.sheet.nStartPage = initial
        
    def __init__(self, flags: int = 0):
        # property sheet data
        self.sheet = PROPSHEETHEADERW_V2()
        self.sheet.dwSize = self.sheet.size()
        
        Window.__init__(self)
        Abs.Object.__init__(self)
        
        flags |= PSH_USECALLBACK
        callback = PFNPROPSHEETCALLBACK(self.sheet_callback)
        self.sheet.pfnCallback = callback
        self.add_ref(callback)
        
        self.on_button_pressed = Event()
        self.on_before_create = Event()
        self.on_create = Event()
        
        self.pages = self.Pages(self)
        self.sheet.dwFlags = flags
        self.page_handles = []
        self.caption = 'Dialog'
        self.modal = True
        
    @property
    def modal(self) -> bool:
        return not self.sheet.dwFlags & PSH_MODELESS
    
    @modal.setter
    def modal(self, modal: bool):
        if modal:
            self.sheet.dwFlags &= ~PSH_MODELESS
        else:
            self.sheet.dwFlags |= PSH_MODELESS
            
    @property
    def watermark(self) -> Bitmap:
        return Bitmap.foreign_owner(self.sheet.hbmWatermark)
    
    @watermark.setter
    def watermark(self, watermark: int | HANDLE):
        self.sheet.hbmWatermark = watermark
        
        if watermark:
            self.sheet.dwFlags |= PSH_USEHBMWATERMARK
        else:
            self.sheet.dwFlags &= ~PSH_USEHBMWATERMARK
            
    @property
    def header(self) -> Bitmap:
        return Bitmap.foreign_owner(self.sheet.hbmHeader)
    
    @header.setter
    def header(self, header: int | HANDLE):
        self.sheet.hbmHeader = header
        
        if header:
            self.sheet.dwFlags |= PSH_USEHBMWATERMARK
        else:
            self.sheet.dwFlags &= ~PSH_USEHBMWATERMARK
            
    @property
    def icon(self) -> Icon:
        return Icon.foreign_owner(self.sheet.hIcon)
    
    @icon.setter
    def icon(self, icon: int | HANDLE):
        self.sheet.hIcon = icon
        
        if icon:
            self.sheet.dwFlags |= PSH_USEHICON
        else:
            self.sheet.dwFlags &= ~PSH_USEHICON
            
    @property
    def rtl(self) -> bool:
        return not not self.sheet.dwFlags & PSH_RTLREADING
    
    @rtl.setter
    def rtl(self, rtl: bool):
        if rtl:
            self.sheet.dwFlags |= PSH_RTLREADING
        else:
            self.sheet.dwFlags &= ~PSH_RTLREADING
    
    class Page(Handle, Abs.Object):
        def __init__(self):
            super().__init__()
            Abs.Object.__init__(self)
            
            # property sheet page evens
            self.on_create = Event()
            self.on_destroy = Event()
            
            # property sheet page data
            self.page = PROPSHEETPAGEW_V4()
            self.page.dwSize = self.page.size()
        
        @classmethod
        def create(cls, title: str, icon: int | HANDLE = None, flags: int = 0) -> 'PropertySheet.Page':
            page = cls()
            
            # setup the property sheet page callback
            flags |= PSP_USECALLBACK
            callback = LPFNPSPCALLBACKW(page.page_callback)
            page.page.pfnCallback = callback
            page.add_ref(callback) # prevent the GC collecting the callback
            
            # icon support for page
            if icon is not None:
                page.page.hIcon = icon
                flags |= PSP_USEHICON
                
            pszTitle = create_unicode_buffer(title)
            page.page.dwFlags |= PSP_USETITLE
            page.page.pszTitle = i_cast(pszTitle, LPWSTR)
            page.add_ref(pszTitle)
                
            page.page.dwFlags = flags
            page.value = CreatePropertySheetPageW(page.page.ref())
            if not page.value:
                raise WinException()
            
            return page
        
        def page_callback(self, hwnd: int, msg: int, ppsp: IPointer[PROPSHEETPAGEW_V4]) -> int: 
            if msg == PSPCB_CREATE:
                if all(self.on_create.execute()):
                    return 1
                return 0
            elif msg == PSPCB_RELEASE:
                self.on_destroy.execute()
                return 0
            else:
                return 0
            
        def close(self):
            DestroyPropertySheetPage(self.value)
            self._closed = True
            
    def create(self) -> int:
        page_handles_length = len(self.page_handles)
        page_handles = (HPROPSHEETPAGE * page_handles_length)(*self.page_handles)
        self.sheet.nPages = page_handles_length
        self.sheet.phpage = page_handles
        caption = create_unicode_buffer(self.caption)
        self.sheet.pszCaption = i_cast(caption, LPCWSTR)
        self.add_ref(page_handles)
        self.add_ref(caption)
        
        result = PropertySheetW(self.sheet.ref())
        
        if not self.modal:
            self.value = result
            Application().modeless_dialogs.append(self.value)
            return 0
        
        return result
        
    def sheet_callback(self, hwnd: int, msg: int, lParam: int):
        if not self.value:
            self.value = hwnd
        
        if msg == PSCB_BUTTONPRESSED:
            self.on_button_pressed.execute(lParam)
        elif msg == PSCB_PRECREATE:
            self.on_before_create.execute(i_cast(lParam, LPDLGTEMPLATEW).contents)
        elif msg == PSCB_INITIALIZED:
            self.on_create.execute()
        
        return 0