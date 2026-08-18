#
# Definitions for WinAbs Theme file (.WAT)
#


#
# WAT Header
#
# CHAR Magic[4] // "WATI"
# DWORD OffsetToResources
# DWORD OffsetToData
# DWORD OffsetToSchemaTable
#

WAT_SCHEMA_TYPE_BUTTON = 1
WAT_SCHEMA_TYPE_EDIT = 2
WAT_SCHEMA_TYPE_WINDOW = 3
WAT_SCHEMA_TYPE_DIALOG = 4
WAT_SCHEMA_TYPE_TOOLBAR = 5
WAT_SCHEMA_TYPE_MENU = 6
WAT_SCHEMA_TYPE_FRAME = 7
WAT_SCHEMA_TYPE_PROPERTYGRID = 8
WAT_SCHEMA_TYPE_LISTBOX = 9
WAT_SCHEMA_TYPE_COMBOBOX = 10
WAT_SCHEMA_TYPE_LISTVIEW = 11
WAT_SCHEMA_TYPE_TREEVIEW = 12
WAT_SCHEMA_TYPE_LISTHEADER = 13
WAT_SCHEMA_TYPE_STATIC = 14
WAT_SCHEMA_TYPE_TAB = 15
WAT_SCHEMA_TYPE_CUSTOM = 65535

#
# Schema Table
#
# DWORD SchemaCount
# WAT_SCHEMA Schemas[SchemaCount]
#

#
# Schema
#
# WORD Type
# DWORD Spec
# DWORD OffsetToResource
#

#
# Data table
#
# The string resources is stored by zero-terminated string.
# The binary resources is stored by DWORD length-prefixed data.
#