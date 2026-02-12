from typing import List
from .wpdbbase import *

class WPDBDocumentation:
    data: str

class WPDBFunctionArgument:
    argument_type: int
    argument_name: int

class WPDBFunction:
    doc: WPDBDocumentation
    name: int

class WPDB:
    functions: List[WPDBFunction]
    constant_pool: List[str]
    accessor: WPDBFile