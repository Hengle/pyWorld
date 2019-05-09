import abc
import traceback
from typing import Set, Type

import components
import mappers
from world import World


class System(abc.ABC):
    def __init__(self, world: World, required_components: Set[Type[components.Component]] = None):
        self._world = world
        if not required_components:
            required_components = set()
        self.required_components: Set[Type[components.Component]] = required_components

    def update(self):
        for entity_id in self._world.entity_manager.get_entities():
            entity_components = self._world.component_manager.get_entity_components(entity_id)
            if self.is_applicable(entity_components.get_keys()):
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
