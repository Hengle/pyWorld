import pygame

import colors
import components
from world import World
from .system import System


class Render(System):
    def __init__(self, world: World):
        required = {
            components.Render,
            components.Position
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        render: components.Render = entity_components[components.Render]
        position: components.Position = entity_components[components.Position]

        pygame.draw.circle(self.world.surface, colors.red,
                           position.get_as_int(),
                           render.radius,
                           render.width)
