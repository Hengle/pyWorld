import collections
from typing import Dict, Iterator, Set, Type
from uuid import uuid4

import components.component


class ComponentMap(collections.MutableMapping):
    def __init__(self):
        self._components: Dict[Type[components.Component], components.Component] = {}

    def __getitem__(self, item: Type[components.C_T]) -> components.C_T:
        return self._components.get(item)

    def __setitem__(self, key: Type[components.C_T], value: components.C_T):
        self._components[key] = value

    def __delitem__(self, key: Type[components.C_T]) -> None:
        if self._components.get(key):
            del self._components[key]

    def __len__(self) -> int:
        return len(self._components)

    def __iter__(self) -> Iterator[Type[components.C_T]]:
        return iter(self._components.copy())

    def get_component_types(self) -> Set[Type[components.Component]]:
        return set(self._components.keys())


class EntityComponentMap(collections.MutableMapping):
    def __init__(self):
        self._entity_components: Dict[str, ComponentMap] = {}

    def __getitem__(self, entity_id: str) -> ComponentMap:
        return self._entity_components.get(entity_id)

    def __setitem__(self, entity_id: str, value: ComponentMap) -> None:
        self._entity_components[entity_id] = value

    def __delitem__(self, entity_id: str) -> None:
        del self._entity_components[entity_id]

    def __len__(self) -> int:
        return len(self._entity_components)

    def __iter__(self) -> Iterator[str]:
        return iter(self._entity_components.copy())

    def items(self):
        return self._entity_components.copy().items()

    def add_component(self, entity_id, component: components.Component) -> None:
        entity_components = self._entity_components.get(entity_id)
        if entity_components is not None:
            entity_components[type(component)] = component

    def create_entity(self) -> str:
        new_identifier = str(uuid4())
        self._entity_components.setdefault(new_identifier, ComponentMap())
        return new_identifier
