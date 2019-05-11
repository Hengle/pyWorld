import colors
from .component import Component


class Render(Component):
    pass


class RenderShape(Component):
    def __init__(self, color=colors.blue, filled=False):
        self.color = color
        self.filled = filled


class ShapeSquare(RenderShape):
    def __init__(self, size=0, color=None, filled=False):
        super().__init__(color, filled)
        self.size = size

    def get_corners(self, position):
        half_size = self.size / 2
        x_plane_1 = position.x - half_size
        x_plane_2 = position.x + half_size
        y_plane_1 = position.y - half_size
        y_plane_2 = position.y + half_size
        return [
            (x_plane_1, y_plane_1),
            (x_plane_2, y_plane_1),
            (x_plane_2, y_plane_2),
            (x_plane_1, y_plane_2)
        ]


class ShapeCircle(RenderShape):
    def __init__(self, radius=0, color=None, filled=False):
        super().__init__(color, filled)
        self.radius = radius
