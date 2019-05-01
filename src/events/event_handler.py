import pygame

from events import input_handler
from exceptions import QuitException


def is_key_event(event):
    return event.type in [pygame.KEYUP, pygame.KEYDOWN]


def is_mouse_event(event):
    return event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL]


def is_quit_event(event):
    return event.type == pygame.QUIT


def handle_event(event):
    if is_quit_event(event):
        raise QuitException
    elif is_key_event(event):
        input_handler.handle_event(event)
    elif is_mouse_event(event):
        pass
    else:
        pass
