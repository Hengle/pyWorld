import typing

import physics
from .component import Component


class Vector(Component, physics.Vector2):
    def __init__(self, vector: typing.Tuple):
        super().__init__(vector)
