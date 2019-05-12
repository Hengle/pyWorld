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
            components.Log
        }
        super().__init__(
            world,
            required_components
        )

        self.is_debug = True

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

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
        debug = entity_components[components.Log]
        if not debug.text or len(debug.text) == 1:
            return
        position = entity_components[components.Position]
        text = debug.text.copy()
        drawables = debug.drawables.copy()
        debug.clear()
        if position:
            self._draw_text_on_position(text, position)

        self._draw_drawables(drawables)

    def _draw_drawables(self, drawables):
        for key, drawable in drawables.items():
            drawable(self._world.surface)

    def _draw_text_on_position(self, text, position):
        # print(lines)
        surface_position_map = {}
        next_position = position.point.as_int_tuple()
        for text_key, text_value in text.items():
            surface = self._key_value_text_surface(text_key, text_value)
            surface_position_map[surface] = next_position, next_position
            surface_rect = surface.get_rect()
            next_position = next_position[0], next_position[1] + surface_rect.height

        for surface, position in surface_position_map.items():
            self._world.surface.blit(surface, position)

    def _key_value_text_surface(self, key, value) -> pygame.Surface:
        return self.font.render(
            f"{key}:->{value}",
            False,
            colors.red
        )
