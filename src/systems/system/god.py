import pygame

import events
from components import component
from core import World
from systems import System


class God(System):

    def __init__(self, world: World):
        required_components = {
            component.God
        }
        super().__init__(world, required_components)

        self.m1_clicked = False
        self.is_random = False

    def update_entity(self, entity_id, entity_components):
        position = entity_components[component.Position]
        position.point = pygame.mouse.get_pos()

        if events.key.is_key_pressed(pygame.K_r):
            self.is_random = not self.is_random
            if self.is_random:
                print("Random location is now on")
            else:
                print("Random location is now off")

        if self.is_random:
            new_entity_position = self._world.get_random_location()
        else:
            new_entity_position = pygame.mouse.get_pos()

        # if events.mouse.is_m1_pressed():
        if events.key.is_key_pressed(pygame.K_b):
            bot_id = self._world.ec_manager.create_bot(new_entity_position)
            self._world.log_text(bot_id, "bot_id", bot_id)

        if events.key.is_key_pressed(pygame.K_f):
            food_id = self._world.ec_manager.create_food(new_entity_position)
