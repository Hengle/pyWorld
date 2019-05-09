from .component import Component


class Vision(Component):
    def __init__(self, range):
        super().__init__()
        self.range = range
