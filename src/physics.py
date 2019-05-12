import math
import typing


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    @staticmethod
    def from_angle(angle):
        """
        Make unit vector from angle
        :param angle:
        :return:
        """
        return Point(math.cos(angle), math.sin(angle))

    @staticmethod
    def from_tuple(xy_tuple):
        return Point(xy_tuple[0], xy_tuple[1])

    def delta(self, other):
        x = other[0] - self.x
        y = other[1] - self.y
        return Point(x, y)

    def angle_between(self, other) -> float:
        """
        Calculate angle between :self and :other
        :param other: :Point or :Tuple
        :return:
        """
        return self.delta(other).angle()

    def angle(self):
        return math.atan2(self.y, self.x)

    def distance_to(self, other) -> float:
        """
        :param other: :Tuple or :Point
        :return: distance to other as :float
        """
        if self is other:
            return 0

        delta = self.delta(other)
        x_2 = delta.x ** 2
        y_2 = delta.y ** 2

        return math.sqrt(x_2 + y_2)

    def as_tuple(self):
        return self.x, self.y

    def as_int_tuple(self):
        return int(self.x), int(self.y)

    def __getitem__(self, item):
        if item > 1:
            return None
        return self.as_tuple()[item]

    def __str__(self):
        return str(self.as_tuple())

    def int_str(self):
        return str(self.as_int_tuple())

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        elif isinstance(other, (typing.Tuple, Point)):
            return self.x == other[0] and self.y == other[1]
        else:
            return False

    def to_vector2(self, other):
        """
        :param other:
        :return: Normalized vector with magnitude as distance between points.
        """
        delta = self.delta(other)
        magnitude = self.distance_to(other)
        unit_x = delta.x / magnitude
        unit_y = delta.y / magnitude
        return Vector2(magnitude, Point(unit_x, unit_y))


class Vector2:
    def __init__(self, magnitude: float = 0, unit_vector: Point() = None):
        self.magnitude = magnitude
        if not unit_vector:
            unit_vector = Point()
        self.unit_vector = unit_vector
