import enum
enum._is_sunder = lambda name: False
enum.EnumType._check_for_existing_members_ = lambda cls, bases: ...

import struct

class WPDBEnum(enum.Enum):
    _type_ = 'b'
    
    def serialize(self) -> bytes:
        return struct.pack(self._type_, self.value)
    
    @classmethod
    def unserialize(cls, serialized: bytes) -> int:
        return cls(struct.unpack(cls._type_, serialized)[0])

    @classmethod
    def size(cls) -> int:
        return struct.calcsize(cls._type_)

class WPDBEnumByte(WPDBEnum): ...

class WPDBEnumInt(WPDBEnum):
    _type_ = 'i'
    
class WPDBEntryType(WPDBEnumByte):
    WPDB_FUNCTION = 0xBB
    WPDB_TYPELIST = 0xBC