import typing

from physics import Point
from .component import Component


class Position(Component):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self._point = Point.from_tuple(position)

    @property
    def x(self):
        return self._point.x

    @x.setter
    def x(self, x):
        self._point.x = x

    @property
    def y(self):
        return self._point.y

    @y.setter
    def y(self, y):
        self._point.y = y

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        if isinstance(point, typing.Tuple):
            point = Point.from_tuple(point)
        self._point = point
