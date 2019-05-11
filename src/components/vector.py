import math
from typing import Tuple

from .component import Component


class Vector2D(Component):
    def __init__(self, vector: Tuple = None):
        self.x = vector[0]
        self.y = vector[1]

    @property
    def vector(self) -> Tuple:
        return self.x, self.y

    @vector.setter
    def vector(self, value: Tuple):
        self.x, self.y = value

    def get_as_int(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def angle(self, other) -> float:
        delta = self.delta(other)
        return math.radians(math.degrees(math.atan2(delta[1], delta[0])))

    def delta(self, other) -> Tuple:
        x = other[0] - self.x
        y = other[1] - self.y
        return x, y

    def distance_to(self, other) -> float:
        if self is other:
            return 0

        x = other[0] - self.x
        y = other[1] - self.y

        x_2 = x ** 2
        y_2 = y ** 2

        return math.sqrt(x_2 + y_2)

    def __getitem__(self, item) -> float:
        if item > 1:
            return None
        return self.vector[item]

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        elif isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        else:
            return False
