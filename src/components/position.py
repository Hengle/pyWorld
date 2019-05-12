from typing import Tuple

from .vector import Vector


class Position(Vector):
    def __init__(self, position: Tuple = (0, 0)):
        super().__init__(position)
