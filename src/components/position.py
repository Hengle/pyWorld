from .component import Component


class Position(Component):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.position = position

    def __getitem__(self, item):
        if item > 1 or not self.position:
            return None
        return self.position[item]

    def get_as_int(self):
        return int(self[0]), int(self[1])
