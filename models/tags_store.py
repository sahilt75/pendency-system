from models.tags_store_interface import TagsStoreInterface


class TagsStore(TagsStoreInterface):
    def __init__(self):
        self.tags_count = {}

    def increment_count(self, tags: str):
        self.tags_count[tags] = self.tags_count.get(tags, 0) + 1

    def decrement_count(self, tags: str):
        self.tags_count[tags] = self.tags_count.get(tags, 0) - 1

    def get_count(self, tags: str):
        return self.tags_count.get(tags, 0)
