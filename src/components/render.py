from .component import Component


class Render(Component):
    def __init__(self, radius=0, width=0):
        super().__init__()
        self.radius = radius
        self.width = width
