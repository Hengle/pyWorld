import abc
import traceback
from typing import Set, Type

import components
from core import World
from managers import mappers


class System(abc.ABC):
    def __init__(self, world: World, required_components: Set[Type[components.Component]]):
        self._world = world
        if not required_components:
            required_components = set()
        self.required_components: Set[Type[components.Component]] = required_components

    def update(self):
        for entity_id, entity_components in self._world.ec_manager.get_items():
            if self.is_applicable(entity_components.get_component_types()):
                try:
                    self.update_entity(entity_id, entity_components)
                except Exception as e:
                    print(f"unable to update entity {entity_id}: {e}")
                    traceback.print_exc()

    @abc.abstractmethod
    def update_entity(self, entity_id, entity_components: mappers.ComponentMap):
        pass

    def is_applicable(self, entity_components):
        return self.required_components.issubset(entity_components)
