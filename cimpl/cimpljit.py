from ..iml.imldef import *
from .cimpldef import *

class CImplJITServer:
    held: dict[str, Any]
    
    def __init__(self, held: dict = {}):
        self.held = held
    
class CImplJITParser(IIMLParser):
    class CImplJITContext(IIMLContext):
        defining_function: CImplFunction
        
        def on_initialize(self):
            self.defining_function = None
        
    VERSION = '100'
        
    context_type = CImplJITContext
    context: CImplJITContext
    server: CImplJITServer
    
    def on_initialize(self):
        self.server = None
        
    def on_line(self, line: str, lineno: int) -> str:
        if lineno == 0:
            if not line.startswith('.cimpl'):
                self.syntax_error('CIMPL Header is corrupted.', 1)
        
            return None

        line = line.strip()
            
        return line
        
    def on_directive(self, directive: str) -> bool:
        if directive == 'noframe':
            self.context.defining_function.has_frame = False
        elif directive == 'noret':
            self.context.defining_function.has_ret = False
        else:
            return False
        return True
        
    def on_instruction(self, instruction: str, lineno: int) -> bool:
        if instruction.startswith('.'):
            if instruction == '.ver':
                if self.context.tokens[1] != self.VERSION:
                    self.syntax_error(f'CIMPL Version is not {self.VERSION}. Update the CIMPL File.', 
                                    len(instruction) + 2)
            if self.context.defining_function is None:
                self.syntax_error('Directive is not supported outside a function.')
            return self.on_directive(instruction[1:])
        elif instruction == 'invoke':
            if self.context.defining_function is None:
                self.syntax_error('Invoke is not supported outside a function.')
        elif instruction == '}':
            if self.context.defining_function is not None:
                self.context.defining_function = None
        elif instruction == 'serverholder':
            self.held_by_server()
        elif instruction == 'function':
            ...
        elif instruction == 'return':
            self.return_value()
        else:
            return False
        return True
    
    def return_value(self):
        if self.context.defining_function is None:
            self.syntax_error('Return statement is not supported outside a function.')
            
        if not self.context.defining_function.has_ret:
            self.syntax_error('Tried to return value, but function does not has "ret" instruction '
                              '(.noret directive used).')
            
        if self.context.tokens_length == 1:
            self.syntax_error('Incorrect return statement, '
                              'missing return value.')
            
        return_value = self.context.tokens[1]
        if return_value.startswith('0x'):
            return_value = int(return_value, 16)
        elif return_value.endswith('h') and return_value[0].isdigit():
            return_value = int(return_value[:-1], 16)
        else:
            if return_value in ...: ...
            
    def held_by_server(self):
        ...