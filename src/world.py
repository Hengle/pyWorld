import pygame

import components
import entities


class World:
    def __init__(self, surface: pygame.Surface):
        self.surface: pygame.Surface = surface
        self.entity_manager: entities.EntityManager = entities.EntityManager()
        self.component_manager: components.ComponentManager = components.ComponentManager()

        # make god
        god = self.entity_manager.create_entity()

        self.component_manager.add_component(god, components.God)
        self.component_manager.add_component(god, components.Position)
        self.component_manager.add_component(god, components.Render, radius=15, width=1)

    def update(self):
        self.entity_manager.update()
        self.component_manager.update()
