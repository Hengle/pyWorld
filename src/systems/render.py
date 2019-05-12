import components
from core import World
from .system import System


class Render(System):
    def __init__(self, world: World):
        required_components = {
            components.Render,
            components.Position
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        position = entity_components[components.Position]

        render = entity_components[components.Render]

        render.render(position.vector_int, self._world.surface)
