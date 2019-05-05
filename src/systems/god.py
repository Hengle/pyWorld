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
        position: components.Position = entity_components[components.Position]
        position.set_position(pygame.mouse.get_pos())

        if 1 in events.mouse.held:
            bot_entity = self.world.entity_manager.create_entity()
            self.world.component_manager.add_component(bot_entity, components.AI)
            self.world.component_manager.add_component(bot_entity, components.Position, position)
            self.world.component_manager.add_component(bot_entity, components.Velocity, (2, 2))
            self.world.component_manager.add_component(bot_entity, components.Render, 20, 1)
            self.world.component_manager.add_component(bot_entity, components.Acceleration, 0.1, 2)
