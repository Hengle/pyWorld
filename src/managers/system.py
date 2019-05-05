from typing import Set

from systems import God, Movement, Render, System
from world import World


class SystemManager:
    def __init__(self, world: World):
        self.world = world

        self.systems: Set[System] = {
            God(world),
            Movement(world),
            Render(world)
        }

    def update(self):
        for system in self.systems:
            system.update()
