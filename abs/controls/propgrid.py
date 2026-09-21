from win.abs.window import *
from win.abs.colordlg import *
from win.abs.button import *
from win.abs.edit import *
from win.abs.combobox import *
from win.abs.msgbox import *
from win.abs.toolbar import *
from win.abs.updown import *

import random

# property grid item operations
PGIO_REVERT       = 0
PGIO_DBLCLK       = 1
PGIO_COMMIT       = 2
PGIO_FOCUS        = 3
PGIO_THEMECHANGED = 4

# property grid item preferences
PGIP_NORMAL = 0
PGIP_FORCEPAINT = 1

class PropertyGridItem:
    name: str
    selected: bool
    description: str
    
    def __init__(self, name: str, description: str = ''):
        self.name = name
        self.selected = False
        self.description = description
        
    def paint(self, dc: DC):
        """
        Draw the property grid item value.
        """
    
    def measure(self, rect: Rect):
        """
        Measure the given value rectangle by-value.
        """
    
    def host(self, view: 'PropertyGridView', rect: Rect):
        """
        Host the property grid item by parent view and rectangle.
        """
        
    def enter(self):
        """
        Enter the property grid item edit mode.
        """
        
    def abort(self) -> bool:
        """
        Abort if the property grid item is in edit mode.
        """
        return True

    def hide(self):
        """
        Hide the property grid item.
        """
        
    def operation(self, op: int):
        """
        Perform an operation over property grid item.
        """
    
    def destroy(self):
        """
        Destroy the property grid item.
        """
        
    def preferences(self) -> int:
        """
        Get the preferences of the property grid item.
        """
        return PGIP_NORMAL
    
    def __del__(self):
        self.destroy()

class PropertyGridItemString(PropertyGridItem):
    edit: Edit | None
    rect: Rect | None
    view: TUnion['PropertyGridView', None]
    text: str
    styles: int
    original_text: str
    
    def __init__(self, name: str, text: str = '', description: str = '', styles: int = 0):
        super().__init__(name, description)
        self.original_text = self.text = text
        self.edit = None
        self.rect = None
        self.view = None
        self.styles = styles
        
    def host(self, view: 'PropertyGridView', rect: Rect):
        self.rect = rect
        if self.view is None:
            self.view = view
        if self.edit is None:
            self.unique_edit_id = random.randint(0, 1<<31)
            self.edit = Edit(rect.width - 4, rect.height, view, Identifiers[f'PropertyGridItemString->Edit-{self.unique_edit_id}'], text=self.text)
            self.edit.on_nm_focus_changed += self.buddy_focused
            self.edit.style |= self.styles
            self.edit.create(rect.x + 4, rect.y)
            self.edit.font = view.logical_bold_name_font
        else:
            self.edit.position = (rect.x + 4, rect.y)
            self.edit.size = (rect.width - 4, rect.height)
            
    def paint(self, dc: DC):
        if not self.edit.visible:
            rect = Rect.create(0 + 4, 0, self.rect.width - 4, self.rect.height)
            self.text = self.edit.text
            font = self.view.logical_bold_name_font
            with dc.select_ex(font):
                dc.draw_text(self.text, rect, DT_LEFT)
            
    def hide(self):
        if self.edit is not None and self.edit.visible:
            self.edit.hide()
    
    def enter(self):
        self.edit.show()

    def abort(self) -> bool:
        if self.edit is not None:
            self.edit.hide()
            self.text = self.edit.text
            self.operation(PGIO_COMMIT)
        return True
    
    def operation(self, op: int):
        if op == PGIO_DBLCLK:
            self.edit.selection = (0, -1)
        elif op == PGIO_REVERT:
            self.text = self.original_text
        elif op == PGIO_COMMIT:
            self.text = self.edit.text
            if self.text != self.original_text:
                self.view.on_item_updated.execute(self)
        elif op == PGIO_FOCUS:
            self.edit.focus()
        elif op == PGIO_THEMECHANGED:
            if self.view is not None and self.edit is not None:
                self.edit.font = self.view.logical_name_font
            
    def destroy(self):
        if self.edit is not None:
            self.edit.hide()
    
    def buddy_focused(self):
        self.view.focus_gained = True
        
    def preferences(self) -> int:
        return PGIP_FORCEPAINT
    
class PropertyGridItemCombobox(PropertyGridItem):
    variants: list[str]
    view: TUnion['PropertyGridView', None]
    rect: Rect | None
    combobox: Combobox | None
    default: int
    current: int
    
    def __init__(self, name: str, variants: list[str] = [], default: int = 0, description: str = ''):
        super().__init__(name, description)
        self.variants = variants
        self.view = None
        self.rect = None
        self.combobox = None
        self.current = self.default = default
    
    def measure(self, rect: Rect):
        rect.right -= GetSystemMetrics(SM_CXVSCROLL)
    
    def host(self, view: 'PropertyGridView', rect: Rect):
        self.rect = rect
        if self.view is None:
            self.view = view
        if self.combobox is None:
            self.unique_combobox_id = random.randint(0, 1<<31)
            self.combobox = Combobox(rect.width - 4, rect.height, view, Identifiers[f'PropertyGridItemCombobox->Combobox-{self.unique_combobox_id}'])
            self.combobox.on_nm_focus_changed += self.buddy_focused
            self.combobox.styles.add(CBS_DROPDOWNLIST)
            self.combobox.create(rect.x + 4, rect.y)
            self.combobox.font = self.view.logical_bold_name_font
            for variant in self.variants:
                self.combobox.append(variant)
            self.combobox.current = self.default
            self.combobox.hide()
        else:
            self.combobox.position = (rect.x + 4, rect.y)
            self.combobox.size = (rect.width - 4, rect.height)
    
    def paint(self, dc: DC):
        rect = Rect.create(0 + 4, 0, self.rect.width - 4, self.rect.height)
        self.current = self.combobox.current
        font = self.view.logical_bold_name_font
        with dc.select_ex(font):
            dc.draw_text(self.combobox.text(self.current), rect, DT_SINGLELINE | DT_LEFT)
    
    def enter(self):
        self.combobox.show()
    
    def abort(self) -> bool:
        if self.combobox is not None:
            self.current = self.combobox.current
            self.combobox.hide()
            self.operation(PGIO_COMMIT)
        return True
            
    def hide(self):
        if self.combobox is not None and self.combobox.visible:
            self.combobox.hide()
            
    def operation(self, op: int):
        if op == PGIO_REVERT:
            self.combobox.current = self.current = self.default
            self.view.invalidate()
        elif op == PGIO_DBLCLK:
            self.current = self.combobox.current
            if self.current < self.combobox.count():
                self.current += 1
                self.combobox.current = self.current
            self.view.invalidate()
        elif op == PGIO_COMMIT:
            self.current = self.combobox.current
            if self.current != self.default:
                self.view.on_item_updated.execute(self)
        elif op == PGIO_FOCUS:
            self.combobox.focus()
        elif op == PGIO_THEMECHANGED:
            if self.view is not None and self.combobox is not None:
                self.combobox.font = self.view.logical_name_font
            
    def destroy(self):
        if self.combobox is not None:
            self.combobox.close()
    
    def buddy_focused(self):
        self.view.focus_gained = True

class LowercaseDict:
    def __init__(self, dictionary: dict[str, Any]):
        self.dictionary = {k.lower(): v for k, v in dictionary.items()}
        
    def __getitem__(self, key: str) -> Any:
        return self.dictionary[key.lower()]

class PropertyGridItemColor(PropertyGridItem):
    color: Color.BGR
    button: Button | None
    rect: Rect | None
    view: TUnion['PropertyGridView', None]
    edit: Edit | None
    edit_mode: bool
    text: str
    original_text: str
    pen_frame: Pen | None
    
    def __init__(self, name: str, 
                 color: Color.IColor = Color.BGR.from_id(Color.ID.Black),
                 text: str = '',
                 description: str = ''):
        super().__init__(name, description)
        self.original_color = self.color = color.bgr()
        self.original_text = self.text = text
        self.button = None
        self.rect = None
        self.view = None
        self.edit = None
        self.edit_mode = False
        self.pen_frame = None
    
    def setup_pens(self):
        if self.pen_frame is None:
            black = Color.BGR.from_id(Color.ID.Black)
            self.pen_frame = Pen.create(PS_SOLID, 1, black)
    
    def paint(self, dc: DC):
        with dc.select_ex(self.pen_frame):
            dc.frame(Rect.create(0 + 1, 0 + 1, 20, self.rect.height - 1 - 1), Brush.stock(BLACK_BRUSH))
            with Brush.create(self.color) as brush:
                dc.fill(Rect.create(0 + 1 + 1, 0 + 1 + 1, 20 - 1 - 1, self.rect.height - 1 - 1 - 1 - 1), brush)
                self.text = self.edit.text
                if self.text.strip():
                    font = self.view.logical_bold_name_font
                    with dc.select_ex(font):
                        dc.draw_text(self.text, Rect.create(
                            1 + 20 + 8, 0, self.rect.width - 1 - 20 - 8 - 24, 
                            self.rect.height), DT_SINGLELINE | DT_LEFT)
    
    def measure(self, rect: Rect):
        rect.right -= GetSystemMetrics(SM_CXVSCROLL)
    
    def host(self, view: 'PropertyGridView', rect: Rect):
        self.rect = rect
        if self.view is None:
            self.view = view
            view.on_command += self.on_command
        if self.button is None:
            self.unique_button_id = random.randint(0, 1<<31)
            self.button = Button(24, rect.height, view, Identifiers[f'PropertyGridItemColor->Color-Button-{self.unique_button_id}'], text='...')
            self.button.on_nm_focus_changed += self.buddy_focused
            self.button.create(rect.right-24, rect.y)
            self.button.hide()
        else:
            self.button.position = (rect.right-24, rect.y)
            self.button.size = (24, rect.height)
        if self.edit is None:
            self.unique_edit_id = random.randint(0, 1<<31)
            self.edit = Edit(rect.width - 1 - 20 - 8 - 24, rect.height, view, Identifiers[f'PropertyGridItemColor->Edit-{self.unique_edit_id}'])
            self.edit.on_nm_focus_changed += self.buddy_focused
            self.edit.create(rect.x + 1 + 20 + 8, rect.y)
            self.edit.font = view.logical_bold_name_font
            self.edit.text = self.original_text
            self.edit.hide()
        else:
            self.edit.position = (rect.x + 1 + 20 + 8, rect.y)
            self.edit.size = (rect.width - 1 - 20 - 8 - 24, rect.height)
        
    def on_command(self, identifier: int, code: int, hwnd: int) -> bool:
        if identifier == Identifiers[f'PropertyGridItemColor->Color-Button-{self.unique_button_id}']:
            if code == BN_CLICKED:
                dialog = ColorDialog(self.view, color=self.color)
                if dialog.create():
                    self.color = dialog.color
                    self.edit.text = '#'+str(self.color.rgb())[2:]
                    self.view.invalidate()
            
    def hide(self):
        if self.button is not None and self.button.visible:
            self.button.hide()
        if self.edit is not None and self.edit.visible:
            self.edit.hide()
            
    def enter(self):
        self.edit_mode = True
        self.button.show()
        self.edit.show()
    
    def abort(self) -> bool:
        if not self.edit_mode: return True
        self.button.hide()
        self.edit.hide()
        self.text = self.edit.text
        return self.commit()
    
    def operation(self, op: int):
        if op == PGIO_REVERT:
            self.color = self.original_color
            self.text = self.original_text
            self.edit.text = self.text
            self.view.invalidate()
        elif op == PGIO_COMMIT:
            self.text = self.edit.text
            self.commit()
        elif op == PGIO_FOCUS:
            self.edit.focus()
        elif op == PGIO_THEMECHANGED:
            if self.view is not None and self.edit is not None:
                self.edit.font = self.view.logical_name_font
            
    def destroy(self):
        if self.button is not None:
            self.button.close()
        if self.edit is not None:
            self.edit.close()
        if self.view is not None:
            self.view.on_command -= self.on_command
            
    def commit(self) -> bool:
        color = self.text.strip()
        if color:
            if color.startswith('#'):
                try:
                    self.color = Color.BGR.string(color)
                except Exception:
                    MsgBox.warning().ok('Properties Window', 'Property value is not valid.', self.view)
                    self.edit.focus()
                    return False
            else:
                try:
                    self.color = Color.BGR.from_id(LowercaseDict(Color.ID.__dict__)[color])
                except Exception:
                    MsgBox.warning().ok('Properties Window', 'Property value is not valid.', self.view)
                    self.edit.focus()
                    return False
        
        if self.color != self.original_color:
            self.view.on_item_updated.execute(self)
            self.view.invalidate()
            self.original_text = self.text
        
        return True
            
    def preferences(self) -> int:
        return PGIP_FORCEPAINT
    
    def buddy_focused(self):
        self.view.focus_gained = True

# property grid view hit-test definitions
PGVHT_NONE = 0
PGVHT_DIRBUTTON = 1
PGVHT_ITEM = 2
PGVHT_DIRECTORY = 3
PGVHT_BUDDY = 4

# property grid view render mode definitions
PGVRM_DIRECTORIES = 1
PGVRM_ALPHABET = 2

# property grid view notify codes
PGVN_ROWCLICK = 0
PGVNRC_DIR = 1 # the lpDir field is valid
PGVNRC_ITEM = 2 # the iItem field is valid
class PGVNMRC(NMHDR):
    _fields_ = [
        ('flags', UINT),
        ('lpDir', LPWSTR),
        ('iItem', INT)
    ]
    flags: int
    lpDir: LPWSTR
    iItem: int

class PropertyGridView(Window):
    SCROLL_Y_UNIT = 3
    DIR_AREA_WIDTH = 14
    DIR_AREA_HEIGHT = 17
    DIR_BUTTON_VIRTUALRECT = Rect.create(2, 3, 10, 10)
    
    directories: dict[str, tuple[bool, bool, list[PropertyGridItem]]]
    ht_map: list[tuple[Rect, int, int | str]]
    propname_width: int
    minimal: int
    render_mode: int
    focus_gained: bool
    
    directory_color: Color.BGR
    background_color: Color.BGR
    directory_name_color: Color.BGR
    select_color: Color.BGR
    name_color: Color.BGR
    select_name_color: Color.BGR
    
    directory_font: str
    name_font: str
    
    has_uxtheme: bool
    vs_glyphopened: VisualStyleElement
    vs_glyphclosed: VisualStyleElement
    
    pen_windowtext: Pen
    
    logical_directory_font: Font
    logical_name_font: Font
    logical_bold_name_font: Font
    
    directory_brush: Brush
    select_color_brush: Brush
    bk_brush: Brush
    directory_name_brush: Brush
    
    def __init__(self):
        super().__init__()
        
        accelerator_table = AcceleratorTable.create(
            [ACCEL(FVIRTKEY, VK_ESCAPE, 
                   Identifiers['Property-Grid-View->Accelerators->ESC']
                   ),
             ACCEL(FVIRTKEY, VK_RETURN, 
                   Identifiers['Property-Grid-View->Accelerators->ENTER']
                   )], self)
        WindowLoopUnit.current(False).accelerator_tables.append(accelerator_table)
        
        # setup styles
        self.styles.add(WS_BORDER, WS_CHILD, WS_VISIBLE, WS_VSCROLL)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add_ex(WS_EX_CLIENTEDGE)
        
        # bind the handlers on window events
        self.on_create += self.gridview_on_create
        self.on_vscroll += self.gridview_on_vscroll
        self.on_left_button_up += self.gridview_on_left_button_up
        self.on_mouse_wheel += self.gridview_on_mouse_wheel
        self.on_command += self.gridview_on_command
        self.on_destroy += self.gridview_on_destroy
        self.on_left_button_double_click += self.gridview_on_left_button_double_click
        self.on_theme_changed += self.gridview_on_theme_changed
        self.on_sys_color_change += self.gridview_on_sys_color_change
        self.on_focus_changed += self.gridview_on_focus_changed
        self.on_item_updated = MultiEvent()
        
        self.propname_width = 40
        self.directories = {}
        self.ht_map = []
        self.minimal = 0
        self.focus_gained = True
        # render mode
        self.render_mode = PGVRM_DIRECTORIES
        
        self.directory_font = 'MS Shell Dlg'
        self.name_font = 'MS Shell Dlg'
        
        # allow double clicks
        self.class_style = CS_DBLCLKS
    
    def gridview_on_destroy(self):
        tables = WindowLoopUnit.current(False).accelerator_tables
        for i, table in enumerate(tables):
            if table.window == self:
                tables.pop(i)
                break
    
    def gridview_on_mouse_wheel(self, delta: int, key_flags: int, x: int, y: int):
        if delta > 0:
            if not self.vscroll.up.enabled:
                self.gridview_on_vscroll(SB_LINEUP, 0, 0)
        else:
            if not self.vscroll.down.enabled:
                self.gridview_on_vscroll(SB_LINEDOWN, 0, 0)
    
    def gridview_on_command(self, identifier: int, code: int, hwnd: int):
        if identifier == Identifiers['Property-Grid-View->Accelerators->ESC']:
            rows = self.rows()
            for row in rows:
                if not isinstance(row, PropertyGridItem): continue
                if row.selected:
                    row.operation(PGIO_REVERT)
                    self.invalidate()
                    break
        elif identifier == Identifiers['Property-Grid-View->Accelerators->ENTER']:
            rows = self.rows()
            for row in rows:
                if not isinstance(row, PropertyGridItem): continue
                if row.selected:
                    row.operation(PGIO_COMMIT)
                    self.invalidate()
                    break
    
    def gridview_on_focus_changed(self, window: Window):
        self.focus_gained = True
    
    def gridview_on_create(self) -> bool:
        # init vertical scrollbar and its state
        self.last_sb_position = 0
        self.vscroll.page = 1
        
        # perform the theming initialization
        self.reload_themes()
        return True
    
    def gridview_on_theme_changed(self):
        self.reload_themes()
        for row in self.rows():
            if isinstance(row, PropertyGridItem):
                row.operation(PGIO_THEMECHANGED)
        self.invalidate()
    
    def setup_colors(self):
        # setup property grid colors
        self.directory_color = Color.BGR.from_id(Color.ID.InactiveBorder)
        self.background_color = Color.BGR.from_id(Color.ID.White)
        self.directory_name_color = Color.BGR.from_id(Color.ID.GrayText)
        self.select_color = Color.BGR.from_id(Color.ID.Highlight)
        self.name_color = Color.BGR.from_id(Color.ID.ControlText)
        self.select_name_color = Color.BGR.from_id(Color.ID.HighlightText)

    def setup_brushes(self):
        self.directory_brush = Brush.create(self.directory_color)
        self.select_color_brush = Brush.create(self.select_color)
        self.bk_brush = Brush.create(self.background_color)
        self.directory_name_brush = Brush.create(self.directory_name_color)

    def setup_fonts(self):
        self.logical_directory_font = Font.create(self.directory_font, 14, weight=FW_DEMIBOLD)
        self.logical_name_font = Font.create(self.name_font, 14)
        self.logical_bold_name_font = Font.create(self.name_font, 14, weight=FW_BOLD)
    
    def setup_pens(self):
        if not self.has_uxtheme:
            self.pen_windowtext = Pen.create(PS_SOLID, 1, Color.BGR.from_id(Color.ID.WindowText))
        else:
            self.pen_windowtext = None
    
    def reload_themes(self):
        # refresh the Theme handles cache
        VisualStyleElement.refresh()
        # check the uxtheme existence or readiness
        if isinstance(uxtheme, NullLibrary):
            has_UxTheme = False
        else:
            try:
                Theme.create(None, 'TREEVIEW')
            except WinException:
                has_UxTheme = False
            else:
                has_UxTheme = True
        # switch the visual style elements
        if has_UxTheme:
            try:
                Theme.create(None, 'Explorer::TreeView')
            except WinException:
                has_ExplorerTreeView = False
            else:
                has_ExplorerTreeView = True
            if has_ExplorerTreeView:
                self.vs_glyphclosed = VisualStyleElements.ExplorerTreeView.Glyph.CLOSED
                self.vs_glyphopened = VisualStyleElements.ExplorerTreeView.Glyph.OPENED
            else:
                self.vs_glyphclosed = VisualStyleElements.TreeView.Glyph.CLOSED
                self.vs_glyphopened = VisualStyleElements.TreeView.Glyph.OPENED
        self.has_uxtheme = has_UxTheme
        
        # reload colors
        self.setup_colors()
        # reload visual GDI components
        self.setup_brushes()
        self.setup_fonts()
        self.setup_pens()
    
    def gridview_on_sys_color_change(self):
        # reload colors
        self.setup_colors()
        # reload brushes and pens
        self.setup_brushes()
        self.setup_pens()
        # redraw the window
        self.invalidate()
    
    def rows(self) -> list[tuple[str, bool] | PropertyGridItem]:
        result = []
        for k, v in self.directories.items():
            visible, selected, rows = v
            result.append((k, selected, visible))
            if visible:
                for row in rows:
                    result.append(row)
        if not (self.render_mode & PGVRM_DIRECTORIES):
            result = []
            for _v, _s, directory_rows in self.directories.values():
                result.extend(directory_rows)
        # if render mode supports PGVRM_ALPHABET, then sort it by alphabet order
        if self.render_mode & PGVRM_ALPHABET:
            def sort_procedure(x): # sort procedure
                if isinstance(x, PropertyGridItem):
                    return x.name
                return x[0]
            if self.render_mode & PGVRM_DIRECTORIES: # if render mode supports PGVRM_DIRECTORIES
                directories = []
                directory_i = -1
                for row in result:
                    if isinstance(row, PropertyGridItem):
                        directories[directory_i][1].append(row)
                    else:
                        directories.append((row, []))
                        directory_i += 1
                result = []
                directories = sorted(directories, key=sort_procedure)
                for directory, directory_rows in directories:
                    result.append(directory)
                    directory_rows = sorted(directory_rows, key=sort_procedure)
                    for row in directory_rows:
                        result.append(row)
            else:
                result = sorted(result, key=sort_procedure)
        return result
    
    def on_paint(self, dc: PaintDC) -> bool:
        # fill with the directory brush
        dc.fill(self.client_rect, self.directory_brush)
        # clear the hit-test map
        self.ht_map.clear()
        # get the rows
        rows = self.rows()
        
        # set the scroll bar info
        self.vscroll.enable_all()
        if self.minimal + self.SCROLL_Y_UNIT >= len(rows):
            self.vscroll.down.disable()
        elif self.minimal == 0:
            self.vscroll.up.disable()
        self.vscroll.range = (0, (len(rows)-1)//self.SCROLL_Y_UNIT)
        
        # recalc the property name width
        maximal_cx = 0
        y = 0
        view_height = self.height
        with dc.select_ex(self.logical_name_font):
            for i, row in enumerate(rows):
                if isinstance(row, PropertyGridItem):
                    # if row is not in view range, skip it
                    if i < self.minimal: continue # minimal extent
                    if y > view_height: continue # maximal extent
                    cx = dc.get_text_extent_point(row.name).cx
                    maximal_cx = max(cx, maximal_cx)
                y += self.DIR_AREA_HEIGHT
        if maximal_cx != 0:
            self.propname_width = maximal_cx + 10
            
        y = 0
        # iterate over all rows
        for i, row in enumerate(rows):
            if isinstance(row, PropertyGridItem):
                # if row is not in view range, skip it
                if i < self.minimal:
                    row.hide()
                    continue
                if y > view_height:
                    row.hide()
                    continue
                self.ht_map.append((Rect.create(self.DIR_AREA_WIDTH, y, self.propname_width, self.DIR_AREA_HEIGHT), PGVHT_ITEM, i))
                
                # fill the directory area background
                dc.fill(Rect.create(0, y, self.DIR_AREA_WIDTH, self.DIR_AREA_HEIGHT), self.directory_brush)
                
                with Pen.create(PS_SOLID, 1, self.directory_color) as pen:
                    with dc.select_ex(pen):
                        # draw the property name delimiter
                        dc.move(self.DIR_AREA_WIDTH + self.propname_width, y)
                        dc.line(self.DIR_AREA_WIDTH + self.propname_width, y+self.DIR_AREA_HEIGHT)
                        
                        # draw the lower horizontal delimiter
                        dc.move(self.DIR_AREA_WIDTH, y + self.DIR_AREA_HEIGHT - 1)
                        dc.line(self.width, y + self.DIR_AREA_HEIGHT - 1)
                
                bk_rect = Rect.create(self.DIR_AREA_WIDTH, y, self.propname_width, self.DIR_AREA_HEIGHT - 1)
                name_rect = bk_rect.copy()
                name_rect.offset(4, 0)
                with dc.select_ex(self.logical_name_font):
                    if row.selected:
                        if not self.focus_gained:
                            selection_brush = self.directory_brush
                            selection_color = self.directory_color
                            selection_name_color = self.name_color
                        else:
                            selection_brush = self.select_color_brush
                            selection_color = self.select_color
                            selection_name_color = self.select_name_color
                        dc.fill(bk_rect, selection_brush)
                        with DC.TransactSelect(dc, selection_color, dc.set_bk_color):
                            with DC.TransactSelect(dc, selection_name_color, dc.set_text_color):
                                dc.draw_text(row.name, name_rect, DT_SINGLELINE | DT_LEFT)
                    else:
                        dc.fill(bk_rect, self.bk_brush)
                        with DC.TransactSelect(dc, self.background_color, dc.set_bk_color):
                            with DC.TransactSelect(dc, self.name_color, dc.set_text_color):
                                dc.draw_text(row.name, name_rect, DT_SINGLELINE | DT_LEFT)
                
                x = self.DIR_AREA_WIDTH + 1 + self.propname_width
                width = self.width - self.propname_width - self.DIR_AREA_HEIGHT - 1
                height = self.DIR_AREA_HEIGHT - 1
                rect = Rect.create(x, y, width, height)
                row.measure(rect)
                prefs = row.preferences()
                
                self.ht_map.append((rect, PGVHT_BUDDY, i))
                row.host(self, rect)
                if row.selected: row.enter()
                if prefs & PGIP_FORCEPAINT or not row.selected:
                    with dc.create_compatible_bitmap(rect.width, rect.height) as bitmap:
                        with dc.create_compatible() as mem_dc:
                            with mem_dc.select_ex(bitmap):
                                # fill the property grid item value background
                                mem_dc.fill(Rect.create(0, 0, rect.width, rect.height), self.bk_brush)
                                row.paint(mem_dc)
                                dc.bit_blt(rect.x, rect.y, 0, 0, rect.width, rect.height, mem_dc, SRCCOPY)
            else:
                # if row is not in view range, skip it
                if i < self.minimal: 
                    continue
                if y > view_height:
                    continue
                name, selected, visible = row
                
                # fill the directory rectangle with color
                dc.fill(Rect.create(0, y, self.width, self.DIR_AREA_HEIGHT), self.directory_brush)
                
                # get the element glyph icon for visible state
                if not visible:
                    state = 0 # +
                    for row in self.directories[name][2]:
                        row.hide()
                else:
                    state = 1 # -
                
                # calculate directory button rectangle, append into HT map and draw
                dirbutton_rect = Rect.create(0 + self.DIR_BUTTON_VIRTUALRECT.x, y + self.DIR_BUTTON_VIRTUALRECT.y, self.DIR_BUTTON_VIRTUALRECT.width, self.DIR_BUTTON_VIRTUALRECT.height)
                self.ht_map.append((dirbutton_rect, PGVHT_DIRBUTTON, name))
                self.draw_directory_button(state, dc, dirbutton_rect)
                
                # draw the directory name
                with dc.select_ex(self.logical_directory_font):
                    # calculate the directory name rectangle
                    cx = dc.get_text_extent_point(name).cx
                    dir_rect = Rect.create(self.DIR_AREA_WIDTH, y, cx + 10, self.DIR_AREA_HEIGHT)
                    self.ht_map.append((dir_rect, PGVHT_DIRECTORY, name))
                    
                    # draw the directory name with colors
                    with DC.TransactSelect(dc, self.directory_color, dc.set_bk_color):
                        with DC.TransactSelect(dc, self.directory_name_color, dc.set_text_color):
                            dc.draw_text(name, Rect.create(self.DIR_AREA_WIDTH+4, y+2, self.width, self.DIR_AREA_HEIGHT - 1 - 1), DT_LEFT|DT_SINGLELINE)
                    
                # draw the selected directory rect state
                if selected:
                    dc.draw_focus_rect(dir_rect)
            y += self.DIR_AREA_HEIGHT
        return True
    
    def draw_directory_button(self, state: int, dc: DC, rect: Rect):
        if self.has_uxtheme:
            if state == 0:
                element = self.vs_glyphclosed
            else:
                element = self.vs_glyphopened
            element.draw_background(dc, rect)
        else:
            rect = Rect.create(rect.x + (rect.width - 9) // 2, rect.y + (rect.height - 9) // 2, 9, 9)
            with dc.select_ex(self.pen_windowtext):
                with dc.select_ex(Brush.stock(NULL_BRUSH)):
                    dc.rectangle(rect)
                if state == 0: # +
                    x = rect.left+rect.width//2
                    dc.move(x, rect.top+2)
                    dc.line(x, rect.bottom-2)
                    
                    y = rect.top+rect.height//2
                    dc.move(rect.left+2, y)
                    dc.line(rect.right-2, y)
                elif state == 1: # -
                    y = rect.top+rect.height//2
                    dc.move(rect.left+2, y)
                    dc.line(rect.right-2, y)
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.invalidate()
        return True
    
    def row_count(self) -> int:
        if self.render_mode & PGVRM_DIRECTORIES:
            n = len(self.directories)
            for v in self.directories.values():
                visible, _, rows = v
                if visible: n += len(rows)
            return n
        else:
            n = 0
            for v in self.directories.values():
                _v, _s, rows = v
                n += len(rows)
            return n
    
    def gridview_on_vscroll(self, code: int, position: int, _):
        if code == SB_LINEDOWN:
            count = self.row_count()
            if self.minimal + self.SCROLL_Y_UNIT < count:
                self.minimal += self.SCROLL_Y_UNIT
                self.vscroll.position += 1
        elif code == SB_LINEUP:
            if self.minimal - self.SCROLL_Y_UNIT >= 0:
                self.minimal -= self.SCROLL_Y_UNIT
                self.vscroll.position -= 1
        elif code == SB_THUMBTRACK:
            diff = position - self.last_sb_position
            self.last_sb_position = position
            self.minimal += (diff*self.SCROLL_Y_UNIT)
            self.vscroll.position = position
        self.invalidate()
    
    def gridview_on_left_button_double_click(self, flags: int, x: int, y: int):
        ht, n = self.hit_test(x, y)
        if ht == PGVHT_NONE: return
        elif ht == PGVHT_DIRECTORY:
            for k, (_v, _s, rows) in self.directories.items():
                for row in rows:
                    if not row.abort(): return
                    row.selected = False
            for k, (visible, _, rows) in self.directories.items():
                if k == n:
                    self.directories[k] = (not visible, True, rows)
                else:
                    self.directories[k] = (visible, False, rows)
            self.invalidate()
        elif ht == PGVHT_ITEM or ht == PGVHT_BUDDY:
            rows = self.rows()
            for i, row in enumerate(rows):
                if not isinstance(row, PropertyGridItem): continue
                if i == n:
                    row.operation(PGIO_DBLCLK)
    
    def gridview_on_left_button_up(self, flags: int, x: int, y: int):
        ht, n = self.hit_test(x, y)
        if ht == PGVHT_NONE: return
        elif ht == PGVHT_DIRBUTTON:
            for k, (_v, _s, rows) in self.directories.items():
                for row in rows:
                    if not row.abort(): return
                    row.selected = False
            for k, (visible, _, rows) in self.directories.items():
                if k == n:
                    self.directories[k] = (not visible, True, rows)
                else:
                    self.directories[k] = (visible, False, rows)
            self.invalidate()
        elif ht == PGVHT_ITEM:
            rows = self.rows()
            for i, row in enumerate(rows):
                if isinstance(row, PropertyGridItem):
                    if i != n: 
                        if not row.abort(): return
                        row.selected = False
            for i, row in enumerate(rows):
                if isinstance(row, PropertyGridItem):
                    if i == n: 
                        row.selected = True
                        row.enter()
            for name in self.directories.keys():
                visible, _, directory_rows = self.directories[name]
                self.directories[name] = (visible, False, directory_rows)
            nmrc = PGVNMRC()
            # NMHDR fields
            nmrc.hwndFrom = self
            nmrc.code = PGVN_ROWCLICK
            # PGVNMRC fields
            nmrc.flags = PGVNRC_ITEM
            nmrc.iItem = n
            self.parent.send(WM_NOTIFY, self.identifier, nmrc.ref())
            self.invalidate()
        elif ht == PGVHT_DIRECTORY:
            for _v, _s, rows in self.directories.values():
                for row in rows:
                    row.selected = False
                    if not row.abort(): return
            for name in self.directories.keys():
                visible, _, rows = self.directories[name]
                if name != n:
                    self.directories[name] = (visible, False, rows)
                else:
                    self.directories[name] = (visible, True, rows)
            
            nmrc = PGVNMRC()
            # NMHDR fields
            nmrc.hwndFrom = self
            nmrc.code = PGVN_ROWCLICK
            # PGVNMRC fields
            nmrc.flags = PGVNRC_DIR
            length = (len(n)+1)<<1
            buffer = malloc(length)
            memcpy(buffer, n, length)
            nmrc.lpDir = i_cast(buffer, LPWSTR)
            self.parent.send(WM_NOTIFY, self.identifier, nmrc.ref())
            self.invalidate()
        elif ht == PGVHT_BUDDY:
            rows = self.rows()
            one_of_failed = False
            entered = None
            for i, row in enumerate(rows):
                if not isinstance(row, PropertyGridItem): continue
                if i != n:
                    if not row.abort():
                        one_of_failed = True
                    else:
                        row.selected = False
                else:
                    entered = row
            if not one_of_failed:
                entered.selected = True
                entered.enter()
                entered.operation(PGIO_FOCUS)
                nmrc = PGVNMRC()
                # NMHDR fields
                nmrc.hwndFrom = self
                nmrc.code = PGVN_ROWCLICK
                # PGVNMRC fields
                nmrc.flags = PGVNRC_ITEM
                nmrc.iItem = n
                self.parent.send(WM_NOTIFY, self.identifier, nmrc.ref())
                self.invalidate()
        
    def hit_test(self, x: int, y: int) -> tuple[int, int | None | str]:
        pt = Point(x, y)
        for rc, ht, v in self.ht_map:
            if pt in rc:
                return (ht, v)
        return (PGVHT_NONE, None)
    
    def on_erase_background(self, dc: DC):
        return True

class PropertyGridDescription(Window):
    text: str
    header: str
    header_font: str
    logical_header_font: Font
    text_font: str
    logical_text_font: Font
    edge_cx: int
    edge_cy: int
    color_background: Color.BGR
    bk_brush: Brush
    
    def __init__(self):
        super().__init__()
        self.styles.add(WS_BORDER, WS_CHILD, WS_VISIBLE)
        self.styles.remove(WS_OVERLAPPEDWINDOW)
        self.styles.add_ex(WS_EX_CLIENTEDGE)
        self.on_create += self.desc_on_create
        self.on_sys_color_change += self.desc_on_sys_color_change
        self.on_theme_changed += self.desc_on_theme_changed
        self.text = ''
        self.header = ''
        self.header_font = 'MS Shell Dlg'
        self.text_font = 'MS Shell Dlg'
        self.edge_cx = GetSystemMetrics(SM_CXEDGE)
        self.edge_cy = GetSystemMetrics(SM_CYEDGE)
        
    def desc_on_create(self) -> bool:
        self.setup_fonts()
        self.setup_colors()
        self.setup_brushes()
        return True
    
    def setup_fonts(self):
        self.logical_header_font = Font.create(self.header_font, 15, weight = FW_ULTRABOLD)
        self.logical_text_font = Font.create(self.text_font, 13)
    
    def setup_colors(self):
        self.color_background = Color.BGR.from_id(Color.ID.InactiveBorder)
    
    def setup_brushes(self):
        self.bk_brush = Brush.create(self.color_background)
    
    def on_paint(self, dc: PaintDC) -> bool:
        with dc.select_ex(self.logical_header_font):
            height = dc.get_text_extent_point(self.header).cy
            with DC.TransactSelect(dc, self.color_background, dc.set_bk_color):
                dc.text_out(self.edge_cx+5, self.edge_cy+4, self.header)
        with dc.select_ex(self.logical_text_font):
            rc = self.client_rect
            dx, dy = self.edge_cx, self.edge_cy
            text = self.text.replace('\r\n', '\n').replace('\n', ' \n ')
            for word in text.split(' '):
                if word == '\n':
                    dy += dc.get_text_extent_point('A').cy
                    dx = self.edge_cx
                else:
                    size = dc.get_text_extent_point(word)
                    if 5 + dx + size.cx >= rc.right:
                        dy += size.cy
                        dx = self.edge_cx
                    with DC.TransactSelect(dc, self.color_background, dc.set_bk_color):
                        dc.text_out(5 + dx, 4 + height + 6 + dy, word)
                    dx += size.cx + dc.get_text_extent_point(' ').cx
        return True
    
    def on_erase_background(self, dc: DC) -> bool:
        dc.fill(self.client_rect, self.bk_brush)
        return True
    
    def get_recommended_height(self, text: str, header: str):
        with DC.create_compatible(NULL) as dc:
            with dc.select_ex(self.logical_header_font):
                height = dc.get_text_extent_point(header).cy
            with dc.select_ex(self.logical_text_font):
                rc = self.client_rect
                dx, dy = self.edge_cx, self.edge_cy + dc.get_text_extent_point('A').cy
                text = text.replace('\r\n', '\n').replace('\n', ' \n ')
                for word in text.split(' '):
                    if word == '\n':
                        dy += dc.get_text_extent_point('A').cy
                        dx = self.edge_cx
                    else:
                        size = dc.get_text_extent_point(word)
                        if 5 + dx + size.cx >= rc.right:
                            dy += size.cy
                            dx = self.edge_cx
                        dx += size.cx + dc.get_text_extent_point(' ').cx
                return 4 + dy + height + 6 + self.edge_cy + 10
            
    def on_size(self, flags: int, width: int, height: int) -> bool:
        self.invalidate()
        return True
    
    def desc_on_sys_color_change(self):
        self.setup_colors()
        self.setup_brushes()
        self.invalidate()
        
    def desc_on_theme_changed(self):
        self.setup_fonts()
        self.invalidate()

PGS_OWNERBUDDY = 0x1

class PropertyGrid(Window):
    ALPHABET_IMAGE = Bitmap.load(os.path.join(os.path.dirname(__file__), 'data/alphabet.bmp'))
    DIRECTORIES_IMAGE = Bitmap.load(os.path.join(os.path.dirname(__file__), 'data/directories.bmp'))
    
    buddy: Window | None
    on_buddy_notify: MultiEvent
    on_buddy_command: MultiEvent
    color_background: Color.BGR
    bk_brush: Brush
    
    def __init__(self):
        super().__init__()
        self.on_create += self.grid_on_create
        self.on_notify += self.grid_on_notify
        self.on_command += self.grid_on_command
        self.on_sys_color_change += self.grid_on_sys_color_change
        self.on_focus_lost += self.grid_on_focus_lost
        self.on_focus_changed += self.grid_on_focus_changed
        self.on_buddy_notify = MultiEvent()
        self.on_buddy_command = MultiEvent()
        self.styles.remove(WS_MAXIMIZEBOX, WS_MINIMIZEBOX)
        self.styles.add_ex(WS_EX_TOOLWINDOW)
        self.buddy = None
    
    def toolbar_buddy_command(self, identifier: int, code: int, hwnd: int):
        if identifier == Identifiers['PropertyGrid->Toolbar->Alphabet']:
            self.grid_view.render_mode ^= PGVRM_ALPHABET
            self.grid_view.invalidate()
        elif identifier == Identifiers['PropertyGrid->Toolbar->Directories']:
            self.grid_view.render_mode ^= (PGVRM_DIRECTORIES)
            self.grid_view.invalidate()
    
    def setup_colors(self):
        self.color_background = Color.BGR.from_id(Color.ID.InactiveBorder)
    
    def setup_brushes(self):
        self.bk_brush = Brush.create(self.color_background)
    
    def grid_on_create(self) -> bool:
        self.setup_colors()
        self.setup_brushes()
        if self.buddy is None and not (self.style & PGS_OWNERBUDDY):
            toolbar = Toolbar(self, Identifiers['PropertyGrid->Toolbar'])
            toolbar.create()
            self.toolbar_image_list = ImageList.create(16, 16, 2, ILC_COLOR24 | ILC_MASK)
            magenta = Color.BGR.from_id(Color.ID.Magenta)
            self.toolbar_image_list.add_masked(self.ALPHABET_IMAGE, magenta)
            self.toolbar_image_list.add_masked(self.DIRECTORIES_IMAGE, magenta)
            toolbar.image_list = self.toolbar_image_list
            toolbar.add(0, Identifiers['PropertyGrid->Toolbar->Alphabet'], BTNS_CHECK)
            toolbar.add(1, Identifiers['PropertyGrid->Toolbar->Directories'], BTNS_CHECK, TBSTATE_CHECKED|TBSTATE_ENABLED)
            self.on_buddy_command += self.toolbar_buddy_command
            self.buddy = toolbar
            dy = toolbar.y
        elif self.buddy is not None:
            self.buddy.parent = self
            dy = self.buddy.y
        else: 
            dy = 0
        self.description = PropertyGridDescription()
        self.description.create(self.width, self.height - 60, 0, 60, parent=self)
        self.grid_view = PropertyGridView()
        self.grid_view.create(self.width, self.height - 60 - dy, 0, dy, parent=self)
        return True
    
    def on_size(self, flags: int, width: int, height: int) -> bool:
        if self.buddy is not None:
            dy = self.buddy.height
            self.buddy.width = width
        else: dy = 0
        recommended = self.description.get_recommended_height(self.description.text, self.description.header)
        self.description.size = (width, recommended)
        self.description.position = (0, height - recommended)
        self.grid_view.size = (width, height - self.description.height - dy - 3)
        self.grid_view.position = (0, dy)
        
        return True
    
    def grid_on_command(self, identifier: int, code: int, hwnd: int):
        if self.buddy is not None and hwnd == self.buddy.value:
            self.on_buddy_command.execute(identifier, code, hwnd)
    
    def grid_on_notify(self, nm: NMHDR):
        if self.buddy is not None and nm.hwndFrom == self.buddy.value:
            self.on_buddy_notify.execute(nm)
        if nm.hwndFrom != self.grid_view.value:
            return
        if nm.code == PGVN_ROWCLICK:
            nmrc = i_cast_structure(nm, PGVNMRC)
            if nmrc.flags & PGVNRC_DIR:
                self.description.header = nmrc.lpDir.value
                free(nmrc.lpDir)
                self.description.invalidate()
            elif nmrc.flags & PGVNRC_ITEM:
                item = self.grid_view.rows()[nmrc.iItem]
                self.description.header = item.name
                self.description.text = item.description
                self.description.invalidate()
                
    def grid_on_sys_color_change(self):
        Color.Table.array = None
        self.setup_colors()
        self.setup_brushes()
        
        self.grid_view.send(WM_SYSCOLORCHANGE)
        self.description.send(WM_SYSCOLORCHANGE)
    
    def on_erase_background(self, dc: DC) -> bool:
        dc.fill(self.client_rect, self.bk_brush)
        return True
    
    def grid_on_focus_lost(self, window: Window):
        self.grid_view.focus_gained = False
        self.grid_view.invalidate()
        
    def grid_on_focus_changed(self, window: Window):
        self.grid_view.focus_gained = True
        self.grid_view.invalidate()