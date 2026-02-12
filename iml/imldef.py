#
# Core interface defines for IML (Instruction Markup Language).
# IML provides base layer to define IML-based language parsers. 
# (IML - is language standard, not language)
#

from typing import ClassVar, TypeVar
from ..defbase import *

import re
import io

class IIMLContext(IInterface):
    last_lineno: int
    last_line: str
    
    tokens_length: int
    tokens: list[str]
    
    def __init__(self): 
        self.last_lineno = 0
        self.last_line = ''
        
        self.tokens_length = 0
        self.tokens = []
        
        if not self.is_abstract(self.on_initialize):
            self.on_initialize()
        
    @interface_abstract_method
    def on_initialize(self):
        ...

WT_IMLCONTEXT = TypeVar('WT_IMLCONTEXT', bound=IIMLContext)

class IIMLParser(IInterface):
    context_type: ClassVar[WT_IMLCONTEXT]
    
    file: io.TextIOWrapper
    context: WT_IMLCONTEXT
    
    def __init__(self, file_path: str):
        self.file = open(file_path, 'r', encoding='utf-8')
        self.context = self.context_type()
        
        if not self.is_abstract(self.on_initialize):
            self.on_initialize()
        
    @staticmethod
    def recursive_replace(string: str, find: str, replace: str) -> str:
        while string.find(find) != -1:
            string = string.replace(find, replace)
        return string
    
    def syntax_error(self, msg: str, charno: int = -1):
        if not self.is_abstract(self.on_syntax_error):
            self.on_syntax_error()
            
        raise SyntaxError(msg, (self.file.name, self.context.last_lineno, 
                                charno, self.context.last_line))
        
    @interface_abstract_method
    def on_initialize(self):
        ...
        
    @interface_abstract_method
    def on_syntax_error(self):
        ...
    
    @interface_abstract_method
    def on_instruction(self, instruction: str, lineno: int) -> bool: 
        ...
        
    @interface_abstract_method
    def on_line(self, line: str, lineno: int) -> str:
        ...
        
    @interface_abstract_method
    def on_parse_started(self):
        ...
        
    @interface_abstract_method
    def on_parse_ended(self):
        ...
        
    @interface_abstract_method
    def on_empty_line(self):
        ...
        
    @interface_abstract_method
    def on_tokens_defined(self):
        ...
        
    @interface_abstract_method
    def on_unknown_instruction(self) -> bool:
        ...
        
    def parse(self):
        if self.file.closed:
            self.file = open(self.file.name, 'r', encoding='utf-8')
        
        if not self.is_abstract(self.on_parse_started):
            self.on_parse_started()
        
        contents = self.file.read()
        contents = re.sub(r'/\*.*\*/', '', contents, flags=re.DOTALL)
        
        lines = contents.split('\n')
        lines_length: int = len(lines)
        if lines_length == 0: self.syntax_error('Empty IML File.')
        
        if lines_length > 1:
            for lineno, line in enumerate(lines):
                line = re.sub('//.*', '', line)
                
                self.context.last_lineno = lineno
                self.context.last_line = line
                
                if not self.is_abstract(self.on_line):
                    line = self.on_line(line, lineno)
                    
                if line is not None:
                    tokens = line.split()
                    tokens_length = len(tokens)
                    
                    self.context.tokens = tokens
                    self.context.tokens_length = tokens_length
                    
                    if not self.is_abstract(self.on_tokens_defined):
                        self.on_tokens_defined()
                    
                    if tokens_length == 0:
                        if not self.is_abstract(self.on_empty_line):
                            self.on_empty_line()
                        continue
                    
                    if not self.on_instruction(self.context.tokens[0]):
                        if self.is_abstract(self.on_unknown_instruction) or not self.on_unknown_instruction():
                            self.syntax_error(f'Unknown instruction "{self.context.tokens[0]}".')
        
        if not self.is_abstract(self.on_parse_ended):
            self.on_parse_ended()