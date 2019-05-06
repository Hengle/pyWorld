from typing import TypeVar


class Component:
    def __init__(self):
        self.identifier = id(self)


C_T = TypeVar('C_T', bound=Component)
