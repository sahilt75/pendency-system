from typing import List


class EntityStorageInterface:
    def update(self, id: int, tags: str):
        """
        Adds / updates entity store
        :param id: Entity ID
        :param tags: Entity tags
        :return: None
        """
        pass

    def remove(self, id: int) -> List[str]:
        """
        Removes from entity store
        :param id: entity ID
        :return: tags
        """
        pass