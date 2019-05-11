import pygame

import colors
import components
import events.events
import events.key
from core import World
from managers import mappers
from .system import System


class Logging(System):
    def __init__(self, world: World):
        required_components = {
            components.Debug
        }
        super().__init__(
            world,
            required_components
        )

        self.is_debug = True

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 5)

    def update(self):
        if events.key.is_key_pressed(pygame.K_d):
            self.is_debug = not self.is_debug
            if self.is_debug:
                print("Debug is now on")
            else:
                print("Debug is now off")
        if not self.is_debug:
            return
        super().update()

    def update_entity(self, entity_id, entity_components: mappers.ComponentMap):
        debug = entity_components[components.Debug]
        if not debug.lines:
            return
        lines = debug.lines.copy()
        # debug.lines.clear()

        print(lines)

        position = entity_components[components.Position]

        suface_position = {}

        if position:
            surfaces = [self.make_font_surface(line) for line in lines.items()]
            for surface in surfaces:
                surface.get_rect()

    def make_font_surface(self, line) -> pygame.Surface:
        return self.font.render(
            f"{line[0]}:->{line[1]}",
            False,
            colors.red
        )
