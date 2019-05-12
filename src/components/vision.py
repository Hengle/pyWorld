from .component import Component


class Vision(Component):
    def __init__(self, radius=0):
        self.radius = radius
        self.in_range = set()
