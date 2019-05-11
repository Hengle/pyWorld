import random

import pygame


class World:
    def __init__(self, surface: pygame.Surface):
        import managers
        from components import God, Position, Render, ShapeCircle

        self.surface: pygame.Surface = surface
        self.ec_manager: managers.EntityComponentManager = managers.EntityComponentManager()
        self.is_debug = True

        # make god
        god = self.ec_manager.create_entity()

        self.ec_manager.create_component(god, God)
        self.ec_manager.create_component(god, Position)
        self.ec_manager.create_component(god, Render)
        self.ec_manager.create_component(god, ShapeCircle, 20, pygame.color.THECOLORS['darkred'])

    def log_line(self, entity_id, key, value):
        if not self.is_debug:
            return
        from components.debug import Debug
        debug = self.ec_manager.get_entity_components(entity_id)[Debug]
        if debug:
            debug.lines[key] = value

    def get_random_location(self):
        max_x, max_y = self.surface.get_size()
        return random.randint(0, max_x), random.randint(0, max_y)
