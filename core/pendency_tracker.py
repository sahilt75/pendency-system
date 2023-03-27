from typing import List

from models.entity_store import EntityStore
from models.tags_store import TagsStore

"""
Assumptions:
1. The tags will not be an empty list and will have at least one tag
2. The tags will be of type list
3. The tag will not be an empty string "" and will always have a value
"""


class PendencyTracker:
    def __init__(self):
        self.entity_store = EntityStore()
        self.tag_store = TagsStore()

    def startTracking(self, id: int, tags: List[str]):
        if self.entity_store.entity_map.get(id):
            return "Entity ID already exists"

        # Update in memory entity store
        self.entity_store.update(id, tags)

        # Update counters for the tags
        ordered_tags = []
        for tag in tags:
            ordered_tags.append(tag)
            tags_str = "-".join(ordered_tags)  # Convert to '-' separated string as lists are unhashable
            self.tag_store.increment_count(tags_str)

    def getCounts(self, tags: List[str]) -> int:
        tags_str = "-".join(tags)
        return self.tag_store.get_count(tags_str)

    def stopTracking(self, id: int):
        if not self.entity_store.entity_map.get(id):
            return "Entity ID does not exist"

        deleted_tags = self.entity_store.remove(id)

        ordered_tags = []
        for tag in deleted_tags:
            ordered_tags.append(tag)
            tags_str = "-".join(ordered_tags)
            self.tag_store.decrement_count(tags_str)
