from typing import Set

import pygame
from pygame.event import Event

keys_pressed: Set = set()
keys_held: Set = set()
keys_released: Set = set()


def update():
    keys_held.add


def handle_event(event: Event):
    global keys_pressed
    global keys_held
    global keys_released

    event_key = event.key

    if is_key_down(event):
        if event_key in keys_pressed:
            keys_pressed.remove(event_key)
            keys_held.add(event_key)
        else:
            keys_pressed.add(event_key)
    elif is_key_up(event):
        if event_key in keys_pressed:
            keys_pressed.remove(event_key)
        elif event_key in keys_held:
            keys_held.remove(event_key)
        keys_released.add(event_key)

    print(f"[{keys_pressed}] [{keys_held}] [{keys_released}]")


def is_key_up(event):
    return event.type == pygame.KEYUP


def is_key_down(event):
    return event.type == pygame.KEYDOWN


def is_key_event(event: pygame.event.Event):
    return event.type in {pygame.KEYUP,
                          pygame.KEYDOWN}
