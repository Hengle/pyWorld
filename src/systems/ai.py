import random
from typing import Tuple

import behaviour
import components
from world import World
from .system import System


class AI(System):
    def __init__(self, world: World):
        required_components = {
            components.Brain
        }
        super().__init__(world, required_components)

    def get_random_point(self) -> Tuple[int, int]:
        max_x, max_y = self.world.surface.get_size()
        return random.randint(0, max_x), random.randint(0, max_y)

    def update_entity(self, entity_id, entity_components):
        brain = entity_components[components.Brain]

        if not brain.routine:
            brain.routine = behaviour.Repeat(entity_id, self.world, behaviour.Wander(entity_id, self.world))
        if not brain.routine.state:
            brain.routine.start()

        brain.routine.act()
