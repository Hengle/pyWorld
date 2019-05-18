from collections import MutableMapping
from typing import Dict, Iterator, Set, Type

from components import C_T, Component


class ComponentMap(MutableMapping):
    def __init__(self):
        self._components: Dict[Type[Component], Component] = {}

    def __getitem__(self, item: Type[C_T]) -> C_T:
        return self._components.get(item)

    def __setitem__(self, key: Type[C_T], value: C_T):
        self._components[key] = value

    def __delitem__(self, key: Type[C_T]) -> None:
        if self._components.get(key):
            del self._components[key]

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[Type[C_T]]:
        return iter(self._components.copy())

    def get_component_types(self) -> Set[Type[Component]]:
        return set(self._components.keys())
