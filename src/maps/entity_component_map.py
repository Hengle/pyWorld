import sys
from collections import MutableMapping
from typing import Any, Dict, Iterator

from components import Component
from maps import ComponentMap


class EntityComponentMap(MutableMapping):
    def __init__(self):
        self._entity_components: Dict[Any, ComponentMap] = {}
        self.id_stack = []
        self.id_count = 0

    def __getitem__(self, entity_id) -> ComponentMap:
        return self._entity_components.get(entity_id)

    def __setitem__(self, entity_id, value: ComponentMap) -> None:
        if entity_id in self._entity_components:
            self._entity_components[entity_id] = value

    def __delitem__(self, entity_id) -> None:
        del self._entity_components[entity_id]
        self.id_stack.append(entity_id)

    def __len__(self) -> int:
        return len(self._entity_components)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._entity_components.copy())

    def items(self):
        return self._entity_components.copy().items()

    def add_component(self, entity_id, comp: Component) -> None:
        entity_components = self._entity_components.get(entity_id)
        if entity_components is not None:
            entity_components[type(comp)] = comp

    def create_entity(self) -> Any:
        new_identifier = self._get_next_identifier()
        if new_identifier is None:
            return None
        self._entity_components.setdefault(new_identifier, ComponentMap())
        return new_identifier

    def _get_next_identifier(self):
        if self.id_count == sys.maxsize - 1:
            return None
        self.id_count += 1
        next_id = self.id_count
        # return str(uuid4())
        return next_id
