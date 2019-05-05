from typing import Dict, Set, TypeVar

from components import Component


class ComponentManager:
    def __init__(self):
        self._components: Dict[int, Dict[TypeVar, Component]] = {}

        self.__added: Dict[int, Set[Component]] = {}
        self.__removed: Dict[int, Set[Component]] = {}

    def update(self):
        for entity_id, removed_components in self.__removed.items():
            for removed_c in removed_components:
                self._components[entity_id].pop(type(removed_c))

        for entity_id, added_components in self.__added.items():
            for added_c in added_components:
                self._components.setdefault(entity_id, {}).setdefault(type(added_c), added_c)

    def add_component(self, entity_id, component_type, *args, **kwargs):
        component = component_type(*args, **kwargs)
        self.__added.setdefault(entity_id, set()).add(component)

    def remove_component(self, entity_id, component_id):
        self.__removed.setdefault(entity_id, set()).add(component_id)

    def get_entity_components(self, entity_id) -> Dict[TypeVar, Component]:
        return self._components[entity_id]
