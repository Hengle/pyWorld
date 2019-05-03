import pygame

import events
from events import key, mouse
from exceptions import QuitException


def is_quit_event(event):
    key_dict = event.dict
    return event.type == pygame.QUIT or (key_dict is not None and key_dict.get('key') == pygame.K_ESCAPE)


def handle_event(event):
    if is_quit_event(event):
        raise QuitException
    elif events.key.is_key_event(event):
        events.key.handle_event(event)
    elif events.mouse.is_mouse_event(event):
        events.mouse.handle_mouse_event(event)
    else:
        pass


def update():
    for event in pygame.event.get():
        handle_event(event)
