from typing import Set, Type

import systems
from core import World
from systems import System


class SystemManager:
    def __init__(self, world: World):
        self._world = world

        system_types: Set[Type[System]] = {
            systems.God,
            systems.Vision,
            systems.Movement,
            systems.Render,
            systems.AI,
            systems.Logging
        }

        self._systems = [system(world) for system in system_types]

    def update(self):
        for system in self._systems:
            system.update()
