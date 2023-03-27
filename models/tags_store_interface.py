class TagsStoreInterface:
    def increment_count(self, tags: str):
        """
        Increments count of the tags (ordered) in tags store
        :param tags:
        :return: None
        """
        pass

    def decrement_count(self, tags: str):
        """
        Decrements count of the tags (ordered) in tags store
        :param tags:
        :return: None
        """
        pass

    def get_count(self, tags: str) -> int:
        """
        Returns count of the tags (ordered) in tags store
        :param tags:
        :return: count of tags
        """
        pass
