from typing import Tuple

from .vector import Vector2D


class Position(Vector2D):
    def __init__(self, position: Tuple = (0, 0)):
        super().__init__(position)
