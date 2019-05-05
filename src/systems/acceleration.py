import components
from world import World
from .system import System


class Acceleration(System):
    def __init__(self, world: World):
        required_components = {
            components.Velocity,
            components.Acceleration
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        # TODO
        pass
