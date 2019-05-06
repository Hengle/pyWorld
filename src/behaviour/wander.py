import random

import components
from world import World
from .move import Move
from .routine import Routine


class Wander(Routine):
    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)
        self.move = Move(entity_id, world)

    def reset(self):
        pass

    def find_random_location(self):
        max_x, max_y = self._world.surface.get_size()
        return random.randint(0, max_x), random.randint(0, max_y)
        # return 0, 0

    def act(self):
        if not self.move.is_running():
            self.move.target = self.find_random_location()
            self.move.start()
        self._world.component_manager.add_component_if_not_exist(self.entity_id, components.Velocity, (1, 1))

        self.move.act()

        if self.move.is_success():
            self._world.component_manager.remove_component(self.entity_id, components.Velocity)
