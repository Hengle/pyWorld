from typing import Type

import colors
import components
from managers import mappers


class EntityComponentManager:

    def __init__(self):
        self._entity_components = mappers.EntityComponentMap()

    def create_component(self, entity_id, component_type: Type[components.C_T], *args, **kwargs) -> components.C_T:
        component = self.get_entity_components(entity_id)[component_type]
        if not component:
            component = component_type(*args, **kwargs)
            self._entity_components.add_component(entity_id, component)
        return component

    def remove_component(self, entity_id, component_type: Type[components.Component]):
        del self._entity_components[entity_id][component_type]

    def get_entity_components(self, entity_id) -> mappers.ComponentMap:
        return self._entity_components[entity_id]

    def create_entity(self) -> str:
        entity_id = self._entity_components.create_entity()
        self.create_component(entity_id, components.Debug)
        return entity_id

    def get_items(self):
        return self._entity_components.items()

    def create_bot(self, position):
        bot_id = self.create_entity()
        self.create_component(bot_id, components.Brain)
        self.create_component(bot_id, components.Position, position)
        self.create_component(bot_id, components.Render)
        return bot_id

    def create_food(self, position):
        food_id = self.create_entity()
        self.create_component(food_id, components.Food)
        self.create_component(food_id, components.Position, position)
        self.create_component(food_id, components.Render)
        self.create_component(food_id, components.ShapeSquare, 8, colors.green)
        return food_id
