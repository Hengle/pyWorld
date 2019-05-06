from typing import Tuple

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

        new_vx = abs(velocity.x)
        new_vy = abs(velocity.y)

        if position.x > self.target.x:
            new_vx = -new_vx
        velocity.x = new_vx

        if position.y > self.target.y:
            new_vy = -new_vy
        velocity.y = new_vy

        velocity.vector = (new_vx, new_vy)

        # if position==self.target
