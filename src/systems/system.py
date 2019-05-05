import abc
from typing import Set, Dict

from world import World


class System(abc.ABC):
    def __init__(self, world: World, required_components: Set):
        self.world = world
        if not required_components:
            required_components = set()
        self.required_components: Set = required_components

    def update(self):
        for entity_id in self.world.entity_manager.get_entities():
            entity_components = self.world.component_manager.get_entity_components(entity_id)
            if self.is_applicable(entity_components):
                self.update_entity(entity_id, entity_components)

    @abc.abstractmethod
    def update_entity(self, entity_id, entity_components):
        pass

    def is_applicable(self, entity_components: Dict):
        x = [k in entity_components for k in self.required_components]
        return all(x)
