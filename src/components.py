from typing import Dict, Set


class Component(object):
    def __init__(self):
        self.identifier = id(self)


class ComponentManager:
    def __init__(self):
        self._components: Dict[int, Dict] = {}

        self.__added: Dict[int, Set] = {}
        self.__removed: Dict[int, Set] = {}

    def update(self):
        for entity_id, removed_components in self.__removed.items():
            for removed_c in removed_components:
                self._components[entity_id].pop(type(removed_c))

        for entity_id, added_components in self.__added.items():
            for added_c in added_components:
                self._components.setdefault(entity_id, {}).setdefault(type(added_c), added_c)

    def add_component(self, entity_id, component_type, *args, **kwargs):
        component = component_type(*args, **kwargs)
        self.__added.setdefault(entity_id, set()).add(component)

    def remove_component(self, entity_id, component_id):
        self.__removed.setdefault(entity_id, set()).add(component_id)

    def get_entity_components(self, entity_id):
        return self._components[entity_id]


class Acceleration(Component):
    def __init__(self, acceleration=0, max_velocity=0):
        super().__init__()
        self.acceleration = acceleration
        self.max_velocity = max_velocity


class Velocity(Component):
    def __init__(self, velocity=(0, 0)):
        super().__init__()
        self.velocity = velocity

    def __getitem__(self, item):
        if item > 1:
            return None
        return self.velocity[item]

    def set_velocity(self, velocity):
        self.velocity = velocity


class Position(Component):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.position = position

    def __getitem__(self, item):
        if item > 1:
            return None
        return self.position[item]

    def get_as_int(self):
        return int(self.position[0]), int(self.position[1])

    def set_position(self, position):
        self.position = position


class Render(Component):
    def __init__(self, radius=0, width=0):
        super().__init__()
        self.radius = radius
        self.width = width


class God(Component):
    pass


class AI(Component):
    def __init__(self, max_velocity=(0, 0)):
        super().__init__()
        self.max_velocity = max_velocity
