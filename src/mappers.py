import collections
from typing import Dict, Iterator, List, Set, Type, ValuesView

import entities
from components import C_T, Component


class EntityCollection(collections.MutableMapping):
    def __init__(self):
        self._entities: Dict[int, entities.Entity] = {}

    def __getitem__(self, key: int) -> entities.Entity:
        return self._entities.get(key)

    def __setitem__(self, key: int, value: entities.Entity) -> None:
        self._entities[key] = value

    def __delitem__(self, key: int) -> None:
        del self._entities[key]

    def __len__(self) -> int:
        return len(self._entities)

    def __iter__(self) -> Iterator[int]:
        return iter(self._entities.copy())


class ComponentMap(collections.MutableMapping):
    def __init__(self):
        self._components: Dict[Type[Component], Component] = {}

    def get_keys(self) -> Set[Type[Component]]:
        return set(self._components.keys())

    def get_values(self) -> ValuesView[Component]:
        return self._components.values()

    def get_sub_keys(self, supertype: Type[C_T]) -> Set[Type[C_T]]:
        return set([key for key in self._components.keys() if issubclass(key, supertype)])

    def get_sub_values(self, supertype) -> List[C_T]:
        return [value for value in self._components.values() if isinstance(value, supertype)]

    def __getitem__(self, item: Type[C_T]) -> C_T:
        return self._components.get(item)

    def __setitem__(self, key: Type[C_T], value: C_T):
        self._components[key] = value

    def __delitem__(self, key: Type[C_T]) -> None:
        del self._components[key]

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[Type[C_T]]:
        return iter(self._components.copy())


class EntityComponentMap(collections.MutableMapping):
    def __init__(self):
        self._entity_components: Dict[int, ComponentMap] = {}

    def __getitem__(self, key: int) -> ComponentMap:
        components = self._entity_components.get(key)
        if not components:
            components = ComponentMap()
            self._entity_components[key] = components
        return components

    def __setitem__(self, key: int, value: ComponentMap) -> None:
        self._entity_components[key] = value

    def __delitem__(self, key: int) -> None:
        del self._entity_components[key]

    def __len__(self) -> int:
        return len(self._entity_components)

    def __iter__(self) -> Iterator[int]:
        return iter(self._entity_components.copy())
