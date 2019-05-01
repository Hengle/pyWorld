import pygame

from exceptions import QuitException


class EventManager:

    @staticmethod
    def is_key_event(event):
        return event.type in [pygame.KEYUP, pygame.KEYDOWN]

    @staticmethod
    def is_mouse_event(event):
        return event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL]

    @staticmethod
    def is_quit_event(event):
        return event.type == pygame.QUIT

    @staticmethod
    def handle_key_event(event):
        key_dict = event.dict
        if key_dict['key'] == pygame.K_ESCAPE:
            raise QuitException

    def handle_event(self, event):
        if self.is_quit_event(event):
            raise QuitException
        elif self.is_key_event(event):
            self.handle_key_event(event)
        elif self.is_mouse_event(event):
            pass
        else:
            pass

    def update(self):
        for event in pygame.event.get():
            self.handle_event(event)
