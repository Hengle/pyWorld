from typing import Tuple

from .component import Component


class Vector2D(Component):
    def __init__(self, vector: Tuple = None):
        super().__init__()
        self.x = vector[0]
        self.y = vector[1]

    @property
    def vector(self) -> Tuple:
        return self.x, self.y

    @vector.setter
    def vector(self, value: Tuple):
        self.x, self.y = value
        pass

    def get_as_int(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        elif isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        else:
            return False
