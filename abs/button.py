from .window import *

class ButtonBase(Control):
    """
    Base class, wrapping the functionality of Win32 BUTTON common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Button'):
        super().__init__(parent, identifier)
        self.class_name = 'BUTTON'
        
        # predefine parameters given in constructor
        self._button_text = text
        self._width = width
        self._height = height
        
        # button events
        self.on_click = Event()
        self.on_double_click = Event()
        
        # if parent is window and Abs-managed object, then subscribe on events
        if isinstance(parent, Window) and Abs.managed(parent):
            parent.on_command += self.parent_window_on_command
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, self._button_text, relative)
    
    def parent_window_on_command(self, identifier: int, notify_code: int, hwnd: int):
        if identifier == self._identifier:
            if notify_code == BN_CLICKED:
                self.on_click.execute()
            elif notify_code == BN_DOUBLECLICKED:
                self.on_double_click.execute()
                
    @property
    def state(self) -> int:
        return self.send(BM_GETSTATE)
    
    @state.setter
    def state(self, state: int):
        self.post(BM_SETSTATE, state)
        
class Button(ButtonBase):
    """
    Win32 Button common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Button'):
        super().__init__(width, height, parent, identifier, text=text)
        self._style |= BS_PUSHBUTTON
        
    def click(self):
        self.post(BM_CLICK)
        
class RadioButton(ButtonBase):
    """
    Win32 Radio button common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'RadioButton', auto: bool = False):
        super().__init__(width, height, parent, identifier, text=text)
        
        # setup styles based on automatically enabling of radio button
        if auto:
            self._style |= BS_AUTORADIOBUTTON
        else:
            self._style |= BS_RADIOBUTTON
        
    def click(self):
        """
        Click on the radio button.
        """
        
        self.post(BM_CLICK)
        
class Checkbox(ButtonBase):
    """
    Win32 Checkbox common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Checkbox', auto: bool = False):
        super().__init__(width, height, parent, identifier, text=text)
        
        # setup styles based on automatically enabling of check box
        if auto:
            self._style |= BS_AUTOCHECKBOX
        else:
            self._style |= BS_CHECKBOX
        
    def click(self):
        self.send(BM_CLICK)
        
    @property
    def checked(self) -> bool:
        return self.send(BM_GETCHECK) == BST_CHECKED
    
    @checked.setter
    def checked(self, checked: bool):
        self.post(BM_SETCHECK, BST_CHECKED if checked else BST_UNCHECKED)
        
    @property
    def grayed(self) -> bool:
        return self.send(BM_GETCHECK) == BST_INDETERMINATE
    
    @grayed.setter
    def grayed(self, grayed: bool):
        if grayed:
            self.post(BM_SETCHECK, BST_INDETERMINATE)
        else:
            self.post(BM_SETCHECK, BST_UNCHECKED)
        
class GroupBox(ButtonBase):
    """
    Win32 Group box common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = ''):
        super().__init__(width, height, parent, identifier, text=text)
        self.style |= BS_GROUPBOX
        
class SplitButton(ButtonBase):
    """
    Win32 Split button common control.
    """
    
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Button'):
        super().__init__(width, height, parent, identifier, text=text)
        self.style |= BS_SPLITBUTTON
        
    def click(self):
        self.send(BM_CLICK)