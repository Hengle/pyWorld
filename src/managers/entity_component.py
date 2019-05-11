from typing import Type

import components
from managers import mappers


class EntityComponentManager:

    def __init__(self):
        self._entity_components = mappers.EntityComponentMap()

    def create_component(self, entity_id: str, component_type: Type[components.C_T], *args, **kwargs) -> components.C_T:
        component = self.get_entity_components(entity_id)[component_type]
        if not component:
            component = component_type(*args, **kwargs)
            self._entity_components.add_component(entity_id, component)
        return component

    def remove_component(self, entity_id, component_type: Type[components.Component]):
        del self._entity_components[entity_id][component_type]

    def get_entity_components(self, entity_id) -> mappers.ComponentMap:
        return self._entity_components[entity_id]

    def create_entity(self) -> str:
        entity = self._entity_components.create_entity()
        return entity

    def get_items(self):
        return self._entity_components.items()
