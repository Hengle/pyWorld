from .component import Component


class Acceleration(Component):
    def __init__(self, acceleration=0, max_velocity=0):
        self.acceleration = acceleration
        self.max_velocity = max_velocity
