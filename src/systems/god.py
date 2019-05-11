import pygame

import components
import events
from core import World
from .system import System


class God(System):

    def __init__(self, world: World):
        required_components = {
            components.God
        }
        super().__init__(world, required_components)

        self.m1_clicked = False

    def update_entity(self, entity_id, entity_components):
        position = entity_components[components.Position]
        position.vector = pygame.mouse.get_pos()

        if events.mouse.is_m1_pressed():
            bot_entity = self._world.ec_manager.create_entity()
            self._world.ec_manager.create_component(bot_entity, components.Brain)
            self._world.ec_manager.create_component(bot_entity, components.Position, pygame.mouse.get_pos())
            self._world.ec_manager.create_component(bot_entity, components.Render)
