import random

import pygame

import physics
from managers import entity_manager


class World:
    def __init__(self, surface: pygame.Surface):

        self.surface: pygame.Surface = surface
        self.ec_manager: entity_manager.EntityManager = entity_manager.EntityManager()
        self.is_debug = True
        self.delta_time = 0

        # make god
        self.ec_manager.create_god()

        self.ec_manager.create_bot(self.get_random_location())
        for i in range(0, 10):
            self.ec_manager.create_food(self.get_random_location())

    def log_text(self, entity_id, key, value):
        if not self.is_debug:
            return
        from components.component.log import Log
        log = self.ec_manager.get_entity_components(entity_id)[Log]
        if log:
            log.text[key] = value

    def log_line(self, entity_id, key, color, start_position, end_position):
        if not self.is_debug:
            return
        from components.component.log import Log
        import shapes
        log = self.ec_manager.get_entity_components(entity_id)[Log]

        log.drawables[f"line:{key}"] = lambda surface: shapes.Line.render_static(surface,
                                                                                 color,
                                                                                 start_position,
                                                                                 end_position)

    def log_circle(self, entity_id, key, color, position, radius):
        if not self.is_debug:
            return
        from components.component.log import Log
        import shapes
        log = self.ec_manager.get_entity_components(entity_id)[Log]
        log.drawables[f"circle:{key}"] = lambda surface: shapes.Circle.render_static(surface,
                                                                                     color,
                                                                                     position,
                                                                                     radius)

    def get_random_location(self):
        max_x, max_y = self.surface.get_size()
        random_x, random_y = random.randint(0, max_x), random.randint(0, max_y)
        return physics.Point(random_x, random_y)
