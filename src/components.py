from typing import Dict, Set


class Component(object):
    def __init__(self):
        self.identifier = id(self)


class ComponentManager:
    _components: Dict[int, Dict] = {}

    __added: Dict[int, Set] = {}
    __removed: Dict[int, Set] = {}

    def update(self):
        for entity_id, removed_components in self.__removed.items():
            for removed_c in removed_components:
                self._components[entity_id].pop(type(removed_c))

        for entity_id, added_components in self.__added.items():
            for added_c in added_components:
                self._components.setdefault(entity_id, {}).setdefault(type(added_c), added_c)

    def add_component(self, component_type, entity_id, *args, **kwargs):
        component = component_type(*args, **kwargs)
        self.__added.setdefault(entity_id, set()).add(component)

    def remove_component(self, entity_id, component_id):
        self.__removed.setdefault(entity_id, set()).add(component_id)

    def get_entity_components(self, entity_id):
        return self._components[entity_id]


class Velocity(Component):
    def __init__(self, velocity=(0, 0)):
        super().__init__()
        self.velocity = velocity

    def set_velocity(self, velocity):
        self.velocity = velocity


class Position(Component):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.position = position

    def set_position(self, position):
        self.position = position


class Render(Component):
    def __init__(self, radius, width):
        super().__init__()
        self.radius = radius
        self.width = width


class God(Component):
    pass
