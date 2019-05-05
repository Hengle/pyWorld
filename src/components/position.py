from .component import Component


class Position(Component):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.position = position

    def __getitem__(self, item):
        if item > 1:
            return None
        return self.position[item]

    def get_as_int(self):
        return int(self.position[0]), int(self.position[1])

    def set_position(self, position):
        self.position = position
