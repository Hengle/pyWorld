from typing import Dict, Set, Type

import components


class ComponentManager:
    def __init__(self):
        self._components: Dict[int, components.ComponentMap] = {}

        self.__added: Dict[int, Set[components.Component]] = {}
        self.__removed: Dict[int, Set[Type[components.Component]]] = {}

    def update(self):
        for entity_id, removed_components in self.__removed.items():
            for removed_component in removed_components:
                self._components[entity_id].pop(removed_component)

        for entity_id, added_components in self.__added.items():
            for added_c in added_components:
                self._components.setdefault(entity_id, components.ComponentMap())\
                    .setdefault(type(added_c), added_c)

    def add_component(self, entity_id, component_type: Type[components.Component], *args, **kwargs):
        component = component_type(*args, **kwargs)
        self.__added.setdefault(entity_id, set()).add(component)

    def remove_component(self, entity_id, component_type: Type[components.Component]):
        self.__removed.setdefault(entity_id, set()).add(component_type)

    def get_entity_components(self, entity_id) -> components.ComponentMap:
        return self._components[entity_id]
