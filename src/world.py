from typing import KeysView

import pygame

import components
import entities


class World:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self._entity_manager = entities.EntityManager()
        self._component_manager = components.ComponentManager()

        # make god
        god = self._entity_manager.create_entity()

        self._component_manager.add_component(components.God, god)
        self._component_manager.add_component(components.Position, god)
        self._component_manager.add_component(components.Render, god, radius=15, width=1)

    def update(self):
        self._entity_manager.update()
        self._component_manager.update()

    def get_entities(self) -> KeysView:
        return self._entity_manager.get_entities()

    def get_entity_components(self, entity_id):
        return self._component_manager.get_entity_components(entity_id)
