from .winnt import LIST_ENTRY, PLIST_ENTRY, byref, addressof
from .defbase import *

from typing import TypeAlias, Union as TUnion, List, Iterator, Any, Generic, TypeVar, Type

class IListEntry():
    Flink: IPointer['IListEntry']
    Blink: IPointer['IListEntry']
    
IListNative: TypeAlias = TUnion['DoubleLinkedList', IPointer[IListEntry], IListEntry]

T = TypeVar('T')

class IDoubleLinkedList(Generic[T]):
    entry_type: Type[T]
    dl_list: T
    
    @staticmethod
    def init(entry_type: Type[T] = IListEntry) -> 'IDoubleLinkedList': ...
    
    def __init__(self, dl_list: IListNative, entry_type: Type[T] = PLIST_ENTRY): ...
    
    @property
    def blink(self) -> IPointer[T]: ...
    
    @property
    def flink(self) -> IPointer[T]: ...
    
    def start(self) -> T: ...
    
    def end(self) -> T: ...

    def items(self) -> List[T]: ...
    
    @property
    def empty(self) -> bool: ...
    
    def __iter__(self) -> Iterator[T]: ...
    
    def __list__(self) -> List[T]: ...

    def __contains__(self, dl_list: IListNative) -> bool: ...
    
    def __len__(self) -> int: ...

class DoubleLinkedList:
    dl_list: IListEntry
    entry_type: type
    
    @staticmethod
    def init(entry_type: type = IListEntry) -> 'DoubleLinkedList':
        list_head: IListEntry = LIST_ENTRY()
        list_head.Flink = list_head.Blink = byref(list_head)
        return DoubleLinkedList(list_head, entry_type)
    
    def __init__(self, dl_list: IListNative, entry_type: type = PLIST_ENTRY):
        dl_list: IListEntry
        
        if isinstance(dl_list, DoubleLinkedList):
            dl_list = dl_list.dl_list
        if isinstance(dl_list, PLIST_ENTRY):
            dl_list = dl_list.contents
        if not isinstance(dl_list, LIST_ENTRY):
            dl_list = i_cast(byref(dl_list), PLIST_ENTRY).contents
            
        self.dl_list = dl_list
        self.entry_type = entry_type
    
    @property
    def blink(self) -> IPointer[IListEntry]:
        return self.dl_list.Blink
    
    @property
    def flink(self) -> IPointer[IListEntry]:
        return self.dl_list.Flink
    
    def start(self) -> IListEntry:
        return i_cast(self.flink, self.entry_type).contents
    
    def end(self) -> IListEntry:
        return i_cast(self.blink, self.entry_type).contents

    def items(self) -> List[Any]:
        dl_list: List[Any] = []
        flink: IPointer[IListEntry] = self.flink
        
        while addressof(flink.contents) != addressof(self.dl_list):
            dl_list.append(i_cast(flink, self.entry_type).contents)
            flink = flink.contents.Flink
            
        return dl_list
    
    @property
    def empty(self) -> bool:
        return addressof(self.flink.contents) == addressof(self.dl_list)
    
    def __iter__(self) -> Iterator[IListEntry]:
        return iter(self.items())
    
    def __list__(self) -> List[IListEntry]:
        return self.items()

    def __contains__(self, dl_list: IListNative) -> bool:
        if isinstance(dl_list, DoubleLinkedList):
            dl_list = dl_list.dl_list
        if isinstance(dl_list, PLIST_ENTRY):
            dl_list = dl_list.contents
            
        return addressof(dl_list) in [addressof(entry) for entry in self.items()]
    
    def __len__(self) -> int:
        return len(self.items())