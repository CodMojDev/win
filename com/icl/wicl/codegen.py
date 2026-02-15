from io import TextIOWrapper
from typing import *

class Code:
    INDENT = '    '
    
    file: TextIOWrapper
    indents: int
    
    def __init__(self, file_path: str):
        self.file = open(file_path, 'w', encoding='utf-8')
        self.indents = 0
        
    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()
            
    def append_decorator(self, decorator: str, args: List[str], 
                         named_args: List[Tuple[str, str]]):
        assert self.file and not self.file.closed
        
        if len(args) == 0 and len(named_args) == 0:
            self.file.write(f'{self.make_indents()}@{decorator}\n')
            return
        named_args: List[str] = [f'{name} = {value}' for name, value in named_args]
        args.extend(named_args)
        arguments = ', '.join(args)
        self.file.write(f'{self.make_indents()}@{decorator}({arguments})\n')
        
    def append_function(self, name: str, return_type: str, 
                        args: List[Tuple[str, str]], 
                         named_args: List[Tuple[str, str]],
                         kwargs: bool = False, has_body: bool = False): 
        assert self.file and not self.file.closed

        named_args: List[str] = [f'{name} = {value}' for name, value in named_args]
        arguments: List[str] = [f'{name}: {value}' if value != '' else name for name, value in args]
        arguments.extend(named_args)
        if kwargs:
            arguments.append('**kwargs')
        arguments = ', '.join(arguments)
        if len(return_type) == 0:
            self.file.write(f'{self.make_indents()}def {name}({arguments}):')
        else:
            self.file.write(f'{self.make_indents()}def {name}({arguments}) -> {return_type}:')
        if not has_body:
            self.file.write(' ...\n\n')
            
    def append_class(self, name: str, base: str = ''):
        assert self.file and not self.file.closed
        
        if base == '':
            self.file.write(f'{self.make_indents()}class {name}:\n')
        else:
            self.file.write(f'{self.make_indents()}class {name}({base}):\n')
        
    def append_field(self, name: str, type: str = '', value: str = ''):
        assert self.file and not self.file.closed
        
        if value != '':
            value = f' = {value}'
        
        if type != '':
            type = f': {type}'
            
        self.file.write(f'{self.make_indents()}{name}{type}{value}\n')
        
    def append(self, string: str, not_breakline: bool = False):
        assert self.file and not self.file.closed
        
        if not not_breakline:
            string += '\n'
            
        self.file.write(string)
        
    def append_newline(self):
        assert self.file and not self.file.closed
        
        self.file.write('\n')
        
    def append_comment(self, comment: str = '', not_breakline: bool = False):
        assert self.file and not self.file.closed
        
        end = '\n' if not not_breakline else ''
        
        if len(comment) != 0:
            self.file.write(f'# {comment}{end}')
        else:
            self.file.write(f'#{end}')
        
    def append_virtdelegate(self, args: List[str]):
        assert self.file and not self.file.closed
        
        arguments = ', '.join(args)
        self.file.write(f'\n{self.make_indents()}{self.INDENT}return self.virt_delegate({arguments})\n\n')
        
    def append_external_delegate(self, args: List[str]):
        assert self.file and not self.file.closed
        
        arguments = ', '.join(args)
        self.file.write(f'\n{self.make_indents()}{self.INDENT}return delegate({arguments})\n\n')
    
    def make_indents(self) -> str:
        return self.indents * self.INDENT
    
    def indent(self): self.indents += 1
    
    def unindent(self): self.indents -= 1