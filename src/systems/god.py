import pygame

import components
import events
from world import World
from .system import System


class God(System):

    def __init__(self, world: World):
        required = {
            components.God
        }
        super().__init__(world, required)
        self.m1_clicked = False

    def update_entity(self, entity_id, entity_components):
        position = entity_components[components.Position]
        position.position = pygame.mouse.get_pos()

        if events.mouse.is_m1_pressed():
            bot_entity = self.world.entity_manager.create_entity()
            self.world.component_manager.add_component(bot_entity, components.Brain)
            self.world.component_manager.add_component(bot_entity, components.Position, pygame.mouse.get_pos())
            self.world.component_manager.add_component(bot_entity, components.Render, 20, 1)
