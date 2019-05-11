from abc import ABC
from typing import TypeVar


class Component(ABC):
    pass


C_T = TypeVar('C_T', bound=Component)
