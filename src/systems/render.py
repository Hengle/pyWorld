import pygame

import components
from world import World
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

        shapes = entity_components.get_sub_values(components.RenderShape)

        for shape in shapes:
            if isinstance(shape, components.ShapeCircle):
                pygame.draw.circle(
                    self._world.surface,
                    shape.color,
                    position.vector,
                    shape.radius,
                    2
                )
            elif isinstance(shape, components.ShapeSquare):
                corners = shape.get_corners(position)
                pygame.draw.lines(
                    self._world.surface,
                    shape.color,
                    True,
                    corners,
                    2
                )
