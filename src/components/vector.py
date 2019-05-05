from typing import Tuple

from .component import Component


class Vector2D(Component):
    def __init__(self, vector: Tuple = None):
        super().__init__()
        self.vector = vector

    def __getitem__(self, item):
        if item > 1 or not self.vector:
            return None
        return self.vector[item]

    @property
    def x(self):
        return self.vector[0]

    @property
    def y(self):
        return self.vector[1]

    def get_as_int(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)
