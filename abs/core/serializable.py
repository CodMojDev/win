#
# WinAbs serialization over WRPC marshalling
#

from win.wrpc.marshal import *
from typing import ClassVar
from _typeshed import ReadableBuffer
from .io import *

import uuid

class Serializer:
    @staticmethod
    def serialize(v: Any, stream: io.IOBase | None = None) -> bytes:
        """
        Serialize the object into bytes.
        """
        if isinstance(v, ISerializable):
            data = WRPC.marshal(v.internal_mshl)
        else:
            data = WRPC.marshal(v)
        if stream is not None:
            stream.write(data)
        return data
    
    @staticmethod
    def deserialize(stream: io.IOBase | WRPCStream | bytes) -> Any:
        """
        Deserialize the serialized object from stream.
        """
        if isinstance(stream, bytes):
            stream = WRPCStream(stream)
        elif isinstance(stream, WRPCStream):
            pass
        else:
            last = stream.tell()
            data = stream.read()
            stream.seek(last)
            stream = WRPCStream(data)
        return WRPC.unmarshal(stream)

class ISerializable:
    class InternalMshl(IWRPCMarshal):
        BASE_UUID = uuid.UUID('{8c72cacb-7695-f111-b0c8-e470b8cb13ef}')
        
        serializable: 'ISerializable'
        serializable_T: ClassVar[type['ISerializable']]
        
        def __init__(self, serializable: 'ISerializable'):
            self.serializable = serializable
            
        def marshal(self) -> bytes:
            return bytes(self.serializable.serialize())
            
        @classmethod
        def unmarshal(cls, stream: Stream):
            stream.protocol = None
            return cls.serializable_T.deserialize(stream)
        
    def serialize(self) -> ReadableBuffer:
        """
        Serialize the object into bytes.
        """
        return b''
    
    @staticmethod
    def deserialize(stream: Stream):
        """
        Deserialize the object into stream.
        """
        return None
    
    def __init_subclass__(cls):
        iid = uuid.uuid5(ISerializable.InternalMshl.BASE_UUID, cls.__module__+cls.__qualname__)
        class InternalMshlEx(ISerializable.InternalMshl):
            _iid_ = IID.from_buffer_copy(bytes(iid))
            serializable_T = cls
        cls.InternalMshl = InternalMshlEx
        WRPC.add(InternalMshlEx)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.internal_mshl = self.InternalMshl(self)

class SerializedFile(DelegatingStream):
    """
    The serialized file helper.
    """
    
    @classmethod
    def open(cls, path: str) -> 'SerializedFile':
        """
        Open the serialized file.
        """
        stream = open(path, 'rb')
        if stream.read(4) != b'SRLZ':
            raise ValueError('Invalid serialized file.')
        return cls(stream)
    
    @classmethod
    def save(cls, path: str) -> 'SerializedFile':
        """
        Save the serialized file.
        """
        stream = open(path, 'wb')
        stream.write(b'SRLZ')
        return cls(stream)