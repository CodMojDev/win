import xml.sax
import time
import os
import io

class OpenGLFeatureOrExt:
    requires: list[tuple[str, str]]
    number: str
    
    def __init__(self, number: str):
        self.requires = []
        self.number = number
        
class OpenGLCommand:
    arguments: list[tuple[str, str]]
    
    name: str
    ret: str
    
    def __init__(self):
        self.arguments = []
        
        self.name = ''
        self.ret = ''

class SAXOpenGLSpecParser(xml.sax.ContentHandler):
    destination: str
    section: str | None
    
    features: dict[str, OpenGLFeatureOrExt]
    enums: dict[str, str]
    commands: dict[str, OpenGLCommand]
    extensions: dict[str, OpenGLFeatureOrExt]
    
    last_feature: OpenGLFeatureOrExt | None
    last_command: OpenGLCommand | None
    
    subcommand: str | None
    protocommand: str | None
    protokind: str | None
    
    def __init__(self):
        super().__init__()
        
        self.destination = os.path.join(os.path.dirname(__file__), '../abs/gl')
        self.section = None
        
        self.features = {}
        self.enums = {}
        self.commands = {}
        self.extensions = {}
        
        self.last_feature = None
        self.last_command = None
        
        self.subcommand = None
        self.protocommand = None
        self.protokind = None
        
    def startElement(self, name, attrs):
        if name in ('enums', 'commands', 'feature', 'extensions'):
            self.section = name
            if name == 'feature':
                self.last_feature = OpenGLFeatureOrExt(attrs['api']+'_'+attrs['number'])
        elif name == 'command':
            if self.section == 'commands':
                self.last_command = OpenGLCommand()
            elif self.section in ('feature', 'extensions'):
                if self.subcommand == 'require':
                    self.last_feature.requires.append(('command', attrs['name']))
                elif self.subcommand == 'remove':
                    try:
                        self.last_feature.requires.remove(('command', attrs['name']))
                    except: pass
        elif name == 'enum':
            if self.section == 'enums':
                self.enums[attrs['name']] = attrs['value']
            elif self.section in ('feature', 'extensions'):
                if self.subcommand == 'require':
                    self.last_feature.requires.append(('enum', attrs['name']))
                elif self.subcommand == 'remove':
                    try:
                        self.last_feature.requires.remove(('enum', attrs['name']))
                    except: pass
        elif name in ('require', 'remove', 'param', 'proto', 'extension'):
            self.subcommand = name
            if name == 'proto':
                self.protokind = attrs.get('kind', None)
            elif name == 'param':
                self.last_command.arguments.append(('', ''))
            elif name == 'extension':
                self.last_feature = OpenGLFeatureOrExt(attrs['name'])
        elif name in ('ptype', 'name'):
            self.protocommand = name
        
    def endElement(self, name):
        if name == 'command' and self.section == 'commands':
            self.commands[self.last_command.name] = self.last_command
            self.last_command = None
        elif name == 'feature':
            self.features[self.last_feature.number] = self.last_feature
            self.last_feature = None
        elif name in ('commands', 'types', 'enums'):
            self.section = None
        elif name in ('require', 'remove', 'param', 'proto'):
            self.subcommand = None
            if name == 'proto':
                self.protokind = None
        elif name in ('ptype', 'name'):
            self.protocommand = None
        elif name == 'extension':
            self.extensions[self.last_feature.number] = self.last_feature
            self.last_feature = None
    
    def characters(self, content):
        if self.section == 'commands' and self.last_command is not None:
            if self.subcommand == 'proto':
                if self.protocommand is None or self.protocommand == 'ptype':
                    if self.protokind == 'String':
                        self.last_command.ret = 'LPSTR'
                    else:
                        self.last_command.ret += content
                elif self.protocommand == 'name':
                    self.last_command.name += content
            elif self.subcommand == 'param':
                if self.protocommand is None or self.protocommand == 'ptype':
                    name, ty = self.last_command.arguments[-1]
                    ty += content
                    self.last_command.arguments[-1] = (name, ty)
                elif self.protocommand == 'name':
                    _, ty = self.last_command.arguments[-1]
                    self.last_command.arguments[-1] = (content, ty)

def gen_argument(ty: str) -> str:
    ty = ty.removeprefix('const ').removeprefix('struct ').removesuffix('const').strip()
    if ty.endswith('*'):
        return 'PTR('+gen_argument(ty[:-1])+')'
    if ty in ('void', 'GLvoid'):
        return 'VOID'
    return ty

def gen_argument_py(ty: str, p: bool) -> str:
    ty = ty.removeprefix('const ').removeprefix('struct ').removesuffix('const').strip()
    if ty.endswith('*'):
        return 'IPointer['+gen_argument_py(ty[:-1], True)+']'
    if p: 
        if ty in ('void', 'GLvoid'):
            return 'int'
        return ty
    if ty in ('GLint', 'GLuint', 'GLbyte', 'GLubyte',
              'GLshort', 'GLushort', 'GLhalf', 'GLhalfARB',
              'GLfixed', 'khronos_int8_t', 'khronos_uint8_t',
              'khronos_int16_t', 'khronos_uint16_t',
              'GLclampx', 'GLeglImageOES', 'GLeglClientBufferEXT',
              'GLintptr', 'GLintptrARB', 'GLsizeiptr', 
              'GLsizeiptrARB', 'GLint64', 'GLint64EXT',
              'GLuint64', 'GLuint64EXT', 'GLsync', 'GLhalfNV',
              'GLvdpauSurfaceNV', 'GLhandleARB', 'GLsizei',
              'GLbitfield', 'GLboolean', 'GLenum'):
        return 'int'
    if ty in ('GLclampf', 'GLclampd', 'GLdouble', 'GLfloat'):
        return 'float'
    if ty in ('GLDEBUGPROC', 'GLDEBUGPROCARB',
              'GLDEBUGPROCKHR', 'GLDEBUGPROCAMD',
              'GLVULKANPROCNV'):
        return 'FARPROC'
    if ty in ('void', 'GLvoid'):
        return 'None'
    return ty

def gen_command(p: SAXOpenGLSpecParser, file: io.TextIOWrapper, command: OpenGLCommand):
    if ('command', command.name) in p.features['gl_1.1'].requires or ('command', command.name) in p.features['gl_1.0'].requires:
        decorator = 'opengl32.foreign'
    else:
        decorator = 'GLExtAPI.method'
    ret = gen_argument(command.ret.strip())
    ret_py = gen_argument_py(command.ret.strip(), False)
    arguments = []
    for name, ty in command.arguments:
        ty = ty.strip()
        py = gen_argument_py(ty, False)
        arguments.append((gen_argument(ty), py, name))
    file.write(f'    @{decorator}({ret}, ')
    for i, (ty, *_) in enumerate(arguments):
        if i != len(arguments)-1:
            ty += ', '
        file.write(ty)
    file.write(')\n')
    file.write(f'    def {command.name}(')
    for i, (_, ty, name) in enumerate(arguments):
        text = f'{name}: {ty}'
        if i != len(arguments)-1:
            text += ', '
        file.write(text)
    file.write(f') -> {ret_py}: pass\n\n')

def gen_versions(p: SAXOpenGLSpecParser, v: list[str], d: str):
    for version in v:
        feature = p.features.get(version, None)
        if feature is None:
            print(f'No OpenGL version/feature "{version}".')
        else:
            with open(os.path.join(d, version.replace('_', '').replace('.', '')+'.py'), 'w', encoding='utf-8') as file:
                file.write(f'#\n'
                           f'# This file generated by a Win.Tools.GLGen generator as a part of the Win project.\n'
                           f'# Definitions for the OpenGL {version}, do not change this file\n'
                           f'# Date/Time of a generation: {time.ctime()}\n'
                           f'#\n\n')
                file.write('# OpenGL Imports\n'
                           'from win.gl.gl import *\n'
                           'from win.gl.glu import *\n'
                           'from win.abs.glext import *\n\n')
                file.write('# Basic OpenGL Types definitions\n'
                           'khronos_int8_t = GLbyte\n'
                           'khronos_uint8_t = GLubyte\n'
                           'khronos_int16_t = GLshort\n'
                           'khornos_uint16_t = GLushort\n'
                           'GLclampx = UINT32\n'
                           'GLeglClientBufferEXT = PVOID\n'
                           'GLeglImageOES = PVOID\n'
                           'GLchar = CHAR\n'
                           'GLcharARB = CHAR\n'
                           'GLhandleARB = UINT\n'
                           'GLhalf = UINT16\n'
                           'GLhalfARB = UINT16\n'
                           'GLfixed = INT32\n'
                           'GLintptr = INT_PTR\n'
                           'GLintptrARB = INT_PTR\n'
                           'GLsizeiptr = SSIZE_T\n'
                           'GLsizeiptrARB = SSIZE_T\n'
                           'GLint64 = INT64\n'
                           'GLint64EXT = INT64\n'
                           'GLuint64 = UINT64\n'
                           'GLuint64EXT = UINT64\n'
                           'GLsync = PVOID\n'
                           'GLDEBUGPROC = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                           'GLDEBUGPROCARB = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                           'GLDEBUGPROCKHR = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                           'GLDEBUGPROCAMD = APIENTRY(VOID, GLuint, GLenum, GLenum, GLsizei, LPSTR, PVOID)\n'
                           'GLhalfNV = USHORT\n'
                           'GLvdpauSurfaceNV = GLintptr\n'
                           'GLVULKANPROCNV = APIENTRY(VOID)\n\n')
                file.write(f'class {version.replace("_", "").replace(".", "").upper()}:\n')
                file.write('    #\n    # Enum definitions\n    #\n\n')
                for ty, name in feature.requires:
                    if ty == 'enum':
                        file.write(f'    {name} = {p.enums[name]}\n')
                file.write('\n')
                file.write('    #\n    # Function/Command definitions\n    #\n\n')
                for ty, name in feature.requires:
                    if ty == 'command':
                        gen_command(p, file, p.commands[name])

def gen_extensions(p: SAXOpenGLSpecParser, e: list[str], d: str):
    with open(os.path.join(d, 'extensions.py'), 'w', encoding='utf-8') as file:
        file.write(f'#\n'
                    f'# This file generated by a Win.Tools.GLGen generator as a part of the Win project.\n'
                    f'# Definitions for the OpenGL Extensions, do not change this file\n'
                    f'# Date/Time of a generation: {time.ctime()}\n'
                    f'#\n\n')
        file.write('# OpenGL Imports\n'
                    'from win.gl.gl import *\n'
                    'from win.gl.glu import *\n'
                    'from win.abs.glext import *\n\n')
        file.write('# Basic OpenGL Types definitions\n'
                    'khronos_int8_t = GLbyte\n'
                    'khronos_uint8_t = GLubyte\n'
                    'khronos_int16_t = GLshort\n'
                    'khronos_uint16_t = GLushort\n'
                    'GLclampx = UINT32\n'
                    'GLeglClientBufferEXT = PVOID\n'
                    'GLeglImageOES = PVOID\n'
                    'GLchar = CHAR\n'
                    'GLcharARB = CHAR\n'
                    'GLhandleARB = UINT\n'
                    'GLhalf = UINT16\n'
                    'GLhalfARB = UINT16\n'
                    'GLfixed = INT32\n'
                    'GLintptr = INT_PTR\n'
                    'GLintptrARB = INT_PTR\n'
                    'GLsizeiptr = SSIZE_T\n'
                    'GLsizeiptrARB = SSIZE_T\n'
                    'GLint64 = INT64\n'
                    'GLint64EXT = INT64\n'
                    'GLuint64 = UINT64\n'
                    'GLuint64EXT = UINT64\n'
                    'GLsync = PVOID\n'
                    'GLDEBUGPROC = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                    'GLDEBUGPROCARB = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                    'GLDEBUGPROCKHR = APIENTRY(VOID, GLenum, GLenum, GLuint, GLenum, GLsizei, LPSTR, PVOID)\n'
                    'GLDEBUGPROCAMD = APIENTRY(VOID, GLuint, GLenum, GLenum, GLsizei, LPSTR, PVOID)\n'
                    'GLhalfNV = USHORT\n'
                    'GLvdpauSurfaceNV = GLintptr\n'
                    'GLVULKANPROCNV = APIENTRY(VOID)\n'
                    'class _cl_context(CStructure): _fields_ = []\n'
                    'class _cl_event(CStructure): _fields_ = []\n\n')
        for extension in e:
            feature = p.extensions.get(extension, None)
            if feature is None:
                print(f'No OpenGL extension "{extension}".')
            else:
                file.write(f'class {extension}:\n')
                if not feature.requires:
                    file.write('    pass\n\n')
                else:
                    for ty, name in feature.requires:
                        if ty == 'enum':
                            file.write(f'    {name} = {p.enums[name]}\n')
                    file.write('\n')
                    for ty, name in feature.requires:
                        if ty == 'command':
                            gen_command(p, file, p.commands[name])

def main():
    gl_file = input('Enter the OpenGL Specification XML File path: ')
    if not os.path.exists(gl_file):
        print('Not found.')
    elif not os.path.isfile(gl_file):
        print('Entered path is a directory, not an XML file.')
    else:
        versions = input('Enter the OpenGL Versions for generate (delimited with space): ').lower()
        extensions = input('Enter the OpenGL Extensions for generate (delimited with space): ')
        while extensions.find('  ') != -1:
            extensions = extensions.replace('  ', ' ')
        versions = versions.split()
        extensions = extensions.split()
        verdir = input('Enter the OpenGL Version Files directory: ')
        os.makedirs(verdir, exist_ok=True)
        if not os.path.isdir(verdir):
            print('Entered path is a file, but expected directory.')
        else:
            extdir = input('Enter the OpenGL Extensions Files directory: ')
            os.makedirs(extdir, exist_ok=True)
            if not os.path.isdir(extdir):
                print('Entered path is a file, but expected directory.')
            else:
                try:
                    parser = SAXOpenGLSpecParser()
                    with open(gl_file, 'r') as gl_descriptor:
                        data = gl_descriptor.read()
                    xml.sax.parseString(data, parser)
                    gen_versions(parser, versions, verdir)
                    gen_extensions(parser, extensions, extdir)
                except Exception as e:
                    print(f'Exception ocurred while parsing OpenGL Specification: {e}')

if __name__ == '__main__':
    main()