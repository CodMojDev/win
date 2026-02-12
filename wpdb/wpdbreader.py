from .wpdbenums import *
from .wpdbbase import *

class WPDBReader(WPDBFile):
    _mode_ = 'r'
    
    def validate_header(self):
        self.file.seek(0)
        header = self.file.read(4)
        if header != b'WPDB':
            raise ValueError('Invalid header of WPDB file.')
        
    def read_entry(self): 
        buffer = self.file.read(WPDBEntryType.size())
        entry_type = WPDBEntryType.unserialize(buffer)
        if entry_type == WPDBEntryType.WPDB_FUNCTION:
            ...
        elif entry_type == WPDBEntryType.WPDB_TYPELIST:
            ...