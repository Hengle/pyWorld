from typing import Tuple

from .vector import Vector2D


class Velocity(Vector2D):
    def __init__(self, velocity: Tuple = (0, 0)):
        super().__init__(velocity)
