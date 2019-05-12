import math
import typing


class Vector2:
    def __init__(self, vector: typing.Tuple = None):
        self.x = vector[0]
        self.y = vector[1]

    @property
    def vector(self) -> typing.Tuple[float, float]:
        return self.x, self.y

    @vector.setter
    def vector(self, value: typing.Tuple):
        self.x, self.y = value

    @property
    def vector_int(self) -> typing.Tuple[int, int]:
        return int(self.x), int(self.y)

    def angle(self, other) -> float:
        delta = self.delta(other)
        return math.radians(math.degrees(math.atan2(delta.y, delta.x)))

    def delta(self, other):
        """
        :param other: :Tuple or :Vector2D
        :return: Normalized :Vector2D
        """
        x = other[0] - self.x
        y = other[1] - self.y
        return Vector2((x, y))

    def distance_to(self, other) -> float:
        """
        :param other: :Tuple or :Vector2D
        :return: distance to other as :float
        """
        if self is other:
            return 0

        x = other[0] - self.x
        y = other[1] - self.y

        x_2 = x ** 2
        y_2 = y ** 2

        return math.sqrt(x_2 + y_2)

    def __getitem__(self, item) -> typing.Optional[float]:
        if item > 1:
            return None
        return self.vector[item]

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        elif isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __str__(self):
        return f"{self.x}:{self.y}"

    def str_int(self):
        return f"{int(self.x)}:{int(self.y)}"
