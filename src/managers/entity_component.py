from typing import Type

import colors
import components
import shapes
from managers import mappers


def _has_components(required_components, existing_components):
    subset = [i for i in required_components if i in existing_components]
    return len(subset) > 0


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
        return entity_id

    def get_items(self, required_components=None):
        world_entities = self._entity_components.items()
        if required_components is not None:
            remaining = {entity_id: entity_components for (entity_id, entity_components) in world_entities if
                         _has_components(required_components, entity_components)}
            world_entities = remaining.items()

        return world_entities

    def create_bot(self, position, radius=15):
        bot_id = self.create_entity()
        self.create_component(bot_id, components.Brain)
        self.create_component(bot_id, components.Position, position=position)
        self.create_component(bot_id, components.Render, shapes.Circle(color=colors.red, radius=radius))
        self.create_component(bot_id, components.Boundary, radius=radius)
        self.create_component(bot_id, components.Vision, radius=(radius * 8))
        self.create_component(bot_id, components.Log, bot_id)
        return bot_id

    def create_food(self, position):
        food_id = self.create_entity()
        self.create_component(food_id, components.Food)
        self.create_component(food_id, components.Position, position=position)
        self.create_component(food_id, components.Render, shapes.Rectangle(color=colors.green, size=(8, 8)))
        return food_id
