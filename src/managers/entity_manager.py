from typing import Type

import pygame

import colors
import maps
import shapes
from components import C_T, Component


def _has_components(required_components, existing_components):
    subset = [i for i in required_components if i in existing_components]
    return len(subset) > 0


class EntityManager:

    def __init__(self):
        self._entity_components = maps.EntityComponentMap()

    def create_component(self, entity_id, component_type: Type[C_T], *args, **kwargs) -> C_T:
        component = self.get_entity_components(entity_id)[component_type]
        if not component:
            component = component_type(*args, **kwargs)
            self._entity_components.add_component(entity_id, component)
        return component

    def remove_component(self, entity_id, component_type: Type[Component]):
        del self._entity_components[entity_id][component_type]

    def get_entity_components(self, entity_id) -> maps.ComponentMap:
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
        from components import component
        bot_id = self.create_entity()
        self.create_component(bot_id, component.Brain)
        self.create_component(bot_id, component.Position, position=position)
        self.create_component(bot_id, component.Render, shapes.Circle(color=colors.red, radius=radius))
        self.create_component(bot_id, component.Boundary, radius=radius)
        self.create_component(bot_id, component.Vision, radius=(radius * 8))
        self.create_component(bot_id, component.Log, bot_id)
        return bot_id

    def create_food(self, position):
        from components import component
        food_id = self.create_entity()
        self.create_component(food_id, component.Food)
        self.create_component(food_id, component.Position, position=position)
        self.create_component(food_id, component.Render, shapes.Rectangle(color=colors.green, size=(8, 8)))
        return food_id

    def create_god(self):
        from components import component
        god_id = self.create_entity()

        self.create_component(god_id, component.God)
        self.create_component(god_id, component.Position)
        self.create_component(god_id, component.Render,
                              shapes.Circle(color=pygame.color.THECOLORS['darkred'], radius=20))
        return god_id
