import pygame

import events
from events import key, mouse
from exceptions import QuitException


def is_quit_event(event):
    is_quit = event.type == pygame.QUIT
    is_esc = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    return is_quit or is_esc


def handle_event(event):
    if is_quit_event(event):
        raise QuitException
    elif events.key.is_key_event(event):
        events.key.handle_event(event)
    elif events.mouse.is_mouse_event(event):
        events.mouse.handle_event(event)
    else:
        pass


def update():
    key.update()
    mouse.update()
    for event in pygame.event.get():
        handle_event(event)
