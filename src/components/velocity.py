from .component import Component


class Velocity(Component):
    def __init__(self, velocity=(0, 0)):
        super().__init__()
        self.velocity = velocity

    def __getitem__(self, item):
        if item > 1 or not self.velocity:
            return None
        return self.velocity[item]
