import pygame

import events
import systems
import world


class WorldEngine:
    surface: pygame.Surface
    clock: pygame.time.Clock
    max_frame_rate = 60
    delta_time = 0

    def __init__(self, size):
        pygame.init()
        pygame.display.set_caption("pyWorld", "pyWorld")

        self.surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.world = world.World(self.surface)
        self.event_manager = events.EventManager()
        self.system_manager = systems.SystemManager(self.world)
        self.is_running = True

    def tick_clock(self):
        self.delta_time = self.clock.tick(self.max_frame_rate)

    def run(self):
        while self.is_running:
            self.tick_clock()

            self.surface.fill(pygame.color.THECOLORS['gray50'])

            self.event_manager.update()
            self.world.update()
            self.system_manager.update()

            pygame.display.flip()
