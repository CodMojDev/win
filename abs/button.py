from .window import *

class ButtonBase(Control):
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Button'):
        super().__init__(parent, identifier)
        self.class_name = 'BUTTON'
        self._button_text = text
        self._width = width
        self._height = height
        
    def create(self, x: int = 0, y: int = 0, relative: int | HWND = NULL):
        super().create(self._width, self._height, x, y, self._button_text, relative)
        
    @property
    def state(self) -> int:
        return SendMessage(self, BM_GETSTATE, 0, 0)
    
    @state.setter
    def state(self, state: int):
        SendMessage(self, BM_SETSTATE, state, 0)
        
class Button(ButtonBase):
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Button'):
        super().__init__(width, height, parent, identifier, text=text)
        self._style |= BS_PUSHBUTTON
        
    def click(self):
        SendMessage(self, BM_CLICK, 0, 0)
        
class RadioButton(ButtonBase):
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'RadioButton', auto: bool = False):
        super().__init__(width, height, parent, identifier, text=text)
        
        if auto:
            self._style |= BS_AUTORADIOBUTTON
        else:
            self._style |= BS_RADIOBUTTON
        
    def click(self):
        SendMessage(self, BM_CLICK, 0, 0)
        
class Checkbox(ButtonBase):
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = 'Checkbox', auto: bool = False):
        super().__init__(width, height, parent, identifier, text=text)
        
        if auto:
            self._style |= BS_AUTOCHECKBOX
        else:
            self._style |= BS_CHECKBOX
        
    def click(self):
        SendMessage(self, BM_CLICK, 0, 0)
        
    @property
    def checked(self) -> bool:
        return SendMessage(self, BM_GETCHECK, 0, 0) == BST_CHECKED
    
    @checked.setter
    def checked(self, checked: bool):
        SendMessage(self, BM_SETCHECK, BST_CHECKED if checked else BST_UNCHECKED, 0)
        
    def get_grayed(self) -> bool:
        return SendMessage(self, BM_GETCHECK, 0, 0) == BST_INDETERMINATE
    
    def set_grayed(self, grayed: bool):
        SendMessage(self, BM_SETCHECK, BST_INDETERMINATE, 0)
        
class GroupBox(ButtonBase):
    def __init__(self, width: int, height: int, parent: int | HWND,
                 identifier: int | HMENU, text: str = ''):
        super().__init__(width, height, parent, identifier, text=text)
        self.style |= BS_GROUPBOX