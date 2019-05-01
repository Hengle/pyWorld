import typing

import pygame

import colors
from . import base_entity


class God(base_entity.DrawableEntity):
    position: typing.Tuple

    def logic(self, delta_time):
        self.position = pygame.mouse.get_pos()

    def draw(self, surface):
        pygame.draw.circle(surface, colors.red, self.position, 20, 1)
