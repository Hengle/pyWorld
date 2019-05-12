import pygame

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
        position: components.Position = entity_components[components.Position]

        circle = entity_components[components.ShapeCircle]
        square = entity_components[components.ShapeSquare]

        if circle:
            pygame.draw.circle(
                self._world.surface,
                circle.color,
                position.vector_int,
                circle.radius,
                2
            )

        if square:
            corners = square.get_corners(position)
            pygame.draw.lines(
                self._world.surface,
                square.color,
                True,
                corners,
                2
            )
