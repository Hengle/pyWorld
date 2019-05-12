from typing import Tuple

from .vector import Vector


class Velocity(Vector):
    def __init__(self, velocity: Tuple = (0, 0)):
        super().__init__(velocity)
