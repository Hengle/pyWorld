import behaviour
from components.abstract_component import Component


class Brain(Component):
    def __init__(self, routine: behaviour.Routine = None):
        self.routine: behaviour.Routine = routine
