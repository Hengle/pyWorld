import behaviour
from .component import Component


class Brain(Component):
    def __init__(self, routine: behaviour.Routine = None):
        super().__init__()
        self.routine: behaviour.Routine = routine
