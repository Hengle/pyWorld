from .component import Component


class Velocity(Component):
    def __init__(self, velocity=(0, 0)):
        super().__init__()
        self.velocity = velocity

    def __getitem__(self, item):
        if item > 1:
            return None
        return self.velocity[item]

    def set_velocity(self, velocity):
        self.velocity = velocity
