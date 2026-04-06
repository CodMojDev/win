from win.com.icl.wicl.parser import *
    
make_library = 'build'
os.makedirs(make_library, exist_ok=True)
    
for file_name in os.listdir(os.curdir):
    if os.path.splitext(file_name)[-1] == '.icl':
        parser = ICLParser(file_name)
        parser.parse()
        try: os.rename(parser.code.file.name, os.path.join(make_library, parser.code.file.name))
        except FileExistsError: 
            os.remove(os.path.join(make_library, parser.code.file.name))
            os.rename(parser.code.file.name, os.path.join(make_library, parser.code.file.name))