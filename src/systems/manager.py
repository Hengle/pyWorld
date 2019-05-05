from typing import Set

from world import World
from .god import God
from .movement import Movement
from .render import Render
from .system import System


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
