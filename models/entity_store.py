from typing import List
from models.entity_store_interface import EntityStorageInterface

class EntityStore(EntityStorageInterface):
    def __init__(self):
        self.entity_map = {}

    def update(self, id: int, tags: List[str]):
        self.entity_map[id] = tags

    def remove(self, id: int) -> List[str]:
        deleted_record = self.entity_map.pop(id)
        return deleted_record
