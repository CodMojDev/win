from typing import ClassVar
from win.winuser import *

class MessageBox:
    _extra_styles_: ClassVar[int] = 0
    
    @classmethod
    def show(cls, name: str, text: str, style: int, parent: int | HWND = NULL) -> int:
        return MessageBoxW(parent, text, name, style | cls._extra_styles_)
    
    @classmethod
    def ok(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_OK, parent)
    
    @classmethod
    def ok_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_OKCANCEL, parent)
    
    @classmethod
    def abort_retry_ignore(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_ABORTRETRYIGNORE, parent)
    
    @classmethod
    def yes_no(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_YESNO, parent)
    
    @classmethod
    def yes_no_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_YESNOCANCEL, parent)
    
    @classmethod
    def retry_cancel(cls, name: str, text: str, parent: int | HWND = NULL) -> int:
        return cls.show(name, text, MB_RETRYCANCEL, parent)

    @staticmethod
    def warning():
        return WarningBox
    
    @staticmethod
    def info():
        return InfoBox
    
    @staticmethod
    def error():
        return ErrorBox
    
    @classmethod
    def exclamation():
        return ExclamationBox
    
    @classmethod
    def asterisk():
        return AsteriskBox
    
    @classmethod
    def question():
        return QuestionBox

class WarningBox(MessageBox):
    _extra_styles_ = MB_ICONWARNING
    
class ErrorBox(MessageBox):
    _extra_styles_ = MB_ICONERROR

class InfoBox(MessageBox):
    _extra_styles_ = MB_ICONINFORMATION
    
class ExclamationBox(MessageBox):
    _extra_styles_ = MB_ICONEXCLAMATION
    
class AsteriskBox(MessageBox):
    _extra_styles_ = MB_ICONASTERISK
    
class QuestionBox(MessageBox):
    _extra_styles_ = MB_ICONQUESTION