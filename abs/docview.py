from .window import *

class Document:
    title: str
    path: str
    modified: bool
    views: list['View']
    
    def __init__(self):
        self.title = 'Document'
        self.path = ''
        self.modified = False
        self.views = []
    
    def get_title(self) -> str:
        return self.title
    
    def set_title(self, title: str):
        self.title = title
    
    def get_path(self) -> str:
        return self.path
    
    def set_path(self, path: str):
        self.path = path
        
    def is_modified(self) -> bool:
        return self.modified
    
    def set_modified(self, modified: bool=True):
        self.modified = modified
        
    def add_view(self, view: 'View'):
        self.views.append(view)
        self.on_view_list_changed()
    
    def remove_view(self, view: 'View'):
        self.views.remove(view)
        self.on_view_list_changed()
    
    def on_view_list_changed(self):
        ...
        
    def send_initial_update(self):
        for view in self.views:
            view.on_initial_update()
        
class View: 
    def on_initial_update(self):
        ...