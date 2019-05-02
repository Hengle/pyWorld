from typing import Set, KeysView


class Entity:
    def __init__(self):
        self.identifier = id(self)


class EntityManager:
    def __init__(self):
        self.__entities = {}
        self.__added = set()
        self.__removed = set()

    def create_entity(self) -> int:
        entity = Entity()
        self.__added.add(entity)
        return entity.identifier

    def remove_entity(self, entity_id: int):
        self.__removed.add(entity_id)

    def update(self):
        for entity_id in self.__removed:
            self.__entities.pop(entity_id)
            if entity_id in self.__added:
                self.__added.remove(entity_id)

        for entity in self.__added:
            self.__entities[entity.identifier] = entity

    def get_entities(self) -> KeysView:
        return self.__entities.keys()
