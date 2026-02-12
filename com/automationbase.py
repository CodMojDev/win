from .comdefbase import *

oleaut32 = get_win_library('oleaut32.dll')

def oleaut_foreign(*args: type, 
            name: Optional[str] = None,
            intermediate_method: bool = False) -> Callable:
        """
        Foreign method declare
        """
        return foreign_optimized(HRESULT, 
                                 *args,
                                 library=oleaut32, 
                                 name=name, 
                                 intermediate_method=intermediate_method)
        
