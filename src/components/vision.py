from .component import Component


class Vision(Component):
    def __init__(self, radius=0):
        self.radius = radius
        self.in_range = set()

    def add(self, item):
        self.in_range.add(item)

    def remove(self, item):
        self.in_range.remove(item)

    def __str__(self):
        return "{%s}" % format(", ".join([str(item) for item in self.in_range]))
