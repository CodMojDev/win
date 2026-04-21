from win.com.comdefbase import *

class WRPCException(RuntimeError): 
    def __init__(self, exceptions: list[tuple[str, str]] = []):
        if not exceptions:
            super().__init__('RPC Generic Exception')
        else:
            exception_text = ''
            for i, (type_name, text) in enumerate(exceptions):
                exception_text += f'Exception #{i+1} {type_name}: {text}\n'
            exception_text += 'Several RPC Exceptions ocurred'
            super().__init__(exception_text)

class WRPCProtocolException(RuntimeError): ...