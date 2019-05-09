import math
from typing import Tuple

import pygame

import colors
import components
from world import World
from .routine import Routine


class Move(Routine):
    def __init__(self, entity_id, world: World, target=None):
        super().__init__(entity_id, world)
        self._target = target

    @property
    def target(self) -> components.Vector2D:
        return self._target

    @target.setter
    def target(self, target):
        if isinstance(target, Tuple):
            target = components.Vector2D(target)
        elif isinstance(target, components.Vector2D):
            pass
        else:
            target = None
        self._target = target

    def reset(self):
        pass

    def act(self):
        if not self.target:
            self.fail()
        entity_components = self._world.component_manager.get_entity_components(self.entity_id)
        position = entity_components[components.Position]
        velocity = entity_components[components.Velocity]
        boundary = entity_components[components.Boundary]

        pygame.draw.line(self._world.surface,
                         colors.green,
                         position.vector,
                         self.target.vector)

        distance_to_target = position.distance_to(self.target)
        if distance_to_target < boundary.radius:
            self.succeed()
            velocity.vector = (0, 0)
            return

        angle_to_target = position.angle(self.target)
        delta = position.delta(self.target)

        new_v_x = math.cos(angle_to_target)
        new_v_y = math.sin(angle_to_target)

        velocity.vector = new_v_x, new_v_y
