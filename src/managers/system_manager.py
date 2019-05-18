from typing import Set, Type

from core import World
from systems import System, system


class SystemManager:
    def __init__(self, world: World):
        self._world = world

        system_types: Set[Type[System]] = {
            system.God,
            system.Vision,
            system.Movement,
            system.Render,
            system.AI,
            system.Logging
        }

        self._systems = [sys(world) for sys in system_types]

    def update(self):
        for system in self._systems:
            system.update()
