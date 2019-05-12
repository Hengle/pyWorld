import math
from typing import Tuple

import pygame

import components
from behaviour import Routine
from core.world import World


class Move(Routine):

    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)
        self.target = None

    @property
    def target(self) -> components.Vector:
        return self._target

    @target.setter
    def target(self, target):
        if isinstance(target, Tuple):
            target = components.Vector(target)
        elif isinstance(target, components.Vector):
            pass
        else:
            target = None
        self._target = target

    def reset(self):
        pass

    def act(self):
        if not self.target:
            self.fail()
        entity_components = self._world.ec_manager.get_entity_components(self.entity_id)
        position = entity_components[components.Position]
        velocity = entity_components[components.Velocity]
        boundary = entity_components[components.Boundary]

        self._world.log_line(self.entity_id,
                             "target_position",
                             pygame.color.THECOLORS['orange'],
                             position.vector,
                             self.target.vector)

        distance_to_target = position.distance_to(self.target)
        self.log("distance_to", int(distance_to_target))
        if distance_to_target < boundary.radius:
            self.succeed()
            return

        angle_to_target = position.angle(self.target)
        delta = position.delta(self.target)

        new_v_x = math.cos(angle_to_target)
        new_v_y = math.sin(angle_to_target)

        velocity.vector = new_v_x, new_v_y
