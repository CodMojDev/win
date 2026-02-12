from .comdefbase import *

oleacc = get_win_library('oleacc.dll')

def oleacc_foreign(*args: type, 
            name: Optional[str] = None,
            intermediate_method: bool = False) -> Callable:
        """
        Foreign method declare
        """
        return foreign_optimized(HRESULT, 
                                 *args,
                                 library=oleacc, 
                                 name=name, 
                                 intermediate_method=intermediate_method)