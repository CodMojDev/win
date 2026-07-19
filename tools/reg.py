from win.com.facade import *

import sys

def main():
    factory = FacadeFactory()

    if '-reg' in sys.argv:
        reg_pos = sys.argv.index('-reg')
        class_name, script_name = sys.argv[reg_pos:reg_pos+2]
        if len(sys.argv)-1 != reg_pos+2:
            progid = sys.argv[reg_pos+3]
        else:
            progid = None
        RegisterCLSID(class_name, script_name, progid)
    elif '-renew' in sys.argv:
        renew_pos = sys.argv.index('-renew')
        RenewFacade(sys.argv[renew_pos+1])
    elif '-guid' in sys.argv:
        print(GUID.new())

def RegisterCLSID(class_name: str, script_name: str, progid: str | None = None):
    factory.RegisterCLSID(class_name, os.path.abspath(script_name), progid)
    print(f'Successfully registered CLSID under name "{class_name}", server {script_name}!')

def RenewFacade(script_name: str):
    print(factory.Facade(os.path.abspath(script_name)))
    
if __name__ == '__main__': main()