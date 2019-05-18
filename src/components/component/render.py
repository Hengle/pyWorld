import shapes
from components.abstract_component import Component


class Render(Component):
    def __init__(self, shape: shapes.Shape = None, position=None):
        self.position = position
        self.shape = shape

    def render(self, position, surface):
        self.shape.position = position
        self.shape.render(surface)
