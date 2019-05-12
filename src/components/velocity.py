from physics import Vector2
from .component import Component


class Velocity(Component):
    def __init__(self, vector: Vector2):
        super().__init__()
        self._vector = vector

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, vector):
        self._vector = vector

    @property
    def unit_vector(self):
        return self._vector.unit_vector

    @unit_vector.setter
    def unit_vector(self, unit_vector):
        self._vector.unit_vector = unit_vector
