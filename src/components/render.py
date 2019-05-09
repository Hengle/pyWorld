from .component import Component


class Render(Component):
    def __init__(self):
        super().__init__()


class RenderShape(Component):
    def __init__(self, color):
        super().__init__()
        self.color = color


class ShapeSquare(RenderShape):
    def __init__(self, size, color):
        super().__init__(color)
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
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
