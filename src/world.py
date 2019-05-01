import typing

import pygame

import entities
import events.event_handler
from entities import god


class WorldEngine:
    surface: pygame.Surface
    clock: pygame.time.Clock
    max_frame_rate = 60
    delta_time = 0
    entities: typing.List[entities.Entity]

    def __init__(self, size):
        pygame.init()
        pygame.display.set_caption("pyWorld", "pyWorld")

        self.surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.entities = []

        self.entities.append(god.God())

        self.is_running = True

    def tick_clock(self):
        self.delta_time = self.clock.tick(self.max_frame_rate)

    def handle_draw(self):
        self.surface.fill(pygame.color.THECOLORS['darkgray'])

        for entity in self.entities:
            if isinstance(entity, entities.DrawableEntity):
                entity.draw(self.surface)

        pygame.display.flip()

    def handle_logic(self):
        for entity in self.entities:
            entity.logic(self.delta_time)

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            events.event_handler.handle_event(event)

    def run(self):
        while self.is_running:
            self.tick_clock()

            self.handle_events()
            self.handle_logic()
            self.handle_draw()
