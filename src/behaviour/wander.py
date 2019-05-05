import components
from world import World
from .routine import Routine


class Wander(Routine):
    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)

    def reset(self):
        pass

    def act(self):
        entity_components = self.world.component_manager.get_entity_components(self.entity_id)
        position = entity_components[components.Position]
        velocity = entity_components[components.Velocity]
