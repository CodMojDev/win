from .io import *

#
# Definitions for WinAbs Resource file (.WAR)
#

#
# WAR Header
#
# CHAR Magic[4] // "WART"
# DWORD OffsetToData
# DWORD OffsetToResources
#

#
# Resource table
#
# DWORD ResourceCount
# WAR_RESOURCE Resources[ResourceCount]
#

WAR_RESOURCE_FLAGS_STRING = 0x01
WAR_RESOURCE_FLAGS_FILE = 0x02
WAR_RESOURCE_FLAGS_DIRECTORY = 0x04

WAR_RESOURCE_FILESPEC_WAR = 0x1
WAR_RESOURCE_FILESPEC_SIMPLE = 0x2

#
# Resource Address Entry
#
# BYTE Flags
# if(Flags & WAR_RESOURCE_FLAGS_STRING)
#   DWORD OffsetToName
# else
#   DWORD ResourceID
#

#
# Resource
#
# BYTE Flags
# if(Flags & WAR_RESOURCE_FLAGS_DIRECTORY)
#   DWORD OffsetToDirectoryName
#   DWORD ChildCount
#   WAR_RESOURCE Children[ChildCount]
# else
#   if(Flags & WAR_RESOURCE_FLAGS_STRING)
#       DWORD OffsetToName
#   else
#       DWORD ResourceID
#   if(Flags & WAR_RESOURCE_FLAGS_FILE)
#       BYTE FileSpec
#       DWORD OffsetToFileName
#       DWORD OffsetToFileSpecificData
#   else
#       DWORD OffsetToData
#

# 
# File Specific Data for WAR_RESOURCE_FILESPEC_WAR
#
# WORD DirectoryChainLength
# DWORD DirectoryNamesChain[DirectoryChainLength]
# RESOURCE_ADDRESS_ENTRY ResourceReferenced
#

#
# Data table
#
# DWORD DataCountForLoader
#
# The string resources is stored by DWORD length-prefixed UTF-8 string.
# The binary resources is stored by DWORD length-prefixed data.
#

class WARResource:
    file: 'WARFile'
    cached: Any | None
    flags: int
    
    resource_id: int | None
    string: str | None
    children: list['WARResource'] | None
    offset: int | None
    string_offset: int | None
    
    ref_res_item: str | int | None
    ref_res_item_string_offset: int | None
    ref_res_offset: int | None
    ref_res_dirchain: list[str] | None
    ref_res_dirchain_offsets: list[int] | None
    ref_file: str | None
    ref_file_offset: int | None
    ref_file_spec: int | None
    
    def __init__(self, file: 'WARFile'):
        self.file = file
        self.cached = None
        self.flags = 0
        
        self.resource_id = None
        self.string = None
        self.string_offset = None
        self.children = None
        self.offset = None
        
        self.ref_res_item = None
        self.ref_res_item_string_offset = None
        self.ref_res_dirchain = None
        self.ref_res_dirchain_offsets = None
        self.ref_file = None
        self.ref_file_offset = None
        self.ref_file_spec = None
        self.ref_res_offset = None
    
    def load(self, stream: ToolStreamOverIO):
        flags = stream.read_uint8()
        self.flags = flags
        if flags & WAR_RESOURCE_FLAGS_DIRECTORY:
            offset = self.string_offset = stream.read_uint32()
            self.string = self.file.data(offset).decode('utf-8')
            self.children = []
            for _ in range(stream.read_uint32()):
                resource = WARResource(self.file)
                resource.load(stream)
                self.children.append(resource)
        else:
            if flags & WAR_RESOURCE_FLAGS_STRING:
                offset = self.string_offset = stream.read_uint32()
                self.string = self.file.data(offset).decode('utf-8')
            else:
                self.resource_id = stream.read_uint32()
        if flags & WAR_RESOURCE_FLAGS_FILE:
            self.ref_file_spec = stream.read_uint8()
            self.ref_file_offset = offset = stream.read_uint32()
            self.ref_file = self.file.data(offset).decode('utf-8')
            if self.ref_file_spec == WAR_RESOURCE_FILESPEC_WAR:
                last = stream.tell()
                offset = self.ref_res_offset = stream.read_uint32()
                stream.seek(self.file.data_offset+offset)
                self.ref_res_dirchain = []
                self.ref_res_dirchain_offsets = []
                count = stream.read_uint16()
                for _ in range(count):
                    offset = stream.read_uint32()
                    self.ref_res_dirchain_offsets.append(offset)
                    item = self.file.data(offset).decode('utf-8')
                    self.ref_res_dirchain.append(item)
                if stream.read_uint8() & WAR_RESOURCE_FLAGS_STRING:
                    self.ref_res_item_string_offset = stream.read_uint32()
                    stream.seek(-4, os.SEEK_CUR)
                stream.seek(-1, os.SEEK_CUR)
                self.ref_res_item = WARResource.decode_address_entry(self.file, stream)
                stream.seek(last)
        else:
            self.offset = stream.read_uint32()
        
    def child(self, item: int | str) -> TUnion['WARResource', None]:
        if isinstance(item, int):
            for child in self.children:
                if child.resource_id == item: return child
        elif isinstance(item, str):
            for child in self.children:
                if child.string == item: return child
        else:
            return None
        return None
    
    def get(self) -> bytes:
        if self.cached is not None: return self.cached
        if self.offset is None:
            if self.ref_file_spec == WAR_RESOURCE_FILESPEC_WAR:
                file = WARFile(self.ref_file)
                file.load()
                if len(self.ref_res_dirchain) != 0:
                    for i, directory in enumerate(self.ref_res_dirchain):
                        if i == 0:
                            item = file.item(directory)
                        else:
                            item = item.child(directory)
                    return item.child(self.ref_res_item)
                else:
                    return file.item(self.ref_res_item)
        data = self.file.get(self.offset)
        self.cached = data
        return data
    
    @staticmethod
    def decode_address_entry(file: 'WARFile', stream: ToolStreamOverIO) -> str | int:
        flags = stream.read_uint8()
        if flags & WAR_RESOURCE_FLAGS_STRING:
            offset = stream.read_uint32()
            return file.data(offset).decode('utf-8')
        else:
            return stream.read_uint32()
            
class WARFile:
    CACHED: ClassVar[dict[str, 'WARFile']] = {}
    
    stream: ToolStreamOverIO
    file: io.IOBase
    path: str
    loaded: bool
    
    resources: list[WARResource]
    data_offset: int
    resources_offset: int
    data_map: list[bytes]
    
    def __init__(self, path: str | None):
        if path in self.CACHE: return
        self.path = path
        
        if path is not None:
            self.file = open(path, 'rb')
            self.stream = ToolStreamOverIO(self.file)
        
        self.resources = []
        self.loaded = False
        self.data_map = []
        
    def load(self):
        if self.loaded: return
        magic = self.stream.read(4)
        if magic != b'WART':
            raise ValueError('WAR Header is invalid.')
        
        self.data_offset = self.stream.read_uint32()
        self.resources_offset = self.stream.read_uint32()
        
        self.stream.seek(self.data_offset)
        count = self.stream.read_uint32()
        for _ in range(count):
            resource = WARResource(self)
            resource.load(self.stream)
            self.resources.append(resource)
        
        self.CACHE[self.path] = self
        self.loaded = True
        
        self.stream.seek(self.data_offset)
        data_count = self.stream.read_uint32()
        
        for _ in range(data_count):
            length = self.stream.read_uint32()
            data = self.stream.read(length)
            self.data_map.append(data)
        
    def item(self, item: int | str) -> WARResource | None:
        if isinstance(item, int):
            for resource in self.resources:
                if resource.resource_id == item: return resource
        elif isinstance(item, str):
            for resource in self.resources:
                if resource.string == resource: return resource
        else:
            return None
        return None
    
    def data(self, offset: int) -> bytes:
        last = self.stream.tell()
        self.stream.seek(self.data_offset+offset)
        length = self.stream.read_uint32()
        data = self.stream.read(length)
        self.stream.seek(last)
        return data
    
    def data_new(self, data: bytes) -> int:
        offset = 0
        for value in self.data_map:
            offset += 4 + len(value)
        self.data_map.append(data)
        return offset
    
    def internal_data_set(self, offset: int, data: bytes):
        calculated = 0
        for i, value in enumerate(self.data_map):
            if calculated == offset: break
            calculated += 4 + len(value)
        self.data_map[i] = data
    
    def data_set(self, offset: int, data: bytes):
        changes = []
        calculated = 0
        for value in self.data_map:
            changes.append((calculated, 0))
            calculated += 4 + len(value)
        calculated = 0
        self.internal_data_set(offset, data)
        calculated = 0
        for i, value in enumerate(self.data_map):
            changes[i] = (changes[i][0], calculated)
            calculated += 4 + len(value)
        changes = dict(changes)
        def recurse(resource: WARResource):
            if resource.children is not None:
                for child in resource.children:
                    recurse(child)
            else:
                if resource.string is not None:
                    if resource.string_offset in changes:
                        resource.string_offset = changes[resource.string_offset]
                if resource.ref_file is None:
                    if resource.offset in changes:
                        resource.offset = changes[resource.offset]
                else:
                    if resource.ref_file_offset in changes:
                        resource.ref_file_offset = changes[resource.ref_file_offset]
                    if resource.ref_file_spec == WAR_RESOURCE_FILESPEC_WAR:
                        if resource.ref_res_offset in changes:
                            resource.ref_res_offset = changes[resource.ref_res_offset]
                        if isinstance(resource.ref_res_item, str):
                            if resource.ref_res_item_string_offset in changes:
                                resource.ref_res_item_string_offset = changes[resource.ref_res_item_string_offset]
                        for i, v in enumerate(resource.ref_res_dirchain_offsets):
                            if v in changes:
                                resource.ref_res_dirchain_offsets[i] = changes[v]

        for resource in self.resources:
            recurse(resource)
        self.save()
    
    def save(self):
        offsets_to_write_offset: list[int] = []
        resources_to_retrieve_data: list[WARResource] = []
        
        ignored_offsets: list[int] = []

        with io.BytesIO() as resources:
            stream = ToolStreamOverIO(resources)
            stream.write_uint32(len(self.resources))
            def recurse(resource: WARResource):
                if resource.children is not None:
                    stream.write_uint8(WAR_RESOURCE_FLAGS_DIRECTORY)
                    stream.write_uint32(len(resource.children))
                    for child in resource.children:
                        recurse(child)
                else:
                    if resource.ref_file is not None:
                        if resource.ref_res_item is not None:
                            stream.write_uint8(WAR_RESOURCE_FILESPEC_WAR)
                            stream.write_uint32(resource.ref_file_offset)
                            stream.write_uint32(0)
                        else:
                            stream.write_uint8(WAR_RESOURCE_FILESPEC_SIMPLE)
                            stream.write_uint32(resource.ref_file_offset)
                            offsets_to_write_offset.append(stream.tell())
                            stream.write_uint32(0)
                            ignored_offsets.append(resource.ref_res_offset)
                            resources_to_retrieve_data.append(resource)
                            
            stream.seek(0)
            resources = stream.read()
        
        with io.BytesIO() as data:
            stream = ToolStreamOverIO(data)
            count = len(self.data_map)+len(offsets_to_write_offset)
            stream.write_uint32(count)
            offset = 0
            for value in self.data_map:
                if offset in ignored_offsets: continue
                stream.write_uint32(len(value))
                stream.write(value)
                offset += 4 + len(value)
            for i, resource in enumerate(resources_to_retrieve_data):
                offset = offsets_to_write_offset[i]
                with io.BytesIO() as ref_data:
                    ref_stream = ToolStreamOverIO(ref_data)
                    ref_stream.write_uint32(len(resource.ref_res_dirchain_offsets))
                    for dir_offset in resource.ref_res_dirchain_offsets:
                        ref_stream.write_uint32(dir_offset)
                    if isinstance(resource.ref_res_item, int):
                        ref_stream.write_uint32(0)
                        ref_stream.write_uint32(resource.ref_res_item)
                    else:
                        ref_stream.write_uint32(WAR_RESOURCE_FLAGS_STRING)
                        ref_stream.write_uint32(resource.ref_res_item_string_offset)
                    ref_stream.seek(0)
                    ref_data = ref_stream.read()
                stream.write_uint32(len(ref_data))
                stream.write(ref_data)
            stream.seek(0)
            data = stream.read()

        self.file.close()
        self.file = open(self.path, 'wb')
        self.stream = ToolStreamOverIO(self.file)
        
        self.stream.write(b'WART')
        
        self.resources_offset = self.stream.tell()
        self.stream.write(resources)
        last = self.stream.tell()
        self.seek(8)
        self.stream.write_uint32(self.resources_offset)
        self.seek(last)
        
        self.data_offset = self.stream.tell()
        self.stream.write(data)
        self.seek(4)
        self.stream.write_uint32(self.data_offset)
        
        self.file.flush()
        self.file.close()
        self.file = open(self.path, 'rb')
        self.stream = ToolStreamOverIO(self.file)