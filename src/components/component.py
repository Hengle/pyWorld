import collections
from typing import Dict, Iterator, Type, TypeVar


class Component(object):
    def __init__(self):
        self.identifier = id(self)


C_T = TypeVar('C_T', bound=Component)


class ComponentMap(collections.MutableMapping):
    def __init__(self):
        self.__components: Dict[Type[Component], Component] = {}

    def __delitem__(self, key: Type[C_T]) -> None:
        self.__components.pop(key)

    def __len__(self) -> int:
        return len(self.__components)

    def __iter__(self) -> Iterator[Type[C_T]]:
        return iter(self.__components)

    def __getitem__(self, item: Type[C_T]) -> C_T:
        return self.__components[item]

    def __setitem__(self, key: Type[C_T], value: C_T):
        self.__components[key] = value
