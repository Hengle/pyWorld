from typing import Set

import pygame

pressed: Set = set()
held: Set = set()


def is_key_pressed(key_code):
    return key_code in pressed


def is_key_held(key_code):
    return key_code in held


def update():
    for key in pressed:
        held.add(key)
    pressed.clear()


def handle_event(event: pygame.event.Event):
    key = event.key
    if is_key_down(event):
        pressed.add(key)
    elif is_key_up(event):
        if key in pressed:
            pressed.remove(key)
        else:
            held.remove(key)


def is_key_up(event: pygame.event.Event):
    return event.type == pygame.KEYUP


def is_key_down(event: pygame.event.Event):
    return event.type == pygame.KEYDOWN


def is_key_event(event: pygame.event.Event):
    return event.type in {pygame.KEYUP,
                          pygame.KEYDOWN}
