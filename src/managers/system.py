from typing import Set, Type

import systems
from systems import System
from world import World


class SystemManager:
    def __init__(self, world: World):
        self.world = world

        system_types: Set[Type[System]] = {
            systems.God,
            systems.Movement,
            systems.Render,
            systems.AI
        }

        self.systems = [system(world) for system in system_types]

    def update(self):
        for system in self.systems:
            system.update()
