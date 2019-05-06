from .component import Component


class Boundary(Component):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
