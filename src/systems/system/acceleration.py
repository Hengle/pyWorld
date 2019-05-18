from components import component
from core import World
from systems import System


class Acceleration(System):
    def __init__(self, world: World):
        required_components = {
            component.Velocity,
            component.Acceleration
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        # TODO
        pass
