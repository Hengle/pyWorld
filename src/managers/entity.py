from typing import AbstractSet

import mappers
from entities import Entity


class EntityManager:
    def __init__(self):
        self._entities = mappers.EntityCollection()

    def create_entity(self) -> int:
        entity = Entity()
        self._entities[entity.identifier] = entity
        return entity.identifier

    def remove_entity(self, entity_id: int):
        del self._entities[entity_id]

    def get_entities(self) -> AbstractSet:
        return self._entities.keys()
