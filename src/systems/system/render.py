from components import component
from core import World
from systems import System


class Render(System):
    def __init__(self, world: World):
        required_components = {
            component.Render,
            component.Position
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        position = entity_components[component.Position]
        render = entity_components[component.Render]

        render.render(position.point.as_int_tuple(), self._world.surface)
