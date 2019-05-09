import pygame

import components
import managers


class World:
    def __init__(self, surface: pygame.Surface):
        self.surface: pygame.Surface = surface
        self.entity_manager: managers.EntityManager = managers.EntityManager()
        self.component_manager: managers.ComponentManager = managers.ComponentManager()

        # make god
        god = self.entity_manager.create_entity()

        self.component_manager.add_component(god, components.God)
        self.component_manager.add_component(god, components.Position)
        self.component_manager.add_component(god, components.Render)
        self.component_manager.add_component(god, components.ShapeCircle, 20, pygame.color.THECOLORS['darkred'])
