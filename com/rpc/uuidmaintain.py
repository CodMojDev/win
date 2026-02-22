from .. import guidmaintain
from .dce import *

def NewUuid(uuidName: str, force: bool = False) -> UUID:
    if uuidName in guidmaintain.registry and not force:
        return guidmaintain.registry[uuidName]
    
    uuid = UUID.create()
    guidmaintain.registry[uuidName] = uuid
    
    guidmaintain._Save()
    
    return uuid

def NewUuidSequential(uuidName: str, force: bool = False) -> UUID:
    if uuidName in guidmaintain.registry and not force:
        return guidmaintain.registry[uuidName]
    
    uuid = UUID.sequential()
    guidmaintain.registry[uuidName] = uuid
    
    guidmaintain._Save()
    
    return uuid