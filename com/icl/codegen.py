from io import TextIOWrapper
from typing import *

class Code:
    INDENT = '    '
    
    file: TextIOWrapper
    indents: int
    
    def __init__(self, file_path: str):
        self.file = open(file_path, 'w', encoding='utf-8')
        self.indents = 0
        self.append('.icl')
        
    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()
        
    def append(self, string: str, not_breakline: bool = False):
        assert self.file and not self.file.closed
        
        if not not_breakline:
            string += '\n'
            
        self.file.write(string)
        
    def append_indented(self, string: str, not_breakline: bool = False):
        self.append(f'{self.make_indents()}{string}', not_breakline)
        
    def append_newline(self):
        assert self.file and not self.file.closed
        
        self.file.write('\n')
        
    def append_comment(self, comment: str = '', not_breakline: bool = False):
        assert self.file and not self.file.closed
        
        end = '\n' if not not_breakline else ''
        
        if len(comment) != 0:
            self.file.write(f'// {comment}{end}')
        else:
            self.file.write(f'//{end}')
            
    def append_gencomment(self):
        self.append('.gencomment')
        
    def append_commentext(self, comment: str):
        self.append(f'.commentext {comment}')
        
    def add_documentation(self, doc: str):
        self.append(f'doc {doc}')
        
    def add_version_data(self, version: int):
        self.append(f'.ver {version}')
        
    def add_block(self, block_name: str):
        self.append_indented(block_name)
        self.append('{')
        self.indent()
        
    def end_block(self):
        self.unindent()
        self.append_indented('}')
        self.append_newline()
        
    def add_silent(self):
        self.add_block('silent')
        
    def add_interface_unknown(self, interface_name: str):
        self.add_block(f'IU {interface_name}')
        
    def add_interface(self, interface_name: str, base: str = None):
        if base is not None:
            self.add_block(f'I {interface_name} ex {base}')
        else:
            self.add_block(f'I {interface_name}')
        
    def add_imports(self):
        self.add_block('imports')
        
    def add_enum(self, enum_name: str):
        self.add_block(f'ed {enum_name}')
    
    def add_enum_entry(self, enum_entry_name: str, enum_entry: int):
        self.append_indented(f'ee {enum_entry_name} {enum_entry}')
        
    def add_enum_entry_force(self, enum_entry_name: str, enum_entry: str):
        self.append_indented(f'eef {enum_entry_name} {enum_entry}')
        
    def add_structure(self, structure_name: str):
        self.add_block(f'sd {structure_name}')
        
    def add_structure_field(self, field: str, typ: str):
        self.append_indented(f'sf {typ} {field}')
        
    def append_equal(self, var: str, eq: str):
        self.append_indented(f'eq {var} {eq}')
        
    def make_indents(self) -> str:
        return self.indents * self.INDENT
    
    def add_import(self, import_entry: str):
        self.append(f'from import_entry import *')
        
    def add_com_function(self, name: str, arguments: list[str]):
        arguments = ' '.join(arguments)
        self.append_indented(f'cf {name} {arguments}')
        
    def add_virtual_function(self, name: str, result_type: str, arguments: list[str]):
        arguments = ' '.join(arguments)
        self.append_indented(f'cf {name} {result_type} {arguments}')
    
    def add_iid(self, iid: str):
        self.append_indented(f'iid {iid}')
    
    def indent(self): self.indents += 1
    
    def unindent(self): self.indents -= 1