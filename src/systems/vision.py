import pygame

import colors
import components
from core import World
from managers import mappers
from .system import System


class Vision(System):
    def __init__(self, world: World):
        required_components = {
            components.Position,
            components.Vision
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components: mappers.ComponentMap):
        position = entity_components[components.Position]
        vision = entity_components[components.Vision]

        # TODO move to logging system
        pygame.draw.circle(self._world.surface, colors.gray, position.vector_int, vision.radius, 1)

        world_entities = self._world.ec_manager.get_items([components.Position])
        for other_id, other_components in world_entities:
            if other_id == entity_id:
                continue
            other_position: components.Position = other_components[components.Position]
            distance_to = position.distance_to(other_position)
            if distance_to < vision.radius:
                vision.in_range.add(other_id)
                # TODO move to logging system
                pygame.draw.line(self._world.surface, colors.gray, position.vector_int, other_position.vector_int, 2)
            elif other_id in vision.in_range:
                vision.in_range.remove(other_id)

        self._world.log_line(entity_id, "in_range", vision.in_range)
