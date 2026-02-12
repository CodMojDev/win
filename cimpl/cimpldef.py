#
# CIMPL core defines
# <!> under construction
#

from ..defbase_assembly import *
from typing import Generic
from .. import cpreproc
from enum import Enum
from ctypes import *

import keystone as ks

class CImplConvention(Enum):
    FASTCALL = 0
    STDCALL = 1
    CDECL = 2

class CImplContext:
    _is_started: bool
    win64: bool
    code: str
    
    def __init__(self):
        self.win64 = cpreproc.defined('_WIN64')
        self._is_started = False
        self.code = ''
        
    def add_line(self, line: str):
        if self._is_started:
            self._is_started = False
            self.code += line
        else:
            self.code += '\n' + line
        
class CImplContainer(Generic[WT]):
    contained: WT
    
    def __init__(self, contained: WT):
        self.contained = contained
        
class CImplByte(CImplContainer[int]): ...

class CImplWord(CImplContainer[int]): ...

class CImplDword(CImplContainer[int]): ...
        
class CImplQword(CImplContainer[int]): ...
        
class CImplInstruction:
    UNKNOWN = -1
    INVOKE = 0
    RETURN = 1
    ASSEMBLY = 2
    
    data: list
    tag: int
    
    def __init__(self, data: list, tag: int = UNKNOWN):
        self.data = data
        self.tag = tag
        
    def __eq__(self, tag: int):
        if not isinstance(tag, int): return NotImplemented
        return self.tag == tag
    
    def format(self) -> str:
        match self.tag:
            case self.UNKNOWN: return 'UNKNOWN'
            case self.INVOKE: return 'INVOKE'
            case self.RETURN: return 'RETURN'
            case self.ASSEMBLY: return 'ASSEMBLY'
            case _: 
                self.tag = self.UNKNOWN
                return 'UNKNOWN'
        
class CImplString: 
    allocation_address: WT_ADDRLIKE
    allocator: IAllocator
    string: str
    
    def __init__(self, string: str, allocator: IAllocator = CLocalAllocator()):
        string_length = (len(string) + 1) << 1
        string_buffer = create_unicode_buffer(string, string_length)
        string_allocation = allocator.allocate(string_length)
        allocator.copy(string_allocation, string_buffer, string_length)
        self.allocation_address = string_allocation
        self.allocator = allocator
        self.string = string
    
    def __repr__(self) -> str:
        return  f'<CImplString allocator={self.allocator}, ' \
                f'string="{self.string}", ' \
                f'allocated at {format_hex(PtrUtil.get_address(
                    self.allocation_address), sizeof(c_void_p))}>'
                    
    def __del__(self):
        self.allocator.deallocate(self.allocation_address)
        
BIT32 = 2**32-1
BIT64 = 2**64-1
        
class CImplFunction:
    convention: CImplConvention
    has_ret: bool
    name: str
    
    instructions: list[CImplInstruction]
    function_space: int
    has_frame: bool
    
    def __init__(self):
        if cpreproc.ifdef('_WIN64'):
            self.convention = CImplConvention.FASTCALL
        else:
            self.convention = CImplConvention.CDECL
        
        self.instructions = []
        self.name = 'unknown_function'
        self.function_space = 0
        self.has_frame = True
        self.has_ret = True
    
    def write(self, context: CImplContext):
        have_invokes = False
        for instruction in self.instructions:
            if instruction == CImplInstruction.INVOKE:
                have_invokes = True
                break
        
        
        if context.win64 and have_invokes:
            if have_invokes:
                context.add_line(f'sub rsp, {self.function_space}')
                
        if self.has_frame:
            if context.win64:
                context.add_line('push rbp')
                context.add_line('mov rbp, rsp')
            else:
                context.add_line('push ebp')
                context.add_line('mov ebp, esp')
        
        for i_no, instruction in enumerate(self.instructions):
            instruction_data = instruction.data.copy()
            if instruction == CImplInstruction.RETURN:
                return_value = instruction_data.pop(0)
                
                if isinstance(return_value, int):
                    if not context.win64 and return_value > BIT32:
                        raise SystemError(f'Returned 64-bit value but system is not 64-bit. '
                                          f'Instruction RETURN at {i_no}.')
                        
                    if return_value == 0:
                        if context.win64:
                            context.add_line('xor rax, rax')
                        else:
                            context.add_line('xor eax, eax')
                    elif return_value > BIT32:
                        context.add_line(f'mov rax {return_value}')
                    else:
                        context.add_line(f'mov eax {return_value}')
                        
            elif instruction == CImplInstruction.INVOKE:
                address = instruction_data.pop(0)
                address = PtrUtil.get_address(address)
                
                if not context.win64 and address > BIT32:
                    raise SystemError(f'Invoked 64-bit function address but system is not 64-bit. '
                                      f'Instruction INVOKE at {i_no}.')
                
                if len(instruction_data) == 0 or not isinstance(instruction_data[0], CImplConvention):
                    if context.win64:
                        convention = CImplConvention.FASTCALL
                    else:
                        convention = CImplConvention.CDECL
                else:
                    convention = instruction_data.pop(0)
                
                if convention == CImplConvention.FASTCALL:
                    if context.win64:
                        for arg_no, argument in enumerate(instruction_data):
                            if not isinstance(argument, CImplContainer):
                                raise ValueError(f'Argument is not a container. '
                                                 f'Instruction INVOKE at {i_no}. '
                                                 f'Argument at {arg_no}.')
                            
                            if argument.contained > BIT64:
                                raise ValueError(f'Too big argument value (bigger than 64-bit). '
                                                 f'Instruction INVOKE at {i_no}. '
                                                 f'Argument at {arg_no}.')
                            
                            if arg_no > 3:
                                context.add_line(f'mov rax, {hex(argument.contained)}')
                                context.add_line(f'push rax')
                            else:
                                match arg_no:
                                    case 0:
                                        register = 'rcx'
                                    case 1:
                                        register = 'rdx'
                                    case 2:
                                        register = 'r8'
                                    case 3:
                                        register = 'r9'
                                if argument.contained == 0:
                                    context.add_line(f'xor {register}, {register}')
                                else:
                                    context.add_line(f'mov {register}, {hex(argument.contained)}')
                    else: 
                        for arg_no, argument in enumerate(instruction_data):
                            if not isinstance(argument, CImplContainer):
                                    raise ValueError(f'Argument is not a container. '
                                                    f'Instruction INVOKE at {i_no}. '
                                                    f'Argument at {arg_no}.')
                                
                            if argument.contained > BIT64:
                                    raise ValueError(f'Too big argument value (bigger than 64-bit) '
                                                    f'(System is 32-bit). '
                                                    f'Instruction INVOKE at {i_no}. '
                                                    f'Argument at {arg_no}.')
                                
                            if argument.contained > BIT32 or isinstance(argument, CImplQword):
                                raise SystemError(f'Argument value is 64-bit, but system is not 64-bit. '
                                                f'Instruction INVOKE at {i_no}. '
                                                f'Argument at {arg_no}.')
                                
                            if arg_no > 1:
                                context.add_line(f'push {hex(argument.contained)}')
                            else:
                                match arg_no:
                                    case 0:
                                        register = 'ecx'
                                    case 1:
                                        register = 'edx'
                                if argument.contained == 0:
                                    context.add_line(f'xor {register}, {register}')
                                else:
                                    context.add_line(f'mov {register}, {hex(argument.contained)}')
                                    
                elif convention == CImplConvention.CDECL and not context.win64:
                    args_size: int = 0
                    for arg_no, argument in enumerate(instruction_data):
                        if not isinstance(argument, CImplContainer):
                                raise ValueError(f'Argument is not a container. '
                                                f'Instruction INVOKE at {i_no}. '
                                                f'Argument at {arg_no}.')
                            
                        if argument.contained > BIT64:
                                raise ValueError(f'Too big argument value (bigger than 64-bit) '
                                                 f'(System is 32-bit). '
                                                f'Instruction INVOKE at {i_no}. '
                                                f'Argument at {arg_no}.')
                            
                        if argument.contained > BIT32 or isinstance(argument, CImplQword):
                            raise SystemError(f'Argument value is 64-bit, but system is not 64-bit. '
                                            f'Instruction INVOKE at {i_no}. '
                                            f'Argument at {arg_no}.')
                            
                        if isinstance(argument, CImplByte): args_size += 1
                        if isinstance(argument, CImplWord): args_size += 2
                        if isinstance(argument, CImplDword): args_size += 4
                            
                        context.add_line(f'push {hex(argument.contained)}')
                            
                elif convention == CImplConvention.STDCALL and not context.win64:
                    for arg_no, argument in enumerate(instruction_data):
                        if not isinstance(argument, CImplContainer):
                                raise ValueError(f'Argument is not a container. '
                                                 f'Instruction INVOKE at {i_no}. '
                                                 f'Argument at {arg_no}.')
                            
                        if argument.contained > BIT64:
                                raise ValueError(f'Too big argument value (bigger than 64-bit) '
                                                 f'(System is 32-bit). '
                                                 f'Instruction INVOKE at {i_no}. '
                                                 f'Argument at {arg_no}.')
                            
                        if argument.contained > BIT32 or isinstance(argument, CImplQword):
                            raise SystemError(f'Argument value is 64-bit, but system is not 64-bit. '
                                             f'Instruction INVOKE at {i_no}. '
                                             f'Argument at {arg_no}.')
                            
                        context.add_line(f'push {hex(argument.contained)}')
                
                if address > BIT32:
                    context.add_line(f'mov rax, {hex(address)}')
                    context.add_line('call rax')
                else:
                    context.add_line(f'call dword ptr [{hex(address)}]')
                
                if convention == CImplConvention.CDECL and not context.win64:
                    context.add_line(f'add esp, {args_size}')
            elif instruction == CImplInstruction.ASSEMBLY:
                context.add_line(instruction_data.pop(0))
            else:
                raise RuntimeError(f'Unknown instruction {instruction.format()} at {i_no}.')
                        
        if have_invokes:
            context.add_line(f'add rsp, {self.function_space}')
            
        if self.has_frame:
            if context.win64:
                context.add_line('mov rsp, rbp')
                context.add_line('pop rbp')
            else:
                context.add_line('mov esp, ebp')
                context.add_line('pop ebp')
                        
        if self.has_ret:
            context.add_line('ret')
            
class CImplAssembly: 
    assembly: CAssembly
    ks_instance: ks.Ks
    
    def __init__(self, is_32: bool = cpreproc.defined('_WIN32'), 
                 allocator: IAllocator = CLocalAllocator()):
        if is_32:
            self.ks_instance = ks.Ks(ks.KS_ARCH_X86, ks.KS_MODE_32)
        else:
            self.ks_instance = ks.Ks(ks.KS_ARCH_X86, ks.KS_MODE_64)
        self.assembly = CAssembly(allocator)
    
    def apply_context(self, context: CImplContext):
        machine_code, _ = self.ks_instance.asm(context.code, as_bytes=True)
        self.assembly.buffer = machine_code
        self.assembly.allocate()
        
    def address(self) -> int:
        return self.assembly.executable