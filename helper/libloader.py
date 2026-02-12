from ..libloaderapi import LoadLibrary, LoadLibraryA, FreeLibrary
from .localehelper import IsLocalesEqual

class LibLoader:
    library: str
    
    def __init__(self, library):
        self.library = library

    def __enter__(self):
        if LoadLibrary == LoadLibraryA:
            self.library = self.library.encode()
        self.hModule = LoadLibrary(self.library)
        if not self.hModule:
            error_text = f"Library {self.library} not found"
            if IsLocalesEqual(["ru-RU", "uk-UA", "be-BY"]):
                error_text = f"Библиотека '{self.library}' не найдена"
            raise ModuleNotFoundError(error_text)
        return self.hModule
    
    def __exit__(self, *_):
        if self.hModule:
            FreeLibrary(self.hModule)