from win.winnt import *
from win.defbase_allocator import *

class IATHook:
    @classmethod
    def rva2va(cls, base: WT_ADDRLIKE, rva: WT_ADDRLIKE) -> int:
        return PtrUtil.get_address(base) + PtrUtil.get_address(rva)
    
    @classmethod
    def retrieve_datadir(cls, base: WT_ADDRLIKE, entry_id: int) -> int:
        dos = i_cast_value(base, IMAGE_DOS_HEADER)
        nt = i_cast_value(cls.rva2va(base, dos.e_lfanew), IMAGE_NT_HEADERS32)
        if nt.OptionalHeader.Magic == IMAGE_NT_OPTIONAL_HDR64_MAGIC:
            nt = i_cast_structure(nt, IMAGE_NT_HEADERS64)
        data = nt.OptionalHeader.DataDirectory
        return cls.rva2va(base, data[entry_id].VirtualAddress)
    
    @classmethod
    def address_by_name(cls, base: WT_ADDRLIKE, import_name: IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64], import_addr: IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64], func_name: bytes) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        while import_name.contents.u1.Ordinal:
            if IMAGE_SNAP_BY_ORDINAL(import_name.contents.u1.Ordinal):
                import_name = PtrArithmetic.add(import_name, 1)
                import_addr = PtrArithmetic.add(import_addr, 1)
                continue
            import_entry = i_cast_value(cls.rva2va(base, import_name.contents.u1.AddressOfData), IMAGE_IMPORT_BY_NAME)
            if import_entry.Name.value != func_name:
                import_name = PtrArithmetic.add(import_name, 1)
                import_addr = PtrArithmetic.add(import_addr, 1)
                continue
            import_name = PtrArithmetic.add(import_name, 1)
            import_addr = PtrArithmetic.add(import_addr, 1)
            return import_addr
        return None
        
    @classmethod
    def address_by_ordinal(cls, base: WT_ADDRLIKE, import_name: IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64], import_addr: IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64], ordinal: int) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        while import_name.contents.u1.Ordinal:
            if IMAGE_SNAP_BY_ORDINAL(import_name.contents.u1.Ordinal) and IMAGE_ORDINAL(import_name.contents.u1.Ordinal) == ordinal:
                return import_addr
            import_name = PtrArithmetic.add(import_name, 1)
            import_addr = PtrArithmetic.add(import_addr, 1)
        return None
    
    @classmethod
    def thunk_by_name(cls, base: WT_ADDRLIKE, dll: bytes, func_name: bytes) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        imports = i_cast(cls.retrieve_datadir(base, IMAGE_DIRECTORY_ENTRY_IMPORT), PIMAGE_IMPORT_DESCRIPTOR)
        while imports.contents.Name:
            if LPSTR(cls.rva2va(base, imports.contents.Name)).value.lower() != dll.lower():
                imports = PtrArithmetic.add(imports, 1)
                continue
            original = i_cast(cls.rva2va(base, imports.contents.OriginalFirstThunk), PIMAGE_THUNK_DATA)
            thunk = i_cast(cls.rva2va(base, imports.contents.FirstThunk), PIMAGE_THUNK_DATA)
            return cls.address_by_name(base, original, thunk, func_name)
        return None
    
    @classmethod
    def thunk_by_ordinal(cls, base: WT_ADDRLIKE, dll: bytes, ordinal: int) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        imports = i_cast(cls.retrieve_datadir(base, IMAGE_DIRECTORY_ENTRY_IMPORT), PIMAGE_IMPORT_DESCRIPTOR)
        while imports.contents.Name:
            if LPSTR(cls.rva2va(base, imports.contents.Name)).value.lower() != dll.lower():
                imports = PtrArithmetic.add(imports, 1)
                continue
            original = i_cast(cls.rva2va(base, imports.contents.OriginalFirstThunk), PIMAGE_THUNK_DATA)
            thunk = i_cast(cls.rva2va(base, imports.contents.FirstThunk), PIMAGE_THUNK_DATA)
            return cls.address_by_ordinal(base, original, thunk, ordinal)
        return None
    
    @classmethod
    def delayload_thunk_by_name(cls, base: WT_ADDRLIKE, dll: bytes, func_name: bytes) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        imports = i_cast(cls.retrieve_datadir(base, IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT), PIMAGE_DELAYLOAD_DESCRIPTOR)
        while imports.contents.DllNameRVA:
            if LPSTR(cls.rva2va(base, imports.contents.DllNameRVA)).value.lower() != dll.lower():
                imports = PtrArithmetic.add(imports, 1)
                continue
            import_name = i_cast(cls.rva2va(base, imports.contents.ImportNameTableRVA, PIMAGE_THUNK_DATA))
            import_addr = i_cast(cls.rva2va(base, imports.contents.ImportAddressTableRVA, PIMAGE_THUNK_DATA))
            return cls.address_by_name(base, import_name, import_addr, func_name)
        return None
    
    @classmethod
    def delayload_thunk_by_ordinal(cls, base: WT_ADDRLIKE, dll: bytes, ordinal: int) -> IPointer[IMAGE_THUNK_DATA32 | IMAGE_THUNK_DATA64] | None:
        imports = i_cast(cls.retrieve_datadir(base, IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT), PIMAGE_DELAYLOAD_DESCRIPTOR)
        while imports.contents.DllNameRVA:
            if LPSTR(cls.rva2va(base, imports.contents.DllNameRVA)).value.lower() != dll.lower():
                imports = PtrArithmetic.add(imports, 1)
                continue
            import_name = i_cast(cls.rva2va(base, imports.contents.ImportNameTableRVA), PIMAGE_THUNK_DATA)
            import_addr = i_cast(cls.rva2va(base, imports.contents.ImportAddressTableRVA), PIMAGE_THUNK_DATA)
            return cls.address_by_ordinal(base, import_name, import_addr, ordinal)
        return None
    
    @classmethod
    def replace(cls, module: CDLL | WT_ADDRLIKE, dll: bytes | str, function: int | bytes | str, value: WT_ADDRLIKE, delay_load: bool = False) -> bool:
        if isinstance(dll, str):
            dll = dll.encode('ascii')
        if isinstance(module, CDLL):
            module = module._handle
        allocator = CVirtualAllocator()
        if isinstance(function, int):
            if delay_load:
                thunk = cls.delayload_thunk_by_ordinal(module, dll, function)
            else:
                thunk = cls.thunk_by_ordinal(module, dll, function)
            if not thunk:
                return False
        else:
            if isinstance(function, str):
                function = function.encode('ascii')
            if delay_load:
                thunk = cls.delayload_thunk_by_name(module, dll, function)
            else:
                thunk = cls.thunk_by_name(module, dll, function)
            if not thunk:
                return False
        protection = allocator.protect(thunk, sizeof(IMAGE_THUNK_DATA), PAGE_READWRITE)
        thunk.contents.u1.Function = PtrUtil.get_address(value)
        allocator.protect(thunk, sizeof(IMAGE_THUNK_DATA), protection)
        return True