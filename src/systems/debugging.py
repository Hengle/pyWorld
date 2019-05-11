import pygame

import colors
import components
from core import World
from managers import mappers
from .system import System


class Debugging(System):
    def __init__(self, world: World):
        required_components = {
            components.Debug
        }
        super().__init__(
            world,
            required_components
        )

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 5)

    def update_entity(self, entity_id, entity_components: mappers.ComponentMap):
        debug = entity_components[components.Debug]
        position = entity_components[components.Position]

        if position:
            surfaces = [self.make_font_surface(line) for line in debug.lines]
            for surface in surfaces:
                surface.get_rect()

        debug.lines = []

    def make_font_surface(self, line) -> pygame.Surface:
        return self.font.render(
            f"{line[0]}:->{line[1]}",
            colors.red,
            False
        )
