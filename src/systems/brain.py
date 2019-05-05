import components
from world import World
from .system import System


class Brain(System):
    def __init__(self, world: World):
        required_components = {
            components.AI,
            components.Position,
            components.Velocity
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        # TODO
        pass
