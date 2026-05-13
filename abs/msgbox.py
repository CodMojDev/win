from typing import ClassVar
from win.winuser import *

class MsgBox:
    _extra_styles_: ClassVar[int] = 0
    
    @classmethod
    def show(cls, name: str, text: str, style: int, parent: int | HWND = NULL) -> int:
        """
        Show message box.
        """
        
        return MessageBoxW(parent, text, name, style | cls._extra_styles_)
    
    @classmethod
    def ok(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Ok" button.
        """
        
        return cls.show(name, text, MB_OK, parent)
    
    @classmethod
    def ok_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Ok" and "Cancel" buttons.
        """
        
        return cls.show(name, text, MB_OKCANCEL, parent)
    
    @classmethod
    def abort_retry_ignore(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Abort", "Retry" and "Ignore" buttons.
        """
        
        return cls.show(name, text, MB_ABORTRETRYIGNORE, parent)
    
    @classmethod
    def yes_no(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Yes" and "No" buttons.
        """
        
        return cls.show(name, text, MB_YESNO, parent)
    
    @classmethod
    def yes_no_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Yes", "No" and "Cancel" buttons.
        """
        
        return cls.show(name, text, MB_YESNOCANCEL, parent)
    
    @classmethod
    def retry_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        """
        Show message box with "Retry" and "Cancel" buttons.
        """
        
        return cls.show(name, text, MB_RETRYCANCEL, parent)

    @staticmethod
    def warning():
        """
        Shortcut for WarningBox.
        """
        return WarningBox
    
    @staticmethod
    def info():
        """
        Shortcut for InfoBox.
        """
        return InfoBox
    
    @staticmethod
    def error():
        """
        Shortcut for ErrorBox.
        """
        return ErrorBox
    
    @classmethod
    def exclamation():
        """
        Shortcut for ExclamationBox.
        """
        return ExclamationBox
    
    @classmethod
    def asterisk():
        """
        Shortcut for AsteriskBox.
        """
        return AsteriskBox
    
    @classmethod
    def question():
        """
        Shortcut for QuestionBox.
        """
        return QuestionBox

class WarningBox(MsgBox):
    """
    Message box with warning icon.
    """
    
    _extra_styles_ = MB_ICONWARNING
    
class ErrorBox(MsgBox):
    """
    Message box with error icon.
    """
    
    _extra_styles_ = MB_ICONERROR

class InfoBox(MsgBox):
    """
    Message box with information icon.
    """
    
    _extra_styles_ = MB_ICONINFORMATION
    
class ExclamationBox(MsgBox):
    """
    Message box with exclamation icon.
    """
    
    _extra_styles_ = MB_ICONEXCLAMATION
    
class AsteriskBox(MsgBox):
    """
    Message box with asterisk icon.
    """
    
    _extra_styles_ = MB_ICONASTERISK
    
class QuestionBox(MsgBox):
    """
    Message box with question icon.
    """
    
    _extra_styles_ = MB_ICONQUESTION
    
MessageBox = MsgBox